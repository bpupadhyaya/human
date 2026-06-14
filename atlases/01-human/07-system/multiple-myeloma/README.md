---
schema: human-scale-entry/v1
id: multiple-myeloma
name: Multiple Myeloma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Plasma cell malignancy driven by CCND1 translocations (t(11;14)), RAS-MAPK mutations, and MYC. Bortezomib, lenalidomide, and daratumumab transformed outcomes; venetoclax is active in t(11;14) MM; BCMA-targeted CAR-T (cilta-cel, ide-cel) and bispecifics (teclistamab) are approved."
aliases: ["MM", "myeloma", "plasma cell myeloma", "Kahler disease", "RRMM", "relapsed/refractory myeloma", "smoldering myeloma", "MGUS", "PCM"]
sources:
  - id: kumar-2022-imwg-criteria
    type: peer-reviewed
    cite: "Kumar SK, Callander NS, Adekola K, et al. Multiple myeloma, version 3.2021, NCCN clinical practice guidelines in oncology. J Natl Compr Canc Netw. 2020;18(12):1685-1717."
    doi: "10.6004/jnccn.2020.0057"
    pmid: "33285519"
    url: "https://doi.org/10.6004/jnccn.2020.0057"
  - id: moreau-2022-teclistamab
    type: peer-reviewed
    cite: "Moreau P, Garfall AL, van de Donk NWCJ, et al. Teclistamab in relapsed or refractory multiple myeloma. N Engl J Med. 2022;387(6):495-505."
    doi: "10.1056/NEJMoa2203478"
    pmid: "35661166"
    url: "https://doi.org/10.1056/NEJMoa2203478"
  - id: martin-2023-carvykti
    type: peer-reviewed
    cite: "San-Miguel J, Dhakal B, Yong K, et al. Cilta-cel or standard care in lenalidomide-refractory multiple myeloma. N Engl J Med. 2023;389(4):335-347."
    doi: "10.1056/NEJMoa2303379"
    pmid: "37285856"
    url: "https://doi.org/10.1056/NEJMoa2303379"
