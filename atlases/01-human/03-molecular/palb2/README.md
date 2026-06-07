---
schema: human-scale-entry/v1
id: palb2
name: PALB2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "PALB2 bridges BRCA1 (coiled-coil N-terminus) to BRCA2 (WD40 C-terminus) at DSBs to enable RAD51-mediated homologous recombination; germline PALB2 = high-risk HBOC (~35-65% breast cancer); biallelic PALB2 = Fanconi anemia FA-N; HRD → PARP inhibitor sensitivity."
aliases: ["PALB2", "Partner and Localizer of BRCA2", "FANCN", "Fanconi PALB2", "PALB2 BRCA1 BRCA2", "PALB2 breast cancer", "PALB2 WD40", "PALB2 HR", "PALB2 HBOC"]
sources:
  - id: xia-2006-palb2
    type: peer-reviewed
    cite: "Xia B, Sheng Q, Nakanishi K, et al. Control of BRCA2 cellular and clinical functions by a nuclear partner, PALB2. Mol Cell. 2006;22(6):719-729."
    doi: "10.1016/j.molcel.2006.05.022"
    pmid: "16793542"
    url: "https://doi.org/10.1016/j.molcel.2006.05.022"
  - id: antoniou-2014-palb2-risk
    type: peer-reviewed
    cite: "Antoniou AC, Casadei S, Heikkinen T, et al. Breast-cancer risk in families with mutations in PALB2. N Engl J Med. 2014;371(6):497-506."
    doi: "10.1056/NEJMoa1400382"
    pmid: "25099575"
    url: "https://doi.org/10.1056/NEJMoa1400382"
cross_links:
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "PALB2 N-terminal coiled-coil domain binds BRCA1 BRCT repeats at DSBs; BRCA1 recruits PALB2 after end resection; PALB2 bridges BRCA1 (end resection) to BRCA2 (RAD51 loading); BRCA1 and PALB2 germline mutations both cause HBOC with distinct cancer spectra."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "PALB2 C-terminal WD40 domain binds BRCA2 N-terminus, enabling BRCA2 nuclear localization at DSBs; BRCA2 loads RAD51 onto resected ssDNA to initiate strand invasion; PALB2 and BRCA2 germline variants both cause HBOC and elevated pancreatic cancer risk."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "PALB2 positions the BRCA2-RAD51 presynaptic filament at resected DSB ends; RAD51 nucleoprotein filament catalyzes strand invasion into homologous duplex → template-directed repair; PALB2 loss → HR deficiency → sensitivity to PARP inhibitors and platinum agents."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "Germline PALB2 pathogenic variants confer ~35-65% lifetime breast cancer risk (second after BRCA1/2); ~5-10% ovarian cancer risk (primarily HGSOC); biallelic PALB2 = Fanconi anemia FA-N; PARP inhibitors are active in PALB2-germline breast and pancreatic cancer."
---

# PALB2

## Overview

**PALB2** (Partner and Localizer of BRCA2; also FANCN — Fanconi Anemia Complementation Group N) encodes a 1,186 amino acid (131 kDa) nuclear protein that functions as a **molecular scaffold bridging BRCA1 and BRCA2** at DNA double-strand break (DSB) repair sites. PALB2 was identified as a BRCA2 interacting partner (Xia 2006) that is essential for BRCA2 nuclear accumulation and chromatin association after DNA damage. Germline pathogenic PALB2 variants cause **hereditary breast and ovarian cancer syndrome (HBOC)**, conferring ~35-65% lifetime breast cancer risk (the third highest after BRCA1 and BRCA2 among currently actionable genes). Biallelic PALB2 inactivation causes **Fanconi anemia subtype FA-N**, a rare recessive disorder with bone marrow failure and early-onset solid tumors [^xia-2006-palb2] [^antoniou-2014-palb2-risk].

**PALB2 germline cancer risk profile:**

| Cancer type | PALB2 germline lifetime risk | Notes |
|---|---|---|
| Breast cancer (female) | ~35-65% | 3rd highest after BRCA1/2; ER+ and TNBC |
| Ovarian cancer | ~5-10% | Primarily HGSOC subtype |
| Pancreatic cancer | ~2-3% | Similar to BRCA2 germline elevation |
| Male breast cancer | ~5-10% | Elevated, less characterized |
| Prostate cancer | Modest elevation | <2-fold; not actionable alone |

## Structure

### PALB2 protein domains

