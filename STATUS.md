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
- [x] Document the minimal-input assignment workflow, standing Canvas defaults,
  consolidated publication confirmation, and end-to-end verification steps.
- [x] Document the private assignment-grading preparation workflow, including
  Canvas download fallback, submission reconciliation, and tracker setup.
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
    - [x] Add a public-safe Math Tutoring Center notice that routes enrolled
      students through Canvas to the live coordinator-maintained schedule.
    - [x] Review textbook and recommended resources.
    - [x] Review prerequisites and requirements.
    - [x] Review course objectives and outline.
    - [x] Reconcile the outline with coverage through October 6 and projected
      remaining units, totaling about 40 lecture hours; condense subtopics and
      use Improving Efficiency consistently (October 8, 2026).
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
  - [x] Schedule (`pages/schedule.qmd`)
    - [x] Create the Fall 2026 Tuesday/Thursday meeting calendar.
    - [x] Verify the August 18 start date and December 3 final regular
      meeting.
    - [x] Mark Thanksgiving Day, November 26, as no class.
    - [x] Record the classroom as PH 109 (room change September 10, 2026).
    - [x] Add a TBA final-exam entry for the following week.
    - [x] Reserve Assignment 4, 5, and 6 due dates on October 7,
      October 21, and November 13 with details pending.
    - [x] Leave unknown topics, materials, and additional dates blank.
    - [x] Audit all nine instructional Panopto recordings from August 18
      through September 17; reconcile actual coverage and covered-deck links,
      preserving assessment and deadline entries.
    - [x] Record the historical audit and September 22 continuation in
      `notes/LECTURE-UPDATES.md`; the next calendar occurrence is annotated.
    - [x] Include the historical schedule audit in the September 17 Checkpoint
      and verify the resulting remote deployment.
    - [x] Validate Quarto rendering and generated page structure.
    - [x] Inspect every monthly table at desktop and phone widths; correct
      cramped Week/Date columns and phone wrapping.
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
      - [x] Migrate the Deck 04 Keister and conditional Monte Carlo notebooks,
        and create the Asian option variance-reduction companion with a
        discretely monitored lookback call; execute all three in clean local
        `qmcpy` kernels and review their saved figures (September 28, 2026).
      - [x] Use QMCPy IID/Sobol' sampling and Gaussian/Brownian transformations
        in the three Deck 04 companions; use FinancialOption for the lookback
        payoff and European reference price. Preserve the Asian-call model,
        execute all three with pinned dependencies, check native-integrand
        agreement, and inspect all four figures (October 1, 2026).
      - [x] Build and link the Deck 04 low discrepancy constructions companion:
        early-point generator recovery, randomization, projections, and a fixed
        Keister comparison; clean `qmcpy` execution and five figures checked
        (October 5, 2026).
      - [x] Audit the efficiency companions: expand lookback to the eight-method
        Asian comparison, add equal-cost IID antithetic comparisons, charge
        independent control pilots and sample generation in timing tables,
        block Asian density calculations, and align empirical-distribution
        notation. All five affected notebooks execute cleanly with pinned
        dependencies; Asian Sobol', lattice, and Halton variants pass
        (October 8, 2026).
      - [x] Add a lattice/Sobol' chooser to Generating Samples and Asian Option
        Variance Reduction; compare low discrepancy sampling plain, with drift,
        with control, and with both. Both complete notebooks execute cleanly
        with each choice; changed figures checked (October 5, 2026).
      - [x] Default Asian Option Variance Reduction to Sobol' with lattice and
        Halton alternatives; preserve weekly d=52, n=2**14, and tolerance=0.05.
        All three choices execute cleanly and meet the tolerance; saved Sobol'
        figure checked (October 5, 2026).
      - [x] Compare CMC density estimates with histograms and KDE; add weekly
        arithmetic-Asian average and call-payoff distributions, including the
        zero-payoff atom. Clean execution, mathematical consistency checks,
        and four-figure review passed (October 5, 2026).
      - [x] Add histogram/KDE/CMC formulas and Asian-density conditioning,
        density, and payoff-atom math to Deck 04; align notebook formulas and
        update Deck 01 terms index. Both decks rendered and changed slides
        visually checked (October 5, 2026).
      - [ ] Complete instructor review of the constructions companion; replace
        its isolated Kronecker helper after the new QMCPy API is pulled in and
        intentionally pinned, then revalidate.
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
      - [x] Close the remaining Deck 02 companion-notebook task, including
        GeneratingSamples mixture and IID/Sobol' review (September 10, 2026).
        The proposed separate financial-payoff notebook was not created; it
        is no longer an outstanding requirement for this task.
      - [x] Complete instructor review of the combined transport/acceptance--rejection
        notebook and add its Colab badge and Deck 02 links.
      - [x] Use pinned QMCPy-native acceptance--rejection for both targets;
        validate all ten code cells locally and inspect all six saved plots.
      - [x] Add the combined notebook’s course notebook-page link; the instructor
        waived separate clean-Colab validation as a publication prerequisite.
      - [x] Confirm successful Colab execution of `AreWeThereYet.ipynb` and
        `GeneratingSamples.ipynb` (reported by the instructor).
      - [x] Migrate the complete non-queueing 2025 MCMC material into
        `MetropolisHastings.ipynb`, `BayesianMCMC.ipynb`, and `Discrepancy.ipynb`.
        Include the existing acceptance--rejection comparison, separated-mode
        trapping, parallel tempering, exact posterior benchmarks, and MMD.
        Validate all three in clean local `qmcpy` kernels and inspect saved figures.
      - [x] Link the three locally validated MCMC notebooks from their matching
        Metropolis--Hastings, discrepancy, and Bayesian sections in Deck 03.
      - [x] Highlight MH consecutive-repeat counts and their acceptance-rate
        complement; validate whole-run, retained-run, and tempering accounting.
      - [x] Clarify negative off-diagonal MMD estimates in Deck 03 and its
        companion notebook, with an exercise distinguishing IID and MCMC pairs.
      - [x] Add the three MCMC notebook-page links under the instructor’s
        policy accepting the established Colab setup without separate validation.
      - [x] Complete instructor content review of the three MCMC notebooks.
      - [x] Migrate `QueueSimulation.ipynb` using SimPy for single-server and
        drive-through blocking models, with finite-run accounting and benchmark
        comparisons; add its notebook-page and Deck 03 links.
      - [x] Add eight deterministic checks for queue paths, blocking, accounting,
        and stopping rules; validate all four Deck 03 companions in clean local
        kernels without warnings and inspect the queue notebook’s four figures.
      - [x] Complete instructor content review of the queueing companion.
      - [x] Add descriptive text and units to mathematical plot labels across
        the Bayesian, queueing, Metropolis--Hastings, discrepancy, and
        transport/rejection companions; execute and visually check all five.
      - [x] Record SimPy >=4.1.2 in course requirements and install the course
        requirements during local setup and CI.
    - [ ] Add notebook links only after each target exists and passes
      validation.
      - [x] Link the validated `AreWeThereYet.ipynb` from the Applications
        section.
      - [x] Link the validated `GeneratingSamples.ipynb` from the Sampling
        section and Deck 02.
    - [x] Validate Quarto rendering and generated page structure.
    - [ ] Inspect the visible page layout in a browser.
  - [ ] Assignments (`pages/homework.qmd`)
    - [x] Record the 20-point homework and lowest-score-drop policy, protect
      the 10-point Diagnostic Survey from dropping, and save unpublished
      Canvas placeholders for Assignments 5–6 (October 9, 2026).
    - [x] Prepare Assignment 4 as Owen Exercises 11.5 and 11.6, due October 7
      at 11:59 PM Chicago; save unpublished Canvas draft 105796 and its metadata.
    - [x] Deploy and verify the public Assignment 4 and Assignments pages
      after checkpoint `e9906ca` on September 30, 2026.
    - [x] Configure Assignment 4's 20 self-sign-up groups (limit two), shared
      submission/grade, and unlimited file uploads; publish assignment 105796
      and all-sections announcement 106931 after instructor approval on
      September 30, 2026; verify saved settings and publication.
    - [x] Create the initial Fall 2026 assignments-page structure.
    - [x] Create the `assignments/` source directory and an Assignment 1
      Quarto template based on the architecture and course-material
      references.
    - [x] Record the currently established assignment ground rules.
    - [x] Require every submitted filename to identify all group members and
      every file's contents to include each member's full name and A-number.
    - [x] Leave assignment details and due dates pending rather than inventing
      them.
    - [x] Finalize Assignment 1 as Owen Exercises 1.2 and 2.1, due September
      2; publish it in Canvas with its assignment-specific pair group set and
      website-only linked description; add the deadline to the assignments
      page, Schedule, and Lecture 1; and post the Canvas announcement.
    - [x] Finalize Assignment 2 as Owen Exercises 4.5 and 4.19, due September
      11, and add the deadline to its detail page, the assignments page,
      Schedule, and Lecture 2.
    - [x] Publish Assignment 2 in Canvas for 20 points with its
      assignment-specific pair group set and a description linking only the
      assignment detail page and Assignments page, then post its Canvas
      announcement after the course website changes are live.
    - [x] Prepare Assignment 3 locally as Owen Exercises 5.4 and 5.13, due
      September 25; save unpublished Canvas draft 104697 for 20 points and
      unlimited file uploads.
    - [x] Commit and push Assignment 3 website sources (`fcbb207`).
    - [x] Verify the deployed Assignment 3 links, configure its separate pair
      group set, and publish its Canvas assignment and announcement after
      instructor approval. Verified September 17; announcement 105901 posted
      to All Sections at 10:30 PM.
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
    - [x] Schedule Test 2 for October 27 in PH 109; set the published
      On Paper Canvas item for 11:15 AM; add the date to the course
      website sources; and post the all-sections announcement. Coverage
      remains TBD.
    - [x] State that final-examination dates will be posted when scheduled by
      the Registrar and that the cumulative examination will emphasize
      material not covered by Test 1 or Test 2.
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
    - [x] Finalize Fall 2026 links, dates, deadlines, scheduling tools, and
      presentation logistics.
      - [x] Set the November 23–24 presentation windows, four 20-minute
        breaks, and 30 bookable 20-minute slots; prepare an Excel
        sign-up workbook and a roster-based quota checker.
      - [x] Grant active students editing access to the schedule and view
        access to the approval sheet; finalize the room, sign-up deadlines,
        and immediate assessment hand-in procedure; publish the combined
        Canvas announcement.
      - [x] Deploy the updated project page and verify both restricted
        workbook links on the live site.
      - [x] Refresh the October 3 topic approvals, preserve resubmission
        history with `SUPERSEDED`, and verify student view permissions.
    - [ ] Inspect the visible page layout and dropdown behavior in a browser.
  - [ ] Policies (`classlib/classlib/quarto/pages/policies.qmd`)
    - [x] Add a detailed instructor statement describing how ChatGPT and Codex
      support course preparation, verification, and maintenance, and link to it
      from an abbreviated early slide in Deck 01.
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
- [x] Standardize all Course Maps at 36% course decks, 4% gutter, and 60%
  deck contents; add Teaser Trailer to Introduction and the sampling pipeline
  to Generating Samples beneath In this deck.
