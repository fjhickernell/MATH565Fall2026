# Next task

## Current task

Prepare Test 1 for September 15, covering Introduction and Generating Samples;
finalize the room, test PDF, and Canvas entry. The regular classroom is PH 109;
confirm the test room explicitly. Also grade homework (Dashboard deadline:
September 9; completion not yet reported) and add the seminar link.
Remaining notebook and later-deck work is listed below.

Deck 03 introduces kernel discrepancy, then its worst-case and Gaussian-process
average-case integration-error interpretations, then KL/relative entropy, Stein
discrepancy, and their comparison. Preserve that order and the
Hickernell–Kirk–Sorokin Section 5 citation.
The revised Decks 01–03 readings and seven-notebook audit are recorded in
`notes/OWEN-COVERAGE-AUDIT.md`.

## Completed Deck 03 review

The instructor confirmed on September 10, 2026 that Deck 03 and all four
companions are reviewed, and that the September 10 lectures are prepared:

- `notebooks/sampling/MetropolisHastings.ipynb`: compare with the already taught
  acceptance--rejection method; study trapping and then parallel tempering.
- `notebooks/applications/BayesianMCMC.ipynb`: retain the 2025 inference example
  with exact posterior benchmarks, multiple-chain diagnostics, and tempering.
- `notebooks/performance/Discrepancy.ipynb`: compare empirical distributions
  using MMD, kernel scales, and the witness function.
- `notebooks/applications/QueueSimulation.ipynb`: SimPy single-server and
  drive-through models, finite-run accounting, independent replications, and
  blocking comparisons.

All four companions pass clean local `qmcpy` execution without warnings.
The queue notebook has saved outputs and four inspected figures, and its eight
deterministic model tests pass. Existing MCMC notebook outputs were preserved. Mathematical checks cover target normalization, rejected-state
retention, swap ratios, exact posterior algebra, and kernel identities. The
source map and corrections are recorded in `notes/MCMC-MIGRATION.md`.

Deck 03 and `pages/notebooks.qmd` now link all four companions, with their
sources and helpers included in the same checkpoint. Instructor content review is complete.
By instructor decision, separate clean-Colab execution is no longer a publication
prerequisite: rely on the established setup and address problems when reported.
Keep `notebooks/mcmc_examples.py` published with the notebooks. The official
PyMC API quickstart is an optional external Bayesian supplement. SimPy 4.1.2
is the queueing engine; course-specific process definitions and exact finite-run
accounting live in `notebooks/queue_examples.py`. No PyMC/NUTS or emcee dependency
is required to finish the current Deck 03 preparation.

The Deck 03 discrepancy section and its companion notebook now clarify that
the off-diagonal IID estimator targets the nonnegative population MMD squared:
its expectation is zero when the two distributions agree, but a more negative
realization is only a larger downward sampling fluctuation, not a better match.
The deck includes a starred roman-numbered exercise on these properties and
on the dependence obstruction for successive Metropolis states. Shared
`classlib` exercise subparts now support documented `.lettered`, `.numbered`,
and `.roman` modifiers while retaining the default en-dash marker.
`MetropolisHastings.ipynb` now also reports consecutive-repeat counts,
transition denominators, and percentages throughout, distinguishes whole-run
from retained-state summaries, and explains why repeated states must remain in
the empirical distribution.

Deck 03 review is complete. The September 8 schedule names
Markov chain Monte Carlo and links Deck 03. Recent slide revisions include the
global construction/local decision contrast, gold-border Markov definition,
asymptotic-distribution motivation, compact martingale note, joint-density
acceptance interpretation, and separated-mode trapping demonstration. The
applications section now opens with a gold-border comparison of direct finance
sampling, Bayesian MCMC, and event-driven queue simulation; detailed
qualifications and optional examples remain in speaker notes.

The instructor-approved inference transition distinguishes frequentist,
Fisherian/likelihood, and Bayesian perspectives using the shared Efron–Hastie
reference. MLE is not a prerequisite for Bayes, and normal observations are
only a worked example in speaker notes. Bayesian and queueing topics each
retain one level-two heading with supporting continuation slides. The queue
notebook now highlights residual times, finite-run averages, blocking, and
capacity versus service rate. The instructor has now confirmed review of the
full deck and all four companions.

## Latest slide refinements

The September 10 lecture follow-up now includes parallel tempering and a
before/after product-density swap explanation. Discrepancy proceeds from
distributions to empirical samples, then unbiased population estimation and
normalization. The worst-case and GP average-case error interpretations precede
KL and Stein. Stein now has explicit supremum and pairwise-kernel formulas,
using true integral minus sample average. Notebook algorithms are unchanged.

