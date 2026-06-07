---
schema: human-scale-entry/v1
id: neurofibromatosis-type-1
name: Neurofibromatosis Type 1
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Neurofibromatosis type 1 (NF1) is caused by germline NF1 mutations; café-au-lait macules, neurofibromas, Lisch nodules, optic pathway gliomas; ~10% lifetime MPNST risk; 1/3000; selumetinib FDA-approved for NF1-associated plexiform neurofibromas in children (2020)."
aliases: ["NF1", "neurofibromatosis type 1", "von Recklinghausen disease", "NF1 syndrome", "NF1 germline", "NF1 plexiform neurofibroma", "NF1 MPNST", "neurofibromatosis cancer risk", "NF1 selumetinib"]
sources:
  - id: gutmann-2017-nf1-primer
    type: peer-reviewed
    cite: "Gutmann DH, Ferner RE, Listernick RH, et al. Neurofibromatosis type 1. Nat Rev Dis Primers. 2017;3:17004."
    doi: "10.1038/nrdp.2017.4"
    pmid: "28230061"
    url: "https://doi.org/10.1038/nrdp.2017.4"
  - id: dombi-2016-selumetinib
    type: peer-reviewed
    cite: "Dombi E, Baldwin A, Marcus LJ, et al. Activity of Selumetinib in Neurofibromatosis Type 1-Related Plexiform Neurofibromas. N Engl J Med. 2016;375(26):2550-2560."
    doi: "10.1056/NEJMoa1605943"
    pmid: "28029918"
    url: "https://doi.org/10.1056/NEJMoa1605943"
cross_links:
  - target: 01-human/03-molecular/spred1
    relation: connects-to
    note: "Germline SPRED1 causes Legius syndrome (café-au-lait macules + axillary freckling) without neurofibromas or cancer predisposition; clinically mimics mild NF1; molecular testing distinguishes both; SPRED1 and NF1 both restrain RAS-MAPK at the plasma membrane."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "Neurofibromin (NF1) is a RAS-GAP; NF1 LOF → sustained RAS-GTP → MAPK/PI3K/mTOR activation → NF1 syndrome manifestations including neurofibromas, MPNST, optic gliomas; selumetinib (MEK1/2 inhibitor) FDA-approved for NF1-associated plexiform neurofibromas in children."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "NF1 LOF activates the same RAS-MAPK pathway as oncogenic KRAS mutations; both result in sustained RAS-GTP → MEK/ERK activation → proliferation; MEK inhibitors (selumetinib, trametinib) are active in NF1-deficient and KRAS-mutant tumors via the shared MAPK pathway."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "MPNST arises in ~10% of NF1 patients from plexiform neurofibromas; NF1-MPNST is more aggressive than sporadic MPNST; NF1 LOF → RAS-MAPK/CDK4 → malignant transformation; selumetinib shrinks plexiform precursors; surgical resection primary for overt MPNST."
---

# Neurofibromatosis Type 1

## Overview

**Neurofibromatosis type 1 (NF1)**, also called **von Recklinghausen disease**, is an autosomal dominant hereditary tumor predisposition and RASopathy caused by germline pathogenic variants in the **NF1** tumor suppressor gene (chromosome 17q11.2, encodes neurofibromin, a RAS-GAP). With a prevalence of approximately **1 in 3,000** (one of the most common single-gene disorders), NF1 is the **most frequently diagnosed single-gene cancer predisposition syndrome** in humans. NF1 syndrome features a broad spectrum of manifestations including café-au-lait macules, cutaneous and plexiform neurofibromas, Lisch nodules, optic pathway gliomas, and cardiovascular abnormalities, as well as a significantly elevated lifetime risk of malignant tumors including **malignant peripheral nerve sheath tumor (MPNST)** (~10%), glioma, leukemia, and gastrointestinal stromal tumor (GIST) [^gutmann-2017-nf1-primer] [^dombi-2016-selumetinib].

**NF1 syndrome prevalence among hereditary cancer syndromes:**

NF1 is unique in being among both the most common and most mutated single-gene cancer syndromes. Half of all NF1 cases arise from de novo mutations (no family history), reflecting the NF1 gene's large target size (350 kb, 60 exons — one of the largest human genes) and correspondingly high spontaneous mutation rate.

