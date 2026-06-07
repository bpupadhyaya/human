---
schema: human-scale-entry/v1
id: arid1a
name: ARID1A
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "ARID1A (BAF250A) is the most mutated SWI/SNF gene; LOF disrupts cBAF → EZH2 dependency; most frequent in ovarian clear cell (~50%), uterine endometrioid (~40%), gastric cancer; ARID1A LOF suppresses MLH1; co-mutation with PIK3CA defines ovarian clear cell carcinoma."
aliases: ["ARID1A", "BAF250A", "ARID1A mutation", "SWI/SNF ARID1A", "ARID1A ovarian", "ARID1A endometrial", "ARID1A gastric", "BAF complex ARID1A", "ARID1A LOF cancer", "OCCC ARID1A"]
sources:
  - id: jones-2010-arid1a-occc
    type: peer-reviewed
    cite: "Jones S, Wang TL, Shih IeM, et al. Frequent mutations of chromatin remodeling gene ARID1A in ovarian clear cell carcinoma. Science. 2010;330(6001):228-231."
    doi: "10.1126/science.1196333"
    pmid: "20826764"
    url: "https://doi.org/10.1126/science.1196333"
  - id: kim-2015-arid1a-ezh2
    type: peer-reviewed
    cite: "Kim KH, Kim W, Howard TP, et al. SWI/SNF-mutant cancers depend on catalytic and non-catalytic activity of EZH2. Nat Med. 2015;21(12):1491-1496."
    doi: "10.1038/nm.3968"
    pmid: "26552009"
    url: "https://doi.org/10.1038/nm.3968"
cross_links:
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "ARID1A LOF disrupts cBAF → EZH2/PRC2 gains access to ARID1A-target loci → H3K27me3 accumulation; OCCC and endometrial cancers with ARID1A LOF are EZH2-dependent in preclinical models; tazemetostat active in ARID1A-mutant OCCC in early-phase trials."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "ARID1A and SMARCB1 are both cBAF complex subunits; ARID1A LOF → cBAF destabilization → EZH2 dependency analogous to SMARCB1 biallelic LOF in AT/RT; ARID1A and SMARCB1 synthetic lethality in the BAF complex; ARID1A-mutant cancers and AT/RT share tazemetostat sensitivity."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "ARID1A + PIK3CA co-mutation defines ~25-30% of ovarian clear cell carcinomas; PIK3CA → PI3K/AKT/mTOR → OCCC proliferation; ARID1A LOF + PIK3CA creates synthetic vulnerability to dual PI3K/mTOR inhibition; temsirolimus active in PIK3CA-mutant OCCC Phase 2."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "ARID1A directly recruits MLH1 and MSH2 (mismatch repair proteins) to chromatin; ARID1A LOF → MLH1 eviction from chromatin → local microsatellite instability; PD-L1 upregulated in ARID1A-mutant OCCC → immunotherapy sensitivity; ARID1A LOF + MLH1 LOF = MSI-H (rare, ~5% OCCC)."
---

# ARID1A

## Overview

**ARID1A** (AT-rich interaction domain 1A; also **BAF250A**) encodes a 2,285-amino-acid (250 kDa) subunit of the **canonical BAF (cBAF) SWI/SNF chromatin remodeling complex**. ARID1A is the most commonly mutated SWI/SNF gene in human cancer (~7% TCGA pan-cancer frequency), and the most mutated chromatin remodeling gene overall. Its AT-rich interaction domain (ARID) binds AT-rich DNA sequences, targeting BAF complexes to specific genomic loci; it also mediates protein-protein interactions that direct cBAF to enhancers and promoters of tumor suppressor genes. Loss of ARID1A function results in cBAF complex destabilization, access of EZH2/PRC2 to previously protected chromatin, and accumulation of the repressive H3K27me3 mark — creating an EZH2-dependent epigenetic state [^jones-2010-arid1a-occc] [^kim-2015-arid1a-ezh2].

**ARID1A alterations across tumor types:**

| Tumor type | Frequency | Notes |
|---|---|---|
| Ovarian clear cell carcinoma (OCCC) | ~50-55% | Co-occurs with PIK3CA in ~25-30%; defines molecular subtype |
| Uterine endometrioid carcinoma | ~35-40% | Often MSI-H tumors; ARID1A LOF → MMR suppression |
| Gastric adenocarcinoma | ~10-15% | EBV-positive subtype (~25%); CIN subtype (~15%) |
| Hepatocellular carcinoma | ~10-15% | Associated with HBV; LOF mechanism |
| Cholangiocarcinoma | ~15-20% | Intrahepatic CCA; enriched in FGFR2 co-mutation cases |
| Colorectal cancer | ~5-10% | MSI-H tumors enriched; sporadic serrated pathway |
| Pancreatic adenocarcinoma | ~5-8% | Associated with KRAS/TP53 background |
| Urothelial carcinoma (bladder) | ~25-30% | High frequency in superficial bladder cancer |

