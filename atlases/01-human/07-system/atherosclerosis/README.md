---
schema: human-scale-entry/v1
id: atherosclerosis
name: Atherosclerosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic arterial intimal disease driven by LDL oxidation, macrophage foam cell formation, and smooth muscle migration; vulnerable plaque rupture causes MI and stroke. Statins, PCSK9 inhibitors, and anti-inflammatory therapies (colchicine) are evidence-based interventions."
aliases: ["arteriosclerosis", "coronary artery disease", "CAD", "ASCVD", "atherosclerotic cardiovascular disease"]
sources:
  - id: ross-1999-atherosclerosis-review
    type: peer-reviewed
    cite: "Ross R. Atherosclerosis — an inflammatory disease. N Engl J Med. 1999;340(2):115-126."
    doi: "10.1056/NEJM199901143400207"
    pmid: "9887164"
    url: "https://doi.org/10.1056/NEJM199901143400207"
  - id: ridker-2017-cantos
    type: peer-reviewed
    cite: "Ridker PM, Everett BM, Thuren T, et al. Antiinflammatory Therapy with Canakinumab for Atherosclerotic Disease. N Engl J Med. 2017;377(12):1119-1131."
    doi: "10.1056/NEJMoa1707914"
    pmid: "28845751"
    url: "https://doi.org/10.1056/NEJMoa1707914"
  - id: sabatine-2017-pcsk9
    type: peer-reviewed
    cite: "Sabatine MS, Giugliano RP, Keech AC, et al. Evolocumab and Clinical Outcomes in Patients with Cardiovascular Disease. N Engl J Med. 2017;376(18):1713-1722."
    doi: "10.1056/NEJMoa1615664"
    pmid: "28304224"
    url: "https://doi.org/10.1056/NEJMoa1615664"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: targets
    note: "Atherosclerosis is the primary cause of coronary artery disease, peripheral arterial disease, and ischemic stroke; plaque build-up reduces luminal diameter, limits perfusion during demand, and ruptures to trigger acute thrombosis — the mechanism of most MIs and ischemic strokes."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "LDL-C is the causal driver of atherosclerosis; apoB-containing lipoproteins (LDL, Lp(a), VLDL remnants) accumulate in the arterial intima → oxidation → foam cell formation; each 1 mmol/L LDL reduction → 22% CVD event reduction (Cholesterol Treatment Trialists 2010)."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "eNOS-derived NO maintains vascular homeostasis; LDL oxidation and hypertension reduce NO via oxidative stress → endothelial dysfunction, the earliest atherosclerotic lesion; statins, exercise, and ACE inhibitors partially restore eNOS activity and plaque stability."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are the defining plaque component; monocytes take up oxLDL via SR-A/CD36 → foam cells; M1-polarized macrophages produce MMP-9/12 → fibrous cap thinning and rupture; TREM2+ macrophages promote lipid export and plaque resolution."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "PCSK9 inhibitors (evolocumab, alirocumab) reduce LDL-C by 50-60% add-on to statins; FOURIER trial (evolocumab): 15% RRR in MACE at ~26 months; ODYSSEY OUTCOMES (alirocumab): 15% RRR with mortality reduction; PCSK9 inhibition is standard-of-care for high-risk atherosclerotic CVD."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2 from endothelium/macrophages → CCR2 on monocytes → subendothelial monocyte recruitment → foam cell formation → atherosclerotic plaque; CCL2/CCR2 knockout reduces plaque 40-60% in ApoE-/- mice; serum CCL2 correlates with MACE risk in MRFIT and EPIC-Norfolk cohorts."
  - target: 01-human/07-system/familial-hypercholesterolemia
    relation: connects-to
    note: "FH accelerates atherosclerosis; HeFH untreated: 20× higher CVD risk; coronary atherosclerosis, tendon xanthomas, and xanthelasma are hallmarks; cumulative LDL-C burden predicts events; early statin initiation reduces atherosclerotic events in HeFH."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "FN accumulates in the arterial intima early in atherosclerosis; EDA-FN activates TLR4 on SMCs and macrophages → NF-κB → inflammation; FN-integrin α5β1 promotes SMC migration from media to intima; plaque FN cross-links collagen → fibrous cap stability; plasma FN falls in acute MI."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: treated-by
    note: "Aspirin 75-100 mg/day is a cornerstone of secondary prevention in atherosclerotic CVD; irreversible platelet COX-1 acetylation blocks TXA₂ → prevents arterial thrombosis at ruptured plaques; ATC meta-analysis: 22% proportional reduction in serious vascular events."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Cholesterol (C₂₇H₄₆O) and fatty acid carbon accumulate in arterial macrophages forming foam cells; oxidised LDL carbon adducts trigger inflammatory NF-κB signalling; statins inhibit HMG-CoA reductase, reducing hepatic cholesterol carbon synthesis."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Atherosclerosis begins at the endothelial cell: disturbed flow, LDL, smoking and hyperglycemia injure it, so it loses nitric-oxide protection and expresses adhesion molecules that recruit monocytes and let LDL enter the intima—the initiating step of plaque."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Coronary atherosclerosis is the dominant cause of heart disease: plaque narrowing produces angina and ischemia, while rupture of a vulnerable plaque triggers thrombosis → myocardial infarction; LDL lowering, antiplatelets and revascularization aim to stabilize coronary plaque."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Atherosclerosis is a leading cause of ischemic stroke: carotid and intracranial plaques narrow vessels and, when they rupture, throw emboli or thrombose to occlude cerebral arteries → infarction; carotid imaging, statins, antiplatelets and endarterectomy target this mechanism."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes powerfully accelerates atherosclerosis: hyperglycemia, insulin resistance, and diabetic dyslipidemia injure the endothelium and inflame plaques, so cardiovascular disease is the top killer in diabetes—hence aggressive lipid and BP control."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Hypertension drives atherosclerosis through mechanical and inflammatory injury: high pressure damages the endothelium, especially at branch points, accelerating plaque formation and rupture—so BP control is among the best ways to prevent its heart attacks and strokes."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Vascular smooth muscle cells shape atherosclerotic plaques both ways: they migrate into the intima to form the fibrous cap that stabilizes a plaque, but also take up lipid to become foam cells—so their behavior decides whether a plaque stays stable or ruptures."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets turn a plaque into a heart attack: when an atherosclerotic cap ruptures, the exposed lipid core triggers platelet adhesion and aggregation forming the occlusive thrombus—so antiplatelet drugs like aspirin help prevent myocardial infarction and stroke."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 links inflammation to atherosclerosis: plaque macrophages release IL-6 that drives CRP and fuels lesion progression, and trials lowering inflammation (canakinumab, colchicine) cut cardiovascular events—showing atherosclerosis is inflammatory, not just lipid."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity accelerates atherosclerosis: excess visceral fat drives insulin resistance, dyslipidemia, hypertension and chronic inflammation that together damage arteries, so obesity is a central, modifiable hub feeding the major atherosclerotic risk factors."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium marks and stiffens atherosclerotic arteries: chronic plaque inflammation drives calcium deposition that hardens vessel walls, and a CT coronary-calcium score quantifies this buildup to gauge cardiovascular risk."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells make atherosclerosis an inflammatory disease: Th1 cells in the plaque secrete cytokines that activate macrophages and destabilize the fibrous cap, so immune activity—not just lipid—governs whether a plaque stays quiet or ruptures."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Chronic kidney disease accelerates atherosclerosis: uremia, phosphate retention and inflammation promote vascular calcification and plaque, so cardiovascular disease—not kidney failure—is the leading cause of death in CKD."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "APOE shapes atherosclerosis risk: this lipid-carrier protein clears cholesterol-rich particles, and the common APOE4 variant raises LDL and cardiovascular (and Alzheimer's) risk, so APOE genotype is a built-in modifier of how fast plaque builds."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome fuels atherosclerosis: gut bacteria convert dietary choline and carnitine into TMAO, a metabolite that promotes plaque and clotting, so what microbes make from red meat and eggs feeds the arterial disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils inflame the atherosclerotic plaque: they release NETs and enzymes that recruit more inflammation and destabilize the fibrous cap, so beyond macrophages, neutrophil-driven inflammation helps turn a stable plaque into a rupture-prone one."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "An atherosclerotic plaque lives or dies by its collagen cap: smooth muscle lays down a collagen-rich fibrous cap that, when thick, keeps the plaque stable, but when thinned by inflammation it ruptures—triggering the clot of a heart attack or stroke."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Atherosclerosis is an immune disease involving cytotoxic T cells: CD8 T cells infiltrate plaques and can kill the cells that stabilize them, adding adaptive immunity to the macrophage-driven inflammation behind plaque progression."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Intraplaque hemorrhage accelerates atherosclerosis: leaky new vessels bleed red cells into the plaque, dumping cholesterol-rich membranes and iron that enlarge the lipid core and destabilize it—turning a quiet plaque into a dangerous one."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Atherosclerosis is dangerous because it cuts off oxygen: narrowed arteries throttle blood flow so tissue demand outstrips supply, causing the angina, claudication and—on plaque rupture—the infarction that kills oxygen-starved muscle."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Atherosclerosis turns deadly when thrombin fires: a ruptured plaque exposes tissue that triggers the clotting cascade, and thrombin builds the clot that abruptly blocks the artery—the final step to heart attack and stroke."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Atherosclerosis attacks the kidney's arteries: narrowing of the renal artery (renovascular disease) lowers kidney blood flow, driving resistant hypertension and progressive kidney damage, so the disease is both a cause and a victim of vascular aging."
---

# Atherosclerosis

## Overview

**Atherosclerosis** is a **chronic inflammatory disease of the arterial intima** characterized by progressive accumulation of lipids, immune cells, smooth muscle cells, and extracellular matrix components forming **atherosclerotic plaques (atheromas)** within the arterial wall. First recognized as an inflammatory disease by Russell Ross in 1999 [^ross-1999-atherosclerosis-review], atherosclerosis is the underlying pathology of **coronary artery disease (CAD), ischemic stroke, and peripheral arterial disease (PAD)** — collectively **atherosclerotic cardiovascular disease (ASCVD)** — the **leading cause of death globally** (~18 million deaths/year, WHO 2019).

The process begins in childhood with **fatty streaks** and progresses silently over decades. Clinically manifest disease (ACS, stable angina, TIA, stroke) typically appears in the 4th-7th decade of life. **Acute plaque rupture or erosion** triggers thrombus formation → abrupt vessel occlusion → myocardial infarction or ischemic stroke.

**Risk factors (established):**
- **Modifiable:** Hyperlipidemia (LDL-C, Lp(a)), hypertension, diabetes mellitus (T2DM > T1DM), smoking, obesity, physical inactivity, chronic inflammation (RA, psoriasis, SLE), air pollution, psychosocial stress
- **Non-modifiable:** Age (men >45, women >55), male sex, family history of premature ASCVD (<55 men, <65 women), genetic hypercholesterolemia (FH)
- **Novel risk enhancers:** hs-CRP ≥2.0 mg/L, coronary artery calcium (CAC) score ≥100, Lp(a) ≥50 mg/dL (≥125 nmol/L), ABI <0.9 (peripheral arterial disease), chronic kidney disease

**Atherosclerosis pathological stages:**
1. **Endothelial dysfunction:** LDL entry, oxidative stress, reduced NO → earliest event; no structural change; reversible
2. **Fatty streak:** Foam cells (macrophage-derived); first visible lesion; present in most adults by age 20; can regress
3. **Plaque (atheroma):** Necrotic core (lipid, dead foam cells, cholesterol crystals), fibrous cap (smooth muscle, collagen), inflammatory infiltrate; decades of progression
4. **Vulnerable (unstable) plaque:** Thin fibrous cap, large necrotic core, rich macrophage infiltrate → prone to rupture → ACS
5. **Plaque rupture/erosion → thrombus:** ACS, MI, ischemic stroke

## Structure

### Plaque anatomy [^ross-1999-atherosclerosis-review]

**Intimal layers (site of atherosclerosis):**
- **Endothelium:** Normally anti-atherogenic (NO production, LDL barrier, PAI-1 low); dysfunction = first step; risk factors → endothelial oxidative stress → ICAM-1, VCAM-1, E-selectin upregulation → monocyte adhesion and transmigration
- **Subendothelial space (intima):** LDL retention via proteoglycans (biglycan, decorin) → oxidative modification (oxLDL, minimally modified LDL) → pattern recognition by SR-A, CD36 on macrophages
- **Internal elastic lamina:** SMC migration from media to intima depends on MMP-mediated IEL remodeling

**Plaque components:**
- **Necrotic core:** Accumulated lipid (free cholesterol, cholesterol esters), dead foam cell remnants, cholesterol crystals (NLRP3 inflammasome activation), calcium deposits; correlates with rupture risk
- **Fibrous cap:** Dense collagen (types I and III) produced by intimal smooth muscle cells; VSMC apoptosis (from ROS, macrophage cytotoxicity) → cap thinning; cap thickness <65 μm defines thin-cap fibroatheroma (TCFA) — the vulnerable plaque phenotype
- **Shoulder region:** Junction of fibrous cap and plaque body; highest inflammatory cell density; site of cap rupture
- **Macrophage infiltrate (foam cells):** Accumulated oxLDL via SR-A/CD36 → lipid-laden foam cells; produce MMP-2/9/12 → fibrous cap degradation; produce TNF-alpha, IL-1beta, IL-6 → local and systemic inflammation
- **Neovascularization:** Intraplaque angiogenesis (VEGF-driven) → fragile intraplaque vessels → intraplaque hemorrhage → rapid plaque expansion

### Lipoprotein pathophysiology

**LDL (low-density lipoprotein):**
- ApoB-100 particle carrying cholesterol; enters intima by transcytosis (endothelial LDLR-independent) → trapped by proteoglycans → oxidized by 12-LOX, 15-LOX, MPO → oxLDL → SR-A/CD36-mediated uptake → foam cells (LDLR-pathway is cholesterol-regulated; scavenger receptors are not → unrestricted foam cell formation)
- **PCSK9 (proprotein convertase subtilisin/kexin type 9):** Binds LDL receptor on hepatocytes → lysosomal LDLR degradation → less hepatic LDL uptake → elevated plasma LDL; gain-of-function PCSK9 mutations → severe hypercholesterolemia; loss-of-function PCSK9 mutations (rare, West Africans) → very low LDL → near-zero lifetime ASCVD risk
- **Lp(a) (lipoprotein a):** LDL-like particle with additional apo(a) protein linked via disulfide bond to apoB; pro-atherogenic (intimal accumulation) and pro-thrombotic (plasminogen homology → antifibrinolytic); genetic (KRINGLE domain size determines levels); elevated in ~20% of population; pelacarsen (antisense oligonucleotide, Phase 3) and olpasiran (siRNA) reduce Lp(a) >90%

## Function

### Inflammatory mechanism of atherosclerosis

**Inflammatory cascade:**

1. **Endothelial activation:** Risk factors → ROS → NFkB → VCAM-1, ICAM-1 → monocyte (CCR2+) binding via MCP-1 (CCL2) → transmigration into intima → differentiation to macrophages
2. **Foam cell formation:** Macrophages engulf oxLDL → lipid overload → foam cell; foam cells release MMP-9/12 → fibrous cap thinning; secrete IL-1beta, TNF-alpha → amplify local inflammation
3. **Adaptive immune response:** Oxidized LDL is immunogenic → CD4+ Th1 cells produce IFN-gamma → macrophage activation; Th17 cells → plaque progression; Tregs → atheroprotective (suppress Th1/Th17 responses)
4. **NLRP3 inflammasome activation:** Cholesterol crystals → NLRP3 → IL-1beta release → systemic and local pro-atherogenic inflammation (basis for IL-1beta blockade therapy)
5. **SMC migration:** Macrophage-derived PDGF → SMC migration from media to intima → fibrous cap formation (protective initially); VSMC apoptosis → cap thinning → vulnerability
6. **Calcification:** Dead foam cells → calcium phosphate deposits; coronary artery calcium (CAC) score by CT quantifies burden

### Vulnerable plaque and acute coronary syndromes

**Plaque vulnerability (TCFA criteria):**
- Cap thickness <65 μm (ruptured plaques typically <23 μm)
- Large necrotic core >40% plaque volume
- Dense macrophage infiltrate in shoulder region
- Intraplaque neovascularization (hemorrhage risk)

**Rupture triggers:**
- Physical exertion, circadian catecholamine surge (morning peak of MIs)
- Systemic inflammation (CRP spike, acute infection)
- MMP-mediated cap degradation (macrophage-derived MMP-9, -12)

**Plaque erosion (~30% of ACS):** Endothelial denudation without plaque rupture → thrombus on intact fibrous cap; more common in younger women, smokers, hypertriglyceridemia; treated with aspirin ± P2Y12 inhibition + statin (less benefit from PCI in some cases)

## Pathology

### Diagnosis

**Functional (ischemia detection):**
- Exercise stress test (ECG ± imaging): Detect flow-limiting stenosis (>70% luminal narrowing)
- Stress echo, nuclear perfusion (SPECT, PET), cardiac MRI: Detect perfusion defects and wall motion abnormalities
- Coronary CT angiography (CCTA): Non-invasive coronary anatomy; detects stenosis and plaque burden; FFRCT (fractional flow reserve by CT) assesses physiological significance

**Anatomical (plaque characterization):**
- **Coronary artery calcium (CAC) score (non-contrast CT):** Most powerful predictor for event risk beyond Framingham score; CAC=0 → very low 10-year risk (statin downgrade candidate); CAC ≥100 → high risk (statin initiation regardless of clinical risk)
- **Intravascular ultrasound (IVUS):** Plaque burden, volume, and echogenicity in cath lab
- **OCT (optical coherence tomography):** High-resolution intravascular; identifies TCFA, fibrous cap thickness, and erosion vs. rupture

### Treatment [^ridker-2017-cantos] [^sabatine-2017-pcsk9]

**Lipid-lowering — primary and secondary prevention:**

*Statins (HMG-CoA reductase inhibitors):*
- Inhibit cholesterol synthesis → hepatic LDLR upregulation → LDL clearance; reduces LDL 30-55% (dose-dependent); high-intensity: atorvastatin 40-80 mg, rosuvastatin 20-40 mg
- **PROVE-IT, TNT, JUPITER, FOURIER (CTT meta-analysis):** Each 1 mmol/L LDL reduction → 22% RRR in major ASCVD events; NNT ~5 for high-risk secondary prevention over 5 years
- **Pleiotropic effects:** Reduce CRP, improve endothelial function, stabilize plaque (↑ fibrous cap thickness via SMC stimulation and MMP suppression); independent of LDL lowering
- **Safety:** Myopathy (1-3%, usually mild); rhabdomyolysis (<0.01%); monitor CK if symptomatic; DM risk increased ~10-12% with high-dose statins (NNT 200 for diabetes vs. NNT 5 for CV event prevention — net benefit)

*PCSK9 inhibitors:*
- **Evolocumab (Repatha, anti-PCSK9 mAb):** SC biweekly or monthly; reduces LDL 60% added to statin; FOURIER trial: evolocumab vs. placebo in statin-treated ASCVD → 15% RRR in composite MACE (MI, stroke, CV death) over 2.2 years; LDL to ~30 mg/dL achievable [^sabatine-2017-pcsk9]
- **Alirocumab (Praluent):** Similar mechanism; ODYSSEY Outcomes: 15% RRR in post-ACS patients; reduces Lp(a) ~25-30%
- **Inclisiran (LEQVIO, anti-PCSK9 siRNA):** SC injection twice/year; reduces LDL ~50% vs. placebo; ORION-10/11 trials; approved for ASCVD and FH; CVOT ongoing (ORION-4)

*Other lipid agents:*
- **Ezetimibe:** Inhibits NPC1L1 → reduced cholesterol absorption; LDL -20%; IMPROVE-IT: ezetimibe+simvastatin vs. simvastatin alone → 6.4% RRR in MACE post-ACS (modest but additive)
- **Bempedoic acid (Nexletol):** ACL inhibitor → reduces hepatic cholesterol synthesis upstream of HMG-CoA reductase; doesn't cause myopathy (not expressed in skeletal muscle); CLEAR Outcomes: 13% RRR in primary endpoint vs placebo; add-on to statins or statin-intolerant patients

**Anti-inflammatory — targeting residual inflammatory risk:**
- **Colchicine (LoDoCo2, COLCOT):** Anti-inflammatory (inhibits tubulin polymerization → inflammasome and neutrophil activation reduction); 0.5 mg daily; 31% RRR in MACE in post-ACS (COLCOT); 23% RRR in stable CAD (LoDoCo2); FDA approved for ASCVD risk reduction
- **Canakinumab (anti-IL-1beta mAb):** CANTOS trial: 150 mg SC quarterly; 15% RRR in MACE in post-MI patients with elevated hs-CRP (≥2 mg/L); confirmed inflammatory hypothesis of atherosclerosis [^ridker-2017-cantos]; not approved for CV indication due to infection mortality risk; paved way for colchicine

**Antiplatelet and antithrombotic:**
- **Aspirin (75-100 mg):** Irreversibly inhibits COX-1 → TXA2 → platelet activation; secondary prevention (established ASCVD): clear benefit; primary prevention: benefit-risk unfavorable in low-to-moderate risk (ARRIVE, ASPREE, ASCEND) — bleeding offsets CV benefit
- **P2Y12 inhibitors:** Clopidogrel, ticagrelor, prasugrel → ADP receptor blockade → antiplatelet; dual antiplatelet therapy (DAPT) post-ACS or PCI for 1-12 months
- **Rivaroxaban 2.5 mg BID + aspirin (COMPASS):** For PAD and CAD without recent ACS; 24% RRR in MACE vs. aspirin alone; FDA approved for ASCVD

## Connections

- `targets` → **[Cardiovascular System](../cardiovascular-system/README.md)** — atherosclerosis is the primary driver of coronary artery disease, ischemic stroke, and peripheral arterial disease; plaque rupture triggers acute thrombosis causing MI and stroke; statins and PCSK9 inhibitors reduce LDL and MACE by 15-50% depending on baseline risk.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — LDL-C is the causal driver of atherosclerosis; apoB-containing lipoproteins accumulate in the arterial intima, undergo oxidation, and are engulfed by macrophages → foam cell formation; each 1 mmol/L LDL reduction yields ~22% relative MACE reduction.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — eNOS-derived NO maintains vascular homeostasis; risk factors reduce NO bioavailability via oxidative stress → endothelial dysfunction, the earliest atherosclerotic lesion; statins, exercise, and ACE inhibitors partially restore eNOS activity and plaque stability.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — macrophages are the defining cellular component of atheromas; monocyte-derived macrophages ingest oxLDL via scavenger receptors → foam cells; M1-polarized macrophages produce MMP-9/12 → cap thinning and plaque rupture; anti-inflammatory therapies (colchicine, canakinumab) target macrophage-driven inflammation.
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — PCSK9 inhibitors (evolocumab, alirocumab) reduce LDL-C by 50-60% add-on to statins; FOURIER trial (evolocumab): 15% RRR in MACE at ~26 months; ODYSSEY OUTCOMES (alirocumab): 15% RRR with mortality reduction; PCSK9 inhibition is standard-of-care for high-risk atherosclerotic CVD.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 from endothelium/macrophages → CCR2 on monocytes → subendothelial monocyte recruitment → foam cell formation → atherosclerotic plaque; CCL2/CCR2 knockout reduces plaque 40-60% in ApoE-/- mice; serum CCL2 correlates with MACE risk in MRFIT and EPIC-Norfolk cohorts.
- `connects-to` → **[Familial Hypercholesterolemia](../familial-hypercholesterolemia/README.md)** — FH accelerates atherosclerosis; HeFH untreated: 20× higher CVD risk; coronary atherosclerosis, tendon xanthomas, and xanthelasma are hallmarks; cumulative LDL-C burden predicts events; early statin initiation reduces atherosclerotic events in HeFH.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — FN accumulates in the arterial intima early in atherosclerosis; EDA-FN activates TLR4 on SMCs and macrophages → NF-κB → inflammation; FN-integrin α5β1 promotes SMC migration from media to intima; plaque FN cross-links collagen → fibrous cap stability; plasma FN falls in acute MI.
- `treated-by` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — aspirin 75-100 mg/day is a cornerstone of secondary prevention in atherosclerotic CVD; irreversible platelet COX-1 acetylation blocks TXA₂ → prevents plaque-rupture-triggered arterial thrombosis; ATC meta-analysis: 22% proportional reduction in serious vascular events.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Cholesterol (C₂₇H₄₆O) and fatty acid carbon accumulate in arterial macrophages forming foam cells; oxidised LDL carbon adducts trigger inflammatory NF-κB signalling; statins inhibit HMG-CoA reductase, reducing hepatic cholesterol carbon synthesis.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Atherosclerosis begins at the endothelial cell: disturbed flow, LDL, smoking and hyperglycemia injure it, so it loses nitric-oxide protection and expresses adhesion molecules that recruit monocytes and let LDL enter the intima—the initiating step of plaque.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Coronary atherosclerosis is the dominant cause of heart disease: plaque narrowing produces angina and ischemia, while rupture of a vulnerable plaque triggers thrombosis → myocardial infarction; LDL lowering, antiplatelets and revascularization aim to stabilize coronary plaque.
- `connects-to` → **[Stroke](../stroke/README.md)** — Atherosclerosis is a leading cause of ischemic stroke: carotid and intracranial plaques narrow vessels and, when they rupture, throw emboli or thrombose to occlude cerebral arteries → infarction; carotid imaging, statins, antiplatelets and endarterectomy target this mechanism.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes powerfully accelerates atherosclerosis: hyperglycemia, insulin resistance, and diabetic dyslipidemia injure the endothelium and inflame plaques, so cardiovascular disease is the top killer in diabetes—hence aggressive lipid and BP control.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Hypertension drives atherosclerosis through mechanical and inflammatory injury: high pressure damages the endothelium, especially at branch points, accelerating plaque formation and rupture—so BP control is among the best ways to prevent its heart attacks and strokes.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Vascular smooth muscle cells shape atherosclerotic plaques both ways: they migrate into the intima to form the fibrous cap that stabilizes a plaque, but also take up lipid to become foam cells—so their behavior decides whether a plaque stays stable or ruptures.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets turn a plaque into a heart attack: when an atherosclerotic cap ruptures, the exposed lipid core triggers platelet adhesion and aggregation forming the occlusive thrombus—so antiplatelet drugs like aspirin help prevent myocardial infarction and stroke.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 links inflammation to atherosclerosis: plaque macrophages release IL-6 that drives CRP and fuels lesion progression, and trials lowering inflammation (canakinumab, colchicine) cut cardiovascular events—showing atherosclerosis is inflammatory, not just lipid.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity accelerates atherosclerosis: excess visceral fat drives insulin resistance, dyslipidemia, hypertension and chronic inflammation that together damage arteries, so obesity is a central, modifiable hub feeding the major atherosclerotic risk factors.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium marks and stiffens atherosclerotic arteries: chronic plaque inflammation drives calcium deposition that hardens vessel walls, and a CT coronary-calcium score quantifies this buildup to gauge cardiovascular risk.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells make atherosclerosis an inflammatory disease: Th1 cells in the plaque secrete cytokines that activate macrophages and destabilize the fibrous cap, so immune activity—not just lipid—governs whether a plaque stays quiet or ruptures.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Chronic kidney disease accelerates atherosclerosis: uremia, phosphate retention and inflammation promote vascular calcification and plaque, so cardiovascular disease—not kidney failure—is the leading cause of death in CKD.
- `connects-to` → **[APOE](../../03-molecular/apoe/README.md)** — APOE shapes atherosclerosis risk: this lipid-carrier protein clears cholesterol-rich particles, and the common APOE4 variant raises LDL and cardiovascular (and Alzheimer's) risk, so APOE genotype is a built-in modifier of how fast plaque builds.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome fuels atherosclerosis: gut bacteria convert dietary choline and carnitine into TMAO, a metabolite that promotes plaque and clotting, so what microbes make from red meat and eggs feeds the arterial disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils inflame the atherosclerotic plaque: they release NETs and enzymes that recruit more inflammation and destabilize the fibrous cap, so beyond macrophages, neutrophil-driven inflammation helps turn a stable plaque into a rupture-prone one.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — An atherosclerotic plaque lives or dies by its collagen cap: smooth muscle lays down a collagen-rich fibrous cap that, when thick, keeps the plaque stable, but when thinned by inflammation it ruptures—triggering the clot of a heart attack or stroke.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Atherosclerosis is an immune disease involving cytotoxic T cells: CD8 T cells infiltrate plaques and can kill the cells that stabilize them, adding adaptive immunity to the macrophage-driven inflammation behind plaque progression.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Intraplaque hemorrhage accelerates atherosclerosis: leaky new vessels bleed red cells into the plaque, dumping cholesterol-rich membranes and iron that enlarge the lipid core and destabilize it—turning a quiet plaque into a dangerous one.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Atherosclerosis is dangerous because it cuts off oxygen: narrowed arteries throttle blood flow so tissue demand outstrips supply, causing the angina, claudication and—on plaque rupture—the infarction that kills oxygen-starved muscle.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Atherosclerosis turns deadly when thrombin fires: a ruptured plaque exposes tissue that triggers the clotting cascade, and thrombin builds the clot that abruptly blocks the artery—the final step to heart attack and stroke.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Atherosclerosis attacks the kidney's arteries: narrowing of the renal artery (renovascular disease) lowers kidney blood flow, driving resistant hypertension and progressive kidney damage, so the disease is both a cause and a victim of vascular aging.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^ross-1999-atherosclerosis-review]: Ross R. Atherosclerosis — an inflammatory disease. *N Engl J Med.* 1999;340(2):115-126. [doi:10.1056/NEJM199901143400207](https://doi.org/10.1056/NEJM199901143400207) · [PubMed 9887164](https://pubmed.ncbi.nlm.nih.gov/9887164/)
[^ridker-2017-cantos]: Ridker PM, Everett BM, Thuren T, et al. Antiinflammatory Therapy with Canakinumab for Atherosclerotic Disease. *N Engl J Med.* 2017;377(12):1119-1131. [doi:10.1056/NEJMoa1707914](https://doi.org/10.1056/NEJMoa1707914) · [PubMed 28845751](https://pubmed.ncbi.nlm.nih.gov/28845751/)
[^sabatine-2017-pcsk9]: Sabatine MS, Giugliano RP, Keech AC, et al. Evolocumab and Clinical Outcomes in Patients with Cardiovascular Disease. *N Engl J Med.* 2017;376(18):1713-1722. [doi:10.1056/NEJMoa1615664](https://doi.org/10.1056/NEJMoa1615664) · [PubMed 28304224](https://pubmed.ncbi.nlm.nih.gov/28304224/)
