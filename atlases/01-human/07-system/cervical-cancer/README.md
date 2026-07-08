---
schema: human-scale-entry/v1
id: cervical-cancer
name: Cervical Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Cervical cancer is HPV-driven in >99% of cases; HPV E6/E7 oncoproteins degrade p53 and inactivate RB → immortalization. Cisplatin + chemoradiation is standard for locally advanced; pembrolizumab + chemotherapy (KEYNOTE-826) is approved for PD-L1+ recurrent/metastatic disease."
aliases: ["cervical cancer", "cervical carcinoma", "HPV cervical cancer", "squamous cell carcinoma cervix", "cervical adenocarcinoma", "FIGO cervical cancer", "invasive cervical cancer"]
sources:
  - id: tewari-2014-gog240
    type: peer-reviewed
    cite: "Tewari KS, Sill MW, Long HJ 3rd, et al. Improved survival with bevacizumab in advanced cervical cancer. N Engl J Med. 2014;370(8):734-743."
    doi: "10.1056/NEJMoa1309748"
    pmid: "24552320"
    url: "https://doi.org/10.1056/NEJMoa1309748"
  - id: colombo-2021-keynote826
    type: peer-reviewed
    cite: "Colombo N, Dubot C, Lorusso D, et al. Pembrolizumab for persistent, recurrent, or metastatic cervical cancer. N Engl J Med. 2021;385(20):1856-1867."
    doi: "10.1056/NEJMoa2112435"
    pmid: "34534430"
    url: "https://doi.org/10.1056/NEJMoa2112435"
