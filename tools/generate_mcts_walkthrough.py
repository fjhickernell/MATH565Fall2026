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
    "root": (500, 70), "A": (275, 200), "B": (750, 200),
    "A0": (155, 330), "A1": (395, 330),
    "A00": (75, 460), "A01": (235, 460), "A10": (395, 460),
    "A000": (75, 590), "A010": (235, 590), "A100": (395, 590),
    "B0": (625, 330), "B1": (875, 330),
    "B01": (625, 460), "B010": (625, 590),
    "B10": (875, 460), "B100": (875, 590),
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
    # Rectangle intersections: each node is 140 wide and 76 high.
    dx, dy = x2 - x1, y2 - y1
    t = min(70 / abs(dx) if dx else 1, 38 / abs(dy))
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


def figure(name, title, tree, *, new=None, rollout=(),
           result=None, minutes=None, updated=(), before=None):
    assert set(tree).isdisjoint(rollout), "Rollout-only nodes must not be stored"
    assert new is None or new in tree
    for node in (*tree, *rollout):
        assert node in POSITIONS
        assert node == "root" or parent_of(node) in (*tree, *rollout)
    description = (
        title + ". Stored labels give successes W / visits N. "
        + "; ".join(f"{node}: {w}/{n}" for node, (w, n) in tree.items())
        + ". Solid edges belong to the stored tree; dashed edges are sampled "
        "continuations only, discarded after the rollout. Every stored node "
        "in both A and B is shown. Green marks the one newly stored node."
    )
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 740" '
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
        color = GOLD if node in updated else BLUE
        svg.append(edge(parent, node, color, reverse=node in updated))
    for node in rollout:
        svg.append(edge(parent_of(node), node, GRAY, dashed=True))
    for node, stats in tree.items():
        x, y = POSITIONS[node]
        color = GOLD if node in updated else BLUE
        fill = "#fff7e7" if color == GOLD else "white"
        if node == new:
            color, fill = GREEN, "#edf8f2"
        svg.append(f'<rect x="{x - 70}" y="{y - 38}" width="140" height="76" '
                   f'rx="12" fill="{fill}" stroke="{color}" stroke-width="3"/>')
        label = "Start" if node == "root" else "–".join(node)
        svg.append(text(x, y - 5, label, 27, color))
        count = f"{stats[0]} / {stats[1]}"
        if node in updated and before is not None:
            old = before.get(node, [0, 0])
            count = f"{old[0]}/{old[1]}→{stats[0]}/{stats[1]}"
        svg.append(text(x, y + 25, count, 24, color))
    for node in rollout:
        x, y = POSITIONS[node]
        svg.append(f'<rect x="{x - 70}" y="{y - 38}" width="140" height="76" '
                   'rx="12" fill="#f8fafb" stroke="#61717a" stroke-width="2" '
                   'stroke-dasharray="9 7"/>')
        svg.append(text(x, y - 5, "–".join(node), 25))
        svg.append(text(x, y + 25, "sampled only", 20))
    if result is not None:
        color = GREEN if result else RED
        x = 190 if rollout and rollout[0].startswith("B") else 800
        svg.append(text(x, 55, f"T = {minutes} min", 27, color))
        svg.append(text(x, 90, f"{'On time' if result else 'Late'}: R = {result}", 27, color))
    svg.append(text(500, 690, "W(s) / N(s) = successes / visits · before → after backup", 24, BLUE))
    svg.append(text(500, 722, "Solid: keep · Dashed: discard · Green: new node · Gold: select / update", 23))
    svg.extend(['</g>', '</svg>'])
    (OUTPUT / f"walkthrough-{name}.svg").write_text("\n".join(svg) + "\n")


def main():
    tree = {"root": [0, 0]}
    figure("00-start", "Start with only the root stored", tree)
    # Each row specifies the expansion and one sampled full route and trip time.
    trace = (
        ("01-first", "A", "A010", 76),
        ("02-second", "B", "B100", 86),
        ("03a-third", "A0", "A010", 78),
        ("03b-fourth", "A1", "A100", 79),
        ("03c-fifth", "A00", "A000", 86),
        ("03d-sixth", "A10", "A100", 85),
        ("07-seventh", "B0", "B010", 76),
        ("08-eighth", "B1", "B100", 86),
        ("09-ninth", "A01", "A010", 84),
        ("10-tenth", "B01", "B010", 78),
    )
    for number, (name, node, route, minutes) in enumerate(trace, 1):
        path = ("root", *(node[:depth] for depth in range(1, len(node) + 1)))
        for parent, child in zip(path[:-2], path[1:-1]):
            children = ("A", "B") if parent == "root" else (parent + "0", parent + "1")
            assert all(candidate in tree for candidate in children)
            assert choose(tree, parent, children) == child

        assert node not in tree and path[-2] in tree
        assert route.startswith(node) and len(route) == 4
        rollout = tuple(route[:depth] for depth in range(len(node) + 1, len(route) + 1))
        result = int(minutes <= 80)
        before = deepcopy(tree)
        tree[node] = [0, 0]
        back_up(tree, path, result)
        figure(name, f"Iteration {number}: expand {'–'.join(node)}, roll out and back up {result}",
               tree, new=node, rollout=rollout, result=result, minutes=minutes,
               updated=path, before=before)

    assert tree == {"root": [5, 10], "A": [3, 6], "B": [2, 4],
                    "A0": [1, 3], "A1": [1, 2], "A00": [0, 1], "A10": [0, 1], "A01": [0, 1],
                    "B0": [2, 2], "B1": [0, 1], "B01": [1, 1]}
    assert len(tree) == 11, "Ten iterations store ten nodes, in addition to Start"
    assert choose(tree, "root", ("A", "B")) == "B"
    print("Generated the initial tree and one SVG per iteration. Verified UCT choices and final counts.")


if __name__ == "__main__":
    main()
