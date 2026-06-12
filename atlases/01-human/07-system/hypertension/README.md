---
schema: human-scale-entry/v1
id: hypertension
name: Hypertension
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Sustained BP ≥130/80 mmHg (AHA 2017); 1.28 billion adults globally. Primary (~95%): RAAS overactivation, sympathetic excess, endothelial NO deficiency. Complications: stroke, MI, HFpEF, CKD. First-line: ACE-I/ARBs, thiazides, CCBs."
aliases: ["hypertension", "high blood pressure", "HTN", "arterial hypertension", "essential hypertension"]
sources:
  - id: whelton-2018-acc-aha
    type: peer-reviewed
    cite: "Whelton PK, Carey RM, Aronow WS, et al. 2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Hypertension. 2018;71(6):e13-e115."
    doi: "10.1161/HYP.0000000000000065"
    pmid: "29133356"
    url: "https://doi.org/10.1161/HYP.0000000000000065"
  - id: mills-2020-global-hypertension
    type: peer-reviewed
    cite: "Mills KT, Stefanescu A, He J. The global epidemiology of hypertension. Nat Rev Nephrol. 2020;16(4):223-237."
    doi: "10.1038/s41581-019-0244-2"
    pmid: "32024986"
    url: "https://doi.org/10.1038/s41581-019-0244-2"
cross_links:
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "Hypertension causes hypertensive nephrosclerosis via afferent arteriole wall thickening and glomerular ischemia; simultaneously, the kidney's RAAS activation and impaired pressure-natriuresis are key drivers of hypertension — a bidirectional relationship."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: modulated-by
    note: "Angiotensin II is the central effector of RAAS: causes vasoconstriction via AT1R on vascular smooth muscle, stimulates aldosterone release, promotes renal sodium retention, drives cardiac hypertrophy, and promotes endothelial dysfunction via ROS generation."
  - target: 01-human/03-molecular/aldosterone
    relation: modulated-by
    note: "Aldosterone (produced by adrenal zona glomerulosa under Ang II/K+ stimulation) acts on renal distal tubule/collecting duct to increase ENaC-mediated Na+ retention and K+ excretion, expanding plasma volume and raising BP."
  - target: 01-human/04-cellular/endothelial-cell
    relation: modulates
    note: "Endothelial dysfunction is both a cause and consequence of hypertension: reduced eNOS activity lowers NO bioavailability, impairs vasodilation, and promotes vascular remodeling; hypertensive shear stress further injures endothelial cells, perpetuating the cycle."
  - target: 01-human/03-molecular/renin
    relation: modulated-by
    note: "Renin is the rate-limiting enzyme of the RAAS: released from JG cells in response to reduced perfusion, low macula densa NaCl, and β1-adrenergic stimulation → angiotensinogen → Ang I → Ang II; aliskiren (direct renin inhibitor) reduces BP; ARR screens for primary aldosteronism."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "ET-1 is the most potent vasoconstrictor and is elevated in resistant hypertension, CKD-related hypertension, and preeclampsia; ETA receptor on vascular smooth muscle → vasoconstriction; ETB receptor on endothelium → NO and PGI2 (counterbalances); dual ERA bosentan lowers BP."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Hypertension accelerates DR through retinal arteriolar pressure, shear stress, and RAAS activation; BP control to <130/80 mmHg reduces DR progression by ~30% (UKPDS); hypertensive retinopathy and DR frequently coexist and share pathophysiology."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Hypertension and gout reinforce each other: elevated urate raises blood pressure by impairing endothelial NO and activating the RAAS, while thiazide and loop diuretics for hypertension reduce renal urate excretion and trigger gout flares — so drug choice must be coordinated."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Hypertension is the most important modifiable risk factor for stroke: chronic high pressure drives both ischemic stroke (atherosclerosis, small-vessel lipohyalinosis) and hemorrhagic stroke (Charcot-Bouchard microaneurysm rupture); each 10 mmHg drop cuts stroke risk by ~a third."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Dietary sodium is the leading modifiable driver of hypertension: excess salt expands extracellular volume and, in salt-sensitive people, raises blood pressure via impaired renal sodium handling; cutting intake toward <2 g/day lowers BP — the basis of DASH and salt-restriction."
---

# Hypertension

## Overview

Hypertension is the **most prevalent modifiable cardiovascular risk factor** globally, affecting approximately 1.28 billion adults in 2019 — nearly one-third of the global adult population — and directly causing an estimated 10.8 million deaths annually through cardiovascular disease, stroke, and kidney failure [^mills-2020-global-hypertension]. Despite effective pharmacological treatments, control rates remain below 25% in many regions.

The AHA/ACC 2017 guidelines [^whelton-2018-acc-aha] define hypertension as sustained systolic BP **≥130 mmHg** or diastolic BP **≥80 mmHg** (measured correctly on 2+ occasions). This threshold, lowered from the previous 140/90 mmHg, reflects the continuous cardiovascular risk relationship: for every 20 mmHg increase in systolic BP above 115 mmHg, risk of cardiovascular death doubles.

