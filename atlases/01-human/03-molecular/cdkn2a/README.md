---
schema: human-scale-entry/v1
id: cdkn2a
name: CDKN2A
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "CDKN2A at 9p21 encodes p16/INK4A (CDK4/6 inhibitor → RB1 G1 checkpoint) and p14/ARF (MDM2 inhibitor → p53 stabilization); homozygous deletion in ~50% melanoma, ~60% glioblastoma, ~80% PDAC; germline p16 mutations cause FAMMM; CDK4/6 inhibitors exploit p16 loss."
aliases: ["CDKN2A", "p16", "INK4A", "ARF", "p14ARF", "MTS1", "CDKN2A deletion", "p16 tumor suppressor", "CDK4 inhibitor", "FAMMM syndrome", "ink4a arf locus"]
sources:
  - id: kamb-1994-cdkn2a-p16
    type: peer-reviewed
    cite: "Kamb A, Gruis NA, Weaver-Feldhaus J, et al. A cell cycle regulator potentially involved in genesis of many tumor types. Science. 1994;264(5157):436-440."
    doi: "10.1126/science.7923360"
    pmid: "7923360"
    url: "https://doi.org/10.1126/science.7923360"
  - id: kim-2006-ink4a-arf-review
    type: peer-reviewed
    cite: "Kim WY, Sharpless NE. The regulation of INK4/ARF in cancer and aging. Cell. 2006;127(2):265-275."
    doi: "10.1016/j.cell.2006.10.003"
    pmid: "17055429"
    url: "https://doi.org/10.1016/j.cell.2006.10.003"
cross_links:
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "p16/INK4A inhibits CDK4/CDK6 → RB1 remains hypophosphorylated → E2F repressed → G1 checkpoint; CDKN2A deletion → CDK4/6 hyperactivation → RB1 phosphorylation → E2F release → S-phase entry; CDK4/6 inhibitors restore G1 arrest in CDKN2A-deleted RB1-intact tumors."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p14/ARF (CDKN2A alternative reading frame) binds MDM2 → sequesters MDM2 → prevents MDM2-mediated p53 ubiquitination → p53 stabilized; ARF deletion silences p53 pathway without TP53 mutation; ~80-90% PDAC loses CDKN2A eliminating both p16 and ARF tumor suppression simultaneously."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "CDKN2A p14/ARF sequesters MDM2 → prevents MDM2-mediated p53 ubiquitination → p53 activation; CDKN2A deletion removes ARF → MDM2 free → p53 degradation; MDM2 amplification (~6-8% osteosarcoma, ~10% liposarcoma) and ARF deletion are functionally equivalent de-repression mechanisms."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "p16/INK4A competitive inhibitor of CDK4 and CDK6 → prevents CCND1-CDK4/6 formation → RB1 unphosphorylated → G1 arrest; CDK4 amplification (~6-8% osteosarcoma, ~10% glioblastoma) bypasses p16; palbociclib, ribociclib, abemaciclib exploit CDK4/6 in CDKN2A-deleted tumors."
---

# CDKN2A

## Overview

**CDKN2A** (cyclin-dependent kinase inhibitor 2A) at chromosome **9p21.3** is unique among tumor suppressors in encoding two structurally and functionally unrelated proteins from the same genomic locus via alternative reading frames and separate first exons:

- **p16/INK4A** (exon 1α, 2, 3): 148-amino-acid CDK4/CDK6 inhibitor; G1 checkpoint enforcer; founder of the INK4 family (p15/INK4B, p18/INK4C, p19/INK4D)
- **p14/ARF** (exon 1β, 2, 3; alternative ORF in exon 2): 132-amino-acid nucleolar MDM2 regulator; p53 pathway stabilizer; murine ortholog is p19/ARF

Both proteins are potent tumor suppressors whose loss destabilizes either the RB1 pathway (p16 loss) or the p53 pathway (ARF loss) — and CDKN2A homozygous deletion eliminates both simultaneously, explaining its exceptionally high frequency in human cancers.

**CDKN2A inactivation frequencies:**
- Melanoma: ~50% homozygous deletion, ~10-15% promoter methylation, ~15% point mutations; germline CDKN2A in familial melanoma
- Glioblastoma: ~60% (nearly always homozygous deletion at 9p21 amplicon)
- HNSCC: ~50-60% (often with concurrent deletion of adjacent CDKN2B/p15)
- NSCLC: ~30%; pancreatic ductal adenocarcinoma: ~80-90% (one of 4 driver genes: KRAS, TP53, SMAD4, CDKN2A)
- Bladder carcinoma: ~25%; osteosarcoma: ~20-30%; mesothelioma: ~65-75%

