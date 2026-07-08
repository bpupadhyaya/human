---
schema: human-scale-entry/v1
id: breast-cancer
name: Breast Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common cancer in women; driven by ER/PR hormone signaling, HER2 amplification, and basal TNBC subtypes. BRCA1/2 mutations drive hereditary cases; CDK4/6 inhibitors (palbociclib), anti-HER2 (trastuzumab), PARP inhibitors (olaparib), and immunotherapy are mainstays."
aliases: ["breast carcinoma", "HR+ breast cancer", "HER2+ breast cancer", "TNBC", "triple-negative breast cancer", "luminal A", "luminal B", "invasive ductal carcinoma", "invasive lobular carcinoma", "DCIS"]
sources:
  - id: siegel-2024-cancer-statistics
    type: peer-reviewed
    cite: "Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. CA Cancer J Clin. 2024;74(1):12-49."
    doi: "10.3322/caac.21820"
    pmid: "38230766"
    url: "https://doi.org/10.3322/caac.21820"
  - id: slamon-2001-trastuzumab-trial
    type: peer-reviewed
    cite: "Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. N Engl J Med. 2001;344(11):783-792."
    doi: "10.1056/NEJM200103153441101"
    pmid: "11248153"
    url: "https://doi.org/10.1056/NEJM200103153441101"
  - id: finn-2016-palbociclib-paloma2
    type: peer-reviewed
    cite: "Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. N Engl J Med. 2016;375(20):1925-1936."
    doi: "10.1056/NEJMoa1607303"
    pmid: "27959613"
    url: "https://doi.org/10.1056/NEJMoa1607303"
