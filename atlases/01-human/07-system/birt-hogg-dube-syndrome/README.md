---
schema: human-scale-entry/v1
id: birt-hogg-dube-syndrome
name: Birt-Hogg-Dubé Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Birt-Hogg-Dubé syndrome (BHD) is caused by germline FLCN mutations; fibrofolliculomas (skin), pulmonary cysts (pneumothorax risk 7×), bilateral multifocal chromophobe/hybrid oncocytic RCC (~30% lifetime); nephron-sparing surveillance surgery; mTOR inhibitors explored."
aliases: ["BHD", "Birt-Hogg-Dubé syndrome", "Birt-Hogg-Dube", "FLCN syndrome", "BHD syndrome", "chromophobe RCC hereditary", "fibrofolliculoma syndrome", "BHD RCC", "BHD pneumothorax", "BHD kidney cancer"]
sources:
  - id: nickerson-2002-flcn-bhd
    type: peer-reviewed
    cite: "Nickerson ML, Warren MB, Toro JR, et al. Mutations in a novel gene lead to kidney tumors, lung wall defects, and benign tumors of the hair follicle in patients with the Birt-Hogg-Dubé syndrome. Cancer Cell. 2002;2(2):157-164."
    doi: "10.1016/s1535-6108(02)00104-6"
    pmid: "12204536"
    url: "https://doi.org/10.1016/s1535-6108(02)00104-6"
  - id: tsun-2013-flcn-rag
    type: peer-reviewed
    cite: "Tsun ZY, Bar-Peled L, Chantranupong L, et al. The folliculin tumor suppressor is a GAP for the RagC/D GTPases that signal amino acid levels to mTORC1. Mol Cell. 2013;52(4):495-505."
    doi: "10.1016/j.molcel.2013.09.016"
    pmid: "24095279"
    url: "https://doi.org/10.1016/j.molcel.2013.09.016"
cross_links:
  - target: 01-human/03-molecular/flcn
    relation: connects-to
    note: "Germline FLCN truncating mutations cause BHD; FLCN is a GAP for RagC/D (amino acid sensing for mTORC1); biallelic FLCN LOF in each BHD tumor (second hit LOH at 17p11.2); somatic FLCN in sporadic chromophobe RCC (~20-25%)"
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "FLCN LOF → Rag GTPase dysregulation → impaired mTORC1 lysosomal docking (RagC/D-GAP activity lost); mTOR inhibitors (everolimus) explored in BHD-associated RCC; FLCN LOF mTOR biology distinct from TSC1/TSC2 LOF (Rheb pathway) but both converge on mTORC1"
  - target: 01-human/03-molecular/vhl
    relation: connects-to
    note: "BHD-associated RCC (chromophobe) vs VHL-associated RCC (clear cell): distinct histology and molecular drivers; VHL → HIF-1α pseudohypoxia; FLCN → mTOR/Rag dysregulation; BHD chromophobe has better prognosis than VHL ccRCC; belzutifan for VHL (not yet BHD)"
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "BHD lifetime RCC risk ~15-30%; chromophobe + hybrid oncocytic histology; bilateral multifocal; annual MRI from age 20; nephron-sparing surgery when >3 cm; sunitinib/cabozantinib for metastatic BHD RCC; chromophobe RCC 5-year OS ~88%"
---

# Birt-Hogg-Dubé Syndrome

## Overview

