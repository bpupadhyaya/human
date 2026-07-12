---
schema: human-scale-entry/v1
id: synovial-sarcoma
name: Synovial Sarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Synovial sarcoma is defined by SS18-SSX1/SSX2 fusion (t(X;18)) → SMARCB1 displacement from BAF → EZH2 dependency; ~800/year USA; biphasic/monophasic histology; TLE1 IHC positive; ifosfamide-based chemotherapy; tazemetostat (SARC057 ORR ~22%) and trabectedin active."
aliases: ["synovial sarcoma", "SS18-SSX sarcoma", "biphasic synovial sarcoma", "monophasic synovial sarcoma", "t(X;18) sarcoma", "TLE1-positive sarcoma", "translocation sarcoma SYT-SSX", "synovial cell sarcoma"]
sources:
  - id: kadoch-2013-ss18-ssx-baf
    type: peer-reviewed
    cite: "Kadoch C, Crabtree GR. Reversible disruption of mSWI/SNF (BAF) complexes by the SS18-SSX oncogenic fusion in synovial sarcoma. Cell. 2013;153(1):71-85."
    doi: "10.1016/j.cell.2013.02.036"
    pmid: "23540691"
    url: "https://doi.org/10.1016/j.cell.2013.02.036"
  - id: kawai-2015-trabectedin-synovial
    type: peer-reviewed
    cite: "Kawai A, Araki N, Sugiura H, et al. Trabectedin monotherapy after standard chemotherapy versus best supportive care in patients with advanced, translocation-related sarcoma: a randomised, open-label, phase 2 study. Lancet Oncol. 2015;16(4):406-416."
    doi: "10.1016/S1470-2045(15)70098-7"
    pmid: "25795407"
    url: "https://doi.org/10.1016/S1470-2045(15)70098-7"
