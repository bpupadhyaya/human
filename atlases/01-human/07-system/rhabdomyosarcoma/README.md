---
schema: human-scale-entry/v1
id: rhabdomyosarcoma
name: Rhabdomyosarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Rhabdomyosarcoma is the most common pediatric soft tissue sarcoma; embryonal (~60%, VAC backbone, 5-year FFS ~90% low-risk) and alveolar (~25%, PAX3/PAX7-FOXO1 fusions, high-risk) subtypes; VAC±irinotecan; RT; metastatic disease 5-year OS ~20-30%."
aliases: ["rhabdomyosarcoma", "RMS", "embryonal RMS", "alveolar RMS", "ERMS", "ARMS", "pediatric soft tissue sarcoma", "botryoid RMS"]
sources:
  - id: crist-2001-irs4-rms
    type: peer-reviewed
    cite: "Crist WM, Anderson JR, Meza JL, et al. Intergroup rhabdomyosarcoma study-IV: results for patients with nonmetastatic disease. J Clin Oncol. 2001;19(12):3091-3102."
    doi: "10.1200/JCO.2001.19.12.3091"
    pmid: "11408506"
    url: "https://doi.org/10.1200/JCO.2001.19.12.3091"
  - id: oberlin-2012-mmt95-rms
    type: peer-reviewed
    cite: "Oberlin O, Rey A, Sanchez de Toledo J, et al. Randomized comparison of intensified six-drug versus standard three-drug chemotherapy for high-risk nonmetastatic rhabdomyosarcoma and other chemotherapy-sensitive childhood soft tissue sarcomas. J Clin Oncol. 2012;30(19):2457-2465."
    doi: "10.1200/JCO.2011.39.3538"
    pmid: "22665546"
    url: "https://doi.org/10.1200/JCO.2011.39.3538"
