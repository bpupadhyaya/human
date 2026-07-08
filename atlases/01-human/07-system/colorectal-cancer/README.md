---
schema: human-scale-entry/v1
id: colorectal-cancer
name: Colorectal Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Second leading cause of cancer deaths; driven by APC/Wnt loss → adenoma-carcinoma sequence, then KRAS, SMAD4, and TP53 mutations. EGFR blockade (cetuximab) for RAS-wild-type metastatic disease; KRAS/BRAF V600E inhibitors and pembrolizumab (MSI-H) are molecularly targeted."
aliases: ["CRC", "colon cancer", "rectal cancer", "colorectal carcinoma", "adenocarcinoma of colon", "mCRC", "Lynch syndrome", "FAP"]
sources:
  - id: siegel-2024-crc-statistics
    type: peer-reviewed
    cite: "Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. CA Cancer J Clin. 2024;74(1):12-49."
    doi: "10.3322/caac.21820"
    pmid: "38230766"
    url: "https://doi.org/10.3322/caac.21820"
  - id: van-cutsem-2011-crystal-cetuximab
    type: peer-reviewed
    cite: "Van Cutsem E, Köhne CH, Láng I, et al. Cetuximab plus irinotecan, fluorouracil, and leucovorin as first-line treatment for metastatic colorectal cancer: updated analysis of overall survival according to tumor KRAS and BRAF mutation status. J Clin Oncol. 2011;29(15):2011-2019."
    doi: "10.1200/JCO.2010.33.5091"
    pmid: "21502544"
    url: "https://doi.org/10.1200/JCO.2010.33.5091"
  - id: kopetz-2019-beacon-crc
    type: peer-reviewed
    cite: "Kopetz S, Grothey A, Yaeger R, et al. Encorafenib, binimetinib, and cetuximab in BRAF V600E-mutated colorectal cancer. N Engl J Med. 2019;381(17):1632-1643."
    doi: "10.1056/NEJMoa1908075"
    pmid: "31566309"
    url: "https://doi.org/10.1056/NEJMoa1908075"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS mutations (~40% of CRC) are acquired in the adenoma-carcinoma sequence; KRAS G12V/G12D-mutant CRC is resistant to EGFR inhibitors (cetuximab, panitumumab); KRAS G12C-mutant CRC → adagrasib + cetuximab (KRYSTAL-10, ORR 34%) — first targeted therapy for CRC with KRAS."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "APC loss is the founding mutation in >80% of sporadic CRC; APC → destruction complex collapse → beta-catenin nuclear accumulation → MYC, cyclin D1 → hyperproliferation; germline APC mutation causes FAP → thousands of colonic polyps → obligate CRC."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR is overexpressed in >80% of CRC; cetuximab and panitumumab improve OS in RAS-wild-type metastatic CRC (CRYSTAL: cetuximab + FOLFIRI vs. FOLFIRI, PFS 9.9 vs. 8.4 months in KRAS-wt); RAS/RAF-wild-type biomarker required for EGFR inhibitor benefit."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E mutations (~8-10% of CRC) confer poor prognosis and EGFR inhibitor resistance; BEACON CRC: encorafenib + cetuximab → OS 9.3 vs. 5.9 months vs. control in BRAF V600E mCRC; BRAF V600E CRC is enriched in MSI-H tumors and right-sided cancers."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "FN-integrin α5β1/αvβ3 signaling drives EMT in CRC → vimentin, N-cadherin, MMP production → invasion and liver metastasis; EDB-FN is overexpressed in CRC stroma; tumor FN correlates with lymph node metastasis and worse prognosis in stage II-III CRC."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Most colorectal cancers arise in the large intestine via the adenoma-carcinoma sequence, so colonoscopy with polypectomy is preventive; right-sided tumors bleed occultly (→ anemia) while left-sided ones obstruct, and rectal cancer is resected by total mesorectal excision."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Lynch syndrome (germline MMR loss) causes ~3% of colorectal cancer, producing dMMR/MSI-H tumors that are hypermutated and exquisitely sensitive to PD-1 blockade — pembrolizumab is now first-line for MSI-H metastatic CRC; universal MMR/MSI testing of all CRC is recommended."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 loss (~75% of CRC) is the rate-limiting step that converts an advanced adenoma into invasive carcinoma: 17p loss plus TP53 mutation removes the DNA-damage checkpoint, unleashing the chromosomal instability that lets cells breach the muscularis mucosae."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "Colorectal and prostate cancers are two of the commonest adult solid tumours; both have hereditary drivers—Lynch raises both, BRCA2 raises prostate—and microsatellite-unstable CRC and DNA-repair-deficient prostate cancer both respond to checkpoint or PARP-based therapy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is the dominant site of colorectal metastasis via portal venous drainage: ~50% of CRC patients develop liver mets, and resection or ablation of oligometastatic liver disease can be curative; this portal route makes CRC liver-metastasis management central to oncology."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Familial adenomatous polyposis, from germline APC mutation, carpets the colon with hundreds-to-thousands of adenomas and guarantees colorectal cancer by mid-adulthood without prophylactic colectomy; APC loss is also the founding event in >80% of sporadic CRC."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "MUTYH-associated polyposis is a recessive hereditary cause of colorectal cancer: biallelic MUTYH loss fails to repair oxidative DNA damage, producing G:C→T:A mutations and multiple adenomas, so a FAP-like polyposis with negative APC testing prompts MUTYH analysis."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Long-standing inflammatory bowel disease drives colitis-associated colorectal cancer: chronic inflammation accelerates the dysplasia-carcinoma sequence (often p53 early, APC late—reversed from sporadic CRC), so colitis warrants surveillance colonoscopy."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The MSI-high subset of colorectal cancer is exquisitely immunotherapy-responsive: mismatch-repair deficiency generates abundant neoantigens that draw cytotoxic CD8+ T cells, so anti-PD-1 (pembrolizumab) works in MSI-high tumors while microsatellite-stable CRC remains resistant."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome shapes colorectal cancer risk: dysbiosis enriches pro-carcinogenic bacteria (e.g. Fusobacterium) that inflame mucosa and damage DNA, while a healthy fiber-fermenting flora is protective—linking the microbial ecosystem to tumorigenesis."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity is a major modifiable colorectal cancer risk factor: visceral adiposity drives insulin/IGF-1 signaling and chronic inflammation that promote colonic tumorigenesis, so rising early-onset CRC parallels obesity—weight and diet are key prevention levers."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is central to rectal (not colon) cancer: neoadjuvant chemoradiation with photon beams shrinks locally advanced rectal tumors before surgery, sometimes enough for watch-and-wait—colon cancer, by contrast, is treated with surgery and chemotherapy."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "APC loss is the gatekeeper mutation that starts colorectal cancer: inactivating APC unleashes Wnt/beta-catenin to form the first adenoma, so it initiates the adenoma-carcinoma sequence—mutated in FAP and in most sporadic colorectal cancers."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: targets
    note: "Colorectal cancer arises stepwise from the intestinal epithelium: normal crypt cells acquire APC, then KRAS, then p53 hits, progressing through adenoma to carcinoma—the textbook adenoma-carcinoma sequence that makes screening colonoscopy preventive."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 is the checkpoint that MSI-high colorectal tumors exploit to evade attack: blocking it produced the first tissue-agnostic FDA approval (pembrolizumab for any MSI-high cancer), so dMMR/MSI status is now tested at diagnosis to guide immunotherapy."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes raises colorectal cancer risk: high insulin and IGF-1 from insulin resistance promote colonocyte proliferation, and shared risks like obesity and inactivity compound it—so metabolic health is part of colorectal cancer prevention."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "After the liver, the lung is colorectal cancer's next metastatic stop: tumor cells reach it via the systemic circulation, and isolated lung metastases are sometimes surgically resected for cure—so chest imaging is routine in staging and follow-up."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "A subset of colorectal cancers are HER2-amplified: like in breast and gastric cancer, this drives growth and predicts resistance to anti-EGFR drugs, but responds to HER2-targeted combinations—so HER2 testing now guides therapy in metastatic disease."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Right-sided colorectal cancer often presents as iron-deficiency anemia: a slow-bleeding tumor depletes iron long before obstruction, so unexplained iron-deficiency anemia in an adult mandates colonoscopy to exclude colon cancer."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D and calcium intake are linked to colorectal risk: higher levels associate with lower incidence, and vitamin D's effects on colonocyte growth make it a studied (if unproven) chemopreventive alongside fiber and aspirin."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts drive colorectal progression: they remodel the tumor stroma, supply growth and survival signals, and promote chemoresistance and metastasis—a major reason the desmoplastic, fibroblast-rich CMS4 subtype carries a worse prognosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Colorectal cancer is treated by starving its vessels of VEGF: the tumor secretes VEGF to build a blood supply, so anti-VEGF bevacizumab is a mainstay added to chemotherapy in metastatic colorectal cancer."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Colorectal cancer turns aggressive when it loses SMAD4: this late hit in the adenoma-carcinoma sequence disables TGF-β's growth restraint, driving invasion and metastasis and predicting a worse prognosis and poorer chemo response."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Most colorectal cancers are immune-cold, walled off by regulatory T cells: unlike MSI-high tumors, microsatellite-stable CRC has few neoantigens and Treg-rich stroma, which is why checkpoint immunotherapy works in only a minority."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Dietary calcium helps guard against colorectal cancer: it binds bile acids and fatty acids in the gut and signals colon cells to differentiate, so adequate calcium is one of the better-supported dietary protections against the disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages shape colorectal cancer: depending on their polarization they can promote or restrain the tumor, and a macrophage-rich, suppressive stroma helps the common microsatellite-stable cancers evade immunity."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Colorectal cancer can reach the brain late: though it spreads first to liver and lung, advanced disease occasionally seeds brain metastases, a sign of widespread disease that shifts care toward palliative and systemic treatment."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency is often the first clue to colorectal cancer: right-sided tumors bleed slowly into the stool, so unexplained iron-deficiency anemia in an older adult is a red flag that should prompt a colonoscopy."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Colorectal tumors build their own blood supply: VEGF recruits endothelial cells to sprout new vessels, and blocking this with bevacizumab is a mainstay of treating metastatic disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "A dense fibrotic stroma walls off colorectal cancer: the tumor provokes desmoplastic scar tissue that shields it from immune cells and drugs, part of why microsatellite-stable disease resists immunotherapy."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads colorectal cancer's grade in its glands: well-differentiated tumor cells keep orderly microvilli and tight junctions making lumina, while poorly differentiated ones lose this architecture — ultrastructure that tracks how aggressive the cancer is."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Colorectal cancer pushes platelets up: a paraneoplastic thrombocytosis appears in many patients and signals worse prognosis, while the platelets themselves help circulating tumor cells survive and seed the liver."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Late colorectal cancer can reach the bone: after seeding the liver and lungs, advanced disease occasionally spreads to the marrow-filled skeleton, an uncommon but ominous site marking widespread metastasis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "FOLFOX chemotherapy bites the nerves: oxaliplatin, a backbone of colorectal cancer treatment, injures peripheral sensory neurons, causing a distinctive cold-triggered tingling and numbness that can force dose reductions and outlast therapy."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Targeted therapy wastes magnesium: the anti-EGFR antibodies cetuximab and panitumumab, used in RAS-wild-type colorectal cancer, block EGFR in the kidney tubule, so magnesium leaks into the urine and must be monitored and replaced."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin reports on EGFR-blocking drugs: cetuximab and panitumumab provoke an acneiform facial rash, and its severity actually tracks with how well the colorectal tumor is responding, making the rash a visible biomarker."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies monitor and steer colorectal cancer: the CEA blood marker, read by immunoassay, tracks recurrence, while mismatch-repair (MMR) stains flag the MSI-high tumors that respond to checkpoint immunotherapy and prompt Lynch testing."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The FOLFOX backbone empties the marrow: the oxaliplatin-and-fluorouracil chemotherapy is myelosuppressive, dropping neutrophil counts between cycles so that febrile neutropenia is a recurring hazard of colorectal-cancer treatment."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Fiber guards the colon: gut bacteria ferment dietary fiber into butyrate that nourishes colonocytes and curbs malignant change, so a fiber-rich diet lowers colorectal-cancer risk while red and processed meat raise it."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Colorectal cancer thickens the blood: tumor procoagulants, surgery, and chemotherapy combine to make deep-vein thrombosis and pulmonary embolism common, so clot prophylaxis is routine around treatment of this cancer."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The 5-FU backbone can stun the heart: fluoropyrimidine chemotherapy (5-FU, capecitabine) provokes coronary vasospasm and direct cardiomyocyte injury, causing chest pain and even infarction that interrupts colorectal cancer treatment."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA links the tumor to aspirin: mutations in this gene activate PI3K signaling in a subset of colorectal cancers, and the chemopreventive benefit of aspirin appears concentrated in these PIK3CA-mutant tumors."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "The Wnt switch is thrown at the gene that APC guards: when APC fails, β-catenin (CTNNB1) escapes degradation, enters the nucleus and turns on growth genes — the molecular heart of the adenoma-carcinoma sequence, and the rare driver when CTNNB1 itself is mutated."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "A gut bacterium can be a carcinogen: strains of E. coli carrying the pks island make colibactin, a genotoxin that scars colon-cell DNA with a signature mutation pattern, directly implicating the microbiome in colorectal tumor initiation."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The liver is its favored landing site: colorectal cells seeding the portal blood lodge among hepatocytes to grow liver metastases, the disease's commonest spread and the reason a resectable liver lesion can still mean cure."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation drives the colitis-to-cancer path: NF-κB activation in the chronically inflamed bowel links inflammatory bowel disease to colorectal cancer, switching on the survival and proliferation signals that turn inflamed mucosa malignant."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 feeds the tumor through STAT3: in inflammation-associated colorectal cancer, IL-6 from the microenvironment activates STAT3 in epithelial cells to push their proliferation and survival, tightly coupled to the NF-κB inflammatory program."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "An obstructing or perforating tumor can seed infection: colorectal cancers that block or breach the bowel wall spill gut flora into the abdomen and bloodstream, and chemotherapy neutropenia adds its own route to sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Beyond bleeding, inflammation blunts the marrow: alongside the iron-deficiency anemia from chronic blood loss, the tumor's IL-6-driven inflammation raises hepcidin and suppresses erythropoiesis, adding an anemia-of-chronic-disease component."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its mainstay chemo can injure the heart: 5-fluorouracil and capecitabine cause coronary vasospasm and a cardiotoxicity that can precipitate ischemia and cardiac dysfunction during colorectal cancer treatment."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Treatment and obstruction both threaten the kidney: the bevacizumab used in metastatic colorectal cancer causes proteinuria and renal injury, while pelvic tumor can obstruct the ureters, together risking chronic kidney disease."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its oxaliplatin leaves nerves burning: the platinum drug in FOLFOX, a backbone of colorectal-cancer therapy, causes a dose-dependent peripheral neuropathy with cold-triggered and chronic neuropathic pain that can persist long after treatment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its chemotherapy opens the lung to mold: the neutropenia from colorectal-cancer regimens can let inhaled Aspergillus invade as pulmonary aspergillosis, especially in heavily pretreated or metastatic patients."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Diagnosis and a stoma weigh on mood: the cancer diagnosis, ostomy and altered bowel function and prolonged chemotherapy of colorectal cancer contribute to substantial depression and impaired quality of life."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It grows in and obstructs the gut: colorectal cancer arises from the colonic epithelium and can occlude the bowel lumen, causing obstruction, altered bowel habit and the need for resection or a stoma."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Colectomy hinges on a healing anastomosis: bowel resection for colorectal cancer joins two ends of gut, and anastomotic leak — failure of that wound to heal — is a feared, life-threatening complication."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Surveillance and stoma life breed worry: the recurrence monitoring, CEA checks and altered bowel function or ostomy of colorectal cancer foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "After the liver, it climbs to the lungs: pulmonary metastases are the second commonest distant site in colorectal cancer, and resectable lung deposits are sometimes removed with curative intent."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The nodes decide its fate: regional lymph-node involvement is the dominant prognostic factor in colorectal cancer, defining stage III disease and the need for adjuvant chemotherapy after surgery."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Mismatch-repair failure makes it visible: MSI-high colorectal tumours carry many neoantigens and respond strongly to checkpoint-inhibitor immunotherapy, unlike the common microsatellite-stable cancers."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its chemotherapy can spasm the coronaries: 5-fluorouracil and capecitabine cause coronary vasospasm and cardiotoxicity, and bevacizumab raises blood pressure and thrombosis risk."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its targeted drugs erupt on the skin: the EGFR inhibitor cetuximab causes a characteristic acneiform rash, and capecitabine causes hand-foot syndrome."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its drugs and spread reach the nerves: oxaliplatin causes a cold-triggered peripheral neuropathy, and advanced rectal cancer can metastasise to the brain."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It is matched to tumour genotype: anti-EGFR antibodies (cetuximab) for RAS-wild-type tumours, anti-VEGF bevacizumab and checkpoint immunotherapy for MSI-high disease guide modern colorectal cancer treatment."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Tumour and drugs reach the kidney: a bulky rectal or pelvic tumour can obstruct the ureters, and oxaliplatin-based chemotherapy carries nephrotoxic risk."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pelvic surgery and spread affect it: rectal cancer surgery risks injury to nerves controlling sexual function, and colorectal cancer can metastasise to the ovaries as Krukenberg-type deposits."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "FOLFOX is the backbone: 5-fluorouracil with oxaliplatin or irinotecan is the cytotoxic core of colorectal cancer treatment, given adjuvantly after surgery for node-positive disease and as first-line therapy for metastatic disease."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "MSI status splits the response: the ~15% of colorectal cancers that are mismatch-repair-deficient (MSI-high) respond dramatically to PD-1 blockade like pembrolizumab, while the microsatellite-stable majority remain immunologically cold and resistant."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It seeds the liver first: draining via the portal vein, colorectal cancer metastasises preferentially to the hepatic lobules, and these liver metastases — uniquely among cancers — are often resected or ablated for cure."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Why some colorectal cancers invite immunotherapy: mismatch-repair-deficient (MSI-high) tumours accumulate neoantigens and dense lymphocytic infiltrates with tertiary lymphoid structures, the immune richness behind their response to checkpoint blockade."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "A hamartomatous route to colorectal cancer: SMAD4/BMPR1A juvenile polyposis studs the colon with hamartomatous polyps that raise lifetime colorectal-cancer risk, a hereditary syndrome beyond the adenomatous FAP and Lynch."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Another hamartomatous predisposition: STK11/LKB1 Peutz-Jeghers syndrome carries a high lifetime risk of colorectal and other GI cancers from its hamartomatous polyps, joining the hereditary colorectal-cancer syndromes."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Lung as a metastatic site: colorectal cancer—especially rectal tumours draining systemically—seeds the lungs after the liver, depositing nodules in the alveolar parenchyma that pulmonary metastasectomy can sometimes cure."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Lynch's other hallmark tumour: the mismatch-repair deficiency that drives hereditary colorectal cancer drives endometrial cancer just as strongly, so the two define the Lynch syndrome spectrum and share MSI-targeted immunotherapy."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Chemotherapy's cardiac risk: 5-fluorouracil, the backbone of colorectal cancer therapy, can provoke coronary vasospasm and ischaemia of the myocardium, an under-recognised cardiotoxicity that occasionally causes infarction."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Same mutation, different drug response: BRAF V600E drives a colorectal cancer subset and melanoma, yet BRAF inhibitors alone fail in colon cancer because EGFR feedback reactivates the pathway—so combinations with anti-EGFR are needed."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Shared GI adenocarcinoma biology: colorectal and gastric cancers overlap in HER2-targeted therapy, microsatellite-instability immunotherapy and Lynch-syndrome predisposition, two adenocarcinomas of the gut tube."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Peritoneal and Lynch links: colorectal cancer can metastasise to the ovary (Krukenberg-type) and seed the peritoneum like ovarian cancer, while Lynch syndrome predisposes to both tumours."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 chemoprevention: COX-2-derived prostaglandins drive colorectal carcinogenesis, and aspirin/NSAID inhibition of this pathway reduces colorectal cancer risk."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Wnt's oncogene: APC loss and constitutive Wnt signalling activate MYC, a central driver of proliferation in colorectal cancer."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Adenoma-to-carcinoma switch: loss of TGF-β/SMAD4 tumour-suppressor signalling drives the progression of colorectal adenomas to invasive, metastatic carcinoma."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: PIK3CA mutation activates AKT in colorectal cancer, driving growth and survival and contributing to resistance to anti-EGFR therapy."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: Wnt-driven cyclin D1 with CDK4/6 propels colorectal cancer cells through the G1 checkpoint along the adenoma-carcinoma sequence."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in hypoxic colorectal tumours drives the VEGF angiogenesis and invasive, metastatic phenotype linked to poor prognosis."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Mismatch repair and immunotherapy: MLH1 loss (germline in Lynch syndrome, or sporadic via promoter hypermethylation) creates the microsatellite-instable, hypermutated CRC subtype that responds to checkpoint inhibitors like pembrolizumab."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Hepatic metastasis: CXCR4 on colorectal-cancer cells follows CXCL12 gradients toward the liver via the portal circulation, helping explain why the liver is the dominant site of CRC metastatic spread."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation-driven cancer: IL-6 signalling through STAT3 links chronic colonic inflammation to carcinogenesis, the basis of the elevated colorectal-cancer risk in inflammatory bowel disease (colitis-associated cancer)."
  - target: 01-human/03-molecular/msh2
    relation: connects-to
    note: "Lynch-syndrome repair: germline MSH2 mutations, alongside MLH1, cause Lynch syndrome and the microsatellite-instable colorectal cancers, the mismatch-repair defect that both drives hereditary risk and predicts response to checkpoint blockade."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "MSI immunogenicity: mismatch-repair-deficient colorectal cancers accumulate mutations and cytosolic DNA that engage cGAS-STING, the innate-immune basis for the striking sensitivity of MSI-high tumours to PD-1 blockade, unlike the immune-cold MSS majority."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Myeloid microenvironment: CCL2 recruits tumour-associated macrophages into colorectal cancer, building the immunosuppressive myeloid niche that helps explain why the microsatellite-stable majority resist immunotherapy."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K resistance: PTEN loss activates the PI3K-AKT axis (PIK3CA and AKT already mapped) in colorectal cancer and is associated with resistance to anti-EGFR antibodies in KRAS-wild-type tumours."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Stem-cell maintenance: NOTCH signalling cooperates with Wnt in the intestinal crypt stem-cell compartment, and its dysregulation sustains the cancer-stem-cell population driving colorectal tumour growth and relapse."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: 5-fluorouracil and oxaliplatin kill colorectal cancer cells through caspase-3-mediated apoptosis, and defects in this death programme underlie the chemoresistance that limits cure in metastatic disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK driver: EGFR, KRAS and BRAF (all mapped) signal through the MAPK-ERK cascade in colorectal cancer, the axis whose RAS-mutation status determines response to anti-EGFR therapy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA, AKT and PTEN already mapped) that cooperates with the adenoma-carcinoma drivers in colorectal cancer."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle release: β-catenin-driven cyclin-D1 (mapped) and CDK4/6 release E2F1 to drive the proliferation initiated by APC loss in the colorectal adenoma-carcinoma sequence."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbiota-driven carcinogenesis: gut-microbiota TLR-MyD88-NF-κB signalling (NF-κB already mapped), exemplified by Fusobacterium nucleatum, promotes inflammation-associated colorectal carcinogenesis and links inflammatory bowel disease to cancer risk."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory microenvironment: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped) sustains the tumour-promoting inflammatory microenvironment of colorectal cancer."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: dysregulation of the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) contributes to the cell-cycle progression of colorectal cancer."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes immune evasion and the liver-metastatic colonisation that drives mortality in colorectal cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling governs the antitumour immune response of colorectal cancer, particularly the immunotherapy-responsive mismatch-repair-deficient subtype."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression silences tumour-suppressor genes and contributes to the epigenetic dysregulation of colorectal cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven cyclin-D1-RB1 cell-cycle entry (cyclin-D1 and RB1 already mapped) sustains the proliferation of colorectal cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-mediated FOXO inactivation (PI3K-AKT already mapped) removes a pro-apoptotic brake, favoring survival in colorectal cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunogenic mismatch-repair-deficient colorectal cancer must evade."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the β-catenin destruction-complex activity (APC/CTNNB1/Wnt already mapped) whose disruption drives colorectal cancer."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in colorectal cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from myeloid cells shape the inflammatory, tumor-promoting microenvironment of colorectal cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of EGFR (EGFR already mapped) drives the invasion and metastasis of colorectal cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the CpG-island-methylator-phenotype epigenetic dysregulation of colorectal cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of colorectal cancer cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of colorectal cancer, a candidate metformin target."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of colorectal cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of colorectal cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of colorectal cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of colorectal cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment (colitis-associated) of colorectal cancer."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "MSI immunotherapy: mismatch-repair-deficient, microsatellite-unstable colorectal cancers (MLH1/MSH2 already mapped) generate abundant neoantigens presented on MHC, making this subset uniquely responsive to checkpoint inhibitors while proficient tumours remain cold."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron-deficiency presentation: right-sided colorectal cancers bleed occultly, and the resulting iron-deficiency anaemia with low transferrin saturation is a classic presenting sign that should prompt colonoscopy in older adults."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Metabolic risk: obesity and insulin resistance raise circulating IGF-1, a mitogen for colonic epithelium, part of the mechanism linking metabolic syndrome and Western diet to increased colorectal cancer risk."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "MSI immunotherapy: the mismatch-repair-deficient, microsatellite-unstable colorectal cancers (MLH1/MSH2 already mapped) are neoantigen-rich and respond to checkpoint blockade (PD-1 already mapped), and IL-2-driven T-cell expansion underlies this immune sensitivity."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Iron-deficiency anaemia: right-sided colorectal cancers bleed occultly (transferrin already mapped), and the iron-deficiency anaemia lowering haemoglobin is a classic presenting sign that should prompt colonoscopy in older adults."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Fluoropyrimidine cardiotoxicity: 5-fluorouracil and capecitabine, backbone chemotherapy for colorectal cancer, can provoke coronary vasospasm and myocardial injury, and troponin elevation helps detect this recognised cardiotoxicity."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Diet and bile acids: a Western diet high in fat raises the cholesterol-derived bile acids that, deconjugated by gut bacteria (microbiome already mapped), promote colorectal carcinogenesis, part of the dietary risk of colorectal cancer."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (CD8 and PD-1 already mapped), the immune evasion that is more readily overcome in the microsatellite-unstable (MLH1 already mapped) tumours."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: chronic colonic inflammation and the high epithelial turnover generate oxidative stress, to which xanthine oxidase contributes, and this oxidative DNA damage speeds the adenoma-carcinoma sequence of colorectal cancer."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment of the microsatellite-stable colorectal cancers that resist checkpoint blockade."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and proliferation: leptin from adipose tissue promotes the proliferation of the colonic epithelium, part of the mechanism by which obesity raises the risk of colorectal cancer alongside the insulin-IGF-1 axis (IGF-1 already mapped)."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Hyperinsulinaemia: the hyperinsulinaemia of obesity and type 2 diabetes drives colorectal carcinogenesis through insulin and the IGF-1 axis (already mapped), a modifiable metabolic risk factor for the cancer."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of colorectal cancer."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Anti-proliferative adipokine: adiponectin falls with obesity (leptin and insulin already mapped), and this loss removes a brake on the colonic epithelial proliferation, part of the obesity link to colorectal cancer."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine inflammation: resistin, with leptin and adiponectin (already mapped), is a pro-inflammatory adipokine of obesity that promotes the colonic proliferation and inflammation implicated in colorectal-cancer risk."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron-deficiency anaemia: the chronic occult bleeding of colorectal cancer causes the iron-deficiency anaemia (transferrin and haemoglobin already mapped), a classic presentation that prompts the diagnosis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "MSI immunogenicity: the cGAS-STING (already mapped) sensing of the genomic instability of the MSI-high (MLH1 and MSH2 already mapped) colorectal cancer drives the type-I interferon behind the checkpoint (PD-1 already mapped) response."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Chemoprevention selenium: the antioxidant selenoprotein status is inversely associated with the colorectal-cancer risk, part of the micronutrient chemoprevention of the colonic epithelium."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of the MSI-high colorectal cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the colorectal-cancer immune microenvironment."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance of the colorectal cancer, complementing the T-cell (already mapped) checkpoint immunotherapy of the MSI-high tumours."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of colorectal cancer (the tumour-associated tissue eosinophilia is prognostic)."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of colorectal cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the colorectal-cancer microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of colorectal cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts the checkpoint (PD-1 already mapped) response of the MSI-high colorectal cancer."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the tumour-promoting-versus-protective immune balance of colorectal cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tumour complement: the complement C3 activation contributes to the inflammatory and immunosuppressive dimension of the colorectal-cancer microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment into the colorectal-cancer microenvironment."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the tumour antigen to the CD8 (already mapped) T cells, shaping the checkpoint (PD-1 already mapped) response of the MSI-high colorectal cancer."
