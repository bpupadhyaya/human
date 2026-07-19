---
schema: human-scale-entry/v1
id: hereditary-breast-ovarian-cancer
name: Hereditary Breast and Ovarian Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary breast and ovarian cancer syndrome (HBOC) is caused by germline BRCA1/2, PALB2, ATM, or CHEK2 variants; BRCA1 lifetime breast risk ~70%, ovarian ~44%; PARP inhibitors approved across cancer types; risk-reducing surgery (mastectomy/BSO) is standard."
aliases: ["HBOC", "hereditary breast and ovarian cancer", "BRCA syndrome", "BRCA1 BRCA2 syndrome", "hereditary breast cancer", "germline BRCA", "HBOC syndrome", "BRCA1 germline", "familial breast cancer"]
sources:
  - id: kuchenbaecker-2017-brca-risks
    type: peer-reviewed
    cite: "Kuchenbaecker KB, Hopper JL, Barnes DR, et al. Risks of Breast, Ovarian, and Contralateral Breast Cancer for BRCA1 and BRCA2 Mutation Carriers. JAMA. 2017;317(23):2402-2416."
    doi: "10.1001/jama.2017.7112"
    pmid: "28632853"
    url: "https://doi.org/10.1001/jama.2017.7112"
  - id: antoniou-2014-palb2-risk
    type: peer-reviewed
    cite: "Antoniou AC, Casadei S, Heikkinen T, et al. Breast-cancer risk in families with mutations in PALB2. N Engl J Med. 2014;371(6):497-506."
    doi: "10.1056/NEJMoa1400382"
    pmid: "25099575"
    url: "https://doi.org/10.1056/NEJMoa1400382"
