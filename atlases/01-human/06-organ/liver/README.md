---
schema: human-scale-entry/v1
id: liver
name: Liver
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-04
summary: "Largest internal organ (~1.5 kg), right upper quadrant. Dual blood supply: portal vein (75%) + hepatic artery (25%). Performs >500 functions: glucose/lipid homeostasis, protein synthesis, detoxification, bile secretion. Exceptional regenerative capacity after injury."
aliases: ["hepar", "hepatic organ"]
sources:
  - id: hall-guyton-14-liver
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 71."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
  - id: michalopoulos-2007-liver-regen
    type: peer-reviewed
    cite: "Michalopoulos GK. Liver regeneration. J Cell Physiol. 2007;213(2):286-300."
    doi: "10.1002/jcp.21172"
    pmid: "17559071"
    url: "https://doi.org/10.1002/jcp.21172"
  - id: who-hepatitis-b
    type: regulatory
    cite: "World Health Organization. Hepatitis B Fact Sheet. WHO; 2023."
    url: "https://www.who.int/news-room/fact-sheets/detail/hepatitis-b"
    accessed: "2026-06-04"
  - id: friedman-2003-liver-fibrosis
    type: peer-reviewed
    cite: "Friedman SL. Mechanisms of hepatic fibrogenesis. Gastroenterology. 2008;134(6):1655-69."
    doi: "10.1053/j.gastro.2008.03.003"
    pmid: "18471545"
    url: "https://doi.org/10.1053/j.gastro.2008.03.003"
  - id: younossi-2019-nafld
    type: peer-reviewed
    cite: "Younossi ZM, Koenig AB, Abdelatif D, Fazel Y, Henry L, Wymer M. Global epidemiology of nonalcoholic fatty liver disease-Meta-analytic assessment of prevalence, incidence, and outcomes. Hepatology. 2016;64(1):73-84."
    doi: "10.1002/hep.28431"
    pmid: "26707365"
    url: "https://doi.org/10.1002/hep.28431"
