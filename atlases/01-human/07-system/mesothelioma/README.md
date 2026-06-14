---
schema: human-scale-entry/v1
id: mesothelioma
name: Mesothelioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Malignant mesothelioma arises from pleural/peritoneal mesothelial cells; asbestos exposure causes ~80% with 30-50-year latency; BAP1 (~55%) and NF2 (~40%) loss define molecular subtypes. Nivolumab+ipilimumab (CheckMate 743: OS 18.1 vs 14.1 months) is first-line standard."
aliases: ["mesothelioma", "malignant pleural mesothelioma", "MPM", "peritoneal mesothelioma", "asbestos cancer", "epithelioid mesothelioma", "sarcomatoid mesothelioma", "biphasic mesothelioma", "Krenning mesothelioma"]
sources:
  - id: baas-2021-checkmate743
    type: peer-reviewed
    cite: "Baas P, Scherpereel A, Nowak AK, et al. First-line nivolumab plus ipilimumab in unresectable malignant pleural mesothelioma (CheckMate 743): a multicentre, randomised, open-label, phase 3 trial. Lancet. 2021;397(10272):375-386."
    doi: "10.1016/S0140-6736(20)32714-8"
    pmid: "33485464"
    url: "https://doi.org/10.1016/S0140-6736(20)32714-8"
  - id: vogelzang-2003-pemetrexed
    type: peer-reviewed
    cite: "Vogelzang NJ, Rusthoven JJ, Symanowski J, et al. Phase III study of pemetrexed in combination with cisplatin versus cisplatin alone in patients with malignant pleural mesothelioma. J Clin Oncol. 2003;21(14):2636-2644."
    doi: "10.1200/JCO.2003.11.136"
    pmid: "12860938"
    url: "https://doi.org/10.1200/JCO.2003.11.136"
