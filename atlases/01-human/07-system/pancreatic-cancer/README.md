---
schema: human-scale-entry/v1
id: pancreatic-cancer
name: Pancreatic Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Aggressive exocrine malignancy; KRAS mutations in >90%, TP53 in ~75%, CDKN2A and SMAD4 in ~50%; desmoplastic stroma limits drug delivery. FOLFIRINOX and gemcitabine+nab-paclitaxel are standards; KRAS inhibitors (sotorasib for G12C) and BRCA-mutant PARP inhibitors are active."
aliases: ["PDAC", "pancreatic ductal adenocarcinoma", "pancreatic adenocarcinoma", "exocrine pancreatic cancer", "metastatic PDAC", "borderline resectable pancreatic cancer"]
sources:
  - id: conroy-2011-folfirinox
    type: peer-reviewed
    cite: "Conroy T, Desseigne F, Ychou M, et al. FOLFIRINOX versus gemcitabine for metastatic pancreatic cancer. N Engl J Med. 2011;364(19):1817-1825."
    doi: "10.1056/NEJMoa1011923"
    pmid: "21561347"
    url: "https://doi.org/10.1056/NEJMoa1011923"
  - id: golan-2019-polo
    type: peer-reviewed
    cite: "Golan T, Hammel P, Reni M, et al. Maintenance olaparib for germline BRCA-mutated metastatic pancreatic cancer. N Engl J Med. 2019;381(4):317-327."
    doi: "10.1056/NEJMoa1903387"
    pmid: "31157963"
    url: "https://doi.org/10.1056/NEJMoa1903387"
  - id: von-hoff-2013-abraxane
    type: peer-reviewed
    cite: "Von Hoff DD, Ervin T, Arena FP, et al. Increased survival in pancreatic cancer with nab-paclitaxel plus gemcitabine. N Engl J Med. 2013;369(18):1691-1703."
    doi: "10.1056/NEJMoa1304369"
    pmid: "24131140"
    url: "https://doi.org/10.1056/NEJMoa1304369"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS is mutated in >90% of PDAC (G12D ~40%, G12V ~33%, G12R ~16%); constitutive RAS → RAF-MEK-ERK drives proliferation and survival; KRAS G12C inhibitors show modest activity in the rare G12C subset; pan-KRAS and KRAS G12D inhibitors are under active clinical development."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta drives pancreatic desmoplasia via stellate cell activation → dense stroma limits chemo delivery; SMAD4 loss (~50% of PDAC) → TGF-beta loses tumor suppression; TGF-beta becomes pro-invasive and immunosuppressive in SMAD4-null PDAC; anti-TGF-beta combinations under study."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1/2 germline mutations occur in ~5-10% of PDAC; olaparib maintenance (POLO trial) improved PFS in BRCA-mutant platinum-responsive mPDAC (7.4 vs. 3.8 months); somatic BRCA mutations in ~3%; homologous recombination deficiency testing guides PARP inhibitor selection."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR is overexpressed in ~60% of PDAC; erlotinib + gemcitabine modestly improves OS vs. gemcitabine alone (NCIC PA.3: OS 6.24 vs. 5.91 months; HR 0.82) — the only approved targeted therapy before KRAS inhibitors; anti-EGFR antibodies (cetuximab) are ineffective in PDAC."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A (p16/INK4a) deleted/silenced in ~95% of PDAC; second earliest driver after KRAS; p16 loss → CDK4/6-RB hyperphosphorylation → unrestricted S-phase entry; ARF co-deletion → MDM2 unchecked → p53 suppressed; CDK4/6 inhibitors (palbociclib) evaluated in p16-null PDAC."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations in ~70-75% of PDAC; p53 LOF → G2/M checkpoint failure and apoptosis evasion; late PanIN-3→PDAC transition event (vs KRAS = early); gain-of-function mutants (R175H, R248W) promote invasion; APR-246 (mutant p53 reactivator) in early PDAC trials."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "SMAD4 (DPC4) loss in ~55% of PDAC switches TGF-β from tumor suppressor to pro-invasive driver; SMAD4 loss predicts systemic metastasis vs local recurrence in SMAD4-intact; TGF-β → non-SMAD (RAS-ERK, PI3K) → EMT; SMAD4 IHC predicts spread in resected PDAC."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Pancreatic ductal adenocarcinoma arises from the pancreas's exocrine ductal epithelium, growing silently until it obstructs the bile duct (painless jaundice) or invades vessels; deep location and early spread mean only ~20% are resectable, survival near 12% at 5 years."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Pancreatic cancer is defined by its stroma: KRAS-driven tumor cells activate stellate cells into cancer-associated fibroblasts that build a dense, hypovascular desmoplastic matrix starving the tumor of drugs and excluding T cells — why PDAC resists chemo and immunotherapy."
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "Hereditary pancreatitis (germline PRSS1, SPINK1) is a major pancreatic cancer risk: decades of recurring autodigestion and inflammation create a field of injury that, with smoking, drives a ~40-50× lifetime risk of pancreatic adenocarcinoma — among the highest predispositions."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "New-onset diabetes can be the first sign of pancreatic cancer: tumor-secreted paraneoplastic insulin resistance causes diabetes months before diagnosis, so new diabetes after 50 with weight loss—rather than weight gain—warrants suspicion of pancreatic adenocarcinoma."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Pancreatic cancer is the classic cause of Trousseau syndrome: mucin and tissue-factor release make it among the most thrombogenic cancers, producing migratory superficial thrombophlebitis, DVT, and pulmonary embolism—sometimes the presenting clue before the tumor."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Peutz-Jeghers syndrome carries one of the highest hereditary pancreatic cancer risks: germline STK11/LKB1 loss raises lifetime risk to ~11-36%, so PJS patients—alongside BRCA2, CDKN2A, and Lynch carriers—are candidates for pancreatic surveillance with MRI/EUS."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Pancreatic cancer is part of the Li-Fraumeni spectrum: germline TP53 loss raises its risk, and somatic TP53 mutation is one of the four near-universal drivers of pancreatic ductal adenocarcinoma—linking the inherited p53 syndrome to a lethal tumor."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy has a contested but real role in pancreatic cancer: chemoradiation or stereotactic body radiation can downstage tumors and palliate local symptoms, though early spread means systemic chemotherapy carries most of the treatment burden."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Pancreatic ductal adenocarcinoma and pancreatic neuroendocrine tumors are different cancers of one organ: PDAC is an aggressive KRAS-driven exocrine cancer, while pancreatic NETs arise from islet cells and are often indolent—same gland, opposite biology."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "BRCA2 makes pancreatic cancer hereditary and treatable: germline BRCA2 (and PALB2) loss raises risk and creates homologous-recombination deficiency, so these tumors respond to platinum chemotherapy and PARP inhibitors—a rare targeted opening in a grim cancer."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "New-onset diabetes can be the first sign of pancreatic cancer: the tumor impairs insulin secretion and induces insulin resistance, so unexplained diabetes after age 50—especially with weight loss—warrants considering an occult pancreatic cancer."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is pancreatic cancer's main metastatic site and a route to jaundice: a head tumor obstructs the bile duct causing painless jaundice, while spread seeds the liver—so liver involvement and biliary obstruction dominate the clinical picture."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Pancreatic cancer frustrates anti-VEGF therapy: despite secreting VEGF, the tumor builds a dense, poorly vascular desmoplastic stroma that walls off blood flow and drug delivery, so antiangiogenic agents have largely failed—part of why PDAC is so chemoresistant."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Pancreatic cancer is among the deadliest cancers of the digestive system: arising silently in the pancreas, it obstructs the bile duct (painless jaundice) and invades nerves and vessels, so most present unresectable—making it a leading cause of cancer death."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Pancreatic cancer is an immune-cold tumor: a dense immunosuppressive, fibroblast-rich stroma excludes T cells, so checkpoint immunotherapy that works elsewhere largely fails here—except in the rare mismatch-repair-deficient subset that responds to PD-1 blockade."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Pancreatic cancer hides behind a wall of collagen: its intense desmoplastic stroma packs dense collagen that compresses vessels and blocks drug delivery, a major reason chemotherapy penetrates poorly and the tumor is so hard to treat."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Pancreatic cancer is a target for cancer vaccines: personalized mRNA neoantigen vaccines (e.g., autogene cevumeran) can induce tumor-specific cytotoxic T cells, and patients who mount a strong CD8 response show delayed recurrence after surgery."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Lynch syndrome is among the inherited causes of pancreatic cancer: MMR-gene carriers face a several-fold increased risk, so Lynch joins BRCA, Peutz-Jeghers and familial pancreatitis on the panel of syndromes prompting familial pancreatic surveillance."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Pancreatic cancer is addicted to autophagy: its KRAS-driven cells recycle their own contents to fuel growth in a nutrient-poor stroma, so blocking autophagy (with hydroxychloroquine plus MEK/ERK inhibitors) is a leading strategy against this lethal cancer."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Pancreatic cancer fills its stroma with suppressive macrophages: tumor-associated macrophages dominate the dense desmoplasia, blocking T cells and feeding growth—a pillar of the immunosuppression that makes PDAC resist checkpoint therapy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Pancreatic cancer is the coldest of tumors, walled off by regulatory T cells: Tregs and a dense stroma exclude and suppress cytotoxic T cells, which is why immunotherapy that works elsewhere repeatedly fails against PDAC."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Pancreatic cancer hides in a near-airless tumor: its dense stroma squeezes the blood vessels, leaving the tumor profoundly hypoxic, which drives aggressive behavior and blocks delivery of chemotherapy—a core reason PDAC is so lethal."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Pancreatic cancer is mostly scar: cancer-associated fibroblasts pack the tumor with a dense desmoplastic fibrosis that walls off immune cells and drugs, so this stromal armor is as much a treatment obstacle as the cancer cells themselves."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Pancreatic cancer announces itself by blocking the gut's bile and food path: tumors in the head compress the bile duct and duodenum, causing painless jaundice and obstruction, often the first sign of a cancer already hard to cure."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Tobacco's carbon carcinogens drive pancreatic cancer: smoking is the leading modifiable cause, its combustion products reaching the pancreas to mutate its cells, roughly doubling the risk."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Pancreatic body and tail tumors clot the splenic vein: lying against the spleen's vein, they thrombose it, causing gastric varices and an enlarged spleen (left-sided portal hypertension)."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Pancreatic cancer turns platelets into clots: it is the classic cause of Trousseau syndrome, activating platelets to produce migratory thrombophlebitis and venous clots that can precede the diagnosis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Pancreatic cancer crawls along nerves: perineural invasion is a hallmark, the tumor tracking down the nerve sheaths around the gland to cause the relentless boring back pain — and to recur after surgery by routes the scalpel can't reach."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "A pancreatic tumor can throttle the stomach: cancers of the head and body grow into the adjacent duodenum and gastric outlet, blocking the passage of food so that vomiting and gastric obstruction become a late, distressing complication."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "After the liver, the lung is pancreatic cancer's next stop: hematogenous metastases seed the lungs, and a pattern of lung-only spread carries a somewhat better outlook than the more usual liver and peritoneal disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "FOLFIRINOX's price is the nerves: oxaliplatin, a pillar of pancreatic cancer chemotherapy, injures peripheral sensory neurons, causing a cold-triggered tingling and numbness that can force dose cuts and linger after treatment ends."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Pancreatic cancer starves the body of protein: profound cachexia and poor intake drop blood albumin, and a low albumin marks the wasting and inflammation that predict shorter survival and poorer tolerance of treatment."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Treatment leaks magnesium away: platinum chemotherapy and EGFR-blocking erlotinib both injure the kidney's handling of magnesium, so levels are tracked and replaced through the course of pancreatic cancer care."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "CA19-9 is read by an antibody: the marker is measured by an immunoassay to follow response and relapse, though it misses Lewis-negative patients, and antibody stains for CK7 and SMAD4 loss help confirm pancreatic origin on a tiny biopsy."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Losing the pancreas makes diabetes treacherous: as the tumor and surgery destroy the alpha cells that make glucagon along with the insulin-making beta cells, the body loses its defense against lows, leaving a brittle diabetes prone to dangerous hypoglycemia."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "FOLFIRINOX and gemcitabine batter the marrow: the chemotherapy backbones of pancreatic cancer are strongly myelosuppressive, dropping neutrophil counts so that growth-factor support and infection vigilance run through every cycle."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Pancreatic cancer melts the body away: it drives a profound cachexia that burns through adipocyte fat stores and muscle, and its disruption of insulin and digestion brings new-onset diabetes and weight loss that are often the first clues to the tumor."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression can precede the diagnosis: pancreatic cancer is classically linked to depression that appears before any pain or jaundice, a paraneoplastic mood change thought to be biologically driven rather than merely a reaction to illness."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "One gene ties pancreas to skin: germline CDKN2A mutations cause the FAMMM syndrome, raising the risk of both pancreatic cancer and melanoma, so families with clustered melanomas warrant pancreatic surveillance."
  - target: 01-human/03-molecular/palb2
    relation: connects-to
    note: "Another repair gene marks familial cases: germline PALB2 mutations, BRCA2's binding partner in homologous-recombination repair, predispose to pancreatic cancer and, like BRCA, leave the tumor sensitive to platinum chemotherapy and PARP inhibitors."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "The stroma builds a chemical wall: cancer-associated fibroblasts pour out CXCL12, which coats the tumor and keeps killer T cells out, a key reason pancreatic cancer resists immunotherapy and a target for breaking down that barrier."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Excess weight stacks the odds: obesity raises pancreatic cancer risk through chronic inflammation, insulin resistance and fatty infiltration of the gland, one of the modifiable contributors to a cancer otherwise dominated by genetics and smoking."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pancreatic cancer is defined by its pain: perineural invasion and tumor wrapping the celiac plexus produce severe, relentless back and abdominal pain, often needing a celiac plexus block — a hallmark of the disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Blocked bile and major surgery breed sepsis: tumor obstruction of the bile duct causes cholangitis, and the Whipple resection it requires can leak and infect, so biliary and post-operative sepsis are real threats."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 drives the desmoplastic tumor: persistent STAT3 signaling in pancreatic cancer cells and their dense stroma promotes proliferation, fibrosis, and immune evasion, marking a node studied for targeted therapy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "KRAS routes survival through NF-κB: constitutive NF-κB activity downstream of mutant KRAS sustains pancreatic-cancer-cell survival, inflammation and chemoresistance, a hard-to-drug hub central to the disease's lethality."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "It is the classic Trousseau cancer: mucin-secreting pancreatic adenocarcinoma activates coagulation so strongly it can cause migratory thrombophlebitis and chronic disseminated intravascular coagulation, sometimes the first clue to the tumor."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Cachexia and inflammation drain the blood: the intense inflammatory and catabolic state of pancreatic cancer suppresses erythropoiesis, producing an anemia of chronic disease that compounds its profound weight loss."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Loss of the exocrine pancreas starves bone of vitamin D: tumor obstruction and resection cause fat malabsorption, and the resulting deficiency of vitamin D and calcium, on top of cachexia, drives metabolic bone loss toward osteoporosis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Gemcitabine can injure the kidneys: a backbone of pancreatic-cancer chemotherapy, gemcitabine occasionally triggers a thrombotic microangiopathy and hemolytic-uremic syndrome that scars the kidney toward chronic disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its fluoropyrimidine can stun the heart: the 5-fluorouracil in FOLFIRINOX can provoke coronary vasospasm and direct myocardial toxicity, occasionally precipitating acute cardiac dysfunction and heart failure."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "BRCA mutations reach the pancreas: germline BRCA2 and BRCA1 carriers face raised pancreatic-cancer risk, and BRCA-mutant tumours are uniquely sensitive to platinum and PARP-inhibitor maintenance."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "The Whipple is a formidable wound: pancreaticoduodenectomy is major surgery whose pancreatic anastomosis is notorious for leak, and malnutrition and jaundice leave these wounds slow and prone to breakdown."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "One of the grimmest diagnoses breeds dread: the very poor survival, rapid course and relentless symptom burden of pancreatic cancer fuel intense anxiety alongside its well-known depression."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "New diabetes can be its first sign: pancreatic cancer destroys islet tissue to cause new-onset diabetes, often heralding the cancer, and a Whipple resection leaves both endocrine and exocrine insufficiency."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It wraps around the body's nerve plexus: pancreatic cancer invades the coeliac plexus, causing severe back pain treated by neurolysis, and it can present with a paraneoplastic depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It seeds the lungs and clots them: the lung is a common site of pancreatic-cancer metastasis, and its strong prothrombotic state (Trousseau) causes pulmonary emboli."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It spreads early through the nodes: pancreatic cancer involves peripancreatic and distant lymph nodes including the left supraclavicular Virchow's node, a marker of advanced disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It writes its prothrombotic state on the skin: the lipase it releases can cause pancreatic panniculitis with tender skin nodules, and Trousseau migratory thrombophlebitis appears as recurrent superficial clots."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It clots the heart's valves: its intense prothrombotic state causes marantic (non-bacterial thrombotic) endocarditis, which can throw emboli to the brain alongside its venous thromboses."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A few tumours have a target: PARP inhibitors help BRCA-mutated pancreatic cancer, and KRAS-G12C and other inhibitors are emerging against this notoriously treatment-resistant cancer."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It wastes the body: pancreatic cancer causes profound cachexia with severe muscle loss, and advanced disease can metastasise to bone."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It obstructs and its drugs reach the kidney: tumour or nodes can compress the ureters, and platinum chemotherapy is nephrotoxic."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "FOLFIRINOX is the most active regimen: FOLFIRINOX or gemcitabine with nab-paclitaxel is the chemotherapy backbone for pancreatic adenocarcinoma, given around Whipple surgery and for advanced disease."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "A profoundly cold tumour: dense desmoplastic stroma and few infiltrating T cells leave pancreatic cancer largely unresponsive to checkpoint inhibitors, except the rare microsatellite-unstable case."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "New-onset diabetes can herald it: pancreatic cancer impairs and destroys the islets of Langerhans, and unexplained new diabetes in an older adult can be an early paraneoplastic sign."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "A profoundly cold tumour: pancreatic ductal adenocarcinoma's dense desmoplastic stroma excludes T cells and rarely forms tertiary lymphoid structures, so it lacks the germinal-centre immune organisation that would let checkpoint inhibitors work."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Two desmoplastic foregut adenocarcinomas: pancreatic cancer and cholangiocarcinoma share a dense fibrotic stroma, late presentation, gemcitabine-based chemotherapy and a grim prognosis, arising from the linked pancreatic and biliary ductal systems."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Both ride the KRAS pathway differently: nearly all pancreatic cancers are KRAS-driven and long untargetable, while KRAS-mutant colorectal cancers add druggable context like anti-EGFR resistance and G12C inhibitors—two windows on one oncogene."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver is the dominant metastatic site: pancreatic cancer drains via the portal vein to the liver, seeding the hepatic lobule, the spread that leaves most patients incurable at diagnosis."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Aggressive upper-GI adenocarcinomas: pancreatic and gastric cancer share late presentation, desmoplastic biology, peritoneal spread and grim prognosis—the lethal upper-gastrointestinal malignancies."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Duodenal invasion and obstruction: a pancreatic head tumour invades the adjacent duodenum, eroding the intestinal epithelium to cause bleeding and gastric-outlet obstruction."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "The line between operable and not: pancreatic cancer's tendency to encase the celiac axis and superior mesenteric artery defines borderline-resectable and unresectable disease, making arterial-wall involvement the key surgical decision point."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Trousseau's hypercoagulability: pancreatic cancer is among the most thrombogenic tumours, causing migratory thrombophlebitis, VTE and nonbacterial thrombotic endocarditis that can throw emboli to the brain and cause stroke."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "CFTR and the pancreas: cystic fibrosis chronically damages the exocrine pancreas, and CFTR carriers and patients carry a modestly raised lifetime risk of pancreatic cancer."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Cooperating oncogene: MYC amplification cooperates with mutant KRAS to drive the proliferation and metabolic rewiring of pancreatic cancer."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic stroma: the dense, poorly perfused desmoplastic stroma of pancreatic cancer stabilises HIF-1α, driving metabolic adaptation and resistance to chemotherapy."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Rare actionable fusion: NTRK gene fusions, though uncommon, offer one of the few targeted-therapy options in otherwise treatment-resistant pancreatic cancer."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: AKT signalling downstream of KRAS sustains pancreatic cancer cell survival and metabolism, contributing to its profound treatment resistance."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: with CDKN2A loss near-universal in pancreatic cancer, cyclin D-CDK4/6 activity drives unrestrained passage through the G1 checkpoint."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes in pancreatic cancer, promoting proliferation and metastasis as an epigenetic target."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Myeloid immunosuppression: pancreatic cancer secretes CCL2 to recruit CCR2+ monocytes that become tumour-associated macrophages, a dominant arm of the immunosuppressive desmoplastic stroma that keeps PDAC resistant to checkpoint therapy."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Cachexia and inflammation: tumour- and stroma-derived IL-6 drives the JAK-STAT3 signalling behind PDAC's profound cachexia and links chronic pancreatitis to pancreatic carcinogenesis."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "Hedgehog desmoplasia: tumour SHH signals through stromal SMO to drive the dense fibrotic stroma that walls off PDAC, raising interstitial pressure and impeding chemotherapy delivery."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "DNA-repair predisposition: germline ATM mutations are among the commonest familial pancreatic-cancer alleles, and ATM-deficient tumours, like BRCA-mutant ones, accumulate the homologous-recombination defects that sensitise PDAC to platinum and PARP inhibitors."
  - target: 01-human/03-molecular/prss1
    relation: connects-to
    note: "Hereditary pancreatitis: gain-of-function PRSS1 mutations cause recurrent trypsin-driven pancreatitis from childhood, and the lifelong inflammation of hereditary pancreatitis carries one of the highest known risks of progression to pancreatic adenocarcinoma."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis evasion: gemcitabine and FOLFIRINOX kill PDAC cells through caspase-3-mediated apoptosis, but the apoptotic resistance conferred by KRAS-driven survival signalling underlies the chemoresistance that makes this one of the deadliest cancers."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "PanIN progression: NOTCH signalling is reactivated downstream of mutant KRAS to drive the acinar-to-ductal metaplasia and PanIN precursor lesions of pancreatic cancer, and sustains the desmoplastic, stem-like phenotype of established tumours."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Mesenchymal resistance: AXL receptor tyrosine kinase drives epithelial-mesenchymal transition, gemcitabine resistance and immune evasion in PDAC, marking the aggressive mesenchymal subtype and motivating AXL inhibitors in combination therapy."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Desmoplastic stroma: tumour-derived PDGF activates pancreatic stellate cells into the cancer-associated fibroblasts that lay down PDAC's dense collagenous stroma, the physical barrier that impairs drug delivery and shields tumour cells."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "KRAS effector: mutant KRAS (mapped), present in ~90% of PDAC, signals through the MAPK-ERK cascade as the central proliferative driver and the focus of KRAS- and MEK-directed therapy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth axis: mTOR completes the PI3K-AKT-mTOR pathway (AKT already mapped) that, alongside KRAS-MAPK, sustains the growth and metabolism of pancreatic cancer."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle release: CDKN2A loss (mapped) frees the cyclin-D1-CDK4/6 axis to phosphorylate RB and release E2F1, driving the cell-cycle progression of pancreatic cancer."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Desmoplasia and cachexia: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped) drives the desmoplastic, immunosuppressive stroma and the cancer cachexia characteristic of pancreatic ductal adenocarcinoma."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "KRAS-NRF2 redox: oncogenic KRAS upregulates NRF2 antioxidant signalling, and the resulting redox balance supports the proliferation and chemoresistance of pancreatic cancer."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbiota-driven carcinogenesis: gut- and pancreatic-microbiota-driven TLR-MyD88-NF-κB signalling (NF-κB already mapped) promotes the inflammation-associated initiation and progression of pancreatic ductal adenocarcinoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is abundantly expressed in the desmoplastic stroma of pancreatic cancer, promoting fibrosis, KRAS signalling and immune evasion."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT and mTOR mapped) cooperates with KRAS in driving pancreatic cancer."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING signalling in the pancreatic-cancer microenvironment shapes the immunologically cold phenotype that limits immunotherapy response."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the weak antitumour immunity of the immunologically cold pancreatic ductal adenocarcinoma."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDKN2A loss (CDKN2A and cyclin-D1 already mapped) releases CDK4/6-cyclin-D control of the cell cycle, a near-universal lesion in pancreatic cancer."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO tumour-suppressor activity, antagonised by KRAS-driven PI3K-AKT signalling, is lost in the progression of pancreatic cancer."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-delivered cytotoxic killing by CD8 T and NK cells is the immune-clearance axis that the immune-cold, desmoplastic pancreatic cancer evades."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in pancreatic cancer."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from myeloid-derived suppressor cells shape the immunosuppressive desmoplastic stroma of pancreatic cancer."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates the NF-κB and survival signaling of pancreatic cancer, a candidate therapeutic target."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) downstream of KRAS supports the survival of pancreatic cancer cells."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of EGFR and AXL (both already mapped) drives the invasion of pancreatic cancer."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of pancreatic cancer."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive desmoplastic microenvironment of pancreatic cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of pancreatic cancer."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of pancreatic cancer."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the desmoplastic tumor microenvironment of pancreatic cancer."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of pancreatic cancer."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Cancer cachexia: pancreatic cancer causes profound skeletal-muscle wasting, and tumour-derived activin A signalling through the ActRIIB receptor is a principal driver of that muscle atrophy, the dominant cause of the weakness and weight loss that shorten survival."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Cold immune evasion: pancreatic cancer is immunologically cold with a dense suppressive stroma, and impaired MHC class II antigen presentation blunts the CD4 T-cell help needed for anti-tumour immunity, part of why checkpoint blockade has largely failed here."
  - target: 01-human/03-molecular/cftr
    relation: connects-to
    note: "Predisposing pancreatitis: CFTR dysfunction causes chronic pancreatitis, and the resulting recurrent inflammation is a recognised risk pathway to pancreatic cancer alongside the hereditary-pancreatitis PRSS1 axis already mapped."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Cancer pain: pancreatic cancer causes severe visceral and back pain from coeliac-plexus involvement, managed with opioids acting at the mu-opioid receptor and with coeliac-plexus neurolysis, a defining palliative challenge of the disease."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cold-tumour immunotherapy: IL-2-driven T-cell expansion underlies the adoptive and vaccine approaches being tried to overcome the immunosuppressive stroma of pancreatic cancer, in which checkpoint blockade (MHC class II already mapped) has largely failed."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: pancreatic cancer lowers haemoglobin through chronic disease, occult gastrointestinal blood loss from duodenal invasion and chemotherapy myelosuppression, adding to the fatigue and cachexia (activin-A already mapped) of advanced disease."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive stroma: IL-10, with the TGF-beta (already mapped) of the desmoplastic stroma and its macrophages (already mapped), makes pancreatic cancer an immunologically cold tumour in which checkpoint blockade has largely failed."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative carcinogenesis: chronic pancreatitis and smoking generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage (NRF2 already mapped) helps drive the KRAS-initiated (already mapped) carcinogenesis of pancreatic cancer."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Radiotherapy: stereotactic body and proton radiotherapy delivering ionising radiation are used for locally advanced, borderline-resectable pancreatic cancer, aiming to improve local control and resectability of this hard-to-treat tumour."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "COX-2 carcinogenesis: cyclooxygenase-2 and prostaglandin E2 from the chronic pancreatitis and tumour inflammation (IL-6 and IL-1 already mapped) promote the proliferation and immunosuppression of the KRAS-driven (already mapped) carcinogenesis of pancreatic cancer."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the dense desmoplastic stroma, part of the immune-excluded, cold microenvironment of pancreatic cancer."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia of malignancy: the chronic disease, gastrointestinal bleeding and chemotherapy of pancreatic cancer cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immune-excluded, cold desmoplastic microenvironment of pancreatic cancer."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Cancer cachexia: the profound weight loss and cancer cachexia (IL-6 and activin-A already mapped) of pancreatic cancer are reflected in the fall in the adipokine leptin as the adipose tissue is depleted."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic risk and cachexia: adiponectin, with leptin (already mapped), links the obesity and metabolic syndrome (insulin already mapped) that raise pancreatic-cancer risk to the adipose-tissue wasting of its cachexia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the obesity risk to the cachexia and the inflammation (IL-6 already mapped) of pancreatic cancer."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and produces the anaemia of chronic disease (haemoglobin already mapped) of pancreatic cancer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "HRD innate signalling: type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the DNA damage of the BRCA/HRD (already mapped) pancreatic cancer, is explored to make the immunologically 'cold' tumour immunogenic."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the (sparse) tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm largely excluded by the desmoplastic, immunosuppressive stroma of pancreatic cancer."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response, explored against the immunologically cold pancreatic cancer."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immunosuppressive microenvironment of pancreatic cancer."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK dysfunction: the natural killer cells (perforin already mapped) are suppressed and excluded by the desmoplastic (fibroblast already mapped), immunologically cold microenvironment of pancreatic cancer."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the pro-tumorigenic inflammation of pancreatic cancer."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the pancreatic-cancer microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Desmoplastic mast cells: the mast cells infiltrate the desmoplastic stroma (collagen already mapped) and contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment of pancreatic cancer."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) recruits and polarises the myeloid-derived suppressor cells that drive the profound immunosuppression of the pancreatic-cancer microenvironment."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Stromal vitamin: the vitamin D receptor ligand reprogrammes the activated stellate cells/fibroblasts (already mapped) of the desmoplastic stroma, a candidate stromal-modulating strategy in pancreatic cancer."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, marks the rare immune-responsive subset of the immunologically cold pancreatic cancer."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 and C5aR1 already mapped) contribute to the myeloid-driven immunosuppression of the pancreatic-cancer microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the pancreatic-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped) within the desmoplastic microenvironment."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Stromal alarmin: TSLP released from the desmoplastic pancreatic stroma activates mast cells and promotes the Th2-skewed, immunosuppressive microenvironment that enables pancreatic cancer to evade cytotoxic immunity."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Desmoplastic scaffold: periostin, a TGF-β-induced ECM component, is a major constituent of the desmoplastic stroma that encases pancreatic cancer, promoting tumour cell survival, invasion and resistance to gemcitabine."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Cancer-cachexia anaemia: erythropoietin addresses the anaemia of the cancer-cachexia and chemotherapy-related marrow suppression in pancreatic cancer; EPOR expression on tumour cells has been documented."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Tumour-pain kinin: bradykinin released by the kallikrein-kinin system in the desmoplastic stroma activates nociceptive B1/B2 receptors on peripancreatic and coeliac nerve fibres, driving the intractable pain of pancreatic cancer."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: C1-esterase inhibitor restrains the complement and contact-activation pathways in the pancreatic-cancer stroma, limiting the C3/C5/C5aR1 (all already mapped) cascade sustaining the immunosuppressive microenvironment."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Stromal mast-cell mediator: histamine from mast cells (already mapped) in the desmoplastic stroma promotes angiogenesis (VEGF already mapped) and T-cell suppression, reinforcing the immunologically cold microenvironment of pancreatic cancer."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Pancreatic cancer melatonin: melatonin inhibits KRAS (already mapped)-driven pancreatic cancer proliferation by suppressing the mTOR (already mapped) and Wnt/β-catenin (already mapped) pathways via MT1/MT2-mediated cAMP reduction, counteracting the desmoplastic stroma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Pancreatic cancer androgen axis: testosterone via androgen receptor modulates pancreatic stellate-cell (already mapped) activation and the desmoplastic stroma, and AR signalling intersects the KRAS (already mapped) and mTOR (already mapped) growth pathways in pancreatic cancer."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Pancreatic neuroendocrine serotonin: serotonin co-produced by serotonin-secreting pancreatic neuroendocrine cells modulates cAMP-PKA signalling; elevated 5-HIAA in KRAS (already mapped)-driven tumours reflects neuroendocrine differentiation in pancreatic cancer."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Pancreatic cancer prolactin: prolactin via JAK2/STAT3 (already mapped) activates pancreatic cancer cells and tumour-associated macrophages (already mapped), augmenting NF-κB (already mapped)-driven desmoplastic stroma and mTOR (already mapped) pro-proliferative signalling."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Pancreatic cancer oxytocin: oxytocin receptors on pancreatic cancer cells and stellate cells couple to Gαq-PKC, cross-activating KRAS (already mapped) and mTOR (already mapped) signalling to promote desmoplastic stroma remodelling and cancer cell invasion."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Pancreatic cancer vasopressin: vasopressin via V1a receptors on pancreatic cancer stroma activates Gαq-PKC signalling, promoting VEGF (already mapped)-driven tumour angiogenesis and NF-κB (already mapped)-mediated cancer-associated fibroblast (already mapped) activation."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Pancreatic cancer selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the pancreatic tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Pancreatic cancer iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade in pancreatic cancer."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Pancreatic cancer sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the T-cytotoxic (already mapped) suppression in pancreatic cancer."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Pancreatic cancer calcium: calcium gates NLRP3 in macrophages (already mapped) and mast-cells (already mapped); calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and suppresses T-cytotoxic (already mapped) anti-tumour function in pancreatic cancer."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Pancreatic cancer copper: copper enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustain tumour immunity; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) mast-cell (already mapped) skewing cascade in pancreatic cancer."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Pancreatic cancer potassium: potassium efflux gates macrophage (already mapped) NLRP3; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade suppressing mast-cell (already mapped) and T-cytotoxic (already mapped) function in pancreatic cancer."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Pancreatic cancer chloride: chloride channels in macrophages (already mapped) and tumour cells modulate cell-volume and invasive potential; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of pancreatic cancer."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Pancreatic cancer hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and tumour cells, supports lipid signalling; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of pancreatic cancer."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Pancreatic cancer nitrogen: nitrogen in amino-acid scaffold of KRAS and NF-κB (already mapped) proteins in tumour cells sustains oncogenic signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of pancreatic cancer."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Pancreatic cancer phosphorus: phosphorus in ATP and phospholipid membranes of tumour cells and macrophages (already mapped) drives KRAS signalling; phosphorus depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of pancreatic cancer."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Pancreatic cancer sulfur: sulfur in cysteine residues of KRAS and NF-κB (already mapped) proteins in tumour cells sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of pancreatic cancer."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Pancreatic cancer PD-1: PD-1 on tumour-infiltrating T-cells (already mapped) and macrophages (already mapped) suppresses anti-tumour immunity; PD-1 checkpoint dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of pancreatic cancer."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Pancreatic cancer glp-1: GLP-1 from macrophages (already mapped) and fibroblasts (already mapped) modulates metabolic-inflammatory tumour tone; glp-1 dysfunction amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of pancreatic cancer."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Pancreatic cancer angiotensin-ii: angiotensin-II from macrophages (already mapped) and endothelial cells (already mapped) drives angiogenesis; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of pancreatic cancer."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Pancreatic cancer wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and fibroblasts (already mapped) drives invasion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of pancreatic cancer."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "PanCa rankl: RANKL from macrophages (already mapped) and fibroblasts (already mapped) promotes pancreatic tumour immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "PanCa fibronectin: fibronectin in macrophages (already mapped) and fibroblasts (already mapped) promotes pancreatic ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "PanCa igf-1: IGF-1 from macrophages (already mapped) and fibroblasts (already mapped) promotes pancreatic tumour cell survival; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "PanCa cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates pancreatic cancer neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "PanCa calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates pancreatic cancer calcium balance; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "PanCa substance-p: substance-P from macrophages (already mapped) and fibroblasts (already mapped) modulates pancreatic cancer immune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer."
