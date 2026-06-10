---
schema: human-scale-entry/v1
id: snare-complex
name: SNARE Complex
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Core vesicle fusion machinery: synaptobrevin-2 (v-SNARE) + syntaxin-1A + SNAP-25 (t-SNAREs) zipper into a four-helix bundle driving membrane fusion. Cleaved by botulinum/tetanus toxins. Nobel 2013: Sudhof, Rothman, Schekman."
aliases: ["SNARE", "SNARE complex", "synaptobrevin", "syntaxin", "SNAP-25", "vesicle fusion"]
sources:
  - id: sudhof-rothman-2009-snare
    type: peer-reviewed
    cite: "Sudhof TC, Rothman JE. Membrane fusion: grappling with SNARE and SM proteins. Science. 2009;323(5913):474-477."
    doi: "10.1126/science.1161748"
    pmid: "19164740"
    url: "https://doi.org/10.1126/science.1161748"
  - id: hanson-1997-nsf-snare
    type: peer-reviewed
    cite: "Hanson PI, Roth R, Morisaki H, Jahn R, Heuser JE. Structure and conformational changes in NSF and its membrane receptor complexes visualized by quick-freeze/deep-etch electron microscopy. Cell. 1997;90(3):523-535."
    doi: "10.1016/s0092-8674(00)80512-7"
    pmid: "9267031"
    url: "https://doi.org/10.1016/s0092-8674(00)80512-7"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: expressed-by
    note: "Neuronal SNAREs (synaptobrevin-2, syntaxin-1A, SNAP-25) are highly expressed in presynaptic axon terminals where they drive calcium-triggered neurotransmitter vesicle exocytosis."
  - target: 01-human/05-tissue/synapse
    relation: modulates
    note: "SNARE complex assembly and disassembly drives the millisecond-timescale vesicle exocytosis that underlies synaptic transmission at the presynaptic active zone."
  - target: 01-human/03-molecular/acetylcholine
    relation: modulates
    note: "SNARE-mediated exocytosis releases acetylcholine-containing synaptic vesicles at neuromuscular junctions and cholinergic CNS synapses; botulinum toxin targeting SNAREs blocks ACh release causing flaccid paralysis."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "The SNARE complex (VAMP2/synaptobrevin + SNAP-25 + syntaxin-1) at the motor nerve terminal mediates ACh vesicle fusion; ACh release via SNARE is intact in MG (disease is postsynaptic); BoNT cleaves SNARE → NMJ blockade that mimics but differs mechanistically from MG."
---

# SNARE Complex

## Overview

The **SNARE complex** (Soluble N-ethylmaleimide-sensitive factor Attachment protein REceptors) is the universal machinery for intracellular membrane fusion in eukaryotes — from constitutive secretory traffic in the Golgi to the millisecond-timescale fusion of synaptic vesicles triggered by calcium influx. Its discovery, mechanism, and regulation were recognized by the 2013 Nobel Prize in Physiology or Medicine (Thomas Südhof, James Rothman, and Randy Schekman) [^sudhof-rothman-2009-snare].

The neuronal SNARE complex is the most studied and clinically relevant. It consists of three proteins — **synaptobrevin-2** (also called VAMP2, on the vesicle membrane), **syntaxin-1A**, and **SNAP-25** (both on the target plasma membrane) — that assemble into a highly stable four-helix bundle bringing vesicle and plasma membranes within fusion distance. This machinery is the specific molecular target of some of the most potent biological toxins known to medicine: botulinum neurotoxins and tetanus toxin.

## Structure

### SNARE Protein Architecture

All SNARE proteins share a conserved **SNARE motif** (~60–70 amino acids) capable of forming coiled-coil interactions. The key distinguishing residue at the center of the four-helix bundle ("0-layer") is glutamine (Q-SNARE) or arginine (R-SNARE):

| Protein | Location | Type | Helix contribution |
|:---|:---|:---|:---|
| **Synaptobrevin-2 (VAMP2)** | Synaptic vesicle | R-SNARE | 1 helix |
| **Syntaxin-1A** | Plasma membrane | Qa-SNARE | 1 helix |
| **SNAP-25** | Plasma membrane (palmitoylated) | Qb+Qc-SNARE | 2 helices |

The assembled **ternary SNARE complex** is a parallel four-helix bundle (1 from synaptobrevin + 1 from syntaxin + 2 from SNAP-25) that is exceptionally stable — requiring the AAA+ ATPase **NSF** (N-ethylmaleimide-sensitive factor) together with **α-SNAP** to disassemble after fusion.

### Regulatory Proteins

| Protein | Function |
|:---|:---|
| **Synaptotagmin-1** | Calcium sensor (C2A/C2B domains, binds Ca²⁺ at 10–100 μM); triggers synchronous release within ~0.2 ms of Ca²⁺ influx |
| **Munc18-1** | SM protein; scaffold for syntaxin-1A in closed conformation; required for SNARE complex nucleation |
| **Munc13-1** | Priming factor; opens syntaxin-1A from closed to SNARE-accessible conformation |
| **Complexin** | Clamps assembled trans-SNARE complex in a primed state awaiting Ca²⁺ trigger |
| **NSF + α-SNAP** | Post-fusion SNARE disassembly ATPase machinery; recycles free SNARE monomers |
| **RIM proteins** | Scaffold active zone; recruits Ca²⁺ channels (CaV2.1/2.2) near vesicles; anchors Munc13 |

