---
schema: human-scale-entry/v1
id: nlrp3-inflammasome
name: NLRP3 Inflammasome
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Cytosolic multiprotein danger-sensing complex (NLRP3/ASC/caspase-1) activated by PAMPs and DAMPs. Processes pro-IL-1β and pro-IL-18 to active cytokines and triggers pyroptosis via gasdermin D pore formation."
aliases: ["NLRP3", "NALP3 inflammasome", "cryopyrin", "CIAS1", "PYPAF1"]
sources:
  - id: martinon-2002-inflammasome
    type: peer-reviewed
    cite: "Martinon F, Burns K, Tschopp J. The inflammasome: a molecular platform triggering activation of inflammatory caspases and processing of proIL-beta. Mol Cell. 2002;10(2):417-426."
    doi: "10.1016/s1097-2765(02)00599-3"
    pmid: "12191486"
  - id: swanson-2019-pyroptosis-review
    type: peer-reviewed
    cite: "Swanson KV, Deng M, Ting JP. The NLRP3 inflammasome: molecular activation and regulation to therapeutics. Nat Rev Immunol. 2019;19(8):477-489."
    doi: "10.1038/s41577-019-0165-0"
    pmid: "31036962"
  - id: duewell-2010-crystal-nlrp3
    type: peer-reviewed
    cite: "Duewell P, Kono H, Rayner KJ, et al. NLRP3 inflammasomes are required for atherogenesis and activated by cholesterol crystals. Nature. 2010;464(7293):1357-1361."
    doi: "10.1038/nature08938"
    pmid: "20428172"
  - id: shi-2017-gasdermin-pore
    type: peer-reviewed
    cite: "Shi J, Zhao Y, Wang K, et al. Cleavage of GSDMD by inflammatory caspases determines pyroptotic cell death. Nature. 2015;526(7575):660-665."
    doi: "10.1038/nature15514"
    pmid: "26375003"
cross_links:
  - target: 01-human/03-molecular/il-6
    relation: modulates
    note: "NLRP3 inflammasome activation triggers IL-1β release, which drives IL-6 production from stromal and immune cells, amplifying systemic inflammation."
  - target: 01-human/03-molecular/nf-kb
    relation: modulated-by
    note: "NF-κB provides the 'Signal 1' priming for NLRP3 transcription and pro-IL-1β synthesis; NLRP3 activation in turn further activates NF-κB via caspase-1-independent mechanisms."
  - target: 01-human/04-cellular/dendritic-cell
    relation: expressed-by
    note: "Dendritic cells express high levels of NLRP3 and are primary inflammasome-activating innate sentinel cells; DC pyroptosis promotes antigen cross-presentation."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "IL-1β and IL-18 released by NLRP3-activated macrophages and DCs drive Th17 polarization and NK cell IFN-γ production, shaping adaptive immunity."
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "NLRP3 is a core sensor of the innate immune system, integrating cellular danger signals into a proteolytic activation cascade that initiates inflammation."
  - target: 01-human/06-organ/heart
    relation: modulates
    note: "NLRP3 inflammasome drives sterile myocardial inflammation post-MI; cholesterol crystals in atherosclerotic plaques are potent NLRP3 activators driving vascular inflammation."
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "NLRP3 contributes to renal tubular injury and interstitial fibrosis in AKI and CKD; urate crystals activate NLRP3 in renal tubular epithelium."
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulates
    note: "TNF-α provides NF-κB-mediated priming (Signal 1) for NLRP3 expression; NLRP3-derived IL-1β synergizes with TNF-α in inflammatory signaling cascades."
---

# NLRP3 Inflammasome

## Overview

The NLRP3 inflammasome is a **cytosolic multiprotein danger-sensing platform** that sits at the intersection of innate immunity, sterile inflammation, and regulated cell death. It was first described by Jürg Tschopp's group in 2002 [^martinon-2002-inflammasome] and has since emerged as one of the most therapeutically relevant complexes in medicine — implicated in atherosclerosis, gout, type 2 diabetes, Alzheimer's disease, ARDS, and numerous autoinflammatory syndromes.

NLRP3 (NOD-like receptor protein 3; also known as cryopyrin, NALP3, or CIAS1) assembles the inflammasome upon sensing **pathogen-associated molecular patterns (PAMPs)** and **damage-associated molecular patterns (DAMPs)**. Its activation triggers two cardinal events: (1) **caspase-1-mediated proteolytic processing** of pro-IL-1β and pro-IL-18 into their biologically active, secretable forms, and (2) **gasdermin D (GSDMD) cleavage**, which releases an N-terminal pore-forming fragment that inserts into the plasma membrane, causing **pyroptosis** — a lytic, highly inflammatory form of programmed cell death [^swanson-2019-pyroptosis-review].

Unlike many innate immune sensors with narrow, structurally defined ligands, NLRP3 responds to an extraordinarily diverse range of signals — from bacterial toxins and viral RNA to crystalline substances, extracellular ATP, and metabolic byproducts — making it a "universal" cellular alarm system for both infectious and sterile danger.

