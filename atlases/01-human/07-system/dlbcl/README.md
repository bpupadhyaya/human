---
schema: human-scale-entry/v1
id: dlbcl
name: Diffuse Large B-Cell Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common aggressive B-cell lymphoma (30% of NHL); GCB subtype driven by t(14;18)/BCL-2 and BCR-PI3K; ABC subtype by MYD88/CD79B/NF-κB. R-CHOP is frontline; CAR-T (axi-cel, liso-cel) and bispecifics (epcoritamab, glofitamab) are approved in relapsed/refractory DLBCL."
aliases: ["DLBCL", "diffuse large B-cell lymphoma", "DLBCL NOS", "large B-cell lymphoma", "aggressive NHL", "LBCL"]
sources:
  - id: coiffier-2002-rchop
    type: peer-reviewed
    cite: "Coiffier B, Lepage E, Brière J, et al. CHOP chemotherapy plus rituximab compared with CHOP alone in elderly patients with diffuse large-B-cell lymphoma. N Engl J Med. 2002;346(4):235-242."
    doi: "10.1056/NEJMoa011795"
    pmid: "11807147"
    url: "https://doi.org/10.1056/NEJMoa011795"
  - id: neelapu-2017-axicel
    type: peer-reviewed
    cite: "Neelapu SS, Locke FL, Bartlett NL, et al. Axicabtagene ciloleucel CAR T-cell therapy in refractory large B-cell lymphoma. N Engl J Med. 2017;377(26):2531-2544."
    doi: "10.1056/NEJMoa1707447"
    pmid: "29226797"
    url: "https://doi.org/10.1056/NEJMoa1707447"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "ABC-DLBCL is driven by constitutive NF-κB via MYD88 L265P → IRAK4 → BTK and CD79B mutation → BCR-NF-κB; ibrutinib + R-CHOP (PHOENIX trial) failed in unselected DLBCL but active in MYD88-mutant/non-GCB DLBCL; zanubrutinib + R-CHOP in DLBCL under investigation."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "GCB-DLBCL: t(14;18) → BCL-2 overexpression → apoptosis block; venetoclax + R-CHOP (POLARIX data secondary) in BCL-2-high GCB-DLBCL under study; double-hit lymphoma (MYC + BCL-2) → venetoclax + dose-adjusted EPOCH-R; BCL-2 IHC ≥50% correlates with inferior R-CHOP outcome."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC rearrangement in ~10% of DLBCL; MYC + BCL-2 rearrangement = double-hit (HGBL-DH) → R-CHOP inferior; DA-EPOCH-R or consolidative CAR-T preferred; MYC protein >40% by IHC is independent prognostic marker; c-MYC amplification (without rearrangement) has intermediate prognosis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "DLBCL expresses PD-L1 in ~20-40%; pembrolizumab approved for relapsed/refractory primary mediastinal large B-cell lymphoma (PMBCL) — a CD20+/PD-L1-high subtype with 9p24 amplification; PD-1 blockade + rituximab combinations under study in follicular and DLBCL histologies."
---

# Diffuse Large B-Cell Lymphoma

## Overview

**Diffuse Large B-Cell Lymphoma (DLBCL)** is the most common aggressive lymphoma in adults, comprising ~30% of all non-Hodgkin lymphomas (NHL) with ~25,000 new cases per year in the United States. DLBCL is defined histologically by large, diffusely growing B-lymphoid cells that express B-cell markers (CD19, CD20, CD79a, PAX5) and have a proliferative fraction (Ki-67) typically >40%. With standard R-CHOP therapy, approximately 60-70% of patients are cured — a triumph of combined chemo-immunotherapy — but the ~30-40% who relapse have historically had poor outcomes [^coiffier-2002-rchop].

