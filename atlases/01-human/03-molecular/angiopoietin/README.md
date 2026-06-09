---
schema: human-scale-entry/v1
id: angiopoietin
name: Angiopoietin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Angiopoietins (Ang-1, Ang-2) bind Tie2 on endothelium; Ang-1 stabilizes vessels; Ang-2 destabilizes and cooperates with VEGF for angiogenesis and vascular leak. Faricimab (anti-Ang-2/VEGF-A bispecific) treats diabetic macular edema and nAMD with extended Q16W dosing intervals."
aliases: ["Ang-1", "Ang-2", "ANGPT1", "ANGPT2", "angiopoietin-1", "angiopoietin-2", "Tie2 ligand"]
sources:
  - id: davis-1996-angiopoietin1-tie2
    type: peer-reviewed
    cite: "Davis S, Aldrich TH, Jones PF, et al. Isolation of angiopoietin-1, a ligand for the TIE2 receptor, by secretion-trap expression cloning. Cell. 1996;87(7):1161-1169."
    doi: "10.1016/S0092-8674(00)81812-7"
    pmid: "8980223"
    url: "https://doi.org/10.1016/S0092-8674(00)81812-7"
  - id: maisonpierre-1997-angiopoietin2
    type: peer-reviewed
    cite: "Maisonpierre PC, Suri C, Jones PF, et al. Angiopoietin-2, a natural antagonist for Tie2 that disrupts in vivo angiogenesis. Science. 1997;277(5322):55-60."
    doi: "10.1126/science.277.5322.55"
    pmid: "9204896"
    url: "https://doi.org/10.1126/science.277.5322.55"
  - id: wykoff-2022-faricimab-tenaya-lucerne
    type: peer-reviewed
    cite: "Wykoff CC, Abreu F, Adamis AP, et al. Efficacy, durability, and safety of intravitreal faricimab with extended dosing up to every 16 weeks in patients with diabetic macular oedema (YOSEMITE and RHINE): two randomised, double-masked, phase 3 trials. Lancet. 2022;399(10326):741-755."
    doi: "10.1016/S0140-6736(22)00018-6"
    pmid: "35085503"
    url: "https://doi.org/10.1016/S0140-6736(22)00018-6"
cross_links:
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Ang-2 elevated in diabetic retinas → Tie2 destabilization → pericyte loss → endothelial junction opening → macular edema + neovascularization; faricimab (anti-Ang-2 + anti-VEGF-A) achieves Q16W dosing with non-inferior VA gains vs. aflibercept Q8W (YOSEMITE/RHINE)."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ang-2 destabilizes vessel walls (pericyte detachment, junction opening) → sensitizes endothelium to VEGF → maximal angiogenic sprouting; faricimab dual blockade (anti-Ang-2 + anti-VEGF-A) reduces edema and neovascularization more effectively than anti-VEGF monotherapy."
  - target: 01-human/04-cellular/endothelial-cell
    relation: modulates
    note: "Ang-1/Tie2 → PI3K/Akt + Rho GTPase → VE-cadherin stabilization and eNOS activation → vascular quiescence; Ang-2 competes for Tie2 → adherens junction destabilization, pericyte loss, sensitization to VEGF-driven leak and sprouting."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Ang-2 released from Weibel-Palade bodies in sepsis → Tie2 destabilization → VE-cadherin cleavage → vascular hyperpermeability → organ edema; plasma Ang-2 >10 ng/mL on day 1 predicts ICU mortality; high Ang-2/Ang-1 ratio defines the severe vascular leak phenotype."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Ang-1/Ang-2 imbalance in PAH: Ang-2 overexpression in pulmonary endothelium → Tie2 destabilization → endothelial mesenchymal transition → vascular remodeling; Ang-2 overexpressing mice develop PAH; plasma Ang-2 correlates with hemodynamic severity in PAH patients."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Ang-2 promotes breast cancer angiogenesis: hypoxic tumor cells secrete Ang-2 → vessel destabilization → VEGF-driven sprouting; tumor Ang-2 correlates with lymph node metastasis and poor prognosis; Ang-2 blockade combined with anti-VEGF shows additive anti-tumor activity."
---

# Angiopoietin

## Overview

**Angiopoietins (Ang-1 and Ang-2)** are a family of secreted vascular growth factors that signal exclusively through the receptor tyrosine kinase **Tie2 (TEK)** on vascular endothelial cells, functioning as the critical regulators of **vascular stability, remodeling, and quiescence** — complementary and antagonistic to the VEGF system [^davis-1996-angiopoietin1-tie2].

