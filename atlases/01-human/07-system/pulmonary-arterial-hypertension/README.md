---
schema: human-scale-entry/v1
id: pulmonary-arterial-hypertension
name: Pulmonary Arterial Hypertension
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "PAH (WHO Group 1) is progressive obliterative pulmonary vascular disease; mPAP >20 mmHg + PVR ≥2 WU; BMPR2/BMP9 mutations in heritable PAH. Three pathways (endothelin/NO/prostacyclin) targeted by ERAs, PDE5i/sGCi, and prostacyclin analogues."
aliases: ["PAH", "Group 1 pulmonary hypertension", "pulmonary hypertension", "idiopathic PAH", "IPAH", "heritable PAH", "HPAH", "connective tissue disease PAH", "CTD-PAH"]
sources:
  - id: galie-2015-esc-pah-guidelines
    type: clinical-guideline
    cite: "Galie N, Humbert M, Vachiery JL, et al. 2015 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Heart J. 2016;37(1):67-119."
    doi: "10.1093/eurheartj/ehv317"
    pmid: "26320113"
    url: "https://doi.org/10.1093/eurheartj/ehv317"
  - id: simonneau-2019-pah-classification
    type: peer-reviewed
    cite: "Simonneau G, Montani D, Celermajer DS, et al. Haemodynamic definitions and updated clinical classification of pulmonary hypertension. Eur Respir J. 2019;53(1):1801913."
    doi: "10.1183/13993003.01913-2018"
    pmid: "30545968"
    url: "https://doi.org/10.1183/13993003.01913-2018"
  - id: sitbon-2015-selexipag-griphon
    type: peer-reviewed
    cite: "Sitbon O, Channick R, Chin KM, et al. Selexipag for the Treatment of Pulmonary Arterial Hypertension. N Engl J Med. 2015;373(26):2522-2533."
    doi: "10.1056/NEJMoa1503184"
    pmid: "26579977"
    url: "https://doi.org/10.1056/NEJMoa1503184"
