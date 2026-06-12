---
schema: human-scale-entry/v1
id: mpnst
name: MPNST
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "MPNST is the most lethal NF1-associated tumor; NF1 LOF + CDKN2A deletion + PRC2/SUZ12 LOF → H3K27me3 loss defines high-grade MPNST; ~50% sporadic; surgery is the only curative modality; 5-year OS ~25-40%; selumetinib active in NF1 plexiform neurofibromas but not MPNST."
aliases: ["MPNST", "malignant peripheral nerve sheath tumor", "NF1 MPNST", "neurofibrosarcoma", "malignant schwannoma", "sarcoma NF1", "plexiform neurofibroma malignant transformation", "MPNST SUZ12", "MPNST H3K27me3", "MPNST PRC2"]
sources:
  - id: evans-2002-mpnst-nf1
    type: peer-reviewed
    cite: "Evans DGR, Baser ME, McGaughran J, et al. Malignant peripheral nerve sheath tumours in neurofibromatosis 1. J Med Genet. 2002;39(5):311-314."
    doi: "10.1136/jmg.39.5.311"
    pmid: "12011145"
    url: "https://doi.org/10.1136/jmg.39.5.311"
  - id: lee-2014-mpnst-prc2
    type: peer-reviewed
    cite: "Lee W, Teckie S, Wiesner T, et al. PRC2 is recurrently inactivated through EED or SUZ12 loss in malignant peripheral nerve sheath tumors. Nat Genet. 2014;46(11):1227-1232."
    doi: "10.1038/ng.3095"
    pmid: "25240281"
    url: "https://doi.org/10.1038/ng.3095"
cross_links:
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 syndrome (germline NF1) confers ~10% lifetime MPNST risk; NF1-associated MPNST arises from plexiform neurofibroma transformation; NF1 LOF → RAS → MAPK/PI3K → MPNST growth; NF1-associated MPNST has worse OS than sporadic (~25% vs ~50% 5-year OS)."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A homozygous deletion in ~70-80% high-grade MPNST; NF1+CDKN2A loss → CDK4/6 → RB1 phosphorylation → E2F proliferation; ARF loss → MDM2 unrestricted → p53 inactivation without TP53 mutation; CDK4/6 inhibitors (palbociclib) active in preclinical MPNST."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "PRC2/EZH2 is inactivated in ~70-90% high-grade MPNST by SUZ12 or EED mutations → H3K27me3 LOST (contrast AT/RT/SS where H3K27me3 accumulates); H3K27me3 loss by IHC is a diagnostic marker for high-grade MPNST; EZH2 inhibitors are NOT active in MPNST (PRC2 already lost)."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "NF1 LOF → RAS → MEK/ERK1/2 hyperactivation drives MPNST proliferation; MEK inhibitors (trametinib, binimetinib) explored in preclinical MPNST — less active than in neurofibroma; MPNST MEK resistance via PI3K bypass; MEK + mTOR or MEK + CDK4/6 dual inhibition being studied."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Neurofibromatosis type 1 (germline NF1 loss) carries a ~10% lifetime MPNST risk, arising when a plexiform neurofibroma transforms via CDKN2A deletion then PRC2 inactivation; sudden growth or pain in a stable plexiform lesion demands urgent FDG-PET and biopsy."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "MPNST is a high-grade sarcoma of the Schwann-cell sheath that grows from a major peripheral nerve trunk, often requiring en bloc nerve sacrifice; perineural spread mandates wide (≥2 cm) margins, and S100/SOX10 are only focally positive unlike benign schwannoma."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "MPNST and AT/RT sit at opposite poles of PRC2 biology: MPNST inactivates PRC2 (SUZ12/EED loss) so H3K27me3 is LOST, whereas AT/RT (SMARCB1 loss) leaves PRC2 hyperactive with H3K27me3 retained — so H3K27me3 IHC separates them and EZH2 inhibitors help AT/RT but not MPNST."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "MPNST and schwannomatosis are both peripheral nerve sheath tumor disorders but opposite in behavior: schwannomatosis makes multiple benign, painful schwannomas (SMARCB1/LZTR1), while MPNST is a high-grade Schwann-cell sarcoma arising mostly from NF1 plexiform neurofibromas."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "MPNST and synovial sarcoma are monomorphic spindle-cell sarcomas that mimic each other, but their epigenetics differ diagnostically: MPNST loses PRC2 (H3K27me3 absent by IHC) while synovial sarcoma's SS18-SSX fusion retains it — one stain excludes one and confirms the other."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "MPNST is a high-grade soft-tissue sarcoma of the limbs, trunk, and paraspinal region arising from a major nerve trunk; like other extremity sarcomas it needs wide en-bloc resection plus radiation, but perineural spread and chemoresistance make it among the deadliest."
---

