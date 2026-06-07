---
schema: human-scale-entry/v1
id: tet2
name: TET2
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "TET2 encodes a 5-methylcytosine dioxygenase that converts 5mC → 5hmC → 5fC → 5caC → demethylation via TDG/BER; TET2 loss-of-function mutations occur in ~20% CHIP (most common), ~20% MDS, ~60% CMML, and ~60-80% AITL; IDH1/2-produced 2-HG inhibits TET2."
aliases: ["TET2", "TET2 mutation", "ten-eleven translocation 2", "TET2 CHIP", "TET2 AITL", "TET2 CMML", "TET2 MDS", "DNA demethylation TET2"]
sources:
  - id: delhommeau-2009-tet2-myeloid
    type: peer-reviewed
    cite: "Delhommeau F, Dupont S, Della Valle V, et al. Mutation in TET2 in myeloid cancers. N Engl J Med. 2009;360(22):2289-2301."
    doi: "10.1056/NEJMoa0810069"
    pmid: "19474426"
    url: "https://doi.org/10.1056/NEJMoa0810069"
  - id: palomero-2014-ptcl-epigenetics
    type: peer-reviewed
    cite: "Palomero T, Couronné L, Khiabanian H, et al. Recurrent mutations in epigenetic regulators, RHOA and FYN kinase in peripheral T cell lymphomas. Nat Genet. 2014;46(2):166-170."
    doi: "10.1038/ng.2872"
    pmid: "24413734"
    url: "https://doi.org/10.1038/ng.2872"
cross_links:
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "TET2 and DNMT3A frequently co-mutate in CHIP (~15% doublet), MDS, and AITL/PTCL; DNMT3A adds methylation (de novo) while TET2 removes it; their co-loss → genome-wide hypermethylation of differentiation genes; TET2+DNMT3A+RHOA G17V is the canonical AITL triplet."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH2 mutations → 2-HG → TET2 dioxygenase inhibition → epigenetic phenocopy of TET2 loss-of-function; IDH2 and TET2 mutations are mutually exclusive in AML but co-occur in AITL (distinct mechanism); enasidenib reverses 2-HG-mediated TET2 inhibition."
  - target: 01-human/03-molecular/srsf2
    relation: connects-to
    note: "TET2+SRSF2 P95H co-mutation occurs in ~30% of CMML (canonical doublet); TET2 drives epigenetic dysregulation while SRSF2 drives splicing errors; together → monocytic lineage expansion; TET2+SRSF2 double-mutant knockin mice develop CMML-like disease in 100% of animals by 6 months."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "TET2 (demethylation) and EZH2 (H3K27me3) act in opposing epigenetic pathways; TET2 loss and EZH2 gain-of-function both impair HSC differentiation; co-mutation in MDS/MPN → compound epigenetic dysfunction and accelerated AML transformation."
---

# TET2

## Overview

**TET2 (Ten-Eleven Translocation 2)** is a member of the TET dioxygenase family (TET1, TET2, TET3) and the central enzyme of active DNA demethylation in mammals. TET2 catalyzes the oxidation of **5-methylcytosine (5mC)** → **5-hydroxymethylcytosine (5hmC)** → **5-formylcytosine (5fC)** → **5-carboxylcytosine (5caC)**, with each oxidized intermediate recognized and excised by thymine DNA glycosylase (TDG) via base excision repair (BER) → restoration of unmethylated cytosine. This iterative oxidation pathway is the primary mechanism of targeted CpG demethylation at gene regulatory elements in human cells. TET2 was identified as a recurrently mutated gene in myeloid malignancies in 2009 [^delhommeau-2009-tet2-myeloid], establishing it as the first demonstrated DNA demethylation enzyme implicated in human cancer. TET2 loss-of-function mutations are now recognized as the most common mutation in **clonal hematopoiesis of indeterminate potential (CHIP)** (~20-30%), occurring in ~20% MDS, ~60% CMML, ~20% MPN, and — critically — ~60-80% of **angioimmunoblastic T-cell lymphoma (AITL)** and related nodal T-follicular helper (TFH) lymphomas [^palomero-2014-ptcl-epigenetics].

**TET2 in hematologic malignancies:**
- **CHIP:** TET2 ~20-30% (most common single CHIP gene); TET2 CHIP carries elevated cardiovascular risk and myeloid malignancy progression risk (~1%/year); TET2 CHIP monocytes produce excess IL-6/IL-1β contributing to atherosclerosis
- **MDS:** TET2 ~20%; no direct prognostic impact alone; IPSS-M incorporates TET2 in context of co-mutations; azacitidine may be particularly effective in TET2-mutant MDS
- **CMML:** TET2 ~60% — most common CMML mutation; TET2+SRSF2 doublet in ~30% CMML; TET2 allele burden and zygosity (heterozygous vs. biallelic) affect monocytic expansion
- **MPN (ET/PV/MF):** TET2 ~10-20%; TET2+JAK2 V617F → worse MF prognosis; TET2 clonal hematopoiesis precedes JAK2 V617F in some patients
- **AITL/nodal TFH lymphoma:** TET2 ~60-80%; earliest genetic event (pre-malignant TFH clone); co-mutations DNMT3A ~30%, RHOA G17V ~50-70%, IDH2 R172K ~20-30%; TET2 mutations in peripheral blood non-T cells of AITL patients confirms pre-malignant hematopoietic origin
- **PTCL-NOS:** TET2 ~20%; less prevalent than AITL but contributes to epigenetic dysregulation

