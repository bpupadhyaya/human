---
schema: human-scale-entry/v1
id: schwannomatosis
name: Schwannomatosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Schwannomatosis is caused by germline SMARCB1 (~40%) or LZTR1 (~30%) mutations; multiple peripheral schwannomas WITHOUT bilateral vestibular schwannomas; chronic pain is the hallmark; distinct from NF2; treatment: surgical resection for symptomatic tumors."
aliases: ["schwannomatosis", "multiple schwannomatosis", "SMARCB1 schwannomatosis", "LZTR1 schwannomatosis", "schwannomatosis type 1", "schwannomatosis type 2", "sporadic schwannomatosis", "schwannomatosis NF2-negative", "hereditary schwannomatosis"]
sources:
  - id: merker-2012-schwannomatosis
    type: peer-reviewed
    cite: "Merker VL, Esparza S, Smith MJ, Stemmer-Rachamimov A, Plotkin SR. Clinical features of schwannomatosis: a retrospective analysis of 87 patients. Oncologist. 2012;17(10):1317-1322."
    doi: "10.1634/theoncologist.2012-0162"
    pmid: "22927469"
    url: "https://doi.org/10.1634/theoncologist.2012-0162"
  - id: piotrowski-2014-lztr1
    type: peer-reviewed
    cite: "Piotrowski A, Xie J, Liu YF, et al. Germline loss-of-function mutations in LZTR1 predispose to an inherited disorder of multiple schwannomas. Nat Genet. 2014;46(2):182-187."
    doi: "10.1038/ng.2855"
    pmid: "24362817"
    url: "https://doi.org/10.1038/ng.2855"
cross_links:
  - target: 01-human/03-molecular/lztr1
    relation: connects-to
    note: "Germline biallelic LZTR1 LOF (or dominant negative missense) causes LZTR1-schwannomatosis; LZTR1 somatic second hit in each schwannoma; Schwann cells with loss of both LZTR1 alleles → RAS-MAPK → schwannoma; presents as chronic pain and multiple peripheral nerve tumors."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SMARCB1 (INI1) germline monoallelic LOF with somatic NF2 LOH as second hit → SMARCB1-schwannomatosis; SMARCB1 acts via Cullin3-RING ligase E3 pathway to regulate SWI/SNF complex; distinct from biallelic SMARCB1 LOF in AT/RT; no increased rhabdoid tumor risk in schwannomatosis."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "NF2 and schwannomatosis both cause multiple schwannomas; NF2 = bilateral VS (pathognomonic) + meningiomas; schwannomatosis = no bilateral VS, peripheral schwannomas, chronic pain; gene panel (NF2/SMARCB1/LZTR1) required for diagnosis; audiogram helps distinguish."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "SMARCB1 biallelic somatic LOF causes AT/RT; germline monoallelic SMARCB1 + somatic NF2 LOH second hit → schwannomatosis (NOT AT/RT); AT/RT risk is not elevated in schwannomatosis carriers; SMARCB1 LOF mechanism is distinct between these two tumor types."
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "Somatic NF2 LOH (22q loss) is the typical second hit in SMARCB1-schwannomatosis schwannomas — the 3-hit model: germline SMARCB1 LOF, then somatic NF2 loss yields the tumor; NF2, SMARCB1, and LZTR1 all cluster on chromosome 22q, so 22q loss inactivates them together."
  - target: 01-human/07-system/noonan-syndrome
    relation: connects-to
    note: "LZTR1 is shared: dominant heterozygous LOF causes Noonan syndrome (a RASopathy), while biallelic LOF or dominant-negative missense variants cause LZTR1-schwannomatosis; some D-N carriers show overlapping Noonan features plus schwannomas — same gene, different dose and mechanism."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Schwannomas arise from the Schwann-cell sheath of peripheral and spinal nerves; spinal nerve roots are the most common site in schwannomatosis; chronic neuropathic pain comes from intraneural growth and nerve compression; fascicle-sparing excision preserves nerve function."
---

# Schwannomatosis

## Overview