cross_links:
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 amplification (~20% of breast cancers) → constitutive kinase → PI3K-AKT-mTOR and RAS-ERK → aggressive biology; trastuzumab + pertuzumab + docetaxel is first-line HER2+ metastatic (CLEOPATRA OS 57 vs. 41 months); T-DM1 and T-DXd (DESTINY-Breast03) are second-line."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutations occur in 30-40% of HR+/HER2- breast cancer → PI3K-AKT-mTOR activation → endocrine therapy resistance; alpelisib (PI3K-alpha inhibitor) + fulvestrant is approved for PIK3CA-mutant HR+/HER2- metastatic breast cancer (SOLAR-1, PFS 11.0 vs. 5.7 months)."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1 germline mutations confer ~70% lifetime breast cancer risk (predominantly TNBC); BRCA1 loss → HR deficiency → PARP inhibitor sensitivity; olaparib (OlympiAD) and talazoparib (EMBRACA) are approved for BRCA1/2-mutant HER2-negative metastatic breast cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) + AI are standard-of-care first-line for HR+/HER2- metastatic breast cancer; ribociclib + letrozole improved OS to 63.9 vs. 51.4 months (MONALEESA-2); abemaciclib is approved adjuvantly for high-risk early-stage disease."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "ERα (ESR1) drives ~70-75% of breast cancers; aromatase inhibitors (anastrozole, letrozole) are first-line adjuvant for postmenopausal ER+ disease; fulvestrant (SERD) degrades ERα; ESR1 LBD mutations (D538G, Y537S) cause AI resistance in metastatic HR+ disease."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "PR+ breast cancers have better prognosis than PR- tumors; combined E2+progestogen HRT (WHI) increased breast cancer risk vs. estrogen-only; progestins in combined OCP contribute to VTE risk; PR agonists (megestrol, medroxyprogesterone) treat endometrial hyperplasia and EC."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Breast cancer bone metastases exploit the RANKL axis: PTHrP from tumor cells → osteoblast RANKL → osteoclast osteolysis releases TGF-β and IGF-1 → vicious cycle of tumor-bone crosstalk; denosumab (Xgeva) delays skeletal-related events by ~8.5 months vs. zoledronate (HALT-BC)."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Breast cancer overexpresses CXCR4 → homing to CXCL12-rich organs (bone marrow, lung, liver, brain) → organ-specific metastasis; stromal CXCL12 promotes primary tumor growth; CXCR4 correlates with lymph node involvement and poor prognosis; anti-CXCR4 therapy in trials."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Ang-2 promotes breast cancer angiogenesis: hypoxic tumor cells secrete Ang-2 → vessel destabilization → VEGF-driven sprouting; tumor Ang-2 correlates with lymph node metastasis and poor prognosis; Ang-2 blockade combined with anti-VEGF shows additive anti-tumor activity."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Breast and endometrial cancers are linked estrogen-driven malignancies: unopposed estrogen fuels both, and tamoxifen—an anti-estrogen in breast tissue—acts as a uterine estrogen agonist, raising endometrial cancer risk; obesity and the hormone milieu tie the two together."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Breast and ovarian cancers are the twin BRCA1/2 tumors of hereditary breast-ovarian cancer syndrome: germline BRCA loss cripples homologous-recombination repair, predisposing to both and making them exquisitely sensitive to PARP inhibitors (olaparib) and platinum chemotherapy."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Bone is the most common site of breast cancer metastasis: tumor cells secrete PTHrP that drives osteoblasts to overproduce RANKL → osteoclast activation → osteolytic destruction and a cycle releasing bone-stored growth factors; denosumab and bisphosphonates target this loop."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Hereditary breast and ovarian cancer syndrome from germline BRCA1/2 underlies ~5-10% of breast cancers: it brings early-onset, often triple-negative or bilateral tumors, intensified screening and risk-reducing surgery, and platinum/PARP-inhibitor sensitivity."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Li-Fraumeni syndrome is a striking cause of early breast cancer: germline TP53 loss yields breast cancer (often HER2-positive) in women under 30 alongside sarcomas—and because radiotherapy can induce second cancers, treatment favors mastectomy over radiation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Triple-negative breast cancer is the subtype most responsive to immunotherapy: its higher mutational burden and tumor-infiltrating cytotoxic T cells make it sensitive to PD-1/PD-L1 blockade (pembrolizumab), unlike the immunologically quiet hormone-receptor-positive tumors."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Breast cancer is a core feature of Cowden syndrome: germline PTEN loss unleashing PI3K-AKT gives a high lifetime breast cancer risk alongside thyroid and endometrial cancer—so Cowden is one of the hereditary syndromes screened for in familial breast cancer."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is integral to breast cancer treatment: after lumpectomy, whole-breast or partial radiation halves local recurrence, and post-mastectomy radiation treats high-risk disease—radiation made breast-conserving surgery as safe as mastectomy."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Breast and prostate cancer are the paradigm hormone-driven cancers and share BRCA biology: breast growth depends on estrogen, prostate on androgens (blocked by ADT), and BRCA2 raises risk of both—endocrine therapy is central to each."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "BRCA2 mutation strongly predisposes to breast cancer: this DNA-repair gene, when lost, leaves cells unable to fix double-strand breaks, so hereditary BRCA2 tumors arise young and are exquisitely sensitive to PARP inhibitors that exploit the repair defect."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 blockade has entered breast cancer through its most aggressive subtype: triple-negative tumors carry more mutations and immune infiltrate, so adding anti-PD-1 (pembrolizumab) to chemotherapy improves outcomes where hormonal and HER2 therapies do not apply."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Breast cancer spreads first through the lymphatic system: tumor cells drain to axillary nodes, so sentinel-node biopsy stages the disease and nodal involvement is among the strongest prognostic factors—guiding decisions on radiation and systemic therapy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Breast cancer is a leading source of brain metastases: HER2-positive and triple-negative subtypes especially seed the brain, where the blood-brain barrier shields tumor cells from many drugs—so brain-penetrant agents like tucatinib are changing outcomes."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts shape breast tumors: they build the stiff, desmoplastic stroma that aids invasion, fuels growth signals, and blocks drug delivery and immune access—so the fibroblast-rich microenvironment, not just tumor cells, drives progression."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity worsens breast cancer at both ends: after menopause, fat tissue's aromatase raises estrogen that drives hormone-receptor-positive tumors, and obesity-linked inflammation and insulin resistance worsen prognosis—so weight is a modifiable risk and outcome factor."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a frequent breast-cancer metastatic site: spread there, alongside bone, lung and brain, marks stage IV disease and worsens prognosis, so liver function and imaging are watched—and HR-positive cancers can colonize it years after the primary."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages help breast cancer spread: recruited into the tumor, they promote angiogenesis, invasion and immune evasion, and a macrophage-rich microenvironment predicts worse outcome—making them a target alongside the cancer cells."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is a clear, modifiable breast-cancer risk: even moderate drinking raises risk by increasing estrogen and generating DNA-damaging acetaldehyde, so reducing alcohol is one of the few lifestyle levers proven to lower breast-cancer incidence."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is a frequent home for breast-cancer spread: tumor cells seeded through the blood lodge in its fine capillaries and grow, so lung metastases—as nodules or a diffuse lymphatic pattern—are a common cause of breast-cancer morbidity."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Breast fat fuels the tumor it surrounds: adipocytes in the breast make aromatase that converts androgens to estrogen, feeding hormone-driven cancer, which is part of why obesity raises postmenopausal breast-cancer risk."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Breast cancer hijacks bone's demolition crew: metastatic cells release RANKL and factors that activate osteoclasts to dissolve bone, releasing growth factors that feed the tumor in a vicious cycle behind painful osteolytic lesions."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Breast cancer in bone can flood the blood with calcium: osteolytic metastases dissolve bone faster than the body can clear the released calcium, causing the hypercalcemia of malignancy—confusion, thirst, and kidney injury needing urgent care."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Breast cancer can hide in the bone marrow: single tumor cells lodge there and lie dormant for years, a reservoir of disseminated disease that can reawaken to cause the late relapses unique to this cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help hold breast cancer in check: these innate lymphocytes can detect and destroy tumor cells without prior sensitization, and strong NK activity is linked to fewer metastases and better outcomes."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper fuels breast cancer's spread: tumors need it for new blood vessels and for enzymes that prime metastasis, so copper-lowering drugs have been trialed to keep dormant disease asleep."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Breast cancer can invade the skin: inflammatory breast cancer reddens and dimples it into peau d'orange, and chest-wall skin recurrences signal aggressive local disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Breast tumors build a fibrotic stroma: a dense, desmoplastic scar stiffens the tumor, shows as the spiculated mass on a mammogram, and helps shield the cancer from drugs."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads breast cancer's glandular roots: ductal carcinoma cells retain microvilli-lined intracytoplasmic lumina and secretory features, ultrastructure that confirms epithelial origin when a poorly differentiated tumor is hard to classify."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Breast cancer is the eye's commonest invader: it is the leading source of choroidal metastasis, the tumor seeding the back of the eye to blur vision, sometimes the first hint that the cancer has spread."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Breast cancer recruits platelets to spread: circulating tumor cells cloak themselves in platelets to hide from immune attack and lodge in distant organs, while the tumor also drives the clotting risk that haunts cancer patients."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The chemotherapy bites the nerves: taxanes like paclitaxel, central to breast cancer treatment, injure peripheral sensory neurons into a stocking-glove neuropathy that can force dose cuts and outlast the therapy."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Two breast cancer drugs strain the heart: the HER2 antibody trastuzumab and the anthracyclines can each weaken the myocardium, so cardiac function is monitored before and during treatment to catch a falling ejection fraction."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment reshapes reproductive life: chemotherapy can force premature menopause and infertility, while tamoxifen — protective in the breast — stimulates the uterine lining and raises endometrial cancer risk."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies define and treat the disease: ER, PR, and HER2 immunostains classify every tumor and pick the therapy, and the targeted drugs are antibodies themselves — trastuzumab and pertuzumab against HER2, plus the newer antibody-drug conjugates."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Chemotherapy hammers the marrow: the anthracycline and taxane regimens are myelosuppressive, dropping neutrophil counts so that growth-factor support and febrile-neutropenia vigilance run through treatment."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Lobular breast cancer has a strange destination: the diffuse, single-file invasive lobular type characteristically metastasizes to the stomach and GI tract, sometimes mimicking a primary gastric cancer years after the breast tumor."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Losing p53 marks the hardest breast cancers: TP53 mutation is the rule in triple-negative and Li-Fraumeni-driven disease, unleashing genomic instability and an aggressive course that resists hormone and HER2 therapies."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The cure can wound the heart: anthracyclines and HER2-targeted trastuzumab are cardiotoxic, so cancer-therapy-related heart failure is a key survivorship concern that ties breast oncology to cardiology surveillance."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Tumors recruit Tregs to hide from immunity: regulatory T cells infiltrate the breast tumor microenvironment and suppress the cytotoxic response, a marker of worse prognosis and a barrier to immunotherapy."
  - target: 01-human/03-molecular/palb2
    relation: connects-to
    note: "Another repair gene joins BRCA: germline PALB2 mutations, which partner BRCA2 in homologous recombination, confer a high breast cancer risk and the same sensitivity to PARP inhibitors, widening who gets genetic testing."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "ER-positive tumors lean on a growth hub: PI3K-AKT-mTOR signaling drives proliferation and resistance to hormone therapy, so the mTOR inhibitor everolimus is added to endocrine treatment when the cancer escapes it."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplification marks the aggressive tumors: MYC is frequently amplified in basal and triple-negative breast cancer, powering relentless proliferation in the subtypes that lack hormonal and HER2 targets."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB drives the hardest-to-treat subtype: constitutive NF-κB signaling supports survival, inflammation and metastasis in ER-negative and triple-negative breast cancer, a pathway studied where hormonal and HER2 targets are absent."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The cancer and its therapy both clot: breast cancer raises thrombosis risk, compounded by tamoxifen and chemotherapy, so deep-vein thrombosis and pulmonary embolism are recognized complications of treatment."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Chemo strips the body's defenses: the cytotoxic regimens used against breast cancer cause neutropenia, making febrile neutropenia and sepsis a recurring hazard of treatment."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Its hormone therapy strips the bone: aromatase inhibitors and ovarian suppression for estrogen-receptor-positive breast cancer cut estrogen sharply, accelerating bone loss so that osteoporosis monitoring and treatment accompany therapy."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Tumor inflammation and chemo blunt the marrow: the IL-6 of advanced breast cancer raises hepcidin while cytotoxic therapy suppresses erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "The diagnosis and its toll weigh on mood: depression is common across the breast-cancer journey, driven by the threat to life, the effects of surgery and chemotherapy, and the menopausal symptoms of endocrine therapy."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Treatment leaves nerves aching: taxane chemotherapy causes peripheral neuropathy, mastectomy can produce post-surgical neuropathic pain, and aromatase inhibitors bring disabling arthralgias."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Cancer and its therapy raise clot risk to the brain: the hypercoagulable state of malignancy, tamoxifen's thrombotic risk and chest radiation's vascular damage together raise the risk of ischemic stroke."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its chemotherapy opens the lung to mold: the neutropenia from breast-cancer chemotherapy can let inhaled Aspergillus invade as pulmonary aspergillosis, particularly with dose-dense regimens."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Most breast cancer is hormone-driven: oestrogen-receptor-positive tumours grow on oestrogen, so endocrine therapy with tamoxifen or aromatase inhibitors is central, bringing menopausal symptoms and bone loss."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Mastectomy and radiation heal slowly: breast surgery with reconstruction and axillary dissection leaves wounds prone to seroma and infection, and prior or adjuvant radiation impairs tissue healing."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Recurrence fear breeds chronic worry: the scan and tumour-marker surveillance, body-image change and dread of relapse in breast cancer foster persistent health anxiety alongside depression."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Bone is its favourite distant home: breast cancer most often metastasises to the skeleton, causing bone pain, pathological fractures, hypercalcaemia and spinal cord compression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to lung and pleura: breast cancer commonly metastasises to the lungs and pleura, producing nodules and malignant pleural effusions with breathlessness."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It reaches the brain: HER2-positive and triple-negative breast cancers in particular metastasise to the brain and leptomeninges, causing headaches, seizures and focal deficits."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its treatments are cardiotoxic: anthracyclines and HER2-targeted trastuzumab can weaken the heart muscle, and radiation to the left breast raises later coronary disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It declares itself on the skin: inflammatory breast cancer gives a peau d'orange dimpling, Paget disease scales the nipple, and chest-wall recurrences seed skin nodules."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can spread to the gut: lobular breast cancer in particular metastasises to the stomach and bowel, while chemotherapy and endocrine therapy bring nausea and hepatotoxicity."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Molecular subtyping drives its treatment: HER2 antibodies (trastuzumab, pertuzumab, T-DXd), CDK4/6 inhibitors for hormone-receptor-positive disease and PARP inhibitors for BRCA-mutant tumours are central to modern breast cancer care."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune microenvironment shapes outcome: tumour-infiltrating lymphocytes predict response in triple-negative breast cancer, where checkpoint inhibitors added to chemotherapy now improve survival."
  - target: 03-medicine/03-food/sulforaphane
    relation: connects-to
    note: "Diet is studied for prevention: cruciferous-vegetable sulforaphane is investigated for breast cancer chemoprevention through effects on oestrogen metabolism and tumour-cell signalling."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Anthracyclines and taxanes anchor it: cytotoxic chemotherapy with anthracyclines and taxanes is given neoadjuvantly or adjuvantly across breast cancer subtypes, especially triple-negative and node-positive disease, alongside targeted and endocrine therapy."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone is its favourite metastatic site: breast cancer spreads to bone as RANKL-driven osteolytic metastases causing pain and fractures, while aromatase inhibitors add their own bone loss — both countered by bisphosphonates and denosumab."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Its treatment can injure the heart: anthracyclines cause dose-dependent cardiomyopathy and trastuzumab a usually reversible cardiac dysfunction, so monitoring myocardial function is central to cardio-oncology in breast cancer."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "CDH1 links breast and stomach: germline loss of E-cadherin (CDH1) causes hereditary diffuse gastric cancer together with lobular breast cancer, so CDH1 carriers undergo breast surveillance and risk-reducing surgery."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Lymphoid islands predict its immunotherapy response: triple-negative breast cancers that form tertiary lymphoid structures with germinal-centre B cells respond better to checkpoint blockade."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Shared BRCA vulnerability: BRCA1/2 and PALB2-mutant breast and pancreatic cancers both respond to PARP inhibitors and platinum chemotherapy, within the HBOC spectrum of homologous-recombination-deficient tumours."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver as a metastatic site: breast cancer commonly spreads to the liver, seeding the hepatic lobules, and luminal subtypes can present with liver-dominant metastatic disease years after the primary."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Therapy-related leukaemia: the alkylators, anthracyclines and radiation that cure breast cancer can seed a secondary, poor-prognosis AML or MDS years later, a late cost of cytotoxic treatment."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "A shared BRCA2 spectrum: germline BRCA2 raises the risk of breast cancer alongside ovarian, prostate, pancreatic cancer and melanoma, a hereditary cancer cluster that guides cascade genetic testing."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Seizures from brain spread: breast cancer (especially HER2-positive and triple-negative) is a leading cause of brain metastases and leptomeningeal disease, producing seizures and secondary epilepsy."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Nerve and cord compromise: bone-tropic breast cancer can collapse vertebrae and compress the spinal cord and nerve roots, while tumour or radiation can injure the brachial plexus—threatening permanent deficits."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Immunotherapy's autoimmune cost: checkpoint inhibitors now used for triple-negative breast cancer can unleash an autoimmune colitis resembling inflammatory bowel disease, managed with steroids and anti-TNF biologics."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT axis: AKT, activated downstream of PIK3CA and HER2, drives breast cancer growth and survival and underlies resistance to endocrine therapy, making AKT inhibitors a targeted option."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic aggression: HIF-1α stabilised in hypoxic breast tumours promotes angiogenesis, metastasis and treatment resistance, and marks the more aggressive triple-negative subtypes."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Tumour angiogenesis: VEGF drives the new-vessel growth that feeds breast tumour expansion and metastasis, a hallmark exploited by anti-angiogenic therapy."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Amplified cell-cycle driver: CCND1 (cyclin D1) is amplified in many ER-positive breast cancers, partnering CDK4/6 to push proliferation and underpinning sensitivity to CDK4/6 inhibitors."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Metastatic switch: TGF-beta turns from tumour suppressor to driver of epithelial-mesenchymal transition, immune evasion and bone-metastatic spread in advancing breast cancer."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 secreted by breast tumours draws tumour-associated macrophages that promote angiogenesis, immune suppression and metastatic seeding of the lung."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "Lobular subtype: loss of E-cadherin (CDH1) defines invasive lobular carcinoma, producing its single-file infiltrative growth and the discohesive cells that make it hard to detect on imaging and prone to diffuse spread."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "HR repair and PARP: BRCA-mutant and HRD breast cancers depend on RAD51-mediated homologous recombination, whose deficiency confers the synthetic-lethal sensitivity to PARP inhibitors (olaparib, talazoparib)."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "AR-driven subtype: the androgen receptor is expressed in many breast cancers and defines the luminal-androgen-receptor triple-negative subtype, where AR-targeted therapy is under investigation."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "HRD immunogenicity: BRCA-mutant, homologous-recombination-deficient breast cancers accumulate cytosolic DNA that activates cGAS-STING, the innate-immune basis for combining PARP inhibitors with checkpoint blockade in triple-negative disease."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Endocrine resistance: FGFR1 amplification is a recurrent event in ER-positive breast cancer that drives resistance to endocrine therapy by providing an alternative growth signal, making FGFR a target to restore sensitivity to hormonal treatment."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Cancer stem cells: Notch signalling sustains the breast-cancer stem-cell population that resists chemotherapy and endocrine therapy and seeds recurrence, a developmental pathway driving treatment resistance and a target under investigation."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K resistance: PTEN loss activates the PI3K-AKT-mTOR pathway (PIK3CA, AKT and mTOR already mapped) in breast cancer and is a major mechanism of resistance to endocrine and HER2-targeted therapy."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle engine: the cyclin-D-CDK4/6-RB-E2F axis (CDK4/6 and cyclin-D1 already mapped) drives proliferation in ER-positive breast cancer, the pathway whose blockade by CDK4/6 inhibitors transformed its treatment."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Endocrine-resistance crosstalk: RAS-MAPK-ERK signalling crosstalks with estrogen-receptor signalling and is a route of acquired resistance to endocrine therapy in breast cancer."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor resistance: IGF-1R signalling crosstalks with the estrogen receptor and HER2 (both mapped), driving acquired resistance to endocrine and HER2-targeted therapy in breast cancer."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Cancer stem cells: Wnt/β-catenin signalling sustains the breast-cancer stem-cell compartment and is especially active in triple-negative breast cancer, contributing to recurrence."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 inactivation: MDM2 amplification suppresses p53 (mapped), an alternative to outright TP53 mutation that disables the apoptotic checkpoint in breast cancer."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) is a context-dependent regulator in breast cancer, switching from tumour suppression to promotion of EMT and metastasis."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 expression, driven by estrogen-receptor signalling (estrogen mapped), promotes survival of luminal breast cancer cells and carries prognostic significance."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-JAK-STAT3 signalling supports breast cancer stem-cell maintenance, proliferation and immune evasion."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports immune evasion and the metastatic colonisation that drives mortality in breast cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of breast cancer, particularly the immunotherapy-relevant triple-negative subtype."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression silences tumour-suppressor genes and contributes to the epigenetic dysregulation and aggressiveness of breast cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-driven FOXO inactivation (PTEN, AKT, and PIK3CA already mapped) removes a tumor-suppressive, pro-apoptotic brake in breast cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that breast cancer, especially the triple-negative subtype, must evade."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from myeloid-derived suppressor cells promote the pre-metastatic niche and immunosuppression of breast cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates β-catenin and cyclin-D1 stability (Wnt and cyclin-D1 already mapped), modulating the survival and proliferation signaling of breast cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of ER, HER2, and growth-factor receptors drives the invasion and endocrine-therapy resistance of breast cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of tumor-suppressor genes in breast cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and endocrine/chemotherapy resistance of breast cancer cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of breast cancer, a candidate metformin target."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven macrophage recruitment shapes the pro-metastatic microenvironment of breast cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of breast cancer."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of breast cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment and bone-metastatic progression of breast cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of breast cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of breast cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of breast cancer."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "TNBC immunotherapy: triple-negative breast cancer, lacking hormone and HER2 targets, is the subtype most responsive to checkpoint inhibitors, and MHC class II antigen presentation with tumour-infiltrating lymphocytes predicts that immune response."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Therapy resistance: the AXL receptor tyrosine kinase drives epithelial-mesenchymal transition, metastasis and resistance to endocrine and targeted therapy in breast cancer, a candidate target for reversing treatment escape."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity risk: obesity raises postmenopausal breast-cancer risk through adipose aromatase-derived estrogen (already mapped) and the adipokine leptin, which promotes tumour-cell proliferation, linking metabolism to breast carcinogenesis."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiotoxicity: HER2-directed trastuzumab (already mapped) and anthracycline chemotherapy are cardiotoxic, and troponin elevation helps detect the myocardial injury that limits these effective breast-cancer treatments."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Immunotherapy: IL-2-driven T-cell responses underlie the tumour-infiltrating lymphocytes and checkpoint benefit (PD-1 already mapped) seen mainly in triple-negative breast cancer, the immunogenic subset where immunotherapy is effective."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Chemotherapy anaemia: breast-cancer chemotherapy is myelosuppressive and lowers haemoglobin, and marrow replacement by metastatic disease compounds the anaemia that contributes to fatigue in advanced breast cancer."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammation-estrogen link: cyclooxygenase-2-derived prostaglandin E2 in the breast tumour and adipose stroma induces aromatase and local estrogen (already mapped) synthesis, linking inflammation to the hormone drive of estrogen-receptor-positive breast cancer."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), part of the immune evasion that limits checkpoint benefit outside the immunogenic triple-negative subset."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and lysis stress: the chemotherapy of breast cancer generates oxidative stress and cell lysis releasing purines that xanthine oxidase converts to uric acid, adding an oxidative and tumour-lysis burden to treatment."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of breast cancer outside the immunogenic triple-negative subset."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia of therapy: the chemotherapy and advanced disease of breast cancer cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obesity and breast cancer: obesity, through the adipokines leptin (already mapped) and the fall in adiponectin, and through the aromatase-driven oestrogen (already mapped), raises the risk and worsens the prognosis of postmenopausal breast cancer."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of breast cancer, promoting the metastasis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages (CCL2 already mapped) of the breast-cancer stroma, in their M2 (IL-4 already mapped) phenotype, drive the immunosuppression, angiogenesis (VEGF already mapped) and metastasis."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts: the CAFs (TGF-β and PDGF already mapped) of the breast-cancer stroma drive the desmoplasia, the immune exclusion and the progression of the tumour."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity risk of the postmenopausal (estrogen already mapped) breast cancer."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hepatic metastases: the liver is a common site of breast-cancer metastasis, the visceral disease of poorer prognosis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Mammary adipose niche: the mammary adipocytes (the source of leptin, adiponectin and resistin already mapped and the local aromatase oestrogen) form the tumour microenvironment driving the breast-cancer progression."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of triple-negative breast cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the breast-cancer immune microenvironment."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of breast cancer."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of breast cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of breast cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the breast-cancer microenvironment (and the emerging AllergoOncology anti-tumour IgE)."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of breast cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts the response to the immunotherapy of breast cancer (especially triple-negative)."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the tumour-promoting-versus-protective immune balance of breast cancer."