**Germline ARID1A:** Rare germline ARID1A pathogenic variants are associated with Coffin-Siris syndrome (intellectual disability, absent 5th fingernail); the tumor predisposition spectrum of germline ARID1A is incompletely characterized

## Structure

### ARID1A protein architecture

**ARID domain (aa 1~1450-1600; C-terminal region):**
AT-rich interaction domain; double-stranded DNA-binding module; binds AT-rich sequences in chromatin; directs cBAF complex to specific genomic loci; ARID domains are broadly distributed across the ARID protein family (ARID1A, ARID1B, ARID2, ARID3A/B, ARID4A/B, ARID5A/B); ARID1A's ARID domain is the least sequence-selective of the family (binds broad AT-rich regions vs. highly specific ARID3 binding)

**N-terminal domain (aa 1-500):**
Proline-rich region; intrinsically disordered; mediates interaction with p53 (ARID1A enhances p53-dependent transcription); contains nuclear localization signals; phosphorylated by CDK2 (cell-cycle-dependent regulation of ARID1A activity)

**BAF complex-anchoring domain:**
ARID1A incorporates into cBAF through interaction with SMARCA4 (BRG1) ATPase and SMARCC1/SMARCC2 subunits; ARID1A replaces ARID1B (mutually exclusive) in individual cBAF complexes — ARID1A and ARID1B define two distinct cBAF subtypes with overlapping but distinct target genes; ARID1A-containing cBAF is more prevalent in differentiated epithelial cells; ARID1B-containing cBAF in neuronal/stem cells

**LANA-binding domain:**
ARID1A recruits MLH1 (MutL homolog 1) and MSH2 (MutS homolog 2) of the mismatch repair (MMR) complex to chromatin at microsatellite loci → MMR protein placement → active mismatch correction during DNA replication; ARID1A LOF → MLH1/MSH2 eviction from chromatin → local microsatellite instability; this mechanism explains the elevated microsatellite instability seen in ARID1A-mutant endometrial and gastric cancers

### ARID1A mutation patterns

**LOF mutation types:**
- Truncating mutations (frameshift/nonsense): ~75% of ARID1A cancer mutations; protein unstable and degraded; loss of BAF complex function
- Missense mutations: minority; many in ARID or protein-interaction domains; often partial LOF
- Large deletions: rare; includes entire gene deletion
- Biallelic LOF: required in most cancers (tumor suppressor mode); heterozygous LOF may confer haploinsufficiency in some contexts (gastric cancer)

**IHC:**
ARID1A IHC (anti-BAF250A, clone PSG3): loss of nuclear staining = ARID1A LOF; sensitivity ~85%, specificity ~90% for ARID1A mutation; useful diagnostic surrogate in OCCC and endometrial carcinoma; intact ARID1A (positive nuclear staining) = wild-type; patchy loss may reflect intratumoral heterogeneity

## Function

### Tumor-suppressive functions of ARID1A

**Transcriptional activation of tumor suppressors:**
ARID1A-containing cBAF remodels chromatin at promoters of CDKN1A (p21), CDKN1B (p27), CDKN2A (p16), and other tumor suppressor genes → open chromatin → transcription; ARID1A LOF → these loci become inaccessible → EZH2/PRC2 fills the vacuum → H3K27me3 → silencing of p21/p27 → cell cycle dysregulation

**DNA damage response:**
ARID1A recruited to DNA double-strand breaks by ATM → promotes DNA repair via homologous recombination (HR) and non-homologous end joining (NHEJ); ARID1A LOF → impaired HR → DNA repair defect → BRD4-mediated error-prone repair → accumulation of somatic mutations; this creates a theoretical synthetic lethality with PARP inhibitors (ARID1A-mutant tumors may be HR-deficient)

**Mismatch repair interaction:** [^jones-2010-arid1a-occc]
ARID1A scaffolds MLH1 and MSH2 at chromatin → MMR complex correctly positioned → active mismatch correction; ARID1A LOF → MLH1/MSH2 displaced → local microsatellite instability → elevated TMB → immunogenic mutation burden; PD-L1 upregulated in ARID1A-mutant tumors via IFN signaling enhancement → higher ICB response rates

**Enhancer regulation:**
ARID1A cBAF complexes are essential for maintaining active enhancers (H3K27ac-marked); ARID1A LOF → enhancer inactivation at lineage-specific tumor suppressor loci → de-differentiation; in OCCC, ARID1A LOF + PIK3CA mutation → coordinate epigenetic (ARID1A) + RTK/kinase (PIK3CA) reprogramming → OCCC-specific transcriptional program

### ARID1A LOF → EZH2 synthetic vulnerability [^kim-2015-arid1a-ezh2]

