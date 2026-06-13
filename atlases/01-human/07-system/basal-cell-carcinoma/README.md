---
schema: human-scale-entry/v1
id: basal-cell-carcinoma
name: Basal Cell Carcinoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common human malignancy (~4 million/year in US); arises from basal keratinocytes driven by UV damage and PTCH1 loss. SMO mutations in ~40% of sporadic BCC activate Hedgehog-GLI → cyclin D1 and MYC; vismodegib and sonidegib are approved SMO inhibitors for advanced BCC."
aliases: ["BCC", "basal cell carcinoma", "basal cell nevus syndrome", "Gorlin syndrome", "rodent ulcer", "basal cell cancer", "BCNevus"]
sources:
  - id: sekulic-2012-vismodegib
    type: peer-reviewed
    cite: "Sekulic A, Migden MR, Oro AE, et al. Efficacy and safety of vismodegib in advanced basal-cell carcinoma. N Engl J Med. 2012;366(23):2171-2179."
    doi: "10.1056/NEJMoa1113600"
    pmid: "22670902"
    url: "https://doi.org/10.1056/NEJMoa1113600"
  - id: stratigos-2021-cemiplimab
    type: peer-reviewed
    cite: "Stratigos AJ, Sekulic A, Peris K, et al. Cemiplimab in locally advanced basal cell carcinoma after hedgehog inhibitor therapy: an open-label, multi-centre, single-arm, phase 2 trial (EMPOWER-BCC 1). Lancet Oncol. 2021;22(6):848-857."
    doi: "10.1016/S1470-2045(21)00126-1"
    pmid: "33930313"
    url: "https://doi.org/10.1016/S1470-2045(21)00126-1"
