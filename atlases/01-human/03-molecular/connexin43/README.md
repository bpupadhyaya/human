---
schema: human-scale-entry/v1
id: connexin43
name: Connexin-43
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-03
summary: "Connexin-43 (Cx43, gene GJA1) — primary gap junction protein of ventricular myocardium. Hexameric connexons dock end-to-end at intercalated discs forming ~1.4 nS pores, making the myocardium an electrical syncytium for coordinated contraction."
aliases: ["Cx43", "GJA1", "gap junction alpha-1", "connexin 43"]
sources:
  - id: severs-2008-cx43-cardiac
    type: peer-reviewed
    cite: "Severs NJ, Bruce AF, Dupont E, Rothery S. Remodelling of gap junctions and connexin expression in diseased myocardium. Cardiovasc Res. 2008;80(1):9-19."
    doi: "10.1093/cvr/cvn133"
    pmid: "18519446"
    url: "https://doi.org/10.1093/cvr/cvn133"
  - id: saffitz-1994-cx43-distribution
    type: peer-reviewed
    cite: "Saffitz JE, Kanter HL, Green KG, Tolley TK, Beyer EC. Tissue-specific determinants of anisotropic conduction velocity in canine atrial and ventricular myocardium. Circ Res. 1994;74(6):1065-70."
    doi: "10.1161/01.RES.74.6.1065"
    pmid: "8187276"
    url: "https://doi.org/10.1161/01.RES.74.6.1065"
  - id: evans-2002-gap-junctions-review
    type: peer-reviewed
    cite: "Evans WH, Martin PE. Gap junctions: structure and function. Mol Membr Biol. 2002;19(2):121-36."
    doi: "10.1080/09687680210139839"
    pmid: "12126230"
    url: "https://doi.org/10.1080/09687680210139839"
  - id: rohr-2004-cx43-arrhythmia
    type: peer-reviewed
    cite: "Rohr S. Role of gap junctions in the propagation of the cardiac action potential. Cardiovasc Res. 2004;62(2):309-22."
    doi: "10.1016/j.cardiores.2003.11.035"
    pmid: "15094351"
    url: "https://doi.org/10.1016/j.cardiores.2003.11.035"
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "Cx43 is the dominant gap-junction protein of working ventricular and atrial cardiomyocytes, concentrated at the intercalated discs that join adjacent cells end-to-end."
  - target: 01-human/05-tissue/myocardium
    relation: expressed-by
    note: "Cx43 expression determines the gap-junction density of ventricular myocardium and is the molecular basis of the myocardium's property as an electrical syncytium."
taxonomy:
  uniprot: "P17302"
  gene_symbol: "GJA1"
  chromosome: "6q22.31"
---

# Connexin-43

## Overview

Connexin-43 (Cx43), encoded by `GJA1`, is the **primary gap-junction protein of the ventricular working myocardium** and the molecular structure that makes the heart a functional electrical syncytium. Six Cx43 subunits assemble into a **connexon (hemichannel)** in the plasma membrane; two connexons from adjacent cells dock head-to-head at the intercalated disc to form a complete **gap junction channel** with a single-channel conductance of approximately **1.4 nS** [^evans-2002-gap-junctions-review].

These gap junction channels are **aqueous pores** — wide enough (~1.5 nm) to pass ions, metabolites, second messengers (cAMP, IP₃), and small RNA molecules (up to ~1,000 Da) directly between the cytoplasms of adjacent cardiomyocytes without traversing the extracellular space. It is this direct cytoplasmic coupling that enables the depolarisation wave initiated by the SA node to propagate cell-to-cell across the myocardium at ~0.3–1 m/s in working muscle, ensuring synchronous contraction of billions of cardiomyocytes as a single coordinated unit.

## Structure

### Connexin Topology

Each Cx43 subunit is a **four-transmembrane protein** (~43 kDa):

