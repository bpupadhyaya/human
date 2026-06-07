---
schema: human-scale-entry/v1
id: src-kinase
name: SRC Kinase
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Non-receptor tyrosine kinase proto-oncogene; activated by RTKs, integrins, and GPCRs → STAT3, PI3K-AKT signaling → survival, invasion, and angiogenesis. Overexpressed in colon, breast, NSCLC, and HCC; dasatinib and bosutinib inhibit SRC-family kinases in CML and solid tumors."
aliases: ["SRC", "c-Src", "pp60-SRC", "SRC proto-oncogene", "SRC family kinase", "SFK", "Rous sarcoma kinase"]
sources:
  - id: parsons-1984-src-review
    type: peer-reviewed
    cite: "Parsons JT, Weber MJ. Genetics of src: structure and functional organization of a protein tyrosine kinase. Curr Top Microbiol Immunol. 1989;147:79-127."
    doi: "10.1007/978-3-642-74697-0_3"
    pmid: "2513341"
    url: "https://doi.org/10.1007/978-3-642-74697-0_3"
  - id: roskoski-2015-src-review
    type: peer-reviewed
    cite: "Roskoski R Jr. Src protein-tyrosine kinase structure, mechanism, and small molecule inhibitors. Pharmacol Res. 2015;94:9-25."
    doi: "10.1016/j.phrs.2015.01.003"
    pmid: "25662515"
    url: "https://doi.org/10.1016/j.phrs.2015.01.003"
cross_links:
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "SRC directly phosphorylates STAT3 Y705 → STAT3 dimerization → nuclear transcription of MCL-1, VEGF, and cyclin D1; SRC-STAT3 is constitutively active in HNSCC, colon, and pancreatic cancer; dasatinib inhibits SRC → STAT3 dephosphorylation in preclinical models."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "SRC is activated by HER2 and forms a SRC-HER2 complex → phosphorylation of EGFR Y845 → enhanced MAPK; SRC is required for HER2-mediated invasion and migration; dasatinib + lapatinib showed synergy in HER2-positive breast cancer preclinical models."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "SRC activates PI3K → PIP3 → AKT via PDK1; SRC-PI3K-AKT drives survival and anoikis resistance in circulating tumor cells; SRC promotes FAK-PI3K signaling in invasion; dasatinib-mediated SRC inhibition reduces AKT activity in colon and breast cancer models."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "SRC phosphorylates EGFR Y845 → enhanced EGFR kinase activity and sustained MAPK; EGFR activates SRC in a reciprocal feedback loop; SRC-mediated EGFR-independent ERK activation contributes to cetuximab resistance; dual EGFR+SRC inhibition is under clinical investigation."
---

# SRC Kinase

## Overview

**SRC** (cellular Src, c-Src, pp60c-src) is the prototypical non-receptor protein tyrosine kinase and the founding member of the **SRC family kinase (SFK)** group. The viral oncogene v-Src, identified in the Rous sarcoma virus (1911), was the first oncogene discovered; c-Src is its cellular homologue (1976 Nobel Prize context — Bishop and Varmus, 1989). In humans, SRC is encoded by the *SRC* gene on chromosome 20q11.2 and is ubiquitously expressed, with highest levels in platelets, neurons, and epithelial cells [^roskoski-2015-src-review].

SRC integrates signals from **receptor tyrosine kinases (RTKs)**, **integrins**, **G-protein-coupled receptors (GPCRs)**, and **cytokine receptors** → downstream activation of STAT3, PI3K-AKT, RAS-MAPK, and focal adhesion kinase (FAK) → proliferation, survival, motility, invasion, and angiogenesis. SRC is not commonly mutated in cancer but is frequently **overexpressed and hyperactivated** (elevated activity without mutation) in colon, breast, NSCLC, hepatocellular carcinoma (HCC), pancreatic, and head/neck cancers — typically driven by RTK activation or loss of CSK (SRC regulatory kinase).

**SRC family kinases (SFKs):**
- 11 members in humans: SRC, LCK, LYN, FYN, YES, BLK, HCK, FGR, ZAP70 (non-classic), CSK (negative regulator)
- SRC, YES, FYN: Ubiquitous; colon, breast, NSCLC
- LCK, ZAP70: T cell receptor signaling (TCR → ZAP70 → downstream T cell activation)
- LYN, HCK, FGR: Myeloid and B cell signaling; LYN couples BCR to downstream activation
- FYN: Neuronal signaling and T cell co-stimulation
- All SFKs share the same domain architecture and regulatory mechanism; inhibitors (dasatinib, bosutinib) broadly inhibit SFKs [^parsons-1984-src-review]