cross_links:
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Pembrolizumab + cisplatin/paclitaxel ± bevacizumab (KEYNOTE-826) improved OS vs chemotherapy in PD-L1 CPS≥1 persistent/recurrent/metastatic cervical cancer (24.4 vs 16.5 months); FDA approved 2021; cemiplimab showed similar OS benefit in EMPOWER-Cervical 1."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "HPV E7 oncoprotein binds RB LXCXE motif → RB inactivation → E2F release → S-phase entry; p16 INK4a (CDKN2A) overexpression is IHC surrogate for RB inactivation in cervical cancer; functional RB loss without mutation is universal in HPV-driven cervical carcinogenesis."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "HPV E6 recruits E6AP (UBE3A) ubiquitin ligase → p53 proteasomal degradation → loss of G1 checkpoint and apoptosis; p53 is wild-type but functionally absent in HPV+ cervical cancer; p53 mutation is rare and not required for HPV-driven carcinogenesis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Bevacizumab + cisplatin/paclitaxel (GOG-0240) improved OS vs chemotherapy alone (17.0 vs 13.3 months) in recurrent/metastatic cervical cancer; bevacizumab is standard for metastatic disease; KEYNOTE-826 added pembrolizumab to bevacizumab + chemotherapy for PD-L1+ patients."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: connects-to
    note: "HPV16/18 infect cervical transformation zone → E6-mediated p53 degradation + E7-mediated RB inactivation → CIN1-3 → invasive carcinoma; HPV16 accounts for ~55% of cervical SCC; viral genome integration disrupts E2 repressor → constitutive E6/E7 overexpression."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutations (E542K, E545K, H1047R) occur in ~35-40% of cervical SCC and adenocarcinoma → AKT-mTOR activation → proliferation; PIK3CA mutation cooperates with HPV E6/E7 in transformation; PI3K inhibitors (alpelisib) being studied in PIK3CA-mutant recurrent cervical cancer."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS mutations occur in ~10-15% of endocervical adenocarcinoma; gastric-type adenocarcinoma is HPV-independent with frequent KRAS + STK11 mutations; KRAS mutation predicts poor response to platinum chemotherapy; no approved KRAS inhibitors for cervical adenocarcinoma."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "Cervical cancer and HPV-positive head-and-neck cancer are the same disease in different epithelia: both arise when high-risk HPV over-expresses E6 and E7 to destroy p53 and inactivate RB, and both carry a better prognosis than HPV-negative cancers."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Immunosuppression sharply raises cervical-cancer risk: HIV-positive women clear HPV poorly and progress from dysplasia to invasive cancer faster, so invasive cervical cancer is an AIDS-defining illness and these patients need intensified HPV screening and earlier colposcopy."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8+ cytotoxic T cells are both the natural defense that usually clears HPV and the target of cervical-cancer immunotherapy: persistent infection reflects failed CD8 surveillance, and checkpoint blockade (pembrolizumab, KEYNOTE-826) unleashes them against the tumor."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Cervical and bladder cancers share the pelvic neighborhood: locally advanced cervical cancer can invade the bladder (vesicovaginal fistula, hematuria), pelvic radiotherapy for one raises risk of the other, and both are smoking-associated cancers managed by pelvic oncology."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Cervical and endometrial cancers are the main uterine-region malignancies but differ: cervical is HPV-driven squamous cancer of the cervix (vaccine-preventable, screen-detected), while endometrial is estrogen/Lynch-driven adenocarcinoma of the uterine body with abnormal bleeding."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Cervical and ovarian cancers are both gynecologic malignancies but contrast in prevention: cervical cancer has effective screening and an HPV vaccine and presents early, whereas ovarian cancer (often BRCA-driven) has no good screening and usually presents late."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Peutz-Jeghers syndrome causes a rare HPV-independent cervical cancer, adenoma malignum: germline STK11 loss drives this deceptively bland mucinous tumor—the one cervical cancer not prevented by HPV vaccination, warranting surveillance in PJS."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is curative for locally advanced cervical cancer: concurrent chemoradiation with external-beam photons plus intracavitary brachytherapy delivers a high radiation dose directly to the cervix—and brachytherapy is uniquely critical to cure in this cancer."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "The HPV vaccine that prevents cervical cancer works through dendritic cells: virus-like particles are taken up by dendritic cells that prime B and T cells to make neutralizing antibodies against HPV capsids, blocking the infection behind nearly all cervical cancer."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Cervical cancer is fundamentally an immune-control failure: most HPV infections clear, but when immune surveillance falters—markedly in HIV—persistent high-risk HPV transforms cervical cells, so immune status governs whether infection becomes cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help clear HPV-infected cervical cells: innate NK responses and interferon limit early infection, and HPV evades them by downregulating immune signals—so weakened NK/innate immunity allows the persistent infection that precedes cervical cancer."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "HPV reactivates telomerase to immortalize cervical cells: the viral E6 oncoprotein, beyond degrading p53, switches on TERT, so infected cells avoid the telomere shortening that normally limits division—a key step from infection to invasive cancer."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cervical cancer is the most preventable cancer of the reproductive system: HPV infects the cervical transformation zone, but Pap/HPV screening catches precancer and vaccination blocks the virus—so a leading female-reproductive cancer is now largely avoidable."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Cervical cancer spreads predictably through the lymphatic system: tumor cells drain to pelvic and para-aortic nodes, so lymph-node status is the dominant prognostic factor and dictates whether surgery or chemoradiation is used and how widely it is targeted."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-ion radiotherapy is an option for some cervical cancers: heavy carbon ions deposit a sharply localized, highly damaging dose, useful for bulky or radioresistant gynecologic tumors—an alternative to conventional photon radiation in specialized centers."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Cervical cancer is now vaccine-preventable through B cells: the HPV vaccine elicits B-cell antibodies against the L1 capsid that block infection before it can transform cervical cells, so a humoral immune response is dramatically cutting cervical cancer rates."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Advanced cervical cancer kills through the kidneys: tumor spreading sideways in the pelvis encases the ureters, causing obstruction and hydronephrosis, so post-renal kidney failure—not the primary tumor—is a classic cause of death."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Cervical cancer intersects with pregnancy at the cervix: screening often first detects disease in young, pregnant women, and cancer found in pregnancy forces hard timing decisions around delivery—so obstetric care and cancer care must be coordinated."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cervical cancer is flagged by p16, the CDKN2A protein: HPV's E7 disables Rb, which paradoxically drives p16 sky-high, so strong p16 staining is the pathologist's surrogate marker that a lesion is HPV-driven and truly precancerous."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Cervical squamous tumors lean on EGFR: the receptor is frequently overexpressed and drives growth, making the ErbB pathway a studied target in advanced cervical cancer alongside anti-angiogenic and checkpoint therapy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "HPV and cervical tumors hide behind regulatory T cells: Tregs infiltrate the lesion and suppress the cytotoxic response that should clear infected cells, part of the immune evasion that lets persistent HPV progress to cancer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Cervical tumors are notoriously oxygen-starved, and that resists radiation: hypoxic regions survive radiotherapy because oxygen is needed to fix radiation-induced DNA damage, so tumor hypoxia predicts worse outcomes and drives research into overcoming it."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "HPV silences the interferon alarm in cervical cancer: the viral E6 and E7 proteins suppress type I interferon signaling, blunting the antiviral response so infected cells evade clearance—an immune escape that lets persistent infection progress."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Advanced cervical cancer spreads to the lungs: tumor cells travel through blood and lymph to seed pulmonary metastases, a common site of distant disease that shapes staging and the shift from curative to systemic treatment."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Cervical cancer bleeds away iron: irregular and postcoital vaginal bleeding is an early sign, and the steady blood loss drains iron into a deficiency anemia that often brings women in for the diagnosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Advanced cervical cancer invades the rectum: spreading through the pelvis, it can breach the large intestine and bladder, forming fistulas that leak stool or urine—devastating complications of locally advanced disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Curing cervical cancer can leave fibrosis behind: the pelvic radiotherapy central to treatment scars surrounding tissues, stiffening the vagina, bladder, and bowel and causing lasting side effects in survivors."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Cervical cancer is fed by new vessels: VEGF drives endothelial cells to vascularize the tumor, and bevacizumab that blocks them improves survival in advanced disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Cervical cancer ultimately spreads to the liver: hematogenous metastasis to liver, lung and bone marks advanced disease beyond its local pelvic invasion."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Pelvic chemoradiation for cervical cancer hits the bone marrow: much of the body's active marrow sits in the pelvis, so treatment causes cytopenias that limit how much chemotherapy can be given."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals HPV's fingerprint on the cervix: infected cells become koilocytes with a clear perinuclear halo and shrunken raisin-like nucleus, and viral particles assemble in the upper layers — the cytologic clue a Pap smear hunts for."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Cervical cancer rarely reaches the brain, but when it does it marks the end stage: late hematogenous spread seeds cerebral metastases, an uncommon site beyond its usual march to lung, liver, and bone."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D may help the body clear HPV: deficiency is associated with persistent infection and cervical dysplasia, fitting the vitamin's role in the immune defense that decides whether an HPV infection resolves or progresses."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The vaccine works by raising antibody: HPV vaccines teach the immune system to make neutralizing antibodies against the virus's capsid, blocking the infection that causes nearly all cervical cancer — a vaccine that prevents a cancer."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Cervical cancer announces itself in blood and worsens with anemia: abnormal vaginal bleeding is the cardinal symptom, and the resulting low red-cell count both weakens the patient and blunts the tumor's response to radiotherapy."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Advanced disease reaches the nerves: pelvic sidewall spread compresses the lumbosacral plexus into leg pain and weakness, while the cisplatin given with radiation injures peripheral sensory neurons."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Clearing HPV is a CD4 job: a strong Th1 helper-T response normally eliminates the virus, so when helper-T immunity falters — in HIV or other immunosuppression — the infection persists and progresses toward cancer, why screening is intensified in these patients."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen is a cofactor in cervical carcinogenesis: in HPV-infected tissue estrogen signaling cooperates with the E6/E7 oncoproteins to drive progression, consistent with the modest extra risk seen with very long-term combined oral contraceptive use."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "HPV's oncoproteins are built around zinc: both E6 and E7 fold into zinc-binding domains that they need to grip and degrade p53 and Rb, so the metal ion is structurally essential to the very proteins that transform the cell."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Advanced cervical cancer kills through the kidneys: local spread encases the ureters and blocks urine flow, so obstructive uropathy and the resulting renal failure are a classic and common cause of death from the disease."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 fuels the HPV-driven tumor: the cytokine activates STAT3 to drive cervical cancer growth, angiogenesis, and resistance to chemoradiation, and high levels mark a worse prognosis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor macrophages help HPV hide: M2-polarized tumor-associated macrophages in the cervical lesion suppress the antiviral T-cell response and promote invasion, abetting the immune evasion that lets the cancer grow."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic inflammation keeps NF-κB switched on: HPV infection and the inflamed cervical microenvironment activate NF-κB, driving pro-survival and pro-invasive gene programs that help the transformed cells persist and progress."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Stromal fibroblasts abet invasion: cancer-associated fibroblasts in the cervical tumor remodel the matrix and secrete factors that promote angiogenesis and help the carcinoma breach the basement membrane."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Pelvic cancer raises the clot risk: advanced cervical cancer and its treatment promote venous thromboembolism, both through the tumor's pro-coagulant state and pelvic vein compression by bulky disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "HPV oncoproteins switch on STAT3: E6/E7 and the inflamed cervical microenvironment activate STAT3, driving proliferation and immune evasion in the progression from HPV infection to invasive cancer."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Bulky pelvic disease opens routes to infection: tumor obstruction of the ureters causes pyelonephritis and urosepsis, while necrotic tumor and fistulae into bladder or bowel can seed pelvic infection and sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic bleeding and inflammation drain the blood: ongoing vaginal blood loss plus the cancer's inflammatory cytokines produce anemia that not only weakens patients but blunts the tumor's response to radiotherapy."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "Immune loss lets HPV run to cancer: HIV impairs clearance of human papillomavirus, so cervical cancer occurs more often, at younger ages and more aggressively — making it an AIDS-defining malignancy."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Steady vaginal bleeding depletes iron: the abnormal and postcoital bleeding of cervical cancer causes chronic blood loss, draining iron stores into an iron-deficiency anemia that often prompts the diagnosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Diagnosis and its sexual toll weigh on mood: a cancer affecting fertility, sexual function and often younger women carries a substantial psychological burden, with high rates of depression."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pelvic spread and treatment injure nerves: tumor invading the pelvic sidewall and the cisplatin and radiation used to treat cervical cancer cause lumbosacral plexopathy and chemotherapy neuropathy with chronic pain."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Pelvic radiation and lost ovaries weaken bone: radiotherapy causes insufficiency fractures and bone loss, and treatment-induced menopause in younger patients withdraws estrogen, accelerating osteoporosis."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its chemoradiation opens the lung to mold: the neutropenia from cisplatin-based chemoradiation for cervical cancer can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Locally advanced tumour strangles the ureters: cervical cancer spreading into the pelvis obstructs the ureters, causing hydronephrosis and renal failure — a classic and common cause of death from the disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Pelvic radiation and spread injure the bowel: chemoradiation for cervical cancer causes radiation proctitis and enteritis, and advanced tumour can erode into the rectum to form a rectovaginal fistula."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A young woman's cancer with fertility loss breeds worry: the diagnosis, loss of fertility and recurrence surveillance of cervical cancer foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to the lungs: the lungs are the commonest site of distant metastasis in cervical cancer, appearing as nodules on staging and recurrence imaging."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It seeds the bones: cervical cancer metastasises to the spine and pelvis, causing bone pain and pathological fractures in advanced disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Pelvic recurrence invades the nerves: tumour growth into the lumbosacral plexus causes a painful plexopathy with leg weakness and numbness, a distressing late complication."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Treatment strains the circulation: cisplatin chemoradiation carries cardiovascular and thromboembolic risk, and pelvic radiation can damage the iliac vessels over time."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Virus and therapy both touch the skin: the same HPV family causes genital and skin warts, while pelvic radiotherapy produces radiation dermatitis and rare cutaneous metastases mark advanced disease."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "A suspected co-factor: herpes simplex virus type 2 was long studied as a possible co-factor cooperating with HPV in cervical carcinogenesis, and genital herpes shares its transmission route."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy extends survival: pembrolizumab added to chemotherapy, and cemiplimab after it, improve survival in advanced PD-L1-positive cervical cancer, which is virally driven and immunogenic."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cisplatin chemoradiation is the backbone: concurrent cisplatin-based chemoradiotherapy is the curative-intent standard for locally advanced cervical cancer."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "Immunodeficiency accelerates it: HIV greatly raises cervical cancer risk by impairing clearance of oncogenic HPV, making it an AIDS-defining cancer and a screening priority in HIV-positive women."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Anti-angiogenics and ADCs extend it: bevacizumab against VEGF improves survival in advanced cervical cancer, and tissue-factor-targeting tisotumab vedotin is an antibody-drug conjugate for recurrent disease beyond chemoradiation."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Advanced disease seeds bone: metastatic cervical cancer spreads to the spine and pelvis as painful osteolytic lesions, a late manifestation after pelvic and nodal spread."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "It kills through the kidneys: locally advanced cervical cancer encases the ureters, and bilateral obstruction backs pressure up to the glomeruli, dropping filtration to cause the uraemia that is a classic cause of death."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Where it spreads: advanced cervical cancer metastasises through the blood to the lungs, seeding tumour deposits in the alveolar capillary bed."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Immune evasion and immunotherapy: HPV-driven cervical cancer draws tertiary lymphoid structures and responds to PD-1 checkpoint blockade, the immune dimension of an infection-driven cancer."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "An emerging target: HER2 amplification occurs in a subset of cervical and other gynaecological cancers, making HER2-directed antibody-drug conjugates a developing treatment option."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Immunosuppression and HPV cancer: transplant recipients and those on GVHD-related immunosuppression have markedly higher rates of HPV-driven cervical and other anogenital cancers."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Radiation's late cancer risk: pelvic radiotherapy for cervical cancer slightly raises the risk of second cancers in the radiation field, including rectal and colorectal cancer years later."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Screening disrupted: COVID-19 sharply cut cervical screening and HPV vaccination uptake, projected to raise cervical cancer incidence and stage at diagnosis in coming years."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC amplification: gain of the 3q26 region amplifying MYC is a common driver of cervical cancer progression, cooperating with HPV E6/E7 to fuel proliferation."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Context-dependent Notch: NOTCH1 is recurrently mutated in cervical cancer, where Notch signalling can act as either tumour suppressor or oncogene depending on stage and context."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Local rectal invasion: advanced cervical cancer can invade the rectum and create rectovaginal fistulas, breaching the intestinal epithelium—a debilitating feature of locally advanced disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT signalling: PIK3CA mutation is among the commonest events in cervical cancer, activating AKT to drive growth and survival and offering a targeted therapeutic node."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxia and radioresistance: HIF-1α stabilised in hypoxic cervical tumours drives angiogenesis and resistance to radiotherapy, a key adverse prognostic factor."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic driver: HPV E7 upregulates EZH2, whose PRC2 silencing of tumour-suppressor genes promotes the progression of HPV-driven cervical cancer."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K-mTOR axis: frequent PIK3CA mutations and PI3K-AKT-mTOR activation drive cervical cancer growth, an actionable pathway downstream of the loss of tumour-suppressor control by HPV oncoproteins."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immune evasion and EMT: TGF-beta in the cervical tumour microenvironment suppresses anti-tumour immunity and promotes epithelial-mesenchymal transition and invasion in advancing disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws tumour-associated macrophages into cervical cancer, building an immunosuppressive microenvironment that abets HPV-driven tumour progression."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "HPV innate evasion: HPV oncoproteins antagonise the cGAS-STING DNA-sensing pathway to evade innate immunity, while viral genome integration generates the cytosolic DNA and instability this pathway would otherwise detect."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic clearance: CD8 T cells use perforin to eliminate HPV-infected cells, the response that prophylactic and therapeutic HPV vaccines harness and whose evasion permits progression to cervical cancer."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic homing: the CXCL12-CXCR4 axis drives the parametrial invasion and lymph-node metastasis of cervical cancer, the spread that governs staging and the need for chemoradiation."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "E7-Rb-E2F release: the HPV E7 oncoprotein inactivates Rb, freeing E2F transcription factors to drive the cell cycle — the second arm of viral transformation alongside E6's degradation of p53, the pair that immortalises the infected cervical cell."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemoradiation apoptosis: concurrent cisplatin chemoradiation, the standard for locally advanced cervical cancer, kills tumour cells through caspase-3-mediated apoptosis, the death pathway whose evasion underlies radioresistance."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Vaccine prevention: HPV vaccines induce neutralising IgG against the L1 capsid that blocks infection, the primary-prevention strategy that is now driving cervical cancer toward elimination where vaccination is widespread."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K amplification: PTEN loss intensifies PI3K-AKT-mTOR signalling (PIK3CA, AKT and mTOR already mapped), a frequent somatic event cooperating with HPV E6/E7 in cervical carcinoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK proliferation: EGFR and RAS signalling (EGFR and KRAS already mapped) drive the MAPK-ERK cascade in cervical cancer, sustaining proliferation and serving as a candidate therapeutic axis."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "EMT and invasion: loss of E-cadherin during epithelial-mesenchymal transition releases cervical-carcinoma cells from their junctions, enabling stromal invasion and the lymph-node spread that worsens prognosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Interferon evasion: HPV oncoproteins suppress the type-I-interferon response (already mapped), and JAK-STAT signalling (STAT3 mapped) governs the immune evasion and inflammatory signalling of cervical cancer."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Treatment resistance: NRF2 antioxidant activation contributes to the chemo- and radio-resistance of cervical cancer, protecting tumour cells from treatment-induced oxidative stress."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Progression to invasion: Wnt/β-catenin signalling cooperates with HPV oncoproteins in the progression from cervical intraepithelial neoplasia to invasive carcinoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) shifts from tumour suppression to promotion of invasion and EMT in cervical carcinogenesis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates apoptosis resistance and the immune microenvironment of cervical cancer."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cyclin-D-CDK4/6 activity (CDKN2A/p16, RB1 and E2F1 mapped) drives the cell-cycle dysregulation that HPV E7 amplifies in cervical cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling (type-I interferon already mapped) underlies the antiviral and antitumour immune response to the HPV-driven cervical cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "HPV oncoproteins disrupt FOXO tumour-suppressor function, removing a brake on proliferation and survival in cervical cancer."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF signalling drives the stromal and angiogenic responses that support the invasive progression of cervical cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory microenvironment of cervical cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates β-catenin and MYC stability (WNT-β-catenin and MYC already mapped), modulating the proliferative signaling of cervical cancer."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2 participates in p53 regulation (p53 already mapped) that, alongside HPV-E6-mediated p53 degradation, restrains apoptosis in cervical cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Aberrant CDK4/6-cyclin-D activity (cyclin-D1 already mapped), reinforced by HPV-E7-driven RB degradation, drives the cell-cycle progression of cervical cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of EGFR (EGFR already mapped) contributes to the invasion of cervical cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of tumor-suppressor genes in HPV-driven cervical cancer."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of cervical cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy, modulated by HPV oncoproteins, supports the survival and therapy resistance of cervical cancer cells."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of cervical cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of cervical cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of cervical cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of cervical cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of cervical cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of cervical cancer."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of cervical cancer."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HPV immunity and vaccine: MHC class II-restricted T-cell help underlies the antibody response (IgG already mapped) to the HPV vaccine, and HPV's downregulation of antigen presentation helps established cervical cancers evade immune clearance."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal defence: secretory IgA at the cervicovaginal mucosa contributes to local immunity against HPV, part of the mucosal barrier that the vaccine and natural infection engage at the site of transmission."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Invasion and resistance: the AXL receptor tyrosine kinase promotes the epithelial-mesenchymal transition and treatment resistance of advanced cervical cancer, a mechanism of progression beyond the HPV-driven oncogenes already mapped."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "TIL immunotherapy: IL-2-driven expansion of tumour-infiltrating lymphocytes (perforin and PD-1 already mapped) underlies the TIL cell therapy now approved for HPV-associated cervical cancer, exploiting its viral neoantigens."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Bleeding and anaemia: abnormal vaginal bleeding is the cardinal symptom of cervical cancer, and the chronic blood loss with chemoradiotherapy myelosuppression lowers haemoglobin, the anaemia that itself worsens radiotherapy outcomes."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: HPV and the cervical tumour induce IL-10 and other immunosuppressive signals that blunt the anti-viral T-cell response, helping the infection persist and the cancer evade immunity."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 carcinogenesis: HPV induces cyclooxygenase-2 and prostaglandin E2 in the cervical epithelium, promoting the inflammation, angiogenesis (VEGF already mapped) and immunosuppression of cervical carcinogenesis, and COX-2 has been studied as a target."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative HPV damage: persistent HPV infection and chronic cervical inflammation generate oxidative stress, to which xanthine oxidase contributes, adding oxidative DNA damage to the E6/E7-driven (p53 and Rb already mapped) carcinogenesis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the angiogenesis and vascular tone of the cervical tumour, and it also contributes to the inflammatory milieu of persistent HPV infection."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment that helps the HPV-driven cancer evade immunity."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of cervical cancer."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant defence: selenium is essential for the glutathione peroxidases that quench the oxidative stress (xanthine oxidase already mapped) of persistent HPV infection, and low selenium status has been linked to cervical dysplasia and cancer risk."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity-related adipokine: leptin is the obesity-related adipokine linked to the risk and progression of the cervical adenocarcinoma and the oestrogen (already mapped) metabolic milieu of cervical cancer."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity and metabolic contribution to cervical cancer."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the metabolic contribution to cervical cancer."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Gynaecological sibling: cervical and endometrial cancers are the common gynaecological cancers of the uterus, distinguished by the site (cervix vs corpus) and the HPV vs oestrogen (already mapped) aetiology."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Gynaecological-oncology context: cervical and ovarian cancers are gynaecological malignancies managed within the gynaecological-oncology field, differing in aetiology and screening."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Anti-HPV T-cell help: the CD4 T-helper cells (IL-2 already mapped) support the cytotoxic (already mapped) anti-HPV E6/E7 (p53 and Rb already mapped) response and the vaccine immunity of cervical cancer."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antiviral/antitumour arm: the IFN-γ of the T cells (perforin already mapped) is the type-II interferon arm of the anti-HPV and anti-tumour immunity of cervical cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the anti-HPV immune response of cervical cancer."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of cervical cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of the HPV-driven cervical cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the cervical-cancer microenvironment."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Anti-HPV antibody arm: the plasma cells secrete the anti-HPV antibodies (immunoglobulin already mapped) that mediate the protection of the prophylactic HPV vaccine against cervical cancer."
