---
schema: human-scale-entry/v1
id: zinc
name: Zinc
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Zinc (Zn²⁺, atomic number 30) — 2–4 g in the human body, 2nd most abundant trace metal after iron. Structural in ~2500 zinc-finger proteins; catalytic in >200 enzymes (carbonic anhydrase, carboxypeptidase, ADH, MMPs); regulates insulin storage and immunity."
aliases: ["Zn", "Zn2+", "zinc ion", "zinc finger", "zinc-65"]
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
  - id: vallee-zinc-enzymes
    type: peer-reviewed
    cite: "Vallee BL, Falchuk KH. The biochemical basis of zinc physiology. Physiol Rev. 1993;73(1):79-118."
    doi: "10.1152/physrev.1993.73.1.79"
    pmid: "8380364"
    url: "https://doi.org/10.1152/physrev.1993.73.1.79"
  - id: prasad-zinc-immunity
    type: peer-reviewed
    cite: "Prasad AS. Zinc in human health: effect of zinc on immune cells. Mol Med. 2008;14(5-6):353-7."
    doi: "10.2119/2008-00033.Prasad"
    pmid: "18385818"
    url: "https://doi.org/10.2119/2008-00033.Prasad"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "2–4 g total Zn²⁺ (60% muscle, 30% bone, 10% liver/kidney/retina/prostate); structural in ~2500 zinc-finger proteins; catalytic in >200 enzymes across every cell type."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "Zinc is required for T-cell maturation via thymulin (Zn-dependent thymic hormone), proliferation, and cytokine production; severe deficiency causes lymphopenia and impaired T-helper function."
  - target: 01-human/03-molecular/insulin
    relation: modulates
    note: "3 Zn²⁺ ions per insulin hexamer in pancreatic β-cell secretory granules; crystallises insulin for dense storage; Zn²⁺ is co-released into portal circulation alongside insulin."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Zn²⁺ is a central regulator of innate and adaptive immunity — required for neutrophil function, NK cell activity, and Ab production; deficiency impairs all arms of immunity."
  - target: 03-medicine/03-food/zinc-dietary
    relation: composed-of
    note: "Composed Of by Dietary Zinc."
---

# Zinc

## Overview

Zinc (symbol Zn, atomic number 30) is a **d-block transition metal** in Group 12 of the periodic table, with atomic mass 65.38 u and ground-state electron configuration [Ar] 3d¹⁰ 4s². Unlike iron and copper, zinc does **not undergo redox cycling** in biology — its d-shell is completely filled, giving Zn²⁺ a fixed +2 oxidation state that makes it exclusively a **Lewis acid** rather than a redox participant [^stryer-biochemistry]. This property — strong Lewis acidity without Fenton chemistry — is what makes Zn²⁺ the ideal catalytic cofactor for hydrolytic enzymes and an indispensable structural scaffold in transcription factors.

The human body contains approximately **2–4 g of zinc**, making it the **second most abundant trace element** after iron. Around 60% resides in skeletal muscle, 30% in bone, and the remaining 10% is distributed across liver, kidney, prostate, skin, and retina — tissues with notably high metabolic activity or specialized secretory functions [^vallee-zinc-enzymes]. Unlike serum iron or calcium, plasma zinc (~80–120 µg/dL) constitutes only ~0.1% of total body zinc and is a poor indicator of zinc status, complicating clinical assessment.

Zinc participates in biology in three distinct roles: **structural** (stabilizing protein folds via tetrahedral Cys/His coordination), **catalytic** (direct participation in enzyme active sites as a Lewis acid), and **regulatory** (modulating signaling pathways, gene expression, and hormone storage). These roles are not mutually exclusive — a single zinc-binding protein often exploits two or three simultaneously.

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 30 |
| Atomic mass | 65.38 u |
| Electron configuration | [Ar] 3d¹⁰ 4s² |
| Ionic form in biology | Zn²⁺ exclusively (d¹⁰, no redox cycling) |
| Ionic radius (Zn²⁺) | 0.074 nm (74 pm) |
| Preferred coordination | Tetrahedral (4-coordinate, sometimes 5 or 6) |
| Coordinating ligands | Cys (thiolate), His (imidazole), Asp/Glu (carboxylate), H₂O |
| Electronegativity (Pauling) | 1.65 |

### Zinc-Finger Protein Families

The zinc finger is the most prevalent small metal-binding domain in the human proteome. Approximately **2500 human proteins** (~10% of the human proteome) contain zinc-coordinating domains. The major structural classes are:

| Class | Ligands | Representative proteins | Function |
|:---|:---|:---|:---|
| **Cys₂His₂ (C2H2)** | 2 Cys + 2 His tetrahedral | SP1, WT1, TFIIIA, Krüppel-like factors | DNA-binding transcription factors |
| **Cys₄ (C4 nuclear receptor)** | 4 Cys per finger | GR, AR, ERα, RAR, VDR, TR | Ligand-activated nuclear receptors; two fingers, one binds Zn²⁺ per finger |
| **RING domain** | 8 Cys/His, two Zn²⁺ per domain | BRCA1, MDM2, TRAF family | E3 ubiquitin ligase scaffold |
| **LIM domain** | 8 Cys/His, two Zn²⁺ | Zyxin, LMO2, PINCH | Cytoskeletal organisation, development |
| **PHD finger** | 8 Cys/His | ING2, BPTF, RAG2 | Histone reader (H3K4me3 recognition) |
| **FYVE domain** | 8 Cys | SARA, EEA1, ESCRT | Phosphoinositide binding, endosome targeting |

In each case, Zn²⁺ **does not participate directly in catalysis** within zinc-finger domains — it acts purely as a structural template, pre-organising the polypeptide chain into a compact fold capable of making sequence-specific contacts with DNA, RNA, or protein partners.

### Zinc in Enzyme Active Sites

In **catalytic zinc sites**, Zn²⁺ acts as a Lewis acid to:
1. Activate water for nucleophilic attack (serine protease-like mechanism without the serine)
2. Polarise carbonyl groups for hydrolysis
3. Stabilise negatively charged transition states and reaction intermediates

Key coordination geometries: three protein ligands (typically His₂Asp or His₃) plus one water molecule complete the tetrahedral coordination sphere; the Zn²⁺-bound water has a pKa of ~7 (versus ~15.7 for free water), providing a Zn-OH⁻ nucleophile at physiological pH.

## Function

### Catalytic Roles: Major Zinc Metalloenzymes

| Enzyme | Zn²⁺ role | Reaction | Clinical relevance |
|:---|:---|:---|:---|
| **Carbonic anhydrase II** | Activates H₂O → Zn-OH⁻ | CO₂ + H₂O ⇌ H₂CO₃ → H⁺ + HCO₃⁻ | RBC CO₂ transport; renal acid-base; inhibited by acetazolamide |
| **Carboxypeptidase A** | Polarises substrate C=O | Hydrolysis of C-terminal residues from peptides | Pancreatic digestion |
| **Alcohol dehydrogenase (ADH)** | Activates substrate by coordination to Zn²⁺ | Ethanol → acetaldehyde (NAD⁺ reduction) | Ethanol metabolism; first-pass liver |
| **Matrix metalloproteinases (MMPs)** | Zn²⁺ in catalytic domain | Extracellular matrix (collagen, gelatin) hydrolysis | Wound healing, metastasis, atherosclerosis |
| **Alkaline phosphatase** | Two Zn²⁺ + one Mg²⁺ | Dephosphorylation at pH 8–10 | Liver/bone marker; ALP elevation in cholestasis/Paget disease |
| **Angiotensin-converting enzyme (ACE)** | Two Zn²⁺ per molecule | Ang I (10-AA) → Ang II (8-AA); cleaves bradykinin | Hypertension target; ACE inhibitors chelate the Zn²⁺ |
| **δ-aminolevulinic acid dehydratase** | Zn²⁺ stabilises active site | ALA condensation step of haem synthesis | Inhibited by lead (Pb²⁺ displaces Zn²⁺) → anaemia |

Zinc is thus embedded in **every major metabolic pathway**: energy metabolism (glycolysis intermediates), nucleic acid metabolism (RNA polymerase, DNA polymerase), protein digestion (carboxypeptidase, MMPs), CO₂ transport (carbonic anhydrase), and hormone regulation (ACE, insulin storage) [^vallee-zinc-enzymes].

### Structural Roles: Zinc-Finger Transcription Factors and Nuclear Receptors

In zinc-finger transcription factors such as SP1 (promoter elements), WT1 (kidney development), and TFIIIA (5S rRNA gene), Cys₂His₂ fingers fold into a ββα motif stabilised by Zn²⁺ coordination. Each finger recognises 3 bp of DNA in the major groove. The number of fingers varies (3 in SP1 exon, 9 in TFIIIA), enabling graded DNA-binding specificity [^stryer-biochemistry].