cross_links:
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Cemiplimab (anti-PD-1) approved for locally advanced and metastatic BCC after SMO inhibitor progression (EMPOWER-BCC); ORR ~30%; pembrolizumab also active; PD-L1 expression in BCC correlates with TIL density; immunotherapy is the main option after vismodegib failure."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations in ~60-70% of BCC (UV signature CC→TT mutations at dipyrimidine sites); TP53 loss cooperates with PTCH1/SMO Hedgehog activation in BCC pathogenesis; p53 pathway inactivation reduces apoptotic response to UV damage; TERT activation also common in advanced BCC."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "HPV-negative BCC (the vast majority) retains RB1 intact; UV-induced CDKN2A deletion in some BCC allows CDK4/6-RB bypass; RB pathway loss is more relevant in Merkel cell carcinoma (skin cancer driven by MCPyV large T antigen targeting RB/p53 simultaneously)."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt/β-catenin pathway is activated in a subset of BCC alongside Hedgehog activation → cooperative proliferative drive; CTNNB1 mutations uncommon in BCC but Wnt ligand overexpression occurs; combined SMO + porcupine inhibition studied in advanced or vismodegib-resistant BCC."
  - target: 01-human/03-molecular/ptch1
    relation: connects-to
    note: "PTCH1 loss-of-function initiates >90% of BCC; UV-induced C→T transitions in PTCH1 → SMO derepression → GLI nuclear translocation; biallelic PTCH1 inactivation required for BCC; germline PTCH1 mutation causes Gorlin syndrome with multiple early-onset BCCs and medulloblastoma."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "SMO activating mutations in ~40-50% of sporadic BCC (W535L most common); vismodegib and sonidegib bind SMO transmembrane domain → inhibit HH signaling; SMO D473H mutation causes on-target vismodegib resistance; cemiplimab (anti-PD-1) is the approved option at vismodegib failure."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "BCC arises from basal keratinocytes of the hair follicle or interfollicular epidermis; UV-B → C→T dipyrimidine mutations → PTCH1/TP53/SMO → clonal BCC expansion; H-zone BCCs require Mohs surgery; skin transplant recipients (immunosuppressed) have 10-30× BCC risk."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "Gorlin syndrome (nevoid BCC syndrome) is the germline form of BCC: an inherited PTCH1 mutation means every cell already carries the first Hedgehog hit, so patients develop dozens to hundreds of BCCs from adolescence — the Mendelian counterpart of sporadic UV-driven BCC."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Basal cell carcinoma and melanoma are the most and least common deadly skin cancers: both UV-driven, but BCC almost never metastasizes (locally destructive via Hedgehog) while melanoma kills through early metastasis (BRAF/MAPK-driven) — biology dictating wholly different care."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "BCC's heavy UV mutational load makes it immunogenic, so when SMO inhibitors fail, anti-PD-1 cemiplimab unleashes cytotoxic CD8+ T cells against tumor neoantigens (EMPOWER-BCC ORR ~30%); conversely, T-cell suppression in transplant recipients raises BCC risk 10-30×."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ultraviolet photons are the prime cause of basal cell carcinoma: UVB induces signature C→T 'UV mutations' in PTCH1 and TP53 of basal keratinocytes, activating Hedgehog signaling; cumulative sun and fair skin make it the commonest human cancer, and photoprotection prevents it."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Immunosurveillance restrains basal cell carcinoma: organ-transplant recipients and the chronically immunosuppressed develop BCC at sharply higher rates and more aggressively, showing the immune system normally clears UV-damaged keratinocyte clones before they become tumors."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Basal cell carcinoma depends on its stroma: tumor cells recruit and reprogram fibroblasts into a characteristic peritumoral myxoid stroma that supplies Hedgehog and growth signals, and the retraction cleft between tumor nests and this stroma is a classic histologic clue."
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "Rothmund-Thomson syndrome predisposes to basal cell carcinoma: defective RECQL4-dependent DNA repair leaves poikilodermatous skin unable to fix UV damage, so BCC and squamous cell carcinoma arise early—a genodermatosis like Gorlin and xeroderma pigmentosum."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Basal cell carcinoma is more common and aggressive in HIV/AIDS and other immunosuppression: weakened immune surveillance lets UV-damaged keratinocytes escape, so skin cancers occur earlier and recur more in HIV and transplant patients—calling for vigilant screening."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Basal cell carcinoma and SHH-subtype medulloblastoma share the hedgehog pathway: PTCH1/SMO mutations drive both and Gorlin syndrome predisposes to each—so the SMO inhibitor vismodegib developed for advanced BCC is also active in hedgehog-driven medulloblastoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help restrain basal cell carcinoma: innate immune surveillance clears UV-damaged keratinocytes, so immunosuppressed patients develop more skin cancers—why BCC is commoner in transplant recipients and why immunotherapy treats advanced disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven angiogenesis feeds basal cell carcinoma: though BCC grows slowly and rarely metastasizes, it recruits new blood vessels via VEGF to sustain expanding tumor nests, and this vascularity underlies the telangiectasias seen over a pearly BCC nodule."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Basal cell carcinoma remodels dermal collagen as it invades: tumor nests provoke a fibrous stroma and degrade surrounding collagen to spread locally, which is why neglected BCCs become destructively invasive rodent ulcers despite almost never metastasizing."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Basal cell carcinoma is the commonest cancer of the integumentary system: it arises from basal keratinocytes driven by UV-induced Hedgehog-pathway mutations, so it is the prototypical sun-related skin malignancy—locally invasive but rarely metastatic."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A loss features in skin cancers including basal cell carcinoma: UV damage to this tumor-suppressor removes a brake on the cell cycle, compounding the Hedgehog-pathway mutations that drive BCC—linking sun-induced DNA damage to unchecked growth."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Basal cell carcinoma exposes the double edge of sunlight: the same UV that lets skin make vitamin D also mutates basal keratinocytes to cause BCC, so sun exposure is both a vitamin source and the dominant risk factor for this skin cancer."
---

# Basal Cell Carcinoma

## Overview

**Basal cell carcinoma (BCC)** is the most common cancer in humans, accounting for ~3-4 million new cases per year in the United States alone and approximately 80% of all non-melanoma skin cancers. BCC arises from basal keratinocytes of the hair follicle and epidermis, driven primarily by **ultraviolet (UV) radiation**-induced DNA damage and near-universal activation of the **Hedgehog (HH) signaling pathway** through PTCH1 loss or SMO mutation. Despite its extremely high incidence, BCC carries a favorable prognosis: the vast majority are treated with local excision, Mohs micrographic surgery, or destructive modalities, with <0.1% metastasis rate [^sekulic-2012-vismodegib].

