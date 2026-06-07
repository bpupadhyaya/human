---
schema: human-scale-entry/v1
id: vhl-disease
name: VHL Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary VHL disease is caused by germline VHL mutations; clear cell RCC, CNS and retinal hemangioblastomas, pheochromocytoma (type 2), and pancreatic NETs; belzutifan (HIF-2α inhibitor) is FDA-approved for VHL-related tumors; type 1/2A/2B/2C classification by pheo risk."
aliases: ["VHL disease", "von Hippel-Lindau disease", "VHL syndrome", "VHL hemangioblastoma", "VHL RCC", "hereditary VHL", "VHL pheochromocytoma", "VHL belzutifan", "von Hippel-Lindau syndrome"]
sources:
  - id: lonser-2003-vhl-disease
    type: peer-reviewed
    cite: "Lonser RR, Glenn GM, Walther M, et al. von Hippel-Lindau disease. Lancet. 2003;361(9374):2059-2067."
    doi: "10.1016/S0140-6736(03)13643-4"
    pmid: "12814730"
    url: "https://doi.org/10.1016/S0140-6736(03)13643-4"
  - id: choueiri-2020-hif2-rcc
    type: peer-reviewed
    cite: "Choueiri TK, Kaelin WG Jr. Targeting the HIF2-VEGF axis in renal cell carcinoma. Nat Med. 2020;26(10):1519-1530."
    doi: "10.1038/s41591-020-1093-z"
    pmid: "33020650"
    url: "https://doi.org/10.1038/s41591-020-1093-z"
cross_links:
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "Germline VHL LOF causes VHL disease via constitutive HIF-1α/2α accumulation; VHL β-domain recognizes EGLN1-hydroxylated HIF → ubiquitination; missense VHL variants predict pheo risk (type 2A/2B/2C) vs truncating (type 1, high RCC); belzutifan targets HIF-2α downstream."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "EGLN1 (PHD2) hydroxylates HIF-1α/2α under normoxia for VHL-mediated degradation; in VHL disease, VHL LOF renders HIF constitutively stable regardless of EGLN1 activity; EGLN1 inhibitors (PHD inhibitors) activate HIF for CKD anemia treatment by the same mechanism as VHL LOF."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Clear cell RCC (ccRCC) is the most common VHL disease tumor (~25-45% lifetime risk); VHL LOF → HIF-2α/VEGF → neovascularization → ccRCC; NSS (nephron-sparing surgery) for ≤3 cm tumors; belzutifan (HIF-2α inhibitor) FDA-approved for VHL disease-associated ccRCC since 2021."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "VHL disease type 2 (missense variants) carries pheochromocytoma risk (~8-20%); VHL pheo is typically bilateral, benign, adrenal, and normetanephrine-secreting; VHL-pheo driven by HIF-2α pseudohypoxia → catecholamine biosynthesis upregulation; resection curative."
---

# VHL Disease

## Overview

**VHL disease** (von Hippel-Lindau disease) is an autosomal dominant hereditary cancer predisposition syndrome caused by germline pathogenic variants in the **VHL** tumor suppressor gene (chromosome 3p25.3; 3 exons; encodes 213 aa pVHL). VHL disease is characterized by a predisposition to a distinctive set of hypervascular tumors and cysts including **hemangioblastomas** of the CNS (cerebellum, spinal cord, brainstem) and retina, **clear cell renal cell carcinoma (ccRCC)**, **pheochromocytoma** (in type 2 VHL), **pancreatic serous cystadenomas and neuroendocrine tumors (pNET)**, and **endolymphatic sac tumors (ELST)**. The molecular basis is loss of pVHL function → constitutive HIF-1α/2α accumulation → HIF target gene overexpression (VEGF, EPO, PDGF, GLUT1) driving the highly vascularized tumor phenotype. VHL disease affects approximately **1 in 36,000** individuals, with a new mutation rate of ~20%. The 2021 FDA approval of **belzutifan** — the first HIF-2α inhibitor — for treatment of VHL disease-related tumors represents a paradigm shift from surgical to targeted medical management [^lonser-2003-vhl-disease] [^choueiri-2020-hif2-rcc].

**VHL disease type classification (genotype-phenotype):**