cross_links:
  - target: 01-human/05-tissue/hepatic-lobule
    relation: contains
    note: "~100,000 hepatic lobules are the repeating functional units of the liver, each containing hepatocyte cords, sinusoids, portal triads, and a central vein."
  - target: 01-human/04-cellular/hepatocyte
    relation: contains
    note: "Hepatocytes are the parenchymal cells of the liver, constituting ~80% of liver volume and executing its core metabolic functions."
  - target: 01-human/07-system/digestive-system
    relation: part-of
    note: "The liver is an accessory organ of the digestive system; it processes absorbed nutrients, synthesizes bile for fat digestion, and detoxifies gut-absorbed toxins."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The liver regulates lipids and glucose entering the systemic circulation; portal hypertension in cirrhosis affects cardiac preload; statins target hepatic cholesterol synthesis."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "SARS-CoV-2 injures the liver via ACE2 expressed in hepatocytes and cholangiocytes, immune-mediated hepatitis, drug-induced liver injury from COVID-19 treatments, and hypoxic hepatitis from systemic hypoxemia."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: treated-by
    note: "Statins inhibit HMG-CoA reductase in hepatocytes, reducing LDL-C synthesis and upregulating hepatic LDL receptor expression; approved for primary and secondary cardiovascular prevention."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: infected-by
    note: "HBV infects hepatocytes via NTCP receptor; cccDNA persists in hepatocyte nuclei as a stable minichromosome; chronic infection leads to fibrosis progression (Metavir F0→F4), cirrhosis, and HCC in 20–30% of cirrhotics."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: damaged-by
    note: "HBV-mediated immune activation drives hepatocellular necroinflammation; progressive hepatocyte loss causes bridging fibrosis, cirrhosis, portal hypertension, and hepatocellular carcinoma."
  - target: 01-human/03-molecular/il-6
    relation: modulated-by
    note: "IL-6/gp130 signaling drives the hepatic acute-phase response: CRP, fibrinogen, SAA, hepcidin synthesis ↑; albumin, transferrin ↓; this is the molecular basis for elevated inflammatory markers in infection and injury."
  - target: 01-human/03-molecular/cortisol
    relation: modulated-by
    note: "Cortisol drives hepatic gluconeogenesis (via PEPCK, G6Pase induction) and glycogen synthesis; chronic glucocorticoid excess causes hepatic steatosis and central obesity."
  - target: 01-human/03-molecular/insulin
    relation: modulated-by
    note: "Insulin suppresses hepatic glucose output via FOXO1 phosphorylation and promotes glycogen synthesis and lipogenesis; hepatic insulin resistance is a key driver of fasting hyperglycemia in T2DM."
  - target: 01-human/03-molecular/tnf-alpha
    relation: damaged-by
    note: "At high concentrations (septic shock, immune hepatitis), TNFR1-mediated caspase-8 activation causes hepatocyte apoptosis and contributes to acute liver failure and coagulopathy."
  - target: 02-pathogen/01-viruses/dengue-virus
    relation: damaged-by
    note: "Dengue virus infects hepatocytes via AXL and DC-SIGN; elevated AST/ALT occurs in >80% of dengue cases; fulminant hepatic failure in severe dengue contributes to coagulopathy."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: treated-by
    note: "The primary site of metformin action; OCT1-mediated hepatocyte uptake → Complex I inhibition → AMPK activation → suppression of PEPCK and G6Pase → reduced hepatic glucose output."
  - target: 01-human/04-cellular/macrophage
    relation: contains
    evidence: hall-guyton-14-liver
    note: "Kupffer cells are the liver's resident macrophages, comprising 15% of hepatic cells and ~80% of all tissue-resident macrophages in the body"
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: damaged-by
    evidence: hall-guyton-14-liver
    note: "E. coli bacteraemia seeds the liver via portal circulation; LPS activates Kupffer TLR4 causing hepatic inflammation; EHEC Shiga toxin causes hepatocyte injury"
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: damaged-by
    evidence: hall-guyton-14-liver
    note: "S. aureus hepatic abscesses and TSST-1-mediated cytokine storm cause hepatocyte apoptosis and elevated transaminases in severe staphylococcal infections"
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: damaged-by
    evidence: hall-guyton-14-liver
    note: "hepatosplenic candidiasis (chronic disseminated candidiasis) causes liver microabscesses and granulomas in neutropenic patients recovering from chemotherapy"
  - target: 03-medicine/02-traditional/berberine
    relation: treated-by
    evidence: younossi-2019-nafld
    note: "berberine activates AMPK in hepatocytes, reducing lipogenesis and improving insulin sensitivity; clinical trials show reductions in hepatic steatosis markers in NAFLD patients"
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: damaged-by
    note: "Chronic HCV triggers hepatic stellate cell activation via TGF-β, driving progressive fibrosis (METAVIR F0→F4); 20–30% develop cirrhosis within 20 years; HCC risk is 2–4% annually after cirrhosis."
  - target: 01-human/03-molecular/collagen
    relation: modulated-by
    note: "Modulated by Collagen."
  - target: 01-human/03-molecular/glucagon
    relation: modulated-by
    note: "Modulated by Glucagon."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: modulated-by
    note: "Modulated by Thyroid Hormones (T3/T4)."
  - target: 01-human/02-atomic/copper
    relation: modulated-by
    note: "Modulated by Copper."
  - target: 01-human/02-atomic/iron
    relation: modulated-by
    note: "Modulated by Iron."
  - target: 01-human/02-atomic/sulfur
    relation: modulated-by
    note: "Modulated by Sulfur."
  - target: 01-human/07-system/reproductive-system
    relation: modulated-by
    note: "Modulated by Reproductive System."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: modulated-by
    note: "Modulated by Islet of Langerhans."
  - target: 01-human/04-cellular/neutrophil
    relation: modulated-by
    note: "Modulated by Neutrophil."
  - target: 01-human/04-cellular/fibroblast
    relation: modulated-by
    note: "Modulated by Fibroblast."
  - target: 01-human/06-organ/large-intestine
    relation: modulated-by
    note: "Modulated by Large Intestine."
  - target: 01-human/06-organ/small-intestine
    relation: modulated-by
    note: "Modulated by Small Intestine."
  - target: 01-human/06-organ/stomach
    relation: modulated-by
    note: "Modulated by Stomach."
  - target: 01-human/06-organ/thyroid
    relation: modulated-by
    note: "Modulated by Thyroid Gland."
  - target: 02-pathogen/01-viruses/ebola-virus
    relation: damaged-by
    note: "Damaged by Ebola Virus (EBOV)."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: damaged-by
    note: "Damaged by Epstein-Barr Virus."
  - target: 02-pathogen/04-parasites/leishmania-donovani
    relation: damaged-by
    note: "Damaged by Leishmania donovani."
  - target: 02-pathogen/02-bacteria/salmonella-typhi
    relation: damaged-by
    note: "Damaged by Salmonella typhi."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: damaged-by
    note: "Damaged by Helicobacter pylori."
  - target: 03-medicine/03-food/sulforaphane
    relation: modulated-by
    note: "Modulated by Sulforaphane."
  - target: 03-medicine/03-food/resveratrol
    relation: modulated-by
    note: "Modulated by Resveratrol."
  - target: 03-medicine/02-traditional/milk-thistle
    relation: modulated-by
    note: "Modulated by Milk Thistle / Silymarin (Silybum marianum)."
