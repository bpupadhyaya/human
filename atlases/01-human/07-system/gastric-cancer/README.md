---
schema: human-scale-entry/v1
id: gastric-cancer
name: Gastric Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "HER2 overexpression (~15-20%) and MSI-H (~10-15%) define actionable subsets; pembrolizumab is first-line for PD-L1+ gastric cancer; trastuzumab+chemotherapy is standard for HER2+ disease; ramucirumab (VEGFR2) and zolbetuximab (CLDN18.2) are approved in later lines."
aliases: ["gastric cancer", "stomach cancer", "gastric adenocarcinoma", "GEJ cancer", "gastroesophageal junction cancer", "gastric carcinoma", "GC"]
sources:
  - id: bang-2010-toga
    type: peer-reviewed
    cite: "Bang YJ, Van Cutsem E, Feyereislova A, et al. Trastuzumab in combination with chemotherapy versus chemotherapy alone for treatment of HER2-positive advanced gastric or gastro-oesophageal junction cancer (ToGA): a phase 3, open-label, randomised controlled trial. Lancet. 2010;376(9742):687-697."
    doi: "10.1016/S0140-6736(10)61121-X"
    pmid: "20728210"
    url: "https://doi.org/10.1016/S0140-6736(10)61121-X"
  - id: janjigian-2021-checkmate649
    type: peer-reviewed
    cite: "Janjigian YY, Shitara K, Moehler M, et al. First-line nivolumab plus chemotherapy versus chemotherapy alone for advanced gastric, gastro-oesophageal junction, and oesophageal adenocarcinoma (CheckMate 649). Lancet. 2021;398(10294):27-40."
    doi: "10.1016/S0140-6736(21)00797-2"
    pmid: "34102137"
    url: "https://doi.org/10.1016/S0140-6736(21)00797-2"
