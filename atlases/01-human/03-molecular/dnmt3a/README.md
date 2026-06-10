---
schema: human-scale-entry/v1
id: dnmt3a
name: DNMT3A
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "DNMT3A encodes de novo DNA methyltransferase 3A; R882H/C dominant-negative hotspot mutations in ~20% of AML and ~40% of CHIP cause focal hypomethylation → HSC clonal expansion; DNMT3A+NPM1+FLT3-ITD is the classic intermediate-risk AML triplet; no direct targeted therapy."
aliases: ["DNMT3A", "DNA methyltransferase 3A", "DNMT3A R882H", "DNMT3A mutation", "DNMT3A AML", "DNMT3A CHIP", "epigenetic AML", "clonal hematopoiesis DNMT3A"]
sources:
  - id: ley-2010-dnmt3a-aml
    type: peer-reviewed
    cite: "Ley TJ, Ding L, Walter MJ, et al. DNMT3A mutations in acute myeloid leukemia. N Engl J Med. 2010;363(25):2424-2433."
    doi: "10.1056/NEJMoa1005143"
    pmid: "21067377"
    url: "https://doi.org/10.1056/NEJMoa1005143"
  - id: jaiswal-2014-chip
    type: peer-reviewed
    cite: "Jaiswal S, Fontanillas P, Flannick J, et al. Age-related clonal hematopoiesis associated with adverse outcomes. N Engl J Med. 2014;371(26):2488-2498."
    doi: "10.1056/NEJMoa1408617"
    pmid: "25426837"
    url: "https://doi.org/10.1056/NEJMoa1408617"
cross_links:
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH2 R140Q/R172K mutations co-occur with DNMT3A R882 in AML; both converge on DNA hypermethylation via 2-HG (IDH2) and reduced de novo methylation fidelity (DNMT3A); DNMT3A+IDH2+NPM1 is a common co-mutation cluster in intermediate-risk AML."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "DNMT3A and EZH2 both regulate epigenetic gene silencing; DNMT3A methylates CpG DNA while EZH2 (PRC2) writes H3K27me3; in AML and MDS, DNMT3A and EZH2 loss-of-function mutations co-occur, amplifying epigenetic deregulation and differentiation block."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "DNMT3A mutations co-exist with TP53 in ~10% of AML; TP53 loss accelerates clonal dominance of DNMT3A-mutant pre-leukemic HSCs; DNMT3A R882H AML with TP53 co-mutation has poor prognosis and inferior response to HMA therapy."
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "DNMT3A+NPM1+FLT3-ITD is the classic intermediate-risk AML triplet (~10% of AML); FLT3-ITD drives proliferation while DNMT3A R882H blocks differentiation; midostaurin+daunorubicin/cytarabine is standard induction; FLT3 inhibitor addition improves OS."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "DNMT3A R882H/C dominant-negative mutations in ~20% of AML block de novo methylation → focal hypomethylation → HSC stemness gene derepression; classic AML triplet DNMT3A+NPM1+FLT3-ITD (~10% of all AML); standard induction 7+3+midostaurin; allo-SCT for intermediate/adverse risk."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "DNMT3A mutations in ~15-20% of MDS; early epigenetic driver co-mutated with TET2, ASXL1, SF3B1; DTA mutations predict reduced response to HMA therapy in MDS; azacitidine/decitabine are standard MDS treatment; DNMT3A+RUNX1 co-mutation confers higher AML transformation risk."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "DNMT3A writes 5mC de novo methylation; TET2 oxidizes 5mC → 5hmC for demethylation; both are top CHIP genes and common AML/MDS mutations; DNMT3A+TET2 co-mutations cause convergent methylation dysregulation in MDS/CMML; TET2 loss also enhances DNMT3A-mutant HSC clonal advantage."
---

# DNMT3A

## Overview

**DNMT3A (DNA Methyltransferase 3 Alpha)** is one of the two de novo DNA methyltransferases (alongside DNMT3B) responsible for establishing CpG methylation patterns on unmethylated DNA during embryogenesis, development, and hematopoietic stem cell (HSC) differentiation. DNMT3A and DNMT3B work with the accessory subunit DNMT3L to methylate cytosine residues at CpG dinucleotides → 5-methylcytosine (5mC) → stable gene silencing at differentiation-associated loci → HSC maintenance in a poised, multipotent state. In cancer and aging, **DNMT3A loss-of-function mutations** — particularly the dominant-negative hotspot **R882H/C** — disrupt normal methylation programming → focal hypomethylation at HSC stemness and polycomb-target loci → clonal HSC expansion without differentiation → pre-leukemic CHIP and eventually AML. DNMT3A is the single most frequently mutated gene in **clonal hematopoiesis of indeterminate potential (CHIP)** (~40% of CHIP cases) and the most commonly mutated epigenetic regulator in **AML** (~20%) [^ley-2010-dnmt3a-aml] [^jaiswal-2014-chip].