**Epidemiology:**
- Incidence: ~7-8/100,000 per year
- Median age: ~64 years; slight male predominance
- Risk factors: immunosuppression (HIV, organ transplant → PTLD), autoimmune disease (Sjögren's, RA, SLE), EBV infection (EBV+ DLBCL NOS), prior indolent lymphoma transformation (Richter transformation in CLL, transformation of FL)

**Key clinical features:**
- Rapidly growing lymphadenopathy (often weeks); B symptoms (fever, night sweats, weight loss) in ~30%
- Extranodal involvement common: GI tract (most common), CNS, testis, bone marrow, skin
- **Bulky disease** (≥10 cm): Adverse prognosis; consolidative radiotherapy considered
- International Prognostic Index (IPI): Age >60, ECOG PS ≥2, elevated LDH, >1 extranodal site, Ann Arbor stage III-IV → 5-year OS from 37% (high-risk) to 94% (low-risk) with R-CHOP

## Structure

### Molecular classification

**Cell of origin (COO):**
Gene expression profiling (GEP; NanoString-based Lymph2Cx assay) classifies DLBCL into two major subtypes based on differentiation state of the cell of origin:

**GCB (germinal center B-cell, ~50%):**
- Resembles germinal center B cells
- Genomic features: t(14;18)/BCL-2 rearrangement (~30%), EZH2 mutation (~20%), CREBBP mutation (~40%), KMT2D mutation (~30%), SGK1 mutation
- Better prognosis with R-CHOP vs. ABC (5-year OS ~75%)
- BCR-PI3K dependency; relatively lower NF-κB activity

**ABC (activated B-cell, ~30%):**
- Resembles post-germinal center, plasmablastic differentiation stage
- Genomic features: MYD88 L265P (~30%), CD79B mutation (Y196 "ITAM hotspot", ~20%), CARD11 mutation (~10%), TNFAIP3/A20 deletion (~20%)
- Constitutive NF-κB → BCL-XL, FLIP, IRF4 → survival
- Worse prognosis with standard R-CHOP (5-year OS ~55%)
- Potential benefit of BTK inhibition (ibrutinib, zanubrutinib) in MYD88+/CD79B+ dual mutation

**Unclassified (GCB/ABC, ~15-20%):** Intermediate characteristics

**Newly recognized DLBCL entities (WHO 2022 / ICC 2022):**
- **DLBCL, NOS** (not otherwise specified): The majority
- **High-grade B-cell lymphoma with MYC and BCL-2 rearrangements (HGBL-DH):** Double-hit; distinct entity
- **EBV+ DLBCL, NOS:** EBV-driven; older/immunocompromised patients; more aggressive
- **Primary DLBCL of the CNS (PCNSL):** CD10−, BCL-6+, MUM1+; high MYD88; high-dose methotrexate-based regimens
- **Primary mediastinal large B-cell lymphoma (PMBCL):** Mediastinal origin; JAK-STAT and 9p24 amplification → PD-L1 high; pembrolizumab approved

### Genetic landscape

**Most frequently mutated genes in DLBCL NOS:**
- KMT2D (~35%), CREBBP (~30%), DDX3X (~20%), EZH2 (~20%), BCL-2 (~25% rearranged), TP53 (~20%), CD79B (~20%), MYD88 (~30% overall, enriched in ABC), BCL-6 rearrangement (~35% overall)

**MYC biology in DLBCL:**
- MYC rearrangement (Ig-MYC) in ~10% — the IGH-MYC t(8;14) is most common, also IGL-MYC, IGK-MYC
- MYC co-rearrangement with BCL-2: "double-hit" → high-grade B-cell lymphoma (HGBL); HGBL-DH median OS ~6-12 months with R-CHOP → requires intensified or CAR-T approaches
- MYC co-rearrangement with BCL-2 + BCL-6: "triple-hit" (HGBL-TH)
- MYC protein overexpression (without rearrangement) in ~30% of DLBCL (copy number gain, post-transcriptional); intermediate prognostic impact vs. rearranged MYC

## Function

### Normal diffuse large B-cell biology

DLBCL is an aggressive malignancy of mature B cells. The normal equivalents are large germinal center B cells (centroblasts) for GCB-DLBCL and post-GC B cells (plasmablasts) for ABC-DLBCL. GCB-DLBCL bears the imprint of somatic hypermutation, class switch recombination, and t(14;18) — events that normally occur in germinal centers.

### Tumor microenvironment (TME)

**Immune infiltration in DLBCL:**
- **T-cell inflamed (hot) TME:** CD8+ T cells, PD-1+ T cells → associated with higher PD-L1 and potential immunotherapy response; seen more in EBV+ DLBCL and PMBCL
- **Immune-excluded TME:** T cells present but excluded from tumor nests; poor prognosis; common in ABC-DLBCL
- **Immunologically cold TME:** Low lymphocyte infiltration; worst prognosis

**Macrophage polarization:**
- Tumor-associated macrophages (TAMs) in DLBCL; M2-polarized TAMs (CD163+) → immunosuppression; high TAM density correlates with inferior R-CHOP outcome in some analyses
- Lenalidomide + R-CHOP → macrophage repolarization (ROBUST trial for ABC-DLBCL: no significant improvement in primary endpoint but ongoing)

## Pathology

### Diagnosis and staging

**Excisional biopsy required:** Core needle biopsy acceptable if excisional not feasible; fine needle aspirate is insufficient (architectural information needed for subtyping)

**Pathological workup:**
- Morphology: Large lymphoid cells, diffuse pattern, mitoses, necrosis
- Immunohistochemistry: CD20+, CD19+, CD79a+, PAX5+; BCL-2 (% positivity), BCL-6 (GCB marker), CD10 (GCB marker), MUM1/IRF4 (ABC marker), MYC (% positivity)
- FISH: MYC, BCL-2, BCL-6 rearrangements — required to identify HGBL-DH/TH
- COO by GEP or IHC algorithm (Hans algorithm: CD10/BCL-6/MUM1)
- PET/CT for staging (Ann Arbor); Deauville score for response assessment
- Bone marrow biopsy or PET-based marrow assessment

**Response criteria (Lugano 2014):**
- Complete metabolic response (CMR): Deauville 1-3 at end-of-treatment PET
- Partial metabolic response (PMR): Deauville 4-5 with ≥50% decrease in SUV
- Progressive disease (PD): Deauville 4-5 + new lesions

### Treatment

**Frontline (R-CHOP):**
- Rituximab 375 mg/m² + CHOP (cyclophosphamide, doxorubicin, vincristine, prednisone); 6 cycles every 21 days [^coiffier-2002-rchop]
- Cure rate ~60-70% (all-comer DLBCL); 5-year EFS ~55-60%
- **Pola-R-CHP** (polatuzumab vedotin-piiq + R-CHP, without vincristine): POLARIX trial → superior 2-year PFS 76.7% vs. 70.2% for R-CHOP; FDA approved 2023 for previously untreated DLBCL (excluding HGBL); new standard option
- **High-intermediate/high IPI + DLBCL:** CNS prophylaxis with intrathecal or high-dose methotrexate in high-risk anatomic sites (testis, paranasal sinus, epidural, bone marrow)

**Relapsed/Refractory (R/R) DLBCL (≥2nd line):**
- **CAR-T cell therapy:**
  - Axicabtagene ciloleucel (axi-cel, Yescarta): CD19-directed; ZUMA-1 → 52% CR in R/R DLBCL; approved 2017 [^neelapu-2017-axicel]
  - Lisocabtagene maraleucel (liso-cel, Breyanzi): CD19-directed 1:1 CD4:CD8 ratio; TRANSCEND → 53% CR
  - Tisagenlecleucel (tisa-cel, Kymriah): CD19-directed; JULIET → 40% CR
  - **2nd-line CAR-T:** ZUMA-7 (axi-cel) and TRANSFORM (liso-cel) → superior to salvage chemo + ASCT in R/R DLBCL ≤12 months from frontline; EFS benefit → axi-cel now preferred 2nd-line option if early relapse
- **CD20×CD3 bispecific antibodies:**
  - Epcoritamab (subcutaneous): CR 39%; approved for R/R DLBCL (3rd-line+)
  - Glofitamab (obinutuzumab pre-treated): CR 39%; fixed duration; approved 2023
- **Loncastuximab tesirine (Zynlonta):** CD19-directed ADC (PBD warhead); approved for R/R DLBCL
- **Tafasitamab + lenalidomide (L-MIND trial):** CR 43% in transplant-ineligible R/R DLBCL; approved 2020
- **Salvage chemo + ASCT:** R-ICE, R-DHAP, R-ESHAP → if chemosensitive; standard for 2nd-line in late-relapsing (>12 months) fit patients

**Special entities:**
- PCNSL: HD-methotrexate + rituximab induction; consolidation with WBRT or HD-thiotepa-based ASCT; maintenance rituximab
- PMBCL: R-DA-EPOCH (BV-CHP under study); pembrolizumab in R/R PMBCL (approved)
- HGBL-DH: DA-EPOCH-R + venetoclax; or CAR-T consolidation after induction — no definitive superior frontline regimen established

## Connections

- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — ABC-DLBCL is driven by constitutive NF-κB via MYD88 L265P → IRAK4 → BTK and CD79B mutation → BCR-NF-κB; ibrutinib + R-CHOP (PHOENIX trial) failed in unselected DLBCL but active in MYD88-mutant/non-GCB DLBCL; zanubrutinib + R-CHOP in DLBCL under investigation.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — GCB-DLBCL: t(14;18) → BCL-2 overexpression → apoptosis block; venetoclax + R-CHOP (POLARIX data secondary) in BCL-2-high GCB-DLBCL under study; double-hit lymphoma (MYC + BCL-2) → venetoclax + dose-adjusted EPOCH-R; BCL-2 IHC ≥50% correlates with inferior R-CHOP outcome.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC rearrangement in ~10% of DLBCL; MYC + BCL-2 rearrangement = double-hit (HGBL-DH) → R-CHOP inferior; DA-EPOCH-R or consolidative CAR-T preferred; MYC protein >40% by IHC is independent prognostic marker; c-MYC amplification (without rearrangement) has intermediate prognosis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — DLBCL expresses PD-L1 in ~20-40%; pembrolizumab approved for relapsed/refractory primary mediastinal large B-cell lymphoma (PMBCL) — a CD20+/PD-L1-high subtype with 9p24 amplification; PD-1 blockade + rituximab combinations under study in follicular and DLBCL histologies.

[^coiffier-2002-rchop]: Coiffier B, Lepage E, Brière J, et al. CHOP chemotherapy plus rituximab compared with CHOP alone in elderly patients with diffuse large-B-cell lymphoma. *N Engl J Med.* 2002;346(4):235-242. [doi:10.1056/NEJMoa011795](https://doi.org/10.1056/NEJMoa011795) · [PubMed 11807147](https://pubmed.ncbi.nlm.nih.gov/11807147/)
[^neelapu-2017-axicel]: Neelapu SS, Locke FL, Bartlett NL, et al. Axicabtagene ciloleucel CAR T-cell therapy in refractory large B-cell lymphoma. *N Engl J Med.* 2017;377(26):2531-2544. [doi:10.1056/NEJMoa1707447](https://doi.org/10.1056/NEJMoa1707447) · [PubMed 29226797](https://pubmed.ncbi.nlm.nih.gov/29226797/)