cross_links:
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is the primary myeloma cell survival cytokine; BMSCs produce IL-6 in response to myeloma adhesion → JAK1/2-STAT3 → MCL-1 and BCL-XL → anti-apoptosis; serum IL-6 and CRP correlate with disease activity; tocilizumab has limited clinical activity in MM."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC is dysregulated in ~50-80% of relapsed MM via chr 8q24 amplification and MMSET-driven histone methylation; MYC drives plasma cell proliferation and immunoglobulin switch recombination; MYC transcription is sensitive to BET bromodomain inhibitors in MM models."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 is selectively overexpressed in t(11;14) MM (~15%); t(11;14) juxtaposes CCND1 near the IgH enhancer and correlates with BCL-2-high/BCL-XL-low expression; venetoclax achieves ORR ~40% in t(11;14) relapsed MM; CANOVA trial evaluated venetoclax + dexamethasone."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF is produced by myeloma cells and BMSCs → bone marrow angiogenesis → disease progression; VEGF promotes myeloma survival via VEGFR → PI3K-AKT; thalidomide and lenalidomide exert anti-angiogenic effects via VEGF suppression; bortezomib reduces VEGF secretion."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "MM cells secrete RANKL → osteoclast hyperactivation → osteolytic lesions and hypercalcemia; MM cells exploit OPG TRAIL-decoy function for survival; Xgeva (denosumab 120 mg Q4W) reduces skeletal-related events in MM bone disease."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "MM-secreted DKK1 and osteocyte sclerostin synergistically block osteoblast Wnt → uncoupled osteolysis; sclerostin inhibition in MM preclinical models restores osteoblast function and reduces lytic lesions; anti-DKK1 antibody (BHQ880) is in clinical trials for MM bone disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "MM plasma cells use CXCL12/CXCR4 for bone marrow homing and survival; plerixafor (AMD3100, CXCR4 antagonist) + G-CSF mobilizes HSC for ASCT in MM (AMBER trial: superior day-1 CD34+ yield); CXCR4 expression on MM cells associates with marrow retention and drug resistance."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Multiple myeloma is a malignancy of plasma cells — antibody-secreting terminal B cells — that clonally expand in the marrow and pour out a single monoclonal immunoglobulin (M-protein); their prolific secretory machinery makes them exquisitely sensitive to proteasome inhibitors."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Multiple myeloma lives in the bone marrow, where malignant plasma cells co-opt stromal cells for IL-6 and CXCL12 survival signals and tip the RANKL/OPG balance toward osteoclasts; marrow plasma cells ≥10% (or a biopsy-proven plasmacytoma) plus CRAB features define the diagnosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a major myeloma target: filtered monoclonal free light chains precipitate with Tamm-Horsfall protein into obstructing tubular casts (cast nephropathy), and with hypercalcemia cause the renal failure of CRAB — reversible if light-chain production is cut quickly."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Multiple myeloma and Waldenström macroglobulinemia are both monoclonal plasma-cell/B-cell dyscrasias secreting a paraprotein but differ: myeloma makes IgG/IgA with lytic bone disease and renal failure, WM makes IgM with hyperviscosity and the MYD88 L265P mutation."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Myeloma bone disease uncouples bone remodeling: tumor cells secrete DKK-1 and sclerostin that suppress osteoblasts and RANKL that activates osteoclasts, so the pure lytic lesions show no reactive new bone (cold on bone scan)—anti-RANKL agents aim to reset this."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Multiple myeloma is defined by a monoclonal immunoglobulin: the plasma-cell clone secretes a single intact IgG (or IgA) or free light chain—the M-protein seen as a serum spike—whose level tracks disease, while suppression of normal immunoglobulins causes myeloma's infection risk."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is central to myeloma's CRAB complications: tumor-driven RANKL activates osteoclasts that dissolve bone, releasing calcium into blood—hypercalcemia causes confusion, constipation and kidney injury, treated urgently with hydration and bisphosphonates."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Myeloma bone disease and osteoporosis both fracture vertebrae but differ: myeloma carves discrete lytic 'punched-out' lesions, while osteoporosis is diffuse low bone density—new vertebral fractures in an older adult warrant a myeloma work-up."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is a key palliative tool in myeloma: though systemic, the disease responds to localized radiation that relieves bone pain and treats impending fractures, and is curative for solitary plasmacytoma—complementing the drugs that control marrow disease."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Multiple myeloma is the malignant end of B-cell maturation: it arises when a B cell becomes a clonal plasma cell, evolving from MGUS through smoldering myeloma—a step beyond the B cell, secreting monoclonal immunoglobulin instead of fighting infection."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Myeloma hijacks osteoclasts to destroy bone: malignant plasma cells secrete RANKL and cytokines that overactivate osteoclasts while suppressing osteoblasts, carving the punched-out lytic lesions, hypercalcemia and fractures that define myeloma bone disease."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Multiple myeloma and DLBCL are B-lineage cancers at opposite maturation ends: DLBCL is an aggressive nodal large B-cell lymphoma, myeloma a marrow plasma-cell tumor secreting monoclonal protein—and rarely a plasmablastic lymphoma blurs the line between them."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Anemia is a defining feature of multiple myeloma: plasma cells crowd the marrow and their cytokines suppress red-cell production, so falling hemoglobin (one of the CRAB criteria) is a common presenting sign alongside bone pain and renal failure."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Multiple myeloma cripples the immune system: as it expands one plasma-cell clone, normal antibody production collapses (immunoparesis), so recurrent infection is a top cause of death—and CD38-targeting and T-cell therapies now turn immunity back against the tumor."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Multiple myeloma is the malignant end of the B-cell lineage of the lymphatic system: it arises from plasma cells—the antibody factories that B cells become—so it produces a monoclonal immunoglobulin (M-protein) while crowding out normal immunity."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Multiple myeloma is a frontier for engineered T cells: BCMA-directed CAR-T cells and T-cell-engaging bispecific antibodies redirect cytotoxic T cells to kill plasma cells, producing deep remissions in disease that has relapsed after every drug class."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Antibody therapy for myeloma works through NK cells: daratumumab against CD38 and elotuzumab tag plasma cells for natural-killer-cell killing (ADCC), making these antibodies a backbone of modern treatment."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Myeloma plasma cells depend on NF-kB for survival: the bone-marrow niche and genetic lesions keep this pathway switched on, and proteasome inhibitors like bortezomib work partly by blocking NF-kB activation—starving the cell of its survival signal."
---