cross_links:
  - target: 01-human/03-molecular/ss18
    relation: connects-to
    note: "SS18-SSX1/SSX2 fusion (t(X;18)(p11;q11)) is the pathognomonic alteration of synovial sarcoma (100% of cases); FISH for SS18 rearrangement or RT-PCR for SS18-SSX transcript is the diagnostic standard; SSX2 predominates in monophasic SS; SSX1 in biphasic SS."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "SS18-SSX displaces SMARCB1 from BAF → PRC2/EZH2 unrestricted → H3K27me3 at CDKN2A, KLF4, and differentiation loci; synovial sarcoma is EZH2-dependent; tazemetostat (EZH2 inhibitor, SARC057): ORR 22% in pretreated SS; FDA breakthrough therapy designation granted for SS."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SS18-SSX displaces SMARCB1 from canonical BAF without SMARCB1 mutation → SMARCB1 degraded → BAF destabilized → PRC2 access; SMARCB1 IHC remains intact in SS (contrast AT/RT where SMARCB1 is lost); SS18-SSX knockdown → SMARCB1 re-occupies BAF → G1 arrest; shared EZH2 dependency."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Homozygous CDKN2A deletion in ~10-15% synovial sarcoma predicts poor prognosis; EZH2/H3K27me3 epigenetically silences CDKN2A even without deletion → absent p16 → CDK4/6 hyperactivation → E2F-driven S-phase; CDK4/6 inhibitors (palbociclib) under evaluation in CDKN2A-deleted SS."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "SS18-SSX QPGY activation domain drives VEGF transcription → angiogenesis; pazopanib (VEGFR2 inhibitor, PALETTE trial: PFS HR 0.35) FDA-approved for advanced STS post-chemo including SS; VEGF overexpression correlates with tumor grade and metastatic potential in synovial sarcoma."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "SS has low TMB (~1-2 mut/Mb) and variable PD-L1 → limited single-agent ICB ORR (~10-15%); tazemetostat + pembrolizumab (Phase 1/2) under investigation; EZH2 inhibition may restore IFN-γ response; TMB-high/MSI-H SS (<5%) most likely ICB responders."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "TLE1 (most specific SS IHC marker) is a Groucho-family WNT/β-catenin co-repressor (binds TCF/LEF); SS18-SSX recruits TLE1 into the oncogenic complex; ~30% of SS show nuclear β-catenin; CTNNB1 mutations in <5%; WNT pathway modulation is part of SS epigenetic de-regulation."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Synovial sarcoma and AT/RT both derange the SWI/SNF (BAF) complex and depend on EZH2: SS18-SSX fusion ejects SMARCB1 from BAF (SMARCB1 stays detectable), while AT/RT deletes SMARCB1 entirely (INI1 lost on IHC) — yet both respond to the EZH2 inhibitor tazemetostat."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Synovial sarcoma is a soft-tissue sarcoma of adolescents and young adults arising near — not from — joints, typically in deep extremity soft tissue (around the knee); despite the name it is not of synovial origin, and wide resection plus radiation is standard."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the dominant metastatic site in synovial sarcoma: it spreads hematogenously to the lungs even years after the primary is controlled, so long-term chest CT surveillance is essential and pulmonary metastasectomy is offered for limited disease."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "Synovial sarcoma and schwannomatosis both subvert the SWI/SNF (BAF) chromatin-remodeling complex: synovial sarcoma's SS18-SSX fusion reprograms BAF to silence tumor-suppressors, while loss of the BAF subunit SMARCB1 drives schwannomatosis and rhabdoid tumors."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Synovial and Ewing sarcoma are fusion-driven sarcomas of young adults defined by a single translocation: SS18-SSX for synovial sarcoma, EWSR1-FLI1 for Ewing—both aberrant transcription factors that remodel the epigenome, models of fusion-oncoprotein cancer."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Synovial sarcoma is a mesenchymal tumor of fibroblast-like spindle cells despite its misleading name: it arises not from synovium but from a primitive mesenchymal cell, its monophasic form being sheets of spindle cells expressing TLE1 and SS18-SSX."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Synovial sarcoma and rhabdomyosarcoma are both fusion-driven soft-tissue sarcomas: synovial sarcoma's SS18-SSX fusion hijacks the SWI/SNF complex, while alveolar RMS's PAX-FOXO1 drives myogenic transcription—translocations defining distinct, aggressive sarcomas."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "Synovial sarcoma and MPNST are spindle-cell sarcomas that can look alike: synovial sarcoma is defined by SS18-SSX, MPNST by NF1-driven nerve-sheath origin—so SS18-SSX testing and S100/SOX10 staining separate these spindle tumors."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Synovial sarcoma is managed like other high-grade soft-tissue sarcomas with surgery plus radiotherapy: wide resection combined with photon radiation improves local control, while the SS18-SSX fusion is now also targeted by EZH2 inhibitors and cellular therapy."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation can mark progression in synovial sarcoma: while the SS18-SSX fusion is the defining initiating event, secondary p53 loss appears in high-grade, dedifferentiated tumors—so the genome guardian's failure layers onto the fusion oncogene to worsen behavior."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT activation helps immortalize synovial sarcoma cells: telomerase reactivation, alongside the SS18-SSX fusion that reprograms the epigenome, lets these translocation-driven sarcomas divide indefinitely—a step common to many cancers despite their distinct drivers."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Synovial sarcoma joins the broad sarcoma spectrum of Li-Fraumeni syndrome: although defined by the somatic SS18-SSX fusion rather than germline p53 loss, sarcomas like it occur excessively in p53-deficient patients—linking fusion-driven and hereditary sarcomas."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Synovial sarcoma is a leading target for engineered T-cell therapy: it expresses cancer-testis antigens (NY-ESO-1, MAGE-A4), so afami-cel/tecelra—TCR T cells the immune system is reprogrammed to deploy—became the first such therapy approved for a solid tumor."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Synovial sarcoma's cancer-testis antigens depend on antigen presentation: dendritic cells process NY-ESO-1 and MAGE-A4 onto HLA, the step that primes the T cells engineered immunotherapies exploit—and the tumor evades this by downregulating MHC."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Synovial sarcoma is a rare primary cardiac sarcoma: though usually arising in limb soft tissue, it can originate in the heart or pericardium, presenting with obstruction or effusion and a grim prognosis given difficult surgical clearance."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Synovial sarcoma is a flagship for engineered T cells: it expresses NY-ESO-1, and afamitresgene autoleucel—TCR-engineered cytotoxic T cells targeting that antigen—won FDA approval in 2024 for this sarcoma, a first for solid-tumor TCR therapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Synovial sarcoma is an immunologically 'cold' tumor rich in macrophages: tumor-associated macrophages dominate its sparse immune infiltrate and suppress T-cell responses, helping explain why checkpoint inhibitors disappoint while TCR-engineered T cells work."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Synovial sarcoma runs an IGF-1 autocrine loop: the tumor overexpresses IGF1R and its ligands to drive growth and survival, so IGF1R inhibition has been explored as targeted therapy in this fusion-driven sarcoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "Synovial sarcoma is a chromatin disease: its SS18-SSX fusion hijacks the SWI/SNF (BAF) complex—which includes ARID1A—wrenching it onto the wrong genes, so the tumor is driven by epigenetic miswiring rather than classic mutations."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Synovial sarcoma's immunotherapy is limited by regulatory T cells: it expresses the NY-ESO-1 antigen targeted by TCR-engineered T cells, but a Treg-rich, suppressive microenvironment blunts the attack and curbs durable responses."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Synovial sarcoma grows on IGF-driven mTOR signaling: autocrine IGF-1 feeds the PI3K-AKT-mTOR axis to fuel proliferation, making mTOR a studied target in a sarcoma otherwise reliant on chemotherapy and surgery."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia stokes synovial sarcoma's aggressiveness: as the tumor outgrows its blood supply, low oxygen drives invasion and metastasis, contributing to the lung spread that threatens patients with this translocation-driven sarcoma."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Synovial sarcoma can spread to the brain: though lung is the dominant metastatic site, hematogenous spread occasionally seeds brain metastases in advanced disease, prompting imaging when neurologic symptoms appear."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Synovial sarcoma leans on AKT downstream of IGF: autocrine IGF-1 activates the PI3K-AKT-mTOR axis to drive proliferation and survival, so AKT-mTOR inhibitors are studied alongside the IGF and immune approaches in this sarcoma."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Synovial sarcoma sometimes calcifies: foci of calcium deposit within the tumor, and heavily calcified synovial sarcomas tend to carry a notably better prognosis than non-calcified ones."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Synovial sarcoma can spread to the liver: though it favors the lungs, hematogenous metastasis seeds the liver and other organs in advanced disease, marking the shift to systemic treatment."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Synovial sarcoma weaves a fibrous stroma: its spindle-cell component lays down dense collagen in the biphasic tumor, the firm fibrous tissue that, with epithelial nests, defines its histology."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy exposes synovial sarcoma's split personality: alongside the spindle cells sit true epithelial cells joined by desmosomes, sprouting microvilli into gland-like lumina over a basal lamina — the ultrastructure of its biphasic histology."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Synovial sarcoma can invade the skeleton: though it favors the lungs, late disease seeds bone and the marrow within, and tumors abutting a joint erode the neighboring bone as they grow."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Rarely synovial sarcoma is born in the kidney itself: primary renal synovial sarcoma, carrying the same SS18 fusion, is a recognized aggressive entity that masquerades as a more common kidney tumor until molecular testing reveals it."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Despite its name, synovial sarcoma weaves a fibrous tumor: its spindle cells sit in a collagen-rich stroma, often with stippled calcification, and the biphasic form adds glandular epithelium — a texture that, with the SS18 fusion, makes the diagnosis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The ifosfamide in its chemotherapy can fog the brain: a metabolite of this alkylator crosses into the CNS and poisons neurons, causing a reversible encephalopathy with confusion and seizures that methylene blue is used to treat."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Ifosfamide also injures the kidney's tubules: the resulting Fanconi-like syndrome wastes magnesium, phosphate, and bicarbonate into the urine, so electrolytes are monitored and replaced through synovial sarcoma treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody now clinches the diagnosis: a stain against the SS18-SSX fusion protein is highly specific for synovial sarcoma, and with TLE1 it confirms the t(X;18)-driven tumor that can otherwise mimic many spindle-cell cancers."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The doxorubicin-ifosfamide regimen empties the marrow: both drugs are heavily myelosuppressive, dropping neutrophil counts so that febrile neutropenia is a recurring hazard through synovial sarcoma chemotherapy."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Treatment and tumor both thin the red cells: the anthracycline-and-alkylator chemotherapy suppresses marrow erythrocyte production, leaving an anemia and fatigue that may need transfusion across the long course of care."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The doxorubicin-ifosfamide chemotherapy strains the heart: the anthracycline backbone for synovial sarcoma is cumulatively cardiotoxic to cardiomyocytes, so cardiac function is checked across treatment in these often-young patients."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cure can cost fertility: synovial sarcoma strikes adolescents and young adults, and its alkylating ifosfamide and any pelvic radiation damage the gonads, so fertility preservation is discussed before treatment begins."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "It is a hypoxic, vessel-hungry tumor: synovial sarcoma stabilizes HIF and pours out VEGF to feed its growth, the angiogenic drive behind the activity of anti-VEGF tyrosine-kinase inhibitors like pazopanib against it."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "It survives by blocking its own death: synovial sarcoma strongly and characteristically expresses the anti-apoptotic protein BCL-2 — useful as a diagnostic marker and a hint that drugs disabling this survival signal might work against it."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "A receptor it leans on: synovial sarcoma frequently overexpresses EGFR, feeding growth signals into its proliferation, which has made the receptor a studied (if so far disappointing) target in this fusion-driven sarcoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "It is a flagship for cell therapy: synovial sarcoma expresses the cancer-testis antigen NY-ESO-1, the target of engineered T-cell therapy, and natural killer and other cell-based approaches are pursued against a tumor that resists checkpoint drugs."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 backs its survival signaling: synovial sarcoma cells show STAT3 activation that supports proliferation and immune evasion, one of the cooperating pathways downstream of the SS18-SSX fusion that drives the tumor."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A solid cancer that clots: like other sarcomas, synovial sarcoma raises thrombosis risk through tumor-driven hypercoagulability, with deep-vein thrombosis and pulmonary embolism worsened by major limb surgery and chemotherapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Chemo neutropenia opens the door to infection: the ifosfamide-doxorubicin regimens used against synovial sarcoma cause deep neutropenia, so neutropenic fever and sepsis are recurrent treatment hazards."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Ifosfamide is hard on the kidney: the alkylator central to synovial-sarcoma chemotherapy is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment, especially with cumulative dosing."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its cure can sow a later leukemia: the alkylators and anthracyclines used against synovial sarcoma carry a small long-term risk of therapy-related myelodysplasia and acute myeloid leukemia in survivors."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Tumor inflammation and chemo blunt the marrow: advanced synovial sarcoma's inflammatory burden raises hepcidin while cytotoxic therapy suppresses erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracycline-based chemo strains the heart: doxorubicin, paired with ifosfamide as the mainstay for synovial sarcoma, is dose-dependently cardiotoxic and can leave a cardiomyopathy and heart failure in young survivors."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its intensive chemotherapy opens the lung to mold: the deep neutropenia of doxorubicin-ifosfamide therapy for synovial sarcoma lets inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A cancer of the young with hard therapy weighs on mood: synovial sarcoma's diagnosis in adolescents and young adults, disfiguring surgery and grueling chemotherapy contribute to depression and distress."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Wide excision in irradiated tissue heals slowly: local control of synovial sarcoma combines extensive limb surgery with radiation, and the irradiated, chemotherapy-suppressed bed leaves wounds prone to breakdown."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Tumour, surgery and chemo all wound the nerves: synovial sarcomas near limb nerves, the resections that sacrifice them and the chemotherapy used together produce lasting neuropathic pain."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A young cancer with lung-relapse risk breeds worry: the disfiguring surgery, lung-metastasis surveillance and uncertain prognosis of synovial sarcoma foster chronic anxiety in survivors alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to the lungs: synovial sarcoma metastasises preferentially to the lungs, so pulmonary metastasectomy and lung surveillance dominate its long-term management."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its chemo reawakens shingles: the doxorubicin-ifosfamide chemotherapy for synovial sarcoma deeply suppresses immunity, allowing latent varicella-zoster to reactivate."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its chemo injures the gut: the ifosfamide and doxorubicin used for synovial sarcoma cause nausea, mucositis and, with ifosfamide, hepatotoxicity."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It is a sarcoma that reaches the nodes: synovial sarcoma is one of the few sarcomas with notable lymph-node metastasis, so nodal assessment matters in its staging."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its chemotherapy injures the kidney and bladder: the ifosfamide in its regimen causes haemorrhagic cystitis and a Fanconi-like renal tubulopathy."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its cure can scar the heart: the doxorubicin in synovial-sarcoma chemotherapy carries a dose-dependent cardiotoxicity risk in the young patients it often affects."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It pioneered TCR cell therapy: synovial sarcoma expresses NY-ESO-1, the target of the first approved engineered TCR T-cell therapy (afami-cel), and pazopanib treats advanced disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Treatment and tumour reach the nerves: ifosfamide causes encephalopathy and peripheral neuropathy, and paraspinal synovial sarcoma can compress nerves."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It and its treatment mark the skin: chemotherapy causes alopecia and mucositis, radiotherapy produces dermatitis over the treated limb, and superficial tumours present as a skin-deep mass."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemosensitive among sarcomas: synovial sarcoma is one of the more chemoresponsive soft-tissue sarcomas, treated with ifosfamide and doxorubicin around surgery and radiotherapy, especially in younger patients with larger tumours."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "First solid tumour with engineered T-cells: synovial sarcoma frequently expresses MAGE-A4 and NY-ESO-1, and afami-cel — autologous TCR-engineered T-cells against MAGE-A4 — became the first approved engineered T-cell therapy for a solid tumour in this disease."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold tumour: despite its antigen expression, synovial sarcoma has a low mutational burden and sparse T-cell infiltrate, so PD-1 checkpoint blockade responds poorly — why adoptive engineered T-cells, not checkpoint inhibitors, broke through."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "It spreads to the lungs: synovial sarcoma metastasises predominantly to the lungs, seeding the alveolar parenchyma, so chest imaging stages the disease and pulmonary metastasectomy is part of treatment."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "One driver defines each: synovial sarcoma is specified by the SS18-SSX fusion and GIST by activating KIT mutation—twin proofs that a single genetic lesion can create a sarcoma, though only GIST's is directly druggable with imatinib."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "Two ways to break SWI/SNF: synovial sarcoma's SS18-SSX fusion hijacks the BAF (SWI/SNF) chromatin complex, while clear cell ovarian cancer disables it through ARID1A loss—different routes to the same epigenetic dysregulation."
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "Two limb soft-tissue tumours, opposite fates: desmoid is a locally aggressive Wnt-driven fibromatosis that never metastasizes, whereas synovial sarcoma's deceptively slow growth hides a lethal capacity to spread."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Sarcomas of the young that home to lung: synovial sarcoma and osteosarcoma both strike adolescents and young adults and metastasize chiefly to the lungs, but osteosarcoma's chaotic genome contrasts with synovial sarcoma's single defining fusion."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "An immune desert: synovial sarcoma rarely forms the tertiary lymphoid structures and germinal-centre-like aggregates that mark hot tumours, explaining its poor checkpoint response and why engineered TCR cells were needed instead."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "A shared cancer-testis target: synovial sarcoma and melanoma both express NY-ESO-1, and engineered TCR T-cell therapy against it (afami-cel) won its first approval in synovial sarcoma after melanoma trials paved the way."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Juxta-articular invasion: arising near joints in the limbs, synovial sarcoma can erode adjacent cortical bone and metastasise to the skeleton, shaping the extent of limb-salvage surgery."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "A spindle-cell mimic near nerves: synovial sarcoma often arises beside nerves and shares a monophasic spindle-cell pattern with MPNST, the two sitting in the differential of a paraneural soft-tissue mass."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Fusion-driven oncogene: the SS18-SSX fusion retargets the BAF complex and activates MYC, driving the proliferation of synovial sarcoma."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: cyclin D1 upregulation, with CDKN2A loss, propels synovial sarcoma cells through the cell cycle, supporting CDK4/6-directed strategies."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo activation: nuclear YAP from deregulated Hippo signalling contributes to synovial sarcoma growth and its mesenchymal phenotype."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Autocrine growth: PDGF signalling, an output of the SS18-SSX-driven transcriptional programme, supports the proliferation of synovial sarcoma."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Growth-factor signalling: FGFR signalling contributes to synovial sarcoma proliferation, a candidate targetable receptor in this fusion-driven sarcoma."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Receptor activation: MET signalling promotes the growth and invasion of synovial sarcoma, part of the receptor-tyrosine-kinase landscape of the tumour."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Developmental reactivation: the SS18-SSX fusion reactivates Notch alongside Wnt signalling in synovial sarcoma, redeploying a developmental programme to sustain the proliferation of this monomorphic blue-cell tumour."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immunosuppressive stroma: TGF-β in the synovial-sarcoma microenvironment promotes an EMT-like invasive phenotype and excludes T cells, a barrier relevant to the engineered NY-ESO-1 TCR T-cell therapies now used in the disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Pulmonary homing: CXCR4 on synovial-sarcoma cells responds to CXCL12 gradients toward the lung, contributing to the pulmonary metastases that are the principal cause of death in this sarcoma."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle target: CDKN2A loss is common in synovial sarcoma, releasing CDK4/6-cyclin-D to drive the cell cycle and providing a rationale for CDK4/6 inhibitors in tumours that have deleted their p16 brake."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Immunosuppressive niche: CCL2 recruits tumour-associated macrophages into synovial sarcoma, building a myeloid-rich immunosuppressive microenvironment that helps explain the limited efficacy of checkpoint blockade despite the tumour's NY-ESO-1 antigen."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: synovial sarcoma is one of the more chemosensitive soft-tissue sarcomas, and doxorubicin and ifosfamide kill its cells through caspase-3-mediated apoptosis, the cytotoxic backbone of treatment alongside surgery."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival axis: PI3K-AKT-mTOR signalling (AKT and mTOR already mapped) is activated in synovial sarcoma and supports growth and survival, a targetable dependency downstream of its receptor tyrosine kinases."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: deregulated RB-E2F1 transcription powers the proliferation of synovial sarcoma, cooperating with the CDK4/6-cyclin-D and CDKN2A lesions already mapped."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "Invasive signalling: SRC-family kinase activity promotes the proliferation and invasive migration of synovial sarcoma cells, relayed from the MET, FGFR and EGFR receptor tyrosine kinases already mapped."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK-MAPK: the MET, FGFR, EGFR and IGF-1R receptors (all mapped) converge on the MAPK-ERK cascade driving proliferation in synovial sarcoma."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K restraint: PTEN limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped), an IGF-1R-driven survival pathway active in synovial sarcoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 suppression: synovial sarcoma usually retains wild-type TP53 (mapped) held in check by MDM2, making MDM2 inhibition a strategy to reactivate p53-driven apoptosis."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: dysregulation of the RB1-E2F checkpoint (CDK4/6, CDKN2A and cyclin-D1 already mapped) contributes to the proliferation of synovial sarcoma."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RTK-RAS proliferation: RAS-ERK signalling (ERK1/2 already mapped) downstream of the receptor tyrosine kinases active in synovial sarcoma provides a proliferative input."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 survival: JAK-STAT3 signalling (STAT3 already mapped) contributes to the survival signalling of synovial sarcoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the invasion and survival of synovial sarcoma cells."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) shapes the fibrotic and immunosuppressive microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment relevant to the NY-ESO-1-directed cell therapy and immunotherapy of synovial sarcoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of synovial sarcoma, relevant to its NY-ESO-1-directed cell therapy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by the PI3K-AKT axis, modulate the survival of the SS18-SSX-driven cells of synovial sarcoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated CD8 cytotoxicity is the effector mechanism of the NY-ESO-1-directed cell therapy used in synovial sarcoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin signaling aberrantly activated by the SS18-SSX fusion of synovial sarcoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the immunosuppressive tumor microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation that cooperates with the BAF-complex disruption of synovial sarcoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of the SS18-SSX-driven cells of synovial sarcoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of synovial sarcoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) shapes the inflammatory microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "CDKN1A-p21 cell-cycle control participates in the checkpoint regulation dysregulated in synovial sarcoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "TCR immunotherapy: synovial sarcoma frequently expresses the cancer-testis antigens NY-ESO-1 and MAGE-A4 and is the leading solid tumour for HLA-restricted engineered T-cell therapy, so antigen-presentation machinery governs its landmark response to TCR-T cells."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Invasion and resistance: the AXL receptor tyrosine kinase is expressed in synovial sarcoma and drives the mesenchymal invasion and drug-tolerant phenotype behind its lung-tropic metastatic course, a candidate target beyond conventional chemotherapy."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Tumour angiogenesis: synovial sarcoma is a vascular soft-tissue sarcoma whose growth depends on neovascularisation driven by angiopoietin-Tie2 and VEGF (VEGF already mapped), the rationale for antiangiogenic tyrosine-kinase inhibitors like pazopanib."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Engineered T-cell therapy: IL-2-driven T-cell expansion underlies the NY-ESO-1-directed TCR T-cell therapy (afamitresgene autoleucel), the first cell therapy approved for synovial sarcoma, which characteristically expresses cancer-testis antigens."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the doxorubicin-based chemotherapy used for synovial sarcoma is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that limits its cumulative dose."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Chemotherapy anaemia: the intensive chemotherapy used in synovial sarcoma is myelosuppressive, lowering haemoglobin and causing the anaemia that requires transfusion and growth-factor support during treatment."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion relevant to the NY-ESO-1 TCR-T cell therapy (CD8 already mapped) approved for synovial sarcoma."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and lysis stress: the doxorubicin-ifosfamide chemotherapy of synovial sarcoma generates oxidative stress and, in bulky disease, cell lysis releasing purines that xanthine oxidase converts to uric acid, adding oxidative and tumour-lysis burden."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of synovial sarcoma, part of the stromal microenvironment of this deep soft-tissue sarcoma of young adults."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, immune-evasive microenvironment of synovial sarcoma that the NY-ESO-1 TCR-T therapy must overcome."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the doxorubicin-ifosfamide chemotherapy of synovial sarcoma is myelosuppressive, causing anaemia (haemoglobin already mapped) that needs transfusion whose repeated support can load the young survivor with iron."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton radiotherapy: proton-beam radiotherapy provides local control of synovial sarcoma while sparing the surrounding normal tissue, an option especially valuable in the young patients typical of this sarcoma."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive cold microenvironment of synovial sarcoma."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages (CCL2 already mapped) infiltrate the synovial-sarcoma stroma, and their M2 polarisation (IL-4 already mapped) supports the immunosuppression relevant to the NY-ESO-1 TCR-T therapy."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone invasion: the para-articular synovial sarcoma can invade the adjacent cortical bone, part of the locally aggressive behaviour of this deep soft-tissue sarcoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic microenvironment: leptin from the marrow and stromal adipose tissue signals within the metabolic microenvironment of the metastatic synovial sarcoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipose adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the synovial-sarcoma microenvironment."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the NY-ESO-1 TCR-T immunotherapy of synovial sarcoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm engaged by the NY-ESO-1 (MHC already mapped) TCR-T cells against synovial sarcoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of synovial sarcoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the synovial-sarcoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the synovial-sarcoma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of synovial sarcoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the microenvironment that the NY-ESO-1 TCR-engineered T-cell therapy of synovial sarcoma must overcome."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) recruits and polarises the myeloid cells to an immunosuppressive phenotype in the synovial-sarcoma microenvironment."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of synovial sarcoma and the NY-ESO-1 TCR-T context."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the myeloid-driven immunosuppression of the synovial-sarcoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the synovial-sarcoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped) within the immunosuppressive microenvironment."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Sarcoma stromal alarmin: TSLP released from the SYT-SSX-driven synovial sarcoma stroma activates mast cells and dendritic cells, promoting the immunosuppressive type-2 microenvironment that blunts NY-ESO-1-targeted cytotoxic immunity."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chemotherapy anaemia: erythropoietin corrects the ifosfamide/doxorubicin-induced anaemia in synovial sarcoma, and EPOR expression on the tumour cells has been reported, suggesting possible direct trophic effects."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM invasion scaffold: periostin, an ECM glycoprotein of the synovial sarcoma stromal niche, promotes the local invasion and lung metastasis of the SYT-SSX-rearranged sarcoma cells and contributes to the desmoplastic microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin tumour-microenvironment mediator: bradykinin, generated by kallikrein-kinin activation in the synovial-sarcoma stroma, amplifies vascular permeability and the pro-tumourigenic microenvironment of the SYT-SSX-driven sarcoma."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact-complement regulation: C1-esterase inhibitor restrains the classical complement C1 and the contact system in the synovial-sarcoma microenvironment (C3/C5/C5aR1 already mapped), limiting complement-driven immune escape."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell sarcoma mediator: histamine from mast cells in the synovial-sarcoma stroma promotes vascular permeability and the immunosuppressive tumour microenvironment, contributing to the immune evasion of this SYT-SSX-fusion-driven sarcoma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "SyS melatonin: melatonin suppresses synovial-sarcoma proliferation via MT1/MT2 receptor-mediated inhibition of mTOR (already mapped) and ERK1/2 (already mapped) signalling, while enhancing NK-cell (already mapped) cytotoxicity against the SS18-SSX-driven tumour."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "SyS testosterone: androgen receptor is expressed by a subset of synovial-sarcoma cells; testosterone drives androgen receptor-mediated upregulation of SS18-SSX (already mapped) transcriptional programme, and androgen-axis suppression reduces synovial-sarcoma tumour proliferation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SyS serotonin: serotonin produced by neuroendocrine-differentiated synovial-sarcoma cells drives autocrine 5-HT receptor proliferative signalling and promotes tumour angiogenesis (VEGF already mapped), contributing to the disease progression of this SYT-SSX-rearranged sarcoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "SyS oxytocin: oxytocin receptor on synovial-sarcoma cells attenuates SS18-SSX (already mapped) transcriptional reprogramming and WNT/β-catenin (already mapped) signalling; oxytocin-driven cAMP/PKA activation limits YAP1 (already mapped) co-activator-mediated tumour proliferation."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "SyS vasopressin: vasopressin V1A receptors on synovial-sarcoma cells activate SRC-kinase (already mapped) and ERK1/2 (already mapped), amplifying the SS18-SSX (already mapped)-driven transcriptional reprogramming of this SYT-rearranged soft-tissue sarcoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "SyS selenium: selenium-dependent GPX4 suppresses ferroptosis-resistance in synovial-sarcoma; GPX4 inhibition synergises with EZH2 (already mapped) targeted therapy to overcome epigenetic reprogramming driven by the SS18-SSX (already mapped) fusion oncoprotein."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SyS iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour surveillance; thyroid deficiency amplifies VEGF (already mapped) and mTOR (already mapped) and IL-6 (already mapped) tumour-promotion cascade of synovial sarcoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "SyS sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced IL-6 (already mapped) amplifies the VEGF (already mapped) and mTOR (already mapped) and YAP1 (already mapped)-driven proliferative cascade of synovial sarcoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "SyS copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped), drives stromal remodelling; copper amplifies VEGF (already mapped) angiogenesis; copper deficiency impairs macrophage (already mapped) and T-cytotoxic-cell (already mapped) immunity in SyS."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "SyS zinc: zinc, as metalloproteinase cofactor in macrophages (already mapped) and T-cytotoxic-cell (already mapped), supports anti-tumour immunity; zinc deficiency amplifies IL-6 (already mapped) and VEGF (already mapped) and mTOR (already mapped) cascade of synovial sarcoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "SyS potassium: potassium efflux gates macrophage (already mapped) NLRP3; potassium loss amplifies IL-6 (already mapped) and WNT (already mapped) and mTOR (already mapped) proliferative cascade and suppresses T-cytotoxic-cell (already mapped) immunity in SyS."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "SyS phosphorus: phosphorus, as ATP donor in mTOR (already mapped) kinase signalling in fibroblasts (already mapped) and macrophages (already mapped), fuels sarcoma proliferation; phosphorus dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) in SyS."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "SyS carbon: carbon, as metabolic backbone of mTOR (already mapped) and VEGF (already mapped) in fibroblasts (already mapped) and macrophages (already mapped), drives proliferative signalling; carbon dysregulation amplifies IL-6 (already mapped) cascade of synovial sarcoma."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "SyS chloride: chloride channels in macrophages (already mapped) and fibroblasts (already mapped) regulate tumour-immune homeostasis; chloride dysregulation amplifies IL-6 (already mapped) and WNT (already mapped) and mTOR (already mapped) cascade of synovial sarcoma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "SyS hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and fibroblasts (already mapped), modulates tumour immune balance; hydrogen dysregulation amplifies IL-6 (already mapped) and WNT (already mapped) and VEGF (already mapped) cascade of synovial sarcoma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "SS nitrogen: nitric oxide from macrophages (already mapped) and tumor-associated endothelial cells modulates vascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour growth cascade of synovial sarcoma."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "SS sulfur: hydrogen sulfide from macrophages (already mapped) and endothelial cells modulates tumour vascular tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of synovial sarcoma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "SS GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells modulates metabolic-immune balance; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of synovial sarcoma."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "SS angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives tumour angiogenesis; angiotensin-ii excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of synovial sarcoma."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "SS rankl: RANKL from macrophages (already mapped) and tumour cells (already mapped) promotes bone remodelling in synovial sarcoma; rankl excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of synovial sarcoma."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "SS fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds synovial sarcoma ECM; fibronectin excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of synovial sarcoma."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "SS activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) drives synovial sarcoma fibrosis; activin-a excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of synovial sarcoma."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "SS cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates synovial sarcoma vascular tone; cgrp excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of synovial sarcoma."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "SS calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates calcium signalling in synovial sarcoma; calcitonin dysregulation amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of synovial sarcoma."
---