**DNMT3A in cancer and clonal hematopoiesis:**
- **AML:** DNMT3A mutations in ~20-22% of AML; predominantly R882H (~40%) and R882C (~20%), both dominant-negative; the classic triplet DNMT3A + NPM1 + FLT3-ITD (~10% of all AML) is classified intermediate-risk (ELN 2022: NPM1-positive without adverse features); co-mutations also with IDH1/IDH2, RUNX1, ASXL1; therapy: 7+3 + midostaurin (FLT3-ITD co-mutation); gilteritinib for FLT3-mutant R/R; allo-SCT consolidation in intermediate/adverse risk
- **MDS:** DNMT3A mutations in ~15-20% of MDS; "early" epigenetic hit; often co-mutated with TET2, ASXL1, SF3B1, SRSF2; DNMT3A+TET2 co-mutations represent convergent DNA methylation dysregulation
- **CHIP (clonal hematopoiesis):** Most common CHIP driver gene (~40%); CHIP = ≥2% VAF mutation in blood without cytopenias/dysplasia; DNMT3A-CHIP associated with ~2-fold increased risk of subsequent hematologic malignancy; also associated with cardiovascular disease (IL-6 pathway activation in CHIP macrophages); atherosclerosis risk
- **T-cell lymphomas:** DNMT3A mutations in PTCL-NOS (~20%), AITL (~30%), other PTCL; arise in pre-malignant TFH/T-progenitor cells (often co-mutated with TET2, IDH2 R172K in AITL)
- **Normal aging:** DNMT3A-CHIP variants detectable in >10% of individuals >65 years; frequency increases exponentially with age; most CHIP carriers never develop AML

## Structure

### DNMT3A protein architecture

DNMT3A is a 912-amino-acid protein organized into functional domains:

**PWWP domain (1-215, Pro-Trp-Trp-Pro):**
- Reads H3K36me2/me3 marks at actively transcribed gene bodies → guides DNMT3A to euchromatin
- Mutation in PWWP → loss of H3K36me2/me3 reading → aberrant targeting; DNMT3A-PWWP mutations (p.W330R) cause overgrowth syndrome (growth hormone excess) distinct from AML hotspot

**ADD domain (ATRX-DNMT3-DNMT3L domain, 470-615):**
- Reads unmodified H3K4 at gene regulatory regions; H3K4me2/me3 INHIBITS ADD-chromatin binding → prevents DNMT3A from methylating actively transcribed loci
- PRC2/polycomb interaction: Unmethylated H3K4 + H3K27me3 (EZH2 mark) → ADD binding → de novo methylation of silenced developmentally regulated genes

**MTase catalytic domain (615-912):**
- Contains the conserved SAM-dependent methyltransferase motifs (I, IV, VI, VIII, IX, X)
- Active site: Cys651 (nucleophilic cysteine); Arg882 (critical for substrate recognition in the active site loop)
- **R882H/C mutation:** Arg882 → His/Cys → disrupts active-site loop conformation → reduces catalytic efficiency ~80% for the R882-mutant monomer AND dominant-negatively inhibits the wild-type DNMT3A/DNMT3L heterotetramer (R882H binds WT DNMT3A but prevents its activation) → ~80% global loss of de novo methylation activity in heterozygous cells
- DNMT3L binding: DNMT3L (catalytically inactive homolog) stimulates DNMT3A MTase by allosteric activation → R882H disrupts DNMT3L interaction → further methylation impairment

**Heterotetramer assembly:**
Normal DNMT3A forms a (DNMT3A)₂:(DNMT3L)₂ heterotetramer → processively methylates CpG DNA; R882H-containing heterotetramer is dominant-negative; DNMT3B also forms heterotetramer with DNMT3L but has distinct genomic targeting (satellite DNA, imprinted regions); DNMT3B mutations cause ICF syndrome (immunodeficiency with centromeric instability).

### Dominant-negative mechanism of R882H

