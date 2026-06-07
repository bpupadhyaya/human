---
schema: human-scale-entry/v1
id: dll3
name: DLL3
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "DLL3 (Delta-like ligand 3) is an inhibitory Notch ligand overexpressed in >80% of SCLC and neuroendocrine carcinomas; DLL3 cis-inhibits Notch1/2 on tumor cells; tarlatamab (DLL3×CD3 bispecific antibody, FDA 2024) is approved for relapsed/refractory SCLC."
aliases: ["DLL3", "Delta-like ligand 3", "DLL3 SCLC", "tarlatamab target", "DLL3 bispecific", "neuroendocrine DLL3", "DLL3 ADC", "rovalpituzumab target"]
sources:
  - id: rudin-2017-rovalpituzumab
    type: peer-reviewed
    cite: "Rudin CM, Pietanza MC, Bauer TM, et al. Rovalpituzumab tesirine, a DLL3-targeted antibody-drug conjugate, in recurrent small-cell lung cancer: a first-in-human, first-in-class, open-label, phase 1 study. Lancet Oncol. 2017;18(1):42-51."
    doi: "10.1016/S1470-2045(16)30565-4"
    pmid: "27932068"
    url: "https://doi.org/10.1016/S1470-2045(16)30565-4"
  - id: ahn-2023-tarlatamab
    type: peer-reviewed
    cite: "Ahn MJ, Cho BC, Felip E, et al. Tarlatamab for patients with previously treated small-cell lung cancer. N Engl J Med. 2023;389(22):2063-2075."
    doi: "10.1056/NEJMoa2307980"
    pmid: "37870964"
    url: "https://doi.org/10.1056/NEJMoa2307980"
cross_links:
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "DLL3 is an inhibitory Notch ligand that cis-inhibits Notch1/2 on SCLC cells, preventing trans-activation; in normal lung, Notch suppresses neuroendocrine differentiation; RB1 loss in SCLC → ASCL1 → DLL3 upregulation → Notch suppression → neuroendocrine fate."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 biallelic loss (>90% of SCLC) releases E2F transcription factors → ASCL1 expression → DLL3 transcription; DLL3 overexpression is a downstream consequence of the RB1/ASCL1 axis; DLL3 IHC positivity correlates with ASCL1-high SCLC subtype."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 biallelic mutation co-occurs with RB1 loss in >90% of SCLC → together enabling rapid proliferation and neuroendocrine differentiation (DLL3 overexpression); DLL3+ SCLC retains TP53 loss; platinum/etoposide sensitivity in SCLC is partly due to p53-null apoptotic priming."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "DLL3 overexpression marks high-grade neuroendocrine carcinomas (SCLC, Merkel cell, extrapulmonary NEC); SSTR2 marks well-differentiated NETs (carcinoids, pNET); DLL3 and SSTR2 are complementary biomarkers separating high-grade NEC from low-grade NET."
---

# DLL3

## Overview

**DLL3 (Delta-like Ligand 3)** is an atypical member of the DSL (Delta/Serrate/LAG-2) family of Notch pathway ligands that, unlike classical trans-activating Notch ligands (DLL1, DLL4, JAG1/2), acts as a **cis-inhibitor** of Notch1 and Notch2 signaling on the surface of the same cell. In normal development, DLL3 is expressed transiently during somitogenesis (segmenting the paraxial mesoderm into somites) — germline DLL3 mutations cause **spondylocostal dysostosis (Jarcho-Levin syndrome)**, characterized by vertebral segmentation defects. In most adult tissues, DLL3 expression is very low. However, in **high-grade neuroendocrine carcinomas** — most prominently **small cell lung cancer (SCLC)** — DLL3 is dramatically re-expressed on the tumor cell surface (>80% of SCLC, driven by ASCL1 transcription downstream of RB1 loss), making it an ideal tumor-specific surface target. The high surface expression and restricted normal-tissue expression of DLL3 have made it a compelling therapeutic target, culminating in the FDA approval (May 2024) of **tarlatamab**, a bispecific DLL3×CD3 T-cell engager, for previously treated SCLC [^ahn-2023-tarlatamab] [^rudin-2017-rovalpituzumab].

**DLL3 expression across tumor types:**
- **SCLC:** DLL3+ in ~80-85% of SCLC; particularly high in ASCL1-high subtype (SCLC-A); robust surface expression across primary and metastatic sites (brain mets included)
- **Large cell neuroendocrine carcinoma (LCNEC):** DLL3+ in ~50-70%; distinct from SCLC by large cell morphology but similarly aggressive NEC; tarlatamab and PRRT under investigation
- **Merkel cell carcinoma:** DLL3+ in ~60-70%; high-grade cutaneous NEC; avelumab/pembrolizumab approved; DLL3-targeting investigational
- **Extrapulmonary SCLC (GI, bladder, prostate NEC):** DLL3+ in ~60-80%; similar biology to pulmonary SCLC; platinum/etoposide treatment extrapolated
- **Neuroendocrine prostate cancer (NEPC):** DLL3+ in ~70-80%; transdifferentiation from adenocarcinoma under ARi pressure; aggressive; platinum/etoposide; cabazitaxel
- **Glioblastoma:** DLL3 expression in ~90% of GBM stem cells; AMG757 (DLL3×CD3 bispecific for GBM) in Phase 1 trials

