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
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eyelid is a top site for basal cell carcinoma: chronic sun exposure makes BCC the most common eyelid and periocular cancer, where slow local invasion can threaten the eye itself—so a non-healing eyelid lesion warrants biopsy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "UV light disarms the skin's dendritic cells to let BCC grow: sunlight depletes and impairs epidermal Langerhans cells, weakening immune surveillance, so UV both mutates keratinocytes and removes the immune watch that would clear early tumors."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells crowd around basal cell carcinoma: they accumulate at the tumor edge and release mediators that remodel stroma and drive angiogenesis, so these innate cells help build the supportive microenvironment BCC needs to invade."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "BCC leans on TGF-beta in its stroma: the tumor and its fibroblasts secrete TGF-beta, which suppresses anti-tumor immunity and drives the fibrous stroma around nests of basal cells, complementing the Hedgehog signaling that fuels growth."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "BCC shelters behind regulatory T cells: Tregs accumulate in the tumor and dampen the cytotoxic response, part of the immune evasion that PD-1 blockade (cemiplimab) tries to reverse in advanced basal cell carcinoma."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages support BCC: recruited into the stroma, they adopt a pro-tumor phenotype that promotes angiogenesis and immune suppression around the slow-growing but locally invasive basal cell tumor."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Basal cell carcinoma is born from oxygen's dark side under UV: sunlight drives reactive oxygen species and DNA-damaging photochemistry in skin cells, so cumulative ultraviolet oxidative injury is the root cause of the most common human cancer."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-kB helps basal cell carcinoma survive UV assault: ultraviolet light and inflammation activate this switch, promoting cell survival and a tumor-friendly inflammatory niche that lets damaged basal cells persist and grow."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxia shapes the basal cell tumor through HIF-1alpha: as the slow-growing nodule outpaces its blood supply, HIF drives VEGF and angiogenesis, helping the locally invasive cancer recruit the vessels it needs to expand."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "The morpheaform basal cell carcinoma hides in fibrosis: this sclerosing subtype provokes a dense fibrous stroma, so the tumor infiltrates like scar tissue with ill-defined edges that make it hard to fully excise."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Aggressive basal cell carcinoma can track along nerves: perineural invasion lets the tumor creep down peripheral nerves beyond its visible border, causing pain or numbness and demanding wider treatment."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Basal cell carcinoma is recognized by its vessels: endothelial cells form the fine, branching surface telangiectasias over a pearly nodule—a hallmark seen on dermoscopy—and feed the tumor's growth."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Neglected facial basal cell carcinoma can reach the brain: by creeping along cranial nerves, advanced tumors invade the skull base and intracranial space, a rare but grave outcome of a usually local cancer."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "The Gorlin syndrome behind multiple basal cell carcinomas calcifies the brain: calcification of the falx cerebri, the dural sheet between the hemispheres, is a diagnostic clue to the inherited disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Basal cell carcinoma dodges death through BCL-2: it strongly expresses this anti-apoptotic protein, which both helps the tumor survive and serves as a marker on biopsy."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy fingerprints basal cell carcinoma: nests of basaloid cells line up in a palisade at their edge, joined by desmosomes and filled with tonofilaments, the ultrastructure of a tumor that mimics the skin's basal layer."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "On the rare occasion basal cell carcinoma metastasizes, it heads for the lung: although it almost always stays local, the exceptional spreading case seeds the lungs and bones, a vanishingly rare but documented event."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Neglected basal cell carcinoma gnaws into bone: the 'rodent ulcer' is locally destructive, eroding through cartilage and into the underlying bone of the face and skull if left untreated for years."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Aggressive basal cell carcinoma creeps along nerves: perineural invasion lets it track centrally beyond the visible tumor, causing numbness or tingling and a higher risk of recurrence that pushes toward wider excision or radiation."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The hedgehog-blocking drugs ache in the muscles: vismodegib and sonidegib, used for advanced BCC, commonly cause muscle spasms and cramps along with hair loss and taste change — side effects that limit how long patients tolerate them."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Immunotherapy now reaches advanced BCC: the anti-PD-1 antibody cemiplimab can shrink locally advanced or metastatic tumors that have progressed on or cannot tolerate hedgehog inhibitors, a second line for the rare aggressive cases."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hedgehog drugs are fiercely teratogenic: because Sonic hedgehog patterns the embryo, vismodegib and sonidegib can cause severe birth defects, demanding strict contraception and a ban on blood donation during and after treatment."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Failing immune surveillance unleashes BCC: organ-transplant recipients and CLL patients, their neutrophils and lymphocytes suppressed, develop numerous and more aggressive basal cell carcinomas as the skin's immune guard falls."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Old radiation seeds later skin cancer: childhood radiotherapy to fields like the head and neck — the same exposure that risks thyroid cancer — raises the chance of basal cell carcinoma arising in the irradiated skin decades on."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Beyond hedgehog, growth-factor signaling helps: basal cell carcinomas express EGFR, whose activation supports their proliferation and survival and may contribute to resistance when hedgehog inhibitors fail."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Hedgehog drives the cell cycle through cyclin D1: unchecked GLI signaling in BCC raises cyclin D1 to push cells past the G1 checkpoint, the proliferative engine downstream of the PTCH1-SMO pathway."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: connects-to
    note: "Viruses may cofactor with the sun: beta-papillomaviruses are implicated as cocarcinogens in UV-driven non-melanoma skin cancer, especially in the immunosuppressed, adding a viral hit to the genetic damage behind some BCCs."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Light therapy for psoriasis carries a cost: long-term PUVA (psoralen plus UVA) phototherapy raises the lifetime risk of non-melanoma skin cancers including basal cell carcinoma, so cumulative dose is tracked and skin surveyed."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Transplant survivors grow skin cancers: chronic graft-versus-host disease and its prolonged immunosuppression—compounded by photosensitizing voriconazole—drive basal cell and other skin cancers in allogeneic stem-cell transplant recipients."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Aggressive subtypes burrow into fat: infiltrative and morpheaform basal cell carcinomas extend deep into the subcutaneous adipocyte layer, a spread that widens surgical margins and is why Mohs surgery traces the tumor's edges."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "UV and inflammation activate STAT3 in the skin: STAT3 signaling promotes keratinocyte survival and proliferation after UV damage, contributing to the non-melanoma skin carcinogenesis that gives rise to basal cell carcinoma."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "A leukemia that lets skin cancers run: chronic lymphocytic leukemia's immune dysfunction sharply raises the incidence and aggressiveness of basal cell and other skin cancers, which behave more invasively in these patients."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A neglected giant tumor can become infected: although basal cell carcinoma almost never metastasizes, large ulcerated or neglected lesions—especially in immunosuppressed patients—can develop wound infection that progresses to sepsis."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "Immune loss multiplies the lesions: HIV-related immunosuppression raises the incidence of basal cell carcinoma and can make it more aggressive and recurrent, part of the broader skin-cancer excess in immunocompromised hosts."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "It can erode into a non-healing ulcer: untreated basal cell carcinoma slowly destroys tissue as a 'rodent ulcer,' a chronic non-healing wound that gnaws into skin, cartilage and even bone."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Facial disfigurement weighs on mood: basal cell carcinoma and its surgical removal commonly involve cosmetically sensitive areas of the face, and the resulting scarring and disfigurement can drive depression."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Arsenic links skin and bladder cancer: chronic arsenic exposure causes basal cell carcinomas (often multiple and on covered skin) alongside an elevated risk of bladder cancer, a shared environmental carcinogenesis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Transplant immunosuppression multiplies skin cancer: the chronic immunosuppression after kidney transplantation markedly raises the risk and aggressiveness of basal cell and other skin carcinomas."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Visible lesions and recurrence breed worry: the cosmetically sensitive sites and tendency to develop further skin cancers in basal cell carcinoma fuel health anxiety alongside depression."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Aggressive facial tumours track along nerves: neglected or recurrent basal cell carcinoma, especially on the face, can invade perineurally and spread along cranial nerves toward the skull base."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Perineural spread causes pain and numbness: when basal cell carcinoma invades along nerves, it produces facial paraesthesia, numbness and neuropathic pain that signal deep, advanced disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its targeted drug attacks taste and appetite: the hedgehog-pathway inhibitor vismodegib used for advanced basal cell carcinoma commonly causes severe dysgeusia, nausea and weight loss."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It almost never spreads to nodes: although locally destructive, basal cell carcinoma metastasises to regional lymph nodes only in rare, advanced or neglected cases — an exception to its indolent reputation."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "When it does spread, the lung leads: the rare metastatic basal cell carcinoma most often reaches the lungs, and locally advanced facial tumours can invade toward the sinuses and orbit."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Neglected tumours can erode vessels: a long-ignored 'rodent ulcer' basal cell carcinoma can invade deeply through tissue and erode major vessels, causing life-threatening haemorrhage."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Transplantation multiplies the risk: long-term immunosuppression in kidney and other organ transplant recipients sharply increases basal cell and other skin cancers, demanding lifelong dermatological surveillance."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Sun is double-edged for the skin's endocrine role: the UV radiation that drives basal cell carcinoma is also what the skin uses to synthesise vitamin D, a hormone precursor."
  - target: 03-medicine/03-food/sulforaphane
    relation: connects-to
    note: "Dietary chemoprevention is studied: sulforaphane from cruciferous vegetables shows photoprotective, chemopreventive activity against UV-induced skin cancer in models, an area of active research."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Hedgehog inhibitors target its driver: vismodegib and sonidegib block SMO in the constitutively active Hedgehog pathway that causes basal cell carcinoma, used for advanced and Gorlin-related disease."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy follows Hedgehog failure: the anti-PD-1 antibody cemiplimab treats locally advanced or metastatic basal cell carcinoma after Hedgehog inhibitors stop working."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "Carcinogen field cancerisation links them: as tobacco and alcohol field-damage the head-and-neck mucosa, UV field damage of sun-exposed skin produces multiple basal cell carcinomas across a damaged field."
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
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eyelid is a top site for basal cell carcinoma: chronic sun exposure makes BCC the most common eyelid and periocular cancer, where slow local invasion can threaten the eye itself—so a non-healing eyelid lesion warrants biopsy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — UV light disarms the skin's dendritic cells to let BCC grow: sunlight depletes and impairs epidermal Langerhans cells, weakening immune surveillance, so UV both mutates keratinocytes and removes the immune watch that would clear early tumors.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells crowd around basal cell carcinoma: they accumulate at the tumor edge and release mediators that remodel stroma and drive angiogenesis, so these innate cells help build the supportive microenvironment BCC needs to invade.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — BCC leans on TGF-beta in its stroma: the tumor and its fibroblasts secrete TGF-beta, which suppresses anti-tumor immunity and drives the fibrous stroma around nests of basal cells, complementing the Hedgehog signaling that fuels growth.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — BCC shelters behind regulatory T cells: Tregs accumulate in the tumor and dampen the cytotoxic response, part of the immune evasion that PD-1 blockade (cemiplimab) tries to reverse in advanced basal cell carcinoma.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages support BCC: recruited into the stroma, they adopt a pro-tumor phenotype that promotes angiogenesis and immune suppression around the slow-growing but locally invasive basal cell tumor.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Basal cell carcinoma is born from oxygen's dark side under UV: sunlight drives reactive oxygen species and DNA-damaging photochemistry in skin cells, so cumulative ultraviolet oxidative injury is the root cause of the most common human cancer.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-kB helps basal cell carcinoma survive UV assault: ultraviolet light and inflammation activate this switch, promoting cell survival and a tumor-friendly inflammatory niche that lets damaged basal cells persist and grow.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Hypoxia shapes the basal cell tumor through HIF-1alpha: as the slow-growing nodule outpaces its blood supply, HIF drives VEGF and angiogenesis, helping the locally invasive cancer recruit the vessels it needs to expand.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — The morpheaform basal cell carcinoma hides in fibrosis: this sclerosing subtype provokes a dense fibrous stroma, so the tumor infiltrates like scar tissue with ill-defined edges that make it hard to fully excise.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Aggressive basal cell carcinoma can track along nerves: perineural invasion lets the tumor creep down peripheral nerves beyond its visible border, causing pain or numbness and demanding wider treatment.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Basal cell carcinoma is recognized by its vessels: endothelial cells form the fine, branching surface telangiectasias over a pearly nodule—a hallmark seen on dermoscopy—and feed the tumor's growth.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Neglected facial basal cell carcinoma can reach the brain: by creeping along cranial nerves, advanced tumors invade the skull base and intracranial space, a rare but grave outcome of a usually local cancer.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — The Gorlin syndrome behind multiple basal cell carcinomas calcifies the brain: calcification of the falx cerebri, the dural sheet between the hemispheres, is a diagnostic clue to the inherited disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Basal cell carcinoma dodges death through BCL-2: it strongly expresses this anti-apoptotic protein, which both helps the tumor survive and serves as a marker on biopsy.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy fingerprints basal cell carcinoma: nests of basaloid cells line up in a palisade at their edge, joined by desmosomes and filled with tonofilaments, the ultrastructure of a tumor that mimics the skin's basal layer.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — On the rare occasion basal cell carcinoma metastasizes, it heads for the lung: although it almost always stays local, the exceptional spreading case seeds the lungs and bones, a vanishingly rare but documented event.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Neglected basal cell carcinoma gnaws into bone: the 'rodent ulcer' is locally destructive, eroding through cartilage and into the underlying bone of the face and skull if left untreated for years.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Aggressive basal cell carcinoma creeps along nerves: perineural invasion lets it track centrally beyond the visible tumor, causing numbness or tingling and a higher risk of recurrence that pushes toward wider excision or radiation.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The hedgehog-blocking drugs ache in the muscles: vismodegib and sonidegib, used for advanced BCC, commonly cause muscle spasms and cramps along with hair loss and taste change — side effects that limit how long patients tolerate them.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Immunotherapy now reaches advanced BCC: the anti-PD-1 antibody cemiplimab can shrink locally advanced or metastatic tumors that have progressed on or cannot tolerate hedgehog inhibitors, a second line for the rare aggressive cases.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hedgehog drugs are fiercely teratogenic: because Sonic hedgehog patterns the embryo, vismodegib and sonidegib can cause severe birth defects, demanding strict contraception and a ban on blood donation during and after treatment.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Failing immune surveillance unleashes BCC: organ-transplant recipients and CLL patients, their neutrophils and lymphocytes suppressed, develop numerous and more aggressive basal cell carcinomas as the skin's immune guard falls.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Old radiation seeds later skin cancer: childhood radiotherapy to fields like the head and neck — the same exposure that risks thyroid cancer — raises the chance of basal cell carcinoma arising in the irradiated skin decades on.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Beyond hedgehog, growth-factor signaling helps: basal cell carcinomas express EGFR, whose activation supports their proliferation and survival and may contribute to resistance when hedgehog inhibitors fail.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Hedgehog drives the cell cycle through cyclin D1: unchecked GLI signaling in BCC raises cyclin D1 to push cells past the G1 checkpoint, the proliferative engine downstream of the PTCH1-SMO pathway.
- `connects-to` → **[HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md)** — Viruses may cofactor with the sun: beta-papillomaviruses are implicated as cocarcinogens in UV-driven non-melanoma skin cancer, especially in the immunosuppressed, adding a viral hit to the genetic damage behind some BCCs.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Light therapy for psoriasis carries a cost: long-term PUVA (psoralen plus UVA) phototherapy raises the lifetime risk of non-melanoma skin cancers including basal cell carcinoma, so cumulative dose is tracked and skin surveyed.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — Transplant survivors grow skin cancers: chronic graft-versus-host disease and its prolonged immunosuppression—compounded by photosensitizing voriconazole—drive basal cell and other skin cancers in allogeneic stem-cell transplant recipients.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Aggressive subtypes burrow into fat: infiltrative and morpheaform basal cell carcinomas extend deep into the subcutaneous adipocyte layer, a spread that widens surgical margins and is why Mohs surgery traces the tumor's edges.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — UV and inflammation activate STAT3 in the skin: STAT3 signaling promotes keratinocyte survival and proliferation after UV damage, contributing to the non-melanoma skin carcinogenesis that gives rise to basal cell carcinoma.
- `connects-to` → **[CLL](../cll/README.md)** — A leukemia that lets skin cancers run: chronic lymphocytic leukemia's immune dysfunction sharply raises the incidence and aggressiveness of basal cell and other skin cancers, which behave more invasively in these patients.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A neglected giant tumor can become infected: although basal cell carcinoma almost never metastasizes, large ulcerated or neglected lesions—especially in immunosuppressed patients—can develop wound infection that progresses to sepsis.
- `connects-to` → **[HIV](../hiv/README.md)** — Immune loss multiplies the lesions: HIV-related immunosuppression raises the incidence of basal cell carcinoma and can make it more aggressive and recurrent, part of the broader skin-cancer excess in immunocompromised hosts.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — It can erode into a non-healing ulcer: untreated basal cell carcinoma slowly destroys tissue as a 'rodent ulcer,' a chronic non-healing wound that gnaws into skin, cartilage and even bone.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Facial disfigurement weighs on mood: basal cell carcinoma and its surgical removal commonly involve cosmetically sensitive areas of the face, and the resulting scarring and disfigurement can drive depression.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Arsenic links skin and bladder cancer: chronic arsenic exposure causes basal cell carcinomas (often multiple and on covered skin) alongside an elevated risk of bladder cancer, a shared environmental carcinogenesis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Transplant immunosuppression multiplies skin cancer: the chronic immunosuppression after kidney transplantation markedly raises the risk and aggressiveness of basal cell and other skin carcinomas.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Visible lesions and recurrence breed worry: the cosmetically sensitive sites and tendency to develop further skin cancers in basal cell carcinoma fuel health anxiety alongside depression.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Aggressive facial tumours track along nerves: neglected or recurrent basal cell carcinoma, especially on the face, can invade perineurally and spread along cranial nerves toward the skull base.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Perineural spread causes pain and numbness: when basal cell carcinoma invades along nerves, it produces facial paraesthesia, numbness and neuropathic pain that signal deep, advanced disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its targeted drug attacks taste and appetite: the hedgehog-pathway inhibitor vismodegib used for advanced basal cell carcinoma commonly causes severe dysgeusia, nausea and weight loss.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It almost never spreads to nodes: although locally destructive, basal cell carcinoma metastasises to regional lymph nodes only in rare, advanced or neglected cases — an exception to its indolent reputation.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — When it does spread, the lung leads: the rare metastatic basal cell carcinoma most often reaches the lungs, and locally advanced facial tumours can invade toward the sinuses and orbit.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Neglected tumours can erode vessels: a long-ignored 'rodent ulcer' basal cell carcinoma can invade deeply through tissue and erode major vessels, causing life-threatening haemorrhage.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Transplantation multiplies the risk: long-term immunosuppression in kidney and other organ transplant recipients sharply increases basal cell and other skin cancers, demanding lifelong dermatological surveillance.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Sun is double-edged for the skin's endocrine role: the UV radiation that drives basal cell carcinoma is also what the skin uses to synthesise vitamin D, a hormone precursor.
- `connects-to` → **[Sulforaphane](../../../03-medicine/03-food/sulforaphane/README.md)** — Dietary chemoprevention is studied: sulforaphane from cruciferous vegetables shows photoprotective, chemopreventive activity against UV-induced skin cancer in models, an area of active research.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Hedgehog inhibitors target its driver: vismodegib and sonidegib block SMO in the constitutively active Hedgehog pathway that causes basal cell carcinoma, used for advanced and Gorlin-related disease.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy follows Hedgehog failure: the anti-PD-1 antibody cemiplimab treats locally advanced or metastatic basal cell carcinoma after Hedgehog inhibitors stop working.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — Carcinogen field cancerisation links them: as tobacco and alcohol field-damage the head-and-neck mucosa, UV field damage of sun-exposed skin produces multiple basal cell carcinomas across a damaged field.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^sekulic-2012-vismodegib]: Sekulic A, Migden MR, Oro AE, et al. Efficacy and safety of vismodegib in advanced basal-cell carcinoma. *N Engl J Med.* 2012;366(23):2171-2179. [doi:10.1056/NEJMoa1113600](https://doi.org/10.1056/NEJMoa1113600) · [PubMed 22670902](https://pubmed.ncbi.nlm.nih.gov/22670902/)
[^stratigos-2021-cemiplimab]: Stratigos AJ, Sekulic A, Peris K, et al. Cemiplimab in locally advanced basal cell carcinoma after hedgehog inhibitor therapy: an open-label, multi-centre, single-arm, phase 2 trial (EMPOWER-BCC 1). *Lancet Oncol.* 2021;22(6):848-857. [doi:10.1016/S1470-2045(21)00126-1](https://doi.org/10.1016/S1470-2045(21)00126-1) · [PubMed 33930313](https://pubmed.ncbi.nlm.nih.gov/33930313/)
