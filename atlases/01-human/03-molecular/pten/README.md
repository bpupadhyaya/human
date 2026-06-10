---
schema: human-scale-entry/v1
id: pten
name: PTEN
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Lipid phosphatase tumor suppressor; dephosphorylates PIP3 to PIP2, opposing PI3K-AKT-mTOR. Second most frequently mutated after p53. Loss drives endometrial, GBM, prostate, and breast cancers; creates synthetic lethality with PARP inhibitors and mTOR inhibitors."
aliases: ["phosphatase and tensin homolog", "MMAC1", "TEP1", "PTEN tumor suppressor", "PTP"]
sources:
  - id: li-1997-pten-discovery
    type: peer-reviewed
    cite: "Li J, Yen C, Liaw D, et al. PTEN, a putative protein tyrosine phosphatase gene mutated in human brain, breast, and prostate cancer. Science. 1997;275(5308):1943-1947."
    doi: "10.1126/science.275.5308.1943"
    pmid: "9072974"
    url: "https://doi.org/10.1126/science.275.5308.1943"
  - id: stambolic-1998-pten-pi3k
    type: peer-reviewed
    cite: "Stambolic V, Suzuki A, de la Pompa JL, et al. Negative regulation of PKB/Akt-dependent cell survival by the tumor suppressor PTEN. Cell. 1998;95(1):29-39."
    doi: "10.1016/S0092-8674(00)81780-8"
    pmid: "9778245"
    url: "https://doi.org/10.1016/S0092-8674(00)81780-8"
  - id: sancar-2016-pten-review
    type: peer-reviewed
    cite: "Milella M, Falcone I, Conciatori F, et al. PTEN: multiple functions in human malignant tumors. Front Oncol. 2015;5:24."
    doi: "10.3389/fonc.2015.00024"
    pmid: "25763356"
    url: "https://doi.org/10.3389/fonc.2015.00024"
cross_links:
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PTEN directly opposes PIK3CA: PI3K generates PIP3 from PIP2; PTEN dephosphorylates PIP3 back to PIP2, restraining AKT; PTEN loss is functionally equivalent to PIK3CA gain-of-function in activating AKT-mTOR; co-mutation is rare due to functional redundancy."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PTEN is the primary brake on AKT activation; PTEN loss → constitutive PIP3 → PDK1 and AKT membrane recruitment → full AKT hyperactivation; PTEN-null tumors are highly sensitive to AKT inhibitors (capivasertib) and mTOR inhibitors (everolimus) — validated predictive biomarkers."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 transcriptionally activates PTEN; PTEN loss + p53 mutation co-occur and cooperate in GBM and prostate cancer; PTEN stabilizes p53 by sequestering MDM2; the PTEN-p53 feedback loop is the central tumor suppressor network."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PTEN loss → PI3K-AKT-TSC2 → mTORC1 hyperactivation → S6K and 4EBP1 → unchecked protein synthesis; everolimus (mTORC1 inhibitor) is approved for PTEN-loss endometrial, breast (HR+/HER2-), and renal tumors; PTEN loss predicts mTOR inhibitor sensitivity in HR+ breast cancer."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "PTEN loss → impaired HR (reduced RAD51 at DSBs) → HR-deficiency phenotype analogous to BRCA1/2; PTEN and BRCA1 cooperate in DNA damage response; PARP inhibitor synthetic lethality with PTEN-null tumors: olaparib trials in mCRPC and breast cancer with PTEN deletion are ongoing."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "PTEN deleted in 30-40% of GBM; co-occurs with EGFR amplification → dual AKT-mTOR + EGFR-RAS-ERK activation; PTEN methylation is an adverse GBM marker; mTOR inhibitors have modest activity in PTEN-null GBM; PTEN loss predicts resistance to EGFR-targeted therapy in GBM."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "AKT (activated by PTEN loss) phosphorylates GSK-3β Ser9 → GSK-3β inhibited → β-catenin freed from destruction complex → Wnt target gene activation; PTEN loss can activate β-catenin without Wnt ligand; cooperates with APC LOF in colorectal cancer to amplify Wnt/β-catenin output."
---

# PTEN

## Overview

**PTEN (phosphatase and tensin homolog)** is a **dual-specificity phosphatase** and major tumor suppressor that functions primarily as a **lipid phosphatase**, converting **PIP3 (phosphatidylinositol-3,4,5-trisphosphate) to PIP2** — directly opposing the action of PI3K and thereby restraining **AKT-mTOR signaling** [^stambolic-1998-pten-pi3k]. PTEN was first identified as a mutated gene at chromosome 10q23 in brain, breast, and prostate cancers in 1997 [^li-1997-pten-discovery], and is now recognized as the **second most frequently mutated tumor suppressor gene** in human cancer after TP53.

