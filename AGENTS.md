# AGENTS.md

## Repository purpose

This repository contains the MATH 565 Fall 2026 course website and course
materials.

## Repository roles

- `MATH565Fall2026` is the target repository. Write course-site changes here.
- `MATH565Fall2026/classlib` is the Hickernell Academic Library submodule.
  Changes may be made here when needed for the course.
- `MATH565Fall2026/qmcsoftware` is a read-only QMCSoftware submodule. Do not
  edit, commit, push, change its checked-out commit, or update its submodule
  pointer.
- `MATH563Spring2026` is a read-only architecture reference. Follow its Quarto
  project organization and Quarto styling when building this site.
- `MATH565Fall2025` is a read-only content reference. Adapt its course content
  for Fall 2026, but do not copy its obsolete Jekyll architecture or
  Apple Keynote workflow.
- Do not write to any other repository unless the user explicitly changes
  these instructions.

## Before editing

Before beginning substantial work, read these project documents when they
exist, in this order:

- `README.md` — project purpose
- `PLAN.md` — long-term strategy
- `PROJECT_STATUS.md` — current construction status
- `AUTHOR_WORKFLOW.md` — author workflow
- `AGENTS.md` — agent behavior

Before substantial work, inspect the state of each repository relevant to the
task. Never overwrite, discard, or commit pre-existing user changes. Run the
established synchronization workflow only when required by the project's
synchronization rules or when the user explicitly requests it. Reference
repositories remain read-only; their tracked files must not be changed.

Report any divergence, dirty worktree, unavailable remote, or submodule
mismatch before proceeding if it could affect the requested work.

## Durable project memory

Git-tracked project documents—`README.md`, `PLAN.md`, `PROJECT_STATUS.md`, and
`AGENTS.md`—are the durable project memory shared across machines and Codex
sessions.

## PROJECT_STATUS.md

`PROJECT_STATUS.md` is the repository's durable construction checklist.
Maintain it as a historical record of how the repository was built:

- Completed items remain checked and visible.
- Do not remove completed items simply because they are finished.
- Insert new tasks in the appropriate construction phase.
- Preserve the checklist as a record of the repository's construction.

## Architecture and content

Use `MATH563Spring2026` as the source of truth for architecture, including
Quarto configuration, navigation, layouts, themes, styling, and the general
course-site build approach.

Use `MATH565Fall2025` as the source of truth for MATH 565 course content.
Translate that content into the Fall 2026 Quarto architecture. Treat its
Jekyll implementation and Apple Keynote files as legacy references, not as
the target toolchain.

Preserve the boundary between course-specific files and reusable academic
library code. Put reusable library changes in `classlib`; put Fall 2026
course-site changes in the target repository.

## Git and completion

Do not commit or push during ordinary intermediate work unless the user asks.

When the user instructs **"Finished"**:

1. Review only the changes associated with the current task in
   `MATH565Fall2026` and `classlib`.
2. Identify and avoid committing unrelated user work.
3. Run appropriate validation for the task's changes before committing.
4. When the task includes intended `classlib` changes, publish `classlib`
   using the established project workflow.
5. Update the target repository's `classlib` submodule pointer if needed.
6. Commit and push the current task's intended `MATH565Fall2026` changes.
7. Confirm that both repositories are clean and synchronized with their
   upstream branches.

Never include changes from `qmcsoftware` or any reference repository in this
completion workflow.
