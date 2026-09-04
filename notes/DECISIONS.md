# Decisions

This file records important course, repository, and design decisions together
with the rationale behind them. Add entries when future maintainers or agents
would benefit from understanding why a choice was made.

## Decision log

### 2026-09-04 — Route the mutable tutoring schedule through Canvas

- **Decision:** The public course website tells enrolled students that Fall
  2026 Math Tutoring Center support is available in RE 129 and online, then
  routes them to Canvas. The Canvas Welcome page links directly to the faculty
  coordinator's original Google Drive PDF; do not upload or copy the PDF into
  Canvas or the course repository.
- **Rationale:** The coordinator may revise the schedule in place, and the PDF
  contains an online-tutoring Zoom link with its passcode. Referencing the
  original file preserves updates, while keeping its URL off the public course
  website reduces public discovery.
- **Consequences:** Do not add the Google Drive or Zoom URL to public course
  sources or metadata. Canvas authentication limits casual public exposure but
  cannot prevent students from forwarding an anyone-with-the-link file. The
  coordinator should restrict the Drive file to the intended Illinois Tech
  audience, and the Zoom meeting should use appropriate authentication or a
  waiting room, when feasible.

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
