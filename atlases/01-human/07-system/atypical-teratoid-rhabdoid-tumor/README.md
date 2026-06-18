---
schema: human-scale-entry/v1
id: atypical-teratoid-rhabdoid-tumor
name: Atypical Teratoid/Rhabdoid Tumor
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "AT/RT (atypical teratoid/rhabdoid tumor) is an aggressive CNS WHO grade 4 pediatric tumor defined by SMARCB1 biallelic LOF (~95%) or SMARCA4 LOF (~5%); peak <3 years; three molecular subgroups (TYR, SHH, MYC); multimodal therapy; 2-year OS ~40-50%; germline SMARCB1 → RTPS1."
aliases: ["AT/RT", "atypical teratoid rhabdoid tumor", "ATRT", "rhabdoid tumor brain", "INI1-deficient CNS tumor", "SMARCB1 brain tumor", "SMARCB1-deficient tumor", "pediatric CNS rhabdoid", "rhabdoid tumor predisposition"]
sources:
  - id: biegel-1999-ini1-atrt
    type: peer-reviewed
    cite: "Biegel JA, Zhou JY, Rorke LB, Stenstrom C, Wainwright LM, Fogelgren B. Germ-line and acquired mutations of INI1 in atypical teratoid and rhabdoid tumors. Cancer Res. 1999;59(1):74-79."
    doi: "10.1158/0008-5472.CAN-58-1-74"
    pmid: "9892189"
    url: "https://pubmed.ncbi.nlm.nih.gov/9892189/"
  - id: fruhwald-2020-atrt-subgroups
    type: peer-reviewed
    cite: "Frühwald MC, Hasselblatt M, Nemes K, et al. Age and DNA methylation subgroup as potential treatment targets in children with atypical teratoid rhabdoid tumors. Neuro Oncol. 2020;22(7):1006-1017."
    doi: "10.1093/neuonc/noz244"
    pmid: "31900478"
    url: "https://doi.org/10.1093/neuonc/noz244"