| Domain | Topology | Function |
|:---|:---|:---|
| N-terminus | Cytoplasmic | Voltage sensing; gating |
| TM1–TM4 | 4 transmembrane helices | Membrane anchoring; TM1 and TM2 line the pore |
| ECL1, ECL2 | Extracellular loops (2) | Docking interface between two hemichannels; disulfide bonds (3 Cys each) ensure specificity |
| Cytoplasmic loop | Intracellular | pH and kinase regulation |
| C-terminus (CT) | Cytoplasmic; long | Primary regulatory domain; phosphorylated at multiple Ser/Tyr sites; interacts with ZO-1, Src, PKC |

### Connexon Assembly

Six Cx43 subunits oligomerise in the ER/Golgi to form a **hexameric connexon** (hemichannel), which traffics to the plasma membrane via microtubule-dependent vesicular transport. At the intercalated disc membrane, connexons from adjacent cells dock via ECL1–ECL2 hydrophobic interactions and disulfide bonds, forming a complete **gap junction channel** of ~1.5 nm internal diameter.

### Plaques and Gap Junction Organisation

Thousands of gap junction channels cluster into **plaques** (~0.1–1 µm diameter, each containing hundreds to thousands of channels), visible by freeze-fracture electron microscopy as ordered particle arrays. At the intercalated disc, Cx43 plaques are spatially co-localised with N-cadherin (adherens junctions) and desmoplakin (desmosomes), forming a mechanically and electrically integrated junction complex [^saffitz-1994-cx43-distribution].

## Mechanism

### Electrical Coupling and Impulse Propagation

When an action potential arrives at one cell, Na⁺ influx depolarises the cell interior. Positive charge flows through gap junction channels into the adjacent cell, depolarising it above threshold and triggering its own action potential. This cell-to-cell electrical coupling propagates the excitation wavefront without chemical synapses.

Gap junctional coupling determines two key conduction properties:

1. **Conduction velocity:** Proportional to gap junction conductance (Gj). In ventricular myocardium, Gj is ~1,000–5,000 pS per cell-pair → CV ~0.3–1 m/s longitudinal (faster along fibers, where more Cx43 and more cell-cell contacts per unit length).
2. **Anisotropy:** Cx43 is predominantly at the **end-to-end** intercalated discs in ventricular myocytes, with little lateral coupling → conduction is ~3–5× faster longitudinally than transversely. This anisotropy shapes the normal excitation sequence and, when disrupted, predisposes to re-entrant arrhythmias [^rohr-2004-cx43-arrhythmia].

### Channel Gating

Cx43 channels close (gate) in response to:
- **Low intracellular pH** (acidosis): intramolecular interaction between the CT domain and the cytoplasmic loop → channel closure. This is an adaptive response to ischemia, limiting damage propagation cell-to-cell.
- **High [Ca²⁺]i**: same CT-mediated gating; Ca²⁺ overload closes channels.
- **Phosphorylation:** Src kinase and PKC phosphorylation of CT domain → channel closure. Conversely, CK1-mediated phosphorylation at Ser residues → channel stabilisation.
- **Voltage-dependent gating:** Transjunctional voltage (Vj) above ~±30 mV partially closes channels (fast gate) and above ~±100 mV fully closes them (slow gate); at physiological Vj, most channels remain open.

### Permeability to Signaling Molecules

Beyond ionic coupling, Cx43 allows passage of:
- **cAMP** — synchronises PKA signaling across cell groups
- **IP₃** — can coordinate Ca²⁺ waves across multiple cells
- **ATP** — paracrine purinergic signaling via hemichannel release (separate from junctional function)
- **Small RNAs** (controversial) — recent evidence for connexin-dependent RNA transfer

## Function

### Myocardium as Electrical Syncytium

Without Cx43, the action potential would be confined to individual cardiomyocytes, making coordinated contraction impossible. The electrical syncytium created by Cx43-mediated gap junctions allows the SA node to be the single pacemaker for ~3 billion cardiomyocytes — each beat initiated by a single automaticity focus and propagated throughout the ventricles within ~80–100 ms. This fundamental property of the heart depends on Cx43 density, distribution, and gating.

### Intercalated Disc as Integrated Junction

