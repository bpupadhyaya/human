---
schema: human-scale-entry/v1
id: hepatic-lobule
name: Hepatic Lobule
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-04
summary: "Hexagonal functional unit of liver (~1–2 mm diameter). Hepatocyte cords radiate from a central vein; portal triads at corners supply blood and drain bile. Three metabolic zones: periportal (O₂-rich), intermediate, and centrilobular (CYP450-rich, ischemia-prone)."
aliases: ["classic liver lobule", "hepatic lobular unit", "liver lobule"]
sources:
  - id: teutsch-1999-lobule-3d
    type: peer-reviewed
    cite: "Teutsch HF, Schuerfeld D, Groezinger E. Three-dimensional reconstruction of parenchymal units in the liver of the rat. Hepatology. 1999;29(2):494-505."
    doi: "10.1002/hep.510290243"
    pmid: "9918928"
    url: "https://doi.org/10.1002/hep.510290243"
  - id: kietzmann-2017-metabolic-zonation
    type: peer-reviewed
    cite: "Kietzmann T. Metabolic zonation of the liver: The oxygen gradient revisited. Redox Biol. 2017;11:622-630."
    doi: "10.1016/j.redox.2017.01.012"
    pmid: "28126520"
    url: "https://doi.org/10.1016/j.redox.2017.01.012"
  - id: jungermann-1996-zonation
    type: peer-reviewed
    cite: "Jungermann K, Kietzmann T. Zonation of parenchymal and nonparenchymal metabolism in liver. Annu Rev Nutr. 1996;16:179-203."
    doi: "10.1146/annurev.nu.16.070196.001143"
    pmid: "8839922"
    url: "https://doi.org/10.1146/annurev.nu.16.070196.001143"
  - id: hall-guyton-14-liver
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 71."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/04-cellular/hepatocyte
    relation: contains
    note: "Hepatocytes are arranged in cords (1–2 cells thick) radiating from the central vein throughout the lobule, constituting the bulk of lobular parenchyma."
  - target: 01-human/06-organ/liver
    relation: part-of
    note: "Each liver contains ~100,000 lobules; the hepatic lobule is the repeating functional and histological unit of the liver."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Blood flows from portal triads (mixed portal venous + hepatic arterial) → sinusoids → central vein. All portal blood from the gastrointestinal tract first passes through liver sinusoids before entering systemic circulation."
  - target: 01-human/04-cellular/macrophage
    relation: contains
    evidence: hall-guyton-14-liver
    note: "Kupffer cells are resident macrophages lining the hepatic sinusoids within each lobule; they are the first line of defence against portal vein pathogens"
---

# Hepatic Lobule

## Overview

The hepatic lobule is the fundamental architectural and functional unit of the liver, the structure around which the liver's remarkable metabolic capacity is organized. On cross-section, it appears as a hexagonal prism approximately 1–2 mm in diameter and 1.5–2 mm in length [^teutsch-1999-lobule-3d]. At the center of each hexagon lies the **central vein** (a tributary of the hepatic vein); at each of the six corners sits a **portal triad** (a portal venule, a hepatic arteriole, and a bile duct).

The hepatic lobule is not simply a geometric description — it is the basis for understanding how blood flow creates metabolic heterogeneity within the liver, why certain toxins (like acetaminophen) and ischemic injury preferentially damage one zone, and how the liver processes absorbed nutrients from the portal circulation before they reach the systemic bloodstream.

An adult human liver contains approximately 100,000 hepatic lobules. These functional units are not sharply demarcated by connective tissue septa (unlike the lobules of other organs such as the kidney), except in certain conditions (e.g., pigs, or pathologic states like congestive hepatopathy where centrizonal fibrosis demarcates lobular boundaries more clearly).

## Structure

### The Classic Lobule

**Central vein (terminal hepatic venule):** A thin-walled venule at the geometric center of the hexagon, ~50–80 µm in diameter. Receives blood from the sinusoids and drains into the sublobular veins → hepatic veins → inferior vena cava.

**Portal triad (portal tract):** Located at each vertex of the hexagonal lobule, a portal triad contains:
- A **portal venule** (branch of portal vein, carries nutrient-rich but O₂-depleted blood from intestine)
- A **hepatic arteriole** (branch of hepatic artery, carries O₂-rich systemic arterial blood)
- A **bile duct** (lined by cholangiocytes; drains bile from canaliculi in the opposite direction to blood flow → toward portal tract → larger ducts)
- Lymphatics (in larger portal tracts)
- Occasionally: nerve fibers (adrenergic/cholinergic)

