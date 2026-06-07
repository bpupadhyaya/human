---
schema: human-scale-entry/v1
id: flt3
name: FLT3
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Receptor tyrosine kinase mutated in ~25-30% of AML (ITD tandem duplications in JM domain and TKD point mutations); constitutive kinase → STAT5, ERK, PI3K → blast proliferation and survival. Midostaurin (frontline) and gilteritinib (relapsed) are approved FLT3 inhibitors in AML."
aliases: ["FLT3", "FMS-like tyrosine kinase 3", "CD135", "STK1", "FLK2", "FLT3-ITD", "FLT3-TKD", "FLT3 internal tandem duplication"]
sources:
  - id: stone-2017-midostaurin
    type: peer-reviewed
    cite: "Stone RM, Mandrekar SJ, Sanford BL, et al. Midostaurin plus chemotherapy for acute myeloid leukemia with a FLT3 mutation. N Engl J Med. 2017;377(5):454-464."
    doi: "10.1056/NEJMoa1614359"
    pmid: "28644114"
    url: "https://doi.org/10.1056/NEJMoa1614359"
  - id: perl-2019-gilteritinib
    type: peer-reviewed
    cite: "Perl AE, Martinelli G, Cortes JE, et al. Gilteritinib or chemotherapy for relapsed or refractory FLT3-mutated AML. N Engl J Med. 2019;381(18):1728-1740."
    doi: "10.1056/NEJMoa1902688"
    pmid: "31665578"
    url: "https://doi.org/10.1056/NEJMoa1902688"
cross_links:
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "FLT3-ITD constitutively activates STAT5 → MCL-1, BCL-XL, cyclin D1, and MYC induction → leukemic blast survival and proliferation; FLT3 inhibition (midostaurin, gilteritinib) rapidly reduces pSTAT5 and triggers apoptosis; STAT5 is the dominant downstream survival effector."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "FLT3-ITD activates MYC via STAT5 → MYC target gene induction (CDK4, cyclin D2, RNR) → cell cycle acceleration; FLT3 inhibition reduces MYC protein; MYC is a co-driver of FLT3-ITD AML self-renewal; combined FLT3 + BET bromodomain inhibition downregulates MYC more potently."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "FLT3-ITD → PI3K → AKT → mTORC1 → protein synthesis and leukemic stem cell (LSC) maintenance; mTOR pathway activation is a resistance mechanism to FLT3 inhibitors; combined FLT3 + mTOR dual inhibition synergizes in FLT3-ITD AML models and may target LSC quiescence."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "FLT3-ITD and KRAS/NRAS mutations activate RAS-MAPK from different points; RAS mutations in ~12% of AML; co-occurrence of FLT3-ITD + RAS mutations drives high ERK activation; acquired RAS mutations are a mechanism of gilteritinib resistance in relapsed FLT3-mutant AML."
---

# FLT3

## Overview

**FLT3 (FMS-like tyrosine kinase 3, CD135)** is a class III receptor tyrosine kinase expressed on early hematopoietic progenitors, dendritic cell precursors, and B cell precursors. FLT3 signaling via its ligand FL (FLT3L) is required for normal hematopoietic stem and progenitor cell (HSPC) development, dendritic cell homeostasis, and B lymphopoiesis. In **acute myeloid leukemia (AML)**, activating mutations of FLT3 are the most common somatic alterations: **FLT3-ITD** (internal tandem duplication) in ~25-30% of AML and **FLT3-TKD** (tyrosine kinase domain point mutations) in ~5-10% — collectively making FLT3 the dominant therapeutic target in AML [^stone-2017-midostaurin] [^perl-2019-gilteritinib].

**FLT3 in normal hematopoiesis:**
- FLT3 is expressed by HSCs, multipotent progenitors (MPPs), and common lymphoid progenitors (CLPs); FLT3 expression is downregulated as myeloid commitment proceeds
- FLT3L (FLT3 ligand, expressed by stromal cells) → FLT3 dimerization → PI3K, MAPK, STAT5 → progenitor expansion and survival; FLT3-null mice have profoundly reduced NK cells, DCs, and early B cells
- **FLT3 expression on leukemic blasts:** FLT3 surface expression (CD135) is nearly universal in AML regardless of mutation status → FLT3 is both a disease biomarker and a therapeutic target (CD33/CD123 ADCs often co-target FLT3-expressing blasts)