## Structure

### SRC domain architecture

SRC (536 amino acids, ~60 kDa) has six functional regions, N→C:

**SH4 domain and unique region (residues 1-84):**
- SH4: 15-aa N-terminal segment; contains myristoylation signal (Gly2) → co-translational myristoylation → membrane anchoring; palmitoylation at Cys3 in LYN/FYN (not SRC itself) → lipid raft association
- Unique region: ~50 aa with no known structure; low sequence conservation among SFKs; site of some regulatory phosphorylations; target of PDZ domain proteins

**SH3 domain (residues 85-140):**
- ~55 aa; canonical SH3 fold (5-stranded beta-barrel); recognizes left-handed PPII helix (PxxP motif) → protein-protein interactions
- In inactive SRC: SH3 domain engages the SH2-kinase linker (which contains a PPII element) → intramolecular interaction that locks SRC in closed/inactive conformation
- SH3 binds proline-rich sequences in FAK, PI3K, and receptor tails → substrate targeting

**SH2 domain (residues 141-248):**
- ~100 aa; binds phosphotyrosine (pTyr)-containing peptides (EEpYFEL consensus for SRC SH2)
- In inactive SRC: SH2 domain binds the C-terminal phosphotyrosine **pY530** (phosphorylated by CSK) → closed, inactive "clamp" conformation
- When Y530 is dephosphorylated (by PTP1B, SHP-1/2) or displaced (by high-affinity pTyr ligands), SH2 releases → open, active conformation

**SH2-kinase linker (residues 248-270):**
- Flexible linker containing a PXXP motif → engaged by SH3 in closed SRC conformation
- Dephosphorylation of Y530 + linker disengagement → cooperatively open SRC → autophosphorylation at Y419 → full activation

**Kinase domain (SH1, residues 271-523):**
- Classic bilobal protein kinase fold: N-lobe (5 beta-strands + αC helix) + C-lobe (7 alpha-helices)
- **Activation loop (A-loop):** Contains Y419 (activation loop phosphorylation); autophosphorylation at Y419 stabilizes open A-loop conformation → full catalytic activity; in inactive SRC, A-loop folds back and blocks substrate access
- **Gatekeeper residue T338:** The threonine gatekeeper allows imatinib-class inhibitors to bind (unlike bulky mutations); T338I/M → steric resistance to type-I ATP-competitive inhibitors
- **αC helix (Glu310):** Glu310-Lys295 salt bridge in active kinase → stabilizes catalytic lysine for ATP coordination
- **DFG motif:** DFG-in = active state; DFG-out = inactive state; type II inhibitors (imatinib-like) bind DFG-out; SRC is generally targeted in DFG-in by dasatinib/bosutinib

**C-terminal regulatory tail (residues 524-536):**
- Contains **Y530** (numbered Y527 in chicken v-Src; human Y530 = chicken Y527 equivalent)
- CSK phosphorylates Y530 → pY530-SH2 intramolecular interaction → inactive closed SRC
- PTP1B and other phosphatases dephosphorylate pY530 → SRC activation
- v-Src lacks the C-terminal tail entirely → constitutively active → oncogenic transformation

### Regulatory mechanism

**Closed (inactive) SRC conformation:**
- pY530 → SH2 intramolecular binding → SH3 → linker binding → bilobal kinase in inactive conformation; ATP can still bind but substrate access restricted
- Y419 dephosphorylated in inactive SRC

**SRC activation:**
1. CSK inactivation or PTP1B/SHP-2 activation → Y530 dephosphorylation
2. OR: high-affinity pTyr peptide (from activated RTK — EGFR pY974, HER2 pY1221) competes for SH2 → displaces pY530 → SH2 released
3. OR: activated integrin → clustering of FAK → SRC SH2 binding to FAK pY397 → Y530 displacement
4. Once SH2 released: SH3-linker interaction also breaks → open conformation → A-loop Y419 exposed → trans-autophosphorylation (SRC dimer or via signaling complex)
5. pY419 → fully active SRC; can be sustained even if pY530 re-engaged (biphasic regulation)

## Function

### SRC signaling outputs

