---
schema: human-scale-entry/v1
id: sstr2
name: SSTR2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "SSTR2 (somatostatin receptor type 2) is the Gi-coupled GPCR mediating antiproliferative and antisecretory somatostatin signaling; SSTR2 is overexpressed in most well-differentiated NETs → octreotide/lanreotide SSA therapy and lutetium-177 DOTATATE PRRT (NETTER-1 trial)."
aliases: ["SSTR2", "somatostatin receptor 2", "somatostatin receptor type 2", "octreotide receptor", "DOTATATE receptor", "somatostatin receptor scintigraphy", "PRRT target", "NET receptor"]
sources:
  - id: rinke-2009-promid
    type: peer-reviewed
    cite: "Rinke A, Müller HH, Schade-Brittinger C, et al. Placebo-controlled, double-blind, prospective, randomized study on the effect of octreotide LAR in the control of tumor growth in patients with metastatic neuroendocrine midgut tumors: a report from the PROMID Study Group. J Clin Oncol. 2009;27(28):4656-4663."
    doi: "10.1200/JCO.2009.22.8510"
    pmid: "19704057"
    url: "https://doi.org/10.1200/JCO.2009.22.8510"
  - id: strosberg-2017-netter1
    type: peer-reviewed
    cite: "Strosberg J, El-Haddad G, Wolin E, et al. Phase 3 trial of 177Lu-DOTATATE for midgut neuroendocrine tumors. N Engl J Med. 2017;376(2):125-135."
    doi: "10.1056/NEJMoa1607427"
    pmid: "28076709"
    url: "https://doi.org/10.1056/NEJMoa1607427"
cross_links:
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Everolimus (mTOR inhibitor) is approved for SSTR2+ pancreatic NET (RADIANT-3: PFS 11.0 vs 4.6 months) and non-functional NET (RADIANT-4); SSA + everolimus combination provides additive antiproliferative effect via Gi-cAMP and mTOR dual suppression."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Sunitinib (VEGFR/PDGFR) is approved for pancreatic NET (PFS 11.4 vs 5.5 months); SSTR2 and VEGFR signaling are complementary targets in pNET; SSA + anti-VEGF combinations studied; bevacizumab active in midgut NET (SWOG S0518 trial)."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "NETs are highly vascularized; HIF-1α drives VEGF secretion in NET cells under hypoxia; everolimus (mTOR inhibitor) reduces HIF-1α → anti-angiogenic in pNET; HIF-1α pathway contributes to NET metastasis and resistance to SSA and PRRT."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Somatostatin (SSTR2 ligand) inhibits glucagon from pancreatic α-cells and insulin from β-cells; SSTR2 agonists (octreotide) control glucagonoma syndrome (necrolytic migratory erythema, diabetes); normal SSTR2 restrains glucagon in the inter-meal state."
---

# SSTR2

## Overview

**SSTR2 (Somatostatin Receptor Type 2)** is a member of the somatostatin receptor family (SSTR1-5), a group of seven-transmembrane Gi-coupled G protein-coupled receptors (GPCRs) that mediate the pleiotropic actions of **somatostatin (SST14 and SST28)** — a 14- or 28-amino-acid cyclic peptide synthesized by δ-cells of the pancreatic islets, hypothalamic neurons, D-cells of the gastric/intestinal mucosa, and immune cells. SSTR2 is the predominant somatostatin receptor subtype in most endocrine tumors and neuroendocrine neoplasms (NEN), where it is dramatically overexpressed relative to normal tissue → exploited both diagnostically (DOTATATE PET/CT; 68Ga-DOTATATE scintigraphy) and therapeutically (SSA and peptide receptor radionuclide therapy, PRRT). The pharmacological targeting of SSTR2 represents one of the most elegant examples of receptor-targeted oncology: somatostatin analogs (octreotide, lanreotide) bind SSTR2 → antiproliferative and antisecretory effects; radiolabeled somatostatin analogs (lutetium-177-DOTATATE, yttrium-90-DOTATOC) bring cytotoxic radiation directly to SSTR2+ tumor cells. The landmark NETTER-1 trial established lutetium-177 DOTATATE (Lutathera) as standard-of-care PRRT for SSTR2+ midgut NETs [^strosberg-2017-netter1] [^rinke-2009-promid].