**FLT3 mutation types in AML:**
| Mutation type | Location | Frequency | Signaling | Prognosis |
|-------------|---------|---------|----------|---------|
| **ITD (internal tandem duplication)** | Juxtamembrane domain (exons 14-15) | ~25-30% | Constitutive kinase, STAT5 dominant | Poor (FLT3-ITD high AR → very poor) |
| **D835Y/H/V (TKD)** | Kinase domain activation loop | ~5-10% | Constitutive kinase, slightly different downstream bias | Intermediate |
| **I836M/S (TKD)** | Kinase domain A-loop | ~2% | Constitutive | Intermediate |
| **K663/M664 (JM)** | Juxtamembrane | Rare | Ligand-independent but weaker | Unknown |

**FLT3-ITD characteristics:**
- ITD = in-frame tandem duplication of 3-400+ bp within exons 14-15 (juxtamembrane domain); insertion length and site vary between patients; variable insert sites within the JM domain → different structural disruption effects
- **Allelic ratio (AR):** Ratio of FLT3-ITD mutant allele signal to wild-type FLT3 signal (by PCR or NGS); high AR (≥0.5 or ≥0.51 by ELN) = both alleles mutated OR mutant amplified → associated with significantly worse prognosis; ELN 2022 classifies FLT3-ITD (any AR) + NPM1-wild-type as high risk
- **Co-mutations:** FLT3-ITD co-occurs with NPM1 mutation (~40% of NPM1-mutant AML also have FLT3-ITD), DNMT3A, TET2; these co-mutation patterns define distinct disease biology

## Structure

### FLT3 receptor architecture

FLT3 is a 993-amino-acid type III RTK with the classic class III architecture (shared with PDGFR, KIT, FMS):

**Extracellular domain (ECD):**
- 5 immunoglobulin-like (Ig-like) domains (D1-D5); D2/D3 bind FLT3L; D4/D5 mediate receptor dimerization upon ligand binding; the Ig-like domains adopt the same general fold as PDGFR and KIT extracellular domains
- FLT3L (a type I transmembrane protein expressed as a soluble form by proteolytic shedding) binds FLT3 → receptor dimerization → juxtamembrane release → kinase activation

**Transmembrane domain:** Single alpha-helix; transmembrane mutations not seen in AML (unlike ECD mutations in GIST)

**Juxtamembrane domain (JM, residues 571-620):**
- The autoinhibitory "switch" of FLT3; in inactive receptor, JM forms a "molecular brake" that inserts into the kinase domain active site → blocks ATP binding → keeps kinase inactive
- **FLT3-ITD mechanism:** Tandem duplication inserts additional amino acids within the JM → disrupts the JM autoinhibitory conformation → constitutive, ligand-independent kinase activation; the longer the ITD and the more distal its location within JM, the more potent the activation

**Kinase domain (split by KI: residues 621-813):**
- N-lobe (ATP-binding), KI insert (kinase insert between N-lobe and C-lobe — class III RTK characteristic; absent in EGFR), C-lobe (substrate binding and phosphotransfer)
- **D835 (activation loop):** The most common TKD mutation site; D835Y/H/V → substitution of the Asp836 "DFG" motif Asp → stabilizes DFG-in (active) conformation without ATP → constitutive activation; structurally similar to D816V in KIT (resistance to imatinib mechanism)
- FLT3-TKD (D835) has different inhibitor sensitivity than FLT3-ITD: most type I inhibitors (midostaurin) retain activity vs. TKD; some type II inhibitors (quizartinib) are TKD-resistant

**C-terminal tail:** Contains regulatory phosphorylation sites; Y969 (adapter binding)

## Function

### FLT3 signaling pathways