cross_links:
  - target: 01-human/03-molecular/bap1
    relation: connects-to
    note: "BAP1 loss (~50-60% of mesothelioma) drives polycomb-mediated epigenetic reprogramming; BAP1 IHC nuclear loss aids mesothelioma diagnosis; epithelioid BAP1-mutant mesothelioma has better prognosis; germline BAP1 mutations → BAP1-TPDS (familial mesothelioma)."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Nivolumab + ipilimumab (CheckMate 743: OS 18.1 vs 14.1 months, HR 0.74, FDA 2021) is first-line for unresectable pleural mesothelioma; benefit most pronounced in sarcomatoid/biphasic subtypes (OS 18.1 vs 8.8 months); PD-L1 expression enriched in sarcomatoid."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Bevacizumab + cisplatin/pemetrexed (MAPS trial: OS 18.8 vs 16.1 months) is used in select European centers; VEGF overexpression is common in mesothelioma; ramucirumab (VEGFR2) under investigation; anti-VEGF + IO combinations in ongoing trials."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss in ~25% of peritoneal mesothelioma and ~10% of pleural; PI3K-AKT-mTOR activation downstream of PTEN loss → mTOR inhibitors studied in mesothelioma; PTEN-CDKN2A co-deletion confers aggressive phenotype; PTEN loss is more common in sarcomatoid subtype."
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "NF2/merlin loss occurs in ~40% of mesothelioma (enriched in the sarcomatoid subtype) → Hippo pathway off → YAP/TAZ nuclear → TEAD-driven proliferation; this makes NF2-null mesothelioma the lead indication for TEAD and FAK inhibitors now in early-phase trials."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pleural mesothelioma grows as a rind encasing the lung after asbestos fibers inhaled decades earlier lodge in the pleura; it presents with dyspnea and a large exudative effusion, and lung-sparing pleurectomy/decortication has largely replaced extrapleural pneumonectomy."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Asbestos drives mesothelioma partly through frustrated phagocytosis of long, biopersistent fibers by mesothelial cells and macrophages → ROS and NLRP3 inflammasome activation → IL-1β-driven chronic inflammation over 30-50 years → the mutagenic milieu that seeds malignancy."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Mesothelioma and meningioma share their central driver — NF2/merlin loss switching off Hippo so YAP/TAZ-TEAD drive proliferation (NF2-null in ~40% of mesothelioma, ~50-60% of meningioma) — why both spearhead trials of TEAD inhibitors despite arising in very different tissues."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Mesothelioma is moderately immunogenic, so dual checkpoint blockade — nivolumab plus ipilimumab, freeing cytotoxic CD8+ T cells — became first-line for unresectable pleural disease (CheckMate 743), with the largest benefit in the chemo-resistant sarcomatoid subtype."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "Mesothelioma and uveal melanoma are linked by BAP1: germline BAP1 loss causes the BAP1 tumor-predisposition syndrome, in which one family develops mesothelioma, uveal melanoma, renal cell carcinoma, and skin tumors — a shared chromatin defect across different organs."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Mesothelioma and renal cell carcinoma are both part of the BAP1 tumor predisposition syndrome: germline BAP1 loss predisposes to mesothelioma, clear-cell RCC, uveal melanoma and atypical melanocytic tumors, so mesothelioma with a family cancer history warrants BAP1 testing."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive asbestos-induced mesothelioma: long fibers resist 'frustrated' macrophage phagocytosis, so they release reactive oxygen species and activate the NLRP3 inflammasome—chronic IL-1β inflammation that transforms mesothelial cells over decades."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Mesothelioma and cholangiocarcinoma both occur in the BAP1 syndrome and share a chromatin-level driver: loss of BAP1, a nuclear deubiquitinase tumor suppressor, promotes both, and the epigenetic vulnerabilities plus checkpoint approaches are being explored across these cancers."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Mesothelioma and lung cancer are the great asbestos-related thoracic malignancies but distinct: mesothelioma arises from the pleural mesothelium, while NSCLC arises from bronchial/alveolar epithelium—asbestos drives both, but only lung cancer is strongly smoking-linked."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy's role in mesothelioma is limited: the tumor's diffuse rind over the pleura makes curative irradiation hard without harming lung, so photon radiation serves mainly palliation—surgery and chemo-immunotherapy carry the main burden."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Peritoneal mesothelioma and ovarian cancer overlap closely: both arise from or mimic serous peritoneal epithelium and may share BAP1 alterations, so a woman with peritoneal carcinomatosis needs pathology to separate mesothelioma from serous ovarian carcinoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion is a defining mesothelioma alteration: loss of this tumor suppressor, alongside BAP1 and NF2, drives the cancer and helps distinguish malignant mesothelioma from benign reactive mesothelial proliferation on biopsy—a key diagnostic marker."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The sarcomatoid subtype of mesothelioma is fibroblast-like and grim: spindle, fibroblast-resembling cells make a dense tumor far more resistant to therapy than the epithelioid type—so histologic subtype strongly predicts survival."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Mesothelioma is responsive to immunotherapy despite few mutations: chronic asbestos inflammation and an immune-rich microenvironment make checkpoint blockade (anti-PD-1/CTLA-4) a frontline option—so engaging the immune system has improved outcomes in this cancer."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Mesothelioma is the signature cancer of the respiratory system's lining: decades after asbestos inhalation, the pleura thickens with tumor that traps the lung in a rind, causing breathlessness and effusions—an almost wholly preventable, dismal-prognosis cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53-pathway disruption helps drive mesothelioma: although BAP1 and CDKN2A losses dominate, p53 inactivation contributes to the genomic chaos of asbestos-induced tumors, so the guardian-of-the-genome network features in this slow-developing malignancy."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-ion radiotherapy is explored for mesothelioma: its dense, sharply localized dose may help this radioresistant, diffusely spreading pleural tumor, complementing the surgery, chemotherapy and immunotherapy used against an asbestos-caused cancer."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Mesothelioma's immunotherapy pairs two checkpoints: combining anti-CTLA-4 (ipilimumab) with anti-PD-1 (nivolumab) became a first-line standard, extending survival in unresectable disease where chemotherapy alone had long stalled."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Asbestos scars the pleura before it causes cancer: dense pleural fibrosis and plaques mark exposure, and the desmoplastic variant of mesothelioma is so fibrous it can be mistaken for benign scarring—making biopsy interpretation difficult."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Asbestos kills mesothelial cells partly through iron: fibers adsorb iron and catalyze reactive oxygen species that damage DNA, and iron-coated 'ferruginous bodies' in tissue are the histologic fingerprint of the exposure that drives mesothelioma."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Mesothelioma is fundamentally a Hippo-pathway cancer acting through YAP1: NF2 and LATS losses release YAP1 to switch on growth genes, so this transcription co-activator is a central driver and a sought-after drug target in the disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Mesothelioma's cause is a magnesium-silicate mineral: asbestos fibers like chrysotile are magnesium silicates whose durable, needle-like shape lodges in the pleura and provokes the decades-long inflammation that seeds the cancer."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Mesothelioma defends itself with regulatory T cells: Tregs fill its immunosuppressive microenvironment and blunt anti-tumor immunity, which is why dual checkpoint blockade (nivolumab plus ipilimumab) is now frontline for the disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Mesothelioma can arise on the heart's lining: though most form on the pleura, the same asbestos-driven malignancy strikes the pericardium, where it encases the heart and impairs its filling—a rare but devastating site."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Mesothelioma hides in a hypoxic, fibrous tumor via HIF-1alpha: its dense desmoplastic stroma outstrips its oxygen supply, and the resulting HIF signaling drives survival and angiogenesis, part of why it resists chemotherapy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are enlisted to fight mesothelioma: because the tumor is poorly immunogenic, dendritic-cell vaccines and other antigen-presenting strategies aim to prime T-cell attack alongside the checkpoint drugs now used frontline."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Mesothelioma also strikes the belly: peritoneal mesothelioma coats the abdominal organs and bowel, including the large intestine, causing pain, ascites, and obstruction—the second most common form after pleural."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Mesothelioma recruits endothelial cells to grow: VEGF from the tumor drives these vessel-lining cells to build its blood supply, which is why anti-VEGF therapy is added to chemotherapy."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Mesothelioma steals the breath of oxygen: as it encases the lung and fills the chest with malignant effusion, it squeezes the lung shut, so worsening breathlessness and low oxygen dominate the illness."
---

