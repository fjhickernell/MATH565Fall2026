# MATH 565 Fall 2026 Construction Status

This checklist is the durable record of how the repository was built.
Completed items remain checked and visible. Unfinished tasks remain ordered
approximately by intended execution, and new work should be inserted into the
appropriate phase rather than appended indiscriminately.

## 1. Repository foundation

- [x] Create the authoritative course repository.
- [x] Establish the root Quarto website skeleton.
- [x] Add the `classlib` and `qmcpy` submodules.
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
- [x] Reconcile project documentation and style guides after establishing the
  prototype course conventions.

## 3. Website framework

- [x] Configure the root Quarto website project.
- [x] Create initial course-page source files.
- [x] Verify that GitHub Actions renders the site successfully.
- [ ] Complete student-facing website pages, see `_quarto.yml`
  navbar:
  - [ ] Welcome (`index.qmd`)
    - [x] Verify course title, semester, and course identity.
    - [x] Review and update the course description.
    - [x] Verify instructor information, photograph, and links.
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
    - [x] Record the classroom as PH 108.
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
      - [x] Create the Sampling, Applications, and Performance directories.
      - [x] Migrate `AreWeThereYet.ipynb` to Applications with modern minimal
        `classlib`/`nbviz` initialization and validate clean execution.
      - [x] Complete instructor review of `AreWeThereYet.ipynb` and finalize
        its mathematical explanations, plots, and method previews.
      - [x] Migrate `GeneratingSamples.ipynb` to Sampling using current QMCPy
        distribution, stochastic-process, and financial-option APIs; validate
        clean execution and saved outputs.
      - [x] Record a cross-deck notebook plan that keeps survey, sampling
        method, application, and performance narratives coherent while
        allowing topics and notebook calls to span multiple decks.
      - [x] Decide the Deck 02 notebook split: a compact Gaussian-mixture
        addition to `GeneratingSamples.ipynb` and one combined
        `TransportMapsAndAcceptanceRejection.ipynb` companion.
      - [x] Add and validate the compact Gaussian-mixture section in
        `GeneratingSamples.ipynb`.
      - [x] Draft and locally validate
        `TransportMapsAndAcceptanceRejection.ipynb` from the Deck 02 transport
        sequence and a narrowed migration of the inherited
        acceptance--rejection notebook.
      - [x] Complete instructor review of the combined transport/acceptance--rejection
        notebook and add its Colab badge and Deck 02 links.
      - [ ] Validate the combined notebook in clean Colab and add its
        course notebook-page link.
      - [x] Confirm successful Colab execution of `AreWeThereYet.ipynb` and
        `GeneratingSamples.ipynb` (reported by the instructor).
    - [ ] Add notebook links only after each target exists and passes
      validation.
      - [x] Link the validated `AreWeThereYet.ipynb` from the Applications
        section.
      - [x] Link the validated `GeneratingSamples.ipynb` from the Sampling
        section and Deck 02.
    - [x] Validate Quarto rendering and generated page structure.
    - [ ] Inspect the visible page layout in a browser.
  - [ ] Assignments (`pages/homework.qmd`)
    - [x] Create the initial Fall 2026 assignments-page structure.
    - [x] Create the `assignments/` source directory and an Assignment 1
      Quarto template based on the architecture and course-material
      references.
    - [x] Record the currently established assignment ground rules.
    - [x] Leave assignment details and due dates pending rather than inventing
      them.
    - [x] Finalize Assignment 1 as Owen Exercises 1.2 and 2.1, due September
      2; publish it in Canvas with its assignment-specific pair group set and
      website-only linked description; add the deadline to the assignments
      page, Schedule, and Lecture 1; and post the Canvas announcement.
    - [ ] Add assignment entries and due dates as they are finalized.
    - [x] Validate Quarto rendering and generated page structure.
    - [ ] Inspect the visible page layout in a browser.
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
  - [ ] Project
    - [x] Configure the Project navbar entry as a dropdown.
    - [x] Add Topic Selection & Presentation Scheduling linking to
      `pages/project.qmd`.
    - [x] Add Project Assessment linking to
      `pages/project-assessment.qmd`.
    - [x] Use the MATH 563 project page as the structural reference.
    - [x] Carry forward relevant MATH 565 Fall 2025 project content.
    - [x] Replace unavailable Fall 2026 links and scheduling resources with
      TBA.
    - [x] Separate topic-selection and presentation-scheduling guidance from
      assessment criteria.
    - [x] Validate Quarto rendering and generated page structure.
    - [x] Verify both Project dropdown links in the generated navigation.
    - [ ] Finalize Fall 2026 links, dates, deadlines, scheduling tools, and
      presentation logistics.
    - [ ] Inspect the visible page layout and dropdown behavior in a browser.
  - [ ] Policies (`classlib/classlib/quarto/pages/policies.qmd`)
    - [ ] Verify that institutional offices, personnel, contact details, and
      policy links are current for Fall 2026.
  - [ ] Accessing repo
    (`classlib/classlib/quarto/pages/git-clone-update-with-submodules.qmd`)
    - [x] Confirm that generic `REPO_URL` and `MATHXXXSpring20YY` placeholders
      are intentional because this is a reusable `classlib` page.
  - [x] Interesting articles & links
    (`classlib/classlib/quarto/pages/interesting-articles-links.qmd`)
  - [x] IMS Student Membership
  - [x] SIAM Student Membership
  - [x] MATH 476 — Statistics
  - [x] MATH 563 — Mathematical Statistics
  - [x] QMCPy
