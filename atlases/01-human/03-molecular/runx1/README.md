---
schema: human-scale-entry/v1
id: runx1
name: RUNX1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "RUNX1 (AML1) is a core binding factor transcription factor essential for hematopoiesis; ETV6-RUNX1 t(12;21) defines ~25% of pediatric B-ALL (favorable); RUNX1-RUNX1T1 t(8;21) defines CBF-AML (favorable); somatic RUNX1 mutations (~15% AML) and germline RUNX1 → FPD-AML."
aliases: ["RUNX1", "AML1", "CBFA2", "core binding factor", "ETV6-RUNX1", "TEL-AML1", "RUNX1-RUNX1T1", "AML1-ETO", "t(8;21) AML", "t(12;21) ALL", "familial platelet disorder", "FPD-AML", "CBF-AML"]
sources:
  - id: golub-1995-etv6-runx1
    type: peer-reviewed
    cite: "Golub TR, Barker GF, Bohlander SK, et al. Fusion of the TEL gene on 12p13 to the AML1 gene on 21q22 in acute lymphoblastic leukemia. Proc Natl Acad Sci USA. 1995;92(11):4917-4921."
    doi: "10.1073/pnas.92.11.4917"
    pmid: "7761424"
    url: "https://doi.org/10.1073/pnas.92.11.4917"
  - id: marcucci-2005-cbf-aml
    type: peer-reviewed
    cite: "Marcucci G, Mrózek K, Ruppert AS, et al. Prognostic factors and outcome of core binding factor acute myeloid leukemia patients with t(8;21) differ from those of patients with inv(16): a Cancer and Leukemia Group B study. J Clin Oncol. 2005;23(24):5705-5717."
    doi: "10.1200/JCO.2005.14.122"
    pmid: "16110030"
    url: "https://doi.org/10.1200/JCO.2005.14.122"
cross_links:
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "RUNX1-RUNX1T1 silences RUNX1 target genes via NCoR/HDAC → reduces BIM → anti-apoptotic BCL-2 dependency; venetoclax active in RUNX1-mutant AML and Ph+ ALL; ETV6-RUNX1 B-ALL has high BCL-2 expression → venetoclax + chemotherapy combinations studied."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "RUNX1 controls T-cell progenitor fate from HSC; NOTCH1 mutations in ~60% of T-ALL; RUNX1 and NOTCH1 cooperate in early T-cell development; ETP-ALL (early T-precursor, immature) has RUNX1 mutations in ~15%; RUNX1 loss accelerates NOTCH1-driven T-ALL in mouse models."
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "FLT3-ITD co-occurs with RUNX1 mutations in ~15% of AML; RUNX1+FLT3-ITD → midostaurin/quizartinib addition to 7+3; FLT3 is expressed in B-ALL and some T-ALL; FLT3 inhibitors active in Ph-like ALL with FLT3 rearrangements; FLT3L-FLT3 axis controls early B-cell development."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 checkpoint limits T-cell killing of RUNX1-rearranged ALL cells; blinatumomab (CD19×CD3 BiTE) and tisagenlecleucel (CD19 CAR-T) rely on T-cell activity; PD-1-mediated exhaustion limits CAR-T durability in ALL; pembrolizumab+blinatumomab studied in MRD+ ALL."
---

# RUNX1

## Overview

**RUNX1 (Runt-related transcription factor 1, also known as AML1 or CBFA2)** is a master hematopoietic transcription factor and the most frequently mutated gene in human leukemia when considering all classes of genetic alterations (point mutations, chromosomal translocations, and deletions). RUNX1 forms the **Core Binding Factor (CBF) complex** by heterodimerizing with CBFβ — together binding the core enhancer DNA sequence (TGT/cGGT) at promoters and enhancers of >1,000 hematopoietic target genes including CEBPA, PU.1, MPO, IL-3, GMCSF, and CSF1R. Two common chromosomal translocations define favorable-risk leukemias: **t(8;21)(q22;q22) → RUNX1-RUNX1T1 (AML1-ETO)** in ~5% of AML (core binding factor AML), and **t(12;21)(p13;q22) → ETV6-RUNX1 (TEL-AML1)** in ~25% of pediatric B-ALL. Both are "favorable" because they define leukemias with high initial response rates, reflecting oncogene addiction to the fusion protein. Germline RUNX1 haploinsufficiency mutations cause **Familial Platelet Disorder with predisposition to AML (FPD-AML)** — an autosomal dominant disorder with ~35-40% lifetime leukemia risk [^golub-1995-etv6-runx1] [^marcucci-2005-cbf-aml].

