---
schema: human-scale-entry/v1
id: lztr1
name: LZTR1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "LZTR1 is a Cullin3 E3 ubiquitin ligase adaptor that targets RAS GTPases (KRAS, MRAS, RRAS2) for proteasomal degradation; LOF → RAS accumulation → RAS-MAPK hyperactivation; germline biallelic LZTR1 LOF = schwannomatosis; LZTR1 also causes Noonan syndrome (dominant)."
aliases: ["LZTR1", "Leucine-Zipper-like Transcription Regulator 1", "LZTR1 schwannomatosis", "LZTR1 RAS ubiquitination", "LZTR1 CUL3", "LZTR1 Noonan", "LZTR1 tumor suppressor", "BTB-Kelch LZTR1", "LZTR1 RAS degradation"]
sources:
  - id: piotrowski-2014-lztr1
    type: peer-reviewed
    cite: "Piotrowski A, Xie J, Liu YF, et al. Germline loss-of-function mutations in LZTR1 predispose to an inherited disorder of multiple schwannomas. Nat Genet. 2014;46(2):182-187."
    doi: "10.1038/ng.2855"
    pmid: "24362817"
    url: "https://doi.org/10.1038/ng.2855"
  - id: steklov-2018-lztr1-ras
    type: peer-reviewed
    cite: "Steklov M, Pandolfi S, Baietti MF, et al. Mutations in LZTR1 drive human disease by dysregulating RAS ubiquitination. Science. 2018;362(6419):1177-1182."
    doi: "10.1126/science.aap7607"
    pmid: "30442762"
    url: "https://doi.org/10.1126/science.aap7607"
cross_links:
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "Germline biallelic LZTR1 LOF (or dominant negative missense) causes LZTR1-schwannomatosis; LZTR1 somatic second hit in each schwannoma; Schwann cells with loss of both LZTR1 alleles → RAS-MAPK → schwannoma; presents as chronic pain and multiple peripheral nerve tumors."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SMARCB1 (INI1, SNF5) is the primary schwannomatosis gene (~40%); SMARCB1 germline heterozygous + somatic mosaic LOH → schwannomas; distinct from SMARCB1 biallelic LOF in AT/RT (malignant); LZTR1 and SMARCB1 are both CUL3-adaptor pathway tumor suppressors in Schwann cells."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "LZTR1 ubiquitinates KRAS, MRAS, and RRAS2 at the polybasic C-terminal region for proteasomal degradation; LZTR1 LOF → RAS protein accumulation → MAPK hyperactivation; distinct from oncogenic KRAS mutations; RAS ubiquitination is LZTR1's primary tumor suppressor function."
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "NF2/merlin and LZTR1 are both schwannoma tumor suppressors at 22q; NF2 causes bilateral VS + meningioma; LZTR1 causes schwannomatosis (multiple peripheral/spinal schwannomas, no bilateral VS); mechanistically distinct: NF2 → Hippo-YAP; LZTR1 → RAS ubiquitination."
---

# LZTR1

## Overview

**LZTR1** (Leucine-Zipper-like Transcription Regulator 1) is an 836 amino acid (92 kDa) **substrate adaptor** for the **Cullin3 (CUL3)-RING E3 ubiquitin ligase** complex that functions as a critical regulator of **RAS GTPase stability**. LZTR1 recruits RAS family proteins (KRAS, MRAS, RRAS2) to the CUL3-E3 complex → polyubiquitination → proteasomal degradation → reduced RAS protein levels → dampened RAS-MAPK signaling. Germline pathogenic variants in LZTR1 cause two distinct hereditary conditions depending on zygosity and mutation type: **biallelic LOF (recessive) or dominant negative missense → schwannomatosis** (multiple schwannomas without bilateral vestibular schwannomas), and **monoallelic dominant LOF → Noonan syndrome** (a RASopathy with cardiac defects and developmental features). LZTR1 was identified as a schwannomatosis predisposition gene by Piotrowski et al. in 2014, and its molecular mechanism as a RAS ubiquitin ligase adaptor was established by Steklov et al. in 2018 [^piotrowski-2014-lztr1] [^steklov-2018-lztr1-ras].

**LZTR1 disease spectrum — genotype-phenotype:**

| Inheritance | LZTR1 variant type | Disease | Key features |
|---|---|---|---|
| Biallelic LOF | Homozygous or compound het. | Schwannomatosis type 2 | Multiple schwannomas, chronic pain, no bilateral VS |
| Dominant negative missense | Heterozygous (D-N) | Schwannomatosis type 2 | Same as biallelic; D-N mimics LOF |
| Monoallelic LOF | Heterozygous LOF | Noonan syndrome | Cardiac defects, short stature, pulmonary stenosis |
| Somatic LOF | Second hit in tumor | Glioblastoma, AML | RAS accumulation in tumor cells |