# Synovial Sarcoma

## Overview

**Synovial sarcoma (SS)** is a malignant soft tissue sarcoma universally defined by the chromosomal translocation **t(X;18)(p11;q11)** generating a **SS18-SSX1, SS18-SSX2, or SS18-SSX4 fusion protein**. Despite its name, synovial sarcoma does not arise from synovial tissue — it originates from undifferentiated mesenchymal/neural crest precursors. SS is the **second most common soft tissue sarcoma in adolescents and young adults** (after rhabdomyosarcoma) and one of the few sarcomas with a pathognomonic chromosomal translocation [^ladanyi note via kadoch-2013-ss18-ssx-baf].

**Epidemiology:**
- Incidence: ~800 cases/year USA; ~7-10% of all soft tissue sarcomas
- Peak age: 15-40 years (median ~26-30 years); rare in children <5 and adults >60
- Slight male predominance (~1.2:1 M:F)
- No established environmental risk factors; not associated with radiation or NF2 syndrome

**Anatomic locations:**
- Lower extremity (knee/thigh/popliteal fossa): ~50-60% — most common
- Upper extremity (shoulder, elbow, wrist, hand): ~15-20%
- Head and neck (pharynx, tongue, larynx): ~5-10%
- Trunk wall, mediastinum, pleura, lung (primary): ~5-10%
- Intra-abdominal, retroperitoneal: rare; worse prognosis
- Joint space involvement is uncommon despite the name