## Structure

### Component proteins

The assembled NLRP3 inflammasome consists of three core proteins:

| Component | Gene | Domains | Function |
|:---|:---|:---|:---|
| **NLRP3** | *NLRP3* (chr 1q44) | PYD – NACHT – LRR | Sensor and scaffold; directly or indirectly detects activating signals |
| **ASC** | *PYCARD* | PYD – CARD | Adapter; bridges NLRP3 (PYD-PYD) to caspase-1 (CARD-CARD) |
| **Caspase-1** | *CASP1* | CARD – p20 – p10 | Effector protease; activated by proximity-induced dimerization |

**NLRP3 domain architecture:**
- **PYD (Pyrin domain)**: Homotypic interaction with ASC PYD; mediates oligomerization
- **NACHT domain** (NOD-like NTPase): Contains Walker A/B motifs; nucleotide-dependent conformational switch; site of gain-of-function mutations in autoinflammatory syndromes
- **LRR (Leucine-rich repeat) domain**: Regulatory; may auto-inhibit in the resting state; proposed sensor domain (though direct ligand binding is debated)

### Assembled complex architecture

Recent cryo-EM studies reveal the assembled inflammasome as a large (~1–2 MDa) two-layer disk structure:
1. **Outer ring**: ~12–14 NLRP3 subunits forming a ring via NACHT-NACHT and LRR-LRR contacts, organized around a decameric "wheel" scaffold
2. **Central ASC filament**: ASC polymerizes through PYD-PYD interactions into a long helical filament ("speck") visible by fluorescence microscopy as a punctum ~1 μm in diameter
3. **Caspase-1 recruitment**: Multiple caspase-1 monomers dock onto ASC CARD domains; proximity-induced conformational change activates catalytic cysteine (Cys285)

The ASC speck is itself a signaling platform that can be released from pyroptotic cells and activate neighboring cells, propagating inflammation.

## Function

### Two-signal requirement

NLRP3 inflammasome activation requires two distinct signals:

**Signal 1 (Priming — transcriptional)**
- Pattern: TLR agonists, TNF-α, IL-1β, bacterial products
- Receptor: TLRs/NF-κB axis; also TNFR, IL-1R
- Outcome: NF-κB-driven transcription of *NLRP3*, *pro-IL-1β*, and *pro-IL-18*
- This step is required because basal NLRP3 expression is low; priming ~10-fold upregulates NLRP3 protein

**Signal 2 (Activation — post-translational)**
- Pattern: Diverse danger signals (see Mechanism)
- Outcome: NLRP3 oligomerization, ASC speck formation, caspase-1 activation
- This is the actual "trigger" that converts primed cells into active inflammasome state

### Effector outputs

| Output | Mediator | Consequence |
|:---|:---|:---|
| **IL-1β maturation** | Caspase-1 cleaves pro-IL-1β (31 kDa → 17 kDa) | Fever, neutrophil recruitment, acute phase response, Th17 polarization |
| **IL-18 maturation** | Caspase-1 cleaves pro-IL-18 (24 kDa → 18 kDa) | IFN-γ induction from NK/T cells; Th1 immunity |
| **Pyroptosis** | GSDMD-NT pore (8-nm inner diameter) in plasma membrane | Lytic cell death; DAMP release (HMGB1, ATP, IL-1α); amplification of inflammation |
| **GSDMD pore secretion** | GSDMD-NT pores serve as conduit | IL-1β/IL-18 secretion before frank pyroptosis |

## Mechanism

### Molecular activation pathways

Multiple cellular events converge on NLRP3 activation, unified by several proposed "common signals" [^swanson-2019-pyroptosis-review]:

**1. Potassium efflux (primary common signal)**
- Nearly all NLRP3 activators cause cytosolic K⁺ drop (from ~140 mM to <80 mM)
- K⁺ efflux required: high extracellular K⁺ blocks NLRP3 activation
- Mechanism: K⁺ efflux may relieve NLRP3 inhibition by NEK7 (a K⁺-sensitive NLRP3 activator) or directly alter NLRP3 conformation

**2. Mitochondrial dysfunction / mtROS**
- Damaged mitochondria release mtROS and oxidized mitochondrial DNA (ox-mtDNA)
- ox-mtDNA directly binds NLRP3 LRR domain and promotes oligomerization
- mtROS oxidizes NLRP3 Cys residues, facilitating activation

**3. Lysosomal rupture**
- Crystalline activators (MSU/urate crystals, cholesterol crystals, silica, alum) are phagocytosed and destabilize lysosomes [^duewell-2010-crystal-nlrp3]
- Cathepsin B released from ruptured lysosomes activates NLRP3 (mechanism downstream of K⁺ efflux)

**4. ATP/P2X7R signaling**
- Extracellular ATP (released by dying cells) activates the P2X7 ion channel
- P2X7R is a large-pore channel that mediates K⁺ efflux and Ca²⁺ influx → NLRP3 activation
- This mechanism explains how cell death in the local environment propagates inflammasome activation

