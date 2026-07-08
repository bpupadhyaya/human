---
schema: human-scale-entry/v1
id: hereditary-pancreatitis
name: Hereditary Pancreatitis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary pancreatitis is caused by autosomal dominant PRSS1 gain-of-function mutations (R122H, N29I); recurrent acute pancreatitis from childhood; chronic pancreatitis with exocrine and endocrine insufficiency; ~40-fold elevated PDAC risk; analgesic-focused management."
aliases: ["hereditary pancreatitis", "hereditary chronic pancreatitis", "PRSS1 pancreatitis", "familial pancreatitis", "trypsinogen R122H pancreatitis", "hereditary pancreatitis PRSS1", "HP pancreatitis", "chronic hereditary pancreatitis", "pancreatitis hereditary syndrome"]
sources:
  - id: whitcomb-1996-prss1
    type: peer-reviewed
    cite: "Whitcomb DC, Gorry MC, Preston RA, et al. Hereditary pancreatitis is caused by a mutation in the cationic trypsinogen gene. Nat Genet. 1996;14(2):141-145."
    doi: "10.1038/ng1096-141"
    pmid: "8841182"
    url: "https://doi.org/10.1038/ng1096-141"
  - id: lowenfels-2001-hp-pdac
    type: peer-reviewed
    cite: "Lowenfels AB, Maisonneuve P, DiMagno EP, et al. Hereditary pancreatitis and the risk of pancreatic cancer. J Natl Cancer Inst. 2001;93(1):26-31."
    doi: "10.1093/jnci/93.1.26"
    pmid: "11136838"
    url: "https://doi.org/10.1093/jnci/93.1.26"