**Schwannomatosis** is a rare hereditary tumor predisposition syndrome characterized by the development of **multiple schwannomas** (benign Schwann cell tumors) arising from peripheral and spinal nerves, **without bilateral vestibular schwannomas** (which would define NF2). Schwannomatosis is clinically defined by **chronic severe pain** as the primary symptom — arising from direct nerve compression or intraneural tumor growth — and by an absence of the pathognomonic NF2 features (bilateral acoustic neuromas, meningiomas). Schwannomatosis is genetically heterogeneous: germline pathogenic variants in **SMARCB1** (schwannomatosis type 1, SWN1; ~40% of familial cases) or **LZTR1** (schwannomatosis type 2, SWN2; ~30% of familial cases) account for ~70% of familial schwannomatosis; ~30% of familial cases remain genetically undefined. Approximately ~70% of schwannomatosis cases are apparently sporadic (no family history); of these, SMARCB1 (~10%) and LZTR1 (~20%) germline variants explain a subset. Schwannomatosis prevalence is estimated at ~1 in 40,000-70,000 [^merker-2012-schwannomatosis] [^piotrowski-2014-lztr1].

**Schwannomatosis vs. NF2 — key distinguishing features:**

| Feature | Schwannomatosis | NF2 |
|---|---|---|
| Bilateral vestibular schwannomas | ABSENT (defines non-NF2) | PRESENT (pathognomonic) |
| Peripheral schwannomas | Multiple; all nerve distributions | Present; less prominent than VS |
| Chronic pain | Hallmark; often debilitating | Less characteristic |
| Meningiomas | Rare (in SMARCB1 cases) | Common (~50-80%) |
| Hearing loss | Not primary | Progressive SNHL → deafness |
| Ependymomas | Not characteristic | ~3-10% |
| Genes | SMARCB1, LZTR1, unknown | NF2 |
| Location of VS | N/A | Bilateral; IAC/CPA |
| Cataracts | Not characteristic | Posterior subcapsular (~80%) |

## Structure

### Genetic basis of schwannomatosis

**SMARCB1 (22q11.23) — Schwannomatosis type 1 (SWN1):**
- 9 exons; 385 aa; INI1 (Integrase Interactor 1) / SNF5 (Sucrose Non-Fermenting 5); core subunit of SWI/SNF chromatin remodeling complex
- Germline pathogenic variants: truncating frameshift/nonsense/splice (most common); missense (rare); mostly monoallelic (heterozygous) in schwannomatosis
- **Two-hit mechanism in schwannomatosis (unusual)**: SMARCB1 germline monoallelic LOF (first hit) + somatic second hit — but the second hit in SMARCB1-schwannomatosis is typically **NF2 LOH (22q loss)**, NOT a second SMARCB1 mutation. This is the "3-hit" model of schwannomatosis: (1) germline SMARCB1 LOF → (2) somatic loss of NF2 → Schwann cell with NF2 LOH + hemizygous SMARCB1 → (3) a third hit (LOH of remaining SMARCB1 allele) in malignant contexts (AT/RT). Schwannoma = steps 1+2; AT/RT = steps 1+2+3.
- SMARCB1 germline monoallelic loss → mild phenotype (schwannomatosis); biallelic SMARCB1 somatic loss → AT/RT (different tumor, requires complete SMARCB1 inactivation); AT/RT risk is NOT elevated in schwannomatosis carriers (the third hit is very rare in Schwann cells)
- **Segmental schwannomatosis**: ~5% of schwannomatosis patients have schwannomas restricted to one body segment (arm, leg); often mosaic for somatic SMARCB1 or LZTR1 first hit rather than true germline

**LZTR1 (22q11.21) — Schwannomatosis type 2 (SWN2):**
- 17 exons; 836 aa; BTB-Kelch domain protein; CUL3 E3 ubiquitin ligase adaptor; ubiquitinates RAS GTPases (KRAS4B, MRAS, RRAS2) → proteasomal degradation → RAS-MAPK suppression
- Germline pathogenic variants: biallelic LOF (homozygous or compound heterozygous) = recessive schwannomatosis; heterozygous dominant negative (D-N) missense variants in BTB/BACK domain = dominant schwannomatosis (D-N mutant poisons CUL3 recruitment)
- Somatic second hit: in each schwannoma from LZTR1-germline patients, a second somatic event (LOH, nonsense, frameshift) inactivates the remaining functional LZTR1 allele → biallelic LZTR1 LOF in tumor → RRAS2 accumulation → schwannoma
- LZTR1 is also a **Noonan syndrome gene** (see molecular entry); dominant LOF → Noonan; biallelic/D-N → schwannomatosis; heterozygous D-N variants may cause both NS features + schwannomas

