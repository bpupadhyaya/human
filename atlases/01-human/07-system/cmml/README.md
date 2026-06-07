---
schema: human-scale-entry/v1
id: cmml
name: Chronic Myelomonocytic Leukemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic myelomonocytic leukemia (CMML) is an MDS/MPN overlap with persistent monocytosis; TET2 (~60%) and SRSF2 (~45%) are the dominant mutations; PDGFRB rearrangements → imatinib-responsive CMML-like disease. Azacitidine is standard; allo-SCT is the only cure; OS ~2 years."
aliases: ["CMML", "chronic myelomonocytic leukemia", "CMML-0", "CMML-1", "CMML-2", "myelodysplastic/myeloproliferative neoplasm", "MDS/MPN overlap", "proliferative CMML", "myelodysplastic CMML"]
sources:
  - id: itzykson-2013-cmml-prognosis
    type: peer-reviewed
    cite: "Itzykson R, Kosmider O, Renneville A, et al. Prognostic score including gene mutations in chronic myelomonocytic leukemia. J Clin Oncol. 2013;31(19):2428-2436."
    doi: "10.1200/JCO.2012.47.3314"
    pmid: "23690417"
    url: "https://doi.org/10.1200/JCO.2012.47.3314"
  - id: patnaik-2022-cmml-review
    type: peer-reviewed
    cite: "Patnaik MM, Tefferi A. Chronic myelomonocytic leukemia: 2022 update on diagnosis, risk stratification and management. Am J Hematol. 2022;97(3):352-372."
    doi: "10.1002/ajh.26457"
    pmid: "34958140"
    url: "https://doi.org/10.1002/ajh.26457"
cross_links:
  - target: 01-human/03-molecular/srsf2
    relation: connects-to
    note: "SRSF2 P95H in ~45% of CMML; most common splicing factor mutation; co-occurs with TET2 (~60%) in the dominant CMML doublet; P95H alters CCNG ESE splicing → monocytic differentiation bias; SRSF2+TET2 knockin mice develop CMML-like disease with full penetrance."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A mutations in ~10% of CMML; DNMT3A is an early CHIP hit establishing pre-malignant HSC clones before SRSF2 or TET2 co-mutation; DNMT3A+TET2+SRSF2 triplet occurs in ~5% of CMML → aggressive progression; DNMT3A-CHIP → CMML progression rate ~1-2% per year."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS/NRAS mutations in ~15% of CMML; RAS activation → monocyte proliferation → MP-CMML phenotype (WBC >13×10⁹/L, splenomegaly, organomegaly); KRAS-mutant CMML is aggressive with poor HMA response; MEK inhibitor trametinib shows early activity in RAS-mutant CMML."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB promotes monocyte/macrophage survival in CMML; SRSF2/ASXL1 mutations dysregulate NF-κB pathway activity; ruxolitinib reduces cytokine-driven NF-κB signaling in MP-CMML → splenomegaly response ~40-50%; GM-CSF/M-CSF autocrine loops drive NF-κB in CMML monocytes."
---

# Chronic Myelomonocytic Leukemia

## Overview

**Chronic myelomonocytic leukemia (CMML)** is a rare clonal hematopoietic stem cell malignancy classified by the WHO as an **MDS/MPN overlap syndrome** — uniquely combining features of myelodysplastic syndromes (cytopenias, bone marrow dysplasia) and myeloproliferative neoplasms (leukocytosis, monocytosis, splenomegaly, organomegaly). The defining hallmark is **persistent peripheral blood monocytosis** (absolute monocyte count ≥0.5×10⁹/L AND monocytes ≥10% of WBC for ≥3 months) in the absence of a reactive cause. CMML affects ~3-4 per 100,000 adults/year (predominantly ages 65-75, male predominance 2:1), carries a median overall survival of ~2-3 years, and transforms to AML in ~15-30% of patients over 5 years. The molecular landscape of CMML is dominated by mutations in DNA methylation genes (TET2 ~60%, DNMT3A ~10%, IDH1/2 ~10%), splicing factors (SRSF2 ~45%, SF3B1 ~5%), and chromatin regulators (ASXL1 ~40%) — a convergence of epigenetic and RNA processing dysregulation driving monocytic clonal expansion. Critically, ~10% of CMML-like presentations harbor **PDGFRB rearrangements** (or PDGFRA, FGFR1) → these are classified separately (MPN with eosinophilia and tyrosine kinase fusions) and are exquisitely sensitive to **imatinib** [^patnaik-2022-cmml-review] [^itzykson-2013-cmml-prognosis].

**Epidemiology and risk factors:**
- Incidence: ~1,100-1,200 cases/year USA; prevalence ~6,000; ~3-4 per 100,000 adults; median age 70-75 years; male:female ~2:1
- Risk factors: Prior chemotherapy (especially alkylating agents → therapy-related MDS/CMML); radiation; CHIP (especially DNMT3A, TET2, SRSF2 CHIP → CMML evolution); no specific environmental risk factors identified beyond those for MDS

