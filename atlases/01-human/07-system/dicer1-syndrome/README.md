---
schema: human-scale-entry/v1
id: dicer1-syndrome
name: DICER1 Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "DICER1 syndrome is caused by germline DICER1 mutations with somatic RNase IIIb hotspot second hits; pleuropulmonary blastoma (PPB), cystic nephroma, ovarian Sertoli-Leydig cell tumors, multinodular goiter; PPB is the sentinel tumor; surveillance from infancy."
aliases: ["DICER1 syndrome", "DICER1 mutation syndrome", "familial PPB", "pleuropulmonary blastoma hereditary", "DICER1 PPB", "DICER1 cystic nephroma", "DICER1 SLCT", "DICER1 goiter", "DICER1 cancer predisposition"]
sources:
  - id: schultz-2018-dicer1-surveillance
    type: peer-reviewed
    cite: "Schultz KAP, Williams GM, Kamihara J, et al. DICER1 and Associated Conditions: Identification of At-risk Individuals and Recommended Surveillance Strategies. Clin Cancer Res. 2018;24(10):2251-2261."
    doi: "10.1158/1078-0432.CCR-17-3089"
    pmid: "29343557"
    url: "https://doi.org/10.1158/1078-0432.CCR-17-3089"
  - id: hill-2009-dicer1
    type: peer-reviewed
    cite: "Hill DA, Ivanovich J, Priest JR, et al. DICER1 mutations in familial pleuropulmonary blastoma. Science. 2009;325(5943):965."
    doi: "10.1126/science.1174334"
    pmid: "19556464"
    url: "https://doi.org/10.1126/science.1174334"
cross_links:
  - target: 01-human/03-molecular/dicer1
    relation: connects-to
    note: "DICER1 RNase IIIb hotspot mutations selectively deplete 5p miRNAs (let-7-5p, miR-17-5p family) → derepression of oncoproteins; germline LOF + somatic hotspot = two-hit mechanism; pathogenic hotspot residues E1705, D1709, E1813, D1810 cluster in metal-binding motif of RNase IIIb."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "MYCN amplification is the most common cooperating somatic event in PPB type III (solid, high-grade); DICER1 5p miRNA loss → let-7/miR-17 family derepression → MYCN upregulation → RB bypass; PPB type III with MYCN amplification has ~53% 5-year OS."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Cervical embryonal rhabdomyosarcoma (ERMS) is a rare but sentinel DICER1 syndrome tumor; DICER1 hotspot mutations found in ~20% of cervical ERMS; DICER1 syndrome RMS is distinct from sporadic RMS; conservative surgery preferred in pediatric cervical ERMS."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Ovarian Sertoli-Leydig cell tumors (SLCT) are the most common ovarian manifestation of DICER1 syndrome; DICER1 hotspot mutations drive ~60% of all SLCT; DICER1 germline carriers: pelvic US surveillance from age 8; BEP chemotherapy for advanced/recurrent SLCT."
---

# DICER1 Syndrome

## Overview

**DICER1 syndrome** (also called **familial pleuropulmonary blastoma** or **DICER1-related tumor predisposition**) is an autosomal dominant hereditary tumor predisposition syndrome caused by germline pathogenic variants in the **DICER1** gene encoding the microRNA-processing enzyme Dicer. DICER1 syndrome is characterized by a predisposition to a spectrum of predominantly **pediatric and adolescent tumors**, most notably **pleuropulmonary blastoma (PPB)** — a rare intrathoracic malignancy that is the sentinel/index tumor for the syndrome — as well as **cystic nephroma**, **ovarian Sertoli-Leydig cell tumors (SLCT)**, **multinodular goiter**, **cervical embryonal rhabdomyosarcoma**, and **pituitary blastoma** among others. DICER1 syndrome tumors have a distinctive two-hit molecular mechanism: the somatic second hit is not a second loss-of-function mutation but a **hotspot missense mutation** in the RNase IIIb domain of DICER1 that selectively impairs processing of miRNA-5p family members. The syndrome was genetically defined by Hill et al. in 2009, with comprehensive clinical guidelines subsequently developed by Schultz et al. in 2018 [^hill-2009-dicer1] [^schultz-2018-dicer1-surveillance].

**DICER1 syndrome tumor spectrum:**

| Tumor | Median age | Lifetime risk in carriers | Key features |
|---|---|---|---|
| Pleuropulmonary blastoma (PPB) | 2-4 years | ~5% (type I-III combined) | Type I (cystic) → type II → type III (solid); lung/pleura |
| Cystic nephroma | 2-4 years | ~2% | Benign cystic renal tumor; female predominance |
| Ovarian SLCT | 15-25 years | ~3-5% (females) | Androgenic; hotspot somatic in ~60% of all SLCT |
| Multinodular goiter | Any age | ~75% (lifetime) | Usually benign; DTC risk modestly elevated |
| Cervical embryonal RMS | 5-20 years | <1% | Rare; botryoid pattern; conservative surgery |
| Pituitary blastoma | <2 years | Very rare | Infancy onset; ACTH excess |
| Ciliary body medulloepithelioma | <10 years | Very rare | Intraocular; locally invasive |
| Nasal chondromesenchymal hamartoma | Infancy | Very rare | Benign; nasal obstruction |

