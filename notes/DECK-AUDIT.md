# MATH 565 deck accuracy and clarity audit

## November 2, 2026 — all five existing decks

Reviewed the complete current sources for Introduction, Generating Samples,
Markov Chain Monte Carlo, Improving Efficiency, and Selected Topics. Scope
includes mathematical claims and conditions, worked examples, exercise prompts
and presenter answers, embedded Python, notation, proof/teaching dependencies,
and consistency with the pinned software and cited saved notebook evidence.
The slides remain the authoritative exposition; this file records the audit.

### Findings and corrections

| Deck | Corrections |
|---|---|
| 01 — Introduction | State moment and fixed-size IID assumptions; define the CDF on all real arguments; distinguish empirical masses from density estimates; match the empirical generalized-inverse quantile with NumPy's inverted-CDF method; use a density histogram. Reserve n for sample size and align input/map notation. Add missing moment, covariance, shrinkage, quantile and conditioning answer notes; distinguish singular Gaussian laws from the displayed full-dimensional density. |
| 02 — Generating Samples | Distinguish individually uniform randomized inputs from fixed low discrepancy quadrature nodes; remove the claim that arbitrary quantile transforms preserve dependence structure. State distribution parameter ranges, specify the continuous-path Brownian version, and label the finite-grid American-put problem as a grid-restricted approximation. Add missing quantile, mixture and geometric-Brownian answer notes. |
| 03 — Markov Chain Monte Carlo | Make the finite-state Metropolis exercise use independent uniform proposals with replacement, matching its acceptance ratio. Add its answer notes, initialization/ergodicity conditions, and the unbiased-MMD answer explanation. Use the nonnegative Gram quadratic-form definition of positive definite kernels, distinguishing strictness and the characteristic property; state kernel moment and sample-size conditions. Clarify the all-coordinate-subset Sobolev norm and single-server FCFS queue scope; fix a multiline display environment. |
| 04 — Improving Efficiency | Replace the old Keister stopping table with the four rows of the actual saved run and correct its exercise answers: replicated Sobol' and the Walsh bound meet the reported tolerance, while IID CLT and tight-budget Sobol' do not. Qualify Brownian drift and monitoring times, inverse-based conditional-density regularity and atoms, and the Asian payoff's positive strike. Add the missing monotone-antithetic proof. Explain that arbitrary generators need not give low discrepancy and rational Kronecker hand examples eventually repeat. |
| 05 — Selected Topics | Clarify conditional unbiasedness of stochastic gradients at adaptive iterates, without implying unbiased minimizer estimates or descent at every step. Align numerical matrix/coordinate notation and separate variance reduction from the role of structured points in the recap. The existing multilevel allocation, cost/error models, worked counts and UCT scores pass independent verification; the instructor's simplified many-level teaching sequence is preserved. |

The shared slide metadata had a stale CDN MathJax override. It now references
the pinned bundled runtime, matching classlib guidance. The generated HTML
for every deck uses that local path and the runtime exists in the assembled
site. No shared dependency or pin was changed.

Updated the MCMC migration handoff to match the existing placement of KL,
Stein and comparison slides after centered discrepancy under Alternative
comparisons. No lecture dates, coverage, assignments, grades, notebook code,
or saved notebook outputs were changed by this audit.

### Validation and references

- All five decks execute and render with the existing qmcpy kernel; all
  18 embedded Python cells complete. The root website also renders. No
  warnings or errors are found in the complete build logs. Generated deck
  output is assembled locally beneath `_site/slides`.
- 19 focused analytic/numerical checks for Decks 01–02 cover quantiles,
  mixtures, covariance factors, Brownian constructions, shrinkage, transport
  Jacobians and rejection. All 13 Python cells in these decks were also
  checked independently against pinned QMCPy.
- Deck 03 checks include both plotted simulations and rejection counts,
  exact finite-state MH invariance and exercise states/acceptance values,
  whole-target tempering algebra, the negative unbiased-MMD example, and
  all queue exercise event/customer-time results.