Nuclear receptors (GR, AR, ERα, RAR, VDR, TR) use a **Cys₄ zinc-finger pair** to bind hormone response elements as homodimers or heterodimers. The D-box (in the second finger) mediates receptor dimerisation and positions the DNA recognition helix of the first finger at the correct register over the half-site AGGTCA or AGAACA sequence. This entire mechanism — and hence the response of the body to glucocorticoids, sex steroids, thyroid hormone, vitamin D, and retinoids — absolutely requires Zn²⁺ [^vallee-zinc-enzymes].

### Zinc and Insulin Storage

Pancreatic β-cells synthesise insulin as a hexamer containing **3 Zn²⁺ ions**. Each Zn²⁺ is octahedrally coordinated by His10 residues from two insulin monomers at the hexamer's 3-fold axis, with three water molecules completing the coordination. Hexameric crystallisation raises the local density of insulin in the secretory granule to near-crystalline packing, enabling β-cells to store massive amounts of insulin in a compact volume. Upon exocytosis, the hexamer dissociates in the low-Zn²⁺ environment of portal blood, releasing monomers that bind the insulin receptor. The co-released Zn²⁺ may exert local paracrine effects on α-cells, suppressing glucagon secretion [^stryer-biochemistry].

### Zinc and Immunity

Zinc is **indispensable for immune function** at multiple levels [^prasad-zinc-immunity]:

- **Thymopoiesis:** Thymulin (facteur thymique sérique, FTS) is a nonapeptide produced by thymic epithelial cells that requires Zn²⁺ for biological activity. Thymulin promotes T-cell differentiation, interleukin-2 production, and thymocyte maturation. Zinc deficiency selectively impairs thymulin activity and causes thymic involution.
- **Lymphocyte proliferation:** Zn²⁺ is required for DNA replication (DNA polymerases contain zinc), for transcription factor function, and as a co-mitogen. Zinc-deficient lymphocytes fail to proliferate normally in response to mitogens.
- **Innate immunity:** Zn²⁺ inhibits NF-κB (by stabilising its inhibitor, IκB-α) and reduces pro-inflammatory cytokine production (TNFα, IL-1β, IL-6); paradoxically, zinc is also required for optimal macrophage killing of intracellular pathogens via zinc-mediated toxicity ("zinc shock" at the phagosome).
- **NK cells:** Natural killer cell cytotoxicity is markedly reduced by zinc deficiency; restoration with zinc supplementation normalises NK activity.
- **Antibody production:** B-cell function and immunoglobulin production require zinc for transcription factor activity (including NF-κB isoforms in B-cell signalling).

### Zinc Homeostasis: Absorption, Transport, and Excretion

Dietary zinc is absorbed in the proximal small intestine via **Zip4 (SLC39A4)** — a high-affinity Zn²⁺ importer expressed on the apical surface of enterocytes. Inside enterocytes, **metallothionein (MT)** — a cysteine-rich, ~6–7 kDa protein that can bind 7 Zn²⁺ (or Cd²⁺) — sequesters excess zinc, providing a buffer against acute Zn²⁺ overload. Metallothionein-bound zinc is lost in faecal shed enterocytes, making intestinal retention a key homeostatic mechanism.

Export from enterocytes into portal blood is mediated by **ZnT1 (SLC30A1)** at the basolateral membrane. In plasma, ~85% of zinc is bound to albumin (low-affinity, readily exchangeable), ~13% to α₂-macroglobulin, and ~2% is free or bound to amino acids (the fraction available for tissue uptake). Tissues import zinc via various Zip (SLC39) family importers and export excess zinc via ZnT (SLC30) family exporters.

Zinc excretion is primarily **faecal** (via pancreatic secretion and intestinal mucosa desquamation); urinary zinc is small (~0.5 mg/day) and relatively fixed regardless of dietary intake, so the kidney is not a major regulatory organ.

**Phytate** (inositol hexaphosphate) in plant foods chelates zinc with high affinity, dramatically reducing its bioavailability. This is why vegetarians and populations reliant on unleavened bread are at higher risk of zinc deficiency — phytate is present in grains, legumes, and nuts.

## Connections

- **Part of** → [Human body](../../08-whole-body/human-body/README.md): 2–4 g total Zn²⁺, distributed 60% muscle / 30% bone / 10% viscera; structural scaffold in ~2500 zinc-finger proteins and catalytic metal in >200 enzymes spanning all metabolic pathways.
- **Modulates** → [T-helper cell](../../04-cellular/t-helper-cell/README.md): Zinc is required for thymulin activity, T-cell maturation, IL-2 production, and proliferation; severe deficiency causes lymphopenia and selectively depletes T-helper (CD4+) cells.
- **Modulates** → [Insulin](../../03-molecular/insulin/README.md): 3 Zn²⁺ per hexamer in pancreatic β-cell granules crystallise insulin for dense storage; Zn²⁺ is co-secreted into portal blood and may suppress α-cell glucagon release locally.
- **Modulates** → [Immune system](../../07-system/immune-system/README.md): Zn²⁺ regulates NF-κB, thymulin, NK cell cytotoxicity, neutrophil oxidative burst, and B-cell antibody production; deficiency impairs both innate and adaptive arms.

