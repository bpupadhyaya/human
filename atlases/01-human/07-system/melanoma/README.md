---
schema: human-scale-entry/v1
id: melanoma
name: Melanoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Skin cancer from melanocytes; BRAF V600E (50%) and NRAS Q61 (25%) are dominant drivers. Dual checkpoint blockade (nivolumab + ipilimumab) and BRAF+MEK inhibitors (dabrafenib+trametinib) each achieve ~50-60% responses; 5-year OS ~50% in the immunotherapy era."
aliases: ["cutaneous melanoma", "malignant melanoma", "uveal melanoma", "acral melanoma", "mucosal melanoma", "BRAF-mutant melanoma", "metastatic melanoma"]
sources:
  - id: larkin-2015-checkmate067
    type: peer-reviewed
    cite: "Larkin J, Chiarion-Sileni V, Gonzalez R, et al. Combined nivolumab and ipilimumab or monotherapy in untreated melanoma. N Engl J Med. 2015;373(1):23-34."
    doi: "10.1056/NEJMoa1504030"
    pmid: "26027431"
    url: "https://doi.org/10.1056/NEJMoa1504030"
  - id: robert-2015-combi-v
    type: peer-reviewed
    cite: "Robert C, Karaszewska B, Schachter J, et al. Improved overall survival in melanoma with combined dabrafenib and trametinib. N Engl J Med. 2015;372(1):30-39."
    doi: "10.1056/NEJMoa1412690"
    pmid: "25399551"
    url: "https://doi.org/10.1056/NEJMoa1412390"
  - id: wolchok-2022-checkmate067-7yr
    type: peer-reviewed
    cite: "Wolchok JD, Chiarion-Sileni V, Gonzalez R, et al. Long-term outcomes with nivolumab plus ipilimumab or nivolumab alone versus ipilimumab in patients with advanced melanoma. J Clin Oncol. 2022;40(2):127-137."
    doi: "10.1200/JCO.21.02229"
    pmid: "34958258"
    url: "https://doi.org/10.1200/JCO.21.02229"
cross_links:
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E occurs in ~50% of melanoma; vemurafenib + cobimetinib and dabrafenib + trametinib achieve ~68-70% ORR in BRAF V600E metastatic melanoma; COMBI-D 5-year OS 34%; acquired resistance via NRAS/MEK mutations; combination prevents paradoxical ERK reactivation."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 blockade transformed advanced melanoma: pembrolizumab and nivolumab achieve 40-45% ORR; 5-year OS 44% with nivolumab monotherapy (CheckMate-003); immunotherapy is preferred over BRAF+MEK for asymptomatic disease due to durable responses and long-term survival plateau."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Ipilimumab was the first checkpoint inhibitor approved for advanced melanoma (2011); nivolumab + ipilimumab (CheckMate-067): 7-year OS 49% vs. 44% nivolumab vs. 21% ipilimumab — dual blockade delivers most durable benefit despite highest toxicity (~55% grade 3-4 irAEs)."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss occurs in ~20-30% of melanoma; PTEN loss → constitutive AKT → BRAF inhibitor resistance (alternative survival pathway); PTEN-null melanomas are relatively resistant to vemurafenib; combined BRAF + AKT inhibition is proposed for PTEN-null/BRAF V600E melanoma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Tumor microenvironment generates adenosine via CD39 (ATP→AMP) and CD73 (AMP→adenosine); A2AR on tumor-infiltrating T cells → ↑cAMP → ↓IL-2/IFN-γ → immune evasion; anti-CD73 (oleclumab) + anti-PD-1 combination trials target adenosine-mediated immune checkpoint resistance."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Melanoma evades perforin-mediated CTL/NK cytotoxicity via MHC-I downregulation, PD-L1 upregulation, and IDO-mediated T-cell suppression; checkpoint inhibitors (anti-PD-1/CTLA-4) restore perforin-granzyme killing; TIL perforin content predicts immunotherapy response."
---

# Melanoma

## Overview

**Melanoma** is a malignant tumor arising from **melanocytes** — neural crest-derived cells that produce melanin pigment in the skin, uveal tract, mucous membranes, and meninges. While accounting for only ~5% of skin cancers, melanoma is responsible for ~75% of skin cancer deaths due to its high metastatic potential and historically poor prognosis in advanced stages. However, the discovery of **BRAF V600E** as a targetable oncogene (2002) and the development of **immune checkpoint inhibitors** (2011-present) have transformed metastatic melanoma from a disease with median OS of ~8 months to one where ~50% of patients are alive at 5 years with modern therapy [^larkin-2015-checkmate067].

