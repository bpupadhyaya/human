---
schema: human-scale-entry/v1
id: hodgkin-lymphoma
name: Hodgkin Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Hodgkin lymphoma is a GC B cell-derived malignancy; RS cells ~100% CD30+; 9p24.1 amplification drives CD30+PD-L1/L2 co-expression; A+AVD (ECHELON-1) is standard for advanced stage; nivolumab/pembrolizumab for R/R; 5-year OS >85% overall; NLPHL has distinct CD20+ biology."
aliases: ["Hodgkin lymphoma", "HL", "cHL", "classical Hodgkin lymphoma", "NLPHL", "Reed-Sternberg", "Hodgkin disease", "nodular sclerosis HL", "mixed cellularity HL"]
sources:
  - id: connors-2018-echelon1
    type: peer-reviewed
    cite: "Connors JM, Jurczak W, Straus DJ, et al. Brentuximab vedotin with chemotherapy for stage III or IV Hodgkin's lymphoma. N Engl J Med. 2018;378(4):331-344."
    doi: "10.1056/NEJMoa1708984"
    pmid: "29360494"
    url: "https://doi.org/10.1056/NEJMoa1708984"
  - id: armand-2018-nivo-hl
    type: peer-reviewed
    cite: "Armand P, Engert A, Younes A, et al. Nivolumab for relapsed/refractory classic Hodgkin lymphoma after failure of autologous hematopoietic cell transplantation: extended follow-up of the multicohort single-arm phase II CheckMate 205 trial. J Clin Oncol. 2018;36(14):1428-1439."
    doi: "10.1200/JCO.2017.77.6717"
    pmid: "29584546"
    url: "https://doi.org/10.1200/JCO.2017.77.6717"
