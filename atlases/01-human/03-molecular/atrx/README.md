---
schema: human-scale-entry/v1
id: atrx
name: ATRX
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "ATRX is a chromatin remodeler of the ATRX-DAXX-H3.3 complex at telomeres; LOF causes alternative lengthening of telomeres (ALT); mutated in ~80% of IDH-mutant astrocytoma (Grade 3/4), MPNST, pancreatic NETs, neuroblastoma; ATRX LOF + IDH1 = astrocytoma lineage; 1p/19q intact."
aliases: ["ATRX", "ATRX mutation", "ATRX glioma", "ATRX astrocytoma", "ALT ATRX", "alternative lengthening of telomeres", "ATRX-DAXX complex", "ATRX LOF", "ATRX IHC", "ATRX chromatin remodeler"]
sources:
  - id: heaphy-2011-atrx-alt
    type: peer-reviewed
    cite: "Heaphy CM, de Wilde RF, Jiao Y, et al. Altered telomeres in tumors with ATRX and DAXX mutations. Science. 2011;333(6041):425."
    doi: "10.1126/science.1207313"
    pmid: "21719641"
    url: "https://doi.org/10.1126/science.1207313"
  - id: jiao-2012-atrx-glioma
    type: peer-reviewed
    cite: "Jiao Y, Killela PJ, Reitman ZJ, et al. Frequent ATRX, CIC, FUBP1 and IDH mutations refine the classification of malignant gliomas. Oncotarget. 2012;3(7):709-722."
    doi: "10.18632/oncotarget.588"
    pmid: "22869205"
    url: "https://doi.org/10.18632/oncotarget.588"
cross_links:
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "ATRX LOF + IDH1 R132H + CDKN2A deletion → WHO Grade 4 IDH-mutant astrocytoma; IDH1+ATRX+TP53 triple mutant is the canonical high-grade astrocytoma genotype; ATRX LOF is a mandatory criterion for astrocytoma lineage (vs oligodendroglioma where ATRX is intact and 1p/19q deleted)."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "ATRX LOF + IDH1 → 2-HG → TET2 inhibition → DNA hypermethylation (G-CIMP); ATRX-DAXX deposits H3.3 at telomeric chromatin; ATRX LOF impairs H3.3 telomeric deposition → ALT mechanism → telomere lengthening independent of TERT; ATRX and TET2 cooperate in chromatin maintenance."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "ATRX LOF + IDH1 + TP53 mutation defines IDH-mutant astrocytoma Grade 3-4; TP53 and ATRX LOF co-occur in >80% of IDH-mutant astrocytomas; ATRX LOF → elevated replication stress at telomeres → p53 pathway activation; TP53 LOF relieves this brake → rapid astrocytoma progression."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A homozygous deletion occurs in ~50-70% of IDH-mutant astrocytoma Grade 4; CDK4/6 hyperactivation → RB1 → E2F proliferation; CDKN2A deletion defines WHO Grade 4 IDH-mutant astrocytoma (from Grade 3); ATRX LOF + CDKN2A deletion → worst IDH-mutant glioma prognosis."
---

# ATRX

## Overview

**ATRX** (Alpha-Thalassemia/Mental Retardation Syndrome X-linked) encodes a 2,492-amino-acid (280 kDa) ATP-dependent chromatin remodeler belonging to the SWI2/SNF2 helicase superfamily. ATRX functions in a stable complex with **DAXX** (death domain-associated protein) and **H3.3** to deposit the histone variant H3.3 at telomeres, pericentromeric heterochromatin, and other repetitive elements. Loss of ATRX function disrupts this deposition mechanism, resulting in telomeric replication stress and engagement of **Alternative Lengthening of Telomeres (ALT)** — a recombination-based, TERT-independent mechanism of telomere maintenance. In neuro-oncology, ATRX LOF is a defining molecular feature of **IDH-mutant astrocytoma** (WHO Grades 3 and 4), separating the astrocytoma lineage from IDH-mutant oligodendroglioma (which retains ATRX and instead shows 1p/19q codeletion) [^heaphy-2011-atrx-alt] [^jiao-2012-atrx-glioma].