## Structure

### TET2 protein architecture

TET2 is a large 2002-amino-acid, 224 kDa protein with a bipartite catalytic domain:

**N-terminal region (1-1127, largely disordered):**
- Intrinsically disordered; functions as regulatory scaffold
- Unlike TET1/TET3, TET2 has NO N-terminal CXXC domain (evolutionarily deleted; chromosome 4q24 inversion separated TET2 from the CXXC4/IDAX gene → IDAX now recruits TET2 to unmethylated CpG islands via its CXXC domain)
- Interacts with OGT (O-GlcNAc transferase) → mutual stabilization; OGT O-GlcNAcylates histone H2B → downstream H3K4 methylation → active gene expression
- Contains binding site for DNMT3A (TET2-DNMT3A interaction → functional antagonism at bivalent promoters)

**Double-stranded β-helix (DSBH/cupin fold) domain (1128-1481, catalytic core A):**
- First DSBH module; required for structural integrity and Fe²⁺ coordination; contains HXD...H iron-binding motif (His1881, Asp1883, His1881 — canonical triad in catalytic domain B)
- Mutations in this region disrupt catalytic activity

**Cys-rich domain (1481-1843, contains catalytic core B):**
- C-terminal extension specific to TET family; spatially contacts DSBH → together form the active site
- Fe²⁺ chelated at catalytic center; α-KG (2-oxoglutarate) occupies cofactor pocket; O₂ activated → Fe⁴⁺=O intermediate → methyl group hydroxylation
- **Hotspot mutation regions:** Distributed throughout both DSBH and Cys-rich regions; no single dominant hotspot (unlike IDH1 R132, JAK2 V617F); R1896H and H1382Y are recurrent but no single residue dominates

### TET2 catalytic mechanism

**Step-by-step demethylation:**
1. TET2 binds double-stranded DNA via Cys-rich domain + DSBH (non-sequence-specific genome-wide recruitment; sequence-specific via partner proteins IDAX/CXXC4, SIN3A, OGT)
2. Fe²⁺ + α-KG + O₂ → Fe⁴⁺=O (oxo-ferryl intermediate) at active site → oxidizes 5mC methyl group → 5hmC
3. Second catalytic cycle: Fe²⁺ + α-KG + O₂ → 5hmC → 5fC
4. Third cycle: 5fC → 5caC
5. TDG recognizes 5fC or 5caC → glycosylase activity → abasic site → BER → unmodified cytosine inserted

**5hmC as a stable epigenetic mark:**
5hmC is not merely an intermediate — it is a stable epigenetic mark at enhancers and gene bodies that impairs DNMT1 maintenance methylation; globally, 5hmC marks active enhancers (together with H3K4me1/H3K27ac) and is specifically depleted in cancers with TET2 loss-of-function.

**2-HG inhibition of TET2:**
IDH1 R132 and IDH2 R140/R172 neomorphic mutations produce 2-hydroxyglutarate (2-HG) as an oncometabolite; 2-HG is a structural analog of α-KG → competitively inhibits TET2 (and other α-KG-dependent dioxygenases including KDM histone demethylases and EglN/PHD prolyl hydroxylases) → global hypermethylation → glioma CpG island methylator phenotype (G-CIMP); AML hypermethylation signature. IDH1/2 mutant and TET2 mutant tumors have overlapping methylation signatures (functional equivalence in AML) — however they are NOT mutually exclusive in AITL (where they cooperate through distinct mechanisms).

## Function

### Normal TET2 roles in hematopoiesis

**HSC self-renewal regulation:**
TET2-null mice develop a CMML-like disease over 12-18 months due to HSC clonal expansion with monocytic skewing; TET2-null HSCs have enhanced self-renewal (increased reconstitution capacity in transplant assays) but defective differentiation; 5hmC is globally reduced in TET2-null HSCs → hypermethylation of differentiation-associated gene regulatory elements → block at myeloid/lymphoid progenitor stages.

**TFH cell identity:**
In the lymphoid compartment, TET2 demethylates regulatory elements of T-follicular helper (TFH) cell-identity genes (CXCR5, BCL6, ICOS, IL-21) → promotes TFH differentiation; TET2 loss → hypermethylation of TFH/regulatory gene loci → paradoxically impairs terminal differentiation → pre-malignant TFH clone expansion → AITL substrate. This explains the lymphoid tropism of TET2 mutations in AITL despite TET2 being a general hematopoietic gene.

