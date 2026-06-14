---
schema: human-scale-entry/v1
id: familial-hypercholesterolemia
name: Familial Hypercholesterolemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Familial hypercholesterolemia (FH) is an autosomal dominant disorder; LDLR mutations (most common), APOB R3527Q, or PCSK9 GOF mutations → LDL-C >190 mg/dL; premature atherosclerosis and MI (HoFH: untreated → MI by age 20). Statins + PCSK9 inhibitors are standard treatment."
aliases: ["FH", "heterozygous FH", "HeFH", "homozygous FH", "HoFH", "familial hypercholesterolaemia", "autosomal dominant hypercholesterolemia", "ADH"]
sources:
  - id: goldstein-1985-ldlr-nobel
    type: peer-reviewed
    cite: "Goldstein JL, Brown MS. The LDL receptor. Arterioscler Thromb Vasc Biol. 2009;29(4):431-438."
    doi: "10.1161/ATVBAHA.108.179564"
    pmid: "19299327"
    url: "https://doi.org/10.1161/ATVBAHA.108.179564"
  - id: raal-2020-inclisiran-fh
    type: peer-reviewed
    cite: "Raal FJ, Kallend D, Ray KK, et al. Inclisiran for the Treatment of Heterozygous Familial Hypercholesterolemia. N Engl J Med. 2020;382(16):1520-1530."
    doi: "10.1056/NEJMoa1913805"
    pmid: "32197277"
    url: "https://doi.org/10.1056/NEJMoa1913805"
  - id: watts-2020-hzfh-guidelines
    type: clinical-guideline
    cite: "Watts GF, Gidding SS, Hegele RA, et al. International Atherosclerosis Society guidance for implementing best practice in the care of familial hypercholesterolaemia. Nat Rev Cardiol. 2023;20(12):845-869."
    doi: "10.1038/s41569-023-00892-0"
    pmid: "37322181"
    url: "https://doi.org/10.1038/s41569-023-00892-0"