**WHO 2022 classification of CMML:**
- **CMML-0:** <2% blasts in PB and <5% blasts in BM; lowest blast count class; lowest AML transformation risk
- **CMML-1:** 2-4% blasts in PB or 5-9% blasts in BM; intermediate risk
- **CMML-2:** 5-19% blasts in PB or 10-19% blasts in BM; OR Auer rods present; highest AML transformation risk (~30-50% at 2 years); treat as high-risk MDS or AML in some cases

**Proliferative (MP-CMML) vs. myelodysplastic (MD-CMML) subtypes:**
- **MD-CMML (WBC ≤13×10⁹/L):** Cytopenias dominant; myelodysplastic features prominent; splenomegaly mild/absent; HMA therapy preferred
- **MP-CMML (WBC >13×10⁹/L):** Monocytosis + leukocytosis dominant; splenomegaly common (in ~50-60%); KRAS/NRAS mutations enriched; ruxolitinib for splenomegaly control; hydroxyurea for cytoreduction

**Molecular landscape:**
- TET2: ~60% (most common; loss of 5-hydroxymethylcytosine → DNA hypermethylation → monocytic differentiation bias)
- SRSF2: ~45% (P95H hotspot; splicing dysregulation → monocytic fate)
- ASXL1: ~40% (PRC1.1 loss → H2AK119ub loss → aberrant HOX gene expression; poor prognosis)
- KRAS/NRAS: ~15% (RAS-MAPK → monocyte proliferation → MP-CMML phenotype)
- CBL: ~10% (E3 ubiquitin ligase; ring domain mutations → dominant negative → RAS activation)
- DNMT3A: ~10% (early epigenetic hit in CHIP → CMML progression)
- IDH1/2: ~8% (2-HG → TET2 inhibition → hypermethylation; enasidenib/ivosidenib active)
- EZH2: ~7% (PRC2 loss; adverse prognosis)
- TP53: ~5% (biallelic → ultra-high risk; rare in CMML vs. AML)
- SETBP1: ~15% (often co-mutated with ASXL1; poor prognosis; SB1-associated CMML type)

## Structure

### Bone marrow and peripheral blood findings

**Diagnostic criteria (WHO 2022):**
1. Persistent peripheral monocytosis: Absolute monocyte count ≥0.5×10⁹/L AND monocytes ≥10% of WBC for ≥3 months
2. Bone marrow dysplasia in ≥1 myeloid lineage (granulocytic, erythroid, megakaryocytic)
3. Blast count: PB <20%, BM <20%
4. No BCR-ABL1 fusion (CML must be excluded)
5. No PDGFRA, PDGFRB, FGFR1, or PCM1-JAK2 rearrangement → if present, classify as MPN with eosinophilia + RTK fusion → imatinib-sensitive
6. No PML-RARA or other AML-defining cytogenetics/fusions

**Flow cytometry diagnostic criteria:**
Monocytes: CD14+/CD16+ monocytes (non-classical + intermediate) >94% of total monocytes (in contrast to reactive monocytosis where these subsets are ~70-80%); high classical monocyte fraction is characteristic of reactive/infectious monocytosis; CMML monocytes are predominantly CD14+/CD16− classical monocytes (≥94% threshold).

**Cytogenetics:**
Normal karyotype in ~70% of CMML; abnormal in ~30%: trisomy 8 (~10%), monosomy 7/del(7q) (~10%), complex karyotype (~5%), del(20q), del(12p), del(5q); trisomy 8 and monosomy 7 are intermediate-adverse; del(17p)/monosomy 17 → TP53 loss; PDGFRB rearrangement: t(5;12)(q33;p13) → ETV6-PDGFRB fusion → eosinophilic CMML-like → imatinib 400 mg/day.

**Bone marrow biopsy/aspirate:**
Hypercellular (>70%) in MP-CMML; monocytic and granulocytic proliferation; dysplasia in ≥1 lineage; blast percentage (critical for CMML-0/1/2 classification); promonocytes (counted as blasts in CMML); plasmacytoid dendritic cell (pDC) proliferations may accompany CMML (blastic pDC neoplasm [BPDCN] may arise from CMML clones).

### Prognostic scoring systems

**CPSS (CMML-Specific Prognostic Scoring System, 2013):** [^itzykson-2013-cmml-prognosis]
Variables: WHO subtype (CMML-1/2), cytogenetic risk group (low/intermediate/high), RBC-transfusion dependence, WBC (≤13 vs. >13×10⁹/L). Scores: Low (0), Intermediate-1 (0.5-1), Intermediate-2 (1.5-2), High (≥2.5). Median OS: 84 vs. 36 vs. 21 vs. 11 months.