**Classification (AHA 2017):**
| Stage | SBP | DBP |
|:---|:---|:---|
| Normal | <120 | <80 |
| Elevated | 120–129 | <80 |
| Stage 1 HTN | 130–139 | 80–89 |
| Stage 2 HTN | ≥140 | ≥90 |
| Hypertensive crisis | >180 | >120 |

## Structure

### Vascular Changes in Hypertension

Sustained elevated pressure drives **structural adaptation** of the vasculature — collectively termed **hypertensive vascular remodeling**:

**Large arteries (aorta, carotids):**
- Increased wall stiffness — loss of elastic fiber compliance; increased collagen deposition in medial layer
- Reduced Windkessel function → elevated pulse wave velocity → increased systolic BP and pulse pressure
- Accelerated atherosclerosis — endothelial dysfunction, increased LDL oxidation and subendothelial accumulation

**Small arteries and arterioles (resistance vessels):**
- **Inward eutrophic remodeling** — same wall mass rearranged around smaller lumen (wall/lumen ratio ↑)
- In severe/chronic hypertension: **hypertrophic remodeling** — increased wall mass via smooth muscle cell hypertrophy
- These changes fix peripheral vascular resistance at an elevated set point even if systemic BP is pharmacologically normalized

**Microcirculation:**
- Arteriolar rarefaction — reduced capillary density (both functional and structural)
- Contributes to insulin resistance (impaired muscle glucose delivery) and target organ ischemia

### End-Organ Architecture Changes

| Organ | Structural change |
|:---|:---|
| **Heart** | Left ventricular hypertrophy (concentric LVH, increased wall:cavity ratio) — response to increased afterload |
| **Kidney** | Afferent arteriole hyalinosis; glomerulosclerosis; tubular atrophy |
| **Brain** | White matter lacunar infarcts (small vessel disease); arterial microaneurysms (Charcot-Bouchard) |
| **Eye** | Arteriolar narrowing, AV nicking, copper/silver wiring; cotton wool spots; papilledema in malignant HTN |

## Function

### Regulatory Systems Governing BP

Blood pressure is determined by: BP = Cardiac Output × Peripheral Vascular Resistance. Both components are dysregulated in hypertension:

**RAAS (Renin-Angiotensin-Aldosterone System):**
- **Renin** (juxtaglomerular cells): cleaves angiotensinogen → angiotensin I (Ang I)
- **ACE** (lung endothelium): Ang I → Ang II
- **Ang II effects**: AT1R → vasoconstriction + aldosterone release + ADH stimulation + sympathetic activation + renal Na/H₂O retention + cardiac/vascular hypertrophy
- In **primary aldosteronism** (most common secondary cause): autonomous aldosterone → Na+ retention → volume-dependent HTN

**Sympathetic Nervous System:**
- Increased sympathetic tone → increased heart rate and contractility (CO ↑) + peripheral vasoconstriction (PVR ↑)
- Chronic sympathetic overactivation in hypertension demonstrated by muscle sympathetic nerve activity (MSNA) recordings

**Renal Pressure-Natriuresis:**
- Normally: BP rise → pressure natriuresis → Na+ and water excretion → BP returns to normal
- In hypertension: pressure-natriuresis relationship is reset at a higher BP operating point — requires higher pressure to achieve the same Na+ excretion; driven by RAAS, aldosterone, renal structural changes

**Endothelial Dysfunction:**
- Reduced eNOS activity and NO bioavailability → impaired vasodilation; increased ET-1 production → vasoconstriction
- Oxidative stress (Ang II → NADPH oxidase → superoxide) scavenges NO → further NO depletion

### Primary vs. Secondary Hypertension

**Primary (essential) hypertension** (~95%): polygenic + environmental; key contributors:
- RAAS genetic variants (ACE gene insertion/deletion, AGT M235T, renin-binding protein polymorphisms)
- Salt sensitivity (variants in ENaC, WNK kinase pathway, 11β-HSD2)
- Obesity-related: increased RAAS, sympathetic tone, and mechanical compression of kidneys
- Chronic stress and hypothalamic sympathetic dysregulation

**Secondary hypertension** (~5%): identifiable cause:
| Cause | Features | Mechanism |
|:---|:---|:---|
| Primary aldosteronism | Hypokalemia, low PRA, high aldosterone | Autonomous aldosterone secretion (adenoma or bilateral hyperplasia) |
| Renovascular disease | Flash pulmonary edema, abdominal bruit | Renal artery stenosis → RAAS activation |
| Pheochromocytoma | Paroxysmal HTN, headache, sweating, palpitations | Catecholamine excess |
| CKD | Renal markers, bilateral small kidneys | Impaired Na excretion + RAAS activation |
| Obstructive sleep apnea | Obesity, nocturnal desaturations | Hypoxia → sympathetic activation |
| Cushing's syndrome | Central obesity, striae, cortisol excess | Glucocorticoid activation of mineralocorticoid receptors |

## Connections