**Key clinical features:**
- Most present as a painless or mildly painful soft tissue mass, often near (but not within) a joint
- Many are initially misdiagnosed as a benign cyst or ganglion; delay in diagnosis 2-4 years is common
- ~20-25% present with calcifications on plain radiograph (stippled, "egg-shell" calcification characteristic)
- MRI: heterogeneous mass with "triple signal" appearance (hemorrhage, necrosis, calcification); T2 bright heterogeneous; invades fascial planes but rarely bone (unlike osteosarcoma)

## Structure

### Histological subtypes

**Biphasic synovial sarcoma (~30%):**
Two morphologically distinct components:
- **Epithelial component**: glandular/tubular structures lined by cuboidal-to-columnar cells with round nuclei, prominent nucleoli; positive for cytokeratin, EMA, CD34 (focal)
- **Spindle cell component**: fascicular spindle cells with scant cytoplasm, overlapping nuclei, minimal pleomorphism; characteristic hemangiopericytoma-like vessels
- SS18-SSX1 predominates in biphasic type
- Higher rate of epithelial marker positivity; diagnosis is more straightforward

**Monophasic synovial sarcoma (~65%):**
Exclusively spindle cell morphology; can mimic solitary fibrous tumor, malignant peripheral nerve sheath tumor (MPNST), or poorly differentiated carcinoma; TLE1 IHC + and SS18 FISH are critical for diagnosis in monophasic type; SS18-SSX2 predominates

**Poorly differentiated/high-grade synovial sarcoma (~5%):**
Round to large pleomorphic cells; loss of spindle cell morphology; >10 mitoses/10 HPF; rapid growth; worst prognosis; CDKN2A deletion common; all subtypes can have focal poorly differentiated areas

### IHC panel and diagnostic workup

**TLE1 (transducin-like enhancer protein 1):** nuclear positivity in ~85-90% of SS; most sensitive and specific single marker for SS among soft tissue tumors; however, focal TLE1 positivity also in MPNST, solitary fibrous tumor, desmoplastic small round cell tumor — context required

**Keratin (AE1/AE3, MNF116, CAM5.2):** positive in epithelial component of biphasic SS (~70%); focal (25-50%) in monophasic; variable

**EMA (epithelial membrane antigen):** positive in 85% of biphasic; 50% monophasic

**CD34:** focal in some SS; helps distinguish from SFT (CD34 diffuse in SFT)

**SOX2:** strongly positive in most SS (EZH2-driven SOX2 re-expression in SS); synergizes with TLE1 positivity

**SS18 FISH**: confirmatory; SS18 break-apart probe; sensitivity ~95%

## Function

### SS18-SSX oncogenic mechanism

