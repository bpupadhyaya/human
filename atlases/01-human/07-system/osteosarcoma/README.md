---
schema: human-scale-entry/v1
id: osteosarcoma
name: Osteosarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Osteosarcoma is the most common primary malignant bone tumor; peak 10-20 years; RB1 biallelic loss ~70-75%, TP53 ~30-40%, MDM2 amplification ~6-8%, CDKN2A deletion ~20-30%; MAP protocol (methotrexate+doxorubicin+cisplatin); localized 5-year OS ~70-75%; metastatic ~20-25%."
aliases: ["osteosarcoma", "OSA", "OS bone", "osteogenic sarcoma", "high-grade osteosarcoma", "MAP protocol bone tumor", "pediatric bone cancer", "conventional osteosarcoma"]
sources:
  - id: bielack-2002-coss-osteosarcoma
    type: peer-reviewed
    cite: "Bielack SS, Kempf-Bielack B, Delling G, et al. Prognostic factors in high-grade osteosarcoma of the extremities or trunk: an analysis of 1,702 patients treated on neoadjuvant Cooperative Osteosarcoma Study Group protocols. J Clin Oncol. 2002;20(3):776-790."
    doi: "10.1200/JCO.2002.20.3.776"
    pmid: "11821461"
    url: "https://doi.org/10.1200/JCO.2002.20.3.776"
  - id: marina-2016-euramos1-osteosarcoma
    type: peer-reviewed
    cite: "Marina NM, Smeland S, Bielack SS, et al. Comparison of MAPIE versus MAP in patients with a poor response to preoperative chemotherapy for newly diagnosed high-grade osteosarcoma (EURAMOS-1). Lancet Oncol. 2016;17(10):1396-1408."
    doi: "10.1016/S1470-2045(16)30214-5"
    pmid: "27569442"
    url: "https://doi.org/10.1016/S1470-2045(16)30214-5"
