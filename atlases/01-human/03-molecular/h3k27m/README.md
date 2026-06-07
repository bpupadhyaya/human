---
schema: human-scale-entry/v1
id: h3k27m
name: H3K27M
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "H3K27M is a histone H3 driver mutation (H3F3A or HIST1H3B K27M); dominant-negative inhibition of PRC2/EZH2 → global H3K27me3 loss; defines WHO Grade 4 diffuse midline glioma; ONC201 (imipridone) FDA-approved for H3K27M+ DMG; H3K27M IHC is diagnostic."
aliases: ["H3K27M", "H3.3K27M", "H3F3A K27M", "HIST1H3B K27M", "histone H3.3 mutation glioma", "DIPG H3K27M", "diffuse midline glioma H3K27M", "H3K27me3 loss glioma", "H3 oncohistone", "histone K27M mutation"]
sources:
  - id: schwartzentruber-2012-h3f3a-glioma
    type: peer-reviewed
    cite: "Schwartzentruber J, Korshunov A, Liu XY, et al. Driver mutations in histone H3.3 and chromatin remodelling genes in paediatric glioblastoma. Nature. 2012;482(7384):226-231."
    doi: "10.1038/nature10833"
    pmid: "22286061"
    url: "https://doi.org/10.1038/nature10833"
  - id: khuong-quang-2012-h3k27m-dipg
    type: peer-reviewed
    cite: "Khuong-Quang DA, Buczkowicz P, Rakopoulos P, et al. K27M mutation in histone H3.3 defines clinically and biologically distinct subgroups of pediatric diffuse intrinsic pontine gliomas. Acta Neuropathol. 2012;124(3):439-447."
    doi: "10.1007/s00401-012-0998-0"
    pmid: "22661320"
    url: "https://doi.org/10.1007/s00401-012-0998-0"
cross_links:
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "H3K27M (histone H3.3 or H3.1 K27M) inserts mutant tail into EZH2 SET domain → dominant-negative PRC2 inhibition → global H3K27me3 loss despite EZH2 intact; one mutant H3 molecule inhibits all PRC2 in trans; EZH2 inhibitors paradoxically restore partial H3K27me3 in DMG."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion in ~15-25% H3K27M DMG (higher in DIPG/thalamic subtypes); NF1+H3K27M co-alteration common in spinal DMG; CDKN2A loss → CDK4/6 → RB1 → E2F proliferation; palbociclib + ONC201 combination being explored in H3K27M+CDKN2A-deleted DMG."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGFRA point mutations and amplification occur in ~25-35% of H3K27M DMG; PDGFRA → MAPK/PI3K → glioma proliferation; PDGFRA co-mutation with H3K27M accelerates malignancy; avapritinib and imatinib explored in PDGFRA-mutant DMG subsets."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYCN amplification in ~15-25% H3K27M spinal DMG and infant DIPG; MYCN + H3K27M → highly aggressive phenotype; BET inhibitors (JQ1) suppress MYCN in H3K27M glioma models; MYC/MYCN co-amplification predicts ONC201 resistance in some DMG series."
---

# H3K27M

## Overview

**H3K27M** (lysine 27-to-methionine substitution on histone H3) is an **oncohistone mutation** that defines **WHO Grade 4 diffuse midline glioma (DMG)** and represents one of the most mechanistically striking driver mutations in oncology — a single amino acid substitution in the histone H3 tail globally reprograms the epigenome of the entire tumor cell. H3K27M occurs predominantly in **H3F3A** (encoding histone H3.3, mostly pontine/thalamic) and in **HIST1H3B** or **HIST1H3C** (encoding histone H3.1, predominantly pontine). The K27M substitution creates a dominant-negative inhibitor of PRC2/EZH2, driving global loss of H3K27 trimethylation (H3K27me3) and de-repression of developmental transcription programs [^schwartzentruber-2012-h3f3a-glioma] [^khuong-quang-2012-h3k27m-dipg].

**H3K27M genetics:**
- **H3F3A K27M** (~75% of H3K27M DMG): mutations in the non-replicative H3.3 histone gene; predominantly pontine (DIPG) and thalamic locations; associated with older pediatric/young adult age; co-occurs with ACVR1, FGFR1, PDGFRA, or NF1 mutations
- **HIST1H3B/HIST1H3C K27M** (~25%): replicative H3.1 variants; exclusively pontine (DIPG); younger children; co-occurs with ACVR1 mutations and PPM1D alterations; slightly better prognosis than H3.3K27M
- **H3.2K27M (HIST2H3C)**: very rare; additional pontine cases
- **K27I (K27I substitution)**: distinct rare variant with similar PRC2 inhibitory mechanism; classified under DMG
- **H3G34R/V**: distinct H3F3A mutations affecting adult/young adult supratentorial hemispheric GBM; different biology from K27M — not classified as DMG

