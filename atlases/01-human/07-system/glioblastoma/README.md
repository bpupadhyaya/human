---
schema: human-scale-entry/v1
id: glioblastoma
name: Glioblastoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most aggressive primary brain tumor; IDH-wildtype GBM has EGFRvIII amplification (~40%), PTEN loss (~30%), and TERT promoter mutations. Temozolomide + radiotherapy is standard; tumor-treating fields (TTFields) improve OS; MGMT promoter methylation predicts temozolomide benefit."
aliases: ["GBM", "glioblastoma multiforme", "WHO grade 4 glioma", "IDH-wildtype glioblastoma", "GBM IDH-wt", "high-grade glioma"]
sources:
  - id: stupp-2005-temozolomide
    type: peer-reviewed
    cite: "Stupp R, Mason WP, van den Bent MJ, et al. Radiotherapy plus concomitant and adjuvant temozolomide for glioblastoma. N Engl J Med. 2005;352(10):987-996."
    doi: "10.1056/NEJMoa043330"
    pmid: "15758009"
    url: "https://doi.org/10.1056/NEJMoa043330"
  - id: chinot-2014-bevacizumab
    type: peer-reviewed
    cite: "Chinot OL, Wick W, Mason W, et al. Bevacizumab plus radiotherapy-temozolomide for newly diagnosed glioblastoma. N Engl J Med. 2014;370(8):709-722."
    doi: "10.1056/NEJMoa1308345"
    pmid: "24552318"
    url: "https://doi.org/10.1056/NEJMoa1308345"
cross_links:
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFRvIII (exons 2-7 deletion) is amplified in ~40% of IDH-wt GBM → constitutive EGFR signaling without ligand; EGFR inhibitors ineffective in GBM due to PTEN co-deletion and lack of kinase domain mutation; EGFRvIII-targeted therapies (depatux-m, AMG 596 BiTE) under investigation."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN deletion in ~30-40% of GBM → unrestrained PI3K-AKT-mTOR → proliferation and survival; PTEN/EGFRvIII co-occurrence → RTK-independent PI3K activation; PTEN loss is a major driver of EGFR-targeted therapy resistance in GBM; PI3K inhibitors under clinical investigation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "GBM is among the most angiogenic solid tumors; intratumoral hypoxia → HIF-1alpha → VEGF, PDGF, and SDF-1 → neovascularization and invasion; bevacizumab (anti-VEGF) improves PFS but not OS in newly diagnosed or recurrent GBM; HIF-1alpha also drives GBM stem cell self-renewal."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations in ~85% of IDH-wt GBM and ~90% of oligodendrogliomas → telomere maintenance → replicative immortality; TERT promoter mutation is a diagnostic criterion for IDH-wt GBM in WHO 2021; G-CIMP-positive IDH-mutant gliomas have TERT mutations via separate pathway."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH-wildtype GBM is defined by IDH-WT; IDH-mutant gliomas (grades 2-4) are distinct entities with better prognosis; vorasidenib (IDH1/2 inhibitor) approved 2024 for grade 2 IDH-mutant glioma (INDIGO trial: 27.7 vs 11.1 months PFS); IDH1 IHC distinguishes IDH-mutant from wt GBM."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 mutations in ~15% of GBM define the mesenchymal subtype; NF1 LOF → constitutive RAS-GTP → RAF-MEK-ERK → GBM invasion; NF1-mutant GBM has highest macrophage/microglia infiltration; MEK inhibitors (selumetinib, cobimetinib) under investigation in NF1-mutant recurrent GBM."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "GBM is highly angiogenic; hypoxia → HIF-1α → VEGF → neovascularization; bevacizumab (anti-VEGF) approved for recurrent GBM (2009): improves PFS and reduces edema/steroid use but no OS benefit; bevacizumab+lomustine no better than lomustine alone (EORTC 26101)."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "Glioblastoma and H3K27M diffuse midline glioma are both WHO grade 4 gliomas but molecularly opposite: GBM is the adult hemispheric tumor driven by EGFR/TERT/PTEN, DMG the pediatric midline tumor driven by an epigenetic H3K27M mutation — ONC201 helps DMG, bevacizumab helps GBM."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Glioblastoma is the most aggressive primary brain tumor, infiltrating along white-matter tracts so diffusely that even gross-total resection leaves cells behind, guaranteeing recurrence; the blood-brain barrier blocks most systemic drugs, capping median survival near 15 months."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Up to a third to half of glioblastoma's mass is tumor-associated macrophages and microglia recruited by tumor chemokines; rather than attacking, they are reprogrammed to an immunosuppressive state promoting invasion and angiogenesis, a key reason immunotherapy has failed in GBM."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Glioblastoma is the malignant endpoint of the astrocytic lineage: it arises from astrocytes or their progenitors, retaining GFAP expression, and reactive astrocytes at the tumor margin help build the invasive, pro-tumor microenvironment."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Glioblastoma is defined molecularly against IDH-mutant glioma: true GBM is IDH-wildtype with TERT-promoter mutation, EGFR amplification and +7/-10, carrying the worst prognosis, whereas IDH-mutant astrocytomas are a separate, better-prognosis entity—so IDH status now defines GBM."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Glioblastoma and meningioma are the two commonest primary brain tumors but opposite in nature: GBM is intra-axial, diffusely infiltrative and malignant, while meningioma is extra-axial, usually benign and dural-based, so resectable—distinguished on MRI by location and dural tail."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is a pillar of glioblastoma care: after maximal safe resection, fractionated radiation with concurrent temozolomide (the Stupp protocol) extends survival, yet the tumor inevitably recurs in the irradiated field—radiation delays but cannot cure GBM."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Glioblastoma wires itself into neural circuits: tumor cells form glutamatergic synapses with neurons and interconnect through gap junctions, so neuronal activity drives proliferation—a discovery making synaptic signaling a therapeutic target in this lethal brain cancer."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Glioblastoma is part of the Li-Fraumeni cancer spectrum: germline TP53 loss predisposes to gliomas, and somatic TP53 mutation is a defining alteration in many GBMs—both show how losing p53, the genome's guardian, helps spawn this aggressive tumor."
---

