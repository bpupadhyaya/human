---
schema: human-scale-entry/v1
id: hereditary-diffuse-gastric-cancer
name: Hereditary Diffuse Gastric Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary diffuse gastric cancer (HDGC) is caused by germline CDH1 (~25%) or CTNNA1 (~2-5%) mutations; diffuse/signet ring histology; lifetime GC risk ~83% (CDH1 male); prophylactic gastrectomy is recommended; lobular breast cancer risk is elevated in CDH1/CTNNA1 carriers."
aliases: ["HDGC", "hereditary diffuse gastric cancer", "CDH1 gastric cancer", "CTNNA1 HDGC", "diffuse gastric cancer hereditary", "signet ring cell hereditary", "E-cadherin gastric cancer", "CDH1 prophylactic gastrectomy", "HDGC lobular breast cancer"]
sources:
  - id: van-der-post-2015-hdgc-guidelines
    type: peer-reviewed
    cite: "van der Post RS, Vogelaar IP, Carneiro F, et al. Hereditary diffuse gastric cancer: updated clinical guidelines with an emphasis on germline CDH1 mutation carriers. J Med Genet. 2015;52(6):361-374."
    doi: "10.1136/jmedgenet-2015-103094"
    pmid: "25979631"
    url: "https://doi.org/10.1136/jmedgenet-2015-103094"
  - id: hansford-2015-hdgc
    type: peer-reviewed
    cite: "Hansford S, Kaurah P, Li-Chang H, et al. Hereditary Diffuse Gastric Cancer Syndrome: CDH1 Mutations and Beyond. JAMA Oncol. 2015;1(1):23-32."
    doi: "10.1001/jamaoncol.2014.168"
    pmid: "26182300"
    url: "https://doi.org/10.1001/jamaoncol.2014.168"