---

# Pancreatic Cancer

## Overview

**Pancreatic ductal adenocarcinoma (PDAC)** is the most common and deadly form of pancreatic cancer, arising from ductal epithelial cells of the exocrine pancreas. Despite accounting for only ~3% of new cancer diagnoses in the United States (~65,000 cases/year), PDAC is the **third leading cause of cancer death** (~50,000 deaths/year; 5-year OS ~13%) due to late-stage diagnosis, rapid disease progression, and deep intrinsic resistance to most cytotoxic agents and immunotherapy. Median OS in metastatic PDAC was <6 months before 2011; modern combination chemotherapy (FOLFIRINOX) improved median OS to ~11 months in fit patients [^conroy-2011-folfirinox].

**Incidence, risk, and epidemiology:**
- **Age:** Median diagnosis age ~70; rare before 45; increasing incidence in younger adults correlating with obesity and T2DM
- **Risk factors:** Smoking (2-3× RR; 25% of PDAC attributable to tobacco), obesity (BMI >35: 1.5× RR), chronic pancreatitis (10-15× lifetime risk), new-onset diabetes (possible early PDAC marker — DM developing in elderly patients without risk factors), heavy alcohol use
- **Hereditary risk (~10-15% of PDAC):**
  - *BRCA2* mutation (3-10× RR; ~5-8% of PDAC), BRCA1 (~2-3× RR)
  - *PALB2* mutation (~3× RR)
  - *ATM* mutation (~3× RR)
  - *CDKN2A* mutation (Familial atypical multiple mole melanoma; FAMMM syndrome — lifetime PCa risk ~17%)
  - *PRSS1* (hereditary pancreatitis) → ~40% lifetime PDAC risk
  - *STK11* (Peutz-Jeghers syndrome) → ~35% lifetime PDAC risk
  - *MLH1/MSH2/MSH6* (Lynch syndrome) → modest PDAC risk increase
  - Familial pancreatic cancer (FPC): ≥2 first-degree relatives → 4-6× RR; genetic basis not always identified
