---
schema: human-scale-entry/v1
id: ckd
name: Chronic Kidney Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Progressive irreversible loss of kidney function (GFR <60 mL/min for >3 months) from diabetes, hypertension, or glomerulonephritis. Staged G1-G5 by GFR; complications include anemia, hyperparathyroidism, and uremia. End-stage managed by dialysis or transplantation."
aliases: ["CKD", "chronic renal failure", "chronic renal insufficiency", "end-stage kidney disease", "ESKD"]
sources:
  - id: kdigo-2012-ckd
    type: clinical-guideline
    cite: "Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int Suppl. 2013;3(1):1-150."
    doi: "10.1038/kisup.2012.73"
    url: "https://doi.org/10.1038/kisup.2012.73"
  - id: levey-2012-ckd-lancet
    type: peer-reviewed
    cite: "Levey AS, Coresh J. Chronic kidney disease. Lancet. 2012;379(9811):165-180."
    doi: "10.1016/S0140-6736(11)60178-5"
    pmid: "21840587"
    url: "https://doi.org/10.1016/S0140-6736(11)60178-5"
  - id: coresh-2007-prevalence
    type: peer-reviewed
    cite: "Coresh J, Selvin E, Stevens LA, et al. Prevalence of chronic kidney disease in the United States. JAMA. 2007;298(17):2038-2047."
    doi: "10.1001/jama.298.17.2038"
    pmid: "17986697"
    url: "https://doi.org/10.1001/jama.298.17.2038"