**Melanoma subtypes (anatomical):**
- **Cutaneous melanoma (~90%):** Arising from skin melanocytes; further subdivided:
  - **Superficial spreading melanoma (SSM, ~70%):** Most common; horizontal growth phase → vertical (invasive); most strongly associated with UV exposure; BRAF V600E frequent
  - **Nodular melanoma (~15%):** Aggressive; no radial growth phase → rapid vertical invasion; often amelanotic (no pigment) → delayed diagnosis
  - **Lentigo maligna melanoma (LMM, ~10%):** In sun-damaged skin (head/neck, elderly); BRAF mutations less common; NF1 and triple wild-type more frequent
  - **Acral lentiginous melanoma (ALM, ~5%):** Palms, soles, nail beds; under-diagnosed in dark skin; no UV association; KIT mutations in ~30%; different treatment implications
- **Uveal (ocular) melanoma (~5%):** GNAQ/GNA11 mutations (in >90%) — not BRAF; BAP1 loss → high metastatic potential; hepatic metastasis predominant; different biology and treatment (KIT pathway unimportant; tebentafusp — bispecific targeting gp100 — FDA approved 2022)
- **Mucosal melanoma (~1%):** Anorectal, vulvovaginal, sinonasal; poor prognosis; KIT mutations (~25%); distinct from cutaneous; imatinib/sunitinib occasionally active in KIT-mutant mucosal melanoma
- **Meningeal (rare):** CNS-primary; associated with congenital melanocytic nevi and NRAS mutations

**Molecular genetic landscape of cutaneous melanoma:**
- **BRAF V600E/K (~50%):** Dominant oncogenic driver; V600E (~90% of BRAF mutations); constitutive BRAF kinase → MEK-ERK → proliferation; mutually exclusive with NRAS (but can co-occur with NF1 loss); targetable with BRAF inhibitors
- **NRAS Q61R/K/L (~25%):** RAS GTPase lock in GTP-bound → RAF-MEK-ERK; harder to target than BRAF; binimetinib (MEK inhibitor) modestly active; no direct NRAS inhibitors approved; NRAS-mutant melanoma has higher Ki-67, worse prognosis
- **NF1 loss (~15%):** NF1 = RAS-GAP; loss → RAS hyperactivation → MEK-ERK; MEK inhibitors (cobimetinib, binimetinib) have activity; "NF1 subtype" enriched in older patients, heavy UV damage
- **Triple wild-type (~10%):** Wild-type for BRAF, NRAS, NF1; KIT mutations, CDK4 amplification, CCND1 amplification; more heterogeneous; uncommon in superficial spreading; acral/mucosal subtypes overrepresented
- **Tumor mutational burden (TMB):** Cutaneous melanoma has among the highest TMB of all cancers (~17 mut/Mb median, up to 100+ in chronic sun-damaged melanoma) due to UV-induced C>T and CC>TT transitions — **UV mutational signature** (COSMIC SBS7a/7b); high TMB correlates with neoantigens → immunogenicity → checkpoint inhibitor response

## Structure

### UV carcinogenesis and melanocyte biology

**UV-induced melanocyte transformation:**
- UV-B (290-315 nm) → cyclobutane pyrimidine dimers (CPDs) and 6-4 photoproducts in melanocyte DNA → if misrepaired → C>T transitions at dipyrimidine sequences; CC>TT doublet mutations are UV-signature hallmarks; UV directly activates the BRAF pathway (short-term) and mutates BRAF, NRAS, TP53 (long-term carcinogenesis)
- **Melanocyte-specific biology:** Melanocytes express MC1R (melanocortin 1 receptor) → activated by alpha-MSH → cAMP → CREB → MITF (microphthalmia-associated transcription factor) → tyrosinase, DCT, TYRP1 → melanin synthesis; MITF is the "master regulator" of melanocyte identity; in melanoma, MITF switches from a differentiation factor to a proliferation/survival factor depending on expression level
- **Melanoma invasion:** Melanocytes are normally anchored by E-cadherin to keratinocytes; in melanoma, E-cadherin → N-cadherin switch → loss of keratinocyte anchor → invasion through dermis; MMP (matrix metalloproteinase) production → basement membrane degradation; VEGF → neoangiogenesis → hematogenous dissemination

**BRAF-MEK-ERK pathway in melanoma:**
- Normal melanocyte: UV → receptor activation → transient ERK activation → cell cycle entry → melanin synthesis
- BRAF V600E melanoma: Constitutive BRAF kinase activity (independent of RAS) → constitutive MEK-ERK → cyclin D1, MYC → proliferation; ERK → transcriptional activation of MITF → complex between proliferative and differentiating signals; BRAF V600E drives both proliferative advantage and some aspects of melanocyte identity (pigmentation) → melanoma retains some melanocytic gene expression