**Note on chromosome 22q clustering:**
Both NF2 (22q12.2), SMARCB1 (22q11.23), and LZTR1 (22q11.21) are on chromosome 22q → somatic 22q loss is a common second hit in all three: NF2 LOH provides the second hit for SMARCB1-schwannomatosis schwannomas; LZTR1 LOH often accompanies NF2 LOH on the same chromosome arm.

## Function

### Clinical features

**Multiple schwannomas — distribution:**
- Peripheral schwannomas: spinal nerve roots (spinal schwannomas most common in schwannomatosis → intraforaminal or extraforaminal masses; cord compression if large), peripheral nerves (brachial plexus, lumbosacral plexus, sciatic nerve, digital nerves)
- Cranial schwannomas: cranial nerves III, V, VII, IX-XII; unilateral CN VIII schwannoma in ~10% of schwannomatosis (UNILATERAL only, not bilateral)
- Cutaneous schwannomas: subcutaneous masses along nerve courses
- Total number: variable; some patients have <10 schwannomas over a lifetime; others develop 50+

**Chronic pain:**
- The dominant clinical problem; pain is often disproportionate to schwannoma size
- Mechanisms: intraneural tumor compression → neuropathic pain; tumor hypersensitivity of nearby nerve fibers; central sensitization
- Character: burning, constant, severe (often 7-10/10 on VAS); affects quality of life dramatically
- Medical management: pregabalin/gabapentin (neuropathic pain); duloxetine; opioids (for severe refractory pain); ketamine infusions; pain clinic involvement critical
- Surgical pain relief: excision of identified schwannomas → often only partial pain relief because multiple tumors exist

**Spinal schwannomas:**
- Spinal cord compression from large intraforaminal/intraspinal schwannomas → myelopathy, radiculopathy; MRI spine is essential for surveillance
- Cauda equina syndrome possible with large lumbosacral schwannomas
- Surgery: primary treatment for symptomatic/compressive spinal schwannomas; goal is nerve preservation (schwannoma arises from nerve sheath but nerve fascicles often preserved → fascicle-sparing excision)

### Malignant peripheral nerve sheath tumor (MPNST)

- MPNST risk in schwannomatosis: controversy; historically reported as elevated; recent data suggest MPNST risk in schwannomatosis is LOW or similar to population baseline (unlike NF1 where MPNST risk is ~10%)
- Key distinction: plexiform neurofibromas (NF1) → MPNST; schwannomas → malignant change is extremely rare
- If rapid growth, pain escalation, new neurological deficit in a known schwannoma → MRI ± FDG-PET; biopsy if malignancy suspected

## Pathology

### Diagnosis of schwannomatosis

**Diagnostic criteria (2022 revised):**
- **Definite schwannomatosis**: ≥2 non-intradermal schwannomas, at least one histopathologically confirmed, NO ipsilateral CN VIII tumor, NO bilateral VS, NO evidence of NF2 germline mutation
- **Suspected schwannomatosis**: ≥2 non-intradermal schwannomas with compatible MRI, no bilateral VS
- **Genetic (molecularly confirmed) schwannomatosis**: meeting above + germline SMARCB1 or LZTR1 pathogenic variant confirmed

**Testing strategy:**
1. MRI brain (with gadolinium): exclude bilateral VS (NF2); detect any unilateral VS (suspicious but not diagnostic for NF2; unilateral VS can occur in schwannomatosis)
2. MRI spine (with gadolinium): spinal schwannomas (most common schwannomatosis location)
3. Audiologic testing: if any VS identified → bilateral hearing evaluation
4. Genetic testing: SMARCB1 sequencing + MLPA; LZTR1 sequencing + MLPA; NF2 sequencing (to exclude NF2)
5. Pathological confirmation: at least one schwannoma from biopsied tumor (histology: Antoni A + Antoni B areas, Verocay bodies, S100+ cells)

**Surveillance:**
- MRI brain + spine: every 2-3 years (all patients); more frequently in symptomatic patients or known growing lesions
- No specific biomarker surveillance (no serum markers established)
- Pain management: referral to specialized pain medicine

