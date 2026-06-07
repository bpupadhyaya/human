---
schema: human-scale-entry/v1
id: htt
name: HTT
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "HTT encodes huntingtin, a HEAT-repeat scaffold protein; CAG repeat expansion ≥36 in exon 1 → polyglutamine-expanded mHTT protein aggregation → striatal medium spiny neuron degeneration → Huntington disease; repeat length inversely predicts age of onset."
aliases: ["HTT", "huntingtin", "HD gene", "IT15", "polyglutamine HTT", "CAG repeat HD", "mHTT", "huntingtin protein", "polyQ expansion", "HD CAG"]
cross_links:
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "HTT CAG repeat ≥36 → polyglutamine mHTT aggregation → impaired proteostasis, mitochondrial dysfunction, and transcriptional dysregulation in striatal MSNs; caudate/putamen atrophy is the hallmark; juvenile HD (>60 CAG) presents with rigidity and seizures rather than chorea."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Mutant huntingtin (mHTT) sequesters p62/SQSTM1 and impairs autophagosome formation → defective selective autophagy → mHTT aggregate accumulation → neuronal proteotoxicity; mTOR inhibitors (rapamycin) and autophagy enhancers reduce mHTT burden in HD mouse models."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "mHTT causes preferential degeneration of striatal MSNs expressing D1 and D2 dopamine receptors; early loss of indirect pathway MSNs (D2) → dopamine pathway imbalance → chorea; tetrabenazine (VMAT2 inhibitor) depletes presynaptic dopamine → suppresses choreiform movements."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "mHTT aggregates activate caspase-3 and caspase-9 in striatal MSNs via mitochondrial pathway; mHTT N-terminal fragments (calpain-cleaved) amplify caspase activation; caspase-3 inhibition with z-DEVD-fmk is neuroprotective in HD mouse models, supporting apoptosis as a driver."
sources:
  - id: gusella-1983-htt-locus
    type: peer-reviewed
    cite: "Gusella JF, Wexler NS, Conneally PM, et al. A polymorphic DNA marker genetically linked to Huntington's disease. Nature. 1983;306(5940):234-238."
    doi: "10.1038/306234a0"
    pmid: "6316146"
    url: "https://doi.org/10.1038/306234a0"
  - id: macdonald-1993-htt-gene
    type: peer-reviewed
    cite: "The Huntington's Disease Collaborative Research Group. A novel gene containing a trinucleotide repeat that is expanded and unstable on Huntington's disease chromosomes. Cell. 1993;72(6):971-983."
    doi: "10.1016/0092-8674(93)90585-E"
    pmid: "8458085"
    url: "https://doi.org/10.1016/0092-8674(93)90585-E"
---

# HTT

## Overview

HTT (huntingtin) is a large, ubiquitously expressed scaffold protein encoded on chromosome 4p16.3. The wild-type protein contains a polyglutamine (polyQ) tract encoded by a CAG repeat in exon 1; normal alleles carry 6–35 repeats. Expansion to ≥36 CAG repeats causes Huntington disease (HD), an autosomal dominant neurodegenerative disorder. Alleles of 36–39 repeats show reduced penetrance; ≥40 repeats are fully penetrant. Repeat length above 60 causes juvenile-onset HD. Longer expansions arise preferentially through paternal transmission due to instability during spermatogenesis.

## Structure

The HTT protein is 3,144 amino acids (~348 kDa). The N-terminal exon-1-encoded segment carries the polyQ tract followed by a proline-rich region (PRR) that modulates aggregation propensity. The bulk of the protein consists of HEAT (Huntingtin, Elongation factor 3, protein phosphatase 2A, TOR) repeats arranged in a superhelical scaffold that mediates protein–protein interactions with >350 binding partners. Three major HEAT-repeat domains (HD1, HD2, HD3) fold around a central axis. Wild-type HTT participates in vesicle trafficking, transcriptional regulation (via HAP1, HIP1), and autophagy scaffolding. mHTT with an expanded polyQ adopts a β-sheet-rich amyloid conformation, forming perinuclear and cytoplasmic inclusion bodies (NIIs) that sequester transcription factors (CREB-binding protein, SP1) and proteasomal components.

## Function

Wild-type huntingtin functions as a cytoplasmic scaffold coordinating:
- **Vesicle trafficking**: Associates with HAP1, dynactin, and kinesin for BDNF-containing vesicle transport along corticostriatal axons; loss of this function starves MSNs of trophic support.
- **Autophagy scaffolding**: Recruits p62/SQSTM1 and ULK1 to nascent autophagosomes; promotes selective autophagy of damaged organelles and aggregate-prone proteins.
- **Transcription**: Sequesters REST/NRSF in the cytoplasm, permitting BDNF transcription; mHTT fails this function, causing nuclear REST accumulation and BDNF suppression.
- **Anti-apoptotic**: Wild-type HTT inhibits pro-caspase-9 activation and cytochrome c release; mHTT loses this property.

## Mechanism

Expanded polyQ (≥36 glutamines) promotes mHTT misfolding via a nucleation-dependent polymerization mechanism. The mHTT exon-1 fragment (generated by aberrant splicing or calpain cleavage) seeds amyloid-like aggregates more efficiently than full-length mHTT. Aggregation follows three pathways:
1. **Proteostasis overload**: mHTT saturates the UPS and autophagy systems, impairing clearance of other misfolded proteins.
2. **Transcriptional toxicity**: Nuclear mHTT co-aggregates with CBP/p300, reducing histone acetylation and silencing pro-survival genes (BDNF, PGC-1α).
3. **Mitochondrial dysfunction**: mHTT associates with the mitochondrial outer membrane, disrupts Complex II/III activity, and increases ROS → mtDNA damage → energy failure in high-demand MSNs.

Repeat length inversely determines age of onset: each additional CAG repeat above 36 lowers mean onset by ~3–4 years. The 50% of variance not explained by repeat length is attributed to modifier genes (MSH3, FAN1) affecting somatic repeat instability in striatum.

## Connections

HTT CAG repeat ≥36 → polyglutamine mHTT aggregation → impaired proteostasis, mitochondrial dysfunction, and transcriptional dysregulation in striatal MSNs; caudate/putamen atrophy is the hallmark; juvenile HD (>60 CAG) presents with rigidity and seizures rather than chorea.

Mutant huntingtin (mHTT) sequesters p62/SQSTM1 and impairs autophagosome formation → defective selective autophagy → mHTT aggregate accumulation → neuronal proteotoxicity; mTOR inhibitors (rapamycin) and autophagy enhancers reduce mHTT burden in HD mouse models.

mHTT causes preferential degeneration of striatal MSNs expressing D1 and D2 dopamine receptors; early loss of indirect pathway MSNs (D2) → dopamine pathway imbalance → chorea; tetrabenazine (VMAT2 inhibitor) depletes presynaptic dopamine → suppresses choreiform movements.

mHTT aggregates activate caspase-3 and caspase-9 in striatal MSNs via mitochondrial pathway; mHTT N-terminal fragments (calpain-cleaved) amplify caspase activation; caspase-3 inhibition with z-DEVD-fmk is neuroprotective in HD mouse models, supporting apoptosis as a driver.
