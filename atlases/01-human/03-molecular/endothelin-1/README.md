---
schema: human-scale-entry/v1
id: endothelin-1
name: Endothelin-1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Endothelin-1 (ET-1, EDN1) is the most potent endogenous vasoconstrictor; ETA/ETB receptor signaling drives sustained vasoconstriction, vascular remodeling, and fibrosis; bosentan and macitentan (dual ERAs) are first-line therapy for pulmonary arterial hypertension."
aliases: ["endothelin-1", "ET-1", "EDN1", "ETA receptor", "ETB receptor", "endothelin receptor antagonist", "ERA", "bosentan", "macitentan", "ambrisentan", "pulmonary arterial hypertension", "PAH"]
cross_links:
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "ET-1 is the most potent vasoconstrictor and is elevated in resistant hypertension, CKD-related hypertension, and preeclampsia; ETA receptor on vascular smooth muscle → vasoconstriction; ETB receptor on endothelium → NO and PGI2 (counterbalances); dual ERA bosentan lowers BP."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "ET-1 promotes cardiac hypertrophy via ETA receptor → Gq/PKC → MAPK → fetal gene program; elevated ET-1 in heart failure correlates with severity; ET-1 activates fibroblasts → cardiac fibrosis; ETA/ETB dual blockade did not improve outcomes in HFrEF (REACH-1 trial)."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "ET-1 and NO are opposing endothelial regulators: ET-1 (ETA) → vasoconstriction; eNOS-derived NO → vasodilation; ET-1 suppresses eNOS expression and NO bioavailability; endothelial ETB → NO and PGI2 release (protective counter-regulation within the endothelium itself)."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "ET-1 → ETA on mesangial cells and podocytes → glomerular hypertension and proteinuria; elevated urinary ET-1 predicts CKD progression; sparsentan (dual ERA + angiotensin receptor blocker) reduced proteinuria in IgA nephropathy (PROTECT trial Phase 3)."
sources:
  - id: yanagisawa-1988-endothelin
    type: peer-reviewed
    cite: "Yanagisawa M, Kurihara H, Kimura S, et al. A novel potent vasoconstrictor peptide produced by vascular endothelial cells. Nature. 1988;332(6163):411-415."
    doi: "10.1038/332411a0"
    pmid: "2451132"
    url: "https://doi.org/10.1038/332411a0"
  - id: galie-2019-pah-guidelines
    type: peer-reviewed
    cite: "Galie N, Channick RN, Frantz RP, et al. Risk stratification and medical therapy of pulmonary arterial hypertension. Eur Respir J. 2019;53(1):1801889."
    doi: "10.1183/13993003.01889-2018"
    pmid: "30545974"
    url: "https://doi.org/10.1183/13993003.01889-2018"
---

# Endothelin-1

## Overview

**Endothelin-1** (ET-1; gene *EDN1*, chromosome 6p24.1) is a **21-amino acid peptide** produced primarily by **vascular endothelial cells** and is the **most potent endogenous vasoconstrictor** known — 10× more potent than angiotensin II on a molar basis, with a prolonged duration of action (hours vs. seconds for angiotensin II). ET-1 was discovered by Yanagisawa et al. in 1988 as a novel peptide produced by vascular endothelial cells that caused sustained contraction of isolated vascular smooth muscle [^yanagisawa-1988-endothelin] — a seminal discovery leading directly to a new therapeutic class.

The endothelin family has three members:
- **ET-1 (EDN1):** Primary vascular isoform; produced by endothelial cells, smooth muscle cells, cardiomyocytes, macrophages; key mediator of vasoconstriction, fibrosis, and mitogenesis
- **ET-2 (EDN2):** Intestinal and renal distribution; minor cardiovascular role
- **ET-3 (EDN3):** Neural and renal crest cells; ENS (enteric nervous system) development; mutations cause Hirschsprung's disease

**Clinical significance of ET-1:**
ET-1 is elevated in **pulmonary arterial hypertension (PAH)**, heart failure, hypertension, CKD, sepsis, preeclampsia, and coronary artery disease. **Endothelin receptor antagonists (ERAs)** — bosentan, ambrisentan, and macitentan — are first-line therapies for PAH, demonstrating improvements in 6-minute walk distance, hemodynamics, and clinical worsening [^galie-2019-pah-guidelines]. Bosentan was the first oral PAH therapy (FDA approved 2001).

**ET-1 receptor biology — two opposing signals:**

