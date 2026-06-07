---
schema: human-scale-entry/v1
id: ret
name: RET
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Receptor tyrosine kinase; point mutations (C634R in MEN2A, M918T in MEN2B) cause hereditary medullary thyroid carcinoma; RET/PTC fusions in papillary thyroid cancer. Selpercatinib and pralsetinib are approved RET inhibitors in RET-mutant MTC and RET fusion thyroid/NSCLC."
aliases: ["RET", "RET proto-oncogene", "RET kinase", "RET/PTC", "BCR-ABL-like RET", "GDNF receptor", "cadherin-related tyrosine kinase"]
sources:
  - id: wirth-2020-selpercatinib
    type: peer-reviewed
    cite: "Wirth LJ, Sherman E, Robinson B, et al. Efficacy of selpercatinib in RET-altered thyroid cancers. N Engl J Med. 2020;383(9):825-835."
    doi: "10.1056/NEJMoa2018485"
    pmid: "32846061"
    url: "https://doi.org/10.1056/NEJMoa2018485"
  - id: wells-2012-vandetanib
    type: peer-reviewed
    cite: "Wells SA Jr, Robinson BG, Gagel RF, et al. Vandetanib in patients with locally advanced or metastatic medullary thyroid cancer: a randomized, double-blind phase III trial. J Clin Oncol. 2012;30(2):134-141."
    doi: "10.1200/JCO.2011.35.5040"
    pmid: "22025146"
    url: "https://doi.org/10.1200/JCO.2011.35.5040"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RET → GRB2/SOS → RAS-MAPK → ERK → proliferation; RAS signaling is a major downstream RET effector; MEK inhibitors combined with RET TKIs in selpercatinib-resistant tumors; RET-fusion papillary thyroid cancer activates RAS through bridging adaptor proteins including IRS-1."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "RET → PI3K-AKT → mTOR → survival; mTOR pathway activated downstream of RET in medullary thyroid carcinoma; everolimus studied in combination with TKIs (cabozantinib, vandetanib) in RET-mutant MTC; PI3K-AKT-mTOR also mediates TKI resistance in RET-driven cancers."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Multi-kinase inhibitors that include RET inhibition also target VEGFR1-3 (lenvatinib, vandetanib, cabozantinib) → anti-angiogenic + anti-tumor effects; lenvatinib + pembrolizumab under study; thyroid cancer is highly vascular → VEGF axis is a co-driver of tumor progression."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "RET kinase activates STAT3 directly and via JAK2 → BCL-XL, MYC, and cyclin D1 → survival and proliferation in MTC; STAT3 phosphorylation is a pharmacodynamic marker of RET inhibition; STAT3 pathway activation is a resistance mechanism to selpercatinib in RET-mutant tumors."
---

# RET

## Overview

**RET (rearranged during transfection)** is a receptor tyrosine kinase encoded at chromosome 10q11.2 that normally mediates signals from **GDNF-family ligands** (GDNF, neurturin, artemin, persephin) through co-receptors (GFRα1-4) to promote neuronal survival, differentiation, and kidney development. RET is unique among RTKs in its cadherin-like extracellular domain and its role as the defining oncogene in thyroid cancer: germline *RET* point mutations cause hereditary **medullary thyroid carcinoma** (MEN2A, MEN2B, FMTC), while somatic *RET* fusions create the **RET/PTC** oncoproteins in papillary thyroid carcinoma [^wirth-2020-selpercatinib].

**RET in cancer:**
- **Medullary thyroid carcinoma (MTC):** Germline RET mutation → MEN2A (C634R/C611R → parafollicular C-cell MTC + parathyroid adenoma + pheochromocytoma) or MEN2B (M918T → most aggressive MTC, marfanoid habitus, mucosal neuromas); somatic RET M918T/C634F/etc. in sporadic MTC (~40%); RET-negative MTC rarely carries other drivers
- **Papillary thyroid carcinoma (PTC):** RET/PTC1 (RET-CCDC6 fusion) and RET/PTC3 (RET-NCOA4 fusion) in ~20% of PTC; younger patients; radiation-associated (post-Chernobyl PTC → high RET/PTC3 frequency); RET/PTC carries better prognosis than BRAF V600E PTC
- **Non-small cell lung cancer (NSCLC):** RET fusions in ~1-2% of lung adenocarcinoma (KIF5B-RET most common); enriched in never-smokers; selective RET inhibitors (selpercatinib, pralsetinib) first-line preferred over chemotherapy
- **Pancreatic ductal adenocarcinoma (PDAC):** RET fusions in ~0.5% — targetable but rare

**Selective vs. multi-kinase RET inhibition:**
First-generation multi-kinase inhibitors (vandetanib, cabozantinib) target RET plus VEGFR/MET/AXL — active in MTC but limited by off-target toxicity and modest potency against RET kinase domain mutations. Second-generation selective RET inhibitors (selpercatinib, pralsetinib) are 100-fold more selective for RET → superior tolerability and intracranial activity.

