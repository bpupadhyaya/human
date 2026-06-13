---
schema: human-scale-entry/v1
id: wilms-tumor
name: Wilms Tumor
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Wilms tumor (nephroblastoma) is the most common pediatric renal malignancy; peak age 3-4 years; favorable histology ~90% with 4-year OS >95%; anaplastic ~10% with TP53 mutations; WT1/CTNNB1/WTX/DROSHA drivers; actinomycin D+vincristine±doxorubicin backbone."
aliases: ["Wilms tumor", "nephroblastoma", "Wilms' tumor", "pediatric kidney cancer", "childhood renal tumor", "nephroblastoma WAGR", "Wilms anaplastic"]
sources:
  - id: dome-2015-wilms
    type: peer-reviewed
    cite: "Dome JS, Graf N, Geller JI, et al. Advances in Wilms tumor treatment and biology: progress through international collaboration. J Clin Oncol. 2015;33(27):2999-3007."
    doi: "10.1200/JCO.2015.62.1888"
    pmid: "26261251"
    url: "https://doi.org/10.1200/JCO.2015.62.1888"
  - id: dix-2006-arenl0002
    type: peer-reviewed
    cite: "Dix DB, Bhatt SM, Geller JI, et al. Treatment of Stage IV favorable histology Wilms tumor with incomplete lung metastasis response after chemotherapy: a report from Children's Oncology Group Study AREN0533. J Clin Oncol. 2018;36(16):1564-1570."
    doi: "10.1200/JCO.2017.77.1877"
    pmid: "29584550"
    url: "https://doi.org/10.1200/JCO.2017.77.1877"
