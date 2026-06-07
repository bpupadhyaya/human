---
schema: human-scale-entry/v1
id: foxo1
name: FOXO1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "FOXO1 (FKHR) is a forkhead TF inactivated by AKT phosphorylation → cytoplasmic sequestration; nuclear FOXO1 induces p27, FasL, and antioxidant genes; PAX3-FOXO1 t(2;13) and PAX7-FOXO1 t(1;13) are defining oncogenic fusions in alveolar rhabdomyosarcoma."
aliases: ["FOXO1", "FKHR", "forkhead box O1", "PAX3-FOXO1", "PAX7-FOXO1", "FOXO1 rhabdomyosarcoma", "FOXO1 AKT", "FKHR alveolar RMS"]
sources:
  - id: galili-1993-pax3-foxo1
    type: peer-reviewed
    cite: "Galili N, Davis RJ, Fredericks WJ, et al. Fusion of a fork head domain gene to PAX3 in the solid tumour alveolar rhabdomyosarcoma. Nat Genet. 1993;5(3):230-235."
    doi: "10.1038/ng1193-230"
    pmid: "8275086"
    url: "https://doi.org/10.1038/ng1193-230"
  - id: missiaglia-2012-foxo1-rms-prognosis
    type: peer-reviewed
    cite: "Missiaglia E, Williamson D, Chisholm J, et al. PAX3/FOXO1 fusion gene status is the key prognostic molecular marker in rhabdomyosarcoma and significantly improves current risk stratification. J Clin Oncol. 2012;30(14):1670-1677."
    doi: "10.1200/JCO.2011.38.5591"
    pmid: "22454413"
    url: "https://doi.org/10.1200/JCO.2011.38.5591"
cross_links:
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT phosphorylates FOXO1 at Thr24/Ser256/Ser319 → cytoplasmic sequestration by 14-3-3 proteins → FOXO1 cannot activate p27, FasL, or antioxidant genes; mTORC2 → AKT → FOXO1 inactivation is a central survival pathway in rhabdomyosarcoma and breast cancer."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "PAX3-FOXO1 transcriptionally activates MYCN in alveolar RMS (MYCN detected in ~50% ARMS); MYC and MYCN amplification in fusion-negative RMS correlate with poor prognosis; BET inhibitors suppress MYC/MYCN in ARMS preclinically; CDK4 is also a PAX3-FOXO1 target."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "PAX3-FOXO1 transcriptionally activates MET (HGF receptor) → invasion and metastasis in alveolar RMS; MET overexpression in >50% ARMS; crizotinib active in MET-expressing pediatric solid tumors including ARMS; MET expression correlates with PAX3-FOXO1 status."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "FOXO1 is the primary tumor suppressor target of the PTEN-PI3K-AKT axis; PTEN loss → AKT → FOXO1 cytoplasmic sequestration → proliferation; PTEN mutations in ~10% RMS activate AKT; PI3K inhibitors (BKM120) restore FOXO1 nuclear activity in PTEN-null cancer cells."
---

# FOXO1

## Overview

**FOXO1 (Forkhead Box protein O1)**, also known as **FKHR (Forkhead in Rhabdomyosarcoma)**, is a member of the FOXO subclass of forkhead (FOX) transcription factors characterized by a conserved ~110-amino-acid winged-helix DNA-binding domain. FOXO1 is a critical integrator of **PI3K-AKT pathway** status and acts as a **tumor suppressor** when nuclear — driving expression of cell cycle arrest (p27/CDKN1B), apoptosis (FasL/FASLG, BIM/BCL2L11, BNIP3), and antioxidant (SOD2, catalase) genes. AKT phosphorylates FOXO1 at three conserved serine/threonine residues → triggers 14-3-3 protein binding → cytoplasmic sequestration → FOXO1 cannot activate target genes → cell survives and proliferates. FOXO1 gained oncological importance in 1993 when **Galili et al. identified the PAX3-FOXO1 (PAX3-FKHR) fusion** — created by t(2;13)(q35;q14) — as the defining molecular alteration of **alveolar rhabdomyosarcoma (ARMS)** [^galili-1993-pax3-foxo1]. In the PAX3-FOXO1 fusion, FOXO1's forkhead domain is replaced by the PAX3 DNA-binding domains, while FOXO1's transactivation domain (TAD) provides ~100-fold stronger transcriptional activation than PAX3 alone — creating a potent oncogenic chimeric transcription factor. PAX3-FOXO1 fusion status is now the most important prognostic molecular marker in RMS, independently predicting inferior survival [^missiaglia-2012-foxo1-rms-prognosis].