Decks 02–05 have larger Course Map trees at lower right and **This deck** links
at lower left; all five decks use bold, larger current-deck links. Deck 01's
Course Map remains tree-free because the Monte Carlo tree has not yet been
introduced. Tree selections reflect substantive coverage: no Discrepancy
Measures or Estimation/Statistics in Deck 02, no finance in Decks 03 or 05,
and Error Assessment on Deck 03's error derivations. Course-specific
conventions are in `docs/slide-style.md`.
Decks 04–05 also now have Course Map themes; their full content review remains
pending. All five decks render, the revised slides and maps have been visually
checked, and their local navigation links are validated.

At the end of Deck 02, mixture sampling and acceptance--rejection now share an
enlarged-input formulation. The first $d$ uniform coordinates are transported
to a proposal draw and one additional independent uniform coordinate makes the
component or acceptance decision. The mixture expectation is a single
expectation over $[0,1]^{d+1}$; the accepted-target expectation is a ratio of
two such expectations. The acceptance indicator also makes explicit the
discontinuity that low discrepancy sampling must resolve. Both new slides and
the consolidated Big Ideas summary render cleanly and have been visually
checked at the standard RevealJS viewport.

## Other pending MATH 565 work

1. Review Deck 04 and then Deck 05 using the instructor-led process, including
   their companion-notebook plans in `notes/TODO-LATER.md`.
2. Complete the remaining Fall 2026 logistics and student-facing page details,
   including assignments, tests, project dates, and visible browser review.

Deck 02 polish and its companion-notebook review are complete for the current
stage. Deck 03 and its four companions are reviewed. Do not reopen those tasks
from older handoff instructions below. Separate presenter/observer Bookings
pages, the QMCPy mixture feature, MCTS, and other deferred extensions remain
in `notes/TODO-LATER.md`; Bookings, mixture support, and MCTS retain their Blue
Dashboard status.

## Deck 02 notebook work — closed September 10, 2026

The instructor confirmed that the remaining companion-notebook task is done,
including review of the Gaussian-mixture and IID/Sobol' sections in
`GeneratingSamples.ipynb`. The combined transport/acceptance--rejection
companion is already reviewed, validated, and linked. The previously planned
separate `FinancialOptionPayoffs.ipynb` does not exist; its creation is no
longer an outstanding requirement for this completed task. Do not reopen the
task solely because that planned file is absent.

## QMCPy acceptance--rejection state

Both the Beta$(2,1)$ and bounded banana examples now use
`qmcpy.AcceptanceRejection` from the course's recorded QMCPy dependency,
with IID uniform drivers, ordinary densities, and the required density
integrals. All ten code cells pass local clean-kernel execution with the
recorded dependencies; all six saved plots have been inspected. Fixed-proposal
experiments retain the acceptance diagnostics without confusing batching
overhead with intrinsic acceptance probability.

The course notebook-page link is included with the validated notebook source.
Separate clean-Colab validation is no longer required. API choices and maintenance details are recorded in
`notes/TECHNICAL-NOTES.md`; the more general classlib sampler remains unchanged.

## Machine handoff — Deck 02 notebooks

The notebook organization is decided:

- Keep `GeneratingSamples.ipynb` as the broad survey and add only the Gaussian
  mixture already taught in Deck 02: $p=0.3$,
  $(\mu_1,\sigma_1)=(-2,0.5)$, and
  $(\mu_2,\sigma_2)=(1,1)$. Place it immediately after the zero-inflated
  exponential. Aim for one short explanatory cell and one executable cell
  showing generated samples against the analytic mixture density.
- Create one focused
  `notebooks/sampling/TransportMapsAndAcceptanceRejection.ipynb`; do not create
  the previously proposed `MixturesAndTransportMaps.ipynb` or a standalone
  `AcceptanceRejection.ipynb`.
- Use the recurring $\operatorname{Beta}(2,1)$ target and
  $\operatorname{Unif}(0,1)$ proposal to compare the exact transport
  $T(z)=\sqrt z$ with acceptance--rejection using $M=2$ and $U\le Z$.
  Continue with the Deck 02 triangular flow, then adapt one bounded nonlinear
  target, its proposal, and its diagnostics from the read-only Fall 2025
  `AcceptanceRejection.ipynb`. Both rejection examples now use
  `qmcpy.AcceptanceRejection`. Do not copy the inherited sampler into the
  course notebook.
  The scalar example makes the method transparent; omit the inherited
  half-normal/exponential example unless instructor review establishes that it
  adds something distinct.
