# Entry Frontmatter Schema (shared spine across all atlases)

The **shared YAML frontmatter contract** that every atlas entry — Human, Pathogen, Medicine, Vaccine — must satisfy. Atlas-specific fields live in per-atlas extension schemas; this doc defines the spine they all inherit.

> **Status:** Adopted. JSON Schema companion not yet written. Per-atlas schemas — `human-scale-entry.schema.md`, `pathogen-entry.schema.md` *(planned)*, `medicine-entry.schema.md` *(planned)*, `vaccine-entry.schema.md` — extend this spine.

**Consumers:**
- All atlas entries: `atlases/01-human/**/README.md`, `atlases/02-pathogen/**/README.md`, `atlases/03-medicine/**/README.md`, `atlases/04-vaccine/**/README.md` (planned)
- `tools/scripts/validate-entries.py`
- The graph-build step that compiles atlases into JSON-LD / RDF for AI consumption (planned, see `tools/`)
- Any project that walks the atlases as a knowledge graph

---

## Why a shared spine

The mission is for an AI agent to reason **across all four atlases at once** — host biology, pathogens, medicines, vaccines — to design new vaccines faster than viruses mutate. That reasoning is graph traversal, and graph traversal only works if every node is the same shape.

Today each atlas grows its own entry conventions. Without a shared spine:

- The graph-build step has to special-case each atlas.
- Cross-atlas validation (back-link presence, ID resolution, citation integrity) duplicates code per atlas.
- Adding a new atlas (Pathology, Clinical, Public Health, Genetics, Imaging) means rewriting the contract each time.

A shared spine fixes all three. Per-atlas schemas still exist — they just *extend* the spine instead of redefining it.

---

## File location & ID rules

Every atlas entry lives at:

```
atlases/<NN-atlas>/<...optional category levels>/<entry-id>/README.md
```

Examples:

```
atlases/01-human/06-organ/heart/README.md
atlases/01-human/03-molecular/troponin-complex/README.md
atlases/02-pathogen/01-viruses/sars-cov-2/README.md
atlases/03-medicine/01-modern/04-cardio/statins/README.md
atlases/04-vaccine/01-mrna/mrna-1273/README.md      (planned)
```

**Local ID rules:**
- The folder name is the entry's local `id`.
- `id` is **kebab-case**, ASCII, no spaces, no dots.
- `id` must be **globally unique within its atlas** (not just within its scale/category).
- `id` must equal the immediate parent folder name.

**Stable URI (derived, not stored):**

Each entry has a globally-unique URI derived from its path:

```
<atlas-prefix>:<id>
```

| Atlas | Prefix | Example URI |
|:---|:---|:---|
| `01-human` | `human` | `human:heart`, `human:troponin-complex`, `human:cardiomyocyte` |
| `02-pathogen` | `pathogen` | `pathogen:sars-cov-2`, `pathogen:mycobacterium-tuberculosis` |
| `03-medicine` | `medicine` | `medicine:atorvastatin`, `medicine:metoprolol` |
| `04-vaccine` *(planned)* | `vaccine` | `vaccine:mrna-1273`, `vaccine:bnt162b2` |

The URI is **derived by tooling** at graph-build time — authors do not write it in frontmatter. This avoids drift between path and URI. Authors write `id` (the local kebab-case slug); the build step composes the URI from `(atlas, id)`.

> **Why local IDs and not URIs in source?** Authors write paths and folder names in real life — `cd atlases/01-human/06-organ/heart` is how the work happens. Forcing them to also write `human:heart` in YAML doubles the surface for typos and drift. Derive once, validate forever.

---

## Required fields (every atlas)