cross_links:
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "PCSK9 GOF mutations cause autosomal dominant FH (ADH3); evolocumab and alirocumab reduce LDL-C 50-60% add-on to statins; inclisiran (PCSK9 siRNA) reduces LDL-C ~50% with Q6M dosing; standard of care for FH not at LDL goal on maximally tolerated statin."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "FH accelerates atherosclerosis; HeFH untreated: 20× higher CVD risk; coronary atherosclerosis, tendon xanthomas, and xanthelasma are hallmarks; cumulative LDL-C burden predicts events; early statin initiation reduces atherosclerotic events in HeFH."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "FH results from impaired LDLR-mediated cholesterol clearance; LDLR mutations → fewer surface receptors → LDL-C >190 mg/dL (HeFH) or >500 mg/dL (HoFH LDLR null); excess cholesterol in macrophages → foam cells → atheromatous plaque."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatocytes express >90% of plasma LDLR; LDLR-mediated LDL endocytosis is the primary clearance route; SREBP-2 upregulates LDLR after statin treatment; liver transplant in HoFH normalizes LDL-C — confirming hepatocytic LDLR as the disease driver."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "In FH, chronically elevated LDL-C → macrophage scavenger receptor (SR-A, CD36) uptake of oxidized LDL → foam cell formation; foam cells are the histological hallmark of the atheromatous plaque; FH macrophages exhibit exaggerated ox-LDL uptake vs. normolipidemic controls."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "FH accelerates carotid and cerebrovascular atherosclerosis; HeFH patients have elevated carotid intima-media thickness (cIMT) and higher stroke risk vs. general population; statin + PCSK9 inhibitor reduces cIMT progression and ischemic stroke incidence in FH cohorts."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Familial hypercholesterolemia is defined by its toll on the heart: lifelong high LDL drives premature coronary disease — heterozygotes infarct in their 40s-50s while homozygotes can have MIs and aortic-valve stenosis in childhood; early intensive LDL lowering is lifesaving."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Atherosclerosis in FH starts at the endothelium: the lifelong excess of LDL infiltrates and is retained in the subendothelial intima, where oxidation activates endothelial cells to recruit monocytes — repeated for decades at FH's LDL levels, this builds plaque far earlier."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Vascular smooth muscle cells shape the FH atheroma: they migrate from the media into the intima, take up modified LDL to become foam cells, and lay down the collagen fibrous cap whose stability — or rupture — determines whether a plaque stays silent or causes infarction."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: treated-by
    note: "Statins are the cornerstone of FH treatment: by inhibiting HMG-CoA reductase they upregulate hepatic LDL receptors to clear LDL, but FH patients—especially homozygotes with few functional receptors—often need high-intensity statins plus ezetimibe and PCSK9 inhibitors."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is central to FH: hepatocyte LDL receptors normally clear ~70% of circulating LDL, so the LDLR (or APOB/PCSK9) mutations of FH cripple this clearance → lifelong high LDL; the liver is thus the target of statins, PCSK9 inhibitors, apheresis and gene therapy."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "FH and hypertension are multiplicative cardiovascular risk factors: lifelong high LDL accelerates atherosclerosis while raised blood pressure adds shear stress and endothelial injury, so an FH patient who is also hypertensive faces especially early coronary disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Familial hypercholesterolemia is a lifelong assault on the cardiovascular system: from birth very high LDL accelerates atherosclerosis, so untreated heterozygotes get coronary disease decades early and homozygotes in childhood—early statin/PCSK9 therapy is essential."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Familial hypercholesterolemia and type 2 diabetes multiply cardiovascular risk together: FH's lifelong LDL burden plus diabetic dyslipidemia compound atherosclerosis—and although statins slightly raise diabetes risk, their cardiovascular benefit in FH far outweighs it."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Familial hypercholesterolemia and NASH are distinct lipid disorders of the liver: FH is a receptor defect that floods blood with LDL but spares the liver, while NASH is hepatic fat from insulin resistance—high LDL with a normal liver differs from fatty liver."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Familial hypercholesterolemia causes premature coronary disease that leads to heart failure: lifelong sky-high LDL drives early severe atherosclerosis and heart attacks, so untreated FH causes ischemic cardiomyopathy decades early."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Familial hypercholesterolemia and obesity stack cardiovascular risk: FH is a genetic LDL-receptor defect causing very high cholesterol, while obesity adds insulin resistance and inflammation—together compounding the premature atherosclerosis FH drives."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Familial hypercholesterolemia and chronic kidney disease are both potent cardiovascular risk amplifiers: FH from extreme LDL, CKD from vascular calcification and dyslipidemia, so an FH patient who also develops CKD faces compounded atherosclerotic risk."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "FH and APOE both shape blood cholesterol but differently: FH is a single-gene defect in LDL clearance causing severe lifelong hypercholesterolemia, while APOE variants modify lipid levels and cardiovascular risk—monogenic versus polygenic cholesterol disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Coronary artery calcium scoring helps gauge risk in FH: lifelong high LDL drives calcified atherosclerotic plaque, so a CT calcium score quantifies accumulated arterial damage and refines who needs the most aggressive lipid lowering."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "FH's silent arterial damage is revealed by photon-based imaging: low-dose CT uses X-ray photons to measure coronary calcium, turning invisible decades of LDL-driven plaque buildup into a number that guides how intensively to treat."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Familial hypercholesterolemia writes itself on the skin: lifelong high LDL deposits cholesterol as tendon xanthomas (Achilles, knuckles) and eyelid xanthelasma, so these fatty bumps are physical clues that prompt lipid testing and family screening."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye flags familial hypercholesterolemia: a corneal arcus—a white lipid ring around the iris—appearing before age 45 strongly suggests it, so this ocular sign, like xanthomas, helps catch the inherited high cholesterol early enough to prevent heart attacks."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cultured skin fibroblasts revealed FH's cause: studying patients' fibroblasts, Brown and Goldstein discovered the LDL receptor and how its loss blocks cholesterol uptake—the Nobel work that explained FH and led to statins and PCSK9 inhibitors."
---

# Familial Hypercholesterolemia

## Overview

**Familial hypercholesterolemia (FH)** is the most common single-gene disorder causing premature cardiovascular disease, characterized by **lifelong markedly elevated LDL-cholesterol (LDL-C)** due to impaired receptor-mediated clearance of LDL particles from the circulation [^goldstein-1985-ldlr-nobel].