---

# Breast Cancer

## Overview

**Breast cancer** is the **most common cancer in women worldwide** and the second leading cause of cancer-related death in women. In 2024, approximately **310,720 new cases** of invasive breast cancer will be diagnosed in the United States, with ~42,000 deaths [^siegel-2024-cancer-statistics]. It is now surpassed by lung cancer in global cancer deaths but remains the most diagnosed cancer among women globally.

**Breast cancer is biologically heterogeneous** — it is best understood as multiple distinct diseases with different molecular drivers, natural histories, prognoses, and treatment strategies, unified by their tissue of origin in mammary epithelium.

**Intrinsic molecular subtypes (PAM50 classification):**
- **Luminal A (~40%):** ER+/PR+, HER2-, low Ki-67 (grade 1-2); best prognosis; driven by estrogen signaling; responds well to hormone therapy; chemotherapy often unnecessary; 10-year DFS >85%; endocrine therapy is sufficient in most
- **Luminal B (~20%):** ER+, HER2-/+, high Ki-67 or grade 3; more proliferative than Luminal A; may benefit from chemotherapy; worse prognosis than Luminal A; CDK4/6 inhibitors have greatest benefit
- **HER2-enriched (~15%):** HER2 amplification/overexpression; ER-negative; aggressive; transformed by advent of HER2-targeted therapy; trastuzumab + pertuzumab + chemotherapy → DFS ~90% at 3 years in early stage; T-DXd highly active in metastatic
- **Basal-like/TNBC (~15%):** ER-, PR-, HER2-; high grade; aggressive; BRCA1-associated tumors mostly in this subtype; no hormonal targets; chemotherapy, immunotherapy (pembrolizumab), PARP inhibitors (BRCA1/2-mutant); worst prognosis but higher rate of pathological complete response to neoadjuvant chemotherapy
- **Normal-like (~5-10%):** Resembles normal breast tissue; variable prognosis

