---
schema: human-scale-entry/v1
id: peripheral-nerve
name: Peripheral Nerve
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-06
summary: "Bundles of myelinated and unmyelinated axons organized by connective tissue layers. Schwann cells provide myelin for saltatory conduction; Remak bundles group unmyelinated C fibers. Regeneration after injury depends on Schwann cell scaffolding and axon regrowth rate (~1 mm/day)."
aliases: ["peripheral nerve trunk", "nerve fascicle", "somatic nerve"]
sources:
  - id: bhatheja-2006-schwann
    type: peer-reviewed
    cite: "Bhatheja K, Field J. Schwann cells: origins and role in axonal maintenance and regeneration. Int J Biochem Cell Biol. 2006;38(12):1995-1999."
    doi: "10.1016/j.biocel.2006.05.007"
    pmid: "16807057"
    url: "https://doi.org/10.1016/j.biocel.2006.05.007"
  - id: stassart-2018-axon-myelin
    type: peer-reviewed
    cite: "Stassart RM, Möbius W, Nave KA, Edgar JM. The axon-myelin unit in development and degenerative disease. Front Neurosci. 2018;12:467."
    doi: "10.3389/fnins.2018.00467"
    pmid: "30050403"
    url: "https://doi.org/10.3389/fnins.2018.00467"
  - id: scheib-2013-nerve-regeneration
    type: peer-reviewed
    cite: "Scheib J, Höke A. Advances in peripheral nerve regeneration. Nat Rev Neurol. 2013;9(12):668-676."
    doi: "10.1038/nrneurol.2013.227"
    pmid: "24217518"
    url: "https://doi.org/10.1038/nrneurol.2013.227"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: contains
    note: "Peripheral nerves consist of bundles of sensory, motor, and autonomic axons — the elongated processes of neurons whose cell bodies reside in dorsal root ganglia, cranial nerve ganglia, or ventral horn of spinal cord."
  - target: 01-human/05-tissue/guillain-barre
    relation: target-of
    note: "Guillain-Barré syndrome is an autoimmune attack on peripheral nerve myelin (AIDP) or axons (AMAN/AMSAN); peripheral nerve demyelination produces conduction block and ascending paralysis."
  - target: 01-human/07-system/nervous-system
    relation: part-of
    note: "Peripheral nerves are the anatomical conduits of the peripheral nervous system (PNS), carrying afferent sensory signals to the CNS and efferent motor/autonomic commands to effector organs."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "CIDP demyelinates peripheral nerves via macrophage-mediated paranodal stripping and anti-NF155/CNTN1 IgG4; NCS shows slowed conduction velocity, prolonged DML, F-wave prolongation, and conduction blocks; axonal loss secondary to chronic demyelination causes long-term disability."
---

# Peripheral Nerve

## Overview

A **peripheral nerve** is the organized tissue conduit of the peripheral nervous system (PNS): a bundle of axons — sensory, motor, and autonomic — encased in successive layers of connective tissue and supported by **Schwann cells**. Unlike central nervous system (CNS) white matter, peripheral nerves retain robust regenerative capacity after injury, owing largely to the persistence of Schwann cell basal lamina tubes (bands of Büngner) that guide regrowing axons to their targets.

The two defining structural classes of peripheral nerve fibers differ by myelination:
- **Myelinated axons (A and B fibers):** Each axon is individually ensheathed by a single Schwann cell, which spirals its membrane up to ~100 times around the axon to form compact myelin; interrupted at **nodes of Ranvier** where voltage-gated Na⁺ channels cluster, enabling **saltatory conduction** (action potential jumps node-to-node) at velocities up to 70 m/s
- **Unmyelinated axons (C fibers):** Groups of ~10 unmyelinated small-diameter axons wrapped (but not spiraled) together by a single Schwann cell (**Remak bundle**); conduct at 0.5–2 m/s; carry nociceptive, temperature, and postganglionic autonomic signals

The peripheral nervous system has no equivalent of the blood-brain barrier's tight junctions; instead, the **blood-nerve barrier** is formed by the perineurium (tight junctions between perineurial cells) and by endoneurial vessels (tight junction endothelium). Loss of barrier integrity contributes to nerve edema and neuropathy.

## Structure

### Connective tissue layers

Three concentric connective tissue sheaths organize the nerve [^stassart-2018-axon-myelin]:

**Endoneurium:** Loose connective tissue surrounding individual axons within a fascicle; contains fibroblasts, collagen type I/III, capillaries, and the endoneurial fluid (positive pressure). The Schwann cell basal lamina forms the innermost layer around each myelinated axon.

**Perineurium:** Dense cellular layers (3–15 layers of flattened perineurial cells linked by tight junctions) enclosing each fascicle; constitutes the **blood-nerve barrier**; maintains endoneurial fluid pressure and ionic homeostasis. Perineurial cells express alkaline phosphatase and are SMA+.

**Epineurium:** Outermost loose connective tissue sheath encasing the entire nerve trunk; contains adipose tissue, blood vessels (vasa nervorum), and lymphatics. The mesoneurium is a thin condensation that loosely tethers the nerve to surrounding structures and through which vascular supply enters.

### Schwann cells and myelin

