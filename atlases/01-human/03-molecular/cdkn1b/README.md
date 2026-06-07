---
schema: human-scale-entry/v1
id: cdkn1b
name: CDKN1B
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "CDKN1B (p27KIP1) is a CIP/KIP CDK inhibitor that arrests G1/S by inhibiting CDK2-CyclinE and CDK4/6-CyclinD; SCF-SKP2 ubiquitinates phospho-Thr187 p27 for S-phase degradation; germline CDKN1B LOF = MEN4 syndrome; cytoplasmic p27 paradoxically promotes migration."
aliases: ["CDKN1B", "p27KIP1", "p27", "KIP1", "CDKN1B tumor suppressor", "p27 CDK inhibitor", "CDKN1B MEN4", "p27KIP1 cell cycle", "SKP2 p27"]
sources:
  - id: polyak-1994-p27-cell-cycle
    type: peer-reviewed
    cite: "Polyak K, Lee MH, Erdjument-Bromage H, et al. Cloning of p27Kip1, a cyclin-dependent kinase inhibitor and a potential mediator of extracellular antimitogenic signals. Cell. 1994;78(1):59-66."
    doi: "10.1016/0092-8674(94)90572-X"
    pmid: "8033212"
    url: "https://doi.org/10.1016/0092-8674(94)90572-X"
  - id: pellegata-2006-cdkn1b-men4
    type: peer-reviewed
    cite: "Pellegata NS, Quintanilla-Martinez L, Siggelkow H, et al. Germ-line mutations in p27Kip1 cause a multiple endocrine neoplasia syndrome in rats and humans. Proc Natl Acad Sci USA. 2006;103(42):15558-15563."
    doi: "10.1073/pnas.0603306103"
    pmid: "17030811"
    url: "https://doi.org/10.1073/pnas.0603306103"
cross_links:
  - target: 01-human/03-molecular/men1
    relation: connects-to
    note: "Menin (MEN1) scaffold controls H3K4me3 at the CDKN1B locus: MEN1 LOF → reduced CDKN1B expression → CDK2 derepressed → neuroendocrine proliferation; both MEN1 and CDKN1B are tumor suppressors in pituitary/parathyroid/pNET context but via different molecular mechanisms."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "CDKN1B (p27KIP1) and CDKN1A (p21WAF1) are both CIP/KIP CDK inhibitors targeting CDK2-CyclinE; p21 is primarily p53-transcribed and mediates DNA damage arrest; p27 is primarily regulated by proteolysis (SCF-SKP2) at G1/S; both control cell cycle entry and senescence."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "MEN1 and MEN4 share similar tumor spectra (pituitary, parathyroid, pancreatic NETs); MEN1 is caused by menin LOF (epigenetic scaffold), MEN4 by CDKN1B LOF (CDK2 inhibitor); MEN4 is rarer (~1/100 of MEN1 prevalence); screening: test CDKN1B in MEN1-negative MEN families."
  - target: 01-human/07-system/men4-syndrome
    relation: connects-to
    note: "Germline CDKN1B LOF causes MEN4 via CDK2-CyclinE derepression → neuroendocrine proliferation; pituitary adenomas (all types), parathyroid hyperplasia, pancreatic NETs; CDKN1B sequencing recommended in MEN1-negative MEN families; WHO 2022 formally recognizes MEN4."
---

# CDKN1B

## Overview