**The ARID1A-EZH2 axis:**
Normal epithelial cell: ARID1A-containing cBAF occupies promoters/enhancers of differentiation genes → PRC2/EZH2 excluded from these loci → H3K27me3 absent → genes transcribed; ARID1A LOF: cBAF complex destabilized → PRC2/EZH2 gains access → H3K27me3 accumulates at ARID1A-target loci → tumor suppressor gene silencing → EZH2 enzymatic activity becomes essential for maintaining the repressed state

**Therapeutic implication (Kim 2015):**
EZH2 catalytic activity is required for the repressive H3K27me3 state in ARID1A-mutant tumors; EZH2 inhibitors (tazemetostat) → H3K27me3 removal → restoration of ARID1A-target gene expression → tumor suppressor reactivation → cell cycle arrest; this is mechanistically analogous to AT/RT (SMARCB1 LOF → EZH2 dependency) and synovial sarcoma (SS18-SSX → SMARCB1 displacement → EZH2 dependency); in each case, BAF complex disruption → EZH2 becomes the essential epigenetic maintainer → tazemetostat active

## Mechanism

### EZH2 inhibition in ARID1A-mutant cancers

**Tazemetostat in ARID1A-mutant tumors:**
Preclinical: selective toxicity in ARID1A-null vs ARID1A-intact cell lines; ARID1A-null ovarian and endometrial cancer cells show ORR-equivalent to AT/RT cells in tazemetostat sensitivity studies; Phase 2 study of tazemetostat in ARID1A-mutant OCCC ongoing (NCT04171700); combination tazemetostat + PARP inhibitor (olaparib) under investigation based on DNA repair defect + epigenetic vulnerability

**PARP inhibitor synthetic lethality:**
ARID1A LOF → HR deficiency → PARP inhibitor sensitivity in a subset; combined PARP inhibitor (olaparib/rucaparib) + EZH2 inhibitor (tazemetostat) → dual epigenetic + DNA repair blockade; Phase 1/2 OCCC-specific trials ongoing

**mTOR inhibitors:**
ARID1A LOF + PIK3CA co-mutation → PI3K/AKT/mTOR hyperactivation; PI3K/mTOR inhibitors active in PIK3CA-mutant OCCC; temsirolimus Phase 2 in OCCC/endometrioid ovarian: ORR ~10-15%; combination temsirolimus + carboplatin/paclitaxel: Phase 2 active

**Immunotherapy:**
ARID1A LOF → MLH1/MSH2 displacement → local MSI-like state → elevated TMB → PD-L1 upregulation; pembrolizumab + bevacizumab shows activity in ARID1A-mutant OCCC; KEYNOTE-158 (pembrolizumab in TMB-high solid tumors): ORR ~29% in TMB-high OCCC subgroup; durvalumab + olaparib combination in ARID1A-mutant tumors being studied

## Connections

- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — ARID1A LOF disrupts cBAF → EZH2/PRC2 gains access to ARID1A-target loci → H3K27me3 accumulation; OCCC and endometrial cancers with ARID1A LOF are EZH2-dependent in preclinical models; tazemetostat active in ARID1A-mutant OCCC in early-phase trials.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — ARID1A and SMARCB1 are both cBAF complex subunits; ARID1A LOF → cBAF destabilization → EZH2 dependency analogous to SMARCB1 biallelic LOF in AT/RT; ARID1A and SMARCB1 synthetic lethality in the BAF complex; ARID1A-mutant cancers and AT/RT share tazemetostat sensitivity.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — ARID1A + PIK3CA co-mutation defines ~25-30% of ovarian clear cell carcinomas; PIK3CA → PI3K/AKT/mTOR → OCCC proliferation; ARID1A LOF + PIK3CA creates synthetic vulnerability to dual PI3K/mTOR inhibition; temsirolimus active in PIK3CA-mutant OCCC Phase 2.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — ARID1A directly recruits MLH1 and MSH2 (mismatch repair proteins) to chromatin; ARID1A LOF → MLH1 eviction from chromatin → local microsatellite instability; PD-L1 upregulated in ARID1A-mutant OCCC → immunotherapy sensitivity; ARID1A LOF + MLH1 LOF = MSI-H (rare, ~5% OCCC).

[^jones-2010-arid1a-occc]: Jones S, Wang TL, Shih IeM, et al. Frequent mutations of chromatin remodeling gene ARID1A in ovarian clear cell carcinoma. *Science.* 2010;330(6001):228-231. [doi:10.1126/science.1196333](https://doi.org/10.1126/science.1196333) · [PubMed 20826764](https://pubmed.ncbi.nlm.nih.gov/20826764/)
[^kim-2015-arid1a-ezh2]: Kim KH, Kim W, Howard TP, et al. SWI/SNF-mutant cancers depend on catalytic and non-catalytic activity of EZH2. *Nat Med.* 2015;21(12):1491-1496. [doi:10.1038/nm.3968](https://doi.org/10.1038/nm.3968) · [PubMed 26552009](https://pubmed.ncbi.nlm.nih.gov/26552009/)
