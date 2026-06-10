---
schema: human-scale-entry/v1
id: egfr
name: EGFR
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "ErbB1/HER1 receptor tyrosine kinase; EGF binding activates RAS-ERK, PI3K-Akt, and STAT3. Mutated or amplified in NSCLC, glioblastoma, HNSCC, and CRC. Targeted by gefitinib/erlotinib (EGFR-mutant NSCLC) and cetuximab (KRAS-WT CRC, HNSCC); osimertinib overcomes T790M resistance."
aliases: ["ErbB1", "HER1", "epidermal growth factor receptor", "ERBB1", "EGF receptor"]
sources:
  - id: yarden-2001-erbb
    type: peer-reviewed
    cite: "Yarden Y, Sliwkowski MX. Untangling the ErbB signalling network. Nat Rev Mol Cell Biol. 2001;2(2):127-137."
    doi: "10.1038/35052073"
    pmid: "11252954"
    url: "https://doi.org/10.1038/35052073"
  - id: lynch-2004-egfr-mutation
    type: peer-reviewed
    cite: "Lynch TJ, Bell DW, Sordella R, et al. Activating mutations in the epidermal growth factor receptor underlying responsiveness of non-small-cell lung cancer to gefitinib. N Engl J Med. 2004;350(21):2129-2139."
    doi: "10.1056/NEJMoa040938"
    pmid: "15118073"
    url: "https://doi.org/10.1056/NEJMoa040938"
  - id: mok-2009-ipass
    type: peer-reviewed
    cite: "Mok TS, Wu YL, Thongprasert S, et al. Gefitinib or carboplatin-paclitaxel in pulmonary adenocarcinoma. N Engl J Med. 2009;361(10):947-957."
    doi: "10.1056/NEJMoa0810699"
    pmid: "19692680"
    url: "https://doi.org/10.1056/NEJMoa0810699"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS is the primary downstream effector of EGFR; oncogenic KRAS mutations bypass EGFR, rendering cetuximab ineffective in RAS-mutant CRC (RAS-WT required for cetuximab benefit); EGFR also drives adaptive KRAS G12C inhibitor resistance via SOS1-mediated feedback."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "EGFR activates PI3K-Akt-mTOR via PI3Kα (p110α) which binds Ras-GTP downstream of EGFR; mTORC1-driven protein synthesis and anti-apoptosis supports EGFR-mutant tumor survival; combined EGFR + mTOR inhibition overcomes PI3K reactivation that limits single-agent EGFR TKI efficacy."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "EGFR directly phosphorylates STAT3 (Tyr705) and activates it via JAK2 → STAT3 drives PD-L1, survivin, Bcl-xL, and MYC expression in EGFR-mutant tumors; STAT3 activation is a key survival pathway in tumors that acquire resistance to EGFR TKIs through EGFR-independent signaling."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β and EGFR signaling cooperate in EMT: EGFR activation promotes SNAIL/TWIST expression; TGF-β drives SMAD-dependent E-cadherin repression; combined EGFR + TGF-β signaling drives mesenchymal transition and invasiveness in NSCLC and HNSCC particularly after EGFR TKI resistance."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "EGFR is the most targetable driver in NSCLC (~20% of non-squamous); osimertinib is standard 1st-line for L858R/exon19del (FLAURA: OS 38.6 vs 31.8 months vs comparator TKI); T790M resistance → osimertinib; C797S → amivantamab; exon 20 insertion → amivantamab+chemo (PAPILLON)."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Cetuximab/panitumumab (anti-EGFR mAbs) benefit only RAS-WT CRC (~50%); KRAS/NRAS mutations bypass EGFR → anti-EGFR mAbs futile; EGFR amplification occurs in ~5% of CRC; addition of cetuximab to FOLFOX improves PFS in 1st-line RAS-WT mCRC (CRYSTAL: ORR 57% vs 40%)."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "EGFR (ErbB1) and HER2 (ErbB2) are ErbB family RTKs that form heterodimers → amplified signaling; co-overexpression in HNSCC, NSCLC, gastric; pertuzumab disrupts HER2-EGFR heterodimerization; EGFR/HER2 cross-talk drives primary resistance to single-agent EGFR TKIs in NSCLC."
---

# EGFR

## Overview

**EGFR (epidermal growth factor receptor, ErbB1/HER1)** is a **receptor tyrosine kinase (RTK)** of the ErbB family — the prototype of a four-member subfamily (EGFR/HER1, HER2/ErbB2, HER3/ErbB3, HER4/ErbB4) that governs epithelial cell proliferation, survival, differentiation, and migration throughout development and tissue homeostasis. EGFR was among the first oncoproteins identified (1984, Downward and Ullrich), catalyzing the era of targeted cancer therapy.