- **Germline testing:** Recommended for all patients with PDAC regardless of family history (NCCN guidelines) — identifies therapy implications (PARP inhibitors, platinum sensitivity) and enables family counseling

**PDAC vs. other pancreatic malignancies:**
- **PDAC (~85%):** The dominant lethal form; duct cells → mucin-producing adenocarcinoma
- **Neuroendocrine tumors (PanNETs, ~10%):** Often indolent; surgery curative for localized; everolimus and sunitinib for advanced; often functional (insulinoma, glucagonoma, VIPoma); well-differentiated (Grade 1-2) vs. poorly differentiated (Grade 3/NEPC); KRAS-wildtype; good prognosis in low-grade disease
- **Acinar cell carcinoma (~1%):** Lipase-secreting; BRCA2 mutations common; responds to platinum; better prognosis than PDAC
- **Intraductal papillary mucinous neoplasm (IPMN):** Precursor lesion → variable malignant potential; main duct IPMN has high (~50-70%) malignant potential → resection; branch duct IPMN followed by MRI unless features of high risk (solid component, main duct involvement)

## Structure

### Pancreatic anatomy and ductal architecture

**Anatomical regions:**
- **Head (right):** ~70% of PDAC; surrounds the common bile duct (CBD) and ampulla of Vater → early biliary obstruction → jaundice is often the presenting symptom; relationship to superior mesenteric artery (SMA), SMV/portal vein determines resectability
- **Body (center):** ~20% of PDAC; lies anterior to the aorta and posterior gastric surface; wraps superior mesenteric vessels; most vascular involvement is here
- **Tail (left):** ~10% of PDAC; extends to the hilum of the spleen; often silent until large — presents at later stage; most common site for PanNETs; distal pancreatectomy + splenectomy for resectable tail tumors

