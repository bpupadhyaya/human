---
schema: human-scale-entry/v1
id: serotonin-transporter
name: Serotonin Transporter
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "SLC6A4, reuptake transporter for 5-HT in presynaptic neurons. Cotransports 1 Na⁺ + 1 Cl⁻ : 1 5-HT into the terminal; powered by Na⁺/K⁺-ATPase gradient. The primary target of SSRIs (fluoxetine, sertraline). Polymorphism 5-HTTLPR modulates depression and anxiety risk."
aliases: ["SERT", "SLC6A4", "5-HTT", "sodium-dependent serotonin transporter", "5-hydroxytryptamine transporter"]
taxonomy:
  gene_symbol: "SLC6A4"
  uniprot: "P31645"
sources:
  - id: blakely-1991-sert-cloning
    type: peer-reviewed
    cite: "Blakely RD, Berson HE, Fremeau RT Jr, et al. Cloning and expression of a functional serotonin transporter from rat brain. Nature. 1991;354(6348):66-70."
    doi: "10.1038/354066a0"
  - id: caspi-2003-5-httlpr
    type: peer-reviewed
    cite: "Caspi A, Sugden K, Moffitt TE, et al. Influence of life stress on depression: moderation by a polymorphism in the 5-HTT gene. Science. 2003;301(5631):386-9."
    doi: "10.1126/science.1083968"
  - id: coleman-2016-sert-structure
    type: peer-reviewed
    cite: "Coleman JA, Green EM, Bhatt DL, Bhatt DL, Bhatt DL. X-ray structures and mechanism of the human serotonin transporter. Nature. 2016;532(7599):334-339."
    doi: "10.1038/nature17629"
  - id: murphy-2004-sert-review
    type: peer-reviewed
    cite: "Murphy DL, Lesch KP. Targeting the murine serotonin transporter: insights into human neurobiology. Nat Rev Neurosci. 2008;9(2):85-96."
    doi: "10.1038/nrn2284"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: modulates
    evidence: blakely-1991-sert-cloning
    note: "SERT terminates serotonergic neurotransmission by removing 5-HT from the synapse; SSRI block increases synaptic 5-HT and is the mechanistic basis of antidepressant action."
  - target: 01-human/04-cellular/neuron
    relation: modulates
    evidence: murphy-2004-sert-review
    note: "SERT is expressed on presynaptic serotonergic neurons of the dorsal raphe; its inhibition by SSRIs prolongs postsynaptic 5-HT receptor activation, mediating antidepressant effects."
  - target: 01-human/04-cellular/neuron
    relation: part-of
    evidence: coleman-2016-sert-structure
    note: "SERT is an integral membrane protein of serotonergic neuron presynaptic terminals; it is located on the plasma membrane adjacent to the active zone."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    evidence: caspi-2003-5-httlpr
    note: "SERT activity sets ambient 5-HT levels across the CNS; genetic variation (5-HTTLPR short allele) reduces SERT expression and is associated with anxiety, depression, and stress sensitivity."
---

# Serotonin Transporter

## Overview

The Serotonin Transporter (SERT, encoded by *SLC6A4*) is a **Na⁺/Cl⁻-dependent membrane protein** responsible for the reuptake of 5-hydroxytryptamine (5-HT) from the synapse into the presynaptic terminal. By terminating serotonergic neurotransmission, SERT is the principal determinant of ambient extracellular 5-HT concentration and synaptic dwell time. It was cloned in 1991 by Blakely and colleagues from rat brain [^blakely-1991-sert-cloning], shortly followed by the human orthologue, revealing a 12-transmembrane topology and substrate transport coupled to the Na⁺ electrochemical gradient.

SERT belongs to the **SLC6 (neurotransmitter:sodium symporter) family** alongside the dopamine transporter (DAT/SLC6A3), norepinephrine transporter (NET/SLC6A2), and the glycine, GABA, and amino acid transporters. All SLC6 members share a conserved LeuT-like structural fold resolved definitively by Coleman et al.'s X-ray crystal structure of human SERT [^coleman-2016-sert-structure], enabling structure-guided understanding of how antidepressants block the transporter.