The two principal ligands have opposing effects on Tie2:
- **Angiopoietin-1 (Ang-1; ANGPT1, chr8q23.1):** Constitutively secreted by pericytes, vascular smooth muscle cells, and stromal cells → **Tie2 agonist** → phosphorylates Tie2 → vessel stabilization, pericyte recruitment, reduced permeability, anti-apoptotic effects on endothelium → **vascular quiescence**
- **Angiopoietin-2 (Ang-2; ANGPT2, chr8p23.1):** Stored in Weibel-Palade bodies of endothelial cells; released acutely by inflammatory stimuli (TNF-α, thrombin, hypoxia, VEGF) → **Tie2 antagonist** (context-dependent) → disrupts Ang-1/Tie2 stabilizing signals → pericyte detachment, junction opening, vascular destabilization → sensitizes endothelium to VEGF → angiogenesis and vascular leak

**Discovery context:** Ang-1 was identified in 1996 by Davis et al. as the first ligand for the orphan receptor Tie2. In 1997, Maisonpierre et al. identified Ang-2 as a natural antagonist of Tie2 that disrupts Ang-1 signaling, establishing the Ang-1/Ang-2 balance as the rheostat controlling vessel stability [^maisonpierre-1997-angiopoietin2].

**Clinical significance:** The Ang-2/VEGF cooperative axis drives pathological neovascularization in **diabetic macular edema (DME)**, **neovascular AMD (nAMD)**, and tumor angiogenesis. **Faricimab** (Vabysmo; Genentech/Roche), the first bispecific antibody approved for ophthalmology, simultaneously blocks Ang-2 and VEGF-A, enabling extended dosing intervals while achieving superior vascular stabilization compared to anti-VEGF monotherapy.

## Structure

**Angiopoietin protein family:**

**Ang-1 (ANGPT1):**
- Gene: chromosome 8q23.1; 498 aa; ~70 kDa monomer; forms multimers (dimers, trimers, tetramers, higher-order oligomers) via N-terminal coiled-coil domain — higher-order oligomers have greater Tie2-activating potency
- **Domains:** N-terminal signal peptide → coiled-coil domain (multimerization) → linker → C-terminal fibrinogen-like domain (FLD; Tie2 binding, Kd ~3 nM)
- **Sources:** Pericytes (primary source), vascular smooth muscle cells, platelets (α-granules), fibroblasts, osteoblasts
- **Regulation:** Relatively constitutive expression; modestly upregulated by PDGF-B and FGF; repressed by Ang-2 autocrine loops in activated endothelium

**Ang-2 (ANGPT2):**
- Gene: chromosome 8p23.1; 496 aa; ~66 kDa; shares 60% homology with Ang-1 in FLD domain; dimerizes but less tendency toward higher-order oligomers (partial explanation for reduced agonist activity)
- **Subcellular localization:** Stored in **Weibel-Palade bodies** (endothelial-specific secretory granules alongside vWF); rapid exocytosis triggered by thrombin, histamine, VEGF, hypoxia, TNF-α, and shear stress
- **Dual role (context-dependent):** In absence of VEGF → Ang-2 can partially activate Tie2 (weak agonist); in presence of VEGF → Ang-2 acts as a Tie2 antagonist, blocking Ang-1 and sensitizing endothelium to VEGF
- **Sources:** Activated endothelial cells (autocrine); pericytes under stress

**Tie2 receptor (TEK):**
- Chromosome 9p21.2; 1124 aa; class III RTK with unique extracellular domain structure
- **Extracellular:** 3 Ig-like domains + EGF-like domain + 3 fibronectin-type III domains → Ang-1 binds Ig1/2 junction; receptor clustering by Ang-1 multimers is required for efficient kinase activation
- **Intracellular:** Juxtamembrane (autoinhibitory Y992 phosphorylation site) + kinase domain (Y1100/Y1108 activation loop) + C-terminal tail (Y1217 → PI3K docking)
- **Tie1 (orphan receptor):** Heterodimerizes with Tie2; modulates Tie2 responses; Tie1 cleavage by ADAM17 in inflammation → regulates Ang-1/Ang-2 sensitivity

**Angiopoietin-4 (Ang-4; ANGPT4, chr20p11.2):**
- Functionally similar to Ang-1 in humans (ortholog of mouse Ang-3 which is a Tie2 antagonist); Tie2 agonist; expressed in lung type II pneumocytes; role in pulmonary vascular homeostasis and alveolar development