cross_links:
  - target: 01-human/03-molecular/wt1
    relation: connects-to
    note: "WT1 mutations occur in ~10-15% sporadic Wilms tumor and are near-universal in WAGR and Denys-Drash syndromes; WT1+CTNNB1 co-mutation → blastemal-predominant Wilms from intralobar nephrogenic rests; WT1 is required for nephron formation from metanephric blastema."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CTNNB1 activating mutations occur in ~15-20% Wilms tumor, co-occurring with WT1 mutations; nuclear β-catenin marks the blastemal component; WNT activation promotes blastema self-renewal and prevents epithelial differentiation; WNT inhibitors studied preclinically."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations occur in ~70% of diffuse anaplastic Wilms (unfavorable histology); anaplasia is the strongest adverse prognostic factor; TP53 drives resistance to standard chemotherapy; anaplastic WT requires alkylator-based intensification (cyclophosphamide/etoposide)."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "IGF2 overexpression (~75% Wilms tumor via 11p15 imprinting loss) → IGF1R → PI3K-AKT-mTOR → proliferation; everolimus explored in relapsed Wilms; DROSHA/DGCR8 mutations impair miRNA biogenesis → mTOR derepression."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Wilms tumor (nephroblastoma) is the most common childhood kidney cancer, arising at age 3-4 from persistent, undifferentiated metanephric blastema; radical nephrectomy is the backbone, with nephron-sparing surgery reserved for bilateral disease to preserve renal function."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "WT1 is essential for podocyte function, so the WT1 mutations that cause Wilms tumor also cause glomerular disease: Denys-Drash (missense) brings diffuse mesangial sclerosis and infantile nephrotic syndrome, while Frasier (KTS splice) causes focal segmental glomerulosclerosis."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The commonest molecular change in Wilms tumor (~75%) is loss of imprinting at 11p15 that doubles IGF2 dosage; excess IGF2 signals through IGF1R to PI3K-AKT-mTOR, driving nephroblast proliferation — the same locus whose disruption underlies Beckwith-Wiedemann overgrowth."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Wilms tumor and rhabdomyosarcoma are both embryonal childhood cancers of arrested development — Wilms from kidney blastema, RMS from myogenic precursors — sharing a key driver: 11p15.5 loss of imprinting doubles IGF2, feeding an IGF1R-PI3K-AKT-mTOR loop in both."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Wilms tumor and neuroblastoma are the two classic malignant abdominal masses of young children (ages 1-4): Wilms is an intrarenal nephroblastoma rarely crossing midline; neuroblastoma is an adrenal/sympathetic tumor that secretes catecholamines and often crosses."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Anaplastic (unfavorable-histology) Wilms tumor is defined by TP53 mutation, driving chemoresistance and worse prognosis; germline TP53 (Li-Fraumeni) is occasionally found with anaplasia or family history — linking Wilms to the p53-driven childhood cancer-predisposition spectrum."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Wilms tumor and renal cell carcinoma are the kidney cancers of childhood versus adulthood: Wilms (nephroblastoma) is an embryonal tumor of nephron precursors curable with surgery and chemo, while RCC arises from mature tubular epithelium in adults, driven by VHL/HIF."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Wilms tumor's blastemal component enters the small-round-blue-cell differential with Ewing sarcoma: both are pediatric tumors of primitive cells, but Wilms is triphasic (blastema/epithelium/stroma) with WT1 changes while Ewing is EWSR1-FLI1-driven."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Wilms tumor and retinoblastoma are paradigm embryonal childhood cancers fitting Knudson's two-hit model: bilateral Wilms (often WT1-linked) parallels heritable bilateral retinoblastoma—germline loss of one suppressor allele plus a somatic second hit drives early tumors."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is part of risk-adapted Wilms tumor cure: flank or whole-abdomen photon radiation is added for higher-stage or unfavorable-histology disease after nephrectomy and chemotherapy, contributing to Wilms' high cure rate."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Wilms tumor and rhabdoid tumors are distinct pediatric renal/CNS cancers: classic Wilms is a WT1-related nephroblastoma with good prognosis, while malignant rhabdoid tumor of the kidney (and CNS ATRT) is a SMARCB1-deficient, far more aggressive tumor."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Wilms tumor and medulloblastoma are both embryonal childhood tumors arising from developmental precursors: Wilms from metanephric blastema (WT1/Wnt), medulloblastoma from cerebellar progenitors—different organs, but both recapitulate arrested embryonic development."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "Wilms tumor is partly a Wnt-driven cancer: beta-catenin (CTNNB1) activating mutations, often with WT1 loss, derail the kidney's developmental Wnt signaling so nephron precursors keep proliferating—turning arrested fetal kidney tissue into the embryonal tumor."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Wilms tumor metastasizes characteristically to the lung: it spreads hematogenously to produce pulmonary nodules, so chest imaging is part of staging—yet even metastatic Wilms is often cured, an unusually favorable pediatric cancer."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Wilms tumor links to several developmental cancer syndromes including DICER1: beyond WT1, predispositions like DICER1 and Beckwith-Wiedemann raise risk, so bilateral or syndromic Wilms prompts genetic evaluation and tailored surveillance."
---

# Wilms Tumor

## Overview

**Wilms tumor (nephroblastoma)** is the most common renal malignancy of childhood and the fourth most common pediatric cancer overall, arising from persistent embryonic metanephric blastema that fails to undergo normal differentiation. Wilms tumor is one of pediatric oncology's greatest success stories — with overall survival exceeding **90%** through decades of cooperative group trials (NWTS/COG in North America; SIOP in Europe) that established risk-adapted chemotherapy regimens [^dome-2015-wilms]. The tri-phasic histology (blastemal, epithelial, stromal components) reflects arrested renal embryogenesis; the genetic landscape is defined by **WT1 mutations** in 10-15%, **CTNNB1 (β-catenin)** in 15-20%, **WTX (AMER1)** in 15-20%, **IGF2 overexpression** in 75% (via 11p15 imprinting loss), and **miRNA processing gene mutations (DROSHA, DGCR8)** in 5-10%. Histological risk stratification — into **favorable histology (FH, ~90%)** and **unfavorable/anaplastic histology (UH, ~10%)** — remains the most powerful prognostic determinant, with TP53 mutations driving anaplastic change and resistance to standard chemotherapy [^dix-2006-arenl0002].