**RUNX1 alterations across leukemias:**
- **AML t(8;21) / CBF-AML:** RUNX1-RUNX1T1 fusion (~5% of AML); AML FAB M2 subtype; Auer rods characteristic; co-mutations: KIT (25-30%), FLT3-ITD (~5-7%), NRAS (~10%); CR rate ~90%; 5-year OS ~50-60%; high-dose cytarabine (HiDAC) consolidation × 3 cycles; KIT co-mutation → poor prognosis within t(8;21); allo-SCT not routinely recommended for first remission in t(8;21) without KIT or other adverse mutations
- **B-ALL t(12;21) / ETV6-RUNX1:** ~25% of pediatric B-ALL; cryptic translocation (not visible on standard karyotype → FISH or RT-PCR required); pre-B ALL phenotype (CD10+, CD19+, CD34+, TdT+); excellent prognosis (5-year EFS ~90-95%); late relapses possible (ETV6-RUNX1 retained in relapses); exquisitely L-asparaginase sensitive
- **Somatic RUNX1 mutations (point mutations, small indels):** ~15% of all AML; adverse prognosis; RUNX1 loss-of-function (Runt domain mutations); RUNX1-mutant AML → differential sensitivity to HMA + venetoclax (high BCL-2 dependency); often co-mutated with SRSF2 or MDS-driver mutations (classified as AML-MRC in WHO 2022)
- **iAMP21 (intrachromosomal amplification of chromosome 21):** ~2% of B-ALL; RUNX1 amplification (not fusion) → overexpression; high-risk ALL; intensive chemotherapy required; allo-SCT in CR1 in most protocols
- **Germline RUNX1 / FPD-AML:** Autosomal dominant; thrombocytopenia (platelet count ~60,000-100,000/μL) + platelet function defects (dense granule deficiency, reduced aggregation to ADP/collagen) → easy bruising; ~35-40% lifetime AML/MDS risk; germline testing for RUNX1 recommended for young AML/MDS patients with thrombocytopenia or family history

## Structure

### RUNX1 protein architecture

RUNX1 is a 453-amino-acid transcription factor with two primary functional domains:

**Runt domain (50-177, DNA- and CBFβ-binding):**
- 128-amino-acid immunoglobulin-like fold; the defining domain of all RUNX proteins (RUNX1, RUNX2, RUNX3)
- Binds DNA sequence 5'-YGYGGTY-3' (Y = pyrimidine) at the consensus core binding factor site; contacts both strands of DNA via loops L3 and L12
- **CBFβ binding:** The Runt domain non-covalently binds CBFβ → CBFβ does NOT contact DNA directly but allosterically stabilizes the Runt domain-DNA complex → ~10-fold increase in DNA affinity; CBFβ is essential for RUNX1 in vivo function
- **ETV6-RUNX1 fusion:** ETV6 HLH (Helix-Loop-Helix) dimerization domain fused to RUNX1 Runt+C-terminal transactivation domains; ETV6 HLH causes constitutive dimerization + nuclear retention of RUNX1; the fusion retains RUNX1 Runt domain → binds CBF target sites as homodimer → represses RUNX1 target genes AND activates novel targets; ETV6-RUNX1 impairs B-cell differentiation → pre-B ALL