cross_links:
  - target: 01-human/03-molecular/prss1
    relation: connects-to
    note: "PRSS1 R122H and N29I gain-of-function mutations cause hereditary pancreatitis by preventing trypsin inactivation; autosomal dominant; onset childhood/early adulthood; recurrent acute → chronic pancreatitis → exocrine + endocrine insufficiency; ~40-fold elevated PDAC risk."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "PRSS1-hereditary pancreatitis confers ~40-fold PDAC risk; chronic pancreatic inflammation → acinar-ductal metaplasia → PanIN lesions → PDAC (same progression as sporadic); KRAS mutations are the initiating event in PDAC even in PRSS1-hereditary pancreatitis background."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic pancreatitis (hereditary PRSS1 or sporadic) → TGF-β release from acinar cells and inflammatory macrophages → pancreatic stellate cell activation → collagen deposition → fibrosis → acinar cell loss → exocrine insufficiency → endocrine β-cell loss → CFRD-like diabetes."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS oncogenic mutations (G12D/V/R) drive PanIN and PDAC even in hereditary pancreatitis (PRSS1 mutation background); KRAS mutation is the initiating event; chronic trypsin-mediated inflammation → KRAS-susceptible acinar cells → transformation; KRAS is the primary PDAC oncogene."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Recurrent trypsin-driven autodigestion progressively destroys the pancreas → fibrosis, exocrine insufficiency (steatorrhea, PERT) and Type 3c diabetes; total pancreatectomy with islet autotransplantation (TPIAT) relieves refractory pain and eliminates the ~40-fold PDAC risk."
  - target: 01-human/03-molecular/cftr
    relation: connects-to
    note: "CFTR-driven ductal bicarbonate secretion raises luminal pH and flushes zymogens — one of the pancreas's defenses against premature trypsin activation; CFTR variants act as modifiers that co-contribute to hereditary pancreatitis alongside PRSS1 and SPINK1 mutations."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Progressive fibrotic loss of islet β-cells causes pancreatogenic (Type 3c) diabetes — brittle, with concurrent glucagon deficiency raising hypoglycemia risk; managed with carefully titrated low-dose insulin rather than sulfonylureas, distinguishing it from Type 1 and Type 2."
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "Hereditary pancreatitis and cystic fibrosis are the two major genetic pancreatic diseases: CFTR's ductal bicarbonate flush normally clears zymogens and blocks premature trypsin activation, so CFTR variants modify hereditary pancreatitis while CF destroys the exocrine pancreas."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibrosis is the endpoint of hereditary pancreatitis, and the pancreatic stellate cell is its fibroblast: recurrent trypsin injury and TGF-β turn these cells into collagen-secreting myofibroblasts that scar the gland — the same switch driving pancreatic-cancer desmoplasia."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Hereditary and alcoholic chronic pancreatitis share one fibrotic endpoint: a PRSS1 mutation resisting trypsin inactivation and chronic alcohol both trigger repeated acinar autodigestion, stellate-cell fibrosis, and exocrine/endocrine failure; smoking raises cancer risk."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Hereditary pancreatitis commonly ends in pancreatogenic (type 3c) diabetes: recurrent inflammation destroys the islets along with the exocrine pancreas, producing an insulin-deficient diabetes that is brittle (glucagon is also lost) and distinct from type 1 and type 2."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Hereditary pancreatitis cripples the digestive system: loss of exocrine acinar tissue causes pancreatic enzyme insufficiency with steatorrhea, malabsorption and weight loss needing lifelong enzyme replacement—while the destroyed gland also forfeits its insulin/glucagon function."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Hereditary pancreatitis impairs small-intestinal digestion: without pancreatic lipase, protease and amylase reaching the duodenum, fats, proteins and fat-soluble vitamins go unabsorbed, causing steatorrhea and deficiency—so enzyme replacement is timed to meals to restore uptake."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium sits at the heart of hereditary pancreatitis: PRSS1 mutations cause premature, calcium-dependent trypsinogen activation in acinar cells, and chronic inflammation leaves the duct studded with calcium-carbonate stones—the hallmark of calcific pancreatitis."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Hereditary pancreatitis is a model of sterile inflammation via the NLRP3 inflammasome: trypsin-induced acinar injury releases damage signals that activate NLRP3 in macrophages, driving IL-1β and attacks that scar the gland—an enzyme defect igniting innate immunity."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Hereditary pancreatitis can cause pancreatogenic (type 3c) diabetes resembling type 1: repeated inflammation destroys acinar tissue and the insulin-producing islets, so endocrine failure follows exocrine—but the loss is from fibrosis, not autoimmunity."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive the chronic inflammation of hereditary pancreatitis: recurrent trypsin-triggered acinar injury recruits macrophages that, with stellate cells, lay down fibrosis—so repeated attacks progressively scar the gland toward exocrine and endocrine failure."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Hereditary pancreatitis can obstruct the neighboring liver's drainage: an inflamed, fibrotic pancreatic head compresses the common bile duct, causing jaundice and cholestasis—a benign cause of biliary obstruction that can mimic pancreatic cancer."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "Hereditary pancreatitis causes brittle type 3c diabetes: progressive destruction wipes out not just insulin-secreting beta cells but glucagon-secreting alpha cells, so patients lose counter-regulation and suffer dangerous hypoglycemia—unlike type 1 or 2 diabetes."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Hereditary pancreatitis scars the pancreas into chronic fibrosis: repeated trypsin-driven autodigestion from PRSS1 mutation triggers recurring inflammation that replaces glandular tissue with fibrosis, destroying both digestive and hormone function over years."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Acute attacks of hereditary pancreatitis are neutrophil-driven: prematurely activated trypsin injures acinar cells, recruiting neutrophils that amplify the inflammation (via the NLRP3 inflammasome) into the recurrent painful flares that define the disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Hereditary pancreatitis is dominated by chronic, disabling pain: recurrent inflammation sensitizes pancreatic and central nerves, so neuropathic-type pain persists between attacks and becomes the hardest feature to treat—driving opioid use and reduced quality of life."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Hereditary pancreatitis causes fat-soluble vitamin deficiency: years of exocrine damage block fat digestion, so vitamins A, D, E, and K fall—low vitamin D and the bone disease it brings make enzyme replacement and supplementation essential."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Chronic pancreatitis depletes magnesium and other minerals: fat malabsorption and poor intake lower magnesium, calcium, and zinc, so electrolyte deficiencies accompany the malnutrition of long-standing hereditary pancreatitis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hereditary pancreatitis eventually wrecks the endocrine pancreas: progressive scarring destroys islet cells, causing type 3c (pancreatogenic) diabetes that is brittle—lacking both insulin and glucagon—so it differs from ordinary diabetes in management."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Hereditary pancreatitis may stem from failed autophagy: acinar cells normally use autophagy to safely clear prematurely activated trypsin, so when that cleanup falters the enzyme digests the pancreas from within, triggering recurrent attacks."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Smoking turns hereditary pancreatitis toward cancer: tobacco's carbon-based carcinogens dramatically multiply the already high pancreatic cancer risk of PRSS1 carriers, so quitting is the single most important step a patient can take."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Chronic hereditary pancreatitis drains zinc: the failing pancreas can't release enough digestive enzymes, so fat and minerals including zinc go unabsorbed, leaving deficiencies that impair immunity and wound healing on top of the diabetes and pain."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Hereditary pancreatitis smolders through NF-kB: premature trypsin activation injures acinar cells and switches on NF-kB, sustaining the chronic inflammation that scars the gland and, over decades, raises pancreatic cancer risk."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 carries hereditary pancreatitis toward cancer: the repeated inflammation pours out IL-6, which via STAT3 drives fibrosis and pushes injured pancreatic cells toward malignant change, linking the inherited inflammation to tumor risk."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells patrol the cancer-prone pancreas in hereditary pancreatitis: as antigen-presenters they shape immune surveillance of the chronically inflamed gland, a focus of efforts to catch or prevent the cancer it predisposes to."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Chronic hereditary pancreatitis can clot the splenic vein: inflammation beside the pancreas thromboses the vein, backing blood into gastric varices and enlarging the spleen, a bleeding risk of long-standing disease."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Pancreatitis digests the body's fat cells: leaked enzymes break down adipocytes around the pancreas, and the freed fatty acids bind calcium into chalky deposits (saponification), a hallmark of severe attacks."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Severe pancreatitis reaches the lungs: inflammatory mediators and enzymes spilling into the blood cause pleural effusions and can trigger ARDS, the respiratory failure that drives early deaths in acute attacks."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Hereditary pancreatitis is mapped by imaging: CT and MRCP photons reveal the ductal stones, calcifications and atrophy of chronic disease, and screen the pancreas for the cancer it predisposes to."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Severe pancreatitis injures the kidneys: hypovolemia and inflammatory mediators cause acute kidney injury, a marker of severity that worsens the prognosis of an attack."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Chronic pancreatitis starves the gut lining of enzymes: without pancreatic lipase the intestinal epithelium can't absorb fat, causing the greasy steatorrhea and malnutrition of exocrine failure."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Hereditary pancreatitis is the gland digesting itself: the PRSS1 mutation lets trypsin activate prematurely inside the acinar cells, and electron microscopy shows the autodigested tissue replaced over time by fibrosis and calcified plugs."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Pancreatic inflammation can clot the splenic vein behind the stomach: the resulting back-pressure swells gastric varices that can bleed massively, a dangerous vascular complication of chronic pancreatitis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Losing fat absorption thins the bones: chronic pancreatitis blocks uptake of vitamin D and calcium, so osteoporosis and fractures of the marrow-bearing skeleton are a common, under-recognized toll."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Relentless pain defines the disease: inflammation and fibrosis sensitize the pancreatic sensory neurons and the celiac plexus into a severe, chronic visceral pain that dominates life and drives nerve blocks and opioid use."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The damaged gland stops digesting fat: exocrine insufficiency lets undigested fat reach the bowel, causing the bulky, greasy, foul steatorrhea and malabsorption that pancreatic enzyme replacement aims to fix."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Malabsorption quietly drains the blood: poor uptake of iron, B12, and folate from the failing exocrine pancreas can leave patients anemic, the red cells falling along with their other nutrients."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Chronic pancreatitis weakens the skeleton: years of fat malabsorption starve the body of vitamin D and calcium, so metabolic bone disease and osteoporosis are common and underdiagnosed, warranting bone-density screening and supplementation."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "The road to pancreatic cancer runs through p53: decades of inflammation in PRSS1 disease layer TP53 loss on top of the early KRAS mutation, the stepwise hits that give hereditary pancreatitis its steeply elevated lifetime cancer risk."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Inflammation by the pancreas clots the splenic vein: chronic pancreatitis can thrombose the adjacent splenic vein, producing gastric varices and a hypersplenism that drops the platelet count, a recognized vascular complication of the disease."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF drives the self-digesting gland: prematurely activated trypsin and dying acinar cells unleash TNF-α and other cytokines that recruit the inflammation, turning each attack of hereditary pancreatitis into tissue destruction."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Pancreatic inflammation reaches the deep veins: beyond the splenic vein, severe flares cause portal and mesenteric vein thrombosis and a systemic prothrombotic state, adding venous thromboembolism to the disease's vascular toll."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "A severe attack can flood the lungs: the systemic inflammation of acute-on-chronic pancreatitis can trigger acute respiratory distress syndrome, the leading early cause of death in a severe flare."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain is the defining burden: chronic pancreatitis sensitizes pancreatic and central nerves into a relentless neuropathic abdominal pain, often persisting even after the gland burns out — the symptom that dominates these patients' lives."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Decades of pain breed dependence: the severe, lifelong pain of hereditary pancreatitis often leads to chronic opioid therapy and the real risk of opioid use disorder, a hard management dilemma in a young-onset disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells wire pain into the inflamed gland: they accumulate around pancreatic nerves and, with activated stellate cells, drive the neuroinflammation and fibrosis that generate chronic pancreatitis pain."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Chronic inflammation steers the pancreas toward cancer through STAT3: persistent IL-6 in the repeatedly inflamed gland activates STAT3, a driver of the acinar-to-ductal change behind hereditary pancreatitis's high pancreatic-cancer risk."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A severe flare can rot and infect the gland: acute-on-chronic attacks of hereditary pancreatitis can produce infected pancreatic necrosis, a leading cause of the disease's mortality through sepsis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Relentless pain wears down the mind: the lifelong, often young-onset pain of hereditary pancreatitis, with its disability and opioid burden, drives high rates of depression that worsen the pain experience."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic inflammation and malabsorption lower the count: the persistent pancreatic inflammation of hereditary pancreatitis raises hepcidin while exocrine insufficiency impairs nutrient uptake, producing an anemia of chronic disease."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Severe attacks can injure the kidney: acute-on-chronic flares of hereditary pancreatitis cause hypovolemia and systemic inflammation that precipitate acute kidney injury, which over repeated episodes can leave chronic kidney impairment."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Chronic ductal inflammation can turn the bile ducts malignant: long-standing hereditary pancreatitis inflames the pancreaticobiliary region and, beyond pancreatic cancer, is associated with an elevated risk of cholangiocarcinoma."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Exocrine failure starves the body of iron: the fat and nutrient malabsorption of chronic pancreatic insufficiency in hereditary pancreatitis impairs iron uptake, contributing to anemia."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Malnutrition and surgery hinder repair: the protein-energy and fat-soluble-vitamin malabsorption of hereditary pancreatitis, plus its repeated pancreatic operations, leave wounds slow to heal."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Unrelenting pain and cancer risk breed worry: the recurrent severe abdominal pain, opioid dependence and lifelong pancreatic-cancer surveillance of hereditary pancreatitis foster chronic anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Severe attacks flood the lungs: an acute pancreatitis flare in hereditary pancreatitis can cause pleural effusions and acute respiratory distress syndrome from the systemic inflammatory response."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Leaked pancreatic enzymes mark the skin: severe pancreatitis causes the bruising of Cullen's and Grey-Turner's signs, and circulating lipase can produce a nodular pancreatic panniculitis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Enzyme release can inflame fat and joints: hereditary pancreatitis can cause the pancreatitis-panniculitis-polyarthritis syndrome, and chronic malabsorption of vitamin D weakens bone."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe attacks injure the kidney: acute pancreatitis causes third-spacing, hypovolaemia and shock that lead to acute kidney injury and tubular necrosis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "A severe attack collapses the circulation: acute pancreatitis triggers a systemic inflammatory response with capillary leak and distributive shock requiring aggressive fluid resuscitation."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Duct disruption leaks lymph and clots veins: pancreatic duct rupture can cause pancreatic and chylous ascites, and peripancreatic inflammation can thrombose the splenic vein."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It must be told apart from autoimmune disease: recurrent hereditary pancreatitis can mimic autoimmune (IgG4-related) pancreatitis, and repeated attacks drive chronic inflammatory injury to the gland."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It shapes family planning: as an autosomal-dominant PRSS1 disorder, hereditary pancreatitis raises genetic-counselling and prenatal questions for affected families."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "Pain control is a mainstay: NSAIDs like ibuprofen and stronger analgesics manage the recurrent abdominal pain of hereditary pancreatitis, though chronic use carries gastrointestinal and renal risk."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "Gut bacteria infect the dead tissue: in severe acute attacks, bacteria such as Escherichia coli translocate from the bowel to infect pancreatic necrosis, a life-threatening complication needing antibiotics and drainage."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Its great late danger is pancreatic cancer: hereditary pancreatitis carries a markedly raised lifetime risk of pancreatic adenocarcinoma, which is treated with chemotherapy when it arises."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "Fibrosis destroys the islets: repeated inflammation scars the pancreas and obliterates the islets of Langerhans, producing the pancreatogenic (type 3c) diabetes that complicates hereditary pancreatitis."
  - target: 01-human/07-system/hereditary-angioedema
    relation: connects-to
    note: "Diseases of an unchecked protease cascade: hereditary pancreatitis unleashes trypsin when its inhibitor SPINK1 fails, much as hereditary angioedema unleashes the kallikrein–bradykinin cascade when C1-inhibitor fails—each a missing brake on a destructive enzyme."
  - target: 03-medicine/03-food/curcumin
    relation: connects-to
    note: "Antioxidants aimed at the pain: oxidative stress drives the inflammation and pain of chronic pancreatitis, and antioxidant compounds such as curcumin have been studied as adjuncts to reduce flares and pain in hereditary pancreatitis."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "When pancreatitis reaches the lungs: a severe attack floods the blood with proteases and cytokines that injure the alveolar–capillary membrane, causing the acute respiratory distress syndrome that makes severe hereditary pancreatitis life-threatening."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Biliary obstruction and the liver: chronic pancreatitis with head fibrosis compresses the bile duct, causing cholestasis that backs up into the hepatic lobule, while shared alcohol injures both organs."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "The relentless pain: pancreatic inflammation sensitises and remodels visceral and peripheral nerves, producing the severe neuropathic pain that dominates chronic pancreatitis and drives opioid use."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Pancreatic osteodystrophy: fat malabsorption and vitamin-D and calcium deficiency in chronic pancreatitis thin cortical bone, causing the osteoporosis and fractures common in these patients."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "SIRS of severe pancreatitis: a severe acute attack unleashes a systemic inflammatory response with ARDS and shock, the trypsin-triggered cytokine surge mechanistically overlapping a cytokine storm."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Vascular complications: chronic pancreatitis erodes nearby vessels, causing splenic-artery pseudoaneurysms of the arterial wall and splenic or portal vein thrombosis—dangerous bleeding and clotting."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infection-triggered pancreatitis: COVID-19 is a recognised cause of acute pancreatitis through ACE2 on acinar and islet cells, which can be severe on a background hereditary predisposition."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcium-triggered injury: sustained intra-acinar calcium activates calcineurin, driving the premature trypsinogen activation that initiates pancreatitis—a pathway protective when blocked experimentally."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Metaplasia toward cancer: repeated injury drives acinar-to-ductal metaplasia through EGFR signalling, which with KRAS sets chronic hereditary pancreatitis on the path to pancreatic cancer."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Microcirculatory failure: endothelin-1-driven vasoconstriction worsens pancreatic ischaemia in severe pancreatitis, converting interstitial inflammation toward necrotising disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome injury: premature trypsin activation triggers NLRP3-driven IL-1β release in hereditary pancreatitis, amplifying the acinar inflammation of each recurrent attack."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes and macrophages into the injured pancreas, sustaining the chronic inflammation that progresses to fibrosis in hereditary pancreatitis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Ischaemic fibrosis: HIF-1α stabilised in the poorly perfused, fibrotic pancreas of chronic hereditary pancreatitis drives the stellate-cell activation that scars the gland."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Stellate-cell mitogen: PDGF is the dominant proliferative signal expanding pancreatic stellate cells into collagen-secreting myofibroblasts, the engine of the progressive fibrosis of chronic hereditary pancreatitis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Acute-attack alarmin: S100A8/A9 from the neutrophils flooding the inflamed gland amplifies each acute pancreatitis flare in hereditary pancreatitis and tracks the severity of the attack."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Cancer-risk progression: TERT reactivation immortalises cells along the path to pancreatic ductal adenocarcinoma, the markedly elevated cancer risk that follows decades of hereditary pancreatitis."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis-necrosis balance: whether injured acinar cells die by caspase-3-mediated apoptosis or by necrosis determines the severity of each attack — apoptosis is protective, while necrosis drives the severe, systemic pancreatitis."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "DAMP systemic inflammation: DAMPs released by necrotic acinar cells engage TLR4 on innate immune cells, driving the systemic inflammatory response syndrome that makes severe acute attacks of hereditary pancreatitis life-threatening."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kallikrein-kinin activation: prematurely activated trypsin also activates the kallikrein-kinin system, generating bradykinin that drives the pain, vascular leak and hypotension of a severe pancreatitis attack."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Acinar calcium overload: a sustained rise in acinar-cell cytosolic calcium is the trigger that prematurely activates trypsin and causes acinar necrosis, the central initiating event of pancreatitis; chronic disease then deposits the ductal calcium of pancreatic calcification."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Pancreatic fibrosis: recurrent attacks in hereditary pancreatitis activate pancreatic stellate cells to lay down collagen, the progressive fibrosis that destroys the gland and produces the exocrine insufficiency and diabetes of chronic pancreatitis."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative acinar injury: xanthine-oxidase-derived reactive oxygen species generated during an attack amplify acinar-cell injury and inflammation, the oxidative stress that worsens the necrosis of severe pancreatitis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Metaplasia to cancer: repeated injury and oncogenic KRAS (mapped) drive MAPK-ERK signalling that pushes acinar cells toward acinar-to-ductal metaplasia, the step that raises pancreatic-cancer risk in hereditary pancreatitis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate relay: TLR4 (mapped) signals through MyD88 to activate NF-κB (mapped) in response to acinar-cell injury, relaying the danger signal into the cytokine cascade of a pancreatitis attack."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Fibrosis and progression: TGF-β/SMAD4 signalling (TGF-β mapped) drives the pancreatic stellate-cell fibrosis of chronic pancreatitis, and SMAD4 loss marks progression to pancreatic ductal adenocarcinoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory reprogramming: IL-6 signalling through JAK-STAT3 (IL-6 and STAT3 already mapped) sustains the chronic inflammation and acinar-to-ductal reprogramming of hereditary pancreatitis."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative acinar injury: NRF2 antioxidant defence counters the oxidative stress of recurrent acinar injury (xanthine-oxidase already mapped) in hereditary pancreatitis."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cancer progression: CDKN2A loss is a key step in the markedly elevated progression of hereditary pancreatitis to pancreatic ductal adenocarcinoma, alongside the KRAS and TP53 lesions already mapped."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling modulates acinar-cell survival and the inflammatory response in the recurrent acute episodes of hereditary pancreatitis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR regulation of autophagy/zymophagy (autophagy mapped) governs the clearance of prematurely activated zymogens, a protective process overwhelmed in hereditary pancreatitis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 secreted in the injured pancreas activates stellate cells and amplifies the fibrosis of chronic hereditary pancreatitis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA released by repeated acinar-cell injury engages cGAS-STING, amplifying the sterile inflammation of recurrent hereditary pancreatitis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune response within the chronically inflamed pancreas of hereditary pancreatitis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) in stressed acinar cells contributes to the survival and the malignant-transformation risk of hereditary pancreatitis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the acinar-cell oxidative-stress and autophagy responses to the recurrent trypsinogen-activation injury of hereditary pancreatitis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the NF-κB-driven inflammatory signaling of the recurrent acinar injury of hereditary pancreatitis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) shapes the cancer risk arising from the chronic inflammation of hereditary pancreatitis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is relevant to the immune injury and cancer risk of the chronically inflamed pancreas of hereditary pancreatitis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the acinar-cell metabolic stress of hereditary pancreatitis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling contributes to the acinar-cell injury and fibrotic responses of hereditary pancreatitis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the inflammation of recurrent hereditary pancreatitis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic changes accompanying the chronic inflammation and cancer risk of hereditary pancreatitis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation implicated in the progression of hereditary pancreatitis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the pancreatic-stellate-cell activation and leukocyte trafficking of hereditary pancreatitis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the pancreatic inflammation and fibrosis of hereditary pancreatitis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the chronic inflammation and fibrogenesis of hereditary pancreatitis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory milieu of the recurrent pancreatic inflammation of hereditary pancreatitis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunomodulation of the pancreatic inflammation of hereditary pancreatitis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the pancreatic stellate-cell activation and fibrosis of hereditary pancreatitis."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Chronic pain: recurrent and then constant abdominal pain from childhood is the dominant clinical burden of hereditary pancreatitis, and its management with opioids acting at the mu-opioid receptor risks dependence, a major therapeutic dilemma."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic pancreatic pain: chronic pancreatitis sensitises and remodels pancreatic sensory nerves, with substance P and neurogenic inflammation amplifying the visceral pain that persists even as the gland burns out."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune inflammation: MHC class II-restricted T-cell responses participate in the immune component of chronic pancreatitis and its overlap with autoimmune pancreatitis, alongside the innate inflammasome signalling (NLRP3 already mapped)."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Malnutrition anaemia: exocrine insufficiency in hereditary pancreatitis causes fat and micronutrient malabsorption, and chronic disease with iron and vitamin deficiency lowers haemoglobin, the anaemia adding to the debility of the burnt-out gland."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Pancreatogenic diabetes: progressive islet loss produces the type-3c diabetes of hereditary pancreatitis (insulin and glucagon already mapped), and the incretin GLP-1 axis is disturbed as the enteroinsular signalling of the damaged gland fails."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory mediators: prostaglandins amplify the pancreatic inflammation and pain of hereditary pancreatitis, and NSAIDs that block their synthesis are used, notably rectal indomethacin to prevent post-ERCP pancreatitis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory counterweight: the anti-inflammatory IL-10 opposes the pro-inflammatory cytokines (TNF, IL-6 and IL-1 already mapped) driving the recurrent pancreatic inflammation, part of the immune balance shaping progression to chronic pancreatitis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Fat malabsorption: the exocrine insufficiency of chronic hereditary pancreatitis causes fat malabsorption, disturbing cholesterol and essential-fatty-acid handling and the absorption of fat-soluble vitamins, part of its nutritional burden."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant therapy: the oxidative stress (NRF2 and xanthine oxidase already mapped) of chronic pancreatitis has prompted antioxidant regimens including selenium to reduce pain and inflammation, a studied adjunct in hereditary pancreatitis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Pro-fibrotic type-2: IL-4 drives the M2 macrophage and pro-fibrotic (TGF-β already mapped) programme that lays down the collagen (already mapped) fibrosis of chronic hereditary pancreatitis (IL-10 already mapped)."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 fibrosis: IL-13, with IL-4 (already mapped), is a potent pro-fibrotic cytokine driving the pancreatic stellate-cell (fibroblast already mapped) fibrosis of chronic hereditary pancreatitis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Malabsorption anaemia: the exocrine insufficiency and the chronic inflammation of hereditary pancreatitis impair nutrient absorption and cause an anaemia (haemoglobin already mapped) with disturbed iron handling."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and, with the malabsorption, produces the anaemia (haemoglobin already mapped) of chronic hereditary pancreatitis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Malnutrition adipokine: leptin reflects the malnutrition and the pancreatogenic-diabetes (insulin already mapped) metabolic disturbance of the exocrine and endocrine insufficiency of hereditary pancreatitis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of the pancreatic insufficiency of hereditary pancreatitis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) and metabolic disturbance of hereditary pancreatitis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the high pancreatic-cancer risk of the chronic inflammation of hereditary pancreatitis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate pancreatitis interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the acinar cell-death DNA, is part of the innate-immune signalling of the recurrent inflammation of hereditary pancreatitis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the chronic inflammation (IL-6 and TNF already mapped) driving the fibrosis and the pancreatic-cancer risk of hereditary pancreatitis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of hereditary pancreatitis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune response of hereditary pancreatitis."
