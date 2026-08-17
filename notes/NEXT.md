# Next task

## Current task

Continue the instructor-directed Deck 02 refinements one at a time. Next, add
lookback and barrier examples to the option-payoff discussion.

## Current state

- `slides/01-introduction.qmd` is complete and may be treated as the finished
  prototype for later lecture conversion; future polishing is optional rather
  than required follow-up.
- The Introduction deck renders cleanly, has an approved closing recap, and
  uses sparse course-tree markers to orient the mathematical sequence.
- `notebooks/applications/AreWeThereYet.ipynb` is complete,
  instructor-approved, and linked from the course notebook page and both
  travel-time slides.
- The shared AI-guidance slides are included from `classlib`; formal AI-policy
  review remains separate.
- `slides/02-generating-samples.qmd` has completed its initial instructor-led
  content review, visible-layout refinement, and guidance audit. It restores
  the important worked examples from the Fall 2025 Keynote deck, uses the
  approved course-tree markers and terminology, and links its cumulative terms
  into Deck 01.
- Four further refinements are planned, in order: a one-dimensional Gaussian
  mixture; CDF and quantile plots for the zero-inflated exponential; lookback
  and barrier option payoffs; and chained transformations, with careful use of
  transport-map and normalizing-flow terminology and a Gaussian-to-logistic
  boundary-behavior example informed by the MCQMC26 plenary material.
- The Gaussian mixture example is complete. It distinguishes the analytic PDF
  and CDF from the generally non-analytic mixture quantile, samples the
  discrete component before applying its normal quantile transform, and plots
  the two weighted component densities together with their mixture.
- The zero-inflated exponential example now pairs its CDF and quantile formulas
  with plots for $p_0=0.3$ and $\lambda=1$. The CDF plot marks the jump at zero,
  while the quantile plot marks the corresponding flat segment through $p_0$.
- Both Decks 01 and 02 render successfully, and their internal links resolve.
- The notebook catalog currently describes the intended Deck 02 sampling
  topics, but the corresponding notebooks still need to be reviewed and
  curated after the planned deck refinements are complete.
- MCTS will be covered in a later slide deck and does not belong in the
  Introduction deck; the specific later deck remains to be chosen.
- The Fall 2025 Keynote deck is the initial content and pedagogical reference
  for Lecture 02. Preserve its mathematical substance, examples, sequence,
  and emphasis as closely as the Quarto format reasonably allows.

## Questions to resolve

- Which lookback and barrier contracts best support the existing geometric
  Brownian motion narrative without overcrowding the payoff slide?
- For the later transformation-chain example, which terminology and map
  direction will be clearest while remaining mathematically precise?

## Constraints

- Treat Deck 02 as the authoritative mathematical narrative; notebooks should
  support computation and exploration without duplicating the slides.
- Complete the four new deck refinements in the instructor's requested order;
  do not begin the transformation-chain discussion before the option-payoff
  examples are approved.
- Use the completed Introduction deck as the local presentation and navigation
  prototype without reopening it as unfinished work.
- Strip out Fall 2025-specific logistics, including references to that
  semester's homework, assignments, due dates, tests, announcements, and
  other dated events; do not present them as Fall 2026 information.
- Keep MATH 565 course content in this repository and promote only genuinely
  reusable infrastructure to `classlib` after demonstrated reuse.
- Keep `qmcsoftware`, the test archive, and reference repositories read-only.
- Preserve MCTS for a later deck.

## Done when

- The option-payoff discussion includes mathematically precise lookback and
  barrier examples that fit the existing narrative and visible layout.
- The section outline, Big Ideas recap, and cumulative terms index are updated
  if the new material requires them.
- Decks 01 and 02 render cleanly, and all new internal links resolve.
