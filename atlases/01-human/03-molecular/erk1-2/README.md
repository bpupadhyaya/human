---
schema: human-scale-entry/v1
id: erk1-2
name: ERK1/2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Terminal kinases of the RAS-RAF-MEK-ERK cascade; activated by RTKs, BRAF, and KRAS → RSK, ELK1, c-FOS → proliferation and survival. BRAF V600E and KRAS mutations drive constitutive ERK activation; MEK inhibitors (trametinib, cobimetinib) block ERK in BRAF-mutant tumors."
aliases: ["extracellular signal-regulated kinase", "MAPK3", "MAPK1", "p44/p42 MAPK", "ERK1", "ERK2", "p44 MAPK", "p42 MAPK"]
sources:
  - id: robinson-1997-mapk-review
    type: peer-reviewed
    cite: "Robinson MJ, Cobb MH. Mitogen-activated protein kinase pathways. Curr Opin Cell Biol. 1997;9(2):180-186."
    doi: "10.1016/S0955-0674(97)80061-0"
    pmid: "9069255"
    url: "https://doi.org/10.1016/S0955-0674(97)80061-0"
  - id: wellbrock-2004-raf-review
    type: peer-reviewed
    cite: "Wellbrock C, Karasarides M, Marais R. The RAF proteins take centre stage. Nat Rev Mol Cell Biol. 2004;5(11):875-885."
    doi: "10.1038/nrm1498"
    pmid: "15520807"
    url: "https://doi.org/10.1038/nrm1498"
  - id: long-2015-combi-trial
    type: peer-reviewed
    cite: "Long GV, Stroyakovskiy D, Gogas H, et al. Dabrafenib and trametinib versus dabrafenib and placebo for Val600 BRAF-mutant melanoma: a multicentre, double-blind, phase 3 randomised controlled trial. Lancet. 2015;386(9992):444-451."
    doi: "10.1016/S0140-6736(15)60898-4"
    pmid: "26037941"
    url: "https://doi.org/10.1016/S0140-6736(15)60898-4"
cross_links:
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "ERK1/2 are the terminal kinases activated by BRAF → MEK1/2 → ERK1/2 phosphorylation; BRAF V600E drives constitutive ERK1/2 output in melanoma; vemurafenib + trametinib combines BRAF suppression with downstream MEK-ERK blockade for durable tumor control."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS activates ERK1/2 via RAF-MEK; KRAS-driven ERK1/2 signaling promotes proliferation in pancreatic, colorectal, and lung adenocarcinoma; direct KRAS inhibitors (sotorasib, adagrasib) suppress ERK1/2 output as a key efficacy readout."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "ERK1/2 activates mTOR via RSK → TSC2 inhibition; ERK1/2 and mTOR co-regulate protein synthesis and cell growth; MEK + mTOR inhibitor combinations overcome adaptive feedback resistance in KRAS-mutant and BRAF-mutant cancers."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR activates ERK1/2 via RAS-RAF-MEK; ERK1/2 drives proliferation in NSCLC, CRC, and HNSCC downstream of EGFR; KRAS mutation and ERK1/2 reactivation are the dominant resistance mechanisms to EGFR inhibitors (erlotinib, osimertinib, cetuximab)."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "BRAF V600E in ~50% of melanoma → constitutive MEK-ERK1/2; BRAF+MEK combinations (dabrafenib+trametinib, encorafenib+binimetinib) approved for BRAF V600E/K melanoma; 5-year OS ~34% (COMBI-D); paradoxical ERK1/2 activation by BRAF monotherapy requires mandatory MEK co-blockade."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 (neurofibromin) is a RAS-GAP; NF1 LOF → prolonged RAS-GTP → constitutive RAF-MEK-ERK1/2; NF1-mutant tumors include MPNST, plexiform neurofibroma, and glioma; selumetinib (Koselugo) is FDA-approved for NF1-associated plexiform neurofibromas in pediatric patients ≥2 years."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "ERK1/2 stabilizes c-MYC at Ser62 → prevents GSK-3β Thr58 phosphorylation → blocks β-TrCP ubiquitination; ERK1/2 → RSK → CREB → cyclin D1 → E2F1 cooperate with MYC in cell cycle entry; ERK1/2-MYC axis is central to KRAS-driven oncogenesis in pancreatic and colorectal cancer."
---

