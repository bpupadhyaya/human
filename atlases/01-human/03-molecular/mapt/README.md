---
schema: human-scale-entry/v1
id: mapt
name: MAPT
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "MAPT encodes tau, a microtubule-stabilizing protein; CDK5 and GSK-3β hyperphosphorylate tau → detachment from microtubules → neurofibrillary tangles; tau Braak staging (I–VI) correlates with cognitive decline in Alzheimer disease and other tauopathies."
aliases: ["MAPT", "tau", "microtubule-associated protein tau", "tau protein", "NFT", "neurofibrillary tangle", "tauopathy", "PHF", "paired helical filament", "tau PET"]
cross_links:
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Tau hyperphosphorylation at Thr181, Ser202/Thr205, Ser396 → PHF → NFT formation; Braak staging I–VI tracks NFT spread from entorhinal cortex to isocortex and correlates with cognitive decline; tau-PET (flortaucipir) predicts cognitive trajectory and guides clinical staging in AD."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "MAPT H1 haplotype (common in Europeans) is a risk factor for PD and PSP; tau co-aggregates with alpha-synuclein in Lewy body dementia and some PD brains; MAPT LOF mutations cause FTLD-MAPT; tau and SNCA pathology converge on mitochondrial dysfunction and autophagy impairment."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Aggregated tau impairs autophagosome formation and lysosomal function via sequestration of autophagy adaptors; p62/SQSTM1 and NDP52 recognize tau for autophagic clearance; declining autophagy in aging and tau mutations accelerates NFT accumulation and tauopathy progression."
  - target: 01-human/03-molecular/app
    relation: connects-to
    note: "Aβ42 oligomers activate CDK5/p25 and GSK-3β → tau hyperphosphorylation at AD-relevant sites (Thr181, Ser202, Ser396) → tau aggregation and NFT formation; APP processing and tau pathology form a feedforward loop — Aβ upstream, tau downstream, driving neurodegeneration."
sources:
  - id: grundke-iqbal-1986-tau-phosphorylation
    type: peer-reviewed
    cite: "Grundke-Iqbal I, Iqbal K, Tung YC, Quinlan M, Wisniewski HM, Binder LI. Abnormal phosphorylation of the microtubule-associated protein tau (tau) in Alzheimer cytoskeletal pathology. Proc Natl Acad Sci USA. 1986;83(13):4913-4917."
    doi: "10.1073/pnas.83.13.4913"
    pmid: "3088567"
    url: "https://doi.org/10.1073/pnas.83.13.4913"
  - id: iqbal-2016-tau-review
    type: peer-reviewed
    cite: "Iqbal K, Liu F, Gong CX. Tau and neurodegenerative disease: the story so far. Nat Rev Neurol. 2016;12(1):15-27."
    doi: "10.1038/nrneurol.2015.225"
    pmid: "26635213"
    url: "https://doi.org/10.1038/nrneurol.2015.225"
---

# MAPT

## Overview

**MAPT** (microtubule-associated protein tau; gene *MAPT*, chromosome 17q21.31) encodes **tau**, a highly soluble phosphoprotein expressed predominantly in neurons — particularly in axons — where it stabilizes microtubules and facilitates axonal transport. Tau's pathological aggregation into **neurofibrillary tangles (NFTs)** is the defining feature of the **tauopathies**, a spectrum of neurodegenerative diseases that includes Alzheimer's disease (the most common), frontotemporal lobar degeneration due to *MAPT* mutations (FTLD-MAPT), progressive supranuclear palsy (PSP), corticobasal degeneration (CBD), Pick's disease, and chronic traumatic encephalopathy (CTE).

In Alzheimer's disease, tau pathology follows the stereotyped anatomical spread of **Braak staging** — from the entorhinal cortex and hippocampus (Braak I–IV) to neocortex (Braak V–VI) — and this staging correlates far more tightly with cognitive decline than amyloid plaque burden. Grundke-Iqbal et al. (1986) first identified that tau in AD brain is **abnormally phosphorylated** at sites not present in normal adult brain, and that this hyperphosphorylation causes tau to detach from microtubules and self-aggregate [^grundke-iqbal-1986-tau-phosphorylation]. Iqbal et al. (2016) provided a comprehensive review of tau biology and its therapeutic implications [^iqbal-2016-tau-review].

**Tau isoform biology:**

