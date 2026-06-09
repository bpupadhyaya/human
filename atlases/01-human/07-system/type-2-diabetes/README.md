---
schema: human-scale-entry/v1
id: type-2-diabetes
name: Type 2 Diabetes
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic metabolic disease from progressive insulin resistance and β-cell failure. Driven by obesity and inactivity. First-line: metformin (AMPK activation); GLP-1 agonists and SGLT2 inhibitors provide cardiovascular and renal benefit beyond glycemic control."
aliases: ["T2DM", "type 2 diabetes mellitus", "non-insulin-dependent diabetes", "NIDDM", "adult-onset diabetes"]
sources:
  - id: defronzo-2009-t2dm
    type: peer-reviewed
    cite: "DeFronzo RA. Banting Lecture. From the triumvirate to the ominous octet: a new paradigm for the treatment of type 2 diabetes mellitus. Diabetes. 2009;58(4):773-795."
    doi: "10.2337/db09-9028"
    pmid: "19336687"
    url: "https://doi.org/10.2337/db09-9028"
  - id: zinman-2015-empareg
    type: peer-reviewed
    cite: "Zinman B, Wanner C, Lachin JM, et al. Empagliflozin, Cardiovascular Outcomes, and Mortality in Type 2 Diabetes. N Engl J Med. 2015;373(22):2117-2128."
    doi: "10.1056/NEJMoa1504720"
    pmid: "26378978"
    url: "https://doi.org/10.1056/NEJMoa1504720"
  - id: marwick-2018-t2dm-cv
    type: peer-reviewed
    cite: "Marwick TH, Ritchie R, Shaw JE, Kaye D. Implications of Underlying Mechanisms for the Recognition and Management of Diabetic Cardiomyopathy. J Am Coll Cardiol. 2018;71(3):339-351."
    doi: "10.1016/j.jacc.2017.11.019"
    pmid: "29348028"
    url: "https://doi.org/10.1016/j.jacc.2017.11.019"
cross_links:
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "T2DM is a disease of insulin signaling failure: IRS-1 Ser307 phosphorylation (by JNK/IKKβ) uncouples PI3K → impaired glucose uptake; progressive β-cell glucotoxicity reduces insulin secretion; therapies must address both peripheral resistance and secretory failure."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Metformin (first-line T2DM therapy) activates AMPK via complex I inhibition → AMPK phosphorylates ACC and activates GLUT4 trafficking; AMPK also inhibits mTORC1 → reduced hepatic glucose output; loss of AMPK activity in obesity and insulin resistance contributes to hyperglycemia."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Diabetes is the leading cause of CKD globally (~40% of CKD); hyperglycemia drives mesangial expansion, podocyte injury, and GBM thickening → diabetic nephropathy; SGLT2 inhibitors provide renoprotection independent of glycemic control (CREDENCE, DAPA-CKD trials)."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "T2DM and hypertension co-occur in >70% of patients via shared insulin resistance and RAAS activation; combined hyperglycemia and hypertension accelerate CVD, retinopathy, and nephropathy; preferred antihypertensives in T2DM are ACEi or ARB (renoprotective)."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "GLP-1R agonists (semaglutide, liraglutide, dulaglutide) reduce HbA1c 1-1.5% and weight 5-15%; glucose-dependent insulin secretion avoids hypoglycemia; SUSTAIN-6 (semaglutide) and LEADER (liraglutide) showed CV risk reduction in T2D with established cardiovascular disease."
  - target: 01-human/03-molecular/sglt2
    relation: connects-to
    note: "EMPA-REG OUTCOME (empagliflozin, T2D + CVD): 14% MACE reduction, 35% CV death reduction, 35% HHF reduction; SGLT2 inhibitors reduce HbA1c ~0.7-1.0% with glucose-dependent mechanism avoiding hypoglycemia; first-line therapy in T2D with established ASCVD or heart failure."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Hyperglycemia → excess AGE formation → RAGE on endothelium and macrophages → NF-κB → VCAM-1, ICAM-1, MCP-1 → diabetic micro- and macroangiopathy; soluble RAGE (sRAGE, a decoy) is inversely associated with T2D complications; RAGE also mediates AGE-driven β-cell dysfunction."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Ghrelin opposes insulin: GHSR1a in pancreatic β cells → reduced insulin secretion; obese T2DM patients have blunted ghrelin suppression after meals; GLP-1 receptor agonists suppress ghrelin surges — contributing to satiety; anamorelin (GHSR1a agonist) treats cancer cachexia."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "GH is counter-regulatory: raises plasma glucose via hepatic output and peripheral insulin resistance (GHR/STAT5 → IRS-1 serine phosphorylation); acromegaly causes T2DM in 25-40%; declining GH/IGF-1 with aging contributes to metabolic inflexibility and abdominal adiposity."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "MTNR1B rs10830963 impairs beta-cell MT2 inhibition of insulin → elevated fasting glucose → T2DM risk; melatonin suppresses nocturnal insulin secretion; high-dose melatonin reduces insulin sensitivity in susceptible individuals; MT2 agonists under investigation for T2DM."