- [x] Add the vector uniform-input, conditional-proposal, and accept-or-stay
  theme to the MCMC Course Map, identifying the target law at stationarity.
- [x] Add larger whole-deck topic trees to Course Maps in Decks 02–05, with
  substantive topic selections, lower-left This deck links, and bold current
  deck emphasis; add themes to Decks 04–05 and validate layouts.
- [x] Audit Decks 02–03 navigation markers against taught content, including
  Error Assessment for the worst-case and GP error derivations.
- [x] Add cumulative closing slides to the developed decks: Big Ideas and
  What Comes Next throughout, How Far We Have Come from Deck 03 onward, and
  a gold-bordered Big Ideas continuation in Deck 02; keep only Big Ideas in
  each Course Map's closing links.
- [x] Connect Decks 02–03 closing summaries to developed applications, keeping
  Deck 03's methods and applications together on one cumulative recap slide.
- [x] Load course-wide slide styling consistently across every deck.
- [x] Link callbacks and forward references across all five decks and audit
  multidimensional vector notation, including Keister and discrepancy formulas.
- [x] Align Decks 02–04 and nine companions with uniform U, proposal/source Z,
  target X, scalar Y=f(X), bold vector-valued maps, and normalized/unnormalized
  density notation. Reframe Deck 04 around equal-mean f(X) and g(Z), distinguish
  exact transport from weighted changes of variables, and use h for cube
  integrands. Align discrepancy nodes, MCMC proposals, observed data, queue
  durations, and antithetic maps; preserve existing slide anchors. All three
  decks render successfully and all nine companions execute cleanly with qmcpy.
