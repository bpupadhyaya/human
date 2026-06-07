---
schema: human-scale-entry/v1
id: idh1
name: IDH1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Metabolic enzyme; IDH1 R132H and IDH2 R172K neomorphic mutations produce D-2-hydroxyglutarate → TET2 and KDM inhibition → DNA hypermethylation (G-CIMP) and HIF stabilization. IDH mutations define grade 2-3 gliomas; ivosidenib (IDH1) and vorasidenib are approved inhibitors."
aliases: ["IDH1", "IDH2", "isocitrate dehydrogenase", "IDH R132H", "D-2-HG", "2-hydroxyglutarate", "IDH-mutant", "oncometabolite IDH"]
sources:
  - id: dang-2016-idh-review
    type: peer-reviewed
    cite: "Dang L, Yen K, Attar EC. IDH mutations in cancer and progress toward development of targeted therapeutics. Ann Oncol. 2016;27(4):599-608."
    doi: "10.1093/annonc/mdw013"
    pmid: "26819363"
    url: "https://doi.org/10.1093/annonc/mdw013"
  - id: mellinghoff-2023-indigo
    type: peer-reviewed
    cite: "Mellinghoff IK, van den Bent MJ, Blumenthal DT, et al. Vorasidenib in IDH1- or IDH2-mutant low-grade glioma. N Engl J Med. 2023;389(7):589-601."
    doi: "10.1056/NEJMoa2304194"
    pmid: "37272516"
    url: "https://doi.org/10.1056/NEJMoa2304194"
cross_links:
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "D-2-HG produced by IDH1 R132H inhibits PHD enzymes → HIF-1alpha hydroxylation impaired → HIF-1alpha stabilization → VEGF and glycolytic gene induction; HIF-1alpha-driven hypoxia response is constitutively active in IDH-mutant tumors independent of oxygen tension."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "IDH-mutant astrocytomas frequently carry TP53 co-mutations and ATRX loss (IDH/ATRX/TP53 triad defines WHO astrocytoma); IDH1 mutation is an early clonal event followed by TP53 — IDH-wt GBM has distinct p53 alteration profile (MDM2 amplification or CDKN2A deletion)."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "IDH-mutant gliomas have lower mTOR pathway activity than IDH-wt GBM; IDH-wt GBM → PTEN loss/EGFR amplification → PI3K-AKT-mTOR → growth and TKI resistance; mTOR inhibitors under investigation in GBM; IDH2-mutant AML also shows mTOR dependence targetable by rapamycin analogs."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "IDH mutation → 2-HG → HIF stabilization → VEGF transcription → tumor angiogenesis; IDH-mutant gliomas are less vascular than IDH-wt GBM despite VEGF induction; bevacizumab used in GBM (IDH-wt and IDH-mutant) but improves PFS without OS benefit in most settings."
---

# IDH1

## Overview

**IDH1 (isocitrate dehydrogenase 1)** and its mitochondrial paralogue **IDH2** are metabolic enzymes that catalyze the oxidative decarboxylation of isocitrate to α-ketoglutarate (α-KG) with NADPH production. Gain-of-function mutations in the active site — **IDH1 R132H** (by far the most common, >85% of IDH-mutant gliomas), **IDH2 R172K/M**, and **IDH2 R140Q** — confer a **neomorphic enzymatic activity**: instead of producing α-KG, they reduce α-KG to **D-2-hydroxyglutarate (D-2-HG)**, an oncometabolite that accumulates to millimolar concentrations and drives epigenetic reprogramming [^dang-2016-idh-review].

**IDH mutations in cancer:**
- **Diffuse glioma:** IDH1/2 mutations in ~70-80% of WHO grade 2-3 astrocytomas and oligodendrogliomas; IDH-wildtype defines glioblastoma (WHO grade 4) — IDH status is the primary molecular determinant of the WHO 2021 glioma classification
- **Acute myeloid leukemia (AML):** IDH1 mutations in ~8%, IDH2 in ~12%; frequently co-mutate with NPM1 and DNMT3A; IDH mutations are potential founder events in clonal hematopoiesis
- **Cholangiocarcinoma (intrahepatic):** IDH1 mutations in ~15-20%; ivosidenib approved for IDH1-mutant cholangiocarcinoma (ClarIDHy trial)
- **Chondrosarcoma:** IDH1/IDH2 mutations in >50%; typically hypermethylated
- **Myelodysplastic syndrome (MDS):** IDH1/2 mutations in ~5-10%