**Birt-Hogg-Dubé syndrome (BHD)** is an autosomal dominant hereditary cancer and hamartoma predisposition syndrome caused by germline pathogenic variants in **FLCN** (folliculin; chromosome 17p11.2), a GAP (GTPase-activating protein) for the **RagC and RagD GTPases** that regulate mTORC1 activation by amino acids at the lysosomal surface. BHD was first described in 1977 by dermatologists Birt, Hogg, and Dubé as a condition of fibrofolliculomas and trichodiscomas; the renal tumor and pulmonary cyst associations were recognized subsequently. BHD is characterized by a triad: (1) **cutaneous fibrofolliculomas** — benign white papules on the face, neck, and trunk from hair follicle origin; (2) **pulmonary cysts** — thin-walled basal cysts causing a ~7-fold increased risk of spontaneous pneumothorax; and (3) **bilateral multifocal renal tumors** — predominantly chromophobe RCC and hybrid oncocytic/chromophobe RCC, with ~15-30% lifetime risk of renal malignancy. BHD-associated RCC has a distinct biology from VHL-driven clear cell RCC (not HIF-1α-mediated; driven by mTOR-Rag GTPase-TFE3 dysregulation) and a relatively favorable prognosis within the RCC spectrum. Surveillance with annual MRI and nephron-sparing surgery for tumors >3 cm are the mainstay of management [^nickerson-2002-flcn-bhd] [^tsun-2013-flcn-rag].

**Epidemiology:**
- Prevalence: ~1/200,000; ~1,500-2,500 diagnosed patients in the USA; considerably underdiagnosed (fibrofolliculomas often mistaken for fibrous papules or adenoma sebaceum)
- Inheritance: autosomal dominant; 50% transmission per generation
- De novo mutations: ~10% of BHD cases; may present without family history
- FLCN germline pathogenic variant found in ~80-90% of clinically diagnosed BHD families; remainder may have deep intronic variants, promoter mutations, or mosaicism
- Penetrance: fibrofolliculomas ~90% by age 40; pulmonary cysts ~80-90%; renal tumors ~15-30% lifetime

**Comparison of hereditary RCC syndromes:**

| Syndrome | Gene | RCC histology | Lifetime RCC risk | Molecular driver |
|---|---|---|---|---|
| VHL disease | VHL | Clear cell | ~65-70% | HIF-1α/HIF-2α pseudohypoxia |
| BHD syndrome | FLCN | Chromophobe, hybrid oncocytic | ~15-30% | mTOR/Rag/TFE3 dysregulation |
| Hereditary papillary RCC | MET | Type 1 papillary | ~70-80% | MET kinase constitutive activation |
| HLRCC | FH | Collecting duct-like, type 2B papillary | ~15-20% | HIF-1α + fumarate oncometabolite |
| TSC | TSC1/TSC2 | Angiomyolipoma (benign) + rarely ccRCC | ~5% (malignant RCC) | mTOR via Rheb |

## Structure

### BHD clinical manifestations

**Cutaneous fibrofolliculomas:**
- Origin: from the fibrous sheath of the hair follicle (mantle/infundibulum region); distinct from sebaceous adenoma or fibrous papule
- Morphology: dome-shaped, smooth, white/skin-colored papules; 1-5 mm; occasionally larger
- Distribution: face (especially nose, perinasal, cheeks), neck, upper trunk; rarely on arms; never on palms or soles
- Age of onset: typically 3rd-5th decade (25-50 years); may be absent or sparse in young adults
- Symptoms: usually asymptomatic; cosmetic concern; may cause misdiagnosis as skin disease alone without kidney/pulmonary workup
- Histology: anastomosing epithelial strands from hair follicle mantles in a fibromyxoid stroma; distinct from trichofolliculoma, fibrous papule; FLCN IHC: reduced nuclear staining in fibrofolliculoma cells
- Dermoscopy: parallel or reticular pattern with yellowish globules
- Additional skin features: trichodiscomas (hair disc hamartomas; similar to fibrofolliculoma, sometimes considered same entity), acrochordons (skin tags — non-specific but associated)

