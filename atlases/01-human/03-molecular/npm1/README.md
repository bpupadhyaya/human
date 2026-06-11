---
schema: human-scale-entry/v1
id: npm1
name: NPM1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "NPM1 (nucleophosmin) exon 12 insertions create cytoplasmic NPM1c in ~30% AML; NPM1c sequesters ARF → reduced p53 activity; NPM1c AML is a WHO-defined entity with favorable prognosis if FLT3-ITD negative; NPM1 mRNA is a sensitive MRD marker by RT-qPCR."
aliases: ["NPM1", "nucleophosmin", "NPM1c", "NPM1 AML", "NPM1 mutation", "NPM1c cytoplasmic", "B23 nucleophosmin", "NPM1-ALK"]
sources:
  - id: falini-2005-npm1c-aml
    type: peer-reviewed
    cite: "Falini B, Mecucci C, Tiacci E, et al. Cytoplasmic nucleophosmin in acute myelogenous leukemia with a normal karyotype. N Engl J Med. 2005;352(3):254-266."
    doi: "10.1056/NEJMoa041974"
    pmid: "15659725"
    url: "https://doi.org/10.1056/NEJMoa041974"
  - id: ivey-2016-npm1-mrd
    type: peer-reviewed
    cite: "Ivey A, Hills RK, Simpson MA, et al. Assessment of minimal residual disease in standard-risk AML. N Engl J Med. 2016;374(5):422-433."
    doi: "10.1056/NEJMoa1507471"
    pmid: "26789727"
    url: "https://doi.org/10.1056/NEJMoa1507471"
cross_links:
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "FLT3-ITD co-occurs with NPM1c in ~30-40% of NPM1c AML; FLT3-ITD negates the favorable NPM1c prognosis → intermediate-risk; gilteritinib+chemotherapy is standard for FLT3-mutant NPM1c AML; NPM1 MRD complements FLT3-ITD allele burden monitoring."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "NPM1c sequesters ARF (p14ARF) in cytoplasm → prevents ARF from inhibiting MDM2 → attenuated p53 tumor suppression; NPM1 wild-type co-activates p53 via ARF in the nucleolus; MDM2 inhibitors (idasanutlin) restore p53 in NPM1c AML."
  - target: 01-human/03-molecular/alk
    relation: connects-to
    note: "NPM1-ALK t(2;5)(p23;q35) fusion in ALK+ ALCL: NPM1 N-terminal oligomerization domain drives ALK homodimerization → constitutive ALK kinase; NPM1-ALK is distinct from NPM1c AML mutation; ALK inhibitors (crizotinib, alectinib) active in NPM1-ALK ALCL."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "TET2 mutations co-occur with NPM1c AML in ~20%; DNMT3A+TET2+NPM1c co-mutation is a recognized AML cluster; TET2 impairs 5mC oxidation → hypermethylation; azacitidine+venetoclax active in TET2+NPM1c AML; NPM1 MRD tracks response to azacitidine."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A is the most frequent NPM1c co-mutation in AML (~40%); DNMT3A+NPM1c = the pre-AML dyad (clonal hematopoiesis → AML; DNMT3A persists at remission as residual CH); DNMT3A+NPM1c+FLT3-ITD is the classical triple-hit NPM1c AML; DNMT3A R882H dominates in NPM1c co-mutant AML."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH1 R132H co-occurs with NPM1c in ~15% AML; IDH1 produces 2-HG → TET2 inhibition → hypermethylation synergizing with NPM1c HOX activation; ivosidenib+venetoclax+azacitidine in IDH1+NPM1c AML → very high CR rates; IDH inhibitors may be redundant to Ven+Aza alone."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "NPM1c AML is among the most venetoclax-sensitive genotypes: HOX program → MCL-1/BCL-2 dependence; venetoclax+azacitidine: CR+CRi 60-70% in NPM1c (best genotype); NPM1 MRD by RT-qPCR tracks depth of BCL-2 inhibition response; NPM1c without FLT3-ITD is the top-responding genotype."
---

# NPM1

## Overview

