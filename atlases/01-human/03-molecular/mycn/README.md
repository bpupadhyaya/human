---
schema: human-scale-entry/v1
id: mycn
name: MYCN
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "MYCN (N-Myc) is an amplified bHLH-LZ TF in ~20% neuroblastoma (~40% high-risk); heterodimerizes with MAX → drives ribosome biogenesis, TERT, cell cycle; AURKA stabilizes MYCN protein; MYCN amplification predicts poor prognosis; AURKA/BET inhibitors target MYCN indirectly."
aliases: ["MYCN", "N-Myc", "MYCN amplification", "N-myc oncogene", "MYCN neuroblastoma", "NMYC", "MYCN NEPC"]
sources:
  - id: schwab-1983-mycn-discovery
    type: peer-reviewed
    cite: "Schwab M, Alitalo K, Klempnauer KH, et al. Amplified DNA with limited homology to myc cellular oncogene is shared by human neuroblastoma cell lines and a neuroblastoma tumour. Nature. 1983;305(5931):245-248."
    doi: "10.1038/305245a0"
    pmid: "6888561"
    url: "https://doi.org/10.1038/305245a0"
  - id: matthay-1999-high-risk-nb
    type: peer-reviewed
    cite: "Matthay KK, Villablanca JG, Seeger RC, et al. Treatment of high-risk neuroblastoma with intensive chemotherapy, radiotherapy, autologous bone marrow transplantation, and 13-cis-retinoic acid. N Engl J Med. 1999;341(16):1165-1173."
    doi: "10.1056/NEJM199910143411601"
    pmid: "10519894"
    url: "https://doi.org/10.1056/NEJM199910143411601"
cross_links:
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC and MYCN share bHLH-LZ/MAX dimerization; MYCN amplification and MYC amplification are alternative drivers in different tumor types; BET bromodomain inhibitors suppress both MYC and MYCN transcription from super-enhancers; MYC and MYCN both activate ribosome biogenesis."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "ALK GOF mutations occur in ~10-14% neuroblastoma; MYCN and ALK are co-amplified in ~4% NB (double-hit worst prognosis); MYCN transcriptionally activates ALK in NB; lorlatinib (3rd-gen ALK inhibitor) is in Phase 3 ANBL2232 for ALK-aberrant high-risk NB."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "MYCN transcriptionally activates TERT; TERT structural rearrangements (~20-25% high-risk NB) and MYCN amplification are alternative telomerase activation strategies; ATRX mutations (~5-10%) activate ALT as a third telomere maintenance mechanism in NB."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "MYCN overactivation → oncogenic stress → p53 activation; neuroblastoma evades via MDM2 amplification (~4%); TP53 mutations rare at NB diagnosis (~1-2%) but acquired in ~80% at relapse; MDM2 inhibitors (idasanutlin) explored in MYCN-amplified NB."
---

# MYCN

## Overview

**MYCN (N-Myc)** is a member of the MYC family of transcription factors (alongside c-MYC and L-MYC) encoded at chromosome 2p24.3. MYCN contains a C-terminal basic helix-loop-helix leucine zipper (bHLH-LZ) domain that mediates obligate heterodimerization with **MAX** → binds E-box sequences (5'-CACGTG-3') → activates transcription of growth, ribosome biogenesis, cell cycle, and metabolic programs. MYCN was discovered in 1983 as an amplified oncogene in human neuroblastoma cell lines [^schwab-1983-mycn-discovery] and established the paradigm that oncogene amplification drives pediatric malignancy. **MYCN amplification** (defined as >4 haploid copies by FISH, commonly 50-300 copies in double minutes or homogeneously staining regions) occurs in ~20% of neuroblastoma overall and ~40% of high-risk cases, and is the most powerful adverse prognostic biomarker in neuroblastoma — its presence renders a tumor high-risk regardless of age or stage. MYCN amplification also occurs in medulloblastoma (Group 3, ~5%), small cell lung cancer (<5%), and **neuroendocrine prostate cancer (NEPC, ~40%)** where it drives lineage plasticity from adenocarcinoma to a treatment-resistant neuroendocrine phenotype. A critical post-translational regulator is **AURORA A kinase (AURKA)**, which forms a stabilizing complex with MYCN and protects it from FBXW7-mediated ubiquitination/degradation — making AURKA the primary druggable surrogate target for MYCN.

**MYCN amplification across cancers:**
- **Neuroblastoma:** ~20% overall; ~40% high-risk; localized disease with MYCN amp → reclassified as high-risk; virtually absent in Stage MS (favorable infant metastatic)
- **Medulloblastoma:** ~5% overall; predominantly Group 3 and Group 4; MYCN amp in SHH subgroup (infant SHH) → high-risk amplified SHH medulloblastoma (distinct from MYCN-amplified WNT — better prognosis)
- **Neuroendocrine prostate cancer:** ~40% NEPC vs <5% prostate adenocarcinoma; MYCN amp + AURKA amp → neuroendocrine lineage switch; enzalutamide-resistant; aurora A inhibitor + enzalutamide combinations in trials
- **SCLC:** MYCN amplification and MYC amplification occur in ~4% each; MYCN-amplified SCLC → aggressive variant-B phenotype
- **Retinoblastoma:** MYCN amplification in a rare subset of hereditary Rb (MYCN-amplified, RB1-wild-type Rb)