**CPSS-Mol (molecular CPSS, 2022):** Integrates ASXL1, NRAS/KRAS, RUNX1 mutations + cytogenetics + clinical variables → improved stratification. ASXL1 and RAS mutations → upgrade risk category; SETBP1 mutation → poor prognosis regardless of other factors.

**CMML-PM scoring:** Integrated score with WBC, BM blast %, hemoglobin, PLT → used by some centers for transplant decision.

## Function

### Monocyte biology in CMML

**CMML monocyte origin:**
CMML monocytes arise from the malignant HSC clone (proven by detection of SRSF2/TET2 mutations in sorted CD14+ monocytes, CD34+ progenitors, B-cells, T-cells in some cases — indicating oligoclonal multilineage involvement); CMML monocytes have abnormal function: impaired phagocytosis, altered cytokine secretion (high IL-6, IL-10, CCL2, M-CSF), immunosuppressive (similar to M2 macrophage phenotype); CMML monocytes produce excess GM-CSF → autocrine proliferative loop.

**Extramedullary monocytic infiltration:**
CMML monocytes infiltrate skin (leukemia cutis), liver, spleen, lymph nodes → organomegaly; splenomegaly in ~30-50% of MP-CMML; liver enlargement in ~20%; pleural/pericardial effusions in advanced disease; extramedullary infiltration → myeloid sarcoma-like presentations.

## Pathology

### Diagnosis and clinical presentation

**Clinical presentation:**
- Constitutional symptoms: Fatigue, weight loss, night sweats (~50% of patients)
- Splenomegaly: More common in MP-CMML; left upper quadrant fullness; early satiety
- Cytopenias: Anemia (most common, requiring transfusions in ~30%), thrombocytopenia, neutropenia
- Skin lesions: Leukemia cutis (papules, plaques with monocytic/myeloid infiltration); Sweet's syndrome (neutrophilic dermatosis)
- Incidental discovery: CBC showing monocytosis ≥10% of WBC → evaluation

**Diagnostic workup:**
1. CBC with differential: Monocyte count, monocyte percentage, WBC, Hgb, platelets
2. Peripheral blood smear: Promonocytes (bilobed, irregular nuclei, gray cytoplasm) vs. blasts; RBC morphology
3. Flow cytometry (peripheral blood): CD14/CD16 monocyte subset analysis → CMML classical monocytosis pattern (≥94% classical CD14+CD16− monocytes)
4. Bone marrow aspirate + biopsy: Dysplasia; blast %; monocytic infiltration; reticulin fibrosis
5. Conventional karyotype: 20-cell metaphase; FISH for PDGFRB, PDGFRA, FGFR1 if eosinophilia
6. FISH for PDGFRB rearrangement: Required if eosinophilia (absolute eosinophil count ≥1.5×10⁹/L) → if PDGFRB+, classify as MPN-eo + PDGFRB → imatinib
7. Molecular NGS: SRSF2, TET2, ASXL1, KRAS, NRAS, CBL, DNMT3A, IDH1/2, EZH2, SETBP1, TP53

**Excluding reactive monocytosis:**
Reactive causes (infection, inflammatory disease, solid tumors, auto-immune) → monocytosis may mimic CMML; differentiated by: Flow cytometry monocyte subset (reactive: <94% classical), absence of dysplasia/mutations, resolution of monocytosis with treatment of underlying condition; some infections (TB, HIV, CMV) → sustained reactive monocytosis requiring careful exclusion.

### Treatment

**Low/Intermediate-risk CMML (CPSS low/Int-1):**
- **Observation:** Asymptomatic CMML-0/1 without significant cytopenias or organomegaly; CBC monitoring q2-3 months
- **ESA (erythropoiesis-stimulating agents):** For symptomatic anemia + EPO <500 in MD-CMML; response rate ~25-35%
- **Hydroxyurea:** For cytoreduction in MP-CMML (WBC >13); rapid WBC control; does not affect mutations or alter natural history; oral daily dosing
- **Ruxolitinib (JAK1/2 inhibitor):** For MP-CMML with symptomatic splenomegaly (analogous to MF use); spleen response ~40-50%; CMML specific Phase 2 data; not FDA-approved specifically for CMML but used off-label; reduces cytokine-driven monocyte proliferation

**Higher-risk CMML (CPSS Int-2/High) or symptomatic disease:**
- **Azacitidine (75 mg/m² SC days 1-7 q28d):** Most widely used HMA; OS benefit in higher-risk CMML; ORR ~40-50% (including stable disease); CR rate ~10-15%; transfusion independence in ~25%; approved for MDS (FDA 2004) and used routinely in CMML; no dedicated FDA approval for CMML specifically
- **Decitabine (20 mg/m² IV days 1-5 q28d):** Alternative HMA; similar efficacy to azacitidine; may be preferred in some institutions; oral decitabine (decitabine + cedazuridine) available
- **Enasidenib/Ivosidenib:** For IDH2- or IDH1-mutant CMML (~8% total); FDA-approved in IDH-mutant AML; active in IDH-mutant MDS/CMML (trial ongoing); ORR ~30-40% in this subset