**NPM1 (Nucleophosmin 1)**, also known as B23 or numatrin, is a ubiquitous nucleolar phosphoprotein that functions as a histone chaperone, ribosome biogenesis cofactor, centrosome regulator, and ARF tumor suppressor anchor. NPM1 was established as the most frequently mutated gene in acute myeloid leukemia (AML) when **Falini et al. (2005)** discovered that exon 12 insertions causing cytoplasmic NPM1 mislocalization (NPM1c) are present in ~30% of all AML and ~50% of normal-karyotype AML [^falini-2005-npm1c-aml]. NPM1c mutations are now WHO-classified as a distinct AML entity ("AML with NPM1 mutation") with generally favorable prognosis in FLT3-ITD-negative cases. A distinctive molecular feature of NPM1c AML is the **HOXA/HOXB gene cluster overexpression** — NPM1c deregulates HOX gene loci, establishing a homeodomain TF program characteristic of progenitor/stem cell states. NPM1 also participates in oncogenesis through **NPM1-ALK fusion** in ALK-positive anaplastic large cell lymphoma (ALCL), where the NPM1 oligomerization domain drives constitutive ALK kinase dimerization. Wild-type NPM1 is a tumor suppressor in multiple contexts: it stabilizes ARF in the nucleolus → ARF inhibits MDM2 → p53 activation; NPM1c removes ARF from this nucleolar tether, attenuating p53 function without TP53 mutation [^ivey-2016-npm1-mrd].

**NPM1 in disease:**
- **NPM1c AML (~30% AML):** Exon 12 frameshift insertions (Type A — TCTG insert ~80%, Type B, Type D); cytoplasmic localization; HOX gene overexpression; favorable prognosis (FLT3-ITD negative: 4-year OS ~60-70%; FLT3-ITD positive: intermediate prognosis)
- **AML MRD:** NPM1 mRNA detectable by allele-specific RT-qPCR in blood/BM; highly sensitive (1:10⁴); MRD negativity after induction → superior RFS; rising NPM1 MRD during follow-up → molecular relapse preceding clinical relapse by weeks-months
- **ALK+ ALCL:** NPM1-ALK t(2;5)(p23;q35); NPM1 coiled-coil domain → ALK homodimerization → constitutive tyrosine kinase
- **NPM1 overexpression (not mutated):** In many solid tumors and high-grade lymphomas (Burkitt, DLBCL) → promotes ribosome biogenesis in rapidly proliferating cells; not actionable

## Structure

### NPM1 protein architecture

NPM1 is a 294-amino-acid protein (~37 kDa, apparent 40 kDa on SDS-PAGE due to phosphorylation) organized as a **pentameric ring** in the nucleolus:

**N-terminal oligomerization domain (1-70):**
Forms a barrel-like β-sheet fold; five subunits assemble into a ring pentamer (and can also form decamers of two pentamers); this domain is retained in NPM1-ALK fusion → drives ALK homodimerization (constitutive activation); conserved among NPM family members (NPM1/2/3); provides the structural scaffold for nucleolar localization.

**Central disordered/acidic region (71-186):**
Intrinsically disordered; contains multiple acidic residues (Asp, Glu) → negatively charged → histone binding (H2A/H2B and H3/H4 tetramers); contains two nuclear export signal (NES) regions: NES1 (~94-102) and NES2 (~148-156); NPM1 shuttles between nucleus and cytoplasm via CRM1-mediated export; phosphorylation at Ser125 by CDK2 at G2/M → NPM1 dimerization on centrosomal material → centrosome duplication licensing; NPM1 deficiency → centrosome amplification.

**C-terminal nucleic acid-binding domain (187-294):**
Winged-helix-like domain; binds rRNA (28S rRNA specifically) → required for ribosome processing and export; contains **nucleolar localization signal (NoLS):** Trp288, Trp290 — two conserved tryptophan residues critical for G-quadruplex rRNA binding and nucleolar retention; NPM1c mutations specifically disrupt this C-terminal domain:

**NPM1c mutation mechanism:**
All NPM1c AML mutations share: (1) exon 12 frameshift insertion → new amino acid sequence → (2) creation of a novel nuclear export signal (NES) in the C-terminus (leucine-rich sequence) → (3) **masking/disruption of Trp288/Trp290 NoLS** → loss of nucleolar retention → (4) CRM1-dependent cytoplasmic translocation; NPM1c protein accumulates in cytoplasm (diagnostic by IHC: cytoplasmic NPM1 staining in AML blasts); NPM1c also carries the wild-type N-terminal domain → can co-sequester wild-type NPM1 into cytoplasm (dominant-negative effect on one pool of NPM1-WT).

### NPM1-ARF-MDM2-p53 axis