cross_links:
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "ET-1 overproduction by PAH endothelium → ETA on pulmonary VSM → vasoconstriction + medial hypertrophy + adventitial fibrosis → elevated PVR; ERAs (bosentan, ambrisentan, macitentan) are first-line oral therapy for PAH; macitentan reduces morbidity/mortality 45% (SERAPHIN trial)."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Impaired eNOS and NO bioavailability in PAH endothelium → cGMP vasodilation failure; PDE5 inhibitors (sildenafil, tadalafil) prevent cGMP degradation → sustained vasodilation + anti-proliferative; sGC stimulators (riociguat) amplify NO-sGC-cGMP independent of endogenous NO."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "PAH endothelium produces insufficient PGI2 (prostacyclin) → IP receptor → cAMP → vasodilation and anti-proliferative; IV epoprostenol (Flolan) reduces mortality in severe PAH; inhaled iloprost, SC/IV treprostinil; selexipag (oral IP agonist) reduces morbidity 40% (GRIPHON trial)."
  - target: 01-human/06-organ/lung
    relation: targets
    note: "PAH is a disease of the pulmonary vasculature; medial hypertrophy, intimal fibrosis, adventitial fibrosis, and plexiform lesions in pulmonary arterioles (<500 µm) → fixed obliterative vascular disease → RV pressure overload → cor pulmonale → right heart failure."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "SSc is the most common cause of CTD-PAH (10-15% of SSc patients); SSc-PAH treated with ERAs + PDE5i (macitentan, ambrisentan + tadalafil); worse prognosis than IPAH; annual echocardiographic screening recommended for all SSc patients."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Ang-1/Ang-2 imbalance in PAH: Ang-2 overexpression in pulmonary endothelium → Tie2 destabilization → endothelial mesenchymal transition → vascular remodeling; Ang-2 overexpressing mice develop PAH; plasma Ang-2 correlates with hemodynamic severity in PAH patients."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Activin A/B are elevated in PAH pulmonary vasculature; activin → VSMC ActRIIB/ALK4 → SMAD2/3 → proliferation and vasoconstriction → vascular remodeling; sotatercept (ActRIIB-Fc; FDA 2024) traps activin A/B → reverses vascular remodeling; STELLAR trial: +34.4 m 6MWD, p<0.001."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "PAH kills through the right heart: obliterated pulmonary arterioles raise vascular resistance until the thin-walled right ventricle, never built for high afterload, hypertrophies, dilates, and fails (cor pulmonale) — so RV function, not pulmonary pressure, best predicts survival."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Pulmonary endothelial dysfunction initiates PAH: injured endothelium underproduces vasodilators (NO, prostacyclin) and overproduces endothelin-1, and apoptosis-resistant clones form the plexiform lesions — so all three drug classes target endothelial signaling pathways."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Pulmonary artery smooth muscle cells drive PAH remodeling: under endothelin, activin, and growth-factor signaling they proliferate and resist apoptosis, thickening the media and muscularizing non-muscular arterioles — sotatercept (activin trap) reverses this remodeling."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Unresolved pulmonary emboli cause a distinct, surgically curable pulmonary hypertension: chronic thromboembolic PH (CTEPH) arises when organized clots obstruct and remodel pulmonary arteries, so every PAH workup includes a V/Q scan—CTEPH is cured by endarterectomy."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV is an established cause of pulmonary arterial hypertension: even with controlled viral loads, HIV proteins like Tat and Nef injure pulmonary endothelium and drive the same plexiform remodeling as idiopathic PAH, so HIV-PAH is a recognized WHO Group 1 subtype."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Pulmonary hypertension is a deadly complication of sickle cell disease: chronic hemolysis scavenges nitric oxide and releases free hemoglobin and arginase, so pulmonary vascular tone rises—an elevated tricuspid regurgitant jet marks patients at high mortality risk."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "PAH and juvenile polyposis converge on the BMP/TGF-β pathway: heritable PAH is most often caused by BMPR2 loss, and SMAD4/BMPR1A mutations can yield a combined JPS-HHT syndrome with PAH—BMP disruption linking gut polyps and pulmonary vascular disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "PAH ultimately kills through right heart failure: the thickened, narrowed pulmonary arteries raise resistance the right ventricle must pump against, so it hypertrophies, dilates and fails—right-heart function, not lung pressure alone, determines survival in PAH."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "PAH is a feared complication of connective-tissue disease, including lupus: immune-mediated injury remodels the pulmonary arteries, so SLE and systemic sclerosis patients are screened with echocardiography—CTD-associated PAH is a major cause of their mortality."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin drives pulmonary arterial hypertension: it constricts and remodels pulmonary arteries, and the appetite suppressants (fen-phen) that flooded the circulation with serotonin caused an epidemic of PAH—cementing the serotonin pathway as a disease driver."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia worsens pulmonary hypertension via a unique reflex: unlike systemic vessels, pulmonary arteries constrict when oxygen is low, so chronic hypoxia sustains vasoconstriction and vascular remodeling—why supplemental oxygen helps."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Pulmonary hypertension ultimately kills through the right ventricle: the right heart's cardiomyocytes hypertrophy then fail against the high pulmonary pressure, so cor pulmonale and right heart failure—not the lung itself—are the usual cause of death in PAH."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF marks the disordered vessels of pulmonary arterial hypertension: the plexiform lesions that obstruct small pulmonary arteries are foci of dysregulated VEGF-driven endothelial proliferation, reflecting how PAH is a vascular-remodeling, not just vasoconstrictive, disease."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Pulmonary arterial hypertension is the vascular disease of the respiratory system: remodeling of the lung's small arteries raises pulmonary pressure, so breathlessness and hypoxemia arise even though the airways and alveoli themselves may be normal."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Pulmonary arterial hypertension is a disease of the lesser circulation within the cardiovascular system: it raises pressure in the pulmonary arteries, not the systemic circuit, so its targeted vasodilators relax the lung's vessels rather than lowering body-wide pressure."