---

# Hereditary Pancreatitis

## Overview

**Hereditary pancreatitis (HP)** is a rare autosomal dominant condition caused primarily by germline gain-of-function mutations in **PRSS1** (cationic trypsinogen), most commonly **R122H** (~65-70% of HP families) and **N29I** (~20-25%), which prevent the normal autolytic self-inactivation of intrapancreatic trypsin. The result is recurrent episodes of acute pancreatitis beginning in childhood or early adulthood, progressive destruction of pancreatic parenchyma → chronic pancreatitis → exocrine pancreatic insufficiency (malabsorption, steatorrhea) and endocrine pancreatic insufficiency (pancreatogenic diabetes mellitus, Type 3c). The most feared complication is a **~40-fold increased lifetime risk of pancreatic ductal adenocarcinoma (PDAC)**, with cumulative PDAC risk estimated at ~40% by age 70 in Lowenfels et al.'s International HP Study Group cohort. HP was the first pancreatitis syndrome for which a molecular genetic cause was identified, by Whitcomb et al. in 1996. Prevalence is estimated at ~1-3 per 100,000; HP accounts for ~1% of all chronic pancreatitis cases in the Western world [^whitcomb-1996-prss1] [^lowenfels-2001-hp-pdac].

**Genetic causes of hereditary/familial pancreatitis:**

