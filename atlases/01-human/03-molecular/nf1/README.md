---
schema: human-scale-entry/v1
id: nf1
name: NF1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "NF1 (neurofibromin) is a RasGAP; LOF → sustained RAS-GTP → MAPK/PI3K hyperactivation; germline NF1 syndrome: café-au-lait macules, neurofibromas, MPNST risk ~10%; somatic NF1 loss in GBM, NSCLC, melanoma; MEK inhibitor selumetinib FDA-approved for NF1 plexiform neurofibromas."
aliases: ["NF1", "neurofibromin", "neurofibromatosis type 1 gene", "NF1 RasGAP", "neurofibromatosis 1", "NF1 tumor suppressor", "NF1 MPNST", "NF1 plexiform neurofibroma", "NF1 GBM", "RasGAP NF1"]
sources:
  - id: legius-2021-nf1-consensus
    type: peer-reviewed
    cite: "Legius E, Messiaen L, Wolkenstein P, et al. Revised diagnostic criteria for neurofibromatosis type 1 and Legius syndrome: an international consensus recommendation. Genet Med. 2021;23(8):1506-1513."
    doi: "10.1038/s41436-021-01170-5"
    pmid: "33976407"
    url: "https://doi.org/10.1038/s41436-021-01170-5"
  - id: dombi-2016-selumetinib-nf1
    type: peer-reviewed
    cite: "Dombi E, Baldwin A, Marcus LJ, et al. Activity of Selumetinib in Neurofibromatosis Type 1-Related Plexiform Neurofibromas. N Engl J Med. 2016;375(26):2550-2560."
    doi: "10.1056/NEJMoa1605943"
    pmid: "28029918"
    url: "https://doi.org/10.1056/NEJMoa1605943"
cross_links:
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "NF1 encodes neurofibromin, a RasGAP that converts RAS-GTP (active) → RAS-GDP (inactive); NF1 LOF functionally equivalent to activating KRAS mutations; both accumulate RAS-GTP → MAPK/ERK hyperactivation; NF1 + KRAS co-alteration is extremely rare (presumed synthetic lethal)."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "NF1 LOF → RAS hyperactivation → MEK1/2 → ERK1/2 hyperphosphorylation in NF1 syndrome tumors (neurofibromas, MPNST, glioma, PHEO); selumetinib (MEK inhibitor): FDA-approved for NF1 plexiform neurofibromas (SPRINT Phase 2); ERK-dependent transcription drives neurofibroma growth."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "NF1 LOF → RAS → PI3K → AKT → mTORC1; neurofibromin also binds TORC1 directly (RAS-independent); mTOR inhibitors (everolimus/sirolimus) active in NF1 optic pathway glioma; rapamycin prevents neurofibroma growth in NF1 mouse models; NF1-driven tumors are mTOR-dependent."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "NF1 LOF → excess EGFR at cell surface (neurofibromin promotes EGFR endocytosis, similar to NF2/merlin); NF1 LOF + EGFR amplification co-occur in GBM; EGFR inhibitors have limited activity in NF1-mutant tumors; EGFR/RAS dual blockade explored in GBM."
---

# NF1

## Overview

**NF1** (neurofibromin 1) encodes **neurofibromin**, a 2,818-amino-acid (327 kDa) RasGAP (GTPase-activating protein) that is the largest known tumor suppressor protein. Neurofibromin is ubiquitously expressed, with highest levels in neural tissue (neurons, Schwann cells, oligodendrocytes). Its primary function is to accelerate intrinsic RAS GTPase activity — converting active RAS-GTP to inactive RAS-GDP — thereby restraining MAPK/PI3K proliferative signaling. Loss of NF1 function, whether germline (neurofibromatosis type 1 syndrome) or somatic, results in constitutive RAS pathway hyperactivation functionally equivalent to an activating RAS mutation [^legius-2021-nf1-consensus].

**NF1 gene:**
- Chromosome 17q11.2; 350 kb genomic locus; 57 coding exons; one of the largest human genes
- mRNA: 13 kb; protein: 2,818 aa (327 kDa)
- Among the highest germline mutation rates of any human gene (~1 in 3,000 live births)
- Germline NF1 syndrome: autosomal dominant; ~50% de novo mutations; full penetrance, variable expressivity

**NF1 alterations across tumor types:**

| Tumor type | Frequency | Context |
|---|---|---|
| MPNST (NF1-associated) | ~50-60% LOF | Somatic second hit in germline NF1 carrier; plexiform → malignant transformation |
| GBM (glioblastoma) | ~15-20% | Somatic; often co-occurs with EGFR amplification; no germline predisposition |
| NSCLC (lung adenocarcinoma) | ~15-20% | Somatic; predominantly concurrent with other drivers; NF1 co-mutation with KRAS rare |
| Melanoma | ~14% | Somatic; triple-WT melanoma (NF1-mutant, BRAF-WT, RAS-WT) is a distinct subtype |
| Breast cancer (TNBC) | ~10-15% | Somatic; confers RAS dependency |
| PHEO/PGL (Cluster 2) | NF1 germline | Epinephrine-secreting; usually benign; RET/RAS pathway |