## Structure

### DLL3 protein architecture

DLL3 is a 618-amino-acid type I transmembrane protein:

**Signal peptide (1-27):** N-terminal secretory signal → ER targeting

**Extracellular domain (ECD, 27-564):**
- **DSL domain (Delta/Serrate/LAG-2 domain):** The canonical Notch ligand-binding module; DLL3 DSL domain contains critical substitutions compared to DLL1/DLL4 that impair trans-Notch binding → DLL3 cannot efficiently engage Notch receptors on adjacent cells (trans-activation) → pure cis-inhibitor
- **EGF-like repeats (EGF 1-6):** Six epidermal growth factor-like repeats; DLL3 has only 6 EGF repeats vs. 8 in DLL1/DLL4 → missing EGF7/8 which are required for high-affinity trans-Notch binding; further explanation for cis-only activity
- **N-linked glycosylation sites:** DLL3 ECD is heavily glycosylated → immunogen for ADC and bispecific antibody targeting; glycosylation does not impair antibody binding for AMG 757 (tarlatamab) or rovalpituzumab

**Transmembrane domain (TM, 564-584):** Single-pass helix

**Intracellular domain (ICD, 585-618):**
- Very short (34 aa) C-terminal cytoplasmic tail; DLL3 ICD lacks the PDZ-binding motif and E3 ubiquitin ligase interaction sequences found in DLL1/DLL4 → DLL3 does not undergo Neur/Mindbomb-mediated ubiquitination → limited endocytosis-driven activation; DLL3 accumulates on cell surface and in trans-Golgi/endosomal compartments rather than plasma membrane-recycling → primarily intracellular in normal cells, primarily surface in SCLC

### DLL3 as cis-Notch inhibitor

**Normal Notch trans-activation (DLL1/DLL4):**
Ligand cell: DLL1 surface expression → Notch receptor on adjacent signal-receiving cell → DSL-EGF binding → Notch proteolytic cleavage (ADAM10/TACE + γ-secretase) → NICD (Notch intracellular domain) release → nuclear translocation → RBPJ/CSL co-activator → HES1/HEY1 target genes → cell fate specification.

**DLL3 cis-inhibition:**
DLL3 expressed on same cell as Notch receptor → DLL3 DSL domain binds Notch1/2 in cis configuration → sequesters Notch away from productive trans-activation by neighboring DLL1/DLL4 → Notch signaling reduced → promotes neuroendocrine fate (Notch normally suppresses neuroendocrine identity in lung progenitors). In SCLC: RB1 loss → ASCL1 expression → DLL3 transcription → DLL3 surface expression → cis-Notch inhibition → sustained neuroendocrine program → SCLC phenotype.

### DLL3-targeting therapeutics

**Rovalpituzumab tesirine (Rova-T, ADC):** [^rudin-2017-rovalpituzumab]
DLL3-targeted antibody (SC16) conjugated to a PBD (pyrrolobenzodiazepine) dimer toxin via a protease-cleavable linker; DAR 2; ADC binds DLL3 → internalizes → lysosomal cleavage → PBD released → DNA crosslinking → apoptosis; Phase 1: ORR 39% in DLL3+ SCLC; BUT Phase 3 (TAHOE: 3rd-line, MERU: maintenance) showed worse OS vs. topotecan → FDA did not approve; PBD toxicity profile (pleural effusion, photosensitivity) contributed to discontinuation.

**Tarlatamab (AMG 757, bispecific DLL3×CD3 T-cell engager):** [^ahn-2023-tarlatamab]
Half-life extended (HLE) BiTE molecule: one arm binds DLL3 (SC16-derived) + second arm binds CD3ε on T-cells → brings T-cells to DLL3+ SCLC cells → T-cell activation → granzyme B/perforin-mediated SCLC killing. Phase 2 (DeLLphi-301): 100 mg cohort in R/R SCLC ≥2 prior lines: ORR 40%; mDOR 9.7 months; mPFS 4.9 months; intracranial response in 52% of patients with brain mets; FDA granted accelerated approval May 2024. Key toxicities: cytokine release syndrome (CRS, ~51% any grade, ~1% grade 3-4), immune effector cell-associated neurotoxicity syndrome (ICANS, ~13%), fatigue. CRS management: premedication (dexamethasone), tocilizumab for grade ≥2; step-dosing (10 mg cycle 1 → 100 mg maintenance) reduces CRS incidence.

**Next-generation DLL3 approaches:**
- AMG 119 (DLL3-CAR-T, autologous): Phase 1 for SCLC (CNS penetration); adoptive T-cell therapy
- DLL3-targeted PRRT (DLL3-PSMA dual-targeting): Under investigation for high-grade NECs
- Cediranib + tarlatamab: Antiangiogenic + BiTE combination

## Function

### DLL3 in neuroendocrine cell identity