# Mesothelioma

## Overview

**Malignant mesothelioma** is an aggressive cancer arising from the mesothelial cells lining the pleural cavities (~80%), peritoneum (~20%), pericardium (<1%), and tunica vaginalis testis (<1%). Mesothelioma is tightly linked to **asbestos exposure** (chrysotile and especially amphibole varieties — crocidolite, amosite, tremolite) in ~80% of cases, with a characteristic latency period of **30-50 years** between initial exposure and cancer diagnosis; workers in shipbuilding, construction, insulation, mining, and demolition are most affected. Despite its relative rarity (~3,000-4,000 new cases/year in the USA; declining with asbestos bans but still high in developing countries with ongoing asbestos use), mesothelioma carries a dismal prognosis — median OS of 12-18 months with current therapy. The landmark **CheckMate 743** trial established nivolumab + ipilimumab as the first-line immunotherapy regimen, improving OS over platinum/pemetrexed chemotherapy [^baas-2021-checkmate743]; cisplatin + pemetrexed remains the chemotherapy backbone [^vogelzang-2003-pemetrexed].

**Epidemiology:**
- USA: ~3,000-4,000 new cases/year; Australia, UK, Italy, Japan: Relatively high incidence from historic asbestos use; global incidence peaks expected 2020-2030 given latency from peak asbestos use in 1960s-1980s
- Asbestos fiber types: Chrysotile (white asbestos, ~90% of use) is less carcinogenic than amphiboles; crocidolite (blue asbestos) and amosite (brown asbestos) are most carcinogenic → fiber geometry (long, thin = biopersistent in lung and pleura); erionite (fibrous zeolite, Turkey) also causes mesothelioma
- **Germline BAP1 mutations (BAP1-TPDS):** Account for 1-2% of mesothelioma; BAP1-TPDS mesothelioma is often epithelioid, younger onset, longer survival; genetic counseling for young patients (<50) and those without asbestos history
- SV40 (simian virus 40): Controversial association; SV40 large T antigen found in ~50% of mesothelioma tumors in early studies; postulated co-carcinogen with asbestos; not consistently confirmed; SV40 T antigen binds RB1 and p53

