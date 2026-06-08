---
schema: human-scale-entry/v1
id: snca
name: SNCA
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "SNCA encodes alpha-synuclein, a presynaptic protein; point mutations (A53T, A30P, E46K) and copy number gains → toxic misfolding and Lewy body formation → dopaminergic neuron degeneration; prion-like propagation via synaptic connections drives Parkinson disease progression."
aliases: ["SNCA", "alpha-synuclein", "PARK1", "PARK4", "synuclein alpha", "alpha synuclein PD", "NACP", "alpha-synuclein Lewy body", "SNCA A53T", "synucleinopathy gene"]
cross_links:
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "SNCA missense mutations (A53T, A30P, E46K) and gene duplication/triplication cause familial PD; misfolded alpha-synuclein fibrils are the main component of Lewy bodies; SNCA propagates via synaptic connections following Braak staging from brainstem to neocortex."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Alpha-synuclein is cleared by macroautophagy and chaperone-mediated autophagy (CMA) via LAMP-2A; mutant SNCA (A53T) and oligomeric alpha-synuclein block CMA → aggregate accumulation; TFEB overexpression and mTOR inhibition rescue synuclein clearance in PD models."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Alpha-synuclein regulates dopamine synthesis and synaptic vesicle exocytosis via SNARE complex interactions; SNCA aggregation → impaired dopamine neurotransmission → motor circuit failure; preformed fibrils (PFFs) selectively kill dopaminergic neurons in PD models."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Alpha-synuclein and amyloid-beta co-aggregate in dementia with Lewy bodies (DLB), an overlap syndrome of AD and PD pathology; SNCA Lewy pathology accelerates tau spreading via prion-like mechanisms; ~10-15% of Alzheimer patients have concurrent Lewy body pathology."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "Cortical and limbic alpha-synuclein Lewy bodies define DLB; SNCA S129-phosphorylated fibrils compose Lewy bodies in both DLB and PD; alpha-synuclein SAA (RT-QuIC) in CSF or skin is >90% sensitive for DLB/PD; SNCA G51D mutation causes early-onset DLB-like syndrome."
sources:
  - id: polymeropoulos-1997-snca-pd
    type: peer-reviewed
    cite: "Polymeropoulos MH, Lavedan C, Leroy E, et al. Mutation in the alpha-synuclein gene identified in families with Parkinson's disease. Science. 1997;276(5321):2045-2047."
    doi: "10.1126/science.276.5321.2045"
    pmid: "9197268"
    url: "https://doi.org/10.1126/science.276.5321.2045"
  - id: spillantini-1997-lewy-body
    type: peer-reviewed
    cite: "Spillantini MG, Schmidt ML, Lee VM, Trojanowski JQ, Jakes R, Goedert M. Alpha-synuclein in Lewy bodies. Nature. 1997;388(6645):839-840."
    doi: "10.1038/42166"
    pmid: "9278044"
    url: "https://doi.org/10.1038/42166"
---

# SNCA

## Overview

**SNCA** (synuclein alpha) encodes **alpha-synuclein**, a 140 amino acid intrinsically disordered presynaptic protein expressed abundantly in dopaminergic neurons of the substantia nigra and throughout the central nervous system. Alpha-synuclein constitutes ~1% of total soluble brain protein. SNCA is the causal gene for **PARK1/PARK4**, autosomal dominant familial Parkinson disease (PD). Three landmark discoveries in 1997 established SNCA as the key PD gene: Polymeropoulos et al. identified the A53T missense mutation in Italian and Greek PD kindreds [^polymeropoulos-1997-snca-pd], and Spillantini et al. demonstrated alpha-synuclein as the principal component of Lewy bodies — the intraneuronal inclusions present in all sporadic PD [^spillantini-1997-lewy-body]. Gene duplication or triplication of the SNCA locus causes PD with dose-dependent severity: duplications → typical late-onset PD; triplications → early-onset PD with dementia and autonomic failure. These genetic data established that wild-type alpha-synuclein, when overexpressed or mutated, is sufficient to cause PD — making SNCA the central molecular driver of synucleinopathies.

**Familial SNCA mutations:**

| Mutation | Biochemical effect | Clinical phenotype |
|---|---|---|
| A53T | Accelerates fibril nucleation; most aggregation-prone | Typical PD, early onset (mean 45y) |
| A30P | Reduces membrane binding; increases oligomer formation | Typical PD |
| E46K | Increases membrane binding and fibril formation | PD + dementia |
| H50Q | Promotes fibril nucleation | Typical PD |
| G51D | Forms shorter, less toxic fibrils; mitochondrial localization | PD with very early onset |
| Duplication | 1.5–2× protein levels | Late-onset PD |
| Triplication | 2–3× protein levels | Early-onset PD + dementia + autonomic failure |

## Structure

Alpha-synuclein is intrinsically disordered in solution but adopts distinct conformations upon membrane binding and aggregation:

**N-terminal amphipathic helix domain (aa 1–60):** Contains seven 11-amino-acid imperfect repeats with the consensus KTKEGV; adopts an amphipathic α-helix upon binding to phospholipid membranes (particularly curved membranes enriched in acidic phospholipids). This region mediates synaptic vesicle association and interaction with SNARE proteins. All known pathogenic point mutations (A53T, A30P, E46K, H50Q, G51D) reside in this domain.

**NAC domain** (Non-Amyloid-β Component, aa 61–95): The hydrophobic core region essential for fibril formation. NAC is necessary and sufficient for amyloid aggregation; deletion of aa 71–82 abolishes aggregation entirely. NAC is absent from beta-synuclein and gamma-synuclein, explaining why only alpha-synuclein forms Lewy body fibrils.