FH is a **monogenic autosomal dominant disorder** caused by mutations in three genes:
1. **LDLR (LDL receptor gene; chr19p13.2):** >2,500 pathogenic variants; accounts for ~85-90% of genetically confirmed FH; loss-of-function → reduced or absent LDLR surface expression → LDL not cleared from plasma
2. **APOB (apolipoprotein B gene; chr2p24.1):** Most common variant R3527Q (European); APOB protein is the ligand for LDLR; R3527Q reduces LDLR binding affinity → LDL clearance ~50% reduced
3. **PCSK9 (chr1p32.3):** Gain-of-function mutations (D374Y most severe; S127R; F216L) → accelerated LDLR degradation → fewer surface LDLR → elevated LDL-C; accounts for ~2-3% of FH

**Prevalence:**
- **Heterozygous FH (HeFH):** 1 in 200-250 in the general population (previously estimated at 1 in 500, upward revision from genomic data); ~30 million people globally
- **Homozygous FH (HoFH):** 1 in ~300,000-400,000; biallelic LDLR mutations; two pathogenic alleles
- **Severely underdiagnosed:** Only ~10-20% of FH patients are diagnosed in most countries despite cascade screening programs
- **Founder effects:** High prevalence in Afrikaners (~1:100), French Canadians (~1:270), Lebanese (~1:170), Ashkenazi Jews — due to founder mutations in LDLR

**Clinical consequences without treatment:**
- HeFH: LDL-C typically 190-300 mg/dL; cumulative exposure → first MI at age 40-50 (men) or 50-60 (women); 20× higher CHD risk vs. age-matched general population
- HoFH: LDL-C typically 500-1000+ mg/dL; MI by age 10-20 years in null-null LDLR mutations; generalized xanthomas in childhood; aortic valve stenosis from lipid deposition

## Structure

### Genetic mechanisms — LDL receptor pathway

**Normal LDLR cycle:**
1. LDLR synthesized in ER → glycosylated → cell surface (~10,000 receptors/hepatocyte)
2. LDLR binds apoB-100 (LDL) or apoE (VLDL remnant/IDL) via EGF-precursor domain
3. LDLR-LDL complex → clathrin-coated pit → endocytosis → early endosome
4. Acidic endosomal pH → LDLR-LDL dissociation → LDLR recycled to cell surface (each LDLR recycles ~150× over its lifetime); LDL → lysosome → cholesterol release → cellular regulation of cholesterol synthesis (SREBP feedback)

**PCSK9 disruption of LDLR recycling:**
- PCSK9 binds LDLR extracellular EGF-A domain with high affinity at acidic pH → prevents LDLR conformational change needed for dissociation from ligand → LDLR-PCSK9-LDL complex → lysosomal degradation of LDLR → net loss of LDLR from cell surface
- Statins → ↑LDLR expression (SREBP-2 activation) but also → ↑PCSK9 secretion → partially offset LDLR increase (explains 50% of LDL-C reduction achievable with statins)
- PCSK9 GOF mutations (D374Y) have 5-10× higher LDLR affinity at acidic pH → maximum LDLR degradation → severe FH phenotype

**LDLR mutation classes:**
- **Class 1 (null):** No protein synthesized; most severe; frameshift/nonsense mutations
- **Class 2 (transport-defective):** LDLR synthesized but trapped in ER; can't reach cell surface
- **Class 3 (binding-defective):** LDLR reaches surface but can't bind LDL (ligand-binding domain mutations)
- **Class 4 (internalization-defective):** LDLR binds LDL but can't internalize (clathrin-coated pit targeting mutations in cytoplasmic domain)
- **Class 5 (recycling-defective):** LDLR binds and internalizes but can't recycle; degraded with ligand

**Clinical features:**
- **Tendon xanthomas:** Achilles tendon (most characteristic), extensor tendons of hand, patellar tendon; lipid-laden macrophage foam cell deposits; pathognomonic for FH when present
- **Xanthelasma:** Yellow plaques on eyelids; less specific (also in normolipidemic patients)
- **Corneal arcus:** Lipid deposit in corneal periphery; highly specific in young patients (<45 years) with elevated LDL-C
- **Premature CAD/aortic stenosis:** Family history of premature MI (first-degree male relative <55, female <65)

### Diagnostic criteria (Dutch Lipid Clinic Network)