# ERK1/2

## Overview

**ERK1 (MAPK3, p44)** and **ERK2 (MAPK1, p42)** are the **terminal effector kinases** of the canonical **RAS-RAF-MEK-ERK mitogen-activated protein kinase (MAPK) cascade** — the most frequently activated oncogenic signaling pathway in human cancer. ERK1/2 are serine/threonine kinases activated by dual phosphorylation (Thr-Glu-Tyr motif) by MEK1/2, which receive input from RAF kinases (BRAF, CRAF/RAF1) downstream of RAS GTPases [^robinson-1997-mapk-review].

**Upstream activation:** Growth factors → RTK (EGFR, HER2, FGFR) → RAS (KRAS, NRAS, HRAS) → RAF (BRAF or CRAF) → MEK1/2 → ERK1/2 Thr202/Tyr204 (ERK1) and Thr185/Tyr187 (ERK2) phosphorylation → full ERK1/2 activation

ERK1/2 signaling is activated by oncogenic mutations in ~35% of all human cancers:
- **KRAS mutation (~25% all cancers):** GTP-locked RAS → constitutive RAF-MEK-ERK flux; pancreatic cancer (>90%), colorectal (40%), NSCLC (30%)
- **BRAF V600E (~8% all cancers):** Constitutive BRAF kinase activity → high-amplitude MEK-ERK activation; melanoma (50%), papillary thyroid cancer (60%), CRC (8-10%), hairy cell leukemia (>95%)
- **NRAS Q61 (~4% of cancers):** Melanoma (15-20%), myeloid malignancies
- **NF1 loss (~5%):** NF1 is a RAS-GAP (GTPase-activating protein); loss → prolonged RAS-GTP → ERK activation; NF1-mutant glioma, melanoma, MPNST

## Structure

### ERK1/2 protein architecture [^robinson-1997-mapk-review]

ERK1 and ERK2 share ~85% sequence identity and are largely functionally redundant, though ERK2 is more highly expressed in most tissues. Both are proline-directed kinases — preferentially phosphorylate Ser/Thr followed by Pro.

**Kinase domain structure:**
- N-terminal lobe: ATP binding (Gly-rich loop, Lys71 [ERK2] for ATP coordination)
- C-terminal lobe: Substrate binding, catalytic Asp165, activation loop (Thr183/Tyr185 in ERK2)
- **Docking groove (D-domain groove):** Hydrophobic + acidic patch → binds DEF (docking for ERK, FXFP) or D-domain motifs on substrates and scaffold proteins (MEK, RSK, ERK phosphatases MKP)
- **TEY activation motif:** Dual phosphorylation of Thr-Glu-Tyr by MEK → activates ERK; this doubly phosphorylated form is detected by diagnostic pERK antibodies used in tumor biomarker testing

**ERK1/2 substrates (>250 known):**
- **Nuclear transcription factors:** ELK1 (SRF co-factor → immediate early gene c-FOS, Egr-1), c-MYC Ser62 (stabilization), ETS factors (PEA3, ER81)
- **Cytoplasmic kinases:** RSK1/2/3/4 → CREB, BAD, S6, TSC2 (mTOR integration); MNK1/2 → eIF4E (cap-dependent translation)
- **Cell cycle regulators:** Cyclin D1 stabilization (via GSK-3β inhibition by RSK); p27 nuclear export → S-phase entry; Rb phosphorylation (via CDK4/6 activation downstream)
- **Pro-apoptotic proteins:** BAD Ser112 (via RSK) → 14-3-3 sequestration → anti-apoptotic; Bim destabilization
- **ERK1/2 feedback:** SOS1 Ser1289 phosphorylation → RAS-GEF inactivation (negative feedback); RAF1 Ser289/296 phosphorylation → RAF1 autoinhibition; EGFR threonine phosphorylation → reduced EGFR activity; this negative feedback is disrupted by MEK inhibitors → paradoxical RAS-ERK reactivation

### ERK1/2 activation dynamics