---

# Colorectal Cancer

## Overview

**Colorectal cancer (CRC)** is the **third most common cancer** and **second leading cause of cancer-related death** worldwide, with approximately 1.9 million new diagnoses and 930,000 deaths globally in 2022 [^siegel-2024-crc-statistics]. In the United States, CRC is the second leading cause of cancer death among men and women combined, accounting for ~53,000 deaths in 2024. The lifetime risk is ~1 in 23 for men and 1 in 26 for women.

**CRC is highly preventable** — colonoscopy with polypectomy prevents cancer by removing adenomatous precursor lesions; population-based screening programs have led to ~25-30% declines in CRC mortality in countries with high screening uptake. Yet incidence is paradoxically rising in adults under 50 ("early-onset CRC"), a trend whose causes are under active investigation (altered gut microbiome, dietary changes, obesity).

**Hereditary CRC syndromes:**
- **Lynch syndrome (Hereditary Non-Polyposis CRC, HNPCC, ~3% of all CRC):** Autosomal dominant; germline mutations in mismatch repair (MMR) genes — MLH1, MSH2, MSH6, PMS2, EPCAM; 40-70% lifetime CRC risk; also endometrial (40-60%), ovarian, gastric, urinary tract cancers; Amsterdam II criteria / revised Bethesda guidelines for identification; universal MMR IHC/MSI testing of all CRC tumors recommended; Lynch CRCs: MSI-H (microsatellite instability-high) → high TMB → highly immunogenic → respond dramatically to pembrolizumab
- **Familial adenomatous polyposis (FAP, ~1% of CRC):** Germline APC mutations (typically truncating) → hundreds to thousands of colorectal polyps → near-obligate CRC by age 40 without colectomy; attenuated FAP (AFAP): APC mutations at 5' end → fewer polyps, later onset; MUTYH-associated polyposis (MAP): biallelic germline MUTYH mutations → attenuated polyposis
- **Serrated polyposis syndrome (SPS):** Multiple serrated polyps (sessile serrated lesions) → BRAF-mutant, CpG island methylation phenotype (CIMP) tumors; MSI-H via MLH1 promoter methylation (epigenetic — not hereditary)