# Multiple Myeloma

## Overview

**Multiple myeloma (MM)** is a hematologic malignancy of terminally differentiated **plasma cells** — long-lived antibody-secreting B cells resident in the bone marrow. Malignant plasma cells accumulate in the bone marrow → monoclonal immunoglobulin (M-protein) production → end-organ damage (**CRAB criteria**: hyperCalcemia, Renal failure, Anemia, Bone lesions). MM accounts for ~10% of all hematologic malignancies and ~1-2% of all cancers — approximately 35,000 new cases and 12,000 deaths annually in the United States [^kumar-2022-imwg-criteria].

MM evolves from precursor conditions through a well-defined continuum:
- **MGUS (monoclonal gammopathy of undetermined significance):** M-protein <3 g/dL, <10% plasma cells in marrow, no CRAB; prevalent (~3% of adults >50); risk of progression to MM/WM/lymphoma ~1%/year
- **Smoldering multiple myeloma (SMM):** M-protein ≥3 g/dL OR ≥10-60% plasma cells, no CRAB; higher progression risk (10-15%/year in high-risk SMM); treatment of high-risk SMM actively studied (AQUILA trial: daratumumab delays progression)
- **Active MM:** CRAB criteria or biomarkers of near-inevitable end-organ damage (>60% plasma cells, involved/uninvolved FLC ratio >100, >1 focal lesion on MRI)

**Epidemiology and risk factors:**
- African American populations have 2-3× higher incidence than white populations (higher MGUS prevalence); men slightly > women; median age at diagnosis ~69; rare <40
- Occupational exposures (ionizing radiation, benzene, herbicides) modestly increase risk
- Monoclonal B cell lineage origin: MM arises from post-germinal center, class-switched memory B cells that home to bone marrow → undergo somatic hypermutation → differentiate toward plasma cell fate but accumulate oncogenic events preventing terminal differentiation arrest

**Molecular subtypes (by primary cytogenetic event):**
- **Hyperdiploid MM (HRD, ~55%):** Odd-numbered chromosomal trisomies (3, 5, 7, 9, 11, 15, 19, 21); relatively favorable prognosis; commonly activates CCND1/D2/D3 via trisomy
- **Translocation-based MM (~45%):**
  - **t(11;14)(q13;q32) (~15-20%):** CCND1 → IgH enhancer; low grade, CD20+, lymphoplasmacytic morphology; BCL-2-high → venetoclax-sensitive; best prognosis among translocations
  - **t(4;14)(p16;q32) (~15%):** FGFR3 and MMSET (NSD2 histone methyltransferase) → H3K36me2 → global chromatin opening → MYC upregulation; intermediate prognosis; bortezomib partially overcomes poor prognosis; FGFR3 targeted (infigratinib) under study
  - **t(14;16)(q32;q23) (~5%):** MAF → cyclin D2, integrin β7, CCND2; worst prognosis; novel agents improving outcomes; MAF target gene upregulation drives adhesion and drug resistance
  - **t(14;20)(q32;q12) (~1%):** MAFB; similar biology to t(14;16); poor prognosis
  - **t(6;14)(p21;q32) (~2%):** CCND3 → IgH; favorable prognosis