**CDKN1B** (Cyclin-Dependent Kinase Inhibitor 1B; also **p27KIP1** — 27 kDa Kinase Inhibitory Protein 1) is a 198 amino acid (27 kDa) **CIP/KIP family CDK inhibitor** that regulates progression through the **G1/S cell cycle transition** by inhibiting CDK2-CyclinE, CDK2-CyclinA, and CDK4/6-CyclinD complexes. p27KIP1 was identified as a TGF-β and contact inhibition mediator by Polyak et al. in 1994. Unlike p21 (CDKN1A), which is primarily regulated at the transcriptional level by p53 in response to DNA damage, **p27 is regulated primarily post-translationally** — its nuclear levels are controlled by SCF-SKP2 (S-Phase Kinase-associated Protein 2) E3 ubiquitin ligase-mediated proteolysis at the G1/S transition. Germline loss-of-function CDKN1B mutations cause **Multiple Endocrine Neoplasia type 4 (MEN4)**, a syndrome with overlapping tumor spectrum to MEN1 but driven by CDK inhibitor LOF rather than epigenetic scaffold dysfunction [^polyak-1994-p27-cell-cycle] [^pellegata-2006-cdkn1b-men4].

**CIP/KIP family CDK inhibitors — comparison:**

| Protein | Gene | Molecular weight | Primary CDK targets | Primary regulation | Germline syndrome |
|---|---|---|---|---|---|
| p21 (WAF1/CIP1) | CDKN1A | 21 kDa | CDK2-E, CDK2-A, CDK4-D | p53 transcriptional target | Li-Fraumeni modifier |
| p27 (KIP1) | CDKN1B | 27 kDa | CDK2-E, CDK2-A, CDK4/6-D | SCF-SKP2 proteolysis | MEN4 |
| p57 (KIP2) | CDKN1C | 57 kDa | CDK2-E, CDK4-D | Imprinting (BWS/RSS) | Beckwith-Wiedemann |

## Structure

### CDKN1B protein domains

**CDK inhibitory domain (CID; aa 28-96):**
- Intrinsically disordered in isolation; folds upon CDK2-CyclinE binding
- Two-site binding mechanism: N-terminal half contacts CyclinE (RRLFG motif at aa 28-37); C-terminal half contacts CDK2 active site (contacts catalytic Asp127 and Asp145 of CDK2, blocking substrate access)
- The CID is shared with p21 and p57; conserved across CIP/KIP family; occupies the CDK2 substrate-binding groove → inhibits substrate phosphorylation by steric exclusion + direct active site occlusion
- For CDK4/6: p27 binds CDK4/6 via a distinct mechanism involving the D-helix of the CID contacting the activation loop of CDK4/6 (less potent inhibition than for CDK2)

**Nuclear localization signals (NLS; two signals: aa 100-126 and aa 152-176):**
- Classical bipartite NLS recognized by importin-α/β
- In quiescent cells: p27 nuclear (high nuclear p27 = cell cycle arrest)
- In proliferating cells: p27 phosphorylated at Thr187 by CDK2-CyclinE (self-catalytic: CDK2 activity first begins with residual p27-free CDK2 → phosphorylates p27 → p27 degraded → CDK2 fully active → irreversible S-phase commitment)

**Thr187 phosphodegron (aa 184-189):**
- CDK2-CyclinE phosphorylates p27 at **Thr187** → creates a phosphodegron (T187-P-V-K = minimal SCF-SKP2 recognition motif)
- **SCF-SKP2 E3 ligase**: SKP1-CUL1-F-box (SKP2) + CKS1 (accessory) → recognizes pThr187-p27 → K48-linked polyubiquitination → proteasomal degradation
- CKS1 (CDK subunit 1): adaptor that directly contacts pThr187-p27 and positions p27 in the SCF-SKP2 active site; CKS1 is required for efficient p27 degradation; SKP2 alone has low affinity for p27 without CKS1

**C-terminal domain (CTD; aa 140-198):**
- Contains a nuclear export signal (NES; aa 163-170): mediates CRM1-dependent nuclear export; regulated by phosphorylation at Ser10 and Thr157 (AKT-mediated) and Thr198 (AMPK-mediated)
- **Cytoplasmic p27**: when exported from nucleus (by AKT phosphorylation of T157 → masks NLS; or Ser10 phosphorylation → CRM1 export enhanced) → p27 binds RhoA-GEF complex → inhibits RhoA → promotes lamellipodia → cell migration
- This cytoplasmic p27 function is **paradoxically pro-tumorigenic**: breast cancer and other cancers with cytoplasmic p27 have increased invasive behavior; represents a gain-of-function from nuclear-to-cytoplasmic redistribution

