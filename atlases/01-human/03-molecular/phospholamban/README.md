---
schema: human-scale-entry/v1
id: phospholamban
name: Phospholamban
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-03
summary: "Phospholamban (PLN, gene PLN) — 52-aa transmembrane micropeptide that tonically inhibits SERCA2a by reducing Ca²⁺ affinity (Km ~0.2→0.6 µM). PKA (Ser16) and CaMKII (Thr17) phosphorylation reverse inhibition, producing lusitropy and increased SR Ca²⁺ loading."
aliases: ["PLN", "phospholamban micropeptide", "cardiac phospholamban"]
sources:
  - id: maclennan-2003-serca-pln
    type: peer-reviewed
    cite: "MacLennan DH, Kranias EG. Phospholamban: a crucial regulator of cardiac contractility. Nat Rev Mol Cell Biol. 2003;4(7):566-77."
    doi: "10.1038/nrm1151"
    pmid: "12838339"
    url: "https://doi.org/10.1038/nrm1151"
  - id: kranias-2007-pln-heart-failure
    type: peer-reviewed
    cite: "Kranias EG, Bers DM. Calcium and cardiomyopathies. Subcell Biochem. 2007;45:523-37."
    doi: "10.1007/978-1-4020-6191-2_20"
    pmid: "18193649"
    url: "https://doi.org/10.1007/978-1-4020-6191-2_20"
  - id: simmerman-1998-pln-review
    type: peer-reviewed
    cite: "Simmerman HK, Jones LR. Phospholamban: protein structure, mechanism of action, and role in cardiac function. Physiol Rev. 1998;78(4):921-47."
    doi: "10.1152/physrev.1998.78.4.921"
    pmid: "9790566"
    url: "https://doi.org/10.1152/physrev.1998.78.4.921"
  - id: schmitt-2003-pln-mutation
    type: peer-reviewed
    cite: "Schmitt JP, Kamisago M, Asahi M, et al. Dilated cardiomyopathy and heart failure caused by a mutation in phospholamban. Science. 2003;299(5611):1410-3."
    doi: "10.1126/science.1081578"
    pmid: "12610310"
    url: "https://doi.org/10.1126/science.1081578"
cross_links:
  - target: 01-human/03-molecular/serca2a
    relation: modulates
    note: "Dephosphorylated PLN binds SERCA2a and reduces its Ca²⁺ affinity, slowing SR Ca²⁺ reuptake at diastolic [Ca²⁺]. Phosphorylation of PLN relieves this inhibition — a central regulatory switch in cardiac contractility."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: modulated-by
    note: "β1-AR/PKA phosphorylates PLN at Ser16 (the dominant site in acute sympathetic stimulation), relieving SERCA2a inhibition → faster SR Ca²⁺ reuptake → faster relaxation and increased SR Ca²⁺ loading."
taxonomy:
  uniprot: "P26678"
  gene_symbol: "PLN"
  chromosome: "6q22.31"
---

# Phospholamban

## Overview

Phospholamban (PLN) is a **52-amino acid transmembrane micropeptide** encoded by the `PLN` gene, expressed almost exclusively in cardiac muscle and, to a lesser extent, slow-twitch skeletal and smooth muscle. It functions as the **tonic inhibitor of SERCA2a** — the SR Ca²⁺-ATPase pump responsible for clearing cytosolic Ca²⁺ after each cardiac contraction [^simmerman-1998-pln-review].

The PLN–SERCA2a interaction is one of the most precisely characterized molecular regulatory mechanisms in cardiac physiology. In its **dephosphorylated state**, PLN associates with SERCA2a and reduces the pump's apparent Ca²⁺ affinity, shifting its Km from ~0.2 µM (uninhibited) to ~0.6 µM — a shift that significantly reduces pump rate at the low [Ca²⁺] of diastole (~100 nM). When PLN is **phosphorylated** at Ser16 (by PKA, downstream of β1-adrenergic stimulation) or at Thr17 (by CaMKII), it dissociates from SERCA2a, restoring full pump activity and enabling faster Ca²⁺ reuptake, faster muscle relaxation (lusitropy), and greater SR Ca²⁺ loading [^maclennan-2003-serca-pln].

