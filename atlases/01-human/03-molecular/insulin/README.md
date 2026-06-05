---
schema: human-scale-entry/v1
id: insulin
name: Insulin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "51 aa peptide hormone from pancreatic β-cells. Master regulator of glucose homeostasis: drives GLUT4 uptake, suppresses hepatic gluconeogenesis via Akt, and coordinates anabolic metabolism. Deficiency or resistance underlies diabetes mellitus."
taxonomy:
  gene_symbol: "INS"
  uniprot: "P01308"
  note: "P01308 = human insulin preproprotein; 5.8 kDa = mature hexameric monomer unit (5808 Da)"
aliases: ["regular insulin", "human insulin", "INS", "peptide hormone"]
sources:
  - id: banting-best-1922-insulin
    type: peer-reviewed
    cite: "Banting FG, Best CH, Collip JB, Campbell WR, Fletcher AA. Pancreatic extracts in the treatment of diabetes mellitus. Can Med Assoc J. 1922;12(3):141-6."
    pmid: "14005847"
  - id: saltiel-2001-insulin-signaling
    type: peer-reviewed
    cite: "Saltiel AR, Kahn CR. Insulin signalling and the regulation of glucose and lipid metabolism. Nature. 2001;414(6865):799-806."
    doi: "10.1038/414799a"
  - id: dcct-1993-t1dm-intensive
    type: peer-reviewed
    cite: "The Diabetes Control and Complications Trial Research Group. The effect of intensive treatment of diabetes on the development and progression of long-term complications in insulin-dependent diabetes mellitus. N Engl J Med. 1993;329(14):977-86."
    doi: "10.1056/NEJM199309303291401"
cross_links:
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Insulin suppresses hepatic gluconeogenesis (via FOXO1 phosphorylation) and promotes glycogen synthesis and lipogenesis."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Insulin promotes endothelial NO production and vascular smooth muscle relaxation; chronic hyperinsulinemia and insulin resistance drive atherosclerosis and hypertension."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Insulin crosses the blood-brain barrier via receptor-mediated transcytosis; acts in hypothalamus to suppress appetite and in hippocampus to modulate memory and neuroplasticity."
  - target: 01-human/07-system/digestive-system
    relation: modulated-by
    note: "Nutrient absorption in the gut drives postprandial glucose and GLP-1/GIP incretin release, which are the primary physiological stimuli for insulin secretion."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: modulated-by
    note: "Metformin reduces hepatic insulin resistance via AMPK-mediated gluconeogenesis suppression, allowing lower insulin concentrations to maintain euglycemia; metformin does not stimulate insulin secretion."
  - target: 01-human/02-atomic/carbon
    relation: contains
    evidence: saltiel-2001-insulin-signaling
    note: "Insulin's 51-residue chain is built entirely on carbon backbones: each α-carbon provides the sp³ stereocentre of every amino acid, carbonyl carbons form every peptide bond, and cysteine carbons anchor the three disulfide bonds."
  - target: 03-medicine/02-traditional/berberine
    relation: modulated-by
    evidence: saltiel-2001-insulin-signaling
    note: "Berberine activates AMPK (via mitochondrial Complex I inhibition) and independently upregulates insulin receptor expression, sensitising peripheral tissues to insulin signalling; HbA1c reduction ~1.0% is comparable to metformin 1500 mg/day."
  - target: 01-human/03-molecular/insulin-receptor
    relation: targets
    evidence: saltiel-2001-insulin-signaling
    note: "The insulin receptor (INSR) is the primary target of insulin; insulin binds with Kd ~0.1 nM, triggering β-subunit Tyr1158/1162/1163 autophosphorylation and IRS-1/2-mediated PI3K→Akt signalling cascade."
  - target: 01-human/03-molecular/insulin-receptor
    relation: modulated-by
    evidence: saltiel-2001-insulin-signaling
    note: "Insulin secretion and receptor downregulation create a feedback loop: activated IR drives IRS-1 Ser phosphorylation via mTORC1/S6K1, reducing IRS-1 Tyr signalling — a negative feedback limiting insulin action."
  - target: 01-human/06-organ/pancreas
    relation: part-of
    evidence: banting-best-1922-insulin
    note: "Insulin is synthesised exclusively in pancreatic β cells of the islets of Langerhans; preproinsulin is processed to proinsulin in the ER and cleaved by PC1/3 and PC2 to yield mature insulin stored in secretory granules."
  - target: 01-human/06-organ/pancreas
    relation: modulated-by
    evidence: banting-best-1922-insulin
    note: "Pancreatic β cells secrete insulin in response to glucose (>6 mmol/L), amino acids, GLP-1, and GIP; glucose-stimulated insulin secretion via KATP channel closure and Ca²⁺-triggered exocytosis is the primary regulatory mechanism."
  - target: 01-human/03-molecular/glucagon
    relation: modulates
    note: "Modulates by Glucagon."
  - target: 01-human/03-molecular/ampk
    relation: modulated-by
    note: "Modulated by AMPK."
  - target: 01-human/02-atomic/zinc
    relation: modulated-by
    note: "Modulated by Zinc."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: expressed-by
    note: "Expressed by Islet of Langerhans."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: modulated-by
    note: "Modulated by Panax ginseng (Korean Red Ginseng)."