**Normal nucleolar NPM1:**
NPM1 directly binds ARF (p14ARF, encoded by CDKN2A alternate reading frame) in the nucleolus → nucleolar retention of ARF → ARF cannot exit to bind MDM2 in the nucleoplasm; this is a complex regulatory balance: low NPM1 → ARF released to nucleoplasm → ARF-MDM2 binding → MDM2 sequestration → p53 stabilization → apoptosis/arrest.

**NPM1c and ARF:**
NPM1c (cytoplasmic) co-sequesters ARF in cytoplasm (ARF has the ability to follow NPM1c to cytoplasm) → ARF is unavailable to inhibit MDM2 → MDM2 is free to ubiquitinate p53 → p53 degradation → attenuated p53 signaling in NPM1c AML; importantly, TP53 mutations are rare in NPM1c AML precisely because NPM1c suppresses p53 without genetic TP53 mutation → functional "p53 silencing" without TP53 mutation.

## Function

### NPM1 in ribosome biogenesis

**Nucleolar function:**
NPM1 processes precursor rRNA: 47S pre-rRNA → (cleavage) → 28S, 18S, 5.8S rRNA; NPM1 interacts with B23-associated domain of pre-rRNPs → escort pre-ribosomal particles from nucleolus to cytoplasm for final assembly; in rapidly dividing cells (K-67 ~100%), NPM1 protein levels are markedly elevated → required for the extraordinary ribosome production rate; NPM1 also interacts with nucleolar RNA Pol I complex (RNAP I) → activates 47S rDNA transcription.

### NPM1 HOX gene regulation in AML

**HOX gene cluster activation:**
Normal adult hematopoiesis: HOXA/HOXB genes are progressively silenced during differentiation (HSC → progenitor → mature blood cell); NPM1c AML has extreme HOXA/HOXB reactivation (HOXA5, HOXA9, HOXA10, HOXB2, HOXB3 at high expression); NPM1c disrupts PRC2 (EZH2/H3K27me3) at HOX loci → derepression; MEIS1 (HOX co-factor) also upregulated; HOXA9+MEIS1 → arrested myeloid differentiation → AML blast maintenance; HOX inhibitors (PROTO-ONCEPT RVX-000222 analogs) being explored.

### NPM1 as centrosome regulator

NPM1 localizes to centrosomes at G2/M (phosphorylated by CDK2 on Ser125); NPM1 binding to unduplicated centrosome prevents premature reduplication; NPM1 heterozygous knockout mice → centrosome amplification → multipolar mitoses → genomic instability; NPM1c (cytoplasmic) may interfere with centrosome licensing, contributing to AML genomic instability.

## Mechanism

### NPM1c AML — clinical implications

**Prognosis:**
- NPM1c + FLT3-ITD negative: favorable risk by ELN 2022; 4-year OS ~70%; consolidation: HiDAC × 3-4 cycles; allo-SCT in CR1 NOT routinely recommended; NPM1 MRD guides decision
- NPM1c + FLT3-ITD high allele burden (≥0.5): intermediate-to-adverse; consider allo-SCT in CR1; gilteritinib + chemotherapy induction
- NPM1c + FLT3-ITD low allele burden (<0.5): intermediate; allo-SCT decision based on MRD and transplant-eligible status
- NPM1c + IDH1/2 co-mutation: venetoclax+azacitidine highly active (IDH inhibitor may not be needed if IDH co-mutation in NPM1c AML responds to Ven+Aza)

**NPM1 MRD by RT-qPCR [^ivey-2016-npm1-mrd]:**
NCRI/MRC AML17 trial: NPM1 MRD positivity (>200 copies/10⁵ ABL copies) in peripheral blood after consolidation Cycle 2 → 5-year RFS 10% vs 80% in MRD-negative (p<0.001); NPM1 MRD is ELN-recommended for CR confirmation and post-consolidation monitoring; rising NPM1 MRD in remission → molecular relapse (pre-emptive allo-SCT or enrollment in salvage trials before overt relapse); blood MRD is as sensitive as BM MRD for NPM1 (leaks into peripheral blood from marrow).

**Treatment of NPM1c AML:**
- Standard induction: "7+3" (cytarabine 100-200 mg/m² × 7 days + daunorubicin 60-90 mg/m² × 3 days) → CR ~75-80% in NPM1c
- CPX-351 (liposomal daunorubicin+cytarabine): superior to 7+3 in secondary AML (prior MDS/MPN); NPM1c less often secondary → 7+3 is preferred
- Venetoclax+azacitidine: highly active in NPM1c AML in older/unfit patients; CR+CRi ~60-70% in NPM1c with Ven+Aza; NPM1c among best responders (alongside IDH1/2 and DNMT3A co-mutations)
- Gilteritinib (FLT3 inhibitor): if FLT3-ITD+NPM1c → gilteritinib+chemotherapy induction (ADMIRAL protocol)

