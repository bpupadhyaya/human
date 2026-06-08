---
schema: human-scale-entry/v1
id: rig-i
name: RIG-I
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "RIG-I (DDX58; DExD/H-box helicase) senses cytosolic 5′ppp ssRNA and blunt-ended dsRNA ≤300 bp → TRIM25 K63-ubiquitination of CARD1 Lys172 → MAVS CARD-CARD interaction → TBK1 → IRF3 → IFN-β; NS1 (influenza) and NS4B (dengue) inhibit RIG-I; MDA5 senses long dsRNA in parallel."
aliases: ["RIG-I", "DDX58", "retinoic acid-inducible gene I", "RIG-I helicase", "RIG-I/MDA5", "cytosolic RNA sensor", "RIGI", "innate RNA helicase", "antiviral helicase", "5-ppp RNA sensor", "DExD-H box"]
sources:
  - id: yoneyama-2004-rig-i-discovery
    type: peer-reviewed
    cite: "Yoneyama M, Kikuchi M, Natsukawa T, et al. The RNA helicase RIG-I has an essential function in double-stranded RNA-induced innate antiviral responses. Nat Immunol. 2004;5(7):730-737."
    doi: "10.1038/ni1087"
    pmid: "15208624"
    url: "https://doi.org/10.1038/ni1087"
    accessed: "2026-06-08"
  - id: loo-2011-rig-i-signaling
    type: peer-reviewed
    cite: "Loo YM, Gale M Jr. Immune signaling by RIG-I-like receptors. Immunity. 2011;34(5):680-692."
    doi: "10.1016/j.immuni.2011.05.003"
    pmid: "21616437"
    url: "https://doi.org/10.1016/j.immuni.2011.05.003"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "RIG-I CARD domains (K63-ubiquitinated by TRIM25) interact with MAVS CARD via homotypic CARD-CARD contacts → nucleate MAVS prion-like filament on OMM → TRAF3 → TBK1 → IRF3 → IFN-β; MAVS is the essential adaptor: cells with MAVS knockout cannot respond to RIG-I ligands."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "RIG-I → MAVS → TRAF3 → TBK1 → IRF3 Ser396 phosphorylation → IRF3 homodimerization → IFN-β enhanceosome (IRF3 + NF-κB + AP-1); IRF3 is the terminal transcriptional endpoint of RIG-I signaling; IRF3 LOF abrogates IFN-β induction from all RIG-I-activating viruses."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Influenza A 5′ppp negative-sense genomic ssRNA and blunt-ended dsRNA replication intermediates are the canonical RIG-I ligands; NS1 blocks RIG-I by: (1) sequestering dsRNA, (2) binding and inhibiting TRIM25; NS1 IFN antagonism strength correlates with pandemic potential."
  - target: 01-human/07-system/zika-virus
    relation: connects-to
    note: "ZIKV positive-sense genomic RNA and dsRNA replication intermediates activate RIG-I/MDA5 → MAVS → IFN-β; adult cells robustly respond; fetal neural progenitor cells (NPCs) have reduced RIG-I/MAVS expression → impaired IFN-β → ZIKV replicates unchecked in NPCs → microcephaly."
---

# RIG-I

## Overview

**RIG-I** (Retinoic acid-Inducible Gene I; DDX58) is the founding member of the **RIG-I-like receptor (RLR) family** of cytosolic RNA helicases that sense viral RNA in the cytoplasm and trigger innate antiviral immunity. Identified by Yoneyama et al. in 2004 [^yoneyama-2004-rig-i-discovery], RIG-I is expressed basally in nearly all cell types and is strongly upregulated by type I IFN (it is itself an interferon-stimulated gene). It functions as a molecular sentinel for **cytosolic viral RNA** — specifically short double-stranded RNA and 5′-triphosphate (5′ppp) RNA structures that are absent from the normal cytoplasmic RNA pool of uninfected cells.