cross_links:
  - target: 01-human/06-organ/kidney
    relation: targets
    note: "CKD is the progressive structural and functional destruction of renal parenchyma — tubular atrophy, glomerulosclerosis, interstitial fibrosis, and nephron loss; the kidney is the primary target organ."
  - target: 01-human/07-system/renal-system
    relation: part-of
    note: "CKD is the defining pathological state of the renal system; GFR decline progressively impairs all renal functions including solute clearance, acid-base balance, erythropoietin secretion, and vitamin D activation."
  - target: 01-human/03-molecular/erythropoietin
    relation: modulates
    note: "CKD reduces erythropoietin (EPO) synthesis from peritubular fibroblasts as nephron mass declines; anemia of CKD is the direct consequence of EPO deficiency and is treated with recombinant EPO (darbepoetin alfa, epoetin alfa)."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "CKD and hypertension are bidirectionally causal: hypertension is the second leading cause of CKD (via nephrosclerosis); CKD causes hypertension through RAAS activation, sodium retention, and reduced nitric oxide. Controlling BP (target <130/80) slows CKD progression."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "CREDENCE (canagliflozin): 30% reduction in kidney endpoint in T2D + CKD; DAPA-CKD (dapagliflozin): 39% reduction in eGFR decline/dialysis/renal death in CKD with and without T2D; SGLT2 inhibitors slow CKD progression via tubuloglomerular feedback and anti-fibrotic effects."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "FGF23 rises 100-1000× in CKD → suppresses 1α-hydroxylase → reduced calcitriol → secondary hyperparathyroidism and CKD-MBD; very high FGF23 predicts LVH, heart failure, and mortality in dialysis patients independent of traditional risk factors."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "OPN is upregulated in injured renal tubular epithelium → integrin αvβ3 on macrophages → macrophage recruitment and pro-inflammatory activation → tubulointerstitial fibrosis; urinary OPN predicts CKD progression; OPN inhibits calcium oxalate crystal adhesion (stone inhibitor)."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "IgA nephropathy is a leading cause of CKD in young adults; mesangial IgA deposition → complement + CCL2 → tubulointerstitial fibrosis → eGFR decline; 20-40% of IgAN reach ESRD within 20 years; sparsentan (ETA/AT1R dual blocker) and iptacopan are disease-modifying therapies."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hepcidin is elevated in CKD from reduced renal clearance and chronic inflammation; elevated hepcidin → functional iron deficiency → ESA hyporesponsiveness in CKD anemia; HIF-PHIs (roxadustat, daprodustat) suppress hepcidin via EPO→ERFE→BMP-SMAD inhibition."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "CKD anemia is the overlap of EPO deficiency and ACD mechanisms: reduced EPO from peritubular cell loss + hepcidin elevation from CKD inflammation/reduced clearance → combined functional iron deficiency + erythropoietic failure; IV iron + ESA are first-line for CKD anemia."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "aHUS from complement dysregulation (CFH/CFI mutations) causes progressive CKD; ~50% of untreated aHUS patients reach ESRD within 1 year; eculizumab/ravulizumab reverse TMA and may improve eGFR; renal transplant requires lifelong C5 inhibition in high-risk CFH mutations."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "SCD causes sickle cell nephropathy via medullary sickling (high osmolarity + low pO2 in vasa recta → medullary ischaemia) → hyposthenuria, papillary necrosis, proteinuria; progressive CKD in ~30% HbSS by age 40; ACE inhibitors + hydroxyurea slow progression."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Severe falciparum malaria causes AKI in 4-8% (haemoglobinuria + microvascular obstruction + cytokine storm); cerebral malaria + AKI → high mortality; repeated malaria episodes contribute to CKD burden in endemic populations."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Dialysis patients have elevated sclerostin from impaired renal clearance + uremic Wnt suppression → adynamic bone disease; elevated sclerostin correlates with vascular calcification and mortality in CKD; romosozumab not approved in severe CKD due to CV risk."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "CKD-associated pruritus (formerly uremic pruritus) causes PN-like nodules in dialysis patients; uremic toxins activate μ-opioid and κ-opioid receptors on pruriceptors; difelikefalin (κ-opioid agonist; FDA 2021 for CKD-aP on HD) reduces itch and may prevent PN nodule formation."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes is the leading cause of chronic kidney disease: chronic hyperglycemia damages the glomerular filter (diabetic nephropathy), causing proteinuria and progressive function loss, so diabetic kidney disease drives most dialysis need—SGLT2 inhibitors now slow it."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "CKD and atherosclerosis form a vicious cardiorenal cycle: declining kidney function accelerates vascular calcification and atherosclerosis, so cardiovascular disease—not kidney failure—is the leading cause of death in CKD."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "CKD deranges calcium and bone metabolism (CKD-MBD): failing kidneys can't activate vitamin D or excrete phosphate, lowering calcium and driving secondary hyperparathyroidism and vascular calcification—so calcium, phosphate and PTH are tightly managed in CKD."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "Podocyte loss is a key driver of progressive CKD: these non-dividing cells form the glomerular filter, and when injury (by diabetes, hypertension or FSGS) kills them, the barrier leaks protein and scars, so podocyte depletion predicts irreversible decline."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "CKD often begins in the glomerulus: damage to the filtering tuft causes proteinuria and falling filtration, and surviving glomeruli hyperfilter to compensate—a maladaptive overwork that scars them too, driving the relentless nephron loss of chronic kidney disease."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "CKD and cardiovascular disease are lethally intertwined: most people with CKD die of heart disease, not kidney failure, because uremia, fluid overload and hypertension accelerate atherosclerosis—so the failing kidney is a powerful cardiac risk factor."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Failing kidneys can't dump potassium: as filtration drops, potassium builds up, and hyperkalemia—worsened by the ACE inhibitors and ARBs used to protect the kidney—can stop the heart, so it is among CKD's most urgent, monitored complications."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Heart and kidney failure drive each other (cardiorenal syndrome): CKD's fluid overload, hypertension, and anemia strain the heart, while a failing heart underperfuses the kidney—so the two organs decline together and share treatments like SGLT2 inhibitors."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "CKD cripples vitamin D activation: damaged kidneys can't perform the final hydroxylation to active calcitriol, so calcium absorption falls and parathyroid hormone rises—driving the renal bone disease that defines CKD's mineral and bone disorder."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "CKD progresses through fibrosis: whatever the initial insult, tubulointerstitial fibrosis is the final common pathway that scars nephrons beyond repair, so the degree of fibrosis on biopsy predicts decline better than the original diagnosis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "CKD throws phosphorus out of balance: failing kidneys can't excrete phosphate, so it rises and—with FGF23, PTH and low vitamin D—drives the bone disease and vascular calcification of CKD-mineral bone disorder."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Angiotensin II accelerates CKD and is the key drug target: it raises glomerular pressure and drives scarring, so ACE inhibitors and ARBs that block it slow progression and reduce proteinuria—the cornerstone of renoprotection."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "CKD and the heart fail together in cardiorenal syndrome: fluid overload, hypertension, anemia and mineral disturbance strain the heart, while heart failure starves the kidneys of flow, so most CKD patients die of cardiovascular causes."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Aldosterone drives the scarring that worsens CKD: beyond raising blood pressure, it promotes fibrosis and inflammation in the kidney, which is why mineralocorticoid blockers like finerenone slow progression on top of ACE inhibitors."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "CKD unleashes bone-dissolving osteoclasts: phosphate retention and secondary hyperparathyroidism overstimulate osteoclasts, the high-turnover renal osteodystrophy that weakens bone and spills calcium and phosphate into vessels."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "CKD turns the blood acidic: failing kidneys cannot excrete the body's daily acid load or regenerate bicarbonate, so hydrogen ions build up into a metabolic acidosis that wastes muscle and bone and is treated with bicarbonate."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "CKD poisons the brain: retained uremic toxins cause the confusion, fatigue, and—in advanced failure—the asterixis and seizures of uremic encephalopathy, symptoms that dialysis is meant to clear."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "CKD wrecks the endothelium: uremic toxins and mineral imbalance injure the vessel-lining cells and calcify artery walls, driving the accelerated atherosclerosis that makes heart disease, not kidney failure, the usual cause of death."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging stages CKD's structure: ultrasound and CT photons show shrunken, scarred kidneys or obstruction, while nuclear scans measure the failing filtration that blood tests only estimate."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "CKD itches relentlessly: retained toxins and mineral imbalance cause uremic pruritus, which patients scratch into prurigo nodularis, one of the most distressing symptoms of advanced kidney failure."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "CKD progresses through fibroblasts: injured kidneys activate myofibroblasts that lay down interstitial scar, the common final pathway by which any kidney disease marches toward failure."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the failing filter: as CKD advances, the glomerular basement membrane thickens and wrinkles while podocyte foot processes flatten and fuse, the ultrastructural decay that lets protein leak and filtration fall."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Failing kidneys leave the blood thin: the diseased kidney makes too little erythropoietin to tell the marrow to build red cells, so anemia is a near-universal companion of CKD, treated with EPO and iron."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "CKD upends magnesium balance: as the kidney loses its power to excrete the mineral, magnesium can build to dangerous levels — especially with magnesium-containing laxatives or antacids — risking weakness and heart-rhythm disturbance."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "CKD drives the parathyroids into overdrive: falling vitamin D and rising phosphate push PTH ever higher (secondary hyperparathyroidism), and the relentless hormone leaches bone into renal osteodystrophy — the core of CKD-mineral-bone disorder."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "The failing kidney lets the blood thin: it makes too little erythropoietin, so hemoglobin falls into the anemia of CKD, treated by replacing the missing hormone with erythropoiesis-stimulating agents."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Uremia makes the platelets sluggish: retained toxins impair platelet function, so even with a normal count CKD patients bruise and bleed more easily, a defect that dialysis and desmopressin can partly correct."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "The kidney loses its grip on salt and water: as CKD advances it cannot excrete a sodium load, so fluid builds up into edema and hypertension, making dietary salt restriction a cornerstone of slowing the disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies cause and define much CKD: anti-GBM, ANCA, and lupus autoantibodies attack the glomerulus, and their blood assays pinpoint the immune glomerulonephritides that, untreated, scar the kidney into failure."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Uremia dampens reproduction: it disrupts the hypothalamic-pituitary-gonadal axis into low libido, erectile dysfunction, and infertility, and pregnancy in advanced CKD carries high risk to mother and fetus."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "The failing kidney misreads its own pressure: falling perfusion drives renin and the RAAS into overdrive, raising blood pressure that further scars the kidney — a vicious loop that RAAS blockers are given to interrupt."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages turn injury into scar: they infiltrate the damaged kidney and pour out fibrogenic signals that activate fibroblasts, driving the tubulointerstitial fibrosis that paces the march to kidney failure."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Kidney and urate trap each other: failing kidneys clear less uric acid, raising it into gout, while urate crystals and the drugs for gout can in turn injure the kidney — a two-way burden in CKD."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Fibrosis is the final common path: whatever the initial insult, TGF-β drives tubular cells and fibroblasts to scar the kidney with collagen, the progressive interstitial fibrosis that determines how fast CKD advances."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Failing kidneys imperil the brain's vessels: uremic vasculopathy, hypertension and accelerated atherosclerosis make stroke far more common in CKD, while the bleeding tendency of uremia raises hemorrhagic risk too."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Long-standing damage turns malignant: years of CKD and the acquired cystic disease of dialysis sharply raise the risk of renal cell carcinoma arising in the scarred kidneys."