**SSTR2 overexpression in neuroendocrine tumors:**
- **Gastroenteropancreatic NETs (GEP-NET):** SSTR2 overexpression in >80% of well-differentiated G1/G2 NETs; midgut NETs (small bowel, appendix, colon) ~90% SSTR2+; pancreatic NETs (pNET) ~75% SSTR2+; gastric NETs ~80%
- **Lung NETs:** Typical carcinoid ~90% SSTR2+; atypical carcinoid ~60% SSTR2+; SCLC ~50% SSTR2+ (variable, lower than carcinoids)
- **Meningioma:** ~80% SSTR2+; DOTATATE PET used for imaging; SSA not typically therapeutic
- **Pituitary adenoma:** GH-secreting (acromegaly): ~90% SSTR2+; SSA (octreotide/lanreotide/pasireotide) normalizes IGF-1 in ~65%; primary medical therapy pre-/post-surgery
- **Pheochromocytoma/paraganglioma (PPGL):** SSTR2/SSTR3/SSTR5 variable expression; DOTATATE PET is superior to MIBG for PPGL imaging; 177Lu-DOTATATE active in SSTR2+ PPGL
- **Thyroid:** Medullary thyroid carcinoma (MTC): SSTR2 variable (~40%); calcitonin/CEA markers more useful; vandetanib/cabozantinib are approved
- **Poorly differentiated NEC:** Low SSTR2 expression → PRRT generally not indicated; treat with cisplatin/etoposide

## Structure

### SSTR2 receptor architecture

SSTR2 is a 369-amino-acid, 41 kDa seven-transmembrane receptor:

**Extracellular domain (ECD) and binding pocket:**
- Three extracellular loops (ECL1, ECL2, ECL3) form the somatostatin ligand-binding pocket
- **Endogenous ligand binding:** SST14 (Trp-Lys-Thr-Phe-Thr-Ser-Cys-Phe-disulfide-bridge) → contacts ECL2 and transmembrane helices TM3/TM6; the pharmacophore is the Phe-Trp-Lys-Thr cyclic tetrapeptide
- **Octreotide/lanreotide selectivity:** These synthetic analogs retain the Phe-Trp-Lys-Thr cyclic pharmacophore → preferential binding to SSTR2 (Ki ~0.4 nM) and SSTR5 (Ki ~7 nM); do NOT significantly bind SSTR1/3/4; SSTR2 is therefore the primary therapeutic target of octreotide/lanreotide

**Pasireotide (pan-SSTR agonist):**
Pasireotide binds SSTR2 (Ki ~1 nM), SSTR3 (Ki ~5 nM), SSTR5 (Ki ~0.16 nM — highest affinity), and SSTR1 (Ki ~9 nM) → pan-SSTR agonist; approved for Cushing's disease (SSTR5 overexpression in ACTH-secreting pituitary adenomas); also used in acromegaly patients failing octreotide/lanreotide; higher rates of hyperglycemia (SSTR2 in β-cells normally stimulates insulin; SSTR5-dominated signaling inhibits insulin more severely).

**Transmembrane core and Gi coupling:**
TM1-TM7 helical bundle; intracellular loops ICL2 and ICL3 → Gi heterotrimer (Gαi/Gβγ) coupling; SST14/octreotide binding → GPCR conformational change → Gαi dissociation → Gαi inhibits adenylyl cyclase → ↓cAMP → ↓PKA activity → multiple downstream effects.

**DOTATATE and DOTATOC radiolabeling:**
DOTATATE (DOTA-Tyr3-octreotate) and DOTATOC (DOTA-Tyr3-octreotide) are SSTR2-selective chelator-conjugated analogs:
- DOTA chelator → binds gallium-68 (PET imaging: 68Ga-DOTATATE, half-life 68 min) or lutetium-177 (PRRT: 177Lu-DOTATATE, β emitter, half-life 6.7 days) or yttrium-90 (90Y-DOTATOC, higher energy β, for larger tumors)
- 177Lu-DOTATATE delivers ~200 Gy to SSTR2+ cells locally with ~1-2 mm tissue penetration (β emission) → DNA double-strand breaks → apoptosis; bystander effect via γ emission (also used for imaging at time of treatment)
- Dosimetry individualized for kidney dose limitation; kidneys express SSTR2 → renal accumulation → limiting toxicity is renal and hematologic

### SSTR2 signaling mechanisms