---

# Cervical Cancer

## Overview

**Cervical cancer** is the fourth most common cancer in women worldwide (~604,000 new cases/year, ~342,000 deaths/year), with the vast majority of cases driven by persistent **human papillomavirus (HPV)** infection — present in >99% of tumors. HPV16 and HPV18 together account for ~70% of cervical cancers; nonavalent vaccination (Gardasil 9, covering HPV6/11/16/18/31/33/45/52/58) and Pap/HPV co-test screening programs have dramatically reduced incidence in high-income countries, while the global burden remains concentrated in low-and-middle-income countries with limited access to vaccination and screening. HPV oncoproteins **E6** (degrades p53 via E6AP) and **E7** (inactivates RB) together immortalize cervical epithelial cells and suppress the DNA damage response. The systemic therapy landscape has been transformed by KEYNOTE-826, demonstrating that adding pembrolizumab to chemotherapy ± bevacizumab significantly prolongs survival in PD-L1-positive recurrent/metastatic disease [^colombo-2021-keynote826].

**Epidemiology:**
- ~14,000 new cases/year in the US; ~4,100 deaths/year; incidence declining due to HPV vaccination and Pap screening
- Globally: ~604,000 cases/year; most in sub-Saharan Africa, South Asia (limited screening/vaccination access)
- Peak incidence: 35-44 years (invasive cancer); CIN3/carcinoma in situ: 25-35 years
- 5-year survival: ~91% localized; ~58% regional; ~17% distant/metastatic
- Risk factors: HPV infection (necessary cause), smoking (2× risk), immunosuppression (HIV/organ transplant), multiple sexual partners, OCP use (weakly associated)

