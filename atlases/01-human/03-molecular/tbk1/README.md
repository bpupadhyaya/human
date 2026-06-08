---
schema: human-scale-entry/v1
id: tbk1
name: TBK1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "TBK1 (TANK-binding kinase 1; NAK) is the shared kinase activated by MAVS and STING → Ser172 autophosphorylation → IRF3 Ser396 → IFN-β; TBK1 LOF causes familial ALS/FTD; synthetic lethal with KRAS; amlexanox inhibits TBK1/IKKε for metabolic syndrome."
aliases: ["TBK1", "TANK-binding kinase 1", "NAK", "T2K", "innate kinase TBK1", "TBK1-IRF3 axis", "TBK1 ALS", "IKKε", "IRF3 kinase"]
sources:
  - id: fitzgerald-2003-tbk1-irf3
    type: peer-reviewed
    cite: "Fitzgerald KA, McWhirter SM, Faia KL, et al. IKKε and TBK1 are essential components of the IRF-3 signaling pathway. Nat Immunol. 2003;4(5):491-496."
    doi: "10.1038/ni921"
    pmid: "12692549"
    url: "https://doi.org/10.1038/ni921"
    accessed: "2026-06-08"
  - id: freischmidt-2015-tbk1-als
    type: peer-reviewed
    cite: "Freischmidt A, Wieland T, Richter B, et al. Haploinsufficiency of TBK1 causes familial ALS and fronto-temporal dementia. Nat Neurosci. 2015;18(5):631-636."
    doi: "10.1038/nn.3985"
    pmid: "25848973"
    url: "https://doi.org/10.1038/nn.3985"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "MAVS filament recruits TRAF3 → K63-polyubiquitin scaffolds TBK1 → TBK1 Ser172 trans-autophosphorylation → IRF3 Ser396 → IFN-β; HCV NS3/4A cleaves MAVS → TBK1-IRF3 severed → chronicity; all MAVS-dependent IFN signaling requires TBK1."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAMP-bound STING oligomerizes → recruits TBK1 directly; STING C-terminal tail positions TBK1 for IRF3 Ser396 phosphorylation at Golgi; STING-TBK1 (DNA sensing) and MAVS-TBK1 (RNA sensing) are the two parallel innate axes converging on IRF3-IFN-β."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "TBK1 phosphorylates IRF3 at Ser396 (and Ser398/402/405) → IRF3 homodimerization → nuclear import → IFN-β enhanceosome; TBK1 Ser172 autophosphorylation (trans) is required for catalytic activity; IKKε is the inducible TBK1 paralog."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "MAVS-TBK1 and STING-TBK1 activate NF-κB in parallel with IRF3: TBK1 → TRAF6 → TAK1 → IKKβ → IκBα degradation → p65/p50 nuclear translocation; NF-κB drives IL-6, TNF-α, CXCL10; IRF3 and NF-κB cooperate at the IFN-β enhanceosome."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "RIG-I and MDA5 helicases signal through MAVS → TRAF3 → TBK1 Ser172 autophosphorylation; active TBK1 phosphorylates IRF3 Ser396 → IFN-β; RIG-I/MAVS/TBK1 is the canonical cytosolic RNA sensing axis; all RIG-I responses require TBK1 or IKKε."
---

# TBK1

## Overview

**TBK1** (TANK-binding kinase 1; also known as NAK or T2K) is the central **serine/threonine kinase** of innate antiviral immunity — the shared catalytic hub activated by both RNA sensing (via **MAVS**) and DNA sensing (via **cGAS-STING**) pathways to phosphorylate **IRF3** and drive IFN-β production. Identified as an IRF3 kinase by Fitzgerald et al. in 2003 [^fitzgerald-2003-tbk1-irf3], TBK1 is remarkable for its position as the **convergence point** of the two major innate sensing axes: virtually all virus-triggered IFN-β production requires TBK1 (or its inducible paralog IKKε).

Beyond innate immunity, TBK1 emerged as a critical disease gene when Freischmidt et al. discovered that haploinsufficiency of TBK1 causes familial **amyotrophic lateral sclerosis (ALS)** and frontotemporal dementia (FTD) [^freischmidt-2015-tbk1-als]. This finding linked TBK1's role in selective autophagy — via phosphorylation of the autophagy receptor **p62/SQSTM1** and **ULK1** — to motor neuron survival, positioning TBK1 at the intersection of innate immunity, autophagy, and neurodegeneration.