PLN is thus the molecular relay point through which sympathetic nervous activation (fight-or-flight) simultaneously increases contractility and ensures complete cardiac relaxation between beats — a physiologically essential pairing.

## Structure

### Protein Features

| Property | Value |
|:---|:---|
| Length | 52 amino acids |
| Molecular weight | ~6 kDa (monomer) |
| Membrane topology | Single C-terminal transmembrane helix (residues 31–52) embedded in SR membrane; N-terminal cytoplasmic domain (1–30) extends into cytosol |
| Oligomeric state | Pentamer in resting cardiac SR (five PLN protomers form a "pinwheel" structure); the pentamer is the inactive storage form; monomers are the SERCA2a-inhibitory species |

### Functional Domains

| Domain | Residues | Key features |
|:---|:---|:---|
| **Cytoplasmic domain (Ia)** | 1–20 | Disordered in solution; contains **Ser16** (PKA phosphorylation site) and **Thr17** (CaMKII phosphorylation site); forms amphipathic helix upon binding SERCA2a |
| **Cytoplasmic domain (Ib)** | 21–30 | Linker; less studied |
| **Transmembrane domain** | 31–52 | α-helix in the SR membrane; engages SERCA2a TM2/TM6/TM9 helices |

### Phosphorylation Sites

| Site | Kinase | Effect |
|:---|:---|:---|
| **Ser16** | PKA (cAMP-activated, downstream of β1-AR) | Dominant acute regulatory site; phosphorylation sufficient to relieve SERCA2a inhibition; Ser16-Ala mutant abolishes β-agonist lusitropic effect |
| **Thr17** | CaMKII | Activated by rising [Ca²⁺]/CaM; contributes to frequency-dependent augmentation of SR Ca²⁺ loading; Thr17 phosphorylation increases at higher heart rates |

In normal physiology, Ser16 phosphorylation occurs first and is quantitatively dominant; Thr17 phosphorylation follows and may contribute to sustained effects at high stimulation rates. Both sites are hyperphosphorylated in some models of heart failure [^kranias-2007-pln-heart-failure].

## Mechanism

### Inhibition of SERCA2a

Unphosphorylated PLN inhibits SERCA2a by a two-component mechanism:

1. **Transmembrane interaction:** The PLN TM helix (residues 31–52) packs against SERCA2a TM helices (primarily TM2, TM6, TM9), stabilizing the E2 conformation of the pump. This shifts the conformational equilibrium toward the low-Ca²⁺-affinity E2 state, reducing Ca²⁺ binding at the cytoplasmic face.
2. **Cytoplasmic interaction:** Domain Ia of PLN contacts the cytoplasmic actuator domain of SERCA2a, impeding the domain movements that are required for Ca²⁺ binding and translocation.

The net kinetic effect: **Km for Ca²⁺ rises from ~0.2 µM to ~0.6 µM** — a shift that reduces SERCA2a pumping rate approximately twofold at the diastolic [Ca²⁺] of ~100 nM, while having negligible effect at the high [Ca²⁺] of systole (~1 µM, where SERCA2a is saturated regardless).

### Relief of Inhibition

PKA-mediated phosphorylation of **Ser16** introduces a negative charge on the cytoplasmic domain, causing an electrostatic repulsion that disrupts the PLN–SERCA2a interface. The PLN cytoplasmic domain adopts a more ordered, non-inhibitory helical structure. Phospho-PLN moves away from SERCA2a (or remains bound in a non-inhibitory orientation), and SERCA2a reverts to its intrinsic high Ca²⁺ affinity → faster Ca²⁺ reuptake.

The pentamer pool acts as a buffer: PLN monomers (the active inhibitory species) are in equilibrium with the pentamer. PKA phosphorylation of monomers shifts the equilibrium, recruiting more monomers from the pentamer pool into the phosphorylated state, amplifying the regulatory range.

## Function

### Physiological Role: Sympathetic Lusitropy

In a resting state (low sympathetic tone):
- PLN is largely dephosphorylated (~60–80% dephospho at rest in vivo)
- SERCA2a operates at ~50% of maximum Ca²⁺ affinity
- Ca²⁺ reuptake kinetics are modest → τ of Ca²⁺ transient decay ~150–200 ms in human ventricle

