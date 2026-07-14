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

Do not edit shared styling locally; make those changes in HickernellClassLib.

## Fresh clone

```bash
git submodule update --init --recursive
python -m pip install -e classlib
python -m pip install -e "qmcsoftware/.[class]"
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
