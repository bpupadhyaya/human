---
schema: human-scale-entry/v1
id: dicer1
name: DICER1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "DICER1 is the dsRNA endonuclease that processes pre-miRNA to mature miRNA via RNase IIIa (3p) and RNase IIIb (5p) cleavage; somatic RNase IIIb hotspot mutations selectively impair 5p miRNA production; germline LOF + hotspot second hit = DICER1 syndrome tumors."
aliases: ["DICER1", "Dicer", "DICER1 RNase III", "DICER1 miRNA", "DICER1 tumor", "DICER1 hotspot", "DICER1 PPB", "DICER1 syndrome gene", "RNase IIIb DICER1"]
sources:
  - id: hill-2009-dicer1
    type: peer-reviewed
    cite: "Hill DA, Ivanovich J, Priest JR, et al. DICER1 mutations in familial pleuropulmonary blastoma. Science. 2009;325(5943):965."
    doi: "10.1126/science.1174334"
    pmid: "19556464"
    url: "https://doi.org/10.1126/science.1174334"
  - id: foulkes-2014-dicer1
    type: peer-reviewed
    cite: "Foulkes WD, Priest JR, Duchaine TF. DICER1: mutations, microRNAs and mechanisms. Nat Rev Cancer. 2014;14(10):662-672."
    doi: "10.1038/nrc3802"
    pmid: "25176334"
    url: "https://doi.org/10.1038/nrc3802"
cross_links:
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "DICER1 syndrome is caused by germline DICER1 LOF + somatic RNase IIIb hotspot second hit; sentinel tumors include PPB (infancy-8y), cystic nephroma, ovarian SLCT, and multinodular goiter; hotspot mutations (E1705, D1709, E1813) specifically impair 5p miRNA biogenesis."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "MYCN amplification occurs as a somatic driver in PPB type III (solid, high-grade); DICER1 5p miRNA loss (let-7, miR-17 family) derepresses MYCN/MYC oncoproteins → RB pathway bypass; MYCN-amplified PPB type III has the worst prognosis (5-year OS ~53%) among PPB types."
  - target: 01-human/07-system/ovarian-cancer
    relation: connects-to
    note: "DICER1 RNase IIIb hotspot mutations drive ~60% of ovarian Sertoli-Leydig cell tumors (SLCT); somatic hotspot in most SLCT; germline DICER1 carriers have elevated SLCT risk; SLCT is androgenic (virilization); BEP chemotherapy (bleomycin-etoposide-cisplatin) for advanced SLCT."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Multinodular goiter occurs in ~75% of DICER1 germline carriers; differentiated thyroid carcinoma (papillary, follicular) risk is modestly elevated; DICER1 somatic hotspot mutations identified in a subset of poorly differentiated and anaplastic thyroid cancer."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "PPB (pleuropulmonary blastoma) is the sentinel DICER1 syndrome tumor arising in the lung; type I cystic (best prognosis) → type II mixed → type III solid (5-year OS ~53%); all types arise under age 8 in germline DICER1 LOF carriers; treatment: lung resection + chemotherapy."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Advanced DICER1 tumors acquire TP53 mutations during high-grade progression; DICER1 5p miRNA loss derepresses MYC/MYCN → replicative stress → p53 activation → TP53 selection; TP53 mutation is the most unfavorable prognostic marker in DICER1-related tumor progression."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "DICER1 somatic RNase IIIb hotspot mutations occur in ~5-10% of Wilms tumors; cystic nephroma (DICER1 syndrome manifestation) can progress to nephroblastoma; germline DICER1 carriers have modestly elevated Wilms tumor risk; DICER1-mutant Wilms tumor may have favorable histology."
---

# DICER1

## Overview

