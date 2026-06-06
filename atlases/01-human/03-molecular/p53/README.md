---
schema: human-scale-entry/v1
id: p53
name: p53
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Transcription factor and master tumor suppressor encoded by TP53; activated by DNA damage, oncogene activation, and hypoxia. Triggers cell-cycle arrest (p21/CDKN1A), apoptosis (PUMA, BAX), and senescence. Mutated in >50% of human cancers; 'guardian of the genome.'"
aliases: ["TP53", "tumor protein p53", "p53 tumor suppressor", "guardian of the genome"]
sources:
  - id: lane-1992-guardian
    type: peer-reviewed
    cite: "Lane DP. Cancer. p53, guardian of the genome. Nature. 1992;358(6381):15-16."
    doi: "10.1038/358015a0"
    pmid: "1614522"
    url: "https://doi.org/10.1038/358015a0"
  - id: vousden-2009-p53-review
    type: peer-reviewed
    cite: "Vousden KH, Prives C. Blinded by the Light: The Growing Complexity of p53. Cell. 2009;137(3):413-431."
    doi: "10.1016/j.cell.2009.04.037"
    pmid: "19410540"
    url: "https://doi.org/10.1016/j.cell.2009.04.037"
  - id: levine-2020-p53-metabolism
    type: peer-reviewed
    cite: "Levine AJ. p53: 800 million years of evolution and 40 years of discovery. Nat Rev Cancer. 2020;20(8):471-480."
    doi: "10.1038/s41568-020-0262-1"
    pmid: "32404993"
    url: "https://doi.org/10.1038/s41568-020-0262-1"
cross_links:
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "p53 activation in neutrophils promotes apoptosis after pathogen clearance, limiting tissue damage from prolonged neutrophil activity; MDM2-mediated p53 degradation extends neutrophil survival during acute infection."
  - target: 01-human/07-system/cytokine-storm
    relation: modulates
    note: "p53 suppresses NF-κB-driven inflammatory gene expression; in cytokine storm contexts, loss of p53 function can amplify hyperinflammatory responses; conversely, p53 activation promotes resolution of inflammation via apoptotic clearance of activated immune cells."
---

# p53

## Overview

**p53** (tumor protein p53, encoded by the **TP53** gene on chromosome 17p13.1) is the most frequently mutated tumor suppressor in human cancer — lost or inactivated in **>50% of all human cancers** across all major types. Dubbed the **"guardian of the genome"** by David Lane in 1992 [^lane-1992-guardian], p53 is a transcription factor that functions as the cell's central sensor and coordinator of responses to **genotoxic stress, oncogenic signaling, hypoxia, and metabolic disruption**. When activated, p53 enforces a suite of protective programs: **DNA repair, cell-cycle arrest, apoptosis, senescence, and metabolic reprogramming** — all aimed at preventing the propagation of genetically damaged cells.

p53 was first described in 1979 as a protein co-immunoprecipitating with the SV40 large T antigen; it was initially misidentified as an oncogene (because early studies used mutant TP53 alleles) before being correctly identified as a tumor suppressor in 1989. The original *p53* nomenclature derives from its molecular weight of ~53 kDa on SDS-PAGE (actual mass ~43.7 kDa; the discrepancy reflects its proline-rich sequence causing anomalous migration).

## Structure

### Protein architecture

p53 is a **homotetrameric transcription factor**; each 393 amino acid monomer contains five functional domains [^vousden-2009-p53-review]:

1. **N-terminal transactivation domain (TAD, aa 1-67):** Two subdomains (AD1: 1-40; AD2: 40-67); binds transcriptional machinery (TFIID, p300/CBP, MDM2); target of the E3 ubiquitin ligase MDM2 (negative regulator of p53)

2. **Proline-rich region (aa 60-90):** PXXP motifs; important for apoptotic signaling and protein interactions (SH3 domain binding)

3. **DNA-binding domain (DBD, aa 94-292):** Core domain; recognizes a specific consensus sequence (two half-sites: RRRCWWGYYY, where R=purine, W=A/T, Y=pyrimidine); most cancer mutations (~90%) occur here; hotspot codons: R175H, G245S, R248W, R248Q, R249S, R273H, R282W — all contact DNA or maintain DBD conformation