**Molecular landscape:**
- **BAP1:** Loss in ~50-60% of pleural mesothelioma; predominantly epithelioid subtype; polycomb epigenetic driver
- **NF2 (merlin):** Loss in ~40%; Hippo pathway → YAP/TAZ nuclear translocation → pro-proliferative; sarcomatoid enriched
- **CDKN2A (p16/p14ARF) homozygous deletion:** ~70% of mesothelioma; chromosome 9p21 region; also deletes MTAP → MAT2A dependency; diagnostic marker by FISH
- **LATS2:** Hippo pathway kinase; mutations in ~20%; NF2-LATS2 pathway loss → YAP activation
- **TP53:** ~25%; less common than other solid tumors
- **PTEN:** ~25% peritoneal; ~10% pleural; PI3K-AKT activation
- **Rare targetable alterations:** NTRK fusions (~2%); MSI-H (<2%); NF2 → FAK inhibitor activity; MTAP deletion → MAT2A inhibitor (AG-270)

## Structure

### Histological subtypes and diagnostic approach

**Epithelioid mesothelioma (~50%):**
Cells: Polygonal, abundant cytoplasm, prominent nucleolus; architectural patterns: tubulopapillary, micropapillary, glandular, solid; nuclear grade (WHO 2021 3-tier grading: N1 monotonous, N2 moderate atypia, N3 pleomorphic) — grade predicts prognosis within epithelioid subtype. Best prognosis: mOS ~12-18 months; BAP1-loss epithelioid → slightly better immune infiltration → best IO response.

**Sarcomatoid mesothelioma (~20%):**
Cells: Spindle-shaped; minimal cytoplasm; destructive growth pattern; variants include desmoplastic mesothelioma (>50% storiform collagen stroma) and lymphohistiocytoid (rare). Most aggressive subtype: mOS ~5-7 months; frequent CDKN2A/NF2 alterations; CK7+/calretinin+ (but often focally); IHC can be challenging; PD-L1 high → IO most active in this subtype. Desmoplastic variant: Stromal response may mimic organizing pleuritis → requires CDKN2A FISH to confirm malignancy.

**Biphasic mesothelioma (~30%):**
Contains both epithelioid and sarcomatoid components (each ≥10%); prognosis intermediate (mOS ~10-15 months); IO benefit intermediate between subtypes.

**Immunohistochemistry panel:**
Positive markers (mesothelial lineage): Calretinin (nuclear+cytoplasmic, ~95% epithelioid, less in sarcomatoid), WT-1 (Wilms tumor protein, nuclear, ~90%), D2-40 (podoplanin, ~90%), CK5/6 (~80%), mesothelin (surface, ~90% epithelioid). Negative markers (to exclude adenocarcinoma): CEA (-), MOC31 (-), Ber-EP4 (-), TTF-1 (-), napsin-A (-). Note: SOX2 can be positive in mesothelioma vs. LUAD-negative pattern, but this is not standardized.

**BAP1 IHC + CDKN2A FISH (diagnostic algorithm):**
On small biopsies or effusion cell blocks: BAP1 nuclear loss (by IHC) OR CDKN2A homozygous deletion (by FISH) in a mesothelial proliferation = highly specific for malignancy (~90% specificity); combined: ~90-95% specificity. This allows diagnosis of malignant mesothelioma vs. reactive mesothelial hyperplasia without the need for surgical biopsy in selected cases.

### Staging

**AJCC 8th Edition (Pleural Mesothelioma):**
T1: Involves ipsilateral pleura only (visceral or parietal); T2: Invades diaphragm or lung parenchyma; T3: Locally advanced (involves chest wall, pericardium — resectable); T4: Unresectable (mediastinum, contralateral pleura, peritoneum, spine, brachial plexus). N1: Ipsilateral bronchopulmonary/hilar nodes; N2: Subcarinal/mediastinal nodes; N3: Contralateral or supraclavicular nodes. M1: Distant metastases. Most patients present with stage III-IV.

**Peritoneal mesothelioma staging:**
Peritoneal Cancer Index (PCI): Quantifies peritoneal disease extent (0-39); completeness of cytoreduction (CC0-CC3); PCI ≤20 with CC0/CC1 resection → HIPEC (hyperthermic intraperitoneal chemotherapy) consideration.