**Epidemiology:**
- Incidence: ~650 cases/year USA; ~9,000 globally/year
- Peak age: 3-4 years; rare after age 8; rare in adults
- ~10% bilateral (synchronous or metachronous); bilateral → higher likelihood of germline predisposition (WAGR, Beckwith-Wiedemann syndrome)
- Sex: slight female predominance; sporadic left-to-right equal; syndrome-associated may differ
- Race: slight higher incidence in African American children; similar outcomes with modern treatment

## Structure

### Molecular and genetic landscape

**Driver pathways:**

**11p15 imprinting (IGF2/H19 locus, ~75%):**
Normal 11p15: Maternal allele (H19 expressed, IGF2 silenced); Paternal allele (H19 silenced, IGF2 expressed). Loss of imprinting (LOI) on maternal allele → biallelic IGF2 expression → IGF2 overproduction → IGF1R-PI3K-AKT-mTOR → proliferation. This is the most common molecular change; associated with Beckwith-Wiedemann syndrome (organomegaly, macroglossia, omphalocele, ~5-10% Wilms risk).

**WT1 pathway (intralobar nephrogenic rests, ~10-15%):**
WT1 loss-of-function → impaired kidney differentiation → persistent intralobar nephrogenic rests (ILNR) → secondary CTNNB1 (WNT pathway) mutations → blastemal-predominant Wilms tumor. WT1+CTNNB1 co-mutation is the canonical "two-hit" model for a subset of Wilms tumor.

**miRNA processing (DROSHA/DGCR8, ~5-10%):**
DROSHA (microprocessor complex subunit) hotspot mutation E1147K; DGCR8 mutations → impaired primary miRNA processing → global mature miRNA reduction → derepression of many oncogenic targets including LIN28 (miRNA suppressor → promotes stem cell state → IGF2/mTOR activation → nephroblastic proliferation). DROSHA E1147K is acquired somatically; associated with blastemal-predominant histology and relapse risk.

**Other recurrent alterations:**
- WTX/AMER1 (X-linked APC-like gene, WNT negative regulator): ~15-20%; truncating mutations → WNT activation; predominantly in boys (hemizygous); independently causes osteopathia striata with cranial sclerosis when germline
- SIX1/SIX2 (homeobox TF, metanephric progenitors): ~5-10%; frameshift hotspot Q177R; associated with epithelial-predominant Wilms tumor; good prognosis
- TP53 mutations: ~70% of anaplastic (unfavorable histology) Wilms tumor; extremely rare in FH Wilms; acquired → signal for impending anaplasia

**Chromosomal changes:**
- 1q gain: most common cytogenetic abnormality (~30%); adverse prognostic factor in FH Wilms tumor
- 16q loss: ~15%; independent adverse factor (NWTS-5)
- 1p loss: ~10%; adverse factor
- 11p15 LOH (paternal UPD/maternal deletion): ~40%; correlates with IGF2 overexpression

### Histological classification

**Favorable histology (FH, ~90%):** Tri-phasic nephroblastoma (blastemal + epithelial + stromal); or predominantly one component without anaplasia; nuclear uniformity; good prognosis with standard treatment.

**Unfavorable histology (UH) / Anaplastic Wilms (~10%):**
- **Diffuse anaplasia (DAWT):** Any anaplastic focus beyond a single foci, or any anaplasia in unfavorable location (extrarenal, invasive); characterized by extreme nuclear enlargement (≥3× adjacent nuclei), hyperchromatic, multipolar mitoses; TP53 mutations ~70%; prognosis poor (Stage IV DAWT 4-year OS ~33%)
- **Focal anaplasia (FAWT):** Single circumscribed anaplastic focus, sharply demarcated; TP53 mutations lower rate; prognosis intermediate between FH and DAWT

**Blastemal-predominant post-chemotherapy (SIOP classification):**
After SIOP neoadjuvant chemotherapy, blastemal cells are treatment-resistant cells; >65% blastemal component post-chemotherapy = "blastemal-type" → high-risk regimen even without anaplasia; analogous to adverse outcome DROSHA-mutant tumors.

## Function

### Normal nephrogenesis and WT1