| Isoform | N inserts | Repeat domain | Disease |
|---|---|---|---|
| 0N3R | 0 | 3 repeats | Pick's disease (3R predominant) |
| 1N3R | 1 | 3 repeats | Mixed tauopathies |
| 2N3R | 2 | 3 repeats | Normal adult (3R) |
| 0N4R | 0 | 4 repeats | PSP, CBD (4R predominant) |
| 1N4R | 1 | 4 repeats | Normal adult (4R) |
| 2N4R | 2 | 4 repeats | Longest, highest MT affinity |

*Adult human brain contains equal proportions of 3R and 4R tau (~50:50). Imbalance of this ratio is disease-specific and contributes to distinct tauopathy phenotypes.*

## Structure

Tau is an **intrinsically disordered protein** — predominantly random coil in solution — with four major functional regions:

**N-terminal projection domain (aa 1–150):**
- Projects from the microtubule surface; involved in microtubule spacing and interactions with neuronal plasma membrane and kinases
- Contains the 0, 1, or 2 N-terminal inserts (29 aa each) from exons 2 and 3 — the basis of isoform nomenclature
- Contains the phosphatase-activating domain (PAD); PAD exposure in disease state signals defects in axonal transport

**Proline-rich region (aa 151–243):**
- Phosphorylated by proline-directed kinases (CDK5, GSK-3β, DYRK1A, ERK2) at Ser/Thr-Pro motifs
- Key AD phosphoepitopes: AT8 (Ser202/Thr205), AT100 (Thr212/Ser214), PHF-1 (Ser396/Ser404)
- Interacts with SH3 domains of Fyn kinase, Src kinases — connecting tau to synaptic NMDA receptor signaling

**Microtubule-binding repeat domain (aa 244–368; MTBD):**
- Contains 3 or 4 tandem repeats (R1–R4; 31 aa each) depending on alternative splicing of exon 10
- R2 (exon 10) is the additional repeat in 4R tau — confers stronger MT binding and is excluded in 3R tau
- **PHF core:** R3-R4 hexapeptide motifs (VQIINK and VQIVYK) form the amyloid-like β-sheet core of paired helical filaments; mutations here (P301L, P301S, R406W) cause FTLD-MAPT
- **Aggregation inhibition:** Full-length soluble tau has complementary pseudorepeat sequences that prevent self-assembly; post-translational modifications disrupting these intramolecular interactions promote aggregation

**C-terminal domain (aa 369–441):**
- Regulatory; contains more AT8 and PHF-1 sites; Arg406 is a key AD hyperphosphorylation site; C-terminal domain modulates MT binding affinity

## Function

**Normal physiological roles of tau:**
- **Microtubule stabilization:** Tau binds tubulin dimers along the outer surface of microtubule walls → reduces catastrophe frequency and promotes elongation; the MTBD and linker regions are the key contact sites
- **Axonal transport:** Tau regulates kinesin-1 motor attachment and processivity on microtubule tracks; hyperphosphorylated tau detaches from MT → impairs kinesin-1 → stalled cargo vesicles → axonal dystrophy
- **Synaptic function:** Low levels of tau in dendritic spines participate in NMDA receptor-dependent signaling via Fyn kinase; tau-Fyn interaction is also relevant to Aβ-mediated excitotoxicity
- **DNA damage response:** Nuclear tau associates with chromatin during heat stress and DNA damage to protect genomic integrity

**Tau propagation — the prion-like spread hypothesis:**
Tau pathology propagates through the brain in a pattern consistent with transneuronal spread along anatomically connected circuits (Braak staging). Fibrillar tau released by degenerating neurons is internalized by connected neurons via macropinocytosis → seeds endogenous tau to aggregate → neuron-to-neuron spread along synaptic pathways. The spreading is template-directed: distinct tau fibril folds (strains) characterize different tauopathies (AD, CBD, PSP have distinct fibril structures by cryo-EM; Fitzpatrick et al., 2017).

**Tau in CTE (chronic traumatic encephalopathy):**
- Repetitive traumatic brain injury (contact sports, blast exposure) → tau aggregation in astrocytes and neurons around small blood vessels at sulcal depths (pathognomonic CTE pattern)
- CTE tau is hyperphosphorylated 4R and 3R, similar to AD — but the anatomical distribution and glial involvement are distinct

## Mechanism

**Tau hyperphosphorylation cascade in AD:**

1. **Trigger:** Aβ42 oligomers → activate CDK5/p25 (via calpain-mediated p35→p25 cleavage) and GSK-3β (via impaired PI3K/Akt) → tau hyperphosphorylation exceeds normal phosphatase (PP2A, PP2B) activity
2. **Detachment:** Hyperphosphorylated tau loses affinity for microtubules → dissociates → accumulates in cytoplasm
3. **Oligomerization:** Soluble monomers → dimers → oligomers (most toxic form for synaptic function) → protofilaments
4. **PHF formation:** VQIINK and VQIVYK hexapeptide repeats form cross-β sheets → paired helical filaments (PHFs, 10–22 nm width, ~160 Å periodicity) → straight filaments (SFs) → NFTs (mature, ghost, flame-shaped)