cross_links:
  - target: 01-human/03-molecular/ctnna1
    relation: connects-to
    note: "Germline CTNNA1 LOF causes HDGC in CDH1-negative families (~2-5% of HDGC); prophylactic gastrectomy is recommended for pathogenic CTNNA1 carriers; penetrance estimated similar to CDH1; somatic CTNNA1 serves as the second hit in CDH1-germline HDGC tumors."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "Germline CDH1 pathogenic variants cause ~25-30% of HDGC; E-cadherin loss → diffuse signet ring cell carcinoma; prophylactic gastrectomy reveals T1a SRCC foci in ~90% of carriers; CDH1 also drives lobular breast cancer risk (~39-52% lifetime in female CDH1 carriers."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "HDGC is a hereditary form of diffuse-type gastric cancer (Lauren classification); signet ring cell histology; endoscopic surveillance is insufficient for SRCC → prophylactic gastrectomy preferred; CDH1/CTNNA1 germline accounts for ~1-3% of all GC globally."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Female CDH1 germline carriers have ~39-52% lifetime lobular breast cancer risk; CTNNA1 carriers also have elevated lobular BC risk; annual breast MRI from age 30 recommended; lobular BC in HDGC families is driven by E-cadherin/alpha-catenin pathway loss in breast epithelium."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "HDGC seeds dozens of T1a signet-ring foci throughout normal-looking gastric mucosa (clustered at the body-antrum transition), invisible to white-light endoscopy; surveillance cannot reliably catch them, so prophylactic total gastrectomy is definitive for CDH1 carriers."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "E-cadherin anchors adherens junctions via its tail → β-catenin (CTNNB1) → α-catenin (CTNNA1) → F-actin; germline loss of CDH1 or CTNNA1 collapses this adhesion complex → poorly cohesive signet-ring cells; the same axis links HDGC to lobular breast cancer."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Lynch syndrome is the other major hereditary gastric cancer syndrome but contrasts sharply: MMR-deficient intestinal-type GC at ~5-13% risk, versus HDGC's diffuse signet-ring tumors at ~67-83%; histology and germline panel (CDH1/CTNNA1 vs MLH1/MSH2/MSH6/PMS2) separate them."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "HDGC and FAP are both dominant GI cancer syndromes but opposite in lesion: HDGC seeds the stomach with CDH1-driven signet-ring foci that form no polyps, while FAP carpets the colon with thousands of APC-driven adenomas — diffuse versus adenomatous, gastrectomy versus colectomy."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Peutz-Jeghers syndrome is another hereditary cause of gastric cancer, but via STK11/LKB1 hamartomatous polyps (and mucocutaneous pigmentation) rather than HDGC's CDH1 signet-ring foci; both raise gastric and breast cancer risk — distinct routes, hamartoma versus loss of cohesion."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Juvenile polyposis syndrome (SMAD4 or BMPR1A) is a third hereditary gastric cancer syndrome, marked by hamartomatous juvenile polyps and, in SMAD4 carriers, massive gastric polyposis with elevated gastric cancer risk — contrasting HDGC's non-polypoid CDH1 signet-ring cancer."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Hereditary diffuse gastric cancer forces a drastic digestive-system decision: because CDH1 carriers develop scattered, endoscopically invisible signet-ring foci throughout the stomach, prophylactic total gastrectomy is recommended early, since screening cannot reliably catch it."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Hereditary diffuse gastric cancer arises from gastric epithelium losing adhesion: germline CDH1 (E-cadherin) loss lets individual epithelial cells detach and infiltrate as signet-ring cells without forming a mass, the diffuse linitis-plastica pattern that makes it hard to detect."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "CDH1 mutations carry a colorectal as well as gastric risk: HDGC families show excess signet-ring/diffuse-type colorectal cancers alongside lobular breast and diffuse gastric cancer, reflecting E-cadherin's role in epithelial adhesion across the gut—so colonoscopy is advised."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "HDGC and HBOC both raise inherited breast cancer risk through different genes: CDH1 loss in HDGC predisposes to lobular breast cancer, while BRCA1/2 loss in HBOC drives ductal/triple-negative breast and ovarian cancer—distinct genes and histologies."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "HDGC and esophageal adenocarcinoma both threaten the upper GI tract: CDH1-driven diffuse gastric cancer can extend into the gastroesophageal junction, overlapping with esophageal adenocarcinoma, so surveillance in CDH1 carriers must cover the distal esophagus too."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "HDGC and Cowden syndrome are both dominant cancer syndromes with prominent breast and GI risk but different drivers: CDH1 (cell adhesion) versus PTEN (PI3K-AKT)—HDGC gives diffuse gastric and lobular breast cancer, Cowden adds thyroid cancer and hamartomas."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "Helicobacter pylori matters even in CDH1-driven gastric cancer: while HDGC arises from inherited E-cadherin loss rather than infection, H. pylori adds carcinogenic inflammation, so eradicating it is recommended in CDH1 carriers to remove an avoidable second hit."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Losing E-cadherin in HDGC unleashes Wnt/beta-catenin signaling: CDH1 normally tethers beta-catenin at the membrane, so its loss frees beta-catenin to drive proliferation while destroying cell-cell adhesion—driving the diffuse spread of signet-ring cells."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Diffuse gastric cancer infiltrates through a fibroblast-rich stroma: lacking E-cadherin, signet-ring cells scatter singly through a desmoplastic wall (linitis plastica) rather than forming a mass—so the stomach stiffens diffusely and tumors hide from endoscopy."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "CDH1 mutation behind HDGC also drives lobular breast cancer: female carriers face a high lifetime risk of this diffuse breast tumor, so HDGC management includes breast MRI surveillance and consideration of risk-reducing mastectomy alongside prophylactic gastrectomy."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "HDGC can seed the ovary as a Krukenberg tumor: diffuse signet-ring gastric cancer characteristically metastasizes to both ovaries, so bilateral ovarian masses with signet-ring cells should prompt a search for an occult gastric primary."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Diffuse signet-ring gastric cancers like HDGC engage the immune system poorly: they tend to be microsatellite-stable with low mutational burden and an immunosuppressive stroma, so checkpoint immunotherapy works far less well than in intestinal-type gastric cancer."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Hereditary diffuse gastric cancer spreads through the stomach wall and lymphatics: signet-ring cells infiltrate diffusely (linitis plastica) and seed nodes and peritoneum without a mass, so it is often advanced when found—why carriers undergo prophylactic gastrectomy."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Diffuse gastric cancer freezes the stomach's smooth muscle: signet-ring infiltration and desmoplasia stiffen all layers into a rigid leather-bottle linitis plastica, so the muscular wall loses peristalsis and the stomach can no longer expand or empty normally."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy struggles against diffuse gastric cancer: the infiltrative, mobile stomach and scattered signet-ring cells make photon-beam targeting hard, so radiation plays a limited, mostly palliative role compared with surgery and chemotherapy."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "HDGC's other cancer is estrogen-driven lobular breast cancer: the same CDH1/E-cadherin loss that causes diffuse stomach cancer produces invasive lobular breast cancer, which is typically estrogen-receptor positive—so carriers need breast as well as stomach surveillance."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "Diffuse gastric cancer in HDGC is usually HER2-negative: unlike intestinal-type stomach tumors that can be HER2-amplified and treated with trastuzumab, the signet-ring cancers of CDH1 carriers lack this target, leaving chemotherapy and surgery."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "HDGC tumors hide among regulatory T cells: the scattered signet-ring cells sit in a desmoplastic, immunosuppressive stroma where Tregs blunt anti-tumor immunity, part of why diffuse gastric cancer is hard to treat once it spreads."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "HDGC's whole problem is calcium-dependent glue gone missing: E-cadherin (CDH1) needs calcium to bind cells together, so losing it dissolves cell-cell adhesion and lets the signet-ring cells scatter and infiltrate diffusely rather than form a lump."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages fill HDGC's dense stroma: tumor-associated macrophages in the desmoplastic, scattered-cell tumor promote invasion and suppress immunity, part of why diffuse gastric cancer is so hard to treat once it spreads through the wall."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta builds the fibrous, infiltrative stroma of HDGC: it drives the desmoplasia and EMT-like behavior that help the discohesive signet-ring cells spread, stiffening the stomach wall as in linitis plastica."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hereditary diffuse gastric cancer spreads silently to the liver: its scattered signet-ring cells seed the peritoneum and liver early, so metastasis is often present by the time the infiltrative tumor is found."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Hereditary diffuse gastric cancer recruits endothelial cells: as the discohesive tumor infiltrates, it drives angiogenesis through these vessel-lining cells to supply blood for its spread through the stomach wall."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Diffuse gastric cancer hides in a low-oxygen stroma: its dense desmoplastic tissue chokes off oxygen, and the hypoxia drives survival signaling and blunts drug delivery, helping the scattered cells resist therapy."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "The prophylactic gastrectomy that prevents HDGC leaves lasting deficiencies: without stomach acid and intrinsic factor, iron and B12 malabsorb, so lifelong supplementation is needed."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "HDGC's signet-ring cells spread across the peritoneum and can encase the bowel, the transcoelomic spread that makes diffuse gastric cancer so lethal once it escapes the stomach."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "HDGC scleroses the stomach: signet-ring cells provoke a dense desmoplastic fibrosis (linitis plastica) that stiffens the wall and hides the cancer from endoscopy until it is advanced."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows why HDGC spreads diffusely: losing E-cadherin, the cells let go of one another and scatter as lone signet-ring cells, each with a mucin vacuole shoving its nucleus to the rim, never forming glands."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Signet-ring gastric cancer can seep into the marrow: HDGC's diffuse cells infiltrate the bone marrow, triggering a microangiopathic anemia and a leukoerythroblastic blood picture in advanced disease."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "HDGC spreads to the lung: beyond the peritoneum and liver, its scattered cells seed pulmonary and lymphangitic metastases, marking the widespread disease that prophylactic gastrectomy aims to prevent."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody stain reveals the defect: loss of E-cadherin (CDH1) on immunohistochemistry betrays the scattered signet-ring cells of HDGC, the molecular hallmark that distinguishes this stealthy, non-mass-forming cancer."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Both the cancer and its prevention drain the red cells: the diffuse tumor bleeds slowly into iron-deficiency anemia, and the prophylactic total gastrectomy that cures the risk leaves patients short of B12 and iron for life."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Losing the stomach can later harm the nerves: without it, B12 absorption fails, so unless replaced, the deficiency can damage peripheral and spinal cord neurons into a subacute combined degeneration."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "After the stomach is removed, the gut is rebuilt: prophylactic total gastrectomy, done young in CDH1 carriers, joins the esophagus to a loop of jejunum, so the small intestine becomes the new reservoir and the site of the lifelong malabsorption that follows."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Life without a stomach burns off fat: total gastrectomy leaves carriers eating small, frequent meals with poor fat absorption, so significant weight loss and depleted adipocyte stores are an expected, lifelong consequence needing dietitian support."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Diffuse gastric cancer drives clotting: like other gastric adenocarcinomas its discohesive, mucin-producing cells trigger paraneoplastic thrombocytosis and a high risk of venous thromboembolism once the disease becomes invasive."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 loss helps the diffuse tumor advance: after CDH1 starts the discohesive growth, TP53 mutation is a frequent secondary hit that lets the signet-ring cells progress to invasive, lethal cancer."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The signet-ring tumor hides from killer T cells: diffuse gastric cancer is typically immune-cold with sparse cytotoxic T-cell infiltration, part of why it responds poorly to the immunotherapy that helps other gastric cancers."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Gastric cancer crosses hereditary syndromes: stomach cancer also features in Li-Fraumeni's TP53 spectrum, so a young diffuse gastric cancer prompts a wider germline search beyond CDH1."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "The stomach's loss costs iron: bleeding from diffuse gastric cancer, and the prophylactic total gastrectomy that prevents it, both cause iron (and B12) deficiency anemia, a lasting consequence carriers manage for life."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "A second hit speeds the cancer: beyond the germline CDH1 loss, cooperating mutations such as CDKN2A inactivation help diffuse gastric cancer progress, part of the somatic events layered on the inherited defect."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Cancer and major surgery raise the clot risk: an established diffuse gastric cancer and the total gastrectomy that treats it both predispose to venous thromboembolism, needing perioperative prophylaxis."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Inflammation accelerates the E-cadherin-deficient stomach: IL-6/STAT3 signaling in the gastric mucosa adds a proliferative push to the loss of cell-cell adhesion from germline CDH1 inactivation that drives diffuse gastric cancer."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Prophylactic gastrectomy carries surgical risk: CDH1 carriers often undergo risk-reducing total gastrectomy, whose anastomotic leak and infection can seed intra-abdominal sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Loss of the stomach drains the blood in many ways: beyond tumor bleeding and B12 malabsorption after gastrectomy, the inflammatory cytokines of the cancer add an anemia of chronic disease."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Removing the stomach costs the bones: total gastrectomy impairs absorption of calcium and vitamin D and disrupts gut hormones, so metabolic bone disease and osteoporosis are recognized long-term consequences."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A drastic preventive choice weighs on the mind: facing a high inherited risk of an aggressive stomach cancer, and choosing prophylactic total gastrectomy with its lifelong eating changes, carries a heavy psychological burden."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Advanced disease and its chemo strain the kidney: the platinum chemotherapy for diffuse gastric cancer is nephrotoxic, and poor intake after gastrectomy adds dehydration, together risking chronic kidney disease."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A genetic verdict and prophylactic gastrectomy breed worry: CDH1 carriers face the decision to remove a healthy stomach and lifelong cancer risk, fostering profound health anxiety."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Total gastrectomy is a major wound to heal: the prophylactic or therapeutic removal of the entire stomach creates a high-risk esophageal anastomosis prone to leak and slow healing."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Surgery, chemo and B12 loss injure nerves: post-gastrectomy adhesive pain, platinum chemotherapy neuropathy and the B12 deficiency of an absent stomach combine to produce neuropathic pain."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Losing the stomach upends metabolism: prophylactic total gastrectomy in HDGC removes ghrelin-producing tissue and causes dumping syndrome with reactive hypoglycaemia and lasting nutritional disturbance."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Malabsorption after gastrectomy weakens bone and muscle: the impaired calcium, vitamin D and protein uptake of an absent stomach causes metabolic bone disease and sarcopenia in HDGC survivors."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Vitamin B12 loss can degrade the spinal cord: with no stomach to make intrinsic factor, untreated B12 deficiency after gastrectomy causes subacute combined degeneration with sensory and cognitive decline."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its gene also binds skin cells: CDH1 encodes E-cadherin, a cell-adhesion protein of epithelia and skin, and some CDH1 families carry cleft lip and palate alongside their cancer risk."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Diffuse spread reaches the chest: signet-ring gastric cancer disseminates transcoelomically to the peritoneum and can seed the pleura, causing malignant effusions and breathlessness."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Life after total gastrectomy strains the circulation: dumping syndrome causes postprandial tachycardia, sweating and hypotension as food rushes into the small bowel."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "A fellow inherited gastrointestinal-cancer syndrome: like MUTYH-associated polyposis, HDGC drives early gastrointestinal cancer needing intensive surveillance, the two entering the hereditary-GI-cancer differential."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Prophylactic surgery disturbs nutrition: the total gastrectomy that removes HDGC risk impairs absorption of vitamin D, calcium and B12, requiring lifelong supplementation."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Loss of the stomach drains minerals: after risk-reducing gastrectomy, impaired gastric acid and absorption deplete iron and zinc, contributing to anaemia and poor healing."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for the diffuse cancer that escapes surgery: advanced signet-ring diffuse gastric cancer is treated with FLOT-type chemotherapy, though this discohesive subtype responds relatively poorly."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Claudin-18.2 offers a target: diffuse gastric cancers often express Claudin-18.2, and the antibody zolbetuximab added to chemotherapy improves survival in this otherwise hard-to-target subtype."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy for advanced disease: PD-1 inhibitors added to chemotherapy treat advanced gastric cancer, with benefit concentrated in MSI-high and PD-L1-high tumours."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Knudson's two-hit model in the stomach: CDH1 is a tumour-suppressor inactivated like RB1—a germline first hit plus somatic loss (often promoter methylation) of the second allele—so HDGC mirrors retinoblastoma's founding mechanism of hereditary cancer."
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "Two diseases of one adhesion complex: HDGC can arise from CTNNA1 (α-catenin) loss that breaks E-cadherin cell adhesion, while desmoid tumours arise from CTNNB1 (β-catenin) activation—opposite faults in the same cadherin–catenin Wnt machinery."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Life after prophylactic gastrectomy: CDH1 carriers often undergo total gastrectomy, then manage dumping syndrome with dietary changes—small meals and soluble fibre to slow the rapid emptying of food into the small intestine."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver metastasis: diffuse gastric cancer drains via the portal vein to seed the hepatic lobule, one of the sites—with bone and lung—that mark incurable spread."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Marrow and bone metastasis: signet-ring diffuse gastric cancer characteristically seeds diffuse osteoblastic and bone-marrow metastases, sometimes presenting as marrow failure."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Lung and pleural spread: diffuse gastric cancer can disseminate to the lungs and pleura (lymphangitic carcinomatosis), seeding the alveolar bed and causing breathlessness."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "E-cadherin loss and diffuse growth: the CDH1/E-cadherin loss defining HDGC's signet-ring cancer also drives discohesive, infiltrative growth in other adenocarcinomas such as pancreatic cancer."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "EMT in adenocarcinoma: like HDGC's CDH1-driven discohesion, loss of E-cadherin and epithelial-mesenchymal transition mark invasion and spread in biliary adenocarcinomas like cholangiocarcinoma."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "E-cadherin loss and metastasis: as in the discohesive HDGC cancer, downregulation of E-cadherin (CDH1) signals the switch to invasive, metastatic disease in cancers such as prostate cancer."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Diffuse-type driver: FGFR2 amplification is characteristic of diffuse-type gastric cancer, a targetable lesion that can accompany the E-cadherin loss central to HDGC."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K activation: PIK3CA-driven PI3K signalling is common in diffuse gastric cancer, cooperating with CDH1 loss to promote the growth of these discohesive tumours."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Unleashed growth signalling: loss of E-cadherin de-represses receptor signalling such as MET, whose activation drives invasion in diffuse gastric cancer."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival signalling: PI3K/AKT activation downstream of PIK3CA cooperates with CDH1 loss in hereditary diffuse gastric cancer, sustaining the survival of discohesive signet-ring cells."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Invasive hypoxia: HIF-1α stabilised in the diffusely infiltrating tumour drives the angiogenesis and epithelial-mesenchymal features that aid its scattered, hard-to-detect spread."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative oncogene: MYC activation, released by loss of E-cadherin-mediated contact inhibition, drives the proliferation of hereditary diffuse gastric cancer cells."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "Junction-kinase activation: loss of E-cadherin at adherens junctions unleashes SRC-family kinase signalling, promoting the motility and scattered invasion of the signet-ring cells of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT reactivation maintains telomeres in hereditary diffuse gastric cancer cells, granting the limitless proliferation that complements the initiating CDH1 loss."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the desmoplastic stroma of diffuse gastric cancer, supporting the infiltrative growth of its scattered tumour cells."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Anoikis resistance: E-cadherin loss confers resistance to anoikis — the caspase-3-mediated apoptosis that normally kills cells detached from their neighbours — letting the discohesive signet-ring cells survive and disseminate."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo release: loss of E-cadherin-dependent contact inhibition frees YAP from Hippo-pathway restraint, driving the proliferative transcriptional programme in hereditary diffuse gastric cancer cells."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Peritoneal spread: the CXCL12-CXCR4 axis directs the discohesive cells of diffuse gastric cancer to the peritoneum, the transcoelomic dissemination behind the linitis plastica and peritoneal carcinomatosis that the syndrome causes."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Desmoplastic linitis plastica: the discohesive signet-ring cells of hereditary diffuse gastric cancer infiltrate diffusely and provoke a dense collagenous desmoplastic reaction, the fibrosis that stiffens the stomach wall into the classic 'leather-bottle' linitis plastica."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy targets: diffuse gastric cancers often express Claudin-18.2, and CAR-T and bispecific approaches against it aim to direct perforin-mediated cytotoxic killing at a tumour otherwise poorly responsive to checkpoint blockade."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Angiogenesis: VEGF-driven angiogenesis supports the growth and peritoneal spread of diffuse gastric cancer, the basis for the anti-VEGFR2 antibody ramucirumab used in advanced gastric cancer."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK convergence: HER2, MET and FGFR (all already mapped) funnel into the MAPK-ERK cascade, the proliferative hub of the diffuse gastric carcinoma that arises once E-cadherin is lost."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) sustaining growth and survival signalling in hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle output: the cyclin-D-CDK4/6 axis (with CDKN2A already mapped) releases E2F1 to drive the proliferation accompanying the E-cadherin-loss-initiated diffuse gastric tumour."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammatory cofactor: Helicobacter-pylori- and inflammation-driven TLR-MyD88-NF-κB signalling acts as an environmental cofactor accelerating gastric carcinogenesis in CDH1-mutation carriers."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "EMT cooperation: TGF-β-SMAD signalling (TGF-β already mapped) drives the epithelial-mesenchymal transition that, compounding the E-cadherin loss of HDGC, promotes the diffuse infiltrative growth of signet-ring carcinoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory microenvironment: IL-6-STAT3 signalling (STAT3 already mapped) sustains the inflammatory, pro-survival microenvironment of diffuse gastric carcinoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates cell-adhesion and anoikis resistance, processes central to the discohesive, infiltrative growth of E-cadherin-deficient hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK kinases transduce the IL-6 signal to STAT3 (IL-6 and STAT3 mapped), an inflammatory proliferative input in hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) supports survival and invasion in hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment of the CDH1-driven hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (CDKN2A already mapped) drives the cell-cycle progression of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) removes a tumor-suppressive brake in hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of the diffuse-type gastric cancer arising in CDH1 carriers."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the β-catenin (Wnt already mapped) and survival signaling dysregulated by E-cadherin (CDH1) loss in hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation is a common second-hit mechanism silencing the CDH1 promoter in hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the anoikis resistance and survival of the detached signet-ring cells of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the tumor microenvironment and metastatic interactions of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "E-cadherin loss and EMT: germline loss of E-cadherin (CDH1 already mapped) releases the epithelial brake on invasion, and AXL-driven epithelial-mesenchymal transition promotes the discohesive, infiltrative signet-ring growth that defines diffuse gastric cancer."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: MHC class II antigen presentation shapes the T-cell response in diffuse gastric cancer, relevant to the checkpoint-based therapies explored for these often microsatellite-stable but sometimes immunogenic tumours."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint blockade: PD-1 inhibitors are part of the systemic therapy for advanced diffuse gastric cancer, though the discohesive, stroma-rich histology of the CDH1-driven tumour tends to respond less than intestinal-type disease."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Occult bleeding: the diffusely infiltrating tumour of hereditary diffuse gastric cancer bleeds and impairs nutrition, and a falling haemoglobin with anaemia can be an early clue in a CDH1 carrier under surveillance."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) underlies the checkpoint response in diffuse gastric cancer, though the stroma-rich CDH1-driven tumour is often poorly immunogenic."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive stroma: IL-10 in the desmoplastic microenvironment (fibroblast already mapped) dampens anti-tumour immunity, part of why the diffuse, stroma-rich histology of CDH1-driven gastric cancer resists checkpoint blockade."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the desmoplastic stroma, part of the poorly immunogenic microenvironment of CDH1-driven diffuse gastric cancer."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: the diffuse gastric tumour and its stroma generate oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species add to the genomic instability and inflammation of the tumour."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 inflammation: cyclooxygenase-2 and prostaglandin E2 promote the proliferation, angiogenesis (VEGF already mapped) and immunosuppression of gastric carcinogenesis, part of the inflammatory milieu of the diffuse tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive microenvironment of hereditary diffuse gastric cancer."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Checkpoint immunotherapy: the cytotoxic T cells (PD-1 and perforin already mapped) are the target of the checkpoint immunotherapy explored in the diffuse gastric cancers, which the immunosuppressive stroma limits."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron-deficiency anaemia: the chronic occult bleeding of the diffuse, infiltrating gastric tumour causes the iron-deficiency anaemia (haemoglobin already mapped) common in hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic adipokine: leptin is the adipokine of the metabolic-inflammatory (IL-6 already mapped) milieu contributing to the diffuse gastric cancer of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine dimension: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic influence on the gastric cancer of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and, with the tumour bleeding, contributes to the anaemia (haemoglobin already mapped) of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic influence on the gastric cancer of hereditary diffuse gastric cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "HER2 ADCC: the NK cells mediate the antibody-dependent cellular cytotoxicity of the anti-HER2 (already mapped) trastuzumab against the HER2-positive diffuse gastric cancer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the (MSI/EBV subset) gastric cancer of HDGC."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the diffuse gastric cancer of HDGC."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the HDGC tumours."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the HDGC tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the HDGC tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the HDGC tumours."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the diffuse HDGC tumours."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the HDGC tumours."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the HDGC tumours."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the desmoplastic stroma of the diffuse HDGC tumours."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the desmoplastic HDGC tumour microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the HDGC tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Blood-loss/tumour iron: transferrin, the iron carrier, reflects the iron-deficiency anaemia of the gastric blood loss and the iron demand of the CDH1-mutant (already mapped) HDGC tumours."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-HDGC axis: TSLP, from the CDH1-mutant (already mapped) gastric epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of HDGC signet-ring-cell tumours."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-HDGC axis: bradykinin, via B1/B2 receptors on HDGC tumour endothelium (already mapped) and mast cells (already mapped), augments vascular permeability and the inflammatory milieu of the CDH1-deficient (already mapped) HDGC gastric stroma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-HDGC axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and iron-deficiency anaemia of HDGC, activates the EPOR on CDH1-mutant (already mapped) tumour cells and modulates macrophage (already mapped) polarisation in the HDGC microenvironment."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-HDGC axis: histamine, from mast cells in the CDH1-deficient (already mapped) HDGC gastric stroma, signals via H2 receptors on tumour cells and endothelium, modulating acid secretion, angiogenesis, and the pro-tumourigenic milieu of signet-ring-cell HDGC."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-HDGC axis: melatonin, produced by gastric enterochromaffin cells, suppresses CDH1-deficient (already mapped) tumour-cell proliferation, modulates H. pylori co-stimulatory oxidative stress, and enhances apoptotic sensitivity in HDGC signet-ring cells."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-HDGC axis: testosterone, via androgen receptor signalling on CDH1-mutant (already mapped) gastric tumour cells and stroma, modulates E-cadherin-loss-driven invasiveness and the sex-biased clinical presentation of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "HDGC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "HDGC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of hereditary diffuse gastric cancer."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "HDGC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of hereditary diffuse gastric cancer."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "HDGC selenium: selenium, via GPx in macrophages (already mapped) and mast cells (already mapped), scavenges ROS; selenium deficiency amplifies IL-6 (already mapped) and STAT3 (already mapped) tumour-promoting inflammation in hereditary diffuse gastric cancer."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "HDGC zinc: zinc cofactors macrophage (already mapped) anti-tumour function and T-cytotoxic (already mapped) cytotoxicity; zinc deficiency amplifies IL-6 (already mapped) and STAT3 (already mapped) tumour-promoting inflammation and impairs CDH1 (already mapped) signalling in HDGC."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "HDGC magnesium: magnesium supports macrophage (already mapped) anti-tumour resolution and mast-cell (already mapped) stability; magnesium deficiency amplifies IL-6 (already mapped) and TGF-β (already mapped) tumour-promoting inflammation and angiogenesis in HDGC."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "HDGC iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and mast-cell (already mapped) stability; iodine deficiency amplifies IL-6 (already mapped) and TGF-β (already mapped) tumour-promoting cascade of HDGC."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "HDGC sodium: high dietary sodium promotes macrophage (already mapped) M2-skewing and mast-cell (already mapped) activation; sodium-induced IL-6 (already mapped) and TGF-β (already mapped) amplifies tumour-promoting microenvironment of HDGC."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "HDGC copper: copper supports macrophage (already mapped) anti-tumour function and mast-cell (already mapped) regulation; copper deficiency amplifies IL-6 (already mapped) and TGF-β (already mapped) tumour-promoting cascade and angiogenesis in HDGC."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "HDGC chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) volume during tumour-microenvironment stress; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) in HDGC."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "HDGC nitrogen: nitrogen as backbone of oncoproteins and cytokines (already mapped) sustains tumour signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) in HDGC."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "HDGC phosphorus: phosphorus as ATP in macrophages (already mapped) and mast cells (already mapped) fuels anti-tumour kinase signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade in HDGC."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "HDGC carbon: carbon in nucleotides of macrophages (already mapped) and mast cells (already mapped) fuels tumour epithelial proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade in HDGC."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "HDGC hydrogen: hydrogen via ROS from macrophages (already mapped) and mast cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) tumour cascade in HDGC."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "HDGC potassium: potassium regulates macrophage (already mapped) and mast-cell (already mapped) membrane potential in tumour microenvironment; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade in HDGC."
---

