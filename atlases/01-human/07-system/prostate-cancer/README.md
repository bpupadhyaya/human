---
schema: human-scale-entry/v1
id: prostate-cancer
name: Prostate Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Second leading cancer death in men; driven by androgen receptor (AR) signaling; PTEN loss (~50%) and AR amplification underlie castration-resistant progression. Docetaxel, abiraterone, enzalutamide, olaparib (BRCA-mutant HRR deficient), and lutetium-177-PSMA are active in mCRPC."
aliases: ["PCa", "prostate adenocarcinoma", "CRPC", "castration-resistant prostate cancer", "mCRPC", "hormone-sensitive prostate cancer", "mCSPC", "CSPC"]
sources:
  - id: beer-2014-prevail
    type: peer-reviewed
    cite: "Beer TM, Armstrong AJ, Rathkopf D, et al. Enzalutamide in metastatic prostate cancer before chemotherapy. N Engl J Med. 2014;371(5):424-433."
    doi: "10.1056/NEJMoa1405095"
    pmid: "24881730"
    url: "https://doi.org/10.1056/NEJMoa1405095"
  - id: sartor-2021-vision
    type: peer-reviewed
    cite: "Sartor O, de Bono J, Chi KN, et al. Lutetium-PSMA-617 for metastatic castration-resistant prostate cancer. N Engl J Med. 2021;385(12):1091-1103."
    doi: "10.1056/NEJMoa2107322"
    pmid: "34161051"
    url: "https://doi.org/10.1056/NEJMoa2107322"
  - id: de-bono-2020-profound
    type: peer-reviewed
    cite: "de Bono J, Mateo J, Fizazi K, et al. Olaparib for metastatic castration-resistant prostate cancer. N Engl J Med. 2020;382(22):2091-2102."
    doi: "10.1056/NEJMoa1911440"
    pmid: "32343890"
    url: "https://doi.org/10.1056/NEJMoa1911440"