**Ductal anatomy:**
- Main pancreatic duct (duct of Wirsung): Runs length of pancreas → joins CBD at ampulla of Vater → major duodenal papilla; obstruction by pancreatic head tumors → upstream duct dilatation ("double duct sign" on CT/ERCP)
- Accessory duct (Santorini): Drains into minor papilla; anatomical variant (~30% of people)

**PDAC precursor lesions:**
- **Pancreatic intraepithelial neoplasia (PanIN):** Most common precursor; 3 grades (PanIN-1A, 1B, 2, 3 = carcinoma in situ); PanIN-1: KRAS mutation (earliest event); PanIN-2: CDKN2A loss; PanIN-3: TP53 and SMAD4 loss; progression takes ~20 years but is largely asymptomatic
- **IPMN:** Gross precursor (visible on imaging); main duct > branch duct risk; mucin-producing; KRAS, GNAS (camp/RAS signaling), SMAD4 mutations
- **Mucinous cystic neoplasm (MCN):** Exclusively in women (ovarian stroma); main duct not involved; resection recommended

**Molecular pathogenesis — genetic progression model:**
1. Normal ductal epithelium → KRAS mutation (PanIN-1): ~100% of PDAC carry KRAS mutation; earliest driver
2. CDKN2A (p16/INK4a) loss → PanIN-2: ~90% of PDAC; loss allows CDK4/6-driven cell cycle progression
3. TP53 mutation → PanIN-3: ~75% of PDAC; loss of G2/M checkpoint and apoptosis regulation
4. SMAD4 (DPC4) loss → metastasis: ~50% of PDAC; SMAD4 loss → TGF-beta switches from suppressor to promoter of invasion and immune exclusion

## Function

### Clinical presentation and diagnosis

**Symptoms (highly varied by location):**
- **Head PDAC:** Painless obstructive jaundice (bilirubin elevation → scleral icterus → dark urine, pale stools), weight loss, anorexia, pruritus (bile salt deposition); Courvoisier sign: palpable non-tender gallbladder + jaundice (suggests malignant obstruction rather than stone)
- **Body/tail PDAC:** Vague epigastric/back pain (celiac plexus invasion), weight loss, new-onset diabetes, migratory thrombophlebitis (Trousseau syndrome — hypercoagulability via tumor TF and mucin)
- **General:** Weight loss (often profound, >10% body weight), fatigue, depression (can precede diagnosis — depression as paraneoplastic); venous thromboembolic events (DVT, PE) — 15% of PDAC have VTE at or before diagnosis

**Biomarkers:**
- **CA 19-9:** Sialylated Lewis antigen; elevated in ~80% of PDAC; sensitivity ~79%, specificity ~82% for pancreatic cancer vs. benign conditions; normal in ~5-10% due to Lewis antigen negativity (Se antigen genotype → no CA 19-9 production regardless of PDAC); useful for monitoring response and detecting recurrence, not for screening
- **CEA:** Elevated in ~50% of PDAC; less specific than CA 19-9; combined CA 19-9 + CEA monitoring improves sensitivity

