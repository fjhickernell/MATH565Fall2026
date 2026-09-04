# Next task

## Current task

Validate the instructor-approved
`notebooks/sampling/TransportMapsAndAcceptanceRejection.ipynb` in a clean
Google Colab runtime using its badge. Both acceptance--rejection examples now
use the pinned QMCPy-native implementation and pass local clean-kernel
validation; clean-Colab validation is the remaining execution check. The
instructor reports that `AreWeThereYet.ipynb` and `GeneratingSamples.ipynb`
both ran successfully in Colab. The Gaussian-mixture addition, IID/Sobol'
comparison, fitted error trends, and sample-size notation harmonization are
implemented. Keep the agreed combined notebook organization.

## Next MATH 565 work

1. Review the Gaussian-mixture section and IID/Sobol' comparison in
   `GeneratingSamples.ipynb` with the instructor.
2. Validate the revised
   `sampling/TransportMapsAndAcceptanceRejection.ipynb` in clean Colab.
   Deck 02 already links it; add the course notebook-page link
   after Colab validation, following `notebooks/NOTEBOOK_INVENTORY.md`.
3. Review the revised advanced-direct-sampling sequence: transport maps,
   acceptance--rejection, the reusable \(\operatorname{Beta}(2,1)\) scalar
   example, and the proposed companion-notebook treatment. Confirm that the
   target/proposal
   roles and their $\varrho_{\mathrm{tar}}$ and
   $\varrho_{\mathrm{prop}}$ notation read consistently across transport,
   importance sampling, and MCMC.
4. Give Deck 02 a final instructor-led polish pass, including its notebook
   links and the relationship between the lecture and retained notebooks.
5. Review Deck 03 individually, beginning with its scope, section sequence,
   and mathematical emphasis before detailed layout polishing.
6. Review Deck 04 and then Deck 05 using the same instructor-led process.
7. Create or adapt the Microsoft Bookings pages for Fall 2026 presenter and
   observer sign-ups, following the separate-page workflow used in Fall 2025,
   and add the finalized links and procedures to the project page.
8. Complete the remaining Fall 2026 logistics and student-facing page details,
   including the seminar link, assignments, tests, project dates, and visible
   browser review.

The immediate 565 work is therefore to finish the Deck 02 notebooks and polish
Deck 02. Deck 03 follows that completed unit.

## Immediate machine handoff target

Complete the GeneratingSamples instructor review and the clean-Colab validation
of the approved combined transport-map and acceptance--rejection notebook. The
QMCPy-native sampler substitution and local validation are complete.
Do not expand this immediate handoff to the still-separate
`FinancialOptionPayoffs.ipynb` migration.

The broader Deck 02 milestone also includes the financial-payoff notebook, an
instructor review of every retained companion, and the deck's final polish pass
before Deck 03 review begins.

## QMCPy acceptance--rejection state

Both the Beta$(2,1)$ and bounded banana examples now use
`qmcpy.AcceptanceRejection` from the existing pinned QMCPy commit `d8fec003`,
with IID uniform drivers, ordinary densities, and the required density
integrals. All ten code cells pass local clean-kernel execution with the
recorded dependencies; all six saved plots have been inspected. Fixed-proposal
experiments retain the acceptance diagnostics without confusing batching
overhead with intrinsic acceptance probability.

Clean-Colab validation remains pending. After it succeeds, add the course
notebook-page link. API choices and maintenance details are recorded in
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

For Deck 03, retain transparent NumPy/SciPy Metropolis--Hastings as the core
MCMC notebook. For a separate Bayesian application, first evaluate PyMC/NUTS
with ArviZ; use `emcee` only as the lighter fallback if dependency or clean
Colab setup is too burdensome. ArviZ is already in QMCPy's `[class]` extra;
PyMC and `emcee` are not current course dependencies.

Before handing back the notebook work, restart and run every edited notebook
with the `qmcpy` kernel, inspect saved output size and warnings, test the
recorded-commit setup in a clean Colab runtime, and render affected pages and
decks after adding links.

## Current state

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
  retains a separate financial-payoff companion, and splits the inherited
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
  Instructor review remains pending; the instructor reports successful Colab
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
  acceptance--rejection comparison. Live-Colab validation and the course-page
  link remain pending.
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
- Decks 03–05 are converted first drafts, not instructor-reviewed final decks.
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

## Later questions for Deck 03

- Does Deck 03 have the right scope, section sequence, and mathematical
  emphasis for Fall 2026?
- Should the Hickernell (1998) and Gretton et al. (2012) discrepancy references
  be added to shared `classlib` metadata and cited in Deck 03?

## Constraints

- Treat Decks 03–05 as first drafts for individual instructor review, not as
  final approvals of scope or visible layout.
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

## Done when

- Clean current Colab runtimes install the recorded `classlib` and `qmcpy`
  commits and execute both `AreWeThereYet.ipynb` and
  `GeneratingSamples.ipynb` end to end without an import or setup failure.
- `GeneratingSamples.ipynb` is instructor-approved.
- Every retained Deck 02 companion notebook is migrated, validated with the
  `qmcpy` kernel, and linked appropriately; decisions to combine or omit other
  inherited notebooks are recorded.
- Deck 02 has received its polish pass for the current stage, renders cleanly,
  and is ready to advance to Deck 03 review; later decks may add calls to the
  same notebooks or motivate coherent extensions.
