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

Close each deck with **Big Ideas** and **What Comes Next**. Starting with
Deck 03, place **How Far We Have Come** between them to connect the current
unit with earlier ones. When Big Ideas needs more room, continue it on a
separate slide. Course Map section links include only the first **Big Ideas**
slide among these closing slides, so the map remains focused on the
instructional sections. Include major applications already developed in **Big
Ideas** and the cumulative **How Far We Have Come**, linking back to their
substantive slides (for example, travel time, option pricing, Bayesian inference,
and queueing). Keep applications on the same cumulative slide when space
permits; omit applications mentioned only as motivation until they receive
substantive treatment. Minor illustrative examples such as Keister need not
appear.

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
In all five Course Maps, the current deck link uses `.current-deck` and
`aria-current="page"`, with blue color, bold weight, and 110% font size. In
Decks 02–05, section links move to the lower left under **This deck**. Per
instructor preference, omit the separate **In this deck** heading above the
theme in these four maps; this is a local exception to the shared theme-heading
convention. The `.deck-course-map` layout reserves the lower right for a
42%-wide tree, compared with the 16% navigation trees. Preserve readable labels, the theme, all links, and footer
clearance when changing either a map or its topic selection. Deck 01 retains
its existing tree-free Course Map because the Monte Carlo tree has not yet
been introduced; its full introductory tree appears later in the deck.

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

- Use bold vector notation for points and random inputs in multidimensional
  spaces: `\vx`, `\vt`, `\vX`, and corresponding shared vector macros.
  Carry it through function and kernel arguments, densities, differentials,
  sample nodes, and subvectors such as `\vX_{2:d}`. Keep scalar coordinates
  (`x_j`, `X_{i\ell}`), scalar time arguments, and explicitly univariate
  examples unbold. Distinguish a sample vector `\vx_i` from its scalar
  coordinates `x_{i\ell}`.
- Use zero-based indexing for samples, observations, Markov-chain states, and
  low discrepancy sequences: a sample of size $n$ is indexed from $0$ through
  $n-1$.
- Keep coordinate indices $1,\ldots,d$ and multilevel indices
  $1,\ldots,L$ one-based.
- For mixture and acceptance--rejection constructions, put the uniform decision
  coordinate last: the first $d$ coordinates generate the proposal or
  within-component draw, and $U_{d+1}$ selects the component or acceptance.
  In the scalar mixture, $U_1$ supplies the normal quantile and $U_2$ chooses
  the component. Keep notebook code and worked examples in the same order.
- Keep notation consistent with the shared macro registry and course
  notebooks.
- Use the role conventions in `AUTHOR_WORKFLOW.md`: uniform inputs `\vU`,
  proposal/source draws `\vZ`, target samples `\vX`, and scalar output
  `Y=f(\vX)`. Bold vector-valued maps (`\vS`, `\vT`, `\vA`); scalar quantiles and scalar transports remain unbold.
- Deck 04 compares equal-mean representations `f(\vX)` and `g(\vZ)`;
  use `h` for composed uniform-input integrands. Retain `g(\vX)` for controls
  and subvectors or conditioning variables where appropriate. Exact transport
  preserves IID output variance; equal-mean weighted contributions need not.
  Introduce `f(\vX)`, `g(\vZ)`, and `h(\vU)=g(\vS(\vU))` together on
  the opening big-picture slide; recall the composition when developing
  low discrepancy variance and cost models.
- In Improving Efficiency, label scalar contributions by method:
  `Y_{\mathrm{IS}}`, `Y_{\mathrm{CV}}`, `Y_{\mathrm{CMC}}`,
  `Y_{\mathrm{Anti}}`, and `Y_T` for exact transport. Use `Y_g` for the
  opening general alternative; reserve unadorned `Y` for `f(\vX)`.
