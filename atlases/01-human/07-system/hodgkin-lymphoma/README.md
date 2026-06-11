---
schema: human-scale-entry/v1
id: hodgkin-lymphoma
name: Hodgkin Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Hodgkin lymphoma is a GC B cell-derived malignancy; RS cells ~100% CD30+; 9p24.1 amplification drives CD30+PD-L1/L2 co-expression; A+AVD (ECHELON-1) is standard for advanced stage; nivolumab/pembrolizumab for R/R; 5-year OS >85% overall; NLPHL has distinct CD20+ biology."
aliases: ["Hodgkin lymphoma", "HL", "cHL", "classical Hodgkin lymphoma", "NLPHL", "Reed-Sternberg", "Hodgkin disease", "nodular sclerosis HL", "mixed cellularity HL"]
sources:
  - id: connors-2018-echelon1
    type: peer-reviewed
    cite: "Connors JM, Jurczak W, Straus DJ, et al. Brentuximab vedotin with chemotherapy for stage III or IV Hodgkin's lymphoma. N Engl J Med. 2018;378(4):331-344."
    doi: "10.1056/NEJMoa1708984"
    pmid: "29360494"
    url: "https://doi.org/10.1056/NEJMoa1708984"
  - id: armand-2018-nivo-hl
    type: peer-reviewed
    cite: "Armand P, Engert A, Younes A, et al. Nivolumab for relapsed/refractory classic Hodgkin lymphoma after failure of autologous hematopoietic cell transplantation: extended follow-up of the multicohort single-arm phase II CheckMate 205 trial. J Clin Oncol. 2018;36(14):1428-1439."
    doi: "10.1200/JCO.2017.77.6717"
    pmid: "29584546"
    url: "https://doi.org/10.1200/JCO.2017.77.6717"
cross_links:
  - target: 01-human/03-molecular/cd30
    relation: connects-to
    note: "CD30 is expressed on ~100% of RS cells (WHO diagnostic criterion for cHL); brentuximab vedotin is the backbone of A+AVD (ECHELON-1) and consolidation post-auto-SCT (AETHERA); 9p24.1 amplification co-amplifies CD30 with PD-L1/PD-L2 in RS cells."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "9p24.1 amplification in RS cells drives PD-L1/PD-L2 overexpression → profound T-cell exhaustion in tumor microenvironment; nivolumab (CheckMate 205) and pembrolizumab (KEYNOTE-087) show ORR ~65-70% in R/R cHL; KEYNOTE-204 (pembrolizumab vs BV): PFS 13.2 vs 8.3 months."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is constitutively active in RS cells via CD30, CD40, EBV-LMP1, and CARD11 signaling; NF-κB drives RS cell survival by upregulating BCL-2, BCL-XL, and cFLIP; microenvironmental TNF-α further activates NF-κB; NF-κB inhibition is a preclinical therapeutic target in R/R cHL."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "9p24.1 amplification co-amplifies JAK2 with PD-L1/PD-L2 and CD30 in RS cells; JAK2 → constitutive STAT6 → IL-13 autocrine + PD-L1 transcription; ruxolitinib studied in R/R cHL; JAK2 amplification is a primary oncogenic driver in cHL."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Reed-Sternberg cells arise from germinal-center B cells that acquired crippling Ig V-gene mutations and should have died during negative selection; they survive via CD30/CD40/NF-κB and EBV rescue while shedding the B-cell program (no surface Ig, loss of OCT2/BOB1)."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV is found in 30-50% of classical HL (up to 80-90% in lymphocyte-depleted and HIV-associated cases); its LMP1 protein mimics a constitutively active CD40 receptor → NF-κB survival signaling in RS cells; prior infectious mononucleosis roughly triples HL risk."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 status splits Hodgkin lymphoma: RS cells of classical HL are CD20-negative, whereas the popcorn (L&H) cells of NLPHL retain the B-cell program and are CD20-positive — making rituximab effective in NLPHL but not classical HL."
---

# Hodgkin Lymphoma

## Overview

