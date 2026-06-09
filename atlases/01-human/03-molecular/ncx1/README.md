---
schema: human-scale-entry/v1
id: ncx1
name: NCX1 (Na⁺/Ca²⁺ exchanger 1)
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-03
summary: "NCX1 (SLC8A1) — cardiac sarcolemmal Na⁺/Ca²⁺ exchanger. Electrogenic: exchanges 3 Na⁺ for 1 Ca²⁺, generating net current. Forward mode (Ca²⁺ extrusion) removes ~28% of Ca²⁺ after systole; reverse mode contributes to CICR in SA node. Upregulated in heart failure."
aliases: ["NCX1", "SLC8A1", "Na/Ca exchanger", "sodium-calcium exchanger 1", "cardiac NCX"]
sources:
  - id: blaustein-1999-ncx-review
    type: peer-reviewed
    cite: "Blaustein MP, Lederer WJ. Sodium/calcium exchange: its physiological implications. Physiol Rev. 1999;79(3):763-854."
    doi: "10.1152/physrev.1999.79.3.763"
    pmid: "10390518"
    url: "https://doi.org/10.1152/physrev.1999.79.3.763"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
    url: "https://doi.org/10.1038/415198a"
  - id: philipson-2000-ncx-structure
    type: peer-reviewed
    cite: "Philipson KD, Bhargava P. Molecular studies of Na+/Ca2+ exchangers. Basic Res Cardiol. 2002;97 Suppl 1:I15-I20."
    doi: "10.1007/s003950200024"
    pmid: "12479234"
    url: "https://doi.org/10.1007/s003950200024"
  - id: armoundas-2003-ncx-hf
    type: peer-reviewed
    cite: "Armoundas AA, Hobai IA, Tomaselli GF, Winslow RL, O'Rourke B. Role of sodium-calcium exchanger in modulating the action potential of ventricular myocytes from normal and failing hearts. Circ Res. 2003;93(1):46-53."
    doi: "10.1161/01.RES.0000080932.98903.D8"
    pmid: "12791707"
    url: "https://doi.org/10.1161/01.RES.0000080932.98903.D8"
cross_links:
  - target: 01-human/02-atomic/calcium
    relation: modulates
    note: "NCX1 in forward mode is responsible for ~28% of cytosolic Ca²⁺ removal from the cardiomyocyte after each systole; in reverse mode it contributes Ca²⁺ entry that supports CICR in pacemaker cells."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: expressed-by
    note: "NCX1 is expressed in the sarcolemma and T-tubule membrane of ventricular and atrial cardiomyocytes; it is the second-largest Ca²⁺ extrusion mechanism after SERCA2a."
  - target: 01-human/04-cellular/sa-node-cell
    relation: expressed-by
    note: "NCX1 is expressed in SA node pacemaker cells; reverse-mode NCX1 (Ca²⁺ entry driven by SR Ca²⁺ release events) contributes inward current during diastolic depolarisation as part of the Ca²⁺ clock."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "NCX1 is upregulated in failing human ventricle → increased Ca²⁺ extrusion → further SR Ca²⁺ depletion (additive to SERCA2a downregulation) → reduced contractility; inward INCX during repolarization prolongs action potential → delayed afterdepolarizations → arrhythmia in HFrEF."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "NCX1 is the second-largest Ca²⁺ removal pathway (~28% per beat); electrogenically exchanges 3 Na⁺:1 Ca²⁺; reverse mode → Ca²⁺ entry during action potential; NCX1 upregulation in HF impairs systolic function; NCX1 is a proposed therapeutic target in heart failure."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "NCX1 is densely expressed in myocardial T-tubules and sarcolemma; NCX1/SERCA2a ratio determines Ca²⁺ removal balance; transient inward INCX (Iti) during Ca²⁺ sparks → delayed afterdepolarizations → triggered arrhythmias; NCX1 drives ischemia-reperfusion Ca²⁺ overload injury."
