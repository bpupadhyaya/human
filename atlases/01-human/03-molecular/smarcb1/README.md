---
schema: human-scale-entry/v1
id: smarcb1
name: SMARCB1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "SMARCB1 (INI1/BAF47) is a core SWI/SNF BAF complex subunit; biallelic LOF in ~100% AT/RT, rhabdoid tumors, and epithelioid sarcoma; SMARCB1 loss → PRC2/EZH2-mediated H3K27me3 at tumor suppressor loci; tazemetostat (EZH2 inhibitor) FDA-approved for epithelioid sarcoma."
aliases: ["SMARCB1", "INI1", "BAF47", "SNF5", "hSNF5", "SMARCB1 rhabdoid", "INI1 loss", "rhabdoid tumor predisposition", "RTPS1", "SWI/SNF tumor suppressor"]
sources:
  - id: versteege-1998-smarcb1-rhabdoid
    type: peer-reviewed
    cite: "Versteege I, Sévenet N, Lange J, et al. Truncating mutations of hSNF5/INI1 in aggressive paediatric cancer. Nature. 1998;394(6689):203-206."
    doi: "10.1038/28212"
    pmid: "9671307"
    url: "https://doi.org/10.1038/28212"
  - id: gounder-2020-tazemetostat-epithelioid
    type: peer-reviewed
    cite: "Gounder M, Schöffski P, Jones RL, et al. Tazemetostat in advanced epithelioid sarcoma with loss of INI1/SMARCB1: an international, open-label, phase 2 basket study. Lancet Oncol. 2020;21(11):1423-1432."
    doi: "10.1016/S1470-2045(20)30451-4"
    pmid: "33007258"
    url: "https://doi.org/10.1016/S1470-2045(20)30451-4"
cross_links:
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "SMARCB1 BAF complex antagonizes PRC2/EZH2 at enhancers; SMARCB1 LOF → SWI/SNF absent → PRC2/EZH2 gains access → H3K27me3 spreads → silences tumor suppressors and differentiation loci; SMARCB1-null tumors are uniquely EZH2-dependent → tazemetostat sensitivity."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "SMARCB1 loss → SWI/SNF cannot maintain open chromatin at CDKN2A locus → p16/INK4A ↓ and p14/ARF ↓ → CDK4/6 hyperactivation → RB1 phosphorylation → E2F-driven proliferation; CDK4/6 inhibitors partially rescue G1 arrest in SMARCB1-null cells when RB1 intact."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "SMARCB1 loss → SWI/SNF cannot activate CDKN2A promoter → p16/INK4A and p14/ARF both silenced; CDKN2A re-expression upon SMARCB1 rescue drives G1 arrest in rhabdoid tumor cells; CDKN2A homozygous deletion occurs in ~15-25% AT/RT and further ablates this checkpoint."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "SMARCB1-containing BAF complex occupies MYC-target gene enhancers to limit MYC-driven transcription; SMARCB1 loss → BRD4-dependent super-enhancer activity at MYC → MYC target gene hyperactivation; BET inhibitors (JQ1) suppress MYC in SMARCB1-null rhabdoid and AT/RT cells."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "SMARCB1 loss → p14/ARF silenced → MDM2 unchecked → p53 degraded despite intact TP53; TP53 mutations uncommon in AT/RT; doxorubicin/vinca chemotherapy depends on residual p53-mediated apoptosis; SMARCB1 rescue restores p14/ARF → p53 re-activation and G1 arrest."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "SMARCB1 and ARID1A are SWI/SNF tumor suppressor subunits with distinct tumor spectra (SMARCB1: rhabdoid/AT/RT; ARID1A: endometrial/ovarian/gastric); both destabilize BAF complex when lost; mutations are mutually exclusive — single-subunit LOF suffices for SWI/SNF inactivation."
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "Germline SMARCB1 LOF + somatic NF2 loss → schwannomatosis (multiple schwannomas without vestibular schwannoma); NF2 (merlin) suppresses Hippo/YAP; SMARCB1 and NF2 both restrict YAP/TAZ; SMARCB1 missense predominates in schwannomatosis vs truncating variants in AT/RT."
---

# SMARCB1