| Type | VHL mutation | Pheochromocytoma | CNS hemangioblastoma | ccRCC | Key notes |
|---|---|---|---|---|---|
| Type 1 | Truncating (nonsense, frameshift, deletion) | No (<1%) | Yes | Yes (high risk ~45%) | Most common; no pheo; high RCC |
| Type 2A | Missense (C162F, V166A, etc.) | Yes | Yes | No/low | Pheo + hemangioblastoma; low RCC |
| Type 2B | Missense (R167Q, L188V, W117R) | Yes | Yes | Yes | Pheo + RCC + hemangioblastoma; worst |
| Type 2C | Missense (L188V some, others) | Yes only | No/minimal | No | Pheo only; rare subtype |

The genotype-phenotype correlation reflects the degree of pVHL function retained: truncating variants = complete LOF = no VHL function = type 1; certain missense variants retain some VHL function in non-pheochromocytoma contexts but specifically impair pVHL interaction with a different substrate that suppresses catecholamine synthesis → pheo risk.

## Structure

### Genetic basis

**VHL gene (3p25.3):**
- 3 exons; 213 aa (pVHL30, cytoplasmic/nuclear) and a shorter isoform (pVHL19, 160 aa) initiated from internal Met; both functional
- Germline pathogenic variant spectrum: missense (~45%), nonsense (~25%), frameshift (~18%), partial deletions (~11%; MLPA required), splice (~1%), complete gene deletion (<1%)
- Penetrance: ~97% lifetime penetrance for at least one VHL manifestation by age 65 (essentially complete)
- De novo rate: ~20% of VHL disease; test parents of a proband
- Somatic second hit: LOH at 3p25 detectable in >90% of VHL-associated tumors; somatic promoter methylation as alternative second hit in sporadic ccRCC (~10%)

**pVHL structure:**
- pVHL contains an **α-domain** (scaffold domain) and a **β-domain** (hydroxyproline-binding substrate recognition domain)
- β-domain: forms a deep hydrophobic pocket that accommodates the LXXLAP-OH (hydroxyproline) motif of HIF-α; Tyr98, His115 and other residues in the pocket contact the hydroxyproline directly
- α-domain: binds Elongin C (ELOC) → ELOC-ELOB-CUL2-RBX1 assembled into the E3 ubiquitin ligase complex → RING domain (RBX1) activates E2 ubiquitin-conjugating enzyme → HIF-α poly-ubiquitination → 26S proteasome degradation
- pVHL has functions beyond HIF degradation: stabilizes microtubules, regulates primary ciliogenesis, modulates fibronectin matrix assembly, promotes differentiation of renal tubular epithelium — many of these contribute to tumor suppression beyond HIF pathway

**Somatic VHL in sporadic ccRCC:**
- VHL somatic biallelic inactivation in ~90% of sporadic clear cell RCC; most common mechanism: one allele lost by LOH at 3p, second allele mutated or methylated
- Sporadic ccRCC VHL mutations: same types as germline but both hits are somatic; no other VHL disease features in sporadic VHL-mutant RCC patients

## Function

### CNS and retinal hemangioblastomas

**Hemangioblastoma biology:**
- Highly vascularized cystic tumors with a mural nodule; the cyst wall is benign but the nodule contains the actual neoplastic stromal cells (pVHL-LOH confirmed in stromal cells)
- Cell of origin debated: hemangioblast (primitive vascular progenitor) vs neural/glial progenitor; gene expression profiling suggests embryonic mesodermal origin
- VHL LOF in stromal cells → HIF-2α/EPAS1 stabilization → massive VEGF overexpression → recruitment of surrounding vasculature → the characteristic hemangioblastoma blood vessel-rich cystic structure
- HIF-2α appears to be the dominant HIF isoform in hemangioblastoma stromal cells (unlike other VHL-related tumors where HIF-1α also contributes)

**CNS hemangioblastoma locations (VHL disease):**
- Cerebellum: ~55% of CNS hemangioblastomas; most common location; often in posterior fossa
- Spinal cord: ~44%; all spinal levels; may cause myelopathy, syringomyelia
- Brainstem: ~18%; medulla most common; high surgical risk
- Supratentorial: ~5%; rare; may involve cerebrum

