# Medicine Entry Schema

Every entry in the **Medicine Atlas** (`atlases/03-medicine/`) — across every modality from small-molecule drugs to biologics, and every tradition from modern pharmacology to documented traditional medicine — conforms to this structure.

> **Status:** Adopted. Extends the spine in [`entry-frontmatter.schema.md`](entry-frontmatter.schema.md). JSON Schema companion not yet written.

**Consumers:**
- `atlases/03-medicine/**/README.md` (every Medicine Atlas entry)
- `tools/scripts/validate-entries.py`
- `comp-prog-proj/*/` (any project that ingests Medicine Atlas data)

---

## Why a single schema for all medicine traditions?

The Medicine Atlas holds a deliberate tension: modern pharmacology and traditional medicine coexist in the same schema, judged by the same evidentiary standard — evidence quality is made explicit in the `status` field and the `sources` block, not hidden by platform. "Modern science gets no automatic priority; tradition gets no automatic pass."

A small-molecule ACE inhibitor entry and a traditional herbal entry share the same frontmatter contract, the same citation format, the same cross-link format. They differ in what the Evidence section contains and what status they carry.

---

## File location

Every entry lives at:

```
atlases/03-medicine/<NN-tradition>/<category>/<entry-id>/README.md
```

Examples:
- `atlases/03-medicine/01-modern/04-cardio/ace-inhibitors/README.md`
- `atlases/03-medicine/01-modern/04-cardio/statins/README.md`
- `atlases/03-medicine/02-traditional/01-ayurveda/turmeric/README.md`
- `atlases/03-medicine/03-investigational/01-gene-therapy/crispr-cas9/README.md`

The folder name is the local `id` (kebab-case, ASCII, lowercase). Drug class entries (e.g., `ace-inhibitors`) cover the class as a whole; individual agent entries (e.g., `enalapril`) live nested within or alongside.

---

## File format

Every entry is a Markdown file with **YAML frontmatter**:

```markdown
---
schema: medicine-entry/v1
id: ace-inhibitors
name: ACE inhibitors
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-03
summary: "Angiotensin-converting enzyme inhibitors — competitive ACE inhibitors preventing Ang I→II conversion. First-line for HFrEF, hypertension, and diabetic nephropathy."
aliases: ["ACEi", "ACE inhibitors", "captopril", "enalapril", "lisinopril"]
sources:
  - id: consensus-1987
    type: peer-reviewed
    cite: "CONSENSUS Trial Study Group. Effects of enalapril on mortality in severe CHF. NEJM. 1987;316(23):1429-35."
    doi: "10.1056/NEJM198706043162301"
    pmid: "2883575"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: acts-on
    note: "Reduces systemic vascular resistance and aldosterone-mediated fluid retention."
  - target: 01-human/07-system/renal-system
    relation: treats
    note: "Renoprotective in CKD — reduces intraglomerular pressure and proteinuria."
---

# ACE inhibitors

## Overview
...
```

---

## Frontmatter contract

### Required fields

| Field | Type | Description |
|:---|:---|:---|
| `schema` | const `medicine-entry/v1` | Schema version this entry conforms to. |
| `id` | string (kebab-case) | Slug — must match the folder name. |
| `name` | string | Display name. Drug class entries use the class name; individual agents use generic name. |
| `atlas` | const `03-medicine` | Atlas membership. |
| `scale` | enum | One of `01-modern`, `02-traditional`, `03-investigational`. |
| `status` | enum | `stub`, `draft`, `reviewed`, `expert-validated`. See *Status lifecycle* below. |
| `last_reviewed` | ISO date `YYYY-MM-DD` | When the entry was last reviewed for accuracy. |
| `summary` | string (≤ 280 chars) | One-sentence definition. Include drug class, primary mechanism, and key indications. |
| `sources` | array of [Citation](citation.schema.md) | At least one source. Landmark trials, meta-analyses, or clinical guidelines preferred for modern entries. |

### Recommended fields