**C-terminal acidic tail (aa 96–140):** Intrinsically disordered; enriched in Asp, Glu, and Pro residues; negatively charged; inhibits aggregation by folding back and shielding the NAC domain (intra-molecular interaction). Post-translational modifications here regulate aggregation: S129 phosphorylation (by CK1, GRK2/5) marks ~90% of Lewy body alpha-synuclein; S87 phosphorylation and Y125 nitration also occur. C-terminal truncation (by calpain-1, caspase-1) removes the auto-inhibitory tail and dramatically accelerates fibril nucleation.

**Lewy body fibril structure:** Alpha-synuclein forms parallel, in-register β-sheet fibrils (cryo-EM resolution: 3.4 Å). The fibril core spans residues 38–95; the NAC domain forms the cross-β spine; N-terminal repeats pack around the core. Different fibril polymorphs (rod, twister, ribbon) have been described with distinct seeding competencies.

## Function

Wild-type alpha-synuclein plays multiple physiological roles at the presynaptic terminal:

**Synaptic vesicle trafficking:** Alpha-synuclein clusters synaptic vesicles and modulates their reserve pool. It assists vesicle docking and fusion by interacting with the SNARE complex (via synaptobrevin/VAMP2 binding), promoting SNARE complex assembly. Alpha-synuclein triple knockout mice show normal viability but impaired neurotransmitter release kinetics and synaptic vesicle recycling defects.

**Dopamine homeostasis:** Alpha-synuclein inhibits tyrosine hydroxylase (TH) activity and promotes dopamine reuptake via DAT. Wild-type SNCA overexpression reduces intracellular dopamine levels; SNCA LOF leads to elevated dopamine turnover and oxidative stress from dopamine auto-oxidation.

**Chaperone activity:** Alpha-synuclein functions as a co-chaperone for CSPα (cysteine-string protein alpha) and assists SNARE complex disassembly via interactions with NSF (N-ethylmaleimide-sensitive factor).

**Mitochondrial homeostasis:** Alpha-synuclein localizes to mitochondrial membranes (particularly Complex I), modulating fusion/fission dynamics and respiratory chain activity.

## Mechanism

Alpha-synuclein aggregation follows a nucleation-polymerization mechanism with three kinetically distinct phases:

**Lag phase (nucleation):** Monomers populate partially folded β-sheet-rich conformations that self-associate into oligomeric nuclei. This phase is rate-limiting. Familial mutations (A53T) and post-translational modifications (S129 phosphorylation in the N-terminus, truncation) shorten the lag phase. Cellular membranes (particularly mitochondrial and ER-associated) serve as aggregation platforms.

**Elongation phase:** Oligomeric nuclei template monomer addition, forming protofibrils and fibrils. Dopamine-induced quinone products stabilize oligomers and inhibit fibril elongation — paradoxically increasing neurotoxic oligomer burden in dopaminergic neurons.

**Prion-like propagation:** Extracellular alpha-synuclein fibrils (released from dying neurons or via exosomes) are internalized by neighboring neurons and template the misfolding of endogenous alpha-synuclein — the molecular basis of Braak staging. PD pathology spreads from the brainstem (olfactory bulb, dorsal motor nucleus of vagus) to substantia nigra (Braak stage 3–4) and neocortex (Braak stage 5–6). Grafted fetal dopamine neurons in PD patients developed Lewy bodies 10–16 years post-transplant, providing human confirmation of prion-like spread.

**Downstream toxicity mechanisms:**
- Mitochondrial dysfunction: monomeric and oligomeric SNCA damage Complex I, increase ROS, and induce mitophagy failure
- ER stress: alpha-synuclein blocks ER-to-Golgi vesicle trafficking → UPR activation → apoptosis
- Proteasome inhibition: oligomers clog and impair the 26S proteasome, amplifying proteotoxic stress
- Neuroinflammation: extracellular alpha-synuclein activates microglia via TLR2/4, driving NLRP3 inflammasome → IL-1β release → dopaminergic neurotoxicity

## Connections

SNCA missense mutations (A53T, A30P, E46K) and gene duplication/triplication cause familial PD; misfolded alpha-synuclein fibrils are the main component of Lewy bodies; SNCA propagates via synaptic connections following Braak staging from brainstem to neocortex.

Alpha-synuclein is cleared by macroautophagy and chaperone-mediated autophagy (CMA) via LAMP-2A; mutant SNCA (A53T) and oligomeric alpha-synuclein block CMA → aggregate accumulation; TFEB overexpression and mTOR inhibition rescue synuclein clearance in PD models.

Alpha-synuclein regulates dopamine synthesis and synaptic vesicle exocytosis via SNARE complex interactions; SNCA aggregation → impaired dopamine neurotransmission → motor circuit failure; preformed fibrils (PFFs) selectively kill dopaminergic neurons in PD models.

Alpha-synuclein and amyloid-beta co-aggregate in dementia with Lewy bodies (DLB), an overlap syndrome of AD and PD pathology; SNCA Lewy pathology accelerates tau spreading via prion-like mechanisms; ~10-15% of Alzheimer patients have concurrent Lewy body pathology.

Cortical and limbic alpha-synuclein Lewy bodies (SNCA S129-phosphorylated fibrils) define DLB neuropathology; alpha-synuclein SAA (RT-QuIC) in CSF or skin is >90% sensitive for DLB/PD; SNCA G51D mutation causes early-onset DLB-like syndrome with prominent cortical Lewy bodies.