**Transient vs. sustained ERK1/2:**
- Transient ERK1/2 (minutes) → differentiation signals (e.g., NGF → PC12 neurite outgrowth)
- Sustained ERK1/2 (hours-days) → proliferation; achieved in cancer by sustained oncogenic input exceeding MKP phosphatase activity
- **ERK nuclear translocation:** Upon activation, ERK1/2 dimerize and translocate to nucleus → ELK1, c-FOS, MNK phosphorylation; nuclear ERK is dephosphorylated by nuclear MKP (DUSP) phosphatases

## Function

### Oncogenic ERK1/2 signaling

**Cell cycle entry (G1-S transition):**
- ERK1/2 → RSK2 → CREB → cyclin D1 transcription
- ERK1/2 → c-MYC Ser62 stabilization → proliferative gene program
- ERK1/2 → p27 nuclear export (via RSK phosphorylation of p27) → CDK2 activation → Rb hyperphosphorylation → E2F-dependent S-phase gene expression

**Survival signaling:**
- ERK1/2 → RSK → BAD Ser112 → anti-apoptotic (14-3-3 sequesters BAD from BCL-2/BCL-XL)
- ERK1/2 → MNK1 → eIF4E → cap-dependent translation of survival mRNAs (BCL-2, VEGF, c-MYC)
- ERK1/2 → suppression of BIM via proteasomal targeting

**Angiogenesis:**
- ERK1/2 → HIF-1alpha stabilization (via MNK/eIF4E) → VEGF transcription → tumor angiogenesis

### Adaptive resistance through ERK1/2 pathway reactivation

A critical challenge in oncology is adaptive reactivation of ERK1/2 following targeted therapy:

**BRAF inhibitor (vemurafenib) paradoxical ERK1/2 activation:**
- In RAS-mutant cells: vemurafenib binds BRAF → transactivates CRAF → paradoxical CRAF-MEK-ERK1/2 hyperactivation → accelerates RAS-mutant tumor growth and causes squamoproliferative skin lesions; explanation: BRAF inhibitor drives RAF dimerization; BRAF-CRAF heterodimers are resistant to inhibition and drive ERK output
- Solution: combine BRAF + MEK inhibitors (vemurafenib + cobimetinib; dabrafenib + trametinib) to block both RAF nodes and prevent paradoxical ERK reactivation

**MEK inhibitor resistance:**
- MEK inhibitors → suppress ERK → loss of negative feedback on RAS and RAF → RAS-GTP accumulates → CRAF reactivated → ERK reactivation despite MEK inhibitor; combined BRAF + MEK or BRAF + MEK + ERK inhibitors are being evaluated

## Mechanism

### Therapeutic targeting

**MEK inhibitors (indirect ERK1/2 inhibitors):**
- **Trametinib (Mekinist):** MEK1/2 inhibitor; COMBI-D trial (dabrafenib + trametinib in BRAF V600E melanoma): 5-year OS 34% — landmark improvement over sequential therapy; approved for BRAF V600E/K melanoma, NSCLC, thyroid (anaplastic) [^long-2015-combi-trial]
- **Cobimetinib:** MEK1/2 inhibitor; combined with vemurafenib (coBRIM trial: PFS 12.3 vs. 7.2 months vs. vemurafenib alone); combined with atezolizumab (MEK + PD-L1, IMspire150 trial in melanoma — signals but modest)
- **Binimetinib:** MEK1/2 inhibitor; combined with encorafenib (COLUMBUS trial in BRAF V600E melanoma: PFS 14.9 months); approved in melanoma, CRC (BEACON triplet: encorafenib + binimetinib + cetuximab)

**ERK inhibitors (direct, investigational):**
- **Ulixertinib (BVD-523):** Covalent ERK1/2 inhibitor; active in MEK-inhibitor-resistant tumors with acquired ERK mutations; Phase 1/2 in BRAF/KRAS-mutant solid tumors
- **LY3214996, MK-8353, KO-947:** Clinical trials ongoing; rationale: bypass MEK inhibitor resistance by targeting ERK directly

