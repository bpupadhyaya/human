---
schema: human-scale-entry/v1
id: hnscc
name: HNSCC
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Head and neck SCC; HPV+ oropharyngeal HNSCC (TP53 WT, PI3K-active) has better prognosis than HPV-negative (TP53 ~80%, CDKN2A ~40%); cetuximab and pembrolizumab are approved; KEYNOTE-048 defines first-line pembrolizumab over EXTREME in PD-L1+ recurrent/metastatic disease."
aliases: ["HNSCC", "head and neck squamous cell carcinoma", "oral cavity cancer", "oropharyngeal cancer", "HPV-positive HNSCC", "laryngeal cancer", "hypopharyngeal cancer", "head and neck cancer"]
sources:
  - id: burtness-2019-keynote048
    type: peer-reviewed
    cite: "Burtness B, Harrington KJ, Greil R, et al. Pembrolizumab alone or with chemotherapy versus cetuximab with chemotherapy for recurrent or metastatic squamous cell carcinoma of the head and neck (KEYNOTE-048). Lancet. 2019;394(10212):1915-1928."
    doi: "10.1016/S0140-6736(19)32591-7"
    pmid: "31679945"
    url: "https://doi.org/10.1016/S0140-6736(19)32591-7"
  - id: vermorken-2008-extreme
    type: peer-reviewed
    cite: "Vermorken JB, Mesia R, Rivera F, et al. Platinum-based chemotherapy plus cetuximab in head and neck cancer. N Engl J Med. 2008;359(11):1116-1127."
    doi: "10.1056/NEJMoa0802656"
    pmid: "18784101"
    url: "https://doi.org/10.1056/NEJMoa0802656"
