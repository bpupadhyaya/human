---
schema: human-scale-entry/v1
id: marfan-syndrome
name: Marfan Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Marfan syndrome is caused by germline FBN1 mutations; aortic root dilation (risk of dissection), ectopia lentis, tall stature with long limbs and arachnodactyly; losartan and beta-blockers slow aortic growth; prophylactic aortic surgery when root diameter reaches 5.0 cm."
aliases: ["Marfan syndrome", "Marfan's syndrome", "FBN1 syndrome", "fibrillin-1 Marfan", "Marfan aortic aneurysm", "Marfan aortic dissection", "Marfan ectopia lentis", "Marfan connective tissue", "MFS", "Marfan cardiovascular"]
sources:
  - id: dietz-1991-fbn1-marfan
    type: peer-reviewed
    cite: "Dietz HC, Cutting GR, Pyeritz RE, et al. Marfan syndrome caused by a recurrent de novo missense mutation in the fibrillin gene. Nature. 1991;352(6333):337-339."
    doi: "10.1038/352337a0"
    pmid: "1852208"
    url: "https://doi.org/10.1038/352337a0"
  - id: loeys-2010-ghent-criteria
    type: peer-reviewed
    cite: "Loeys BL, Dietz HC, Braverman AC, et al. The revised Ghent nosology for the Marfan syndrome. J Med Genet. 2010;47(7):476-485."
    doi: "10.1136/jmg.2009.072785"
    pmid: "20591885"
    url: "https://doi.org/10.1136/jmg.2009.072785"