**ERK1/2 as a biomarker:**
- pERK (phospho-ERK) IHC: surrogate of pathway activation in tumor biopsy; pharmacodynamic endpoint in clinical trials of MEK/BRAF/KRAS inhibitors
- **On-treatment ERK reactivation (serial biopsy or ctDNA):** Predicts acquired resistance; triggers switch or combination therapy

## Connections

- `connects-to` → **[BRAF](../braf/README.md)** — ERK1/2 are the terminal kinases activated by BRAF → MEK1/2 → ERK1/2; BRAF V600E drives constitutive ERK1/2 in melanoma; vemurafenib + trametinib combines BRAF suppression with downstream MEK-ERK blockade for durable tumor control.
- `connects-to` → **[KRAS](../kras/README.md)** — KRAS activates ERK1/2 via RAF-MEK; KRAS-driven ERK1/2 promotes proliferation in pancreatic, colorectal, and lung adenocarcinoma; direct KRAS inhibitors (sotorasib, adagrasib) suppress ERK1/2 output as the key efficacy readout.
- `connects-to` → **[mTOR](../mtor/README.md)** — ERK1/2 activates mTOR via RSK → TSC2 inhibition; ERK1/2 and mTOR co-regulate protein synthesis and growth; MEK + mTOR inhibitor combinations overcome adaptive feedback resistance in KRAS-mutant and BRAF-mutant cancers.
- `connects-to` → **[EGFR](../egfr/README.md)** — EGFR activates ERK1/2 via RAS-RAF-MEK; ERK1/2 drives proliferation in NSCLC, CRC, and HNSCC downstream of EGFR; KRAS mutation and ERK1/2 reactivation are the dominant resistance mechanisms to EGFR inhibitors (erlotinib, osimertinib, cetuximab).
- `connects-to` → **[Melanoma](../../07-system/melanoma/README.md)** — BRAF V600E in ~50% of melanoma → constitutive MEK-ERK1/2; BRAF+MEK combinations (dabrafenib+trametinib, encorafenib+binimetinib) approved for BRAF V600E/K melanoma; 5-year OS ~34% (COMBI-D); paradoxical ERK1/2 activation by BRAF monotherapy requires mandatory MEK co-blockade.
- `connects-to` → **[NF1](../nf1/README.md)** — NF1 (neurofibromin) is a RAS-GAP; NF1 LOF → prolonged RAS-GTP → constitutive RAF-MEK-ERK1/2; NF1-mutant tumors include MPNST, plexiform neurofibroma, and glioma; selumetinib (Koselugo) is FDA-approved for NF1-associated plexiform neurofibromas in pediatric patients ≥2 years.
- `connects-to` → **[Myc](../myc/README.md)** — ERK1/2 stabilizes c-MYC at Ser62 → prevents GSK-3β Thr58 phosphorylation → blocks β-TrCP ubiquitination; ERK1/2 → RSK → CREB → cyclin D1 → E2F1 cooperate with MYC in cell cycle entry; ERK1/2-MYC axis is central to KRAS-driven oncogenesis in pancreatic and colorectal cancer.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^robinson-1997-mapk-review]: Robinson MJ, Cobb MH. Mitogen-activated protein kinase pathways. *Curr Opin Cell Biol.* 1997;9(2):180-186. [doi:10.1016/S0955-0674(97)80061-0](https://doi.org/10.1016/S0955-0674(97)80061-0) · [PubMed 9069255](https://pubmed.ncbi.nlm.nih.gov/9069255/)
[^wellbrock-2004-raf-review]: Wellbrock C, Karasarides M, Marais R. The RAF proteins take centre stage. *Nat Rev Mol Cell Biol.* 2004;5(11):875-885. [doi:10.1038/nrm1498](https://doi.org/10.1038/nrm1498) · [PubMed 15520807](https://pubmed.ncbi.nlm.nih.gov/15520807/)
[^long-2015-combi-trial]: Long GV, Stroyakovskiy D, Gogas H, et al. Dabrafenib and trametinib versus dabrafenib and placebo for Val600 BRAF-mutant melanoma. *Lancet.* 2015;386(9992):444-451. [doi:10.1016/S0140-6736(15)60898-4](https://doi.org/10.1016/S0140-6736(15)60898-4) · [PubMed 26037941](https://pubmed.ncbi.nlm.nih.gov/26037941/)