**Ligands:** EGFR is activated by seven EGF-family ligands: EGF, TGF-α, HB-EGF (heparin-binding EGF), amphiregulin, betacellulin, epiregulin, epigen — produced by stromal cells, tumor cells, and inflammatory cells as autocrine and paracrine signals.

**Canonical activation cascade:**
- Ligand → EGFR dimerization (homo- or heterodimerization with HER2/3/4) → allosteric activation of intracellular kinase domain → trans-autophosphorylation of C-terminal tyrosines (Tyr992, Tyr1045, Tyr1068, Tyr1086, Tyr1148, Tyr1173) → docking sites for SH2/PTB-domain adaptors → activation of RAS-MAPK, PI3K-Akt, PLCγ, and STAT3 pathways

**Oncogenic alterations:**
- **Activating mutations** (NSCLC): Exon 19 deletions (del19, ~45%) and L858R point mutation (exon 21, ~40%) — together >85% of sensitizing mutations; constitutively active kinase domain; exquisitely sensitive to 1st/2nd-gen TKIs
- **Amplification:** Glioblastoma (~40%), HNSCC (~30%), CRC (~5%); drives ligand-independent signaling
- **Overexpression:** Head and neck, breast, CRC, lung — correlates with poor prognosis
- **EGFRvIII deletion mutant:** In-frame deletion of exons 2-7 → constitutively active, ligand-independent; in ~50% of EGFR-amplified GBM; not targetable by standard TKIs (no ligand-binding pocket)

**Clinical targeting:**
- **EGFR TKIs** for NSCLC with sensitizing mutations (del19/L858R): gefitinib/erlotinib (1st gen), afatinib/dacomitinib (2nd gen, irreversible), osimertinib (3rd gen, T790M-selective and now 1st line)
- **Anti-EGFR antibodies:** Cetuximab, panitumumab — for KRAS/NRAS-WT CRC and HNSCC

## Structure

### ErbB family architecture [^yarden-2001-erbb]

All four ErbB receptors share a common four-domain extracellular architecture:
- **Domain I (L1) and Domain III (L2):** Leucine-rich repeat domains; ligand binding (primarily domains I and III create the ligand-binding cleft)
- **Domain II (CR1) and Domain IV (CR2):** Cysteine-rich dimerization domains; tethering loop in Domain II is essential for EGFR homodimerization; domain IV contains an autoinhibitory "tether" (intramolecular interaction with Domain II that holds EGFR in inactive closed conformation)
- **Transmembrane domain:** Single-pass α-helix; transmits dimerization to intracellular domain
- **Juxtamembrane domain:** Required for kinase activation; NLS sequence for nuclear EGFR translocation
- **Kinase domain:** EGFR kinase activates by asymmetric dimerization: the "activator" kinase (C-lobe of one monomer) contacts the "receiver" kinase (N-lobe of the other) → activates receiver in a mechanism analogous to cyclin-CDK activation
- **C-terminal tail:** Contains tyrosine phosphorylation sites; docking sites for Grb2 (via Tyr1068 → SOS → Ras), Shc (via Tyr1148/1173 → Ras), PLCγ (via Tyr992), GAB1 (via Tyr1045 → PI3K), STAT3/5

**HER2 is the preferred dimerization partner:** HER2 has no known high-affinity ligand and an open, dimerization-ready conformation → acts as co-receptor amplifying all ErbB signals; HER2 amplification hijacks this role → amplifies EGFR/HER3/HER4 downstream signaling without EGFR mutation

### EGFR mutations in NSCLC [^lynch-2004-egfr-mutation]

| Mutation | Type | Frequency | TKI sensitivity |
|:---|:---|:---|:---|
| Exon 19 del (del746-750) | Deletion, activating | ~45% of sensitizing | Osimertinib > afatinib > erlotinib |
| L858R (exon 21) | Point mutation, activating | ~40% of sensitizing | All TKI generations; similar to del19 |
| T790M (exon 20) | Point mutation, resistance | ~60% of 1st/2nd-gen resistance | Osimertinib (3rd-gen) |
| Exon 20 insertions | Insertion, activating | ~4% NSCLC | Amivantamab + lazertinib; mobocertinib |
| G719X, L861Q, S768I | Uncommon activating | ~5% | Afatinib, osimertinib |

## Function

### EGFR downstream signaling branches