## Function

### CDKN1B as cell cycle brake at G1/S

**Quiescence (G0) → cell cycle entry:**
1. Mitogen withdrawal or TGF-β → p27 gene transcription maintained (FOXO3-driven) → nuclear p27 accumulates → CDK2-CyclinE inhibited → Rb hypo-phosphorylated → E2F1 sequestered → S-phase genes not activated → G1 arrest or quiescence
2. Mitogen stimulation → PI3K-AKT → FOXO3 nuclear export (reduces p27 transcription) + AKT phosphorylates p27 Thr157/Thr198 → cytoplasmic p27 → reduced nuclear CDK inhibition + CDK2-CyclinE activity rises → pThr187-p27 → SKP2-CKS1 ubiquitination → p27 degradation → irreversible S-phase commitment

**CDK2-CyclinE activation cascade (restriction point commitment):**
- Late G1: CDK4/6-CyclinD → partial Rb phosphorylation → partial E2F1 release → CyclinE upregulation → CDK2-CyclinE → further Rb phosphorylation → full E2F1 release → S-phase gene program (DNA polymerase δ, MCM2-7, PCNA)
- p27 is the critical brake at this transition: when p27 is high (quiescent cells), CDK2-CyclinE is inhibited → no Rb hyperphosphorylation; when p27 falls (CDK2 accumulates → pThr187 → proteasomal) → CDK2 fully active → S-phase entry

**Mitogens and p27 regulation:**
- EGF/HER2: PI3K-AKT → phospho-FOXO3 → reduced p27 transcription + cytoplasmic p27 redistribution → CDK2 derepressed; HER2-amplified breast cancer has very low nuclear p27 via this mechanism
- TGF-β (anti-proliferative context): SMAD2/3 → CDKN1B transcriptional upregulation → p27 accumulates → G1 arrest; this is a tumor suppressor mechanism that is lost in many cancers (despite intact CDKN1B gene, TGF-β anti-proliferative response is broken)
- Contact inhibition: E-cadherin-mediated → RhoA → p27 nuclear retention + reduced SKP2 expression → p27 accumulates → growth arrest

### CDKN1B in neuroendocrine tumors

Low nuclear p27 expression is a well-established biomarker in:
- **Pancreatic neuroendocrine tumors (pNET)**: nuclear p27 loss correlates with aggressive behavior, higher Ki-67 index; predicts worse PFS with somatostatin analog therapy
- **Pituitary adenomas**: p27 IHC loss in aggressive adenomas; predicts higher recurrence
- **Parathyroid carcinoma**: p27 LOH at 12p13 (CDKN1B locus) detected in some parathyroid carcinomas; reduced p27 IHC correlates with malignancy

## Mechanism

### Germline CDKN1B and MEN4

**Discovery of CDKN1B as a MEN gene:**
Pellegata et al. (2006) identified homozygous p27 mutations in the MENX rat model (multiple endocrine neoplasia-like tumors in rats) and found heterozygous CDKN1B mutations in human MEN1-negative multiple endocrine neoplasia patients → establishing MEN4 as a distinct clinical entity. WHO 2022 Classification of Endocrine Tumors formally recognized MEN4 as a separate entity.

**CDKN1B germline variant spectrum:**
- Frameshift and nonsense (most common): ~55%
- Missense in the CID domain (impairing CDK2 binding): ~25%
- Splice site: ~10%
- 5'UTR variants disrupting translation initiation or Kozak context: ~10%
- Most are heterozygous LOF → haploinsufficiency mechanism (p27 dosage matters; complete homozygous LOF is embryonic lethal in mice)