cross_links:
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "AR is the primary driver of prostate cancer; ADT is foundational; resistance via AR amplification, AR-V7 splice variant, and LBD mutations drives CRPC; enzalutamide, apalutamide, and darolutamide extend survival in mCSPC and mCRPC."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss occurs in ~50% of localized and ~70% of mCRPC; PTEN null → AKT-AR crosstalk → poor prognosis; PTEN-null tumors have higher Gleason grade; ipatasertib + abiraterone (IPATential150) improves rPFS in PTEN-null mCRPC."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1/2 and ATM mutations occur in ~25% of mCRPC (germline + somatic); HRR deficiency → PARP inhibitor sensitivity; olaparib (PROfound) and rucaparib (TRITON2) approved for BRCA-mutant mCRPC; germline testing recommended for all mCRPC patients."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR is activated downstream of PTEN loss in prostate cancer; mTOR inhibitors showed modest activity alone; combinations with AR-pathway inhibitors under study; TORC1/2 dual inhibitors with enzalutamide in trials for PTEN-null CRPC."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Testosterone fuels AR-driven prostate cancer; ADT (GnRH agonists/antagonists) is first-line for advanced disease; castration resistance arises via AR amplification, AR-V7, and adrenal androgen synthesis; abiraterone (CYP17A1 inhibitor) blocks residual androgens in CRPC."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The prostate is a male reproductive accessory gland encircling the urethra; ~70% of cancers arise in its peripheral zone (palpable on DRE) while benign hyperplasia crowds the transitional zone; localized disease may be watched, irradiated, or removed by radical prostatectomy."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "BRCA2 is the most important inherited prostate-cancer gene: germline BRCA2 raises risk 4-6× and predicts higher Gleason grade, and BRCA2/HRR deficiency makes tumors PARP-inhibitor-sensitive (olaparib PROfound); germline testing is recommended for all metastatic disease."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Over 85% of prostate-cancer metastases go to bone, where tumor cells drive osteoblasts to overproduce RANKL → osteoclast activation → a vicious cycle of bone destruction and growth-factor release; the anti-RANKL antibody denosumab reduces skeletal-related events."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Prostate and colorectal cancers are two of the commonest adult solid tumours, both rising with age and Western diet; both have hereditary forms—BRCA2 raises lethal prostate cancer, Lynch raises both—and PARP and checkpoint therapy now target their DNA-repair-deficient subsets."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Prostate cancer characteristically forms osteoblastic (bone-forming) metastases: tumour-secreted Wnt, ET-1 and BMPs drive osteoblasts to lay down disorganized woven bone, while RANKL fuels a vicious turnover cycle; this pattern underlies bone-targeted radium-223 and denosumab."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Prostate and breast cancers are the paradigm hormone-driven adenocarcinomas—androgen- vs estrogen-receptor signalling—each treated by depriving that hormone; they also share BRCA1/2 predisposition, so PARP inhibitors (olaparib) work in both, and both seed bone metastases."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is a curative mainstay for localized prostate cancer: external-beam photon radiation and brachytherapy (radioactive seeds) rival surgery for cure, while in metastatic disease the radioligand Lu-177-PSMA delivers radiation to PSMA-expressing tumor cells."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Lynch syndrome modestly raises prostate cancer risk: mismatch-repair-deficient prostate cancers are part of the Lynch spectrum, and like other MSI-high tumors can respond to checkpoint blockade, so a strong family cancer history warrants germline MMR testing."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Prostate cancer hosts the first FDA-approved cancer vaccine, a dendritic-cell therapy: sipuleucel-T harvests a patient's antigen-presenting cells, primes them against prostatic acid phosphatase, and reinfuses them to spark a T-cell response against the tumor."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Prostate cancer is part of the BRCA/HBOC cancer spectrum: germline BRCA2 (and BRCA1) mutations raise prostate cancer risk and aggressiveness, and BRCA-mutant tumors respond to PARP inhibitors—so HBOC families need prostate screening."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Prostate and pancreatic cancer share BRCA2-linked DNA-repair predisposition: families with BRCA2 mutations face raised risk of both, and both respond to platinum and PARP-inhibitor therapy—two distant organs linked by one gene."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Prostate and bladder cancer are the two commonest urologic malignancies but differ: prostate cancer arises from androgen-driven glandular epithelium, while bladder cancer is a smoking-linked urothelial tumor—both present with urinary symptoms, so evaluation overlaps."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC amplification is an early prostate cancer driver: MYC gains, often with PTEN loss and ERG fusions, push the malignant transformation and predict aggressive disease—so the same proliferation oncogene seen across cancers helps grade prostate tumor biology."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Prostate cancer's bone metastases hijack osteoclasts: though the lesions look bone-forming (osteoblastic), tumor RANKL still activates osteoclasts, fueling a vicious cycle of bone turnover—so denosumab and bisphosphonates that block osteoclasts reduce skeletal events."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Prostate cancer floods the bone marrow: it spreads preferentially to the axial-skeleton marrow, where deposits cause pain, fractures and marrow failure with anemia, so bone is the dominant metastatic site that drives the morbidity of advanced disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Liver metastasis marks aggressive prostate cancer: though bone is the usual target, spread to the liver (and other viscera) signals a more lethal, often treatment-resistant or neuroendocrine phenotype—so visceral metastases carry worse prognosis than bone-only disease."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Prostate cancer can also seed the lung: less common than bone metastasis, pulmonary spread reflects hematogenous dissemination of advanced disease, so chest imaging in progressive castration-resistant cancer can reveal visceral metastases that change treatment."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Prostate cancer is an immunologically 'cold' tumor: it has few mutations and poor T-cell infiltration, so checkpoint inhibitors largely fail, and sipuleucel-T—a vaccine priming cytotoxic T cells against prostate antigen—remains one of the few working immunotherapies."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Prostate cancer with ATM or BRCA defects is PARP-sensitive: like BRCA, ATM loss impairs DNA repair, marking metastatic tumors that respond to PARP inhibitors—so guideline testing of homologous-recombination genes now guides therapy."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Prostate cancer can escape hormone therapy by turning neuroendocrine: under prolonged androgen blockade, some tumors transdifferentiate into aggressive, AR-independent neuroendocrine prostate cancer—a treatment-emergent resistance resembling small-cell cancer."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Prostate cancer makes bone in its metastases: unusually, its bone deposits are osteoblastic (bone-forming) rather than lytic, and the calcium-seeking alpha-emitter radium-223 homes to these lesions to deliver targeted radiation and prolong life."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Prostate cancer leans on the PTEN-AKT pathway: PTEN loss is one of its commonest events, switching on AKT survival signaling that cooperates with the androgen receptor—so AKT inhibitors are combined with hormone therapy in PTEN-deficient disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Prostate cancer is an immunologically cold tumor full of regulatory T cells: a Treg-rich, suppressive microenvironment is why checkpoint immunotherapy mostly fails here, leaving the dendritic-cell vaccine sipuleucel-T as the main immune option."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Prostate cancer is supported by tumor-associated macrophages: they promote its growth, angiogenesis, and especially its spread to bone, where they help build the niche for the osteoblastic metastases that define advanced disease."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "The prostate is the body's zinc capital, and cancer abandons it: healthy prostate cells hoard zinc to block citrate breakdown, but malignant cells lose this zinc accumulation to fuel their metabolism—a metabolic switch unique to prostate cancer."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Advanced prostate cancer can shut down the kidneys: the enlarging tumor or its pelvic lymph nodes compress the ureters and bladder outlet, backing urine up into the kidneys (hydronephrosis) and causing post-renal failure."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Prostate cancer recruits fibroblasts as accomplices: cancer-associated fibroblasts form the reactive stroma around tumor glands, secreting growth and remodeling signals that spur invasion—and the amount of reactive stroma predicts outcome."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Prostate cancer's bone metastases are unusually bone-forming: osteoblastic lesions lay down calcium-phosphate, so the invaded skeleton turns denser, not eaten away—the opposite of most cancers' bone disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Prostate cancer loves nerves: perineural invasion, tracking along nerve sheaths, is a hallmark route of spread out of the gland and a marker of aggressiveness read on the biopsy."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Even after castration the adrenal glands feed prostate cancer: they keep making androgens that fuel castration-resistant disease, which is why abiraterone blocks adrenal steroid synthesis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy unmasks prostate cancer's most lethal turn: when it transforms into a neuroendocrine cancer to escape hormone therapy, the cells fill with dense-core secretory granules — the ultrastructure that flags this treatment-resistant variant."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The treatment can wound the heart: androgen-deprivation therapy, the backbone of advanced prostate cancer care, raises the risk of metabolic syndrome, coronary disease, and cardiac events by stripping away protective testosterone."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Prostate cancer rarely reaches the brain, but when it does it signals trouble: the aggressive neuroendocrine and late castration-resistant forms can seed cerebral and dural metastases, a grave sign in end-stage disease."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Shutting off testosterone lowers the red cells: androgen deprivation therapy removes a hormone that drives erythropoiesis, so a mild anemia is a common, expected side effect of treating prostate cancer."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Androgen deprivation reshapes the body's fat: it drives weight gain, insulin resistance, and a sarcopenic obesity, the metabolic syndrome that raises cardiovascular and diabetic risk during long-term hormone therapy."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The rectum sits right behind the prostate: locally advanced tumors can invade it, and the radiotherapy aimed at the gland often inflames it into a radiation proctitis with bleeding and urgency."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies screen, image, and treat it: the PSA blood test is an antibody immunoassay, PSMA-targeted antibodies guide PET imaging and radioligand therapy, and sipuleucel-T harnesses the immune system against the tumor."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads first to the pelvic nodes: prostate cancer drains to the obturator and iliac lymph nodes, so nodal staging by imaging or dissection shapes treatment before the more distant bone metastases appear."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Chemotherapy for advanced disease taxes the marrow: the docetaxel and cabazitaxel given in castration-resistant prostate cancer are myelosuppressive, dropping neutrophil counts and raising the risk of febrile neutropenia."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Losing p53 turns prostate cancer lethal: TP53 mutation, often with RB loss, drives the shift to aggressive castration-resistant and neuroendocrine disease that escapes hormone therapy and carries a grim prognosis."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "The hormone therapy that controls it thins the bones: androgen-deprivation therapy strips the testosterone that maintains the male skeleton, accelerating bone loss and fractures, so patients need bone-density monitoring with calcium, vitamin D, and antiresorptive drugs."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium promised prostate protection but failed: the large SELECT trial found selenium supplements did not prevent prostate cancer (and vitamin E may have slightly raised risk), tempering the antioxidant chemoprevention hopes."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Most of it resists immunotherapy: prostate cancer is immunologically cold, so PD-1 blockade helps only the rare mismatch-repair-deficient, high-mutation tumors — a reminder that checkpoint drugs need a visible target to work."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Excess weight breeds the aggressive form: obesity is linked less to getting prostate cancer than to developing the high-grade, lethal disease, through insulin, inflammation and altered androgen handling in fat tissue."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "It builds vessels to spread: prostate tumors drive VEGF-dependent angiogenesis to grow and seed bone, where the new vasculature supports the osteoblastic metastases that define advanced disease."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB helps it shake off hormone therapy: constitutive NF-κB signaling supports survival and androgen-receptor-independent growth, a route by which prostate cancer escapes castration into the lethal castration-resistant state."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The cancer and its hormone therapy both clot the blood: advanced prostate cancer is prothrombotic, and androgen-deprivation therapy further raises the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "It blocks the urinary tract and seeds infection: locally advanced prostate cancer obstructs the bladder outlet and ureters, and the resulting urinary stasis and instrumentation make urosepsis a real hazard."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Hormone therapy and marrow disease lower the count: androgen-deprivation therapy withdraws the testosterone that drives erythropoiesis, and bone-marrow metastases plus chronic inflammation add an anemia of chronic disease."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The pelvic tumor can throttle the kidneys: locally advanced prostate cancer obstructs the ureters and bladder outlet, and the resulting obstructive uropathy can progress to chronic kidney disease if unrelieved."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Androgen deprivation skews metabolism: ADT causes weight gain, fat redistribution and insulin resistance, raising the risk of type 2 diabetes and the metabolic syndrome over the years men spend on it."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Androgen deprivation strains the heart: the metabolic syndrome and direct vascular effects of ADT raise cardiovascular risk, and the resulting coronary disease and cardiac stress can progress to heart failure."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Bone metastases press on nerves: prostate cancer spreads avidly to the spine, where vertebral deposits and epidural cord or nerve-root compression produce severe neuropathic pain and neurological emergency."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Diagnosis and hormone therapy weigh on mood: the cancer itself plus the fatigue, loss of libido and brain effects of androgen-deprivation therapy contribute to substantial depression in treated men."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its mainstay treatment is endocrine: androgen-deprivation therapy chemically or surgically castrates men, causing hypogonadism with hot flushes, gynaecomastia, metabolic syndrome and bone loss."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It sits astride the urinary outflow: prostate cancer obstructs the bladder outlet and can invade the ureters or trigones, causing retention and hydronephrosis, while prostatectomy risks lasting incontinence."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "PSA surveillance breeds chronic worry: the repeated PSA checks, active-surveillance uncertainty and fear of recurrence in prostate cancer foster persistent health anxiety alongside depression."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It loves to spread to bone: prostate cancer produces characteristic osteoblastic metastases, especially in the spine and pelvis, causing bone pain and pathological fractures."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Spinal metastases can crush the cord: vertebral deposits from prostate cancer cause malignant spinal cord compression, an oncological emergency presenting with back pain, weakness and incontinence."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Hormone therapy strains the heart: androgen-deprivation therapy raises cardiovascular risk and metabolic syndrome, increasing myocardial infarction and stroke during long-term treatment."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It has its own cellular vaccine: the autologous immunotherapy sipuleucel-T is approved for prostate cancer, and the rare mismatch-repair-deficient tumours may respond to checkpoint inhibitors."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Pelvic radiotherapy inflames the rectum: radiation for prostate cancer causes radiation proctitis with rectal bleeding and urgency, and locally advanced disease can obstruct the bowel."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Advanced disease reaches the lungs: pulmonary metastases occur in advanced prostate cancer, and androgen-deprivation-related deconditioning reduces respiratory reserve."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Hormonal and precision drugs lead its care: androgen-deprivation and AR inhibitors (enzalutamide, abiraterone), PARP inhibitors for BRCA-mutant disease and Lu-177-PSMA radioligand therapy treat advanced prostate cancer."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Treatment shows on the skin: androgen-deprivation therapy causes hot flushes and gynaecomastia, and rare cutaneous metastases mark advanced prostate cancer."
  - target: 03-medicine/03-food/sulforaphane
    relation: connects-to
    note: "Diet draws chemoprevention interest: cruciferous-vegetable sulforaphane is studied for slowing prostate cancer, part of the dietary research around this hormone-driven tumour."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Taxanes for castration-resistant disease: docetaxel and cabazitaxel chemotherapy prolong survival in metastatic prostate cancer once it escapes hormonal control, used alongside androgen-pathway inhibitors."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It seeds the skeleton with dense bone: prostate cancer characteristically makes osteoblastic (sclerotic) bone metastases driving pain and fractures, treated with radium-223, denosumab and bisphosphonates targeting the bone."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "A largely cold tumour: most prostate cancers respond poorly to PD-1 checkpoint blockade owing to low mutational burden and sparse T-cell infiltrate, with benefit limited to the rare MSI-high or dMMR tumours."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Shared BRCA vulnerability: BRCA2-mutant prostate cancer, like high-grade serous ovarian cancer, carries homologous-recombination deficiency and responds to PARP inhibitors, placing both in the HBOC spectrum."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "It can transform to a small-cell cancer: under androgen-receptor blockade, prostate cancer can switch to treatment-emergent neuroendocrine/small-cell carcinoma with RB1 and p53 loss, resembling and treated like small-cell lung cancer."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Its hormone therapy hits the arteries: androgen-deprivation therapy accelerates metabolic syndrome and atherosclerosis of the arterial wall, making cardiovascular disease a leading cause of death in treated prostate cancer."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver spread marks aggressive disease: visceral metastasis to the hepatic lobules, uncommon in indolent prostate cancer, signals aggressive or neuroendocrine castration-resistant disease with a poor prognosis."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "A shared BRCA2 risk: germline BRCA2 mutations raise the risk of aggressive prostate cancer alongside breast, ovarian, pancreatic cancer and melanoma, defining a hereditary cancer spectrum that guides screening."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "A textbook cause of cancer DIC: metastatic prostate cancer is a classic trigger of chronic disseminated intravascular coagulation, its tumour procoagulants driving simultaneous clotting and bleeding."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "RB1 and lethal transformation: loss of RB1, the retinoblastoma gene, drives treatment-emergent neuroendocrine (small-cell) prostate cancer, an aggressive androgen-independent transformation under therapy pressure."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The cardiovascular cost of ADT: androgen-deprivation therapy induces metabolic syndrome and accelerates atherosclerosis, so cardiovascular disease is a leading cause of non-cancer death in prostate cancer survivors."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Metastatic cord compression: prostate cancer's bone-tropic spinal metastases can collapse vertebrae and compress the spinal cord and nerve roots, an oncologic emergency threatening permanent paralysis."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes and helps drive the lethal neuroendocrine transdifferentiation of castration-resistant prostate cancer."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: cyclin D1-CDK4/6 activity pushes prostate cancer cells through the G1 checkpoint, cooperating with androgen-receptor signalling to fuel proliferation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in poorly oxygenated prostate tumours promotes angiogenesis, glycolysis and resistance to radiotherapy and androgen deprivation."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Osteoblastic bone metastasis: prostate cancer cells secrete endothelin-1 that stimulates osteoblasts, driving the dense sclerotic bone metastases that distinguish it from most other cancers' lytic lesions."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase immortalisation: TERT reactivation maintains telomeres in prostate cancer cells, granting the unlimited replicative capacity that underlies progression to castration-resistant disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage homing: CCL2 secreted by prostate tumours recruits tumour-associated macrophages and supports metastatic seeding of bone, where it amplifies osteoclast activity and tumour growth."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Osteotropic homing: CXCR4 on prostate-cancer cells follows CXCL12 gradients to the bone marrow, a key mechanism behind the bone-dominant metastatic pattern that defines advanced prostate cancer."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "HR repair and PARP: prostate cancers with BRCA/ATM mutations are homologous-recombination deficient, engaging RAD51-mediated repair whose loss confers synthetic-lethal sensitivity to PARP inhibitors like olaparib."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-axis driver: IGF-1 signalling promotes prostate epithelial proliferation and survival, and higher circulating IGF-1 is associated with prostate-cancer risk and progression independent of androgens."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Resistance bypass: upregulation of the glucocorticoid receptor lets prostate-cancer cells drive an AR-like transcriptional programme despite AR blockade, a key mechanism of resistance to enzalutamide in castration-resistant disease."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Neuroendocrine transition: under potent AR-pathway inhibition some prostate cancers transdifferentiate into aggressive neuroendocrine tumours that lose AR and express neuroendocrine markers like SSTR2, a lethal, treatment-induced phenotype switch."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "HRD immunogenicity: BRCA/ATM-mutant, homologous-recombination-deficient prostate cancers accumulate cytosolic DNA that activates cGAS-STING, the innate-immune rationale for combining PARP inhibitors with checkpoint blockade in this molecular subset."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AR crosstalk: PTEN loss (already mapped) and PIK3CA activation drive the PI3K-AKT-mTOR pathway in prostate cancer, a resistance route that reciprocally cross-talks with androgen-receptor signalling to sustain castration-resistant growth."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Castration-resistant progression: Wnt/β-catenin signalling drives castration-resistant progression and contributes to the osteoblastic bone metastases (RANKL and osteoblasts already mapped) that characterise advanced prostate cancer."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Metastatic switch: TGF-β shifts from tumour suppressor to driver as prostate cancer advances, promoting epithelial-mesenchymal transition, the bone-metastatic niche and the immunosuppression of the tumour microenvironment."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK and castration resistance: TMPRSS2-ERG and RAS-MAPK signalling cooperate with the androgen receptor to drive prostate-cancer proliferation, and MAPK reactivation underlies progression to castration-resistant disease."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Lineage plasticity: the cyclin-D1-RB-E2F axis (cyclin-D1 mapped) drives proliferation, and RB loss releasing E2F1 promotes the lineage plasticity that yields treatment-emergent neuroendocrine prostate cancer."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 inactivation: MDM2-mediated suppression and outright TP53 loss (p53 mapped) mark the aggressive, often neuroendocrine castration-resistant prostate cancer."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signalling promotes androgen-receptor reactivation and neuroendocrine differentiation in castration-resistant prostate cancer."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Loss of TGF-β-SMAD4 signalling (TGF-β mapped) is a key metastasis-suppressor lesion whose inactivation drives aggressive, bone-metastatic prostate cancer."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A (p16) loss releases CDK4/6-cyclin-D control (cyclin-D1 mapped) of the cell cycle, a recurrent lesion in lethal prostate cancer."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports immune evasion and the bone-metastatic colonisation that drives mortality in advanced prostate cancer."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling supports androgen-independent growth and contributes to the castration resistance of advanced prostate cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of the immunologically cold prostate cancer, relevant to its limited immunotherapy responsiveness."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PTEN-loss-driven PI3K-AKT signaling (PTEN, AKT, and PIK3CA already mapped) inactivates FOXO, removing a tumor-suppressive brake in prostate cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 acting on the cyclin-D1-RB axis (cyclin-D1 already mapped) drives the cell-cycle progression of prostate cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunologically cold prostate cancer evades."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates AR and β-catenin stability (androgen receptor and Wnt already mapped), modulating the survival signaling of prostate cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the immunosuppressive, bone-metastatic microenvironment of prostate cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling contributes to the castration-resistant progression and bone-metastatic tropism of prostate cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of prostate cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and androgen-deprivation-therapy resistance of prostate cancer cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of prostate cancer."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment and bone-metastatic niche of prostate cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape and androgen-receptor cooperativity of prostate cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment and bone-metastatic progression of prostate cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of prostate cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of prostate cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of prostate cancer."
  - target: 01-human/03-molecular/dll3
    relation: connects-to
    note: "Neuroendocrine transformation: androgen-receptor-directed therapy can drive lineage plasticity to aggressive treatment-emergent neuroendocrine prostate cancer, which expresses DLL3, the target of DLL3-directed agents beyond hormonal treatment."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Castration resistance: AXL receptor tyrosine kinase signalling promotes the epithelial-mesenchymal transition and therapy tolerance underlying progression to castration-resistant, metastatic prostate cancer despite androgen-receptor blockade."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune-cold tumour: prostate cancer generally presents few neoantigens and low MHC class II-driven antigen presentation, the basis of its poor checkpoint response, with exceptions in the MSI and CDK12-altered subsets and the sipuleucel-T vaccine."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Sipuleucel-T vaccine: IL-2-driven T-cell responses underlie sipuleucel-T, the autologous cellular immunotherapy that improves survival in castration-resistant prostate cancer (MHC and PD-1 already mapped) despite this tumour's poor response to checkpoint blockade."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: prostate cancer lowers haemoglobin through marrow replacement by bone metastases (RANKL already mapped), androgen-deprivation therapy and chemotherapy, and the resulting anaemia contributes to fatigue in advanced disease."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Androgen-deprivation cardiotoxicity: long-term androgen-deprivation therapy raises cardiovascular risk through adverse metabolic changes, and troponin elevation marks the myocardial injury of the cardiac events that complicate this mainstay treatment."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Radioligand and proton therapy: prostate cancer is treated with proton-beam radiotherapy and, in metastatic disease, the beta-emitting Lu-177-PSMA radioligand that targets the prostate-specific membrane antigen, delivering radiation to the tumour."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive cold tumour: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), part of the immune evasion that makes most prostate cancer a checkpoint-resistant 'cold' tumour."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: oxidative stress, to which xanthine oxidase contributes, and its reactive oxygen species contribute to prostate carcinogenesis and progression (NRF2-adjacent redox biology), part of the tumour's oxidative dimension."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, checkpoint-resistant immune microenvironment of most prostate cancer."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia of therapy: androgen-deprivation therapy and metastatic marrow involvement cause anaemia (haemoglobin already mapped) in prostate cancer, and the transfusional support can load the body with iron."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 and inflammation: prostaglandins from cyclooxygenase-2 in the inflamed prostate contribute to carcinogenesis and progression (IL-6 already mapped), part of the chronic-inflammation link in prostate cancer."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive 'cold' microenvironment of prostate cancer."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and aggressiveness: the adipokine leptin links obesity — a risk factor for aggressive and lethal prostate cancer — to the proliferation and progression of the tumour."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine axis: adiponectin, with leptin (already mapped), links the obesity and metabolic state to the risk and aggressiveness of prostate cancer, part of the adipokine influence on the tumour."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity risk of the aggressive prostate cancer."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the M2 (IL-4 and IL-13 already mapped) tumour-associated macrophages (CCL2 already mapped) of the immunosuppressive 'cold' microenvironment of prostate cancer."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Reactive stroma: the cancer-associated fibroblasts of the reactive prostate-cancer stroma (TGF-β already mapped) support the tumour progression and the androgen (androgen-receptor already mapped) signalling."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the (sparse) tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm largely excluded by the immunosuppressive 'cold' microenvironment of prostate cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response explored against the immunologically cold prostate cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance of the prostate cancer, an arm explored to overcome its immunosuppressive microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immunosuppressive microenvironment of prostate cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of prostate cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immunologically cold prostate-cancer microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of prostate cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures within the immunologically cold prostate-cancer microenvironment, a candidate correlate of the immunotherapy response."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the tumour-promoting inflammation of prostate cancer."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory and immunosuppressive dimension of the immunologically cold prostate-cancer microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid (macrophage already mapped) recruitment and immunosuppression of the prostate-cancer microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the prostate-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the microenvironment."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Tumour-stromal alarmin: TSLP, secreted by cancer-associated fibroblasts (already mapped) and bone-marrow (already mapped) stroma, activates mast cells (already mapped) and dendritic cells (already mapped), promoting the immunosuppressive microenvironment of prostate cancer."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-growth axis: bradykinin, generated via the kallikrein-kinin system in the tumour microenvironment, signals via B2 receptors on cancer cells and endothelial cells (already mapped) to promote proliferation and angiogenesis (VEGF already mapped) of prostate cancer."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anemia correction: erythropoietin addresses the anemia of chronic disease (already mapped) and the myelosuppression from chemotherapy (already mapped), supporting haematopoiesis and quality of life in advanced prostate cancer."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell TME effector: histamine, released by mast cells (already mapped) in the tumour microenvironment of prostate cancer, promotes angiogenesis (VEGF already mapped), immunosuppression and androgen-receptor (already mapped) signalling crosstalk of prostate cancer."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Bone metastasis ECM scaffold: periostin, highly expressed in the bone microenvironment, promotes osteoblastic (already mapped) and mixed prostate cancer bone metastasis by facilitating tumour cell adhesion and the fibrotic remodelling of bone lesions."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3 and C5 already mapped) and contact-kinin (bradykinin already mapped) activation in the tumour microenvironment, moderating complement-driven immunosuppression of prostate cancer."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "PC serotonin: serotonin, via 5-HT receptors on prostate cancer cells and macrophages (already mapped), promotes tumour proliferation and the immunosuppressive tumour microenvironment; 5-HT also modulates the androgen-receptor (already mapped) signalling axis of prostate cancer."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "PC melatonin: melatonin, via MT1/MT2 receptors, attenuates androgen-receptor (already mapped) signalling and tumour proliferation in prostate cancer; melatonin also suppresses osteoblast (already mapped) RANKL (already mapped) bone-metastatic niche formation."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "PC prolactin: prolactin, via PRLR on prostate cancer cells, activates mTOR (already mapped) and promotes tumour survival; prolactin also modulates macrophage (already mapped) polarisation and androgen-receptor (already mapped) signalling crosstalk in prostate cancer."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PC oxytocin: oxytocin, via OXTR on prostate cancer cells and macrophages (already mapped), attenuates NF-κB (already mapped) tumour inflammation and androgen-receptor (already mapped) signalling; oxytocin modulates the immunosuppressive tumour microenvironment of prostate cancer."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PC vasopressin: vasopressin V1 receptors on prostate cancer cells promote the NF-κB (already mapped) driven tumour proliferation and vascular remodelling; V2-receptor activation amplifies androgen-receptor (already mapped) signalling and tumour invasion in prostate cancer."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PC iodine: iodine-dependent thyroid hormones regulate prostate cancer cell proliferation and androgen-receptor (already mapped) sensitivity; thyroid-hormone deficiency amplifies the NF-κB (already mapped) tumour growth and mTOR (already mapped) driven metastatic progression."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "PC sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the mTOR (already mapped) and androgen-receptor (already mapped) tumour cascade of prostate cancer."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "PC magnesium: magnesium, as mTOR (already mapped) kinase cofactor in prostate cells and macrophages (already mapped), restrains tumour growth; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of prostate cancer."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "PC copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped) and osteoblasts (already mapped), drives ECM remodelling and bone metastasis; copper deficiency amplifies the NF-κB (already mapped) and VEGF (already mapped) angiogenic cascade of prostate cancer."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "PC potassium: potassium channels in macrophages (already mapped) and prostate tumour cells regulate NLRP3 inflammasome; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade supporting mTOR (already mapped) tumour growth in prostate cancer."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "PC chloride: chloride channels in macrophages (already mapped) and fibroblasts (already mapped) modulate tumour-stromal ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of prostate cancer."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "PC carbon: carbon as backbone of androgen receptor and NF-κB (already mapped) proteins in prostate tumour cells and macrophages (already mapped) sustains oncogenic signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of prostate cancer."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "PC hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and fibroblasts (already mapped), supports androgen receptor signalling; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of prostate cancer."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "PC nitrogen: nitrogen in amino-acid scaffold of androgen receptor and VEGF (already mapped) proteins in prostate tumour cells sustains oncogenic signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of prostate cancer."
