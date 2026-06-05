---
schema: human-scale-entry/v1
id: glucagon
name: Glucagon
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "29-aa pancreatic α-cell peptide that opposes insulin: activates glycogenolysis, gluconeogenesis, β-oxidation, and ketogenesis via GCGR-cAMP-PKA signaling. Hyperglucagonemia drives fasting hyperglycemia in T2DM; target of new tri-agonist drugs."
aliases: ["glucagon", "GCG", "pancreatic glucagon", "proglucagon", "GCGR", "glucagon receptor", "alpha-cell hormone", "hyperglucagonemia"]
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
  - id: drucker-2018-glucagon-physiology
    type: peer-reviewed
    cite: "Sandoval DA, D'Alessio DA. Physiology of proglucagon peptides: role of glucagon and GLP-1 in health and disease. Physiol Rev. 2015;95(2):513-48."
    doi: "10.1152/physrev.00013.2014"
    pmid: "25834231"
    url: "https://doi.org/10.1152/physrev.00013.2014"
    accessed: "2026-06-05"
  - id: unger-1971-glucagon-diabetes
    type: peer-reviewed
    cite: "Unger RH, Orci L. Physiology and pathophysiology of glucagon. Physiol Rev. 1976;56(4):778-826."
    doi: "10.1152/physrev.1976.56.4.778"
    pmid: "790423"
    url: "https://doi.org/10.1152/physrev.1976.56.4.778"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Glucagon activates GCGR (Gs-GPCR) on hepatocytes → cAMP → PKA → glycogen phosphorylase kinase → glycogenolysis; CREB → ↑PEPCK/G6Pase → ↑gluconeogenesis. The liver is the primary target organ, rapidly raising blood glucose during fasting, hypoglycemia, and exercise."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "In hepatocytes, PKA phosphorylates glycogen phosphorylase kinase (activating it) and glycogen synthase (inactivating it), simultaneously driving glycogen breakdown and halting synthesis. Glucagon also ↓malonyl-CoA → ↑CPT-1 activity → ↑β-oxidation → ↑ketogenesis from acetyl-CoA."
  - target: 01-human/03-molecular/insulin
    relation: modulated-by
    note: "Insulin suppresses glucagon secretion via paracrine inhibition (GABA and Zn²⁺ from β-cells → α-cell hyperpolarization) and opposes downstream effects (activating glycogen synthase, inhibiting PEPCK). Insulin:glucagon ratio is the master switch for hepatic glucose output."
  - target: 01-human/07-system/digestive-system
    relation: modulates
    note: "GLP-1 from intestinal L-cells (same proglucagon gene) potently suppresses α-cell glucagon secretion. Ingested amino acids directly stimulate α-cells, driving hepatic gluconeogenesis to prevent protein-induced hypoglycemia."
---

# Glucagon

## Overview

**Glucagon** is a 29-amino acid peptide hormone and the primary counter-regulatory hormone to insulin. Secreted by pancreatic islet **α-cells** (which constitute ~20-25% of islet cells), glucagon is the primary driver of endogenous glucose production during fasting, hypoglycemia, and sustained aerobic exercise.

The insulin-glucagon axis represents the core hormonal switch governing whether the body operates in an **anabolic (fed) state** — directed by insulin toward glucose storage and biosynthesis — or a **catabolic (fasted) state** — directed by glucagon toward glucose mobilization, fat oxidation, and ketogenesis.

**Glucagon in context:**
- During a 12-hour fast, hepatic glucose output (~180 g/day in total; ~1-2 mg/kg/min basal rate) is maintained almost entirely by glucagon-driven glycogenolysis (short-term, hours 0-8) transitioning to glucagon-driven gluconeogenesis (long-term, beyond 24 hours)
- In exercise, glucagon rises in concert with ↓insulin, preventing hypoglycemia during sustained muscle glucose uptake
- Glucagon also acts in liver, kidney (cortex), heart, brain (limited GCGR expression), fat (lipolysis), and enteric nervous system

**Historical significance:** Glucagon was identified by Kimball and Murlin in 1923 (the same year as insulin) as a hyperglycemic substance in pancreatic extracts. Unger and Orci [^unger-1971-glucagon-diabetes] established the bihormonal model of diabetes: T1DM and T2DM involve not just insulin deficiency/resistance but also **hyperglucagonemia** — a pathological failure of glucagon suppression, driving fasting hyperglycemia. This insight sparked glucagon receptor as a therapeutic target.