cross_links:
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "HER2 overexpression in ~15-20% of gastric/GEJ cancer; trastuzumab+cisplatin+fluoropyrimidine is first-line for HER2+ disease (ToGA trial); T-DXd (trastuzumab deruxtecan) active in HER2-low and HER2-overexpressing gastric cancer (DESTINY-Gastric01)."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ramucirumab (anti-VEGFR2) + paclitaxel is standard second-line for advanced gastric cancer (RAINBOW trial: OS 9.6 vs. 7.4 months); ramucirumab monotherapy also approved; bevacizumab failed to improve OS in AVAGAST; VEGFR2 is the validated antiangiogenic target in gastric cancer."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Pembrolizumab + chemotherapy is first-line for PD-L1 CPS ≥5 advanced gastric/GEJ adenocarcinoma (KEYNOTE-590/811); nivolumab + chemotherapy approved in many regions (CheckMate 649); MSI-H/dMMR gastric cancer (~10-15%) has particularly high response to PD-1 blockade (ORR >40%)."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR overexpression in ~30-40% of gastric cancer but EGFR-targeted therapy (cetuximab, panitumumab) failed in unselected gastric cancer trials; EGFR amplification in a subset → potential biomarker; FGFR2 amplification (~5-10%) responds to bemarituzumab (anti-FGFR2b)."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "H. pylori is the dominant cause of non-cardia intestinal-type gastric cancer via the Correa cascade (gastritis → atrophy → metaplasia → dysplasia → carcinoma); CagA hijacks SHP-2/RAS-ERK and disrupts E-cadherin/β-catenin; eradication cuts GC incidence ~35-40%."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV defines a distinct ~9% gastric cancer subtype (TCGA) with viral integration, near-universal PIK3CA mutation, CDKN2A silencing, and amplified CD274/PDCD1LG2 → very high PD-L1 → strong response to PD-1 blockade; EBER in-situ hybridization confirms it."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "Germline CDH1 (E-cadherin) loss causes hereditary diffuse gastric cancer — signet-ring/poorly cohesive tumors with ~70% lifetime diffuse-GC risk plus elevated lobular breast cancer risk; prophylactic total gastrectomy is recommended for CDH1 carriers aged 18-40."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Gastric cancer and cholangiocarcinoma are GI adenocarcinomas sharing actionable targets — HER2, PD-1/PD-L1, and FGFR2 — but arise differently: gastric cancer from stomach epithelium (H. pylori, EBV, germline CDH1), CCA from biliary cholangiocytes (FGFR2 fusions, IDH1 mutations)."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Gastric cancer arises from the stomach's mucosal epithelium, usually via the Correa cascade of H. pylori gastritis → atrophy → metaplasia → dysplasia → intestinal-type carcinoma; the diffuse type (CDH1 loss) instead infiltrates the wall as signet-ring cells (linitis plastica)."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Gastric and esophageal cancers merge at the gastroesophageal junction, where Siewert-classified adenocarcinomas are treated as one entity; both share HER2 amplification, PD-1 blockade, and reflux/obesity risk, while distal gastric and esophageal squamous cancers diverge by cause."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Gastric and colorectal cancer are both GI adenocarcinomas sharing pathways and predispositions: microsatellite-unstable subtypes of each respond to checkpoint inhibitors, both arise in Lynch syndrome, and both are screened by endoscopy where incidence is high."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Gastric cancer is part of the Lynch syndrome tumor spectrum: germline mismatch-repair mutations raise gastric (especially intestinal-type) cancer risk alongside colorectal and endometrial cancer, so MMR/MSI testing and upper endoscopic surveillance are warranted in carriers."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Iron-deficiency anemia is a classic presenting sign of gastric cancer: chronic occult blood loss from an ulcerated tumor (and impaired absorption from atrophic gastritis) depletes iron, so unexplained IDA—especially in older adults—mandates upper endoscopy to exclude it."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Gastric cancer is part of the FAP tumor spectrum: APC-driven polyposis extends beyond the colon to the stomach, where fundic-gland polyps and gastric adenomas raise cancer risk and warrant upper-GI surveillance—one germline mutation reshaping the gut's risk."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "Gastric cancer and GIST are the two main stomach tumors but from different cells: carcinoma arises from glandular epithelium (H. pylori, CDH1), GIST from KIT-mutant interstitial cells of Cajal, the gut pacemaker—epithelial versus mesenchymal, very different therapy."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "CDH1 (E-cadherin) loss defines diffuse gastric cancer: without this adhesion molecule cells scatter through the stomach wall as linitis plastica rather than a mass, and germline CDH1 mutation drives hereditary diffuse gastric cancer—prompting prophylactic gastrectomy."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation is among the commonest events in gastric cancer: loss of p53 removes a key checkpoint as H. pylori-driven inflammation and intestinal metaplasia progress to carcinoma, so p53 inactivation marks the late, invasive stage of the Correa cascade."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS and related signaling drive a subset of gastric cancers: activating mutations push proliferation in intestinal-type tumors, contributing to the molecular diversity (alongside HER2, EBV, MSI) that increasingly guides targeted gastric cancer therapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages shape gastric cancer: recruited into the tumor, they promote invasion, angiogenesis and immune suppression, and high macrophage infiltration predicts worse outcome—part of the microenvironment seeded by chronic H. pylori gastritis."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Gastric cancer is a major cancer of the digestive system: it arises in the stomach lining often after H. pylori gastritis and intestinal metaplasia, and vague early symptoms mean it usually presents late—making it a leading cause of cancer death worldwide."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Gastric cancer often follows a metaplastic change in the gut epithelium: chronic inflammation drives the stomach lining toward an intestinal-type epithelium (intestinal metaplasia), a recognized precancerous step in the Correa cascade from gastritis to carcinoma."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy has a role in gastric cancer: photon-beam radiation combined with chemotherapy is used before or after surgery to improve local control of resectable tumors and to palliate bleeding or obstruction in advanced disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Gastric cancer subsets respond to T-cell immunotherapy: EBV-positive and MSI-high tumors are richly infiltrated by cytotoxic T cells and respond to checkpoint inhibitors, so molecular subtyping now guides who gets immunotherapy."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is gastric cancer's main metastatic target: tumor cells drain via the portal vein to seed the liver, so hepatic metastases mark incurable disease and shift treatment from surgery to systemic chemo-immunotherapy."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "Gastric cancer can masquerade as ovarian cancer: signet-ring cells spread to the ovaries as Krukenberg tumors, so bilateral ovarian masses in a woman may actually be metastatic stomach cancer—a crucial diagnostic catch."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Dietary salt is a major driver of gastric cancer: high sodium intake damages the stomach lining and promotes H. pylori colonization and carcinogenesis, which is why salt-heavy diets track with the world's highest stomach cancer rates."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Diffuse gastric cancer is often driven by FGFR2: amplification of this receptor fuels the aggressive signet-ring type, making FGFR inhibitors a targeted option beyond the HER2-directed drugs used in intestinal-type tumors."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Diffuse gastric cancer turns the stomach to leather through fibroblasts: cancer-associated fibroblasts lay down dense stroma in linitis plastica, stiffening the whole stomach wall and helping the scattered signet-ring cells resist therapy."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Nitrogen-based nitrosamines help cause gastric cancer: salted, smoked and pickled foods, and nitrate converted by stomach bacteria, generate DNA-damaging N-nitroso compounds, a dietary driver that compounds Helicobacter infection."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Helicobacter drives gastric cancer through NF-kB: the infection keeps this inflammatory switch active in the stomach lining, sustaining the chronic gastritis and survival signaling that step the mucosa toward malignancy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Helicobacter recruits regulatory T cells that shield gastric cancer: the bacterium induces Tregs that dampen the immune attack, letting infection persist and the tumor evade clearance, while blunting checkpoint-therapy responses."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Gastric cancer bleeds away iron: the tumor oozes blood into the stomach, so a slow, painless iron-deficiency anemia is often the first clue, especially in older patients."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Gastric cancer invades the neighboring pancreas: as it grows through the stomach wall, the tumor can reach the adjacent pancreas, a local spread that signals advanced, often unresectable disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Diffuse gastric cancer turns the stomach to fibrosis: signet-ring cells provoke a dense desmoplastic reaction (linitis plastica) that stiffens the whole stomach wall into a rigid 'leather bottle.'"
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Gastric cancer is fed by new vessels: VEGF recruits endothelial cells, and ramucirumab, an anti-VEGFR2 antibody, is a mainstay of advanced disease that starves the tumor of its blood supply."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Gastric cancer seeds the abdomen: signet-ring cells spread across the peritoneum and can encase the bowel, and ovarian Krukenberg deposits mark this transcoelomic spread."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Gastric cancer can invade the marrow: diffuse signet-ring disease is a classic cause of cancer-associated microangiopathy and a leukoerythroblastic blood picture from marrow infiltration."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals gastric cancer's signet-ring cell: a mucin vacuole so large it shoves the nucleus to a crescent at the cell's rim, the hallmark of the diffuse type that stiffens the stomach into linitis plastica."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Gastric cancer signals through the skin: the velvety dark patches of paraneoplastic acanthosis nigricans and a hard umbilical 'Sister Mary Joseph' nodule from peritoneal spread can be the first outward signs of the hidden tumor."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Gastric cancer spreads to the lung: beyond the liver and peritoneum, hematogenous metastases and lymphangitic spread reach the lungs, a marker of the advanced disease that surgery can no longer cure."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies target gastric cancer's surface markers: trastuzumab against HER2, the checkpoint antibodies pembrolizumab and nivolumab, and zolbetuximab against claudin-18.2 now extend survival in selected advanced tumors."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Gastric cancer bleeds and starves the red cells: chronic oozing causes iron-deficiency anemia that is often the first clue, and autoimmune atrophic gastritis can add a B12-deficient pernicious anemia."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The chemotherapy frays the nerves: the cisplatin and oxaliplatin backbones of gastric cancer regimens injure peripheral sensory neurons into a cold-triggered, dose-limiting neuropathy."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Gastric cancer can drop seeds in the ovary: signet-ring cells spreading through the peritoneum implant on the ovaries as Krukenberg tumors, sometimes the presenting finding in a young woman whose stomach primary is still silent."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "A minority of gastric cancers are MET-driven: amplification or overexpression of the MET receptor marks aggressive, fast-spreading tumors and a poor prognosis, an actionable target probed by MET-directed therapies."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Gastric adenocarcinoma is a classic clot-maker: its mucin-secreting cells trigger paraneoplastic thrombocytosis and the migratory thrombophlebitis of Trousseau syndrome, driving a high rate of venous thromboembolism."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K signaling drives a major subtype: PIK3CA mutations are common in gastric cancer, especially the Epstein-Barr-virus-positive group, switching on the AKT growth pathway and marking a targetable vulnerability."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "How the tumor handles antigen decides immunotherapy's reach: dendritic-cell-driven T-cell priming is most effective in the EBV-positive and microsatellite-unstable gastric cancers, the subtypes that respond to checkpoint blockade."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "One gene ties stomach to breast: germline CDH1 (E-cadherin) loss causes hereditary diffuse gastric cancer and lobular breast cancer together, so a CDH1 carrier needs surveillance — or surgery — for both organs."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "MLH1 silencing defines a gastric subtype: epigenetic loss of this mismatch-repair gene produces the microsatellite-unstable, hypermutated gastric cancers — a TCGA molecular class that is especially responsive to immune-checkpoint therapy."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells crowd the gastric tumor stroma: their density correlates with angiogenesis and worse prognosis, part of the inflammatory microenvironment that Helicobacter-driven gastritis builds before cancer arises."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Gastric cancer is strongly pro-thrombotic: like other GI adenocarcinomas it drives a high rate of venous thromboembolism (Trousseau), complicating the chemotherapy and major gastrectomy its treatment requires."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Helicobacter inflammation drives the stomach to cancer through STAT3: chronic gastritis raises IL-6 and IL-11 that activate STAT3 in gastric epithelium, a central inflammation-to-cancer pathway in gastric carcinogenesis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "An obstructing or perforating tumor seeds infection: gastric cancer that blocks the outlet or breaches the wall spills contents into the peritoneum, and gastrectomy and chemotherapy add their own routes to sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Beyond bleeding, inflammation suppresses the marrow: gastric cancer's chronic blood loss causes iron deficiency, but its inflammatory cytokines also drive an anemia of chronic disease, and gastrectomy adds B12 malabsorption."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its platinum chemo and obstruction strain the kidney: the cisplatin and oxaliplatin used against gastric cancer are nephrotoxic, and outlet obstruction with poor intake adds prerenal injury, together threatening chronic kidney disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its fluoropyrimidine chemo can wound the heart: the 5-fluorouracil and capecitabine in gastric-cancer regimens cause coronary vasospasm and cardiotoxicity that can precipitate ischemia and cardiac dysfunction."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Gastrectomy and a poor prognosis weigh on mood: loss of the stomach, the eating difficulties of dumping and weight loss, and a guarded outlook give gastric cancer a substantial burden of depression."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Gastrectomy starves bone of nutrients: removing the stomach impairs absorption of calcium, vitamin D and B12, and the resulting metabolic bone disease accelerates osteoporosis after gastric-cancer surgery."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its platinum chemo and B12 loss injure nerves: the oxaliplatin and cisplatin used for gastric cancer cause peripheral neuropathy, compounded by the B12 deficiency of gastrectomy, producing neuropathic pain."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemotherapy opens the lung to mold: the neutropenia from platinum-based gastric-cancer chemotherapy can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Gastrectomy hinges on a fragile join: removing the stomach for gastric cancer leaves an oesophago-jejunal anastomosis prone to leak, and the malnutrition of the disease slows wound healing."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Losing the stomach upsets metabolism: gastrectomy removes ghrelin-producing tissue and causes dumping syndrome with reactive hypoglycaemia, alongside the nutritional and metabolic fallout of the disease."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A grim cancer with altered eating breeds worry: the poor prognosis, weight loss and the lifelong dietary upheaval after gastrectomy in gastric cancer foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads early through the nodes: gastric cancer disseminates to lymph nodes including the classic left supraclavicular Virchow's node, and nodal involvement drives its staging and prognosis."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It signals through the skin: paraneoplastic acanthosis nigricans, the Leser-Trélat sign of sudden seborrhoeic keratoses, and a Sister Mary Joseph umbilical nodule are recognised cutaneous clues."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Some subtypes invite immunotherapy: MSI-high and EBV-positive gastric cancers are highly immunogenic and respond to checkpoint-inhibitor therapy, unlike most gastric tumours."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It seeds the meninges: gastric adenocarcinoma is a classic cause of leptomeningeal carcinomatosis, and paraneoplastic neurological syndromes can occur."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to the lungs: gastric cancer metastasises to the lungs and pleura, and lymphangitis carcinomatosa causes progressive breathlessness."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It reaches bone and muscle: gastric cancer metastasises to the skeleton, and paraneoplastic dermatomyositis can herald the underlying tumour."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy joins first-line: PD-1 inhibitors (nivolumab, pembrolizumab) added to chemotherapy improve survival in advanced gastric cancer, especially MSI-high and EBV-positive tumours."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Perioperative chemo is standard: the FLOT regimen before and after surgery, or platinum-fluoropyrimidine for advanced disease, is the chemotherapy backbone of gastric cancer."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Molecular subsets get matched drugs: trastuzumab and T-DXd for HER2-positive disease, ramucirumab against VEGFR2 and zolbetuximab for Claudin-18.2 widen gastric cancer treatment."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It drains to the liver: gastric cancer cells travel the portal vein to seed the liver lobule, and hepatic metastases mark incurable disease, shifting care from surgery to systemic chemo-immunotherapy."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It spreads to bone and marrow: gastric cancer metastasises to bone, and diffuse marrow infiltration can cause a leukoerythroblastic picture and even DIC, signs of widespread disease."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Aggressive upper-GI adenocarcinomas: gastric and pancreatic cancer share late presentation, desmoplastic biology, peritoneal spread and grim prognosis, dominating the lethal upper-gastrointestinal malignancies."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Where it spreads: gastric cancer metastasises to the lungs, seeding tumour deposits in the alveolar capillary bed in advanced disease."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "MALT origin and immunotherapy: chronic H. pylori infection induces gastric lymphoid follicles with germinal centres (the root of MALT lymphoma), and EBV-positive and MSI-high gastric cancers respond to checkpoint blockade."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Two Lynch-spectrum cancers: mismatch-repair-deficient gastric and endometrial cancers both arise in Lynch syndrome and share the MSI-high, immunotherapy-responsive phenotype."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Lymphoma in the stomach: chronic Helicobacter inflammation causes gastric MALT lymphoma that can transform into diffuse large B-cell lymphoma, a non-epithelial gastric cancer treated very differently."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Gastric carcinoids: atrophic gastritis and the hypergastrinaemia it causes drive gastric neuroendocrine tumours, a distinct cancer arising from the same chronically inflamed stomach."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity and the upper stomach: obesity and its reflux raise the risk of cardia and gastro-oesophageal junction adenocarcinoma, a rising subtype distinct from H. pylori-driven distal cancer."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Hamartoma-syndrome risk: Peutz-Jeghers syndrome (STK11) carries a markedly raised risk of gastric cancer among its broad spectrum of gastrointestinal malignancies."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Polyposis predisposition: juvenile polyposis syndrome (SMAD4/BMPR1A) produces gastric hamartomatous polyps and a substantially increased risk of gastric cancer."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Intestinal-type carcinogenesis: aberrant Wnt/β-catenin activation drives the intestinal-type gastric cancers that arise through the chronic gastritis-to-carcinoma Correa cascade."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT activation: PIK3CA mutation activates AKT in gastric cancer, driving growth and survival, especially in the EBV-associated molecular subtype."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified oncogene: MYC amplification is common in gastric cancer, driving the proliferation and metabolic reprogramming of the tumour."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in hypoxic gastric tumours drives angiogenesis and an invasive, chemoresistant phenotype linked to peritoneal spread."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "EMT and desmoplasia: TGF-beta drives the epithelial-mesenchymal transition and desmoplastic stroma of diffuse-type gastric cancer, the signet-ring histology that spreads through the stomach wall and peritoneum."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase immortalisation: TERT reactivation maintains telomeres in gastric cancer cells, granting the replicative immortality that complements its p53 and RTK driver lesions."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws tumour-associated macrophages into gastric cancer, building the immunosuppressive microenvironment that promotes invasion and blunts immunotherapy."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Helicobacter carcinogenesis: TLR4 sensing of Helicobacter pylori products drives the chronic gastritis that initiates the Correa cascade — atrophy, metaplasia, dysplasia — underlying most intestinal-type gastric cancer."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Subtype immunogenicity: the EBV-positive and microsatellite-instable gastric cancers carry high mutational and viral-antigen burdens that engage cGAS-STING, the innate basis for their strong response to checkpoint inhibitors."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Peritoneal metastasis: the CXCL12-CXCR4 axis directs gastric cancer cells to the peritoneum and ovary (Krukenberg tumours), the transcoelomic spread that dominates the mortality of advanced disease."
  - target: 01-human/03-molecular/lmp1
    relation: connects-to
    note: "EBV-positive subtype: about a tenth of gastric cancers are driven by Epstein-Barr virus, a molecularly distinct subtype with PD-L1 amplification and dense immune infiltration that is especially responsive to checkpoint blockade."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: perioperative FLOT and platinum-based regimens kill gastric-cancer cells through caspase-3-mediated apoptosis, the cytotoxic backbone whose effect on the resected tumour predicts outcome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy killing: checkpoint inhibitors and emerging CAR-T against targets like Claudin18.2 work by unleashing cytotoxic T cells that kill gastric-cancer cells through perforin and granzyme, especially in the EBV-positive and MSI-high subtypes."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK convergence: HER2, EGFR, KRAS, FGFR2 and MET (all already mapped) funnel into the MAPK-ERK cascade, the proliferative hub driving gastric carcinoma."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) that sustains growth and survival signalling in gastric cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory initiation: Helicobacter-pylori-induced IL-1β both suppresses gastric acid and drives the chronic inflammation that initiates carcinogenesis, and IL1B polymorphisms raise gastric-cancer risk."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "H. pylori innate sensing: Helicobacter pylori activates TLR-MyD88-NF-κB signalling (TLR4 and NF-κB already mapped), the chronic inflammation that drives the intestinal-type gastric-carcinogenesis cascade."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory microenvironment: IL-6-STAT3 signalling (STAT3 already mapped) sustains the pro-proliferative inflammatory microenvironment linking chronic gastritis to gastric cancer."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle silencing: CDKN2A/p16 silencing is a frequent epigenetic and deletional event in gastric cancer, releasing the cyclin-D-CDK4/6 brake on proliferation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IL-6-JAK-STAT3 signalling (IL-6 and STAT3 mapped), driven by Helicobacter pylori inflammation, promotes gastric carcinogenesis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the invasion, peritoneal dissemination and immune evasion of gastric cancer."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Loss of TGF-β-SMAD4 signalling (TGF-β mapped) contributes to progression, particularly of diffuse-type gastric cancer."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of gastric cancer, particularly the immunotherapy-responsive EBV-positive and MSI-high subtypes."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression silences tumour-suppressor genes and contributes to the epigenetic dysregulation of gastric cancer."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (CDKN2A already mapped) drives the cell-cycle progression of gastric cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) removes a tumor-suppressive brake in gastric cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the H. pylori-associated inflammatory microenvironment that drives gastric carcinogenesis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in gastric cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the Wnt/β-catenin and survival signaling (Wnt already mapped) of gastric cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of HER2, MET, and EGFR (all already mapped) drives the invasion of gastric cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation, prominent in the EBV-associated CpG-island-methylator subtype, contributes to gastric cancer."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of gastric cancer."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy, modulated during Helicobacter pylori infection, supports the survival and therapy resistance of gastric cancer cells."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of gastric cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling, frequently mutated in the EBV and microsatellite-instability subtypes, participates in the epigenetic landscape of gastric cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of gastric cancer."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the Helicobacter-pylori-linked inflammation and tumor microenvironment of gastric cancer."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of gastric cancer."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of gastric cancer."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the tumor microenvironment and metastatic interactions of gastric cancer."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy subtypes: the microsatellite-instable and EBV-associated (LMP1 already mapped) subtypes of gastric cancer are neoantigen-rich and respond to checkpoint inhibitors, with MHC class II antigen presentation shaping the T-cell response."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Hypochlorhydria and carcinogenesis: Helicobacter-induced atrophic gastritis reduces gastric acid (proton) secretion, and the resulting hypochlorhydria fosters bacterial overgrowth and nitrosamine formation that promote the intestinal-type gastric carcinogenesis cascade."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Diffuse-type invasion: the AXL receptor tyrosine kinase drives the epithelial-mesenchymal transition and treatment resistance of gastric cancer, particularly the diffuse E-cadherin-deficient type (CDH1 already mapped)."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Bleeding and anaemia: chronic occult bleeding from gastric cancer causes iron-deficiency anaemia (iron already mapped), and the falling haemoglobin with weight loss and dyspepsia is a common presentation prompting endoscopy."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunotherapy: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) supports the checkpoint-inhibitor response, especially effective in the EBV-positive and microsatellite-unstable (MLH1 already mapped) subtypes of gastric cancer."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: Helicobacter inflammation and dietary nitrosamines generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage drives the intestinal-type gastric carcinogenesis cascade."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 gastric carcinogenesis: Helicobacter-driven inflammation induces cyclooxygenase-2 and prostaglandin E2 in the gastric mucosa, promoting the proliferation and angiogenesis (VEGF already mapped) of the intestinal-type carcinogenesis cascade."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune escape that the checkpoint inhibitors used in MSI-high and EBV-positive gastric cancer aim to reverse."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron-deficiency anaemia: chronic occult bleeding and the atrophic gastritis impairing iron absorption cause iron-deficiency anaemia (haemoglobin already mapped), often the presenting sign of gastric cancer."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment that checkpoint inhibitors in MSI-high and EBV-positive gastric cancer must overcome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of gastric cancer."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity and cardia cancer: the adipokine leptin links obesity to gastric-cardia adenocarcinoma, its pro-proliferative signalling (Wnt already mapped) part of the metabolic contribution to the disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity-related gastric-cardia adenocarcinoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the obesity-related gastric cancer."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and, with the chronic tumour bleeding, produces the anaemia (haemoglobin already mapped) of gastric cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "MALT B-cell response: the Helicobacter pylori (already mapped)-driven chronic gastric B-cell (MALT) lymphoid response shares the aetiology with the gastric adenocarcinoma and drives the gastric MALT lymphoma."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal IgA defence: the secretory IgA of the gastric mucosal immunity against the Helicobacter pylori (already mapped) shapes the chronic-infection microenvironment of gastric cancer."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 atrophic gastritis: the IFN-γ Th1 response to the Helicobacter pylori (already mapped) drives the atrophic gastritis and the intestinal metaplasia along the Correa cascade to gastric cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response to the Helicobacter pylori (already mapped) that drives the atrophic gastritis of gastric cancer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate/EBV interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing, shapes the innate-immune microenvironment of the EBV-associated (LMP1 already mapped) and other gastric cancers."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of gastric cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the Helicobacter-driven (already mapped) tumour-promoting inflammation of gastric cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the gastric-cancer microenvironment."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral/MALT arm: the plasma cells secrete the antibodies (secretory IgA already mapped) of the Helicobacter (already mapped) and MALT humoral response of the gastric mucosa."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Trastuzumab ADCC: the NK cells (perforin already mapped) mediate the antibody-dependent cellular cytotoxicity of the anti-HER2 (already mapped) trastuzumab against HER2-positive gastric cancer."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of gastric cancer."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the Helicobacter-associated (already mapped) inflammatory gastric-cancer stroma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the Helicobacter-associated gastric-cancer microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the gastric-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Blood-loss iron: transferrin, the iron carrier, reflects the iron-deficiency anaemia of the chronic gastrointestinal blood loss and the iron demand of gastric cancer."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-GC axis: TSLP, from the H. pylori (already mapped)-infected gastric epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2-skewed immunosuppressive microenvironment of gastric cancer."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-GC axis: bradykinin, via B1/B2 receptors on gastric-cancer endothelium (already mapped) and mast cells (already mapped), augments the vascular permeability, tumour oedema, and the H. pylori (already mapped)-driven inflammatory milieu of gastric cancer."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-GC axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and the iron-deficiency anaemia of gastric cancer, activates the EPOR on tumour cells (already mapped) and modulates macrophage (already mapped) polarisation in the tumour microenvironment."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-GC axis: histamine, from H. pylori (already mapped)-activated mast cells and ECL cells in the gastric mucosa, signals via H2 receptors on gastric-cancer cells, modulating acid secretion, angiogenesis, and the pro-tumourigenic milieu of gastric cancer."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-GC axis: melatonin, produced by gastric enterochromaffin cells and circulating pineal melatonin, suppresses H. pylori (already mapped)-driven oxidative stress and NFκB (already mapped) signalling, limiting the progression from gastritis to gastric cancer."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-GC axis: testosterone, via androgen receptor signalling on gastric-cancer cells and stroma, modulates H. pylori (already mapped)-driven oncogenic signalling and the well-established male sex bias in gastric-cancer incidence and mortality."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "GC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of gastric cancer."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "GC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of gastric cancer."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "GC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of gastric cancer."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "GC serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of gastric cancer."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "GC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative tumour cascade of gastric cancer."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "GC iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of gastric cancer."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "GC magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour cascade of gastric cancer."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "GC copper: copper supports macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of gastric cancer."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "GC zinc: zinc cofactors macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour immune function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour cascade of gastric cancer."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "GC calcium: calcium regulates macrophage (already mapped) and T-cytotoxic (already mapped) immune activation; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of gastric cancer."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "GC phosphorus: phosphorus, as ATP in macrophages (already mapped) and mast cells (already mapped), fuels gastric tumour-stromal signalling; phosphorus excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of gastric cancer."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "GC potassium: potassium regulates macrophage (already mapped) and mast-cell (already mapped) membrane function; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of gastric cancer."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "GC carbon: carbon in nucleotides of macrophages (already mapped) and mast cells (already mapped) fuels gastric tumour proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of gastric cancer."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "GC chloride: chloride channels on macrophages (already mapped) and mast cells (already mapped) regulate ionic signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of gastric cancer."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "GC hydrogen: hydrogen via ROS from macrophages (already mapped) and mast cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of gastric cancer."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "gastric-cancer glp-1: GLP-1 from gastric cells (already mapped) and macrophages (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "gastric-cancer angiotensin-ii: angiotensin II on gastric epithelial cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "gastric-cancer rankl: RANKL from gastric epithelial cells (already mapped) and macrophages (already mapped) modulates immune invasion; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "gastric-cancer fibronectin: fibronectin in gastric epithelial cells (already mapped) and macrophages (already mapped) promotes ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "gastric-cancer notch: Notch signalling on gastric epithelial cells (already mapped) and macrophages (already mapped) regulates tumour stem-cell renewal; notch excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "gastric-cancer igf-1: IGF-1 from macrophages (already mapped) and gastric epithelial cells (already mapped) promotes tumour growth; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer."
