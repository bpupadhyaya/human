---
schema: human-scale-entry/v1
id: brca1
name: BRCA1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Tumor suppressor with RING-BRCT architecture; BARD1 heterodimer confers E3 ubiquitin ligase activity for homologous recombination (HR). Germline mutations: 70% lifetime breast and 40% ovarian cancer risk. Loss creates PARP inhibitor (olaparib) synthetic lethality."
aliases: ["BRCA1 protein", "breast cancer type 1 susceptibility", "BRCAI", "BRCA-1"]
sources:
  - id: miki-1994-brca1
    type: peer-reviewed
    cite: "Miki Y, Swensen J, Shattuck-Eidens D, et al. A strong candidate for the breast and ovarian cancer susceptibility gene BRCA1. Science. 1994;266(5182):66-71."
    doi: "10.1126/science.7545954"
    pmid: "7545954"
    url: "https://doi.org/10.1126/science.7545954"
  - id: roy-2012-brca-repair
    type: peer-reviewed
    cite: "Roy R, Chun J, Powell SN. BRCA1 and BRCA2: different roles in a common pathway of genome protection. Nat Rev Cancer. 2012;12(1):68-78."
    doi: "10.1038/nrc3181"
    pmid: "22193408"
    url: "https://doi.org/10.1038/nrc3181"
  - id: robson-2017-olaparib-breast
    type: peer-reviewed
    cite: "Robson M, Im SA, Senkus E, et al. Olaparib for Metastatic Breast Cancer in Patients with a Germline BRCA Mutation. N Engl J Med. 2017;377(6):523-533."
    doi: "10.1056/NEJMoa1706450"
    pmid: "28578601"
    url: "https://doi.org/10.1056/NEJMoa1706450"
cross_links:
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "BRCA1 BRCT domain binds phosphorylated p53 (Ser15) after DNA damage; BRCA1 stabilizes p53 and co-activates p21 and PUMA transcription; both are guardians of genome integrity — co-loss of BRCA1 and p53 drives highly aggressive triple-negative breast cancer."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "BRCA1 coactivates NF-κB-dependent gene expression in response to DNA damage; conversely, BRCA1 loss leads to constitutive NF-κB activation and inflammatory cytokine secretion → pro-tumorigenic microenvironment in BRCA1-mutant breast and ovarian cancers."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BRCA1 overexpression shifts BCL-2/BAX balance toward apoptosis; BRCA1-deficient tumors often acquire BCL-2 overexpression as a compensatory survival mechanism, reducing sensitivity to genotoxic chemotherapy and immune-mediated killing — a co-occurring resistance pathway."
---

# BRCA1

## Overview

**BRCA1 (breast cancer type 1 susceptibility protein)** is a **nuclear tumor suppressor** and scaffolding protein that coordinates the cellular response to DNA double-strand breaks (DSBs). Cloned by Miki, King, and colleagues in 1994 after two decades of genetic linkage studies in hereditary breast cancer families [^miki-1994-brca1], BRCA1 was the first high-penetrance breast cancer susceptibility gene identified — establishing that hereditary breast cancer arises from impaired genome maintenance, not just accelerated proliferation.

BRCA1 functions at the intersection of **DNA repair, cell cycle checkpoint control, transcriptional regulation, and chromatin remodeling**:
- **Homologous recombination (HR):** The primary DNA repair pathway for high-fidelity DSB repair; BRCA1 is essential for HR at replication forks and in S/G2 phase
- **G2/M checkpoint:** BRCA1 phosphorylation by ATM/ATR → CHK1/CHK2 activation → CDC25C inhibition → CDK1 inactivation → arrest before mitotic entry with damaged DNA
- **Transcription-coupled repair (TCR):** BRCA1 facilitates repair of DNA lesions in actively transcribed genes via RNA Pol II interaction

**Germline BRCA1 mutations** (heterozygous) confer markedly elevated cancer risk:
- Breast cancer: ~70% lifetime risk (vs. ~12% general population)
- Ovarian cancer: ~40% lifetime risk (vs. ~1.3% general population)
- Also elevated risk of fallopian tube and primary peritoneal cancer
- BRCA1-associated breast cancers: predominantly **ER-negative, PR-negative, HER2-negative (triple-negative)** with high grade and poor prognosis (due to estrogen receptor suppression by BRCA1 and defective DNA repair)

Therapeutically, BRCA1 loss creates **synthetic lethality** with **PARP inhibition**: cancer cells lacking BRCA1-mediated HR depend on PARP1/2 for single-strand break repair; blocking PARP1/2 (with olaparib, niraparib, rucaparib, talazoparib) → unrepaired SSBs → DSBs at replication forks → catastrophic genomic instability → cell death selectively in BRCA1-deficient tumor cells [^robson-2017-olaparib-breast].

## Structure

### BRCA1 protein architecture

BRCA1 is a **1,863 amino acid, ~220 kDa nuclear protein** with three principal structural modules:

**RING domain (aa 1-109):**
- RING (Really Interesting New Gene) zinc-finger fold; binds two Zn²⁺ ions
- Forms obligate heterodimer with **BARD1 (BRCA1-associated RING domain protein)** → BRCA1:BARD1 heterodimer has **E3 ubiquitin ligase activity** (mono-ubiquitinates H2A-Lys119 at DSB sites → DNA repair signaling; ubiquitinates unknown substrates for DDR propagation)
- RING mutation (e.g., C61G, C64G) abolishes BARD1 interaction and E3 activity → pathogenic
- BARD1 interaction also stabilizes BRCA1 protein against proteasomal degradation

**Central domain (aa 110-1645):**
- Contains **serine-rich BASC (BRCA1-associated genome surveillance complex)** interaction regions
- Multiple ATM/ATR phosphorylation sites (Ser1387, Ser1423, Ser1524, Ser1387) — required for checkpoint signaling
- **Nuclear localization signals (NLS)** within this region
- PALB2 interaction domain (aa 1395-1424): PALB2 bridges BRCA1 to BRCA2, which recruits RAD51 for strand invasion during HR

**BRCT domains (aa 1646-1863):**
- Two tandem BRCT (BRCA1 C-terminal) repeats; conserved phosphopeptide-binding module
- Bind phosphorylated SQ/TQ motifs in DDR proteins:
  - **BACH1/FANCJ:** Helicase that processes DSB ends for HR
  - **CtIP (RBBP8):** Nuclease that initiates 5'→3' resection at DSBs → creates 3' overhangs for RPA→RAD51 loading
  - **Abraxas/BRCC36:** Forms BRCA1-A complex (with RAP80, MERIT40) that localizes BRCA1 to ubiquitin chains at DSB sites (via H2A-Lys63-Ub)
  - **Phospho-p53 (Ser15):** BRCA1 co-activates p53-dependent transcription of DNA damage response genes
- BRCT mutations abolish phosphopeptide binding → pathogenic (e.g., S1655F, M1775R, W1837R)

### BRCA1 complex assembly at DSBs [^roy-2012-brca-repair]

BRCA1 forms distinct complexes for different repair functions:
1. **BRCA1-A complex (Abraxas/RAP80/MERIT40/BRCC36/UBR5):** Recruited by RNF8/RNF168-generated Lys63-polyubiquitin chains on H2A → retains BRCA1 at DSBs; promotes HR over NHEJ
2. **BRCA1-B complex (BACH1/FANCJ/TopBP1):** Involved in S-phase checkpoint and fork restart; mutations in BACH1 cause Fanconi anemia-like phenotype
3. **BRCA1-C complex (CtIP/MRN complex):** Initiates end resection → 3' ssDNA → RPA binding → ATR activation → checkpoint

## Function

### Homologous recombination: the core function

**HR pathway steps:**
1. DSB formation → MRN complex (MRE11-RAD50-NBS1) senses DSB ends → recruits ATM kinase → ATM autophosphorylation (Ser1981) → γH2AX formation (labels break site)
2. **Resection:** CtIP (BRCA1-C complex) initiates 5'→3' nucleolytic resection → ssDNA overhangs; EXOI and BLM extend resection → ~1-2 kb ssDNA tails
3. **RPA loading:** RPA (replication protein A) coats ssDNA → activates ATR–ATRIP → CHK1 phosphorylation → S-phase checkpoint
4. **BRCA2 and RAD51:** PALB2 (bridged to BRCA1) recruits BRCA2 → BRCA2 displaces RPA → loads RAD51 onto ssDNA → RAD51 nucleoprotein filament
5. **Strand invasion:** RAD51 filament invades homologous dsDNA → D-loop → DNA synthesis → ligation → error-free repair

**Why HR is critical for BRCA1-deficient tumorigenesis:**
- Without HR, DSBs are repaired by error-prone **NHEJ (non-homologous end joining)** → insertions/deletions → chromosomal rearrangements → genome instability → accumulation of oncogenic mutations
- BRCA1-deficient cells show characteristic **mutational signature 3 ("HRD signature")**: base substitutions at TpC, deletions flanked by microhomology, large-scale chromosomal rearrangements

### PARP inhibitor synthetic lethality [^robson-2017-olaparib-breast]

**Mechanism:**
- PARP1/2 repair **single-strand breaks (SSBs)** via base excision repair (BER); PARP traps itself at SSBs during catalysis
- **PARP inhibitors (olaparib, niraparib, rucaparib, talazoparib):** Catalytic inhibition + PARP trapping → unrepaired SSBs → stalled replication forks → DSBs at forks → if HR-deficient (BRCA1/2 mutant) → cell death
- Normal cells: can repair via HR → survive; BRCA1-mutant tumor cells: cannot repair → die (synthetic lethality)

**Olaparib (Lynparza, AstraZeneca/Merck) clinical approvals:**
- **Germline BRCA1/2 HER2-negative metastatic breast cancer** (OlympiAD trial, 2017): ORR 59.9% vs 28.8% (chemotherapy), PFS 7.0 vs 4.2 months
- **Germline BRCA1/2 ovarian cancer** (SOLO-2 trial, maintenance): 13.6 vs 5.4 months PFS
- **HRRm (HR repair mutation) metastatic castration-resistant prostate cancer** (PROfound trial, 2020): 7.4 vs 3.6 months PFS