taxonomy:
  uberon: "UBERON:0002107"
  fma: "FMA:7197"
---

# Liver

## Overview

The liver is the largest internal organ of the human body and the metabolic hub of virtually every major biochemical pathway. Weighing approximately 1.2–1.6 kg in adults, it occupies the right hypochondriac region and much of the epigastric region of the upper abdomen, tucked beneath the right hemidiaphragm and protected by the lower rib cage [^hall-guyton-14-liver].

Two features make the liver anatomically unique among abdominal organs:

1. **Dual blood supply:** The liver receives blood from two sources: the **hepatic portal vein** (~75% of total flow, nutrient-rich but relatively O₂-poor, arriving from the gastrointestinal tract) and the **hepatic artery proper** (~25% of flow, O₂-rich from the aorta via the celiac trunk). This portal circulation ensures that absorbed nutrients, drugs, and gut-derived toxins all pass through the liver before entering the systemic circulation — the first-pass effect that enables the liver to buffer and regulate systemic blood chemistry.

2. **Exceptional regenerative capacity:** Unlike most organs, the adult liver retains robust regenerative potential. After a 70% hepatectomy (the amount donated in living-related transplantation), the remnant restores full functional mass within 4–8 weeks in humans [^michalopoulos-2007-liver-regen]. This capacity is exploited clinically and limits progression to liver failure in many disease states.

## Structure

### Gross Anatomy

The liver is classically described as having **4 lobes:**
- **Right lobe** — largest, bounded by the falciform ligament on its left
- **Left lobe** — left of the falciform ligament
- **Caudate lobe** — posterior, between the IVC and porta hepatis; drains directly into the IVC via short hepatic veins (spared in Budd-Chiari syndrome)
- **Quadrate lobe** — anterior, between the gallbladder fossa and the round ligament

The **Couinaud classification** divides the liver into 8 independent functional segments based on hepatic venous and portal pedicle territory — the surgical standard for planning partial hepatectomy.

**Porta hepatis ("gate of the liver"):** The transverse fissure on the inferior surface where the portal vein, hepatic artery, and common hepatic duct enter/exit. The hepatoduodenal ligament (part of the lesser omentum) contains these structures and can be compressed (Pringle maneuver) to temporarily stop inflow bleeding during liver surgery.

**Ligamentous attachments:** Falciform ligament (anterior, connects to anterior abdominal wall), round ligament (ligamentum teres, obliterated left umbilical vein), coronary ligaments, triangular ligaments, hepatogastric and hepatoduodenal ligaments (lesser omentum).

### Microscopic Structure

The liver contains approximately 100,000 **[hepatic lobules](../../05-tissue/hepatic-lobule/README.md)** — hexagonal units with a central vein surrounded by hepatocyte cords and sinusoids, with portal triads at each vertex.