---

# Type 2 Diabetes

## Overview

**Type 2 diabetes mellitus (T2DM)** is a chronic metabolic disease characterized by **hyperglycemia resulting from progressive insulin resistance in peripheral tissues (skeletal muscle, adipose, liver) combined with relative insulin secretory failure** from pancreatic β-cells — the so-called "ominous octet" of pathological defects described by DeFronzo [^defronzo-2009-t2dm]. Unlike type 1 diabetes (autoimmune β-cell destruction → absolute insulin deficiency), T2DM involves a gradual decline from compensated insulin resistance (elevated insulin, normal glucose) → impaired fasting glucose/glucose intolerance → overt T2DM as β-cell compensation fails.

**Global burden:** 537 million people worldwide with T2DM in 2021 (IDF Diabetes Atlas); projected 643 million by 2030; responsible for ~6.7 million deaths/year; a major driver of cardiovascular disease (3-4× increased risk of MI and stroke), chronic kidney disease (leading cause globally), blindness (diabetic retinopathy), and lower limb amputations.

**Pathophysiology triad:**
1. **Insulin resistance:** Muscle and adipose fail to take up glucose in response to insulin → postprandial hyperglycemia; liver fails to suppress gluconeogenesis → fasting hyperglycemia
2. **β-cell dysfunction:** Progressive: hyperinsulinemia → ER stress → lipotoxicity → glucotoxicity → β-cell apoptosis → insulin secretory capacity falls ~50% by T2DM diagnosis and continues declining
3. **Adipocyte dysfunction:** Visceral adiposity → ectopic fat deposition in liver and muscle → lipotoxicity → insulin resistance; adipokine imbalance (↑ TNF-α, IL-6, resistin; ↓ adiponectin)

**Risk factors:** Obesity (BMI >30), physical inactivity, family history (heritability ~40-70%), age >45, hypertension, dyslipidemia, gestational diabetes, polycystic ovary syndrome, certain medications (glucocorticoids, antipsychotics), sleep apnea.

**Genetic architecture:** Highly polygenic (>400 susceptibility loci identified by GWAS); individual SNPs confer modest risk; major loci: TCF7L2 (Wnt/β-catenin → β-cell development), SLC30A8 (ZnT8, β-cell zinc transporter), PPARG (adipogenesis), KCNJ11 (K_ATP channel → insulin secretion).

## Structure

### The DeFronzo "Ominous Octet" — organ-level contributions [^defronzo-2009-t2dm]

