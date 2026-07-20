# MATH 565 Fall 2026 Construction Status

This checklist is the durable record of how the repository was built.
Completed items remain checked and visible. Unfinished tasks remain ordered
approximately by intended execution, and new work should be inserted into the
appropriate phase rather than appended indiscriminately.

## 1. Repository foundation

- [x] Create the authoritative course repository.
- [x] Establish the root Quarto website skeleton.
- [x] Add the `classlib` and `qmcsoftware` submodules.
- [x] Create the core `pages/`, `slides/`, and `assets/` directories.
- [x] Add the course landing page and basic website navigation.
- [x] Add `README.md` with the course purpose and local setup instructions.
- [ ] Confirm that a fresh clone with recursive submodules installs all
  documented dependencies successfully.

## 2. Project governance and durable memory

- [x] Add `AGENTS.md` with repository boundaries, safeguards, and completion
  behavior.
- [x] Add `PLAN.md` with the project vision, target architecture, and durable
  development strategy.
- [x] Add `AUTHOR_WORKFLOW.md` with author setup, preview, render, and
  publishing procedures.
- [x] Add `STATUS.md` as the permanent phase-organized construction record.
- [ ] Reconcile project documentation whenever repository strategy or author
  workflow changes.

## 3. Website framework

- [x] Configure the root Quarto website project.
- [x] Create initial course-page source files.
- [ ] Verify that GitHub Actions renders the site successfully.
- [ ] Complete student-facing website pages, see `_quarto.yml`
  navbar:
  - [ ] Welcome (`index.qmd`)
    - [x] Verify course title, semester, and course identity.
    - [x] Review and update the course description.
    - [x] Verify instructor information, photograph, and links.
    - [ ] Verify teaching-assistant information or clearly mark unknown
      details.
    - [x] Review textbook and recommended resources.
    - [x] Review prerequisites and requirements.
    - [x] Review course objectives and outline.
    - [x] Verify “Where to Find It” and other internal course links.
    - [x] Review assessment categories, percentages, and links.
    - [x] Correct Markdown and Quarto formatting issues.
    - [x] Validate Quarto rendering and generated page structure.
    - [ ] Inspect the visible page layout in a browser.
  - [ ] Stats Qs (`classlib/classlib/quarto/pages/stats-qs.qmd`)
    - [x] Verify navbar link.
    - [x] Verify page renders correctly.
    - [ ] Inspect visible browser layout.
    - [x] Confirm no course-specific customization is presently required.
  - [ ] Schedule (`pages/schedule.qmd`)
    - [x] Create the Fall 2026 Tuesday/Thursday meeting calendar.
    - [x] Verify the August 18 start date and December 3 final regular
      meeting.
    - [x] Mark Thanksgiving Day, November 26, as no class.
    - [x] Record the classroom as TBA.
    - [x] Add a TBA final-exam entry for the following week.
    - [x] Leave unknown topics, materials, and additional dates blank.
    - [x] Validate Quarto rendering and generated page structure.
    - [ ] Inspect the visible page layout in a browser.
  - [ ] Notebooks (`pages/notebooks.qmd`)
    - [x] Introduce the role of notebooks in MATH 565.
    - [x] Organize future links under Sampling, Applications, and
      Performance.
    - [x] Clearly mark notebook migration as in progress without adding
      placeholder links.
    - [x] Record the detailed Fall 2025 inventory, target paths,
      dependencies, concerns, and migration order in
      `notebooks/NOTEBOOK_INVENTORY.md`.
    - [ ] Create the target directories and migrate notebooks incrementally
      according to `notebooks/NOTEBOOK_INVENTORY.md`.
    - [ ] Add notebook links only after each target exists and passes
      validation.
    - [x] Validate Quarto rendering and generated page structure.
    - [ ] Inspect the visible page layout in a browser.
  - [ ] Assignments (`pages/homework.qmd`)
    - [x] Create the initial Fall 2026 assignments-page structure.
    - [x] Record the currently established assignment ground rules.
    - [x] Leave assignment details and due dates pending rather than inventing
      them.
    - [ ] Add assignment entries and due dates as they are finalized.
    - [x] Validate Quarto rendering and generated page structure.
  - [ ] Tests (`pages/tests.qmd`)
    - [x] Create the initial Fall 2026 tests-page skeleton and provisional
      instructions.
    - [x] Add and initialize `HickernellTestArchive` at
      `assets/tests/archive`.
    - [x] Leave test dates, coverage, rooms, final-exam details, and current
      PDFs marked TBA.
    - [x] Connect the shared archive-search instructions and dynamic MATH 565
      archive listing.
    - [x] Adopt the established test and examination instructions.
    - [ ] Finalize coverage, rooms, final-exam date/time/location, and current
      PDF links.
    - [x] Validate recursive submodule initialization and archive enumeration.
    - [x] Validate Quarto rendering and generated page structure.
    - [ ] Inspect the visible page layout in a browser.
  - [ ] Project (`pages/project.qmd`)
  - [ ] Policies (`classlib/classlib/quarto/pages/policies.qmd`)
  - [ ] Accessing repo
    (`classlib/classlib/quarto/pages/git-clone-update-with-submodules.qmd`)
  - [ ] Interesting articles & links
    (`classlib/classlib/quarto/pages/interesting-articles-links.qmd`)
  - [ ] IMS Student Membership
  - [ ] SIAM Student Membership
  - [ ] MATH 476 — Statistics
  - [ ] MATH 563 — Mathematical Statistics
  - [ ] QMCPy