**STAT5 activation (dominant survival pathway in FLT3-ITD AML):**
- FLT3-ITD → JAK2-independent, direct STAT5 tyrosine phosphorylation (Y694/Y699) → STAT5 homodimerization → nuclear → transcription of: BCL-XL, MCL-1, cyclin D1, PIM kinases, and MYC
- Constitutive STAT5 phosphorylation distinguishes FLT3-ITD (strong STAT5) from FLT3-TKD (weaker STAT5); this explains worse prognosis and stronger transformation by FLT3-ITD
- **PIM kinases:** STAT5 → PIM1/2/3 → phosphorylation of BAD (anti-apoptosis) + 4EBP1 (mTOR bypass) + CDC25C (cell cycle); PIM kinases confer a unique STAT5-driven survival mechanism; PIM inhibitors synergize with FLT3 inhibitors in models

**RAS-MEK-ERK pathway:**
- FLT3 → GRB2-SOS → RAS-GTP → RAF-MEK-ERK → cyclin D1, Bcl-2, AP-1; ERK activation is a secondary pathway (less dominant than STAT5 in FLT3-ITD AML); RAS mutations in AML (~12% NRAS + ~5% KRAS) activate this axis in FLT3-WT disease and serve as resistance mechanism in FLT3-inhibitor-treated disease

**PI3K-AKT-mTOR pathway:**
- FLT3-ITD → PI3K (via direct p85 binding or via Grb2-GAB1) → PIP3 → PDK1 → AKT → mTORC1; AKT phosphorylates BAD, GSK3β, and FoxO factors → leukemic cell survival
- mTORC1 → 4EBP1 and S6K1 → protein synthesis and ribosome biogenesis → leukemic blast growth; mTOR is also required for LSC self-renewal (quiescent LSCs are mTOR-high, not low as previously thought)

**Epigenetic dysregulation by FLT3-ITD:**
- FLT3-ITD → nuclear ERK → direct phosphorylation of nuclear DNMT3A → DNMT3A mislocalization → hypermethylation of tumor suppressor loci (e.g., *SPI1/PU.1* promoter); FLT3-ITD-driven epigenetic silencing of myeloid differentiation genes contributes to blast immortalization
- FLT3-ITD → FLT3-ITD-STAT5 → HOX gene dysregulation → blocked differentiation; HOXA9 upregulation by FLT3-ITD cooperates with NPM1 cytoplasmic mislocalization

## Mechanism

### FLT3 inhibitors and resistance

**Midostaurin (PKC412, Rydapt) — RATIFY trial [^stone-2017-midostaurin]:**
- Multi-kinase inhibitor targeting FLT3-ITD/TKD, KIT, PDGFR, PKC; first-generation broad kinase inhibitor
- FDA-approved (2017) for FLT3-mutant AML in combination with standard induction (7+3) and consolidation chemotherapy; RATIFY trial: OS benefit (74.7 vs. 25.6 months at 5-year landmark in responders); midostaurin is added to standard 7+3 induction and HiDAC consolidation → alloSCT recommended for FLT3-ITD high-risk
- Limitations: Moderate FLT3 selectivity; many off-target kinases → toxicity profile (nausea, vomiting, cytopenias); does not achieve complete FLT3 inhibition; sub-optimal for single-agent use in relapsed/refractory disease

**Quizartinib (AC220, Vanflyta):**
- Type II (DFG-out binding), highly selective FLT3 inhibitor; superior pharmacological FLT3 inhibition (IC50 ~0.5 nM)
- FDA-approved (2023) for newly diagnosed FLT3-ITD AML (frontline + chemotherapy, QuANTUM-First trial: OS benefit)
- **Limitation: D835 TKD mutation resistance** — quizartinib only binds DFG-out conformation; D835 mutations stabilize DFG-in → quizartinib cannot bind → D835 mutations arise under quizartinib pressure (acquired resistance in ~25%)

**Gilteritinib (ASP2215, Xospata) — ADMIRAL trial [^perl-2019-gilteritinib]:**
- Type I FLT3/AXL inhibitor; active against both FLT3-ITD and FLT3-TKD (D835); significant AXL inhibition (AXL promotes resistance to earlier FLT3 inhibitors)
- FDA-approved (2018) for relapsed/refractory FLT3-mutant AML; ADMIRAL trial: OS 9.3 vs. 5.6 months vs. salvage chemotherapy; CR rate 21.1% vs. 10.5%
- **Gilteritinib + venetoclax:** Highly active combination in R/R FLT3-mutant AML (ORR ~70% in early-phase trials); being evaluated in frontline setting