- Treat the triangular-flow target on $\mathbb R^2$ and the bounded
  banana-shaped acceptance--rejection target as different examples, with
  explicit names and domains.
- In the acceptance--rejection explanation, allow the desired density to be
  $c\varrho_{\mathrm{tar}}$, use $U$ for the independent uniform decision
  draw and $W$ for the acceptance indicator, and use the 2025 Bayes
  conditional-density derivation rather than a small-$dz$ argument.
- Use $f$ for a function of the sample, not $h$. Write density evaluations
  with ordinary or sized parentheses, such as
  $\varrho_{\mathrm{tar}}(x)$, never braces around the argument.
- Let Deck 03 call back to the combined notebook instead of repeating its
  inherited acceptance--rejection review. Let Deck 04 return to the same
  scalar pair for the importance weight $2z$.

The detailed content sequence, inherited-source inventory, and validation
order are authoritative in `notebooks/NOTEBOOK_INVENTORY.md`. Use
`slides/02-generating-samples.qmd` as the source of truth for the current
mixture, transport, and acceptance--rejection exposition; use
`slides/04-improving-efficiency.qmd` for the later transport/importance
sampling comparison; use the sibling Fall 2025 repository only as a read-only
source for inherited notebook code. When later editing slides, retain punch
points rather than prose sentences and omit terminal periods. Do not add
student-facing links until a notebook exists, runs from a clean kernel, and
has been reviewed.

If the QMCPy sampler exposes a genuine reusable QMCPy defect, report it
for upstream repair rather than hiding a workaround in course-only code. Do
not remove or alter the more general `classlib` utility merely because this
notebook no longer needs it.

For Deck 03, the three course-owned notebooks retain the non-queueing MCMC
material. Parallel tempering is implemented. The Bayesian notebook uses ArviZ
and links the external PyMC quickstart as an optional supplement; a course-owned
PyMC/NUTS example is only a possible later extension. Do not add emcee now.

The discrepancy notebook's current saved parameters are 1,000 candidate states,
10,000 independent AR reference points, and 1,000 burn-in states. Kernel sums
use exact blocks and cache the reference self-comparison for each length scale.
The candidate/reference draws are independent. A scatter plot can hide repeated
states, and a single-run MMD ranking does not establish an optimal proposal scale.

Before handing back the notebook work, restart and run every edited notebook
with the `qmcpy` kernel, inspect saved output size and warnings, retain the
recorded-commit Colab setup, and render affected pages and
decks after adding links.

## Current state

- The regular classroom is PH 109, as confirmed September 10, 2026. The
  Schedule source is updated and rendered for publication with this checkpoint.
  The published Canvas Welcome page now displays PH 109 and
  the Tuesday/Thursday 10:00 AM meeting time; the saved page is verified.
- `AreWeThereYet.ipynb` and `GeneratingSamples.ipynb` now have consistent
  Colab badges and conditional setup cells. In Colab they clone the current
  course and install the repository's exact recorded `classlib` and `qmcpy`
  commits through public HTTPS submodule URLs; they do not depend on PyPI or a
  moving QMCPy `develop` branch. This preserves access to newer QMCPy work and
  interim `nbviz` support recorded by the course. Both notebooks execute
  cleanly with the local `qmcpy` kernel, and the root site, all five decks, and
  assembled site render cleanly. The shared lazy-import fix is tested and
  published in HickernellAcademicLib commit `615b402`. The current `classlib`
  pin includes the published MathJax 3
  loader from the 332 checkpoint, retains the shared repairs, guides,
  heading-hierarchy convention, and RevealJS `\mLambda` and `\mV` macros, and
  records the standalone-`amsmath`, punch-point, terminal-period, and
  function-delimiter guidance, together with the shared Course Map theme
  guidance. The instructor reports successful Colab
  execution of both current notebooks.
- Assignment 1 is published in Canvas for 20 points, due September 2 at 11:59
  PM. It uses a 20-group self-sign-up set with at most two students per group.
  Its Owen Exercises 1.2 and 2.1, due date, and links appear on the Assignments
  page, Schedule, and Lecture 1. Its title-slide reminder appears only on Deck
  01 because that deck contains the assignment's coverage. The course-hosted
  detail page is authoritative; Canvas links to it and the course Assignments
  page without repeating the exercise details, and a Canvas announcement has
  been posted.
- Assignment 2 is published in Canvas for 20 points, due September 11 at 11:59
  PM Chicago Time. It uses 20 self-sign-up groups limited to two students, one
  shared group grade, and unlimited file-upload attempts. Its Canvas description
  links only to the assignment detail page and Assignments page. Its detail
  page, Assignments entry, Schedule entry, and Deck 02 reminder are live, and
  its all-sections Canvas announcement has been posted.
