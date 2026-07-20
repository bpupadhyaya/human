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
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Engineered cells are being aimed at it: CAR-T and related cell therapies against targets like B7-H3, delivered intrathecally for CNS tumours, are investigational for the dismal-prognosis rhabdoid tumours including AT/RT."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy has limited reach: despite a low mutational burden, some rhabdoid tumours carry immune infiltrate, so checkpoint inhibitors are explored in AT/RT, though responses so far are modest."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Craniospinal radiation scars cognition: the intensive radiotherapy needed to control AT/RT, especially craniospinal irradiation in older children, injures the hippocampus and leaves survivors with lasting neurocognitive deficits."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Extracranial spread to the lung: AT/RT can disseminate beyond the CNS to seed pulmonary metastases in the alveolar capillary bed, a marker of widespread and often fatal disease."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver metastasis: AT/RT, one of the few brain tumours that spreads outside the nervous system, can seed the hepatic lobule as part of disseminated rhabdoid disease."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Childhood cancers of the Li-Fraumeni spectrum: like AT/RT, osteosarcoma can arise in Li-Fraumeni syndrome from germline TP53 loss, linking a brain rhabdoid tumour and a bone sarcoma through shared tumour-suppressor failure."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "Two ways to break SWI/SNF: AT/RT loses the SMARCB1 subunit while ovarian clear cell carcinoma loses ARID1A—different subunits crippling the same SWI/SNF chromatin-remodelling complex."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "SMARCB1 beyond the brain: the same SMARCB1 loss defining AT/RT drives renal medullary carcinoma (in sickle-cell trait) and malignant rhabdoid tumour of the kidney, a family of SMARCB1-deficient cancers."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Metastatic spread: malignant rhabdoid tumours, including extracranial forms, can metastasise to bone, depositing in the cortical bone alongside their spread to lung and liver."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cyclin D1 dependence: loss of SMARCB1 derepresses cyclin D1, driving the CDK4/6-fuelled cell cycle and making ATRT cells dependent on this axis—the rationale for CDK4/6 inhibition."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Aberrant Wnt signalling: SMARCB1 loss can derepress Wnt/β-catenin target genes, an oncogenic signalling pathway contributing to rhabdoid tumour proliferation distinct from the cell-cycle axis."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Epigenetic contrast: like ATRT, IDH-mutant glioma is fundamentally an epigenetic disease, but driven by oncometabolite-mediated DNA hypermethylation rather than SWI/SNF chromatin-remodeller loss."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Growth signalling: SMARCB1 loss in ATRT activates PI3K/AKT signalling, driving the survival and proliferation that make this aggressive infant brain tumour so rapidly fatal."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the rapidly growing, hypoxic ATRT promotes the VEGF angiogenesis that feeds its aggressive expansion."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT reactivation maintains telomeres in ATRT cells, granting the limitless proliferation needed to sustain this fast-growing embryonal tumour."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "SHH subgroup: the ATRT-SHH molecular subgroup shows active sonic-hedgehog signalling through Smoothened, one of the distinct lineage programmes that SMARCB1 loss unleashes in these tumours."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Lineage signalling: Notch pathway activation features in ATRT subgroups, contributing to the aberrant neural-developmental programmes driving the tumour after loss of SWI/SNF repression."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Immunosuppressive niche: CCL2 recruits tumour-associated macrophages into the ATRT microenvironment, building the immunosuppressive milieu that hampers immune control of this aggressive infant tumour."
  - target: 01-human/03-molecular/ptch1
    relation: connects-to
    note: "Hedgehog receptor: in the ATRT-SHH subgroup the Hedgehog pathway is active at the PTCH1-SMO receptor level, the lineage programme that SMARCB1 loss derepresses and a potential target with Hedgehog inhibitors."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Leptomeningeal spread: CXCR4 on ATRT cells follows CXCL12 gradients in the cerebrospinal fluid, contributing to the leptomeningeal dissemination that worsens the already dismal prognosis of these infant brain tumours."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemoradiation apoptosis: the intensive chemotherapy and radiation used against ATRT kill tumour cells through caspase-3-mediated apoptosis, the effector step whose evasion underlies treatment resistance and relapse."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Viral-mimicry immunogenicity: SMARCB1 (SWI/SNF) loss can derepress endogenous retroelements whose double-stranded RNA and DNA activate innate sensing including cGAS-STING, a 'viral mimicry' that EZH2 inhibition enhances to make ATRT more immunogenic."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Methylation subgroups: ATRT is epigenetically driven and divides into distinct DNA-methylation subgroups (TYR, SHH, MYC) with different biology and outcome, making DNA methylation both a classifier and a therapeutic axis in this SWI/SNF-deficient tumour."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Growth-factor dependency: a subset of rhabdoid tumours upregulate FGFR signalling as SMARCB1 loss reshapes the enhancer landscape, an oncogenic pathway under study as a targetable vulnerability in ATRT."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Derepressed cell cycle: SMARCB1 loss derepresses the CDK4/6-cyclin-D-RB axis (all already mapped), and E2F1-driven transcription powers the aggressive proliferation of atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival: PI3K-AKT-mTOR signalling (AKT and mTOR already mapped) is activated in ATRT and supports its growth, a targetable axis in this therapy-resistant infant brain tumour."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis resistance: high anti-apoptotic BCL-2 contributes to the chemoresistance of ATRT, a dependency that BH3-mimetic agents are being explored to exploit."
  - target: 01-human/03-molecular/sufu
    relation: connects-to
    note: "Hedgehog subgroup: SUFU negatively regulates GLI in the Sonic-Hedgehog pathway (PTCH1 and SMO already mapped), the pathway driving the SHH molecular subgroup of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Growth signalling: PTEN loss releases the PI3K-AKT-mTOR axis (all three already mapped), a growth-driving pathway exploited by the aggressive proliferation of ATRT."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK proliferation: ERK1/2 MAPK transduces receptor-tyrosine-kinase signals (FGFR already mapped) into the proliferative drive of ATRT, supporting its rapid growth."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) contributes to the proliferative and immunosuppressive programme of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling modulates the tumour microenvironment and invasive behaviour of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is expressed in rhabdoid tumours and contributes to their invasive and immunomodulatory phenotype."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "SMARCB1 loss in ATRT derepresses the cyclin-D-CDK4/6 axis (cyclin-D1 and CDK4/6 mapped), driving RB1 inactivation and the cell-cycle progression of the tumour."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of the immunologically variable atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the differentiation block and microenvironment of the SMARCB1-deficient atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-driven FOXO inactivation (PTEN, AKT, and PIK3CA already mapped) removes a pro-apoptotic brake in atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the often immune-cold atypical teratoid/rhabdoid tumor must evade."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory tumor microenvironment of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the GLI and β-catenin stability (SHH/SMO and WNT already mapped) of the developmental-signaling programs of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling contributes to the invasive and survival signaling of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic vulnerabilities of the SMARCB1-deficient cells of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "YAP1-Hippo signaling, de-repressed by SMARCB1 loss, contributes to the proliferation of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor-cell survival and immune signaling of atypical teratoid/rhabdoid tumor."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy target: this poor-prognosis infant brain tumour is being explored for checkpoint and cellular immunotherapy (PD-1 already mapped), and MHC class II antigen presentation shapes the T-cell response in an otherwise immunologically cold tumour."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cellular immunotherapy: IL-2 drives the expansion of the engineered and endogenous T cells behind the CAR-T and adoptive approaches under investigation for atypical teratoid/rhabdoid tumour given its dismal outcomes with conventional therapy."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint blockade: CTLA-4 restrains anti-tumour T-cell activation, and blocking it, alongside PD-1, is part of the immunotherapy strategy being tested to overcome the immune evasion of atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Chemotherapy anaemia: the intensive multi-agent chemotherapy for atypical teratoid/rhabdoid tumour is profoundly myelosuppressive, lowering haemoglobin and causing the anaemia and cytopenias that complicate treatment in these very young children."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: anthracyclines in the treatment regimens are cardiotoxic, and troponin elevation helps detect the myocardial injury that threatens the few long-term survivors of atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis and oxidative stress: the high proliferative rate of this embryonal tumour, lysed by chemotherapy, releases purines catabolised by xanthine oxidase to uric acid, contributing to tumour-lysis risk and oxidative stress."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton craniospinal therapy: proton-beam radiotherapy spares the developing infant brain (already mapped) compared with photon (already mapped) craniospinal irradiation, an important consideration in the very young children with atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1, CTLA-4 and CD8 already mapped), part of the immune evasion of this aggressive embryonal tumour."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the highly vascular atypical teratoid/rhabdoid tumour, part of its stromal microenvironment."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold immune microenvironment of atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of atypical teratoid/rhabdoid tumour."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the intensive multi-agent chemotherapy of atypical teratoid/rhabdoid tumour is myelosuppressive, causing anaemia (haemoglobin already mapped) that needs transfusion whose repeated support can load the young child with iron."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton-beam therapy: proton radiotherapy is used for atypical teratoid/rhabdoid tumour to deliver the tumour dose while sparing the developing brain of the young child, reducing the neurocognitive and growth toxicity."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy: the photon (X-ray) radiotherapy, often craniospinal, is part of the intensive multimodal treatment of atypical teratoid/rhabdoid tumour, balanced against the toxicity in the infant brain."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Tumour angiogenesis and stroma: PDGF drives the tumour angiogenesis (VEGF already mapped) and the stromal recruitment of atypical teratoid/rhabdoid tumour, part of its aggressive vascular biology."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Survivorship hypothalamic obesity: the craniospinal radiotherapy (photon already mapped) of ATRT can damage the hypothalamus, causing the leptin-resistant hypothalamic obesity of the survivors."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Survivorship metabolic syndrome: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic syndrome of the ATRT survivors after the craniospinal radiotherapy."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the anthracycline chemotherapy of the intensive ATRT regimens causes the cardiotoxicity (troponin already mapped) of the heart, a survivorship concern in the infant."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, explored with the checkpoint (PD-1 already mapped) immunotherapy of ATRT."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Survivorship adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic syndrome of the ATRT survivors after the craniospinal radiotherapy."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the atypical teratoid/rhabdoid tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the atypical teratoid/rhabdoid tumour."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the atypical teratoid/rhabdoid tumour."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the atypical teratoid/rhabdoid tumour."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the immune microenvironment of the atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory dimension of the atypical teratoid/rhabdoid tumour microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid (macrophage already mapped) recruitment into the atypical teratoid/rhabdoid tumour microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-TME axis: TSLP, from brain stromal cells and barrier epithelium, primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the immunosuppressive tumour microenvironment of atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-tumour axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability and the inflammatory cytokine milieu of the tumour microenvironment of ATRT."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Survivorship-anaemia axis: erythropoietin supports the management of the anaemia from the craniospinal irradiation and the myelosuppressive chemotherapy in the treatment of atypical teratoid/rhabdoid tumour."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell TME axis: histamine, from mast cells (already mapped) in the ATRT tumour microenvironment, amplifies the vascular permeability, the angiogenesis (already mapped) and the immunosuppressive cytokine milieu of the tumour stroma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-survivorship axis: melatonin, via MT1/MT2 receptors on tumour cells and neural progenitors (already mapped), exerts antitumour and neuroprotective effects relevant to the craniospinal-radiation survivorship of ATRT."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 already mapped) whose activation contributes to the tumour-promoting neuroinflammation and the immunosuppressive complement dimension of ATRT."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "ATRT testosterone: testosterone, via androgen receptors on neurons (already mapped) and microglia (already mapped), modulates the TME; testosterone deficiency amplifies the T-cytotoxic (already mapped) and complement-C5 (already mapped) antitumour cascade impairment of ATRT."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "ATRT serotonin: serotonin, via 5-HT receptors on microglia (already mapped) and neurons (already mapped), modulates the neuroinflammatory TME; serotonin dysregulation amplifies the T-cytotoxic (already mapped) and mast-cell (already mapped) antitumour cascade of ATRT."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "ATRT prolactin: prolactin, via PRLR on microglia (already mapped) and T-cytotoxic cells (already mapped), modulates the neuroimmune TME; prolactin dysregulation amplifies the neuroinflammatory (neuron already mapped) and mast-cell (already mapped) tumour cascade of ATRT."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "ATRT oxytocin: oxytocin, via OXTR on microglia (already mapped) and T-cytotoxic cells (already mapped), attenuates the neuroinflammatory TME; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of ATRT."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "ATRT vasopressin: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates the neuroimmune TME of ATRT; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory tumour cascade of ATRT."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "ATRT selenium: selenium, as GPx in neurons (already mapped) and microglia (already mapped), scavenges ROS driving the neuroinflammatory TME; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of ATRT."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "ATRT sodium: sodium dysregulation in bone-marrow (already mapped) stroma and tumour cells amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) tumour-promoting cascade in ATRT."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "ATRT potassium: potassium regulates macrophage (already mapped) and tumour cell membrane function; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) and mTOR (already mapped) tumour cascade in ATRT."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "ATRT zinc: zinc cofactors macrophage (already mapped) anti-tumour function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) and VEGF (already mapped) tumour-promoting cascade in ATRT."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "ATRT iodine: iodine supports thyroid-hormone-driven differentiation in brain (already mapped) tumour cells; iodine deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) and VEGF (already mapped) cascade in ATRT."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "ATRT copper: copper is a cofactor of antioxidant enzymes in macrophages (already mapped) and tumour cells; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "ATRT phosphorus: phosphorus fuels PI3K/AKT/mTOR (already mapped) signalling and energy metabolism in brain (already mapped) tumour cells; phosphorus excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in ATRT."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "ATRT carbon: carbon backbone of nucleotides in neurons (already mapped) and astrocytes (already mapped) sustains tumour metabolic reprogramming; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour growth in ATRT."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "ATRT chloride: chloride channels in astrocytes (already mapped) and endothelial cells (already mapped) modulate tumour microenvironment osmolarity; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour invasion in ATRT."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "ATRT hydrogen: hydrogen via ROS balance in macrophages (already mapped) and microglia (already mapped) modulates tumour oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour inflammatory cascade in ATRT."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "ATRT glp-1: GLP-1 on macrophages (already mapped) and microglia (already mapped) attenuates tumour inflammatory skewing; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour growth cascade in ATRT."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "ATRT angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes tumour angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "ATRT rankl: RANKL in macrophages (already mapped) and microglia (already mapped) modulates bone-immune tumour axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour inflammatory cascade in ATRT."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "ATRT fibronectin: Fibronectin in rhabdoid tumor cells (already mapped) and macrophages (already mapped) scaffolds tumour ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour inflammatory cascade in ATRT."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "ATRT activin-a: activin-A from rhabdoid tumor cells (already mapped) and macrophages (already mapped) regulates tumour immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "ATRT cgrp: CGRP from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour inflammatory cascade in ATRT."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "ATRT calcitonin: calcitonin from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour calcium signalling; calcitonin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "ATRT substance-p: substance-P from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour neuroinflammation; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "ATRT insulin-receptor: insulin receptor on rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour metabolic axis; insulin-receptor excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "ATRT aldosterone: aldosterone from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour ion balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "ATRT androgen-receptor: androgen receptor on rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates hormonal tone; androgen-receptor dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in ATRT."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "ATRT norepinephrine: norepinephrine from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "ATRT adrenomedullin: adrenomedullin from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "ATRT bdnf: BDNF from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour neural tone; bdnf excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "ATRT osteopontin: osteopontin from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour immune tone; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT."
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
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Engineered cells are being aimed at it: CAR-T and related cell therapies against targets like B7-H3, delivered intrathecally for CNS tumours, are investigational for the dismal-prognosis rhabdoid tumours including AT/RT.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy has limited reach: despite a low mutational burden, some rhabdoid tumours carry immune infiltrate, so checkpoint inhibitors are explored in AT/RT, though responses so far are modest.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Craniospinal radiation scars cognition: the intensive radiotherapy needed to control AT/RT, especially craniospinal irradiation in older children, injures the hippocampus and leaves survivors with lasting neurocognitive deficits.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Extracranial spread to the lung: AT/RT can disseminate beyond the CNS to seed pulmonary metastases in the alveolar capillary bed, a marker of widespread and often fatal disease.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver metastasis: AT/RT, one of the few brain tumours that spreads outside the nervous system, can seed the hepatic lobule as part of disseminated rhabdoid disease.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Childhood cancers of the Li-Fraumeni spectrum: like AT/RT, osteosarcoma can arise in Li-Fraumeni syndrome from germline TP53 loss, linking a brain rhabdoid tumour and a bone sarcoma through shared tumour-suppressor failure.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — Two ways to break SWI/SNF: AT/RT loses the SMARCB1 subunit while ovarian clear cell carcinoma loses ARID1A—different subunits crippling the same SWI/SNF chromatin-remodelling complex.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — SMARCB1 beyond the brain: the same SMARCB1 loss defining AT/RT drives renal medullary carcinoma (in sickle-cell trait) and malignant rhabdoid tumour of the kidney, a family of SMARCB1-deficient cancers.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Metastatic spread: malignant rhabdoid tumours, including extracranial forms, can metastasise to bone, depositing in the cortical bone alongside their spread to lung and liver.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cyclin D1 dependence: loss of SMARCB1 derepresses cyclin D1, driving the CDK4/6-fuelled cell cycle and making ATRT cells dependent on this axis—the rationale for CDK4/6 inhibition.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Aberrant Wnt signalling: SMARCB1 loss can derepress Wnt/β-catenin target genes, an oncogenic signalling pathway contributing to rhabdoid tumour proliferation distinct from the cell-cycle axis.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Epigenetic contrast: like ATRT, IDH-mutant glioma is fundamentally an epigenetic disease, but driven by oncometabolite-mediated DNA hypermethylation rather than SWI/SNF chromatin-remodeller loss.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Growth signalling: SMARCB1 loss in ATRT activates PI3K/AKT signalling, driving the survival and proliferation that make this aggressive infant brain tumour so rapidly fatal.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the rapidly growing, hypoxic ATRT promotes the VEGF angiogenesis that feeds its aggressive expansion.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT reactivation maintains telomeres in ATRT cells, granting the limitless proliferation needed to sustain this fast-growing embryonal tumour.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — SHH subgroup: the ATRT-SHH molecular subgroup shows active sonic-hedgehog signalling through Smoothened, one of the distinct lineage programmes that SMARCB1 loss unleashes in these tumours.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Lineage signalling: Notch pathway activation features in ATRT subgroups, contributing to the aberrant neural-developmental programmes driving the tumour after loss of SWI/SNF repression.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Immunosuppressive niche: CCL2 recruits tumour-associated macrophages into the ATRT microenvironment, building the immunosuppressive milieu that hampers immune control of this aggressive infant tumour.
- `connects-to` → **[PTCH1](../../03-molecular/ptch1/README.md)** — In the ATRT-SHH subgroup the Hedgehog pathway is active at the PTCH1-SMO receptor level, the lineage program that SMARCB1 loss derepresses and a potential target for Hedgehog pathway inhibitors in this subgroup.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on ATRT cells follows CXCL12 gradients in the cerebrospinal fluid, contributing to the leptomeningeal dissemination that worsens the already dismal prognosis of these aggressive infant brain tumors.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — The intensive chemotherapy and radiation used against ATRT kill tumor cells through caspase-3-mediated apoptosis, the effector step whose evasion underlies the treatment resistance and frequent relapse of this tumor.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — SMARCB1 (SWI/SNF) loss can derepress endogenous retroelements whose double-stranded RNA and DNA activate innate sensing including cGAS-STING, a "viral mimicry" that EZH2 inhibition enhances to make ATRT more immunogenic.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — ATRT is epigenetically driven and divides into distinct DNA-methylation subgroups (TYR, SHH, MYC) with different biology and outcome, making DNA methylation both a classifier and a therapeutic axis in this SWI/SNF-deficient tumor.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — A subset of rhabdoid tumors upregulate FGFR signaling as SMARCB1 loss reshapes the enhancer landscape, an oncogenic pathway under study as a targetable vulnerability in ATRT.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — SMARCB1 loss derepresses the CDK4/6-cyclin-D-RB axis (all already mapped), and E2F1-driven transcription powers the aggressive proliferation of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR signaling (AKT and mTOR already mapped) is activated in ATRT and supports its growth, a targetable axis in this therapy-resistant infant brain tumor.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — High anti-apoptotic BCL-2 contributes to the chemoresistance of ATRT, a dependency that BH3-mimetic agents are being explored to exploit.
- `connects-to` → **[SUFU](../../03-molecular/sufu/README.md)** — SUFU negatively regulates GLI in the Sonic-Hedgehog pathway (PTCH1 and SMO already mapped), the pathway driving the SHH molecular subgroup of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss releases the PI3K-AKT-mTOR axis (all three already mapped), a growth-driving pathway exploited by the aggressive proliferation of ATRT.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK1/2 MAPK transduces receptor-tyrosine-kinase signals (FGFR already mapped) into the proliferative drive of ATRT, supporting its rapid growth.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) contributes to the proliferative and immunosuppressive program of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling modulates the tumor microenvironment and invasive behavior of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is expressed in rhabdoid tumors and contributes to their invasive and immunomodulatory phenotype.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — SMARCB1 loss in ATRT derepresses the cyclin-D-CDK4/6 axis (cyclin-D1 and CDK4/6 mapped), driving RB1 inactivation and the cell-cycle progression of the tumor.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of the immunologically variable atypical teratoid/rhabdoid tumor.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the differentiation block and microenvironment of the SMARCB1-deficient atypical teratoid/rhabdoid tumor.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-driven FOXO inactivation (PTEN, AKT, and PIK3CA already mapped) removes a pro-apoptotic brake in atypical teratoid/rhabdoid tumor.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the often immune-cold atypical teratoid/rhabdoid tumor must evade.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory tumor microenvironment of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the GLI and β-catenin stability (SHH/SMO and WNT already mapped) of the developmental-signaling programs of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in atypical teratoid/rhabdoid tumor.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling contributes to the invasive and survival signaling of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic vulnerabilities of the SMARCB1-deficient cells of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — YAP1-Hippo signaling, de-repressed by SMARCB1 loss, contributes to the proliferation of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor-cell survival and immune signaling of atypical teratoid/rhabdoid tumor.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy target: this poor-prognosis infant brain tumour is being explored for checkpoint and cellular immunotherapy (PD-1 already mapped), and MHC class II antigen presentation shapes the T-cell response in an otherwise immunologically cold tumour.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cellular immunotherapy: IL-2 drives the expansion of the engineered and endogenous T cells behind the CAR-T and adoptive approaches under investigation for atypical teratoid/rhabdoid tumour given its dismal outcomes with conventional therapy.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint blockade: CTLA-4 restrains anti-tumour T-cell activation, and blocking it, alongside PD-1, is part of the immunotherapy strategy being tested to overcome the immune evasion of atypical teratoid/rhabdoid tumour.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Chemotherapy anaemia: the intensive multi-agent chemotherapy for atypical teratoid/rhabdoid tumour is profoundly myelosuppressive, lowering haemoglobin and causing the anaemia and cytopenias that complicate treatment in these very young children.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: anthracyclines in the treatment regimens are cardiotoxic, and troponin elevation helps detect the myocardial injury that threatens the few long-term survivors of atypical teratoid/rhabdoid tumour.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis and oxidative stress: the high proliferative rate of this embryonal tumour, lysed by chemotherapy, releases purines catabolised by xanthine oxidase to uric acid, contributing to tumour-lysis risk and oxidative stress.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton craniospinal therapy: proton-beam radiotherapy spares the developing infant brain (already mapped) compared with photon (already mapped) craniospinal irradiation, an important consideration in the very young children with atypical teratoid/rhabdoid tumour.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1, CTLA-4 and CD8 already mapped), part of the immune evasion of this aggressive embryonal tumour.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the highly vascular atypical teratoid/rhabdoid tumour, part of its stromal microenvironment.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold immune microenvironment of atypical teratoid/rhabdoid tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of atypical teratoid/rhabdoid tumour.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the intensive multi-agent chemotherapy of atypical teratoid/rhabdoid tumour is myelosuppressive, causing anaemia (haemoglobin already mapped) that needs transfusion whose repeated support can load the young child with iron.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton-beam therapy: proton radiotherapy is used for atypical teratoid/rhabdoid tumour to deliver the tumour dose while sparing the developing brain of the young child, reducing the neurocognitive and growth toxicity.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy: the photon (X-ray) radiotherapy, often craniospinal, is part of the intensive multimodal treatment of atypical teratoid/rhabdoid tumour, balanced against the toxicity in the infant brain.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Tumour angiogenesis and stroma: PDGF drives the tumour angiogenesis (VEGF already mapped) and the stromal recruitment of atypical teratoid/rhabdoid tumour, part of its aggressive vascular biology.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Survivorship hypothalamic obesity: the craniospinal radiotherapy (photon already mapped) of ATRT can damage the hypothalamus, causing the leptin-resistant hypothalamic obesity of the survivors.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Survivorship metabolic syndrome: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic syndrome of the ATRT survivors after the craniospinal radiotherapy.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Anthracycline cardiotoxicity: the anthracycline chemotherapy of the intensive ATRT regimens causes the cardiotoxicity (troponin already mapped) of the heart, a survivorship concern in the infant.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, explored with the checkpoint (PD-1 already mapped) immunotherapy of ATRT.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the atypical teratoid/rhabdoid tumour.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Survivorship adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic syndrome of the ATRT survivors after the craniospinal radiotherapy.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the atypical teratoid/rhabdoid tumour.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the atypical teratoid/rhabdoid tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the atypical teratoid/rhabdoid tumour.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the atypical teratoid/rhabdoid tumour.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the atypical teratoid/rhabdoid tumour.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the immune microenvironment of the atypical teratoid/rhabdoid tumour.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory dimension of the atypical teratoid/rhabdoid tumour microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid (macrophage already mapped) recruitment into the atypical teratoid/rhabdoid tumour microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the atypical teratoid/rhabdoid tumour.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-TME axis: TSLP, from brain stromal cells and barrier epithelium, primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the immunosuppressive tumour microenvironment of atypical teratoid/rhabdoid tumour.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-tumour axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability and the inflammatory cytokine milieu of the tumour microenvironment of ATRT.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Survivorship-anaemia axis: erythropoietin supports the management of the anaemia from the craniospinal irradiation and the myelosuppressive chemotherapy in the treatment of atypical teratoid/rhabdoid tumour.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell TME axis: histamine, from mast cells (already mapped) in the ATRT tumour microenvironment, amplifies the vascular permeability, the angiogenesis (already mapped) and the immunosuppressive cytokine milieu of the tumour stroma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-survivorship axis: melatonin, via MT1/MT2 receptors on tumour cells and neural progenitors (already mapped), exerts antitumour and neuroprotective effects relevant to the craniospinal-radiation survivorship of ATRT.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 already mapped) whose activation contributes to the tumour-promoting neuroinflammation and the immunosuppressive complement dimension of ATRT.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — ATRT testosterone: testosterone, via androgen receptors on neurons (already mapped) and microglia (already mapped), modulates the TME; testosterone deficiency amplifies the T-cytotoxic (already mapped) and complement-C5 (already mapped) antitumour cascade impairment of ATRT.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — ATRT serotonin: serotonin, via 5-HT receptors on microglia (already mapped) and neurons (already mapped), modulates the neuroinflammatory TME; serotonin dysregulation amplifies the T-cytotoxic (already mapped) and mast-cell (already mapped) antitumour cascade of ATRT.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — ATRT prolactin: prolactin, via PRLR on microglia (already mapped) and T-cytotoxic cells (already mapped), modulates the neuroimmune TME; prolactin dysregulation amplifies the neuroinflammatory (neuron already mapped) and mast-cell (already mapped) tumour cascade of ATRT.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — ATRT oxytocin: oxytocin, via OXTR on microglia (already mapped) and T-cytotoxic cells (already mapped), attenuates the neuroinflammatory TME; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of ATRT.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — ATRT vasopressin: vasopressin, via V1aR on neurons (already mapped) and microglia (already mapped), modulates the neuroimmune TME of ATRT; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory tumour cascade of ATRT.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — ATRT selenium: selenium, as GPx in neurons (already mapped) and microglia (already mapped), scavenges ROS driving the neuroinflammatory TME; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour-promoting cascade of ATRT.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — ATRT sodium: sodium dysregulation in bone-marrow (already mapped) stroma and tumour cells amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) tumour-promoting cascade in ATRT.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — ATRT potassium: potassium regulates macrophage (already mapped) and tumour cell membrane function; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) and mTOR (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — ATRT zinc: zinc cofactors macrophage (already mapped) anti-tumour function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) and VEGF (already mapped) tumour-promoting cascade in ATRT.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — ATRT iodine: iodine supports thyroid-hormone-driven differentiation in brain (already mapped) tumour cells; iodine deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) and VEGF (already mapped) cascade in ATRT.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — ATRT copper: copper is a cofactor of antioxidant enzymes in macrophages (already mapped) and tumour cells; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — ATRT phosphorus: phosphorus fuels PI3K/AKT/mTOR (already mapped) signalling and energy metabolism in brain (already mapped) tumour cells; phosphorus excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in ATRT.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — ATRT carbon: carbon backbone of nucleotides in neurons (already mapped) and astrocytes (already mapped) sustains tumour metabolic reprogramming; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour growth in ATRT.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — ATRT chloride: chloride channels in astrocytes (already mapped) and endothelial cells (already mapped) modulate tumour microenvironment osmolarity; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour invasion in ATRT.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — ATRT hydrogen: hydrogen via ROS balance in macrophages (already mapped) and microglia (already mapped) modulates tumour oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour inflammatory cascade in ATRT.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — ATRT glp-1: GLP-1 on macrophages (already mapped) and microglia (already mapped) attenuates tumour inflammatory skewing; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour growth cascade in ATRT.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — ATRT angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes tumour angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — ATRT rankl: RANKL in macrophages (already mapped) and microglia (already mapped) modulates bone-immune tumour axis; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour inflammatory cascade in ATRT.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — ATRT fibronectin: Fibronectin in rhabdoid tumor cells (already mapped) and macrophages (already mapped) scaffolds tumour ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour inflammatory cascade in ATRT.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — ATRT activin-a: activin-A from rhabdoid tumor cells (already mapped) and macrophages (already mapped) regulates tumour immune-fibrotic balance; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — ATRT cgrp: CGRP from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour inflammatory cascade in ATRT.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — ATRT calcitonin: calcitonin from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour calcium signalling; calcitonin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — ATRT substance-p: substance-P from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour neuroinflammation; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — ATRT insulin-receptor: insulin receptor on rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour metabolic axis; insulin-receptor excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — ATRT aldosterone: aldosterone from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour ion balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — ATRT androgen-receptor: androgen receptor on rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates hormonal tone; androgen-receptor dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — ATRT norepinephrine: norepinephrine from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — ATRT adrenomedullin: adrenomedullin from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — ATRT bdnf: BDNF from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour neural tone; bdnf excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — ATRT osteopontin: osteopontin from rhabdoid tumor cells (already mapped) and macrophages (already mapped) modulates tumour immune tone; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade in ATRT.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^biegel-1999-ini1-atrt]: Biegel JA, Zhou JY, Rorke LB, Stenstrom C, Wainwright LM, Fogelgren B. Germ-line and acquired mutations of INI1 in atypical teratoid and rhabdoid tumors. *Cancer Res.* 1999;59(1):74-79. [PubMed 9892189](https://pubmed.ncbi.nlm.nih.gov/9892189/)
[^fruhwald-2020-atrt-subgroups]: Frühwald MC, Hasselblatt M, Nemes K, et al. Age and DNA methylation subgroup as potential treatment targets in children with atypical teratoid rhabdoid tumors. *Neuro Oncol.* 2020;22(7):1006-1017. [doi:10.1093/neuonc/noz244](https://doi.org/10.1093/neuonc/noz244) · [PubMed 31900478](https://pubmed.ncbi.nlm.nih.gov/31900478/)