# Hereditary Diffuse Gastric Cancer

## Overview

**Hereditary diffuse gastric cancer (HDGC)** is an autosomal dominant hereditary cancer predisposition syndrome defined by a predisposition to **diffuse-type gastric cancer (DGC)** — specifically the **signet ring cell carcinoma (SRCC)** histological subtype — and to **lobular breast carcinoma**. HDGC is caused by germline pathogenic variants in **CDH1** (E-cadherin; ~25-30% of HDGC probands) or **CTNNA1** (alpha-E-catenin; ~2-5%) or remains genetically uncharacterized in the majority of families meeting clinical criteria. CDH1 was established as the HDGC gene by Guilford et al. in 1998 in Māori families with clustering of diffuse gastric cancer; CTNNA1 was subsequently identified in CDH1-negative HDGC families by Majewski et al. in 2013. The HDGC germline prevalence is ~1 in 5,000-10,000 in populations with elevated gastric cancer background rates (East Asia, South America) and rarer in low-incidence populations [^van-der-post-2015-hdgc-guidelines] [^hansford-2015-hdgc].

**HDGC Clinical Criteria (IGCLC 2015, updated):**

Testing for CDH1 (and CTNNA1) is indicated in any of the following:
1. ≥2 cases of gastric cancer in family, any age, ≥1 confirmed diffuse type (or SRCC)
2. ≥1 case of diffuse gastric cancer at any age in a family with ≥1 case of lobular breast cancer (one diagnosed <50 years)
3. Individual diagnosed with diffuse gastric cancer at age <40 (no family history required)
4. Personal or family history of bilateral lobular breast cancer diagnosed <50 years
5. Personal history of SRCC in situ in otherwise healthy gastric mucosa

