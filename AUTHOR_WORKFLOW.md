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
