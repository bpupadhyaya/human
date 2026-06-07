---
schema: human-scale-entry/v1
id: lrrk2
name: LRRK2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "LRRK2 encodes a dual GTPase-kinase; G2019S (most common pathogenic variant) hyperactivates LRRK2 kinase → Rab GTPase hyperphosphorylation → autophagy and vesicle trafficking dysfunction → α-synuclein accumulation; LRRK2 inhibitors are in Phase 2 trials for Parkinson disease."
aliases: ["LRRK2", "leucine-rich repeat kinase 2", "PARK8", "dardarin", "LRRK2 G2019S", "LRRK2 kinase", "LRRK2 Parkinson", "LRRK2 inhibitor", "ROCO protein", "LRRK2 GTPase"]
cross_links:
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "LRRK2 G2019S (~1-2% of sporadic PD, ~40% penetrance by age 80) is the most common pathogenic variant causing familial PD; LRRK2 kinase hyperactivation → Rab GTPase hyperphosphorylation → vesicle trafficking defects and α-synuclein aggregation in dopaminergic neurons."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "LRRK2 regulates autophagy via phosphorylation of Rab7 and Beclin-1 complexes; G2019S LRRK2 impairs autophagic flux → α-synuclein accumulation; LRRK2 inhibitors restore autophagy in G2019S iPSC-derived dopaminergic neurons; Rab7 hyperphosphorylation impairs lysosomal maturation."
  - target: 01-human/03-molecular/snca
    relation: connects-to
    note: "LRRK2 G2019S and SNCA A53T cause familial PD via convergent mechanisms; G2019S Rab hyperphosphorylation impairs α-synuclein vesicle trafficking → aggregation; LRRK2 and α-synuclein physically interact; LRRK2 kinase inhibition reduces α-synuclein aggregation in G2019S neurons."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "LRRK2 regulates mTORC1 via Rab7 phosphorylation at lysosomes; G2019S LRRK2 hyperactivates mTORC1 → reduced TFEB nuclear translocation → defective lysosomal biogenesis; rapamycin rescues lysosomal function and reduces α-synuclein accumulation in G2019S iPSC-derived neurons."
sources:
  - id: zimprich-2004-lrrk2-pd
    type: peer-reviewed
    cite: "Zimprich A, Biskup S, Leitner P, et al. Mutations in LRRK2 cause autosomal-dominant parkinsonism with pleomorphic pathology. Neuron. 2004;44(4):601-607."
    doi: "10.1016/j.neuron.2004.11.005"
    pmid: "15541309"
    url: "https://doi.org/10.1016/j.neuron.2004.11.005"
  - id: steger-2017-lrrk2-rab
    type: peer-reviewed
    cite: "Steger M, Tonelli F, Ito G, et al. Phosphoproteomics reveals that Parkinson's disease kinase LRRK2 regulates a subset of Rab GTPases. Elife. 2017;6:e22289."
    doi: "10.7554/eLife.22289"
    pmid: "28071628"
    url: "https://doi.org/10.7554/eLife.22289"
---

# LRRK2

## Overview

**LRRK2** (leucine-rich repeat kinase 2; also **dardarin**, from Basque for "tremor") is a large, multi-domain kinase encoded by the PARK8 locus on chromosome 12q12. At 2,527 amino acids (~286 kDa), LRRK2 is one of the largest human kinases. Zimprich et al. (2004) identified LRRK2 mutations as the cause of autosomal dominant Parkinson disease in multiple families [^zimprich-2004-lrrk2-pd]. The **G2019S** missense mutation in the kinase domain is the most prevalent pathogenic variant: it is found in ~1–2% of sporadic PD cases in European populations, ~15–20% of Ashkenazi Jewish PD cases, and ~40% of North African Arab PD cases. G2019S has ~40% lifetime penetrance by age 80.

LRRK2 belongs to the **ROCO (Ras-of-complex proteins)** family, defined by a tandem Roc-COR GTPase module that regulates the adjacent kinase domain. Unlike most kinases, LRRK2 has both GTPase and kinase activity, enabling bidirectional autoinhibition. Steger et al. (2017) used phosphoproteomics to identify a subset of Rab GTPases as the principal LRRK2 substrates — Rab8A (Thr72), Rab10 (Thr73), Rab35 (Thr72), and several others — establishing the mechanistic link between LRRK2 kinase hyperactivation and vesicle trafficking dysfunction [^steger-2017-lrrk2-rab].

**LRRK2 pathogenic mutations:**

| Mutation | Domain | Effect | Penetrance |
|---|---|---|---|
| G2019S | Kinase | ~2-3× kinase hyperactivation | ~40% by age 80 |
| R1441C/G/H | Roc GTPase | Impairs GTP hydrolysis → altered kinase activation | High (~>70% by age 80 for R1441G) |
| Y1699C | COR | Disrupts Roc-COR interface | High |
| I2020T | Kinase | Modest kinase hyperactivation | High |
| N1437H | Roc | Impairs GTP hydrolysis | High |

## Structure

LRRK2 contains seven structural domains arranged N- to C-terminally:

**ANK (ankyrin repeat) domain (aa 692–860):** Mediates protein-protein interactions; binds FADD, Akt, 14-3-3 proteins; anchors LRRK2 to the plasma membrane.

**LRR (leucine-rich repeat) domain (aa 984–1278):** 13 LRR motifs; involved in substrate recognition and protein scaffolding; mutations here affect interactome composition.

