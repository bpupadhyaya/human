---
schema: human-scale-entry/v1
id: ptcl
name: Peripheral T-cell Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "PTCLs are aggressive T/NK-cell lymphomas (~10-15% of NHL); major subtypes PTCL-NOS (~25%), AITL (~20%), ALK+ ALCL (~7%), ALK- ALCL (~8%); AITL driven by TET2+DNMT3A+RHOA G17V; brentuximab vedotin+CHP is standard for CD30+ PTCL (ECHELON-2); 5-year OS ~30-50%."
aliases: ["PTCL", "peripheral T-cell lymphoma", "AITL", "angioimmunoblastic T-cell lymphoma", "ALCL", "anaplastic large cell lymphoma", "ALK+ ALCL", "ALK- ALCL", "T-cell lymphoma", "PTCL-NOS"]
sources:
  - id: horwitz-2019-echelon2
    type: peer-reviewed
    cite: "Horwitz S, O'Connor OA, Pro B, et al. Brentuximab vedotin with chemotherapy for CD30-positive peripheral T-cell lymphoma (ECHELON-2): a global, double-blind, randomised, phase 3 trial. Lancet. 2019;393(10168):229-240."
    doi: "10.1016/S0140-6736(18)32984-2"
    pmid: "30522922"
    url: "https://doi.org/10.1016/S0140-6736(18)32984-2"
  - id: palomero-2014-ptcl-epigenetics
    type: peer-reviewed
    cite: "Palomero T, Couronné L, Khiabanian H, et al. Recurrent mutations in epigenetic regulators, RHOA and FYN kinase in peripheral T cell lymphomas. Nat Genet. 2014;46(2):166-170."
    doi: "10.1038/ng.2872"
    pmid: "24413734"
    url: "https://doi.org/10.1038/ng.2872"
