---
schema: human-scale-entry/v1
id: endometrial-cancer
name: Endometrial Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common gynecologic malignancy in the US (~67,000/year); POLE-ultramutated and MSI-H subtypes respond to pembrolizumab; endometrioid type driven by PTEN/PIK3CA/KRAS; serous by TP53/ERBB2. Carboplatin+paclitaxel is standard; dostarlimab approved for dMMR endometrial cancer."
aliases: ["endometrial cancer", "endometrial carcinoma", "uterine cancer", "endometrioid adenocarcinoma", "uterine serous carcinoma", "POLE-ultramutated", "Lynch-associated endometrial cancer"]
sources:
  - id: konstantinopoulos-2019-dostarlimab
    type: peer-reviewed
    cite: "Konstantinopoulos PA, Lheureux S, Moore KN. PARP inhibitors for ovarian and endometrial cancers: state of the art and clinical perspectives. J Clin Oncol. 2020;38(25):2896-2909."
    doi: "10.1200/JCO.20.00571"
    pmid: "32706635"
    url: "https://doi.org/10.1200/JCO.20.00571"
  - id: eskander-2023-ruby
    type: peer-reviewed
    cite: "Eskander RN, Sill MW, Beffa L, et al. Pembrolizumab plus chemotherapy in advanced endometrial cancer. N Engl J Med. 2023;388(23):2159-2170."
    doi: "10.1056/NEJMoa2302312"
    pmid: "37166384"
    url: "https://doi.org/10.1056/NEJMoa2302312"
