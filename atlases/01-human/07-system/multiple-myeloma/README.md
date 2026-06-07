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

[^kumar-2022-imwg-criteria]: Kumar SK, Callander NS, Adekola K, et al. Multiple myeloma, version 3.2021, NCCN clinical practice guidelines in oncology. *J Natl Compr Canc Netw.* 2020;18(12):1685-1717. [doi:10.6004/jnccn.2020.0057](https://doi.org/10.6004/jnccn.2020.0057) · [PubMed 33285519](https://pubmed.ncbi.nlm.nih.gov/33285519/)
[^moreau-2022-teclistamab]: Moreau P, Garfall AL, van de Donk NWCJ, et al. Teclistamab in relapsed or refractory multiple myeloma. *N Engl J Med.* 2022;387(6):495-505. [doi:10.1056/NEJMoa2203478](https://doi.org/10.1056/NEJMoa2203478) · [PubMed 35661166](https://pubmed.ncbi.nlm.nih.gov/35661166/)
[^martin-2023-carvykti]: San-Miguel J, Dhakal B, Yong K, et al. Cilta-cel or standard care in lenalidomide-refractory multiple myeloma. *N Engl J Med.* 2023;389(4):335-347. [doi:10.1056/NEJMoa2303379](https://doi.org/10.1056/NEJMoa2303379) · [PubMed 37285856](https://pubmed.ncbi.nlm.nih.gov/37285856/)