## Structure

### RET protein architecture

RET is a 1,114-amino-acid single-pass transmembrane RTK:

**Extracellular domain (ECD, 1-635):**
- **Cadherin-like domain (CLD1-4, 1-489):** Four tandem cadherin homology domains — unusual for RTKs; CLD1-2 bind GFRα co-receptors (which first bind GDNF) → RET homodimerization; CLD2 contains the critical **cysteine-rich region** where MEN2A mutations cluster (C634, C620, C618, C611) — cysteine substitutions → unpaired cysteine → constitutive intermolecular disulfide bridging → constitutive RET homodimerization without ligand → constitutive kinase activation
- **Cysteine-rich domain (CRD, 490-635):** Four cysteine pairs maintain tertiary structure; oncogenic cysteine substitutions in MEN2A disrupt one pair → free cysteine available for intermolecular disulfide

**Transmembrane domain (TM, 636-657):** Single helix

**Intracellular domain:**
- **Juxtamembrane domain (658-708):** Autophosphorylation and adaptor binding (Y981, Y1015, Y1062 phosphorylation sites)
- **Kinase domain (709-980):** Bilobal kinase fold; **M918** in the activation loop — MEN2B M918T alters substrate specificity of the kinase → constitutive activation + phosphorylation of novel substrates (higher transforming potential than MEN2A mutations); **"gatekeeper" residue V804** — V804M/L → resistance to vandetanib/cabozantinib/pralsetinib but selpercatinib retains activity
- **C-terminal tail (981-1114):** Regulatory; Tyr1062 → multifunction adaptor docking (SHC/IRS-1/GRB10) → PI3K-AKT + RAS-MAPK

### RET fusion oncoproteins

**Mechanism of RET fusions:**
Chromosomal rearrangements (inversions or translocations) fuse the 5' regulatory sequences and coiled-coil/dimerization domain of partner genes to the 3' kinase domain of RET:
- **RET/PTC1 (CCDC6-RET):** Inv(10)(q11q21); CCDC6 coiled-coil → constitutive dimerization → kinase activation; most common RET fusion (~70% of RET-fusion PTC)
- **RET/PTC3 (NCOA4-RET):** Inv(10)(q11q11); NCOA4 coiled-coil; associated with solid-variant PTC and radiation-induced PTC
- **KIF5B-RET:** Inv(10)(p11q11); most common in lung adenocarcinoma (~70% of RET fusion NSCLC)
- **CCDC6-RET** and **NCOA4-RET** also occur in NSCLC

