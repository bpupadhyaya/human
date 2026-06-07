---
schema: human-scale-entry/v1
id: ntrk
name: NTRK
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "NTRK1/2/3 encode TrkA/B/C neurotrophin receptors; chromosomal fusions (ETV6-NTRK3 in secretory carcinoma; TPM3-NTRK1 pan-tumor) create constitutively active kinases. Larotrectinib and entrectinib are approved TRK inhibitors with ~75% ORR in NTRK fusion-positive tumors."
aliases: ["NTRK", "NTRK1", "NTRK2", "NTRK3", "TrkA", "TrkB", "TrkC", "neurotrophic receptor kinase", "TRK fusion", "ETV6-NTRK3", "TPM3-NTRK1", "larotrectinib", "entrectinib"]
sources:
  - id: larotrectinib-2018-nejm
    type: peer-reviewed
    cite: "Drilon A, Laetsch TW, Kummar S, et al. Efficacy of larotrectinib in TRK fusion-positive cancers in adults and children. N Engl J Med. 2018;378(8):731-739."
    doi: "10.1056/NEJMoa1714448"
    pmid: "29466156"
    url: "https://doi.org/10.1056/NEJMoa1714448"
  - id: entrectinib-2019-basket
    type: peer-reviewed
    cite: "Doebele RC, Drilon A, Paz-Ares L, et al. Entrectinib in patients with advanced or metastatic NTRK fusion-positive solid tumours. Lancet Oncol. 2020;21(2):271-282."
    doi: "10.1016/S1470-2045(19)30691-6"
    pmid: "31838007"
    url: "https://doi.org/10.1016/S1470-2045(19)30691-6"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "TRK fusions activate RAS-MAPK via GRB2-SOS → KRAS → MEK-ERK → proliferation; KRAS co-mutations are rare in NTRK fusion-positive tumors; KRAS/BRAF mutations are acquired resistance to TRK inhibitors; MEK inhibitors studied in TRK-inhibitor-resistant tumors."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "TRK fusions activate PI3K-AKT-mTOR via IRS-1/GAB1 → AKT → mTORC1; mTOR is a major downstream effector of TRK signaling; PI3K-AKT activation is a bypass resistance mechanism to larotrectinib; mTOR inhibitors studied in TRK-inhibitor-resistant tumors."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "TRK → JAK2 → STAT3 → BCL-XL, MYC → survival in neuroblastoma and secretory carcinoma; TrkB (NTRK2) signaling → STAT3 promotes MYCN expression → aggressive neuroblastoma; TrkB high expression correlates with poor prognosis in MYCN-amplified neuroblastoma."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "NTRK fusions occur in tumors lacking EGFR mutations (NTRK fusion-positive NSCLCs are mostly never-smokers with WT EGFR); EGFR bypass via ErbB3 is a larotrectinib resistance mechanism; entrectinib also inhibits ROS1 and ALK; TRK and EGFR pathways converge on RAS-MAPK."
---

# NTRK

## Overview

**NTRK (Neurotrophic Receptor Tyrosine Kinase)** refers to three paralogs — **NTRK1** (TrkA, NGF receptor), **NTRK2** (TrkB, BDNF/NT4 receptor), and **NTRK3** (TrkC, NT3 receptor) — that physiologically mediate neuronal survival, differentiation, and axonal growth downstream of neurotrophin ligands. In cancer, NTRK genes undergo **chromosomal rearrangements** that fuse the 3' kinase domain of NTRK1/2/3 to 5' dimerization domains from partner genes, creating constitutively active oncogenic fusion kinases. NTRK fusions are **pan-tumor drivers** found at low frequency across >20 cancer types, and represent the archetypical tumor-agnostic molecular target — with **larotrectinib (Vitrakvi)** becoming the second FDA tumor-agnostic approval (2018) based on ORR regardless of tumor histology [^larotrectinib-2018-nejm].

**NTRK fusions in cancer:**
- **Frequency by tumor type:** Infantile fibrosarcoma (ETV6-NTRK3, ~100%); congenital/secretory carcinoma of salivary gland (ETV6-NTRK3, ~100%); papillary thyroid cancer (TRK fusions ~12%); colorectal cancer (MSI-H CRC: NTRK fusions ~1-2%); NSCLC (~0.2-1%); GBM (~2%); breast secretory carcinoma (ETV6-NTRK3, ~100%); cholangiocarcinoma (~2%); biliary tract; pancreatic cancer (<1%)
- **Overall pan-tumor frequency:** ~0.1-1% of all solid tumors; enriched in tumors lacking other oncogenic drivers (KRAS WT, EGFR WT, ALK WT)
- **Age distribution:** NTRK fusions more common in pediatric tumors and rare adult tumors than in common adult carcinomas
- **Larotrectinib ORR:** 75% overall (LOXO-TRK-14001, SCOUT, NAVIGATE basket trials); 73% in adults; 90% in pediatric patients; responses across >20 histologies