| Gene | Role | Inheritance | HP contribution |
|---|---|---|---|
| PRSS1 (R122H) | Cationic trypsinogen GOF — no autolysis | Autosomal dominant | ~65-70% of HP families |
| PRSS1 (N29I) | Cationic trypsinogen GOF — Ca²⁺ destabilization | Autosomal dominant | ~20-25% of HP families |
| SPINK1 (N34S) | Trypsin inhibitor LOF — modifier | Complex/recessive modifier | Co-contributor; ~1-2% population |
| CTRC (R254W, etc.) | Chymotrypsin C LOF — impaired trypsin clearance | Autosomal recessive modifier | Rare; amplifies other mutations |
| CFTR variants | Ductal fluid/pH dysfunction | Complex modifier | Co-contributor with PRSS1/SPINK1 |

## Structure

### Genetic basis of hereditary pancreatitis

**PRSS1 R122H (Arg122His) — dominant mechanism:**
- Arg122 is the autolysis site: wild-type trypsin cleaves the Arg122-Val123 bond → trypsin fragments → self-inactivation; this prevents persistent trypsin activity in the pancreas
- R122H: Arg→His substitution; trypsin cannot cleave His; autolysis abolished → once activated inside acinar cell, trypsin cannot self-destruct → chain activation of other zymogens → acinar cell autodigestion
- Penetrance of R122H: ~80% lifetime penetrance (vs 100% for most autosomal dominant conditions); modifiers (SPINK1, CFTR, alcohol, smoking, diet) influence phenotypic expression
- Anticipation: some families show earlier onset and more severe disease in successive generations (proposed mechanism: epigenetic modifier accumulation; not fully established)

**PRSS1 N29I (Asn29Ile) — Ca²⁺ destabilization:**
- Asn29 is part of the calcium-binding loop of trypsinogen; Ca²⁺ binding stabilizes trypsinogen in the inactive conformation
- N29I: disrupts Ca²⁺ coordination → lower calcium affinity → trypsinogen less stable → lower threshold for activation (spontaneous premature activation inside acinar cells at normal physiological calcium concentrations)
- Penetrance: somewhat lower than R122H (~65-70%); phenotype is clinically similar but can be milder
- Also associated with higher risk of exocrine insufficiency and diabetes compared to R122H in some cohort studies

**SPINK1 N34S — modifier allele:**
- SPINK1 encodes pancreatic secretory trypsin inhibitor (PSTI); inhibits ~20% of trypsin activity; a first-line buffer against premature trypsin activation
- N34S: found in ~1-2% of the European population; reduces SPINK1 mRNA stability → reduced inhibitor levels; alone not sufficient to cause pancreatitis (~5-10% lifetime risk with N34S alone, requiring additional environmental or genetic co-hits)
- In PRSS1-HP patients: SPINK1 N34S co-inheritance worsens phenotype (earlier onset, more severe chronic pancreatitis, higher PDAC risk)

### Pancreatic physiology and HP pathophysiology

**Normal protection against intrapancreatic trypsin activation:**
1. TAP peptide: blocks active site until enterokinase cleaves in duodenum
2. SPINK1: inhibits nascent premature trypsin in acinar cell and duct
3. CTRC: chymotrypsin C cleaves trypsinogen/trypsin at Leu81 and Arg122 → inactivation
4. Autolysis (Arg122): trypsin destroys itself
5. Alkaline pH: bicarbonate in pancreatic duct (CFTR-mediated) → high pH → trypsin less active

**HP pathophysiology:**
1. PRSS1 GOF → premature/persistent trypsin inside acinar cells
2. Trypsin activates: chymotrypsinogen → chymotrypsin, proelastase → elastase, phospholipase A2, procarboxypeptidase → all digestive enzymes activated inside the cell
3. Acinar cell autodigestion → necrosis → acute pancreatitis episode
4. Repeated acute episodes → persistent inflammation → macrophage infiltration → TGF-β release → pancreatic stellate cell activation → collagen deposition → pancreatic fibrosis
5. Fibrosis → loss of acinar cell mass → exocrine insufficiency; loss of islet β-cells → Type 3c diabetes
6. Chronic inflammation + oxidative stress → genomic instability in ductal epithelium → KRAS mutation acquisition → PanIN lesion formation → PDAC

## Function

### Clinical manifestations

**Recurrent acute pancreatitis (childhood to early adulthood):**
- First episode: typically age 5-15 years; earlier onset than sporadic acute pancreatitis
- Presentation: severe epigastric pain radiating to back, nausea, vomiting; elevated serum amylase and lipase (>3× upper limit of normal); CT: peripancreatic fat stranding, edema, ± necrosis
- Triggers: alcohol, high-fat meals, stress, viral illness — same as sporadic acute pancreatitis but at much lower exposure thresholds
- Recurrence pattern: multiple episodes per year initially; frequency may decrease as parenchyma is depleted; pain character changes from episodic (acute) to constant (chronic)

**Chronic pancreatitis:**
- Develops after ~10-20 years of recurrent acute episodes (earlier in smokers or with SPINK1 co-mutation)
- Pathology: widespread intralobular and perilobular fibrosis, acinar cell loss, ductal epithelial metaplasia, intracanalicular protein plugs, pancreatic stones (calcium carbonate intraductal concretions)
- Pain: often debilitating, constant (neuropathic component); not reliably correlated with disease activity; central sensitization develops in many patients
- Main pancreatic duct dilation: upstream of strictures or stones → obstructive chronic pancreatitis; indication for endoscopic or surgical decompression