- Test 1 is scheduled for the full class period on September 15 and covers
  **Introduction** and **Generating Samples**. Its date and coverage appear on
  the Schedule, Tests page, and Deck 02 title slide. The room, current test PDF,
  and Canvas entry remain to be finalized.
- The Fall 2026 project-selection deadline is Friday, September 18. A live
  Illinois-Tech-only Microsoft Form records students' names, A-numbers, project
  type, article citation and PDF or proposed QMCPy feature, and optional QMCPy
  teammate. The course page links the form, the Schedule records its deadline,
  and the page correctly states that a review article must have been published
  less than fifteen years ago. Presenter and
  observer scheduling still needs separate Microsoft Bookings pages adapted
  from the Fall 2025 workflow; no tracked 2025 Python sign-up checker exists.
- Deck 01 is complete and instructor-approved. Its cumulative Terms to Know
  index links terminology introduced in Decks 02–05, and its approved closing
  transition previews Generating Samples using the transformation
  $\vX=T(\vU)$.
- Deck 02 has completed its initial instructor-led content and visible-layout
  review. Its multivariate-normal development now compares Cholesky and PCA
  factorizations for the same covariance matrix and explains why PCA places
  dominant variance in early coordinates for low discrepancy sampling. Its
  geometric-Brownian-motion sequence now distinguishes mean from median
  growth before specializing to risk-neutral paths. Its option-payoff section
  now includes QMCPy's right and trapezoidal
  arithmetic-Asian discretizations together with discretely monitored lookback
  and barrier payoffs, plus an American-put optimal-stopping formulation. The
  preceding material now separates general geometric Brownian motion from its
  risk-neutral discrete asset-path specialization. Transport maps no longer
  sit under low discrepancy; transport and acceptance--rejection are the two
  children of More Advanced Direct Sampling. The transport sequence now uses
  a \(\operatorname{Beta}(2,1)\) target with a
  \(\operatorname{Unif}(0,1)\) proposal before the triangular flow.
  Acceptance--rejection reuses the same pair by keeping \(Z\) with probability
  \(Z\). Its general derivation follows the 2025 acceptance-indicator \(W\)
  and Bayes' theorem argument and explicitly allows an unnormalized target.
  Deck 04 returns to the pair to contrast the exact transport
  \(T(z)=\sqrt z\) with the varying importance weight \(2z\). Deck 03 uses the
  same target/proposal roles in Metropolis--Hastings.
  The notation $\varrho_{\mathrm{tar}}$ and $\varrho_{\mathrm{prop}}$ is
  intentionally course-wide even where the literature uses other symbols.
  Shrinkage now immediately follows Deck 01's first bias--variance and random
  sampling development, where it demonstrates that accepting bias can reduce
  MSE. Deck 04 refers back to that lesson while keeping its opening sequence
  focused on variance reduction. The revised sequence awaits instructor
  review.
- `notebooks/applications/AreWeThereYet.ipynb` is instructor-approved, executes
  cleanly, and is linked from the notebook page and both travel-time slides.
  Its multiline displays use standalone `align` environments, and its
  standard-deviation results use rich mathematical display rather than
  printing visible dollar-sign delimiters.
- `notebooks/sampling/GeneratingSamples.ipynb` has been migrated with current
  QMCPy distribution, stochastic-process, and financial-option APIs. It
  now presents separate Asian arithmetic-mean and floating-strike lookback
  call subsections, including an IID replication diagnostic for each. It
  executes cleanly, has inspected saved outputs, and is linked from the
  notebook page, the quantile-transform portion of Deck 02, and Deck 02's Big
  Ideas slide. Its simulations are intentionally unseeded so reruns produce
  different realizations.
- `notebooks/NOTEBOOK_INVENTORY.md` now records the deck-to-notebook plan. It
  keeps `GeneratingSamples.ipynb` as a survey with a compact mixture section,
  combines transport maps and acceptance--rejection in one focused companion,
  originally proposed a separate financial-payoff companion, and splits the inherited
  Asian-option and MCMC omnibus material across Decks 02--04 by teaching
  purpose. Deck assignments identify previews, main developments,
  continuations, and retrospective calls rather than exclusive ownership;
  topics and notebooks may span decks.
- The compact Gaussian-mixture section has been added immediately after the
  zero-inflated exponential in `GeneratingSamples.ipynb`, with a component
  choice, conditional normal transform, and sample histogram against the
  analytic density. Its low discrepancy section now compares IID and
  randomized Sobol' sampling using CDF errors and 32 independent repetitions,
  with fitted power-law trends for the median maximum CDF errors.
  Instructor review is complete; the instructor reports successful Colab
  execution of the notebook.