---

# Chronic Kidney Disease

## Overview

**Chronic kidney disease (CKD)** is defined by the KDIGO 2012 guidelines as persistent abnormalities of kidney structure or function (eGFR <60 mL/min/1.73 m² or markers of kidney damage) present for **>3 months** [^kdigo-2012-ckd]. It represents a global public health crisis — affecting approximately **14% of the US adult population** (37 million individuals) and **697 million** people globally — and is the leading cause of **end-stage kidney disease (ESKD)** requiring renal replacement therapy (dialysis or transplantation).

The two dominant causes are **diabetic nephropathy** (~44% of new ESKD cases) and **hypertensive nephrosclerosis** (~27%), together responsible for nearly three-quarters of ESKD. Additional causes include glomerulonephritis (IgA nephropathy, FSGS, membranous nephropathy), polycystic kidney disease, chronic tubulointerstitial disease (analgesic nephropathy, reflux nephropathy), and obstructive uropathy.

CKD is fundamentally a disease of **progressive nephron loss**: regardless of etiology, the final common pathway is tubular atrophy, glomerulosclerosis, and interstitial fibrosis driven by TGF-β, renin-angiotensin-aldosterone system (RAAS) activation, and complement-mediated injury. As the GFR declines, the remaining nephrons undergo adaptive hyperfiltration — increasing single-nephron GFR — which sustains overall clearance temporarily but accelerates glomerular injury.