## Function

### Normal mesothelium physiology

Mesothelial cells form a single-layer lining of the pleural, pericardial, and peritoneal cavities, providing: frictionless surface via secretion of phosphatidylcholine-rich fluid; regulation of fluid transport (mesothelium expresses AQP1 aquaporin water channels and lymphatic drainage pores — stomata); inflammation modulation (mesothelial cells produce IL-8, MCP-1, TNF-α upon injury); fibrinolysis (mesothelium produces plasminogen activators → prevents fibrin adhesion after injury). After injury: submesothelial fibroblasts differentiate into new mesothelial cells via mesothelial-to-mesenchymal transition (MMT) — analogous to EMT in cancer; asbestos fibers trigger MMT, ROS generation, and NLRP3 inflammasome activation in mesothelial cells → chronic inflammation → carcinogenic mutagenesis.

## Pathology

### Diagnosis and clinical presentation

**Pleural mesothelioma presentation:**
- Dyspnea (from pleural effusion, most common initial symptom)
- Pleuritic or dull chest pain (encasement of lung, chest wall invasion)
- Pleural effusion: Often large, unilateral, exudative; pleural fluid cytology alone has ~30% sensitivity for malignant mesothelioma → surgical biopsy (VATS/thoracoscopy) or CT-guided biopsy preferred; pleural fluid is exudative, often serosanguineous, with low glucose and high LDH
- Constitutional symptoms: Weight loss, fatigue (especially sarcomatoid subtype)
- SVC syndrome, Horner's syndrome: Late (mediastinal invasion)

**Peritoneal mesothelioma presentation:**
- Abdominal pain, distension, ascites
- Omental cake and peritoneal nodules on CT
- Serum CA-125 elevated; misdiagnosed as ovarian peritoneal carcinoma → calretinin/WT-1 IHC and mesothelin serology distinguish

**Imaging:**
- Chest CT: Unilateral pleural thickening ± effusion; rind-like pleural thickening encasing lung (sheet-like mesothelioma); pleural plaques (asbestos-related but non-malignant); lymph nodes; mediastinal involvement
- PET/CT: Pleural uptake; mediastinal/diaphragmatic extension; peritoneal spread; FDG-avid especially sarcomatoid
- MRI chest: Diaphragm and chest wall invasion assessment (T3/T4 distinction); better soft-tissue contrast than CT

**Diagnosis:**
- Surgical biopsy (VATS thoracoscopy) preferred over CT-guided to obtain adequate tissue for IHC + FISH; VATS allows direct visualization + macroscopic assessment
- Biomarkers: Serum mesothelin (SMR, N-ERC mesothelin): Elevated in ~80% of pleural mesothelioma; sensitivity ~60-70%, specificity ~90%; useful for monitoring but not for screening; Mesomark and MESOMARK assay
- Molecular testing: BAP1 IHC, CDKN2A FISH, next-gen sequencing panel (NF2, BAP1, CDKN2A, TP53, LATS2, PTEN); germline BAP1 testing if clinical criteria met

### Systemic treatment

**First-line (unresectable MPM):**

**Nivolumab + Ipilimumab (CheckMate 743, FDA 2021):** [^baas-2021-checkmate743]
- 605 patients unresectable treatment-naive MPM; nivolumab 3 mg/kg q2w + ipilimumab 1 mg/kg q6w vs. cisplatin/carboplatin + pemetrexed × 6 cycles
- OS 18.1 vs 14.1 months overall (HR 0.74, p=0.002); benefit most pronounced in non-epithelioid (sarcomatoid/biphasic: OS 18.1 vs 8.8 months, HR 0.46); epithelioid: OS 18.7 vs 16.3 months (modest, HR 0.85, NS for epithelioid alone)
- NCCN Category 1 preferred first-line; irAE profile: rash, colitis, hepatitis, endocrinopathies

