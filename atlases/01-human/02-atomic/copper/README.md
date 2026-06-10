---
schema: human-scale-entry/v1
id: copper
name: Copper
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Copper (Cu, atomic number 29) — 80–100 mg total; Cu⁺/Cu²⁺ redox cycling drives cytochrome c oxidase, SOD1, ceruloplasmin (iron loading), lysyl oxidase (ECM crosslinking), and dopamine β-hydroxylase. Wilson (ATP7B) and Menkes (ATP7A) are the hallmark copper disorders."
aliases: ["Cu", "Cu+", "Cu2+", "cuprous", "cupric", "copper-63"]
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
  - id: lutsenko-copper-transport
    type: peer-reviewed
    cite: "Lutsenko S. Human copper homeostasis: a network of interconnected pathways. Curr Opin Chem Biol. 2010;14(2):211-7."
    doi: "10.1016/j.cbpa.2010.01.003"
    pmid: "20117040"
    url: "https://doi.org/10.1016/j.cbpa.2010.01.003"
  - id: ala-wilson-disease
    type: peer-reviewed
    cite: "Ala A, Walker AP, Ashkan K, Dooley JS, Schilsky ML. Wilson's disease. Lancet. 2007;369(9559):397-408."
    doi: "10.1016/S0140-6736(07)60196-2"
    pmid: "17276780"
    url: "https://doi.org/10.1016/S0140-6736(07)60196-2"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "80–100 mg total Cu; redox-active Cu⁺/Cu²⁺ cycling in cytochrome c oxidase (ETC), SOD1 (antioxidant), ceruloplasmin (Fe metabolism), and dopamine β-hydroxylase (catecholamine synthesis)."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Liver is the central Cu hub — ATP7B exports Cu into bile (main excretion route); Wilson disease (ATP7B mutation) causes Cu accumulation leading to hepatic necrosis and cirrhosis."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Cu required for DβH (dopamine→norepinephrine), Complex IV (neuronal ATP production), and SOD1 (ALS-linked mutations); Menkes disease — X-linked ATP7A defect causes brain Cu deficiency → neurodegeneration."
  - target: 01-human/03-molecular/dopamine
    relation: modulates
    note: "Dopamine β-hydroxylase requires Cu²⁺ and ascorbate to hydroxylate dopamine → norepinephrine in synaptic vesicles; copper deficiency impairs catecholamine synthesis and sympathetic neurotransmission."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc supplementation induces intestinal metallothionein → traps Cu⁺ in enterocytes → reduced Cu absorption → copper deficiency (myeloneuropathy, cytopenias); Wilson disease maintenance uses zinc 150 mg/day to block Cu absorption; Cu/Zn SOD1 requires both metals for activity."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "SOD1 (Cu/Zn superoxide dismutase) mutations cause ~20% of familial ALS: >180 variants (A4V, G93A) destabilize the fold → Cu/Zn miscoordination → SOD1 aggregation → motor neuron death; misfolded SOD1 propagates prion-like; SOD1 antisense (tofersen) approved for SOD1-ALS."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Amyloid precursor protein (APP) has a Cu-binding domain; Aβ peptides chelate Cu and Fe → redox cycling → oxidative neuronal damage; Cu chelators (clioquinol, PBT2) dissolve Aβ plaques in animal models; Cu dyshomeostasis is an early feature of AD neurodegeneration."
---

# Copper

## Overview

Copper (symbol Cu, atomic number 29) is a **d-block transition metal** in Group 11 of the periodic table, with atomic mass 63.55 u and electron configuration [Ar] 3d¹⁰ 4s¹. Copper is one of the most ancient metallic cofactors in life — its use as a redox catalyst predates the Great Oxidation Event 2.4 billion years ago — and today it is an **essential trace element** for every organism with aerobic metabolism. The total human body copper content is approximately **80–100 mg**, distributed highest in the liver (~15 µg/g wet weight), brain, kidney, heart, and muscle [^lutsenko-copper-transport].