The intercalated disc is not merely an electrical junction; it is a multifunctional organelle:
- **Mechanical coupling** (fascia adherens + desmosomes): transmit contractile force cell-to-cell
- **Electrical coupling** (gap junctions, Cx43): propagate depolarisation
- **Metabolic coupling** (gap junction pores): share ATP, metabolites, second messengers

Cx43 interacts with structural proteins (N-cadherin, ZO-1, β-catenin) and with Nav1.5 (voltage-gated Na⁺ channel) at a specialised subdomain of the intercalated disc called the **perinexus** — a spatial proximity that may allow Nav1.5 activity to influence gap junction function and vice versa.

## Connections

- **Expressed-by** → [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md): Cx43 is the dominant gap-junction protein of working ventricular cardiomyocytes, clustered at intercalated discs; it creates the ionic continuity between cells that enables synchronous contraction.
- **Expressed-by** → [Myocardium](../../05-tissue/myocardium/README.md): At the tissue scale, Cx43 expression level and distribution determine the electrical properties of the myocardium — conduction velocity, anisotropy, and susceptibility to re-entrant arrhythmia.

## Pathology

| Disease | Cx43 mechanism |
|:---|:---|
| **Arrhythmia in heart failure** | Cx43 is down-regulated, dephosphorylated, and re-distributed away from intercalated discs ("lateralisation") in failing ventricles — reducing electrical coupling, slowing conduction, and increasing re-entry risk [^severs-2008-cx43-cardiac] |
| **Ischemia/reperfusion** | Ischemia acidosis closes Cx43 channels acutely (protective: limits injury propagation); paradoxically, reperfusion reopens them, potentially propagating Ca²⁺ overload to adjacent non-ischemic cells |
| **Hypoplastic left heart syndrome (HLHS)** | GJA1 mutations found in some HLHS cases; role of Cx43 in cardiac morphogenesis is established |
| **Oculodentodigital dysplasia (ODDD)** | Autosomal dominant GJA1 mutations cause a multisystem syndrome with craniofacial abnormalities and cardiac arrhythmias |
| **Re-entrant tachyarrhythmias** | Heterogeneous Cx43 loss in healed infarct border zones creates slow conduction channels — the substrate for monomorphic VT |

## See Also

- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — the cell expressing Cx43.
- [Myocardium](../../05-tissue/myocardium/README.md) — the tissue-scale syncytium enabled by Cx43.

[^evans-2002-gap-junctions-review]: Evans WH, Martin PE. Gap junctions: structure and function. *Mol Membr Biol.* 2002;19(2):121-36. [doi:10.1080/09687680210139839](https://doi.org/10.1080/09687680210139839) · [PubMed 12126230](https://pubmed.ncbi.nlm.nih.gov/12126230/)
[^severs-2008-cx43-cardiac]: Severs NJ, Bruce AF, Dupont E, Rothery S. Remodelling of gap junctions and connexin expression in diseased myocardium. *Cardiovasc Res.* 2008;80(1):9-19. [doi:10.1093/cvr/cvn133](https://doi.org/10.1093/cvr/cvn133) · [PubMed 18519446](https://pubmed.ncbi.nlm.nih.gov/18519446/)
[^saffitz-1994-cx43-distribution]: Saffitz JE, Kanter HL, Green KG, Tolley TK, Beyer EC. Tissue-specific determinants of anisotropic conduction velocity in canine atrial and ventricular myocardium. *Circ Res.* 1994;74(6):1065-70. [doi:10.1161/01.RES.74.6.1065](https://doi.org/10.1161/01.RES.74.6.1065) · [PubMed 8187276](https://pubmed.ncbi.nlm.nih.gov/8187276/)
[^rohr-2004-cx43-arrhythmia]: Rohr S. Role of gap junctions in the propagation of the cardiac action potential. *Cardiovasc Res.* 2004;62(2):309-22. [doi:10.1016/j.cardiores.2003.11.035](https://doi.org/10.1016/j.cardiores.2003.11.035) · [PubMed 15094351](https://pubmed.ncbi.nlm.nih.gov/15094351/)