**Presentation and management:**
- Symptoms: cerebellar ataxia, headache (cerebellar); limb weakness, sensory loss, bladder dysfunction (spinal); dysphagia, dysarthria (brainstem)
- Polycythemia: hemangioblastoma stromal cells produce EPO (HIF-2α-driven) → paraneoplastic erythrocytosis; rare (more common in VHL type 1)
- Surveillance: annual brain + spine MRI from age 11
- Treatment: symptomatic or enlarging hemangioblastoma → surgical resection (mural nodule excision); stereotactic radiosurgery (SRS) for small, surgically inaccessible lesions; belzutifan (see below) stabilizes or shrinks hemangioblastomas

**Retinal hemangioblastoma (retinal capillary hemangioma, RCH):**
- Present in ~25-60% of VHL patients; often the earliest presenting tumor (mean age 25); may be bilateral (multiple lesions in one or both eyes)
- Peripheral lesion: treatable with laser photocoagulation or cryotherapy; anti-VEGF (bevacizumab intravitreal) for some lesions
- Juxtapapillary lesion: difficult to treat; can affect optic disc → optic atrophy; higher risk of vision loss
- Surveillance: annual dilated fundus exam from age 1 (or at diagnosis of VHL); fluorescein angiography to define lesion boundaries

### Clear cell renal cell carcinoma (ccRCC)

- **Lifetime risk**: ~25-45% for VHL type 1 and type 2B; lower for type 2A/2C
- **Biology**: VHL LOF → HIF-2α → VEGF → angiogenesis; PDGF → stromal growth; CXCR4/CXCL12 → invasion; metabolic reprogramming (Warburg shift, lipid accumulation — clear cell morphology = glycogen and lipid-filled cytoplasm)
- **Bilaterality and multifocality**: VHL ccRCC is characteristically bilateral and multifocal; dozens to hundreds of early lesions may be present; risk of developing new lesions over decades
- **3 cm threshold**: standard surveillance/surgical rule — lesions ≤3 cm: active surveillance (annual MRI/CT); lesions >3 cm: nephron-sparing surgery (NSS) recommended due to metastatic risk rising sharply above 3 cm; RFA/cryoablation as alternatives in bilateral disease to preserve renal function
- **Belzutifan (Welireg)**: oral HIF-2α inhibitor (PT2977; MK-6482); FDA approved August 2021; LITESPARK-004 trial: ORR ~49% for RCC (23% CR, 26% PR), ~93% ORR for CNS hemangioblastoma; indicated for VHL disease-associated RCC, CNS hemangioblastoma, and pNET (not requiring immediate surgery)
- **Advanced/metastatic VHL-ccRCC**: VEGF pathway inhibitors (sunitinib, pazopanib, cabozantinib); PD-1/PD-L1 + VEGF combination (nivolumab+cabozantinib, pembrolizumab+axitinib) effective in VHL-associated metastatic ccRCC similar to sporadic ccRCC

### Pancreatic manifestations

- **Serous cystadenomas**: most common pancreatic lesion (~70% of VHL patients); benign honeycomb cyst clusters; monitoring with MRI; rare complication (biliary obstruction if very large)
- **Pancreatic NETs (pNET)**: ~15% of VHL patients; typically non-functional (no excess hormone production); risk of malignancy correlates with size; ≥3 cm or doubling time <2 years → resection; belzutifan approved for VHL-related pNET requiring no immediate surgery

### Pheochromocytoma (VHL type 2)

