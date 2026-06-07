---
schema: human-scale-entry/v1
id: tert
name: TERT
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Catalytic subunit of telomerase; adds TTAGGG repeats to telomeres, preventing replicative senescence. Silenced in somatic cells; reactivated in ~90% of cancers via TERT promoter mutations (C228T/C250T) or MYC amplification — oncogenic drivers in GBM, melanoma, and bladder cancer."
aliases: ["telomerase reverse transcriptase", "TERT promoter mutation", "telomerase", "TP1", "TRT", "hTERT"]
sources:
  - id: shay-2007-telomeres-ageing
    type: peer-reviewed
    cite: "Shay JW, Wright WE. Hallmarks of telomeres in ageing research. J Pathol. 2007;211(2):114-123."
    doi: "10.1002/path.2090"
    pmid: "17200946"
    url: "https://doi.org/10.1002/path.2090"
  - id: huang-2013-tert-melanoma
    type: peer-reviewed
    cite: "Huang FW, Hodis E, Xu MJ, Kryukov GV, Chin L, Garraway LA. Highly recurrent TERT promoter mutations in human melanoma. Science. 2013;339(6122):957-959."
    doi: "10.1126/science.1229259"
    pmid: "23348506"
    url: "https://doi.org/10.1126/science.1229259"
  - id: barthel-2017-tert-pancancer
    type: peer-reviewed
    cite: "Barthel FP, Wei W, Tang M, et al. Systematic analysis of telomere length and somatic alterations in 31 cancer types. Nat Genet. 2017;49(3):349-357."
    doi: "10.1038/ng.3781"
    pmid: "28135248"
    url: "https://doi.org/10.1038/ng.3781"
cross_links:
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC is the primary TERT transcriptional activator; c-MYC binds E-boxes in the TERT promoter → telomerase reactivation in MYC-amplified tumors; telomere maintenance is required for MYC-driven immortalization and protects against MYC-induced replicative stress."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 represses TERT transcription; telomere shortening → p53-dependent senescence in normal cells; TERT reactivation circumvents p53-mediated senescence; concurrent p53 loss and TERT promoter mutation cooperate for full malignant transformation in GBM and melanoma."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1alpha transcriptionally activates TERT in hypoxic tumor cells via HRE elements in the TERT promoter; TERT in turn activates HIF-1alpha target genes by non-canonical mitochondrial mechanisms → mutual reinforcement under hypoxia."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS activates TERT expression via ERK → AP-1/ETS factors binding the TERT promoter; TERT promoter mutations and KRAS co-occur in CRC and PDAC; KRAS-driven replicative stress → telomere dysfunction → dependency on TERT for genome stabilization."
---

# TERT

## Overview

**TERT (telomerase reverse transcriptase)** is the **catalytic protein subunit** of the **telomerase holoenzyme** — a ribonucleoprotein complex that maintains telomere length by adding hexanucleotide **TTAGGG repeats** to chromosome ends, directly opposing the end-replication problem that causes progressive telomere shortening with each cell division [^shay-2007-telomeres-ageing].

**Telomerase holoenzyme components:**
- **TERT (catalytic reverse transcriptase):** Uses RNA template → DNA synthesis; rate-limiting component in most cells
- **TERC (TR, hTR):** Non-coding RNA template (5'-AAUCCC-3' repeat template region); ~451 nt in humans; provides the template for TTAGGG synthesis
- **Dyskerin (DKC1):** Pseudouridine synthase; stabilizes TERC; mutations in DKC1 → dyskeratosis congenita (telomere maintenance syndrome)
- **Additional proteins:** NHP2, NOP10, GAR1 (H/ACA RNP complex) → TERC stabilization; TCAB1 (Cajal body localization of TERC); POT1-TPP1-TIN2-RAP1-TRF1-TRF2 (shelterin complex protecting telomere ends from DDR activation)

**TERT in normal biology:**
- **Germline and stem cells:** High TERT expression → telomere length maintenance → unlimited self-renewal potential; essential for spermatogenesis, hematopoietic stem cell maintenance, intestinal crypt cell renewal
- **Somatic differentiated cells:** TERT silenced in virtually all normal somatic cells → progressive telomere shortening (~50-200 bp/division) → replicative senescence after ~50-70 population doublings (Hayflick limit)
- **Senescence and aging:** Short telomeres → p53/p21-mediated G1 arrest (senescence); telomere length inversely correlates with biological aging; constitutional TERT mutations → short telomeres → telomere biology disorders (TBDs): dyskeratosis congenita, aplastic anemia, pulmonary fibrosis (IPF), hepatic fibrosis, bone marrow failure