cross_links:
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "PAX3-FOXO1 t(2;13) (~55% ARMS) and PAX7-FOXO1 t(1;13) (~20% ARMS) are the defining fusions of alveolar RMS; PAX3-FOXO1 confers worse prognosis than PAX7-FOXO1; fusion status is the most important molecular prognostic factor in RMS."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "PAX3-FOXO1 drives MYCN expression in ARMS; MYCN amplification in fusion-negative RMS → poor prognosis; MYC amplification in pleomorphic RMS; BET inhibitors suppress MYC/MYCN in RMS preclinically; CDK4 is also a downstream PAX3-FOXO1 target."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT is constitutively active in most RMS subtypes via PTEN deletion (~10%), PIK3CA mutation, or IGF2 overexpression; AKT inactivates FOXO1 → removes cell cycle arrest; CDK4/6 inhibitors and PI3K inhibitors are explored in combination for RMS."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "PAX3-FOXO1 transcriptionally activates MET (HGF receptor) → invasion in alveolar RMS; MET overexpression in >50% ARMS; crizotinib active in MET-expressing pediatric solid tumors; MET amplification is an additional adverse prognostic factor in fusion-positive ARMS."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Rhabdomyosarcoma — especially embryonal, in young children — is one of the sentinel soft-tissue sarcomas of Li-Fraumeni syndrome; germline TP53 should be considered in any child with RMS under 3 or with a suggestive family history, as it also signals radiation-sparing caution."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Embryonal RMS is driven by an IGF2/IGF1R autocrine loop: 11p15.5 loss of imprinting unleashes biallelic IGF2, which signals through IGF1R → PI3K-AKT-mTOR for proliferation and survival; IGF1R antibodies have been tried but show limited single-agent activity."
  - target: 01-human/03-molecular/dicer1
    relation: connects-to
    note: "DICER1 syndrome predisposes to embryonal rhabdomyosarcoma, classically of the uterine cervix and in pleuropulmonary blastoma–associated tumors; biallelic DICER1 disrupts miRNA processing, so a young woman's cervical botryoid RMS should prompt germline DICER1 testing."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "Rhabdomyosarcoma and Wilms tumor are both embryonal childhood cancers of arrested development — RMS from myogenic precursors, Wilms from kidney blastema — sharing the IGF2 driver: 11p15.5 loss of imprinting doubles IGF2, powering an IGF1R-PI3K-AKT-mTOR loop in both."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Rhabdomyosarcoma is the malignant tumor of skeletal-muscle lineage: cells express myogenic regulators (MYOD1, myogenin, desmin) yet fail to mature into myofibers, and it arises wherever muscle precursors exist — head/neck, GU tract, extremities, even sites with no muscle."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Rhabdomyosarcoma and neuroblastoma are both pediatric small-round-blue-cell tumors that look alike microscopically, but immunohistochemistry separates them: RMS expresses myogenic markers (desmin, myogenin), neuroblastoma neuroendocrine ones (synaptophysin, PHOX2B)."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Rhabdomyosarcoma and Ewing sarcoma are the two commonest small-round-blue-cell sarcomas of childhood: RMS shows skeletal-muscle (myogenin/MyoD) differentiation and PAX-FOXO1 fusions, while Ewing is undifferentiated with EWSR1-FLI1—told apart by immunostains."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Embryonal rhabdomyosarcoma is part of the DICER1 tumor spectrum: germline DICER1 loss disrupts microRNA processing and drives botryoid/embryonal RMS (often of the cervix) alongside pleuropulmonary blastoma and other tumors—so syndromic testing is warranted."
  - target: 01-human/07-system/noonan-syndrome
    relation: connects-to
    note: "As a RASopathy, Noonan syndrome modestly raises the risk of embryonal rhabdomyosarcoma: constitutive RAS-MAPK signaling that drives the syndrome also promotes myogenic tumor growth, one of the embryonal cancers (with JMML and neuroblastoma) seen in RASopathies."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Rhabdomyosarcoma and osteosarcoma are the commonest pediatric soft-tissue and bone sarcomas: RMS arises from skeletal-muscle precursors (PAX-FOXO1 or RAS-driven), osteosarcoma from osteoblasts making malignant osteoid—both high-grade, lung-metastasizing sarcomas."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Rhabdomyosarcoma and synovial sarcoma are both translocation-associated soft-tissue sarcomas of the young: alveolar RMS carries PAX3/7-FOXO1, while synovial sarcoma carries SS18-SSX—each a fusion-defined tumor that immunohistochemistry plus genetics distinguishes."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is integral to rhabdomyosarcoma's multimodal cure: because RMS is chemo- and radio-responsive, photon radiation provides local control of the primary after chemotherapy when surgery would be mutilating—key to curing most localized RMS."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "NF1 raises rhabdomyosarcoma risk: RAS-pathway overactivity from neurofibromin loss predisposes to this muscle-lineage sarcoma, so RMS in a child can be a clue to neurofibromatosis—one of several cancer syndromes (Li-Fraumeni, DICER1, Noonan) linked to RMS."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Rhabdomyosarcoma is a soft-tissue sarcoma of skeletal-muscle lineage: its primitive mesenchymal cells, related to fibroblasts, attempt myogenic differentiation (desmin, myogenin) yet never mature—so it is diagnosed by muscle markers despite a spindle/round-cell look."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 loss drives aggressive rhabdomyosarcoma: as part of Li-Fraumeni and acquired in sporadic tumors, p53 inactivation removes the damage checkpoint and worsens prognosis—linking RMS to the broader sarcoma-prone genome-guardian network."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy benefits children with rhabdomyosarcoma: head-and-neck and parameningeal tumors sit near eyes, brain and growth plates, so protons' lack of exit dose limits disfigurement, cognitive harm and second cancers in young survivors."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Parameningeal rhabdomyosarcoma threatens the nervous system: tumors of the head and neck can erode the skull base and invade the meninges, causing cranial-nerve palsies and CNS spread—so this site carries a worse prognosis and needs CNS-directed treatment."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is rhabdomyosarcoma's main metastatic site: this aggressive childhood soft-tissue sarcoma spreads hematogenously to the lungs (and marrow and bone), so chest imaging stages it and pulmonary metastases mark high-risk disease."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Rhabdomyosarcoma can flood the bone marrow: alveolar RMS especially metastasizes to marrow so heavily it mimics acute leukemia on a blood smear, so marrow involvement is staged carefully and signals high-risk, disseminated disease."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Rhabdomyosarcoma is the malignant face of developing skeletal muscle: it shows the cross-striations and myogenic markers (MyoD, myogenin) of muscle cells, distinguishing it from tumors of cardiac muscle (cardiomyocytes) or smooth muscle."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Rhabdomyosarcoma signals through PI3K-AKT-mTOR: IGF and receptor-kinase inputs converge on mTOR to drive growth, especially in embryonal tumors, so mTOR inhibitors have been tested to add to chemotherapy in this childhood sarcoma."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Embryonal rhabdomyosarcoma is often RAS-driven: unlike the fusion-positive alveolar type, embryonal RMS frequently carries NRAS/KRAS mutations that switch on RAS-MAPK growth, defining a biologically distinct, generally better-prognosis subtype."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "Rhabdomyosarcoma can run on Hedgehog through SMO: embryonal RMS often shows Hedgehog pathway activation, and Gorlin-syndrome patients are prone to it, so smoothened-driven signaling is a developmental pathway hijacked by this muscle cancer."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Rhabdomyosarcoma is infiltrated by tumor-associated macrophages: these cells populate the sarcoma's stroma and promote growth and immune escape, and a macrophage-rich infiltrate is linked to worse outcomes in this childhood cancer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia makes rhabdomyosarcoma more aggressive: the fast-growing muscle sarcoma outpaces its blood supply, and low oxygen drives invasion, metastasis and resistance, contributing to its tendency to spread to the lungs."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Parameningeal rhabdomyosarcoma threatens the brain: tumors near the skull base and meninges can invade the central nervous system directly, a high-risk location that demands intensive radiation and CNS-directed treatment."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Rhabdomyosarcoma largely evades cytotoxic T cells: with few mutations and an immunosuppressive microenvironment it resists checkpoint drugs, so engineered T-cell therapies are explored to direct killing at this childhood sarcoma."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Rhabdomyosarcoma often strikes the orbit: it is the commonest soft-tissue sarcoma of the eye socket in children, causing rapidly progressive proptosis that demands urgent diagnosis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Rhabdomyosarcoma is muscle gone wrong, down to its calcium: the rhabdomyoblasts switch on skeletal-muscle genes and the calcium-driven contraction machinery, expressing markers like desmin and myogenin that confirm the diagnosis."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Rhabdomyosarcoma builds its blood supply through endothelial cells: VEGF from the tumor recruits new vessels to feed its rapid growth, a feature studied for anti-angiogenic therapy."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy proves a tumor is rhabdomyosarcoma: the malignant cells assemble crude sarcomeres — thick and thin filaments aligned into Z-bands — the ultrastructural sign of skeletal-muscle differentiation that named the cancer."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Pelvic rhabdomyosarcoma threatens the kidney from afar: bladder, prostate, and vaginal tumors fill the pelvis and compress the ureters, backing urine up into the kidneys as obstructive hydronephrosis that can damage them if not relieved."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Rhabdomyosarcoma can spread to the liver: alongside its favored routes to lung, bone, and marrow, the bloodborne tumor seeds hepatic metastases in widespread disease, a marker of the high-risk, hardest-to-cure cases."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The VAC backbone frays the nerves: vincristine, the 'V' of the standard rhabdomyosarcoma regimen, jams the microtubule transport of peripheral neurons, causing a dose-limiting neuropathy with foot drop, constipation, and tingling."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Intensified chemotherapy can scar the heart: when doxorubicin is added for higher-risk rhabdomyosarcoma, its cumulative cardiotoxicity threatens a late cardiomyopathy that survivors are monitored for long after cure."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "The bladder is a common cradle for childhood RMS: embryonal (botryoid) rhabdomyosarcoma often springs from the bladder and prostate, a sarcoma of muscle quite unlike the urothelial bladder cancer that strikes adults."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains prove the muscle lineage: nuclear myogenin and MyoD1 with cytoplasmic desmin confirm a tumor is rhabdomyosarcoma, and diffuse myogenin especially flags the aggressive alveolar, PAX-FOXO1-fusion subtype on biopsy."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The VAC regimen empties the marrow: vincristine, actinomycin-D, and cyclophosphamide are heavily myelosuppressive, dropping neutrophil counts so that febrile neutropenia is a recurring danger through a child's rhabdomyosarcoma treatment."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "RMS favors the genitourinary tract: paratesticular, vaginal (botryoid), and uterine tumors are classic embryonal sites, so the reproductive organs are both where many of these sarcomas start and what surgery and radiation must try to spare."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Ifosfamide injures the kidney's salt handling: the alkylating drug central to RMS chemotherapy damages the proximal tubule into a Fanconi-like state that wastes magnesium and phosphate, electrolytes replaced through the course of treatment."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Fusion-positive RMS amplifies the cell-cycle engine: alveolar tumors driven by PAX3-FOXO1 often co-amplify CDK4 and MDM2, pushing cells past the cycle checkpoint and making CDK4/6 inhibition an actively studied target."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The multi-drug chemotherapy empties the marrow: the vincristine-actinomycin-cyclophosphamide backbone suppresses platelet production into thrombocytopenia, adding bleeding risk to the long, intensive treatment these tumors demand."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "Amplification marks the worst form: the aggressive alveolar subtype carrying the PAX3-FOXO1 fusion often also amplifies MYCN, a proliferation driver that helps explain its high-risk behavior and resistance to standard chemotherapy."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate killers are recruited against it: rhabdomyosarcoma is hard for T cells to see, so natural killer cell–based and engineered cell therapies are explored to attack a tumor that resists checkpoint immunotherapy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The tumor cloaks itself in suppression: regulatory T cells accumulate in the rhabdomyosarcoma microenvironment and blunt anti-tumor immunity, part of the immune-cold profile that has frustrated immunotherapy in this childhood sarcoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle loss marks the fusion-negative tumors: CDKN2A deletion is recurrent in embryonal rhabdomyosarcoma, releasing CDK4/6 to drive proliferation and complementing the cell-cycle amplicons of the fusion-positive subtype."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Tumor and treatment hurt the nerves: head-and-neck, paraspinal, and pelvic rhabdomyosarcomas compress nerves, and vincristine adds a peripheral neuropathy, together a real pain burden in these children."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Intensive chemotherapy invites sepsis: the VAC regimen's deep neutropenia leaves children with rhabdomyosarcoma prone to febrile neutropenia and bloodstream infection through the long treatment course."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "An activating receptor signals through it: FGFR4 mutations recurrent in rhabdomyosarcoma drive STAT3 activation that promotes survival and proliferation, marking the pathway as a candidate target in fusion-positive disease."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its cure can seed a later leukemia: the alkylators and topoisomerase poisons in the VAC backbone carry a small risk of therapy-related acute myeloid leukemia years after rhabdomyosarcoma treatment."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Ifosfamide scars the young kidney: the alkylator central to many rhabdomyosarcoma regimens is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment in treated children."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracyclines and alkylators strain the heart: doxorubicin in high-risk rhabdomyosarcoma and high-dose cyclophosphamide are cardiotoxic, risking a cardiomyopathy and heart failure that can surface during childhood-cancer survivorship."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Intensive chemotherapy opens the lung to mold: the deep neutropenia from rhabdomyosarcoma's multi-agent regimens lets inhaled Aspergillus invade as pulmonary aspergillosis in these young patients."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A childhood cancer and its long therapy strain the mind: the diagnosis in children and teens, disfiguring surgery and prolonged treatment contribute to depression and distress in patients and families."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Wide resection in irradiated tissue heals slowly: the local control of rhabdomyosarcoma combines extensive surgery with radiation, and the irradiated, chemotherapy-suppressed bed leaves wounds prone to breakdown."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Chemotherapy reawakens shingles: the multi-agent regimens for rhabdomyosarcoma suppress a child's immunity, allowing latent or primary varicella-zoster to cause severe disseminated infection."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A childhood cancer with relapse risk breeds lasting worry: disfiguring surgery, intensive therapy and long survivorship surveillance after rhabdomyosarcoma foster chronic anxiety in survivors and families."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to the lungs: like other sarcomas, rhabdomyosarcoma metastasises preferentially to the lungs, so pulmonary metastases shape its staging, treatment and prognosis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Head-and-neck radiation and chemo hit the glands: parameningeal and orbital radiotherapy for rhabdomyosarcoma can damage the hypothalamus and pituitary, and chemotherapy impairs future fertility."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Pelvic tumours and chemo disturb the gut: genitourinary and pelvic rhabdomyosarcoma can obstruct the bowel, and its multi-agent chemotherapy causes mucositis, nausea and hepatotoxicity."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Unlike most sarcomas it spreads to nodes: rhabdomyosarcoma, especially the alveolar subtype, involves regional lymph nodes, so nodal sampling is part of its staging."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its drugs and pelvic tumours injure the urinary tract: ifosfamide and cyclophosphamide cause haemorrhagic cystitis and a Fanconi-like tubulopathy, and genitourinary tumours can obstruct the urinary tract."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its chemotherapy can scar the heart: the doxorubicin and dactinomycin in rhabdomyosarcoma regimens carry a cardiotoxicity risk in the children who receive them."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Therapy suppresses immunity: the intensive vincristine-actinomycin-cyclophosphamide chemotherapy for rhabdomyosarcoma is profoundly immunosuppressive, raising opportunistic-infection risk."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Treatment marks the skin: chemotherapy causes alopecia and mucositis, and radiotherapy produces dermatitis over the treated site, with rare cutaneous rhabdomyosarcoma."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "New agents target its fusion biology: research pursues drugs against the PAX3/7-FOXO1 fusion and downstream pathways of alveolar rhabdomyosarcoma beyond conventional chemotherapy."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "VAC is the backbone: rhabdomyosarcoma is treated with intensive multi-agent chemotherapy — vincristine, actinomycin-D and cyclophosphamide — alongside surgery and radiotherapy, the regimen that turned a once-fatal childhood sarcoma curable."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "A contrasting mesenchymal tumour: both are soft-tissue sarcomas, but GIST is a KIT/PDGFRA-driven adult tumour exquisitely sensitive to imatinib, whereas rhabdomyosarcoma is a paediatric myogenic cancer relying on cytotoxic chemotherapy."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunologically cold: rhabdomyosarcoma has a low mutational burden and sparse T-cell infiltrate, so checkpoint blockade that transformed melanoma and lung cancer shows little activity, keeping chemotherapy central."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Its metastases seed the lung: rhabdomyosarcoma spreads to the lungs (and bone marrow), studding the alveolar parenchyma with deposits, so chest imaging stages the disease and lung involvement worsens the prognosis."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "An SHH-driven childhood tumour: embryonal rhabdomyosarcoma can be driven by Hedgehog signalling and occurs in Gorlin syndrome, whose germline PTCH1 loss activates the SMO pathway this sarcoma can also exploit."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Two embryonal tumours of childhood: rhabdomyosarcoma and medulloblastoma are densely cellular paediatric cancers that can both run on Hedgehog/SHH signalling, arising in muscle lineage and cerebellum respectively."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Embryonal childhood cancers compared: rhabdomyosarcoma and retinoblastoma are both classic paediatric tumours treated on cooperative-group protocols, contrasting a muscle-lineage sarcoma with an RB1-driven eye cancer."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone-marrow metastasis: rhabdomyosarcoma, especially the alveolar subtype, spreads to bone and bone marrow, and marrow involvement mimicking leukaemia carries a grim prognosis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Parameningeal invasion: head-and-neck rhabdomyosarcoma near the skull base invades along nerves toward the meninges, causing cranial-nerve palsies and a worse, CNS-threatening outlook."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Sarcoma botryoides of the genital tract: embryonal rhabdomyosarcoma arises in the vagina and cervix of young girls as grape-like botryoid masses, often DICER1-driven—a sarcoma of the same region as cervical carcinoma."
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "A deep soft-tissue differential: like rhabdomyosarcoma, a desmoid tumour presents as an infiltrative soft-tissue mass, the two sitting in the differential of an enlarging extremity or trunk lesion despite very different biology."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "NF1 sarcomas: neurofibromatosis type 1 predisposes to both rhabdomyosarcoma in childhood and MPNST from nerve sheaths, two RAS-pathway soft-tissue sarcomas of the syndrome."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Targetable kinase: FGFR4 activating mutations and amplification drive a subset of rhabdomyosarcomas, marking an actionable receptor tyrosine kinase."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo activation: Hippo-YAP signalling drives fusion-negative embryonal rhabdomyosarcoma, sustaining proliferation and blocking muscle differentiation."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Differentiation block: Notch signalling maintains the undifferentiated, proliferative state of rhabdomyosarcoma, preventing the myogenic maturation its cells are poised toward."
---