**Hepatocyte cords:** [Hepatocytes](../../04-cellular/hepatocyte/README.md) are arranged in radially oriented cords (plates), one to two cells thick, extending from the portal triads toward the central vein. This radial geometry maximizes the exposure of each hepatocyte to sinusoidal blood flowing along the cord.

**Sinusoids:** The spaces between adjacent hepatocyte cords are the liver sinusoids — modified capillaries 7–15 µm wide. They receive mixed blood from the portal venule and hepatic arteriole at the periphery of the lobule and carry it centripetally to the central vein.

Lining the sinusoids are two specialized non-parenchymal cell types:
- **Liver sinusoidal endothelial cells (LSECs):** Unique fenestrated endothelial cells with pores 100–150 nm in diameter (no diaphragm, no basement membrane under them). These fenestrae allow plasma (but not chylomicrons or large particles) to enter the **Space of Disse** — the perisinusoidal space between LSECs and hepatocytes — enabling direct exchange of lipoproteins, proteins, and metabolites between plasma and hepatocyte surfaces.
- **Kupffer cells:** Resident liver macrophages (derived from yolk sac macrophages and bone marrow monocytes) that line the sinusoids and phagocytose bacteria, endotoxins, aged red blood cells, and cellular debris arriving from the portal blood. They are the largest population of tissue-resident macrophages in the body and first responders to gut-derived pathogens.

**Space of Disse (perisinusoidal space):** The 0.2–0.5 µm subendothelial space between LSECs and hepatocyte basolateral membranes. Contains plasma (filtered through LSEC fenestrae), matrix components, and **hepatic stellate cells** (HSCs). HSCs (also called Ito cells) store vitamin A as retinyl esters (comprising 80% of total body vitamin A). Upon activation by injury, HSCs transform into myofibroblasts → produce collagen I, III → hepatic fibrosis. This is the central mechanism of cirrhosis.

**Bile canaliculi:** Tiny (~1 µm) channels formed by the apical (canalicular) membranes of adjacent hepatocytes, sealed by tight junctions. Bile flows from hepatocyte to canaliculi → to the canal of Hering (junction with bile ductules) → to bile ducts in portal triads — in the opposite direction to blood flow (from center to periphery).

### Three Models of Hepatic Architecture

Anatomists and physiologists use three overlapping models to describe the hepatic unit:

| Model | Unit | Focus |
|:---|:---|:---|
| **Classic lobule** | Hexagonal, central vein to portal triads | Histological/structural |
| **Portal lobule** | Triangular, portal triad to central, bile flow | Biliary/secretory |
| **Hepatic acinus (Rappaport)** | Rhomboid, zone 1–3 along sinusoid | Metabolic/clinical |