**Hereditary breast cancer:**
- **BRCA1/2 (~5-10% of all breast cancers):** BRCA1 → predominantly TNBC/basal-like; BRCA2 → Luminal/HER2-enriched; BRCA1/2 mutations → 70%/45% lifetime risk respectively; management: prophylactic mastectomy, bilateral salpingo-oophorectomy (also prevents ovarian cancer), intensive surveillance (annual MRI + mammography from age 25-30)
- **Other hereditary genes:** PALB2 (40-60% lifetime risk, similar to BRCA2), ATM (20-30%), CHEK2 (15-25%), CDH1 (hereditary diffuse gastric + lobular breast cancer), TP53 (Li-Fraumeni — 50-90% lifetime risk), PTEN (Cowden syndrome), STK11 (Peutz-Jeghers)

**Epidemiology and risk factors:**
- **Age:** Incidence rises sharply after 40; peak incidence 60-70 years; younger-onset more likely hereditary or TNBC
- **Hormonal:** Early menarche, late menopause, nulliparity, late first birth, hormone replacement therapy (combined estrogen/progesterone HRT → increased risk), oral contraceptives (modest)
- **Lifestyle:** Obesity (postmenopausal), alcohol consumption, physical inactivity, dense breast tissue (imaging-based risk factor)
- **Prior breast biopsy:** ADH (atypical ductal hyperplasia), ALH → 4-5× increased risk; LCIS → 7-10× risk (marker not obligate precursor)
- **Race:** Black women have lower incidence but higher mortality (later stage at diagnosis, more TNBC, higher grade, socioeconomic/access factors)

## Structure

### Histopathology and staging

**Histological types:**
- **Invasive ductal carcinoma (IDC/NST, no special type, ~75%):** Most common; forms infiltrating cords/nests; graded by Nottingham grade (tubule formation, nuclear pleomorphism, mitotic rate; Grade 1-3)
- **Invasive lobular carcinoma (ILC, ~15%):** CDH1 (E-cadherin) loss → discohesive single-file "Indian file" infiltration; often ER+/lobular; associated with bilateral disease; may be occult on mammogram; responds to endocrine therapy
- **Special types (better prognosis):** Mucinous (colloid), tubular, medullary, cribriform, adenoid cystic (TNBC but indolent)
- **DCIS (ductal carcinoma in situ):** Non-invasive; precursor lesion; managed by excision ± radiation ± endocrine therapy (tamoxifen reduces ipsilateral invasive recurrence); controversial: subset of low-grade DCIS may never become invasive (active surveillance trials: COMET, LORIS, LORD)

**TNM staging (AJCC 8th edition — includes molecular subtype):**
- Stage I-III: Locoregional; curative intent; Stage IV: Distant metastasis (bone, lung, liver, brain most common) — generally incurable but increasingly manageable as chronic disease (median OS in HR+/HER2- metastatic: 3-4 years; HR+ HER2-: improving)
- Prognostic genomic tests (Oncotype DX [21-gene RS], MammaPrint [70-gene], PAM50/Prosigna, EndoPredict) identify which early-stage HR+ breast cancers benefit from adjuvant chemotherapy vs. endocrine therapy alone

### Molecular oncogenesis

**HR+ pathway (estrogen receptor-driven):**
- Estrogen → ER-alpha binding → ER dimerization → ERE binding → cyclin D1, MYC, BCL-2 transcription → G1-S progression
- **PI3K-AKT-mTOR axis:** PIK3CA gain-of-function (30-40% of HR+ tumors) → AKT-mTOR → ER-independent growth → endocrine resistance; PTEN loss (25-30%) → same net effect
- **CDK4/6-Rb axis:** Cyclin D1-CDK4/6 → Rb phosphorylation → E2F activation → S-phase; CDK4/6 inhibitors restore Rb-mediated G1 arrest
- **Endocrine resistance mechanisms:** ESR1 mutations (D538G, Y537S — acquired, found in cfDNA) → ligand-independent ER activation; PI3K pathway activation; CDK4/6 pathway amplification (cyclin D1, CDK4 amplification)

