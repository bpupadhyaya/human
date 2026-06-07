---
schema: human-scale-entry/v1
id: atm
name: ATM
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "ATM kinase senses DNA double-strand breaks → phosphorylates H2AX, CHK2, BRCA1, and p53 → cell cycle arrest and HR repair. Germline ATM mutations cause ataxia-telangiectasia; somatic ATM deletion in ~15% of CLL and ~40% of mantle cell lymphoma."
aliases: ["ATM", "Ataxia-Telangiectasia Mutated", "AT1", "ATM kinase", "DNA damage response", "double-strand break repair", "ataxia-telangiectasia"]
sources:
  - id: kastan-2010-atm-review
    type: peer-reviewed
    cite: "Kastan MB, Bartek J. Cell-cycle checkpoints and cancer. Nature. 2004;432(7015):316-323."
    doi: "10.1038/nature03097"
    pmid: "15549093"
    url: "https://doi.org/10.1038/nature03097"
  - id: young-2014-atm-cancer
    type: peer-reviewed
    cite: "Young LM, Bharat AG, Bhatt DL, et al. ATM mutations in CLL and its impact on treatment outcome. Leukemia. 2014;28(2):241-248."
    doi: "10.1038/leu.2013.298"
    pmid: "24166298"
    url: "https://doi.org/10.1038/leu.2013.298"
cross_links:
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "ATM phosphorylates p53 at Ser15 → MDM2 dissociation → p21/PUMA/BAX → G1 arrest or apoptosis; TP53 mutations and ATM deletion are distinct but converging DDR failure mechanisms in CLL; del17p/TP53-mutant CLL is the highest-risk subset."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "ATM phosphorylates BRCA1 at Ser1387/Ser1524 after DSB → HR repair activation; BRCA1 RING domain ubiquitinates H2A at damage foci; ATM-BRCA1 axis is a core HR step; ATM deficiency → partial HRD → PARP inhibitor synthetic lethality in ATM-mutant prostate and pancreatic cancer."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "ATM activates NF-κB via NEMO-ATM nuclear complex → IKK → IκB phosphorylation → NF-κB; ATM-NF-κB promotes survival in B-CLL; BCR-NF-κB and ATM-NF-κB are co-activated in CLL; ibrutinib (BTK inhibitor) blocks BCR-NF-κB and attenuates ATM-dependent survival."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "ATM-p53 axis activates PUMA and BAX → mitochondrial apoptosis; BCL-2 overexpression in CLL neutralizes ATM-driven apoptosis; ATM-deleted CLL has impaired DNA-damage-induced apoptosis → venetoclax active regardless of ATM status; BCL-2 dependency is independent of ATM/p53 DDR."
---

# ATM

## Overview

**ATM (Ataxia-Telangiectasia Mutated)** is a 3,056-amino-acid serine/threonine kinase of the PIKK (PI3K-related kinase) family that serves as the principal sensor and signal transducer of **DNA double-strand breaks (DSBs)**. Recruited by the MRN (MRE11-RAD50-NBS1) complex to DSB ends, ATM autophosphorylates at Ser1981, activates, and phosphorylates hundreds of downstream substrates including H2AX (→γH2AX), CHK2, BRCA1, p53, and FANCD2 — coordinating cell cycle arrest, DNA repair (homologous recombination), and apoptosis. Loss of ATM causes **ataxia-telangiectasia (AT)**, a rare autosomal-recessive syndrome of cerebellar degeneration, immunodeficiency, radiosensitivity, and markedly elevated cancer risk [^kastan-2010-atm-review].

**ATM in cancer:**
- **Ataxia-telangiectasia (germline biallelic):** Cerebellar ataxia, oculocutaneous telangiectasias, combined immunodeficiency (reduced IgA, IgG2), 100× increased cancer risk (predominantly lymphoid; B-cell lymphoma, T-cell leukemia); extreme radiosensitivity (no radiation therapy) — autosomal recessive, incidence ~1:40,000-100,000
- **CLL del(11q22.3)/ATM deletion (~15-20% of CLL):** Usually monoallelic; combined with TP53 deletion (del17p) → highest-risk CLL; ATM loss → reduced apoptosis after DNA damage; ibrutinib active regardless of ATM status; venetoclax also active
- **Mantle cell lymphoma (MCL):** ATM biallelic inactivation in ~40-50% of MCL; ATM mutation is a defining feature of MCL (MCL-specific mutagenesis)
- **Prostate cancer:** ATM mutations in ~7% of metastatic castration-resistant prostate cancer; PARP inhibitor (olaparib, PROfound trial) active in ATM-mutant MCRPC alongside BRCA2/BRCA1 mutations — though ATM benefit is more modest than BRCA2

