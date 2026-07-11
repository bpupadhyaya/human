---
schema: human-scale-entry/v1
id: peutz-jeghers-syndrome
name: Peutz-Jeghers Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Peutz-Jeghers syndrome (PJS) is caused by germline STK11/LKB1 mutations; hamartomatous GI polyps + mucocutaneous melanotic spots; cumulative cancer risk by age 70: breast 45%, CRC 39%, pancreatic 36%; intussusception risk; surveillance from age 8."
aliases: ["Peutz-Jeghers syndrome", "PJS", "STK11 hamartoma", "LKB1 polyp syndrome", "Peutz-Jeghers", "hereditary hamartomatous polyposis", "PJ polyp", "STK11 cancer syndrome", "hamartomatous polyposis", "Peutz-Jeghers cancer risk"]
sources:
  - id: hearle-2006-pjs-cancer
    type: peer-reviewed
    cite: "Hearle N, Schumacher V, Menko FH, et al. Frequency and spectrum of cancers in the Peutz-Jeghers syndrome. Clin Cancer Res. 2006;12(10):3209-3215."
    doi: "10.1158/1078-0432.CCR-06-0083"
    pmid: "16707622"
    url: "https://doi.org/10.1158/1078-0432.CCR-06-0083"
  - id: skoulidis-2018-stk11-nsclc
    type: peer-reviewed
    cite: "Skoulidis F, Goldberg ME, Greenawalt DM, et al. STK11/LKB1 mutations and PD-1 inhibitor resistance in KRAS-mutant lung adenocarcinoma. Cancer Cell. 2018;34(3):412-424."
    doi: "10.1016/j.ccell.2018.08.013"
    pmid: "30174241"
    url: "https://doi.org/10.1016/j.ccell.2018.08.013"
