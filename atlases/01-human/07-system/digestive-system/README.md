---
schema: human-scale-entry/v1
id: digestive-system
name: Digestive System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-04
summary: "Alimentary canal (~9 m, mouth to anus) plus accessory organs (liver, gallbladder, pancreas). Performs mechanical/chemical digestion, nutrient absorption, water reabsorption, and waste excretion. Enteric nervous system (~100M neurons) provides semi-autonomous regulation."
aliases: ["gastrointestinal system", "GI system", "alimentary system"]
sources:
  - id: hall-guyton-14-gi
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 63-72."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
  - id: openstax-anatomy-ch23
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 23: The Digestive System."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/23-introduction"
    accessed: "2026-06-04"
  - id: who-global-hepatitis
    type: regulatory
    cite: "World Health Organization. Global Hepatitis Report 2024. WHO; 2024."
    url: "https://www.who.int/publications/i/item/9789240091672"
    accessed: "2026-06-04"
  - id: sung-2021-global-cancer-stats
    type: peer-reviewed
    cite: "Sung H, Ferlay J, Siegel RL, et al. Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries. CA Cancer J Clin. 2021;71(3):209-249."
    doi: "10.3322/caac.21660"
    pmid: "33538338"
    url: "https://doi.org/10.3322/caac.21660"
  - id: bray-2024-colorectal
    type: peer-reviewed
    cite: "Siegel RL, Wagle NS, Cercek A, Smith RA, Jemal A. Colorectal cancer statistics, 2023. CA Cancer J Clin. 2023;73(3):233-254."
    doi: "10.3322/caac.21772"
    pmid: "36856579"
    url: "https://doi.org/10.3322/caac.21772"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The digestive system is one of the primary organ systems of the human body, responsible for nutrient intake and processing."
  - target: 01-human/06-organ/liver
    relation: contains
    note: "The liver is the dominant accessory organ of digestion, processing all portal blood from the GI tract, producing bile, and regulating systemic nutrient levels."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Portal vein drains entire GI tract to liver before entering systemic circulation; absorbed lipids enter lymphatics (chylomicrons) → thoracic duct → left subclavian vein → circulation. Splanchnic circulation comprises ~25% of cardiac output."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Water and electrolyte balance is jointly regulated between GI absorption (small/large intestine) and renal reabsorption/secretion; GI fluid losses (diarrhea, vomiting) are a major cause of prerenal AKI."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "SARS-CoV-2 causes GI symptoms (diarrhea, nausea, vomiting) in up to 50% of patients via ACE2 expressed on enterocytes and cholangiocytes; liver injury occurs in 14-53% of COVID-19 patients."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: damaged-by
    note: "GI tuberculosis: ileocecal TB (most common site), peritoneal TB, hepatic TB; M. tuberculosis can infect any GI segment via swallowed sputum or hematogenous spread."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: infected-by
    note: "HBV infects hepatocytes within the liver — the dominant accessory digestive organ — via NTCP receptor; cccDNA persistence drives chronic liver disease that manifests throughout the digestive system."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: damaged-by
    note: "HBV primarily damages the liver (an accessory digestive organ), causing chronic hepatitis, cirrhosis, and portal hypertension; GI manifestations include variceal bleeding, ascites, and hepatic encephalopathy."
  - target: 01-human/03-molecular/serotonin
    relation: modulated-by
    note: "~95% of body serotonin resides in enterochromaffin cells of the GI mucosa; 5-HT4 receptor activation drives the peristaltic reflex; 5-HT3 mediates nausea and vomiting; 5-HT coordinates enteric nervous system motility throughout the gut."
  - target: 01-human/03-molecular/insulin
    relation: modulates
    note: "Gut-derived incretin hormones (GLP-1 from L-cells, GIP from K-cells) amplify glucose-stimulated insulin secretion; postprandial nutrient absorption in the small intestine is the primary physiological trigger for insulin release."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: contains
    evidence: openstax-anatomy-ch23
    note: "The intestinal epithelium is the primary cellular barrier of the digestive system, covering ~32 m² of luminal surface."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: infected-by
    evidence: hall-guyton-14-gi
    note: "ETEC and EHEC colonise and infect the intestinal epithelium of the digestive system, causing diarrhoea, HUS, and intestinal inflammation."
  - target: 02-pathogen/06-microbiome/lactobacillus-rhamnosus
    relation: modulated-by
    evidence: hall-guyton-14-gi
    note: "L. rhamnosus GG colonises the gut epithelium, modulating digestive system function by enhancing barrier integrity and reducing transit time in antibiotic-associated diarrhoea."
  - target: 01-human/06-organ/pancreas
    relation: modulated-by
    note: "The exocrine pancreas secretes ~1.5 L/day of bicarbonate-rich fluid containing amylase, lipase, and proteases into the duodenum via the pancreatic duct, providing the digestive system's principal luminal enzyme activity."
  - target: 01-human/03-molecular/glucagon
    relation: modulated-by
    note: "Modulated by Glucagon."
  - target: 01-human/06-organ/large-intestine
    relation: composed-of
    note: "Composed Of by Large Intestine."
  - target: 01-human/06-organ/small-intestine
    relation: composed-of
    note: "Composed Of by Small Intestine."
  - target: 01-human/06-organ/stomach
    relation: composed-of
    note: "Composed Of by Stomach."
  - target: 02-pathogen/01-viruses/norovirus
    relation: damaged-by
    note: "Damaged by Norovirus."
  - target: 02-pathogen/01-viruses/rotavirus
    relation: damaged-by
    note: "Damaged by Rotavirus."
  - target: 02-pathogen/06-microbiome/bacteroides-fragilis
    relation: modulated-by
    note: "Modulated by Bacteroides fragilis."
  - target: 02-pathogen/06-microbiome/akkermansia-muciniphila
    relation: modulated-by
    note: "Modulated by Akkermansia muciniphila."
  - target: 02-pathogen/06-microbiome/faecalibacterium-prausnitzii
    relation: modulated-by
    note: "Modulated by Faecalibacterium prausnitzii."
  - target: 02-pathogen/06-microbiome/bifidobacterium-longum
    relation: modulated-by
    note: "Modulated by Bifidobacterium longum."
  - target: 02-pathogen/04-parasites/giardia-lamblia
    relation: damaged-by
    note: "Damaged by Giardia lamblia (G. intestinalis / G. duodenalis)."
  - target: 02-pathogen/04-parasites/leishmania-donovani
    relation: damaged-by
    note: "Damaged by Leishmania donovani."
  - target: 02-pathogen/02-bacteria/salmonella-typhi
    relation: damaged-by
    note: "Damaged by Salmonella typhi."
  - target: 02-pathogen/02-bacteria/clostridioides-difficile
    relation: damaged-by
    note: "Damaged by Clostridioides difficile."
  - target: 02-pathogen/02-bacteria/listeria-monocytogenes
    relation: infected-by
    note: "Infected by Listeria monocytogenes."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: damaged-by
    note: "Damaged by Helicobacter pylori."
  - target: 03-medicine/03-food/dietary-fiber
    relation: modulated-by
    note: "Modulated by Dietary Fiber and Butyrate."
  - target: 01-human/03-molecular/ghrelin
    relation: modulated-by
    note: "Ghrelin from gastric fundus X/A cells rises preprandially → vagal GHSR1a → gastric motility (prokinetic); relamorelin (GHSR1a agonist) showed Phase 2b efficacy for diabetic gastroparesis; ghrelin falls after eating, coordinating hunger and gastric emptying."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The gut moves food by peristalsis: rings of smooth muscle contract in waves from esophagus to colon, coordinated by the enteric nervous system, so motility disorders arise when this muscle or its control fails."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "The gut is the body's gateway for iron: the duodenum absorbs dietary iron, so malabsorption or chronic GI bleeding here is a leading cause of iron-deficiency anemia."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "The digestive tract is explored with light and radiation: endoscopy shines visible-light photons into the gut lumen, while X-ray photons in barium studies and CT trace its structure and motility."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals how the gut absorbs so much: each enterocyte is crowned with a brush border of densely packed microvilli that multiplies the absorptive surface many times over, the ultrastructure behind nutrient uptake."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium powers digestion's uptake: the sodium gradient set by membrane pumps drives the cotransporters that haul glucose, amino acids, and water across the gut lining — the principle that makes salt-and-sugar oral rehydration save lives."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "The hepatocyte is the digestive system's chemical plant: it makes the bile that emulsifies fat and receives the nutrient-rich portal blood from the gut, processing and storing what the intestine absorbs."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The gut runs its own brain: the enteric nervous system, ~500 million neurons in the bowel wall, drives peristalsis and secretion largely autonomously, while the vagus-linked gut-brain axis ties digestion to mood and appetite."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Most of the body's immune cells guard the gut: gut-associated lymphoid tissue (Peyer's patches, lamina propria) polices the vast luminal antigen load, tolerating food and flora while repelling pathogens across a single-cell barrier."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The digestive tract houses an organ of microbes: trillions of gut bacteria ferment fiber into short-chain fatty acids, synthesize vitamins, train immunity, and shape motility — a metabolic partner the system feeds and depends on."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The gut is the body's largest antibody factory: plasma cells in the lamina propria pump out secretory IgA that bathes the mucosa, neutralizing pathogens and shaping the flora while teaching tolerance to food and friendly microbes."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The gut is also the largest endocrine organ: scattered enteroendocrine cells release ghrelin, CCK, secretin, gastrin, and GLP-1 that pace digestion and signal hunger and fullness to the brain, the gut-hormone arm of metabolism."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "A vast, restrained macrophage army lines the gut: the largest pool of macrophages in the body clears the trickle of bacteria crossing the barrier yet stays tolerant, and when that balance breaks, inflammatory bowel disease follows."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The gut runs its own nervous system: the enteric nervous system, a mesh of millions of neurons in the bowel wall, coordinates peristalsis and secretion largely on its own, earning the gut its name as the body's second brain."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "The gut is an endocrine organ: L-cells release GLP-1 after a meal to spur insulin, slow gastric emptying and curb appetite, the incretin axis now harnessed by the blockbuster GLP-1 weight and diabetes drugs."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Gut microbes help set circulating estrogen: the estrobolome — bacterial enzymes that deconjugate estrogens for reabsorption — links the digestive tract to reproductive and hormonal health across the body."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "When gut tolerance breaks, the wall inflames: inflammatory bowel disease is the digestive system turning on itself, as a misfired immune response to the microbiome ulcerates the bowel — the chronic counterpart to the gut's normal restraint."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "The gut decides friend from foe through dendritic cells: they reach between epithelial cells to sample luminal antigens, then teach tolerance to food and flora or mount defense against pathogens — the gatekeepers of intestinal immunity."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine drives the stomach's acid: enterochromaffin-like cells release it to stimulate parietal-cell acid secretion through H2 receptors, the pathway that H2-blockers shut down to treat ulcers and reflux."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Its most common cancer grows from the lining: colorectal cancer arises from the glandular epithelium of the large bowel, the digestive system's leading malignancy and the reason colonoscopy screens the tract for precancerous polyps."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Chronic injury to the stomach turns malignant: gastric cancer develops from the gastric mucosa after years of H. pylori infection, inflammation and atrophy, a digestive-tract cancer still common worldwide."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "An accessory organ harbors a lethal cancer: pancreatic adenocarcinoma arises from the ductal cells of the pancreas, a digestive gland, and its silent deep location makes it one of the deadliest cancers of the system."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Its biliary tree can turn malignant: cholangiocarcinoma arises in the bile ducts that drain the liver into the gut, a hepatobiliary cancer of the digestive system often linked to chronic inflammation of the ducts."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "The liver fattens and inflames: NASH is the inflammatory fatty-liver disease of the digestive system's largest gland, driven by metabolic excess and progressing toward cirrhosis and liver cancer."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "A commensal yeast can turn invader: Candida normally lives quietly in the gut, but disrupted flora or immunity let it overgrow into oral and esophageal candidiasis along the upper digestive tract."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Gut and brain talk constantly: most of the body's serotonin is made in the gut and the microbiome signals along the gut-brain axis, so digestive function and mood are tightly linked in both directions."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "The gut sets the metabolic tone: intestinal incretin hormones like GLP-1, nutrient absorption and the microbiome shape insulin secretion and resistance, placing the digestive system at the heart of type 2 diabetes."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "It both absorbs iron and loses it: the gut is the sole site of iron uptake, so malabsorption or chronic bleeding from ulcers, tumors or inflammation along the tract is a leading cause of iron-deficiency anemia."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The gut is the body's largest immune and lymphatic organ: gut-associated lymphoid tissue and Peyer's patches guard the lumen, while intestinal lacteals absorb dietary fat into the lymphatics as chyle."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "They share an origin and a crossroads: the gut and airways arise from the same primitive foregut and meet at the pharynx, so swallowing disorders cause aspiration and a gut-lung axis links the two."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The gut shows on the skin: malabsorption produces hair, nail and skin changes, liver disease causes jaundice, and a gut-skin axis links conditions like coeliac disease to dermatitis herpetiformis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The gut feeds the skeleton: it absorbs the calcium and vitamin D that build bone, so malabsorption from coeliac or bowel disease causes osteoporosis and osteomalacia, while inflammatory bowel disease brings enteropathic arthritis."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "A virus that smoulders in the liver: hepatitis C establishes chronic infection of hepatocytes, driving cirrhosis and hepatocellular carcinoma, though direct-acting antivirals now cure most cases."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Zinc and the gut depend on each other: zinc is absorbed in the small intestine and maintains mucosal integrity, so malabsorption causes deficiency with diarrhoea and acrodermatitis, and supplementation shortens acute diarrhoea."
  - target: 03-medicine/01-modern/08-gi/omeprazole
    relation: connects-to
    note: "A drug that quietens the stomach: proton pump inhibitors like omeprazole suppress gastric acid to heal ulcers and reflux, but long-term use can impair absorption of B12, iron, calcium and magnesium and alter the gut microbiome."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "A common painkiller that ulcerates it: NSAIDs like ibuprofen block the prostaglandins that protect the gastric lining, causing peptic ulcers and gastrointestinal bleeding."
  - target: 03-medicine/03-food/curcumin
    relation: connects-to
    note: "A spice studied for the gut: curcumin from turmeric has anti-inflammatory effects investigated in inflammatory bowel disease, though its poor absorption limits how much reaches the bloodstream."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Dietary fats shape gut health: long-chain omega-3 fatty acids, absorbed via intestinal lacteals, have anti-inflammatory effects studied in inflammatory bowel disease and the gut-liver axis."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: connects-to
    note: "Enteroviruses pass through the gut: Coxsackie and other enteroviruses are swallowed and replicate in the intestinal lining, causing herpangina and hand-foot-and-mouth disease before systemic spread."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "The gut handles magnesium two ways: the intestine absorbs dietary magnesium, and poorly absorbed magnesium salts act as osmotic laxatives, while malabsorption causes deficiency."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "It begins at the top of the tract: esophageal cancer — squamous from smoking and alcohol, adenocarcinoma from reflux and Barrett's — completes the digestive tract's malignancies alongside gastric, colorectal and pancreatic cancer."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The liver is its chemical factory: the hepatic lobule, the liver's functional unit, processes everything absorbed from the gut via the portal vein, secretes bile for fat digestion, and detoxifies and stores the nutrients the gut delivers."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "It both treats and is harmed: the gut's common cancers depend on cytotoxic chemotherapy, while the rapidly dividing intestinal lining makes the digestive tract a prime victim of chemo, producing the mucositis, nausea and diarrhoea that limit dosing."
  - target: 01-human/05-tissue/peyers-patches
    relation: connects-to
    note: "The gut's immune sentinels: Peyer's patches in the small-intestinal wall sample luminal antigens through M cells, the gut-associated lymphoid tissue where the digestive and immune systems meet."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "The endocrine pancreas within the gut: the islets of Langerhans, embedded in the digestive organ that also makes digestive enzymes, secrete insulin and glucagon to regulate the metabolism of absorbed nutrients."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "Its commonest mesenchymal tumour: gastrointestinal stromal tumours arise from the interstitial cells of Cajal—the gut's pacemaker cells—anywhere from oesophagus to rectum, distinct from the epithelial carcinomas of the digestive tract."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Cancer of the digestive system's largest organ: hepatocellular carcinoma arises in the chronically injured liver—from viral hepatitis, alcohol or fatty liver—the dominant primary cancer of the gut's metabolic powerhouse."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "The metabolic burden on the gut: obesity reshapes bile acids and the microbiome and drives fatty liver, gallstones, reflux and colorectal cancer, tying excess adiposity to disease across the digestive tract."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The portal partner: the spleen drains into the portal vein, so cirrhosis and portal hypertension cause congestive splenomegaly and hypersplenism—linking digestive disease to sequestration of blood cells."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "The gut-brain axis: Parkinson's may begin in the enteric nervous system, with alpha-synuclein aggregating in the gut wall and ascending the vagus nerve, and constipation often precedes the motor disease by years."
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "Recurrent pancreatic injury: hereditary pancreatitis (PRSS1) causes repeated attacks of pancreatitis in the digestive system's exocrine pancreas, leading to chronic pancreatitis and a high lifetime pancreatic-cancer risk."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Two roles for one organ: the pancreas is both a digestive (exocrine) and endocrine gland, and type 1 diabetes destroys its islets of Langerhans, the endocrine cells embedded within this digestive organ."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Parasympathetic drive: acetylcholine is the principal enteric and vagal neurotransmitter stimulating gut motility, secretion and sphincter function throughout the digestive tract."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Inhibitory neurotransmission: nitric oxide from enteric inhibitory neurons relaxes gut smooth muscle for peristalsis and sphincter opening, with its loss causing achalasia and pyloric stenosis."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Toxin food poisoning: preformed staphylococcal enterotoxin causes rapid-onset vomiting and diarrhoea, a classic toxin-mediated gastroenteritis of the digestive tract."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal defence: dimeric secretory IgA transcytosed across gut epithelium coats luminal microbes and toxins, shaping the microbiota and protecting the digestive mucosal surface from invasion."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Satiety signalling: leptin from adipose and gastric chief cells acts on the gut-brain axis and enteric neurons to curb appetite and modulate motility, linking digestion to energy balance."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Barrier homeostasis: TGF-beta drives intestinal epithelial repair and oral tolerance, inducing regulatory T cells that restrain immune responses to food antigens and commensal flora in the gut."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Mucosal cytoprotection: prostaglandins (PGE2) maintain the gastric mucus-bicarbonate barrier and mucosal blood flow, which is why NSAIDs that block their synthesis predispose to gastric and duodenal ulcers."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Enteric peristalsis: substance P from enteric neurons is an excitatory tachykinin that contracts gut smooth muscle, helping coordinate the peristaltic reflex that propels contents through the digestive tract."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Sensory gastroprotection: CGRP released from gut sensory afferents increases mucosal blood flow and defends the stomach lining against acid and injury, a neural protective reflex of the gastrointestinal mucosa."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Universal inhibitory hormone: somatostatin from gut D cells acts through SSTR2 to brake acid secretion, gastrin release and motility, the master off-switch of the gastrointestinal tract exploited therapeutically by octreotide in bleeding and secretory diarrhoea."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile-acid digestion: the liver converts cholesterol into bile acids that emulsify dietary fat into micelles for pancreatic-lipase digestion and absorption, then recovers them through the enterohepatic circulation, the GI tract's fat-handling system."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Colonic fluid recovery: aldosterone drives sodium and water reabsorption across the distal colonic epithelium, the final electrolyte- and fluid-conserving step of the gastrointestinal tract that hardens stool and prevents dehydration."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Crypt stem-cell renewal: Wnt/β-catenin signalling from the intestinal crypt base drives the continuous self-renewal of the gut epithelium, the most rapidly regenerating tissue in the body and the basis of digestive-tract homeostasis."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Cell-fate patterning: NOTCH signalling sets the choice between absorptive enterocytes and secretory (goblet, enteroendocrine, Paneth) cells in the intestinal epithelium, patterning the functional surface of the digestive lining."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Microbiota tolerance: regulatory IL-10 maintains immune tolerance to the gut microbiota, and its loss breaks digestive-tract homeostasis to drive the intestinal inflammation of inflammatory bowel disease."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Epithelial renewal: EGF-family signalling drives the continuous renewal of the gut epithelium from Wnt-driven crypt stem cells (Wnt mapped), maintaining the rapidly turning-over digestive lining."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Enteric motility: μ-opioid receptors on enteric neurons slow gut motility and secretion, the basis of opioid-induced constipation and a node of the enteric nervous control of digestion."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Microbiota sensing: intestinal epithelial TLR4 senses the gut microbiota, calibrating the mucosal immune tolerance (with secretory-IgA and IL-10 mapped) that maintains digestive homeostasis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microbiota signal transduction: epithelial and immune TLR signalling through MyD88 (TLR4 already mapped) transduces gut-microbiota cues into the mucosal homeostasis and barrier defence of the digestive tract."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Crypt nutrient sensing: mTOR nutrient-sensing in intestinal crypt stem cells couples luminal nutrient availability to the continuous epithelial renewal of the gut lining."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Mucosal inflammatory balance: NF-κB signalling in the intestinal epithelium balances antimicrobial defence against tolerance, governing the inflammatory homeostasis of the gut mucosa."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates mucosal immunity and epithelial repair in the gut and contributes to the fibrosis that follows chronic intestinal inflammation."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING in the intestinal mucosa links microbial and damage-associated DNA to the inflammatory tone of the gut."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α responds to the steep physiological oxygen gradient of the gut lumen and supports the barrier function and metabolism of the intestinal epithelium."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling (TGF-β already mapped) governs epithelial homeostasis, mucosal fibrosis, and the regulatory immune tone of the digestive tract."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signaling drives the epithelial regeneration and mucosal inflammatory tone of the gastrointestinal tract."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate intestinal stem-cell homeostasis and the metabolic and oxidative-stress responses of the gut epithelium."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signaling governs the proliferation and survival of the rapidly renewing intestinal epithelium of the digestive system."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of growth-factor and hormone receptors drives the epithelial renewal and secretory responses of the digestive system."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β, within the Wnt destruction complex (Wnt already mapped), governs the crypt stem-cell renewal of the intestinal epithelium of the digestive system."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the epithelial proliferation and renewal of the gastrointestinal mucosa of the digestive system."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK integrates the nutrient and energy status of the enterocytes and hepatocytes of the digestive system."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the mucosal immune surveillance of the digestive system."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy maintains the epithelial homeostasis, Paneth-cell function, and mucosal barrier of the digestive system."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the epithelial junction dynamics and growth-factor responses of the digestive system."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the epithelial renewal and immune tolerance of the digestive system."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling participates in the mucosal immune trafficking of the digestive system."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the epithelial-stromal and immune interactions of the digestive system."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 signaling participates in the mucosal immune and epithelial-regeneration processes of the digestive system."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Gastric acid: parietal cells secrete hydrochloric acid by pumping protons through the H+/K+ ATPase, the target of proton-pump inhibitors, creating the acidic lumen that activates pepsin and provides a barrier against ingested microbes."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Mineral absorption: the small intestine absorbs dietary calcium under vitamin D control, so the digestive tract governs the calcium supply for bone and neuromuscular function and becomes a source of deficiency when absorption fails."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Enteric melatonin: the gut's enterochromaffin cells produce far more melatonin than the pineal gland, where it regulates intestinal motility and provides mucosal antioxidant protection, an under-recognised digestive-system endocrine function."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Enteric dopamine: the gut contains large amounts of dopamine that modulates motility and secretion, and dopamine-receptor drugs (prokinetics like metoclopramide, antiemetics) act on this enteric dopaminergic system of the digestive tract."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Colonic potassium: the colon secretes and absorbs potassium under aldosterone control (aldosterone already mapped), an electrolyte-handling role of the digestive tract that becomes clinically important in diarrhoea and renal failure."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Enteric nervous system: BDNF and neurotrophic signalling support the enteric nervous system, the gut's intrinsic 'second brain' of over a hundred million neurons that coordinates the motility and secretion of the digestive system."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc absorption: the small intestine absorbs dietary zinc, essential for the many digestive enzymes and for mucosal integrity and taste, and malabsorption causes the dermatitis and diarrhoea of zinc deficiency."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mucosal mast cells: mast cells in the gut wall (histamine already mapped) defend the mucosa and, when dysregulated, contribute to the visceral hypersensitivity and altered motility of functional gastrointestinal disorders."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Secretory chloride: chloride secretion by the intestinal epithelium drives the fluid that lubricates digestion, and its dysregulation underlies the secretory diarrhoea of infections and the defect of cystic fibrosis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The gut-brain axis: the enteric nervous system and the vagal and serotonergic signalling (serotonin, dopamine and BDNF already mapped) link the digestive system to the nervous system, coordinating motility, secretion and appetite."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium-coupled absorption: sodium gradients power the absorption of glucose and amino acids across the intestinal epithelium, and sodium handling (chloride already mapped) governs the fluid balance of the digestive tract."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Gut mucosal macrophages: the macrophages of the gut wall and the Kupffer cells of the liver sample the luminal contents and maintain tolerance (secretory IgA already mapped), a large part of the body's immune tissue serving the digestive system."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium absorption: the small intestine of the digestive system absorbs dietary magnesium, and the malabsorption of gut disease (or proton-pump inhibitors) causes the hypomagnesaemia of digestive disorders."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Gut inflammation: TNF from the gut-associated lymphoid tissue (IL-6 and IL-10 already mapped) is a central mediator of the inflammation of the digestive tract, the target of anti-TNF therapy in inflammatory bowel disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Mucosal Th17 defence: IL-17 from the gut mucosal Th17 cells defends the epithelial barrier of the digestive system against invading microbes, and its dysregulation drives the inflammation of gut immune disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is the adipokine signalling that links the digestive system's nutrient handling to the whole-body energy and metabolic balance."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the visceral adipose and the digestive-system nutrient handling to the metabolic-inflammatory state."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Gut IgA plasma cells: the intestinal plasma cells — the largest plasma-cell pool in the body — secrete the secretory IgA (already mapped) that defends the mucosal barrier of the digestive system."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "GALT B cells: the gut-associated lymphoid tissue B cells class-switch to the IgA (secretory-IgA already mapped) and populate the plasma-cell (already mapped) pool of the digestive-system mucosal immunity."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Oral tolerance: the intestinal regulatory T cells maintain the tolerance to the food antigens and the commensal microbiome (gut-microbiome already mapped) of the digestive system."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Gut adaptive immunity: the CD4 T-helper cells of the gut-associated lymphoid tissue coordinate the mucosal immune response and the barrier defence of the digestive system."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 mucosal immunity: IL-4, a type-2 cytokine, drives the anti-helminth and the goblet-cell/mucus response of the gut mucosal immunity of the digestive system."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 barrier: IL-13, with IL-4 (already mapped), drives the goblet-cell mucus and the epithelial-barrier type-2 response of the digestive system."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the gut eosinophils of the anti-parasite type-2 immunity of the digestive system."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the mucosal barrier defence and the inflammatory tone of the gut of the digestive system."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/allergy arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), is the antibody arm of the anti-parasite and food-allergy type-2 immunity of the digestive system."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Epithelial alarmin: IL-33, released by the injured gut epithelium, activates the ILC2s and initiates the type-2 (IL-4, IL-5 and IL-13 already mapped) mucosal immunity of the digestive system."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Mucosal complement: the complement C3, produced locally and from the liver (already mapped), opsonises the gut microbes and is part of the innate mucosal defence of the digestive system."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the neutrophil recruitment into the intestinal mucosa during the innate immune response of the digestive system."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Mucosal neutrophils: the neutrophils are recruited into the intestinal mucosa and lumen as the innate effectors of the antimicrobial defence of the digestive system."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial alarmin: TSLP, secreted by intestinal epithelial cells under microbial and mechanical stress, polarises dendritic cells (already mapped) toward Th2 tolerance and tunes the mucosal immune set-point of the digestive system."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Gut EPO axis: erythropoietin, produced by the intestinal epithelium under hypoxic stress, supports epithelial repair, modulates the enteric immune tone, and links gut oxygenation to the systemic haematopoietic response of the digestive system."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement gateway: complement C5 cleavage in the intestinal lamina propria generates C5a (signalling via C5aR1 already mapped) and C5b-9 MAC, amplifying the inflammatory and tissue-remodelling responses of the digestive system."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin mediator: bradykinin, generated by kallikrein activation in the intestinal mucosa during injury and inflammation, amplifies vascular permeability, smooth-muscle contraction (already mapped) and nociceptive signalling of the digestive system."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact/complement regulator: the C1-esterase inhibitor regulates the classical complement and contact-kinin (bradykinin and kallikrein) pathways activated in the intestinal mucosa, moderating the inflammatory cascade of the digestive system."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Stromal ECM scaffold: periostin, secreted by subepithelial fibroblasts (already mapped) of the intestinal crypt niche, maintains the basement-membrane integrity and supports epithelial regeneration and stem-cell quiescence of the digestive system."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "DS testosterone: testosterone modulates liver (already mapped) bile metabolism and smooth-muscle-cell (already mapped) motility in the gut; androgen signalling shapes the gut microbiome (already mapped) composition and the IL-6 (already mapped) intestinal inflammatory tone."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "DS prolactin: prolactin receptors on intestinal epithelium (already mapped) promote mucosal cell proliferation; prolactin also stimulates pancreatic (already mapped) enzyme secretion and modulates the gut-microbiome (already mapped) composition via immune crosstalk."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "DS oxytocin: oxytocin regulates gut motility by modulating smooth-muscle-cell (already mapped) contractility and the enteric nervous system; oxytocin also enhances intestinal epithelium (already mapped) barrier integrity and the gut-microbiome (already mapped) microbial balance."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "DS vasopressin: vasopressin (ADH) regulates intestinal water absorption via V2/aquaporin-2 in the intestinal epithelium (already mapped); AVP-driven cAMP pathway modulates gut-microbiome (already mapped) colonisation resistance and NF-κB (already mapped) mucosal immunity."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "DS selenium: selenoproteins in the intestinal epithelium (already mapped) counter NF-κB (already mapped) oxidative stress; selenium deficiency impairs gut-microbiome (already mapped) diversity and amplifies macrophage (already mapped) mediated mucosal inflammation."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "DS iodine: intestinal lactoperoxidase (iodine-dependent) in the epithelium (already mapped) limits pathogen colonisation; iodine deficiency amplifies NF-κB (already mapped) driven gut-microbiome (already mapped) dysbiosis and impairs macrophage (already mapped) mucosal defence."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "DS phosphorus: phosphorus fuels epithelial-cell (already mapped) and macrophage (already mapped) ATP; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) mucosal inflammation and gut-microbiome (already mapped) dysbiosis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "DS copper: copper, via ceruloplasmin and SOD in intestinal epithelial cells (already mapped), counters oxidative injury; copper deficiency impairs gut-microbiome (already mapped) balance and amplifies NF-κB (already mapped) macrophage (already mapped) mucosal inflammation."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "DS sulfur: H2S from sulfur-amino acids in intestinal epithelial cells (already mapped) and macrophages (already mapped) promotes mucosal barrier integrity; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) gut-microbiome (already mapped) dysbiosis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "DS nitrogen: nitric oxide from iNOS in intestinal epithelial cells (already mapped) and macrophages (already mapped) maintains mucosal vasodilation; nitrogen deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) mucosal inflammation."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "DS oxygen: mitochondrial oxygen in intestinal epithelial cells (already mapped) and macrophages (already mapped) sustains ATP for mucosal repair; hypoxia amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade and gut-microbiome (already mapped) dysbiosis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "DS carbon: carbon backbone of amino acids in intestinal epithelial cells (already mapped) and hepatocytes (already mapped) fuels mucosal repair; carbon catabolites in gut-microbiome (already mapped) dysbiosis amplify NF-κB (already mapped) and IL-6 (already mapped) inflammation."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "DS hydrogen: hydrogen ions regulate pH in intestinal epithelial cells (already mapped) and macrophages (already mapped); proton gradient collapse from hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and gut-microbiome (already mapped) dysbiosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "DS VEGF: VEGF from macrophages (already mapped) and intestinal epithelial cells (already mapped) drives mucosal angiogenesis and repair; excess VEGF amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade and gut-microbiome (already mapped) dysbiosis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "DS pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses mucosal immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and gut-microbiome (already mapped) dysbiotic cascade in the digestive system."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "DS angiotensin-ii: angiotensin-II from macrophages (already mapped) and intestinal epithelial cells (already mapped) modulates gut vascular tone; angiotensin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and gut-microbiome (already mapped) dysbiosis."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "DS rankl: RANKL from macrophages (already mapped) and intestinal epithelial cells (already mapped) modulates mucosal immune-epithelial crosstalk; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and gut-microbiome (already mapped) dysbiosis."
taxonomy:
  uberon: "UBERON:0001007"
---

# Digestive System

## Overview

The digestive system transforms consumed food into molecular nutrients absorbable by the body — and safely expels indigestible residue as feces. It is among the body's most chemically complex systems, coordinating mechanical, enzymatic, hormonal, neural, microbial, and immunological processes across a ~9-meter length of specialized epithelium in adults [^openstax-anatomy-ch23].

The system consists of the **alimentary canal** (the gastrointestinal tract proper, from mouth to anus) and **accessory organs** that contribute secretions to the lumen without being physically continuous with it: the **liver** (bile production, nutrient processing), **gallbladder** (bile storage), **pancreas** (digestive enzymes + bicarbonate), and **salivary glands** (amylase, mucin, antimicrobials).

Three major dimensions of digestive physiology:

1. **Mechanical:** Mastication (teeth/jaw), deglutition (swallowing), peristalsis, segmentation, mixing, defecation — move and churn food to maximize contact with enzymes and absorptive surfaces.

2. **Chemical:** Salivary, gastric, pancreatic, and brush-border enzymes progressively reduce macromolecules to monomers: starch → glucose, proteins → amino acids, triglycerides → fatty acids + monoglycerides.

3. **Absorptive:** The small intestinal villus-crypt epithelium absorbs ~8–9 liters of fluid per day (diet + secretions), along with all major nutrients, vitamins (fat-soluble: A, D, E, K; water-soluble: C, B-complex, B₁₂ via intrinsic factor in terminal ileum), and minerals (iron in duodenum, Ca²⁺ in duodenum/proximal jejunum, Mg²⁺ in ileum).

The **enteric nervous system (ENS)** — containing ~100 million neurons embedded in the gut wall (more than the spinal cord) — provides semi-autonomous regulation of motility, secretion, and blood flow, earning it the nickname "the second brain" [^hall-guyton-14-gi].

## Structure

### The Alimentary Canal — Segment by Segment

**Oral Cavity:** Mastication (teeth), salivary amylase (starch digestion begins), lingual lipase, antimicrobial proteins (lysozyme, IgA). The bolus is propelled by voluntary deglutition through the pharynx → upper esophageal sphincter.

**Esophagus:** ~25 cm muscular tube, no digestion or absorption. Upper 1/3: striated muscle; lower 2/3: smooth muscle. Lower esophageal sphincter (LES) — prevents reflux; relaxes on swallowing. GERD = inappropriate LES relaxation → acid → esophageal injury.

**Stomach:**
| Region | Structure | Function |
|:---|:---|:---|
| Cardia | Mucous cells | Mucus secretion |
| Fundus/body | Parietal cells | HCl secretion (H⁺/K⁺-ATPase, proton pump); intrinsic factor |
| Fundus/body | Chief cells | Pepsinogen (activated to pepsin by HCl) |
| Pyloric antrum | G-cells | Gastrin release (stimulates parietal cells) |
| Pyloric antrum | D-cells | Somatostatin (inhibits G-cells, parietal cells) |

Gastric acid (pH 1.5–3.5): protein denaturation, pepsin activation, bactericidal. **Helicobacter pylori** disrupts mucous barrier → peptic ulcer. PPIs (omeprazole) block H⁺/K⁺-ATPase → acid suppression.

Volume: ~1 L capacity. Pylorus controls rate of gastric emptying → regulates nutrient delivery to duodenum.

**Small Intestine (~6–7 m: duodenum 25 cm, jejunum ~2.5 m, ileum ~3.5 m):**
The primary site of digestion and absorption. Surface area amplification:
- **Plicae circulares (valves of Kerckring):** circular mucosal folds — ×3 area increase
- **Villi:** finger-like projections (0.5–1.5 mm) — ×10 additional area
- **Microvilli (brush border):** 0.1 µm projections on each enterocyte — ×20 additional area
- **Total:** ×600 amplification → ~250 m² absorptive surface (size of a tennis court)

**Duodenum:** Receives gastric acid + chyme → CCK (from I-cells) → pancreatic enzyme release + bile delivery from common bile duct → emulsification + digestion. Secretin (from S-cells) → pancreatic HCO₃⁻ → pH neutralization. Iron (Fe²⁺), calcium, folate absorbed here.

**Jejunum:** Major site for absorption of monosaccharides (SGLT1, GLUT5), amino acids (multiple specific transporters), fatty acids and monoglycerides (passive, micelle-dependent), fat-soluble vitamins, most minerals.

**Ileum:** Terminal ileum specifically absorbs vitamin B₁₂ (cubilin/amnionless receptor) and reabsorbs bile salts (ASBT/SLC10A2, ~95% recovery — enterohepatic circulation). Ileocecal valve prevents backflow.

**Large Intestine (~1.5 m: cecum, colon, rectum):**
- Water and electrolyte reabsorption (~1.5 L/day → ~100 mL in feces)
- No enzymes; bacterially fermented fiber → short-chain fatty acids (butyrate, propionate, acetate) → colonocyte energy, microbiome support
- Mucus secretion (goblet cells)
- **Colonic microbiome:** ~10¹³ bacteria (comparable to human cell count), predominantly Firmicutes + Bacteroidetes; produce vitamin K₂, B vitamins; regulate immune maturation; disrupted microbiome (dysbiosis) → IBD, C. difficile infection, obesity, possibly colorectal cancer risk

**Rectum and Anus:** Storage and voluntary defecation. Internal anal sphincter (involuntary, smooth muscle) + external anal sphincter (voluntary, skeletal muscle, pudendal nerve S2-S4).

### Accessory Organs

**Liver (~1.5 kg):** See [Liver](../../06-organ/liver/README.md). Produces bile (500–1000 mL/day), processes all portal blood, detoxifies, synthesizes plasma proteins, regulates glucose/lipid metabolism.

**Gallbladder:** Pear-shaped, 7–10 cm, tucked in liver fossa. Concentrates bile 5–10× by absorbing water + Na⁺; stores until CCK-stimulated contraction propels it to duodenum. Biliary sludge → gallstones (calcium bilirubinate, cholesterol) → cholelithiasis.

**Pancreas:** Exocrine (95%): acinar cells secrete digestive enzymes (lipase, amylase, trypsinogen, chymotrypsinogen, elastase, colipase, phospholipase A2) + ductal cells secrete HCO₃⁻-rich fluid. Endocrine (5%): islets of Langerhans (α/β/δ cells → glucagon/insulin/somatostatin). Pancreatitis: autodigestion by prematurely activated enzymes.

**Salivary glands:** Parotid (serous, amylase-rich), submandibular, sublingual. ~1–1.5 L saliva/day. Antimicrobials (IgA, lysozyme, lactoferrin), mucin lubrication, pH buffering, taste.

### The Enteric Nervous System (ENS)

The ENS contains ~100 million neurons in two main plexuses:
- **Submucosal (Meissner's) plexus:** sensory + secretomotor control
- **Myenteric (Auerbach's) plexus:** coordinates motility (peristalsis, segmentation) by controlling longitudinal and circular smooth muscle

The ENS can function autonomously without extrinsic innervation (Hirschsprung's disease — absence of ENS ganglion cells in the distal colon → obstruction). Extrinsic modulation via vagal (parasympathetic, promotes motility/secretion) and sympathetic (reduces motility, vasoconstricts splanchnic vessels) input.

## Function

### Digestion

**Carbohydrates:** Salivary amylase (starch → maltose), gastric acid (inactivates amylase), pancreatic amylase (starch → disaccharides/oligosaccharides), brush-border disaccharidases (maltase, sucrase-isomaltase, lactase) → monosaccharides (glucose, fructose, galactose). Lactase deficiency → lactose intolerance (~70% of adult world population).

**Proteins:** Gastric pepsin (endopeptidase, active pH <4), pancreatic proteases (trypsin, chymotrypsin, elastase — activated by enteropeptidase in duodenum), brush-border and cytosolic peptidases → di/tripeptides → amino acids (absorbed via PepT1, PEPT2, specific AAs).

**Lipids:** Lingual/gastric lipase (~30% of triglyceride digestion), bile emulsification → mixed micelles, pancreatic lipase (+colipase) → fatty acids + monoglycerides → absorbed passively → re-esterified in enterocytes → chylomicrons → lymph (lacteals) → thoracic duct → subclavian vein.

### Absorption

| Nutrient | Primary site | Mechanism |
|:---|:---|:---|
| Glucose, galactose | Jejunum | SGLT1 (Na⁺-coupled active) |
| Fructose | Jejunum | GLUT5 (facilitated) |
| Amino acids | Jejunum | Na⁺-coupled + H⁺-coupled cotransporters |
| Long-chain fatty acids | Jejunum | Passive (micelle-dependent) |
| Medium-chain fatty acids | Jejunum | Portal vein directly (bypass lymph) |
| Iron (Fe²⁺) | Duodenum | DMT1; hepcidin regulates ferroportin export |
| Calcium | Duodenum/proximal jejunum | Transcellular (calcitriol-regulated, TRPV6) + paracellular |
| Vitamin B₁₂ | Terminal ileum | IF-B₁₂ complex → cubilin receptor |
| Bile salts | Terminal ileum | ASBT active reabsorption |
| Water | Jejunum > ileum > colon | Osmotic, following solute absorption |

### GI Hormones

| Hormone | Cell | Stimulus | Effect |
|:---|:---|:---|:---|
| Gastrin (CCK-like) | G-cells (antrum) | Protein, distension | ↑ HCl, ↑ pepsinogen, ↑ gastric motility |
| CCK | I-cells (duodenum/jejunum) | Fat, protein | ↑ Pancreatic enzymes, ↑ bile release (gallbladder), ↑ Oddi relaxation; satiety |
| Secretin | S-cells (duodenum) | Acid | ↑ Pancreatic HCO₃⁻, ↑ biliary HCO₃⁻, ↓ gastric acid |
| GIP | K-cells (duodenum) | Glucose, fat | Incretins: ↑ insulin (glucose-dependent) |
| GLP-1 | L-cells (ileum/colon) | Carbohydrate, fat, protein | Strong incretin, ↓ glucagon, satiety, ↓ gastric emptying (target of GLP-1 RAs: semaglutide) |
| Motilin | Mo-cells (duodenum) | Fasting (every 90 min) | Migrating motor complex (MMC) — cleares stomach/SI between meals |
| Somatostatin | D-cells (stomach, pancreas) | Multiple | Broad inhibitory: ↓ gastrin, ↓ insulin, ↓ glucagon, ↓ gut motility |

## Connections

- **Part of:** [Human Body](../../08-whole-body/human-body/README.md) — one of the major organ systems.
- **Contains:** [Liver](../../06-organ/liver/README.md) — the dominant accessory organ.
- **Contains:** [Hepatocyte](../../04-cellular/hepatocyte/README.md) — the liver parenchymal cell.
- **Connects to:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — portal blood flow; lipid entry via thoracic duct; splanchnic vasculature (~25% of CO).
- **Connects to:** [Renal System](../renal-system/README.md) — fluid and electrolyte balance shared between GI absorption and renal excretion; GI fluid losses cause prerenal AKI.
- **Damaged by:** SARS-CoV-2 — GI manifestations (diarrhea, nausea, anorexia), liver injury via ACE2 in enterocytes/cholangiocytes.
- **Damaged by:** Mycobacterium tuberculosis — GI TB (ileocecal most common), peritoneal TB.
- **Connects to:** [Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md) — peristalsis: waves of smooth-muscle contraction from esophagus to colon, coordinated by the enteric nervous system; motility disorders when it fails.
- **Connects to:** [Iron](../../02-atomic/iron/README.md) — the duodenum is the body's gateway for dietary iron; malabsorption or chronic GI bleeding here drives iron-deficiency anemia.
- **Connects to:** [Photon](../../01-subatomic/photon/README.md) — explored with light and radiation: endoscopy shines visible light into the lumen, while X-ray photons in barium studies and CT trace structure.
- **Connects to:** [Electron](../../01-subatomic/electron/README.md) — electron microscopy reveals how the gut absorbs so much: each enterocyte is crowned with a brush border of densely packed microvilli that multiplies the absorptive surface, the ultrastructure behind nutrient uptake.
- **Connects to:** [Sodium](../../02-atomic/sodium/README.md) — sodium powers digestion's uptake: the sodium gradient set by membrane pumps drives the cotransporters that haul glucose, amino acids, and water across the gut lining — the principle behind oral rehydration therapy.
- **Connects to:** [Hepatocyte](../../04-cellular/hepatocyte/README.md) — the hepatocyte is the digestive system's chemical plant: it makes the bile that emulsifies fat and receives the nutrient-rich portal blood from the gut, processing and storing what the intestine absorbs.
- **Connects to:** [Nervous System](../nervous-system/README.md) — the gut runs its own brain: the enteric nervous system, ~500 million neurons in the bowel wall, drives peristalsis and secretion largely autonomously, while the vagus-linked gut-brain axis ties digestion to mood and appetite.
- **Connects to:** [Immune System](../immune-system/README.md) — most of the body's immune cells guard the gut: gut-associated lymphoid tissue (Peyer's patches, lamina propria) polices the vast luminal antigen load, tolerating food and flora while repelling pathogens across a single-cell barrier.
- **Connects to:** [Gut Microbiome](../gut-microbiome/README.md) — the digestive tract houses an organ of microbes: trillions of gut bacteria ferment fiber into short-chain fatty acids, synthesize vitamins, train immunity, and shape motility — a metabolic partner the system feeds and depends on.
- **Connects to:** [Antibody](../../03-molecular/antibody/README.md) — the gut is the body's largest antibody factory: plasma cells in the lamina propria pump out secretory IgA that bathes the mucosa, neutralizing pathogens and shaping the flora while teaching tolerance to food and friendly microbes.
- **Connects to:** [Endocrine System](../endocrine-system/README.md) — the gut is also the largest endocrine organ: scattered enteroendocrine cells release ghrelin, CCK, secretin, gastrin, and GLP-1 that pace digestion and signal hunger and fullness to the brain, the gut-hormone arm of metabolism.
- **Connects to:** [Macrophage](../../04-cellular/macrophage/README.md) — a vast, restrained macrophage army lines the gut: the largest pool of macrophages in the body clears the trickle of bacteria crossing the barrier yet stays tolerant, and when that balance breaks, inflammatory bowel disease follows.
- **Connects to:** [Neuron](../../04-cellular/neuron/README.md) — the gut runs its own nervous system: the enteric nervous system, a mesh of millions of neurons in the bowel wall, coordinates peristalsis and secretion largely on its own, earning the gut its name as the body's second brain.
- **Connects to:** [GLP-1](../../03-molecular/glp-1/README.md) — the gut is an endocrine organ: L-cells release GLP-1 after a meal to spur insulin, slow gastric emptying and curb appetite, the incretin axis now harnessed by the blockbuster GLP-1 weight and diabetes drugs.
- **Connects to:** [Reproductive System](../reproductive-system/README.md) — gut microbes help set circulating estrogen: the estrobolome — bacterial enzymes that deconjugate estrogens for reabsorption — links the digestive tract to reproductive and hormonal health across the body.
- **Connects to:** [Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md) — when gut tolerance breaks, the wall inflames: inflammatory bowel disease is the digestive system turning on itself, as a misfired immune response to the microbiome ulcerates the bowel — the chronic counterpart to the gut's normal restraint.
- **Connects to:** [Dendritic Cell](../../04-cellular/dendritic-cell/README.md) — the gut decides friend from foe through dendritic cells: they reach between epithelial cells to sample luminal antigens, then teach tolerance to food and flora or mount defense against pathogens — the gatekeepers of intestinal immunity.
- **Connects to:** [Histamine](../../03-molecular/histamine/README.md) — histamine drives the stomach's acid: enterochromaffin-like cells release it to stimulate parietal-cell acid secretion through H2 receptors, the pathway that H2-blockers shut down to treat ulcers and reflux.
- **Connects to:** [Colorectal Cancer](../colorectal-cancer/README.md) — its most common cancer grows from the lining: colorectal cancer arises from the glandular epithelium of the large bowel, the digestive system's leading malignancy and the reason colonoscopy screens the tract for precancerous polyps.
- **Connects to:** [Gastric Cancer](../gastric-cancer/README.md) — chronic injury to the stomach turns malignant: gastric cancer develops from the gastric mucosa after years of H. pylori infection, inflammation and atrophy, a digestive-tract cancer still common worldwide.
- **Connects to:** [Pancreatic Cancer](../pancreatic-cancer/README.md) — an accessory organ harbors a lethal cancer: pancreatic adenocarcinoma arises from the ductal cells of the pancreas, a digestive gland, and its silent deep location makes it one of the deadliest cancers of the system.
- **Connects to:** [Cholangiocarcinoma](../cholangiocarcinoma/README.md) — its biliary tree can turn malignant: cholangiocarcinoma arises in the bile ducts that drain the liver into the gut, a hepatobiliary cancer of the digestive system often linked to chronic inflammation of the ducts.
- **Connects to:** [NASH](../nash/README.md) — the liver fattens and inflames: NASH is the inflammatory fatty-liver disease of the digestive system's largest gland, driven by metabolic excess and progressing toward cirrhosis and liver cancer.
- **Connects to:** [Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md) — a commensal yeast can turn invader: Candida normally lives quietly in the gut, but disrupted flora or immunity let it overgrow into oral and esophageal candidiasis along the upper digestive tract.
- **Connects to:** [Major Depressive Disorder](../major-depressive-disorder/README.md) — gut and brain talk constantly: most of the body's serotonin is made in the gut and the microbiome signals along the gut-brain axis, so digestive function and mood are tightly linked in both directions.
- **Connects to:** [Type 2 Diabetes](../type-2-diabetes/README.md) — the gut sets the metabolic tone: intestinal incretin hormones like GLP-1, nutrient absorption and the microbiome shape insulin secretion and resistance, placing the digestive system at the heart of type 2 diabetes.
- **Connects to:** [Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md) — it both absorbs iron and loses it: the gut is the sole site of iron uptake, so malabsorption or chronic bleeding from ulcers, tumors or inflammation along the tract is a leading cause of iron-deficiency anemia.
- **Connects to:** [Lymphatic System](../lymphatic-system/README.md) — the gut is the body's largest immune and lymphatic organ: gut-associated lymphoid tissue and Peyer's patches guard the lumen, while intestinal lacteals absorb dietary fat into the lymphatics as chyle.
- **Connects to:** [Respiratory System](../respiratory-system/README.md) — they share an origin and a crossroads: the gut and airways arise from the same primitive foregut and meet at the pharynx, so swallowing disorders cause aspiration and a gut-lung axis links the two.
- **Connects to:** [Integumentary System](../integumentary-system/README.md) — the gut shows on the skin: malabsorption produces hair, nail and skin changes, liver disease causes jaundice, and a gut-skin axis links conditions like coeliac disease to dermatitis herpetiformis.
- **Connects to:** [Musculoskeletal System](../musculoskeletal-system/README.md) — the gut feeds the skeleton: it absorbs the calcium and vitamin D that build bone, so malabsorption from coeliac or bowel disease causes osteoporosis and osteomalacia, while inflammatory bowel disease brings enteropathic arthritis.
- **Connects to:** [Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md) — a virus that smoulders in the liver: hepatitis C establishes chronic infection of hepatocytes, driving cirrhosis and hepatocellular carcinoma, though direct-acting antivirals now cure most cases.
- **Connects to:** [Zinc (Dietary)](../../../03-medicine/03-food/zinc-dietary/README.md) — zinc and the gut depend on each other: zinc is absorbed in the small intestine and maintains mucosal integrity, so malabsorption causes deficiency with diarrhoea and acrodermatitis, and supplementation shortens acute diarrhoea.
- **Connects to:** [Omeprazole](../../../03-medicine/01-modern/08-gi/omeprazole/README.md) — a drug that quietens the stomach: proton pump inhibitors like omeprazole suppress gastric acid to heal ulcers and reflux, but long-term use can impair absorption of B12, iron, calcium and magnesium and alter the gut microbiome.
- **Connects to:** [Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md) — a common painkiller that ulcerates it: NSAIDs like ibuprofen block the prostaglandins that protect the gastric lining, causing peptic ulcers and gastrointestinal bleeding.
- **Connects to:** [Curcumin](../../../03-medicine/03-food/curcumin/README.md) — a spice studied for the gut: curcumin from turmeric has anti-inflammatory effects investigated in inflammatory bowel disease, though its poor absorption limits how much reaches the bloodstream.
- **Connects to:** [Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md) — dietary fats shape gut health: long-chain omega-3 fatty acids, absorbed via intestinal lacteals, have anti-inflammatory effects studied in inflammatory bowel disease and the gut-liver axis.
- **Connects to:** [Coxsackievirus B](../../../02-pathogen/01-viruses/coxsackievirus-b/README.md) — enteroviruses pass through the gut: Coxsackie and other enteroviruses are swallowed and replicate in the intestinal lining, causing herpangina and hand-foot-and-mouth disease before systemic spread.
- **Connects to:** [Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md) — the gut handles magnesium two ways: the intestine absorbs dietary magnesium, and poorly absorbed magnesium salts act as osmotic laxatives, while malabsorption causes deficiency.
- **Connects to:** [Esophageal Cancer](../esophageal-cancer/README.md) — it begins at the top of the tract: esophageal cancer — squamous from smoking and alcohol, adenocarcinoma from reflux and Barrett's — completes the digestive tract's malignancies alongside gastric, colorectal and pancreatic cancer.
- **Connects to:** [Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md) — the liver is its chemical factory: the hepatic lobule, the liver's functional unit, processes everything absorbed from the gut via the portal vein, secretes bile for fat digestion, and detoxifies and stores the nutrients the gut delivers.
- **Connects to:** [Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md) — it both treats and is harmed: the gut's common cancers depend on cytotoxic chemotherapy, while the rapidly dividing intestinal lining makes the digestive tract a prime victim of chemo, producing the mucositis, nausea and diarrhoea that limit dosing.
- **Connects to:** [Peyer's Patches](../../05-tissue/peyers-patches/README.md) — the gut's immune sentinels: Peyer's patches in the small-intestinal wall sample luminal antigens through M cells, the gut-associated lymphoid tissue where the digestive and immune systems meet.
- **Connects to:** [Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md) — the endocrine pancreas within the gut: the islets of Langerhans, embedded in the digestive organ that also makes digestive enzymes, secrete insulin and glucagon to regulate the metabolism of absorbed nutrients.
- **Connects to:** [GIST](../gist/README.md) — its commonest mesenchymal tumour: gastrointestinal stromal tumours arise from the interstitial cells of Cajal—the gut's pacemaker cells—anywhere from oesophagus to rectum, distinct from the epithelial carcinomas of the digestive tract.
- **Connects to:** [HCC](../hcc/README.md) — cancer of the digestive system's largest organ: hepatocellular carcinoma arises in the chronically injured liver—from viral hepatitis, alcohol or fatty liver—the dominant primary cancer of the gut's metabolic powerhouse.
- **Connects to:** [Obesity](../obesity/README.md) — the metabolic burden on the gut: obesity reshapes bile acids and the microbiome and drives fatty liver, gallstones, reflux and colorectal cancer, tying excess adiposity to disease across the digestive tract.
- **Connects to:** [Spleen](../../06-organ/spleen/README.md) — the portal partner: the spleen drains into the portal vein, so cirrhosis and portal hypertension cause congestive splenomegaly and hypersplenism—linking digestive disease to sequestration of blood cells.
- **Connects to:** [Parkinson's Disease](../parkinsons-disease/README.md) — the gut-brain axis: Parkinson's may begin in the enteric nervous system, with alpha-synuclein aggregating in the gut wall and ascending the vagus nerve, and constipation often precedes the motor disease by years.
- **Connects to:** [Hereditary Pancreatitis](../hereditary-pancreatitis/README.md) — recurrent pancreatic injury: hereditary pancreatitis (PRSS1) causes repeated attacks of pancreatitis in the digestive system's exocrine pancreas, leading to chronic pancreatitis and a high lifetime pancreatic-cancer risk.
- **Connects to:** [Type 1 Diabetes](../type-1-diabetes/README.md) — two roles for one organ: the pancreas is both a digestive (exocrine) and endocrine gland, and type 1 diabetes destroys its islets of Langerhans, the endocrine cells embedded within this digestive organ.
- **Connects to:** [Acetylcholine](../../03-molecular/acetylcholine/README.md) — parasympathetic drive: acetylcholine is the principal enteric and vagal neurotransmitter stimulating gut motility, secretion and sphincter function throughout the digestive tract.
- **Connects to:** [Nitric Oxide](../../03-molecular/nitric-oxide/README.md) — inhibitory neurotransmission: nitric oxide from enteric inhibitory neurons relaxes gut smooth muscle for peristalsis and sphincter opening, with its loss causing achalasia and pyloric stenosis.
- **Connects to:** [Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md) — toxin food poisoning: preformed staphylococcal enterotoxin causes rapid-onset vomiting and diarrhoea, a classic toxin-mediated gastroenteritis of the digestive tract.
- **Connects to:** [Secretory IgA](../../03-molecular/secretory-iga/README.md) — mucosal defence: dimeric secretory IgA transcytosed across gut epithelium coats luminal microbes and toxins, shaping the microbiota and protecting the digestive mucosal surface from invasion.
- **Connects to:** [Leptin](../../03-molecular/leptin/README.md) — satiety signalling: leptin from adipose and gastric chief cells acts on the gut-brain axis and enteric neurons to curb appetite and modulate motility, linking digestion to energy balance.
- **Connects to:** [TGF-beta](../../03-molecular/tgf-beta/README.md) — barrier homeostasis: TGF-beta drives intestinal epithelial repair and oral tolerance, inducing regulatory T cells that restrain immune responses to food antigens and commensal flora in the gut.
- **Connects to:** [Prostaglandins](../../03-molecular/prostaglandins/README.md) — mucosal cytoprotection: prostaglandins (PGE2) maintain the gastric mucus-bicarbonate barrier and mucosal blood flow, which is why NSAIDs that block their synthesis predispose to gastric and duodenal ulcers.
- **Connects to:** [Substance P](../../03-molecular/substance-p/README.md) — enteric peristalsis: substance P from enteric neurons is an excitatory tachykinin that contracts gut smooth muscle, helping coordinate the peristaltic reflex that propels contents through the digestive tract.
- **Connects to:** [CGRP](../../03-molecular/cgrp/README.md) — sensory gastroprotection: CGRP released from gut sensory afferents increases mucosal blood flow and defends the stomach lining against acid and injury, a neural protective reflex of the gastrointestinal mucosa.
- **Connects to:** [SSTR2](../../03-molecular/sstr2/README.md) — universal inhibitory hormone: somatostatin from gut D cells acts through SSTR2 to brake acid secretion, gastrin release and motility, the master off-switch of the gastrointestinal tract exploited therapeutically by octreotide in bleeding and secretory diarrhea.
- **Connects to:** [Cholesterol](../../03-molecular/cholesterol/README.md) — bile-acid digestion: the liver converts cholesterol into bile acids that emulsify dietary fat into micelles for pancreatic-lipase digestion and absorption, then recovers them through the enterohepatic circulation, the GI tract's fat-handling system.
- **Connects to:** [Aldosterone](../../03-molecular/aldosterone/README.md) — colonic fluid recovery: aldosterone drives sodium and water reabsorption across the distal colonic epithelium, the final electrolyte- and fluid-conserving step of the gastrointestinal tract that hardens stool and prevents dehydration.
- **Connects to:** [Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md) — crypt stem-cell renewal: Wnt/β-catenin signaling from the intestinal crypt base drives the continuous self-renewal of the gut epithelium, the most rapidly regenerating tissue in the body and the basis of digestive-tract homeostasis.
- **Connects to:** [NOTCH](../../03-molecular/notch/README.md) — cell-fate patterning: NOTCH signaling sets the choice between absorptive enterocytes and secretory (goblet, enteroendocrine, Paneth) cells in the intestinal epithelium, patterning the functional surface of the digestive lining.
- **Connects to:** [Interleukin-10](../../03-molecular/il-10/README.md) — microbiota tolerance: regulatory IL-10 maintains immune tolerance to the gut microbiota, and its loss breaks digestive-tract homeostasis to drive the intestinal inflammation of inflammatory bowel disease.
- **Connects to:** [EGFR](../../03-molecular/egfr/README.md) — epithelial renewal: EGF-family signaling drives the continuous renewal of the gut epithelium from Wnt-driven crypt stem cells (Wnt mapped), maintaining the rapidly turning-over digestive lining.
- **Connects to:** [Mu-Opioid Receptor](../../03-molecular/mu-opioid-receptor/README.md) — enteric motility: μ-opioid receptors on enteric neurons slow gut motility and secretion, the basis of opioid-induced constipation and a node of the enteric nervous control of digestion.
- **Connects to:** [TLR4](../../03-molecular/tlr4/README.md) — microbiota sensing: intestinal epithelial TLR4 senses the gut microbiota, calibrating the mucosal immune tolerance (with secretory-IgA and IL-10 mapped) that maintains digestive homeostasis.
- **Connects to:** [MYD88](../../03-molecular/myd88/README.md) — microbiota signal transduction: epithelial and immune TLR signaling through MyD88 (TLR4 already mapped) transduces gut-microbiota cues into the mucosal homeostasis and barrier defense of the digestive tract.
- **Connects to:** [mTOR](../../03-molecular/mtor/README.md) — crypt nutrient sensing: mTOR nutrient-sensing in intestinal crypt stem cells couples luminal nutrient availability to the continuous epithelial renewal of the gut lining.
- **Connects to:** [NF-κB](../../03-molecular/nf-kb/README.md) — mucosal inflammatory balance: NF-κB signaling in the intestinal epithelium balances antimicrobial defense against tolerance, governing the inflammatory homeostasis of the gut mucosa.
- **Connects to:** [Galectin-3](../../03-molecular/galectin-3/README.md) — mucosal immunity and repair: galectin-3 modulates mucosal immunity and epithelial repair in the gut and contributes to the fibrosis that follows chronic intestinal inflammation.
- **Connects to:** [cGAS-STING](../../03-molecular/cgas-sting/README.md) — DNA-sensing in the mucosa: cytosolic DNA sensing through cGAS-STING links microbial and damage-associated DNA to the inflammatory tone of the gut.
- **Connects to:** [HIF-1alpha](../../03-molecular/hif-1alpha/README.md) — physiological gut hypoxia: HIF-1α responds to the steep oxygen gradient of the gut lumen and supports the barrier function and metabolism of the intestinal epithelium.
- **Connects to:** [SMAD4](../../03-molecular/smad4/README.md) — epithelial homeostasis and fibrosis: TGF-β-SMAD signaling (TGF-β already mapped) governs epithelial homeostasis, mucosal fibrosis, and the regulatory immune tone of the digestive tract.
- **Connects to:** [STAT3](../../03-molecular/stat3/README.md) — mucosal regeneration: IL-6-STAT3 signaling drives the epithelial regeneration and mucosal inflammatory tone of the gastrointestinal tract.
- **Connects to:** [FOXO](../../03-molecular/foxo/README.md) — epithelial stem-cell homeostasis: FOXO transcription factors regulate intestinal stem-cell homeostasis and the metabolic and oxidative-stress responses of the gut epithelium.
- **Connects to:** [AKT](../../03-molecular/akt/README.md) — epithelial renewal: PI3K-AKT signaling governs the proliferation and survival of the rapidly renewing intestinal epithelium of the digestive system.
- **Connects to:** [ERK1/2](../../03-molecular/erk1-2/README.md) — growth-factor signaling: ERK-MAPK signaling downstream of growth-factor and hormone receptors drives the epithelial renewal and secretory responses of the digestive system.
- **Connects to:** [GSK-3β](../../03-molecular/gsk-3b/README.md) — crypt stem-cell renewal: GSK-3β, within the Wnt destruction complex (Wnt already mapped), governs the crypt stem-cell renewal of the intestinal epithelium of the digestive system.
- **Connects to:** [PIK3CA](../../03-molecular/pik3ca/README.md) — epithelial proliferation: PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the epithelial proliferation and renewal of the gastrointestinal mucosa of the digestive system.
- **Connects to:** [AMPK](../../03-molecular/ampk/README.md) — nutrient sensing: AMPK integrates the nutrient and energy status of the enterocytes and hepatocytes of the digestive system.
- **Connects to:** [STAT1](../../03-molecular/stat1/README.md) — mucosal immunity: IFN-STAT1 signaling shapes the mucosal immune surveillance of the digestive system.
- **Connects to:** [Autophagy](../../03-molecular/autophagy/README.md) — epithelial homeostasis: Autophagy maintains the epithelial homeostasis, Paneth-cell function, and mucosal barrier of the digestive system.
- **Connects to:** [SRC Kinase](../../03-molecular/src-kinase/README.md) — junction dynamics: SRC-family kinase signaling participates in the epithelial junction dynamics and growth-factor responses of the digestive system.
- **Connects to:** [DNMT3A](../../03-molecular/dnmt3a/README.md) — epigenetic renewal: DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the epithelial renewal and immune tolerance of the digestive system.
- **Connects to:** [CCR5](../../03-molecular/ccr5/README.md) — mucosal trafficking: CCR5-driven chemokine signaling participates in the mucosal immune trafficking of the digestive system.
- **Connects to:** [CXCL12](../../03-molecular/cxcl12/README.md) — epithelial-stromal crosstalk: CXCL12-CXCR4 signaling participates in the epithelial-stromal and immune interactions of the digestive system.
- **Connects to:** [Interleukin-6](../../03-molecular/il-6/README.md) — mucosal regeneration: IL-6 signaling participates in the mucosal immune and epithelial-regeneration processes of the digestive system.
- **Connects to:** [Proton](../../01-subatomic/proton/README.md) — gastric acid: parietal cells secrete hydrochloric acid by pumping protons through the H+/K+ ATPase, the target of proton-pump inhibitors, creating the acidic lumen that activates pepsin and provides a barrier against ingested microbes.
- **Connects to:** [Calcium](../../02-atomic/calcium/README.md) — mineral absorption: the small intestine absorbs dietary calcium under vitamin D control, so the digestive tract governs the calcium supply for bone and neuromuscular function and becomes a source of deficiency when absorption fails.
- **Connects to:** [Melatonin](../../03-molecular/melatonin/README.md) — enteric melatonin: the gut's enterochromaffin cells produce far more melatonin than the pineal gland, where it regulates intestinal motility and provides mucosal antioxidant protection, an under-recognised digestive-system endocrine function.
- **Connects to:** [Dopamine](../../03-molecular/dopamine/README.md) — enteric dopamine: the gut contains large amounts of dopamine that modulates motility and secretion, and dopamine-receptor drugs (prokinetics like metoclopramide, antiemetics) act on this enteric dopaminergic system of the digestive tract.
- **Connects to:** [Potassium](../../02-atomic/potassium/README.md) — colonic potassium: the colon secretes and absorbs potassium under aldosterone control (aldosterone already mapped), an electrolyte-handling role of the digestive tract that becomes clinically important in diarrhoea and renal failure.
- **Connects to:** [BDNF](../../03-molecular/bdnf/README.md) — enteric nervous system: BDNF and neurotrophic signalling support the enteric nervous system, the gut's intrinsic 'second brain' of over a hundred million neurons that coordinates the motility and secretion of the digestive system.
- **Connects to:** [Zinc](../../02-atomic/zinc/README.md) — zinc absorption: the small intestine absorbs dietary zinc, essential for the many digestive enzymes and for mucosal integrity and taste, and malabsorption causes the dermatitis and diarrhoea of zinc deficiency.
- **Connects to:** [Mast cell](../../04-cellular/mast-cell/README.md) — mucosal mast cells: mast cells in the gut wall (histamine already mapped) defend the mucosa and, when dysregulated, contribute to the visceral hypersensitivity and altered motility of functional gastrointestinal disorders.
- **Connects to:** [Chloride](../../02-atomic/chloride/README.md) — secretory chloride: chloride secretion by the intestinal epithelium drives the fluid that lubricates digestion, and its dysregulation underlies the secretory diarrhoea of infections and the defect of cystic fibrosis.
- **Connects to:** [Nervous system](../nervous-system/README.md) — the gut-brain axis: the enteric nervous system and the vagal and serotonergic signalling (serotonin, dopamine and BDNF already mapped) link the digestive system to the nervous system, coordinating motility, secretion and appetite.
- **Connects to:** [Sodium](../../02-atomic/sodium/README.md) — sodium-coupled absorption: sodium gradients power the absorption of glucose and amino acids across the intestinal epithelium, and sodium handling (chloride already mapped) governs the fluid balance of the digestive tract.
- **Connects to:** [Macrophage](../../04-cellular/macrophage/README.md) — gut mucosal macrophages: the macrophages of the gut wall and the Kupffer cells of the liver sample the luminal contents and maintain tolerance (secretory IgA already mapped), a large part of the body's immune tissue serving the digestive system.
- **Connects to:** [Magnesium](../../02-atomic/magnesium/README.md) — magnesium absorption: the small intestine of the digestive system absorbs dietary magnesium, and the malabsorption of gut disease (or proton-pump inhibitors) causes the hypomagnesaemia of digestive disorders.
- **Connects to:** [TNF-alpha](../../03-molecular/tnf-alpha/README.md) — gut inflammation: TNF from the gut-associated lymphoid tissue (IL-6 and IL-10 already mapped) is a central mediator of the inflammation of the digestive tract, the target of anti-TNF therapy in inflammatory bowel disease.
- **Connects to:** [IL-17a](../../03-molecular/il-17a/README.md) — mucosal Th17 defence: IL-17 from the gut mucosal Th17 cells defends the epithelial barrier of the digestive system against invading microbes, and its dysregulation drives the inflammation of gut immune disease.
- **Connects to:** [Adiponectin](../../03-molecular/adiponectin/README.md) — metabolic adipokine: adiponectin, with leptin (already mapped), is the adipokine signalling that links the digestive system's nutrient handling to the whole-body energy and metabolic balance.
- **Connects to:** [Resistin](../../03-molecular/resistin/README.md) — adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the visceral adipose and the digestive-system nutrient handling to the metabolic-inflammatory state.
- **Connects to:** [Plasma cell](../../04-cellular/plasma-cell/README.md) — gut IgA plasma cells: the intestinal plasma cells — the largest plasma-cell pool in the body — secrete the secretory IgA (already mapped) that defends the mucosal barrier of the digestive system.
- **Connects to:** [B cell](../../04-cellular/b-cell/README.md) — GALT B cells: the gut-associated lymphoid tissue B cells class-switch to the IgA (secretory-IgA already mapped) and populate the plasma-cell (already mapped) pool of the digestive-system mucosal immunity.
- **Connects to:** [Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md) — oral tolerance: the intestinal regulatory T cells maintain the tolerance to the food antigens and the commensal microbiome (gut-microbiome already mapped) of the digestive system.
- **Connects to:** [T-helper cell](../../04-cellular/t-helper-cell/README.md) — gut adaptive immunity: the CD4 T-helper cells of the gut-associated lymphoid tissue coordinate the mucosal immune response and the barrier defence of the digestive system.
- **Connects to:** [IL-4](../../03-molecular/il-4/README.md) — type-2 mucosal immunity: IL-4, a type-2 cytokine, drives the anti-helminth and the goblet-cell/mucus response of the gut mucosal immunity of the digestive system.
- **Connects to:** [IL-13](../../03-molecular/il-13/README.md) — type-2 barrier: IL-13, with IL-4 (already mapped), drives the goblet-cell mucus and the epithelial-barrier type-2 response of the digestive system.
- **Connects to:** [IL-5](../../03-molecular/il-5/README.md) — eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), recruits the gut eosinophils of the anti-parasite type-2 immunity of the digestive system.
- **Connects to:** [IL-23](../../03-molecular/il-23/README.md) — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the mucosal barrier defence and the inflammatory tone of the gut of the digestive system.
- **Connects to:** [IgE](../../03-molecular/ige/README.md) — type-2/allergy arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), is the antibody arm of the anti-parasite and food-allergy type-2 immunity of the digestive system.
- **Connects to:** [IL-33](../../03-molecular/il-33/README.md) — epithelial alarmin: IL-33, released by the injured gut epithelium, activates the ILC2s and initiates the type-2 (IL-4, IL-5 and IL-13 already mapped) mucosal immunity of the digestive system.
- **Connects to:** [Complement C3](../../03-molecular/complement-c3/README.md) — mucosal complement: the complement C3, produced locally and from the liver (already mapped), opsonises the gut microbes and is part of the innate mucosal defence of the digestive system.
- **Connects to:** [C5aR1](../../03-molecular/c5ar1/README.md) — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the neutrophil recruitment into the intestinal mucosa during the innate immune response of the digestive system.
- **Connects to:** [Neutrophil](../../04-cellular/neutrophil/README.md) — mucosal neutrophils: the neutrophils are recruited into the intestinal mucosa and lumen as the innate effectors of the antimicrobial defence of the digestive system.
- **Connects to:** [TSLP](../../03-molecular/tslp/README.md) — epithelial alarmin: TSLP, secreted by intestinal epithelial cells under microbial and mechanical stress, polarises dendritic cells (already mapped) toward Th2 tolerance and tunes the mucosal immune set-point of the digestive system.
- **Connects to:** [Erythropoietin](../../03-molecular/erythropoietin/README.md) — gut EPO axis: erythropoietin, produced by intestinal epithelium under hypoxic stress, supports epithelial repair, modulates enteric immune tone, and links gut oxygenation to the systemic haematopoietic response of the digestive system.
- **Connects to:** [Complement C5](../../03-molecular/complement-c5/README.md) — terminal complement gateway: complement C5 cleavage in the intestinal lamina propria generates C5a (signalling via C5aR1 already mapped) and C5b-9 MAC, amplifying inflammatory and tissue-remodelling responses of the digestive system.
- **Connects to:** [Bradykinin](../../03-molecular/bradykinin/README.md) — kinin mediator: bradykinin, generated by kallikrein activation in the intestinal mucosa during injury and inflammation, amplifies vascular permeability, smooth-muscle contraction (already mapped) and nociceptive signalling of the digestive system.
- **Connects to:** [C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md) — contact/complement regulator: the C1-esterase inhibitor regulates the classical complement and contact-kinin (bradykinin and kallikrein) pathways activated in the intestinal mucosa, moderating the inflammatory cascade of the digestive system.
- **Connects to:** [Periostin](../../03-molecular/periostin/README.md) — stromal ECM scaffold: periostin, secreted by subepithelial fibroblasts (already mapped) of the intestinal crypt niche, maintains the basement-membrane integrity and supports epithelial regeneration and stem-cell quiescence of the digestive system.
- **Connects to:** [Testosterone](../../03-molecular/testosterone/README.md) — DS testosterone: testosterone modulates liver (already mapped) bile metabolism and smooth-muscle-cell (already mapped) motility in the gut; androgen signalling shapes the gut microbiome (already mapped) composition and the IL-6 (already mapped) intestinal inflammatory tone.
- **Connects to:** [Prolactin](../../03-molecular/prolactin/README.md) — DS prolactin: prolactin receptors on intestinal epithelium (already mapped) promote mucosal cell proliferation; prolactin also stimulates pancreatic (already mapped) enzyme secretion and modulates the gut-microbiome (already mapped) composition via immune crosstalk.
- **Connects to:** [Oxytocin](../../03-molecular/oxytocin/README.md) — DS oxytocin: oxytocin regulates gut motility by modulating smooth-muscle-cell (already mapped) contractility and the enteric nervous system; oxytocin also enhances intestinal epithelium (already mapped) barrier integrity and the gut-microbiome (already mapped) microbial balance.
- **Connects to:** [Vasopressin](../../03-molecular/vasopressin/README.md) — DS vasopressin: vasopressin (ADH) regulates intestinal water absorption via V2/aquaporin-2 in the intestinal epithelium (already mapped); AVP-driven cAMP pathway modulates gut-microbiome (already mapped) colonisation resistance and NF-κB (already mapped) mucosal immunity.
- **Connects to:** [Selenium](../../02-atomic/selenium/README.md) — DS selenium: selenoproteins in the intestinal epithelium (already mapped) counter NF-κB (already mapped) oxidative stress; selenium deficiency impairs gut-microbiome (already mapped) diversity and amplifies macrophage (already mapped) mediated mucosal inflammation.
- **Connects to:** [Iodine](../../02-atomic/iodine/README.md) — DS iodine: intestinal lactoperoxidase (iodine-dependent) in the epithelium (already mapped) limits pathogen colonisation; iodine deficiency amplifies NF-κB (already mapped) driven gut-microbiome (already mapped) dysbiosis and impairs macrophage (already mapped) mucosal defence.
- **Connects to:** [Phosphorus](../../02-atomic/phosphorus/README.md) — DS phosphorus: phosphorus fuels epithelial-cell (already mapped) and macrophage (already mapped) ATP; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) mucosal inflammation and gut-microbiome (already mapped) dysbiosis.
- **Connects to:** [Copper](../../02-atomic/copper/README.md) — DS copper: copper, via ceruloplasmin and SOD in intestinal epithelial cells (already mapped), counters oxidative injury; copper deficiency impairs gut-microbiome (already mapped) balance and amplifies NF-κB (already mapped) macrophage (already mapped) mucosal inflammation.
- **Connects to:** [Sulfur](../../02-atomic/sulfur/README.md) — DS sulfur: H2S from sulfur-amino acids in intestinal epithelial cells (already mapped) and macrophages (already mapped) promotes mucosal barrier integrity; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) gut-microbiome (already mapped) dysbiosis.
- **Connects to:** [Nitrogen](../../02-atomic/nitrogen/README.md) — DS nitrogen: nitric oxide from iNOS in intestinal epithelial cells (already mapped) and macrophages (already mapped) maintains mucosal vasodilation; nitrogen deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped) and IL-6 (already mapped) mucosal inflammation.
- **Connects to:** [Oxygen](../../02-atomic/oxygen/README.md) — DS oxygen: mitochondrial oxygen in intestinal epithelial cells (already mapped) and macrophages (already mapped) sustains ATP for mucosal repair; hypoxia amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade and gut-microbiome (already mapped) dysbiosis.
- **Connects to:** [Carbon](../../02-atomic/carbon/README.md) — DS carbon: carbon backbone of amino acids in intestinal epithelial cells (already mapped) and hepatocytes (already mapped) fuels mucosal repair; carbon catabolites in gut-microbiome (already mapped) dysbiosis amplify NF-κB (already mapped) and IL-6 (already mapped) inflammation.
- **Connects to:** [Hydrogen](../../02-atomic/hydrogen/README.md) — DS hydrogen: hydrogen ions regulate pH in intestinal epithelial cells (already mapped) and macrophages (already mapped); proton gradient collapse from hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and gut-microbiome (already mapped) dysbiosis.
- **Connects to:** [VEGF](../../03-molecular/vegf/README.md) — DS VEGF: VEGF from macrophages (already mapped) and intestinal epithelial cells (already mapped) drives mucosal angiogenesis and repair; excess VEGF amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade and gut-microbiome (already mapped) dysbiosis.
- **Connects to:** [PD-1](../../03-molecular/pd-1/README.md) — DS pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses mucosal immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and gut-microbiome (already mapped) dysbiotic cascade in the digestive system.
- **Connects to:** [Angiotensin-II](../../03-molecular/angiotensin-ii/README.md) — DS angiotensin-ii: angiotensin-II from macrophages (already mapped) and intestinal epithelial cells (already mapped) modulates gut vascular tone; angiotensin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and gut-microbiome (already mapped) dysbiosis.
- **Connects to:** [RANKL](../../03-molecular/rankl/README.md) — DS rankl: RANKL from macrophages (already mapped) and intestinal epithelial cells (already mapped) modulates mucosal immune-epithelial crosstalk; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and gut-microbiome (already mapped) dysbiosis.