# Rhabdomyosarcoma

## Overview

**Rhabdomyosarcoma (RMS)** is the most common **pediatric soft tissue sarcoma**, accounting for ~3-4% of all childhood cancers and ~50% of pediatric soft tissue sarcomas. RMS arises from primitive mesenchymal precursors committed to the skeletal muscle lineage (expressing myogenic TFs: MYOD1, myogenin), though it can occur in sites without skeletal muscle (bladder, vagina, middle ear) — reflecting the myogenic progenitor origin from embryonic mesoderm. The two major clinically relevant histological subtypes are **embryonal RMS (ERMS, ~60%)** and **alveolar RMS (ARMS, ~25%)**: ERMS is driven by complex copy number alterations and loss of heterozygosity at 11p15 (IGF2 imprinting loss); ARMS is defined by PAX3-FOXO1 or PAX7-FOXO1 chromosomal translocations that create chimeric oncogenic transcription factors. Treatment is multimodal: the **VAC backbone** (vincristine+actinomycin D+cyclophosphamide) established by the Intergroup Rhabdomyosarcoma Studies (IRS) remains the cornerstone [^crist-2001-irs4-rms]; radiation therapy is critical for residual/unresected disease; intensified regimens (VAC+irinotecan, six-drug therapy) have been explored for high-risk disease but do not clearly improve outcomes in metastatic RMS [^oberlin-2012-mmt95-rms].

