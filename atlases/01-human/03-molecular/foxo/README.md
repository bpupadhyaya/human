---
schema: human-scale-entry/v1
id: foxo
name: FOXO
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Transcription factors (FOXO1/3/4) integrating PI3K-AKT, mTOR, and oxidative stress with cell cycle arrest and longevity; AKT phosphorylation → FOXO nuclear exclusion → loss of p21, BIM, PUMA. PI3K inhibition → FOXO re-activation → tumor suppression and longevity programs."
aliases: ["FOXO1", "FOXO3", "FOXO4", "FOXO6", "forkhead box O", "DAF-16", "FKHR", "FKHRL1", "AFX", "MLLT7"]
sources:
  - id: brunet-1999-foxo-akt
    type: peer-reviewed
    cite: "Brunet A, Bonni A, Zigmond MJ, et al. Akt promotes cell survival by phosphorylating and inhibiting a Forkhead transcription factor. Cell. 1999;96(6):857-868."
    doi: "10.1016/S0092-8674(00)80595-4"
    pmid: "10102273"
    url: "https://doi.org/10.1016/S0092-8674(00)80595-4"
  - id: calnan-2008-foxo-review
    type: peer-reviewed
    cite: "Calnan DR, Brunet A. The FoxO code. Oncogene. 2008;27(16):2276-2288."
    doi: "10.1038/onc.2008.21"
    pmid: "18391970"
    url: "https://doi.org/10.1038/onc.2008.21"
  - id: eijkelenboom-2013-foxo-cancer
    type: peer-reviewed
    cite: "Eijkelenboom A, Burgering BM. FOXOs: signalling integrators for homeostasis maintenance. Nat Rev Mol Cell Biol. 2013;14(2):83-97."
    doi: "10.1038/nrm3507"
    pmid: "23325358"
    url: "https://doi.org/10.1038/nrm3507"
cross_links:
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "AKT is the primary FOXO kinase: AKT phosphorylates FOXO1 Thr24/Ser256, FOXO3 Thr32/Ser253 → 14-3-3 binding → nuclear exclusion → loss of p21, BIM, PUMA, catalase; PTEN loss → constitutive AKT → constitutive FOXO cytoplasmic sequestration → oncogenic survival in cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "FOXO3 and p53 co-activate overlapping programs (PUMA, p21, BIM, GADD45) → apoptosis and arrest; FOXO3 competes with MDM2 for p53 binding → p53 stabilization; combined FOXO + p53 inactivation is required for full oncogenic transformation downstream of PI3K-RAS."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTORC1 suppresses FOXO via S6K → IRS-1 degradation → reduced AKT → partial FOXO nuclear entry (negative feedback); mTORC2 phosphorylates AKT Ser473 → FOXO phosphorylation; mTOR inhibitors → FOXO re-activation → cell cycle arrest and partial tumor suppression."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Insulin → IRS-1/2 → PI3K → AKT → FOXO1 phosphorylation → nuclear exclusion → glucose homeostasis; hepatic FOXO1 drives PEPCK/G6Pase → gluconeogenesis; FOXO1 deregulation contributes to fasting hyperglycemia in type 2 diabetes; GLP-1 agonists suppress FOXO1 via AKT."
---

# FOXO

## Overview

**FOXO transcription factors (Forkhead box class O)** are **evolutionarily conserved longevity regulators and tumor suppressors** that serve as integration nodes for **insulin/PI3K-AKT, mTOR, AMPK, and oxidative stress signals** — coupling nutrient sensing with cell cycle arrest, apoptosis, stress resistance, and longevity programs [^brunet-1999-foxo-akt]. In mammals there are four FOXO family members: **FOXO1 (FKHR), FOXO3 (FKHRL1), FOXO4 (AFX), and FOXO6** — the mammalian homologs of DAF-16 (C. elegans), the founding member whose gain-of-function extends C. elegans lifespan dramatically when insulin/IGF-1 signaling is reduced.

