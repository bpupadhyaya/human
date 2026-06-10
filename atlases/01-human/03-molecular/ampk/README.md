---
schema: human-scale-entry/v1
id: ampk
name: AMPK
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Heterotrimeric serine/threonine kinase (α/β/γ) activated by ↑AMP:ATP via LKB1-mediated Thr172 phosphorylation. Master cellular energy sensor: switches off anabolism, switches on catabolism. Metformin activates hepatic AMPK to lower glucose."
aliases: ["AMP-activated protein kinase", "5-AMP-activated protein kinase", "energy sensor kinase", "PRKA"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/03-molecular/insulin
    relation: modulates
    note: "AMPK and insulin converge on glucose and lipid metabolism; AMPK drives GLUT4 translocation in muscle independently of Akt; suppresses mTORC1 via TSC2/Raptor; metformin-activated AMPK sensitises hepatocytes to insulin action."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Hepatic AMPK is metformin's primary target: ↓ACC → ↓malonyl-CoA → ↑FA oxidation; ↓HMGR → ↓cholesterol; ↓SREBP-1c → ↓lipogenesis; CRTC2 phosphorylation → ↓PEPCK/G6Pase → ↓gluconeogenesis; key glucose-lowering mechanism."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: modulated-by
    note: "Metformin inhibits mitochondrial Complex I → ↑AMP:ATP → allosteric AMPK activation → ↓hepatic gluconeogenesis, ↑FA oxidation, ↑GLUT4 in muscle; also AMPK-independent effects: direct PEPCK suppression, lysosomal mTORC1 inhibition."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Cardiac AMPK (α2) is activated by ischaemia (↑AMP:ATP) → ↑GLUT1/4 uptake and ↑FA oxidation → cardiomyocyte survival; PRKAG2 gain-of-function γ2 mutations → glycogen storage cardiomyopathy with Wolff-Parkinson-White syndrome."
  - target: 01-human/03-molecular/mtor
    relation: modulates
    note: "AMPK phosphorylates TSC2 (Ser1387) → activates TSC1/2 GAP → inhibits Rheb → suppresses mTORC1; AMPK also phosphorylates Raptor (Ser792) → mTORC1 inhibition; LKB1-AMPK-TSC2-mTOR is a tumour suppressor pathway; metformin/AICAR phenocopy mTOR inhibitors in reducing proliferation."
  - target: 01-human/04-cellular/adipocyte
    relation: modulates
    note: "Adiponectin activates AMPK via AdipoR1/R2 → T172 phosphorylation → ↑FA oxidation in liver and muscle; AMPK in adipocytes inhibits ACC → ↓malonyl-CoA → ↑mitochondrial FA import; adiponectin-AMPK axis mediates insulin sensitisation in obesity-linked metabolic disease."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "AMPK deficiency contributes to hepatic insulin resistance in T2DM; metformin-activated AMPK reduces hepatic glucose output → lowers fasting glucose; exercise-activated muscle AMPK drives GLUT4 translocation independently of insulin — basis for exercise therapy in T2DM."
---

# AMPK

## Overview

AMP-activated protein kinase (AMPK) is the cell's **master energy sensor** — a heterotrimeric serine/threonine kinase that monitors the AMP:ADP:ATP ratio and, when energy is low, orchestrates a comprehensive switch from anabolic (ATP-consuming) to catabolic (ATP-generating) programmes. It is conserved in all eukaryotes (yeast ortholog: Snf1) and expressed in virtually every human cell type, with particularly high activity in liver, muscle, heart, and brain [^stryer-biochemistry].

AMPK was initially characterised as a kinase that inhibited fatty acid synthesis and cholesterol synthesis; it is now understood as a nexus integrating energy status, nutrient sensing, hormonal signals (leptin, adiponectin, insulin), and cellular stress into coordinated metabolic responses [^guyton-hall]. Its clinical importance is underscored by two facts: **metformin** (the world's most prescribed antidiabetic drug) works primarily by activating hepatic AMPK, and **LKB1** (the principal upstream AMPK kinase) is a tumour suppressor mutated in Peutz-Jeghers syndrome and in ~20% of non-small-cell lung cancers.

## Structure

AMPK is an **obligate heterotrimer** of three subunits:

| Subunit | Isoforms | Role |
|:---|:---|:---|
| **α (catalytic)** | α1 (PRKAA1), α2 (PRKAA2) | N-terminal kinase domain; Thr172 in activation loop — must be phosphorylated for full activity; C-terminal auto-inhibitory domain; α2 predominates in heart and skeletal muscle |
| **β (scaffold)** | β1 (PRKAB1), β2 (PRKAB2) | Central scaffold linking α and γ; carbohydrate-binding module (CBM) — senses glycogen (↑glycogen → ↓AMPK activity, targets AMPK to glycogen granules); myristoylation at Gly2 → membrane anchoring |
| **γ (regulatory)** | γ1 (PRKAG1), γ2 (PRKAG2), γ3 (PRKAG3) | Four CBS (cystathionine β-synthase) domains forming two Bateman domains; CBS1 and CBS3 bind AMP/ADP/ATP competitively; CBS2 and CBS4 constitute regulatory sites |

**Twelve mammalian AMPK complexes** (α1/2 × β1/2 × γ1/2/3) have distinct tissue distributions and regulatory properties:
- α2β2γ3 — skeletal muscle, mediates exercise responses
- α2β2γ1 — cardiac muscle
- α1β1γ1 — liver, adipose tissue, macrophages

**Key structural interfaces:**
- α-subunit kinase domain + β-subunit CBM → allosteric drug-binding site (A769662, MK-8722 bind here, stabilising the active conformation)
- γ-subunit CBS1/CBS3 → AMP/ADP binding induces conformational change transmitted to α-subunit

## Function

AMPK acts as a **bidirectional metabolic switch**:

**When activated (low energy, ↑AMP:ATP):**

*Catabolic processes activated (generate ATP):*
- ↑Fatty acid oxidation (↓ACC → ↓malonyl-CoA → CPT1 derepressed → mitochondrial FA import)
- ↑Glucose uptake in muscle (GLUT4 translocation, Akt-independent)
- ↑Mitochondrial biogenesis (↑PGC-1α → ↑TFAM → ↑mtDNA transcription)
- ↑Autophagy (ULK1 phosphorylation → nutrient recovery from organelles)

*Anabolic processes inhibited (save ATP):*
- ↓Fatty acid synthesis (ACC inhibition)
- ↓Cholesterol synthesis (↓HMGR activity)
- ↓Protein synthesis (↓mTORC1 via Raptor Ser792 and TSC2 phosphorylation)
- ↓Glycogen synthesis (↓glycogen synthase)

**When inactivated (high energy, ↑ATP:AMP):**
- All the above programmes reverse — anabolism dominates
- Growth, protein synthesis, lipogenesis, glycogen deposition proceed

## Mechanism

### Activation — Three Synergistic Mechanisms

**1. AMP/ADP allosteric activation (fast, ≤1 min):**
- AMP or ADP (in energetic stress: AMP:ATP may shift from 1:50 to 1:1) binds γ-subunit CBS1/CBS3
- Induces conformational change → exposes Thr172 in α-subunit activation loop for phosphorylation AND simultaneously reduces accessibility of Thr172 to phosphatases (PP2Cα, PP2A)
- 10-fold rise in AMP:ATP → ~100-fold increase in net AMPK activity (allosteric activation × protection from dephosphorylation = multiplicative amplification)

**2. Thr172 phosphorylation by upstream kinases (required for full activation):**
- **LKB1 (STK11):** Major upstream kinase; constitutively active serine/threonine kinase; forms complex with STRAD and MO25 → phosphorylates Thr172 when AMPK is in AMP-bound (protected) conformation; LKB1 is a tumour suppressor (see Pathology); active in liver, muscle, most somatic cells
- **CaMKKβ (calmodulin-dependent protein kinase kinase β):** Activated by cytoplasmic Ca²⁺ (independent of AMP); important in neurons (neuronal AMPK activation by Ca²⁺ signals), T cells, endothelial cells; explains AMPK activation by thrombin, VEGF (Ca²⁺-raising stimuli) without AMP change
- **TAK1 (TGF-β-activated kinase 1):** Can phosphorylate Thr172; active during inflammatory signalling

**3. Inactivation:**
- PP2Cα (protein phosphatase 2C-α) is the primary Thr172 phosphatase; dephosphorylates and inactivates AMPK when AMP:ATP is low (ATP out-competes AMP at γ-subunit CBS sites → conformational change → Thr172 exposed to PP2Cα)
- GSK3 can also phosphorylate α-subunit at inhibitory sites

### Key Substrate Phosphorylations

| Substrate | Site | Consequence |
|:---|:---|:---|
| **ACC1/2** (acetyl-CoA carboxylase) | Ser79 (ACC1), Ser221 (ACC2) | ↓Malonyl-CoA production → ↑CPT1 → ↑FA import into mitochondria → ↑β-oxidation; also ↓malonyl-CoA as substrate for FASN → ↓FA synthesis |
| **HMGR** (HMG-CoA reductase) | Ser872 | ↓Cholesterol synthesis (rate-limiting step of mevalonate pathway) |
| **Raptor** | Ser792 | Disrupts mTORC1 complex assembly → ↓mTORC1 → ↓protein synthesis, ↓cell growth |
| **TSC2** (tuberous sclerosis 2) | Ser1387, Ser1345 | ↑TSC1/2 complex GAP activity → ↑Rheb-GDP → ↓mTOR (orthogonal route to Raptor phosphorylation) |
| **ULK1** (autophagy initiator) | Ser317, Ser555, Ser777 | Activates ULK1 (and simultaneously AMPK prevents mTORC1 from inhibiting ULK1) → ↑autophagosome formation → ↑nutrient recycling |
| **CRTC2** (CREB coactivator) | Ser171 | ↓Nuclear translocation of CRTC2 → ↓CREB-driven transcription of PEPCK/G6Pase → ↓hepatic gluconeogenesis |
| **Glycogen synthase** | Ser7 | ↓Glycogen synthesis (saves UDP-glucose for glycolysis) |
| **PGC-1α** | Ser538, Thr177 | ↑PGC-1α activity → ↑TFAM → ↑mitochondrial biogenesis; also ↑UCP1 in brown adipose |

### Metformin's Mechanism via AMPK

Metformin (dimethylbiguanide) accumulates in hepatocyte mitochondria (attracted by membrane potential to matrix, reaches mM concentrations) → mildly inhibits **Complex I** (NADH-coenzyme Q reductase, NDH-1) of the electron transport chain → ↑NADH:NAD⁺ → ↓ATP production → ↑AMP:ATP ratio → AMPK activation. This is the dominant molecular mechanism for metformin's glucose-lowering effect. AMPK-independent effects also contribute: direct allosteric inhibition of fructose-1,6-bisphosphatase (FBPase), lysosomal AXIN-LKB1-AMPK complex activation (v-ATPase sensing), and PEN2-mediated lysosomal mTORC1 inhibition [^stryer-biochemistry].

## Connections

- `modulates` → **[insulin](../insulin/README.md)** — AMPK and insulin converge on glucose/lipid metabolism; AMPK activates GLUT4 in muscle independently of Akt; suppresses mTORC1 via TSC2/Raptor; metformin-activated AMPK sensitises hepatocytes to insulin
- `modulates` → **[hepatocyte](../../04-cellular/hepatocyte/README.md)** — primary target of metformin; hepatic AMPK → ↓ACC → ↑FA oxidation; ↓HMGR; ↓SREBP-1c; CRTC2 phosphorylation → ↓gluconeogenic gene expression
- `modulated-by` → **[metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — metformin inhibits Complex I → ↑AMP:ATP → AMPK Thr172 phosphorylation → ↓hepatic gluconeogenesis, ↑FA oxidation, ↑muscle GLUT4; also AMPK-independent effects
- `modulates` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — cardiac AMPK (α2) activated by ischaemia → ↑GLUT1/4 → cardiomyocyte survival; PRKAG2 gain-of-function mutations → glycogen cardiomyopathy + Wolff-Parkinson-White
- `modulates` → **[mTOR](../mtor/README.md)** — AMPK phosphorylates TSC2 and Raptor to suppress mTORC1 activity; the LKB1-AMPK-mTOR axis is a tumour suppressor pathway limiting cell growth under energy stress; metformin and AICAR phenocopy mTOR inhibitors via AMPK activation.
- `modulates` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — adiponectin (secreted by adipocytes) activates AMPK via AdipoR1/R2; AMPK in adipocytes inhibits ACC → reduces malonyl-CoA → promotes mitochondrial FA import; the adiponectin-AMPK axis mediates insulin sensitisation in obesity.
- `connects-to` → **[Type 2 Diabetes](../../07-system/type-2-diabetes/README.md)** — AMPK deficiency in liver and muscle contributes to insulin resistance; metformin restores AMPK → reduces hepatic glucose output; exercise-activated AMPK drives muscle GLUT4 translocation independently of insulin, the basis for exercise in T2DM management.

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **Peutz-Jeghers syndrome** | Germline heterozygous *STK11* (LKB1) loss-of-function mutations → ↓AMPK activity in epithelial cells → ↑mTORC1 → ↑cell growth in energy-poor environments | GI hamartomatous polyps (risk of intussusception); mucocutaneous melanin pigmentation (lips, buccal mucosa, digits); 15–20× ↑cancer risk (colorectal, gastric, pancreatic, breast, ovarian, cervical) |
| **LKB1-mutant lung cancer** | Somatic *STK11* mutations in ~20% NSCLC (co-occurs with KRAS mutations in ~10%) → loss of AMPK → ↑mTORC1 → sustained growth despite metabolic stress | Aggressive phenotype; keratinisation; resistance to immune checkpoint inhibitors (↓T cell infiltration); KRAS/LKB1 co-mutation → poorest prognosis subset |
| **PRKAG2 cardiomyopathy** | Gain-of-function mutations in AMPK γ2 subunit (R302Q, N488I, T400N etc.) → constitutive AMPK activity → ↑GLUT4-mediated glucose uptake → glycogen accumulation in cardiomyocytes | Glycogen storage cardiomyopathy: massive glycogen deposits → ventricular hypertrophy, conduction abnormalities; **Wolff-Parkinson-White syndrome** (accessory pathway: glycogen disrupts annulus fibrosus insulation); risk of sudden cardiac death; autosomal dominant |
| **Metabolic syndrome / T2DM** | ↓AMPK activity in liver and muscle (high-fat diet, obesity, sedentary lifestyle) → ↑lipogenesis, ↑gluconeogenesis, ↓FA oxidation, ↓GLUT4 → insulin resistance and hepatic steatosis | Metformin, exercise, weight loss restore AMPK activity; adiponectin (from adipose) activates AMPK via LKB1 and CaMKKβ pathways — adiponectin levels are low in obesity |
| **Heart failure** | ↓AMPK activity (α2 subunit specifically) in failing myocardium (despite ↑AMP:ATP — may reflect AMPK inhibition by downstream feedback or phosphatase overactivation) → ↓glucose uptake, ↓mitochondrial biogenesis → energy deficit accelerates failure | AMPK activators (AICAR, metformin) have shown benefit in preclinical HF models; clinical evidence for metformin in HFpEF is emerging |
| **Cancer metabolism** | AMPK loss (via LKB1 mutation or other mechanisms) → ↓autophagy + ↑mTORC1 → permissive for Warburg metabolism; AMPK gain → tumour suppressor (limits growth in nutrient-poor tumour microenvironment) | AMPK activators (metformin, AICAR, A769662) inhibit growth of AMPK-intact cancer cells in preclinical models; observational data: metformin use → ↓cancer incidence and mortality in T2DM cohorts |

## See Also

- [^stryer-biochemistry] Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
- [^guyton-hall] Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
- Related entries: [insulin](../insulin/README.md), [hepatocyte](../../04-cellular/hepatocyte/README.md), [metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md), [cortisol](../cortisol/README.md), [leptin](../leptin/README.md)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
