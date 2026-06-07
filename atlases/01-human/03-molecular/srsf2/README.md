---
schema: human-scale-entry/v1
id: srsf2
name: SRSF2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "SRSF2 encodes a spliceosome serine-arginine protein; P95H hotspot alters CCNG exonic splicing enhancer recognition → aberrant mRNA splicing; SRSF2 P95H mutations occur in ~45% of CMML (with TET2 co-mutation), ~15% of MDS, and ~11% of PTCL; no direct targeted therapy."
aliases: ["SRSF2", "SC35", "serine-arginine splicing factor 2", "SRSF2 P95H", "splicing factor mutation MDS", "splicing factor CMML", "spliceosome mutation", "SRSF2 myeloid"]
sources:
  - id: yoshida-2011-splicing
    type: peer-reviewed
    cite: "Yoshida K, Sanada M, Shiraishi Y, et al. Frequent pathway mutations of splicing machinery in myeloid diseases. Nature. 2011;478(7367):64-69."
    doi: "10.1038/nature10496"
    pmid: "21909114"
    url: "https://doi.org/10.1038/nature10496"
  - id: patnaik-2013-srsf2-cmml
    type: peer-reviewed
    cite: "Patnaik MM, Lasho TL, Finke CM, et al. Spliceosome mutations involving SRSF2, SF3B1, and U2AF35 in chronic myelomonocytic leukemia: prevalence, clinical correlates, and prognostic relevance. Am J Hematol. 2013;88(3):201-206."
    doi: "10.1002/ajh.23373"
    pmid: "23335075"
    url: "https://doi.org/10.1002/ajh.23373"
cross_links:
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "SRSF2 and DNMT3A mutations frequently co-occur in MDS and CMML; SRSF2 affects RNA processing while DNMT3A affects de novo DNA methylation; their co-occurrence drives more severe hematopoietic dysfunction; DNMT3A-SRSF2 doublet is common in therapy-related MDS/CMML."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "SRSF2 P95H alters EZH2 exon splicing → altered PRC2 isoform abundance; EZH2 and SRSF2 loss-of-function co-occur in MDS and CMML; both contribute to compound epigenetic dysfunction and accelerated AML transformation risk in MDS/CMML."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "SRSF2 regulates splicing of NF-κB pathway genes; aberrant SRSF2 → altered IKK splicing → constitutive NF-κB activation → monocyte proliferation in CMML; NF-κB is a key survival pathway in CMML blasts; JAK/STAT and NF-κB co-activation drive MP-CMML proliferation."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS/NRAS mutations co-occur with SRSF2 in ~15% of CMML; KRAS drives RAS-MAPK monocyte proliferation → MP-CMML phenotype (WBC >13×10⁹/L, splenomegaly); SRSF2+KRAS doublet → aggressive CMML; MEK inhibitor trametinib active in RAS-mutant CMML in early trials."
---

# SRSF2

## Overview

**SRSF2 (Serine/Arginine-Rich Splicing Factor 2, also known as SC35)** is a constitutively expressed RNA-binding protein and core component of the spliceosome responsible for exon recognition during pre-mRNA splicing. SRSF2 contains a single N-terminal RRM (RNA recognition motif) domain that recognizes **CCNG exonic splicing enhancer (ESE) sequences** and a C-terminal RS (arginine-serine) domain that mediates protein-protein interactions with other splicing factors and spliceosome assembly factors. SRSF2 recruits U1 snRNP (to the 5' splice site) and U2AF65 (to the 3' splice site) → promotes splice site definition → correct exon inclusion in mRNA. The landmark 2011 discovery that **splicing factor mutations** (in SRSF2, SF3B1, U2AF1, ZRSR2, SF3A1, PRPF40B) occur in the majority of myelodysplastic syndromes (~50-85%) revealed splicing dysregulation as a central oncogenic mechanism in myeloid malignancies [^yoshida-2011-splicing]. The canonical **SRSF2 P95H/R/L hotspot** occurs at a single proline residue in the RRM domain that specifically contacts the CCNG ESE sequence → altered nucleotide binding preference → genome-wide splicing errors [^patnaik-2013-srsf2-cmml].