**STAT3 pathway:**
- Active SRC → direct phosphorylation of STAT3 at Y705 → STAT3 dimerization and nuclear translocation → transcription of MCL-1, BCL-XL, VEGF, cyclin D1, survivin, and c-MYC
- SRC-STAT3 constitutive activation is a hallmark of HNSCC, colorectal cancer, and pancreatic ductal adenocarcinoma (PDAC); STAT3 Y705 phosphorylation level correlates with SRC activity

**PI3K-AKT pathway:**
- Active SRC → direct phosphorylation of p85 regulatory subunit of PI3K → PI3K activation → PIP3 → PDK1 → AKT; SRC also phosphorylates IRS-1 as an alternate PI3K activator
- SRC-AKT provides anoikis resistance in circulating tumor cells (CTCs) → critical for metastatic dissemination; SRC inhibition sensitizes CTCs to anoikis in preclinical models

**RAS-MAPK pathway:**
- SRC → Grb2-SOS recruitment (via Grb2 SH2 binding to SRC pY) → RAS → RAF-MEK-ERK
- SRC also phosphorylates EPS8 → RAC1 → lamellipodia → cytoskeletal remodeling for migration
- SRC-mediated ERK activation can bypass EGFR blockade → cetuximab resistance mechanism in colorectal cancer

**Focal adhesion kinase (FAK):**
- **SRC-FAK complex is the master regulator of cell adhesion, migration, and invasion**
- Integrin clustering (fibronectin, vitronectin, collagen) → FAK autophosphorylation at Y397 → SRC SH2 binding → SRC activation → SRC phosphorylates FAK at Y576/577 (A-loop) + Y925 (Grb2 binding) → full FAK activation → paxillin, talin, vinculin → focal adhesion assembly and turnover
- SRC-FAK complex drives matrix metalloproteinase (MMP) secretion and invadopodia formation → basement membrane degradation → invasion and metastasis

**EGFR transactivation:**
- SRC phosphorylates EGFR at Y845 (within the kinase domain A-loop) → enhanced EGFR kinase activity and resistance to receptor internalization → sustained MAPK signaling
- EGFR reciprocally activates SRC via pY845-SH2 binding → positive feedback loop; this circuit is active at focal adhesions and contributes to anchorage-independent growth

**Angiogenesis (VEGFR2):**
- VEGF → VEGFR2 → SRC activation → VE-cadherin Y658 phosphorylation → endothelial junction opening → vascular permeability (Src-knockout mice are resistant to VEGF-induced permeability)
- SRC also activates VEGFR2 in a paracrine manner from tumor cells → endothelial activation → neovascularization of tumors

### SRC in cancer

| Cancer type | SRC status | Mechanism |
|------------|------------|----------|
| **Colorectal cancer** | Overexpressed; 80-90% of tumors | Activation by EGFR, IGF-1R; SRC-STAT3-MCL-1 survival; cetuximab resistance |
| **Breast cancer (TNBC)** | Overexpressed; hyperactivated | SRC-FAK invasion; SRC activates HER2; dasatinib activity in preclinical TNBC |
| **NSCLC** | Overexpressed; activated by EGFR | Bypass of EGFR TKI → erlotinib/osimertinib resistance; SRC inhibition restores sensitivity |
| **Hepatocellular carcinoma** | Overexpressed; mutated (rare, <5%) | HBV X protein → SRC activation; SRC-STAT3-cyclin D1 proliferation |
| **HNSCC** | Overexpressed; EGFR-driven | SRC-EGFR-STAT3 axis; cetuximab resistance via SRC bypass |
| **Pancreatic cancer** | Overactivated | SRC-integrin-FAK-invasion; SRC drives EMT and metastasis |

**SRC mutations in cancer:**
- SRC is rarely mutated in cancer (unlike EGFR, KRAS); copy number gain (20q11.2 region) is more common; overexpression and post-translational activation (CSK loss, tyrosine phosphatase dysregulation) are the dominant mechanisms
- Rare activating mutations (E531K, D531N) described in colorectal cancer (~5%)

## Mechanism

### SRC inhibitors