## Pathology

### Gastroesophageal Reflux Disease (GERD)

Affects ~20% of Western adults. Lower esophageal sphincter dysfunction → acid reflux → esophageal mucosal injury → Barrett's esophagus (columnar metaplasia) → esophageal adenocarcinoma (0.5%/year risk in Barrett's). Treatment: PPIs (omeprazole, pantoprazole).

### Peptic Ulcer Disease (PUD)

H. pylori infection (~50% of world population, but ulcers in ~10–15%): disrupts mucous barrier → acid erosion → ulcer. NSAID use second leading cause (COX-1 inhibition → ↓ prostaglandins → ↓ mucus + ↓ bicarbonate + ↓ mucosal blood flow). Complications: hemorrhage, perforation, obstruction.

### Inflammatory Bowel Disease (IBD)

**Crohn's disease:** Transmural inflammation, skip lesions, can affect any GI segment (most common: ileocolonic); fistulae, strictures, abscesses. Th1/Th17-driven; NOD2 mutation highest single genetic risk factor.

**Ulcerative colitis:** Mucosal inflammation, continuous from rectum proximally; limited to colon. Th2-driven. Risk of colorectal cancer with disease duration + extent.

Both treated with aminosalicylates, corticosteroids, immunomodulators (azathioprine), biologics (anti-TNF, anti-IL-12/23, anti-integrin).