**TERT reactivation in cancer (~90% of cancers):**
- Telomere shortening in pre-cancerous cells → chromosomal instability (breakage-fusion-bridge cycles) → oncogenic mutations; TERT reactivation at critical telomere shortening → immortalization → allows cancer cells to maintain telomeres indefinitely
- **Alternative lengthening of telomeres (ALT, ~10-15% of cancers):** TERT-independent telomere maintenance via homologous recombination-mediated template switching; common in soft tissue sarcomas, osteosarcoma, glioblastoma; associated with ATRX/DAXX mutations; can be identified by ALT-associated PML bodies (APBs) and C-circle assay
- **Together:** TERT reactivation or ALT is required in >95% of malignant tumors — a near-universal cancer hallmark

## Structure

### TERT protein domains [^shay-2007-telomeres-ageing]

TERT is a **1,132 amino acid** reverse transcriptase with a canonical RRRP (RNA-binding, fingers, palm, thumb) domain architecture:

**N-terminal extension (NTE, aa 1-350):**
- Contains DAT (dissociates activities of telomerase) region → mediates TERT association with shelterin proteins (TPP1 OB fold via TEN domain); essential for recruitment of telomerase to telomeres in vivo; TERT Lys570 → nuclear localization

**RNA-binding domain (TRBD, aa 350-516):**
- Cp/TRBD motif → binds TERC pseudoknot and CR4/CR5 domain; mutations here → selective loss of processivity (telomerase adds only a few repeats rather than continuous synthesis)

**Reverse transcriptase (RT) domain (aa 600-900):**
- RFLVP motif, FYLI motif, catalytic Asp-Asp in palm → RNA-dependent DNA polymerase activity; conserved with retroviral RT but uniquely adapted for telomeric repeat synthesis; lacks RNase H activity; uses TERC template for TTAGGG synthesis
- **TERT inhibitors target this domain:** BIBR1532 (non-competitive RT inhibitor, research tool); GRN163L (imetelstat, antisense oligonucleotide targeting TERC template) — clinically most advanced

**C-terminal extension (CTE, aa 900-1132):**
- Thumb domain → template/primer positioning; IFD (insertion in fingers domain) unique to telomerase → processivity and template translocation; interaction with TPP1/POT1 for chromosome end protection at telomere

### TERT promoter mutations — oncogenic drivers [^huang-2013-tert-melanoma]

The TERT gene promoter contains two hotspot mutation positions discovered in 2013 simultaneously in melanoma:

**C228T and C250T:**
- Located at -124 bp and -146 bp upstream of the TERT ATG start codon
- Create de novo E26 transformation-specific (ETS) transcription factor binding motifs (5'-CCGGAA-3') → ETS family TFs (GABPA/GABPB1) bind the new site → TERT transcriptional upregulation (~2-4× above baseline in normal cells)
- **Cancer-type frequency:** Melanoma (70-80%), GBM (80-85%), bladder/urothelial cancer (60-70%), papillary thyroid cancer (~10%), hepatocellular carcinoma (~25%), meningioma (5%)
- **Clinical significance:** TERT promoter mutations are early oncogenic events (melanoma in situ can harbor them) and associate with worse prognosis in glioma and bladder cancer; detected in liquid biopsy ctDNA
- **IDH-wild-type GBM:** TERT promoter mutation + EGFR amplification/PTEN loss is the dominant molecular signature of IDH-wt GBM and combined with IDH mutation status to classify WHO Grade 4 glioblastoma vs. Grade 3 IDH-mutant astrocytoma

## Function

### Telomere biology and cancer immortalization

**The senescence barrier and TERT bypass:**
Somatic cells: progressive telomere shortening → at critically short telomeres → DDR activation (ATM/ATR → p53/Rb → p21/p16) → replicative senescence (M1) → if p53/Rb bypassed → further shortening → chromosome fusions → crisis (M2) → genome chaos → TERT reactivation → escape from crisis → malignant immortalization

**Telomere length in cancer biology:**
- Short telomeres → chromosomal instability (CIN) → oncogenic copy number alterations → early cancer driver; TERT reactivation then stabilizes the genome for tumor propagation
- **Pan-cancer analysis:** Cancers with TERT reactivation have significantly shorter telomeres than matched normal tissue; telomere length restoration tracks with TERT expression levels [^barthel-2017-tert-pancancer]

**Non-canonical TERT functions (beyond telomere maintenance):**
- **Mitochondrial function:** TERT localizes to mitochondria under oxidative stress → reduces mitochondrial ROS and improves respiratory efficiency → anti-apoptotic; mitochondrial TERT does not require TERC
- **Wnt/beta-catenin:** Nuclear TERT associates with BRG1 (chromatin remodeler) → epigenetically activates Wnt target genes independent of telomere synthesis → stem cell self-renewal programs
- **NF-kB activation:** TERT translocates to nucleus under NF-kB activation → binds NF-kB RelA → prolongs NF-kB target gene transcription → survival and inflammatory signaling
- **RNA-dependent RNA polymerase:** TERT + TERC → dicer-substrate RNA → siRNA → gene silencing (RMRP); controversial but may contribute to epigenetic regulation

### TERT in telomere biology disorders (TBDs)