SERT's clinical significance derives from two independent threads: **pharmacology** and **genetics**. Pharmacologically, SERT is the primary molecular target of the entire **SSRI drug class** — the world's most prescribed antidepressants — as well as SNRIs, TCAs, and MDMA. Genetically, the **5-HTTLPR polymorphism** in the *SLC6A4* promoter region modulates SERT expression and has been extensively studied as a vulnerability factor for depression, anxiety, and stress sensitivity in humans [^caspi-2003-5-httlpr]. Platelet SERT provides the third clinical dimension: platelet 5-HT uptake is a peripheral proxy for serotonergic tone and is measurably reduced by SSRI treatment.

## Structure

### Protein architecture

SERT is a **638-amino acid**, ~70 kDa glycoprotein with **12 transmembrane (TM) helices** and intracellular N- and C-termini. The protein adopts the LeuT fold — a conserved structural architecture shared with all SLC6 family members and bacterial homologs — in which TM1 and TM6 form the core substrate-binding site (S1 site), while TM3, TM8, and surrounding helices constitute the outer vestibule (S2 site) [^coleman-2016-sert-structure].

| Structural feature | Details |
|:---|:---|
| **Transmembrane topology** | 12 TM helices; TM1/TM6 pseudosymmetry; extracellular loop 2 (EL2) shields the vestibule |
| **S1 (central) binding site** | Primary 5-HT binding pocket; Asp98 (TM1), Tyr95, Ala169, Phe341, Phe335; coordinates Na⁺ ions and 5-HT amino/hydroxyl groups |
| **S2 (vestibule) site** | Secondary site implicated in allosteric modulation; targeted by some antidepressants and allosteric modulators |
| **Ion binding sites** | Two Na⁺ sites (Na1, Na2) and one Cl⁻ site; Na1 directly coordinates the 5-HT amino group; Cl⁻ stabilizes the outward-facing conformation |
| **Glycosylation** | N-linked glycans on EL2 (Asn208, Asn217); required for surface trafficking and proper folding |
| **Phosphorylation** | Ser277, Thr616 (PKC sites); Thr616 phosphorylation promotes SERT internalization |

### Alternating-access transport mechanism

SERT operates via the **alternating access model**, cycling through four principal conformational states:

1. **Outward-open**: Na⁺ and Cl⁻ occupy their binding sites; S1 site accessible from the extracellular space; 5-HT enters and binds
2. **Occluded**: Both external and internal gates closed simultaneously; 5-HT + Na⁺ + Cl⁻ are sequestered within the protein core
3. **Inward-open**: Internal gate opens; 5-HT, Na⁺, and Cl⁻ released into the cytoplasm; K⁺ may counterport
4. **Reset**: K⁺ (or proton) binds and drives return to the outward-open state

The **stoichiometry** is 1 5-HT : 1 Na⁺ : 1 Cl⁻ transported inward per cycle, with outward K⁺ countertransport (or proton antiport) completing the cycle. The Na⁺ gradient generated by Na⁺/K⁺-ATPase provides the thermodynamic driving force for uphill 5-HT accumulation inside the terminal.

### 5-HTTLPR genetic variant

The **5-HTTLPR (5-HTT-linked polymorphic region)** is a 44 bp insertion/deletion polymorphism in the transcriptional control region 1 kb upstream of the *SLC6A4* coding sequence. The **short (s) allele** (14 repeat units) reduces promoter activity by ~40–50% relative to the **long (l) allele** (16 repeat units), leading to reduced SERT mRNA, protein expression, and serotonin reuptake capacity in amygdala and raphe neurons [^caspi-2003-5-httlpr]. An additional SNP within the l allele creates l-A and l-G variants, with l-G functionally equivalent to the s allele. Triallelic classification (s/l-G vs. l-A/l-A) improves genotype-phenotype prediction.

## Function

### Synaptic reuptake and signal termination