**Prevention:**
- **Gardasil 9 vaccination:** Covers 9 HPV types → ~90% of cervical cancer-causing types; recommended ages 9-26 (up to 45 shared decision-making); must be given before HPV exposure for full efficacy
- **Screening (US guidelines):** Pap smear alone every 3 years (21-29); Pap + HPV co-testing every 5 years or Pap alone every 3 years (30-65); colposcopy + biopsy for abnormal results → CIN1/2/3 → LEEP/cone biopsy

## Structure

### Histological subtypes

**Squamous cell carcinoma (SCC, ~70-75%):**
Arises from squamocolumnar junction (transformation zone) — the interface between ectocervical squamous epithelium and endocervical columnar epithelium; high-grade squamous intraepithelial lesion (HSIL/CIN3) is the obligate precursor; keratinizing and non-keratinizing variants; p16 IHC diffuse-positive as HPV surrogate; HPV16 most common

**Adenocarcinoma (~20-25%):**
Arises from endocervical columnar epithelium; HPV18 more commonly associated; usual-type endocervical adenocarcinoma (HPVA — HPV-associated adenocarcinoma) most common; gastric-type adenocarcinoma is HPV-independent (STK11/CDKN2A); adenocarcinoma of the endocervix is more difficult to detect on Pap smear → often presents at more advanced stage than SCC

**Adenosquamous carcinoma (<5%):**
Mixed squamous and glandular differentiation; aggressive; associated with HPV

**Rare subtypes:**
- Neuroendocrine carcinoma (small cell/large cell NEC): Aggressive; MYC amplification; treated with platinum+etoposide + chemoradiation; atezolizumab studied; similar to lung SCLC biology
- Clear cell carcinoma: DES-associated (diethylstilbestrol) in older patients; rare; non-HPV-driven; RNF43 mutation
- Undifferentiated carcinoma

### Molecular landscape

**HPV-driven (>99%):**
- HPV16 (~55-60%): High-risk; SCC-associated; highly oncogenic E6/E7
- HPV18 (~10-15%): Adenocarcinoma-associated; faster progression to invasion
- HPV31/33/45/52/58: Additional high-risk types in Gardasil 9

**Key somatic mutations (TCGA 2017):**
- **PIK3CA** mutations: ~35-40% of cervical SCC and adenocarcinoma; helical domain (E542K, E545K) and kinase domain (H1047R) mutations → AKT-mTOR pathway activation → PI3K inhibitors studied
- **PTEN** loss: ~15-20%; cooperates with PIK3CA in adenocarcinoma
- **FBXW7** mutation: ~15%; ubiquitin ligase targeting cyclin E, MYC, NOTCH for degradation
- **KRAS** mutations: ~10-15% of adenocarcinoma; less common in SCC
- **STK11/CDKN2A**: Gastric-type cervical adenocarcinoma (HPV-independent variant)
- **ERBB2 (HER2) amplification**: ~10% of adenocarcinoma; potential target
- **TMB:** Generally moderate; cervical cancer has ~2-3 mutations/Mb; not reliably TMB-high
- **PD-L1 CPS≥1:** ~75% of recurrent/metastatic cervical cancer; PD-L1 CPS≥10: ~50%

## Function

### HPV oncogenesis

**HPV life cycle and malignant transformation:**
HPV16/18 infects basal keratinocytes of the transformation zone via microabrasions → episomal replication → productive infection with viral particle production in differentiated upper layers. In cells that fail to complete the productive cycle, viral DNA may integrate into the host genome → disruption of the E2 open reading frame (which normally suppresses E6/E7) → constitutive E6/E7 overexpression → immortalization and malignant transformation.

**E6 oncoprotein — p53 destruction:**
HPV E6 binds E6AP (UBE3A, a HECT ubiquitin ligase) → E6-E6AP complex binds p53 tumor suppressor → ubiquitination of p53 → proteasomal degradation. Without functional p53, cells cannot arrest at G1 in response to DNA damage and cannot undergo p53-mediated apoptosis → accumulation of mutations → progression from CIN1 → CIN2 → CIN3 → invasive cancer.