**Normal neuroendocrine differentiation:**
In the developing lung, ASCL1 (achaete-scute homolog 1, MASH1) drives pulmonary neuroendocrine cell (PNEC) fate; Notch1/2 counter-regulate ASCL1 to limit neuroendocrine cell numbers (HES1 → ASCL1 repression); DLL3 acts downstream of ASCL1 to cis-inhibit Notch → creates a positive feedback: ASCL1 → DLL3 → Notch inhibition → sustained ASCL1 expression → maintained PNEC identity. This ASCL1-DLL3-Notch circuit is the molecular basis of the SCLC-A (ASCL1-high) subtype.

**SCLC molecular subtypes (Rudin 2019 classification):**
- SCLC-A (ASCL1-high, ~70%): DLL3+, synaptophysin/chromogranin high, Notch-low; most responsive to tarlatamab; classic SCLC chemosensitive
- SCLC-N (NEUROD1-high, ~18%): DLL3 intermediate, less neuroendocrine; may respond to tarlatamab
- SCLC-P (POU2F3-high, tuft cell, ~10%): DLL3 variable; distinct molecular program
- SCLC-Y (YAP1-high, ~2%): DLL3 low; non-neuroendocrine; poor response to tarlatamab

## Mechanism

### Tarlatamab mechanism of action and resistance

**BiTE-mediated T-cell engagement:**
Tarlatamab bridges DLL3+ SCLC cells and CD3+ T-cells → immunological synapse formation → T-cell activation (independent of MHC-peptide recognition) → perforin/granzyme B secretion → SCLC apoptosis; T-cell engagers do not require pre-existing tumor antigen-specific T-cells; activity in immunosuppressed microenvironments can be limited by T-cell exhaustion.

**Mechanisms of resistance (emerging data):**
- DLL3 downregulation: SCLC phenotypic plasticity (SCLC-A → SCLC-Y transition) → DLL3 loss → tarlatamab resistance
- T-cell exhaustion: Chronic T-cell activation by BiTE → PD-1/TIM-3/LAG-3 upregulation → T-cell dysfunction; combination with PD-1 inhibitor under investigation
- Antigen escape: Heterogeneous DLL3 expression within tumor → DLL3-negative clone expansion
- Regulatory T-cell infiltration: Immunosuppressive TME → BiTE activity blunted

**DLL3 IHC scoring for patient selection:**
Currently tarlatamab approval is not restricted by DLL3 IHC threshold (approval is in unselected SCLC R/R ≥2 lines); DLL3+ (≥1% of cells by IHC) in ~80% of SCLC → broad applicability; DLL3-negative SCLC has lower ORR (~10%) vs. DLL3+ (ORR ~45%). DOTATATE PET low in SCLC (high-grade, low SSTR2) → DLL3 IHC/FISH not routinely required for tarlatamab selection per current label but may guide future treatment algorithms.

## Connections

- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — DLL3 is an inhibitory Notch ligand that cis-inhibits Notch1/2 on SCLC cells, preventing trans-activation; in normal lung, Notch suppresses neuroendocrine differentiation; RB1 loss in SCLC → ASCL1 → DLL3 upregulation → Notch suppression → neuroendocrine fate.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 biallelic loss (>90% of SCLC) releases E2F transcription factors → ASCL1 expression → DLL3 transcription; DLL3 overexpression is a downstream consequence of the RB1/ASCL1 axis; DLL3 IHC positivity correlates with ASCL1-high SCLC subtype.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 biallelic mutation co-occurs with RB1 loss in >90% of SCLC → together enabling rapid proliferation and neuroendocrine differentiation (DLL3 overexpression); DLL3+ SCLC retains TP53 loss; platinum/etoposide sensitivity in SCLC is partly due to p53-null apoptotic priming.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — DLL3 overexpression marks high-grade neuroendocrine carcinomas (SCLC, Merkel cell, extrapulmonary NEC); SSTR2 marks well-differentiated NETs (carcinoids, pNET); DLL3 and SSTR2 are complementary biomarkers separating high-grade NEC from low-grade NET.

[^rudin-2017-rovalpituzumab]: Rudin CM, Pietanza MC, Bauer TM, et al. Rovalpituzumab tesirine, a DLL3-targeted antibody-drug conjugate, in recurrent small-cell lung cancer: a first-in-human, first-in-class, open-label, phase 1 study. *Lancet Oncol.* 2017;18(1):42-51. [doi:10.1016/S1470-2045(16)30565-4](https://doi.org/10.1016/S1470-2045(16)30565-4) · [PubMed 27932068](https://pubmed.ncbi.nlm.nih.gov/27932068/)
[^ahn-2023-tarlatamab]: Ahn MJ, Cho BC, Felip E, et al. Tarlatamab for patients with previously treated small-cell lung cancer. *N Engl J Med.* 2023;389(22):2063-2075. [doi:10.1056/NEJMoa2307980](https://doi.org/10.1056/NEJMoa2307980) · [PubMed 37870964](https://pubmed.ncbi.nlm.nih.gov/37870964/)
