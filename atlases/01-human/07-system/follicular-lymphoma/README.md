---
schema: human-scale-entry/v1
id: follicular-lymphoma
name: Follicular Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Follicular lymphoma is the most common indolent B-cell lymphoma; t(14;18) BCL-2-IGH in ~85% drives apoptosis resistance; EZH2 Y641 in ~25% silences tumor suppressors. Rituximab+bendamustine or R-CHOP are standard; tazemetostat is approved for EZH2-mutant relapsed/refractory FL."
aliases: ["follicular lymphoma", "FL", "indolent NHL", "t(14;18) lymphoma", "BCL-2-IGH", "follicle center lymphoma", "grade 1-2 follicular lymphoma"]
sources:
  - id: marcus-2017-gallium
    type: peer-reviewed
    cite: "Marcus R, Davies A, Ando K, et al. Obinutuzumab for the first-line treatment of follicular lymphoma. N Engl J Med. 2017;377(14):1331-1344."
    doi: "10.1056/NEJMoa1614598"
    pmid: "28976863"
    url: "https://doi.org/10.1056/NEJMoa1614598"
  - id: morschhauser-2020-tazemetostat
    type: peer-reviewed
    cite: "Morschhauser F, Tilly H, Chaidos A, et al. Tazemetostat for patients with relapsed or refractory follicular lymphoma (E7438-G-003): a multicentre, open-label, single-arm, phase 2 trial. Lancet Oncol. 2020;21(11):1433-1442."
    doi: "10.1016/S1470-2045(20)30441-1"
    pmid: "33035457"
    url: "https://doi.org/10.1016/S1470-2045(20)30441-1"