taxonomy:
  uniprot: "P32418"
  gene_symbol: "SLC8A1"
  chromosome: "2p22.1"
---

# NCX1 (Na⁺/Ca²⁺ exchanger 1)

## Overview

NCX1 (Sodium-Calcium Exchanger 1, encoded by `SLC8A1`) is the **cardiac sarcolemmal Na⁺/Ca²⁺ exchanger** — a secondary active transporter that uses the electrochemical gradient for Na⁺ to move Ca²⁺ across the plasma membrane. NCX1 is **electrogenic**: it exchanges **3 Na⁺ for 1 Ca²⁺**, generating a net charge transfer (one positive charge per cycle in the forward direction) that produces a measurable ionic current [^blaustein-1999-ncx-review].

NCX1 operates in two modes:

- **Forward mode (physiological Ca²⁺ extrusion):** 3 Na⁺ in, 1 Ca²⁺ out. Driven by the large inward Na⁺ gradient and the negative membrane potential. Responsible for approximately **28% of cytosolic Ca²⁺ removal** from ventricular cardiomyocytes following each systolic Ca²⁺ transient (the remaining ~70% being handled by SERCA2a).
- **Reverse mode (Ca²⁺ entry):** 3 Na⁺ out, 1 Ca²⁺ in. Occurs when membrane potential is strongly depolarised (early action potential plateau) or when [Na⁺]i is elevated. Contributes to Ca²⁺ entry that supports CICR in some cell types and contributes to the Ca²⁺ clock in SA node cells.

Unlike SERCA2a, NCX1 **does not use ATP** — it is a passive exchanger driven by electrochemical gradients. This makes NCX1 Ca²⁺ extrusion energetically less expensive but also thermodynamically reversible [^bers-2002-cardiac-ec-coupling].

## Structure

### Protein Architecture

NCX1 is a large (~110 kDa, 938 amino acids in humans) single-pass membrane protein with an unusual topology:

| Domain | Residues | Function |
|:---|:---|:---|
| **TM1–TM5 (α-1 repeat)** | 1–218 | N-terminal transmembrane bundle; contains the α-1 transport repeat contributing to the ion translocation pathway |
| **Large intracellular regulatory loop (f-loop)** | 218–764 | ~520 aa cytoplasmic loop; contains regulatory Ca²⁺ binding domains (CBD1, CBD2) and XIP region |
| **TM6–TM10 (α-2 repeat)** | 764–900 | C-terminal transmembrane bundle; contains the α-2 transport repeat; both α repeats form the exchange site |
| **C-terminus** | 900–938 | Short cytoplasmic tail |

### Regulatory Domains in the f-Loop

| Feature | Location | Function |
|:---|:---|:---|
| **XIP (exchanger inhibitory peptide) region** | N-terminal f-loop | Autoinhibitory domain; XIP peptide was the first selective NCX inhibitor identified |
| **CBD1 (Ca²⁺-binding domain 1)** | f-loop | High-affinity Ca²⁺ sensor; Ca²⁺ binding relieves XIP autoinhibition → allosteric activation of NCX1 |
| **CBD2 (Ca²⁺-binding domain 2)** | f-loop | Lower affinity; modulates transport kinetics; contains an alternatively spliced region (exon A–F contribute to tissue-specific isoforms) |

## Mechanism

### Ion Exchange Stoichiometry

The 3:1 Na⁺:Ca²⁺ stoichiometry makes NCX1 electrogenic with a reversal potential (E_NCX):

$$E_{NCX} = \frac{3E_{Na} - 2E_{Ca}}{1}$$

Where ENa ≈ +70 mV and ECa ≈ +130 mV in a resting cardiomyocyte:

$$E_{NCX} = (3 \times 70) - (2 \times 130) = 210 - 260 = -50 \text{ mV (approximately)}$$