**Germline CDKN2A:**
- Familial atypical multiple mole and melanoma syndrome (FAMMM/FAMMM-PC): lifetime melanoma risk ~76%; pancreatic cancer risk ~17%; autosomal dominant; genetic counseling + surveillance mandatory
- ~25-40% of familial melanoma kindreds carry germline CDKN2A mutations; p.R24P, p.G101W, and p16-Leiden (19-bp deletion) are recurrent European variants

## Structure

### p16/INK4A protein

p16/INK4A folds into a stack of four ankyrin repeats (ANK1-ANK4), each comprising a helix-turn-helix motif:

**CDK4/6 binding interface:**
ANK repeats 2-4 contact the CDK4 N-terminal lobe and hinge region; p16 inserts into the cyclin D1 binding site on CDK4 → competitive displacement of cyclin D1 → CDK4 kinase domain cannot assume the active conformation; p16 binds CDK4 and CDK6 with similar affinity (Kd ~10 nM) but not CDK2 or CDK1 — INK4 specificity is structurally determined by the ANK repeat geometry.

**Key cancer mutations:**
- p.R24P, p.D84N, p.G101W: loss of ANK3-4 packing → CDK4 binding surface disrupted
- Exon 2 missense mutations frequently disrupt p16 AND p14/ARF (shared exon)
- UV-signature C>T transitions at dipyrimidines in melanoma (UV carcinogenesis)

### p14/ARF protein

p14/ARF is a highly basic nucleolar protein with no structural homology to p16:

**MDM2 interaction:**
N-terminal domain (aa 1-45) binds MDM2 central region (aa 210-304) → sequesters MDM2 in the nucleolus; MDM2 cannot ubiquitinate nuclear p53 when tethered in nucleolus → p53 accumulates; ARF also inhibits MDM2 E3 ubiquitin ligase activity directly (independent of sequestration).

**Induction signals:**
ARF is induced by oncogenic RAS, MYC, E2F1, and STAT3 — it is a critical sensor of aberrant mitogenic signaling → ARF→MDM2→p53 axis triggers oncogene-induced senescence (OIS); ARF loss allows MYC-overexpressing or RAS-activated cells to bypass OIS.

### Locus architecture

```
9p21.3: ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
  CDKN2B (p15/INK4B) ← CDKN2A ← CDKN2A
                         exon 1β   exon 1α
                              \      /
                           exon 2 (shared)
                                |
                             exon 3
```

CDKN2B (p15/INK4B) is telomeric to CDKN2A and co-deleted in many cancers; p15 is TGF-β-inducible CDK4/6 inhibitor; co-deletion of p15+p16+ARF in a single event is common in glioblastoma, mesothelioma, and HNSCC.

## Function

### p16 → RB1 pathway

In normal cycling cells:
- Mitogenic signals → CCND1 synthesis → CCND1-CDK4/6 complexes → phosphorylate RB1 at Ser780/Ser795 → E2F1-3 released → transcribe S-phase genes (CCNE1, PCNA, MCM2-7)
- p16 accumulates after ~6 passages (replicative senescence) → suppresses CDK4/6 → RB1 hypophosphorylated → permanent E2F repression → irreversible cell cycle arrest (senescence)

p16 enforces the restriction point: once cells pass G1 restriction point, CDK2-cyclin E takes over → p16 no longer controls S-phase entry. p16 thus governs only the CDK4/6-RB1 G1 checkpoint.

### p14/ARF → p53 pathway

ARF functions as an oncogenic stress sensor:
- Normally absent or very low in quiescent cells
- Induced by: MYC, RAS, E1A, E2F1, cyclin E overexpression, viral oncoproteins
- ARF → MDM2 sequestration → p53 accumulation → cell cycle arrest, apoptosis, or senescence
- ARF-mediated senescence is independent of p16; double-knockout (p16 + ARF) shows additive effects in mouse models

### Oncogene-induced senescence (OIS)

Activated BRAF V600E → MEK/ERK → p16 induction (via ETS2) + ARF induction (via RAS) → p16-RB1 + ARF-p53 dual activation → senescence; BRAF V600E nevi (benign melanocytic lesions) are OIS-arrested cells; CDKN2A/TP53 co-deletion is required for progression to invasive melanoma.

## Mechanism

### CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib)

**Rational basis:**
CDKN2A deletion → CDK4/6 constitutively active → tumors dependent on CDK4/6 for proliferation → CDK4/6 inhibitors selectively suppress these tumors (when RB1 intact); if RB1 is also lost, CDK4/6 inhibition loses efficacy (E2F already released).