**Imaging:**
- **CT (triple phase pancreas protocol):** Defines tumor location, ductal/vascular involvement, liver metastases, peritoneal disease; thin-slice axial + MPR reconstructions; arteries (SMA, celiac, hepatic) and veins (SMV, portal vein) evaluated for contact, abutment, or encasement — determines resectability classification
- **MRI/MRCP:** Superior soft tissue contrast; useful for IPMN characterization, liver characterization, and perineural invasion detection
- **Endoscopic ultrasound (EUS):** Gold standard for diagnosis — fine needle aspiration (FNA) or biopsy (FNB/core); highest sensitivity for small pancreatic masses (<2 cm); provides tissue for pathology, molecular profiling, and KRAS G12D NGS
- **PET-CT:** Not standard for initial staging; useful for detecting occult metastases before surgery in high-risk cases; FDG-avid PDAC confirmed metastasis → changes surgery plan

**Resectability criteria (NCCN/AHPBA):**
- **Resectable:** No arterial (SMA, celiac, CHA) contact; ≤180° SMV/portal vein contact; no distant metastases
- **Borderline resectable (BRPC):** 180°-360° SMV/PV contact (reconstructable), ≤180° SMA contact, short CHA contact; requires preoperative chemotherapy → restaging → surgery if response
- **Locally advanced (LAPC):** >360° SMA or celiac involvement; SMA or celiac encasement; aorta involvement; typically unresectable; aggressive chemotherapy (FOLFIRINOX) → conversion resection in ~10-15%
- **Metastatic:** Liver, peritoneal, lung metastases; chemotherapy and supportive care only

## Pathology

### Diagnosis and molecular profiling

**Histopathology:** PDAC — duct-like glands surrounded by dense desmoplastic stroma (~90% stroma by volume in some tumors); perineural invasion, lymphovascular invasion, regional node involvement are common; R0 vs. R1 (positive margin) resection is the most important surgical quality metric

**Molecular profiling at diagnosis:**
- **KRAS genotyping:** Critical for KRAS-targeted therapy eligibility; G12C (~2-3% of PDAC) → sotorasib or adagrasib eligible; G12D (~40%) → MRTX1133, RMC-9805 under investigation
- **HRR (homologous recombination repair) genes:** BRCA1/2, PALB2, ATM, BRIP1, RAD51C/D — germline and somatic testing; HRR-deficient PDAC → platinum sensitivity + PARP inhibitor maintenance [^golan-2019-polo]
- **MSI/MMR:** Rare in PDAC (<2%); pembrolizumab eligible if MSI-H
- **NTRK fusions:** Rare (<1%); larotrectinib or entrectinib eligible
- **TMB-high:** Pembrolizumab (tissue-agnostic)

### Treatment

**Resectable PDAC:**
- **Surgery:** Pancreaticoduodenectomy (Whipple procedure) for head tumors; distal pancreatectomy + splenectomy for body/tail; total pancreatectomy (rare); robotic-assisted increasingly common; lymph node harvest ≥15 nodes required for adequate staging; mortality <3% at high-volume centers
- **Adjuvant chemotherapy (CONKO-001, ESPAC-4, PRODIGE 24/CCTG):**
  - Modified FOLFIRINOX (mFOLFIRINOX) × 24 weeks: DFS 21.4 vs. 12.8 months; OS 54.4 vs. 35.0 months (PRODIGE 24; preferred for fit patients)
  - Gemcitabine + capecitabine (GemCap; ESPAC-4): OS 28.0 vs. 25.5 months vs. gemcitabine alone
  - Gemcitabine alone: Historical standard (CONKO-001); now largely superseded

**Borderline resectable/locally advanced — neoadjuvant:**
- mFOLFIRINOX × 4-6 months → restaging CT → surgery if resectability criteria met; landmark Alliance A021101: feasibility established; LAP07 trial (chemo vs. CRT for LAPC): no OS difference; stereotactic body radiotherapy (SBRT) or MR-linac adaptive RT as consolidation for LAPC (SCALOP, CONKO-007)

**Metastatic PDAC:**
- **FOLFIRINOX (FFX):** Oxaliplatin + irinotecan + leucovorin + fluorouracil; first-line for ECOG PS 0-1, adequate biliary drainage, no neuropathy; OS 11.1 vs. 6.8 months vs. gemcitabine (PRODIGE 4/ACCORD 11); ORR 31.6%; diarrhea, fatigue, neutropenia, neuropathy are key toxicities [^conroy-2011-folfirinox]
- **Gemcitabine + nab-paclitaxel (gem-nabP):** First-line for ECOG PS 0-2; OS 8.5 vs. 6.7 months vs. gemcitabine alone; ORR 23% (MPACT trial); neurotoxicity and myelosuppression; preferred in PS 2 or comorbidity that precludes FFX [^von-hoff-2013-abraxane]
- **Olaparib maintenance (POLO trial):** For germline BRCA1/2-mutant mPDAC not progressed on ≥16 weeks platinum-based chemotherapy; PFS 7.4 vs. 3.8 months (HR 0.53); no OS benefit (may reflect crossover); FDA-approved December 2019 [^golan-2019-polo]
- **KRAS G12C-directed therapy:** Sotorasib and adagrasib have modest activity as monotherapy (ORR ~20%) in KRAS G12C-mutant PDAC; G12C represents only ~2-3% of PDAC; combinations with SHP2 inhibitors, MEK inhibitors, and anti-EGFR underway
- **Second-line chemotherapy:** Nanoliposomal irinotecan (nal-IRI) + 5-FU/LV (NAPOLI-1: OS 6.1 vs. 4.2 months) — FDA-approved for post-gemcitabine; FOLFIRINOX if gem-nabP first-line; oxaliplatin + 5-FU/LV (OFF) for third-line

**Immunotherapy in PDAC:**
- Largely ineffective due to: (1) dense immunosuppressive desmoplastic stroma; (2) low TMB and low neoantigen burden in KRAS-mutant PDAC; (3) abundant MDSCs, TAMs (M2), and Tregs; (4) CXCL17 and galectin → exclusion of CD8+ T cells
- **MSI-H/MMR-deficient PDAC (<2%):** Pembrolizumab (KEYNOTE-158: ORR 18.2%); pembrolizumab first-line for MSI-H PDAC
- **Combination strategies under study:** Anti-PD-1 + anti-LAG-3, anti-PD-1 + CD40 agonist, anti-PD-1 + TGF-beta blockade, STING agonists, CAR-T (mesothelin, CEA targets); stroma-depleting strategies (hyaluronidase, anti-FAP CAR-T)