**RAS-MAPK pathway:**
- EGFR (pTyr1068) → Grb2 (SH2) → SOS1 (GEF) → Ras-GTP → RAF1/BRAF → MEK1/2 → ERK1/2 → nuclear: ELK1, c-Fos, AP-1 → proliferation, survival, migration
- The **Grb2-SOS1 axis** is the critical EGFR→KRAS adapter; SOS1 inhibitors (BI-1701963) block EGFR→KRAS→GTP loading → antitumor activity in KRAS G12C-resistant tumors

**PI3K-Akt-mTOR pathway:**
- EGFR → direct p85α (PI3K regulatory subunit) binding at pTyr992/1045 → PI3Kα activation → PIP3 → Akt → TSC2 → mTORC1; also via Ras-GTP → PI3Kα direct interaction
- Dominant survival pathway; PTEN loss (common in GBM) constitutively activates this arm independent of EGFR

**PLCγ-PKC pathway:**
- EGFR (pTyr992) → PLCγ-SH2 binding → PLCγ activated → PIP2 cleavage → IP3 (→ Ca²⁺ release) + DAG (→ PKC activation) → proliferation, secretion, cytoskeletal effects
- Particularly important in non-epithelial EGFR signaling contexts

**STAT3 pathway:**
- EGFR directly phosphorylates STAT3 (Tyr705) or activates JAK2 → STAT3; nuclear STAT3 drives survival (BCL-XL, MCL-1, survivin), proliferation (cyclin D1), angiogenesis (VEGF), and immune evasion (PD-L1, IL-10)

### EGFR in normal physiology

- **Skin:** Keratinocyte proliferation and migration; EGFR TKIs cause acneiform rash (on-target; correlates with TKI efficacy) and paronychia
- **GI epithelium:** Mucosal maintenance; cetuximab causes GI toxicity (mucosal inflammation)
- **Wound healing:** EGF and TGF-α promote re-epithelialization; ophthalmic EGF drops used for persistent corneal epithelial defects

### EGFRvIII in glioblastoma

EGFRvIII (deletion of exons 2-7 → 267 aa in-frame deletion) is found exclusively in cancer (not normal tissue):
- Constitutively active without ligand binding (altered structure of extracellular domain creates unpaired Cys → activates kinase)
- Present in ~25-30% of GBM; co-occurs with EGFR amplification (~50% of EGFR-amplified GBM have EGFRvIII)
- Therapeutic target: AMG-595 (anti-EGFRvIII ADC), anti-EGFRvIII CAR-T cells (Phase I), depatuxizumab mafodotin (ABT-414, anti-EGFR ADC) — all in clinical development; depatuxizumab Phase III (INTELLANCE-1) failed

## Mechanism

### EGFR TKI resistance and osimertinib [^mok-2009-ipass]

**1st generation gefitinib/erlotinib (IPASS trial, 2009):**
- IPASS: gefitinib vs carboplatin-paclitaxel in Asian EGFR-mutant NSCLC → PFS 9.5 vs 6.3 months (HR 0.48); transformed EGFR-mutant NSCLC management; Asian prevalence ~35% (vs ~15% in Western populations)

**T790M resistance mechanism:**
- T790M substitution in exon 20: Thr→Met at gatekeeper residue → steric clash with 1st/2nd gen TKIs (competitive with ATP) → 100-1000× reduced TKI affinity; also increases intrinsic kinase activity
- Occurs in ~60% of patients after 1st/2nd gen TKI (acquired resistance, ~12 months median)

**Osimertinib (AZD9291, Tagrisso, 3rd gen):**
- Covalent irreversible inhibitor of C797 in EGFR kinase domain → doesn't require Thr790 binding → overcomes T790M
- Selectivity: ~200× more potent against T790M than WT EGFR → spares rash/GI toxicity at therapeutic doses
- **FLAURA trial (1st-line):** Osimertinib vs gefitinib/erlotinib in EGFR-mutant NSCLC → PFS 18.9 vs 10.2 months, OS 38.6 vs 31.8 months → osimertinib is now 1st-line standard of care
- CNS activity: osimertinib crosses BBB well (CNS ORR 91% in CNS-metastasis cohort)

**Post-osimertinib resistance mechanisms:**
- **C797S mutation** (exon 20): Removes osimertinib's covalent binding cysteine → resistance; if T790M+C797S in trans → may respond to combination 1st/3rd gen TKI
- **MET amplification:** ~15% of acquired resistance; rationale for osimertinib + savolitinib (MET TKI) combination
- **EGFR amplification:** Overcomes osimertinib via kinase overdrive
- **RAS/RAF/MEK mutations:** Bypass EGFR dependency
- **Cell state transition:** Epithelial-mesenchymal transition (EMT), small cell transformation (~5%)

