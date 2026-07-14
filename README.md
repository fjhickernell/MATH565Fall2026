# MATH 565 — Fall 2026

This repository contains the Quarto website source for **MATH 565: Monte
Carlo and Quasi-Monte Carlo Methods** at Illinois Institute of Technology.

Course content will be added incrementally. The current repository is a clean
website skeleton based on the architecture of MATH563Spring2026.

**Course website:** https://fjhickernell.github.io/MATH565Fall2026/

## Local setup

```bash
git clone --recurse-submodules https://github.com/fjhickernell/MATH565Fall2026.git
cd MATH565Fall2026
python -m pip install -e classlib
python -m pip install -e "qmcsoftware/.[class]"
quarto render
(cd slides && quarto render)
```

The deployment workflow renders the website and slides separately, stages the
slides under `_site/slides`, and publishes the combined site to `gh-pages`.