PTEN loss is a founding event in many cancer types, including:
- **Endometrial carcinoma:** 40-80% PTEN mutation/loss — the highest frequency of any cancer; co-mutation with PIK3CA and KRAS; often POLE-ultramutated in endometrioid subtype
- **Glioblastoma (GBM):** 30-40% PTEN loss or mutation; often co-occurring with EGFR amplification → dual PI3K/EGFR activation
- **Prostate cancer:** 20-40% PTEN loss; correlates with Gleason grade ≥7, biochemical recurrence, and castration resistance; ERG fusion co-occurs frequently
- **Breast cancer:** 25-40% PTEN loss (primarily triple-negative and HER2+); PTEN loss predicts poor response to PI3K inhibitors if not combined with AKT inhibitors (downstream of PTEN)
- **Thyroid cancer (follicular):** 30-50% PTEN loss; distinguishes from papillary (BRAF/RAS-driven)
- **Colorectal cancer:** 10-15%

**PTEN hamartoma tumor syndrome (PHTS / Cowden syndrome):**
- Germline PTEN loss-of-function mutations → Cowden syndrome; autosomal dominant
- Pathognomonic: trichilemmomas, papillomatous papules, acral keratoses, macrocephaly
- Dramatically elevated lifetime cancer risks: breast (85%), thyroid (35%), endometrial (28%), kidney (34%), colorectal (16%); management: annual surveillance + prophylactic options
- PTEN germline variants overlap with autism spectrum disorder (macrocephaly + ASD)

## Structure

### PTEN protein domains [^li-1997-pten-discovery]

PTEN is a **403 amino acid** dual-specificity phosphatase with a characteristic domain architecture:

**N-terminal phosphatase domain (aa 1-185, PBD + Cys domain):**
- **PIP3 binding region (PBD, aa 1-13):** Positively charged motif (Lys-Arg) → binds anionic phospholipid head groups → PTEN membrane localization
- **Catalytic core (Cys domain, aa 96-185):** Contains the HCxxGxxRS/T motif (phosphatase active site); **Cys124** is the catalytic cysteine — PTEN Cys124Ser is inactive; Gly129 in P-loop coordinates phosphate substrate
- **Dual specificity:** PTEN primarily dephosphorylates PIP3 (3-phosphate) → PIP2; also has protein phosphatase activity (dephosphorylates phosphotyrosine and phosphoserine substrates) including focal adhesion kinase (FAK) → reduced cell migration

**C2 domain (aa 185-351):**
- Lipid-binding module; Ca²⁺-independent; stabilizes PTEN at plasma membrane; contains nuclear localization sequences (NLS1/2); mutational hotspot — many missense mutations in C2 domain impair membrane binding without affecting catalytic activity
- Membrane binding is enhanced by PI(4,5)P2 (PIP2) → positive feedback loop (PTEN binds PIP2 it generates → stays at membrane)

**C-terminal tail (aa 351-403):**
- Contains PDZ-binding motif (C-terminal Thr-Lys-Val) → binds MAGI, MAST, NHERF family scaffold proteins → PTEN localization at cell-cell contacts and postsynaptic densities
- **Phospho-regulatory cluster:** Ser380, Thr382, Thr383, Ser385 — phosphorylated by CK2 → PTEN adopts closed conformation → reduced membrane binding → reduced activity → tumor cells with CK2 overexpression can inactivate PTEN without mutation
- **Ubiquitination:** NEDD4-1 and WWP2 E3 ligases ubiquitinate PTEN Lys289/380 → nuclear import (monoubiquitination) or proteasomal degradation (polyubiquitination)

**PTEN nuclear functions:**
- Nuclear PTEN (monoubiquitinated or HAUSP-stabilized) maintains genomic stability: associates with centromeres and kinetochores → faithful chromosome segregation; nuclear PTEN loss → chromosomal instability (CIN) → aneuploidy; nuclear PTEN also inhibits PI3K-independent AKT by reducing nuclear AKT activity; distinct from cytoplasmic PIP3 phosphatase role

### PTEN inactivation mechanisms in cancer