**Cell types of the liver:**

| Cell | Proportion | Function |
|:---|:---|:---|
| Hepatocytes | ~60% of cells, ~80% volume | Metabolism, protein synthesis, detoxification, bile secretion |
| Liver sinusoidal endothelial cells (LSEC) | ~20% | Fenestrated, gatekeeping access to Disse space; scavenge oxidized LDL; express anti-inflammatory molecules |
| Kupffer cells | ~15% | Resident macrophages; phagocytosis; immune surveillance; TLR4-LPS sensing |
| Hepatic stellate cells (HSC) | ~5% | Vitamin A storage (quiescent); fibrosis producer (activated myofibroblasts) |
| Cholangiocytes | Small % | Line bile ducts; bile modification (HCO₃⁻ secretion, water); primary target in PBC/PSC |
| Pit cells (NK cells) | Small % | Liver-resident lymphocytes; surveillance |

### Biliary Tree

Bile secreted by hepatocytes into canaliculi flows via a tree of progressively larger ducts:
```
Bile canaliculi → Canals of Hering → bile ductules → interlobular bile ducts (portal tracts)
→ segmental ducts → right/left hepatic ducts → common hepatic duct → 
→ [± cystic duct/gallbladder storage] → common bile duct → ampulla of Vater → duodenum
```
Sphincter of Oddi (at ampulla) regulates entry of bile into duodenum; CCK causes contraction of gallbladder + Oddi relaxation postprandially.

## Function

### Carbohydrate Metabolism

The liver maintains blood glucose within the narrow 70–100 mg/dL range through opposing processes:

**Postprandial (insulin-dominant):**
- Glucose uptake via GLUT2 (high Km — only active when portal glucose is high)
- Glucokinase phosphorylates glucose → glucose-6-phosphate (trapped in hepatocyte)
- Glycogen synthesis (glycogen synthase activated by insulin signaling)
- Glycolysis → pyruvate → acetyl-CoA → de novo lipogenesis → VLDL secretion (surplus calories)

**Fasted/overnight:**
- Glycogen phosphorylase activation (glucagon → PKA → phosphorylase kinase)
- Glycogenolysis → glucose-6-phosphate → (glucose-6-phosphatase, only in liver/kidney) → free glucose → blood

**Prolonged fast (>12 h):**
- Gluconeogenesis (PEPCK, FBPase, G6Pase) from: lactate (Cori cycle), alanine (glucose-alanine cycle), glycerol (from lipolysis)
- Ketogenesis: acetyl-CoA excess → acetoacetyl-CoA → HMG-CoA → β-hydroxybutyrate/acetoacetate (exported to brain, cardiac muscle)

### Lipid and Lipoprotein Metabolism

**Endogenous cholesterol synthesis (~70% of total):**
Acetyl-CoA → HMG-CoA → (HMG-CoA reductase, HMGCR — **statin target**) → mevalonate → cholesterol. Hepatic cholesterol is incorporated into bile or packaged into VLDL.

**Lipoprotein secretion:**
- **VLDL** (triglyceride-rich) assembled in hepatocyte ER → secreted → plasma lipolysis by LPL → IDL → LDL
- **HDL** assembly initiated by ABCA1-mediated cholesterol efflux to apoA-I

**LDL clearance:**
Hepatic LDL receptors (LDLR) clear ~70% of plasma LDL. Statin-induced reduction of intracellular cholesterol → SREBP2 activation → LDLR upregulation → reduced plasma LDL-C.

### Protein Synthesis and Secretion

Daily hepatic protein secretion:
- **Albumin:** 10–15 g/day; major oncotic pressure protein; carrier for fatty acids, bilirubin, drugs, calcium, hormones
- **Fibrinogen:** 1–5 g/day; clotting substrate
- **Clotting factors II, V, VII, VIII, IX, X, XI:** hepatic synthesis (factors II, VII, IX, X require vitamin K for γ-carboxylation)
- **Complement (C1–C9):** mostly hepatic origin
- **CRP, serum amyloid A, haptoglobin, ferritin:** acute-phase response (IL-6/STAT3 activation within hours of injury/infection)
- **IGF-1:** liver-derived growth factor (GH → hepatic IGF-1 → somatic growth)