**Resistance mechanisms to FLT3 inhibitors:**
- **F691L gatekeeper mutation:** Most common resistance mutation; bulky Leu691 steric clash with FLT3 inhibitors; reduces binding affinity of quizartinib and crenolanib; gilteritinib retains partial activity vs. F691L
- **D835 TKD mutations:** Rise under quizartinib pressure (DFG-out inhibitors); gilteritinib (type I) overcomes; but combination F691L+D835 → gilteritinib resistance
- **RAS-pathway mutations:** NRAS/KRAS Q61/G12 mutations acquired under FLT3 inhibitor pressure → ERK bypass; combination with MEK inhibitor (cobimetinib) under investigation
- **BCL-2 upregulation:** MCL-1 upregulation under FLT3-inhibitor-mediated STAT5 reduction → survival through alternative BCL-2 family member; venetoclax + gilteritinib exploits BCL-2 dependence after STAT5 suppression
- **AXL activation:** AXL RTK → PI3K/AKT bypass; gilteritinib (AXL inhibitor) addresses this mechanism but F691L+AXL co-activation → combination needed

**Menin inhibitors in FLT3-ITD + NPM1-mutant AML:**
- **Revumenib (AUGMENT-101):** Menin-KMT2A (MLL) interaction inhibitor; FDA approved 2024 for KMT2A-rearranged or NPM1-mutant AML; ORR 23%, CR 17% in heavily pretreated R/R; works partly by downregulating HOXA9/MEIS1 axis shared with FLT3-ITD biology
- NPM1-mutant + FLT3-ITD AML: Both independently require HOXA9/MEIS1 for self-renewal → revumenib + gilteritinib combination highly rationale → under clinical investigation

## Connections

- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — FLT3-ITD constitutively activates STAT5 (and STAT3) → MCL-1, BCL-XL, cyclin D1, and MYC induction → leukemic blast survival and proliferation; FLT3 inhibition (midostaurin, gilteritinib) rapidly reduces pSTAT5 and triggers apoptosis; STAT5 is the dominant downstream survival effector.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — FLT3-ITD activates MYC via STAT5 → MYC target gene induction (CDK4, cyclin D2, RNR) → cell cycle acceleration; FLT3 inhibition reduces MYC protein; MYC is a co-driver of FLT3-ITD AML self-renewal; combined FLT3 + BET bromodomain inhibition downregulates MYC more potently.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — FLT3-ITD → PI3K → AKT → mTORC1 → protein synthesis and leukemic stem cell (LSC) maintenance; mTOR pathway activation is a resistance mechanism to FLT3 inhibitors; combined FLT3 + mTOR dual inhibition synergizes in FLT3-ITD AML models and may target LSC quiescence.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — FLT3-ITD and KRAS/NRAS mutations activate RAS-MAPK from different points; RAS mutations in ~12% of AML (KRAS G12D/V, NRAS Q61); co-occurrence of FLT3-ITD + RAS mutations drives high ERK activation; acquired RAS mutations are a mechanism of gilteritinib resistance in relapsed FLT3-mutant AML.

[^stone-2017-midostaurin]: Stone RM, Mandrekar SJ, Sanford BL, et al. Midostaurin plus chemotherapy for acute myeloid leukemia with a FLT3 mutation. *N Engl J Med.* 2017;377(5):454-464. [doi:10.1056/NEJMoa1614359](https://doi.org/10.1056/NEJMoa1614359) · [PubMed 28644114](https://pubmed.ncbi.nlm.nih.gov/28644114/)
[^perl-2019-gilteritinib]: Perl AE, Martinelli G, Cortes JE, et al. Gilteritinib or chemotherapy for relapsed or refractory FLT3-mutated AML. *N Engl J Med.* 2019;381(18):1728-1740. [doi:10.1056/NEJMoa1902688](https://doi.org/10.1056/NEJMoa1902688) · [PubMed 31665578](https://pubmed.ncbi.nlm.nih.gov/31665578/)