Autosomal dominant or X-linked mutations in telomerase pathway genes (TERT, TERC, DKC1, NHP2, NOP10, RTEL1, PARN, ACD, NAF1) → accelerated telomere shortening → organ failure:
- **Dyskeratosis congenita (DC):** Skin pigmentation, nail dystrophy, oral leukoplakia (triad); bone marrow failure, pulmonary fibrosis, liver cirrhosis; highest risk in DKC1 (X-linked) mutations; most severe when TERT mutations are compound heterozygous
- **Idiopathic pulmonary fibrosis (IPF):** 20-25% of familial IPF due to TERT or TERC mutations; short telomeres → type II pneumocyte senescence → impaired alveolar repair → fibrosis; telomerase gene mutations are the most common genetic cause of familial IPF
- **Aplastic anemia:** Short telomeres → hematopoietic stem cell exhaustion; may respond to androgens (danazol) → upregulate TERT expression → extend telomeres modestly → improve blood counts
- **Hereditary liver disease:** TERT/TERC mutations → hepatic stellate cell and hepatocyte telomere dysfunction → cirrhosis

## Mechanism

### Therapeutic targeting

**Imetelstat (GRN163L, Rytelo):**
- 13-mer thiophosphoramidate oligonucleotide complementary to TERC template region → competitive inhibition of TERT catalytic activity → progressive telomere shortening → cancer cell senescence/apoptosis over weeks-months
- FDA approved 2024 for **transfusion-dependent low-risk myelodysplastic syndrome (MDS)** and **relapsed/refractory myelofibrosis** (IMbark, IMerge trials); mechanism: MDS stem cells are telomerase-dependent; imetelstat selectively depletes malignant HSCs with short telomeres
- Key adverse effect: myelosuppression (thrombocytopenia, neutropenia) — dose-limiting; managed with growth factors and dose modification; avoids normal telomerase-independent HSC reserve

**TERT promoter mutations as liquid biopsy targets:**
- ctDNA assays detecting C228T/C250T: highly specific for cancer (near-absent in cfDNA from healthy individuals) → diagnostic/monitoring utility in GBM (CSF liquid biopsy), urothelial cancer (urine ctDNA), and melanoma
- Tumor volume correlates with TERT promoter mutation allele fraction in ctDNA; clearance post-resection; emergence at relapse

**TERT mRNA vaccines (investigational):**
- TERT is a shared tumor antigen (expressed in most cancers, absent in most normal cells) → target for cancer vaccines; TERT peptide vaccines (GX-188E for HPV+ cervical) and mRNA vaccines in clinical trials for GBM and NSCLC; limited by central tolerance against self-antigen

## Connections

- `connects-to` → **[MYC](../myc/README.md)** — MYC is the primary TERT transcriptional activator; c-MYC binds E-boxes in the TERT promoter → telomerase reactivation in MYC-amplified tumors; telomere maintenance is required for MYC-driven immortalization and protects against MYC-induced replicative stress.
- `connects-to` → **[p53](../p53/README.md)** — p53 represses TERT transcription; telomere shortening → p53-dependent senescence in normal cells; TERT reactivation circumvents p53-mediated senescence; concurrent p53 loss and TERT promoter mutation cooperate for full malignant transformation in GBM and melanoma.
- `connects-to` → **[HIF-1alpha](../hif-1alpha/README.md)** — HIF-1alpha transcriptionally activates TERT in hypoxic tumor cells via HRE elements in the TERT promoter; TERT activates HIF-1alpha target genes by non-canonical mitochondrial mechanisms → mutual reinforcement under hypoxia.
- `connects-to` → **[KRAS](../kras/README.md)** — KRAS activates TERT expression via ERK → AP-1/ETS factors; TERT promoter mutations and KRAS co-occur in CRC and PDAC; KRAS-driven replicative stress → telomere dysfunction → dependency on TERT for genome stabilization.

[^shay-2007-telomeres-ageing]: Shay JW, Wright WE. Hallmarks of telomeres in ageing research. *J Pathol.* 2007;211(2):114-123. [doi:10.1002/path.2090](https://doi.org/10.1002/path.2090) · [PubMed 17200946](https://pubmed.ncbi.nlm.nih.gov/17200946/)
[^huang-2013-tert-melanoma]: Huang FW, Hodis E, Xu MJ, Kryukov GV, Chin L, Garraway LA. Highly recurrent TERT promoter mutations in human melanoma. *Science.* 2013;339(6122):957-959. [doi:10.1126/science.1229259](https://doi.org/10.1126/science.1229259) · [PubMed 23348506](https://pubmed.ncbi.nlm.nih.gov/23348506/)
[^barthel-2017-tert-pancancer]: Barthel FP, Wei W, Tang M, et al. Systematic analysis of telomere length and somatic alterations in 31 cancer types. *Nat Genet.* 2017;49(3):349-357. [doi:10.1038/ng.3781](https://doi.org/10.1038/ng.3781) · [PubMed 28135248](https://pubmed.ncbi.nlm.nih.gov/28135248/)