cross_links:
  - target: 01-human/03-molecular/cd30
    relation: connects-to
    note: "CD30 is expressed on ~100% of RS cells (WHO diagnostic criterion for cHL); brentuximab vedotin is the backbone of A+AVD (ECHELON-1) and consolidation post-auto-SCT (AETHERA); 9p24.1 amplification co-amplifies CD30 with PD-L1/PD-L2 in RS cells."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "9p24.1 amplification in RS cells drives PD-L1/PD-L2 overexpression → profound T-cell exhaustion in tumor microenvironment; nivolumab (CheckMate 205) and pembrolizumab (KEYNOTE-087) show ORR ~65-70% in R/R cHL; KEYNOTE-204 (pembrolizumab vs BV): PFS 13.2 vs 8.3 months."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is constitutively active in RS cells via CD30, CD40, EBV-LMP1, and CARD11 signaling; NF-κB drives RS cell survival by upregulating BCL-2, BCL-XL, and cFLIP; microenvironmental TNF-α further activates NF-κB; NF-κB inhibition is a preclinical therapeutic target in R/R cHL."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "9p24.1 amplification co-amplifies JAK2 with PD-L1/PD-L2 and CD30 in RS cells; JAK2 → constitutive STAT6 → IL-13 autocrine + PD-L1 transcription; ruxolitinib studied in R/R cHL; JAK2 amplification is a primary oncogenic driver in cHL."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Reed-Sternberg cells arise from germinal-center B cells that acquired crippling Ig V-gene mutations and should have died during negative selection; they survive via CD30/CD40/NF-κB and EBV rescue while shedding the B-cell program (no surface Ig, loss of OCT2/BOB1)."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV is found in 30-50% of classical HL (up to 80-90% in lymphocyte-depleted and HIV-associated cases); its LMP1 protein mimics a constitutively active CD40 receptor → NF-κB survival signaling in RS cells; prior infectious mononucleosis roughly triples HL risk."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 status splits Hodgkin lymphoma: RS cells of classical HL are CD20-negative, whereas the popcorn (L&H) cells of NLPHL retain the B-cell program and are CD20-positive — making rituximab effective in NLPHL but not classical HL."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Hodgkin lymphoma is unusual: malignant Reed-Sternberg cells are <1% of the tumor, the bulk being reactive CD4+ T cells (rosetting around RS cells), eosinophils, and histiocytes that RS cells recruit and depend on — why PD-1 blockade freeing exhausted T cells works so well."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is a key Hodgkin lymphoma site: classical HL spreads contiguously node to adjacent node and to the spleen, and splenic involvement upstages disease and historically guided staging laparotomy; this orderly spread (unlike scattered NHL) reflects HL's lymphatic biology."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Hodgkin lymphoma is the prototypical lymphatic-system cancer: it arises in lymph nodes and spreads in an orderly, contiguous fashion down chains of nodes (Ann Arbor staging), usually as painless cervical or mediastinal adenopathy — distinguishing it from non-Hodgkin lymphomas."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Hodgkin lymphoma and DLBCL are the two ends of large-B-cell lymphoma, bridged by gray-zone lymphoma: classic Hodgkin's CD30+ Reed-Sternberg cells lose most B-cell markers while DLBCL keeps them, and gray-zone tumors share both—the distinction drives very different chemo."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "The Reed-Sternberg cell of classic Hodgkin lymphoma is a crippled B cell: a germinal-center B cell that lost its B-cell receptor and most B-lineage markers yet escaped apoptosis via constitutive NF-κB and EBV, surviving as a rare malignant cell amid a reactive immune infiltrate."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV raises Hodgkin lymphoma risk several-fold and changes its biology: HIV-associated Hodgkin is almost always EBV-driven, presents at advanced stage with B symptoms and marrow involvement, and—unlike AIDS-defining lymphomas—its incidence did not fall with antiretroviral therapy."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is woven into Hodgkin lymphoma's cure: because HL spreads contiguously between nodes, involved-site photon irradiation (lower-dose, after chemo) controls it well—but extended-field radiation's late second cancers and heart disease pushed toward less."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Hodgkin lymphoma is mostly microenvironment: the malignant Reed-Sternberg cells are rare amid an immune infiltrate, and abundant tumor-associated macrophages predict worse outcomes—so the supporting macrophages, not just the cancer cells, shape prognosis."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Hodgkin lymphoma and CLL are both B-cell neoplasms that can intersect through transformation: CLL occasionally undergoes Richter transformation into Hodgkin lymphoma, and both can be EBV-associated—so an indolent leukemia can give rise to an aggressive lymphoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Hodgkin lymphoma evades NK and immune killing despite few tumor cells: the rare Reed-Sternberg cells survive amid abundant immune cells by suppressing NK and T-cell attack and overexpressing PD-L1—why PD-1 blockade is strikingly effective in Hodgkin lymphoma."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone marrow involvement upstages Hodgkin lymphoma: though it usually spreads predictably node-to-node, marrow infiltration signals advanced (stage IV) disease, so staging marrow assessment (now often PET) guides whether limited or extended chemotherapy is used."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Reed-Sternberg cells secrete IL-10 to build an immunosuppressive niche: this and other cytokines recruit and pacify the reactive immune cells that make up most of the tumor, letting the few malignant cells thrive—explaining Hodgkin lymphoma's odd cellular makeup."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Nodular sclerosing Hodgkin lymphoma favors the mediastinum near the thymus: it classically presents as an anterior mediastinal mass in young adults, so it enters the differential of a mediastinal mass alongside thymoma and germ-cell tumors."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Hodgkin lymphoma commonly causes anemia: cytokines from Reed-Sternberg cells drive anemia of chronic disease, and marrow involvement or autoimmune hemolysis can deepen it—so falling red cells are part of the systemic 'B-symptom' illness of advanced HL."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Hodgkin lymphoma thrives by hijacking the immune system: Reed-Sternberg cells amplify PD-L1 to silence surrounding T cells and recruit a protective inflammatory infiltrate, which is exactly why PD-1 checkpoint blockade is strikingly effective in relapsed HL."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Hodgkin lymphoma has a curious alcohol sign: in a minority of patients, drinking alcohol triggers pain in affected lymph nodes within minutes—an unusual, near-specific clue that points to Hodgkin rather than other lymphomas."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Curing Hodgkin lymphoma can later cost the heart: chest radiation and anthracycline chemotherapy raise the risk of coronary disease, valve damage, and heart failure decades on, so cardiac surveillance is central to long-term survivor care."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Curing Hodgkin lymphoma raises later breast cancer risk: chest (mantle) radiation in young women sharply increases breast cancer decades later, so female survivors irradiated young begin breast MRI screening years before the general population."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Hodgkin lymphoma is mostly a crowd of protective cells: the rare malignant Reed-Sternberg cells survive by surrounding themselves with regulatory T cells and other immune cells that shield them, so the tumor is <1% cancer cells and 99% recruited defenders."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Nodular sclerosis Hodgkin lymphoma is defined by fibrosis: broad bands of collagen divide the lymph node into nodules, the histologic signature of the commonest subtype, typically affecting the chest of young adults."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Reed-Sternberg cells grow on their own IL-13: they secrete this Th2 cytokine as an autocrine growth signal and to recruit the eosinophil-rich infiltrate, shaping the inflammatory backdrop that defines Hodgkin lymphoma."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Hodgkin lymphoma centers on the chest and threatens the lungs: it classically forms a mediastinal mass and can invade lung tissue, while bleomycin in its chemotherapy risks pulmonary fibrosis—so the lungs matter both to the disease and its cure."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta lays down the bands of nodular sclerosis Hodgkin: the commonest subtype is defined by collagen bands that TGF-beta drives fibroblasts to deposit, walling the Reed-Sternberg cells into fibrous nodules."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells fill Hodgkin's reactive infiltrate: the tumor is mostly normal immune cells around scarce Reed-Sternberg cells, and dysfunctional antigen presentation by dendritic cells helps the malignant cells evade the surrounding immunity."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Hodgkin lymphoma drains the body's iron: its systemic inflammation and any marrow involvement suppress red-cell production and lock iron away, so anemia of chronic disease is a common feature."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Hodgkin lymphoma can itch through the skin: severe generalized pruritus, sometimes with the lymph-node pain that alcohol triggers, is a classic paraneoplastic symptom that may precede the diagnosis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells populate the Hodgkin microenvironment: drawn around the Reed-Sternberg cells, they engage CD30 ligand to support the malignant cells, and their numbers can track with prognosis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Hodgkin can raise blood calcium: its activated macrophages convert vitamin D to its active form, driving the hypercalcemia it shares with granulomatous diseases."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Hodgkin's classic kidney lesion is minimal-change nephrotic syndrome: the lymphoma's cytokines make the glomeruli leak protein, a paraneoplastic effect that resolves when the cancer is treated."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Hodgkin draws eosinophils with IL-5: the Reed-Sternberg cells secrete it to recruit the eosinophils that fill the reactive infiltrate, part of the inflamed microenvironment that hides the rare malignant cells."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy hunts Hodgkin's rare giant cell: the binucleate Reed-Sternberg cell with its two huge 'owl-eye' nucleoli sits sparse amid a sea of reactive immune cells, the diagnostic needle in the haystack."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Advanced Hodgkin lymphoma involves the liver: stage IV disease seeds hepatic deposits, and bulky disease can crowd the organ, a marker of widespread spread beyond the lymph nodes and spleen."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Hodgkin rarely strays into the gut: primary or secondary gastrointestinal involvement of the bowel is uncommon for a disease that spreads node to node, but it occurs in advanced or immunosuppressed cases."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Hodgkin is exquisitely vulnerable to antibody drugs: brentuximab vedotin, an anti-CD30 antibody-drug conjugate, and the checkpoint antibodies nivolumab and pembrolizumab have transformed treatment of relapsed disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Curing Hodgkin frays the nerves: both the vincristine of ABVD and brentuximab vedotin injure peripheral neurons into a dose-limiting neuropathy that often dictates how much treatment a patient can take."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It strikes the young, so fertility matters: the alkylating chemotherapy of escalated regimens and any pelvic radiation can cause infertility, so sperm banking and ovarian preservation are offered before treatment."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Neck radiation lands on the thyroid: the mantle or involved-field irradiation that helps cure Hodgkin commonly leaves survivors hypothyroid years later, and carries a long-term risk of radiation-induced thyroid cancer."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The cure can seed a second blood cancer: the alkylating agents and radiation used against Hodgkin carry a delayed risk of therapy-related myelodysplastic syndrome and acute leukemia, among the most feared late effects of treatment."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Hodgkin can turn the immune system on the platelets: it is a recognized cause of secondary immune thrombocytopenia, and the chemotherapy that treats it suppresses platelet production too, so bleeding and low counts are watched for."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK-STAT3 keeps the Reed-Sternberg cell alive: constitutive STAT3 signaling, downstream of JAK2 and cytokine loops, sustains the malignant cell and shapes the immunosuppressive milieu around it."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Reed-Sternberg cells recruit a reactive crowd: the cytokines they secrete pull in neutrophils, eosinophils, and other inflammatory cells that vastly outnumber the rare tumor cells in the node."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The cure shadows the survivor's heart: anthracycline chemotherapy and mediastinal radiation cause late cardiomyopathy, valve disease, and heart failure, among the leading non-relapse causes of death in long-term Hodgkin survivors."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 carries the B symptoms: Reed-Sternberg cells and their reactive infiltrate pour out IL-6, driving the fevers, night sweats, and weight loss that mark advanced Hodgkin lymphoma and track with worse prognosis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Treatment and asplenia open the door to sepsis: chemotherapy neutropenia and the splenectomy or splenic radiation once used leave Hodgkin patients vulnerable to overwhelming infection from encapsulated bacteria."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A bulky mediastinal mass clots the blood: Hodgkin lymphoma, especially with a large mediastinal tumor compressing veins, carries a high venous thromboembolism risk during diagnosis and treatment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Its cytokines blunt the marrow: the IL-6 and inflammatory output of Hodgkin lymphoma — the same drive behind its B symptoms — suppresses erythropoiesis, producing an anemia of chronic disease that tracks with tumor burden."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Cure casts a long shadow: decades after thoracic (mantle) radiotherapy, Hodgkin survivors face a markedly raised risk of second cancers including lung cancer, a central concern of long-term survivorship care."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Impaired cell-mediated immunity invites an opportunist: Hodgkin lymphoma classically weakens T-cell immunity, and with chemotherapy this leaves patients at risk of Pneumocystis pneumonia, prompting prophylaxis."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its cure can sow a leukemia: the alkylators and etoposide used to treat Hodgkin lymphoma carry a real risk of therapy-related myelodysplasia and acute myeloid leukemia years later, a feared late effect."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "Mantle radiation breeds lung cancer: decades after chest radiotherapy, and amplified by smoking, Hodgkin survivors face a sharply raised risk of lung cancer including the aggressive small cell type."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Neck and chest radiation scar the arteries: mediastinal and cervical radiotherapy for Hodgkin lymphoma accelerates carotid and coronary atherosclerosis, raising the long-term risk of stroke in survivors."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its chemo injures the nerves: the vinblastine in ABVD and brentuximab vedotin used for Hodgkin lymphoma cause a dose-limiting peripheral neuropathy with numbness and neuropathic pain."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemotherapy opens the lung to mold: the neutropenia from Hodgkin-lymphoma chemotherapy, and bleomycin lung injury, can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A cancer of the young and its long survivorship weigh on mood: the diagnosis in young adults, intensive therapy and decades of late-effect surveillance contribute to depression in Hodgkin survivors."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its drugs and bulk attack the lungs: bleomycin in ABVD causes pulmonary fibrosis, and a bulky mediastinal Hodgkin mass can compress the airway and superior vena cava."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Mantle radiation silences glands and gonads: neck radiotherapy for Hodgkin lymphoma causes late hypothyroidism, while chemotherapy and pelvic radiation impair fertility and gonadal function."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A young cancer with decades of late-effect risk breeds worry: the diagnosis in youth and the lifelong surveillance for second cancers and cardiac and lung damage foster chronic health anxiety."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its cure scars the heart for decades: mediastinal radiation and the doxorubicin in ABVD cause late premature coronary disease, valve damage and cardiomyopathy in young survivors."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It announces itself through the skin: severe generalised pruritus is a classic constitutional feature of Hodgkin lymphoma, and alcohol-induced pain at involved nodes is a curious sign."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It can leak protein from the kidney: Hodgkin lymphoma is the cancer most classically associated with paraneoplastic minimal-change nephrotic syndrome, which resolves when the lymphoma is treated."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It reaches bone and marrow: advanced Hodgkin lymphoma can infiltrate the bone marrow and skeleton, and treatment-related avascular necrosis follows long steroid use."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can attack the nerves remotely: Hodgkin lymphoma is a classic cause of paraneoplastic cerebellar degeneration and limbic encephalitis, and vinca-alkaloid chemotherapy causes peripheral neuropathy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can involve gut and liver: Hodgkin lymphoma occasionally infiltrates the liver and gastrointestinal tract, and treatment brings nausea and hepatotoxicity."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "ABVD cures most: doxorubicin-bleomycin-vinblastine-dacarbazine chemotherapy, sometimes with radiation, cures the great majority of Hodgkin lymphoma."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Brentuximab targets CD30: the anti-CD30 antibody-drug conjugate brentuximab vedotin, replacing bleomycin in A+AVD, is central to modern Hodgkin lymphoma treatment."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Uniquely sensitive to PD-1 blockade: 9p24.1 amplification floods Reed-Sternberg cells with PD-L1, making Hodgkin lymphoma exquisitely responsive to nivolumab and pembrolizumab."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "The cure can wound the heart: doxorubicin in ABVD and mediastinal radiotherapy injure the myocardium, so cardiomyopathy and heart failure are leading late causes of death in patients cured of Hodgkin lymphoma decades earlier."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Two lymphomas born in the germinal center: Hodgkin lymphoma scatters rare Reed-Sternberg cells through a reactive infiltrate, while follicular lymphoma fills nodes with malignant BCL2-driven germinal-center B cells—shared origin, opposite tumour cellularity."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Engineering T cells against CD30: after brentuximab and checkpoint blockade, anti-CD30 CAR-T cells are in trials for relapsed Hodgkin lymphoma, aiming at the same surface marker the antibody-drug conjugate targets on Reed-Sternberg cells."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Two EBV-linked B-cell lymphomas: Hodgkin and Burkitt both derive from germinal-centre B cells and associate with EBV, contrasting an indolent-curable nodal lymphoma with the fastest-growing human tumour."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Mediastinal disease and lung toxicity: bulky mediastinal Hodgkin and the bleomycin and radiation used to cure it injure the alveoli, causing pneumonitis and pulmonary fibrosis."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "A radiation late effect: neck radiotherapy for Hodgkin lymphoma raises the long-term risk of thyroid cancer and hypothyroidism, a survivorship concern decades after cure."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Radiation's late heart disease: mediastinal radiotherapy for Hodgkin lymphoma accelerates coronary atherosclerosis and valve disease over decades, a leading cause of late mortality in cured survivors."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Paraneoplastic kidney: Hodgkin lymphoma is the classic cause of paraneoplastic minimal-change nephrotic syndrome, the glomerulus leaking massive protein in response to lymphoma-derived cytokines."
  - target: 02-pathogen/04-parasites/leishmania-donovani
    relation: connects-to
    note: "A great mimic: visceral leishmaniasis causes fever, weight loss and massive splenomegaly that can mimic Hodgkin lymphoma, an infectious differential to consider in endemic areas."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "Raised risk despite ART: unlike most cancers, Hodgkin lymphoma incidence is markedly increased in HIV infection, often EBV-driven, making it a key non-AIDS-defining malignancy."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Reactive microenvironment: Hodgkin lymphoma is dominated by a reactive infiltrate of plasma cells, T cells and eosinophils surrounding the rare malignant Reed-Sternberg cells."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Late radiation cancer: survivors who received subdiaphragmatic radiation for Hodgkin lymphoma face an increased long-term risk of gastric cancer, a delayed treatment complication."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Microenvironment cytokine: Reed-Sternberg cells secrete TNF-α to recruit and sustain the reactive inflammatory infiltrate that surrounds and protects them."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: Reed-Sternberg cells release CCL2 to draw in tumour-associated macrophages, whose abundance is an adverse prognostic marker in Hodgkin lymphoma."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Nodal angiogenesis: VEGF drives the angiogenesis of the involved lymph nodes in Hodgkin lymphoma, supporting tumour growth within the reactive microenvironment."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Glycolytic Reed-Sternberg cells: HIF-1α drives the avid glycolytic metabolism of Hodgkin lymphoma cells, the basis of its intense FDG-PET avidity used for staging and response assessment."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Interferon-driven PD-L1: IFN-γ in the Hodgkin microenvironment, with 9p24 amplification, upregulates PD-L1 on Reed-Sternberg cells, the basis of Hodgkin lymphoma's exquisite sensitivity to PD-1 blockade."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell survival rescue: BAFF supports the survival of the crippled germinal-centre B cells from which Reed-Sternberg cells derive, helping them escape the apoptosis their defective B-cell receptor should trigger."
  - target: 01-human/03-molecular/lmp1
    relation: connects-to
    note: "EBV-driven NF-κB: in EBV-positive classical Hodgkin lymphoma, the viral protein LMP1 mimics a constitutively active CD40 receptor to drive the NF-κB signalling on which the Reed-Sternberg cells depend for survival."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "9p24.1 amplification: the 9p24.1 amplification of Hodgkin lymphoma co-amplifies JAK2 with PD-L1, driving JAK-STAT signalling and the PD-L1 expression behind both JAK-inhibitor interest and the exquisite PD-1 sensitivity."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Reinvigorated cytotoxicity: the CD8 T cells surrounding Reed-Sternberg cells are exhausted, and PD-1 blockade restores their perforin-mediated killing — the mechanism of Hodgkin lymphoma's remarkable response to checkpoint inhibitors."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: ABVD and escalated-BEACOPP chemotherapy kill Reed-Sternberg cells through caspase-3-mediated apoptosis, the cytotoxic backbone that cures the majority of Hodgkin lymphoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune evasion: Reed-Sternberg cells often downregulate MHC class I and II to escape T-cell recognition, an antigen-presentation defect that, with their PD-L1 amplification, shapes the immunosuppressed niche they build around themselves."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Nodular sclerosis: the commonest Hodgkin subtype, nodular sclerosis, is defined by broad collagen bands that divide the node into nodules, a fibrotic stromal reaction orchestrated by the cytokine-secreting Reed-Sternberg cells."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 microenvironment: IL-4, with the IL-5 and IL-13 already mapped, completes the Th2 cytokine programme that Reed-Sternberg cells secrete to build their permissive, eosinophil-rich tumour microenvironment."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Survival and lost identity: NOTCH1 signalling supports Reed-Sternberg cell survival and contributes to the loss of B-cell identity that characterises the malignant cells of classical Hodgkin lymphoma."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis resistance: anti-apoptotic BCL-2 helps Reed-Sternberg cells survive against the apoptotic pressure of their inflammatory milieu, contributing to treatment resistance in some Hodgkin lymphomas."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative drive: MYC-driven transcription supports the proliferation and metabolic demands of the Hodgkin Reed-Sternberg cell."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Survival signalling: PI3K-AKT-mTOR signalling sustains the survival of Hodgkin Reed-Sternberg cells, complementing their constitutive NF-κB and JAK-STAT activation (both already mapped)."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Apoptosis evasion: MDM2 overexpression degrades p53, contributing to the apoptosis evasion that allows the genomically aberrant Hodgkin Reed-Sternberg cell to survive."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) supports the survival of Reed-Sternberg cells in Hodgkin lymphoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the immunosuppressive microenvironment and T-cell evasion that protect Reed-Sternberg cells in Hodgkin lymphoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) helps establish the immunosuppressive microenvironment that Reed-Sternberg cells exploit in Hodgkin lymphoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of Hodgkin lymphoma, central to its highly effective PD-1 checkpoint immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory, immune-cell-rich microenvironment of Hodgkin lymphoma."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression contributes to the silencing of B-cell identity genes in the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, antagonized by the constitutive PI3K-AKT and JAK-STAT signaling of Reed-Sternberg cells (AKT and JAK1/2 already mapped), are inactivated in Hodgkin lymphoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the abundant reactive inflammatory infiltrate that characterizes Hodgkin lymphoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of CD30 and other receptors (CD30 already mapped) contributes to the survival of the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB and survival signaling of the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling contributes to the survival signaling of the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the recruitment of the reactive immune infiltrate that sustains the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of Hodgkin lymphoma."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-microenvironment and Reed-Sternberg-cell interactions of Hodgkin lymphoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of Hodgkin lymphoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the survival and immune signaling of Hodgkin lymphoma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of Hodgkin lymphoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microenvironment and stromal interactions of Hodgkin lymphoma."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy: involved-site radiation with photons is part of curative therapy for early-stage Hodgkin lymphoma, though its long-term cardiac and second-cancer risks drive efforts to reduce or omit it in favourable cases."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Treatment cardiotoxicity: cured Hodgkin lymphoma survivors face late cardiovascular disease from anthracyclines and mediastinal radiation, and troponin elevation marks the cardiac injury that is a leading cause of their late mortality."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell microenvironment: the Reed-Sternberg cells sit in a T-cell-rich, immunosuppressive infiltrate, and IL-2-driven T-cell responses are unleashed by the checkpoint inhibitors (PD-1 already mapped) to which Hodgkin lymphoma is exquisitely sensitive."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia and B-symptoms: bone-marrow involvement (already mapped) and the systemic inflammatory cytokines of Hodgkin lymphoma lower haemoglobin, the anaemia accompanying the fevers, night sweats and weight loss of the B-symptoms."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Checkpoint effectors: cytotoxic CD8 T cells (perforin and IL-2 already mapped), released from PD-1 restraint, mediate the response to the checkpoint inhibitors to which Hodgkin lymphoma is exquisitely sensitive."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: on initiating chemotherapy for bulky Hodgkin lymphoma, cell breakdown releases purines that xanthine oxidase converts to uric acid, a tumour-lysis risk managed with allopurinol and hydration."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Immunosuppressive eicosanoids: prostaglandin E2 in the Hodgkin microenvironment (IL-10 already mapped) dampens the anti-tumour immune response, part of the immunosuppression the minority Reed-Sternberg cells orchestrate in the reactive infiltrate."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the Hodgkin lymphoma microenvironment, part of its supportive reactive stroma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Th2 eosinophilic milieu: IgE, with the type-2 cytokines IL-4, IL-5 and IL-13 (already mapped), reflects the Th2-skewed, eosinophil-rich microenvironment that the Reed-Sternberg cells cultivate in Hodgkin lymphoma."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and drives the anaemia of chronic disease (haemoglobin already mapped) common in active Hodgkin lymphoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "B-symptom cachexia: the systemic cytokines (TNF and IL-6 already mapped) of Hodgkin lymphoma disturb leptin and the adipokine balance, part of the weight loss and B-symptom cachexia of the disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), links the metabolic and adipose state to the systemic inflammation of Hodgkin lymphoma, part of its metabolic dimension."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Cachexia adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) and the B-symptom cachexia of Hodgkin lymphoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate microenvironment: type-I interferon is part of the innate-immune signalling of the EBV (LMP1 already mapped)-associated and checkpoint-responsive (PD-1 already mapped) microenvironment of Hodgkin lymphoma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and immune dysfunction: zinc is essential for the lymphocyte and immune function, and disturbed zinc status accompanies the immune dysfunction and cachexia of Hodgkin lymphoma."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "B-cell-neoplasm differential: Hodgkin lymphoma and mantle-cell lymphoma are lymphoid neoplasms in the diagnostic differential, distinguished by the Reed-Sternberg (CD30 already mapped) versus the cyclin-D1 mantle-cell biology."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response opposing the Th2/immunosuppressive (IL-4, IL-13 and IL-10 already mapped) microenvironment shaped by the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium immune status: the selenium selenoprotein antioxidant defence supports the lymphocyte (zinc already mapped) immune function disturbed in the immune dysfunction and cachexia of Hodgkin lymphoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the reactive inflammatory infiltrate shaped by the Reed-Sternberg cells of Hodgkin lymphoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1 inflammation: IL-1β, an inflammasome cytokine, is part of the pro-inflammatory cytokine milieu secreted within the reactive microenvironment of Hodgkin lymphoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Alarmin arm: IL-33, an IL-1-family alarmin, contributes to the type-2 (IL-4, IL-5 and IL-13 already mapped) skewing of the Reed-Sternberg microenvironment of Hodgkin lymphoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Anti-CD20/CD30 CDC: the complement C5 and the terminal MAC (with C3 already mapped) mediate the complement-dependent cytotoxicity contributing to the anti-CD20 (rituximab in NLPHL; CD20 already mapped) killing of Hodgkin lymphoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling shapes the myeloid and macrophage (already mapped) response within the reactive microenvironment of Hodgkin lymphoma."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Prognostic vitamin: the low vitamin D status is associated with a worse outcome in Hodgkin lymphoma and modulates the immune microenvironment and the response to therapy."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the Reed-Sternberg cells recruit factor H to regulate the alternative complement pathway (C5, C5aR1 and C3 already mapped) and evade the antibody-mediated complement attack of Hodgkin lymphoma."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the antibodies (already mapped) within the reactive microenvironment of Hodgkin lymphoma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic inflammation of Hodgkin lymphoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Central complement: complement C3 (upstream of C5 and C5aR1 already mapped) is activated by EBV-LMP1 (already mapped) on Reed-Sternberg cells and mediates the complement-dependent cytotoxicity of anti-CD20/CD30 therapies in HL."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Th2 microenvironment: TSLP released by Reed-Sternberg cells drives dendritic-cell and mast-cell (both already mapped) priming that skews HL toward Th2 (IL-4, IL-5, IL-13 already mapped) immune evasion."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Pruritus and type-2 skewing: mast-cell-derived (already mapped) histamine causes the pruritus (a classic B symptom) and amplifies the Th2 (IL-4, IL-5 already mapped) microenvironment of Hodgkin lymphoma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Vasoactive kinin in reactive stroma: bradykinin, from the kallikrein-kinin system activated within the reactive microenvironment of Hodgkin lymphoma, promotes vascular permeability and augments the prostaglandin (already mapped) and histamine (already mapped) B-symptom mediators."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia-of-cancer treatment: erythropoietin corrects the anemia of chronic disease (already mapped) and cancer-chemotherapy-induced (already mapped) anaemia in Hodgkin lymphoma; monitoring of EPO levels aids in distinguishing inflammatory from iron-deficiency anaemia."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Stromal matricellular remodelling: periostin, secreted by the fibroblasts (fibrosis already mapped) of the reactive stromal microenvironment of Hodgkin lymphoma, promotes the collagen (already mapped) deposition and the desmoplastic niche of the Reed-Sternberg cells."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-HL axis: melatonin, via MT1/MT2 receptors on Reed-Sternberg cells and tumour-microenvironment lymphocytes (already mapped), modulates circadian immune rhythms, suppresses NFκB (already mapped) signalling, and enhances the apoptotic sensitivity to ABVD chemotherapy."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-HL axis: testosterone, via androgen receptor signalling on Reed-Sternberg cells and tumour-microenvironment T cells (already mapped), modulates EBV (already mapped)-driven oncogenesis and the male sex bias in Hodgkin-lymphoma incidence and prognosis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonin-HL axis: serotonin, released by activated platelets (already mapped) in the Reed-Sternberg tumour microenvironment, amplifies mast-cell (already mapped) histamine secretion, vascular permeability, and the B-symptom complex of Hodgkin lymphoma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "HL prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Hodgkin lymphoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "HL oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Hodgkin lymphoma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "HL vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates vascular tone in the lymphoma; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Hodgkin lymphoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "HL iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Hodgkin lymphoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "HL sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) cascade of Hodgkin lymphoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "HL magnesium: magnesium, as cofactor of immune enzymes in macrophages (already mapped) and mast cells (already mapped), restrains NF-κB (already mapped) and IL-6 (already mapped); magnesium deficiency amplifies the T-cytotoxic (already mapped) cascade of Hodgkin lymphoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "HL copper: copper supports macrophage (already mapped) and mast-cell (already mapped) anti-inflammatory function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) Reed-Sternberg tumour cascade of Hodgkin lymphoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "HL potassium: potassium regulates macrophage (already mapped) and mast-cell (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of Hodgkin lymphoma."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "HL phosphorus: phosphorus, as ATP in macrophages (already mapped) and mast cells (already mapped), fuels kinase signalling; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of Hodgkin lymphoma."