1. **Mutation:** Nonsense, frameshift, splice site → protein truncation; missense → most commonly affect catalytic Cys124, phosphatase P-loop, or C2 domain → loss of PIP3 phosphatase activity
2. **Deletion:** Homozygous deletion (LOH) at 10q23; heterozygous PTEN loss alone → haploinsufficiency (PTEN dosage-sensitive; monoallelic loss → partial PI3K-AKT activation without complete cancer transformation)
3. **Promoter methylation:** Epigenetic silencing; enriched in GBM, breast, and head/neck cancers
4. **Post-translational:** CK2 phosphorylation → inactivation; NEDD4-1 ubiquitination → degradation; PI3K generates PIP3 which reduces PTEN membrane binding (substrate competition)
5. **Non-coding RNA:** MiR-21 (most common cancer-overexpressed microRNA) targets PTEN 3'UTR → PTEN suppression in many cancers

## Function

### PIP3 phosphatase function [^stambolic-1998-pten-pi3k]

**Core reaction:** PTEN 3-phosphatase: PI(3,4,5)P3 → PI(4,5)P2 (PIP3 → PIP2)
- At the plasma membrane, PI3K generates PIP3 from PIP2 upon RTK activation → PTEN antagonizes this by rapidly converting PIP3 back to PIP2
- **Kinetics:** PTEN limits peak PIP3 amplitude and duration → controls magnitude of AKT activation

**Downstream of PTEN loss:**
1. PIP3 accumulates → AKT recruited via PH domain → PDK1 phosphorylates AKT Thr308 → mTORC2 phosphorylates Ser473 → full AKT activation
2. AKT → TSC2 phosphorylation → mTORC1 → S6K/4EBP1 → protein synthesis and cell growth
3. AKT → FOXO nuclear exclusion → loss of p21, BIM, PUMA transcription → anti-apoptotic
4. AKT → MDM2 phosphorylation → nuclear MDM2 → p53 degradation → loss of DNA damage response
5. AKT → GSK-3beta inhibition → beta-catenin and cyclin D1 stabilization → Wnt-like cell cycle activation

### PTEN in cancer vs. normal development

**PTEN heterozygosity (haploinsufficiency):**
- One functional PTEN allele is insufficient in mice to fully suppress cancer → heterozygous PTEN mice develop tumors (prostate, thyroid, breast) — demonstrates PTEN is dosage-sensitive
- Human germline heterozygous PTEN mutations → Cowden syndrome with dramatically elevated cancer risk (not obligate cancer)

**PTEN and genome stability:**
- Nuclear PTEN directly participates in DNA DSB repair (associates with RAD51) → PTEN loss → impaired homologous recombination → increased genomic instability → accelerates further oncogenic mutation
- **Synthetic lethality:** PTEN-null cells have impaired HR → sensitive to PARP inhibitors (similar to BRCA1/2 deficiency) → preclinical evidence for olaparib in PTEN-loss cancers; clinical trials ongoing in prostate cancer

**PTEN and metabolism:**
- mTORC1 hyperactivation in PTEN-null cells → S6K → feedback suppression of IRS-1 → reduced PI3K input from insulin → paradoxical insulin resistance in PTEN-null endocrine tissues
- PTEN in liver: PTEN loss in hepatocytes → hepatic lipid accumulation (NASH-like) → hepatocellular carcinoma; liver-specific PTEN knockout mice develop hepatic steatosis and HCC

## Mechanism

### Therapeutic targeting of PTEN-loss tumors

**mTOR inhibitors:**
- PTEN loss → constitutive mTORC1 → sensitive to mTOR inhibitors (everolimus, temsirolimus); approved in:
  - HR+/HER2- breast cancer (BOLERO-2: everolimus + exemestane → 10.6 vs. 4.1 months PFS vs. exemestane alone; PTEN-low tumor subgroup has variable benefit)
  - Renal cell carcinoma (temsirolimus, ARCC trial: improved OS in high-risk pts)
  - Endometrial cancer (everolimus + letrozole → 40% CBR in recurrent endometrial cancer)
  - TSC (tuberous sclerosis complex) — everolimus reduces renal angiomyolipoma, pulmonary LAM (complete mTOR dependence in TSC1/2-loss)
- **Resistance:** S6K → IRS-1 feedback → PI3K reactivation; AKT Ser473 remains partially active via mTORC2 (rapamycin-insensitive) → combine mTOR + AKT inhibitors for sustained pathway suppression

**AKT inhibitors in PTEN-loss:**
- Capivasertib (pan-AKT1/2/3 inhibitor, CAPItello-291): Approved for PIK3CA/AKT/PTEN-altered HR+/HER2- breast cancer; PTEN loss is a qualifying biomarker
- Ipatasertib: Phase 3 IPAT-150 in TNBC (PTEN-loss enriched population; ongoing)