cross_links:
  - target: 01-human/03-molecular/fbn1
    relation: connects-to
    note: "Germline FBN1 haploinsufficiency or dominant-negative mutations → Marfan syndrome; FBN1 LOF reduces microfibril scaffold → less TGF-β sequestration → excess TGF-β signaling → SMAD2/3 activation → aortic smooth muscle cell phenotypic switch → progressive aortic root aneurysm."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "FBN1 microfibrils bind LTBP (latent TGF-β binding protein) → sequester TGF-β in ECM; FBN1 LOF → reduced TGF-β sequestration → excess TGF-β → ERK and SMAD2/3 activation in aortic SMCs → MMP production → elastic lamina fragmentation → aneurysm formation."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "FBN1 LOF → excess TGF-β signaling → SMAD2/3 phosphorylation → nuclear translocation → aortic gene expression changes driving aneurysm; SMAD4 is the common SMAD that co-activates SMAD2/3 transcription; SMAD4 mutations in juvenile polyposis syndrome also cause aortic aneurysm."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "FBN1 fibrillin-1 microfibrils and collagen fibers are the two major structural components of the arterial wall ECM; fibrillin-1 provides elastic recoil; collagen provides tensile strength; Marfan syndrome (FBN1) and OI (COL1A1/2) both affect connective tissue integrity."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Losartan (AT1R blocker) reduces angiotensin II → attenuated TGF-β signaling in aortic SMCs → slower aortic root growth in MFS (COMPARE trial); AT1R-TGF-β crosstalk: angiotensin II stimulates TGF-β1 production and SMAD2/3 activation → MMP-mediated ECM degradation in aortic wall."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Fibronectin and fibrillin-1 are both major aortic ECM scaffolding proteins; fibronectin provides SMC adhesion substrate; fibrillin-1 provides elastic recoil; fibronectin deposition increases in Marfan aortic tissue as a compensatory response to fibrillin-1 microfibril failure."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Hypertension management is critical in Marfan syndrome: elevated SBP increases aortic wall shear stress → accelerated root aneurysm growth; beta-blockers (atenolol) reduce HR + BP + aortic pulsatility; losartan provides additional AT1R/TGF-β inhibition; target SBP <120 mmHg."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart and aorta carry Marfan's lethal risk: FBN1 deficiency lets excess TGF-β weaken the aortic media, producing progressive aortic-root dilatation that can dissect or rupture; β-blockers and losartan slow root growth, and prophylactic root replacement at ~5 cm prevents it."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The lens betrays Marfan syndrome: ectopia lentis — upward dislocation of the lens from stretched, failing zonular fibers (made of fibrillin-1) — is a cardinal diagnostic criterion present in ~60%; Marfan eyes are also myopic and prone to retinal detachment and early glaucoma."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The skeleton makes Marfan visible: tall stature with disproportionately long limbs and fingers (arachnodactyly), arm-span-to-height >1.05, pectus deformity, scoliosis, and joint hypermobility all stem from fibrillin-1's role in connective tissue — scored in the Ghent criteria."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The cardiovascular system carries Marfan's lethal risk: fibrillin-1 deficiency weakens the aortic media, so progressive aortic-root dilatation leads to dissection or rupture—the main cause of death—while mitral valve prolapse adds regurgitation; β-blockers/ARBs and surgery help."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Marfan is a disease of the aortic smooth-muscle-cell environment: fibrillin-1 loss frees excess TGF-β in the media, so vascular smooth muscle cells lose elastic-fiber anchorage and undergo apoptosis and phenotype switching—weakening the aortic wall toward aneurysm and dissection."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is an underrecognized Marfan target: weakened connective tissue predisposes to apical blebs and spontaneous pneumothorax (in ~5-10%), and emphysematous changes and restrictive disease from chest-wall deformity (pectus, scoliosis) can further impair breathing."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts build Marfan's failing scaffold: they secrete fibrillin-1 to assemble microfibrils that lend connective tissue elasticity and sequester TGF-β, so FBN1 mutations leave microfibrils defective—weakening aorta, lens zonules and ligaments and unleashing TGF-β."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin shows Marfan's connective-tissue defect: deficient fibrillin-1 microfibrils reduce dermal elasticity, producing striae atrophicae (stretch marks) and sometimes thin, hyperextensible skin—visible clues to a disorder whose real danger lies in the aorta."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Marfan syndrome raises stroke risk through vascular fragility: aortic root disease can throw cardioembolic clots, and the same fibrillin-1 weakness predisposes to cervical artery dissection—so an aortic disease can also strike the brain."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Marfan syndrome weakens the lungs: fibrillin-deficient connective tissue forms apical blebs that rupture, causing spontaneous pneumothorax, and chest-wall deformity restricts breathing—so respiratory complications add to the cardiovascular and skeletal features."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Marfan's skeletal overgrowth reflects disordered bone formation: excess TGF-beta signaling from fibrillin-1 loss drives long-bone overgrowth, giving tall stature and arachnodactyly—so bone-forming cells build too much skeleton on a faulty connective scaffold."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Dural ectasia is a hallmark Marfan feature: weakened connective tissue lets the dura around the lower spine balloon out, causing back pain and headaches and serving as a diagnostic criterion—showing Marfan's reach into the nervous system's coverings."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Marfan syndrome shows in the skin and soft tissue: fibrillin-1 loss weakens connective tissue throughout, producing striae (stretch marks) without weight change, thin skin and hernias—visible signs of the same defect that endangers the aorta."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy is dangerous in Marfan syndrome: the hemodynamic load and hormonal softening of connective tissue sharply raise the risk of aortic dissection, so the reproductive years demand careful cardiac monitoring and counseling in affected women."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Marfan's tall stature is not from growth hormone: unlike pituitary gigantism, the overgrowth comes from defective fibrillin-1 connective tissue, so patients are tall with long limbs and arachnodactyly despite normal growth-hormone levels—a key diagnostic distinction."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Marfan can weaken heart muscle itself: beyond valve and aortic disease, excess TGF-beta signaling produces an intrinsic cardiomyopathy in which cardiomyocyte dysfunction mildly dilates and weakens the left ventricle, so the heart is monitored even when valves look normal."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "The Marfan aorta fails through medial degeneration: fibrillin loss and unleashed TGF-beta fragment elastic fibers and drive fibrosis in the vessel wall, weakening it until the aortic root dilates and risks dissection—the syndrome's lethal complication."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Marfan vessels show endothelial dysfunction: the abnormal fibrillin matrix and altered TGF-beta signaling impair the endothelial cells lining the aorta, reducing flow-mediated dilation and adding to the wall stress that drives aneurysm."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Marfan's weak connective tissue threatens oxygen supply through pneumothorax: fragile apical lung blebs rupture and collapse the lung, cutting off air exchange—a recurrent emergency in tall, Marfan-bodied patients."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help weaken the Marfan aorta: they infiltrate the aneurysmal aortic wall and release proteases that chew through the elastic media, adding to the matrix breakdown that drives dilation toward dissection."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Marfan aneurysms are fueled by overactive mTOR: disrupted fibrillin and TGF-β signaling ramp up mTOR in the aortic wall, driving the smooth-muscle changes behind aortic dilation—so rapamycin-class drugs are studied to slow it."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Marfan often enlarges the spinal dura around the brain's continuation: dural ectasia—ballooning of the dural sac—is a common, weakly symptomatic feature that, found on imaging, helps confirm the diagnosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Marfan aortas grow weak partly through AKT signaling: disrupted fibrillin and TGF-beta ramp up AKT alongside mTOR in the vessel wall, driving the smooth-muscle changes behind aneurysm, so this growth axis is studied as a drug target."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation via NF-kB worsens the Marfan aorta: the failing elastic wall activates this inflammatory switch, recruiting cells and enzymes that degrade the matrix further, accelerating the dilation toward dissection."
