# MATH 565 Fall 2026 Project Plan

## Repository roles

These project-specific values define the repositories used by this plan:

- **Authoritative repository:** `MATH565Fall2026`
- **Architecture reference:** `MATH563Spring2026`
- **Course-material reference:** `MATH565Fall2025`

The authoritative repository is the writable home of the completed course.
The two reference repositories are read-only. `classlib` is the writable
shared academic library, while `qmcsoftware` is a read-only pinned dependency
whose checked-out commit and submodule pointer must remain unchanged.
`HickernellTestArchive` is a permanent read-only pinned submodule mounted at
`assets/tests/archive`; it supports references to archived material without
duplicating that material in the authoritative repository.

Local builds and automation initialize submodules recursively at the commits
recorded by `MATH565Fall2026`, without overriding them with moving branch tips.

## Purpose

The authoritative repository maintains the course website, lecture slides,
course pages, and supporting materials. It delivers Monte Carlo and
quasi-Monte Carlo instruction through a coherent, reproducible Quarto project
that can be developed, rendered, and published across machines.

## Project vision

Migrate the course-material reference from its Jekyll website and Apple
Keynote lecture workflow to a modern Quarto-based course. Preserve the
mathematical substance, pedagogical sequence, examples, assignments,
notebooks, and supporting resources while improving clarity, consistency,
accessibility, and maintainability.

Reuse the proven Quarto organization and presentation conventions of the
architecture reference, together with shared infrastructure from `classlib`,
wherever they fit. The result should feel like a current member of the same
course-site family while remaining specific to MATH 565.

## Guiding principles

- Reuse proven components and patterns rather than reinventing them.
- Keep reusable styling, metadata, snippets, and teaching infrastructure in
  `classlib`.
- Keep course content, navigation, schedules, and course-specific assets in
  the authoritative repository.
- Use the architecture reference to decide how the course is structured and
  the course-material reference to decide what the course teaches.
- Make incremental, verifiable improvements rather than an all-at-once
  conversion.
- Preserve mathematical correctness and pedagogical intent during format
  changes.
- Keep source files understandable to future instructors and Codex sessions.
- Commit source and durable project documentation, not generated site output.

## Target architecture

The completed repository is organized around these layers:

- **Website:** Root `_quarto.yml` and `index.qmd` define the course website,
  navigation, shared resources, and deployment inputs. The main render
  excludes the independent slide project.
- **Slides:** `slides/` is a RevealJS Quarto project containing one
  maintainable source deck per lecture or coherent teaching unit. Rendered
  slides are staged under the published website's `slides/` path.
- **Pages:** `pages/` contains course-specific schedules, assignments,
  notebooks, tests, projects, and other student-facing information.
- **Assets:** `assets/` contains course-specific images, documents, data, and
  other static resources. Shared visual or instructional assets belong in
  `classlib`.
- **Reusable infrastructure:** `classlib/` supplies common Quarto styling,
  layouts, metadata, pages, snippets, notebooks, and teaching utilities.
  `qmcsoftware/` remains a pinned software dependency.
- **Supporting documentation:** `README.md`, `PLAN.md`, `STATUS.md`,
  `AUTHOR_WORKFLOW.md`, and `AGENTS.md` preserve project purpose, direction,
  construction history, author procedures, and agent behavior.
- **Automation:** GitHub Actions renders the website and slides from source,
  combines their output, and publishes it without committing rendered
  artifacts to `main`.

## Development strategy

1. Establish and verify the Quarto website, slide, shared-resource, and
   deployment framework before large-scale content conversion.
2. Convert one representative lecture into a complete prototype, including
   mathematics, examples, assets, code execution, slide navigation, and links
   from the website.
3. Validate the prototype locally and through deployment, including rendering,
   navigation, styling, dependency setup, and cross-machine reproducibility.
4. Refine reusable patterns in `classlib` and course-specific conventions in
   the authoritative repository based on the prototype.
5. Apply the validated pattern to remaining lectures and supporting course
   content in coherent increments.
6. Continuously test website and slide rendering, links, navigation,
   executable examples, and published output as the course grows.

This strategy defines durable direction rather than individual tasks.
Detailed construction work and completion history belong in `STATUS.md`.

## Quality goals

- **Correctness:** Mathematical notation, claims, algorithms, examples,
  assignments, and executable results are accurate and preserve the intended
  pedagogy.
- **Maintainability:** Sources use consistent Quarto patterns, clear
  organization, minimal duplication, and documented conventions.
- **Reproducibility:** A fresh clone with initialized submodules and documented
  dependencies can render the website and slides through the author workflow.
- **Cross-machine continuity:** Git-tracked sources, pinned submodules, and
  durable project documents carry necessary context between computers and
  Codex sessions without relying on local generated state.
- **Separation of concerns:** Reusable code and presentation infrastructure
  live in `classlib`; course-specific content and configuration remain in the
  authoritative repository; read-only dependencies and references remain
  unmodified.
- **Verifiability:** Changes are small enough to review and are validated at
  the page, deck, navigation, and complete-site levels as appropriate.

## Relationship to other project documents

- `README.md` introduces the repository to human readers and provides
  essential setup and entry points.
- `PLAN.md` records what is being built, why, and the durable development
  strategy; it changes only when that direction changes.
- `STATUS.md` records completed and remaining construction work as a durable,
  phase-organized checklist.
- `AUTHOR_WORKFLOW.md` documents practical setup, preview, rendering, and
  publishing procedures for course authors.
- `AGENTS.md` defines how Codex behaves, protects repository boundaries, and
  completes work.
