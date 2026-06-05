---
schema: human-scale-entry/v1
id: islet-of-langerhans
name: Islet of Langerhans
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-05
summary: "Compact endocrine clusters (~1 million per pancreas) containing β-cells (insulin), α-cells (glucagon), δ-cells (somatostatin), PP cells, and ε-cells (ghrelin). KATP channel-coupled glucose sensing drives pulsatile insulin secretion controlling systemic glycaemia."
aliases: ["pancreatic islet", "islet", "islets of Langerhans", "endocrine pancreas", "pancreatic islet microorgan"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/pancreas
    relation: part-of
    note: "~1 million islets dispersed within exocrine pancreatic tissue (~1–2% of mass); islets receive 5–10× higher blood flow per unit weight; paracrine and neural signals within islets coordinate β/α/δ cell function."
  - target: 01-human/03-molecular/insulin
    relation: expresses
    note: "β-cells are the exclusive source of insulin; GLUT2/glucokinase sensing → KATP channel closure → Ca²⁺ influx → exocytosis; first-phase (pre-formed granules) and second-phase secretion; first-phase loss is an early T2DM marker."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Portal vein delivers insulin (~5× peripheral concentration) to hepatocytes; 50% extracted in first pass; portal insulin suppresses hepatic glucose output (glycogenolysis + gluconeogenesis); absent in T1DM → fasting hyperglycaemia."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: modulates
    note: "Cortisol activates GR in β-cells → impairs GLP-1R signalling and Ca²⁺ entry; GR in hepatocytes → ↑gluconeogenesis; GR in skeletal muscle → ↑insulin resistance; β-cell reserve determines steroid-induced DM risk."
---

# Islet of Langerhans

## Overview

Islets of Langerhans are compact, ovoid endocrine microorgans (100–200 µm diameter) dispersed throughout the exocrine pancreatic tissue. Approximately one million islets exist per adult pancreas, representing only 1–2% of pancreatic mass yet receiving 5–10 times higher blood flow per unit weight than the surrounding acinar tissue.[^guyton-hall] Each islet is a highly vascularised, autonomously regulated endocrine unit that monitors blood glucose, amino acid, and incretin levels in real time and secretes hormones to maintain glucose homeostasis within the narrow range of 4–7 mmol/L.

The five cell types of the islet act as a paracrine community, integrating signals from the portal blood, autonomic nervous system, and neighbouring islet cells through gap junctions, paracrine diffusion (aided by the centrifugal portal blood flow: β-cell core → α/δ cell periphery), and direct neural input.[^alberts-mol-cell-biology] Loss or dysfunction of β-cells underlies both type 1 diabetes mellitus (absolute loss via autoimmune destruction) and type 2 diabetes mellitus (progressive functional failure combined with insulin resistance), the two most prevalent metabolic diseases globally.

## Structure

**Cell types and proportions.**

| Cell type | Proportion | Hormone | Location in human islet |
|-----------|-----------|---------|--------------------------|
| β-cell | 65–80% | Insulin, C-peptide, amylin (IAPP) | Central core |
| α-cell | 15–20% | Glucagon | Peripheral mantle |
| δ-cell | 5–10% | Somatostatin (SST-14/SST-28) | Peripheral mantle |
| PP/γ-cell | 1–5% | Pancreatic polypeptide | Peripheral (mainly head of pancreas) |
| ε-cell | <1% | Ghrelin | Scattered (mainly fetal) |

**Islet architecture.** Human islets adopt a "mantle" (corino) configuration: β-cells cluster centrally, with α, δ, and PP cells forming a peripheral rim. This differs from rodent islets (where β-cells completely surround α/δ cells). The islet portal microcirculation flows from the β-cell core outward, so insulin and Zn²⁺ secreted by β-cells bathe peripheral α-cells first — the paracrine basis of glucose-mediated glucagon suppression. Gap junctions (connexin-36, Cx36) between adjacent β-cells synchronise calcium oscillations, generating pulsatile insulin secretion at 2–14 minute intervals.[^alberts-mol-cell-biology]

**Innervation.** Islets receive sympathetic (norepinephrine: α₂R→Gi→↓insulin; β₂R→Gs→↑glucagon), parasympathetic (acetylcholine: M3→Gq→IP₃→Ca²⁺→↑insulin, particularly pre-meal cephalic phase), and sensory (CGRP, substance P) input, as well as neuropeptides VIP and GRP (gastrin-releasing peptide → ↑insulin).

**KATP channel structure.** An octameric complex of 4 Kir6.2 pore subunits + 4 SUR1 regulatory subunits. SUR1 contains two ABC domains (NBD1, NBD2): NBD1 binds ATP (inhibitory, closes channel); NBD2 binds MgADP (stimulatory, opens channel — provides negative feedback after secretion). Sulphonylureas (glibenclamide, gliclazide) bind SUR1 → channel closure → depolarisation → ↑insulin. Diazoxide binds SUR1 → channel opening → hyperpolarisation → ↓insulin (used in nesidioblastosis). Repaglinide/nateglinide (meglitinides) bind a distinct site on SUR1 for faster, meal-coupled insulin release.[^guyton-hall]

## Function

**Glucose-stimulated insulin secretion (GSIS) by β-cells.**
1. Glucose enters β-cells via GLUT2 (low-affinity, high-capacity glucose transporter; Km ~15 mM) — flux is proportional to blood glucose concentration.
2. Glucokinase (GCK, hexokinase IV; Km ~10 mM, Hill coefficient ~1.7) phosphorylates glucose → glucose-6-phosphate; GCK is the rate-limiting glucose sensor ("glucose thermostat").
3. Glycolysis → pyruvate → TCA cycle → oxidative phosphorylation → ↑ATP/ADP ratio.
4. ↑ATP/ADP → KATP channel closure (Kir6.2/SUR1) → plasma membrane depolarisation (from ~−70 mV toward −40 mV).
5. Voltage-gated L-type Ca²⁺ channels (Cav1.2, Cav1.3) open → [Ca²⁺]ᵢ rises from ~100 nM to ~500 nM.
6. Ca²⁺ triggers SNARE-mediated exocytosis of insulin granules (VAMP2/syntaxin-1A/SNAP25 complex).[^guyton-hall]

**Biphasic insulin secretion.**
- *First phase* (rapid, ~5 min): Pre-docked, release-ready insulin granules at the plasma membrane; immediately responsive to glucose rise. Blunted or absent in early T2DM — an important clinical biomarker.
- *Second phase* (sustained, 15–60+ min): Newly recruited granules translocated from reserve pool to plasma membrane via actin/tubulin cytoskeletal tracks; dependent on ongoing Ca²⁺ influx and amplifying signals.

**Amplifying signals (KATP-independent).**
- GLP-1 (glucagon-like peptide-1, from intestinal L-cells): GLP-1R → Gs → ↑cAMP → PKA (phosphorylates KATP, Cav1.2, exocytosis machinery) + Epac2 → potentiates glucose-stimulated insulin secretion and β-cell survival; basis of GLP-1 agonist therapy (semaglutide, liraglutide).
- GIP (glucose-dependent insulinotropic peptide, from duodenal K-cells): GIPR→Gs→cAMP; blunted in T2DM.
- Free fatty acids: FFA1R/GPR40 → Gq → IP₃ → Ca²⁺ → amplifies GSIS (basis of fasiglifam).
- Acetylcholine (M3R → Gq → IP₃/DAG → PKC + Ca²⁺ → augments GSIS).

**α-cell glucagon secretion.** Glucagon is secreted when blood glucose falls below ~4 mmol/L (or when amino acids rise, independent of glucose). Low glucose → ↓ATP/ADP in α-cells → KATP channel partially open → maintained depolarisation → T-type Ca²⁺ channel + Na⁺ channel → action potential → glucagon granule exocytosis. Paracrine inhibition by β-cell insulin and Zn²⁺ (co-released with insulin) suppresses α-cell output during euglycaemia and hyperglycaemia; disrupted in T1DM → glucagon excess → ketoacidosis risk.

**δ-cell somatostatin.** SST-14/SST-28 act via SSTR2 on β-cells (Gi → ↓cAMP → ↓insulin exocytosis) and SSTR1/2 on α-cells (Gi → ↓glucagon), providing a paracrine brake on islet hormone secretion. Stimulated by high glucose, amino acids, and GLP-1. Pharmacological analogue octreotide suppresses glucagon in glucagonoma and insulin in insulinoma.

## Connections

- **part-of** [pancreas](../../06-organ/pancreas/README.md): ~1 million islets dispersed within exocrine pancreatic tissue (~1–2% of mass); islets receive 5–10× higher blood flow per unit weight; paracrine and neural signals within islets coordinate β/α/δ cell function.
- **expresses** [insulin](../../03-molecular/insulin/README.md): β-cells are the exclusive source of insulin; GLUT2/glucokinase sensing → KATP channel closure → Ca²⁺ influx → exocytosis; first-phase (pre-formed granules) and second-phase secretion; first-phase loss is an early T2DM marker.
- **modulates** [liver](../../06-organ/liver/README.md): Portal vein delivers insulin (~5× peripheral concentration) to hepatocytes; 50% extracted in first pass; portal insulin suppresses hepatic glucose output (glycogenolysis + gluconeogenesis); absent in T1DM → fasting hyperglycaemia.
- **modulates** [glucocorticoid-receptor](../../03-molecular/glucocorticoid-receptor/README.md): Cortisol activates GR in β-cells → impairs GLP-1R signalling and Ca²⁺ entry; GR in hepatocytes → ↑gluconeogenesis; GR in skeletal muscle → ↑insulin resistance; β-cell reserve determines steroid-induced DM risk.

## Pathology

**Type 1 diabetes mellitus (T1DM).** CD4⁺ and CD8⁺ T cell autoimmune destruction of β-cells, mediated by molecular mimicry (e.g., viral antigens cross-reacting with islet autoantigens: GAD65, IA-2/ICA512, ZnT8, proinsulin). HLA-DR3/DR4-DQ2/DQ8 haplotypes confer ~50% of genetic risk; non-HLA loci (INS VNTR, PTPN22, IL2RA) contribute additional risk. Complete β-cell loss → absolute insulin deficiency → hyperglycaemia, ketoacidosis (unopposed glucagon→↑hepatic ketogenesis), catabolism. Management: basal-bolus insulin analogues; closed-loop insulin pump systems (artificial pancreas); pancreatic or islet transplantation (Edmonton protocol: cadaveric islet infusion into portal vein → hepatic engraftment → insulin independence ~50% at 1 year, declining without immunosuppression); stem cell-derived β-cells (Vertex VX-880, Phase 1/2 data: insulin independence achieved).[^guyton-hall]

**Type 2 diabetes mellitus (T2DM).** Progressive β-cell functional failure superimposed on peripheral insulin resistance (skeletal muscle, liver, adipose). Islet amyloid (IAPP/amylin aggregation → β-cell toxicity, membrane disruption), β-cell glucolipotoxicity (chronic ↑glucose + ↑FFA → ER stress, oxidative stress, mitochondrial dysfunction), and HIF-1α hypoxia → ↓β-cell mass (~50% loss at T2DM diagnosis). Loss of first-phase insulin secretion is the earliest functional defect. Treatment escalation: lifestyle → metformin (↓hepatic glucose output) → sulphonylureas (KATP closure → ↑insulin) → GLP-1 agonists (↑GSIS + ↓glucagon + weight loss) → DPP-4 inhibitors → SGLT2 inhibitors (renal glucose excretion) → insulin.

**Insulinoma.** β-cell adenoma (~90% benign, ~10% malignant) → autonomous insulin secretion independent of blood glucose → fasting hypoglycaemia. Whipple's triad: symptomatic hypoglycaemia + low blood glucose + relief with glucose. C-peptide positive (distinguishes from exogenous insulin). Localised by endoscopic ultrasound + CT; curative treatment: enucleation or distal pancreatectomy. Medical bridge: diazoxide (↑KATP opening → ↓insulin), octreotide.

**Glucagonoma.** α-cell tumour → chronic glucagon excess → necrolytic migratory erythema (NME, pathognomonic), new-onset diabetes, normochromic anaemia, weight loss, DVT/PE. 80% malignant at diagnosis. Treat: octreotide, surgical resection, everolimus/streptozocin for metastatic disease.

**Nesidioblastosis / Persistent hyperinsulinaemic hypoglycaemia of infancy (PHHI).** Loss-of-function mutations in KATP channel subunits (ABCC8/SUR1 or KCNJ11/Kir6.2) → constitutive membrane depolarisation → unregulated insulin secretion regardless of glucose → severe neonatal hypoglycaemia. Treat: diazoxide (KATP opener); if unresponsive, near-total pancreatectomy.

## See Also

- [pancreas](../../06-organ/pancreas/README.md) — organ context for islet tissue
- [insulin](../../03-molecular/insulin/README.md) — principal secretory product of the β-cell
- [insulin-receptor](../../03-molecular/insulin-receptor/README.md) — mediates insulin action in target tissues
- [glucocorticoid-receptor](../../03-molecular/glucocorticoid-receptor/README.md) — links stress axis to β-cell dysfunction
- [liver](../../06-organ/liver/README.md) — primary target of portal insulin for glucose homeostasis
- [t-helper-cell](../../04-cellular/t-helper-cell/README.md) — mediates autoimmune β-cell destruction in T1DM