- [x] Create the initial project-assessment page
  (`pages/project-assessment.qmd`), which is not currently a navbar
  destination.
- [x] Configure course-page metadata.
- [ ] Confirm that shared website styling and resources are sourced from
  `classlib` where appropriate.

## 4. Validation and deployment

- [x] Render the complete website successfully from a clean local setup.
- [x] Render the complete slide project successfully.
- [x] Stage slide output beneath the website output and verify the combined
  site.
- [ ] Validate internal links, external links, navigation, assets,
  mathematical notation, and executable examples.
- [x] Verify that generated output remains excluded from `main`.
- [x] Correct the GitHub Pages workflow to retain the parent-recorded recursive
  submodule commits without moving-branch overrides.
- [x] Validate GitHub Pages using the parent-recorded recursive submodule
  commits.
- [x] Establish and validate automated GitHub Pages deployment.
- [ ] Confirm that the published site matches local validated output.

## 5. Slide framework

- [x] Create an independent RevealJS Quarto project under `slides/`.
- [x] Add slide-project configuration and metadata.
- [x] Add an initial course-overview slide source.
- [ ] Validate shared slide styling, metadata, navigation, and assets from
  `classlib`.
- [ ] Confirm that rendered slides are linked correctly from the website.

## 6. Prototype lecture conversion

- [ ] Select a representative lecture from the course-material reference.
- [ ] Convert the lecture to a maintainable Quarto RevealJS source deck.
- [ ] Migrate its mathematical notation, examples, figures, and executable
  code without changing pedagogical intent.
- [ ] Verify website links, slide navigation, rendering, and local execution.
- [ ] Refine reusable slide and course conventions based on the prototype.
- [ ] Document any resulting author-workflow changes.

## 7. Remaining course-content migration

- [ ] Inventory lectures, assignments, notebooks, policies, schedules,
  assessments, and supporting resources in the course-material reference.
- [ ] Convert remaining lecture decks in coherent teaching units.
- [ ] Adapt course pages and policies to the authoritative repository.
- [ ] Migrate assignments, notebooks, examples, and required static assets.
- [ ] Review migrated material for obsolete dates, links, software
  instructions, and legacy Jekyll or Keynote assumptions.
- [ ] Move only genuinely reusable improvements into `classlib`.

## 8. Course readiness

- [ ] Verify the complete lecture sequence and course schedule.
- [ ] Confirm that assignments, notebooks, assessments, policies, and project
  materials are current for Fall 2026.
- [ ] Perform an accessibility and mobile-layout review.
- [ ] Perform a final mathematical and pedagogical review.
- [ ] Test the documented workflow on another machine or a fresh clone.
- [ ] Confirm that all student-facing pages and downloads are ready for the
  course launch.