4. **Tetramerization domain (TET, aa 323-356):** Forms dimers-of-dimers (D2D2) → tetramer; oligomeric state regulates DNA-binding affinity and transcriptional activity

5. **C-terminal regulatory domain (CTD, aa 356-393):** Negative regulatory domain; subject to post-translational modifications (acetylation, methylation, ubiquitination) that modulate p53 activity; contains nuclear localization signals (NLS)

### MDM2 — the principal negative regulator

Under normal conditions, p53 protein is extremely short-lived (~20 min half-life): **MDM2** (an E3 ubiquitin ligase, also a p53 transcriptional target) binds p53's N-terminal TAD → ubiquitination of p53's CTD → proteasomal degradation. This creates a **negative feedback loop** keeping basal p53 levels low.

Stress signals disrupt MDM2–p53 interaction through **post-translational modifications**:
- **Phosphorylation:** ATM/ATR kinases phosphorylate p53 at Ser15 and Ser20 (disrupts MDM2 binding) in response to DNA double-strand breaks; CHK1/CHK2 phosphorylate Ser20
- **Acetylation:** p300/CBP acetylates C-terminal lysines (K370, K372, K373, K381, K382) → enhanced DBD activity; competes with MDM2-mediated ubiquitination at same lysines
- Result: p53 stabilizes, tetramerizes, and transactivates target genes

## Function

### Stress sensing and activation

**Upstream activating signals → p53 activation:**
- **DNA damage (DSBs):** ATM → CHK2 → p53 Ser15/Ser20 phosphorylation (also direct ATM phosphorylation at Ser15); MDM2 also phosphorylated by ATM → impaired MDM2 E3 activity
- **Oncogene activation (Ras, Myc, E2F1):** ARF (p14^ARF^, encoded by CDKN2A locus) induced by oncogene signals → binds MDM2 → sequesters MDM2 in nucleolus → p53 released from degradation
- **Hypoxia:** HIF-1α and p53 interact; VHL-dependent pVHL binds p53 C-terminus and promotes its activity in hypoxic cells; hypoxia can also activate p53 via ATR/REDD1-dependent pathways
- **Nucleolar stress (ribosomal stress):** RPL5, RPL11 bind MDM2 when rDNA transcription is impaired → MDM2 inhibition → p53 activation
- **Metabolic stress:** AMPK activated by energy depletion → MDM2 phosphorylation → p53 stabilization

### Transcriptional outputs — the p53 target gene network

p53 binds **response elements (RE)** in target gene promoters and transactivates hundreds of genes [^levine-2020-p53-metabolism]:

**Cell-cycle arrest:**
- **p21 (CDKN1A):** CDK inhibitor; binds and inhibits CDK2/cyclin E and CDK4/cyclin D → G1 arrest; also inhibits CDK1/cyclin B → G2/M arrest; most reliably induced p53 target
- **GADD45A:** Promotes G2/M checkpoint; interacts with PCNA and CDK1/cyclin B

**Apoptosis — intrinsic pathway:**
- **PUMA (BBC3):** BCL-2 homology domain 3 (BH3)-only protein; the dominant pro-apoptotic p53 target; binds all anti-apoptotic BCL-2 family members → releases BAX/BAK → mitochondrial outer membrane permeabilization (MOMP) → cytochrome c → caspase-9 → executioner caspases
- **NOXA (PMAIP1):** BH3-only; selectively binds MCL-1 and BCL-XL
- **BAX:** Direct p53 target; also directly translocates to mitochondria upon p53 activation
- **Apoptosis-inducing factor (AIF):** Caspase-independent apoptosis

**Senescence:**
- Prolonged p21 induction + positive feedback through p16^INK4a^/RB axis → permanent senescence; senescent cells remain metabolically active but cannot divide → tumor suppressive barrier but also contributes to aging (senescence-associated secretory phenotype, SASP)

**DNA repair:**
- **XPC, DDB2:** Nucleotide excision repair; induced by p53 after UV damage
- **FANCC:** Fanconi anemia pathway (interstrand crosslink repair)