# MPNST

## Overview

**Malignant peripheral nerve sheath tumor (MPNST)** is a high-grade soft tissue sarcoma arising from the neural crest-derived Schwann cell lineage, defined by a characteristic molecular signature of **NF1 LOF + CDKN2A deletion + PRC2 (SUZ12/EED) inactivation**. MPNST is the most lethal tumor associated with **neurofibromatosis type 1 (NF1) syndrome** and the leading cause of NF1-related mortality. It arises predominantly from malignant transformation of plexiform neurofibromas, but ~40-50% of cases occur sporadically without germline NF1 mutation. MPNST has no approved targeted therapy; surgery is the only curative modality, and prognosis remains poor, particularly in NF1-associated disease [^evans-2002-mpnst-nf1].

**Epidemiology:**
- Incidence: ~1,500-2,000 cases/year USA (~0.001% general population); ~10% lifetime risk in NF1 syndrome
- NF1-associated MPNST: ~50-60% of all MPNST; arises from plexiform neurofibroma
- Sporadic MPNST: ~40-50%; arise de novo from peripheral nerve without NF1; molecularly distinct from NF1-associated in ~30-40% (lack biallelic NF1 mutation but share CDKN2A + PRC2 alterations)
- Radiation-induced MPNST: ~10%; arises in radiation field, median 10-15 years after exposure; worst prognosis
- Median age: NF1-associated ~26-30 years; sporadic ~40-50 years; MPNST is a "young adult" sarcoma
- Sex: equal M:F distribution

**Key clinical features:**
- Rapidly enlarging, painful mass arising from or along a peripheral nerve trunk
- Most common sites: proximal extremities (thigh, upper arm), trunk/paraspinal region, head and neck
- In NF1 patients: rapid growth or pain in a previously stable plexiform neurofibroma → urgent workup
- FDG-PET: highly SUV-avid (SUVmax typically >4-6); distinguishes MPNST from benign plexiform (SUVmax <3.5) and guides biopsy; MPNST FDG-PET sensitivity ~89%, specificity ~95%

## Structure

### Molecular classification

**The three-hit model of MPNST:**
1. **NF1 LOF**: biallelic NF1 inactivation (germline + somatic LOH, or two somatic hits) → RAS constitutive activation
2. **CDKN2A homozygous deletion** (~70-80%): p16(INK4a) loss → CDK4/6 → RB1 hyperphosphorylation → E2F cell cycle; ARF loss → MDM2 unrestricted → p53 pathway loss (without TP53 mutation)
3. **PRC2 inactivation** (SUZ12 or EED mutation, ~70-90%): [^lee-2014-mpnst-prc2] H3K27 trimethylation LOST → de-repression of developmental transcription factors; inverse of AT/RT and synovial sarcoma (where PRC2 is hyperactive)

**Additional somatic alterations in MPNST:**
- TP53 mutations: ~15-25%; late event; radiotherapy-induced MPNST enriched
- ATRX mutations: ~20%; alternative lengthening of telomeres
- RB1 mutations: ~10-15%; often in the setting of CDKN2A deletion
- EGFR amplification: ~15-20%; receptor tyrosine kinase amplification
- MET amplification: ~10%; poor prognosis
- CDC42/RAC1 mutations: rare; cytoskeletal signaling