### Detoxification

The liver intercepts xenobiotics and metabolic waste before systemic exposure:

**Phase I reactions (CYP450s)** — oxidation, reduction, hydrolysis; create reactive intermediates:
- CYP3A4: ~50% of drug metabolism
- CYP2D6: codeine, metoprolol, many antidepressants
- CYP2E1: ethanol metabolism (zone 3) → acetaldehyde (toxic) → acetate; also activates CCl4, acetaminophen at high doses

**Phase II reactions** — conjugation → increased solubility for excretion:
- Glucuronidation (UGTs): bilirubin, morphine, estrogen
- Sulfation (SULTs): acetaminophen, estrogen
- Glutathione conjugation (GSTs): reactive electrophiles (NAPQI from acetaminophen overdose — when glutathione depleted → hepatocyte necrosis)
- Acetylation (NAT2): isoniazid, sulfonamides (pharmacogenomic variation in acetylator status)

**Phase III** — biliary and sinusoidal transporters: MRP2 (canalicular bilirubin glucuronide), P-glycoprotein (MDR1), BSEP (bile salts).

**Ammonia detoxification:** The urea cycle converts toxic NH₃ from amino acid catabolism and gut bacteria to non-toxic urea; hepatic failure → hyperammonemia → hepatic encephalopathy.

