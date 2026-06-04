# Vaccine Entry Schema

Every entry in the **Vaccine Atlas** (`atlases/04-vaccine/`) — across every platform from inactivated whole-virus to mRNA — conforms to this structure.

> **Status:** Adopted. Extends the spine in [`entry-frontmatter.schema.md`](entry-frontmatter.schema.md). JSON Schema companion not yet written.

**Consumers:**
- `atlases/04-vaccine/**/README.md` (every Vaccine Atlas entry)
- `tools/scripts/validate-entries.py`
- `comp-prog-proj/*/` (any project that ingests Vaccine Atlas data)
- The graph-build step (vaccines are the *output artifact* the AI agent produces — schema rigor here is mission-critical)

---

## Why a single schema for every vaccine platform?

Vaccines span a vast platform diversity — mRNA, viral-vector, recombinant-subunit, inactivated, live-attenuated, virus-like-particle, conjugate, polysaccharide, toxoid, DNA, peptide, dendritic-cell, plant-based, and combinations of these. A single schema with **platform-aware sections** keeps cross-platform comparison simple and the graph uniform. A live-attenuated MMR entry and an mRNA-1273 entry have the same frontmatter contract, the same citation format, the same cross-link format — they differ only in which platform-specific sections are required and how the antigen is delivered.

The schema is **inclusive by design** — ancient (variolation, smallpox), modern (mRNA, viral vector), traditional (BCG, MMR, polio family), investigational (DNA, saRNA, peptide), and discontinued (Pandemrix, RotaShield) vaccines all fit. Status lifecycle handles maturity; `discontinued: true` handles withdrawal.

---

## File location

Every entry lives at:

```
atlases/04-vaccine/<NN-platform>/<entry-id>/README.md
```

Examples:
- `atlases/04-vaccine/01-mrna/mrna-1273/README.md`
- `atlases/04-vaccine/01-mrna/bnt162b2/README.md`
- `atlases/04-vaccine/02-viral-vector/azd1222/README.md`
- `atlases/04-vaccine/05-live-attenuated/mmr/README.md`
- `atlases/04-vaccine/04-inactivated/coronavac/README.md`

Folder name is the local `id` (kebab-case, ASCII, lowercase). Combination vaccines (e.g., DTaP) live under their primary platform with sub-antigens listed in the entry.

---

## Platform sub-folders

| # | Folder | Platform | Examples |
|:---:|:---|:---|:---|
| 01 | `01-mrna/` | mRNA (modified-nucleoside or self-amplifying) | mRNA-1273, BNT162b2, ARCT-154 |
| 02 | `02-viral-vector/` | Replication-deficient or replication-competent viral vector | AZD1222 (ChAdOx1), Ad26.COV2.S, Sputnik V, rVSV-ZEBOV |
| 03 | `03-recombinant-subunit/` | Recombinant protein subunit | NVX-CoV2373, Engerix-B (HBV), Shingrix |
| 04 | `04-inactivated/` | Inactivated whole pathogen | CoronaVac, Sinopharm BBIBP-CorV, Covaxin, IPV (Salk), inactivated influenza |
| 05 | `05-live-attenuated/` | Live attenuated organism | MMR, BCG, OPV (Sabin), varicella, yellow fever, FluMist, oral typhoid, rotavirus |
| 06 | `06-virus-like-particle/` | Virus-like particle (VLP) | Gardasil-9, Cervarix, Hep E (Hecolin) |
| 07 | `07-conjugate/` | Polysaccharide–protein conjugate | Hib (PRP-T), PCV13 / PCV15 / PCV20, MenACWY-CRM |
| 08 | `08-polysaccharide/` | Pure polysaccharide | PPSV23, MPSV4 |
| 09 | `09-toxoid/` | Inactivated toxin | Tetanus toxoid, diphtheria toxoid |
| 10 | `10-dna/` | DNA vaccine | ZyCoV-D, INO-4800 |
| 11 | `11-peptide/` | Synthetic peptide / epitope | Investigational cancer vaccines |
| 12 | `12-dendritic-cell/` | Dendritic-cell / cellular | Sipuleucel-T (Provenge) |
| 13 | `13-plant-based/` | Plant-produced protein | Covifenz (discontinued) |
| 14 | `14-bacterial-vector/` | Bacterial vector | Listeria-, Salmonella-vectored cancer vaccines |
| 99 | `99-other/` | Hybrid or novel platforms not yet categorized | — |

