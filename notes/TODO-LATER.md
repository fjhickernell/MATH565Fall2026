# Todo Later

This file tracks deferred work and lower-priority tasks that should remain
visible without crowding the active project plan or status. Entries should
state why the work was deferred when that context will matter later.

## Deferred work

- Revisit the optional Deck 02 extensions after Decks 03–05 have completed
  individual instructor review: add selected lookback and barrier option
  payoffs, then decide whether the planned transport-map and normalizing-flow
  discussion belongs in the deck. These were deferred when the instructor
  directed the batch conversion to start with Deck 03.
- Review the notebooks associated with Deck 02 and align them with the final
  lecture narrative after the planned instructor-directed deck
  refinements are complete. Decide which inherited notebooks to retain,
  revise, combine, or omit; then validate each retained notebook with the
  `qmcpy` kernel and update the notebook page and deck links.
- Add a reusable mixture-distribution feature to QMCPy. Design and implement
  it in the standalone QMCSoftware repository rather than modifying the
  course repository's pinned `qmcsoftware` submodule.

## Parked review questions

- Decide during the Deck 05 review whether to add Monte Carlo tree search,
  which was planned for Fall 2026 but does not appear in the Fall 2025
  Selected Topics deck.
- Choose an overarching text or chapter reference for Deck 05; the Fall 2025
  title slide says only `Owen, Chapters ???`.
- Decide during the Deck 03 review whether to add the Hickernell (1998) and
  Gretton et al. (2012) discrepancy references to shared `classlib` metadata
  and cite them in the deck.
- When the optional Deck 02 extensions resume, choose the lookback and barrier
  contracts and the clearest transformation-map direction for the chained
  transformation example.

## Fall 2026 improvement backlog recovered from Fall 2025

The following ideas were preserved from the read-only
`MATH565Fall2025/MATH565_Improvements.md`, version 2025.11.28. They are a
backlog for later prioritization, not commitments for the current Deck 03
review.

### Curriculum

- Add an accessible Monte Carlo tree search introduction covering exploration
  versus exploitation, UCT, and connections to stochastic optimization;
  consider it as a short module or optional project.
- Expand MCMC coverage with ensemble sampling (`emcee`), NUTS demonstrations
  in PyMC, and Langevin or Hamiltonian MCMC; decide whether these supplement or
  partly replace Metropolis and parallel tempering.
- Reconsider the queueing examples using SimPy, possibly with a small shim for
  a consistent course interface.

### Notebooks and code

- Modernize inherited notebooks to use the current `classlib` workflow,
  especially GPU/CPU timing, gradient versus stochastic-gradient descent,
  stopping criteria, and Asian-option examples.
- Extend the introductory QMCPy Asian-option example with importance sampling
  and control variates, together with clearer `nbviz` styling and explanatory
  overlays.
- Develop a fuller reusable QMCPy kernel abstraction for covariance kernels,
  kernel herding, and Bayesian cubature demonstrations. Do this in the
  standalone QMCPy repository, not the pinned course submodule.

### Workflow

- Add periodic full-repository notebook execution to catch breakage before the
  semester.
- Test the student installation workflow with a clean macOS user and simplify
  the Conda and QMCPy setup instructions based on the result.

### Publishing

- Continue the unified Quarto visual style for figures, code, and exposition.
  The Fall 2026 repository has adopted Quarto, so the earlier Quarto versus
  Jupyter Book platform evaluation is no longer an open migration decision.