Kidney development proceeds through three waves of induction: pronephros → mesonephros → metanephros (permanent kidney). Metanephric mesenchyme (MM) expresses WT1, PAX2, SIX2 → receives ureteric bud signals (WNT9B, WNT4) → MM undergoes mesenchymal-to-epithelial transition (MET) → forms nephrons (glomeruli + tubules). WT1 maintains the MM pool while allowing controlled differentiation; WT1 loss → MM fails to differentiate → forms nephrogenic rests → risk of Wilms tumor.

## Pathology

### Predisposition syndromes

**WAGR syndrome (11p13 deletion):**
WT1 + PAX6 deletion; ~30% lifetime Wilms tumor risk; aniridia (PAX6 deletion); genitourinary malformalities; intellectual disability; annual abdominal ultrasound surveillance until age 8-10.

**Denys-Drash syndrome (WT1 ZF3/4 missense, R394W/Q):**
~90% Wilms tumor risk; diffuse mesangial sclerosis → nephrotic syndrome in infancy; male pseudohermaphroditism (46,XY with ambiguous genitalia); diagnosis → bilateral prophylactic nephrectomy recommended by age 2 after gonadal histology clarification.

**Frasier syndrome (WT1 KTS splice mutations):**
+KTS/-KTS ratio disruption → focal segmental glomerulosclerosis → nephrotic syndrome; gonadoblastoma in 46,XY; low Wilms tumor risk (unlike Denys-Drash); managed conservatively.

**Beckwith-Wiedemann syndrome (11p15 imprinting):**
Macroglossia, omphalocele, organomegaly, hemihypertrophy; ~5-10% Wilms tumor (bilateral more common); abdominal ultrasound every 3 months until age 8.

**Isolated hemihypertrophy:** Wilms tumor risk ~5%; screening recommended.

### Staging (COG/NWTS, upfront nephrectomy)

| Stage | Definition | 4-year OS (FH) |
|-------|-----------|----------------|
| I | Confined to kidney, completely resected | ~99% |
| II | Extends beyond kidney, completely resected | ~98% |
| III | Residual tumor (local spillage, positive margins, abdominal nodes, biopsy) | ~95% |
| IV | Hematogenous metastases (lung, liver, bone) | ~85% |
| V | Bilateral | ~80% (depends on salvage) |

**SIOP staging (post-chemotherapy):** Uses similar criteria but applied after neoadjuvant chemotherapy; necrosis/blastemal classification differs from COG upfront system.

### Treatment (COG approach — upfront nephrectomy)

**Standard-risk FH (Stage I-II, no 1q gain or 16q LOH):**
- Radical nephrectomy → actinomycin D + vincristine × 18 weeks (Regimen EE-4A or DD-4A)
- No radiation; 4-year EFS ~95%

**Higher-risk FH (Stage III, bilateral, 1q gain, or Stage IV):**
- Radical nephrectomy (for Stage I-III) → actinomycin D + vincristine + doxorubicin × 24 weeks (Regimen DD-4A/M)
- ± Flank radiation (Stage III local, Stage IV incomplete pulmonary response)
- Stage IV pulmonary metastases: 2 chemotherapy cycles → assess lung response: if complete → omit lung RT; if incomplete → whole-lung RT 12 Gy [^dix-2006-arenl0002]
- 4-year EFS ~87-90%

**Unfavorable histology / Anaplastic Wilms:**
- Focal anaplasia: DD-4A + flank RT (Stage II+)
- Diffuse anaplasia: Regimen UH-1/I (vincristine, actinomycin D, doxorubicin, cyclophosphamide, etoposide, carboplatin) + RT; 4-year EFS ~33% (Stage IV DAWT)
- TP53-mutant DAWT: Very high risk; allo-SCT considered after relapse

**Bilateral Wilms tumor (Stage V):**
- Biopsy first → neoadjuvant chemotherapy × 6 weeks (actinomycin D + vincristine) → reassess bilaterally → nephron-sparing surgery (bilateral partial nephrectomy to preserve renal function) → final staging → further chemotherapy ± RT
- Goal: preserve maximum renal parenchyma; avoid dialysis-dependent chronic kidney disease
- Genetic testing strongly recommended for bilateral cases