**Supportive care:**
- **Pancreatic enzyme replacement (PERT):** Required for exocrine insufficiency → malabsorption → weight loss; Creon 40,000+ units per meal
- **Pain:** Celiac plexus neurolysis (EUS-guided or CT-guided) — effective for abdominal/back pain; early palliative care integration associated with improved QoL and OS
- **Biliary obstruction:** ERCP + metal biliary stent (preferred); percutaneous transhepatic cholangiography (PTC) if ERCP fails
- **Gastric outlet obstruction:** Duodenal stent or surgical bypass (gastrojejunostomy)
- **DVT/PE:** Anticoagulation (LMWH preferred in cancer; direct oral anticoagulants in selected patients); VTE prevention with LMWH in high-risk ambulatory patients (AVERT/CASSINI trials)

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS is mutated in >90% of PDAC (G12D ~40%, G12V ~33%, G12R ~16%); constitutive RAS → RAF-MEK-ERK drives proliferation and survival; KRAS G12C inhibitors show modest activity in the rare G12C subset; pan-KRAS and KRAS G12D inhibitors are under active clinical development.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta drives pancreatic desmoplasia via stellate cell activation → dense stroma limits chemo delivery; SMAD4 loss (~50% of PDAC) → TGF-beta loses tumor suppression; TGF-beta becomes pro-invasive and immune-exclusionary in SMAD4-null PDAC; anti-TGF-beta combinations under study.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — BRCA1/2 germline mutations occur in ~5-10% of PDAC; olaparib maintenance (POLO trial) improved PFS in BRCA-mutant platinum-responsive mPDAC (7.4 vs. 3.8 months); somatic BRCA mutations in ~3%; homologous recombination deficiency testing guides PARP inhibitor selection.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR is overexpressed in ~60% of PDAC; erlotinib + gemcitabine modestly improves OS vs. gemcitabine alone (NCIC PA.3: OS 6.24 vs. 5.91 months; HR 0.82) — the only approved targeted therapy before KRAS inhibitors; anti-EGFR monoclonal antibodies (cetuximab) are ineffective in PDAC.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A (p16/INK4a) deleted/silenced in ~95% of PDAC; second earliest driver after KRAS; p16 loss → CDK4/6-RB hyperphosphorylation → unrestricted S-phase entry; ARF co-deletion → MDM2 unchecked → p53 suppressed; CDK4/6 inhibitors (palbociclib) evaluated in p16-null PDAC.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations in ~70-75% of PDAC; p53 LOF → G2/M checkpoint failure and apoptosis evasion; late PanIN-3→PDAC transition event (vs KRAS = early); gain-of-function mutants (R175H, R248W) promote invasion; APR-246 (mutant p53 reactivator) in early PDAC trials.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — SMAD4 (DPC4) loss in ~55% of PDAC switches TGF-β from tumor suppressor to pro-invasive driver; SMAD4 loss predicts systemic metastasis vs local recurrence in SMAD4-intact; TGF-β → non-SMAD (RAS-ERK, PI3K) → EMT; SMAD4 IHC predicts spread in resected PDAC.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Pancreatic ductal adenocarcinoma arises from the pancreas's exocrine ductal epithelium, growing silently until it obstructs the bile duct (painless jaundice) or invades vessels; deep location and early spread mean only ~20% are resectable, survival near 12% at 5 years.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Pancreatic cancer is defined by its stroma: KRAS-driven tumor cells activate stellate cells into cancer-associated fibroblasts that build a dense, hypovascular desmoplastic matrix starving the tumor of drugs and excluding T cells — why PDAC resists chemo and immunotherapy.
- `connects-to` → **[Hereditary Pancreatitis](../hereditary-pancreatitis/README.md)** — Hereditary pancreatitis (germline PRSS1, SPINK1) is a major pancreatic cancer risk: decades of recurring autodigestion and inflammation create a field of injury that, with smoking, drives a ~40-50× lifetime risk of pancreatic adenocarcinoma — among the highest predispositions.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — New-onset diabetes can be the first sign of pancreatic cancer: tumor-secreted paraneoplastic insulin resistance causes diabetes months before diagnosis, so new diabetes after 50 with weight loss—rather than weight gain—warrants suspicion of pancreatic adenocarcinoma.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Pancreatic cancer is the classic cause of Trousseau syndrome: mucin and tissue-factor release make it among the most thrombogenic cancers, producing migratory superficial thrombophlebitis, DVT, and pulmonary embolism—sometimes the presenting clue before the tumor.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Peutz-Jeghers syndrome carries one of the highest hereditary pancreatic cancer risks: germline STK11/LKB1 loss raises lifetime risk to ~11-36%, so PJS patients—alongside BRCA2, CDKN2A, and Lynch carriers—are candidates for pancreatic surveillance with MRI/EUS.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Pancreatic cancer is part of the Li-Fraumeni spectrum: germline TP53 loss raises its risk, and somatic TP53 mutation is one of the four near-universal drivers of pancreatic ductal adenocarcinoma—linking the inherited p53 syndrome to a lethal tumor.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy has a contested but real role in pancreatic cancer: chemoradiation or stereotactic body radiation can downstage tumors and palliate local symptoms, though early spread means systemic chemotherapy carries most of the treatment burden.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Pancreatic ductal adenocarcinoma and pancreatic neuroendocrine tumors are different cancers of one organ: PDAC is an aggressive KRAS-driven exocrine cancer, while pancreatic NETs arise from islet cells and are often indolent—same gland, opposite biology.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — BRCA2 makes pancreatic cancer hereditary and treatable: germline BRCA2 (and PALB2) loss raises risk and creates homologous-recombination deficiency, so these tumors respond to platinum chemotherapy and PARP inhibitors—a rare targeted opening in a grim cancer.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — New-onset diabetes can be the first sign of pancreatic cancer: the tumor impairs insulin secretion and induces insulin resistance, so unexplained diabetes after age 50—especially with weight loss—warrants considering an occult pancreatic cancer.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is pancreatic cancer's main metastatic site and a route to jaundice: a head tumor obstructs the bile duct causing painless jaundice, while spread seeds the liver—so liver involvement and biliary obstruction dominate the clinical picture.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Pancreatic cancer frustrates anti-VEGF therapy: despite secreting VEGF, the tumor builds a dense, poorly vascular desmoplastic stroma that walls off blood flow and drug delivery, so antiangiogenic agents have largely failed—part of why PDAC is so chemoresistant.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Pancreatic cancer is among the deadliest cancers of the digestive system: arising silently in the pancreas, it obstructs the bile duct (painless jaundice) and invades nerves and vessels, so most present unresectable—making it a leading cause of cancer death.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Pancreatic cancer is an immune-cold tumor: a dense immunosuppressive, fibroblast-rich stroma excludes T cells, so checkpoint immunotherapy that works elsewhere largely fails here—except in the rare mismatch-repair-deficient subset that responds to PD-1 blockade.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Pancreatic cancer hides behind a wall of collagen: its intense desmoplastic stroma packs dense collagen that compresses vessels and blocks drug delivery, a major reason chemotherapy penetrates poorly and the tumor is so hard to treat.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Pancreatic cancer is a target for cancer vaccines: personalized mRNA neoantigen vaccines (e.g., autogene cevumeran) can induce tumor-specific cytotoxic T cells, and patients who mount a strong CD8 response show delayed recurrence after surgery.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Lynch syndrome is among the inherited causes of pancreatic cancer: MMR-gene carriers face a several-fold increased risk, so Lynch joins BRCA, Peutz-Jeghers and familial pancreatitis on the panel of syndromes prompting familial pancreatic surveillance.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Pancreatic cancer is addicted to autophagy: its KRAS-driven cells recycle their own contents to fuel growth in a nutrient-poor stroma, so blocking autophagy (with hydroxychloroquine plus MEK/ERK inhibitors) is a leading strategy against this lethal cancer.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Pancreatic cancer fills its stroma with suppressive macrophages: tumor-associated macrophages dominate the dense desmoplasia, blocking T cells and feeding growth—a pillar of the immunosuppression that makes PDAC resist checkpoint therapy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Pancreatic cancer is the coldest of tumors, walled off by regulatory T cells: Tregs and a dense stroma exclude and suppress cytotoxic T cells, which is why immunotherapy that works elsewhere repeatedly fails against PDAC.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Pancreatic cancer hides in a near-airless tumor: its dense stroma squeezes the blood vessels, leaving the tumor profoundly hypoxic, which drives aggressive behavior and blocks delivery of chemotherapy—a core reason PDAC is so lethal.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Pancreatic cancer is mostly scar: cancer-associated fibroblasts pack the tumor with a dense desmoplastic fibrosis that walls off immune cells and drugs, so this stromal armor is as much a treatment obstacle as the cancer cells themselves.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Pancreatic cancer announces itself by blocking the gut's bile and food path: tumors in the head compress the bile duct and duodenum, causing painless jaundice and obstruction, often the first sign of a cancer already hard to cure.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Tobacco's carbon carcinogens drive pancreatic cancer: smoking is the leading modifiable cause, its combustion products reaching the pancreas to mutate its cells, roughly doubling the risk.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Pancreatic body and tail tumors clot the splenic vein: lying against the spleen's vein, they thrombose it, causing gastric varices and an enlarged spleen (left-sided portal hypertension).
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Pancreatic cancer turns platelets into clots: it is the classic cause of Trousseau syndrome, activating platelets to produce migratory thrombophlebitis and venous clots that can precede the diagnosis.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Pancreatic cancer crawls along nerves: perineural invasion is a hallmark, the tumor tracking down the nerve sheaths around the gland to cause the relentless boring back pain — and to recur after surgery by routes the scalpel can't reach.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — A pancreatic tumor can throttle the stomach: cancers of the head and body grow into the adjacent duodenum and gastric outlet, blocking the passage of food so that vomiting and gastric obstruction become a late, distressing complication.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — After the liver, the lung is pancreatic cancer's next stop: hematogenous metastases seed the lungs, and a pattern of lung-only spread carries a somewhat better outlook than the more usual liver and peritoneal disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — FOLFIRINOX's price is the nerves: oxaliplatin, a pillar of pancreatic cancer chemotherapy, injures peripheral sensory neurons, causing a cold-triggered tingling and numbness that can force dose cuts and linger after treatment ends.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Pancreatic cancer starves the body of protein: profound cachexia and poor intake drop blood albumin, and a low albumin marks the wasting and inflammation that predict shorter survival and poorer tolerance of treatment.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Treatment leaks magnesium away: platinum chemotherapy and EGFR-blocking erlotinib both injure the kidney's handling of magnesium, so levels are tracked and replaced through the course of pancreatic cancer care.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — CA19-9 is read by an antibody: the marker is measured by an immunoassay to follow response and relapse, though it misses Lewis-negative patients, and antibody stains for CK7 and SMAD4 loss help confirm pancreatic origin on a tiny biopsy.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Losing the pancreas makes diabetes treacherous: as the tumor and surgery destroy the alpha cells that make glucagon along with the insulin-making beta cells, the body loses its defense against lows, leaving a brittle diabetes prone to dangerous hypoglycemia.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — FOLFIRINOX and gemcitabine batter the marrow: the chemotherapy backbones of pancreatic cancer are strongly myelosuppressive, dropping neutrophil counts so that growth-factor support and infection vigilance run through every cycle.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Pancreatic cancer melts the body away: it drives a profound cachexia that burns through adipocyte fat stores and muscle, and its disruption of insulin and digestion brings new-onset diabetes and weight loss that are often the first clues to the tumor.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression can precede the diagnosis: pancreatic cancer is classically linked to depression that appears before any pain or jaundice, a paraneoplastic mood change thought to be biologically driven rather than merely a reaction to illness.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — One gene ties pancreas to skin: germline CDKN2A mutations cause the FAMMM syndrome, raising the risk of both pancreatic cancer and melanoma, so families with clustered melanomas warrant pancreatic surveillance.
- `connects-to` → **[PALB2](../../03-molecular/palb2/README.md)** — Another repair gene marks familial cases: germline PALB2 mutations, BRCA2's binding partner in homologous-recombination repair, predispose to pancreatic cancer and, like BRCA, leave the tumor sensitive to platinum chemotherapy and PARP inhibitors.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — The stroma builds a chemical wall: cancer-associated fibroblasts pour out CXCL12, which coats the tumor and keeps killer T cells out, a key reason pancreatic cancer resists immunotherapy and a target for breaking down that barrier.
- `connects-to` → **[Obesity](../obesity/README.md)** — Excess weight stacks the odds: obesity raises pancreatic cancer risk through chronic inflammation, insulin resistance and fatty infiltration of the gland, one of the modifiable contributors to a cancer otherwise dominated by genetics and smoking.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pancreatic cancer is defined by its pain: perineural invasion and tumor wrapping the celiac plexus produce severe, relentless back and abdominal pain, often needing a celiac plexus block — a hallmark of the disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Blocked bile and major surgery breed sepsis: tumor obstruction of the bile duct causes cholangitis, and the Whipple resection it requires can leak and infect, so biliary and post-operative sepsis are real threats.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 drives the desmoplastic tumor: persistent STAT3 signaling in pancreatic cancer cells and their dense stroma promotes proliferation, fibrosis, and immune evasion, marking a node studied for targeted therapy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — KRAS routes survival through NF-κB: constitutive NF-κB activity downstream of mutant KRAS sustains pancreatic-cancer-cell survival, inflammation and chemoresistance, a hard-to-drug hub central to the disease's lethality.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — It is the classic Trousseau cancer: mucin-secreting pancreatic adenocarcinoma activates coagulation so strongly it can cause migratory thrombophlebitis and chronic disseminated intravascular coagulation, sometimes the first clue to the tumor.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Cachexia and inflammation drain the blood: the intense inflammatory and catabolic state of pancreatic cancer suppresses erythropoiesis, producing an anemia of chronic disease that compounds its profound weight loss.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Loss of the exocrine pancreas starves bone of vitamin D: tumor obstruction and resection cause fat malabsorption, and the resulting deficiency of vitamin D and calcium, on top of cachexia, drives metabolic bone loss toward osteoporosis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Gemcitabine can injure the kidneys: a backbone of pancreatic-cancer chemotherapy, gemcitabine occasionally triggers a thrombotic microangiopathy and hemolytic-uremic syndrome that scars the kidney toward chronic disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its fluoropyrimidine can stun the heart: the 5-fluorouracil in FOLFIRINOX can provoke coronary vasospasm and direct myocardial toxicity, occasionally precipitating acute cardiac dysfunction and heart failure.
- `connects-to` → **[Hereditary Breast & Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — BRCA mutations reach the pancreas: germline BRCA2 and BRCA1 carriers face raised pancreatic-cancer risk, and BRCA-mutant tumours are uniquely sensitive to platinum and PARP-inhibitor maintenance.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — The Whipple is a formidable wound: pancreaticoduodenectomy is major surgery whose pancreatic anastomosis is notorious for leak, and malnutrition and jaundice leave these wounds slow and prone to breakdown.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — One of the grimmest diagnoses breeds dread: the very poor survival, rapid course and relentless symptom burden of pancreatic cancer fuel intense anxiety alongside its well-known depression.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — New diabetes can be its first sign: pancreatic cancer destroys islet tissue to cause new-onset diabetes, often heralding the cancer, and a Whipple resection leaves both endocrine and exocrine insufficiency.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It wraps around the body's nerve plexus: pancreatic cancer invades the coeliac plexus, causing severe back pain treated by neurolysis, and it can present with a paraneoplastic depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It seeds the lungs and clots them: the lung is a common site of pancreatic-cancer metastasis, and its strong prothrombotic state (Trousseau) causes pulmonary emboli.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It spreads early through the nodes: pancreatic cancer involves peripancreatic and distant lymph nodes including the left supraclavicular Virchow's node, a marker of advanced disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It writes its prothrombotic state on the skin: the lipase it releases can cause pancreatic panniculitis with tender skin nodules, and Trousseau migratory thrombophlebitis appears as recurrent superficial clots.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It clots the heart's valves: its intense prothrombotic state causes marantic (non-bacterial thrombotic) endocarditis, which can throw emboli to the brain alongside its venous thromboses.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A few tumours have a target: PARP inhibitors help BRCA-mutated pancreatic cancer, and KRAS-G12C and other inhibitors are emerging against this notoriously treatment-resistant cancer.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It wastes the body: pancreatic cancer causes profound cachexia with severe muscle loss, and advanced disease can metastasise to bone.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It obstructs and its drugs reach the kidney: tumour or nodes can compress the ureters, and platinum chemotherapy is nephrotoxic.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — FOLFIRINOX is the most active regimen: FOLFIRINOX or gemcitabine with nab-paclitaxel is the chemotherapy backbone for pancreatic adenocarcinoma, given around Whipple surgery and for advanced disease.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — A profoundly cold tumour: dense desmoplastic stroma and few infiltrating T cells leave pancreatic cancer largely unresponsive to checkpoint inhibitors, except the rare microsatellite-unstable case.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — New-onset diabetes can herald it: pancreatic cancer impairs and destroys the islets of Langerhans, and unexplained new diabetes in an older adult can be an early paraneoplastic sign.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — A profoundly cold tumour: pancreatic ductal adenocarcinoma's dense desmoplastic stroma excludes T cells and rarely forms tertiary lymphoid structures, so it lacks the germinal-centre immune organisation that would let checkpoint inhibitors work.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Two desmoplastic foregut adenocarcinomas: pancreatic cancer and cholangiocarcinoma share a dense fibrotic stroma, late presentation, gemcitabine-based chemotherapy and a grim prognosis, arising from the linked pancreatic and biliary ductal systems.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Both ride the KRAS pathway differently: nearly all pancreatic cancers are KRAS-driven and long untargetable, while KRAS-mutant colorectal cancers add druggable context like anti-EGFR resistance and G12C inhibitors—two windows on one oncogene.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver is the dominant metastatic site: pancreatic cancer drains via the portal vein to the liver, seeding the hepatic lobule, the spread that leaves most patients incurable at diagnosis.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Aggressive upper-GI adenocarcinomas: pancreatic and gastric cancer share late presentation, desmoplastic biology, peritoneal spread and grim prognosis—the lethal upper-gastrointestinal malignancies.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Duodenal invasion and obstruction: a pancreatic head tumour invades the adjacent duodenum, eroding the intestinal epithelium to cause bleeding and gastric-outlet obstruction.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — The line between operable and not: pancreatic cancer's tendency to encase the celiac axis and superior mesenteric artery defines borderline-resectable and unresectable disease, making arterial-wall involvement the key surgical decision point.
- `connects-to` → **[Stroke](../stroke/README.md)** — Trousseau's hypercoagulability: pancreatic cancer is among the most thrombogenic tumours, causing migratory thrombophlebitis, VTE and nonbacterial thrombotic endocarditis that can throw emboli to the brain and cause stroke.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — CFTR and the pancreas: cystic fibrosis chronically damages the exocrine pancreas, and CFTR carriers and patients carry a modestly raised lifetime risk of pancreatic cancer.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Cooperating oncogene: MYC amplification cooperates with mutant KRAS to drive the proliferation and metabolic rewiring of pancreatic cancer.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic stroma: the dense, poorly perfused desmoplastic stroma of pancreatic cancer stabilises HIF-1α, driving metabolic adaptation and resistance to chemotherapy.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — Rare actionable fusion: NTRK gene fusions, though uncommon, offer one of the few targeted-therapy options in otherwise treatment-resistant pancreatic cancer.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: AKT signalling downstream of KRAS sustains pancreatic cancer cell survival and metabolism, contributing to its profound treatment resistance.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: with CDKN2A loss near-universal in pancreatic cancer, cyclin D-CDK4/6 activity drives unrestrained passage through the G1 checkpoint.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes in pancreatic cancer, promoting proliferation and metastasis as an epigenetic target.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Pancreatic cancer secretes CCL2 to recruit CCR2+ monocytes that become tumor-associated macrophages, a dominant arm of the immunosuppressive desmoplastic stroma that keeps PDAC resistant to checkpoint therapy despite high stromal content.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Tumor- and stroma-derived IL-6 drives the JAK-STAT3 signaling behind PDAC's profound cachexia, and chronic IL-6 inflammation links long-standing pancreatitis to the carcinogenesis that initiates the disease.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — Tumor Sonic hedgehog signals through stromal SMO to drive the dense fibrotic stroma that walls off PDAC, raising interstitial pressure and impeding the chemotherapy delivery that makes this cancer so treatment-refractory.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — Germline ATM mutations are among the commonest familial pancreatic-cancer alleles, and ATM-deficient tumors, like BRCA-mutant ones, accumulate the homologous-recombination defects that sensitize PDAC to platinum and PARP inhibitors.
- `connects-to` → **[PRSS1](../../03-molecular/prss1/README.md)** — Gain-of-function PRSS1 mutations cause recurrent trypsin-driven pancreatitis from childhood, and the lifelong inflammation of hereditary pancreatitis carries one of the highest known risks of progression to pancreatic adenocarcinoma.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Gemcitabine and FOLFIRINOX kill PDAC cells through caspase-3-mediated apoptosis, but the apoptotic resistance conferred by KRAS-driven survival signaling underlies the chemoresistance that makes this one of the deadliest cancers.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling is reactivated downstream of mutant KRAS to drive the acinar-to-ductal metaplasia and PanIN precursor lesions of pancreatic cancer, and sustains the desmoplastic, stem-like phenotype of established tumors.
- `connects-to` → **[AXL Receptor Tyrosine Kinase](../../03-molecular/axl-receptor/README.md)** — AXL drives epithelial-mesenchymal transition, gemcitabine resistance and immune evasion in PDAC, marking the aggressive mesenchymal subtype and motivating AXL inhibitors in combination therapy.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Tumor-derived PDGF activates pancreatic stellate cells into the cancer-associated fibroblasts that lay down PDAC's dense collagenous stroma, the physical barrier that impairs drug delivery and shields tumor cells.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Mutant KRAS (mapped), present in ~90% of PDAC, signals through the MAPK-ERK cascade as the central proliferative driver and the focus of KRAS- and MEK-directed therapy.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR completes the PI3K-AKT-mTOR pathway (AKT already mapped) that, alongside KRAS-MAPK, sustains the growth and metabolism of pancreatic cancer.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — CDKN2A loss (mapped) frees the cyclin-D1-CDK4/6 axis to phosphorylate RB and release E2F1, driving the cell-cycle progression of pancreatic cancer.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped) drives the desmoplastic, immunosuppressive stroma and the cancer cachexia characteristic of pancreatic ductal adenocarcinoma.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Oncogenic KRAS upregulates NRF2 antioxidant signaling, and the resulting redox balance supports the proliferation and chemoresistance of pancreatic cancer.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Gut- and pancreatic-microbiota-driven TLR-MyD88-NF-κB signaling (NF-κB already mapped) promotes the inflammation-associated initiation and progression of pancreatic ductal adenocarcinoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is abundantly expressed in the desmoplastic stroma of pancreatic cancer, promoting fibrosis, KRAS signaling and immune evasion.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT and mTOR mapped) cooperates with KRAS in driving pancreatic cancer.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING signaling in the pancreatic-cancer microenvironment shapes the immunologically cold phenotype that limits immunotherapy response.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the weak antitumor immunity of the immunologically cold pancreatic ductal adenocarcinoma.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDKN2A loss (CDKN2A and cyclin-D1 already mapped) releases CDK4/6-cyclin-D control of the cell cycle, a near-universal lesion in pancreatic cancer.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO tumor-suppressor activity, antagonized by KRAS-driven PI3K-AKT signaling, is lost in the progression of pancreatic cancer.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-delivered cytotoxic killing by CD8 T and NK cells is the immune-clearance axis that the immune-cold, desmoplastic pancreatic cancer evades.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in pancreatic cancer.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from myeloid-derived suppressor cells shape the immunosuppressive desmoplastic stroma of pancreatic cancer.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates the NF-κB and survival signaling of pancreatic cancer, a candidate therapeutic target.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) downstream of KRAS supports the survival of pancreatic cancer cells.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of EGFR and AXL (both already mapped) drives the invasion of pancreatic cancer.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of pancreatic cancer.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive desmoplastic microenvironment of pancreatic cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of pancreatic cancer.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of pancreatic cancer.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the desmoplastic tumor microenvironment of pancreatic cancer.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of pancreatic cancer.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Cancer cachexia: pancreatic cancer causes profound skeletal-muscle wasting, and tumour-derived activin A signalling through the ActRIIB receptor is a principal driver of that muscle atrophy, the dominant cause of the weakness and weight loss that shorten survival.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Cold immune evasion: pancreatic cancer is immunologically cold with a dense suppressive stroma, and impaired MHC class II antigen presentation blunts the CD4 T-cell help needed for anti-tumour immunity, part of why checkpoint blockade has largely failed here.
- `connects-to` → **[CFTR](../../03-molecular/cftr/README.md)** — Predisposing pancreatitis: CFTR dysfunction causes chronic pancreatitis, and the resulting recurrent inflammation is a recognised risk pathway to pancreatic cancer alongside the hereditary-pancreatitis PRSS1 axis already mapped.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Cancer pain: pancreatic cancer causes severe visceral and back pain from coeliac-plexus involvement, managed with opioids acting at the mu-opioid receptor and with coeliac-plexus neurolysis, a defining palliative challenge of the disease.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cold-tumour immunotherapy: IL-2-driven T-cell expansion underlies the adoptive and vaccine approaches being tried to overcome the immunosuppressive stroma of pancreatic cancer, in which checkpoint blockade (MHC class II already mapped) has largely failed.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: pancreatic cancer lowers haemoglobin through chronic disease, occult gastrointestinal blood loss from duodenal invasion and chemotherapy myelosuppression, adding to the fatigue and cachexia (activin-A already mapped) of advanced disease.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive stroma: IL-10, with the TGF-beta (already mapped) of the desmoplastic stroma and its macrophages (already mapped), makes pancreatic cancer an immunologically cold tumour in which checkpoint blockade has largely failed.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative carcinogenesis: chronic pancreatitis and smoking generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative DNA damage (NRF2 already mapped) helps drive the KRAS-initiated (already mapped) carcinogenesis of pancreatic cancer.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Radiotherapy: stereotactic body and proton radiotherapy delivering ionising radiation are used for locally advanced, borderline-resectable pancreatic cancer, aiming to improve local control and resectability of this hard-to-treat tumour.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — COX-2 carcinogenesis: cyclooxygenase-2 and prostaglandin E2 from the chronic pancreatitis and tumour inflammation (IL-6 and IL-1 already mapped) promote the proliferation and immunosuppression of the KRAS-driven (already mapped) carcinogenesis of pancreatic cancer.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the dense desmoplastic stroma, part of the immune-excluded, cold microenvironment of pancreatic cancer.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia of malignancy: the chronic disease, gastrointestinal bleeding and chemotherapy of pancreatic cancer cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immune-excluded, cold desmoplastic microenvironment of pancreatic cancer.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Cancer cachexia: the profound weight loss and cancer cachexia (IL-6 and activin-A already mapped) of pancreatic cancer are reflected in the fall in the adipokine leptin as the adipose tissue is depleted.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic risk and cachexia: adiponectin, with leptin (already mapped), links the obesity and metabolic syndrome (insulin already mapped) that raise pancreatic-cancer risk to the adipose-tissue wasting of its cachexia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the obesity risk to the cachexia and the inflammation (IL-6 already mapped) of pancreatic cancer.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and produces the anaemia of chronic disease (haemoglobin already mapped) of pancreatic cancer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — HRD innate signalling: type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the DNA damage of the BRCA/HRD (already mapped) pancreatic cancer, is explored to make the immunologically 'cold' tumour immunogenic.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the (sparse) tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm largely excluded by the desmoplastic, immunosuppressive stroma of pancreatic cancer.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response, explored against the immunologically cold pancreatic cancer.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immunosuppressive microenvironment of pancreatic cancer.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK dysfunction: the natural killer cells (perforin already mapped) are suppressed and excluded by the desmoplastic (fibroblast already mapped), immunologically cold microenvironment of pancreatic cancer.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the pro-tumorigenic inflammation of pancreatic cancer.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the pancreatic-cancer microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Desmoplastic mast cells: the mast cells infiltrate the desmoplastic stroma (collagen already mapped) and contribute to the angiogenesis (VEGF already mapped) and type-2 microenvironment of pancreatic cancer.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) recruits and polarises the myeloid-derived suppressor cells that drive the profound immunosuppression of the pancreatic-cancer microenvironment.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Stromal vitamin: the vitamin D receptor ligand reprogrammes the activated stellate cells/fibroblasts (already mapped) of the desmoplastic stroma, a candidate stromal-modulating strategy in pancreatic cancer.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, marks the rare immune-responsive subset of the immunologically cold pancreatic cancer.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 and C5aR1 already mapped) contribute to the myeloid-driven immunosuppression of the pancreatic-cancer microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the pancreatic-cancer cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped) within the desmoplastic microenvironment.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Stromal alarmin: TSLP released from the desmoplastic pancreatic stroma activates mast cells and promotes the Th2-skewed, immunosuppressive microenvironment that enables pancreatic cancer to evade cytotoxic immunity.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Desmoplastic scaffold: periostin, a TGF-β-induced ECM component, is a major constituent of the desmoplastic stroma that encases pancreatic cancer, promoting tumour cell survival, invasion and resistance to gemcitabine.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Cancer-cachexia anaemia: erythropoietin addresses the anaemia of the cancer-cachexia and chemotherapy-related marrow suppression in pancreatic cancer; EPOR expression on tumour cells has been documented.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Tumour-pain kinin: bradykinin released by the kallikrein-kinin system in the desmoplastic stroma activates nociceptive B1/B2 receptors on peripancreatic and coeliac nerve fibres, driving the intractable pain of pancreatic cancer.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: C1-esterase inhibitor restrains the complement and contact-activation pathways in the pancreatic-cancer stroma, limiting the C3/C5/C5aR1 (all already mapped) cascade sustaining the immunosuppressive microenvironment.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Stromal mast-cell mediator: histamine from mast cells (already mapped) in the desmoplastic stroma promotes angiogenesis (VEGF already mapped) and T-cell suppression, reinforcing the immunologically cold microenvironment of pancreatic cancer.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Pancreatic cancer melatonin: melatonin inhibits KRAS (already mapped)-driven pancreatic cancer proliferation by suppressing the mTOR (already mapped) and Wnt/β-catenin (already mapped) pathways via MT1/MT2-mediated cAMP reduction, counteracting the desmoplastic stroma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Pancreatic cancer androgen axis: testosterone via androgen receptor modulates pancreatic stellate-cell (already mapped) activation and the desmoplastic stroma, and AR signalling intersects the KRAS (already mapped) and mTOR (already mapped) growth pathways in pancreatic cancer.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Pancreatic neuroendocrine serotonin: serotonin co-produced by serotonin-secreting pancreatic neuroendocrine cells modulates cAMP-PKA signalling; elevated 5-HIAA in KRAS (already mapped)-driven tumours reflects neuroendocrine differentiation in pancreatic cancer.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Pancreatic cancer prolactin: prolactin via JAK2/STAT3 (already mapped) activates pancreatic cancer cells and tumour-associated macrophages (already mapped), augmenting NF-κB (already mapped)-driven desmoplastic stroma and mTOR (already mapped) pro-proliferative signalling.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Pancreatic cancer oxytocin: oxytocin receptors on pancreatic cancer cells and stellate cells couple to Gαq-PKC, cross-activating KRAS (already mapped) and mTOR (already mapped) signalling to promote desmoplastic stroma remodelling and cancer cell invasion.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Pancreatic cancer vasopressin: vasopressin via V1a receptors on pancreatic cancer stroma activates Gαq-PKC signalling, promoting VEGF (already mapped)-driven tumour angiogenesis and NF-κB (already mapped)-mediated cancer-associated fibroblast (already mapped) activation.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Pancreatic cancer selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the pancreatic tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Pancreatic cancer iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade in pancreatic cancer.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Pancreatic cancer sodium: excess sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplifies the T-cytotoxic (already mapped) suppression in pancreatic cancer.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Pancreatic cancer calcium: calcium signalling in macrophages (already mapped) and mast-cells (already mapped) governs immune activation; calcium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade suppressing T-cytotoxic (already mapped) killing in pancreatic cancer.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Pancreatic cancer copper: copper enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustain tumour immunity; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) mast-cell (already mapped) skewing cascade in pancreatic cancer.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Pancreatic cancer potassium: potassium efflux gates macrophage (already mapped) NLRP3; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour inflammation and suppresses mast-cell (already mapped) and T-cytotoxic (already mapped) function in pancreatic cancer.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Pancreatic cancer chloride: chloride channels in macrophages (already mapped) and tumour cells modulate cell-volume and invasive potential; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of pancreatic cancer.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Pancreatic cancer hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and tumour cells, supports lipid signalling; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of pancreatic cancer.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Pancreatic cancer nitrogen: nitrogen in amino-acid scaffold of KRAS and NF-κB (already mapped) proteins in tumour cells sustains oncogenic signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of pancreatic cancer.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Pancreatic cancer phosphorus: phosphorus in ATP and phospholipid membranes of tumour cells and macrophages (already mapped) drives KRAS signalling; phosphorus depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of pancreatic cancer.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Pancreatic cancer sulfur: sulfur in cysteine residues of KRAS and NF-κB (already mapped) proteins in tumour cells sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of pancreatic cancer.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Pancreatic cancer PD-1: PD-1 on tumour-infiltrating T-cells (already mapped) and macrophages (already mapped) suppresses anti-tumour immunity; PD-1 checkpoint dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of pancreatic cancer.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Pancreatic cancer glp-1: GLP-1 from macrophages (already mapped) and fibroblasts (already mapped) modulates metabolic-inflammatory tumour tone; glp-1 dysfunction amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of pancreatic cancer.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Pancreatic cancer angiotensin-ii: angiotensin-II from macrophages (already mapped) and endothelial cells (already mapped) drives angiogenesis; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of pancreatic cancer.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Pancreatic cancer wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and fibroblasts (already mapped) drives invasion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of pancreatic cancer.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — PanCa rankl: RANKL from macrophages (already mapped) and fibroblasts (already mapped) promotes pancreatic tumour immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — PanCa fibronectin: fibronectin in macrophages (already mapped) and fibroblasts (already mapped) promotes pancreatic ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — PanCa igf-1: IGF-1 from macrophages (already mapped) and fibroblasts (already mapped) promotes pancreatic tumour cell survival; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — PanCa cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates pancreatic cancer neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — PanCa calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates pancreatic cancer calcium balance; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — PanCa substance-p: substance-P from macrophages (already mapped) and fibroblasts (already mapped) modulates pancreatic cancer immune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of pancreatic cancer.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^conroy-2011-folfirinox]: Conroy T, Desseigne F, Ychou M, et al. FOLFIRINOX versus gemcitabine for metastatic pancreatic cancer. *N Engl J Med.* 2011;364(19):1817-1825. [doi:10.1056/NEJMoa1011923](https://doi.org/10.1056/NEJMoa1011923) · [PubMed 21561347](https://pubmed.ncbi.nlm.nih.gov/21561347/)
[^golan-2019-polo]: Golan T, Hammel P, Reni M, et al. Maintenance olaparib for germline BRCA-mutated metastatic pancreatic cancer. *N Engl J Med.* 2019;381(4):317-327. [doi:10.1056/NEJMoa1903387](https://doi.org/10.1056/NEJMoa1903387) · [PubMed 31157963](https://pubmed.ncbi.nlm.nih.gov/31157963/)
[^von-hoff-2013-abraxane]: Von Hoff DD, Ervin T, Arena FP, et al. Increased survival in pancreatic cancer with nab-paclitaxel plus gemcitabine. *N Engl J Med.* 2013;369(18):1691-1703. [doi:10.1056/NEJMoa1304369](https://doi.org/10.1056/NEJMoa1304369) · [PubMed 24131140](https://pubmed.ncbi.nlm.nih.gov/24131140/)