**Hodgkin lymphoma (HL)** is a B-cell-derived malignancy defined by the presence of neoplastic **Reed-Sternberg (RS) cells** (binucleated giant cells with prominent "owl eye" nucleoli) within an inflammatory tumor microenvironment. HL is one of oncology's major treatment success stories: overall 5-year OS exceeds **85-90%** with modern therapy, including cures in the majority of patients with advanced-stage disease. RS cells represent only ~0.1-1% of the tumor mass and are derived from **germinal center (GC) B cells** that have undergone incomplete apoptosis during negative selection — they carry somatic hypermutated Ig V genes but have catastrophically lost the B-cell transcription program (no surface Ig, absent BOB1/OCT2/PU.1). The landmark identification of **9p24.1 chromosomal amplification** in RS cells — co-amplifying CD30, PDL1, PDL2, and JAK2 — explained the extraordinary sensitivity of HL to PD-1 checkpoint inhibitors and the tumor's immune evasion strategy [^armand-2018-nivo-hl]. **Brentuximab vedotin (anti-CD30 ADC) + AVD** replaced ABVD as the standard for advanced stage cHL after ECHELON-1 demonstrated superior OS [^connors-2018-echelon1].

**Epidemiology:**
- Incidence: ~8,500 cases/year USA; ~83,000 globally
- Bimodal age distribution: peak 1 at 15-34 years (NSHL predominant); peak 2 at >55 years (MCHL and LDHL)
- Male slight predominance; EBV+ forms more common in low-resource settings and older/young children
- Risk factors: infectious mononucleosis (EBV) — 3-fold elevated risk; HIV; immunosuppression; family history

## Structure

### Classification

**Classical Hodgkin lymphoma (cHL, ~95%):**
RS cells: CD15+, CD30+, PAX5 dim, CD20−, OCT2−, BOB1−, CD45−; EBV in 30-50% (depends on subtype and geography)

Histological subtypes:
- **Nodular sclerosis (NSHL, ~60-65%):** Young adults; mediastinal mass common (~75%); broad collagen bands ("lacunar cells" — RS cell variant); EBV+ ~10-25%; most common in high-income countries; favorable prognosis
- **Mixed cellularity (MCHL, ~25%):** Older adults and young children; EBV+ ~50-70%; no fibrosis; rich inflammatory infiltrate; often stage III-IV at presentation
- **Lymphocyte-rich (LRHL, ~5%):** Rare; similar to NLPHL but CD30+; excellent prognosis; difficult to distinguish from NLPHL without IHC
- **Lymphocyte-depleted (LDHL, ~1%):** Elderly; advanced stage; HIV-associated; EBV+ ~80-90%; worst prognosis of cHL subtypes

**Nodular lymphocyte predominant HL (NLPHL, ~5%):**
Neoplastic "lymphocytic and histiocytic" (L&H) cells, also called "popcorn cells":
- CD20+, CD19+, CD79a+, BCL6+, OCT2+, BOB1+ — maintains B-cell program (unlike RS cells)
- CD30−, CD15−, EBV−
- Distinctly different from cHL: GC B cell origin with intact B-cell transcription; NF-κB via BCR signaling
- Treatment: rituximab (anti-CD20) effective alone or with CHOP; excellent prognosis; late relapses possible; may transform to DLBCL
- Sometimes reclassified as T-cell/histiocyte-rich large B-cell lymphoma (THRLBCL) after transformation

### Reed-Sternberg cell molecular biology

**Origin:**
RS cells originate from GC B cells that failed negative selection: they carry clonal rearranged Ig V genes with somatic hypermutations but often have "crippling" mutations in the Ig V gene that abolish BCR expression — these cells would normally die in the GC by apoptosis; RS cells escape via rescue mechanisms involving CD30, NF-κB, and possibly EBV.

**9p24.1 amplification (~97% cHL):**
Chromosome 9p24.1 harbors JAK2, PD-L1 (CD274), PD-L2 (PDCD1LG2), and CD30 (TNFRSF8) within a shared amplicon; amplification (and polysomy) increases: (1) JAK2 expression → constitutive JAK2-STAT6 → IL-13 auto-stimulation + PD-L1 transcription; (2) PD-L1/PD-L2 surface expression → T-cell exhaustion in tumor microenvironment; (3) CD30 overexpression → TRAF/NF-κB survival signals; this convergent amplification explains the >60-70% ORR to PD-1 inhibitors.

**Other molecular features:**
- SOCS1 mutations/deletions (~40%): loss of JAK-STAT negative regulator → enhanced IL-13 signaling
- TNFRSF14 (HVEM) mutations (~15%): impairs CD8+ T-cell activation in microenvironment
- CARD11 mutations (~5%): constitutive NF-κB activation
- A20 (TNFAIP3) deletions (~30%): NF-κB negative regulator loss
- EBV LMP1: functional CD40 mimic → TRAF2/TRAF3/TRAF6 → NF-κB; also induces PD-L1; expressed in ~40-50% cHL RS cells

