---
schema: human-scale-entry/v1
id: wt1
name: WT1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "WT1 encodes a zinc-finger TF essential for kidney and gonadal development; germline mutations cause WAGR and Denys-Drash syndromes; mutations in ~10-15% sporadic Wilms tumor; WT1 overexpression in ~70-90% AML is an adverse prognostic marker and MRD target."
aliases: ["WT1", "Wilms tumor 1", "WT1 gene", "WT1 zinc finger", "WT1 AML", "WT1 Wilms tumor", "WAGR WT1", "Denys-Drash WT1"]
sources:
  - id: huff-2011-wt1
    type: peer-reviewed
    cite: "Huff V. Wilms' tumour genetics and biology. J Clin Oncol. 2011;29(10):1273-1278."
    doi: "10.1200/JCO.2010.32.0507"
    pmid: "21402607"
    url: "https://doi.org/10.1200/JCO.2010.32.0507"
  - id: dome-2015-wilms
    type: peer-reviewed
    cite: "Dome JS, Graf N, Geller JI, et al. Advances in Wilms tumor treatment and biology: progress through international collaboration. J Clin Oncol. 2015;33(27):2999-3007."
    doi: "10.1200/JCO.2015.62.1888"
    pmid: "26261251"
    url: "https://doi.org/10.1200/JCO.2015.62.1888"
cross_links:
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "WT1 and p53 physically interact; WT1 can activate or repress p53 target genes; diffuse anaplastic Wilms tumor is associated with TP53 mutations in ~70%; WT1+TP53 co-loss → worst Wilms prognosis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CTNNB1 mutations occur in ~15-20% Wilms tumor, co-occurring with WT1 mutations; WT1 loss impairs WNT antagonist expression (SFRP1); WNT+WT1 co-mutation → intralobar nephrogenic rest → blastemal-predominant Wilms; β-catenin nuclear localization is diagnostic."
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "WT1 mRNA is overexpressed in ~70-90% AML including FLT3-ITD-mutant AML; FLT3-ITD transcriptionally upregulates WT1; WT1 RT-qPCR quantification is used as AML MRD marker; rising WT1 predicts relapse; WT1 peptide vaccines in clinical trials."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "IGF2 overexpression (~75% Wilms tumor, via 11p15 imprinting loss) → IGF1R → PI3K-AKT-mTOR → proliferation; everolimus studied in relapsed Wilms tumor; WT1 transcriptionally suppresses IGF2 in normal kidney development."
---

# WT1

## Overview

**WT1 (Wilms Tumor 1)** is a tumor suppressor gene at chromosome 11p13 encoding a zinc finger transcription factor with critical roles in urogenital development and hematopoietic differentiation. WT1 was discovered in 1990 as the first gene causally linked to **Wilms tumor (nephroblastoma)**, the most common renal malignancy of childhood, establishing the paradigm of pediatric cancer as a developmental defect [^huff-2011-wt1]. WT1 contains a **C-terminal DNA-binding domain with four Cys2-His2 zinc fingers** (ZF1-4) that recognize the GCG(G/T)GGGCG consensus sequence (EGR binding motif) and an N-terminal transcriptional regulatory domain (repression and activation domains). A **24-amino-acid alternatively spliced segment between ZF3 and ZF4** (+KTS or -KTS isoforms) fundamentally alters WT1 function: **-KTS isoforms** primarily bind DNA as transcriptional activators/repressors; **+KTS isoforms** preferentially bind RNA and co-localize with splicing factors, implicating WT1 in post-transcriptional mRNA processing [^dome-2015-wilms]. In addition to its role in pediatric Wilms tumor, WT1 protein is aberrantly **overexpressed in ~70-90% of AML** — independent of WT1 gene mutation — making WT1 mRNA quantification a validated minimal residual disease (MRD) marker in leukemia.