| Criterion | Points |
|:---|:---|
| Family history of premature CAD or familial hypercholesterolemia | 1-2 |
| Clinical history of premature CAD or cerebrovascular/peripheral artery disease | 2 |
| Tendon xanthomas (patient or first-degree relative) | 6 |
| Corneal arcus <45 years | 4 |
| LDL-C ≥8.5 mmol/L (≥330 mg/dL) | 8 |
| LDL-C 6.5-8.4 mmol/L (250-329 mg/dL) | 5 |
| LDL-C 5.0-6.4 mmol/L (190-249 mg/dL) | 3 |
| LDL-C 4.0-4.9 mmol/L (155-189 mg/dL) | 1 |
| Causative mutation in LDLR, APOB, PCSK9 | 8 |
- **Definite FH:** ≥8 points; **Probable FH:** 6-7; **Possible FH:** 3-5

**Cascade screening:** Genetic testing of first-degree relatives of confirmed FH patients → most cost-effective FH detection strategy; identifying an affected parent yields 50% probability per child

## Function

### Treatment — Lipid-lowering strategy

**Goal:** LDL-C reduction to target (ESC/EAS guidelines for very high risk: <55 mg/dL or ≥50% reduction from baseline; for HoFH: as low as possible, ideally <70 mg/dL)

**High-intensity statin therapy (first-line):**
- Rosuvastatin 20-40 mg or atorvastatin 40-80 mg: ↓LDL-C ~45-55%
- Mechanism: inhibit HMG-CoA reductase → ↓cholesterol synthesis → SREBP-2 activation → ↑LDLR expression (and ↑PCSK9 — partially offsetting the benefit)
- Adverse effects: myalgia (5-10%); rare myopathy/rhabdomyolysis; statin-induced myopathy screening via CK; LFT elevation (rare)

**Ezetimibe (second-line add-on):**
- NPC1L1 inhibitor → ↓intestinal cholesterol absorption → further LDLR upregulation; adds ~20-25% LDL-C reduction to statin
- SHARP trial: simvastatin + ezetimibe → 17% RRR atherosclerotic events in CKD; IMPROVE-IT: ezetimibe + simvastatin vs. simvastatin alone → 6.4% RRR MACE at 7 years (modest incremental benefit)

**PCSK9 inhibitors (standard for FH not at goal):**
- **Evolocumab (Repatha):** 140 mg SC Q2W or 420 mg SC Q4W; FOURIER trial: 59% LDL-C reduction; 15% MACE reduction at 26 months; FDA-approved for HeFH and HoFH (reduced but not absent LDLR function)
- **Alirocumab (Praluent):** 75-150 mg SC Q2W; ODYSSEY OUTCOMES: 15% MACE reduction + 15% all-cause mortality reduction at 2.8 years; FDA-approved for HeFH
- **Inclisiran (Leqvio; siRNA):** 284 mg SC at month 0, 3, then Q6 months [^raal-2020-inclisiran-fh]; mRNA silencing of hepatic PCSK9 → ~50% sustained LDL-C reduction with twice-yearly dosing; FDA-approved 2021 for HeFH; ORION-9: primary endpoint met

**HoFH-specific therapies:**
- **LDL apheresis:** Weekly/biweekly extracorporeal LDL removal; ~60-70% acute LDL-C reduction; required for LDLR null/null patients until new therapies available
- **Lomitapide (Juxtapid):** MTP (microsomal triglyceride transfer protein) inhibitor → ↓VLDL assembly/secretion → LDL-C reduction 50%; Black Box Warning: hepatotoxicity; FDA-approved for HoFH only
- **Evinacumab (Evkeeza; anti-ANGPTL3 mAb; Regeneron):** FDA-approved 2021 for HoFH; ANGPTL3 inhibits lipoprotein lipase and endothelial lipase; evinacumab → ↓LDL-C ~49% in HoFH even with null LDLR (LPL-mediated pathway, LDLR-independent); monthly IV infusion
- **Mipomersen (Kynamro; antisense oligonucleotide targeting APOB):** Discontinued in most markets due to hepatotoxicity

## Pathology

**Accelerated atherosclerosis:**
- Lifetime elevated LDL-C drives plaque in coronary, carotid, and peripheral arteries decades earlier than in the general population; cumulative cholesterol burden (LDL-C × years = cholesterol-year score) predicts events better than single measurements
- Imaging: Coronary artery calcium (CAC) score; carotid intima-media thickness (IMT); coronary CT angiography — useful for risk stratification and treatment decision-making in FH