**Schwann cells** are the defining glial cells of the PNS [^bhatheja-2006-schwann]:
- **Myelinating Schwann cells:** One cell per internode (200–1,500 μm length); spiral their membrane around the axon; compact myelin is formed by apposition of the cytoplasm-free inner leaflets (MBP, P0, and PMP22 hold the layers together); cytoplasmic channels (Schmidt-Lanterman incisures, paranodal loops) remain for metabolic communication with the axon
- **Non-myelinating (Remak) Schwann cells:** Embed multiple small C fibers in cytoplasmic tongues without compaction
- **Node of Ranvier:** 1–2 μm gap between adjacent myelin sheaths; flanked by paranodal loops; Nav1.6 channels clustered at >1,000/μm² (vs <5/μm² under myelin) — the site of action potential regeneration

### Fiber classification

| Fiber class | Diameter (μm) | Conduction velocity | Function |
|:---|:---|:---|:---|
| Aα | 12–20 | 70–120 m/s | Proprioception, motor (to skeletal muscle) |
| Aβ | 6–12 | 30–70 m/s | Touch, pressure, vibration |
| Aγ | 3–6 | 15–30 m/s | Motor to muscle spindles (intrafusal fibers) |
| Aδ | 1–5 | 5–30 m/s | Sharp pain, cold temperature, fast nociception |
| B | 1–3 | 3–15 m/s | Preganglionic autonomic |
| C | 0.2–1.5 | 0.5–2 m/s | Slow/burning pain, heat, postganglionic autonomic |

## Function

**Saltatory conduction (myelinated fibers):** Action potentials jump from node to node (Ranvier) without regenerating under the myelin sheath; this dramatically increases conduction velocity while reducing metabolic cost (Na⁺/K⁺-ATPase need only restore ion gradients at nodes, not along the full axon).

**Axonal transport:** Motor proteins (kinesin: anterograde; dynein: retrograde) move organelles, vesicles, and signaling molecules along microtubule tracks within axons — even over meter-long distances in sciatic or ulnar nerves.

**Regeneration [^scheib-2013-nerve-regeneration]:** After axotomy, the distal nerve stump undergoes **Wallerian degeneration** (axon and myelin breakdown within days); Schwann cells dedifferentiate, proliferate, and align within the basal lamina tube to form **bands of Büngner** — growth-promoting channels that guide regenerating axon sprouts from the proximal stump at ~1–3 mm/day. Functional recovery depends on accurate target reinnervation; this is why long nerve gaps (>3 cm) often require conduit repair or nerve grafting.

**Clinical pathology:**
- **Demyelinating neuropathies** (Guillain-Barré AIDP, CIDP, CMT1): Schwann cell/myelin damage → conduction slowing/block → weakness and sensory loss; repair possible if axons intact
- **Axonal neuropathies** (AMAN, diabetic neuropathy, toxic): direct axon loss → permanent denervation if extensive; regeneration limited by distance
- **Entrapment neuropathies** (carpal tunnel, cubital tunnel): focal compression → ischemia and paranodal demyelination at constriction sites

## Connections

- `contains` → **[Neuron](../../04-cellular/neuron/README.md)** — peripheral nerves bundle the axons of sensory (DRG), motor (ventral horn), and autonomic neurons; the nerve is essentially the axon tract of the peripheral nervous system.
- `target-of` → **[Guillain-Barré Syndrome](../guillain-barre/README.md)** — AIDP/AMAN/AMSAN are autoimmune attacks on peripheral nerve myelin and axons; demyelination produces conduction block and ascending paralysis.
- `part-of` → **[Nervous System](../../07-system/nervous-system/README.md)** — peripheral nerves form the afferent and efferent limbs of the PNS, connecting the CNS to all peripheral sensory receptors, muscles, and autonomic targets.
- `connects-to` → **[CIDP](../../07-system/cidp/README.md)** — CIDP demyelinates peripheral nerves via macrophage-mediated paranodal stripping and anti-NF155/CNTN1 IgG4 antibodies; NCS shows slowed conduction velocity, conduction blocks, and F-wave prolongation; efgartigimod (ADHERE; FDA Jun 2024) is now approved.

[^bhatheja-2006-schwann]: Bhatheja K, Field J. Schwann cells: origins and role in axonal maintenance and regeneration. *Int J Biochem Cell Biol.* 2006;38(12):1995-1999. [doi:10.1016/j.biocel.2006.05.007](https://doi.org/10.1016/j.biocel.2006.05.007) · [PubMed 16807057](https://pubmed.ncbi.nlm.nih.gov/16807057/)
[^stassart-2018-axon-myelin]: Stassart RM, Möbius W, Nave KA, Edgar JM. The axon-myelin unit in development and degenerative disease. *Front Neurosci.* 2018;12:467. [doi:10.3389/fnins.2018.00467](https://doi.org/10.3389/fnins.2018.00467) · [PubMed 30050403](https://pubmed.ncbi.nlm.nih.gov/30050403/)
[^scheib-2013-nerve-regeneration]: Scheib J, Höke A. Advances in peripheral nerve regeneration. *Nat Rev Neurol.* 2013;9(12):668-676. [doi:10.1038/nrneurol.2013.227](https://doi.org/10.1038/nrneurol.2013.227) · [PubMed 24217518](https://pubmed.ncbi.nlm.nih.gov/24217518/)