**Common NTRK fusion partners:**
- **ETV6-NTRK3:** Infantile fibrosarcoma (congenital); secretory carcinoma of breast/salivary gland; t(12;15) translocation; ETV6 (TEL) helix-loop-helix domain drives constitutive dimerization
- **TPM3-NTRK1:** Papillary thyroid cancer, NSCLC; inv(1)(q25q21)
- **LMNA-NTRK1:** Colorectal cancer; nuclear envelope protein → cytoplasmic TrkA fusion
- **SQSTM1-NTRK1:** Lung adenocarcinoma
- **RBPMS-NTRK3, ETV6-NTRK3:** NSCLC, mammary secretory carcinoma

## Structure

### TRK receptor architecture

NTRK1/2/3 encode 800-900 aa single-pass transmembrane RTKs:

**Extracellular domain (ECD):**
- Signal peptide → Leucine-rich motifs (LRM1/LRM2) → Cysteine clusters (CC1/CC2) → Immunoglobulin-like domains (Ig-C1/Ig-C2) → Ligand binding at Ig-C2: NTRK1/NGF, NTRK2/BDNF+NT4, NTRK3/NT3
- Ligand-induced receptor homodimerization → trans-autophosphorylation at activation loop tyrosines

**Transmembrane domain (TM):** Single pass, aa ~430-450

**Intracellular kinase domain (ICD):**
- Juxtamembrane (JM) domain: Tyr496/Tyr501 phosphorylation sites → SHC, FRS2 docking
- Kinase domain: Activation loop Tyr670/671 (NTRK1) — primary autophosphorylation sites
- C-terminal tail: Tyr785 (NTRK1) → PLCγ recruitment

### Oncogenic NTRK fusion structure

**Fusion mechanism:**
5' partner gene (ETV6, TPM3, LMNA) → promoter + dimerization domain
+ 3' NTRK kinase domain → fusion kinase:
- Constitutive dimerization → kinase activity without ligand
- Cytoplasmic localization (no TM domain) → constitutive signaling
- High expression driven by partner gene promoter

**TRK inhibitor binding pocket:**
Larotrectinib and entrectinib bind the ATP-binding cleft of the TRK kinase domain (between N-lobe and C-lobe); highly selective for TrkA/B/C; resistance mutations at gatekeeper (G595R in NTRK1 = equivalent to EGFR T790M) and solvent front (G667C) positions.

### Larotrectinib vs. entrectinib

| Feature | Larotrectinib (LOXO-101) | Entrectinib (RXDX-101) |
|---------|--------------------------|------------------------|
| Targets | NTRK1/2/3 only | NTRK1/2/3 + ROS1 + ALK |
| CNS penetration | Limited | Good (FDA-approved for CNS ROS1) |
| Generation | 1st (highly selective) | 1st (multi-kinase) |
| ORR (NTRK) | ~75% | ~57% (all-comers) |
| CNS ORR | ~75% intracranial (limited data) | 55% intracranial ORR |
| Resistance mutations | G595R, G667C, F589L | G595R, G667C |
| Approval year | FDA 2018 | FDA 2019 |

**Second-generation TRK inhibitors:**
- Selitrectinib (LOXO-195): Active against G595R, G667C resistance mutations; ORR ~45% in larotrectinib-resistant tumors
- Repotrectinib (TPX-0005): Active against solvent-front mutations; also inhibits ROS1 and ALK

## Function

### Normal TRK signaling in neural development

**Neurotrophin-TRK signaling:**
- NGF → TrkA → survival of sympathetic and sensory neurons; pro-NGF → p75NTR → apoptosis (opposing effect)
- BDNF → TrkB → survival of hippocampal neurons, learning and memory, mood regulation; disrupted in depression and neurodegenerative disease
- NT-3 → TrkC → proprioceptive sensory neurons; NT-3 also binds TrkA at lower affinity

**TRK signaling pathways:**
1. SHC → GRB2-SOS → RAS → MEK-ERK1/2 → neuronal differentiation, proliferation
2. GAB1/IRS-1 → PI3K → AKT → mTOR → cell survival, growth
3. PLCγ → IP3/DAG → Ca²⁺ → PKC → synaptic plasticity, gene expression (CREB)
4. JAK → STAT3 → BCL-XL, MYC → survival

**Retrograde signaling:**
TrkA/B signaling in axons must travel retrogradely from the axon terminal to the cell body (meters in some neurons). This is achieved via endocytosed TrkA/B signaling endosomes transported by dynein motors — a unique long-range signaling mechanism unique to neurons.

