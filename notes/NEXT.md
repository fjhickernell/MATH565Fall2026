# Next task

## Current task

Review the notebooks associated with Deck 02, Generating Samples, and align
them with the completed lecture deck.

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
- `slides/02-generating-samples.qmd` has completed its instructor-led content
  review, visible-layout refinement, and guidance audit. It restores the
  important worked examples from the Fall 2025 Keynote deck, uses the approved
  course-tree markers and terminology, and links its cumulative terms into
  Deck 01.
- Both Decks 01 and 02 render successfully, and their internal links resolve.
- The notebook catalog currently describes the intended Deck 02 sampling
  topics, but the corresponding notebooks still need to be reviewed and
  curated against the finished lecture narrative.
- MCTS will be covered in a later slide deck and does not belong in the
  Introduction deck; the specific later deck remains to be chosen.
- The Fall 2025 Keynote deck is the initial content and pedagogical reference
  for Lecture 02. Preserve its mathematical substance, examples, sequence,
  and emphasis as closely as the Quarto format reasonably allows.

## Questions to resolve

- Which existing or inherited notebooks should be retained, revised, combined,
  or omitted for Deck 02?

## Constraints

- Treat Deck 02 as the authoritative mathematical narrative; notebooks should
  support computation and exploration without duplicating the slides.
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

- The Deck 02 notebook set has an instructor-approved scope.
- Each retained notebook executes cleanly with the `qmcpy` kernel and uses
  notation and terminology consistent with the lecture deck.
- The notebook page and relevant deck links point to the curated notebooks.