## Structure

### Neurofibromin protein architecture

**N-terminal domain (aa 1-1171):**
Large N-terminal region with cysteine-serine-rich domain (CSRD, aa 197-607); interacts with syndecan and calmodulin; regulates plasma membrane localization; involved in TORC1 binding independent of RasGAP activity; CSRD mutations → severe NF1 phenotype with optic glioma and cognitive impairment

**GRD — GTPase-activating protein-related domain (aa 1172-1473):**
The catalytic core of neurofibromin; directly homologous to other RasGAP family members (RASA1/p120RasGAP, GAP1); the GRD inserts an **arginine finger** (Arg1276) into the active site of RAS at switch II → positions the catalytic water molecule → 1,000-fold acceleration of intrinsic GTPase activity; missense mutations within the GRD (e.g., Arg1276Pro) → complete LOF; all three RAS isoforms (HRAS, KRAS, NRAS) are substrates of neurofibromin GRD

**C-terminal domain (aa 1474-2818):**
SEC-PH domain (Sec14-like pleckstrin homology): binds phosphoinositide lipids → plasma membrane recruitment of neurofibromin; RAS-related protein domains; synectin-binding domain near C-terminus for synaptic localization; CTD frameshift/truncating mutations cause loss of GRD context and membrane targeting

**Alternatively spliced isoforms:**
- **Exon 23a**: brain-specific isoform (type II neurofibromin); reduced GRD catalytic efficiency; expressed in CNS neurons; preferential expression → may explain neurological manifestations
- **Exon 48a**: cardiac/muscle isoform; expressed during embryogenesis; exon 48a-containing neurofibromin interacts with RALGDS (RalGEF) → Ral pathway

### NF1 germline variants

**Pathogenic variant types:**
- Frameshift/truncating (~80% of NF1 pathogenic variants): protein unstable → rapidly degraded; complete LOF
- Missense within GRD: partial or complete LOF depending on position
- Whole-gene deletion (chromosome 17q11.2 microdeletion): ~5-10% of NF1 cases; more severe phenotype (>1,000 neurofibromas, learning disability, MPNST risk ~15-20%)
- Deep intronic/splicing variants: underdetected by exome sequencing; whole-genome sequencing required
- **Somatic second hit**: NF1 syndrome tumor suppressor requires biallelic inactivation; second somatic hit (LOH, frameshift, or intragenic deletion at germline allele) needed for neurofibroma/MPNST formation

## Function

### RasGAP function and RAS signaling

**Mechanism of GTPase acceleration:**
Under normal signaling, receptor tyrosine kinases (EGFR, PDGFR, RET) → adapter proteins (GRB2, SOS) → RAS GDP→GTP exchange (activation) → RAS-GTP activates RAF/MEK/ERK and PI3K/AKT/mTOR; neurofibromin GRD enters the RAS-effector interface → inserts arginine finger → stabilizes the transition state for GTP hydrolysis → 1,000-fold acceleration → RAS inactivation; without functional neurofibromin, RAS-GTP persists → constitutive MAPK/PI3K

**NF1 LOF = activating RAS mutation:**
Functionally, homozygous NF1 LOF is indistinguishable from an activating KRAS G12D mutation in terms of downstream MAPK output; key differences: (1) NF1-LOF acts on all three RAS isoforms; (2) NF1-LOF can be reversed by upstream RTK pathway changes; (3) NF1 + KRAS co-mutations are extremely rare and potentially synthetic lethal (maximum RAS-GTP with no escape mechanism)

### NF1 syndrome manifestations

**Diagnostic criteria (Legius 2021 consensus):** [^legius-2021-nf1-consensus]
≥2 of the following required for diagnosis:
- ≥6 café-au-lait macules (≥5 mm prepubertal; ≥15 mm postpubertal)
- ≥2 neurofibromas (any type) or ≥1 plexiform neurofibroma
- Axillary/inguinal freckling (Crowe sign)
- Optic pathway glioma
- ≥2 Lisch nodules (iris hamartomas) or ≥2 choroidal abnormalities on OCT
- Distinctive osseous lesion (sphenoid wing dysplasia, tibial dysplasia)
- Pathogenic NF1 variant
- First-degree relative with NF1

**Tumor spectrum in NF1 syndrome:**
- **Cutaneous neurofibromas**: virtually universal by adulthood; benign; thousands in severely affected patients; NF1+p53 LOF → not malignant
- **Plexiform neurofibromas**: ~30-50% of NF1 patients; infiltrative, along nerve plexuses; precursor lesion for MPNST
- **MPNST**: ~10% lifetime risk (vs <0.1% in general population); plexiform → MPNST transformation
- **Optic pathway glioma (OPG)**: ~15-20%; usually BRAF/KIAA1549 fusion negative (pure NF1 LOF); most respond to MEK inhibition
- **GBM/astrocytoma**: rare; adult-onset; somatic NF1 co-mutation
- **Leukemia** (juvenile myelomonocytic leukemia, JMML): RAS hyperactivation in myeloid precursors; NF1 LOF in JMML is somatic
- **Cardiovascular**: pulmonary artery stenosis, renovascular hypertension
- **PHEO/PGL**: rare; NF1-associated PHEO is epinephrine-secreting (adrenal), mostly benign