**FOXO as a tumor suppressor:**
- FOXO proteins are functionally inactivated in >50% of human cancers via PI3K-AKT pathway activation (PIK3CA mutation, PTEN loss, RTK amplification)
- Unlike conventional tumor suppressors, FOXO genes themselves are rarely mutated — instead, they are silenced post-translationally through AKT-mediated nuclear exclusion
- **Exception: FOXO1/3/4 fusion oncogenes** — in alveolar rhabdomyosarcoma, FOXO1 is fused to PAX3 or PAX7 via t(2;13) or t(1;13) chromosomal translocations → PAX3-FOXO1 gain-of-function chimeric transcription factor → constitutive nuclear FOXO1 activity in an oncogenic context (paradoxically, FOXO1 fused to PAX3 drives proliferation rather than arrest)

**FOXO in aging and longevity:**
- **C. elegans daf-16 (FOXO homolog):** daf-2 (IGF-1R) mutants with nuclear FOXO/DAF-16 → 2-3× lifespan extension; stress resistance and fat storage programs
- **Human FOXO3 variants:** GWAS studies consistently identify FOXO3 polymorphisms associated with exceptional human longevity (centenarians); rs2802292 variant (intronic FOXO3) associated with longevity in Hawaiian, European, German, Italian, and Chinese cohorts
- **Mechanism:** Low insulin/IGF-1 → reduced AKT → FOXO nuclear → SOD2, catalase, GADD45 → ROS detoxification → reduced cellular aging; this pathway is conserved from yeast (Rim15/Gis1) through C. elegans (daf-2/daf-16) to mammals

## Structure

### FOXO protein architecture and regulation [^calnan-2008-foxo-review]

**Forkhead domain (DBD, DNA-binding domain):**
- ~110 aa winged-helix domain → binds **FHRE (Forkhead response element):** 5'-GTAAACAA-3' (consensus); also extended binding motifs (TGTTTTK) — "DBE" (DAF-16/FOXO binding element); DNA binding is inhibited by AKT phosphorylation near the DBD (Ser256 in FOXO1 within the DBD → disrupts DNA contacts)

**AKT phosphorylation sites — the main FOXO regulatory switch:**
- **FOXO1:** Thr24 (N-terminal → 14-3-3 docking site 1), Ser256 (DBD → reduces DNA binding), Ser319 (C-terminal → nuclear export signal activation → CRM1/exportin-dependent nuclear export)
- **FOXO3a:** Thr32, Ser253, Ser315 — same pattern; doubly phosphorylated FOXO3a = cytoplasmic and inactive
- **14-3-3 binding:** Both phospho-Thr24/Thr32 and phospho-Ser256/Ser253 → 14-3-3 protein dimer → FOXO cytoplasmic sequestration; FOXO is also polyubiquitinated by MDM2, SKP2, and IKK when phosphorylated → proteasomal degradation

**Additional post-translational regulation:**
- **AMPK:** Phosphorylates FOXO3a Thr179/Ser399/Ser413/Ser555/Ser588/Ser626 → nuclear localization and activity → stress-induced FOXO activation (glucose starvation → AMPK → FOXO → p27, MnSOD)
- **JNK:** Phosphorylates FOXO4 Thr447/Thr451 → nuclear translocation; activated by oxidative stress → FOXO-dependent ROS response (GADD45, SOD2)
- **SIRT1 (sirtuin deacetylase):** Deacetylates FOXO → shifts FOXO activity from apoptosis to stress resistance (GADD45 > BIM induction); SIRT1-FOXO axis = central caloric restriction/longevity mechanism
- **CBP/p300 acetylation:** Acetylates FOXO → reduces DNA binding affinity → post-translational repression; balanced by SIRT1/SIRT2 deacetylation
- **Monoubiquitination (USP7/HAUSP):** Stabilizes nuclear FOXO; similar to PTEN monoubiquitination