Unlike zinc (which is exclusively Zn²⁺), copper cycles between two oxidation states: **cuprous Cu⁺** (d¹⁰, colourless, soft Lewis acid) and **cupric Cu²⁺** (d⁹, blue, harder Lewis acid). This **redox cycling** — analogous to Fe²⁺/Fe³⁺ in iron chemistry — is what makes copper indispensable for electron transfer enzymes: cytochrome c oxidase (Complex IV of the mitochondrial ETC), ceruloplasmin (ferroxidase), and others. However, this same redox activity makes free copper **acutely toxic**: Cu⁺ + H₂O₂ → Cu²⁺ + OH• + OH⁻ (Fenton-like reaction), generating the most reactive oxidant in biology. Consequently, living cells maintain free Cu at concentrations of less than **one free copper atom per cell** — all cellular copper is protein-bound, trafficked by dedicated chaperones [^stryer-biochemistry].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 29 |
| Atomic mass | 63.55 u (⁶³Cu 69.2%, ⁶⁵Cu 30.8%) |
| Electron configuration | [Ar] 3d¹⁰ 4s¹ |
| Oxidation states in biology | Cu⁺ (cuprous, d¹⁰) and Cu²⁺ (cupric, d⁹) |
| Ionic radius Cu⁺ | 0.077 nm; Cu²⁺ 0.073 nm |
| Preferred coordination | Cu⁺: linear or tetrahedral (thiolate, His); Cu²⁺: square planar or distorted octahedral (His, Met, Cys) |
| Electronegativity (Pauling) | 1.90 |
| Redox potential (Cu²⁺/Cu⁺) | +0.15 V (vs. SHE); varies widely by protein environment (+0.18 to +0.80 V in blue copper proteins) |

### Copper Sites in Proteins: Type 1, 2, and 3

Bioinorganic chemists classify protein copper centres by their spectroscopic and functional properties:

| Type | Features | Examples | Function |
|:---|:---|:---|:---|
| **Type 1 (T1) "Blue copper"** | Intense blue colour (600 nm); tetragonal distorted; His₂CysMet ligands; high redox potential | Azurin, plastocyanin, copper chaperone CCS, Cu_A in CcO | Electron transfer (single electron) |
| **Type 2 (T2) "Normal copper"** | No EPR-detectable coupling; His₂–4O; catalytic | SOD1 Cu, galactose oxidase, amine oxidases | Substrate oxidation; O₂ activation |
| **Type 3 (T3) "Coupled binuclear"** | Antiferromagnetically coupled Cu₂ pair; EPR silent | Tyrosinase, laccase | O₂ binding; hydroxylation |
| **Cu_B in CcO** | Paired with haem a₃ | Cytochrome c oxidase | O₂ reduction site |

The **Cu_A centre** in cytochrome c oxidase (a mixed-valence Cu₁.₅⁺–Cu₁.₅⁺ pair bridged by two Cys residues) is one of the most unusual metal centres in biology — a delocalised binuclear site that accepts electrons from cytochrome c and delivers them efficiently to the haem a / Cu_B active site where O₂ is reduced to H₂O.

## Function

### Key Copper Enzymes and Proteins

#### 1. Cytochrome c Oxidase (Complex IV of ETC)

CcO is the terminal electron acceptor of the mitochondrial respiratory chain, reducing O₂ to H₂O while pumping protons across the inner mitochondrial membrane to generate the electrochemical gradient that drives ATP synthesis:

> 4 ferrocyt c + O₂ + 8H⁺_(matrix) → 4 ferricyt c + 2H₂O + 4H⁺_(intermembrane)

