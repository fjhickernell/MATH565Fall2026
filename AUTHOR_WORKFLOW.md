# MATH 565 Quarto Website — Author Workflow

The `main` branch contains source files only. Rendered output is published to
the root of the `gh-pages` branch by GitHub Actions.

## Repository structure

- `index.qmd` — landing page
- `pages/*.qmd` — course pages
- `slides/*.qmd` — RevealJS slide decks
- `assets/` — course assets
- `classlib/` — shared styling, metadata, snippets, and notebooks (submodule)
- `qmcpy/` — QMCPy source and course dependencies (submodule)

Make genuinely reusable shared-style or presentation-infrastructure changes in
the `classlib` submodule. Validate, commit, and push those changes to
HickernellAcademicLib first, then intentionally update the course repository's
`classlib` pointer. Keep course-specific content and styling in this
repository, and do not leave course-only modifications in `classlib`.

## Adding or updating an assignment

Use this workflow whenever the instructor asks to create, set up, or materially
revise an assignment, including a minimal “here is an assignment” request. A
minimal request normally needs only the assignment number, assigned content,
and due date. Unless the instructor says otherwise, ordinary MATH 565
assignments use these standing defaults:

- `Assignment N` as the Canvas assignment title;
- 20 points, due at 11:59 PM America/Chicago on the stated date;
- individual work or one partner, using 20 assignment-specific self-sign-up
  groups limited to two students;
- one shared group grade from one group submission using Canvas's file-upload
  submission type, with unlimited attempts; and
- a Canvas description that links to the authoritative course-hosted assignment
  page and the course Assignments page, followed by an all-sections Canvas
  announcement after publication.

At intake, give the instructor one compact checklist covering the assignment
page, Assignments table, Schedule, deck reminder, rendering and deployment,
Canvas groups and assignment, announcement, and final verification. Identify
the details supplied by the instructor, the standing defaults being applied,
and only the unresolved decisions that would materially change the result. Do
not pause for a value covered by these defaults or one that can be established
from authoritative course sources. Never invent the assigned content or the due
date.

Complete every safe, reversible, and local step before asking for input. The
workflow has two publication gates:

1. After local validation, request the exact `Checkpoint` command if the
   instructor has not already issued it. The public website must be deployed
   and verified before Canvas publication.
2. After the public links are live and the Canvas changes are completely
   prepared, present one combined summary of the group set, assignment, and
   announcement and request one final Canvas publication confirmation. Once
   confirmed, finish those Canvas actions in order without another pause unless
   Canvas exposes a material conflict or unexpected setting.

After Canvas publication and verification, update the tracked handoff and
status files and request one closeout `Checkpoint` if those completion updates
are uncommitted. This preserves the finished external state and is not another
Canvas confirmation.

Then carry out the following steps:

1. Audit the repository and Canvas for an existing assignment page, assignment
   item, group set, or announcement. Resume and verify valid existing work
   rather than creating duplicates. Confirm any nonstandard content, coverage,
   date, points, submission requirements, or Canvas settings.
2. Create only an unpublished Canvas draft at this stage when one does not
   already exist, and record every Canvas assignment URL as
   `canvas.assignment_N` in `course-metadata.yml`. The saved URL supports site
   links, later verification, and duplicate prevention even when no current
   page consumes the metadata key. Do not publish the Canvas assignment or
   announce it while its course-website links are unavailable.
3. Create or update `assignments/assignment_N.qmd` when the assignment needs a
   course-hosted detail page. State the due date, assignment, and submission
   requirements, and link back to the ground rules in `pages/homework.qmd`.
4. Add or update the assignment in the table in `pages/homework.qmd`, with its
   descriptive title, coverage, and due date. Link to the course-hosted detail
   page when one exists; otherwise link directly to Canvas.
5. Add or update the due-date entry in `pages/schedule.qmd`, linking to the
   same authoritative assignment details.
6. Determine from the assignment coverage which RevealJS deck contains the
   relevant notes. Put the assignment name and due date on exactly one deck's
   title slide. If the appropriate deck is ambiguous, choose one suitable deck
   rather than duplicating the reminder. When useful, add a brief linked
   logistics slide describing the assignment and group-submission
   expectations. Because `slides/` is an independent Quarto project, link from
   a deck to a root-site assignment page using its published `.html` path
   rather than its `.qmd` source path. Retain past assignment reminders on their
   original decks as a chronological record; do not remove or replace them
   merely because their due dates have passed.