## Structure

### MYCN protein architecture

MYCN is a 464-amino-acid protein (nuclear, ~62 kDa):

**N-terminal transactivation domain (TAD, 1-73):**
Two subdomains (TAD1, MBII/Myc box II): interacts with TRRAP (a component of the TIP60/SAGA acetyltransferase complex) → histone H4 acetylation at target loci; MBII contains the conserved MYCN regulatory sequence; TAD phosphorylation by CDK7 → transcriptional competence; Aurora B can phosphorylate Ser62 analog in MYCN → modulates activity.

**Myc boxes (Mb I-IV):**
Conserved regulatory sequences across MYC family:
- MbI (~41-49): binds FBXW7 E3 ubiquitin ligase → Thr58 phosphorylation (GSK3β) → FBXW7 recognition → polyubiquitination → degradation
- MbII (~128-145): essential for transformation; recruits GCN5/PCAF acetyltransferases
- MbIII and MbIV: less characterized; contribute to chromatin remodeling complex recruitment

**Basic region + HLH + LZ (bHLH-LZ, 355-464):**
- Basic region (~355-379): makes major groove DNA contacts at E-box (CACGTG)
- HLH motif: mediates MAX heterodimerization (obligate, required for DNA binding and transcriptional activity); MYCN-MAX heterodimer is thermodynamically much tighter than MYCN homodimer
- Leucine zipper (LZ, ~440-464): contributes to dimerization interface; leucine side chains interdigitate with MAX LZ
- MYCN cannot bind DNA or activate transcription as a monomer — MAX dimerization is absolutely required

### AURKA-MYCN stabilization complex

**Key interaction:**
AURKA (serine/threonine kinase) binds MYCN (residues ~28-89, overlapping with N-terminal TAD) in a non-catalytic manner — does NOT phosphorylate MYCN at this interaction; instead, the AURKA-MYCN complex **sterically blocks FBXW7 recognition of phospho-Thr58** → prevents MYCN polyubiquitination → extends MYCN half-life from minutes to hours in dividing cells. AURKA protein levels peak in G2/M and maintain MYCN during mitotic entry → ensures daughter cells receive MYCN before protein degradation resumes in G1. In MYCN-amplified NB, AURKA protein is also frequently overexpressed (though not genetically amplified in most cases), creating a MYCN-AURKA co-dependency.

**Therapeutic implication:**
Alisertib (MLN8237), an AURKA-selective inhibitor: disrupts AURKA-MYCN complex → frees MYCN for FBXW7-dependent degradation → MYCN protein loss → G1 cell cycle arrest → differentiation/apoptosis in MYCN-amplified cells; alisertib is active in MYCN-amplified NB (Phase 2 ORR ~30%) and NEPC (Phase 2); resistance: FBXW7 loss-of-function mutations → MYCN resistant to degradation even without AURKA protection.

## Function

### MYCN transcriptional program

**Core outputs of MYCN/MAX E-box activation:**

**Ribosome biogenesis:**
MYCN activates all ~350 ribosomal protein genes (RPL/RPS) and rDNA transcription (RNA Pol I pathway via upstream binding factor, UBF) → increased ribosome density → enhanced translational capacity → anabolic growth; neuroblastoma cells with MYCN amplification have extreme ribosome production (detected as prominent nucleoli); inhibitors of RNA Pol I (CX-5461) exploit MYCN-driven ribosome stress → nucleolar stress → MDM2 sequestration → p53 activation.

**Cell cycle:**
MYCN activates CCND2 (cyclin D2) → CDK4/CDK6 → Rb phosphorylation → E2F release → S-phase entry; MYCN activates CDK4 expression; MYCN represses p21 (CDKN1A), p27 (CDKN1B) via transactivation of MIZ-1 repressor complex → removes G1 arrest checkpoints; CDK4/6 inhibitors explored in MYCN-amplified tumors.

**Telomere maintenance:**
MYCN directly activates TERT promoter → telomerase expression → telomere maintenance → replicative immortality; in TERT-structural-variant NB, TERT promoter is hijacked by adjacent regulatory elements — MYCN amplification and TERT structural variants are mutually exclusive mechanisms of telomerase activation.

**Metabolic reprogramming:**
MYCN activates LDHA (lactate dehydrogenase A), GLUT1 (SLC2A1) → Warburg metabolism; MYCN activates serine synthesis pathway (PHGDH, PSAT1) → one-carbon metabolism → nucleotide synthesis; MYCN-amplified cells are highly glutamine-dependent (MYCN activates GLS, glutaminase) → sensitivity to glutamine antagonists.