**N-terminal coiled-coil domain (aa 1-100):**
- Mediates BRCA1 interaction: PALB2 coiled-coil binds BRCA1 BRCT repeats (Trp1184-Trp1145 contact interface)
- BRCA1-PALB2 interaction is required to recruit PALB2 (and hence BRCA2-RAD51) to DSB foci after RPA-coated ssDNA appears post-end-resection
- Pathogenic germline variants: truncating variants near N-terminus (c.229T>C, c.509T>G; founder variants in Finnish population) disrupt coiled-coil and BRCA1 interaction
- Self-oligomerization: coiled-coil also mediates PALB2 homo-oligomerization (tetramer) → increases avidity for BRCA1 at DSBs

**Central domain (aa 101-853):**
- Chromatin-associated region; contains short chromatin association motif (ChAM, aa 395-445) — binds nucleosomes directly; required for stable PALB2 retention at damaged chromatin after laser microirradiation
- Nuclear localization signal: embedded in central domain; PALB2 is constitutively nuclear (unlike BRCA2 which requires PALB2 for nuclear localization after damage)
- Contains NLS-1 and NLS-2 elements

**C-terminal WD40 beta-propeller domain (aa 853-1186):**
- Seven-bladed β-propeller; structurally analogous to WD40 domains in chromatin-remodeling proteins
- Directly binds **BRCA2 N-terminus** (first 40 aa of BRCA2; non-BRC repeat region)
- Crystal structure of PALB2 WD40 — BRCA2 N-terminus complex solved at 2.0 Å (Oliver 2009); reveals a groove on the WD40 surface accommodating BRCA2 Leu-Pro motif
- WD40 domain also interacts with RAD51 (independent of BRCA2) and with KEAP1 (NRF2 regulation context)
- Pathogenic missense variants in WD40: Ala1025Glu, Leu939Trp (disrupt WD40-BRCA2 interaction) — functionally validated

**The BRCA1-PALB2-BRCA2-RAD51 (BPBR) complex:**
```
DSB occurs
   ↓
ATM/RPA signals → BRCA1 recruited (via ubiquitin-BARD1, RIF1, 53BP1 cleared)
   ↓
BRCA1 coiled-coil → binds PALB2 coiled-coil → PALB2 anchored at DSB
   ↓
PALB2 WD40 → binds BRCA2 N-terminus → BRCA2 brought to resected ssDNA
   ↓
BRCA2 BRC repeats → displace RPA from ssDNA → load RAD51 monomers
   ↓
RAD51 nucleoprotein filament (presynaptic) → strand invasion into sister chromatid
   ↓
Homologous recombination repair (HDR) — template-directed, error-free
```

## Function

### Homologous recombination repair (HR)

PALB2 functions at the S/G2 phase-restricted HR repair step (after end resection by CtIP/MRN, RPA loading, and ssDNA formation):

1. **BRCA2 localization**: PALB2 nuclear chromatin association (via ChAM + BRCA1 recruitment) provides a platform for BRCA2 to accumulate at DSBs; without PALB2, BRCA2 fails to localize to DSB foci even though BRCA2 protein is present and stable
2. **RAD51 filament assembly**: BRCA2 (brought by PALB2) displaces RPA from ssDNA → loads RAD51 monomers in ATPase-competent orientation; PALB2 itself interacts with RAD51 directly (WD40 and central domain contacts) to stabilize the presynaptic filament
3. **Strand invasion**: RAD51 filament catalyzes invasion of homologous duplex DNA (sister chromatid in S/G2) → D-loop → DNA synthesis by Pol δ → Holliday junction → branch migration → ligation → complete DSB repair without error

### Fanconi anemia FA-N

Biallelic PALB2 inactivation (compound heterozygous or homozygous truncating pathogenic variants) causes **FA-N**, one of 23+ FA complementation groups. FA is characterized by:
- Bone marrow failure (aplastic anemia, pancytopenia): defective ICL (interstrand crosslink) repair → hematopoietic stem cell exhaustion
- AML and MDS: clonal evolution from failing marrow
- Solid tumors: Wilms tumor, medulloblastoma, HNSCC in childhood (second decade)
- Hypersensitivity to bifunctional alkylating agents (mitomycin C, cisplatin, cyclophosphamide): diagnostic test (chromosome fragility test with MMC)
- FA-N is rare; PALB2 biallelic mutations in FA patients identified by Reid 2007

PALB2 role in Fanconi anemia pathway: PALB2 functions downstream of the FA core complex (FANCA-FANCM-FANCD2-I monoubiquitination) in ICL repair; the ICL repair pathway uses HR at the final step of error-free repair, where PALB2-BRCA2-RAD51 are essential.

### PALB2 and replication fork protection

Beyond DSB repair, PALB2-BRCA1-BRCA2 protect stalled replication forks from nucleolytic degradation by MRE11 nuclease. When forks stall (e.g., at ICLs, under replication stress), PALB2 maintains fork integrity; PALB2 loss → fork degradation → genomic instability under replication stress.

## Mechanism

