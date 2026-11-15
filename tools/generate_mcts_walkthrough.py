"""Build the fixed-layout SVGs for Deck 05's constructed MCTS trace.

Run with the qmcpy Python environment from any directory. The tree is a
four-decision teaching example, not an output of the six-segment notebook.
Each figure shares the same coordinate system; rollout nodes are never
silently converted into stored nodes. Only explicit expansions store a node.
"""

from copy import deepcopy
from html import escape
from math import log, sqrt
from pathlib import Path


OUTPUT = Path(__file__).resolve().parents[1] / "slides/assets/mcts"
BLUE, GOLD, GREEN, RED, GRAY = (
    "#1f5a91", "#9a6509", "#216b56", "#ac3543", "#61717a"
)
POSITIONS = {
    "root": (360, 70), "A": (150, 200), "B": (535, 200),
    "A0": (150, 330), "A01": (150, 460), "A010": (150, 590),
    "B0": (420, 330), "B1": (660, 330),
    "B01": (420, 460), "B010": (420, 590),
    "B10": (660, 460), "B100": (660, 590),
}


def uct(tree, parent, child):
    w, n = tree[child]
    return w / n + sqrt(log(tree[parent][1]) / n)


def choose(tree, parent, children):
    return max(children, key=lambda child: uct(tree, parent, child))


def back_up(tree, path, result):
    for node in path:
        tree[node][0] += result
        tree[node][1] += 1


def parent_of(node):
    return "root" if len(node) == 1 else node[:-1]


def text(x, y, content, size=26, color=GRAY):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">'
        f'{escape(content)}</text>'
    )


def edge(parent, child, color=GRAY, dashed=False, reverse=False):
    x1, y1 = POSITIONS[parent]
    x2, y2 = POSITIONS[child]
    # Rectangle intersections: each node is 190 wide and 76 high.
    dx, dy = x2 - x1, y2 - y1
    t = min(95 / abs(dx) if dx else 1, 38 / abs(dy))
    start, end = (x1 + t * dx, y1 + t * dy), (x2 - t * dx, y2 - t * dy)
    if reverse:
        start, end = end, start
    dash = ' stroke-dasharray="9 7"' if dashed else ""
    marker = {BLUE: "blue", GOLD: "gold", GREEN: "green", RED: "red", GRAY: "gray"}[color]
    return (
        f'<path d="M{start[0]:.1f} {start[1]:.1f} L{end[0]:.1f} {end[1]:.1f}" '
        f'fill="none" stroke="{color}" stroke-width="4"{dash} '
        f'marker-end="url(#{marker})"/>'
    )


def figure(name, title, tree, *, selected=(), new=None, rollout=(),
           result=None, minutes=None, updated=(), before=None, collapsed=True):
    description = (
        title + ". Stored labels give successes W / visits N. "
        + "; ".join(f"{node}: {w}/{n}" for node, (w, n) in tree.items())
        + ". Solid edges belong to the stored tree; dashed edges are sampled "
        "continuations only. A's stored descendants are collapsed when shown."
    )
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 690" '
        'role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">{escape(description)}</desc>', '<defs>',
    ]
    for key, color in (("blue", BLUE), ("gold", GOLD), ("green", GREEN),
                       ("red", RED), ("gray", GRAY)):
        svg.append(
            f'<marker id="{key}" viewBox="0 0 10 10" refX="10" refY="5" '
            'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 Z" fill="{color}"/></marker>'
        )
    svg.extend(['</defs>', '<g font-family="Arial, sans-serif" text-anchor="middle">'])
    for node in tree:
        if node == "root":
            continue
        parent = parent_of(node)
        color = GOLD if node in selected else BLUE
        if node == new:
            color = GREEN
        if node in updated:
            color = GOLD
        svg.append(edge(parent, node, color, reverse=node in updated))
    for node in rollout:
        svg.append(edge(parent_of(node), node, GRAY, dashed=True))
    if collapsed and "A" in tree:
        svg.append('<path d="M150 238 L80 355 L220 355 Z" '
                   'fill="#eef2f6" stroke="#61717a" stroke-width="2"/>')
        svg.append(text(150, 390, "Stored subtree", 25))
        svg.append(text(150, 422, "details hidden", 24))
    for node, stats in tree.items():
        x, y = POSITIONS[node]
        color = GOLD if node in selected or node in updated else BLUE
        fill = "#fff7e7" if color == GOLD else "white"
        if node == new:
            color, fill = GREEN, "#edf8f2"
        svg.append(f'<rect x="{x - 95}" y="{y - 38}" width="190" height="76" '
                   f'rx="12" fill="{fill}" stroke="{color}" stroke-width="3"/>')
        label = "Start" if node == "root" else "–".join(node)
        svg.append(text(x, y - 5, label, 29, color))
        count = f"{stats[0]} / {stats[1]}"
        if node in updated and before is not None:
            old = before.get(node, [0, 0])
            count = f"{old[0]}/{old[1]} → {stats[0]}/{stats[1]}"
        svg.append(text(x, y + 25, count, 25, color))
    for node in rollout:
        x, y = POSITIONS[node]
        svg.append(f'<rect x="{x - 95}" y="{y - 38}" width="190" height="76" '
                   'rx="12" fill="#f8fafb" stroke="#61717a" stroke-width="2" '
                   'stroke-dasharray="9 7"/>')
        svg.append(text(x, y - 5, "–".join(node), 27))
        svg.append(text(x, y + 25, "sampled only", 23))
    if "B" in tree and "B0" not in tree and not rollout:
        svg.append(text(535, 300, "Next choices: 0 or 1", 24))
        svg.append(text(535, 334, "neither stored yet", 24))
    elif "B0" in tree and "B1" not in tree:
        svg.append(text(660, 330, "1 untried", 24))
    if result is not None:
        color = GREEN if result else RED
        x = 150 if rollout and rollout[0].startswith("B") else 540
        svg.append(text(x, 515, f"T = {minutes} min", 28, color))
        svg.append(text(x, 554, f"{'On time' if result else 'Late'}: R = {result}", 28, color))
    svg.append(text(400, 660, "W / N = successes / visits", 25, BLUE))
    svg.append(text(400, 686, "Solid: stored tree · Dashed: rollout only", 23))
    svg.extend(['</g>', '</svg>'])
    (OUTPUT / f"walkthrough-{name}.svg").write_text("\n".join(svg) + "\n")