**The IDH/α-KG relationship:**
IDH mutations make cancer cells dependent on exogenous α-KG (or glutamine) to replenish α-KG consumed by the neomorphic reaction. This metabolic liability is currently being exploited by IDH inhibitors and glutaminase inhibitors in combination studies.

## Structure

### IDH1 protein (cytoplasmic)

IDH1 is a homodimer; each monomer is ~47 kDa:
- **Clasp domain:** Mediates homodimerization and the NADPH binding site
- **Large domain:** Contains the isocitrate binding pocket and the critical **R132** residue at the active site; isocitrate binds via ionic interactions with R132 — mutation to H/C/S/G disrupts isocitrate oxidation and allows α-KG reduction
- **Small domain:** Regulatory domain; undergoes conformational change (open→closed) upon substrate binding

**Wild-type catalysis:**
Isocitrate + NADP⁺ → α-KG + CO₂ + NADPH
- Provides NADPH for antioxidant defense (GSH regeneration)
- Provides α-KG for the TCA cycle and as a cofactor for α-KG-dependent dioxygenases

**Mutant R132H neomorphic catalysis:**
α-KG + NADPH → D-2-hydroxyglutarate (D-2-HG) + NADP⁺
- R132H active site cannot bind isocitrate → exclusively reduces α-KG
- Consumes NADPH → oxidative stress
- Produces D-2-HG → competitive inhibitor of α-KG-dependent enzymes

### IDH2 (mitochondrial paralogue)

IDH2 is a homodimer in the mitochondrial matrix; contributes isocitrate → α-KG flux to the TCA cycle. IDH2 mutations:
- **R172K/M/W/S:** ~60% of IDH2-mutant cancers; higher 2-HG production capacity than IDH1 R132H
- **R140Q:** ~40%; lower 2-HG production; frequently in AML with NPM1 co-mutation

IDH1 and IDH2 mutations are mutually exclusive (because both create 2-HG; dual mutation provides no additional advantage).

### D-2-hydroxyglutarate (2-HG) as oncometabolite

2-HG accumulates to 5-35 mM in IDH-mutant tumors (vs. <0.1 mM baseline):

**Epigenetic targets of 2-HG (α-KG-dependent enzymes inhibited):**
- **TET1/2/3 (5-methylcytosine hydroxylases):** TET2 inhibition → failure to demethylate CpGs → global DNA hypermethylation → **Glioma CpG Island Methylator Phenotype (G-CIMP)**; G-CIMP silences tumor suppressor genes and differentiation factors
- **KDM (KDM2A, KDM4A, KDM5A) histone demethylases:** Inhibition → H3K9me3 and H3K27me3 accumulation → chromatin compaction → transcriptional silencing; particularly important for HOX gene cluster silencing and differentiation block
- **EglN/PHD prolyl hydroxylases:** Inhibition → impaired HIF-1alpha hydroxylation → HIF-1alpha accumulation without hypoxia (pseudohypoxia)

**Metabolic effects:**
- NADPH consumption → increased ROS sensitivity
- α-KG depletion → impairs collagen prolyl hydroxylation → ECM abnormalities
- 2-HG inhibits ATP synthase at high concentrations → metabolic vulnerability

## Function

### Normal IDH1 physiology

**Cytoplasmic NADPH production:**
IDH1 is the primary cytoplasmic source of NADPH (together with G6PD). NADPH is required for: glutathione reduction (GSH/GSSG), fatty acid synthesis (via FASN), reductive carboxylation (reverse TCA) in hypoxia.

**Lipid synthesis and reductive carboxylation:**
In rapidly proliferating cells under hypoxia, IDH1 runs in reverse — consuming NADPH and incorporating CO₂ into α-KG to produce isocitrate, which feeds citrate synthesis for lipid biosynthesis. This "reductive carboxylation" mode is disrupted by R132H mutation.

### IDH mutations and differentiation block

IDH1/2 mutations → 2-HG → KDM inhibition → H3K9me3/H3K27me3 → silencing of differentiation-promoting transcription factors (GATA2, C/EBPα, etc.) → blocked differentiation; this is particularly important in AML, where IDH-mutant progenitors fail to differentiate into mature myeloid cells → blast accumulation.

**IDH inhibitors rescue differentiation:**
Ivosidenib/enasidenib treatment → 2-HG clearance → demethylation of differentiation gene promoters → blast maturation/differentiation → decreasing blast count (differentiation syndrome risk in first weeks of therapy — similar to ATRA in APL).

## Mechanism

### IDH in glioma classification (WHO 2021)