---

# Insulin

## Overview

Insulin is the body's **master anabolic hormone** — a 51 amino acid peptide secreted by pancreatic β-cells in direct proportion to blood glucose concentration. Its discovery in 1921–1922 by Banting, Best, Collip, and Macleod at the University of Toronto transformed type 1 diabetes from a uniformly fatal wasting disease into a manageable chronic condition, earning the Nobel Prize in 1923 [^banting-best-1922-insulin]. It remains among the most important molecules in clinical medicine: insulin therapy sustains the lives of over 8 million people with type 1 diabetes worldwide, and is a critical tool in the management of type 2 diabetes.

Physiologically, insulin acts as a **glucose sensor and metabolic coordinator**: when portal glucose rises after a meal, β-cells respond within seconds with first-phase insulin release, suppressing hepatic glucose output and driving peripheral uptake. Between meals, falling insulin permits lipolysis and ketogenesis, maintaining fuel delivery during fasting. The ratio of insulin to its counter-regulatory antagonist glucagon is the primary determinant of whether the liver produces or consumes glucose at any moment.

The molecular signaling pathway — insulin receptor tyrosine kinase → IRS → PI3K → Akt — is one of the most studied in all of cell biology, both because of its fundamental importance and because its disruption underlies type 2 diabetes, the metabolic syndrome, and contributes to aging-related insulin resistance [^saltiel-2001-insulin-signaling].

## Structure

### Peptide Architecture

Insulin is synthesized as a **single-chain preproprotein** (110 aa), processed through two intermediates:

| Form | Description |
|:---|:---|
| **Preproinsulin** (110 aa) | Signal peptide (24 aa) + B-chain + C-peptide + A-chain; cotranslationally translocated into ER lumen |
| **Proinsulin** (86 aa) | After signal peptide cleavage; single chain B-C-A; folds in ER with 3 disulfide bonds |
| **Insulin** (51 aa) | Prohormone convertases PC1/3 and PC2 excise the **C-peptide** (31 aa) in secretory granules; A-chain (21 aa) and B-chain (30 aa) remain linked by **2 interchain disulfide bonds** (A7-B7, A20-B19) and 1 intrachain bond (A6-A11) |

**C-peptide** is secreted in equimolar amounts with insulin and is used clinically as a marker of endogenous β-cell secretory capacity (unaffected by exogenous insulin administration, because therapeutic insulin lacks C-peptide). C-peptide has modest biological activity of its own (renal and neural microvascular effects) but its primary value is diagnostic.

In solution at high concentrations (as in secretory granules), insulin self-assembles into **hexamers** coordinated by two Zn²⁺ ions at the center of the B10 His triad. Rapid-acting insulin analogs (lispro, aspart, glulisine) are engineered to disrupt hexamer formation, allowing faster dissociation into biologically active monomers after subcutaneous injection.

### Receptor