**Pulmonary cysts:**
- Prevalence: ~80-90% of BHD gene carriers; may be asymptomatic and discovered incidentally
- Imaging (HRCT): bilateral, basal, subpleural thin-walled cysts (air-filled, no matrix); 2 mm to >20 cm; may be multifocal; cyst walls are thin (<2 mm); no ground-glass halo; variable size/number within same patient
- Histology of cyst wall: lined by type II pneumocytes or flattened cells; small FLCN-deficient cells may be present in some cysts
- Pulmonary function: usually normal (cysts are air-filled, not solid); reduced DLCO in some patients
- Spontaneous pneumothorax: ~22-38% of BHD patients (vs ~0.1-0.3% general population); risk ~7-fold higher than general population; bilateral simultaneous pneumothorax rare but described; management: observation for small, tube thoracostomy for large; after first spontaneous pneumothorax in BHD → contralateral risk ~30-50% over 10 years → pleurodesis (surgical or mechanical) recommended after first ipsilateral recurrence or bilateral event
- No treatment for asymptomatic cysts: surveillance HRCT to monitor cyst growth (rate rare); HRCT baseline recommended for all confirmed BHD carriers

### BHD-associated renal tumors

**Histological spectrum:**
- Chromophobe RCC (~50% of BHD renal tumors): large pale cells with perinuclear halo; Hale colloidal iron diffusely positive; IHC: CK7++, CD117+, parvalbumin+; nuclear TFE3 often positive; not HIF-1α-driven; 5-year OS ~88% for localized disease (better than ccRCC)
- Hybrid oncocytic/chromophobe tumor (~33%): overlapping features of chromophobe RCC and oncocytoma; eosinophilic granular cytoplasm (mitochondria-packed); perinuclear halo may be subtle; IHC: mixed CK7/CD117
- Renal oncocytoma (benign, ~5%): mahogany-brown, well-circumscribed; mitochondria-rich cells; FLCN LOF found in ~25% of sporadic oncocytomas; in BHD, oncocytomas may be adjacent to or mixed with chromophobe foci
- Clear cell RCC (~5%): less common in BHD; unclear if true association or coincidence; VHL is intact in BHD (unless coincidental second germline mutation)
- Papillary RCC (<5%): rare in BHD

**Tumor characteristics:**
- Bilateral: ~67% of BHD-associated RCC is bilateral at time of diagnosis (compared to ~1-2% in sporadic RCC)
- Multifocal: ~52% of BHD RCC patients have multifocal tumors on a single kidney
- Small at detection: surveillance-detected tumors often <3 cm; asymptomatic; favorable stage at detection

## Function

### Molecular pathogenesis of BHD

**FLCN LOF and RagC/D dysregulation:** [^tsun-2013-flcn-rag]
Normal: amino acid availability → Ragulator activates FLCN-FNIP → FLCN stimulates RagC/D GTPase → RagC/D-GDP → mTORC1 lysosomal docking → mTOR activated; in FLCN-deficient cells: RagC/D remains GTP-loaded → impaired mTORC1 lysosomal docking under some conditions; but net mTORC1 output in BHD RCC: elevated (via other inputs — AKT, ERK) — this paradox is explained by differential Rag signaling contexts and feedback loops

**TFE3/TFEB nuclear translocation:**
FLCN LOF → TFE3 and TFEB escape mTORC1-mediated cytoplasmic sequestration → nuclear TFE3/TFEB → lysosomal biogenesis genes (LAMP1, CTSD, MCOLN1), autophagy genes (BECN1, LC3), and mitochondrial biogenesis genes (PGC-1α, TFAM, NDUFA, COX subunits) upregulated; mitochondrial biogenesis → mitochondria accumulation → oncocytic appearance; TFE3 nuclear immunostaining is a practical diagnostic marker for FLCN-deficient RCC

**mTOR-Rag vs mTOR-Rheb (comparison with TSC):**
| Pathway | Regulator | mTOR activator | Tumor type |
|---|---|---|---|
| Rheb pathway | TSC1-TSC2 complex (GAP for Rheb) | Rheb-GTP | TSC-associated AML, SEGA |
| Rag pathway | FLCN-FNIP (GAP for RagC/D) | RagA/B-GTP + RagC/D-GDP | BHD-associated chromophobe RCC |
Both converge on mTORC1 but via distinct upstream signals; rapalogues active in both contexts