### Celiac Disease

Immune-mediated enteropathy triggered by gluten (gliadin) in genetically susceptible individuals (HLA-DQ2/DQ8). Villous atrophy → malabsorption. Diagnosis: serology (anti-tTG IgA) + duodenal biopsy. Treatment: lifelong gluten-free diet.

### Colorectal Cancer (CRC)

Second leading cause of cancer death worldwide (~935,000 deaths/year) [^sung-2021-global-cancer-stats] [^bray-2024-colorectal]. Adenoma → carcinoma sequence driven by APC, KRAS, TP53, SMAD4 mutations. Lynch syndrome (MMR gene mutations) → hereditary nonpolyposis CRC (HNPCC). Screening: colonoscopy, fecal immunochemical test (FIT), stool DNA.

### Liver Diseases (see [Liver](../../06-organ/liver/README.md))

NAFLD (~25% global prevalence), alcoholic liver disease, viral hepatitis (296M chronic HBV, 58M chronic HCV worldwide) [^who-global-hepatitis], cirrhosis, HCC, DILI, acute liver failure.

### Pancreatitis

**Acute:** Most common causes: gallstones (biliary obstruction → pancreatic duct obstruction) and alcohol. Trypsin autoactivation → autodigestion → enzyme release → systemic inflammatory cascade. Severity by Revised Atlanta Classification. Severe AP mortality 20-30%.

