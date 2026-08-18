# Next task

## Current task

Review Deck 03 individually with the instructor, beginning with its scope,
section sequence, and mathematical emphasis before detailed layout polishing.

## Current state

- Deck 01 is complete and instructor-approved. Its cumulative Terms to Know
  index links terminology introduced in Decks 02–05, and its approved closing
  transition previews Generating Samples using the transformation
  $\vX=T(\vU)$.
- Deck 02 has completed its initial instructor-led content and visible-layout
  review. Its optional lookback/barrier and transformation-chain extensions
  are parked for later rather than blocking Deck 03 review.
- `notebooks/applications/AreWeThereYet.ipynb` is instructor-approved, executes
  cleanly, and is linked from the notebook page and both travel-time slides.
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

## Questions to resolve

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
- Keep `qmcsoftware`, the test archive, and reference repositories read-only.
- Preserve the Fall 2025 examples while improving notation, mathematical
  layout, semantic emphasis, and gaps in visual explanation.
- Keep MCTS in Deck 05, Selected Topics, rather than the MCMC deck.

## Done when

- Deck 03's content scope and section sequence are instructor-approved.
- Its mathematical notation, examples, alert emphasis, and visible layout have
  been reviewed slide by slide and refined.
- Deck 03 renders cleanly, its internal and cross-deck links resolve, and any
  remaining questions are recorded for the next review pass.
