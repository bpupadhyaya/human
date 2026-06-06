---
schema: human-scale-entry/v1
id: braf
name: BRAF
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Serine/threonine kinase; V600E mutation constitutively activates MEK-ERK without RAS input. Mutated in ~50% of melanomas, 60% of papillary thyroid cancers, and 10% of CRC. Combined BRAF+MEK inhibition (dabrafenib+trametinib) is standard of care in V600E-mutant melanoma."
aliases: ["BRAF V600E", "v-raf murine sarcoma viral oncogene homolog B", "BRAF kinase", "B-RAF"]
sources:
  - id: davies-2002-braf-mutation
    type: peer-reviewed
    cite: "Davies H, Bignell GR, Cox C, et al. Mutations of the BRAF gene in human cancer. Nature. 2002;417(6892):949-954."
    doi: "10.1038/nature00766"
    pmid: "12068308"
    url: "https://doi.org/10.1038/nature00766"
  - id: chapman-2011-vemurafenib
    type: peer-reviewed
    cite: "Chapman PB, Hauschild A, Robert C, et al. Improved survival with vemurafenib in melanoma with BRAF V600E mutation. N Engl J Med. 2011;364(26):2507-2516."
    doi: "10.1056/NEJMoa1103782"
    pmid: "21639808"
    url: "https://doi.org/10.1056/NEJMoa1103782"
  - id: robert-2015-combi-d
    type: peer-reviewed
    cite: "Robert C, Karaszewska B, Schachter J, et al. Improved overall survival in melanoma with combined dabrafenib and trametinib. N Engl J Med. 2015;372(1):30-39."
    doi: "10.1056/NEJMoa1412690"
    pmid: "25399551"
    url: "https://doi.org/10.1056/NEJMoa1412690"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS and BRAF are mutually exclusive in CRC; both activate MEK-ERK; BRAF V600E bypasses RAS feedback; combined BRAF+MEK inhibition (dabrafenib+trametinib) blocks ERK reactivation, the mechanistic basis for dual-inhibitor superiority over monotherapy."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR→RAS→BRAF→MEK is the canonical MAPK axis; BRAF V600E CRC reactivates EGFR feedback under BRAF inhibition, escaping single-agent blockade; BEACON CRC: cetuximab+encorafenib improved OS vs chemotherapy (9.3 vs 5.9 months), establishing triplet therapy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "MEK-ERK and mTORC1 are parallel downstream effectors of BRAF in melanoma; BRAF inhibitor resistance restores PI3K-AKT-mTOR signaling; combining BRAF+MEK with mTOR inhibitors reverses resistance in preclinical BRAF-mutant tumor models."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "BRAF-MEK-ERK activates STAT3 in melanoma → anti-apoptotic and pro-tumor transcription; STAT3 contributes to BRAF inhibitor resistance; combined BRAF+MEK inhibition suppresses STAT3 activation more effectively than single-agent BRAF inhibition alone."
---

# BRAF

## Overview

**BRAF** is a serine/threonine kinase — the third member of the RAF kinase family (ARAF, BRAF, CRAF/RAF1) — that functions as a central effector of RAS signaling in the **MAPK cascade**: RAS → RAF → MEK → ERK → transcription factors controlling proliferation, survival, and differentiation. The **V600E** point mutation (valine → glutamate at codon 600) is the most clinically important oncogenic mutation in human cancer, discovered in 2002 [^davies-2002-braf-mutation].

**BRAF V600E** (and rarer V600K, V600D, V600R) mutations constitutively activate BRAF kinase activity ~500-fold by mimicking the phosphorylated activation loop state, eliminating the requirement for RAS activation → continuous MEK-ERK signaling without mitogenic input → uncontrolled proliferation and evasion of apoptosis.

**Prevalence across cancer types:**
- **Melanoma:** ~50-60% (V600E in ~80%, V600K in ~15% of BRAF-mutant cases); higher in cutaneous, non-acral/non-mucosal
- **Papillary thyroid cancer:** ~60%; lower grade, better prognosis but prognostic implications with combination therapy
- **Colorectal cancer (CRC):** ~10% (predominantly right-sided; associated with microsatellite instability and hypermethylation phenotype, CIMP); worst prognosis of any CRC subgroup
- **Low-grade glioma:** ~15-20% (especially BRAF-KIAA1549 fusion, pediatric); vemurafenib less effective; MEK inhibitors (selumetinib) now FDA approved for pediatric NF1-associated plexiform neurofibromas
- **Hairy cell leukemia:** ~100% BRAF V600E → vemurafenib highly active
- **Non-small cell lung cancer:** ~2-4% BRAF V600E; dabrafenib+trametinib FDA approved

## Structure

### BRAF protein