**Epidemiology:**
- ~350-400 cases/year USA; ~5,000/year globally
- Median age: ~5 years (ERMS bimodal: peak <5 and 10-17); ~16 years for ARMS
- Male predominance (~1.4:1 overall); orbital RMS: female slight predominance
- Primary sites: head/neck (~35%), genitourinary (~25%), extremity (~20%), trunk/retroperitoneum (~15%)
- ~15-20% have metastatic disease at diagnosis; 5-year OS: localized ~70-80%, metastatic ~20-30%

## Structure

### Molecular classification

**Embryonal RMS (ERMS, ~60%):**
- Molecular: No fusion gene; 11p15.5 loss of heterozygosity → IGF2 imprinting loss → IGF2 overexpression → IGF1R signaling; complex karyotype; gain of whole chromosomes (7, 8, 13); NRAS mutations (~10%), KRAS mutations, PIK3CA mutations; MYOD1 L122R in sclerosing variant; CTNNB1 mutations rare; DICER1 mutations in embryonal pleural pulmonary blastoma-associated RMS
- Prognosis: Generally better than ARMS; low-risk ERMS: 5-year FFS ~90%; intermediate-risk: ~65-80%
- Location: Head/neck (orbital — best prognosis, parameningeal — high-risk), genitourinary (bladder/prostate, vagina/uterus), extremity

**Alveolar RMS (ARMS, ~25%):**
- Molecular: PAX3-FOXO1 t(2;13)(q35;q14) ~55%; PAX7-FOXO1 t(1;13)(p36;q14) ~20%; fusion-negative ARMS ~25% (behaves like ERMS molecularly and prognostically); FISH for FOXO1 rearrangement is essential for all histologically ARMS and RMS-ambiguous cases
- Prognosis: Fusion-positive ARMS (especially PAX3-FOXO1): 5-year OS ~50-60%; PAX7-FOXO1: ~70-75%; fusion-negative ARMS: ~75% (reclassified as ERMS in practice)
- Location: Extremity, trunk, parameningeal — typically non-genitourinary

**Sclerosing/Spindle Cell RMS:**
- Molecular: MYOD1 L122R mutation (~25%); VGLL2 and NCOA2 fusions (in infantile spindle cell variant — good prognosis); SRF-NCOA2 fusion
- Prognosis: Highly variable; MYOD1 L122R → poor prognosis despite relatively low-grade histological appearance; NCOA2-fused: excellent prognosis in infants

**Pleomorphic RMS:**
- Adults (rare in children); no fusion genes; complex karyotype; myogenic markers (desmin, myogenin) positive; very poor prognosis (5-year OS <20%); treated as adult high-grade sarcoma (gemcitabine/docetaxel, ifos/doxo)

### Histology and immunophenotype

**ERMS:** Hypercellular areas alternating with loosely myxoid stroma; rhabdomyoblasts (elongated, tadpole-shaped cells with abundant eosinophilic cytoplasm); cross-striations may be visible; variable differentiation; **botryoid RMS** (variant): polypoid grape-like clusters beneath mucosal surface in hollow organs (bladder, vagina, nasopharynx) → "cambium layer" (hypercellular zone immediately deep to surface epithelium) → diagnostic feature.

**ARMS:** Pseudo-alveolar spaces separated by fibrovascular septa; loosely cohesive small round blue cells lining the septa like a respiratory alveolus; solid variant (may lack alveolar pattern) → FISH essential.

**Immunophenotype:**
- Desmin+, vimentin+ (mesenchymal)
- Myogenin+ (nuclear; more diffuse in ARMS — ~75% cells; focal in ERMS — <10% cells)
- MYOD1+ (nuclear; present in all variants)
- MyoD1 (protein) and Myogenin are the most diagnostic IHC markers for any RMS type
- CD99 variable (positive in ~50% — can cause confusion with Ewing)
- ALK negative (unlike inflammatory myofibroblastic tumor)
- SMA variable, S100 negative

## Function

### Pathophysiology

**RMS as an arrested myogenic differentiation:**
Normal skeletal muscle regeneration: satellite cells (Pax7+, Myf5+) activate → MYOD1 expression → myoblast → MYOG (myogenin) → myocyte → fusion → myofiber; PAX3-FOXO1 recapitulates early myogenic gene activation (MYOD1, FGFR4, MET) without allowing terminal differentiation → cells express early myogenic markers but cannot complete the differentiation program → arrested blast state that proliferates.