**High-risk genomic features:**
- **del(17p13)/TP53 loss:** Most adverse prognostic factor; ~10% at diagnosis, ~30% in RRMM; monoallelic deletion → residual TP53 haplo-insufficient; biallelic → complete p53 loss; extremely poor prognosis; clinical trials specifically targeting del(17p) MM needed
- **t(4;14), t(14;16), t(14;20), del(1p), gain(1q21):** ISS (International Staging System) criteria for high risk; R-ISS (Revised ISS) incorporates LDH + del(17p) + t(4;14) + t(14;16) for stage I-III risk stratification
- **Gain(1q21)/amplification:** Most common secondary event (~40% at diagnosis, ~70% RRMM); correlates with disease progression; 1q21 contains CKS1B (CDK substrate) and MCL-1; 1q amp correlates with shorter PFS with standard therapy
- **Chromothripsis:** Catastrophic chromosomal rearrangement in ~10% of RRMM → rapid clonal evolution and drug resistance

## Structure

### Bone marrow microenvironment and myeloma biology

**Myeloma-bone marrow stromal cell (BMSC) interactions:**
- MM cells home to bone marrow via CXCL12 (SDF-1)-CXCR4 axis; CXCR4 is highly expressed on MM cells → marrow homing and retention; CXCR4 inhibitors (plerixafor) mobilize MM cells out of protective marrow niche → sensitization to chemotherapy (hypothetical)
- **VLA-4 (integrin α4β1)-VCAM-1 axis:** MM cell VLA-4 binds BMSC VCAM-1 → cell adhesion-mediated drug resistance (CAM-DR); integrin signaling → NF-kB → MCL-1 and BCL-XL → anti-apoptosis; this explains why in vitro drug sensitivity often overestimates clinical efficacy
- **IL-6 paracrine circuit:** MM-BMSC contact → BMSC IL-6 secretion (10-100× basal) → JAK1/2 → STAT3 → MCL-1, BCL-XL, VEGF → MM survival; elevated serum IL-6 and CRP (acute phase reactant) are MM disease activity biomarkers

**Plasma cell biology:**
- **IRF4, BLIMP1 (PRDM1), XBP1:** Master transcription factors of plasma cell identity; IRF4 is required for MM survival (IRF4 knockdown → MM apoptosis); BLIMP1 drives terminal differentiation and immunoglobulin secretion; XBP1 is the unfolded protein response (UPR) regulator of the ER secretory pathway — essential for managing massive Ig production
- **Immunoproteasome:** Plasma cells have extremely high proteasome activity to clear misfolded Ig chains; this dependence on proteasome → vulnerability to bortezomib (proteasome inhibitor → accumulation of misfolded proteins → UPR → CHOP → apoptosis); MM is uniquely sensitive among hematologic malignancies

**BCMA (B-cell maturation antigen, TNFRSF17):**
- BCMA is expressed selectively on plasma cells and MM cells (minimal normal tissue expression); binds APRIL and BAFF → NF-kB → plasma cell survival
- BCMA is the dominant target for new-generation MM immunotherapy: CAR-T cells (cilta-cel, ide-cel), bispecific T cell engagers (teclistamab, elranatamab), ADCs (belantamab mafodotin); BCMA is internalized rapidly after antibody binding → BCMA shedding (gamma-secretase cleavage → soluble BCMA) can compete for BCMA-targeting agents

**Osteolytic bone disease:**
- MM cells produce DKK1 (Wnt antagonist) and RANKL → osteoblast suppression + osteoclast activation → net bone destruction → lytic lesions, fractures, hypercalcemia
- Osteoclast-derived IL-6 and SDF-1 provide additional MM survival signals → bidirectional bone-myeloma crosstalk
- Bisphosphonates (zoledronic acid) and denosumab (anti-RANKL) are standard for all symptomatic MM — reduce skeletal-related events (SREs) and may have direct anti-myeloma effects (zoledronate inhibits osteoclast-derived IL-6)

## Function

### Clinical presentation and staging