---

# Prostate Cancer

## Overview

**Prostate cancer (PCa)** is the most common non-skin cancer and the **second leading cause of cancer death** in men in Western countries (after lung cancer), with ~300,000 new cases and ~35,000 deaths annually in the United States. The disease spans a wide spectrum from indolent, low-grade tumors managed by active surveillance to lethal metastatic castration-resistant prostate cancer (mCRPC) with median survival of 3-5 years despite modern therapies [^beer-2014-prevail].

**Incidence and risk factors:**
- **Age:** Primary risk factor; median age at diagnosis ~66 years; rare before 40
- **Family history:** 2× risk with first-degree relative; 4-6× with BRCA2 mutation carriers (also higher Gleason grade and younger age)
- **Race:** African American men have 1.7× higher incidence and 2× higher mortality vs. white men; Asian-American men have lower rates; mechanisms involve genetic ancestry (HOXB13, BRCA2 variant frequencies), healthcare access, and potentially diet/exposures
- **BRCA2 germline:** ~5-8% of high-grade or metastatic PCa; BRCA2 mutation carriers more likely to present with metastatic or high-grade disease; germline testing now recommended for all metastatic and high-grade localized PCa
- **Geographic variation:** Rates highest in North America/Northern Europe, lowest in Asia; dietary fat, dairy, and red meat associated with increased risk in epidemiological studies; finasteride and dutasteride (5α-reductase inhibitors) reduce low-grade PCa but do not reduce high-grade cancer (possible detection bias)