**FOXO1 in disease:**
- **Alveolar RMS:** PAX3-FOXO1 t(2;13) ~55%; PAX7-FOXO1 t(1;13) ~20%; fusion-negative ARMS ~25%; fusion status determines prognosis
- **PI3K/AKT-driven cancers:** FOXO1 inactivation (via AKT hyperactivation) in breast cancer (PIK3CA mutations), prostate cancer (PTEN loss), endometrial cancer (PIK3CA + PTEN mutations) — FOXO1 is a functional tumor suppressor in these contexts even without genetic mutation
- **Diabetic metabolism:** FOXO1 in liver activates PEPCK, G6Pase → gluconeogenesis; AKT/insulin signaling suppresses FOXO1 → prevents excess glucose output; hepatic FOXO1 knockdown in mice → hypoglycemia
- **Immunology:** FOXO1 regulates T-cell quiescence and naïve T-cell trafficking (FOXO1 → KLF2 → CCR7, S1PR1 expression → lymph node egress); germinal center B cells: FOXO1 → AID activation → somatic hypermutation

## Structure

### FOXO1 protein architecture

FOXO1 is a 655-amino-acid protein (~71 kDa):

**Forkhead DNA-binding domain (FHD, ~156-255):**
Winged-helix fold (3 helices, 3 β-strands, 2 wing loops); recognizes consensus insulin response element (IRE): 5'-GTAAACAA-3' → FOXO1 binds and activates promoters/enhancers of target genes; crystal structures reveal H1 and H3 helices make major groove contacts; the "wing2" region is required for high-affinity DNA binding; in the **PAX3-FOXO1 fusion**, this FHD is replaced by PAX3's paired box + homeodomain → the fusion protein binds PAX3 targets (MYOD1 enhancers, MET promoter, CDK4 targets) not FOXO1 targets.

**Nuclear export signal (NES, ~383-395):**
Leucine-rich NES that mediates CRM1 (exportin-1)-dependent nuclear export when FOXO1 is phosphorylated; AKT phosphorylation at Ser256 exposes NES → CRM1 binding → export; leptomycin B (CRM1 inhibitor) traps FOXO1 in nucleus → anti-proliferative in cancer cells.

**C-terminal transactivation domain (TAD, ~469-655):**
Proline/glutamine-rich; interacts with CREB-binding protein (CBP/p300) → histone acetyltransferase recruitment → H3K27ac at FOXO1 target genes; this domain is **retained in both PAX3-FOXO1 and PAX7-FOXO1 fusions** → provides strong transcriptional activation capacity far exceeding PAX3/PAX7 alone; FOXO1-TAD is the key oncogenic contribution to the fusion.

**AKT phosphorylation sites:**
- **Thr24:** 14-3-3 binding site; phosphorylation alone insufficient for full cytoplasmic sequestration
- **Ser256:** Primary 14-3-3 binding site; essential for AKT-mediated nuclear exclusion
- **Ser319:** Promotes CK1 phosphorylation at Ser322/Ser325 → additional 14-3-3 interaction; maximal cytoplasmic retention requires all three sites

### PAX3-FOXO1 and PAX7-FOXO1 fusions