The SS18-SSX fusion protein drives synovial sarcoma through BAF complex subversion [^kadoch-2013-ss18-ssx-baf]:
- SS18-SSX incorporates into cBAF complex, displacing wild-type SS18 → SMARCB1 evicted → BAF destabilized
- EZH2/PRC2 gains chromatin access → H3K27me3 spreads over differentiation loci → CDKN2A, KLF4, neural differentiation genes silenced
- QPGY activation domain (from SS18) drives ETV4, VEGF, and MYC target gene transcription
- Net result: tumor cells are locked in a proliferative, undifferentiated, vascular state with features of both epithelial and mesenchymal lineages

Normal cell (with wild-type BAF-SS18): BAF → SMARCB1 intact → PRC2 excluded from BAF target loci → CDKN2A transcribed → G1 arrest maintained; differentiation programs active

SS cell (with SS18-SSX): cBAF disrupted → SMARCB1 evicted → PRC2 silences CDKN2A + differentiation → proliferative state; paradoxically retains some epithelial features via ETV4/SOX2 de-repression

## Pathology

### Staging and risk stratification

**FNCLCC grading:**
- SS is uniformly high grade (FNCLCC grade 2-3); grading matters less for SS than for other STS
- Poor differentiation, CDKN2A deletion, high mitotic rate → grade 3

**Prognostic factors:**
- **Tumor size**: most important prognostic variable; ≤5 cm → 5-year OS ~85%; >5 cm → ~50%
- **CDKN2A deletion** (~10-15%): associated with >50% reduction in 5-year OS; worst prognostic marker in SS
- **Location**: extremity better than axial/pleural/intra-abdominal; head-neck intermediate
- **Extent of resection**: R0 (negative margin) resection → curative intent; R2 → high recurrence
- **Histological subtype**: poorly differentiated confers worst prognosis within SS
- **Metastases at diagnosis**: ~20-25% have metastases; lung (80%), lymph node (5-10%), bone

### Treatment

**Surgery:**
Wide local excision with ≥1 cm margins is the cornerstone; amputation rarely necessary with modern limb-salvage; compartmental resection when feasible; en-bloc resection of adjacent structures (nerve, vessel) when invaded; regional lymph node dissection for pathologically positive nodes (rare)

**Radiation therapy:**
- Adjuvant RT for high-risk features: tumor >5 cm, positive/close margins (<1 mm), deep location, recurrence
- Standard dose: 50-54 Gy preoperative or 60-66 Gy postoperative (IMRT preferred); equivalent local control in randomized VORTEX trial
- Preoperative RT preferred by most centers (smaller volume, better wound healing in selected cases)

**Chemotherapy — ifosfamide-based regimens:**
SS is one of the most chemotherapy-sensitive sarcomas:
- **First-line**: AI (doxorubicin 75 mg/m² + ifosfamide 10 g/m²) or AIM (AI + mesna) — ORR ~40-60%; PFS ~6-8 months in metastatic SS
- **Ifosfamide monotherapy**: ORR ~25-30% in SS; higher single-agent activity than in other STS subtypes
- **High-dose ifosfamide** (14-21 g/m²): ORR ~30-35% in ifosfamide-pretreated SS (unique ifosfamide sensitivity in SS vs other STS)

**Trabectedin:**
KAWAI 2015 (Phase 2 vs BSC) [^kawai-2015-trabectedin-synovial]: N=73 translocation-positive sarcomas (SS + myxoid liposarcoma); trabectedin 1.5 mg/m² q21d vs BSC; primary endpoint PFS; HR 0.07 (p<0.0001); 12-week PFS 60% vs 21%; OS benefit trending; ORR 17%; approved in Japan for translocation-related sarcoma; used off-label in USA; proposed mechanism: trabectedin directly disrupts SS18-SSX from chromatin

**Pazopanib:**
PALETTE Phase 3: PFS benefit in non-adipocytic STS including SS; HR 0.35; FDA-approved for advanced STS after prior chemotherapy; ORR ~5-10% in SS; PFS benefit more reliable than objective response

**Tazemetostat (EZH2 inhibitor):**
SARC057 (Phase 2): ORR ~22%, DCR ~67% in relapsed/refractory SS; FDA breakthrough therapy designation; ongoing Phase 1/2 combination studies (tazemetostat + ifosfamide; tazemetostat + pembrolizumab); represents first molecularly targeted therapy in SS

**Pembrolizumab/nivolumab:**
SS has low TMB (~1-2 mut/Mb) and variable PD-L1 expression; ICB response rates ~10-15% (lower than expected); MSS phenotype (no mismatch repair deficiency); combination with tazemetostat under investigation (EZH2 inhibition may restore IFN-γ response via epigenetic de-repression)

**Prognosis:**
- Localized SS (≤5 cm, R0 resection, no poor-differentiation): 5-year OS ~80-85%
- Localized SS (>5 cm, positive margin, or grade 3): 5-year OS ~50-60%
- Metastatic SS at diagnosis: 5-year OS ~20-25%; median OS ~18-24 months
- CDKN2A-deleted SS: 5-year OS ~30-40% regardless of stage
- Local recurrence: ~20-30% at 5 years; re-resection feasible if technically possible
- Lung metastases: surgical resection if oligometastatic; 5-year OS after resection ~30%

## Connections