BRAF is an **766 amino acid** serine/threonine protein kinase:
- **N-terminal regulatory region:**
  - **RAS-binding domain (RBD, aa 155-227):** CREB-binding protein domain; binds GTP-loaded RAS → relieves autoinhibition → kinase activation
  - **Cysteine-rich domain (CRD, aa 234-280):** Membrane localization; binds diacylglycerol and phorbol esters
- **Proline-rich hinge (aa 280-455):** Connects regulatory and kinase domains; contains BRAF-specific insert
- **Kinase domain (aa 457-712):** Bilobed protein kinase fold:
  - **Activation loop (A-loop, aa 596-600):** pThr598/pSer601 activates kinase; V600E mutation mimics phosphorylated state → constitutive activation
  - **DFG motif (aa 594-596):** Mg²⁺ coordination for ATP binding; "DFG-out" conformation targeted by type II inhibitors (sorafenib)
  - **αC helix:** Regulatory element; glutamate-lysine salt bridge required for catalysis
  - **Hydrophobic spine:** R-spine and C-spine; V600E stabilizes R-spine in active conformation

**Dimerization:**
- Active BRAF forms homodimers (BRAF-BRAF) or heterodimers (BRAF-CRAF); dimerization is required for full kinase activation in normal signaling
- **Paradoxical ERK activation with RAF inhibitors:** First-generation BRAF inhibitors (vemurafenib) bind BRAF V600E monomer but allosterically activate CRAF in the dimer → paradoxical MEK-ERK activation in RAS-mutant cells → cutaneous squamous cell carcinomas (~20-25% of patients); newer inhibitors (PLX8394) are "paradox-breakers"

### BRAF isoforms and class II/III mutations

Beyond class I (V600E, activate as monomer), BRAF mutations include:
- **Class II:** K601E, L597Q — activates as kinase-active dimer; RAS-independent; resistant to many BRAF inhibitors but responsive to MEK inhibitors
- **Class III:** D594G, G466A — kinase-impaired; signals through CRAF (heterodimerization); often co-occurs with RAS mutation

## Function

### MAPK signaling through BRAF

The canonical **RAS-RAF-MEK-ERK cascade:**

1. Growth factor receptor (RTK, e.g., EGFR) → GRB2/SOS → RAS GEF → RAS-GDP → RAS-GTP
2. RAS-GTP recruits BRAF to membrane via RBD → BRAF adopts active conformation → dimerizes
3. **BRAF** phosphorylates **MEK1/2** (MAP2K1/2) on Ser217/Ser221 → MEK activation
4. MEK1/2 phosphorylates **ERK1/2** (MAPK3/MAPK1) on Thr202/Tyr204 and Thr185/Tyr187
5. **ERK** phosphorylates and activates transcription factors: ELK1, RSK → MYC stabilization, FOS/JUN, CREB → proliferative gene program
6. ERK also phosphorylates SOS1 and RAF → **negative feedback** to terminate signaling

**BRAF V600E bypass:** Constitutively active BRAF V600E signals through MEK-ERK without upstream RAS activation → RAF inhibitor treatment releases feedback → RAS reactivates → paradoxical MEK-ERK activation (basis for cutaneous SCC and resistance)

### BRAF inhibition mechanisms and clinical response [^chapman-2011-vemurafenib]

**Vemurafenib (PLX4032, Zelboraf):** First selective BRAF V600E inhibitor; Phase III trial BRIM-3 (2011):
- ORR: 48% vs 5% dacarbazine; median PFS 5.3 vs 1.6 months; OS 13.6 vs 9.7 months
- **Mechanism:** Type I ATP-competitive inhibitor; occupies the active (DFG-in) conformation specifically in BRAF V600E
- **Resistance:** Median duration of response ~7 months; resistance via MEK/ERK reactivation (NRAS mutation, BRAF amplification, MAP2K1/MAP2K2 mutation, alternative splicing of BRAF V600E), PI3K-AKT pathway activation, COT1 kinase

### Combined BRAF+MEK inhibition [^robert-2015-combi-d]

Targeting both BRAF and MEK overcomes the key resistance mechanism (BRAF inhibitor → MEK reactivation) and reduces paradoxical ERK activation (reduced SCC):

**COMBI-D trial (dabrafenib + trametinib vs dabrafenib, treatment-naive BRAF V600E/K melanoma):**
- PFS: 11.0 vs 8.8 months; **5-year OS: 34% (combination) vs 24% (dabrafenib alone)**
- Established dabrafenib+trametinib as standard of care for BRAF-mutant advanced melanoma

**Combination regimens:**
- **Dabrafenib (BRAF) + trametinib (MEK1/2):** Melanoma, NSCLC, thyroid; most commonly used combination
- **Vemurafenib + cobimetinib:** Melanoma (coBRIM trial: PFS 12.3 vs 7.2 months)
- **Encorafenib + binimetinib:** Melanoma (COLUMBUS: PFS 14.9 vs 7.3 months — longest PFS among BRAF+MEK combinations to date); encorafenib has longest BRAF kinase residence time (no paradoxical activation)
- **Encorafenib + cetuximab (+ binimetinib, BEACON CRC):** CRC; ORR 26% (triplet) vs 2% (chemotherapy); approved for BRAF V600E-mutant CRC