At membrane potentials **more negative than E_NCX** (~−50 mV, including diastole at ~−85 mV), the driving force favours Ca²⁺ extrusion (**forward mode**). At potentials **more positive than E_NCX**, Ca²⁺ entry (**reverse mode**) is thermodynamically favoured — which occurs during the plateau phase of the ventricular action potential.

### Allosteric Ca²⁺ Activation

Rising cytosolic [Ca²⁺] during systole activates NCX1 (via CBD1 binding) — an autoregulatory mechanism that increases Ca²⁺ extrusion precisely when cytosolic [Ca²⁺] is highest. This self-activation is the basis for the Ca²⁺-dependent increase in NCX1 current during the systolic phase.

### Na⁺ Dependence

NCX1 is exquisitely sensitive to intracellular [Na⁺]. Elevated [Na⁺]i (as occurs in heart failure, when Na⁺/K⁺-ATPase activity is reduced):
- Reduces the inward Na⁺ driving force
- Shifts E_NCX in a positive direction
- Promotes reverse-mode activity → less Ca²⁺ extrusion → SR Ca²⁺ accumulation or alternatively Ca²⁺ overload

This is the mechanistic link between digitalis (Na⁺/K⁺-ATPase inhibitor → ↑[Na⁺]i → less NCX1 forward mode → ↑intracellular Ca²⁺ → positive inotropy) and the toxicity of high digitalis levels.

## Function

### Ca²⁺ Removal from the Cardiomyocyte

In human ventricular myocytes, the Ca²⁺ removal fractions per beat:

| Mechanism | Fraction |
|:---:|:---:|
| SERCA2a (SR uptake) | ~70% |
| **NCX1 (sarcolemmal extrusion)** | **~28%** |
| PMCA (plasma membrane Ca²⁺-ATPase) | ~1% |
| Mitochondrial uniporter | ~1% |

The Ca²⁺ extruded by NCX1 represents a **net loss** from the cell per beat — it must be balanced by Ca²⁺ entry via Cav1.2 (L-type channels) to maintain Ca²⁺ homeostasis over many beats. The balance (gain via Cav1.2 = loss via NCX1) is referred to as the **Ca²⁺ steady-state condition**. Any perturbation (e.g., increased Cav1.2 entry with β-agonist) is compensated over time by increased NCX1 extrusion until a new steady state is reached.

### Ca²⁺ Entry and the SA Node Ca²⁺ Clock

In SA node pacemaker cells, spontaneous SR Ca²⁺ release events (Ca²⁺ sparks, via RyR) during diastole trigger NCX1 **forward mode** — Ca²⁺ moves out, 3 Na⁺ move in → net inward current (INCX) depolarises the membrane. This inward INCX is a key component of the **Ca²⁺ clock**, one of two oscillatory mechanisms that drive pacemaker automaticity. The interplay between the Ca²⁺ clock (INCX-driven depolarisation) and the membrane clock (I_f, ICaT) produces robust SA node pacemaking [^blaustein-1999-ncx-review].

## Connections

