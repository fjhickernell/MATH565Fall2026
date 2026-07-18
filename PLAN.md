# MATH 565 Fall 2026 Project Plan

## Purpose

This repository is the maintained source for the MATH 565 Fall 2026 course
website, lecture slides, course pages, and supporting materials. It exists to
deliver Monte Carlo and quasi-Monte Carlo instruction through a coherent,
reproducible Quarto project that can be developed, rendered, and published
across machines.

## Project Vision

Migrate the Fall 2025 course from its Jekyll website and Apple Keynote lecture
workflow to a modern Quarto-based course. Preserve the mathematical substance,
pedagogical sequence, examples, assignments, notebooks, and supporting
resources while improving their clarity, consistency, accessibility, and
maintainability.

Reuse the proven Quarto architecture of MATH563Spring2026 and shared
infrastructure from `classlib` wherever they fit. The completed repository
should feel like a current member of the same course-site family, while
remaining specific to the needs of MATH 565.

## Guiding Principles

- Reuse proven components and patterns rather than reinventing them.
- Keep reusable styling, metadata, snippets, and teaching infrastructure in
  `classlib`.
- Keep MATH 565 content, navigation, schedules, and course-specific assets in
  this repository.
- Separate architectural decisions from content migration decisions.
- Make incremental, verifiable improvements instead of performing an
  all-at-once conversion.
- Preserve mathematical correctness and pedagogical intent during format
  changes.
- Keep source files understandable to future instructors and future Codex
  sessions.
- Commit source and durable project documentation, not generated site output.

## Sources of Truth

| Source | Role |
|---|---|
| `MATH563Spring2026` | Read-only architecture reference for Quarto project organization, website and slide configuration, navigation patterns, styling, rendering, and deployment. |
| `MATH565Fall2025` | Read-only course-content reference for lecture material, mathematical development, examples, assignments, notebooks, policies, schedules, and assessments. Its Jekyll and Apple Keynote implementation is legacy, not target architecture. |
| `classlib` | Writable shared library for reusable styling, metadata, snippets, notebooks, pages, and instructional infrastructure that should serve more than this course. |
| `qmcsoftware` | Read-only pinned dependency providing QMCPy software and examples used by the course. Course work must not modify it or its submodule pointer. |
| `MATH565Fall2026` | Authoritative home for the completed Fall 2026 course: course-specific Quarto sources, configuration, navigation, content, assets, documentation, and the pinned `classlib` revision. |

When sources overlap, use MATH563Spring2026 to answer *how the course is
structured* and MATH565Fall2025 to answer *what MATH 565 teaches*. Resolve the
result in this repository, moving only genuinely reusable improvements into
`classlib`.

## Target Architecture

The completed repository is organized around these layers:

- **Website:** Root `_quarto.yml` and `index.qmd` define the course website,
  navigation, shared resources, and deployment inputs. The main render
  excludes the independent slide project.
- **Slides:** `slides/` is a RevealJS Quarto project containing one
  maintainable source deck per lecture or coherent teaching unit. Its rendered
  output is staged under the published website's `slides/` path.
- **Pages:** `pages/` contains course-specific schedules, assignments,
  notebooks, tests, projects, and other student-facing information.
- **Assets:** `assets/` contains course-specific images, documents, data, and
  other static resources. Shared visual or instructional assets belong in
  `classlib`.
- **Reusable infrastructure:** `classlib/` supplies common Quarto styling,
  layouts, metadata, pages, snippets, and notebooks. `qmcsoftware/` remains a
  pinned software dependency.
- **Supporting documentation:** `README.md`, `PLAN.md`,
  `PROJECT_STATUS.md`, `AUTHOR_WORKFLOW.md`, and `AGENTS.md` preserve project
  purpose, direction, construction history, author procedures, and agent
  behavior.
- **Automation:** GitHub Actions renders the website and slides from source,
  combines their output, and publishes the result without committing rendered
  artifacts to `main`.

## Development Strategy

1. Establish and verify the Quarto website, slide, shared-resource, and
   deployment framework before large-scale content conversion.
2. Convert one representative lecture into a complete prototype, including
   mathematics, examples, assets, code execution, slide navigation, and links
   from the website.
3. Validate the prototype workflow locally and through deployment. Confirm
   rendering, navigation, styling, dependency setup, and cross-machine
   reproducibility.
4. Refine reusable patterns in `classlib` and course-specific conventions in
   this repository based on the prototype.
5. Scale the validated pattern to the remaining lectures and supporting
   course content in coherent increments.
6. Continuously test website and slide rendering, internal and external
   links, navigation, executable examples, and published output as the course
   grows.

This strategy defines direction rather than individual tasks. Detailed
construction work and its completion history belong in `PROJECT_STATUS.md`.

## Quality Goals

- **Correctness:** Mathematical notation, claims, algorithms, examples,
  assignments, and executable results are accurate and preserve the intended
  pedagogy.
- **Maintainability:** Sources use consistent Quarto patterns, clear
  organization, minimal duplication, and documented conventions.
- **Reproducibility:** A fresh clone with initialized submodules and documented
  dependencies can render the website and slides through the author workflow.
- **Cross-machine continuity:** Git-tracked sources, pinned submodules, and
  durable project documents carry the necessary context between computers and
  Codex sessions without relying on local generated state.
- **Separation of concerns:** Reusable code and presentation infrastructure
  live in `classlib`; Fall 2026 content and configuration remain here;
  `qmcsoftware` and reference repositories remain unmodified.
- **Verifiability:** Changes are small enough to review and are validated at
  the page, deck, navigation, and complete-site levels as appropriate.

## Relationship to Other Project Documents

- `README.md` introduces the repository to human readers and provides the
  essential setup and entry points.
- `PLAN.md` describes the project's durable direction, target architecture,
  and development strategy; it changes only when that direction changes.
- `PROJECT_STATUS.md` records construction progress as a durable,
  phase-organized checklist and history.
- `AGENTS.md` defines how Codex operates in this repository, including scope,
  safeguards, references, and completion behavior.
- `AUTHOR_WORKFLOW.md` documents the practical setup, preview, rendering, and
  publishing workflow for course authors.