**Epidemiology:**
- Frequency: H3K27M in ~70-80% of all DIPG; ~50% of thalamic diffuse glioma; ~30% of spinal diffuse glioma
- Age: DIPG peak 6-9 years; thalamic DMG peak 10-15 years; adult H3K27M DMG (~15-20% of cases, median 25-30 years)
- No germline predisposition; somatic mutation; no familial clustering

## Structure

### H3K27M molecular mechanism — oncohistone

**Normal H3K27 methylation:**
Histone H3 lysine 27 (K27) is a key regulatory residue:
- H3K27me3 (EZH2/PRC2 → SET domain catalysis): marks silenced developmental genes (HOX clusters, cell fate inhibitors); required for maintenance of cell identity
- H3K27me1/2: intermediate states with distinct regulatory roles
- H3K27ac (acetyltransferases p300/CBP): marks active enhancers and promoters — mutually exclusive with H3K27me3

**The K→M substitution mechanism:**
The K27M mutant histone tail mimics the transition state of the PRC2 methyltransferase reaction:
1. EZH2 SET domain binds K27M peptide → K27M methionine fits the SET domain active site as a pseudo-substrate
2. K27M captures the SAM (S-adenosylmethionine) cofactor → stalls catalysis → permanently occupies the EZH2 active site
3. This **dominant-negative** mechanism means: although K27M nucleosomes represent only ~3-17% of total H3 (one mutant allele), EZH2 bound to K27M-containing nucleosomes cannot methylate remaining wild-type H3 → global H3K27me3 loss throughout the genome
4. H3K27me3 drops from ~50% of H3 to ~3-5%; H3K27me2 reduced similarly
5. H3K27ac increases at previously repressed enhancers → de-repression of PDGFRA, MET, CDK6, and stem cell programs

**Paradox of residual H3K27me3:**
Despite global H3K27me3 loss, ~3-5% of genomic loci retain H3K27me3 in K27M tumors — particularly at polycomb target genes critical for identity (CDX2, HOX genes); this residual H3K27me3 maintains essential gene silencing; H3K27me3 at these select loci is disproportionately dependent on JARID2 (PRC2 cofactor); this residual methylation is the target of panobinostat and other HDAC inhibitors that partially restore H3K27me3

### H3K27M protein interaction surface

**K27M and the EZH2 SET domain:**
The K27M substitution specifically occludes the lysine-binding channel of EZH2; methionine (non-ionizable, uncharged) cannot accept SAM-methyl group transfer; the K27M tail binds with ~100-fold higher affinity to EZH2 SET domain than wild-type K27; crystal structure (Justin 2016, eLife) shows K27M methionine deep in the active site with SAM cofactor stalled; this structural insight enables rational drug development targeting the K27M-EZH2 interaction

**Downstream consequences in DMG:**
- H3K27me3 loss → PRC2 target gene de-repression: PDGFRA, CDK6, MET, AXL
- H3K27ac gain at DMG-specific enhancers → PDGFRA super-enhancer activation
- H3K27me3 loss at CDKN2A → CDK4/6 activation (even without genetic CDKN2A deletion)
- Neural stem cell gene re-expression: SOX2, OLIG2, NESTIN → maintained stemness
- HOX gene dysregulation → block in neuroglial differentiation

## Function

### H3K27M in gliomagenesis

**Cell of origin:**
H3K27M mutations arise in **neural stem cells or oligodendrocyte precursor cells (OPCs)** at critical developmental windows during neurogenesis:
- Pontine DMG (DIPG): arises from a progenitor population in the ventral pons during the peak of oligodendrogenesis (ages 5-10); the ventral pons-specific progenitor pool is particularly sensitive to H3K27M at this developmental stage
- Thalamic DMG: arises from thalamic precursors with a different developmental timing
- H3K27M in non-neural cells does not produce gliomas — cell context is required

**Cooperation with co-driver mutations:**
H3K27M alone is insufficient to produce glioma; cooperating mutations define molecular subgroups of H3K27M DMG:
- **ACVR1 (ALK2) mutations** (~20-25%): gain-of-function BMP signaling → SMAD1/5/8 activation; exclusively in H3.1K27M DIPG; targeted by BMP pathway inhibitors
- **PDGFRA mutations/amplification** (~25-35%): RTK activation → MAPK/PI3K; targeted by PDGFRA inhibitors
- **PIK3CA/PIK3R1 mutations** (~15-20%): PI3K pathway; mTOR inhibitors being explored
- **NF1 mutations** (~10-15%): RAS hyperactivation; co-driver in spinal H3K27M DMG

**H3K27M as lineage marker:**
H3K27M IHC (anti-H3.3K27M, clone D5E7) is pathognomonic for DMG:
- Sensitivity ~95% for H3K27M+ DMG; negative in all H3K27M-negative gliomas
- H3K27M also detected in CSF cell-free DNA (cfDNA) and tumor-derived cell-free RNA → liquid biopsy for monitoring
- Diagnostic per 2021 WHO Classification of CNS Tumors (5th edition)