- `modulates` → **[Calcium](../../02-atomic/calcium/README.md)** — NCX1 in forward mode is the second-largest Ca²⁺ removal pathway from the cardiomyocyte cytosol (~28% per beat in human ventricle); in reverse mode it brings Ca²⁺ into the cell.
- `expressed-by` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — NCX1 is expressed in the sarcolemma and T-tubule membrane of working cardiomyocytes; its current (INCX) contributes to action potential shape and Ca²⁺ homeostasis.
- `expressed-by` → **[SA Node Cell](../../04-cellular/sa-node-cell/README.md)** — Reverse-mode NCX1 in pacemaker cells generates an inward depolarising current during Ca²⁺ spark events, contributing to the Ca²⁺ clock component of pacemaker automaticity.
- `connects-to` → **[Heart Failure](../../07-system/heart-failure/README.md)** — NCX1 is upregulated in failing human ventricle → increased Ca²⁺ extrusion → further SR Ca²⁺ depletion (additive to SERCA2a downregulation) → reduced contractility; inward INCX during repolarization prolongs action potential → delayed afterdepolarizations → arrhythmia in HFrEF.
- `connects-to` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — NCX1 is the second-largest Ca²⁺ removal pathway (~28% per beat); electrogenically exchanges 3 Na⁺:1 Ca²⁺; reverse mode → Ca²⁺ entry during action potential; NCX1 upregulation in HF impairs systolic function; NCX1 is a proposed therapeutic target in heart failure.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — NCX1 is densely expressed in myocardial T-tubules and sarcolemma; NCX1/SERCA2a ratio determines Ca²⁺ removal balance; transient inward INCX (Iti) during Ca²⁺ sparks → delayed afterdepolarizations → triggered arrhythmias; NCX1 drives ischemia-reperfusion Ca²⁺ overload injury.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

## Pathology

| Disease | NCX1 mechanism |
|:---|:---|
| **Heart failure** | NCX1 is upregulated (mRNA and protein) in failing human ventricular myocardium [^armoundas-2003-ncx-hf]; this increases Ca²⁺ extrusion, further depleting SR Ca²⁺ (on top of SERCA2a downregulation) → reduced systolic Ca²⁺ transient → reduced contractility; also prolongs action potential via increased inward INCX during repolarisation |
| **Afterdepolarisations and arrhythmia** | When [Ca²⁺]i rises abnormally (Ca²⁺ sparks from hyperphosphorylated RyR2, Ca²⁺ overload), NCX1 forward mode generates an inward current called the **transient inward current (Iti)** → **delayed afterdepolarisations (DADs)** → triggered arrhythmias in heart failure, CPVT, and digitalis toxicity |
| **Digitalis toxicity** | High-dose cardiac glycosides → severe [Na⁺]i rise → NCX1 reverse mode → Ca²⁺ overload → arrhythmia |
| **Ischemia-reperfusion** | Ischemia raises [Na⁺]i (Na⁺/K⁺-ATPase fails) → NCX1 reverse mode → Ca²⁺ overload during reperfusion — a major mechanism of reperfusion injury |

## See Also

- [Calcium](../../02-atomic/calcium/README.md) — the ion NCX1 transports.
- [Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md) — the primary expressing cell.
- [SA node cell](../../04-cellular/sa-node-cell/README.md) — NCX1 drives the Ca²⁺ clock.
- [SERCA2a](serca2a/README.md) — the complementary Ca²⁺ removal pump.

[^blaustein-1999-ncx-review]: Blaustein MP, Lederer WJ. Sodium/calcium exchange: its physiological implications. *Physiol Rev.* 1999;79(3):763-854. [doi:10.1152/physrev.1999.79.3.763](https://doi.org/10.1152/physrev.1999.79.3.763) · [PubMed 10390518](https://pubmed.ncbi.nlm.nih.gov/10390518/)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
[^philipson-2000-ncx-structure]: Philipson KD, Bhargava P. Molecular studies of Na+/Ca2+ exchangers. *Basic Res Cardiol.* 2002;97 Suppl 1:I15-I20. [doi:10.1007/s003950200024](https://doi.org/10.1007/s003950200024) · [PubMed 12479234](https://pubmed.ncbi.nlm.nih.gov/12479234/)
[^armoundas-2003-ncx-hf]: Armoundas AA, Hobai IA, Tomaselli GF, Winslow RL, O'Rourke B. Role of sodium-calcium exchanger in modulating the action potential of ventricular myocytes from normal and failing hearts. *Circ Res.* 2003;93(1):46-53. [doi:10.1161/01.RES.0000080932.98903.D8](https://doi.org/10.1161/01.RES.0000080932.98903.D8) · [PubMed 12791707](https://pubmed.ncbi.nlm.nih.gov/12791707/)