**Epidemiology:**
- ~3-4 million cases/year in US; worldwide most common cancer
- Lifetime risk: ~30% in fair-skinned populations
- Male:Female ~1.5:1; incidence rises sharply with age (median age ~65)
- Risk factors: UV radiation (cumulative sun exposure, tanning bed use), prior ionizing radiation, immunosuppression (organ transplant recipients have 10-30× higher BCC risk), arsenic exposure, prior BCC/SCC
- Anatomical distribution: ~80% on head and neck (sun-exposed); nose (most common single site)
- Geographic: Highest rates in Australia/New Zealand → due to UV exposure, Fitzpatrick skin type I-II

**Gorlin syndrome (Basal Cell Nevus Syndrome, BCNS):**
- Autosomal dominant; germline PTCH1 mutation (~85%) or PTCH2/SUFU mutation (~5%)
- Features: Multiple BCCs beginning in second decade, odontogenic keratocysts, calcification of falx cerebri, medulloblastoma (desmoplastic type), skeletal anomalies (bifid ribs), ovarian fibromas, macrocephaly
- Management: Vismodegib/sonidegib reduces new BCC formation; avoid PTCH1-loss-promoting DNA damage (minimize ionizing radiation, UV); oral retinoids (isotretinoin) partially protective

## Structure

### Histological subtypes and clinical behavior

**Histological subtypes (affect recurrence risk and treatment):**

| Subtype | Histology | Growth pattern | Risk |
|---------|-----------|----------------|------|
| Nodular | Well-circumscribed nodule; palisading nuclei | Expansile | Low |
| Superficial | Nests attached to overlying epidermis | Lateral spread | Low |
| Morpheaform/sclerosing | Thin strands in desmoplastic stroma | Infiltrative | High |
| Infiltrative | Spiky, jagged tumor nests | Infiltrative | High |
| Micronodular | Small discrete nests | Infiltrative | High |
| Basosquamous | BCC + SCC features | Intermediate | Intermediate-high |
| Metatypical | Similar to basosquamous | Intermediate | Intermediate |

High-risk subtypes (morpheaform, infiltrative, micronodular) have higher rates of recurrence after standard excision → Mohs micrographic surgery preferred.

### Molecular landscape

**PTCH1 mutations (>90% of BCC):**
- PTCH1 is the classic tumor suppressor in BCC (two-hit model: UV-induced mutation + loss of heterozygosity)
- UV signature (C→T transitions at dipyrimidine sites) in PTCH1 mutations confirms UV etiology
- PTCH1 loss → SMO no longer inhibited → constitutive GLI activation → BCC initiation

**SMO mutations (~40-50% of sporadic BCC):**
- Gain-of-function SMO mutations that mimic the activated (HH-ON) conformation without ligand binding
- W535L (most common, ~30% of SMO-mutant BCC) → locks SMO in active state; also targets drug binding pocket → reduces vismodegib binding
- Other activating mutations: L412F, S533N, I408L

**TP53 mutations (~60-70% of BCC):**
- UV-signature C→T transitions at hotspots; early events in BCC pathogenesis
- Cooperate with PTCH1/SMO activation to drive full BCC malignancy

**Other molecular alterations:**
- CDKN2A (p16) deletion: ~10-30% of BCC
- MYCN amplification: Aggressive BCC
- PI3K-AKT pathway: Activated in ~30% of advanced BCC

## Function

### Normal basal keratinocyte biology and BCC pathogenesis

**Hair follicle biology:**
BCC is thought to arise from hair follicle bulge stem cells or interfollicular basal keratinocytes that aberrantly activate the HH pathway. SHH from dermal papilla → physiological HH signaling → hair follicle cycling. BCC may represent a pathological "permanent anagen" state where HH signaling is constitutively active.