cross_links:
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SMARCB1 biallelic LOF defines AT/RT (~95% of cases); INI1 IHC (loss of nuclear staining) is the diagnostic standard; germline SMARCB1 → RTPS1 with multi-focal rhabdoid tumors at birth; SMARCA4-mutant AT/RT (~5%) is clinically similar."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "SMARCB1 LOF → PRC2/EZH2 unrestricted → H3K27me3 at BAF-target loci (CDKN2A, HOX, differentiation genes); AT/RT cells are EZH2-dependent; tazemetostat reduces H3K27me3 and restores differentiation markers; AT/RT EZH2 inhibition is in clinical trials."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "AT/RT-MYC subgroup (~30%): MYC overexpression via BRD4-occupied super-enhancers (SMARCB1 loss → BRD4 unrestricted); supratentorial, older patients; BET inhibitors (JQ1) suppress MYC in AT/RT-MYC cells; ONC201 (DRD2 antagonist) investigated in AT/RT."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations are absent in most AT/RT; SMARCB1 loss → ARF epigenetically silenced → MDM2 unrestricted → p53 degraded without TP53 mutation; p53 suppression via ARF silencing (not TP53 mutation) is the primary p53-pathway inactivation mechanism in SMARCB1-null rhabdoid tumors."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "SMARCB1 LOF epigenetically silences ARF (CDKN2A p14) → MDM2 unrestricted → p53 degradation without TP53 mutation; CDKN2A homozygous deletion (~15-25% of AT/RT) adds permanent G1 bypass; CDKN2A deletion correlates with AT/RT-TYR and worst OS among molecular subgroups."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "AT/RT is predominantly a CNS tumor; infratentorial (cerebellum, brainstem) in ~50-60%; the most common malignant brain tumor in infants <1 year; leptomeningeal dissemination in ~30-40%; proton CSI preferred in eligible patients to reduce long-term neurocognitive injury."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "AT/RT and medulloblastoma are the two most common pediatric malignant posterior fossa tumors; INI1 IHC loss (AT/RT) vs. intact INI1 (MB) is the key differentiator; SMARCB1 LOF never seen in MB; misdiagnosis as MB is a known pitfall; methylation profiling resolves ambiguous cases."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "AT/RT and synovial sarcoma are united by SWI/SNF (BAF) disruption and EZH2 dependence: AT/RT deletes SMARCB1 outright, while SS18-SSX fusion evicts SMARCB1 from BAF — both unleash PRC2/EZH2, so the EZH2 inhibitor tazemetostat is active in each despite different ages and sites."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "AT/RT has a renal twin: malignant rhabdoid tumor of the kidney shares the same biallelic SMARCB1 (INI1) loss and rhabdoid morphology, and germline SMARCB1 (rhabdoid predisposition) causes synchronous brain AT/RT and renal rhabdoid tumors in infants — one disease across organs."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "SMARCB1 links AT/RT and schwannomatosis at opposite doses: biallelic SMARCB1 loss in a child causes aggressive AT/RT, while a germline single-allele SMARCB1 variant causes schwannomatosis — multiple benign schwannomas in adults — same gene, very different tumors."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "ATRT and malignant rhabdoid tumor of the kidney are the same SMARCB1-driven cancer in different sites: loss of the SWI/SNF subunit SMARCB1 (INI1) produces rhabdoid tumors in brain (ATRT) or kidney, so both belong to the rhabdoid tumor predisposition syndrome and resemble Wilms."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "ATRT and rhabdomyosarcoma both feature rhabdoid/small-round-blue-cell morphology and must be distinguished molecularly: ATRT is defined by SMARCB1 (INI1) loss while rhabdomyosarcoma shows myogenic markers and PAX-FOXO1 fusions—a distinction that dictates very different therapy."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "ATRT and diffuse midline glioma are both aggressive pediatric brain tumors driven by epigenetic dysregulation: ATRT by SMARCB1/SWI-SNF loss, DMG by the H3 K27M histone mutation—both reprogram chromatin rather than relying on classic oncogenes, and both carry a grim prognosis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is central but fraught in atypical teratoid/rhabdoid tumor: this aggressive infant brain tumor needs craniospinal photon or proton irradiation, but radiation is especially neurotoxic to the very young brain—so proton beam and timing limit lifelong damage."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "ATRT and neuroblastoma are both aggressive embryonal tumors of infancy with small-round-blue-cell histology: ATRT is a SMARCB1-deficient CNS/renal rhabdoid tumor, while neuroblastoma is a sympathoadrenal MYCN-driven tumor—told apart by INI1 loss and site."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "ATRT and retinoblastoma are aggressive embryonal cancers of early childhood driven by loss of a single tumor suppressor—SMARCB1 in ATRT versus RB1 in retinoblastoma—and like trilateral retinoblastoma, ATRT can arise in the pineal region of an infant brain."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "ATRT arises in the neuron-rich central nervous system: this aggressive infant tumor forms brain masses that compress and infiltrate neural tissue, causing the hydrocephalus and deficits that bring it to attention—though its cells are rhabdoid, not neuronal."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "ATRT must be distinguished from astrocyte-derived tumors: unlike gliomas that arise from astrocytes, ATRT is an embryonal rhabdoid tumor defined by SMARCB1 loss, so molecular testing—not histology alone—separates it from the astrocytomas it can mimic on imaging."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "ATRT and glioblastoma are both highly aggressive brain tumors but at opposite ages and origins: ATRT strikes infants via SWI/SNF (SMARCB1) loss, while glioblastoma is an adult glial tumor—yet both share dismal prognosis and therapy resistance."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Immunotherapy is being explored in ATRT: despite a low mutation burden, SMARCB1 loss can make these tumors immunogenic, so PD-1 checkpoint blockade is under study for a cancer that resists conventional therapy and devastates infants."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "ATRT is a highly aggressive embryonal tumor of the central nervous system: it arises in the brain (often the cerebellum) of very young children, so it presents with raised intracranial pressure and rapid neurological decline—among the most lethal pediatric CNS cancers."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "ATRT and Li-Fraumeni syndrome both stem from tumor-suppressor loss but differ in gene: ATRT is driven by biallelic SMARCB1 (a chromatin-remodeler) loss, while Li-Fraumeni is germline TP53—two routes by which a single gene defect unleashes childhood cancer."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "ATRT shows actionable pathway activation including mTOR: loss of SMARCB1 deregulates signaling that converges on mTOR and aurora kinase, so targeted inhibitors are being tested to add precision options to this aggressive infant brain tumor's harsh chemoradiation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunotherapy is being explored in ATRT via cytotoxic T cells: despite few mutations, some ATRTs carry immune infiltrate, so checkpoint blockade and T-cell approaches are studied for a tumor where conventional treatment often fails in the very young."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "ATRT cells may depend on autophagy to survive: SWI/SNF loss and metabolic stress make these tumors lean on autophagic recycling, so blocking autophagy is studied as a vulnerability in a cancer that resists standard treatment."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ATRT is a SWI/SNF disease beyond SMARCB1: ARID1A is another subunit of the same chromatin-remodeling complex, so the rhabdoid tumor's defining loss of SMARCB1 sits in a pathway where ARID1A mutations cause related epigenetically-driven cancers."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "ATRT recruits the brain's own microglia: these resident immune cells infiltrate the tumor and are often co-opted into a tumor-supporting state, shaping the immune microenvironment of this aggressive infant brain cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "SMARCB1 loss makes ATRT a target for NK cells: rhabdoid tumors lacking SMARCB1 can downregulate MHC and upregulate stress ligands, and NK-cell-based immunotherapy is explored against these poorly immunogenic tumors."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Losing SMARCB1 makes ATRT lean on CDK4/6: the chromatin defect derepresses cyclin D and drives the cell-cycle kinase, so CDK4/6 inhibitors are being tested to exploit this dependency in a cancer with few other targets."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are being enlisted against ATRT: because these rhabdoid tumors are poorly immunogenic, dendritic-cell vaccines and other strategies to present tumor antigens aim to spark a T-cell attack on residual disease."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "ATRT arises in the developing brain among glial precursors: its rhabdoid cells can show divergent differentiation toward neural and glial lines including oligodendrocyte features, reflecting the primitive cell of origin in infants."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "ATRT outgrows its oxygen: this fast, aggressive infant tumor turns hypoxic at its core, switching on the HIF/VEGF program that sprouts new vessels and helps it expand and resist therapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "ATRT hides in a macrophage-rich niche: tumor-associated macrophages dominate its immunosuppressive microenvironment, helping this poorly immunogenic rhabdoid tumor evade T cells and resist checkpoint therapy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "ATRT drives angiogenesis through VEGF: to feed its rapid growth the tumor releases VEGF, building the leaky vessels that supply it—a target for anti-angiogenic strategies in this hard-to-treat cancer."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "ATRT often calcifies: flecks of calcium within the tumor are a clue on the CT scan, appearing alongside the hemorrhage and cysts that mark these aggressive infant brain tumors."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "ATRT can spread beyond the nervous system: its extracranial rhabdoid counterparts and metastases reach the liver, lungs and bone, especially in the very young children it strikes."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "ATRT and rhabdoid tumors can seed the marrow: bone and bone-marrow metastases occur in disseminated disease, so staging looks beyond the brain in this highly malignant cancer."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the rhabdoid cell: a whorled ball of intermediate filaments shoves the nucleus to one side, the cytoplasmic inclusion that names these tumors and betrays their loss of the SMARCB1 brake."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "When rhabdoid tumors spread, the lung is a target: this aggressive cancer disseminates beyond the nervous system, seeding pulmonary metastases that mark widespread, often fatal disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "ATRT can reach the eye: leptomeningeal spread along the optic pathway and orbital involvement threaten vision, part of why this tumor's reach is mapped across the whole neuraxis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody clinches the diagnosis: ATRT is defined by loss of the SMARCB1/INI1 protein, and an immunohistochemical stain — an antibody against INI1 — shows the missing nuclear signal that separates it from other embryonal brain tumors."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "The platinum chemotherapy wastes magnesium: cisplatin and carboplatin, central to the intensive multi-agent regimens against ATRT, injure the kidney's tubules so magnesium leaks out and must be replaced."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Curing ATRT empties the marrow: its dose-intense, often high-dose chemotherapy crashes the neutrophil count, leaving these infants in long stretches of febrile neutropenia that demand vigilant infection control."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "ATRT can run in families: many cases stem from germline SMARCB1 loss (rhabdoid tumor predisposition syndrome), so finding it prompts genetic counseling and testing of parents and future siblings."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The marrow's red line falls too: the intensive chemotherapy and any craniospinal radiation suppress erythrocyte production into an anemia that, with the low platelets and neutrophils, leaves these infants transfusion-dependent through treatment."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The rhabdoid family reaches the soft tissues: the same SMARCB1 loss spawns malignant rhabdoid tumors of the kidney and paraspinal soft tissue and muscle, ATRT's extracranial cousins under one genetic umbrella."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth signaling drives the rhabdoid cell: the IGF-1/IGF1R pathway is active in ATRT and other rhabdoid tumors, fueling proliferation and offering a targeted vulnerability under study."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The tumor builds an immune-cold microenvironment: regulatory T cells and few effector lymphocytes blunt the antitumor response in ATRT, a barrier that checkpoint and other immunotherapies are being tested against."
  - target: 01-human/07-system/chordoma
    relation: connects-to
    note: "SMARCB1 loss links them across the midline: poorly-differentiated chordoma deletes the same SMARCB1 gene as ATRT, so the two share a defining epigenetic lesion despite arising from utterly different tissues."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "The growing mass irritates the cortex: like other brain tumors, ATRT can present with or cause seizures as it expands and raises intracranial pressure, so seizure control is part of the supportive care for these infants."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "SMARCB1 loss spans CNS tumors: germline SMARCB1 inactivation that causes ATRT also predisposes to familial multiple meningiomas and schwannomas, placing them in one SWI-SNF tumor-predisposition spectrum."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "ATRT recruits a dense blood supply: the tumor is highly vascular and VEGF-driven, so its endothelial cells sustain rapid growth and make antiangiogenic strategies a line of investigation alongside cytotoxic therapy."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Rhabdoid cells lean on STAT3: SMARCB1-deficient ATRT shows STAT3 activation supporting proliferation and survival, one of the signaling dependencies explored where this aggressive infant tumor resists standard therapy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Loss of the SWI/SNF brake lifts NF-κB: SMARCB1 loss in ATRT derepresses inflammatory and survival signaling including NF-κB, contributing to the tumor's growth in the absence of its chromatin-remodeling tumor suppressor."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Intensive infant therapy invites infection: the high-dose chemotherapy and sometimes stem-cell rescue used against ATRT cause profound neutropenia, making febrile neutropenia and sepsis a major treatment hazard in these young children."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Prolonged neutropenia opens the lung to mold: the deep neutropenia of high-dose ATRT chemotherapy and stem-cell rescue lets inhaled Aspergillus invade as pulmonary aspergillosis, a dangerous infection in these infants."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its platinum chemo is hard on small kidneys: the cisplatin and ifosfamide in ATRT regimens are nephrotoxic, and in an infant the tubular and electrolyte injury can leave lasting chronic kidney impairment."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracyclines can scar the developing heart: doxorubicin used against ATRT is dose-dependently cardiotoxic, risking a cardiomyopathy and heart failure that can surface years into survivorship."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Vincristine and CNS injury leave lasting pain: the vincristine in ATRT regimens causes peripheral neuropathy, and tumor or surgery affecting the spinal cord adds neuropathic pain in these young patients."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Intensive therapy and tumor blunt the marrow: the aggressive multi-agent chemotherapy for ATRT plus the inflammatory burden of an advanced tumor suppress erythropoiesis into an anemia of chronic disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A devastating infant brain cancer strains families: the dire prognosis, intensive treatment and neurological injury of ATRT impose a heavy psychological burden on survivors and their parents."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Infant neurosurgery is a healing challenge: the maximal-safe resection of an ATRT in a small child, often followed by chemotherapy and radiation, leaves a cranial wound that must heal in a vulnerable patient."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Treatment damages the hormone axis: craniospinal irradiation and surgery near the hypothalamus and pituitary in ATRT cause growth-hormone deficiency and other endocrinopathies in survivors."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A dire prognosis breeds relentless worry: the aggressive course, intensive therapy and grim outlook of ATRT foster profound anxiety in families alongside the depression it brings."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It shares a gene with a kidney tumour: germline SMARCB1 loss causes rhabdoid tumour predisposition syndrome, in which ATRT coexists with malignant rhabdoid tumours of the kidney, prompting renal surveillance."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its intensive therapy assaults the skin: craniospinal radiation causes radiation dermatitis, and the multi-agent chemotherapy of infant ATRT brings alopecia and mucocutaneous toxicity."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its chemotherapy can scar the heart: anthracyclines used against ATRT carry a long-term cardiotoxicity risk in the rare survivors of this aggressive infant tumour."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Treatment suppresses immunity and biology invites it: intensive infant chemotherapy leaves children profoundly immunocompromised, while SMARCB1-deficient rhabdoid tumours are being explored for immune and EZH2-targeted therapy."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It seeds the neuraxis and beyond: ATRT spreads through the cerebrospinal fluid and can metastasise outside the brain, including to the lungs, while intensive therapy invites pneumonia."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Harsh chemotherapy hits the gut: the multidrug regimens used against ATRT cause severe nausea, mucositis and feeding difficulty in very young children."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Intensive chemo is the backbone: AT/RT is treated with aggressive multi-agent chemotherapy, sometimes high-dose with stem-cell rescue, given its poor prognosis in very young children."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Epigenetic drugs target the defect: because SMARCB1 loss unleashes EZH2, EZH2 inhibitors such as tazemetostat and CDK4/6 inhibitors are being trialled against rhabdoid tumours."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "A fellow aggressive childhood tumour: like Ewing sarcoma, AT/RT is a highly malignant paediatric cancer driven by a single defining genetic lesion, and the two enter the small-round-blue-cell differential."