cross_links:
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "TET2 loss-of-function is the most common mutation in AITL (~60-80%) and a major driver in PTCL-NOS (~20%); TET2+DNMT3A+RHOA G17V is the canonical AITL triplet; TET2 mutations arise in a pre-malignant TFH HSC clone and precede RHOA G17V acquisition."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A R882H/C mutations occur in ~20-30% of AITL and ~15% PTCL-NOS, co-mutating with TET2 in the pre-malignant TFH clone; DNMT3A+TET2 co-loss → genome-wide hypermethylation; therapy-related T-cell lymphomas from DNMT3A CHIP clones have been reported."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "NPM1-ALK t(2;5)(p23;q35) defines ALK+ ALCL (~7% of PTCL); ALK fusion drives JAK-STAT3 constitutive activation; crizotinib, alectinib, brigatinib active in ALK+ ALCL; ALK+ ALCL is the most favorable PTCL subtype (5-year OS ~70-80% with A+CHP)."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 is a TFH cell surface marker expressed in AITL tumor cells; anti-PD-1 (pembrolizumab, nivolumab) has activity in relapsed PTCL (ORR ~15-30%) but risk of paradoxical lymphoma acceleration in AITL; PD-L1 overexpressed on ALK- ALCL via DUSP22/IRF4 rearrangements."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH2 R172K (distinct from MDS R140Q) occurs in ~20-30% of AITL/nTFHL; IDH2 → 2-HG → TET2 + KDM competitive inhibition → epigenetic reprogramming; enasidenib (IDH2 inhibitor, approved AML) explored in IDH2-mutant AITL; IDH2+TET2 co-mutation drives extreme hypermethylation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Constitutive STAT3 activation in ALK+ ALCL (NPM1-ALK → JAK3 → STAT3), ALK- ALCL (STAT3 activating mutations ~15%), and HSTCL (STAT3/STAT5b mutations); STAT3 drives CD30, BCL-2, MCL-1, and VEGF → lymphoma survival; ruxolitinib (JAK1/2→STAT3) has activity in PTCL trials."
  - target: 01-human/03-molecular/cd30
    relation: connects-to
    note: "CD30 (TNFRSF8) is the primary PTCL therapeutic target; brentuximab vedotin (anti-CD30 ADC) FDA-approved for ALCL and CD30+ PTCL; ECHELON-2: BV+CHP vs CHOP → PFS HR 0.71; CD30 in ALCL (~100%), PTCL-NOS (~30-50%); CD30 signals via TRAF1/2/3 → NF-κB → lymphoma survival."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Peripheral T-cell lymphoma and primary CNS lymphoma are aggressive non-Hodgkin lymphomas of opposite lineage: PTCL is a heterogeneous T-cell group (TET2/RHOA/STAT3-driven), PCNSL a CNS-confined B-cell (DLBCL) tumor driven by MYD88 — lineage and site reshape lymphoma biology."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Angioimmunoblastic T-cell lymphoma, a major PTCL subtype, arises from the follicular helper T cell (TFH): tumor cells keep TFH markers (PD-1, CXCL13, ICOS, BCL6) and recruit a reactive B-cell/EBV background, while TET2/DNMT3A/RHOA-G17V mutations drive the malignancy."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin is a defining PTCL site: primary cutaneous CD30+ T-cell lymphomas (cutaneous ALCL, lymphomatoid papulosis) and the mycosis fungoides/Sézary spectrum home to skin, often indolent — contrasting with the aggressive nodal PTCLs like AITL and systemic ALCL."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Peripheral T-cell and diffuse large B-cell lymphoma are the aggressive non-Hodgkin lymphomas of the two lineages: PTCL arises from mature T cells, is rarer, and has a worse prognosis than DLBCL, which is CD20+ and responds to rituximab-based R-CHOP that PTCL cannot use."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "PTCL and Hodgkin lymphoma intersect at CD30: anaplastic large cell lymphoma, a PTCL subtype, strongly expresses CD30 like Hodgkin's Reed-Sternberg cells, so the anti-CD30 drug brentuximab vedotin treats both—and the two can be hard to distinguish histologically."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Some peripheral T-cell lymphomas derive from regulatory or follicular-helper T cells: adult T-cell leukemia often has a Treg-like FOXP3+ phenotype and angioimmunoblastic PTCL arises from follicular-helper T cells—so the normal T-cell subset shapes the lymphoma."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Several peripheral T-cell lymphomas are EBV-driven: extranodal NK/T-cell lymphoma is defined by EBV infection, and angioimmunoblastic T-cell lymphoma harbors EBV-positive B-immunoblasts—so the virus shapes diagnosis and biology across this T-cell lymphoma group."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "PTCL and mantle cell lymphoma are both aggressive non-Hodgkin lymphomas but of opposite lineage: PTCL arises from mature T cells, while MCL is a B-cell tumor with t(11;14) cyclin D1—immunophenotyping the T- versus B-cell origin guides therapy."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "PTCL and follicular lymphoma sit at opposite ends of lineage and tempo: follicular lymphoma is an indolent germinal-center B-cell tumor, while most PTCLs are aggressive mature T-cell cancers—the T-versus-B distinction fundamentally separates their biology and treatment."
---

# Peripheral T-cell Lymphoma

## Overview

**Peripheral T-cell lymphomas (PTCL)** are a heterogeneous group of mature (post-thymic) T-cell and NK-cell neoplasms arising from peripheral T/NK lymphocytes at various differentiation stages. PTCLs collectively account for **~10-15% of all non-Hodgkin lymphomas** (NHL) and are notably more aggressive and chemotherapy-resistant than B-cell lymphomas. The landmark discovery of recurrent **TET2, DNMT3A, RHOA G17V**, and **IDH2 R172K** mutations in AITL established epigenetic dysregulation as a central oncogenic mechanism in nodal T-cell lymphomas [^palomero-2014-ptcl-epigenetics]. The ECHELON-2 trial established **brentuximab vedotin + CHP** (BV+CHP) as standard first-line therapy for CD30-positive PTCL, replacing CHOP [^horwitz-2019-echelon2]. Overall prognosis remains poor for most PTCL subtypes: 5-year OS ~30-50% with current standard therapy.