Eight organs/tissues contribute to T2DM pathophysiology:
1. **Skeletal muscle (75% of insulin-stimulated glucose disposal):** Impaired GLUT4 translocation → reduced glucose uptake → postprandial hyperglycemia
2. **Liver:** Failure of insulin to suppress gluconeogenesis → fasting hyperglycemia; elevated hepatic glucose output even with hyperinsulinemia (hepatic insulin resistance)
3. **Pancreatic β-cells:** Progressive secretory failure; initially compensatory hypersecretion → burnout from glucotoxicity and lipotoxicity → reduced first-phase insulin release → hyperglycemia
4. **Pancreatic α-cells:** Hyperglucagonemia (α-cells are relatively insulin-resistant in T2DM) → excess hepatic glucose production; GLP-1 agonists suppress glucagon; GIP+GLP-1 dual agonists target both
5. **Adipocytes:** Increased lipolysis → elevated free fatty acids (FFA) → liver (hepatic steatosis, gluconeogenesis), muscle (insulin resistance via ceramide and diacylglycerol), β-cells (lipotoxicity)
6. **Brain:** Central insulin resistance → altered satiety; GLP-1 receptor agonists act centrally to reduce appetite and weight
7. **Kidney:** Increased tubular glucose reabsorption (SGLT2 upregulation in diabetic kidney → exacerbates hyperglycemia); SGLT2 inhibitors exploit this
8. **Gut:** Reduced GLP-1 secretion from L-cells (impaired incretin effect accounts for 50% of postprandial glucose rise); GLP-1 agonists restore this deficit

### Molecular basis of insulin resistance

**Adipokine-driven inflammation:**
- Visceral fat → TNF-α, IL-6, resistin secretion + reduced adiponectin → systemic low-grade inflammation
- TNF-α → IKKβ → IRS-1 Ser307 phosphorylation → IRS-1 degradation → PI3K uncoupled from insulin receptor → Akt not activated → GLUT4 not translocated

**JNK pathway:**
- Saturated fatty acids (palmitate) → ceramide synthesis → ceramide activates PP2A → dephosphorylates Akt → insulin resistance; also via ER stress → IRE1→JNK → IRS-1 Ser307 phosphorylation

**Mitochondrial dysfunction:**
- Reduced mitochondrial biogenesis (reduced PGC-1α in T2DM muscle) → impaired fatty acid oxidation → intramyocellular lipid accumulation (IMCL) → DAG → PKCθ → IRS-1 Ser phosphorylation → insulin resistance

## Function

### Chronic complications: the ABCDE of T2DM

**Microvascular complications (from hyperglycemia):**
- **Diabetic retinopathy:** Pericyte loss → acellular capillaries → microaneurysms → neovascularization (VEGF-driven) → tractional retinal detachment; leading cause of new blindness in working-age adults
- **Diabetic nephropathy:** GBM thickening, mesangial expansion, podocyte injury → proteinuria → progressive CKD → ESRD; GFR declines ~4-10 mL/min/year in proteinuric T2DM
- **Diabetic neuropathy:** Schwann cell dysfunction, axonal degeneration → painful peripheral neuropathy, autonomic neuropathy (gastroparesis, orthostatic hypotension, neurogenic bladder), Charcot foot

**Macrovascular complications (from insulin resistance + dyslipidemia + hypertension):**
- 2-4× increased cardiovascular mortality; atherosclerosis accelerated by endothelial dysfunction (reduced eNOS), foam cell formation, advanced glycation end-products (AGEs → RAGE → NF-κB → inflammation)
- Diabetic cardiomyopathy: impaired cardiac energetics (shift to fatty acid oxidation → reduced efficiency), myocardial fibrosis, diastolic dysfunction [^marwick-2018-t2dm-cv]

### Diagnostic criteria (ADA 2024)

| Test | Diabetes | Pre-diabetes | Normal |
|:---|:---|:---|:---|
| Fasting plasma glucose | ≥126 mg/dL | 100-125 mg/dL | <100 mg/dL |
| 2-hour OGTT | ≥200 mg/dL | 140-199 mg/dL | <140 mg/dL |
| HbA1c | ≥6.5% | 5.7-6.4% | <5.7% |
| Random glucose | ≥200 + symptoms | — | — |

## Pathology