---

# Marfan Syndrome

## Overview

**Marfan syndrome (MFS)** is a systemic **connective tissue disorder** caused by autosomal dominant germline mutations in **FBN1** (15q21.1), encoding fibrillin-1 — the principal structural protein of elastic microfibrils in the extracellular matrix. Marfan syndrome was first described by Antoine Marfan in 1896 (a patient named Gabrielle, with arachnodactyly and long limbs); the FBN1 gene was identified as the causative gene by Dietz et al. in 1991 [^dietz-1991-fbn1-marfan]. Marfan syndrome affects approximately **1 in 5,000-10,000** individuals worldwide (~200,000 in the United States), with equal sex distribution and autosomal dominant inheritance; ~25% of cases arise from de novo FBN1 mutations with no family history.

MFS is a **multi-system disorder** defined by cardiovascular, ocular, and skeletal features arising from fibrillin-1 microfibril dysfunction in multiple tissues. The **life-threatening complication** is **aortic root aneurysm** (present in ~70-80% of adults) → aortic dissection (Type A, involving ascending aorta) — the historical primary cause of premature death in Marfan syndrome (median survival ~40-50 years pre-1970). Modern management — beta-blockers, losartan, and prophylactic aortic root replacement — has extended median survival to >70 years. Revised Ghent criteria (Loeys et al. 2010) provide systematic diagnostic criteria integrating aortic measurements, ectopia lentis, FBN1 genotype, and systemic features [^loeys-2010-ghent-criteria].

**Marfan syndrome vs. related heritable thoracic aortic aneurysm syndromes (HTAAS):**

| Syndrome | Gene | Cardiac | Ocular | Skeletal | Distinguishing |
|---|---|---|---|---|---|
| Marfan (MFS) | FBN1 | Aortic root dilation, MVP | Ectopia lentis (~60%) | Tall, arachnodactyly, scoliosis | Fibrillin-1 LOF |
| Loeys-Dietz type 1 (LDS1) | TGFBR1 | Aortic root + branch vessel | Hypertelorism, cleft palate | Severe scoliosis, craniosynostosis | More aggressive aneurysm |
| Loeys-Dietz type 2 (LDS2) | TGFBR2 | Similar to LDS1 | Normal | Similar | Bifid uvula |
| Vascular EDS (vEDS) | COL3A1 | Aortic dissection, arterial rupture | Normal | Normal | No aortic root dilation; rupture |
| MASS phenotype | FBN1 | No aortic dilation | No ectopia lentis | Marfanoid | Subclinical FBN1 mutations |

## Structure

### Genetic basis of Marfan syndrome