# Glioblastoma

## Overview

**Glioblastoma (GBM)** is the most common and lethal primary brain tumor in adults, classified as **WHO grade 4 glioma**. Under the WHO 2021 CNS tumor classification, glioblastoma is defined as an **IDH-wildtype astrocytic glioma** bearing at least one of: EGFR amplification, TERT promoter mutation, or chromosome 7 gain/10 loss — regardless of histological grade (a histologically grade 2-3 astrocytoma with these molecular features is classified as GBM). This molecular definition replaced the prior histology-only classification and substantially changed clinical trial design and patient prognostication [^stupp-2005-temozolomide].

**Epidemiology:**
- Incidence: ~3.2/100,000 per year; ~15,000 new cases/year in the United States
- Median age at diagnosis: ~64 years; rare before age 40
- Slight male predominance (M:F ~1.6:1)
- Median OS: ~15-17 months with standard treatment (Stupp protocol + TTFields)
- 2-year OS: ~25-30%; 5-year OS: ~5-10%
- No established environmental risk factors; prior cranial irradiation is the only known risk factor

**GBM subtypes (TCGA molecular classification):**
- **Proneural:** IDH-mutant (now reclassified) or IDH-wt with PDGFRA amplification; G-CIMP subtype
- **Classical:** EGFR amplification; RB1 loss; CDKN2A deletion; most common subtype
- **Mesenchymal:** NF1 mutation; CHI3L1/YKL-40 high; MET amplification; associated with higher macrophage infiltration; worst prognosis
- **Neural:** (largely invalidated by subsequent deconvolution studies — contaminating normal neurons)

## Structure

### Tumor architecture and heterogeneity

**Intratumoral heterogeneity:**
GBM is defined by extreme intra- and inter-tumoral heterogeneity. Single-cell RNA sequencing reveals four cellular states within a single tumor:
- **Mesenchymal-like (MES):** High invasive capacity; NF1 mutations; hypoxia-driven; resilient to therapy
- **Neural progenitor-like (NPC):** Sox2+; cycling; TCA-cycle dependent
- **Oligodendrocyte progenitor-like (OPC):** Intermediate proliferative
- **Astrocyte-like (AC):** EGFR-high; quiescent; CDK4 amplification