**Differentiation block:**
MYCN represses pro-differentiation transcription factors (HAND2, DBH, PHOX2B targets) → prevents sympathoadrenal differentiation from neural crest progenitor state → arrested in proliferative undifferentiated state; 13-cis-retinoic acid (isotretinoin) partially overcomes MYCN-driven differentiation block by inducing RAR/RXR-mediated MYCN repression → terminal differentiation; MYCN-high cells exhibit high OCT4, NANOG stem cell transcription program.

### MYCN in neuroendocrine prostate cancer

NEPC development under androgen deprivation therapy (ADT): prostate adenocarcinoma → lineage plasticity → neuroendocrine differentiation (NE markers: chromogranin A, synaptophysin, CD56); **MYCN amplification** (~40% NEPC) and **AURKA amplification** (~65% NEPC) drive NE transcriptional reprogramming via EZH2 activation (MYCN → EZH2 → H3K27me3 on AR-target and epithelial genes → NE gene derepression); NEPC is resistant to enzalutamide/abiraterone (AR-independent); alisertib + enzalutamide (Phase 2 NCT01799278): ORR ~36% in NEPC/high-AURKA; NEPC patients with MYCN/AURKA co-amplification benefit most.

## Mechanism

### Indirect MYCN targeting strategies

**BET bromodomain inhibition (JQ1, OTX015):**
MYCN is transcribed from a large super-enhancer (SE) at 2p24; BRD4 (BET family reader) reads acetyl-H3K27/H3K9 at the MYCN SE → enhances elongation of MYCN mRNA; JQ1 (BET inhibitor) displaces BRD4 from MYCN SE → MYCN mRNA transcription drops ~50-80%; cells with highest MYCN SE size are most sensitive; resistance: MED12 mutations, MYCN enhancer remodeling; clinical BET inhibitors (ABBV-075/mivebresib, BMS-986158) in early trials in MYCN-amplified tumors.

**CDK7 inhibition (THZ1, SY-1365):**
CDK7 (transcription-associated kinase, part of TFIIH) phosphorylates RNA Pol II CTD (Ser5) → transcription initiation; CDK7 also phosphorylates MYCN TAD (activating) and CDK4/CDK6/CDK1 (activating kinase); THZ1 covalently inhibits CDK7 → preferential reduction of SE-driven transcription (MYCN, HAND1, PHOX2B targets) → tumor-selective toxicity.

**Aurora A inhibition (alisertib):**
As described above; disrupts AURKA-MYCN stabilization → FBXW7-mediated MYCN degradation; alisertib Phase 2 in R/R neuroblastoma (MIBG non-avid): ORR ~30%; dose-limiting neutropenia; Phase 3 not yet completed.

**MDM2 inhibition (idasanutlin):**
MYCN-amplified cells depend on MDM2 to suppress p53-driven apoptosis (MYCN → p53 oncogenic stress → MDM2 induction → p53 suppression); idasanutlin (RG7388) → MDM2 blockade → p53 reactivation → MYCN-amplified cell apoptosis; Phase 1/2 in pediatric solid tumors including NB; AML combination (idasanutlin + cytarabine).

## Connections

- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC and MYCN share bHLH-LZ/MAX dimerization; MYCN amplification and MYC amplification are alternative drivers in different tumor types; BET bromodomain inhibitors suppress both MYC and MYCN transcription from super-enhancers; MYC and MYCN both activate ribosome biogenesis.
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — ALK GOF mutations occur in ~10-14% neuroblastoma; MYCN and ALK are co-amplified in ~4% NB (double-hit worst prognosis); MYCN transcriptionally activates ALK in NB; lorlatinib (3rd-gen ALK inhibitor) is in Phase 3 ANBL2232 for ALK-aberrant high-risk NB.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — MYCN transcriptionally activates TERT; TERT structural rearrangements (~20-25% high-risk NB) and MYCN amplification are alternative telomerase activation strategies; ATRX mutations (~5-10%) activate ALT as a third telomere maintenance mechanism in NB.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — MYCN overactivation → oncogenic stress → p53 activation; neuroblastoma evades via MDM2 amplification (~4%); TP53 mutations rare at NB diagnosis (~1-2%) but acquired in ~80% at relapse; MDM2 inhibitors (idasanutlin) explored in MYCN-amplified NB.

[^schwab-1983-mycn-discovery]: Schwab M, Alitalo K, Klempnauer KH, et al. Amplified DNA with limited homology to myc cellular oncogene is shared by human neuroblastoma cell lines and a neuroblastoma tumour. *Nature.* 1983;305(5931):245-248. [doi:10.1038/305245a0](https://doi.org/10.1038/305245a0) · [PubMed 6888561](https://pubmed.ncbi.nlm.nih.gov/6888561/)
[^matthay-1999-high-risk-nb]: Matthay KK, Villablanca JG, Seeger RC, et al. Treatment of high-risk neuroblastoma with intensive chemotherapy, radiotherapy, autologous bone marrow transplantation, and 13-cis-retinoic acid. *N Engl J Med.* 1999;341(16):1165-1173. [doi:10.1056/NEJM199910143411601](https://doi.org/10.1056/NEJM199910143411601) · [PubMed 10519894](https://pubmed.ncbi.nlm.nih.gov/10519894/)