**Metabolic reprogramming:**
- **TIGAR:** TP53-induced glycolysis and apoptosis regulator; inhibits PFK-2 → decreases glycolysis → increases PPP → reduces ROS; allows cells to survive mild stress (DNA repair time)
- **SCO2:** Cytochrome c oxidase assembly factor; promotes OXPHOS over glycolysis in p53-WT cells — opposite of Warburg effect

### p53-independent functions

Non-transcriptional p53 activity: cytoplasmic p53 directly promotes **BAX oligomerization** at the mitochondrial membrane (transcription-independent apoptosis); also directly inhibits mitophagy and autophagy via interaction with Beclin1.

## Mechanism

### TP53 mutation in cancer

Approximately 50% of cancers carry TP53 mutations; virtually all mutations are **missense** point mutations in the DBD (unlike most tumor suppressors which are truncated/deleted). Two categories:

1. **Loss-of-function (LOF) mutations:** Abolish p53 transcriptional activity; cells lose checkpoint responses — cells with DNA damage continue dividing → genomic instability → tumor progression. All hotspot mutations (R175H, R248W, R248Q, R273H, etc.) cause LOF.

2. **Gain-of-function (GOF) mutations:** Subset of LOF mutations additionally acquire novel oncogenic activities — transactivating genes not normally p53 targets (PDGFRB, NOS2), interacting with and inhibiting other tumor suppressors (p63, p73), promoting invasion, metastasis, and drug resistance. R175H and R273H are the most studied GOF mutants.

**Li-Fraumeni syndrome:** Germline TP53 mutations → inherited predisposition to multiple early-onset cancers (breast, sarcoma, brain, adrenocortical carcinoma, leukemia); pattern of malignancies called the **SBLA syndrome**. Inheritance of one mutant TP53 allele (LOH of the second allele in tumors).

### MDM2 amplification

In ~7% of cancers (especially sarcomas), **MDM2 is amplified** → excessive p53 degradation despite WT TP53. These tumors are sensitive to **MDM2 inhibitors** (Nutlins — idasanutlin, navtemadlin, milademetan) that block MDM2–p53 interaction → p53 reactivation → tumor cell apoptosis. Nutlins show efficacy in WT p53 cancers (MDM2-amplified sarcomas, AML, neuroblastoma).

### p53 reactivation strategies in cancer therapy

- **MDM2 inhibitors (Nutlins):** For MDM2-amplified/overexpressing cancers with WT TP53
- **APR-246 (Eprenetapopt):** Small molecule that covalently modifies mutant p53 DBD cysteines → restores WT folding and transcriptional activity; in clinical trials for TP53-mutant AML, MDS, and ovarian cancer
- **PRIMA-1^MET^:** Converts mutant p53 to WT-like conformation

## Connections

- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — p53 regulates neutrophil apoptosis after pathogen clearance; MDM2-mediated p53 suppression extends neutrophil survival during acute infection.
- `modulates` → **[Cytokine Storm](../../07-system/cytokine-storm/README.md)** — p53 suppresses NF-κB-driven inflammation; in hyperinflammatory states, p53 promotes apoptotic clearance of activated immune cells to limit cytokine storm severity.

[^lane-1992-guardian]: Lane DP. Cancer. p53, guardian of the genome. *Nature.* 1992;358(6381):15-16. [doi:10.1038/358015a0](https://doi.org/10.1038/358015a0) · [PubMed 1614522](https://pubmed.ncbi.nlm.nih.gov/1614522/)
[^vousden-2009-p53-review]: Vousden KH, Prives C. Blinded by the Light: The Growing Complexity of p53. *Cell.* 2009;137(3):413-431. [doi:10.1016/j.cell.2009.04.037](https://doi.org/10.1016/j.cell.2009.04.037) · [PubMed 19410540](https://pubmed.ncbi.nlm.nih.gov/19410540/)
[^levine-2020-p53-metabolism]: Levine AJ. p53: 800 million years of evolution and 40 years of discovery. *Nat Rev Cancer.* 2020;20(8):471-480. [doi:10.1038/s41568-020-0262-1](https://doi.org/10.1038/s41568-020-0262-1) · [PubMed 32404993](https://pubmed.ncbi.nlm.nih.gov/32404993/)