GBM stem cells (GSCs) cycle between states — particularly from AC/NPC → MES under hypoxia or therapy pressure — explaining therapeutic resistance and recurrence.

**Anatomical compartments:**
- **Enhancing tumor core:** Contrast-enhancing on MRI; necrotic center (pseudopalisading necrosis); active proliferating tumor cells; well-vascularized (VEGF-driven)
- **Non-enhancing infiltrating tumor:** T2/FLAIR abnormality beyond the enhancing rim; diffusely infiltrating GBM cells along white matter tracts → cannot be surgically resected; source of almost all recurrences
- **Perivascular niche:** GSCs reside adjacent to blood vessels; CXCL12/CXCR4 axis maintains GSC niche

### Molecular architecture

**Core GBM driver alterations:**

| Alteration | Frequency | Pathway | Therapeutic Implication |
|------------|-----------|---------|------------------------|
| EGFR amplification | ~40% | RTK → RAS/PI3K | TKIs ineffective; EGFRvIII bispecifics |
| EGFRvIII mutation | ~25% | Constitutive RTK | Vaccine (DCVax-L), bispecifics |
| PTEN deletion | ~30% | PI3K-AKT-mTOR | PI3K inhibitors under study |
| CDKN2A/B deletion | ~50% | CDK4/6-RB | CDK4/6 inhibitors + RT |
| TERT promoter | ~85% | Telomere | No direct target yet |
| TP53 mutation | ~30% | DNA damage | MDM2 inhibitors in study |
| NF1 mutation | ~15% | RAS-MAPK | MEK inhibitors investigated |
| MDM2 amplification | ~15% | p53 suppression | MDM2 inhibitors |
| CDK4 amplification | ~15% | CDK4-RB | CDK4/6 inhibitors |
| PDGFRA amplification | ~10% | RTK/proneural | PDGFR TKIs (limited benefit) |

**MGMT methylation:**
- MGMT (O⁶-methylguanine-DNA methyltransferase) repairs the DNA alkylation caused by temozolomide
- **MGMT promoter methylation** (~40-50% of GBM) silences MGMT expression → reduced DNA repair capacity → 3-4x improved response to temozolomide; methylated tumors have ~23 months median OS vs. ~12.6 months in unmethylated [^stupp-2005-temozolomide]
- MGMT status is assessed by pyrosequencing or methylation-specific PCR; not yet FDA-approved as a companion diagnostic but routinely used in clinical practice

## Function

### Normal glial biology

**Astrocytes (GBM precursor cell type):**
- Provide metabolic support (lactate shuttle, glutamate clearance) for neurons
- Maintain blood-brain barrier
- Respond to injury via reactive astrogliosis (GFAP upregulation)

GBM likely arises from neural stem cells or oligodendrocyte precursor cells (OPCs) rather than mature astrocytes, based on cellular state analysis. IDH-mutant gliomas arise at an earlier, more differentiated progenitor state.

### BBB and immunological sanctuary

The blood-brain barrier (BBB) creates a pharmacological challenge:
- Large molecule drugs (antibodies, ADCs) have minimal BBB penetration
- Temozolomide is a rare alkylating agent with >90% oral bioavailability and good CNS penetration
- Bevacizumab reduces contrast enhancement (BBB disruption) but does not effectively penetrate beyond the non-enhancing infiltrating tumor
- Immunological isolation: brain has reduced lymphocyte trafficking (no lymphatics in parenchyma); GBM exploits this → profound immunosuppression; PD-L1 expression + TGF-beta and IDO secretion by tumor → T cell exclusion

## Pathology

### Histological features

**Pseudopalisading necrosis:** Characteristic GBM hallmark; cells arrayed around necrotic foci in a radiating pattern; driven by hypoxia (necrotic zone) → HIF-1alpha → MES transition → migration away from necrosis → creates moving wave of invasion; area between necrosis and pseudopalisade is maximally hypoxic

**Microvascular proliferation:** Glomeruloid vascular tufts → result of VEGF/PDGFR-B-driven angiogenesis; another WHO diagnostic criterion for grade 4; not seen in grade 2-3 gliomas

