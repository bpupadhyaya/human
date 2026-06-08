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

## Pathology

**Acute-on-chronic kidney disease (AoCKD):** Superimposed AKI in CKD — from contrast, NSAIDs, ACEi in dehydration, infection, obstruction — accelerates irreversible nephron loss; prevention requires careful drug management and hydration.

**Hyperkalemia:** Life-threatening in advanced CKD (G4-G5); exacerbated by ACEi/ARB, aldosterone antagonists, acidosis; managed with dietary K⁺ restriction, patiromer/sodium zirconium cyclosilicate (K⁺ binders), correction of acidosis, and ultimately dialysis.

**Uremic encephalopathy:** End-stage uremia → asterixis, myoclonus, seizures, coma; an emergency indication for dialysis initiation.

**Nephrotic-range proteinuria:** >3.5 g/day (or >3500 mg/g Cr) → albumin loss → hypoalbuminemia → edema, thrombosis risk, hyperlipidemia; occurs with primary glomerulopathies (minimal change, membranous, FSGS).

**CKD and drug dosing:** Reduced GFR requires dose adjustment for renally cleared drugs (antibiotics, anticoagulants, digoxin, metformin [contraindicated <30 mL/min], SGLT2i [less efficacy <20-30 mL/min]).

[^kdigo-2012-ckd]: KDIGO CKD Work Group. KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. *Kidney Int Suppl.* 2013;3(1):1-150. [doi:10.1038/kisup.2012.73](https://doi.org/10.1038/kisup.2012.73)
[^levey-2012-ckd-lancet]: Levey AS, Coresh J. Chronic kidney disease. *Lancet.* 2012;379(9811):165-180. [doi:10.1016/S0140-6736(11)60178-5](https://doi.org/10.1016/S0140-6736(11)60178-5) · [PubMed 21840587](https://pubmed.ncbi.nlm.nih.gov/21840587/)
[^coresh-2007-prevalence]: Coresh J, Selvin E, Stevens LA, et al. Prevalence of chronic kidney disease in the United States. *JAMA.* 2007;298(17):2038-2047. [doi:10.1001/jama.298.17.2038](https://doi.org/10.1001/jama.298.17.2038) · [PubMed 17986697](https://pubmed.ncbi.nlm.nih.gov/17986697/)
