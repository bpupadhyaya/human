---
schema: human-scale-entry/v1
id: sdhb
name: SDHB
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "SDHB is the iron-sulfur subunit of mitochondrial complex II; LOF → succinate → PHD inhibition → HIF-1α pseudohypoxia + TET inhibition → CIMP; germline SDHB causes paraganglioma type 4 (malignancy risk ~30-40%); SDH-deficient GIST/RCC are WHO entities."
aliases: ["SDHB", "succinate dehydrogenase B", "complex II", "SDH complex", "SDH-deficient GIST", "SDH-deficient RCC", "PGL4", "hereditary paraganglioma", "SDHB paraganglioma", "succinate dehydrogenase iron-sulfur"]
sources:
  - id: astuti-2001-sdhb-paraganglioma
    type: peer-reviewed
    cite: "Astuti D, Latif F, Dallol A, et al. Gene mutations in the succinate dehydrogenase subunit SDHB cause susceptibility to familial pheochromocytoma and to familial paraganglioma. Am J Hum Genet. 2001;69(1):49-54."
    doi: "10.1086/321282"
    pmid: "11404820"
    url: "https://doi.org/10.1086/321282"
  - id: selak-2005-succinate-hif
    type: peer-reviewed
    cite: "Selak MA, Armour SM, MacKenzie ED, et al. Succinate links TCA cycle dysfunction to oncogenesis by inhibiting HIF-α prolyl hydroxylase. Cancer Cell. 2005;7(1):77-85."
    doi: "10.1016/j.ccr.2004.11.022"
    pmid: "15652751"
    url: "https://doi.org/10.1016/j.ccr.2004.11.022"
cross_links:
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "SDH LOF → succinate accumulates → competitively inhibits PHD1/2/3 prolyl hydroxylases → HIF-1α Pro402/564 not hydroxylated → VHL E3 ligase cannot bind → HIF-1α escapes proteasomal degradation → pseudohypoxia; VHL-mutant tumors similarly stabilize HIF-1α via VHL LOF."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "SDH LOF → succinate → PHD inhibition → HIF-1α not hydroxylated → VHL cannot bind → HIF-1α nuclear → VEGF, GLUT1, LDHA, EPO transcription (pseudohypoxia); HIF-1α also activated by NF2/VHL loss → TEAD and HIF-1α share angiogenic targets in NF2-null meningioma and PHEO/PGL."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "SDH LOF → HIF-1α pseudohypoxia → VEGF-A transcription (HIF-1α binds VEGF promoter HRE) → tumor angiogenesis in PHEO/PGL and SDH-deficient GIST; bevacizumab (anti-VEGF) active in SDH-deficient GISTs; VEGF also secreted by chromaffin cells in response to catecholamine synthesis."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "SDH LOF → succinate accumulates → competitively inhibits TET1/2/3 (α-KG-dependent) → 5mC oxidation blocked → CpG DNA hypermethylation (CIMP); same excess succinate inhibits KDM histone demethylases → H3K27me3 accumulation; SDH-null tumors show genome-wide CIMP phenotype."
---

# SDHB

## Overview

**SDHB** (succinate dehydrogenase iron-sulfur subunit B) encodes the iron-sulfur protein subunit of **mitochondrial complex II** (succinate-coenzyme Q oxidoreductase, succinate dehydrogenase). The SDH complex catalyzes the oxidation of succinate to fumarate in the **TCA cycle** while simultaneously reducing ubiquinone (coenzyme Q) to ubiquinol in the **electron transport chain** — the only enzyme serving both pathways. SDHB is an obligate tumor suppressor: germline SDHB mutations cause hereditary pheochromocytoma/paraganglioma (PHEO/PGL) with the highest malignancy risk among all SDHx loci (~30-40%) [^astuti-2001-sdhb-paraganglioma], and somatic SDH complex loss defines WHO-recognized entities including SDH-deficient GIST and SDH-deficient renal cell carcinoma.