**WT1 in development and disease:**
- **Normal kidney development:** WT1 is essential for metanephric blastema → glomerulus specification; WT1-null mice lack kidneys and gonads (bilateral renal and gonadal agenesis); WT1 activates PODXL (podocalyxin), NPHS1 (nephrin), and NPHS2 (podocin) in glomerular podocytes → essential for glomerular filtration
- **Wilms tumor germline syndromes:** WAGR (11p13 deletion, ~30% Wilms tumor risk), Denys-Drash (ZF missense mutations, ~90% Wilms tumor risk), Frasier syndrome (ZF3-ZF4 KTS splice mutations → glomerulopathy + gonadoblastoma)
- **Sporadic Wilms tumor:** Somatic WT1 mutations in ~10-15%; most Wilms tumor is WT1 wild-type (driven by 11p15 imprinting, CTNNB1, WTX, miRNA processing genes DROSHA/DGCR8, SIX1/2)
- **AML:** WT1 overexpression in ~70-90%; adverse prognostic marker in cytogenetically normal (CN)-AML; WT1 mutations (distinct from overexpression) in ~10% AML/MDS → independent adverse prognosis; WT1 MRD monitoring by RT-qPCR (ELN recommendations)
- **MDS:** WT1 mutations in ~5-10%; associated with RUNX1 and TP53 co-mutations; adverse prognosis

## Structure

### WT1 protein architecture

WT1 is a 449-amino-acid, 52-54 kDa protein (multiple isoforms due to alternative splicing):

**N-terminal regulatory domain (1-296):**
- Self-association domain (dimerization): homotypic WT1-WT1 interactions → DNA binding cooperativity
- **Proline/glutamine-rich transactivation/repression domain (aa 1-182):** Interacts with p53 (WT1 N-terminus contacts p53 tetramerization domain → context-dependent transcriptional modulation); interacts with BASP1 → co-repressor → chromatin compaction; interacts with CREB-binding protein (CBP) → co-activation
- Alternatively spliced 17-aa segment (exon 5): present in ~70-80% of WT1 mRNAs; functionally separates repression and activation capabilities; exon 5-containing isoforms have higher leukemia-promoting activity