All fusion partners provide: (1) a dimerization domain enabling constitutive kinase activation, and (2) cytoplasmic targeting (the fusion protein lacks RET's transmembrane domain → entirely cytoplasmic RTK).

## Function

### Normal RET signaling

**GDNF-GFRα-RET signaling:**
GDNF binds GFRα1 co-receptor → GDNF-GFRα1 complex recruits RET at the membrane → RET homodimerization → trans-autophosphorylation at Y905, Y981, Y1015, Y1062 → signaling cascades:
- **Y1062 (multifunction adaptor site):** SHC/IRS-1 → GRB2/SOS → RAS → ERK1/2 → proliferation; also IRS-1 → PI3K → AKT → mTOR → survival
- **Y981:** SRC → SRC-FAK → cell migration
- **Y1015:** PLCγ → PKC → transcription

**Physiological roles:**
- **Kidney development:** RET-GDNF signaling mediates ureteric bud branching → renal collecting duct formation; RET knockout → bilateral renal agenesis
- **Enteric nervous system:** RET → neural crest cell migration into gut → myenteric and submucosal plexus formation; RET loss-of-function → Hirschsprung disease (aganglionic megacolon)
- **Parasympathetic neurons:** RET-neurturin-GFRα2 → maintenance of cholinergic neurons

## Mechanism

### Oncogenic RET activation mechanisms

**Point mutations (MEN2):**
- MEN2A cysteine mutations (CLD2, residues 609-634): Constitutive disulfide-mediated homodimerization; oncogenicity proportional to position (C634 > C611 > C618)
- MEN2B M918T: Changes substrate specificity → hyperactivated kinase; accelerated disease onset (MTC by age 1-2 in untreated MEN2B); highest risk category per ATA guidelines → thyroidectomy in first 6 months of life

**Gatekeeper mutations (therapeutic resistance):**
V804M/L → steric clash with vandetanib/cabozantinib hinge-binding region → resistance; selpercatinib and pralsetinib are designed with smaller hinge moieties → retain activity against V804 mutants; compound V804M + Y806C → broader resistance, including selpercatinib

### Selective RET inhibitors

**Selpercatinib (LOXO-292, Retevmo):**
- Highly selective ATP-competitive RET inhibitor (selectivity ratio >100-fold vs. VEGFR, KIT, PDGFR)
- **LIBRETTO-001 trial:** [^wirth-2020-selpercatinib]
  - RET-mutant MTC (previously treated): ORR 69%, median DOR 20.3 months
  - RET-mutant MTC (treatment-naive): ORR 73%, DOR not reached at 14 months
  - RET fusion-positive thyroid cancer: ORR 79% (previously treated)
  - RET fusion-positive NSCLC: ORR 64% (TAXOTERE/platinum-naive), 85% (treatment-naive)
- Intracranial activity: confirmed CNS responses in RET fusion NSCLC with brain metastases
- FDA approved 2020 for RET fusion+ NSCLC, RET-mutant/fusion+ MTC, RET fusion+ thyroid cancer (any histology)
- Well-tolerated: hypertension (~35%), QTc prolongation (~17%), elevated AST/ALT (~35%), edema

**Pralsetinib (BLU-667, Gavreto):**
- Selective RET inhibitor; high potency including against V804M
- **ARROW trial:**
  - RET fusion+ NSCLC: ORR 70% (treatment-naive), 61% (platinum-pretreated)
  - RET-mutant MTC: ORR 60% (cabozantinib/vandetanib-pretreated)
- FDA approved 2020 (same day as selpercatinib) for RET fusion+ NSCLC and RET-mutant/fusion+ MTC
- Toxicity: neutropenia, hypertension, constipation, elevated LFTs

**First-generation (non-selective) RET inhibitors:** [^wells-2012-vandetanib]
- Vandetanib (Caprelsa): Multikinase (VEGFR2, EGFR, RET); approved for MTC (phase III ZETA trial → PFS 30.5 vs. 19.3 months); QTc prolongation is dose-limiting
- Cabozantinib (Cometriq): Multikinase (MET, VEGFR, RET, AXL, KIT); approved for MTC (EXAM trial → PFS 7.2 vs. 4.0 months); progressive disease after vandetanib; diarrhea, fatigue, HFSR are main toxicities

### RET germline testing and MEN2 surveillance

**Genotype-phenotype correlations (ATA risk stratification):**
- **Highest risk (HST):** M918T → prophylactic thyroidectomy within 6 months of birth
- **High risk (H):** C634F/R/S/W/Y, C609/611/618/620 → thyroidectomy by age 5
- **Moderate risk (MOD):** Other RET mutations → thyroidectomy by age 5-10 or based on calcitonin levels

**MEN2A surveillance:** Annual calcitonin, calcium/PTH (parathyroid), plasma metanephrines/urine catecholamines (pheochromocytoma); pheo must be resected before thyroid surgery to prevent hypertensive crisis

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RET → GRB2/SOS → RAS-MAPK → ERK → proliferation; RAS signaling is a major downstream RET effector; MEK inhibitors combined with RET TKIs in selpercatinib-resistant tumors; RET-fusion papillary thyroid cancer activates RAS through bridging adaptor proteins including IRS-1.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — RET → PI3K-AKT → mTOR → survival; mTOR pathway activated downstream of RET in medullary thyroid carcinoma; everolimus studied in combination with TKIs (cabozantinib, vandetanib) in RET-mutant MTC; PI3K-AKT-mTOR also mediates TKI resistance in RET-driven cancers.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Multi-kinase inhibitors that include RET inhibition also target VEGFR1-3 (lenvatinib, vandetanib, cabozantinib) → anti-angiogenic + anti-tumor effects; lenvatinib + pembrolizumab under study; thyroid cancer is highly vascular → VEGF axis is a co-driver of tumor progression.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — RET kinase activates STAT3 directly and via JAK2 → BCL-XL, MYC, and cyclin D1 → survival and proliferation in MTC; STAT3 phosphorylation is a pharmacodynamic marker of RET inhibition; STAT3 pathway activation is a resistance mechanism to selpercatinib in RET-mutant tumors.

[^wirth-2020-selpercatinib]: Wirth LJ, Sherman E, Robinson B, et al. Efficacy of selpercatinib in RET-altered thyroid cancers. *N Engl J Med.* 2020;383(9):825-835. [doi:10.1056/NEJMoa2018485](https://doi.org/10.1056/NEJMoa2018485) · [PubMed 32846061](https://pubmed.ncbi.nlm.nih.gov/32846061/)
[^wells-2012-vandetanib]: Wells SA Jr, Robinson BG, Gagel RF, et al. Vandetanib in patients with locally advanced or metastatic medullary thyroid cancer: a randomized, double-blind phase III trial. *J Clin Oncol.* 2012;30(2):134-141. [doi:10.1200/JCO.2011.35.5040](https://doi.org/10.1200/JCO.2011.35.5040) · [PubMed 22025146](https://pubmed.ncbi.nlm.nih.gov/22025146/)