**PTCL epidemiology:**
- Incidence: ~9,000 cases/year in USA; global variation (higher in Asia: ENKTL, ATLL)
- Median age at diagnosis: ~60 years; male predominance (M:F ~1.5-2:1)
- Geographic variation: ALK+ ALCL more common in young patients; ATLL endemic in HTLV-1 areas (Japan, Caribbean, West Africa); ENKTL prevalent in Asia and Latin America

## Structure

### WHO 2022 classification of mature T/NK-cell neoplasms

**Nodal PTCLs (lymph node-derived):**
- **PTCL-NOS (not otherwise specified):** Largest subtype (~25%); heterogeneous; aggressive; lacks defining genetic alterations of other subtypes; molecular subgroups: TBX21+ (Th1-like, worse prognosis) and GATA3+ (Th2-like, worse prognosis), CD30+
- **AITL / Nodal T-follicular helper lymphoma (nTFHL-AI, ~20%):** TFH immunophenotype; TET2+DNMT3A+RHOA G17V; follicular dendritic cell meshwork; EBER-negative (EBV in bystander B cells); hypergammaglobulinemia; autoimmune features
- **Nodal PTCL with TFH phenotype (nTFHL-other, ~5%):** TFH markers but AITL-like histology without full AITL criteria
- **Follicular T-cell lymphoma (FTCL, ~2%):** TFH phenotype with follicular growth pattern; RHOA G17V, TET2

**Systemic PTCLs:**
- **ALK+ ALCL (~7%):** NPM1-ALK t(2;5)(p23;q35) or variant ALK fusions; strong CD30+; TIA-1+; 5-year OS ~70-80%; best prognosis among PTCL
- **ALK- ALCL (~8%):** CD30+ without ALK rearrangement; DUSP22/IRF4 rearrangements (favorable, ~30%), TP63 rearrangements (adverse, ~8%), JAK1 mutations (~15%); 5-year OS ~40-50%
- **Breast implant-associated ALCL (BIA-ALCL):** CD30+; ALK-; in peri-implant fluid; excellent prognosis with implant removal; rare progression to systemic ALCL
- **PTCL with GATA3/TBX21:** Emerging molecular subtypes within PTCL-NOS

**Extranodal PTCLs:**
- **Extranodal NK/T-cell lymphoma (ENKTL, ~10%):** EBV-driven; nasal type; KIR3DL2+; DDX3X, KMT2D, ARID1A, TP53 mutations; SMILE protocol or l-asparaginase-based regimens; PD-L1 overexpressed via EBV LMP1; pembrolizumab activity in R/R
- **Hepatosplenic T-cell lymphoma (HSTCL, ~1%):** γδ TCR; STAT3/STAT5b mutations; isochromosome 7q; young males; iatrogenic immunosuppression (IBD on biologics); aggressive; median OS <2 years
- **Subcutaneous panniculitis-like T-cell lymphoma (SPTCL):** αβ TCR; indolent when HLH-absent
- **Mycosis fungoides/Sézary syndrome:** Cutaneous PTCL; CTCL; separate clinical considerations

**Adult T-cell leukemia/lymphoma (ATLL):**
- HTLV-1 driven; endemic Japan, Caribbean, West Africa; acute/lymphomatous/chronic/smoldering
- Tax protein → NF-κB constitutive activation; CCR4+; FOXP3+
- Mogamulizumab (anti-CCR4, FDA 2018 for CTCL; activity in ATLL); lenalidomide; allogeneic SCT

### AITL molecular architecture

AITL arises from TFH (T-follicular helper) cell progenitors through sequential mutational acquisition:

**Stage 1 — Pre-malignant HSC clone:**
TET2 and/or DNMT3A mutations in HSCs → clonal expansion; TET2-mutant HSCs differentiate toward both myeloid and lymphoid lineages → pre-malignant TFH cells carry TET2/DNMT3A mutations alongside normal cells; this stage is detectable in peripheral blood (non-T cells also carry mutations).

**Stage 2 — TFH progenitor expansion:**
RHOA G17V acquired in TFH progenitor → impairs RhoA GTPase activity (dominant-negative) → altered VAV1 signaling, PI3K activation → TFH clonal expansion; RHOA G17V is lymphoid-specific (not in myeloid compartment of same patient).

**Stage 3 — AITL:**
IDH2 R172K (not R140Q) acquired in ~20-30% → 2-HG → TET2 further inhibited → hypermethylation accelerated; FYN kinase mutations (~3%); additional co-mutations accumulate → overt lymphoma with TFH phenotype, follicular dendritic cell meshwork, abundant reactive cells (B cells, plasma cells, eosinophils, macrophages).

**AITL immunophenotype:**
CD3+, CD4+, CD10+, BCL6+, CXCR5+, ICOS+, PD-1+, CD279+ (TFH markers); CD30 variable; EBV+ bystander B cells (EBER+); follicular dendritic cell meshwork (CD21+, CD23+).

### ALK+ ALCL molecular biology

**NPM1-ALK fusion (t(2;5)):**
NPM1 N-terminus provides oligomerization → constitutive cytoplasmic ALK dimerization → trans-autophosphorylation → JAK3/STAT3, PI3K/AKT, RAS/ERK activation; ALK+ALCL: strong uniform CD30 staining; cytoplasmic ALK by IHC; hallmark "doughnut cells" (horseshoe/kidney-shaped nuclei); pediatric peak (15-30 years).

**Variant ALK fusions:**
TPM3-ALK (cytoplasmic, granular), CLTC-ALK (cytoplasmic, granular), EML4-ALK (cytoplasmic) → same downstream signaling; IHC pattern differs from NPM1-ALK (nuclear+cytoplasmic).

## Function

### Normal T-cell biology context

**TFH biology (AITL origin):**
TFH cells are CD4+ T cells that home to germinal centers via CXCR5 (follicle-homing receptor); interact with B cells via ICOS-ICOSL, CD40L-CD40, IL-21; promote B-cell somatic hypermutation and affinity maturation; BCL6 is the master TFH transcription factor; PD-1 expressed on TFH prevents premature T-cell activation. AITL neoplastic cells retain full TFH identity: CXCR5+, BCL6+, ICOS+, PD-1+, IL-21-producing.

**TCR signaling in T-cell lymphoma:**
T-cell receptor (TCR) signaling amplified in PTCL: LCK/ZAP70 → LAT → PLC-γ → DAG+IP₃ → PKC-θ+NFAT → T-cell activation; RHOA G17V interferes with VAV1-CDC42/RAC1 axis → promotes aberrant cytoskeletal organization and PI3K activation without requiring TCR stimulation; FYN mutations (gain-of-function) → hyperactive Src-family kinase → enhanced TCR-proximal signaling.

## Pathology

### Clinical presentation

**AITL:**
Generalized lymphadenopathy (>90%); B symptoms (fever, night sweats, weight loss) ~75%; hepatosplenomegaly ~70%; skin rash (maculopapular, ~50%); pleural effusion, ascites (~30%); autoimmune hemolytic anemia (Coombs+), cold agglutinins, thrombocytopenia; hypergammaglobulinemia (polyclonal IgG elevation); elevated LDH, β2-microglobulin; often misdiagnosed as autoimmune disease before biopsy.

**ALK+ ALCL:**
Young patients (median ~25 years); advanced stage (~70%); systemic symptoms; excellent prognosis; B symptoms common; extranodal involvement (bone, skin, liver, lung); mediastinal disease less common than Hodgkin lymphoma.