---

# Gastric Cancer

## Overview

**Gastric cancer (GC)** is the 5th most common cancer and 4th leading cause of cancer death worldwide, with the highest burden in East Asia, Eastern Europe, and South America. The majority (~95%) are **gastric adenocarcinomas** arising from the gastric mucosa. Gastric cancer biology is shaped by two major environmental exposures: *Helicobacter pylori* infection (the dominant etiological factor for non-cardia, intestinal-type GC) and Epstein-Barr virus (EBV, in a distinct molecular subtype). Modern molecular profiling has revealed actionable subsets — particularly HER2-overexpressing (~15-20%), MSI-H (~10-15%), and CLDN18.2-expressing (~30-40%) tumors — that are transforming treatment paradigms [^bang-2010-toga].

**Epidemiology:**
- ~1 million new cases/year globally (5th most common); declining incidence in Western countries (H. pylori eradication, dietary changes)
- ~30,000 new cases/year in the United States; much higher incidence in Japan/Korea (~40× higher than US)
- Male predominance (M:F ~2:1)
- 5-year survival: ~33% overall (US); <15% for metastatic disease; >90% for localized resected disease
- Risk factors: H. pylori infection (~80% of intestinal-type GC), high salt/nitrite diet, smoking, obesity (GERD → cardia GC), atrophic gastritis, intestinal metaplasia