cross_links:
  - target: 01-human/03-molecular/stk11
    relation: connects-to
    note: "Germline STK11 mutations cause ~94% of PJS; STK11 encodes LKB1 (AMPK activator); haploinsufficiency → polyp formation (second hit in polyp epithelium); truncating STK11 mutations associate with higher cancer risk than missense; STK11 germline panel + deletion analysis required"
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "STK11 LOF → AMPK inactivation → mTOR unrestrained → hamartoma growth in PJS; rapamycin reduces polyp burden in STK11+/− mouse models; mTORC1 is the primary growth driver in PJS hamartomas; AMPK activators (metformin) explored as chemoprevention in PJS pilot studies"
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "PJS lifetime CRC risk ~39% by age 70 (Hearle 2006); PJS CRC arises through hamartoma-adenoma-carcinoma sequence; proximal colon predominance; colonoscopy with polypectomy every 1-3 years from age 15-20; CRC is the third most common PJS cancer after breast and pancreatic"
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "PJS lifetime pancreatic cancer risk ~36% by age 70; EUS + MRI surveillance from age 30-35; STK11 LOF co-mutation with KRAS in pancreatic cancer → mTOR + MAPK dual activation; PJS pancreatic cancer prognosis poor; resectability rate ~40% at detection"
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "STK11 LOF → AMPK loss → mTORC1 unrestrained → S6K1/4EBP1 → epithelial and smooth muscle proliferation → PJ hamartoma formation; rapamycin reduces polyp burden ~50-80% in STK11+/− mice; sirolimus + metformin pilot trial ongoing in PJS patients (NCT03943992)."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "PJS breast cancer lifetime risk ~45-54% by age 70 (BRCA1/2-equivalent); breast MRI + mammogram from age 25; STK11 LOF → mTOR hyperactivation in breast epithelium; HR+ predominant; no PJS-specific breast cancer histology; risk-reducing bilateral mastectomy discussed."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "STK11/LKB1 somatic mutations in ~15-20% of KRAS-mutant lung adenocarcinoma; STK11 loss → PD-L1 downregulation + CXCL7 secretion → neutrophilic immunosuppressive TME → primary ICB resistance; STK11-mutant KRAS+ NSCLC is the poorest immunotherapy responder subgroup."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine is the danger zone of Peutz-Jeghers syndrome: large hamartomatous polyps in the jejunum and ileum become lead points for intussusception — the most common complication, often needing emergency surgery in childhood; surveillance and polypectomy prevent it."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The diagnostic clue to Peutz-Jeghers syndrome is on the skin and lips: mucocutaneous melanotic macules — dark freckle-like spots on the lips, buccal mucosa, and fingertips — appear in infancy and often fade with age, but with hamartomatous polyps they establish the diagnosis."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Peutz-Jeghers hamartomas have a unique histology: an arborizing (tree-like) core of bundled smooth muscle extending into the polyp, covered by normal epithelium — distinguishing them from the edematous juvenile polyps of JPS or the dysplastic adenomas of FAP."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Peutz-Jeghers and juvenile polyposis are the two main hamartomatous polyposis syndromes: PJS (STK11) produces arborizing smooth-muscle polyps and mucocutaneous pigmentation, while JPS (SMAD4/BMPR1A) produces juvenile polyps—both raise GI cancer risk."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Peutz-Jeghers syndrome predisposes to distinctive ovarian tumors: sex cord tumors with annular tubules (SCTAT) and mucinous tumors arise from STK11 loss, often causing precocious puberty or estrogen effects—part of the syndrome's broad, organ-spanning cancer risk."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Peutz-Jeghers syndrome carries a rare cervical cancer—adenoma malignum (minimal-deviation adenocarcinoma): this deceptively bland, HPV-independent tumor is strongly associated with STK11 loss, so PJS patients warrant gynecologic surveillance for it."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Peutz-Jeghers and Cowden are both hamartomatous polyposis syndromes with different genes: PJS from STK11 loss giving GI hamartomas and mucocutaneous pigmentation, Cowden from PTEN (PI3K-AKT) loss—both fill the gut with hamartomas and raise multi-organ cancer risk."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Peutz-Jeghers and FAP are inherited polyposis syndromes with opposite polyp types: PJS produces hamartomatous polyps from STK11 loss, while FAP produces hundreds of adenomatous polyps from APC loss with near-certain colorectal cancer—hamartoma versus adenoma."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Peutz-Jeghers raises gastric as well as colorectal cancer risk: STK11 loss seeds hamartomatous polyps throughout the stomach and small bowel that can bleed, obstruct or harbor dysplasia, so upper-GI surveillance accompanies colonoscopy in PJS patients from childhood."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Peutz-Jeghers polyps stud the large intestine and beyond: STK11 loss produces hamartomatous polyps throughout the GI tract—small bowel most, but also colon—that bleed, cause intussusception, and modestly raise colorectal cancer risk."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "PJS hamartomas arise in disordered intestinal epithelium: loss of the STK11/LKB1 kinase deranges epithelial polarity and growth, so the crypts overgrow into the branching, smooth-muscle-cored hamartomatous polyps that distinguish PJS from adenomatous polyposis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "PJS shows a non-Wnt route to GI tumors: unlike FAP's APC/Wnt adenomas, Peutz-Jeghers polyps arise from STK11/LKB1-AMPK-mTOR dysregulation, so its hamartomas form by a different pathway—though malignant transformation can still recruit Wnt-driven changes."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Peutz-Jeghers fills the digestive tract with hamartomatous polyps: STK11/LKB1 loss seeds large hamartomas, especially in the small bowel, that bleed and cause intussusception in childhood—so GI polyps and obstruction often bring the diagnosis."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Pigmented spots make Peutz-Jeghers visible on the skin: mucocutaneous melanin macules on the lips, mouth and fingers appear in childhood, so these freckle-like spots are often the first clue to this STK11 polyposis-and-cancer syndrome."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Peutz-Jeghers affects the reproductive system with distinctive tumors: women develop sex-cord tumors with annular tubules (SCTAT) and raised cervical/ovarian cancer risk, and men can get calcifying Sertoli cell testicular tumors—warranting gonadal surveillance."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Peutz-Jeghers hamartomas stud the whole gut, including the stomach: gastric polyps add to the small-bowel ones, contributing bleeding and a raised gastric-cancer risk, so upper endoscopy joins small-bowel surveillance in management."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Peutz-Jeghers often presents with iron-deficiency anemia: chronic slow bleeding from gastrointestinal hamartomas depletes iron, so unexplained anemia in a young patient with lip pigmentation can be the clue that prompts diagnosis."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Peutz-Jeghers and MUTYH-associated polyposis are distinct inherited polyposes: PJS makes STK11-driven hamartomas with smooth-muscle cores, while MAP makes adenomas from oxidative DNA-repair failure—so polyp histology and gene testing separate them."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Peutz-Jeghers grows hormone-secreting gonadal tumors: ovarian sex cord tumors (SCTAT) and testicular Sertoli cell tumors pour out estrogen, causing precocious puberty, gynecomastia, and irregular bleeding—distinctive endocrine clues to the syndrome."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Peutz-Jeghers unleashes AKT-mTOR growth: LKB1 loss disables the AMPK brake, so the AKT-mTOR pathway runs unchecked in the hamartomatous polyps—rationale for trialing mTOR inhibitors to slow polyp growth and cancer risk."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Peutz-Jeghers polyps grow large on a fibroblast-rich hamartomatous stroma: their bulky, arborizing structure can drag a loop of bowel into itself (intussusception), the acute complication that often brings these polyps to medical attention."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Peutz-Jeghers polyps bleed and drain iron: the large hamartomas erode and ooze blood into the gut, and with the obstruction they cause, chronic blood loss makes iron-deficiency anemia a frequent sign in these patients."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages help build the Peutz-Jeghers polyp: tumor-associated macrophages populate the fibroblast-rich hamartomatous stroma and secrete growth and angiogenic factors, supporting the bulky polyps that arise from LKB1 loss."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Peutz-Jeghers polyps recruit blood vessels via VEGF: LKB1/AMPK loss disinhibits mTOR, which drives VEGF and angiogenesis to feed the growing hamartomas, part of the rationale for mTOR-pathway drugs studied in the syndrome."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Peutz-Jeghers' freckles are made with copper: the dark spots on the lips and mouth are melanin, built by the copper-dependent enzyme tyrosinase, the mucocutaneous sign that flags the syndrome."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Peutz-Jeghers carries a steep pancreatic cancer risk: STK11 loss makes the pancreas one of the syndrome's most dangerous cancer sites, so it joins the gut and breast in lifelong surveillance."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Peutz-Jeghers polyps are fragile and vascular: their endothelial-lined vessels tear easily as the bulky polyps tumble and intussuscept, causing the recurrent bleeding that drains the body's iron."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons keep watch over the small bowel: video capsule endoscopy and MR enterography survey the long stretches of intestine that ordinary scopes miss, finding the hamartomatous polyps before they grow big enough to bleed or obstruct."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Losing STK11 raises the lung's cancer risk: Peutz-Jeghers carries one of the highest lifetime risks of lung cancer among inherited syndromes, so the same gene that studs the gut with polyps also primes the airway lining for malignancy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver becomes a target as Peutz-Jeghers cancers spread: the syndrome's many adenocarcinomas — pancreatic, gastrointestinal, breast — metastasize there, so liver imaging joins the broad cancer surveillance these patients need."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Peutz-Jeghers often shows up as anemia: the hamartomatous polyps bleed slowly into the gut, draining red cells and iron until a child turns up pale and microcytic — sometimes the first clue that leads to the diagnosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "The telltale freckling is melanin under the microscope: the dark macules on lips and buccal mucosa come from melanin packed into basal keratinocytes, pigment granules that electron microscopy resolves within the epidermis."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Peutz-Jeghers reaches into the gynecologic tract: beyond its signature cervical and ovarian sex-cord tumors, the syndrome raises the lifetime risk of endometrial cancer, adding the uterus to its wide field of cancer surveillance."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains confirm the hallmark polyp: desmin and smooth-muscle-actin staining reveal the arborizing tree of smooth muscle that defines a Peutz-Jeghers hamartoma, separating it from the adenomas of other polyposis syndromes."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid joins the long cancer list: differentiated (papillary) thyroid carcinoma appears within the Peutz-Jeghers tumor spectrum, one more organ folded into the lifelong, head-to-pelvis surveillance the syndrome demands."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Chronic ooze from the polyps shows in the blood: the slow intestinal bleeding that drains iron also drives a reactive thrombocytosis, the platelet count climbing as the marrow responds to ongoing loss."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "STK11 is the master switch above AMPK: losing it deranges the LKB1-AMPK energy sensor that ties metabolism to growth, which is why metformin — an AMPK activator that improves insulin signaling — is studied as chemoprevention in Peutz-Jeghers."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Losing LKB1 turns tumors cold: STK11/LKB1 loss reshapes the microenvironment to exclude and disarm cytotoxic T cells, a recognized driver of resistance to checkpoint immunotherapy in the lung and other cancers it predisposes to."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "The faulty gene sits at the body's energy controls: LKB1-AMPK signaling governs how adipocytes and other tissues sense and store energy, so the syndrome's defect reaches a metabolic network far beyond the gut polyps it is known for."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "The defective kinase reaches the master tumor suppressor: LKB1 normally helps activate p53-dependent apoptosis and growth arrest, so losing it weakens this checkpoint as well, compounding the cancer risk beyond the unleashed mTOR signaling."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "The lungs are on the long cancer list: Peutz-Jeghers raises the risk of lung cancer, including small cell carcinoma, one of the many epithelial tissues where LKB1 loss removes a brake — a reminder its danger reaches well beyond the gut."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "The biliary tree is not spared: the syndrome's broad cancer predisposition extends to the bile ducts, so cholangiocarcinoma joins the pancreatic and gastrointestinal tumors that make lifelong, multi-organ surveillance the core of PJS care."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "It headlines the hereditary GI-cancer differential: PJS's hamartomatous polyps and pigmentation set it apart from the mismatch-repair Lynch syndrome, each a distinct gene with its own cancer spectrum and surveillance."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Bowel emergencies invite sepsis: intussusception and obstruction from large polyps can lead to bowel ischemia and perforation, and the repeated surgeries PJS requires risk intra-abdominal infection and sepsis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Repeated surgery and cancer raise the clot risk: the lifetime of polyp resections and any malignancy that develops predispose Peutz-Jeghers patients to perioperative venous thromboembolism."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Losing the LKB1 brake unleashes it: STK11/LKB1 loss in PJS-associated tumors relieves a restraint on inflammatory and STAT3 signaling, a driver pathway implicated in the lung and GI cancers these patients are prone to."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The tumor-suppressor restrains inflammation: LKB1 loss in Peutz-Jeghers tissue de-represses NF-κB-driven inflammatory signaling, linking the hamartomatous, cancer-prone polyps to a pro-inflammatory microenvironment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Beyond bleeding, chronic disease blunts the marrow: alongside iron-deficiency anemia from chronic polyp bleeding, longstanding inflammation and any malignancy in PJS can add a component of anemia of chronic disease."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Its cancer risk runs the whole gut tube: STK11 loss in Peutz-Jeghers elevates malignancy across the gastrointestinal tract, including the esophagus, adding it to the well-known stomach, small-bowel, colon and pancreatic risks."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Repeated bowel surgery starves bone of nutrients: recurrent intussusception forces small-bowel resections in PJS, and the resulting malabsorption of calcium and vitamin D over a lifetime drives loss of bone density toward osteoporosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong surveillance and surgery weigh on the mind: the constant cancer-screening regimen, recurrent operations and pervasive malignancy risk of Peutz-Jeghers impose a chronic psychological burden that raises depression and anxiety."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Recurrent bowel surgery means recurrent wounds: the repeated laparotomies for intussusception and polypectomy in PJS, sometimes in malnourished patients, leave abdominal wounds and anastomoses prone to slow healing."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its rare gonadal tumours disturb hormones: PJS predisposes to large-cell calcifying Sertoli cell tumours of the testis and sex-cord tumours of the ovary, which secrete oestrogen to cause gynaecomastia and precocious puberty."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Pervasive cancer risk breeds worry: the very high lifetime malignancy risk, lifelong multi-organ screening and recurrent surgery of Peutz-Jeghers foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It markedly raises lung-cancer risk: Peutz-Jeghers carries one of the highest lifetime risks of lung cancer among the hereditary cancer syndromes, extending its spectrum to the respiratory tract."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Microbiome and hamartoma carcinogenesis intertwine: in PJS the colonic microbiome contributes to the inflammation and genotoxic stress that drive its hamartomatous polyps toward malignancy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Loss of LKB1 cools tumour immunity: STK11/LKB1 loss in PJS-related cancers reprogrammes metabolism and creates an immunosuppressive, immune-excluded tumour microenvironment resistant to checkpoint therapy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its many cancers spread through the nodes: the breast, gastrointestinal and gynaecological cancers of PJS metastasise to lymph nodes, determining staging and treatment."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Bleeding and obstruction stress the circulation: recurrent polyp bleeding causes iron-deficiency anaemia that strains the heart, while acute intussusception can cause bowel ischaemia and shock."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its gene tunes energy metabolism: LKB1/AMPK is a master regulator of cellular energy that also governs muscle metabolism, and chronic anaemia and malnutrition from GI bleeding sap muscle strength."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "mTOR inhibition is being explored: because STK11 loss disinhibits mTOR, rapamycin-class drugs are studied to slow the hamartomatous polyps of Peutz-Jeghers syndrome."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "Shared gastric and breast risk: like hereditary diffuse gastric cancer, Peutz-Jeghers syndrome raises the risk of gastric and lobular breast cancer, overlapping their surveillance."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Diet supports the at-risk gut: a high-fibre diet aids gastrointestinal health, a backdrop to the intensive endoscopic surveillance that Peutz-Jeghers syndrome's polyp and cancer risk demands."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for the many cancers it brings: Peutz-Jeghers syndrome sharply raises lifetime risk of gastrointestinal, breast, pancreatic and gynaecological cancers, treated with standard chemotherapy."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Pigmentation marks both: like Carney complex's lentigines, the mucocutaneous pigmentation of Peutz-Jeghers flags an inherited multi-tumour syndrome, the spots a clue to internal cancer risk."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "A marker of immunotherapy resistance: loss of STK11/LKB1, the gene behind Peutz-Jeghers, makes lung and other cancers resistant to PD-1 checkpoint inhibitors, a key negative predictive biomarker."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "It targets the missing kinase's pathway: PJS loses LKB1 (STK11), the kinase that switches on AMPK, so metformin—an AMPK activator—is studied to restrain the mTOR-driven polyp growth and cancer risk that LKB1 loss unleashes."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Two syndromes that unleash mTOR: Peutz-Jeghers loses LKB1-AMPK restraint on mTOR, while tuberous sclerosis loses the TSC1/2 brake on it—different upstream lesions converging on the same hamartoma-driving kinase."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Losing a master metabolic switch: the LKB1-AMPK signalling lost in Peutz-Jeghers normally induces autophagy via ULK1 under energy stress, so STK11 loss impairs this recycling pathway while freeing mTOR—coupling the syndrome's metabolism and cancer risk."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Shared ovarian sex-cord tumours: Peutz-Jeghers (sex-cord tumours with annular tubules) and DICER1 (Sertoli-Leydig) both predispose to ovarian sex-cord-stromal tumours, two germline syndromes converging on this rare tumour family."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "STK11 and lung cancer: the LKB1/STK11 loss of Peutz-Jeghers raises lung cancer risk and is the same gene inactivated somatically in lung adenocarcinoma—where it confers immunotherapy resistance—tying the syndrome to the alveolar epithelium."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Germline multi-cancer surveillance: like Li-Fraumeni, Peutz-Jeghers is an autosomal-dominant syndrome with a very high lifetime cancer risk across many organs, demanding lifelong structured screening."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Pancreatic neoplasia beyond adenocarcinoma: Peutz-Jeghers raises the risk of pancreatic tumours including neuroendocrine tumours, reflecting STK11/LKB1 loss in enteropancreatic tissue alongside the ductal cancers it predisposes to."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "Two syndromes, shared pancreatic surveillance: Peutz-Jeghers and MEN1 are both autosomal-dominant predispositions to pancreatic neoplasia, so both warrant lifelong imaging surveillance of the pancreas despite their different driver genes."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Metastatic endpoint: the gastrointestinal and pancreatic cancers that arise in Peutz-Jeghers spread to the liver, seeding the hepatic lobule in advanced disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 chemoprevention angle: LKB1 loss upregulates COX-2 and prostaglandins in Peutz-Jeghers hamartomas, a rationale for NSAID chemoprevention of its polyps."
  - target: 01-human/03-molecular/tsc1-tsc2
    relation: connects-to
    note: "mTOR convergence: LKB1-AMPK normally restrains mTORC1 through the TSC1-TSC2 complex, so STK11 loss in Peutz-Jeghers deregulates the same mTOR pathway as tuberous sclerosis."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Progression to cancer: unrestrained mTOR and Wnt signalling from LKB1 loss drive MYC activation, helping push Peutz-Jeghers hamartomas toward malignancy."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: mTOR-driven cyclin D1 upregulation from LKB1 loss propels Peutz-Jeghers polyp cells through the G1 checkpoint, fuelling hamartoma growth."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK crosstalk: LKB1 loss in Peutz-Jeghers also enhances RAS-ERK signalling, cooperating with mTOR activation to drive the hamartomatous overgrowth."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Metabolic adaptation: loss of LKB1-AMPK energy sensing stabilises HIF-1α, shifting Peutz-Jeghers cells toward the glycolytic metabolism that supports their growth."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "Lost cell-cycle brake: LKB1 normally induces p21 (CDKN1A) to arrest the cell cycle, so STK11 loss in Peutz-Jeghers removes a checkpoint restraint that contributes to hamartomatous overgrowth and elevated cancer risk."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "Metabolic/stress control: LKB1-AMPK signalling regulates FOXO transcription factors governing gluconeogenesis and stress resistance, an axis disrupted when STK11 is lost in Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Parallel hamartoma suppressor: Peutz-Jeghers (LKB1) and Cowden syndrome (PTEN) are distinct hamartomatous-polyposis syndromes that converge on mTOR disinhibition, illustrating how two tumour suppressors feed the same growth pathway."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Malignant progression: the benign LKB1-driven hamartomas of Peutz-Jeghers acquire somatic driver mutations such as KRAS as they transform into the gastrointestinal adenocarcinomas behind the syndrome's markedly elevated GI-cancer risk."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Hamartomatous-polyposis differential: Peutz-Jeghers (LKB1) sits beside juvenile polyposis (SMAD4/BMPR1A) among the inherited hamartomatous-polyposis syndromes, distinct BMP-versus-LKB1 lesions that share GI polyps and cancer predisposition."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis-resistant growth: LKB1 loss leaves polyp cells with unrestrained mTOR-driven survival signalling that resists caspase-3 apoptosis, the biology that rapalogs (everolimus, rapamycin) reverse to shrink polyps in Peutz-Jeghers models."
  - target: 01-human/03-molecular/cdkn1b
    relation: connects-to
    note: "Cell-cycle restraint: LKB1 normally supports the p27 (CDKN1B) checkpoint, so its loss in Peutz-Jeghers syndrome weakens p27-mediated cell-cycle arrest and contributes to the hamartoma-to-carcinoma progression that drives the syndrome's broad cancer risk."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "AMPK activation requirement: LKB1 is the upstream kinase required for both metformin and adiponectin to activate AMPK, so its germline loss in Peutz-Jeghers blunts this metabolic-sensing axis, part of why metformin is studied as chemoprevention here."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Hamartomatous stroma: the smooth-muscle-rich hamartomatous polyps of Peutz-Jeghers carry an active TGF-β stromal programme, overlapping the SMAD4/TGF-β biology of juvenile polyposis and linking LKB1 loss to the polyp's mesenchymal compartment."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Unrestrained PI3K-mTOR: LKB1 loss removes AMPK-mediated restraint on mTOR (AMPK, mTOR and TSC1-TSC2 mapped), and PIK3CA-driven PI3K signalling further amplifies the growth axis in Peutz-Jeghers polyps and cancers."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle output: the cyclin-D1 axis (mapped, with CDK-inhibitor p21/p27 also mapped) releases E2F1 to drive proliferation in the malignant progression of Peutz-Jeghers-associated tumours."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "EMT and invasion: loss of E-cadherin during epithelial-mesenchymal transition contributes to the invasion of the gastrointestinal and other carcinomas that complicate Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory polyp stroma: IL-6-STAT3 signalling (STAT3 already mapped) sustains the inflammatory stroma of the hamartomatous polyps and the tumour-promoting microenvironment of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbiota inflammation: gut-microbiota-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) provides an inflammatory drive promoting the elevated gastrointestinal-cancer risk of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cancer progression: loss of the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) is among the cooperating events in the malignant progression of Peutz-Jeghers-associated neoplasia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is upregulated in the polyp-to-carcinoma progression of Peutz-Jeghers syndrome, modulating adhesion and immune evasion."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IL-6-JAK-STAT3 signalling (IL-6 and STAT3 mapped) provides a tumour-promoting inflammatory input in the gastrointestinal neoplasia of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of the tumours that arise in Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune surveillance of the gastrointestinal and other neoplasms of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "STK11/LKB1 loss in Peutz-Jeghers syndrome dysregulates the AMPK-FOXO axis (AMPK already mapped) that couples energy stress to growth control."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1 and RB1 already mapped) drives the cell-cycle progression of the hamartoma-to-carcinoma sequence in Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β, integrated with LKB1-AMPK metabolic signaling, modulates the Wnt/β-catenin and survival pathways of the hamartomatous polyps of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis during the polyp-to-cancer progression of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory stroma of the hamartomatous polyps of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative epithelial signaling of the hamartomatous polyps of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic progression of the tumors of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is relevant to the cancer risk of the hamartomatous polyps of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the inflammatory microenvironment of the polyps and tumors of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression participates in the epigenetic dysregulation of the tumors of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the polyps and cancers of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the polyp and tumor microenvironment of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the intestinal-tumor immune microenvironment of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Energy-sensing axis: LKB1 loss in Peutz-Jeghers cripples the AMPK energy sensor it activates, and leptin is the adipokine that signals through hypothalamic AMPK to regulate energy balance, extending the metabolic dysregulation beyond the adiponectin link already mapped."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Feminising gonadal tumours: Peutz-Jeghers boys develop large-cell calcifying Sertoli cell tumours that aromatise androgens to estrogen, causing gynaecomastia and disrupting the testosterone-estrogen balance (estrogen already mapped), a distinctive endocrine feature."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Sex-cord secretory marker: the ovarian sex-cord tumours with annular tubules and gonadal stromal tumours of Peutz-Jeghers secrete inhibin/activin-family peptides, so activin signalling marks and drives this characteristic gonadal neoplasia."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Bleeding anaemia: the hamartomatous polyps of Peutz-Jeghers bleed chronically and cause acute haemorrhage with intussusception, producing the iron-deficiency anaemia that lowers haemoglobin and often prompts the endoscopy that reveals the polyposis."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Mucocutaneous pigmentation: the dark lentiginous macules of the lips, buccal mucosa and digits arise from melanocyte activity, which endothelin-1 through EDNRB regulates, underlying the pathognomonic pigmentation of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Gonadal sex-cord tumours: the ovarian sex-cord and testicular Sertoli-cell tumours of Peutz-Jeghers disturb sex-hormone balance (estrogen and testosterone already mapped), so progesterone and the reproductive-hormone axis figure in their endocrine effects."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Obstructive pain: recurrent intussusception and bowel obstruction from the small-intestinal polyps (already mapped) of Peutz-Jeghers cause severe abdominal pain, often requiring opioid analgesia acting at the mu-opioid receptor around surgery."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: chronic mucosal turnover in the hamartomatous polyps and the loss of LKB1-AMPK metabolic control (already mapped) generate oxidative stress, to which xanthine oxidase contributes, adding DNA damage that speeds malignant progression."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive stroma: the anti-inflammatory cytokine IL-10 in the polyp microenvironment dampens anti-tumour immunity (CD8 already mapped), part of the immune tolerance that allows some Peutz-Jeghers polyps and cancers to progress."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the hamartomatous polyp stroma of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile acids and diet: dietary fat and the bile acids derived from cholesterol promote the gastrointestinal proliferation and the hamartoma-carcinoma progression, a modifiable dietary influence on the cancer risk of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Polyp vasculature: nitric oxide with VEGF and endothelin-1 (already mapped) regulates the vascular tone and angiogenesis of the vascular hamartomatous polyps of Peutz-Jeghers syndrome, part of their stromal biology."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the hamartomatous polyps of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), links the metabolic state governed by the STK11-AMPK (already mapped) axis to the polyp and cancer biology of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin adds an anaemia of chronic disease to the iron-deficiency (already mapped) anaemia of the chronically bleeding polyps of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Hamartoma stroma: PDGF drives the stromal and smooth-muscle (arborising) mesenchymal component of the hamartomatous Peutz-Jeghers polyps, part of their characteristic architecture."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Malabsorption zinc: the zinc deficiency from the chronic GI blood loss and the malabsorption of the extensive polyposis of Peutz-Jeghers syndrome impairs the healing and immunity."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Micronutrient malabsorption: the calcium and micronutrient malabsorption of the extensive GI polyposis of Peutz-Jeghers syndrome, contributing to the nutritional depletion."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate immune surveillance: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the hamartomatous polyps and the cancer-risk surveillance of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the multi-cancer risk of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response along the cancer-risk pathways of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflamed hamartomatous-polyp stroma of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Peutz-Jeghers polyps."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflamed Peutz-Jeghers polyp stroma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Polyp stroma mast cells: the mast cells of the inflamed hamartomatous polyp stroma contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment of Peutz-Jeghers syndrome."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the inflamed polyp stroma of Peutz-Jeghers syndrome."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) shaping the immune surveillance against the malignant transformation of the Peutz-Jeghers polyps."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Mucosal B cells: the B cells of the intestinal mucosa contribute to the humoral and organised immune response within the inflamed stroma of the Peutz-Jeghers polyps."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Polyp complement: the complement C3 activation contributes to the inflammatory dimension of the hamartomatous-polyp stroma of Peutz-Jeghers syndrome."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment into the inflamed stroma of the Peutz-Jeghers polyps."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Intestinal alarmin: TSLP released by the inflamed intestinal epithelium of Peutz-Jeghers polyps activates mast cells and dendritic cells, promoting the type-2 inflammatory stroma and accelerating the STK11-mutant adenoma transition."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Hamartomatous ECM: periostin, a downstream target of the PI3K pathway (mTOR already mapped) dysregulated by STK11 loss, drives the mesenchymal overgrowth and fibroblast expansion of the Peutz-Jeghers polyp stroma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Polyp mast-cell effector: histamine from the abundant stromal mast cells of Peutz-Jeghers polyps promotes angiogenesis and mucous secretion, contributing to the obstructive and intussusception episodes that dominate the clinical course."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Polyp-pain kinin: bradykinin generated in the inflamed stroma of Peutz-Jeghers intestinal polyps activates nociceptive B1/B2 receptors, amplifying visceral pain and the obstructive and intussusception episodes that drive emergency presentations."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: C1-esterase inhibitor restrains the classical complement pathway (C3 and C5aR1 already mapped) within the inflammatory polyp stroma of Peutz-Jeghers syndrome, limiting complement-driven myeloid recruitment and mucosal oedema."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Iron-deficiency anaemia support: erythropoietin addresses the chronic iron-deficiency anaemia (iron and IDA already mapped) driven by repeated haemorrhage from the large vascular Peutz-Jeghers polyps, when endoscopic resection cannot keep pace."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "PJS circadian-oncology: melatonin inhibits the STK11/LKB1 (already mapped) loss-driven mTOR (already mapped) hyperactivation underlying Peutz-Jeghers polyp growth, and melatonin receptor expression on the hamartomatous polyp epithelium modulates polyp cell proliferation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "PJS enterochromaffin serotonin: serotonin secreted by the abundant enterochromaffin cells in the Peutz-Jeghers gastrointestinal polyps modulates secretory diarrhoea, motility and visceral pain (bradykinin already mapped) in the hamartomatous polyposis syndrome."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "PJS prolactin: prolactin via JAK2/STAT5 signalling activates the mTOR (already mapped) pathway in the Peutz-Jeghers hamartomatous polyp epithelium, and hyperprolactinaemia amplifies the STK11/LKB1 (already mapped) loss-driven epithelial proliferation."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PJS oxytocin: oxytocin modulates intestinal motility and mucosal barrier integrity in the GI tract bearing the Peutz-Jeghers hamartomatous polyps, and oxytocin receptor signalling on enteric neurons (already mapped) intersects STK11/LKB1 (already mapped) epithelial homeostasis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PJS vasopressin: vasopressin via V2R modulates intestinal fluid absorption and mucosal homeostasis in the GI tract harbouring the Peutz-Jeghers hamartomatous polyps, intersecting the STK11/LKB1 (already mapped) and mTOR (already mapped) epithelial proliferation axis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "PJS selenium: selenium-dependent selenoprotein antioxidants quench reactive-oxygen-species arising from STK11/LKB1 (already mapped) loss-driven mTOR (already mapped) hyperactivation in Peutz-Jeghers polyp epithelium, reducing oncogenic transformation risk."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Peutz-Jeghers iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) polyp cascade of Peutz-Jeghers syndrome."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Peutz-Jeghers sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the T-cytotoxic (already mapped) cancer cascade of Peutz-Jeghers syndrome."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Peutz-Jeghers magnesium: magnesium, as LKB1/STK11 (already mapped) kinase cofactor in fibroblasts (already mapped) and macrophages (already mapped), supports tumour-suppression; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of PJS."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Peutz-Jeghers potassium: potassium governs macrophage (already mapped) and mast-cell (already mapped) polyp immune tone; potassium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade suppressing T-cytotoxic (already mapped) function in PJS."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Peutz-Jeghers phosphorus: phosphorus as ATP cofactor in macrophages (already mapped) and fibroblasts (already mapped) sustains LKB1/STK11 (already mapped) signalling; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) polyp-cancer cascade of PJS."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Peutz-Jeghers chloride: chloride in macrophages (already mapped) and mast-cell (already mapped) regulates stromal inflammation; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and suppresses T-cytotoxic (already mapped) surveillance in PJS."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Peutz-Jeghers carbon: carbon as backbone of LKB1/STK11 (already mapped) and NF-κB (already mapped) proteins in epithelial cells sustains tumour-suppressive signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) polyp-cancer cascade of PJS."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Peutz-Jeghers hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and fibroblasts (already mapped), supports LKB1/STK11 (already mapped) kinase activity; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PJS."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Peutz-Jeghers nitrogen: nitrogen in amino-acid scaffold of LKB1/STK11 (already mapped) and mTOR (already mapped) proteins in polyp epithelial cells sustains signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PJS."