**Molecular subtypes:**
- **ERG-positive (~50%):** TMPRSS2-ERG fusion → ETS factor ERG overexpressed; ERG drives invasion, EMT, and androgen-independent transcription; ERG fusions are an early and defining molecular event in ~50% of PCa
- **ETV1/4/5-positive (~10%):** Other ETS fusions; similar to ERG; less common
- **SPINK1-positive (~10%):** SPINK1 (serine peptidase inhibitor Kazal type 1) overexpression without ETS fusion; distinct biology; higher grade association
- **CDK12-mutant (~5% of mCRPC):** CDK12 loss → defective DNA damage repair → tandem duplications → high focal amplifications → high neoantigen burden → immunotherapy-responsive phenotype distinct from MSI-H
- **FOXA1-mutant (~10%):** FOXA1 is an AR pioneer factor; mutations alter AR cistrome (chromatin binding landscape) → altered transcriptional program; distinct from ERG-positive tumors
- **MSI-H/MMR-deficient (~5% of mCRPC):** Pembrolizumab-eligible (tissue-agnostic FDA approval); Lynch syndrome rare in PCa
- **Neuroendocrine prostate cancer (NEPC, ~10-20% of treatment-refractory mCRPC):** AR-low/negative, NE differentiation markers (synaptophysin, chromogranin, NSE), RB1 loss + TP53 loss + PTEN loss; driven by treatment selective pressure (enzalutamide/abiraterone → lineage plasticity); no approved targeted therapy; platinum-based chemotherapy + etoposide used empirically; very poor prognosis

## Structure

### Prostate anatomy and zones

**Prostate gland anatomy:**
- Walnut-sized gland (~20-30 g in young adult men) at the bladder neck; surrounds the proximal urethra; lies anterior to the rectum (DRE access)
- **McNeal zones:**
  - **Peripheral zone (PZ, ~70% of gland):** Most prostate cancers arise here (70%); palpable on DRE; immediately adjacent to the rectum; where post-biopsy bleeding and infection risk are highest
  - **Transitional zone (TZ, ~25%):** Site of benign prostatic hyperplasia (BPH); ~25% of cancers arise here; lower grade on average; less likely to be ERG-positive
  - **Central zone (CZ, ~5%):** Surrounds ejaculatory ducts; relatively cancer-resistant; when central zone cancer occurs, often aggressive
  - **Anterior fibromuscular stroma:** No glandular tissue; structural component

**Histology:**
- Prostate epithelium has two cell layers: **luminal secretory cells** (AR-high, PSA-producing) and **basal cells** (AR-low, p63/CK5/14-positive, stem-cell-like); PCa arises from luminal cells (or a luminal-like progenitor)
- **Prostatic intraepithelial neoplasia (PIN):** High-grade PIN (HGPIN) is the precursor to PCa; architectural and cytological atypia; ERG-positive HGPIN adjacent to ERG-positive PCa → shared clonal origin

### Gleason grading and Grade Groups

**Gleason grading (2014 ISUP revised):**
- Based on glandular architecture (not nuclear atypia): Gleason patterns 1-5 (1=well-formed glands, 5=no glandular differentiation)
- **Gleason score (GS):** Primary pattern + secondary pattern (most common + second most common): GS 6 (3+3) = low grade; GS 7 (3+4 or 4+3) = intermediate; GS 8-10 = high grade
- **Grade Groups (ISUP 2016):** GG1 (GS 6), GG2 (GS 3+4=7), GG3 (GS 4+3=7), GG4 (GS 8), GG5 (GS 9-10) — simplified grading that better predicts prognosis and guides treatment intensity

**Gleason pattern 4 significance:**
- Gleason pattern 4 (poorly formed, fused, or cribriform glands) is the key dividing line between favorable and unfavorable disease
- **Cribriform pattern 4 and intraductal carcinoma (IDC):** Both associated with adverse pathology, genomic instability, and worse prognosis independent of overall GS; ISUP recommends noting their presence specifically

## Function

### Clinical presentation and staging

**Screening and PSA:**
- **Prostate-specific antigen (PSA):** Serine protease (KLK3) secreted into semen; normally low in blood (<4 ng/mL); elevated in PCa, BPH, prostatitis; PSA density (PSA/prostate volume), PSA velocity, and free/total PSA ratio improve specificity
- **PSA screening controversy:** PLCO and ERSPC trials showed PSA screening reduces PCa-specific mortality (~20-30% reduction) but over-diagnoses low-grade cancer with associated over-treatment harms (incontinence, impotence); current guideline: shared decision-making for men 50-69; USPSTF Grade C recommendation for 55-69; early testing at 40-45 for high-risk (Black men, BRCA2)
- **MRI and mpMRI-targeted biopsy:** Multiparametric MRI (T2, DWI, DCE) before biopsy → PI-RADS 1-5 classification; PRECISION trial: MRI-targeted biopsy detected more clinically significant PCa (Grade Group ≥2) and fewer Grade Group 1 (over-diagnosis reduction) vs. systematic biopsy