cross_links:
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "t(14;18) BCL-2-IGH translocation in ~85-90% of FL → BCL-2 overexpression in GC B-cells → apoptosis resistance; BCL-2 is the defining molecular feature of FL; venetoclax (BCL-2 inhibitor) active in relapsed FL; BCL-2 overexpression does not predict venetoclax response in FL."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20 mAb) is the backbone of FL therapy; R-CHOP and R-bendamustine are first-line options; obinutuzumab (glycoengineered anti-CD20) + chemotherapy (GALLIUM trial) improved PFS vs. rituximab; anti-CD20 maintenance improves PFS after induction."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Histologic transformation of FL to DLBCL occurs in ~30% at 10 years; POD24 (progression within 24 months) is associated with MYC acquisition and poor prognosis; double-hit lymphoma (MYC+BCL-2 rearrangement) arising from FL is treated as aggressive lymphoma."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "CREBBP mutations in ~60% and EP300 mutations in ~15% of FL → loss of HAT activity → decreased H3K18/K27 acetylation; CREBBP/EZH2 co-mutations in ~30% of FL → dual epigenetic reprogramming; EZH2 silences TNFAIP3/A20 (NF-κB inhibitor) → enhanced NF-κB in FL cells."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2 Y641F/N gain-of-function in ~25% of FL → H3K27me3 → silences tumor suppressor and differentiation genes; tazemetostat (EZH2i) approved for R/R EZH2-mutant FL (ORR 69%) and EZH2-WT FL (ORR 35%); CREBBP co-mutation in ~30% creates dual epigenetic dysregulation."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Histologic transformation from FL to DLBCL occurs in ~30% at 10 years; requires MYC rearrangement, TP53 mutation, or CDKN2A loss on top of BCL-2-IGH; transformed FL is treated as de novo DLBCL; CAR-T (axi-cel) or auto-SCT preferred after induction."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "FL tumor microenvironment is immune-rich (Tfh, Tregs, FDC); mosunetuzumab (CD20×CD3 bispecific, approved R/R FL) redirects T-cells to kill FL B-cells; PD-1 blockade + rituximab has modest single-agent activity; lenalidomide → NK-cell ADCC and immune reprogramming in R/R FL."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Follicular and mantle cell lymphoma are both translocation-defined B-cell NHLs but opposites: FL (t(14;18), BCL-2) is indolent and apoptosis-resistant, MCL (t(11;14), cyclin D1) is proliferation-driven and aggressive — the two classic overexpression translocation lymphomas."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Follicular lymphoma arises from germinal-center B cells frozen mid-maturation: t(14;18) places BCL-2 under the immunoglobulin enhancer, so cells that should die during affinity maturation survive, accumulating as CD10+/BCL6+ clonal follicles that mimic the germinal center."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Follicular lymphoma is a disseminated nodal disease that often involves the spleen and bone marrow at diagnosis (stage III-IV in ~80%); splenic and marrow involvement rarely changes the indolent watch-and-wait or rituximab-based management, since FL is treatable but not curable."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Follicular lymphoma and CLL/SLL are the commonest indolent B-cell lymphomas: both slow-growing, manageable-but-incurable, and prone to transformation into aggressive DLBCL (Richter for CLL); they differ in origin—germinal-center FL with t(14;18)/BCL2 vs CD5+ post-GC CLL."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Follicular lymphoma is a disease of the lymphatic system: malignant germinal-center B cells expand lymph-node follicles, producing the waxing-and-waning painless lymphadenopathy that is its hallmark, with spread to spleen and marrow; many cases are watched while asymptomatic."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Follicular lymphoma arises directly from the germinal center: a malignancy of follicle-center B cells frozen mid-reaction that recapitulates follicular architecture, and its founding t(14;18) drives constitutive BCL2 to block the apoptosis that normally prunes these cells."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Follicular and Hodgkin lymphomas both arise from germinal-center B cells but behave oppositely: follicular is indolent, BCL2-driven and incurable, smoldering for years, while Hodgkin's Reed-Sternberg tumor is aggressive yet highly curable—indolence versus curability."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Follicular and Burkitt lymphomas are germinal-center B-cell tumors at opposite tempos: follicular is slow, BCL2 [t(14;18)]-driven and incurable, while Burkitt is the fastest-growing human tumor, MYC [t(8;14)]-driven yet curable—each named by its translocation."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Follicular lymphoma and multiple myeloma are both incurable B-lineage malignancies at different maturation stages: FL is a CD20+ germinal-center B-cell tumor, myeloma a marrow plasma-cell cancer secreting monoclonal protein—both relapse and remit over years."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Follicular lymphoma depends on follicular helper T cells in its microenvironment: the malignant B cells need Tfh signals and a supportive niche to survive, so FL is as much a disease of the microenvironment as of the B cell—explaining its indolent, relapsing course."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Follicular lymphoma is a germinal-center B cell blocked from becoming a plasma cell: the t(14;18) BCL2 translocation lets it resist apoptosis and accumulate instead of maturing into antibody-secreting cells—an indolent buildup unlike high-grade lymphomas."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Follicular lymphoma's behavior is shaped by immune surveillance: the microenvironment can restrain or enable the tumor, and FL can spontaneously regress or transform—so immune-modulating therapies (rituximab, lenalidomide) are central to its largely incurable course."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Follicular lymphoma usually involves the bone marrow at diagnosis: the indolent clone seeds marrow in a paratrabecular pattern, so it is typically advanced-stage yet slow-growing—curative local therapy is rarely possible, but it can be watched or controlled for years."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy can cure the rare localized follicular lymphoma: low-dose photon radiation to a single involved site is potentially curative in stage I disease, a notable exception in a lymphoma that is otherwise incurable but indolent and managed over many years."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Follicular lymphoma can transform and reach the nervous system: histologic transformation to aggressive DLBCL—and rarely CNS involvement—marks a turn for the worse in this usually indolent disease, shifting management from watchful waiting to intensive therapy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Follicular lymphoma is built on follicular dendritic cells: these stromal cells form the germinal-center meshwork the malignant B cells depend on for survival signals, so the tumor recreates a follicle—its microenvironment shaping when indolent disease turns aggressive."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Follicular lymphoma now yields to T-cell therapies: CD19 CAR-T cells and CD20×CD3 bispecifics (mosunetuzumab) redirect cytotoxic T cells against the B-cell clone, giving durable remissions in this otherwise relapsing, incurable indolent lymphoma."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Follicular lymphoma is usually widespread at diagnosis, infiltrating the liver: indolent but disseminated, it commonly involves liver, spleen, and marrow by the time it is found—so it is staged as advanced yet often watched rather than treated."
---

