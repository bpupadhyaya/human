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
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Leptin resistance in obesity links to T2DM: SOCS3 impairs IRS-1 → convergent blunting of leptin and insulin signalling; hyperleptinemia independently predicts T2DM onset; metformin reduces leptin; bariatric surgery lowers leptin and improves insulin sensitivity."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "T2DM → elevated sclerostin via AGE accumulation in osteocyte lacuno-canalicular network; contributes to impaired bone quality despite normal BMD; diabetic patients have higher fracture risk at any given BMD due to sclerostin-mediated osteoblast suppression."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Obese adipocyte CCL2 → CCR2+ monocyte recruitment → adipose tissue macrophage (ATM) infiltration → M1 polarization → TNF-α + IL-6 → hepatic and skeletal muscle insulin resistance; crown-like structures (ATM clusters around dead adipocytes) predict T2DM independently of BMI."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is the dominant driver of type 2 diabetes: excess, dysfunctional adipose tissue releases free fatty acids and inflammatory cytokines causing insulin resistance, overworking β-cells until they fail—so weight loss can prevent or even remit T2DM."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Type 2 diabetes powerfully accelerates atherosclerosis: hyperglycemia, dyslipidemia and insulin resistance injure the endothelium and inflame plaques, so cardiovascular disease is the leading cause of death in diabetics—driving aggressive risk-factor control."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "The adipocyte sits at the heart of type 2 diabetes: enlarged, stressed fat cells become insulin-resistant and secrete adipokines and free fatty acids that spread resistance to muscle and liver—adipose tissue as an endocrine driver, not just a fat store."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Type 2 diabetes is a bihormonal disease, not just insulin failure: alpha cells oversecrete glucagon while beta cells under-secrete insulin, so unchecked glucagon drives hepatic glucose output—why GLP-1 and amylin-based drugs that suppress glucagon help control it."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Type 2 diabetes ends in pancreatic beta-cell failure: insulin resistance first forces beta cells to overwork, but they progressively exhaust and die, so the pancreas's declining insulin output—not just resistance—drives the need for insulin therapy over time."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Type 2 diabetes roughly doubles stroke risk: chronic hyperglycemia accelerates atherosclerosis and small-vessel disease while high glucose worsens stroke outcome, so glycemic and vascular risk-factor control is central to preventing the cerebrovascular toll of diabetes."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Type 2 diabetes is a leading cause of blindness via retinopathy: chronic hyperglycemia damages retinal microvessels, causing leakage, ischemia, and neovascularization—so annual retinal screening and tight glucose and blood-pressure control protect vision."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Diabetic peripheral neuropathy is among type 2 diabetes' most common complications: hyperglycemia and microvascular injury damage long nerves, causing stocking-glove numbness and pain that underlie foot ulcers and amputations—so foot care is central to management."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Type 2 diabetes and the liver are tightly linked through fatty liver disease: insulin resistance drives hepatic fat accumulation (MASLD/MASH), which worsens glucose control and can progress to cirrhosis—so the diabetic liver is both cause and casualty of the disease."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Type 2 diabetes is the leading cause of diabetic retinopathy: chronic hyperglycemia damages retinal microvessels, causing the leading preventable blindness in working-age adults—so glucose and blood-pressure control plus eye screening protect vision."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Type 2 diabetes drives heart failure independently: hyperglycemia and insulin resistance stiffen and weaken the myocardium (diabetic cardiomyopathy), and SGLT2 inhibitors—first diabetes drugs—now treat heart failure even in non-diabetics."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Type 2 diabetes is fueled by adipose inflammation via TNF-alpha: enlarged fat tissue releases TNF-alpha and other cytokines that impair insulin signaling, linking obesity's chronic low-grade inflammation directly to insulin resistance."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium deficiency feeds type 2 diabetes: low magnesium worsens insulin resistance and is common in poorly controlled diabetes (and worsened by it), so correcting it modestly improves glucose control—a two-way street between the mineral and the disease."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome shapes type 2 diabetes: dysbiosis fuels low-grade inflammation and insulin resistance, and metformin partly works by reshaping gut bacteria—so what lives in the intestine influences blood sugar."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol drives the diabetes of stress and steroids: the hormone raises blood glucose by spurring the liver and blunting insulin, so chronic stress, Cushing's, and steroid therapy can unmask or worsen type 2 diabetes."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Insulin is packaged with zinc: beta cells store the hormone as zinc-coordinated crystals, and the zinc transporter ZnT8 is both a diabetes-risk gene and an autoantibody target, tying trace-metal handling to the disease."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Type 2 diabetes is the leading cause of kidney failure: years of high glucose scar the glomeruli (diabetic nephropathy), so protecting the kidney with SGLT2 inhibitors and blood-pressure control is central to long-term care."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages link fat to insulin resistance in type 2 diabetes: inflamed adipose tissue recruits macrophages whose cytokines blunt insulin signaling, so this immune-metabolic crosstalk helps turn obesity into diabetes."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Type 2 diabetes is at its core a cardiovascular disease: it doubles the risk of heart attack and heart failure, which remain the leading cause of death, so modern care prizes drugs that protect the heart, not just lower glucose."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "High glucose injures the endothelial cells lining blood vessels: this endothelial dysfunction is the shared root of diabetes's micro- and macrovascular complications, from retinopathy and nephropathy to accelerated atherosclerosis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Insulin drives potassium into cells, so diabetes is also a potassium story: emergencies like ketoacidosis hide a whole-body deficit, and giving insulin can crash serum potassium dangerously low unless it is replaced."
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
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — leptin resistance in obesity links to T2DM: SOCS3 impairs IRS-1 → convergent blunting of leptin and insulin signalling; hyperleptinemia independently predicts T2DM onset; metformin reduces leptin; bariatric surgery lowers leptin and improves insulin sensitivity.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — T2DM elevates sclerostin via AGE accumulation in the osteocyte lacuno-canalicular network; sclerostin-mediated osteoblast suppression impairs bone quality despite normal BMD, leading to higher fracture risk at any given BMD; a mechanistic link between hyperglycemia and diabetic bone fragility.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Obese adipocyte CCL2 → CCR2+ monocyte recruitment → adipose tissue macrophage (ATM) infiltration → M1 polarization → TNF-α + IL-6 → hepatic and skeletal muscle insulin resistance; crown-like structures (ATM clusters around dead adipocytes) predict T2DM independently of BMI.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is the dominant driver of type 2 diabetes: excess, dysfunctional adipose tissue releases free fatty acids and inflammatory cytokines causing insulin resistance, overworking β-cells until they fail—so weight loss can prevent or even remit T2DM.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Type 2 diabetes powerfully accelerates atherosclerosis: hyperglycemia, dyslipidemia and insulin resistance injure the endothelium and inflame plaques, so cardiovascular disease is the leading cause of death in diabetics—driving aggressive risk-factor control.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — The adipocyte sits at the heart of type 2 diabetes: enlarged, stressed fat cells become insulin-resistant and secrete adipokines and free fatty acids that spread resistance to muscle and liver—adipose tissue as an endocrine driver, not just a fat store.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Type 2 diabetes is a bihormonal disease, not just insulin failure: alpha cells oversecrete glucagon while beta cells under-secrete insulin, so unchecked glucagon drives hepatic glucose output—why GLP-1 and amylin-based drugs that suppress glucagon help control it.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Type 2 diabetes ends in pancreatic beta-cell failure: insulin resistance first forces beta cells to overwork, but they progressively exhaust and die, so the pancreas's declining insulin output—not just resistance—drives the need for insulin therapy over time.
- `connects-to` → **[Stroke](../stroke/README.md)** — Type 2 diabetes roughly doubles stroke risk: chronic hyperglycemia accelerates atherosclerosis and small-vessel disease while high glucose worsens stroke outcome, so glycemic and vascular risk-factor control is central to preventing the cerebrovascular toll of diabetes.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Type 2 diabetes is a leading cause of blindness via retinopathy: chronic hyperglycemia damages retinal microvessels, causing leakage, ischemia, and neovascularization—so annual retinal screening and tight glucose and blood-pressure control protect vision.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Diabetic peripheral neuropathy is among type 2 diabetes' most common complications: hyperglycemia and microvascular injury damage long nerves, causing stocking-glove numbness and pain that underlie foot ulcers and amputations—so foot care is central to management.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Type 2 diabetes and the liver are tightly linked through fatty liver disease: insulin resistance drives hepatic fat accumulation (MASLD/MASH), which worsens glucose control and can progress to cirrhosis—so the diabetic liver is both cause and casualty of the disease.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Type 2 diabetes is the leading cause of diabetic retinopathy: chronic hyperglycemia damages retinal microvessels, causing the leading preventable blindness in working-age adults—so glucose and blood-pressure control plus eye screening protect vision.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Type 2 diabetes drives heart failure independently: hyperglycemia and insulin resistance stiffen and weaken the myocardium (diabetic cardiomyopathy), and SGLT2 inhibitors—first diabetes drugs—now treat heart failure even in non-diabetics.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Type 2 diabetes is fueled by adipose inflammation via TNF-alpha: enlarged fat tissue releases TNF-alpha and other cytokines that impair insulin signaling, linking obesity's chronic low-grade inflammation directly to insulin resistance.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium deficiency feeds type 2 diabetes: low magnesium worsens insulin resistance and is common in poorly controlled diabetes (and worsened by it), so correcting it modestly improves glucose control—a two-way street between the mineral and the disease.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome shapes type 2 diabetes: dysbiosis fuels low-grade inflammation and insulin resistance, and metformin partly works by reshaping gut bacteria—so what lives in the intestine influences blood sugar.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol drives the diabetes of stress and steroids: the hormone raises blood glucose by spurring the liver and blunting insulin, so chronic stress, Cushing's, and steroid therapy can unmask or worsen type 2 diabetes.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Insulin is packaged with zinc: beta cells store the hormone as zinc-coordinated crystals, and the zinc transporter ZnT8 is both a diabetes-risk gene and an autoantibody target, tying trace-metal handling to the disease.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Type 2 diabetes is the leading cause of kidney failure: years of high glucose scar the glomeruli (diabetic nephropathy), so protecting the kidney with SGLT2 inhibitors and blood-pressure control is central to long-term care.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages link fat to insulin resistance in type 2 diabetes: inflamed adipose tissue recruits macrophages whose cytokines blunt insulin signaling, so this immune-metabolic crosstalk helps turn obesity into diabetes.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Type 2 diabetes is at its core a cardiovascular disease: it doubles the risk of heart attack and heart failure, which remain the leading cause of death, so modern care prizes drugs that protect the heart, not just lower glucose.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — High glucose injures the endothelial cells lining blood vessels: this endothelial dysfunction is the shared root of diabetes's micro- and macrovascular complications, from retinopathy and nephropathy to accelerated atherosclerosis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Insulin drives potassium into cells, so diabetes is also a potassium story: emergencies like ketoacidosis hide a whole-body deficit, and giving insulin can crash serum potassium dangerously low unless it is replaced.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^defronzo-2009-t2dm]: DeFronzo RA. Banting Lecture. From the triumvirate to the ominous octet: a new paradigm for the treatment of type 2 diabetes mellitus. *Diabetes.* 2009;58(4):773-795. [doi:10.2337/db09-9028](https://doi.org/10.2337/db09-9028) · [PubMed 19336687](https://pubmed.ncbi.nlm.nih.gov/19336687/)
[^zinman-2015-empareg]: Zinman B, Wanner C, Lachin JM, et al. Empagliflozin, Cardiovascular Outcomes, and Mortality in Type 2 Diabetes. *N Engl J Med.* 2015;373(22):2117-2128. [doi:10.1056/NEJMoa1504720](https://doi.org/10.1056/NEJMoa1504720) · [PubMed 26378978](https://pubmed.ncbi.nlm.nih.gov/26378978/)
[^marwick-2018-t2dm-cv]: Marwick TH, Ritchie R, Shaw JE, Kaye D. Implications of Underlying Mechanisms for the Recognition and Management of Diabetic Cardiomyopathy. *J Am Coll Cardiol.* 2018;71(3):339-351. [doi:10.1016/j.jacc.2017.11.019](https://doi.org/10.1016/j.jacc.2017.11.019) · [PubMed 29348028](https://pubmed.ncbi.nlm.nih.gov/29348028/)