**Clinical staging:**
- **T1:** Clinically inapparent (found incidentally or via biopsy only)
- **T2:** Palpable/visible, confined to prostate
- **T3:** Extraprostatic extension (T3a) or seminal vesicle invasion (T3b)
- **T4:** Invasion of adjacent structures (bladder, rectum, levator muscle)
- **N:** Regional lymph node metastasis
- **M:** Distant metastasis (M1a: non-regional lymph node; M1b: bone — >85% of metastases; M1c: visceral)

**PSMA PET imaging:**
- **PSMA (prostate-specific membrane antigen):** Folate hydrolase enzyme overexpressed on PCa cell membranes; targeted by PSMA-617 (lutetium-177 radioligand) and PSMA PET ligands (Ga-68-PSMA-11, F-18-DCFPyL/piflufolastat)
- PSMA PET (ProPSMA trial): Superior to conventional imaging (CT+bone scan) for primary staging (AUC 0.85 vs. 0.38); detects metastases earlier; changed management in 28% of patients; now standard for high-risk localized and biochemically recurrent PCa

## Pathology

### Diagnosis and risk stratification

**Biopsy:** Transrectal or transperineal ultrasound-guided biopsy (12-core systematic ± MRI-targeted cores); transperineal approach has lower infectious risk (no rectal contamination); becoming preferred with antibiotic stewardship concerns.

**Risk stratification (NCCN criteria for localized PCa):**
- **Very low risk:** cT1c, GS ≤6 (GG1), PSA <10, <3 positive cores, ≤50% cancer per core, PSA density <0.15
- **Low risk:** cT1-T2a, GS ≤6, PSA <10
- **Favorable intermediate:** cT2b-T2c or GS 3+4=7 (GG2) or PSA 10-20; <50% positive cores
- **Unfavorable intermediate:** GS 4+3=7 (GG3) or ≥50% positive cores
- **High risk:** cT3a or GS 8-10 (GG4-5) or PSA >20
- **Very high risk:** cT3b-T4, primary Gleason 5, or >4 cores GG4-5

**Genomic classifiers:**
- **Oncotype DX GPS (17-gene):** Predicts 10-year PCa-specific mortality; validated in TURP-based series; used for active surveillance vs. treatment decision in low-intermediate risk disease
- **Decipher (22-gene):** Predicts metastasis risk after radical prostatectomy; validated in multiple post-prostatectomy series; helps guide adjuvant vs. salvage RT decision

### Treatment

**Active surveillance:**
- Very low and low-risk, and selected favorable intermediate-risk PCa; PSA every 6-12 months, DRE annually, repeat biopsy at 1-2 years, PSMA PET or MRI for monitoring; 10-year PCa-specific survival >99%; avoids treatment side effects; PROTECT trial: no OS difference between active monitoring, RP, and RT at 10 years for low/intermediate risk

**Radical prostatectomy (RP) and radiation therapy (RT):**
- **RP (robotic-assisted RARP preferred):** Gold standard for localized high-risk disease and young patients; pathological staging from specimen; positive margin → salvage RT; nerve-sparing for potency preservation
- **External beam RT (EBRT):** Intensity-modulated RT (IMRT) or stereotactic body RT (SBRT); equivalent to RP for localized disease (PROTECT); combined with ADT for intermediate/high-risk (EORTC 22991, DART 01/05)
- **Brachytherapy (LDR/HDR):** Low-dose rate (Pd-103, I-125 seeds) or high-dose rate (Ir-192); used in low/favorable intermediate risk or as boost; excellent local control rates

**Hormone-sensitive metastatic PCa (mCSPC):**
- ADT backbone (GnRH agonist: leuprolide, goserelin; or GnRH antagonist: degarelix, relugolix)
- **Intensification beyond ADT (all high-volume or unfavorable risk disease):**
  - Docetaxel + ADT (CHAARTED, STAMPEDE): OS benefit; particularly for high-volume (≥4 bone metastases ± visceral) disease
  - Abiraterone + ADT (LATITUDE, STAMPEDE): OS benefit in high-risk disease; prednisone co-administered
  - Enzalutamide + ADT (ARCHES, ENZAMET): OS benefit
  - Apalutamide + ADT (TITAN): OS benefit
  - Darolutamide + ADT + docetaxel (ARASENS): OS benefit in triplet
  - **Preferred for most patients:** Doublet (ADT + novel AR agent); triplet for highly selected fit patients with high-volume disease

**Castration-resistant prostate cancer (mCRPC):**
- **Definition:** PCa progressing (PSA, radiographic, or clinical) despite castrate testosterone levels (<50 ng/dL)
- **Second-generation AR-pathway agents:** Enzalutamide (PREVAIL), abiraterone (COU-AA-302) for mCRPC post-ADT [^beer-2014-prevail]
- **Docetaxel + prednisone:** Standard chemotherapy; AFFIRM, TAX327 trials; cabazitaxel for post-docetaxel
- **PARP inhibitors for HRR-deficient mCRPC [^de-bono-2020-profound]:**
  - **Olaparib (PROfound):** BRCA1/2 and ATM mutations; FDA approved 2020; rPFS and OS benefit
  - **Rucaparib (TRITON2):** BRCA1/2 mutations; FDA approved 2020
  - **Niraparib + abiraterone (MAGNITUDE):** HRR-deficient mCRPC; FDA approved 2023
  - **Talazoparib + enzalutamide (TALAPRO-2):** HRR-deficient; FDA approved 2023
  - All patients with mCRPC should receive germline genetic testing; somatic HRR testing on tissue/liquid biopsy
- **Lutetium-177-PSMA-617 (VISION trial) [^sartor-2021-vision]:** PSMA-positive mCRPC post-AR-agent + taxane; rPFS improved from 3.4 → 8.7 months; OS 15.3 vs. 11.3 months; FDA approved 2022; PSMA PET required to confirm PSMA-avid disease before treatment
- **Immunotherapy:** Sipuleucel-T (autologous DC vaccine) modest OS benefit; pembrolizumab for MSI-H/TMB-H; pembrolizumab for MMR-deficient PCa
- **Ra-223 dichloride (ALSYMPCA):** Bone-only mCRPC; alpha emitter targets bone metastases; OS benefit; no visceral metastases; combined with AR-axis agents under study

**Bone metastasis management:**
- Denosumab (RANKL inhibitor) or zoledronic acid: Reduce skeletal-related events (SREs) in mCRPC with bone metastases; preferred: denosumab for fracture prevention
- Bone-seeking radiopharmaceuticals: Ra-223; lutetium-177-PSMA also targets bone mets

## Connections

- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — AR is the primary driver of prostate cancer; ADT is foundational; resistance via AR amplification, AR-V7 splice variant, and LBD mutations drives CRPC; enzalutamide, apalutamide, and darolutamide extend survival in mCSPC and mCRPC.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss occurs in ~50% of localized and ~70% of mCRPC; PTEN null → AKT-AR crosstalk → poor prognosis; PTEN-null tumors have higher Gleason grade; ipatasertib + abiraterone (IPATential150) improves rPFS in PTEN-null mCRPC.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1/2 and ATM mutations occur in ~25% of mCRPC (germline + somatic); HRR deficiency → PARP inhibitor sensitivity; olaparib (PROfound) and rucaparib (TRITON2) approved for BRCA-mutant mCRPC; germline testing recommended for all mCRPC patients.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR is activated downstream of PTEN loss in prostate cancer; mTOR inhibitors showed modest activity alone; combinations with AR-pathway inhibitors under study; TORC1/2 dual inhibitors with enzalutamide in trials for PTEN-null CRPC.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Testosterone fuels AR-driven prostate cancer; ADT (GnRH agonists/antagonists) is first-line for advanced disease; castration resistance arises via AR amplification, AR-V7, and adrenal androgen synthesis; abiraterone (CYP17A1 inhibitor) blocks residual androgens in CRPC.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The prostate is a male reproductive accessory gland encircling the urethra; ~70% of cancers arise in its peripheral zone (palpable on DRE) while benign hyperplasia crowds the transitional zone; localized disease may be watched, irradiated, or removed by radical prostatectomy.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — BRCA2 is the most important inherited prostate-cancer gene: germline BRCA2 raises risk 4-6× and predicts higher Gleason grade, and BRCA2/HRR deficiency makes tumors PARP-inhibitor-sensitive (olaparib PROfound); germline testing is recommended for all metastatic disease.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Over 85% of prostate-cancer metastases go to bone, where tumor cells drive osteoblasts to overproduce RANKL → osteoclast activation → a vicious cycle of bone destruction and growth-factor release; the anti-RANKL antibody denosumab reduces skeletal-related events.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Prostate and colorectal cancers are two of the commonest adult solid tumours, both rising with age and Western diet; both have hereditary forms—BRCA2 raises lethal prostate cancer, Lynch raises both—and PARP and checkpoint therapy now target their DNA-repair-deficient subsets.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Prostate cancer characteristically forms osteoblastic (bone-forming) metastases: tumour-secreted Wnt, ET-1 and BMPs drive osteoblasts to lay down disorganized woven bone, while RANKL fuels a vicious turnover cycle; this pattern underlies bone-targeted radium-223 and denosumab.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Prostate and breast cancers are the paradigm hormone-driven adenocarcinomas—androgen- vs estrogen-receptor signalling—each treated by depriving that hormone; they also share BRCA1/2 predisposition, so PARP inhibitors (olaparib) work in both, and both seed bone metastases.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is a curative mainstay for localized prostate cancer: external-beam photon radiation and brachytherapy (radioactive seeds) rival surgery for cure, while in metastatic disease the radioligand Lu-177-PSMA delivers radiation to PSMA-expressing tumor cells.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Lynch syndrome modestly raises prostate cancer risk: mismatch-repair-deficient prostate cancers are part of the Lynch spectrum, and like other MSI-high tumors can respond to checkpoint blockade, so a strong family cancer history warrants germline MMR testing.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Prostate cancer hosts the first FDA-approved cancer vaccine, a dendritic-cell therapy: sipuleucel-T harvests a patient's antigen-presenting cells, primes them against prostatic acid phosphatase, and reinfuses them to spark a T-cell response against the tumor.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — Prostate cancer is part of the BRCA/HBOC cancer spectrum: germline BRCA2 (and BRCA1) mutations raise prostate cancer risk and aggressiveness, and BRCA-mutant tumors respond to PARP inhibitors—so HBOC families need prostate screening.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Prostate and pancreatic cancer share BRCA2-linked DNA-repair predisposition: families with BRCA2 mutations face raised risk of both, and both respond to platinum and PARP-inhibitor therapy—two distant organs linked by one gene.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Prostate and bladder cancer are the two commonest urologic malignancies but differ: prostate cancer arises from androgen-driven glandular epithelium, while bladder cancer is a smoking-linked urothelial tumor—both present with urinary symptoms, so evaluation overlaps.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC amplification is an early prostate cancer driver: MYC gains, often with PTEN loss and ERG fusions, push the malignant transformation and predict aggressive disease—so the same proliferation oncogene seen across cancers helps grade prostate tumor biology.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Prostate cancer's bone metastases hijack osteoclasts: though the lesions look bone-forming (osteoblastic), tumor RANKL still activates osteoclasts, fueling a vicious cycle of bone turnover—so denosumab and bisphosphonates that block osteoclasts reduce skeletal events.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Prostate cancer floods the bone marrow: it spreads preferentially to the axial-skeleton marrow, where deposits cause pain, fractures and marrow failure with anemia, so bone is the dominant metastatic site that drives the morbidity of advanced disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Liver metastasis marks aggressive prostate cancer: though bone is the usual target, spread to the liver (and other viscera) signals a more lethal, often treatment-resistant or neuroendocrine phenotype—so visceral metastases carry worse prognosis than bone-only disease.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Prostate cancer can also seed the lung: less common than bone metastasis, pulmonary spread reflects hematogenous dissemination of advanced disease, so chest imaging in progressive castration-resistant cancer can reveal visceral metastases that change treatment.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Prostate cancer is an immunologically 'cold' tumor: it has few mutations and poor T-cell infiltration, so checkpoint inhibitors largely fail, and sipuleucel-T—a vaccine priming cytotoxic T cells against prostate antigen—remains one of the few working immunotherapies.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — Prostate cancer with ATM or BRCA defects is PARP-sensitive: like BRCA, ATM loss impairs DNA repair, marking metastatic tumors that respond to PARP inhibitors—so guideline testing of homologous-recombination genes now guides therapy.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Prostate cancer can escape hormone therapy by turning neuroendocrine: under prolonged androgen blockade, some tumors transdifferentiate into aggressive, AR-independent neuroendocrine prostate cancer—a treatment-emergent resistance resembling small-cell cancer.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Prostate cancer makes bone in its metastases: unusually, its bone deposits are osteoblastic (bone-forming) rather than lytic, and the calcium-seeking alpha-emitter radium-223 homes to these lesions to deliver targeted radiation and prolong life.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Prostate cancer leans on the PTEN-AKT pathway: PTEN loss is one of its commonest events, switching on AKT survival signaling that cooperates with the androgen receptor—so AKT inhibitors are combined with hormone therapy in PTEN-deficient disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Prostate cancer is an immunologically cold tumor full of regulatory T cells: a Treg-rich, suppressive microenvironment is why checkpoint immunotherapy mostly fails here, leaving the dendritic-cell vaccine sipuleucel-T as the main immune option.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Prostate cancer is supported by tumor-associated macrophages: they promote its growth, angiogenesis, and especially its spread to bone, where they help build the niche for the osteoblastic metastases that define advanced disease.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — The prostate is the body's zinc capital, and cancer abandons it: healthy prostate cells hoard zinc to block citrate breakdown, but malignant cells lose this zinc accumulation to fuel their metabolism—a metabolic switch unique to prostate cancer.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Advanced prostate cancer can shut down the kidneys: the enlarging tumor or its pelvic lymph nodes compress the ureters and bladder outlet, backing urine up into the kidneys (hydronephrosis) and causing post-renal failure.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Prostate cancer recruits fibroblasts as accomplices: cancer-associated fibroblasts form the reactive stroma around tumor glands, secreting growth and remodeling signals that spur invasion—and the amount of reactive stroma predicts outcome.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Prostate cancer's bone metastases are unusually bone-forming: osteoblastic lesions lay down calcium-phosphate, so the invaded skeleton turns denser, not eaten away—the opposite of most cancers' bone disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Prostate cancer loves nerves: perineural invasion, tracking along nerve sheaths, is a hallmark route of spread out of the gland and a marker of aggressiveness read on the biopsy.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Even after castration the adrenal glands feed prostate cancer: they keep making androgens that fuel castration-resistant disease, which is why abiraterone blocks adrenal steroid synthesis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy unmasks prostate cancer's most lethal turn: when it transforms into a neuroendocrine cancer to escape hormone therapy, the cells fill with dense-core secretory granules — the ultrastructure that flags this treatment-resistant variant.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The treatment can wound the heart: androgen-deprivation therapy, the backbone of advanced prostate cancer care, raises the risk of metabolic syndrome, coronary disease, and cardiac events by stripping away protective testosterone.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Prostate cancer rarely reaches the brain, but when it does it signals trouble: the aggressive neuroendocrine and late castration-resistant forms can seed cerebral and dural metastases, a grave sign in end-stage disease.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Shutting off testosterone lowers the red cells: androgen deprivation therapy removes a hormone that drives erythropoiesis, so a mild anemia is a common, expected side effect of treating prostate cancer.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Androgen deprivation reshapes the body's fat: it drives weight gain, insulin resistance, and a sarcopenic obesity, the metabolic syndrome that raises cardiovascular and diabetic risk during long-term hormone therapy.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The rectum sits right behind the prostate: locally advanced tumors can invade it, and the radiotherapy aimed at the gland often inflames it into a radiation proctitis with bleeding and urgency.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies screen, image, and treat it: the PSA blood test is an antibody immunoassay, PSMA-targeted antibodies guide PET imaging and radioligand therapy, and sipuleucel-T harnesses the immune system against the tumor.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads first to the pelvic nodes: prostate cancer drains to the obturator and iliac lymph nodes, so nodal staging by imaging or dissection shapes treatment before the more distant bone metastases appear.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Chemotherapy for advanced disease taxes the marrow: the docetaxel and cabazitaxel given in castration-resistant prostate cancer are myelosuppressive, dropping neutrophil counts and raising the risk of febrile neutropenia.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Losing p53 turns prostate cancer lethal: TP53 mutation, often with RB loss, drives the shift to aggressive castration-resistant and neuroendocrine disease that escapes hormone therapy and carries a grim prognosis.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — The hormone therapy that controls it thins the bones: androgen-deprivation therapy strips the testosterone that maintains the male skeleton, accelerating bone loss and fractures, so patients need bone-density monitoring with calcium, vitamin D, and antiresorptive drugs.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium promised prostate protection but failed: the large SELECT trial found selenium supplements did not prevent prostate cancer (and vitamin E may have slightly raised risk), tempering the antioxidant chemoprevention hopes.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Most of it resists immunotherapy: prostate cancer is immunologically cold, so PD-1 blockade helps only the rare mismatch-repair-deficient, high-mutation tumors — a reminder that checkpoint drugs need a visible target to work.
- `connects-to` → **[Obesity](../obesity/README.md)** — Excess weight breeds the aggressive form: obesity is linked less to getting prostate cancer than to developing the high-grade, lethal disease, through insulin, inflammation and altered androgen handling in fat tissue.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — It builds vessels to spread: prostate tumors drive VEGF-dependent angiogenesis to grow and seed bone, where the new vasculature supports the osteoblastic metastases that define advanced disease.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB helps it shake off hormone therapy: constitutive NF-κB signaling supports survival and androgen-receptor-independent growth, a route by which prostate cancer escapes castration into the lethal castration-resistant state.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The cancer and its hormone therapy both clot the blood: advanced prostate cancer is prothrombotic, and androgen-deprivation therapy further raises the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — It blocks the urinary tract and seeds infection: locally advanced prostate cancer obstructs the bladder outlet and ureters, and the resulting urinary stasis and instrumentation make urosepsis a real hazard.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Hormone therapy and marrow disease lower the count: androgen-deprivation therapy withdraws the testosterone that drives erythropoiesis, and bone-marrow metastases plus chronic inflammation add an anemia of chronic disease.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The pelvic tumor can throttle the kidneys: locally advanced prostate cancer obstructs the ureters and bladder outlet, and the resulting obstructive uropathy can progress to chronic kidney disease if unrelieved.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Androgen deprivation skews metabolism: ADT causes weight gain, fat redistribution and insulin resistance, raising the risk of type 2 diabetes and the metabolic syndrome over the years men spend on it.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Androgen deprivation strains the heart: the metabolic syndrome and direct vascular effects of ADT raise cardiovascular risk, and the resulting coronary disease and cardiac stress can progress to heart failure.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Bone metastases press on nerves: prostate cancer spreads avidly to the spine, where vertebral deposits and epidural cord or nerve-root compression produce severe neuropathic pain and neurological emergency.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Diagnosis and hormone therapy weigh on mood: the cancer itself plus the fatigue, loss of libido and brain effects of androgen-deprivation therapy contribute to substantial depression in treated men.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its mainstay treatment is endocrine: androgen-deprivation therapy chemically or surgically castrates men, causing hypogonadism with hot flushes, gynaecomastia, metabolic syndrome and bone loss.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It sits astride the urinary outflow: prostate cancer obstructs the bladder outlet and can invade the ureters or trigones, causing retention and hydronephrosis, while prostatectomy risks lasting incontinence.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — PSA surveillance breeds chronic worry: the repeated PSA checks, active-surveillance uncertainty and fear of recurrence in prostate cancer foster persistent health anxiety alongside depression.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It loves to spread to bone: prostate cancer produces characteristic osteoblastic metastases, especially in the spine and pelvis, causing bone pain and pathological fractures.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Spinal metastases can crush the cord: vertebral deposits from prostate cancer cause malignant spinal cord compression, an oncological emergency presenting with back pain, weakness and incontinence.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Hormone therapy strains the heart: androgen-deprivation therapy raises cardiovascular risk and metabolic syndrome, increasing myocardial infarction and stroke during long-term treatment.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It has its own cellular vaccine: the autologous immunotherapy sipuleucel-T is approved for prostate cancer, and the rare mismatch-repair-deficient tumours may respond to checkpoint inhibitors.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Pelvic radiotherapy inflames the rectum: radiation for prostate cancer causes radiation proctitis with rectal bleeding and urgency, and locally advanced disease can obstruct the bowel.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Advanced disease reaches the lungs: pulmonary metastases occur in advanced prostate cancer, and androgen-deprivation-related deconditioning reduces respiratory reserve.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Hormonal and precision drugs lead its care: androgen-deprivation and AR inhibitors (enzalutamide, abiraterone), PARP inhibitors for BRCA-mutant disease and Lu-177-PSMA radioligand therapy treat advanced prostate cancer.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Treatment shows on the skin: androgen-deprivation therapy causes hot flushes and gynaecomastia, and rare cutaneous metastases mark advanced prostate cancer.
- `connects-to` → **[Sulforaphane](../../../03-medicine/03-food/sulforaphane/README.md)** — Diet draws chemoprevention interest: cruciferous-vegetable sulforaphane is studied for slowing prostate cancer, part of the dietary research around this hormone-driven tumour.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Taxanes for castration-resistant disease: docetaxel and cabazitaxel chemotherapy prolong survival in metastatic prostate cancer once it escapes hormonal control, used alongside androgen-pathway inhibitors.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It seeds the skeleton with dense bone: prostate cancer characteristically makes osteoblastic (sclerotic) bone metastases driving pain and fractures, treated with radium-223, denosumab and bisphosphonates targeting the bone.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — A largely cold tumour: most prostate cancers respond poorly to PD-1 checkpoint blockade owing to low mutational burden and sparse T-cell infiltrate, with benefit limited to the rare MSI-high or dMMR tumours.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Shared BRCA vulnerability: BRCA2-mutant prostate cancer, like high-grade serous ovarian cancer, carries homologous-recombination deficiency and responds to PARP inhibitors, placing both in the HBOC spectrum.
- `connects-to` → **[SCLC](../sclc/README.md)** — It can transform to a small-cell cancer: under androgen-receptor blockade, prostate cancer can switch to treatment-emergent neuroendocrine/small-cell carcinoma with RB1 and p53 loss, resembling and treated like small-cell lung cancer.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Its hormone therapy hits the arteries: androgen-deprivation therapy accelerates metabolic syndrome and atherosclerosis of the arterial wall, making cardiovascular disease a leading cause of death in treated prostate cancer.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver spread marks aggressive disease: visceral metastasis to the hepatic lobules, uncommon in indolent prostate cancer, signals aggressive or neuroendocrine castration-resistant disease with a poor prognosis.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — A shared BRCA2 risk: germline BRCA2 mutations raise the risk of aggressive prostate cancer alongside breast, ovarian, pancreatic cancer and melanoma, defining a hereditary cancer spectrum that guides screening.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — A textbook cause of cancer DIC: metastatic prostate cancer is a classic trigger of chronic disseminated intravascular coagulation, its tumour procoagulants driving simultaneous clotting and bleeding.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — RB1 and lethal transformation: loss of RB1, the retinoblastoma gene, drives treatment-emergent neuroendocrine (small-cell) prostate cancer, an aggressive androgen-independent transformation under therapy pressure.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — The cardiovascular cost of ADT: androgen-deprivation therapy induces metabolic syndrome and accelerates atherosclerosis, so cardiovascular disease is a leading cause of non-cancer death in prostate cancer survivors.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Metastatic cord compression: prostate cancer's bone-tropic spinal metastases can collapse vertebrae and compress the spinal cord and nerve roots, an oncologic emergency threatening permanent paralysis.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes and helps drive the lethal neuroendocrine transdifferentiation of castration-resistant prostate cancer.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: cyclin D1-CDK4/6 activity pushes prostate cancer cells through the G1 checkpoint, cooperating with androgen-receptor signalling to fuel proliferation.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in poorly oxygenated prostate tumours promotes angiogenesis, glycolysis and resistance to radiotherapy and androgen deprivation.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Osteoblastic bone metastasis: prostate cancer cells secrete endothelin-1 that stimulates osteoblasts, driving the dense sclerotic bone metastases that distinguish it from most other cancers' lytic lesions.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase immortalisation: TERT reactivation maintains telomeres in prostate cancer cells, granting the unlimited replicative capacity that underlies progression to castration-resistant disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage homing: CCL2 secreted by prostate tumours recruits tumour-associated macrophages and supports metastatic seeding of bone, where it amplifies osteoclast activity and tumour growth.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on prostate-cancer cells follows CXCL12 gradients to the bone marrow, a key homing mechanism behind the bone-dominant metastatic pattern that defines advanced prostate cancer and drives its skeletal morbidity.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — Prostate cancers with BRCA2 or ATM mutations are homologous-recombination deficient, engaging RAD51-mediated repair whose loss confers the synthetic-lethal sensitivity to PARP inhibitors (olaparib) now used in metastatic disease.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1 signaling promotes prostate epithelial proliferation and survival, and higher circulating IGF-1 is associated with prostate-cancer risk and progression independent of androgens—an alternate growth axis sustaining castration-resistant disease.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Upregulation of the glucocorticoid receptor lets prostate-cancer cells drive an AR-like transcriptional program despite AR blockade, a key mechanism of resistance to enzalutamide in castration-resistant disease.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Under potent AR-pathway inhibition some prostate cancers transdifferentiate into aggressive neuroendocrine tumors that lose AR and express neuroendocrine markers like SSTR2, a lethal, treatment-induced phenotype switch.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — BRCA/ATM-mutant, homologous-recombination-deficient prostate cancers accumulate cytosolic DNA that activates cGAS-STING, the innate-immune rationale for combining PARP inhibitors with checkpoint blockade in this molecular subset.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PTEN loss (already mapped) and PIK3CA activation drive the PI3K-AKT-mTOR pathway in prostate cancer, a resistance route that reciprocally cross-talks with androgen-receptor signaling to sustain castration-resistant growth.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/β-catenin signaling drives castration-resistant progression and contributes to the osteoblastic bone metastases (RANKL and osteoblasts already mapped) that characterize advanced prostate cancer.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β shifts from tumor suppressor to driver as prostate cancer advances, promoting epithelial-mesenchymal transition, the bone-metastatic niche and the immunosuppression of the tumor microenvironment.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — TMPRSS2-ERG and RAS-MAPK signaling cooperate with the androgen receptor to drive prostate-cancer proliferation, and MAPK reactivation underlies progression to castration-resistant disease.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D1-RB-E2F axis (cyclin-D1 mapped) drives proliferation, and RB loss releasing E2F1 promotes the lineage plasticity that yields treatment-emergent neuroendocrine prostate cancer.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated suppression and outright TP53 loss (p53 mapped) mark the aggressive, often neuroendocrine castration-resistant prostate cancer.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling promotes androgen-receptor reactivation and neuroendocrine differentiation in castration-resistant prostate cancer.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Loss of TGF-β-SMAD4 signaling (TGF-β mapped) is a key metastasis-suppressor lesion whose inactivation drives aggressive, bone-metastatic prostate cancer.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A (p16) loss releases CDK4/6-cyclin-D control (cyclin-D1 mapped) of the cell cycle, a recurrent lesion in lethal prostate cancer.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports immune evasion and the bone-metastatic colonization that drives mortality in advanced prostate cancer.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling supports androgen-independent growth and contributes to the castration resistance of advanced prostate cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of the immunologically cold prostate cancer, relevant to its limited immunotherapy responsiveness.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PTEN-loss-driven PI3K-AKT signaling (PTEN, AKT, and PIK3CA already mapped) inactivates FOXO, removing a tumor-suppressive brake in prostate cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 acting on the cyclin-D1-RB axis (cyclin-D1 already mapped) drives the cell-cycle progression of prostate cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunologically cold prostate cancer evades.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates AR and β-catenin stability (androgen receptor and Wnt already mapped), modulating the survival signaling of prostate cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the immunosuppressive, bone-metastatic microenvironment of prostate cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling contributes to the castration-resistant progression and bone-metastatic tropism of prostate cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of prostate cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and androgen-deprivation-therapy resistance of prostate cancer cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of prostate cancer.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment and bone-metastatic niche of prostate cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape and androgen-receptor cooperativity of prostate cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment and bone-metastatic progression of prostate cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of prostate cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of prostate cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of prostate cancer.
- `connects-to` → **[DLL3](../../03-molecular/dll3/README.md)** — Neuroendocrine transformation: androgen-receptor-directed therapy can drive lineage plasticity to aggressive treatment-emergent neuroendocrine prostate cancer, which expresses DLL3, the target of DLL3-directed agents beyond hormonal treatment.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Castration resistance: AXL receptor tyrosine kinase signalling promotes the epithelial-mesenchymal transition and therapy tolerance underlying progression to castration-resistant, metastatic prostate cancer despite androgen-receptor blockade.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune-cold tumour: prostate cancer generally presents few neoantigens and low MHC class II-driven antigen presentation, the basis of its poor checkpoint response, with exceptions in the MSI and CDK12-altered subsets and the sipuleucel-T vaccine.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Sipuleucel-T vaccine: IL-2-driven T-cell responses underlie sipuleucel-T, the autologous cellular immunotherapy that improves survival in castration-resistant prostate cancer (MHC and PD-1 already mapped) despite this tumour's poor response to checkpoint blockade.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: prostate cancer lowers haemoglobin through marrow replacement by bone metastases (RANKL already mapped), androgen-deprivation therapy and chemotherapy, and the resulting anaemia contributes to fatigue in advanced disease.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Androgen-deprivation cardiotoxicity: long-term androgen-deprivation therapy raises cardiovascular risk through adverse metabolic changes, and troponin elevation marks the myocardial injury of the cardiac events that complicate this mainstay treatment.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Radioligand and proton therapy: prostate cancer is treated with proton-beam radiotherapy and, in metastatic disease, the beta-emitting Lu-177-PSMA radioligand that targets the prostate-specific membrane antigen, delivering radiation to the tumour.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive cold tumour: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), part of the immune evasion that makes most prostate cancer a checkpoint-resistant 'cold' tumour.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: oxidative stress, to which xanthine oxidase contributes, and its reactive oxygen species contribute to prostate carcinogenesis and progression (NRF2-adjacent redox biology), part of the tumour's oxidative dimension.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, checkpoint-resistant immune microenvironment of most prostate cancer.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia of therapy: androgen-deprivation therapy and metastatic marrow involvement cause anaemia (haemoglobin already mapped) in prostate cancer, and the transfusional support can load the body with iron.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 and inflammation: prostaglandins from cyclooxygenase-2 in the inflamed prostate contribute to carcinogenesis and progression (IL-6 already mapped), part of the chronic-inflammation link in prostate cancer.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive 'cold' microenvironment of prostate cancer.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and aggressiveness: the adipokine leptin links obesity — a risk factor for aggressive and lethal prostate cancer — to the proliferation and progression of the tumour.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine axis: adiponectin, with leptin (already mapped), links the obesity and metabolic state to the risk and aggressiveness of prostate cancer, part of the adipokine influence on the tumour.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity risk of the aggressive prostate cancer.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the M2 (IL-4 and IL-13 already mapped) tumour-associated macrophages (CCL2 already mapped) of the immunosuppressive 'cold' microenvironment of prostate cancer.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Reactive stroma: the cancer-associated fibroblasts of the reactive prostate-cancer stroma (TGF-β already mapped) support the tumour progression and the androgen (androgen-receptor already mapped) signalling.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the (sparse) tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm largely excluded by the immunosuppressive 'cold' microenvironment of prostate cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response explored against the immunologically cold prostate cancer.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance of the prostate cancer, an arm explored to overcome its immunosuppressive microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immunosuppressive microenvironment of prostate cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of prostate cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immunologically cold prostate-cancer microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of prostate cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures within the immunologically cold prostate-cancer microenvironment, a candidate correlate of the immunotherapy response.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the tumour-promoting inflammation of prostate cancer.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory and immunosuppressive dimension of the immunologically cold prostate-cancer microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid (macrophage already mapped) recruitment and immunosuppression of the prostate-cancer microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the prostate-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the microenvironment.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Tumour-stromal alarmin: TSLP, secreted by cancer-associated fibroblasts (already mapped) and bone-marrow (already mapped) stroma, activates mast cells (already mapped) and dendritic cells (already mapped), promoting the immunosuppressive microenvironment of prostate cancer.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-growth axis: bradykinin, generated via the kallikrein-kinin system in the tumour microenvironment, signals via B2 receptors on cancer cells and endothelial cells (already mapped) to promote proliferation and angiogenesis (VEGF already mapped) of prostate cancer.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anemia correction: erythropoietin addresses the anemia of chronic disease (already mapped) and the myelosuppression from chemotherapy (already mapped), supporting haematopoiesis and quality of life in advanced prostate cancer.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell TME effector: histamine, released by mast cells (already mapped) in the tumour microenvironment of prostate cancer, promotes angiogenesis (VEGF already mapped), immunosuppression and androgen-receptor (already mapped) signalling crosstalk of prostate cancer.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Bone metastasis ECM scaffold: periostin, highly expressed in the bone microenvironment, promotes osteoblastic (already mapped) and mixed prostate cancer bone metastasis by facilitating tumour cell adhesion and the fibrotic remodelling of bone lesions.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3 and C5 already mapped) and contact-kinin (bradykinin already mapped) activation in the tumour microenvironment, moderating complement-driven immunosuppression of prostate cancer.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — PC serotonin: serotonin, via 5-HT receptors on prostate cancer cells and macrophages (already mapped), promotes tumour proliferation and the immunosuppressive tumour microenvironment; 5-HT also modulates the androgen-receptor (already mapped) signalling axis of prostate cancer.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — PC melatonin: melatonin, via MT1/MT2 receptors, attenuates androgen-receptor (already mapped) signalling and tumour proliferation in prostate cancer; melatonin also suppresses osteoblast (already mapped) RANKL (already mapped) bone-metastatic niche formation.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — PC prolactin: prolactin, via PRLR on prostate cancer cells, activates mTOR (already mapped) and promotes tumour survival; prolactin also modulates macrophage (already mapped) polarisation and androgen-receptor (already mapped) signalling crosstalk in prostate cancer.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PC oxytocin: oxytocin, via OXTR on prostate cancer cells and macrophages (already mapped), attenuates NF-κB (already mapped) tumour inflammation and androgen-receptor (already mapped) signalling; oxytocin modulates the immunosuppressive tumour microenvironment of prostate cancer.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PC vasopressin: vasopressin V1 receptors on prostate cancer cells promote the NF-κB (already mapped) driven tumour proliferation and vascular remodelling; V2-receptor activation amplifies androgen-receptor (already mapped) signalling and tumour invasion in prostate cancer.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PC iodine: iodine-dependent thyroid hormones regulate prostate cancer cell proliferation and androgen-receptor (already mapped) sensitivity; thyroid-hormone deficiency amplifies the NF-κB (already mapped) tumour growth and mTOR (already mapped) driven metastatic progression.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — PC sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the mTOR (already mapped) and androgen-receptor (already mapped) tumour cascade of prostate cancer.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — PC magnesium: magnesium, as mTOR (already mapped) kinase cofactor in prostate cells and macrophages (already mapped), restrains tumour growth; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of prostate cancer.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — PC copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped) and osteoblasts (already mapped), drives ECM remodelling and bone metastasis; copper deficiency amplifies the NF-κB (already mapped) and VEGF (already mapped) angiogenic cascade of prostate cancer.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — PC potassium: potassium channels in macrophages (already mapped) and prostate tumour cells regulate NLRP3 inflammasome; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade supporting mTOR (already mapped) tumour growth in prostate cancer.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — PC chloride: chloride channels in macrophages (already mapped) and fibroblasts (already mapped) modulate tumour-stromal ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of prostate cancer.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — PC carbon: carbon as backbone of androgen receptor and NF-κB (already mapped) proteins in prostate tumour cells and macrophages (already mapped) sustains oncogenic signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of prostate cancer.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — PC hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and fibroblasts (already mapped), supports androgen receptor signalling; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of prostate cancer.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — PC nitrogen: nitrogen in amino-acid scaffold of androgen receptor and VEGF (already mapped) proteins in prostate tumour cells sustains oncogenic signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of prostate cancer.

[^beer-2014-prevail]: Beer TM, Armstrong AJ, Rathkopf D, et al. Enzalutamide in metastatic prostate cancer before chemotherapy. *N Engl J Med.* 2014;371(5):424-433. [doi:10.1056/NEJMoa1405095](https://doi.org/10.1056/NEJMoa1405095) · [PubMed 24881730](https://pubmed.ncbi.nlm.nih.gov/24881730/)
[^sartor-2021-vision]: Sartor O, de Bono J, Chi KN, et al. Lutetium-PSMA-617 for metastatic castration-resistant prostate cancer. *N Engl J Med.* 2021;385(12):1091-1103. [doi:10.1056/NEJMoa2107322](https://doi.org/10.1056/NEJMoa2107322) · [PubMed 34161051](https://pubmed.ncbi.nlm.nih.gov/34161051/)
[^de-bono-2020-profound]: de Bono J, Mateo J, Fizazi K, et al. Olaparib for metastatic castration-resistant prostate cancer. *N Engl J Med.* 2020;382(22):2091-2102. [doi:10.1056/NEJMoa1911440](https://doi.org/10.1056/NEJMoa1911440) · [PubMed 32343890](https://pubmed.ncbi.nlm.nih.gov/32343890/)
