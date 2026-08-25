# MATH 565 — Fall 2026

This repository contains the Quarto website source for **MATH 565: Monte
Carlo and Quasi-Monte Carlo Methods** at Illinois Institute of Technology.

Course content is being added incrementally. The website and slide framework
are established, and the introductory lecture is the completed prototype for
the remaining course conversion. MATH563Spring2026 provides the read-only
architecture reference, while MATH565Fall2025 provides the read-only
course-material reference.

**Course website:** https://fjhickernell.github.io/MATH565Fall2026/

## Local setup

See [`AUTHOR_WORKFLOW.md`](AUTHOR_WORKFLOW.md) for the complete author setup,
preview, rendering, and publishing workflow. The course uses the standard
`qmcpy` Python environment and Jupyter kernel. If the environment does not
already exist, create it once with Python 3.11 or later:

```bash
conda create --name qmcpy "python>=3.11"
```

Then perform the initial course setup:

```bash
git clone --recurse-submodules https://github.com/fjhickernell/MATH565Fall2026.git
cd MATH565Fall2026
conda activate qmcpy
python -m pip install -e classlib
python -m pip install -e "qmcpy/.[class]"
python -m ipykernel install --user --name qmcpy --display-name "qmcpy"
```

The deployment workflow renders the website and slides separately, stages the
slides under `_site/slides`, and publishes the combined site to `gh-pages`.