**Gastroesophageal junction (GEJ) cancer:**
GEJ adenocarcinoma (Siewert type I-III) is biologically closer to distal esophageal/gastric cancer than esophageal squamous cell carcinoma; treated similarly to gastric cancer in most trials.

## Structure

### Molecular classification (TCGA 2014)

The TCGA classified gastric cancer into four molecular subtypes:

**EBV+ (~9%):**
- EBV viral integration → host gene silencing + PIK3CA mutations (~80%, highest frequency of any GC subtype) + amplification of JAK2, CD274 (PD-L1), PDCD1LG2 (PD-L2) → extreme PD-L1 expression → high PD-1 IO sensitivity; CDKN2A promoter hypermethylation (100%)
- Most frequently at gastric fundus/body; male predominance
- Highest PD-L1 expression → may benefit most from anti-PD-1 therapy

**MSI-H (~22%):**
- Hypermutation from microsatellite instability (MLH1 silencing by promoter methylation in sporadic MSI-H GC; MMR germline mutations in Lynch syndrome-associated GC)
- Good prognosis; most frequently in antrum; female, elderly
- High tumor mutational burden (TMB) → high neoantigen load → very high PD-1 response (ORR >40%)
- KRAS/NRAS/BRAF, PIK3CA mutations enriched; POLE mutations in some
- Pembrolizumab: accelerated approval for MSI-H/TMB-H solid tumors (2017) → MSI-H GC

**Genomically stable (GS, ~20%):**
- Diffuse histology (Signet ring/poorly cohesive); CDH1 mutations → E-cadherin loss → cell dissociation; RHOA mutations (~15%) → altered cytoskeletal dynamics; CLDN18-ARHGAP6/26 fusions; poorest prognosis; early peritoneal dissemination
- HER2-negative, MSI-stable; least responsive to current targeted therapy

**CIN (chromosomal instability, ~50%):**
- Intestinal histology; enriched in GEJ and fundus; aneuploidy; TP53 mutations (~70%); HER2 amplification enriched here; receptor tyrosine kinase amplification (VEGFR2, EGFR, FGFR2, MET)
- Most common subtype; most HER2-positive GC here

### Lauren classification (histology)

- **Intestinal type:** Gland-forming; associated with H. pylori, atrophic gastritis → intestinal metaplasia → dysplasia → carcinoma; better prognosis
- **Diffuse type:** Non-cohesive cells (signet-ring); CDH1 loss → E-cadherin-mediated adhesion lost; younger patients; early dissemination; hereditary diffuse GC (CDH1 germline mutation); worse prognosis
- **Mixed type:** Both patterns

### Hereditary gastric cancer

**Hereditary diffuse gastric cancer (HDGC):**
- Caused by germline CDH1 mutation (~40% of HDGC families)
- Lifetime risk of diffuse GC: ~70% (male), ~56% (female)
- Also elevated risk of lobular breast cancer
- **Prophylactic total gastrectomy** recommended for CDH1 pathogenic variant carriers (usually age 18-40) — confirmed HDGC at pathology in >80% of prophylactic gastrectomies

**Lynch syndrome:**
- MSI-H gastric cancer in ~1-5% of Lynch syndrome carriers (MLH1, MSH2, MSH6, PMS2 germline mutations)
- GC is the second most common Lynch-associated cancer after colorectal

## Function

### Helicobacter pylori carcinogenesis

**H. pylori molecular mechanisms:**
- **CagA (cytotoxin-associated gene A):** Injected into gastric epithelial cells via T4SS → CagA phosphorylation by Src/Abl kinases → CagA-SHP-2 interaction → RAS-ERK activation → proliferation; CagA also disrupts E-cadherin-β-catenin complex → Wnt/β-catenin activation → MYC; EPIYA motifs (Western vs. East Asian CagA) correlate with oncogenic potency
- **VacA (vacuolating cytotoxin A):** Forms ion channels → mitochondrial damage → apoptosis evasion; immune suppression (T cell inhibition); VacA+/CagA+ H. pylori strains → highest GC risk
- **Inflammatory cascade:** H. pylori → NFκB → IL-8, IL-1β, TNF-α → chronic gastritis → reactive oxygen species → DNA damage → epithelial-to-mesenchymal transition