cross_links:
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR overexpression in ~90% of HNSCC (copy number gain, not mutation); cetuximab + cisplatin/5-FU (EXTREME) improved OS vs. chemo alone (10.1 vs. 7.4 months); cetuximab+radiation is definitive for locally advanced HNSCC in platinum-ineligible patients."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Pembrolizumab (KEYNOTE-048) improved OS vs. EXTREME in PD-L1 CPS≥20 (14.9 vs. 10.7 months) and CPS≥1 (13.6 vs. 10.4 months); pembrolizumab+chemotherapy improved OS for CPS≥1; nivolumab (CheckMate 141) improved OS vs. chemotherapy in platinum-refractory R/M HNSCC."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations in ~80% of HPV-negative HNSCC (UV and tobacco mutational signatures; R175H, R248W hotspots); HPV-positive HNSCC has WT TP53 (HPV E6 degrades p53 via E6AP ubiquitin ligase); TP53 mutation correlates with poor prognosis and cisplatin resistance in HNSCC."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutation/amplification in ~20-30% of HNSCC; especially HPV+ oropharyngeal HNSCC (HPV E7 → RB disruption → CDK activation; higher PI3K pathway activity); PI3K inhibitors (copanlisib, alpelisib) studied in HNSCC; AKT inhibitors in clinical trials."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Epstein-Barr virus — not HPV — drives nasopharyngeal carcinoma, a distinct head-and-neck SCC: >95% of endemic undifferentiated NPC is EBV+; EBER in-situ hybridization confirms it and plasma EBV DNA tracks tumor burden; pembrolizumab and nivolumab are active in recurrent EBV+ NPC."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "HPV16 E7 binds and inactivates RB1, releasing E2F to drive S-phase entry without mitogens — the RB arm of HPV oncogenesis that pairs with E6-mediated p53 degradation; because RB is disabled by protein, HPV+ HNSCC rarely carries RB1 or CDKN2A mutations."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A/p16 behaves oppositely by HPV status: deleted in ~40% of tobacco-driven HPV-negative HNSCC, but strongly overexpressed in HPV+ tumors (RB loss removes feedback), making p16 immunostaining the practical surrogate marker for HPV-positive oropharyngeal cancer."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Head and neck and esophageal squamous cell carcinomas are linked by field cancerization: chronic alcohol and tobacco mutagenizes the whole aerodigestive squamous mucosa, so HNSCC patients carry elevated risk of esophageal SCC — both TP53-driven, immunotherapy-responsive tumors."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "HNSCC and cervical cancer are united by HPV: high-risk HPV16 drives oropharyngeal HNSCC as it drives cervical cancer, E6 degrading p53 and E7 inactivating RB; HPV-positive oropharyngeal cancer has a better prognosis than tobacco-driven HNSCC, and the same vaccine prevents both."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "HNSCC is one of the more immunogenic solid tumors — heavy tobacco or viral mutational load generates neoantigens — so anti-PD-1 (pembrolizumab, nivolumab) reactivating cytotoxic CD8+ T cells extended survival in recurrent/metastatic disease (KEYNOTE-048, CheckMate 141)."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is a primary cause of head and neck squamous cell carcinoma: acetaldehyde is a direct mucosal carcinogen that synergizes strongly with tobacco to multiply oral, pharyngeal and laryngeal cancer risk—an etiology distinct from the HPV-driven oropharyngeal subset."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Tobacco smoke is the dominant cause of head and neck squamous cell carcinoma: its carbon-based polycyclic aromatic hydrocarbons and nitrosamines damage upper-aerodigestive mucosal DNA, producing field cancerization with multiple primaries, especially when combined with alcohol."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: connects-to
    note: "HPV-16 drives a distinct, rising subset of head and neck squamous cell carcinoma: the virus infects oropharyngeal (tonsil, base of tongue) crypt epithelium, its E6/E7 oncoproteins inactivating p53 and Rb; HPV-positive HNSCC affects younger non-smokers and has a better prognosis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is central to head and neck cancer: definitive chemoradiation can cure many HNSCCs (especially HPV-positive oropharyngeal tumors) and organ-preserve the larynx, while IMRT spares salivary glands—radiation is as pivotal here as surgery."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts shape head and neck cancer: HNSCC recruits and reprograms fibroblasts that secrete growth factors, remodel matrix and blunt immunity, promoting invasion and resistance—making the fibroblast-rich microenvironment a therapeutic target."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Head and neck cancer and thyroid cancer both arise in the neck but differ: HNSCC is a smoking/HPV-driven squamous carcinoma of the aerodigestive mucosa, while thyroid cancer is a usually indolent endocrine tumor—neck radiation, a thyroid-cancer risk factor, links them."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "HNSCC and lung cancer share tobacco field cancerization: the same carcinogen exposure mutates the entire aerodigestive lining, so head-and-neck cancer patients carry a high risk of synchronous or later lung cancer—warranting chest screening and smoking cessation."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages shape HNSCC: they infiltrate the tumor, suppress T-cell responses and promote invasion and angiogenesis, contributing to the immunosuppressive microenvironment that immune checkpoint inhibitors aim to reverse in recurrent disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven angiogenesis sustains HNSCC: these tumors secrete VEGF to build new vessels, high levels predict worse outcomes, and anti-angiogenic approaches are studied alongside the radiation, chemotherapy and EGFR-targeted therapy that anchor treatment."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations help immortalize head and neck cancer: reactivating telomerase lets HPV-negative, smoking-related HNSCC cells bypass the telomere limit on division, complementing TP53 loss—one of the genetic steps from chronic carcinogen exposure to cancer."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Head and neck cancer spreads first to cervical lymph nodes: the rich lymphatic drainage of the upper aerodigestive tract carries tumor to neck nodes early, so nodal status dominates staging and dictates whether the neck is treated surgically or with radiation."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "HNSCC is a checkpoint-immunotherapy-responsive cancer: carcinogen- and HPV-driven tumors carry neoantigens and immune infiltrate, so anti-PD-1 therapy (pembrolizumab, nivolumab) now treats recurrent and metastatic disease, sometimes as first-line care."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy refines head and neck radiation: its sharp dose stop spares salivary glands, swallowing muscles, and the spinal cord beside the tumor, so protons can cut the dry mouth and swallowing damage of conventional photon treatment."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells now prevent many head and neck cancers: the HPV vaccine elicits antibodies that block the oral HPV infection driving rising oropharyngeal SCC, so a B-cell-based vaccine is set to lower this cancer's incidence."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Head and neck cancer shares field cancerization with the lung: the same tobacco and alcohol carcinogens that mutate the airway lining cause both, so HNSCC patients face high rates of second primary lung cancers, prompting chest surveillance."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "HPV-negative head and neck cancers amplify cyclin D1: gain of CCND1 at 11q13, paired with p16/CDKN2A loss, throws the cell cycle into overdrive—a hallmark of the tobacco-and-alcohol-driven tumors that behave worse than HPV-positive ones."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Cetuximab fights head and neck cancer through NK cells: the anti-EGFR antibody not only blocks growth signaling but flags tumor cells for natural killer cells to destroy by antibody-dependent killing, adding an immune mechanism to a targeted drug."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Head and neck tumors silence immunity with regulatory T cells: Tregs accumulate in the tumor and suppress the cytotoxic response, part of the immune evasion that PD-1 blockade (pembrolizumab, nivolumab) tries to reverse in this cancer."