- `TransportMapsAndAcceptanceRejection.ipynb` is now drafted with transport
  first: the Beta(2,1) map, the unbounded triangular flow, the Bayes
  acceptance-indicator derivation, and the same Beta target by rejection.
  Both rejection examples use `qmcpy.AcceptanceRejection` with uniform
  proposals. The bounded 2025 banana example has a proved envelope;
  quadrature supplies the API's density integral, marginal densities, and
  acceptance-probability benchmarks. Local clean-kernel validation of the
  revised notebook is complete, and the instructor has approved the draft.
  The Colab badge now
  targets its Fall 2026 repository path.
  Deck 02 links it from More Advanced Direct Sampling and the scalar
  acceptance--rejection comparison. The course-page link is included with the
  notebook source; separate Colab validation is no longer required.
- `slides/03-markov-chain-monte-carlo.qmd` is a full first-pass conversion of
  the Fall 2025 Keynote deck. It preserves the Markov-chain examples,
  Metropolis–Hastings practice, discrepancy development, MLE and Bayesian
  material, and queueing example; it adds a reproducible random-walk
  Metropolis figure.
- `slides/04-improving-efficiency.qmd` is a full first-pass conversion covering
  transformations, importance sampling, control
  variates, conditional and antithetic Monte Carlo, Latin hypercube sampling,
  low discrepancy methods, randomization, and stopping criteria. It now gives
  exact transport and importance sampling a common correction-weight formula
  and compares them with the recurring \(\operatorname{Beta}(2,1)\) scalar
  example, including a reversal in their variance ranking for two choices of
  \(f\). It adds an executable IID/LHS/Sobol' comparison.
- `slides/05-selected-topics.qmd` is a full first-pass conversion covering
  parallel computing, gradient and stochastic-gradient descent, and two-level
  and multilevel Monte Carlo. It adds an executable gradient-path comparison.
- Deck 03 and its four companions are instructor-reviewed as of September 10,
  2026. Decks 04–05 remain first drafts awaiting instructor review.
- MCTS is assigned to Deck 05, Selected Topics. It remains parked until that
  deck's review.
- The root website and all five decks render with the `qmcpy` kernel, and the
  assembled site's local links resolve.
- Fall 2025 dates, tests, assignments, Mentimeter prompts, feedback responses,
  and other semester-specific logistics were omitted during conversion.
- The M5 batch-conversion commit has been incorporated on the Mini together
  with the Mini's Deck 01 transition, PH 108 schedule correction, MCTS
  decision, and deferred-work notes. A read-only Intel audit found no
  unpublished work, commits, stashes, or dirty submodules there.

## Optional later reference work for Deck 03

- Should the Hickernell (1998) and Gretton et al. (2012) discrepancy references
  be added to shared `classlib` metadata and cited in Deck 03?

## Constraints

- Treat Decks 04–05 as first drafts for individual instructor review. Deck 03
  and its four companions have completed instructor review.
- Use Decks 01 and 02 as the local presentation and navigation prototypes
  without reopening their approved lecture content during Deck 03 review.
- Strip out Fall 2025-specific logistics, including references to that
  semester's assignments, tests, announcements, and dated events.
- Keep course-specific content in this repository and promote only genuinely
  reusable infrastructure to `classlib` after demonstrated reuse.
- In Colab, install the course's recorded `classlib` and `qmcpy` commits rather
  than assuming PyPI or a moving QMCPy branch contains every required feature.
- Keep `qmcpy`, the test archive, and reference repositories read-only.
- Preserve the Fall 2025 examples while improving notation, mathematical
  layout, semantic emphasis, and gaps in visual explanation.
- Keep MCTS in Deck 05, Selected Topics, rather than the MCMC deck.

## Deck 03 notebook handoff — complete September 10, 2026

- All four Deck 03 companions are instructor-reviewed; local validation is complete.
- Their notebook-page links are rendered and published. Separate clean-Colab
  validation is not required.

## Deck 02 maintenance and later polish

- Preserve the recorded-commit Colab setup and address reported runtime problems;
  separate clean-Colab execution is not a publication prerequisite.
- `GeneratingSamples.ipynb` is instructor-approved.
- Every retained Deck 02 companion notebook is migrated, validated with the
  `qmcpy` kernel, and linked appropriately; decisions to combine or omit other
  inherited notebooks are recorded.
- Deck 02 has received its polish pass for the current stage, renders cleanly,
  independently of the completed Deck 03 review; later decks may add calls to the
  same notebooks or motivate coherent extensions.
