# Next task

## Current task

Review Deck 03 individually with the instructor, beginning with its scope,
section sequence, and mathematical emphasis before detailed layout polishing.

## Current state

- Decks 01 and 02 remain the approved prototype and substantially reviewed
  course opening; the batch conversion did not reopen their lecture content.
- Deck 01's cumulative Terms to Know index now links important terminology
  introduced in Decks 03–05.
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
- All three new decks and the complete five-deck project render successfully
  with the `qmcpy` kernel, and all local cross-deck links resolve.
- Fall 2025 dates, tests, assignments, Mentimeter prompts, feedback responses,
  and other semester-specific logistics were omitted.
- Deck 02's uncompleted lookback/barrier and transformation-chain extensions
  remain possible later refinements rather than the current next task.
- The unresolved review questions and the Fall 2026 improvement backlog
  recovered from `MATH565Fall2025/MATH565_Improvements.md` are parked in
  `notes/TODO-LATER.md`; they are not blockers for the Deck 03 review.

## Cross-machine handoff

- The commit containing this handoff is the M5 batch-conversion baseline for
  Decks 03–05. A remote check immediately before publication found no newer
  MATH 565 commits from the Mini or Intel.
- M5 validation completed successfully on August 17, 2026: the root website
  and all five slide decks rendered, the assembled site contained every deck,
  local slide links resolved, Decks 03–05 had matching section outlines, and
  `git diff --check` passed. The recorded `classlib`, `qmcsoftware`, and
  test-archive submodule pins did not change.
- The protected `MATH565Fall2025` reference briefly appeared dirty because its
  clean local `classlib` checkout had moved beyond the parent-recorded pin. The
  checkout was restored to recorded commit `060d78b`; no Fall 2025 content,
  commit, or submodule pointer was changed.
- The iCloud-shared Check-In Dashboard was reconciled separately: Deck 03 is
  the active MATH 565 task, while the deferred Deck 02, notebook, QMCPy, and
  MCTS work is Blue. Preserve the user's other same-day dashboard changes.
- Before synchronizing MATH 565 on the Mini, inspect its current branch,
  worktree, recent commits, submodule status, stashes, and any unpublished work
  from the earlier Mini session. Do not pull, reset, run `arrive`, or overwrite
  files until that work has been identified and compared with this baseline.
- If the Mini worktree is clean and has no unpublished commits, fast-forward it
  normally. If it contains separate work, preserve that work and reconcile it
  explicitly; report overlapping files or divergent commits instead of
  silently choosing one machine's version.

## Constraints

- Treat the batch versions of Decks 03–05 as first drafts for individual
  instructor review, not as final approvals of scope or visible layout.
- Use Decks 01 and 02 as the local presentation and navigation prototypes
  without reopening their lecture content during review of Deck 03.
- Strip out Fall 2025-specific logistics, including references to that
  semester's homework, assignments, due dates, tests, announcements, and
  other dated events; do not present them as Fall 2026 information.
- Keep MATH 565 course content in this repository and promote only genuinely
  reusable infrastructure to `classlib` after demonstrated reuse.
- Keep `qmcsoftware`, the test archive, and reference repositories read-only.
- Preserve the Fall 2025 examples while improving notation, mathematical
  layout, punctuation, semantic emphasis, and gaps in visual explanation.

## Done when

- Deck 03's content scope and section sequence are instructor-approved.
- Its mathematical notation, examples, alert emphasis, and visible layout have
  been reviewed slide by slide and refined.
- Deck 03 renders cleanly, its internal and cross-deck links resolve, and any
  remaining questions are recorded for the next review pass.