cross_links:
  - target: 01-human/03-molecular/palb2
    relation: connects-to
    note: "Germline PALB2 pathogenic variants confer ~35-65% lifetime breast cancer risk (second after BRCA1/2); ~5-10% ovarian cancer risk (primarily HGSOC); biallelic PALB2 = Fanconi anemia FA-N; PARP inhibitors are active in PALB2-germline breast and pancreatic cancer."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1 germline variants confer the highest hereditary breast cancer risk (~55-72% lifetime) and ovarian cancer risk (~44%); BRCA1-mutant tumors are often triple-negative (ER-/PR-/HER2-) and high-grade; risk-reducing BSO at age 35 and bilateral mastectomy are standard options."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "BRCA2 germline variants confer ~45-69% lifetime breast cancer risk and ~17% ovarian cancer risk (lower than BRCA1); BRCA2-mutant breast cancer is often ER+/HER2-; olaparib and niraparib FDA-approved for BRCA-mutant metastatic breast cancer; risk-reducing BSO at age 40-45."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "HBOC-associated ovarian cancer is predominantly high-grade serous carcinoma (HGSOC); BRCA1 germline: 44% lifetime risk; BRCA2: 17%; PALB2/RAD51C/D: 5-10%; bilateral salpingo-oophorectomy (BSO) at age 35-40 reduces ovarian cancer mortality; PARP inhibitors in maintenance."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Germline ATM pathogenic variants confer ~20-30% lifetime breast cancer risk; elevated prostate (~6%) and pancreatic risk; biallelic ATM = ataxia-telangiectasia; ATM-germline BC is often ER+/luminal; NCCN recommends breast MRI from age 40 for ATM heterozygotes with family history."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "BRCA2 loads RAD51 monomers onto ssDNA at DSBs via eight BRC repeats → RAD51 filament → strand invasion (HR repair); BRCA2 LOF → RAD51 loading failure → error-prone NHEJ/MMEJ → tumorigenesis; RAD51 paralogs (RAD51C, RAD51D) each confer ~10-15% lifetime ovarian cancer risk in HBOC."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "HBOC causes ~5-10% of breast cancer; BRCA1-associated BC is predominantly TNBC (~60-80%) with peak onset at 30-40 years; BRCA2-associated BC is predominantly ER+ (~60-70%); olaparib (OlympiAD) and talazoparib (EMBRACA) are FDA-approved for germline BRCA1/2 HER2-neg metastatic BC."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "HBOC and Li-Fraumeni are the major hereditary breast cancer syndromes but differ in scope: HBOC (BRCA1/2) focuses on breast and ovarian cancer with PARP sensitivity, while LFS (germline TP53) spans sarcomas, brain tumors, and adrenocortical carcinoma — focused vs multi-cancer."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "BRCA2 (and to a lesser degree BRCA1, PALB2, ATM) raises pancreatic cancer risk ~3-7×, extending HBOC beyond breast and ovary; these HR-deficient pancreatic cancers respond to platinum and PARP-inhibitor maintenance (olaparib, POLO), so germline testing now guides therapy."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "BRCA2 carriers face ~2-6× prostate cancer risk with more aggressive, earlier-onset disease; HBOC thus affects men too, and BRCA/HR-deficient metastatic prostate cancer responds to PARP inhibitors (olaparib, PROfound) — making germline and tumor testing standard in advanced cases."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "BRCA2 widens the hereditary breast-ovarian cancer spectrum to melanoma: germline BRCA2 modestly raises risk of cutaneous and especially uveal melanoma alongside breast, ovarian, pancreatic and prostate cancer, so a melanoma history can inform BRCA testing."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hereditary breast-ovarian cancer strikes the reproductive system hardest: BRCA1/2 carriers face high lifetime risks of breast, ovarian and fallopian-tube cancer, so risk-reducing salpingo-oophorectomy and enhanced breast surveillance are cornerstones of management."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: treated-by
    note: "Hereditary breast-ovarian cancer is the paradigm for synthetic-lethal targeted therapy: BRCA1/2-mutant tumors cannot repair DNA by homologous recombination, so PARP inhibitors (olaparib) blocking backup repair selectively kill them—turning the germline defect into a drug target."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "HBOC and Lynch syndrome are major hereditary cancers raising women's ovarian/endometrial risk via different repair defects: HBOC from BRCA1/2 homologous-recombination loss, Lynch from mismatch-repair loss—each guides distinct screening and surgery."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "HBOC and Cowden syndrome both sharply raise hereditary breast cancer risk through different genes: HBOC via BRCA1/2 (homologous-recombination repair), Cowden via PTEN (PI3K-AKT pathway)—PTEN also brings thyroid and endometrial cancer plus hamartomas."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "HBOC and Peutz-Jeghers both elevate breast cancer risk through different mechanisms: HBOC from BRCA1/2 DNA-repair loss, PJS from STK11 loss—PJS also raises ovarian (sex-cord) and GI cancer risk, so both warrant intensified breast surveillance from a young age."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen exposure modulates HBOC risk: BRCA-driven breast cancers often still respond to hormonal signaling, and reducing estrogen—via risk-reducing oophorectomy or endocrine therapy—lowers cancer risk, so the lifetime estrogen burden shapes when these cancers arise."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "HBOC carries a modest endometrial cancer risk: BRCA1 carriers, especially after tamoxifen, have a slightly raised risk of serous endometrial cancer, so gynecologic surveillance and decisions about hysterectomy at oophorectomy are part of managing the syndrome."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "BRCA-mutant cells are radiosensitive from impaired DNA repair: their inability to fix double-strand breaks makes ionizing radiation more damaging, a reason young carriers are screened with non-ionizing MRI rather than repeated mammography."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "HBOC overlaps with the p53-driven Li-Fraumeni spectrum of inherited cancer: BRCA loss cripples DNA double-strand-break repair while TP53 loss removes the damage checkpoint, so both germline defects in the genome-guardian network produce familial breast and other cancers."
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "HBOC belongs to the family of DNA-repair cancer syndromes like Bloom: BRCA1/2 run homologous recombination just as BLM helicase resolves recombination intermediates, so loss of either destabilizes the genome—a shared theme of repair failure driving cancer."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "BRCA-mutant tumors engage the immune system distinctively: defective DNA repair raises mutational load and neoantigens, making some HBOC cancers more immunogenic—so checkpoint immunotherapy is explored alongside the PARP inhibitors that exploit the repair defect."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "HBOC overlaps another hereditary breast syndrome via CDH1: while BRCA carriers get ductal breast cancer, CDH1 (hereditary diffuse gastric cancer) carriers develop lobular breast cancer, so inherited breast-cancer risk spans more than one gene and tumor type."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "HBOC sits among the DNA-repair cancer syndromes alongside MUTYH-associated polyposis: HBOC stems from broken homologous recombination and MAP from faulty base-excision repair, so both show how losing a specific repair pathway seeds inherited cancer."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Tumor-infiltrating cytotoxic T cells track BRCA tumors' outcomes: HRD cancers, especially triple-negative breast and high-grade ovarian, often draw dense T-cell infiltrates that predict better prognosis and chemo response—so immune contexture is a built-in biomarker."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "BRCA1 breast cancer is fueled by progesterone signaling: the hormone drives RANKL and proliferation in mammary stem cells primed by BRCA1 loss, which is why anti-progesterone strategies are studied to prevent cancer in carriers."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "BRCA1 tumors are usually triple-negative, lacking HER2: unlike many breast cancers they express neither HER2 nor hormone receptors, so they miss those targeted drugs and instead rely on chemotherapy and PARP inhibitors against their DNA-repair defect."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "BRCA-mutant cancers are more immunogenic but shielded by regulatory T cells: their crippled DNA repair generates many neoantigens, yet Tregs blunt the response—so combining PARP inhibitors with immunotherapy aims to tip the balance."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "HBOC reaches beyond breast and ovary to the pancreas: BRCA2 (and BRCA1) carriers face higher pancreatic cancer risk, and these tumors' DNA-repair defect makes them responsive to platinum chemotherapy and PARP inhibitors."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "BRCA-related ovarian cancers lean on VEGF for blood supply: the angiogenesis driver fuels their growth and ascites, so anti-VEGF bevacizumab is combined with chemotherapy and PARP inhibitors in these tumors."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells aid the attack on BRCA-mutant tumors: their DNA-repair defect spawns neoantigens and stress signals that NK cells sense, and antibody therapies like trastuzumab recruit NK killing against HER2-positive BRCA breast cancers."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "BRCA-related ovarian cancers recruit endothelial cells: VEGF drives these vessel-lining cells to build the vasculature feeding the tumor and its ascites, the target of the bevacizumab added to therapy."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Treating HBOC cancers can strain the bone marrow: the PARP inhibitors exploiting BRCA's repair defect suppress marrow blood production and, rarely, trigger secondary MDS or leukemia, so counts are watched."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "HBOC reaches the skin through melanoma risk: BRCA2 carriers face a raised chance of melanoma alongside breast, ovarian, and pancreatic cancer, so skin surveillance joins their screening."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts shape HBOC tumors: they build the stroma of BRCA breast and ovarian cancers, influencing how the tumor grows and how well drugs reach it."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "HBOC tumors and their treatment leave fibrosis: a desmoplastic stroma surrounds the cancers, and radiation and surgery scar the breast and pelvis, lasting effects survivors carry."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Breast cancers often announce themselves as microcalcifications: clusters of calcium specks on a mammogram are an early sign that prompts biopsy, central to screening BRCA carriers."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "BRCA loss leaves cells unable to mend broken DNA: without homologous recombination, the double-strand breaks that radiation and chemotherapy inflict go unrepaired — a weakness PARP inhibitors exploit to kill the cancer by synthetic lethality."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "BRCA-driven cancers reach for the brain: BRCA-mutant breast and ovarian tumors, often triple-negative, carry a notable tendency to seed central-nervous-system metastases, prompting vigilance for brain spread."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a frequent destination as BRCA cancers spread: hematogenous metastases from the breast, ovarian, and pancreatic tumors of the syndrome lodge there, marking advanced disease."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The targeted drugs thin the blood: PARP inhibitors like olaparib — which exploit the BRCA repair defect — commonly cause anemia by suppressing the marrow, and carry a small long-term risk of MDS and leukemia."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "BRCA tumors are platinum- and taxane-sensitive, at a neural cost: the carboplatin and paclitaxel used against them injure peripheral sensory neurons into a numbing, tingling neuropathy."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Immunotherapy suits the BRCA1 breast cancers: many are triple-negative and respond to checkpoint antibodies like pembrolizumab, harnessing the antibody-driven immune system against tumors hard to target otherwise."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The targeted drugs squeeze the marrow: PARP inhibitors like olaparib and niraparib commonly drop platelet and red-cell counts, so blood counts are watched closely and doses adjusted through the long maintenance courses these carriers take."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The treatments can seed a second cancer: years of platinum chemotherapy and PARP-inhibitor maintenance carry a small but real risk of therapy-related myelodysplastic syndrome and leukemia, a sobering late cost of controlling the solid tumors."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Risk-reducing surgery brings early menopause: removing the ovaries and tubes in a young BRCA carrier abruptly cuts off estrogen, accelerating bone loss toward osteoporosis unless hormone or bone-protective therapy is considered."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K offers a second target alongside the BRCA defect: PIK3CA mutations are common in BRCA-associated breast cancers, so PI3K-AKT inhibitors are combined with the PARP drugs that exploit the homologous-recombination flaw."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Broken DNA repair makes a visible tumor: BRCA loss spawns genomic instability and neoantigens that dendritic cells can present, making these cancers more immunogenic and a rationale for combining PARP inhibitors with immunotherapy."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "BRCA's reach extends to the bile ducts: BRCA2 (and BRCA1) carriers face a raised risk of cholangiocarcinoma, and these homologous-recombination-deficient biliary tumors may respond to platinum and PARP therapy."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "BRCA2 widens the cancer net to the stomach: carriers, especially of BRCA2, face an increased risk of gastric cancer, one of the extra-breast/ovarian tumors that shape the surveillance of these families."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "The therapy can end in leukemia: years of platinum chemotherapy and PARP-inhibitor maintenance occasionally cause therapy-related acute myeloid leukemia, the frank-leukemia end of the marrow damage these treatments inflict."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC amplification drives the BRCA1 tumor: the basal-like, triple-negative breast cancers typical of BRCA1 carriers frequently amplify MYC, adding a proliferative push to the homologous-recombination defect."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its cancers and their treatment clot the blood: the breast and especially ovarian cancers of HBOC carriers are strongly prothrombotic, and the surgery and chemotherapy they require make venous thromboembolism a major hazard."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Chemo empties the marrow's defenses: the platinum and taxane regimens used against HBOC-related cancers cause neutropenia, so febrile neutropenia and sepsis are recurrent treatment dangers."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Cancer and chemo wear down the blood: the advanced ovarian and breast cancers of HBOC carriers, with their chronic inflammation and marrow-suppressing therapy, commonly cause an anemia of chronic disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Carrying the mutation weighs on the mind: learning of a high inherited cancer risk and facing prophylactic mastectomy and oophorectomy impose a heavy psychological burden, with depression common among carriers."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Breast-cancer therapy can wound the heart: the anthracyclines and HER2-directed trastuzumab used to treat cancers in HBOC carriers are cardiotoxic, risking a cardiomyopathy and heart failure."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Platinum chemo strains the kidney: the cisplatin and carboplatin central to treating the ovarian cancers of HBOC carriers are nephrotoxic, and cumulative exposure can leave chronic kidney impairment."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A genetic verdict and hard choices breed worry: learning of a BRCA mutation, weighing risk-reducing mastectomy and oophorectomy, and lifelong screening foster chronic health anxiety in HBOC carriers."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its chemotherapy injures the nerves: the platinum and taxane chemotherapy and post-mastectomy surgery in HBOC carriers cause peripheral and post-surgical neuropathic pain."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemotherapy opens the lung to mold: the neutropenia from chemotherapy for the breast and ovarian cancers of HBOC carriers can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Risk-reducing surgery means major wounds: prophylactic mastectomy with reconstruction and salpingo-oophorectomy in HBOC carriers leave surgical wounds, sometimes irradiated, that must heal."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Removing the ovaries forces early menopause: the risk-reducing salpingo-oophorectomy recommended to BRCA carriers triggers abrupt surgical menopause with its hormonal, bone and cardiovascular consequences."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its drugs and its genes reach the gut: PARP inhibitors and platinum used in BRCA-mutant cancers cause nausea and GI toxicity, and BRCA mutations also raise pancreatic and other GI cancer risk."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Risk reduction and treatment burden the heart: prophylactic oophorectomy induces premature menopause that raises cardiovascular risk, and anthracycline and HER2 therapy for BRCA breast cancer is cardiotoxic."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its cancers travel through the nodes: BRCA-associated breast and ovarian cancers spread to lymph nodes, and axillary surgery for breast cancer causes arm lymphoedema."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It favours the brain and harms the nerves: BRCA1 breast cancers are often triple-negative with a propensity for brain metastasis, and platinum and taxane chemotherapy cause peripheral neuropathy."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It widens the cancer spectrum to the skin: BRCA2 carriers have an increased risk of melanoma, adding the skin to the breast, ovary, pancreas and prostate in BRCA-related cancer."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its cancers spread to bone: the breast and prostate cancers driven by BRCA mutations frequently metastasise to the skeleton, causing pain and fractures."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Advanced disease reaches the lungs: BRCA-related breast and ovarian cancers metastasise to the lungs and pleura, causing effusions and breathlessness."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "BRCA tumours are platinum-sensitive: homologous-recombination deficiency from BRCA1/2 loss makes these breast, ovarian and pancreatic cancers exquisitely sensitive to platinum chemotherapy."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Genomic instability invites immunotherapy: BRCA/HRD tumours carry more neoantigens, and checkpoint inhibitors, often with PARP inhibitors, benefit triple-negative breast and ovarian cancers in HBOC."
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "A fellow genomic-instability syndrome: like Rothmund-Thomson, hereditary breast-ovarian cancer stems from defective DNA repair, both belonging to the family of inherited genome-instability cancer predispositions."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Gatekeeper versus caretaker: FAP is driven by loss of the APC gatekeeper that restrains tissue growth, whereas HBOC arises from loss of BRCA caretaker genes guarding genome integrity—the classic two categories of tumour-suppressor gene."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Knudson's two-hit rule applies to both: retinoblastoma defined the model in which a germline first hit plus somatic loss of the second allele triggers cancer, exactly how BRCA1/2 carriers in HBOC lose their remaining wild-type allele in the tumour."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Two gynaecological cancers, opposite prevention: cervical cancer is HPV-driven and largely prevented by vaccination and screening, whereas HBOC ovarian cancer is germline-driven with no good screening, so management turns to risk-reducing surgery."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Genome-instability cancer syndromes: like Werner syndrome's RecQ-helicase defect, BRCA-driven HBOC reflects failed genome maintenance, predisposing to cancer through accumulated unrepaired DNA damage."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Biallelic BRCA2 is Fanconi anaemia: inheriting two faulty BRCA2/FANCD1 alleles causes Fanconi anaemia with childhood bone-marrow failure—the recessive extreme of an HBOC gene."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "Which ovarian cancer it causes: BRCA-associated ovarian cancer is high-grade serous, biologically distinct from the ARID1A-driven clear-cell subtype that arises from endometriosis."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "BRCA2 and eye melanoma: germline BRCA2 mutations modestly raise the risk of uveal melanoma alongside the cutaneous melanoma of the broader BRCA2 cancer spectrum."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Surgical menopause and bone: risk-reducing oophorectomy in BRCA carriers brings early oestrogen loss that accelerates cortical-bone loss and osteoporosis—a trade-off of cancer prevention."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Treatment cardiotoxicity: anthracyclines and HER2-targeted trastuzumab used for BRCA-associated breast cancer can injure the myocardium, a survivorship concern alongside cure."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle therapy: CDK4/6 inhibitors are a mainstay for hormone-receptor-positive breast cancers, including many that arise in BRCA carriers, blocking cyclin-driven proliferation."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT targeting: AKT-pathway activation in BRCA-associated breast cancer is targetable with AKT inhibitors such as capivasertib, complementing PARP and endocrine therapy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR blockade: mTOR inhibitors like everolimus add benefit in hormone-receptor-positive breast cancer, part of the layered targeting of these BRCA-spectrum tumours."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic aggression: HIF-1α stabilised in the often hypoxic, triple-negative BRCA1-associated tumours drives angiogenesis and a metastatic, treatment-resistant phenotype."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic driver: EZH2 overexpression cooperates with BRCA loss in HBOC tumours, silencing tumour-suppressor genes and offering an epigenetic therapeutic target."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT reactivation maintains telomeres in the genomically unstable BRCA-mutant tumours, enabling the limitless proliferation of HBOC cancers."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Immunogenic HRD tumours: homologous-recombination-deficient BRCA-mutant cancers carry a high neoantigen load that, with their genomic scarring, makes them more responsive to PD-1 checkpoint immunotherapy."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cooperating tumour suppressor: CDKN2A loss accompanies BRCA mutation in HBOC tumours, releasing the cell-cycle brake to accelerate the proliferation of genomically unstable cells."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into HBOC breast and ovarian tumours, contributing to the stroma that shapes growth and immunotherapy response."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "BRCA1-RANKL axis: RANK/RANKL signalling drives the proliferation of BRCA1-mutant mammary progenitor cells, the cells of origin of basal-like breast cancer — the basis for testing denosumab as chemoprevention in BRCA1 carriers."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "HRD cytosolic DNA: the homologous-recombination deficiency of BRCA-mutant cancers produces micronuclei and cytosolic DNA that activate cGAS-STING, an innate-immune mechanism behind combining PARP inhibitors with immunotherapy."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic homing: the CXCL12-CXCR4 axis drives the metastasis of the triple-negative breast and high-grade serous ovarian cancers that BRCA carriers develop, a chemokine route to their characteristic spread."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Synthetic-lethal apoptosis: PARP inhibitors and platinum exploit the homologous-recombination defect of BRCA-mutant tumours to drive lethal DNA damage and caspase-3-mediated apoptosis, the synthetic-lethal killing central to treating HBOC cancers."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy: the high genomic instability of BRCA-mutant, homologous-recombination-deficient tumours makes them more immunogenic, and checkpoint blockade unleashing perforin-mediated cytotoxic killing is active in triple-negative breast cancer."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Subtype heterogeneity: a fraction of the triple-negative breast cancers BRCA carriers develop are of the luminal-androgen-receptor subtype, where AR-targeted therapy is being explored, reflecting the molecular diversity within the disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Cooperating PI3K hit: PTEN loss activates the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped), a frequent cooperating event in BRCA-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Repair-proliferation link: the cyclin-D-CDK4/6 axis (CDK4/6 and CDKN2A already mapped) releases E2F1, which itself transactivates homologous-recombination genes including BRCA1 and RAD51 (both mapped), tying proliferation to the repair pathway lost in HBOC."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Basal-like biology: the triple-negative, basal-like breast cancers that predominate in BRCA1 carriers frequently express EGFR, a hallmark of the basal phenotype and a candidate therapeutic target."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 regulation: MDM2 negatively regulates p53 (already mapped), and its dysregulation cooperates with the homologous-recombination defects of BRCA-mutant tumours to permit survival of genomically unstable cells."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle disruption: the RB1-E2F checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) is frequently disrupted in BRCA-associated basal-like breast and high-grade serous ovarian cancer, driving proliferation."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Hormonal survival: estrogen-induced anti-apoptotic BCL-2 supports the survival of the hormone-receptor-positive breast cancers arising in HBOC, balancing the caspase-3 apoptosis already mapped."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes invasion and immune evasion in the breast and ovarian cancers of hereditary breast-ovarian cancer syndrome."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling, a context-dependent regulator, shapes EMT, invasion and the immunosuppressive microenvironment in BRCA-associated cancers."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling downstream of EGFR/HER2 (both mapped) provides a proliferative input in BRCA-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "BRCA deficiency floods the cytosol with DNA that activates cGAS-STING (mapped) and IFN-STAT1 signalling, shaping the immunogenicity of BRCA-associated cancers."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling supports the survival and immune evasion of the BRCA-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the invasion and microenvironment of the BRCA-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) removes a tumor-suppressive brake in BRCA-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory and pre-metastatic microenvironment of hereditary breast and ovarian cancers."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt/β-catenin signaling of BRCA-associated breast and ovarian tumors."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferation and invasion of the tumors of hereditary breast and ovarian cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the tumors of hereditary breast and ovarian cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival of the genomically unstable, HR-deficient cells of hereditary breast and ovarian cancer."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of hereditary breast and ovarian cancer."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of the tumors of hereditary breast and ovarian cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of hereditary breast and ovarian cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the cancers of hereditary breast and ovarian cancer syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of hereditary breast and ovarian cancer syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of hereditary breast and ovarian cancer syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of hereditary breast and ovarian cancer syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of hereditary breast and ovarian cancer syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of hereditary breast and ovarian cancer syndrome."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HRD immunogenicity: BRCA-deficient tumours accumulate genomic scars and neoantigens from failed homologous recombination (RAD51 already mapped), and MHC class II antigen presentation shapes the immunotherapy responses seen in these more immunogenic cancers."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell expansion supports the anti-tumour immunity and checkpoint responses (PD-1 already mapped) that are more active in the neoantigen-rich BRCA-mutant breast and ovarian cancers."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Therapy resistance: the AXL receptor tyrosine kinase drives epithelial-mesenchymal transition and can contribute to resistance to PARP inhibitors and platinum, the mainstays that exploit the homologous-recombination defect of BRCA-mutant tumours."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Treatment myelosuppression: the platinum chemotherapy and PARP inhibitors used against BRCA-mutant cancers are myelosuppressive, lowering haemoglobin, and PARP inhibitors carry a small long-term risk of therapy-related myelodysplasia (already mapped)."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour response to the neoantigens generated by the homologous-recombination defect (PD-1 already mapped), opposing the immunotherapy explored for BRCA-mutant cancers."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative DNA damage: with homologous-recombination repair crippled by BRCA loss (RAD51 already mapped), the oxidative DNA damage to which xanthine-oxidase-derived reactive oxygen species contribute is less faithfully repaired, adding to genomic instability."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 and aromatase: cyclooxygenase-2 and prostaglandin E2 promote aromatase-driven oestrogen synthesis (estrogen already mapped) and inflammation in breast tissue, part of the carcinogenesis of the BRCA-mutant breast cancers."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment that the immunotherapy explored for BRCA-mutant tumours must overcome."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the platinum and other chemotherapy for the BRCA-associated cancers causes anaemia (haemoglobin already mapped) often needing transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of the BRCA-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and cancer risk: the adipokine leptin links obesity to the risk of the hormone-responsive breast (estrogen already mapped) and endometrial cancers, a modifiable factor modulating the penetrance in hereditary breast-ovarian cancer."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine modulation: adiponectin, with leptin (already mapped), links the metabolic state to the breast-cancer risk, part of the modifiable adipokine influence on the hormone-responsive cancers of hereditary breast-ovarian cancer."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the obesity-related modifiable adipokine influence on the hormone-responsive cancers of hereditary breast-ovarian cancer."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Melanoma risk: the BRCA2 (already mapped) carriers have an elevated risk of melanoma (cutaneous and uveal), part of the broader cancer spectrum of hereditary breast-ovarian cancer."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunogenic HRD tumours: the homologous-recombination-deficient (BRCA already mapped) tumours accumulate neoantigens, making them susceptible to the cytotoxic T cells (perforin already mapped) and the checkpoint (PD-1 already mapped) immunotherapy."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "CDH1 lobular-breast overlap: the hereditary diffuse gastric cancer (CDH1 already mapped) and the hereditary breast-ovarian cancer overlap in the lobular breast-cancer risk, hereditary breast-cancer syndromes in the genetic differential."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "HRD innate immunogenicity: the homologous-recombination deficiency (BRCA already mapped) generates the cytosolic DNA that activates the cGAS-STING (already mapped) type-I interferon, the innate immunogenicity of the HBOC tumours."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the M2 (IL-4 and IL-13 already mapped) macrophages populate the immunosuppressive stroma of the HBOC tumours, opposing the neoantigen (T-cell already mapped) immunity."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, enhanced by the HRD (BRCA already mapped) neoantigen load and the PARP-inhibitor-induced immunogenicity of HBOC tumours."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm counter to the M2 macrophage (already mapped) immunosuppression of the HBOC tumour microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the HBOC tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the HBOC tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the HBOC tumours."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral arm: the plasma cells secrete the anti-tumour antibodies (already mapped) of the humoral response, which in the BRCA-mutant (already mapped) homologous-recombination-deficient tumours can be enhanced by the higher neoantigen load."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, associates with the immunotherapy (PD-1 already mapped) response of the higher-neoantigen HRD-deficient HBOC tumours."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the HBOC tumours."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the HBOC tumour stroma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the HBOC tumour microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the HBOC tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the BRCA-deficient (already mapped) proliferating cells of the HBOC tumours."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-HBOC axis: TSLP, from the BRCA-deficient (already mapped) tumour stroma and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of HBOC-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-HBOC axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), augments vascular permeability and the inflammatory stromal milieu of HBOC-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-HBOC axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and anaemia of HBOC-associated cancers, activates the EPOR on BRCA-deficient (already mapped) tumour cells and modulates macrophage (already mapped) polarisation in the tumour microenvironment."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-HBOC axis: histamine, from mast cells in the HBOC tumour stroma, signals via H1/H2 receptors on BRCA-deficient (already mapped) tumour cells, promoting angiogenesis, immune evasion, and the pro-tumourigenic milieu of HBOC-associated breast and ovarian cancers."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-HBOC axis: melatonin, via MT1/MT2 receptors on BRCA-deficient (already mapped) tumour cells, suppresses HIF-1α (already mapped) and oestrogen-receptor-driven proliferation, modulates circadian breast-cancer risk, and enhances PARP-inhibitor sensitivity."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-HBOC axis: testosterone, via androgen receptor signalling on BRCA-deficient (already mapped) breast and ovarian tumour cells, modulates HER2 (already mapped) and PARP-inhibitor sensitivity, and the sex-biased hormonal milieu of HBOC-associated cancers."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "HBOC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the BRCA-deficient immune TME; hyperprolactinaemia amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of HBOC."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "HBOC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of HBOC."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "HBOC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of hereditary breast-ovarian cancer."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "HBOC serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the TME; serotonin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of HBOC."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "HBOC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) oxidative tumour cascade of HBOC."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "HBOC iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of HBOC."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "HBOC sodium: high dietary sodium promotes Th17 polarisation and macrophage (already mapped) activation; sodium-induced IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) and T-helper-cell (already mapped) tumour cascade of HBOC."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "HBOC magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies IL-6 (already mapped) and T-helper-cell (already mapped) tumour-promoting cascade of HBOC."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "HBOC copper: copper supports macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour function; copper deficiency amplifies IL-6 (already mapped) and T-helper-cell (already mapped) tumour-promoting cascade of HBOC."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "HBOC potassium: potassium regulates macrophage (already mapped) and T-cytotoxic (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) tumour-promoting cascade in HBOC."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "HBOC zinc: zinc cofactors macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) tumour-promoting inflammatory cascade in HBOC."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "HBOC phosphorus: phosphorus as ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) fuels anti-tumour kinase signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "HBOC carbon: carbon in nucleotides of macrophages (already mapped) and T-cytotoxic cells (already mapped) fuels anti-tumour proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) cascade in HBOC."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "HBOC chloride: chloride channels on macrophages (already mapped) and T-cytotoxic cells (already mapped) regulate ionic anti-tumour signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) cascade in HBOC."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "HBOC hydrogen: hydrogen via ROS from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "HBOC glp-1: GLP-1 from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) anti-tumour cascade in HBOC."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "HBOC angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BRCA1 (already mapped) anti-tumour cascade in HBOC."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "HBOC wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and T-cytotoxic cells (already mapped) regulates tumour immune tone; wnt-beta-catenin dysregulation amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "HBOC fibronectin: fibronectin in macrophages (already mapped) and T-cytotoxic cells (already mapped) promotes tumour ECM remodelling; fibronectin excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "HBOC notch: Notch signalling on macrophages (already mapped) and T-cytotoxic cells (already mapped) regulates tumour immune recognition; notch excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "HBOC igf-1: IGF-1 from macrophages (already mapped) and T-cytotoxic cells (already mapped) promotes tumour immune resistance; igf-1 excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "HBOC activin-a: activin-A from macrophages (already mapped) and T-cytotoxic cells (already mapped) regulates tumour immune-fibrotic balance; activin-a excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "HBOC cgrp: CGRP from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour neuroimmune tone; cgrp excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "HBOC calcitonin: calcitonin from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour calcium signalling; calcitonin excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "HBOC substance-p: substance-P from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour pain tone; substance-P excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "HBOC insulin-receptor: insulin receptor on macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour metabolic axis; insulin-receptor loss amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "HBOC aldosterone: aldosterone from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour fluid balance; aldosterone excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC."
---

