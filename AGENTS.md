# AGENTS.md

At the beginning of every new Codex session, follow the document-reading order
under "Before editing"; inspect the current Git status, submodule status, and
recent commits; and reconstruct the current project state from the repository.
Do not rely on memory from prior chat sessions.

## Repository purpose

This repository contains the MATH 565 Fall 2026 course website and course
materials.

## Repository boundaries

- Write course-specific changes only in this authoritative repository.
- `classlib` may be edited only for genuinely reusable academic-library code
  and presentation infrastructure. Validate, commit, and push an intended
  change in `HickernellAcademicLib` first, then intentionally update the
  `classlib` pointer in this repository. Never advance the pointer merely
  because a newer `classlib` commit exists.
- `qmcsoftware` and `assets/tests/archive` (`HickernellTestArchive`) are
  read-only pinned dependencies unless the user explicitly authorizes a
  change.
- Routine builds and deployment must initialize the recorded submodule commits
  recursively and must not use `git submodule update --remote`.
- The architecture and course-material reference repositories named in
  `PLAN.md` are read-only.
- Do not write to any other repository unless the user explicitly changes
  these instructions.

## Before editing

Before substantial work, read these documents when they exist, in this order:

1. `README.md`
2. `PLAN.md`
3. `STATUS.md`
4. `AUTHOR_WORKFLOW.md`
5. `AGENTS.md`

Before making substantial slide changes, also read `docs/slide-style.md`.
Before making substantial page changes, also read `docs/pages-style.md`.

Inspect the state of every repository relevant to the task. Never overwrite,
discard, or commit pre-existing user changes. Run the established
synchronization workflow only when required by the project's synchronization
rules or explicitly requested by the user. Keep reference repositories
read-only.

Report any divergence, dirty worktree, unavailable remote, or submodule
mismatch before proceeding when it could affect the requested work.

Follow the repository roles and target architecture defined in `PLAN.md`.
Keep course-specific work in the authoritative repository, move only genuinely
reusable infrastructure into `classlib`, and leave read-only dependencies and
references unchanged.

## Durable project memory

Git-tracked project documents—especially `README.md`, `PLAN.md`, `STATUS.md`,
and `AGENTS.md`—are durable project memory shared across machines and Codex
sessions. Update the appropriate document when work changes repository
purpose, strategy, construction state, workflow, or agent behavior.

`STATUS.md` is the durable construction checklist. Completed items remain
checked and visible; insert new tasks in the appropriate phase, and do not
remove completed work merely because it is finished.

## Git and completion

Do not commit or push during ordinary intermediate work unless the user asks.

When the user instructs **"Finished"**, complete the workflow below. If text
follows `Finished:`, use that text as the commit message. If the user says only
`Finished`, construct a concise commit message that accurately describes the
current task's intended changes.

1. Review only the changes associated with the current task in the
   authoritative repository and `classlib`.
2. Identify and avoid committing unrelated user work.
3. Run appropriate validation for the task's changes before committing.
4. When the task includes intended `classlib` changes, publish `classlib`
   using the established project workflow.
5. Update the authoritative repository's `classlib` submodule pointer if
   needed.
6. Commit and push the current task's intended authoritative-repository
   changes.
7. Confirm that the authoritative course repository and any intentionally
   modified writable repositories, such as `classlib`, are clean and
   synchronized with their upstream branches. Confirm that pinned read-only
   submodules remain unchanged.

Never include changes from `qmcsoftware`, `assets/tests/archive`, or either
reference repository in this completion workflow.