**SDHB germline mutations — hereditary paraganglioma:**
- **PGL4 syndrome (SDHB)**: chromosome 1p36; autosomal dominant; penetrance ~30-40%; PHEO (~10-15%) + sympathetic paraganglioma (abdominal, thoracic, pelvic) + head-neck PGL; malignancy risk ~30-40% (highest of all SDHx loci)
- **PGL1 syndrome (SDHD)**: chromosome 11q23; parasympathetic head-neck PGL predominant; paternally imprinted; malignancy risk <5%
- **PGL3 syndrome (SDHC)**: chromosome 1q23; head-neck PGL; low penetrance; malignancy rare
- **PGL5 syndrome (SDHA)**: chromosome 5p15; least penetrant (~7-10%); multiple tumor types including GIST

**SDH-deficient non-PHEO/PGL entities:**
- **SDH-deficient GIST**: pediatric gastric GIST; Carney triad (GIST + pulmonary chondroma + PHEO); Carney-Stratakis syndrome (germline SDHx + GIST + PGL); KIT/PDGFRA wild-type (imatinib-resistant); treatment: sunitinib, regorafenib; SDHB IHC loss
- **SDH-deficient RCC**: WHO 2022 entity; tubular architecture with vacuolated cytoplasm; most are low grade and stage; surveillance feasible for indolent cases; SDHB IHC shows complete loss of granular cytoplasmic staining
- **SDH-deficient pituitary adenoma (PitNET)**: rare; in Carney triad variant; SDHB IHC loss; screening warranted in SDHx carriers

## Structure

### SDH complex architecture

The succinate dehydrogenase complex is a heterotetrameric enzyme embedded in the inner mitochondrial membrane:

**SDHA (subunit A, ~73 kDa):**
Flavoprotein containing covalently linked FAD cofactor (His99); oxidizes succinate → fumarate (TCA cycle step 6); forms the catalytic head in the matrix; germline SDHA mutations → PHEO/PGL (PGL5) and pituitary adenoma; interfaces directly with SDHB

**SDHB (subunit B, ~31 kDa, 280 amino acids):**
Iron-sulfur protein with three Fe-S clusters arranged in tandem as an electron relay wire:
- **[2Fe-2S] cluster (S1)**: N-terminal; accepts electrons from SDHA/FADH₂; highest redox potential
- **[4Fe-4S] cluster (S2)**: middle; intermediate electron relay
- **[3Fe-4S] cluster (S3)**: C-terminal; lowest redox potential; transfers electrons to ubiquinone-binding pocket via SDHD

SDHB contacts SDHA on the matrix side and SDHC/SDHD on the membrane anchor side; the SDHB C-terminus borders the ubiquinone (CoQ) binding site

**SDHC/SDHD (subunits C/D, membrane anchors):**
Integral membrane proteins forming the ubiquinone-binding pocket; SDHD contains a heme b group; germline SDHC mutations → PGL3; SDHD mutations → PGL1 (paternally imprinted, head-neck PGL)

**SDHAF2 (assembly factor):**
Inserts FAD into SDHA; germline SDHAF2 mutations → PGL2 syndrome (rare); not a structural subunit

### Oncogenic succinate accumulation

SDHB biallelic LOF → SDH complex inactive → succinate cannot be oxidized → **succinate accumulates** in the mitochondrial matrix and cytoplasm (exported via mitochondrial dicarboxylate carrier):

**PHD inhibition (primary oncogenic driver):** [^selak-2005-succinate-hif]
Succinate competes with α-ketoglutarate (α-KG) at the active site of PHD1/2/3 (EglN1/2/3) prolyl hydroxylase enzymes → HIF-1α Pro402 and Pro564 not hydroxylated → VHL E3-RING ubiquitin ligase cannot recognize OHyP (hydroxyproline) → HIF-1α not polyubiquitinated → proteasomal degradation blocked → **pseudohypoxia** (HIF-1α nuclear despite normal oxygen tension)