**CRAB criteria (active MM requiring treatment):**
- **C** (Calcium): Serum calcium >11 mg/dL (>1 mg/dL above ULN)
- **R** (Renal): Creatinine >2 mg/dL or CrCl <40 mL/min attributable to myeloma (typically cast nephropathy from Ig light chains)
- **A** (Anemia): Hgb <10 g/dL or >2 g/dL below LLN; normochromic normocytic (bone marrow failure + EPO suppression)
- **B** (Bone): One or more lytic lesions on skeletal survey, CT, or PET-CT; or compression fractures

**Biomarkers of near-inevitable end-organ damage (SLiM-CRAB):**
- **S**ixty percent (≥60%) plasma cells in bone marrow
- **Li**ght chain ratio: Involved/uninvolved serum FLC ratio ≥100
- **M**RI: >1 focal lesion (≥5 mm) on MRI (independent of skeletal survey)

**M-protein characterization:**
- SPEP (serum protein electrophoresis) → M-spike quantification; immunofixation → M-protein isotype (IgG most common ~55%, IgA ~25%, IgD rare, IgE rare, non-secretory ~3%)
- **Serum free light chains (sFLC):** Kappa or lambda free light chains; FLC ratio (kappa/lambda or lambda/kappa) abnormal → diagnostic and monitoring value; FLC-only MM and non-secretory MM monitored exclusively by sFLC
- **Bence Jones protein (BJP):** Urinary light chains; 24-hour urine protein electrophoresis in all MM patients at diagnosis

**ISS and R-ISS staging:**
- **ISS:** Serum β2-microglobulin + albumin → Stage I (β2M <3.5, alb ≥3.5), II, III (β2M ≥5.5)
- **R-ISS:** ISS + del(17p)/t(4;14)/t(14;16) + LDH → Stage I-III; R-ISS III: 5-year OS ~40%

**Imaging:**
- Whole-body low-dose CT (WBLD-CT): Standard; detects lytic lesions ≥5 mm; superior to skeletal survey (plain X-ray); does not detect active marrow infiltration without lysis
- FDG-PET/CT: Detects active lesions (FDG-avid plasma cells); useful for staging, response assessment (complete metabolic response = good prognostic marker), and identifying extramedullary disease
- MRI: Best modality for spine involvement and bone marrow infiltration; diffuse low T1 signal → extensive marrow replacement; useful in smoldering MM for progression risk assessment

## Pathology

### Diagnosis

**Bone marrow biopsy and aspirate:** Required for diagnosis; clonal plasma cells identified by CD138+, CD38+, CD19- (unlike normal plasma cells — CD19+); light chain restriction (kappa or lambda clonal); flow cytometry and FISH (fluorescence in situ hybridization) for cytogenetic risk stratification

**FISH panel:** del(17p13), t(4;14), t(14;16), t(14;20), t(11;14), gain(1q21), del(1p32) — all at diagnosis; determines risk category and targeted therapy eligibility (t(11;14) → venetoclax)

**Minimal residual disease (MRD) assessment:**
- Next-generation flow (NGF, EuroFlow) or next-generation sequencing (NGS, clonoSEQ): Sensitivity 10^-5 to 10^-6; MRD negativity is a strong surrogate for PFS and OS in MM; FDA-approved as a clinical trial endpoint; MRD-guided treatment strategies (stopping therapy in MRD-neg patients, intensifying in MRD-pos) under active study (MASTER, MIDAS trials)

### Treatment

**Newly diagnosed multiple myeloma (NDMM) — transplant eligible:**
- **Induction (4-6 cycles):** VRd (bortezomib-lenalidomide-dexamethasone) or DaraVRd (daratumumab + VRd; PERSEUS trial: PFS benefit → FDA approved 2024)
- **Autologous stem cell transplant (ASCT):** High-dose melphalan (200 mg/m²) → stem cell rescue; PFS benefit vs. no transplant maintained in lenalidomide era (DETERMINATION trial); depth of response (MRD negativity) post-ASCT is key prognostic factor
- **Consolidation:** 2 additional cycles VRd (optional)
- **Maintenance:** Lenalidomide (10 mg/day) until progression (MYELOMA XI, CALGB 100104); daratumumab + lenalidomide if DaraVRd induction (AURIGA trial ongoing); bortezomib-based maintenance for del(17p)

