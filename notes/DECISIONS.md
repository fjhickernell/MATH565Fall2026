# Decisions

This file records important course, repository, and design decisions together
with the rationale behind them. Add entries when future maintainers or agents
would benefit from understanding why a choice was made.

## Decision log

### 2026-09-02 — Put mixtures in the survey and combine transport with acceptance--rejection

- **Decision:** Add one compact Gaussian-mixture section to
  `sampling/GeneratingSamples.ipynb` and create one focused
  `sampling/TransportMapsAndAcceptanceRejection.ipynb`. Do not create separate
  mixture/transport and acceptance--rejection notebooks.
- **Rationale:** Mixture sampling is a basic hierarchical construction that
  belongs beside the other direct constructions in `GeneratingSamples`, but
  that notebook is already full and should receive only a small addition.
  Transport and acceptance--rejection answer the same question in contrasting
  ways: move every proposal or keep selected proposals. A shared target and
  proposal make that comparison visible without duplicating setup.
- **Consequences:** The combined notebook reuses the Deck 02
  $\operatorname{Beta}(2,1)$/Uniform example, the triangular flow, and a
  narrowed portion of the Fall 2025 acceptance--rejection notebook. Deck 03
  calls back to it when motivating MCMC, and Deck 04 calls back to it when
  comparing exact transport with importance sampling.

### 2026-08-08 — Place MCTS in Selected Topics

- **Decision:** Do not add Markov chain tree search (MCTS) to the Introduction
  deck; cover it in Deck 05, Selected Topics, the final deck.
- **Rationale:** MCTS is a tree-search and sequential-decision method that uses
  exploration and exploitation; it is not an MCMC method for sampling a target
  distribution. Selected Topics preserves that distinction and allows the
  module to connect naturally to stochastic optimization or an optional
  project.
- **Consequences:** Finish `slides/01-introduction.qmd` without an MCTS
  example and include MCTS when developing `slides/05-selected-topics.qmd`.