## Structure

### Genetic basis of DICER1 syndrome

**DICER1 gene (14q32.13):**
- 1922 aa; 218 kDa; ubiquitously expressed; essential for embryonic development and tissue homeostasis
- Germline pathogenic variant spectrum: frameshift, nonsense, splice site (~70%); missense in non-RNase IIIb domains (~15%); large deletions (~5%); some germline missense variants in RNase IIIb (these may function differently from somatic hotspot variants)
- Penetrance: variable; **5-10%** of DICER1 carriers develop PPB by age 8; most carriers never develop cancer; some develop only multinodular goiter (very high penetrance); incomplete and sex-specific (SLCT only in females)
- De novo germline: ~10-15% of DICER1 pathogenic variants arise de novo (no family history)
- **Autosomal dominant inheritance**: 50% offspring risk; families may appear to have only one affected individual because PPB is rare and penetrance is incomplete for most tumor types

**Somatic second-hit hotspot mechanism:**

DICER1 somatic hotspot mutations cluster in the RNase IIIb metal-binding residues:
- **E1705** (Glu1705): changed to K, D, G, Q — most common hotspot
- **D1709** (Asp1709): changed to N, G, V
- **E1813** (Glu1813): changed to K, D, G
- **D1810** (Asp1810): changed to V, N

All hotspot substitutions eliminate Mg²⁺ chelation in the RNase IIIb active site → 5p arm cleavage fails → pre-miRNA is cleaved on the 3p arm only (by RNase IIIa, which is intact) → only miRNA-3p strands are produced; miRNA-5p strands accumulate as unprocessed hairpin or are degraded

Downstream consequence:
- let-7-5p family depletion → KRAS, NRAS, LIN28A/B, MYCN, IGF2BP1 derepression → cell cycle entry
- miR-200-5p family depletion → ZEB1/ZEB2 derepression → mesenchymal phenotype → PPB stromal component
- miR-17-5p (oncomiR cluster) — paradoxically depleted by RNase IIIb hotspot despite being oncogenic when overexpressed; indicates complex miRNA network rewiring

## Function

### Pleuropulmonary blastoma (PPB)

PPB is the **defining sentinel tumor** of DICER1 syndrome. It is the most common primary malignant lung tumor of childhood and virtually always associated with DICER1 mutations (germline ± somatic):

**PPB type classification (Dehner):**
- **Type I (cystic)**: Pure multilocular cystic lesion; thin-walled cysts; grossly resembles congenital pulmonary airway malformation (CPAM/CCAM); malignant cells are a minor camouflaged subepithelial population (subepithelial cambium layer of malignant cells beneath bland epithelium); median age 7 months; 5-year OS ~90%; surgical resection curative if complete
- **Type Ir (regressed/spontaneously resolved cystic)**: Cyst that has involuted; no residual malignant cells; recognized retrospectively; may represent spontaneous regression of type I PPB
- **Type II (cystic-solid)**: Mixed cystic and solid components; overt malignant stroma (blastomatous, sarcomatous, rhabdoid); median age 30 months; 5-year OS ~71%; treatment: surgery + chemotherapy (vincristine-actinomycin D-cyclophosphamide or IVADo regimen)
- **Type III (solid)**: Purely solid, high-grade blastematous/sarcomatous mass; MYCN amplification common; median age 44 months; 5-year OS ~53%; treatment: surgery + aggressive chemotherapy ± consolidation

**PPB and DICER1 genetics:**
- >98% of PPB harbor DICER1 mutations (most: germline LOF + somatic hotspot); rare PPB with only somatic DICER1 hotspot (no germline); even rarer PPB without DICER1 mutations
- PPB mimics: type I PPB can be mistaken for CPAM/CCAM on imaging and even pathology; re-review of lung cysts in children → significant fraction reclassified as PPB type I; key distinction: subepithelial primitive cells in PPB type I vs mature smooth muscle lining in CPAM

**PPB chemotherapy regimens:**
- **Type I**: Complete surgical resection ± observation; chemotherapy not universally required after R0 resection; ongoing debate
- **Type II/III**: Post-resection chemotherapy: IVADo (ifosfamide-vincristine-actinomycin D-doxorubicin) or VAC (vincristine-actinomycin D-cyclophosphamide)-based; high-dose chemotherapy with autologous stem cell rescue in relapsed/refractory type III

### Ovarian Sertoli-Leydig cell tumors (SLCT)