## Overview

**SMARCB1** (SWI/SNF-related, matrix-associated, actin-dependent regulator of chromatin, subfamily B, member 1) — also called **INI1** (integrase interactor 1), **BAF47**, or **SNF5** — is a core, non-catalytic subunit of the **SWI/SNF (BAF/PBAF)** chromatin remodeling complexes. SMARCB1 is an obligate tumor suppressor: biallelic inactivation is the defining molecular lesion in the rhabdoid tumor family and epithelioid sarcoma, and is among the most potent and consistent tumor suppressor losses in human oncology [^versteege-1998-smarcb1-rhabdoid].

**SMARCB1-deficient tumors:**
- **Atypical teratoid/rhabdoid tumor (AT/RT)**: CNS, WHO grade 4; ~95% SMARCB1 LOF; infants and young children
- **Malignant rhabdoid tumor of the kidney (MRT/RTK)**: ~95% SMARCB1 LOF; mean age ~18 months; often extra-renal rhabdoid tumors (ERTO) at soft tissue sites
- **Epithelioid sarcoma** (proximal and distal types): ~95% SMARCB1 loss by IHC/FISH; proximal type (trunk/mediastinum, adults) is more aggressive; EZH2 inhibitor tazemetostat FDA-approved 2020 [^gounder-2020-tazemetostat-epithelioid]
- **SMARCB1-deficient sinonasal carcinoma**: undifferentiated nasopharyngeal-type carcinoma with INI1 loss
- **Cribriform neuroepithelial tumor (CRINET)**: rare intracranial tumor with SMARCB1 loss, RELA alteration
- **Schwannomatosis (germline)**: heterozygous SMARCB1 germline + somatic NF2 loss → multiple schwannomas without VS; distinct from NF2
- **Rare epithelioid/dedifferentiated neoplasms**: epithelioid malignant peripheral nerve sheath tumor (eMPNST); myoepithelial carcinoma

**Germline SMARCB1:**
Rhabdoid tumor predisposition syndrome type 1 (RTPS1): heterozygous germline SMARCB1 mutations (deletion, truncating); familial rhabdoid tumor risk; synchronous or metachronous AT/RT + MRT in infants; penetrance high but not complete; Knudson two-hit model confirmed; genetic counseling + surveillance MRI from birth in affected families.

## Structure

### SMARCB1 protein architecture

SMARCB1 is a 385-amino-acid nuclear protein organized into three functional domains:

**Repeat domain (RPT1-RPT2, aa 1-183):**
Two tandem repeat units (each ~50 aa), structurally resembling Myb/SANT domains; RPT1 mediates direct DNA binding to AT-rich sequences; RPT2 mediates interaction with the SWI/SNF catalytic subunit SMARCA4 (BRG1) and SMARCA2 (BRM); RPT truncations account for ~40% of rhabdoid tumor mutations (frameshift/nonsense in exons 1-5).

**Coiled-coil / linker region (aa 183-270):**
Flexible; mediates SMARCB1 homodimerization; forms the BAF complex scaffold; interacts with BAF60 (SMARCD1/2/3) subunits.

**C-terminal domain (aa 270-385):**
α-helical; mediates interaction with ARID1A/ARID1B (SMARCB1 anchors within cBAF vs ncBAF complexes); MH (Mad-Homology)-like domain for nuclear localization.

**Key functional surfaces:**
- RPT1 acidic patch contact → nucleosome engagement
- BRG1 ATPase interaction → translocase stimulation
- SMARCB1 directly contacts the nucleosome acidic patch (H2A/H2B), competing with PRC2 for nucleosome access → mechanistic basis of SMARCB1-PRC2 antagonism

**SMARCB1 in BAF complex variants:**
- **cBAF (canonical BAF)**: SMARCA4 or SMARCA2 + SMARCB1 + ARID1A/ARID1B + BRD7/BRD9 + additional subunits; activates transcription
- **PBAF**: SMARCA4 + SMARCB1 + ARID2 + PBRM1 + PHF10 + BRD7; poised/enhancer-associated
- **ncBAF**: SMARCA4 + BICRA/BRD9 — SMARCB1 absent in ncBAF; explains selective dependency on SMARCB1