# Hereditary Breast and Ovarian Cancer

## Overview

**Hereditary breast and ovarian cancer syndrome (HBOC)** is the most common hereditary cancer predisposition syndrome, caused by germline pathogenic variants in **BRCA1** or **BRCA2** (primarily) and in moderate-to-high risk genes including **PALB2**, **ATM**, **CHEK2**, **RAD51C**, and **RAD51D**. HBOC accounts for approximately **5-10% of all breast cancers** and **10-15% of all ovarian cancers**. The BRCA1 and BRCA2 proteins are core components of the homologous recombination (HR) DNA repair pathway; their loss creates HR deficiency (HRD), rendering cells reliant on error-prone repair — accumulating mutations and facilitating cancer initiation [^kuchenbaecker-2017-brca-risks] [^antoniou-2014-palb2-risk].

**HBOC gene risk stratification (2026 NCCN/ACMG framework):**

| Gene | Breast Ca lifetime risk | Ovarian Ca lifetime risk | Other elevated risks |
|---|---|---|---|
| BRCA1 | ~55-72% | ~44% | TNBC, premenopausal |
| BRCA2 | ~45-69% | ~17% | Pancreatic (~4%), prostate (~19% in males), male breast (~7%) |
| PALB2 | ~35-65% | ~5-10% | Pancreatic (~2-3%) |
| ATM (germline, biallelic = AT) | ~20-30% | Low | Prostate (~6%), pancreatic elevated |
| CHEK2 | ~15-25% | Low | CRC (~3%), prostate moderate |
| RAD51C | ~15-20% | ~10-15% | HGSOC subtype |
| RAD51D | ~15-20% | ~10-15% | HGSOC subtype |
| CDH1 (E-cadherin) | ~42% (lobular BC) | Low | Diffuse gastric cancer ~70% |
| PTEN (Cowden) | ~50% | Low | Thyroid, endometrial |

