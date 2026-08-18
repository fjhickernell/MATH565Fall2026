# Decisions

This file records important course, repository, and design decisions together
with the rationale behind them. Add entries when future maintainers or agents
would benefit from understanding why a choice was made.

## Decision log

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
