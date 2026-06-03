# Human Scale Entry Schema

Every entry in the **Human Atlas** — at every scale from subatomic to whole-body — conforms to this structure.

> **Machine-readable companion:** [`human-scale-entry.schema.json`](human-scale-entry.schema.json) — JSON Schema for the YAML frontmatter.

**Consumers:**
- `atlases/01-human/**/README.md` (every Human Atlas entry)
- `tools/scripts/validate-entries.py`
- `comp-prog-proj/*/` (any project that ingests Human Atlas data)

---

## Why a single schema for all 8 scales?

The scale ladder — subatomic → atomic → molecular → cellular → tissue → organ → system → whole-body — is a *continuum*, not 8 disconnected layers. A single schema with **scale-aware sections** keeps cross-scale traversal and validation simple. An organ entry and a molecule entry have the same frontmatter contract, the same citation format, the same cross-link format — they differ only in which body sections are required.

---

## File location

Every entry lives at:

```
atlases/01-human/<NN-scale>/<entry-id>/README.md
```

Examples:
- `atlases/01-human/06-organ/heart/README.md`
- `atlases/01-human/05-tissue/myocardium/README.md`
- `atlases/01-human/04-cellular/cardiomyocyte/README.md`
- `atlases/01-human/03-molecular/troponin-complex/README.md`

The folder name is the `id`. The `id` is a kebab-case slug, globally unique within the Human Atlas.

---

## File format

Every entry is a Markdown file with **YAML frontmatter**:

```markdown
---
schema: human-scale-entry/v1
id: heart
name: Heart
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-03
summary: "The four-chambered muscular pump that drives the cardiovascular system."
sources:
  - id: openstax-anatomy-19-1
    type: textbook
    cite: "OpenStax Anatomy & Physiology, Ch 19.1: Heart Anatomy."
    url: "https://openstax.org/..."
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/05-tissue/myocardium
    relation: contains
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
simulator: docs/sim/heart.html
---

# Heart

## Overview
...

## Structure
...
```

---

## Frontmatter contract

### Required fields

| Field | Type | Description |
|:---|:---|:---|
| `schema` | const `human-scale-entry/v1` | Schema version this entry conforms to. |
| `id` | string (kebab-case) | Slug — must match the folder name. |
| `name` | string | Display name. Capitalized as a reader expects to see it. |
| `atlas` | const `01-human` | Atlas membership. |
| `scale` | enum | One of `01-subatomic`, `02-atomic`, `03-molecular`, `04-cellular`, `05-tissue`, `06-organ`, `07-system`, `08-whole-body`. |
| `status` | enum | `stub`, `draft`, `reviewed`, `expert-validated`. See *Status lifecycle* below. |
| `last_reviewed` | ISO date `YYYY-MM-DD` | When the entry was last reviewed for accuracy. |
| `summary` | string (≤ 280 chars) | One-sentence definition. The first thing a reader or agent sees. |
| `sources` | array of [Citation](citation.schema.md) | At least one source. Every claim in the body must be traceable here. |

### Recommended fields

| Field | Type | Description |
|:---|:---|:---|
| `cross_links` | array of [CrossLink](cross-link.schema.md) | Edges to other atlas entries. Strongly preferred for any entry past `stub`. |
| `aliases` | array of strings | Synonyms a reader might search for. |
| `contributors` | array of strings | Names or GitHub handles of people who substantively wrote or reviewed this entry. |

### Optional fields

| Field | Type | Description |
|:---|:---|:---|
| `simulator` | string (relative path) | Path to an interactive simulator HTML page (typically `docs/sim/<id>.html`). |
| `media` | array | References to images, videos, or 3D models. See *Media format* below. |
| `taxonomy` | object | Scale-specific structured fields. See *Scale-specific structure* below. |

---

## Body sections

Required for **all scales**:

- `## Overview` — the entry, defined and contextualized in 1–3 paragraphs.
- `## Structure` — what is it physically? Anatomy / morphology / molecular geometry / chemical composition, depending on scale.
- `## Function` — what does it do? Physiological role, mechanism, contribution to the next-larger scale.
- `## Connections` — narrative summary of the cross-links: what it contains, what contains it, what pathogens damage it, what medicines modulate it.

Required at specific scales:

| Scale | Additional required sections |
|:---|:---|
| `06-organ`, `07-system`, `08-whole-body` | `## Pathology` — diseases of this entry. Cross-references the Pathogen Atlas where infectious; otherwise summarizes mechanisms. |
| `04-cellular` | `## Lifecycle` — origin, differentiation, division, death. |
| `03-molecular` | `## Mechanism` — biochemical or biophysical mechanism, in detail. |
| `01-subatomic`, `02-atomic` | (Overview + Structure + Function + Connections only — these scales are foundational, not biological.) |

Recommended for any scale:

- `## Variation` — natural variation, polymorphisms, sex differences, age-related differences, demographic differences. Critical for the *For Humanity* principle: a model that ignores variation is a model of one person.
- `## Open questions` — what is genuinely unsettled? Honest uncertainty.
- `## See also` — pointers to related entries beyond the formal cross-links.

---

## Status lifecycle

| Status | What it means |
|:---|:---|
| `stub` | Folder exists, frontmatter valid, body has at least Overview. Acceptable as a placeholder when needed for cross-linking from a more developed entry. |
| `draft` | All required sections present, source-backed, internally consistent. Has not yet been reviewed by anyone other than the original author. |
| `reviewed` | At least one other contributor has read the entry end-to-end and signed off. Recorded in `contributors`. |
| `expert-validated` | A domain expert (clinician, researcher, or specialist in the topic) has reviewed and signed off. The expert is named in `contributors` with their qualification noted. |

`expert-validated` is the bar for entries that the project markets as authoritative. Until enough entries reach it, the live site clearly labels content with its status.

---

## Scale-specific structure (the optional `taxonomy` field)

For some scales, structured data beyond prose is valuable. When provided, it lives in the `taxonomy` field of the frontmatter and follows scale-specific conventions:

### `03-molecular`

```yaml
taxonomy:
  uniprot: "P12883"        # for proteins
  gene_symbol: "MYH7"
  ec_number: ""            # if enzyme
  pdb_examples: ["4DB1", "5N69"]
```

### `04-cellular`

```yaml
taxonomy:
  cell_ontology: "CL:0000746"   # Cell Ontology ID
  lineage: "mesoderm"
```

### `06-organ`, `07-system`

```yaml
taxonomy:
  uberon: "UBERON:0000948"      # Uberon anatomy ontology ID
  fma: "FMA:7088"               # Foundational Model of Anatomy ID
```

These fields are optional; if present, they must follow the format above. The validator does not check that the IDs *exist* in their respective ontologies — that's a stronger check that requires online lookup, deferred to a later tooling phase.

---

## Media format

```yaml
media:
  - kind: image
    path: media/heart/heart-anatomy.svg
    caption: "Cross-section of the four-chambered heart with major vessels labeled."
    license: CC-BY-4.0
    source: "Wikimedia Commons, author: ..."
  - kind: 3d-model
    path: media/heart/heart.glb
    caption: "Public-domain anatomical mesh for the 3D viewer."
    license: CC0
```

Required `kind` values: `image`, `video`, `3d-model`, `audio`. Every media entry must have a `license` and either a `source` or attribution within `caption`.

---

## Worked example — Heart entry skeleton

```markdown
---
schema: human-scale-entry/v1
id: heart
name: Heart
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-03
summary: "The four-chambered muscular pump that drives the cardiovascular system, beating ~100,000 times per day to circulate ~7,500 L of blood."
aliases: ["cardiac muscle organ", "cor"]
sources:
  - id: openstax-anatomy-19-1
    type: textbook
    cite: "OpenStax Anatomy & Physiology, Ch. 19.1: Heart Anatomy."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy"
    accessed: "2026-06-03"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
cross_links:
  - target: 01-human/05-tissue/myocardium
    relation: contains
  - target: 01-human/05-tissue/endocardium
    relation: contains
  - target: 01-human/05-tissue/epicardium
    relation: contains
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
  - target: 02-pathogen/viruses/coxsackievirus-b
    relation: damaged-by
    scale: 04-cellular
    note: "Cytolytic infection of cardiomyocytes; immune-mediated inflammation."
  - target: 03-medicine/cardiovascular/metoprolol
    relation: modulated-by
    scale: 03-molecular
    note: "β1-adrenergic blockade reduces heart rate and contractility."
taxonomy:
  uberon: "UBERON:0000948"
  fma: "FMA:7088"
simulator: docs/sim/heart.html
---

# Heart

## Overview
...

## Structure
...

## Function
...

## Connections
...

## Pathology
...

## Variation
...

## Open questions
...
```

---

## Validation rules (enforced by `tools/scripts/validate-entries.py`)

### Frontmatter
1. Frontmatter must parse as YAML.
2. Frontmatter must validate against `human-scale-entry.schema.json`.
3. `id` must equal the folder name.
4. `scale` must equal the parent folder name (e.g., entry under `06-organ/` must have `scale: 06-organ`).
5. Every entry in `sources` must validate against `citation.schema.json`.
6. Every entry in `cross_links` must validate against `cross-link.schema.json`.
7. Every cross-link `target` must resolve to an existing entry.
8. Every cross-link `evidence` (if set) must match a `sources[].id`.

### Body
9. The `# <Name>` heading must equal the frontmatter `name`.
10. All scale-required sections must be present as `## <Section>` headings.
11. Inline citation references `[^id]` must match a `sources[].id`.

---

## Versioning

This schema's version is encoded in the `schema:` frontmatter field (`human-scale-entry/v1`). Breaking changes will bump to `v2` while keeping `v1` validation alive until all entries migrate.

---

**[← Back to schemas index](README.md)**