**Clinical significance:** TBK1 LOF mutations (~1% of familial ALS) cause progressive motor neuron degeneration. TBK1 hyperactivation (in STING-associated vasculopathy, SAVI) causes systemic inflammation. TBK1 is **synthetic lethal with KRAS mutations** in lung and pancreatic cancer — KRAS-mutant cells depend on TBK1-driven autophagy for survival. TBK1/IKKε inhibitor **amlexanox** improves insulin resistance in metabolic syndrome.

## Structure

### TBK1 protein (~712 aa, ~80 kDa)

TBK1 shares the IKK-family kinase architecture with three ordered domains:

- **Kinase domain (KD, aa ~1–307)**: N-terminal serine/threonine kinase; DFG motif defines the active site; **Ser172** in the activation loop is the primary autophosphorylation site required for catalytic activity; substrate recognition via activation loop conformation
- **Ubiquitin-like domain (ULD, aa ~308–385)**: Central β-grasp fold; mediates protein-protein interactions and substrate specificity; required for IRF3 (but not NF-κB) activation; regulates kinase domain activity allosterically
- **Scaffold/dimerization domain (SDD, aa ~386–712)**: C-terminal coiled-coil; mediates TBK1 homodimerization and interaction with TRAF3/TRAF6 K63-ubiquitin chains; also binds STING C-terminal tail; positions TBK1 for trans-autophosphorylation

**IKKε (IKK-related kinase):** The inducible paralog of TBK1 (58% overall identity; kinase domain >75% identical); expressed at low level basally and strongly induced by IFN-β (ISG); can substitute for TBK1 in secondary IFN responses; dual TBK1/IKKε inhibitors (amlexanox, BX795, MRT67307) inhibit both.

**Trans-autophosphorylation model:** TBK1 forms dimers via SDD → within a dimer, one TBK1 molecule phosphorylates Ser172 of the partner → catalytic activation; K63-polyubiquitin chains (from TRAF3) act as scaffolds clustering multiple TBK1 dimers → cooperative activation

### Upstream signaling complexes

**MAVS pathway (RNA sensing):**
- MAVS prion-like filament on OMM recruits **TRAF3** via PVQE/PVQT TRAF-binding motifs
- TRAF3 assembles K63-linked polyubiquitin chains → scaffold for TBK1 SDD binding
- NAP1/SINTBAD/AZI2 adaptor proteins bridge TRAF3-TBK1 complex

**STING pathway (DNA sensing):**
- cGAMP-bound STING oligomerizes and traffics ER → ERGIC → Golgi
- STING C-terminal tail (CTT, Ser366) directly recruits TBK1 → TBK1 trans-autophosphorylates on STING scaffold
- TBK1 phosphorylates STING CTT pSer366 → recruits IRF3 → TBK1 phosphorylates IRF3

## Function

1. **IFN-β induction** (primary): TBK1 Ser172 phosphorylation → IRF3 Ser396 phosphorylation → IRF3 homodimerization → nuclear translocation → IFN-β enhanceosome (IRF3 + NF-κB + AP-1) → IFN-β transcription within 1–2 h of infection
2. **IFN-α amplification**: TBK1 phosphorylates **IRF7** (expressed in pDCs and as ISG) → IRF3/IRF7 heterodimers → IFN-α/β amplification; pDC TBK1 drives the systemic IFN-α response
3. **NF-κB activation**: TBK1 → TRAF6 → TAK1 → IKKβ → IκBα degradation → p65/p50 → TNF-α, IL-6, CXCL10 (parallel to IRF3 arm; shared requirement for inflammatory innate immunity)
4. **Selective autophagy**: TBK1 phosphorylates **p62/SQSTM1** (Ser403) → enhanced ubiquitin-binding → selective autophagy of ubiquitinated cargo (mitochondria, lipid droplets, bacteria); TBK1 → **ULK1** (Ser757 phosphorylation) initiates autophagy; this function is disrupted by ALS mutations
5. **AKT/mTOR pathway**: TBK1 directly phosphorylates AKT at Thr308 → pro-survival/proliferative signaling; relevant to KRAS-mutant cancer survival
6. **STAT6 cross-talk**: TBK1 phosphorylates STAT6 at Ser407 → modulates IL-4/IL-13 Th2 signaling amplitude

## Mechanism

### MAVS → TBK1 → IRF3 (canonical RNA sensing)