cross_links:
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss in ~50-80% of endometrioid endometrial cancer; earliest molecular event in endometrial carcinogenesis; PTEN loss → PI3K-AKT-mTOR activation → proliferation; mTOR inhibitors (everolimus+letrozole) active in ER+ disease; germline PTEN mutations cause Cowden syndrome."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "dMMR endometrial cancer (~25-30%) responds to pembrolizumab; KEYNOTE-158 ORR 57%; dostarlimab FDA approved 2021 for dMMR recurrent endometrial; RUBY trial improved OS in dMMR subset; PD-1 blockade is standard for dMMR recurrent disease."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "ERBB2/HER2 amplification in ~30% of uterine serous carcinoma and carcinosarcoma; trastuzumab+carboplatin/paclitaxel improved PFS (Fader 2018); HER2+ USC is actionable; T-DXd studied in HER2-low endometrial; HER2 testing recommended for serous histology."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K/AKT/mTOR activated in ~70% of endometrioid endometrial cancer (PTEN loss, PIK3CA ~40%, AKT1 E17K); everolimus+letrozole → 32% clinical benefit in ER+ disease; lenvatinib+pembrolizumab (KEYNOTE-146) active in non-MSI-H recurrent endometrial cancer."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Unopposed estrogen drives endometrial hyperplasia → EIN → type 1 endometrioid cancer; obesity → adipose aromatase → androgen-to-estrogen conversion → ~3× EC risk at BMI >30; aromatase inhibitors active in ER+ endometrial cancer; combined HRT (with progestogen) prevents EC risk."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Progesterone drives endometrial secretory transformation opposing estrogen proliferation; mifepristone (PR/GR antagonist) blocks P4 receptor → decidual breakdown → pregnancy termination; progesterone supplementation treats luteal phase deficiency and recurrent miscarriage."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Endometrial cancer is the sentinel cancer of Lynch syndrome: about half of female carriers present with it before any colorectal cancer, so a young or dMMR endometrial tumour should prompt germline testing — and these MSI-H cancers respond well to PD-1 immunotherapy."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is the dominant modifiable driver of endometrial cancer: adipose aromatase converts androgens to estrogen, and this unopposed estrogen pushes endometrium through hyperplasia to type-1 endometrioid cancer — roughly tripling risk at BMI >30 and fueling rising incidence."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation defines the most aggressive endometrial cancers: near-universal (~90%) in uterine serous carcinoma, it marks the copy-number-high TCGA group with the worst prognosis, unlike the estrogen-driven endometrioid tumours — a split that now guides adjuvant therapy."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Endometrial and breast cancers are linked estrogen-driven cancers: unopposed estrogen and obesity raise risk of both, and tamoxifen used for breast cancer acts as a uterine estrogen agonist that increases endometrial cancer risk—so bleeding on tamoxifen warrants evaluation."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Endometrial and ovarian cancers frequently co-occur: ~10% of endometrioid endometrial cancers have a synchronous endometrioid ovarian primary, and both are core Lynch-syndrome tumors from mismatch-repair deficiency—so MMR/MSI testing and gynecologic surveillance span the two."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Endometrial and colorectal cancer are the defining Lynch-syndrome malignancies: germline mismatch-repair mutations (MLH1, MSH2/6, PMS2) drive microsatellite instability in both, endometrial cancer is often the sentinel cancer in women, and MSI-high tumors take immunotherapy."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Cowden syndrome is a hereditary cause of endometrial cancer: germline PTEN loss unleashes PI3K/mTOR signaling in the endometrium—the pathway mutated in most sporadic endometrioid tumors—so PTEN carriers face raised endometrial, breast, and thyroid cancer risk."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes and endometrial cancer are tied via obesity and hyperinsulinemia: excess insulin and adipose estrogen stimulate endometrial proliferation, so diabetic, obese women face much higher endometrial cancer risk—metformin is studied as prevention."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Mismatch-repair-deficient (MSI-high) endometrial cancer is highly immunotherapy-responsive: defective DNA repair generates abundant neoantigens that draw cytotoxic CD8+ T cells, so anti-PD-1 (dostarlimab, pembrolizumab) has transformed treatment of dMMR endometrial tumors."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is a key adjuvant in endometrial cancer: after hysterectomy, vaginal brachytherapy or pelvic external-beam photon radiation lowers local recurrence, and radiation can treat inoperable patients—complementing surgery in the commonest gynecologic cancer."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Endometrial cancer is the commonest gynecologic-tract cancer of the reproductive system: arising from the estrogen-responsive uterine lining, it is driven by unopposed estrogen, so the reproductive system's own hormonal milieu fuels the tumor."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "Endometrial and uterine tumors link endometrial cancer to HLRCC: fumarate-hydratase loss causes the uterine leiomyomas that name HLRCC and FH-deficient uterine cancers—so uterine smooth-muscle or endometrial tumors with a family history may flag the HLRCC mutation."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutation is among the commonest drivers of endometrial cancer: it activates the PI3K/AKT/mTOR growth pathway (often alongside PTEN loss), so this axis is a leading target for the mTOR and PI3K inhibitors being developed for the disease."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Endometrial cancer is tightly linked to insulin and metabolic excess: obesity and type 2 diabetes raise insulin and IGF-1, which—with the estrogen made by fat tissue—stimulate endometrial proliferation, explaining why metabolic disease so strongly raises risk."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Endometrial cancer is the prototypical hormone-dependent tumor of the endocrine system: unopposed estrogen without progesterone drives endometrial overgrowth, so conditions and drugs that disturb the estrogen-progesterone balance change the risk markedly."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Endometrial cancer is staged through the lymphatic system: spread to pelvic and para-aortic nodes drives staging and prognosis, so sentinel-lymph-node mapping now guides how aggressively surgery and adjuvant therapy are pursued."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "CTNNB1 mutations define a deceptive endometrial subgroup: activating this Wnt/beta-catenin gene marks low-grade endometrioid tumors that look indolent but carry a surprisingly high recurrence risk—part of the molecular classification reshaping endometrial cancer care."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Endometrial cancer can spread to the lung: high-grade and serous subtypes disseminate hematogenously, making the lung a common distant metastatic site, so chest imaging is part of staging advanced or recurrent disease."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Endometrial cancer's molecular classes hinge on MMR genes like MLH1: silencing of MLH1 by promoter methylation creates the common microsatellite-instability subtype, which is hypermutated and responds well to checkpoint immunotherapy—so MMR testing guides treatment."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Depth of myometrial invasion stages endometrial cancer, and fibroblasts pave the way: cancer-associated fibroblasts remodel the stroma to let tumor burrow into the muscle wall, and how deep it goes is a key prognostic factor guiding surgery."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Advanced endometrial cancer is treated by hitting VEGF: lenvatinib (a VEGFR inhibitor) plus pembrolizumab became a standard for recurrent disease, choking the tumor's blood supply while unleashing the immune system."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Body fat is the engine of endometrial cancer: adipocytes make aromatase that turns androgens into estrogen, so obesity floods the uterine lining with unopposed estrogen, making it the malignancy most strongly tied to excess weight."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver tunes endometrial-cancer risk through SHBG: it makes sex-hormone-binding globulin that mops up estrogen, and obesity and insulin resistance lower SHBG, raising the free estrogen that drives this hormone-sensitive tumor."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages connect obesity to endometrial cancer: inflamed fat draws macrophages that pour out cytokines, and tumor-associated macrophages in the uterine tumor promote its growth and blood supply, a cellular bridge from adiposity to malignancy."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Endometrial cancer announces itself by spending iron: abnormal uterine bleeding—especially after menopause—is the cardinal warning sign, and the chronic blood loss drains the body's iron into a deficiency anemia that often prompts the diagnosis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells matter most in mismatch-repair-deficient endometrial cancer: these immunogenic tumors draw NK and T-cell attack, part of why such cancers respond well to immunotherapy that unleashes the immune assault."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Advanced endometrial cancer can threaten the kidneys: a bulky uterine tumor or its pelvic spread compresses the ureters, backing urine up into the kidneys (hydronephrosis) and causing post-renal kidney injury."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Endometrial cancer and its treatment leave fibrosis: a reactive desmoplastic stroma surrounds the tumor, and pelvic radiation scars nearby tissues, a late cause of bowel and bladder problems in survivors."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endometrial cancer drives angiogenesis: VEGF recruits endothelial cells to vascularize the tumor, and the fragile new vessels contribute to the abnormal bleeding that usually reveals it early."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Endometrial cancer can invade the bowel: locally advanced disease spreads to the rectum and sigmoid colon and seeds the peritoneum, complicating surgery and signaling advanced spread."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy separates endometrial cancer's two faces: the common endometrioid type keeps orderly glandular cells with microvilli, while the aggressive serous type shows papillary tufts and chaotic nuclei, an ultrastructural divide that tracks prognosis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Serous endometrial cancer leaves calcium fingerprints: like its ovarian counterpart it forms psammoma bodies, concentric calcium deposits whose presence on histology flags the high-grade serous subtype."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D ties into endometrial cancer through fat: deficiency travels with the obesity that is its biggest risk factor, and the vitamin's influence on cell growth and estrogen metabolism has made it a focus of prevention research."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The cancer announces itself in blood: postmenopausal bleeding is the cardinal early sign, and chronic abnormal uterine bleeding can drain enough red cells and iron to leave a woman anemic before the diagnosis is made."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Advanced disease draws on nerve-toxic chemotherapy: the carboplatin-paclitaxel regimen used for high-risk endometrial cancer injures peripheral sensory neurons, leaving the numbness and tingling of a taxane neuropathy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Platinum chemotherapy wastes magnesium: the carboplatin paired with paclitaxel injures the kidney's tubular handling of the mineral, so magnesium is checked and replaced through endometrial cancer treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies now classify and treat it: mismatch-repair and p53 immunostains sort endometrial cancers into molecular groups, and the MMR-deficient tumors respond to checkpoint antibodies like dostarlimab and pembrolizumab."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The carboplatin-paclitaxel backbone empties the marrow: both drugs are myelosuppressive, dropping neutrophil counts between cycles so that growth-factor support and febrile-neutropenia watch run through advanced-disease treatment."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet and weight are the dominant levers: obesity-driven excess estrogen is the leading modifiable cause, so weight loss and a high-fiber, plant-rich diet that lowers circulating estrogen reduce endometrial cancer risk."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The obesity-diabetes link runs through IGF-1: hyperinsulinemia raises bioactive IGF-1, a potent mitogen that, with excess estrogen, fuels endometrial proliferation — a molecular reason metabolic disease drives this cancer."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells help the tumor hide: they accumulate in the endometrial tumor microenvironment and damp the antitumor response, a dynamic that matters most in the mismatch-repair-deficient tumors targeted by immunotherapy."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "An STK11 syndrome raises the risk: Peutz-Jeghers syndrome predisposes to endometrial cancer and the rare cervical adenoma malignum, one of the inherited routes to gynecologic cancer beyond Lynch and Cowden."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "A chromatin gene falters early: ARID1A, part of the SWI/SNF remodeling complex, is frequently mutated in endometrioid endometrial cancer, loosening gene regulation as one of the disease's commonest driver events."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS pushes the endometrioid type: activating KRAS mutations fire the MAPK growth pathway in the estrogen-driven endometrioid subtype, often alongside PTEN and PIK3CA loss in the same tumor."
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "Lynch lands hardest on the womb: germline mismatch-repair defects in genes like MSH2 make endometrial cancer the sentinel cancer of Lynch syndrome in women, and the resulting MSI makes these tumors immunotherapy-responsive."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Obesity-driven inflammation feeds the tumor through NF-κB: the chronic inflammation of excess fat activates NF-κB in the endometrium, adding a pro-survival, pro-proliferative push to the estrogen excess that drives type I endometrial cancer."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "An obese cancer prone to clots: endometrial cancer, usually arising in obese patients, carries a high venous thromboembolism risk that pelvic surgery and the tumor's own procoagulant state compound."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Surgery and chemo open the door to infection: hysterectomy, the mainstay treatment, and the neutropenia of chemotherapy for advanced disease make postoperative infection and sepsis recognized hazards."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Bleeding and inflammation both lower the count: alongside the iron-deficiency anemia from abnormal uterine bleeding, the tumor's inflammatory burden raises hepcidin and suppresses erythropoiesis into an anemia of chronic disease."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Advanced pelvic disease can obstruct the kidneys: locally invasive or recurrent endometrial cancer can compress the ureters, and platinum chemotherapy adds nephrotoxicity, together threatening chronic kidney disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Diagnosis and treatment weigh on mood: the cancer diagnosis, surgical menopause from hysterectomy-oophorectomy and the demands of treatment contribute to a substantial burden of depression."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Removing the ovaries withdraws bone-protective estrogen: the hysterectomy with oophorectomy that treats endometrial cancer throws younger patients into surgical menopause, accelerating bone loss toward osteoporosis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "It rides on a cardiometabolic profile: endometrial cancer's strong association with obesity, diabetes and hypertension means these patients carry a heavy cardiovascular burden that predisposes to heart failure."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemotherapy for advanced disease opens the lung to mold: the neutropenia from carboplatin-paclitaxel treatment of high-risk or recurrent endometrial cancer can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Hysterectomy is its central surgery: total hysterectomy with lymph-node dissection treats endometrial cancer, and obesity and diabetes — its main risk factors — leave these abdominal wounds slow and infection-prone."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its taxane chemo numbs the nerves: the carboplatin-paclitaxel regimen for advanced or high-risk endometrial cancer causes a dose-dependent, often lasting peripheral neuropathy."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Recurrence surveillance breeds worry: the monitoring for relapse and the body-image and fertility-loss impact of hysterectomy in endometrial cancer foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to the lungs: the lungs are a common site of distant metastasis in endometrial cancer, found on staging imaging and at recurrence as pulmonary nodules."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Mismatch-repair failure makes it treatable by immunotherapy: dMMR/MSI-high endometrial tumours — common and often linked to Lynch syndrome — respond to checkpoint-inhibitor therapy."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "A bulky pelvic tumour can block the ureters: locally advanced endometrial cancer can obstruct the ureters, causing hydronephrosis and post-renal acute kidney injury."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Shared metabolic roots: the obesity, insulin resistance and unopposed oestrogen that drive type-I endometrial cancer are the same risk cluster behind cardiovascular disease, a leading cause of death in survivors."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Advanced disease spreads within the abdomen: endometrial cancer seeds the omentum and bowel surfaces, and platinum-taxane chemotherapy brings nausea and mucositis."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It can surface at the navel: like other intra-abdominal cancers it occasionally seeds a Sister Mary Joseph nodule at the umbilicus, a visible sign of peritoneal spread."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Mismatch-repair loss makes it immunogenic: about a quarter of endometrial cancers are dMMR/MSI-high and respond strongly to PD-1 inhibitors like pembrolizumab, now central to advanced and Lynch-associated disease."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Molecular drivers guide newer drugs: lenvatinib (anti-VEGFR) with pembrolizumab, mTOR inhibitors for PTEN-altered tumours and anti-HER2 antibody-drug conjugates for HER2-positive serous cancer extend treatment options."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "A diabetes drug studied against it: metformin lowers the insulin and IGF-1 signalling that fuels endometrial cancer, and is investigated as adjunct and chemoprevention in the obese, insulin-resistant women most at risk."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Carboplatin-paclitaxel for advanced disease: while early endometrial cancer is cured by surgery, advanced and high-grade (serous, carcinosarcoma) disease relies on platinum-taxane chemotherapy, now often combined with immunotherapy."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "The two uterine cancers contrasted: endometrial cancer arises from the hormone-responsive uterine lining driven by unopposed oestrogen and obesity, whereas cervical cancer arises from HPV infection of the cervix — different organs, causes and prevention."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "A shared ARID1A/endometriosis pathway: endometrioid and clear-cell cancers of both the uterus and ovary arise from endometriosis-like glands with ARID1A and PIK3CA mutations, linking these gynaecological malignancies mechanistically."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Why it responds to immunotherapy: mismatch-repair-deficient (MSI-high) endometrial cancers—Lynch and sporadic—accumulate neoantigens and tertiary lymphoid structures with germinal-centre B cells, the immune richness behind checkpoint-inhibitor response."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Two cancers of the Lynch spectrum: endometrial cancer is the sentinel Lynch-syndrome cancer in women and gastric cancer is another mismatch-repair-deficient Lynch tumour—shared MMR loss across the uterus and stomach."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Shared metabolic roots with heart disease: the obesity, insulin resistance and unopposed oestrogen that drive endometrial cancer also accelerate arterial-wall atherosclerosis, so cardiovascular disease is a leading cause of death in survivors."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Lung as a metastatic site: endometrial cancer, especially serous and high-grade subtypes, spreads haematogenously to the lungs, seeding nodules in the alveolar parenchyma in advanced disease."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver metastasis: advanced endometrial cancer can spread to the liver, seeding the hepatic lobules, a marker of disseminated disease beyond its usual pelvic and nodal spread."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Lynch beyond gut and uterus: the mismatch-repair deficiency behind hereditary endometrial cancer also raises urothelial (bladder and ureter) cancer risk, part of the broad Lynch tumour spectrum."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The Lynch sentinel: in women with Lynch syndrome, endometrial cancer often appears before colorectal cancer, the same mismatch-repair loss driving tumours in the uterine and intestinal epithelium."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Serous, p53-driven disease: the aggressive serous subtype of endometrial cancer is TP53-mutated, and germline TP53 (Li-Fraumeni) adds it to that syndrome's broad cancer spectrum."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Obesity and disrupted care: the obesity that drives endometrial cancer also worsens COVID-19, and the pandemic delayed diagnosis of postmenopausal bleeding and gynaecological-cancer surgery."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT engine: with PTEN loss and PIK3CA mutation near-universal in endometrioid tumours, AKT is constitutively active to drive growth and survival, making the PI3K/AKT/mTOR axis a key target."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: oestrogen-driven endometrial cancer relies on cyclin D-CDK4/6 to pass the G1 checkpoint, and CDK4/6 inhibition with endocrine therapy is under active investigation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in hypoxic endometrial tumours promotes the VEGF angiogenesis, glycolysis and invasion that mark the more aggressive, higher-grade disease."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Serous-subtype oncogene: MYC amplification helps drive the copy-number-high, p53-mutant serous endometrial cancers, the most aggressive molecular subtype with the poorest prognosis."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase reactivation: TERT activation immortalises endometrial cancer cells, sustaining the unlimited proliferation that complements the PI3K and mismatch-repair lesions of the disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Tumour microenvironment: CCL2 secreted by endometrial tumours recruits tumour-associated macrophages that promote angiogenesis and immune evasion, linked to obesity-driven inflammation in the disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Hypermutation immunogenicity: the mismatch-repair-deficient and POLE-ultramutated endometrial cancers accumulate cytosolic DNA that activates cGAS-STING, the innate-immune basis for their strong response to checkpoint inhibitors."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity link: leptin from excess adipose tissue stimulates endometrial epithelial proliferation through JAK-STAT and PI3K signalling, a key mechanism connecting obesity — the dominant risk factor — to endometrial carcinogenesis."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Invasion and EMT: TGF-β drives the epithelial-mesenchymal transition and stromal remodelling that enable myometrial invasion, the depth of which is the key determinant of stage and prognosis in endometrial cancer."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Recurrent driver: activating FGFR2 mutations occur in a substantial fraction of endometrioid endometrial cancers and are associated with worse outcome, a targetable oncogenic driver distinct from the dominant PTEN/PI3K and mismatch-repair lesions."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: carboplatin-paclitaxel, the backbone of advanced endometrial-cancer treatment, kills tumour cells through caspase-3-mediated apoptosis, the death pathway whose evasion underlies chemoresistance in serous and high-grade disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic spread: CXCR4-CXCL12 signalling directs endometrial-cancer cells toward the pelvic lymph nodes and peritoneum, the lymphatic and transcoelomic routes of spread that define advanced-stage disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK arm: KRAS and FGFR2 mutations (already mapped) in endometrioid endometrial cancer activate the MAPK-ERK pathway, a proliferative driver complementing the dominant PI3K-AKT axis."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: the CDK4/6-RB-E2F axis (CDK4/6 already mapped) powers the cell-cycle progression of endometrial cancer, particularly the estrogen-stimulated proliferation of endometrioid tumours."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Hormonal survival: estrogen induces anti-apoptotic BCL-2 in the endometrium, and its overexpression supports the survival of endometrioid endometrial-cancer cells in this hormonally driven tumour."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Obesity-driven inflammation: adipose-derived IL-6 fuels the chronic inflammatory and estrogenic milieu of obesity that is the dominant modifiable risk factor for endometrioid endometrial cancer, promoting tumour-cell proliferation and survival."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 inactivation: MDM2 amplification degrades p53, providing an alternative route to loss of p53 tumour-suppressor function in serous endometrial cancer beyond the TP53 mutations that define this aggressive subtype."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Oncogenic Wnt: constitutive Wnt/β-catenin signalling — through CTNNB1 exon-3 mutations — defines a molecular subgroup of endometrioid endometrial cancer associated with younger age and recurrence risk."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-JAK-STAT3 signalling (IL-6 mapped) links the obesity-associated inflammatory state to proliferation and immune evasion in endometrial cancer."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A loss releases CDK4/6-cyclin-D control (CDK4/6 mapped) of the cell cycle, a recurrent lesion contributing to endometrial carcinogenesis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Altered TGF-β-SMAD signalling (TGF-β mapped) contributes to invasion and epithelial-mesenchymal transition in aggressive endometrial cancer."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports immune evasion and the invasive progression of endometrial cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of endometrial cancer, particularly the immunotherapy-responsive mismatch-repair-deficient subtype."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression silences tumour-suppressor genes and contributes to the epigenetic dysregulation of endometrial cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PTEN-loss-driven PI3K-AKT signaling (PTEN, AKT, and PIK3CA already mapped) inactivates FOXO, removing a tumor-suppressive brake in endometrial cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunotherapy-responsive mismatch-repair-deficient endometrial cancer must evade."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from infiltrating myeloid cells promote the inflammatory, often obesity-linked, microenvironment of endometrial cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates β-catenin stability (CTNNB1/Wnt already mapped), a pathway aberrantly activated in the endometrioid subtype of endometrial cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of HER2 and growth-factor receptors contributes to the invasion of endometrial cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of MLH1 and other tumor-suppressor genes in endometrial cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of endometrial cancer cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling, coupled to the obesity and insulin-resistance risk (insulin already mapped), participates in endometrial cancer."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven macrophage recruitment shapes the inflammatory microenvironment of endometrial cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation, linked to the obesity-associated pathogenesis, participates in the tumor microenvironment of endometrial cancer."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the proliferation and differentiation programs dysregulated in endometrial cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of endometrial cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of endometrial cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of endometrial cancer."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the estrogen-linked proliferative and immune signaling of endometrial cancer."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy subtypes: the mismatch-repair-deficient (MSI, MLH1/MSH2 already mapped) and POLE-ultramutated endometrial cancers generate abundant neoantigens presented on MHC, making them the subtypes most responsive to checkpoint inhibitors."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Obesity risk: obesity is the leading modifiable risk factor for endometrial cancer, and low adiponectin alongside the leptin excess already mapped links adipose dysfunction and insulin resistance to endometrial carcinogenesis."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Treatment resistance: the AXL receptor tyrosine kinase promotes epithelial-mesenchymal transition and therapy resistance in endometrial cancer, a route of progression beyond the hormonal and PI3K-pathway drivers already mapped."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "MSI immunotherapy: the mismatch-repair-deficient endometrial cancers (MLH1/MSH2 already mapped) are neoantigen-rich and respond to checkpoint blockade (PD-1 already mapped), and IL-2-driven T-cell activity underlies this immune sensitivity."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Bleeding anaemia: abnormal uterine and postmenopausal bleeding is the cardinal presentation of endometrial cancer, and the chronic blood loss produces an iron-deficiency anaemia lowering haemoglobin that often prompts diagnosis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic dyslipidaemia: the obesity and insulin resistance (already mapped) that drive endometrial cancer come with atherogenic dyslipidaemia, and cholesterol metabolism intersects the estrogen and mTOR pathways fuelling the tumour."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammation-estrogen link: cyclooxygenase-2-derived prostaglandin E2 in the endometrial tumour and adipose stroma induces aromatase and local estrogen (already mapped) synthesis, linking the obesity-associated inflammation to the hormone drive of endometrial cancer."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), the immune evasion that is more readily overcome in the mismatch-repair-deficient (MLH1 already mapped) tumours."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and lysis stress: the chemotherapy of advanced endometrial cancer generates oxidative stress and cell lysis releasing purines that xanthine oxidase converts to uric acid, adding an oxidative and tumour-lysis burden to treatment."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the mismatch-repair-proficient endometrial cancers."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Bleeding and anaemia: the abnormal uterine bleeding that presents most endometrial cancer causes iron-deficiency anaemia (haemoglobin already mapped), and the chemotherapy of advanced disease adds a transfusional iron burden."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary metastases: the lungs are a common site of metastasis of advanced and serous (p53 already mapped) endometrial cancer, the haematogenous spread driving the prognosis of high-risk disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of endometrial cancer."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages (CCL2 already mapped) of the endometrial-cancer stroma, in their M2 (IL-4 already mapped) phenotype, drive the immunosuppression and angiogenesis (VEGF already mapped) of the tumour."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "PTEN hamartoma syndrome: Cowden syndrome (germline PTEN already mapped) markedly raises the risk of endometrial cancer, part of the hereditary predisposition alongside Lynch syndrome (already mapped)."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity (already mapped) risk of the type-1 endometrial cancer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "MSI immunogenicity: the cGAS-STING (already mapped) sensing of the genomic instability of the MMR-deficient/MSI (MLH1 and MSH2 already mapped) endometrial cancer drives the type-I interferon behind the checkpoint (PD-1 already mapped) response."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "BRCA-associated risk: the hereditary breast-ovarian cancer syndrome (germline BRCA) carries an increased serous endometrial-cancer risk, part of the PARP-inhibitor rationale."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of the MSI-high endometrial cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the endometrial-cancer immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of endometrial cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of endometrial cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the endometrial-cancer microenvironment."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 TIL source: the CD4 T-helper cells of the tumour-infiltrating lymphocytes are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the MSI-high/POLE immune response of endometrial cancer."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of endometrial cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, marks the favourable immune response of the MSI-high/POLE endometrial cancer."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the tumour neoantigen to the T cells (already mapped), driving the checkpoint (PD-1 already mapped) response of the MSI-high endometrial cancer."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory and immunosuppressive dimension of the endometrial-cancer microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid (macrophage already mapped) recruitment and immunosuppression of the endometrial-cancer microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the endometrial-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the microenvironment."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-tumour axis: TSLP, from cancer-associated fibroblasts (already mapped) and tumour stroma, primes dendritic cells (already mapped) and mast cells (already mapped) toward the Th2 immunosuppressive bias of the endometrial-cancer microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-tumour axis: bradykinin, via the kallikrein-kinin system in the tumour microenvironment, amplifies the vascular permeability and the pro-tumorigenic myeloid (macrophage already mapped) recruitment in endometrial cancer."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia of cancer: erythropoietin corrects the cancer-related and chemotherapy-induced anaemia of endometrial cancer; EpoR expression on tumour cells also modulates a potential direct proliferative signal."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell stroma: mast cells (already mapped) in the endometrial-cancer stroma release histamine that amplifies VEGF (already mapped)-driven angiogenesis and the type-2 microenvironment (IL-4, IL-13 already mapped) of the tumour."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Stromal matricellular: periostin, secreted by cancer-associated fibroblasts (already mapped) in the endometrial-cancer stroma, promotes invasive myometrial penetration and TGF-β (already mapped)-linked epithelial-mesenchymal transition."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor modulates the classical complement pathway (C3, C5 and C5aR1 already mapped) within the endometrial-cancer microenvironment, attenuating complement-driven myeloid recruitment."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "EC testosterone: testosterone, via androgen receptors on endometrial cells, modulates the estrogen (already mapped)-mTOR (already mapped) proliferative axis; low androgen-to-oestrogen ratios in obesity (already mapped) amplify Type I endometrial carcinogenesis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "EC serotonin: serotonin, via 5-HT receptors on endometrial cells and macrophages (already mapped), promotes VEGF (already mapped)-driven angiogenesis; serotonin excess amplifies the estrogen (already mapped) and mTOR (already mapped) proliferative milieu of endometrial cancer."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "EC prolactin: prolactin, via PRLR on endometrial cells and macrophages (already mapped), promotes mTOR (already mapped)-driven tumour proliferation; hyperprolactinaemia amplifies the estrogen (already mapped)-linked uterine proliferative axis of Type I endometrial cancer."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "EC oxytocin: oxytocin, via OXTR on endometrial-cancer cells, suppresses mTOR (already mapped) and NF-κB (already mapped) tumour-proliferative signalling; oxytocin attenuates estrogen (already mapped)-driven angiogenesis and the VEGF (already mapped) pro-tumourigenic milieu."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "EC vasopressin: vasopressin, via V1bR on endometrial cells, promotes CRH-cortisol (already mapped) immune suppression in the tumour microenvironment; vasopressin amplifies the mTOR (already mapped) and NF-κB (already mapped) pro-tumourigenic milieu of endometrial cancer."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "EC selenium: selenium, via GPx and selenoproteins, suppresses ROS-driven NF-κB (already mapped) and mTOR (already mapped) tumour-proliferative signalling; selenium induces apoptosis and attenuates estrogen (already mapped)-linked carcinogenesis in endometrial cancer."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "EC zinc: zinc cofactors estrogen receptor (already mapped) signalling and macrophage (already mapped) anti-tumour immunity; zinc deficiency amplifies NF-κB (already mapped) and mTOR (already mapped)-driven endometrial tumour proliferation and angiogenesis in endometrial cancer."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "EC iodine: thyroid hormones (iodine-dependent) modulate estrogen-receptor (already mapped) activity in endometrial cells; iodine deficiency amplifies NF-κB (already mapped) and mTOR (already mapped) proliferative signalling and IL-6 (already mapped) tumour inflammation."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "EC sodium: sodium-driven osmotic stress on endometrial cells amplifies NF-κB (already mapped) and mTOR (already mapped) tumour-proliferative signalling; sodium-stimulated IL-6 (already mapped) and VEGF (already mapped) promote the pro-tumourigenic milieu of endometrial cancer."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "EC copper: copper, via ceruloplasmin and SOD, in macrophages (already mapped) and fibroblasts (already mapped), scavenges ROS; copper excess amplifies NF-κB (already mapped) and mTOR (already mapped) endometrial tumour growth via VEGF (already mapped) angiogenesis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "EC potassium: potassium regulates macrophage (already mapped) and endometrial epithelial membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and mTOR (already mapped) and IL-6 (already mapped) tumour-proliferative signalling of endometrial cancer."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "EC phosphorus: phosphorus, as ATP in macrophages (already mapped) and fibroblasts (already mapped), fuels tumour-stromal crosstalk; phosphorus excess amplifies NF-κB (already mapped) and mTOR (already mapped) and VEGF (already mapped) endometrial cancer cascade."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "EC chloride: chloride channels on macrophages (already mapped) and endothelial cells (already mapped) regulate ionic homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) endometrial cancer cascade."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "EC carbon: carbon backbone of nucleotides in macrophages (already mapped) and endothelial cells (already mapped) fuels tumour growth; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) endometrial cancer cascade."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "EC hydrogen: hydrogen via ROS from macrophages (already mapped) and endothelial cells (already mapped) modulates tumour oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) endometrial cancer cascade."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "EC nitrogen: nitrogen in DNA bases of macrophages (already mapped) and endothelial cells (already mapped) sustains tumour growth; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) endometrial cancer cascade."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "endometrial-cancer glp-1: GLP-1 from macrophages (already mapped) and endometrial cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "endometrial-cancer angiotensin-ii: angiotensin II on endometrial cells (already mapped) and macrophages (already mapped) drives angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "endometrial-cancer rankl: RANKL from endometrial cells (already mapped) and macrophages (already mapped) modulates immune invasion; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "endometrial-cancer fibronectin: fibronectin in endometrial cells (already mapped) and macrophages (already mapped) promotes ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "endometrial-cancer activin-a: activin-A from endometrial cells (already mapped) and macrophages (already mapped) promotes tumour-stromal invasion; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "endometrial-cancer cgrp: CGRP from endometrial cells (already mapped) and macrophages (already mapped) modulates uterine nociception; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "endometrial-cancer calcitonin: calcitonin from endometrial cells (already mapped) and macrophages (already mapped) modulates calcium balance; calcitonin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "endometrial-cancer substance-p: substance-P from endometrial cells (already mapped) and macrophages (already mapped) modulates uterine pain tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "endometrial-cancer insulin-receptor: insulin receptor on endometrial cells (already mapped) and macrophages (already mapped) drives tone; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "EMC aldosterone: aldosterone from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "EMC androgen-receptor: androgen receptor on endometrial cells (already mapped) and macrophages (already mapped) modulates EMC androgen tone; androgen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "EMC norepinephrine: norepinephrine from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "EMC adrenomedullin: adrenomedullin from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "EMC bdnf: BDNF from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC neurotrophin axis; BDNF excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "EMC osteopontin: osteopontin from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC matrix tone; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC."
---