**UV carcinogenesis:**
UV-B (280-315 nm) → pyrimidine dimer formation (CPD, 6-4 PP) at dipyrimidine sites → NER pathway → if unrepaired → C→T transition mutations → PTCH1, TP53, SMO mutations → HH pathway activation → BCC initiation.

The basal layer sits on the basement membrane and contains stem cells and transient amplifying cells that proliferate and differentiate upward. PTCH1 mutation in a basal stem cell → clonal HH-activated expansion → BCC formation over years to decades.

### Immune evasion in BCC

BCC has a complex immune microenvironment:
- High tumor mutational burden (TMB) from UV signature → high neoantigen load → potentially immunogenic
- PD-L1 expressed on BCC tumor cells and macrophages → T cell exclusion
- CD8+ TIL density correlates with PD-L1 expression and immunotherapy response
- Vismodegib treatment → HH pathway suppression → partial immune restoration (increased TIL density) in some patients; combination SMO inhibitor + PD-1 being studied
- Transplant BCC: Immunosuppression → impaired T cell surveillance → 10-30× higher BCC incidence; often multiple, aggressive, or metastatic in solid organ transplant recipients

## Pathology

### Staging and risk assessment

**Most BCC are clinical/pathological staging:**
- Low-risk BCC: Size <2 cm, well-defined borders, primary lesion, non-aggressive subtype, not in high-risk location (H-zone: central face, eyelids, ears, lips, nose), immunocompetent patient
- High-risk BCC: Size ≥2 cm, OR in H-zone, OR aggressive subtype, OR recurrent/previously treated, OR perineural invasion, OR vascular invasion, OR immunosuppressed patient

**Metastatic BCC (<0.1%):**
- Requires regional lymph node or distant spread → AJCC staging applies
- Portends extremely poor prognosis (median OS <10 months without effective therapy)
- Risk factors for metastasis: Large tumor (>6 cm), deep invasion, prior radiation, morpheaform/infiltrative subtype, basosquamous subtype, immunosuppression

### Treatment

**Surgical:**
- **Standard excision:** 4 mm margin for low-risk BCC; recurrence rate <2%
- **Mohs micrographic surgery (MMS):** 100% margin control; gold standard for high-risk BCC, high-risk locations (H-zone), recurrent BCC, morpheaform/infiltrative subtypes; recurrence rate <1%
- **Curettage and electrodesiccation (C&E):** For low-risk, non-hair-bearing areas; alternative to excision for select tumors

**Non-surgical (destructive/topical):**
- **Cryotherapy:** Liquid nitrogen; for small superficial/nodular BCC; not for aggressive subtypes
- **Topical imiquimod (Aldara):** TLR7 agonist → innate immune activation → for superficial BCC; 80-85% complete clinical response; lower cure rate than excision
- **Topical 5-fluorouracil:** Antimetabolite; superficial BCC; similar to imiquimod
- **Photodynamic therapy (PDT):** Aminolevulinic acid → protoporphyrin IX → light activation → ROS → cell death; superficial BCC

**Radiation therapy:**
- For surgical ineligibility or patient preference; 5-year recurrence 5-10%; useful for older patients with cosmetically challenging locations (eyelid, nose, ear)

**Targeted therapy (SMO inhibitors):**
- **Vismodegib (Erivedge, 150 mg PO daily):** [^sekulic-2012-vismodegib] FDA approved 2012; ORR 43% (metastatic), 30% (locally advanced); median DOR 7.6 months; used for locally advanced (unresectable) or metastatic BCC; Gorlin syndrome (reduces new BCC)
- **Sonidegib (Odomzo, 200 mg PO daily):** FDA approved 2015; BOLT trial → ORR 43% (locally advanced) at 200 mg; comparable to vismodegib; drug interactions differ (sonidegib is CYP3A4 substrate)
- **Toxicities (both agents):** Muscle cramps (68%), alopecia (64%), dysgeusia (51%), weight loss (36%), fatigue, nausea, diarrhea; highly teratogenic — Category X; effective contraception mandatory; QTc monitoring
- **Resistance:** ~50% develop resistance within 12-18 months; on-target SMO mutations (D473H most common); off-target (GLI amplification, KRAS); switch to cemiplimab at progression

