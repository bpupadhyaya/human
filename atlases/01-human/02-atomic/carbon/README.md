---
schema: human-scale-entry/v1
id: carbon
name: Carbon
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "C, atomic number 6. Chemical backbone of all organic molecules. 18% of human body mass. sp³/sp²/sp hybridisation enables the tetrahedral, planar, and linear geometries underlying carbohydrate, lipid, protein, and nucleic acid architecture."
aliases: ["C", "carbon-12", "¹²C", "carbon backbone", "organic carbon"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Carbon is 18% of body mass (second to oxygen at 65%), the structural backbone of all macromolecules. A 70 kg adult contains ~12.6 kg carbon distributed across proteins (~43%), lipids (~33%), carbohydrates (~2%), nucleic acids (~1%), and metabolites."
  - target: 01-human/03-molecular/insulin
    relation: part-of
    note: "Insulin (51 residues, MW 5808 Da) is built entirely on carbon backbones: the α-carbon of each residue, side-chain carbons, and the carbonyl carbon of every peptide bond. Disulfide bonds crosslink carbon-bearing cysteine residues, defining the hormone's active 3D conformation."
---

# Carbon

## Overview

Carbon (symbol C, atomic number 6, atomic mass 12.011 u) is the fourth most abundant element in the universe by mass and the **second most abundant element in the human body by mass**, constituting approximately 18% of total body weight. More importantly, carbon is the **chemical foundation of all life**: it is the universal backbone element of organic chemistry, and the entire discipline of biochemistry can be understood as the chemistry of carbon-containing compounds in aqueous, physiological environments [^stryer-biochemistry].

The reason carbon is uniquely suited to this role lies in four properties that no other element combines in the same way:

1. **Tetravalence:** Carbon has four valence electrons and forms four covalent bonds of comparable strength, allowing it to bond to itself and to H, N, O, S, and P simultaneously.
2. **Hybridisation flexibility:** sp³, sp², and sp hybridisation give carbon atoms tetrahedral, trigonal planar, and linear geometries — enabling the full architectural diversity of biomolecules.
3. **Bond strength and stability:** C–C bonds (347 kJ/mol), C–H bonds (413 kJ/mol), C=C double bonds (614 kJ/mol), and C≡C triple bonds (839 kJ/mol) are thermodynamically stable under physiological aqueous conditions, allowing persistent molecular structures.
4. **Oxidation state range:** Carbon ranges from −4 (in methane) to +4 (in CO₂), enabling the full span of bioenergetic reactions from highly reduced fuel molecules (fats) to fully oxidised end products.

Carbon was recognised as a distinct element by Antoine Lavoisier in 1787, though it had been known since antiquity as charcoal, graphite, and diamond. The systematic chemistry of carbon compounds became organic chemistry in the nineteenth century (Kekulé's 1858 formulation of carbon's tetravalence; Fischer's glucose stereochemistry, 1891). The isotope ¹⁴C — radioactive, t₁/₂ = 5730 years — is the basis of radiocarbon dating and is used in metabolic tracer studies [^alberts-mol-cell-biology].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 6 |
| Atomic mass | 12.011 u |
| Electron configuration | [He] 2s² 2p² |
| Valence electrons | 4 |
| Electronegativity (Pauling) | 2.55 |
| Covalent radius | 77 pm (sp³) |
| Common oxidation states | −4 to +4 |
| Principal isotopes | ¹²C (98.9%), ¹³C (1.1%), ¹⁴C (trace, radioactive) |

### Hybridisation and Molecular Geometry

**sp³ hybridisation (tetrahedral, 109.5°):**
Four equivalent sp³ hybrid orbitals form four σ-bonds. The carbon atom at the centre of a tetrahedron. Exemplified by:
- Methane (CH₄) — the simplest organic molecule.
- Saturated fatty acids — long linear chains of sp³ CH₂ groups.
- The α-carbon of every amino acid — a tetrahedral stereocentre bearing four different substituents (except glycine).
- The anomeric carbon of monosaccharides (C1 of glucose — the site of O-glycosidic bond formation).

**sp² hybridisation (trigonal planar, 120°):**
Three sp² hybrid orbitals form three σ-bonds; one unhybridised p orbital forms a π-bond. Creates a planar double bond. Exemplified by:
- Peptide bond C=O and N–Cα — the peptide bond is planar due to partial double bond character (resonance), rigidifying the polypeptide backbone and constraining protein secondary structure.
- Purine and pyrimidine bases of nucleic acids — flat aromatic rings that stack via π–π interactions in B-DNA.
- Carbonyl groups (ketones, aldehydes, carboxylic acids, esters, amides) — the reaction centres of metabolic chemistry.
- Unsaturated fatty acids — cis double bonds (e.g., oleic acid, 18:1Δ⁹) introduce ~30° kinks that prevent crystalline packing, maintaining membrane fluidity.

**sp hybridisation (linear, 180°):**
Two sp hybrid orbitals form two σ-bonds; two unhybridised p orbitals form two π-bonds (triple bond). Exemplified by:
- CO₂ (linear O=C=O) — the end product of aerobic metabolism and the key molecule in bicarbonate buffering.
- Nitriles (C≡N) present in some toxic compounds (cyanide); rare in normal biochemistry.

## Function

### Carbon in Macromolecular Architecture

**Proteins:** Every amino acid contains a central α-carbon (Cα) in sp³ hybridisation bearing the amino group (–NH₂), carboxyl group (–COOH), hydrogen (–H), and a variable side chain (R group). The 20 standard amino acid side chains range from a single hydrogen (glycine) to aromatic rings (phenylalanine, tyrosine, tryptophan) to charged chains (glutamate, lysine). Peptide bond formation (condensation between –COOH and –NH₂) is catalysed by the ribosome and produces a planar, partial-double-bond linkage (C–N bond length 1.33 Å, between C–N single bond 1.45 Å and C=N double bond 1.29 Å), imposing the trans conformation in >99.9% of peptide bonds [^stryer-biochemistry].

**Nucleic acids:** The deoxyribose (in DNA) and ribose (in RNA) five-membered ring — C1 through C5 — is the carbon scaffold onto which bases attach (N-glycosidic bond at C1) and the phosphodiester backbone is assembled (via C3 3'-OH and C5 5'-phosphate). The purine and pyrimidine bases are flat, aromatic, carbon-nitrogen ring systems that base-stack via van der Waals forces and pair via hydrogen bonds.

**Lipids:** Fatty acid chains are predominantly C–H₂ (methylene) groups in sp³ hybridisation. The caloric density of fat (9 kcal/g) arises from the high degree of reduction (H:C ratio ~2:1 vs. ~1:1 for carbohydrates); β-oxidation of each two-carbon (acetyl-CoA) unit yields 10 ATP. Membrane phospholipids contain a glycerol backbone (3 carbons), two fatty acid chains, and a polar head group, all constructed on carbon skeletons.

**Carbohydrates:** Glucose (C₆H₁₂O₆) and all monosaccharides are polyhydroxylated aldehydes or ketones. Glycolysis converts one glucose to two pyruvates (C₃H₄O₃) through 10 enzymatic steps, each involving carbon skeleton rearrangement. The pentose phosphate pathway generates five-carbon sugars (ribose-5-phosphate) for nucleotide biosynthesis and NADPH for reductive chemistry.

### Carbon Flow in Metabolism: The Central Pathways

The carbon atoms of glucose (or fatty acids, or amino acids) are progressively oxidised:

1. **Glycolysis (cytosol):** Glucose (C₆) → 2 pyruvate (C₃). Net yield: 2 ATP, 2 NADH.
2. **Pyruvate decarboxylation (mitochondria):** Pyruvate (C₃) → acetyl-CoA (C₂) + CO₂. Loss of 1 carbon as CO₂.
3. **TCA cycle (mitochondria):** Acetyl-CoA (C₂) condenses with oxaloacetate (C₄) → citrate (C₆). Two decarboxylations per turn release 2 CO₂, regenerating oxaloacetate (C₄). Net yield per turn: 3 NADH, 1 FADH₂, 1 GTP.
4. **Oxidative phosphorylation:** NADH and FADH₂ donate electrons to the ETC; O₂ is the terminal acceptor → H₂O. ~28 ATP/glucose.

The carbon atoms that entered as glucose exit as CO₂, exhaled by the lungs. The ATP, synthesised using the proton gradient driven by electron transfer from these carbons, powers cellular work.

### Isotopic Carbon in Biological Research

- **¹⁴C labelling:** Radioactive carbon injected as labelled precursors (e.g., ¹⁴C-glucose, ¹⁴C-acetate) traces metabolic flux through pathways. Autoradiography or liquid scintillation counting localises ¹⁴C in tissues.
- **¹³C-NMR:** Stable isotope ¹³C tracing followed by NMR spectroscopy maps metabolic fluxes non-destructively; used in intact perfused heart experiments to measure TCA cycle activity and anaplerosis.
- **Radiocarbon dating:** The ¹⁴C/¹²C ratio in atmospheric CO₂ is incorporated into living organisms; after death, ¹⁴C decays (t₁/₂ = 5730 yr), allowing dating of organic remains. Applied clinically to estimate the age of forensic bone samples and, more recently, to measure cell turnover rates (neurogenesis studies using ¹⁴C from atmospheric nuclear tests).

### Carbon in Structural Biology

The backbone dihedral angles of polypeptides (φ, ψ around N–Cα and Cα–C bonds) define secondary structure:
- α-helix: φ ≈ −57°, ψ ≈ −47°
- β-sheet (antiparallel): φ ≈ −139°, ψ ≈ +135°
- These angles are constrained by the sp³ geometry of Cα and the planarity of the sp² peptide bond — a carbon hybridisation-driven geometric constraint encoded in the Ramachandran plot.

## Connections

- **Part-of** → [Human Body](../../08-whole-body/human-body/README.md): Carbon is 18% of body mass and the structural backbone of every biomolecule. A 70 kg adult contains ~12.6 kg of carbon.

- **Part-of** → [Insulin](../../03-molecular/insulin/README.md): Insulin's 51-amino-acid covalent structure is built entirely on carbon backbones; the α-carbon of each residue is the sp³ stereocentre defining peptide chain geometry, and the carbonyl carbons form every peptide bond.

## Pathology

| Condition | Carbon mechanism |
|:---|:---|
| **Cystic fibrosis** | CFTR mutations alter chloride/sodium transport; the carbon-based lipid membranes in airway epithelia accumulate mucus due to altered ion flux |
| **Diabetes mellitus** | Impaired glucose (C₆) metabolism; in T1DM, carbon is diverted to ketone body synthesis (acetoacetate, β-hydroxybutyrate, acetone) → ketoacidosis |
| **Carbon monoxide poisoning** | CO (C≡O) binds haemoglobin with 240× the affinity of O₂; blocks O₂ delivery; the carbon in CO originates from endogenous haem catabolism (normal signalling) or exogenous combustion (toxic) |
| **Cancer — Warburg effect** | Tumour cells divert carbon from oxidative phosphorylation to aerobic glycolysis and biosynthesis; ¹³C flux tracing reveals abnormal anaplerotic use of glutamine (C₅) to replenish TCA cycle |
| **Atherosclerosis** | Cholesterol (C₂₇H₄₆O) and lipid (fatty acid) carbon accumulate in arterial wall macrophages (foam cells); oxidised LDL carbon adducts trigger inflammatory signalling |

## Open Questions

- **One-carbon metabolism:** Transfer of single-carbon units (formyl, methylene, methyl groups) by folate and SAM-dependent enzymes underlies nucleotide synthesis, methylation reactions, and epigenetic control. The quantitative relationship between one-carbon metabolism, epigenetic programming, and disease risk in humans is not fully elucidated.
- **Carbon capture by the gut microbiome:** Colonic bacteria ferment dietary fibre (complex carbon polymers) to short-chain fatty acids (SCFA: acetate, propionate, butyrate — C₂, C₃, C₄). The metabolic and signalling contribution of microbiome-derived carbon to host energy balance and colon epithelial health is an active research field.
- **Allosteric carbon sensors:** Several metabolic enzymes may directly sense the local concentration of carbon intermediates (e.g., acetyl-CoA levels modulating histone acetyltransferases). The extent to which intracellular carbon metabolite concentrations act as direct epigenetic signals is under investigation.

## See Also

- [Human Body](../../08-whole-body/human-body/README.md) — carbon's macroscopic context.
- [Insulin](../../03-molecular/insulin/README.md) — a carbon-backbone protein whose structure and function illustrate carbon's role in biomolecular architecture.
- [ATP](../../03-molecular/atp/README.md) — the adenine base and ribose of ATP are carbon-containing structures; ATP's energy currency depends on the phosphoanhydride bond linked to an adenosine carbon scaffold.

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022. [ncbi.nlm.nih.gov/books/NBK26880](https://www.ncbi.nlm.nih.gov/books/NBK26880/)