**RUNX1 C-terminal transactivation domain (178-453):**
- Contains nuclear localization signal; PST (proline/serine/threonine-rich) domain; autoinhibitory domain
- Interacts with coactivators (CBP/p300, SRC family kinases) → transactivation of hematopoietic target genes
- **RUNX1-RUNX1T1 fusion:** C-terminal ~453 aa of RUNX1 → replaced by RUNX1T1 (ETO/MTG8); RUNX1T1 contains NHR1-4 (Nervy Homology Region) domains → recruits NCoR1/NCoR2, Sin3A, HDAC1/2/3/8 corepressor complex → RUNX1 target genes strongly repressed → differentiation block at myeloid progenitor stage → CBF-AML

### CBF complex biology

**Core Binding Factor (CBF):**
RUNX1 + CBFβ form the CBF complex — essential for definitive hematopoiesis; RUNX1-null mice die at E12.5 from complete failure of definitive hematopoiesis in the fetal liver (yolk sac/primitive hematopoiesis preserved); CBFβ-null mice have identical phenotype. CBF target genes include: CEBPA (granulocytic commitment), PU.1 (myeloid/lymphoid commitment), MPO (myeloperoxidase), IL-3 receptor, GM-CSF receptor, and T-cell receptor genes (RAG1/2, TCRα/β enhancers) → CBF is essential for both myeloid and lymphoid differentiation.

**Inv(16) / CBFβ-MYH11 (second CBF-AML type):**
Inversion of chromosome 16 → CBFβ fused to smooth muscle myosin heavy chain (MYH11) → CBFβ-MYH11 → sequesters RUNX1 into cytoplasmic filaments → RUNX1 target gene derepression; distinct from t(8;21) clinically: inv(16) → AML-M4Eo (monocytic differentiation + eosinophils); similar favorable prognosis (~55% 5-year OS); both CBF-AML subtypes require high-dose cytarabine consolidation and KIT testing.

## Function

### Normal RUNX1 in hematopoiesis

**Primitive vs. definitive hematopoiesis:**
RUNX1 is required only for **definitive hematopoiesis** (HSC generation from hemogenic endothelium in the AGM region of the embryo); RUNX1 activates the "endothelial-to-hematopoietic transition" (EHT) by repressing endothelial genes (Cdh5/VE-cadherin, Sox17) and activating hematopoietic genes (Spi1/PU.1, Cebpa, Gata2). RUNX1 is transiently expressed at very high levels during EHT → thereafter, RUNX1 expression is maintained at lower levels in adult HSCs and progenitors.

**Megakaryocyte-platelet axis (FPD-AML mechanism):**
RUNX1 activates megakaryocyte-specific genes (GP1BA, GP1BB, GP9 → platelet GPIb-IX-V complex; ITGA2B/ITGB3 → GPIIb/IIIa; PF4; PPBP) → heterozygous RUNX1 loss → haploinsufficiency → reduced megakaryocyte maturation → thrombocytopenia + platelet dysfunction; the remaining wildtype RUNX1 allele is susceptible to second-hit mutations (LOH, somatic RUNX1 mutations) → complete RUNX1 loss → AML/MDS transformation in FPD-AML.

### RUNX1 in T-cell and B-cell development

**T-cell:** RUNX1 → TCR β-chain enhancer → TCRβ rearrangement in thymocytes (V→DJ recombination); RUNX1 also regulates Tdt (terminal deoxynucleotidyl transferase) → V(D)J recombination junctional diversity; RUNX1 is a direct RAG1/2 enhancer binding protein → TCR/BCR diversity generation.

**B-cell:** RUNX1 → regulates EBF1 and PAX5 → B-lineage commitment; ETV6-RUNX1 impairs B-cell differentiation by repressing PAX5 targets and IL-7R signaling → arrest at pre-B cell stage → B-ALL.

## Mechanism

### Therapeutic targeting of CBF-AML and ETV6-RUNX1 ALL