7. Render the root website and the independent slide project, assemble the
   complete site, and verify the assignment page, assignments table, schedule,
   Canvas links, deck notice, and internal links. Inspect the visible assignment
   page and affected deck at the standard RevealJS viewport. After the
   instructor issues the exact `Checkpoint` command, checkpoint and push the
   website changes, then verify that the public assignment and Assignments-page
   URLs are live. This publication check is a hard gate before publishing the
   Canvas assignment.
8. Finish the Canvas configuration only after the website is live. Unless the
   assignment explicitly requires individual work, first create or verify a
   separate self-sign-up group set named `Assignment N Groups` with 20 groups
   limited to two students, so students may choose a new partner each time.
   Configure the unpublished assignment against that group set so one
   submission and grade are shared by both group members. Keep the
   assignment-specific details authoritative on the course-hosted detail page;
   the Canvas description should link only to that page and to the course
   Assignments page rather than repeat instructions that could later diverge.
   Publish and verify the assignment, then post and verify an all-sections
   Canvas announcement linking to the live course pages and providing only the
   operational group and submission information students need. Do not repeat
   the assignment content or due date in the announcement.
9. Re-open the published Canvas assignment and announcement and verify their
   titles, points, due date and time, file-upload submission type, unlimited
   attempts, publication status, and all-sections audience. Verify that the
   assignment uses its 20-group self-sign-up set with a two-student limit and a
   shared group grade; that its description contains both intended course-page
   links and no duplicated assignment details; and that the announcement links
   to the live pages without repeating the assignment content or due date.
   Update the appropriate project handoff and status files so a later session
   does not repeat completed work. If the workflow is interrupted, preserve any
   draft, report the last verified step, and resume by auditing current
   repository and Canvas state rather than relying on conversational memory.
   Request the exact `Checkpoint` command to publish any post-Canvas completion
   updates still uncommitted in the repository.

## Preparing assignment grading materials

When asked to prepare an assignment for grading, inspect the previous
assignment's private OneDrive grading folder and use its workbook and folder
organization as the reference. Keep all submissions, student identities,
scores, and feedback outside the public course repository.

1. Verify the current assignment and its SpeedGrader roster. Reconcile groups
   afresh for each assignment; do not carry forward a previous assignment's
   partner mapping. Keep non-submission rows visible and exclude Test Student.
2. Use Canvas's normal **Download Submissions** action to obtain the bulk ZIP
   and save it in the private `Homework/Assignment N` folder. If automated
   downloading fails, distinguish that failure from a restriction on the
   instructor's access. An automated browser error, even one displaying an
   organization-policy message, does not establish that manual downloading
   will fail or that IT assistance is required. For Assignment 2, the normal
   manual Canvas download succeeded after automated attempts failed.
3. When a manual download is needed, clearly say that the instructor's action
   is required and give the steps immediately: open the assignment, left-click
   **Download Submissions**, wait for Canvas to prepare the ZIP, and save it
   in the private assignment folder or Downloads. Do not substitute **Save
   Link As** for the normal Canvas flow. Do not bypass security controls. If
   the manual flow also fails, report that specific result and seek an
   institution-approved resolution.
4. Once the ZIP is saved, resume autonomously: verify archive integrity,
   preserve the original, record its checksum, organize files by submitter,
   safely extract nested archives, and reconcile attachment IDs against
   Canvas. Do not execute uninspected student code.
5. Prepare or update the Excel tracker with local folder paths, separate
   exercise scores, totals that remain blank until all required scores are
   entered, feedback, and a separate general-comments tab. Preserve existing
   instructor edits. Flag apparent missing deliverables for review without
   assigning automatic deductions. Save a private grading guide and handoff
   describing the verified state and any remaining work.

## Loading grades, instructor review, and release

1. Use the instructor's saved `.xlsx` grading workbook when available, rather
   than an older CSV. Select the grading sheet by name, not the active tab.
   Match the total and feedback columns by their headers, confirm the points
   scale, and match each row to its Canvas student or group. Preserve the
   instructor's scores and feedback; leave blank feedback blank. Keep private
   grading files outside the public course repository.