**FBN1 mutation spectrum:**
- Over 3,000 distinct FBN1 mutations catalogued; most are unique to individual families (private mutations)
- Missense (~35%), nonsense/frameshift (~25%), splice site (~20%), large rearrangements (~10-15%), in-frame insertions/deletions (~5%)
- **Cysteine substitutions in cbEGF domains**: most common pathogenic missense type; disrupts disulfide bonding → dominant-negative protein misincorporated into microfibrils → most severe phenotype
- **Neonatal Marfan zone (exons 24-32)**: cysteine substitutions in cbEGF domains 14-20 → neonatal Marfan syndrome: severe mitral and tricuspid valve disease at birth, pulmonary emphysema, hyperflexible joints, arachnodactyly; cardiac failure in infancy; poorest prognosis; no significant aortic dilation at birth
- De novo mutations: ~25% of MFS; parents unaffected; recurrence risk low for unaffected parents (<1%); offspring of affected individual = 50% risk

**FBN1-related conditions (allelic to MFS):**
- **Ectopia lentis syndrome**: FBN1 mutations causing isolated lens dislocation without systemic features; may be early/attenuated Marfan; Ghent criteria classify separately
- **MASS phenotype**: myopia, MVP, aortic dilation (borderline), striae, skeletal features — incomplete Marfan phenotype; some FBN1 variants; normal life expectancy
- **Familial thoracic aortic aneurysm**: subset caused by FBN1 mutations with predominantly cardiovascular features; classified separately from MFS

**Molecular pathogenesis:**
- Structural: FBN1 haploinsufficiency → 50% normal microfibril scaffold → mechanically weaker elastic fibers → greater wall stress per cycle → fatigue failure → aneurysm
- Biochemical (TGF-β excess): FBN1 microfibrils tether LTBP1/3 → sequester latent TGF-β in ECM; FBN1 LOF → less TGF-β sequestration → elevated TGF-β activity in aortic media → SMAD2/3 + ERK1/2 → MMP9 overexpression → elastic laminae fragmentation → vascular smooth muscle cell (vSMC) apoptosis → aortic wall weakening
- TGF-β excess confirmed in human MFS aortic tissue: pSMAD2 elevated 2-4x vs. control; correlates with aneurysm severity

## Function

### Cardiovascular manifestations (primary morbidity and mortality)

**Aortic root aneurysm:**
- Dilation of the sinuses of Valsalva (the aortic root); detected by echocardiography
- Present in ~70-80% of adult MFS patients; progressive over time; growth rate ~0.5-1.5 mm/year (varies)
- **Aortic Z-score**: age- and BSA-adjusted measurement; Z-score ≥2 at any aortic site is Ghent criterion A; Z-score ≥3 is highly significant
- Risk of Type A aortic dissection (ascending aorta): rises sharply at root diameter >5.0 cm; catastrophic if untreated; emergent surgical repair mortality ~25-30%; predicted by root diameter + rate of growth
- **Type B dissection** (descending aorta): less common in Marfan; may complicate preexisting aortic dilation or after Type A repair

**Mitral valve disease:**
- MVP (mitral valve prolapse) in ~80% of MFS; fibrillin-1 microfibrils normally support mitral leaflet structure; FBN1 LOF → myxomatous valve changes → leaflet redundancy, chordal elongation
- Mitral regurgitation (MR): mild in most; severe MR requiring repair in ~10-20% of patients over a lifetime; most common cardiac complication requiring intervention in childhood
- Management: echocardiography every 1-2 years; beta-blocker (also slows MR progression and aortic growth)

**Arrhythmias:**
- Atrial fibrillation: elevated risk from mitral regurgitation, aortic dilation; may occur at younger age than general population
- Ventricular arrhythmia: rarely reported; sudden cardiac death very rare in MFS (unlike CPVT, HCM)

### Ocular manifestations