**Surgical management:**
- Symptomatic schwannomas (pain, neurological deficit): surgical excision; microsurgical nerve-sparing technique; incomplete excision → recurrence risk ~10% in schwannomatosis vs ~5% in sporadic schwannoma
- Asymptomatic schwannomas: observation; no prophylactic excision
- Gamma Knife / radiosurgery: not typically used for peripheral schwannomas (no established efficacy data for pain relief; RT-associated risk of malignant transformation in multiply irradiated field)

**Family screening:**
- Autosomal dominant for SMARCB1 or LZTR1 dominant schwannomatosis: 50% offspring risk; genetic testing of first-degree relatives
- Recessive LZTR1: siblings of proband have 25% risk (compound het)
- Cascade testing: clinical + genetic screening from age 20

## Connections

- `connects-to` → **[LZTR1](../../03-molecular/lztr1/README.md)** — Germline biallelic LZTR1 LOF (or dominant negative missense) causes LZTR1-schwannomatosis; LZTR1 somatic second hit in each schwannoma; Schwann cells with loss of both LZTR1 alleles → RAS-MAPK → schwannoma; presents as chronic pain and multiple peripheral nerve tumors.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SMARCB1 (INI1) germline monoallelic LOF with somatic NF2 LOH as second hit → SMARCB1-schwannomatosis; SMARCB1 acts via Cullin3-RING ligase E3 pathway to regulate SWI/SNF complex; distinct from biallelic SMARCB1 LOF in AT/RT; no increased rhabdoid tumor risk in schwannomatosis.
- `connects-to` → **[Neurofibromatosis Type 2](../../07-system/neurofibromatosis-type-2/README.md)** — NF2 and schwannomatosis both cause multiple schwannomas; NF2 = bilateral VS (pathognomonic) + meningiomas; schwannomatosis = no bilateral VS, peripheral schwannomas, chronic pain; gene panel (NF2/SMARCB1/LZTR1) required for diagnosis; audiogram helps distinguish.
- `connects-to` → **[Atypical Teratoid Rhabdoid Tumor](../../07-system/atypical-teratoid-rhabdoid-tumor/README.md)** — SMARCB1 biallelic somatic LOF causes AT/RT; germline monoallelic SMARCB1 + somatic NF2 LOH second hit → schwannomatosis (NOT AT/RT); AT/RT risk is not elevated in schwannomatosis carriers; SMARCB1 LOF mechanism is distinct between these two tumor types.
- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — Somatic NF2 LOH (22q loss) is the typical second hit in SMARCB1-schwannomatosis schwannomas — the 3-hit model: germline SMARCB1 LOF, then somatic NF2 loss yields the tumor; NF2, SMARCB1, and LZTR1 all cluster on chromosome 22q, so 22q loss inactivates them together.
- `connects-to` → **[Noonan Syndrome](../noonan-syndrome/README.md)** — LZTR1 is shared: dominant heterozygous LOF causes Noonan syndrome (a RASopathy), while biallelic LOF or dominant-negative missense variants cause LZTR1-schwannomatosis; some D-N carriers show overlapping Noonan features plus schwannomas — same gene, different dose and mechanism.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Schwannomas arise from the Schwann-cell sheath of peripheral and spinal nerves; spinal nerve roots are the most common site in schwannomatosis; chronic neuropathic pain comes from intraneural growth and nerve compression; fascicle-sparing excision preserves nerve function.

[^merker-2012-schwannomatosis]: Merker VL, Esparza S, Smith MJ, Stemmer-Rachamimov A, Plotkin SR. Clinical features of schwannomatosis: a retrospective analysis of 87 patients. *Oncologist.* 2012;17(10):1317-1322. [doi:10.1634/theoncologist.2012-0162](https://doi.org/10.1634/theoncologist.2012-0162) · [PubMed 22927469](https://pubmed.ncbi.nlm.nih.gov/22927469/)
[^piotrowski-2014-lztr1]: Piotrowski A, Xie J, Liu YF, et al. Germline loss-of-function mutations in LZTR1 predispose to an inherited disorder of multiple schwannomas. *Nat Genet.* 2014;46(2):182-187. [doi:10.1038/ng.2855](https://doi.org/10.1038/ng.2855) · [PubMed 24362817](https://pubmed.ncbi.nlm.nih.gov/24362817/)