## Structure

### LZTR1 protein domains

**N-terminal Kelch domain cluster (aa 1-480):**
- Contains six Kelch repeat modules (Kelch1-6); each Kelch repeat is a ~50 aa antiparallel β-hairpin; six repeats fold into a **β-propeller** (six-bladed propeller with pseudo-6-fold symmetry)
- The Kelch propeller is the **substrate recognition domain**: binds the C-terminal polybasic region (PBR) and CaaX motif of RAS family GTPases (specifically the hypervariable region, HVR, C-terminal of KRAS4B, MRAS, RRAS2)
- RAS binding to Kelch propeller does NOT require RAS to be in GTP-bound (active) or GDP-bound (inactive) state — LZTR1 ubiquitinates both active and inactive RAS (ubiquitination at Lys170 or Lys147 within RAS)
- KRAS Lys170 ubiquitination (on the HVR) → prevents membrane association (reduces RAS membrane localization); also targets RAS for proteasomal degradation via K48-ubiquitin chain; net effect: reduced functional RAS at plasma membrane

**BTB domain (Bric-à-brac, Tramtrack, Broad Complex; aa 481-640):**
- Bihelical domain for dimerization and Cullin3 (CUL3) recruitment
- BTB domain binds the N-terminal domain of CUL3 → LZTR1 is the substrate adaptor (F-box equivalent) of the **CUL3-LZTR1-RBX1 E3 ligase**
- LZTR1 must dimerize (homodimerize via BTB domain) for efficient E3 function; dominant negative (D-N) pathogenic missense variants disrupt CUL3 binding or dimerization → the mutant subunit poisons the dimer → impaired E3 function despite intact wild-type allele

**BACK domain (BTB and C-terminal Kelch; aa 641-836):**
- Connects BTB to Kelch; contributes to proper orientation of the Kelch propeller relative to the CUL3 complex for efficient substrate presentation
- Contains additional protein-protein interactions not yet fully characterized; may interact with COP9 signalosome (de-neddylation regulator of CUL3)

### RAS ubiquitination mechanism

**Substrates of LZTR1:**
- **KRAS4B** (primary substrate): polybasic region (KEKMSK) and CaaX box (CVIM) → HVR (aa 167-189) recognized by Kelch propeller → ubiquitinated at Lys170 → reduced membrane association + degradation
- **MRAS** (muscle-specific RAS): HVR also recognized; MRAS ubiquitination reduces SHOC2-PP1C complex formation (SHOC2-MRAS-PP1C phosphatase dephosphorylates RAF pSer259 → RAF activation); thus LZTR1 LOF → MRAS accumulation → SHOC2 complex hyperactivity → sustained RAF activation even without upstream RAS signal
- **RRAS2 (TC21)**: third LZTR1 substrate; RRAS2 is highly expressed in Schwann cells → LZTR1 LOF in Schwann cells → RRAS2 accumulation → Schwann cell proliferation (schwannoma formation)
- HRAS, NRAS, KRAS4A: much weaker LZTR1 substrates; C-terminal HVR differs

**Why schwannoma specifically?**
RRAS2 is highly expressed in Schwann cells and is the primary RAS isoform driving Schwann cell proliferation. LZTR1 LOF → RRAS2 protein accumulation → RAS-MAPK → Schwann cell hyperproliferation → schwannoma. Biallelic LZTR1 LOF (both alleles lost) is required in tumor cells (follows two-hit tumor suppressor model); germline one allele + somatic second hit in each schwannoma.

## Function

### LZTR1 in RAS pathway homeostasis

**LZTR1 as a RAS rheostat:**
Under normal signaling:
1. RTK activation → RAS-GTP
2. RAS-GTP → RAF → MEK → ERK → gene expression
3. RAS intrinsic GTPase + GAPs → RAS-GDP (inactive)
4. **LZTR1-CUL3 → ubiquitinates RAS (both GDP and GTP forms) → degradation → limits total RAS pool at membrane**

With LZTR1 LOF:
- Total RAS protein increases (less degradation)
- More RAS at membrane → prolonged RAS-GTP signal amplitude after RTK activation
- MRAS accumulation → SHOC2 complex hyperactive → RAF activated even without upstream signal
- Net: RAS-MAPK chronically upregulated → neoplastic transformation in susceptible cell types (Schwann cells with RRAS2 high expression)