Numbering is **stable** — new platforms append. Combination vaccines (DTaP, MMRV, hexavalent) live under their dominant platform; the other components are recorded in `antigens:`.

---

## File format

Every entry is a Markdown file with **YAML frontmatter** extending [`entry-frontmatter.schema.md`](entry-frontmatter.schema.md).

```markdown
---
schema: vaccine-entry/v1
id: mrna-1273
name: mRNA-1273 (Spikevax)
atlas: 04-vaccine
platform: 01-mrna
status: draft
last_reviewed: 2026-06-04
summary: "Modified-nucleoside mRNA vaccine encoding the SARS-CoV-2 prefusion-stabilized (2P) spike, delivered in a lipid nanoparticle. Co-developed by Moderna and the NIH Vaccine Research Center; first dosed Mar 2020, EUA Dec 2020."
aliases: ["Spikevax", "Moderna COVID-19 vaccine", "CX-024414", "elasomeran"]
target_pathogens:
  - target: 02-pathogen/01-viruses/sars-cov-2
    antigen: spike-prefusion-2P
    coverage: ["wild-type", "alpha", "delta", "omicron-BA.1", "..."]
antigens:
  - name: "SARS-CoV-2 spike (prefusion-stabilized, 2P)"
    source_pathogen: 02-pathogen/01-viruses/sars-cov-2
    modification: "K986P + V987P (2P stabilization, Graham/McLellan/Corbett)"
    encoded_as: "modified-nucleoside mRNA (N1-methylpseudouridine)"
    structure_ref: { pdb: ["6VSB", "6VXX"] }
delivery_system: "lipid-nanoparticle (LNP, SM-102 ionizable lipid; Moderna proprietary)"
adjuvants: []
route_of_administration: "intramuscular"
dose_schedule:
  primary_series: "2 doses, 28 days apart, 100 µg each (adults ≥18)"
  pediatric_50ug: "2 doses, 28 days apart, 50 µg (ages 6–17)"
  pediatric_25ug: "2 doses, 28 days apart, 25 µg (ages 6 months–5 years)"
  booster: "single 50 µg dose ≥ 5 months after primary"
manufacturer:
  developer: "Moderna, Inc. (with NIAID/VRC)"
  partners: ["Acuitas (LNP IP)", "Lonza (manufacturing)", "Catalent (fill-finish)"]
regulatory_status:
  - body: "FDA"
    status: "EUA"
    date: "2020-12-18"
  - body: "FDA"
    status: "BLA-approved (Spikevax)"
    date: "2022-01-31"
  - body: "EMA"
    status: "Conditional Marketing Authorization"
    date: "2021-01-06"
  - body: "WHO"
    status: "Emergency Use Listing"
    date: "2021-04-30"
discontinued: false
xrefs:
  drugbank: "DB15654"
  rxnorm: "2468230"
  vo: "VO:0005177"
sources:
  - id: baden-2021-cove
    type: peer-reviewed
    cite: "Baden LR, El Sahly HM, Essink B, et al. Efficacy and safety of the mRNA-1273 SARS-CoV-2 vaccine. NEJM. 2021;384(5):403-416."
    doi: "10.1056/NEJMoa2035389"
    pmid: "33378609"
cross_links:
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: immunizes-against
    evidence: baden-2021-cove
    note: "Phase 3 efficacy 94.1% against symptomatic COVID-19 (wild-type / pre-Omicron)."
  - target: 04-vaccine/01-mrna/bnt162b2
    relation: same-platform-as
    note: "Both modified-nucleoside mRNA-LNP encoding 2P spike."
---

# mRNA-1273 (Spikevax)

## Overview
...

## Platform
...
```

---

## Frontmatter contract

Inherits all required spine fields from [`entry-frontmatter.schema.md`](entry-frontmatter.schema.md): `schema`, `id`, `name`, `atlas`, `status`, `last_reviewed`, `summary`, `sources`. Adds the vaccine-specific fields below.