The **insulin receptor (IR)** is a **receptor tyrosine kinase (RTK)** of the heterotetrameric class:
- **Structure:** α₂β₂ disulfide-linked dimer-of-heterodimers; the two α-subunits form the extracellular ligand-binding domain; two β-subunits span the membrane and contain the cytoplasmic kinase domains
- **Gene:** *INSR* (chromosome 19p13.2); alternatively spliced into IR-A and IR-B isoforms with different affinities for IGF-II and insulin
- **Related receptors:** IGF-1 receptor (IGF1R) shares ~50% homology; hybrid IR/IGF1R receptors exist in some tissues

## Mechanism

### Glucose-Stimulated Insulin Secretion (GSIS)

The canonical β-cell secretion model:

1. **Glucose uptake:** GLUT2 (liver, β-cell) or GLUT1 (rodent β-cell) transports glucose down its gradient; rate proportional to blood glucose
2. **Glycolysis → ↑ ATP/ADP ratio:** Glucose metabolism elevates cytosolic ATP:ADP; glucokinase (hexokinase IV) is the glucose sensor — low affinity (Km ~10 mM), rate-limiting for β-cell glucose oxidation
3. **KATP channel closure:** Rising ATP closes **ATP-sensitive K⁺ channels** (Kir6.2/SUR1 complex) → membrane depolarization from ~−70 mV toward ~−40 mV
4. **Ca²⁺ influx:** Depolarization opens **voltage-gated Ca²⁺ channels** (Cav1.2/1.3, L-type) → [Ca²⁺]i spike
5. **Exocytosis:** Ca²⁺ triggers SNARE-mediated fusion of insulin secretory granules with the plasma membrane → insulin release into portal blood

**First-phase secretion (0–10 min):** Rapid release of a small pool of **pre-docked granules** at the plasma membrane; amplitude reflects the size of this readily releasable pool; characteristically absent or blunted very early in T2DM.

**Second-phase secretion (10–60+ min and sustained):** Mobilization and exocytosis of reserve granule pools; requires ongoing ATP generation and granule trafficking; involves PKA (cAMP/GLP-1 amplification), PKC (DAG/IP₃), and Ca²⁺-dependent signaling.

**Incretin amplification:** GLP-1 and GIP (from intestinal L and K cells, respectively) bind GPCRs on β-cells → adenylyl cyclase → ↑cAMP → PKA and Epac2 → markedly enhanced second-phase secretion and β-cell survival. This is the basis of GLP-1 receptor agonist (semaglutide, liraglutide) and DPP-4 inhibitor pharmacology.

### Intracellular Signaling

Insulin binding to the IR α-subunit induces conformational change → **transautophosphorylation** of β-subunit activation loop Tyr residues (Tyr1158, Tyr1162, Tyr1163) → full kinase activation → phosphorylation of **IRS proteins (IRS1/IRS2)** on multiple Tyr residues [^saltiel-2001-insulin-signaling]:

**PI3K → Akt branch (metabolic):**
- Tyr-phosphorylated IRS1/2 recruit and activate **class IA PI3K** (p85 regulatory + p110 catalytic)
- PI3K phosphorylates PIP2 → **PIP3**
- PIP3 recruits **PDK1** and **mTORC2** to the membrane
- PDK1 + mTORC2 → **Akt (PKB)** phosphorylation at Thr308 and Ser473 → full Akt activation
- Akt substrates:
  - **AS160 (TBC1D4):** Akt phosphorylation inhibits AS160 GAP activity → Rab-GTP accumulates → **GLUT4 vesicle translocation** to plasma membrane (skeletal muscle and adipose tissue; 5- to 10-fold increase in glucose uptake)
  - **GSK3β:** Akt phosphorylates (inhibits) GSK3β → **glycogen synthase** remains active → glycogen synthesis
  - **FOXO1:** Akt phosphorylates FOXO1 → nuclear exclusion → suppression of gluconeogenic genes (PEPCK, G6Pase) → ↓ hepatic glucose output
  - **mTORC1 (via TSC2):** Akt phosphorylates TSC2 (inhibits) → Rheb-GTP → mTORC1 active → **p70S6K + 4E-BP1** → protein synthesis, ribosome biogenesis

**Ras/MAPK branch (mitogenic):**
- IRS1 or Shc adaptor → Grb2 → SOS → **Ras-GTP** → Raf → MEK → **ERK1/2** → cell proliferation and gene expression (this branch is less metabolic, more growth-promoting; aberrant in cancer insulin signaling)