**Ectopia lentis (lens subluxation, ~60% of MFS):**
- Fibrillin-1 is the primary structural protein of ocular zonular fibers (the suspensory ligaments of the lens); FBN1 LOF → zonular weakness → lens subluxation
- Direction: classically superotemporal (upward-outward) in Marfan; contrast with homocystinuria (inferotemporal) and Weill-Marchesani (inferior, microspherophakia)
- Detected by slit-lamp examination (dilation required); present from childhood; may be stable or progressive
- Complications: phacodonesis (tremulous lens), monocular diplopia, high myopia (from axial length increase + refractive error), complete dislocation (zonulysis) → pupillary block → acute glaucoma
- Management: optical correction of myopia/astigmatism; amblyopia treatment in children; surgical lensectomy (pars plana lensectomy/vitrectomy) for severe dislocation or reduced vision; avoid hard contact lens in dislocation

**Myopia:**
- Axial myopia in ~70% of MFS (elongated globe); often severe (−5 to −20 D)
- Increased risk of retinal detachment from high myopia; annual dilated fundus exam essential

**Other ocular features:**
- Flat cornea (cornea plana): flattened corneal curvature → reduced refracting power
- Increased risk of glaucoma (open angle) even without lens subluxation
- Reduced pupil dilation (miosis) from iris hypoplasia

### Skeletal manifestations

**Height and body proportions:**
- Tall stature: mean adult height ~191 cm (males), ~175 cm (females) in classical MFS; usually above 95th percentile
- **Dolichostenomelia** (long, thin limbs): arm span > height by >1.05× ratio; reduced upper/lower segment ratio (<0.85 in adults); measured clinically
- **Arachnodactyly** (long, slender fingers and toes): Walker-Murdoch wrist sign (thumb and little finger overlap when wrapped around contralateral wrist; a sign with ~87% sensitivity); Steinberg thumb sign (thumb extends beyond ulnar border of hand when folded into palm)

**Chest wall deformities:**
- Pectus excavatum (sunken chest, ~50%) or pectus carinatum (prominent sternum, ~15%)
- Pectus excavatum can impair cardiac function if severe (reduced venous return); correctable surgically (Nuss procedure) or cosmetically

**Spinal features:**
- Scoliosis: ~60-70%; often progressive in adolescence; bracing in mild-moderate curves; spinal fusion for severe curves
- Spondylolisthesis (vertebral slippage): L5-S1 most common; pain, radiculopathy
- Dural ectasia: widening of the dural sac in lumbar spine (from dural weakness); present in ~90% of MFS adults; detected by MRI; causes low back pain, neurologic symptoms from nerve root impingement

**Craniofacial features:**
- Dolichocephaly (long, narrow skull), malar hypoplasia, deep-set eyes, high-arched palate, crowded teeth
- Retrognathia (recessed jaw); temporomandibular joint pain

**Foot:**
- Pes planus (flat feet) from ligamentous laxity; hindfoot valgus; custom orthotics

## Pathology

### Diagnosis — Revised Ghent criteria (2010)

**Core criteria:**
- **Aortic root dilation** (Z-score ≥2 or aortic dissection) — major cardiac criterion
- **Ectopia lentis** — major ocular criterion
- **FBN1 pathogenic variant** — genetic criterion
- **Systemic score** ≥7 (scoring: wrist + thumb sign 3; wrist OR thumb sign 1; pectus carinatum 2; pectus excavatum 1; hindfoot deformity 2; pes planus 1; pneumothorax 2; dural ectasia 2; protrusio acetabulae 2; reduced US/LS ratio AND arm span >1.05 × height AND no severe scoliosis 1; scoliosis/thoracolumbar kyphosis 1; reduced elbow extension 1; 3/5 facial features 1; skin striae 1; myopia 1; MVP 1)

**Diagnostic pathways (Ghent 2010):**
1. **Definite MFS in index patient**: aortic root dilation (Z≥2) + ectopia lentis; OR aortic root dilation + FBN1 pathogenic variant; OR aortic root dilation + systemic score ≥7; OR ectopia lentis + FBN1 pathogenic variant (with aortic root dilation known in other family members)
2. **Definite MFS in relative of diagnosed proband**: ectopia lentis; OR aortic root dilation (Z≥2 or dissection); OR systemic score ≥7