## Mechanism

### MEK inhibition — selumetinib

**SPRINT Pediatric Phase 2 (Dombi 2016):** [^dombi-2016-selumetinib-nf1]
N=24 pediatric NF1 patients with inoperable plexiform neurofibromas; selumetinib (AZD6244) 25 mg/m² BID oral; primary endpoint: ≥20% volumetric reduction by MRI; ORR 17/24 (71%); 12/24 (50%) sustained ≥20% tumor volume reduction; no complete responses; grade 3/4 toxicity: 4/24; FDA approval granted June 2020 for NF1 plexiform neurofibromas in pediatric patients ≥2 years; first FDA-approved therapy for NF1

**Mechanism:** selumetinib (MEK1/2 inhibitor, ATP non-competitive) → ERK1/2 phosphorylation ↓ → cyclin D1 ↓ → G1 arrest in neurofibroma Schwann cells; MEK inhibition does NOT reverse NF1 LOF but blocks the key downstream effector

**Clinical limitations:** selumetinib does not convert plexiform neurofibromas to MPNST therapy; MPNST trials with MEK inhibitors have been largely negative (CDKN2A + PRC2 loss in MPNST adds bypass pathways); resistance mechanisms include PI3K/AKT upregulation

### mTOR inhibitors

Neurofibromin acts on mTOR via two mechanisms: (1) RAS-GTP → PI3K → AKT → TSC2 inactivation → mTORC1; (2) neurofibromin directly binds raptor (mTORC1 component) via CSRD, limiting mTORC1 activity independent of RAS; NF1 LOF → both mechanisms → mTORC1 hyperactivation; everolimus/sirolimus show preclinical activity in NF1 mouse models and NF1 optic pathway glioma; combination MEK + mTOR under investigation (trametinib + everolimus Phase 2 in NF1-MPNST, NCT03433144)

### EGFR and receptor context

Neurofibromin promotes EGFR internalization and lysosomal degradation (independent of GRD); NF1 LOF → EGFR surface retention → enhanced EGFR signaling; this mechanism parallels NF2/merlin regulation of EGFR; in GBM (NF1 LOF + EGFR amplification), dual NF1/EGFR alteration → maximum RAS + RTK → highly aggressive phenotype; EGFR monotherapy ineffective in NF1-mutant GBM due to downstream RAS constitutive activation

## Connections

- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — NF1 encodes neurofibromin, a RasGAP that converts RAS-GTP (active) → RAS-GDP (inactive); NF1 LOF functionally equivalent to activating KRAS mutations; both accumulate RAS-GTP → MAPK/ERK hyperactivation; NF1 + KRAS co-alteration is extremely rare (presumed synthetic lethal).
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — NF1 LOF → RAS hyperactivation → MEK1/2 → ERK1/2 hyperphosphorylation in NF1 syndrome tumors (neurofibromas, MPNST, glioma, PHEO); selumetinib (MEK inhibitor): FDA-approved for NF1 plexiform neurofibromas (SPRINT Phase 2); ERK-dependent transcription drives neurofibroma growth.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — NF1 LOF → RAS → PI3K → AKT → mTORC1; neurofibromin also binds TORC1 directly (RAS-independent); mTOR inhibitors (everolimus/sirolimus) active in NF1 optic pathway glioma; rapamycin prevents neurofibroma growth in NF1 mouse models; NF1-driven tumors are mTOR-dependent.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — NF1 LOF → excess EGFR at cell surface (neurofibromin promotes EGFR endocytosis, similar to NF2/merlin); NF1 LOF + EGFR amplification co-occur in GBM; EGFR inhibitors have limited activity in NF1-mutant tumors; EGFR/RAS dual blockade explored in GBM.

[^legius-2021-nf1-consensus]: Legius E, Messiaen L, Wolkenstein P, et al. Revised diagnostic criteria for neurofibromatosis type 1 and Legius syndrome: an international consensus recommendation. *Genet Med.* 2021;23(8):1506-1513. [doi:10.1038/s41436-021-01170-5](https://doi.org/10.1038/s41436-021-01170-5) · [PubMed 33976407](https://pubmed.ncbi.nlm.nih.gov/33976407/)
[^dombi-2016-selumetinib-nf1]: Dombi E, Baldwin A, Marcus LJ, et al. Activity of Selumetinib in Neurofibromatosis Type 1-Related Plexiform Neurofibromas. *N Engl J Med.* 2016;375(26):2550-2560. [doi:10.1056/NEJMoa1605943](https://doi.org/10.1056/NEJMoa1605943) · [PubMed 28029918](https://pubmed.ncbi.nlm.nih.gov/28029918/)