**TET enzyme inhibition:**
The same excess succinate competitively inhibits TET1/2/3 (α-KG-dependent dioxygenases that oxidize 5-methylcytosine → 5-hydroxymethylcytosine) → 5mC oxidation blocked → CpG loci remain methylated → **CpG island methylator phenotype (CIMP)** in SDH-null tumors; CIMP silences tumor suppressors, differentiation genes, and imprinted loci

**KDM histone demethylase inhibition:**
Succinate also inhibits KDM5/KDM6 Jumonji-domain histone demethylases (also α-KG-dependent) → H3K27me3 and H3K9me3 accumulate → silencing of lineage-specific enhancers and differentiation loci → epigenetically enforced dedifferentiation in SDH-null chromaffin cells

## Function

### Normal SDH roles

**TCA cycle (step 6):**
Succinate (4C) + FAD → fumarate (4C) + FADH₂; ΔG ≈ −40 kJ/mol; the reaction is freely reversible under extreme succinate accumulation conditions; SDH is the only enzyme participating in both the TCA cycle and the ETC

**Electron transport chain:**
FADH₂ from SDHA → electrons conducted via Fe-S clusters of SDHB → ubiquinol (QH₂) at the SDHD ubiquinone pocket → QH₂ enters the respiratory chain at complex III; complex II does not pump protons directly (contrast with complexes I, III, IV); it contributes to ΔΨ via the ubiquinol pool

**ROS generation:**
Complex II is a secondary site of superoxide generation, particularly under reverse electron transport (succinate drives RET at complex I) → ROS contributes to oxidative stress in SDH-null cells and can directly stabilize HIF-1α (oxidation of HIF-1α Pro402 by ROS prevents PHD recognition paradoxically — only relevant under extreme succinate accumulation)

### SDH as tumor suppressor

SDHB LOF → combined succinate-mediated epigenetic reprogramming:
1. **Pseudohypoxia**: HIF-1α → VEGF, EPO, LDHA, GLUT1, Notch, PDGF → angiogenesis, glycolysis, cell survival
2. **CIMP**: TET inhibition → hypermethylation → silences CDKN2A (some SDH-deficient GISTs), HOX genes, differentiation loci
3. **H3K27me3/H3K9me3**: KDM inhibition → silences lineage-specific differentiation programs

This triple epigenetic mechanism explains why SDH-deficient tumors:
- Retain chromaffin cell identity (SSTR2 expression, norepinephrine transporter = MIBG-avid)
- Show globally hypermethylated DNA methylomes detectable by profiling
- Are KIT/PDGFRA wild-type (no kinase activation) yet hypervascular
- Express VEGF at levels similar to RCC (HIF-1α-driven)

## Mechanism

### SDHB IHC for universal tumor screening

SDHB immunohistochemistry (rabbit anti-SDHB antibody, granular mitochondrial cytoplasmic pattern) is the universal SDH-deficiency surrogate:
- **Normal (SDH-intact)**: granular brown cytoplasmic staining in all cells
- **SDH-deficient**: complete loss of granular cytoplasmic staining in tumor cells (endothelium, stroma retain staining as internal control)
- **Why SDHB IHC works for all SDHx**: when any SDH subunit (SDHB, SDHA, SDHC, or SDHD) is mutated, the entire complex is destabilized → SDHB protein lost from all SDH-deficient tumors regardless of which subunit is primarily mutated
- SDHB IHC recommended for ALL GIST, PHEO/PGL, chromophobe RCC, and pituitary adenoma → if lost, triggers germline SDHx testing

### Therapeutic targeting in SDH-deficient tumors

