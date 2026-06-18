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
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart is a principal victim of hypertension: chronic pressure overload drives left-ventricular hypertrophy, diastolic then systolic heart failure, atrial fibrillation and—via accelerated coronary disease—myocardial infarction; blood-pressure control best prevents these."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Hypertension and CKD are locked in a vicious cycle: high pressure damages glomeruli (nephrosclerosis) while failing kidneys retain sodium and activate renin-angiotensin to raise pressure; ACE inhibitors/ARBs break the loop and are first-line in hypertensive CKD."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Hypertension is a major driver of atherosclerosis: elevated pressure and shear stress injure the endothelium and accelerate plaque formation throughout the arterial tree, so treating blood pressure reduces myocardial infarction, stroke and peripheral arterial disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Hypertension is the leading cause of heart failure: chronic pressure overload forces the left ventricle to hypertrophy, then stiffen and fail (HFpEF) or dilate (HFrEF)—decades of high afterload remodel the heart, so controlling pressure best prevents it."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Pheochromocytoma is a classic curable cause of secondary hypertension: a catecholamine-secreting adrenal tumor drives paroxysmal high blood pressure with headache, sweating and palpitations, so resistant or episodic hypertension warrants screening—surgery can cure it."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium is the dietary counterweight to sodium in blood pressure: higher potassium intake promotes natriuresis and vasodilation, lowering pressure, while hypokalemia—often from hyperaldosteronism—signals a secondary, treatable cause of hypertension."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide failure underlies much hypertension: healthy endothelium releases NO to relax arteries, so when endothelial dysfunction cuts NO, vessels stay constricted and pressure rises—linking early vascular injury to sustained high blood pressure."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Hypertension is the leading driver of cardiovascular disease: chronic high pressure damages arteries throughout the body, accelerating atherosclerosis and straining the heart, so controlling it prevents the strokes, heart attacks and kidney failure it causes."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium handling is a key hypertension lever: calcium influx contracts vascular smooth muscle to raise pressure, which is why calcium-channel blockers are first-line antihypertensives—relaxing arteries by blocking the calcium that drives their tone."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Hypertension is driven by vascular smooth muscle: arteriolar smooth-muscle tone sets peripheral resistance, and chronic high pressure thickens these cells, stiffening vessels—so smooth-muscle relaxation is the target of calcium-channel blockers and vasodilators."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The renal system is both cause and victim of hypertension: the kidney sets long-term blood pressure through salt and renin handling, so renal disease raises pressure while sustained hypertension damages the kidney—a self-amplifying vicious loop."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Norepinephrine and sympathetic drive raise blood pressure: catecholamines constrict vessels and speed the heart, so overactive sympathetic tone elevates pressure—the rationale for beta-blockers and alpha-blockers and the cause of surges in pheochromocytoma."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "The adrenal gland causes curable secondary hypertension: primary aldosteronism (Conn's), cortisol excess (Cushing's), and pheochromocytoma each drive high blood pressure, so resistant or young-onset hypertension prompts a hunt for an adrenal cause."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Hypertension in pregnancy centers on the placenta: poor placental perfusion releases factors that injure maternal blood vessels, causing pre-eclampsia—high blood pressure with organ damage that endangers mother and baby and resolves only with delivery."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome helps set blood pressure: microbes ferment fiber into short-chain fatty acids that relax vessels and modulate salt handling, so dysbiosis is emerging as a factor in hypertension beyond diet and genetics."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "The heart fights hypertension by releasing BNP: when high pressure stretches the heart, it secretes natriuretic peptide to make the kidneys dump sodium and relax vessels—a built-in counterweight to high blood pressure that doctors also measure to gauge cardiac strain."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium helps set blood pressure: the mineral relaxes vascular smooth muscle and counters calcium-driven constriction, so magnesium deficiency tightens vessels while supplementing it modestly lowers blood pressure."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance drives hypertension: high insulin levels make the kidney retain sodium and rev up the sympathetic nervous system, which is why high blood pressure clusters with obesity and diabetes in the metabolic syndrome."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain both controls and suffers from blood pressure: brainstem centers set the sympathetic tone that drives it, while severe hypertension damages cerebral vessels to cause stroke and hypertensive encephalopathy—a two-way street."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol raises blood pressure: it sensitizes vessels to constrictors and makes the kidney hold sodium, so excess—from Cushing's or chronic stress—causes hypertension, one reason endocrine causes are sought in resistant cases."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T-helper cells are an emerging player in hypertension: activated T cells infiltrate the vessel wall and kidney, releasing cytokines that stiffen arteries and impair sodium handling, recasting high blood pressure partly as an inflammatory disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Hypertension is read in the eye: high pressure narrows and damages retinal vessels (hypertensive retinopathy), a visible window onto the systemic vascular harm the disease does everywhere."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Hypertension stiffens organs with fibrosis: sustained pressure drives the heart and arteries to lay down collagen, thickening and scarring the walls, a remodeling that worsens the disease and damages the kidney too."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Hypertension forces cardiomyocytes to grow: pumping against high pressure makes heart-muscle cells enlarge, thickening the left ventricle into hypertensive heart disease that eventually stiffens and fails."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging hunts secondary and end-organ hypertension: CT and MR angiography photons find renal-artery stenosis and adrenal tumors, while echocardiography measures the thickened, straining heart."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Hypertension has an immune side: macrophages infiltrate the kidney and vessel walls, and the salt they help handle and the inflammation they drive contribute to the rise in blood pressure."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Hypertension is partly a nerve disease: overactive sympathetic peripheral nerves drive up the pressure, which is why renal denervation—burning the kidney's nerves—is a treatment for resistant cases."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows how pressure remodels the arteries: chronic hypertension thickens small-vessel walls with glassy hyaline deposits and muscle overgrowth, and in malignant disease the wall undergoes fibrinoid necrosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Hypertension's vascular damage can starve the bowel: hardened, narrowed mesenteric arteries make the gut prone to ischemic colitis, especially when blood pressure suddenly drops in an already-diseased circulation."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Untreated hypertension floods the lungs: as the pressure-strained left ventricle stiffens and fails, blood backs up into the pulmonary vessels, causing the breathlessness and flash pulmonary edema of hypertensive heart disease."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Blood pressure touches reproduction at both ends: it underlies preeclampsia and pregnancy hypertension that endanger mother and fetus, and chronic hypertension and its drugs are common causes of erectile dysfunction."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "A pressure spike can overwhelm the brain: in a hypertensive emergency, autoregulation fails and fluid leaks around neurons into hypertensive encephalopathy and the posterior reversible encephalopathy syndrome (PRES), with headache, confusion, and seizures."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid is a fixable cause: hyperthyroidism raises systolic pressure and the pulse, while hypothyroidism stiffens vessels into a diastolic hypertension, so thyroid function is checked when secondary hypertension is sought."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "High pressure shears the kidney's filter cells: chronic hypertension batters the glomerular podocytes, and as these hard-to-replace cells detach, protein leaks into the urine and nephrosclerosis sets in — a main route by which hypertension drives chronic kidney disease."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Midlife hypertension is a leading modifiable risk for dementia: years of high pressure damage small cerebral vessels, starving the brain and adding vascular injury that hastens cognitive decline and Alzheimer's, so blood-pressure control helps protect the aging brain."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Vasopressin nudges pressure up two ways: the pituitary hormone constricts vessels through V1 receptors and makes the kidney retain water through V2, expanding volume — a lesser arm of blood-pressure control beyond the renin-angiotensin system."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Excess weight is a leading driver of high pressure: obesity raises blood volume, sympathetic tone, and aldosterone while compressing the kidneys, so weight gain accounts for much of the hypertension in rich and rising populations."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Hypertension has an immune arm: CD8 cytotoxic T cells infiltrate the kidney and vessel wall and sustain the salt retention and vascular inflammation that keep blood pressure high, a mechanism that reframes part of the disease as immune-driven."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Adrenaline drives the pressure surges: epinephrine from sympathetic activation and the adrenal medulla speeds the heart and constricts vessels, behind stress-related spikes and the extreme swings of pheochromocytoma."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Hypertension and diabetes travel as a metabolic pair: shared insulin resistance links them, they co-occur in metabolic syndrome, and together they multiply the risk of the kidney, heart, and stroke disease each causes."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Fat cells push the pressure up: visceral adipocytes secrete angiotensinogen, leptin, and inflammatory adipokines while activating the sympathetic nervous system, a key link between obesity and hypertension."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Hypertension has an inflammasome arm: NLRP3 activation and the IL-1β it releases promote the vascular and renal inflammation that sustains high blood pressure, part of the immune contribution to the disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Angiotensin II inflames the vessel through NF-κB: it activates NF-κB in vascular and renal cells to drive the cytokines and oxidative stress that stiffen arteries, the inflammatory engine upstream of the NLRP3 arm of hypertension."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Poor sleep pushes the pressure up: insomnia and short sleep raise sympathetic tone and blunt the normal nocturnal dip, and obstructive sleep apnea is a leading cause of resistant hypertension."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "It shares its soil with venous clots: hypertension clusters with the metabolic and vascular risk factors of venous thromboembolism, and the two are modestly associated beyond their common arterial disease."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "The link runs both ways with the kidney's cancer: hypertension is an established risk factor for renal cell carcinoma, while the tumor's renin secretion and renal damage in turn cause secondary hypertension."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Small-vessel damage muddies the movement disorder: midlife hypertension drives the cerebral small-vessel disease behind vascular parkinsonism, which mimics and worsens Parkinson's, and orthostatic swings complicate its management."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Pressure and mood interact: depression is more common in hypertension and worsens adherence and outcomes, while chronic stress and some antihypertensives influence mood, a clinically important two-way link."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety and blood pressure feed each other: chronic anxiety and sympathetic arousal acutely raise blood pressure, and living with hypertension breeds health anxiety — a bidirectional, clinically relevant link."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "It clusters with fatty-liver disease: hypertension is a core component of the metabolic syndrome that drives NASH, the two coexisting through shared insulin resistance and visceral adiposity."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Through the kidney it lowers the blood count: hypertensive nephrosclerosis is a leading cause of chronic kidney disease, and the failing kidney's loss of erythropoietin produces a renal anemia."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones cause and control blood pressure: secondary hypertension arises from primary aldosteronism, Cushing's, thyroid disease and phaeochromocytoma, and the RAAS that drives it is an endocrine axis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Severe spikes injure the brain: a hypertensive emergency causes encephalopathy and posterior reversible encephalopathy syndrome, and chronic hypertension is the leading cause of intracerebral haemorrhage."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Sleep-disordered breathing drives it up: obstructive sleep apnoea, with its nocturnal hypoxia and sympathetic surges, is a major reversible cause of resistant hypertension."
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
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart is a principal victim of hypertension: chronic pressure overload drives left-ventricular hypertrophy, diastolic then systolic heart failure, atrial fibrillation and—via accelerated coronary disease—myocardial infarction; blood-pressure control best prevents these.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Hypertension and CKD are locked in a vicious cycle: high pressure damages glomeruli (nephrosclerosis) while failing kidneys retain sodium and activate renin-angiotensin to raise pressure; ACE inhibitors/ARBs break the loop and are first-line in hypertensive CKD.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Hypertension is a major driver of atherosclerosis: elevated pressure and shear stress injure the endothelium and accelerate plaque formation throughout the arterial tree, so treating blood pressure reduces myocardial infarction, stroke and peripheral arterial disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Hypertension is the leading cause of heart failure: chronic pressure overload forces the left ventricle to hypertrophy, then stiffen and fail (HFpEF) or dilate (HFrEF)—decades of high afterload remodel the heart, so controlling pressure best prevents it.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Pheochromocytoma is a classic curable cause of secondary hypertension: a catecholamine-secreting adrenal tumor drives paroxysmal high blood pressure with headache, sweating and palpitations, so resistant or episodic hypertension warrants screening—surgery can cure it.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium is the dietary counterweight to sodium in blood pressure: higher potassium intake promotes natriuresis and vasodilation, lowering pressure, while hypokalemia—often from hyperaldosteronism—signals a secondary, treatable cause of hypertension.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide failure underlies much hypertension: healthy endothelium releases NO to relax arteries, so when endothelial dysfunction cuts NO, vessels stay constricted and pressure rises—linking early vascular injury to sustained high blood pressure.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Hypertension is the leading driver of cardiovascular disease: chronic high pressure damages arteries throughout the body, accelerating atherosclerosis and straining the heart, so controlling it prevents the strokes, heart attacks and kidney failure it causes.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium handling is a key hypertension lever: calcium influx contracts vascular smooth muscle to raise pressure, which is why calcium-channel blockers are first-line antihypertensives—relaxing arteries by blocking the calcium that drives their tone.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Hypertension is driven by vascular smooth muscle: arteriolar smooth-muscle tone sets peripheral resistance, and chronic high pressure thickens these cells, stiffening vessels—so smooth-muscle relaxation is the target of calcium-channel blockers and vasodilators.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The renal system is both cause and victim of hypertension: the kidney sets long-term blood pressure through salt and renin handling, so renal disease raises pressure while sustained hypertension damages the kidney—a self-amplifying vicious loop.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Norepinephrine and sympathetic drive raise blood pressure: catecholamines constrict vessels and speed the heart, so overactive sympathetic tone elevates pressure—the rationale for beta-blockers and alpha-blockers and the cause of surges in pheochromocytoma.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — The adrenal gland causes curable secondary hypertension: primary aldosteronism (Conn's), cortisol excess (Cushing's), and pheochromocytoma each drive high blood pressure, so resistant or young-onset hypertension prompts a hunt for an adrenal cause.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Hypertension in pregnancy centers on the placenta: poor placental perfusion releases factors that injure maternal blood vessels, causing pre-eclampsia—high blood pressure with organ damage that endangers mother and baby and resolves only with delivery.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome helps set blood pressure: microbes ferment fiber into short-chain fatty acids that relax vessels and modulate salt handling, so dysbiosis is emerging as a factor in hypertension beyond diet and genetics.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — The heart fights hypertension by releasing BNP: when high pressure stretches the heart, it secretes natriuretic peptide to make the kidneys dump sodium and relax vessels—a built-in counterweight to high blood pressure that doctors also measure to gauge cardiac strain.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium helps set blood pressure: the mineral relaxes vascular smooth muscle and counters calcium-driven constriction, so magnesium deficiency tightens vessels while supplementing it modestly lowers blood pressure.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance drives hypertension: high insulin levels make the kidney retain sodium and rev up the sympathetic nervous system, which is why high blood pressure clusters with obesity and diabetes in the metabolic syndrome.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain both controls and suffers from blood pressure: brainstem centers set the sympathetic tone that drives it, while severe hypertension damages cerebral vessels to cause stroke and hypertensive encephalopathy—a two-way street.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol raises blood pressure: it sensitizes vessels to constrictors and makes the kidney hold sodium, so excess—from Cushing's or chronic stress—causes hypertension, one reason endocrine causes are sought in resistant cases.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T-helper cells are an emerging player in hypertension: activated T cells infiltrate the vessel wall and kidney, releasing cytokines that stiffen arteries and impair sodium handling, recasting high blood pressure partly as an inflammatory disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Hypertension is read in the eye: high pressure narrows and damages retinal vessels (hypertensive retinopathy), a visible window onto the systemic vascular harm the disease does everywhere.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Hypertension stiffens organs with fibrosis: sustained pressure drives the heart and arteries to lay down collagen, thickening and scarring the walls, a remodeling that worsens the disease and damages the kidney too.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Hypertension forces cardiomyocytes to grow: pumping against high pressure makes heart-muscle cells enlarge, thickening the left ventricle into hypertensive heart disease that eventually stiffens and fails.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging hunts secondary and end-organ hypertension: CT and MR angiography photons find renal-artery stenosis and adrenal tumors, while echocardiography measures the thickened, straining heart.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Hypertension has an immune side: macrophages infiltrate the kidney and vessel walls, and the salt they help handle and the inflammation they drive contribute to the rise in blood pressure.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Hypertension is partly a nerve disease: overactive sympathetic peripheral nerves drive up the pressure, which is why renal denervation—burning the kidney's nerves—is a treatment for resistant cases.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows how pressure remodels the arteries: chronic hypertension thickens small-vessel walls with glassy hyaline deposits and muscle overgrowth, and in malignant disease the wall undergoes fibrinoid necrosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Hypertension's vascular damage can starve the bowel: hardened, narrowed mesenteric arteries make the gut prone to ischemic colitis, especially when blood pressure suddenly drops in an already-diseased circulation.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Untreated hypertension floods the lungs: as the pressure-strained left ventricle stiffens and fails, blood backs up into the pulmonary vessels, causing the breathlessness and flash pulmonary edema of hypertensive heart disease.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Blood pressure touches reproduction at both ends: it underlies preeclampsia and pregnancy hypertension that endanger mother and fetus, and chronic hypertension and its drugs are common causes of erectile dysfunction.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — A pressure spike can overwhelm the brain: in a hypertensive emergency, autoregulation fails and fluid leaks around neurons into hypertensive encephalopathy and the posterior reversible encephalopathy syndrome (PRES), with headache, confusion, and seizures.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid is a fixable cause: hyperthyroidism raises systolic pressure and the pulse, while hypothyroidism stiffens vessels into a diastolic hypertension, so thyroid function is checked when secondary hypertension is sought.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — High pressure shears the kidney's filter cells: chronic hypertension batters the glomerular podocytes, and as these hard-to-replace cells detach, protein leaks into the urine and nephrosclerosis sets in — a main route by which hypertension drives chronic kidney disease.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Midlife hypertension is a leading modifiable risk for dementia: years of high pressure damage small cerebral vessels, starving the brain and adding vascular injury that hastens cognitive decline and Alzheimer's, so blood-pressure control helps protect the aging brain.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Vasopressin nudges pressure up two ways: the pituitary hormone constricts vessels through V1 receptors and makes the kidney retain water through V2, expanding volume — a lesser arm of blood-pressure control beyond the renin-angiotensin system.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Hypertension and diabetes travel as a metabolic pair: shared insulin resistance links them, they co-occur in metabolic syndrome, and together they multiply the risk of the kidney, heart, and stroke disease each causes.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Fat cells push the pressure up: visceral adipocytes secrete angiotensinogen, leptin, and inflammatory adipokines while activating the sympathetic nervous system, a key link between obesity and hypertension.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Hypertension has an inflammasome arm: NLRP3 activation and the IL-1β it releases promote the vascular and renal inflammation that sustains high blood pressure, part of the immune contribution to the disease.
- `connects-to` → **[Obesity](../obesity/README.md)** — Excess weight is a leading driver of high pressure: obesity raises blood volume, sympathetic tone, and aldosterone while compressing the kidneys, so weight gain accounts for much of the hypertension in rich and rising populations.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Hypertension has an immune arm: CD8 cytotoxic T cells infiltrate the kidney and vessel wall and sustain the salt retention and vascular inflammation that keep blood pressure high, a mechanism that reframes part of the disease as immune-driven.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Adrenaline drives the pressure surges: epinephrine from sympathetic activation and the adrenal medulla speeds the heart and constricts vessels, behind stress-related spikes and the extreme swings of pheochromocytoma.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Angiotensin II inflames the vessel through NF-κB: it activates NF-κB in vascular and renal cells to drive the cytokines and oxidative stress that stiffen arteries, the inflammatory engine upstream of the NLRP3 arm of hypertension.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Poor sleep pushes the pressure up: insomnia and short sleep raise sympathetic tone and blunt the normal nocturnal dip, and obstructive sleep apnea is a leading cause of resistant hypertension.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — It shares its soil with venous clots: hypertension clusters with the metabolic and vascular risk factors of venous thromboembolism, and the two are modestly associated beyond their common arterial disease.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — The link runs both ways with the kidney's cancer: hypertension is an established risk factor for renal cell carcinoma, while the tumor's renin secretion and renal damage in turn cause secondary hypertension.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Small-vessel damage muddies the movement disorder: midlife hypertension drives the cerebral small-vessel disease behind vascular parkinsonism, which mimics and worsens Parkinson's, and orthostatic swings complicate its management.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Pressure and mood interact: depression is more common in hypertension and worsens adherence and outcomes, while chronic stress and some antihypertensives influence mood, a clinically important two-way link.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety and blood pressure feed each other: chronic anxiety and sympathetic arousal acutely raise blood pressure, and living with hypertension breeds health anxiety — a bidirectional, clinically relevant link.
- `connects-to` → **[NASH](../nash/README.md)** — It clusters with fatty-liver disease: hypertension is a core component of the metabolic syndrome that drives NASH, the two coexisting through shared insulin resistance and visceral adiposity.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Through the kidney it lowers the blood count: hypertensive nephrosclerosis is a leading cause of chronic kidney disease, and the failing kidney's loss of erythropoietin produces a renal anemia.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones cause and control blood pressure: secondary hypertension arises from primary aldosteronism, Cushing's, thyroid disease and phaeochromocytoma, and the RAAS that drives it is an endocrine axis.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Severe spikes injure the brain: a hypertensive emergency causes encephalopathy and posterior reversible encephalopathy syndrome, and chronic hypertension is the leading cause of intracerebral haemorrhage.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Sleep-disordered breathing drives it up: obstructive sleep apnoea, with its nocturnal hypoxia and sympathetic surges, is a major reversible cause of resistant hypertension.

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