**Molecular classification:**
- **Consensus Molecular Subtypes (CMS 1-4):**
  - **CMS1 (MSI immune, ~14%):** MSI-H, BRAF mutation, high TIL infiltration, immune activation; best prognosis after stage adjustment; pembrolizumab highly active
  - **CMS2 (canonical, ~37%):** Microsatellite stable (MSS), WNT/MYC activation, EGFR amplification; standard FOLFOX + anti-EGFR (RAS-wt)
  - **CMS3 (metabolic, ~13%):** KRAS/NRAS mutations, metabolic dysregulation, mixed phenotype; worse response to anti-EGFR
  - **CMS4 (mesenchymal, ~23%):** TGF-beta activation, stromal invasion, worst prognosis; resistance to most therapies; stromal/mesenchymal gene signature
  - ~13% mixed/intermediate → no single CMS assignment

## Structure

### Adenoma-carcinoma sequence (Fearon-Vogelstein model)

The step-wise genetic progression from normal epithelium to carcinoma in CRC was first systematically described by Fearon and Vogelstein (1990) and remains the paradigm for solid tumor progression:

**Stage 0 → Normal epithelium:**
- Normal crypt stem cells (ASCL2+, LGR5+ at crypt base); Wnt gradient (high at base → low at tip) → stem cell proliferation vs. differentiation

