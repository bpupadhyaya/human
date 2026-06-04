# Citation Schema

The structure every cited source must follow, anywhere in the project — atlas entries, datasets, notebooks, agents.

> **Machine-readable companion:** [`citation.schema.json`](citation.schema.json) — JSON Schema for validators.

**Consumers:**
- `atlases/*/**/README.md` (every atlas entry's `sources` array)
- `tools/scripts/validate-entries.py`
- `comp-prog-proj/*/` (any project that ingests atlas data)
- `notebooks/*/` (any notebook that asserts a fact)

---

## Why this exists

Every claim in the project must be traceable to a source — that is non-negotiable for *Rigorous* in the project Principles. A common citation format makes the source layer machine-checkable, dedupable across entries, and re-usable by AI agents that need provenance.

---

## Fields

| Field | Required | Type | Description |
|:---|:---:|:---|:---|
| `id` | ✅ | string (kebab-case) | Locally unique slug within the entry's `sources` array. Used by other fields to reference this source (e.g. `claim_source: openstax-anatomy-19-1`). |
| `type` | ✅ | enum | One of: `textbook`, `peer-reviewed`, `preprint`, `clinical-guideline`, `regulatory`, `database`, `consortium`, `oral-tradition`. See *Type guide* below. |
| `cite` | ✅ | string | Full human-readable citation. Author(s), title, venue, year. No formatting requirements beyond legibility. |
| `url` | ✅ required | URI | Canonical, stable URL. Prefer DOI redirector or publisher's permalink over a search-engine result. For entries with a DOI, `https://doi.org/{doi}` is the canonical URL and must be provided. |
| `doi` | optional | string | Bare DOI (e.g. `10.1038/s41586-022-04819-6`). No `https://doi.org/` prefix. |
| `pmid` | optional | string of digits | PubMed ID, if peer-reviewed and indexed. |
| `accessed` | ⚠️ for non-DOI sources | ISO date `YYYY-MM-DD` | When the source was last verified. Required if the source has no DOI/PMID (because URLs rot). |
| `note` | optional | string | Brief context — e.g., "Chapter 19, section 1" or "Figure 4 cited specifically". One line. |

---

## Type guide

| `type` | Use for | Example |
|:---|:---|:---|
| `textbook` | Open or closed textbooks | OpenStax, NIH Bookshelf, Robbins, Guyton & Hall |
| `peer-reviewed` | Journal articles past peer review | Nature, NEJM, JAMA, PLoS, eLife |
| `preprint` | Not yet peer-reviewed | bioRxiv, medRxiv, arXiv |
| `clinical-guideline` | Authoritative clinical practice docs | AHA/ACC, ESC, WHO, NICE, IDSA |
| `regulatory` | Drug labels, package inserts, agency docs | FDA label, EMA SmPC, WHO Essential Medicines List |
| `database` | Curated structured datasets | UniProt, PDB, ChEMBL, NCBI Gene, Ensembl |
| `consortium` | Multi-institution data releases | Human Cell Atlas, ENCODE, GTEx, UK Biobank summaries |
| `oral-tradition` | Documented traditional medicine knowledge — must cite the *documenting* source | Recorded interviews, ethnobotany papers, traditional pharmacopoeia |

If a source spans two types (e.g., a peer-reviewed paper *about* a database), choose the type that best describes *what is being cited*, not what wrote about it.

---

## Examples

### Peer-reviewed paper

```yaml
sources:
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
```

### Open textbook chapter

```yaml
sources:
  - id: openstax-anatomy-19-1
    type: textbook
    cite: "OpenStax, Anatomy & Physiology, Ch. 19.1: Heart Anatomy. 2nd ed."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy"
    accessed: "2026-06-03"
```

### Curated database

```yaml
sources:
  - id: uniprot-p12883-myh7
    type: database
    cite: "UniProt entry P12883 (MYH7_HUMAN), beta-myosin heavy chain."
    url: "https://www.uniprot.org/uniprotkb/P12883/entry"
    accessed: "2026-06-03"
```

### Clinical guideline

```yaml
sources:
  - id: aha-2022-hf-guideline
    type: clinical-guideline
    cite: "Heidenreich PA et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032."
    doi: "10.1161/CIR.0000000000001063"
```

---

## How sources are referenced from entries

Inside an atlas entry's frontmatter, list every source under the `sources` array:

```yaml
---
sources:
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    ...
  - id: openstax-anatomy-19-1
    type: textbook
    ...
---
```

Inside the entry body, reference sources by `id` in inline-citation form:

```markdown
The cardiac action potential is dominated by L-type Ca²⁺ current during phase 2 [^bers-2002-cardiac-ec-coupling].

[^bers-2002-cardiac-ec-coupling]: See entry frontmatter.
```

The validator checks that every `[^id]` reference resolves to a `sources[].id`.

---

## Validation rules (enforced by `tools/scripts/validate-entries.py`)

1. `id` must be unique within a single entry's `sources` array.
2. `type` must be one of the enumerated values.
3. `cite` must be non-empty.
4. If `type` is `peer-reviewed` or `preprint`, exactly one of `doi`, `pmid`, or `url` must be present.
5. If neither `doi` nor `pmid` is present, `accessed` must be set.
6. `accessed`, if set, must be a valid `YYYY-MM-DD` date.
7. **At least one of `url`, `doi`, or `pmid` must be present in every source.** A citation with none of these fields is not linkable and will generate a warning.

---

## What does NOT belong in `sources`

- Personal communications (use `oral-tradition` only when *documented*; otherwise the claim isn't yet defensible)
- Wikipedia links (use Wikipedia's own primary source instead)
- Generative AI output (no AI-authored facts; AI-assisted *drafting* is fine but the underlying source must be human-authored)

---

**[← Back to schemas index](README.md)**