**Exocrine pancreatic insufficiency (EPI):**
- Occurs when >90% of functional acinar mass is lost; typically after 10-20 years of disease
- Symptoms: steatorrhea (greasy, foul-smelling stools), weight loss, malabsorption of fat-soluble vitamins (A, D, E, K)
- Diagnosis: fecal elastase-1 (FE-1 <100 μg/g = severe EPI); 72-hour fecal fat collection; secretin-enhanced MRCP for direct measurement of pancreatic secretory capacity
- Treatment: pancreatic enzyme replacement therapy (PERT) — lipase, protease, amylase with all meals; fat-soluble vitamin supplementation

**Pancreatogenic diabetes mellitus (Type 3c diabetes):**
- Results from islet cell destruction by chronic inflammation and fibrosis
- Characteristics: brittle diabetes (loss of glucagon counterregulation → hypoglycemia risk); low insulin requirement initially (preserved β-cells); eventual absolute insulin deficiency
- Type 3c management: low-dose insulin titrated carefully; avoid sulfonylureas (risk of hypoglycemia); metformin for insulin resistance component if tolerated; glucagon monitoring
- Distinct from Type 1 (autoimmune) and Type 2 (insulin resistance): requires different management approach

**Pancreatic ductal adenocarcinoma (PDAC) — the critical late complication:**
- ~40-fold elevated PDAC risk vs general population; cumulative risk ~40% by age 70 in HP
- PDAC develops from pancreatic intraepithelial neoplasia (PanIN) lesions in the chronically inflamed ductal epithelium
- The oncogenic sequence: chronic inflammation → ductal metaplasia → KRAS mutation acquisition → PanIN1 → PanIN2 → PanIN3 → invasive PDAC (same as sporadic PDAC pathway)
- Risk factors that further elevate PDAC risk within HP: smoking (most important — ~2-fold additional multiplier); onset before age 20; PRSS1 R122H (vs N29I); paternal inheritance (vs maternal — possibly imprinting); SPINK1 N34S co-mutation
- Surveillance: recommended from ~40 years of age (or 20 years after first pancreatitis episode, whichever is later); annual EUS (preferred) or MRCP for early detection; serum CA19-9 (limited sensitivity in chronic pancreatitis background)
- TPIAT eliminates PDAC risk by removing the target organ

## Pathology

### Diagnosis and differential

**Diagnosis of hereditary pancreatitis:**
1. Clinical: ≥2 first- or second-degree relatives with recurrent acute pancreatitis or chronic pancreatitis without clear etiology; OR young-onset idiopathic pancreatitis (childhood/adolescence)
2. Genetic testing: PRSS1 sequencing (R122H, N29I, other coding variants); SPINK1 sequencing (N34S); CFTR sequencing (modifier); CTRC sequencing (modifier)
3. Imaging: CT/MRI pancreas (acute episodes); MRCP (chronic disease — duct morphology, stones, strictures); EUS (fine detail of duct and parenchyma; dysplasia surveillance)
4. Functional: fecal elastase (EPI), HbA1c/glucose (Type 3c diabetes), fat-soluble vitamins

**Differential diagnosis of recurrent childhood pancreatitis:**
- Idiopathic recurrent acute pancreatitis (most common; may have subclinical SPINK1 or CFTR variants)
- Pancreas divisum: congenital failure of dorsal/ventral pancreatic ductal fusion → relative obstruction; MRI/MRCP diagnosis; usually less severe
- Structural anomalies: choledochal cyst, anomalous pancreaticobiliary junction
- Hypertriglyceridemia-induced pancreatitis: serum TG >1000 mg/dL; autosomal recessive LPL/APOC2/APOA5 mutations
- Autoimmune pancreatitis (AIP): IgG4-related; responds to steroids; mass-forming; serum IgG4 elevated; PRSS1 test negative
- Trauma, medication-induced (valproic acid, azathioprine), Reye syndrome

### Management