---

# Pulmonary Arterial Hypertension

## Overview

**Pulmonary arterial hypertension (PAH)** is a severe, progressive, and ultimately fatal disease of the **pulmonary vasculature** characterized by obliterative remodeling of small pulmonary arterioles, leading to increased pulmonary vascular resistance (PVR), right ventricular (RV) pressure overload, and — without treatment — RV failure and death [^galie-2015-esc-pah-guidelines].

**Updated hemodynamic definition (2018 World Symposium):**
- Mean pulmonary artery pressure (mPAP) **>20 mmHg** at rest (lowered from previous ≥25 mmHg)
- Pulmonary vascular resistance (PVR) **≥2 Wood Units** (corrected for normal post-capillary pressure)
- Pulmonary artery wedge pressure (PAWP) **≤15 mmHg** (distinguishes pre-capillary/arteriolar from post-capillary disease)
- Right heart catheterization (RHC) is the **gold standard** — required for definitive diagnosis

**WHO Clinical Classification of Pulmonary Hypertension (Group 1 = PAH):**

| Group | Etiology |
|:---|:---|
| **Group 1 (PAH)** | Idiopathic (IPAH), heritable (HPAH; BMPR2/BMP9), drug/toxin-induced (anorexigens), CTD (SSc most common), CHD (Eisenmenger), portal hypertension, HIV |
| Group 2 | Left heart disease (most common cause of PH overall) |
| Group 3 | Lung disease/hypoxia (COPD, IPF, OSA) |
| Group 4 | Chronic thromboembolic PH (CTEPH) |
| Group 5 | Multifactorial (sarcoidosis, myeloproliferative) |

**Epidemiology:**
- PAH (Group 1) prevalence: ~15-50 cases/million in Western countries; incidence 2-5/million/year
- **Gender:** Female predominance 2-4:1 in IPAH; female-to-male ratio narrows in HPAH (BMPR2 mutations)
- **Age:** Median age at diagnosis ~50 years (bimodal: young women for connective tissue disease PAH; older for IPAH)
- **Prognosis:** Without treatment, median survival 2.8 years from diagnosis (historical NIH registry); with modern combination therapy, 5-year survival ~60-70% in low/intermediate-risk patients
- **Systemic sclerosis (SSc-PAH):** PAH develops in 10-15% of SSc patients; worst prognosis of all PAH subgroups (5-year survival ~40-50%)

## Structure

### Pulmonary vascular pathobiology

**Three-layer vascular remodeling:**
1. **Intimal layer:** Endothelial cell proliferation + smooth muscle-like myofibroblast infiltration → eccentric intimal fibrosis → progressive luminal narrowing; **plexiform lesions** (pathognomonic): disorganized endothelial cell proliferation resembling a glomerulus — found in advanced IPAH/HPAH (not CTEPH)
2. **Medial layer:** Smooth muscle cell (SMC) hypertrophy and proliferation; abnormal extension of SMC into normally non-muscularized distal arterioles (<100 µm); driven by ET-1, PDGF, FGF-2
3. **Adventitial layer:** Fibroblast → myofibroblast activation; collagen deposition; pericyte loss; mast cell infiltration

**Three vasoactive pathway imbalances (the PAH triad):**
- **ET-1 excess:** Endothelial ET-1 production ↑ → ETA-mediated vasoconstriction + SMC proliferation; ETB-mediated endothelial clearance of ET-1 is also reduced (compound effect)
- **NO deficiency:** eNOS uncoupling + ↑PDE5 expression in pulmonary arteries → ↓cGMP → ↑vasoconstriction + proliferation; sGC expression also reduced
- **PGI2 deficiency:** ↓Prostacyclin synthase (PTGIS/CYP8A1) → ↓PGI2 → ↓IP receptor-cAMP signaling → ↑SMC proliferation + ↑platelet aggregation (thrombus in situ)