**SRSF2 in hematologic malignancies:**
- **CMML (chronic myelomonocytic leukemia):** P95H in ~45% — the most common splicing factor mutation in CMML; occurs predominantly with TET2 (~60%) co-mutations; SRSF2+TET2 doublet in ~30% of all CMML; marks monocytic lineage expansion and dysplastic hematopoiesis
- **MDS:** SRSF2 P95H in ~15% of MDS; associated with CMML-like monocytosis; co-mutations with ASXL1 → aggressive MDS; worse prognosis than SF3B1-mutant MDS (favorable)
- **MF and ET (myeloproliferative neoplasms):** SRSF2 mutations in ~5-10% of MF, ~3% of ET; often co-mutated with JAK2 V617F; SRSF2+JAK2 V617F → worse prognosis in MF
- **Secondary AML (sAML):** SRSF2 mutations in ~15% of sAML arising from MDS/CMML; retained from the preceding MDS/CMML clone; persistence indicates same clonal origin; associated with lower CR rates than de novo AML
- **Peripheral T-cell lymphoma (PTCL):** SRSF2 mutations in ~11% of PTCL-NOS and ~15% of AITL; typically co-mutated with TET2, DNMT3A → shared pre-malignant T-cell clone biology (analogous to myeloid CHIP)
- **CHIP:** SRSF2 P95H in CHIP (~3%) is specifically associated with elevated cardiovascular risk (higher than DNMT3A-CHIP) and rapid progression to MDS/CMML vs. other CHIP mutations

## Structure

### SRSF2 protein architecture

SRSF2 is a 221-amino-acid, 25 kDa protein:

**RRM domain (1-101, RNA recognition motif):**
- Single RRM; contains two RNA-binding surface elements: RNP1 (octapeptide) and RNP2 (hexapeptide)
- **Proline 95 (P95):** Located in the β4 strand of the RRM, which contacts the second and third positions of the CCNG ESE consensus sequence; P95 (proline) maintains a rigid turn in the β-strand conformation; P95H substitution → imidazole (His) replaces cyclic pyrrolidine (Pro) → altered contact with cytosine C2 and guanine G3 of CCNG ESE → preferential binding of CCNG→CCGG sequences instead (gain-of-function for different ESE sequence)
- P95H is a gain-of-sequence-specificity mutation, NOT a loss-of-function: SRSF2 P95H protein is expressed, nuclear, and functional as a splicing factor but with altered sequence preference → aberrant splicing of transcripts bearing CCNG ESEs

**RS domain (101-221, arginine-serine domain):**
- Intrinsically disordered; extensively phosphorylated by SRPK1/2 (SR protein kinases) and CLK1/2/3/4 (CDC-like kinases) → phosphorylation regulates: SR protein nuclear localization, spliceosome complex assembly (interaction with U1-70K, U2AF35, U2AF65), mRNA export from nucleus

### P95H altered splicing targets

**Genome-wide consequences of SRSF2 P95H:**
Studies using SRSF2 P95H knockin mouse models and patient RNA-seq reveal: Aberrant cassette exon skipping and inclusion in thousands of transcripts; most severely affected are long transcripts with multiple exons (hematopoietic differentiation genes); the altered ESE preference (CCNG→CCGG) leads to predictable alternative splicing at affected sites.

**Key target transcripts (documented):**
- **EZH2:** SRSF2 P95H → exon 14 skipping of EZH2 mRNA → truncated EZH2 protein → partial PRC2 loss-of-function (phenocopies EZH2 mutation) → reduced H3K27me3 → derepression of myeloid differentiation genes
- **BCOR:** Altered splicing → BCOR isoform with reduced PRC1.1 complex activity → altered H2AK119 ubiquitination
- **ASXL1:** Aberrant SRSF2 splicing may affect ASXL1 mRNA → PR-DUB complex disruption
- **Dnmt3a:** Mouse knockin studies: Aberrant Dnmt3a exon inclusion → Dnmt3a protein isoform changes → altered DNA methylation patterns in HSCs
- **MYC targets:** Altered splicing of MYC target mRNAs → dysregulated proliferation signals

**SF3B1 vs. SRSF2 splicing pattern comparison:**
| Feature | SF3B1 K700E | SRSF2 P95H |
|---------|-------------|-------------|
| Primary alteration | 3' splice site preference | ESE sequence preference |
| Splicing change | Cryptic 3' SS activation | Cassette exon skipping/inclusion |
| Disease association | MDS-RS (ring sideroblasts) | CMML, MDS, PTCL |
| Prognosis | Favorable (in MDS) | Intermediate-adverse (CMML) |
| Unique feature | Ring sideroblasts | Monocytic differentiation bias |

## Function

### Normal SRSF2 roles in hematopoiesis

**Constitutive splicing regulation:**
SRSF2 is an "SR protein" — one of 7 classic SR splicing factors (SRSF1-7) that together regulate >95% of all alternative splicing events in human cells; SRSF2 is particularly enriched in hematopoietic progenitors and rapidly differentiating cells; essential for early embryonic development (SRSF2-null mice die at gastrulation).