**CBF-AML (t(8;21)) treatment:**
Standard: 7+3 induction (cytarabine + daunorubicin) → CR ~90%; consolidation: 3-4 cycles of high-dose cytarabine (HiDAC, 3 g/m² q12h × 3 days); 5-year OS ~50-60%; allo-SCT: Reserved for relapse or first remission with adverse features (KIT mutation, >1 course to CR, persistent MRD). Gemtuzumab ozogamicin (anti-CD33 ADC, GO) added to induction → improves EFS in CBF-AML (ALFA-0702 trial); now standard in many protocols. KIT inhibitors (imatinib/dasatinib): KIT mutation in ~25% of t(8;21) → combined with chemotherapy in trials.

**ETV6-RUNX1 B-ALL treatment:**
COG protocol (children): Augmented-BFM chemotherapy; L-asparaginase (PEG-asparagine) is especially effective; methotrexate-based CNS prophylaxis; maintenance (6-mercaptopurine + MTX); 5-year EFS ~90-95%; NO allo-SCT in first remission for standard-risk ETV6-RUNX1 ALL; MRD negativity by end of induction → further de-escalation of therapy (less intensive consolidation).

**Late relapses in ETV6-RUNX1 ALL:**
ETV6-RUNX1 fusion persists as a "first hit" in quiescent preleukemic B-cell progenitors → late relapses (years 2-7 post-treatment) from de novo leukemia arising from the persisting preleukemic clone (with new secondary mutations); late relapse may respond to re-induction; blinatumomab + chemo for MRD+ relapse.

**RUNX1-mutant AML:**
HMA + venetoclax (azacitidine + venetoclax, VIALE-A): RUNX1-mutant AML has high BCL-2 dependency → CR+CRi ~70-80% in RUNX1-mutant subgroup; HMA+VEN preferred for older/unfit RUNX1-mutant AML; allo-SCT in CR1 for eligible.

## Connections

- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — RUNX1-RUNX1T1 silences RUNX1 target genes via NCoR/HDAC → reduces BIM → anti-apoptotic BCL-2 dependency; venetoclax active in RUNX1-mutant AML and Ph+ ALL; ETV6-RUNX1 B-ALL has high BCL-2 expression → venetoclax + chemotherapy combinations studied.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — RUNX1 controls T-cell progenitor fate from HSC; NOTCH1 mutations in ~60% of T-ALL; RUNX1 and NOTCH1 cooperate in early T-cell development; ETP-ALL (early T-precursor, immature) has RUNX1 mutations in ~15%; RUNX1 loss accelerates NOTCH1-driven T-ALL in mouse models.
- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — FLT3-ITD co-occurs with RUNX1 mutations in ~15% of AML; RUNX1+FLT3-ITD → midostaurin/quizartinib addition to 7+3; FLT3 is expressed in B-ALL and some T-ALL; FLT3 inhibitors active in Ph-like ALL with FLT3 rearrangements; FLT3L-FLT3 axis controls early B-cell development.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 checkpoint limits T-cell killing of RUNX1-rearranged ALL cells; blinatumomab (CD19×CD3 BiTE) and tisagenlecleucel (CD19 CAR-T) rely on T-cell activity; PD-1-mediated exhaustion limits CAR-T durability in ALL; pembrolizumab+blinatumomab studied in MRD+ ALL.

[^golub-1995-etv6-runx1]: Golub TR, Barker GF, Bohlander SK, et al. Fusion of the TEL gene on 12p13 to the AML1 gene on 21q22 in acute lymphoblastic leukemia. *Proc Natl Acad Sci USA.* 1995;92(11):4917-4921. [doi:10.1073/pnas.92.11.4917](https://doi.org/10.1073/pnas.92.11.4917) · [PubMed 7761424](https://pubmed.ncbi.nlm.nih.gov/7761424/)
[^marcucci-2005-cbf-aml]: Marcucci G, Mrózek K, Ruppert AS, et al. Prognostic factors and outcome of core binding factor acute myeloid leukemia patients with t(8;21) differ from those of patients with inv(16): a Cancer and Leukemia Group B study. *J Clin Oncol.* 2005;23(24):5705-5717. [doi:10.1200/JCO.2005.14.122](https://doi.org/10.1200/JCO.2005.14.122) · [PubMed 16110030](https://pubmed.ncbi.nlm.nih.gov/16110030/)
