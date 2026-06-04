---
schema: human-scale-entry/v1
id: electron
name: Electron
atlas: 01-human
scale: 01-subatomic
status: draft
last_reviewed: 2026-06-03
summary: "The fundamental subatomic particle whose configuration governs all chemical bonding and reactivity in biology. Redox reactions are electron transfers; membrane potentials arise from charge separation; the mitochondrial electron transport chain generates the ATP that powers every heartbeat."
aliases: ["e⁻", "valence electron", "conduction electron"]
sources:
  - id: lodish-molecular-cell-biology
    type: textbook
    cite: "Lodish H, Berk A, Kaiser CA, et al. Molecular Cell Biology. 8th ed. W.H. Freeman; 2016. ISBN 978-1-4641-8339-3."
    url: "https://www.macmillanlearning.com/college/us/product/Molecular-Cell-Biology/p/1464183392"
    accessed: "2026-06-03"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019. ISBN 978-1-319-11467-1."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-03"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
    url: "https://doi.org/10.1038/415198a"
cross_links:
  - target: 01-human/02-atomic/calcium
    relation: modulates
    note: "Electron configuration of Ca (Z=20, [Ar]4s²) determines that it loses 2 electrons to form Ca²⁺ — the dominant biological ion. Electron density of binding site governs Ca²⁺ coordination by EF-hand proteins."
  - target: 01-human/03-molecular/troponin-complex
    relation: modulates
    note: "Electrostatic interactions (electron density differences) between Ca²⁺ and the EF-hand of troponin C drive the Ca²⁺-triggered conformational change that gates every heartbeat."
---

# Electron

## Overview

The electron (symbol e⁻) is a fundamental subatomic particle with charge −1.602 × 10⁻¹⁹ coulombs and mass 9.109 × 10⁻³¹ kg. In atoms, electrons occupy quantized orbital shells described by four quantum numbers (n, l, mₗ, mₛ). The **valence electrons** in the outermost shell determine all chemical reactivity — every covalent bond, every ionic attraction, every van der Waals interaction, and every hydrogen bond that holds biological molecules together is, at its core, an arrangement of electrons [^lodish-molecular-cell-biology].

In biology, the electron plays three categories of roles:

1. **Bonding** — electron sharing (covalent bonds) and transfer (ionic bonds) build every molecule in the body.
2. **Redox reactions** — transfer of electrons between molecules is the chemical definition of oxidation and reduction; metabolism is fundamentally a series of controlled electron transfers.
3. **Charge separation** — separation of charge across membranes creates the electrical potentials that drive nerve impulses, muscle contraction, ATP synthesis, and every heartbeat.

## Structure

The electron has no known internal structure — it is treated as a point particle in quantum electrodynamics. Its biological relevance comes from its wave-like behavior in atoms and molecules:

- In atomic orbitals (s, p, d, f), electrons occupy probability distributions (wavefunctions) that define bond angles and molecular geometry.
- **Electronegativity** — the tendency of an atom to attract electrons in a bond — arises from nuclear charge and orbital shielding; it generates the polar bonds (C=O, N–H, O–H) that enable hydrogen bonding, protein folding, and enzyme catalysis.
- **Orbital hybridization** (sp, sp², sp³) determines the geometry of carbon-containing biomolecules (linear, planar, tetrahedral), which governs enzyme active-site shape, receptor-ligand complementarity, and protein secondary structure.

## Function

### Redox and Metabolism

Every metabolic pathway involves electron transfer. The central principle:

- **Oxidation** = loss of electrons (or gain of oxygen / loss of hydrogen). Glucose is oxidized in cellular respiration.
- **Reduction** = gain of electrons. NAD⁺ + 2H → NADH (carries electrons as hydride).
- **Electron carriers** (NADH, FADH₂, ubiquinone/CoQ, cytochrome c) shuttle electrons from fuel oxidation to the mitochondrial electron transport chain (ETC).

The mitochondrial ETC (Complexes I–IV) sequentially transfers electrons from NADH/FADH₂ to molecular oxygen (O₂ → H₂O). This electron flow is thermodynamically favorable and coupled to **proton pumping** across the inner mitochondrial membrane, generating the proton-motive force that drives **ATP synthase** [^stryer-biochemistry].

### Charge Separation and Membrane Potentials

Ions carry charge by virtue of electron deficits (cations, e.g., Na⁺, K⁺, Ca²⁺) or surpluses (anions, e.g., Cl⁻, HCO₃⁻). The unequal distribution of these ions across biological membranes — maintained by ion pumps that use ATP (itself derived from electron transport) — creates the **membrane potential**, the electrical potential difference across the cell membrane [^lodish-molecular-cell-biology].

For cardiac cells at rest: **~−85 mV** (interior negative). This potential energy, stored in the charge separation, drives the action potential when voltage-gated Na⁺ channels open.

## Relevance to the Heart

The electron's role in the heart is comprehensive — it underlies every process from molecular to organ scale:

| Process | Electron-level mechanism |
|:---|:---|
| **Action potential** | Na⁺/K⁺/Ca²⁺ ion movements across the membrane = redistribution of charge = electron deficit/surplus flows. The resting potential (−85 mV) is a charge separation maintained by the Na⁺/K⁺-ATPase. |
| **Ca²⁺ binding to troponin C** | Electrostatic interaction between Ca²⁺ (electron-poor, divalent cation) and the negatively-charged EF-hand residues (electron-rich carbonyl oxygens) of troponin C — an electron density interaction that triggers the conformational shift gating every contraction [^bers-2002-cardiac-ec-coupling]. |
| **ATP hydrolysis** | The energy stored in ATP's phosphoanhydride bonds is electronic (high-energy resonance forms, electron delocalization in inorganic phosphate after hydrolysis). Myosin uses this energy to change conformation and pull actin — the cross-bridge cycle. |
| **Mitochondrial ETC** | The heart's cardiomyocytes, with their 30–40% mitochondrial volume fraction, are among the most aerobically active cells in the body. Their ATP supply (and hence contractile capacity) is directly coupled to the rate of electron flow through the ETC. |
| **Redox signaling** | Reactive oxygen species (ROS), generated as by-products of electron transport, serve as second messengers in cardiomyocyte signaling; excessive ROS in heart failure contributes to contractile dysfunction and arrhythmia. |

## Connections

- **Up (atomic scale):** The electron configuration of each element determines its ionic form in biology. For calcium: Z=20, [Ar]4s² → loses 2 electrons → Ca²⁺. See **[Calcium](../../02-atomic/calcium/README.md)**.
- **Up (molecular scale):** Electrostatic interactions at the electron-density level drive Ca²⁺ binding to troponin C — see **[Troponin complex](../../03-molecular/troponin-complex/README.md)**.

## See Also

- [Calcium](../../02-atomic/calcium/README.md) — the heart's signaling ion, whose chemistry is defined by its electron configuration.
- [Troponin complex](../../03-molecular/troponin-complex/README.md) — electrostatic interactions underlie Ca²⁺ binding.

[^lodish-molecular-cell-biology]: Lodish H, Berk A, Kaiser CA, et al. *Molecular Cell Biology.* 8th ed. W.H. Freeman; 2016. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Molecular-Cell-Biology/p/1464183392)
[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [macmillanlearning.com](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