---

# Hodgkin Lymphoma

## Overview

**Hodgkin lymphoma (HL)** is a B-cell-derived malignancy defined by the presence of neoplastic **Reed-Sternberg (RS) cells** (binucleated giant cells with prominent "owl eye" nucleoli) within an inflammatory tumor microenvironment. HL is one of oncology's major treatment success stories: overall 5-year OS exceeds **85-90%** with modern therapy, including cures in the majority of patients with advanced-stage disease. RS cells represent only ~0.1-1% of the tumor mass and are derived from **germinal center (GC) B cells** that have undergone incomplete apoptosis during negative selection — they carry somatic hypermutated Ig V genes but have catastrophically lost the B-cell transcription program (no surface Ig, absent BOB1/OCT2/PU.1). The landmark identification of **9p24.1 chromosomal amplification** in RS cells — co-amplifying CD30, PDL1, PDL2, and JAK2 — explained the extraordinary sensitivity of HL to PD-1 checkpoint inhibitors and the tumor's immune evasion strategy [^armand-2018-nivo-hl]. **Brentuximab vedotin (anti-CD30 ADC) + AVD** replaced ABVD as the standard for advanced stage cHL after ECHELON-1 demonstrated superior OS [^connors-2018-echelon1].

**Epidemiology:**
- Incidence: ~8,500 cases/year USA; ~83,000 globally
- Bimodal age distribution: peak 1 at 15-34 years (NSHL predominant); peak 2 at >55 years (MCHL and LDHL)
- Male slight predominance; EBV+ forms more common in low-resource settings and older/young children
- Risk factors: infectious mononucleosis (EBV) — 3-fold elevated risk; HIV; immunosuppression; family history

