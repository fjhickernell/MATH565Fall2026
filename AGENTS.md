# AGENTS.md

## Repository purpose

This repository contains the MATH 565 Fall 2026 course website and course
materials.

## Repository boundaries

- Write course-specific changes only in this authoritative repository.
- `classlib` is a writable submodule for genuinely reusable academic-library
  code and presentation infrastructure.
- `qmcsoftware` is read-only. Do not edit, commit, push, change its checked-out
  commit, or update its submodule pointer.
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
7. Confirm that both repositories are clean and synchronized with their
   upstream branches.

Never include changes from `qmcsoftware` or either reference repository in
this completion workflow.