*Population breast cancer risk ~13% lifetime; ovarian risk ~2% lifetime.*

## Structure

### Genetic architecture

**BRCA1 (17q21.31):**
- 1863 aa, 220 kDa; RING domain (N-terminus; E3 ubiquitin ligase with BARD1), BRCT repeats (C-terminus; phosphoprotein binding after DNA damage: pSer1524-CtIP, pSer1387-BACH1, pSer178-ABRAXAS)
- Germline spectrum: ~1,650 pathogenic/likely pathogenic variants in ClinVar; frameshift (~40%), nonsense (~20%), large deletions (MLPA required, ~10%), missense (rare pathogenic); founder variants: 185delAG (Ashkenazi Jewish); 5382insC (Ashkenazi Jewish, Eastern European)
- De novo rate: ~1% of BRCA1 PV
- Penetrance modifiers: polygenic risk score (PRS), reproductive history, BMI, oral contraceptive use

**BRCA2 (13q12.3):**
- 3418 aa, 384 kDa; eight BRC repeats (bind RAD51 monomers); nuclear export signal (C-terminal); DNA-binding domain (OB-fold, tower domain)
- Germline spectrum: ~1,250 pathogenic variants; similar to BRCA1 (frameshift, nonsense, large deletions); founder variants: 6174delT (Ashkenazi Jewish); 999del5 (Icelandic/Celtic)
- BRCA2 germline also elevated in prostate cancer (HIGH risk: up to ~19-23% lifetime in BRCA2 vs ~12% population), pancreatic adenocarcinoma (~4% vs ~1.5%), cholangiocarcinoma
- Male BRCA2 carriers: elevated male breast cancer (~7% lifetime vs <0.1% population)

**Genetic testing landscape (2026):**
Multigene panel testing has largely replaced sequential BRCA1/2 testing; panels include BRCA1, BRCA2, PALB2, ATM, CHEK2, RAD51C, RAD51D, CDH1, PTEN, TP53, STK11, and up to 75+ genes depending on platform. Cascade testing (family members of identified carriers) is cost-effective and recommended.

### BRCA gene discovery

- BRCA1: Hall 1990 (linkage) → Miki 1994 (cloning, Science); BRCA2: Wooster 1995 (linkage) → Tavtigian 1996 (cloning, Nature Genetics)
- BRCA1/2 population prevalence: ~1 in 400 carry a BRCA1/2 pathogenic variant in general population; 1 in 40 in Ashkenazi Jewish population (due to three founder variants)

## Function

### HR pathway and BRCA proteins

Both BRCA1 and BRCA2 are required for the S/G2 phase homologous recombination repair of DSBs — the error-free, template-directed mechanism using a sister chromatid as repair template. Loss of HR → cells use error-prone non-homologous end joining (NHEJ) or microhomology-mediated end joining (MMEJ) → accumulation of structural variants, inversions, translocations → genomic instability → tumorigenesis.

**BRCA1 roles:**
- **DSB recognition and signaling**: BRCA1 localizes to DSBs via 53BP1 competition (ATM phosphorylates histone H2AX → MDC1 → BRCA1 recruited); BRCA1 promotes end resection (long-range resection) by antagonizing 53BP1-RIF1-Shieldin
- **Ubiquitin E3 ligase (RING-BARD1)**: ubiquitinates H2A at Lys127/129 → local chromatin remodeling at DSBs; also ubiquitinates RPB8 → stalled RNA Pol II degradation at DSBs (transcription-coupled repair)
- **Cell cycle checkpoint**: BRCA1 BRCT phosphopeptide-binding → BACH1/FANCJ helicase interaction → replication fork stability; ABRAXAS-RAP80 complex → BRCA1 retained at DSBs
- **Centrosome number**: BRCA1 localizes to centrosomes; BRCA1 LOF → supernumerary centrosomes → multipolar spindles → aneuploidy