### SWI/SNF-PRC2 antagonism

The most critical mechanism of SMARCB1 tumor suppression:
- SWI/SNF occupies H3K27me3-marked loci and uses ATPase-driven nucleosome remodeling to open chromatin → PRC2 evicted → H3K27me3 removed (by KDM6A/KDM6B)
- SMARCB1 LOF → entire BAF complex destabilized (SMARCB1 is required for BAF complex stability) → PRC2/EZH2 gains access to enhancers and gene bodies → H3K27me3 spreads → silences CDKN2A (p16+ARF), HOX genes, differentiation TFs, and lineage-specific enhancers
- This creates a profound **EZH2 dependency** in SMARCB1-null cells: growth depends on sustained PRC2 activity → EZH2 inhibitors restore SMARCB1-like PRC2 suppression

## Function

### Normal SMARCB1 roles

**Differentiation and development:**
SMARCB1 is required for differentiation of multiple lineages: muscle (MYOD1 target gene activation), neural (neural crest differentiation), and hematopoietic; SMARCB1 knockout mice die at embryonic day 3.5 (ICM failure) — underscoring its essentiality; heterozygous mice develop rhabdoid tumors spontaneously (~30% penetrance).

**Enhancer activation:**
BAF complex containing SMARCB1 is recruited to super-enhancers during cell differentiation → evicts nucleosomes → creates DNase I-hypersensitive accessible chromatin → RNA Pol II binding and elongation; lineage-specific enhancers of key TFs (MYOD1, PAX, RUNX) require SMARCB1 for activation.

**Cell cycle control via CDKN2A:**
SMARCB1 directly activates the CDKN2A promoter → p16/INK4A and p14/ARF → enforces G1 checkpoint and OIS barrier; SMARCB1 reintroduction into rhabdoid cells → p16 and ARF ↑ → RB1 hypophosphorylation → cell cycle arrest within 24-48 h (faster than transcriptional turnover time, suggesting direct chromatin remodeling at CDKN2A).

**Interaction with chromatin modifiers:**
- SMARCB1 interacts with HDAC3/NCoR → couples chromatin remodeling with deacetylation at repressed targets
- Competes with H1 for linker DNA binding → controls chromatin compaction at SMARCB1 target loci

## Mechanism

### EZH2 inhibitors (tazemetostat)

**Mechanism:**
Tazemetostat (EPZ-6438) is an orally bioavailable, selective EZH2 inhibitor; competitive inhibitor of S-adenosylmethionine (SAM) at EZH2 SET domain → prevents H3K27 methylation → H3K27me3 ↓ at PRC2-target loci → transcriptional de-repression → differentiation-associated gene activation.

**SMARCB1-null specificity:**
In normal cells, BAF limits PRC2 → tazemetostat has minimal antiproliferative effect; in SMARCB1-null cells, PRC2/EZH2 is the dominant transcriptional repressor → tazemetostat removes the only repressive force → growth arrest and differentiation; INI1-negative tumors are ~10-100x more sensitive to EZH2 inhibitors than INI1-intact tumors.

**Clinical data (Gounder 2020, E7438-014):** [^gounder-2020-tazemetostat-epithelioid]
N=62 patients with SMARCB1-deficient epithelioid sarcoma; tazemetostat 800 mg BID; ORR 15% (9/62; 1 CR, 8 PR); median DOR 5.7 months; clinical benefit rate (CR+PR+SD) 26%; FDA approval January 2020 for metastatic or locally advanced epithelioid sarcoma not eligible for curative surgery; first FDA-approved EZH2 inhibitor.

**Tazemetostat in follicular lymphoma:**
Also FDA-approved for EZH2-mutant follicular lymphoma (GOF EZH2 mutations at Y646) → demonstrates utility both in EZH2 LOF-context (SMARCB1 null → EZH2 dependency) and EZH2 GOF-context (activating mutations in FL).

### BET inhibitors (JQ1, birabresib)

