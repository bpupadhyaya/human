# Pathogen Entry Schema

Every entry in the **Pathogen Atlas** (`atlases/02-pathogen/`) — across every biological category from viruses to prions — conforms to this structure.

> **Status:** Adopted. Extends the spine in [`entry-frontmatter.schema.md`](entry-frontmatter.schema.md). JSON Schema companion not yet written.

**Consumers:**
- `atlases/02-pathogen/**/README.md` (every Pathogen Atlas entry)
- `tools/scripts/validate-entries.py`
- `comp-prog-proj/*/` (any project that ingests Pathogen Atlas data)

---

## Why a single schema for all pathogen categories?

Pathogens span a vast biological range — viruses (from 20 nm to >2,500 nm), bacteria (unicellular prokaryotes), fungi (eukaryotes), parasites (helminths, protozoa), and prions (misfolded proteins). A single schema with **category-aware sections** keeps cross-pathogen comparison and graph traversal simple. A prion entry and an RNA virus entry share the same frontmatter contract, the same citation format, the same cross-link format — they differ only in which sections are present and what the Biology/Structure section discusses.

---

## File location

Every entry lives at:

```
atlases/02-pathogen/<NN-category>/<entry-id>/README.md
```

Examples:
- `atlases/02-pathogen/01-viruses/sars-cov-2/README.md`
- `atlases/02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md`
- `atlases/02-pathogen/03-fungi/aspergillus-fumigatus/README.md`
- `atlases/02-pathogen/04-parasites/plasmodium-falciparum/README.md`
- `atlases/02-pathogen/05-prions/creutzfeldt-jakob/README.md`

The folder name is the local `id` (kebab-case, ASCII, lowercase). Entries may be focused on a specific disease manifestation (e.g., SARS-CoV-2 is primarily covered in the cardiac context) or may be general entries for the pathogen.

---

## File format

Every entry is a Markdown file with **YAML frontmatter**:

```markdown
---
schema: pathogen-entry/v1
id: mycobacterium-tuberculosis
name: Mycobacterium tuberculosis
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-03
summary: "Aerobic acid-fast bacillus (Mycobacteriaceae). Causes TB — leading infectious disease killer (~1.5 million deaths/year)."
aliases: ["Mtb", "M. tuberculosis", "TB bacillus"]
sources:
  - id: who-tb-report-2023
    type: regulatory
    cite: "WHO. Global Tuberculosis Report 2023."
    url: "https://www.who.int/..."
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/07-system/respiratory-system
    relation: damages
    note: "Primary site of infection — pulmonary TB."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Blocks phagosome maturation to evade macrophage killing."
---

# Mycobacterium tuberculosis

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
| `schema` | const `pathogen-entry/v1` | Schema version this entry conforms to. |
| `id` | string (kebab-case) | Slug — must match the folder name. |
| `name` | string | Display name. Species names in standard binomial notation. Viruses as commonly known (e.g., "SARS-CoV-2"). |
| `atlas` | const `02-pathogen` | Atlas membership. |
| `scale` | enum | One of `01-viruses`, `02-bacteria`, `03-fungi`, `04-parasites`, `05-prions`. |
| `status` | enum | `stub`, `draft`, `reviewed`, `expert-validated`. See *Status lifecycle* below. |
| `last_reviewed` | ISO date `YYYY-MM-DD` | When the entry was last reviewed for accuracy. |
| `summary` | string (≤ 280 chars) | One-sentence definition. Include taxonomic family and one key clinical fact. |
| `sources` | array of [Citation](citation.schema.md) | At least one source. Every epidemiological claim must be traceable here. |

### Recommended fields

| Field | Type | Description |
|:---|:---|:---|
| `cross_links` | array of [CrossLink](cross-link.schema.md) | Edges to Human Atlas entries (damages, infects), Medicine Atlas (treated-by), Vaccine Atlas (target-of). |
| `aliases` | array of strings | Common names, strain designations, ICTV or NCBI names a reader might search. |
| `taxonomy` | object | Structured biological classification. |

### Optional fields

| Field | Type | Description |
|:---|:---|:---|
| `ncbi_taxid` | integer | NCBI Taxonomy ID (e.g., `2697049` for SARS-CoV-2). |
| `who_priority` | string | WHO priority classification (e.g., `"WHO Priority Pathogen — Critical"`, `"WHO Select Agent"`). |
| `bsl` | enum | Biosafety level: `"BSL-1"`, `"BSL-2"`, `"BSL-3"`, `"BSL-4"`. |
| `pandemic_potential` | boolean | Whether WHO or CDC has flagged this pathogen for pandemic potential. |
| `notifiable` | boolean | Whether infection is reportable to public health authorities in most jurisdictions. |
| `contributors` | array of strings | Names or GitHub handles of contributors who wrote or reviewed this entry. |

### `taxonomy` sub-object (example for a virus)

```yaml
taxonomy:
  domain: Riboviria
  family: Coronaviridae
  genus: Betacoronavirus
  species: "Severe acute respiratory syndrome-related coronavirus"
  genome: "+ssRNA"            # genome type: +ssRNA, -ssRNA, dsDNA, ssDNA, dsRNA, ssRNA-RT
  genome_size_kb: 29.9
  host_range: ["mammals", "birds"]