**ATM vs. ATR:**
- ATM: Responds to DSBs (ionizing radiation, chemotherapy); activates CHK2
- ATR: Responds to single-stranded DNA/replication stress (UV, hydroxyurea, replication fork stalling); activates CHK1
- Both converge on RPA, BRCA1, and p53 activation; synthetic lethality approaches target both kinases

## Structure

### ATM protein architecture

ATM is a 370 kDa, 3,056-aa PIKK superfamily kinase with a complex modular architecture:

**N-terminal HEAT repeats (1-1960):**
- 36 HEAT repeat pairs → solenoid scaffold for protein-protein interactions
- Recruits MRN complex after DSB formation; also scaffolds BRCA1, CHK2, and p53
- NLS within HEAT domain mediates nuclear import

**FAT domain (Focal adhesion kinase target-like, 1960-2566):**
- PIKK-specific structural module; stabilizes kinase domain fold
- Autophosphorylation at Ser1981 (within FAT domain) → monomer-to-dimer activation

**Kinase domain (PI3K-like, 2712-2962):**
- PIKK family catalytic domain; DFG motif present; phosphorylates Ser/Thr-Q consensus motifs (SQ/TQ)
- Key substrates: H2AX Ser139 (→γH2AX), CHK2 Thr68, BRCA1 Ser1387/Ser1524, p53 Ser15, NBS1 Ser343, MDM2 Ser395
- Wortmannin and KU-55933 are ATM inhibitors (used experimentally)

**FATC domain (2963-3056):**
- C-terminal domain; required for kinase activity; interacts with TIP60 (KAT5) histone acetyltransferase → ATM activation step (TIP60 acetylates ATM-Lys3016 → autophosphorylation and activation)

### DSB detection and ATM activation

**Step-by-step DSB response:**
1. **DSB formation** → MRE11-RAD50-NBS1 (MRN) complex binds DSB ends within seconds
2. **ATM recruitment:** NBS1 C-terminus directly binds ATM → ATM localized to break
3. **TIP60 activation:** TIP60 (lysine acetyltransferase) acetylates ATM-Lys3016 → ATM autophosphorylation at Ser1981 → dimer dissociates → active monomer
4. **γH2AX spreading:** ATM phosphorylates H2AX at Ser139 → γH2AX mark spreads megabases from DSB via MDC1 (MEDIATOR OF DNA-DAMAGE CHECKPOINT 1) → amplification loop recruiting more MRN-ATM complexes
5. **Checkpoint activation:** ATM → CHK2 Thr68 phosphorylation → CHK2 dimerizes/autophosphorylates → active CHK2 → phosphorylates CDC25A (degradation) → G1/S arrest; p53 Ser15 phosphorylation → p21 → G1 arrest; CDC25C phosphorylation → 14-3-3 binding → G2/M arrest
6. **HR initiation:** ATM → BRCA1 phosphorylation → PALB2-BRCA2 → RAD51 loading onto resected ssDNA

## Function

### Normal ATM roles

**Genomic stability maintenance:**
ATM is essential for mammalian genome maintenance; ATM-null mice are viable but infertile (meiotic defect), immunodeficient, radiation-sensitive, and prone to thymic lymphoma. ATM processes approximately 50 DSBs per cell per cell cycle arising from replication errors, reactive oxygen species, and endogenous nucleases — without ATM, these DSBs accumulate → chromosomal instability → cancer.

**V(D)J recombination and class switching:**
RAG1/RAG2 generate programmed DSBs during lymphocyte V(D)J recombination → ATM signals these as DSBs → ATM ensures breaks are rejoined correctly; ATM-deficient lymphocytes have elevated RAG-DSB-associated chromosomal translocations → explains lymphoid malignancy predisposition in AT.

**Meiotic recombination:**
SPO11 generates programmed DSBs in meiosis → ATM (and MRE11) process meiotic DSBs → crossover formation; ATM-null male mice are infertile due to spermatocyte arrest at zygotene.

### Synthetic lethality with ATM deficiency