**Relapsed Wilms tumor:**
- Prior chemotherapy determines salvage: if previously treated with 2-drug → ICE (ifosfamide, carboplatin, etoposide) or VDC/IE (vincristine+doxorubicin+cyclophosphamide/ifosfamide+etoposide)
- High-dose chemotherapy + autologous SCT for multiply relapsed FH
- Irinotecan+vincristine: active in salvage; ORR ~40-60%
- Everolimus (mTOR), bevacizumab (VEGF): Studied in refractory disease; limited single-agent activity

**SIOP approach (European — neoadjuvant chemotherapy):**
Neoadjuvant actinomycin D + vincristine × 4 weeks (Stage I-III) or + doxorubicin × 6 weeks (Stage IV) → nephrectomy → pathology-based staging + blastemal typing → risk-adapted consolidation; advantage: tumor downstaging (easier surgery, less spillage); disadvantage: loss of upfront pathology staging.

### Long-term effects

Wilms tumor survivors face late effects proportional to treatment intensity:
- **Renal insufficiency:** Single kidney (after radical nephrectomy) → lifetime GFR monitoring; 30-year CKD risk ~15%; bilateral Wilms → higher risk; avoid nephrotoxic drugs
- **Cardiac toxicity:** Doxorubicin → cardiomyopathy; flank RT → cardiac RT if large field; cardiac surveillance echocardiography at 5-year intervals
- **Secondary malignancies:** Abdominal RT → risk of sarcoma, breast cancer (if chest field); doxorubicin → secondary AML (rare)
- **Musculoskeletal:** Flank RT → scoliosis (if field encompasses spine growth plates); asymmetric muscle atrophy
- **Reproductive:** Gonadal irradiation → infertility; oophoropexy before pelvic RT in girls

## Connections

