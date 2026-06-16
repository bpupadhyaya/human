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
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2 gain-of-function mutations (Y641F/N, ~20% GCB-DLBCL) silence differentiation genes via H3K27me3; tazemetostat (EZH2i) FDA-approved for R/R follicular lymphoma; EZH2-mutant DLBCL shows activity with tazemetostat+R-CHOP; CREBBP co-mutation reduces tazemetostat sensitivity."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "DLBCL arises from FL transformation (~3%/year); transformed FL-DLBCL shares t(14;18)/BCL-2 and KMT2D with FL but acquires MYC rearrangement, CDKN2A deletion, or TP53 mutation → worse prognosis than de novo DLBCL; CAR-T consolidation is preferred after induction."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 is the essential rituximab target in R-CHOP; CD20 loss (mutation, methylation, shedding) → rituximab resistance; bispecifics (epcoritamab, glofitamab) bind CD3×CD20 at low CD20 expression; CD19-directed ADCs (loncastuximab) and CAR-T are CD20-loss-resistant alternatives."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "DLBCL is a malignancy of mature B cells whose two subtypes mirror the cell of origin: germinal-center B-cell DLBCL carries the germinal center's BCL-2 translocation, while activated B-cell DLBCL resembles a post-germinal-center plasmablast driven by chronic BCR/NF-κB signaling."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Epstein-Barr virus drives a distinct, more aggressive subtype — EBV-positive DLBCL — chiefly in older or immunosuppressed patients; viral LMP1 and EBNA proteins switch on NF-κB to keep the B cell alive, the same mechanism behind post-transplant lymphoproliferative disease."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Distinguishing DLBCL from Burkitt lymphoma is treatment-critical: both are aggressive GC B-cell tumors, but Burkitt has a pure MYC translocation, near-100% Ki-67, and no BCL-2, whereas a MYC-plus-BCL-2 'double-hit' large-cell lymphoma sits between them and does poorly on R-CHOP."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "DLBCL is the endpoint of Richter transformation: in ~5-10% of CLL the indolent clone evolves into aggressive, often clonally-related diffuse large B-cell lymphoma; this transformation, likelier on BTK-inhibitor therapy, links the commonest indolent and aggressive B-cell cancers."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Primary CNS lymphoma is a DLBCL confined to the brain, eyes and CSF: an aggressive activated-B-cell-type lymphoma that, behind the blood-brain barrier, needs high-dose methotrexate-based regimens rather than standard R-CHOP, and is far more common in immunosuppression."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "DLBCL is classified by its germinal-center relationship: the germinal-center B-cell (GCB) subtype, with BCL2/BCL6 rearrangements, has a better prognosis than the activated B-cell (ABC) subtype driven by chronic NF-κB signaling—a cell-of-origin split that guides therapy."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "DLBCL and mantle cell lymphoma are aggressive B-cell non-Hodgkin lymphomas differing at the core: MCL is defined by t(11;14) cyclin D1 overexpression driving cell-cycle escape, while DLBCL is heterogeneous (GCB vs ABC)—both CD20+ and treated with rituximab regimens."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "DLBCL and Hodgkin lymphoma are both germinal-center B-cell lymphomas but diverge: Hodgkin's malignant Reed-Sternberg cells are sparse amid reactive infiltrate and often EBV-driven, while DLBCL is a sheet of malignant B cells—Hodgkin is highly curable, DLBCL in ~60%."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "DLBCL and multiple myeloma are B-lineage cancers at opposite ends of differentiation: myeloma is a plasma-cell tumor flooding marrow and secreting monoclonal immunoglobulin, while DLBCL is a CD20+ lymph-node B-cell tumor—DLBCL can transform to plasmablastic forms."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "DLBCL spans the B-cell-to-plasma-cell transition: the GCB subtype resembles germinal-center B cells while the ABC subtype leans toward plasma-cell differentiation—and the plasmablastic variant nearly resembles a plasma cell, so cell-of-origin shapes prognosis."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV greatly raises DLBCL risk: immunosuppression and EBV co-infection drive aggressive AIDS-related lymphomas, including DLBCL and its plasmablastic variant—so a new mass in an HIV patient prompts lymphoma workup, and antiretroviral therapy is part of treatment."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation marks high-risk DLBCL: loss of p53 function, often with MYC and BCL2 rearrangements (double/triple-hit lymphoma), predicts resistance to R-CHOP and poor survival—so molecular testing now guides intensified or novel therapy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "DLBCL is the most common aggressive lymphoma of the lymphatic system: it usually presents as rapidly enlarging lymph nodes or an extranodal mass, and because it is fast-growing it is paradoxically curable in many with R-CHOP immunochemotherapy."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "DLBCL can involve the bone marrow, worsening prognosis: marrow infiltration upstages the disease and may cause cytopenias, so staging includes marrow assessment—and concordant large-cell marrow involvement portends a worse outcome than discordant low-grade disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy complements chemo in localized DLBCL: photon-beam radiation to involved sites consolidates limited-stage disease after abbreviated R-CHOP and treats bulky masses, so it remains part of curative therapy alongside immunochemotherapy and CAR-T for relapse."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "DLBCL is a triumph of T-cell therapy: CD19-directed CAR-T cells re-engineer the patient's cytotoxic T cells to kill the lymphoma, curing many with relapsed disease—so T cells are now a frontline weapon against this most common aggressive lymphoma."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "DLBCL is the commonest extranodal lymphoma of the stomach: it can arise there directly or transform from indolent gastric MALT lymphoma, so a stomach mass or ulcer that is lymphoma, not carcinoma, changes treatment entirely toward chemo-immunotherapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages shape DLBCL's fate: tumor-associated macrophages and the CD47 'don't-eat-me' signal let lymphoma cells evade clearance, so blocking CD47 to unleash macrophage phagocytosis is an emerging therapeutic strategy."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "The aggressive ABC subtype of DLBCL is addicted to BTK: chronic B-cell-receptor signaling through Bruton's tyrosine kinase keeps NF-κB switched on, so BTK inhibitors like ibrutinib are aimed at this molecular subset of the lymphoma."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "DLBCL can arise in or invade the spleen: primary splenic large B-cell lymphoma and splenic involvement of nodal disease cause massive splenomegaly, so an enlarging spleen with B-symptoms can be the face of this aggressive lymphoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "DLBCL is increasingly attacked with NK-cell therapy: beyond CAR-T against CD19, engineered NK cells and antibodies that engage NK killing are being developed to clear large B-cell lymphoma, harnessing innate cytotoxicity."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "DLBCL can trigger tumor lysis when treated: this fast-growing lymphoma sheds huge numbers of cells under chemotherapy, dumping potassium into the blood, so hyperkalemia must be anticipated and prevented in bulky disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "DLBCL can invade or relapse in the brain: secondary CNS involvement carries a grim prognosis, so high-risk patients receive CNS-directed prophylaxis to reach a sanctuary that standard chemotherapy penetrates poorly."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells shape the immune fight against DLBCL: as antigen-presenters they prime T-cell responses to the lymphoma, and harnessing them is explored to boost immunity alongside CD20 antibodies and CAR-T therapy."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "DLBCL drains the body's iron and blood: marrow involvement and chronic inflammation suppress red-cell production and lock iron away, so anemia commonly accompanies this aggressive lymphoma."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "DLBCL spreads beyond nodes into the liver: as an aggressive lymphoma it seeds extranodal organs, infiltrating the liver to cause hepatomegaly and abnormal liver tests in advanced disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "DLBCL shields itself with regulatory T cells: the lymphoma microenvironment recruits Tregs that suppress the antitumor immune response, a factor in prognosis and a barrier for immunotherapy."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "DLBCL's bulky tumor lyses fast on treatment: dying cells spill phosphate and potassium in tumor lysis syndrome, a metabolic emergency at the start of chemotherapy that needs prevention."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "DLBCL has a skin form: primary cutaneous DLBCL, leg type, appears as firm red-brown nodules, and systemic lymphoma can also infiltrate the skin."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "DLBCL can invade the nerves: neurolymphomatosis, infiltration of peripheral nerves and roots, causes painful neuropathy, a rare and aggressive pattern of spread."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows DLBCL's namesake cell: a large lymphoid blast with abundant cytoplasm, dispersed chromatin, and prominent nucleoli — the big, fast-dividing B cell that gives diffuse large B-cell lymphoma its name."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "DLBCL can both infiltrate and overwhelm the kidney: lymphoma deposits enlarge it directly, and as chemotherapy bursts the bulky tumor in tumor lysis syndrome, urate and phosphate crystals clog the tubules into acute failure."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Treating DLBCL swings the calcium: tumor lysis releases a flood of phosphate that binds calcium, dropping it sharply, a metabolic emergency watched for as the rapidly dividing lymphoma dies under therapy."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "DLBCL was the proving ground for antibody therapy: adding rituximab (anti-CD20) to CHOP transformed survival, and bispecific antibodies and CAR-T now rescue relapsed disease — making it a showcase of immunotherapy."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "DLBCL threatens the nervous system twice: high-risk disease seeds the CNS, prompting intrathecal prophylaxis, while the vincristine in R-CHOP poisons peripheral neurons into a dose-limiting neuropathy."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The cure can weaken the heart: doxorubicin — the 'H' (hydroxydaunorubicin) of R-CHOP — is cumulatively cardiotoxic, so cardiac function is checked before treatment and watched for a later cardiomyopathy."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Anthracyclines kill heart muscle cells directly: doxorubicin poisons topoisomerase-2-beta and floods cardiomyocytes with reactive oxygen, causing irreversible cell loss — the cellular basis of the dose-limiting cardiotoxicity, blunted by dexrazoxane."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Rituximab can wake a sleeping virus: by stripping out B cells it lifts the immune control of hepatitis B, so patients are screened and given antiviral prophylaxis before R-CHOP to prevent a dangerous viral reactivation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The aggressive ABC subtype runs on chronic signaling: alongside constitutive NF-kB, JAK-STAT3 activation drives survival in activated B-cell DLBCL, marking worse-prognosis tumors and a pathway probed by JAK and STAT inhibitors."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF feeds the malignant B cell: the survival cytokine supports DLBCL cells, especially the NF-κB-addicted activated B-cell subtype, one of the microenvironmental lifelines the lymphoma exploits."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "The newest cure can trigger a storm: CD19 CAR-T therapy for relapsed DLBCL routinely sets off cytokine release syndrome as the engineered cells attack, managed with the IL-6 blocker tocilizumab."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T cells fill and shape the tumor: follicular-helper and other T cells in the DLBCL microenvironment can either support or restrain the lymphoma, and the T-cell-rich variants behave and respond differently."
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
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2 gain-of-function mutations (Y641F/N, ~20% GCB-DLBCL) silence differentiation genes via H3K27me3; tazemetostat (EZH2i) FDA-approved for R/R follicular lymphoma; EZH2-mutant DLBCL shows activity with tazemetostat+R-CHOP; CREBBP co-mutation reduces tazemetostat sensitivity.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — DLBCL arises from FL transformation (~3%/year); transformed FL-DLBCL shares t(14;18)/BCL-2 and KMT2D with FL but acquires MYC rearrangement, CDKN2A deletion, or TP53 mutation → worse prognosis than de novo DLBCL; CAR-T consolidation is preferred after induction.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 is the essential rituximab target in R-CHOP; CD20 loss (mutation, methylation, shedding) → rituximab resistance; bispecifics (epcoritamab, glofitamab) bind CD3×CD20 at low CD20 expression; CD19-directed ADCs (loncastuximab) and CAR-T are CD20-loss-resistant alternatives.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — DLBCL is a malignancy of mature B cells whose two subtypes mirror the cell of origin: germinal-center B-cell DLBCL carries the germinal center's BCL-2 translocation, while activated B-cell DLBCL resembles a post-germinal-center plasmablast driven by chronic BCR/NF-κB signaling.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Epstein-Barr virus drives a distinct, more aggressive subtype — EBV-positive DLBCL — chiefly in older or immunosuppressed patients; viral LMP1 and EBNA proteins switch on NF-κB to keep the B cell alive, the same mechanism behind post-transplant lymphoproliferative disease.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Distinguishing DLBCL from Burkitt lymphoma is treatment-critical: both are aggressive GC B-cell tumors, but Burkitt has a pure MYC translocation, near-100% Ki-67, and no BCL-2, whereas a MYC-plus-BCL-2 'double-hit' large-cell lymphoma sits between them and does poorly on R-CHOP.
- `connects-to` → **[CLL](../cll/README.md)** — DLBCL is the endpoint of Richter transformation: in ~5-10% of CLL the indolent clone evolves into aggressive, often clonally-related diffuse large B-cell lymphoma; this transformation, likelier on BTK-inhibitor therapy, links the commonest indolent and aggressive B-cell cancers.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Primary CNS lymphoma is a DLBCL confined to the brain, eyes and CSF: an aggressive activated-B-cell-type lymphoma that, behind the blood-brain barrier, needs high-dose methotrexate-based regimens rather than standard R-CHOP, and is far more common in immunosuppression.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — DLBCL is classified by its germinal-center relationship: the germinal-center B-cell (GCB) subtype, with BCL2/BCL6 rearrangements, has a better prognosis than the activated B-cell (ABC) subtype driven by chronic NF-κB signaling—a cell-of-origin split that guides therapy.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — DLBCL and mantle cell lymphoma are aggressive B-cell non-Hodgkin lymphomas differing at the core: MCL is defined by t(11;14) cyclin D1 overexpression driving cell-cycle escape, while DLBCL is heterogeneous (GCB vs ABC)—both CD20+ and treated with rituximab regimens.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — DLBCL and Hodgkin lymphoma are both germinal-center B-cell lymphomas but diverge: Hodgkin's malignant Reed-Sternberg cells are sparse amid reactive infiltrate and often EBV-driven, while DLBCL is a sheet of malignant B cells—Hodgkin is highly curable, DLBCL in ~60%.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — DLBCL and multiple myeloma are B-lineage cancers at opposite ends of differentiation: myeloma is a plasma-cell tumor flooding marrow and secreting monoclonal immunoglobulin, while DLBCL is a CD20+ lymph-node B-cell tumor—DLBCL can transform to plasmablastic forms.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — DLBCL spans the B-cell-to-plasma-cell transition: the GCB subtype resembles germinal-center B cells while the ABC subtype leans toward plasma-cell differentiation—and the plasmablastic variant nearly resembles a plasma cell, so cell-of-origin shapes prognosis.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV greatly raises DLBCL risk: immunosuppression and EBV co-infection drive aggressive AIDS-related lymphomas, including DLBCL and its plasmablastic variant—so a new mass in an HIV patient prompts lymphoma workup, and antiretroviral therapy is part of treatment.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation marks high-risk DLBCL: loss of p53 function, often with MYC and BCL2 rearrangements (double/triple-hit lymphoma), predicts resistance to R-CHOP and poor survival—so molecular testing now guides intensified or novel therapy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — DLBCL is the most common aggressive lymphoma of the lymphatic system: it usually presents as rapidly enlarging lymph nodes or an extranodal mass, and because it is fast-growing it is paradoxically curable in many with R-CHOP immunochemotherapy.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — DLBCL can involve the bone marrow, worsening prognosis: marrow infiltration upstages the disease and may cause cytopenias, so staging includes marrow assessment—and concordant large-cell marrow involvement portends a worse outcome than discordant low-grade disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy complements chemo in localized DLBCL: photon-beam radiation to involved sites consolidates limited-stage disease after abbreviated R-CHOP and treats bulky masses, so it remains part of curative therapy alongside immunochemotherapy and CAR-T for relapse.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — DLBCL is a triumph of T-cell therapy: CD19-directed CAR-T cells re-engineer the patient's cytotoxic T cells to kill the lymphoma, curing many with relapsed disease—so T cells are now a frontline weapon against this most common aggressive lymphoma.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — DLBCL is the commonest extranodal lymphoma of the stomach: it can arise there directly or transform from indolent gastric MALT lymphoma, so a stomach mass or ulcer that is lymphoma, not carcinoma, changes treatment entirely toward chemo-immunotherapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages shape DLBCL's fate: tumor-associated macrophages and the CD47 'don't-eat-me' signal let lymphoma cells evade clearance, so blocking CD47 to unleash macrophage phagocytosis is an emerging therapeutic strategy.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — The aggressive ABC subtype of DLBCL is addicted to BTK: chronic B-cell-receptor signaling through Bruton's tyrosine kinase keeps NF-κB switched on, so BTK inhibitors like ibrutinib are aimed at this molecular subset of the lymphoma.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — DLBCL can arise in or invade the spleen: primary splenic large B-cell lymphoma and splenic involvement of nodal disease cause massive splenomegaly, so an enlarging spleen with B-symptoms can be the face of this aggressive lymphoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — DLBCL is increasingly attacked with NK-cell therapy: beyond CAR-T against CD19, engineered NK cells and antibodies that engage NK killing are being developed to clear large B-cell lymphoma, harnessing innate cytotoxicity.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — DLBCL can trigger tumor lysis when treated: this fast-growing lymphoma sheds huge numbers of cells under chemotherapy, dumping potassium into the blood, so hyperkalemia must be anticipated and prevented in bulky disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — DLBCL can invade or relapse in the brain: secondary CNS involvement carries a grim prognosis, so high-risk patients receive CNS-directed prophylaxis to reach a sanctuary that standard chemotherapy penetrates poorly.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells shape the immune fight against DLBCL: as antigen-presenters they prime T-cell responses to the lymphoma, and harnessing them is explored to boost immunity alongside CD20 antibodies and CAR-T therapy.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — DLBCL drains the body's iron and blood: marrow involvement and chronic inflammation suppress red-cell production and lock iron away, so anemia commonly accompanies this aggressive lymphoma.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — DLBCL spreads beyond nodes into the liver: as an aggressive lymphoma it seeds extranodal organs, infiltrating the liver to cause hepatomegaly and abnormal liver tests in advanced disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — DLBCL shields itself with regulatory T cells: the lymphoma microenvironment recruits Tregs that suppress the antitumor immune response, a factor in prognosis and a barrier for immunotherapy.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — DLBCL's bulky tumor lyses fast on treatment: dying cells spill phosphate and potassium in tumor lysis syndrome, a metabolic emergency at the start of chemotherapy that needs prevention.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — DLBCL has a skin form: primary cutaneous DLBCL, leg type, appears as firm red-brown nodules, and systemic lymphoma can also infiltrate the skin.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — DLBCL can invade the nerves: neurolymphomatosis, infiltration of peripheral nerves and roots, causes painful neuropathy, a rare and aggressive pattern of spread.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows DLBCL's namesake cell: a large lymphoid blast with abundant cytoplasm, dispersed chromatin, and prominent nucleoli — the big, fast-dividing B cell that gives diffuse large B-cell lymphoma its name.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — DLBCL can both infiltrate and overwhelm the kidney: lymphoma deposits enlarge it directly, and as chemotherapy bursts the bulky tumor in tumor lysis syndrome, urate and phosphate crystals clog the tubules into acute failure.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Treating DLBCL swings the calcium: tumor lysis releases a flood of phosphate that binds calcium, dropping it sharply, a metabolic emergency watched for as the rapidly dividing lymphoma dies under therapy.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — DLBCL was the proving ground for antibody therapy: adding rituximab (anti-CD20) to CHOP transformed survival, and bispecific antibodies and CAR-T now rescue relapsed disease — making it a showcase of immunotherapy.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — DLBCL threatens the nervous system twice: high-risk disease seeds the CNS, prompting intrathecal prophylaxis, while the vincristine in R-CHOP poisons peripheral neurons into a dose-limiting neuropathy.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The cure can weaken the heart: doxorubicin — the 'H' (hydroxydaunorubicin) of R-CHOP — is cumulatively cardiotoxic, so cardiac function is checked before treatment and watched for a later cardiomyopathy.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Anthracyclines kill heart muscle cells directly: doxorubicin poisons topoisomerase-2-beta and floods cardiomyocytes with reactive oxygen, causing irreversible cell loss — the cellular basis of the dose-limiting cardiotoxicity, blunted by dexrazoxane.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Rituximab can wake a sleeping virus: by stripping out B cells it lifts the immune control of hepatitis B, so patients are screened and given antiviral prophylaxis before R-CHOP to prevent a dangerous viral reactivation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The aggressive ABC subtype runs on chronic signaling: alongside constitutive NF-kB, JAK-STAT3 activation drives survival in activated B-cell DLBCL, marking worse-prognosis tumors and a pathway probed by JAK and STAT inhibitors.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF feeds the malignant B cell: the survival cytokine supports DLBCL cells, especially the NF-κB-addicted activated B-cell subtype, one of the microenvironmental lifelines the lymphoma exploits.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — The newest cure can trigger a storm: CD19 CAR-T therapy for relapsed DLBCL routinely sets off cytokine release syndrome as the engineered cells attack, managed with the IL-6 blocker tocilizumab.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T cells fill and shape the tumor: follicular-helper and other T cells in the DLBCL microenvironment can either support or restrain the lymphoma, and the T-cell-rich variants behave and respond differently.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^coiffier-2002-rchop]: Coiffier B, Lepage E, Brière J, et al. CHOP chemotherapy plus rituximab compared with CHOP alone in elderly patients with diffuse large-B-cell lymphoma. *N Engl J Med.* 2002;346(4):235-242. [doi:10.1056/NEJMoa011795](https://doi.org/10.1056/NEJMoa011795) · [PubMed 11807147](https://pubmed.ncbi.nlm.nih.gov/11807147/)
[^neelapu-2017-axicel]: Neelapu SS, Locke FL, Bartlett NL, et al. Axicabtagene ciloleucel CAR T-cell therapy in refractory large B-cell lymphoma. *N Engl J Med.* 2017;377(26):2531-2544. [doi:10.1056/NEJMoa1707447](https://doi.org/10.1056/NEJMoa1707447) · [PubMed 29226797](https://pubmed.ncbi.nlm.nih.gov/29226797/)