## Function

**Tie2 signaling — Ang-1 agonist pathway:**
- Ang-1 multimer binding → Tie2 dimerization/clustering → transautophosphorylation at Y1100/Y1108 (kinase activation loop)
- **PI3K/Akt axis:** pTie2 → Y1217 → PI3K-p85 → Akt → **eNOS** (Ser1177 phosphorylation → NO → vasodilation) + **Foxo1** (phosphorylation → nuclear exclusion → ↓Ang-2 transcription → negative feedback loop) + **mTOR** → endothelial survival
- **GTPase axis:** Akt/Rac1 + RhoA inhibition → VE-cadherin stabilization at adherens junctions + cortical actin → reduced permeability
- **ABIN-2 (A20-binding inhibitor of NF-κB):** Recruited to phospho-Tie2 → inhibits NF-κB → ↓ICAM-1, VCAM-1, E-selectin → anti-inflammatory phenotype
- Net: quiescent, barrier-competent endothelium with pericyte coverage and tight junctions

**Ang-2 destabilization pathway:**
- Acute Ang-2 release (Weibel-Palade exocytosis) → competitive displacement of Ang-1 from Tie2 → Tie2 dephosphorylation → ↓PI3K/Akt → Foxo1 nuclear re-entry → ↑Ang-2 transcription (positive feedback) + ↑MMP-9, MMP-14 → pericyte detachment (↓PDGFR-β/PDGF-B signaling) + ↓claudin-5/occludin → junction opening → vascular leak
- **Cooperates with VEGF:** Ang-2-destabilized endothelium upregulates VEGFR-2 and is hypersensitive to VEGF → maximal angiogenic sprouting (tip cell selection via Dll4/Notch) + plasma protein extravasation

**Ang-2 in inflammation:**
- TNF-α/IL-1β → rapid Weibel-Palade exocytosis → Ang-2 release → NF-κB derepression (loss of ABIN-2 signaling) → ICAM-1, VCAM-1, E-selectin → neutrophil and monocyte adhesion and transmigration
- **Sepsis:** Ang-2/Ang-1 ratio is a validated biomarker of endothelial activation in sepsis; elevated Ang-2 predicts capillary leak, ARDS, and 28-day mortality

**Ang-2 in tumor angiogenesis:**
- Tumor hypoxia + VEGF → sustained Ang-2 expression by tumor-associated endothelium → destabilized, leaky tumor vasculature → efficient metastatic intravasation; high tumor Ang-2 predicts poor prognosis in multiple cancers

## Mechanism

**Faricimab (Vabysmo; Genentech/Roche) — first bispecific antibody in ophthalmology:** [^wykoff-2022-faricimab-tenaya-lucerne]
- IgG1 bispecific antibody; simultaneously binds:
  - **Ang-2** (blocks Tie2 destabilization → restores pericyte coverage, reduces vascular leak)
  - **VEGF-A** (blocks VEGFR-2 activation → reduces endothelial proliferation and sprouting)
- Dual blockade rationale: anti-VEGF alone leaves Ang-2-mediated destabilization unchecked; faricimab achieves superior vascular stabilization vs. anti-VEGF monotherapy in preclinical models

**YOSEMITE and RHINE trials (DME) [^wykoff-2022-faricimab-tenaya-lucerne]:**
- Design: 1891 patients with center-involving DME; faricimab 6 mg Q8W or personalized treatment interval (PTI) up to Q16W vs. aflibercept 2 mg Q8W; 2-year follow-up
- **Primary endpoint (year 1 BCVA gain):** Faricimab Q8W: +10.7 letters; PTI: +11.6 letters; aflibercept Q8W: +10.9 letters → **non-inferiority** achieved
- **Durability advantage (Q16W eligible):** At 1 year, 53-60% of faricimab PTI patients on Q12W-Q16W dosing (vs. fixed Q8W for aflibercept); by year 2: ~50-60% of faricimab patients maintained Q12W-Q16W intervals
- Anatomical outcomes: Greater central subfield thickness (CST) reduction with faricimab; higher rates of fluid resolution on OCT
- **FDA approval:** January 2022 for DME; simultaneous approval for nAMD

**TENAYA and LUCERNE trials (nAMD):**
- 1329 patients with nAMD; faricimab PTI up to Q16W vs. aflibercept Q8W; 2-year follow-up
- BCVA: Non-inferior at year 1; at 2 years: +6.6 letters vs. +6.0 letters (faricimab vs. aflibercept)
- Durability: ~45% of faricimab patients at Q16W intervals at 2 years; sustained anatomical benefit