---

# Peutz-Jeghers Syndrome

## Overview

**Peutz-Jeghers syndrome (PJS)** is an autosomal dominant hamartomatous polyposis syndrome caused by germline pathogenic variants in **STK11** (LKB1), a master serine/threonine kinase that activates AMPK and controls mTOR signaling and cell polarity. PJS affects approximately 1 in 50,000 to 200,000 individuals and is characterized by: (1) **hamartomatous gastrointestinal polyps** (predominantly small intestine) lined by branching smooth muscle with overlying normal mucosa — the so-called "Christmas tree" arborizing pattern; (2) **mucocutaneous melanotic macules** (lips, perioral skin, buccal mucosa, fingertips, genitalia) from melanin deposits in dermal macrophages; and (3) markedly elevated lifetime risks for multiple cancers — most prominently breast (~45%), CRC (~39%), and pancreatic (~36%) by age 70. The most acute complication is **small bowel intussusception** from large polyps, presenting as episodic abdominal pain, vomiting, and obstruction. There is no cure; management focuses on endoscopic surveillance and polypectomy to prevent obstruction and cancer [^hearle-2006-pjs-cancer].

**Epidemiology:**
- Prevalence: 1/50,000-200,000; estimated ~5,000-15,000 cases in the USA
- Inheritance: autosomal dominant; 50% transmission per pregnancy; ~45% de novo (no family history)
- STK11 germline pathogenic variant: ~94% of PJS families; ~6% STK11-negative (possible other loci or missed variants)
- Penetrance: nearly complete for polyps (>95%); cancer risk penetrance variable and age-dependent
- Median age of PJS diagnosis: typically childhood (polyp detection or intussusception) or young adulthood; mucocutaneous pigmentation may be the first clue in infancy