**Resistance to dual BRAF+MEK inhibition:**
- **Intrinsic (primary):** High baseline AXL expression, PTEN loss, CDK4 amplification
- **Acquired (secondary):** MEK1 mutations (P124L), ERK1/2 amplification, receptor tyrosine kinase (EGFR, FGFR) upregulation → bypass MEK dependence; PI3K-AKT-mTOR reactivation

## Mechanism

### Adaptive vs. acquired resistance

Resistance to BRAF+MEK inhibition evolves through adaptive and genetic mechanisms:

**Adaptive (early, minutes-hours):** BRAF inhibition reduces ERK-mediated negative feedback on RAS/RAF → RAS-GTP accumulates → CRAF (kinase-active) and alternative MEK signals emerge → initial "adaptive resistance"

**Acquired (weeks-months):**
1. MAPK pathway reactivation: NRAS Q61K/L/R mutation (~20%); BRAF V600E amplification (~10%); BRAF alternative splicing → truncated BRAF that dimerizes constitutively; MAP2K1 mutations (MEK1, resistant to trametinib)
2. PI3K-AKT-mTOR reactivation: PTEN loss, PIK3CA gain-of-function, AKT amplification — bypass MEK dependence entirely
3. Lineage switch: Melanoma cells undergo phenotypic switch from proliferative (BRAF-dependent, MITF-high, S100-low) to invasive (BRAF-independent, MITF-low, AXL/EGFR-high) state → loss of BRAF dependence

**Strategies to overcome resistance:**
- Immunotherapy combinations: Atezolizumab+vemurafenib+cobimetinib (IMspire150) improved PFS; sequential strategy (BRAF+MEK → anti-PD-1) vs concurrent being investigated
- Triplet (BRAF+MEK+EGFR): Encorafenib+binimetinib+cetuximab for CRC
- ERK inhibitors (ulixertinib, MK-8353): Target ERK directly downstream of MEK → overcome MEK mutations; Phase 2 trials in BRAF/MEK inhibitor-resistant melanoma

## Connections

- `connects-to` → **[KRAS](../kras/README.md)** — KRAS and BRAF are mutually exclusive oncogenic drivers in CRC; both activate MEK-ERK; BRAF V600E bypasses RAS input; combined BRAF+MEK inhibition blocks feedback ERK reactivation — mechanistic rationale for dual inhibitor superiority over monotherapy.
- `connects-to` → **[EGFR](../egfr/README.md)** — EGFR→RAS→BRAF→MEK is the canonical MAPK cascade; BRAF V600E CRC reactivates EGFR feedback under BRAF inhibition; BEACON CRC trial established cetuximab+encorafenib ± binimetinib as standard of care for BRAF V600E CRC.
- `connects-to` → **[mTOR](../mtor/README.md)** — MEK-ERK and mTORC1 are parallel BRAF effectors in melanoma; resistance to BRAF+MEK inhibitors frequently restores mTOR via PI3K-AKT; triplet BRAF+MEK+mTOR inhibition reverses resistance in preclinical models.
- `connects-to` → **[STAT3](../stat3/README.md)** — BRAF-MEK-ERK activates STAT3 in melanoma contributing to anti-apoptotic transcription and BRAF inhibitor resistance; combined BRAF+MEK inhibition more effectively suppresses STAT3 than BRAF inhibition alone.

[^davies-2002-braf-mutation]: Davies H, Bignell GR, Cox C, et al. Mutations of the BRAF gene in human cancer. *Nature.* 2002;417(6892):949-954. [doi:10.1038/nature00766](https://doi.org/10.1038/nature00766) · [PubMed 12068308](https://pubmed.ncbi.nlm.nih.gov/12068308/)
[^chapman-2011-vemurafenib]: Chapman PB, Hauschild A, Robert C, et al. Improved survival with vemurafenib in melanoma with BRAF V600E mutation. *N Engl J Med.* 2011;364(26):2507-2516. [doi:10.1056/NEJMoa1103782](https://doi.org/10.1056/NEJMoa1103782) · [PubMed 21639808](https://pubmed.ncbi.nlm.nih.gov/21639808/)
[^robert-2015-combi-d]: Robert C, Karaszewska B, Schachter J, et al. Improved overall survival in melanoma with combined dabrafenib and trametinib. *N Engl J Med.* 2015;372(1):30-39. [doi:10.1056/NEJMoa1412690](https://doi.org/10.1056/NEJMoa1412390) · [PubMed 25399551](https://pubmed.ncbi.nlm.nih.gov/25399551/)