## Function

### Vesicle Cycle at the Active Zone

At the neuronal presynaptic terminal, synaptic vesicles undergo a tightly regulated cycle:

1. **Docking** — vesicles attach to the plasma membrane at the active zone via RIM–Rab3 interactions and initial syntaxin contacts
2. **Priming** — Munc13 opens syntaxin; partial SNARE zippering (N-terminal half) creates the readily releasable pool (RRP); Munc18 stabilizes the complex
3. **Clamping** — Complexin binds the half-zippered trans-SNARE complex, arresting it before full fusion
4. **Calcium triggering** — action potential → CaV2.1/2.2 Ca²⁺ influx at the active zone → synaptotagmin-1 C2 domains bind Ca²⁺ → complexin displacement → full C-terminal zippering of SNARE bundle → membrane merger
5. **Fusion pore opening** — lipid bilayers merge, opening an aqueous pore; neurotransmitter diffuses into the synaptic cleft within ~0.2 ms of Ca²⁺ entry
6. **Disassembly** — NSF (hexameric ATPase) + α-SNAP hydrolyze ATP to disassemble the extremely stable cis-SNARE complex; free SNARE monomers are recycled

### SNARE Function Beyond Neurons

SNAREs are universal in eukaryotic membrane traffic. Different SNARE paralogues operate at each trafficking step:
- **Golgi trafficking** — NSF/SNAP was first discovered in Golgi vesicle fusion (Rothman's original work)
- **Autophagosome-lysosome fusion** — STX17 + SNAP29 + VAMP7/8
- **Insulin secretion** — SNAP-23, syntaxin-4, VAMP2 drive glucose-stimulated insulin granule exocytosis from pancreatic beta cells
- **Platelet degranulation** — VAMP3/VAMP8, syntaxin-11, SNAP-23

## Mechanism

### Four-Helix Bundle Zippering

SNARE complex formation follows a **N→C directional zipper** mechanism:
1. N-terminal ends of the SNARE motifs interact first (weak, reversible)
2. Zippering propagates toward the C-terminal transmembrane anchors
3. Full C-terminal zippering generates ~35 kBT of free energy — sufficient to overcome the hydrophobic barrier to membrane fusion
4. The central 0-layer (Arg from synaptobrevin + 3 Gln from syntaxin/SNAP-25) forms a critical ionic interaction that establishes register fidelity

### Toxin Cleavage

The neuronal SNARE proteins are targeted with high specificity by bacterial metalloprotease toxins:

| Toxin | Target | Site | Effect |
|:---|:---|:---|:---|
| **Botulinum neurotoxin A** (BoNT/A) | SNAP-25 | Q197-R198 | Flaccid paralysis; longest duration (months) |
| **Botulinum neurotoxin B** (BoNT/B) | Synaptobrevin-2 | Q76-F77 | Flaccid paralysis |
| **Botulinum neurotoxin C** (BoNT/C) | Syntaxin-1A + SNAP-25 | Multiple | Flaccid paralysis |
| **Tetanus toxin** (TeNT) | Synaptobrevin-2 | Q76-F77 | Spastic paralysis (retrograde transport to inhibitory interneurons) |

BoNT/A is the basis of **botulinum toxin (Botox)** medical applications: cosmetic wrinkle reduction, focal hyperhidrosis, cervical dystonia, chronic migraine, overactive bladder — all via targeted blockade of exocytosis at neuromuscular junctions or autonomic terminals.

## Connections

- `expressed-by` → **[Neuron](../../04-cellular/neuron/README.md)** — neuronal SNAREs are the presynaptic vesicle fusion engine at every chemical synapse
- `acts-on` → **[Synapse](../../05-tissue/synapse/README.md)** — drives millisecond-timescale vesicle exocytosis underlying synaptic transmission
- `acts-on` → **[Acetylcholine](../acetylcholine/README.md)** — SNARE machinery releases acetylcholine vesicles at NMJs and cholinergic synapses; BoNT blockade of SNAREs causes flaccid paralysis by silencing ACh release
- `connects-to` → **[Myasthenia Gravis](../../07-system/myasthenia-gravis/README.md)** — the SNARE complex (VAMP2/synaptobrevin + SNAP-25 + syntaxin-1) at the motor nerve terminal mediates ACh vesicle fusion; ACh release via SNARE is intact in MG (disease is postsynaptic); BoNT cleaves SNARE → NMJ blockade that mimics but differs mechanistically from MG.

[^sudhof-rothman-2009-snare]: Sudhof TC, Rothman JE. Membrane fusion: grappling with SNARE and SM proteins. *Science.* 2009;323(5913):474-477. [doi:10.1126/science.1161748](https://doi.org/10.1126/science.1161748) · [PubMed 19164740](https://pubmed.ncbi.nlm.nih.gov/19164740/)
[^hanson-1997-nsf-snare]: Hanson PI et al. Structure and conformational changes in NSF and its membrane receptor complexes. *Cell.* 1997;90(3):523-535. [doi:10.1016/s0092-8674(00)80512-7](https://doi.org/10.1016/s0092-8674(00)80512-7) · [PubMed 9267031](https://pubmed.ncbi.nlm.nih.gov/9267031/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