# Endometrial Cancer

## Overview

**Endometrial cancer** is the most common gynecologic malignancy in the United States, with ~67,000 new cases and ~13,000 deaths per year. It arises from the endometrial lining of the uterus and is diagnosed in two broad histological categories: **Type I (endometrioid, estrogen-driven, ~80%)** and **Type II (serous, clear cell, carcinosarcoma, ~20%)** — a distinction reflected in their divergent molecular landscapes, treatment responses, and prognoses. The TCGA molecular classification (2013) — now integrated into WHO 2020 — stratified endometrial cancer into four prognostic groups: **POLE-ultramutated** (best prognosis), **MSI-H/dMMR** (good prognosis; responds to pembrolizumab), **copy-number low** (intermediate), and **copy-number high/TP53-mutant** (worst prognosis). This classification guides modern adjuvant and systemic therapy decisions [^eskander-2023-ruby].

**Epidemiology:**
- ~67,000 cases/year in the US; worldwide ~400,000/year; incidence rising (obesity epidemic)
- Median age at diagnosis: ~60 years; ~75% diagnosed at stage I (favorable prognosis)
- 5-year survival: ~83% overall; ~95% for stage I; ~17% for stage IV
- Risk factors: Obesity (estrogen excess from adipose conversion of androgens), unopposed estrogen exposure (anovulation, hormone replacement without progestin, tamoxifen), nulliparity, diabetes, PCOS, Lynch syndrome
- Protective: Oral contraceptives (>50% risk reduction), multiparity, physical activity, smoking (weakly protective via anti-estrogen effect)