**C-terminal zinc finger domain (296-449, 4 Cys2-His2 ZF):**
- ZF1 (296-320), ZF2 (322-346), ZF3 (350-374), ZF4 (376-400)
- ZF2-4 make primary DNA contacts; GCG(G/T)GGGCG consensus; EGR1 recognition sequence variant
- **KTS insert (between ZF3 and ZF4):** Lys-Thr-Ser tripeptide (from alternative 3' splice in exon 9) → +KTS isoforms have lower DNA-binding affinity but preferentially bind GU-rich RNA → co-localize with snRNPs in nuclear speckles → post-transcriptional role in pre-mRNA splicing

**Denys-Drash mutations:**
R394W (ZF3) and R394Q: Arg394 contacts guanine in position 3 of recognition sequence; R394W/Q abolishes DNA binding → dominant-negative (mutant ZF3 disrupts adjacent ZF dimer contacts in WT complexes) → loss of WT1 tumor suppressor function + dominant-negative interference with WT1-wild-type allele → DDS penetrance despite heterozygosity.

### Nephrogenic rests and WT1

**Nephrogenic rests** are foci of metanephric blastema cells that persist postnatally (normal embryonic structures that should involute):
- **Intralobar nephrogenic rests (ILNR):** Located anywhere within the lobe; associated with WT1 mutations + CTNNB1 mutations; develop into blastemal-predominant Wilms tumor; present in WAGR and Denys-Drash patients
- **Perilobar nephrogenic rests (PLNR):** Located at periphery of renal lobe; associated with 11p15 IGF2 imprinting changes (Beckwith-Wiedemann syndrome); develop into epithelial/stromal-predominant Wilms tumor
Nephrogenic rests are pre-malignant lesions; nephroblastomatosis (diffuse hyperplastic perilobar) → increased Wilms risk requiring close surveillance.

## Function

### Normal WT1 roles in development

**Kidney organogenesis:**
WT1 in metanephric mesenchyme (MM) → activates GDNF (ligand for RET receptor in ureteric bud) → ureteric bud branching → signals back to MM via WNT9B/WNT4 → mesenchymal-to-epithelial transition (MET) → nephron formation; WT1-null → no GDNF → no ureteric bud branching → bilateral renal agenesis. WT1 also activates PAX2 and PODXL → glomerular podocyte specification → filtration barrier integrity.

**Hematopoiesis:**
WT1 is expressed in HSCs, early myeloid progenitors, and megakaryocytes; WT1 promotes HSC self-renewal via MYC, BCL-2 target activation; WT1 overexpression in AML leukemic stem cells → survival advantage; WT1-low expression correlates with neutrophil maturation → AML blasts arrest before WT1 downregulation → high WT1 → sustained blast survival.

### WT1 as AML MRD marker

**Quantification:**
WT1 mRNA measured by RT-qPCR standardized against housekeeping gene (ABL1 or GUSB); ELN 2022 recommendations: WT1 can be used as AML MRD marker when no other suitable marker available; decreasing WT1 during induction/consolidation correlates with CR; WT1 >250 copies/10⁴ ABL copies in remission BM → residual disease; rising WT1 during follow-up → molecular relapse signal.

**Limitations:**
WT1 is expressed in normal hematopoiesis (low level); specificity limited (~70-80%); best used as supplementary marker when NPM1, RUNX1-RUNX1T1, or CBFβ-MYH11 MRD markers not available.

### WT1 immunotherapy

**WT1 protein as tumor-associated antigen (TAA):**
WT1 is overexpressed in AML, MDS, breast cancer, ovarian cancer, lung cancer (not in normal tissue at significant levels) → HLA-A2-restricted WT1 peptides (WT1 126-134: RMFPNAPYL) presented on tumor cell surface → CTL recognition.

**Clinical approaches:**
- WT1 peptide vaccines (galinpepimut-S/DSP-7888): Phase 2 in AML post-allo-SCT (maintenance); modest MRD clearance; ongoing Phase 3 (ASPIRANT trial)
- Anti-WT1/HLA-A2 bispecific antibody (ESK1): Preclinical → clinical Phase 1 in AML
- WT1-specific CAR-T and TCR-T cell therapy: Early Phase 1 clinical trials

## Mechanism

### WT1 as therapeutic target in AML

**WT1 mutations in AML (distinct from overexpression):**
~10% AML have somatic WT1 mutations (exon 1 frameshift or ZF domain missense); WT1 mutations → loss of tumor suppressor function → adverse cytogenetics-independent poor prognosis; co-occur with IDH1/2, DNMT3A, TET2 in AML; WT1-mutant AML → hypermethylation phenotype (WT1 normally promotes demethylation via TET2 induction).

**WT1 in targeted therapy resistance:**
WT1 mutations are acquired during chemotherapy resistance → may contribute to relapse; FLT3 inhibitors (midostaurin, gilteritinib) reduce FLT3-ITD-driven WT1 overexpression → WT1 MRD level can serve as pharmacodynamic marker of FLT3 inhibitor efficacy.

## Connections

- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — WT1 and p53 physically interact; WT1 can activate or repress p53 target genes; diffuse anaplastic Wilms tumor is associated with TP53 mutations in ~70%; WT1+TP53 co-loss → worst Wilms prognosis.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — CTNNB1 mutations occur in ~15-20% Wilms tumor, co-occurring with WT1 mutations; WT1 loss impairs WNT antagonist expression (SFRP1); WNT+WT1 co-mutation → intralobar nephrogenic rest → blastemal-predominant Wilms; β-catenin nuclear localization is diagnostic.
- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — WT1 mRNA is overexpressed in ~70-90% AML including FLT3-ITD-mutant AML; FLT3-ITD transcriptionally upregulates WT1; WT1 RT-qPCR quantification is used as AML MRD marker; rising WT1 predicts relapse; WT1 peptide vaccines in clinical trials.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — IGF2 overexpression (~75% Wilms tumor, via 11p15 imprinting loss) → IGF1R → PI3K-AKT-mTOR → proliferation; everolimus studied in relapsed Wilms tumor; WT1 transcriptionally suppresses IGF2 in normal kidney development.

[^huff-2011-wt1]: Huff V. Wilms' tumour genetics and biology. *J Clin Oncol.* 2011;29(10):1273-1278. [doi:10.1200/JCO.2010.32.0507](https://doi.org/10.1200/JCO.2010.32.0507) · [PubMed 21402607](https://pubmed.ncbi.nlm.nih.gov/21402607/)
[^dome-2015-wilms]: Dome JS, Graf N, Geller JI, et al. Advances in Wilms tumor treatment and biology: progress through international collaboration. *J Clin Oncol.* 2015;33(27):2999-3007. [doi:10.1200/JCO.2015.62.1888](https://doi.org/10.1200/JCO.2015.62.1888) · [PubMed 26261251](https://pubmed.ncbi.nlm.nih.gov/26261251/)
