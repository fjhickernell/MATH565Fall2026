# Next task

## Current task

Focus has switched to MATH 332. When MATH 565 work resumes, finish the Deck 02
notebooks and polish Deck 02 before beginning Deck 03.

## Next MATH 565 work

1. Review `notebooks/sampling/GeneratingSamples.ipynb` with the instructor and
   make any requested pedagogical or presentation refinements.
2. Finish the Deck 02 notebook migration: use the completed lecture narrative
   to decide which inherited companion notebooks to retain, revise, combine,
   or omit; migrate and validate every retained notebook.
3. Give Deck 02 a final instructor-led polish pass, including its notebook
   links and the relationship between the lecture and retained notebooks.
4. Review Deck 03 individually, beginning with its scope, section sequence,
   and mathematical emphasis before detailed layout polishing.
5. Review Deck 04 and then Deck 05 using the same instructor-led process.
6. After Decks 03–05 are reviewed, return to the deliberately deferred Deck 02
   extensions, including possible lookback and barrier examples.
7. Complete the remaining Fall 2026 logistics and student-facing page details,
   including the seminar link, assignments, tests, project dates, and visible
   browser review.

The first 565 work after the course switch is therefore to finish the Deck 02
notebooks and polish Deck 02. Deck 03 follows that completed unit.

## Deck 02 completion target

Review `GeneratingSamples.ipynb`, finish the retained Deck 02 notebook
migrations, and give Deck 02 a final polish pass before beginning Deck 03.

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
- `notebooks/sampling/GeneratingSamples.ipynb` has been migrated with current
  QMCPy distribution, stochastic-process, and financial-option APIs. It
  executes cleanly, has inspected saved outputs, and is linked from the
  notebook page and Deck 02. Its simulations are intentionally unseeded so
  reruns produce different realizations.
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
- Keep `qmcsoftware`, the test archive, and reference repositories read-only.
- Preserve the Fall 2025 examples while improving notation, mathematical
  layout, semantic emphasis, and gaps in visual explanation.
- Keep MCTS in Deck 05, Selected Topics, rather than the MCMC deck.

## Done when

- `GeneratingSamples.ipynb` is instructor-approved.
- Every retained Deck 02 companion notebook is migrated, validated with the
  `qmcpy` kernel, and linked appropriately; decisions to combine or omit other
  inherited notebooks are recorded.
- Deck 02 has received its final polish pass, renders cleanly, and is ready to
  hand off before Deck 03 review begins.