| Receptor | Location | Coupling | Effect |
|---|---|---|---|
| ETA | VSM (dominant), cardiac fibroblasts, mesangial cells | Gq/G₁₂ → PLC → DAG/IP₃ → Ca²⁺; PKC → MAPK | Vasoconstriction, hypertrophy, fibrosis |
| ETB | Endothelium (type 1); VSM (type 2); renal tubules | Gq/Gi → eNOS → NO; PLC → PGI₂ | Endothelial: vasodilation, NO/PGI₂; VSM: vasoconstriction (type 2) |

## Structure

**ET-1 processing:**

**Prepro-ET-1 (212 aa)** → signal peptide cleavage → **Pro-ET-1 (203 aa)** → furin/PC5/7 → **Big ET-1 (38 aa)** → **Endothelin-converting enzyme-1 (ECE-1; NEP-like metalloprotease)** → **Mature ET-1 (21 aa)**

**Mature ET-1 structure (21 aa):**
- N-terminal tail (residues 1-6): flexible; not required for receptor binding
- **Cys1-Cys15 and Cys3-Cys11 disulfide bonds:** Create the characteristic bicycle ring structure essential for receptor binding — ET-1 contains two interlocking disulfide bonds forming a compact bicyclic structure unique among vasopeptides
- **C-terminal hydrophobic tail (residues 16-21, WSXWII):** Critical for high-affinity ETA binding; less important for ETB
- The disulfide scaffold makes ET-1 resistant to most proteases — contributes to its prolonged activity

**ECE-1 (Endothelin-Converting Enzyme):**
- Membrane-anchored zinc metallopeptidase (neprilysin family); same family as neprilysin (which degrades natriuretic peptides, ET-1, and bradykinin)
- Note: sacubitril (neprilysin inhibitor in ARNI) also inhibits ECE-1, reducing ET-1 conversion from Big ET-1 — contributing to ARNI's anti-fibrotic effects in HF

**Big ET-1:**
- 38-aa precursor; 10-100× less vasoactive than mature ET-1; circulates at higher levels; cleaved locally at tissue sites
- Plasma Big ET-1 is a more stable biomarker than ET-1 (which has ~5 min plasma half-life)

## Function

**Vascular effects (ETA on VSM):**
- ETA → Gq → PLC → IP₃ → ER Ca²⁺ release + DAG → PKC → myosin light chain kinase (MLCK) activation → sustained vasoconstriction
- ETA → G₁₂ → RhoA/ROCK → inhibition of MLCP (myosin light chain phosphatase) → Ca²⁺ sensitization → sustained contraction at lower cytoplasmic [Ca²⁺]
- ETA → MAPK (ERK1/2) → VSM proliferation and migration → vascular remodeling → wall thickening → hypertensive structural changes
- ETA → TGF-β → fibroblast activation → adventitial fibrosis → reduced vascular compliance

**Endothelial effects (ETB type 1 on endothelium — counter-regulatory):**
- Endothelial ETB → Gq → PLC → Ca²⁺ → calmodulin → eNOS → NO production
- Endothelial ETB → prostacyclin (PGI₂) synthesis → vasodilation and platelet inhibition
- Endothelial ETB mediates ET-1 clearance (endocytosis + degradation) — ~80% of circulating ET-1 is cleared by pulmonary endothelial ETB
- This is why selective ETA antagonists (ambrisentan) preserve ETB clearance → potentially more effective ET-1 removal; dual ERA (bosentan, macitentan) blocks this clearance → theoretical pro-ET-1 accumulation, but long-term outcomes equivalent

**Cardiac effects:**
- Cardiomyocyte ETA → Gq → PKC → MAPK → MEF2/NFAT → fetal gene program (β-MHC, ANP, BNP re-expression) → cardiac hypertrophy
- Cardiac fibroblast ETA → TGF-β → collagen I/III → interstitial fibrosis → impaired relaxation
- ET-1 promotes arrhythmogenesis via enhanced afterdepolarizations and Ca²⁺ overload

**Renal effects:**
- ET-1 → ETA/ETB on mesangial cells → glomerular contraction → reduced GFR (acute)
- ET-1 → podocyte ETA → cytoskeletal disruption → increased podocyte permeability → proteinuria
- Collecting duct ETB (type 2) → natriuresis and diuresis — a renoprotective role of ETB
- Urinary ET-1 excretion reflects intrarenal ET-1 production → biomarker of diabetic nephropathy and CKD progression

## Mechanism