## Structure

### Classification

**Classical Hodgkin lymphoma (cHL, ~95%):**
RS cells: CD15+, CD30+, PAX5 dim, CD20−, OCT2−, BOB1−, CD45−; EBV in 30-50% (depends on subtype and geography)

Histological subtypes:
- **Nodular sclerosis (NSHL, ~60-65%):** Young adults; mediastinal mass common (~75%); broad collagen bands ("lacunar cells" — RS cell variant); EBV+ ~10-25%; most common in high-income countries; favorable prognosis
- **Mixed cellularity (MCHL, ~25%):** Older adults and young children; EBV+ ~50-70%; no fibrosis; rich inflammatory infiltrate; often stage III-IV at presentation
- **Lymphocyte-rich (LRHL, ~5%):** Rare; similar to NLPHL but CD30+; excellent prognosis; difficult to distinguish from NLPHL without IHC
- **Lymphocyte-depleted (LDHL, ~1%):** Elderly; advanced stage; HIV-associated; EBV+ ~80-90%; worst prognosis of cHL subtypes

**Nodular lymphocyte predominant HL (NLPHL, ~5%):**
Neoplastic "lymphocytic and histiocytic" (L&H) cells, also called "popcorn cells":
- CD20+, CD19+, CD79a+, BCL6+, OCT2+, BOB1+ — maintains B-cell program (unlike RS cells)
- CD30−, CD15−, EBV−
- Distinctly different from cHL: GC B cell origin with intact B-cell transcription; NF-κB via BCR signaling
- Treatment: rituximab (anti-CD20) effective alone or with CHOP; excellent prognosis; late relapses possible; may transform to DLBCL
- Sometimes reclassified as T-cell/histiocyte-rich large B-cell lymphoma (THRLBCL) after transformation

### Reed-Sternberg cell molecular biology

**Origin:**
RS cells originate from GC B cells that failed negative selection: they carry clonal rearranged Ig V genes with somatic hypermutations but often have "crippling" mutations in the Ig V gene that abolish BCR expression — these cells would normally die in the GC by apoptosis; RS cells escape via rescue mechanisms involving CD30, NF-κB, and possibly EBV.

**9p24.1 amplification (~97% cHL):**
Chromosome 9p24.1 harbors JAK2, PD-L1 (CD274), PD-L2 (PDCD1LG2), and CD30 (TNFRSF8) within a shared amplicon; amplification (and polysomy) increases: (1) JAK2 expression → constitutive JAK2-STAT6 → IL-13 auto-stimulation + PD-L1 transcription; (2) PD-L1/PD-L2 surface expression → T-cell exhaustion in tumor microenvironment; (3) CD30 overexpression → TRAF/NF-κB survival signals; this convergent amplification explains the >60-70% ORR to PD-1 inhibitors.

**Other molecular features:**
- SOCS1 mutations/deletions (~40%): loss of JAK-STAT negative regulator → enhanced IL-13 signaling
- TNFRSF14 (HVEM) mutations (~15%): impairs CD8+ T-cell activation in microenvironment
- CARD11 mutations (~5%): constitutive NF-κB activation
- A20 (TNFAIP3) deletions (~30%): NF-κB negative regulator loss
- EBV LMP1: functional CD40 mimic → TRAF2/TRAF3/TRAF6 → NF-κB; also induces PD-L1; expressed in ~40-50% cHL RS cells

