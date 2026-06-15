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
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "NF1 neurofibromas — cutaneous, subcutaneous, and plexiform — grow from Schwann cells of peripheral nerves after a somatic second hit knocks out the remaining NF1 allele; plexiform neurofibromas are the precursor lesion that can transform into MPNST in ~10-15%."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Neurofibroma growth depends on its microenvironment: NF1-haploinsufficient mast cells and fibroblasts secrete stem-cell factor (SCF/KIT ligand) that drives proliferation of the NF1-null Schwann cells — a paracrine loop explored therapeutically with imatinib (anti-KIT)."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "GIST occurs in ~3-5% of NF1 patients but is biologically distinct from sporadic GIST: NF1-associated GISTs are KIT/PDGFRA wild-type (driven instead by NF1 loss → RAS-MAPK), so they respond poorly to imatinib, with sunitinib or regorafenib used in later lines."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "NF1 and NF2 share a name and dominant inheritance but are unrelated diseases: NF1 (neurofibromin, a RAS-GAP) drives café-au-lait spots and neurofibromas, while NF2 (merlin, a Hippo regulator) drives bilateral vestibular schwannomas and meningiomas — different genes and pathways."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin shows NF1's earliest and most reliable signs: six or more café-au-lait macules and axillary/inguinal freckling appear in childhood, followed by cutaneous and plexiform neurofibromas; these criteria often establish the diagnosis before nerve or brain tumors appear."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The optic pathway glioma is NF1's signature brain tumor: a low-grade pilocytic astrocytoma of the optic nerve/chiasm in ~15% of children, often indolent but able to threaten vision; NF1 also raises risk of other gliomas, with MEK inhibitors (selumetinib) used for progression."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "NF1 predisposes to pheochromocytoma: loss of neurofibromin's RAS-GAP activity in adrenal-medullary chromaffin cells drives catecholamine-secreting tumors in ~1-5% of NF1 patients, so unexplained hypertension in NF1 warrants plasma metanephrine screening."
  - target: 01-human/07-system/noonan-syndrome
    relation: connects-to
    note: "NF1 and Noonan syndrome are both RASopathies—germline disorders of the RAS-MAPK pathway—and overlap clinically: a 'neurofibromatosis-Noonan' phenotype exists, with short stature, learning issues, and cardiac or pigmentary signs blurring the two."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Women with NF1 carry roughly double the breast cancer risk with worse outcomes, especially before age 50: neurofibromin loss disinhibits RAS-MAPK in breast epithelium, so NF1 guidelines recommend earlier, enhanced mammographic and MRI screening."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "NF1-associated and IDH-mutant gliomas are two distinct molecular routes to glioma: NF1's neurofibromin loss disinhibits Ras, driving optic-pathway gliomas, while sporadic adult gliomas are often IDH-mutant—Ras-pathway versus metabolic-epigenetic routes."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Rhabdomyosarcoma is part of the NF1 tumor spectrum: neurofibromin loss disinhibiting Ras predisposes children with NF1 to this skeletal-muscle sarcoma (often embryonal subtype), adding a soft-tissue cancer to NF1's neurofibromas, optic gliomas and MPNSTs."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "NF1 and Gorlin are both autosomal-dominant tumor-predisposition phakomatoses driven by loss of a single pathway brake: NF1's neurofibromin loss unleashes Ras, Gorlin's PTCH1 loss unleashes Hedgehog—two pathways, one syndromic logic."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Neurofibromas grow on the nerves NF1 affects: loss of neurofibromin in Schwann-cell-lineage cells lets benign neurofibromas form along peripheral nerves enveloping their neurons, causing the skin nodules and plexiform tumors that define neurofibromatosis type 1."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "NF1 predisposes to gliomas from optic pathway to high-grade: neurofibromin normally restrains RAS, so its loss drives childhood optic pathway gliomas and, less often, glioblastoma—linking the syndrome's RAS-pathway defect to brain as well as nerve tumors."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye gives diagnostic clues to NF1: Lisch nodules (iris hamartomas) are a near-universal diagnostic criterion, and optic pathway gliomas threaten vision—so ophthalmologic exam is central to diagnosing and monitoring neurofibromatosis type 1."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "NF1 is fundamentally a tumor-prone disorder of the nervous system: loss of neurofibromin unleashes RAS in nerve-sheath cells, producing neurofibromas, optic gliomas and learning difficulties—so the nervous system bears both the benign tumors and the cognitive features."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin announces NF1: café-au-lait macules, axillary freckling and cutaneous neurofibromas are diagnostic criteria usually present from childhood, so the integumentary system gives the earliest and most accessible signs of the syndrome."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "NF1 also affects the skeleton: scoliosis, sphenoid-wing dysplasia and tibial pseudarthrosis (a non-healing congenital fracture) are recognized bony features, so the musculoskeletal system is part of this multisystem RAS-pathway disorder."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "NF1 is a treatable cause of secondary hypertension in the young: renal-artery stenosis from arterial dysplasia and catecholamine-secreting pheochromocytomas both raise blood pressure, so hypertension in an NF1 patient triggers a search for these causes."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "NF1's signature brain tumor is an astrocyte glioma: optic pathway and other low-grade pilocytic astrocytomas arise when neurofibromin loss unleashes RAS in glial cells, so children with NF1 are screened for vision-threatening optic gliomas."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "NF1 is a RASopathy driven through ERK: neurofibromin normally switches off RAS, so its loss leaves RAS-RAF-MEK-ERK signaling stuck on—the rationale for MEK inhibitors like selumetinib that shrink inoperable plexiform neurofibromas."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "NF1 loss feeds the mTOR growth engine: without neurofibromin's brake on RAS, the PI3K-AKT-mTOR arm runs high alongside the MAPK pathway, so mTOR inhibitors like sirolimus are tested to shrink plexiform neurofibromas."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "NF1 weakens bone through its osteoblasts: neurofibromin loss disrupts these bone-building cells, causing scoliosis, sphenoid-wing dysplasia, and the hard-to-heal tibial pseudarthrosis that are skeletal hallmarks of the syndrome."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "NF1's optic pathway gliomas can disturb growth hormone: tumors near the hypothalamus and pituitary derail the growth axis, causing precocious puberty or growth-hormone problems—why NF1 children need growth and endocrine monitoring."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Neurofibromas are built with macrophages: alongside the mast cells that drive their itch, macrophages make up much of the tumor and secrete factors that help the Schwann-cell tumors grow—a stromal target in this nerve disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "NF1 loss unleashes growth through AKT: without neurofibromin's brake on Ras, signaling pours into the PI3K-AKT-mTOR pathway as well as ERK, so AKT-mTOR inhibitors join MEK inhibitors as strategies against the tumors."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "NF1 predisposes to adrenal pheochromocytoma: loss of neurofibromin in adrenal medullary cells drives catecholamine-secreting tumors, so unexplained hypertension in NF1 prompts a hunt for a pheochromocytoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "NF1's café-au-lait spots are painted with copper: the flat brown macules and skinfold freckling come from excess melanin, built by the copper-dependent enzyme tyrosinase in pigment cells."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "NF1 vasculopathy chokes the kidney's arteries: neurofibromin loss in vessel walls narrows the renal arteries, a cause of the hypertension that, with pheochromocytoma, must be sought in NF1."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "NF1 weakens the blood-vessel lining: loss of neurofibromin in endothelial and smooth-muscle cells drives a vasculopathy of stenoses and aneurysms, behind the strokes and renovascular disease of the syndrome."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons watch NF1 unfold: MRI tracks optic-pathway gliomas and plexiform neurofibromas, whole-body MRI gauges tumor burden, and slit-lamp light spots the Lisch nodules on the iris that help clinch the diagnosis."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Neurofibromas are mixed tumors, and fibroblasts are part of the mix: alongside Schwann cells, perineurial cells, and mast cells, fibroblasts lay down the loose collagenous matrix that gives these soft, fleshy nodules their texture."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "NF1 can be born into the heart: like the related RASopathies, it raises the risk of congenital heart disease — pulmonary valve stenosis most of all — so children are screened for structural defects alongside their tumors."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy dissects the neurofibroma: it is a mix of Schwann cells, perineurial cells, fibroblasts, and mast cells loosely wrapped in collagen, the heterogeneous tangle that distinguishes it from a pure schwannoma."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "NF1 distorts the growing skeleton: sphenoid-wing dysplasia, scoliosis, and the non-healing tibial pseudarthrosis reflect a bone-forming defect, warping the marrow-bearing bones from birth."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "NF1 can scar the lungs: a diffuse interstitial lung disease with basal fibrosis and upper-lobe bullae develops in some adults, adding pulmonary disease to the syndrome's tumors and skeletal changes."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Biopsy reads the tumors by antibody: S100 and SOX10 stains confirm a neurofibroma's Schwann-cell origin, and as a benign lesion transforms toward MPNST the loss of H3K27me3 staining flags the dangerous change."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "NF1 reaches the bowel several ways: intestinal neurofibromas and ganglioneuromatosis stud the gut wall, and the syndrome's GISTs and periampullary neuroendocrine tumors can bleed or obstruct, making GI symptoms a reason to look harder."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "NF1 quietly weakens bone: patients run low on vitamin D with reduced bone mineral density and more fractures, an osteopenia that compounds the syndrome's scoliosis and dysplasia and is watched and supplemented in their care."
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
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — NF1 neurofibromas — cutaneous, subcutaneous, and plexiform — grow from Schwann cells of peripheral nerves after a somatic second hit knocks out the remaining NF1 allele; plexiform neurofibromas are the precursor lesion that can transform into MPNST in ~10-15%.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Neurofibroma growth depends on its microenvironment: NF1-haploinsufficient mast cells and fibroblasts secrete stem-cell factor (SCF/KIT ligand) that drives proliferation of the NF1-null Schwann cells — a paracrine loop explored therapeutically with imatinib (anti-KIT).
- `connects-to` → **[GIST](../gist/README.md)** — GIST occurs in ~3-5% of NF1 patients but is biologically distinct from sporadic GIST: NF1-associated GISTs are KIT/PDGFRA wild-type (driven instead by NF1 loss → RAS-MAPK), so they respond poorly to imatinib, with sunitinib or regorafenib used in later lines.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — NF1 and NF2 share a name and dominant inheritance but are unrelated diseases: NF1 (neurofibromin, a RAS-GAP) drives café-au-lait spots and neurofibromas, while NF2 (merlin, a Hippo regulator) drives bilateral vestibular schwannomas and meningiomas — different genes and pathways.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin shows NF1's earliest and most reliable signs: six or more café-au-lait macules and axillary/inguinal freckling appear in childhood, followed by cutaneous and plexiform neurofibromas; these criteria often establish the diagnosis before nerve or brain tumors appear.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The optic pathway glioma is NF1's signature brain tumor: a low-grade pilocytic astrocytoma of the optic nerve/chiasm in ~15% of children, often indolent but able to threaten vision; NF1 also raises risk of other gliomas, with MEK inhibitors (selumetinib) used for progression.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — NF1 predisposes to pheochromocytoma: loss of neurofibromin's RAS-GAP activity in adrenal-medullary chromaffin cells drives catecholamine-secreting tumors in ~1-5% of NF1 patients, so unexplained hypertension in NF1 warrants plasma metanephrine screening.
- `connects-to` → **[Noonan Syndrome](../noonan-syndrome/README.md)** — NF1 and Noonan syndrome are both RASopathies—germline disorders of the RAS-MAPK pathway—and overlap clinically: a 'neurofibromatosis-Noonan' phenotype exists, with short stature, learning issues, and cardiac or pigmentary signs blurring the two.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Women with NF1 carry roughly double the breast cancer risk with worse outcomes, especially before age 50: neurofibromin loss disinhibits RAS-MAPK in breast epithelium, so NF1 guidelines recommend earlier, enhanced mammographic and MRI screening.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — NF1-associated and IDH-mutant gliomas are two distinct molecular routes to glioma: NF1's neurofibromin loss disinhibits Ras, driving optic-pathway gliomas, while sporadic adult gliomas are often IDH-mutant—Ras-pathway versus metabolic-epigenetic routes.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Rhabdomyosarcoma is part of the NF1 tumor spectrum: neurofibromin loss disinhibiting Ras predisposes children with NF1 to this skeletal-muscle sarcoma (often embryonal subtype), adding a soft-tissue cancer to NF1's neurofibromas, optic gliomas and MPNSTs.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — NF1 and Gorlin are both autosomal-dominant tumor-predisposition phakomatoses driven by loss of a single pathway brake: NF1's neurofibromin loss unleashes Ras, Gorlin's PTCH1 loss unleashes Hedgehog—two pathways, one syndromic logic.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Neurofibromas grow on the nerves NF1 affects: loss of neurofibromin in Schwann-cell-lineage cells lets benign neurofibromas form along peripheral nerves enveloping their neurons, causing the skin nodules and plexiform tumors that define neurofibromatosis type 1.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — NF1 predisposes to gliomas from optic pathway to high-grade: neurofibromin normally restrains RAS, so its loss drives childhood optic pathway gliomas and, less often, glioblastoma—linking the syndrome's RAS-pathway defect to brain as well as nerve tumors.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye gives diagnostic clues to NF1: Lisch nodules (iris hamartomas) are a near-universal diagnostic criterion, and optic pathway gliomas threaten vision—so ophthalmologic exam is central to diagnosing and monitoring neurofibromatosis type 1.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — NF1 is fundamentally a tumor-prone disorder of the nervous system: loss of neurofibromin unleashes RAS in nerve-sheath cells, producing neurofibromas, optic gliomas and learning difficulties—so the nervous system bears both the benign tumors and the cognitive features.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin announces NF1: café-au-lait macules, axillary freckling and cutaneous neurofibromas are diagnostic criteria usually present from childhood, so the integumentary system gives the earliest and most accessible signs of the syndrome.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — NF1 also affects the skeleton: scoliosis, sphenoid-wing dysplasia and tibial pseudarthrosis (a non-healing congenital fracture) are recognized bony features, so the musculoskeletal system is part of this multisystem RAS-pathway disorder.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — NF1 is a treatable cause of secondary hypertension in the young: renal-artery stenosis from arterial dysplasia and catecholamine-secreting pheochromocytomas both raise blood pressure, so hypertension in an NF1 patient triggers a search for these causes.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — NF1's signature brain tumor is an astrocyte glioma: optic pathway and other low-grade pilocytic astrocytomas arise when neurofibromin loss unleashes RAS in glial cells, so children with NF1 are screened for vision-threatening optic gliomas.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — NF1 is a RASopathy driven through ERK: neurofibromin normally switches off RAS, so its loss leaves RAS-RAF-MEK-ERK signaling stuck on—the rationale for MEK inhibitors like selumetinib that shrink inoperable plexiform neurofibromas.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — NF1 loss feeds the mTOR growth engine: without neurofibromin's brake on RAS, the PI3K-AKT-mTOR arm runs high alongside the MAPK pathway, so mTOR inhibitors like sirolimus are tested to shrink plexiform neurofibromas.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — NF1 weakens bone through its osteoblasts: neurofibromin loss disrupts these bone-building cells, causing scoliosis, sphenoid-wing dysplasia, and the hard-to-heal tibial pseudarthrosis that are skeletal hallmarks of the syndrome.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — NF1's optic pathway gliomas can disturb growth hormone: tumors near the hypothalamus and pituitary derail the growth axis, causing precocious puberty or growth-hormone problems—why NF1 children need growth and endocrine monitoring.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Neurofibromas are built with macrophages: alongside the mast cells that drive their itch, macrophages make up much of the tumor and secrete factors that help the Schwann-cell tumors grow—a stromal target in this nerve disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — NF1 loss unleashes growth through AKT: without neurofibromin's brake on Ras, signaling pours into the PI3K-AKT-mTOR pathway as well as ERK, so AKT-mTOR inhibitors join MEK inhibitors as strategies against the tumors.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — NF1 predisposes to adrenal pheochromocytoma: loss of neurofibromin in adrenal medullary cells drives catecholamine-secreting tumors, so unexplained hypertension in NF1 prompts a hunt for a pheochromocytoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — NF1's café-au-lait spots are painted with copper: the flat brown macules and skinfold freckling come from excess melanin, built by the copper-dependent enzyme tyrosinase in pigment cells.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — NF1 vasculopathy chokes the kidney's arteries: neurofibromin loss in vessel walls narrows the renal arteries, a cause of the hypertension that, with pheochromocytoma, must be sought in NF1.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — NF1 weakens the blood-vessel lining: loss of neurofibromin in endothelial and smooth-muscle cells drives a vasculopathy of stenoses and aneurysms, behind the strokes and renovascular disease of the syndrome.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons watch NF1 unfold: MRI tracks optic-pathway gliomas and plexiform neurofibromas, whole-body MRI gauges tumor burden, and slit-lamp light spots the Lisch nodules on the iris that help clinch the diagnosis.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Neurofibromas are mixed tumors, and fibroblasts are part of the mix: alongside Schwann cells, perineurial cells, and mast cells, fibroblasts lay down the loose collagenous matrix that gives these soft, fleshy nodules their texture.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — NF1 can be born into the heart: like the related RASopathies, it raises the risk of congenital heart disease — pulmonary valve stenosis most of all — so children are screened for structural defects alongside their tumors.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy dissects the neurofibroma: it is a mix of Schwann cells, perineurial cells, fibroblasts, and mast cells loosely wrapped in collagen, the heterogeneous tangle that distinguishes it from a pure schwannoma.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — NF1 distorts the growing skeleton: sphenoid-wing dysplasia, scoliosis, and the non-healing tibial pseudarthrosis reflect a bone-forming defect, warping the marrow-bearing bones from birth.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — NF1 can scar the lungs: a diffuse interstitial lung disease with basal fibrosis and upper-lobe bullae develops in some adults, adding pulmonary disease to the syndrome's tumors and skeletal changes.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Biopsy reads the tumors by antibody: S100 and SOX10 stains confirm a neurofibroma's Schwann-cell origin, and as a benign lesion transforms toward MPNST the loss of H3K27me3 staining flags the dangerous change.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — NF1 reaches the bowel several ways: intestinal neurofibromas and ganglioneuromatosis stud the gut wall, and the syndrome's GISTs and periampullary neuroendocrine tumors can bleed or obstruct, making GI symptoms a reason to look harder.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — NF1 quietly weakens bone: patients run low on vitamin D with reduced bone mineral density and more fractures, an osteopenia that compounds the syndrome's scoliosis and dysplasia and is watched and supplemented in their care.

[^gutmann-2017-nf1-primer]: Gutmann DH, Ferner RE, Listernick RH, et al. Neurofibromatosis type 1. *Nat Rev Dis Primers.* 2017;3:17004. [doi:10.1038/nrdp.2017.4](https://doi.org/10.1038/nrdp.2017.4) · [PubMed 28230061](https://pubmed.ncbi.nlm.nih.gov/28230061/)
[^dombi-2016-selumetinib]: Dombi E, Baldwin A, Marcus LJ, et al. Activity of Selumetinib in Neurofibromatosis Type 1-Related Plexiform Neurofibromas. *N Engl J Med.* 2016;375(26):2550-2560. [doi:10.1056/NEJMoa1605943](https://doi.org/10.1056/NEJMoa1605943) · [PubMed 28029918](https://pubmed.ncbi.nlm.nih.gov/28029918/)