## Structure

### Staging by GFR and albuminuria (KDIGO G-A classification)

CKD is classified by GFR category (G1-G5) and albuminuria category (A1-A3) [^levey-2012-ckd-lancet]:

**GFR stages:**
| Stage | eGFR (mL/min/1.73 m²) | Description |
|:---|:---|:---|
| G1 | ≥90 | Normal or high (with kidney damage marker) |
| G2 | 60–89 | Mildly decreased |
| G3a | 45–59 | Mildly-moderately decreased |
| G3b | 30–44 | Moderately-severely decreased |
| G4 | 15–29 | Severely decreased |
| G5 | <15 | Kidney failure (ESKD if treated) |

**Albuminuria categories:**
- A1: <30 mg/g creatinine (normal to mildly increased)
- A2: 30–300 mg/g (moderately increased; formerly "microalbuminuria")
- A3: >300 mg/g (severely increased; formerly "macroalbuminuria")

The combination of GFR stage + albuminuria category determines risk of progression and complications; G3b-G5 + A3 ("orange/red zone") carries the highest risk.

**eGFR estimation:** The 2021 **CKD-EPI creatinine equation** (race-free version) is the current standard for estimating GFR from serum creatinine and cystatin C in adults. Measured GFR (iohexol, inulin clearance) is reserved for borderline cases.

### Histopathology of CKD progression

The final common structural endpoint across CKD etiologies:
- **Glomerulosclerosis:** Global or segmental obliteration of glomerular capillary tufts; collagen deposition replacing mesangium; podocyte loss
- **Tubular atrophy:** Shrinkage and loss of tubular cells, with basement membrane thickening; marker of irreversible nephron loss
- **Interstitial fibrosis:** Progressive collagen deposition (types I, III, IV) in tubulointerstitium driven by TGF-β → fibroblast-to-myofibroblast transition; the extent of interstitial fibrosis correlates most strongly with GFR decline rate
- **Arterial/arteriolar thickening:** Medial hypertrophy, intimal fibrosis, hyalinosis (especially with hypertension and diabetes)

## Function

### Consequences of declining GFR

As nephron mass decreases, impaired renal functions accumulate:

**Solute accumulation (uremia):** Retained uremic solutes (urea, creatinine, β₂-microglobulin, indoxyl sulfate, p-cresyl sulfate) cause the **uremic syndrome**: nausea, pericarditis, asterixis, encephalopathy, platelet dysfunction (uremic bleeding).

**Fluid and electrolyte imbalance:** Reduced urine concentrating ability → isosthenuria; Na⁺ retention → hypertension, edema; K⁺ retention → hyperkalemia (risk of arrhythmia); impaired acid excretion → metabolic acidosis (↓HCO₃⁻, normal/high anion gap).

**Anemia of CKD:** EPO deficiency from loss of peritubular interstitial cells → normocytic normochromic anemia; target Hgb 10–11.5 g/dL with EPO-stimulating agents (ESA); iron deficiency often co-exists.

**CKD-mineral bone disease (CKD-MBD):**
- ↓GFR → ↑phosphate retention → ↓ionized Ca²⁺ → ↑PTH (secondary hyperparathyroidism)
- ↓1α-hydroxylase (renal) → ↓calcitriol (1,25-OH₂D₃) → ↓intestinal Ca absorption → worsened hypocalcemia → further ↑PTH
- Consequence: osteitis fibrosa cystica, adynamic bone disease, vascular calcification (from CaPO₄ deposition)

**Cardiovascular disease:** The leading cause of death in CKD. Mechanisms: hypertension, volume overload, uremic cardiomyopathy (LVH), accelerated atherosclerosis, endothelial dysfunction, and increased oxidative stress. CKD stages G3-G5 carry 10–100× higher CV mortality than the general population.

### Treatment and progression slowing [^coresh-2007-prevalence]

**RAAS blockade (ACEi/ARB):** First-line for proteinuric CKD — reduce intraglomerular pressure, decrease proteinuria, attenuate TGF-β-driven fibrosis; proven to slow progression in diabetic and non-diabetic CKD. Avoid combination ACEi + ARB (↑AKI/hyperkalemia risk without added benefit).

**SGLT2 inhibitors:** Second-line (now often first-line in diabetic CKD); empagliflozin, dapagliflozin reduce proteinuria and slow GFR decline by ~40% through tubuloglomerular feedback restoration, reduced hyperfiltration, and anti-inflammatory effects independent of glycemic control.

**Blood pressure control:** Target <130/80 mmHg in CKD; reduces progression rate and CV mortality.

**Renal replacement therapy (ESKD):** 
- Hemodialysis: 3× weekly × 4h sessions; removes small solutes but not middle molecules well
- Peritoneal dialysis: CAPD or APD; continuous; removes middle molecules better; preserves residual renal function longer
- Renal transplantation: Preferred; 1-year graft survival >95%; 10-year patient survival superior to dialysis; requires immunosuppression (tacrolimus + mycophenolate + steroids)

## Connections