---

# Atypical Teratoid/Rhabdoid Tumor

## Overview

**Atypical teratoid/rhabdoid tumor (AT/RT)** is a highly malignant CNS neoplasm (WHO grade 4, 2021) defined by biallelic inactivation of **SMARCB1** (INI1/BAF47, chromosome 22q11.23) in ~95% of cases, or **SMARCA4** (BRG1) in ~5%. AT/RT is the most common malignant brain tumor in **infants under 1 year** (~50% of pediatric malignant brain tumors <12 months) and accounts for ~1-2% of all pediatric CNS tumors. Approximately 50-60 cases are diagnosed per year in the USA. Despite intensive multimodal therapy, AT/RT remains one of the most devastating pediatric cancers, with 2-year OS ~40-50% and a markedly worse prognosis in infants (<18 months) and patients with disseminated disease [^fruhwald-2020-atrt-subgroups].

The tumor derives its name from its mixed histology: rhabdoid cells (classic morphology) co-exist with primitive neuroectodermal, mesenchymal, and epithelial components — resembling a teratoma. However, unlike true teratomas, AT/RT has a single driver molecular event (SMARCB1/SMARCA4 LOF) underlying its apparent lineage plasticity.

**Sites:** Infratentorial (posterior fossa, ~50-60%): cerebellar hemisphere, brainstem, cerebellopontine angle; supratentorial (~30-40%); spinal cord/cauda equina (~5-10%); leptomeningeal dissemination at diagnosis in ~30-40%.