**Immunotherapy:**
- **Cemiplimab (Libtayo, 350 mg IV every 3 weeks):** [^stratigos-2021-cemiplimab] FDA approved 2021 for locally advanced or metastatic BCC after SMO inhibitor progression; EMPOWER-BCC trial → ORR 29% in locally advanced, 21% in metastatic; durable responses (~median DOR not reached); first PD-1 inhibitor approved in BCC
- **Pembrolizumab:** Case series and basket trial data; similar ORR; not FDA-approved in BCC
- Rationale: High TMB from UV signature → neoantigen-rich tumor → PD-1 blockade unlocks T cell response; PD-L1 expression in ~40% of advanced BCC

## Connections

- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Cemiplimab (anti-PD-1) approved for locally advanced and metastatic BCC after SMO inhibitor progression (EMPOWER-BCC); ORR ~30%; pembrolizumab also active; PD-L1 expression in BCC correlates with tumor-infiltrating lymphocytes; immunotherapy is the main option after vismodegib failure.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations in ~60-70% of BCC (UV signature CC→TT mutations at dipyrimidine sites); TP53 loss cooperates with PTCH1/SMO Hedgehog activation in BCC pathogenesis; p53 pathway inactivation reduces apoptotic response to UV damage; TERT activation also common in advanced BCC.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — HPV-negative BCC (the vast majority) retains RB1 intact; UV-induced CDKN2A deletion in some BCC allows CDK4/6-RB bypass; RB pathway loss is more relevant in Merkel cell carcinoma (skin cancer driven by MCPyV large T antigen targeting RB/p53 simultaneously).
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/β-catenin pathway is activated in a subset of BCC alongside Hedgehog activation → cooperative proliferative drive; CTNNB1 mutations uncommon in BCC but Wnt ligand overexpression occurs; combined SMO + porcupine inhibition studied in advanced or vismodegib-resistant BCC.
- `connects-to` → **[PTCH1](../../03-molecular/ptch1/README.md)** — PTCH1 loss-of-function is the defining molecular event in >90% of BCC; UV-induced C→T mutations in PTCH1 → SMO derepression → constitutive GLI nuclear translocation; germline PTCH1 mutation causes Gorlin syndrome (BCNS) with multiple early-onset BCCs, odontogenic keratocysts, and medulloblastoma risk.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — SMO activating mutations (W535L most common) in ~40-50% of sporadic BCC → constitutive HH signaling independent of PTCH1 ligand; vismodegib and sonidegib bind SMO transmembrane domain; SMO D473H mutation causes on-target resistance; cemiplimab (anti-PD-1) is the approved post-vismodegib option.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — BCC arises from basal keratinocytes of hair follicle or interfollicular epidermis; UV-B → dipyrimidine mutations → PTCH1/TP53/SMO → clonal BCC expansion over decades; H-zone BCCs (central face, eyelids) require Mohs surgery; organ transplant recipients (immunosuppressed) have 10-30× BCC risk.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — Gorlin syndrome (nevoid BCC syndrome) is the germline form of BCC: an inherited PTCH1 mutation means every cell already carries the first Hedgehog hit, so patients develop dozens to hundreds of BCCs from adolescence — the Mendelian counterpart of sporadic UV-driven BCC.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Basal cell carcinoma and melanoma are the most and least common deadly skin cancers: both UV-driven, but BCC almost never metastasizes (locally destructive via Hedgehog) while melanoma kills through early metastasis (BRAF/MAPK-driven) — biology dictating wholly different care.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — BCC's heavy UV mutational load makes it immunogenic, so when SMO inhibitors fail, anti-PD-1 cemiplimab unleashes cytotoxic CD8+ T cells against tumor neoantigens (EMPOWER-BCC ORR ~30%); conversely, T-cell suppression in transplant recipients raises BCC risk 10-30×.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ultraviolet photons are the prime cause of basal cell carcinoma: UVB induces signature C→T 'UV mutations' in PTCH1 and TP53 of basal keratinocytes, activating Hedgehog signaling; cumulative sun and fair skin make it the commonest human cancer, and photoprotection prevents it.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Immunosurveillance restrains basal cell carcinoma: organ-transplant recipients and the chronically immunosuppressed develop BCC at sharply higher rates and more aggressively, showing the immune system normally clears UV-damaged keratinocyte clones before they become tumors.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Basal cell carcinoma depends on its stroma: tumor cells recruit and reprogram fibroblasts into a characteristic peritumoral myxoid stroma that supplies Hedgehog and growth signals, and the retraction cleft between tumor nests and this stroma is a classic histologic clue.
- `connects-to` → **[Rothmund-Thomson Syndrome](../rothmund-thomson/README.md)** — Rothmund-Thomson syndrome predisposes to basal cell carcinoma: defective RECQL4-dependent DNA repair leaves poikilodermatous skin unable to fix UV damage, so BCC and squamous cell carcinoma arise early—a genodermatosis like Gorlin and xeroderma pigmentosum.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Basal cell carcinoma is more common and aggressive in HIV/AIDS and other immunosuppression: weakened immune surveillance lets UV-damaged keratinocytes escape, so skin cancers occur earlier and recur more in HIV and transplant patients—calling for vigilant screening.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Basal cell carcinoma and SHH-subtype medulloblastoma share the hedgehog pathway: PTCH1/SMO mutations drive both and Gorlin syndrome predisposes to each—so the SMO inhibitor vismodegib developed for advanced BCC is also active in hedgehog-driven medulloblastoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help restrain basal cell carcinoma: innate immune surveillance clears UV-damaged keratinocytes, so immunosuppressed patients develop more skin cancers—why BCC is commoner in transplant recipients and why immunotherapy treats advanced disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis feeds basal cell carcinoma: though BCC grows slowly and rarely metastasizes, it recruits new blood vessels via VEGF to sustain expanding tumor nests, and this vascularity underlies the telangiectasias seen over a pearly BCC nodule.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Basal cell carcinoma remodels dermal collagen as it invades: tumor nests provoke a fibrous stroma and degrade surrounding collagen to spread locally, which is why neglected BCCs become destructively invasive rodent ulcers despite almost never metastasizing.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Basal cell carcinoma is the commonest cancer of the integumentary system: it arises from basal keratinocytes driven by UV-induced Hedgehog-pathway mutations, so it is the prototypical sun-related skin malignancy—locally invasive but rarely metastatic.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss features in skin cancers including basal cell carcinoma: UV damage to this tumor-suppressor removes a brake on the cell cycle, compounding the Hedgehog-pathway mutations that drive BCC—linking sun-induced DNA damage to unchecked growth.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Basal cell carcinoma exposes the double edge of sunlight: the same UV that lets skin make vitamin D also mutates basal keratinocytes to cause BCC, so sun exposure is both a vitamin source and the dominant risk factor for this skin cancer.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^sekulic-2012-vismodegib]: Sekulic A, Migden MR, Oro AE, et al. Efficacy and safety of vismodegib in advanced basal-cell carcinoma. *N Engl J Med.* 2012;366(23):2171-2179. [doi:10.1056/NEJMoa1113600](https://doi.org/10.1056/NEJMoa1113600) · [PubMed 22670902](https://pubmed.ncbi.nlm.nih.gov/22670902/)
[^stratigos-2021-cemiplimab]: Stratigos AJ, Sekulic A, Peris K, et al. Cemiplimab in locally advanced basal cell carcinoma after hedgehog inhibitor therapy: an open-label, multi-centre, single-arm, phase 2 trial (EMPOWER-BCC 1). *Lancet Oncol.* 2021;22(6):848-857. [doi:10.1016/S1470-2045(21)00126-1](https://doi.org/10.1016/S1470-2045(21)00126-1) · [PubMed 33930313](https://pubmed.ncbi.nlm.nih.gov/33930313/)
