# `notebooks/` — Research & Exploration

Jupyter / marimo / Quarto notebooks, exploratory analyses, paper drafts, and one-off investigations. The **lab journal** of Human Engineering.

**[← Back to project README](../README.md)**

---

## What lives here

Anything **exploratory, in-progress, or unfinished**. Notebooks are where ideas are tested before they graduate into:

- a polished atlas entry (`atlases/`)
- a productionized project (`comp-prog-proj/`)
- a permanent dataset (`data/`)
- a paper or formal write-up

Notebooks can be messy. They have a different bar than atlases or production code.

---

## Naming

Two patterns are acceptable:

### Pattern A — Dated single-file (for short investigations)
```
notebooks/
└── 2026-06-04-spike-binding-affinity-comparison.ipynb
```

### Pattern B — Topic folder (for multi-file investigations)
```
notebooks/
└── 2026-06-spike-binding/
    ├── README.md                  # what we're investigating, status, conclusion
    ├── 01-data-prep.ipynb
    ├── 02-binding-affinity.ipynb
    ├── 03-mutation-scan.ipynb
    └── figures/                   # OPTIONAL — local outputs (or move to /media/)
```

**Use Pattern B as soon as a single notebook would exceed 3–4 sections** or you have intermediate outputs to keep alongside.

**Date prefix:** `YYYY-MM-DD-` for files; `YYYY-MM-` for folders. Keeps chronological ordering visible in the file listing.

---

## When a notebook is "done"

Notebooks reach one of three end states:

| End state | What to do |
|:---|:---|
| **Promoted** — findings are solid enough to publish | Distill into an atlas entry, productionize the code into `comp-prog-proj/`, persist any dataset into `data/`. Leave the notebook for provenance; add a `README.md` linking forward. |
| **Archived** — useful but inactive | Add a one-line status note at the top of the notebook (`> **Status:** Archived 2026-06-04 — superseded by [link]`). Keep the file. |
| **Discarded** — wrong path, no future value | `git rm` and write a one-line `notebooks/_dead-ends.md` entry noting what was tried and why it didn't work (so nobody repeats it). |

The default end state is **archived** — almost no notebook is truly worthless; most teach something even when wrong.

---

## Tech conventions

- **Format:** `.ipynb` is the lingua franca; `.qmd` (Quarto), `.py` (marimo / percent-format), `.jl` (Julia / Pluto) are all welcome.
- **Reproducibility:** at the top of each notebook, declare the kernel / Python version / required packages (or commit a `requirements.txt` / `environment.yml` next to it).
- **Output cells:** commit them. They're part of the research record. For very large outputs, strip with `nbstripout` and link to the data instead.
- **Large outputs:** if a notebook produces a figure / dataset that should outlive the notebook, move it to `media/` or `data/` and link from the notebook.

---

## How notebooks cite atlases & data

```python
# In a markdown cell at the top:

# ## Investigation: Spike-ACE2 binding affinity across variants
# - Atlas entry: ../atlases/02-pathogen/01-viruses/sars-cov-2.md
# - Data: ../data/sars-cov-2-genomes/
# - Schema: ../schemas/binding-affinity.schema.md
```

---

## What does NOT go here

- Production-grade code → `comp-prog-proj/`
- Polished knowledge writeups → `atlases/`
- Persistent datasets → `data/`
- Final figures for publication → `media/`

---

**[← Back to project README](../README.md)**