Wild-type DNMT3A R882 contacts the +1 CpG base in the substrate DNA → required for optimal catalytic geometry. R882H → imidazole (His) replaces guanidinium (Arg) → altered electrostatic contact → methylation efficiency reduced; additionally, R882H-containing (DNMT3A)₂:(DNMT3L)₂ heterotetramers have ~50% reduced activity relative to WT homotetramer — this dominant-negative effect means heterozygous R882H cells (~same as germline AML) have only ~20% of normal DNMT3A activity. Loss of methylation is not global: specifically, **HOXA cluster genes, stemness loci (GATA2, CEBPA enhancers), and polycomb target genes** are most affected → HSC gene expression program dominates → myeloid differentiation block.

### DNMT3A and CHIP biology

**CHIP definition and evolution:**
CHIP (clonal hematopoiesis of indeterminate potential): ≥2% variant allele frequency (VAF) of a leukemia-driver mutation in peripheral blood DNA, without cytopenias meeting MDS criteria. DNMT3A-CHIP → slow clonal expansion (doubling time ~6-10 years) driven by HSC competitive fitness advantage from impaired differentiation. CHIP → ~0.5-1% per year risk of progression to MDS or AML; DNMT3A-CHIP + co-occurring NRAS or FLT3 mutation → accelerated progression. Cardiovascular risk: DNMT3A-mutant macrophages → NF-κB activation → IL-6/IL-1β secretion → atherosclerotic plaque formation (mouse model: bone marrow transplant of DNMT3A-CHIP → accelerated atherosclerosis).

## Function

### Normal DNMT3A roles in hematopoiesis

**HSC epigenetic programming:**
DNMT3A establishes methylation patterns during HSC differentiation → silences HSC-specific genes (HOXA genes, MYC targets, multipotency factors) as HSCs commit to myeloid or lymphoid progenitors. DNMT3A knockout mice: HSCs accumulate with age (competitive repopulation advantage) but fail to differentiate → expansion of phenotypic HSC pool → serially transplantable, self-renewing HSC pool resembling AML pre-leukemic state. Loss of DNMT3A alone (in mice) is insufficient for AML — requires co-mutation (NPM1, FLT3, NRAS, IDH2) to produce overt leukemia.

**DNMT3A in myeloid vs. lymphoid lineage:**
DNMT3A is required for myeloid differentiation (CEBPA and PU.1 promoter methylation of HSC-specific genes), but also for lymphoid lineage: DNMT3A deficiency in T-cells → loss of regulatory T-cell (Treg) stability (FOXP3 locus hypomethylation) → autoimmune phenotype in mice; DNMT3A-mutant T-cell precursors → PTCL and AITL in humans.

### DNMT3A-mutant AML biology

**Differentiation block mechanism:**
R882H → hypomethylation of HSC-specific loci (HOXA9, HOXA10, MEIS1 targets) → sustained expression of multipotency transcription factors → myeloid progenitors maintain stem-cell program → fail to complete granulocytic or monocytic differentiation → blast accumulation. Azacitidine and decitabine (HMAs): Covalently trap DNMT1 (maintenance methyltransferase) → genome-wide passive demethylation → paradoxically re-expresses silenced genes (tumor suppressors in MDS/AML) → differentiation. HMAs do NOT specifically target DNMT3A-mutant AML; activity in R882H AML is similar to other AML subtypes.

**DNMT3A + IDH1/IDH2 co-mutations:**
IDH1/IDH2 mutations → 2-HG → competitively inhibits TET2 (demethylase) → DNA hypermethylation; DNMT3A R882H simultaneously causes focal hypomethylation at different loci; the net effect is a complex mixed methylation phenotype with both hyper- and hypo-methylated regions depending on locus. These mutations often co-occur (~15% of DNMT3A-mutant AML also have IDH1 or IDH2) → compound epigenetic dysregulation.

## Mechanism

### DNMT3A-mutant AML treatment

**Induction chemotherapy:**
Standard 7+3 (cytarabine + daunorubicin or idarubicin) induction; CR rate ~70-80% for DNMT3A-mutant AML overall; DNMT3A+NPM1+FLT3-ITD triplet: add midostaurin (RATIFY trial: OS 74.7 vs 25.6 months median in 4-year landmark) or quizartinib (FLT3-ITD specific). Consolidation: allo-SCT if intermediate or adverse risk; high-dose cytarabine HIDAC for favorable risk.

**CPX-351 (liposomal daunorubicin/cytarabine):**
FDA approved for therapy-related AML or AML-MRC; DNMT3A-mutant AML with prior MDS/CHIP history may be classified as AML-MRC → CPX-351 preferred over 7+3.