1. Viral RNA → RIG-I/MDA5 → MAVS filament polymerization on OMM
2. MAVS recruits **TRAF3** via TRAF-binding motifs → TRAF3 assembles K63-polyubiquitin chains
3. K63-Ub chains scaffold multiple TBK1 dimers via SDD → **Ser172 trans-autophosphorylation** → active TBK1
4. Active TBK1 phosphorylates **IRF3 Ser396** (primary) and Ser398/402/404/405
5. Phospho-IRF3 homodimerizes → nuclear import via importin-α → PRDI/III IFN-β enhanceosome binding
6. **IFN-β** transcription + NF-κB (PRDII) + AP-1 (PRDIV) cooperative enhanceosome assembly

### STING → TBK1 → IRF3 (DNA sensing)

1. cGAS → 2'3'-cGAMP → STING at ER → STING undergoes conformational change + oligomerization
2. STING traffics ER → ERGIC → Golgi, recruiting TBK1 via CTT direct interaction
3. STING-scaffold TBK1 trans-autophosphorylates (Ser172) → STING pSer366 created → IRF3 docking
4. IRF3 recruited to STING-TBK1 complex → phosphorylated Ser396 → same IRF3 pathway as above

### Viral TBK1 evasion

| Virus | Strategy |
|-------|---------|
| SARS-CoV-2 NSP13 | Helicase inhibits TBK1 Ser172 autophosphorylation |
| Influenza NS1 | Upstream: blocks TRIM25/RIG-I before TBK1 |
| HCV NS3/4A + NS5A | Cleaves MAVS (upstream); NS5A directly inhibits TBK1 |
| Picornavirus 3Cpro | Directly cleaves TBK1 and IRF3 |
| KSHV vIRF-1 | Viral IRF blocks TBK1-IRF3 interaction |

### Regulation and termination

- **PPM1B phosphatase**: Dephosphorylates TBK1 Ser172 → signal termination
- **NLRP4-DTX4**: K48-ubiquitination of TBK1 → proteasomal degradation
- **SIKE1**: Competes with TRAF3 for TBK1 binding → attenuates signaling amplitude
- **A20**: Deubiquitinase removes TRAF3 K63-chains → reduces TBK1 scaffolding

### TBK1 in ALS/FTD

TBK1 LOF mutations (frameshift, nonsense, missense including p.S172G kinase-dead) → impaired selective autophagy → p62-ubiquitinated inclusions accumulate in motor neurons → TDP-43/FUS aggregates not cleared → ER stress, mitochondrial dysfunction, motor neuron death. Mechanism parallels: mutations in *OPTN* (optineurin, TBK1 substrate), *p62/SQSTM1*, and *ULK1* also cause ALS, confirming the selective autophagy pathway.

## Connections

**→ [MAVS](../mavs/)**: MAVS filament recruits TRAF3 → K63-polyubiquitin scaffolds TBK1 → TBK1 Ser172 trans-autophosphorylation → IRF3 Ser396 → IFN-β; HCV NS3/4A cleaves MAVS → TBK1-IRF3 severed → chronicity; all MAVS-dependent IFN signaling requires TBK1.

**→ [cGAS-STING](../cgas-sting/)**: cGAMP-bound STING oligomerizes → recruits TBK1 directly; STING C-terminal tail positions TBK1 for IRF3 Ser396 phosphorylation at Golgi; STING-TBK1 (DNA sensing) and MAVS-TBK1 (RNA sensing) are the two parallel innate axes converging on IRF3-IFN-β.

**→ [IRF3](../irf3/)**: TBK1 phosphorylates IRF3 at Ser396 (and Ser398/402/405) → IRF3 homodimerization → nuclear import → IFN-β enhanceosome; TBK1 Ser172 autophosphorylation (trans) is required for catalytic activity; IKKε is the inducible TBK1 paralog.

**→ [NF-κB](../nf-kb/)**: MAVS-TBK1 and STING-TBK1 activate NF-κB in parallel with IRF3: TBK1 → TRAF6 → TAK1 → IKKβ → IκBα degradation → p65/p50 nuclear translocation; NF-κB drives IL-6, TNF-α, CXCL10; IRF3 and NF-κB cooperate at the IFN-β enhanceosome.

**→ [RIG-I](../rig-i/)**: RIG-I and MDA5 helicases signal through MAVS → TRAF3 → TBK1 Ser172 autophosphorylation; active TBK1 phosphorylates IRF3 Ser396 → IFN-β; RIG-I/MAVS/TBK1 is the canonical cytosolic RNA sensing axis; all RIG-I responses require TBK1 or IKKε.