cross_links:
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion (~20-30% osteosarcoma) eliminates both p16 (→ CDK4/6 → RB1 inactivation) and ARF (→ MDM2 → p53 loss); CDK4 amplification (~6-8%) and CDKN2A deletion are mutually exclusive alternative Rb/p53 co-inactivation mechanisms in OS."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 biallelic inactivation in ~70-75% high-grade osteosarcoma via deletion, mutation, or methylation; RB1 LOF → E2F-driven proliferation → CCND1/CDK4 upregulation; germline RB1 (hereditary retinoblastoma) increases osteosarcoma risk ~1,000-fold."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations/deletions in ~30-40% high-grade osteosarcoma; MDM2 amplification is mutually exclusive with TP53 mutation as both de-repress MDM2 → p53 degradation; Li-Fraumeni syndrome (germline TP53) confers ~15-fold excess OS risk; TP53 loss predicts poor histologic response."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2 amplification (~6-8% osteosarcoma, ~90% well-differentiated liposarcoma) functionally mimics ARF loss → rapid p53 ubiquitination; MDM2 amplification and TP53 mutation are mutually exclusive in OS; MDM2 inhibitors (idasanutlin) in trials for MDM2-amplified sarcomas."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Osteosarcoma arises from osteoblast progenitors that produce malignant osteoid — its diagnostic hallmark; loss of RB1 and TP53 checkpoints lets these RUNX2/Osterix-lineage cells proliferate, and the growth spurt's high osteoprogenitor turnover explains the adolescent peak."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Hereditary retinoblastoma (germline RB1 loss) is the prototypical osteosarcoma predisposition, raising OS risk ~500-1000-fold as the classic second malignancy — especially within prior radiation fields; this mirrors the somatic RB1 loss in ~70-75% of sporadic high-grade OS."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The pubertal IGF-1 surge drives osteoprogenitor proliferation via IGF1R → PI3K/AKT and MEK/ERK, helping explain why osteosarcoma peaks during the adolescent growth spurt at the fast-growing metaphyses of the distal femur and proximal tibia; ~40% of OS overexpress IGF1R."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Li-Fraumeni syndrome (germline TP53) is a major osteosarcoma predisposition, raising OS risk ~15-fold and making bone sarcoma a sentinel cancer; this mirrors the somatic TP53 loss in ~30-40% of sporadic high-grade OS, as p53 checkpoint failure is central to osteosarcoma biology."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Osteosarcoma is the most common primary bone cancer, arising at the fast-growing metaphyses of long bones — classically the distal femur and proximal tibia around the knee — in the adolescent growth spurt; it produces malignant osteoid and destroys bone, causing pain and a mass."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the dominant metastatic site in osteosarcoma: hematogenous spread seeds pulmonary nodules that determine prognosis, so chest CT staging is essential and surgical metastasectomy of lung lesions — even repeated — is part of curative-intent therapy with chemotherapy."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Osteosarcoma and Ewing sarcoma are the two commonest bone cancers of adolescence: osteosarcoma makes malignant osteoid and arises at the metaphysis of long bones, while Ewing is a small-round-blue-cell tumor driven by EWSR1-FLI1, often diaphyseal or in flat bones."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Osteosarcoma subverts bone remodeling: its malignant osteoblasts lay down disorganized osteoid and recruit osteoclasts that resorb bone, fueling growth—so bone-targeted agents like bisphosphonates, denosumab, and mifamurtide have been trialed against it."
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "Rothmund-Thomson syndrome is a hereditary cause of osteosarcoma: biallelic RECQL4 helicase loss yields poikiloderma, skeletal defects, and a markedly raised osteosarcoma risk—a DNA-repair syndrome that, with Li-Fraumeni and retinoblastoma, predisposes to it."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "Osteosarcoma and MPNST are both aggressive sarcomas that arise as radiation-induced second cancers: years after radiotherapy a high-grade sarcoma can emerge in the treated field, both resist chemotherapy—so a new mass in an irradiated bone or nerve raises alarm."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Osteosarcoma is the tumor that makes bone: its malignant osteoblasts deposit immature osteoid that mineralizes with calcium, producing the dense, disorganized 'sunburst' bone on imaging—calcified matrix distinguishes it from other bone sarcomas."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Osteosarcoma is relatively radioresistant, unlike Ewing sarcoma: photon radiotherapy gives poor local control, so wide surgical resection plus chemotherapy is the mainstay, with radiation reserved for unresectable or palliative cases."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Osteosarcoma is a malignant spindle-cell tumor making osteoid: its fibroblast-like mesenchymal cells produce immature bone matrix directly, distinguishing it from other sarcomas—so finding tumor cells laying down osteoid is the diagnostic hallmark on biopsy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven angiogenesis fuels osteosarcoma and predicts spread: the tumor secretes VEGF to vascularize and metastasize (chiefly to lung), high levels worsen prognosis, and anti-angiogenic kinase inhibitors are used in relapsed disease."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The PI3K/mTOR pathway is active in osteosarcoma: growth signaling through mTOR drives proliferation and survival, so mTOR inhibitors (often with other agents) are studied in this chemotherapy-resistant sarcoma where few targeted options exist."
---

# Osteosarcoma

## Overview