**Lynch syndrome and endometrial cancer:**
- Lynch syndrome (germline MLH1, MSH2, MSH6, PMS2 mutation) → endometrial cancer is the sentinel cancer in ~50% of female Lynch carriers (diagnosed before CRC)
- Lifetime endometrial cancer risk: ~40-60% for MLH1/MSH2 carriers; ~15-26% for MSH6 carriers; ~15% for PMS2 carriers
- Lynch-associated endometrial cancer: Often diagnosed at younger age (<50), MSI-H, favorable prognosis with surgery, excellent ICI response

## Structure

### Histological subtypes and molecular features

**Endometrioid adenocarcinoma (Type I):**
- Well-differentiated (Grade 1-2): PTEN loss, PIK3CA mutation (~40%), KRAS mutation (~30%), microsatellite instability (~25-30%)
- Grade 3 endometrioid: More aggressive; overlaps with serous carcinoma molecularly
- POLE-ultramutated: ~5-10% of endometrioid; POLE proofreading domain mutations → ultrahigh TMB (>100 mut/Mb) → exceptional ICI response; excellent prognosis

**Uterine serous carcinoma (Type II, ~10%):**
- Near-universal TP53 mutation (~90%); ERBB2 amplification (~30%); CCNE1 amplification (~20%); HR deficient in ~25%
- Behaves like HGSOC (often presents at advanced stage, highly aggressive, platinum-sensitive)
- Intraepithelial serous carcinoma (SEIC) = precursor lesion in polyps/surface epithelium

**Clear cell carcinoma (Type II, ~5%):**
- ARID1A mutations (~30%); TP53 mutations; POLE mutations in subset; MSI-H in ~10%
- Platinum-partially sensitive; SMAD2/3 mutations in some

**Carcinosarcoma (malignant mixed Müllerian tumor, ~5%):**
- Most aggressive; metastatic disease in >50% at presentation; HER2 amplification ~30%
- Carboplatin + paclitaxel ± trastuzumab (if HER2+); carboplatin + ifosfamide is historical alternative

**TCGA/WHO 2020 molecular classification:**

| Subtype | Frequency | Key alterations | Prognosis |
|---------|-----------|-----------------|-----------|
| POLE-ultramutated | ~5-10% | POLE exonuclease domain mutations | Excellent |
| MSI-H/dMMR | ~25-30% | MLH1/MSH2/MSH6/PMS2 loss | Favorable |
| Copy-number low (NSMP) | ~40% | PTEN/KRAS/PIK3CA; low genomic instability | Intermediate |
| Copy-number high/p53abn | ~20% | TP53 mutation; ERBB2 amp; CCNE1 amp | Poor |

### Molecular landscape

**PTEN (50-80% of endometrioid):**
- PTEN loss → PI3K-AKT activation → mTORC1 → proliferation; cooperates with PIK3CA mutation
- PTEN is also lost in endometrial intraepithelial neoplasia (EIN = precancer), establishing it as an early driver

**KRAS/NRAS/BRAF mutations (~30% of endometrioid):**
- KRAS mutations (mainly G12D/G12V): activate MAPK and PI3K; co-occur with PTEN loss