**Cisplatin + Pemetrexed (+ folic acid/B12 supplementation, FDA 2004):** [^vogelzang-2003-pemetrexed]
- 456 patients; cisplatin/pemetrexed vs. cisplatin alone: OS 12.1 vs 9.3 months; ORR 41.3% vs 16.7%; established as chemotherapy backbone for mesothelioma
- Carboplatin (AUC 5) may substitute cisplatin; pemetrexed 500 mg/m² q21d; B12 and folic acid supplementation mandatory (reduces pemetrexed toxicity)
- Bevacizumab option: MAPS trial (France): Cisplatin/pemetrexed + bevacizumab: OS 18.8 vs 16.1 months; not FDA-approved for mesothelioma in USA; used in EU in cisplatin-eligible patients

**Second-line:**
- **Ramucirumab (VEGFR2) + gemcitabine:** RAMES trial: OS benefit vs. gemcitabine alone; European guideline recommendation
- **Vinorelbine:** OS 9.9 months in 2nd-line; single-agent; well-tolerated
- **Gemcitabine ± cisplatin:** Modest activity; ORR ~10-15%
- **Lurbinectedin:** Investigational for 2nd-line; ongoing Phase 2
- **Pembrolizumab:** KEYNOTE-158: Modest activity; PD-L1 ≥1% enriched for response; ORR ~18%; 3rd-line option
- **Nivolumab monotherapy:** ORR ~18-24% in 2nd+ line (IFCT-1501); option post-chemotherapy first-line

**Peritoneal mesothelioma:**
Cytoreductive surgery (CRS) + hyperthermic intraperitoneal chemotherapy (HIPEC): Standard for eligible patients (PCI ≤20, good performance status, epithelioid); 5-year OS ~50% after CRS+HIPEC vs. <15% for systemic chemotherapy alone; cisplatin-based HIPEC at 42°C × 90 minutes.

**Surgery for pleural mesothelioma:**
- **EPP (extrapleural pneumonectomy):** Removes lung, pleura, ipsilateral diaphragm, pericardium; MARS trial (2011): No survival benefit over palliative chemotherapy → largely abandoned; associated with high morbidity (5-10% operative mortality)
- **P/D (pleurectomy/decortication):** Lung-sparing pleura removal; less morbidity; MARS-2 trial: P/D + chemo vs. chemo alone → preliminary results suggest no survival benefit; NCCN: Surgery only in highly selected LS-SCLC patients at expert centers
- **Radiation:** Hemithoracic radiation post-EPP (to prevent seeding); palliative radiation for chest wall pain, SVC syndrome

**Emerging targets:**
- **MAT2A inhibitors (MTAP-deleted):** CDKN2A deletion (9p21) co-deletes MTAP in ~70% of mesothelioma → MAT2A synthetic lethality → AG-270 (Phase 1/2, PRISM study); promising early signals
- **Tazemetostat (EZH2 inhibitor):** BAP1 loss → EZH2 dependency; CELLO-2 Phase 2 for BAP1-null pleural mesothelioma ongoing
- **Mesothelin ADC (BMS-986148):** Anetumab ravtansine Phase 2; ORR ~20%; DM4-maytansine payload; mesothelin surface expression enables targeting
- **NTRK fusions:** Larotrectinib/entrectinib for rare NTRK+ mesothelioma (tumor-agnostic)

## Connections