- `connects-to` → **[SS18](../../03-molecular/ss18/README.md)** — SS18-SSX1/SSX2 fusion (t(X;18)(p11;q11)) is the pathognomonic alteration of synovial sarcoma (100% of cases); FISH for SS18 rearrangement or RT-PCR for SS18-SSX transcript is the diagnostic standard; SSX2 predominates in monophasic SS; SSX1 in biphasic SS.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — SS18-SSX displaces SMARCB1 from BAF → PRC2/EZH2 unrestricted → H3K27me3 at CDKN2A, KLF4, and differentiation loci; synovial sarcoma is EZH2-dependent; tazemetostat (EZH2 inhibitor, SARC057): ORR 22% in pretreated SS; FDA breakthrough therapy designation granted for SS.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SS18-SSX displaces SMARCB1 from canonical BAF without SMARCB1 mutation → SMARCB1 degraded → BAF destabilized → PRC2 access; SMARCB1 IHC remains intact in SS (contrast AT/RT where SMARCB1 is lost); SS18-SSX knockdown → SMARCB1 re-occupies BAF → G1 arrest; shared EZH2 dependency.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Homozygous CDKN2A deletion in ~10-15% synovial sarcoma predicts poor prognosis; EZH2/H3K27me3 epigenetically silences CDKN2A even without deletion → absent p16 → CDK4/6 hyperactivation → E2F-driven S-phase; CDK4/6 inhibitors (palbociclib) under evaluation in CDKN2A-deleted SS.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — SS18-SSX QPGY activation domain drives VEGF transcription → angiogenesis; pazopanib (VEGFR2 inhibitor, PALETTE trial: PFS HR 0.35) FDA-approved for advanced STS post-chemo including SS; VEGF overexpression correlates with tumor grade and metastatic potential in synovial sarcoma.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — SS has low TMB (~1-2 mut/Mb) and variable PD-L1 → limited single-agent ICB ORR (~10-15%); tazemetostat + pembrolizumab (Phase 1/2) under investigation; EZH2 inhibition may restore IFN-γ response; TMB-high/MSI-H SS (<5%) most likely ICB responders.
- `connects-to` → **[WNT/β-Catenin](../../03-molecular/wnt-beta-catenin/README.md)** — TLE1 (most specific SS IHC marker) is a Groucho-family WNT/β-catenin co-repressor (binds TCF/LEF); SS18-SSX recruits TLE1 into the oncogenic complex; ~30% of SS show nuclear β-catenin; CTNNB1 mutations in <5%; WNT pathway modulation is part of SS epigenetic de-regulation.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Synovial sarcoma and AT/RT both derange the SWI/SNF (BAF) complex and depend on EZH2: SS18-SSX fusion ejects SMARCB1 from BAF (SMARCB1 stays detectable), while AT/RT deletes SMARCB1 entirely (INI1 lost on IHC) — yet both respond to the EZH2 inhibitor tazemetostat.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Synovial sarcoma is a soft-tissue sarcoma of adolescents and young adults arising near — not from — joints, typically in deep extremity soft tissue (around the knee); despite the name it is not of synovial origin, and wide resection plus radiation is standard.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the dominant metastatic site in synovial sarcoma: it spreads hematogenously to the lungs even years after the primary is controlled, so long-term chest CT surveillance is essential and pulmonary metastasectomy is offered for limited disease.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — Synovial sarcoma and schwannomatosis both subvert the SWI/SNF (BAF) chromatin-remodeling complex: synovial sarcoma's SS18-SSX fusion reprograms BAF to silence tumor-suppressors, while loss of the BAF subunit SMARCB1 drives schwannomatosis and rhabdoid tumors.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Synovial and Ewing sarcoma are fusion-driven sarcomas of young adults defined by a single translocation: SS18-SSX for synovial sarcoma, EWSR1-FLI1 for Ewing—both aberrant transcription factors that remodel the epigenome, models of fusion-oncoprotein cancer.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Synovial sarcoma is a mesenchymal tumor of fibroblast-like spindle cells despite its misleading name: it arises not from synovium but from a primitive mesenchymal cell, its monophasic form being sheets of spindle cells expressing TLE1 and SS18-SSX.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Synovial sarcoma and rhabdomyosarcoma are both fusion-driven soft-tissue sarcomas: synovial sarcoma's SS18-SSX fusion hijacks the SWI/SNF complex, while alveolar RMS's PAX-FOXO1 drives myogenic transcription—translocations defining distinct, aggressive sarcomas.
- `connects-to` → **[MPNST](../mpnst/README.md)** — Synovial sarcoma and MPNST are spindle-cell sarcomas that can look alike: synovial sarcoma is defined by SS18-SSX, MPNST by NF1-driven nerve-sheath origin—so SS18-SSX testing and S100/SOX10 staining separate these spindle tumors.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Synovial sarcoma is managed like other high-grade soft-tissue sarcomas with surgery plus radiotherapy: wide resection combined with photon radiation improves local control, while the SS18-SSX fusion is now also targeted by EZH2 inhibitors and cellular therapy.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation can mark progression in synovial sarcoma: while the SS18-SSX fusion is the defining initiating event, secondary p53 loss appears in high-grade, dedifferentiated tumors—so the genome guardian's failure layers onto the fusion oncogene to worsen behavior.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT activation helps immortalize synovial sarcoma cells: telomerase reactivation, alongside the SS18-SSX fusion that reprograms the epigenome, lets these translocation-driven sarcomas divide indefinitely—a step common to many cancers despite their distinct drivers.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Synovial sarcoma joins the broad sarcoma spectrum of Li-Fraumeni syndrome: although defined by the somatic SS18-SSX fusion rather than germline p53 loss, sarcomas like it occur excessively in p53-deficient patients—linking fusion-driven and hereditary sarcomas.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Synovial sarcoma is a leading target for engineered T-cell therapy: it expresses cancer-testis antigens (NY-ESO-1, MAGE-A4), so afami-cel/tecelra—TCR T cells the immune system is reprogrammed to deploy—became the first such therapy approved for a solid tumor.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Synovial sarcoma's cancer-testis antigens depend on antigen presentation: dendritic cells process NY-ESO-1 and MAGE-A4 onto HLA, the step that primes the T cells engineered immunotherapies exploit—and the tumor evades this by downregulating MHC.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Synovial sarcoma is a rare primary cardiac sarcoma: though usually arising in limb soft tissue, it can originate in the heart or pericardium, presenting with obstruction or effusion and a grim prognosis given difficult surgical clearance.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Synovial sarcoma is a flagship for engineered T cells: it expresses NY-ESO-1, and afamitresgene autoleucel—TCR-engineered cytotoxic T cells targeting that antigen—won FDA approval in 2024 for this sarcoma, a first for solid-tumor TCR therapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Synovial sarcoma is an immunologically 'cold' tumor rich in macrophages: tumor-associated macrophages dominate its sparse immune infiltrate and suppress T-cell responses, helping explain why checkpoint inhibitors disappoint while TCR-engineered T cells work.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Synovial sarcoma runs an IGF-1 autocrine loop: the tumor overexpresses IGF1R and its ligands to drive growth and survival, so IGF1R inhibition has been explored as targeted therapy in this fusion-driven sarcoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — Synovial sarcoma is a chromatin disease: its SS18-SSX fusion hijacks the SWI/SNF (BAF) complex—which includes ARID1A—wrenching it onto the wrong genes, so the tumor is driven by epigenetic miswiring rather than classic mutations.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Synovial sarcoma's immunotherapy is limited by regulatory T cells: it expresses the NY-ESO-1 antigen targeted by TCR-engineered T cells, but a Treg-rich, suppressive microenvironment blunts the attack and curbs durable responses.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Synovial sarcoma grows on IGF-driven mTOR signaling: autocrine IGF-1 feeds the PI3K-AKT-mTOR axis to fuel proliferation, making mTOR a studied target in a sarcoma otherwise reliant on chemotherapy and surgery.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia stokes synovial sarcoma's aggressiveness: as the tumor outgrows its blood supply, low oxygen drives invasion and metastasis, contributing to the lung spread that threatens patients with this translocation-driven sarcoma.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Synovial sarcoma can spread to the brain: though lung is the dominant metastatic site, hematogenous spread occasionally seeds brain metastases in advanced disease, prompting imaging when neurologic symptoms appear.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Synovial sarcoma leans on AKT downstream of IGF: autocrine IGF-1 activates the PI3K-AKT-mTOR axis to drive proliferation and survival, so AKT-mTOR inhibitors are studied alongside the IGF and immune approaches in this sarcoma.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Synovial sarcoma sometimes calcifies: foci of calcium deposit within the tumor, and heavily calcified synovial sarcomas tend to carry a notably better prognosis than non-calcified ones.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Synovial sarcoma can spread to the liver: though it favors the lungs, hematogenous metastasis seeds the liver and other organs in advanced disease, marking the shift to systemic treatment.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Synovial sarcoma weaves a fibrous stroma: its spindle-cell component lays down dense collagen in the biphasic tumor, the firm fibrous tissue that, with epithelial nests, defines its histology.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy exposes synovial sarcoma's split personality: alongside the spindle cells sit true epithelial cells joined by desmosomes, sprouting microvilli into gland-like lumina over a basal lamina — the ultrastructure of its biphasic histology.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Synovial sarcoma can invade the skeleton: though it favors the lungs, late disease seeds bone and the marrow within, and tumors abutting a joint erode the neighboring bone as they grow.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Rarely synovial sarcoma is born in the kidney itself: primary renal synovial sarcoma, carrying the same SS18 fusion, is a recognized aggressive entity that masquerades as a more common kidney tumor until molecular testing reveals it.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Despite its name, synovial sarcoma weaves a fibrous tumor: its spindle cells sit in a collagen-rich stroma, often with stippled calcification, and the biphasic form adds glandular epithelium — a texture that, with the SS18 fusion, makes the diagnosis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The ifosfamide in its chemotherapy can fog the brain: a metabolite of this alkylator crosses into the CNS and poisons neurons, causing a reversible encephalopathy with confusion and seizures that methylene blue is used to treat.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Ifosfamide also injures the kidney's tubules: the resulting Fanconi-like syndrome wastes magnesium, phosphate, and bicarbonate into the urine, so electrolytes are monitored and replaced through synovial sarcoma treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody now clinches the diagnosis: a stain against the SS18-SSX fusion protein is highly specific for synovial sarcoma, and with TLE1 it confirms the t(X;18)-driven tumor that can otherwise mimic many spindle-cell cancers.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The doxorubicin-ifosfamide regimen empties the marrow: both drugs are heavily myelosuppressive, dropping neutrophil counts so that febrile neutropenia is a recurring hazard through synovial sarcoma chemotherapy.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Treatment and tumor both thin the red cells: the anthracycline-and-alkylator chemotherapy suppresses marrow erythrocyte production, leaving an anemia and fatigue that may need transfusion across the long course of care.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The doxorubicin-ifosfamide chemotherapy strains the heart: the anthracycline backbone for synovial sarcoma is cumulatively cardiotoxic to cardiomyocytes, so cardiac function is checked across treatment in these often-young patients.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cure can cost fertility: synovial sarcoma strikes adolescents and young adults, and its alkylating ifosfamide and any pelvic radiation damage the gonads, so fertility preservation is discussed before treatment begins.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — It is a hypoxic, vessel-hungry tumor: synovial sarcoma stabilizes HIF and pours out VEGF to feed its growth, the angiogenic drive behind the activity of anti-VEGF tyrosine-kinase inhibitors like pazopanib against it.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — It survives by blocking its own death: synovial sarcoma strongly and characteristically expresses the anti-apoptotic protein BCL-2 — useful as a diagnostic marker and a hint that drugs disabling this survival signal might work against it.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — A receptor it leans on: synovial sarcoma frequently overexpresses EGFR, feeding growth signals into its proliferation, which has made the receptor a studied (if so far disappointing) target in this fusion-driven sarcoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — It is a flagship for cell therapy: synovial sarcoma expresses the cancer-testis antigen NY-ESO-1, the target of engineered T-cell therapy, and natural killer and other cell-based approaches are pursued against a tumor that resists checkpoint drugs.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 backs its survival signaling: synovial sarcoma cells show STAT3 activation that supports proliferation and immune evasion, one of the cooperating pathways downstream of the SS18-SSX fusion that drives the tumor.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A solid cancer that clots: like other sarcomas, synovial sarcoma raises thrombosis risk through tumor-driven hypercoagulability, with deep-vein thrombosis and pulmonary embolism worsened by major limb surgery and chemotherapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Chemo neutropenia opens the door to infection: the ifosfamide-doxorubicin regimens used against synovial sarcoma cause deep neutropenia, so neutropenic fever and sepsis are recurrent treatment hazards.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Ifosfamide is hard on the kidney: the alkylator central to synovial-sarcoma chemotherapy is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment, especially with cumulative dosing.
- `connects-to` → **[AML](../aml/README.md)** — Its cure can sow a later leukemia: the alkylators and anthracyclines used against synovial sarcoma carry a small long-term risk of therapy-related myelodysplasia and acute myeloid leukemia in survivors.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Tumor inflammation and chemo blunt the marrow: advanced synovial sarcoma's inflammatory burden raises hepcidin while cytotoxic therapy suppresses erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracycline-based chemo strains the heart: doxorubicin, paired with ifosfamide as the mainstay for synovial sarcoma, is dose-dependently cardiotoxic and can leave a cardiomyopathy and heart failure in young survivors.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its intensive chemotherapy opens the lung to mold: the deep neutropenia of doxorubicin-ifosfamide therapy for synovial sarcoma lets inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A cancer of the young with hard therapy weighs on mood: synovial sarcoma's diagnosis in adolescents and young adults, disfiguring surgery and grueling chemotherapy contribute to depression and distress.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Wide excision in irradiated tissue heals slowly: local control of synovial sarcoma combines extensive limb surgery with radiation, and the irradiated, chemotherapy-suppressed bed leaves wounds prone to breakdown.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Tumour, surgery and chemo all wound the nerves: synovial sarcomas near limb nerves, the resections that sacrifice them and the chemotherapy used together produce lasting neuropathic pain.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A young cancer with lung-relapse risk breeds worry: the disfiguring surgery, lung-metastasis surveillance and uncertain prognosis of synovial sarcoma foster chronic anxiety in survivors alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to the lungs: synovial sarcoma metastasises preferentially to the lungs, so pulmonary metastasectomy and lung surveillance dominate its long-term management.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its chemo reawakens shingles: the doxorubicin-ifosfamide chemotherapy for synovial sarcoma deeply suppresses immunity, allowing latent varicella-zoster to reactivate.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its chemo injures the gut: the ifosfamide and doxorubicin used for synovial sarcoma cause nausea, mucositis and, with ifosfamide, hepatotoxicity.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It is a sarcoma that reaches the nodes: synovial sarcoma is one of the few sarcomas with notable lymph-node metastasis, so nodal assessment matters in its staging.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its chemotherapy injures the kidney and bladder: the ifosfamide in its regimen causes haemorrhagic cystitis and a Fanconi-like renal tubulopathy.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its cure can scar the heart: the doxorubicin in synovial-sarcoma chemotherapy carries a dose-dependent cardiotoxicity risk in the young patients it often affects.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It pioneered TCR cell therapy: synovial sarcoma expresses NY-ESO-1, the target of the first approved engineered TCR T-cell therapy (afami-cel), and pazopanib treats advanced disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Treatment and tumour reach the nerves: ifosfamide causes encephalopathy and peripheral neuropathy, and paraspinal synovial sarcoma can compress nerves.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It and its treatment mark the skin: chemotherapy causes alopecia and mucositis, radiotherapy produces dermatitis over the treated limb, and superficial tumours present as a skin-deep mass.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemosensitive among sarcomas: synovial sarcoma is one of the more chemoresponsive soft-tissue sarcomas, treated with ifosfamide and doxorubicin around surgery and radiotherapy, especially in younger patients with larger tumours.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — First solid tumour with engineered T-cells: synovial sarcoma frequently expresses MAGE-A4 and NY-ESO-1, and afami-cel — autologous TCR-engineered T-cells against MAGE-A4 — became the first approved engineered T-cell therapy for a solid tumour in this disease.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold tumour: despite its antigen expression, synovial sarcoma has a low mutational burden and sparse T-cell infiltrate, so PD-1 checkpoint blockade responds poorly — why adoptive engineered T-cells, not checkpoint inhibitors, broke through.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — It spreads to the lungs: synovial sarcoma metastasises predominantly to the lungs, seeding the alveolar parenchyma, so chest imaging stages the disease and pulmonary metastasectomy is part of treatment.
- `connects-to` → **[GIST](../gist/README.md)** — One driver defines each: synovial sarcoma is specified by the SS18-SSX fusion and GIST by activating KIT mutation—twin proofs that a single genetic lesion can create a sarcoma, though only GIST's is directly druggable with imatinib.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — Two ways to break SWI/SNF: synovial sarcoma's SS18-SSX fusion hijacks the BAF (SWI/SNF) chromatin complex, while clear cell ovarian cancer disables it through ARID1A loss—different routes to the same epigenetic dysregulation.
- `connects-to` → **[Desmoid Tumor](../desmoid-tumor/README.md)** — Two limb soft-tissue tumours, opposite fates: desmoid is a locally aggressive Wnt-driven fibromatosis that never metastasizes, whereas synovial sarcoma's deceptively slow growth hides a lethal capacity to spread.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Sarcomas of the young that home to lung: synovial sarcoma and osteosarcoma both strike adolescents and young adults and metastasize chiefly to the lungs, but osteosarcoma's chaotic genome contrasts with synovial sarcoma's single defining fusion.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — An immune desert: synovial sarcoma rarely forms the tertiary lymphoid structures and germinal-centre-like aggregates that mark hot tumours, explaining its poor checkpoint response and why engineered TCR cells were needed instead.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — A shared cancer-testis target: synovial sarcoma and melanoma both express NY-ESO-1, and engineered TCR T-cell therapy against it (afami-cel) won its first approval in synovial sarcoma after melanoma trials paved the way.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Juxta-articular invasion: arising near joints in the limbs, synovial sarcoma can erode adjacent cortical bone and metastasise to the skeleton, shaping the extent of limb-salvage surgery.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — A spindle-cell mimic near nerves: synovial sarcoma often arises beside nerves and shares a monophasic spindle-cell pattern with MPNST, the two sitting in the differential of a paraneural soft-tissue mass.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Fusion-driven oncogene: the SS18-SSX fusion retargets the BAF complex and activates MYC, driving the proliferation of synovial sarcoma.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: cyclin D1 upregulation, with CDKN2A loss, propels synovial sarcoma cells through the cell cycle, supporting CDK4/6-directed strategies.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo activation: nuclear YAP from deregulated Hippo signalling contributes to synovial sarcoma growth and its mesenchymal phenotype.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Autocrine growth: PDGF signalling, an output of the SS18-SSX-driven transcriptional programme, supports the proliferation of synovial sarcoma.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Growth-factor signalling: FGFR signalling contributes to synovial sarcoma proliferation, a candidate targetable receptor in this fusion-driven sarcoma.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Receptor activation: MET signalling promotes the growth and invasion of synovial sarcoma, part of the receptor-tyrosine-kinase landscape of the tumour.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — The SS18-SSX fusion reactivates Notch alongside Wnt signaling in synovial sarcoma, redeploying a developmental program to sustain the proliferation of this monomorphic blue-cell tumor—part of the aberrant transcriptional state the fusion creates.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β in the synovial-sarcoma microenvironment promotes an EMT-like invasive phenotype and excludes T cells—a barrier directly relevant to the engineered NY-ESO-1 TCR T-cell therapies (afami-cel) now approved for the disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on synovial-sarcoma cells responds to CXCL12 gradients toward the lung, contributing to the pulmonary metastases that are the principal cause of death in this otherwise often slow-growing sarcoma.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDKN2A loss is common in synovial sarcoma, releasing CDK4/6-cyclin-D to drive the cell cycle and providing a rationale for CDK4/6 inhibitors in tumors that have deleted their p16 brake.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits tumor-associated macrophages into synovial sarcoma, building a myeloid-rich immunosuppressive microenvironment that helps explain the limited efficacy of checkpoint blockade despite the tumor's NY-ESO-1 antigen.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Synovial sarcoma is one of the more chemosensitive soft-tissue sarcomas, and doxorubicin and ifosfamide kill its cells through caspase-3-mediated apoptosis, the cytotoxic backbone of treatment alongside surgery.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR signaling (AKT and mTOR already mapped) is activated in synovial sarcoma and supports growth and survival, a targetable dependency downstream of its receptor tyrosine kinases.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Deregulated RB-E2F1 transcription powers the proliferation of synovial sarcoma, cooperating with the CDK4/6-cyclin-D and CDKN2A lesions already mapped.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase activity promotes the proliferation and invasive migration of synovial sarcoma cells, relayed from the MET, FGFR and EGFR receptor tyrosine kinases already mapped.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The MET, FGFR, EGFR and IGF-1R receptors (all mapped) converge on the MAPK-ERK cascade driving proliferation in synovial sarcoma.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN limits the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped), an IGF-1R-driven survival pathway active in synovial sarcoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — Synovial sarcoma usually retains wild-type TP53 (mapped) held in check by MDM2, making MDM2 inhibition a strategy to reactivate p53-driven apoptosis.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (CDK4/6, CDKN2A and cyclin-D1 already mapped) contributes to the proliferation of synovial sarcoma.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-ERK signaling (ERK1/2 already mapped) downstream of the receptor tyrosine kinases active in synovial sarcoma provides a proliferative input.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) contributes to the survival signaling of synovial sarcoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the invasion and survival of synovial sarcoma cells.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) shapes the fibrotic and immunosuppressive microenvironment of synovial sarcoma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment relevant to the NY-ESO-1-directed cell therapy and immunotherapy of synovial sarcoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of synovial sarcoma, relevant to its NY-ESO-1-directed cell therapy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by the PI3K-AKT axis, modulate the survival of the SS18-SSX-driven cells of synovial sarcoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 cytotoxicity is the effector mechanism of the NY-ESO-1-directed cell therapy used in synovial sarcoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin signaling aberrantly activated by the SS18-SSX fusion of synovial sarcoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the immunosuppressive tumor microenvironment of synovial sarcoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation that cooperates with the BAF-complex disruption of synovial sarcoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of the SS18-SSX-driven cells of synovial sarcoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of synovial sarcoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) shapes the inflammatory microenvironment of synovial sarcoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of synovial sarcoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of synovial sarcoma.
- `connects-to` → **[CDKN1A](../../03-molecular/cdkn1a/README.md)** — CDKN1A-p21 cell-cycle control participates in the checkpoint regulation dysregulated in synovial sarcoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of synovial sarcoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of synovial sarcoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of synovial sarcoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — TCR immunotherapy: synovial sarcoma frequently expresses the cancer-testis antigens NY-ESO-1 and MAGE-A4 and is the leading solid tumour for HLA-restricted engineered T-cell therapy, so antigen-presentation machinery governs its landmark response to TCR-T cells.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Invasion and resistance: the AXL receptor tyrosine kinase is expressed in synovial sarcoma and drives the mesenchymal invasion and drug-tolerant phenotype behind its lung-tropic metastatic course, a candidate target beyond conventional chemotherapy.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Tumour angiogenesis: synovial sarcoma is a vascular soft-tissue sarcoma whose growth depends on neovascularisation driven by angiopoietin-Tie2 and VEGF (VEGF already mapped), the rationale for antiangiogenic tyrosine-kinase inhibitors like pazopanib.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Engineered T-cell therapy: IL-2-driven T-cell expansion underlies the NY-ESO-1-directed TCR T-cell therapy (afamitresgene autoleucel), the first cell therapy approved for synovial sarcoma, which characteristically expresses cancer-testis antigens.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the doxorubicin-based chemotherapy used for synovial sarcoma is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that limits its cumulative dose.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Chemotherapy anaemia: the intensive chemotherapy used in synovial sarcoma is myelosuppressive, lowering haemoglobin and causing the anaemia that requires transfusion and growth-factor support during treatment.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion relevant to the NY-ESO-1 TCR-T cell therapy (CD8 already mapped) approved for synovial sarcoma.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and lysis stress: the doxorubicin-ifosfamide chemotherapy of synovial sarcoma generates oxidative stress and, in bulky disease, cell lysis releasing purines that xanthine oxidase converts to uric acid, adding oxidative and tumour-lysis burden.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of synovial sarcoma, part of the stromal microenvironment of this deep soft-tissue sarcoma of young adults.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, immune-evasive microenvironment of synovial sarcoma that the NY-ESO-1 TCR-T therapy must overcome.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the doxorubicin-ifosfamide chemotherapy of synovial sarcoma is myelosuppressive, causing anaemia (haemoglobin already mapped) that needs transfusion whose repeated support can load the young survivor with iron.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton radiotherapy: proton-beam radiotherapy provides local control of synovial sarcoma while sparing the surrounding normal tissue, an option especially valuable in the young patients typical of this sarcoma.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive cold microenvironment of synovial sarcoma.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages (CCL2 already mapped) infiltrate the synovial-sarcoma stroma, and their M2 polarisation (IL-4 already mapped) supports the immunosuppression relevant to the NY-ESO-1 TCR-T therapy.
- `connects-to` → **[Cortical bone](../../05-tissue/cortical-bone/README.md)** — Bone invasion: the para-articular synovial sarcoma can invade the adjacent cortical bone, part of the locally aggressive behaviour of this deep soft-tissue sarcoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic microenvironment: leptin from the marrow and stromal adipose tissue signals within the metabolic microenvironment of the metastatic synovial sarcoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipose adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the microenvironment of synovial sarcoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the synovial-sarcoma microenvironment.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the NY-ESO-1 TCR-T immunotherapy of synovial sarcoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm engaged by the NY-ESO-1 (MHC already mapped) TCR-T cells against synovial sarcoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of synovial sarcoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of synovial sarcoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the synovial-sarcoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the synovial-sarcoma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of synovial sarcoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the microenvironment that the NY-ESO-1 TCR-engineered T-cell therapy of synovial sarcoma must overcome.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) recruits and polarises the myeloid cells to an immunosuppressive phenotype in the synovial-sarcoma microenvironment.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of synovial sarcoma and the NY-ESO-1 TCR-T context.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the myeloid-driven immunosuppression of the synovial-sarcoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the synovial-sarcoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped) within the immunosuppressive microenvironment.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Sarcoma stromal alarmin: TSLP released from the SYT-SSX-driven synovial sarcoma stroma activates mast cells and dendritic cells, promoting the immunosuppressive type-2 microenvironment that blunts NY-ESO-1-targeted cytotoxic immunity.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chemotherapy anaemia: erythropoietin corrects the ifosfamide/doxorubicin-induced anaemia in synovial sarcoma, and EPOR expression on the tumour cells has been reported, suggesting possible direct trophic effects.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM invasion scaffold: periostin, an ECM glycoprotein of the synovial sarcoma stromal niche, promotes the local invasion and lung metastasis of the SYT-SSX-rearranged sarcoma cells and contributes to the desmoplastic microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin tumour-microenvironment mediator: bradykinin, generated by kallikrein-kinin activation in the synovial-sarcoma stroma, amplifies vascular permeability and the pro-tumourigenic microenvironment of the SYT-SSX-driven sarcoma.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact-complement regulation: C1-esterase inhibitor restrains the classical complement C1 and the contact system in the synovial-sarcoma microenvironment (C3/C5/C5aR1 already mapped), limiting complement-driven immune escape.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell sarcoma mediator: histamine from mast cells in the synovial-sarcoma stroma promotes vascular permeability and the immunosuppressive tumour microenvironment, contributing to the immune evasion of this SYT-SSX-fusion-driven sarcoma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — SyS melatonin: melatonin suppresses synovial-sarcoma proliferation via MT1/MT2 receptor-mediated inhibition of mTOR (already mapped) and ERK1/2 (already mapped) signalling, while enhancing NK-cell (already mapped) cytotoxicity against the SS18-SSX-driven tumour.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — SyS testosterone: androgen receptor is expressed by a subset of synovial-sarcoma cells; testosterone drives androgen receptor-mediated upregulation of SS18-SSX (already mapped) transcriptional programme, and androgen-axis suppression reduces synovial-sarcoma tumour proliferation.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — SyS serotonin: serotonin produced by neuroendocrine-differentiated synovial-sarcoma cells drives autocrine 5-HT receptor proliferative signalling and promotes tumour angiogenesis (VEGF already mapped), contributing to the disease progression of this SYT-SSX-rearranged sarcoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — SyS oxytocin: oxytocin receptor on synovial-sarcoma cells attenuates SS18-SSX (already mapped) transcriptional reprogramming and WNT/β-catenin (already mapped) signalling; oxytocin-driven cAMP/PKA activation limits YAP1 (already mapped) co-activator-mediated tumour proliferation.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — SyS vasopressin: vasopressin V1A receptors on synovial-sarcoma cells activate SRC-kinase (already mapped) and ERK1/2 (already mapped), amplifying the SS18-SSX (already mapped)-driven transcriptional reprogramming of this SYT-rearranged soft-tissue sarcoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — SyS selenium: selenium-dependent GPX4 suppresses ferroptosis-resistance in synovial-sarcoma; GPX4 inhibition synergises with EZH2 (already mapped) targeted therapy to overcome epigenetic reprogramming driven by the SS18-SSX (already mapped) fusion oncoprotein.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — SyS iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour surveillance; thyroid deficiency amplifies VEGF (already mapped) and mTOR (already mapped) and IL-6 (already mapped) tumour-promotion cascade of synovial sarcoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — SyS sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced IL-6 (already mapped) amplifies the VEGF (already mapped) and mTOR (already mapped) and YAP1 (already mapped)-driven proliferative cascade of synovial sarcoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — SyS copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped), drives stromal remodelling; copper amplifies VEGF (already mapped) angiogenesis; copper deficiency impairs macrophage (already mapped) and T-cytotoxic-cell (already mapped) immunity in SyS.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — SyS zinc: zinc, as metalloproteinase cofactor in macrophages (already mapped) and T-cytotoxic-cell (already mapped), supports anti-tumour immunity; zinc deficiency amplifies IL-6 (already mapped) and VEGF (already mapped) and mTOR (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — SyS potassium: potassium efflux gates macrophage (already mapped) NLRP3; potassium loss amplifies IL-6 (already mapped) and WNT (already mapped) and mTOR (already mapped) proliferative cascade and suppresses T-cytotoxic-cell (already mapped) immunity in SyS.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — SyS phosphorus: phosphorus, as ATP donor in mTOR (already mapped) kinase signalling in fibroblasts (already mapped) and macrophages (already mapped), fuels sarcoma proliferation; phosphorus dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) in SyS.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — SyS carbon: carbon, as metabolic backbone of mTOR (already mapped) and VEGF (already mapped) in fibroblasts (already mapped) and macrophages (already mapped), drives proliferative signalling; carbon dysregulation amplifies IL-6 (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — SyS chloride: chloride channels in macrophages (already mapped) and fibroblasts (already mapped) regulate tumour-immune homeostasis; chloride dysregulation amplifies IL-6 (already mapped) and WNT (already mapped) and mTOR (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — SyS hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and fibroblasts (already mapped), modulates tumour immune balance; hydrogen dysregulation amplifies IL-6 (already mapped) and WNT (already mapped) and VEGF (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — SS nitrogen: nitric oxide from macrophages (already mapped) and tumor-associated endothelial cells modulates vascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour growth cascade of synovial sarcoma.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — SS sulfur: hydrogen sulfide from macrophages (already mapped) and endothelial cells modulates tumour vascular tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — SS GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells modulates metabolic-immune balance; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — SS angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives tumour angiogenesis; angiotensin-ii excess amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — SS rankl: RANKL from macrophages (already mapped) and tumour cells (already mapped) promotes bone remodelling in synovial sarcoma; rankl excess amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — SS fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds synovial sarcoma ECM; fibronectin excess amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — SS activin-a: activin-A from macrophages (already mapped) and fibroblasts (already mapped) drives synovial sarcoma fibrosis; activin-a excess amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — SS cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates synovial sarcoma vascular tone; cgrp excess amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of synovial sarcoma.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — SS calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates calcium signalling in synovial sarcoma; calcitonin dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of synovial sarcoma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^kadoch-2013-ss18-ssx-baf]: Kadoch C, Crabtree GR. Reversible disruption of mSWI/SNF (BAF) complexes by the SS18-SSX oncogenic fusion in synovial sarcoma. *Cell.* 2013;153(1):71-85. [doi:10.1016/j.cell.2013.02.036](https://doi.org/10.1016/j.cell.2013.02.036) · [PubMed 23540691](https://pubmed.ncbi.nlm.nih.gov/23540691/)
[^kawai-2015-trabectedin-synovial]: Kawai A, Araki N, Sugiura H, et al. Trabectedin monotherapy after standard chemotherapy versus best supportive care in patients with advanced, translocation-related sarcoma: a randomised, open-label, phase 2 study. *Lancet Oncol.* 2015;16(4):406-416. [doi:10.1016/S1470-2045(15)70098-7](https://doi.org/10.1016/S1470-2045(15)70098-7) · [PubMed 25795407](https://pubmed.ncbi.nlm.nih.gov/25795407/)
