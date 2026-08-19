# Todo Later

This file tracks deferred work and lower-priority tasks that should remain
visible without crowding the active project plan or status. Entries should
state why the work was deferred when that context will matter later.

## Parked review questions

- Choose an overarching text or chapter reference for Deck 05; the Fall 2025
  title slide says only `Owen, Chapters ???`.
- Decide during the Deck 03 review whether to add the Hickernell (1998) and
  Gretton et al. (2012) discrepancy references to shared `classlib` metadata
  and cite them in the deck.

## Deck 02 — Generating Samples

- After Decks 03–05 complete individual review, revisit selected lookback and
  barrier option payoffs, then decide whether the planned transport-map and
  normalizing-flow discussion belongs in Deck 02. Choose the contracts and map
  direction during that review rather than in advance.
- Refactor the Asian-option sampling code so path construction and payoff
  interfaces can be reused for importance sampling and control variates in
  Deck 04.
- Reconsider a modern queueing simulation using SimPy. It may support the
  stochastic-process narrative here or become a larger selected application in
  Deck 05.
- If QMCPy's kernel abstraction has matured, consider using covariance kernels
  in the Gaussian-process material. Keep reusable implementation work in the
  standalone QMCSoftware repository.
- Add a reusable mixture-distribution feature to QMCPy in the standalone
  QMCSoftware repository, not the course repository's pinned submodule.

## Deck 03 — Markov Chain Monte Carlo

- Expand the sampler progression beyond basic Metropolis methods as time and
  narrative permit: ensemble sampling with `emcee`, Langevin MCMC,
  Hamiltonian Monte Carlo, and PyMC/NUTS as an automatic HMC demonstration.
- Decide whether those methods supplement or replace inherited
  parallel-tempering material. Preserve a coherent conceptual progression
  rather than accumulating a catalog of packages.
- Reconsider the queueing examples using SimPy, possibly with a small shim for
  a consistent course interface.

## Deck 04 — Improving Efficiency

- Expand the Asian-option example with importance sampling and control
  variates, building on reusable sampling/payoff architecture from Deck 02.
- Improve `nbviz` styling and explanatory overlays when modernizing that
  example.
- Modernize inherited GPU/CPU timing, stopping-criteria, and performance
  notebooks. Separate algorithmic efficiency from hardware timing and avoid
  claims tied to obsolete machines.
- Consider kernel herding and Bayesian cubature demonstrations if the QMCPy
  kernel abstraction is sufficiently complete and these topics support the
  efficiency narrative.

## Deck 05 — Selected Topics

- Add an accessible introduction to Monte Carlo tree search (MCTS), including
  exploration versus exploitation, upper confidence bounds for trees (UCT),
  and connections to stochastic optimization. It may be a short module or
  support an optional project.
- Modernize the inherited gradient/stochastic-gradient notebook and clarify
  its connection to Monte Carlo methods.
- Consider queueing simulation here if developed as a substantial application
  rather than a sampling example in Deck 02 or an MCMC example in Deck 03.
- Consider kernel herding and Bayesian cubature here if they are better framed
  as selected modern methods than as efficiency techniques in Deck 04.

## Cross-course notebooks and workflow

- Align retained older notebooks with the current `classlib`/`nbviz` workflow,
  notation, and visual conventions rather than mechanically porting them.
- Add periodic full-repository notebook execution to detect dependency and
  runtime breakage before students encounter it.
- Test the documented student installation workflow in a clean macOS user or
  fresh environment and simplify the Conda/QMCPy instructions based on the
  result.
- Continue the established Quarto architecture and unified visual style;
  reevaluate Jupyter Book only if it offers a concrete capability the current
  workflow lacks.

These items incorporate the durable ideas from the read-only Fall 2025
planning document `MATH565Fall2025/MATH565_Improvements.md`, version
2025.11.28. They are prompts for later deck development, not commitments to
include every item.