## Structure

**Gene and precursor:**
- **GCG gene** on chromosome 2q36.3; encodes **proglucagon** (180 amino acids)
- Proglucagon is processed differentially by tissue-specific prohormone convertases:
  - **Pancreatic α-cells (PCSK2/PC2):** cleaves proglucagon → **glucagon** (aa 33-61) + GRPP (glicentin-related pancreatic peptide) + intervening peptide 1/2 + MPGF (major proglucagon fragment, biologically inactive in the pancreas)
  - **Intestinal L-cells and brain neurons (PCSK1/PC1):** cleaves proglucagon → **GLP-1** (glucagon-like peptide-1, aa 72-108 or 78-108) + **GLP-2** (aa 126-158) + glicentin — the incretin hormones with opposite metabolic effects

**Glucagon peptide structure (29 amino acids):**
```
H-His1-Ser2-Gln3-Gly4-Thr5-Phe6-Thr7-Ser8-Asp9-Tyr10-
Ser11-Lys12-Tyr13-Leu14-Asp15-Ser16-Arg17-Arg18-Ala19-
Gln20-Asp21-Phe22-Val23-Gln24-Trp25-Leu26-Met27-Asn28-
Thr29-NH₂
```
- **His1** is essential for receptor activation (N-terminal truncation produces glucagon antagonists)
- **Phe6** and **Tyr10/Tyr13** are critical receptor-binding determinants
- In solution, glucagon is largely unstructured (random coil) at low concentration but adopts an α-helical conformation (residues 10-25) upon GCGR binding and in aggregated forms (fibrils — a challenge for formulation stability)
- **MW:** ~3,485 Da; pI ~6.8; t₁/₂ plasma ~5-6 minutes (cleared by liver, kidney, plasma dipeptidyl peptidase IV/DPP-4 — though DPP-4 acts less efficiently on glucagon than GLP-1)

**GCGR (Glucagon Receptor):**
- Class B1 GPCR (secretin family); 485 amino acids; 7-TM; expressed primarily in liver > kidney > heart > adipose > small intestine > pancreatic β-cells > brain
- Extracellular domain (ECD) binds the C-terminal helix of glucagon (the "two-domain" binding model: ECD + TMD cooperate); N-terminal His1 of glucagon engages the receptor TMD core to activate it
- Couples to **Gαs** → adenylate cyclase → ↑cAMP → PKA activation (primary pathway)
- Also couples to **Gαq** at high concentrations → PLC → IP₃/DAG → PKC → Ca²⁺ mobilization (secondary pathway; relevant at supra-physiological concentrations)

## Function

Glucagon coordinates a multi-organ catabolic response to maintain euglycemia during fasting, hypoglycemia, and energy expenditure:

**Liver (primary target):**
1. **Glycogenolysis:** Rapid (minutes) mobilization of hepatic glycogen (normally 70-100 g stored); provides glucose over first ~8 hours of fasting
2. **Gluconeogenesis:** Sustained (hours-to-days) synthesis of new glucose from: lactate (Cori cycle), amino acids (alanine cycle from muscle), glycerol (from lipolysis), and propionate (from odd-chain fatty acid oxidation)
3. **Ketogenesis:** ↓Malonyl-CoA → ↑CPT-1 → ↑β-oxidation → ↑acetyl-CoA → ↑HMG-CoA synthase/lyase → ↑β-hydroxybutyrate and acetoacetate; ketone bodies provide fuel for brain, heart, and muscle during prolonged fasting

**Adipose tissue:**
- GCGR activation (lower expression than liver) → HSL (hormone-sensitive lipase) activation → ↑lipolysis → ↑free fatty acid release to blood → liver β-oxidation substrate → gluconeogenic (glycerol) substrate

**Heart and skeletal muscle:**
- Minor GCGR expression; glucagon at pharmacological doses → ↑HR, ↑contractility (relevant for beta-blocker overdose treatment — glucagon rescues cardiac function)

## Mechanism

### Signal Transduction: cAMP-PKA Cascade in the Hepatocyte

Upon glucagon binding to GCGR: [^drucker-2018-glucagon-physiology]