The **hepatic acinus (Rappaport's acinus)** is the most clinically useful model: it describes the metabolic zones along the axis of a single sinusoid from its portal end to the central vein.

### Metabolic Zonation

The oxygen and nutrient gradient along the sinusoidal axis creates distinct metabolic zones [^kietzmann-2017-metabolic-zonation] [^jungermann-1996-zonation]:

**Zone 1 — Periportal (high O₂, ~65–70 mmHg pO₂):**
- First to receive portal blood (high glucose, amino acids, O₂)
- Specializations: **gluconeogenesis**, **β-oxidation**, **urea synthesis**, **bile acid secretion**, **primary bile salt uptake** (NTCP)
- Cells express: PEPCK, PC (gluconeogenic enzymes), carbamoyl phosphate synthase (urea cycle)
- Resistant to ischemia; vulnerable to periportal hepatitis (e.g., viral hepatitis B, yellow fever)

**Zone 2 — Intermediate (midzonal):**
- Intermediate metabolic profile
- Some metabolic functions overlap with zones 1 and 3

**Zone 3 — Centrilobular/Perivenous (low O₂, ~35 mmHg pO₂):**
- Last to receive sinusoidal blood; hypoxic, low nutrient
- Specializations: **glycolysis**, **de novo lipogenesis**, **CYP450 drug metabolism** (CYP3A4, CYP2E1 — highest here), **glutamine synthesis**, **ketogenesis**
- **Most vulnerable to ischemia** (centrilobular necrosis in heart failure, shock) and toxins metabolized by CYP450 to reactive intermediates (acetaminophen zone-3 necrosis via CYP2E1/CYP3A4 → NAPQI → glutathione depletion → hepatocyte necrosis)
- Cells express: Wnt target genes (β-catenin high in zone 3 → GS glutamine synthetase, which is a reliable zone-3 hepatocyte marker on immunohistochemistry)

Zonation is not a fixed static property but is dynamically maintained by morphogen gradients: Wnt3a/Wnt2 from central vein endothelium keeps zone-3 hepatocytes in "perivenous fate"; EGF/Notch from portal tract maintains periportal fate.

## Function

### Processing of Portal Blood

Every nutrient absorbed by the gut epithelium enters the portal circulation and must pass through the hepatic lobule before entering the systemic bloodstream. The first-pass effect:
- **Glucose:** portally absorbed glucose is extracted by periportal zone 1 hepatocytes in postprandial state → stored as glycogen or converted to fat; only excess passes to systemic circulation
- **Amino acids:** deaminated; nitrogen → urea cycle (zone 1); carbon → gluconeogenesis or Krebs cycle
- **Lipids:** chylomicron remnants (too large for LSEC fenestrae) are cleared in periportal zone by LDL receptor-related protein (LRP1/ApoE recognition); free fatty acids enter hepatocytes via FATP5/CD36
- **Bile acids:** >95% of portal bile acids efficiently re-extracted by NTCP on periportal zone 1 hepatocytes (enterohepatic circulation)
- **Drugs and xenobiotics:** first-pass metabolism via CYP450s

### Bile Secretion

Hepatocytes constitutively secrete bile (~0.5–1.0 L/day) into canaliculi:
- **Primary components:** bile salts (conjugated bile acids, 50%), phosphatidylcholine (25%), cholesterol (4%), bilirubin-glucuronide, electrolytes, water
- **Direction:** canalicular → canal of Hering → bile ductules → portal duct → common hepatic duct → stored in gallbladder (concentrated 10-fold) → released into duodenum by CCK
- **Failure of bile flow (cholestasis):** bile accumulates → hepatocyte toxicity → jaundice; causes: viral hepatitis, drugs (DILI), PBC, PSC, intrahepatic cholestasis of pregnancy

### Immunological Function

Kupffer cells in the sinusoids form a first-line defense against bacteria and endotoxins (LPS) from the intestinal microbiome that continuously arrive via portal blood. This "gut-liver axis" surveillance prevents systemic bacteremia from normal gut leakage. Activated by LPS/TLR4, Kupffer cells release TNF-α, IL-6, IL-1β — inducing the acute-phase response in hepatocytes.

## Connections

- **Contains:** [Hepatocyte](../../04-cellular/hepatocyte/README.md) — the parenchymal cell population arranged in cords.
- **Part of:** [Liver](../../06-organ/liver/README.md) — the organ composed of ~100,000 lobules.
- **Connects to:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — portal venous and hepatic arterial blood converge in lobular sinusoids; absorbed lipids and nutrients enter systemic circulation after hepatic processing; portal hypertension in cirrhosis causes hepatic sinusoidal resistance → varices.

[^teutsch-1999-lobule-3d]: Teutsch HF, Schuerfeld D, Groezinger E. Three-dimensional reconstruction of parenchymal units in the liver of the rat. *Hepatology.* 1999;29(2):494-505. [doi:10.1002/hep.510290243](https://doi.org/10.1002/hep.510290243) · [PubMed 9918928](https://pubmed.ncbi.nlm.nih.gov/9918928/)
[^kietzmann-2017-metabolic-zonation]: Kietzmann T. Metabolic zonation of the liver: The oxygen gradient revisited. *Redox Biol.* 2017;11:622-630. [doi:10.1016/j.redox.2017.01.012](https://doi.org/10.1016/j.redox.2017.01.012) · [PubMed 28126520](https://pubmed.ncbi.nlm.nih.gov/28126520/)
[^jungermann-1996-zonation]: Jungermann K, Kietzmann T. Zonation of parenchymal and nonparenchymal metabolism in liver. *Annu Rev Nutr.* 1996;16:179-203. [doi:10.1146/annurev.nu.16.070196.001143](https://doi.org/10.1146/annurev.nu.16.070196.001143) · [PubMed 8839922](https://pubmed.ncbi.nlm.nih.gov/8839922/)
[^hall-guyton-14-liver]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 71.