**Angiopoietin pathway in sepsis and ARDS:**
- Ang-1 (rhAng-1 or COMP-Ang1 — modified Ang-1 with better pharmacokinetics) → preclinical sepsis/ARDS: reduced pulmonary edema, neutrophil transmigration, and organ injury
- **VasculoTIDE (Tie2 agonist peptide):** Preclinical efficacy in sepsis/LPS models; not yet in Phase 3
- Ang-2 as sepsis biomarker: Ang-2/Ang-1 ratio on ICU day 1 predicts 28-day mortality (AUROC ~0.75 in multiple cohorts); Ang-2 >10,000 pg/mL associated with high capillary leak risk

## Connections

- `connects-to` → **[Diabetic Retinopathy](../../07-system/diabetic-retinopathy/README.md)** — Ang-2 elevated in diabetic retinas → Tie2 destabilization → pericyte loss → endothelial junction opening → macular edema + neovascularization; faricimab (anti-Ang-2 + anti-VEGF-A) achieves Q16W dosing with non-inferior VA gains vs. aflibercept Q8W (YOSEMITE/RHINE).
- `connects-to` → **[VEGF](../vegf/README.md)** — Ang-2 destabilizes vessel walls (pericyte detachment, junction opening) → sensitizes endothelium to VEGF → maximal angiogenic sprouting; faricimab dual blockade (anti-Ang-2 + anti-VEGF-A) reduces edema and neovascularization more effectively than anti-VEGF monotherapy.
- `modulates` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Ang-1/Tie2 → PI3K/Akt + Rho GTPase → VE-cadherin stabilization and eNOS activation → vascular quiescence; Ang-2 competes for Tie2 → adherens junction destabilization, pericyte loss, sensitization to VEGF-driven leak and sprouting.
- `connects-to` → **[Sepsis](../../07-system/sepsis/README.md)** — Ang-2 released from Weibel-Palade bodies in sepsis → Tie2 destabilization → VE-cadherin cleavage → vascular hyperpermeability → organ edema; plasma Ang-2 >10 ng/mL on day 1 predicts ICU mortality; high Ang-2/Ang-1 ratio defines the severe vascular leak phenotype.
- `connects-to` → **[Pulmonary Arterial Hypertension](../../07-system/pulmonary-arterial-hypertension/README.md)** — Ang-1/Ang-2 imbalance in PAH: Ang-2 overexpression in pulmonary endothelium → Tie2 destabilization → endothelial mesenchymal transition → vascular remodeling; Ang-2 overexpressing mice develop PAH; plasma Ang-2 correlates with hemodynamic severity in PAH patients.
- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — Ang-2 promotes breast cancer angiogenesis: hypoxic tumor cells secrete Ang-2 → vessel destabilization → VEGF-driven sprouting; tumor Ang-2 correlates with lymph node metastasis and poor prognosis; Ang-2 blockade combined with anti-VEGF shows additive anti-tumor activity.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^davis-1996-angiopoietin1-tie2]: Davis S, Aldrich TH, Jones PF, et al. Isolation of angiopoietin-1, a ligand for the TIE2 receptor, by secretion-trap expression cloning. *Cell.* 1996;87(7):1161-1169. [doi:10.1016/S0092-8674(00)81812-7](https://doi.org/10.1016/S0092-8674(00)81812-7) · [PubMed 8980223](https://pubmed.ncbi.nlm.nih.gov/8980223/)
[^maisonpierre-1997-angiopoietin2]: Maisonpierre PC, Suri C, Jones PF, et al. Angiopoietin-2, a natural antagonist for Tie2 that disrupts in vivo angiogenesis. *Science.* 1997;277(5322):55-60. [doi:10.1126/science.277.5322.55](https://doi.org/10.1126/science.277.5322.55) · [PubMed 9204896](https://pubmed.ncbi.nlm.nih.gov/9204896/)
[^wykoff-2022-faricimab-tenaya-lucerne]: Wykoff CC, Abreu F, Adamis AP, et al. Efficacy, durability, and safety of intravitreal faricimab with extended dosing up to every 16 weeks in patients with diabetic macular oedema (YOSEMITE and RHINE). *Lancet.* 2022;399(10326):741-755. [doi:10.1016/S0140-6736(22)00018-6](https://doi.org/10.1016/S0140-6736(22)00018-6) · [PubMed 35085503](https://pubmed.ncbi.nlm.nih.gov/35085503/)