**ATRX alterations across tumor types:**

| Tumor type | Frequency | Notes |
|---|---|---|
| IDH-mutant astrocytoma Grade 3 | ~70-80% | Co-occurs with TP53; 1p/19q intact; ATRX LOF = diagnostic |
| IDH-mutant astrocytoma Grade 4 | ~80-85% | CDKN2A deletion frequently added; ATRX LOF + CDKN2A = worst prognosis |
| Pancreatic neuroendocrine tumor | ~40% | ATRX or DAXX LOF; ALT mechanism; associated with metastatic behavior |
| MPNST | ~20-25% | Occurs in NF1 background; ATRX LOF + PRC2 LOF in aggressive MPNST |
| Neuroblastoma (MYCN-non-amplified) | ~5-10% | High-risk subgroup; ALT positivity associated with worse OS |
| Osteosarcoma | ~25-30% | ALT-positive osteosarcoma; ATRX LOF with poor prognosis |
| Glioblastoma (IDH-wildtype) | <5% | IDH-wt GBM rarely shows ATRX LOF; not diagnostically relevant |

**Germline ATRX:** Germline ATRX pathogenic variants cause **ATR-X syndrome** (X-linked intellectual disability, hemoglobin H disease/alpha-thalassemia, characteristic facial features); no significant solid tumor predisposition in germline carriers; germline mutations in males (X-linked recessive)

## Structure

### ATRX protein architecture

**ADD domain (ATRX-DNMT3-DNMT3L domain; aa ~160-600):**
PHD-like zinc finger + BAH (bromo-adjacent homology) domain; recognizes H3K9me3 (repressive mark at heterochromatin) and H3K4me0 (unmodified H3K4 at silenced loci); ADD domain binding at H3K9me3 + H3K4me0 recruits ATRX to constitutive heterochromatin at telomeres and pericentromeric repeats; missense mutations in the ADD domain alter chromatin targeting (frequently mutated in ATR-X syndrome germline mutations); cancer ATRX truncating mutations typically inactivate both ADD and ATPase domains

**ATPase/helicase domain (aa ~1700-2500; SWI2/SNF2-family):**
DNA-stimulated ATPase activity; drives chromatin remodeling and H3.3 deposition; ATP hydrolysis couples energy to nucleosome displacement and H3.3-DAXX chaperone-mediated loading; cancer ATRX truncating mutations in this domain eliminate catalytic activity; SNF2-family ATPase conserved across ATRX, SMARCA4 (BRG1), CHD1, RAD54

**DAXX-binding domain:**
N-terminal region mediates DAXX protein-protein interaction; DAXX is the H3.3 chaperone that physically escorts H3.3 to ATRX for deposition; ATRX LOF → DAXX-H3.3 complex cannot deposit H3.3 at telomeres → free H3.3 availability increased → telomeric chromatin disrupted

### ATRX mutation patterns

**LOF mutation types in cancer:**
- Truncating (frameshift/nonsense): ~60-70% of ATRX cancer mutations; protein unstable/absent by IHC
- Large deletions: ~15-20%; entire exons removed; gene-level deletion by FISH or CNV array
- Missense: ~15%; often in ADD domain or ATPase domain; partial LOF or dominant-negative effect
- X-linked: ATRX is on chromosome Xq21; males require only one hit (hemizygous LOF sufficient); females require biallelic LOF or X-inactivation of the wild-type allele

**IHC:**
ATRX IHC: loss of nuclear staining in tumor cells (with intact staining in internal controls — endothelial cells, lymphocytes) = ATRX LOF; sensitivity ~85-90% for ATRX truncating mutation; combined with IDH1 R132H IHC and 1p/19q FISH for glioma classification; used in WHO 2021 CNS tumor classification as a mandatory biomarker for astrocytoma vs oligodendroglioma distinction