**Aortic valve disease in HoFH:**
- Supravalvular and valvular aortic stenosis from lipid infiltration in aortic root; progressive → aortic valve replacement may be required in 3rd-4th decade in severe HoFH

**Statin intolerance:**
- 5-10% of patients discontinue statins due to muscle symptoms; objective statin-associated myopathy (CK elevation >3-10×) is rare; nocebo effect accounts for significant proportion; management: lower dose, alternate-day dosing, hydrophilic statins (rosuvastatin, pravastatin), switch statin; if truly intolerant → bempedoic acid (ACL inhibitor, doesn't affect skeletal muscle) + ezetimibe + PCSK9 inhibitor

**Pediatric FH:**
- Current guidelines recommend statin initiation at age 8-10 years in HeFH with LDL-C >160 mg/dL; early treatment reduces subclinical atherosclerosis progression; HoFH: treatment from age 2-5 with LDL apheresis + statin ± lomitapide

## Connections

- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — PCSK9 GOF mutations cause autosomal dominant FH (ADH3); evolocumab and alirocumab reduce LDL-C 50-60% add-on to statins; inclisiran (PCSK9 siRNA) reduces LDL-C ~50% with Q6M dosing; standard of care for FH not at LDL goal on maximally tolerated statin.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — FH accelerates atherosclerosis; HeFH untreated: 20× higher CVD risk; coronary atherosclerosis, tendon xanthomas, and xanthelasma are hallmarks; cumulative LDL-C burden predicts events; early statin initiation reduces atherosclerotic events in HeFH.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — FH results from impaired LDLR-mediated cholesterol clearance; LDLR mutations → fewer surface receptors → LDL-C >190 mg/dL (HeFH) or >500 mg/dL (HoFH LDLR null); excess cholesterol in macrophages → foam cells → atheromatous plaque.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — hepatocytes express >90% of plasma LDLR; LDLR-mediated LDL endocytosis is the primary clearance route; SREBP-2 upregulates LDLR after statin treatment; liver transplant in HoFH normalizes LDL-C — confirming hepatocytic LDLR as the disease driver.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — in FH, chronically elevated LDL-C → macrophage scavenger receptor (SR-A, CD36) uptake of oxidized LDL → foam cell formation; foam cells are the histological hallmark of the atheromatous plaque; FH macrophages exhibit exaggerated ox-LDL uptake vs. normolipidemic controls.
- `connects-to` → **[Stroke](../stroke/README.md)** — FH accelerates carotid and cerebrovascular atherosclerosis; HeFH patients have elevated carotid intima-media thickness (cIMT) and higher stroke risk vs. general population; statin + PCSK9 inhibitor reduces cIMT progression and ischemic stroke incidence in FH cohorts.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Familial hypercholesterolemia is defined by its toll on the heart: lifelong high LDL drives premature coronary disease — heterozygotes infarct in their 40s-50s while homozygotes can have MIs and aortic-valve stenosis in childhood; early intensive LDL lowering is lifesaving.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Atherosclerosis in FH starts at the endothelium: the lifelong excess of LDL infiltrates and is retained in the subendothelial intima, where oxidation activates endothelial cells to recruit monocytes — repeated for decades at FH's LDL levels, this builds plaque far earlier.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Vascular smooth muscle cells shape the FH atheroma: they migrate from the media into the intima, take up modified LDL to become foam cells, and lay down the collagen fibrous cap whose stability — or rupture — determines whether a plaque stays silent or causes infarction.
- `treated-by` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — Statins are the cornerstone of FH treatment: by inhibiting HMG-CoA reductase they upregulate hepatic LDL receptors to clear LDL, but FH patients—especially homozygotes with few functional receptors—often need high-intensity statins plus ezetimibe and PCSK9 inhibitors.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is central to FH: hepatocyte LDL receptors normally clear ~70% of circulating LDL, so the LDLR (or APOB/PCSK9) mutations of FH cripple this clearance → lifelong high LDL; the liver is thus the target of statins, PCSK9 inhibitors, apheresis and gene therapy.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — FH and hypertension are multiplicative cardiovascular risk factors: lifelong high LDL accelerates atherosclerosis while raised blood pressure adds shear stress and endothelial injury, so an FH patient who is also hypertensive faces especially early coronary disease.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Familial hypercholesterolemia is a lifelong assault on the cardiovascular system: from birth very high LDL accelerates atherosclerosis, so untreated heterozygotes get coronary disease decades early and homozygotes in childhood—early statin/PCSK9 therapy is essential.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Familial hypercholesterolemia and type 2 diabetes multiply cardiovascular risk together: FH's lifelong LDL burden plus diabetic dyslipidemia compound atherosclerosis—and although statins slightly raise diabetes risk, their cardiovascular benefit in FH far outweighs it.
- `connects-to` → **[NASH](../nash/README.md)** — Familial hypercholesterolemia and NASH are distinct lipid disorders of the liver: FH is a receptor defect that floods blood with LDL but spares the liver, while NASH is hepatic fat from insulin resistance—high LDL with a normal liver differs from fatty liver.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Familial hypercholesterolemia causes premature coronary disease that leads to heart failure: lifelong sky-high LDL drives early severe atherosclerosis and heart attacks, so untreated FH causes ischemic cardiomyopathy decades early.
- `connects-to` → **[Obesity](../obesity/README.md)** — Familial hypercholesterolemia and obesity stack cardiovascular risk: FH is a genetic LDL-receptor defect causing very high cholesterol, while obesity adds insulin resistance and inflammation—together compounding the premature atherosclerosis FH drives.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Familial hypercholesterolemia and chronic kidney disease are both potent cardiovascular risk amplifiers: FH from extreme LDL, CKD from vascular calcification and dyslipidemia, so an FH patient who also develops CKD faces compounded atherosclerotic risk.
- `connects-to` → **[APOE](../../03-molecular/apoe/README.md)** — FH and APOE both shape blood cholesterol but differently: FH is a single-gene defect in LDL clearance causing severe lifelong hypercholesterolemia, while APOE variants modify lipid levels and cardiovascular risk—monogenic versus polygenic cholesterol disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Coronary artery calcium scoring helps gauge risk in FH: lifelong high LDL drives calcified atherosclerotic plaque, so a CT calcium score quantifies accumulated arterial damage and refines who needs the most aggressive lipid lowering.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — FH's silent arterial damage is revealed by photon-based imaging: low-dose CT uses X-ray photons to measure coronary calcium, turning invisible decades of LDL-driven plaque buildup into a number that guides how intensively to treat.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Familial hypercholesterolemia writes itself on the skin: lifelong high LDL deposits cholesterol as tendon xanthomas (Achilles, knuckles) and eyelid xanthelasma, so these fatty bumps are physical clues that prompt lipid testing and family screening.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye flags familial hypercholesterolemia: a corneal arcus—a white lipid ring around the iris—appearing before age 45 strongly suggests it, so this ocular sign, like xanthomas, helps catch the inherited high cholesterol early enough to prevent heart attacks.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cultured skin fibroblasts revealed FH's cause: studying patients' fibroblasts, Brown and Goldstein discovered the LDL receptor and how its loss blocks cholesterol uptake—the Nobel work that explained FH and led to statins and PCSK9 inhibitors.

[^goldstein-1985-ldlr-nobel]: Goldstein JL, Brown MS. The LDL receptor. *Arterioscler Thromb Vasc Biol.* 2009;29(4):431-438. [doi:10.1161/ATVBAHA.108.179564](https://doi.org/10.1161/ATVBAHA.108.179564) · [PubMed 19299327](https://pubmed.ncbi.nlm.nih.gov/19299327/)
[^raal-2020-inclisiran-fh]: Raal FJ, Kallend D, Ray KK, et al. Inclisiran for the Treatment of Heterozygous Familial Hypercholesterolemia. *N Engl J Med.* 2020;382(16):1520-1530. [doi:10.1056/NEJMoa1913805](https://doi.org/10.1056/NEJMoa1913805) · [PubMed 32197277](https://pubmed.ncbi.nlm.nih.gov/32197277/)
[^watts-2020-hzfh-guidelines]: Watts GF, Gidding SS, Hegele RA, et al. International Atherosclerosis Society guidance for implementing best practice in the care of familial hypercholesterolaemia. *Nat Rev Cardiol.* 2023;20(12):845-869. [doi:10.1038/s41569-023-00892-0](https://doi.org/10.1038/s41569-023-00892-0) · [PubMed 37322181](https://pubmed.ncbi.nlm.nih.gov/37322181/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