- `modulates` → **[Kidney](../../06-organ/kidney/README.md)** — hypertension drives hypertensive nephrosclerosis and CKD; kidney RAAS dysregulation is a key hypertension driver
- `modulated-by` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — central RAAS effector driving vasoconstriction, aldosterone release, and vascular remodeling
- `modulated-by` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — promotes sodium retention and volume expansion; primary aldosteronism is the most common secondary cause of hypertension
- `modulates` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — hypertensive shear stress damages endothelium; endothelial NO deficiency sustains elevated BP
- `modulated-by` → **[Renin](../../03-molecular/renin/README.md)** — Renin is the rate-limiting enzyme of the RAAS: released from JG cells in response to reduced perfusion, low macula densa NaCl, and β1-adrenergic stimulation → angiotensinogen → Ang I → Ang II; aliskiren (direct renin inhibitor) reduces BP; ARR screens for primary aldosteronism.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — ET-1 is the most potent vasoconstrictor and is elevated in resistant hypertension, CKD-related hypertension, and preeclampsia; ETA receptor on vascular smooth muscle → vasoconstriction; ETB receptor on endothelium → NO and PGI2 (counterbalances); dual ERA bosentan lowers BP.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Hypertension accelerates DR through retinal arteriolar pressure, shear stress, and RAAS activation; BP control to <130/80 mmHg reduces DR progression by ~30% (UKPDS); hypertensive retinopathy and DR frequently coexist and share pathophysiology.
- `connects-to` → **[Gout](../gout/README.md)** — Hypertension and gout reinforce each other: elevated urate raises blood pressure by impairing endothelial NO and activating the RAAS, while thiazide and loop diuretics for hypertension reduce renal urate excretion and trigger gout flares — so drug choice must be coordinated.
- `connects-to` → **[Stroke](../stroke/README.md)** — Hypertension is the most important modifiable risk factor for stroke: chronic high pressure drives both ischemic stroke (atherosclerosis, small-vessel lipohyalinosis) and hemorrhagic stroke (Charcot-Bouchard microaneurysm rupture); each 10 mmHg drop cuts stroke risk by ~a third.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Dietary sodium is the leading modifiable driver of hypertension: excess salt expands extracellular volume and, in salt-sensitive people, raises blood pressure via impaired renal sodium handling; cutting intake toward <2 g/day lowers BP — the basis of DASH and salt-restriction.

## Pathology

### Cardiovascular Complications

Hypertension drives a spectrum of cardiovascular diseases through mechanical stress and neurohumoral activation:

**Left Ventricular Hypertrophy (LVH):**
- Concentric LVH (increased wall:cavity ratio) in chronic pressure overload
- LVH is an independent cardiovascular risk factor (beyond BP itself); associated with diastolic dysfunction → HFpEF
- Regression of LVH with BP control reduces mortality

**Coronary Artery Disease:**
- Accelerated atherosclerosis (endothelial injury → lipid accumulation → plaque → ACS)
- Hypertension doubles MI risk; the population-attributable fraction of MI from hypertension is ~35%

**Stroke:**
- Hypertension is the strongest modifiable stroke risk factor; risk is ~4-fold for ischemic, ~10-fold for hemorrhagic stroke vs. normotension
- Lacunar infarcts: small vessel disease → fibrinoid necrosis of penetrating arteries → deep white matter infarcts
- Intracerebral hemorrhage: Charcot-Bouchard microaneurysm rupture in basal ganglia/pons/cerebellum

**Heart Failure:**
- HFpEF: LVH → diastolic dysfunction → elevated filling pressures → pulmonary congestion with preserved EF
- HFrEF: chronic pressure overload → myocyte apoptosis + fibrosis → systolic dysfunction

**CKD and ESRD:**
- Hypertensive nephrosclerosis: afferent arteriole injury → glomerular ischemia → glomerulosclerosis → proteinuria → ESRD
- Hypertension is the second leading cause of ESRD (after diabetes) globally

### Hypertensive Crisis

**Hypertensive urgency** (SBP >180 or DBP >120, without end-organ damage): gradual oral BP lowering over 24–48 hours.

**Hypertensive emergency** (severe HTN + acute end-organ damage): IV therapy with target of reducing MAP by ≤25% in first hour, then to 160/100 over next 2–6 hours:
- Encephalopathy/stroke: labetalol, nicardipine (avoid nitroprusside)
- Acute MI: nitroglycerine, beta-blockade
- Aortic dissection: esmolol + nitroprusside (target SBP <120 within minutes)
- Pulmonary edema: nitroglycerine, loop diuretics
- Eclampsia: magnesium + hydralazine/labetalol

[^whelton-2018-acc-aha]: Whelton PK et al. 2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. *Hypertension.* 2018;71(6):e13-e115. [doi:10.1161/HYP.0000000000000065](https://doi.org/10.1161/HYP.0000000000000065) · [PubMed 29133356](https://pubmed.ncbi.nlm.nih.gov/29133356/)
[^mills-2020-global-hypertension]: Mills KT, Stefanescu A, He J. The global epidemiology of hypertension. *Nat Rev Nephrol.* 2020;16(4):223-237. [doi:10.1038/s41581-019-0244-2](https://doi.org/10.1038/s41581-019-0244-2) · [PubMed 32024986](https://pubmed.ncbi.nlm.nih.gov/32024986/)