## Function

### ATRX-DAXX-H3.3 complex at telomeres

**H3.3 deposition mechanism:**
ATRX (ADD domain) recognizes H3K9me3 at telomeres → ATRX recruits DAXX → DAXX binds free H3.3 (replication-independent deposition) → ATRX ATPase displaces existing nucleosomes → DAXX deposits H3.3-H4 dimer → chromatin restored; telomeric repeat sequences (TTAGGG repeats) are inherently replication-difficult → ATRX-DAXX-H3.3 is essential for resolving telomeric replication stress; ATRX also functions at pericentromeric heterochromatin (major satellite repeats) via the same mechanism

**Normal telomere maintenance:**
Two mechanisms in normal and cancer cells:
1. **TERT (telomerase)**: RNA-templated extension of telomeric repeats; expressed in germ cells, stem cells, and TERT-reactivated cancers
2. **ALT (Alternative Lengthening of Telomeres)**: Homologous recombination-based; uses telomere DNA as template; requires ATRX LOF; marker: APBs (ALT-associated PML bodies), ultra-bright telomeric FISH signals, high C-circle levels

### ATRX LOF → ALT mechanism [^heaphy-2011-atrx-alt]

**ALT pathway:**
ATRX LOF → telomeric H3.3 deposition fails → telomeric chromatin becomes accessible → RPA (replication protein A) accumulates at telomeres → RAD51/RAD52-dependent recombination → break-induced replication (BIR) uses neighboring telomeric DNA as template → telomere length maintained without TERT; ALT-positive tumors show highly heterogeneous telomere lengths (contrasting uniform TERT-mediated extension); ALT is paradoxically associated with longer telomeres on average but with extreme telomere length heterogeneity

**ALT markers:**
- **APBs (ALT-associated PML bodies)**: PML protein + telomeric DNA co-localization by IF + FISH; most specific ALT marker; sensitivity ~80%
- **C-circles**: extrachromosomal circular telomeric ssDNA (CCCCAA repeats); detectable by rolling-circle amplification; quantitative ALT biomarker
- **Ultra-bright telomere signals**: telomere FISH shows heterogeneous, some very bright foci (>1% of cells with 4× mean signal)
- **ATRX IHC loss**: indirect marker; most practical for routine diagnostic use

### ATRX in IDH-mutant glioma lineage definition [^jiao-2012-atrx-glioma]

**WHO 2021 CNS tumor classification using ATRX:**
IDH-mutant diffuse gliomas are split by ATRX/1p19q:
- **ATRX LOF + TP53 mutation → IDH-mutant astrocytoma** (Grade 2, 3, or 4 depending on histology/CDKN2A)
- **ATRX intact + 1p/19q codeletion + TERT promoter mutation → IDH-mutant oligodendroglioma** (Grade 2 or 3)
- These are mutually exclusive lineages; rarely do tumors have ATRX LOF + 1p/19q codeletion simultaneously (true mixed phenotype exceedingly rare)

**Molecular progression of IDH-mutant astrocytoma:**
- Grade 2: IDH1 R132H + ATRX LOF + TP53 mutation; intact 1p/19q; no CDKN2A deletion
- Grade 3: above + increased mitoses/cellularity; some acquire CDKN2A deletion
- Grade 4: above + CDKN2A homozygous deletion (diagnostic of Grade 4 by WHO 2021); OR microvascular proliferation/necrosis; no EGFR amplification or TERT promoter mutation (contrast IDH-wildtype GBM)

## Mechanism

### Therapeutic implications of ATRX LOF

**ALT as a therapeutic vulnerability:**
ALT tumors depend on RAD52-mediated recombination; RAD52 inhibitors (BI-3536, VX-984) under preclinical investigation; ALT tumors show elevated PARP1 at telomeres → PARP inhibitor sensitivity in ALT-positive cell lines; ATR inhibitors (ceralasertib, AZD6738): ALT cells have elevated replication stress → ATR inhibition → synthetic lethality; Phase 1/2 trials of PARP + ATR inhibitor combinations in ATRX-mutant tumors (including astrocytoma and pancreatic NETs)

