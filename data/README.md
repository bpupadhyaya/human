# `data/` — Datasets

Structured, machine-readable data used by [atlases](../atlases/) for citation, by [comp-prog-proj](../comp-prog-proj/) for computation, and by [notebooks](../notebooks/) for analysis.

**[← Back to project README](../README.md)**

---

## What lives here

Datasets — small enough to commit, structured enough to be useful. One folder per dataset.

```
data/
└── <dataset-name>/
    ├── README.md       # what it is, source, license, schema, last updated
    ├── schema.md       # OR reference an entry in /schemas/
    ├── LICENSE.md      # IF different from the repo MIT license
    └── <files>         # .csv / .json / .parquet / .fasta / .pdb / pointers to external
```

---

## Naming

`kebab-case-noun/` — descriptive, dataset-focused. Examples:

- `sars-cov-2-genomes/`
- `human-protein-atlas-subset/`
- `drug-target-interactions/`
- `who-essential-medicines/`
- `pubchem-compounds-cardiovascular/`

---

## Required: `README.md` per dataset

Every dataset folder **must** carry a `README.md` answering:

```markdown
# <dataset-name>

## What it is
One paragraph.

## Source
URL, paper DOI, organization, dataset version.

## License
SPDX identifier (MIT / CC-BY-4.0 / CC0-1.0 / etc.). If proprietary or restricted — don't commit, link instead.

## Schema
Either inline OR pointer to /schemas/<name>.schema.md

## Update cadence
Snapshot date / version / how to refresh.

## Used by
- atlases/02-pathogen/01-viruses/sars-cov-2.md
- comp-prog-proj/sarscov2-classifier/
- notebooks/2026-06-spike-binding-analysis/
```

---

## File size: when to use git-lfs vs. external pointers

| Size | Strategy |
|:---|:---|
| < 1 MB | Commit directly |
| 1–10 MB | Commit, but think about it (does every clone need this?) |
| 10 MB – 1 GB | `git-lfs track "*.<ext>"` before committing |
| > 1 GB | External hosting (S3, Hugging Face datasets, Zenodo). Commit a `pointers.md` with URLs and SHA256 hashes |

**For large public datasets** that already live somewhere stable (NCBI, UniProt, PDB, etc.) → **don't mirror them**. Commit a `README.md` with the download URL, version, and any subset filter to apply.

---

## Provenance & reproducibility

For every non-trivial dataset:
- Record **how** it was generated (script, query, API call, raw download URL) in the README
- Record **when** it was generated / pulled (date, commit hash, source version)
- Where applicable, commit the script that produced it (in this folder, or referenced from `comp-prog-proj/` or `tools/`)

The goal: any contributor should be able to regenerate or refresh the dataset from scratch using only what is documented here.

---

## Licensing notes

- Data is **not** automatically covered by the repo MIT license — many datasets carry their own license (CC-BY, CDLA, CC0, restricted, etc.).
- For every third-party dataset: include `LICENSE.md` in the dataset folder with the SPDX identifier and any attribution requirements.
- If a dataset's license **forbids redistribution**, do NOT commit the files — commit only a `README.md` describing how to obtain it.

---

## How atlases & code reference data

From an atlas:

```markdown
<!-- atlases/02-pathogen/01-viruses/sars-cov-2.md -->

Sequence data: [`data/sars-cov-2-genomes/`](../../../data/sars-cov-2-genomes/README.md)
```

From a project:

```python
# comp-prog-proj/sarscov2-classifier/src/load.py
DATA_DIR = Path(__file__).parent.parent.parent.parent / "data" / "sars-cov-2-genomes"
```

(Or use an environment variable `HUMAN_REPO_ROOT` — convention TBD when needed.)

---

## What does NOT go here

- Rendered figures, charts, diagrams → `media/`
- HTML page assets → `docs/_assets/`
- Source code that processes data → `comp-prog-proj/`
- Exploratory analysis notebooks → `notebooks/`
- Schema definitions standalone → `schemas/` (this folder may reference them)

---

**[← Back to project README](../README.md)**