**Microenvironment composition:**
RS cells recruit and program an inflammatory microenvironment via secreted chemokines and cytokines:
- CCL17/TARC, CCL22: recruit regulatory T cells (Treg) and Th2 cells → immune suppression
- IL-5, eotaxin: recruit eosinophils (prominent in NSHL and MCHL)
- IL-13: auto-stimulatory for RS cells; also drives fibrosis (NSHL collagen bands)
- PGE2: suppresses NK and CD8+ T cells
- CD47 ("don't eat me"): expressed on RS cells → blocks macrophage phagocytosis

## Function

### Staging

**Ann Arbor / Lugano staging (PET-CT based):**
- Stage I: Single lymph node region or single extralymphatic site
- Stage II: ≥2 lymph node regions, same side of diaphragm (± contiguous extranodal site)
- Stage III: Lymph node regions or structures on both sides of diaphragm
- Stage IV: Disseminated extranodal involvement (liver, bone marrow, lungs)

**Modifiers:**
- B symptoms: fever >38°C, drenching night sweats, >10% body weight loss in 6 months (adverse; B-symptom stage is worse prognosis)
- Bulky disease: mediastinal mass >1/3 of thoracic diameter OR any mass >10 cm

**IPS (International Prognostic Score) for advanced stage:**
7 adverse factors (1 point each): albumin <4 g/dL, Hgb <10.5 g/dL, male sex, stage IV, age ≥45, WBC ≥15,000/μL, lymphocyte count <600/μL or <8% of WBC
Score 0-1: 5-year FFS ~77%; Score ≥5: ~42% (though A+AVD has improved outcomes across all IPS groups)

## Pathology

### Treatment approach

**Early-stage favorable cHL (Stage I-II, no bulky disease, no B symptoms):**
- ABVD × 2 cycles + ISRT (involved-site radiotherapy, 20 Gy): ~95% 5-year PFS; standard
- Or ABVD × 4 cycles without RT (for patients refusing RT; slightly inferior PFS but equivalent OS)
- PET-adapted: interim PET-2 (after 2 ABVD) negative → complete ABVD without RT; positive → escalate to BEACOPP

**Early-stage unfavorable cHL (Stage I-II with bulk/B symptoms/other risk factors):**
- ABVD × 4 cycles + ISRT 30 Gy
- Or 2 cycles eBEACOPP + 2 cycles ABVD + RT (HD14 trial)
- A+AVD being studied in early-stage unfavorable (ECHELON-1 enrolled advanced stage only)

**Advanced-stage cHL (Stage III-IV):**
- **A+AVD (brentuximab vedotin + doxorubicin, vinblastine, dacarbazine) × 6 cycles:** Standard of care [^connors-2018-echelon1]; G-CSF primary prophylaxis required (higher neutropenia vs ABVD)
- Or eBEACOPP (escalated bleomycin, etoposide, doxorubicin, cyclophosphamide, vincristine, procarbazine, prednisone): higher toxicity; used in some European centers; higher 2-year PFS than ABVD but OS equivalent; may be preferred in IPS 4-7 patients
- PET-adapted de-escalation: interim PET-2 negative → switch to ABVD for cycles 3-6 (RATHL trial)

**Relapsed/Refractory cHL:**
- **Salvage chemotherapy:** DHAP, ICE, GVD, IGEV → aiming for CR → proceed to auto-SCT
- **Auto-SCT** (autologous stem cell transplant): standard for chemosensitive R/R cHL; 50-55% 5-year OS in auto-SCT-eligible patients
- **Brentuximab vedotin consolidation post-auto-SCT (AETHERA):** 5-year PFS 59% vs 41%; standard post-auto-SCT for high-risk patients
- **Nivolumab (CheckMate 205):** ORR ~69% in auto-SCT-relapsed/refractory cHL; CR ~16%; duration of response ~17 months; FDA 2016 [^armand-2018-nivo-hl]
- **Pembrolizumab (KEYNOTE-087):** ORR ~69% in R/R cHL; FDA 2017
- **KEYNOTE-204** (pembrolizumab vs brentuximab vedotin in R/R cHL): PFS 13.2 vs 8.3 months (HR 0.65) → pembrolizumab superior to brentuximab monotherapy in R/R; brentuximab now used more in combination or post-PD-1
- **Allo-SCT:** Chemorefractory disease; higher NRM than auto-SCT; DLI for molecular relapse
- **Camidanlumab tesirine (ADCT-301):** CD25 ADC (PBD dimer); ORR ~70% in R/R cHL; under investigation