**Gi-dependent signaling:**
1. Gαi → adenylyl cyclase inhibition → ↓cAMP → ↓PKA → ↓CREB phosphorylation → reduced cyclin D1, MYC transcription → cell cycle arrest G1
2. Gβγ → PI3K-γ activation → IP3 → Ca²⁺ release; paradoxically also some Gβγ → PLC-β → DAG → PKC (cell-type specific)
3. Gαi → activation of K⁺ channels (GIRK) → hyperpolarization → reduced secretion from endocrine cells (inhibits insulin, glucagon, GH, TSH release)
4. Gαi → inhibition of voltage-gated Ca²⁺ channels → reduced exocytosis of secretory granules

**Receptor internalization and desensitization:**
SST14 → SSTR2 activation → GRK phosphorylation of ICL3/C-terminus → β-arrestin recruitment → clathrin-mediated endocytosis → receptor recycling (SSTR2 recycles rapidly, unlike SSTR3/5 which are more degraded) → PRRT benefit: SSTR2 internalizes with radiolabeled DOTATATE → intracellular radiation accumulation + receptor recycling to cell surface for further DOTATATE uptake.

**Anti-secretory mechanism in carcinoid syndrome:**
Carcinoid syndrome (flushing, diarrhea, bronchospasm) from serotonin, substance P, and bradykinin secretion by midgut NET liver metastases → octreotide/lanreotide → SSTR2 → Gαi → inhibits Ca²⁺ influx → blocks secretory granule exocytosis → reduced serotonin, substance P, VIP, glucagon, insulin secretion; telotristat (serotonin synthesis inhibitor, tryptophan hydroxylase 1 inhibitor) added for breakthrough diarrhea in carcinoid syndrome refractory to SSA.

## Function

### Normal SSTR2 physiology

**Hypothalamus-pituitary axis:**
Hypothalamic somatostatin (from periventricular nucleus) → SSTR2/5 on pituitary somatotrophs → inhibits GH secretion; pituitary SSTR2 → inhibits TSH and ACTH (modest effect); pancreatic δ-cells secrete SST14 in a paracrine manner → SSTR2 on adjacent α-cells (glucagon) and β-cells (insulin) → inhibition → inter-meal glucose homeostasis.

**GI tract and enteric nervous system:**
Intestinal D-cells secrete SST14 → SSTR2 on enteroendocrine cells and enterocytes → inhibits gastric acid (HCl), pepsinogen, CCK, secretin, VIP, motilin, and gastrin secretion; reduces intestinal motility via enteric neurons → SSA causes constipation and reduced gallbladder contractility (SSA-induced gallstones form in ~20% with long-term use → prophylactic ursodeoxycholic acid in some centers).

**Immune modulation:**
SSTR2 expressed on activated T-cells, macrophages, and dendritic cells → somatostatin → anti-inflammatory (inhibits TNF-α, IL-6, IFN-γ production); possibly contributes to tumor immune evasion in SSTR2+ NETs.

### SSTR2-targeted radionuclide therapy (PRRT)

**Mechanism of 177Lu-DOTATATE:**
1. IV administration → 177Lu-DOTATATE circulates and binds SSTR2 on NET cells
2. Receptor-ligand complex internalizes via clathrin-mediated endocytosis
3. Intracellular: DOTA-lutetium releases low-energy β radiation (0.5 MeV, 1-2 mm range) → DNA DSBs → cell death
4. Gamma emission (113/208 keV) used for post-treatment dosimetry imaging (scintigraphy)
5. SSTR2 recycles to surface → repeated DOTATATE uptake cycles amplify radiation dose
- Renal radiation dose: Limiting toxicity; amino acid infusion (lysine/arginine) given co-infusion to competitively block tubular reabsorption of DOTATATE → reduces renal dose; maximum cumulative dose 4 cycles of 7.4 GBq (200 mCi) each

**NETTER-1 trial (Phase 3):** [^strosberg-2017-netter1]
- 229 patients with progressive SSTR2+ midgut NET on octreotide LAR; randomized to 177Lu-DOTATATE + octreotide LAR 30 mg vs. octreotide LAR 60 mg (high-dose)
- 20-month PFS: 65.2% vs 10.8% (HR 0.21, p<0.001); ORR 18% vs 3%; interim OS: 48.0 vs 36.3 months
- FDA approved 2018 (Lutathera); standard of care for progressive SSTR2+ midgut NET post-SSA