**Sunitinib (VEGFR/PDGFR/KIT inhibitor):**
SDH LOF → HIF-1α → VEGF → VEGFR2 → tumor angiogenesis; FIRSTMAPPP trial (Baudin 2021): first randomized placebo-controlled trial in progressive malignant PHEO/PGL; N=78; sunitinib vs placebo; PFS HR 0.50 (95% CI 0.28-0.88); 12-month PFS 35.9% vs 19.2%; standard of care for progressive metastatic PHEO/PGL

**177Lu-DOTATATE (lutetium PRRT):**
SDH-deficient PHEO/PGL retain SSTR2 expression; 68Ga-DOTATATE PET identifies PRRT-eligible patients; ORR ~25-30% from retrospective PHEO/PGL series; COMPETE trial ongoing

**Cabozantinib (VEGFR2/MET/RET/AXL):**
SDHB-mutant Cluster 1 tumors co-activate MET and AXL; Phase 2 data (NCT02302742): ORR ~15% in malignant PHEO/PGL

**131I-MIBG (Azedra, iobenguane I-131):**
SDH-deficient chromaffin cells retain NET (SLC6A2) → MIBG uptake; FDA-approved 2018 for iobenguane-avid unresectable PHEO/PGL; ORR ~25%; note: SDHB-mutant PHEO/PGL are frequently MIBG-negative → prefer 68Ga-DOTATATE PET for these patients

**Metabolic approaches (investigational):**
- α-KG supplementation: restores α-KG/succinate ratio → PHD reactivation → HIF-1α re-degradation (preclinical)
- HDAC inhibitors + EZH2 inhibitors: H3K27me3 accumulation in SDH-null tumors → chromatin derepression strategies in early preclinical studies

## Connections

- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — SDH LOF → succinate accumulates → competitively inhibits PHD1/2/3 prolyl hydroxylases → HIF-1α Pro402/564 not hydroxylated → VHL E3 ligase cannot bind → HIF-1α escapes proteasomal degradation → pseudohypoxia; VHL-mutant tumors similarly stabilize HIF-1α via VHL LOF.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — SDH LOF → succinate → PHD inhibition → HIF-1α not hydroxylated → VHL cannot bind → HIF-1α nuclear → VEGF, GLUT1, LDHA, EPO transcription (pseudohypoxia); HIF-1α also activated by NF2/VHL loss → TEAD and HIF-1α share angiogenic targets in NF2-null meningioma and PHEO/PGL.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — SDH LOF → HIF-1α pseudohypoxia → VEGF-A transcription (HIF-1α binds VEGF promoter HRE) → tumor angiogenesis in PHEO/PGL and SDH-deficient GIST; bevacizumab (anti-VEGF) active in SDH-deficient GISTs; VEGF also secreted by chromaffin cells in response to catecholamine synthesis.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — SDH LOF → succinate accumulates → competitively inhibits TET1/2/3 (α-KG-dependent) → 5mC oxidation blocked → CpG DNA hypermethylation (CIMP); same excess succinate inhibits KDM histone demethylases → H3K27me3 accumulation; SDH-null tumors show genome-wide CIMP phenotype.

[^astuti-2001-sdhb-paraganglioma]: Astuti D, Latif F, Dallol A, et al. Gene mutations in the succinate dehydrogenase subunit SDHB cause susceptibility to familial pheochromocytoma and to familial paraganglioma. *Am J Hum Genet.* 2001;69(1):49-54. [doi:10.1086/321282](https://doi.org/10.1086/321282) · [PubMed 11404820](https://pubmed.ncbi.nlm.nih.gov/11404820/)
[^selak-2005-succinate-hif]: Selak MA, Armour SM, MacKenzie ED, et al. Succinate links TCA cycle dysfunction to oncogenesis by inhibiting HIF-α prolyl hydroxylase. *Cancer Cell.* 2005;7(1):77-85. [doi:10.1016/j.ccr.2004.11.022](https://doi.org/10.1016/j.ccr.2004.11.022) · [PubMed 15652751](https://pubmed.ncbi.nlm.nih.gov/15652751/)