def main():
    tree = {"root": [0, 0]}
    figure("00-start", "Start with only the root stored", tree, collapsed=False)
    tree["A"] = [0, 0]
    back_up(tree, ("root", "A"), 1)
    figure("01-first", "First simulation: expand A, roll out and back up one", tree,
           rollout=("A0", "A01", "A010"), result=1, minutes=76, collapsed=False)
    tree["B"] = [0, 0]
    back_up(tree, ("root", "B"), 0)
    figure("02-second", "Second simulation: expand B, roll out and back up zero", tree,
           rollout=("B1", "B10", "B100"), result=0, minutes=86, collapsed=False)

    # Check the omitted warm-up trials too, then collapse A's descendants.
    full_tree = deepcopy(tree)
    for node, result in (("A0", 1), ("A1", 1), ("A00", 0), ("A10", 0)):
        assert choose(full_tree, "root", ("A", "B")) == "A"
        path = ["root", "A"]
        if len(node) == 3:
            assert choose(full_tree, "A", ("A0", "A1")) == node[:-1]
            path.append(node[:-1])
        assert node not in full_tree
        full_tree[node] = [0, 0]
        back_up(full_tree, (*path, node), result)
    tree = {node: full_tree[node] for node in ("root", "A", "B")}
    assert tree == {"root": [3, 6], "A": [3, 5], "B": [0, 1]}
    figure("03-snapshot", "After six simulations: A has three successes in five visits", tree)
    assert choose(tree, "root", ("A", "B")) == "B"
    figure("04-select", "Simulation seven: select the less-visited branch B", tree,
           selected=("B",))
    tree["B0"] = [0, 0]
    figure("05-expand", "Simulation seven: store the new child B zero", tree,
           selected=("B",), new="B0")
    figure("06-rollout", "Simulation seven: sample two remaining choices and on-time traffic", tree,
           selected=("B",), new="B0", rollout=("B01", "B010"), result=1, minutes=76)
    before = deepcopy(tree)
    back_up(tree, ("root", "B", "B0"), 1)
    figure("07-backup", "Simulation seven: back up one through B zero, B and Start", tree,
           updated=("root", "B", "B0"), before=before)

    assert choose(tree, "root", ("A", "B")) == "B"
    tree["B1"] = [0, 0]
    figure("08-failure-expand", "Simulation eight: select B and expand its untried child one", tree,
           selected=("B",), new="B1")
    figure("09-failure-rollout", "Simulation eight: the sampled trip is late", tree,
           selected=("B",), new="B1", rollout=("B10", "B100"), result=0, minutes=86)
    before = deepcopy(tree)
    back_up(tree, ("root", "B", "B1"), 0)
    figure("10-failure-backup", "Simulation eight: visits increase but successes do not", tree,
           updated=("root", "B", "B1"), before=before)

    assert choose(tree, "root", ("A", "B")) == "A"
    before = deepcopy(tree)
    back_up(tree, ("root", "A"), 0)
    figure("11-intervening", "Simulation nine visits the collapsed A subtree and returns zero", tree,
           selected=("A",), updated=("root", "A"), before=before)

    assert choose(tree, "root", ("A", "B")) == "B"
    assert choose(tree, "B", ("B0", "B1")) == "B0"
    figure("12-deeper-select", "Simulation ten: select B, then select its stored child B zero", tree,
           selected=("B", "B0"))
    tree["B01"] = [0, 0]
    figure("13-deeper-rollout", "Simulation ten: expand B zero one and roll out one final choice", tree,
           selected=("B", "B0"), new="B01", rollout=("B010",), result=1, minutes=78)
    before = deepcopy(tree)
    back_up(tree, ("root", "B", "B0", "B01"), 1)
    figure("14-deeper-backup", "Simulation ten: back up one along the longer stored path", tree,
           updated=("root", "B", "B0", "B01"), before=before)
    assert tree == {"root": [5, 10], "A": [3, 6], "B": [2, 4],
                    "B0": [2, 2], "B1": [0, 1], "B01": [1, 1]}
    assert choose(tree, "root", ("A", "B")) == "B"
    print("Generated 15 fixed-layout SVGs; UCT choices and backup totals verified")


if __name__ == "__main__":
    main()