## Mechanism

### Therapeutic strategies in H3K27M DMG

**ONC201 (imipridone) — FDA approved 2024:**
ONC201 is a first-in-class imipridone compound with multi-modal mechanism:
1. **DRD2/DRD5 (dopamine receptor 2/5) antagonism**: allosteric modulation → ISR (integrated stress response) activation via HRI kinase → eIF2α phosphorylation → ATF4 activation → apoptosis
2. **ClpP mitochondrial protease agonism**: direct activation → mitochondrial protein degradation → bioenergetic collapse; H3K27M gliomas show unique ClpP dependency
3. **Mevalonate pathway disruption**: ONC201 inhibits MVD (mevalonate diphosphate decarboxylase) → cholesterol/isoprenoid depletion → synergy with H3K27M epigenetic vulnerability

**Phase 2 data (ACTION study, multicenter):** ORR ~22-30% in relapsed/refractory H3K27M+ DMG; DCR ~60-70%; median OS ~15-17 months in H3F3A K27M vs ~10-12 months in HIST1H3B K27M; FDA granted accelerated approval (April 2024) for adults and pediatric patients ≥1 year with relapsed/refractory H3K27M-mutant diffuse glioma; **first drug approved specifically for an epigenetic oncohistone mutation**

**ONC201 resistance mechanisms:** MYCN/MYC amplification reduces ONC201 sensitivity; EGFR amplification → bypass proliferation; TP53 mutations reduce apoptotic response; combination strategies (ONC201 + MEK inhibitor, ONC201 + HDAC inhibitor) under investigation

**Panobinostat (HDAC inhibitor):**
Rationale: H3K27M-driven H3K27me3 loss → H3K27ac gain at oncogene enhancers; panobinostat (pan-HDAC inhibitor) → H3K27ac reduction → partial H3K27me3 restoration; Phase 1 PBTC-047: ORR modest but disease control signals; crosses blood-brain barrier at therapeutic concentrations; Phase 2 PBTC-047b ongoing; combination panobinostat + ONC201 in preclinical models shows synergy

**Radiation therapy:**
External beam RT (54 Gy in 30 fractions) remains the **only standard initial treatment** for DIPG/DMG; median TTP ~6-8 months after RT; RT is palliative, not curative; flash-RT (ultra-high dose rate) being explored; re-irradiation at progression used in selected cases

**CDK4/6 inhibitors:**
Rationale: H3K27me3 loss at CDKN2A locus → CDK4/6 hyperactivation even without CDKN2A deletion; palbociclib and ribociclib being explored in DMG Phase 1/2; CDK4/6i + ONC201 combination shows preclinical synergy in H3K27M cell lines

## Connections

- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — H3K27M (histone H3.3 or H3.1 K27M) inserts mutant tail into EZH2 SET domain → dominant-negative PRC2 inhibition → global H3K27me3 loss despite EZH2 intact; one mutant H3 molecule inhibits all PRC2 in trans; EZH2 inhibitors paradoxically restore partial H3K27me3 in DMG.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion in ~15-25% H3K27M DMG (higher in DIPG/thalamic subtypes); NF1+H3K27M co-alteration common in spinal DMG; CDKN2A loss → CDK4/6 → RB1 → E2F proliferation; palbociclib + ONC201 combination being explored in H3K27M+CDKN2A-deleted DMG.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGFRA point mutations and amplification occur in ~25-35% of H3K27M DMG; PDGFRA → MAPK/PI3K → glioma proliferation; PDGFRA co-mutation with H3K27M accelerates malignancy; avapritinib and imatinib explored in PDGFRA-mutant DMG subsets.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYCN amplification in ~15-25% H3K27M spinal DMG and infant DIPG; MYCN + H3K27M → highly aggressive phenotype; BET inhibitors (JQ1) suppress MYCN in H3K27M glioma models; MYC/MYCN co-amplification predicts ONC201 resistance in some DMG series.

[^schwartzentruber-2012-h3f3a-glioma]: Schwartzentruber J, Korshunov A, Liu XY, et al. Driver mutations in histone H3.3 and chromatin remodelling genes in paediatric glioblastoma. *Nature.* 2012;482(7384):226-231. [doi:10.1038/nature10833](https://doi.org/10.1038/nature10833) · [PubMed 22286061](https://pubmed.ncbi.nlm.nih.gov/22286061/)
[^khuong-quang-2012-h3k27m-dipg]: Khuong-Quang DA, Buczkowicz P, Rakopoulos P, et al. K27M mutation in histone H3.3 defines clinically and biologically distinct subgroups of pediatric diffuse intrinsic pontine gliomas. *Acta Neuropathol.* 2012;124(3):439-447. [doi:10.1007/s00401-012-0998-0](https://doi.org/10.1007/s00401-012-0998-0) · [PubMed 22661320](https://pubmed.ncbi.nlm.nih.gov/22661320/)
