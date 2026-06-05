---
schema: human-scale-entry/v1
id: hydrogen
name: Hydrogen
atlas: 01-human
scale: 02-atomic
status: draft
last_reviewed: 2026-06-05
summary: "H, atomic number 1. Most abundant element in the body by atom count; essential constituent of water (H₂O), all organic molecules, and hydrogen bonds stabilising DNA and protein secondary structure. H⁺ (proton) gradient across the inner mitochondrial membrane drives ATP synthesis."
aliases: ["H", "¹H", "protium", "deuterium", "H⁺", "hydrogen bond donor"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: mitchell-1961-chemiosmosis
    type: peer-reviewed
    cite: "Mitchell P. Coupling of phosphorylation to electron and hydrogen transfer by a chemi-osmotic type of mechanism. Nature. 1961;191:144-8."
    doi: "10.1038/191144a0"
    pmid: "13771349"
    url: "https://doi.org/10.1038/191144a0"
cross_links:
  - target: 01-human/01-subatomic/proton
    relation: contains
    note: "The hydrogen atom (¹H) consists of one proton and one electron. As H⁺ it is the sole bare nuclear species free in aqueous chemistry. Proton transfer (Brønsted acid–base) is the basis of enzyme catalysis, pH buffering, and the mitochondrial proton-motive force."
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "Hydrogen is the most abundant element by atom count (~60% of atoms), as the body is ~60% water by mass. Every water molecule, every C–H bond in lipids, every N–H in peptide bonds and amino groups, and every O–H in hydroxyl and carboxyl groups contains hydrogen."
  - target: 01-human/03-molecular/atp
    relation: modulates
    note: "The H⁺ electrochemical gradient (pmf) across the inner mitochondrial membrane drives F₀F₁-ATP synthase: proton flow through the F₀ c-ring rotates the γ-stalk, synthesising ATP in the F₁ head via Boyer's binding-change mechanism — ~28 of ~32 ATP per glucose."
---

# Hydrogen

## Overview

Hydrogen (symbol H, atomic number 1, atomic mass 1.008 u) is the lightest and simplest element in the periodic table: one proton, one electron, no neutrons (in the most abundant isotope, ¹H, protium). It is the **most abundant element in the universe** and the **most abundant element in the human body by atom count**, comprising approximately 60% of all atoms in a 70 kg adult — primarily as the two hydrogen atoms in each water molecule [^stryer-biochemistry].

Despite its structural simplicity, hydrogen is functionally indispensable at every biological scale:

- **Atomic/molecular level:** H atoms form C–H, N–H, and O–H bonds that are the covalent scaffolding of all biomolecules.
- **Non-covalent level:** Hydrogen bonds (N–H···O, O–H···N, O–H···O, O–H···S) are the dominant stabilising interactions in protein secondary and tertiary structure, DNA base pairing, RNA folding, and carbohydrate conformation.
- **Ionic level:** As H⁺ (proton), hydrogen is the transported species in the mitochondrial electrochemical gradient that drives ATP synthesis, the lysosomal acidification pump, and gastric acid secretion.

Hydrogen was identified as a distinct element by Henry Cavendish in 1766, who described it as "inflammable air." Antoine Lavoisier named it hydrogen (Greek: hydro = water, genes = forming) in 1783. Peter Mitchell's 1961 proposal that proton gradients — hydrogen ions moving down their electrochemical potential — couple the electron transport chain to ATP synthesis was the last major conceptual advance in understanding hydrogen's central bioenergetic role [^mitchell-1961-chemiosmosis].

## Structure

### Atomic Properties

| Property | Value |
|:---|:---|
| Atomic number (Z) | 1 |
| Atomic mass (¹H) | 1.00794 u |
| Electron configuration | 1s¹ |
| Electronegativity (Pauling) | 2.20 |
| Ionic form | H⁺ (proton; loses sole electron) or H⁻ (hydride; gains one electron) |
| Covalent radius | 31 pm |
| van der Waals radius | 120 pm |
| Standard oxidation states | +1 (in most compounds), −1 (hydride, e.g., NADH) |

### Isotopes

| Isotope | Symbol | Nucleus | Abundance | Biological use |
|:---|:---|:---|:---|:---|
| Protium | ¹H | 1 proton | 99.985% | All biochemistry |
| Deuterium | ²H, D | 1 proton + 1 neutron | 0.015% | NMR, kinetic isotope effect studies, deuterium tracing |
| Tritium | ³H, T | 1 proton + 2 neutrons | Trace (radioactive) | Autoradiography, radioimmunoassay |

Deuterium is used in isotope tracer studies because C–D bonds have a slightly longer half-life than C–H bonds (kinetic isotope effect, KIE ~2–7), enabling discrimination of metabolic pathways. ²H-NMR and ²H₂O dilution are also used to measure total body water in clinical nutrition research.

### The Hydrogen Bond

A hydrogen bond forms when a hydrogen atom covalently bonded to an electronegative atom (donor: N, O, F) is attracted to a second electronegative atom (acceptor: N, O, S). The donor atom polarises the N–H or O–H bond, placing a partial positive charge (δ+) on H and allowing electrostatic attraction to the lone pair of the acceptor.

| Hydrogen bond type | Bond energy | Biological context |
|:---|:---:|:---|
| O–H···O | 20–25 kJ/mol | Water; serine/threonine H-bonds to backbone |
| N–H···O | 15–20 kJ/mol | Peptide backbone α-helix and β-sheet |
| N–H···N | 10–15 kJ/mol | DNA base pairing (A···T: 2 bonds; G···C: 3 bonds) |
| O–H···N | 15–20 kJ/mol | Enzyme active sites; tRNA tertiary structure |

Although each hydrogen bond is individually 5–30 kJ/mol (compared to C–C covalent bonds at ~347 kJ/mol), macromolecular structures contain hundreds to thousands of hydrogen bonds in concert. The double helix of a typical gene contains ~10⁶ hydrogen bonds; the protein folding energy of a 300-residue protein is dominated by the net difference between hydrogen bonds within the folded protein and those with surrounding water.

## Function

### Water and Body Fluid Composition

Approximately 63% of body mass is water (H₂O). At physiological temperature and ionic strength, liquid water has unique properties arising from its extensive hydrogen-bond network:

- **High heat capacity (4.18 J/g·°C):** Blood and intracellular water buffer thermal fluctuations from metabolism.
- **High dielectric constant (ε ≈ 80):** Stabilises separated ions in solution (Na⁺, K⁺, Ca²⁺, Cl⁻), enabling ionic physiology.
- **Cohesion and surface tension:** Drive capillary action in small vessels and maintain alveolar surface film properties in concert with surfactant.
- **Solvent for polar biomolecules:** Hydrophilic interactions orient lipid bilayers (hydrophobic effect), position ligands in enzyme active sites, and dissolve metabolites.

The hydrogen bond between water molecules (O–H···O) is directional and constantly breaking and reforming on the picosecond timescale at 37°C, giving water its liquid character while maintaining local order.

### Organic Biomolecule Backbone

Hydrogen is the second most abundant element in biomolecules by atom count after carbon. Every organic molecule in the body contains C–H bonds:

- **Carbohydrates:** Glucose (C₆H₁₂O₆) — 12 hydrogen atoms per molecule. The glycolytic intermediates and Krebs cycle substrates are all C–H–O compounds.
- **Lipids:** Fatty acids (e.g., palmitic acid C₁₆H₃₂O₂) are largely C–H chains. The high caloric density of fat (9 kcal/g) reflects the highly reduced (hydrogen-rich) state of these molecules — oxidising their C–H bonds releases far more energy than oxidising carbohydrates.
- **Proteins:** Every amino acid contains C–H bonds and at least one N–H bond (the α-amino group and the peptide bond N–H). The peptide bond C=O···H–N hydrogen bond is the structural unit of secondary structure.
- **Nucleic acids:** The Watson-Crick base pairs are hydrogen bond patterns: A:T (2 H-bonds), G:C (3 H-bonds). The major and minor grooves of B-form DNA present N–H and C–H donors accessible to proteins and drugs.

### Hydride Transfer and Redox Chemistry

In oxidoreductive metabolism, hydrogen is transferred not only as H⁺ (proton) but as H⁻ (hydride — a proton + 2 electrons):

- **NAD⁺/NADH:** Accepts hydride (H⁻) from glucose, fatty acids, and amino acids during oxidative metabolism. The nicotinamide ring accepts H⁻ at C4. This is the dominant electron carrier feeding the mitochondrial ETC.
- **FADH₂:** FAD accepts 2H (1H⁺ + 1H⁻ equivalent) from succinate in the TCA cycle. Feeds electrons into CoQ (Complex II), with lower free energy yield than NADH.
- **NADPH:** Carries reducing equivalents (H⁻) for biosynthesis (fatty acid synthesis, cholesterol synthesis) and antioxidant defence (glutathione reductase).

### Proton Gradient and ATP Synthesis

As H⁺, hydrogen is the species transported to build the mitochondrial electrochemical gradient. Complexes I, III, and IV of the ETC pump protons from the matrix into the intermembrane space. The resulting pmf (~200 mV equivalent) drives proton re-entry through ATP synthase, phosphorylating ADP to ATP [^mitchell-1961-chemiosmosis]. Each proton flowing through the F₀ c-ring contributes fractionally to the 120° rotation of the γ-subunit stalk that sequentially activates the three β-subunits of F₁ — Boyer's binding-change mechanism.

Per molecule of glucose: approximately 10 NADH + 2 FADH₂ produced → ~28 ATP from oxidative phosphorylation (plus ~4 from substrate-level phosphorylation). The entire process depends on the ability to move H⁺ across a membrane — a function that leverages hydrogen's unique property of existing as a bare nucleus (proton) in water.

### Hydrogen in Acid–Base Physiology

| Compartment | pH | [H⁺] |
|:---|:---:|:---:|
| Arterial blood | 7.38–7.42 | 38–42 nmol/L |
| Cytosol (most cells) | ~7.2 | ~63 nmol/L |
| Mitochondrial matrix | ~8.0 | ~10 nmol/L |
| Lysosome | ~4.5–5.0 | ~31–100 µmol/L |
| Gastric juice | ~1.5 | ~32 mmol/L |

The body maintains blood pH within the narrow range 7.35–7.45 through the bicarbonate buffer system, respiratory CO₂ control, and renal H⁺ excretion (as NH₄⁺ and H₂PO₄⁻).

## Connections

- **Contains** → [Proton](../../01-subatomic/proton/README.md): The proton is the nucleus of hydrogen. In solution, H⁺ is the proton, the fundamental H-transferring species in acid–base chemistry and the chemiosmotic coupling of ATP synthesis.

- **Part-of** → [Human Body](../../08-whole-body/human-body/README.md): Hydrogen is the most abundant element in the body by atom count. It is present in every molecule of water, every C–H and N–H and O–H bond, and every hydrogen bond in every macromolecule.

- **Modulates** → [ATP](../../03-molecular/atp/README.md): The H⁺ electrochemical gradient (pmf) across the inner mitochondrial membrane is the driving force for F₀F₁-ATP synthase, converting the kinetic energy of proton flow into the chemical energy of the ATP phosphoanhydride bond.

## Pathology

| Condition | Hydrogen mechanism |
|:---|:---|
| **Metabolic acidosis** | Excess H⁺ (lactic acid, ketoacids, uraemic acids); blood pH < 7.35; inhibits cardiac contractility, causes kalaemia dysregulation (H⁺/K⁺ exchange across cell membranes) |
| **Respiratory alkalosis** | Hyperventilation removes CO₂, raising blood pH; cerebrovascular constriction, paraesthesia, tetany (reduced ionised Ca²⁺) |
| **Dehydration** | Reduction in total body H₂O reduces plasma volume → haemoconcentration, increased blood viscosity, impaired renal perfusion |
| **Mitochondrial complex deficiency** | Impaired ETC proton pumping → reduced pmf → insufficient ATP synthesis → energy failure in heart, brain, and muscle |
| **Ischaemia–reperfusion injury** | Intracellular acidosis during ischaemia activates Na⁺/H⁺ exchanger (NHE1); Na⁺ overload → Ca²⁺ overload via NCX reverse mode on reperfusion → myocardial stunning or infarction |

## Open Questions

- **Hydrogen molecular medicine:** Inhalation of H₂ gas or drinking H₂-dissolved water has been reported to reduce oxidative stress and ischaemia–reperfusion injury in animal models, putatively via selective scavenging of hydroxyl radicals. Rigorous human clinical trial data are lacking.
- **Quantum tunnelling in enzyme catalysis:** A subset of enzyme-catalysed proton and hydride transfers show unusually large kinetic isotope effects, suggesting quantum mechanical tunnelling through the energy barrier rather than classical over-barrier transfer. The extent to which tunnelling contributes to catalytic rates in vivo is debated.
- **Deuterium depletion:** The ratio of ²H/¹H (deuterium/protium) in body water reflects dietary intake; some researchers propose that deuterium-depleted water improves mitochondrial function by reducing the kinetic isotope effect on ATP synthase rotation. The evidence base is preliminary.

## See Also

- [Proton](../../01-subatomic/proton/README.md) — the nucleus of the hydrogen atom; the unit of H⁺ transfer.
- [ATP](../../03-molecular/atp/README.md) — the molecule whose synthesis is powered by the proton gradient.
- [Human Body](../../08-whole-body/human-body/README.md) — hydrogen's macroscopic context as the most abundant element.

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^mitchell-1961-chemiosmosis]: Mitchell P. Coupling of phosphorylation to electron and hydrogen transfer by a chemi-osmotic type of mechanism. *Nature.* 1961;191:144-8. [doi:10.1038/191144a0](https://doi.org/10.1038/191144a0) · [PubMed 13771349](https://pubmed.ncbi.nlm.nih.gov/13771349/)