**NIH Diagnostic Criteria for NF1 (1988, still in clinical use; 2021 revised criteria available):**
Two or more of:
1. ≥6 café-au-lait macules (≥5 mm pre-pubertal; ≥15 mm post-pubertal)
2. ≥2 cutaneous or subcutaneous neurofibromas, or ≥1 plexiform neurofibroma
3. Freckling in axilla or groin (Crowe's sign)
4. Optic pathway glioma
5. ≥2 Lisch nodules (iris hamartomas)
6. Distinctive bony lesion: sphenoid wing dysplasia, pseudarthrosis of long bone
7. First-degree relative with NF1 by these criteria

**2021 Updated criteria add:** heterotopic/ectopic spleen, moyamoya syndrome, NF1-associated GIST

## Structure

### Genetic basis

- **NF1 gene**: 17q11.2; 350 kb; 60 exons; encodes 2818 aa neurofibromin
- **Inheritance**: autosomal dominant; 50% offspring risk
- **De novo rate**: ~50% of NF1 cases; among the highest de novo rates of any monogenic condition (due to large gene size → high target for new mutations)
- **Mutation spectrum**: diverse; >3,500 unique pathogenic variants; frameshift + nonsense + splice (~60%), missense (~20%), large deletions (~10%, often severe phenotype), deep intronic variants
- **Severe/atypical phenotype**: large genomic deletions (>1 Mb) encompassing NF1 and flanking genes → more neurofibromas, cognitive effects, dysmorphic features, vasculopathy
- **Genotype-phenotype**: generally poor; same mutation can produce highly variable phenotype even within families; exceptions: c.2970-2972delAAT (in-frame exon 17 deletion) = milder, CALM only; c.5543C>T (Arg1849Trp) = spinal neurofibromas; large deletions = severe
- **Somatic mosaicism**: ~5-10% of apparent NF1; detected by deep sequencing (VAF <30%)

### Two-hit model in NF1 tumors

NF1 follows a modified two-hit tumor suppressor model:
1. **Germline first hit**: one pathogenic NF1 allele inactivated in every cell
2. **Somatic second hit (LOH at 17q11.2)**: in Schwann cells (neurofibromas) and mast cells; LOH detected in >95% of individual neurofibroma Schwann cells
3. **Neurofibroma microenvironment**: NF1+/− mast cells and fibroblasts in the neurofibroma stroma produce KIT ligand (SCF) and other factors that promote NF1−/− Schwann cell proliferation; haploinsufficiency of flanking cells is required, not just the tumor-initiating Schwann cell

In glioma and MPNST: additional alterations required — MPNST requires CDKN2A/2B loss (cyclin-CRK4 pathway) and sometimes EGFR amplification or TP53 mutation beyond NF1 biallelic LOH.

## Function

### NF1 syndrome manifestations

**Skin (café-au-lait macules and neurofibromas):**
- Café-au-lait macules (CALM): uniform tan spots; arise in infancy; increase throughout childhood; benign; present in >99% of NF1 patients; also present in Legius syndrome, McCune-Albright, and normal population (<5 CALMs is normal)
- Axillary/inguinal freckling (Crowe's sign): pathognomonic in combination with CALMs; develops in ~65% of NF1 patients in early childhood
- Cutaneous neurofibromas: soft flesh-colored papules, may be hundreds to thousands; increase with age; benign but cosmetically significant; arise from skin Schwann cells; typically puberty-onset
- Subcutaneous neurofibromas: deeper, firmer, often painful; arise from deeper nerve sheaths
- **Plexiform neurofibromas (PNF)**: large diffuse tumors arising from major nerve plexuses; present in ~30-50% of NF1 patients; often disfiguring; can be life-threatening if near airway; the precursor lesion for MPNST (malignant transformation in ~10-15%)

**Eye (Lisch nodules and optic glioma):**
- Lisch nodules: iris melanocytic hamartomas; slit-lamp examination required; present in >90% of NF1 adults; benign; pathognomonic for NF1; absent in NF2, Legius, and most other syndromes
- Optic pathway glioma (OPG): usually low-grade pilocytic astrocytoma (WHO grade 1) involving optic nerves, chiasm, or tracts; ~15% of NF1 patients; mostly asymptomatic; symptomatic OPG (~6%): visual acuity loss, proptosis, precocious puberty (if hypothalamic involvement); treatment: carboplatin + vincristine (CV) first-line; MEK inhibitors (selumetinib/trametinib) increasingly used; rarely requires surgery

**Bone:**
- Sphenoid wing dysplasia: congenital absence/hypoplasia of the sphenoid bone; rare; can cause pulsatile exophthalmos
- Tibial pseudarthrosis (bowed tibia, fracture risk): congenital; rare; difficult to treat; associated with young age
- Short stature, scoliosis, reduced bone density: common

**Cardiovascular:**
- Congenital heart disease (pulmonary stenosis, ASD): ~2-3%
- **NF1-associated vasculopathy**: RAS-MAPK dysregulation in vascular smooth muscle → stenosis, aneurysm; renovascular hypertension, moyamoya syndrome; often in children
- Hypertension: ~20% of NF1 patients; renovascular or essential

**CNS (learning/cognition):**
- Learning disabilities: ~50-60% of NF1 patients (most common complication)
- Attention-deficit disorder (ADHD): ~50%
- Autism spectrum features: ~30%
- Lower IQ on average (~10-15 points below population mean); rarely severe intellectual disability
- T2 hyperintense foci (UBOs — unidentified bright objects) on brain MRI: common; significance unclear; may correlate with cognitive issues
- Epilepsy: ~5-7%

**Malignant complications:**
- **MPNST**: lifetime risk ~10-15%; arises from plexiform neurofibromas; if size >3 cm + rapid growth + pain + new neurological deficit → suspicious for MPNST; FDG-PET (SUV >3.5) distinguishes from benign PNF; poor prognosis (5-year OS ~40-50%)
- **Optic pathway glioma**: low-grade but may be visually threatening
- **Low-grade glioma (pilocytic)**: brain tumors common in NF1; usually low-grade; BRAF internal duplication (KIAA1549-BRAF fusion) drives NF1-associated LGG; MEK inhibitors (trametinib, dabrafenib) active in BRAF-fusion NF1 LGG
- **JMML (juvenile myelomonocytic leukemia)**: RAS-MAPK pathway in hematopoiesis; NF1 infants at elevated JMML risk; PTPN11, NRAS, KRAS, NF1 mutations all cause JMML
- **Pheochromocytoma/paraganglioma**: slightly elevated risk (~3-4%)
- **Breast cancer**: modest elevation (~10-15% lifetime vs ~13% population; age-dependent elevated risk at 40-50)
- **GIST**: ~3-5% of NF1 patients; distinct from KIT/PDGFRA-mutant sporadic GIST; NF1-GIST is KIT/PDGFRA wildtype; imatinib less effective; sunitinib or regorafenib second-line

## Pathology

### Surveillance and management

**Annual surveillance:**
- Annual clinical assessment: neurological exam, skin survey, ophthalmology (children — annual until age 6; then as needed), blood pressure
- **Brain MRI**: recommended for any new neurological symptom; periodic in children with known OPG
- **Whole-body MRI (WB-MRI)**: recommended for NF1 patients, especially to monitor known PNF and detect MPNST; frequency guided by clinical risk

**Selumetinib (Koselugo) for NF1-associated PNF:**
- MEK1/2 inhibitor; oral; pediatric use for symptomatic/progressive inoperable PNF
- SPRINT Phase 2 trial (Dombi 2016, NEJM): 20 of 24 patients had ≥20% tumor volume reduction; confirmed in Phase 2b expansion; FDA Breakthrough Therapy; FDA-approved April 2020 for pediatric NF1 with inoperable PNF (≥2 years)
- Adult NF1-PNF: trials ongoing (SPRINT extension, RENEW trial)
- MEK inhibitor toxicity: acneiform rash, GI toxicity, cardiac (LVEF monitoring), retinal vein occlusion; dose adjustments; teratogenic → contraception required

**MPNST management:**
- Surgical resection with wide margins: primary curative intent; R0 resection goal
- Adjuvant RT: used in R1/R2 resection or high-grade MPNST (same RT-second cancer concern as hereditary RB — less prominent in NF1 context but considered)
- Systemic chemotherapy: no FDA-approved agent; doxorubicin ± ifosfamide (standard soft tissue sarcoma regimen); limited responses
- CDK4/6 inhibitors + MEK inhibitors: clinical trials in MPNST (CDK4 pathway co-activated with NF1 LOF)

**Pregnancy in NF1:**
- Neurofibroma proliferation can increase during pregnancy (estrogen effect on neurofibroma Schwann cells)
- Preconception: 50% offspring risk; preimplantation genetic testing (PGT-M) available

## Connections

- `connects-to` → **[SPRED1](../../03-molecular/spred1/README.md)** — Germline SPRED1 causes Legius syndrome (café-au-lait macules + axillary freckling) without neurofibromas or cancer predisposition; clinically mimics mild NF1; molecular testing distinguishes both; SPRED1 and NF1 both restrain RAS-MAPK at the plasma membrane.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — Neurofibromin (NF1) is a RAS-GAP; NF1 LOF → sustained RAS-GTP → MAPK/PI3K/mTOR activation → NF1 syndrome manifestations including neurofibromas, MPNST, optic gliomas; selumetinib (MEK1/2 inhibitor) FDA-approved for NF1-associated plexiform neurofibromas in children.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — NF1 LOF activates the same RAS-MAPK pathway as oncogenic KRAS mutations; both result in sustained RAS-GTP → MEK/ERK activation → proliferation; MEK inhibitors (selumetinib, trametinib) are active in NF1-deficient and KRAS-mutant tumors via the shared MAPK pathway.
- `connects-to` → **[MPNST](../../07-system/mpnst/README.md)** — MPNST arises in ~10% of NF1 patients from plexiform neurofibromas; NF1-MPNST is more aggressive than sporadic MPNST; NF1 LOF → RAS-MAPK/CDK4 → malignant transformation; selumetinib shrinks plexiform precursors; surgical resection primary for overt MPNST.

[^gutmann-2017-nf1-primer]: Gutmann DH, Ferner RE, Listernick RH, et al. Neurofibromatosis type 1. *Nat Rev Dis Primers.* 2017;3:17004. [doi:10.1038/nrdp.2017.4](https://doi.org/10.1038/nrdp.2017.4) · [PubMed 28230061](https://pubmed.ncbi.nlm.nih.gov/28230061/)
[^dombi-2016-selumetinib]: Dombi E, Baldwin A, Marcus LJ, et al. Activity of Selumetinib in Neurofibromatosis Type 1-Related Plexiform Neurofibromas. *N Engl J Med.* 2016;375(26):2550-2560. [doi:10.1056/NEJMoa1605943](https://doi.org/10.1056/NEJMoa1605943) · [PubMed 28029918](https://pubmed.ncbi.nlm.nih.gov/28029918/)
