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