**Somatic CDKN1B in sporadic cancers:**
- Unlike CDKN2A (p16) or TP53, CDKN1B somatic mutations are rare (<5% of most solid tumors)
- p27 downregulation in cancer is primarily via: (1) SKP2 overexpression (ubiquitous in cancer, driven by β-catenin, MYC, etc. → enhanced p27 degradation); (2) AKT-mediated cytoplasmic redistribution; (3) reduced transcription (FOXO3 nuclear export in high-PI3K tumors)
- **SKP2 as oncogene**: SKP2 overexpression is functionally equivalent to CDKN1B LOF in cancer; SKP2 amplification at 5p13 detected in NSCLC, prostate, colorectal; SKP2 inhibitors are in preclinical development

**CDK inhibition and p27 pharmacology:**
CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) re-activate p27 function indirectly:
- CDK4/6 inhibition → Rb remains hypo-phosphorylated → E2F1 sequestered → CCNE1/CDK2 not upregulated → reduced pThr187-p27 → reduced SKP2-mediated degradation → net p27 accumulation → reinforced G1 arrest
- p27-low tumors (high SKP2, AKT-active): may be more resistant to CDK4/6 inhibitors (CDK2-CyclinE bypass); combination CDK2+CDK4/6 inhibition is under investigation

## Connections

- `connects-to` → **[MEN1](../../03-molecular/men1/README.md)** — Menin (MEN1) scaffold controls H3K4me3 at the CDKN1B locus: MEN1 LOF → reduced CDKN1B expression → CDK2 derepressed → neuroendocrine proliferation; both MEN1 and CDKN1B are tumor suppressors in pituitary/parathyroid/pNET context but via different molecular mechanisms.
- `connects-to` → **[CDKN1A](../../03-molecular/cdkn1a/README.md)** — CDKN1B (p27KIP1) and CDKN1A (p21WAF1) are both CIP/KIP CDK inhibitors targeting CDK2-CyclinE; p21 is primarily p53-transcribed and mediates DNA damage arrest; p27 is primarily regulated by proteolysis (SCF-SKP2) at G1/S; both control cell cycle entry and senescence.
- `connects-to` → **[MEN1 Syndrome](../../07-system/men1-syndrome/README.md)** — MEN1 and MEN4 share similar tumor spectra (pituitary, parathyroid, pancreatic NETs); MEN1 is caused by menin LOF (epigenetic scaffold), MEN4 by CDKN1B LOF (CDK2 inhibitor); MEN4 is rarer (~1/100 of MEN1 prevalence); screening: test CDKN1B in MEN1-negative MEN families.
- `connects-to` → **[MEN4 Syndrome](../../07-system/men4-syndrome/README.md)** — Germline CDKN1B LOF causes MEN4 via CDK2-CyclinE derepression → neuroendocrine proliferation; pituitary adenomas (all types), parathyroid hyperplasia, pancreatic NETs; CDKN1B sequencing recommended in MEN1-negative MEN families; WHO 2022 formally recognizes MEN4.

[^polyak-1994-p27-cell-cycle]: Polyak K, Lee MH, Erdjument-Bromage H, et al. Cloning of p27Kip1, a cyclin-dependent kinase inhibitor and a potential mediator of extracellular antimitogenic signals. *Cell.* 1994;78(1):59-66. [doi:10.1016/0092-8674(94)90572-X](https://doi.org/10.1016/0092-8674(94)90572-X) · [PubMed 8033212](https://pubmed.ncbi.nlm.nih.gov/8033212/)
[^pellegata-2006-cdkn1b-men4]: Pellegata NS, Quintanilla-Martinez L, Siggelkow H, et al. Germ-line mutations in p27Kip1 cause a multiple endocrine neoplasia syndrome in rats and humans. *Proc Natl Acad Sci USA.* 2006;103(42):15558-15563. [doi:10.1073/pnas.0603306103](https://doi.org/10.1073/pnas.0603306103) · [PubMed 17030811](https://pubmed.ncbi.nlm.nih.gov/17030811/)