**Pulmonary cyst biology:**
FLCN-deficient alveolar type II cells → mTOR dysregulation + TFE3 activation → abnormal alveolar remodeling → cyst formation; mouse models (lung-specific Flcn knockout): cysts develop, similar to BHD human lung; mechanism: FLCN LOF → lysosomal exocytosis → cathepsins secreted → extracellular matrix degradation → cyst formation; similar biology may explain pulmonary LAM in TSC (smooth muscle-like LAM cells with TSC2 LOF) though distinct cell types

## Pathology

### Diagnosis

**Clinical diagnosis:**
Major diagnostic criteria:
- ≥5 fibrofolliculomas or trichodiscomas with at least 1 histologically confirmed, adult onset
- Pathogenic FLCN germline variant

Minor criteria:
- Multiple bilateral pulmonary cysts (basal, subpleural) with no other apparent cause ± spontaneous pneumothorax
- Renal tumor ≤50 years of age OR bilateral or multifocal RCC OR chromophobe/hybrid oncocytic RCC (confirmed histology)
- First-degree relative with BHD

Definite BHD: 1 major OR 2 minor criteria (European BHD Consortium definition)

**Genetic testing:**
- FLCN gene sequencing (full coding + splice sites): ~80-85% sensitivity in clinical BHD
- MLPA for large deletions: additional ~5-10%
- If all negative: repeat sequencing with attention to intragenic microsatellite repeats (c.1285dupC exon 11 most common mutation); RNA splicing analysis; somatic mosaicism testing
- Cascade testing: all first-degree relatives of pathogenic FLCN variant carrier

### Surveillance and management (NCCN/European guidelines)

**Renal:**
- Annual renal MRI (preferred) or ultrasound alternating every 6 months from age 20-21
- Any renal tumor <3 cm: active surveillance with imaging every 6-12 months
- Renal tumor ≥3 cm or growing: intervention recommended
  - **Nephron-sparing surgery (partial nephrectomy)**: gold standard; open, laparoscopic, or robot-assisted; goal: complete tumor excision with negative margins while preserving maximum renal parenchyma; critical in BHD due to bilateral/multifocal tumors
  - **Thermal ablation** (radiofrequency ablation, cryoablation): for smaller tumors (<3 cm) in selected patients; less morbidity; incomplete ablation risk; used in patients with poor surgical risk or existing renal insufficiency
  - **Radical nephrectomy**: avoided unless entire kidney is tumor-replaced; lifelong kidney function preservation is paramount
- Post-treatment surveillance: MRI every 6-12 months × 2-3 years, then annually

**Pulmonary:**
- Baseline HRCT for all confirmed BHD carriers
- Routine HRCT surveillance not necessary if cysts stable and asymptomatic
- First spontaneous pneumothorax: hospitalization, tube thoracostomy or aspiration; after resolution, discuss pleurodesis
- After 2nd ipsilateral pneumothorax OR after 1st contralateral spontaneous pneumothorax: video-assisted thoracoscopic (VATS) pleurodesis (mechanical or chemical) recommended
- Counsel BHD patients: avoid scuba diving (barotrauma → pneumothorax); pressurized aircraft OK (commercial airline pressure equivalent to 8,000 ft — minimal additional risk)
- Genetic counseling: inform family members of pneumothorax risk during air travel or diving

**Dermatologic:**
- Confirm fibrofolliculoma diagnosis by punch biopsy (histology)
- Cosmetic management: laser (CO2, Er:YAG), dermabrasion, shave excision; lesions recur after treatment
- Topical rapamycin: anecdotal reports of fibrofolliculoma reduction with topical sirolimus ointment (not FDA-approved for this indication)