**BMPR2/BMP9 genetic axis (heritable PAH):**
- **BMPR2 (BMP receptor type 2):** Chromosome 2q33; ~75% of familial PAH and ~15-25% of IPAH carry pathogenic BMPR2 mutations (autosomal dominant, ~20% penetrance); BMPR2 → SMAD1/5/8 → ID1/2 target genes → anti-proliferative + anti-apoptotic programs in pulmonary endothelium; BMPR2 loss → endothelial apoptosis + SMC proliferation → PAH
- **BMP9 (GDF2; chr10q11.22):** Circulating BMP ligand for BMPR2; BMP9 mutations (loss-of-function) → PAH (classified as HPAH type 5); BMP9/BMPR2 axis is the primary anti-remodeling pathway in pulmonary endothelium
- Sotatercept (ActRIIA-Fc fusion; Merck): binds BMP9 ligand trap (traps activin A/B, ligands that compete with BMP9 for BMPR2) → restores BMPR2 pro-survival signaling; **STELLAR trial** (NEJM 2023): 38% improvement in 6MWD; first therapy showing modified RV remodeling; FDA-approved March 2024

**In situ thrombosis:** Platelet-rich microthrombi in small pulmonary arteries (platelet ↓PGI2 sensitivity + ↑TXA2) → contributes to vascular obliteration; anticoagulation historically recommended for IPAH/HPAH (current guidelines selective — not universal)

### Risk stratification (ESC/ERS 2022)

**Four-strata model (low/intermediate-low/intermediate-high/high risk):**
Key variables: WHO functional class (I-IV), 6-minute walk distance (6MWD), NT-proBNP/BNP, echocardiographic RV parameters, hemodynamics (PVR, CI, mRAP), and exercise capacity

**Low risk targets** (goal of therapy):
- WHO FC I-II
- 6MWD >440 m
- NT-proBNP <300 pg/mL (or BNP <50 pg/mL)
- Cardiac index ≥2.5 L/min/m²; mRAP <8 mmHg; PVR <4 WU
- No pericardial effusion

## Function

### Treatment — Three-pathway combination

**Initial combination therapy (standard of care for newly diagnosed treatment-naive WHO FC II-III):**

**ERA + PDE5i dual therapy:**
- **AMBITION trial:** Ambrisentan (ERA) + tadalafil (PDE5i) vs. either monotherapy → 50% reduction in clinical failure events at 24 weeks (primary endpoint); combination superior to monotherapy
- Now guideline-recommended as initial oral combination for most PAH patients

**Endothelin receptor antagonists (ERA):**
- **Ambrisentan (Letairis):** ETA-selective; 5-10 mg QD; FDA-approved 2007; ARIES-1/2 trials: +44 m 6MWD
- **Bosentan (Tracleer):** Dual ETA+ETB; 62.5-125 mg BID; FDA-approved 2001 (first oral PAH therapy); BREATHE-1: +54 m 6MWD; hepatotoxicity monitoring required monthly
- **Macitentan (Opsumit):** Dual ETA+ETB; highly lipophilic → tissue penetration; 10 mg QD; SERAPHIN trial: 45% reduction in morbidity/mortality composite (primary endpoint) vs. placebo

**PDE5 inhibitors:**
- **Sildenafil (Revatio):** 20 mg TID; inhibits PDE5 (predominant in pulmonary vasculature) → ↓cGMP degradation → ↑NO-mediated vasodilation; SUPER-1 trial: +45 m 6MWD
- **Tadalafil (Adcirca):** 40 mg QD; longer half-life (t½ 17.5h); PHIRST trial: +33 m 6MWD; preferred for daily dosing