**Mechanism in SMARCB1-null tumors:**
SMARCB1 loss → BRD4-occupied super-enhancers at MYC, GLI1, and other oncogenes → MYC-driven transcription; BET inhibitors displace BRD4 from bromodomains → MYC transcription ↓ → proliferation arrest; preclinical AT/RT and rhabdoid tumor models show strong BET inhibitor sensitivity (~100-fold lower IC50 than SMARCB1-intact lines).

### Other therapeutic approaches

- **CDK4/6 inhibitors (palbociclib)**: SMARCB1-null → p16 silenced → CDK4/6 hyperactive → CDK4/6 inhibition restores G1 arrest; preclinical Phase 2 data modest in AT/RT
- **HDAC inhibitors (panobinostat, entinostat)**: restore chromatin acetylation at SMARCB1 targets; synergizes with EZH2 inhibitors in preclinical models
- **SMARCB1 reintroduction via viral vector**: proof-of-concept gene therapy; impractical currently but validates SMARCB1 as the key tumor suppressor

## Connections

- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — SMARCB1 BAF complex antagonizes PRC2/EZH2 at enhancers; SMARCB1 LOF → SWI/SNF absent → PRC2/EZH2 gains access → H3K27me3 spreads → silences tumor suppressors and differentiation loci; SMARCB1-null tumors are uniquely EZH2-dependent → tazemetostat sensitivity.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — SMARCB1 loss → SWI/SNF cannot maintain open chromatin at CDKN2A locus → p16/INK4A ↓ and p14/ARF ↓ → CDK4/6 hyperactivation → RB1 phosphorylation → E2F-driven proliferation; CDK4/6 inhibitors partially rescue G1 arrest in SMARCB1-null cells when RB1 intact.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — SMARCB1 loss → SWI/SNF cannot activate CDKN2A promoter → p16/INK4A and p14/ARF both silenced; CDKN2A re-expression upon SMARCB1 rescue drives G1 arrest in rhabdoid tumor cells; CDKN2A homozygous deletion occurs in ~15-25% AT/RT and further ablates this checkpoint.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — SMARCB1-containing BAF complex occupies MYC-target gene enhancers to limit MYC-driven transcription; SMARCB1 loss → BRD4-dependent super-enhancer activity at MYC → MYC target gene hyperactivation; BET inhibitors (JQ1) suppress MYC in SMARCB1-null rhabdoid and AT/RT cells.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — SMARCB1 loss → p14/ARF silenced → MDM2 unchecked → p53 degraded despite intact TP53; TP53 mutations uncommon in AT/RT; doxorubicin/vinca chemotherapy depends on residual p53-mediated apoptosis; SMARCB1 rescue restores p14/ARF → p53 re-activation and G1 arrest.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — SMARCB1 and ARID1A are SWI/SNF tumor suppressor subunits with distinct tumor spectra (SMARCB1: rhabdoid/AT/RT; ARID1A: endometrial/ovarian/gastric); both destabilize BAF complex when lost; mutations are mutually exclusive — single-subunit LOF suffices for SWI/SNF inactivation.
- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — Germline SMARCB1 LOF + somatic NF2 loss → schwannomatosis (multiple schwannomas without vestibular schwannoma); NF2 (merlin) suppresses Hippo/YAP; SMARCB1 and NF2 both restrict YAP/TAZ; SMARCB1 missense predominates in schwannomatosis vs truncating variants in AT/RT.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^versteege-1998-smarcb1-rhabdoid]: Versteege I, Sévenet N, Lange J, et al. Truncating mutations of hSNF5/INI1 in aggressive paediatric cancer. *Nature.* 1998;394(6689):203-206. [doi:10.1038/28212](https://doi.org/10.1038/28212) · [PubMed 9671307](https://pubmed.ncbi.nlm.nih.gov/9671307/)
[^gounder-2020-tazemetostat-epithelioid]: Gounder M, Schöffski P, Jones RL, et al. Tazemetostat in advanced epithelioid sarcoma with loss of INI1/SMARCB1: an international, open-label, phase 2 basket study. *Lancet Oncol.* 2020;21(11):1423-1432. [doi:10.1016/S1470-2045(20)30451-4](https://doi.org/10.1016/S1470-2045(20)30451-4) · [PubMed 33007258](https://pubmed.ncbi.nlm.nih.gov/33007258/)