**LZTR1 and Noonan syndrome (monoallelic dominant LOF):**
- Noonan syndrome (NS) is a RASopathy (germline RAS-MAPK pathway gain-of-function): short stature, pulmonary stenosis, ptosis, cryptorchidism, mild cognitive effects
- LZTR1 monoallelic LOF → heterozygous → 50% reduced LZTR1 → RAS not fully ubiquitinated → elevated RAS → mild MAPK gain-of-function → NS phenotype (similar to KRAS, RAF1, BRAF, MEK1/2 heterozygous activating mutations causing Noonan)
- Recessive NS: biallelic LZTR1 LOF → same MAPK gain but more severe (Johnston 2018); may present with coarctation of aorta, hypertrophic cardiomyopathy, more severe NS features
- Overlap between LZTR1 dominant NS and schwannomatosis: some LZTR1 dominant negative missense variants cause NS features AND elevated schwannoma risk (dual phenotype)

### LZTR1 somatic mutations in cancer

**Glioblastoma:**
- LZTR1 somatic LOF mutations in ~2-3% of GBM (IDH-wildtype); identified in next-gen sequencing cohorts; biallelic LZTR1 loss → RRAS2/KRAS accumulation → RAS-MAPK → glioblastoma growth
- LZTR1 somatic LOF may contribute to MAPK inhibitor resistance (KRAS accumulation despite upstream EGFR inhibition)

**AML and myeloid malignancies:**
- LZTR1 somatic LOF in a small fraction of AML; KRAS/NRAS mutations are common in AML; LZTR1 loss may functionally mimic KRAS/NRAS mutation by elevating RAS protein levels

## Mechanism

### LZTR1 and CUL3 E3 ligase pathway

LZTR1 functions as one of ~200 BTB domain-containing CUL3 adaptors in the human genome:
- CUL3 is a scaffold protein (a Cullin family member); CUL3 is neddylated (NEDD8-CUL3) for activation → E2 conjugating enzyme (UBE2D/UBE2L3 family) charged with ubiquitin → RING domain (RBX1) catalyzes Ub transfer to substrate
- COP9 Signalosome (CSN) deneddylates CUL3 → CUL3 inactive (off state); cyclic neddylation/deneddylation regulates CUL3 activity
- LZTR1 degrades SMAD3, a β-catenin component, and RAS proteins; its substrates define it as a tumor suppressor in multiple contexts

**Therapeutic implications:**
- MLN4924 (pevonedistat): a NEDD8-activating enzyme (NAE) inhibitor that blocks neddylation → prevents CUL3 (and all other Cullins) activation → global inhibition of Cullin-RING ligases; in clinical trials for AML/MDS; LZTR1-deficient tumors may respond differently (already impaired CUL3-LZTR1 function)
- No LZTR1-specific activators clinically available; MEK inhibitors (trametinib, cobimetinib) rationale in LZTR1-deficient tumors (LZTR1 LOF = RAS-MAPK gain → MEK inhibitor may target downstream)

## Connections

- `connects-to` → **[Schwannomatosis](../../07-system/schwannomatosis/README.md)** — Germline biallelic LZTR1 LOF (or dominant negative missense) causes LZTR1-schwannomatosis; LZTR1 somatic second hit in each schwannoma; Schwann cells with loss of both LZTR1 alleles → RAS-MAPK → schwannoma; presents as chronic pain and multiple peripheral nerve tumors.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SMARCB1 (INI1, SNF5) is the primary schwannomatosis gene (~40%); SMARCB1 germline heterozygous + somatic mosaic LOH → schwannomas; distinct from SMARCB1 biallelic LOF in AT/RT (malignant); LZTR1 and SMARCB1 are both CUL3-adaptor pathway tumor suppressors in Schwann cells.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — LZTR1 ubiquitinates KRAS, MRAS, and RRAS2 at the polybasic C-terminal region for proteasomal degradation; LZTR1 LOF → RAS protein accumulation → MAPK hyperactivation; distinct from oncogenic KRAS mutations; RAS ubiquitination is LZTR1's primary tumor suppressor function.
- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — NF2/merlin and LZTR1 are both schwannoma tumor suppressors at 22q; NF2 causes bilateral VS + meningioma; LZTR1 causes schwannomatosis (multiple peripheral/spinal schwannomas, no bilateral VS); mechanistically distinct: NF2 → Hippo-YAP; LZTR1 → RAS ubiquitination.

[^piotrowski-2014-lztr1]: Piotrowski A, Xie J, Liu YF, et al. Germline loss-of-function mutations in LZTR1 predispose to an inherited disorder of multiple schwannomas. *Nat Genet.* 2014;46(2):182-187. [doi:10.1038/ng.2855](https://doi.org/10.1038/ng.2855) · [PubMed 24362817](https://pubmed.ncbi.nlm.nih.gov/24362817/)
[^steklov-2018-lztr1-ras]: Steklov M, Pandolfi S, Baietti MF, et al. Mutations in LZTR1 drive human disease by dysregulating RAS ubiquitination. *Science.* 2018;362(6419):1177-1182. [doi:10.1126/science.aap7607](https://doi.org/10.1126/science.aap7607) · [PubMed 30442762](https://pubmed.ncbi.nlm.nih.gov/30442762/)