**Roc (Ras-of-complex) GTPase domain (aa 1335–1516):** Binds and hydrolyzes GTP; GTP binding activates LRRK2 kinase; R1441 mutations here impair GTPase activity → LRRK2 locked in GTP-bound (active) state → constitutive kinase activation.

**COR (C-terminal of Roc) domain (aa 1517–1836):** Acts as a GTPase effector arm; mediates dimerization; Y1699C mutation disrupts Roc-COR interface.

**Kinase domain (aa 1879–2138):** Serine/threonine kinase; Mg²⁺-dependent; G2019S mutation in the DYGφ activation loop → increased Vmax for substrate phosphorylation ~2–3-fold. The kinase is autoinhibited by the N-terminal LRR-Roc-COR module.

**WD40 domain (aa 2142–2527):** Seven-bladed β-propeller; serves as a scaffold for Rab substrate engagement; required for pT-Rab recognition.

**Dimerization:** LRRK2 forms dimers via the COR and WD40 domains; G2019S hyperactivation occurs in the dimeric state.

## Function

Wild-type LRRK2 coordinates multiple cellular processes:

**Rab GTPase regulation:** LRRK2 phosphorylates a switch-II-adjacent residue (Thr/Ser) on ~14 Rab GTPases. Phospho-Rab8A and phospho-Rab10 recruit RILPL1/RILPL2 effectors → regulate ciliogenesis and vesicle docking at the trans-Golgi network (TGN). Non-phosphorylated Rabs interact with alternative effectors (rabaptin-5, Rabenosyn-5) for endolysosomal trafficking. LRRK2 thus functions as a "Rab kinase switch" that routes vesicles to different destinations.

**Autophagy regulation:** LRRK2 interacts with Beclin-1 and Rubicon to modulate autophagosome nucleation; phosphorylates Rab7 (Ser72) to regulate late endosome-lysosome fusion and autophagic flux; controls lysosomal pH via Rab7-dependent V-ATPase assembly.

**Mitochondrial dynamics:** LRRK2 phosphorylates Miro1 and Miro2 (mitochondrial Rho GTPases) at the outer mitochondrial membrane → regulates mitochondrial motility along axons → controls local ATP supply and mitophagy clearance.

**Innate immune signaling:** LRRK2 is highly expressed in macrophages and dendritic cells; promotes NF-κB and NFAT activation downstream of TLR2 and NOD2; LRRK2 knockout mice have impaired mycobacterial clearance. LRRK2 inhibitors dampen IL-6 and TNF-α production.

## Mechanism

**G2019S kinase hyperactivation:** The G2019S substitution (Gly→Ser in the DYGφ motif of the activation loop) destabilizes the inactive kinase conformation. The Ser2019 hydroxyl makes a hydrogen bond with Arg1823, holding the activation loop in the active position and increasing substrate turnover ~2–3-fold.

**Pathogenic cascade:**
1. G2019S → excess Rab phosphorylation (especially pRab8A, pRab10, pRab35) in neurons
2. Hyperphosphorylated Rabs fail to associate with normal effectors → TGN-to-lysosome trafficking defects → impaired α-synuclein clearance via endolysosomal pathway
3. Impaired Rab7 cycling → defective late endosome maturation → reduced autophagic flux → α-synuclein aggregate accumulation
4. Mitochondrial Miro1 hyperphosphorylation → impaired mitophagy → damaged mitochondria accumulate in dopaminergic axons

**LRRK2 inhibitors (clinical development):**
- DNL201 (Denali): oral, brain-penetrant type I kinase inhibitor; Phase 1/2 showed pRab10 reduction in CSF and leukocytes; lung toxicity signal (reversible vacuolation, class effect of LRRK2 kinase inhibition in type II pneumocytes) requires monitoring
- BIIB094: antisense oligonucleotide targeting LRRK2 mRNA; intrathecal delivery; Phase 2 trial ongoing for G2019S carriers and sporadic PD
- MLi-2: highly selective tool compound; reduced pRab10 in mouse brain by >90%

## Connections

LRRK2 G2019S (~1-2% of sporadic PD, ~40% penetrance by age 80) is the most common pathogenic variant causing familial PD; LRRK2 kinase hyperactivation → Rab GTPase hyperphosphorylation → vesicle trafficking defects and α-synuclein aggregation in dopaminergic neurons.

LRRK2 regulates autophagy via phosphorylation of Rab7 and Beclin-1 complexes; G2019S LRRK2 impairs autophagic flux → α-synuclein accumulation; LRRK2 inhibitors restore autophagy in G2019S iPSC-derived dopaminergic neurons; Rab7 hyperphosphorylation impairs lysosomal maturation.

LRRK2 G2019S and SNCA A53T cause familial PD via convergent mechanisms; G2019S Rab hyperphosphorylation impairs α-synuclein vesicle trafficking → aggregation; LRRK2 and α-synuclein physically interact; LRRK2 kinase inhibition reduces α-synuclein aggregation in G2019S neurons.

LRRK2 regulates mTORC1 via Rab7 phosphorylation at lysosomes; G2019S LRRK2 hyperactivates mTORC1 → reduced TFEB nuclear translocation → defective lysosomal biogenesis; rapamycin rescues lysosomal function and reduces α-synuclein accumulation in G2019S iPSC-derived neurons.