**Vorasidenib and IDH inhibition in ATRX-mutant astrocytoma:**
The primary driver in IDH-mutant astrocytoma is IDH1 R132H mutation (produces 2-HG oncometabolite); vorasidenib (brain-penetrant IDH1/2 inhibitor) FDA-approved August 2024 for Grade 2 IDH-mutant glioma; ATRX LOF is a co-mutation in most Grade 3-4 astrocytomas undergoing vorasidenib treatment; ATRX status does not predict vorasidenib response specifically — IDH mutation is the predictive biomarker

**No direct ATRX-targeted therapy:**
ATRX is a tumor suppressor (LOF); no small-molecule that restores ATRX function; therapeutic approach is to exploit downstream consequences: ALT vulnerability (PARP/ATR), IDH1 inhibition (vorasidenib), CDKN2A-deleted context (CDK4/6 inhibitors), and mTOR inhibition (ATRX-mutant pancreatic NETs respond to everolimus in Phase 3 RADIANT-3)

**RADIANT-3 (everolimus in pancreatic NETs):**
~40% of pancreatic NETs harbor ATRX or DAXX LOF → ALT mechanism; everolimus (mTOR inhibitor) Phase 3: PFS HR 0.35; FDA-approved for advanced pancreatic NETs; retrospective analyses show ATRX/DAXX-mutant pNETs may have longer PFS on everolimus vs wild-type; ATRX/DAXX mutations define a pNET molecular subgroup with ALT and metastatic tendency

## Connections

- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — ATRX LOF + IDH1 R132H + CDKN2A deletion → WHO Grade 4 IDH-mutant astrocytoma; IDH1+ATRX+TP53 triple mutant is the canonical high-grade astrocytoma genotype; ATRX LOF is a mandatory criterion for astrocytoma lineage (vs oligodendroglioma where ATRX is intact and 1p/19q deleted).
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — ATRX LOF + IDH1 → 2-HG → TET2 inhibition → DNA hypermethylation (G-CIMP); ATRX-DAXX deposits H3.3 at telomeric chromatin; ATRX LOF impairs H3.3 telomeric deposition → ALT mechanism → telomere lengthening independent of TERT; ATRX and TET2 cooperate in chromatin maintenance.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — ATRX LOF + IDH1 + TP53 mutation defines IDH-mutant astrocytoma Grade 3-4; TP53 and ATRX LOF co-occur in >80% of IDH-mutant astrocytomas; ATRX LOF → elevated replication stress at telomeres → p53 pathway activation; TP53 LOF relieves this brake → rapid astrocytoma progression.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A homozygous deletion occurs in ~50-70% of IDH-mutant astrocytoma Grade 4; CDK4/6 hyperactivation → RB1 → E2F proliferation; CDKN2A deletion defines WHO Grade 4 IDH-mutant astrocytoma (from Grade 3); ATRX LOF + CDKN2A deletion → worst IDH-mutant glioma prognosis.

[^heaphy-2011-atrx-alt]: Heaphy CM, de Wilde RF, Jiao Y, et al. Altered telomeres in tumors with ATRX and DAXX mutations. *Science.* 2011;333(6041):425. [doi:10.1126/science.1207313](https://doi.org/10.1126/science.1207313) · [PubMed 21719641](https://pubmed.ncbi.nlm.nih.gov/21719641/)
[^jiao-2012-atrx-glioma]: Jiao Y, Killela PJ, Reitman ZJ, et al. Frequent ATRX, CIC, FUBP1 and IDH mutations refine the classification of malignant gliomas. *Oncotarget.* 2012;3(7):709-722. [doi:10.18632/oncotarget.588](https://doi.org/10.18632/oncotarget.588) · [PubMed 22869205](https://pubmed.ncbi.nlm.nih.gov/22869205/)