**BRCA2 roles:**
- **RAD51 loader**: BRC repeats 1-8 each bind one RAD51 monomer → BRCA2 can load up to 8 RAD51 units at once; BRCA2 OB-fold also contacts ssDNA directly → positions RAD51 filament for optimal strand invasion
- **Replication fork protection**: BRCA2 stabilizes RAD51 on ssDNA at stalled forks → prevents MRE11 nuclease degradation of nascent DNA; fork protection is independent of DSB repair and requires distinct BRCA2 domains (Leu2647-Asp2803)
- **Meiosis**: BRCA2 regulates DMC1 (meiosis-specific RAD51 homolog) loading during meiotic HR; BRCA2 loss in mouse germline → meiotic failure → infertility

**Synthetic lethality basis for PARP inhibition:**

Normal cells: single-strand breaks → PARP1 binds SSB → poly-ADP ribose (PAR) chain → recruits XRCC1-DNA Pol β-LIG3 → base excision repair → SSB fixed (PARP released/recycled)

BRCA-mutant cells (HRD):
1. PARP inhibitor occupies PARP1 catalytic domain → prevents PAR synthesis AND traps PARP1 on DNA (PARP trapping; potency: talazoparib > niraparib > olaparib > rucaparib)
2. Trapped PARP1 on DNA → replication forks collide with trapped PARP1 → fork collapse → DSB
3. DSB repair requires HR (BRCA1/2-RAD51) — absent in BRCA-mutant cells → cell dies
4. Normal cells (HR-proficient): DSB repaired by HR → survival; selective toxicity to HRD cells

## Pathology

### Cancer subtypes in HBOC

**BRCA1-associated breast cancer:**
- Predominantly **triple-negative breast cancer (TNBC)** (~60-80% of BRCA1-associated invasive breast cancer)
- High grade (grade 3); high Ki-67; often medullary/pushing border histology
- Young age at onset (peak 30-40 years); bilateral risk ~40% at 10 years
- Chemotherapy: platinum agents (carboplatin) + taxane + immunotherapy (pembrolizumab, KEYNOTE-522 in TNBC regardless of germline status)
- PARP inhibitor: olaparib adjuvant (OlympiA trial: germline BRCA1/2, HER2-negative, residual disease after neoadjuvant; 4-year OS benefit 3.4%)

**BRCA2-associated breast cancer:**
- Predominantly **luminal (ER+/HER2-)**: ~60-70% ER-positive; less TNBC than BRCA1
- Higher grade than average ER+ BC; may behave like ER+ but with HRD features
- CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) for ER+/HER2- metastatic disease (BRCA2 does not affect CDK4/6i sensitivity)
- PARP inhibitor: olaparib/talazoparib for germline BRCA1/2 HER2-negative metastatic breast cancer

**HBOC-associated ovarian cancer:**
- **High-grade serous carcinoma (HGSOC)**: the predominant histology in BRCA1/2/PALB2/RAD51C/D-associated OC; TP53 mutation is universal in HGSOC
- Clear cell carcinoma: NOT elevated in BRCA1/2 carriers (associated with ARID1A, PIK3CA, loss of MLH1)
- Mucinous: NOT elevated in BRCA1/2 carriers
- **BRCA1-associated OC**: onset age 40-50 (earlier than sporadic OC age 60-70)
- **BRCA2-associated OC**: onset age 50-60
- PARP inhibitor maintenance: olaparib (SOLO-1: germline BRCA1/2, first-line OC; OS benefit at 5 years, HR 0.55); niraparib (PRIMA: germline BRCA + HRD-positive sporadic); rucaparib (ARIEL3)
- Bevacizumab + chemotherapy → maintenance: GOG-0218, ICON7 (regardless of BRCA status)

### Risk management (NCCN 2024)

**Breast cancer surveillance:**
- Annual **breast MRI** (preferred) + **mammogram**: from age 25 (BRCA1/2); from age 30 (PALB2, ATM with fam history, CHEK2)
- Semi-annual clinical breast exam: every 6 months from age 25
- Risk-reducing bilateral mastectomy (BRM): reduces breast cancer risk by ~90-95%; does not eliminate completely (residual axillary tail/skin tissue); timing at patient's discretion after genetic counseling
- No role for tamoxifen chemoprevention in BRCA1 carriers (TNBC is ER-negative, tamoxifen not protective); tamoxifen reduces contralateral BC in BRCA2 carriers

**Ovarian cancer risk reduction:**
- **Bilateral salpingo-oophorectomy (BSO)**: most effective risk reduction
  - BRCA1 carriers: age 35-40 (after childbearing)
  - BRCA2 carriers: age 40-45 (later onset, more time; natural menopause may be acceptable in some)
  - PALB2, RAD51C/D: age 45-50 (lower risk)
- BSO also reduces breast cancer risk in premenopausal carriers (estrogen deprivation): ~50% reduction in BRCA1/2 (if done before age 40)
- Annual CA-125 + transvaginal ultrasound (TVU): low sensitivity for early OC detection (not recommended as primary surveillance); used in women who decline BSO

**Male BRCA2 carriers:**
- Breast self-exam monthly + annual clinical breast exam from age 35; mammogram annually from 40
- PSA + DRE from age 40 for prostate cancer surveillance
- Pancreatic cancer: MRI/MRCP + EUS every 1-2 years from age 50 (CAPS consortium guidelines) for BRCA2 + one affected relative

**Chemoprevention:**
- Oral contraceptive pills (OCP): reduce ovarian cancer risk by ~50% in BRCA1/2 carriers (any duration); possible slight increase in breast cancer risk with long-term use; net benefit for ovarian cancer prevention is generally accepted, especially in BRCA2
- Risk-benefit counseling: individualized; BSO is more protective than OCP alone

### PARP inhibitor clinical approvals (as of 2026)

| PARP inhibitor | Indication | Key trial |
|---|---|---|
| Olaparib (Lynparza) | gBRCA1/2 HER2-neg metastatic BC; gBRCA1/2 HGSOC 1L + maintenance + relapse; gBRCA1/2 mCRPC; gBRCA1/2 mPDAC maintenance | OlympiAD, OlympiA, SOLO-1/2, PROfound, POLO |
| Niraparib (Zejula) | HGSOC maintenance (HRD+/BRCA+); HER2-neg gBRCA1/2 metastatic BC | PRIMA, BRAVO |
| Rucaparib (Rubraca) | gBRCA1/2 HGSOC maintenance + relapse | ARIEL3 |
| Talazoparib (Talzenna) | gBRCA1/2 HER2-neg metastatic BC | EMBRACA |

## Connections