**FOXO target genes (context-dependent):**
- **Cell cycle arrest:** p21/CDKN1A, p27/CDKN1B, p15/CDKN2B → CDK2/CDK4 inhibition → Rb hypophosphorylation → G1 arrest; cyclin G2 → M-phase arrest
- **Apoptosis:** BIM (BCL-2 interacting mediator of cell death), PUMA/BBC3 → BAX/BAK activation → cytochrome c → caspase cascade; TRAIL/TNFSF10 → extrinsic apoptosis
- **Stress resistance:** MnSOD (SOD2), catalase → ROS detoxification; GADD45 → G2/M checkpoint and DNA repair
- **DNA repair:** GADD45, DNA-PK enhancement → improved DSB repair under FOXO activation
- **Metabolism:** G6Pase (glucose-6-phosphatase), PEPCK1 (phosphoenolpyruvate carboxykinase) → gluconeogenesis (FOXO1 in liver); ATGL (adipocyte triglyceride lipase) → lipolysis (FOXO1 in adipose)
- **Autophagy:** LC3, Beclin1, Rab7 (FOXO3) → autophagy induction under starvation
- **Treg function:** FOXO1 directly activates FOXP3 → Treg identity; AKT-FOXO1 axis controls Treg vs. effector T cell fate

## Function

### FOXO in cancer biology [^eijkelenboom-2013-foxo-cancer]

**FOXO as a PI3K-AKT pathway readout and tumor suppressor:**
- In normal tissues: growth factor withdrawal → reduced PI3K → AKT dephosphorylation → FOXO nuclear entry → p21/p27/BIM → quiescence or apoptosis → prevents inappropriate proliferation
- In cancer: PI3K gain-of-function (PIK3CA H1047R) or PTEN loss → AKT hyperactivation → constitutive FOXO cytoplasmic sequestration → loss of all FOXO tumor suppressor functions → unchecked proliferation and apoptosis evasion
- **Clinical implication:** Tumors with PTEN loss and constitutive AKT have near-zero nuclear FOXO1/3 activity; restoration of FOXO by PI3K/AKT inhibition → tumor cell cycle arrest and apoptosis; FOXO re-activation is the mechanistic basis for alpelisib (PI3K-alpha inhibitor) activity in PIK3CA-mutant breast cancer

**FOXO and drug resistance:**
- **Endocrine therapy resistance in HR+ breast cancer:** ESR1 mutations → ligand-independent ER → AKT → FOXO1 cytoplasmic → loss of p21 → continued proliferation despite tamoxifen; CDK4/6 inhibitors + endocrine therapy restores Rb control partially independent of FOXO
- **EGFR TKI resistance (NSCLC):** KRAS secondary mutations → RAS → PI3K → AKT → FOXO suppression → growth factor independence; PI3K inhibitors partially restore FOXO in EGFR TKI-resistant tumors

**FOXO in immunity:**
- **Treg differentiation:** FOXO1 activates FOXP3 transcription → Treg identity; AKT-FOXO1 axis determines effector vs. regulatory T cell fate; FOXO1 deletion in Tregs → Treg instability → autoimmunity; PI3K inhibitors → FOXO1 re-activation → Treg expansion → immunosuppression (potential application in autoimmunity)
- **CD8+ T cell memory:** FOXO1 promotes T cell longevity (TCF7, CCR7 expression) → memory T cell formation; AKT/mTOR-driven FOXO1 exclusion → effector differentiation; IL-15-driven FOXO1 re-expression → memory T cell survival; FOXO1-TCF1+ T cell population predicts checkpoint inhibitor response

### FOXO in aging and metabolic disease

**Type 2 diabetes and hepatic FOXO1:**
- Normal: postprandial insulin → AKT → FOXO1 phosphorylation → nuclear exclusion → PEPCK/G6Pase suppressed → hepatic glucose production off
- T2D: hepatic insulin resistance → AKT fails to phosphorylate FOXO1 → FOXO1 nuclear → PEPCK/G6Pase constitutively active → fasting hyperglycemia; metformin (AMPK) and GLP-1 agonists suppress hepatic FOXO1 via converging mechanisms
- **Therapeutic target:** Liver-specific FOXO1 inhibitor AS1842856 (small molecule) suppresses hepatic glucose production in diabetic mice — proof of concept for FOXO1-targeted T2DM therapy

**Skeletal muscle atrophy:**
- Denervation, disuse, cachexia → reduced AKT → FOXO1/3/4 nuclear → MURF1 (muscle RING finger 1) and Atrogin-1 (MAFbx) E3 ubiquitin ligases → sarcomere protein ubiquitination → proteasomal degradation → muscle atrophy; IGF-1 → PI3K → AKT → FOXO exclusion → prevents atrophy