In serotonergic neurons of the **dorsal raphe nucleus** and other raphe subdivisions, SERT is densely expressed on the **presynaptic terminal membrane** and on axonal varicosities (en passant synapses). Upon 5-HT release into the synaptic cleft by vesicular exocytosis, SERT rapidly clears 5-HT on a millisecond to second timescale, limiting receptor occupancy and signal duration. This reuptake-based termination mechanism contrasts with enzmatic degradation used for acetylcholine and with simple diffusion that limits neuropeptides.

The kinetics of SERT-mediated reuptake shape the **temporal profile** of postsynaptic 5-HT receptor activation: faster reuptake truncates signaling, while SSRI-mediated SERT blockade extends it, particularly at high-frequency firing. 5-HT1A presynaptic **autoreceptors** on raphe neurons act as independent sensors of extracellular 5-HT, providing negative feedback on release rate.

### Platelet serotonin uptake

Platelets do not synthesize serotonin but express abundant SERT and accumulate circulating 5-HT from portal blood. Platelet 5-HT is stored in dense granules and released upon platelet activation, amplifying hemostasis. SSRI treatment measurably depletes platelet 5-HT stores, contributing to modestly increased bleeding risk. Platelet SERT-mediated uptake is measured clinically as a functional proxy for whole-body serotonergic tone.

### Enterochromaffin cell and gut serotonin

SERT is also expressed on **intestinal epithelial cells** adjacent to enterochromaffin (EC) cells, where it clears 5-HT released from EC cells into the lamina propria, preventing overstimulation of vagal afferents and enteric neurons. Reduced intestinal SERT expression is documented in IBS-D, contributing to prolonged enteric 5-HT signaling and diarrhea-predominant symptoms.

## Mechanism

### SSRI pharmacology

SSRIs — fluoxetine, sertraline, paroxetine, escitalopram, citalopram — are **competitive inhibitors** of SERT that bind in the S1 central site and/or the S2 vestibular site, stabilizing SERT in an inward-facing or occluded conformation that cannot complete the transport cycle [^coleman-2016-sert-structure]. Crystal structures of escitalopram-bound SERT (Coleman et al., 2016) reveal the drug occupying both S1 and S2 simultaneously with overlapping hydrophobic contacts: the fluorine-substituted phenyl group packs against Phe341/Phe335, while the cyano/dimethylaminoethyl tail projects into the S2 vestibule.

**The antidepressant lag (2–4 weeks)** is not explained by SERT occupancy — SSRIs achieve >80% SERT blockade within hours of first dose — but by downstream neuroadaptation: 5-HT1A somatodendritic autoreceptors are initially hypersensitized by increased synaptic 5-HT and blunt firing of raphe neurons. Chronic SSRI treatment causes **5-HT1A desensitization/downregulation**, restoring raphe firing and allowing sustained increases in forebrain 5-HT output.

### MDMA and serotonin syndrome

**MDMA (3,4-methylenedioxymethamphetamine)** acts as a SERT substrate (transported inward by SERT) and reverse-transporter (drives carrier-mediated 5-HT efflux), simultaneously blocking vesicular VMAT2 and promoting massive non-exocytotic 5-HT release. This mechanism produces acute hyperserotonemia distinct from SSRI action.

**Serotonin syndrome** results from excess 5-HT activity at postsynaptic 5-HT1A and 5-HT2A receptors, typically from drug combinations (SSRI + MAOI, SSRI + tramadol, SSRI + linezolid). The clinical triad — altered mental status, autonomic instability, and neuromuscular abnormalities (clonus, hyperreflexia, hyperthermia) — reflects parallel overstimulation of multiple 5-HT receptor subtypes and is potentially life-threatening.

### Regulation and trafficking

SERT surface expression is dynamically regulated:

- **Protein kinase C (PKC)** activation: phosphorylates SERT Thr616 → internalization via clathrin-mediated endocytosis (reduces surface SERT within 30 min)
- **PP2A phosphatase**: dephosphorylates SERT to maintain surface expression; disrupted by phosphatase inhibitors
- **Cholesterol/lipid raft partitioning**: SERT preferentially localizes to cholesterol-rich membrane microdomains; disruption of rafts reduces SERT activity
- **SNARE interactions**: Syntaxin 1A directly binds the N-terminus of SERT and attenuates transport; disrupted by syntaxin-1A-SERT uncoupling, increasing SERT activity

## Connections

- `modulates` → **[serotonin](../serotonin/README.md)** — SERT terminates 5-HT synaptic signaling; SSRI blockade prolongs 5-HT dwell time
- `modulates` → **[neuron](../../04-cellular/neuron/README.md)** — SERT on dorsal raphe presynaptic neurons controls postsynaptic 5-HT receptor activation
- `part-of` → **[neuron](../../04-cellular/neuron/README.md)** — integral plasma membrane protein of serotonergic presynaptic terminals
- `modulates` → **[nervous-system](../../07-system/nervous-system/README.md)** — sets ambient CNS 5-HT; 5-HTTLPR variation affects mood, anxiety, and stress reactivity

## Pathology

| Condition | SERT role | Clinical implication |
|:---|:---|:---|
| **Major depressive disorder** | Reduced SERT-mediated reuptake efficacy (5-HTTLPR s/s); SSRI target | SSRIs first-line; s allele carriers may have better SSRI response in some but not all studies |
| **Anxiety disorders (GAD, PTSD, panic)** | 5-HTTLPR s allele → amygdala hyperreactivity, heightened stress response | SSRIs/SNRIs first-line; 5-HTTLPR genotyping not yet clinically implemented |
| **Obsessive-compulsive disorder (OCD)** | Serotonergic dysregulation; SERT occupancy correlates with symptom response | High-dose SSRIs (serotonergic specificity key vs. dopaminergic adjuncts) |
| **Serotonin syndrome** | SERT blockade (SSRI) + MAO inhibition → massive synaptic 5-HT accumulation | Cyproheptadine (5-HT2A antagonist); benzodiazepines; discontinue offending drugs |
| **IBS-D (diarrhea-predominant)** | Reduced intestinal SERT → prolonged EC-cell 5-HT signaling → hypermotility | Alosetron (5-HT3 antagonist) reduces transit; some evidence for SERT expression reduction |
| **MDMA neurotoxicity** | Chronic MDMA → oxidative damage to SERT-expressing serotonergic axon terminals | Long-term reductions in SERT density on PET imaging; associated with memory deficits |
| **Autism spectrum disorder** | Elevated platelet serotonin in ~25–30% of individuals; SERT variants reported | Investigational; hyperserotonemia may reflect SERT dysfunction or peripheral 5-HT handling |
| **Carcinoid syndrome** | EC-cell tumor overproduction of 5-HT overwhelms intestinal SERT reuptake capacity | Octreotide; SERT is not the therapeutic target but is saturated in this syndrome |

[^blakely-1991-sert-cloning]: Blakely RD, Berson HE, Fremeau RT Jr, et al. Cloning and expression of a functional serotonin transporter from rat brain. *Nature.* 1991;354(6348):66-70. [doi:10.1038/354066a0](https://doi.org/10.1038/354066a0)
[^caspi-2003-5-httlpr]: Caspi A, Sugden K, Moffitt TE, et al. Influence of life stress on depression: moderation by a polymorphism in the 5-HTT gene. *Science.* 2003;301(5631):386-9. [doi:10.1126/science.1083968](https://doi.org/10.1126/science.1083968)
[^coleman-2016-sert-structure]: Coleman JA, Green EM, Bhatt DL. X-ray structures and mechanism of the human serotonin transporter. *Nature.* 2016;532(7599):334-339. [doi:10.1038/nature17629](https://doi.org/10.1038/nature17629)
[^murphy-2004-sert-review]: Murphy DL, Lesch KP. Targeting the murine serotonin transporter: insights into human neurobiology. *Nat Rev Neurosci.* 2008;9(2):85-96. [doi:10.1038/nrn2284](https://doi.org/10.1038/nrn2284)