**Mitotic activity:** High Ki-67/MIB-1 index (often >20%); numerous mitoses

### Recurrence and progression

**Pattern of recurrence:**
- ~90% recur within 2 cm of the original tumor margin (non-enhancing infiltrating cells)
- True distant recurrence is rare in IDH-wt GBM (vs. IDH-mutant gliomas which can occasionally disseminate via CSF)
- Recurrence is nearly universal despite treatment; median time to progression ~7 months

**Resistance mechanisms:**
- GSC state transition (AC/NPC → MES) under temozolomide pressure
- MGMT upregulation (acquired from unmethylated subclone outgrowth)
- PI3K-AKT-mTOR upregulation after EGFR-targeted therapy
- Hypermutation phenotype in patients treated with prolonged temozolomide (~20% of recurrent GBM)

### Treatment

**Standard frontline (Stupp protocol, 2005):**
1. Maximal safe surgical resection (goal: >95% gross total resection if achievable)
2. Concomitant temozolomide (75 mg/m²/day) + focal radiotherapy (60 Gy in 30 fractions)
3. Adjuvant temozolomide (150-200 mg/m² × 5 days, 28-day cycles × 6 cycles)
4. **+ Tumor-treating fields (TTFields, Optune device):** Alternating electric fields 200 kHz → disrupt mitotic spindle → cell death; EF14 trial → OS 20.9 vs. 16.0 months (Stupp 2017); now standard of care with temozolomide

**Bevacizumab (anti-VEGF):**
- FDA-approved for recurrent GBM (accelerated approval, 2009)
- RTOG 0825 and AVAglio trials: no OS benefit in newly diagnosed GBM despite PFS improvement [^chinot-2014-bevacizumab]
- Reduces corticosteroid requirement; palliative benefit; shrinks contrast enhancement (pseudoresponse pitfall)

**Recurrent GBM:**
- No universally effective standard; options: bevacizumab, lomustine (CCNU), re-irradiation, temozolomide re-challenge (if MGMT methylated + hypermutation-free), clinical trial
- Lomustine + bevacizumab: EORTC 26101 — OS 9.1 vs. 8.6 months (no benefit)

**Immunotherapy (disappointing to date):**
- Pembrolizumab (CheckMate 143, Keynote-028): no significant benefit in recurrent GBM
- DCVax-L (autologous dendritic cell vaccine loaded with tumor lysate): phase 3 showed 19.3 months OS vs. 16.5 months for placebo in newly diagnosed GBM; FDA approved 2023 (accelerated approval)
- EGFRvIII CAR-T, bispecifics, oncolytic virus (DNX-2401): active early-phase studies

**IDH-mutant grade 2 glioma:**
- Vorasidenib (IDH1/2 inhibitor): INDIGO trial → 27.7 vs. 11.1 months PFS; approved 2024; watch-and-wait alternative to RT/chemo in select low-grade IDH-mutant glioma

## Connections

- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFRvIII (exons 2-7 deletion) is amplified in ~40% of IDH-wt GBM → constitutive EGFR signaling without ligand; EGFR inhibitors ineffective in GBM due to PTEN co-deletion and lack of kinase domain mutation; EGFRvIII-targeted therapies (depatux-m, AMG 596 BiTE) under investigation.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN deletion in ~30-40% of GBM → unrestrained PI3K-AKT-mTOR → proliferation and survival; PTEN loss co-occurs with EGFRvIII → redundant RTK-independent PI3K activation; PTEN loss is a major driver of EGFR-targeted therapy resistance in GBM; PI3K inhibitors under clinical investigation.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — GBM is among the most angiogenic solid tumors; intratumoral hypoxia → HIF-1alpha → VEGF, PDGF, and SDF-1 → neovascularization and invasion; bevacizumab (anti-VEGF) improves PFS but not OS in newly diagnosed or recurrent GBM; HIF-1alpha also drives GBM stem cell self-renewal.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations (C228T, C250T) in ~85% of IDH-wt GBM and ~90% of oligodendrogliomas → telomere maintenance → replicative immortality; TERT promoter mutation is a diagnostic criterion for IDH-wt GBM in WHO 2021; G-CIMP-positive IDH-mutant gliomas have TERT mutations via separate pathway.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH-wildtype GBM is defined by IDH-WT; IDH-mutant gliomas (grades 2-4) are distinct entities with better prognosis; vorasidenib (IDH1/2 inhibitor) approved 2024 for grade 2 IDH-mutant glioma (INDIGO trial: 27.7 vs 11.1 months PFS); IDH1 IHC distinguishes IDH-mutant from wt GBM.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 mutations in ~15% of GBM define the mesenchymal subtype; NF1 LOF → constitutive RAS-GTP → RAF-MEK-ERK → GBM invasion; NF1-mutant GBM has highest macrophage/microglia infiltration; MEK inhibitors (selumetinib, cobimetinib) under investigation in NF1-mutant recurrent GBM.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — GBM is highly angiogenic; hypoxia → HIF-1α → VEGF → neovascularization; bevacizumab (anti-VEGF) approved for recurrent GBM (2009): improves PFS and reduces edema/steroid use but no OS benefit; bevacizumab+lomustine no better than lomustine alone (EORTC 26101).
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — Glioblastoma and H3K27M diffuse midline glioma are both WHO grade 4 gliomas but molecularly opposite: GBM is the adult hemispheric tumor driven by EGFR/TERT/PTEN, DMG the pediatric midline tumor driven by an epigenetic H3K27M mutation — ONC201 helps DMG, bevacizumab helps GBM.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Glioblastoma is the most aggressive primary brain tumor, infiltrating along white-matter tracts so diffusely that even gross-total resection leaves cells behind, guaranteeing recurrence; the blood-brain barrier blocks most systemic drugs, capping median survival near 15 months.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Up to a third to half of glioblastoma's mass is tumor-associated macrophages and microglia recruited by tumor chemokines; rather than attacking, they are reprogrammed to an immunosuppressive state promoting invasion and angiogenesis, a key reason immunotherapy has failed in GBM.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Glioblastoma is the malignant endpoint of the astrocytic lineage: it arises from astrocytes or their progenitors, retaining GFAP expression, and reactive astrocytes at the tumor margin help build the invasive, pro-tumor microenvironment.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Glioblastoma is defined molecularly against IDH-mutant glioma: true GBM is IDH-wildtype with TERT-promoter mutation, EGFR amplification and +7/-10, carrying the worst prognosis, whereas IDH-mutant astrocytomas are a separate, better-prognosis entity—so IDH status now defines GBM.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Glioblastoma and meningioma are the two commonest primary brain tumors but opposite in nature: GBM is intra-axial, diffusely infiltrative and malignant, while meningioma is extra-axial, usually benign and dural-based, so resectable—distinguished on MRI by location and dural tail.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is a pillar of glioblastoma care: after maximal safe resection, fractionated radiation with concurrent temozolomide (the Stupp protocol) extends survival, yet the tumor inevitably recurs in the irradiated field—radiation delays but cannot cure GBM.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Glioblastoma wires itself into neural circuits: tumor cells form glutamatergic synapses with neurons and interconnect through gap junctions, so neuronal activity drives proliferation—a discovery making synaptic signaling a therapeutic target in this lethal brain cancer.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Glioblastoma is part of the Li-Fraumeni cancer spectrum: germline TP53 loss predisposes to gliomas, and somatic TP53 mutation is a defining alteration in many GBMs—both show how losing p53, the genome's guardian, helps spawn this aggressive tumor.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stupp-2005-temozolomide]: Stupp R, Mason WP, van den Bent MJ, et al. Radiotherapy plus concomitant and adjuvant temozolomide for glioblastoma. *N Engl J Med.* 2005;352(10):987-996. [doi:10.1056/NEJMoa043330](https://doi.org/10.1056/NEJMoa043330) · [PubMed 15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/)
[^chinot-2014-bevacizumab]: Chinot OL, Wick W, Mason W, et al. Bevacizumab plus radiotherapy-temozolomide for newly diagnosed glioblastoma. *N Engl J Med.* 2014;370(8):709-722. [doi:10.1056/NEJMoa1308345](https://doi.org/10.1056/NEJMoa1308345) · [PubMed 24552318](https://pubmed.ncbi.nlm.nih.gov/24552318/)