**Acute pancreatitis episodes:**
- IV fluids (aggressive hydration, especially Lactated Ringer's — reduces SIRS vs normal saline); pain management (NSAIDs/opioids); NPO then early enteral feeding (reduces infectious complications vs TPN); antibiotics only for infected necrosis
- Severity scoring: APACHE II, Atlanta 2012 criteria; CT Severity Index for necrosis quantification
- Necrosectomy: for infected necrotizing pancreatitis; endoscopic step-up approach preferred over open necrosectomy (PANTER trial)

**Chronic pancreatitis — pain management:**
- Analgesic ladder: NSAIDs → tramadol → opioids; opioid addiction risk is very high in chronic pancreatitis patients
- Antineuropathic: pregabalin, duloxetine for neuropathic component of chronic pain
- Endoscopic therapy: ERCP with stone extraction, stricture dilation, pancreatic duct stenting → reduces duct hypertension → pain relief in ~50-70% of patients with ductal disease
- Surgical drainage procedures: lateral pancreaticojejunostomy (Puestow/Partington-Rochelle) for main pancreatic duct ≥5-7 mm; pain-free rate ~60-80% at 5 years
- Pancreatic head resection: Beger procedure (duodenum-preserving), Whipple (pancreaticoduodenectomy) for head-dominant fibrotic disease with inflammatory mass

**Total Pancreatectomy with Islet Autotransplantation (TPIAT):**
- Indication: refractory disabling pain not responsive to endoscopic/surgical drainage; diffuse disease; patient willing to accept lifelong enzyme replacement and manage insulin-requiring diabetes
- Procedure: total pancreatectomy (removes entire pancreas) → islet isolation from the resected pancreas → intraportal infusion of islets into the liver → islets engraft → ~30-40% achieve insulin independence; ~60-70% require reduced insulin vs total pancreatectomy without IAT
- Advantage in HP: eliminates lifetime PDAC risk entirely (no pancreas = no PDAC); removes source of recurrent acute pancreatitis; provides pain relief in ~80% of patients at 1 year
- Timing: best outcomes when performed before development of significant islet damage from prior pancreatitis; TPIAT registry data (University of Minnesota, Cincinnati Children's) guide timing decisions

**PDAC surveillance:**
- Start from age 40 (or 20 years after HP onset if HP began before age 20)
- Annual EUS preferred over CT (avoids radiation; better for small lesions); alternative: MRCP
- Serum CA19-9 annually (limited sensitivity in chronic pancreatitis background; useful for trend)
- Smoking cessation: critically important (smoking alone doubles PDAC risk; in HP, synergistic)
- New FNA/EUS-guided biopsy for any new solid lesion, new ductal stricture, or CA19-9 rise

**Genetic counseling:**
- Autosomal dominant; 50% offspring risk for PRSS1 mutations
- Penetrance: ~80% for R122H; ~65-70% for N29I; phenotypic variability within families
- Testing: genetic counseling before testing children; clinical benefit of early identification → lifestyle modifications (smoking avoidance, alcohol avoidance, surveillance)
- SPINK1 N34S: complex inheritance; counsel as modifier allele; alone does not predict reliable HP

## Connections

- `connects-to` → **[PRSS1](../../03-molecular/prss1/README.md)** — PRSS1 R122H and N29I gain-of-function mutations cause hereditary pancreatitis by preventing trypsin inactivation; autosomal dominant; onset childhood/early adulthood; recurrent acute → chronic pancreatitis → exocrine + endocrine insufficiency; ~40-fold elevated PDAC risk.
- `connects-to` → **[Pancreatic Cancer](../../07-system/pancreatic-cancer/README.md)** — PRSS1-hereditary pancreatitis confers ~40-fold PDAC risk; chronic pancreatic inflammation → acinar-ductal metaplasia → PanIN lesions → PDAC (same progression as sporadic); KRAS mutations are the initiating event in PDAC even in PRSS1-hereditary pancreatitis background.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Chronic pancreatitis (hereditary PRSS1 or sporadic) → TGF-β release from acinar cells and inflammatory macrophages → pancreatic stellate cell activation → collagen deposition → fibrosis → acinar cell loss → exocrine insufficiency → endocrine β-cell loss → CFRD-like diabetes.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS oncogenic mutations (G12D/V/R) drive PanIN and PDAC even in hereditary pancreatitis (PRSS1 mutation background); KRAS mutation is the initiating event; chronic trypsin-mediated inflammation → KRAS-susceptible acinar cells → transformation; KRAS is the primary PDAC oncogene.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Recurrent trypsin-driven autodigestion progressively destroys the pancreas → fibrosis, exocrine insufficiency (steatorrhea, PERT) and Type 3c diabetes; total pancreatectomy with islet autotransplantation (TPIAT) relieves refractory pain and eliminates the ~40-fold PDAC risk.
- `connects-to` → **[CFTR](../../03-molecular/cftr/README.md)** — CFTR-driven ductal bicarbonate secretion raises luminal pH and flushes zymogens — one of the pancreas's defenses against premature trypsin activation; CFTR variants act as modifiers that co-contribute to hereditary pancreatitis alongside PRSS1 and SPINK1 mutations.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Progressive fibrotic loss of islet β-cells causes pancreatogenic (Type 3c) diabetes — brittle, with concurrent glucagon deficiency raising hypoglycemia risk; managed with carefully titrated low-dose insulin rather than sulfonylureas, distinguishing it from Type 1 and Type 2.
- `connects-to` → **[Cystic Fibrosis](../cystic-fibrosis/README.md)** — Hereditary pancreatitis and cystic fibrosis are the two major genetic pancreatic diseases: CFTR's ductal bicarbonate flush normally clears zymogens and blocks premature trypsin activation, so CFTR variants modify hereditary pancreatitis while CF destroys the exocrine pancreas.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibrosis is the endpoint of hereditary pancreatitis, and the pancreatic stellate cell is its fibroblast: recurrent trypsin injury and TGF-β turn these cells into collagen-secreting myofibroblasts that scar the gland — the same switch driving pancreatic-cancer desmoplasia.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Hereditary and alcoholic chronic pancreatitis share one fibrotic endpoint: a PRSS1 mutation resisting trypsin inactivation and chronic alcohol both trigger repeated acinar autodigestion, stellate-cell fibrosis, and exocrine/endocrine failure; smoking raises cancer risk.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Hereditary pancreatitis commonly ends in pancreatogenic (type 3c) diabetes: recurrent inflammation destroys the islets along with the exocrine pancreas, producing an insulin-deficient diabetes that is brittle (glucagon is also lost) and distinct from type 1 and type 2.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Hereditary pancreatitis cripples the digestive system: loss of exocrine acinar tissue causes pancreatic enzyme insufficiency with steatorrhea, malabsorption and weight loss needing lifelong enzyme replacement—while the destroyed gland also forfeits its insulin/glucagon function.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Hereditary pancreatitis impairs small-intestinal digestion: without pancreatic lipase, protease and amylase reaching the duodenum, fats, proteins and fat-soluble vitamins go unabsorbed, causing steatorrhea and deficiency—so enzyme replacement is timed to meals to restore uptake.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium sits at the heart of hereditary pancreatitis: PRSS1 mutations cause premature, calcium-dependent trypsinogen activation in acinar cells, and chronic inflammation leaves the duct studded with calcium-carbonate stones—the hallmark of calcific pancreatitis.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Hereditary pancreatitis is a model of sterile inflammation via the NLRP3 inflammasome: trypsin-induced acinar injury releases damage signals that activate NLRP3 in macrophages, driving IL-1β and attacks that scar the gland—an enzyme defect igniting innate immunity.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Hereditary pancreatitis can cause pancreatogenic (type 3c) diabetes resembling type 1: repeated inflammation destroys acinar tissue and the insulin-producing islets, so endocrine failure follows exocrine—but the loss is from fibrosis, not autoimmunity.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive the chronic inflammation of hereditary pancreatitis: recurrent trypsin-triggered acinar injury recruits macrophages that, with stellate cells, lay down fibrosis—so repeated attacks progressively scar the gland toward exocrine and endocrine failure.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Hereditary pancreatitis can obstruct the neighboring liver's drainage: an inflamed, fibrotic pancreatic head compresses the common bile duct, causing jaundice and cholestasis—a benign cause of biliary obstruction that can mimic pancreatic cancer.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — Hereditary pancreatitis causes brittle type 3c diabetes: progressive destruction wipes out not just insulin-secreting beta cells but glucagon-secreting alpha cells, so patients lose counter-regulation and suffer dangerous hypoglycemia—unlike type 1 or 2 diabetes.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Hereditary pancreatitis scars the pancreas into chronic fibrosis: repeated trypsin-driven autodigestion from PRSS1 mutation triggers recurring inflammation that replaces glandular tissue with fibrosis, destroying both digestive and hormone function over years.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Acute attacks of hereditary pancreatitis are neutrophil-driven: prematurely activated trypsin injures acinar cells, recruiting neutrophils that amplify the inflammation (via the NLRP3 inflammasome) into the recurrent painful flares that define the disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Hereditary pancreatitis is dominated by chronic, disabling pain: recurrent inflammation sensitizes pancreatic and central nerves, so neuropathic-type pain persists between attacks and becomes the hardest feature to treat—driving opioid use and reduced quality of life.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Hereditary pancreatitis causes fat-soluble vitamin deficiency: years of exocrine damage block fat digestion, so vitamins A, D, E, and K fall—low vitamin D and the bone disease it brings make enzyme replacement and supplementation essential.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Chronic pancreatitis depletes magnesium and other minerals: fat malabsorption and poor intake lower magnesium, calcium, and zinc, so electrolyte deficiencies accompany the malnutrition of long-standing hereditary pancreatitis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hereditary pancreatitis eventually wrecks the endocrine pancreas: progressive scarring destroys islet cells, causing type 3c (pancreatogenic) diabetes that is brittle—lacking both insulin and glucagon—so it differs from ordinary diabetes in management.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Hereditary pancreatitis may stem from failed autophagy: acinar cells normally use autophagy to safely clear prematurely activated trypsin, so when that cleanup falters the enzyme digests the pancreas from within, triggering recurrent attacks.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Smoking turns hereditary pancreatitis toward cancer: tobacco's carbon-based carcinogens dramatically multiply the already high pancreatic cancer risk of PRSS1 carriers, so quitting is the single most important step a patient can take.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Chronic hereditary pancreatitis drains zinc: the failing pancreas can't release enough digestive enzymes, so fat and minerals including zinc go unabsorbed, leaving deficiencies that impair immunity and wound healing on top of the diabetes and pain.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Hereditary pancreatitis smolders through NF-kB: premature trypsin activation injures acinar cells and switches on NF-kB, sustaining the chronic inflammation that scars the gland and, over decades, raises pancreatic cancer risk.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 carries hereditary pancreatitis toward cancer: the repeated inflammation pours out IL-6, which via STAT3 drives fibrosis and pushes injured pancreatic cells toward malignant change, linking the inherited inflammation to tumor risk.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells patrol the cancer-prone pancreas in hereditary pancreatitis: as antigen-presenters they shape immune surveillance of the chronically inflamed gland, a focus of efforts to catch or prevent the cancer it predisposes to.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Chronic hereditary pancreatitis can clot the splenic vein: inflammation beside the pancreas thromboses the vein, backing blood into gastric varices and enlarging the spleen, a bleeding risk of long-standing disease.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Pancreatitis digests the body's fat cells: leaked enzymes break down adipocytes around the pancreas, and the freed fatty acids bind calcium into chalky deposits (saponification), a hallmark of severe attacks.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Severe pancreatitis reaches the lungs: inflammatory mediators and enzymes spilling into the blood cause pleural effusions and can trigger ARDS, the respiratory failure that drives early deaths in acute attacks.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Hereditary pancreatitis is mapped by imaging: CT and MRCP photons reveal the ductal stones, calcifications and atrophy of chronic disease, and screen the pancreas for the cancer it predisposes to.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Severe pancreatitis injures the kidneys: hypovolemia and inflammatory mediators cause acute kidney injury, a marker of severity that worsens the prognosis of an attack.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Chronic pancreatitis starves the gut lining of enzymes: without pancreatic lipase the intestinal epithelium can't absorb fat, causing the greasy steatorrhea and malnutrition of exocrine failure.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Hereditary pancreatitis is the gland digesting itself: the PRSS1 mutation lets trypsin activate prematurely inside the acinar cells, and electron microscopy shows the autodigested tissue replaced over time by fibrosis and calcified plugs.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Pancreatic inflammation can clot the splenic vein behind the stomach: the resulting back-pressure swells gastric varices that can bleed massively, a dangerous vascular complication of chronic pancreatitis.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Losing fat absorption thins the bones: chronic pancreatitis blocks uptake of vitamin D and calcium, so osteoporosis and fractures of the marrow-bearing skeleton are a common, under-recognized toll.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Relentless pain defines the disease: inflammation and fibrosis sensitize the pancreatic sensory neurons and the celiac plexus into a severe, chronic visceral pain that dominates life and drives nerve blocks and opioid use.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The damaged gland stops digesting fat: exocrine insufficiency lets undigested fat reach the bowel, causing the bulky, greasy, foul steatorrhea and malabsorption that pancreatic enzyme replacement aims to fix.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Malabsorption quietly drains the blood: poor uptake of iron, B12, and folate from the failing exocrine pancreas can leave patients anemic, the red cells falling along with their other nutrients.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Chronic pancreatitis weakens the skeleton: years of fat malabsorption starve the body of vitamin D and calcium, so metabolic bone disease and osteoporosis are common and underdiagnosed, warranting bone-density screening and supplementation.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — The road to pancreatic cancer runs through p53: decades of inflammation in PRSS1 disease layer TP53 loss on top of the early KRAS mutation, the stepwise hits that give hereditary pancreatitis its steeply elevated lifetime cancer risk.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Inflammation by the pancreas clots the splenic vein: chronic pancreatitis can thrombose the adjacent splenic vein, producing gastric varices and a hypersplenism that drops the platelet count, a recognized vascular complication of the disease.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF drives the self-digesting gland: prematurely activated trypsin and dying acinar cells unleash TNF-α and other cytokines that recruit the inflammation, turning each attack of hereditary pancreatitis into tissue destruction.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Pancreatic inflammation reaches the deep veins: beyond the splenic vein, severe flares cause portal and mesenteric vein thrombosis and a systemic prothrombotic state, adding venous thromboembolism to the disease's vascular toll.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — A severe attack can flood the lungs: the systemic inflammation of acute-on-chronic pancreatitis can trigger acute respiratory distress syndrome, the leading early cause of death in a severe flare.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain is the defining burden: chronic pancreatitis sensitizes pancreatic and central nerves into a relentless neuropathic abdominal pain, often persisting even after the gland burns out — the symptom that dominates these patients' lives.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Decades of pain breed dependence: the severe, lifelong pain of hereditary pancreatitis often leads to chronic opioid therapy and the real risk of opioid use disorder, a hard management dilemma in a young-onset disease.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells wire pain into the inflamed gland: they accumulate around pancreatic nerves and, with activated stellate cells, drive the neuroinflammation and fibrosis that generate chronic pancreatitis pain.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Chronic inflammation steers the pancreas toward cancer through STAT3: persistent IL-6 in the repeatedly inflamed gland activates STAT3, a driver of the acinar-to-ductal change behind hereditary pancreatitis's high pancreatic-cancer risk.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A severe flare can rot and infect the gland: acute-on-chronic attacks of hereditary pancreatitis can produce infected pancreatic necrosis, a leading cause of the disease's mortality through sepsis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Relentless pain wears down the mind: the lifelong, often young-onset pain of hereditary pancreatitis, with its disability and opioid burden, drives high rates of depression that worsen the pain experience.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic inflammation and malabsorption lower the count: the persistent pancreatic inflammation of hereditary pancreatitis raises hepcidin while exocrine insufficiency impairs nutrient uptake, producing an anemia of chronic disease.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Severe attacks can injure the kidney: acute-on-chronic flares of hereditary pancreatitis cause hypovolemia and systemic inflammation that precipitate acute kidney injury, which over repeated episodes can leave chronic kidney impairment.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Chronic ductal inflammation can turn the bile ducts malignant: long-standing hereditary pancreatitis inflames the pancreaticobiliary region and, beyond pancreatic cancer, is associated with an elevated risk of cholangiocarcinoma.
- `connects-to` → **[Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Exocrine failure starves the body of iron: the fat and nutrient malabsorption of chronic pancreatic insufficiency in hereditary pancreatitis impairs iron uptake, contributing to anemia.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Malnutrition and surgery hinder repair: the protein-energy and fat-soluble-vitamin malabsorption of hereditary pancreatitis, plus its repeated pancreatic operations, leave wounds slow to heal.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Unrelenting pain and cancer risk breed worry: the recurrent severe abdominal pain, opioid dependence and lifelong pancreatic-cancer surveillance of hereditary pancreatitis foster chronic anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Severe attacks flood the lungs: an acute pancreatitis flare in hereditary pancreatitis can cause pleural effusions and acute respiratory distress syndrome from the systemic inflammatory response.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Leaked pancreatic enzymes mark the skin: severe pancreatitis causes the bruising of Cullen's and Grey-Turner's signs, and circulating lipase can produce a nodular pancreatic panniculitis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Enzyme release can inflame fat and joints: hereditary pancreatitis can cause the pancreatitis-panniculitis-polyarthritis syndrome, and chronic malabsorption of vitamin D weakens bone.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe attacks injure the kidney: acute pancreatitis causes third-spacing, hypovolaemia and shock that lead to acute kidney injury and tubular necrosis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — A severe attack collapses the circulation: acute pancreatitis triggers a systemic inflammatory response with capillary leak and distributive shock requiring aggressive fluid resuscitation.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Duct disruption leaks lymph and clots veins: pancreatic duct rupture can cause pancreatic and chylous ascites, and peripancreatic inflammation can thrombose the splenic vein.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It must be told apart from autoimmune disease: recurrent hereditary pancreatitis can mimic autoimmune (IgG4-related) pancreatitis, and repeated attacks drive chronic inflammatory injury to the gland.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It shapes family planning: as an autosomal-dominant PRSS1 disorder, hereditary pancreatitis raises genetic-counselling and prenatal questions for affected families.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — Pain control is a mainstay: NSAIDs like ibuprofen and stronger analgesics manage the recurrent abdominal pain of hereditary pancreatitis, though chronic use carries gastrointestinal and renal risk.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — Gut bacteria infect the dead tissue: in severe acute attacks, bacteria such as Escherichia coli translocate from the bowel to infect pancreatic necrosis, a life-threatening complication needing antibiotics and drainage.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Its great late danger is pancreatic cancer: hereditary pancreatitis carries a markedly raised lifetime risk of pancreatic adenocarcinoma, which is treated with chemotherapy when it arises.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — Fibrosis destroys the islets: repeated inflammation scars the pancreas and obliterates the islets of Langerhans, producing the pancreatogenic (type 3c) diabetes that complicates hereditary pancreatitis.
- `connects-to` → **[Hereditary Angioedema](../hereditary-angioedema/README.md)** — Diseases of an unchecked protease cascade: hereditary pancreatitis unleashes trypsin when its inhibitor SPINK1 fails, much as hereditary angioedema unleashes the kallikrein–bradykinin cascade when C1-inhibitor fails—each a missing brake on a destructive enzyme.
- `connects-to` → **[Curcumin](../../../03-medicine/03-food/curcumin/README.md)** — Antioxidants aimed at the pain: oxidative stress drives the inflammation and pain of chronic pancreatitis, and antioxidant compounds such as curcumin have been studied as adjuncts to reduce flares and pain in hereditary pancreatitis.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — When pancreatitis reaches the lungs: a severe attack floods the blood with proteases and cytokines that injure the alveolar–capillary membrane, causing the acute respiratory distress syndrome that makes severe hereditary pancreatitis life-threatening.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Biliary obstruction and the liver: chronic pancreatitis with head fibrosis compresses the bile duct, causing cholestasis that backs up into the hepatic lobule, while shared alcohol injures both organs.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — The relentless pain: pancreatic inflammation sensitises and remodels visceral and peripheral nerves, producing the severe neuropathic pain that dominates chronic pancreatitis and drives opioid use.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Pancreatic osteodystrophy: fat malabsorption and vitamin-D and calcium deficiency in chronic pancreatitis thin cortical bone, causing the osteoporosis and fractures common in these patients.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — SIRS of severe pancreatitis: a severe acute attack unleashes a systemic inflammatory response with ARDS and shock, the trypsin-triggered cytokine surge mechanistically overlapping a cytokine storm.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Vascular complications: chronic pancreatitis erodes nearby vessels, causing splenic-artery pseudoaneurysms of the arterial wall and splenic or portal vein thrombosis—dangerous bleeding and clotting.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infection-triggered pancreatitis: COVID-19 is a recognised cause of acute pancreatitis through ACE2 on acinar and islet cells, which can be severe on a background hereditary predisposition.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcium-triggered injury: sustained intra-acinar calcium activates calcineurin, driving the premature trypsinogen activation that initiates pancreatitis—a pathway protective when blocked experimentally.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Metaplasia toward cancer: repeated injury drives acinar-to-ductal metaplasia through EGFR signalling, which with KRAS sets chronic hereditary pancreatitis on the path to pancreatic cancer.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Microcirculatory failure: endothelin-1-driven vasoconstriction worsens pancreatic ischaemia in severe pancreatitis, converting interstitial inflammation toward necrotising disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome injury: premature trypsin activation triggers NLRP3-driven IL-1β release in hereditary pancreatitis, amplifying the acinar inflammation of each recurrent attack.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes and macrophages into the injured pancreas, sustaining the chronic inflammation that progresses to fibrosis in hereditary pancreatitis.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Ischaemic fibrosis: HIF-1α stabilised in the poorly perfused, fibrotic pancreas of chronic hereditary pancreatitis drives the stellate-cell activation that scars the gland.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Stellate-cell mitogen: PDGF is the dominant proliferative signal expanding pancreatic stellate cells into collagen-secreting myofibroblasts, the engine of the progressive fibrosis of chronic hereditary pancreatitis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Acute-attack alarmin: S100A8/A9 from the neutrophils flooding the inflamed gland amplifies each acute pancreatitis flare in hereditary pancreatitis and tracks the severity of the attack.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Cancer-risk progression: TERT reactivation immortalises cells along the path to pancreatic ductal adenocarcinoma, the markedly elevated cancer risk that follows decades of hereditary pancreatitis.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Whether injured acinar cells die by caspase-3-mediated apoptosis or by necrosis determines the severity of each attack—apoptosis is protective, while a shift toward necrosis drives the severe, systemic pancreatitis.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — DAMPs released by necrotic acinar cells engage TLR4 on innate immune cells, driving the systemic inflammatory response that makes severe acute attacks of hereditary pancreatitis life-threatening beyond the local gland injury.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Prematurely activated trypsin also activates the kallikrein-kinin system, generating bradykinin that drives the abdominal pain, vascular leak, and hypotension of a severe pancreatitis attack.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — A sustained rise in acinar-cell cytosolic calcium is the trigger that prematurely activates trypsin and causes acinar necrosis, the central initiating event of pancreatitis; chronic disease then deposits the ductal calcium of pancreatic calcification.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Recurrent attacks in hereditary pancreatitis activate pancreatic stellate cells to lay down collagen, the progressive fibrosis that destroys the gland and produces the exocrine insufficiency and diabetes of chronic pancreatitis.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Xanthine-oxidase-derived reactive oxygen species generated during an attack amplify acinar-cell injury and inflammation, the oxidative stress that worsens the necrosis of severe pancreatitis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Repeated injury and oncogenic KRAS (mapped) drive MAPK-ERK signaling that pushes acinar cells toward acinar-to-ductal metaplasia, the step that raises pancreatic-cancer risk in hereditary pancreatitis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 (mapped) signals through MyD88 to activate NF-κB (mapped) in response to acinar-cell injury, relaying the danger signal into the cytokine cascade of a pancreatitis attack.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β/SMAD4 signaling (TGF-β mapped) drives the pancreatic stellate-cell fibrosis of chronic pancreatitis, and SMAD4 loss marks progression to pancreatic ductal adenocarcinoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 signaling through JAK-STAT3 (IL-6 and STAT3 already mapped) sustains the chronic inflammation and acinar-to-ductal reprogramming of hereditary pancreatitis.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense counters the oxidative stress of recurrent acinar injury (xanthine-oxidase already mapped) in hereditary pancreatitis.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss is a key step in the markedly elevated progression of hereditary pancreatitis to pancreatic ductal adenocarcinoma, alongside the KRAS and TP53 lesions already mapped.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling modulates acinar-cell survival and the inflammatory response in the recurrent acute episodes of hereditary pancreatitis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR regulation of autophagy/zymophagy (autophagy mapped) governs the clearance of prematurely activated zymogens, a protective process overwhelmed in hereditary pancreatitis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 secreted in the injured pancreas activates stellate cells and amplifies the fibrosis of chronic hereditary pancreatitis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA released by repeated acinar-cell injury engages cGAS-STING, amplifying the sterile inflammation of recurrent hereditary pancreatitis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune response within the chronically inflamed pancreas of hereditary pancreatitis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) in stressed acinar cells contributes to the survival and the malignant-transformation risk of hereditary pancreatitis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the acinar-cell oxidative-stress and autophagy responses to the recurrent trypsinogen-activation injury of hereditary pancreatitis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the NF-κB-driven inflammatory signaling of the recurrent acinar injury of hereditary pancreatitis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) shapes the cancer risk arising from the chronic inflammation of hereditary pancreatitis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is relevant to the immune injury and cancer risk of the chronically inflamed pancreas of hereditary pancreatitis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the acinar-cell metabolic stress of hereditary pancreatitis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling contributes to the acinar-cell injury and fibrotic responses of hereditary pancreatitis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the inflammation of recurrent hereditary pancreatitis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic changes accompanying the chronic inflammation and cancer risk of hereditary pancreatitis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation implicated in the progression of hereditary pancreatitis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the pancreatic-stellate-cell activation and leukocyte trafficking of hereditary pancreatitis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the pancreatic inflammation and fibrosis of hereditary pancreatitis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the chronic inflammation and fibrogenesis of hereditary pancreatitis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory milieu of the recurrent pancreatic inflammation of hereditary pancreatitis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunomodulation of the pancreatic inflammation of hereditary pancreatitis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the pancreatic stellate-cell activation and fibrosis of hereditary pancreatitis.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Chronic pain: recurrent and then constant abdominal pain from childhood is the dominant clinical burden of hereditary pancreatitis, and its management with opioids acting at the mu-opioid receptor risks dependence, a major therapeutic dilemma.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Neurogenic pancreatic pain: chronic pancreatitis sensitises and remodels pancreatic sensory nerves, with substance P and neurogenic inflammation amplifying the visceral pain that persists even as the gland burns out.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune inflammation: MHC class II-restricted T-cell responses participate in the immune component of chronic pancreatitis and its overlap with autoimmune pancreatitis, alongside the innate inflammasome signalling (NLRP3 already mapped).
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Malnutrition anaemia: exocrine insufficiency in hereditary pancreatitis causes fat and micronutrient malabsorption, and chronic disease with iron and vitamin deficiency lowers haemoglobin, the anaemia adding to the debility of the burnt-out gland.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Pancreatogenic diabetes: progressive islet loss produces the type-3c diabetes of hereditary pancreatitis (insulin and glucagon already mapped), and the incretin GLP-1 axis is disturbed as the enteroinsular signalling of the damaged gland fails.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory mediators: prostaglandins amplify the pancreatic inflammation and pain of hereditary pancreatitis, and NSAIDs that block their synthesis are used, notably rectal indomethacin to prevent post-ERCP pancreatitis.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory counterweight: the anti-inflammatory IL-10 opposes the pro-inflammatory cytokines (TNF, IL-6 and IL-1 already mapped) driving the recurrent pancreatic inflammation, part of the immune balance shaping progression to chronic pancreatitis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Fat malabsorption: the exocrine insufficiency of chronic hereditary pancreatitis causes fat malabsorption, disturbing cholesterol and essential-fatty-acid handling and the absorption of fat-soluble vitamins, part of its nutritional burden.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant therapy: the oxidative stress (NRF2 and xanthine oxidase already mapped) of chronic pancreatitis has prompted antioxidant regimens including selenium to reduce pain and inflammation, a studied adjunct in hereditary pancreatitis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Pro-fibrotic type-2: IL-4 drives the M2 macrophage and pro-fibrotic (TGF-β already mapped) programme that lays down the collagen (already mapped) fibrosis of chronic hereditary pancreatitis (IL-10 already mapped).
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 fibrosis: IL-13, with IL-4 (already mapped), is a potent pro-fibrotic cytokine driving the pancreatic stellate-cell (fibroblast already mapped) fibrosis of chronic hereditary pancreatitis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Malabsorption anaemia: the exocrine insufficiency and the chronic inflammation of hereditary pancreatitis impair nutrient absorption and cause an anaemia (haemoglobin already mapped) with disturbed iron handling.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and, with the malabsorption, produces the anaemia (haemoglobin already mapped) of chronic hereditary pancreatitis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Malnutrition adipokine: leptin reflects the malnutrition and the pancreatogenic-diabetes (insulin already mapped) metabolic disturbance of the exocrine and endocrine insufficiency of hereditary pancreatitis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic disturbance of the pancreatic insufficiency of hereditary pancreatitis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) and metabolic disturbance of hereditary pancreatitis.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunosurveillance: the cytotoxic T cells (perforin already mapped) provide the immune surveillance of the high pancreatic-cancer risk of the chronic inflammation of hereditary pancreatitis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate pancreatitis interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the acinar cell-death DNA, is part of the innate-immune signalling of the recurrent inflammation of hereditary pancreatitis.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the chronic inflammation (IL-6 and TNF already mapped) driving the fibrosis and the pancreatic-cancer risk of hereditary pancreatitis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of hereditary pancreatitis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune response of hereditary pancreatitis.

[^whitcomb-1996-prss1]: Whitcomb DC, Gorry MC, Preston RA, et al. Hereditary pancreatitis is caused by a mutation in the cationic trypsinogen gene. *Nat Genet.* 1996;14(2):141-145. [doi:10.1038/ng1096-141](https://doi.org/10.1038/ng1096-141) · [PubMed 8841182](https://pubmed.ncbi.nlm.nih.gov/8841182/)
[^lowenfels-2001-hp-pdac]: Lowenfels AB, Maisonneuve P, DiMagno EP, et al. Hereditary pancreatitis and the risk of pancreatic cancer. *J Natl Cancer Inst.* 2001;93(1):26-31. [doi:10.1093/jnci/93.1.26](https://doi.org/10.1093/jnci/93.1.26) · [PubMed 11136838](https://pubmed.ncbi.nlm.nih.gov/11136838/)