**PI3K inhibitors — PTEN loss as predictor:**
- PTEN loss → PI3K-beta (not alpha) drives AKT → alpelisib (PI3K-alpha selective) less effective in PTEN-null tumors vs. PIK3CA-mutant tumors; PI3K-beta inhibitors (GSK2636771) or pan-PI3K inhibitors may be required

**PARP inhibitors in PTEN-loss:**
- PTEN loss → impaired HR (reduced RAD51 at DSBs) → HR-deficiency-like state → PARP inhibitor sensitivity; clinical trials: olaparib in mCRPC (TRITON2/3 includes PTEN-loss arm); preliminary signal of activity

## Connections

- `connects-to` → **[PIK3CA](../pik3ca/README.md)** — PTEN directly opposes PIK3CA; PI3K generates PIP3 from PIP2; PTEN dephosphorylates PIP3 back to PIP2, restraining AKT activation; PTEN loss is functionally equivalent to PIK3CA gain-of-function mutation; the two are rarely co-mutated in the same tumor due to functional redundancy.
- `connects-to` → **[AKT](../akt/README.md)** — PTEN is the primary AKT pathway brake; PTEN loss → constitutive PIP3 → full AKT hyperactivation; PTEN-null tumors are highly sensitive to AKT inhibitors (capivasertib) and represent a validated biomarker for PI3K-AKT pathway-directed therapy.
- `connects-to` → **[p53](../p53/README.md)** — p53 transcriptionally activates PTEN; PTEN protein stabilizes p53 by sequestering MDM2; PTEN loss + TP53 mutation are co-occurring and mutually cooperating alterations in aggressive cancers; the PTEN-p53 feedback loop is the central tumor suppressor network.
- `connects-to` → **[mTOR](../mtor/README.md)** — PTEN loss → PI3K-AKT-TSC2 → mTORC1 hyperactivation; everolimus (mTORC1 inhibitor) is approved for PTEN-loss endometrial, HR+ breast, and RCC; TSC1/2-loss (complete mTOR dependence) is the extreme example of PTEN-pathway addiction to mTOR.
- `connects-to` → **[BRCA1](../brca1/README.md)** — PTEN loss → impaired HR (reduced RAD51 at DSBs) → HR-deficiency phenotype analogous to BRCA1/2; PTEN and BRCA1 cooperate in DNA damage response; PARP inhibitor synthetic lethality with PTEN-null tumors: olaparib trials in mCRPC and breast cancer with PTEN deletion are ongoing.
- `connects-to` → **[Glioblastoma](../../07-system/glioblastoma/README.md)** — PTEN deleted in 30-40% of GBM; co-occurs with EGFR amplification → dual AKT-mTOR + EGFR-RAS-ERK activation; PTEN methylation is an adverse GBM marker; mTOR inhibitors have modest activity in PTEN-null GBM; PTEN loss predicts resistance to EGFR-targeted therapy in GBM.
- `connects-to` → **[Wnt/β-catenin](../wnt-beta-catenin/README.md)** — AKT (activated by PTEN loss) phosphorylates GSK-3β Ser9 → GSK-3β inhibited → β-catenin freed from destruction complex → Wnt target gene activation; PTEN loss can activate β-catenin without Wnt ligand; cooperates with APC LOF in colorectal cancer to amplify Wnt/β-catenin output.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^li-1997-pten-discovery]: Li J, Yen C, Liaw D, et al. PTEN, a putative protein tyrosine phosphatase gene mutated in human brain, breast, and prostate cancer. *Science.* 1997;275(5308):1943-1947. [doi:10.1126/science.275.5308.1943](https://doi.org/10.1126/science.275.5308.1943) · [PubMed 9072974](https://pubmed.ncbi.nlm.nih.gov/9072974/)
[^stambolic-1998-pten-pi3k]: Stambolic V, Suzuki A, de la Pompa JL, et al. Negative regulation of PKB/Akt-dependent cell survival by the tumor suppressor PTEN. *Cell.* 1998;95(1):29-39. [doi:10.1016/S0092-8674(00)81780-8](https://doi.org/10.1016/S0092-8674(00)81780-8) · [PubMed 9778245](https://pubmed.ncbi.nlm.nih.gov/9778245/)
[^sancar-2016-pten-review]: Milella M, Falcone I, Conciatori F, et al. PTEN: multiple functions in human malignant tumors. *Front Oncol.* 2015;5:24. [doi:10.3389/fonc.2015.00024](https://doi.org/10.3389/fonc.2015.00024) · [PubMed 25763356](https://pubmed.ncbi.nlm.nih.gov/25763356/)