### Required (vaccine-specific)

| Field | Type | Description |
|:---|:---|:---|
| `schema` | const `vaccine-entry/v1` | Schema version. |
| `atlas` | const `04-vaccine` | Atlas membership. |
| `platform` | enum | One of `01-mrna`, `02-viral-vector`, `03-recombinant-subunit`, `04-inactivated`, `05-live-attenuated`, `06-virus-like-particle`, `07-conjugate`, `08-polysaccharide`, `09-toxoid`, `10-dna`, `11-peptide`, `12-dendritic-cell`, `13-plant-based`, `14-bacterial-vector`, `99-other`. Must equal the parent folder name. |
| `target_pathogens` | array | The pathogens this vaccine immunizes against. Each item: `target` (cross-link path), `antigen` (name), optional `coverage` (array of variants/strains). At least one. |
| `antigens` | array | The antigen(s) presented by this vaccine. Each item: `name`, optional `source_pathogen` cross-link path, optional `modification`, optional `encoded_as` (for nucleic-acid vaccines), optional `structure_ref` (PDB IDs). |
| `delivery_system` | string | LNP, viral capsid, alum-adsorbed, electroporation, plain-injection, etc. For viral-vector vaccines, name the vector (e.g., `chimpanzee-adenovirus-ChAdOx1`). |
| `adjuvants` | array of strings | Names of adjuvants used. Empty array `[]` if none. Examples: `aluminum-hydroxide`, `AS01`, `AS03`, `AS04`, `MF59`, `Matrix-M`, `CpG-1018`. For mRNA / viral-vector vaccines this is typically `[]`. |
| `route_of_administration` | enum | `intramuscular`, `subcutaneous`, `intradermal`, `intranasal`, `oral`, `microneedle-patch`, `electroporation`, `scarification`. |
| `manufacturer` | object | `developer` (lead organization), optional `partners` array. Captures who built it, distinct from who *funded* it (which goes in `sources`). |
| `regulatory_status` | array | One entry per regulator. Each: `body` (FDA / EMA / MHRA / PMDA / NMPA / WHO / DCGI / TGA / Health-Canada / Anvisa / etc.), `status` (e.g., `EUA`, `BLA-approved`, `Conditional Marketing Authorization`, `Emergency Use Listing`, `withdrawn`, `under-review`), `date` (ISO date). |

### Recommended (vaccine-specific)

| Field | Type | Description |
|:---|:---|:---|
| `dose_schedule` | object | Free-form keyed object — primary series, boosters, pediatric variants, immunocompromised regimens. |
| `efficacy` | array | One entry per pathogen × variant × endpoint. Each: `target` (pathogen cross-link), `variant` (string or `"wild-type"`), `endpoint` (e.g., `symptomatic-disease`, `severe-disease`, `hospitalization`, `death`, `transmission`), `point_estimate` (percent), `ci_low`, `ci_high`, `study_id` (citation source `id`). |
| `discontinued` | boolean | `true` if withdrawn from use globally; otherwise `false` or omitted. If `true`, add `discontinued_reason` (string) and `discontinued_date`. |
| `cold_chain` | string | Storage requirement (e.g., `−80°C ultra-cold`, `−20°C frozen`, `2–8°C refrigerator`, `room temperature`). |

### Optional (vaccine-specific)

| Field | Type | Description |
|:---|:---|:---|
| `cost_per_dose_usd` | number or range | Approximate, with `cost_year` and `cost_market` (e.g., `government-procurement-low-income`, `private-us`). |
| `clinical_trials` | array | NCT numbers + brief tag. |
| `who_essential_medicine` | boolean | Listed on WHO Model List of Essential Medicines. |
| `composition_per_dose` | object | mg/µg of antigen, lipid composition for LNPs, etc. |

The full common spine fields (`xrefs`, `aliases`, `cross_links`, `contributors`, `media`, `provenance`) are inherited from [`entry-frontmatter.schema.md`](entry-frontmatter.schema.md) — see that doc for their structure.

---

## Body sections

Required for **all platforms**:

- `## Overview` — what the vaccine is, why it exists, who it's for, in 1–3 paragraphs.
- `## Platform` — the technology underneath. For mRNA, the chemistry + LNP. For viral vector, the vector + insert. For inactivated, the inactivation method + adjuvant. For live-attenuated, the attenuation lineage.
- `## Antigen design` — what the immune system actually sees. Sequence source, modifications (e.g., 2P prefusion stabilization), conformational rationale, structural data (PDB IDs).
- `## Mechanism of immunity` — what arms of the immune response are elicited (humoral / cellular / mucosal), correlates of protection if known, expected duration.
- `## Manufacturing` — where it's made, scale, cold chain, supply constraints. Critical for the project's mission of fast pandemic response.
- `## Trials` — Phase 1/2/3 design, sample sizes, primary endpoints, efficacy results, follow-up duration. Cite the NCT IDs.
- `## Regulatory` — narrative of authorization timelines across regulators.
- `## Safety` — known adverse-event profile (rates, mechanisms where understood), contraindications, monitoring signals.

Required for **specific platforms**:

| Platform | Additional required sections |
|:---|:---|
| `01-mrna`, `10-dna` | `## Delivery system` — LNP composition, electroporation parameters, etc. |
| `02-viral-vector` | `## Vector` — origin organism, attenuation/replication-deficiency mechanism, anti-vector immunity considerations. |
| `04-inactivated`, `05-live-attenuated` | `## Strain & cell substrate` — passage history, cell line (Vero, MRC-5, embryonated egg, etc.). |
| `06-virus-like-particle`, `03-recombinant-subunit` | `## Expression system` — Sf9/baculovirus, yeast, CHO, plant, etc. |
| `07-conjugate` | `## Carrier protein` — CRM197, tetanus toxoid, etc. |

Recommended for any platform:

- `## Variation` — how response differs across age, immune status, sex, ethnicity, prior infection. Critical for the *For Humanity* principle.
- `## Equity & access` — pricing, COVAX status, LMIC distribution, IP / licensing.
- `## Open questions` — what's genuinely unsettled? Honest uncertainty.
- `## See also` — related entries beyond formal cross-links.

---

## Status lifecycle

Same four-stage lifecycle as [`human-scale-entry.schema.md`](human-scale-entry.schema.md#status-lifecycle): `stub` → `draft` → `reviewed` → `expert-validated`.

For vaccine entries, the bar for `expert-validated` is review by a vaccinologist, immunologist, or clinical-trial expert (named in `contributors` with qualification noted).

---

## Validation rules (enforced by `tools/scripts/validate-entries.py`)

In addition to the spine rules in [`entry-frontmatter.schema.md`](entry-frontmatter.schema.md#validation-rules):

### Frontmatter
1. `schema` must equal `vaccine-entry/v1`.
2. `atlas` must equal `04-vaccine`.
3. `platform` must equal the parent folder name and be in the platform enum.
4. `target_pathogens` must have at least one entry; each `target` must resolve to an existing Pathogen Atlas entry.
5. `antigens` must have at least one entry; each `source_pathogen` (if set) must resolve to an existing Pathogen Atlas entry.
6. `route_of_administration` must be in the enum.
7. Each `regulatory_status[].body` must be a recognized regulator (registry maintained in `schemas/regulators.registry.md` *(planned)*).
8. Each `regulatory_status[].date` must be a valid ISO date.
9. Each `efficacy[].study_id` (if set) must match a `sources[].id`.

### Cross-links
10. The `(04-vaccine, relation, target-atlas)` triple must be legal per [`relation-vocabulary.schema.md`](relation-vocabulary.schema.md).
11. Every entry in `target_pathogens` should have a corresponding `cross_links` entry with relation `immunizes-against` to the same target. (Warning if missing.)

### Body
12. All required body sections (universal + platform-specific) must be present as `## <Section>` headings.
13. Inline citation references `[^id]` must match a `sources[].id`.

---

## Versioning

This is `vaccine-entry/v1`. Adding new optional fields, new platforms, new regulators, or new adjuvants is **non-breaking**. Removing or renaming required fields is **breaking** — bump to `v2`.

---

**[← Back to schemas index](README.md)** · **[Spine](entry-frontmatter.schema.md)** · **[Relations](relation-vocabulary.schema.md)**