### NTRK in pediatric tumors

**Infantile fibrosarcoma (IFS):**
- ETV6-NTRK3 in ~95% of congenital IFS; NTRK fusion is the defining genomic event
- Larotrectinib: ORR 90% in pediatric tumors; CR possible; has replaced doxorubicin-based chemotherapy as first-line for metastatic/unresectable IFS
- ETV6-NTRK3 also defines secretory carcinoma of breast (adult rarity) and salivary gland (parotid, ~100% ETV6-NTRK3)

**Congenital mesoblastic nephroma (cellular type):**
- ETV6-NTRK3 in ~50% of cellular CMN; good prognosis with nephrectomy alone for most; larotrectinib for unresectable

## Mechanism

### TRK inhibitor resistance

**On-target resistance (kinase domain mutations):**
- **G595R (NTRK1, solvent front):** Most common (~30% of resistant); equivalent to ALK G1202R; structural change reduces larotrectinib binding; selitrectinib active
- **G667C (NTRK1, DFG+1 position):** Activation loop mutation → resistance; selitrectinib active
- **F589L (NTRK1, xDFG):** Less common; partial resistance
- NTRK2/3 equivalent mutations: G639R (NTRK2), G623R (NTRK3)

**Off-target bypass resistance:**
- KRAS G12D or G12V amplification → ERK activation independent of TRK → MEK inhibitors studied
- MET amplification → AKT/ERK bypass
- BRAF V600E → downstream MAPK activation
- CDK4/6 amplification

### Testing for NTRK fusions

**Detection methods:**
- **FISH:** Detects gene rearrangement; does not identify partner; preferred for ETV6-NTRK3 (IFS, secretory carcinoma)
- **IHC (pan-TRK antibody EPR17341):** Positive IHC (diffuse cytoplasmic) is ~96% sensitive for NTRK fusion; false positives in NTRK-expressing normal tissues; confirms presence, doesn't distinguish fusion from expression
- **RNA sequencing/RT-PCR:** Identifies specific fusion partners; most sensitive; required when IHC is equivocal; recommended for treatment selection
- **CGP (comprehensive genomic profiling, e.g., Foundation One):** Detects NTRK fusions in DNA sequencing; may miss some fusions with large introns (ETV6-NTRK3 in intron 5 is reliably detected)

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — TRK fusions activate RAS-MAPK via GRB2-SOS → KRAS → MEK-ERK → proliferation; KRAS co-mutations are rare in NTRK fusion-positive tumors (like ALK, mutually exclusive with KRAS); KRAS/BRAF mutations are acquired resistance mechanisms to TRK inhibitors; MEK inhibitors studied in TRK-resistant tumors.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — TRK fusions activate PI3K-AKT-mTOR via IRS-1/GAB1 → AKT → mTORC1; mTOR pathway activation is a major downstream effector of TRK signaling in neural tumors and secretory carcinomas; PI3K-AKT activation as bypass resistance to larotrectinib; mTOR inhibitors studied in TRK-inhibitor-resistant tumors.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — TRK → JAK2 → STAT3 → BCL-XL, MYC, cyclin D1 → survival in neuroblastoma and secretory carcinoma; TrkB (NTRK2) signaling in neuroblastoma → STAT3 promotes MYCN expression → aggressive neuroblastoma; TrkB high expression correlates with poor prognosis in MYCN-amplified neuroblastoma.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — NTRK fusions occur in tumors that lack EGFR mutations (most NTRK fusion-positive NSCLCs are never-smokers with WT EGFR); EGFR bypass via ErbB3 overexpression is a larotrectinib resistance mechanism; entrectinib also inhibits ROS1 and ALK (but not EGFR); TRK and EGFR pathways converge on RAS-MAPK.

[^larotrectinib-2018-nejm]: Drilon A, Laetsch TW, Kummar S, et al. Efficacy of larotrectinib in TRK fusion-positive cancers in adults and children. *N Engl J Med.* 2018;378(8):731-739. [doi:10.1056/NEJMoa1714448](https://doi.org/10.1056/NEJMoa1714448) · [PubMed 29466156](https://pubmed.ncbi.nlm.nih.gov/29466156/)
[^entrectinib-2019-basket]: Doebele RC, Drilon A, Paz-Ares L, et al. Entrectinib in patients with advanced or metastatic NTRK fusion-positive solid tumours. *Lancet Oncol.* 2020;21(2):271-282. [doi:10.1016/S1470-2045(19)30691-6](https://doi.org/10.1016/S1470-2045(19)30691-6) · [PubMed 31838007](https://pubmed.ncbi.nlm.nih.gov/31838007/)
