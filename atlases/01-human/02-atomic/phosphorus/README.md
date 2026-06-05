---
schema: human-scale-entry/v1
id: phosphorus
name: Phosphorus
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "Phosphorus (P, Z=15, [Ne] 3s² 3p³). 4th most abundant element by body mass (~1.1%, ~770g). 85% in bone as hydroxyapatite, 14% soft-tissue (ATP, nucleic acids, phospholipids), 1% extracellular Pi (0.8–1.5 mmol/L serum)."
aliases: ["P", "phosphate", "inorganic phosphate", "Pi", "phosphorus-31"]
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
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "~1.1% body mass (~770g in 70kg adult); 85% in bone/teeth as hydroxyapatite, ~14% soft tissue (ATP, nucleic acids, phospholipids), ~1% extracellular as inorganic phosphate (Pi, serum 0.8–1.5 mmol/L)."
  - target: 01-human/03-molecular/atp
    relation: part-of
    note: "Phosphorus forms all 3 phosphate groups of ATP; α-β and β-γ phosphoanhydride bonds each store ~30 kJ/mol. Hydrolysis by ATPases drives muscle contraction, active transport, and biosynthesis."
  - target: 01-human/04-cellular/hepatocyte
    relation: part-of
    note: "Phospholipid membranes, phosphorylation signaling, and ATP regeneration via gluconeogenesis and glycolysis are all critical to hepatocyte function; hepatocytes also synthesize phosphoproteins for export."
  - target: 01-human/05-tissue/bone-marrow
    relation: modulates
    note: "Phosphate fuels haematopoietic progenitor energy metabolism (Mg-ATP) and provides nucleotides for DNA replication during rapid cell proliferation in bone marrow."
---

# Phosphorus

## Overview

Phosphorus (symbol P, atomic number 15, atomic mass 30.97 u) is a nonmetallic element belonging to Group 15 of the periodic table, with ground-state electron configuration [Ne] 3s² 3p³. It is the **fourth most abundant element by mass in the human body** (~1.1%, roughly 770 g in a 70 kg adult), exceeded only by oxygen, carbon, and hydrogen. Unlike many biologically important ions that exist at trace or micromolar concentrations, phosphorus is a structural component of virtually every macromolecule class: it forms the backbone of DNA and RNA, the high-energy bonds of ATP, and the head groups of membrane phospholipids [^stryer-biochemistry].

Phosphorus in biology exists almost exclusively as **orthophosphate** (PO₄³⁻) and its protonated forms. The ionization equilibria of phosphoric acid (H₃PO₄ → H₂PO₄⁻ → HPO₄²⁻ → PO₄³⁻, pKa values 2.1, 7.2, 12.4) are critically important: at physiological pH ~7.4, the H₂PO₄⁻/HPO₄²⁻ pair (pKa 7.2) functions as the **major intracellular and urinary buffer**, resisting pH swings in the renal tubular fluid and cytoplasm alike [^guyton-hall].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 15 |
| Atomic mass | 30.97 u |
| Electron configuration | [Ne] 3s² 3p³ |
| Common valence | +5 (in phosphate esters, anhydrides) |
| Electronegativity (Pauling) | 2.19 |
| Oxidation states in biology | +5 (phosphate esters), +3 (phosphonates) |

### Phosphate Chemistry in Biological Contexts

Phosphorus achieves its versatility through five bonding capacity. In the body, phosphate appears in several forms:

| Form | Example | Bond type | Energy significance |
|:---|:---|:---|:---|
| Orthophosphate (Pi) | H₂PO₄⁻ / HPO₄²⁻ | — | Buffer, substrate for ATP synthesis |
| Phosphate ester | Glucose-6-phosphate, serine-P | P–O–C | Traps metabolites in cell, activates proteins |
| Phosphoanhydride | ATP α-β, β-γ | P–O–P | ~30 kJ/mol per bond; high-energy |
| Phosphodiester | DNA/RNA backbone | P–O–C–O–P | Structural; negatively charged at pH 7 |
| Pyrophosphate (PPi) | Released in many biosyntheses | P–O–P | Hydrolysis by pyrophosphatase drives reactions forward |

The **phosphoanhydride bond** of ATP is often called "high-energy," but this designation refers to the large negative ΔG° of hydrolysis (approximately −30.5 kJ/mol for the γ-phosphate), not to an intrinsically energetic bond. The large ΔG° arises from resonance stabilization of inorganic phosphate products and electrostatic repulsion relief between the negatively charged phosphate groups in ATP [^stryer-biochemistry].