**Osteosarcoma (OS)** is the most common primary malignant bone tumor, with ~1,000 new cases/year in the USA (~5 per million/year). It arises from primitive mesenchymal bone-forming cells (osteoblast progenitors) and is defined by the production of malignant osteoid. OS shows a **bimodal age distribution**: a dominant first peak in adolescents and young adults (10-20 years, coinciding with the pubertal growth spurt) and a smaller second peak in adults >65 years (often secondary to Paget's disease, prior radiation, or de-differentiated bone lesions). The metaphyses of the long bones in the lower extremity are the most common sites: **distal femur** (~40%), **proximal tibia** (~20%), and **proximal humerus** (~10%).

**Predisposition syndromes:**
- **Hereditary retinoblastoma** (germline RB1): ~500-fold increased OS risk (~6% lifetime); the prototypical RB1-associated second malignancy; OS risk further elevated in patients who received external-beam radiation for the primary retinoblastoma
- **Li-Fraumeni syndrome** (germline TP53): ~15-fold excess OS risk; ~3-4% of all OS have germline TP53
- **Rothmund-Thomson syndrome** (RECQL4 helicase): congenital poikiloderma + ~30% lifetime OS risk; RECQL4 mutations disrupt DNA replication and repair in osteoprogenitors
- **Werner syndrome** (WRN helicase): adult-onset progeria; premature OS in second OS peak
- **Paget's disease of bone**: osteosarcomatous transformation in ~1% after >10 years; 5-year OS after transformation <5%

**OS prognosis:**
- Localized extremity: 5-year OS ~70-75%
- Localized axial/pelvis/skull: 5-year OS ~30-50% (R0 resection often unachievable)
- Pulmonary metastases (most common site, ~20% at diagnosis): 5-year OS ~20-30%; complete resection of lung mets improves survival
- Relapsed/refractory: 5-year OS ~15-20% (second-line chemotherapy + surgery)

## Structure

### Histological subtypes

**High-grade conventional OS (~80% of all OS):**
- **Osteoblastic** (~50% of conventional): abundant osteoid/woven bone; densely packed spindle cells; "sunburst" periosteal reaction on X-ray; ALP markedly elevated
- **Chondroblastic** (~25%): malignant chondroid matrix predominates; cartilaginous lobules + osteoid foci; MRI shows lobulated T2-hyperintense areas; can mimic chondrosarcoma (IDHA-negative, p53 IHC positive in OS)
- **Fibroblastic** (~25%): spindled cells with minimal osteoid; worst histologic response to chemotherapy among conventional subtypes; overlaps morphologically with fibrosarcoma or MFH — osteoid required for diagnosis

**Low-grade OS:**
- **Parosteal OS** (low-grade, surface): posterior distal femur; densely mineralized; "cauliflower" exophytic; MDM2+/CDK4+ by FISH/IHC; 5-year OS ~90% after surgery alone (no chemotherapy needed)
- **Periosteal OS** (intermediate-grade): posterior tibia/femur; cartilage-predominant; limited chemotherapy use

**Other:**
- **Telangiectatic OS**: cystic spaces filled with blood; X-ray shows "blow-out" lesion; ~5% of OS; responds well to preoperative chemotherapy
- **Small cell OS**: SRBCT morphology; must exclude Ewing sarcoma (EWSR1 FISH negative; osteoid present)
- **Secondary OS**: Paget's, post-irradiation; poor prognosis; older patients; often polyostotic or axial

### Key radiographic features

- "Sunburst" periosteal reaction (perpendicular spicules of periosteal new bone)
- Codman triangle (periosteal elevation at tumor margin)
- Ill-defined permeative bone destruction on X-ray
- MRI: T1-hypointense, T2-heterogeneous; essential for marrow extent and skip lesions
- Staging: CT chest (lung mets), bone scan or FDG-PET (skip mets/distant bone mets)

## Function

### Normal osteoblast biology and OS origin

OS arises from uncommitted or committed osteoblast progenitors in the bone marrow stroma; the cell of origin is likely the **mesenchymal stem cell (MSC)** or an **osteoblast progenitor** that has lost RB1- and TP53-mediated checkpoints:

**Normal osteoblastogenesis:**
- MSC → pre-osteoblast (RUNX2+, SP7/Osterix+) → osteoblast (ALP+, osteocalcin+) → osteocyte
- RB1 enforces differentiation checkpoint: RB1-null osteoprogenitors fail to exit the cell cycle → accumulate genomic instability
- p53 enforces DNA damage response: TP53-null osteoprogenitors escape apoptosis after genotoxic stress → acquire further mutations
- Growth plates in adolescents have the highest osteoprogenitor proliferation rate → peak susceptibility to RB1/TP53 loss events → explains adolescent incidence peak

**IGF-1 signaling in OS:**
High IGF-1 levels during pubertal growth → IGF1R → PI3K/AKT + MEK/ERK → osteoprogenitor proliferation; OS cells overexpress IGF1R (~40%); anti-IGF1R antibodies (robatumumab, ganitumab) showed modest Phase 2 activity in recurrent OS; not yet standard.

## Pathology

### Molecular drivers

**Core tumor suppressors (co-lost in >80% high-grade OS):**
- **RB1 biallelic LOF** (~70-75%): deletion (13q14), frameshift, or nonsense mutations; loss of RB1 G1 checkpoint → E2F-driven osteoprogenitor hyperproliferation; RB1 loss is an early initiating event (shown in Rb1+/+ heterozygous mice with p53 loss)
- **TP53 mutations/deletions** (~30-40%): loss of DNA damage checkpoint; enables acquisition of complex chromosomal instability; TP53 LOF in pediatric OS often occurs via large chromosomal deletions (17p13)

**Alternative pathway activation (mutually exclusive events):**
- **MDM2 amplification** (~6-8%): functionally equivalent to TP53 mutation; co-amplified with CDK4 at 12q14-15 in a subset (especially dedifferentiated osteosarcoma, parosteal OS)
- **CDK4 amplification** (~6-8%): functionally equivalent to CDKN2A deletion; drives G1 bypass
- **CDKN2A homozygous deletion** (~20-30%): eliminates both p16 (→ CDK4/6 → RB1) and p14/ARF (→ MDM2 → p53)

**Secondary alterations:**
- **ATRX mutations** (~25%): alternative lengthening of telomeres (ALT pathway); associated with longer median OS survival in some series
- **DLG2 deletions** (~30%): postsynaptic density protein; mechanism of pro-tumorigenic effect unclear
- **WNT pathway**: CTNNB1 mutations (rare); DKK1 overexpression in OS stroma
- **PI3K/AKT/mTOR** pathway activation (~30-35%): PIK3CA mutations, PTEN loss, AKT amplification
- **VEGF/PDGFR** overexpression: correlates with metastatic phenotype; sorafenib, cabozantinib, regorafenib target these

**Chromosomal instability:**
OS karyotypes are typically highly complex (tens of structural rearrangements, chromothripsis events); unlike Ewing sarcoma or synovial sarcoma, OS has no single defining translocation; WGS reveals chromothripsis at chromosome 11, 12, and 17 in ~30-50% of OS; the extremely complex karyotype reflects the consequences of early RB1/TP53 loss allowing unchecked mitotic errors.

### Treatment

**Neoadjuvant MAP protocol (standard backbone):**
- **M** = high-dose methotrexate (HDMTX) 12 g/m²/cycle with leucovorin rescue; mechanism: DHFR inhibition → thymidylate depletion → DNA replication block
- **A** = doxorubicin 75 mg/m² (Adriamycin); intercalation → TOP2A inhibition → DSBs
- **P** = cisplatin 100-120 mg/m²/cycle; DNA intrastrand cross-links → apoptosis
- Standard cycle: 2 cycles MAP neoadjuvant → surgery → 4 cycles MAP adjuvant (total 6 cycles MAP over ~9-10 months); some protocols use 3 cycles neoadjuvant

**Histologic response (Huvos grading):**
- Grade I: <50% necrosis (poor)
- Grade II: 50-89% necrosis (partial response)
- Grade III: 90-99% necrosis (good response)
- Grade IV: 100% necrosis (complete pathologic response)
- **Good responder (≥90% necrosis)**: continue MAP adjuvant → 5-year EFS ~75-80%
- **Poor responder (<90% necrosis)**: historically, no benefit adding ifosfamide+etoposide (IE)

**EURAMOS-1 (Marina 2016):** [^marina-2016-euramos1-osteosarcoma] N=2,260 patients; largest prospective OS study; poor responders randomized to MAP vs MAP+IE: 3-year EFS 48% vs 47% (HR 0.98, 95% CI 0.77-1.25); no benefit to intensification with IE in poor responders; MAP remains standard for all risk groups; 5-year EFS for good responders 65%, poor responders 52%.

**COSS data (Bielack 2002):** [^bielack-2002-coss-osteosarcoma] Prognostic factors from 1,702 patients: poor response to chemotherapy, axial location, metastases at diagnosis, and elevated LDH are independent adverse prognostic factors.

**Limb-salvage surgery:**
- ~90% of OS patients can undergo limb-salvage surgery (endoprosthesis, allograft, rotationplasty)
- R0 resection required: wide surgical margin (≥2 cm preferred, or anatomical barrier)
- Local recurrence with R0: <5%; R1/R2 → high local recurrence risk
- Rotationplasty (Van Nes procedure): ankle-joint as neo-knee; functional outcomes comparable to endoprosthesis in very young children

**Radiation:**
OS is relatively radiation-resistant (high-dose radiation ~70+ Gy may achieve local control); primary RT reserved for unresectable lesions (skull base, spine); palliative RT for pain control; no role for adjuvant RT after R0 surgery.

**Relapsed/refractory OS:**
- Second-line chemotherapy: ifosfamide+etoposide (IE), gemcitabine+docetaxel (~20-25% ORR), carboplatin+etoposide
- Sorafenib (Phase 2, Grignani 2012): median OS 14 weeks vs 4 weeks historical control in relapsed OS; modest activity
- Regorafenib (REGOBONE trial, Duffaud 2019): ORR 5%, but PFS benefit (3.6 vs 1.7 months, HR 0.43, p=0.008) in relapsed OS
- Cabozantinib: MET/VEGFR/RET inhibitor; Phase 2 CABONE trial in bone sarcomas showing some PFS benefit
- Pulmonary metastasectomy: if lung mets are few and resectable, aggressive thoracotomy → 5-year OS ~25-35% in selected patients
- HDCT+auto-SCT: no proven benefit in OS (unlike Ewing sarcoma); not standard
- Immunotherapy: immune desert tumor (low TMB, immunosuppressive TME); PD-L1 variable; pembrolizumab single-agent ORR ~5% in unselected OS; dinutuximab (anti-GD2): GD2 expressed on ~40-60% OS → Phase 2 trials ongoing

**Emerging targets:**
- CDK4/6 inhibitors: MDM2/CDK4-co-amplified OS (parosteal) are sensitive; palbociclib Phase 2 (SARC033) for CDK4-amplified sarcomas
- MDM2 inhibitors (idasanutlin, milademetan): TP53-WT MDM2-amplified OS; dose-limiting thrombocytopenia managed with G-CSF
- WEE1 inhibitors (adavosertib): exploit replication stress in p53-deficient OS; Phase 2 ongoing
- mTOR inhibitors (ridaforolimus): activity in bone sarcomas; Phase 2 data modest; used in combination with PI3K inhibitors
- CAR-T cell therapy: GD2-directed, HER2-directed, B7-H3-directed CAR-T constructs in early Phase 1 trials

## Connections

- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion (~20-30% osteosarcoma) eliminates both p16 (→ CDK4/6 → RB1 inactivation) and ARF (→ MDM2 → p53 loss); CDK4 amplification (~6-8%) and CDKN2A deletion are mutually exclusive alternative Rb/p53 co-inactivation mechanisms in OS.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 biallelic inactivation in ~70-75% high-grade osteosarcoma via deletion, mutation, or methylation; RB1 LOF → E2F-driven proliferation → CCND1/CDK4 upregulation; germline RB1 (hereditary retinoblastoma) increases osteosarcoma risk ~1,000-fold.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations/deletions in ~30-40% high-grade osteosarcoma; MDM2 amplification is mutually exclusive with TP53 mutation as both de-repress MDM2 → p53 degradation; Li-Fraumeni syndrome (germline TP53) confers ~15-fold excess OS risk; TP53 loss predicts poor histologic response.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 amplification (~6-8% osteosarcoma, ~90% well-differentiated liposarcoma) functionally mimics ARF loss → rapid p53 ubiquitination; MDM2 amplification and TP53 mutation are mutually exclusive in OS; MDM2 inhibitors (idasanutlin) in trials for MDM2-amplified sarcomas.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Osteosarcoma arises from osteoblast progenitors that produce malignant osteoid — its diagnostic hallmark; loss of RB1 and TP53 checkpoints lets these RUNX2/Osterix-lineage cells proliferate, and the growth spurt's high osteoprogenitor turnover explains the adolescent peak.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Hereditary retinoblastoma (germline RB1 loss) is the prototypical osteosarcoma predisposition, raising OS risk ~500-1000-fold as the classic second malignancy — especially within prior radiation fields; this mirrors the somatic RB1 loss in ~70-75% of sporadic high-grade OS.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The pubertal IGF-1 surge drives osteoprogenitor proliferation via IGF1R → PI3K/AKT and MEK/ERK, helping explain why osteosarcoma peaks during the adolescent growth spurt at the fast-growing metaphyses of the distal femur and proximal tibia; ~40% of OS overexpress IGF1R.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Li-Fraumeni syndrome (germline TP53) is a major osteosarcoma predisposition, raising OS risk ~15-fold and making bone sarcoma a sentinel cancer; this mirrors the somatic TP53 loss in ~30-40% of sporadic high-grade OS, as p53 checkpoint failure is central to osteosarcoma biology.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Osteosarcoma is the most common primary bone cancer, arising at the fast-growing metaphyses of long bones — classically the distal femur and proximal tibia around the knee — in the adolescent growth spurt; it produces malignant osteoid and destroys bone, causing pain and a mass.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the dominant metastatic site in osteosarcoma: hematogenous spread seeds pulmonary nodules that determine prognosis, so chest CT staging is essential and surgical metastasectomy of lung lesions — even repeated — is part of curative-intent therapy with chemotherapy.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Osteosarcoma and Ewing sarcoma are the two commonest bone cancers of adolescence: osteosarcoma makes malignant osteoid and arises at the metaphysis of long bones, while Ewing is a small-round-blue-cell tumor driven by EWSR1-FLI1, often diaphyseal or in flat bones.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Osteosarcoma subverts bone remodeling: its malignant osteoblasts lay down disorganized osteoid and recruit osteoclasts that resorb bone, fueling growth—so bone-targeted agents like bisphosphonates, denosumab, and mifamurtide have been trialed against it.
- `connects-to` → **[Rothmund-Thomson Syndrome](../rothmund-thomson/README.md)** — Rothmund-Thomson syndrome is a hereditary cause of osteosarcoma: biallelic RECQL4 helicase loss yields poikiloderma, skeletal defects, and a markedly raised osteosarcoma risk—a DNA-repair syndrome that, with Li-Fraumeni and retinoblastoma, predisposes to it.
- `connects-to` → **[MPNST](../mpnst/README.md)** — Osteosarcoma and MPNST are both aggressive sarcomas that arise as radiation-induced second cancers: years after radiotherapy a high-grade sarcoma can emerge in the treated field, both resist chemotherapy—so a new mass in an irradiated bone or nerve raises alarm.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Osteosarcoma is the tumor that makes bone: its malignant osteoblasts deposit immature osteoid that mineralizes with calcium, producing the dense, disorganized 'sunburst' bone on imaging—calcified matrix distinguishes it from other bone sarcomas.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Osteosarcoma is relatively radioresistant, unlike Ewing sarcoma: photon radiotherapy gives poor local control, so wide surgical resection plus chemotherapy is the mainstay, with radiation reserved for unresectable or palliative cases.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Osteosarcoma is a malignant spindle-cell tumor making osteoid: its fibroblast-like mesenchymal cells produce immature bone matrix directly, distinguishing it from other sarcomas—so finding tumor cells laying down osteoid is the diagnostic hallmark on biopsy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis fuels osteosarcoma and predicts spread: the tumor secretes VEGF to vascularize and metastasize (chiefly to lung), high levels worsen prognosis, and anti-angiogenic kinase inhibitors are used in relapsed disease.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The PI3K/mTOR pathway is active in osteosarcoma: growth signaling through mTOR drives proliferation and survival, so mTOR inhibitors (often with other agents) are studied in this chemotherapy-resistant sarcoma where few targeted options exist.

[^bielack-2002-coss-osteosarcoma]: Bielack SS, Kempf-Bielack B, Delling G, et al. Prognostic factors in high-grade osteosarcoma of the extremities or trunk: an analysis of 1,702 patients treated on neoadjuvant Cooperative Osteosarcoma Study Group protocols. *J Clin Oncol.* 2002;20(3):776-790. [doi:10.1200/JCO.2002.20.3.776](https://doi.org/10.1200/JCO.2002.20.3.776) · [PubMed 11821461](https://pubmed.ncbi.nlm.nih.gov/11821461/)
[^marina-2016-euramos1-osteosarcoma]: Marina NM, Smeland S, Bielack SS, et al. Comparison of MAPIE versus MAP in patients with a poor response to preoperative chemotherapy for newly diagnosed high-grade osteosarcoma (EURAMOS-1). *Lancet Oncol.* 2016;17(10):1396-1408. [doi:10.1016/S1470-2045(16)30214-5](https://doi.org/10.1016/S1470-2045(16)30214-5) · [PubMed 27569442](https://pubmed.ncbi.nlm.nih.gov/27569442/)