2. **Before entering any score**, inspect the assignment's grade-posting policy
   and set it to manual posting if necessary. Verify the setting so the uploaded
   grades remain hidden for instructor review. Check feedback visibility too;
   if comments cannot remain hidden, retain them locally until release is
   approved. If Canvas cannot support a private upload, explain the limitation
   before entering data. Do not rely on hiding grades after automatic posting
   has already exposed them.
3. Load and verify all intended grades and eligible hidden feedback. Check group
   propagation and exclude Test Student. Verify saved comments in the Gradebook
   submission tray before retrying: for individuals on a group assignment,
   SpeedGrader and submission details may omit comments that were actually
   saved. Avoid duplicate comments.
4. Open the Grades page for the instructor to scan. After loading, draft an
   announcement stating that the grades are posted and incorporating the
   workbook's separate general-comments tab. Preserve its meaning, with light
   editing for clarity. Keep this draft local or otherwise unpublished; do not
   schedule an automatic release. Present the completed upload and announcement
   for review and wait for explicit publication approval.
5. After approval, post grades, release any held feedback, and verify student
   visibility before publishing an approved grades-posted announcement. A request
   to draft the announcement alone does not authorize sending it. Record the
   verified outcome in the private grading handoff without putting student data
   into the public repository.

## Adding or updating a test or examination

Use the following workflow whenever a test or final-examination detail is
finalized or materially revised:

1. Confirm the assessment name, date, duration, coverage, room, current PDF,
   and Canvas status. Leave unresolved details explicitly marked TBA.
2. Maintain `pages/tests.qmd` as the authoritative location for the assessment
   schedule, coverage, and course-wide testing rules.
3. Add the assessment to `pages/schedule.qmd`. Put only its name in the class
   event column. In the materials column, link to every covered deck by its
   full title, placing each link on its own line with `<br>`. The Tests page is
   available through the site navigation and should not be linked redundantly
   from an assessment's schedule row.
4. Add the assessment name and date to the title slide of the latest deck
   included in its coverage. Do not put the coverage or duration on the title
   slide, and remove or replace stale notices as the course advances.
5. Render the root website and independent slide project, assemble the complete
   site, and verify the Tests page, schedule links, assessment notice, internal
   navigation, and affected deck at the standard RevealJS viewport.

## Propagating classlib changes

Develop and review a reusable change in the course repository's `classlib`
working tree. Leave both the classlib change and the course submodule pointer
uncommitted until issuing `Checkpoint`.

During the checkpoint, use this sequence:

1. Validate, commit, and push the classlib change to HickernellAcademicLib.
2. Restore the course repository's recorded classlib checkout with
   `git submodule update --checkout classlib`.
3. Run `arrive` to synchronize standalone development repositories and
   fast-forward active repositories while retaining their recorded submodule
   pins.
4. Check out the newly published classlib commit in the course submodule and
   run the complete course validation, including the root website render, the
   independent slide render, and the assembled-site check.
5. Run `depart` to promote the published classlib commit, commit the resulting
   course submodule pointer, and push the course repository.
6. Confirm that HickernellAcademicLib and the course repository are clean and
   synchronized with their upstreams and that protected submodules remain
   clean.

This ordering ensures that the course never publishes a pointer to a classlib
commit that is unavailable upstream. Review the complete pointer diff before
`depart`; do not propagate unrelated or unauthorized dependency updates.

## Prerequisites

Install:

- Git
- Quarto
- Conda for the standard `qmcpy` Python environment and Jupyter kernel
- R with `knitr`, `rmarkdown`, and `reticulate`

Install the required R packages when they are not already available:

```r
install.packages(c("knitr", "rmarkdown", "reticulate"))
```

## Fresh clone and Python environment

If the `qmcpy` environment does not already exist, create it once with Python
3.11 or later:

```bash
conda create --name qmcpy "python>=3.11"
```

Then install the course dependencies and register that environment as the
`qmcpy` kernel:

```bash
git clone --recurse-submodules https://github.com/fjhickernell/MATH565Fall2026.git
cd MATH565Fall2026
git submodule update --init --recursive
conda activate qmcpy
python -m pip install -e classlib
python -m pip install -e "qmcpy/.[class]"
python -m ipykernel install --user --name qmcpy --display-name "qmcpy"
```