**ET-1 in pulmonary arterial hypertension (PAH):**
1. Hypoxia, inflammation, and endothelial injury → ET-1 overproduction by pulmonary endothelial cells
2. ET-1 → ETA on pulmonary VSM → sustained pulmonary vasoconstriction → increased pulmonary vascular resistance (PVR)
3. ET-1 → ETA → MAPK → pulmonary VSM proliferation → medial hypertrophy → fixed vascular remodeling
4. ET-1 → pulmonary fibroblast activation → adventitial fibrosis → reduced vessel compliance
5. Plexiform lesions (end-stage PAH): endothelial cell proliferation and plexiform remodeling — ET-1 drives endothelial survival/proliferation via ETB
6. Result: elevated mean pulmonary artery pressure (mPAP >20 mmHg), PVR elevation → RV pressure overload → RV failure

**Endothelin receptor antagonists (ERAs) in PAH:**
- **Bosentan (Tracleer):** Dual ETA/ETB antagonist; first oral PAH therapy (BREATHE-1 trial, 2002); improves 6MWD, hemodynamics, and delays clinical worsening; hepatotoxicity in ~10% (LFT monitoring required); teratogenic
- **Ambrisentan (Letairis):** Selective ETA antagonist; ARIES-1/2 trials; fewer liver toxicity concerns; lower drug interaction burden; approved alone and in combination with tadalafil (PDE5i)
- **Macitentan (Opsumit):** Dual ERA; SERAPHIN trial (event-driven, long-term): 45% RRR for morbidity/mortality in PAH; improved tissue penetration (sustained receptor occupancy); lower hepatotoxicity than bosentan; FDA black box warning for embryotoxicity (negative pregnancy test monthly)
- All ERAs require REMS programs for embryotoxicity

**Sparsentan (FILSPARI) — ET-1 in CKD/IgA nephropathy:**
- Dual angiotensin receptor blocker (ARB) + ETA antagonist in a single molecule
- PROTECT trial (Phase 3, IgA nephropathy): sparsentan reduced proteinuria 49% vs. irbesartan 15% at 36 weeks; FDA approved 2023 (accelerated approval) for IgA nephropathy
- Mechanism: ARB blocks Ang II-driven mesangial hypertension + ETA blockade reduces podocyte injury → synergistic reduction in proteinuria

**ET-1 in resistant hypertension:**
- Plasma ET-1 and Big ET-1 are elevated in patients with treatment-resistant hypertension (>3 drug classes)
- Darusentan (selective ETA antagonist): Phase 3 trial in resistant hypertension — reduced BP ~8-10 mmHg vs. placebo; not approved but established proof-of-concept
- ETB-mediated clearance is partially reduced in CKD/ESRD → ET-1 accumulates → worsens hypertension in CKD patients

## Connections

ET-1 is the most potent vasoconstrictor and is elevated in resistant hypertension, CKD-related hypertension, and preeclampsia; ETA receptor on vascular smooth muscle → vasoconstriction; ETB receptor on endothelium → NO and PGI2 (counterbalances); dual ERA bosentan lowers BP.

ET-1 promotes cardiac hypertrophy via ETA receptor → Gq/PKC → MAPK → fetal gene program; elevated ET-1 in heart failure correlates with severity; ET-1 activates fibroblasts → cardiac fibrosis; ETA/ETB dual blockade did not improve outcomes in HFrEF (REACH-1 trial).

ET-1 and NO are opposing endothelial regulators: ET-1 (ETA) → vasoconstriction; eNOS-derived NO → vasodilation; ET-1 suppresses eNOS expression and NO bioavailability; endothelial ETB → NO and PGI2 release (protective counter-regulation within the endothelium itself).

ET-1 → ETA on mesangial cells and podocytes → glomerular hypertension and proteinuria; elevated urinary ET-1 predicts CKD progression; sparsentan (dual ERA + angiotensin receptor blocker) reduced proteinuria in IgA nephropathy (PROTECT trial Phase 3).

[^yanagisawa-1988-endothelin]: Yanagisawa M, Kurihara H, Kimura S, et al. A novel potent vasoconstrictor peptide produced by vascular endothelial cells. *Nature.* 1988;332(6163):411-415. [doi:10.1038/332411a0](https://doi.org/10.1038/332411a0) · [PubMed 2451132](https://pubmed.ncbi.nlm.nih.gov/2451132/)
[^galie-2019-pah-guidelines]: Galie N, Channick RN, Frantz RP, et al. Risk stratification and medical therapy of pulmonary arterial hypertension. *Eur Respir J.* 2019;53(1):1801889. [doi:10.1183/13993003.01889-2018](https://doi.org/10.1183/13993003.01889-2018) · [PubMed 30545974](https://pubmed.ncbi.nlm.nih.gov/30545974/)