**sGC stimulators:**
- **Riociguat (Adempas; Bayer):** Directly stimulates soluble guanylate cyclase (sGC) independent of NO and sensitizes sGC to endogenous NO → ↑cGMP; FDA-approved 2013 for both PAH and CTEPH (unique dual approval); PATENT-1 trial: +36 m 6MWD + significant PVR reduction; contraindicated with PDE5 inhibitors (additive hypotension risk)

**Prostacyclin pathway:**
- **Epoprostenol (Flolan, Veletri; IV PGI2):** Continuous IV infusion via tunneled catheter; t½ ~3-5 min (requires continuous pump); first PAH therapy to demonstrate mortality reduction (McLaughlin 2002); ORR ~80% in WHO FC III-IV; still gold standard for severe disease
- **Treprostinil (Remodulin; SC/IV; Orenitram; oral; Tyvaso; inhaled):** Chemically stable PGI2 analog; multiple formulations; subcutaneous infusion most common
- **Iloprost (Ventavis; inhaled):** 2.5-5 µg Q2-3h during waking hours; 6-9 inhalations/day
- **Selexipag (Uptravi; oral non-prostanoid IP receptor agonist):** [^sitbon-2015-selexipag-griphon]: IP receptor selectivity (avoids EP3 receptor — cardiac); GRIPHON trial (1156 patients, largest PAH outcome trial): 40% reduction in morbidity/mortality composite at a median ~1.4 years; FDA-approved Dec 2015; selexipag is a prodrug hydrolyzed to active MRE-269 (ACT-333679) — 37× more potent at IP receptor vs. selexipag

**Novel agents:**
- **Sotatercept (Winrevair; ActRIIA-Fc; Merck):** Trap for activin A/B → restoration of BMPR2/BMP9 → rebalanced pro/anti-proliferative signaling in pulmonary endothelium; STELLAR trial: +34.4 m 6MWD (mean difference vs. placebo); significant NT-proBNP reduction, PVR reduction; **FDA approval March 2024** for WHO FC II-III PAH; adds to ERAs + PDE5i
- **Ralinepag (oral IP agonist):** Phase 3 ADVANCE trial (vs. selexipag)

**Initial triple combination (WHO FC IV or rapid clinical deterioration):**
- ERA + PDE5i + IV epoprostenol; aggressive up-front approach in high-risk PAH
- Sequential addition vs. initial combination: AMBITION shows initial combination superior

**Lung transplantation:**
- For patients unresponsive to maximal combination therapy; bilateral sequential lung transplant preferred; 5-year survival ~50%; PAH recurs in 10-20% of transplanted lungs if immune-mediated mechanisms persist

### Supportive management

- **Supplemental O2:** Target SpO2 >92%; reduces hypoxic vasoconstriction (important in Group 3 overlap)
- **Diuretics:** For RV volume overload and edema; careful to avoid preload reduction impairing RV output
- **Digoxin:** Improves cardiac output in acute RV failure; limited evidence for chronic use
- **Supervised rehabilitation:** Exercise training (low-resistance aerobic) → improved 6MWD and QoL; safe in stable WHO FC II-III PAH

## Pathology

**RV failure (cor pulmonale):**
- Progressive PVR elevation → RV dilation and hypertrophy → tricuspid regurgitation → reduced cardiac output → systemic venous hypertension → ascites, edema, hepatic congestion
- **Pericardial effusion:** Present in 33-50% of advanced PAH; sign of poor prognosis; large effusions can cause tamponade
- RV failure is the primary cause of death in PAH; management: IV inotropy (milrinone, dobutamine), atrial septostomy (palliative; creates right-to-left shunt to decompress RV)

**CTEPH (Group 4) vs. PAH (Group 1):**
- CTEPH: organized thrombus and fibrous tissue obstruction of major pulmonary arteries; diagnosed by V/Q scan + CT pulmonary angiography; treatment: pulmonary endarterectomy (PEA; surgical — first-line for operable CTEPH), balloon pulmonary angioplasty (BPA for inoperable), riociguat (only approved medical therapy for CTEPH)
- Key distinction: PAH has plexiform lesions and microvascular disease; CTEPH has macrovascular organized thrombus