**HER2+ pathway:** See HER2 cross-link entry.

**TNBC/Basal-like:**
- High genomic instability, TP53 mutations (>80%), BRCA1 loss, RB1 loss; driven by PI3K-AKT, EGFR, FGFR, AR (androgen receptor — ~30% of TNBC express AR → potential therapeutic target)
- High tumor-infiltrating lymphocytes (TILs) correlate with better prognosis and immunotherapy response; high PD-L1 expression in ~40% of TNBC → pembrolizumab + chemotherapy approved in PD-L1+ metastatic TNBC (KEYNOTE-522 in early-stage regardless of PD-L1)

## Function

### Clinical presentation and screening

**Presentation:**
- Most common: painless, hard, irregular breast lump; asymmetric thickening
- Nipple discharge (bloody → suspicious), skin changes (peau d'orange = lymphatic obstruction, dimpling, nipple retraction, erythema)
- Inflammatory breast cancer (IBC, 1-3%): Rapid-onset erythema, warmth, edema, peau d'orange of breast skin without palpable mass → dermal lymphatic invasion; aggressive; requires neoadjuvant chemotherapy before surgery
- Paget's disease: Eczematous nipple rash → intraepidermal carcinoma cells (Paget cells); associated with underlying DCIS or invasive cancer in most cases

**Screening:**
- **Mammography:** Annual from age 40-74 (USPSTF updated 2024: recommends starting at 40, previously 50); reduces breast cancer mortality ~15-20% in screened populations; digital breast tomosynthesis (3D mammography) improves cancer detection and reduces false positives vs. 2D
- **MRI:** Annual breast MRI + mammography for high-risk (BRCA1/2, >20% lifetime risk); superior sensitivity in dense breasts; false-positive rate higher
- **Ultrasound:** Supplement to mammography in dense breasts; not a standalone screening tool in average risk

## Pathology

### Diagnosis and biomarkers

**Core needle biopsy:** Ultrasound or stereotactic-guided; provides histology, grade, ER/PR (IHC, % cells + Allred score), HER2 (IHC 0/1+/2+/3+; 2+ → FISH/ISH reflex), Ki-67 (proliferation index)

**Genomic testing in early-stage HR+/HER2- breast cancer:**
- **Oncotype DX (21-gene recurrence score, RS):** Predicts 10-year distant recurrence risk and chemotherapy benefit in node-negative (TAILORx trial) and 1-3 node-positive (RxPONDER) ER+/HER2- early breast cancer; RS <26 → endocrine therapy alone (chemotherapy no benefit in postmenopausal); RS ≥26 → chemotherapy benefit; now standard of care globally
- **MammaPrint (70-gene):** MINDACT trial: ~46% of clinically high-risk/genomic low-risk patients spared chemotherapy; approved in US for node-negative or 1-3 node-positive HR+/HER2-

### Treatment

**Early-stage (curative intent):**

*Surgery:*
- Breast-conserving surgery (lumpectomy + radiation) equivalent to mastectomy in OS for stages I-II; sentinel lymph node biopsy standard (avoids axillary lymph node dissection in sentinel-negative; Z0011 trial validates omission of ALND in limited nodal disease); nipple-sparing mastectomy with reconstruction increasingly used

*Radiation:*
- Post-lumpectomy whole-breast radiation reduces local recurrence 50-70%; hypofractionation (40 Gy/15 fractions) vs. conventional (50 Gy/25 fractions) equivalent efficacy; partial breast irradiation for select low-risk early-stage; regional nodal irradiation for ≥4 positive nodes

*Adjuvant systemic therapy by subtype:*
- **HR+:** Endocrine therapy 5-10 years (tamoxifen premenopausal; AI postmenopausal ± ovarian suppression); CDK4/6 inhibitors (abemaciclib × 2 years for high-risk, monarchE: significantly improved DFS)
- **HER2+:** Trastuzumab × 1 year ± pertuzumab (APHINITY); T-DM1 for residual disease after neoadjuvant (KATHERINE: iDFS 88% vs. 77% trastuzumab)
- **TNBC:** Pembrolizumab + chemotherapy neoadjuvant → pembrolizumab adjuvant (KEYNOTE-522: EFS benefit regardless of pCR); capecitabine for non-pCR; olaparib adjuvant for BRCA1/2-mutant (OlympiA: distant DFS benefit) [^slamon-2001-trastuzumab-trial]

**Metastatic HR+/HER2- (chronic disease management):**
- **First-line:** CDK4/6 inhibitor + AI (palbociclib/PALOMA-2, ribociclib/MONALEESA-2, abemaciclib/MONARCH-3); OS benefit confirmed for ribociclib (63.9 vs. 51.4 months, MONALEESA-2) [^finn-2016-palbociclib-paloma2]
- **Second-line (post-CDK4/6 + ESR1 mutation):** Elacestrant (oral SERD, EMERALD trial: PFS benefit in ESR1-mutant); fulvestrant + alpelisib (SOLAR-1, PIK3CA-mutant)
- **mTOR inhibitors:** Everolimus + exemestane (BOLERO-2: PFS 10.6 vs. 4.1 months); capivasertib (AKT inhibitor) + fulvestrant (CAPItello-291: approved for PIK3CA/AKT/PTEN-altered)
- **ADC (antibody-drug conjugate):** Sacituzumab govitecan (TROPION-Breast01 in HR+) and trastuzumab deruxtecan (T-DXd, DESTINY-Breast06 in HER2-low HR+) expanding options

**Metastatic TNBC:**
- **PD-L1+ (CPS ≥10):** Pembrolizumab + chemotherapy (KEYNOTE-355: OS 23.0 vs. 16.1 months)
- **BRCA1/2-mutant:** Olaparib (OlympiAD) or talazoparib (EMBRACA) superior to chemotherapy
- **Sacituzumab govitecan (Trodelvy, Trop-2 ADC):** ASCENT trial: OS 12.1 vs. 6.7 months vs. chemotherapy; approved for 2L+ TNBC

## Connections

- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 amplification (~20% of breast cancers) → constitutive kinase → PI3K-AKT-mTOR and RAS-ERK → aggressive biology; trastuzumab + pertuzumab + docetaxel is first-line HER2+ metastatic (CLEOPATRA: OS 57 vs. 41 months); T-DXd leads in second-line.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutations in 30-40% of HR+/HER2- breast cancer → PI3K-AKT-mTOR → endocrine therapy resistance; alpelisib + fulvestrant is approved for PIK3CA-mutant HR+/HER2- metastatic breast cancer (SOLAR-1, PFS 11.0 vs. 5.7 months).
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1 germline mutations confer ~70% lifetime breast cancer risk (predominantly TNBC); BRCA1 loss → HR deficiency → PARP inhibitor sensitivity; olaparib (OlympiAD) and talazoparib (EMBRACA) approved for BRCA1/2-mutant HER2-negative metastatic breast cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) + AI are standard-of-care first-line for HR+/HER2- metastatic breast cancer; ribociclib + letrozole improved OS to 63.9 vs. 51.4 months (MONALEESA-2); abemaciclib approved adjuvantly for high-risk early-stage HR+ disease.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — ERα (ESR1) drives ~70-75% of breast cancers; aromatase inhibitors (anastrozole, letrozole) are first-line adjuvant for postmenopausal ER+ disease; fulvestrant (SERD) degrades ERα; ESR1 LBD mutations (D538G, Y537S) cause AI resistance in metastatic HR+ disease.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — PR+ breast cancers have better prognosis than PR- tumors; combined E2+progestogen HRT (WHI) increased breast cancer risk vs. estrogen-only; progestins in combined OCP contribute to VTE risk; PR agonists (megestrol, medroxyprogesterone) treat endometrial hyperplasia and EC.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — breast cancer bone metastases exploit the RANKL axis: PTHrP from tumor cells → osteoblast RANKL → osteoclast osteolysis releases TGF-β and IGF-1 → vicious cycle of tumor-bone crosstalk; denosumab (Xgeva) delays skeletal-related events by ~8.5 months vs. zoledronate (HALT-BC).
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Breast cancer overexpresses CXCR4 → homing to CXCL12-rich organs (bone marrow, lung, liver, brain) → organ-specific metastasis; stromal CXCL12 promotes primary tumor growth; CXCR4 correlates with lymph node involvement and poor prognosis; anti-CXCR4 therapy in trials.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-2 promotes breast cancer angiogenesis: hypoxic tumor cells secrete Ang-2 → vessel destabilization → VEGF-driven sprouting; tumor Ang-2 correlates with lymph node metastasis and poor prognosis; Ang-2 blockade combined with anti-VEGF shows additive anti-tumor activity.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Breast and endometrial cancers are linked estrogen-driven malignancies: unopposed estrogen fuels both, and tamoxifen—an anti-estrogen in breast tissue—acts as a uterine estrogen agonist, raising endometrial cancer risk; obesity and the hormone milieu tie the two together.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Breast and ovarian cancers are the twin BRCA1/2 tumors of hereditary breast-ovarian cancer syndrome: germline BRCA loss cripples homologous-recombination repair, predisposing to both and making them exquisitely sensitive to PARP inhibitors (olaparib) and platinum chemotherapy.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Bone is the most common site of breast cancer metastasis: tumor cells secrete PTHrP that drives osteoblasts to overproduce RANKL → osteoclast activation → osteolytic destruction and a cycle releasing bone-stored growth factors; denosumab and bisphosphonates target this loop.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — Hereditary breast and ovarian cancer syndrome from germline BRCA1/2 underlies ~5-10% of breast cancers: it brings early-onset, often triple-negative or bilateral tumors, intensified screening and risk-reducing surgery, and platinum/PARP-inhibitor sensitivity.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Li-Fraumeni syndrome is a striking cause of early breast cancer: germline TP53 loss yields breast cancer (often HER2-positive) in women under 30 alongside sarcomas—and because radiotherapy can induce second cancers, treatment favors mastectomy over radiation.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Triple-negative breast cancer is the subtype most responsive to immunotherapy: its higher mutational burden and tumor-infiltrating cytotoxic T cells make it sensitive to PD-1/PD-L1 blockade (pembrolizumab), unlike the immunologically quiet hormone-receptor-positive tumors.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Breast cancer is a core feature of Cowden syndrome: germline PTEN loss unleashing PI3K-AKT gives a high lifetime breast cancer risk alongside thyroid and endometrial cancer—so Cowden is one of the hereditary syndromes screened for in familial breast cancer.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is integral to breast cancer treatment: after lumpectomy, whole-breast or partial radiation halves local recurrence, and post-mastectomy radiation treats high-risk disease—radiation made breast-conserving surgery as safe as mastectomy.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Breast and prostate cancer are the paradigm hormone-driven cancers and share BRCA biology: breast growth depends on estrogen, prostate on androgens (blocked by ADT), and BRCA2 raises risk of both—endocrine therapy is central to each.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — BRCA2 mutation strongly predisposes to breast cancer: this DNA-repair gene, when lost, leaves cells unable to fix double-strand breaks, so hereditary BRCA2 tumors arise young and are exquisitely sensitive to PARP inhibitors that exploit the repair defect.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 blockade has entered breast cancer through its most aggressive subtype: triple-negative tumors carry more mutations and immune infiltrate, so adding anti-PD-1 (pembrolizumab) to chemotherapy improves outcomes where hormonal and HER2 therapies do not apply.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Breast cancer spreads first through the lymphatic system: tumor cells drain to axillary nodes, so sentinel-node biopsy stages the disease and nodal involvement is among the strongest prognostic factors—guiding decisions on radiation and systemic therapy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Breast cancer is a leading source of brain metastases: HER2-positive and triple-negative subtypes especially seed the brain, where the blood-brain barrier shields tumor cells from many drugs—so brain-penetrant agents like tucatinib are changing outcomes.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts shape breast tumors: they build the stiff, desmoplastic stroma that aids invasion, fuels growth signals, and blocks drug delivery and immune access—so the fibroblast-rich microenvironment, not just tumor cells, drives progression.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity worsens breast cancer at both ends: after menopause, fat tissue's aromatase raises estrogen that drives hormone-receptor-positive tumors, and obesity-linked inflammation and insulin resistance worsen prognosis—so weight is a modifiable risk and outcome factor.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a frequent breast-cancer metastatic site: spread there, alongside bone, lung and brain, marks stage IV disease and worsens prognosis, so liver function and imaging are watched—and HR-positive cancers can colonize it years after the primary.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages help breast cancer spread: recruited into the tumor, they promote angiogenesis, invasion and immune evasion, and a macrophage-rich microenvironment predicts worse outcome—making them a target alongside the cancer cells.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is a clear, modifiable breast-cancer risk: even moderate drinking raises risk by increasing estrogen and generating DNA-damaging acetaldehyde, so reducing alcohol is one of the few lifestyle levers proven to lower breast-cancer incidence.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is a frequent home for breast-cancer spread: tumor cells seeded through the blood lodge in its fine capillaries and grow, so lung metastases—as nodules or a diffuse lymphatic pattern—are a common cause of breast-cancer morbidity.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Breast fat fuels the tumor it surrounds: adipocytes in the breast make aromatase that converts androgens to estrogen, feeding hormone-driven cancer, which is part of why obesity raises postmenopausal breast-cancer risk.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Breast cancer hijacks bone's demolition crew: metastatic cells release RANKL and factors that activate osteoclasts to dissolve bone, releasing growth factors that feed the tumor in a vicious cycle behind painful osteolytic lesions.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Breast cancer in bone can flood the blood with calcium: osteolytic metastases dissolve bone faster than the body can clear the released calcium, causing the hypercalcemia of malignancy—confusion, thirst, and kidney injury needing urgent care.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Breast cancer can hide in the bone marrow: single tumor cells lodge there and lie dormant for years, a reservoir of disseminated disease that can reawaken to cause the late relapses unique to this cancer.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help hold breast cancer in check: these innate lymphocytes can detect and destroy tumor cells without prior sensitization, and strong NK activity is linked to fewer metastases and better outcomes.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper fuels breast cancer's spread: tumors need it for new blood vessels and for enzymes that prime metastasis, so copper-lowering drugs have been trialed to keep dormant disease asleep.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Breast cancer can invade the skin: inflammatory breast cancer reddens and dimples it into peau d'orange, and chest-wall skin recurrences signal aggressive local disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Breast tumors build a fibrotic stroma: a dense, desmoplastic scar stiffens the tumor, shows as the spiculated mass on a mammogram, and helps shield the cancer from drugs.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads breast cancer's glandular roots: ductal carcinoma cells retain microvilli-lined intracytoplasmic lumina and secretory features, ultrastructure that confirms epithelial origin when a poorly differentiated tumor is hard to classify.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Breast cancer is the eye's commonest invader: it is the leading source of choroidal metastasis, the tumor seeding the back of the eye to blur vision, sometimes the first hint that the cancer has spread.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Breast cancer recruits platelets to spread: circulating tumor cells cloak themselves in platelets to hide from immune attack and lodge in distant organs, while the tumor also drives the clotting risk that haunts cancer patients.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The chemotherapy bites the nerves: taxanes like paclitaxel, central to breast cancer treatment, injure peripheral sensory neurons into a stocking-glove neuropathy that can force dose cuts and outlast the therapy.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Two breast cancer drugs strain the heart: the HER2 antibody trastuzumab and the anthracyclines can each weaken the myocardium, so cardiac function is monitored before and during treatment to catch a falling ejection fraction.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment reshapes reproductive life: chemotherapy can force premature menopause and infertility, while tamoxifen — protective in the breast — stimulates the uterine lining and raises endometrial cancer risk.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies define and treat the disease: ER, PR, and HER2 immunostains classify every tumor and pick the therapy, and the targeted drugs are antibodies themselves — trastuzumab and pertuzumab against HER2, plus the newer antibody-drug conjugates.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Chemotherapy hammers the marrow: the anthracycline and taxane regimens are myelosuppressive, dropping neutrophil counts so that growth-factor support and febrile-neutropenia vigilance run through treatment.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Lobular breast cancer has a strange destination: the diffuse, single-file invasive lobular type characteristically metastasizes to the stomach and GI tract, sometimes mimicking a primary gastric cancer years after the breast tumor.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Losing p53 marks the hardest breast cancers: TP53 mutation is the rule in triple-negative and Li-Fraumeni-driven disease, unleashing genomic instability and an aggressive course that resists hormone and HER2 therapies.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The cure can wound the heart: anthracyclines and HER2-targeted trastuzumab are cardiotoxic, so cancer-therapy-related heart failure is a key survivorship concern that ties breast oncology to cardiology surveillance.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Tumors recruit Tregs to hide from immunity: regulatory T cells infiltrate the breast tumor microenvironment and suppress the cytotoxic response, a marker of worse prognosis and a barrier to immunotherapy.
- `connects-to` → **[PALB2](../../03-molecular/palb2/README.md)** — Another repair gene joins BRCA: germline PALB2 mutations, which partner BRCA2 in homologous recombination, confer a high breast cancer risk and the same sensitivity to PARP inhibitors, widening who gets genetic testing.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — ER-positive tumors lean on a growth hub: PI3K-AKT-mTOR signaling drives proliferation and resistance to hormone therapy, so the mTOR inhibitor everolimus is added to endocrine treatment when the cancer escapes it.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplification marks the aggressive tumors: MYC is frequently amplified in basal and triple-negative breast cancer, powering relentless proliferation in the subtypes that lack hormonal and HER2 targets.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB drives the hardest-to-treat subtype: constitutive NF-κB signaling supports survival, inflammation and metastasis in ER-negative and triple-negative breast cancer, a pathway studied where hormonal and HER2 targets are absent.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The cancer and its therapy both clot: breast cancer raises thrombosis risk, compounded by tamoxifen and chemotherapy, so deep-vein thrombosis and pulmonary embolism are recognized complications of treatment.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Chemo strips the body's defenses: the cytotoxic regimens used against breast cancer cause neutropenia, making febrile neutropenia and sepsis a recurring hazard of treatment.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Its hormone therapy strips the bone: aromatase inhibitors and ovarian suppression for estrogen-receptor-positive breast cancer cut estrogen sharply, accelerating bone loss so that osteoporosis monitoring and treatment accompany therapy.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Tumor inflammation and chemo blunt the marrow: the IL-6 of advanced breast cancer raises hepcidin while cytotoxic therapy suppresses erythropoiesis, adding an anemia-of-chronic-disease component to treatment cytopenias.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — The diagnosis and its toll weigh on mood: depression is common across the breast-cancer journey, driven by the threat to life, the effects of surgery and chemotherapy, and the menopausal symptoms of endocrine therapy.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Treatment leaves nerves aching: taxane chemotherapy causes peripheral neuropathy, mastectomy can produce post-surgical neuropathic pain, and aromatase inhibitors bring disabling arthralgias.
- `connects-to` → **[Stroke](../stroke/README.md)** — Cancer and its therapy raise clot risk to the brain: the hypercoagulable state of malignancy, tamoxifen's thrombotic risk and chest radiation's vascular damage together raise the risk of ischemic stroke.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its chemotherapy opens the lung to mold: the neutropenia from breast-cancer chemotherapy can let inhaled Aspergillus invade as pulmonary aspergillosis, particularly with dose-dense regimens.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Most breast cancer is hormone-driven: oestrogen-receptor-positive tumours grow on oestrogen, so endocrine therapy with tamoxifen or aromatase inhibitors is central, bringing menopausal symptoms and bone loss.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Mastectomy and radiation heal slowly: breast surgery with reconstruction and axillary dissection leaves wounds prone to seroma and infection, and prior or adjuvant radiation impairs tissue healing.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Recurrence fear breeds chronic worry: the scan and tumour-marker surveillance, body-image change and dread of relapse in breast cancer foster persistent health anxiety alongside depression.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Bone is its favourite distant home: breast cancer most often metastasises to the skeleton, causing bone pain, pathological fractures, hypercalcaemia and spinal cord compression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to lung and pleura: breast cancer commonly metastasises to the lungs and pleura, producing nodules and malignant pleural effusions with breathlessness.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It reaches the brain: HER2-positive and triple-negative breast cancers in particular metastasise to the brain and leptomeninges, causing headaches, seizures and focal deficits.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its treatments are cardiotoxic: anthracyclines and HER2-targeted trastuzumab can weaken the heart muscle, and radiation to the left breast raises later coronary disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It declares itself on the skin: inflammatory breast cancer gives a peau d'orange dimpling, Paget disease scales the nipple, and chest-wall recurrences seed skin nodules.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can spread to the gut: lobular breast cancer in particular metastasises to the stomach and bowel, while chemotherapy and endocrine therapy bring nausea and hepatotoxicity.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Molecular subtyping drives its treatment: HER2 antibodies (trastuzumab, pertuzumab, T-DXd), CDK4/6 inhibitors for hormone-receptor-positive disease and PARP inhibitors for BRCA-mutant tumours are central to modern breast cancer care.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune microenvironment shapes outcome: tumour-infiltrating lymphocytes predict response in triple-negative breast cancer, where checkpoint inhibitors added to chemotherapy now improve survival.
- `connects-to` → **[Sulforaphane](../../../03-medicine/03-food/sulforaphane/README.md)** — Diet is studied for prevention: cruciferous-vegetable sulforaphane is investigated for breast cancer chemoprevention through effects on oestrogen metabolism and tumour-cell signalling.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Anthracyclines and taxanes anchor it: cytotoxic chemotherapy with anthracyclines and taxanes is given neoadjuvantly or adjuvantly across breast cancer subtypes, especially triple-negative and node-positive disease, alongside targeted and endocrine therapy.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Bone is its favourite metastatic site: breast cancer spreads to bone as RANKL-driven osteolytic metastases causing pain and fractures, while aromatase inhibitors add their own bone loss — both countered by bisphosphonates and denosumab.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Its treatment can injure the heart: anthracyclines cause dose-dependent cardiomyopathy and trastuzumab a usually reversible cardiac dysfunction, so monitoring myocardial function is central to cardio-oncology in breast cancer.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — CDH1 links breast and stomach: germline loss of E-cadherin (CDH1) causes hereditary diffuse gastric cancer together with lobular breast cancer, so CDH1 carriers undergo breast surveillance and risk-reducing surgery.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Lymphoid islands predict its immunotherapy response: triple-negative breast cancers that form tertiary lymphoid structures with germinal-centre B cells respond better to checkpoint blockade.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Shared BRCA vulnerability: BRCA1/2 and PALB2-mutant breast and pancreatic cancers both respond to PARP inhibitors and platinum chemotherapy, within the HBOC spectrum of homologous-recombination-deficient tumours.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver as a metastatic site: breast cancer commonly spreads to the liver, seeding the hepatic lobules, and luminal subtypes can present with liver-dominant metastatic disease years after the primary.
- `connects-to` → **[AML](../aml/README.md)** — Therapy-related leukaemia: the alkylators, anthracyclines and radiation that cure breast cancer can seed a secondary, poor-prognosis AML or MDS years later, a late cost of cytotoxic treatment.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — A shared BRCA2 spectrum: germline BRCA2 raises the risk of breast cancer alongside ovarian, prostate, pancreatic cancer and melanoma, a hereditary cancer cluster that guides cascade genetic testing.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Seizures from brain spread: breast cancer (especially HER2-positive and triple-negative) is a leading cause of brain metastases and leptomeningeal disease, producing seizures and secondary epilepsy.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Nerve and cord compromise: bone-tropic breast cancer can collapse vertebrae and compress the spinal cord and nerve roots, while tumour or radiation can injure the brachial plexus—threatening permanent deficits.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Immunotherapy's autoimmune cost: checkpoint inhibitors now used for triple-negative breast cancer can unleash an autoimmune colitis resembling inflammatory bowel disease, managed with steroids and anti-TNF biologics.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT axis: AKT, activated downstream of PIK3CA and HER2, drives breast cancer growth and survival and underlies resistance to endocrine therapy, making AKT inhibitors a targeted option.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic aggression: HIF-1α stabilised in hypoxic breast tumours promotes angiogenesis, metastasis and treatment resistance, and marks the more aggressive triple-negative subtypes.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Tumour angiogenesis: VEGF drives the new-vessel growth that feeds breast tumour expansion and metastasis, a hallmark exploited by anti-angiogenic therapy.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Amplified cell-cycle driver: CCND1 (cyclin D1) is amplified in many ER-positive breast cancers, partnering CDK4/6 to push proliferation and underpinning sensitivity to CDK4/6 inhibitors.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Metastatic switch: TGF-beta turns from tumour suppressor to driver of epithelial-mesenchymal transition, immune evasion and bone-metastatic spread in advancing breast cancer.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 secreted by breast tumours draws tumour-associated macrophages that promote angiogenesis, immune suppression and metastatic seeding of the lung.
- `connects-to` → **[E-cadherin (CDH1)](../../03-molecular/cdh1/README.md)** — Loss of E-cadherin (CDH1) defines invasive lobular carcinoma, producing its single-file infiltrative growth and discohesive cells that make it hard to detect on imaging and prone to diffuse, late-presenting spread.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — BRCA-mutant and homologous-recombination-deficient breast cancers depend on RAD51-mediated repair, whose deficiency confers the synthetic-lethal sensitivity to PARP inhibitors (olaparib, talazoparib) now used in germline-BRCA disease.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — The androgen receptor is expressed in many breast cancers and defines the luminal-androgen-receptor triple-negative subtype, where AR-targeted therapy is being investigated as an alternative to chemotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — BRCA-mutant, homologous-recombination-deficient breast cancers accumulate cytosolic DNA that activates cGAS-STING, the innate-immune basis for combining PARP inhibitors with checkpoint blockade in triple-negative disease.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR1 amplification is a recurrent event in ER-positive breast cancer that drives resistance to endocrine therapy by providing an alternative growth signal, making FGFR a target to restore sensitivity to hormonal treatment.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch signaling sustains the breast-cancer stem-cell population that resists chemotherapy and endocrine therapy and seeds recurrence, a developmental pathway driving treatment resistance and a target under investigation.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates the PI3K-AKT-mTOR pathway (PIK3CA, AKT and mTOR already mapped) in breast cancer and is a major mechanism of resistance to endocrine and HER2-targeted therapy.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6-RB-E2F axis (CDK4/6 and cyclin-D1 already mapped) drives proliferation in ER-positive breast cancer, the pathway whose blockade by CDK4/6 inhibitors transformed its treatment.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-MAPK-ERK signaling crosstalks with estrogen-receptor signaling and is a route of acquired resistance to endocrine therapy in breast cancer.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1R signaling crosstalks with the estrogen receptor and HER2 (both mapped), driving acquired resistance to endocrine and HER2-targeted therapy in breast cancer.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt/β-catenin signaling sustains the breast-cancer stem-cell compartment and is especially active in triple-negative breast cancer, contributing to recurrence.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 amplification suppresses p53 (mapped), an alternative to outright TP53 mutation that disables the apoptotic checkpoint in breast cancer.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) is a context-dependent regulator in breast cancer, switching from tumor suppression to promotion of EMT and metastasis.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 expression, driven by estrogen-receptor signaling (estrogen mapped), promotes survival of luminal breast cancer cells and carries prognostic significance.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-JAK-STAT3 signaling supports breast cancer stem-cell maintenance, proliferation and immune evasion.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports immune evasion and the metastatic colonization that drives mortality in breast cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of breast cancer, particularly the immunotherapy-relevant triple-negative subtype.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression silences tumor-suppressor genes and contributes to the epigenetic dysregulation and aggressiveness of breast cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-driven FOXO inactivation (PTEN, AKT, and PIK3CA already mapped) removes a tumor-suppressive, pro-apoptotic brake in breast cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that breast cancer, especially the triple-negative subtype, must evade.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from myeloid-derived suppressor cells promote the pre-metastatic niche and immunosuppression of breast cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates β-catenin and cyclin-D1 stability (Wnt and cyclin-D1 already mapped), modulating the survival and proliferation signaling of breast cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of ER, HER2, and growth-factor receptors drives the invasion and endocrine-therapy resistance of breast cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of tumor-suppressor genes in breast cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and endocrine/chemotherapy resistance of breast cancer cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of breast cancer, a candidate metformin target.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven macrophage recruitment shapes the pro-metastatic microenvironment of breast cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of breast cancer.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of breast cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment and bone-metastatic progression of breast cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of breast cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of breast cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of breast cancer.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — TNBC immunotherapy: triple-negative breast cancer, lacking hormone and HER2 targets, is the subtype most responsive to checkpoint inhibitors, and MHC class II antigen presentation with tumour-infiltrating lymphocytes predicts that immune response.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Therapy resistance: the AXL receptor tyrosine kinase drives epithelial-mesenchymal transition, metastasis and resistance to endocrine and targeted therapy in breast cancer, a candidate target for reversing treatment escape.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity risk: obesity raises postmenopausal breast-cancer risk through adipose aromatase-derived estrogen (already mapped) and the adipokine leptin, which promotes tumour-cell proliferation, linking metabolism to breast carcinogenesis.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiotoxicity: HER2-directed trastuzumab (already mapped) and anthracycline chemotherapy are cardiotoxic, and troponin elevation helps detect the myocardial injury that limits these effective breast-cancer treatments.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Immunotherapy: IL-2-driven T-cell responses underlie the tumour-infiltrating lymphocytes and checkpoint benefit (PD-1 already mapped) seen mainly in triple-negative breast cancer, the immunogenic subset where immunotherapy is effective.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Chemotherapy anaemia: breast-cancer chemotherapy is myelosuppressive and lowers haemoglobin, and marrow replacement by metastatic disease compounds the anaemia that contributes to fatigue in advanced breast cancer.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammation-estrogen link: cyclooxygenase-2-derived prostaglandin E2 in the breast tumour and adipose stroma induces aromatase and local estrogen (already mapped) synthesis, linking inflammation to the hormone drive of estrogen-receptor-positive breast cancer.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), part of the immune evasion that limits checkpoint benefit outside the immunogenic triple-negative subset.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and lysis stress: the chemotherapy of breast cancer generates oxidative stress and cell lysis releasing purines that xanthine oxidase converts to uric acid, adding an oxidative and tumour-lysis burden to treatment.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of breast cancer outside the immunogenic triple-negative subset.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia of therapy: the chemotherapy and advanced disease of breast cancer cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Obesity and breast cancer: obesity, through the adipokines leptin (already mapped) and the fall in adiponectin, and through the aromatase-driven oestrogen (already mapped), raises the risk and worsens the prognosis of postmenopausal breast cancer.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of breast cancer, promoting the metastasis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages (CCL2 already mapped) of the breast-cancer stroma, in their M2 (IL-4 already mapped) phenotype, drive the immunosuppression, angiogenesis (VEGF already mapped) and metastasis.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts: the CAFs (TGF-β and PDGF already mapped) of the breast-cancer stroma drive the desmoplasia, the immune exclusion and the progression of the tumour.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity risk of the postmenopausal (estrogen already mapped) breast cancer.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hepatic metastases: the liver is a common site of breast-cancer metastasis, the visceral disease of poorer prognosis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Mammary adipose niche: the mammary adipocytes (the source of leptin, adiponectin and resistin already mapped and the local aromatase oestrogen) form the tumour microenvironment driving the breast-cancer progression.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of triple-negative breast cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the breast-cancer immune microenvironment.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of breast cancer.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of breast cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of breast cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the breast-cancer microenvironment (and the emerging AllergoOncology anti-tumour IgE).
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of breast cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the intratumoural tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts the response to the immunotherapy of breast cancer (especially triple-negative).
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the tumour-promoting-versus-protective immune balance of breast cancer.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^siegel-2024-cancer-statistics]: Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. *CA Cancer J Clin.* 2024;74(1):12-49. [doi:10.3322/caac.21820](https://doi.org/10.3322/caac.21820) · [PubMed 38230766](https://pubmed.ncbi.nlm.nih.gov/38230766/)
[^slamon-2001-trastuzumab-trial]: Slamon DJ, Leyland-Jones B, Shak S, et al. Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. *N Engl J Med.* 2001;344(11):783-792. [doi:10.1056/NEJM200103153441101](https://doi.org/10.1056/NEJM200103153441101) · [PubMed 11248153](https://pubmed.ncbi.nlm.nih.gov/11248153/)
[^finn-2016-palbociclib-paloma2]: Finn RS, Martin M, Rugo HS, et al. Palbociclib and letrozole in advanced breast cancer. *N Engl J Med.* 2016;375(20):1925-1936. [doi:10.1056/NEJMoa1607303](https://doi.org/10.1056/NEJMoa1607303) · [PubMed 27959613](https://pubmed.ncbi.nlm.nih.gov/27959613/)