The RLR family comprises three members:
- **RIG-I** (DDX58): Senses 5′ppp ssRNA, blunt-ended dsRNA ≤300 bp — primary sensor for influenza, SARS-CoV-2 DI particles, RSV, Sendai virus, Ebola virus
- **MDA5** (IFIH1): Senses long dsRNA (>1 kb) and dsRNA without 5′ppp — primary sensor for picornaviruses (EMCV, poliovirus), MRE11 RNA, retroviruses; GOF mutations in MDA5 cause Aicardi-Goutières syndrome
- **LGP2** (DHX58): Lacks CARD domains; regulates RIG-I and MDA5 activity; required for efficient MDA5 signaling

All three signal through the common adapter **MAVS** on the outer mitochondrial membrane → TBK1 → IRF3/IRF7 → type I IFN production.

## Structure

### RIG-I protein (~106 kDa, 925 aa)

RIG-I adopts an autoinhibited, compact conformation in resting cells:

- **N-terminal CARD domains** (CARD1: aa 1–91; CARD2: aa 91–184): Two tandem CARDs; interact with MAVS CARD upon activation; autoinhibited in the resting state by the CTD folding back onto the CARD
- **Pincer domain** (aa 185–321): Connects CARD2 to helicase domain; regulates conformational dynamics
- **DExD/H-box helicase domain** (aa 322–795): Two RecA-like subdomains (Hel1 and Hel2); ATP-dependent dsRNA unwinding; encircles the RNA duplex in a ring-clamp configuration upon activation; Hel2i insert subdomain is critical for ligand specificity
- **C-terminal domain (CTD, aa 796–925)**: Zinc-binding repressor domain; recognizes blunt-ended dsRNA and 5′ppp moieties; in resting state contacts CARD2 → autoinhibited; RNA binding releases this contact

**Autoinhibition model:**
- Resting RIG-I: CTD folds against CARD2 → CARDs sequestered, inaccessible to TRIM25 or MAVS
- 5′ppp RNA binding to CTD: Releases the CTD-CARD2 contact → CARD domains exposed
- TRIM25 K63-ubiquitinates CARD1 Lys172 → stabilizes open conformation → MAVS interaction enabled

### MDA5 comparison

| Feature | RIG-I | MDA5 |
|---------|-------|------|
| Gene | DDX58 | IFIH1 |
| RNA ligand | 5′ppp ssRNA, dsRNA ≤300 bp | Long dsRNA (>1 kb), poly(I:C) |
| Ubiquitination | TRIM25 K63-Ub Lys172 | Riplet? (mechanism less defined) |
| Sensing | Influenza, SARS-CoV-2, RSV, EBOV | Picornaviruses, EMCV, MRE11 RNA |
| Clinical relevance | NS1 target (flu); NSP3 target (CoV) | GOF → AGS; LOF → susceptibility |

## Function

1. **Antiviral IFN induction**: Primary cytosolic RNA sensor for most RNA viruses; triggers MAVS → TBK1 → IRF3/IRF7 → IFN-β/IFN-α within 1–4 h of infection
2. **NF-κB activation** (via MAVS → TRAF6 → IKKβ): Pro-inflammatory cytokines (TNF-α, IL-6) parallel IFN induction
3. **Apoptosis**: RIG-I can directly induce apoptosis in infected cells via CARD-mediated interaction with pro-caspase-8 (FADD/RIP1 complex)
4. **Tumor immunology**: RIG-I agonists (poly(I:C), 5′ppp dsRNA) activate innate immunity in tumors → anti-tumor IFN-β; RIG-I agonists can induce apoptosis in cancer cells independently of immune cells
5. **Self-RNA discrimination**: RIG-I selectively ignores cellular RNA via: (a) 5′ppp cap modifications (m7GTP cap) on host mRNAs; (b) 2′-O-methylation of first nucleotide of cellular RNA by CMTR1 prevents CTD binding; (c) cellular dsRNA generally lacks blunt ends >8 bp

## Mechanism

### Canonical RIG-I activation