**Differential diagnosis:**
- Loeys-Dietz syndrome (TGFBR1/2, SMAD3, TGFB2/3): aortic aneurysm; hypertelorism, bifid uvula, cleft palate; more aggressive vascular disease; TGFBR1/2 sequencing
- Homocystinuria (CBS gene defect): inferior ectopia lentis, Marfanoid body habitus, intellectual disability, thrombosis; plasma homocysteine elevated; AR inheritance; betaine/B6 treatment
- Congenital contractural arachnodactyly (FBN2): arachnodactyly, camptodactyly (flexion contractures), ear crumpling; no aortic dilation; FBN2 mutations
- MASS phenotype (FBN1): borderline aortic measurements; no ectopia lentis; below threshold for MFS diagnosis
- Ehlers-Danlos syndrome hypermobile type (hEDS): joint hypermobility, skin extensibility; no aortic root dilation; COL5A1/2 genes for classical EDS

**Surveillance and management:**
- **Annual echocardiography**: aortic root and ascending aorta measurements; more frequent if root ≥4.5 cm or growing rapidly
- **CT/MRI aorta** (baseline and then every 3-5 years): assess full aorta + branch vessels; at time of aortic dissection, annually post-dissection
- **Beta-blocker (atenolol, propranolol)**: reduce hemodynamic shear stress on aortic root; proven to slow root growth rate; lifelong
- **Losartan (25-100 mg/day)**: AT1R blockade → reduces TGF-β signaling → slows aortic root growth; often combined with beta-blocker; COMPARE trial data support this approach
- **Prophylactic aortic root replacement**:
  - Trigger diameter: ≥5.0 cm (standard); ≥4.5 cm with family history of dissection/rapid growth; ≥4.0 cm if concurrent pregnancy planned or severe AR
  - **David valve-sparing root replacement**: preferred in young patients with competent aortic valve — preserves native valve, avoids anticoagulation; excellent long-term freedom from reoperation (~90% at 10 years)
  - **Bentall procedure** (composite graft + valve): for significant aortic regurgitation or elderly; mechanical valve → lifelong anticoagulation; tissue valve → risk of structural deterioration
- **Avoid isometric exercise and contact sports**: high-impact, breath-holding, or competitive sports increase aortic shear stress → increased dissection risk; swimming, cycling, golf generally permitted; individualize with cardiology
- **MRI rather than CT** where feasible: avoid radiation for serial surveillance (MFS patients require decades of imaging)
- **Pregnancy in Marfan syndrome**: high-risk pregnancy; aortic root ≥4.0 cm → increased dissection risk during labor and postpartum; cesarean delivery recommended for root ≥4.0 cm; losartan discontinued (teratogenic; switch to labetalol); surveillance echocardiography monthly in 3rd trimester + 6 months postpartum
- **Genetic counseling**: AD inheritance; 50% risk per child; prenatal diagnosis available; PGT for couples who wish to avoid transmission
- **Ophthalmology**: annual dilated eye exam; refractive correction; amblyopia treatment in children; glaucoma monitoring; retinal detachment surveillance

## Connections