**Stage 1 → Early adenoma (polyp initiation):**
- **APC loss (first hit):** APC biallelic inactivation (mutation/deletion) → destruction complex (APC-AXIN-CK1-GSK3beta) collapses → beta-catenin accumulates → nuclear translocation → MYC, CCND1, AXIN2, LGR5 → crypt-like hyperproliferation → tubular adenoma formation; ~5-10 years for normal epithelium → small adenoma

**Stage 2 → Intermediate adenoma (early progression):**
- **KRAS activation (second hit, ~40%):** G12D/G12V/G12C mutations → RAS GTP-locked → RAF-MEK-ERK constitutive → proliferation amplification; adenoma grows from <1 cm → 1-2 cm; KRAS mutation found in ~40% of intermediate adenomas

**Stage 3 → Advanced adenoma (dysplasia):**
- **SMAD4/TGF-beta loss (~30%):** Biallelic SMAD4 (DPC4) loss → loss of TGF-beta growth inhibition → villous adenoma with high-grade dysplasia; also TGFBR2 mutations (especially in MSI-H tumors where repeat sequences in TGFBR2 are mutation hotspots)
- **PIK3CA mutations (~15%):** Activate PI3K-AKT → enhanced survival
- **Chromosome 18q loss (DCC, SMAD2, SMAD4):** Deleted in colorectal cancer (DCC) gene region; 18q LOH predicts poor prognosis

**Stage 4 → Invasive carcinoma:**
- **TP53 mutation/loss (~75%):** CIN (chromosomal instability) → 17p loss → TP53 mutation → loss of DNA damage checkpoint → rapid genomic instability → invasion through muscularis mucosae → T1 cancer; TP53 mutation is the rate-limiting step from adenoma to carcinoma
- **Additional alterations:** SMAD4 (metastatic phenotype), PI3K amplification, BRAF V600E (serrated pathway), MLH1 epigenetic silencing (MSI-H serrated carcinoma)

**Serrated pathway (alternative to adenoma-carcinoma):**
- Normal epithelium → hyperplastic polyp → sessile serrated lesion (SSL, formerly SSA/P) → SSL with dysplasia → CRC; BRAF V600E + CpG island methylator phenotype (CIMP) + MLH1 promoter methylation → MSI-H carcinoma; accounts for ~15-20% of sporadic CRC; biologically and therapeutically distinct from conventional adenoma pathway

## Function

### Clinical presentation

**Symptoms (variable by location):**
- **Right colon (cecum, ascending):** Occult blood loss → iron deficiency anemia (hypochromic microcytic anemia); mass palpable in right lower quadrant; often presents late due to paucity of obstructive symptoms (large lumen)
- **Left colon and sigmoid:** Pencil-thin stools, change in bowel habits, bright rectal bleeding; obstructive symptoms (left colon has smaller lumen and formed stool → higher obstruction risk)
- **Rectal cancer:** Rectal bleeding (bright red), tenesmus (incomplete evacuation feeling), urgency, mucus; distal rectal tumors may be palpable by digital exam
- **Metastatic:** Liver metastases → hepatomegaly, right upper quadrant pain, elevated LFTs; lung metastases → cough, hemoptysis; peritoneal carcinomatosis → ascites, abdominal distension; bone metastases (less common)

