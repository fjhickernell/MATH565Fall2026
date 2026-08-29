# Next task

## Current task

Finish the first Deck 02 companion-notebook stage and polish its current calls
before beginning Deck 03 review. First test the two published current notebooks
in clean Google Colab runtimes using the course's recorded `classlib` and
`qmcpy` commits. Preserve flexibility for later decks to call or extend the
same notebooks.

## Next MATH 565 work

1. Review `notebooks/sampling/GeneratingSamples.ipynb` with the instructor and
   make any requested pedagogical or presentation refinements.
2. Finish the Deck 02 notebook migration: use the completed lecture narrative
   and the deck-to-notebook plan in `notebooks/NOTEBOOK_INVENTORY.md` to build
   the focused mixture/transport, acceptance--rejection, and financial-payoff
   companions; migrate and validate every retained notebook.
3. Review the drafted transport-map and normalizing-flow extension, its
   triangular-flow example, and its treatment in the companion notebook.
4. Give Deck 02 a final instructor-led polish pass, including its notebook
   links and the relationship between the lecture and retained notebooks.
5. Review Deck 03 individually, beginning with its scope, section sequence,
   and mathematical emphasis before detailed layout polishing.
6. Review Deck 04 and then Deck 05 using the same instructor-led process.
7. Complete the remaining Fall 2026 logistics and student-facing page details,
   including the seminar link, assignments, tests, project dates, and visible
   browser review.

The immediate 565 work is therefore to finish the Deck 02 notebooks and polish
Deck 02. Deck 03 follows that completed unit.

## Deck 02 completion target

Review `GeneratingSamples.ipynb`, finish the retained Deck 02 notebook
migrations, and give Deck 02 a final polish pass before beginning Deck 03.

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
  pin advances to commit `22a02a4`, which retains that repair and adds the
  authoritative shared slide and webpage style guides. Clean live-Colab
  validation remains pending.
- Assignment 1 is published in Canvas for 20 points, due September 2 at 11:59
  PM. It uses a 20-group self-sign-up set with at most two students per group.
  Its Owen Exercises 1.2 and 2.1, due date, and links appear on the Assignments
  page, Schedule, and Lecture 1. The course-hosted detail page is authoritative;
  Canvas links to it and the course Assignments page without repeating the
  exercise details, and a Canvas announcement has been posted.
- The Fall 2026 project page now records proposed October 1 topic submissions,
  November 23--24 presentations, November 11 and 18 presenter and observer
  sign-ups, a November 25 assessment deadline, presentation lengths, and
  conference-style logistics. The submission form, scheduling tools, location,
  and detailed procedures remain to be finalized; dates that are not yet final
  remain visibly labeled as proposed.
- Deck 01 is complete and instructor-approved. Its cumulative Terms to Know
  index links terminology introduced in Decks 02–05, and its approved closing
  transition previews Generating Samples using the transformation
  $\vX=T(\vU)$.
- Deck 02 has completed its initial instructor-led content and visible-layout
  review. Its option-payoff section now includes QMCPy's right and trapezoidal
  arithmetic-Asian discretizations together with discretely monitored lookback
  and barrier payoffs, plus an American-put optimal-stopping formulation. The
  preceding material now separates general geometric Brownian motion from its
  risk-neutral discrete asset-path specialization. A compact transport-map and
  normalizing-flow sequence with a triangular-flow example is now drafted
  immediately before acceptance--rejection and awaits instructor review.
- `notebooks/applications/AreWeThereYet.ipynb` is instructor-approved, executes
  cleanly, and is linked from the notebook page and both travel-time slides.
- `notebooks/sampling/GeneratingSamples.ipynb` has been migrated with current
  QMCPy distribution, stochastic-process, and financial-option APIs. It
  executes cleanly, has inspected saved outputs, and is linked from the
  notebook page and Deck 02. Its simulations are intentionally unseeded so
  reruns produce different realizations.
- `notebooks/NOTEBOOK_INVENTORY.md` now records the deck-to-notebook plan. It
  keeps `GeneratingSamples.ipynb` as a survey, adds focused Deck 02 companions
  for mixtures/transports, acceptance--rejection, and financial payoffs, and
  splits the inherited Asian-option and MCMC omnibus material across Decks
  02--04 by teaching purpose. Deck assignments identify previews, main
  developments, continuations, and retrospective calls rather than exclusive
  ownership; topics and notebooks may span decks.
- `slides/03-markov-chain-monte-carlo.qmd` is a full first-pass conversion of
  the Fall 2025 Keynote deck. It preserves the Markov-chain examples,
  Metropolis–Hastings practice, discrepancy development, MLE and Bayesian
  material, and queueing example; it adds a reproducible random-walk
  Metropolis figure.
- `slides/04-improving-efficiency.qmd` is a full first-pass conversion covering
  transformations, importance sampling, control variates, conditional and
  antithetic Monte Carlo, Latin hypercube sampling, low discrepancy methods,
  randomization, and stopping criteria. It adds an executable IID/LHS/Sobol'
  comparison.
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