- `connects-to` → **[BAP1](../../03-molecular/bap1/README.md)** — BAP1 loss (~50-60% of mesothelioma) drives polycomb-mediated epigenetic reprogramming; BAP1 IHC nuclear loss aids mesothelioma diagnosis; epithelioid BAP1-mutant mesothelioma has better prognosis; germline BAP1 mutations → BAP1-TPDS (familial mesothelioma).
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Nivolumab + ipilimumab (CheckMate 743: OS 18.1 vs 14.1 months, HR 0.74, FDA 2021) is first-line for unresectable pleural mesothelioma; benefit most pronounced in sarcomatoid/biphasic subtypes (OS 18.1 vs 8.8 months); PD-L1 expression enriched in sarcomatoid.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Bevacizumab + cisplatin/pemetrexed (MAPS trial: OS 18.8 vs 16.1 months) is used in select European centers; VEGF overexpression is common in mesothelioma; ramucirumab (VEGFR2) under investigation; anti-VEGF + IO combinations in ongoing trials.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss in ~25% of peritoneal mesothelioma and ~10% of pleural; PI3K-AKT-mTOR activation downstream of PTEN loss → mTOR inhibitors studied in mesothelioma; PTEN-CDKN2A co-deletion confers aggressive phenotype; PTEN loss is more common in sarcomatoid subtype.
- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — NF2/merlin loss occurs in ~40% of mesothelioma (enriched in the sarcomatoid subtype) → Hippo pathway off → YAP/TAZ nuclear → TEAD-driven proliferation; this makes NF2-null mesothelioma the lead indication for TEAD and FAK inhibitors now in early-phase trials.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pleural mesothelioma grows as a rind encasing the lung after asbestos fibers inhaled decades earlier lodge in the pleura; it presents with dyspnea and a large exudative effusion, and lung-sparing pleurectomy/decortication has largely replaced extrapleural pneumonectomy.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Asbestos drives mesothelioma partly through frustrated phagocytosis of long, biopersistent fibers by mesothelial cells and macrophages → ROS and NLRP3 inflammasome activation → IL-1β-driven chronic inflammation over 30-50 years → the mutagenic milieu that seeds malignancy.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Mesothelioma and meningioma share their central driver — NF2/merlin loss switching off Hippo so YAP/TAZ-TEAD drive proliferation (NF2-null in ~40% of mesothelioma, ~50-60% of meningioma) — why both spearhead trials of TEAD inhibitors despite arising in very different tissues.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Mesothelioma is moderately immunogenic, so dual checkpoint blockade — nivolumab plus ipilimumab, freeing cytotoxic CD8+ T cells — became first-line for unresectable pleural disease (CheckMate 743), with the largest benefit in the chemo-resistant sarcomatoid subtype.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — Mesothelioma and uveal melanoma are linked by BAP1: germline BAP1 loss causes the BAP1 tumor-predisposition syndrome, in which one family develops mesothelioma, uveal melanoma, renal cell carcinoma, and skin tumors — a shared chromatin defect across different organs.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Mesothelioma and renal cell carcinoma are both part of the BAP1 tumor predisposition syndrome: germline BAP1 loss predisposes to mesothelioma, clear-cell RCC, uveal melanoma and atypical melanocytic tumors, so mesothelioma with a family cancer history warrants BAP1 testing.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive asbestos-induced mesothelioma: long fibers resist 'frustrated' macrophage phagocytosis, so they release reactive oxygen species and activate the NLRP3 inflammasome—chronic IL-1β inflammation that transforms mesothelial cells over decades.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Mesothelioma and cholangiocarcinoma both occur in the BAP1 syndrome and share a chromatin-level driver: loss of BAP1, a nuclear deubiquitinase tumor suppressor, promotes both, and the epigenetic vulnerabilities plus checkpoint approaches are being explored across these cancers.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Mesothelioma and lung cancer are the great asbestos-related thoracic malignancies but distinct: mesothelioma arises from the pleural mesothelium, while NSCLC arises from bronchial/alveolar epithelium—asbestos drives both, but only lung cancer is strongly smoking-linked.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy's role in mesothelioma is limited: the tumor's diffuse rind over the pleura makes curative irradiation hard without harming lung, so photon radiation serves mainly palliation—surgery and chemo-immunotherapy carry the main burden.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Peritoneal mesothelioma and ovarian cancer overlap closely: both arise from or mimic serous peritoneal epithelium and may share BAP1 alterations, so a woman with peritoneal carcinomatosis needs pathology to separate mesothelioma from serous ovarian carcinoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion is a defining mesothelioma alteration: loss of this tumor suppressor, alongside BAP1 and NF2, drives the cancer and helps distinguish malignant mesothelioma from benign reactive mesothelial proliferation on biopsy—a key diagnostic marker.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The sarcomatoid subtype of mesothelioma is fibroblast-like and grim: spindle, fibroblast-resembling cells make a dense tumor far more resistant to therapy than the epithelioid type—so histologic subtype strongly predicts survival.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Mesothelioma is responsive to immunotherapy despite few mutations: chronic asbestos inflammation and an immune-rich microenvironment make checkpoint blockade (anti-PD-1/CTLA-4) a frontline option—so engaging the immune system has improved outcomes in this cancer.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Mesothelioma is the signature cancer of the respiratory system's lining: decades after asbestos inhalation, the pleura thickens with tumor that traps the lung in a rind, causing breathlessness and effusions—an almost wholly preventable, dismal-prognosis cancer.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — p53-pathway disruption helps drive mesothelioma: although BAP1 and CDKN2A losses dominate, p53 inactivation contributes to the genomic chaos of asbestos-induced tumors, so the guardian-of-the-genome network features in this slow-developing malignancy.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-ion radiotherapy is explored for mesothelioma: its dense, sharply localized dose may help this radioresistant, diffusely spreading pleural tumor, complementing the surgery, chemotherapy and immunotherapy used against an asbestos-caused cancer.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Mesothelioma's immunotherapy pairs two checkpoints: combining anti-CTLA-4 (ipilimumab) with anti-PD-1 (nivolumab) became a first-line standard, extending survival in unresectable disease where chemotherapy alone had long stalled.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Asbestos scars the pleura before it causes cancer: dense pleural fibrosis and plaques mark exposure, and the desmoplastic variant of mesothelioma is so fibrous it can be mistaken for benign scarring—making biopsy interpretation difficult.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Asbestos kills mesothelial cells partly through iron: fibers adsorb iron and catalyze reactive oxygen species that damage DNA, and iron-coated 'ferruginous bodies' in tissue are the histologic fingerprint of the exposure that drives mesothelioma.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Mesothelioma is fundamentally a Hippo-pathway cancer acting through YAP1: NF2 and LATS losses release YAP1 to switch on growth genes, so this transcription co-activator is a central driver and a sought-after drug target in the disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Mesothelioma's cause is a magnesium-silicate mineral: asbestos fibers like chrysotile are magnesium silicates whose durable, needle-like shape lodges in the pleura and provokes the decades-long inflammation that seeds the cancer.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Mesothelioma defends itself with regulatory T cells: Tregs fill its immunosuppressive microenvironment and blunt anti-tumor immunity, which is why dual checkpoint blockade (nivolumab plus ipilimumab) is now frontline for the disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Mesothelioma can arise on the heart's lining: though most form on the pleura, the same asbestos-driven malignancy strikes the pericardium, where it encases the heart and impairs its filling—a rare but devastating site.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Mesothelioma hides in a hypoxic, fibrous tumor via HIF-1alpha: its dense desmoplastic stroma outstrips its oxygen supply, and the resulting HIF signaling drives survival and angiogenesis, part of why it resists chemotherapy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are enlisted to fight mesothelioma: because the tumor is poorly immunogenic, dendritic-cell vaccines and other antigen-presenting strategies aim to prime T-cell attack alongside the checkpoint drugs now used frontline.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Mesothelioma also strikes the belly: peritoneal mesothelioma coats the abdominal organs and bowel, including the large intestine, causing pain, ascites, and obstruction—the second most common form after pleural.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Mesothelioma recruits endothelial cells to grow: VEGF from the tumor drives these vessel-lining cells to build its blood supply, which is why anti-VEGF therapy is added to chemotherapy.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Mesothelioma steals the breath of oxygen: as it encases the lung and fills the chest with malignant effusion, it squeezes the lung shut, so worsening breathlessness and low oxygen dominate the illness.

[^baas-2021-checkmate743]: Baas P, Scherpereel A, Nowak AK, et al. First-line nivolumab plus ipilimumab in unresectable malignant pleural mesothelioma (CheckMate 743). *Lancet.* 2021;397(10272):375-386. [doi:10.1016/S0140-6736(20)32714-8](https://doi.org/10.1016/S0140-6736(20)32714-8) · [PubMed 33485464](https://pubmed.ncbi.nlm.nih.gov/33485464/)
[^vogelzang-2003-pemetrexed]: Vogelzang NJ, Rusthoven JJ, Symanowski J, et al. Phase III study of pemetrexed in combination with cisplatin versus cisplatin alone in patients with malignant pleural mesothelioma. *J Clin Oncol.* 2003;21(14):2636-2644. [doi:10.1200/JCO.2003.11.136](https://doi.org/10.1200/JCO.2003.11.136) · [PubMed 12860938](https://pubmed.ncbi.nlm.nih.gov/12860938/)