**Cumulative cancer risks by age 70 (Hearle 2006):** [^hearle-2006-pjs-cancer]

| Cancer | Cumulative risk by age 70 | Notes |
|---|---|---|
| Breast | ~45-54% | High; BRCA1/2-equivalent risk in some series |
| Colorectal | ~39% | Hamartoma-adenoma-carcinoma sequence |
| Pancreatic | ~36% | Very high; aggressive; EUS surveillance critical |
| Small intestinal | ~13% | Arising from PJ polyps; rare pre-PJS surveillance era |
| Gastric | ~29% | Type depends on PJS genetics and geography |
| Ovarian (SCTAT) | ~21% | Sex cord tumor with annular tubules — unique PJS tumor |
| Cervical (adenoma malignum) | ~10% | Minimal deviation adenocarcinoma; unusual PJS tumor |
| Uterine | ~9% | Less studied; cervical + uterine combined risk ~10-15% |

## Structure

### STK11 and PJS polyp biology

**STK11/LKB1 molecular basis:**
STK11 is the master upstream kinase of AMPK and 12 AMPK-related kinases (MARK1-4, SIK1-3, BRSK1/2, NUAK1/2); germline STK11 LOF → haploinsufficiency of STK11 in intestinal epithelium → somatic second hit in polyp epithelium → biallelic STK11 LOF → AMPK inactivation → mTOR hyperactivation → epithelial overgrowth + smooth muscle proliferation → hamartoma formation; unlike FAP (adenomatous) or juvenile polyposis (JPS), PJS polyps are hamartomas — they contain normal cellular elements in disorganized architecture

**PJ polyp pathology:**
- Macroscopic: lobulated, pedunculated; largest in small intestine (jejunum > ileum); smaller in colon and stomach; multiple (dozens to hundreds over a lifetime)
- Microscopic: arborizing smooth muscle core (from muscularis mucosae) covered by normal colonic/small intestinal epithelium; the "Christmas tree" pattern of smooth muscle branching into polyp lobules is pathognomonic; no dysplasia in the polyp itself
- Intussusception mechanism: large polyp acts as intussusceptum (lead point) → peristalsis → telescoping of bowel around polyp → obstruction; can be acute surgical emergency; PJS presents with recurrent episodic intussusception in childhood/adolescence

**Mucocutaneous pigmentation:**
- Mechanism: dermal melanin deposition in histiocytes/macrophages; NOT melanocyte proliferation (non-neoplastic)
- Distribution: lips (lower and upper; most specific for PJS), perioral skin, buccal mucosa, fingertips, palms, genitalia; may be present at birth or appear in early childhood
- Fate: perioral and skin pigmentation may fade with age (especially after puberty); buccal mucosal pigmentation tends to persist; the fading of lip pigmentation does not mean LOF — PJS diagnosis is still valid
- Distinction: Laugier-Hunziker syndrome (acquired; no polyps; no cancer risk); Addison disease (diffuse hyperpigmentation, not discrete macules); normal ethnic variation

### Unique PJS tumor types

**Sex cord tumor with annular tubules (SCTAT):**
Unique ovarian tumor type in PJS: arises from granulosa-theca cells; bilateral (multifocal) in PJS (contrast: unilateral in sporadic SCTAT); usually benign in PJS; small, calcified; estrogen and inhibin-producing → menstrual irregularities, precocious puberty; IHC: inhibin-positive, calretinin-positive; malignancy rare but possible in large PJS SCTAT; annual TVUS for female PJS patients

**Adenoma malignum (minimal deviation adenocarcinoma of cervix):**
Rare cervical glandular tumor seen disproportionately in PJS (~10% lifetime risk, vs <0.1% general population); well-differentiated mucin-producing glands → easily mistaken for normal endocervical glands; extremely difficult to diagnose by cytology alone; diagnosis: deep biopsy + CEA staining; pap smear + annual cervical examination for PJS females; radical hysterectomy if diagnosed