**Clinical approvals:**
- Palbociclib (Ibrance): HR+/HER2− breast cancer + letrozole (PALOMA-1/2: PFS 24.8 vs 14.5 months); + fulvestrant (PALOMA-3: PFS 9.5 vs 4.6 months, p<0.0001); FDA 2015
- Ribociclib (Kisqali): HR+/HER2− breast cancer; MONALEESA-2: PFS HR 0.56, OS benefit at 42 months (70.2% vs 46.0%); FDA 2017
- Abemaciclib (Verzenio): single-agent activity in heavily pretreated HR+ BC; FDA 2017; also approved as adjuvant with ET in high-risk early breast cancer (monarchE: IDFS HR 0.664)

**CDKN2A and CDK4/6 inhibitor response:**
- In breast cancer, CDKN2A deletion/methylation does NOT consistently predict CDK4/6 inhibitor benefit (RB1 expression is better predictor)
- In bladder, HNSCC, glioblastoma: CDKN2A-deleted cells enriched for CDK4/6 inhibitor sensitivity in preclinical models; trials ongoing
- Resistance: RB1 loss (20-30% of acquired resistance), CCNE1 amplification, CDK6 amplification, CDKN2A-independent alternative activation

### ARF-MDM2-p53 axis targeting

**MDM2 inhibitors (nutlins, idasanutlin, milademetan):**
Block MDM2-p53 binding → p53 activation; require intact TP53; CDKN2A ARF loss predicts sensitivity (ARF-null tumors rely entirely on MDM2 to suppress p53 → MDM2 inhibitors highly effective); CDKN2A ARF-intact tumors may show compensatory ARF induction when MDM2 is inhibited → ARF acts redundantly with MDM2 inhibitor.

### Promoter methylation

CDKN2A promoter CpG island hypermethylation (epigenetic silencing):
- ~15-30% colorectal cancer; ~50% NSCLC; ~10% acute leukemia; ~30% DLBCL
- EZH2-driven H3K27me3 can initiate CDKN2A silencing; DNMT3A maintains methylation
- Detectable in plasma cfDNA (liquid biopsy marker for early detection); often reversible with HDAC inhibitors or demethylating agents (5-azacytidine) in preclinical models

## Connections

- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — p16/INK4A inhibits CDK4/CDK6 → RB1 remains hypophosphorylated → E2F repressed → G1 checkpoint; CDKN2A deletion → CDK4/6 hyperactivation → RB1 phosphorylation → E2F release → S-phase entry; CDK4/6 inhibitors restore G1 arrest in CDKN2A-deleted RB1-intact tumors.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — p14/ARF (CDKN2A alternative reading frame) binds MDM2 → sequesters MDM2 → prevents MDM2-mediated p53 ubiquitination → p53 stabilized; ARF deletion silences p53 pathway without TP53 mutation; ~80-90% PDAC loses CDKN2A eliminating both p16 and ARF tumor suppression simultaneously.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — CDKN2A p14/ARF sequesters MDM2 → prevents MDM2-mediated p53 ubiquitination → p53 activation; CDKN2A deletion removes ARF → MDM2 free → p53 degradation; MDM2 amplification (~6-8% osteosarcoma, ~10% liposarcoma) and ARF deletion are functionally equivalent de-repression mechanisms.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — p16/INK4A competitive inhibitor of CDK4 and CDK6 → prevents CCND1-CDK4/6 formation → RB1 unphosphorylated → G1 arrest; CDK4 amplification (~6-8% osteosarcoma, ~10% glioblastoma) bypasses p16; palbociclib, ribociclib, abemaciclib exploit CDK4/6 in CDKN2A-deleted tumors.

[^kamb-1994-cdkn2a-p16]: Kamb A, Gruis NA, Weaver-Feldhaus J, et al. A cell cycle regulator potentially involved in genesis of many tumor types. *Science.* 1994;264(5157):436-440. [doi:10.1126/science.7923360](https://doi.org/10.1126/science.7923360) · [PubMed 7923360](https://pubmed.ncbi.nlm.nih.gov/7923360/)
[^kim-2006-ink4a-arf-review]: Kim WY, Sharpless NE. The regulation of INK4/ARF in cancer and aging. *Cell.* 2006;127(2):265-275. [doi:10.1016/j.cell.2006.10.003](https://doi.org/10.1016/j.cell.2006.10.003) · [PubMed 17055429](https://pubmed.ncbi.nlm.nih.gov/17055429/)