# Follicular Lymphoma

## Overview

**Follicular lymphoma (FL)** is the most common indolent non-Hodgkin B-cell lymphoma in western countries, comprising ~20-25% of all NHL (~15,000 new cases/year in the US). FL arises from germinal center (GC) B-cells, characterized by follicular (nodular) growth pattern recapitulating normal GC architecture, with CD10+/BCL-6+/BCL-2+ B-cells filling and expanding secondary lymphoid follicles. The pathognomonic molecular event is **t(14;18)(q32;q21)** — BCL-2-IGH translocation in ~85-90% of cases — juxtaposing BCL-2 under the IGH enhancer to drive constitutive BCL-2 overexpression in GC B-cells that normally downregulate BCL-2 during affinity maturation. FL is an incurable disease in most patients with current therapy, yet it follows a characteristically indolent natural history with median OS >15 years in early stages; the GALLIUM trial demonstrated obinutuzumab-based regimens improve progression-free survival over rituximab in frontline treatment [^marcus-2017-gallium]. **Histologic transformation** to aggressive DLBCL is the most serious complication (~30% at 10 years) and is the most common cause of FL-related death.

**Epidemiology:**
- ~15,000 new cases/year in the US; median age at diagnosis ~60 years; M:F equal
- Incidence rising in western countries; higher in North America and Europe than Asia
- 5-year survival: ~90% for grades 1-2; ~70-80% for grade 3B; transformed FL treated like de novo DLBCL
- Median OS: >15 years for grade 1-2 FL; ~50% of patients alive at 20 years; 5-year OS ~88%

**Prognostic risk stratification:**
- **FLIPI (Follicular Lymphoma International Prognostic Index):** 5 adverse factors: age >60, Ann Arbor stage III-IV, Hgb <12 g/dL, LDH > ULN, ≥5 nodal areas
  - Low risk (0-1): 5-year OS ~91%; Intermediate (2): ~78%; High (≥3): ~53%
- **FLIPI-2:** Bone marrow involvement, longest diameter >6 cm, β2M > ULN, Hgb < LLN, age >60
- **POD24 (progression of disease within 24 months):** Strong adverse prognostic marker; ~20% of patients; OS only ~50% at 5 years from POD24; associated with histologic transformation risk

## Structure

### Molecular landscape

**Founding event — t(14;18) BCL-2-IGH:**
t(14;18)(q32;q21) translocation → BCL-2 gene (18q21) fused to IgH locus (14q32) → constitutive BCL-2 overexpression in GC B-cells (which normally downregulate BCL-2 during affinity maturation to allow negative selection). BCL-2 overexpression blocks GC B-cell apoptosis → prolonged GC residence → accumulation of additional mutations → FL development. t(14;18) is detectable in ~50% of normal healthy adults (clonal hematopoiesis-like phenomenon) — requiring additional "hits" for malignant transformation.

**Epigenetic mutations (co-drivers):**
- **CREBBP:** Mutations in ~60% of FL; HAT (histone acetyltransferase) domain mutations → loss of H3K18/K27 acetylation at BCL-6-target loci → impaired activation-induced deaminase (AID) regulation; cooperates with EZH2
- **EP300:** Mutations in ~15% (non-overlapping with CREBBP); similar HAT function
- **KMT2D (MLL4):** ~80% of FL; histone H3K4 methyltransferase; loss → decreased H3K4me3 at promoters → gene silencing (including CDKN2A-independent tumor suppressors)
- **EZH2 Y641/A677/A687:** ~25% gain-of-function mutations → H3K27me3 accumulation → silences tumor suppressors and differentiation regulators; cooperates with CREBBP/KMT2D loss
- **TNFRSF14 (HVEM):** ~40% mutations → loss of BTLA-HVEM checkpoint → tumor-microenvironment immune evasion
- **RRAGC:** ~17% mutations → mTORC1 amino acid sensing dysregulation (rare among lymphomas)