**Colorectal cancer screening:**
- **Colonoscopy:** 10-year interval if normal; removes polyps at time of detection; 90-95% sensitive for adenomas >10 mm; gold standard
- **FIT (fecal immunochemical test, fecal occult blood):** Annual stool test; detects hemoglobin in stool → low-cost, high-compliance; used as primary screen in many European and Asian national programs; positive FIT → colonoscopy
- **CT colonography (virtual colonoscopy):** 5-year interval; comparable sensitivity to optical colonoscopy for polyps >6 mm; cannot do polypectomy → requires colonoscopy for positive findings
- **Multi-target stool DNA test (Cologuard):** Detects abnormal DNA (KRAS mutations, NDRG4/BMP3 methylation, hemoglobin) → 3-year interval; higher false-positive rate than FIT; used in average-risk patients
- Starting age: USPSTF recommends starting at 45 (previously 50) given rising early-onset CRC incidence

## Pathology

### Staging and prognosis

**TNM staging (AJCC 8th):**
- **Stage I:** T1-2 N0 M0 (tumor in mucosa/submucosa or muscularis propria, no nodes); 5-year OS >90%
- **Stage II:** T3-4 N0 M0 (through muscularis propria or into adjacent structures, no nodes); 5-year OS 70-85%; adjuvant chemotherapy benefit limited to high-risk features (T4, perforation, <12 lymph nodes examined, MSS)
- **Stage III:** Any T N1-2 M0 (1+ positive nodes); 5-year OS 40-70%; adjuvant FOLFOX × 3-6 months standard
- **Stage IV:** Any T, N, M1 (distant metastasis); 5-year OS ~15-25% for selected patients with resectable liver-only metastases; generally incurable but median OS improved from ~12 months (1990s) to ~30+ months with modern treatment

### Treatment [^van-cutsem-2011-crystal-cetuximab] [^kopetz-2019-beacon-crc]

**Curative intent (stages I-III + selected stage IV):**
- **Surgery:** Colectomy with adequate margins and regional lymph node dissection (minimum 12 nodes); laparoscopic approaches standard for colon; rectal cancer: total mesorectal excision (TME) — sharp dissection in areolar tissue plane → low local recurrence rates (<10%); robotic-assisted TME increasingly used
- **Adjuvant chemotherapy stage III:** FOLFOX (oxaliplatin + leucovorin + 5-FU) or CAPOX × 3-6 months; reduces recurrence risk ~25%; oxaliplatin adds benefit vs. 5-FU alone; adjuvant oxaliplatin not beneficial in stage II MSS or MSI-H tumors
- **Neoadjuvant rectal cancer:** Locally advanced rectal cancer (T3-4 or N+): long-course chemoradiation (5-FU + 45 Gy) OR short-course RT (5×5 Gy) followed by total neoadjuvant therapy (TNT: induction chemotherapy + CRT) → RAPIDO, PRODIGE-23 trials show higher pCR with TNT; "watch and wait" after clinical complete response increasingly considered for distal rectal cancer (non-operative management in ~25-30% of cCR patients)
- **Hepatic metastasectomy:** For resectable liver-only metastases; 5-year OS 30-50%; conversion chemotherapy (FOLFOX/FOLFIRI + bevacizumab or anti-EGFR) → downstage to resectability; repeat hepatectomy for recurrence

**Metastatic CRC (mCRC) — systemic therapy:**

*Backbone chemotherapy regimens:*
- **FOLFOX:** Oxaliplatin + leucovorin + 5-FU bolus + infusion (biweekly); first-line or adjuvant
- **FOLFIRI:** Irinotecan + leucovorin + 5-FU; equivalent first-line efficacy to FOLFOX; used second-line after FOLFOX failure
- **FOLFOXIRI:** Triple combination → higher ORR (66% in TRIBE trial) → for conversion chemotherapy for initially unresectable liver metastases

*Targeted therapies by biomarker:*

**RAS-wild-type (KRAS/NRAS codons 12/13/59/61/117/146 WT):**
- **Anti-EGFR:** Cetuximab (Erbitux) or panitumumab (Vectibix) + FOLFIRI → first-line; CRYSTAL trial: KRAS-wt patients, cetuximab + FOLFIRI: PFS 9.9 vs. 8.4 months vs. FOLFIRI alone; FIRE-3 head-to-head (cetuximab vs. bevacizumab with FOLFIRI): OS favored cetuximab in KRAS-wt (34.3 vs. 25.0 months) [^van-cutsem-2011-crystal-cetuximab]
- **Bevacizumab (anti-VEGFA):** Active in all mCRC regardless of RAS status; IFL: bevacizumab + IFL → PFS 10.6 vs. 6.2 months; OS 20.3 vs. 15.6 months; bevacizumab preferred in right-sided or BRAF-mutant mCRC (where EGFR inhibitors are ineffective)
- **Left vs. right primary site:** Left-sided (descending colon, sigmoid, rectum) RAS-wt mCRC → strongly prefer anti-EGFR first-line (OS ~33-36 months); right-sided (cecum, ascending, transverse) RAS-wt → anti-EGFR less effective (OS ~17-19 months); right-sided mCRC tends to be BRAF-mutant or MSI-H more often

**BRAF V600E-mutant mCRC:**
- **BEACON CRC:** Encorafenib (BRAF inhibitor) + cetuximab (anti-EGFR) → OS 9.3 vs. 5.9 months vs. control; also encorafenib + cetuximab + binimetinib (MEK inhibitor) triplet FDA approved; unlike melanoma BRAF-mutant, single-agent BRAF inhibition is ineffective in CRC due to EGFR-driven feedback reactivation [^kopetz-2019-beacon-crc]

**KRAS G12C-mutant mCRC:**
- **Adagrasib + cetuximab (KRYSTAL-10):** ORR 34%, PFS 6.9 months → FDA approved 2024; sotorasib + panitumumab (CodeBreaK 300): ORR 26% — both approved; KRAS G12C CRC accounts for ~3-4% of mCRC

**MSI-H/dMMR mCRC (~5% of mCRC):**
- **Pembrolizumab first-line (KEYNOTE-177):** PFS 16.5 vs. 8.2 months vs. chemotherapy; OS 77.8 vs. 36.7 months at 5 years — practice-changing; pembrolizumab now first-line for MSI-H mCRC (regardless of PD-L1)
- **Nivolumab + ipilimumab (CheckMate-142):** 58% ORR in MSI-H mCRC; approved second-line

**HER2 amplification/overexpression (~3-5% of RAS/RAF-wt mCRC):**
- Tucatinib + trastuzumab (MOUNTAINEER): ORR 38%, FDA approved 2023; pertuzumab + trastuzumab (MyPathway): ORR 38%

