# MATH 565 slide conventions

Follow the authoritative shared
[`classlib` slide style guide](../classlib/docs/slide-style.md),
[`classlib` agent guidance](../classlib/AGENTS.md), and shared
[`classlib` diagram guide](../classlib/docs/revealjs-diagram-construction.md).
This document records only MATH 565 deck architecture, terminology, notation,
local components, migration policy, and intentional exceptions.

## Course Map and deck navigation

Each MATH 565 deck follows this opening sequence:

1. The generated title slide identifies the course and deck and gives its
   principal textbook or overarching reference in title-slide metadata.
2. `# Course Map` uses the following navigation elements:
   - **Course decks** lists every deck in course order and marks the current
     deck with the emphasis specified below.
   - **This deck** (Decks 02–05) or **In this deck** (Deck 01) links every
     instructional `#` section in presentation order, repeating its
     capitalization and punctuation exactly.
3. The instructional sections follow the shared section-outline convention.

Follow the [shared Course Map theme convention](../classlib/docs/slide-style.md#course-map-themes).
MATH 565 uses 36% for Course decks, a 4% empty gutter, and 60% for the
right-hand theme area. Center phrase-only themes at `1.5em`;
Introduction uses a 🎬 clapperboard beside `[Teaser Trailer]{.alert}`.

Decks 02–05 use a whole-deck MC tree on the lower right of the Course Map,
with named `deck-02-overview` through `deck-05-overview` presets in
`slides/tree-markers.yml`. Select existing tree labels from the deck's actual
substantive content, including foundational subjects and developed applications;
omit passing mentions (for example, finance in Decks 03 and 05). Do not simply
collect the small navigation-marker presets or introduce new tree topics.
The upper row retains the 36% / 4% / 60% course-list and theme proportions.
The current deck link uses `.current-deck` and `aria-current="page"`, with
blue color, bold weight, and 110% font size. Section links move to the lower
left under **This deck**. Per instructor preference, omit the separate **In this deck** heading above the theme in
these four maps; this is a local exception to the shared theme-heading
convention. The `.deck-course-map` layout reserves the lower right for a
42%-wide tree, compared with the 16% navigation trees. Preserve readable labels, the theme, all links, and footer
clearance when changing either a map or its topic selection. Deck 01 retains
its existing Course Map and full introductory tree.

Use raw `<h3>` elements for the Course Map column labels so they do not change
RevealJS hierarchy. Register every deck in `slides/_metadata.yml` with its
file, full title, and short footer title. Each deck supplies `deck-nav-meta`
from adjacent entries; the first has no previous target and the last has no
next target.

## Cumulative terms index

Maintain the cumulative **Terms to Know** index in Deck 01. After completing
or substantially revising a deck, add important terms alphabetically and link
each to the slide where it first receives substantial treatment. Do not link a
mere first mention or an undeveloped topic. Keep alphabetical ranges and the
Deck 01 Course Map synchronized.

## MATH 565 terminology and notation

- Use zero-based indexing for samples, observations, Markov-chain states, and
  low discrepancy sequences: a sample of size $n$ is indexed from $0$ through
  $n-1$.
- Keep coordinate indices $1,\ldots,d$ and multilevel indices
  $1,\ldots,L$ one-based.
- Keep notation consistent with the shared macro registry and course
  notebooks.
- Keep the [uniform-input, target-sample, and output roles](../AUTHOR_WORKFLOW.md#course-wide-simulation-notation)
  visible when explaining a sampling method. Use `[target]{.alert}` at its
  first definition and key conclusions, with selective reinforcement in
  examples. Keep proposal and target roles distinct; do not highlight every
  occurrence mechanically.

## Course-wide styling

The shared `hickernell-slides.scss` theme remains authoritative. Put a genuine
MATH 565-wide addition in `slides/math565-slides.scss`, loaded through
`slides/_metadata.yml`. Use deck-specific CSS only for a one-deck exception.

## Course tree markers

MATH 565 tree variants are named in `slides/tree-markers.yml`. Shared defaults
belong under `defaults`; entries under `markers` select groups, labels,
headings, or masks for one teaching context.

Add a preset using `.tree-marker-slide` and `tree-marker`:

```markdown
## Random variables and distributions {.tree-marker-slide tree-marker="probability"}
```

Use tree markers on major-section (`#`) and regular slide (`##`) headings.
Continuation slides created with `---`, including those with a visible `###`
subheading, intentionally omit the navigation tree. Do not add an empty or
hidden heading solely to place a tree on a continuation slide. If a future
request would add one, remind the author of this convention before making the
change.

The `tree-marker.lua` filter resolves the preset and stops on an unknown name.
Add or tune presets rather than copying full rendering calls. Position the
marker element rather than changing RevealJS's slide positioning model.

Published deck HTML lives under `_site/slides/`, while shared tree assets live
under `_site/classlib/`. Tree renderers and presets must therefore use
`../classlib/classlib/quarto/components/trees` as `asset_base_url`.

### Deck 02 marker selections

Generating Samples develops Probability, Analysis (inverse transforms and
Jacobians), Linear Algebra (Cholesky and PCA), random-number generation,
Pseudorandom Numbers, Low Discrepancy sampling, and Quantitative Finance.
It previews discrepancy measures without defining them and does not develop
statistical estimation. Its overview therefore omits Discrepancy Measures,
Statistics, and Estimation. Use `low-discrepancy-sampling` for its small trees,
and `random-generation` for its Big Ideas slide. Decks 03–04 develop the
actual discrepancy formulas and may use the combined marker.

### Deck 03 marker selections

Use the existing MCMC label for Metropolis--Hastings algorithms and add
Probability for invariance arguments, Statistics for diagnostics, or Practice
for worked experiments. Use Discrepancy Measures for general MMD/KL/KSD
comparisons; reserve the combined Low Discrepancy marker for the centered
QMC discrepancy material. Use Analysis for kernel/RKHS foundations and
Error Assessment for the integration-error section, worst-case bounds, the
discrepancy identity, and Gaussian-process RMSE. Avoid combining adjacent
labels when they overlap at marker size.

Bayesian applications use Bayesian Computation, MCMC, and Statistics;
likelihood uses Statistical Inference and Estimation. Queueing uses Probability
and Practice: event-driven Markov-system simulation does not by itself make
it an MCMC sampler. These are selections from the existing MC tree, not new
overall-tree labels. Continuations retain the no-marker convention above.
Full-width comparison tables omit markers to keep their header rows
unobscured; their section or parent slide supplies the navigation context.

## Shared references

MATH 565 loads `hickernell-texts.yml` and `hickernell-papers.yml` through
`../classlib/classlib/quarto/slides/hickernell-slides.yml`. Use their metadata
shortcodes rather than repeating citation text or publisher URLs.

## Calendar dates

Format calendar dates on slides as a three-letter English month abbreviation
followed by an unpadded day, such as `Sep 15`. Do not use numeric month/day
forms such as `9/15` or full month names such as `September 15`.

## Fall 2025 conversion policy

Use the corresponding Fall 2025 Keynote deck as the initial content and
pedagogical reference. Preserve its mathematical substance, examples,
sequence, and emphasis before intentional instructor-review changes.

Do not carry forward Fall 2025 logistics. Remove or replace obsolete homework,
assignment, test, announcement, feedback, and dated-event references.

## Local exceptions

MATH 565 currently has no general exception to the shared RevealJS visual
language. Record a future exception here only when it should not apply to
other consumers.