**IDH-mutant glioma:**
- Oligodendroglioma: IDH-mutant + 1p/19q codeletion (TERT promoter mutation, CIC/FUBP1 mutations); WHO grade 2-3
- Astrocytoma: IDH-mutant + ATRX loss + TP53 mutation (no 1p/19q codeletion); WHO grade 2-4
- IDH-mutant gliomas have substantially better prognosis than IDH-wt GBM at the same histological grade

**IDH-wildtype GBM:**
- IDH-wt + TERT promoter mutation + chromosome 7 gain/10 loss → classified as GBM regardless of histology
- Key alterations: EGFR amplification/EGFRvIII (~40%), PTEN deletion (~30%), CDKN2A deletion (~50%), TP53 mutation (~30%), NF1 mutation (~15%)
- Median OS ~15 months with maximal safe resection + temozolomide + RT + tumor treating fields

### IDH inhibitors

**Ivosidenib (AG-120, IDH1 inhibitor):**
- Active site inhibitor → reduces 2-HG production by ~90%
- **AML (IDH1-mutant, relapsed/refractory):** CR+CRh rate ~30%; approved 2018 (FDA)
- **Cholangiocarcinoma (IDH1-mutant):** PFS improvement vs. placebo (ClarIDHy trial); approved 2021
- Differentiation syndrome: 10-15% risk, especially in first 30 days

**Enasidenib (AG-221, IDH2 inhibitor):**
- Active site inhibitor; IDH2-specific
- **AML (IDH2-mutant, R/R):** CR+CRh ~20%; approved 2017 (first IDH inhibitor approval)

**Vorasidenib (IDH1/2 dual inhibitor):**
- Brain-penetrant (designed to cross BBB) → key for CNS disease
- **IDH-mutant grade 2 glioma (INDIGO trial):** PFS 27.7 months vs. 11.1 months with placebo; 61% reduction in risk of progression or death; FDA approved August 2024 — **first targeted therapy approved for IDH-mutant glioma** [^mellinghoff-2023-indigo]
- Ongoing trials in IDH-mutant grade 3 astrocytoma and oligodendroglioma

**Olutasidenib (FT-2102, IDH1 inhibitor):**
- Second IDH1 inhibitor; approved 2022 for IDH1-mutant R/R AML
- CR+CRh ~35%

## Connections

- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — D-2-HG produced by IDH1 R132H inhibits prolyl hydroxylase domain (PHD) enzymes → HIF-1alpha hydroxylation impaired → HIF-1alpha stabilization → VEGF and glycolytic gene induction; HIF-1alpha-driven hypoxia response is constitutively active in IDH-mutant tumors independent of oxygen tension.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — IDH-mutant astrocytomas frequently carry TP53 co-mutations and ATRX loss (IDH/ATRX/TP53 triad defines WHO astrocytoma); IDH1 mutation is an early clonal event followed by TP53 — IDH-wt GBM has distinct p53 alteration profile (MDM2 amplification or CDKN2A deletion rather than TP53 mutation).
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — IDH-mutant gliomas have lower mTOR pathway activity than IDH-wt GBM; IDH-wt GBM → PTEN loss/EGFR amplification → PI3K-AKT-mTOR → growth and TKI resistance; mTOR inhibitors under investigation in GBM; IDH2-mutant AML also shows mTOR dependence targetable by rapamycin analogs.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — IDH mutation → 2-HG → HIF stabilization → VEGF transcription → tumor angiogenesis; IDH-mutant gliomas are less vascular than IDH-wt GBM despite VEGF induction; bevacizumab used in GBM (IDH-wt and IDH-mutant) but improves PFS without OS benefit in most settings.

[^dang-2016-idh-review]: Dang L, Yen K, Attar EC. IDH mutations in cancer and progress toward development of targeted therapeutics. *Ann Oncol.* 2016;27(4):599-608. [doi:10.1093/annonc/mdw013](https://doi.org/10.1093/annonc/mdw013) · [PubMed 26819363](https://pubmed.ncbi.nlm.nih.gov/26819363/)
[^mellinghoff-2023-indigo]: Mellinghoff IK, van den Bent MJ, Blumenthal DT, et al. Vorasidenib in IDH1- or IDH2-mutant low-grade glioma. *N Engl J Med.* 2023;389(7):589-601. [doi:10.1056/NEJMoa2304194](https://doi.org/10.1056/NEJMoa2304194) · [PubMed 37272516](https://pubmed.ncbi.nlm.nih.gov/37272516/)