### Cetuximab and anti-EGFR antibodies

**Cetuximab (Erbitux, IgG1 anti-EGFR):**
- Competitive with EGF for EGFR domain III binding → blocks ligand binding → no EGFR dimerization → no kinase activation; also induces ADCC (IgG1 Fc → NK cell/macrophage killing of EGFR-expressing tumor cells)
- **CRC:** Requires KRAS/NRAS exon 2-4 wildtype (RAS-WT) → ~50% of CRC; ORR ~25% monotherapy, ~55% with FOLFOX in 1st-line RAS-WT mCRC (CRYSTAL trial)
- **HNSCC:** Cetuximab + platinum/5-FU improved OS in recurrent/metastatic HNSCC (EXTREME trial); pembrolizumab now replacing in PD-L1+ disease

## Connections

- `connects-to` → **[KRAS](../kras/README.md)** — KRAS is downstream of EGFR (RAS-MAPK); oncogenic KRAS bypasses EGFR → cetuximab futile in RAS-mutant CRC; EGFR drives adaptive feedback against KRAS G12C inhibitors via SOS1.
- `connects-to` → **[mTOR](../mtor/README.md)** — EGFR activates PI3K→Akt→mTORC1; mTOR-driven anabolism supports EGFR-mutant tumor survival; combined EGFR + mTOR inhibition overcomes PI3K reactivation resistance in EGFR-mutant NSCLC.
- `connects-to` → **[STAT3](../stat3/README.md)** — EGFR directly activates STAT3 and via JAK2; nuclear STAT3 drives PD-L1, survivin, and BCL-XL — key survival genes in EGFR-mutant tumors; STAT3 activation is an alternative pathway in TKI resistance.
- `connects-to` → **[TGF-β](../tgf-beta/README.md)** — TGF-β and EGFR cooperate in epithelial-mesenchymal transition; combined signaling drives invasiveness in NSCLC and HNSCC; TGF-β-driven EMT is a key mechanism of acquired EGFR TKI resistance.
- `connects-to` → **[NSCLC](../../07-system/nsclc/README.md)** — EGFR is the most targetable driver in NSCLC (~20% of non-squamous); osimertinib is standard 1st-line for L858R/exon19del (FLAURA: OS 38.6 vs 31.8 months vs comparator TKI); T790M resistance → osimertinib; C797S → amivantamab; exon 20 insertion → amivantamab+chemo (PAPILLON).
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — Cetuximab/panitumumab (anti-EGFR mAbs) benefit only RAS-WT CRC (~50%); KRAS/NRAS mutations bypass EGFR → anti-EGFR mAbs futile; EGFR amplification occurs in ~5% of CRC; addition of cetuximab to FOLFOX improves PFS in 1st-line RAS-WT mCRC (CRYSTAL: ORR 57% vs 40%).
- `connects-to` → **[HER2](../her2/README.md)** — EGFR (ErbB1) and HER2 (ErbB2) are ErbB family RTKs that form heterodimers → amplified signaling; co-overexpression in HNSCC, NSCLC, gastric; pertuzumab disrupts HER2-EGFR heterodimerization; EGFR/HER2 cross-talk drives primary resistance to single-agent EGFR TKIs in NSCLC.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^yarden-2001-erbb]: Yarden Y, Sliwkowski MX. Untangling the ErbB signalling network. *Nat Rev Mol Cell Biol.* 2001;2(2):127-137. [doi:10.1038/35052073](https://doi.org/10.1038/35052073) · [PubMed 11252954](https://pubmed.ncbi.nlm.nih.gov/11252954/)
[^lynch-2004-egfr-mutation]: Lynch TJ, Bell DW, Sordella R, et al. Activating mutations in the epidermal growth factor receptor underlying responsiveness of non-small-cell lung cancer to gefitinib. *N Engl J Med.* 2004;350(21):2129-2139. [doi:10.1056/NEJMoa040938](https://doi.org/10.1056/NEJMoa040938) · [PubMed 15118073](https://pubmed.ncbi.nlm.nih.gov/15118073/)
[^mok-2009-ipass]: Mok TS, Wu YL, Thongprasert S, et al. Gefitinib or carboplatin-paclitaxel in pulmonary adenocarcinoma. *N Engl J Med.* 2009;361(10):947-957. [doi:10.1056/NEJMoa0810699](https://doi.org/10.1056/NEJMoa0810699) · [PubMed 19692680](https://pubmed.ncbi.nlm.nih.gov/19692680/)