**Lifetime cancer risks by gene:**

| Cancer | CDH1 male | CDH1 female | CTNNA1 (estimated) |
|---|---|---|---|
| Diffuse gastric cancer | ~67-83% | ~56-83% | ~50-80% (limited data) |
| Lobular breast cancer | N/A | ~39-52% | Elevated (exact figure unclear) |
| Colorectal cancer | Modest elevation reported in some families | Same | Under investigation |

## Structure

### Genetic basis of HDGC

**CDH1 (E-cadherin; 16q22.1):**
- 16 exons; 882 aa; transmembrane cadherin; extracellular Ca²⁺-dependent homotypic adhesion; cytoplasmic tail binds CTNNB1 → CTNNA1 → F-actin
- Germline pathogenic variant spectrum: frameshift + nonsense (~25%), splice site (~20%), missense in EC domains (~20%), large deletions (~10%), promoter mutations (~5%), intronic variants with impact on splicing (~20%)
- Somatic second hit: LOH at 16q22 (CDH1 locus) in most HDGC tumor foci; methylation-driven silencing of the second CDH1 allele less common but described
- Phenotype: extremely high penetrance for diffuse GC (>80% by age 80 in white European HDGC families); lobular BC penetrance elevated in female carriers (~39-52% by age 80)
- Founder variants: Māori (c.1137G>A, p.=, exon 9 skipping); Northern Ireland and Newfoundland kindreds (specific splice and truncating variants)

**CTNNA1 (alpha-E-catenin; 5q31.2):**
- 9 exons encoding 906 aa; links CTNNB1-CDH1 complex to F-actin
- Germline pathogenic variant spectrum: frameshift, nonsense, splice site — LOF variants; missense variants of uncertain significance being classified
- Penetrance: estimated ~50-80% lifetime diffuse GC risk; data from smaller family cohorts than CDH1; prophylactic gastrectomies in CTNNA1 carriers reveal T1a SRCC foci confirming cancer susceptibility
- Lobular breast cancer elevation: biologically expected (same pathway as CDH1); clinical data accumulating from family registries

**Uncharacterized HDGC families (~65-70% of HDGC probands):**
- Despite meeting clinical criteria and negative CDH1/CTNNA1 testing, many HDGC families remain gene-negative
- Candidates: MAP3K6 (regulation of CDH1 expression; identified in some HDGC families); RhoA activating mutations (somatic in sporadic DGC but not established as germline HDGC genes); RHOA pathway genes; INSR; ongoing research
- Clinical management: same surveillance and prophylactic surgery recommendations as for CDH1/CTNNA1 variants in families with strong HDGC pedigrees

### Pathology — diffuse gastric cancer histology

**Lauren classification:**
- **Intestinal type** (~40% of GC): glandular; CDH1-retained; H. pylori → IM → dysplasia → adenocarcinoma; prevalent in East Asia; males > females
- **Diffuse type** (~35% of GC): signet ring cells and poorly cohesive carcinoma; CDH1/CTNNA1 lost; no glandular architecture; infiltrates stomach wall diffusely (linitis plastica in advanced cases)
- **Mixed type** (~15%)

**HDGC/SRCC histopathology:**
- Signet ring cell carcinoma: individual malignant cells with intracytoplasmic mucin vacuole displacing nucleus to periphery; no cell-cell adhesion (mimicking isolated cell invasion); linitis plastica when diffuse submucosal spread occurs
- In prophylactic gastrectomy specimens: multiple microscopic T1a SRCC foci (typically 2-100 foci) scattered throughout otherwise normal-appearing gastric mucosa; most common at the junction between gastric body and antrum (transition zone); atrophic mucosa, intestinal metaplasia, or dysplasia NOT present (HDGC lacks H. pylori pathway)
- Distinction from sporadic DGC: germline-driven HDGC has multifocal microscopic disease without pre-malignant mucosal changes; sporadic DGC may have H. pylori-associated atrophy in some cases