**DICER1** (Double-stranded RNA-specific endoribonuclease) is a 1922 amino acid (218 kDa) **RNase III family endoribonuclease** that is the central enzyme in **microRNA (miRNA) biogenesis** in vertebrates. DICER1 processes **pre-miRNA** (precursor miRNA hairpin structures exported from the nucleus by Exportin-5/RAN-GTP) into the ~22 nucleotide mature miRNA duplex. Each mature miRNA is then loaded onto the RNA-induced silencing complex (RISC) to direct mRNA cleavage or translational repression of hundreds of target transcripts. DICER1 therefore acts as a **global regulator of gene expression programs** through miRNA-mediated post-transcriptional silencing. Germline DICER1 mutations were identified as the cause of **familial pleuropulmonary blastoma (PPB)** by Hill et al. in 2009, establishing DICER1 as a human tumor predisposition gene and the founding cause of **DICER1 syndrome** [^hill-2009-dicer1] [^foulkes-2014-dicer1].

**miRNA biogenesis — canonical pathway:**

```
Nucleus:                          Cytoplasm:
Pri-miRNA (RNA Pol II)           Pre-miRNA hairpin
  → DROSHA-DGCR8 cleavage           (~60-70 nt)
  → Pre-miRNA hairpin                    ↓ DICER1
  → Exportin-5 export            miRNA:miRNA* duplex
                                       ↓ AGO2/RISC
                              Mature miRNA-5p (guide) loaded
                              miRNA-3p (passenger) degraded
                                       ↓
                              mRNA silencing (3'UTR binding)
```

DICER1 performs two sequential cleavage events:
- **RNase IIIa domain**: cleaves the 3p arm of the pre-miRNA hairpin (generates the miRNA-3p strand end)
- **RNase IIIb domain**: cleaves the 5p arm of the pre-miRNA hairpin (generates the miRNA-5p strand end)
- **Result**: a ~22 bp RNA duplex with 2-nt 3' overhangs on both ends; the guide (usually 5p) strand is loaded into AGO2-RISC; the passenger (usually 3p) strand is typically degraded

## Structure

### DICER1 protein domains

**N-terminal helicase domain (DExD/H box; aa 1-600):**
- Contains DEAD-box ATPase helicase; required for unwinding of perfectly paired dsRNA substrates; contributes to processivity and dsRNA selection; not required for pre-miRNA cleavage (miRNA substrates are imperfect hairpins)
- Helicase domain interfaces with TRBP (TARBP2) and PACT/PRKRA — cofactors that enhance DICER1 activity and assist in loading the guide strand into AGO2
- Germline frameshift/nonsense mutations in this domain: LOF → haploinsufficiency

**Platform domain + PAZ domain (aa 600-900):**
- PAZ domain (Piwi-Argonaute-Zwille): binds the 2-nt 3' overhang of pre-miRNA — serves as a molecular ruler measuring exactly 2 nt from the 3' end to position the pre-miRNA for cleavage
- Platform domain: structural scaffold connecting helicase domain to the two-lobed RNase III fold
- PAZ-to-RNase III distance (~65 Å) determines the ~22 nt cleavage product length — effectively a molecular ruler

**RNase IIIa domain (aa 1200-1450):**
- Catalyzes cleavage of the **3p arm** of the pre-miRNA duplex
- Contains two Mg²⁺-binding residues (D1320, E1322) in the catalytic center
- Mutations in RNase IIIa: relatively uncommon in DICER1 syndrome; do not show "hotspot" clustering

**RNase IIIb domain (aa 1450-1650):**
- Catalyzes cleavage of the **5p arm** of the pre-miRNA duplex
- Contains metal-binding residues critical for catalysis: **E1705, D1709, E1813, D1810, G1809** — these are the **DICER1 hotspot residues** where somatic missense mutations cluster in DICER1 syndrome tumors
- Hotspot missense variants (E1705K/D/Q/G, D1709N, E1813K/D/G, etc.) disable 5p arm cleavage while preserving 3p arm cleavage → selective depletion of **miRNA-5p family** (let-7-5p, miR-17-5p, miR-20a-5p, miR-25-5p) → specific downstream oncogenic program