SLCT is the most common ovarian tumor associated with DICER1:
- **Well-differentiated SLCT**: low malignant potential; primary oophorectomy often curative; uncommon
- **Intermediate/poorly differentiated SLCT**: androgenic virilization (hirsutism, clitoromegaly, amenorrhea); stage I at diagnosis ~80%; unilateral; treatment: fertility-sparing surgery (unilateral oophorectomy) if stage I + young patient; systemic chemotherapy (BEP) for advanced stage (II-IV) or recurrence
- DICER1 hotspot mutations: in ~60% of all SLCT regardless of germline status; also seen in gynandroblastomas (mixed SLCT)

### Multinodular goiter (DICER1-related)

- Present in the majority of adult DICER1 carriers (~75%); often the only clinical manifestation
- Histology: multinodular, hyperplastic, often with colloid-filled follicles; distinct from PTEN-related thyroid pathology (Cowden syndrome) which shows follicular adenoma
- Differentiated thyroid cancer: modestly elevated; surveillance with thyroid ultrasound annually from age 8

## Pathology

### Surveillance and management guidelines

**Surveillance by age (Schultz 2018 guidelines):**

**Birth to 8 years (PPB risk window):**
- Annual chest CT or MRI (for PPB detection)
- Abdominal/pelvic ultrasound (for cystic nephroma); frequency may be reduced after age 4
- Physical examination every 6-12 months

**Age 8 onward:**
- Annual thyroid ultrasound (for goiter/DTC surveillance)
- Annual pelvic ultrasound in females (for SLCT surveillance from age 8-40)
- Head/neck MRI every 3 years (for rare tumors: pituitary blastoma, DICER1-related SNUC/nasal tumors)

**At-risk individuals (family members of DICER1 germline carriers):**
- Germline DICER1 testing recommended for all first-degree relatives
- If positive: initiate surveillance protocol above
- Cascade genetic testing: 50% risk per first-degree relative

**Genetic counseling:**
- DICER1 syndrome is autosomal dominant; 50% offspring risk
- Prenatal testing/preimplantation genetic testing available
- Most DICER1 carriers have an excellent prognosis; morbidity and mortality concentrated in PPB (especially type III) and relapsed SLCT
- Incidental DICER1 variants of uncertain significance (VUS): challenge in interpretation; functional assays in development

**Differential diagnosis of childhood thoracic cysts:**

When a child is found to have a thoracic cystic lesion, DICER1 syndrome should be considered:
- CPAM/CCAM (congenital pulmonary airway malformation): histologically mature smooth muscle lining; no subepithelial primitive cells; no DICER1 mutation
- PPB type I: malignant subepithelial cells; DICER1 mutations present; subtle but critical distinction
- Key diagnostic approach: any thoracic cyst in a child <8 years → pathological review by expert PPB pathologist + DICER1 testing of tumor and germline

## Connections

- `connects-to` → **[DICER1](../../03-molecular/dicer1/README.md)** — DICER1 RNase IIIb hotspot mutations selectively deplete 5p miRNAs (let-7-5p, miR-17-5p family) → derepression of oncoproteins; germline LOF + somatic hotspot = two-hit mechanism; pathogenic hotspot residues E1705, D1709, E1813, D1810 cluster in metal-binding motif of RNase IIIb.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — MYCN amplification is the most common cooperating somatic event in PPB type III (solid, high-grade); DICER1 5p miRNA loss → let-7/miR-17 family derepression → MYCN upregulation → RB bypass; PPB type III with MYCN amplification has ~53% 5-year OS.
- `connects-to` → **[Rhabdomyosarcoma](../../07-system/rhabdomyosarcoma/README.md)** — Cervical embryonal rhabdomyosarcoma (ERMS) is a rare but sentinel DICER1 syndrome tumor; DICER1 hotspot mutations found in ~20% of cervical ERMS; DICER1 syndrome RMS is distinct from sporadic RMS; conservative surgery preferred in pediatric cervical ERMS.
- `connects-to` → **[Ovarian Cancer](../../07-system/ovarian-cancer/README.md)** — Ovarian Sertoli-Leydig cell tumors (SLCT) are the most common ovarian manifestation of DICER1 syndrome; DICER1 hotspot mutations drive ~60% of all SLCT; DICER1 germline carriers: pelvic US surveillance from age 8; BEP chemotherapy for advanced/recurrent SLCT.

[^schultz-2018-dicer1-surveillance]: Schultz KAP, Williams GM, Kamihara J, et al. DICER1 and Associated Conditions: Identification of At-risk Individuals and Recommended Surveillance Strategies. *Clin Cancer Res.* 2018;24(10):2251-2261. [doi:10.1158/1078-0432.CCR-17-3089](https://doi.org/10.1158/1078-0432.CCR-17-3089) · [PubMed 29343557](https://pubmed.ncbi.nlm.nih.gov/29343557/)
[^hill-2009-dicer1]: Hill DA, Ivanovich J, Priest JR, et al. DICER1 mutations in familial pleuropulmonary blastoma. *Science.* 2009;325(5943):965. [doi:10.1126/science.1174334](https://doi.org/10.1126/science.1174334) · [PubMed 19556464](https://pubmed.ncbi.nlm.nih.gov/19556464/)