**HMA + venetoclax:**
For older/unfit DNMT3A-mutant AML patients: azacitidine + venetoclax (VIALE-A: CR+CRi 66.4% vs 28.3%, OS 14.7 vs 9.6 months) → DNMT3A-mutant AML is among the highest-responding subgroups (CR+CRi ~75-80%) because DNMT3A mutations co-occur with NPM1 (which drives BCL-2 dependency).

**Resistance and clonal evolution:**
DNMT3A-mutant pre-leukemic HSC clone can persist after CR → "residual disease at the epigenetic level" → later relapse; DNMT3A R882H is often retained at relapse while secondary co-mutations evolve (FLT3, NRAS, IDH1/2 may change clonally) → relapse clone often differs from diagnosis clone; MRD for DNMT3A is therefore less reliable as a solo marker.

**No direct DNMT3A-targeted therapy:**
Unlike IDH1/2 (ivosidenib/enasidenib) or FLT3 (midostaurin/gilteritinib), there is no approved drug directly targeting DNMT3A R882H. Research approaches: menin inhibitor (menin-HOXA9 complex disruption — menin inhibitors revaciclib/DSP-5336 active in NPM1/KMT2A AML; DNMT3A-mutant NPM1+ AML is a high-priority subgroup); DNMT3A activator (restoring WT-like activity in R882H cells — preclinical).

## Connections

- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH2 R140Q/R172K mutations co-occur with DNMT3A R882 in AML; both converge on DNA hypermethylation via 2-HG (IDH2) and reduced de novo methylation fidelity (DNMT3A); DNMT3A+IDH2+NPM1 is a common co-mutation cluster in intermediate-risk AML.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — DNMT3A and EZH2 both regulate epigenetic gene silencing; DNMT3A methylates CpG DNA while EZH2 (PRC2) writes H3K27me3; in AML and MDS, DNMT3A and EZH2 loss-of-function mutations co-occur, amplifying epigenetic deregulation and differentiation block.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — DNMT3A mutations co-exist with TP53 in ~10% of AML; TP53 loss accelerates clonal dominance of DNMT3A-mutant pre-leukemic HSCs; DNMT3A R882H AML with TP53 co-mutation has poor prognosis and inferior response to HMA therapy.
- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — DNMT3A+NPM1+FLT3-ITD is the classic intermediate-risk AML triplet (~10% of AML); FLT3-ITD drives proliferation while DNMT3A R882H blocks differentiation; midostaurin+daunorubicin/cytarabine is standard induction; FLT3 inhibitor addition improves OS.
- `connects-to` → **[AML](../../07-system/aml/README.md)** — DNMT3A R882H/C dominant-negative mutations in ~20% of AML block de novo methylation → HSC stemness gene derepression; classic triplet DNMT3A+NPM1+FLT3-ITD (~10% of all AML); standard induction 7+3+midostaurin; allo-SCT consolidates intermediate/adverse risk disease.
- `connects-to` → **[MDS](../../07-system/mds/README.md)** — DNMT3A mutations in ~15-20% of MDS; early epigenetic driver co-mutated with TET2, ASXL1, SF3B1; DTA mutations predict reduced HMA response; azacitidine/decitabine are standard MDS treatment; DNMT3A+RUNX1 co-mutation confers higher AML transformation risk.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — DNMT3A writes 5mC de novo methylation; TET2 oxidizes 5mC → 5hmC for demethylation; both are top CHIP genes and common AML/MDS mutations; DNMT3A+TET2 co-mutations cause convergent methylation dysregulation in MDS/CMML; TET2 loss enhances DNMT3A-mutant HSC clonal advantage.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^ley-2010-dnmt3a-aml]: Ley TJ, Ding L, Walter MJ, et al. DNMT3A mutations in acute myeloid leukemia. *N Engl J Med.* 2010;363(25):2424-2433. [doi:10.1056/NEJMoa1005143](https://doi.org/10.1056/NEJMoa1005143) · [PubMed 21067377](https://pubmed.ncbi.nlm.nih.gov/21067377/)
[^jaiswal-2014-chip]: Jaiswal S, Fontanillas P, Flannick J, et al. Age-related clonal hematopoiesis associated with adverse outcomes. *N Engl J Med.* 2014;371(26):2488-2498. [doi:10.1056/NEJMoa1408617](https://doi.org/10.1056/NEJMoa1408617) · [PubMed 25426837](https://pubmed.ncbi.nlm.nih.gov/25426837/)