**Correa cascade (intestinal-type pathway):**
Normal mucosa → superficial gastritis (H. pylori) → atrophic gastritis → intestinal metaplasia → dysplasia → intestinal-type GC

H. pylori eradication: Reduces GC incidence by ~35-40% (meta-analyses); most benefit when treated before atrophic changes develop.

### CLDN18.2 as a therapeutic target

**Claudin-18 isoform 2 (CLDN18.2):**
- A tight junction protein normally expressed exclusively on differentiated gastric mucosa cells (limited expression in normal organs)
- In GC, dedifferentiation → aberrant surface exposure of CLDN18.2 → targetable antigen
- **Zolbetuximab (IMAB362):** Anti-CLDN18.2 monoclonal antibody; **SPOTLIGHT trial** (zolbetuximab + mFOLFOX6): PFS 10.6 vs. 8.7 months and **GLOW trial** (zolbetuximab + CAPOX): PFS 8.2 vs. 6.8 months; FDA approved May 2024 for CLDN18.2+ HER2-negative GC/GEJ — first approved CLDN18.2-targeted therapy

## Pathology

### Staging and diagnosis

**Endoscopy:**
- Biopsy is essential; EGD with multiple biopsies for any suspicious lesion
- EUS (endoscopic ultrasound): T staging (T1 vs. T2-4) and regional node assessment → determines resectability and neoadjuvant chemotherapy need

**Imaging:**
- CT chest/abdomen/pelvis + PET/CT: Staging, detection of M1 disease; peritoneal metastasis often PET-negative → diagnostic laparoscopy for potentially resectable GC

**Biomarker testing (required for all advanced GC):**
- HER2 IHC ± FISH (IHC 3+ or IHC 2+/FISH+)
- MSI by PCR or dMMR by IHC (MLH1/MSH2/MSH6/PMS2)
- PD-L1 CPS (combined positive score)
- CLDN18.2 by IHC (≥75% of tumor cells with moderate-to-strong membranous staining = CLDN18.2+)
- HER2, FGFR2, and MET copy number and mutation by NGS
- TMB by NGS

**Lauren histology and TCGA molecular subtype** are not formally required outside research settings but inform prognosis and emerging targeted strategies.

### Treatment

**Localized gastric cancer (Stage I-III):**

*Surgery:*
- **Distal gastrectomy** (subtotal): For antral/body GC with adequate proximal margin
- **Total gastrectomy:** Proximal GC, multi-focal GC, HDGC prophylaxis
- **D2 lymphadenectomy:** Standard of care in Eastern practice; recommended ≥15 lymph nodes for adequate staging
- Minimally invasive (laparoscopic/robotic) gastrectomy: Non-inferior to open for early-stage GC

*Perioperative (neoadjuvant + adjuvant) chemotherapy:*
- **FLOT (docetaxel + oxaliplatin + leucovorin + 5-FU):** FLOT4 trial → OS 50 vs. 35 months vs. ECF; now standard perioperative regimen in Western practice
- **CAPOX or FOLFOX adjuvant:** For East Asian patients (CLASSIC trial); post-surgical
- **Nivolumab adjuvant:** CheckMate 577 (for resected GEJ, post-neoadjuvant CRT, residual disease) → DFS 22.4 vs. 11.0 months; approved 2021 for resected GEJ/esophageal cancer; expanding to gastric cancer

**Advanced/metastatic gastric cancer:**

*HER2+ (trastuzumab first-line, then T-DXd):*
- **Trastuzumab + cisplatin + fluoropyrimidine (ToGA trial):** [^bang-2010-toga] OS 13.8 vs. 11.1 months; PFS 6.7 vs. 5.5 months; ORR 47% vs. 35%; FDA approved 2010 — **first targeted therapy in GC**
- **Trastuzumab + pembrolizumab + chemotherapy (KEYNOTE-811):** PFS 10.0 vs. 8.1 months in HER2+/CPS≥1; FDA approved 2023 for HER2+ gastric cancer; now preferred frontline for HER2+/PD-L1+
- **T-DXd (DESTINY-Gastric01):** ORR 51% vs. 14%; OS 12.5 vs. 8.4 months in HER2+ post-trastuzumab gastric cancer; FDA approved 2021 as second-line HER2+ GC

*HER2-negative first-line (pembrolizumab ± chemotherapy):*
- **Nivolumab + chemotherapy (CheckMate 649):** [^janjigian-2021-checkmate649] OS 14.4 vs. 11.1 months for CPS≥5 (HR 0.71); PFS 7.7 vs. 6.0 months; FDA approved 2021 for GC/GEJC/EAC
- **Pembrolizumab + chemotherapy (KEYNOTE-590/811):** Active in PD-L1 CPS≥10 population

*MSI-H GC:*
- Pembrolizumab (pan-tumor MSI-H/TMB-H approval)
- High ORR (~40-60%), durable responses; may avoid chemotherapy in MSI-H high-risk GC
- Consider pembrolizumab monotherapy as first-line in MSI-H GC (KEYNOTE-158)

*Second-line:*
- Ramucirumab + paclitaxel (RAINBOW trial: OS 9.6 vs. 7.4 months — largest GC phase III) → most commonly used 2nd-line option
- Trifluridine-tipiracil (TAS-102) for 3rd-line+
- Irinotecan monotherapy
- FOLFIRI

*Novel targets:*
- **CLDN18.2:** Zolbetuximab + chemotherapy (approved 2024 for CLDN18.2+ HER2-negative GC)
- **FGFR2b (bemarituzumab):** ORR 38% vs. 25%; PFS 9.5 vs. 7.4 months in FGFR2b+ GC (FIGHT trial); not yet approved
- **MET amplification:** Telisotuzumab vedotin (MET-directed ADC) in early trials

## Connections

- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 overexpression in ~15-20% of gastric/GEJ cancer; trastuzumab+cisplatin+fluoropyrimidine is first-line for HER2+ disease (ToGA trial); T-DXd (trastuzumab deruxtecan) active in HER2-low and HER2-overexpressing gastric cancer (DESTINY-Gastric01).
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Ramucirumab (anti-VEGFR2) + paclitaxel is standard second-line for advanced gastric cancer (RAINBOW trial: OS 9.6 vs. 7.4 months); ramucirumab monotherapy also approved; bevacizumab failed to improve OS in AVAGAST; VEGFR2 is the validated antiangiogenic target in gastric cancer.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Pembrolizumab + chemotherapy is first-line for PD-L1 CPS ≥5 advanced gastric/GEJ adenocarcinoma (KEYNOTE-590/811); nivolumab + chemotherapy approved in many regions (CheckMate 649); MSI-H/dMMR gastric cancer (~10-15%) has particularly high response to PD-1 blockade (ORR >40%).
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR overexpression in ~30-40% of gastric cancer but EGFR-targeted therapy (cetuximab, panitumumab) failed in unselected gastric cancer trials; EGFR amplification in a subset → potential biomarker; FGFR2 amplification (~5-10%) responds to bemarituzumab (anti-FGFR2b).
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — H. pylori is the dominant cause of non-cardia intestinal-type gastric cancer via the Correa cascade (gastritis → atrophy → metaplasia → dysplasia → carcinoma); CagA hijacks SHP-2/RAS-ERK and disrupts E-cadherin/β-catenin; eradication cuts GC incidence ~35-40%.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — EBV defines a distinct ~9% gastric cancer subtype (TCGA) with viral integration, near-universal PIK3CA mutation, CDKN2A silencing, and amplified CD274/PDCD1LG2 → very high PD-L1 → strong response to PD-1 blockade; EBER in-situ hybridization confirms it.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../hereditary-diffuse-gastric-cancer/README.md)** — Germline CDH1 (E-cadherin) loss causes hereditary diffuse gastric cancer — signet-ring/poorly cohesive tumors with ~70% lifetime diffuse-GC risk plus elevated lobular breast cancer risk; prophylactic total gastrectomy is recommended for CDH1 carriers aged 18-40.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Gastric cancer and cholangiocarcinoma are GI adenocarcinomas sharing actionable targets — HER2, PD-1/PD-L1, and FGFR2 — but arise differently: gastric cancer from stomach epithelium (H. pylori, EBV, germline CDH1), CCA from biliary cholangiocytes (FGFR2 fusions, IDH1 mutations).
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Gastric cancer arises from the stomach's mucosal epithelium, usually via the Correa cascade of H. pylori gastritis → atrophy → metaplasia → dysplasia → intestinal-type carcinoma; the diffuse type (CDH1 loss) instead infiltrates the wall as signet-ring cells (linitis plastica).
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Gastric and esophageal cancers merge at the gastroesophageal junction, where Siewert-classified adenocarcinomas are treated as one entity; both share HER2 amplification, PD-1 blockade, and reflux/obesity risk, while distal gastric and esophageal squamous cancers diverge by cause.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Gastric and colorectal cancer are both GI adenocarcinomas sharing pathways and predispositions: microsatellite-unstable subtypes of each respond to checkpoint inhibitors, both arise in Lynch syndrome, and both are screened by endoscopy where incidence is high.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Gastric cancer is part of the Lynch syndrome tumor spectrum: germline mismatch-repair mutations raise gastric (especially intestinal-type) cancer risk alongside colorectal and endometrial cancer, so MMR/MSI testing and upper endoscopic surveillance are warranted in carriers.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Iron-deficiency anemia is a classic presenting sign of gastric cancer: chronic occult blood loss from an ulcerated tumor (and impaired absorption from atrophic gastritis) depletes iron, so unexplained IDA—especially in older adults—mandates upper endoscopy to exclude it.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Gastric cancer is part of the FAP tumor spectrum: APC-driven polyposis extends beyond the colon to the stomach, where fundic-gland polyps and gastric adenomas raise cancer risk and warrant upper-GI surveillance—one germline mutation reshaping the gut's risk.
- `connects-to` → **[GIST](../gist/README.md)** — Gastric cancer and GIST are the two main stomach tumors but from different cells: carcinoma arises from glandular epithelium (H. pylori, CDH1), GIST from KIT-mutant interstitial cells of Cajal, the gut pacemaker—epithelial versus mesenchymal, very different therapy.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — CDH1 (E-cadherin) loss defines diffuse gastric cancer: without this adhesion molecule cells scatter through the stomach wall as linitis plastica rather than a mass, and germline CDH1 mutation drives hereditary diffuse gastric cancer—prompting prophylactic gastrectomy.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation is among the commonest events in gastric cancer: loss of p53 removes a key checkpoint as H. pylori-driven inflammation and intestinal metaplasia progress to carcinoma, so p53 inactivation marks the late, invasive stage of the Correa cascade.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS and related signaling drive a subset of gastric cancers: activating mutations push proliferation in intestinal-type tumors, contributing to the molecular diversity (alongside HER2, EBV, MSI) that increasingly guides targeted gastric cancer therapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages shape gastric cancer: recruited into the tumor, they promote invasion, angiogenesis and immune suppression, and high macrophage infiltration predicts worse outcome—part of the microenvironment seeded by chronic H. pylori gastritis.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Gastric cancer is a major cancer of the digestive system: it arises in the stomach lining often after H. pylori gastritis and intestinal metaplasia, and vague early symptoms mean it usually presents late—making it a leading cause of cancer death worldwide.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Gastric cancer often follows a metaplastic change in the gut epithelium: chronic inflammation drives the stomach lining toward an intestinal-type epithelium (intestinal metaplasia), a recognized precancerous step in the Correa cascade from gastritis to carcinoma.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy has a role in gastric cancer: photon-beam radiation combined with chemotherapy is used before or after surgery to improve local control of resectable tumors and to palliate bleeding or obstruction in advanced disease.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Gastric cancer subsets respond to T-cell immunotherapy: EBV-positive and MSI-high tumors are richly infiltrated by cytotoxic T cells and respond to checkpoint inhibitors, so molecular subtyping now guides who gets immunotherapy.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is gastric cancer's main metastatic target: tumor cells drain via the portal vein to seed the liver, so hepatic metastases mark incurable disease and shift treatment from surgery to systemic chemo-immunotherapy.
- `connects-to` → **[Ovarian Cancer](../ovarian-cancer/README.md)** — Gastric cancer can masquerade as ovarian cancer: signet-ring cells spread to the ovaries as Krukenberg tumors, so bilateral ovarian masses in a woman may actually be metastatic stomach cancer—a crucial diagnostic catch.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Dietary salt is a major driver of gastric cancer: high sodium intake damages the stomach lining and promotes H. pylori colonization and carcinogenesis, which is why salt-heavy diets track with the world's highest stomach cancer rates.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Diffuse gastric cancer is often driven by FGFR2: amplification of this receptor fuels the aggressive signet-ring type, making FGFR inhibitors a targeted option beyond the HER2-directed drugs used in intestinal-type tumors.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Diffuse gastric cancer turns the stomach to leather through fibroblasts: cancer-associated fibroblasts lay down dense stroma in linitis plastica, stiffening the whole stomach wall and helping the scattered signet-ring cells resist therapy.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Nitrogen-based nitrosamines help cause gastric cancer: salted, smoked and pickled foods, and nitrate converted by stomach bacteria, generate DNA-damaging N-nitroso compounds, a dietary driver that compounds Helicobacter infection.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Helicobacter drives gastric cancer through NF-kB: the infection keeps this inflammatory switch active in the stomach lining, sustaining the chronic gastritis and survival signaling that step the mucosa toward malignancy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Helicobacter recruits regulatory T cells that shield gastric cancer: the bacterium induces Tregs that dampen the immune attack, letting infection persist and the tumor evade clearance, while blunting checkpoint-therapy responses.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Gastric cancer bleeds away iron: the tumor oozes blood into the stomach, so a slow, painless iron-deficiency anemia is often the first clue, especially in older patients.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Gastric cancer invades the neighboring pancreas: as it grows through the stomach wall, the tumor can reach the adjacent pancreas, a local spread that signals advanced, often unresectable disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Diffuse gastric cancer turns the stomach to fibrosis: signet-ring cells provoke a dense desmoplastic reaction (linitis plastica) that stiffens the whole stomach wall into a rigid 'leather bottle.'
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Gastric cancer is fed by new vessels: VEGF recruits endothelial cells, and ramucirumab, an anti-VEGFR2 antibody, is a mainstay of advanced disease that starves the tumor of its blood supply.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Gastric cancer seeds the abdomen: signet-ring cells spread across the peritoneum and can encase the bowel, and ovarian Krukenberg deposits mark this transcoelomic spread.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Gastric cancer can invade the marrow: diffuse signet-ring disease is a classic cause of cancer-associated microangiopathy and a leukoerythroblastic blood picture from marrow infiltration.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals gastric cancer's signet-ring cell: a mucin vacuole so large it shoves the nucleus to a crescent at the cell's rim, the hallmark of the diffuse type that stiffens the stomach into linitis plastica.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Gastric cancer signals through the skin: the velvety dark patches of paraneoplastic acanthosis nigricans and a hard umbilical 'Sister Mary Joseph' nodule from peritoneal spread can be the first outward signs of the hidden tumor.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Gastric cancer spreads to the lung: beyond the liver and peritoneum, hematogenous metastases and lymphangitic spread reach the lungs, a marker of the advanced disease that surgery can no longer cure.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies target gastric cancer's surface markers: trastuzumab against HER2, the checkpoint antibodies pembrolizumab and nivolumab, and zolbetuximab against claudin-18.2 now extend survival in selected advanced tumors.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Gastric cancer bleeds and starves the red cells: chronic oozing causes iron-deficiency anemia that is often the first clue, and autoimmune atrophic gastritis can add a B12-deficient pernicious anemia.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The chemotherapy frays the nerves: the cisplatin and oxaliplatin backbones of gastric cancer regimens injure peripheral sensory neurons into a cold-triggered, dose-limiting neuropathy.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Gastric cancer can drop seeds in the ovary: signet-ring cells spreading through the peritoneum implant on the ovaries as Krukenberg tumors, sometimes the presenting finding in a young woman whose stomach primary is still silent.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — A minority of gastric cancers are MET-driven: amplification or overexpression of the MET receptor marks aggressive, fast-spreading tumors and a poor prognosis, an actionable target probed by MET-directed therapies.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Gastric adenocarcinoma is a classic clot-maker: its mucin-secreting cells trigger paraneoplastic thrombocytosis and the migratory thrombophlebitis of Trousseau syndrome, driving a high rate of venous thromboembolism.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K signaling drives a major subtype: PIK3CA mutations are common in gastric cancer, especially the Epstein-Barr-virus-positive group, switching on the AKT growth pathway and marking a targetable vulnerability.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — How the tumor handles antigen decides immunotherapy's reach: dendritic-cell-driven T-cell priming is most effective in the EBV-positive and microsatellite-unstable gastric cancers, the subtypes that respond to checkpoint blockade.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — One gene ties stomach to breast: germline CDH1 (E-cadherin) loss causes hereditary diffuse gastric cancer and lobular breast cancer together, so a CDH1 carrier needs surveillance — or surgery — for both organs.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — MLH1 silencing defines a gastric subtype: epigenetic loss of this mismatch-repair gene produces the microsatellite-unstable, hypermutated gastric cancers — a TCGA molecular class that is especially responsive to immune-checkpoint therapy.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells crowd the gastric tumor stroma: their density correlates with angiogenesis and worse prognosis, part of the inflammatory microenvironment that Helicobacter-driven gastritis builds before cancer arises.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Gastric cancer is strongly pro-thrombotic: like other GI adenocarcinomas it drives a high rate of venous thromboembolism (Trousseau), complicating the chemotherapy and major gastrectomy its treatment requires.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Helicobacter inflammation drives the stomach to cancer through STAT3: chronic gastritis raises IL-6 and IL-11 that activate STAT3 in gastric epithelium, a central inflammation-to-cancer pathway in gastric carcinogenesis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — An obstructing or perforating tumor seeds infection: gastric cancer that blocks the outlet or breaches the wall spills contents into the peritoneum, and gastrectomy and chemotherapy add their own routes to sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Beyond bleeding, inflammation suppresses the marrow: gastric cancer's chronic blood loss causes iron deficiency, but its inflammatory cytokines also drive an anemia of chronic disease, and gastrectomy adds B12 malabsorption.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its platinum chemo and obstruction strain the kidney: the cisplatin and oxaliplatin used against gastric cancer are nephrotoxic, and outlet obstruction with poor intake adds prerenal injury, together threatening chronic kidney disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its fluoropyrimidine chemo can wound the heart: the 5-fluorouracil and capecitabine in gastric-cancer regimens cause coronary vasospasm and cardiotoxicity that can precipitate ischemia and cardiac dysfunction.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Gastrectomy and a poor prognosis weigh on mood: loss of the stomach, the eating difficulties of dumping and weight loss, and a guarded outlook give gastric cancer a substantial burden of depression.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Gastrectomy starves bone of nutrients: removing the stomach impairs absorption of calcium, vitamin D and B12, and the resulting metabolic bone disease accelerates osteoporosis after gastric-cancer surgery.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its platinum chemo and B12 loss injure nerves: the oxaliplatin and cisplatin used for gastric cancer cause peripheral neuropathy, compounded by the B12 deficiency of gastrectomy, producing neuropathic pain.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemotherapy opens the lung to mold: the neutropenia from platinum-based gastric-cancer chemotherapy can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Gastrectomy hinges on a fragile join: removing the stomach for gastric cancer leaves an oesophago-jejunal anastomosis prone to leak, and the malnutrition of the disease slows wound healing.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Losing the stomach upsets metabolism: gastrectomy removes ghrelin-producing tissue and causes dumping syndrome with reactive hypoglycaemia, alongside the nutritional and metabolic fallout of the disease.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A grim cancer with altered eating breeds worry: the poor prognosis, weight loss and the lifelong dietary upheaval after gastrectomy in gastric cancer foster chronic health anxiety alongside depression.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads early through the nodes: gastric cancer disseminates to lymph nodes including the classic left supraclavicular Virchow's node, and nodal involvement drives its staging and prognosis.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It signals through the skin: paraneoplastic acanthosis nigricans, the Leser-Trélat sign of sudden seborrhoeic keratoses, and a Sister Mary Joseph umbilical nodule are recognised cutaneous clues.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Some subtypes invite immunotherapy: MSI-high and EBV-positive gastric cancers are highly immunogenic and respond to checkpoint-inhibitor therapy, unlike most gastric tumours.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It seeds the meninges: gastric adenocarcinoma is a classic cause of leptomeningeal carcinomatosis, and paraneoplastic neurological syndromes can occur.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to the lungs: gastric cancer metastasises to the lungs and pleura, and lymphangitis carcinomatosa causes progressive breathlessness.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It reaches bone and muscle: gastric cancer metastasises to the skeleton, and paraneoplastic dermatomyositis can herald the underlying tumour.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy joins first-line: PD-1 inhibitors (nivolumab, pembrolizumab) added to chemotherapy improve survival in advanced gastric cancer, especially MSI-high and EBV-positive tumours.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Perioperative chemo is standard: the FLOT regimen before and after surgery, or platinum-fluoropyrimidine for advanced disease, is the chemotherapy backbone of gastric cancer.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Molecular subsets get matched drugs: trastuzumab and T-DXd for HER2-positive disease, ramucirumab against VEGFR2 and zolbetuximab for Claudin-18.2 widen gastric cancer treatment.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It drains to the liver: gastric cancer cells travel the portal vein to seed the liver lobule, and hepatic metastases mark incurable disease, shifting care from surgery to systemic chemo-immunotherapy.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It spreads to bone and marrow: gastric cancer metastasises to bone, and diffuse marrow infiltration can cause a leukoerythroblastic picture and even DIC, signs of widespread disease.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Aggressive upper-GI adenocarcinomas: gastric and pancreatic cancer share late presentation, desmoplastic biology, peritoneal spread and grim prognosis, dominating the lethal upper-gastrointestinal malignancies.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Where it spreads: gastric cancer metastasises to the lungs, seeding tumour deposits in the alveolar capillary bed in advanced disease.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — MALT origin and immunotherapy: chronic H. pylori infection induces gastric lymphoid follicles with germinal centres (the root of MALT lymphoma), and EBV-positive and MSI-high gastric cancers respond to checkpoint blockade.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Two Lynch-spectrum cancers: mismatch-repair-deficient gastric and endometrial cancers both arise in Lynch syndrome and share the MSI-high, immunotherapy-responsive phenotype.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Lymphoma in the stomach: chronic Helicobacter inflammation causes gastric MALT lymphoma that can transform into diffuse large B-cell lymphoma, a non-epithelial gastric cancer treated very differently.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Gastric carcinoids: atrophic gastritis and the hypergastrinaemia it causes drive gastric neuroendocrine tumours, a distinct cancer arising from the same chronically inflamed stomach.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity and the upper stomach: obesity and its reflux raise the risk of cardia and gastro-oesophageal junction adenocarcinoma, a rising subtype distinct from H. pylori-driven distal cancer.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Hamartoma-syndrome risk: Peutz-Jeghers syndrome (STK11) carries a markedly raised risk of gastric cancer among its broad spectrum of gastrointestinal malignancies.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — Polyposis predisposition: juvenile polyposis syndrome (SMAD4/BMPR1A) produces gastric hamartomatous polyps and a substantially increased risk of gastric cancer.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Intestinal-type carcinogenesis: aberrant Wnt/β-catenin activation drives the intestinal-type gastric cancers that arise through the chronic gastritis-to-carcinoma Correa cascade.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT activation: PIK3CA mutation activates AKT in gastric cancer, driving growth and survival, especially in the EBV-associated molecular subtype.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified oncogene: MYC amplification is common in gastric cancer, driving the proliferation and metabolic reprogramming of the tumour.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in hypoxic gastric tumours drives angiogenesis and an invasive, chemoresistant phenotype linked to peritoneal spread.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — EMT and desmoplasia: TGF-beta drives the epithelial-mesenchymal transition and desmoplastic stroma of diffuse-type gastric cancer, the signet-ring histology that spreads through the stomach wall and peritoneum.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase immortalisation: TERT reactivation maintains telomeres in gastric cancer cells, granting the replicative immortality that complements its p53 and RTK driver lesions.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws tumour-associated macrophages into gastric cancer, building the immunosuppressive microenvironment that promotes invasion and blunts immunotherapy.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of Helicobacter pylori products drives the chronic gastritis that initiates the Correa cascade—atrophy, intestinal metaplasia, dysplasia—underlying most intestinal-type gastric cancer worldwide.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The EBV-positive and microsatellite-instable gastric cancers carry high mutational and viral-antigen burdens that engage cGAS-STING, the innate-immune basis for their strong response to checkpoint inhibitors.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — The CXCL12-CXCR4 axis directs gastric cancer cells to the peritoneum and ovary (Krukenberg tumors), the transcoelomic spread that dominates the morbidity and mortality of advanced diffuse-type disease.
- `connects-to` → **[LMP1](../../03-molecular/lmp1/README.md)** — About a tenth of gastric cancers are driven by Epstein-Barr virus, a molecularly distinct subtype with PD-L1 amplification and dense immune infiltration that is especially responsive to checkpoint blockade.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Perioperative FLOT and platinum-based regimens kill gastric-cancer cells through caspase-3-mediated apoptosis, the cytotoxic backbone whose effect on the resected tumor predicts outcome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Checkpoint inhibitors and emerging CAR-T against targets like Claudin18.2 work by unleashing cytotoxic T cells that kill gastric-cancer cells through perforin and granzyme, especially in the EBV-positive and MSI-high subtypes.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — HER2, EGFR, KRAS, FGFR2 and MET (all already mapped) funnel into the MAPK-ERK cascade, the proliferative hub driving gastric carcinoma.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (PIK3CA and AKT already mapped) that sustains growth and survival signaling in gastric cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Helicobacter-pylori-induced IL-1β both suppresses gastric acid and drives the chronic inflammation that initiates carcinogenesis, and IL1B polymorphisms raise gastric-cancer risk.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Helicobacter pylori activates TLR-MyD88-NF-κB signaling (TLR4 and NF-κB already mapped), the chronic inflammation that drives the intestinal-type gastric-carcinogenesis cascade.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) sustains the pro-proliferative inflammatory microenvironment linking chronic gastritis to gastric cancer.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/p16 silencing is a frequent epigenetic and deletional event in gastric cancer, releasing the cyclin-D-CDK4/6 brake on proliferation.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 mapped), driven by Helicobacter pylori inflammation, promotes gastric carcinogenesis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the invasion, peritoneal dissemination and immune evasion of gastric cancer.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Loss of TGF-β-SMAD4 signaling (TGF-β mapped) contributes to progression, particularly of diffuse-type gastric cancer.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of gastric cancer, particularly the immunotherapy-responsive EBV-positive and MSI-high subtypes.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression silences tumor-suppressor genes and contributes to the epigenetic dysregulation of gastric cancer.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (CDKN2A already mapped) drives the cell-cycle progression of gastric cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-driven FOXO inactivation (AKT and PIK3CA already mapped) removes a tumor-suppressive brake in gastric cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the H. pylori-associated inflammatory microenvironment that drives gastric carcinogenesis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in gastric cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the Wnt/β-catenin and survival signaling (Wnt already mapped) of gastric cancer.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of HER2, MET, and EGFR (all already mapped) drives the invasion of gastric cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation, prominent in the EBV-associated CpG-island-methylator subtype, contributes to gastric cancer.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of gastric cancer.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy, modulated during Helicobacter pylori infection, supports the survival and therapy resistance of gastric cancer cells.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of gastric cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling, frequently mutated in the EBV and microsatellite-instability subtypes, participates in the epigenetic landscape of gastric cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of gastric cancer.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the Helicobacter-pylori-linked inflammation and tumor microenvironment of gastric cancer.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of gastric cancer.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of gastric cancer.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the tumor microenvironment and metastatic interactions of gastric cancer.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy subtypes: the microsatellite-instable and EBV-associated (LMP1 already mapped) subtypes of gastric cancer are neoantigen-rich and respond to checkpoint inhibitors, with MHC class II antigen presentation shaping the T-cell response.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Hypochlorhydria and carcinogenesis: Helicobacter-induced atrophic gastritis reduces gastric acid (proton) secretion, and the resulting hypochlorhydria fosters bacterial overgrowth and nitrosamine formation that promote the intestinal-type gastric carcinogenesis cascade.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Diffuse-type invasion: the AXL receptor tyrosine kinase drives the epithelial-mesenchymal transition and treatment resistance of gastric cancer, particularly the diffuse E-cadherin-deficient type (CDH1 already mapped).
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Bleeding and anaemia: chronic occult bleeding from gastric cancer causes iron-deficiency anaemia (iron already mapped), and the falling haemoglobin with weight loss and dyspepsia is a common presentation prompting endoscopy.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunotherapy: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) supports the checkpoint-inhibitor response, especially effective in the EBV-positive and microsatellite-unstable (MLH1 already mapped) subtypes of gastric cancer.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: Helicobacter inflammation and dietary nitrosamines generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage drives the intestinal-type gastric carcinogenesis cascade.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 gastric carcinogenesis: Helicobacter-driven inflammation induces cyclooxygenase-2 and prostaglandin E2 in the gastric mucosa, promoting the proliferation and angiogenesis (VEGF already mapped) of the intestinal-type carcinogenesis cascade.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune escape that the checkpoint inhibitors used in MSI-high and EBV-positive gastric cancer aim to reverse.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron-deficiency anaemia: chronic occult bleeding and the atrophic gastritis impairing iron absorption cause iron-deficiency anaemia (haemoglobin already mapped), often the presenting sign of gastric cancer.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the microenvironment that checkpoint inhibitors in MSI-high and EBV-positive gastric cancer must overcome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of gastric cancer.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity and cardia cancer: the adipokine leptin links obesity to gastric-cardia adenocarcinoma, its pro-proliferative signalling (Wnt already mapped) part of the metabolic contribution to the disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity-related gastric-cardia adenocarcinoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the obesity-related gastric cancer.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and, with the chronic tumour bleeding, produces the anaemia (haemoglobin already mapped) of gastric cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — MALT B-cell response: the Helicobacter pylori (already mapped)-driven chronic gastric B-cell (MALT) lymphoid response shares the aetiology with the gastric adenocarcinoma and drives the gastric MALT lymphoma.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal IgA defence: the secretory IgA of the gastric mucosal immunity against the Helicobacter pylori (already mapped) shapes the chronic-infection microenvironment of gastric cancer.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 atrophic gastritis: the IFN-γ Th1 response to the Helicobacter pylori (already mapped) drives the atrophic gastritis and the intestinal metaplasia along the Correa cascade to gastric cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response to the Helicobacter pylori (already mapped) that drives the atrophic gastritis of gastric cancer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate/EBV interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing, shapes the innate-immune microenvironment of the EBV-associated (LMP1 already mapped) and other gastric cancers.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of gastric cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the Helicobacter-driven (already mapped) tumour-promoting inflammation of gastric cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the gastric-cancer microenvironment.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral/MALT arm: the plasma cells secrete the antibodies (secretory IgA already mapped) of the Helicobacter (already mapped) and MALT humoral response of the gastric mucosa.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Trastuzumab ADCC: the NK cells (perforin already mapped) mediate the antibody-dependent cellular cytotoxicity of the anti-HER2 (already mapped) trastuzumab against HER2-positive gastric cancer.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of gastric cancer.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the Helicobacter-associated (already mapped) inflammatory gastric-cancer stroma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the Helicobacter-associated gastric-cancer microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the gastric-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Blood-loss iron: transferrin, the iron carrier, reflects the iron-deficiency anaemia of the chronic gastrointestinal blood loss and the iron demand of gastric cancer.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-GC axis: TSLP, from the H. pylori (already mapped)-infected gastric epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2-skewed immunosuppressive microenvironment of gastric cancer.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-GC axis: bradykinin, via B1/B2 receptors on gastric-cancer endothelium (already mapped) and mast cells (already mapped), augments the vascular permeability, tumour oedema, and the H. pylori (already mapped)-driven inflammatory milieu of gastric cancer.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-GC axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia and the iron-deficiency anaemia of gastric cancer, activates the EPOR on tumour cells (already mapped) and modulates macrophage (already mapped) polarisation in the tumour microenvironment.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-GC axis: histamine, from H. pylori (already mapped)-activated mast cells and ECL cells in the gastric mucosa, signals via H2 receptors on gastric-cancer cells, modulating acid secretion, angiogenesis, and the pro-tumourigenic milieu of gastric cancer.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-GC axis: melatonin, produced by gastric enterochromaffin cells and circulating pineal melatonin, suppresses H. pylori (already mapped)-driven oxidative stress and NFκB (already mapped) signalling, limiting the progression from gastritis to gastric cancer.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-GC axis: testosterone, via androgen receptor signalling on gastric-cancer cells and stroma, modulates H. pylori (already mapped)-driven oncogenic signalling and the well-established male sex bias in gastric-cancer incidence and mortality.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — GC prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of gastric cancer.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — GC oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates tumour-promoting inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of gastric cancer.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — GC vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of gastric cancer.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — GC serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of gastric cancer.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — GC selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative tumour cascade of gastric cancer.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — GC iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of gastric cancer.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — GC magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour cascade of gastric cancer.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — GC copper: copper supports macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of gastric cancer.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — GC zinc: zinc cofactors macrophage (already mapped) and T-cytotoxic (already mapped) anti-tumour immune function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour cascade of gastric cancer.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — GC calcium: calcium regulates macrophage (already mapped) and T-cytotoxic (already mapped) immune activation; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of gastric cancer.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — GC phosphorus: phosphorus, as ATP in macrophages (already mapped) and mast cells (already mapped), fuels gastric tumour-stromal signalling; phosphorus excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of gastric cancer.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — GC potassium: potassium regulates macrophage (already mapped) and mast-cell (already mapped) membrane function; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of gastric cancer.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — GC carbon: carbon in nucleotides of macrophages (already mapped) and mast cells (already mapped) fuels gastric tumour proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of gastric cancer.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — GC chloride: chloride channels on macrophages (already mapped) and mast cells (already mapped) regulate ionic signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of gastric cancer.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — GC hydrogen: hydrogen via ROS from macrophages (already mapped) and mast cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of gastric cancer.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — gastric-cancer glp-1: GLP-1 from gastric cells (already mapped) and macrophages (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — gastric-cancer angiotensin-ii: angiotensin II on gastric epithelial cells (already mapped) and macrophages (already mapped) promotes angiogenesis; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — gastric-cancer rankl: RANKL from gastric epithelial cells (already mapped) and macrophages (already mapped) modulates immune invasion; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — gastric-cancer fibronectin: fibronectin in gastric epithelial cells (already mapped) and macrophages (already mapped) promotes ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — gastric-cancer notch: Notch signalling on gastric epithelial cells (already mapped) and macrophages (already mapped) regulates tumour stem-cell renewal; notch excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — gastric-cancer igf-1: IGF-1 from macrophages (already mapped) and gastric epithelial cells (already mapped) promotes tumour growth; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in gastric cancer.

[^bang-2010-toga]: Bang YJ, Van Cutsem E, Feyereislova A, et al. Trastuzumab in combination with chemotherapy versus chemotherapy alone for treatment of HER2-positive advanced gastric or gastro-oesophageal junction cancer (ToGA): a phase 3, open-label, randomised controlled trial. *Lancet.* 2010;376(9742):687-697. [doi:10.1016/S0140-6736(10)61121-X](https://doi.org/10.1016/S0140-6736(10)61121-X) · [PubMed 20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/)
[^janjigian-2021-checkmate649]: Janjigian YY, Shitara K, Moehler M, et al. First-line nivolumab plus chemotherapy versus chemotherapy alone for advanced gastric, gastro-oesophageal junction, and oesophageal adenocarcinoma (CheckMate 649). *Lancet.* 2021;398(10294):27-40. [doi:10.1016/S0140-6736(21)00797-2](https://doi.org/10.1016/S0140-6736(21)00797-2) · [PubMed 34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/)