| Field | Type | Description |
|:---|:---|:---|
| `cross_links` | array of [CrossLink](cross-link.schema.md) | Edges to Human Atlas (acts-on, treats), Pathogen Atlas (treats), Vaccine Atlas (contains-adjuvant). |
| `aliases` | array of strings | Generic names, brand names, INN names, abbreviations a reader might search. |
| `drug_class` | string | Drug class or pharmacological category (e.g., `"beta-blocker"`, `"HMG-CoA reductase inhibitor"`). |
| `modality` | enum | `small-molecule`, `biologic`, `antibody`, `peptide`, `gene-therapy`, `cell-therapy`, `herbal`, `nutritional`, `device-based`, `other`. |
| `contributors` | array of strings | Names or GitHub handles of contributors who wrote or reviewed this entry. |

### Optional fields

| Field | Type | Description |
|:---|:---|:---|
| `key_agents` | array of strings | Individual drugs in a class entry (e.g., `["enalapril", "lisinopril", "ramipril", "captopril"]`). |
| `who_essential_medicine` | boolean | Whether on the WHO Model List of Essential Medicines. |
| `rxnorm` | string | RxNorm CUI for the class or lead agent. |
| `atc` | string | ATC code (e.g., `"C09AA"` for ACE inhibitors plain). |
| `approval_year` | integer | Year of first regulatory approval (any jurisdiction). |
| `fda_pregnancy_category` | string | Historical FDA pregnancy category (`"A"`, `"B"`, `"C"`, `"D"`, `"X"`) or `"contraindicated"`. |

---

## Body sections

Required for **all scales**:

- `## Overview` — what is it, why does it matter, principal indications, historical context.
- `## Mechanism` — molecular and cellular mechanism of action. Should be derivable from first principles with sufficient detail to understand cross-links to the Human Atlas.
- `## Clinical Use` — indications, dosing, contraindications, key patient populations.
- `## Evidence` — landmark trials, meta-analyses, guideline citations with specific findings (hazard ratios, NNTs, effect sizes). For traditional/investigational entries: quality of available evidence and its interpretation.
- `## Connections` — narrative summary of cross-links: what human systems it acts on or treats, what pathogens it targets, what other drugs it relates to.

Recommended:

- `## Key Agents` — for drug class entries, a table of individual agents with distinguishing features (selectivity, half-life, renal/hepatic dosing, special populations).
- `## Side Effects` — adverse event profile with mechanisms where known and rates where established.
- `## See Also` — related drug classes or alternative treatments.

---

## Cross-link relations for medicine entries

Medicine entries use these relations in `cross_links`:

| Relation | Direction | Inverse | Meaning |
|:---|:---|:---|:---|
| `treats` | medicine → human entry (organ/system) | `treated-by` | Used as primary or adjunct therapy for disease in this organ/system. |
| `acts-on` | medicine → human entry (any scale) | `target-of` | Pharmacological target — receptor, enzyme, ion channel, transporter, pathway. |
| `modulates` | medicine → human entry | `modulated-by` | Alters the function of this entity (less specific than `acts-on`; used when mechanism is partial or indirect). |
| `treats` | medicine → pathogen entry | `treated-by` | Anti-infective: kills or inhibits the pathogen. |
| `contains-adjuvant` | medicine/vaccine → molecular entry | — | Contains this molecule as an adjuvant or excipient. |

---

## Evidence standards by scale

| `scale` | Evidence expectation |
|:---|:---|
| `01-modern` | Randomized controlled trials, systematic reviews, or clinical practice guidelines preferred. Observational studies explicitly labeled. Every efficacy claim needs a citation. |
| `02-traditional` | Systematic reviews of RCTs if available; ethnobotanical/ethnopharmacological sources; traditional pharmacopoeia references. Absence of high-quality RCTs noted explicitly — not omitted. |
| `03-investigational` | Phase 1/2/3 trial citations; regulatory IND/CTA filings; preprint literature clearly labeled. Mechanism entries (e.g., CRISPR) may rely on foundational molecular biology papers. |

---

## Status lifecycle

| Status | What it means |
|:---|:---|
| `stub` | Folder exists, frontmatter valid, body has at least Overview. Acceptable as a placeholder when needed for cross-linking from a more developed entry. |
| `draft` | All required sections present, source-backed, internally consistent. Not yet independently reviewed. |
| `reviewed` | At least one other contributor has read the entry end-to-end and signed off. Recorded in `contributors`. |
| `expert-validated` | A clinician, pharmacologist, or specialist in this drug class has reviewed and signed off. Named in `contributors` with qualification. |