**HRD (homologous recombination deficiency) beyond BRCA1/2:**
- Genomic instability score (GIS): large-scale transitions, loss of heterozygosity, telomeric allelic imbalance → predict PARP inhibitor sensitivity even in BRCA-wild-type tumors
- Other HR pathway genes: PALB2, RAD51C, RAD51D, BRIP1, ATM mutations → variable PARP inhibitor sensitivity

### BRCA1 and transcriptional regulation

BRCA1 interacts with the **RNA Pol II holoenzyme** (via CTD phosphorylation) and co-activates a broad transcriptional program:
- **Positive regulation:** p53 target genes (PUMA, p21), ESR1 (estrogen receptor α) suppression → explains ER-negative BRCA1 breast cancers; also activates BRCA2, RAD51, and repair genes
- **NF-κB interaction:** BRCA1 modulates NF-κB-dependent inflammatory gene expression; BRCA1 loss → constitutive NF-κB → inflammatory tumor microenvironment

## Mechanism

### BRCA1 in the cell cycle

BRCA1 phosphorylation status controls its function across the cell cycle:
- **S phase:** CDK2-dependent BRCA1 phosphorylation (Ser1497, Ser308) → localized to active replication factories; essential for fork protection
- **G2/M checkpoint:** ATM phosphorylates BRCA1 (Ser1387) after DSBs → BRCA1 activates CHK2 (Thr68) → CHK2 phosphorylates CDC25C (Ser216) → 14-3-3 binding → nuclear exclusion → CDC25C cannot dephosphorylate CDK1/cyclin B → G2 arrest
- **Mitosis:** CDK1 phosphorylates BRCA1 (Ser1497, others) → centrosome localization → spindle assembly checkpoint

### BRCA1 protein variants: pathogenicity classification

**Five-tier classification** (ENIGMA Consortium):
- Class 5 (pathogenic): Frameshift, nonsense, splice-site mutations that truncate protein → loss of BRCT or RING domain; ~1,800 known
- Class 4 (likely pathogenic): Missense mutations at critical residues (BRCT Trp1837, Met1775R); validated functional studies
- Class 3 (uncertain significance): ~10,000 VUS (variants of uncertain significance) — the clinical challenge; functional assays (saturation genome editing, MAVE) are being deployed to reclassify these
- Class 2 (likely benign): Common polymorphisms; functional impact negligible
- Class 1 (benign)

**Testing strategy:** Germline testing (blood DNA) via multigene panel for BRCA1, BRCA2, PALB2, CHEK2, ATM, CDH1 for individuals meeting NCCN criteria (family history, personal history of ovarian cancer or ≤50 years breast cancer, Ashkenazi Jewish ancestry, triple-negative breast cancer ≤60 years, male breast cancer).

## Connections

- `connects-to` → **[p53](../p53/README.md)** — BRCA1 BRCT domain binds phospho-p53 (Ser15) and co-activates p21 and PUMA transcription; BRCA1 and p53 are cooperative genome guardians — co-loss drives aggressive triple-negative breast cancer.
- `connects-to` → **[NF-κB](../nf-kb/README.md)** — BRCA1 modulates NF-κB-dependent inflammatory gene expression; BRCA1 loss → constitutive NF-κB → pro-tumorigenic microenvironment in BRCA1-mutant breast and ovarian cancers.
- `connects-to` → **[BCL-2](../bcl-2/README.md)** — BRCA1 overexpression shifts BCL-2/BAX ratio toward apoptosis; BRCA1-deficient tumor cells frequently acquire BCL-2 overexpression as a survival compensatory mechanism, reducing sensitivity to genotoxic therapy.

[^miki-1994-brca1]: Miki Y, Swensen J, Shattuck-Eidens D, et al. A strong candidate for the breast and ovarian cancer susceptibility gene BRCA1. *Science.* 1994;266(5182):66-71. [doi:10.1126/science.7545954](https://doi.org/10.1126/science.7545954) · [PubMed 7545954](https://pubmed.ncbi.nlm.nih.gov/7545954/)
[^roy-2012-brca-repair]: Roy R, Chun J, Powell SN. BRCA1 and BRCA2: different roles in a common pathway of genome protection. *Nat Rev Cancer.* 2012;12(1):68-78. [doi:10.1038/nrc3181](https://doi.org/10.1038/nrc3181) · [PubMed 22193408](https://pubmed.ncbi.nlm.nih.gov/22193408/)
[^robson-2017-olaparib-breast]: Robson M, Im SA, Senkus E, et al. Olaparib for Metastatic Breast Cancer in Patients with a Germline BRCA Mutation. *N Engl J Med.* 2017;377(6):523-533. [doi:10.1056/NEJMoa1706450](https://doi.org/10.1056/NEJMoa1706450) · [PubMed 28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/)