- `connects-to` → **[PALB2](../../03-molecular/palb2/README.md)** — Germline PALB2 pathogenic variants confer ~35-65% lifetime breast cancer risk (second after BRCA1/2); ~5-10% ovarian cancer risk (primarily HGSOC); biallelic PALB2 = Fanconi anemia FA-N; PARP inhibitors are active in PALB2-germline breast and pancreatic cancer.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1 germline variants confer the highest hereditary breast cancer risk (~55-72% lifetime) and ovarian cancer risk (~44%); BRCA1-mutant tumors are often triple-negative (ER-/PR-/HER2-) and high-grade; risk-reducing BSO at age 35 and bilateral mastectomy are standard options.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — BRCA2 germline variants confer ~45-69% lifetime breast cancer risk and ~17% ovarian cancer risk (lower than BRCA1); BRCA2-mutant breast cancer is often ER+/HER2-; olaparib and niraparib FDA-approved for BRCA-mutant metastatic breast cancer; risk-reducing BSO at age 40-45.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — HBOC-associated ovarian cancer is predominantly high-grade serous carcinoma (HGSOC); BRCA1 germline: 44% lifetime risk; BRCA2: 17%; PALB2/RAD51C/D: 5-10%; bilateral salpingo-oophorectomy (BSO) at age 35-40 reduces ovarian cancer mortality; PARP inhibitors in maintenance.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — Germline ATM pathogenic variants confer ~20-30% lifetime breast cancer risk; elevated prostate (~6%) and pancreatic risk; biallelic ATM = ataxia-telangiectasia; ATM-germline BC is often ER+/luminal; NCCN recommends breast MRI from age 40 for ATM heterozygotes with family history.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — BRCA2 loads RAD51 monomers onto ssDNA at DSBs via eight BRC repeats → RAD51 filament → strand invasion (HR repair); BRCA2 LOF → RAD51 loading failure → error-prone NHEJ/MMEJ → tumorigenesis; RAD51 paralogs (RAD51C, RAD51D) each confer ~10-15% lifetime ovarian cancer risk in HBOC.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — HBOC causes ~5-10% of breast cancer; BRCA1-associated BC is predominantly TNBC (~60-80%) with peak onset at 30-40 years; BRCA2-associated BC is predominantly ER+ (~60-70%); olaparib (OlympiAD) and talazoparib (EMBRACA) are FDA-approved for germline BRCA1/2 HER2-neg metastatic BC.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — HBOC and Li-Fraumeni are the major hereditary breast cancer syndromes but differ in scope: HBOC (BRCA1/2) focuses on breast and ovarian cancer with PARP sensitivity, while LFS (germline TP53) spans sarcomas, brain tumors, and adrenocortical carcinoma — focused vs multi-cancer.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — BRCA2 (and to a lesser degree BRCA1, PALB2, ATM) raises pancreatic cancer risk ~3-7×, extending HBOC beyond breast and ovary; these HR-deficient pancreatic cancers respond to platinum and PARP-inhibitor maintenance (olaparib, POLO), so germline testing now guides therapy.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — BRCA2 carriers face ~2-6× prostate cancer risk with more aggressive, earlier-onset disease; HBOC thus affects men too, and BRCA/HR-deficient metastatic prostate cancer responds to PARP inhibitors (olaparib, PROfound) — making germline and tumor testing standard in advanced cases.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — BRCA2 widens the hereditary breast-ovarian cancer spectrum to melanoma: germline BRCA2 modestly raises risk of cutaneous and especially uveal melanoma alongside breast, ovarian, pancreatic and prostate cancer, so a melanoma history can inform BRCA testing.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hereditary breast-ovarian cancer strikes the reproductive system hardest: BRCA1/2 carriers face high lifetime risks of breast, ovarian and fallopian-tube cancer, so risk-reducing salpingo-oophorectomy and enhanced breast surveillance are cornerstones of management.
- `treated-by` → **[Targeted Therapy](../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Hereditary breast-ovarian cancer is the paradigm for synthetic-lethal targeted therapy: BRCA1/2-mutant tumors cannot repair DNA by homologous recombination, so PARP inhibitors (olaparib) blocking backup repair selectively kill them—turning the germline defect into a drug target.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — HBOC and Lynch syndrome are major hereditary cancers raising women's ovarian/endometrial risk via different repair defects: HBOC from BRCA1/2 homologous-recombination loss, Lynch from mismatch-repair loss—each guides distinct screening and surgery.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — HBOC and Cowden syndrome both sharply raise hereditary breast cancer risk through different genes: HBOC via BRCA1/2 (homologous-recombination repair), Cowden via PTEN (PI3K-AKT pathway)—PTEN also brings thyroid and endometrial cancer plus hamartomas.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — HBOC and Peutz-Jeghers both elevate breast cancer risk through different mechanisms: HBOC from BRCA1/2 DNA-repair loss, PJS from STK11 loss—PJS also raises ovarian (sex-cord) and GI cancer risk, so both warrant intensified breast surveillance from a young age.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen exposure modulates HBOC risk: BRCA-driven breast cancers often still respond to hormonal signaling, and reducing estrogen—via risk-reducing oophorectomy or endocrine therapy—lowers cancer risk, so the lifetime estrogen burden shapes when these cancers arise.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — HBOC carries a modest endometrial cancer risk: BRCA1 carriers, especially after tamoxifen, have a slightly raised risk of serous endometrial cancer, so gynecologic surveillance and decisions about hysterectomy at oophorectomy are part of managing the syndrome.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — BRCA-mutant cells are radiosensitive from impaired DNA repair: their inability to fix double-strand breaks makes ionizing radiation more damaging, a reason young carriers are screened with non-ionizing MRI rather than repeated mammography.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — HBOC overlaps with the p53-driven Li-Fraumeni spectrum of inherited cancer: BRCA loss cripples DNA double-strand-break repair while TP53 loss removes the damage checkpoint, so both germline defects in the genome-guardian network produce familial breast and other cancers.
- `connects-to` → **[Bloom Syndrome](../bloom-syndrome/README.md)** — HBOC belongs to the family of DNA-repair cancer syndromes like Bloom: BRCA1/2 run homologous recombination just as BLM helicase resolves recombination intermediates, so loss of either destabilizes the genome—a shared theme of repair failure driving cancer.
- `connects-to` → **[Immune System](../immune-system/README.md)** — BRCA-mutant tumors engage the immune system distinctively: defective DNA repair raises mutational load and neoantigens, making some HBOC cancers more immunogenic—so checkpoint immunotherapy is explored alongside the PARP inhibitors that exploit the repair defect.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — HBOC overlaps another hereditary breast syndrome via CDH1: while BRCA carriers get ductal breast cancer, CDH1 (hereditary diffuse gastric cancer) carriers develop lobular breast cancer, so inherited breast-cancer risk spans more than one gene and tumor type.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — HBOC sits among the DNA-repair cancer syndromes alongside MUTYH-associated polyposis: HBOC stems from broken homologous recombination and MAP from faulty base-excision repair, so both show how losing a specific repair pathway seeds inherited cancer.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Tumor-infiltrating cytotoxic T cells track BRCA tumors' outcomes: HRD cancers, especially triple-negative breast and high-grade ovarian, often draw dense T-cell infiltrates that predict better prognosis and chemo response—so immune contexture is a built-in biomarker.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — BRCA1 breast cancer is fueled by progesterone signaling: the hormone drives RANKL and proliferation in mammary stem cells primed by BRCA1 loss, which is why anti-progesterone strategies are studied to prevent cancer in carriers.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — BRCA1 tumors are usually triple-negative, lacking HER2: unlike many breast cancers they express neither HER2 nor hormone receptors, so they miss those targeted drugs and instead rely on chemotherapy and PARP inhibitors against their DNA-repair defect.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — BRCA-mutant cancers are more immunogenic but shielded by regulatory T cells: their crippled DNA repair generates many neoantigens, yet Tregs blunt the response—so combining PARP inhibitors with immunotherapy aims to tip the balance.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — HBOC reaches beyond breast and ovary to the pancreas: BRCA2 (and BRCA1) carriers face higher pancreatic cancer risk, and these tumors' DNA-repair defect makes them responsive to platinum chemotherapy and PARP inhibitors.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — BRCA-related ovarian cancers lean on VEGF for blood supply: the angiogenesis driver fuels their growth and ascites, so anti-VEGF bevacizumab is combined with chemotherapy and PARP inhibitors in these tumors.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells aid the attack on BRCA-mutant tumors: their DNA-repair defect spawns neoantigens and stress signals that NK cells sense, and antibody therapies like trastuzumab recruit NK killing against HER2-positive BRCA breast cancers.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — BRCA-related ovarian cancers recruit endothelial cells: VEGF drives these vessel-lining cells to build the vasculature feeding the tumor and its ascites, the target of the bevacizumab added to therapy.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Treating HBOC cancers can strain the bone marrow: the PARP inhibitors exploiting BRCA's repair defect suppress marrow blood production and, rarely, trigger secondary MDS or leukemia, so counts are watched.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — HBOC reaches the skin through melanoma risk: BRCA2 carriers face a raised chance of melanoma alongside breast, ovarian, and pancreatic cancer, so skin surveillance joins their screening.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts shape HBOC tumors: they build the stroma of BRCA breast and ovarian cancers, influencing how the tumor grows and how well drugs reach it.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — HBOC tumors and their treatment leave fibrosis: a desmoplastic stroma surrounds the cancers, and radiation and surgery scar the breast and pelvis, lasting effects survivors carry.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Breast cancers often announce themselves as microcalcifications: clusters of calcium specks on a mammogram are an early sign that prompts biopsy, central to screening BRCA carriers.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — BRCA loss leaves cells unable to mend broken DNA: without homologous recombination, the double-strand breaks that radiation and chemotherapy inflict go unrepaired — a weakness PARP inhibitors exploit to kill the cancer by synthetic lethality.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — BRCA-driven cancers reach for the brain: BRCA-mutant breast and ovarian tumors, often triple-negative, carry a notable tendency to seed central-nervous-system metastases, prompting vigilance for brain spread.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a frequent destination as BRCA cancers spread: hematogenous metastases from the breast, ovarian, and pancreatic tumors of the syndrome lodge there, marking advanced disease.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The targeted drugs thin the blood: PARP inhibitors like olaparib — which exploit the BRCA repair defect — commonly cause anemia by suppressing the marrow, and carry a small long-term risk of MDS and leukemia.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — BRCA tumors are platinum- and taxane-sensitive, at a neural cost: the carboplatin and paclitaxel used against them injure peripheral sensory neurons into a numbing, tingling neuropathy.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Immunotherapy suits the BRCA1 breast cancers: many are triple-negative and respond to checkpoint antibodies like pembrolizumab, harnessing the antibody-driven immune system against tumors hard to target otherwise.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The targeted drugs squeeze the marrow: PARP inhibitors like olaparib and niraparib commonly drop platelet and red-cell counts, so blood counts are watched closely and doses adjusted through the long maintenance courses these carriers take.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The treatments can seed a second cancer: years of platinum chemotherapy and PARP-inhibitor maintenance carry a small but real risk of therapy-related myelodysplastic syndrome and leukemia, a sobering late cost of controlling the solid tumors.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Risk-reducing surgery brings early menopause: removing the ovaries and tubes in a young BRCA carrier abruptly cuts off estrogen, accelerating bone loss toward osteoporosis unless hormone or bone-protective therapy is considered.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K offers a second target alongside the BRCA defect: PIK3CA mutations are common in BRCA-associated breast cancers, so PI3K-AKT inhibitors are combined with the PARP drugs that exploit the homologous-recombination flaw.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Broken DNA repair makes a visible tumor: BRCA loss spawns genomic instability and neoantigens that dendritic cells can present, making these cancers more immunogenic and a rationale for combining PARP inhibitors with immunotherapy.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — BRCA's reach extends to the bile ducts: BRCA2 (and BRCA1) carriers face a raised risk of cholangiocarcinoma, and these homologous-recombination-deficient biliary tumors may respond to platinum and PARP therapy.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — BRCA2 widens the cancer net to the stomach: carriers, especially of BRCA2, face an increased risk of gastric cancer, one of the extra-breast/ovarian tumors that shape the surveillance of these families.
- `connects-to` → **[AML](../aml/README.md)** — The therapy can end in leukemia: years of platinum chemotherapy and PARP-inhibitor maintenance occasionally cause therapy-related acute myeloid leukemia, the frank-leukemia end of the marrow damage these treatments inflict.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC amplification drives the BRCA1 tumor: the basal-like, triple-negative breast cancers typical of BRCA1 carriers frequently amplify MYC, adding a proliferative push to the homologous-recombination defect.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its cancers and their treatment clot the blood: the breast and especially ovarian cancers of HBOC carriers are strongly prothrombotic, and the surgery and chemotherapy they require make venous thromboembolism a major hazard.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Chemo empties the marrow's defenses: the platinum and taxane regimens used against HBOC-related cancers cause neutropenia, so febrile neutropenia and sepsis are recurrent treatment dangers.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Cancer and chemo wear down the blood: the advanced ovarian and breast cancers of HBOC carriers, with their chronic inflammation and marrow-suppressing therapy, commonly cause an anemia of chronic disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Carrying the mutation weighs on the mind: learning of a high inherited cancer risk and facing prophylactic mastectomy and oophorectomy impose a heavy psychological burden, with depression common among carriers.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Breast-cancer therapy can wound the heart: the anthracyclines and HER2-directed trastuzumab used to treat cancers in HBOC carriers are cardiotoxic, risking a cardiomyopathy and heart failure.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Platinum chemo strains the kidney: the cisplatin and carboplatin central to treating the ovarian cancers of HBOC carriers are nephrotoxic, and cumulative exposure can leave chronic kidney impairment.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A genetic verdict and hard choices breed worry: learning of a BRCA mutation, weighing risk-reducing mastectomy and oophorectomy, and lifelong screening foster chronic health anxiety in HBOC carriers.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its chemotherapy injures the nerves: the platinum and taxane chemotherapy and post-mastectomy surgery in HBOC carriers cause peripheral and post-surgical neuropathic pain.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemotherapy opens the lung to mold: the neutropenia from chemotherapy for the breast and ovarian cancers of HBOC carriers can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Risk-reducing surgery means major wounds: prophylactic mastectomy with reconstruction and salpingo-oophorectomy in HBOC carriers leave surgical wounds, sometimes irradiated, that must heal.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Removing the ovaries forces early menopause: the risk-reducing salpingo-oophorectomy recommended to BRCA carriers triggers abrupt surgical menopause with its hormonal, bone and cardiovascular consequences.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its drugs and its genes reach the gut: PARP inhibitors and platinum used in BRCA-mutant cancers cause nausea and GI toxicity, and BRCA mutations also raise pancreatic and other GI cancer risk.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Risk reduction and treatment burden the heart: prophylactic oophorectomy induces premature menopause that raises cardiovascular risk, and anthracycline and HER2 therapy for BRCA breast cancer is cardiotoxic.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its cancers travel through the nodes: BRCA-associated breast and ovarian cancers spread to lymph nodes, and axillary surgery for breast cancer causes arm lymphoedema.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It favours the brain and harms the nerves: BRCA1 breast cancers are often triple-negative with a propensity for brain metastasis, and platinum and taxane chemotherapy cause peripheral neuropathy.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It widens the cancer spectrum to the skin: BRCA2 carriers have an increased risk of melanoma, adding the skin to the breast, ovary, pancreas and prostate in BRCA-related cancer.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its cancers spread to bone: the breast and prostate cancers driven by BRCA mutations frequently metastasise to the skeleton, causing pain and fractures.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Advanced disease reaches the lungs: BRCA-related breast and ovarian cancers metastasise to the lungs and pleura, causing effusions and breathlessness.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — BRCA tumours are platinum-sensitive: homologous-recombination deficiency from BRCA1/2 loss makes these breast, ovarian and pancreatic cancers exquisitely sensitive to platinum chemotherapy.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Genomic instability invites immunotherapy: BRCA/HRD tumours carry more neoantigens, and checkpoint inhibitors, often with PARP inhibitors, benefit triple-negative breast and ovarian cancers in HBOC.
- `connects-to` → **[Rothmund-Thomson](../rothmund-thomson/README.md)** — A fellow genomic-instability syndrome: like Rothmund-Thomson, hereditary breast-ovarian cancer stems from defective DNA repair, both belonging to the family of inherited genome-instability cancer predispositions.
- `connects-to` → **[FAP](../fap/README.md)** — Gatekeeper versus caretaker: FAP is driven by loss of the APC gatekeeper that restrains tissue growth, whereas HBOC arises from loss of BRCA caretaker genes guarding genome integrity—the classic two categories of tumour-suppressor gene.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Knudson's two-hit rule applies to both: retinoblastoma defined the model in which a germline first hit plus somatic loss of the second allele triggers cancer, exactly how BRCA1/2 carriers in HBOC lose their remaining wild-type allele in the tumour.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Two gynaecological cancers, opposite prevention: cervical cancer is HPV-driven and largely prevented by vaccination and screening, whereas HBOC ovarian cancer is germline-driven with no good screening, so management turns to risk-reducing surgery.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — Genome-instability cancer syndromes: like Werner syndrome's RecQ-helicase defect, BRCA-driven HBOC reflects failed genome maintenance, predisposing to cancer through accumulated unrepaired DNA damage.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Biallelic BRCA2 is Fanconi anaemia: inheriting two faulty BRCA2/FANCD1 alleles causes Fanconi anaemia with childhood bone-marrow failure—the recessive extreme of an HBOC gene.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — Which ovarian cancer it causes: BRCA-associated ovarian cancer is high-grade serous, biologically distinct from the ARID1A-driven clear-cell subtype that arises from endometriosis.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — BRCA2 and eye melanoma: germline BRCA2 mutations modestly raise the risk of uveal melanoma alongside the cutaneous melanoma of the broader BRCA2 cancer spectrum.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Surgical menopause and bone: risk-reducing oophorectomy in BRCA carriers brings early oestrogen loss that accelerates cortical-bone loss and osteoporosis—a trade-off of cancer prevention.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Treatment cardiotoxicity: anthracyclines and HER2-targeted trastuzumab used for BRCA-associated breast cancer can injure the myocardium, a survivorship concern alongside cure.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle therapy: CDK4/6 inhibitors are a mainstay for hormone-receptor-positive breast cancers, including many that arise in BRCA carriers, blocking cyclin-driven proliferation.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT targeting: AKT-pathway activation in BRCA-associated breast cancer is targetable with AKT inhibitors such as capivasertib, complementing PARP and endocrine therapy.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR blockade: mTOR inhibitors like everolimus add benefit in hormone-receptor-positive breast cancer, part of the layered targeting of these BRCA-spectrum tumours.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic aggression: HIF-1α stabilised in the often hypoxic, triple-negative BRCA1-associated tumours drives angiogenesis and a metastatic, treatment-resistant phenotype.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic driver: EZH2 overexpression cooperates with BRCA loss in HBOC tumours, silencing tumour-suppressor genes and offering an epigenetic therapeutic target.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT reactivation maintains telomeres in the genomically unstable BRCA-mutant tumours, enabling the limitless proliferation of HBOC cancers.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immunogenic HRD tumours: homologous-recombination-deficient BRCA-mutant cancers carry a high neoantigen load that, with their genomic scarring, makes them more responsive to PD-1 checkpoint immunotherapy.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Cooperating tumour suppressor: CDKN2A loss accompanies BRCA mutation in HBOC tumours, releasing the cell-cycle brake to accelerate the proliferation of genomically unstable cells.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into HBOC breast and ovarian tumours, contributing to the stroma that shapes growth and immunotherapy response.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — RANK/RANKL signaling drives the proliferation of BRCA1-mutant mammary progenitor cells, the cells of origin of basal-like breast cancer—the basis for testing denosumab as a chemoprevention strategy in BRCA1 carriers.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The homologous-recombination deficiency of BRCA-mutant cancers produces micronuclei and cytosolic DNA that activate cGAS-STING, the innate-immune mechanism underlying the synergy of combining PARP inhibitors with immunotherapy.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — The CXCL12-CXCR4 axis drives the metastasis of the triple-negative breast and high-grade serous ovarian cancers that BRCA carriers develop, a chemokine route to the characteristic spread of these aggressive tumors.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — PARP inhibitors and platinum exploit the homologous-recombination defect of BRCA-mutant tumors to drive lethal DNA damage and caspase-3-mediated apoptosis, the synthetic-lethal killing central to treating HBOC cancers.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The high genomic instability of BRCA-mutant, homologous-recombination-deficient tumors makes them more immunogenic, and checkpoint blockade unleashing perforin-mediated cytotoxic killing is active in triple-negative breast cancer.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — A fraction of the triple-negative breast cancers BRCA carriers develop are of the luminal-androgen-receptor subtype, where AR-targeted therapy is being explored, reflecting the molecular diversity within the disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped), a frequent cooperating event in BRCA-associated breast and ovarian cancers.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis (CDK4/6 and CDKN2A already mapped) releases E2F1, which itself transactivates homologous-recombination genes including BRCA1 and RAD51 (both mapped), tying proliferation to the repair pathway lost in HBOC.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — The triple-negative, basal-like breast cancers that predominate in BRCA1 carriers frequently express EGFR, a hallmark of the basal phenotype and a candidate therapeutic target.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 negatively regulates p53 (already mapped), and its dysregulation cooperates with the homologous-recombination defects of BRCA-mutant tumors to permit survival of genomically unstable cells.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) is frequently disrupted in BRCA-associated basal-like breast and high-grade serous ovarian cancer, driving proliferation.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Estrogen-induced anti-apoptotic BCL-2 supports the survival of the hormone-receptor-positive breast cancers arising in HBOC, balancing the caspase-3 apoptosis already mapped.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes invasion and immune evasion in the breast and ovarian cancers of hereditary breast-ovarian cancer syndrome.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling, a context-dependent regulator, shapes EMT, invasion and the immunosuppressive microenvironment in BRCA-associated cancers.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of EGFR/HER2 (both mapped) provides a proliferative input in BRCA-associated breast and ovarian cancers.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — BRCA deficiency floods the cytosol with DNA that activates cGAS-STING (mapped) and IFN-STAT1 signaling, shaping the immunogenicity of BRCA-associated cancers.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling supports the survival and immune evasion of the BRCA-associated breast and ovarian cancers.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the invasion and microenvironment of the BRCA-associated breast and ovarian cancers.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) removes a tumor-suppressive brake in BRCA-associated breast and ovarian cancers.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory and pre-metastatic microenvironment of hereditary breast and ovarian cancers.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt/β-catenin signaling of BRCA-associated breast and ovarian tumors.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferation and invasion of the tumors of hereditary breast and ovarian cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the tumors of hereditary breast and ovarian cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival of the genomically unstable, HR-deficient cells of hereditary breast and ovarian cancer.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the tumors of hereditary breast and ovarian cancer.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of the tumors of hereditary breast and ovarian cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of hereditary breast and ovarian cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the cancers of hereditary breast and ovarian cancer syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of hereditary breast and ovarian cancer syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of hereditary breast and ovarian cancer syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of hereditary breast and ovarian cancer syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of hereditary breast and ovarian cancer syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of hereditary breast and ovarian cancer syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — HRD immunogenicity: BRCA-deficient tumours accumulate genomic scars and neoantigens from failed homologous recombination (RAD51 already mapped), and MHC class II antigen presentation shapes the immunotherapy responses seen in these more immunogenic cancers.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell expansion supports the anti-tumour immunity and checkpoint responses (PD-1 already mapped) that are more active in the neoantigen-rich BRCA-mutant breast and ovarian cancers.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Therapy resistance: the AXL receptor tyrosine kinase drives epithelial-mesenchymal transition and can contribute to resistance to PARP inhibitors and platinum, the mainstays that exploit the homologous-recombination defect of BRCA-mutant tumours.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Treatment myelosuppression: the platinum chemotherapy and PARP inhibitors used against BRCA-mutant cancers are myelosuppressive, lowering haemoglobin, and PARP inhibitors carry a small long-term risk of therapy-related myelodysplasia (already mapped).
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour response to the neoantigens generated by the homologous-recombination defect (PD-1 already mapped), opposing the immunotherapy explored for BRCA-mutant cancers.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative DNA damage: with homologous-recombination repair crippled by BRCA loss (RAD51 already mapped), the oxidative DNA damage to which xanthine-oxidase-derived reactive oxygen species contribute is less faithfully repaired, adding to genomic instability.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 and aromatase: cyclooxygenase-2 and prostaglandin E2 promote aromatase-driven oestrogen synthesis (estrogen already mapped) and inflammation in breast tissue, part of the carcinogenesis of the BRCA-mutant breast cancers.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment that the immunotherapy explored for BRCA-mutant tumours must overcome.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the platinum and other chemotherapy for the BRCA-associated cancers causes anaemia (haemoglobin already mapped) often needing transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of the BRCA-associated breast and ovarian cancers.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and cancer risk: the adipokine leptin links obesity to the risk of the hormone-responsive breast (estrogen already mapped) and endometrial cancers, a modifiable factor modulating the penetrance in hereditary breast-ovarian cancer.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine modulation: adiponectin, with leptin (already mapped), links the metabolic state to the breast-cancer risk, part of the modifiable adipokine influence on the hormone-responsive cancers of hereditary breast-ovarian cancer.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), is part of the obesity-related modifiable adipokine influence on the hormone-responsive cancers of hereditary breast-ovarian cancer.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Melanoma risk: the BRCA2 (already mapped) carriers have an elevated risk of melanoma (cutaneous and uveal), part of the broader cancer spectrum of hereditary breast-ovarian cancer.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunogenic HRD tumours: the homologous-recombination-deficient (BRCA already mapped) tumours accumulate neoantigens, making them susceptible to the cytotoxic T cells (perforin already mapped) and the checkpoint (PD-1 already mapped) immunotherapy.
- `connects-to` → **[Hereditary diffuse gastric cancer](../hereditary-diffuse-gastric-cancer/README.md)** — CDH1 lobular-breast overlap: the hereditary diffuse gastric cancer (CDH1 already mapped) and the hereditary breast-ovarian cancer overlap in the lobular breast-cancer risk, hereditary breast-cancer syndromes in the genetic differential.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — HRD innate immunogenicity: the homologous-recombination deficiency (BRCA already mapped) generates the cytosolic DNA that activates the cGAS-STING (already mapped) type-I interferon, the innate immunogenicity of the HBOC tumours.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the M2 (IL-4 and IL-13 already mapped) macrophages populate the immunosuppressive stroma of the HBOC tumours, opposing the neoantigen (T-cell already mapped) immunity.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, enhanced by the HRD (BRCA already mapped) neoantigen load and the PARP-inhibitor-induced immunogenicity of HBOC tumours.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm counter to the M2 macrophage (already mapped) immunosuppression of the HBOC tumour microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the HBOC tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the HBOC tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the HBOC tumours.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral arm: the plasma cells secrete the anti-tumour antibodies (already mapped) of the humoral response, which in the BRCA-mutant (already mapped) homologous-recombination-deficient tumours can be enhanced by the higher neoantigen load.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, associates with the immunotherapy (PD-1 already mapped) response of the higher-neoantigen HRD-deficient HBOC tumours.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the HBOC tumours.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the HBOC tumour stroma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the HBOC tumour microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the HBOC tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the BRCA-deficient (already mapped) proliferating cells of the HBOC tumours.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-HBOC axis: TSLP, from the BRCA-deficient (already mapped) tumour stroma and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of HBOC-associated breast and ovarian cancers.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-HBOC axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), augments vascular permeability and the inflammatory stromal milieu of HBOC-associated breast and ovarian cancers.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-HBOC axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and anaemia of HBOC-associated cancers, activates the EPOR on BRCA-deficient (already mapped) tumour cells and modulates macrophage (already mapped) polarisation in the tumour microenvironment.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-HBOC axis: histamine, from mast cells in the HBOC tumour stroma, signals via H1/H2 receptors on BRCA-deficient (already mapped) tumour cells, promoting angiogenesis, immune evasion, and the pro-tumourigenic milieu of HBOC-associated breast and ovarian cancers.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-HBOC axis: melatonin, via MT1/MT2 receptors on BRCA-deficient (already mapped) tumour cells, suppresses HIF-1α (already mapped) and oestrogen-receptor-driven proliferation, modulates circadian breast-cancer risk, and enhances PARP-inhibitor sensitivity.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-HBOC axis: testosterone, via androgen receptor signalling on BRCA-deficient (already mapped) breast and ovarian tumour cells, modulates HER2 (already mapped) and PARP-inhibitor sensitivity, and the sex-biased hormonal milieu of HBOC-associated cancers.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — HBOC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the BRCA-deficient immune TME; hyperprolactinaemia amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of HBOC.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — HBOC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of HBOC.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — HBOC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of hereditary breast-ovarian cancer.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — HBOC serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the TME; serotonin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of HBOC.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — HBOC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) oxidative tumour cascade of HBOC.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — HBOC iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of HBOC.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — HBOC sodium: high dietary sodium promotes Th17 polarisation and macrophage (already mapped) activation; sodium-induced IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) and T-helper-cell (already mapped) tumour cascade of HBOC.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — HBOC magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies IL-6 (already mapped) and T-helper-cell (already mapped) tumour-promoting cascade of HBOC.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — HBOC copper: copper supports macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour function; copper deficiency amplifies IL-6 (already mapped) and T-helper-cell (already mapped) tumour-promoting cascade of HBOC.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — HBOC potassium: potassium regulates macrophage (already mapped) and T-cytotoxic (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) tumour-promoting cascade in HBOC.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — HBOC zinc: zinc cofactors macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) tumour-promoting inflammatory cascade in HBOC.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — HBOC phosphorus: phosphorus as ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) fuels anti-tumour kinase signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — HBOC carbon: carbon in nucleotides of macrophages (already mapped) and T-cytotoxic cells (already mapped) fuels anti-tumour proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) cascade in HBOC.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — HBOC chloride: chloride channels on macrophages (already mapped) and T-cytotoxic cells (already mapped) regulate ionic anti-tumour signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) cascade in HBOC.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — HBOC hydrogen: hydrogen via ROS from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-helper-cell (already mapped) cascade in HBOC.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — HBOC glp-1: GLP-1 from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) anti-tumour cascade in HBOC.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — HBOC angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and BRCA1 (already mapped) anti-tumour cascade in HBOC.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — HBOC wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and T-cytotoxic cells (already mapped) regulates tumour immune tone; wnt-beta-catenin dysregulation amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — HBOC fibronectin: fibronectin in macrophages (already mapped) and T-cytotoxic cells (already mapped) promotes tumour ECM remodelling; fibronectin excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — HBOC notch: Notch signalling on macrophages (already mapped) and T-cytotoxic cells (already mapped) regulates tumour immune recognition; notch excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — HBOC igf-1: IGF-1 from macrophages (already mapped) and T-cytotoxic cells (already mapped) promotes tumour immune resistance; igf-1 excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — HBOC activin-a: activin-A from macrophages (already mapped) and T-cytotoxic cells (already mapped) regulates tumour immune-fibrotic balance; activin-a excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — HBOC cgrp: CGRP from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour neuroimmune tone; cgrp excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — HBOC calcitonin: calcitonin from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour calcium signalling; calcitonin excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — HBOC substance-p: substance-P from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour pain tone; substance-P excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — HBOC insulin-receptor: insulin receptor on macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour metabolic axis; insulin-receptor loss amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — HBOC aldosterone: aldosterone from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates tumour fluid balance; aldosterone excess amplifies BRCA1 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade in HBOC.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^kuchenbaecker-2017-brca-risks]: Kuchenbaecker KB, Hopper JL, Barnes DR, et al. Risks of Breast, Ovarian, and Contralateral Breast Cancer for BRCA1 and BRCA2 Mutation Carriers. *JAMA.* 2017;317(23):2402-2416. [doi:10.1001/jama.2017.7112](https://doi.org/10.1001/jama.2017.7112) · [PubMed 28632853](https://pubmed.ncbi.nlm.nih.gov/28632853/)
[^antoniou-2014-palb2-risk]: Antoniou AC, Casadei S, Heikkinen T, et al. Breast-cancer risk in families with mutations in PALB2. *N Engl J Med.* 2014;371(6):497-506. [doi:10.1056/NEJMoa1400382](https://doi.org/10.1056/NEJMoa1400382) · [PubMed 25099575](https://pubmed.ncbi.nlm.nih.gov/25099575/)