**IGF2-IGF1R autocrine in ERMS:**
11p15 LOH → biallelic IGF2 expression → autocrine IGF2 → IGF1R → PI3K-AKT-mTOR → ERMS proliferation and survival; FOXO1 is inactivated by AKT in ERMS → loss of FOXO1-mediated differentiation signals; PI3K inhibitors and IGF1R antibodies explored but have limited single-agent activity.

**PAX3-FOXO1 myogenic reprogramming:**
PAX3-FOXO1 hijacks the PAX3 myogenic regulatory network → activates MYOD1 enhancers → MYOD1 expression without differentiation context (because PAX3-FOXO1 also represses myogenin's differentiation program through competitive binding); the result: high MYOD1 with low differentiated muscle gene expression → proliferative blast state; CDK4 overexpression from PAX3-FOXO1 → sustained cell cycle progression.

## Pathology

### Staging — IRS grouping

| IRS Group | Definition |
|----------|-----------|
| I | Complete resection, no microscopic residual |
| II | Regional disease; complete resection with microscopic residual (Group IIA) or positive regional lymph nodes, completely resected (Group IIB/C) |
| III | Incomplete resection with gross residual disease |
| IV | Distant metastases at onset |

**TNM staging** also applied (T1/T2 × a/b + N + M); combined to create risk groups for treatment.

**Risk groups (COG):**
- **Low risk:** Stage 1 or 2, Group I/II, ERMS histology; or Stage 1, Group I/II, ARMS; 5-year FFS ~90%
- **Intermediate risk:** Stage 1-3, Group III, ERMS; or Stage 2-3, Group I/II/III, ARMS; or Stage 4 <10 years ERMS; 5-year FFS ~55-65%
- **High risk:** Stage 4 (metastatic), any age, ARMS; or Stage 4, ≥10 years; 5-year FFS ~20-30%

### Treatment

**Chemotherapy backbone — VAC:**
Vincristine (1.5 mg/m² IV weekly, max 2 mg) + actinomycin D (0.045 mg/kg or 1.5 mg/m² IV Days 1-5, max 2 mg) + cyclophosphamide (2.2 g/m² IV) every 3 weeks; mesna uroprotection; IRS-IV established VAC as standard backbone; IRS-IV (N=883): randomized comparison of VAC vs VAI (ifosfamide substituted) vs VIE (ifosfamide+etoposide) → no significant difference in outcome, confirming VAC as standard [^crist-2001-irs4-rms]; G-CSF support required for subsequent courses.

**VAC + irinotecan (intermediate/high-risk):**
Irinotecan added to VAC for intermediate and high-risk RMS: ARST0431 (high-risk, N=109): VAC/IE with vincristine, irinotecan → 3-year EFS ~38% for metastatic ARMS; ARST0531 (intermediate-risk): VAC+irinotecan improved 5-year EFS slightly vs VAC alone; current COG standard incorporates irinotecan for intermediate/high-risk RMS.

**Intensified regimens (six-drug):**
SIOP MMT95 (Oberlin 2012): randomized comparison 6-drug (IVA+vincristine/doxorubicin/etoposide, 6-drug) vs 3-drug (IVA) in high-risk non-metastatic RMS → no benefit from intensification (5-year EFS 64% vs 64%); intensification not superior to standard 3-drug for non-metastatic high-risk RMS [^oberlin-2012-mmt95-rms].

**Radiation therapy:**
RT is mandatory for all Group II-IV disease and Group I ARMS:
- Embryonal low-risk Group I: VAC alone × 24 weeks, no RT
- Orbital/parameningeal: 45-50.4 Gy (IMRT or proton preferred); CNS extension → craniospinal RT
- Extremity: 45-50.4 Gy; proton beam to spare growth plate/normal tissue
- Bladder/prostate: 45 Gy proton; if complete resection achievable by surgery → surgery preferred to preserve bladder function
- Whole-lung: 15-18 Gy for lung metastases (concurrent with maintenance chemo)

**Surgery:**
Maximal safe resection with negative margins (R0) wherever achievable without mutilation; for orbital, parameningeal, bladder-prostate, vaginal primaries — extensive upfront surgery avoided; preoperative (induction) chemotherapy to shrink tumor → delayed definitive surgery (DSS) after response evaluation; second-look surgery after induction to assess response and achieve resection.

**Novel/investigational agents:**
- **CDK4/6 inhibitors (palbociclib):** PAX3-FOXO1 → CDK4; SARC037: palbociclib in pediatric RMS — Phase 1 data favorable; ongoing Phase 2 randomized
- **Anti-GD2 (dinutuximab):** GD2 expressed on RMS; COG ANBL1422: dinutuximab + irinotecan+temsirolimus in pediatric solid tumors including RMS
- **MET inhibitors (crizotinib):** COG ADVL1312: crizotinib Phase 1 including RMS cohort; RMS responses observed in MET-positive tumors
- **Anti-PD-1/PD-L1:** PD-L1 expressed in ~40% RMS; pembrolizumab Phase 2 in pediatric solid tumors including RMS; limited data; genomically quiet ERMS may be less immunogenic
- **Cabozantinib:** Multi-TKI (MET/VEGFR/AXL/RET); Phase 2 in R/R pediatric solid tumors
- **BET inhibitors:** Phase 1 studies evaluating BRD4/MYC suppression in ARMS; combination with CDK4/6 inhibitors explored

**Relapsed RMS:**
- Topotecan+cyclophosphamide (TC): ORR ~30-35%; standard salvage
- Irinotecan+temozolomide (IT): ORR ~25%
- Gemcitabine+docetaxel: ORR ~15-20% in pediatric RMS; better in adult pleomorphic RMS
- Vinorelbine+cyclophosphamide (metronomic): modest ORR; less toxicity; continuous low-dose oral
- Allo-SCT: No established role in R/R RMS; high TRM without demonstrated survival benefit

### Long-term effects

- **Infertility:** Cyclophosphamide → gonadal damage; cryopreservation recommended; LMWD (lowest-effective-dose) cyclophosphamide strategies
- **Growth:** RT to bone → growth plate damage → limb length discrepancy, scoliosis
- **Bladder function:** Pelvic/bladder RT → urinary dysfunction; bladder-prostate RMS — bladder-preservation approach has reduced late urinary morbidity substantially
- **Secondary malignancy:** Alkylator → MDS/AML; RT field → secondary sarcoma (10+ year latency)
- **Cardiac:** Cyclophosphamide → hemorrhagic cystitis (with mesna prophylaxis); late cardiomyopathy if doxorubicin used (most protocols minimize doxorubicin in RMS)

## Connections

- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — PAX3-FOXO1 t(2;13) (~55% ARMS) and PAX7-FOXO1 t(1;13) (~20% ARMS) are the defining fusions of alveolar RMS; PAX3-FOXO1 confers worse prognosis than PAX7-FOXO1; fusion status is the most important molecular prognostic factor in RMS.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — PAX3-FOXO1 drives MYCN expression in ARMS; MYCN amplification in fusion-negative RMS → poor prognosis; MYC amplification in pleomorphic RMS; BET inhibitors suppress MYC/MYCN in RMS preclinically; CDK4 is also a downstream PAX3-FOXO1 target.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT is constitutively active in most RMS subtypes via PTEN deletion (~10%), PIK3CA mutation, or IGF2 overexpression; AKT inactivates FOXO1 → removes cell cycle arrest; CDK4/6 inhibitors and PI3K inhibitors are explored in combination for RMS.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — PAX3-FOXO1 transcriptionally activates MET (HGF receptor) → invasion in alveolar RMS; MET overexpression in >50% ARMS; crizotinib active in MET-expressing pediatric solid tumors; MET amplification is an additional adverse prognostic factor in fusion-positive ARMS.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Rhabdomyosarcoma — especially embryonal, in young children — is one of the sentinel soft-tissue sarcomas of Li-Fraumeni syndrome; germline TP53 should be considered in any child with RMS under 3 or with a suggestive family history, as it also signals radiation-sparing caution.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Embryonal RMS is driven by an IGF2/IGF1R autocrine loop: 11p15.5 loss of imprinting unleashes biallelic IGF2, which signals through IGF1R → PI3K-AKT-mTOR for proliferation and survival; IGF1R antibodies have been tried but show limited single-agent activity.
- `connects-to` → **[DICER1](../../03-molecular/dicer1/README.md)** — DICER1 syndrome predisposes to embryonal rhabdomyosarcoma, classically of the uterine cervix and in pleuropulmonary blastoma–associated tumors; biallelic DICER1 disrupts miRNA processing, so a young woman's cervical botryoid RMS should prompt germline DICER1 testing.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — Rhabdomyosarcoma and Wilms tumor are both embryonal childhood cancers of arrested development — RMS from myogenic precursors, Wilms from kidney blastema — sharing the IGF2 driver: 11p15.5 loss of imprinting doubles IGF2, powering an IGF1R-PI3K-AKT-mTOR loop in both.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Rhabdomyosarcoma is the malignant tumor of skeletal-muscle lineage: cells express myogenic regulators (MYOD1, myogenin, desmin) yet fail to mature into myofibers, and it arises wherever muscle precursors exist — head/neck, GU tract, extremities, even sites with no muscle.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Rhabdomyosarcoma and neuroblastoma are both pediatric small-round-blue-cell tumors that look alike microscopically, but immunohistochemistry separates them: RMS expresses myogenic markers (desmin, myogenin), neuroblastoma neuroendocrine ones (synaptophysin, PHOX2B).
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Rhabdomyosarcoma and Ewing sarcoma are the two commonest small-round-blue-cell sarcomas of childhood: RMS shows skeletal-muscle (myogenin/MyoD) differentiation and PAX-FOXO1 fusions, while Ewing is undifferentiated with EWSR1-FLI1—told apart by immunostains.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Embryonal rhabdomyosarcoma is part of the DICER1 tumor spectrum: germline DICER1 loss disrupts microRNA processing and drives botryoid/embryonal RMS (often of the cervix) alongside pleuropulmonary blastoma and other tumors—so syndromic testing is warranted.
- `connects-to` → **[Noonan Syndrome](../noonan-syndrome/README.md)** — As a RASopathy, Noonan syndrome modestly raises the risk of embryonal rhabdomyosarcoma: constitutive RAS-MAPK signaling that drives the syndrome also promotes myogenic tumor growth, one of the embryonal cancers (with JMML and neuroblastoma) seen in RASopathies.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Rhabdomyosarcoma and osteosarcoma are the commonest pediatric soft-tissue and bone sarcomas: RMS arises from skeletal-muscle precursors (PAX-FOXO1 or RAS-driven), osteosarcoma from osteoblasts making malignant osteoid—both high-grade, lung-metastasizing sarcomas.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Rhabdomyosarcoma and synovial sarcoma are both translocation-associated soft-tissue sarcomas of the young: alveolar RMS carries PAX3/7-FOXO1, while synovial sarcoma carries SS18-SSX—each a fusion-defined tumor that immunohistochemistry plus genetics distinguishes.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is integral to rhabdomyosarcoma's multimodal cure: because RMS is chemo- and radio-responsive, photon radiation provides local control of the primary after chemotherapy when surgery would be mutilating—key to curing most localized RMS.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — NF1 raises rhabdomyosarcoma risk: RAS-pathway overactivity from neurofibromin loss predisposes to this muscle-lineage sarcoma, so RMS in a child can be a clue to neurofibromatosis—one of several cancer syndromes (Li-Fraumeni, DICER1, Noonan) linked to RMS.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Rhabdomyosarcoma is a soft-tissue sarcoma of skeletal-muscle lineage: its primitive mesenchymal cells, related to fibroblasts, attempt myogenic differentiation (desmin, myogenin) yet never mature—so it is diagnosed by muscle markers despite a spindle/round-cell look.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 loss drives aggressive rhabdomyosarcoma: as part of Li-Fraumeni and acquired in sporadic tumors, p53 inactivation removes the damage checkpoint and worsens prognosis—linking RMS to the broader sarcoma-prone genome-guardian network.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy benefits children with rhabdomyosarcoma: head-and-neck and parameningeal tumors sit near eyes, brain and growth plates, so protons' lack of exit dose limits disfigurement, cognitive harm and second cancers in young survivors.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Parameningeal rhabdomyosarcoma threatens the nervous system: tumors of the head and neck can erode the skull base and invade the meninges, causing cranial-nerve palsies and CNS spread—so this site carries a worse prognosis and needs CNS-directed treatment.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is rhabdomyosarcoma's main metastatic site: this aggressive childhood soft-tissue sarcoma spreads hematogenously to the lungs (and marrow and bone), so chest imaging stages it and pulmonary metastases mark high-risk disease.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Rhabdomyosarcoma can flood the bone marrow: alveolar RMS especially metastasizes to marrow so heavily it mimics acute leukemia on a blood smear, so marrow involvement is staged carefully and signals high-risk, disseminated disease.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Rhabdomyosarcoma is the malignant face of developing skeletal muscle: it shows the cross-striations and myogenic markers (MyoD, myogenin) of muscle cells, distinguishing it from tumors of cardiac muscle (cardiomyocytes) or smooth muscle.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Rhabdomyosarcoma signals through PI3K-AKT-mTOR: IGF and receptor-kinase inputs converge on mTOR to drive growth, especially in embryonal tumors, so mTOR inhibitors have been tested to add to chemotherapy in this childhood sarcoma.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Embryonal rhabdomyosarcoma is often RAS-driven: unlike the fusion-positive alveolar type, embryonal RMS frequently carries NRAS/KRAS mutations that switch on RAS-MAPK growth, defining a biologically distinct, generally better-prognosis subtype.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — Rhabdomyosarcoma can run on Hedgehog through SMO: embryonal RMS often shows Hedgehog pathway activation, and Gorlin-syndrome patients are prone to it, so smoothened-driven signaling is a developmental pathway hijacked by this muscle cancer.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Rhabdomyosarcoma is infiltrated by tumor-associated macrophages: these cells populate the sarcoma's stroma and promote growth and immune escape, and a macrophage-rich infiltrate is linked to worse outcomes in this childhood cancer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia makes rhabdomyosarcoma more aggressive: the fast-growing muscle sarcoma outpaces its blood supply, and low oxygen drives invasion, metastasis and resistance, contributing to its tendency to spread to the lungs.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Parameningeal rhabdomyosarcoma threatens the brain: tumors near the skull base and meninges can invade the central nervous system directly, a high-risk location that demands intensive radiation and CNS-directed treatment.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Rhabdomyosarcoma largely evades cytotoxic T cells: with few mutations and an immunosuppressive microenvironment it resists checkpoint drugs, so engineered T-cell therapies are explored to direct killing at this childhood sarcoma.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Rhabdomyosarcoma often strikes the orbit: it is the commonest soft-tissue sarcoma of the eye socket in children, causing rapidly progressive proptosis that demands urgent diagnosis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Rhabdomyosarcoma is muscle gone wrong, down to its calcium: the rhabdomyoblasts switch on skeletal-muscle genes and the calcium-driven contraction machinery, expressing markers like desmin and myogenin that confirm the diagnosis.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Rhabdomyosarcoma builds its blood supply through endothelial cells: VEGF from the tumor recruits new vessels to feed its rapid growth, a feature studied for anti-angiogenic therapy.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy proves a tumor is rhabdomyosarcoma: the malignant cells assemble crude sarcomeres — thick and thin filaments aligned into Z-bands — the ultrastructural sign of skeletal-muscle differentiation that named the cancer.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Pelvic rhabdomyosarcoma threatens the kidney from afar: bladder, prostate, and vaginal tumors fill the pelvis and compress the ureters, backing urine up into the kidneys as obstructive hydronephrosis that can damage them if not relieved.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Rhabdomyosarcoma can spread to the liver: alongside its favored routes to lung, bone, and marrow, the bloodborne tumor seeds hepatic metastases in widespread disease, a marker of the high-risk, hardest-to-cure cases.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The VAC backbone frays the nerves: vincristine, the 'V' of the standard rhabdomyosarcoma regimen, jams the microtubule transport of peripheral neurons, causing a dose-limiting neuropathy with foot drop, constipation, and tingling.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Intensified chemotherapy can scar the heart: when doxorubicin is added for higher-risk rhabdomyosarcoma, its cumulative cardiotoxicity threatens a late cardiomyopathy that survivors are monitored for long after cure.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — The bladder is a common cradle for childhood RMS: embryonal (botryoid) rhabdomyosarcoma often springs from the bladder and prostate, a sarcoma of muscle quite unlike the urothelial bladder cancer that strikes adults.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains prove the muscle lineage: nuclear myogenin and MyoD1 with cytoplasmic desmin confirm a tumor is rhabdomyosarcoma, and diffuse myogenin especially flags the aggressive alveolar, PAX-FOXO1-fusion subtype on biopsy.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The VAC regimen empties the marrow: vincristine, actinomycin-D, and cyclophosphamide are heavily myelosuppressive, dropping neutrophil counts so that febrile neutropenia is a recurring danger through a child's rhabdomyosarcoma treatment.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — RMS favors the genitourinary tract: paratesticular, vaginal (botryoid), and uterine tumors are classic embryonal sites, so the reproductive organs are both where many of these sarcomas start and what surgery and radiation must try to spare.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Ifosfamide injures the kidney's salt handling: the alkylating drug central to RMS chemotherapy damages the proximal tubule into a Fanconi-like state that wastes magnesium and phosphate, electrolytes replaced through the course of treatment.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Fusion-positive RMS amplifies the cell-cycle engine: alveolar tumors driven by PAX3-FOXO1 often co-amplify CDK4 and MDM2, pushing cells past the cycle checkpoint and making CDK4/6 inhibition an actively studied target.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The multi-drug chemotherapy empties the marrow: the vincristine-actinomycin-cyclophosphamide backbone suppresses platelet production into thrombocytopenia, adding bleeding risk to the long, intensive treatment these tumors demand.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — Amplification marks the worst form: the aggressive alveolar subtype carrying the PAX3-FOXO1 fusion often also amplifies MYCN, a proliferation driver that helps explain its high-risk behavior and resistance to standard chemotherapy.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Innate killers are recruited against it: rhabdomyosarcoma is hard for T cells to see, so natural killer cell–based and engineered cell therapies are explored to attack a tumor that resists checkpoint immunotherapy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The tumor cloaks itself in suppression: regulatory T cells accumulate in the rhabdomyosarcoma microenvironment and blunt anti-tumor immunity, part of the immune-cold profile that has frustrated immunotherapy in this childhood sarcoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Cell-cycle loss marks the fusion-negative tumors: CDKN2A deletion is recurrent in embryonal rhabdomyosarcoma, releasing CDK4/6 to drive proliferation and complementing the cell-cycle amplicons of the fusion-positive subtype.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Tumor and treatment hurt the nerves: head-and-neck, paraspinal, and pelvic rhabdomyosarcomas compress nerves, and vincristine adds a peripheral neuropathy, together a real pain burden in these children.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Intensive chemotherapy invites sepsis: the VAC regimen's deep neutropenia leaves children with rhabdomyosarcoma prone to febrile neutropenia and bloodstream infection through the long treatment course.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — An activating receptor signals through it: FGFR4 mutations recurrent in rhabdomyosarcoma drive STAT3 activation that promotes survival and proliferation, marking the pathway as a candidate target in fusion-positive disease.
- `connects-to` → **[AML](../aml/README.md)** — Its cure can seed a later leukemia: the alkylators and topoisomerase poisons in the VAC backbone carry a small risk of therapy-related acute myeloid leukemia years after rhabdomyosarcoma treatment.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Ifosfamide scars the young kidney: the alkylator central to many rhabdomyosarcoma regimens is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment in treated children.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracyclines and alkylators strain the heart: doxorubicin in high-risk rhabdomyosarcoma and high-dose cyclophosphamide are cardiotoxic, risking a cardiomyopathy and heart failure that can surface during childhood-cancer survivorship.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Intensive chemotherapy opens the lung to mold: the deep neutropenia from rhabdomyosarcoma's multi-agent regimens lets inhaled Aspergillus invade as pulmonary aspergillosis in these young patients.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A childhood cancer and its long therapy strain the mind: the diagnosis in children and teens, disfiguring surgery and prolonged treatment contribute to depression and distress in patients and families.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Wide resection in irradiated tissue heals slowly: the local control of rhabdomyosarcoma combines extensive surgery with radiation, and the irradiated, chemotherapy-suppressed bed leaves wounds prone to breakdown.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Chemotherapy reawakens shingles: the multi-agent regimens for rhabdomyosarcoma suppress a child's immunity, allowing latent or primary varicella-zoster to cause severe disseminated infection.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A childhood cancer with relapse risk breeds lasting worry: disfiguring surgery, intensive therapy and long survivorship surveillance after rhabdomyosarcoma foster chronic anxiety in survivors and families.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to the lungs: like other sarcomas, rhabdomyosarcoma metastasises preferentially to the lungs, so pulmonary metastases shape its staging, treatment and prognosis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Head-and-neck radiation and chemo hit the glands: parameningeal and orbital radiotherapy for rhabdomyosarcoma can damage the hypothalamus and pituitary, and chemotherapy impairs future fertility.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Pelvic tumours and chemo disturb the gut: genitourinary and pelvic rhabdomyosarcoma can obstruct the bowel, and its multi-agent chemotherapy causes mucositis, nausea and hepatotoxicity.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Unlike most sarcomas it spreads to nodes: rhabdomyosarcoma, especially the alveolar subtype, involves regional lymph nodes, so nodal sampling is part of its staging.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its drugs and pelvic tumours injure the urinary tract: ifosfamide and cyclophosphamide cause haemorrhagic cystitis and a Fanconi-like tubulopathy, and genitourinary tumours can obstruct the urinary tract.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its chemotherapy can scar the heart: the doxorubicin and dactinomycin in rhabdomyosarcoma regimens carry a cardiotoxicity risk in the children who receive them.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Therapy suppresses immunity: the intensive vincristine-actinomycin-cyclophosphamide chemotherapy for rhabdomyosarcoma is profoundly immunosuppressive, raising opportunistic-infection risk.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Treatment marks the skin: chemotherapy causes alopecia and mucositis, and radiotherapy produces dermatitis over the treated site, with rare cutaneous rhabdomyosarcoma.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — New agents target its fusion biology: research pursues drugs against the PAX3/7-FOXO1 fusion and downstream pathways of alveolar rhabdomyosarcoma beyond conventional chemotherapy.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — VAC is the backbone: rhabdomyosarcoma is treated with intensive multi-agent chemotherapy — vincristine, actinomycin-D and cyclophosphamide — alongside surgery and radiotherapy, the regimen that turned a once-fatal childhood sarcoma curable.
- `connects-to` → **[GIST](../gist/README.md)** — A contrasting mesenchymal tumour: both are soft-tissue sarcomas, but GIST is a KIT/PDGFRA-driven adult tumour exquisitely sensitive to imatinib, whereas rhabdomyosarcoma is a paediatric myogenic cancer relying on cytotoxic chemotherapy.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunologically cold: rhabdomyosarcoma has a low mutational burden and sparse T-cell infiltrate, so checkpoint blockade that transformed melanoma and lung cancer shows little activity, keeping chemotherapy central.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Its metastases seed the lung: rhabdomyosarcoma spreads to the lungs (and bone marrow), studding the alveolar parenchyma with deposits, so chest imaging stages the disease and lung involvement worsens the prognosis.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — An SHH-driven childhood tumour: embryonal rhabdomyosarcoma can be driven by Hedgehog signalling and occurs in Gorlin syndrome, whose germline PTCH1 loss activates the SMO pathway this sarcoma can also exploit.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Two embryonal tumours of childhood: rhabdomyosarcoma and medulloblastoma are densely cellular paediatric cancers that can both run on Hedgehog/SHH signalling, arising in muscle lineage and cerebellum respectively.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Embryonal childhood cancers compared: rhabdomyosarcoma and retinoblastoma are both classic paediatric tumours treated on cooperative-group protocols, contrasting a muscle-lineage sarcoma with an RB1-driven eye cancer.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Bone-marrow metastasis: rhabdomyosarcoma, especially the alveolar subtype, spreads to bone and bone marrow, and marrow involvement mimicking leukaemia carries a grim prognosis.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Parameningeal invasion: head-and-neck rhabdomyosarcoma near the skull base invades along nerves toward the meninges, causing cranial-nerve palsies and a worse, CNS-threatening outlook.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Sarcoma botryoides of the genital tract: embryonal rhabdomyosarcoma arises in the vagina and cervix of young girls as grape-like botryoid masses, often DICER1-driven—a sarcoma of the same region as cervical carcinoma.
- `connects-to` → **[Desmoid Tumor](../desmoid-tumor/README.md)** — A deep soft-tissue differential: like rhabdomyosarcoma, a desmoid tumour presents as an infiltrative soft-tissue mass, the two sitting in the differential of an enlarging extremity or trunk lesion despite very different biology.
- `connects-to` → **[MPNST](../mpnst/README.md)** — NF1 sarcomas: neurofibromatosis type 1 predisposes to both rhabdomyosarcoma in childhood and MPNST from nerve sheaths, two RAS-pathway soft-tissue sarcomas of the syndrome.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Targetable kinase: FGFR4 activating mutations and amplification drive a subset of rhabdomyosarcomas, marking an actionable receptor tyrosine kinase.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo activation: Hippo-YAP signalling drives fusion-negative embryonal rhabdomyosarcoma, sustaining proliferation and blocking muscle differentiation.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Differentiation block: Notch signalling maintains the undifferentiated, proliferative state of rhabdomyosarcoma, preventing the myogenic maturation its cells are poised toward.

[^crist-2001-irs4-rms]: Crist WM, Anderson JR, Meza JL, et al. Intergroup rhabdomyosarcoma study-IV: results for patients with nonmetastatic disease. *J Clin Oncol.* 2001;19(12):3091-3102. [doi:10.1200/JCO.2001.19.12.3091](https://doi.org/10.1200/JCO.2001.19.12.3091) · [PubMed 11408506](https://pubmed.ncbi.nlm.nih.gov/11408506/)
[^oberlin-2012-mmt95-rms]: Oberlin O, Rey A, Sanchez de Toledo J, et al. Randomized comparison of intensified six-drug versus standard three-drug chemotherapy for high-risk nonmetastatic rhabdomyosarcoma and other chemotherapy-sensitive childhood soft tissue sarcomas. *J Clin Oncol.* 2012;30(19):2457-2465. [doi:10.1200/JCO.2011.39.3538](https://doi.org/10.1200/JCO.2011.39.3538) · [PubMed 22665546](https://pubmed.ncbi.nlm.nih.gov/22665546/)