1. **Gs activation → adenylate cyclase (AC) → ↑cAMP:** GCGR-Gαs coupling stimulates membrane-bound adenylate cyclase III/V/VI → cAMP rises from resting ~0.1 µM to ~1-5 µM within seconds

2. **PKA activation:** cAMP binds regulatory subunits (R1α, R2α) of PKA → releases catalytic subunits (Cα) → free active Cα subunit phosphorylates Ser/Thr residues on target proteins:

3. **Glycogenolysis (within 1-2 minutes):**
   - PKA phosphorylates and activates **phosphorylase kinase** (PhK)
   - PhK phosphorylates and activates **glycogen phosphorylase b → a**
   - Phosphorylase a cleaves α-1,4-glycosidic bonds in glycogen → glucose-1-phosphate → glucose-6-phosphate → dephosphorylated by glucose-6-phosphatase (G6Pase, present only in liver and kidney) → **free glucose released to blood**
   - Simultaneously: PKA phosphorylates **glycogen synthase** (inactivating it) → dual action stops glycogen synthesis and drives breakdown

4. **Gluconeogenesis (minutes-to-hours, transcriptional component):**
   - Short-term: PKA phosphorylates and activates **fructose-1,6-bisphosphatase** (FBPase) and inhibits PFK-2 (↓fructose-2,6-bisphosphate) → diverts metabolites toward gluconeogenesis
   - Long-term: PKA → **CREB phosphorylation** (Ser133) → CREB + CBP/p300 → transcription of **PGC-1α** → drives PEPCK (phosphoenolpyruvate carboxykinase) and G6Pase expression → sustained gluconeogenic capacity

5. **Ketogenesis (hours-to-days):**
   - PKA → ↓acetyl-CoA carboxylase (ACC) activity → ↓malonyl-CoA → relieves malonyl-CoA inhibition of CPT-1 (carnitine palmitoyl-transferase 1, the rate-limiting step of mitochondrial fatty acid import)
   - ↑FA entry into mitochondria → ↑β-oxidation → ↑acetyl-CoA excess → ↑HMG-CoA synthase/lyase → ↑ketone body production (β-hydroxybutyrate >> acetoacetate in severe fasting)

### Regulation of Glucagon Secretion

**Stimulators of glucagon secretion:**
- **Hypoglycemia:** The primary physiological stimulus; α-cells sense glucose via KATP channel-dependent and -independent mechanisms (controversial whether α-cells sense glucose directly or via paracrine β-cell signals)
- **Amino acids** (especially arginine, alanine): Direct α-cell stimulation via amino acid transporters → membrane depolarization → Ca²⁺ influx → exocytosis; this prevents hypoglycemia after protein-only meals (protein ingestion → insulin rises → without glucagon, hypoglycemia would follow)
- **Epinephrine (adrenaline):** β₂-adrenergic receptors on α-cells → Gs → ↑cAMP → ↑glucagon; critical for hypoglycemia counterregulation (including during exercise)
- **Sympathetic nervous system:** Norepinephrine via β₂-AR; nerve terminals innervate islets
- **Cortisol:** Indirect effect — cortisol-driven proteolysis → ↑amino acid delivery → ↑glucagon
- **Gastric inhibitory peptide (GIP):** Stimulates both insulin AND glucagon (relevant for tri-agonist drug design)

**Inhibitors of glucagon secretion:**
- **Glucose (hyperglycemia):** ↑Glucose → ↑insulin/GABA/Zn²⁺ from β-cells → paracrine suppression of α-cells; also possible direct glucose effects on α-cells
- **Insulin:** Via paracrine inhibition within the islet (KATP-independent); insulin receptor on α-cells → PI3K → Akt → ↓glucagon granule exocytosis
- **GLP-1:** Potently suppresses α-cell glucagon via GLP-1R → Gαs (paradoxically — GLP-1R couples to Gs in α-cells but produces opposite effect to glucagon in liver); inhibits α-cell exocytosis — mechanism involves ↑cAMP → PKA → phosphorylation of inhibitory substrates in α-cells (distinct from stimulatory PKA cascade in hepatocytes)
- **Somatostatin (δ-cells):** Paracrine inhibition via SSTR2 (Gi-coupled) → ↓cAMP → ↓glucagon; somatostatin analogs (octreotide, lanreotide) suppress glucagon in insulinoma management and treat glucagonoma excess
- **Hyperglucagonemia in T2DM:** Critically, α-cells in T2DM fail to suppress glucagon after meals (loss of glucose/insulin paracrine suppression due to β-cell dysfunction and α-cell insulin resistance) → inappropriate postprandial glucagon → hepatic glucose output persists → worsens postprandial hyperglycemia