- VHL type 2 pheo: median age at diagnosis ~30 years; often bilateral (>50% of VHL pheo); usually adrenal (rarely extra-adrenal); typically secretes normetanephrine (norepinephrine-producing; NMN elevated, MN not elevated)
- Plasma free metanephrines: annual screening from age 8 in type 2 families
- Treatment: surgical adrenalectomy; cortical-sparing adrenalectomy for bilateral pheo (to avoid permanent Addison's)

### Endolymphatic sac tumor (ELST)

- Present in ~10-15% of VHL patients; locally invasive tumor of the endolymphatic sac (posterior petrous bone); hearing loss (sensorineural), tinnitus, vertigo → mimics Menière's disease
- Surveillance: MRI of temporal bones at diagnosis and every 3-5 years; audiologic testing
- Treatment: surgical excision; early detection and resection preserves hearing better than late treatment

## Pathology

### Surveillance program (VHL disease)

| Age | Screening modality | Target |
|---|---|---|
| Annual, from age 1 | Dilated funduscopy | Retinal hemangioblastoma |
| Annual, from age 8 | Plasma free metanephrines | Pheochromocytoma (type 2) |
| Annual, from age 11 | Brain + spine MRI | CNS hemangioblastoma |
| Annual, from age 15 | Abdominal MRI or CT | RCC, pancreatic NETs/cysts |
| Annual, from age 11 | Audiologic testing + petrous MRI | ELST |

**Surgical principles:**
- NSS (nephron-sparing surgery): bilateral multifocal RCC → preserve nephrons; laparoscopic/robotic approaches preferred; R0 resection of mural nodule only in hemangioblastoma
- Cortical-sparing adrenalectomy: bilateral pheo → preserve cortex where possible to avoid Addison's
- Belzutifan as bridge therapy: used to stabilize lesions before surgery or as an alternative to surgery in patients with multiple lesions not yet requiring intervention

**VHL disease vs. other hereditary RCC syndromes:**

| Syndrome | Gene | RCC histology | Other features |
|---|---|---|---|
| VHL disease | VHL | Clear cell | Hemangioblastoma, pheo, pNET |
| BHD | FLCN | Chromophobe, hybrid oncocytic | Fibrofolliculoma, lung cysts |
| HLRCC | FH | Type 2 papillary | Cutaneous/uterine leiomyoma |
| Hereditary papillary RCC | MET | Type 1 papillary | Multifocal type 1 pRCC only |
| SDH-related | SDHB/C/D | Clear cell or chromophobe | Paraganglioma, pheo, GIST |

## Connections

- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — Germline VHL LOF causes VHL disease via constitutive HIF-1α/2α accumulation; VHL β-domain recognizes EGLN1-hydroxylated HIF → ubiquitination; missense VHL variants predict pheo risk (type 2A/2B/2C) vs truncating (type 1, high RCC); belzutifan targets HIF-2α downstream.
- `connects-to` → **[EGLN1](../../03-molecular/egln1/README.md)** — EGLN1 (PHD2) hydroxylates HIF-1α/2α under normoxia for VHL-mediated degradation; in VHL disease, VHL LOF renders HIF constitutively stable regardless of EGLN1 activity; EGLN1 inhibitors (PHD inhibitors) activate HIF for CKD anemia treatment by the same mechanism as VHL LOF.
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — Clear cell RCC (ccRCC) is the most common VHL disease tumor (~25-45% lifetime risk); VHL LOF → HIF-2α/VEGF → neovascularization → ccRCC; NSS (nephron-sparing surgery) for ≤3 cm tumors; belzutifan (HIF-2α inhibitor) FDA-approved for VHL disease-associated ccRCC since 2021.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../../07-system/pheochromocytoma-paraganglioma/README.md)** — VHL disease type 2 (missense variants) carries pheochromocytoma risk (~8-20%); VHL pheo is typically bilateral, benign, adrenal, and normetanephrine-secreting; VHL-pheo driven by HIF-2α pseudohypoxia → catecholamine biosynthesis upregulation; resection curative.

[^lonser-2003-vhl-disease]: Lonser RR, Glenn GM, Walther M, et al. von Hippel-Lindau disease. *Lancet.* 2003;361(9374):2059-2067. [doi:10.1016/S0140-6736(03)13643-4](https://doi.org/10.1016/S0140-6736(03)13643-4) · [PubMed 12814730](https://pubmed.ncbi.nlm.nih.gov/12814730/)
[^choueiri-2020-hif2-rcc]: Choueiri TK, Kaelin WG Jr. Targeting the HIF2-VEGF axis in renal cell carcinoma. *Nat Med.* 2020;26(10):1519-1530. [doi:10.1038/s41591-020-1093-z](https://doi.org/10.1038/s41591-020-1093-z) · [PubMed 33020650](https://pubmed.ncbi.nlm.nih.gov/33020650/)