**Microenvironment composition:**
RS cells recruit and program an inflammatory microenvironment via secreted chemokines and cytokines:
- CCL17/TARC, CCL22: recruit regulatory T cells (Treg) and Th2 cells → immune suppression
- IL-5, eotaxin: recruit eosinophils (prominent in NSHL and MCHL)
- IL-13: auto-stimulatory for RS cells; also drives fibrosis (NSHL collagen bands)
- PGE2: suppresses NK and CD8+ T cells
- CD47 ("don't eat me"): expressed on RS cells → blocks macrophage phagocytosis

## Function

### Staging

**Ann Arbor / Lugano staging (PET-CT based):**
- Stage I: Single lymph node region or single extralymphatic site
- Stage II: ≥2 lymph node regions, same side of diaphragm (± contiguous extranodal site)
- Stage III: Lymph node regions or structures on both sides of diaphragm
- Stage IV: Disseminated extranodal involvement (liver, bone marrow, lungs)

**Modifiers:**
- B symptoms: fever >38°C, drenching night sweats, >10% body weight loss in 6 months (adverse; B-symptom stage is worse prognosis)
- Bulky disease: mediastinal mass >1/3 of thoracic diameter OR any mass >10 cm

**IPS (International Prognostic Score) for advanced stage:**
7 adverse factors (1 point each): albumin <4 g/dL, Hgb <10.5 g/dL, male sex, stage IV, age ≥45, WBC ≥15,000/μL, lymphocyte count <600/μL or <8% of WBC
Score 0-1: 5-year FFS ~77%; Score ≥5: ~42% (though A+AVD has improved outcomes across all IPS groups)

## Pathology

### Treatment approach

**Early-stage favorable cHL (Stage I-II, no bulky disease, no B symptoms):**
- ABVD × 2 cycles + ISRT (involved-site radiotherapy, 20 Gy): ~95% 5-year PFS; standard
- Or ABVD × 4 cycles without RT (for patients refusing RT; slightly inferior PFS but equivalent OS)
- PET-adapted: interim PET-2 (after 2 ABVD) negative → complete ABVD without RT; positive → escalate to BEACOPP

**Early-stage unfavorable cHL (Stage I-II with bulk/B symptoms/other risk factors):**
- ABVD × 4 cycles + ISRT 30 Gy
- Or 2 cycles eBEACOPP + 2 cycles ABVD + RT (HD14 trial)
- A+AVD being studied in early-stage unfavorable (ECHELON-1 enrolled advanced stage only)

**Advanced-stage cHL (Stage III-IV):**
- **A+AVD (brentuximab vedotin + doxorubicin, vinblastine, dacarbazine) × 6 cycles:** Standard of care [^connors-2018-echelon1]; G-CSF primary prophylaxis required (higher neutropenia vs ABVD)
- Or eBEACOPP (escalated bleomycin, etoposide, doxorubicin, cyclophosphamide, vincristine, procarbazine, prednisone): higher toxicity; used in some European centers; higher 2-year PFS than ABVD but OS equivalent; may be preferred in IPS 4-7 patients
- PET-adapted de-escalation: interim PET-2 negative → switch to ABVD for cycles 3-6 (RATHL trial)

**Relapsed/Refractory cHL:**
- **Salvage chemotherapy:** DHAP, ICE, GVD, IGEV → aiming for CR → proceed to auto-SCT
- **Auto-SCT** (autologous stem cell transplant): standard for chemosensitive R/R cHL; 50-55% 5-year OS in auto-SCT-eligible patients
- **Brentuximab vedotin consolidation post-auto-SCT (AETHERA):** 5-year PFS 59% vs 41%; standard post-auto-SCT for high-risk patients
- **Nivolumab (CheckMate 205):** ORR ~69% in auto-SCT-relapsed/refractory cHL; CR ~16%; duration of response ~17 months; FDA 2016 [^armand-2018-nivo-hl]
- **Pembrolizumab (KEYNOTE-087):** ORR ~69% in R/R cHL; FDA 2017
- **KEYNOTE-204** (pembrolizumab vs brentuximab vedotin in R/R cHL): PFS 13.2 vs 8.3 months (HR 0.65) → pembrolizumab superior to brentuximab monotherapy in R/R; brentuximab now used more in combination or post-PD-1
- **Allo-SCT:** Chemorefractory disease; higher NRM than auto-SCT; DLI for molecular relapse
- **Camidanlumab tesirine (ADCT-301):** CD25 ADC (PBD dimer); ORR ~70% in R/R cHL; under investigation

**NLPHL treatment:**
- Stage IA: Involved site RT alone (excellent prognosis); observation considered in some
- Stage II-IV: R-CHOP or R-CVP; rituximab monotherapy for relapse; watch-and-wait for asymptomatic advanced stage
- Late relapses (10-20 years) common; requires long-term surveillance

### Long-term effects and survivorship

Hodgkin lymphoma survivors (~150,000 in USA) face significant late treatment toxicity:
- **Secondary malignancies:** Breast cancer (RT to mediastinum), lung cancer (bleomycin+RT+smoking), secondary AML/MDS (alkylating agents, etoposide — BEACOPP > ABVD risk), NHL
- **Cardiovascular:** Coronary artery disease and cardiomyopathy from mediastinal RT and anthracyclines; major cause of late mortality
- **Pulmonary:** Bleomycin-induced pulmonary fibrosis (~5-10% clinically significant; dose-dependent); pneumonitis from RT
- **Hypothyroidism:** From neck/mediastinal RT (~50% at 20 years)
- **Infertility:** Procarbazine-containing regimens (BEACOPP) → gonadal toxicity; ABVD and A+AVD have lower infertility risk; fertility preservation counseling before therapy

Modern protocols minimize RT fields and doses (ISRT replacing extended-field RT), reduce bleomycin exposure (A+AVD eliminates bleomycin), and use PET-adapted de-escalation to decrease cumulative toxicity.

## Connections