**Newly diagnosed MM — transplant ineligible:**
- **DaraVMP** (daratumumab + bortezomib + melphalan + prednisone; ALCYONE): PFS and OS benefit; FDA approved
- **DaraRd** (daratumumab + lenalidomide + dexamethasone; MAIA): OS benefit vs. Rd; FDA approved for non-transplant NDMM
- **VRd-lite:** Bortezomib + lenalidomide + low-dose dexamethasone; standard for frail/elderly patients

**Relapsed/refractory myeloma (RRMM):**
- **Second-line after 1-3 prior lines (with daratumumab exposure):**
  - Carfilzomib (next-gen proteasome inhibitor, irreversible) + Rd (KRd; ASPIRE trial)
  - Isatuximab (anti-CD38) + carfilzomib + Rd (IsaKRd)
  - Elotuzumab (anti-SLAMF7) + Rd (ELOQUENT-2)
  - Ixazomib (oral proteasome inhibitor) + Rd (TOURMALINE-MM1)
- **Venetoclax:** t(11;14) MM; ORR ~40% in monotherapy; venetoclax + dexamethasone (CANOVA trial); BCL-2 dependence in t(11;14) due to low MCL-1/low BCL-XL expression; venetoclax + bortezomib (BELLINI trial showed OS detriment in non-t(11;14) → restrict to t(11;14))
- **BCMA-directed therapies [^moreau-2022-teclistamab] [^martin-2023-carvykti]:**
  - **Teclistamab (Tecvayli):** Anti-BCMA × anti-CD3 bispecific; ORR 63% in RRMM ≥3 prior lines (MajesTEC-1); FDA approved 2022; CRS (step-up dosing) and infections are key toxicities
  - **Elranatamab (Elrexfio):** Anti-BCMA × anti-CD3; ORR 61% (MagnetisMM-3); FDA approved 2023
  - **Idecabtagene vicleucel (ide-cel, Abecma):** BCMA-directed CAR-T; ORR 73% in triple-class refractory MM (KarMMa); FDA approved 2021; CRS and neurotoxicity; 4-1BB costimulatory domain
  - **Ciltacabtagene autoleucel (cilta-cel, Carvykti):** BCMA-targeted CAR-T; ORR 98% in RRMM ≥3 prior lines (CARTITUDE-1); PFS 27.7 months; FDA approved 2022; FDA approved in 2nd-line (CARTITUDE-4: superior PFS vs. standard therapy in 1-3 prior lines) [^martin-2023-carvykti]
  - **Belantamab mafodotin (Blenrep):** ADC; corneal toxicity (keratopathy → blurred vision) led to initial FDA withdrawal; restored conditional approval 2023 with DREAMM-3 data vs. pomalidomide
- **GPRC5D-directed bispecifics:** Talquetamab (anti-GPRC5D × anti-CD3); ORR 73% in RRMM (MonumenTAL-1); GPRC5D expressed on plasma cells and hair follicles → skin/nail toxicity; FDA approved 2023
- **Sequencing:** With multiple classes available, optimal sequencing depends on prior exposures, toxicity, t(11;14) status, and performance status; BCMA CAR-T preferred early in eligible patients (manufacturing lead time ~4-6 weeks)

**Supportive care:**
- **VTE prophylaxis:** Lenalidomide/thalidomide + steroids → thrombogenic; aspirin or LMWH based on risk score (IMWG risk model)
- **Infection prophylaxis:** Anti-viral (acyclovir), anti-Pneumocystis (TMP-SMX or dapsone), anti-fungal for high-dose steroids; IVIG for IgG <4 g/dL with recurrent infections
- **Bone protection:** Denosumab (preferred) or zoledronic acid × 2 years; calcium/vitamin D supplementation
- **EPO agents:** For anemia not corrected by disease therapy; ESAs avoid transfusion dependency