**Akt-independent pathway: TC10/CAP-Cbl:**
- IR autophosphorylates Cbl-associated protein (CAP) → Cbl phosphorylation → recruits CrkII → TC10 activation at lipid rafts → secondary GLUT4 trafficking (minor pathway)

### Hepatic Glucose Regulation

The portal vein delivers insulin at ~3× the peripheral concentration directly to hepatocytes. In the fed state:
- Akt → FOXO1 nuclear exclusion → ↓ PEPCK, G6Pase → ↓ gluconeogenesis and glycogenolysis
- Akt → GSK3β inhibition → ↑ glycogen synthase → glycogen deposition
- ChREBP and SREBP-1c (activated by insulin) → ↑ lipogenesis → fatty acid and VLDL synthesis

In insulin-resistant T2DM, FOXO1 suppression fails but lipogenesis signaling is partially preserved — contributing to **selective hepatic insulin resistance** (ectopic fat, NAFLD, dyslipidemia).

## Function

### Glucose Homeostasis

Insulin and **glucagon** (from α-cells) jointly regulate blood glucose through opposing actions:

| Parameter | ↑ Insulin (fed state) | ↑ Glucagon (fasting/stress) |
|:---|:---|:---|
| Hepatic gluconeogenesis | ↓ (FOXO1 suppression) | ↑ (cAMP → CREB → PEPCK/G6Pase) |
| Hepatic glycogenolysis | ↓ | ↑ |
| Peripheral glucose uptake | ↑ (GLUT4 translocation) | No direct effect |
| Lipolysis (adipose) | ↓ (HSL inhibition via PDE3B) | ↑ |
| Ketogenesis (liver) | ↓ | ↑ |
| Protein synthesis | ↑ (mTORC1) | No direct effect |

Normal fasting glucose: 70–100 mg/dL; postprandial peak <140 mg/dL (returns to fasting within 2 h). This tight regulation protects the brain, which is almost entirely glucose-dependent and cannot use fatty acids.

### Anabolic Coordination

Beyond glucose, insulin coordinates the entire fed-state anabolic program:
- **Amino acid uptake** (hepatocytes, muscle): upregulates amino acid transporters; suppresses protein catabolism
- **Lipid storage:** stimulates lipase in adipocytes, promotes VLDL uptake via LPL upregulation; inhibits HSL to prevent lipolysis
- **Growth:** via mTORC1-mediated protein synthesis and IGF-1 receptor cross-talk

### Clinical Pharmacology of Insulin

The pharmacological goal is to mimic physiological insulin secretion:

| Category | Examples | Onset / Peak / Duration |
|:---|:---|:---|
| **Rapid-acting analogs** | Lispro, Aspart, Glulisine | 15 min / 1–2 h / 3–4 h |
| **Regular (short-acting)** | Human regular | 30–60 min / 2–4 h / 6–8 h |
| **Intermediate-acting** | NPH | 1–3 h / 4–10 h / 12–18 h |
| **Long-acting analogs** | Glargine (U100/U300), Detemir | 1–4 h / flat / 20–42 h |
| **Ultra-long-acting** | Degludec | 1–4 h / flat / >42 h (variable) |

**Biosimilars** (insulin glargine-yfgn, -aglr, etc.) are widely approved and have substantially reduced cost in many markets.

The DCCT trial demonstrated conclusively that intensive insulin therapy in T1DM (HbA1c ~7% vs ~9%) reduced: retinopathy progression by **76%**, nephropathy development by **50%**, and clinical neuropathy by **60%** [^dcct-1993-t1dm-intensive] — establishing tight glycemic control as the standard of care.

## Connections