| Field | Type | Description |
|:---|:---|:---|
| `schema` | const string | The per-atlas schema this entry conforms to: `human-scale-entry/v1`, `pathogen-entry/v1`, `medicine-entry/v1`, `vaccine-entry/v1`. |
| `id` | string (kebab-case) | Local slug. Must equal folder name. Globally unique within atlas. |
| `name` | string | Display name as a reader expects to see it. |
| `atlas` | enum | One of `01-human`, `02-pathogen`, `03-medicine`, `04-vaccine` (and future atlases as added). |
| `status` | enum | `stub`, `draft`, `reviewed`, `expert-validated`. See *Status lifecycle* in [`human-scale-entry.schema.md`](human-scale-entry.schema.md#status-lifecycle). |
| `last_reviewed` | ISO date `YYYY-MM-DD` | When the entry was last reviewed for accuracy. |
| `summary` | string (≤ 280 chars) | One-sentence definition. The first thing a reader or agent sees. |
| `sources` | array of [Citation](citation.schema.md) | At least one. Every claim in the body must trace to one of these. |

---

## Recommended fields (every atlas)

| Field | Type | Description |
|:---|:---|:---|
| `cross_links` | array of [CrossLink](cross-link.schema.md) | Typed edges to other atlas entries. Required for any entry past `stub`. The relation must come from [`relation-vocabulary.schema.md`](relation-vocabulary.schema.md). |
| `xrefs` | object | External-ontology cross-references. See *External cross-references* below. Strongly recommended for every entry. |
| `aliases` | array of strings | Synonyms and historical names. |
| `contributors` | array of strings | Names or GitHub handles of substantive contributors / reviewers. |

---

## Optional fields (every atlas)

| Field | Type | Description |
|:---|:---|:---|
| `media` | array | References to images, videos, 3D models, simulators. See media block in [`human-scale-entry.schema.md`](human-scale-entry.schema.md#media-format). |
| `taxonomy` | object | Atlas-specific structured fields. See per-atlas schemas. |
| `provenance` | object | If the entry was generated or seeded by an automated ingestion pipeline (e.g., from UniProt/PDB/DrugBank), record the pipeline run. See *Provenance* below. |

---

## External cross-references — the `xrefs` block

A first-class field that maps every entry to its identifiers in canonical reference databases. This is what lets the AI agent (and humans) connect Human Engineering's atlas to the rest of the world's biomedical data.

```yaml
xrefs:
  uniprot: "P12883"             # protein
  pdb: ["4DB1", "5N69"]         # structures
  pfam: "PF00063"               # protein family
  gene_symbol: "MYH7"           # HGNC gene symbol
  hgnc: "7577"                  # HGNC numeric ID
  ensembl_gene: "ENSG00000092054"
  uberon: "UBERON:0000948"      # anatomy ontology
  fma: "FMA:7088"               # Foundational Model of Anatomy
  cell_ontology: "CL:0000746"   # Cell Ontology
  go: ["GO:0006936", "GO:0030017"]   # Gene Ontology terms
  chebi: "CHEBI:15422"          # ChEBI for small molecules
  drugbank: "DB01076"           # DrugBank for drugs
  chembl: "CHEMBL1487"
  rxnorm: "83367"               # RxNorm for clinical drug
  atc: "C10AA05"                # ATC classification
  ncbi_taxon: "2697049"         # NCBI Taxonomy ID for organisms/pathogens
  refseq: "NC_045512.2"         # RefSeq genome / transcript
  doid: "DOID:14250"            # Disease Ontology (where applicable)
  snomed: "73211009"
  icd11: "8E62.4"
  meddra: "10000648"
  vo: "VO:0000022"              # Vaccine Ontology (for vaccine entries)
```

**Rules:**
- Every key is **optional individually**, but every entry must have *at least one* xref where one applies (e.g., a protein entry without a UniProt ID is a smell).
- Values are strings (or arrays of strings for one-to-many fields like `pdb` or `go`).
- The validator does **not** verify that IDs *exist* in their source databases (that requires online lookup, deferred). It does verify ID *format* (regex per database).
- Atlas-appropriate keys are listed in each per-atlas schema; the full master list lives in `schemas/xrefs.registry.md` *(planned)*.

The presence of strong xrefs is what turns the atlas from a wiki into an interoperable knowledge graph node.

---

## Provenance (for ingested entries)

When an entry is created or seeded by an automated pipeline (UniProt fetch, PDB scrape, DrugBank import), record the run:

```yaml
provenance:
  ingested_by: "tools/scripts/ingest-uniprot.py"
  ingested_at: "2026-06-04T09:33:00Z"
  source_db: "UniProt"
  source_id: "P12883"
  source_version: "2026_03"
  human_curated: false           # set true when a human reviews & expands
```

Every entry past `status: stub` should be **human-curated** even if originally ingested. The `human_curated` flag lets the AI agent (and reviewers) distinguish raw imports from reviewed knowledge.

---

## What goes in per-atlas extension schemas

Each per-atlas schema **extends this spine** by:

1. Locking `atlas` and `schema` to its specific values.
2. Defining atlas-specific scale or category enums (e.g., `scale` for Human, `kingdom` for Pathogen, `class` for Medicine, `platform` for Vaccine).
3. Adding atlas-specific required body sections.
4. Specifying which relations are legal source-side from this atlas (the atlas-pair tables in [`relation-vocabulary.schema.md`](relation-vocabulary.schema.md)).
5. Listing which `xrefs` keys are atlas-relevant.

The four per-atlas schemas:

| Schema | Status | File |
|:---|:---|:---|
| `human-scale-entry/v1` | exists | [`human-scale-entry.schema.md`](human-scale-entry.schema.md) |
| `pathogen-entry/v1` | implicit (referenced in entries; spec doc not yet written) | *to write* |
| `medicine-entry/v1` | implicit | *to write* |
| `vaccine-entry/v1` | not yet started; mission-critical | *to write* |

---

## Worked example — minimum viable entry

```yaml
---
schema: human-scale-entry/v1
id: ace2
name: ACE2
atlas: 01-human
status: draft
last_reviewed: 2026-06-04
summary: "Angiotensin-converting enzyme 2; carboxypeptidase that cleaves angiotensin II → angiotensin-(1-7); receptor for SARS-CoV-2 spike protein."
aliases: ["angiotensin-converting enzyme 2", "ACEH"]
xrefs:
  uniprot: "Q9BYF1"
  gene_symbol: "ACE2"
  hgnc: "13557"
  pdb: ["1R42", "6M0J", "6VW1"]
  go: ["GO:0008241", "GO:0001618"]
sources:
  - id: hoffmann-2020-ace2-entry
    type: peer-reviewed
    cite: "Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 cell entry depends on ACE2 and TMPRSS2. Cell. 2020;181(2):271-280."
    doi: "10.1016/j.cell.2020.02.052"
    pmid: "32142651"
cross_links:
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: bound-by
    scale: 03-molecular
    evidence: hoffmann-2020-ace2-entry
    note: "Spike RBD binds ACE2 with KD ~15 nM; primary entry receptor."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "ACE2 expressed on cardiomyocytes — molecular basis for direct viral infection of myocardium."
provenance:
  ingested_by: "tools/scripts/ingest-uniprot.py"
  ingested_at: "2026-06-04T09:33:00Z"
  source_db: "UniProt"
  source_id: "Q9BYF1"
  source_version: "2026_03"
  human_curated: false
---
```

---

## Validation rules (enforced by `tools/scripts/validate-entries.py`)

### Frontmatter spine
1. Frontmatter must parse as YAML.
2. Every required field must be present and well-typed.
3. `id` must equal the folder name.
4. `atlas` must equal the top-level atlas folder of the entry's path.
5. `schema` must reference an existing per-atlas schema file.
6. `last_reviewed` must be a valid ISO date.
7. `summary` must be ≤ 280 characters.

### Sources
8. Every entry in `sources` must validate against `citation.schema.json`.
9. Every `[^id]` reference in the body must match a `sources[].id`.

### Cross-links
10. Every entry in `cross_links` must validate against `cross-link.schema.json`.
11. Every cross-link `target` must resolve to an existing entry.
12. Every `relation` must be a member of [`relation-vocabulary.schema.md`](relation-vocabulary.schema.md).
13. The `(source-atlas, relation, target-atlas)` triple must be legal per the atlas-pair tables.

### Xrefs
14. If `xrefs` is present, every key must be in the registry.
15. Each value must match its registered format regex.

### Per-atlas extensions
16. Per-atlas schemas (e.g., `human-scale-entry/v1`) layer additional rules on top of these.

---

## Versioning

This is `entry-frontmatter/v1`. Per-atlas schemas reference the spine version they extend. Breaking changes to the spine bump the per-atlas schemas as well; non-breaking additions (new optional fields, new `xrefs` keys) do not.

---

**[← Back to schemas index](README.md)**