---

# HNSCC

## Overview

**Head and neck squamous cell carcinoma (HNSCC)** refers to SCC arising in the oral cavity, oropharynx, hypopharynx, larynx, and nasopharynx — a heterogeneous group of mucosal cancers unified by squamous histology and key oncogenic pathways (EGFR, TP53, CDKN2A, PIK3CA). HNSCC is globally common (~900,000 cases/year worldwide) and is etiologically divided into two biologically distinct groups: **HPV-positive oropharyngeal HNSCC** (driven by HPV16/18 E6/E7 oncoproteins targeting p53 and RB; rising incidence due to sexual transmission; favorable prognosis) and **HPV-negative HNSCC** (driven by tobacco and alcohol; TP53 mutations ~80%; worse prognosis). The systemic therapy landscape has been transformed by the KEYNOTE-048 trial demonstrating pembrolizumab superiority over the EXTREME regimen (cetuximab + platinum + 5-FU) for PD-L1-expressing recurrent/metastatic disease [^burtness-2019-keynote048].

**Epidemiology:**
- ~65,000 new cases/year in the US; ~14,000 deaths/year; 6th most common cancer worldwide
- HPV+ oropharyngeal SCC: Rising incidence (~70-80% of oropharyngeal HNSCC in the US); younger patients (~55 years), non-smokers, better prognosis
- HPV- HNSCC: Tobacco + alcohol; oral cavity, hypopharynx, larynx; older patients; worse outcomes
- 5-year overall survival: ~50-60% for locally advanced; ~30% for recurrent/metastatic

**Risk factors:**
- HPV infection (HPV16 most common): Oropharynx (tonsil, base of tongue); sexual transmission; vaccination (Gardasil 9) reduces risk
- Tobacco (cigarettes, smokeless tobacco): Risk proportional to pack-years; 5-10× increased risk
- Alcohol: Synergistic with tobacco (~15× combined vs. either alone)
- Betel quid chewing: Major risk factor in South and Southeast Asia (buccal/oral cavity SCC)
- Prior radiation: Secondary malignancy

## Structure

### Molecular subtypes

**HPV-positive oropharyngeal HNSCC:**
- HPV16 E6 → targets p53 via E6AP ubiquitin ligase → p53 degradation; HPV16 E7 → binds RB → releases E2F → cell cycle entry
- Molecular: PIK3CA mutation/amplification (~20-30%); FGFR3 alterations; minimal TP53 mutation (wild-type p53 degraded post-translationally)
- Immunological: High TIL density; PD-L1 high; HPV peptide neoantigens → immunogenic; responds to de-escalated therapy
- Prognosis: 5-year OS ~80% for locally advanced vs. ~45-50% for HPV-negative; used in treatment de-escalation trials (PATHOS, QUARTERBACK, De-ESCALaTE)