**Dasatinib (BMS-354825, Sprycel):**
- Multi-kinase inhibitor targeting BCR-ABL, SRC, KIT, PDGFR, EPHA2; Type I inhibitor binding both DFG-in conformations
- **Approved for:** CML (first-line, after imatinib failure), Ph+ ALL
- SRC inhibition mechanism: Dasatinib binds SRC kinase domain in active DFG-in conformation; 300× more potent than imatinib vs. BCR-ABL; ~3-fold more potent vs. SRC than ABL; very low IC50 (~0.5 nM for SRC)
- Solid tumor activity: Modest single-agent activity; trials ongoing in combination with chemotherapy and immunotherapy for TNBC, NSCLC, colorectal cancer
- Side effects: Pleural effusion (~15-35%; class effect via SRC inhibition in pleural mesothelium), bleeding (platelet SRC), fluid retention; BCR-ABL mutations (T315I gatekeeper) cause dasatinib resistance (requires ponatinib)

**Bosutinib (SKI-606, Bosulif):**
- Dual BCR-ABL + SRC inhibitor; Type I; approved for CML after failure of prior TKI therapy
- Less potent vs. SRC than dasatinib; less PDGFR/KIT inhibition → fewer fluid retention side effects; diarrhea and liver toxicity are class issues

**Saracatinib (AZD0530):**
- Selective SRC/ABL inhibitor; extensive clinical evaluation in solid tumors; modest single-agent activity in colorectal, NSCLC, and ovarian cancer; clinical development largely discontinued due to insufficient efficacy; used as pharmacodynamic tool (confirmed SRC pY419 inhibition but failed to translate to tumor response)

**Steroid-sparing effects of SRC inhibition:**
- SRC drives osteoclast function (via SRC-integrin-FAK in osteoclast podosomes); SRC-knockout mice have osteopetrosis (dense bones); SRC inhibitors (dasatinib) reduce bone resorption → rationale for combinations with bone-directed therapy in prostate/breast bone metastases

### Resistance to SRC inhibitors

- **EGFR/MAPK rebound:** SRC inhibition → loss of negative feedback on RAS → rebound ERK activation → proliferative survival
- **PI3K pathway upregulation:** SRC inhibition → loss of PTEN regulation → AKT rebound via PI3K
- **FAK pathway bypass:** FAK can activate PI3K independently of SRC in some contexts → motility and invasion preserved despite SRC inhibition
- **BCR-ABL T315I (gatekeeper):** In CML setting, T315I mutation causes dasatinib resistance; ponatinib (pan-BCR-ABL inhibitor) or asciminib (STAMP inhibitor binding myristoyl pocket) overcome T315I

## Connections

- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — SRC directly phosphorylates STAT3 Y705 → STAT3 dimerization → nuclear transcription of MCL-1, VEGF, and cyclin D1; SRC-STAT3 is constitutively active in HNSCC, colon, and pancreatic cancer; dasatinib inhibits SRC → STAT3 dephosphorylation in preclinical models.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — SRC is activated by HER2 and forms a SRC-HER2 complex → phosphorylation of EGFR Y845 → enhanced MAPK; SRC is required for HER2-mediated invasion and migration; dasatinib + lapatinib showed synergy in HER2-positive breast cancer preclinical models.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — SRC activates PI3K → PIP3 → AKT via PDK1; SRC-PI3K-AKT drives survival and anoikis resistance in circulating tumor cells; SRC promotes FAK-PI3K signaling in invasion; dasatinib-mediated SRC inhibition reduces AKT activity in colon and breast cancer models.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — SRC phosphorylates EGFR Y845 → enhanced EGFR kinase activity and sustained MAPK; EGFR activates SRC in a reciprocal feedback loop; SRC-mediated EGFR-independent ERK activation contributes to cetuximab resistance; dual EGFR+SRC inhibition is under clinical investigation.

[^parsons-1984-src-review]: Parsons JT, Weber MJ. Genetics of src: structure and functional organization of a protein tyrosine kinase. *Curr Top Microbiol Immunol.* 1989;147:79-127. [doi:10.1007/978-3-642-74697-0_3](https://doi.org/10.1007/978-3-642-74697-0_3) · [PubMed 2513341](https://pubmed.ncbi.nlm.nih.gov/2513341/)
[^roskoski-2015-src-review]: Roskoski R Jr. Src protein-tyrosine kinase structure, mechanism, and small molecule inhibitors. *Pharmacol Res.* 2015;94:9-25. [doi:10.1016/j.phrs.2015.01.003](https://doi.org/10.1016/j.phrs.2015.01.003) · [PubMed 25662515](https://pubmed.ncbi.nlm.nih.gov/25662515/)