**Germline SMARCB1 (RTPS1):**
~30-35% of AT/RT patients carry germline SMARCB1 mutations (compared to ~5% for most pediatric brain tumors). Rhabdoid tumor predisposition syndrome type 1 (RTPS1) confers risk for AT/RT, malignant rhabdoid tumor of the kidney (MRT), and extra-renal rhabdoid tumors; infants with synchronous CNS + renal rhabdoid tumors typically carry germline mutations; genetic testing at diagnosis is mandatory for all AT/RT patients.

## Structure

### Molecular subgroups (WHO 2021 / DNA methylation-based)

Three AT/RT subgroups defined by DNA methylation profiling and gene expression [^fruhwald-2020-atrt-subgroups]:

**AT/RT-TYR (~35%):**
- Dominant gene expression: tyrosinase (TYR), MITF overexpression → melanocytic differentiation signature
- Location: posterior fossa (cerebellum, brainstem)
- Age: youngest patients (median ~5-9 months)
- Genetic: SMARCB1 LOF (deletion predominant); high CDKN2A deletion rate (~30%)
- Prognosis: worst OS among subgroups (~30-35% 2-year OS); aggressive; responds poorly to chemotherapy

**AT/RT-SHH (~35%):**
- Dominant gene expression: GLI2, MYCN, PTCH1 → SHH pathway activation
- Location: supratentorial and posterior fossa; spinal cord
- Age: broader age range (median ~18-24 months), some older children
- Genetic: SMARCB1 LOF (point mutations and deletions); highest rate of germline SMARCB1
- Prognosis: intermediate (~45-55% 2-year OS)

**AT/RT-MYC (~30%):**
- Dominant gene expression: MYC, HOTAIR, mesenchymal markers
- Location: supratentorial predominant; suprasellar/3rd ventricular region
- Age: older children (median ~24-36 months); some school-age children
- Genetic: SMARCB1 LOF (point mutations predominant); CDKN2A deletion less frequent
- Prognosis: relatively better (~55-65% 2-year OS); longer PFS after HDC/ASCR in some series

### Histology

**Classic rhabdoid cells:**
Large cells (15-25 μm) with eccentric nuclei, prominent eosinophilic nucleoli ("owl-eye"), and abundant pale eosinophilic cytoplasm with fibrillary or globular inclusions (intermediate filament whorls); cells mimic skeletal muscle cells (rhabdomyoblasts) morphologically but are not myogenic.

**IHC panel:**
- **INI1 (SMARCB1) by IHC**: complete loss of nuclear staining in tumor cells (retained in endothelium, lymphocytes, normal glia) — diagnostic; ~95-100% sensitive for AT/RT; negative INI1 in any undifferentiated pediatric brain tumor should trigger molecular workup
- Vimentin: ~90-100% positive
- EMA (epithelial membrane antigen): ~80% positive
- SMA (smooth muscle actin): ~40-50% positive
- Synaptophysin, GFAP, cytokeratin: variable (reflects lineage plasticity)
- CD99: variable; MIB-1 (Ki-67): typically >80%

**Ultra-rare variant:**
SMARCA4-deficient AT/RT: identical morphology and prognosis; SMARCA4 IHC (BRG1) shows loss of nuclear staining; SMARCB1 IHC intact; must test both in INI1-intact rhabdoid-appearing tumors.

## Function