CcO contains **4 copper atoms per functional unit** (plus 2 haem groups):
- **Cu_A** (binuclear, in subunit 2): accepts electrons from cytochrome c (E°' = +0.24 V); → haem a → Cu_B/haem a₃
- **Cu_B** (subunit 1, paired with haem a₃): the actual O₂ reduction site — the ferryl-oxo intermediate [Fe(IV)=O ... Cu_B²⁺] is the reaction intermediate; 4 electrons + 4 H⁺ + O₂ → 2 H₂O

Copper deficiency therefore directly impairs aerobic ATP production, especially in high-energy-demand tissues (brain, heart, skeletal muscle) [^stryer-biochemistry].

#### 2. Cu/Zn Superoxide Dismutase (SOD1)

SOD1 is the principal cytosolic antioxidant enzyme that catalyses the disproportionation of superoxide radicals:
> O₂•⁻ + O₂•⁻ + 2H⁺ → O₂ + H₂O₂

The catalytic mechanism alternates Cu between +2 and +1:
- Cu²⁺ + O₂•⁻ → Cu⁺ + O₂
- Cu⁺ + O₂•⁻ + 2H⁺ → Cu²⁺ + H₂O₂

Zinc in SOD1 is structural (not redox-active), stabilising the β-barrel fold and maintaining Cu in position. The CCS (copper chaperone for SOD1) copper chaperone delivers Cu specifically to SOD1. **ALS-linked SOD1 mutations** (>180 identified; e.g., A4V, G93A) destabilise the protein fold, leading to aberrant Cu/Zn coordination, protein aggregation, and motor neuron death — the mechanism of ~20% of familial ALS cases [^lutsenko-copper-transport].

#### 3. Ceruloplasmin

Ceruloplasmin (CP) is an α₂-glycoprotein (~132 kDa) containing **6 copper atoms per molecule** (3 T1, 1 T2, and 1 T3 pair). It is synthesised exclusively in the liver, secreted into plasma, and circulates as the **dominant plasma copper carrier** (>95% of plasma copper). Its primary enzymatic activity is **ferroxidase** — oxidising Fe²⁺ → Fe³⁺:
> 4 Fe²⁺ + O₂ + 4H⁺ → 4 Fe³⁺ + 2H₂O

This activity is essential for iron export from cells: **Fe²⁺ (transported out by ferroportin) must be oxidised to Fe³⁺ before transferrin can bind it**. Without ceruloplasmin ferroxidase activity (as in acaeruloplasminaemia — a rare AR disorder from CP gene mutation), iron accumulates in the brain, liver, and pancreas despite normal total body iron stores, causing **neurodegeneration with brain iron accumulation** (retinal degeneration, cerebellar ataxia, dementia, diabetes mellitus) [^lutsenko-copper-transport].

Ceruloplasmin is also an **acute-phase protein** — its synthesis rises during inflammation, trauma, and infection (IL-6 stimulates transcription), causing the plasma copper to increase during acute illness.

#### 4. Lysyl Oxidase (LOX)

Lysyl oxidase is a copper-containing amine oxidase secreted into the extracellular matrix. It catalyses the **oxidative deamination of lysine residues** in collagen and elastin, initiating the formation of covalent crosslinks (lysinonorleucine, hydroxylysyl pyridinoline, desmosine/isodesmosine) that provide tensile strength and resilience to ECM:
> Peptidyl-lysine + O₂ + H₂O → peptidyl-allysine + H₂O₂ + NH₃

Copper deficiency → reduced LOX activity → **defective collagen and elastin crosslinking** → connective tissue fragility → vascular aneurysms (especially of the aorta), skeletal deformities, and skin laxity. This is dramatically illustrated in **Menkes disease** (see Pathology), where defective copper delivery to LOX produces the characteristic aortic aneurysms, tortuous vessels, and "kinky hair" (defective hair keratin crosslinking).

#### 5. Dopamine β-Hydroxylase (DβH)

DβH is a tetrameric copper-containing monooxygenase located in the **lumen of catecholamine-secretory vesicles** in noradrenergic neurons and adrenal chromaffin cells. It catalyses:
> Dopamine + O₂ + 2 ascorbate → norepinephrine + H₂O + 2 dehydroascorbate

Each DβH subunit contains **2 copper atoms** (one T2 type) that cycle between Cu⁺ and Cu²⁺ during catalysis; ascorbate (vitamin C) is the essential electron donor that regenerates Cu⁺ after each catalytic cycle. Copper deficiency impairs DβH, reducing norepinephrine synthesis relative to dopamine — a feature of both Menkes disease and experimental copper deficiency in animals [^guyton-hall].

#### 6. Peptidylglycine α-Amidating Monooxygenase (PAM)

PAM amidates the C-terminus of neuropeptides and peptide hormones (oxytocin, TRH, calcitonin, substance P, neuropeptide Y, VIP) — a modification required for biological activity. The enzyme contains 2 copper atoms (type 2) and requires ascorbate and O₂. Without copper or ascorbate, these regulatory peptides are inactive.

#### 7. Cytochrome c Oxidase Assembly Chaperones

Copper delivery to CcO requires a dedicated chaperone cascade:
- **COX17** (soluble IMS protein): Cu⁺ carrier from cytoplasm → IMS
- **SCO1/SCO2** (IMS membrane proteins): deliver Cu to Cu_A centre (subunit 2)
- **COX11** (IMS membrane protein): delivers Cu to Cu_B site (subunit 1)

Mutations in SCO1, SCO2, or COX11 cause CcO assembly deficiency (mitochondrial disease) — demonstrating that copper chaperones, not just copper itself, are essential for CcO function.

### Copper Homeostasis: Absorption, Trafficking, and Excretion

**Intestinal absorption:**
1. Dietary Cu²⁺ is reduced to Cu⁺ by the brush-border reductase **DCYTB (CYBRD1)**
2. **hCTR1 (SLC31A1)** — a homotrimeric high-affinity Cu⁺ importer at the apical membrane — translocates Cu⁺ into enterocytes; hCTR1 is the primary route of intestinal Cu uptake
3. Intracellular Cu⁺ is immediately captured by **ATOX1** (Cu chaperone), **CCS**, or **COX17** chaperones — free Cu is never detectable
4. **ATP7A** (Menkes protein) — a P-type Cu-transporting ATPase at the enterocyte trans-Golgi network (TGN) — exports Cu into portal blood under normal conditions; under Cu excess, ATP7A redistributes to the basolateral membrane to accelerate Cu efflux

**Liver handling:**
1. Portal Cu²⁺ is extracted by hepatocytes via hCTR1
2. ATOX1 delivers Cu to **ATP7B** (Wilson protein) — a P-type ATPase at the hepatocyte TGN
3. Under normal conditions, ATP7B pumps Cu into the TGN to be incorporated into ceruloplasmin (for secretion) and into bile (for excretion via apical vesicle fusion with bile canaliculi)
4. Under Cu excess, ATP7B relocates to apical vesicles to increase biliary Cu excretion — the primary Cu homeostatic mechanism [^ala-wilson-disease]

**Excretion:** ~80% of excess copper is excreted in **bile** → feces; urinary copper excretion is small (~50 µg/day) under normal conditions. Unlike most trace elements, there is no hormonal regulation of copper excretion analogous to hepcidin for iron; biliary excretion kinetics are the main control.

## Connections

- `part-of` → **[Human body](../../08-whole-body/human-body/README.md)** — 80–100 mg total Cu; redox-active Cu⁺/Cu²⁺ cycling is essential in cytochrome c oxidase (ETC), SOD1 (antioxidant), ceruloplasmin (Fe metabolism), lysyl oxidase (ECM crosslinking), and dopamine β-hydroxylase.
- `modulates` → **[Liver](../../06-organ/liver/README.md)** — liver is the central copper processing hub; ATP7B exports Cu into bile (primary excretion route); Wilson disease (ATP7B mutation) causes hepatic Cu accumulation → necrosis, cirrhosis, and acute liver failure.
- `modulates` → **[Nervous system](../../07-system/nervous-system/README.md)** — Cu required for DβH (dopamine→norepinephrine), Complex IV (neuronal ATP), and SOD1 (ALS-linked mutations); Menkes disease — X-linked ATP7A defect causes brain Cu deficiency → neurodegeneration and death in early childhood.
- `modulates` → **[Dopamine](../../03-molecular/dopamine/README.md)** — dopamine β-hydroxylase requires Cu²⁺ and ascorbate to hydroxylate dopamine → norepinephrine in synaptic vesicles; copper deficiency impairs catecholamine synthesis and sympathetic neurotransmission.
- `connects-to` → **[Zinc](../zinc/README.md)** — zinc supplementation induces intestinal metallothionein → traps Cu⁺ in enterocytes → reduced absorption → copper deficiency; Wilson disease maintenance uses zinc 150 mg/day; Cu/Zn SOD1 requires both metals for antioxidant activity.
- `connects-to` → **[ALS](../../07-system/als/README.md)** — SOD1 mutations cause ~20% of familial ALS; A4V and G93A variants destabilize the Cu/Zn coordination → SOD1 aggregation → motor neuron death; misfolded SOD1 spreads prion-like; SOD1 antisense (tofersen) is approved for SOD1-ALS.
- `connects-to` → **[Alzheimer's Disease](../../07-system/alzheimers-disease/README.md)** — APP has a Cu-binding domain; Aβ peptides chelate Cu and Fe → redox cycling → oxidative neuronal damage; Cu chelators (clioquinol, PBT2) dissolve Aβ plaques in animal models; Cu dyshomeostasis is an early feature of AD.

## Pathology

### Wilson Disease (ATP7B Mutation)

**Wilson disease (hepatolenticular degeneration)** is an autosomal recessive disorder caused by mutations in *ATP7B* (chromosome 13q14.3), encoding the hepatic copper-exporting P-type ATPase. Over 900 pathogenic variants have been identified; H1069Q is the most common in European patients, and R778L in East Asian populations [^ala-wilson-disease].

Without functional ATP7B, copper accumulates progressively in the liver from birth (biliary excretion abolished; ceruloplasmin poorly cuproylated → apo-ceruloplasmin rapidly cleared from plasma). Overflow then deposits copper in brain, kidneys, and eyes:

| Organ | Features | Mechanism |
|:---|:---|:---|
| **Liver** | Steatosis → chronic hepatitis → cirrhosis → acute liver failure | Mitochondrial dysfunction (CcO); oxidative stress (Fenton OH•) |
| **Brain (basal ganglia/cortex)** | Dysarthria, dystonia, tremor, psychiatric (depression, psychosis) | Cu deposition in lenticular nuclei → neuronal death |
| **Eyes (cornea)** | Kayser-Fleischer rings (gold-brown ring at limbus) | Cu granule deposition in Descemet membrane; near-universal in neurological presentation |
| **Kidney** | Fanconi syndrome (proximal tubule dysfunction), haematuria | Cu toxicity to tubular epithelium |
| **Blood** | Coombs-negative haemolytic anaemia (acute liver failure crisis) | Massive Cu release into blood oxidises RBC membranes |

**Diagnosis:** Low serum ceruloplasmin (<0.20 g/L; >95% sensitive for neurological WD), elevated 24h urine copper (>100 µg/day at baseline, >1600 µg/day after penicillamine challenge), liver biopsy Cu >250 µg/g dry weight, ATP7B mutation analysis (genotyping).

**Treatment:**
- **D-penicillamine** (first-line chelator): forms soluble Cu-penicillamine complexes → urinary excretion; major side effects: lupus-like reaction, Goodpasture nephritis, worsening neurological symptoms (Cu chelation releases hepatic Cu into blood transiently)
- **Trientine (triethylenetetramine)**: second-line chelator; fewer side effects than penicillamine
- **Zinc acetate (elemental Zn 150 mg/day)**: induces intestinal metallothionein → traps Cu in shed enterocytes → reduces net absorption; used for maintenance and in presymptomatic patients
- **Liver transplantation**: curative for hepatic Wilson disease; corrects the metabolic defect; not indicated as primary treatment for neurological Wilson disease (neurological damage may persist)

### Menkes Disease (ATP7A Mutation)

**Menkes disease (kinky hair disease)** is an X-linked recessive disorder caused by mutations in *ATP7A*, the copper-exporting ATPase in most non-hepatic cells. Boys are predominantly affected (X-linked); girls are heterozygous carriers with variable expression.

**Pathophysiology:** ATP7A is required for copper export from enterocytes into portal blood, and for copper delivery within the TGN to cuproenzymes (DβH, LOX, COX, PAM). Without ATP7A, copper accumulates in enterocytes and kidney but is depleted from all other organs — a paradox of copper abundance in gut and deficiency in brain.

| Feature | Mechanism |
|:---|:---|
| **Kinky/steely/pili torti hair** | LOX deficiency → defective keratin crosslinks → twisted, brittle hair shafts |
| **Neurodegeneration** | CcO and DβH deficiency in neurons; progressive seizures, hypotonia, developmental regression |
| **Vascular tortuosity** | LOX deficiency → fragile elastin/collagen in vessel walls → cerebral artery elongation ("corkscrew" vessels on angiography) |
| **Bone abnormalities** | LOX deficiency → poor cortical bone crosslinking → metaphyseal fractures, wormian skull bones |
| **Bladder diverticula** | LOX deficiency → fragile bladder wall connective tissue |

Onset: 2–3 months of age (after maternal copper stores depleted); death typically before age 3 without treatment. Treatment with subcutaneous copper-histidine early in infancy (before symptom onset) can modify the course if diagnosed presymptomatically; most cases present symptomatically with a worse prognosis.

### Acquired Copper Deficiency

Causes: excessive zinc supplementation (see Zinc entry), gastric bypass surgery, parenteral nutrition without Cu, malabsorption. Presentation mimics **subacute combined degeneration of the spinal cord** (B12 deficiency): myelopathy (posterior column > lateral column), peripheral neuropathy, and haematological features (microcytic or normocytic anaemia, neutropenia). Treatment: oral or IV copper supplementation.

### Copper and Neurodegenerative Disease

- **ALS:** 20% of familial ALS caused by SOD1 mutations; >180 variants identified; aggregated misfolded SOD1 is toxic to motor neurons; animal models faithfully reproduce ALS
- **Prion disease:** Cellular prion protein (PrPC) binds 4 Cu²⁺ at its octapeptide repeat region; copper binding may regulate PrPC endocytosis and signalling; the PrPC → PrPSc conversion in prion disease may involve loss of Cu-binding neuroprotection
- **Alzheimer disease:** Amyloid precursor protein (APP) has a Cu-binding domain; Aβ peptides chelate Cu and Fe, promoting redox cycling and oxidative damage; Cu-chelating compounds (clioquinol, PBT2) have been investigated as therapeutics

| Disease | Cu-related mechanism | Clinical implication |
|:---|:---|:---|
| Wilson disease | ATP7B loss → hepatic/brain Cu accumulation | Copper chelation; zinc; liver transplant |
| Menkes disease | ATP7A loss → systemic Cu deficiency except enterocytes | Early Cu-His injection; genetic counselling |
| Acquired Cu deficiency | Myeloneuropathy, cytopenias | Cu supplementation; identify cause |
| Familial ALS | SOD1 Cu/Zn miscoordination → aggregation | SOD1-targeted therapies (antisense, gene therapy) |
| Acaeruloplasminaemia | CP loss → brain iron accumulation | Plasma ceruloplasmin infusion; deferoxamine |

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
[^lutsenko-copper-transport]: Lutsenko S. Human copper homeostasis: a network of interconnected pathways. *Curr Opin Chem Biol.* 2010;14(2):211-7. [doi:10.1016/j.cbpa.2010.01.003](https://doi.org/10.1016/j.cbpa.2010.01.003) · [PubMed 20117040](https://pubmed.ncbi.nlm.nih.gov/20117040/)
[^ala-wilson-disease]: Ala A, Walker AP, Ashkan K, Dooley JS, Schilsky ML. Wilson's disease. *Lancet.* 2007;369(9559):397-408. [doi:10.1016/S0140-6736(07)60196-2](https://doi.org/10.1016/S0140-6736(07)60196-2) · [PubMed 17276780](https://pubmed.ncbi.nlm.nih.gov/17276780/)