**Immune microenvironment:**
- Cutaneous melanoma has the highest TIL (tumor-infiltrating lymphocyte) density of most solid tumors; TILs — CD8+ T cells predominating — are recruited by CXCL9/10 (IFN-gamma-driven); PD-L1 expression on melanoma cells and macrophages → T cell exhaustion; checkpoint inhibitor response directly correlates with: TIL density, IFN-gamma signature, PD-L1 expression, and TMB
- **BRAF V600E → immune exclusion:** Vemurafenib-treated tumors show increased T cell infiltration within weeks (BRAF inhibition → MEK-ERK suppression → decreased immunosuppressive VEGF and IL-10 production → increased T cell access); this is why BRAF+MEK → immunotherapy sequencing or combinations are being explored

## Function

### Clinical presentation, staging, and surveillance

**ABCDE criteria (early detection):**
- **A**symmetry, **B**order irregularity, **C**olor variation (multiple hues), **D**iameter >6 mm, **E**volution (change over time); melanoma often presents as a new or changing pigmented lesion; clinician examination + dermoscopy → biopsy threshold

**Staging (AJCC 8th edition):**
- **Stage I-II:** Primary melanoma with/without ulceration and mitotic rate; 5-year OS >90% (Stage I) to 60-70% (Stage IIc)
- **Stage III:** Regional lymph node metastasis; subdivided by nodal burden (IIIA/B/C/D); 5-year OS 40-78%
- **Stage IV:** Distant metastasis; M1a (skin/subcutaneous/lymph node), M1b (lung), M1c (visceral), M1d (brain); 5-year OS 15-30% with modern therapy

**Sentinel lymph node biopsy (SLNB):**
- Recommended for melanomas ≥0.8 mm Breslow thickness (or 0.6-0.8 mm with ulceration); provides staging information (SLN positive → Stage III); completion lymph node dissection (CLND) no longer standard (DeCOG, MSLT-II trials); adjuvant therapy guided by SLN status

## Pathology

### Diagnosis

**Excisional biopsy** (preferred, 1-2 mm margins) with histopathology: Breslow thickness (depth in mm, most important prognostic factor), Clark level (anatomical level), ulceration, mitotic rate, satellitosis, lymphovascular invasion — all reported in standardized format.

**BRAF mutation testing:** Required before initiating targeted therapy; BRAF V600E/K testing by RT-PCR (cobas, THxID) or next-generation sequencing; extended BRAF/NRAS/NF1/KIT molecular profiling on metastatic disease for treatment planning.

### Treatment [^larkin-2015-checkmate067] [^robert-2015-combi-v]

**Early-stage (adjuvant therapy after resection of Stage III-IIA disease):**
- **Pembrolizumab adjuvant (KEYNOTE-716):** 18 months; reduces recurrence in Stage IIb-IIc (high-risk) and Stage III; 2-year RFS 83.4% vs. 77.1%
- **Nivolumab adjuvant (CheckMate-238):** vs. ipilimumab in Stage IIIB-IV; 5-year RFS 50% vs. 39%; OS benefit at 5 years
- **Dabrafenib + trametinib adjuvant (COMBI-AD):** For BRAF V600E/K Stage III; 5-year RFS 52% vs. 36% placebo; OS not significantly different from checkpoint inhibitor adjuvant in cross-trial comparison (no head-to-head data)

**Metastatic melanoma — immune checkpoint blockade:**
- **Nivolumab + ipilimumab (CheckMate-067):** 7-year OS 49% vs. 44% (nivo alone) vs. 21% (ipi alone); dual blockade achieves the deepest and most durable responses; recommended for symptomatic/rapid-progression/high-volume disease [^wolchok-2022-checkmate067-7yr]; grade 3-4 irAEs ~55% (discontinuation rate high)
- **Pembrolizumab monotherapy (KEYNOTE-006):** OS 38.7% at 5 years; 5-year PFS 21%; landmark data establishing checkpoint immunotherapy as a dominant first-line strategy
- **Relatlimab + nivolumab (Opdualag — anti-LAG-3 + anti-PD-1):** RELATIVITY-047: PFS 10.1 vs. 4.6 months vs. nivolumab; FDA approved 2022; less toxicity than nivo + ipi; LAG-3 is the third checkpoint after PD-1 and CTLA-4

**Metastatic melanoma — BRAF-targeted therapy:**
- **Dabrafenib + trametinib (COMBI-D/V):** ORR ~68%; median PFS ~12-15 months; 5-year OS 34% (COMBI-D); superior to BRAF inhibitor monotherapy; approved for BRAF V600E/K metastatic melanoma; preferred in rapidly progressive, high-burden, or LDH-elevated disease where rapid response needed [^robert-2015-combi-v]
- **Encorafenib + binimetinib (COLUMBUS):** PFS 14.9 months; OS 33.6 months; lower pyrexia than dabrafenib/trametinib; approved for BRAF V600E/K metastatic melanoma
- **Vemurafenib + cobimetinib (coBRIM):** PFS 12.3 months; first approved BRAF+MEK combination