### Hydroxyapatite — Bone Phosphorus

Eighty-five percent of body phosphorus resides in bone and teeth as **hydroxyapatite**, with stoichiometry Ca₁₀(PO₄)₆(OH)₂. This insoluble calcium phosphate mineral provides compressive strength to cortical bone (Young's modulus ~15–20 GPa) and acts as a vast reservoir — bone phosphate is exchangeable with plasma Pi over hours to days, allowing serum Pi to be maintained within its narrow physiological range (0.8–1.5 mmol/L in adults) even during dietary fluctuations [^guyton-hall].

## Function

### ATP and Cellular Energy Currency

The three phosphate groups of ATP — designated α, β, and γ counting from the adenosine — are the molecular mechanism by which cells store and spend chemical energy. The β-γ phosphoanhydride bond releases ~30 kJ/mol on hydrolysis (ATP → ADP + Pi), and the α-β bond releases a similar amount (ADP → AMP + Pi). These hydrolysis reactions are coupled to endergonic cellular work:

- **Muscle contraction**: myosin ATPase hydrolyses Mg-ATP, releasing phosphate and allowing the power stroke; without Pi release, the lever arm cannot swing.
- **Active transport**: Na⁺/K⁺-ATPase translocates 3 Na⁺ out and 2 K⁺ in per ATP consumed, maintaining cell resting potential and volume.
- **Biosynthesis**: fatty acid synthesis, gluconeogenesis, aminoacyl-tRNA charging, and DNA/RNA polymerization all consume ATP phosphoanhydride bonds.
- **Signal amplification**: GTP (a phosphate analogue) powers G-protein signaling; cAMP and cGMP (cyclic phosphodiesters) are second messengers.

### DNA and RNA Backbone

The phosphodiester backbone of nucleic acids consists of alternating phosphate and ribose (or deoxyribose) units, with each phosphate bridging the 3′-OH of one sugar to the 5′-OH of the next. This 3′-5′ phosphodiester linkage:

1. Imparts **structural rigidity** and a defined helical geometry to double-stranded DNA.
2. Creates a **polyanionic chain** (one negative charge per nucleotide at pH 7) that repels nucleases, stabilises the double helix through counter-ion condensation, and requires specific cation coordination (especially Mg²⁺) for folding of catalytic RNAs (ribozymes).
3. Is cleaved by nucleases (DNase, RNase) and exploited by restriction enzymes, all of which target the P–O bond.

Human diploid cells contain approximately 6 billion base pairs, each requiring one phosphorus atom — roughly **6 × 10⁹ phosphorus atoms per cell nucleus** in DNA alone, plus comparable amounts in cytoplasmic RNA [^stryer-biochemistry].

### Phospholipids and Membrane Architecture

All eukaryotic cell membranes consist predominantly of **glycerophospholipids** (phosphatidylcholine, phosphatidylethanolamine, phosphatidylserine, phosphatidylinositol) and sphingomyelin, in which a phosphate group links the glycerol (or sphingosine) backbone to a hydrophilic head group. The phosphate moiety:

- Creates the **amphipathic character** enabling bilayer self-assembly.
- Provides an anionic surface (particularly on the cytoplasmic leaflet via phosphatidylserine) that recruits cationic signaling proteins (PKC, annexins).
- In **phosphatidylinositol 4,5-bisphosphate (PIP2)**: cleavage by phospholipase C generates inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) — the canonical second messengers of Gq-coupled receptor signaling, triggering Ca²⁺ release from ER (via IP3R) and PKC activation (DAG) [^stryer-biochemistry].

### Protein Phosphorylation — the Master Regulatory Switch

Over 500 human kinases add a phosphate group from ATP to hydroxyl-bearing residues — **serine** (most common), **threonine**, or **tyrosine** — in a reversible reaction reversed by phosphatases. Phosphorylation alters protein conformation, activity, localization, and protein-protein interactions:

- **Signal transduction cascades**: receptor tyrosine kinases (EGFR, PDGFR) autophosphorylate on Tyr, recruiting SH2-domain effectors; MAP kinase cascades (Ras-Raf-MEK-ERK) amplify mitogenic signals.
- **Metabolic regulation**: phosphorylation of glycogen phosphorylase (by PKA, activated by glucagon/epinephrine) activates glycogen breakdown; simultaneous phosphorylation of glycogen synthase inhibits synthesis — a reciprocal hormonal switch.
- **Cell cycle control**: CDK-mediated phosphorylation of Rb releases E2F transcription factors, committing cells to S phase.