Copy `.Renviron.example` to `.Renviron` and adjust the Python path when the
local `qmcpy` environment is not in the default location.

## Course-wide simulation notation

Use the following default data flow in new or substantially revised course
notebooks, slides, and related explanations:

\[
\boldsymbol U \sim \operatorname{Unif}([0,1]^d), \qquad
\boldsymbol X = T(\boldsymbol U), \qquad
Y = f(\boldsymbol X).
\]

- Write the uniform and normal distribution names as `\operatorname{Unif}`
  and `\operatorname{Norm}` in notebooks, matching the slides' `\Unif` and
  `\Norm` macros. Do not use calligraphic U or N for these distributions.
- Use \(n\) for sample size consistently in explanations, code, and plot
  labels. Give distribution parameters such as a binomial trial count
  distinct descriptive names when needed to avoid a collision.
- Use the vector `\vU` in course source for the underlying uniform random
  input, whether its points are IID or low discrepancy. In a one-dimensional
  example, a scalar \(U\) is acceptable when the dimension matters
  pedagogically.
- Use `\vX` for the sample obtained after a quantile transformation, transport
  map, stochastic-process construction, or other transformation of the
  uniform input. State the transformation \(T\) when students first need it.
- Use \(Y=f(\boldsymbol X)\) for the output of an integrand, option payoff,
  simulator, or other potentially complicated black box. Use
  \(\boldsymbol Y=f(\boldsymbol X)\) only when the output is genuinely
  vector-valued.
- When an example naturally introduces a nonuniform proposal or intermediate
  variable, use \(\boldsymbol Z=S(\boldsymbol U)\) and then
  \(\boldsymbol X=T(\boldsymbol Z)\). Do not call a nonuniform proposal
  \(\boldsymbol U\). Define any example-specific exception explicitly and
  return to the default notation when the distinction is no longer needed.

Keep this notation consistent across the mathematical explanation, Python
variables, plots, captions, and links between decks and notebooks. Apply it
prospectively as materials are created or substantially revised; do not make a
mechanical notation-only rewrite of otherwise untouched material.

## Variable accents in notebooks and slides

Use `\widehat{...}` for hats and `\overline{...}` for bars over variables,
rather than narrow `\hat` or `\bar` accents. The existing shared bar macros
already use `\overline`; retain them when their meaning matches. Keep sample
indices outside the accent unless the entire indexed expression is averaged.
Before editing a notebook, name it to the instructor so an open copy can be
reloaded afterward. Preserve existing edits and saved outputs when changing
only Markdown notation.

## Deck 03 notebook dependencies

`QueueSimulation.ipynb` uses SimPy 4.1.2 in addition to the standard course
runtime. Install it locally with `python -m pip install "simpy==4.1.2"` in the
`qmcpy` environment; the notebook's Colab setup installs the same version.
Publish `notebooks/queue_examples.py` with the notebook. Validate its process
and accounting code with
`python -m unittest discover -s tests -p 'test_queue_examples.py'`.

`BayesianMCMC.ipynb` uses the course's transparent Metropolis and tempering
implementations with ArviZ diagnostics. The PyMC quickstart is an optional
external supplement, not a required package or unfinished prerequisite for
Deck 03. A course-owned PyMC/NUTS extension requires a distinct teaching purpose.

## Notebook execution timing

Every course notebook must set
`NOTEBOOK_START_TIME = time.perf_counter()` in its initial setup cell, before
Colab detection and setup, and keep a final code cell with the ID
`notebook-runtime` that reports `Total execution time for this notebook is …
min … sec.` The runtime cell must remain the notebook's last cell. Validate the
complete run and its timing output with the `qmcpy` kernel before publication;
separate clean-Colab execution is not a publication prerequisite. The instructor
accepts the established Colab setup based on successful use across many
notebooks; investigate and fix Colab problems when they arise. Keep local
execution validation and record instructor content review separately from
publication.

## Preview and render

Preview the website with:

```bash
quarto preview
```

Build the complete local output with:

```bash
quarto render
(cd slides && quarto render)
rm -rf _site/slides
mkdir -p _site/slides
rsync -a --delete slides/_site/ _site/slides/
```

The GitHub Actions workflow performs these steps and publishes the result on
every push to `main`. Do not commit `_site/` or other rendered output.
