---
schema: medicine-entry/v1
id: zinc-dietary
name: Dietary Zinc
atlas: 03-medicine
scale: 03-food
status: draft
last_reviewed: 2026-06-05
summary: "Dietary zinc (RDA 8–11 mg/day) is essential for immune function, wound healing, and enzyme catalysis. Bioavailability is limited by phytates. Supplementation ≥75 mg/day reduces cold duration ~33%. Deficiency impairs T-cell maturation and growth."
aliases: ["zinc", "Zn", "zinc supplement", "zinc acetate", "zinc gluconate", "zinc sulfate", "zinc picolinate", "zinc lozenges", "zinc bisglycinate", "zinc deficiency", "hypozincemia"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: prasad-2008-zinc-review
    type: peer-reviewed
    cite: "Prasad AS. Zinc: role in immunity, oxidative stress and chronic inflammation. Curr Opin Clin Nutr Metab Care. 2009;12(6):646-52."
    doi: "10.1097/MCO.0b013e3283312956"
    pmid: "19770647"
    url: "https://doi.org/10.1097/MCO.0b013e3283312956"
    accessed: "2026-06-05"
  - id: cochrane-zinc-colds-2015
    type: peer-reviewed
    cite: "Science M, Johnstone J, Roth DE, Guyatt G, Loeb M. Zinc for the treatment of the common cold: a systematic review and meta-analysis of randomized controlled trials. CMAJ. 2012;184(10):E551-61."
    doi: "10.1503/cmaj.111990"
    pmid: "22566526"
    url: "https://doi.org/10.1503/cmaj.111990"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Zinc is required for thymulin (a zinc-dependent thymic peptide driving T-cell maturation), NK cell cytotoxicity, and macrophage oxidative burst. Deficiency impairs lymphocyte proliferation, reduces CD4+ T-cell counts, and increases susceptibility to intracellular pathogens and respiratory infections."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "Zinc is essential for IL-2 signalling and T-helper cell proliferation; zinc finger domains in TCR signalling kinases and transcription factors (GATA-3, T-bet, RORγt) require Zn²⁺ for structural integrity. Supplementation in deficient subjects restores Th1/Th2 balance and thymulin activity."
  - target: 01-human/07-system/musculoskeletal-system
    relation: modulates
    note: "Zinc is required for collagen synthesis, keratinocyte migration during wound healing, and osteoblast differentiation. Zinc finger-containing transcription factors (Runx2, Sp7/Osterix) govern osteoblastogenesis. Deficiency causes growth retardation, impaired wound healing, and reduced bone mineral density in children."
  - target: 01-human/02-atomic/zinc
    relation: part-of
    note: "Dietary zinc entry covers bioavailability, absorption (ZIP4/SLC39A4), RDA, food sources, and supplementation context. The atomic-scale entry covers Zn²⁺ electron configuration, coordination chemistry, and role as Lewis acid in catalytic zinc enzymes (carbonic anhydrase, carboxypeptidase, alcohol dehydrogenase)."
---

# Dietary Zinc

## Overview

**Zinc (Zn, atomic number 30)** is an essential trace mineral present in every cell of the human body. It ranks second only to iron as the most abundant trace element in the body, with a total body content of approximately **2–3 g** distributed across muscle (~57%), bone (~29%), skin and hair (~6%), liver (~5%), and all other tissues including a high concentration in the prostate gland, eye (choroid), and immune cells.

Unlike iron, zinc has no dedicated storage form — the body does not maintain appreciable labile zinc stores. This makes **dietary adequacy critical**: even brief deficiency can rapidly impair immune function.

**Dietary Reference Intakes (DRIs):**

| Population | RDA (mg/day) | Tolerable Upper Limit (UL) |
|:---|:---|:---|
| Men ≥19 years | 11 | 40 |
| Women ≥19 years | 8 | 40 |
| Pregnant women | 11 | 40 |
| Lactating women | 12 | 40 |
| Children 9–13 years | 8 | 23 |

**Food Sources (mg zinc per standard serving):**

| Food | Zinc content |
|:---|:---|
| Oysters (3 oz, cooked) | 74 mg — by far the richest source |
| Beef (ground, 3 oz) | 5.4 mg |
| Crab (blue, 3 oz) | 3.2 mg |
| Lobster (3 oz) | 3.4 mg |
| Pork loin (3 oz) | 2.9 mg |
| Baked beans (1/2 cup) | 2.9 mg |
| Pumpkin seeds (1 oz) | 2.2 mg |
| Cashews (1 oz) | 1.6 mg |
| Chickpeas (1/2 cup) | 1.3 mg |
| Yogurt (plain, 8 oz) | 1.7 mg |
| Almonds (1 oz) | 0.9 mg |

The critical caveat: **bioavailability differs dramatically by food matrix**. [^prasad-2008-zinc-review]

## Mechanism

### Intestinal Absorption: ZIP4 and Metallothionein Regulation

Dietary zinc absorption occurs primarily in the **duodenum and proximal jejunum** via a saturable, transporter-mediated process:

**Luminal uptake (apical membrane):**
- **ZIP4 (SLC39A4):** The primary zinc importer on the enterocyte brush-border membrane. ZIP4 expression is upregulated at the mRNA and protein level during zinc deficiency (a classical homeostatic response). Mutations in ZIP4 cause **acrodermatitis enteropathica** — a rare recessive disorder of severe zinc malabsorption presenting with perioral/perigenital dermatitis, alopecia, diarrhea, and immune failure in infancy.
- **ZIP5 (SLC39A5):** Expressed on the basolateral surface; facilitates zinc efflux during zinc repletion
- **Divalent metal transporter 1 (DMT1/SLC11A2):** Minor contribution; primarily the iron transporter but has zinc affinity at high concentrations

**Intracellular buffering:**
- **Metallothionein (MT-1/MT-2):** Cysteine-rich, low-molecular-weight proteins in the enterocyte cytoplasm that bind 7 atoms of Zn²⁺ per molecule. MT synthesis is induced by zinc (via metal-responsive transcription factor MTF1) and also by glucocorticoids, IL-1, and inflammation. When enterocyte zinc is high, more MT is synthesized → traps zinc intracellularly → it is shed with the enterocyte at villus tip turnover (every 3-5 days), limiting net absorption — a key homeostatic mechanism.
- **ZnT5 (SLC30A5):** Transports zinc from ER lumen; involved in Golgi-zinc loading of zinc-requiring secretory proteins

**Basolateral exit:**
- **ZnT1 (SLC30A1):** The primary basolateral zinc exporter; transfers zinc into portal circulation
- Portal zinc is bound to albumin (~80%) and α₂-macroglobulin (~18%) for transport to the liver

**Net absorption rate:**
- **Omnivore diet:** ~25-30% of dietary zinc absorbed
- **Vegetarian/vegan diet:** ~15-20% — substantially reduced due to phytate content

### Phytates: The Major Inhibitor of Zinc Absorption

**Phytic acid (inositol hexaphosphate, IP6)** is the primary storage form of phosphorus in plant seeds (legumes, grains, nuts). Phytate binds zinc (and also iron, calcium, magnesium) with high affinity in the GI lumen → forms insoluble zinc-phytate complexes → prevents ZIP4 uptake.

- **Molar phytate:zinc ratio (PZR)** is the key predictor of zinc bioavailability: PZR <5 → minimal inhibition; PZR 5-15 → moderate inhibition; PZR >15 → severe inhibition (common in un-fermented, un-sprouted whole grain and legume staple diets)
- **Strategies to reduce phytate content:**
  - **Fermentation (sourdough, tempeh, natto):** Phytase enzymes (from lactobacilli and yeasts) hydrolyze IP6 → inositol + free phosphate → releases zinc → markedly improves bioavailability
  - **Soaking and sprouting:** Activates endogenous seed phytases; reduces phytate 25-75% depending on duration and temperature
  - **Milling (removing bran):** Removes phytate-concentrated aleurone layer but also removes zinc — a net negative unless consuming predominantly refined grain

**Animal protein enhancers:** Cysteine-rich peptides from meat digestion form soluble zinc-amino acid chelates → maintain zinc solubility in the upper intestine → improve absorption (explaining higher bioavailability from animal vs. plant sources)

### Biochemical Roles of Zinc

Zinc functions in three biochemical roles: **catalytic**, **structural**, and **regulatory**.

**Catalytic zinc proteins (>300 known):**
- **Carbonic anhydrase (CA II in red blood cells):** Zn²⁺ in the active site activates water to hydroxide, enabling CO₂ + H₂O ⇌ HCO₃⁻ + H⁺ at 10⁶ reactions/second — one of the fastest known enzymes; essential for CO₂ transport in blood
- **Carboxypeptidase A:** Zn²⁺ coordinates the substrate carbonyl and polarizes it for nucleophilic attack by Glu270 — digestive enzyme cleaving C-terminal residues from proteins
- **Alcohol dehydrogenase (ADH):** Contains two Zn²⁺ per subunit; catalytic Zn²⁺ activates the alcohol substrate for hydride transfer to NAD⁺
- **Matrix metalloproteinases (MMPs):** Zn²⁺-dependent endopeptidases that remodel extracellular matrix — role in wound healing, tumor invasion, tissue remodeling
- **Angiotensin-converting enzyme (ACE):** Contains catalytic Zn²⁺; target of ACE inhibitor drugs

**Structural zinc — "zinc fingers":**
- Classical C₂H₂ zinc fingers (Zn²⁺ tetrahedrally coordinated by 2 Cys + 2 His): most common in transcription factors; stabilizes the 12-aa β-β-α "zinc finger" fold that inserts into DNA major groove
- LIM domain zinc fingers, RING domain zinc fingers (E3 ubiquitin ligases), PHD fingers (chromatin readers) — collectively represent ~3% of the human proteome containing zinc-binding domains
- **Zinc finger transcription factors relevant to immune function:** GATA-3 (Th2 lineage), T-bet (Th1 lineage), RORγt (Th17 lineage), Foxp3 (Treg lineage) — all require Zn²⁺ for structural integrity of DNA-binding domains

**Regulatory zinc:**
- Free Zn²⁺ concentration in the cytoplasm is ~1 pM (femtomolar in some estimates) — tightly buffered by metallothionein and other zinc-binding proteins
- Synaptic zinc (released from glutamatergic vesicles at ~300 µM concentrations): modulates NMDA receptor, GABA_A receptor, and acid-sensing ion channels at the synapse
- Zinc transients in immune cells: "zinc spark" (massive zinc release from ER/vesicles during oocyte fertilization); rapid zinc flux following BCR/TCR activation modulates MAPK and PI3K/Akt signaling

### Immune Function: Thymulin and Lymphocyte Biology

Zinc's role in immunity is among its most clinically important functions: [^prasad-2008-zinc-review]

**Thymulin:**
- A nonapeptide hormone (FTS — facteur thymique sérique / serum thymic factor) secreted by thymic epithelial cells
- **Zinc-dependent:** Thymulin is active only when chelated with Zn²⁺; apothymulin (zinc-free form) is inactive
- Functions: drives thymocyte maturation → CD3+ T cell development, promotes CD4/CD8 differentiation, induces IL-2 receptor expression → required for IL-2-driven T-cell proliferation
- Thymulin levels **decline with age** (thymic involution) — contributing to immunosenescence; zinc supplementation in elderly partially restores thymulin levels and T-cell function

**Natural killer (NK) cell function:**
- NK cell cytotoxicity (ADCC and spontaneous killing) requires zinc for perforin formation and granzyme B activation in cytotoxic granules
- Zinc deficiency → reduced NK cell numbers and activity; restoration with zinc supplementation (25-45 mg/day) partially reverses NK cell defects in deficient individuals

**Macrophage function:**
- Zinc is required for respiratory burst (NADPH oxidase activity) — superoxide radical generation against phagocytosed pathogens
- Zinc deficiency → reduced macrophage phagocytic capacity and ↓IL-12 production (biasing away from Th1)
- Zinc also inhibits NF-κB (via A20/TNFAIP3 upregulation) → ↓pro-inflammatory cytokine production — anti-inflammatory effect at adequate/high zinc levels

## Clinical Use

### Zinc and the Common Cold

The most clinically tested application. Proposed mechanism: Zn²⁺ ions (released from lozenges in the oropharynx) directly inhibit rhinovirus replication by:
- Blocking rhinovirus 3C protease (a cysteine protease; Zn²⁺ coordinates the active-site Cys)
- Preventing rhinovirus attachment to ICAM-1 (the cellular receptor on nasal epithelium)
- Stimulating mucociliary clearance and IFN-γ production

**Evidence (Cochrane/systematic review):** Science et al. (2012) [^cochrane-zinc-colds-2015]:
- Zinc acetate lozenges ≥75 mg/day (elemental zinc): ~33% reduction in duration of common cold (risk ratio 0.67 for symptom resolution by day 7)
- Zinc sulfate (lower bioavailability as Zn²⁺ in oropharynx): less consistent benefit
- **Critical requirement:** lozenges must dissolve slowly in the mouth to achieve high oropharyngeal Zn²⁺ concentrations; swallowed tablets are ineffective for cold treatment (only effective for systemic immunity)
- Side effects of high-dose lozenges: nausea, metallic/bad taste (caused by zinc-amino acid complexes from salivary protein binding)

### Zinc Deficiency: Clinical Presentation

Global zinc deficiency is the **fifth leading cause of disease burden** in developing countries. Presentations:

| Symptom | Mechanism |
|:---|:---|
| Hypogeusia/anosmia | Gustin (carbonic anhydrase VI in saliva) requires zinc; taste bud renewal impaired |
| Growth retardation | ↓IGF-1 bioavailability (zinc required for IGFBP proteolysis); impaired collagen synthesis |
| Impaired wound healing | ↓keratinocyte proliferation; ↓collagen cross-linking; ↓MMP remodeling |
| Alopecia | ↓follicular keratinocyte turnover; telogen effluvium pattern |
| Dermatitis (perioral/perigenital) | Acrodermatitis enteropathica pattern; severe deficiency only |
| Hypogonadism (males) | Testosterone biosynthesis requires zinc-dependent 5α-reductase and aromatase modulation |
| Night blindness | Zinc required for retinol dehydrogenase (vitamin A metabolism in retina) |
| ↑Infection susceptibility | Impaired innate and adaptive immunity (see above) |

### Zinc Toxicity (Chronic Excess)

- **>40 mg/day (UL) chronically:** Copper deficiency — zinc and copper share intestinal absorption machinery (both inducing MT in enterocytes; MT has higher affinity for copper); high zinc → excess MT → copper trapped in shed enterocytes → copper malabsorption → microcytic anemia, peripheral neuropathy (myelopathy), neutropenia
- **Acute high dose (>150-200 mg):** Nausea, vomiting, abdominal cramping (direct GI irritant effect of ionic zinc)
- **Therapeutic exception:** High-dose zinc (150-200 mg/day elemental) is used to treat Wilson's disease (copper overload) by deliberately inducing MT-mediated copper block — the toxicity mechanism is exploited therapeutically

### Drug and Nutrient Interactions

- **Antibiotics (quinolones, tetracyclines):** Zinc chelates the antibiotic in the GI lumen → markedly reduced antibiotic bioavailability; separate by ≥2 hours
- **Penicillamine (Wilson's disease, RA):** Zinc reduces penicillamine absorption; separate administration
- **Phytates (see above):** Major dietary interaction; also applies to supplemental zinc taken with high-phytate meals
- **Calcium supplements:** High-dose calcium may compete for ZIP4 uptake at very high intakes; less established than phytate interaction

## Evidence

### Immune Function

Prasad [^prasad-2008-zinc-review] and multiple subsequent reviews establish:
- Zinc deficiency is associated with lymphopenia, reduced NK cell activity, reduced DTH responses, and increased susceptibility to pneumonia, diarrheal disease, and malaria
- **GRADE: Moderate** for immune function impairment in deficiency and restoration with supplementation
- RCTs in malnourished children (ZINC trial and others): zinc supplementation 10-20 mg/day × 2 weeks reduces duration of acute diarrhea by ~25% and pneumonia-related morbidity

### Growth in Children

Multiple RCTs in zinc-deficient developing-country children show significant improvements in height and weight velocity with zinc supplementation 10-20 mg/day. Effect size is larger in stunted (height-for-age z-score <-2) children. WHO/UNICEF recommend zinc supplementation as adjunct treatment in acute diarrhea in children under 5.

### Macular Degeneration

**Age-Related Eye Disease Study (AREDS, n=3,640):** Zinc (80 mg/day zinc oxide + antioxidants) significantly reduced progression to advanced AMD (RR 0.72; 95% CI: 0.60-0.87) over 10 years. The AREDS2 formula (replacing β-carotene with lutein/zeaxanthin) retains zinc at 80 mg/day as a key component. GRADE: **High** for AMD risk reduction in intermediate/advanced-risk AMD.

## Connections

- **Modulates** → [Immune System](../../../../../01-human/07-system/immune-system/README.md): Zinc is required for thymulin (a zinc-dependent thymic peptide that drives T-cell maturation), NK cell cytotoxicity, and macrophage oxidative burst. Deficiency impairs lymphocyte proliferation, reduces circulating CD4+ T-cell counts, and increases susceptibility to intracellular pathogens and respiratory infections. Supplementation restores thymulin bioactivity in deficient individuals.

- **Modulates** → [T-Helper Cell](../../../../../01-human/04-cellular/t-helper-cell/README.md): Zinc is essential for IL-2 signalling and T-helper cell proliferation; zinc finger domains in TCR signalling kinases and lineage-defining transcription factors (GATA-3, T-bet, RORγt, Foxp3) require Zn²⁺ for structural integrity and DNA binding. Supplementation in deficient subjects restores Th1/Th2 balance and reverses thymulin deficiency-associated T-cell maturation arrest.

- **Modulates** → [Musculoskeletal System](../../../../../01-human/07-system/musculoskeletal-system/README.md): Zinc is required for collagen synthesis (zinc-dependent MMPs in ECM remodeling), keratinocyte migration during wound healing, and osteoblast differentiation via zinc-finger transcription factors Runx2 and Sp7/Osterix. Deficiency causes growth retardation, impaired fracture healing, reduced bone mineral density, and prolonged wound closure time.

- **Part-of** → [Zinc (Atomic)](../../../../../01-human/02-atomic/zinc/README.md): This dietary/supplemental entry covers bioavailability, absorption (ZIP4/SLC39A4), RDA, food sources, deficiency, toxicity, and clinical use. The atomic-scale entry covers Zn²⁺ electron configuration, coordination chemistry, and its fundamental role as a Lewis acid in catalytic zinc enzymes (carbonic anhydrase, carboxypeptidase A, alcohol dehydrogenase, matrix metalloproteinases).

[^prasad-2008-zinc-review]: Prasad AS. Curr Opin Clin Nutr Metab Care. 2009;12(6):646-52. doi:10.1097/MCO.0b013e3283312956
[^cochrane-zinc-colds-2015]: Science M et al. CMAJ. 2012;184(10):E551-61. doi:10.1503/cmaj.111990

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