During sympathetic stimulation (β1-AR → PKA → Ser16 phosphorylation):
- PLN is rapidly phosphorylated (seconds)
- SERCA2a operates at full Ca²⁺ affinity
- Ca²⁺ reuptake accelerates → τ decreases → faster relaxation
- SR Ca²⁺ load increases → next systolic Ca²⁺ transient is larger → increased contractility

This PKA-PLN-SERCA2a axis is a central mechanism by which the heart simultaneously increases both heart rate (via HCN4) and ensures complete relaxation between each (now faster) beat.

### PLN as a Regulatory Reserve

In transgenic mouse hearts where PLN is deleted, basal contractility is enhanced (SERCA2a is fully active constitutively), but the additional β-agonist response is blunted — the heart loses its "sympathetic reserve." This demonstrates that PLN inhibition is not merely a brake but the **physiological substrate for catecholamine-driven inotropic and lusitropic reserve** [^maclennan-2003-serca-pln].

## Connections

- **Modulates** → [SERCA2a](serca2a/README.md): PLN is the direct physiological inhibitor of SERCA2a; the PLN–SERCA2a binary interaction is the primary molecular determinant of cardiac relaxation rate.
- **Modulated-by** → [β1-adrenergic receptor](beta1-adrenergic-receptor/README.md): PKA downstream of β1-AR phosphorylates PLN Ser16, the dominant switch that relieves SERCA2a inhibition and produces sympathetic lusitropy.

## Pathology

| Disease | PLN mechanism |
|:---|:---|
| **Heart failure** | PLN hyperinhibition of SERCA2a (reduced PLN phosphorylation due to elevated PP1/PP2A phosphatase activity and reduced PKA signaling) → slower Ca²⁺ reuptake → impaired relaxation, reduced SR Ca²⁺ load, reduced systolic Ca²⁺ transient → a core mechanism of HFrEF diastolic and systolic dysfunction [^kranias-2007-pln-heart-failure] |
| **PLN Arg9Cys mutation (dominant-negative)** | Mutant PLN cannot be phosphorylated and super-inhibits SERCA2a; causes a familial dilated cardiomyopathy [^schmitt-2003-pln-mutation] |
| **PLN null (homozygous loss-of-function)** | Not known to cause human disease; PLN-KO mouse model has enhanced basal contractility but loss of β-agonist reserve |

## See Also

- [SERCA2a](serca2a/README.md) — the primary regulatory target.
- [β1-adrenergic receptor](beta1-adrenergic-receptor/README.md) — upstream kinase signaling.
- [Calcium](../../02-atomic/calcium/README.md) — the ion whose handling PLN regulates.

[^simmerman-1998-pln-review]: Simmerman HK, Jones LR. Phospholamban: protein structure, mechanism of action, and role in cardiac function. *Physiol Rev.* 1998;78(4):921-47. [doi:10.1152/physrev.1998.78.4.921](https://doi.org/10.1152/physrev.1998.78.4.921) · [PubMed 9790566](https://pubmed.ncbi.nlm.nih.gov/9790566/)
[^maclennan-2003-serca-pln]: MacLennan DH, Kranias EG. Phospholamban: a crucial regulator of cardiac contractility. *Nat Rev Mol Cell Biol.* 2003;4(7):566-77. [doi:10.1038/nrm1151](https://doi.org/10.1038/nrm1151) · [PubMed 12838339](https://pubmed.ncbi.nlm.nih.gov/12838339/)
[^kranias-2007-pln-heart-failure]: Kranias EG, Bers DM. Calcium and cardiomyopathies. *Subcell Biochem.* 2007;45:523-37. [doi:10.1007/978-1-4020-6191-2_20](https://doi.org/10.1007/978-1-4020-6191-2_20) · [PubMed 18193649](https://pubmed.ncbi.nlm.nih.gov/18193649/)
[^schmitt-2003-pln-mutation]: Schmitt JP, Kamisago M, Asahi M, et al. Dilated cardiomyopathy and heart failure caused by a mutation in phospholamban. *Science.* 2003;299(5611):1410-3. [doi:10.1126/science.1081578](https://doi.org/10.1126/science.1081578) · [PubMed 12610310](https://pubmed.ncbi.nlm.nih.gov/12610310/)