**Treatment of metastatic BHD-associated RCC:**
- No FDA-approved BHD-specific therapy
- Sunitinib (VEGFR-TKI): modest activity in chromophobe RCC (ORR ~5-10%); less effective than in ccRCC
- Cabozantinib (VEGFR/MET/AXL inhibitor): higher activity in non-ccRCC including chromophobe (ORR ~15-20%)
- Checkpoint inhibitors: nivolumab + ipilimumab; chromophobe RCC has low TMB and PD-L1 → modest ICB response
- Everolimus: mTOR inhibitor; rational in FLCN-deficient RCC; case reports of activity; Phase 2 BHD-specific study ongoing
- Belzutifan (HIF-2α inhibitor): explored in chromophobe RCC (not VHL-driven but may have HIF-2α activity via mTOR); Phase 2 data emerging (NCT04924075)

**Prognosis:**
- BHD-associated RCC: when detected by surveillance at early stage (I-II), cure rate with NSS ~95%; 5-year OS for chromophobe RCC overall ~88% (significantly better than ccRCC at equivalent stage)
- Metastatic chromophobe RCC: mOS ~24-30 months (vs ~18-24 months for metastatic ccRCC in VEGF-TKI era)
- Major life impact: pulmonary (pneumothorax morbidity) and the need for lifelong renal surveillance/surgery dominate quality of life in BHD; with surveillance, premature death from BHD is rare

## Connections

- `connects-to` → **[FLCN](../../03-molecular/flcn/README.md)** — Germline FLCN truncating mutations cause BHD; FLCN is a GAP for RagC/D (amino acid sensing for mTORC1); biallelic FLCN LOF in each BHD tumor (second hit LOH at 17p11.2); somatic FLCN in sporadic chromophobe RCC (~20-25%)
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — FLCN LOF → Rag GTPase dysregulation → impaired mTORC1 lysosomal docking (RagC/D-GAP activity lost); mTOR inhibitors (everolimus) explored in BHD-associated RCC; FLCN LOF mTOR biology distinct from TSC1/TSC2 LOF (Rheb pathway) but both converge on mTORC1
- `connects-to` → **[VHL](../../03-molecular/vhl/README.md)** — BHD-associated RCC (chromophobe) vs VHL-associated RCC (clear cell): distinct histology and molecular drivers; VHL → HIF-1α pseudohypoxia; FLCN → mTOR/Rag dysregulation; BHD chromophobe has better prognosis than VHL ccRCC; belzutifan for VHL (not yet BHD)
- `connects-to` → **[Renal Cell Carcinoma](../../07-system/renal-cell-carcinoma/README.md)** — BHD lifetime RCC risk ~15-30%; chromophobe + hybrid oncocytic histology; bilateral multifocal; annual MRI from age 20; nephron-sparing surgery when >3 cm; sunitinib/cabozantinib for metastatic BHD RCC; chromophobe RCC 5-year OS ~88%

[^nickerson-2002-flcn-bhd]: Nickerson ML, Warren MB, Toro JR, et al. Mutations in a novel gene lead to kidney tumors, lung wall defects, and benign tumors of the hair follicle in patients with the Birt-Hogg-Dubé syndrome. *Cancer Cell.* 2002;2(2):157-164. [doi:10.1016/s1535-6108(02)00104-6](https://doi.org/10.1016/s1535-6108(02)00104-6) · [PubMed 12204536](https://pubmed.ncbi.nlm.nih.gov/12204536/)
[^tsun-2013-flcn-rag]: Tsun ZY, Bar-Peled L, Chantranupong L, et al. The folliculin tumor suppressor is a GAP for the RagC/D GTPases that signal amino acid levels to mTORC1. *Mol Cell.* 2013;52(4):495-505. [doi:10.1016/j.molcel.2013.09.016](https://doi.org/10.1016/j.molcel.2013.09.016) · [PubMed 24095279](https://pubmed.ncbi.nlm.nih.gov/24095279/)