### Glucagon as Drug: Rescue and Novel Therapeutics

**Classic use — hypoglycemia rescue:**
- Subcutaneous or IM glucagon (1 mg) raises blood glucose ~50-100 mg/dL within 10-15 minutes; requires intact hepatic glycogen stores to work (fails in prolonged fasting or alcohol-induced hypoglycemia, where glycogen is depleted)
- Nasal glucagon powder (Baqsimi) and autoinjector formulations (Gvoke, Zegalogue — dasiglucagon) improve ease of use in emergencies
- Intranasal 3 mg → measurable glucose rise within 10 minutes

**Emerging therapeutic targets — glucagon receptor antagonists:**
- Liver-selective GCGR antagonists (LY2409021, PF-06291874): reduce HbA1c by 0.5-1.5% in T2DM RCTs but cause compensatory hyperglucagonemia → massive α-cell hyperplasia (safety concern) and ↑LDL/↑liver transaminases — pipeline largely halted

**Incretin/glucagon tri-agonism (the future):**
- **Retatrutide (GLP-1R + GIPR + GCGR triple agonist):** The glucagon component at low doses contributes to energy expenditure (↑thermogenesis in brown adipose tissue), ↑hepatic fat oxidation (↓NAFLD), and appetite suppression (acting centrally via hypothalamic GCGR); Phase 2 trials showed ~24% body weight loss at 48 weeks — the most weight loss seen with any pharmacological agent; ↑glucagon receptor agonism in this context works because the GLP-1R + GIPR components maintain normoglycemia despite glucagon's hyperglycemic potential

## Connections

- **Modulates** → [Liver](../../../../../01-human/06-organ/liver/README.md): Glucagon is the dominant hormonal driver of hepatic glucose output. GCGR → cAMP → PKA simultaneously activates glycogen phosphorylase (glycogenolysis) and CREB-driven PEPCK/G6Pase transcription (gluconeogenesis), while ↓malonyl-CoA drives the shift to β-oxidation and ketogenesis. The liver expresses the highest GCGR density of any tissue and is glucagon's primary physiological target.

- **Modulates** → [Hepatocyte](../../../../../01-human/04-cellular/hepatocyte/README.md): At the cellular level, PKA phosphorylates glycogen phosphorylase kinase (activating it) and glycogen synthase (inactivating it), simultaneously driving glycogen breakdown and halting synthesis. Glucagon also ↓malonyl-CoA via ACC inhibition → ↑CPT-1 activity → ↑mitochondrial fatty acid import → ↑β-oxidation → ↑ketogenesis from hepatic acetyl-CoA overflow.

- **Modulated-by** → [Insulin](../../../../../01-human/03-molecular/insulin/README.md): Insulin suppresses glucagon secretion via paracrine inhibition (GABA and Zn²⁺ co-released from β-cells → α-cell hyperpolarization) and opposes glucagon's hepatic effects by activating glycogen synthase and suppressing PEPCK via PI3K-Akt-FoxO1 signaling. The insulin:glucagon molar ratio is the master hepatic switch. In T2DM, α-cell insulin resistance disrupts this suppression → pathological hyperglucagonemia.

- **Modulates** → [Digestive System](../../../../../01-human/07-system/digestive-system/README.md): The GCG gene expressed in intestinal L-cells is processed by PC1/3 (not PC2) to yield GLP-1, which potently suppresses α-cell glucagon — a critical negative feedback loop. Protein ingestion stimulates α-cell glucagon to prevent amino acid-induced hypoglycemia. GIP from K-cells also modulates glucagon, informing dual/triple incretin-glucagon agonist pharmacology.

[^drucker-2018-glucagon-physiology]: Sandoval DA, D'Alessio DA. Physiol Rev. 2015;95(2):513-48. doi:10.1152/physrev.00013.2014
[^unger-1971-glucagon-diabetes]: Unger RH, Orci L. Physiol Rev. 1976;56(4):778-826. doi:10.1152/physrev.1976.56.4.778

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