- `connects-to` → **[CD30](../../03-molecular/cd30/README.md)** — CD30 is expressed on ~100% of RS cells (WHO diagnostic criterion for cHL); brentuximab vedotin is the backbone of A+AVD (ECHELON-1) and consolidation post-auto-SCT (AETHERA); 9p24.1 amplification co-amplifies CD30 with PD-L1/PD-L2 in RS cells.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — 9p24.1 amplification in RS cells drives PD-L1/PD-L2 overexpression → profound T-cell exhaustion in tumor microenvironment; nivolumab (CheckMate 205) and pembrolizumab (KEYNOTE-087) show ORR ~65-70% in R/R cHL; KEYNOTE-204 (pembrolizumab vs BV): PFS 13.2 vs 8.3 months.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is constitutively active in RS cells via CD30, CD40, EBV-LMP1, and CARD11 signaling; NF-κB drives RS cell survival by upregulating BCL-2, BCL-XL, and cFLIP; microenvironmental TNF-α further activates NF-κB; NF-κB inhibition is a preclinical therapeutic target in R/R cHL.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — 9p24.1 amplification co-amplifies JAK2 with PD-L1/PD-L2 and CD30 in RS cells; JAK2 → constitutive STAT6 → IL-13 autocrine + PD-L1 transcription; ruxolitinib studied in R/R cHL; JAK2 amplification is a primary oncogenic driver in cHL.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Reed-Sternberg cells arise from germinal-center B cells that acquired crippling Ig V-gene mutations and should have died during negative selection; they survive via CD30/CD40/NF-κB and EBV rescue while shedding the B-cell program (no surface Ig, loss of OCT2/BOB1).
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — EBV is found in 30-50% of classical HL (up to 80-90% in lymphocyte-depleted and HIV-associated cases); its LMP1 protein mimics a constitutively active CD40 receptor → NF-κB survival signaling in RS cells; prior infectious mononucleosis roughly triples HL risk.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 status splits Hodgkin lymphoma: RS cells of classical HL are CD20-negative, whereas the popcorn (L&H) cells of NLPHL retain the B-cell program and are CD20-positive — making rituximab effective in NLPHL but not classical HL.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Hodgkin lymphoma is unusual: malignant Reed-Sternberg cells are <1% of the tumor, the bulk being reactive CD4+ T cells (rosetting around RS cells), eosinophils, and histiocytes that RS cells recruit and depend on — why PD-1 blockade freeing exhausted T cells works so well.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is a key Hodgkin lymphoma site: classical HL spreads contiguously node to adjacent node and to the spleen, and splenic involvement upstages disease and historically guided staging laparotomy; this orderly spread (unlike scattered NHL) reflects HL's lymphatic biology.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Hodgkin lymphoma is the prototypical lymphatic-system cancer: it arises in lymph nodes and spreads in an orderly, contiguous fashion down chains of nodes (Ann Arbor staging), usually as painless cervical or mediastinal adenopathy — distinguishing it from non-Hodgkin lymphomas.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Hodgkin lymphoma and DLBCL are the two ends of large-B-cell lymphoma, bridged by gray-zone lymphoma: classic Hodgkin's CD30+ Reed-Sternberg cells lose most B-cell markers while DLBCL keeps them, and gray-zone tumors share both—the distinction drives very different chemo.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — The Reed-Sternberg cell of classic Hodgkin lymphoma is a crippled B cell: a germinal-center B cell that lost its B-cell receptor and most B-lineage markers yet escaped apoptosis via constitutive NF-κB and EBV, surviving as a rare malignant cell amid a reactive immune infiltrate.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV raises Hodgkin lymphoma risk several-fold and changes its biology: HIV-associated Hodgkin is almost always EBV-driven, presents at advanced stage with B symptoms and marrow involvement, and—unlike AIDS-defining lymphomas—its incidence did not fall with antiretroviral therapy.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is woven into Hodgkin lymphoma's cure: because HL spreads contiguously between nodes, involved-site photon irradiation (lower-dose, after chemo) controls it well—but extended-field radiation's late second cancers and heart disease pushed toward less.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Hodgkin lymphoma is mostly microenvironment: the malignant Reed-Sternberg cells are rare amid an immune infiltrate, and abundant tumor-associated macrophages predict worse outcomes—so the supporting macrophages, not just the cancer cells, shape prognosis.
- `connects-to` → **[CLL](../cll/README.md)** — Hodgkin lymphoma and CLL are both B-cell neoplasms that can intersect through transformation: CLL occasionally undergoes Richter transformation into Hodgkin lymphoma, and both can be EBV-associated—so an indolent leukemia can give rise to an aggressive lymphoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Hodgkin lymphoma evades NK and immune killing despite few tumor cells: the rare Reed-Sternberg cells survive amid abundant immune cells by suppressing NK and T-cell attack and overexpressing PD-L1—why PD-1 blockade is strikingly effective in Hodgkin lymphoma.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone marrow involvement upstages Hodgkin lymphoma: though it usually spreads predictably node-to-node, marrow infiltration signals advanced (stage IV) disease, so staging marrow assessment (now often PET) guides whether limited or extended chemotherapy is used.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Reed-Sternberg cells secrete IL-10 to build an immunosuppressive niche: this and other cytokines recruit and pacify the reactive immune cells that make up most of the tumor, letting the few malignant cells thrive—explaining Hodgkin lymphoma's odd cellular makeup.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Nodular sclerosing Hodgkin lymphoma favors the mediastinum near the thymus: it classically presents as an anterior mediastinal mass in young adults, so it enters the differential of a mediastinal mass alongside thymoma and germ-cell tumors.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Hodgkin lymphoma commonly causes anemia: cytokines from Reed-Sternberg cells drive anemia of chronic disease, and marrow involvement or autoimmune hemolysis can deepen it—so falling red cells are part of the systemic 'B-symptom' illness of advanced HL.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Hodgkin lymphoma thrives by hijacking the immune system: Reed-Sternberg cells amplify PD-L1 to silence surrounding T cells and recruit a protective inflammatory infiltrate, which is exactly why PD-1 checkpoint blockade is strikingly effective in relapsed HL.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Hodgkin lymphoma has a curious alcohol sign: in a minority of patients, drinking alcohol triggers pain in affected lymph nodes within minutes—an unusual, near-specific clue that points to Hodgkin rather than other lymphomas.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Curing Hodgkin lymphoma can later cost the heart: chest radiation and anthracycline chemotherapy raise the risk of coronary disease, valve damage, and heart failure decades on, so cardiac surveillance is central to long-term survivor care.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Curing Hodgkin lymphoma raises later breast cancer risk: chest (mantle) radiation in young women sharply increases breast cancer decades later, so female survivors irradiated young begin breast MRI screening years before the general population.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Hodgkin lymphoma is mostly a crowd of protective cells: the rare malignant Reed-Sternberg cells survive by surrounding themselves with regulatory T cells and other immune cells that shield them, so the tumor is <1% cancer cells and 99% recruited defenders.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Nodular sclerosis Hodgkin lymphoma is defined by fibrosis: broad bands of collagen divide the lymph node into nodules, the histologic signature of the commonest subtype, typically affecting the chest of young adults.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — Reed-Sternberg cells grow on their own IL-13: they secrete this Th2 cytokine as an autocrine growth signal and to recruit the eosinophil-rich infiltrate, shaping the inflammatory backdrop that defines Hodgkin lymphoma.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Hodgkin lymphoma centers on the chest and threatens the lungs: it classically forms a mediastinal mass and can invade lung tissue, while bleomycin in its chemotherapy risks pulmonary fibrosis—so the lungs matter both to the disease and its cure.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta lays down the bands of nodular sclerosis Hodgkin: the commonest subtype is defined by collagen bands that TGF-beta drives fibroblasts to deposit, walling the Reed-Sternberg cells into fibrous nodules.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells fill Hodgkin's reactive infiltrate: the tumor is mostly normal immune cells around scarce Reed-Sternberg cells, and dysfunctional antigen presentation by dendritic cells helps the malignant cells evade the surrounding immunity.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Hodgkin lymphoma drains the body's iron: its systemic inflammation and any marrow involvement suppress red-cell production and lock iron away, so anemia of chronic disease is a common feature.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Hodgkin lymphoma can itch through the skin: severe generalized pruritus, sometimes with the lymph-node pain that alcohol triggers, is a classic paraneoplastic symptom that may precede the diagnosis.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells populate the Hodgkin microenvironment: drawn around the Reed-Sternberg cells, they engage CD30 ligand to support the malignant cells, and their numbers can track with prognosis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Hodgkin can raise blood calcium: its activated macrophages convert vitamin D to its active form, driving the hypercalcemia it shares with granulomatous diseases.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Hodgkin's classic kidney lesion is minimal-change nephrotic syndrome: the lymphoma's cytokines make the glomeruli leak protein, a paraneoplastic effect that resolves when the cancer is treated.
- `connects-to` → **[Interleukin-5](../../03-molecular/il-5/README.md)** — Hodgkin draws eosinophils with IL-5: the Reed-Sternberg cells secrete it to recruit the eosinophils that fill the reactive infiltrate, part of the inflamed microenvironment that hides the rare malignant cells.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy hunts Hodgkin's rare giant cell: the binucleate Reed-Sternberg cell with its two huge 'owl-eye' nucleoli sits sparse amid a sea of reactive immune cells, the diagnostic needle in the haystack.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Advanced Hodgkin lymphoma involves the liver: stage IV disease seeds hepatic deposits, and bulky disease can crowd the organ, a marker of widespread spread beyond the lymph nodes and spleen.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Hodgkin rarely strays into the gut: primary or secondary gastrointestinal involvement of the bowel is uncommon for a disease that spreads node to node, but it occurs in advanced or immunosuppressed cases.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Hodgkin is exquisitely vulnerable to antibody drugs: brentuximab vedotin, an anti-CD30 antibody-drug conjugate, and the checkpoint antibodies nivolumab and pembrolizumab have transformed treatment of relapsed disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Curing Hodgkin frays the nerves: both the vincristine of ABVD and brentuximab vedotin injure peripheral neurons into a dose-limiting neuropathy that often dictates how much treatment a patient can take.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It strikes the young, so fertility matters: the alkylating chemotherapy of escalated regimens and any pelvic radiation can cause infertility, so sperm banking and ovarian preservation are offered before treatment.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Neck radiation lands on the thyroid: the mantle or involved-field irradiation that helps cure Hodgkin commonly leaves survivors hypothyroid years later, and carries a long-term risk of radiation-induced thyroid cancer.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The cure can seed a second blood cancer: the alkylating agents and radiation used against Hodgkin carry a delayed risk of therapy-related myelodysplastic syndrome and acute leukemia, among the most feared late effects of treatment.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Hodgkin can turn the immune system on the platelets: it is a recognized cause of secondary immune thrombocytopenia, and the chemotherapy that treats it suppresses platelet production too, so bleeding and low counts are watched for.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK-STAT3 keeps the Reed-Sternberg cell alive: constitutive STAT3 signaling, downstream of JAK2 and cytokine loops, sustains the malignant cell and shapes the immunosuppressive milieu around it.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Reed-Sternberg cells recruit a reactive crowd: the cytokines they secrete pull in neutrophils, eosinophils, and other inflammatory cells that vastly outnumber the rare tumor cells in the node.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The cure shadows the survivor's heart: anthracycline chemotherapy and mediastinal radiation cause late cardiomyopathy, valve disease, and heart failure, among the leading non-relapse causes of death in long-term Hodgkin survivors.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 carries the B symptoms: Reed-Sternberg cells and their reactive infiltrate pour out IL-6, driving the fevers, night sweats, and weight loss that mark advanced Hodgkin lymphoma and track with worse prognosis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Treatment and asplenia open the door to sepsis: chemotherapy neutropenia and the splenectomy or splenic radiation once used leave Hodgkin patients vulnerable to overwhelming infection from encapsulated bacteria.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A bulky mediastinal mass clots the blood: Hodgkin lymphoma, especially with a large mediastinal tumor compressing veins, carries a high venous thromboembolism risk during diagnosis and treatment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Its cytokines blunt the marrow: the IL-6 and inflammatory output of Hodgkin lymphoma — the same drive behind its B symptoms — suppresses erythropoiesis, producing an anemia of chronic disease that tracks with tumor burden.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Cure casts a long shadow: decades after thoracic (mantle) radiotherapy, Hodgkin survivors face a markedly raised risk of second cancers including lung cancer, a central concern of long-term survivorship care.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Impaired cell-mediated immunity invites an opportunist: Hodgkin lymphoma classically weakens T-cell immunity, and with chemotherapy this leaves patients at risk of Pneumocystis pneumonia, prompting prophylaxis.
- `connects-to` → **[AML](../aml/README.md)** — Its cure can sow a leukemia: the alkylators and etoposide used to treat Hodgkin lymphoma carry a real risk of therapy-related myelodysplasia and acute myeloid leukemia years later, a feared late effect.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — Mantle radiation breeds lung cancer: decades after chest radiotherapy, and amplified by smoking, Hodgkin survivors face a sharply raised risk of lung cancer including the aggressive small cell type.
- `connects-to` → **[Stroke](../stroke/README.md)** — Neck and chest radiation scar the arteries: mediastinal and cervical radiotherapy for Hodgkin lymphoma accelerates carotid and coronary atherosclerosis, raising the long-term risk of stroke in survivors.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its chemo injures the nerves: the vinblastine in ABVD and brentuximab vedotin used for Hodgkin lymphoma cause a dose-limiting peripheral neuropathy with numbness and neuropathic pain.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemotherapy opens the lung to mold: the neutropenia from Hodgkin-lymphoma chemotherapy, and bleomycin lung injury, can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A cancer of the young and its long survivorship weigh on mood: the diagnosis in young adults, intensive therapy and decades of late-effect surveillance contribute to depression in Hodgkin survivors.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its drugs and bulk attack the lungs: bleomycin in ABVD causes pulmonary fibrosis, and a bulky mediastinal Hodgkin mass can compress the airway and superior vena cava.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Mantle radiation silences glands and gonads: neck radiotherapy for Hodgkin lymphoma causes late hypothyroidism, while chemotherapy and pelvic radiation impair fertility and gonadal function.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A young cancer with decades of late-effect risk breeds worry: the diagnosis in youth and the lifelong surveillance for second cancers and cardiac and lung damage foster chronic health anxiety.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its cure scars the heart for decades: mediastinal radiation and the doxorubicin in ABVD cause late premature coronary disease, valve damage and cardiomyopathy in young survivors.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It announces itself through the skin: severe generalised pruritus is a classic constitutional feature of Hodgkin lymphoma, and alcohol-induced pain at involved nodes is a curious sign.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It can leak protein from the kidney: Hodgkin lymphoma is the cancer most classically associated with paraneoplastic minimal-change nephrotic syndrome, which resolves when the lymphoma is treated.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It reaches bone and marrow: advanced Hodgkin lymphoma can infiltrate the bone marrow and skeleton, and treatment-related avascular necrosis follows long steroid use.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can attack the nerves remotely: Hodgkin lymphoma is a classic cause of paraneoplastic cerebellar degeneration and limbic encephalitis, and vinca-alkaloid chemotherapy causes peripheral neuropathy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can involve gut and liver: Hodgkin lymphoma occasionally infiltrates the liver and gastrointestinal tract, and treatment brings nausea and hepatotoxicity.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — ABVD cures most: doxorubicin-bleomycin-vinblastine-dacarbazine chemotherapy, sometimes with radiation, cures the great majority of Hodgkin lymphoma.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Brentuximab targets CD30: the anti-CD30 antibody-drug conjugate brentuximab vedotin, replacing bleomycin in A+AVD, is central to modern Hodgkin lymphoma treatment.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Uniquely sensitive to PD-1 blockade: 9p24.1 amplification floods Reed-Sternberg cells with PD-L1, making Hodgkin lymphoma exquisitely responsive to nivolumab and pembrolizumab.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — The cure can wound the heart: doxorubicin in ABVD and mediastinal radiotherapy injure the myocardium, so cardiomyopathy and heart failure are leading late causes of death in patients cured of Hodgkin lymphoma decades earlier.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Two lymphomas born in the germinal center: Hodgkin lymphoma scatters rare Reed-Sternberg cells through a reactive infiltrate, while follicular lymphoma fills nodes with malignant BCL2-driven germinal-center B cells—shared origin, opposite tumour cellularity.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Engineering T cells against CD30: after brentuximab and checkpoint blockade, anti-CD30 CAR-T cells are in trials for relapsed Hodgkin lymphoma, aiming at the same surface marker the antibody-drug conjugate targets on Reed-Sternberg cells.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Two EBV-linked B-cell lymphomas: Hodgkin and Burkitt both derive from germinal-centre B cells and associate with EBV, contrasting an indolent-curable nodal lymphoma with the fastest-growing human tumour.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Mediastinal disease and lung toxicity: bulky mediastinal Hodgkin and the bleomycin and radiation used to cure it injure the alveoli, causing pneumonitis and pulmonary fibrosis.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — A radiation late effect: neck radiotherapy for Hodgkin lymphoma raises the long-term risk of thyroid cancer and hypothyroidism, a survivorship concern decades after cure.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Radiation's late heart disease: mediastinal radiotherapy for Hodgkin lymphoma accelerates coronary atherosclerosis and valve disease over decades, a leading cause of late mortality in cured survivors.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Paraneoplastic kidney: Hodgkin lymphoma is the classic cause of paraneoplastic minimal-change nephrotic syndrome, the glomerulus leaking massive protein in response to lymphoma-derived cytokines.
- `connects-to` → **[Leishmania donovani](../../../02-pathogen/04-parasites/leishmania-donovani/README.md)** — A great mimic: visceral leishmaniasis causes fever, weight loss and massive splenomegaly that can mimic Hodgkin lymphoma, an infectious differential to consider in endemic areas.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — Raised risk despite ART: unlike most cancers, Hodgkin lymphoma incidence is markedly increased in HIV infection, often EBV-driven, making it a key non-AIDS-defining malignancy.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Reactive microenvironment: Hodgkin lymphoma is dominated by a reactive infiltrate of plasma cells, T cells and eosinophils surrounding the rare malignant Reed-Sternberg cells.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Late radiation cancer: survivors who received subdiaphragmatic radiation for Hodgkin lymphoma face an increased long-term risk of gastric cancer, a delayed treatment complication.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Microenvironment cytokine: Reed-Sternberg cells secrete TNF-α to recruit and sustain the reactive inflammatory infiltrate that surrounds and protects them.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: Reed-Sternberg cells release CCL2 to draw in tumour-associated macrophages, whose abundance is an adverse prognostic marker in Hodgkin lymphoma.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Nodal angiogenesis: VEGF drives the angiogenesis of the involved lymph nodes in Hodgkin lymphoma, supporting tumour growth within the reactive microenvironment.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Glycolytic Reed-Sternberg cells: HIF-1α drives the avid glycolytic metabolism of Hodgkin lymphoma cells, the basis of its intense FDG-PET avidity used for staging and response assessment.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Interferon-driven PD-L1: IFN-γ in the Hodgkin microenvironment, with 9p24 amplification, upregulates PD-L1 on Reed-Sternberg cells, the basis of Hodgkin lymphoma's exquisite sensitivity to PD-1 blockade.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — B-cell survival rescue: BAFF supports the survival of the crippled germinal-centre B cells from which Reed-Sternberg cells derive, helping them escape the apoptosis their defective B-cell receptor should trigger.
- `connects-to` → **[LMP1](../../03-molecular/lmp1/README.md)** — In EBV-positive classical Hodgkin lymphoma, the viral protein LMP1 mimics a constitutively active CD40 receptor to drive the NF-κB signaling on which the Reed-Sternberg cells depend for survival—the viral route to the disease's defining pathway.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The 9p24.1 amplification of Hodgkin lymphoma co-amplifies JAK2 with PD-L1, driving JAK-STAT signaling and the PD-L1 expression behind both JAK-inhibitor interest and the disease's exquisite sensitivity to PD-1 blockade.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The CD8 T cells surrounding Reed-Sternberg cells are exhausted, and PD-1 blockade restores their perforin-mediated killing—the mechanism behind Hodgkin lymphoma's remarkable, often durable response to checkpoint inhibitors.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — ABVD and escalated-BEACOPP chemotherapy kill Reed-Sternberg cells through caspase-3-mediated apoptosis, the cytotoxic backbone that cures the majority of Hodgkin lymphoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Reed-Sternberg cells often downregulate MHC class I and II to escape T-cell recognition, an antigen-presentation defect that, with their PD-L1 amplification, shapes the immunosuppressed niche they build around themselves.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — The commonest Hodgkin subtype, nodular sclerosis, is defined by broad collagen bands that divide the node into nodules, a fibrotic stromal reaction orchestrated by the cytokine-secreting Reed-Sternberg cells.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4, with the IL-5 and IL-13 already mapped, completes the Th2 cytokine program that Reed-Sternberg cells secrete to build their permissive, eosinophil-rich tumor microenvironment.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH1 signaling supports Reed-Sternberg cell survival and contributes to the loss of B-cell identity that characterizes the malignant cells of classical Hodgkin lymphoma.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 helps Reed-Sternberg cells survive against the apoptotic pressure of their inflammatory milieu, contributing to treatment resistance in some Hodgkin lymphomas.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC-driven transcription supports the proliferation and metabolic demands of the Hodgkin Reed-Sternberg cell.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K-AKT-mTOR signaling sustains the survival of Hodgkin Reed-Sternberg cells, complementing their constitutive NF-κB and JAK-STAT activation (both already mapped).
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 overexpression degrades p53, contributing to the apoptosis evasion that allows the genomically aberrant Hodgkin Reed-Sternberg cell to survive.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) supports the survival of Reed-Sternberg cells in Hodgkin lymphoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the immunosuppressive microenvironment and T-cell evasion that protect Reed-Sternberg cells in Hodgkin lymphoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) helps establish the immunosuppressive microenvironment that Reed-Sternberg cells exploit in Hodgkin lymphoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of Hodgkin lymphoma, central to its highly effective PD-1 checkpoint immunotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory, immune-cell-rich microenvironment of Hodgkin lymphoma.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression contributes to the silencing of B-cell identity genes in the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, antagonized by the constitutive PI3K-AKT and JAK-STAT signaling of Reed-Sternberg cells (AKT and JAK1/2 already mapped), are inactivated in Hodgkin lymphoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the abundant reactive inflammatory infiltrate that characterizes Hodgkin lymphoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of CD30 and other receptors (CD30 already mapped) contributes to the survival of the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB and survival signaling of the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling contributes to the survival signaling of the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the recruitment of the reactive immune infiltrate that sustains the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of Hodgkin lymphoma.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-microenvironment and Reed-Sternberg-cell interactions of Hodgkin lymphoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of Hodgkin lymphoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the survival and immune signaling of Hodgkin lymphoma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of Hodgkin lymphoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microenvironment and stromal interactions of Hodgkin lymphoma.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy: involved-site radiation with photons is part of curative therapy for early-stage Hodgkin lymphoma, though its long-term cardiac and second-cancer risks drive efforts to reduce or omit it in favourable cases.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Treatment cardiotoxicity: cured Hodgkin lymphoma survivors face late cardiovascular disease from anthracyclines and mediastinal radiation, and troponin elevation marks the cardiac injury that is a leading cause of their late mortality.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell microenvironment: the Reed-Sternberg cells sit in a T-cell-rich, immunosuppressive infiltrate, and IL-2-driven T-cell responses are unleashed by the checkpoint inhibitors (PD-1 already mapped) to which Hodgkin lymphoma is exquisitely sensitive.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia and B-symptoms: bone-marrow involvement (already mapped) and the systemic inflammatory cytokines of Hodgkin lymphoma lower haemoglobin, the anaemia accompanying the fevers, night sweats and weight loss of the B-symptoms.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Checkpoint effectors: cytotoxic CD8 T cells (perforin and IL-2 already mapped), released from PD-1 restraint, mediate the response to the checkpoint inhibitors to which Hodgkin lymphoma is exquisitely sensitive.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: on initiating chemotherapy for bulky Hodgkin lymphoma, cell breakdown releases purines that xanthine oxidase converts to uric acid, a tumour-lysis risk managed with allopurinol and hydration.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Immunosuppressive eicosanoids: prostaglandin E2 in the Hodgkin microenvironment (IL-10 already mapped) dampens the anti-tumour immune response, part of the immunosuppression the minority Reed-Sternberg cells orchestrate in the reactive infiltrate.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of the Hodgkin lymphoma microenvironment, part of its supportive reactive stroma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Th2 eosinophilic milieu: IgE, with the type-2 cytokines IL-4, IL-5 and IL-13 (already mapped), reflects the Th2-skewed, eosinophil-rich microenvironment that the Reed-Sternberg cells cultivate in Hodgkin lymphoma.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and drives the anaemia of chronic disease (haemoglobin already mapped) common in active Hodgkin lymphoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — B-symptom cachexia: the systemic cytokines (TNF and IL-6 already mapped) of Hodgkin lymphoma disturb leptin and the adipokine balance, part of the weight loss and B-symptom cachexia of the disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), links the metabolic and adipose state to the systemic inflammation of Hodgkin lymphoma, part of its metabolic dimension.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Cachexia adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) and the B-symptom cachexia of Hodgkin lymphoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate microenvironment: type-I interferon is part of the innate-immune signalling of the EBV (LMP1 already mapped)-associated and checkpoint-responsive (PD-1 already mapped) microenvironment of Hodgkin lymphoma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and immune dysfunction: zinc is essential for the lymphocyte and immune function, and disturbed zinc status accompanies the immune dysfunction and cachexia of Hodgkin lymphoma.
- `connects-to` → **[Mantle cell lymphoma](../mantle-cell-lymphoma/README.md)** — B-cell-neoplasm differential: Hodgkin lymphoma and mantle-cell lymphoma are lymphoid neoplasms in the diagnostic differential, distinguished by the Reed-Sternberg (CD30 already mapped) versus the cyclin-D1 mantle-cell biology.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response opposing the Th2/immunosuppressive (IL-4, IL-13 and IL-10 already mapped) microenvironment shaped by the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium immune status: the selenium selenoprotein antioxidant defence supports the lymphocyte (zinc already mapped) immune function disturbed in the immune dysfunction and cachexia of Hodgkin lymphoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the reactive inflammatory infiltrate shaped by the Reed-Sternberg cells of Hodgkin lymphoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1 inflammation: IL-1β, an inflammasome cytokine, is part of the pro-inflammatory cytokine milieu secreted within the reactive microenvironment of Hodgkin lymphoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — Alarmin arm: IL-33, an IL-1-family alarmin, contributes to the type-2 (IL-4, IL-5 and IL-13 already mapped) skewing of the Reed-Sternberg microenvironment of Hodgkin lymphoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Anti-CD20/CD30 CDC: the complement C5 and the terminal MAC (with C3 already mapped) mediate the complement-dependent cytotoxicity contributing to the anti-CD20 (rituximab in NLPHL; CD20 already mapped) killing of Hodgkin lymphoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling shapes the myeloid and macrophage (already mapped) response within the reactive microenvironment of Hodgkin lymphoma.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Prognostic vitamin: the low vitamin D status is associated with a worse outcome in Hodgkin lymphoma and modulates the immune microenvironment and the response to therapy.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the Reed-Sternberg cells recruit factor H to regulate the alternative complement pathway (C5, C5aR1 and C3 already mapped) and evade the antibody-mediated complement attack of Hodgkin lymphoma.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the antibodies (already mapped) within the reactive microenvironment of Hodgkin lymphoma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Anaemia iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic inflammation of Hodgkin lymphoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Central complement: complement C3 (upstream of C5 and C5aR1 already mapped) is activated by EBV-LMP1 (already mapped) on Reed-Sternberg cells and mediates the complement-dependent cytotoxicity of anti-CD20/CD30 therapies in HL.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Th2 microenvironment: TSLP released by Reed-Sternberg cells drives dendritic-cell and mast-cell (both already mapped) priming that skews HL toward Th2 (IL-4, IL-5, IL-13 already mapped) immune evasion.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Pruritus and type-2 skewing: mast-cell-derived (already mapped) histamine causes the pruritus (a classic B symptom) and amplifies the Th2 (IL-4, IL-5 already mapped) microenvironment of Hodgkin lymphoma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Vasoactive kinin in reactive stroma: bradykinin, from the kallikrein-kinin system activated within the reactive microenvironment of Hodgkin lymphoma, promotes vascular permeability and augments the prostaglandin (already mapped) and histamine (already mapped) B-symptom mediators.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia-of-cancer treatment: erythropoietin corrects the anemia of chronic disease (already mapped) and cancer-chemotherapy-induced (already mapped) anaemia in Hodgkin lymphoma; monitoring of EPO levels aids in distinguishing inflammatory from iron-deficiency anaemia.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Stromal matricellular remodelling: periostin, secreted by the fibroblasts (fibrosis already mapped) of the reactive stromal microenvironment of Hodgkin lymphoma, promotes the collagen (already mapped) deposition and the desmoplastic niche of the Reed-Sternberg cells.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-HL axis: melatonin, via MT1/MT2 receptors on Reed-Sternberg cells and tumour-microenvironment lymphocytes (already mapped), modulates circadian immune rhythms, suppresses NFκB (already mapped) signalling, and enhances the apoptotic sensitivity to ABVD chemotherapy.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-HL axis: testosterone, via androgen receptor signalling on Reed-Sternberg cells and tumour-microenvironment T cells (already mapped), modulates EBV (already mapped)-driven oncogenesis and the male sex bias in Hodgkin-lymphoma incidence and prognosis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonin-HL axis: serotonin, released by activated platelets (already mapped) in the Reed-Sternberg tumour microenvironment, amplifies mast-cell (already mapped) histamine secretion, vascular permeability, and the B-symptom complex of Hodgkin lymphoma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — HL prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Hodgkin lymphoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — HL oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of Hodgkin lymphoma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — HL vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates vascular tone in the lymphoma; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Hodgkin lymphoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — HL iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of Hodgkin lymphoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — HL sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) cascade of Hodgkin lymphoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — HL magnesium: magnesium, as cofactor of immune enzymes in macrophages (already mapped) and mast cells (already mapped), restrains NF-κB (already mapped) and IL-6 (already mapped); magnesium deficiency amplifies the T-cytotoxic (already mapped) cascade of Hodgkin lymphoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — HL copper: copper supports macrophage (already mapped) and mast-cell (already mapped) anti-inflammatory function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) Reed-Sternberg tumour cascade of Hodgkin lymphoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — HL potassium: potassium regulates macrophage (already mapped) and mast-cell (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of Hodgkin lymphoma.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — HL phosphorus: phosphorus, as ATP in macrophages (already mapped) and mast cells (already mapped), fuels kinase signalling; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of Hodgkin lymphoma.

[^connors-2018-echelon1]: Connors JM, Jurczak W, Straus DJ, et al. Brentuximab vedotin with chemotherapy for stage III or IV Hodgkin's lymphoma. *N Engl J Med.* 2018;378(4):331-344. [doi:10.1056/NEJMoa1708984](https://doi.org/10.1056/NEJMoa1708984) · [PubMed 29360494](https://pubmed.ncbi.nlm.nih.gov/29360494/)
[^armand-2018-nivo-hl]: Armand P, Engert A, Younes A, et al. Nivolumab for relapsed/refractory classic Hodgkin lymphoma after failure of autologous hematopoietic cell transplantation: extended follow-up of the multicohort single-arm phase II CheckMate 205 trial. *J Clin Oncol.* 2018;36(14):1428-1439. [doi:10.1200/JCO.2017.77.6717](https://doi.org/10.1200/JCO.2017.77.6717) · [PubMed 29584546](https://pubmed.ncbi.nlm.nih.gov/29584546/)