## Function

### PJS carcinogenesis: hamartoma-adenoma-carcinoma sequence

**Mechanism of cancer development:**
PJS polyps themselves are hamartomas — they have very low intrinsic malignant potential; however, PJS patients develop adenomas (not from PJ hamartomas directly, but as separate lesions) at higher rates than the general population; adenomas arise in the context of STK11 LOF + mTOR hyperactivation + dysregulated epithelial proliferation; adenoma → carcinoma sequence is the main pathway for CRC in PJS; small intestinal cancer may arise directly from PJ hamartoma-adenoma transition (uncommon)

**mTOR pathway in PJS tumorigenesis:**
STK11 LOF → AMPK loss → mTORC1 unrestrained → S6K1 activation → ribosome biogenesis → epithelial and smooth muscle growth → PJ polyp formation; in mouse models: STK11+/- mice develop GI polyps similar to human PJS; rapamycin (mTOR inhibitor) given to STK11+/- mice reduces polyp number and size by ~50-80% (several independent studies); this validates mTOR as the mechanistic driver; in STK11+/- cells: rapamycin induces autophagy and corrects the proliferative excess

**STK11 and breast cancer risk:**
PJS breast cancer risk (~45%) approaches BRCA1/2-associated risk; mechanism: STK11 LOF → AMPK loss → mTOR hyperactivation in breast epithelium → accelerated proliferation; STK11-mutant breast cancer: no specific histology; HR+ predominance; no clear HER2 enrichment; breast MRI surveillance (same as BRCA1/2 guidelines) recommended from age 25; risk-reducing mastectomy: discussed but evidence limited compared to BRCA1/2 context

## Pathology

### Diagnosis

**Clinical diagnostic criteria:**
Any ONE of the following confirms PJS diagnosis:
1. Three or more histologically confirmed PJ polyps (small intestinal hamartomas with arborizing smooth muscle)
2. Any number of PJ polyps + family history of PJS in a first-degree relative
3. Characteristic mucocutaneous pigmentation + family history of PJS
4. Any number of PJ polyps + characteristic mucocutaneous pigmentation

**Genetic testing:**
- STK11 germline sequencing (full coding + splice sites) + MLPA for large rearrangements: ~94% detection rate in clinical PJS
- ~6% STK11-negative PJS: likely technical false-negative (deep intronic, somatic mosaicism) or extremely rare alternative loci
- Pathogenicity classification: truncating = pathogenic; missense: variant interpretation using functional assays and co-segregation data
- Cascade testing: all first-degree relatives of STK11 carrier should be offered testing

### Surveillance and management (NCCN/ESMO 2024)

**Gastrointestinal surveillance:**

Small bowel (highest priority):
- Video capsule endoscopy (VCE): gold standard for small bowel visualization; every 1-3 years from age 8-10; polypectomy of polyps >1-1.5 cm by device-assisted enteroscopy (double-balloon enteroscopy, DBE) to prevent intussusception
- DBE polypectomy: preferred over surgical resection to preserve small bowel length; all PJ polyps >1.5 cm should be removed

Upper GI (gastric/duodenal):
- Upper endoscopy: every 1-3 years from age 8-10; gastric PJ polyps usually small; duodenal surveillance important (ampullary region)

Colorectal:
- Colonoscopy: every 1-3 years from age 15-20 (some guidelines: 18 years or first bowel symptoms, whichever is first)
- Adenomatous polyps removed at colonoscopy (same as non-PJS adenoma management)

**Gynecologic surveillance (female PJS):**
- Pelvic exam + pap smear annually from age 18-20 (cervical adenoma malignum)
- Pelvic TVUS: annually from age 20-25 (SCTAT detection)
- Endometrial biopsy: not routinely recommended (uterine cancer risk ~9% is lower); evaluate abnormal uterine bleeding

**Breast surveillance:**
- Annual breast MRI + annual mammogram from age 25-30 (same intensity as BRCA1/2)
- Clinical breast exam every 6 months from age 25
- Risk-reducing bilateral mastectomy: considered in high-risk individuals after discussion of risk-benefit; less evidence than BRCA1/2 context

**Pancreatic surveillance:**
- Endoscopic ultrasound (EUS) + MRI/MRCP: every 1-2 years from age 30-35
- CA19-9: annual from age 30-35 (modest sensitivity/specificity; trend more useful than single value)
- Urgency: PJS pancreatic cancer is often detected at advanced/unresectable stage; early detection critical

**Treatment:**
- Small bowel intussusception: urgent endoscopic or surgical reduction; DBE or laparotomy + intraoperative enteroscopy to clear accessible polyps at time of surgery
- Cancer treatment: same as sporadic cancer of that type; no PJS-specific chemotherapy regimen
- mTOR inhibition: rapamycin (sirolimus) + metformin combination pilot trial in PJS patients (NCT03943992): reduces polyp burden modestly; ongoing; not yet standard of care
- Metformin: single-agent pilot data showing reduction in small bowel polyp number in PJS; Phase 2 trials ongoing; mechanism: indirect AMPK activation bypasses STK11 LOF

**Prognosis:**
Without surveillance: cumulative cancer risk reaches ~85-93% by age 70 (all cancer types combined); with active surveillance: cancer incidence and mortality markedly reduced but not eliminated; intussusception risk remains the dominant pediatric morbidity; cancer accounts for the major adult morbidity and mortality

## Connections