**Resistance to BRAF+MEK inhibitors:**
- Acquired resistance after median 12-15 months; mechanisms: NRAS mutation (10-20%), MEK1/2 mutations (5-10%), BRAF V600E amplification (5-10%), BRAF splice variants, NF1 loss, PI3K activation (PTEN loss), MAP3K/COT1 → ERK reactivation; immunotherapy after BRAF+MEK failure (cross-resistance uncommon)

**Brain metastases:**
- ~40-50% of metastatic melanoma develop brain metastases; ipilimumab + nivolumab (CheckMate-204: intracranial ORR 57%); dabrafenib + trametinib (intracranial ORR 58% in BRAF V600E); SRS (stereotactic radiosurgery) for ≤4 lesions; whole-brain RT generally avoided (neurotoxicity); targeted + IO combinations under investigation for leptomeningeal disease

**Uveal melanoma:**
- **Tebentafusp (Kimmtrak):** First approved therapy for uveal melanoma (2022); bispecific T cell engager (TCE) targeting gp100 (melanocytic antigen) × CD3; requires HLA-A*02:01 (40% of patients); IMCgp100-202 trial: OS 73% vs. 59% at 1 year vs. investigator choice — first survival benefit in uveal melanoma; cytokine release syndrome manageable

## Connections

- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E occurs in ~50% of melanoma; vemurafenib + cobimetinib and dabrafenib + trametinib achieve ~68-70% ORR; COMBI-D 5-year OS 34%; acquired resistance via NRAS/MEK mutations; combination prevents paradoxical ERK reactivation from single-agent BRAF inhibition.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 blockade transformed advanced melanoma: pembrolizumab and nivolumab achieve 40-45% ORR; 5-year OS 44% with nivolumab; immunotherapy preferred for asymptomatic disease due to durable responses and long-term survival plateau not seen with BRAF+MEK.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Ipilimumab was the first checkpoint inhibitor approved in advanced melanoma (2011); nivolumab + ipilimumab (CheckMate-067): 7-year OS 49% vs. 21% ipilimumab — dual blockade delivers the most durable benefit despite highest toxicity (~55% grade 3-4 irAEs).
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss occurs in ~20-30% of melanoma → constitutive AKT → BRAF inhibitor resistance; PTEN-null melanomas are relatively resistant to vemurafenib; combined BRAF + AKT inhibition is proposed and under investigation for PTEN-null/BRAF V600E melanoma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — tumor microenvironment generates adenosine via CD39 (ATP→AMP) and CD73 (AMP→adenosine) on melanoma cells and MDSCs; A2AR on tumor-infiltrating T cells → ↑cAMP → ↓IL-2/IFN-γ → immune evasion; anti-CD73 (oleclumab) + anti-PD-1 combination trials target adenosine-mediated immune checkpoint resistance.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Melanoma evades perforin-mediated CTL/NK cytotoxicity via MHC-I downregulation, PD-L1 upregulation, and IDO-mediated T-cell suppression; checkpoint inhibitors (anti-PD-1/CTLA-4) restore perforin-granzyme killing; TIL perforin content predicts immunotherapy response.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^larkin-2015-checkmate067]: Larkin J, Chiarion-Sileni V, Gonzalez R, et al. Combined nivolumab and ipilimumab or monotherapy in untreated melanoma. *N Engl J Med.* 2015;373(1):23-34. [doi:10.1056/NEJMoa1504030](https://doi.org/10.1056/NEJMoa1504030) · [PubMed 26027431](https://pubmed.ncbi.nlm.nih.gov/26027431/)
[^robert-2015-combi-v]: Robert C, Karaszewska B, Schachter J, et al. Improved overall survival in melanoma with combined dabrafenib and trametinib. *N Engl J Med.* 2015;372(1):30-39. [doi:10.1056/NEJMoa1412690](https://doi.org/10.1056/NEJMoa1412690) · [PubMed 25399551](https://pubmed.ncbi.nlm.nih.gov/25399551/)
[^wolchok-2022-checkmate067-7yr]: Wolchok JD, Chiarion-Sileni V, Gonzalez R, et al. Long-term outcomes with nivolumab plus ipilimumab or nivolumab alone versus ipilimumab in patients with advanced melanoma. *J Clin Oncol.* 2022;40(2):127-137. [doi:10.1200/JCO.21.02229](https://doi.org/10.1200/JCO.21.02229) · [PubMed 34958258](https://pubmed.ncbi.nlm.nih.gov/34958258/)
