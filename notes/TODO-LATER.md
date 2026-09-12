# Todo Later

This file tracks deferred work and lower-priority tasks that should remain
visible without crowding the active project plan or status. Entries should
state why the work was deferred when that context will matter later.

Deck headings identify the current main development, not exclusive ownership.
A topic or notebook may be previewed, developed, revisited, or extended across
multiple decks.

## Parked review questions

- Choose an overarching text or chapter reference for Deck 05; the Fall 2025
  title slide says only `Owen, Chapters ???`.
- In a later citation pass, decide whether to add the Hickernell (1998) and
  Gretton et al. (2012) discrepancy references to shared `classlib` metadata
  and cite them in the deck.

## Deck 02 — Generating Samples

- Refactor the Asian-option sampling code so path construction and payoff
  interfaces can be reused for importance sampling and control variates in
  Deck 04, starting from the retained `GeneratingSamples.ipynb` examples.
  The separate `FinancialOptionPayoffs.ipynb` proposal was closed without
  creating that notebook; it is not a prerequisite. Decide the reusable
  code organization while developing `AsianOptionVarianceReduction.ipynb`.
- If QMCPy's kernel abstraction has matured, consider using covariance kernels
  in the Gaussian-process material. Keep reusable implementation work in the
  standalone QMCSoftware repository.
- Add a reusable mixture-distribution feature to QMCPy in the standalone
  QMCSoftware repository, not the course repository's pinned submodule.

## Deck 03 — Markov Chain Monte Carlo

- The course-owned Metropolis, Bayesian, and discrepancy notebooks now retain
  the non-queueing 2025 material. Parallel tempering follows mode trapping in
  Metropolis and recurs in the Bayesian application; it is no longer deferred.
- The Bayesian notebook links the official PyMC API quickstart as an optional
  supplement. Consider a course-owned PyMC/NUTS extension only after assessing
  dependency burden and a distinct teaching purpose. Langevin and hand-built
  Hamiltonian Monte Carlo remain possible later extensions.
- The queueing companion now uses SimPy 4.1.2 with course-owned process and
  measurement code. The current review is complete; further queueing extensions remain optional.

## Deck 04 — Improving Efficiency

- Create `AsianOptionVarianceReduction.ipynb` with importance sampling and
  control variates, reusing or extracting the sampling/payoff code retained in
  `GeneratingSamples.ipynb`; no separate financial-payoff notebook is required.
- Improve `nbviz` styling and explanatory overlays when modernizing that
  example.
- Modernize retained stopping-criteria notebook material and keep algorithmic
  efficiency distinct from hardware timing.
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
- Modernize the inherited GPU/CPU timing notebook as a separate selected-topic
  demonstration. Qualify backend, synchronization, precision, and
  machine-specific timing results.
- Consider queueing simulation here if developed as a substantial application
  rather than the current Markov-chain application in Deck 03.
- Consider kernel herding and Bayesian cubature here if they are better framed
  as selected modern methods than as efficiency techniques in Deck 04.

## Deferred course logistics

- Create or adapt separate Microsoft Bookings pages for Fall 2026 presenter
  and observer project sign-ups, following the Fall 2025 workflow. Add the
  finalized links and procedures to the project page. This remains Blue on
  the Dashboard until activated.

## Cross-course notebooks and workflow

- Consider adding an `all` mode to the shared `quarto-slides-live` helper.
  `quarto-slides-live all` would render every deck initially, serve the common
  `slides/_site` output, and rebuild all decks when slide or shared-style
  sources change, so navigation always reaches current local output. The
  tradeoff is slower rebuilds than the existing single-deck mode; do not
  implement this without a separate request.
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