**FL histological grading:**
- Grade 1: 0-5 centroblasts per high power field (HPF)
- Grade 2: 6-15 centroblasts/HPF
- Grade 3A: >15 centroblasts/HPF; centrocytes still present
- Grade 3B: >15 centroblasts/HPF; solid sheets of centroblasts; no centrocytes → treated as aggressive DLBCL
- **Diffuse large B-cell lymphoma (DLBCL) transformation:** Loss of follicular architecture; MYC rearrangement (de novo or secondary); TP53 mutation → aggressive lymphoma with poor prognosis

**Immunophenotype:**
CD19+, CD20+, CD10+ (GC marker), BCL-6+, BCL-2+ (overexpressed via t(14;18)), surface IgM or IgG, FMC7+; CD5 negative, CD23 negative (distinguishes FL from mantle cell lymphoma, CLL).

## Function

### Germinal center biology and FL pathogenesis

**Normal GC B-cell biology:**
GC formation → B-cells undergo somatic hypermutation (SHM) of Ig variable regions → selection for high-affinity antibody clones → antigen-selected B-cells differentiate into plasma cells (BCL-2-low; BLIMP1+) or memory B-cells (BCL-2 restored). BCL-2 is transiently downregulated during GC to allow negative selection of low-affinity clones. EZH2 is highly expressed in GC B-cells to maintain GC identity and suppress PRDM1 (BLIMP1) — preventing premature plasma cell differentiation.

**FL oncogenesis:**
t(14;18) translocation (during V(D)J recombination or SHM) → BCL-2 constitutively expressed in GC B-cells → apoptosis resistance → prolonged GC residence → accumulation of KMT2D, CREBBP, EZH2, TNFRSF14 mutations → FL initiation. The BCL-2-overexpressing, GC-arrested B-cells accumulate in lymph nodes → follicular (nodular) architecture → tumor mass formation without significant constitutional symptoms initially.

**Immunologic microenvironment:**
FL is characteristically "immune-rich" — abundant T follicular helper cells (Tfh), T regulatory cells (Tregs), and follicular dendritic cells (FDC) in the tumor microenvironment. The immune microenvironment influences FL prognosis (high Tfh → better prognosis; high Tregs → worse). TNFRSF14 mutations → loss of HVEM → loss of BTLA/CD160 inhibitory signaling → modified tumor-T cell crosstalk. Mosunetuzumab and bispecific antibodies redirect endogenous T-cells to kill FL B-cells.

### Histologic transformation to DLBCL

**Mechanisms:**
- MYC rearrangement acquisition (in addition to BCL-2-IGH) → double-hit lymphoma; often q8p24 → MYC-IG translocation
- TP53 mutation/deletion → p53 dysfunction → rapid proliferation
- CDKN2A loss → CDK4/6 unrestrained → cell cycle bypass
- BCL-2-IGH + BCL-6 rearrangement → MYC-independent transformation route

**Clinical significance:**
- Transformation rate: ~2-3%/year in first 5 years; lower thereafter
- Histologic biopsy required to confirm transformation (PET can identify biopsy target: FDG avid site)
- Transformed FL: Treat as de novo DLBCL; CAR-T or consolidative auto-SCT in second remission

## Pathology

### Staging and workup

**Ann Arbor staging (Lugano classification 2014):**
- Stage I: Single node region or single extranodal site
- Stage II: ≥2 node regions, same side of diaphragm
- Stage III: Node regions on both sides of diaphragm
- Stage IV: Disseminated extralymphatic involvement
- Most FL presents at Stage III-IV (~80%) — but this does not mandate immediate treatment