**dsRNA-binding domain (dsRBD; aa 1750-1922):**
- C-terminal; non-specific dsRNA binding; stabilizes the DICER1-pre-miRNA interaction
- Also mediates interaction with TRBP (trans-activating response RNA binding protein)

**The DICER1 two-hit mechanism — why hotspot missense ≠ second LOF:**

In conventional tumor suppressors, both hits cause LOF. DICER1 is unusual:
1. **First hit (germline)**: Frameshift/nonsense → LOF → haploinsufficiency; one functional DICER1 allele remains
2. **Second hit (somatic)**: NOT a second LOF — instead, a **missense hotspot** in the RNase IIIb metal-binding center → the mutant allele retains partial DICER1 activity (3p cleavage preserved) but selectively loses 5p miRNA processing

This creates a **specific miRNA deficiency signature** rather than complete miRNA loss:
- miRNA-5p family members (let-7, miR-17, miR-200 family) are selectively depleted
- Derepresses LIN28 (let-7 target), MYCN, MYC, E2F family oncoproteins
- Biologically distinct from complete DICER1 loss (which is embryonic lethal in mice)

## Function

### DICER1 in development and homeostasis

DICER1 is essential for vertebrate development: constitutive Dicer1 knockout in mice → embryonic lethal (E7.5). Conditional Dicer1 knockout in specific lineages:
- Neural progenitors: impaired cortical layering, microcephaly
- Lung epithelium: pulmonary hypoplasia (relevant to PPB biology)
- Ovarian granulosa cells: infertility, polycystic ovary-like phenotype
- Thyroid follicular cells: goiter, altered thyroid hormone synthesis

DICER1 haploinsufficiency (one functional allele) is well-tolerated in most tissues but creates susceptibility for somatic second-hit mutations in specific progenitor cell populations.

### DICER1 and tumor suppression

DICER1 functions as a **context-dependent tumor suppressor** through several mechanisms:

**let-7 family miRNAs:**
let-7-5p (let-7a, let-7b, let-7c, let-7d, let-7e, let-7f, let-7g, let-7i) collectively repress multiple oncoproteins:
- **KRAS, NRAS, HRAS** (let-7 seed matches in 3'UTR)
- **MYC, MYCN** (let-7 binding → reduced translation)
- **LIN28A/B** (let-7 target + lin28 reciprocally represses let-7 → double-negative loop)
- **IGF2BP1/2/3** (oncofetal RNA binding proteins promoted by let-7 loss)

DICER1 hotspot → selective let-7-5p depletion → derepression of KRAS, LIN28, MYCN → oncogenic proliferation

**miR-17-92 cluster (oncomiR) and miR-200 family:**
- miR-17-5p and miR-20a-5p (from miR-17-92 cluster) are processed from the 5p arm → depleted by RNase IIIb hotspot
- Despite miR-17-92 being an oncomiR when overexpressed, the loss of its 5p arm products in DICER1-mutant contexts may paradoxically reflect miRNA biogenesis dysregulation rather than straightforward tumor suppressor loss
- miR-200 family (5p): EMT suppression — derepressed ZEB1/ZEB2 (E-cadherin repressors) in DICER1-mutant tumors

## Mechanism

### Somatic DICER1 hotspot mutation detection

DICER1 hotspot mutations are detectable in tumor DNA by:
- NGS panels targeting exons 24-26 (RNase IIIb domain)
- Liquid biopsy (ctDNA): being evaluated for PPB surveillance
- IHC: not applicable (no validated antibody surrogate)

Germline DICER1 testing: full gene sequencing + MLPA for large deletions; panel-based (next-gen multigene panel including DICER1 + associated miRNA pathway genes)

**Clinical significance of somatic hotspot detection:**
Finding a DICER1 RNase IIIb hotspot mutation in a pediatric tumor (PPB, cystic nephroma, SLCT, cervical RMS) should prompt:
1. Germline DICER1 testing of the patient
2. Cascade testing of parents and siblings (autosomal dominant, 50% risk)
3. Surveillance protocol initiation for germline carriers

**DICER1-independent miRNA pathway:**
In DICER1-null cells (second allele also lost via LOH), essentially no mature miRNA is produced — this state is more severely growth-inhibitory than hotspot mutations. Rare tumors with complete biallelic DICER1 LOF exist but are uncommon (the hotspot model is more frequent because complete LOF is too growth-suppressive without additional genetic drivers).

## Connections

- `connects-to` → **[DICER1 Syndrome](../../07-system/dicer1-syndrome/README.md)** — DICER1 syndrome is caused by germline DICER1 LOF + somatic RNase IIIb hotspot second hit; sentinel tumors include PPB (infancy-8y), cystic nephroma, ovarian SLCT, and multinodular goiter; hotspot mutations (E1705, D1709, E1813) specifically impair 5p miRNA biogenesis.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — MYCN amplification occurs as a somatic driver in PPB type III (solid, high-grade); DICER1 5p miRNA loss (let-7, miR-17 family) derepresses MYCN/MYC oncoproteins → RB pathway bypass; MYCN-amplified PPB type III has the worst prognosis (5-year OS ~53%) among PPB types.
- `connects-to` → **[Ovarian Cancer](../../07-system/ovarian-cancer/README.md)** — DICER1 RNase IIIb hotspot mutations drive ~60% of ovarian Sertoli-Leydig cell tumors (SLCT); somatic hotspot in most SLCT; germline DICER1 carriers have elevated SLCT risk; SLCT is androgenic (virilization); BEP chemotherapy (bleomycin-etoposide-cisplatin) for advanced SLCT.
- `connects-to` → **[Thyroid Cancer](../../07-system/thyroid-cancer/README.md)** — Multinodular goiter occurs in ~75% of DICER1 germline carriers; differentiated thyroid carcinoma (papillary, follicular) risk is modestly elevated; DICER1 somatic hotspot mutations identified in a subset of poorly differentiated and anaplastic thyroid cancer.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — PPB (pleuropulmonary blastoma) is the sentinel DICER1 syndrome tumor arising in the lung; type I cystic → type II mixed → type III solid (5-year OS ~53%); all types arise under age 8 in germline DICER1 LOF carriers; lung resection + chemotherapy is primary treatment.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — advanced DICER1 tumors acquire TP53 mutations during high-grade progression; DICER1 5p miRNA loss derepresses MYC/MYCN → replicative stress → p53 activation → TP53 selection; TP53 mutation is the most unfavorable prognostic marker in DICER1-related tumors.
- `connects-to` → **[Wilms Tumor](../../07-system/wilms-tumor/README.md)** — DICER1 somatic RNase IIIb hotspot mutations occur in ~5-10% of Wilms tumors; cystic nephroma (DICER1 syndrome manifestation) can progress to nephroblastoma; germline DICER1 carriers have modestly elevated Wilms tumor risk.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^hill-2009-dicer1]: Hill DA, Ivanovich J, Priest JR, et al. DICER1 mutations in familial pleuropulmonary blastoma. *Science.* 2009;325(5943):965. [doi:10.1126/science.1174334](https://doi.org/10.1126/science.1174334) · [PubMed 19556464](https://pubmed.ncbi.nlm.nih.gov/19556464/)
[^foulkes-2014-dicer1]: Foulkes WD, Priest JR, Duchaine TF. DICER1: mutations, microRNAs and mechanisms. *Nat Rev Cancer.* 2014;14(10):662-672. [doi:10.1038/nrc3802](https://doi.org/10.1038/nrc3802) · [PubMed 25176334](https://pubmed.ncbi.nlm.nih.gov/25176334/)