### NPM1-ALK in ALCL

**Fusion structure:**
NPM1 exons 1-4 (encoding the oligomerization pentameric domain) fused in-frame to ALK exon 2 onward (encoding the complete kinase domain); NPM1 N-terminal oligomerization → NPM1-ALK dimerizes → ALK kinase domain transphosphorylation → constitutive ALK kinase activity; NPM1-ALK activates STAT3, PI3K-AKT, MAPK → CD30+ ALCL with characteristic cytoplasmic+nuclear ALK staining by IHC (due to NPM1 shuttling → takes ALK into nucleus); ALK inhibitors (crizotinib, alectinib, lorlatinib) are active; ECHELON-2: brentuximab+CHP (anti-CD30 ADC + chemotherapy) for CD30+ PTCL including NPM1-ALK+ ALCL.

## Connections

- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — FLT3-ITD co-occurs with NPM1c in ~30-40% of NPM1c AML; FLT3-ITD negates the favorable NPM1c prognosis → intermediate-risk; gilteritinib+chemotherapy is standard for FLT3-mutant NPM1c AML; NPM1 MRD complements FLT3-ITD allele burden monitoring.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — NPM1c sequesters ARF (p14ARF) in cytoplasm → prevents ARF from inhibiting MDM2 → attenuated p53 tumor suppression; NPM1 wild-type co-activates p53 via ARF in the nucleolus; MDM2 inhibitors (idasanutlin) restore p53 in NPM1c AML.
- `connects-to` → **[ALK](../../03-molecular/alk/README.md)** — NPM1-ALK t(2;5)(p23;q35) fusion in ALK+ ALCL: NPM1 N-terminal oligomerization domain drives ALK homodimerization → constitutive ALK kinase; NPM1-ALK is distinct from NPM1c AML mutation; ALK inhibitors (crizotinib, alectinib) active in NPM1-ALK ALCL.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — TET2 mutations co-occur with NPM1c AML in ~20%; DNMT3A+TET2+NPM1c co-mutation is a recognized AML cluster; TET2 impairs 5mC oxidation → hypermethylation; azacitidine+venetoclax active in TET2+NPM1c AML; NPM1 MRD tracks response to azacitidine.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A is the most frequent NPM1c co-mutation in AML (~40%); DNMT3A+NPM1c = the pre-AML dyad (clonal hematopoiesis → AML; DNMT3A persists at remission as residual CH); DNMT3A+NPM1c+FLT3-ITD is the classical triple-hit NPM1c AML; DNMT3A R882H dominates in NPM1c co-mutant AML.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH1 R132H co-occurs with NPM1c in ~15% AML; IDH1 produces 2-HG → TET2 inhibition → hypermethylation synergizing with NPM1c HOX activation; ivosidenib+venetoclax+azacitidine in IDH1+NPM1c AML → very high CR rates; IDH inhibitors may be redundant to Ven+Aza alone.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — NPM1c AML is among the most venetoclax-sensitive genotypes: HOX program → MCL-1/BCL-2 dependence; venetoclax+azacitidine: CR+CRi 60-70% in NPM1c (best genotype); NPM1 MRD by RT-qPCR tracks depth of BCL-2 inhibition response; NPM1c without FLT3-ITD is the top-responding genotype.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^falini-2005-npm1c-aml]: Falini B, Mecucci C, Tiacci E, et al. Cytoplasmic nucleophosmin in acute myelogenous leukemia with a normal karyotype. *N Engl J Med.* 2005;352(3):254-266. [doi:10.1056/NEJMoa041974](https://doi.org/10.1056/NEJMoa041974) · [PubMed 15659725](https://pubmed.ncbi.nlm.nih.gov/15659725/)
[^ivey-2016-npm1-mrd]: Ivey A, Hills RK, Simpson MA, et al. Assessment of minimal residual disease in standard-risk AML. *N Engl J Med.* 2016;374(5):422-433. [doi:10.1056/NEJMoa1507471](https://doi.org/10.1056/NEJMoa1507471) · [PubMed 26789727](https://pubmed.ncbi.nlm.nih.gov/26789727/)