**Key phosphorylation sites in AD pathology:**
- **pThr181:** CSF biomarker (p-tau181); elevated in early prodromal AD; plasma p-tau181 is sensitive and specific (AUC ~0.93 vs controls)
- **pThr217:** Even more specific for AD vs other tauopathies; plasma p-tau217 is the current clinical standard for amyloid status prediction without PET
- **pSer202/Thr205 (AT8 epitope):** Earliest neuropathological marker; AT8 immunostaining defines Braak stages
- **pSer396/Ser404 (PHF-1 epitope):** Late AD; NFT cores

**MAPT mutations in FTLD-MAPT:**
- >60 known pathogenic mutations in exons 9–13 (MTBD) and intron 10 (splicing)
- **P301L, P301S, R406W:** Promote tau aggregation directly; autosomal dominant; mean onset ~50s
- **Intronic (IVS10+16):** Shift 3R:4R ratio to excess 4R → PSP/CBD-like pathology
- Clinical: behavioral FTD, PSP-like syndrome, or CBD-like asymmetric rigidity/apraxia

**Tau-directed therapeutics (clinical trials):**

| Approach | Agent | Target | Status |
|---|---|---|---|
| Anti-tau antibody | Gosuranemab | N-terminal tau | Phase 2 negative in FTLD |
| Anti-tau antibody | Semorinemab | N3pG tau (pyroglutamate) | Phase 2 (AD) — slowed progression in mild AD |
| Anti-tau antibody | Zagotenemab | Tau aggregates | Phase 2 negative |
| ASO | BIIB080 | MAPT mRNA | Phase 1/2 (AD): 50-80% CSF tau reduction |
| Small molecule | Salsalate (salicylate) | SIRT1 → tau deacetylation | Exploratory AD/PSP |
| Kinase inhibitor | TDI-6160 (DYRK1A) | Tau phosphorylation | Preclinical |

*BIIB080 (ION285, anti-MAPT ASO) represents the most promising strategy — CSF tau reduction of 50–80% in Phase 1, with Phase 2 biomarker outcomes pending (HTT-lowering ASO analogy applied to tau).*

## Connections

Tau hyperphosphorylation at Thr181, Ser202/Thr205, Ser396 → PHF → NFT formation; Braak staging I–VI tracks NFT spread from entorhinal cortex to isocortex and correlates with cognitive decline; tau-PET (flortaucipir) predicts cognitive trajectory and guides clinical staging in AD.

MAPT H1 haplotype (common in Europeans) is a risk factor for PD and PSP; tau co-aggregates with alpha-synuclein in Lewy body dementia and some PD brains; MAPT LOF mutations cause FTLD-MAPT; tau and SNCA pathology converge on mitochondrial dysfunction and autophagy impairment.

Aggregated tau impairs autophagosome formation and lysosomal function via sequestration of autophagy adaptors; p62/SQSTM1 and NDP52 recognize tau for autophagic clearance; declining autophagy in aging and tau mutations accelerates NFT accumulation and tauopathy progression.

Aβ42 oligomers activate CDK5/p25 and GSK-3β → tau hyperphosphorylation at AD-relevant sites (Thr181, Ser202, Ser396) → tau aggregation and NFT formation; APP processing and tau pathology form a feedforward loop — Aβ upstream, tau downstream, driving neurodegeneration.

[^grundke-iqbal-1986-tau-phosphorylation]: Grundke-Iqbal I, Iqbal K, Tung YC, Quinlan M, Wisniewski HM, Binder LI. Abnormal phosphorylation of the microtubule-associated protein tau (tau) in Alzheimer cytoskeletal pathology. *Proc Natl Acad Sci USA.* 1986;83(13):4913-4917. [doi:10.1073/pnas.83.13.4913](https://doi.org/10.1073/pnas.83.13.4913) · [PubMed 3088567](https://pubmed.ncbi.nlm.nih.gov/3088567/)
[^iqbal-2016-tau-review]: Iqbal K, Liu F, Gong CX. Tau and neurodegenerative disease: the story so far. *Nat Rev Neurol.* 2016;12(1):15-27. [doi:10.1038/nrneurol.2015.225](https://doi.org/10.1038/nrneurol.2015.225) · [PubMed 26635213](https://pubmed.ncbi.nlm.nih.gov/26635213/)