```

---

## Body sections

Required for **all categories**:

- `## Overview` — the pathogen, defined and contextualized: classification, disease, global burden, why it matters.
- `## Structure` — morphology, genome organization, surface proteins/antigens, key virulence factors. This is the section vaccine antigen design draws from.
- `## Infection Mechanism` — host entry, cell/tissue tropism, receptor(s), replication cycle, spread.
- `## Host Interactions` — immune evasion strategies, innate/adaptive immune response triggered, clinical immunopathology.
- `## Connections` — narrative summary of cross-links: which human systems it damages, which medicines treat it, which vaccines target it.
- `## Pathology` — organ- and system-level disease. Clinical presentation, complications, mortality.

Recommended for any category:

- `## Epidemiology` — transmission, incubation, R₀/Rt, global burden, population at risk, seasonality.
- `## Treatment` — standard-of-care antiviral/antibiotic/antifungal/antiparasitic agents; placeholder for Medicine Atlas cross-links.
- `## See Also` — related pathogens, taxonomically or clinically similar entries.

---

## Cross-link relations for pathogen entries

Pathogen entries use these relations in `cross_links`:

| Relation | Direction | Inverse | Meaning |
|:---|:---|:---|:---|
| `damages` | pathogen → human entry | `damaged-by` | Causes injury to an organ, tissue, cell type, or system. |
| `infects` | pathogen → human cell/tissue | `infected-by` | Actively replicates within this cell or tissue. |
| `treated-by` | pathogen → medicine entry | `treats` | A therapeutic agent that targets this pathogen. |
| `target-of` | pathogen → molecular/vaccine entry | `targets` | An antibody, drug molecule, or vaccine that acts on this pathogen. |

---

## Status lifecycle

| Status | What it means |
|:---|:---|
| `stub` | Folder exists, frontmatter valid, body has at least Overview. Acceptable as a placeholder when needed for cross-linking from a more developed entry. |
| `draft` | All required sections present, source-backed, internally consistent. Not yet independently reviewed. |
| `reviewed` | At least one other contributor has read the entry end-to-end and signed off. Recorded in `contributors`. |
| `expert-validated` | A domain expert (virologist, microbiologist, infectious disease specialist) has reviewed and signed off. Named in `contributors` with qualification. |

---

## Notes on entry focus

Some pathogens have tissue- or organ-specific entries because the pathogen is well-documented in that context (e.g., SARS-CoV-2 is currently documented in a cardiac-focus entry). As coverage expands, new entries may cover the same pathogen from different organ perspectives, or a general entry may replace multiple focused ones. The `id` slug identifies the entry — a second cardiac-vs-pulmonary distinction can be encoded in the `name` field.