- `expressed-by` → **[beta-cell](../../04-cellular/beta-cell/README.md)** (forward reference) — exclusively synthesized and secreted by pancreatic islet β-cells
- `modulates` → **[liver](../../06-organ/liver/README.md)** — suppresses gluconeogenesis, drives glycogen synthesis and lipogenesis via IRS1/Akt/FOXO1
- `modulates` → **[cardiovascular-system](../../07-system/cardiovascular-system/README.md)** — promotes vascular NO production; chronic resistance is atherogenic
- `modulates` → **[nervous-system](../../07-system/nervous-system/README.md)** — hypothalamic and hippocampal insulin signaling regulates appetite, neuroplasticity, and cognitive function
- `modulated-by` → **[digestive-system](../../07-system/digestive-system/README.md)** — postprandial glucose absorption and incretin (GLP-1, GIP) release from the gut are the primary physiological stimuli driving insulin secretion

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **Type 1 Diabetes Mellitus (T1DM)** | Autoimmune destruction of β-cells (HLA-DR3/DR4 risk; autoantibodies: GADA, IA-2A, ZnT8A, IAA) → absolute insulin deficiency | Hyperglycemia, weight loss, polyuria, polydipsia; life-threatening **diabetic ketoacidosis (DKA)** without insulin; requires lifelong insulin therapy |
| **Type 2 Diabetes Mellitus (T2DM)** | Peripheral insulin resistance (↓ PI3K/Akt in muscle, liver, fat) → compensatory hyperinsulinemia → progressive β-cell exhaustion → relative insulin deficiency | Gradual onset; initially managed with diet/metformin/GLP-1 agonists; eventually requires insulin in many patients; macrovascular and microvascular complications |
| **Diabetic Ketoacidosis (DKA)** | Near-complete insulin deficiency → unopposed glucagon → massive hepatic ketogenesis (β-hydroxybutyrate, acetoacetate) + hyperglycemia + osmotic diuresis → anion-gap metabolic acidosis | Nausea, Kussmaul breathing, fruity breath, altered consciousness; treated with insulin infusion + IV fluids + electrolyte correction |
| **Hyperosmolar Hyperglycemic State (HHS)** | Severe insulin deficiency with enough residual insulin to prevent ketosis; profound dehydration and hyperglycemia (>600 mg/dL) | Typically T2DM, elderly; mortality higher than DKA; treatment is gradual rehydration + insulin |
| **Hypoglycemia** | Excessive insulin (therapeutic, or insulinoma) → blood glucose <70 mg/dL | Autonomic symptoms (tremor, diaphoresis, tachycardia) at <70 mg/dL; neuroglycopenia (confusion, seizure, coma) at <50 mg/dL; brain is uniquely vulnerable due to sole dependence on glucose; **major barrier to tight glycemic control** |
| **Metabolic syndrome / insulin resistance** | Ectopic lipid accumulation, inflammation, mitochondrial dysfunction → serine phosphorylation of IRS1 → impaired PI3K signaling | Central obesity, hypertension, dyslipidemia, impaired fasting glucose; links to NAFLD/NASH, PCOS, CVD |
| **Insulinoma** | β-cell adenoma with unregulated insulin secretion | Fasting hypoglycemia; Whipple's triad (symptoms, glucose <55, resolution with glucose); diagnosed by elevated C-peptide during hypoglycemia |
| **Congenital hyperinsulinism** | Gain-of-function KATP channel mutations → constitutive β-cell depolarization → excess insulin | Neonatal persistent hypoglycemia; treated with diazoxide (KATP opener), somatostatin analogs, or partial pancreatectomy |

[^banting-best-1922-insulin]: Banting FG, Best CH, Collip JB, Campbell WR, Fletcher AA. Pancreatic extracts in the treatment of diabetes mellitus. *Can Med Assoc J.* 1922;12(3):141-6. [PubMed 14005847](https://pubmed.ncbi.nlm.nih.gov/14005847/)
[^saltiel-2001-insulin-signaling]: Saltiel AR, Kahn CR. Insulin signalling and the regulation of glucose and lipid metabolism. *Nature.* 2001;414(6865):799-806. [doi:10.1038/414799a](https://doi.org/10.1038/414799a)
[^dcct-1993-t1dm-intensive]: The Diabetes Control and Complications Trial Research Group. The effect of intensive treatment of diabetes on the development and progression of long-term complications in insulin-dependent diabetes mellitus. *N Engl J Med.* 1993;329(14):977-86. [doi:10.1056/NEJM199309303291401](https://doi.org/10.1056/NEJM199309303291401)