**PAX3-FOXO1 t(2;13)(q35;q14) (~55% of ARMS):**
PAX3 exons 1-7 (paired box + octapeptide + homeodomain, aa 1-340) fused in-frame to FOXO1 exons 2-3 (TAD, aa 1-655 of FOXO1 → approximately the entire FOXO1 C-terminal 2/3); PAX3 provides DNA-binding specificity for PAX3-recognized sequences; FOXO1 TAD provides transcriptional activation 100x stronger than PAX3 alone; PAX3-FOXO1 is resistant to AKT-mediated cytoplasmic sequestration (the Ser256/Thr24 of FOXO1 are present but partially blocked by PAX3 structure — the fusion mainly localizes to nucleus even when AKT is active); **most aggressive alveolar RMS variant**: 5-year OS ~50-55% vs ~75% for PAX7-FOXO1.

**PAX7-FOXO1 t(1;13)(p36;q14) (~20% of ARMS):**
PAX7 (chromosome 1p36) exons 1-5 (paired box + octapeptide) fused to FOXO1 TAD; PAX7 normally expressed in satellite cells (muscle stem cells); PAX7-FOXO1 binds PAX7 recognition sites with enhanced transactivation; weaker transformation than PAX3-FOXO1; associated with peripheral/extremity location and amplification of the fusion locus on 1p36 (genomic amplification → higher fusion transcript levels); **intermediate prognosis**: 5-year OS ~75% (similar to ERMS in some series).

## Function

### Normal FOXO1 roles

**PI3K-AKT-FOXO1 axis in growth factor signaling:**
Growth factors (EGF, IGF1, insulin) → RTK → IRS1 → PI3K → PIP3 → PDK1 + mTORC2 → AKT (Thr308 by PDK1, Ser473 by mTORC2) → AKT phosphorylates FOXO1 at Thr24/Ser256/Ser319 → 14-3-3ε binds → FOXO1 exported from nucleus → no FOXO1 target gene expression → cell cycle progression and survival; conversely, growth factor withdrawal → AKT inactive → FOXO1 dephosphorylated → FOXO1 nuclear → p27 (CDKN1B) → G1 arrest; FasL → apoptosis; catalase/SOD2 → oxidative stress protection.

**FOXO1 in muscle stem cells:**
Satellite cells express PAX7 (not PAX3); FOXO1 regulates satellite cell quiescence and self-renewal; normal satellite cell activation: quiescent FOXO1-high → activated satellite cell: AKT → FOXO1 cytoplasmic → MYOD1 expression → myoblast → myofiber; FOXO1 knockout mice: impaired muscle regeneration.

**FOXO1 in hepatic glucose metabolism:**
Insulin → AKT → FOXO1 phosphorylation/cytoplasmic → PEPCK (PCK1) and G6Pase (G6PC) genes silenced → reduced gluconeogenesis; fasting → low insulin → FOXO1 nuclear → PEPCK/G6Pase expression → hepatic glucose output; type 2 diabetes: insulin resistance → AKT blunted → FOXO1 persistently nuclear → fasting hyperglycemia from excess gluconeogenesis; therapeutic target: FOXO1 inhibitors (AS1842856) reduce fasting glucose in T2D models.

### PAX3-FOXO1 oncogenic transcriptional program

**Key downstream targets:**
- **MYOD1/MYOG (myogenin):** PAX3-FOXO1 activates MYOD1 enhancer → myogenic differentiation arrest (blast cells express MYOD1 without differentiating — diagnostic IHC marker)
- **MET (HGF receptor):** PAX3 binds MET promoter → MET overexpression → HGF-MET signaling → invasion, metastasis, survival; MET is a therapeutic target in ARMS
- **CDK4:** PAX3-FOXO1 → CDK4 overexpression → RB phosphorylation → E2F → proliferation; CDK4 amplification also occurs independently in RMS
- **FGFR4:** PAX3-FOXO1 activates FGFR4 expression → FGF-FGFR4 signaling → RMS survival; FGFR4 mutations (~7%) also activate this pathway in fusion-negative RMS
- **MYCN:** Downstream of PAX3-FOXO1; MYCN amplification in ~50% of ARMS; MYCN maintains the proliferative blast state

## Mechanism

### PAX3-FOXO1 as a therapeutic target