### Cardiovascular-renal metabolic syndrome: the T2DM complication nexus

T2DM, CKD, heart failure, and obesity form the **cardiorenal metabolic (CRM) syndrome** — each condition worsens the others:
- T2DM → diabetic nephropathy → CKD → hypertension → cardiovascular disease
- Heart failure → reduced renal perfusion → cardiorenal syndrome → worsened glycemic control
- Obesity → visceral adiposity → insulin resistance → T2DM → all complications

### Pharmacological management

**Glycemic targets:**
- HbA1c <7.0% (most patients); <6.5% in young, low hypoglycemia risk; <8.0% in elderly/complex
- ADA 2024: Time-in-range (TIR) ≥70% on CGM for adults

**Drug classes (stepwise intensification):**

**Metformin (1st line):**
- Mechanism: AMPK activation (via Complex I inhibition → ATP→AMP rise → AMPK) → hepatic gluconeogenesis suppression (phosphorylates CREB coactivator TORC2) + sensitizes peripheral tissues; also independent of AMPK via direct phosphoglucose isomerase inhibition
- Benefits: neutral/weight loss, low hypoglycemia risk, CV-neutral (UKPDS long-term data), reduced cancer risk (meta-analyses), $4/month
- Limitation: GI intolerance, contraindicated eGFR <30

**GLP-1 receptor agonists (2nd line, cardioprotective):**
- Liraglutide, semaglutide, dulaglutide — GLP-1 mimetics; bind GLP-1R on β-cells → cAMP → PKA → KATP channel closure → insulin secretion (glucose-dependent, no hypoglycemia); also: suppress glucagon, slow gastric emptying, central satiety (weight loss 3-15%)
- **CV outcomes:** LEADER (liraglutide), SUSTAIN-6 (semaglutide), REWIND (dulaglutide) — significant MACE reduction in high-CV-risk T2DM; primary prevention CV benefit: SELECT trial (semaglutide 2.4 mg in obesity, regardless of T2DM)
- Oral semaglutide: first oral GLP-1 agonist (Rybelsus); PIONEER-6: non-inferior to IV

**SGLT2 inhibitors (2nd/3rd line, cardiorenal protective):**
- Empagliflozin, dapagliflozin, canagliflozin — block SGLT2 in proximal tubule → ~60-80 g glucose/day excreted in urine → HbA1c ↓0.7-1.0%; also: osmotic diuresis → BP reduction, weight loss (~2-3 kg)
- **Cardiovascular:** EMPA-REG OUTCOME (empagliflozin): 38% reduction in CV death, 35% reduction in heart failure hospitalization vs placebo in established CVD [^zinman-2015-empareg]; mechanisms beyond glycemic: reduced preload/afterload, improved cardiac energetics, reduced uric acid
- **Renal:** CREDENCE (canagliflozin), DAPA-CKD (dapagliflozin): ~30-40% reduction in renal composite (eGFR decline, ESRD, renal death) — now approved for CKD independent of T2DM; tubuloglomerular feedback mechanism (SGLT2 inhibition → increased NaCl at macula densa → afferent arteriole constriction → reduced glomerular hyperfiltration → long-term nephroprotection)

**Additional agents:**
- **DPP-4 inhibitors (sitagliptin, saxagliptin):** Block GLP-1/GIP degradation → modestly increase endogenous incretin levels; CV-neutral; well tolerated; lower HbA1c-lowering than GLP-1 agonists
- **TZDs (pioglitazone):** PPARγ agonist → insulin sensitization; reduces CV events in insulin-resistant patients (PROactive); weight gain, heart failure risk limits use
- **Sulfonylureas (glipizide, glyburide):** Stimulate insulin secretion (close K_ATP channels); low cost but hypoglycemia risk, weight gain, lose efficacy as β-cells fail
- **Basal insulin (glargine, detemir, degludec):** When oral/non-insulin injectable agents insufficient; added at bedtime; titrate to fasting glucose <130 mg/dL