**PTCL-NOS:**
Aggressive presentation; generalized lymphadenopathy; extranodal involvement (~60%); advanced stage (~70%); elevated LDH; poor prognosis (5-year OS ~30-40%).

### Diagnosis and workup

**Biopsy essential:** Excisional lymph node biopsy preferred (core needle biopsy may be insufficient for architecture assessment).

**Immunophenotyping:**
- TCR flow cytometry and IHC: αβ vs γδ; pan-T markers (CD2, CD3, CD5, CD7) often aberrantly lost
- CD4/CD8 ratio; TFH markers for AITL (PD-1, CXCR5, CD10, BCL6, ICOS)
- CD30 IHC (ALCL, some PTCL-NOS): scored quantitatively for brentuximab eligibility
- ALK IHC (ALCL): nuclear+cytoplasmic = NPM1-ALK; cytoplasmic = variant fusions
- EBER ISH (EBV in bystander B cells = AITL feature; if tumor cells EBV+ = ENKTL or EBV+ DLBCL)

**Molecular:**
- TCR gene clonality (PCR/NGS): confirms clonal T-cell expansion; not subtype-specific
- NGS panel: TET2, DNMT3A, RHOA G17V, IDH2, SRSF2 (AITL pattern); TP53, SETD2, KMT2D (PTCL-NOS); STAT3/5B (HSTCL)
- ALK FISH for t(2;5) and variant fusions
- Cytogenetics: isochromosome 7q (HSTCL); DUSP22/IRF4 FISH (ALK- ALCL)

### Prognostic scoring

**PTCL-specific IPI (PIT — Prognostic Index for PTCL):** Age >60, PS ≥2, elevated LDH, bone marrow involvement → 4 adverse factors; Low (0), Low-Int (1), High-Int (2), High (3-4) risk groups; 5-year OS: 62%, 53%, 33%, 18%.

**AITL-specific:** No validated molecular prognostic score; TET2 biallelic → worse; IDH2 co-mutation → may predict enasidenib sensitivity.

### Treatment

**First-line (non-ALK+ ALCL):**
- **CHOP (cyclophosphamide, doxorubicin, vincristine, prednisone):** Historical standard; ORR ~60-75%; CR ~50%; 5-year OS ~30-40%; inadequate for most PTCL
- **CHOEP (CHOP + etoposide):** Benefit in young (<60 years) patients in Nordic retrospective data; no Phase 3 RCT confirmation; etoposide toxicity limits use in elderly
- **BV+CHP (brentuximab vedotin + cyclophosphamide, doxorubicin, prednisone) for CD30+ PTCL:**
  ECHELON-2 (Phase 3 RCT, N=452): BV+CHP vs CHOP for CD30+ PTCL; primary endpoint PFS: 48.2 vs 20.8 months (HR 0.71, p=0.011); 5-year OS: 70.1% vs 61.0% (HR 0.72); FDA approved 2018 for CD30+ PTCL; neuropathy (Grade ≥3 ~17%) main toxicity [^horwitz-2019-echelon2]
- **AITL epigenetic approach:** Azacitidine ± CHOP in clinical trials (NCT02795832); romidepsin+CHOP (ROMIDEPSIN trial)

**ALK+ ALCL:**
- BV+CHP: primary frontline regimen for CD30+ PTCL including ALK+ ALCL
- CHOP → excellent outcomes (5-year OS ~75%); BV+CHP improves upon CHOP in ECHELON-2 subgroup
- ALK inhibitors (crizotinib, alectinib): active in relapsed/refractory ALK+ ALCL; ORR ~75-85%