**CTNNB1 (β-catenin, ~40% of endometrioid Grade 1-2):**
- Exon 3 mutations stabilize β-catenin → nuclear Wnt signaling → cyclin D1, MYC
- Associated with squamoid morule differentiation; better prognosis subgroup within copy-number low

**ARID1A (~30% of endometrioid and CCC):**
- SWI/SNF chromatin remodeling subunit; tumor suppressor; loss promotes DNA damage tolerance and EZH2 synthetic lethality

## Function

### Normal endometrial biology

**Hormonal cycling:**
- Estrogen (follicular phase) → endometrial proliferation via ERα → PTEN/PIK3CA mutation-harboring clones expand
- Progesterone (luteal phase) → secretory differentiation → antiproliferative; also suppresses endometrial proliferation
- Anovulatory cycles (PCOS, obesity, perimenopause) → prolonged unopposed estrogen → endometrial hyperplasia → EIN → endometrioid cancer

**Estrogen receptor (ERα) signaling:**
- ERα → cyclin D1 upregulation → CDK4/6 activation → RB phosphorylation → S-phase entry
- Aromatase in adipose tissue converts androgens to estrogens → central mechanism for obesity-associated endometrial cancer; BMI >30 → 3× higher risk; BMI >40 → 6× higher risk

## Pathology

### Staging and diagnosis

**FIGO 2023 staging (revised):**
- Stage I: Confined to uterus
  - IA: Limited to endometrium or <50% myometrial invasion (low-risk histology)
  - IB: ≥50% myometrial invasion; or low-grade endometrioid with LVSI
  - IC: p53-abnormal (serous/CCNE1-high) stage I tumors
- Stage II: Cervical stromal invasion
- Stage III: Pelvic/para-aortic lymph node or adnexal/vaginal extension
- Stage IV: Bladder/bowel invasion (IVA) or distant metastasis (IVB)

**Diagnosis:**
- Postmenopausal uterine bleeding: diagnostic in 90% → evaluate with transvaginal ultrasound (endometrial thickness ≥4 mm → biopsy)
- Endometrial biopsy (Pipelle): Office procedure; sensitivity ~90% for Type II histologies; hysteroscopy + D&C if initial biopsy non-diagnostic
- MRI: Best for myometrial invasion depth; CT for staging/lymph node assessment

**Surgical staging:**
- Total hysterectomy + bilateral salpingo-oophorectomy (TH-BSO) is curative for early-stage disease; sentinel lymph node (SLN) mapping has replaced full pelvic lymphadenectomy in most centers
- Molecular testing at surgery: POLE, MMR/MSI, TP53 IHC guides adjuvant therapy decisions

### Treatment

**Stage I-II low-risk (Grade 1-2 endometrioid, <50% MI, no LVSI):**
- Surgery alone (TH-BSO ± SLN); no adjuvant therapy; recurrence rate <5%
- Vaginal brachytherapy (VBT) for Grade 3 or with LVSI → reduces vaginal recurrence

**Stage I-II high-risk / Stage III:**
- Carboplatin (AUC5) + paclitaxel (175 mg/m²) × 6 cycles ± pelvic radiation
- **Pembrolizumab + carboplatin/paclitaxel (KEYNOTE-868):** dMMR: PFS not reached vs. 13.1 months; pMMR: PFS 13.1 vs. 8.7 months; FDA approved 2023 for 1st-line advanced/recurrent endometrial cancer (all comers, based on both dMMR and pMMR benefit) [^eskander-2023-ruby]
- **Dostarlimab + carboplatin/paclitaxel (RUBY trial):** dMMR subset: OS not reached vs. 30.2 months; FDA approved 2023

**Recurrent/metastatic:**
- **dMMR/MSI-H:** Pembrolizumab (ORR 57%); dostarlimab (ORR 44%); nivolumab; durvalumab — exceptional responses possible
- **pMMR (mismatch repair proficient):** Lenvatinib (VEGFR TKI) + pembrolizumab (KEYNOTE-146): ORR 38%, median PFS 7.2 months vs. 3.8 months; FDA approved 2019 for pMMR advanced endometrial cancer
- **ER+/PR+ endometrioid recurrence:** Progestin (medroxyprogesterone acetate, megestrol); aromatase inhibitor (letrozole); fulvestrant; everolimus + letrozole (32% CBR)
- **HER2+ serous:** Trastuzumab + carboplatin/paclitaxel (phase II benefit; ongoing phase III)
- **POLE-ultramutated:** Excellent ICI response even in advanced disease; single-agent pembrolizumab ORR ~75%

**Lynch syndrome-associated endometrial cancer:**
- Standard hysterectomy + BSO; Lynch patients benefit from prophylactic BSO at time of surgery (eliminates ovarian cancer risk)
- MSI-H → immunotherapy-responsive; adjuvant pembrolizumab under study in stage III-IV dMMR

## Connections

- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss-of-function mutations in ~50-80% of low-grade endometrioid endometrial cancer; earliest molecular event in endometrial carcinogenesis; PTEN loss → PI3K-AKT-mTOR activation → cell proliferation; mTOR inhibitors (everolimus + letrozole) active in ER+ endometrial cancer; germline PTEN mutations cause Cowden syndrome.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — dMMR/MSI-H endometrial cancer (~25-30%) responds to pembrolizumab; KEYNOTE-158 ORR 57% in dMMR endometrial; dostarlimab FDA approved 2021 for dMMR recurrent endometrial; RUBY trial (dostarlimab+carboplatin/paclitaxel) improved OS in dMMR subset; PD-1 blockade is standard for dMMR recurrent disease.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — ERBB2 (HER2) amplification in ~30% of uterine serous carcinoma (USC) and carcinosarcoma; trastuzumab + carboplatin/paclitaxel improved PFS vs. chemo alone (phase II, Fader 2018); HER2-positive USC is an actionable subset; T-DXd studied in HER2-low endometrial cancer; HER2 testing recommended for serous histology.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K/AKT/mTOR pathway activated in ~70% of endometrioid endometrial cancer via PTEN loss, PIK3CA mutation (~40%), or AKT1 E17K (~5%); everolimus + letrozole showed 32% clinical benefit rate in ER+ endometrial cancer; lenvatinib + pembrolizumab (KEYNOTE-146) active in non-MSI-H recurrent endometrial cancer.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Unopposed estrogen drives endometrial hyperplasia → EIN → type 1 endometrioid cancer; obesity → adipose aromatase → androgen-to-estrogen conversion → ~3× EC risk at BMI >30; aromatase inhibitors active in ER+ endometrial cancer; combined HRT (with progestogen) prevents EC risk.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Progesterone drives endometrial secretory transformation opposing estrogen proliferation; mifepristone (PR/GR antagonist) blocks P4 receptor → decidual breakdown → pregnancy termination; progesterone supplementation treats luteal phase deficiency and recurrent miscarriage.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Endometrial cancer is the sentinel cancer of Lynch syndrome: about half of female carriers present with it before any colorectal cancer, so a young or dMMR endometrial tumour should prompt germline testing — and these MSI-H cancers respond well to PD-1 immunotherapy.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is the dominant modifiable driver of endometrial cancer: adipose aromatase converts androgens to estrogen, and this unopposed estrogen pushes endometrium through hyperplasia to type-1 endometrioid cancer — roughly tripling risk at BMI >30 and fueling rising incidence.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation defines the most aggressive endometrial cancers: near-universal (~90%) in uterine serous carcinoma, it marks the copy-number-high TCGA group with the worst prognosis, unlike the estrogen-driven endometrioid tumours — a split that now guides adjuvant therapy.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Endometrial and breast cancers are linked estrogen-driven cancers: unopposed estrogen and obesity raise risk of both, and tamoxifen used for breast cancer acts as a uterine estrogen agonist that increases endometrial cancer risk—so bleeding on tamoxifen warrants evaluation.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Endometrial and ovarian cancers frequently co-occur: ~10% of endometrioid endometrial cancers have a synchronous endometrioid ovarian primary, and both are core Lynch-syndrome tumors from mismatch-repair deficiency—so MMR/MSI testing and gynecologic surveillance span the two.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Endometrial and colorectal cancer are the defining Lynch-syndrome malignancies: germline mismatch-repair mutations (MLH1, MSH2/6, PMS2) drive microsatellite instability in both, endometrial cancer is often the sentinel cancer in women, and MSI-high tumors take immunotherapy.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Cowden syndrome is a hereditary cause of endometrial cancer: germline PTEN loss unleashes PI3K/mTOR signaling in the endometrium—the pathway mutated in most sporadic endometrioid tumors—so PTEN carriers face raised endometrial, breast, and thyroid cancer risk.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes and endometrial cancer are tied via obesity and hyperinsulinemia: excess insulin and adipose estrogen stimulate endometrial proliferation, so diabetic, obese women face much higher endometrial cancer risk—metformin is studied as prevention.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Mismatch-repair-deficient (MSI-high) endometrial cancer is highly immunotherapy-responsive: defective DNA repair generates abundant neoantigens that draw cytotoxic CD8+ T cells, so anti-PD-1 (dostarlimab, pembrolizumab) has transformed treatment of dMMR endometrial tumors.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is a key adjuvant in endometrial cancer: after hysterectomy, vaginal brachytherapy or pelvic external-beam photon radiation lowers local recurrence, and radiation can treat inoperable patients—complementing surgery in the commonest gynecologic cancer.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Endometrial cancer is the commonest gynecologic-tract cancer of the reproductive system: arising from the estrogen-responsive uterine lining, it is driven by unopposed estrogen, so the reproductive system's own hormonal milieu fuels the tumor.
- `connects-to` → **[HLRCC](../hlrcc/README.md)** — Endometrial and uterine tumors link endometrial cancer to HLRCC: fumarate-hydratase loss causes the uterine leiomyomas that name HLRCC and FH-deficient uterine cancers—so uterine smooth-muscle or endometrial tumors with a family history may flag the HLRCC mutation.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutation is among the commonest drivers of endometrial cancer: it activates the PI3K/AKT/mTOR growth pathway (often alongside PTEN loss), so this axis is a leading target for the mTOR and PI3K inhibitors being developed for the disease.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Endometrial cancer is tightly linked to insulin and metabolic excess: obesity and type 2 diabetes raise insulin and IGF-1, which—with the estrogen made by fat tissue—stimulate endometrial proliferation, explaining why metabolic disease so strongly raises risk.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Endometrial cancer is the prototypical hormone-dependent tumor of the endocrine system: unopposed estrogen without progesterone drives endometrial overgrowth, so conditions and drugs that disturb the estrogen-progesterone balance change the risk markedly.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Endometrial cancer is staged through the lymphatic system: spread to pelvic and para-aortic nodes drives staging and prognosis, so sentinel-lymph-node mapping now guides how aggressively surgery and adjuvant therapy are pursued.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — CTNNB1 mutations define a deceptive endometrial subgroup: activating this Wnt/beta-catenin gene marks low-grade endometrioid tumors that look indolent but carry a surprisingly high recurrence risk—part of the molecular classification reshaping endometrial cancer care.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Endometrial cancer can spread to the lung: high-grade and serous subtypes disseminate hematogenously, making the lung a common distant metastatic site, so chest imaging is part of staging advanced or recurrent disease.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — Endometrial cancer's molecular classes hinge on MMR genes like MLH1: silencing of MLH1 by promoter methylation creates the common microsatellite-instability subtype, which is hypermutated and responds well to checkpoint immunotherapy—so MMR testing guides treatment.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Depth of myometrial invasion stages endometrial cancer, and fibroblasts pave the way: cancer-associated fibroblasts remodel the stroma to let tumor burrow into the muscle wall, and how deep it goes is a key prognostic factor guiding surgery.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Advanced endometrial cancer is treated by hitting VEGF: lenvatinib (a VEGFR inhibitor) plus pembrolizumab became a standard for recurrent disease, choking the tumor's blood supply while unleashing the immune system.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Body fat is the engine of endometrial cancer: adipocytes make aromatase that turns androgens into estrogen, so obesity floods the uterine lining with unopposed estrogen, making it the malignancy most strongly tied to excess weight.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver tunes endometrial-cancer risk through SHBG: it makes sex-hormone-binding globulin that mops up estrogen, and obesity and insulin resistance lower SHBG, raising the free estrogen that drives this hormone-sensitive tumor.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages connect obesity to endometrial cancer: inflamed fat draws macrophages that pour out cytokines, and tumor-associated macrophages in the uterine tumor promote its growth and blood supply, a cellular bridge from adiposity to malignancy.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Endometrial cancer announces itself by spending iron: abnormal uterine bleeding—especially after menopause—is the cardinal warning sign, and the chronic blood loss drains the body's iron into a deficiency anemia that often prompts the diagnosis.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells matter most in mismatch-repair-deficient endometrial cancer: these immunogenic tumors draw NK and T-cell attack, part of why such cancers respond well to immunotherapy that unleashes the immune assault.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Advanced endometrial cancer can threaten the kidneys: a bulky uterine tumor or its pelvic spread compresses the ureters, backing urine up into the kidneys (hydronephrosis) and causing post-renal kidney injury.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Endometrial cancer and its treatment leave fibrosis: a reactive desmoplastic stroma surrounds the tumor, and pelvic radiation scars nearby tissues, a late cause of bowel and bladder problems in survivors.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endometrial cancer drives angiogenesis: VEGF recruits endothelial cells to vascularize the tumor, and the fragile new vessels contribute to the abnormal bleeding that usually reveals it early.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Endometrial cancer can invade the bowel: locally advanced disease spreads to the rectum and sigmoid colon and seeds the peritoneum, complicating surgery and signaling advanced spread.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy separates endometrial cancer's two faces: the common endometrioid type keeps orderly glandular cells with microvilli, while the aggressive serous type shows papillary tufts and chaotic nuclei, an ultrastructural divide that tracks prognosis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Serous endometrial cancer leaves calcium fingerprints: like its ovarian counterpart it forms psammoma bodies, concentric calcium deposits whose presence on histology flags the high-grade serous subtype.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D ties into endometrial cancer through fat: deficiency travels with the obesity that is its biggest risk factor, and the vitamin's influence on cell growth and estrogen metabolism has made it a focus of prevention research.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The cancer announces itself in blood: postmenopausal bleeding is the cardinal early sign, and chronic abnormal uterine bleeding can drain enough red cells and iron to leave a woman anemic before the diagnosis is made.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Advanced disease draws on nerve-toxic chemotherapy: the carboplatin-paclitaxel regimen used for high-risk endometrial cancer injures peripheral sensory neurons, leaving the numbness and tingling of a taxane neuropathy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Platinum chemotherapy wastes magnesium: the carboplatin paired with paclitaxel injures the kidney's tubular handling of the mineral, so magnesium is checked and replaced through endometrial cancer treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies now classify and treat it: mismatch-repair and p53 immunostains sort endometrial cancers into molecular groups, and the MMR-deficient tumors respond to checkpoint antibodies like dostarlimab and pembrolizumab.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The carboplatin-paclitaxel backbone empties the marrow: both drugs are myelosuppressive, dropping neutrophil counts between cycles so that growth-factor support and febrile-neutropenia watch run through advanced-disease treatment.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet and weight are the dominant levers: obesity-driven excess estrogen is the leading modifiable cause, so weight loss and a high-fiber, plant-rich diet that lowers circulating estrogen reduce endometrial cancer risk.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The obesity-diabetes link runs through IGF-1: hyperinsulinemia raises bioactive IGF-1, a potent mitogen that, with excess estrogen, fuels endometrial proliferation — a molecular reason metabolic disease drives this cancer.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells help the tumor hide: they accumulate in the endometrial tumor microenvironment and damp the antitumor response, a dynamic that matters most in the mismatch-repair-deficient tumors targeted by immunotherapy.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — An STK11 syndrome raises the risk: Peutz-Jeghers syndrome predisposes to endometrial cancer and the rare cervical adenoma malignum, one of the inherited routes to gynecologic cancer beyond Lynch and Cowden.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — A chromatin gene falters early: ARID1A, part of the SWI/SNF remodeling complex, is frequently mutated in endometrioid endometrial cancer, loosening gene regulation as one of the disease's commonest driver events.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS pushes the endometrioid type: activating KRAS mutations fire the MAPK growth pathway in the estrogen-driven endometrioid subtype, often alongside PTEN and PIK3CA loss in the same tumor.
- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — Lynch lands hardest on the womb: germline mismatch-repair defects in genes like MSH2 make endometrial cancer the sentinel cancer of Lynch syndrome in women, and the resulting MSI makes these tumors immunotherapy-responsive.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Obesity-driven inflammation feeds the tumor through NF-κB: the chronic inflammation of excess fat activates NF-κB in the endometrium, adding a pro-survival, pro-proliferative push to the estrogen excess that drives type I endometrial cancer.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — An obese cancer prone to clots: endometrial cancer, usually arising in obese patients, carries a high venous thromboembolism risk that pelvic surgery and the tumor's own procoagulant state compound.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Surgery and chemo open the door to infection: hysterectomy, the mainstay treatment, and the neutropenia of chemotherapy for advanced disease make postoperative infection and sepsis recognized hazards.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Bleeding and inflammation both lower the count: alongside the iron-deficiency anemia from abnormal uterine bleeding, the tumor's inflammatory burden raises hepcidin and suppresses erythropoiesis into an anemia of chronic disease.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Advanced pelvic disease can obstruct the kidneys: locally invasive or recurrent endometrial cancer can compress the ureters, and platinum chemotherapy adds nephrotoxicity, together threatening chronic kidney disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Diagnosis and treatment weigh on mood: the cancer diagnosis, surgical menopause from hysterectomy-oophorectomy and the demands of treatment contribute to a substantial burden of depression.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Removing the ovaries withdraws bone-protective estrogen: the hysterectomy with oophorectomy that treats endometrial cancer throws younger patients into surgical menopause, accelerating bone loss toward osteoporosis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — It rides on a cardiometabolic profile: endometrial cancer's strong association with obesity, diabetes and hypertension means these patients carry a heavy cardiovascular burden that predisposes to heart failure.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemotherapy for advanced disease opens the lung to mold: the neutropenia from carboplatin-paclitaxel treatment of high-risk or recurrent endometrial cancer can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Hysterectomy is its central surgery: total hysterectomy with lymph-node dissection treats endometrial cancer, and obesity and diabetes — its main risk factors — leave these abdominal wounds slow and infection-prone.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its taxane chemo numbs the nerves: the carboplatin-paclitaxel regimen for advanced or high-risk endometrial cancer causes a dose-dependent, often lasting peripheral neuropathy.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Recurrence surveillance breeds worry: the monitoring for relapse and the body-image and fertility-loss impact of hysterectomy in endometrial cancer foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to the lungs: the lungs are a common site of distant metastasis in endometrial cancer, found on staging imaging and at recurrence as pulmonary nodules.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Mismatch-repair failure makes it treatable by immunotherapy: dMMR/MSI-high endometrial tumours — common and often linked to Lynch syndrome — respond to checkpoint-inhibitor therapy.
- `connects-to` → **[Renal System](../renal-system/README.md)** — A bulky pelvic tumour can block the ureters: locally advanced endometrial cancer can obstruct the ureters, causing hydronephrosis and post-renal acute kidney injury.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Shared metabolic roots: the obesity, insulin resistance and unopposed oestrogen that drive type-I endometrial cancer are the same risk cluster behind cardiovascular disease, a leading cause of death in survivors.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Advanced disease spreads within the abdomen: endometrial cancer seeds the omentum and bowel surfaces, and platinum-taxane chemotherapy brings nausea and mucositis.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It can surface at the navel: like other intra-abdominal cancers it occasionally seeds a Sister Mary Joseph nodule at the umbilicus, a visible sign of peritoneal spread.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Mismatch-repair loss makes it immunogenic: about a quarter of endometrial cancers are dMMR/MSI-high and respond strongly to PD-1 inhibitors like pembrolizumab, now central to advanced and Lynch-associated disease.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Molecular drivers guide newer drugs: lenvatinib (anti-VEGFR) with pembrolizumab, mTOR inhibitors for PTEN-altered tumours and anti-HER2 antibody-drug conjugates for HER2-positive serous cancer extend treatment options.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — A diabetes drug studied against it: metformin lowers the insulin and IGF-1 signalling that fuels endometrial cancer, and is investigated as adjunct and chemoprevention in the obese, insulin-resistant women most at risk.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Carboplatin-paclitaxel for advanced disease: while early endometrial cancer is cured by surgery, advanced and high-grade (serous, carcinosarcoma) disease relies on platinum-taxane chemotherapy, now often combined with immunotherapy.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — The two uterine cancers contrasted: endometrial cancer arises from the hormone-responsive uterine lining driven by unopposed oestrogen and obesity, whereas cervical cancer arises from HPV infection of the cervix — different organs, causes and prevention.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — A shared ARID1A/endometriosis pathway: endometrioid and clear-cell cancers of both the uterus and ovary arise from endometriosis-like glands with ARID1A and PIK3CA mutations, linking these gynaecological malignancies mechanistically.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Why it responds to immunotherapy: mismatch-repair-deficient (MSI-high) endometrial cancers—Lynch and sporadic—accumulate neoantigens and tertiary lymphoid structures with germinal-centre B cells, the immune richness behind checkpoint-inhibitor response.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Two cancers of the Lynch spectrum: endometrial cancer is the sentinel Lynch-syndrome cancer in women and gastric cancer is another mismatch-repair-deficient Lynch tumour—shared MMR loss across the uterus and stomach.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Shared metabolic roots with heart disease: the obesity, insulin resistance and unopposed oestrogen that drive endometrial cancer also accelerate arterial-wall atherosclerosis, so cardiovascular disease is a leading cause of death in survivors.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Lung as a metastatic site: endometrial cancer, especially serous and high-grade subtypes, spreads haematogenously to the lungs, seeding nodules in the alveolar parenchyma in advanced disease.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver metastasis: advanced endometrial cancer can spread to the liver, seeding the hepatic lobules, a marker of disseminated disease beyond its usual pelvic and nodal spread.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Lynch beyond gut and uterus: the mismatch-repair deficiency behind hereditary endometrial cancer also raises urothelial (bladder and ureter) cancer risk, part of the broad Lynch tumour spectrum.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The Lynch sentinel: in women with Lynch syndrome, endometrial cancer often appears before colorectal cancer, the same mismatch-repair loss driving tumours in the uterine and intestinal epithelium.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Serous, p53-driven disease: the aggressive serous subtype of endometrial cancer is TP53-mutated, and germline TP53 (Li-Fraumeni) adds it to that syndrome's broad cancer spectrum.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Obesity and disrupted care: the obesity that drives endometrial cancer also worsens COVID-19, and the pandemic delayed diagnosis of postmenopausal bleeding and gynaecological-cancer surgery.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT engine: with PTEN loss and PIK3CA mutation near-universal in endometrioid tumours, AKT is constitutively active to drive growth and survival, making the PI3K/AKT/mTOR axis a key target.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: oestrogen-driven endometrial cancer relies on cyclin D-CDK4/6 to pass the G1 checkpoint, and CDK4/6 inhibition with endocrine therapy is under active investigation.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in hypoxic endometrial tumours promotes the VEGF angiogenesis, glycolysis and invasion that mark the more aggressive, higher-grade disease.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Serous-subtype oncogene: MYC amplification helps drive the copy-number-high, p53-mutant serous endometrial cancers, the most aggressive molecular subtype with the poorest prognosis.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase reactivation: TERT activation immortalises endometrial cancer cells, sustaining the unlimited proliferation that complements the PI3K and mismatch-repair lesions of the disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Tumour microenvironment: CCL2 secreted by endometrial tumours recruits tumour-associated macrophages that promote angiogenesis and immune evasion, linked to obesity-driven inflammation in the disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The mismatch-repair-deficient and POLE-ultramutated endometrial cancers accumulate cytosolic DNA that activates cGAS-STING, the innate-immune basis for the strong response of these subtypes to checkpoint inhibitors like dostarlimab.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Leptin from excess adipose tissue stimulates endometrial epithelial proliferation through JAK-STAT and PI3K signaling, a key mechanism connecting obesity—the dominant modifiable risk factor—to endometrial carcinogenesis.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the epithelial-mesenchymal transition and stromal remodeling that enable myometrial invasion, the depth of which is the key determinant of stage and prognosis in endometrial cancer.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Activating FGFR2 mutations occur in a substantial fraction of endometrioid endometrial cancers and are associated with worse outcome, a targetable oncogenic driver distinct from the dominant PTEN/PI3K and mismatch-repair lesions.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Carboplatin-paclitaxel, the backbone of advanced endometrial-cancer treatment, kills tumor cells through caspase-3-mediated apoptosis, the death pathway whose evasion underlies chemoresistance in serous and high-grade disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4-CXCL12 signaling directs endometrial-cancer cells toward the pelvic lymph nodes and peritoneum, the lymphatic and transcoelomic routes of spread that define advanced-stage disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KRAS and FGFR2 mutations (already mapped) in endometrioid endometrial cancer activate the MAPK-ERK pathway, a proliferative driver complementing the dominant PI3K-AKT axis.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The CDK4/6-RB-E2F axis (CDK4/6 already mapped) powers the cell-cycle progression of endometrial cancer, particularly the estrogen-stimulated proliferation of endometrioid tumors.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Estrogen induces anti-apoptotic BCL-2 in the endometrium, and its overexpression supports the survival of endometrioid endometrial-cancer cells in this hormonally driven tumor.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Adipose-derived IL-6 fuels the chronic inflammatory and estrogenic milieu of obesity that is the dominant modifiable risk factor for endometrioid endometrial cancer, promoting tumor-cell proliferation and survival.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 amplification degrades p53, providing an alternative route to loss of p53 tumor-suppressor function in serous endometrial cancer beyond the TP53 mutations that define this aggressive subtype.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Constitutive Wnt/β-catenin signaling — through CTNNB1 exon-3 mutations — defines a molecular subgroup of endometrioid endometrial cancer associated with younger age and recurrence risk.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 mapped) links the obesity-associated inflammatory state to proliferation and immune evasion in endometrial cancer.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss releases CDK4/6-cyclin-D control (CDK4/6 mapped) of the cell cycle, a recurrent lesion contributing to endometrial carcinogenesis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Altered TGF-β-SMAD signaling (TGF-β mapped) contributes to invasion and epithelial-mesenchymal transition in aggressive endometrial cancer.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports immune evasion and the invasive progression of endometrial cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of endometrial cancer, particularly the immunotherapy-responsive mismatch-repair-deficient subtype.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression silences tumor-suppressor genes and contributes to the epigenetic dysregulation of endometrial cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PTEN-loss-driven PI3K-AKT signaling (PTEN, AKT, and PIK3CA already mapped) inactivates FOXO, removing a tumor-suppressive brake in endometrial cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunotherapy-responsive mismatch-repair-deficient endometrial cancer must evade.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from infiltrating myeloid cells promote the inflammatory, often obesity-linked, microenvironment of endometrial cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates β-catenin stability (CTNNB1/Wnt already mapped), a pathway aberrantly activated in the endometrioid subtype of endometrial cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of HER2 and growth-factor receptors contributes to the invasion of endometrial cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic silencing of MLH1 and other tumor-suppressor genes in endometrial cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of endometrial cancer cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling, coupled to the obesity and insulin-resistance risk (insulin already mapped), participates in endometrial cancer.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven macrophage recruitment shapes the inflammatory microenvironment of endometrial cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation, linked to the obesity-associated pathogenesis, participates in the tumor microenvironment of endometrial cancer.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the proliferation and differentiation programs dysregulated in endometrial cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of endometrial cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of endometrial cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of endometrial cancer.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the estrogen-linked proliferative and immune signaling of endometrial cancer.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy subtypes: the mismatch-repair-deficient (MSI, MLH1/MSH2 already mapped) and POLE-ultramutated endometrial cancers generate abundant neoantigens presented on MHC, making them the subtypes most responsive to checkpoint inhibitors.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Obesity risk: obesity is the leading modifiable risk factor for endometrial cancer, and low adiponectin alongside the leptin excess already mapped links adipose dysfunction and insulin resistance to endometrial carcinogenesis.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Treatment resistance: the AXL receptor tyrosine kinase promotes epithelial-mesenchymal transition and therapy resistance in endometrial cancer, a route of progression beyond the hormonal and PI3K-pathway drivers already mapped.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — MSI immunotherapy: the mismatch-repair-deficient endometrial cancers (MLH1/MSH2 already mapped) are neoantigen-rich and respond to checkpoint blockade (PD-1 already mapped), and IL-2-driven T-cell activity underlies this immune sensitivity.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Bleeding anaemia: abnormal uterine and postmenopausal bleeding is the cardinal presentation of endometrial cancer, and the chronic blood loss produces an iron-deficiency anaemia lowering haemoglobin that often prompts diagnosis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic dyslipidaemia: the obesity and insulin resistance (already mapped) that drive endometrial cancer come with atherogenic dyslipidaemia, and cholesterol metabolism intersects the estrogen and mTOR pathways fuelling the tumour.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammation-estrogen link: cyclooxygenase-2-derived prostaglandin E2 in the endometrial tumour and adipose stroma induces aromatase and local estrogen (already mapped) synthesis, linking the obesity-associated inflammation to the hormone drive of endometrial cancer.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 and CD8 already mapped), the immune evasion that is more readily overcome in the mismatch-repair-deficient (MLH1 already mapped) tumours.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and lysis stress: the chemotherapy of advanced endometrial cancer generates oxidative stress and cell lysis releasing purines that xanthine oxidase converts to uric acid, adding an oxidative and tumour-lysis burden to treatment.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the mismatch-repair-proficient endometrial cancers.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Bleeding and anaemia: the abnormal uterine bleeding that presents most endometrial cancer causes iron-deficiency anaemia (haemoglobin already mapped), and the chemotherapy of advanced disease adds a transfusional iron burden.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary metastases: the lungs are a common site of metastasis of advanced and serous (p53 already mapped) endometrial cancer, the haematogenous spread driving the prognosis of high-risk disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of endometrial cancer.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages (CCL2 already mapped) of the endometrial-cancer stroma, in their M2 (IL-4 already mapped) phenotype, drive the immunosuppression and angiogenesis (VEGF already mapped) of the tumour.
- `connects-to` → **[Cowden syndrome](../cowden-syndrome/README.md)** — PTEN hamartoma syndrome: Cowden syndrome (germline PTEN already mapped) markedly raises the risk of endometrial cancer, part of the hereditary predisposition alongside Lynch syndrome (already mapped).
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the obesity (already mapped) risk of the type-1 endometrial cancer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — MSI immunogenicity: the cGAS-STING (already mapped) sensing of the genomic instability of the MMR-deficient/MSI (MLH1 and MSH2 already mapped) endometrial cancer drives the type-I interferon behind the checkpoint (PD-1 already mapped) response.
- `connects-to` → **[Hereditary breast-ovarian cancer](../hereditary-breast-ovarian-cancer/README.md)** — BRCA-associated risk: the hereditary breast-ovarian cancer syndrome (germline BRCA) carries an increased serous endometrial-cancer risk, part of the PARP-inhibitor rationale.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of the MSI-high endometrial cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the endometrial-cancer immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of endometrial cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of endometrial cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the endometrial-cancer microenvironment.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 TIL source: the CD4 T-helper cells of the tumour-infiltrating lymphocytes are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the MSI-high/POLE immune response of endometrial cancer.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of endometrial cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, marks the favourable immune response of the MSI-high/POLE endometrial cancer.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the tumour neoantigen to the T cells (already mapped), driving the checkpoint (PD-1 already mapped) response of the MSI-high endometrial cancer.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the inflammatory and immunosuppressive dimension of the endometrial-cancer microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the myeloid (macrophage already mapped) recruitment and immunosuppression of the endometrial-cancer microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the endometrial-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the microenvironment.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-tumour axis: TSLP, from cancer-associated fibroblasts (already mapped) and tumour stroma, primes dendritic cells (already mapped) and mast cells (already mapped) toward the Th2 immunosuppressive bias of the endometrial-cancer microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-tumour axis: bradykinin, via the kallikrein-kinin system in the tumour microenvironment, amplifies the vascular permeability and the pro-tumorigenic myeloid (macrophage already mapped) recruitment in endometrial cancer.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia of cancer: erythropoietin corrects the cancer-related and chemotherapy-induced anaemia of endometrial cancer; EpoR expression on tumour cells also modulates a potential direct proliferative signal.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell stroma: mast cells (already mapped) in the endometrial-cancer stroma release histamine that amplifies VEGF (already mapped)-driven angiogenesis and the type-2 microenvironment (IL-4, IL-13 already mapped) of the tumour.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Stromal matricellular: periostin, secreted by cancer-associated fibroblasts (already mapped) in the endometrial-cancer stroma, promotes invasive myometrial penetration and TGF-β (already mapped)-linked epithelial-mesenchymal transition.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor modulates the classical complement pathway (C3, C5 and C5aR1 already mapped) within the endometrial-cancer microenvironment, attenuating complement-driven myeloid recruitment.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — EC testosterone: testosterone, via androgen receptors on endometrial cells, modulates the estrogen (already mapped)-mTOR (already mapped) proliferative axis; low androgen-to-oestrogen ratios in obesity (already mapped) amplify Type I endometrial carcinogenesis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — EC serotonin: serotonin, via 5-HT receptors on endometrial cells and macrophages (already mapped), promotes VEGF (already mapped)-driven angiogenesis; serotonin excess amplifies the estrogen (already mapped) and mTOR (already mapped) proliferative milieu of endometrial cancer.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — EC prolactin: prolactin, via PRLR on endometrial cells and macrophages (already mapped), promotes mTOR (already mapped)-driven tumour proliferation; hyperprolactinaemia amplifies the estrogen (already mapped)-linked uterine proliferative axis of Type I endometrial cancer.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — EC oxytocin: oxytocin, via OXTR on endometrial-cancer cells, suppresses mTOR (already mapped) and NF-κB (already mapped) tumour-proliferative signalling; oxytocin attenuates estrogen (already mapped)-driven angiogenesis and the VEGF (already mapped) pro-tumourigenic milieu.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — EC vasopressin: vasopressin, via V1bR on endometrial cells, promotes CRH-cortisol (already mapped) immune suppression in the tumour microenvironment; vasopressin amplifies the mTOR (already mapped) and NF-κB (already mapped) pro-tumourigenic milieu of endometrial cancer.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — EC selenium: selenium, via GPx and selenoproteins, suppresses ROS-driven NF-κB (already mapped) and mTOR (already mapped) tumour-proliferative signalling; selenium induces apoptosis and attenuates estrogen (already mapped)-linked carcinogenesis in endometrial cancer.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — EC zinc: zinc cofactors estrogen receptor (already mapped) signalling and macrophage (already mapped) anti-tumour immunity; zinc deficiency amplifies NF-κB (already mapped) and mTOR (already mapped)-driven endometrial tumour proliferation and angiogenesis in endometrial cancer.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — EC iodine: thyroid hormones (iodine-dependent) modulate estrogen-receptor (already mapped) activity in endometrial cells; iodine deficiency amplifies NF-κB (already mapped) and mTOR (already mapped) proliferative signalling and IL-6 (already mapped) tumour inflammation.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — EC sodium: sodium-driven osmotic stress on endometrial cells amplifies NF-κB (already mapped) and mTOR (already mapped) tumour-proliferative signalling; sodium-stimulated IL-6 (already mapped) and VEGF (already mapped) promote the pro-tumourigenic milieu of endometrial cancer.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — EC copper: copper, via ceruloplasmin and SOD, in macrophages (already mapped) and fibroblasts (already mapped), scavenges ROS; copper excess amplifies NF-κB (already mapped) and mTOR (already mapped) endometrial tumour growth via VEGF (already mapped) angiogenesis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — EC potassium: potassium regulates macrophage (already mapped) and endometrial epithelial membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and mTOR (already mapped) and IL-6 (already mapped) tumour-proliferative signalling of endometrial cancer.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — EC phosphorus: phosphorus, as ATP in macrophages (already mapped) and fibroblasts (already mapped), fuels tumour-stromal crosstalk; phosphorus excess amplifies NF-κB (already mapped) and mTOR (already mapped) and VEGF (already mapped) endometrial cancer cascade.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — EC chloride: chloride channels on macrophages (already mapped) and endothelial cells (already mapped) regulate ionic homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) endometrial cancer cascade.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — EC carbon: carbon backbone of nucleotides in macrophages (already mapped) and endothelial cells (already mapped) fuels tumour growth; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) endometrial cancer cascade.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — EC hydrogen: hydrogen via ROS from macrophages (already mapped) and endothelial cells (already mapped) modulates tumour oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) endometrial cancer cascade.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — EC nitrogen: nitrogen in DNA bases of macrophages (already mapped) and endothelial cells (already mapped) sustains tumour growth; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) endometrial cancer cascade.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — endometrial-cancer glp-1: GLP-1 from macrophages (already mapped) and endometrial cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — endometrial-cancer angiotensin-ii: angiotensin II on endometrial cells (already mapped) and macrophages (already mapped) drives angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — endometrial-cancer rankl: RANKL from endometrial cells (already mapped) and macrophages (already mapped) modulates immune invasion; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — endometrial-cancer fibronectin: fibronectin in endometrial cells (already mapped) and macrophages (already mapped) promotes ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — endometrial-cancer activin-a: activin-A from endometrial cells (already mapped) and macrophages (already mapped) promotes tumour-stromal invasion; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — endometrial-cancer cgrp: CGRP from endometrial cells (already mapped) and macrophages (already mapped) modulates uterine nociception; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — endometrial-cancer calcitonin: calcitonin from endometrial cells (already mapped) and macrophages (already mapped) modulates calcium balance; calcitonin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — endometrial-cancer substance-p: substance-P from endometrial cells (already mapped) and macrophages (already mapped) modulates uterine pain tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — endometrial-cancer insulin-receptor: insulin receptor on endometrial cells (already mapped) and macrophages (already mapped) drives tone; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in endometrial cancer.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — EMC aldosterone: aldosterone from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC.
- `connects-to` → **[Androgen-Receptor](../../03-molecular/androgen-receptor/README.md)** — EMC androgen-receptor: androgen receptor on endometrial cells (already mapped) and macrophages (already mapped) modulates EMC androgen tone; androgen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — EMC norepinephrine: norepinephrine from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — EMC adrenomedullin: adrenomedullin from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — EMC bdnf: BDNF from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC neurotrophin axis; BDNF excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — EMC osteopontin: osteopontin from endometrial cells (already mapped) and macrophages (already mapped) modulates EMC matrix tone; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in EMC.

[^konstantinopoulos-2019-dostarlimab]: Konstantinopoulos PA, Lheureux S, Moore KN. PARP inhibitors for ovarian and endometrial cancers: state of the art and clinical perspectives. *J Clin Oncol.* 2020;38(25):2896-2909. [doi:10.1200/JCO.20.00571](https://doi.org/10.1200/JCO.20.00571) · [PubMed 32706635](https://pubmed.ncbi.nlm.nih.gov/32706635/)
[^eskander-2023-ruby]: Eskander RN, Sill MW, Beffa L, et al. Pembrolizumab plus chemotherapy in advanced endometrial cancer. *N Engl J Med.* 2023;388(23):2159-2170. [doi:10.1056/NEJMoa2302312](https://doi.org/10.1056/NEJMoa2302312) · [PubMed 37166384](https://pubmed.ncbi.nlm.nih.gov/37166384/)