**Pulmonary veno-occlusive disease (PVOD) and PCH:**
- Rare subtypes of Group 1 PAH: PVOD (postcapillary component; pulmonary venous involvement); PCH (pulmonary capillary hemangiomatosis); both have BMPR2/EIF2AK4 mutations; prone to pulmonary edema with vasodilator therapy; poor prognosis; lung transplant recommended

## Connections

- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — ET-1 overproduction by PAH endothelium → ETA on pulmonary VSM → vasoconstriction + medial hypertrophy + adventitial fibrosis → elevated PVR; ERAs (bosentan, ambrisentan, macitentan) are first-line oral therapy for PAH; macitentan reduces morbidity/mortality 45% (SERAPHIN trial).
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Impaired eNOS and NO bioavailability in PAH endothelium → cGMP vasodilation failure; PDE5 inhibitors (sildenafil, tadalafil) prevent cGMP degradation → sustained vasodilation + anti-proliferative; sGC stimulators (riociguat) amplify NO-sGC-cGMP independent of endogenous NO.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — PAH endothelium produces insufficient PGI2 (prostacyclin) → IP receptor → cAMP → vasodilation and anti-proliferative; IV epoprostenol (Flolan) reduces mortality in severe PAH; inhaled iloprost, SC/IV treprostinil; selexipag (oral IP agonist) reduces morbidity 40% (GRIPHON trial).
- `targets` → **[Lung](../../06-organ/lung/README.md)** — PAH is a disease of the pulmonary vasculature; medial hypertrophy, intimal fibrosis, adventitial fibrosis, and plexiform lesions in pulmonary arterioles (<500 µm) → fixed obliterative vascular disease → RV pressure overload → cor pulmonale → right heart failure.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — SSc is the most common cause of CTD-PAH (10-15% of SSc patients); SSc-PAH treated with ERAs + PDE5i (macitentan, ambrisentan + tadalafil); worse prognosis than IPAH; annual echocardiographic screening recommended for all SSc patients.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-1/Ang-2 imbalance in PAH: Ang-2 overexpression in pulmonary endothelium → Tie2 destabilization → endothelial mesenchymal transition → vascular remodeling; Ang-2 overexpressing mice develop PAH; plasma Ang-2 correlates with hemodynamic severity in PAH patients.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Activin A/B are elevated in PAH pulmonary vasculature; activin → VSMC ActRIIB/ALK4 → SMAD2/3 → proliferation and vasoconstriction → vascular remodeling; sotatercept (ActRIIB-Fc; FDA 2024) traps activin A/B → reverses vascular remodeling; STELLAR trial: +34.4 m 6MWD, p<0.001.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — PAH kills through the right heart: obliterated pulmonary arterioles raise vascular resistance until the thin-walled right ventricle, never built for high afterload, hypertrophies, dilates, and fails (cor pulmonale) — so RV function, not pulmonary pressure, best predicts survival.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Pulmonary endothelial dysfunction initiates PAH: injured endothelium underproduces vasodilators (NO, prostacyclin) and overproduces endothelin-1, and apoptosis-resistant clones form the plexiform lesions — so all three drug classes target endothelial signaling pathways.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Pulmonary artery smooth muscle cells drive PAH remodeling: under endothelin, activin, and growth-factor signaling they proliferate and resist apoptosis, thickening the media and muscularizing non-muscular arterioles — sotatercept (activin trap) reverses this remodeling.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Unresolved pulmonary emboli cause a distinct, surgically curable pulmonary hypertension: chronic thromboembolic PH (CTEPH) arises when organized clots obstruct and remodel pulmonary arteries, so every PAH workup includes a V/Q scan—CTEPH is cured by endarterectomy.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is an established cause of pulmonary arterial hypertension: even with controlled viral loads, HIV proteins like Tat and Nef injure pulmonary endothelium and drive the same plexiform remodeling as idiopathic PAH, so HIV-PAH is a recognized WHO Group 1 subtype.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Pulmonary hypertension is a deadly complication of sickle cell disease: chronic hemolysis scavenges nitric oxide and releases free hemoglobin and arginase, so pulmonary vascular tone rises—an elevated tricuspid regurgitant jet marks patients at high mortality risk.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — PAH and juvenile polyposis converge on the BMP/TGF-β pathway: heritable PAH is most often caused by BMPR2 loss, and SMAD4/BMPR1A mutations can yield a combined JPS-HHT syndrome with PAH—BMP disruption linking gut polyps and pulmonary vascular disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — PAH ultimately kills through right heart failure: the thickened, narrowed pulmonary arteries raise resistance the right ventricle must pump against, so it hypertrophies, dilates and fails—right-heart function, not lung pressure alone, determines survival in PAH.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — PAH is a feared complication of connective-tissue disease, including lupus: immune-mediated injury remodels the pulmonary arteries, so SLE and systemic sclerosis patients are screened with echocardiography—CTD-associated PAH is a major cause of their mortality.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin drives pulmonary arterial hypertension: it constricts and remodels pulmonary arteries, and the appetite suppressants (fen-phen) that flooded the circulation with serotonin caused an epidemic of PAH—cementing the serotonin pathway as a disease driver.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia worsens pulmonary hypertension via a unique reflex: unlike systemic vessels, pulmonary arteries constrict when oxygen is low, so chronic hypoxia sustains vasoconstriction and vascular remodeling—why supplemental oxygen helps.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Pulmonary hypertension ultimately kills through the right ventricle: the right heart's cardiomyocytes hypertrophy then fail against the high pulmonary pressure, so cor pulmonale and right heart failure—not the lung itself—are the usual cause of death in PAH.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF marks the disordered vessels of pulmonary arterial hypertension: the plexiform lesions that obstruct small pulmonary arteries are foci of dysregulated VEGF-driven endothelial proliferation, reflecting how PAH is a vascular-remodeling, not just vasoconstrictive, disease.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Pulmonary arterial hypertension is the vascular disease of the respiratory system: remodeling of the lung's small arteries raises pulmonary pressure, so breathlessness and hypoxemia arise even though the airways and alveoli themselves may be normal.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Pulmonary arterial hypertension is a disease of the lesser circulation within the cardiovascular system: it raises pressure in the pulmonary arteries, not the systemic circuit, so its targeted vasodilators relax the lung's vessels rather than lowering body-wide pressure.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^galie-2015-esc-pah-guidelines]: Galie N, Humbert M, Vachiery JL, et al. 2015 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. *Eur Heart J.* 2016;37(1):67-119. [doi:10.1093/eurheartj/ehv317](https://doi.org/10.1093/eurheartj/ehv317) · [PubMed 26320113](https://pubmed.ncbi.nlm.nih.gov/26320113/)
[^simonneau-2019-pah-classification]: Simonneau G, Montani D, Celermajer DS, et al. Haemodynamic definitions and updated clinical classification of pulmonary hypertension. *Eur Respir J.* 2019;53(1):1801913. [doi:10.1183/13993003.01913-2018](https://doi.org/10.1183/13993003.01913-2018) · [PubMed 30545968](https://pubmed.ncbi.nlm.nih.gov/30545968/)
[^sitbon-2015-selexipag-griphon]: Sitbon O, Channick R, Chin KM, et al. Selexipag for the Treatment of Pulmonary Arterial Hypertension. *N Engl J Med.* 2015;373(26):2522-2533. [doi:10.1056/NEJMoa1503184](https://doi.org/10.1056/NEJMoa1503184) · [PubMed 26579977](https://pubmed.ncbi.nlm.nih.gov/26579977/)