### Histology

**Classic MPNST histology:**
- Fascicular architecture of spindle cells with hyperchromatic, wavy, or comma-shaped nuclei; reminiscent of cellular schwannoma but with atypia
- Alternating hypercellular and hypocellular areas ("marbling pattern")
- Geographic necrosis; hemangiopericytoma-like vessels
- High mitotic rate (>4/10 HPF in WHO definition; typically >10/10 HPF in high-grade)
- Variable "heterologous differentiation" (rhabdomyoblastic = Triton tumor, osteosarcomatous, chondroid): ~15-20% of MPNST have divergent elements

**Grading:** MPNST are uniformly FNCLCC grade 2-3; grade 3 features (>10 mitoses/10 HPF, necrosis, high cellularity) confer worse prognosis

### IHC panel and diagnostic workup

**SOX10**: most sensitive marker for Schwann cell lineage in MPNST; positive in ~40-50%; focal; absent in ~50% (unlike benign schwannoma where SOX10 is diffusely positive)

**S100**: positive in ~50-70% of low-grade MPNST; only ~30-40% of high-grade MPNST; focal/patchy (unlike diffuse S100 in schwannoma)

**H3K27me3 (trimethyl H3K27 IHC):** LOST (complete loss of nuclear H3K27me3 staining) in ~70-90% of high-grade MPNST due to PRC2 inactivation; highly diagnostic — complete H3K27me3 loss in a spindle cell sarcoma = strong evidence for MPNST; retained in schwannoma, neurofibroma, synovial sarcoma, AT/RT; sensitivity ~70-90%, specificity ~95% for MPNST vs benign NF1 neurofibroma

**CDKN2A FISH:** homozygous deletion by FISH → confirms MPNST molecular signature; useful in NF1 patients where biopsy shows borderline atypia

**NF1 protein (neurofibromin IHC):** neurofibromin expression lost in most MPNST; however, IHC is variable and not routinely used in diagnosis; NF1 FISH/sequencing preferred

**Ki-67:** typically >30% in high-grade MPNST; useful for distinguishing from atypical neurofibroma (Ki-67 <10%)

## Function

### Oncogenesis: plexiform neurofibroma → MPNST

The malignant transformation of plexiform neurofibroma to MPNST follows an ordered acquisition of molecular hits:

**Step 1 — NF1 LOF (neurofibroma):**
Germline NF1 + somatic LOH at 17q11.2 → biallelic NF1 loss in Schwann cell → RAS-GTP accumulation → mast cell recruitment (SCF/c-KIT) → neurofibroma microenvironment; benign neurofibromas require mast cell support and are indolent

**Step 2 — CDKN2A deletion (atypical neurofibroma):**
Emerging somatic CDKN2A homozygous deletion → p16 loss → CDK4/6 hyperactivation → first step toward autonomy; "atypical neurofibromatous neoplasm of uncertain biological potential" (ANNUBP) = intermediate lesion with CDKN2A deletion but lacking PRC2 mutations or high-grade features

**Step 3 — PRC2 inactivation (MPNST):**
SUZ12 or EED mutation (often biallelic) → EZH2 enzymatic activity lost → H3K27me3 erased → developmental transcription factors (HOXC, HOXD clusters, TWIST1, SOX11) de-repressed → Schwann cells lose lineage identity → mesenchymal plasticity → high-grade sarcomatous phenotype

**Key distinction from AT/RT and synovial sarcoma:**
- **AT/RT**: SMARCB1 biallelic deletion → BAF lost → PRC2/EZH2 hyperactive → H3K27me3 accumulated → EZH2 inhibitors active
- **Synovial sarcoma**: SS18-SSX → SMARCB1 displaced from BAF → PRC2/EZH2 hyperactive → H3K27me3 accumulated → EZH2 inhibitors active
- **MPNST**: SUZ12/EED LOF → PRC2/EZH2 catalytically dead → H3K27me3 LOST → EZH2 inhibitors NOT active (PRC2 cannot be further inhibited)