- `connects-to` → **[STK11](../../03-molecular/stk11/README.md)** — Germline STK11 mutations cause ~94% of PJS; STK11 encodes LKB1 (AMPK activator); haploinsufficiency → polyp formation (second hit in polyp epithelium); truncating STK11 mutations associate with higher cancer risk than missense; STK11 germline panel + deletion analysis required
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — STK11 LOF → AMPK inactivation → mTOR unrestrained → hamartoma growth in PJS; rapamycin reduces polyp burden in STK11+/− mouse models; mTORC1 is the primary growth driver in PJS hamartomas; AMPK activators (metformin) explored as chemoprevention in PJS pilot studies
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — PJS lifetime CRC risk ~39% by age 70 (Hearle 2006); PJS CRC arises through hamartoma-adenoma-carcinoma sequence; proximal colon predominance; colonoscopy with polypectomy every 1-3 years from age 15-20; CRC is the third most common PJS cancer after breast and pancreatic
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — PJS lifetime pancreatic cancer risk ~36% by age 70; EUS + MRI surveillance from age 30-35; STK11 LOF co-mutation with KRAS in pancreatic cancer → mTOR + MAPK dual activation; PJS pancreatic cancer prognosis poor; resectability rate ~40% at detection
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — STK11 LOF → AMPK loss → mTORC1 unrestrained → S6K1/4EBP1 → epithelial and smooth muscle proliferation → PJ hamartoma formation; rapamycin reduces polyp burden ~50-80% in STK11+/− mice; sirolimus + metformin pilot trial ongoing in PJS patients (NCT03943992).
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — PJS breast cancer lifetime risk ~45-54% by age 70 (BRCA1/2-equivalent); breast MRI + mammogram from age 25; STK11 LOF → mTOR hyperactivation in breast epithelium; HR+ predominant; no PJS-specific breast cancer histology; risk-reducing bilateral mastectomy discussed.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — STK11/LKB1 somatic mutations in ~15-20% of KRAS-mutant lung adenocarcinoma; STK11 loss → PD-L1 downregulation + CXCL7 secretion → neutrophilic immunosuppressive TME → primary ICB resistance; STK11-mutant KRAS+ NSCLC is the poorest immunotherapy responder subgroup.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine is the danger zone of Peutz-Jeghers syndrome: large hamartomatous polyps in the jejunum and ileum become lead points for intussusception — the most common complication, often needing emergency surgery in childhood; surveillance and polypectomy prevent it.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The diagnostic clue to Peutz-Jeghers syndrome is on the skin and lips: mucocutaneous melanotic macules — dark freckle-like spots on the lips, buccal mucosa, and fingertips — appear in infancy and often fade with age, but with hamartomatous polyps they establish the diagnosis.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Peutz-Jeghers hamartomas have a unique histology: an arborizing (tree-like) core of bundled smooth muscle extending into the polyp, covered by normal epithelium — distinguishing them from the edematous juvenile polyps of JPS or the dysplastic adenomas of FAP.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — Peutz-Jeghers and juvenile polyposis are the two main hamartomatous polyposis syndromes: PJS (STK11) produces arborizing smooth-muscle polyps and mucocutaneous pigmentation, while JPS (SMAD4/BMPR1A) produces juvenile polyps—both raise GI cancer risk.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Peutz-Jeghers syndrome predisposes to distinctive ovarian tumors: sex cord tumors with annular tubules (SCTAT) and mucinous tumors arise from STK11 loss, often causing precocious puberty or estrogen effects—part of the syndrome's broad, organ-spanning cancer risk.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Peutz-Jeghers syndrome carries a rare cervical cancer—adenoma malignum (minimal-deviation adenocarcinoma): this deceptively bland, HPV-independent tumor is strongly associated with STK11 loss, so PJS patients warrant gynecologic surveillance for it.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Peutz-Jeghers and Cowden are both hamartomatous polyposis syndromes with different genes: PJS from STK11 loss giving GI hamartomas and mucocutaneous pigmentation, Cowden from PTEN (PI3K-AKT) loss—both fill the gut with hamartomas and raise multi-organ cancer risk.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Peutz-Jeghers and FAP are inherited polyposis syndromes with opposite polyp types: PJS produces hamartomatous polyps from STK11 loss, while FAP produces hundreds of adenomatous polyps from APC loss with near-certain colorectal cancer—hamartoma versus adenoma.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Peutz-Jeghers raises gastric as well as colorectal cancer risk: STK11 loss seeds hamartomatous polyps throughout the stomach and small bowel that can bleed, obstruct or harbor dysplasia, so upper-GI surveillance accompanies colonoscopy in PJS patients from childhood.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Peutz-Jeghers polyps stud the large intestine and beyond: STK11 loss produces hamartomatous polyps throughout the GI tract—small bowel most, but also colon—that bleed, cause intussusception, and modestly raise colorectal cancer risk.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — PJS hamartomas arise in disordered intestinal epithelium: loss of the STK11/LKB1 kinase deranges epithelial polarity and growth, so the crypts overgrow into the branching, smooth-muscle-cored hamartomatous polyps that distinguish PJS from adenomatous polyposis.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — PJS shows a non-Wnt route to GI tumors: unlike FAP's APC/Wnt adenomas, Peutz-Jeghers polyps arise from STK11/LKB1-AMPK-mTOR dysregulation, so its hamartomas form by a different pathway—though malignant transformation can still recruit Wnt-driven changes.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Peutz-Jeghers fills the digestive tract with hamartomatous polyps: STK11/LKB1 loss seeds large hamartomas, especially in the small bowel, that bleed and cause intussusception in childhood—so GI polyps and obstruction often bring the diagnosis.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Pigmented spots make Peutz-Jeghers visible on the skin: mucocutaneous melanin macules on the lips, mouth and fingers appear in childhood, so these freckle-like spots are often the first clue to this STK11 polyposis-and-cancer syndrome.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Peutz-Jeghers affects the reproductive system with distinctive tumors: women develop sex-cord tumors with annular tubules (SCTAT) and raised cervical/ovarian cancer risk, and men can get calcifying Sertoli cell testicular tumors—warranting gonadal surveillance.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Peutz-Jeghers hamartomas stud the whole gut, including the stomach: gastric polyps add to the small-bowel ones, contributing bleeding and a raised gastric-cancer risk, so upper endoscopy joins small-bowel surveillance in management.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Peutz-Jeghers often presents with iron-deficiency anemia: chronic slow bleeding from gastrointestinal hamartomas depletes iron, so unexplained anemia in a young patient with lip pigmentation can be the clue that prompts diagnosis.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — Peutz-Jeghers and MUTYH-associated polyposis are distinct inherited polyposes: PJS makes STK11-driven hamartomas with smooth-muscle cores, while MAP makes adenomas from oxidative DNA-repair failure—so polyp histology and gene testing separate them.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Peutz-Jeghers grows hormone-secreting gonadal tumors: ovarian sex cord tumors (SCTAT) and testicular Sertoli cell tumors pour out estrogen, causing precocious puberty, gynecomastia, and irregular bleeding—distinctive endocrine clues to the syndrome.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Peutz-Jeghers unleashes AKT-mTOR growth: LKB1 loss disables the AMPK brake, so the AKT-mTOR pathway runs unchecked in the hamartomatous polyps—rationale for trialing mTOR inhibitors to slow polyp growth and cancer risk.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Peutz-Jeghers polyps grow large on a fibroblast-rich hamartomatous stroma: their bulky, arborizing structure can drag a loop of bowel into itself (intussusception), the acute complication that often brings these polyps to medical attention.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Peutz-Jeghers polyps bleed and drain iron: the large hamartomas erode and ooze blood into the gut, and with the obstruction they cause, chronic blood loss makes iron-deficiency anemia a frequent sign in these patients.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages help build the Peutz-Jeghers polyp: tumor-associated macrophages populate the fibroblast-rich hamartomatous stroma and secrete growth and angiogenic factors, supporting the bulky polyps that arise from LKB1 loss.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Peutz-Jeghers polyps recruit blood vessels via VEGF: LKB1/AMPK loss disinhibits mTOR, which drives VEGF and angiogenesis to feed the growing hamartomas, part of the rationale for mTOR-pathway drugs studied in the syndrome.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Peutz-Jeghers' freckles are made with copper: the dark spots on the lips and mouth are melanin, built by the copper-dependent enzyme tyrosinase, the mucocutaneous sign that flags the syndrome.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Peutz-Jeghers carries a steep pancreatic cancer risk: STK11 loss makes the pancreas one of the syndrome's most dangerous cancer sites, so it joins the gut and breast in lifelong surveillance.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Peutz-Jeghers polyps are fragile and vascular: their endothelial-lined vessels tear easily as the bulky polyps tumble and intussuscept, causing the recurrent bleeding that drains the body's iron.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons keep watch over the small bowel: video capsule endoscopy and MR enterography survey the long stretches of intestine that ordinary scopes miss, finding the hamartomatous polyps before they grow big enough to bleed or obstruct.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Losing STK11 raises the lung's cancer risk: Peutz-Jeghers carries one of the highest lifetime risks of lung cancer among inherited syndromes, so the same gene that studs the gut with polyps also primes the airway lining for malignancy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver becomes a target as Peutz-Jeghers cancers spread: the syndrome's many adenocarcinomas — pancreatic, gastrointestinal, breast — metastasize there, so liver imaging joins the broad cancer surveillance these patients need.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Peutz-Jeghers often shows up as anemia: the hamartomatous polyps bleed slowly into the gut, draining red cells and iron until a child turns up pale and microcytic — sometimes the first clue that leads to the diagnosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — The telltale freckling is melanin under the microscope: the dark macules on lips and buccal mucosa come from melanin packed into basal keratinocytes, pigment granules that electron microscopy resolves within the epidermis.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Peutz-Jeghers reaches into the gynecologic tract: beyond its signature cervical and ovarian sex-cord tumors, the syndrome raises the lifetime risk of endometrial cancer, adding the uterus to its wide field of cancer surveillance.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains confirm the hallmark polyp: desmin and smooth-muscle-actin staining reveal the arborizing tree of smooth muscle that defines a Peutz-Jeghers hamartoma, separating it from the adenomas of other polyposis syndromes.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid joins the long cancer list: differentiated (papillary) thyroid carcinoma appears within the Peutz-Jeghers tumor spectrum, one more organ folded into the lifelong, head-to-pelvis surveillance the syndrome demands.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Chronic ooze from the polyps shows in the blood: the slow intestinal bleeding that drains iron also drives a reactive thrombocytosis, the platelet count climbing as the marrow responds to ongoing loss.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — STK11 is the master switch above AMPK: losing it deranges the LKB1-AMPK energy sensor that ties metabolism to growth, which is why metformin — an AMPK activator that improves insulin signaling — is studied as chemoprevention in Peutz-Jeghers.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Losing LKB1 turns tumors cold: STK11/LKB1 loss reshapes the microenvironment to exclude and disarm cytotoxic T cells, a recognized driver of resistance to checkpoint immunotherapy in the lung and other cancers it predisposes to.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — The faulty gene sits at the body's energy controls: LKB1-AMPK signaling governs how adipocytes and other tissues sense and store energy, so the syndrome's defect reaches a metabolic network far beyond the gut polyps it is known for.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — The defective kinase reaches the master tumor suppressor: LKB1 normally helps activate p53-dependent apoptosis and growth arrest, so losing it weakens this checkpoint as well, compounding the cancer risk beyond the unleashed mTOR signaling.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — The lungs are on the long cancer list: Peutz-Jeghers raises the risk of lung cancer, including small cell carcinoma, one of the many epithelial tissues where LKB1 loss removes a brake — a reminder its danger reaches well beyond the gut.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — The biliary tree is not spared: the syndrome's broad cancer predisposition extends to the bile ducts, so cholangiocarcinoma joins the pancreatic and gastrointestinal tumors that make lifelong, multi-organ surveillance the core of PJS care.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — It headlines the hereditary GI-cancer differential: PJS's hamartomatous polyps and pigmentation set it apart from the mismatch-repair Lynch syndrome, each a distinct gene with its own cancer spectrum and surveillance.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Bowel emergencies invite sepsis: intussusception and obstruction from large polyps can lead to bowel ischemia and perforation, and the repeated surgeries PJS requires risk intra-abdominal infection and sepsis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Repeated surgery and cancer raise the clot risk: the lifetime of polyp resections and any malignancy that develops predispose Peutz-Jeghers patients to perioperative venous thromboembolism.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Losing the LKB1 brake unleashes it: STK11/LKB1 loss in PJS-associated tumors relieves a restraint on inflammatory and STAT3 signaling, a driver pathway implicated in the lung and GI cancers these patients are prone to.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The tumor-suppressor restrains inflammation: LKB1 loss in Peutz-Jeghers tissue de-represses NF-κB-driven inflammatory signaling, linking the hamartomatous, cancer-prone polyps to a pro-inflammatory microenvironment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Beyond bleeding, chronic disease blunts the marrow: alongside iron-deficiency anemia from chronic polyp bleeding, longstanding inflammation and any malignancy in PJS can add a component of anemia of chronic disease.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Its cancer risk runs the whole gut tube: STK11 loss in Peutz-Jeghers elevates malignancy across the gastrointestinal tract, including the esophagus, adding it to the well-known stomach, small-bowel, colon and pancreatic risks.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Repeated bowel surgery starves bone of nutrients: recurrent intussusception forces small-bowel resections in PJS, and the resulting malabsorption of calcium and vitamin D over a lifetime drives loss of bone density toward osteoporosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong surveillance and surgery weigh on the mind: the constant cancer-screening regimen, recurrent operations and pervasive malignancy risk of Peutz-Jeghers impose a chronic psychological burden that raises depression and anxiety.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Recurrent bowel surgery means recurrent wounds: the repeated laparotomies for intussusception and polypectomy in PJS, sometimes in malnourished patients, leave abdominal wounds and anastomoses prone to slow healing.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its rare gonadal tumours disturb hormones: PJS predisposes to large-cell calcifying Sertoli cell tumours of the testis and sex-cord tumours of the ovary, which secrete oestrogen to cause gynaecomastia and precocious puberty.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Pervasive cancer risk breeds worry: the very high lifetime malignancy risk, lifelong multi-organ screening and recurrent surgery of Peutz-Jeghers foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It markedly raises lung-cancer risk: Peutz-Jeghers carries one of the highest lifetime risks of lung cancer among the hereditary cancer syndromes, extending its spectrum to the respiratory tract.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Microbiome and hamartoma carcinogenesis intertwine: in PJS the colonic microbiome contributes to the inflammation and genotoxic stress that drive its hamartomatous polyps toward malignancy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Loss of LKB1 cools tumour immunity: STK11/LKB1 loss in PJS-related cancers reprogrammes metabolism and creates an immunosuppressive, immune-excluded tumour microenvironment resistant to checkpoint therapy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its many cancers spread through the nodes: the breast, gastrointestinal and gynaecological cancers of PJS metastasise to lymph nodes, determining staging and treatment.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Bleeding and obstruction stress the circulation: recurrent polyp bleeding causes iron-deficiency anaemia that strains the heart, while acute intussusception can cause bowel ischaemia and shock.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its gene tunes energy metabolism: LKB1/AMPK is a master regulator of cellular energy that also governs muscle metabolism, and chronic anaemia and malnutrition from GI bleeding sap muscle strength.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — mTOR inhibition is being explored: because STK11 loss disinhibits mTOR, rapamycin-class drugs are studied to slow the hamartomatous polyps of Peutz-Jeghers syndrome.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — Shared gastric and breast risk: like hereditary diffuse gastric cancer, Peutz-Jeghers syndrome raises the risk of gastric and lobular breast cancer, overlapping their surveillance.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Diet supports the at-risk gut: a high-fibre diet aids gastrointestinal health, a backdrop to the intensive endoscopic surveillance that Peutz-Jeghers syndrome's polyp and cancer risk demands.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for the many cancers it brings: Peutz-Jeghers syndrome sharply raises lifetime risk of gastrointestinal, breast, pancreatic and gynaecological cancers, treated with standard chemotherapy.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Pigmentation marks both: like Carney complex's lentigines, the mucocutaneous pigmentation of Peutz-Jeghers flags an inherited multi-tumour syndrome, the spots a clue to internal cancer risk.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — A marker of immunotherapy resistance: loss of STK11/LKB1, the gene behind Peutz-Jeghers, makes lung and other cancers resistant to PD-1 checkpoint inhibitors, a key negative predictive biomarker.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — It targets the missing kinase's pathway: PJS loses LKB1 (STK11), the kinase that switches on AMPK, so metformin—an AMPK activator—is studied to restrain the mTOR-driven polyp growth and cancer risk that LKB1 loss unleashes.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Two syndromes that unleash mTOR: Peutz-Jeghers loses LKB1-AMPK restraint on mTOR, while tuberous sclerosis loses the TSC1/2 brake on it—different upstream lesions converging on the same hamartoma-driving kinase.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Losing a master metabolic switch: the LKB1-AMPK signalling lost in Peutz-Jeghers normally induces autophagy via ULK1 under energy stress, so STK11 loss impairs this recycling pathway while freeing mTOR—coupling the syndrome's metabolism and cancer risk.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Shared ovarian sex-cord tumours: Peutz-Jeghers (sex-cord tumours with annular tubules) and DICER1 (Sertoli-Leydig) both predispose to ovarian sex-cord-stromal tumours, two germline syndromes converging on this rare tumour family.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — STK11 and lung cancer: the LKB1/STK11 loss of Peutz-Jeghers raises lung cancer risk and is the same gene inactivated somatically in lung adenocarcinoma—where it confers immunotherapy resistance—tying the syndrome to the alveolar epithelium.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Germline multi-cancer surveillance: like Li-Fraumeni, Peutz-Jeghers is an autosomal-dominant syndrome with a very high lifetime cancer risk across many organs, demanding lifelong structured screening.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Pancreatic neoplasia beyond adenocarcinoma: Peutz-Jeghers raises the risk of pancreatic tumours including neuroendocrine tumours, reflecting STK11/LKB1 loss in enteropancreatic tissue alongside the ductal cancers it predisposes to.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — Two syndromes, shared pancreatic surveillance: Peutz-Jeghers and MEN1 are both autosomal-dominant predispositions to pancreatic neoplasia, so both warrant lifelong imaging surveillance of the pancreas despite their different driver genes.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Metastatic endpoint: the gastrointestinal and pancreatic cancers that arise in Peutz-Jeghers spread to the liver, seeding the hepatic lobule in advanced disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 chemoprevention angle: LKB1 loss upregulates COX-2 and prostaglandins in Peutz-Jeghers hamartomas, a rationale for NSAID chemoprevention of its polyps.
- `connects-to` → **[TSC1-TSC2](../../03-molecular/tsc1-tsc2/README.md)** — mTOR convergence: LKB1-AMPK normally restrains mTORC1 through the TSC1-TSC2 complex, so STK11 loss in Peutz-Jeghers deregulates the same mTOR pathway as tuberous sclerosis.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Progression to cancer: unrestrained mTOR and Wnt signalling from LKB1 loss drive MYC activation, helping push Peutz-Jeghers hamartomas toward malignancy.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: mTOR-driven cyclin D1 upregulation from LKB1 loss propels Peutz-Jeghers polyp cells through the G1 checkpoint, fuelling hamartoma growth.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK crosstalk: LKB1 loss in Peutz-Jeghers also enhances RAS-ERK signalling, cooperating with mTOR activation to drive the hamartomatous overgrowth.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Metabolic adaptation: loss of LKB1-AMPK energy sensing stabilises HIF-1α, shifting Peutz-Jeghers cells toward the glycolytic metabolism that supports their growth.
- `connects-to` → **[p21 (CDKN1A)](../../03-molecular/cdkn1a/README.md)** — LKB1 normally induces p21 to arrest the cell cycle, so STK11 loss in Peutz-Jeghers removes a checkpoint restraint—contributing to the hamartomatous overgrowth and the broadly elevated cancer risk that defines the syndrome.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — LKB1-AMPK signaling regulates FOXO transcription factors governing gluconeogenesis and stress resistance, an axis disrupted when STK11 is lost in Peutz-Jeghers, linking the syndrome's tumor-suppressor gene to metabolic dysregulation.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Peutz-Jeghers (LKB1) and Cowden syndrome (PTEN) are distinct hamartomatous-polyposis syndromes that converge on mTOR disinhibition—illustrating how two different tumor suppressors funnel into the same growth pathway and overlapping GI-polyp and cancer phenotypes.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — The benign LKB1-driven hamartomas of Peutz-Jeghers acquire somatic driver mutations such as KRAS as they transform into the gastrointestinal adenocarcinomas behind the syndrome's markedly elevated GI-cancer risk.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Peutz-Jeghers (LKB1) sits beside juvenile polyposis (SMAD4/BMPR1A) among the inherited hamartomatous-polyposis syndromes, distinct BMP-versus-LKB1 lesions that share GI polyps and cancer predisposition.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — LKB1 loss leaves polyp cells with unrestrained mTOR-driven survival signaling that resists caspase-3 apoptosis, the biology that rapalogs (everolimus, rapamycin) reverse to shrink polyps in Peutz-Jeghers models.
- `connects-to` → **[CDKN1B](../../03-molecular/cdkn1b/README.md)** — LKB1 normally supports the p27 (CDKN1B) checkpoint, so its loss in Peutz-Jeghers syndrome weakens p27-mediated cell-cycle arrest and contributes to the hamartoma-to-carcinoma progression that drives the syndrome's broad cancer risk.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — LKB1 is the upstream kinase required for both metformin and adiponectin to activate AMPK, so its germline loss in Peutz-Jeghers blunts this metabolic-sensing axis, part of why metformin is studied as chemoprevention here.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — The smooth-muscle-rich hamartomatous polyps of Peutz-Jeghers carry an active TGF-β stromal program, overlapping the SMAD4/TGF-β biology of juvenile polyposis and linking LKB1 loss to the polyp's mesenchymal compartment.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — LKB1 loss removes AMPK-mediated restraint on mTOR (AMPK, mTOR and TSC1-TSC2 mapped), and PIK3CA-driven PI3K signaling further amplifies the growth axis in Peutz-Jeghers polyps and cancers.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D1 axis (mapped, with CDK-inhibitor p21/p27 also mapped) releases E2F1 to drive proliferation in the malignant progression of Peutz-Jeghers-associated tumors.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Loss of E-cadherin during epithelial-mesenchymal transition contributes to the invasion of the gastrointestinal and other carcinomas that complicate Peutz-Jeghers syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) sustains the inflammatory stroma of the hamartomatous polyps and the tumor-promoting microenvironment of Peutz-Jeghers syndrome.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Gut-microbiota-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) provides an inflammatory drive promoting the elevated gastrointestinal-cancer risk of Peutz-Jeghers syndrome.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Loss of the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) is among the cooperating events in the malignant progression of Peutz-Jeghers-associated neoplasia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is upregulated in the polyp-to-carcinoma progression of Peutz-Jeghers syndrome, modulating adhesion and immune evasion.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 mapped) provides a tumor-promoting inflammatory input in the gastrointestinal neoplasia of Peutz-Jeghers syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of the tumors that arise in Peutz-Jeghers syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune surveillance of the gastrointestinal and other neoplasms of Peutz-Jeghers syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — STK11/LKB1 loss in Peutz-Jeghers syndrome dysregulates the AMPK-FOXO axis (AMPK already mapped) that couples energy stress to growth control.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1 and RB1 already mapped) drives the cell-cycle progression of the hamartoma-to-carcinoma sequence in Peutz-Jeghers syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β, integrated with LKB1-AMPK metabolic signaling, modulates the Wnt/β-catenin and survival pathways of the hamartomatous polyps of Peutz-Jeghers syndrome.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis during the polyp-to-cancer progression of Peutz-Jeghers syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory stroma of the hamartomatous polyps of Peutz-Jeghers syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative epithelial signaling of the hamartomatous polyps of Peutz-Jeghers syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic progression of the tumors of Peutz-Jeghers syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is relevant to the cancer risk of the hamartomatous polyps of Peutz-Jeghers syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the inflammatory microenvironment of the polyps and tumors of Peutz-Jeghers syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of Peutz-Jeghers syndrome.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression participates in the epigenetic dysregulation of the tumors of Peutz-Jeghers syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the polyps and cancers of Peutz-Jeghers syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the polyp and tumor microenvironment of Peutz-Jeghers syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the intestinal-tumor immune microenvironment of Peutz-Jeghers syndrome.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Energy-sensing axis: LKB1 loss in Peutz-Jeghers cripples the AMPK energy sensor it activates, and leptin is the adipokine that signals through hypothalamic AMPK to regulate energy balance, extending the metabolic dysregulation beyond the adiponectin link already mapped.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Feminising gonadal tumours: Peutz-Jeghers boys develop large-cell calcifying Sertoli cell tumours that aromatise androgens to estrogen, causing gynaecomastia and disrupting the testosterone-estrogen balance (estrogen already mapped), a distinctive endocrine feature.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Sex-cord secretory marker: the ovarian sex-cord tumours with annular tubules and gonadal stromal tumours of Peutz-Jeghers secrete inhibin/activin-family peptides, so activin signalling marks and drives this characteristic gonadal neoplasia.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Bleeding anaemia: the hamartomatous polyps of Peutz-Jeghers bleed chronically and cause acute haemorrhage with intussusception, producing the iron-deficiency anaemia that lowers haemoglobin and often prompts the endoscopy that reveals the polyposis.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Mucocutaneous pigmentation: the dark lentiginous macules of the lips, buccal mucosa and digits arise from melanocyte activity, which endothelin-1 through EDNRB regulates, underlying the pathognomonic pigmentation of Peutz-Jeghers syndrome.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Gonadal sex-cord tumours: the ovarian sex-cord and testicular Sertoli-cell tumours of Peutz-Jeghers disturb sex-hormone balance (estrogen and testosterone already mapped), so progesterone and the reproductive-hormone axis figure in their endocrine effects.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Obstructive pain: recurrent intussusception and bowel obstruction from the small-intestinal polyps (already mapped) of Peutz-Jeghers cause severe abdominal pain, often requiring opioid analgesia acting at the mu-opioid receptor around surgery.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: chronic mucosal turnover in the hamartomatous polyps and the loss of LKB1-AMPK metabolic control (already mapped) generate oxidative stress, to which xanthine oxidase contributes, adding DNA damage that speeds malignant progression.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive stroma: the anti-inflammatory cytokine IL-10 in the polyp microenvironment dampens anti-tumour immunity (CD8 already mapped), part of the immune tolerance that allows some Peutz-Jeghers polyps and cancers to progress.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the hamartomatous polyp stroma of Peutz-Jeghers syndrome.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Bile acids and diet: dietary fat and the bile acids derived from cholesterol promote the gastrointestinal proliferation and the hamartoma-carcinoma progression, a modifiable dietary influence on the cancer risk of Peutz-Jeghers syndrome.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Polyp vasculature: nitric oxide with VEGF and endothelin-1 (already mapped) regulates the vascular tone and angiogenesis of the vascular hamartomatous polyps of Peutz-Jeghers syndrome, part of their stromal biology.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the microenvironment of the hamartomatous polyps of Peutz-Jeghers syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), links the metabolic state governed by the STK11-AMPK (already mapped) axis to the polyp and cancer biology of Peutz-Jeghers syndrome.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin adds an anaemia of chronic disease to the iron-deficiency (already mapped) anaemia of the chronically bleeding polyps of Peutz-Jeghers syndrome.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Hamartoma stroma: PDGF drives the stromal and smooth-muscle (arborising) mesenchymal component of the hamartomatous Peutz-Jeghers polyps, part of their characteristic architecture.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Malabsorption zinc: the zinc deficiency from the chronic GI blood loss and the malabsorption of the extensive polyposis of Peutz-Jeghers syndrome impairs the healing and immunity.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Micronutrient malabsorption: the calcium and micronutrient malabsorption of the extensive GI polyposis of Peutz-Jeghers syndrome, contributing to the nutritional depletion.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate immune surveillance: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the hamartomatous polyps and the cancer-risk surveillance of Peutz-Jeghers syndrome.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immunosurveillance: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immunosurveillance of the multi-cancer risk of Peutz-Jeghers syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response along the cancer-risk pathways of Peutz-Jeghers syndrome.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflamed hamartomatous-polyp stroma of Peutz-Jeghers syndrome.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the Peutz-Jeghers polyps.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflamed Peutz-Jeghers polyp stroma.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Polyp stroma mast cells: the mast cells of the inflamed hamartomatous polyp stroma contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment of Peutz-Jeghers syndrome.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the inflamed polyp stroma of Peutz-Jeghers syndrome.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen to the T cells (already mapped) shaping the immune surveillance against the malignant transformation of the Peutz-Jeghers polyps.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Mucosal B cells: the B cells of the intestinal mucosa contribute to the humoral and organised immune response within the inflamed stroma of the Peutz-Jeghers polyps.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Polyp complement: the complement C3 activation contributes to the inflammatory dimension of the hamartomatous-polyp stroma of Peutz-Jeghers syndrome.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment into the inflamed stroma of the Peutz-Jeghers polyps.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Intestinal alarmin: TSLP released by the inflamed intestinal epithelium of Peutz-Jeghers polyps activates mast cells and dendritic cells, promoting the type-2 inflammatory stroma and accelerating the STK11-mutant adenoma transition.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Hamartomatous ECM: periostin, a downstream target of the PI3K pathway (mTOR already mapped) dysregulated by STK11 loss, drives the mesenchymal overgrowth and fibroblast expansion of the Peutz-Jeghers polyp stroma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Polyp mast-cell effector: histamine from the abundant stromal mast cells of Peutz-Jeghers polyps promotes angiogenesis and mucous secretion, contributing to the obstructive and intussusception episodes that dominate the clinical course.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Polyp-pain kinin: bradykinin generated in the inflamed stroma of Peutz-Jeghers intestinal polyps activates nociceptive B1/B2 receptors, amplifying visceral pain and the obstructive and intussusception episodes that drive emergency presentations.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: C1-esterase inhibitor restrains the classical complement pathway (C3 and C5aR1 already mapped) within the inflammatory polyp stroma of Peutz-Jeghers syndrome, limiting complement-driven myeloid recruitment and mucosal oedema.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Iron-deficiency anaemia support: erythropoietin addresses the chronic iron-deficiency anaemia (iron and IDA already mapped) driven by repeated haemorrhage from the large vascular Peutz-Jeghers polyps, when endoscopic resection cannot keep pace.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — PJS circadian-oncology: melatonin inhibits the STK11/LKB1 (already mapped) loss-driven mTOR (already mapped) hyperactivation underlying Peutz-Jeghers polyp growth, and melatonin receptor expression on the hamartomatous polyp epithelium modulates polyp cell proliferation.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — PJS enterochromaffin serotonin: serotonin secreted by the abundant enterochromaffin cells in the Peutz-Jeghers gastrointestinal polyps modulates secretory diarrhoea, motility and visceral pain (bradykinin already mapped) in the hamartomatous polyposis syndrome.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — PJS prolactin: prolactin via JAK2/STAT5 signalling activates the mTOR (already mapped) pathway in the Peutz-Jeghers hamartomatous polyp epithelium, and hyperprolactinaemia amplifies the STK11/LKB1 (already mapped) loss-driven epithelial proliferation.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PJS oxytocin: oxytocin modulates intestinal motility and mucosal barrier integrity in the GI tract bearing the Peutz-Jeghers hamartomatous polyps, and oxytocin receptor signalling on enteric neurons (already mapped) intersects STK11/LKB1 (already mapped) epithelial homeostasis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PJS vasopressin: vasopressin via V2R modulates intestinal fluid absorption and mucosal homeostasis in the GI tract harbouring the Peutz-Jeghers hamartomatous polyps, intersecting the STK11/LKB1 (already mapped) and mTOR (already mapped) epithelial proliferation axis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — PJS selenium: selenium-dependent selenoprotein antioxidants quench reactive-oxygen-species arising from STK11/LKB1 (already mapped) loss-driven mTOR (already mapped) hyperactivation in Peutz-Jeghers polyp epithelium, reducing oncogenic transformation risk.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Peutz-Jeghers iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) polyp cascade of Peutz-Jeghers syndrome.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Peutz-Jeghers sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the T-cytotoxic (already mapped) cancer cascade of Peutz-Jeghers syndrome.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Peutz-Jeghers magnesium: magnesium, as LKB1/STK11 (already mapped) kinase cofactor in fibroblasts (already mapped) and macrophages (already mapped), supports tumour-suppression; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of PJS.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Peutz-Jeghers potassium: potassium governs macrophage (already mapped) and mast-cell (already mapped) polyp immune tone; potassium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade suppressing T-cytotoxic (already mapped) function in PJS.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Peutz-Jeghers phosphorus: phosphorus as ATP cofactor in macrophages (already mapped) and fibroblasts (already mapped) sustains LKB1/STK11 (already mapped) signalling; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) polyp-cancer cascade of PJS.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Peutz-Jeghers chloride: chloride in macrophages (already mapped) and mast-cell (already mapped) regulates stromal inflammation; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and suppresses T-cytotoxic (already mapped) surveillance in PJS.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Peutz-Jeghers carbon: carbon as backbone of LKB1/STK11 (already mapped) and NF-κB (already mapped) proteins in epithelial cells sustains tumour-suppressive signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) polyp-cancer cascade of PJS.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Peutz-Jeghers hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and fibroblasts (already mapped), supports LKB1/STK11 (already mapped) kinase activity; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PJS.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Peutz-Jeghers nitrogen: nitrogen in amino-acid scaffold of LKB1/STK11 (already mapped) and mTOR (already mapped) proteins in polyp epithelial cells sustains signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of PJS.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hearle-2006-pjs-cancer]: Hearle N, Schumacher V, Menko FH, et al. Frequency and spectrum of cancers in the Peutz-Jeghers syndrome. *Clin Cancer Res.* 2006;12(10):3209-3215. [doi:10.1158/1078-0432.CCR-06-0083](https://doi.org/10.1158/1078-0432.CCR-06-0083) · [PubMed 16707622](https://pubmed.ncbi.nlm.nih.gov/16707622/)
[^skoulidis-2018-stk11-nsclc]: Skoulidis F, Goldberg ME, Greenawalt DM, et al. STK11/LKB1 mutations and PD-1 inhibitor resistance in KRAS-mutant lung adenocarcinoma. *Cancer Cell.* 2018;34(3):412-424. [doi:10.1016/j.ccell.2018.08.013](https://doi.org/10.1016/j.ccell.2018.08.013) · [PubMed 30174241](https://pubmed.ncbi.nlm.nih.gov/30174241/)