- `connects-to` → **[FBN1](../../03-molecular/fbn1/README.md)** — Germline FBN1 haploinsufficiency or dominant-negative mutations → Marfan syndrome; FBN1 LOF reduces microfibril scaffold → less TGF-β sequestration → excess TGF-β signaling → SMAD2/3 activation → aortic smooth muscle cell phenotypic switch → progressive aortic root aneurysm.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — FBN1 microfibrils bind LTBP (latent TGF-β binding protein) → sequester TGF-β in ECM; FBN1 LOF → reduced TGF-β sequestration → excess TGF-β → ERK and SMAD2/3 activation in aortic SMCs → MMP production → elastic lamina fragmentation → aneurysm formation.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — FBN1 LOF → excess TGF-β signaling → SMAD2/3 phosphorylation → nuclear translocation → aortic gene expression changes driving aneurysm; SMAD4 is the common SMAD that co-activates SMAD2/3 transcription; SMAD4 mutations in juvenile polyposis syndrome also cause aortic aneurysm.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — FBN1 fibrillin-1 microfibrils and collagen fibers are the two major structural components of the arterial wall ECM; fibrillin-1 provides elastic recoil; collagen provides tensile strength; Marfan syndrome (FBN1) and OI (COL1A1/2) both affect connective tissue integrity.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — losartan (AT1R blocker) reduces angiotensin II → attenuated TGF-β signaling in aortic SMCs → slower aortic root growth in MFS (COMPARE trial); AT1R-TGF-β crosstalk: angiotensin II stimulates TGF-β1 production and SMAD2/3 activation → MMP-mediated ECM degradation in aortic wall.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — fibronectin and fibrillin-1 are both major aortic ECM scaffolding proteins; fibronectin provides SMC adhesion substrate; fibrillin-1 provides elastic recoil; fibronectin deposition increases in Marfan aortic tissue as a compensatory response to fibrillin-1 microfibril failure.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — hypertension management is critical in Marfan syndrome: elevated SBP increases aortic wall shear stress → accelerated root aneurysm growth; beta-blockers (atenolol) reduce HR + BP + aortic pulsatility; losartan provides additional AT1R/TGF-β inhibition; target SBP <120 mmHg.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart and aorta carry Marfan's lethal risk: FBN1 deficiency lets excess TGF-β weaken the aortic media, producing progressive aortic-root dilatation that can dissect or rupture; β-blockers and losartan slow root growth, and prophylactic root replacement at ~5 cm prevents it.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The lens betrays Marfan syndrome: ectopia lentis — upward dislocation of the lens from stretched, failing zonular fibers (made of fibrillin-1) — is a cardinal diagnostic criterion present in ~60%; Marfan eyes are also myopic and prone to retinal detachment and early glaucoma.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The skeleton makes Marfan visible: tall stature with disproportionately long limbs and fingers (arachnodactyly), arm-span-to-height >1.05, pectus deformity, scoliosis, and joint hypermobility all stem from fibrillin-1's role in connective tissue — scored in the Ghent criteria.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — The cardiovascular system carries Marfan's lethal risk: fibrillin-1 deficiency weakens the aortic media, so progressive aortic-root dilatation leads to dissection or rupture—the main cause of death—while mitral valve prolapse adds regurgitation; β-blockers/ARBs and surgery help.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Marfan is a disease of the aortic smooth-muscle-cell environment: fibrillin-1 loss frees excess TGF-β in the media, so vascular smooth muscle cells lose elastic-fiber anchorage and undergo apoptosis and phenotype switching—weakening the aortic wall toward aneurysm and dissection.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is an underrecognized Marfan target: weakened connective tissue predisposes to apical blebs and spontaneous pneumothorax (in ~5-10%), and emphysematous changes and restrictive disease from chest-wall deformity (pectus, scoliosis) can further impair breathing.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts build Marfan's failing scaffold: they secrete fibrillin-1 to assemble microfibrils that lend connective tissue elasticity and sequester TGF-β, so FBN1 mutations leave microfibrils defective—weakening aorta, lens zonules and ligaments and unleashing TGF-β.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin shows Marfan's connective-tissue defect: deficient fibrillin-1 microfibrils reduce dermal elasticity, producing striae atrophicae (stretch marks) and sometimes thin, hyperextensible skin—visible clues to a disorder whose real danger lies in the aorta.
- `connects-to` → **[Stroke](../stroke/README.md)** — Marfan syndrome raises stroke risk through vascular fragility: aortic root disease can throw cardioembolic clots, and the same fibrillin-1 weakness predisposes to cervical artery dissection—so an aortic disease can also strike the brain.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Marfan syndrome weakens the lungs: fibrillin-deficient connective tissue forms apical blebs that rupture, causing spontaneous pneumothorax, and chest-wall deformity restricts breathing—so respiratory complications add to the cardiovascular and skeletal features.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Marfan's skeletal overgrowth reflects disordered bone formation: excess TGF-beta signaling from fibrillin-1 loss drives long-bone overgrowth, giving tall stature and arachnodactyly—so bone-forming cells build too much skeleton on a faulty connective scaffold.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Dural ectasia is a hallmark Marfan feature: weakened connective tissue lets the dura around the lower spine balloon out, causing back pain and headaches and serving as a diagnostic criterion—showing Marfan's reach into the nervous system's coverings.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Marfan syndrome shows in the skin and soft tissue: fibrillin-1 loss weakens connective tissue throughout, producing striae (stretch marks) without weight change, thin skin and hernias—visible signs of the same defect that endangers the aorta.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy is dangerous in Marfan syndrome: the hemodynamic load and hormonal softening of connective tissue sharply raise the risk of aortic dissection, so the reproductive years demand careful cardiac monitoring and counseling in affected women.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Marfan's tall stature is not from growth hormone: unlike pituitary gigantism, the overgrowth comes from defective fibrillin-1 connective tissue, so patients are tall with long limbs and arachnodactyly despite normal growth-hormone levels—a key diagnostic distinction.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Marfan can weaken heart muscle itself: beyond valve and aortic disease, excess TGF-beta signaling produces an intrinsic cardiomyopathy in which cardiomyocyte dysfunction mildly dilates and weakens the left ventricle, so the heart is monitored even when valves look normal.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — The Marfan aorta fails through medial degeneration: fibrillin loss and unleashed TGF-beta fragment elastic fibers and drive fibrosis in the vessel wall, weakening it until the aortic root dilates and risks dissection—the syndrome's lethal complication.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Marfan vessels show endothelial dysfunction: the abnormal fibrillin matrix and altered TGF-beta signaling impair the endothelial cells lining the aorta, reducing flow-mediated dilation and adding to the wall stress that drives aneurysm.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Marfan's weak connective tissue threatens oxygen supply through pneumothorax: fragile apical lung blebs rupture and collapse the lung, cutting off air exchange—a recurrent emergency in tall, Marfan-bodied patients.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help weaken the Marfan aorta: they infiltrate the aneurysmal aortic wall and release proteases that chew through the elastic media, adding to the matrix breakdown that drives dilation toward dissection.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Marfan aneurysms are fueled by overactive mTOR: disrupted fibrillin and TGF-β signaling ramp up mTOR in the aortic wall, driving the smooth-muscle changes behind aortic dilation—so rapamycin-class drugs are studied to slow it.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Marfan often enlarges the spinal dura around the brain's continuation: dural ectasia—ballooning of the dural sac—is a common, weakly symptomatic feature that, found on imaging, helps confirm the diagnosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Marfan aortas grow weak partly through AKT signaling: disrupted fibrillin and TGF-beta ramp up AKT alongside mTOR in the vessel wall, driving the smooth-muscle changes behind aneurysm, so this growth axis is studied as a drug target.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation via NF-kB worsens the Marfan aorta: the failing elastic wall activates this inflammatory switch, recruiting cells and enzymes that degrade the matrix further, accelerating the dilation toward dissection.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^dietz-1991-fbn1-marfan]: Dietz HC, Cutting GR, Pyeritz RE, et al. Marfan syndrome caused by a recurrent de novo missense mutation in the fibrillin gene. *Nature.* 1991;352(6333):337-339. [doi:10.1038/352337a0](https://doi.org/10.1038/352337a0) · [PubMed 1852208](https://pubmed.ncbi.nlm.nih.gov/1852208/)
[^loeys-2010-ghent-criteria]: Loeys BL, Dietz HC, Braverman AC, et al. The revised Ghent nosology for the Marfan syndrome. *J Med Genet.* 2010;47(7):476-485. [doi:10.1136/jmg.2009.072785](https://doi.org/10.1136/jmg.2009.072785) · [PubMed 20591885](https://pubmed.ncbi.nlm.nih.gov/20591885/)