**Relapsed/Refractory:**
- **Brentuximab vedotin** (CD30+, single-agent R/R): ORR ~86% ALK+ ALCL, ~57% ALK- ALCL; FDA 2011 accelerated (R/R ALCL); FDA 2018 (PCNS+ PTCL)
- **Romidepsin** (HDAC inhibitor, IV): ORR ~25-38% in PTCL; FDA 2011; preferred for PTCL-NOS/AITL
- **Belinostat** (HDAC inhibitor, IV): ORR ~26% PTCL; FDA 2014 (Belingen-1 trial)
- **Pralatrexate** (antifolate, Folotyn): ORR ~29% PTCL; FDA 2009; mucositis dose-limiting
- **Mogamulizumab** (anti-CCR4): ORR ~35% in CCR4+ PTCL (ATLL, AITL); FDA approved CTCL, investigational PTCL
- **Duvelisib** (PI3K-δ/γ inhibitor): ORR ~32% R/R PTCL (PRIMO trial); FDA approved for FL
- **Pembrolizumab/nivolumab:** ORR ~15-33% in selected PTCL; **caution in AITL** (paradoxical progression reported — checkpoint inhibition may promote AITL TFH expansion)

**Consolidation allo-SCT:**
- Recommended in responding high-risk patients in first remission (CR1/PR1)
- 3-year OS post-allo-SCT ~45-60% (registry data)
- Particularly beneficial: PTCL-NOS, AITL, ALK- ALCL (especially TP63-rearranged)
- Myeloablative vs RIC depending on age/comorbidities

**ENKTL-specific:**
- L-asparaginase-containing regimens (SMILE: dexamethasone, methotrexate, ifosfamide, l-asparaginase, etoposide; AspaMetDex)
- Concurrent/sequential radiotherapy for localized nasal ENKTL
- Pembrolizumab: ORR ~46% in R/R ENKTL (EBV-driven PD-L1 upregulation)

## Connections

- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — TET2 loss-of-function is the most common mutation in AITL (~60-80%) and a major driver in PTCL-NOS (~20%); TET2+DNMT3A+RHOA G17V is the canonical AITL triplet; TET2 mutations arise in a pre-malignant TFH HSC clone and precede RHOA G17V acquisition.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A R882H/C mutations occur in ~20-30% of AITL and ~15% PTCL-NOS, co-mutating with TET2 in the pre-malignant TFH clone; DNMT3A+TET2 co-loss → genome-wide hypermethylation; therapy-related T-cell lymphomas from DNMT3A CHIP clones have been reported.
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — NPM1-ALK t(2;5)(p23;q35) defines ALK+ ALCL (~7% of PTCL); ALK fusion drives JAK-STAT3 constitutive activation; crizotinib, alectinib, brigatinib active in ALK+ ALCL; ALK+ ALCL is the most favorable PTCL subtype (5-year OS ~70-80% with A+CHP).
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 is a TFH cell surface marker expressed in AITL tumor cells; anti-PD-1 (pembrolizumab, nivolumab) has activity in relapsed PTCL (ORR ~15-30%) but risk of paradoxical lymphoma acceleration in AITL; PD-L1 overexpressed on ALK- ALCL via DUSP22/IRF4 rearrangements.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH2 R172K (distinct from MDS R140Q) occurs in ~20-30% of AITL/nTFHL; IDH2 → 2-HG → TET2 + KDM competitive inhibition → epigenetic reprogramming; enasidenib (IDH2 inhibitor, approved AML) explored in IDH2-mutant AITL; IDH2+TET2 co-mutation drives extreme hypermethylation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — constitutive STAT3 activation in ALK+ ALCL (NPM1-ALK → JAK3 → STAT3), ALK- ALCL (STAT3 activating mutations ~15%), and HSTCL (STAT3/STAT5b mutations); STAT3 drives CD30, BCL-2, MCL-1, and VEGF → lymphoma survival; ruxolitinib (JAK1/2→STAT3) has activity in PTCL trials.
- `connects-to` → **[CD30](../../03-molecular/cd30/README.md)** — CD30 (TNFRSF8) is the primary PTCL therapeutic target; brentuximab vedotin (anti-CD30 ADC) FDA-approved for ALCL and CD30+ PTCL; ECHELON-2: BV+CHP vs CHOP → PFS HR 0.71; CD30 in ALCL (~100%), PTCL-NOS (~30-50%); CD30 signals via TRAF1/2/3 → NF-κB → lymphoma survival.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Peripheral T-cell lymphoma and primary CNS lymphoma are aggressive non-Hodgkin lymphomas of opposite lineage: PTCL is a heterogeneous T-cell group (TET2/RHOA/STAT3-driven), PCNSL a CNS-confined B-cell (DLBCL) tumor driven by MYD88 — lineage and site reshape lymphoma biology.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Angioimmunoblastic T-cell lymphoma, a major PTCL subtype, arises from the follicular helper T cell (TFH): tumor cells keep TFH markers (PD-1, CXCL13, ICOS, BCL6) and recruit a reactive B-cell/EBV background, while TET2/DNMT3A/RHOA-G17V mutations drive the malignancy.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin is a defining PTCL site: primary cutaneous CD30+ T-cell lymphomas (cutaneous ALCL, lymphomatoid papulosis) and the mycosis fungoides/Sézary spectrum home to skin, often indolent — contrasting with the aggressive nodal PTCLs like AITL and systemic ALCL.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Peripheral T-cell and diffuse large B-cell lymphoma are the aggressive non-Hodgkin lymphomas of the two lineages: PTCL arises from mature T cells, is rarer, and has a worse prognosis than DLBCL, which is CD20+ and responds to rituximab-based R-CHOP that PTCL cannot use.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — PTCL and Hodgkin lymphoma intersect at CD30: anaplastic large cell lymphoma, a PTCL subtype, strongly expresses CD30 like Hodgkin's Reed-Sternberg cells, so the anti-CD30 drug brentuximab vedotin treats both—and the two can be hard to distinguish histologically.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Some peripheral T-cell lymphomas derive from regulatory or follicular-helper T cells: adult T-cell leukemia often has a Treg-like FOXP3+ phenotype and angioimmunoblastic PTCL arises from follicular-helper T cells—so the normal T-cell subset shapes the lymphoma.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Several peripheral T-cell lymphomas are EBV-driven: extranodal NK/T-cell lymphoma is defined by EBV infection, and angioimmunoblastic T-cell lymphoma harbors EBV-positive B-immunoblasts—so the virus shapes diagnosis and biology across this T-cell lymphoma group.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — PTCL and mantle cell lymphoma are both aggressive non-Hodgkin lymphomas but of opposite lineage: PTCL arises from mature T cells, while MCL is a B-cell tumor with t(11;14) cyclin D1—immunophenotyping the T- versus B-cell origin guides therapy.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — PTCL and follicular lymphoma sit at opposite ends of lineage and tempo: follicular lymphoma is an indolent germinal-center B-cell tumor, while most PTCLs are aggressive mature T-cell cancers—the T-versus-B distinction fundamentally separates their biology and treatment.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^horwitz-2019-echelon2]: Horwitz S, O'Connor OA, Pro B, et al. Brentuximab vedotin with chemotherapy for CD30-positive peripheral T-cell lymphoma (ECHELON-2): a global, double-blind, randomised, phase 3 trial. *Lancet.* 2019;393(10168):229-240. [doi:10.1016/S0140-6736(18)32984-2](https://doi.org/10.1016/S0140-6736(18)32984-2) · [PubMed 30522922](https://pubmed.ncbi.nlm.nih.gov/30522922/)
[^palomero-2014-ptcl-epigenetics]: Palomero T, Couronné L, Khiabanian H, et al. Recurrent mutations in epigenetic regulators, RHOA and FYN kinase in peripheral T cell lymphomas. *Nat Genet.* 2014;46(2):166-170. [doi:10.1038/ng.2872](https://doi.org/10.1038/ng.2872) · [PubMed 24413734](https://pubmed.ncbi.nlm.nih.gov/24413734/)