**Hematopoietic stem cell maintenance:**
SRSF2 P95H knockin mice: Normal HSC numbers at young age → progressive HSC clonal expansion with monocytic skewing → myeloid dysplasia → CMML-like disease by 12-18 months; requires co-mutation with Tet2 for overt CMML penetrance (TET2 homozygous + SRSF2 P95H → CMML-like disease in 100% of mice at 6 months). This mouse model recapitulates the genetic architecture of human CMML (TET2+SRSF2 co-mutation).

**Monocytic lineage bias:**
SRSF2 P95H → altered splicing of monocyte/macrophage differentiation transcription factors (SPI1/PU.1 targets, IRF8 targets) → HSCs preferentially differentiate toward monocytic progenitors (GMP → cMOP → monocyte) rather than granulocytic or erythroid lineages → persistent monocytosis (>0.5×10⁹/L, ≥10% of WBC) = the hallmark of CMML.

## Mechanism

### SRSF2 P95H as a therapeutic vulnerability

**No direct SRSF2 inhibitor approved:**
SRSF2 is a core spliceosome component → targeting it directly risks normal cell toxicity. Research approaches:
- **H3B-8800 (spliceosome modulator targeting SF3B complex):** Active against splicing-factor-mutant cells (SRSF2 P95H, SF3B1 K700E, U2AF1 S34F) via selective sensitivity of pre-mRNA with short introns (enriched in spliceosome-mutant cells); Phase 1 for R/R MDS, AML, CMML: ORR ~12-15%; best benefit in SF3B1/SRSF2-mutant patients; no major toxicity advantage yet
- **SRPK1/2 inhibitors:** Block RS domain hyperphosphorylation → impair SRSF2 nuclear localization → force cytoplasmic accumulation → splicing inhibition; SRPK1 inhibitor SPHINX31 (research compound) slows SRSF2-mutant leukemia growth in mouse models
- **Indirect approaches:** Azacitidine/decitabine (HMA) for SRSF2-mutant MDS/CMML → global demethylation → partially restores aberrant splicing patterns; ruxolitinib for JAK-STAT signaling in MF+SRSF2

**Prognostic significance:**
In MDS: SRSF2 mutation is an intermediate-adverse factor (IPSS-M); particularly adverse when combined with ASXL1 or RUNX1; SRSF2+ASXL1 co-mutation → very high-risk MDS → allo-SCT evaluation. In CMML: SRSF2 alone is not independently prognostic (TET2, ASXL1, KRAS, and NRAS are stronger CMML prognostic factors); CPSS (CMML-Specific Prognostic Scoring System) and CPSS-Mol include molecular data.

## Connections

- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — SRSF2 and DNMT3A mutations frequently co-occur in MDS and CMML; SRSF2 affects RNA processing while DNMT3A affects de novo DNA methylation; their co-occurrence drives more severe hematopoietic dysfunction; DNMT3A-SRSF2 doublet is common in therapy-related MDS/CMML.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — SRSF2 P95H alters EZH2 exon splicing → altered PRC2 isoform abundance; EZH2 and SRSF2 loss-of-function co-occur in MDS and CMML; both contribute to compound epigenetic dysfunction and accelerated AML transformation risk in MDS/CMML.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — SRSF2 regulates splicing of NF-κB pathway genes; aberrant SRSF2 → altered IKK splicing → constitutive NF-κB activation → monocyte proliferation in CMML; NF-κB is a key survival pathway in CMML blasts; JAK/STAT and NF-κB co-activation drive MP-CMML proliferation.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS/NRAS mutations co-occur with SRSF2 in ~15% of CMML; KRAS drives RAS-MAPK monocyte proliferation → MP-CMML phenotype (WBC >13×10⁹/L, splenomegaly); SRSF2+KRAS doublet → aggressive CMML; MEK inhibitor trametinib active in RAS-mutant CMML in early trials.

[^yoshida-2011-splicing]: Yoshida K, Sanada M, Shiraishi Y, et al. Frequent pathway mutations of splicing machinery in myeloid diseases. *Nature.* 2011;478(7367):64-69. [doi:10.1038/nature10496](https://doi.org/10.1038/nature10496) · [PubMed 21909114](https://pubmed.ncbi.nlm.nih.gov/21909114/)
[^patnaik-2013-srsf2-cmml]: Patnaik MM, Lasho TL, Finke CM, et al. Spliceosome mutations involving SRSF2, SF3B1, and U2AF35 in chronic myelomonocytic leukemia: prevalence, clinical correlates, and prognostic relevance. *Am J Hematol.* 2013;88(3):201-206. [doi:10.1002/ajh.23373](https://doi.org/10.1002/ajh.23373) · [PubMed 23335075](https://pubmed.ncbi.nlm.nih.gov/23335075/)