### PALB2 pathogenic variants and clinical categorization

- **Truncating (frameshift, nonsense, splice)**: ~75-80% of clinically actionable PALB2 germline variants; all considered high-penetrance; protein absent or nonfunctional; treated similarly to BRCA1/2 truncating for clinical management
- **Missense**: difficult to classify; WD40 domain missense (Ala1025Glu, Leu939Trp) functionally validated as pathogenic; majority of PALB2 missense variants are VUS; functional HR assays used for classification
- **Founder variants**: c.1592delT (Finnish founder); c.3113G>A (UK, BRCA Exchange); different populations have different founders
- **Large deletions**: rare; MLPA required

**Penetrance nuance (Antoniou 2014 NEJM):**
- Breast cancer risk is family-history-dependent: PALB2 PV carriers with two or more relatives with breast cancer have ~58-65% lifetime risk; carriers without family history have ~35% risk
- Younger age of onset: PALB2-associated breast cancer peaks at age 30-40 (younger than BRCA2, similar to BRCA1)
- Histology: ER-positive (~40-50%) and triple-negative (~25-30%); HER2-enriched rare; unlike BRCA1 (predominantly TNBC)

### PARP inhibitor sensitivity

PALB2 LOF → HR deficiency (HRD) → cells dependent on PARP1-mediated single-strand break repair and BER for survival → PARP inhibitor (olaparib, niraparib, rucaparib, talazoparib) causes replication fork collapse → lethal synthetic lethality. PALB2-germline tumors:
- Breast cancer: olaparib (OlympiAD, BRCA1/2 also; PALB2 included in label as "germline BRCA1/2 or other HRR-mutant"); talazoparib (EMBRACA trial); niraparib (BRAVO); all FDA-approved for HER2-negative germline HRR-mutant metastatic breast cancer
- Pancreatic cancer: olaparib maintenance (POLO trial: BRCA1/2 germline; PALB2 explored in exploratory cohort)
- Ovarian cancer: olaparib, niraparib, rucaparib approved for HRR-mutant or HRD-positive HGSOC

### HRD assays

Tumor-level genomic HRD assays (Myriad myChoice, FoundationOne CDx HRD) detect: loss of heterozygosity (LOH), telomeric allelic imbalance (TAI), and large-scale state transitions (LST) → HRD score ≥42 (Myriad) or positive HRD (Foundation) = HRD-positive. PALB2-mutant tumors often have high HRD scores and HRD-positive assays, predicting PARP inhibitor and platinum sensitivity even in sporadic-appearing tumors with somatic PALB2 biallelic loss.

## Connections

- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — PALB2 N-terminal coiled-coil domain binds BRCA1 BRCT repeats at DSBs; BRCA1 recruits PALB2 after end resection; PALB2 bridges BRCA1 (end resection) to BRCA2 (RAD51 loading); BRCA1 and PALB2 germline mutations both cause HBOC with distinct cancer spectra.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — PALB2 C-terminal WD40 domain binds BRCA2 N-terminus, enabling BRCA2 nuclear localization at DSBs; BRCA2 loads RAD51 onto resected ssDNA to initiate strand invasion; PALB2 and BRCA2 germline variants both cause HBOC and elevated pancreatic cancer risk.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — PALB2 positions the BRCA2-RAD51 presynaptic filament at resected DSB ends; RAD51 nucleoprotein filament catalyzes strand invasion into homologous duplex → template-directed repair; PALB2 loss → HR deficiency → sensitivity to PARP inhibitors and platinum agents.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../../07-system/hereditary-breast-ovarian-cancer/README.md)** — Germline PALB2 pathogenic variants confer ~35-65% lifetime breast cancer risk (second after BRCA1/2); ~5-10% ovarian cancer risk (primarily HGSOC); biallelic PALB2 = Fanconi anemia FA-N; PARP inhibitors are active in PALB2-germline breast and pancreatic cancer.

[^xia-2006-palb2]: Xia B, Sheng Q, Nakanishi K, et al. Control of BRCA2 cellular and clinical functions by a nuclear partner, PALB2. *Mol Cell.* 2006;22(6):719-729. [doi:10.1016/j.molcel.2006.05.022](https://doi.org/10.1016/j.molcel.2006.05.022) · [PubMed 16793542](https://pubmed.ncbi.nlm.nih.gov/16793542/)
[^antoniou-2014-palb2-risk]: Antoniou AC, Casadei S, Heikkinen T, et al. Breast-cancer risk in families with mutations in PALB2. *N Engl J Med.* 2014;371(6):497-506. [doi:10.1056/NEJMoa1400382](https://doi.org/10.1056/NEJMoa1400382) · [PubMed 25099575](https://pubmed.ncbi.nlm.nih.gov/25099575/)