## Connections

- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is the primary myeloma cell survival cytokine; BMSCs produce IL-6 in response to myeloma adhesion → JAK1/2-STAT3 → MCL-1 and BCL-XL → anti-apoptosis; serum IL-6 and CRP correlate with disease activity; tocilizumab has limited clinical activity in MM.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC is dysregulated in ~50-80% of relapsed MM via chr 8q24 amplification and MMSET-driven histone methylation; MYC drives plasma cell proliferation and immunoglobulin switch recombination; MYC transcription is sensitive to BET bromodomain inhibitors in MM models.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 is selectively overexpressed in t(11;14) MM (~15%); t(11;14) juxtaposes CCND1 near the IgH enhancer and correlates with BCL-2-high/BCL-XL-low expression; venetoclax achieves ORR ~40% in t(11;14) relapsed MM; CANOVA trial evaluated venetoclax + dexamethasone.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF is produced by myeloma cells and BMSCs → bone marrow angiogenesis → disease progression; VEGF promotes myeloma survival via VEGFR → PI3K-AKT; thalidomide and lenalidomide exert anti-angiogenic effects via VEGF suppression; bortezomib reduces VEGF secretion.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — MM cells secrete RANKL → osteoclast hyperactivation → osteolytic lesions and hypercalcemia; MM cells exploit OPG TRAIL-decoy function for survival; Xgeva (denosumab 120 mg Q4W) reduces skeletal-related events in MM bone disease.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — MM-secreted DKK1 and osteocyte sclerostin synergistically block osteoblast Wnt → uncoupled osteolysis; sclerostin inhibition in MM preclinical models restores osteoblast function and reduces lytic lesions; anti-DKK1 antibody (BHQ880) is in clinical trials for MM bone disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — MM plasma cells use CXCL12/CXCR4 for bone marrow homing and survival; plerixafor (AMD3100, CXCR4 antagonist) + G-CSF mobilizes HSC for ASCT in MM (AMBER trial: superior day-1 CD34+ yield); CXCR4 expression on MM cells associates with marrow retention and drug resistance.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Multiple myeloma is a malignancy of plasma cells — antibody-secreting terminal B cells — that clonally expand in the marrow and pour out a single monoclonal immunoglobulin (M-protein); their prolific secretory machinery makes them exquisitely sensitive to proteasome inhibitors.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Multiple myeloma lives in the bone marrow, where malignant plasma cells co-opt stromal cells for IL-6 and CXCL12 survival signals and tip the RANKL/OPG balance toward osteoclasts; marrow plasma cells ≥10% (or a biopsy-proven plasmacytoma) plus CRAB features define the diagnosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a major myeloma target: filtered monoclonal free light chains precipitate with Tamm-Horsfall protein into obstructing tubular casts (cast nephropathy), and with hypercalcemia cause the renal failure of CRAB — reversible if light-chain production is cut quickly.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Multiple myeloma and Waldenström macroglobulinemia are both monoclonal plasma-cell/B-cell dyscrasias secreting a paraprotein but differ: myeloma makes IgG/IgA with lytic bone disease and renal failure, WM makes IgM with hyperviscosity and the MYD88 L265P mutation.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Myeloma bone disease uncouples bone remodeling: tumor cells secrete DKK-1 and sclerostin that suppress osteoblasts and RANKL that activates osteoclasts, so the pure lytic lesions show no reactive new bone (cold on bone scan)—anti-RANKL agents aim to reset this.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Multiple myeloma is defined by a monoclonal immunoglobulin: the plasma-cell clone secretes a single intact IgG (or IgA) or free light chain—the M-protein seen as a serum spike—whose level tracks disease, while suppression of normal immunoglobulins causes myeloma's infection risk.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is central to myeloma's CRAB complications: tumor-driven RANKL activates osteoclasts that dissolve bone, releasing calcium into blood—hypercalcemia causes confusion, constipation and kidney injury, treated urgently with hydration and bisphosphonates.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Myeloma bone disease and osteoporosis both fracture vertebrae but differ: myeloma carves discrete lytic 'punched-out' lesions, while osteoporosis is diffuse low bone density—new vertebral fractures in an older adult warrant a myeloma work-up.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is a key palliative tool in myeloma: though systemic, the disease responds to localized radiation that relieves bone pain and treats impending fractures, and is curative for solitary plasmacytoma—complementing the drugs that control marrow disease.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Multiple myeloma is the malignant end of B-cell maturation: it arises when a B cell becomes a clonal plasma cell, evolving from MGUS through smoldering myeloma—a step beyond the B cell, secreting monoclonal immunoglobulin instead of fighting infection.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Myeloma hijacks osteoclasts to destroy bone: malignant plasma cells secrete RANKL and cytokines that overactivate osteoclasts while suppressing osteoblasts, carving the punched-out lytic lesions, hypercalcemia and fractures that define myeloma bone disease.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Multiple myeloma and DLBCL are B-lineage cancers at opposite maturation ends: DLBCL is an aggressive nodal large B-cell lymphoma, myeloma a marrow plasma-cell tumor secreting monoclonal protein—and rarely a plasmablastic lymphoma blurs the line between them.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Anemia is a defining feature of multiple myeloma: plasma cells crowd the marrow and their cytokines suppress red-cell production, so falling hemoglobin (one of the CRAB criteria) is a common presenting sign alongside bone pain and renal failure.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Multiple myeloma cripples the immune system: as it expands one plasma-cell clone, normal antibody production collapses (immunoparesis), so recurrent infection is a top cause of death—and CD38-targeting and T-cell therapies now turn immunity back against the tumor.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Multiple myeloma is the malignant end of the B-cell lineage of the lymphatic system: it arises from plasma cells—the antibody factories that B cells become—so it produces a monoclonal immunoglobulin (M-protein) while crowding out normal immunity.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Multiple myeloma is a frontier for engineered T cells: BCMA-directed CAR-T cells and T-cell-engaging bispecific antibodies redirect cytotoxic T cells to kill plasma cells, producing deep remissions in disease that has relapsed after every drug class.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Antibody therapy for myeloma works through NK cells: daratumumab against CD38 and elotuzumab tag plasma cells for natural-killer-cell killing (ADCC), making these antibodies a backbone of modern treatment.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Myeloma plasma cells depend on NF-kB for survival: the bone-marrow niche and genetic lesions keep this pathway switched on, and proteasome inhibitors like bortezomib work partly by blocking NF-kB activation—starving the cell of its survival signal.