- `connects-to` → **[WT1](../../03-molecular/wt1/README.md)** — WT1 mutations occur in ~10-15% sporadic Wilms tumor and are near-universal in WAGR and Denys-Drash syndromes; WT1+CTNNB1 co-mutation → blastemal-predominant Wilms from intralobar nephrogenic rests; WT1 is required for nephron formation from metanephric blastema.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — CTNNB1 activating mutations occur in ~15-20% Wilms tumor, co-occurring with WT1 mutations; nuclear β-catenin marks the blastemal component; WNT activation promotes blastema self-renewal and prevents epithelial differentiation; WNT inhibitors studied preclinically.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — TP53 mutations occur in ~70% of diffuse anaplastic Wilms (unfavorable histology); anaplasia is the strongest adverse prognostic factor; TP53 drives resistance to standard chemotherapy; anaplastic WT requires alkylator-based intensification (cyclophosphamide/etoposide).
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — IGF2 overexpression (~75% Wilms tumor via 11p15 imprinting loss) → IGF1R → PI3K-AKT-mTOR → proliferation; everolimus explored in relapsed Wilms; DROSHA/DGCR8 mutations impair miRNA biogenesis → mTOR derepression.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Wilms tumor (nephroblastoma) is the most common childhood kidney cancer, arising at age 3-4 from persistent, undifferentiated metanephric blastema; radical nephrectomy is the backbone, with nephron-sparing surgery reserved for bilateral disease to preserve renal function.
- `connects-to` → **[Podocyte](../../04-cellular/podocyte/README.md)** — WT1 is essential for podocyte function, so the WT1 mutations that cause Wilms tumor also cause glomerular disease: Denys-Drash (missense) brings diffuse mesangial sclerosis and infantile nephrotic syndrome, while Frasier (KTS splice) causes focal segmental glomerulosclerosis.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The commonest molecular change in Wilms tumor (~75%) is loss of imprinting at 11p15 that doubles IGF2 dosage; excess IGF2 signals through IGF1R to PI3K-AKT-mTOR, driving nephroblast proliferation — the same locus whose disruption underlies Beckwith-Wiedemann overgrowth.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Wilms tumor and rhabdomyosarcoma are both embryonal childhood cancers of arrested development — Wilms from kidney blastema, RMS from myogenic precursors — sharing a key driver: 11p15.5 loss of imprinting doubles IGF2, feeding an IGF1R-PI3K-AKT-mTOR loop in both.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Wilms tumor and neuroblastoma are the two classic malignant abdominal masses of young children (ages 1-4): Wilms is an intrarenal nephroblastoma rarely crossing midline; neuroblastoma is an adrenal/sympathetic tumor that secretes catecholamines and often crosses.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Anaplastic (unfavorable-histology) Wilms tumor is defined by TP53 mutation, driving chemoresistance and worse prognosis; germline TP53 (Li-Fraumeni) is occasionally found with anaplasia or family history — linking Wilms to the p53-driven childhood cancer-predisposition spectrum.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Wilms tumor and renal cell carcinoma are the kidney cancers of childhood versus adulthood: Wilms (nephroblastoma) is an embryonal tumor of nephron precursors curable with surgery and chemo, while RCC arises from mature tubular epithelium in adults, driven by VHL/HIF.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Wilms tumor's blastemal component enters the small-round-blue-cell differential with Ewing sarcoma: both are pediatric tumors of primitive cells, but Wilms is triphasic (blastema/epithelium/stroma) with WT1 changes while Ewing is EWSR1-FLI1-driven.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Wilms tumor and retinoblastoma are paradigm embryonal childhood cancers fitting Knudson's two-hit model: bilateral Wilms (often WT1-linked) parallels heritable bilateral retinoblastoma—germline loss of one suppressor allele plus a somatic second hit drives early tumors.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is part of risk-adapted Wilms tumor cure: flank or whole-abdomen photon radiation is added for higher-stage or unfavorable-histology disease after nephrectomy and chemotherapy, contributing to Wilms' high cure rate.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Wilms tumor and rhabdoid tumors are distinct pediatric renal/CNS cancers: classic Wilms is a WT1-related nephroblastoma with good prognosis, while malignant rhabdoid tumor of the kidney (and CNS ATRT) is a SMARCB1-deficient, far more aggressive tumor.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Wilms tumor and medulloblastoma are both embryonal childhood tumors arising from developmental precursors: Wilms from metanephric blastema (WT1/Wnt), medulloblastoma from cerebellar progenitors—different organs, but both recapitulate arrested embryonic development.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — Wilms tumor is partly a Wnt-driven cancer: beta-catenin (CTNNB1) activating mutations, often with WT1 loss, derail the kidney's developmental Wnt signaling so nephron precursors keep proliferating—turning arrested fetal kidney tissue into the embryonal tumor.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Wilms tumor metastasizes characteristically to the lung: it spreads hematogenously to produce pulmonary nodules, so chest imaging is part of staging—yet even metastatic Wilms is often cured, an unusually favorable pediatric cancer.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Wilms tumor links to several developmental cancer syndromes including DICER1: beyond WT1, predispositions like DICER1 and Beckwith-Wiedemann raise risk, so bilateral or syndromic Wilms prompts genetic evaluation and tailored surveillance.

[^dome-2015-wilms]: Dome JS, Graf N, Geller JI, et al. Advances in Wilms tumor treatment and biology: progress through international collaboration. *J Clin Oncol.* 2015;33(27):2999-3007. [doi:10.1200/JCO.2015.62.1888](https://doi.org/10.1200/JCO.2015.62.1888) · [PubMed 26261251](https://pubmed.ncbi.nlm.nih.gov/26261251/)
[^dix-2006-arenl0002]: Dix DB, Bhatt SM, Geller JI, et al. Treatment of Stage IV favorable histology Wilms tumor with incomplete lung metastasis response after chemotherapy: a report from Children's Oncology Group Study AREN0533. *J Clin Oncol.* 2018;36(16):1564-1570. [doi:10.1200/JCO.2017.77.1877](https://doi.org/10.1200/JCO.2017.77.1877) · [PubMed 29584550](https://pubmed.ncbi.nlm.nih.gov/29584550/)