**Chronic:** Irreversible parenchymal fibrosis and destruction; exocrine insufficiency (malabsorption) + endocrine insufficiency (diabetes). Main causes: alcohol (chronic), genetic (PRSS1, CFTR, SPINK1 mutations), autoimmune, idiopathic.

### Gallstone Disease (Cholelithiasis)

~15% of adults in developed countries. Cholesterol stones (80%, bile cholesterol supersaturation, impaired gallbladder motility) vs. pigment stones. Complications: biliary colic, acute cholecystitis, choledocholithiasis, ascending cholangitis, gallstone pancreatitis.

[^hall-guyton-14-gi]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 63-72.
[^openstax-anatomy-ch23]: OpenStax. *Anatomy & Physiology 2e*, Ch. 23: The Digestive System. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/23-introduction)
[^who-global-hepatitis]: World Health Organization. *Global Hepatitis Report 2024.* WHO; 2024. [who.int](https://www.who.int/publications/i/item/9789240091672)
[^sung-2021-global-cancer-stats]: Sung H, Ferlay J, Siegel RL, et al. Global Cancer Statistics 2020: GLOBOCAN. *CA Cancer J Clin.* 2021;71(3):209-249. [doi:10.3322/caac.21660](https://doi.org/10.3322/caac.21660) · [PubMed 33538338](https://pubmed.ncbi.nlm.nih.gov/33538338/)
[^bray-2024-colorectal]: Siegel RL et al. Colorectal cancer statistics, 2023. *CA Cancer J Clin.* 2023;73(3):233-254. [doi:10.3322/caac.21772](https://doi.org/10.3322/caac.21772) · [PubMed 36856579](https://pubmed.ncbi.nlm.nih.gov/36856579/)