[^kumar-2022-imwg-criteria]: Kumar SK, Callander NS, Adekola K, et al. Multiple myeloma, version 3.2021, NCCN clinical practice guidelines in oncology. *J Natl Compr Canc Netw.* 2020;18(12):1685-1717. [doi:10.6004/jnccn.2020.0057](https://doi.org/10.6004/jnccn.2020.0057) · [PubMed 33285519](https://pubmed.ncbi.nlm.nih.gov/33285519/)
[^moreau-2022-teclistamab]: Moreau P, Garfall AL, van de Donk NWCJ, et al. Teclistamab in relapsed or refractory multiple myeloma. *N Engl J Med.* 2022;387(6):495-505. [doi:10.1056/NEJMoa2203478](https://doi.org/10.1056/NEJMoa2203478) · [PubMed 35661166](https://pubmed.ncbi.nlm.nih.gov/35661166/)
[^martin-2023-carvykti]: San-Miguel J, Dhakal B, Yong K, et al. Cilta-cel or standard care in lenalidomide-refractory multiple myeloma. *N Engl J Med.* 2023;389(4):335-347. [doi:10.1056/NEJMoa2303379](https://doi.org/10.1056/NEJMoa2303379) · [PubMed 37285856](https://pubmed.ncbi.nlm.nih.gov/37285856/)