## Connections

- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — T2DM is fundamentally a disease of insulin signaling failure; peripheral insulin resistance (IRS-1 Ser307 phosphorylation) prevents glucose uptake; progressive β-cell burnout reduces insulin secretion; both arms must be addressed therapeutically.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — metformin activates AMPK via Complex I inhibition → suppresses hepatic gluconeogenesis and activates GLUT4; AMPK activity is impaired in insulin-resistant states; AMPK is a major target for T2DM drug development.
- `connects-to` → **[CKD](../ckd/README.md)** — diabetes is the leading cause of CKD globally; hyperglycemia drives diabetic nephropathy; SGLT2 inhibitors provide renoprotection beyond glycemic control.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — T2DM and hypertension co-occur in >70% of patients through shared insulin resistance and RAAS activation; combined hyperglycemia and hypertension accelerate CVD, retinopathy, and nephropathy.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GLP-1R agonists (semaglutide, liraglutide, dulaglutide) reduce HbA1c 1-1.5% and weight 5-15%; glucose-dependent insulin secretion avoids hypoglycemia; SUSTAIN-6 (semaglutide) and LEADER (liraglutide) showed CV risk reduction in T2D with established cardiovascular disease.
- `connects-to` → **[SGLT2](../../03-molecular/sglt2/README.md)** — EMPA-REG OUTCOME (empagliflozin, T2D + CVD): 14% MACE reduction, 35% CV death reduction, 35% HHF reduction; SGLT2 inhibitors reduce HbA1c ~0.7-1.0% with glucose-dependent mechanism avoiding hypoglycemia; first-line therapy in T2D with established ASCVD or heart failure.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Hyperglycemia → excess AGE formation → RAGE on endothelium and macrophages → NF-κB → VCAM-1, ICAM-1, MCP-1 → diabetic micro- and macroangiopathy; soluble RAGE (sRAGE, a decoy) is inversely associated with T2D complications; RAGE also mediates AGE-driven β-cell dysfunction.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — GH is counter-regulatory: raises plasma glucose via hepatic output and peripheral insulin resistance (GHR/STAT5 → IRS-1 serine phosphorylation); acromegaly causes T2DM in 25-40% of cases; exogenous GH raises insulin requirements; declining GH/IGF-1 with aging contributes to metabolic inflexibility.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — MTNR1B rs10830963 impairs beta-cell MT2 inhibition of insulin → elevated fasting glucose → T2DM risk; melatonin suppresses nocturnal insulin secretion; high-dose melatonin reduces insulin sensitivity in susceptible individuals; MT2 agonists under investigation for T2DM.

[^defronzo-2009-t2dm]: DeFronzo RA. Banting Lecture. From the triumvirate to the ominous octet: a new paradigm for the treatment of type 2 diabetes mellitus. *Diabetes.* 2009;58(4):773-795. [doi:10.2337/db09-9028](https://doi.org/10.2337/db09-9028) · [PubMed 19336687](https://pubmed.ncbi.nlm.nih.gov/19336687/)
[^zinman-2015-empareg]: Zinman B, Wanner C, Lachin JM, et al. Empagliflozin, Cardiovascular Outcomes, and Mortality in Type 2 Diabetes. *N Engl J Med.* 2015;373(22):2117-2128. [doi:10.1056/NEJMoa1504720](https://doi.org/10.1056/NEJMoa1504720) · [PubMed 26378978](https://pubmed.ncbi.nlm.nih.gov/26378978/)
[^marwick-2018-t2dm-cv]: Marwick TH, Ritchie R, Shaw JE, Kaye D. Implications of Underlying Mechanisms for the Recognition and Management of Diabetic Cardiomyopathy. *J Am Coll Cardiol.* 2018;71(3):339-351. [doi:10.1016/j.jacc.2017.11.019](https://doi.org/10.1016/j.jacc.2017.11.019) · [PubMed 29348028](https://pubmed.ncbi.nlm.nih.gov/29348028/)