## Function

### Clinical management — HDGC

**Prophylactic total gastrectomy:**
- **Recommended for all CDH1 germline carriers** who have been adequately counseled; standard recommendation is gastrectomy between age 20-30 (after multidisciplinary counseling) or at an age 5-10 years before the earliest case in the family
- Evidence: ~90% of prophylactic gastrectomy specimens from CDH1 carriers contain at least one focus of T1a SRCC; this validates gastrectomy as life-saving even in asymptomatic carriers; most individuals who defer gastrectomy and develop advanced GC have stage III-IV disease due to insidious growth
- Surgical approach: total gastrectomy with Roux-en-Y esophagojejunostomy; D1+ or D2 lymphadenectomy; minimally invasive (laparoscopic) preferred at experienced centers
- Postoperative: dumping syndrome management (small meals, dietary modification); vitamin B12 IM supplementation (lifelong); iron, D, Ca²⁺ supplementation; nutritional counseling; weight management
- **CTNNA1 carriers**: prophylactic gastrectomy recommended following same CDH1 guidelines given equivalent penetrance estimates and confirmed SRCC foci in gastrectomy specimens

**Endoscopic surveillance (for carriers deferring gastrectomy):**
- Annual upper endoscopy with random biopsies from 6 sites (body, antrum, cardia/squamocolumnar junction) per Cambridge protocol
- Limitations: SRCC foci are submucous, pale, flat; easily missed on standard white-light endoscopy; magnification + narrow-band imaging + chromo-endoscopy (congo red + methylene blue) improve detection
- Consensus: endoscopic surveillance is **not equivalent to prophylactic gastrectomy** and should only be used for carriers who decline surgery or when surgery is contraindicated; not a substitute for gastrectomy
- Endoscopic surveillance schedule: annually from age 20 (or 5-10 years before earliest family case)

**Breast surveillance (female CDH1 and CTNNA1 carriers):**
- Lobular breast cancer elevated risk: CDH1 female carriers have ~39-52% lifetime risk; MRI is the primary modality (lobular BC is mammographically occult in ~30-40% of cases due to infiltrative growth pattern)
- Protocol: annual breast MRI ± mammography from age 30 (or 5-10 years before earliest family lobular BC)
- Risk-reducing options: bilateral prophylactic mastectomy (after gastrectomy); aromatase inhibitor or tamoxifen not validated specifically for CDH1-lobular BC prevention

**Genetic testing and counseling:**
- **Multigene panel recommended**: CDH1 + CTNNA1 + MAP3K6 ± other emerging genes
- Cascade testing: 50% offspring risk for CDH1/CTNNA1 pathogenic variants; first-degree relatives should undergo testing
- Prenatal/preimplantation: available for CDH1 pathogenic variants

## Pathology

### HDGC vs other hereditary GC syndromes

| Syndrome | Gene(s) | GC histology | GC risk | Other cancers |
|---|---|---|---|---|
| HDGC | CDH1, CTNNA1 | Diffuse/SRCC | ~67-83% (CDH1) | Lobular BC (CDH1 female ~50%) |
| Lynch syndrome | MLH1, MSH2, MSH6, PMS2 | Intestinal type | 5-13% | CRC, endometrial, ovarian |
| Hereditary intestinal GC | APC (FAP-associated), MUTYH | Intestinal | Moderate (in FAP context) | Colorectal polyps/cancer |
| Li-Fraumeni (TP53) | TP53 | Intestinal or diffuse | Slightly elevated | Sarcoma, breast, brain |
| Peutz-Jeghers (STK11) | STK11 | Intestinal | Elevated | GI polyps, sex cord tumors |
| Juvenile polyposis (SMAD4/BMPR1A) | SMAD4, BMPR1A | Intestinal | Elevated | Hamartomatous GI polyps |

**H. pylori and HDGC:**
- H. pylori is NOT the driver of CDH1/CTNNA1-germline HDGC (no H. pylori-associated IM or SPEM in prophylactic specimens); however, H. pylori eradication is still recommended as a general GC risk reduction measure in HDGC carriers, as co-infection may accelerate the somatic second hit
- Alcohol and smoking: may modify penetrance in HDGC (data limited); general risk reduction counseling appropriate

**Somatic CDH1 methylation in sporadic DGC:**
- ~50% of sporadic diffuse GC cases have somatic CDH1 promoter hypermethylation (epigenetic silencing of both alleles); this is distinct from germline mutation but produces identical loss of E-cadherin protein → same diffuse/SRCC histology; not hereditary
- HDGC vs sporadic DGC: IHC for E-cadherin protein (absent in both); germline testing required to distinguish

## Connections