**HPV-negative HNSCC (oral cavity, larynx, hypopharynx):**
- TP53 mutations ~80%; CDKN2A (p16) deletion ~40% (tobacco signature); CCND1 amplification (~30%); EGFR amplification (~30%); MYC amplification
- High TMB but lower neoantigen immunogenicity than HPV+ (due to fewer frameshift mutations, no viral peptides)
- Tobacco-driven mutational signature (C→A transversions); alcohol → acetaldehyde → DNA adducts

**Genomic landscape (TCGA 2015):**
HNSCC molecular subtypes (4 clusters):
1. **Atypical:** TP53 WT, PIK3CA/HRAS mutation, often HPV+
2. **Classical:** EGFR amplification, CDKN2A loss, smoker-associated
3. **Basal:** EGFR overexpression, YAP1 amplification
4. **Mesenchymal:** Immune-rich, EMT markers, MET/AXL high

### Site-specific features

**Oral cavity (lip, tongue, floor of mouth, hard palate, buccal mucosa):**
- High tobacco/alcohol/betel; TP53 ~85%; CCND1 amplification; worst nodal spread pattern
- Surgery preferred for resectable disease; adjuvant chemoradiation for high-risk pathology (positive margins, perineural invasion, lymphovascular invasion, ≥2 LN, extranodal extension)

**Oropharynx (tonsil, soft palate, base of tongue, pharyngeal walls):**
- HPV+ increasingly common; p16 IHC as surrogate for HPV testing; p16+ = HPV+ in oropharynx (high sensitivity/specificity)
- Favorable prognosis → de-escalation trials testing reduced chemoradiation doses or radiation alone for early-stage HPV+ disease

**Larynx (supraglottic, glottic, subglottic):**
- Glottic SCC: Often early hoarseness → early diagnosis; favorable prognosis; voice preservation with radiotherapy
- Supraglottic SCC: Late presentation; poor prognosis; tobacco-driven
- Larynx preservation: Concurrent cisplatin + radiotherapy (VA Cooperative Study and RTOG 91-11) established as alternative to laryngectomy for organ preservation

**Hypopharynx:**
- Poorest prognosis of all HNSCC (late presentation, high nodal involvement); pyriform sinus most common

## Function

### HPV oncogenesis vs. tobacco/alcohol carcinogenesis

**HPV oncogenesis (HPV+ HNSCC):**
HPV16/18 infects basal cells of the oropharyngeal mucosa → viral episome (circular dsDNA) integrates into host genome → E6/E7 oncoproteins expressed:
- E6 + E6AP → p53 ubiquitination/degradation → impaired apoptosis and G1 checkpoint
- E7 → binds pRB LXCXE motif → RB inactivation → E2F release → S-phase entry even without mitogens
- E5: Promotes EGFR recycling → enhanced EGF signaling
Result: Immortalized basal cells with active PI3K/CDK4 and impaired DNA damage response → HNSCC initiation.

**Tobacco/alcohol carcinogenesis (HPV- HNSCC):**
Polycyclic aromatic hydrocarbons (PAH) in tobacco → carcinogen-DNA adducts → C→A transversions at TP53/CDKN2A; acetaldehyde (from alcohol) → N2-ethylidene-dG adducts → TP53 mutations; combined → 15× elevated HNSCC risk; accumulating TP53 mutations in field cancerization → synchronous/metachronous multiple primary tumors (field effect throughout entire aerodigestive tract).

## Pathology

### Staging and workup

**AJCC 8th edition (HPV+ and HPV- staged separately):**
HPV+ oropharyngeal: Node staging based on number (not laterality); HPV-negative staging follows standard pT/pN/pM.
- Most patients present with locally advanced stage III-IV (~60%)