- `targets` → **[Kidney](../../06-organ/kidney/README.md)** — CKD destroys renal parenchyma through glomerulosclerosis, tubular atrophy, and interstitial fibrosis; the kidney is the primary target organ.
- `part-of` → **[Renal System](../renal-system/README.md)** — CKD is the defining chronic pathological state of the renal system, progressively impairing all kidney functions.
- `modulates` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — CKD reduces EPO synthesis from peritubular fibroblasts; anemia of CKD requires ESA therapy to maintain hemoglobin targets.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — CKD and hypertension are bidirectionally causal; each accelerates the other. BP control to <130/80 mmHg is the cornerstone of CKD management.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — CREDENCE (canagliflozin): 30% reduction in kidney endpoint in T2D + CKD; DAPA-CKD (dapagliflozin): 39% reduction in eGFR decline/dialysis/renal death in CKD with and without T2D; SGLT2 inhibitors slow CKD progression via tubuloglomerular feedback and anti-fibrotic effects.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — FGF23 rises 100-1000× in CKD → suppresses 1α-hydroxylase → reduced calcitriol → secondary hyperparathyroidism and CKD-MBD; very high FGF23 predicts LVH, heart failure, and mortality in dialysis patients independent of traditional risk factors.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — OPN is upregulated in injured renal tubular epithelium → integrin αvβ3 on macrophages → macrophage recruitment and pro-inflammatory activation → tubulointerstitial fibrosis; urinary OPN predicts CKD progression; OPN inhibits calcium oxalate crystal adhesion (stone inhibitor).
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — IgA nephropathy is a leading cause of CKD in young adults; mesangial IgA deposition → complement + CCL2 → tubulointerstitial fibrosis → eGFR decline; 20-40% of IgAN reach ESRD within 20 years; sparsentan (ETA/AT1R dual blocker) and iptacopan are disease-modifying therapies.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Hepcidin is elevated in CKD from reduced renal clearance and chronic inflammation; elevated hepcidin → functional iron deficiency → ESA hyporesponsiveness in CKD anemia; HIF-PHIs (roxadustat, daprodustat) suppress hepcidin via EPO→ERFE→BMP-SMAD inhibition.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — CKD anemia is the overlap of EPO deficiency and ACD mechanisms: reduced EPO from peritubular cell loss + hepcidin elevation from CKD inflammation/reduced clearance → combined functional iron deficiency + erythropoietic failure; IV iron + ESA are first-line for CKD anemia.
- `connects-to` → **[Atypical HUS](../ahus/README.md)** — aHUS from complement dysregulation (CFH/CFI mutations) causes progressive CKD; ~50% of untreated aHUS patients reach ESRD within 1 year; eculizumab/ravulizumab reverse TMA and may improve eGFR; renal transplant requires lifelong C5 inhibition in high-risk CFH mutations.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — SCD causes sickle cell nephropathy via medullary sickling (high osmolarity + low pO2 in vasa recta → medullary ischaemia) → hyposthenuria, papillary necrosis, proteinuria; progressive CKD in ~30% HbSS by age 40; ACE inhibitors + hydroxyurea slow progression.
- `connects-to` → **[Malaria](../malaria/README.md)** — Severe falciparum malaria causes AKI in 4-8% (haemoglobinuria + microvascular obstruction + cytokine storm); cerebral malaria + AKI → high mortality; repeated malaria episodes contribute to CKD burden in endemic populations.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — dialysis patients have elevated sclerostin from impaired renal clearance + uremic Wnt suppression → adynamic bone disease; elevated sclerostin correlates with vascular calcification and mortality in CKD; romosozumab is not approved in severe CKD due to CV risk.
- `connects-to` → **[Prurigo Nodularis](../prurigo-nodularis/README.md)** — CKD-associated pruritus (formerly uremic pruritus) causes PN-like nodules in dialysis patients; uremic toxins activate μ-opioid and κ-opioid receptors on pruriceptors; difelikefalin (κ-opioid agonist; FDA 2021 for CKD-aP on HD) reduces itch and may prevent PN nodule formation.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes is the leading cause of chronic kidney disease: chronic hyperglycemia damages the glomerular filter (diabetic nephropathy), causing proteinuria and progressive function loss, so diabetic kidney disease drives most dialysis need—SGLT2 inhibitors now slow it.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — CKD and atherosclerosis form a vicious cardiorenal cycle: declining kidney function accelerates vascular calcification and atherosclerosis, so cardiovascular disease—not kidney failure—is the leading cause of death in CKD.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — CKD deranges calcium and bone metabolism (CKD-MBD): failing kidneys can't activate vitamin D or excrete phosphate, lowering calcium and driving secondary hyperparathyroidism and vascular calcification—so calcium, phosphate and PTH are tightly managed in CKD.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — Podocyte loss is a key driver of progressive CKD: these non-dividing cells form the glomerular filter, and when injury (by diabetes, hypertension or FSGS) kills them, the barrier leaks protein and scars, so podocyte depletion predicts irreversible decline.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — CKD often begins in the glomerulus: damage to the filtering tuft causes proteinuria and falling filtration, and surviving glomeruli hyperfilter to compensate—a maladaptive overwork that scars them too, driving the relentless nephron loss of chronic kidney disease.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — CKD and cardiovascular disease are lethally intertwined: most people with CKD die of heart disease, not kidney failure, because uremia, fluid overload and hypertension accelerate atherosclerosis—so the failing kidney is a powerful cardiac risk factor.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Failing kidneys can't dump potassium: as filtration drops, potassium builds up, and hyperkalemia—worsened by the ACE inhibitors and ARBs used to protect the kidney—can stop the heart, so it is among CKD's most urgent, monitored complications.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Heart and kidney failure drive each other (cardiorenal syndrome): CKD's fluid overload, hypertension, and anemia strain the heart, while a failing heart underperfuses the kidney—so the two organs decline together and share treatments like SGLT2 inhibitors.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — CKD cripples vitamin D activation: damaged kidneys can't perform the final hydroxylation to active calcitriol, so calcium absorption falls and parathyroid hormone rises—driving the renal bone disease that defines CKD's mineral and bone disorder.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — CKD progresses through fibrosis: whatever the initial insult, tubulointerstitial fibrosis is the final common pathway that scars nephrons beyond repair, so the degree of fibrosis on biopsy predicts decline better than the original diagnosis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — CKD throws phosphorus out of balance: failing kidneys can't excrete phosphate, so it rises and—with FGF23, PTH and low vitamin D—drives the bone disease and vascular calcification of CKD-mineral bone disorder.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Angiotensin II accelerates CKD and is the key drug target: it raises glomerular pressure and drives scarring, so ACE inhibitors and ARBs that block it slow progression and reduce proteinuria—the cornerstone of renoprotection.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — CKD and the heart fail together in cardiorenal syndrome: fluid overload, hypertension, anemia and mineral disturbance strain the heart, while heart failure starves the kidneys of flow, so most CKD patients die of cardiovascular causes.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Aldosterone drives the scarring that worsens CKD: beyond raising blood pressure, it promotes fibrosis and inflammation in the kidney, which is why mineralocorticoid blockers like finerenone slow progression on top of ACE inhibitors.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — CKD unleashes bone-dissolving osteoclasts: phosphate retention and secondary hyperparathyroidism overstimulate osteoclasts, the high-turnover renal osteodystrophy that weakens bone and spills calcium and phosphate into vessels.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — CKD turns the blood acidic: failing kidneys cannot excrete the body's daily acid load or regenerate bicarbonate, so hydrogen ions build up into a metabolic acidosis that wastes muscle and bone and is treated with bicarbonate.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — CKD poisons the brain: retained uremic toxins cause the confusion, fatigue, and—in advanced failure—the asterixis and seizures of uremic encephalopathy, symptoms that dialysis is meant to clear.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — CKD wrecks the endothelium: uremic toxins and mineral imbalance injure the vessel-lining cells and calcify artery walls, driving the accelerated atherosclerosis that makes heart disease, not kidney failure, the usual cause of death.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging stages CKD's structure: ultrasound and CT photons show shrunken, scarred kidneys or obstruction, while nuclear scans measure the failing filtration that blood tests only estimate.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — CKD itches relentlessly: retained toxins and mineral imbalance cause uremic pruritus, which patients scratch into prurigo nodularis, one of the most distressing symptoms of advanced kidney failure.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — CKD progresses through fibroblasts: injured kidneys activate myofibroblasts that lay down interstitial scar, the common final pathway by which any kidney disease marches toward failure.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the failing filter: as CKD advances, the glomerular basement membrane thickens and wrinkles while podocyte foot processes flatten and fuse, the ultrastructural decay that lets protein leak and filtration fall.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Failing kidneys leave the blood thin: the diseased kidney makes too little erythropoietin to tell the marrow to build red cells, so anemia is a near-universal companion of CKD, treated with EPO and iron.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — CKD upends magnesium balance: as the kidney loses its power to excrete the mineral, magnesium can build to dangerous levels — especially with magnesium-containing laxatives or antacids — risking weakness and heart-rhythm disturbance.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — CKD drives the parathyroids into overdrive: falling vitamin D and rising phosphate push PTH ever higher (secondary hyperparathyroidism), and the relentless hormone leaches bone into renal osteodystrophy — the core of CKD-mineral-bone disorder.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — The failing kidney lets the blood thin: it makes too little erythropoietin, so hemoglobin falls into the anemia of CKD, treated by replacing the missing hormone with erythropoiesis-stimulating agents.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Uremia makes the platelets sluggish: retained toxins impair platelet function, so even with a normal count CKD patients bruise and bleed more easily, a defect that dialysis and desmopressin can partly correct.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — The kidney loses its grip on salt and water: as CKD advances it cannot excrete a sodium load, so fluid builds up into edema and hypertension, making dietary salt restriction a cornerstone of slowing the disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies cause and define much CKD: anti-GBM, ANCA, and lupus autoantibodies attack the glomerulus, and their blood assays pinpoint the immune glomerulonephritides that, untreated, scar the kidney into failure.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Uremia dampens reproduction: it disrupts the hypothalamic-pituitary-gonadal axis into low libido, erectile dysfunction, and infertility, and pregnancy in advanced CKD carries high risk to mother and fetus.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — The failing kidney misreads its own pressure: falling perfusion drives renin and the RAAS into overdrive, raising blood pressure that further scars the kidney — a vicious loop that RAAS blockers are given to interrupt.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages turn injury into scar: they infiltrate the damaged kidney and pour out fibrogenic signals that activate fibroblasts, driving the tubulointerstitial fibrosis that paces the march to kidney failure.
- `connects-to` → **[Gout](../gout/README.md)** — Kidney and urate trap each other: failing kidneys clear less uric acid, raising it into gout, while urate crystals and the drugs for gout can in turn injure the kidney — a two-way burden in CKD.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Fibrosis is the final common path: whatever the initial insult, TGF-β drives tubular cells and fibroblasts to scar the kidney with collagen, the progressive interstitial fibrosis that determines how fast CKD advances.
- `connects-to` → **[Stroke](../stroke/README.md)** — Failing kidneys imperil the brain's vessels: uremic vasculopathy, hypertension and accelerated atherosclerosis make stroke far more common in CKD, while the bleeding tendency of uremia raises hemorrhagic risk too.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Long-standing damage turns malignant: years of CKD and the acquired cystic disease of dialysis sharply raise the risk of renal cell carcinoma arising in the scarred kidneys.