**Allogeneic SCT:**
Only potentially curative treatment for CMML; CPSS Int-2/High + age ≤75 + good performance status → transplant evaluation; 5-year OS ~30-40% post-transplant; reduced intensity conditioning (RIC) for older patients; relapse post-transplant remains significant (~30-40%); molecular MRD monitoring (SRSF2, TET2, ASXL1 VAF) post-transplant → guide preemptive therapy.

**PDGFRB-rearranged MPN (imatinib-sensitive):**
~10% of CMML-like presentations have PDGFRB fusions (ETV6-PDGFRB, rabaptin-5-PDGFRB, others) → constitutive PDGFRB kinase → myeloproliferation + eosinophilia; imatinib 400 mg/day → complete hematologic and cytogenetic remission in >90%; sustained long-term; this subset should not be treated as CMML → always exclude PDGFRB by FISH when eosinophilia present.

**Emerging therapies:**
- **Lenzilumab (anti-GM-CSF antibody):** GM-CSF drives CMML monocyte self-renewal → lenzilumab in Phase 2 for MP-CMML; responses in early data (~40%)
- **STP1002 (CSF1R inhibitor):** M-CSF (CSF1) drives monocyte/macrophage proliferation → CSF1R (CD115) inhibition → reduces monocyte burden; Phase 1 for CMML ongoing
- **H3B-8800 (spliceosome modulator):** Selectively toxic to SRSF2/SF3B1-mutant cells; Phase 1 for MDS/AML/CMML; modest early ORR ~12%
- **Venetoclax + azacitidine:** Active in AML/MDS → being evaluated in higher-risk CMML; early data promising
- **Trametinib (MEK inhibitor):** For KRAS/NRAS-mutant CMML; disease control in ~50% in Phase 2 data; KRAS/NRAS-mutant CMML is enriched in MP-CMML and aggressive subtypes

**AML transformation management:**
CMML → AML transformation (~15-30% at 5 years): Treat as secondary AML; CPX-351 (liposomal daunorubicin/cytarabine, AML-MRC indication): Response ~40-50%; venetoclax + azacitidine: Response ~55-65% but duration limited; allo-SCT if CR achieved; prognosis of transformed CMML AML is poor (median OS ~6-8 months with standard therapy).

## Connections

- `connects-to` → **[SRSF2](../../03-molecular/srsf2/README.md)** — SRSF2 P95H in ~45% of CMML; most common splicing factor mutation; co-occurs with TET2 (~60%) in the dominant CMML doublet; P95H alters CCNG ESE splicing → monocytic differentiation bias; SRSF2+TET2 knockin mice develop CMML-like disease with full penetrance.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A mutations in ~10% of CMML; DNMT3A is an early CHIP hit establishing pre-malignant HSC clones before SRSF2 or TET2 co-mutation; DNMT3A+TET2+SRSF2 triplet occurs in ~5% of CMML → aggressive progression; DNMT3A-CHIP → CMML progression rate ~1-2% per year.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS/NRAS mutations in ~15% of CMML; RAS activation → monocyte proliferation → MP-CMML phenotype (WBC >13×10⁹/L, splenomegaly, organomegaly); KRAS-mutant CMML is aggressive with poor HMA response; MEK inhibitor trametinib shows early activity in RAS-mutant CMML.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB promotes monocyte/macrophage survival in CMML; SRSF2/ASXL1 mutations dysregulate NF-κB pathway activity; ruxolitinib reduces cytokine-driven NF-κB signaling in MP-CMML → splenomegaly response ~40-50%; GM-CSF/M-CSF autocrine loops drive NF-κB in CMML monocytes.

[^itzykson-2013-cmml-prognosis]: Itzykson R, Kosmider O, Renneville A, et al. Prognostic score including gene mutations in chronic myelomonocytic leukemia. *J Clin Oncol.* 2013;31(19):2428-2436. [doi:10.1200/JCO.2012.47.3314](https://doi.org/10.1200/JCO.2012.47.3314) · [PubMed 23690417](https://pubmed.ncbi.nlm.nih.gov/23690417/)
[^patnaik-2022-cmml-review]: Patnaik MM, Tefferi A. Chronic myelomonocytic leukemia: 2022 update on diagnosis, risk stratification and management. *Am J Hematol.* 2022;97(3):352-372. [doi:10.1002/ajh.26457](https://doi.org/10.1002/ajh.26457) · [PubMed 34958140](https://pubmed.ncbi.nlm.nih.gov/34958140/)