## Pathology

### Zinc Deficiency

**Acrodermatitis enteropathica (AE)** is an autosomal recessive disorder caused by loss-of-function mutations in *SLC39A4* (Zip4). Without functional Zip4, intestinal zinc absorption is near-abolished, producing severe systemic zinc depletion that manifests as a classic triad: perioral and acral **dermatitis**, **diarrhoea**, and **alopecia**, accompanied by immune failure (recurrent infections), growth retardation, hypogonadism, and neuropsychiatric symptoms. The condition is fatal if untreated but responds completely to oral zinc supplementation (bypassing the need for Zip4 at supra-physiological concentrations).

**Acquired zinc deficiency** occurs in malabsorption syndromes (Crohn disease, coeliac disease, short bowel syndrome), alcoholic liver disease (reduced hepatic MT, increased urinary zinc loss), parenteral nutrition without adequate zinc, and in populations with high-phytate diets [^prasad-zinc-immunity]. Milder deficiency produces: growth retardation in children, hypogonadism, delayed wound healing, hypogeusia (taste loss — gustin/carbonic anhydrase VI is a zinc enzyme in saliva), immune dysfunction, and increased susceptibility to infections. Marginal zinc deficiency is estimated to affect >2 billion people globally and is particularly prevalent in sub-Saharan Africa and South Asia.

**Zinc and the common cold:** Multiple randomised trials and meta-analyses support a modest reduction in cold duration (~1–2 days) with zinc acetate lozenges begun within 24 hours of symptom onset; the proposed mechanism involves zinc inhibition of ICAM-1-mediated rhinovirus binding in the nasal mucosa.

### Zinc Toxicity

Acute zinc toxicity (>100 mg/day) produces nausea, vomiting, and epigastric pain. Chronic excess (>25–50 mg/day) causes **copper deficiency** by competitive inhibition — excess zinc induces intestinal metallothionein, which has higher affinity for copper than for zinc, trapping copper in shed enterocytes. Manifestations include microcytic anaemia (copper-dependent ceruloplasmin/ferroxidase is needed for iron loading onto transferrin), neutropenia, and myeloneuropathy mimicking B12 deficiency — a clinically well-documented syndrome in patients taking high-dose zinc supplements (e.g., for macular degeneration).

| Condition | Mechanism | Clinical features |
|:---|:---|:---|
| Acrodermatitis enteropathica | SLC39A4 (Zip4) mutation; zero intestinal Zn²⁺ absorption | Dermatitis, diarrhoea, alopecia, immune failure |
| Acquired deficiency | Malabsorption / high phytate diet / alcoholism | Growth retardation, hypogonadism, hypogeusia, immune suppression |
| Zinc-induced copper deficiency | MT trapping of Cu in enterocytes | Anaemia, neutropenia, myeloneuropathy |
| Lead poisoning (occupational) | Pb²⁺ displaces Zn²⁺ from δ-ALA-dehydratase | Sideroblastic anaemia, basophilic stippling |

## See Also

- [Insulin](../../03-molecular/insulin/README.md) — hexameric storage requires Zn²⁺.
- [T-helper cell](../../04-cellular/t-helper-cell/README.md) — Zn²⁺-dependent maturation via thymulin.
- [Immune system](../../07-system/immune-system/README.md) — broad Zn²⁺ regulation of innate and adaptive immunity.
- [Copper](../../02-atomic/copper/README.md) — competes with Zn²⁺ for intestinal absorption via metallothionein.

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
[^vallee-zinc-enzymes]: Vallee BL, Falchuk KH. The biochemical basis of zinc physiology. *Physiol Rev.* 1993;73(1):79-118. [doi:10.1152/physrev.1993.73.1.79](https://doi.org/10.1152/physrev.1993.73.1.79) · [PubMed 8380364](https://pubmed.ncbi.nlm.nih.gov/8380364/)
[^prasad-zinc-immunity]: Prasad AS. Zinc in human health: effect of zinc on immune cells. *Mol Med.* 2008;14(5-6):353-7. [doi:10.2119/2008-00033.Prasad](https://doi.org/10.2119/2008-00033.Prasad) · [PubMed 18385818](https://pubmed.ncbi.nlm.nih.gov/18385818/)