**Bilirubin metabolism:**
- Senescent RBCs → macrophage heme catabolism → unconjugated (indirect) bilirubin
- Albumin transport → liver OATP1B1/1B3 uptake → conjugation (UGT1A1 glucuronidation) → direct bilirubin → bile
- Gut bacteria → urobilinogen → urobilin (urine) or stercobilin (feces)
- Jaundice: conjugation defect (Gilbert's: UGT1A1 polymorphism), biliary obstruction, hemolysis, hepatocellular disease

### Bile Secretion

~500–1000 mL bile/day:
- **Primary bile acids:** cholic acid and chenodeoxycholic acid (synthesized from cholesterol via CYP7A1 — rate-limiting, regulated by FXR/FGF-19 feedback)
- **Conjugated bile salts:** glycocholate, taurocholate — more water-soluble, better intestinal absorption
- **Function in duodenum:** emulsification of dietary fats → micelle formation → lipase access → fat absorption
- **Enterohepatic circulation:** 95% of bile salts reabsorbed in terminal ileum (ASBT transporter) → portal vein → hepatocyte NTCP reuptake → recycled; total pool circulates 2–3×/meal

### Immune and Inflammatory Functions

- Kupffer cells: first-line defense against portal bacteremia; major source of TNF-α, IL-6, IL-12 during sepsis
- Acute-phase response: hepatocytes produce CRP, fibrinogen, haptoglobin, SAA → support immune defense and opsonization
- Immunological tolerance: the liver is inherently tolerogenic (preventing immune reactivity to gut antigens constantly arriving via portal blood) — relevant to transplantation tolerance

## Connections

- **Contains:** [Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md) — the tissue unit.
- **Contains:** [Hepatocyte](../../04-cellular/hepatocyte/README.md) — the parenchymal cell.
- **Part of:** [Digestive System](../../07-system/digestive-system/README.md) — processes absorbed nutrients and produces bile.
- **Connects to:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — portal circulation, VLDL/HDL secretion influencing systemic lipids, portal hypertension → cardiac effects.
- **Damaged by:** SARS-CoV-2 — hepatic injury in 14–53% of COVID-19 patients.
- **Treated by:** [Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md) — HMG-CoA reductase inhibition for LDL-C reduction.

## Pathology

### Non-Alcoholic Fatty Liver Disease (NAFLD) / NASH

NAFLD affects ~25% of the global adult population (1.8 billion people) [^younossi-2019-nafld]. The spectrum:
- **Simple steatosis** (NAFL): ≥5% hepatocyte fat, no significant inflammation → usually benign
- **NASH (steatohepatitis)**: steatosis + hepatocyte ballooning + lobular inflammation → fibrosis risk
- **Advanced fibrosis/cirrhosis**: portal hypertension, varices, ascites, HRS
- **Hepatocellular carcinoma (HCC)**: NASH-cirrhosis → HCC at ~2%/year

Pathophysiology: insulin resistance → excess hepatic fat → ER stress → mitochondrial dysfunction → JNK/IκB → inflammation (Kupffer activation) → TGF-β → hepatic stellate cell activation → fibrosis [^friedman-2003-liver-fibrosis].

### Alcoholic Liver Disease

Spectrum: steatosis → alcoholic hepatitis → cirrhosis/HCC. Ethanol → acetaldehyde (CYP2E1, ADH) → oxidative stress, mitochondrial injury, Kupffer activation, HSC activation → fibrosis.

### Viral Hepatitis

| Virus | Route | Chronicity | Cancer risk |
|:---|:---|:---|:---|
| HAV | Fecal-oral | Never | None |
| HBV | Blood/sexual/perinatal | 5-10% adults, 90% neonates | High (HCC) |
| HCV | Blood | 55-85% | High (HCC, cirrhosis) |
| HEV | Fecal-oral | Rare (immunosuppressed) | None typically |

~296 million people live with chronic HBV, ~58 million with chronic HCV (WHO 2023) [^who-hepatitis-b].

### Cirrhosis

End-stage chronic liver disease: replacement of functional parenchyma with fibrotic scar (collagen I/III from activated HSCs) → nodular regenerative architecture → increased intrahepatic vascular resistance → portal hypertension.

**Complications of portal hypertension:**
- Esophageal/gastric varices → life-threatening hemorrhage
- Ascites (low portal oncotic + high hydrostatic → fluid transudation into peritoneum)
- Hepatorenal syndrome (HRS) — functional renal failure from renal vasoconstriction; splanchnic vasodilation
- Hepatic encephalopathy — hyperammonemia + systemic inflammatory state → neurological dysfunction
- Spontaneous bacterial peritonitis (SBP) — bacterial translocation from gut → ascitic fluid infection

### Hepatocellular Carcinoma (HCC)

Third most common cause of cancer death worldwide. Major risk factors: HBV (+HBV DNA integration), HCV, NASH-cirrhosis, aflatoxin exposure, alcohol cirrhosis. Surveillance: AFP + liver ultrasound every 6 months in cirrhotic patients.

### Drug-Induced Liver Injury (DILI)

Most common cause of acute liver failure in Western countries (>50%). Mechanisms: direct toxicity (acetaminophen → NAPQI → zone-3 necrosis), idiosyncratic (amoxicillin-clavulanate, isoniazid, halothane), cholestatic (flucloxacillin, erythromycin), hepatocellular (statins — class effect, usually mild), immune-mediated.

[^hall-guyton-14-liver]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 71.
[^michalopoulos-2007-liver-regen]: Michalopoulos GK. Liver regeneration. *J Cell Physiol.* 2007;213(2):286-300. [doi:10.1002/jcp.21172](https://doi.org/10.1002/jcp.21172) · [PubMed 17559071](https://pubmed.ncbi.nlm.nih.gov/17559071/)
[^who-hepatitis-b]: World Health Organization. Hepatitis B Fact Sheet. WHO; 2023. [who.int](https://www.who.int/news-room/fact-sheets/detail/hepatitis-b)
[^friedman-2003-liver-fibrosis]: Friedman SL. Mechanisms of hepatic fibrogenesis. *Gastroenterology.* 2008;134(6):1655-69. [doi:10.1053/j.gastro.2008.03.003](https://doi.org/10.1053/j.gastro.2008.03.003) · [PubMed 18471545](https://pubmed.ncbi.nlm.nih.gov/18471545/)
[^younossi-2019-nafld]: Younossi ZM et al. Global epidemiology of nonalcoholic fatty liver disease. *Hepatology.* 2016;64(1):73-84. [doi:10.1002/hep.28431](https://doi.org/10.1002/hep.28431) · [PubMed 26707365](https://pubmed.ncbi.nlm.nih.gov/26707365/)