## Mechanism

### Somatostatin analogs — pharmacology and resistance

**Octreotide LAR (long-acting release):** 20-30 mg IM q28d; SSTR2/SSTR5 selective; controls carcinoid syndrome in ~70-80% initially; antiproliferative (PROMID: PFS 14.3 vs 6.0 months in midgut NET) [^rinke-2009-promid].

**Lanreotide depot (Somatuline):** 90-120 mg SC q28d; SSTR2/SSTR5; CLARINET trial (placebo-controlled, non-functional GEP-NET G1/G2): PFS not reached vs 18 months (HR 0.47); FDA approved 2014 for non-functional GEP-NET.

**SSA resistance mechanisms:**
- SSTR2 downregulation (receptor loss by promoter methylation or post-translational degradation) → tumor "escapes" SSA
- Downstream pathway bypass: PI3K/mTOR activation → proliferation despite Gi suppression
- Receptor heterogeneity: Tumor subclones with SSTR1/3/4 dominance instead of SSTR2
- Management: Add everolimus (mTOR inhibitor) or PRRT (if still SSTR2+ by DOTATATE PET); switch to chemotherapy for G3

**SSTR2 status assessment:**
- 68Ga-DOTATATE PET/CT (Netspot, FDA 2016): Sensitivity ~96%, specificity ~100% for SSTR2+ NET lesions ≥1 cm; superior to CT/MRI alone and OctreoScan (99mTc-HYNIC-TOC); required for PRRT eligibility (Krenning score ≥3 = liver uptake intensity)
- IHC for SSTR2A: Antibody-based semiquantitative assessment in surgical/biopsy specimens; correlates with PET/CT

**Combination strategies:**
- SSA + everolimus: COOPERATE-2 (lanreotide + everolimus vs. lanreotide alone in pNET): PFS 16.7 vs 14.0 months (not significant); additive in practice for select patients
- SSA + PRRT sequencing: SSA for symptom control throughout; PRRT added for progressive disease; post-PRRT SSA maintenance common practice
- PRRT + radiosensitizer (NETTER-2 first-line): Ongoing evaluation in G2/G3 NETs

## Connections

- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Everolimus (mTOR inhibitor) is approved for SSTR2+ pancreatic NET (RADIANT-3: PFS 11.0 vs 4.6 months) and non-functional NET (RADIANT-4); SSA + everolimus combination provides additive antiproliferative effect via Gi-cAMP and mTOR dual suppression.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Sunitinib (VEGFR/PDGFR) is approved for pancreatic NET (PFS 11.4 vs 5.5 months); SSTR2 and VEGFR signaling are complementary targets in pNET; SSA + anti-VEGF combinations studied; bevacizumab active in midgut NET (SWOG S0518 trial).
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — NETs are highly vascularized; HIF-1α drives VEGF secretion in NET cells under hypoxia; everolimus (mTOR inhibitor) reduces HIF-1α → anti-angiogenic in pNET; HIF-1α pathway contributes to NET metastasis and resistance to SSA and PRRT.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Somatostatin (SSTR2 ligand) inhibits glucagon from pancreatic α-cells and insulin from β-cells; SSTR2 agonists (octreotide) control glucagonoma syndrome (necrolytic migratory erythema, diabetes); normal SSTR2 restrains glucagon in the inter-meal state.

[^rinke-2009-promid]: Rinke A, Müller HH, Schade-Brittinger C, et al. Placebo-controlled, double-blind, prospective, randomized study on the effect of octreotide LAR in the control of tumor growth in patients with metastatic neuroendocrine midgut tumors: a report from the PROMID Study Group. *J Clin Oncol.* 2009;27(28):4656-4663. [doi:10.1200/JCO.2009.22.8510](https://doi.org/10.1200/JCO.2009.22.8510) · [PubMed 19704057](https://pubmed.ncbi.nlm.nih.gov/19704057/)
[^strosberg-2017-netter1]: Strosberg J, El-Haddad G, Wolin E, et al. Phase 3 trial of 177Lu-DOTATATE for midgut neuroendocrine tumors. *N Engl J Med.* 2017;376(2):125-135. [doi:10.1056/NEJMoa1607427](https://doi.org/10.1056/NEJMoa1607427) · [PubMed 28076709](https://pubmed.ncbi.nlm.nih.gov/28076709/)
