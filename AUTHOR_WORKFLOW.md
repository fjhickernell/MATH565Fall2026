# MATH 565 Quarto Website — Author Workflow

The `main` branch contains source files only. Rendered output is published to
the root of the `gh-pages` branch by GitHub Actions.

## Repository structure

- `index.qmd` — landing page
- `pages/*.qmd` — course pages
- `slides/*.qmd` — RevealJS slide decks
- `assets/` — course assets
- `classlib/` — shared styling, metadata, snippets, and notebooks (submodule)
- `qmcsoftware/` — QMCPy source and course dependencies (submodule)

Make genuinely reusable shared-style or presentation-infrastructure changes in
the `classlib` submodule. Validate, commit, and push those changes to
HickernellAcademicLib first, then intentionally update the course repository's
`classlib` pointer. Keep course-specific content and styling in this
repository, and do not leave course-only modifications in `classlib`.

## Adding or updating an assignment

Use the following workflow whenever an assignment is finalized or materially
revised:

1. Confirm the assignment content, coverage, due date and time, point value,
   submission requirements, and Canvas settings. Do not invent unresolved
   details.
2. If course sources need a stable Canvas assignment URL, create only an
   unpublished Canvas draft at this stage and record its URL as
   `canvas.assignment_N` in `course-metadata.yml`. Do not publish the Canvas
   assignment or announce it while its course-website links are unavailable.
3. Create or update `assignments/assignment_N.qmd` when the assignment needs a
   course-hosted detail page. State the due date, assignment, and submission
   requirements, and link back to the ground rules in `pages/homework.qmd`.
4. Add or update the assignment in the table in `pages/homework.qmd`, with its
   descriptive title, coverage, and due date. Link to the course-hosted detail
   page when one exists; otherwise link directly to Canvas.
5. Add or update the due-date entry in `pages/schedule.qmd`, linking to the
   same authoritative assignment details.
6. Determine from the schedule which RevealJS deck is current when the
   assignment is assigned. Add or update the due-date notice on that deck's
   title slide and, when useful, a brief linked logistics slide describing the
   assignment and group-submission expectations. Remove or replace stale
   notices as the course advances.
7. Render the root website and the independent slide project, assemble the
   complete site, and verify the assignment page, assignments table, schedule,
   Canvas links, deck notice, and internal links. Inspect the visible assignment
   page and affected deck at the standard RevealJS viewport. Checkpoint and
   push the website changes, then verify that the public assignment and
   Assignments-page URLs are live. This publication check is a hard gate before
   publishing the Canvas assignment.
8. Finish and publish the Canvas assignment only after the website is live.
   Unless the assignment explicitly requires individual work, create a
   separate self-sign-up group set named `Assignment N Groups` for that
   assignment so students may choose a new partner each time. Limit groups to
   pairs, and configure Canvas so that one submission is shared by both group
   members. Keep the assignment-specific details authoritative on the
   course-hosted detail page; the Canvas description should link to that page
   and to the course Assignments page rather than repeat instructions that
   could later diverge. Verify the published assignment, then announce it in
   Canvas by linking to the live course pages and providing only the operational
   group and submission information students need. Do not repeat the assignment
   content or due date in the announcement.

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
python -m pip install -e "qmcsoftware/.[class]"
python -m ipykernel install --user --name qmcpy --display-name "qmcpy"
```

Copy `.Renviron.example` to `.Renviron` and adjust the Python path when the
local `qmcpy` environment is not in the default location.

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