**Later-line therapies:**
- **Trifluridine + tipiracil (Lonsurf):** 5-FU prodrug combination; RECOURSE trial: OS 7.1 vs. 5.3 months vs. placebo; oral; approved 3L+
- **Regorafenib (Stivarga):** Multi-kinase inhibitor (VEGFR1-3, PDGFR, FGFR1, KIT, RET); CORRECT trial: OS 6.4 vs. 5.0 months; 3L+; tolerability challenging (hand-foot syndrome, liver toxicity)
- **Fruquintinib (Fruzaqla):** VEGFR1-3 inhibitor; FRESCO-2 trial: OS 7.4 vs. 4.8 months; approved 3L+ 2023

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS mutations (~40% of CRC) are acquired in the adenoma-carcinoma sequence; KRAS G12V/G12D-mutant CRC is resistant to EGFR inhibitors; KRAS G12C-mutant CRC → adagrasib + cetuximab (KRYSTAL-10, ORR 34%) — first targeted therapy for KRAS-mutant CRC.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — APC loss is the founding mutation in >80% of sporadic CRC → destruction complex collapse → beta-catenin nuclear accumulation → MYC, cyclin D1 → hyperproliferation; germline APC mutation causes FAP → obligate CRC without colectomy.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR is overexpressed in >80% of CRC; cetuximab and panitumumab improve OS in RAS-wild-type mCRC (CRYSTAL: cetuximab + FOLFIRI, PFS 9.9 vs. 8.4 months); RAS/RAF-wild-type status required for EGFR inhibitor benefit; left-sided primary strongly predicts EGFR inhibitor response.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E mutations (~8-10% of CRC) confer poor prognosis and EGFR inhibitor resistance; BEACON CRC: encorafenib + cetuximab → OS 9.3 vs. 5.9 months in BRAF V600E mCRC; single-agent BRAF inhibition is ineffective in CRC due to EGFR-driven feedback reactivation.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — FN-integrin α5β1/αvβ3 signaling drives EMT in CRC → vimentin, N-cadherin, MMP production → invasion and liver metastasis; EDB-FN is overexpressed in CRC stroma; tumor FN correlates with lymph node metastasis and worse prognosis in stage II-III CRC.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Most colorectal cancers arise in the large intestine via the adenoma-carcinoma sequence, so colonoscopy with polypectomy is preventive; right-sided tumors bleed occultly (→ anemia) while left-sided ones obstruct, and rectal cancer is resected by total mesorectal excision.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Lynch syndrome (germline MMR loss) causes ~3% of colorectal cancer, producing dMMR/MSI-H tumors that are hypermutated and exquisitely sensitive to PD-1 blockade — pembrolizumab is now first-line for MSI-H metastatic CRC; universal MMR/MSI testing of all CRC is recommended.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 loss (~75% of CRC) is the rate-limiting step that converts an advanced adenoma into invasive carcinoma: 17p loss plus TP53 mutation removes the DNA-damage checkpoint, unleashing the chromosomal instability that lets cells breach the muscularis mucosae.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — Colorectal and prostate cancers are two of the commonest adult solid tumours; both have hereditary drivers—Lynch raises both, BRCA2 raises prostate—and microsatellite-unstable CRC and DNA-repair-deficient prostate cancer both respond to checkpoint or PARP-based therapy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is the dominant site of colorectal metastasis via portal venous drainage: ~50% of CRC patients develop liver mets, and resection or ablation of oligometastatic liver disease can be curative; this portal route makes CRC liver-metastasis management central to oncology.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Familial adenomatous polyposis, from germline APC mutation, carpets the colon with hundreds-to-thousands of adenomas and guarantees colorectal cancer by mid-adulthood without prophylactic colectomy; APC loss is also the founding event in >80% of sporadic CRC.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — MUTYH-associated polyposis is a recessive hereditary cause of colorectal cancer: biallelic MUTYH loss fails to repair oxidative DNA damage, producing G:C→T:A mutations and multiple adenomas, so a FAP-like polyposis with negative APC testing prompts MUTYH analysis.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Long-standing inflammatory bowel disease drives colitis-associated colorectal cancer: chronic inflammation accelerates the dysplasia-carcinoma sequence (often p53 early, APC late—reversed from sporadic CRC), so colitis warrants surveillance colonoscopy.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The MSI-high subset of colorectal cancer is exquisitely immunotherapy-responsive: mismatch-repair deficiency generates abundant neoantigens that draw cytotoxic CD8+ T cells, so anti-PD-1 (pembrolizumab) works in MSI-high tumors while microsatellite-stable CRC remains resistant.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome shapes colorectal cancer risk: dysbiosis enriches pro-carcinogenic bacteria (e.g. Fusobacterium) that inflame mucosa and damage DNA, while a healthy fiber-fermenting flora is protective—linking the microbial ecosystem to tumorigenesis.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity is a major modifiable colorectal cancer risk factor: visceral adiposity drives insulin/IGF-1 signaling and chronic inflammation that promote colonic tumorigenesis, so rising early-onset CRC parallels obesity—weight and diet are key prevention levers.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is central to rectal (not colon) cancer: neoadjuvant chemoradiation with photon beams shrinks locally advanced rectal tumors before surgery, sometimes enough for watch-and-wait—colon cancer, by contrast, is treated with surgery and chemotherapy.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — APC loss is the gatekeeper mutation that starts colorectal cancer: inactivating APC unleashes Wnt/beta-catenin to form the first adenoma, so it initiates the adenoma-carcinoma sequence—mutated in FAP and in most sporadic colorectal cancers.
- `targets` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Colorectal cancer arises stepwise from the intestinal epithelium: normal crypt cells acquire APC, then KRAS, then p53 hits, progressing through adenoma to carcinoma—the textbook adenoma-carcinoma sequence that makes screening colonoscopy preventive.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 is the checkpoint that MSI-high colorectal tumors exploit to evade attack: blocking it produced the first tissue-agnostic FDA approval (pembrolizumab for any MSI-high cancer), so dMMR/MSI status is now tested at diagnosis to guide immunotherapy.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes raises colorectal cancer risk: high insulin and IGF-1 from insulin resistance promote colonocyte proliferation, and shared risks like obesity and inactivity compound it—so metabolic health is part of colorectal cancer prevention.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — After the liver, the lung is colorectal cancer's next metastatic stop: tumor cells reach it via the systemic circulation, and isolated lung metastases are sometimes surgically resected for cure—so chest imaging is routine in staging and follow-up.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — A subset of colorectal cancers are HER2-amplified: like in breast and gastric cancer, this drives growth and predicts resistance to anti-EGFR drugs, but responds to HER2-targeted combinations—so HER2 testing now guides therapy in metastatic disease.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Right-sided colorectal cancer often presents as iron-deficiency anemia: a slow-bleeding tumor depletes iron long before obstruction, so unexplained iron-deficiency anemia in an adult mandates colonoscopy to exclude colon cancer.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D and calcium intake are linked to colorectal risk: higher levels associate with lower incidence, and vitamin D's effects on colonocyte growth make it a studied (if unproven) chemopreventive alongside fiber and aspirin.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts drive colorectal progression: they remodel the tumor stroma, supply growth and survival signals, and promote chemoresistance and metastasis—a major reason the desmoplastic, fibroblast-rich CMS4 subtype carries a worse prognosis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Colorectal cancer is treated by starving its vessels of VEGF: the tumor secretes VEGF to build a blood supply, so anti-VEGF bevacizumab is a mainstay added to chemotherapy in metastatic colorectal cancer.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Colorectal cancer turns aggressive when it loses SMAD4: this late hit in the adenoma-carcinoma sequence disables TGF-β's growth restraint, driving invasion and metastasis and predicting a worse prognosis and poorer chemo response.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Most colorectal cancers are immune-cold, walled off by regulatory T cells: unlike MSI-high tumors, microsatellite-stable CRC has few neoantigens and Treg-rich stroma, which is why checkpoint immunotherapy works in only a minority.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Dietary calcium helps guard against colorectal cancer: it binds bile acids and fatty acids in the gut and signals colon cells to differentiate, so adequate calcium is one of the better-supported dietary protections against the disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages shape colorectal cancer: depending on their polarization they can promote or restrain the tumor, and a macrophage-rich, suppressive stroma helps the common microsatellite-stable cancers evade immunity.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Colorectal cancer can reach the brain late: though it spreads first to liver and lung, advanced disease occasionally seeds brain metastases, a sign of widespread disease that shifts care toward palliative and systemic treatment.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency is often the first clue to colorectal cancer: right-sided tumors bleed slowly into the stool, so unexplained iron-deficiency anemia in an older adult is a red flag that should prompt a colonoscopy.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Colorectal tumors build their own blood supply: VEGF recruits endothelial cells to sprout new vessels, and blocking this with bevacizumab is a mainstay of treating metastatic disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — A dense fibrotic stroma walls off colorectal cancer: the tumor provokes desmoplastic scar tissue that shields it from immune cells and drugs, part of why microsatellite-stable disease resists immunotherapy.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads colorectal cancer's grade in its glands: well-differentiated tumor cells keep orderly microvilli and tight junctions making lumina, while poorly differentiated ones lose this architecture — ultrastructure that tracks how aggressive the cancer is.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Colorectal cancer pushes platelets up: a paraneoplastic thrombocytosis appears in many patients and signals worse prognosis, while the platelets themselves help circulating tumor cells survive and seed the liver.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Late colorectal cancer can reach the bone: after seeding the liver and lungs, advanced disease occasionally spreads to the marrow-filled skeleton, an uncommon but ominous site marking widespread metastasis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — FOLFOX chemotherapy bites the nerves: oxaliplatin, a backbone of colorectal cancer treatment, injures peripheral sensory neurons, causing a distinctive cold-triggered tingling and numbness that can force dose reductions and outlast therapy.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Targeted therapy wastes magnesium: the anti-EGFR antibodies cetuximab and panitumumab, used in RAS-wild-type colorectal cancer, block EGFR in the kidney tubule, so magnesium leaks into the urine and must be monitored and replaced.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin reports on EGFR-blocking drugs: cetuximab and panitumumab provoke an acneiform facial rash, and its severity actually tracks with how well the colorectal tumor is responding, making the rash a visible biomarker.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies monitor and steer colorectal cancer: the CEA blood marker, read by immunoassay, tracks recurrence, while mismatch-repair (MMR) stains flag the MSI-high tumors that respond to checkpoint immunotherapy and prompt Lynch testing.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The FOLFOX backbone empties the marrow: the oxaliplatin-and-fluorouracil chemotherapy is myelosuppressive, dropping neutrophil counts between cycles so that febrile neutropenia is a recurring hazard of colorectal-cancer treatment.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Fiber guards the colon: gut bacteria ferment dietary fiber into butyrate that nourishes colonocytes and curbs malignant change, so a fiber-rich diet lowers colorectal-cancer risk while red and processed meat raise it.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Colorectal cancer thickens the blood: tumor procoagulants, surgery, and chemotherapy combine to make deep-vein thrombosis and pulmonary embolism common, so clot prophylaxis is routine around treatment of this cancer.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The 5-FU backbone can stun the heart: fluoropyrimidine chemotherapy (5-FU, capecitabine) provokes coronary vasospasm and direct cardiomyocyte injury, causing chest pain and even infarction that interrupts colorectal cancer treatment.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA links the tumor to aspirin: mutations in this gene activate PI3K signaling in a subset of colorectal cancers, and the chemopreventive benefit of aspirin appears concentrated in these PIK3CA-mutant tumors.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — The Wnt switch is thrown at the gene that APC guards: when APC fails, β-catenin (CTNNB1) escapes degradation, enters the nucleus and turns on growth genes — the molecular heart of the adenoma-carcinoma sequence, and the rare driver when CTNNB1 itself is mutated.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — A gut bacterium can be a carcinogen: strains of E. coli carrying the pks island make colibactin, a genotoxin that scars colon-cell DNA with a signature mutation pattern, directly implicating the microbiome in colorectal tumor initiation.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — The liver is its favored landing site: colorectal cells seeding the portal blood lodge among hepatocytes to grow liver metastases, the disease's commonest spread and the reason a resectable liver lesion can still mean cure.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation drives the colitis-to-cancer path: NF-κB activation in the chronically inflamed bowel links inflammatory bowel disease to colorectal cancer, switching on the survival and proliferation signals that turn inflamed mucosa malignant.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 feeds the tumor through STAT3: in inflammation-associated colorectal cancer, IL-6 from the microenvironment activates STAT3 in epithelial cells to push their proliferation and survival, tightly coupled to the NF-κB inflammatory program.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — An obstructing or perforating tumor can seed infection: colorectal cancers that block or breach the bowel wall spill gut flora into the abdomen and bloodstream, and chemotherapy neutropenia adds its own route to sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Beyond bleeding, inflammation blunts the marrow: alongside the iron-deficiency anemia from chronic blood loss, the tumor's IL-6-driven inflammation raises hepcidin and suppresses erythropoiesis, adding an anemia-of-chronic-disease component.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its mainstay chemo can injure the heart: 5-fluorouracil and capecitabine cause coronary vasospasm and a cardiotoxicity that can precipitate ischemia and cardiac dysfunction during colorectal cancer treatment.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Treatment and obstruction both threaten the kidney: the bevacizumab used in metastatic colorectal cancer causes proteinuria and renal injury, while pelvic tumor can obstruct the ureters, together risking chronic kidney disease.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its oxaliplatin leaves nerves burning: the platinum drug in FOLFOX, a backbone of colorectal-cancer therapy, causes a dose-dependent peripheral neuropathy with cold-triggered and chronic neuropathic pain that can persist long after treatment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its chemotherapy opens the lung to mold: the neutropenia from colorectal-cancer regimens can let inhaled Aspergillus invade as pulmonary aspergillosis, especially in heavily pretreated or metastatic patients.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Diagnosis and a stoma weigh on mood: the cancer diagnosis, ostomy and altered bowel function and prolonged chemotherapy of colorectal cancer contribute to substantial depression and impaired quality of life.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It grows in and obstructs the gut: colorectal cancer arises from the colonic epithelium and can occlude the bowel lumen, causing obstruction, altered bowel habit and the need for resection or a stoma.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Colectomy hinges on a healing anastomosis: bowel resection for colorectal cancer joins two ends of gut, and anastomotic leak — failure of that wound to heal — is a feared, life-threatening complication.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Surveillance and stoma life breed worry: the recurrence monitoring, CEA checks and altered bowel function or ostomy of colorectal cancer foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — After the liver, it climbs to the lungs: pulmonary metastases are the second commonest distant site in colorectal cancer, and resectable lung deposits are sometimes removed with curative intent.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The nodes decide its fate: regional lymph-node involvement is the dominant prognostic factor in colorectal cancer, defining stage III disease and the need for adjuvant chemotherapy after surgery.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Mismatch-repair failure makes it visible: MSI-high colorectal tumours carry many neoantigens and respond strongly to checkpoint-inhibitor immunotherapy, unlike the common microsatellite-stable cancers.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its chemotherapy can spasm the coronaries: 5-fluorouracil and capecitabine cause coronary vasospasm and cardiotoxicity, and bevacizumab raises blood pressure and thrombosis risk.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its targeted drugs erupt on the skin: the EGFR inhibitor cetuximab causes a characteristic acneiform rash, and capecitabine causes hand-foot syndrome.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its drugs and spread reach the nerves: oxaliplatin causes a cold-triggered peripheral neuropathy, and advanced rectal cancer can metastasise to the brain.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It is matched to tumour genotype: anti-EGFR antibodies (cetuximab) for RAS-wild-type tumours, anti-VEGF bevacizumab and checkpoint immunotherapy for MSI-high disease guide modern colorectal cancer treatment.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Tumour and drugs reach the kidney: a bulky rectal or pelvic tumour can obstruct the ureters, and oxaliplatin-based chemotherapy carries nephrotoxic risk.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pelvic surgery and spread affect it: rectal cancer surgery risks injury to nerves controlling sexual function, and colorectal cancer can metastasise to the ovaries as Krukenberg-type deposits.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — FOLFOX is the backbone: 5-fluorouracil with oxaliplatin or irinotecan is the cytotoxic core of colorectal cancer treatment, given adjuvantly after surgery for node-positive disease and as first-line therapy for metastatic disease.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — MSI status splits the response: the ~15% of colorectal cancers that are mismatch-repair-deficient (MSI-high) respond dramatically to PD-1 blockade like pembrolizumab, while the microsatellite-stable majority remain immunologically cold and resistant.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It seeds the liver first: draining via the portal vein, colorectal cancer metastasises preferentially to the hepatic lobules, and these liver metastases — uniquely among cancers — are often resected or ablated for cure.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Why some colorectal cancers invite immunotherapy: mismatch-repair-deficient (MSI-high) tumours accumulate neoantigens and dense lymphocytic infiltrates with tertiary lymphoid structures, the immune richness behind their response to checkpoint blockade.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — A hamartomatous route to colorectal cancer: SMAD4/BMPR1A juvenile polyposis studs the colon with hamartomatous polyps that raise lifetime colorectal-cancer risk, a hereditary syndrome beyond the adenomatous FAP and Lynch.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Another hamartomatous predisposition: STK11/LKB1 Peutz-Jeghers syndrome carries a high lifetime risk of colorectal and other GI cancers from its hamartomatous polyps, joining the hereditary colorectal-cancer syndromes.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Lung as a metastatic site: colorectal cancer—especially rectal tumours draining systemically—seeds the lungs after the liver, depositing nodules in the alveolar parenchyma that pulmonary metastasectomy can sometimes cure.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Lynch's other hallmark tumour: the mismatch-repair deficiency that drives hereditary colorectal cancer drives endometrial cancer just as strongly, so the two define the Lynch syndrome spectrum and share MSI-targeted immunotherapy.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Chemotherapy's cardiac risk: 5-fluorouracil, the backbone of colorectal cancer therapy, can provoke coronary vasospasm and ischaemia of the myocardium, an under-recognised cardiotoxicity that occasionally causes infarction.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Same mutation, different drug response: BRAF V600E drives a colorectal cancer subset and melanoma, yet BRAF inhibitors alone fail in colon cancer because EGFR feedback reactivates the pathway—so combinations with anti-EGFR are needed.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Shared GI adenocarcinoma biology: colorectal and gastric cancers overlap in HER2-targeted therapy, microsatellite-instability immunotherapy and Lynch-syndrome predisposition, two adenocarcinomas of the gut tube.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Peritoneal and Lynch links: colorectal cancer can metastasise to the ovary (Krukenberg-type) and seed the peritoneum like ovarian cancer, while Lynch syndrome predisposes to both tumours.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 chemoprevention: COX-2-derived prostaglandins drive colorectal carcinogenesis, and aspirin/NSAID inhibition of this pathway reduces colorectal cancer risk.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Wnt's oncogene: APC loss and constitutive Wnt signalling activate MYC, a central driver of proliferation in colorectal cancer.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Adenoma-to-carcinoma switch: loss of TGF-β/SMAD4 tumour-suppressor signalling drives the progression of colorectal adenomas to invasive, metastatic carcinoma.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: PIK3CA mutation activates AKT in colorectal cancer, driving growth and survival and contributing to resistance to anti-EGFR therapy.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: Wnt-driven cyclin D1 with CDK4/6 propels colorectal cancer cells through the G1 checkpoint along the adenoma-carcinoma sequence.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in hypoxic colorectal tumours drives the VEGF angiogenesis and invasive, metastatic phenotype linked to poor prognosis.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — MLH1 loss—germline in Lynch syndrome or sporadic via promoter hypermethylation—creates the microsatellite-instable, hypermutated CRC subtype that, uniquely among colorectal cancers, responds dramatically to checkpoint inhibitors like pembrolizumab.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on colorectal-cancer cells follows CXCL12 gradients toward the liver through the portal circulation, helping explain why the liver is the dominant site of CRC metastasis and the focus of metastasectomy.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 signaling through STAT3 links chronic colonic inflammation to carcinogenesis, the molecular basis of the elevated colorectal-cancer risk in inflammatory bowel disease that defines colitis-associated cancer.
- `connects-to` → **[MSH2](../../03-molecular/msh2/README.md)** — Germline MSH2 mutations, alongside MLH1, cause Lynch syndrome and the microsatellite-instable colorectal cancers, the mismatch-repair defect that both drives hereditary risk and predicts response to checkpoint blockade.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Mismatch-repair-deficient colorectal cancers accumulate mutations and cytosolic DNA that engage cGAS-STING, the innate-immune basis for the striking sensitivity of MSI-high tumors to PD-1 blockade, unlike the immune-cold MSS majority.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits tumor-associated macrophages into colorectal cancer, building the immunosuppressive myeloid niche that helps explain why the microsatellite-stable majority resist immunotherapy.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates the PI3K-AKT axis (PIK3CA and AKT already mapped) in colorectal cancer and is associated with resistance to anti-EGFR antibodies in KRAS-wild-type tumors.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling cooperates with Wnt in the intestinal crypt stem-cell compartment, and its dysregulation sustains the cancer-stem-cell population driving colorectal tumor growth and relapse.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — 5-fluorouracil and oxaliplatin kill colorectal cancer cells through caspase-3-mediated apoptosis, and defects in this death program underlie the chemoresistance that limits cure in metastatic disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGFR, KRAS and BRAF (all mapped) signal through the MAPK-ERK cascade in colorectal cancer, the axis whose RAS-mutation status determines response to anti-EGFR therapy.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA, AKT and PTEN already mapped) that cooperates with the adenoma-carcinoma drivers in colorectal cancer.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — β-catenin-driven cyclin-D1 (mapped) and CDK4/6 release E2F1 to drive the proliferation initiated by APC loss in the colorectal adenoma-carcinoma sequence.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Gut-microbiota TLR-MyD88-NF-κB signaling (NF-κB already mapped), exemplified by Fusobacterium nucleatum, promotes inflammation-associated colorectal carcinogenesis and links inflammatory bowel disease to cancer risk.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped) sustains the tumor-promoting inflammatory microenvironment of colorectal cancer.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) contributes to the cell-cycle progression of colorectal cancer.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes immune evasion and the liver-metastatic colonization that drives mortality in colorectal cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling governs the antitumor immune response of colorectal cancer, particularly the immunotherapy-responsive mismatch-repair-deficient subtype.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression silences tumor-suppressor genes and contributes to the epigenetic dysregulation of colorectal cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven cyclin-D1-RB1 cell-cycle entry (cyclin-D1 and RB1 already mapped) sustains the proliferation of colorectal cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-mediated FOXO inactivation (PI3K-AKT already mapped) removes a pro-apoptotic brake, favoring survival in colorectal cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells mediates the immune clearance that the immunogenic mismatch-repair-deficient colorectal cancer must evade.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the β-catenin destruction-complex activity (APC/CTNNB1/Wnt already mapped) whose disruption drives colorectal cancer.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in colorectal cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from myeloid cells shape the inflammatory, tumor-promoting microenvironment of colorectal cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of EGFR (EGFR already mapped) drives the invasion and metastasis of colorectal cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the CpG-island-methylator-phenotype epigenetic dysregulation of colorectal cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of colorectal cancer cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of colorectal cancer, a candidate metformin target.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of colorectal cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of colorectal cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of colorectal cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of colorectal cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment (colitis-associated) of colorectal cancer.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — MSI immunotherapy: mismatch-repair-deficient, microsatellite-unstable colorectal cancers (MLH1/MSH2 already mapped) generate abundant neoantigens presented on MHC, making this subset uniquely responsive to checkpoint inhibitors while proficient tumours remain cold.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron-deficiency presentation: right-sided colorectal cancers bleed occultly, and the resulting iron-deficiency anaemia with low transferrin saturation is a classic presenting sign that should prompt colonoscopy in older adults.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Metabolic risk: obesity and insulin resistance raise circulating IGF-1, a mitogen for colonic epithelium, part of the mechanism linking metabolic syndrome and Western diet to increased colorectal cancer risk.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — MSI immunotherapy: the mismatch-repair-deficient, microsatellite-unstable colorectal cancers (MLH1/MSH2 already mapped) are neoantigen-rich and respond to checkpoint blockade (PD-1 already mapped), and IL-2-driven T-cell expansion underlies this immune sensitivity.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Iron-deficiency anaemia: right-sided colorectal cancers bleed occultly (transferrin already mapped), and the iron-deficiency anaemia lowering haemoglobin is a classic presenting sign that should prompt colonoscopy in older adults.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Fluoropyrimidine cardiotoxicity: 5-fluorouracil and capecitabine, backbone chemotherapy for colorectal cancer, can provoke coronary vasospasm and myocardial injury, and troponin elevation helps detect this recognised cardiotoxicity.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Diet and bile acids: a Western diet high in fat raises the cholesterol-derived bile acids that, deconjugated by gut bacteria (microbiome already mapped), promote colorectal carcinogenesis, part of the dietary risk of colorectal cancer.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (CD8 and PD-1 already mapped), the immune evasion that is more readily overcome in the microsatellite-unstable (MLH1 already mapped) tumours.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: chronic colonic inflammation and the high epithelial turnover generate oxidative stress, to which xanthine oxidase contributes, and this oxidative DNA damage speeds the adenoma-carcinoma sequence of colorectal cancer.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment of the microsatellite-stable colorectal cancers that resist checkpoint blockade.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and proliferation: leptin from adipose tissue promotes the proliferation of the colonic epithelium, part of the mechanism by which obesity raises the risk of colorectal cancer alongside the insulin-IGF-1 axis (IGF-1 already mapped).
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Hyperinsulinaemia: the hyperinsulinaemia of obesity and type 2 diabetes drives colorectal carcinogenesis through insulin and the IGF-1 axis (already mapped), a modifiable metabolic risk factor for the cancer.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of colorectal cancer.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Anti-proliferative adipokine: adiponectin falls with obesity (leptin and insulin already mapped), and this loss removes a brake on the colonic epithelial proliferation, part of the obesity link to colorectal cancer.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine inflammation: resistin, with leptin and adiponectin (already mapped), is a pro-inflammatory adipokine of obesity that promotes the colonic proliferation and inflammation implicated in colorectal-cancer risk.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron-deficiency anaemia: the chronic occult bleeding of colorectal cancer causes the iron-deficiency anaemia (transferrin and haemoglobin already mapped), a classic presentation that prompts the diagnosis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — MSI immunogenicity: the cGAS-STING (already mapped) sensing of the genomic instability of the MSI-high (MLH1 and MSH2 already mapped) colorectal cancer drives the type-I interferon behind the checkpoint (PD-1 already mapped) response.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Chemoprevention selenium: the antioxidant selenoprotein status is inversely associated with the colorectal-cancer risk, part of the micronutrient chemoprevention of the colonic epithelium.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, exploited by the checkpoint (PD-1 already mapped) immunotherapy of the MSI-high colorectal cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the colorectal-cancer immune microenvironment.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK surveillance: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance of the colorectal cancer, complementing the T-cell (already mapped) checkpoint immunotherapy of the MSI-high tumours.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of colorectal cancer (the tumour-associated tissue eosinophilia is prognostic).
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the tumour-promoting inflammation of colorectal cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the colorectal-cancer microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of colorectal cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, predicts the checkpoint (PD-1 already mapped) response of the MSI-high colorectal cancer.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the tumour-promoting-versus-protective immune balance of colorectal cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tumour complement: the complement C3 activation contributes to the inflammatory and immunosuppressive dimension of the colorectal-cancer microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment into the colorectal-cancer microenvironment.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the tumour antigen to the CD8 (already mapped) T cells, shaping the checkpoint (PD-1 already mapped) response of the MSI-high colorectal cancer.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^siegel-2024-crc-statistics]: Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. *CA Cancer J Clin.* 2024;74(1):12-49. [doi:10.3322/caac.21820](https://doi.org/10.3322/caac.21820) · [PubMed 38230766](https://pubmed.ncbi.nlm.nih.gov/38230766/)
[^van-cutsem-2011-crystal-cetuximab]: Van Cutsem E, Köhne CH, Láng I, et al. Cetuximab plus irinotecan, fluorouracil, and leucovorin as first-line treatment for metastatic colorectal cancer: updated analysis according to tumor KRAS and BRAF mutation status. *J Clin Oncol.* 2011;29(15):2011-2019. [doi:10.1200/JCO.2010.33.5091](https://doi.org/10.1200/JCO.2010.33.5091) · [PubMed 21502544](https://pubmed.ncbi.nlm.nih.gov/21502544/)
[^kopetz-2019-beacon-crc]: Kopetz S, Grothey A, Yaeger R, et al. Encorafenib, binimetinib, and cetuximab in BRAF V600E-mutated colorectal cancer. *N Engl J Med.* 2019;381(17):1632-1643. [doi:10.1056/NEJMoa1908075](https://doi.org/10.1056/NEJMoa1908075) · [PubMed 31566309](https://pubmed.ncbi.nlm.nih.gov/31566309/)
