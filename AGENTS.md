# AGENTS.md

At the beginning of every new Codex session, follow the document-reading order
under "Before editing"; inspect the current Git status, submodule status, and
recent commits; and reconstruct the current project state from the repository.
Do not rely on memory from prior chat sessions.

## Repository shorthand

Within the current teaching workspace:

- `332` refers to the most recent MATH 332 course repository.
- `565` refers to the most recent MATH 565 course repository.

If older course repositories are also open in the workspace, refer to them
explicitly by year (e.g., `565-2025` or `MATH565Fall2025`) to avoid ambiguity.

## Repository purpose

This is the active, authoritative MATH 565 course repository. It contains the
Fall 2026 course website and course materials.

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
- The most recent MATH 332 repository is a separate active course repository.
  Do not modify it during MATH 565 work unless the task explicitly includes
  MATH 332.
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

Read `notes/NEXT.md` early in each work session. Treat it as the current
cross-session handoff, not as authorization to begin its task without the
user's request. Before a checkpoint, update it when the immediate next task
has changed; keep longer-term work in `notes/TODO-LATER.md`.

### Next-task shorthand

Interpret `Next?` as a request to read and summarize `notes/NEXT.md` from both
active repositories, `MATH332Fall2026` and `MATH565Fall2026`. Interpret
`Next 332?` and `Next 565?` as requests for only the named course. Read the
files each time rather than relying on conversation memory. Reporting a next
task does not authorize beginning it.

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

## Institutional memory

The `notes/` directory is this repository's institutional memory. Agents
should consult its files when planning work, proposing changes, drafting or
revising course materials, or making architectural decisions.

These files document design intent, rationale, deferred ideas, and
implementation knowledge. Detailed institutional memory belongs there rather
than in this concise `AGENTS.md` file.

The files under `notes/` are not student-facing course content and must not be
treated as source material for lectures, slides, notebooks, assignments,
exams, or the course website.

Content from `notes/` should appear in student-facing materials only after it
has been intentionally incorporated into those materials or when the user
explicitly requests it.

## Git and checkpoints

Do not commit or push during ordinary intermediate work unless the user asks.

The word **"Finished"** has no special meaning. Treat it as ordinary
conversation unless the user explicitly asks to commit or push.

Only these two checkpoint commands are recognized:

- `Checkpoint`
- `Checkpoint <commit message>`

Either command is explicit authorization to validate, document durable
conventions when needed, stage every modified or untracked non-ignored file,
commit the complete repository state, and push the current branch. A
checkpoint is a preservation snapshot, not a task-scoped commit: do not omit a
change merely because it was created by the user, predates the current task,
or appears unrelated. Files properly ignored by Git remain excluded. For
`Checkpoint <commit message>`, use the text after `Checkpoint ` as the exact
commit message. For `Checkpoint`, construct a concise commit message that
accurately describes the complete set of changes.

1. Inspect the authoritative repository and every submodule recursively using
   status output that includes all untracked files.
2. Inventory every tracked modification and every untracked, non-ignored file
   in the authoritative repository and any writable repository in scope, such
   as `classlib`.
3. Run appropriate validation for the complete set of changes before
   committing.
4. Decide whether the work established a permanent convention or workflow
   that belongs in developer documentation such as `docs/slide-style.md`,
   `AUTHOR_WORKFLOW.md`, or another appropriate file. Document durable
   guidance when needed, but do not record transient debugging or failed
   attempts.
5. When `classlib` contains non-ignored changes, include all of them and
   publish `classlib` using the arrive/validation/depart sequence documented
   under "Propagating classlib changes" in `AUTHOR_WORKFLOW.md`.
6. Update the authoritative repository's `classlib` submodule pointer if
   needed.
7. Stage every modified and untracked non-ignored file in the authoritative
   repository and create the commit using the requested or constructed
   message.
8. Push the current branch.
9. Confirm that the authoritative course repository and every writable
   repository in scope are clean and synchronized with their upstream
   branches. Confirm that pinned read-only submodules remain unchanged.
10. Report the commit hash, confirmation that the push succeeded, whether
    documentation was updated and where, and any remaining follow-up items.

Never include changes from `qmcsoftware`, `assets/tests/archive`, or either
reference repository in this checkpoint workflow. If any protected read-only
repository is dirty, do not discard or silently omit its work and do not claim
the checkpoint is complete; report the blocker and obtain user direction.