**Staging workup:**
- CT with contrast (neck/chest/abdomen): Primary tumor and nodal assessment; distant staging
- FDG-PET/CT: Standard for N0 clinical staging (detect occult N+ disease); post-treatment assessment (12-16 weeks post-CRT) to determine need for planned neck dissection
- MRI: Preferred for soft tissue involvement (tongue base, skull base)
- HPV testing: p16 IHC in oropharynx (positive = CPS >70%, practically all oropharyngeal SCC p16+ are HPV+); HPV ISH or PCR for equivocal cases

### Treatment

**Locally advanced HNSCC (Stage III-IVB):**
- **Concurrent cisplatin (100 mg/m² q3w) + IMRT:** Standard of care for resectable/unresectable disease; cisplatin superior to carboplatin or cetuximab with radiation (TROG 02.02); 3-year locoregional control ~75%
- **Cetuximab + radiation (Bonner trial):** Inferior to cisplatin+RT in fit patients (RTOG 1016, De-ESCALaTE trials); reserved for cisplatin-ineligible patients; cisplatin+RT now preferred when feasible
- **Surgery ± adjuvant chemoradiation:** Resectable oral cavity and selected oropharynx tumors; adjuvant CRT for positive margins or extranodal extension (EORTC 22931/RTOG 9501 trials)
- **De-escalation (HPV+):** PATHOS, QUARTERBACK, NRG-HN002 trials studying reduced dose radiation (50-60 Gy vs. 70 Gy) in p16+/HPV+ oropharynx; not yet standard

**Recurrent/metastatic HNSCC (R/M HNSCC):**

**First-line:**
- **Pembrolizumab monotherapy (CPS≥1):** FDA approved for R/M HNSCC; OS 14.9 months (CPS≥20), 13.6 months (CPS≥1) — first-line standard for PD-L1+ disease [^burtness-2019-keynote048]
- **Pembrolizumab + platinum + 5-FU (CPS≥1):** OS benefit; preferred over EXTREME for PD-L1+ patients; ORR ~36%
- **EXTREME (cetuximab + cisplatin/carboplatin + 5-FU):** [^vermorken-2008-extreme] OS 10.1 vs. 7.4 months vs. chemo alone; FDA approved 2011; still used for CPS<1 patients where pembrolizumab alone is not recommended; 6 cycles then maintenance cetuximab

**Second-line and beyond:**
- **Nivolumab (CheckMate 141):** OS 7.5 vs. 5.1 months vs. chemotherapy in platinum-refractory R/M HNSCC; ORR 13%; FDA approved 2016; now largely used after pembrolizumab failure
- **Cetuximab monotherapy:** ORR ~13% in platinum-refractory disease; option for cetuximab-naive patients
- **Docetaxel, paclitaxel, methotrexate:** Palliative options in later lines

**Nasopharyngeal carcinoma (NPC — distinct from HNSCC):**
- EBV-associated (>95% of undifferentiated/non-keratinizing NPC in endemic regions)
- Cisplatin + radiation (NPC-specific protocols); induction chemotherapy with cisplatin+gemcitabine → CRT for locally advanced
- Pembrolizumab and nivolumab active in recurrent/metastatic EBV+ NPC

## Connections

- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR overexpression in ~90% of HNSCC (mainly copy number gain, not mutation); cetuximab (anti-EGFR mAb) + cisplatin/5-FU (EXTREME regimen) improved OS vs. chemo alone (10.1 vs. 7.4 months); cetuximab + radiation is definitive for locally advanced HNSCC in platinum-ineligible patients.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Pembrolizumab (KEYNOTE-048) improved OS vs. EXTREME in PD-L1 CPS≥20 (14.9 vs. 10.7 months) and CPS≥1 (13.6 vs. 10.4 months); pembrolizumab+chemotherapy improved OS for CPS≥1; nivolumab (CheckMate 141) improved OS vs. chemotherapy in platinum-refractory R/M HNSCC.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations in ~80% of HPV-negative HNSCC (UV and tobacco mutational signatures; R175H, R248W hotspots); HPV-positive HNSCC has WT TP53 (HPV E6 degrades p53 via E6AP ubiquitin ligase); TP53 mutation correlates with poor prognosis and cisplatin resistance in HNSCC.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutation/amplification in ~20-30% of HNSCC; especially HPV-positive oropharyngeal HNSCC (HPV E7 → retinoblastoma pathway disruption → CDK activation; HPV-positive HNSCC has higher PI3K pathway activation); PI3K inhibitors (copanlisib, alpelisib) studied in HNSCC; AKT inhibitors in clinical trials.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Epstein-Barr virus — not HPV — drives nasopharyngeal carcinoma, a distinct head-and-neck SCC: >95% of endemic undifferentiated NPC is EBV+; EBER in-situ hybridization confirms it and plasma EBV DNA tracks tumor burden; pembrolizumab and nivolumab are active in recurrent EBV+ NPC.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — HPV16 E7 binds and inactivates RB1, releasing E2F to drive S-phase entry without mitogens — the RB arm of HPV oncogenesis that pairs with E6-mediated p53 degradation; because RB is disabled by protein, HPV+ HNSCC rarely carries RB1 or CDKN2A mutations.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/p16 behaves oppositely by HPV status: deleted in ~40% of tobacco-driven HPV-negative HNSCC, but strongly overexpressed in HPV+ tumors (RB loss removes feedback), making p16 immunostaining the practical surrogate marker for HPV-positive oropharyngeal cancer.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Head and neck and esophageal squamous cell carcinomas are linked by field cancerization: chronic alcohol and tobacco mutagenizes the whole aerodigestive squamous mucosa, so HNSCC patients carry elevated risk of esophageal SCC — both TP53-driven, immunotherapy-responsive tumors.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — HNSCC and cervical cancer are united by HPV: high-risk HPV16 drives oropharyngeal HNSCC as it drives cervical cancer, E6 degrading p53 and E7 inactivating RB; HPV-positive oropharyngeal cancer has a better prognosis than tobacco-driven HNSCC, and the same vaccine prevents both.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — HNSCC is one of the more immunogenic solid tumors — heavy tobacco or viral mutational load generates neoantigens — so anti-PD-1 (pembrolizumab, nivolumab) reactivating cytotoxic CD8+ T cells extended survival in recurrent/metastatic disease (KEYNOTE-048, CheckMate 141).
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is a primary cause of head and neck squamous cell carcinoma: acetaldehyde is a direct mucosal carcinogen that synergizes strongly with tobacco to multiply oral, pharyngeal and laryngeal cancer risk—an etiology distinct from the HPV-driven oropharyngeal subset.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Tobacco smoke is the dominant cause of head and neck squamous cell carcinoma: its carbon-based polycyclic aromatic hydrocarbons and nitrosamines damage upper-aerodigestive mucosal DNA, producing field cancerization with multiple primaries, especially when combined with alcohol.
- `connects-to` → **[HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md)** — HPV-16 drives a distinct, rising subset of head and neck squamous cell carcinoma: the virus infects oropharyngeal (tonsil, base of tongue) crypt epithelium, its E6/E7 oncoproteins inactivating p53 and Rb; HPV-positive HNSCC affects younger non-smokers and has a better prognosis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is central to head and neck cancer: definitive chemoradiation can cure many HNSCCs (especially HPV-positive oropharyngeal tumors) and organ-preserve the larynx, while IMRT spares salivary glands—radiation is as pivotal here as surgery.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts shape head and neck cancer: HNSCC recruits and reprograms fibroblasts that secrete growth factors, remodel matrix and blunt immunity, promoting invasion and resistance—making the fibroblast-rich microenvironment a therapeutic target.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Head and neck cancer and thyroid cancer both arise in the neck but differ: HNSCC is a smoking/HPV-driven squamous carcinoma of the aerodigestive mucosa, while thyroid cancer is a usually indolent endocrine tumor—neck radiation, a thyroid-cancer risk factor, links them.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — HNSCC and lung cancer share tobacco field cancerization: the same carcinogen exposure mutates the entire aerodigestive lining, so head-and-neck cancer patients carry a high risk of synchronous or later lung cancer—warranting chest screening and smoking cessation.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages shape HNSCC: they infiltrate the tumor, suppress T-cell responses and promote invasion and angiogenesis, contributing to the immunosuppressive microenvironment that immune checkpoint inhibitors aim to reverse in recurrent disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis sustains HNSCC: these tumors secrete VEGF to build new vessels, high levels predict worse outcomes, and anti-angiogenic approaches are studied alongside the radiation, chemotherapy and EGFR-targeted therapy that anchor treatment.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations help immortalize head and neck cancer: reactivating telomerase lets HPV-negative, smoking-related HNSCC cells bypass the telomere limit on division, complementing TP53 loss—one of the genetic steps from chronic carcinogen exposure to cancer.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Head and neck cancer spreads first to cervical lymph nodes: the rich lymphatic drainage of the upper aerodigestive tract carries tumor to neck nodes early, so nodal status dominates staging and dictates whether the neck is treated surgically or with radiation.
- `connects-to` → **[Immune System](../immune-system/README.md)** — HNSCC is a checkpoint-immunotherapy-responsive cancer: carcinogen- and HPV-driven tumors carry neoantigens and immune infiltrate, so anti-PD-1 therapy (pembrolizumab, nivolumab) now treats recurrent and metastatic disease, sometimes as first-line care.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy refines head and neck radiation: its sharp dose stop spares salivary glands, swallowing muscles, and the spinal cord beside the tumor, so protons can cut the dry mouth and swallowing damage of conventional photon treatment.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells now prevent many head and neck cancers: the HPV vaccine elicits antibodies that block the oral HPV infection driving rising oropharyngeal SCC, so a B-cell-based vaccine is set to lower this cancer's incidence.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Head and neck cancer shares field cancerization with the lung: the same tobacco and alcohol carcinogens that mutate the airway lining cause both, so HNSCC patients face high rates of second primary lung cancers, prompting chest surveillance.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — HPV-negative head and neck cancers amplify cyclin D1: gain of CCND1 at 11q13, paired with p16/CDKN2A loss, throws the cell cycle into overdrive—a hallmark of the tobacco-and-alcohol-driven tumors that behave worse than HPV-positive ones.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Cetuximab fights head and neck cancer through NK cells: the anti-EGFR antibody not only blocks growth signaling but flags tumor cells for natural killer cells to destroy by antibody-dependent killing, adding an immune mechanism to a targeted drug.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Head and neck tumors silence immunity with regulatory T cells: Tregs accumulate in the tumor and suppress the cytotoxic response, part of the immune evasion that PD-1 blockade (pembrolizumab, nivolumab) tries to reverse in this cancer.

[^burtness-2019-keynote048]: Burtness B, Harrington KJ, Greil R, et al. Pembrolizumab alone or with chemotherapy versus cetuximab with chemotherapy for recurrent or metastatic squamous cell carcinoma of the head and neck (KEYNOTE-048). *Lancet.* 2019;394(10212):1915-1928. [doi:10.1016/S0140-6736(19)32591-7](https://doi.org/10.1016/S0140-6736(19)32591-7) · [PubMed 31679945](https://pubmed.ncbi.nlm.nih.gov/31679945/)
[^vermorken-2008-extreme]: Vermorken JB, Mesia R, Rivera F, et al. Platinum-based chemotherapy plus cetuximab in head and neck cancer. *N Engl J Med.* 2008;359(11):1116-1127. [doi:10.1056/NEJMoa0802656](https://doi.org/10.1056/NEJMoa0802656) · [PubMed 18784101](https://pubmed.ncbi.nlm.nih.gov/18784101/)