**E7 oncoprotein — RB inactivation:**
HPV E7 binds the RB pocket domain at the LXCXE motif → dissociation of RB-E2F complexes → release of free E2F transcription factors → activation of E2F target genes (cyclin A, CDK2, thymidine kinase) → cell cycle entry without mitogenic signals. E7-driven RB inactivation also induces compensatory p16 INK4a (CDKN2A) overexpression — the basis for p16 IHC as a diagnostic marker for HPV infection in cervical pathology.

**Progression from CIN to invasive cancer:**
CIN1 (mild dysplasia) → HPV productive infection, often clears spontaneously (~70% within 1 year)
CIN2 → intermediate dysplasia; ~40-50% regression; high-risk E6/E7 expression
CIN3 (severe dysplasia/carcinoma in situ) → high-risk HPV; p53 + RB inactivated; near-zero spontaneous regression; direct precursor to invasive SCC
Invasive SCC → basement membrane penetration → lymphovascular invasion → nodal spread and distant metastasis

### Normal cervical transformation zone biology

The cervical transformation zone (TZ) — the area between the original and new squamocolumnar junctions — undergoes squamous metaplasia from columnar to squamous epithelium driven by acidic vaginal pH and hormonal changes at puberty. This area of active epithelial remodeling is particularly susceptible to HPV infection because basal cells are exposed during metaplastic transformation. Colposcopy identifies the TZ for targeted biopsy of abnormal areas.

## Pathology

### Staging and workup

**FIGO 2018 staging (clinical and pathological):**
- **Stage I:** Confined to cervix
  - IA1: Stromal invasion ≤3 mm; IA2: >3 to ≤5 mm
  - IB1: >5 mm to ≤2 cm; IB2: >2 to ≤4 cm; IB3: >4 cm
- **Stage II:** Beyond cervix, not to pelvic wall or lower vagina
  - IIA: Upper 2/3 vagina (IIA1: ≤4 cm; IIA2: >4 cm); IIB: Parametrial invasion
- **Stage III:** Pelvic wall, lower vagina, hydronephrosis, or positive nodes (pelvic → IIIC1; para-aortic → IIIC2)
- **Stage IV:** IVA: Bladder/rectal mucosa; IVB: Distant metastasis

**Staging workup:**
- MRI pelvis/abdomen: Primary tumor extent, parametrial invasion, nodal staging — superior to CT for soft tissue assessment
- CT chest/abdomen/pelvis: Lymph node and distant metastasis staging
- FDG-PET/CT: Standard for node-positive or ≥IB3 disease; detects para-aortic lymph node metastasis → alters radiation field; superior sensitivity to CT for nodal staging
- Cystoscopy/proctoscopy: For suspected IVA disease (bladder/rectal involvement)
- Biopsy: Colposcopy-directed or simple punch biopsy of visible lesion for diagnosis

### Treatment

**Early-stage (IA1 with no LVI to IB2):**
- **Surgery:** Radical hysterectomy + bilateral pelvic lymph node dissection (BPLND) ± sentinel lymph node mapping; preferred for young women wishing to avoid radiation-induced ovarian failure
  - IA1 without LVI: Simple hysterectomy or cone biopsy (fertility preservation)
  - IA1 with LVI / IA2 / IB1: Modified radical or radical hysterectomy + PLND
- **Adjuvant chemoradiation** for high-risk pathologic features: Positive margins, positive pelvic nodes, parametrial invasion (GOG-92: pelvic RT; GOG-109: cisplatin+RT superior to RT alone)
- **Fertility-preserving:** Radical trachelectomy + PLND for select IB1 (<2 cm, no LVI, negative MRI nodes)

**Locally advanced (IB3-IVA):**
- **Concurrent cisplatin (40 mg/m² weekly) + external beam radiation therapy (EBRT) + brachytherapy:** Standard of care; based on multiple RTOG trials (GOG-120, GOG-123, RTOG 90-01); cisplatin sensitizes tumor to radiation; EBRT 45-50 Gy to pelvis → high-dose-rate (HDR) intracavitary brachytherapy boost (85-90 Gy EQD2 to HRCTV); 5-year OS ~65-70% for IIB-IIIA
- Carboplatin as cisplatin alternative in renal insufficiency; inferior but acceptable
- **Extended-field RT:** Para-aortic RT for PET-positive para-aortic nodes → improved regional control

**Recurrent/metastatic (persistent or R/M) first-line:**
- **Pembrolizumab + cisplatin/paclitaxel ± bevacizumab (KEYNOTE-826):** [^colombo-2021-keynote826] OS 24.4 vs 16.5 months (PD-L1 CPS≥1) vs chemotherapy alone; PFS 10.4 vs 8.2 months; FDA approved 2021; standard first-line for PD-L1+ R/M cervical cancer
- **Bevacizumab + cisplatin/paclitaxel (GOG-0240):** [^tewari-2014-gog240] OS 17.0 vs 13.3 months vs chemo alone; FDA approved 2014; first targeted agent to improve OS in cervical cancer; ORR 48%; now used with pembrolizumab for PD-L1+ patients
- **Cemiplimab + chemotherapy ± bevacizumab (EMPOWER-Cervical 1):** OS benefit vs chemotherapy in PD-L1+ population; cemiplimab approved 2022 for R/M cervical cancer

**Second-line and beyond:**
- **Tisotumab vedotin (TV, Tivdak):** Antibody-drug conjugate targeting tissue factor (TF) with MMAE warhead; ORR ~24% (innovaTV 204 single-arm); OS benefit vs investigator's choice in TV-301 (phase III); FDA approved 2021 (accelerated), 2023 (regular approval)
- **Pembrolizumab monotherapy:** Active in PD-L1+ recurrent cervical cancer (ORR ~12-14% as monotherapy in KEYNOTE-158)
- **Topotecan:** Standard cytotoxic in 2nd-line; ORR ~13%; used with bevacizumab
- **Ifosfamide:** Active in sarcomatoid variant

## Connections

- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Pembrolizumab + cisplatin/paclitaxel ± bevacizumab (KEYNOTE-826) improved OS vs chemotherapy in PD-L1 CPS≥1 persistent/recurrent/metastatic cervical cancer (24.4 vs 16.5 months); FDA approved 2021; cemiplimab showed similar OS benefit in EMPOWER-Cervical 1.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — HPV E7 oncoprotein binds RB LXCXE motif → RB inactivation → E2F release → S-phase entry; p16 INK4a (CDKN2A) overexpression is IHC surrogate for RB inactivation in cervical cancer; functional RB loss without mutation is universal in HPV-driven cervical carcinogenesis.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — HPV E6 recruits E6AP (UBE3A) ubiquitin ligase → p53 proteasomal degradation → loss of G1 checkpoint and apoptosis; p53 is wild-type but functionally absent in HPV+ cervical cancer; p53 mutation is rare and not required for HPV-driven carcinogenesis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Bevacizumab + cisplatin/paclitaxel (GOG-0240) improved OS vs chemotherapy alone (17.0 vs 13.3 months) in recurrent/metastatic cervical cancer; bevacizumab is standard for metastatic disease; KEYNOTE-826 added pembrolizumab to bevacizumab + chemotherapy for PD-L1+ patients.
- `connects-to` → **[HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md)** — HPV16/18 infect cervical transformation zone → E6-mediated p53 degradation + E7-mediated RB inactivation → CIN1-3 → invasive carcinoma; HPV16 accounts for ~55% of cervical SCC; viral genome integration disrupts E2 repressor → constitutive E6/E7 overexpression.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutations (E542K, E545K, H1047R) occur in ~35-40% of cervical SCC and adenocarcinoma → AKT-mTOR activation → proliferation; PIK3CA mutation cooperates with HPV E6/E7 in transformation; PI3K inhibitors (alpelisib) being studied in PIK3CA-mutant recurrent cervical cancer.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS mutations occur in ~10-15% of endocervical adenocarcinoma; gastric-type adenocarcinoma is HPV-independent with frequent KRAS + STK11 mutations; KRAS mutation predicts poor response to platinum chemotherapy; no approved KRAS inhibitors for cervical adenocarcinoma.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — Cervical cancer and HPV-positive head-and-neck cancer are the same disease in different epithelia: both arise when high-risk HPV over-expresses E6 and E7 to destroy p53 and inactivate RB, and both carry a better prognosis than HPV-negative cancers.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Immunosuppression sharply raises cervical-cancer risk: HIV-positive women clear HPV poorly and progress from dysplasia to invasive cancer faster, so invasive cervical cancer is an AIDS-defining illness and these patients need intensified HPV screening and earlier colposcopy.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8+ cytotoxic T cells are both the natural defense that usually clears HPV and the target of cervical-cancer immunotherapy: persistent infection reflects failed CD8 surveillance, and checkpoint blockade (pembrolizumab, KEYNOTE-826) unleashes them against the tumor.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Cervical and bladder cancers share the pelvic neighborhood: locally advanced cervical cancer can invade the bladder (vesicovaginal fistula, hematuria), pelvic radiotherapy for one raises risk of the other, and both are smoking-associated cancers managed by pelvic oncology.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Cervical and endometrial cancers are the main uterine-region malignancies but differ: cervical is HPV-driven squamous cancer of the cervix (vaccine-preventable, screen-detected), while endometrial is estrogen/Lynch-driven adenocarcinoma of the uterine body with abnormal bleeding.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Cervical and ovarian cancers are both gynecologic malignancies but contrast in prevention: cervical cancer has effective screening and an HPV vaccine and presents early, whereas ovarian cancer (often BRCA-driven) has no good screening and usually presents late.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Peutz-Jeghers syndrome causes a rare HPV-independent cervical cancer, adenoma malignum: germline STK11 loss drives this deceptively bland mucinous tumor—the one cervical cancer not prevented by HPV vaccination, warranting surveillance in PJS.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is curative for locally advanced cervical cancer: concurrent chemoradiation with external-beam photons plus intracavitary brachytherapy delivers a high radiation dose directly to the cervix—and brachytherapy is uniquely critical to cure in this cancer.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — The HPV vaccine that prevents cervical cancer works through dendritic cells: virus-like particles are taken up by dendritic cells that prime B and T cells to make neutralizing antibodies against HPV capsids, blocking the infection behind nearly all cervical cancer.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Cervical cancer is fundamentally an immune-control failure: most HPV infections clear, but when immune surveillance falters—markedly in HIV—persistent high-risk HPV transforms cervical cells, so immune status governs whether infection becomes cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help clear HPV-infected cervical cells: innate NK responses and interferon limit early infection, and HPV evades them by downregulating immune signals—so weakened NK/innate immunity allows the persistent infection that precedes cervical cancer.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — HPV reactivates telomerase to immortalize cervical cells: the viral E6 oncoprotein, beyond degrading p53, switches on TERT, so infected cells avoid the telomere shortening that normally limits division—a key step from infection to invasive cancer.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cervical cancer is the most preventable cancer of the reproductive system: HPV infects the cervical transformation zone, but Pap/HPV screening catches precancer and vaccination blocks the virus—so a leading female-reproductive cancer is now largely avoidable.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Cervical cancer spreads predictably through the lymphatic system: tumor cells drain to pelvic and para-aortic nodes, so lymph-node status is the dominant prognostic factor and dictates whether surgery or chemoradiation is used and how widely it is targeted.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-ion radiotherapy is an option for some cervical cancers: heavy carbon ions deposit a sharply localized, highly damaging dose, useful for bulky or radioresistant gynecologic tumors—an alternative to conventional photon radiation in specialized centers.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Cervical cancer is now vaccine-preventable through B cells: the HPV vaccine elicits B-cell antibodies against the L1 capsid that block infection before it can transform cervical cells, so a humoral immune response is dramatically cutting cervical cancer rates.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Advanced cervical cancer kills through the kidneys: tumor spreading sideways in the pelvis encases the ureters, causing obstruction and hydronephrosis, so post-renal kidney failure—not the primary tumor—is a classic cause of death.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Cervical cancer intersects with pregnancy at the cervix: screening often first detects disease in young, pregnant women, and cancer found in pregnancy forces hard timing decisions around delivery—so obstetric care and cancer care must be coordinated.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Cervical cancer is flagged by p16, the CDKN2A protein: HPV's E7 disables Rb, which paradoxically drives p16 sky-high, so strong p16 staining is the pathologist's surrogate marker that a lesion is HPV-driven and truly precancerous.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Cervical squamous tumors lean on EGFR: the receptor is frequently overexpressed and drives growth, making the ErbB pathway a studied target in advanced cervical cancer alongside anti-angiogenic and checkpoint therapy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — HPV and cervical tumors hide behind regulatory T cells: Tregs infiltrate the lesion and suppress the cytotoxic response that should clear infected cells, part of the immune evasion that lets persistent HPV progress to cancer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Cervical tumors are notoriously oxygen-starved, and that resists radiation: hypoxic regions survive radiotherapy because oxygen is needed to fix radiation-induced DNA damage, so tumor hypoxia predicts worse outcomes and drives research into overcoming it.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — HPV silences the interferon alarm in cervical cancer: the viral E6 and E7 proteins suppress type I interferon signaling, blunting the antiviral response so infected cells evade clearance—an immune escape that lets persistent infection progress.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Advanced cervical cancer spreads to the lungs: tumor cells travel through blood and lymph to seed pulmonary metastases, a common site of distant disease that shapes staging and the shift from curative to systemic treatment.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Cervical cancer bleeds away iron: irregular and postcoital vaginal bleeding is an early sign, and the steady blood loss drains iron into a deficiency anemia that often brings women in for the diagnosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Advanced cervical cancer invades the rectum: spreading through the pelvis, it can breach the large intestine and bladder, forming fistulas that leak stool or urine—devastating complications of locally advanced disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Curing cervical cancer can leave fibrosis behind: the pelvic radiotherapy central to treatment scars surrounding tissues, stiffening the vagina, bladder, and bowel and causing lasting side effects in survivors.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Cervical cancer is fed by new vessels: VEGF drives endothelial cells to vascularize the tumor, and bevacizumab that blocks them improves survival in advanced disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Cervical cancer ultimately spreads to the liver: hematogenous metastasis to liver, lung and bone marks advanced disease beyond its local pelvic invasion.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Pelvic chemoradiation for cervical cancer hits the bone marrow: much of the body's active marrow sits in the pelvis, so treatment causes cytopenias that limit how much chemotherapy can be given.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals HPV's fingerprint on the cervix: infected cells become koilocytes with a clear perinuclear halo and shrunken raisin-like nucleus, and viral particles assemble in the upper layers — the cytologic clue a Pap smear hunts for.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Cervical cancer rarely reaches the brain, but when it does it marks the end stage: late hematogenous spread seeds cerebral metastases, an uncommon site beyond its usual march to lung, liver, and bone.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D may help the body clear HPV: deficiency is associated with persistent infection and cervical dysplasia, fitting the vitamin's role in the immune defense that decides whether an HPV infection resolves or progresses.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — The vaccine works by raising antibody: HPV vaccines teach the immune system to make neutralizing antibodies against the virus's capsid, blocking the infection that causes nearly all cervical cancer — a vaccine that prevents a cancer.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Cervical cancer announces itself in blood and worsens with anemia: abnormal vaginal bleeding is the cardinal symptom, and the resulting low red-cell count both weakens the patient and blunts the tumor's response to radiotherapy.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Advanced disease reaches the nerves: pelvic sidewall spread compresses the lumbosacral plexus into leg pain and weakness, while the cisplatin given with radiation injures peripheral sensory neurons.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Clearing HPV is a CD4 job: a strong Th1 helper-T response normally eliminates the virus, so when helper-T immunity falters — in HIV or other immunosuppression — the infection persists and progresses toward cancer, why screening is intensified in these patients.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen is a cofactor in cervical carcinogenesis: in HPV-infected tissue estrogen signaling cooperates with the E6/E7 oncoproteins to drive progression, consistent with the modest extra risk seen with very long-term combined oral contraceptive use.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — HPV's oncoproteins are built around zinc: both E6 and E7 fold into zinc-binding domains that they need to grip and degrade p53 and Rb, so the metal ion is structurally essential to the very proteins that transform the cell.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Advanced cervical cancer kills through the kidneys: local spread encases the ureters and blocks urine flow, so obstructive uropathy and the resulting renal failure are a classic and common cause of death from the disease.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 fuels the HPV-driven tumor: the cytokine activates STAT3 to drive cervical cancer growth, angiogenesis, and resistance to chemoradiation, and high levels mark a worse prognosis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor macrophages help HPV hide: M2-polarized tumor-associated macrophages in the cervical lesion suppress the antiviral T-cell response and promote invasion, abetting the immune evasion that lets the cancer grow.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic inflammation keeps NF-κB switched on: HPV infection and the inflamed cervical microenvironment activate NF-κB, driving pro-survival and pro-invasive gene programs that help the transformed cells persist and progress.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Stromal fibroblasts abet invasion: cancer-associated fibroblasts in the cervical tumor remodel the matrix and secrete factors that promote angiogenesis and help the carcinoma breach the basement membrane.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Pelvic cancer raises the clot risk: advanced cervical cancer and its treatment promote venous thromboembolism, both through the tumor's pro-coagulant state and pelvic vein compression by bulky disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — HPV oncoproteins switch on STAT3: E6/E7 and the inflamed cervical microenvironment activate STAT3, driving proliferation and immune evasion in the progression from HPV infection to invasive cancer.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Bulky pelvic disease opens routes to infection: tumor obstruction of the ureters causes pyelonephritis and urosepsis, while necrotic tumor and fistulae into bladder or bowel can seed pelvic infection and sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic bleeding and inflammation drain the blood: ongoing vaginal blood loss plus the cancer's inflammatory cytokines produce anemia that not only weakens patients but blunts the tumor's response to radiotherapy.
- `connects-to` → **[HIV](../hiv/README.md)** — Immune loss lets HPV run to cancer: HIV impairs clearance of human papillomavirus, so cervical cancer occurs more often, at younger ages and more aggressively — making it an AIDS-defining malignancy.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Steady vaginal bleeding depletes iron: the abnormal and postcoital bleeding of cervical cancer causes chronic blood loss, draining iron stores into an iron-deficiency anemia that often prompts the diagnosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Diagnosis and its sexual toll weigh on mood: a cancer affecting fertility, sexual function and often younger women carries a substantial psychological burden, with high rates of depression.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pelvic spread and treatment injure nerves: tumor invading the pelvic sidewall and the cisplatin and radiation used to treat cervical cancer cause lumbosacral plexopathy and chemotherapy neuropathy with chronic pain.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Pelvic radiation and lost ovaries weaken bone: radiotherapy causes insufficiency fractures and bone loss, and treatment-induced menopause in younger patients withdraws estrogen, accelerating osteoporosis.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its chemoradiation opens the lung to mold: the neutropenia from cisplatin-based chemoradiation for cervical cancer can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Locally advanced tumour strangles the ureters: cervical cancer spreading into the pelvis obstructs the ureters, causing hydronephrosis and renal failure — a classic and common cause of death from the disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Pelvic radiation and spread injure the bowel: chemoradiation for cervical cancer causes radiation proctitis and enteritis, and advanced tumour can erode into the rectum to form a rectovaginal fistula.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A young woman's cancer with fertility loss breeds worry: the diagnosis, loss of fertility and recurrence surveillance of cervical cancer foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to the lungs: the lungs are the commonest site of distant metastasis in cervical cancer, appearing as nodules on staging and recurrence imaging.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It seeds the bones: cervical cancer metastasises to the spine and pelvis, causing bone pain and pathological fractures in advanced disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Pelvic recurrence invades the nerves: tumour growth into the lumbosacral plexus causes a painful plexopathy with leg weakness and numbness, a distressing late complication.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Treatment strains the circulation: cisplatin chemoradiation carries cardiovascular and thromboembolic risk, and pelvic radiation can damage the iliac vessels over time.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Virus and therapy both touch the skin: the same HPV family causes genital and skin warts, while pelvic radiotherapy produces radiation dermatitis and rare cutaneous metastases mark advanced disease.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — A suspected co-factor: herpes simplex virus type 2 was long studied as a possible co-factor cooperating with HPV in cervical carcinogenesis, and genital herpes shares its transmission route.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy extends survival: pembrolizumab added to chemotherapy, and cemiplimab after it, improve survival in advanced PD-L1-positive cervical cancer, which is virally driven and immunogenic.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cisplatin chemoradiation is the backbone: concurrent cisplatin-based chemoradiotherapy is the curative-intent standard for locally advanced cervical cancer.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — Immunodeficiency accelerates it: HIV greatly raises cervical cancer risk by impairing clearance of oncogenic HPV, making it an AIDS-defining cancer and a screening priority in HIV-positive women.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Anti-angiogenics and ADCs extend it: bevacizumab against VEGF improves survival in advanced cervical cancer, and tissue-factor-targeting tisotumab vedotin is an antibody-drug conjugate for recurrent disease beyond chemoradiation.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Advanced disease seeds bone: metastatic cervical cancer spreads to the spine and pelvis as painful osteolytic lesions, a late manifestation after pelvic and nodal spread.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — It kills through the kidneys: locally advanced cervical cancer encases the ureters, and bilateral obstruction backs pressure up to the glomeruli, dropping filtration to cause the uraemia that is a classic cause of death.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Where it spreads: advanced cervical cancer metastasises through the blood to the lungs, seeding tumour deposits in the alveolar capillary bed.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Immune evasion and immunotherapy: HPV-driven cervical cancer draws tertiary lymphoid structures and responds to PD-1 checkpoint blockade, the immune dimension of an infection-driven cancer.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — An emerging target: HER2 amplification occurs in a subset of cervical and other gynaecological cancers, making HER2-directed antibody-drug conjugates a developing treatment option.
- `connects-to` → **[GVHD](../gvhd/README.md)** — Immunosuppression and HPV cancer: transplant recipients and those on GVHD-related immunosuppression have markedly higher rates of HPV-driven cervical and other anogenital cancers.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Radiation's late cancer risk: pelvic radiotherapy for cervical cancer slightly raises the risk of second cancers in the radiation field, including rectal and colorectal cancer years later.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Screening disrupted: COVID-19 sharply cut cervical screening and HPV vaccination uptake, projected to raise cervical cancer incidence and stage at diagnosis in coming years.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC amplification: gain of the 3q26 region amplifying MYC is a common driver of cervical cancer progression, cooperating with HPV E6/E7 to fuel proliferation.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Context-dependent Notch: NOTCH1 is recurrently mutated in cervical cancer, where Notch signalling can act as either tumour suppressor or oncogene depending on stage and context.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Local rectal invasion: advanced cervical cancer can invade the rectum and create rectovaginal fistulas, breaching the intestinal epithelium—a debilitating feature of locally advanced disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT signalling: PIK3CA mutation is among the commonest events in cervical cancer, activating AKT to drive growth and survival and offering a targeted therapeutic node.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxia and radioresistance: HIF-1α stabilised in hypoxic cervical tumours drives angiogenesis and resistance to radiotherapy, a key adverse prognostic factor.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic driver: HPV E7 upregulates EZH2, whose PRC2 silencing of tumour-suppressor genes promotes the progression of HPV-driven cervical cancer.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K-mTOR axis: frequent PIK3CA mutations and PI3K-AKT-mTOR activation drive cervical cancer growth, an actionable pathway downstream of the loss of tumour-suppressor control by HPV oncoproteins.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Immune evasion and EMT: TGF-beta in the cervical tumour microenvironment suppresses anti-tumour immunity and promotes epithelial-mesenchymal transition and invasion in advancing disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws tumour-associated macrophages into cervical cancer, building an immunosuppressive microenvironment that abets HPV-driven tumour progression.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — HPV oncoproteins antagonize the cGAS-STING DNA-sensing pathway to evade innate immunity, while viral genome integration generates the cytosolic DNA and chromosomal instability this pathway would otherwise detect and act on.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD8 T cells use perforin to eliminate HPV-infected cells, the response that prophylactic and therapeutic HPV vaccines harness—and whose evasion by persistent high-risk HPV permits progression to cervical cancer.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — The CXCL12-CXCR4 axis drives the parametrial invasion and lymph-node metastasis of cervical cancer, the spread that governs FIGO staging and the decision to use concurrent chemoradiation.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The HPV E7 oncoprotein inactivates Rb, freeing E2F transcription factors to drive the cell cycle—the second arm of viral transformation alongside E6's degradation of p53, the pair that immortalizes the infected cervical cell.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Concurrent cisplatin chemoradiation, the standard for locally advanced cervical cancer, kills tumor cells through caspase-3-mediated apoptosis, the death pathway whose evasion underlies radioresistance.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — HPV vaccines induce neutralizing IgG against the L1 capsid that blocks infection, the primary-prevention strategy now driving cervical cancer toward elimination where vaccination is widespread.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss intensifies PI3K-AKT-mTOR signaling (PIK3CA, AKT and mTOR already mapped), a frequent somatic event cooperating with HPV E6/E7 in cervical carcinoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGFR and RAS signaling (EGFR and KRAS already mapped) drive the MAPK-ERK cascade in cervical cancer, sustaining proliferation and serving as a candidate therapeutic axis.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Loss of E-cadherin during epithelial-mesenchymal transition releases cervical-carcinoma cells from their junctions, enabling stromal invasion and the lymph-node spread that worsens prognosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — HPV oncoproteins suppress the type-I-interferon response (already mapped), and JAK-STAT signaling (STAT3 mapped) governs the immune evasion and inflammatory signaling of cervical cancer.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant activation contributes to the chemo- and radio-resistance of cervical cancer, protecting tumor cells from treatment-induced oxidative stress.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/β-catenin signaling cooperates with HPV oncoproteins in the progression from cervical intraepithelial neoplasia to invasive carcinoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) shifts from tumor suppression to promotion of invasion and EMT in cervical carcinogenesis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates apoptosis resistance and the immune microenvironment of cervical cancer.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cyclin-D-CDK4/6 activity (CDKN2A/p16, RB1 and E2F1 mapped) drives the cell-cycle dysregulation that HPV E7 amplifies in cervical cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling (type-I interferon already mapped) underlies the antiviral and antitumor immune response to the HPV-driven cervical cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — HPV oncoproteins disrupt FOXO tumor-suppressor function, removing a brake on proliferation and survival in cervical cancer.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF signaling drives the stromal and angiogenic responses that support the invasive progression of cervical cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory microenvironment of cervical cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates β-catenin and MYC stability (WNT-β-catenin and MYC already mapped), modulating the proliferative signaling of cervical cancer.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 participates in p53 regulation (p53 already mapped) that, alongside HPV-E6-mediated p53 degradation, restrains apoptosis in cervical cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Aberrant CDK4/6-cyclin-D activity (cyclin-D1 already mapped), reinforced by HPV-E7-driven RB degradation, drives the cell-cycle progression of cervical cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of EGFR (EGFR already mapped) contributes to the invasion of cervical cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of tumor-suppressor genes in HPV-driven cervical cancer.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of cervical cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy, modulated by HPV oncoproteins, supports the survival and therapy resistance of cervical cancer cells.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of cervical cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of cervical cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of cervical cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of cervical cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of cervical cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of cervical cancer.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of cervical cancer.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — HPV immunity and vaccine: MHC class II-restricted T-cell help underlies the antibody response (IgG already mapped) to the HPV vaccine, and HPV's downregulation of antigen presentation helps established cervical cancers evade immune clearance.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal defence: secretory IgA at the cervicovaginal mucosa contributes to local immunity against HPV, part of the mucosal barrier that the vaccine and natural infection engage at the site of transmission.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Invasion and resistance: the AXL receptor tyrosine kinase promotes the epithelial-mesenchymal transition and treatment resistance of advanced cervical cancer, a mechanism of progression beyond the HPV-driven oncogenes already mapped.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — TIL immunotherapy: IL-2-driven expansion of tumour-infiltrating lymphocytes (perforin and PD-1 already mapped) underlies the TIL cell therapy now approved for HPV-associated cervical cancer, exploiting its viral neoantigens.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Bleeding and anaemia: abnormal vaginal bleeding is the cardinal symptom of cervical cancer, and the chronic blood loss with chemoradiotherapy myelosuppression lowers haemoglobin, the anaemia that itself worsens radiotherapy outcomes.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: HPV and the cervical tumour induce IL-10 and other immunosuppressive signals that blunt the anti-viral T-cell response, helping the infection persist and the cancer evade immunity.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 carcinogenesis: HPV induces cyclooxygenase-2 and prostaglandin E2 in the cervical epithelium, promoting the inflammation, angiogenesis (VEGF already mapped) and immunosuppression of cervical carcinogenesis, and COX-2 has been studied as a target.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative HPV damage: persistent HPV infection and chronic cervical inflammation generate oxidative stress, to which xanthine oxidase contributes, adding oxidative DNA damage to the E6/E7-driven (p53 and Rb already mapped) carcinogenesis.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the angiogenesis and vascular tone of the cervical tumour, and it also contributes to the inflammatory milieu of persistent HPV infection.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment that helps the HPV-driven cancer evade immunity.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of cervical cancer.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant defence: selenium is essential for the glutathione peroxidases that quench the oxidative stress (xanthine oxidase already mapped) of persistent HPV infection, and low selenium status has been linked to cervical dysplasia and cancer risk.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity-related adipokine: leptin is the obesity-related adipokine linked to the risk and progression of the cervical adenocarcinoma and the oestrogen (already mapped) metabolic milieu of cervical cancer.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity and metabolic contribution to cervical cancer.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the metabolic contribution to cervical cancer.
- `connects-to` → **[Endometrial cancer](../endometrial-cancer/README.md)** — Gynaecological sibling: cervical and endometrial cancers are the common gynaecological cancers of the uterus, distinguished by the site (cervix vs corpus) and the HPV vs oestrogen (already mapped) aetiology.
- `connects-to` → **[Ovarian cancer](../ovarian-cancer/README.md)** — Gynaecological-oncology context: cervical and ovarian cancers are gynaecological malignancies managed within the gynaecological-oncology field, differing in aetiology and screening.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Anti-HPV T-cell help: the CD4 T-helper cells (IL-2 already mapped) support the cytotoxic (already mapped) anti-HPV E6/E7 (p53 and Rb already mapped) response and the vaccine immunity of cervical cancer.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antiviral/antitumour arm: the IFN-γ of the T cells (perforin already mapped) is the type-II interferon arm of the anti-HPV and anti-tumour immunity of cervical cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the anti-HPV immune response of cervical cancer.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of cervical cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of the HPV-driven cervical cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the cervical-cancer microenvironment.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Anti-HPV antibody arm: the plasma cells secrete the anti-HPV antibodies (immunoglobulin already mapped) that mediate the protection of the prophylactic HPV vaccine against cervical cancer.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^tewari-2014-gog240]: Tewari KS, Sill MW, Long HJ 3rd, et al. Improved survival with bevacizumab in advanced cervical cancer. *N Engl J Med.* 2014;370(8):734-743. [doi:10.1056/NEJMoa1309748](https://doi.org/10.1056/NEJMoa1309748) · [PubMed 24552320](https://pubmed.ncbi.nlm.nih.gov/24552320/)
[^colombo-2021-keynote826]: Colombo N, Dubot C, Lorusso D, et al. Pembrolizumab for persistent, recurrent, or metastatic cervical cancer. *N Engl J Med.* 2021;385(20):1856-1867. [doi:10.1056/NEJMoa2112435](https://doi.org/10.1056/NEJMoa2112435) · [PubMed 34534430](https://pubmed.ncbi.nlm.nih.gov/34534430/)