- Name the corresponding complete contribution functions `g_{\mathrm{IS}}`,
  `g_{\mathrm{CV}}`, and `g_{\mathrm{CMC}}`. For cost comparisons, use
  `C(\varepsilon;g)` for cost at an error tolerance, `T(n;g)` for runtime at
  sample size `n`, `S(g)` for setup/pilot cost, and `\$(g)` for generating
  the input and evaluating one complete contribution at that input, including
  all required transformations. For cube integrands, `\$(h)` includes both
  point generation and evaluating `h(\vU_i)`. Use `\hmu_n(h)` for both
  deterministic and randomized cube estimates; fixed `\vu_i` versus random
  `\vU_i` distinguishes their defining averages. For RQMC replications use
  `\hmu_n^{(r)}` for an n-point run and `\hmu_{R,n}` for the average of R
  runs, with nR total point evaluations. Use `\hat\sigma^2_{R,n}` for the
  across-run sample variance, estimating the variance of one n-point run;
  divide it by R for the variance of the reported average. Write the
  replication interval directly without a separate radius symbol. Reserve
  `\alpha` for nominal failure probability and write confidence as
  `1-\alpha`; use `p_{\mathrm{QMC}}` and `p_{\mathrm{RQMC}}` for
  decay orders. When comparing IID and RQMC, label complete-estimate
  variances `\sigma_{\mathrm{IID},n}^2` and
  `\sigma_{\mathrm{RQMC},n}^2`; distinguish both from the one-value
  variance `\sigma^2(h)`, defining the latter in the IID column.
  For same-RMSE work comparisons, IID uses one n-point average with no R;
  fix R only for RQMC and choose n separately for each method to expose
  the RQMC epsilon exponent `-1/p_RQMC` and replication
  factor `R^{1-1/(2p_RQMC)}`. Do not substitute the fixed-n, growing-R
  variance-times-runtime diagnostic for that comparison.
  Separate normal/CLT approximation from the additional
  coverage justification required by data-dependent stopping; even exact
  fixed-sample intervals do not automatically justify repeated checks.
  Specify the error criterion;
  distinguish IID variance from the variation or smoothness governing QMC.
  Retain setup in the complete model; simple hand calculations may explicitly
  omit it as a stated simplifying assumption.
  When the method is an explicit cost argument, match it with QMC or RQMC
  subscripts on rate constants, exponents, setup, and per-point costs.
  Use `\lesssim` for sufficient-work bounds that absorb bounded sample-size
  rounding factors. Recall `D_n(K)=D(F_{\mathrm{unif}},\{\vu_i\};K)` when
  introducing its shorthand for the current cube points and kernel.
  For randomized QMC use an integrand-dependent error constant
  `A_{\mathrm{RQMC}}(h)` in the approximate variance model
  `var_rand{\hmu_n(h)} approx A_{\mathrm{RQMC}}^2(h) n^{-2 p_RQMC}`.
  Put every power on `A`, including `A_{\mathrm{RQMC}}^{1/p_{\mathrm{RQMC}}}(h)`
  in cost comparisons, and use approximation signs consistently in its
  derived RMSE, sample-size, and cost models; do not label them upper bounds.
  Keep this design-dependent quantity separate from deterministic RKHS
  variation, including in RMSE, cost, and representation comparisons.
- Use `\operatorname{vtn}_K(f)=\norm{f}_{\mathcal H_K}` as the general RKHS
  variation. When constants belong to the space and the quadrature rule
  integrates them exactly, the variation may be sharpened to
  `\min_{c\in\reals}\norm{f-c}_{\mathcal H_K}`. Equal-weight sample averages
  have the required exactness. In general normed spaces use an infimum unless
  attainment is established. Define this alongside the discrepancy error bound in
  Markov Chain Monte Carlo and recall it in Improving Efficiency. Distinguish
  the fixed integrand's variation from variance over randomized designs;
  the constant-shift variation in target `L_2` is the standard deviation.
- Preserve established slide anchors when notation in a mathematical heading
  changes, so callbacks from previously published decks remain valid.
- Keep the [uniform-input, target-sample, and output roles](../AUTHOR_WORKFLOW.md#course-wide-simulation-notation)
  visible when explaining a sampling method. Use `[target]{.alert}` at its
  first definition and key conclusions, with selective reinforcement in
  examples. Keep proposal and target roles distinct; do not highlight every
  occurrence mechanically.

## Highlighting

Omit unnecessary commas and periods in visible slide text and displayed
equations, including punctuation at the ends of equation rows. Preserve
punctuation needed for mathematical meaning or clear grammar.

Prefer highlighting the key word that carries a contrast, condition, or payoff,
rather than an entire phrase or sentence. Retain a short compound technical term
when its full name is the concept being introduced. Add selective emphasis to
important teaching cues; do not highlight every bullet mechanically. For example,
the LHS strengths highlight “No,” “faster,” and “stratum.”

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

### Deck 04 marker selections

Use the existing tree's specific method labels rather than Estimation or a
generic sampling pair throughout Deck 04. Mark variance reduction for controls,
conditioning, antithetic sampling, and Latin hypercubes; importance sampling
for density reweighting; density estimation for the conditional-density
examples; and low discrepancy or discrepancy for the QMC material. Add
Analysis, Linear Algebra, Probability, Error Assessment, or Data-Driven Error
Bounds when the slide actually develops that connection. Keep nearby labels
legible at the small-marker size. The opening section uses a short `##`
outline for its main ideas; supporting examples and bridges use marker-free
`###` continuation slides.

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