**Challenges:**
PAX3-FOXO1 is a transcription factor with no clear enzymatic pocket; direct small-molecule inhibition is challenging; indirect approaches target:

**BET bromodomain inhibition:**
PAX3-FOXO1 super-enhancer occupancy requires BRD4; JQ1 (BET inhibitor) → disrupts BRD4 at PAX3-FOXO1 SE → reduces PAX3-FOXO1 mRNA → downstream target gene suppression → RMS cell death; clinical BET inhibitors (BMS-986158, INCB054329) in Phase 1 trials including pediatric solid tumors.

**CDK4/6 inhibition:**
PAX3-FOXO1 → CDK4 overexpression → palbociclib, ribociclib, abemaciclib: reduce RB phosphorylation → G1 arrest → apoptosis in ARMS; SARC037 trial: palbociclib in pediatric sarcomas including RMS; combination CDK4/6 + SRC inhibitor: synergistic in ARMS preclinically.

**MET inhibition:**
Crizotinib, cabozantinib: MET inhibition → ARMS cell death in vitro; COG ADVL1312 (crizotinib phase 1 in pediatric): RMS cohort showed ~20% ORR; ongoing: cabozantinib in pediatric solid tumors including MET-positive RMS.

**FOXO1 as prognostic biomarker [^missiaglia-2012-foxo1-rms-prognosis]:**
FOXO1 FISH (PAX3::FOXO1 or PAX7::FOXO1 break-apart): essential for all histologically alveolar or ambiguous RMS; COG molecular classification: PAX3-FOXO1+ → "ARMS-PAX3" (high-risk); PAX7-FOXO1+ → "ARMS-PAX7" (intermediate, context-dependent); fusion-negative RMS → treat like ERMS (intermediate-to-good prognosis); FOXO1 status significantly reclassifies risk compared to histology alone.

## Connections

- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT phosphorylates FOXO1 at Thr24/Ser256/Ser319 → cytoplasmic sequestration by 14-3-3 proteins → FOXO1 cannot activate p27, FasL, or antioxidant genes; mTORC2 → AKT → FOXO1 inactivation is a central survival pathway in rhabdomyosarcoma and breast cancer.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — PAX3-FOXO1 transcriptionally activates MYCN in alveolar RMS (MYCN detected in ~50% ARMS); MYC and MYCN amplification in fusion-negative RMS correlate with poor prognosis; BET inhibitors suppress MYC/MYCN in ARMS preclinically; CDK4 is also a PAX3-FOXO1 target.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — PAX3-FOXO1 transcriptionally activates MET (HGF receptor) → invasion and metastasis in alveolar RMS; MET overexpression in >50% ARMS; crizotinib active in MET-expressing pediatric solid tumors including ARMS; MET expression correlates with PAX3-FOXO1 status.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — FOXO1 is the primary tumor suppressor target of the PTEN-PI3K-AKT axis; PTEN loss → AKT → FOXO1 cytoplasmic sequestration → proliferation; PTEN mutations in ~10% RMS activate AKT; PI3K inhibitors (BKM120) restore FOXO1 nuclear activity in PTEN-null cancer cells.

[^galili-1993-pax3-foxo1]: Galili N, Davis RJ, Fredericks WJ, et al. Fusion of a fork head domain gene to PAX3 in the solid tumour alveolar rhabdomyosarcoma. *Nat Genet.* 1993;5(3):230-235. [doi:10.1038/ng1193-230](https://doi.org/10.1038/ng1193-230) · [PubMed 8275086](https://pubmed.ncbi.nlm.nih.gov/8275086/)
[^missiaglia-2012-foxo1-rms-prognosis]: Missiaglia E, Williamson D, Chisholm J, et al. PAX3/FOXO1 fusion gene status is the key prognostic molecular marker in rhabdomyosarcoma and significantly improves current risk stratification. *J Clin Oncol.* 2012;30(14):1670-1677. [doi:10.1200/JCO.2011.38.5591](https://doi.org/10.1200/JCO.2011.38.5591) · [PubMed 22454413](https://pubmed.ncbi.nlm.nih.gov/22454413/)