**Staging workup:**
- CT chest/abdomen/pelvis with contrast: Baseline nodal and extranodal assessment
- PET-CT: Standard per Lugano guidelines for staging and treatment response (Deauville score); essential for identifying histologic transformation (avid site for biopsy)
- Bone marrow biopsy: For staging in low-risk or limited staging CT; often involved in FL (BM involvement = stage IV → does not change management in asymptomatic FL)
- CBC, CMP, LDH, β2M, uric acid, hepatitis B/C (rituximab reactivation risk)
- t(14;18) FISH or PCR: Confirmatory in atypical cases
- EZH2 mutation testing: If considering tazemetostat for R/R FL
- Molecular profile (NGS panel): CREBBP, KMT2D, EZH2, TNFRSF14 for prognosis/clinical trials

### Treatment

**Watch and wait (asymptomatic, low tumor burden):**
Standard approach for asymptomatic Grade 1-2 FL without GELF criteria (Groupe d'Etude des Lymphomes Folliculaires): No "B symptoms," no bulky disease >7 cm, no organ compromise, no rapid progression, adequate blood counts. Observation with CT q3-6 months; treatment initiation at symptom onset or disease progression.

**First-line (symptomatic or high tumor burden):**
- **R-bendamustine (BR):** Rituximab 375 mg/m² D1 + Bendamustine 90 mg/m² D1-2 q28d × 6 cycles; preferred over R-CHOP for Grade 1-2 FL (BRIGHT trial: superior PFS; less alopecia/neurotoxicity)
- **R-CHOP:** Rituximab + cyclophosphamide + doxorubicin + vincristine + prednisone; q21d × 6-8 cycles; alternative for Grade 3A or bulky disease
- **Obinutuzumab + chemotherapy (G-CHOP or G-bendamustine, GALLIUM trial):** [^marcus-2017-gallium] 3-year PFS 80.0% vs. 73.3% (rituximab+chemo); FDA approved 2016; obinutuzumab maintenance × 2 years post-induction; preferred for high-FLIPI or high tumor burden
- **Rituximab monotherapy:** For elderly/frail patients with limited tumor burden; ORR ~60-70%; maintenance rituximab q8 weeks × 2 years improves PFS

**Rituximab/obinutuzumab maintenance (post-induction):**
- Rituximab 375 mg/m² q8w × 2 years (PRIMA trial): Improves PFS vs. observation; OS benefit not shown
- Obinutuzumab 1000 mg q8w × 2 years: After G-chemotherapy induction (GALLIUM)

**Relapsed/refractory FL:**
- **Tazemetostat 800 mg BID (EZH2-mutant FL):** [^morschhauser-2020-tazemetostat] ORR 69%; FDA approved 2020 for ≥2 prior lines
- **Tazemetostat 800 mg BID (EZH2 WT FL, no satisfactory alternatives):** ORR 35%; FDA approved
- **Lenalidomide + rituximab (R-squared, AUGMENT trial):** ORR 78%; PFS 39.4 vs. 14.1 months vs. rituximab+placebo; FDA approved 2019 for R/R FL
- **Mosunetuzumab (CD20×CD3 bispecific, CELESTIMO trial):** FDA approved 2022 for R/R FL ≥2 prior lines; ORR 80% (CR 60%); step-up dosing cycle 1 (to mitigate CRS)
- **Epcoritamab, glofitamab:** CD20×CD3 bispecifics under evaluation for R/R FL
- **Axicabtagene ciloleucel (CAR-T, ZUMA-5):** ORR 94% in R/R FL ≥2 prior lines; CR 79%; FDA approved 2021; durable responses (18-month DOR ~76%); toxicities: CRS, ICANS

**Consolidation (selected patients):**
- Auto-SCT: PR/CR after ≥2 prior lines; improves PFS; OS benefit not demonstrated in biologic therapy era
- Allo-SCT: For chemotherapy-sensitive disease in poor-risk patients or transformed FL; curative potential at cost of transplant morbidity/mortality

**Radiation:**
- Involved-field RT (24-30 Gy): Stage I/II FL → 10-year PFS ~50%; potentially curative in 40% of stage I
- Palliative RT (2×2 Gy): Very effective for local symptoms (response rate >90%)

**POD24 management:**
High-risk subset (progression within 24 months of first chemoimmunotherapy): Consider CAR-T, clinical trial, or allo-SCT; immune-mediated agents preferred over chemoimmunotherapy rechallenge.

## Connections

- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — t(14;18) BCL-2-IGH translocation in ~85-90% of FL → BCL-2 overexpression in GC B-cells → apoptosis resistance; BCL-2 is the defining molecular feature of FL; venetoclax (BCL-2 inhibitor) active in relapsed FL; BCL-2 overexpression does not predict venetoclax response in FL.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20 mAb) is the backbone of FL therapy; R-CHOP and R-bendamustine are first-line options; obinutuzumab (glycoengineered anti-CD20) + chemotherapy (GALLIUM trial) improved PFS vs. rituximab; anti-CD20 maintenance improves PFS after induction.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Histologic transformation of FL to DLBCL occurs in ~30% at 10 years; POD24 (progression within 24 months) is associated with MYC acquisition and poor prognosis; double-hit lymphoma (MYC+BCL-2 rearrangement) arising from FL is treated as aggressive lymphoma.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — CREBBP mutations in ~60% and EP300 mutations in ~15% of FL → loss of HAT activity → decreased H3K18/K27 acetylation; CREBBP/EZH2 co-mutations in ~30% of FL → dual epigenetic reprogramming; EZH2 silences TNFAIP3/A20 (NF-κB inhibitor) → enhanced NF-κB in FL cells.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2 Y641F/N gain-of-function in ~25% of FL → H3K27me3 → silences tumor suppressor and differentiation genes; tazemetostat (EZH2i) approved for R/R EZH2-mutant FL (ORR 69%) and EZH2-WT FL (ORR 35%); CREBBP co-mutation in ~30% creates dual epigenetic dysregulation.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Histologic transformation from FL to DLBCL occurs in ~30% at 10 years; requires MYC rearrangement, TP53 mutation, or CDKN2A loss on top of BCL-2-IGH; transformed FL is treated as de novo DLBCL; CAR-T (axi-cel) or auto-SCT preferred after induction.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — FL tumor microenvironment is immune-rich (Tfh, Tregs, FDC); mosunetuzumab (CD20×CD3 bispecific, approved R/R FL) redirects T-cells to kill FL B-cells; PD-1 blockade + rituximab has modest single-agent activity; lenalidomide → NK-cell ADCC and immune reprogramming in R/R FL.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Follicular and mantle cell lymphoma are both translocation-defined B-cell NHLs but opposites: FL (t(14;18), BCL-2) is indolent and apoptosis-resistant, MCL (t(11;14), cyclin D1) is proliferation-driven and aggressive — the two classic overexpression translocation lymphomas.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Follicular lymphoma arises from germinal-center B cells frozen mid-maturation: t(14;18) places BCL-2 under the immunoglobulin enhancer, so cells that should die during affinity maturation survive, accumulating as CD10+/BCL6+ clonal follicles that mimic the germinal center.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Follicular lymphoma is a disseminated nodal disease that often involves the spleen and bone marrow at diagnosis (stage III-IV in ~80%); splenic and marrow involvement rarely changes the indolent watch-and-wait or rituximab-based management, since FL is treatable but not curable.
- `connects-to` → **[CLL](../cll/README.md)** — Follicular lymphoma and CLL/SLL are the commonest indolent B-cell lymphomas: both slow-growing, manageable-but-incurable, and prone to transformation into aggressive DLBCL (Richter for CLL); they differ in origin—germinal-center FL with t(14;18)/BCL2 vs CD5+ post-GC CLL.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Follicular lymphoma is a disease of the lymphatic system: malignant germinal-center B cells expand lymph-node follicles, producing the waxing-and-waning painless lymphadenopathy that is its hallmark, with spread to spleen and marrow; many cases are watched while asymptomatic.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Follicular lymphoma arises directly from the germinal center: a malignancy of follicle-center B cells frozen mid-reaction that recapitulates follicular architecture, and its founding t(14;18) drives constitutive BCL2 to block the apoptosis that normally prunes these cells.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Follicular and Hodgkin lymphomas both arise from germinal-center B cells but behave oppositely: follicular is indolent, BCL2-driven and incurable, smoldering for years, while Hodgkin's Reed-Sternberg tumor is aggressive yet highly curable—indolence versus curability.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Follicular and Burkitt lymphomas are germinal-center B-cell tumors at opposite tempos: follicular is slow, BCL2 [t(14;18)]-driven and incurable, while Burkitt is the fastest-growing human tumor, MYC [t(8;14)]-driven yet curable—each named by its translocation.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Follicular lymphoma and multiple myeloma are both incurable B-lineage malignancies at different maturation stages: FL is a CD20+ germinal-center B-cell tumor, myeloma a marrow plasma-cell cancer secreting monoclonal protein—both relapse and remit over years.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Follicular lymphoma depends on follicular helper T cells in its microenvironment: the malignant B cells need Tfh signals and a supportive niche to survive, so FL is as much a disease of the microenvironment as of the B cell—explaining its indolent, relapsing course.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Follicular lymphoma is a germinal-center B cell blocked from becoming a plasma cell: the t(14;18) BCL2 translocation lets it resist apoptosis and accumulate instead of maturing into antibody-secreting cells—an indolent buildup unlike high-grade lymphomas.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Follicular lymphoma's behavior is shaped by immune surveillance: the microenvironment can restrain or enable the tumor, and FL can spontaneously regress or transform—so immune-modulating therapies (rituximab, lenalidomide) are central to its largely incurable course.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Follicular lymphoma usually involves the bone marrow at diagnosis: the indolent clone seeds marrow in a paratrabecular pattern, so it is typically advanced-stage yet slow-growing—curative local therapy is rarely possible, but it can be watched or controlled for years.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy can cure the rare localized follicular lymphoma: low-dose photon radiation to a single involved site is potentially curative in stage I disease, a notable exception in a lymphoma that is otherwise incurable but indolent and managed over many years.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Follicular lymphoma can transform and reach the nervous system: histologic transformation to aggressive DLBCL—and rarely CNS involvement—marks a turn for the worse in this usually indolent disease, shifting management from watchful waiting to intensive therapy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Follicular lymphoma is built on follicular dendritic cells: these stromal cells form the germinal-center meshwork the malignant B cells depend on for survival signals, so the tumor recreates a follicle—its microenvironment shaping when indolent disease turns aggressive.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Follicular lymphoma now yields to T-cell therapies: CD19 CAR-T cells and CD20×CD3 bispecifics (mosunetuzumab) redirect cytotoxic T cells against the B-cell clone, giving durable remissions in this otherwise relapsing, incurable indolent lymphoma.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Follicular lymphoma is usually widespread at diagnosis, infiltrating the liver: indolent but disseminated, it commonly involves liver, spleen, and marrow by the time it is found—so it is staged as advanced yet often watched rather than treated.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^marcus-2017-gallium]: Marcus R, Davies A, Ando K, et al. Obinutuzumab for the first-line treatment of follicular lymphoma. *N Engl J Med.* 2017;377(14):1331-1344. [doi:10.1056/NEJMoa1614598](https://doi.org/10.1056/NEJMoa1614598) · [PubMed 28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/)
[^morschhauser-2020-tazemetostat]: Morschhauser F, Tilly H, Chaidos A, et al. Tazemetostat for patients with relapsed or refractory follicular lymphoma (E7438-G-003). *Lancet Oncol.* 2020;21(11):1433-1442. [doi:10.1016/S1470-2045(20)30441-1](https://doi.org/10.1016/S1470-2045(20)30441-1) · [PubMed 33035457](https://pubmed.ncbi.nlm.nih.gov/33035457/)