- [x] Create the initial project-assessment page
  (`pages/project-assessment.qmd`).
- [x] Configure course-page metadata.
- [x] Confirm that shared website styling and resources are sourced from
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
- [x] Validate shared tree asset paths in the staged output and published
  GitHub Pages slides.
- [ ] Confirm that the published site matches local validated output.

## 5. Slide framework

- [x] Create an independent RevealJS Quarto project under `slides/`.
- [x] Add slide-project configuration and metadata.
- [x] Add the initial numbered slide source and metadata entry.
- [x] Register the five Fall 2026 decks using the Fall 2025 lecture titles.
- [x] Add placeholder Quarto sources for decks awaiting conversion.
- [x] Connect previous/next deck navigation across all five decks.
- [x] Establish the Course Map and per-section outline conventions.
- [x] Load course-wide slide styling consistently across every deck.
- [x] Validate shared slide styling, metadata, navigation, and assets from
  `classlib`.
- [x] Add reusable Monte Carlo overview-tree rendering and named course tree
  marker presets.
- [x] Document the GitHub Pages asset-path convention for shared tree images.
- [x] Confirm that rendered slides are linked correctly from the website.

## 6. Prototype lecture conversion

- [x] Select the introductory lecture from the course-material reference as
  the prototype.
- [x] Convert the introductory lecture to a maintainable Quarto RevealJS
  source deck.
- [x] Migrate its mathematical notation, examples, and pedagogical sequence
  to native Markdown, LaTeX, tables, and RevealJS fragments.
- [x] Verify the website link, slide navigation, and Quarto rendering.
- [x] Inspect the rendered lecture slide by slide and compare it with the
  Fall 2025 PDF.
- [x] Establish prototype conventions: numbered course-specific sources,
  metadata-driven deck titles and navigation, native Markdown and LaTeX,
  native tables and layouts, and RevealJS fragments for staged builds.
- [x] Link the companion `AreWeThereYet` notebook after it has been migrated
  and validated.
- [x] Link the companion `GeneratingSamples` notebook after it has been
  migrated and validated.
- [x] Reassess possible reusable `classlib` improvements after Lecture 2;
  promote precomputed-replication median/IQR bands and optional fitted log--log
  trends to `cl.nbviz.plot_replication_band`.
- [x] Confirm that the prototype requires no change to the documented author
  workflow.

## 7. Remaining course-content migration

- [ ] Inventory remaining lectures, assignments, policies, schedules,
  assessments, and supporting resources in the course-material reference.
- [x] Convert remaining lecture decks in coherent teaching units.
  - [x] Draft Lecture 02, Generating Samples, from the Fall 2025 Keynote deck.
  - [x] Complete instructor review of Lecture 02 and refine its scope,
    narrative, and mathematical presentation.
  - [ ] Extend Lecture 02 with additional instructor-directed examples and
    transformation context.
    - [x] Add a one-dimensional Gaussian mixture example with analytic PDF and
      CDF formulas, hierarchical sampling, and a density plot.
    - [x] Add CDF and quantile plots for the zero-inflated exponential.
    - [x] Compare Cholesky and PCA factorizations for one covariance matrix and
      explain the importance of coordinate ordering for low discrepancy
      sampling.
    - [x] Add lookback and barrier option-payoff examples.
    - [x] Separate general geometric Brownian motion from risk-neutral discrete
      asset paths and add American-put optimal stopping.
    - [x] Distinguish geometric-Brownian-motion mean and median growth through
      a student exercise and paired-shock explanation.
    - [x] Add separate Asian and lookback call subsections to the
      `GeneratingSamples` survey notebook and link it from the quantile
      transform material as well as the closing summary.
    - [x] Recast transport maps and acceptance--rejection as two advanced
      direct-sampling methods, add a reusable $\operatorname{Beta}(2,1)$
      scalar example and a triangular-flow transport example, and connect
      exact transport to acceptance--rejection and importance sampling
      through the common target/proposal pair and correction weight. Use
      densities denoted by $\varrho_{\mathrm{tar}}$ and
      $\varrho_{\mathrm{prop}}$ across Decks 02--04, and retain the 2025
      acceptance-indicator and Bayes' theorem explanation for an unnormalized
      target.
    - [ ] Complete instructor review of the revised transport-map sequence and
      its companion notebook treatment.
  - [x] Draft Lecture 03, Markov Chain Monte Carlo, from the Fall 2025
    Keynote deck, including its discrepancy, Bayesian, and queueing material.
  - [x] Draft Lecture 04, Improving Efficiency, from the Fall 2025 Keynote
    deck, including executable comparisons of sampling designs.
  - [x] Draft Lecture 05, Selected Topics, from the Fall 2025 Keynote deck,
    including parallel computation, stochastic gradient descent, and
    multilevel Monte Carlo.
  - [ ] Review Lectures 03–05 individually with the instructor and refine
    their scope, narrative, examples, and visible layout.
  - [ ] Include Markov chain tree search (MCTS) in Deck 05, Selected Topics.
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
- [ ] Announce the course website on Canvas.