- [x] Add Deck 04 overlaid exact-transport/importance-sampling contribution
  plots for two functions, audit keyword highlighting, and add larger-index
  van der Corput exercises.
- [x] Complete the final nine-companion notation audit against Deck 04:
  identify exact transport and importance contributions, clarify correction
  weights and cube maps, align observed-data labels, lowercase variance and
  covariance, and repair the MCMC autocorrelation formula. Execute all nine
  companions with pinned dependencies and inspect their figures.
- [x] Demonstrate practical stopping in the Keister and Asian-option companions,
  including tolerance, estimate, reported interval or bound, sample count,
  pilot cost, budget exhaustion, and accuracy assumptions. Add the Deck 04
  continuation links and update the notebook page; validate execution and rendering.
- [x] Add four starred Deck 04 exercises in the sparsest sections: transport
  versus importance sampling, control variance and cost, conditional density,
  and stopping decisions. Include presenter-note answers, retain the three
  main control/conditioning headings, and check rendering and visible layouts
  (October 8, 2026).
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
    - [x] Complete instructor review of the revised transport-map sequence and
      its companion notebook treatment.
    - [x] Reframe mixture sampling and acceptance--rejection as unit-cube integrals
      over a $(d+1)$-dimensional uniform input after transporting the first
      $d$ coordinates to the proposal distribution; write out the mixture
      sample mean and the rejection ratio of sample means explicitly.
  - [x] Draft Lecture 03, Markov Chain Monte Carlo, from the Fall 2025
    Keynote deck, including its discrepancy, Bayesian, and queueing material.
  - [x] Add a gold-border applications comparison of direct finance sampling,
    Bayesian MCMC, and event-driven queue simulation, with a multilevel Monte
    Carlo preview and qualifications in speaker notes.
  - [x] Clarify the frequentist–Fisherian–Bayesian transition with the shared
    Efron–Hastie citation; distinguish general likelihood from the normal
    worked example and demote supporting Bayesian/queueing headings.
  - [x] Add four queue-notebook callouts emphasizing residual times, finite-run
    averages, blocking, and the distinction between capacity and service rate.
  - [x] Refine the Bayesian and queueing materials; distinguish full
    interarrival and service inputs from event-state residual clocks, align the
    simulation helper and companion, and add worked four-event queue practice.
  - [x] Compare ordinary kernel discrepancy, KL/relative entropy, and
    score-based Stein discrepancy, including normalizing constants and
    limitations; place alternatives after the integration-error development and cite the
    Hickernell–Kirk–Sorokin tutorial for the kernel/error development.
  - [x] Expand parallel-tempering swap explanations and normalize discrepancy;
    organize distribution, empirical, and unbiased formulas; make Stein's
    supremum and kernel formulas explicit with true-integral-minus-sum order.
  - [x] Audit all seven notebooks through MCMC against Owen's available
    chapters, update Decks 01–03 title readings, and record the detailed
    mapping in `notes/OWEN-COVERAGE-AUDIT.md`.
  - [x] Draft Lecture 04, Improving Efficiency, from the Fall 2025 Keynote
    deck, including executable comparisons of sampling designs.
  - [x] Draft Lecture 05, Selected Topics, from the Fall 2025 Keynote deck,
    including parallel computation, stochastic gradient descent, and
    multilevel Monte Carlo.
  - [x] Complete instructor review of Lecture 03 and its four companions
    (September 10, 2026).
  - [ ] Review Lectures 04–05 individually with the instructor and refine
    their scope, narrative, examples, and visible layout.
  - [ ] Include Monte Carlo tree search (MCTS) in Deck 05, Selected Topics.
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