This is a critical diagnostic and therapeutic distinction: H3K27me3 IHC distinguishes MPNST (lost) from AT/RT and SS (retained/elevated).

## Pathology

### Staging and risk stratification

**Prognostic factors:**
- **Germline NF1 status**: NF1-associated MPNST 5-year OS ~25-40%; sporadic MPNST ~50-60%; radiation-induced MPNST ~20-30%
- **Tumor size**: most important single factor; ≤5 cm → 5-year OS ~55-70%; >5 cm → ~30-40%
- **Margin status**: R0 resection essential; R1 → 50% local recurrence; R2 → near-universal recurrence
- **Grade**: FNCLCC grade 3 → significantly worse prognosis than grade 2
- **CDKN2A deletion**: independently associated with worse OS
- **Metastases**: lung (~80% of metastases), liver, bone; ~20% metastatic at diagnosis; 5-year OS ~15%

### Treatment

**Surgery:**
Wide local excision with negative margins is the only potentially curative intervention; MPNST margins must be generous (≥2 cm) due to perineural spread tendency; limb-sparing preferred; en bloc nerve sacrifice required if MPNST arises from named nerve (sciatic, brachial plexus); compartmental resection for large tumors; spinal MPNST requires vertebrectomy ± cord decompression

**Radiation therapy:**
- Pre- or postoperative RT for high-risk features (tumor >5 cm, positive margin, recurrence, radiation-naive)
- Standard dose: 50-54 Gy preoperative or 60-66 Gy postoperative
- RT for MPNST must balance efficacy against radiation-field carcinogenesis risk (especially in NF1 patients)
- NF1 patients have increased radiation sensitivity and secondary malignancy risk → limit RT field/dose where possible

**Chemotherapy:**
- MPNST is chemotherapy-resistant compared to other sarcomas; responses are modest
- **Doxorubicin + ifosfamide (AI)**: standard first-line for metastatic/unresectable; ORR ~20-30% (lower than synovial sarcoma ORR ~40-60%)
- **Ifosfamide monotherapy**: ORR ~10-15% in MPNST
- **Gemcitabine + docetaxel**: second-line option; ORR ~10-15%
- No clinical trial has demonstrated OS benefit from chemotherapy in MPNST to date; chemotherapy used to control symptoms/slow progression

**Targeted therapies (no approved agent for MPNST):**
- **MEK inhibitors** (selumetinib, trametinib): active in NF1 plexiform neurofibromas but largely inactive in MPNST (CDKN2A + PRC2 co-mutations bypass MEK dependence); single-arm Phase 2 trials: selumetinib ORR 0% in MPNST; MEK + CDK4/6 and MEK + mTOR combinations in Phase 1/2
- **CDK4/6 inhibitors** (palbociclib): CDKN2A deletion in ~70-80% provides rationale; preclinical activity; clinical trials ongoing (NCT03605654)
- **PRC2 reconstitution**: investigational — strategies to restore H3K27me3 via epigenetic modulators; no clinical agents yet
- **Cabozantinib** (MET/VEGFR/RET): Phase 2 SARC051 ongoing in advanced sarcomas including MPNST
- **VEGFR inhibitors** (pazopanib): modest activity in MPNST as part of STS population trials

**Prognosis:**
- NF1-associated MPNST: 5-year OS ~25-40%; local recurrence major problem (~40-50%)
- Sporadic MPNST: 5-year OS ~50-60%
- Radiation-induced MPNST: 5-year OS ~20-25%; worst outcome subgroup
- Metastatic MPNST: median OS ~12-18 months; no curative option
- Local recurrence: ~40-50% at 5 years even after R0 resection; re-resection if technically feasible
- Primary CNS MPNST (optic nerve, cranial nerve VIII): particularly difficult; CN VIII MPNST rare; surgical approach highly morbid

## Connections

- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 syndrome (germline NF1) confers ~10% lifetime MPNST risk; NF1-associated MPNST arises from plexiform neurofibroma transformation; NF1 LOF → RAS → MAPK/PI3K → MPNST growth; NF1-associated MPNST has worse OS than sporadic (~25% vs ~50% 5-year OS).
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A homozygous deletion in ~70-80% high-grade MPNST; NF1+CDKN2A loss → CDK4/6 → RB1 phosphorylation → E2F proliferation; ARF loss → MDM2 unrestricted → p53 inactivation without TP53 mutation; CDK4/6 inhibitors (palbociclib) active in preclinical MPNST.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — PRC2/EZH2 is inactivated in ~70-90% high-grade MPNST by SUZ12 or EED mutations → H3K27me3 LOST (contrast AT/RT/SS where H3K27me3 accumulates); H3K27me3 loss by IHC is a diagnostic marker for high-grade MPNST; EZH2 inhibitors are NOT active in MPNST (PRC2 already lost).
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — NF1 LOF → RAS → MEK/ERK1/2 hyperactivation drives MPNST proliferation; MEK inhibitors (trametinib, binimetinib) explored in preclinical MPNST — less active than in neurofibroma; MPNST MEK resistance via PI3K bypass; MEK + mTOR or MEK + CDK4/6 dual inhibition being studied.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Neurofibromatosis type 1 (germline NF1 loss) carries a ~10% lifetime MPNST risk, arising when a plexiform neurofibroma transforms via CDKN2A deletion then PRC2 inactivation; sudden growth or pain in a stable plexiform lesion demands urgent FDG-PET and biopsy.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — MPNST is a high-grade sarcoma of the Schwann-cell sheath that grows from a major peripheral nerve trunk, often requiring en bloc nerve sacrifice; perineural spread mandates wide (≥2 cm) margins, and S100/SOX10 are only focally positive unlike benign schwannoma.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — MPNST and AT/RT sit at opposite poles of PRC2 biology: MPNST inactivates PRC2 (SUZ12/EED loss) so H3K27me3 is LOST, whereas AT/RT (SMARCB1 loss) leaves PRC2 hyperactive with H3K27me3 retained — so H3K27me3 IHC separates them and EZH2 inhibitors help AT/RT but not MPNST.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — MPNST and schwannomatosis are both peripheral nerve sheath tumor disorders but opposite in behavior: schwannomatosis makes multiple benign, painful schwannomas (SMARCB1/LZTR1), while MPNST is a high-grade Schwann-cell sarcoma arising mostly from NF1 plexiform neurofibromas.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — MPNST and synovial sarcoma are monomorphic spindle-cell sarcomas that mimic each other, but their epigenetics differ diagnostically: MPNST loses PRC2 (H3K27me3 absent by IHC) while synovial sarcoma's SS18-SSX fusion retains it — one stain excludes one and confirms the other.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — MPNST is a high-grade soft-tissue sarcoma of the limbs, trunk, and paraspinal region arising from a major nerve trunk; like other extremity sarcomas it needs wide en-bloc resection plus radiation, but perineural spread and chemoresistance make it among the deadliest.

[^evans-2002-mpnst-nf1]: Evans DGR, Baser ME, McGaughran J, et al. Malignant peripheral nerve sheath tumours in neurofibromatosis 1. *J Med Genet.* 2002;39(5):311-314. [doi:10.1136/jmg.39.5.311](https://doi.org/10.1136/jmg.39.5.311) · [PubMed 12011145](https://pubmed.ncbi.nlm.nih.gov/12011145/)
[^lee-2014-mpnst-prc2]: Lee W, Teckie S, Wiesner T, et al. PRC2 is recurrently inactivated through EED or SUZ12 loss in malignant peripheral nerve sheath tumors. *Nat Genet.* 2014;46(11):1227-1232. [doi:10.1038/ng.3095](https://doi.org/10.1038/ng.3095) · [PubMed 25240281](https://pubmed.ncbi.nlm.nih.gov/25240281/)