### Phosphate Homeostasis — Hormonal Regulation

Serum Pi is tightly regulated by three hormones acting primarily on intestine, kidney, and bone:

| Hormone | Source | Effect on Pi |
|:---|:---|:---|
| PTH | Parathyroid glands | ↑ renal Pi excretion (↓ NaPi-IIa/IIc cotransporters in proximal tubule); ↑ 1α-hydroxylase → calcitriol synthesis → ↑ GI absorption |
| FGF23 | Osteocytes (bone) | ↓ tubular Pi reabsorption (↓ NaPi-IIa/IIc); ↓ 1α-hydroxylase; requires Klotho co-receptor |
| Calcitriol (1,25(OH)₂D₃) | Kidney | ↑ intestinal Pi absorption via NaPi-IIb in enterocytes; ↑ bone resorption |

FGF23 and PTH are regulated in a feedback loop: rising Pi stimulates FGF23 and PTH secretion; rising calcitriol feeds back to suppress PTH [^guyton-hall].

## Connections

- **Part-of** → [Human Body](../../08-whole-body/human-body/README.md): ~1.1% body mass (~770g in 70 kg adult); 85% in bone/teeth as hydroxyapatite, ~14% soft tissue (ATP, nucleic acids, phospholipids), ~1% extracellular as inorganic phosphate (serum 0.8–1.5 mmol/L).
- **Part-of** → [ATP](../../03-molecular/atp/README.md): Phosphorus forms all 3 phosphate groups of ATP; α-β and β-γ phosphoanhydride bonds each store ~30 kJ/mol; hydrolysis by ATPases drives muscle contraction, active transport, and biosynthesis across all cell types.
- **Part-of** → [Hepatocyte](../../04-cellular/hepatocyte/README.md): Phospholipid membranes, phosphorylation signaling, and ATP regeneration via gluconeogenesis and glycolysis are all critical to hepatocyte function; hepatocytes also synthesize phosphoproteins (albumin, clotting factors) for export.
- **Modulates** → [Bone Marrow](../../05-tissue/bone-marrow/README.md): Phosphate fuels haematopoietic progenitor energy metabolism (Mg-ATP) and provides nucleotides for rapid DNA replication during the high-turnover cell proliferation that produces billions of blood cells daily.

## Pathology

| Condition | Mechanism | Key features |
|:---|:---|:---|
| **X-linked hypophosphataemia (XLH)** | Loss-of-function *PHEX* mutation → FGF23 excess → chronic renal Pi wasting | Rickets/osteomalacia in children; bowing deformity; dental abscesses; treated with burosumab (anti-FGF23 mAb) |
| **Refeeding syndrome** | Acute hypophosphataemia when carbohydrate refeeding after starvation drives Pi into cells (glycolysis, ATP synthesis) | Cardiac arrhythmias, respiratory failure, haemolytic anaemia; can be fatal if Pi falls below ~0.3 mmol/L |
| **CKD-related hyperphosphataemia** | Reduced renal Pi excretion → elevated Pi → ↑ FGF23 (early), then frank hyperphosphataemia; Pi × Ca product drives vascular calcification | Accelerated cardiovascular disease; secondary hyperparathyroidism; treated with dietary restriction and Pi binders |
| **Diabetic ketoacidosis (DKA)** | Insulin deficiency + osmotic diuresis → total body Pi depletion; apparent hyperphosphataemia may mask true deficit | Hypophosphataemia emerges during insulin therapy; may impair respiratory muscle function and erythrocyte 2,3-BPG synthesis |
| **Tumour-induced osteomalacia (TIO)** | FGF23-secreting mesenchymal tumours → renal Pi wasting → osteomalacia | Difficult to localise tumour; treated surgically; octreotide/burosumab used if surgery fails |

## See Also

- [ATP](../../03-molecular/atp/README.md) — the primary molecular vehicle of phosphate-bond energy.
- [Hepatocyte](../../04-cellular/hepatocyte/README.md) — central hub for phospholipid synthesis and phosphate metabolism.
- [Bone Marrow](../../05-tissue/bone-marrow/README.md) — haematopoietic tissue dependent on phosphate for nucleotide synthesis.
- [Human Body](../../08-whole-body/human-body/README.md) — whole-body phosphorus compartments and balance.
- [Calcium](../calcium/README.md) — inextricably linked: hydroxyapatite Ca₁₀(PO₄)₆(OH)₂, PTH, calcitriol regulate both ions together.

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^guyton-hall]: Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. [elsevier.com](https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8)