ATM-deficient tumors are:
- **Sensitive to PARP inhibitors:** ATM loss reduces HR → PARP inhibitor synthetic lethality (especially in BRCA2-like context); olaparib FDA-approved for ATM-mutant mCRPC (though ATM benefit smaller than BRCA2)
- **Sensitive to DNA-damaging chemotherapy:** Platinum compounds, alkylating agents create DSBs → ATM-deficient cells cannot repair → enhanced cytotoxicity (but also in normal cells)
- **ATR inhibitors:** Synthetic lethal with ATM in some contexts (ATM-mutant cells rely more on ATR for checkpoint → ATR inhibition → catastrophic replication failure)

## Mechanism

### ATM inhibitors in development

**Olaparib (PARP inhibitor, exploiting ATM-associated HRD):**
- PROfound trial: olaparib active in BRCA1/2-mutant mCRPC (and ATM cohort B, though modest benefit); ATM mutation generates partial HRD
- Ongoing trials of PARP inhibitors in ATM-mutant pancreatic cancer, MCL, and AML

**ATM inhibitors (AZD0156, AZD1390):**
- AZD1390: CNS-penetrant ATM inhibitor; phase I in glioblastoma with radiation; rationale: ATM required for radioresistance → ATM inhibitor + RT → sensitizes GBM
- AZD0156 in AML combination studies

### ATM in CLL

**Del(11q22.3) and ATM mutation in CLL:**
- Del(11q22.3) removes one ATM allele; second allele often has point mutation → biallelic loss
- Clinical features: Large lymph nodes (bulky adenopathy), aggressive course; median time to treatment shorter than del(13q) or trisomy 12
- Treatment: Ibrutinib (BTK inhibitor) and venetoclax (BCL-2 inhibitor) are equally effective in del(11q) CLL compared to standard CLL; neither requires ATM for cytotoxicity → del(11q) is NOT a high-risk feature for ibrutinib/venetoclax era (unlike del17p/TP53 which affects p53-dependent apoptosis)
- Historical chemotherapy impact: FC/FCR regimens relied on p53-dependent apoptosis → del(17p)/TP53-mutant CLL (and ATM-deleted CLL) responded poorly to FCR → now superseded by TKI/BCL-2 inhibitor combinations

## Connections

- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — ATM phosphorylates p53 at Ser15 → p53 stabilization → MDM2 dissociation → p21/PUMA/BAX transcription → G1 arrest or apoptosis; TP53 mutations and ATM deletion are distinct but converging DDR failure mechanisms in CLL; p53-pathway-defective CLL (del17p or TP53 mutation) is the highest-risk CLL subset.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — ATM phosphorylates BRCA1 at Ser1387 and Ser1524 after DSB → BRCA1 activates HR repair; BRCA1 RING domain also ubiquitinates H2A at damage foci; ATM-BRCA1 axis is a core HR activation step; ATM deficiency reduces HR capacity → PARP inhibitor synthetic lethality in ATM-mutant tumors (prostate, pancreatic cancer).
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — ATM activates NF-κB in response to DSBs via NEMO-ATM nuclear complex → IKK → IκB phosphorylation → NF-κB; ATM-NF-κB signaling promotes survival in B-CLL; BCR-NF-κB and ATM-NF-κB are co-activated in CLL; ibrutinib (BTK inhibitor) blocks BCR-NF-κB and indirectly attenuates ATM-dependent survival.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — ATM-p53 axis activates PUMA (BBC3) and BAX → mitochondrial apoptosis; BCL-2 overexpression in CLL neutralizes ATM-driven apoptotic signaling; ATM-deleted CLL has impaired DNA-damage-induced apoptosis → venetoclax (BCL-2 inhibitor) active regardless of ATM status; BCL-2 dependency is independent of ATM/p53 DDR.

[^kastan-2010-atm-review]: Kastan MB, Bartek J. Cell-cycle checkpoints and cancer. *Nature.* 2004;432(7015):316-323. [doi:10.1038/nature03097](https://doi.org/10.1038/nature03097) · [PubMed 15549093](https://pubmed.ncbi.nlm.nih.gov/15549093/)
[^young-2014-atm-cancer]: Young LM, Bharat AG, Bhatt DL, et al. ATM mutations in CLL and its impact on treatment outcome. *Leukemia.* 2014;28(2):241-248. [doi:10.1038/leu.2013.298](https://doi.org/10.1038/leu.2013.298) · [PubMed 24166298](https://pubmed.ncbi.nlm.nih.gov/24166298/)