**NLPHL treatment:**
- Stage IA: Involved site RT alone (excellent prognosis); observation considered in some
- Stage II-IV: R-CHOP or R-CVP; rituximab monotherapy for relapse; watch-and-wait for asymptomatic advanced stage
- Late relapses (10-20 years) common; requires long-term surveillance

### Long-term effects and survivorship

Hodgkin lymphoma survivors (~150,000 in USA) face significant late treatment toxicity:
- **Secondary malignancies:** Breast cancer (RT to mediastinum), lung cancer (bleomycin+RT+smoking), secondary AML/MDS (alkylating agents, etoposide — BEACOPP > ABVD risk), NHL
- **Cardiovascular:** Coronary artery disease and cardiomyopathy from mediastinal RT and anthracyclines; major cause of late mortality
- **Pulmonary:** Bleomycin-induced pulmonary fibrosis (~5-10% clinically significant; dose-dependent); pneumonitis from RT
- **Hypothyroidism:** From neck/mediastinal RT (~50% at 20 years)
- **Infertility:** Procarbazine-containing regimens (BEACOPP) → gonadal toxicity; ABVD and A+AVD have lower infertility risk; fertility preservation counseling before therapy

Modern protocols minimize RT fields and doses (ISRT replacing extended-field RT), reduce bleomycin exposure (A+AVD eliminates bleomycin), and use PET-adapted de-escalation to decrease cumulative toxicity.

## Connections

- `connects-to` → **[CD30](../../03-molecular/cd30/README.md)** — CD30 is expressed on ~100% of RS cells (WHO diagnostic criterion for cHL); brentuximab vedotin is the backbone of A+AVD (ECHELON-1) and consolidation post-auto-SCT (AETHERA); 9p24.1 amplification co-amplifies CD30 with PD-L1/PD-L2 in RS cells.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — 9p24.1 amplification in RS cells drives PD-L1/PD-L2 overexpression → profound T-cell exhaustion in tumor microenvironment; nivolumab (CheckMate 205) and pembrolizumab (KEYNOTE-087) show ORR ~65-70% in R/R cHL; KEYNOTE-204 (pembrolizumab vs BV): PFS 13.2 vs 8.3 months.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is constitutively active in RS cells via CD30, CD40, EBV-LMP1, and CARD11 signaling; NF-κB drives RS cell survival by upregulating BCL-2, BCL-XL, and cFLIP; microenvironmental TNF-α further activates NF-κB; NF-κB inhibition is a preclinical therapeutic target in R/R cHL.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — 9p24.1 amplification co-amplifies JAK2 with PD-L1/PD-L2 and CD30 in RS cells; JAK2 → constitutive STAT6 → IL-13 autocrine + PD-L1 transcription; ruxolitinib studied in R/R cHL; JAK2 amplification is a primary oncogenic driver in cHL.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Reed-Sternberg cells arise from germinal-center B cells that acquired crippling Ig V-gene mutations and should have died during negative selection; they survive via CD30/CD40/NF-κB and EBV rescue while shedding the B-cell program (no surface Ig, loss of OCT2/BOB1).
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — EBV is found in 30-50% of classical HL (up to 80-90% in lymphocyte-depleted and HIV-associated cases); its LMP1 protein mimics a constitutively active CD40 receptor → NF-κB survival signaling in RS cells; prior infectious mononucleosis roughly triples HL risk.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 status splits Hodgkin lymphoma: RS cells of classical HL are CD20-negative, whereas the popcorn (L&H) cells of NLPHL retain the B-cell program and are CD20-positive — making rituximab effective in NLPHL but not classical HL.

[^connors-2018-echelon1]: Connors JM, Jurczak W, Straus DJ, et al. Brentuximab vedotin with chemotherapy for stage III or IV Hodgkin's lymphoma. *N Engl J Med.* 2018;378(4):331-344. [doi:10.1056/NEJMoa1708984](https://doi.org/10.1056/NEJMoa1708984) · [PubMed 29360494](https://pubmed.ncbi.nlm.nih.gov/29360494/)
[^armand-2018-nivo-hl]: Armand P, Engert A, Younes A, et al. Nivolumab for relapsed/refractory classic Hodgkin lymphoma after failure of autologous hematopoietic cell transplantation: extended follow-up of the multicohort single-arm phase II CheckMate 205 trial. *J Clin Oncol.* 2018;36(14):1428-1439. [doi:10.1200/JCO.2017.77.6717](https://doi.org/10.1200/JCO.2017.77.6717) · [PubMed 29584546](https://pubmed.ncbi.nlm.nih.gov/29584546/)