**Inflammatory cytokine regulation:**
TET2 demethylates the promoters of anti-inflammatory genes (e.g., IL-10, IL-12) and represses IL-6 production; TET2-null macrophages produce excess IL-6 and IL-1β → systemic inflammation → atherosclerosis acceleration in TET2 CHIP; TET2 mutation in CHIP monocytes → elevated circulating IL-6/IL-1β → cardiovascular event risk independent of traditional risk factors.

### Vitamin C (ascorbate) and TET activity

Vitamin C (L-ascorbate) is a cofactor that reduces Fe³⁺ → Fe²⁺ at the TET2 active site, regenerating the catalytically active ferrous state → enhances TET2 activity → increased 5hmC globally. Vitamin C supplementation can restore 5hmC levels in TET2-heterozygous HSCs and slow clonal expansion in mouse models. Clinical trials of high-dose IV vitamin C in combination with azacitidine are ongoing in TET2-mutant AML/MDS (NCT03397173); preclinical synergy demonstrated.

## Mechanism

### TET2 as a therapeutic target

**No direct TET2 activator approved:**
TET2 loss-of-function cannot be directly reversed by a small molecule inhibitor; indirect strategies:
- **Azacitidine/decitabine (HMA):** Preferential activity in TET2-mutant MDS/CMML (higher response rates in TET2-mutant vs. DNMT3A-mutant disease in retrospective analyses); mechanism: HMAs deplete DNMT1 → passive demethylation partially compensates for TET2 loss
- **Vitamin C (ascorbate):** Enhances residual TET2 activity in heterozygous mutations; under clinical investigation
- **IDH inhibitors (enasidenib, ivosidenib):** Reduce 2-HG → restore TET2 activity in IDH-mutant malignancies (specifically relevant when IDH inhibition rescues TET2-dependent demethylation)
- **EZH2 inhibitors (tazemetostat):** Counteract the synergistic epigenetic repression when TET2 loss co-occurs with EZH2 gain-of-function in MDS/MPN

**AITL therapeutic implications:**
TET2+DNMT3A+RHOA G17V → epigenetic dysregulation → HMA therapy (azacitidine) shows activity in AITL; romidepsin (HDAC inhibitor) + azacitidine synergistic in TET2-mutant AITL models; IDH2 R172K (co-mutation in ~20-30% AITL) → enasidenib targeting investigated.

**Prognostic significance:**
In MDS/CMML: TET2 mutation alone is not a major adverse prognostic marker (unlike TP53, ASXL1); TET2 mutations are intermediate; particularly adverse when biallelic. In CHIP: TET2 CHIP → ~1%/year malignancy progression; cardiovascular risk; cardiology monitoring recommended in TET2-CHIP carriers with elevated hsCRP.

## Connections

- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — TET2 and DNMT3A frequently co-mutate in CHIP (~15% doublet), MDS, and AITL/PTCL; DNMT3A adds methylation (de novo) while TET2 removes it; their co-loss → genome-wide hypermethylation of differentiation genes; TET2+DNMT3A+RHOA G17V is the canonical AITL triplet.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH2 mutations → 2-HG → TET2 dioxygenase inhibition → epigenetic phenocopy of TET2 loss-of-function; IDH2 and TET2 mutations are mutually exclusive in AML but co-occur in AITL (distinct mechanism); enasidenib reverses 2-HG-mediated TET2 inhibition.
- `connects-to` → **[SRSF2](../../03-molecular/srsf2/README.md)** — TET2+SRSF2 P95H co-mutation occurs in ~30% of CMML (canonical doublet); TET2 drives epigenetic dysregulation while SRSF2 drives splicing errors; together → monocytic lineage expansion; TET2+SRSF2 double-mutant knockin mice develop CMML-like disease in 100% of animals by 6 months.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — TET2 (demethylation) and EZH2 (H3K27me3) act in opposing epigenetic pathways; TET2 loss and EZH2 gain-of-function both impair HSC differentiation; co-mutation in MDS/MPN → compound epigenetic dysfunction and accelerated AML transformation.

[^delhommeau-2009-tet2-myeloid]: Delhommeau F, Dupont S, Della Valle V, et al. Mutation in TET2 in myeloid cancers. *N Engl J Med.* 2009;360(22):2289-2301. [doi:10.1056/NEJMoa0810069](https://doi.org/10.1056/NEJMoa0810069) · [PubMed 19474426](https://pubmed.ncbi.nlm.nih.gov/19474426/)
[^palomero-2014-ptcl-epigenetics]: Palomero T, Couronné L, Khiabanian H, et al. Recurrent mutations in epigenetic regulators, RHOA and FYN kinase in peripheral T cell lymphomas. *Nat Genet.* 2014;46(2):166-170. [doi:10.1038/ng.2872](https://doi.org/10.1038/ng.2872) · [PubMed 24413734](https://pubmed.ncbi.nlm.nih.gov/24413734/)