### Pyroptosis and GSDMD

Activated caspase-1 cleaves **gasdermin D** between its N-terminal pore-forming domain (GSDMD-NT) and C-terminal autoinhibitory domain (GSDMD-CT) at Asp275 [^shi-2017-gasdermin-pore]. GSDMD-NT:
1. Binds specifically to inner leaflet lipids (PIP2, PS, cardiolipin) via a positively charged surface
2. Oligomerizes in the membrane (16–28 subunits) forming ~8 nm pores
3. Pores permit IL-1β/IL-18 secretion and cause osmotic imbalance → cell swelling → membrane rupture = pyroptosis

Caspase-4/5 (human) and caspase-11 (mouse) can also cleave GSDMD in a non-canonical inflammasome pathway, responding to cytoplasmic LPS.

## Connections

- `part-of` → **[Immune System](../../07-system/immune-system/README.md)** — core innate danger-sensing platform
- `expressed-by` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — major NLRP3-expressing sentinel cell
- `modulates` → **[IL-6](../il-6/README.md)** — NLRP3-derived IL-1β drives downstream IL-6 amplification
- `modulated-by` → **[NF-κB](../nf-kb/README.md)** — NF-κB provides transcriptional priming of NLRP3 and pro-IL-1β
- `modulates` → **[Heart](../../06-organ/heart/README.md)** — drives sterile myocardial inflammation and atherogenesis via cholesterol crystal activation

## Pathology

| Disease | NLRP3 Role | Therapeutic implication |
|:---|:---|:---|
| **Gout / pseudogout** | MSU and CPPD crystals → lysosomal rupture → NLRP3 activation → acute arthritis | Colchicine (microtubule disruption), IL-1β blockade (anakinra, canakinumab) |
| **Atherosclerosis** | Cholesterol crystals in plaques → NLRP3 → plaque instability; CANTOS trial showed canakinumab (IL-1β Ab) reduced MACE [^duewell-2010-crystal-nlrp3] | Anti-IL-1β therapy; NLRP3 inhibitors in trials |
| **Type 2 diabetes** | IAPP amyloid deposits → NLRP3 → β-cell death; high glucose primes NLRP3 | NLRP3 inhibitors (MCC950) in preclinical/phase II trials |
| **Alzheimer's disease** | Aβ fibrils → NLRP3 → microglial pyroptosis → ASC speck cross-seeding of Aβ | NLRP3 inhibitors being investigated |
| **ARDS / sepsis** | Cytokine storm involves NLRP3-derived IL-1β/IL-18; pyroptosis of lung epithelium | Caspase-1 inhibitors, anakinra in COVID-19 trials |
| **Cryopyrin-associated periodic syndromes (CAPS)** | Gain-of-function *NLRP3* mutations → constitutive activation → autoinflammatory disease | Canakinumab (IL-1β Ab) — highly effective; rilonacept |
| **CKD / renal fibrosis** | Uremic toxins activate NLRP3 → tubular pyroptosis → TGF-β-driven fibrosis | Experimental NLRP3 inhibitors; clinical trials ongoing |

The **selective NLRP3 inhibitor MCC950** (CMPD-4) has demonstrated potent anti-inflammatory effects across dozens of disease models and is in Phase II trials for several indications, making NLRP3 one of the most actively pursued drug targets in inflammation biology.

[^martinon-2002-inflammasome]: Martinon F, Burns K, Tschopp J. The inflammasome: a molecular platform triggering activation of inflammatory caspases and processing of proIL-beta. *Mol Cell.* 2002;10(2):417-426. [doi:10.1016/s1097-2765(02)00599-3](https://doi.org/10.1016/s1097-2765(02)00599-3) · [PubMed 12191486](https://pubmed.ncbi.nlm.nih.gov/12191486/)
[^swanson-2019-pyroptosis-review]: Swanson KV, Deng M, Ting JP. The NLRP3 inflammasome: molecular activation and regulation to therapeutics. *Nat Rev Immunol.* 2019;19(8):477-489. [doi:10.1038/s41577-019-0165-0](https://doi.org/10.1038/s41577-019-0165-0) · [PubMed 31036962](https://pubmed.ncbi.nlm.nih.gov/31036962/)
[^duewell-2010-crystal-nlrp3]: Duewell P, Kono H, Rayner KJ, et al. NLRP3 inflammasomes are required for atherogenesis and activated by cholesterol crystals. *Nature.* 2010;464(7293):1357-1361. [doi:10.1038/nature08938](https://doi.org/10.1038/nature08938) · [PubMed 20428172](https://pubmed.ncbi.nlm.nih.gov/20428172/)
[^shi-2017-gasdermin-pore]: Shi J, Zhao Y, Wang K, et al. Cleavage of GSDMD by inflammatory caspases determines pyroptotic cell death. *Nature.* 2015;526(7575):660-665. [doi:10.1038/nature15514](https://doi.org/10.1038/nature15514) · [PubMed 26375003](https://pubmed.ncbi.nlm.nih.gov/26375003/)