- `connects-to` → **[CTNNA1](../../03-molecular/ctnna1/README.md)** — Germline CTNNA1 LOF causes HDGC in CDH1-negative families (~2-5% of HDGC); prophylactic gastrectomy is recommended for pathogenic CTNNA1 carriers; penetrance estimated similar to CDH1; somatic CTNNA1 serves as the second hit in CDH1-germline HDGC tumors.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Germline CDH1 pathogenic variants cause ~25-30% of HDGC; E-cadherin loss → diffuse signet ring cell carcinoma; prophylactic gastrectomy reveals T1a SRCC foci in ~90% of carriers; CDH1 also drives lobular breast cancer risk (~39-52% lifetime in female CDH1 carriers.
- `connects-to` → **[Gastric Cancer](../../07-system/gastric-cancer/README.md)** — HDGC is a hereditary form of diffuse-type gastric cancer (Lauren classification); signet ring cell histology; endoscopic surveillance is insufficient for SRCC → prophylactic gastrectomy preferred; CDH1/CTNNA1 germline accounts for ~1-3% of all GC globally.
- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — Female CDH1 germline carriers have ~39-52% lifetime lobular breast cancer risk; CTNNA1 carriers also have elevated lobular BC risk; annual breast MRI from age 30 recommended; lobular BC in HDGC families is driven by E-cadherin/alpha-catenin pathway loss in breast epithelium.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — HDGC seeds dozens of T1a signet-ring foci throughout normal-looking gastric mucosa (clustered at the body-antrum transition), invisible to white-light endoscopy; surveillance cannot reliably catch them, so prophylactic total gastrectomy is definitive for CDH1 carriers.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — E-cadherin anchors adherens junctions via its tail → β-catenin (CTNNB1) → α-catenin (CTNNA1) → F-actin; germline loss of CDH1 or CTNNA1 collapses this adhesion complex → poorly cohesive signet-ring cells; the same axis links HDGC to lobular breast cancer.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Lynch syndrome is the other major hereditary gastric cancer syndrome but contrasts sharply: MMR-deficient intestinal-type GC at ~5-13% risk, versus HDGC's diffuse signet-ring tumors at ~67-83%; histology and germline panel (CDH1/CTNNA1 vs MLH1/MSH2/MSH6/PMS2) separate them.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — HDGC and FAP are both dominant GI cancer syndromes but opposite in lesion: HDGC seeds the stomach with CDH1-driven signet-ring foci that form no polyps, while FAP carpets the colon with thousands of APC-driven adenomas — diffuse versus adenomatous, gastrectomy versus colectomy.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Peutz-Jeghers syndrome is another hereditary cause of gastric cancer, but via STK11/LKB1 hamartomatous polyps (and mucocutaneous pigmentation) rather than HDGC's CDH1 signet-ring foci; both raise gastric and breast cancer risk — distinct routes, hamartoma versus loss of cohesion.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — Juvenile polyposis syndrome (SMAD4 or BMPR1A) is a third hereditary gastric cancer syndrome, marked by hamartomatous juvenile polyps and, in SMAD4 carriers, massive gastric polyposis with elevated gastric cancer risk — contrasting HDGC's non-polypoid CDH1 signet-ring cancer.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Hereditary diffuse gastric cancer forces a drastic digestive-system decision: because CDH1 carriers develop scattered, endoscopically invisible signet-ring foci throughout the stomach, prophylactic total gastrectomy is recommended early, since screening cannot reliably catch it.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Hereditary diffuse gastric cancer arises from gastric epithelium losing adhesion: germline CDH1 (E-cadherin) loss lets individual epithelial cells detach and infiltrate as signet-ring cells without forming a mass, the diffuse linitis-plastica pattern that makes it hard to detect.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — CDH1 mutations carry a colorectal as well as gastric risk: HDGC families show excess signet-ring/diffuse-type colorectal cancers alongside lobular breast and diffuse gastric cancer, reflecting E-cadherin's role in epithelial adhesion across the gut—so colonoscopy is advised.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — HDGC and HBOC both raise inherited breast cancer risk through different genes: CDH1 loss in HDGC predisposes to lobular breast cancer, while BRCA1/2 loss in HBOC drives ductal/triple-negative breast and ovarian cancer—distinct genes and histologies.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — HDGC and esophageal adenocarcinoma both threaten the upper GI tract: CDH1-driven diffuse gastric cancer can extend into the gastroesophageal junction, overlapping with esophageal adenocarcinoma, so surveillance in CDH1 carriers must cover the distal esophagus too.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — HDGC and Cowden syndrome are both dominant cancer syndromes with prominent breast and GI risk but different drivers: CDH1 (cell adhesion) versus PTEN (PI3K-AKT)—HDGC gives diffuse gastric and lobular breast cancer, Cowden adds thyroid cancer and hamartomas.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — Helicobacter pylori matters even in CDH1-driven gastric cancer: while HDGC arises from inherited E-cadherin loss rather than infection, H. pylori adds carcinogenic inflammation, so eradicating it is recommended in CDH1 carriers to remove an avoidable second hit.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Losing E-cadherin in HDGC unleashes Wnt/beta-catenin signaling: CDH1 normally tethers beta-catenin at the membrane, so its loss frees beta-catenin to drive proliferation while destroying cell-cell adhesion—driving the diffuse spread of signet-ring cells.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Diffuse gastric cancer infiltrates through a fibroblast-rich stroma: lacking E-cadherin, signet-ring cells scatter singly through a desmoplastic wall (linitis plastica) rather than forming a mass—so the stomach stiffens diffusely and tumors hide from endoscopy.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — CDH1 mutation behind HDGC also drives lobular breast cancer: female carriers face a high lifetime risk of this diffuse breast tumor, so HDGC management includes breast MRI surveillance and consideration of risk-reducing mastectomy alongside prophylactic gastrectomy.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — HDGC can seed the ovary as a Krukenberg tumor: diffuse signet-ring gastric cancer characteristically metastasizes to both ovaries, so bilateral ovarian masses with signet-ring cells should prompt a search for an occult gastric primary.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Diffuse signet-ring gastric cancers like HDGC engage the immune system poorly: they tend to be microsatellite-stable with low mutational burden and an immunosuppressive stroma, so checkpoint immunotherapy works far less well than in intestinal-type gastric cancer.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Hereditary diffuse gastric cancer spreads through the stomach wall and lymphatics: signet-ring cells infiltrate diffusely (linitis plastica) and seed nodes and peritoneum without a mass, so it is often advanced when found—why carriers undergo prophylactic gastrectomy.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Diffuse gastric cancer freezes the stomach's smooth muscle: signet-ring infiltration and desmoplasia stiffen all layers into a rigid leather-bottle linitis plastica, so the muscular wall loses peristalsis and the stomach can no longer expand or empty normally.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy struggles against diffuse gastric cancer: the infiltrative, mobile stomach and scattered signet-ring cells make photon-beam targeting hard, so radiation plays a limited, mostly palliative role compared with surgery and chemotherapy.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — HDGC's other cancer is estrogen-driven lobular breast cancer: the same CDH1/E-cadherin loss that causes diffuse stomach cancer produces invasive lobular breast cancer, which is typically estrogen-receptor positive—so carriers need breast as well as stomach surveillance.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — Diffuse gastric cancer in HDGC is usually HER2-negative: unlike intestinal-type stomach tumors that can be HER2-amplified and treated with trastuzumab, the signet-ring cancers of CDH1 carriers lack this target, leaving chemotherapy and surgery.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — HDGC tumors hide among regulatory T cells: the scattered signet-ring cells sit in a desmoplastic, immunosuppressive stroma where Tregs blunt anti-tumor immunity, part of why diffuse gastric cancer is hard to treat once it spreads.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — HDGC's whole problem is calcium-dependent glue gone missing: E-cadherin (CDH1) needs calcium to bind cells together, so losing it dissolves cell-cell adhesion and lets the signet-ring cells scatter and infiltrate diffusely rather than form a lump.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages fill HDGC's dense stroma: tumor-associated macrophages in the desmoplastic, scattered-cell tumor promote invasion and suppress immunity, part of why diffuse gastric cancer is so hard to treat once it spreads through the wall.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta builds the fibrous, infiltrative stroma of HDGC: it drives the desmoplasia and EMT-like behavior that help the discohesive signet-ring cells spread, stiffening the stomach wall as in linitis plastica.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hereditary diffuse gastric cancer spreads silently to the liver: its scattered signet-ring cells seed the peritoneum and liver early, so metastasis is often present by the time the infiltrative tumor is found.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Hereditary diffuse gastric cancer recruits endothelial cells: as the discohesive tumor infiltrates, it drives angiogenesis through these vessel-lining cells to supply blood for its spread through the stomach wall.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Diffuse gastric cancer hides in a low-oxygen stroma: its dense desmoplastic tissue chokes off oxygen, and the hypoxia drives survival signaling and blunts drug delivery, helping the scattered cells resist therapy.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — The prophylactic gastrectomy that prevents HDGC leaves lasting deficiencies: without stomach acid and intrinsic factor, iron and B12 malabsorb, so lifelong supplementation is needed.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — HDGC's signet-ring cells spread across the peritoneum and can encase the bowel, the transcoelomic spread that makes diffuse gastric cancer so lethal once it escapes the stomach.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — HDGC scleroses the stomach: signet-ring cells provoke a dense desmoplastic fibrosis (linitis plastica) that stiffens the wall and hides the cancer from endoscopy until it is advanced.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows why HDGC spreads diffusely: losing E-cadherin, the cells let go of one another and scatter as lone signet-ring cells, each with a mucin vacuole shoving its nucleus to the rim, never forming glands.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Signet-ring gastric cancer can seep into the marrow: HDGC's diffuse cells infiltrate the bone marrow, triggering a microangiopathic anemia and a leukoerythroblastic blood picture in advanced disease.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — HDGC spreads to the lung: beyond the peritoneum and liver, its scattered cells seed pulmonary and lymphangitic metastases, marking the widespread disease that prophylactic gastrectomy aims to prevent.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody stain reveals the defect: loss of E-cadherin (CDH1) on immunohistochemistry betrays the scattered signet-ring cells of HDGC, the molecular hallmark that distinguishes this stealthy, non-mass-forming cancer.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Both the cancer and its prevention drain the red cells: the diffuse tumor bleeds slowly into iron-deficiency anemia, and the prophylactic total gastrectomy that cures the risk leaves patients short of B12 and iron for life.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Losing the stomach can later harm the nerves: without it, B12 absorption fails, so unless replaced, the deficiency can damage peripheral and spinal cord neurons into a subacute combined degeneration.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — After the stomach is removed, the gut is rebuilt: prophylactic total gastrectomy, done young in CDH1 carriers, joins the esophagus to a loop of jejunum, so the small intestine becomes the new reservoir and the site of the lifelong malabsorption that follows.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Life without a stomach burns off fat: total gastrectomy leaves carriers eating small, frequent meals with poor fat absorption, so significant weight loss and depleted adipocyte stores are an expected, lifelong consequence needing dietitian support.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Diffuse gastric cancer drives clotting: like other gastric adenocarcinomas its discohesive, mucin-producing cells trigger paraneoplastic thrombocytosis and a high risk of venous thromboembolism once the disease becomes invasive.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — p53 loss helps the diffuse tumor advance: after CDH1 starts the discohesive growth, TP53 mutation is a frequent secondary hit that lets the signet-ring cells progress to invasive, lethal cancer.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The signet-ring tumor hides from killer T cells: diffuse gastric cancer is typically immune-cold with sparse cytotoxic T-cell infiltration, part of why it responds poorly to the immunotherapy that helps other gastric cancers.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Gastric cancer crosses hereditary syndromes: stomach cancer also features in Li-Fraumeni's TP53 spectrum, so a young diffuse gastric cancer prompts a wider germline search beyond CDH1.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — The stomach's loss costs iron: bleeding from diffuse gastric cancer, and the prophylactic total gastrectomy that prevents it, both cause iron (and B12) deficiency anemia, a lasting consequence carriers manage for life.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — A second hit speeds the cancer: beyond the germline CDH1 loss, cooperating mutations such as CDKN2A inactivation help diffuse gastric cancer progress, part of the somatic events layered on the inherited defect.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Cancer and major surgery raise the clot risk: an established diffuse gastric cancer and the total gastrectomy that treats it both predispose to venous thromboembolism, needing perioperative prophylaxis.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Inflammation accelerates the E-cadherin-deficient stomach: IL-6/STAT3 signaling in the gastric mucosa adds a proliferative push to the loss of cell-cell adhesion from germline CDH1 inactivation that drives diffuse gastric cancer.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Prophylactic gastrectomy carries surgical risk: CDH1 carriers often undergo risk-reducing total gastrectomy, whose anastomotic leak and infection can seed intra-abdominal sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Loss of the stomach drains the blood in many ways: beyond tumor bleeding and B12 malabsorption after gastrectomy, the inflammatory cytokines of the cancer add an anemia of chronic disease.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Removing the stomach costs the bones: total gastrectomy impairs absorption of calcium and vitamin D and disrupts gut hormones, so metabolic bone disease and osteoporosis are recognized long-term consequences.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A drastic preventive choice weighs on the mind: facing a high inherited risk of an aggressive stomach cancer, and choosing prophylactic total gastrectomy with its lifelong eating changes, carries a heavy psychological burden.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Advanced disease and its chemo strain the kidney: the platinum chemotherapy for diffuse gastric cancer is nephrotoxic, and poor intake after gastrectomy adds dehydration, together risking chronic kidney disease.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A genetic verdict and prophylactic gastrectomy breed worry: CDH1 carriers face the decision to remove a healthy stomach and lifelong cancer risk, fostering profound health anxiety.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Total gastrectomy is a major wound to heal: the prophylactic or therapeutic removal of the entire stomach creates a high-risk esophageal anastomosis prone to leak and slow healing.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Surgery, chemo and B12 loss injure nerves: post-gastrectomy adhesive pain, platinum chemotherapy neuropathy and the B12 deficiency of an absent stomach combine to produce neuropathic pain.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Losing the stomach upends metabolism: prophylactic total gastrectomy in HDGC removes ghrelin-producing tissue and causes dumping syndrome with reactive hypoglycaemia and lasting nutritional disturbance.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Malabsorption after gastrectomy weakens bone and muscle: the impaired calcium, vitamin D and protein uptake of an absent stomach causes metabolic bone disease and sarcopenia in HDGC survivors.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Vitamin B12 loss can degrade the spinal cord: with no stomach to make intrinsic factor, untreated B12 deficiency after gastrectomy causes subacute combined degeneration with sensory and cognitive decline.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its gene also binds skin cells: CDH1 encodes E-cadherin, a cell-adhesion protein of epithelia and skin, and some CDH1 families carry cleft lip and palate alongside their cancer risk.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Diffuse spread reaches the chest: signet-ring gastric cancer disseminates transcoelomically to the peritoneum and can seed the pleura, causing malignant effusions and breathlessness.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Life after total gastrectomy strains the circulation: dumping syndrome causes postprandial tachycardia, sweating and hypotension as food rushes into the small bowel.
- `connects-to` → **[MUTYH-associated Polyposis](../mutyh-associated-polyposis/README.md)** — A fellow inherited gastrointestinal-cancer syndrome: like MUTYH-associated polyposis, HDGC drives early gastrointestinal cancer needing intensive surveillance, the two entering the hereditary-GI-cancer differential.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Prophylactic surgery disturbs nutrition: the total gastrectomy that removes HDGC risk impairs absorption of vitamin D, calcium and B12, requiring lifelong supplementation.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Loss of the stomach drains minerals: after risk-reducing gastrectomy, impaired gastric acid and absorption deplete iron and zinc, contributing to anaemia and poor healing.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for the diffuse cancer that escapes surgery: advanced signet-ring diffuse gastric cancer is treated with FLOT-type chemotherapy, though this discohesive subtype responds relatively poorly.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Claudin-18.2 offers a target: diffuse gastric cancers often express Claudin-18.2, and the antibody zolbetuximab added to chemotherapy improves survival in this otherwise hard-to-target subtype.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy for advanced disease: PD-1 inhibitors added to chemotherapy treat advanced gastric cancer, with benefit concentrated in MSI-high and PD-L1-high tumours.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Knudson's two-hit model in the stomach: CDH1 is a tumour-suppressor inactivated like RB1—a germline first hit plus somatic loss (often promoter methylation) of the second allele—so HDGC mirrors retinoblastoma's founding mechanism of hereditary cancer.
- `connects-to` → **[Desmoid Tumor](../desmoid-tumor/README.md)** — Two diseases of one adhesion complex: HDGC can arise from CTNNA1 (α-catenin) loss that breaks E-cadherin cell adhesion, while desmoid tumours arise from CTNNB1 (β-catenin) activation—opposite faults in the same cadherin–catenin Wnt machinery.
- `connects-to` → **[Dietary Fiber](../../../03-medicine/03-food/dietary-fiber/README.md)** — Life after prophylactic gastrectomy: CDH1 carriers often undergo total gastrectomy, then manage dumping syndrome with dietary changes—small meals and soluble fibre to slow the rapid emptying of food into the small intestine.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver metastasis: diffuse gastric cancer drains via the portal vein to seed the hepatic lobule, one of the sites—with bone and lung—that mark incurable spread.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Marrow and bone metastasis: signet-ring diffuse gastric cancer characteristically seeds diffuse osteoblastic and bone-marrow metastases, sometimes presenting as marrow failure.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Lung and pleural spread: diffuse gastric cancer can disseminate to the lungs and pleura (lymphangitic carcinomatosis), seeding the alveolar bed and causing breathlessness.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — E-cadherin loss and diffuse growth: the CDH1/E-cadherin loss defining HDGC's signet-ring cancer also drives discohesive, infiltrative growth in other adenocarcinomas such as pancreatic cancer.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — EMT in adenocarcinoma: like HDGC's CDH1-driven discohesion, loss of E-cadherin and epithelial-mesenchymal transition mark invasion and spread in biliary adenocarcinomas like cholangiocarcinoma.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — E-cadherin loss and metastasis: as in the discohesive HDGC cancer, downregulation of E-cadherin (CDH1) signals the switch to invasive, metastatic disease in cancers such as prostate cancer.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Diffuse-type driver: FGFR2 amplification is characteristic of diffuse-type gastric cancer, a targetable lesion that can accompany the E-cadherin loss central to HDGC.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K activation: PIK3CA-driven PI3K signalling is common in diffuse gastric cancer, cooperating with CDH1 loss to promote the growth of these discohesive tumours.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Unleashed growth signalling: loss of E-cadherin de-represses receptor signalling such as MET, whose activation drives invasion in diffuse gastric cancer.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Survival signalling: PI3K/AKT activation downstream of PIK3CA cooperates with CDH1 loss in hereditary diffuse gastric cancer, sustaining the survival of discohesive signet-ring cells.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Invasive hypoxia: HIF-1α stabilised in the diffusely infiltrating tumour drives the angiogenesis and epithelial-mesenchymal features that aid its scattered, hard-to-detect spread.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative oncogene: MYC activation, released by loss of E-cadherin-mediated contact inhibition, drives the proliferation of hereditary diffuse gastric cancer cells.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — Junction-kinase activation: loss of E-cadherin at adherens junctions unleashes SRC-family kinase signalling, promoting the motility and scattered invasion of the signet-ring cells of hereditary diffuse gastric cancer.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT reactivation maintains telomeres in hereditary diffuse gastric cancer cells, granting the limitless proliferation that complements the initiating CDH1 loss.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the desmoplastic stroma of diffuse gastric cancer, supporting the infiltrative growth of its scattered tumour cells.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — E-cadherin loss confers resistance to anoikis—the caspase-3-mediated apoptosis that normally kills cells detached from their neighbors—letting the discohesive signet-ring cells of HDGC survive and disseminate freely.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Loss of E-cadherin-dependent contact inhibition frees YAP from Hippo-pathway restraint, driving the proliferative transcriptional program in hereditary diffuse gastric cancer cells beyond the loss of adhesion itself.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — The CXCL12-CXCR4 axis directs the discohesive cells of diffuse gastric cancer to the peritoneum, the transcoelomic dissemination behind the linitis plastica and peritoneal carcinomatosis that the syndrome causes.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — The discohesive signet-ring cells of hereditary diffuse gastric cancer infiltrate diffusely and provoke a dense collagenous desmoplastic reaction, the fibrosis that stiffens the stomach wall into the classic "leather-bottle" linitis plastica.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Diffuse gastric cancers often express Claudin-18.2, and CAR-T and bispecific approaches against it aim to direct perforin-mediated cytotoxic killing at a tumor otherwise poorly responsive to checkpoint blockade.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis supports the growth and peritoneal spread of diffuse gastric cancer, the basis for the anti-VEGFR2 antibody ramucirumab used in advanced gastric cancer.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — HER2, MET and FGFR (all already mapped) funnel into the MAPK-ERK cascade, the proliferative hub of the diffuse gastric carcinoma that arises once E-cadherin is lost.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) sustaining growth and survival signaling in hereditary diffuse gastric cancer.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis (with CDKN2A already mapped) releases E2F1 to drive the proliferation accompanying the E-cadherin-loss-initiated diffuse gastric tumor.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Helicobacter-pylori- and inflammation-driven TLR-MyD88-NF-κB signaling acts as an environmental cofactor accelerating gastric carcinogenesis in CDH1-mutation carriers.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the epithelial-mesenchymal transition that, compounding the E-cadherin loss of HDGC, promotes the diffuse infiltrative growth of signet-ring carcinoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) sustains the inflammatory, pro-survival microenvironment of diffuse gastric carcinoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates cell-adhesion and anoikis resistance, processes central to the discohesive, infiltrative growth of E-cadherin-deficient hereditary diffuse gastric cancer.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK kinases transduce the IL-6 signal to STAT3 (IL-6 and STAT3 mapped), an inflammatory proliferative input in hereditary diffuse gastric cancer.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) supports survival and invasion in hereditary diffuse gastric cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of hereditary diffuse gastric cancer.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment of the CDH1-driven hereditary diffuse gastric cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (CDKN2A already mapped) drives the cell-cycle progression of hereditary diffuse gastric cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) removes a tumor-suppressive brake in hereditary diffuse gastric cancer.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in hereditary diffuse gastric cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of the diffuse-type gastric cancer arising in CDH1 carriers.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the β-catenin (Wnt already mapped) and survival signaling dysregulated by E-cadherin (CDH1) loss in hereditary diffuse gastric cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation is a common second-hit mechanism silencing the CDH1 promoter in hereditary diffuse gastric cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the anoikis resistance and survival of the detached signet-ring cells of hereditary diffuse gastric cancer.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of hereditary diffuse gastric cancer.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of hereditary diffuse gastric cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of hereditary diffuse gastric cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of hereditary diffuse gastric cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of hereditary diffuse gastric cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of hereditary diffuse gastric cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of hereditary diffuse gastric cancer.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of hereditary diffuse gastric cancer.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the tumor microenvironment and metastatic interactions of hereditary diffuse gastric cancer.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — E-cadherin loss and EMT: germline loss of E-cadherin (CDH1 already mapped) releases the epithelial brake on invasion, and AXL-driven epithelial-mesenchymal transition promotes the discohesive, infiltrative signet-ring growth that defines diffuse gastric cancer.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: MHC class II antigen presentation shapes the T-cell response in diffuse gastric cancer, relevant to the checkpoint-based therapies explored for these often microsatellite-stable but sometimes immunogenic tumours.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint blockade: PD-1 inhibitors are part of the systemic therapy for advanced diffuse gastric cancer, though the discohesive, stroma-rich histology of the CDH1-driven tumour tends to respond less than intestinal-type disease.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Occult bleeding: the diffusely infiltrating tumour of hereditary diffuse gastric cancer bleeds and impairs nutrition, and a falling haemoglobin with anaemia can be an early clue in a CDH1 carrier under surveillance.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) underlies the checkpoint response in diffuse gastric cancer, though the stroma-rich CDH1-driven tumour is often poorly immunogenic.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive stroma: IL-10 in the desmoplastic microenvironment (fibroblast already mapped) dampens anti-tumour immunity, part of why the diffuse, stroma-rich histology of CDH1-driven gastric cancer resists checkpoint blockade.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the desmoplastic stroma, part of the poorly immunogenic microenvironment of CDH1-driven diffuse gastric cancer.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: the diffuse gastric tumour and its stroma generate oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species add to the genomic instability and inflammation of the tumour.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 inflammation: cyclooxygenase-2 and prostaglandin E2 promote the proliferation, angiogenesis (VEGF already mapped) and immunosuppression of gastric carcinogenesis, part of the inflammatory milieu of the diffuse tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive microenvironment of hereditary diffuse gastric cancer.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Checkpoint immunotherapy: the cytotoxic T cells (PD-1 and perforin already mapped) are the target of the checkpoint immunotherapy explored in the diffuse gastric cancers, which the immunosuppressive stroma limits.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron-deficiency anaemia: the chronic occult bleeding of the diffuse, infiltrating gastric tumour causes the iron-deficiency anaemia (haemoglobin already mapped) common in hereditary diffuse gastric cancer.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic adipokine: leptin is the adipokine of the metabolic-inflammatory (IL-6 already mapped) milieu contributing to the diffuse gastric cancer of hereditary diffuse gastric cancer.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine dimension: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic influence on the gastric cancer of hereditary diffuse gastric cancer.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and, with the tumour bleeding, contributes to the anaemia (haemoglobin already mapped) of hereditary diffuse gastric cancer.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic influence on the gastric cancer of hereditary diffuse gastric cancer.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — HER2 ADCC: the NK cells mediate the antibody-dependent cellular cytotoxicity of the anti-HER2 (already mapped) trastuzumab against the HER2-positive diffuse gastric cancer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the (MSI/EBV subset) gastric cancer of HDGC.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity of the diffuse gastric cancer of HDGC.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the HDGC tumours.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the HDGC tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the HDGC tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the HDGC tumours.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of the diffuse HDGC tumours.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the HDGC tumours.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the HDGC tumours.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the desmoplastic stroma of the diffuse HDGC tumours.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the desmoplastic HDGC tumour microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the HDGC tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Blood-loss/tumour iron: transferrin, the iron carrier, reflects the iron-deficiency anaemia of the gastric blood loss and the iron demand of the CDH1-mutant (already mapped) HDGC tumours.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-HDGC axis: TSLP, from the CDH1-mutant (already mapped) gastric epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of HDGC signet-ring-cell tumours.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-HDGC axis: bradykinin, via B1/B2 receptors on HDGC tumour endothelium (already mapped) and mast cells (already mapped), augments vascular permeability and the inflammatory milieu of the CDH1-deficient (already mapped) HDGC gastric stroma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-HDGC axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and iron-deficiency anaemia of HDGC, activates the EPOR on CDH1-mutant (already mapped) tumour cells and modulates macrophage (already mapped) polarisation in the HDGC microenvironment.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-HDGC axis: histamine, from mast cells in the CDH1-deficient (already mapped) HDGC gastric stroma, signals via H2 receptors on tumour cells and endothelium, modulating acid secretion, angiogenesis, and the pro-tumourigenic milieu of signet-ring-cell HDGC.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-HDGC axis: melatonin, produced by gastric enterochromaffin cells, suppresses CDH1-deficient (already mapped) tumour-cell proliferation, modulates H. pylori co-stimulatory oxidative stress, and enhances apoptotic sensitivity in HDGC signet-ring cells.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-HDGC axis: testosterone, via androgen receptor signalling on CDH1-mutant (already mapped) gastric tumour cells and stroma, modulates E-cadherin-loss-driven invasiveness and the sex-biased clinical presentation of hereditary diffuse gastric cancer.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — HDGC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of hereditary diffuse gastric cancer.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — HDGC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of hereditary diffuse gastric cancer.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — HDGC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of hereditary diffuse gastric cancer.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — HDGC selenium: selenium, via GPx in macrophages (already mapped) and mast cells (already mapped), scavenges ROS; selenium deficiency amplifies IL-6 (already mapped) and STAT3 (already mapped) tumour-promoting inflammation in hereditary diffuse gastric cancer.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — HDGC zinc: zinc cofactors macrophage (already mapped) anti-tumour function and T-cytotoxic (already mapped) cytotoxicity; zinc deficiency amplifies IL-6 (already mapped) and STAT3 (already mapped) tumour-promoting inflammation and impairs CDH1 (already mapped) signalling in HDGC.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — HDGC magnesium: magnesium supports macrophage (already mapped) anti-tumour resolution and mast-cell (already mapped) stability; magnesium deficiency amplifies IL-6 (already mapped) and TGF-β (already mapped) tumour-promoting inflammation and angiogenesis in HDGC.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — HDGC iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and mast-cell (already mapped) stability; iodine deficiency amplifies IL-6 (already mapped) and TGF-β (already mapped) tumour-promoting cascade of HDGC.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — HDGC sodium: high dietary sodium promotes macrophage (already mapped) M2-skewing and mast-cell (already mapped) activation; sodium-induced IL-6 (already mapped) and TGF-β (already mapped) amplifies tumour-promoting microenvironment of HDGC.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — HDGC copper: copper supports macrophage (already mapped) anti-tumour function and mast-cell (already mapped) regulation; copper deficiency amplifies IL-6 (already mapped) and TGF-β (already mapped) tumour-promoting cascade and angiogenesis in HDGC.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — HDGC chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) volume during tumour-microenvironment stress; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) in HDGC.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — HDGC nitrogen: nitrogen as backbone of oncoproteins and cytokines (already mapped) sustains tumour signalling; nitrogen-derived RNS from macrophages (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) in HDGC.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — HDGC phosphorus: phosphorus as ATP in macrophages (already mapped) and mast cells (already mapped) fuels anti-tumour kinase signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade in HDGC.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — HDGC carbon: carbon in nucleotides of macrophages (already mapped) and mast cells (already mapped) fuels tumour epithelial proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade in HDGC.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — HDGC hydrogen: hydrogen via ROS from macrophages (already mapped) and mast cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) tumour cascade in HDGC.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — HDGC potassium: potassium regulates macrophage (already mapped) and mast-cell (already mapped) membrane potential in tumour microenvironment; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) cascade in HDGC.

[^van-der-post-2015-hdgc-guidelines]: van der Post RS, Vogelaar IP, Carneiro F, et al. Hereditary diffuse gastric cancer: updated clinical guidelines with an emphasis on germline CDH1 mutation carriers. *J Med Genet.* 2015;52(6):361-374. [doi:10.1136/jmedgenet-2015-103094](https://doi.org/10.1136/jmedgenet-2015-103094) · [PubMed 25979631](https://pubmed.ncbi.nlm.nih.gov/25979631/)
[^hansford-2015-hdgc]: Hansford S, Kaurah P, Li-Chang H, et al. Hereditary Diffuse Gastric Cancer Syndrome: CDH1 Mutations and Beyond. *JAMA Oncol.* 2015;1(1):23-32. [doi:10.1001/jamaoncol.2014.168](https://doi.org/10.1001/jamaoncol.2014.168) · [PubMed 26182300](https://pubmed.ncbi.nlm.nih.gov/26182300/)