## Pathology

**Acute-on-chronic kidney disease (AoCKD):** Superimposed AKI in CKD — from contrast, NSAIDs, ACEi in dehydration, infection, obstruction — accelerates irreversible nephron loss; prevention requires careful drug management and hydration.

**Hyperkalemia:** Life-threatening in advanced CKD (G4-G5); exacerbated by ACEi/ARB, aldosterone antagonists, acidosis; managed with dietary K⁺ restriction, patiromer/sodium zirconium cyclosilicate (K⁺ binders), correction of acidosis, and ultimately dialysis.

**Uremic encephalopathy:** End-stage uremia → asterixis, myoclonus, seizures, coma; an emergency indication for dialysis initiation.

**Nephrotic-range proteinuria:** >3.5 g/day (or >3500 mg/g Cr) → albumin loss → hypoalbuminemia → edema, thrombosis risk, hyperlipidemia; occurs with primary glomerulopathies (minimal change, membranous, FSGS).

**CKD and drug dosing:** Reduced GFR requires dose adjustment for renally cleared drugs (antibiotics, anticoagulants, digoxin, metformin [contraindicated <30 mL/min], SGLT2i [less efficacy <20-30 mL/min]).

[^kdigo-2012-ckd]: KDIGO CKD Work Group. KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. *Kidney Int Suppl.* 2013;3(1):1-150. [doi:10.1038/kisup.2012.73](https://doi.org/10.1038/kisup.2012.73)
[^levey-2012-ckd-lancet]: Levey AS, Coresh J. Chronic kidney disease. *Lancet.* 2012;379(9811):165-180. [doi:10.1016/S0140-6736(11)60178-5](https://doi.org/10.1016/S0140-6736(11)60178-5) · [PubMed 21840587](https://pubmed.ncbi.nlm.nih.gov/21840587/)
[^coresh-2007-prevalence]: Coresh J, Selvin E, Stevens LA, et al. Prevalence of chronic kidney disease in the United States. *JAMA.* 2007;298(17):2038-2047. [doi:10.1001/jama.298.17.2038](https://doi.org/10.1001/jama.298.17.2038) · [PubMed 17986697](https://pubmed.ncbi.nlm.nih.gov/17986697/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