### Normal SWI/SNF biology in CNS

In the normal CNS, SMARCB1-containing BAF complex is essential for:
- Neural stem cell self-renewal and lineage restriction
- Neuron differentiation (BAF complexes switch subunit composition from npBAF in neural progenitors → nBAF in postmitotic neurons)
- Oligodendrocyte maturation (BRG1-containing BAF required for myelination gene activation)
- SMARCB1 specifically maintains open chromatin at enhancers of differentiation TFs → loss of SMARCB1 → epigenetic reprogramming toward an undifferentiated rhabdoid state

AT/RT epigenome is characterized by global **H3K27me3 accumulation** (due to unopposed PRC2 activity) at genes that mediate neural differentiation, lineage identity, and the G1 checkpoint — explaining the morphologic primitiveness and mixed lineage marker expression.

## Pathology

### Molecular drivers

**Primary driver (obligate):**
- **SMARCB1 biallelic LOF** (~95%): deletions (single exon, partial gene, or whole-gene deletion at 22q11.23) in ~60%; intragenic frameshift/truncating mutations in ~35%; rarely inactivating missense
- **SMARCA4 biallelic LOF** (~5%): equivalent mechanism via BRG1 loss (also SMARCB1-independent BRG1 loss in aggressive undifferentiated thoracic tumors — a distinct entity)

**Secondary alterations (rare in AT/RT — oligogenomic tumor):**
- **CDKN2A deletion** (~15-25%): second most common alteration; SMARCB1-mediated CDKN2A silencing is epigenetic (reversible), but true deletion is permanent and associated with worse prognosis
- **TP53 mutations**: rare (~5-8%); when present, correlate with Li-Fraumeni background
- **PIK3CA mutations**: ~5%; mTOR pathway activation
- **MYC amplification** (<5%): distinct from AT/RT-MYC subgroup (which has high MYC expression without amplification in most cases)
- AT/RT has remarkably simple genomic landscape (compared to GBM or medulloblastoma) — SMARCB1 LOF is sufficient for full oncogenic transformation

### Treatment

AT/RT has no established standard of care; protocols are protocol-driven and center-specific, with COG and EU-RHAB providing the largest prospective datasets.

**Standard multimodal approach:**
1. **Surgery**: maximal safe resection (GTR associated with better OS in all series); ETV/VP shunt for hydrocephalus
2. **Induction chemotherapy**: typically ICT (ifosfamide, carboplatin, etoposide) or High-Dose Intensive Chemotherapy regimens (IVADo: ifosfamide, vincristine, dactinomycin + doxorubicin); European SIOPE/EU-RHAB protocols use VEC (vincristine, etoposide, carboplatin) + HD-MTX
3. **Consolidation**: HDC + autologous stem cell rescue (HDC/ASCR): most common regimen — thiotepa-based or carboplatin+thiotepa+etoposide; shown to improve EFS vs non-HDC historical controls; tandem ASCR in some centers
4. **Radiation therapy**: CSI + local boost; deferred in infants <36 months (severe neurocognitive effects); focal stereotactic RT for older children; proton preferred (reduce integral dose); role of radiation in AT/RT-TYR vs AT/RT-MYC subgroups may differ

**COG ACNS0333 (published 2023):** N=65 evaluable patients; head-trauma (HD) induction + HDC/ASCR × 2 cycles + focal RT; 4-year EFS 37%; 4-year OS 43%; best results in non-disseminated AT/RT-SHH; AT/RT-TYR had worst outcomes; no late relapses beyond 3 years.

**EU-RHAB registry (Frühwald 2020):** [^fruhwald-2020-atrt-subgroups] N=147 patients; intensive multimodal treatment (surgery + chemotherapy ± HDC ± RT); 3-year OS 43%; subgroup differences: AT/RT-SHH and AT/RT-MYC showed significantly better OS than AT/RT-TYR (log-rank p<0.001); germline SMARCB1 did NOT independently predict worse outcome after stratification by subgroup and metastasis.

**Prognosis by clinical factors:**
- Non-disseminated + GTR + AT/RT-SHH or AT/RT-MYC + age >18 months: 3-year OS ~60-70%
- Disseminated disease at diagnosis: 3-year OS ~15-25%
- Age <12 months: 3-year OS ~25-35% (radiation not given, limiting local control)
- Germline SMARCB1 (RTPS1): prognosis similar to sporadic AT/RT when matched for subgroup

**Novel therapies (investigational):**
- **Tazemetostat (EZH2 inhibitor)**: FDA-approved for epithelioid sarcoma (SMARCB1-null); Phase 1/2 in AT/RT (COG ADVL1213/PBTC): NCT trials ongoing; H3K27me3 reduction documented in tumor biopsies; response rates ~10-20% in early data
- **ONC201 (DRD2/DRD3 antagonist)**: activity in Group 4 MB; being evaluated in AT/RT-MYC (MYC overexpression downstream of dopaminergic signaling); Phase 1 pediatric trial
- **Anti-PD-1 (pembrolizumab, nivolumab)**: low TMB in AT/RT limits expected immunotherapy benefit; PD-L1 expressed variably; trials ongoing in recurrent AT/RT
- **Alisertib (AURKA inhibitor)**: Phase 2 in recurrent AT/RT; modest activity; synergizes with SMARCB1 rescue in preclinical models
- **BET inhibitors**: strong preclinical rationale (MYC suppression in AT/RT-MYC); mivebresib and ZEN-3694 in early trials

**Radiation considerations:**
- CSI 36 Gy + boost 54-59.4 Gy (standard for non-infant, localized AT/RT)
- Focal RT 54-59.4 Gy (some centers for localized non-disseminated AT/RT >12-18 months)
- Proton beam preferred (HiRES trial ongoing comparing proton vs photon in pediatric CNS)
- Radiation omission in infants → high local and distant failure rates; some centers use focal stereotactic for isolated posterior fossa disease