## Mechanism

### Therapeutic targeting

**PI3K/AKT inhibitors → FOXO re-activation:**
- Alpelisib (PI3K-alpha) → FOXO1/3 nuclear → p21/BIM → tumor suppression in PIK3CA-mutant tumors; capivasertib (pan-AKT) → FOXO re-activation; idelalisib/copanlisib (PI3K-delta/pan) → FOXO in hematologic malignancies
- Biomarker: nuclear FOXO1/3 IHC can serve as pharmacodynamic marker of PI3K/AKT inhibitor target engagement

**FOXO activators (investigational):**
- Metformin/AMPK activators → FOXO3 Ser413/555 phosphorylation → nuclear → anti-aging and anti-proliferative effects
- Direct FOXO activators (small molecules) — limited development; challenge: FOXO activation simultaneously causes atrophy in muscle and immunosuppression in Tregs

**SIRT1-FOXO axis in aging:**
- Caloric restriction → SIRT1 → FOXO3 deacetylation → stress resistance (not apoptosis); resveratrol (SIRT1 activator) → FOXO3 → SOD2/catalase → lifespan extension in model organisms; clinical trials in aging/metabolic disease ongoing (CALERIE study)

## Connections

- `connects-to` → **[AKT](../akt/README.md)** — AKT is the primary FOXO kinase: AKT phosphorylates FOXO1 Thr24/Ser256 and FOXO3 Thr32/Ser253 → 14-3-3 binding → nuclear exclusion → loss of p21, BIM, PUMA, catalase; PTEN loss → constitutive AKT → constitutive FOXO cytoplasmic sequestration in cancer.
- `connects-to` → **[p53](../p53/README.md)** — FOXO3 and p53 co-activate overlapping programs (PUMA, p21, BIM, GADD45) → apoptosis and arrest; FOXO3 competes with MDM2 for p53 binding → p53 stabilization; combined FOXO + p53 inactivation is required for full oncogenic transformation downstream of PI3K-RAS.
- `connects-to` → **[mTOR](../mtor/README.md)** — mTORC1 suppresses FOXO via S6K → IRS-1 degradation → reduced AKT → partial FOXO nuclear entry (negative feedback); mTORC2 phosphorylates AKT Ser473 → FOXO phosphorylation; mTOR inhibitors → FOXO re-activation → cell cycle arrest and partial tumor suppression.
- `connects-to` → **[Insulin Receptor](../insulin-receptor/README.md)** — Insulin → IRS-1/2 → PI3K → AKT → FOXO1 phosphorylation → nuclear exclusion → glucose homeostasis; hepatic FOXO1 drives PEPCK/G6Pase → gluconeogenesis; FOXO1 deregulation contributes to fasting hyperglycemia in type 2 diabetes.

[^brunet-1999-foxo-akt]: Brunet A, Bonni A, Zigmond MJ, et al. Akt promotes cell survival by phosphorylating and inhibiting a Forkhead transcription factor. *Cell.* 1999;96(6):857-868. [doi:10.1016/S0092-8674(00)80595-4](https://doi.org/10.1016/S0092-8674(00)80595-4) · [PubMed 10102273](https://pubmed.ncbi.nlm.nih.gov/10102273/)
[^calnan-2008-foxo-review]: Calnan DR, Brunet A. The FoxO code. *Oncogene.* 2008;27(16):2276-2288. [doi:10.1038/onc.2008.21](https://doi.org/10.1038/onc.2008.21) · [PubMed 18391970](https://pubmed.ncbi.nlm.nih.gov/18391970/)
[^eijkelenboom-2013-foxo-cancer]: Eijkelenboom A, Burgering BM. FOXOs: signalling integrators for homeostasis maintenance. *Nat Rev Mol Cell Biol.* 2013;14(2):83-97. [doi:10.1038/nrm3507](https://doi.org/10.1038/nrm3507) · [PubMed 23325358](https://pubmed.ncbi.nlm.nih.gov/23325358/)