1. Viral RNA enters cytoplasm (after endosomal uncoating or cytosolic replication)
2. **RNA recognition**: 5′ppp ssRNA or blunt-ended dsRNA binds CTD → CTD-CARD2 contact releases → CARD domains exposed
3. **TRIM25 ubiquitination**: TRIM25 (E3 ligase) catalyzes K63-linked polyubiquitin chain on CARD1 Lys172; alternatively, unanchored K63 poly-Ub chains bind RIG-I CARD2
4. **Helicase engagement**: RIG-I encircles RNA duplex via helicase + CTD → stable RIG-I–RNA complex (multiple RIG-I monomers assemble on one RNA molecule)
5. **MAVS CARD interaction**: K63-Ub RIG-I CARD contacts MAVS CARD via electrostatic complementarity → template MAVS monomer for prion-like filament propagation
6. **Downstream signaling**: MAVS filament → TRAF3/TRAF6 → TBK1 → IRF3 (Ser396 phosphorylation) + NF-κB → IFN-β and inflammatory cytokines

### Negative regulation of RIG-I

- **NLRX1**: Mitochondrial NLR protein competes with MAVS for RIG-I CARD binding → attenuates excessive antiviral signaling
- **PCBP2 and AIP4**: K48-ubiquitination of MAVS → proteasomal degradation → terminates RIG-I signaling
- **A20 (TNFAIP3)**: Deubiquitinase removes K63-Ub from RIG-I CARD1 → reduces MAVS activation
- **USP21**: Deubiquitinase that removes K63-Ub from RIG-I → negative feedback ISG
- **CYLD**: Deubiquitinase active on RIG-I and MAVS K63-chains → attenuates IFN induction

### Viral inhibition of RIG-I

| Virus | Protein | Mechanism |
|-------|---------|-----------|
| Influenza A | NS1 | Binds TRIM25 (blocks K63-Ub); sequesters 5′ppp dsRNA; E96/E97/K102 residues on NS1 mediate TRIM25 binding |
| Dengue/Zika | NS4B | Blocks RIG-I signaling; exact mechanism may involve RIG-I CARD sequestration |
| SARS-CoV-2 | NSP14 | N7-methyltransferase caps viral RNA → avoids 5′ppp detection; NSP1 blocks translation |
| HCV | NS3/4A | Cleaves MAVS downstream (see MAVS entry) |
| Ebola | VP35 | dsRNA binding protein; sequesters dsRNA → RIG-I not activated; critical virulence factor |
| Picornaviruses | L-protein | Directly cleaves RIG-I CARD domains; enteroviruses also cleave via 3Cpro |
| Vaccinia | E3L | dsRNA binding protein; IFN-resistant vaccinia strains lack functional E3L |

## Connections

**→ [MAVS](../mavs/)**: RIG-I CARD domains (K63-ubiquitinated by TRIM25) interact with MAVS CARD via homotypic CARD-CARD contacts → nucleate MAVS prion-like filament on OMM → TRAF3 → TBK1 → IRF3 → IFN-β; MAVS is the essential adaptor: cells with MAVS knockout cannot respond to RIG-I ligands.

**→ [IRF3](../irf3/)**: RIG-I → MAVS → TRAF3 → TBK1 → IRF3 Ser396 phosphorylation → IRF3 homodimerization → IFN-β enhanceosome (IRF3 + NF-κB + AP-1); IRF3 is the terminal transcriptional endpoint of RIG-I signaling; IRF3 LOF abrogates IFN-β induction from all RIG-I-activating viruses.

**→ [Influenza](../../../07-system/influenza/)**: Influenza A 5′ppp negative-sense genomic ssRNA and blunt-ended dsRNA replication intermediates are the canonical RIG-I ligands; NS1 blocks RIG-I by: (1) sequestering dsRNA, (2) binding and inhibiting TRIM25; NS1 IFN antagonism strength correlates with pandemic potential.

**→ [Zika Virus](../../../07-system/zika-virus/)**: ZIKV positive-sense genomic RNA and dsRNA replication intermediates activate RIG-I/MDA5 → MAVS → IFN-β; adult cells robustly respond; fetal neural progenitor cells (NPCs) have reduced RIG-I/MAVS expression → impaired IFN-β → ZIKV replicates unchecked in NPCs → microcephaly.