- 51 exact/evidence checks for Deck 04 cover IS means/variances and Brownian
  weights, controls and their cost, self-normalized IS, antithetic identities,
  low discrepancy construction arithmetic, RQMC cost powers, and the actual
  saved stopping rows. Pinned QMCPy source confirms the stopping interfaces
  and formulas referenced in the deck.
- 43 exact/numerical checks for Deck 05 cover random and deterministic
  allocations at p=1/2, 1 and 3/2, optimized cost formulas, the IID exercise,
  same-time error powers, covariance, quadratic losses/gradients, and UCT scores.
- All 634 local links/assets emitted by the five decks resolve, including
  destination fragments. Generated IDs are unique and the bundled MathJax
  configuration/path is verified for every deck.
- All previous explicit anchors and exercise markers are preserved. Visible
  prose emphasis/terminal-period checks, Python syntax/execution and
  `git diff --check` pass. All three pinned dependencies and the historical
  reference checkout remain clean and unchanged; MATH 332 is untouched.

Primary-reference checks support the theorem qualifications already in the
slides: [Giles, Multilevel Monte Carlo methods](https://people.maths.ox.ac.uk/gilesm/files/acta15.pdf)
for allocation and complexity assumptions, and
[Kocsis and Szepesvari, Bandit based Monte-Carlo Planning](https://sites.ualberta.ca/~szepesva/papers/ecml06.pdf)
for the UCT setting and evolving rollout returns. The kernel Stein expression
and boundary conditions were checked against
[Liu, Lee and Jordan (2016), Section 2.2 and Theorem 3.6](https://proceedings.mlr.press/v48/liub16.pdf).
The primary abstracts of [Gorham and Mackey (2017)](https://proceedings.mlr.press/v70/gorham17a.html)
and [Liu, Duncan and Gandy (2023)](https://proceedings.mlr.press/v202/liu23i.html)
support the existing kernel-choice/nonconvergence and separated-mode
limitations; those two complete papers were not re-audited.

### Remaining work

The deck source/content review is complete. No further mathematical issue
was identified in this pass. This does not complete the instructor's review
of the later drafts or select the remaining enrichment coverage.

The Keister companion notebook has a separate stale Markdown explanation:
it still names a green band of 0.05 while its executed settings, saved table
and plot use 0.0005. The deck now matches the actual output. This notebook
prose follow-up is recorded in [issue 3](https://github.com/fjhickernell/MATH565Fall2026/issues/3),
assigned to fjhickernell; its code and saved outputs were left intact.

Visual layout, interactive navigation and browser MathJax typesetting remain
unverified under the existing local-file browser restriction; no alternate
route was attempted. Review the changed slides before classroom use,
especially the extra statistical-estimation table row, quantile explanation,
Metropolis prompt, kernel definition and four-row stopping table.

The November 3 Selected Topics continuation and the instructor's simplified
many-level/SGD review plan are unchanged. The source/documentation corrections
are included in the November 2 Checkpoint. Remote CI/deployment and live
verification remain pending.

## November 17, 2026 — Selected Topics clarity and completeness

Reviewed the complete Deck 05 source, with an independent second pass through
parallel computing, two-level/MLMC allocation and bias, and SGD. No material
formula error was found. The MCTS walkthrough's choices and all stored-node
counts were independently replayed against its SVG generator.

### Corrections

- Move “Where MCTS is used” immediately after the first substantive MCTS slide;
  retain the three main section headings and existing public anchors.
- Explain why this variant retains at most one new node per iteration:
  persistent storage and bookkeeping costs, selective growth on revisited
  branches, and retention of the rollout return in stored-path statistics.
  Distinguish this choice from the cost of generating/evaluating the rollout
  and from expansion policies that retain more nodes. The supporting primary
  reference is [Coulom (2006), Section 2](https://www.remi-coulom.fr/CG2006/CG2006.pdf).
- Put all UCT notation in a bullet glossary after the formula, then place the
  concrete Start-node example beside the later six-iteration tree. Distinguish
  N(s) from N(s,a) and explain why a node's first
  evaluation before child storage makes parent visits exceed summed child
  visits: after six iterations, N(A)=5=1+2+2. A new continuation immediately
  after Iteration 3 contrasts parent W(A)=2,N(A)=2 with action/child
  W(A,0)=W(A–0)=1,N(A,0)=N(A–0)=1. Iteration 3 shows its pre-selection
  N(Start)=2 above the table, with A successes/visits 1/1 and B successes/visits
  0/1 in the W(s,a) and N(s,a) columns. Omit duplicate count bullets and
  score-calculation algebra. Scored iterations
  use a 52%/4%/44% layout, combining all relevant child counts/scores and a
  formula reminder. Both display sizes pass the final layout checks.
- Use “MCTS iteration 1” and “Iteration 2” onward for four-phase cycles, “search
  run” for a complete budget, and “rollout” for the temporary continuation.
  Regenerate SVG accessibility titles, preserve tree geometry/statistics, and
  lower both captions 40 pixels with a taller viewBox. Label the stored counts
  W(s)/N(s) and connect child-node counts to the UCT action notation.
- Define SGD loss gap and equivalent passes visibly. State that the comparison
  records target crossings retrospectively while every run stops at its fixed
  eight-pass budget. Include curvature-based rates among the GD comparison's
  practical choices, matching the logistic experiment.

The CPU/GPU notebook's visible link remains intentionally deferred until
instructor review. No notebook code, outputs, course meeting coverage, assessment
content, dependency pins or MATH 332 sources changed. Instructor review of the
remaining Deck 04–05 material remains open.


### Validation of the November 17 changes

- The complete 98-slide deck renders successfully with all five embedded
  Python cells. No numerical algorithm or notebook output was changed.
- The SVG generator's assertions and an independent replay verify all ten
  expansions, UCT choices and stored-node backup totals. All 20 figures retain
  their node/edge coordinates and use the lower W(s)/N(s) captions.
- All 33 MCTS slides and the two revised SGD comparison slides pass rendered
  geometry checks at 1600×1000 and 1280×720. Subsequent checks cover the final
  Select text, combined W/N/UCT tables and consistent Back up instructions.
  The affected slides were visually inspected.
- The final browser checks have no missing images, MathJax errors, JavaScript
  errors, or unresolved internal fragments. All original heading anchors are
  preserved, and 122 assembled local links/assets resolve.
- Visible bold-prose and terminal-period checks and git diff --check pass.
  The three pinned dependencies remain clean at their recorded commits.

The current prose and captions are reflected in the ignored local preview
and included in the November 17 checkpoint. Remote deployment/live verification
and instructor walkthrough remain open.


### Score reminders and complete selection inputs — November 17

All 12 pre-selection UCT decisions in iterations 3–10 now expose their parent
visit totals and per-child W(s,a), N(s,a), and scores. Iterations 5, 6, 9 and
10 include both root and deeper comparisons in one table, separated by a row
rule. The tables carry per-child W and N values without duplicate bullets;
parent visit totals remain above them as the formula's N(s) inputs.
The formula reminder is above each table, with c=1 substituted. The first
UCT-table column states “c=1 for this example”; per-table metadata is removed.
Gold cells identify the actual selected score for each parent; ties choose
0. This replaces separate visible selection-result statements. Iterations
1–2 state why their untried actions bypass scoring.

The four-phase overview and all ten worked iterations retain “Back up” as
the phase label, explicitly grouping the stored-counter update and
rollout-suffix discard under it. Iteration 8's rollout panel says “One return
for this iteration” because backup is still to come.

A read-only generator replay independently verifies every input, score and
chosen action. All ten changed iteration panels pass at 1600×1000 and
1280×720, including cell backgrounds, inline count pairs, formula bounds,
images, MathJax and internal fragments. The course SCSS compiles; only
pre-existing Sass import deprecations were emitted. The source changes and
ignored local preview are reconciled; these changes are included in the
November 17 checkpoint. Remote deployment/live verification remain pending.