## Connections

- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SMARCB1 biallelic LOF defines AT/RT (~95% of cases); INI1 IHC (loss of nuclear staining) is the diagnostic standard; germline SMARCB1 → RTPS1 with multi-focal rhabdoid tumors at birth; SMARCA4-mutant AT/RT (~5%) is clinically similar.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — SMARCB1 LOF → PRC2/EZH2 unrestricted → H3K27me3 at BAF-target loci (CDKN2A, HOX, differentiation genes); AT/RT cells are EZH2-dependent; tazemetostat reduces H3K27me3 and restores differentiation markers; AT/RT EZH2 inhibition is in clinical trials.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — AT/RT-MYC subgroup (~30%): MYC overexpression via BRD4-occupied super-enhancers (SMARCB1 loss → BRD4 unrestricted); supratentorial, older patients; BET inhibitors (JQ1) suppress MYC in AT/RT-MYC cells; ONC201 (DRD2 antagonist) investigated in AT/RT.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations are absent in most AT/RT; SMARCB1 loss → ARF epigenetically silenced → MDM2 unrestricted → p53 degraded without TP53 mutation; p53 suppression via ARF silencing (not TP53 mutation) is the primary p53-pathway inactivation mechanism in SMARCB1-null rhabdoid tumors.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — SMARCB1 LOF epigenetically silences ARF (CDKN2A p14) → MDM2 unrestricted → p53 degradation without TP53 mutation; CDKN2A homozygous deletion (~15-25% of AT/RT) adds permanent G1 bypass; CDKN2A deletion correlates with AT/RT-TYR and worst OS among molecular subgroups.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — AT/RT is predominantly a CNS tumor; infratentorial (cerebellum, brainstem) in ~50-60%; the most common malignant brain tumor in infants <1 year; leptomeningeal dissemination in ~30-40%; proton CSI preferred in eligible patients to reduce long-term neurocognitive injury.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — AT/RT and medulloblastoma are the two most common pediatric malignant posterior fossa tumors; INI1 IHC loss (AT/RT) vs. intact INI1 (MB) is the key differentiator; SMARCB1 LOF never seen in MB; misdiagnosis as MB is a known pitfall; methylation profiling resolves ambiguous cases.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — AT/RT and synovial sarcoma are united by SWI/SNF (BAF) disruption and EZH2 dependence: AT/RT deletes SMARCB1 outright, while SS18-SSX fusion evicts SMARCB1 from BAF — both unleash PRC2/EZH2, so the EZH2 inhibitor tazemetostat is active in each despite different ages and sites.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — AT/RT has a renal twin: malignant rhabdoid tumor of the kidney shares the same biallelic SMARCB1 (INI1) loss and rhabdoid morphology, and germline SMARCB1 (rhabdoid predisposition) causes synchronous brain AT/RT and renal rhabdoid tumors in infants — one disease across organs.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — SMARCB1 links AT/RT and schwannomatosis at opposite doses: biallelic SMARCB1 loss in a child causes aggressive AT/RT, while a germline single-allele SMARCB1 variant causes schwannomatosis — multiple benign schwannomas in adults — same gene, very different tumors.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — ATRT and malignant rhabdoid tumor of the kidney are the same SMARCB1-driven cancer in different sites: loss of the SWI/SNF subunit SMARCB1 (INI1) produces rhabdoid tumors in brain (ATRT) or kidney, so both belong to the rhabdoid tumor predisposition syndrome and resemble Wilms.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — ATRT and rhabdomyosarcoma both feature rhabdoid/small-round-blue-cell morphology and must be distinguished molecularly: ATRT is defined by SMARCB1 (INI1) loss while rhabdomyosarcoma shows myogenic markers and PAX-FOXO1 fusions—a distinction that dictates very different therapy.
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — ATRT and diffuse midline glioma are both aggressive pediatric brain tumors driven by epigenetic dysregulation: ATRT by SMARCB1/SWI-SNF loss, DMG by the H3 K27M histone mutation—both reprogram chromatin rather than relying on classic oncogenes, and both carry a grim prognosis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is central but fraught in atypical teratoid/rhabdoid tumor: this aggressive infant brain tumor needs craniospinal photon or proton irradiation, but radiation is especially neurotoxic to the very young brain—so proton beam and timing limit lifelong damage.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — ATRT and neuroblastoma are both aggressive embryonal tumors of infancy with small-round-blue-cell histology: ATRT is a SMARCB1-deficient CNS/renal rhabdoid tumor, while neuroblastoma is a sympathoadrenal MYCN-driven tumor—told apart by INI1 loss and site.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — ATRT and retinoblastoma are aggressive embryonal cancers of early childhood driven by loss of a single tumor suppressor—SMARCB1 in ATRT versus RB1 in retinoblastoma—and like trilateral retinoblastoma, ATRT can arise in the pineal region of an infant brain.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — ATRT arises in the neuron-rich central nervous system: this aggressive infant tumor forms brain masses that compress and infiltrate neural tissue, causing the hydrocephalus and deficits that bring it to attention—though its cells are rhabdoid, not neuronal.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — ATRT must be distinguished from astrocyte-derived tumors: unlike gliomas that arise from astrocytes, ATRT is an embryonal rhabdoid tumor defined by SMARCB1 loss, so molecular testing—not histology alone—separates it from the astrocytomas it can mimic on imaging.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — ATRT and glioblastoma are both highly aggressive brain tumors but at opposite ages and origins: ATRT strikes infants via SWI/SNF (SMARCB1) loss, while glioblastoma is an adult glial tumor—yet both share dismal prognosis and therapy resistance.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immunotherapy is being explored in ATRT: despite a low mutation burden, SMARCB1 loss can make these tumors immunogenic, so PD-1 checkpoint blockade is under study for a cancer that resists conventional therapy and devastates infants.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — ATRT is a highly aggressive embryonal tumor of the central nervous system: it arises in the brain (often the cerebellum) of very young children, so it presents with raised intracranial pressure and rapid neurological decline—among the most lethal pediatric CNS cancers.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — ATRT and Li-Fraumeni syndrome both stem from tumor-suppressor loss but differ in gene: ATRT is driven by biallelic SMARCB1 (a chromatin-remodeler) loss, while Li-Fraumeni is germline TP53—two routes by which a single gene defect unleashes childhood cancer.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — ATRT shows actionable pathway activation including mTOR: loss of SMARCB1 deregulates signaling that converges on mTOR and aurora kinase, so targeted inhibitors are being tested to add precision options to this aggressive infant brain tumor's harsh chemoradiation.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunotherapy is being explored in ATRT via cytotoxic T cells: despite few mutations, some ATRTs carry immune infiltrate, so checkpoint blockade and T-cell approaches are studied for a tumor where conventional treatment often fails in the very young.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — ATRT cells may depend on autophagy to survive: SWI/SNF loss and metabolic stress make these tumors lean on autophagic recycling, so blocking autophagy is studied as a vulnerability in a cancer that resists standard treatment.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ATRT is a SWI/SNF disease beyond SMARCB1: ARID1A is another subunit of the same chromatin-remodeling complex, so the rhabdoid tumor's defining loss of SMARCB1 sits in a pathway where ARID1A mutations cause related epigenetically-driven cancers.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — ATRT recruits the brain's own microglia: these resident immune cells infiltrate the tumor and are often co-opted into a tumor-supporting state, shaping the immune microenvironment of this aggressive infant brain cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — SMARCB1 loss makes ATRT a target for NK cells: rhabdoid tumors lacking SMARCB1 can downregulate MHC and upregulate stress ligands, and NK-cell-based immunotherapy is explored against these poorly immunogenic tumors.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Losing SMARCB1 makes ATRT lean on CDK4/6: the chromatin defect derepresses cyclin D and drives the cell-cycle kinase, so CDK4/6 inhibitors are being tested to exploit this dependency in a cancer with few other targets.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are being enlisted against ATRT: because these rhabdoid tumors are poorly immunogenic, dendritic-cell vaccines and other strategies to present tumor antigens aim to spark a T-cell attack on residual disease.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — ATRT arises in the developing brain among glial precursors: its rhabdoid cells can show divergent differentiation toward neural and glial lines including oligodendrocyte features, reflecting the primitive cell of origin in infants.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — ATRT outgrows its oxygen: this fast, aggressive infant tumor turns hypoxic at its core, switching on the HIF/VEGF program that sprouts new vessels and helps it expand and resist therapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — ATRT hides in a macrophage-rich niche: tumor-associated macrophages dominate its immunosuppressive microenvironment, helping this poorly immunogenic rhabdoid tumor evade T cells and resist checkpoint therapy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — ATRT drives angiogenesis through VEGF: to feed its rapid growth the tumor releases VEGF, building the leaky vessels that supply it—a target for anti-angiogenic strategies in this hard-to-treat cancer.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — ATRT often calcifies: flecks of calcium within the tumor are a clue on the CT scan, appearing alongside the hemorrhage and cysts that mark these aggressive infant brain tumors.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — ATRT can spread beyond the nervous system: its extracranial rhabdoid counterparts and metastases reach the liver, lungs and bone, especially in the very young children it strikes.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — ATRT and rhabdoid tumors can seed the marrow: bone and bone-marrow metastases occur in disseminated disease, so staging looks beyond the brain in this highly malignant cancer.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the rhabdoid cell: a whorled ball of intermediate filaments shoves the nucleus to one side, the cytoplasmic inclusion that names these tumors and betrays their loss of the SMARCB1 brake.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — When rhabdoid tumors spread, the lung is a target: this aggressive cancer disseminates beyond the nervous system, seeding pulmonary metastases that mark widespread, often fatal disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — ATRT can reach the eye: leptomeningeal spread along the optic pathway and orbital involvement threaten vision, part of why this tumor's reach is mapped across the whole neuraxis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody clinches the diagnosis: ATRT is defined by loss of the SMARCB1/INI1 protein, and an immunohistochemical stain — an antibody against INI1 — shows the missing nuclear signal that separates it from other embryonal brain tumors.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — The platinum chemotherapy wastes magnesium: cisplatin and carboplatin, central to the intensive multi-agent regimens against ATRT, injure the kidney's tubules so magnesium leaks out and must be replaced.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Curing ATRT empties the marrow: its dose-intense, often high-dose chemotherapy crashes the neutrophil count, leaving these infants in long stretches of febrile neutropenia that demand vigilant infection control.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — ATRT can run in families: many cases stem from germline SMARCB1 loss (rhabdoid tumor predisposition syndrome), so finding it prompts genetic counseling and testing of parents and future siblings.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The marrow's red line falls too: the intensive chemotherapy and any craniospinal radiation suppress erythrocyte production into an anemia that, with the low platelets and neutrophils, leaves these infants transfusion-dependent through treatment.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The rhabdoid family reaches the soft tissues: the same SMARCB1 loss spawns malignant rhabdoid tumors of the kidney and paraspinal soft tissue and muscle, ATRT's extracranial cousins under one genetic umbrella.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth signaling drives the rhabdoid cell: the IGF-1/IGF1R pathway is active in ATRT and other rhabdoid tumors, fueling proliferation and offering a targeted vulnerability under study.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The tumor builds an immune-cold microenvironment: regulatory T cells and few effector lymphocytes blunt the antitumor response in ATRT, a barrier that checkpoint and other immunotherapies are being tested against.
- `connects-to` → **[Chordoma](../chordoma/README.md)** — SMARCB1 loss links them across the midline: poorly-differentiated chordoma deletes the same SMARCB1 gene as ATRT, so the two share a defining epigenetic lesion despite arising from utterly different tissues.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — The growing mass irritates the cortex: like other brain tumors, ATRT can present with or cause seizures as it expands and raises intracranial pressure, so seizure control is part of the supportive care for these infants.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — SMARCB1 loss spans CNS tumors: germline SMARCB1 inactivation that causes ATRT also predisposes to familial multiple meningiomas and schwannomas, placing them in one SWI-SNF tumor-predisposition spectrum.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — ATRT recruits a dense blood supply: the tumor is highly vascular and VEGF-driven, so its endothelial cells sustain rapid growth and make antiangiogenic strategies a line of investigation alongside cytotoxic therapy.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Rhabdoid cells lean on STAT3: SMARCB1-deficient ATRT shows STAT3 activation supporting proliferation and survival, one of the signaling dependencies explored where this aggressive infant tumor resists standard therapy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Loss of the SWI/SNF brake lifts NF-κB: SMARCB1 loss in ATRT derepresses inflammatory and survival signaling including NF-κB, contributing to the tumor's growth in the absence of its chromatin-remodeling tumor suppressor.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Intensive infant therapy invites infection: the high-dose chemotherapy and sometimes stem-cell rescue used against ATRT cause profound neutropenia, making febrile neutropenia and sepsis a major treatment hazard in these young children.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Prolonged neutropenia opens the lung to mold: the deep neutropenia of high-dose ATRT chemotherapy and stem-cell rescue lets inhaled Aspergillus invade as pulmonary aspergillosis, a dangerous infection in these infants.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its platinum chemo is hard on small kidneys: the cisplatin and ifosfamide in ATRT regimens are nephrotoxic, and in an infant the tubular and electrolyte injury can leave lasting chronic kidney impairment.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracyclines can scar the developing heart: doxorubicin used against ATRT is dose-dependently cardiotoxic, risking a cardiomyopathy and heart failure that can surface years into survivorship.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Vincristine and CNS injury leave lasting pain: the vincristine in ATRT regimens causes peripheral neuropathy, and tumor or surgery affecting the spinal cord adds neuropathic pain in these young patients.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Intensive therapy and tumor blunt the marrow: the aggressive multi-agent chemotherapy for ATRT plus the inflammatory burden of an advanced tumor suppress erythropoiesis into an anemia of chronic disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A devastating infant brain cancer strains families: the dire prognosis, intensive treatment and neurological injury of ATRT impose a heavy psychological burden on survivors and their parents.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Infant neurosurgery is a healing challenge: the maximal-safe resection of an ATRT in a small child, often followed by chemotherapy and radiation, leaves a cranial wound that must heal in a vulnerable patient.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Treatment damages the hormone axis: craniospinal irradiation and surgery near the hypothalamus and pituitary in ATRT cause growth-hormone deficiency and other endocrinopathies in survivors.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A dire prognosis breeds relentless worry: the aggressive course, intensive therapy and grim outlook of ATRT foster profound anxiety in families alongside the depression it brings.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It shares a gene with a kidney tumour: germline SMARCB1 loss causes rhabdoid tumour predisposition syndrome, in which ATRT coexists with malignant rhabdoid tumours of the kidney, prompting renal surveillance.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its intensive therapy assaults the skin: craniospinal radiation causes radiation dermatitis, and the multi-agent chemotherapy of infant ATRT brings alopecia and mucocutaneous toxicity.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its chemotherapy can scar the heart: anthracyclines used against ATRT carry a long-term cardiotoxicity risk in the rare survivors of this aggressive infant tumour.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Treatment suppresses immunity and biology invites it: intensive infant chemotherapy leaves children profoundly immunocompromised, while SMARCB1-deficient rhabdoid tumours are being explored for immune and EZH2-targeted therapy.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It seeds the neuraxis and beyond: ATRT spreads through the cerebrospinal fluid and can metastasise outside the brain, including to the lungs, while intensive therapy invites pneumonia.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Harsh chemotherapy hits the gut: the multidrug regimens used against ATRT cause severe nausea, mucositis and feeding difficulty in very young children.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Intensive chemo is the backbone: AT/RT is treated with aggressive multi-agent chemotherapy, sometimes high-dose with stem-cell rescue, given its poor prognosis in very young children.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Epigenetic drugs target the defect: because SMARCB1 loss unleashes EZH2, EZH2 inhibitors such as tazemetostat and CDK4/6 inhibitors are being trialled against rhabdoid tumours.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — A fellow aggressive childhood tumour: like Ewing sarcoma, AT/RT is a highly malignant paediatric cancer driven by a single defining genetic lesion, and the two enter the small-round-blue-cell differential.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^biegel-1999-ini1-atrt]: Biegel JA, Zhou JY, Rorke LB, Stenstrom C, Wainwright LM, Fogelgren B. Germ-line and acquired mutations of INI1 in atypical teratoid and rhabdoid tumors. *Cancer Res.* 1999;59(1):74-79. [PubMed 9892189](https://pubmed.ncbi.nlm.nih.gov/9892189/)
[^fruhwald-2020-atrt-subgroups]: Frühwald MC, Hasselblatt M, Nemes K, et al. Age and DNA methylation subgroup as potential treatment targets in children with atypical teratoid rhabdoid tumors. *Neuro Oncol.* 2020;22(7):1006-1017. [doi:10.1093/neuonc/noz244](https://doi.org/10.1093/neuonc/noz244) · [PubMed 31900478](https://pubmed.ncbi.nlm.nih.gov/31900478/)
