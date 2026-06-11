---
schema: human-scale-entry/v1
id: tuberous-sclerosis-complex
name: Tuberous Sclerosis Complex
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Tuberous sclerosis complex (TSC) is caused by germline TSC1 or TSC2 mutations; mTOR hyperactivation → hamartomas in brain (cortical tubers, SEGA), kidney (angiomyolipoma), lung (LAM), skin; everolimus/sirolimus FDA-approved; epilepsy and intellectual disability are common."
aliases: ["TSC", "tuberous sclerosis complex", "tuberous sclerosis", "TSC1 syndrome", "TSC2 syndrome", "SEGA TSC", "angiomyolipoma TSC", "LAM TSC", "TSC brain", "TSC epilepsy"]
sources:
  - id: crino-2006-tsc-review
    type: peer-reviewed
    cite: "Crino PB, Nathanson KL, Henske EP. The tuberous sclerosis complex. N Engl J Med. 2006;355(13):1345-1356."
    doi: "10.1056/NEJMra055323"
    pmid: "17005952"
    url: "https://doi.org/10.1056/NEJMra055323"
  - id: northrup-2013-tsc-consensus
    type: peer-reviewed
    cite: "Northrup H, Krueger DA. Tuberous sclerosis complex diagnostic criteria update: recommendations of the 2012 International Tuberous Sclerosis Complex Consensus Conference. Pediatr Neurol. 2013;49(4):243-254."
    doi: "10.1016/j.pediatrneurol.2013.08.001"
    pmid: "24053982"
    url: "https://doi.org/10.1016/j.pediatrneurol.2013.08.001"
cross_links:
  - target: 01-human/03-molecular/tsc1-tsc2
    relation: connects-to
    note: "Germline TSC1 or TSC2 mutations cause TSC; TSC2 mutations more common (~2/3) and associated with more severe phenotype than TSC1; TSC1-TSC2 complex is the GTPase-activating protein for Rheb; TSC2 is phosphorylated by AKT and AMPK; somatic second hit required in each hamartoma"
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "TSC1/TSC2 LOF → mTORC1 hyperactivation → S6K1/4EBP1 → hamartoma growth; everolimus FDA-approved for TSC-associated renal AML, SEGA, and pulmonary LAM; sirolimus used in TSC-LAM (off-label); mTOR inhibitor side effects: stomatitis, infections, hyperlipidemia"
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK phosphorylates TSC2 Thr1462 → TSC1-TSC2 GTPase activated → Rheb inhibited → mTORC1 OFF; in TSC, this energy-sensing brake is removed → mTORC1 constitutively ON; AMPK activators (metformin) have theoretical benefit in TSC (downstream AMPK activation bypasses TSC2 LOF)"
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "TSC-associated renal tumors: angiomyolipoma (AML; fat+muscle+vessels; embolization or everolimus) and rarely clear cell RCC; everolimus FDA-approved for AML >3 cm at risk of hemorrhage; TSC2 somatic mutation in sporadic RCC = mTOR-sensitive subset"
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "TSC epilepsy affects 80-90% of patients; infantile spasms treated with vigabatrin (~70% ORR); everolimus adjunctive (EXIST-3: 40% vs 22% ≥50% seizure reduction); cannabidiol (Epidiolex; GWPCARE 6: 49% vs 26% reduction); cortical tuber resection for refractory focal seizures."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "~50% of TSC patients have ASD, primarily TSC2 mutations with early severe epilepsy; mTOR hyperactivation → excess synaptic protein translation → abnormal synaptogenesis; rapalogue reverses autism-like behaviors in TSC2+/− mice; ASD severity correlates with cortical tuber burden."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K→AKT→TSC2 phosphorylation is the canonical RTK-to-mTORC1 signal; TSC2 integrates PI3K/AKT, ERK, and AMPK inputs into mTORC1 control; PIK3CA activating mutations in sporadic tumors phenocopy TSC LOF for mTOR; PI3K + mTOR dual inhibitors studied in TSC tumor models."
---

# Tuberous Sclerosis Complex

## Overview

**Tuberous sclerosis complex (TSC)** is an autosomal dominant multisystem hamartoma syndrome caused by germline pathogenic variants in **TSC1** (hamartin; chromosome 9q34) or **TSC2** (tuberin; chromosome 16p13.3), which together form a GTPase-activating protein (GAP) complex that restrains **mTORC1** (mechanistic target of rapamycin complex 1) activity. Loss of TSC1 or TSC2 → Rheb-GTP → mTORC1 constitutively active → uncontrolled cell growth → hamartomas (benign tumor-like growths composed of disorganized but differentiated tissue) in multiple organ systems. TSC affects approximately 1 in 6,000 newborns worldwide (~50,000 patients in the USA) and is characterized by hamartomas in the **brain** (cortical tubers, subependymal nodules, SEGAs), **kidneys** (angiomyolipomas, cysts), **lungs** (LAM in women), **skin** (ash-leaf spots, angiofibromas, shagreen patches), **heart** (rhabdomyomas), and **eyes** (retinal hamartomas). Neurological manifestations — epilepsy (80-90% of TSC patients) and TSC-associated neuropsychiatric disorders (TAND) including autism spectrum disorder and intellectual disability — dominate morbidity. **Everolimus** (mTOR inhibitor) is FDA-approved for TSC-associated renal AML, SEGA, pulmonary LAM, and adjunctive epilepsy treatment [^crino-2006-tsc-review] [^northrup-2013-tsc-consensus].

**Epidemiology:**
- Prevalence: 1/6,000 live births; ~1.5-2 million patients worldwide; ~50,000 in the USA
- TSC1:TSC2 ratio: TSC1 germline ~33%, TSC2 germline ~67% (of patients with identifiable germline variant)
- De novo mutations: ~66-75% of TSC cases (no family history); high spontaneous mutation rate
- Mosaic TSC: ~15-20% of TSC patients without identifiable germline variant; somatic mosaicism (allele fraction 2-15%); milder phenotype; detected by sensitive NGS or analysis of multiple tissues
- Life expectancy: historically reduced; with modern management (anti-seizure + everolimus), approaching normal; major causes of death: renal hemorrhage from AML, status epilepticus, respiratory failure from LAM

**TSC diagnostic criteria (Northrup 2013):** [^northrup-2013-tsc-consensus]
Definite TSC: 2 major features OR 1 major + ≥2 minor features
- **Major features**: hypomelanotic macules (≥3, ≥5 mm), angiofibromas (≥3) or fibrous cephalic plaque, ungual fibromas (≥2), shagreen patch, multiple retinal hamartomas, cortical dysplasias (cortical tubers or white matter radial migration lines), subependymal nodule (SEN), SEGA, cardiac rhabdomyoma, lymphangioleiomyomatosis (LAM), angiomyolipoma (≥2)
- **Minor features**: "confetti" skin lesions, dental enamel pits (≥3), intraoral fibromas (≥2), retinal achromic patch, multiple renal cysts, nonrenal hamartomas
- **Pathognomonic**: TSC1 or TSC2 pathogenic variant = definite TSC regardless of clinical features

## Structure

### Molecular basis: TSC1-TSC2-Rheb-mTORC1 axis

**TSC1-TSC2 function:**
TSC1 (hamartin) stabilizes TSC2; TSC2 (tuberin) acts as GAP for Rheb → hydrolyzes Rheb-GTP → Rheb-GDP → mTORC1 inactive; germline TSC1 or TSC2 pathogenic variant → haploinsufficient state in all cells → somatic second hit in individual progenitor cells → biallelic TSC LOF → Rheb-GTP → mTORC1 constitutively active → hamartoma

**Upstream regulators of TSC1-TSC2:**
- **AKT** (activated by PI3K/RTK): phosphorylates TSC2 → INHIBITS TSC2 → mTOR ON (growth factor signal)
- **AMPK** (activated by energy depletion, STK11/LKB1): phosphorylates TSC2 → ACTIVATES TSC2 → mTOR OFF (energy stress signal)
- **ERK** (activated by RAS/MAPK): phosphorylates TSC2 → INHIBITS → mTOR ON (proliferative signal)

**mTORC1 consequences in TSC:**
S6K1 (ribosome biogenesis, cell size) + 4EBP1 (cap-dependent translation, HIF-1α, VEGF) + ULK1 inhibition (autophagy suppressed) → cell growth, proliferation, angiogenesis; in TSC cells: feedback loop — mTORC1 → S6K1 → IRS-1 phosphorylation (serine) → IRS-1 degradation → reduced PI3K/AKT input → lower AKT activity in TSC cells (paradoxical); this feedback explains why rapalogue withdrawal → rebound mTOR activity

### TSC manifestations by organ

**Brain:**
Cortical tubers: focal areas of cortical dysplasia with giant cells and dysmorphic neurons; present in ~90% of TSC patients; epileptogenic; number and location correlate with seizure severity and cognitive outcome; appear as T2-hyperintense cortical/subcortical lesions on MRI; calcification common; non-enhancing; histology: loss of cortical lamination, balloon cells (large dysmorphic neurons/astrocytes expressing vimentin)

Subependymal nodules (SENs): calcified nodules along ventricular walls; asymptomatic; appear in early childhood; distinguish from SEGA by lack of growth; "candle-dripping" appearance on MRI (FLAIR/T2 hypointense, calcified)

Subependymal giant cell astrocytoma (SEGA): low-grade astrocytic tumor (WHO Grade 1) arising from subependymal nodule at foramen of Monro; occurs in ~10-15% of TSC patients; progressive growth → obstructive hydrocephalus; may cause sudden neurological deterioration; contrast-enhancing on MRI (unlike SEN); usually age 5-20 years; treatment: everolimus or surgical resection

Radial migration lines (white matter hamartomata): T2-hyperintense subcortical bands extending from periventricular to cortical surface; not epileptogenic in isolation; marker of fetal migration abnormality in TSC

**Kidney:**
Angiomyolipoma (AML): benign hamartoma composed of abnormal blood vessels + smooth muscle + mature adipose tissue; present in ~80% of TSC patients; typically bilateral and multifocal; triphasic CT/MRI (fat, muscle, vascularity) is diagnostic; fat-poor AML may be mistaken for RCC; risk: hemorrhage (Wunderlich syndrome) → spontaneous retroperitoneal hemorrhage → life-threatening; hemorrhage risk increases with size (>3-4 cm) and aneurysm formation; treatment: prophylactic embolization or everolimus for large AML (>3 cm or growing)

TSC-associated RCC: <5% of TSC patients develop RCC; histology variable (clear cell, chromophobe, unclassified); often younger age; treated as sporadic RCC; everolimus may have activity

Renal cysts: ~30-50% of TSC patients; usually small; renal insufficiency rare; TSC2-PKD1 contiguous deletion → polycystic kidney disease

**Lung:**
Lymphangioleiomyomatosis (LAM): proliferation of TSC2-deficient smooth muscle-like cells (LAM cells) in lungs and lymphatics; occurs almost exclusively in women (~50-80% of TSC women); sporadic LAM also exists (only women; somatic TSC2 mutations); symptoms: dyspnea, recurrent pneumothorax (30-40%), chylothorax; HRCT: diffuse bilateral thin-walled cysts (2-5 mm) throughout both lungs; PFTs: obstructive pattern with air trapping; serum VEGF-D (>800 pg/mL): elevated in LAM → diagnostic biomarker; lymph node or pulmonary biopsy: LAM cells (HMB-45+, smooth muscle actin+, PR+); treatment: sirolimus (FDA-approved for LAM, 2015)

**Skin:**
- **Hypomelanotic macules (ash-leaf spots)**: most common TSC skin finding (>90%); present from birth; 5-20 mm depigmented macules (not true vitiligo — melanocytes present but defective); best seen under Wood's lamp (UV); diagnostic major feature
- **Angiofibromas**: malar distribution (butterfly-shaped); 2-5 mm red-pink papules; appear in childhood/adolescence; caused by TSC-deficient fibroblast proliferation + vascularization; treatment: laser (Nd:YAG, CO2), topical sirolimus (approved for facial angiofibromas in TSC, 2022)
- **Shagreen patch**: connective tissue nevus; thickened, orange-peel textured plaque; lumbosacral region; fibrous hamartoma
- **Fibrous cephalic plaque**: irregular fibrous plaque on forehead or scalp; firm, elevated; major diagnostic criterion
- **Ungual fibromas (Koenen tumors)**: periungual or subungual fibromas; appear at puberty; toenails more common than fingernails; painful; surgical removal or laser

**Heart:**
Cardiac rhabdomyomas: most common benign cardiac tumor in children; present in ~50-60% of fetuses/neonates with TSC2 mutations; frequently multiple; located in ventricular walls or septum; may cause outflow obstruction, arrhythmias, or hydrops fetalis; regress spontaneously with age (largely resolve by age 6-10 years without treatment); everolimus may accelerate regression (used in severe fetal/neonatal cases); echocardiography for all newborns with suspected TSC

**Eye:**
Retinal hamartomas (astrocytic hamartomas): flat or elevated white/yellowish lesions; present in ~40-50% of TSC; typically bilateral; calcified (mulberry lesion) or non-calcified (salmon-patch); usually asymptomatic; giant astrocytic hamartoma rarely causes visual impairment

## Function

### TSC-associated neuropsychiatric disorders (TAND)

**Epilepsy in TSC (80-90% of TSC patients):**
- Onset: typically <1 year of age (60% in first year); infantile spasms (IS) most common early presentation; untreated IS → hypsarrhythmia → West syndrome → developmental regression
- Seizure types: infantile spasms, focal seizures, tonic, atonic, absence, rarely GTC
- TSC2 mutations → more cortical tubers → more severe epilepsy than TSC1
- Treatment:
  - Vigabatrin (GABA transaminase inhibitor): first-line for TSC-associated infantile spasms; ORR ~70-80% for IS; visual field restriction toxicity (irreversible; requires visual field testing every 3-6 months)
  - ACTH: alternative first-line for IS (non-vigabatrin approach)
  - Everolimus adjunctive (EXIST-3): ≥50% seizure frequency reduction in 40% vs 22% placebo; approved adjunctive for focal-onset seizures in TSC ≥2 years
  - Cannabidiol (Epidiolex): FDA-approved for TSC-associated seizures (GWPCARE 6 trial: 49% seizure reduction vs 26% placebo); oral CBD solution; for patients ≥1 year
  - Surgical: resection of epileptogenic cortical tuber (identified by MEG, EEG dipole localization, stereoEEG); 50% seizure freedom in selected patients

**TSC-associated neuropsychiatric disorders (TAND):**
Autism spectrum disorder (ASD): ~50% of TSC patients; diagnosed primarily in those with TSC2 mutations and early severe epilepsy; mTOR hyperactivation → synaptic protein overexpression → abnormal synaptic plasticity → autism-related behaviors
Intellectual disability (ID): ~50% of TSC patients; primarily severe in TSC2, milder in TSC1; correlated with cortical tuber burden and seizure onset age
Neuropsychiatric: anxiety, depression, ADHD, OCD, sleep disorders — common in TSC
Behavioral: aggressive behaviors in non-verbal TSC patients with ID

## Pathology

### Diagnosis and surveillance

**Genetic testing:**
- TSC1 + TSC2 comprehensive sequencing + deletion analysis (MLPA): ~85-90% sensitivity in clinically diagnosed TSC; 10-15% remain genetically unsolved (somatic mosaicism, non-coding variants)
- TSC1 NM_000368 (9q34): 23 exons; TSC2 NM_000548 (16p13.3): 41 exons
- TSC2-PKD1 contiguous gene deletion: chromosome 16p13.3 deletion; severe early-onset PKD + TSC; diagnosed by chromosomal microarray

**Surveillance schedule (2012 Consensus/NCCN TSC):** [^northrup-2013-tsc-consensus]
- Brain MRI: every 1-3 years for SEGA (foramen of Monro); more frequently if prior rapid growth; non-enhancing SENs = observe; SEGA enhancing and growing = everolimus or surgery
- Abdominal MRI: every 1-3 years for renal AML and cysts; immediately if symptomatic
- Echocardiogram + EKG: at diagnosis; annually in children while rhabdomyomas present; adults as clinically indicated
- Pulmonary HRCT: at baseline (age 18 years for women; earlier if symptomatic); VEGF-D serum level; if LAM present: PFTs every 6-12 months
- Ophthalmology: at diagnosis; annually in children; as needed in adults
- Dermatology: at diagnosis; annually for new/growing lesions
- Neuropsychological assessment: at diagnosis; every 3 years or at educational transitions
- EEG: at diagnosis; as clinically indicated for seizure changes

### Treatment

**Renal AML:** [^crino-2006-tsc-review]
- AML <3 cm and asymptomatic: surveillance every 1-3 years; no intervention
- AML ≥3 cm or growing: preventive intervention
  - **Everolimus**: EXIST-2 Phase 3 (AML ≥3 cm): AML volume response 42% vs 0%; sustained responses; standard for TSC-associated AML; indefinite treatment (lesions regrow on discontinuation)
  - **Embolization** (selective arterial embolization): for acute hemorrhage (Wunderlich syndrome) or for growing AML in patients intolerant of everolimus; highly effective for hemorrhage control; tumor shrinkage temporary; re-embolization may be required
  - **Surgery**: reserved for isolated renal lesions when embolization fails or RCC cannot be excluded; nephron-sparing approach preferred

**SEGA:**
- Asymptomatic, small (≤1 cm), stable: MRI surveillance every 1-3 years
- Growing SEGA or symptomatic (obstructive hydrocephalus): treatment required
  - **Everolimus** (EXIST-1): 35% reduction in SEGA volume vs 0% placebo; prevents hydrocephalus progression; first-line for unresectable or bilateral SEGA; surgical risk reduction
  - **Surgical resection**: for SEGA with acute hydrocephalus requiring emergent drainage; craniotomy; complete resection preferred if surgically accessible; no adjuvant therapy needed for complete resection (tumor suppressor, no malignancy)
  - **CSF shunting**: ventriculoperitoneal shunt for hydrocephalus if surgery not immediately feasible; temporary measure

**Pulmonary LAM:**
- Sirolimus (rapamycin): MILES trial Phase 3: FEV1 stabilization during treatment (−12 mL/year sirolimus vs −134 mL/year placebo); FDA-approved for LAM (2015); regrowth after discontinuation; indefinite treatment in progressive LAM
- Bronchodilators: for symptomatic obstruction (20-40% of LAM patients respond)
- Pleurodesis: for recurrent pneumothorax (bilateral pleurodesis preferred in TSC-LAM to prevent recurrence on both sides)
- Lung transplantation: for end-stage respiratory failure; TSC-LAM does not recur in transplanted lung (LAM cells in circulation but require local mTOR activation to establish); acceptable outcomes

**Skin:**
- Topical sirolimus (0.1% cream or ointment): FDA-approved for facial angiofibromas in TSC (2022); applied daily; significant improvement in angiofibroma volume; well tolerated topically
- Laser: Nd:YAG or CO2 laser for angiofibromas; vascular IPL for erythema

**Prognosis:**
With modern management: life expectancy increasingly normal; major risks: renal AML hemorrhage (embolization/everolimus mitigates), LAM respiratory failure (sirolimus delays but not prevents), status epilepticus (antiseizure + vigabatrin), SEGA hydrocephalus (everolimus/surgery); intellectual disability and autism remain the dominant long-term challenges; ~40% of TSC patients have normal cognition and near-normal quality of life

## Connections

- `connects-to` → **[TSC1-TSC2](../../03-molecular/tsc1-tsc2/README.md)** — Germline TSC1 or TSC2 mutations cause TSC; TSC2 mutations more common (~2/3) and associated with more severe phenotype than TSC1; TSC1-TSC2 complex is the GTPase-activating protein for Rheb; TSC2 is phosphorylated by AKT and AMPK; somatic second hit required in each hamartoma
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — TSC1/TSC2 LOF → mTORC1 hyperactivation → S6K1/4EBP1 → hamartoma growth; everolimus FDA-approved for TSC-associated renal AML, SEGA, and pulmonary LAM; sirolimus used in TSC-LAM (off-label); mTOR inhibitor side effects: stomatitis, infections, hyperlipidemia
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK phosphorylates TSC2 Thr1462 → TSC1-TSC2 GTPase activated → Rheb inhibited → mTORC1 OFF; in TSC, this energy-sensing brake is removed → mTORC1 constitutively ON; AMPK activators (metformin) have theoretical benefit in TSC (downstream AMPK activation bypasses TSC2 LOF)
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — TSC-associated renal tumors: angiomyolipoma (AML; fat+muscle+vessels; embolization or everolimus) and rarely clear cell RCC; everolimus FDA-approved for AML >3 cm at risk of hemorrhage; TSC2 somatic mutation in sporadic RCC = mTOR-sensitive subset
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — TSC epilepsy affects 80-90% of patients; infantile spasms treated with vigabatrin (~70% ORR); everolimus adjunctive (EXIST-3: 40% vs 22% ≥50% seizure reduction); cannabidiol (Epidiolex; GWPCARE 6: 49% vs 26% reduction); cortical tuber resection for refractory focal seizures.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — ~50% of TSC patients have ASD, primarily TSC2 mutations with early severe epilepsy; mTOR hyperactivation → excess synaptic protein translation → abnormal synaptogenesis; rapalogue reverses autism-like behaviors in TSC2+/− mice; ASD severity correlates with cortical tuber burden.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K→AKT→TSC2 phosphorylation is the canonical RTK-to-mTORC1 signal; TSC2 integrates PI3K/AKT, ERK, and AMPK inputs into mTORC1 control; PIK3CA activating mutations in sporadic tumors phenocopy TSC LOF for mTOR; PI3K + mTOR dual inhibitors studied in TSC tumor models.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^crino-2006-tsc-review]: Crino PB, Nathanson KL, Henske EP. The tuberous sclerosis complex. *N Engl J Med.* 2006;355(13):1345-1356. [doi:10.1056/NEJMra055323](https://doi.org/10.1056/NEJMra055323) · [PubMed 17005952](https://pubmed.ncbi.nlm.nih.gov/17005952/)
[^northrup-2013-tsc-consensus]: Northrup H, Krueger DA. Tuberous sclerosis complex diagnostic criteria update: recommendations of the 2012 International Tuberous Sclerosis Complex Consensus Conference. *Pediatr Neurol.* 2013;49(4):243-254. [doi:10.1016/j.pediatrneurol.2013.08.001](https://doi.org/10.1016/j.pediatrneurol.2013.08.001) · [PubMed 24053982](https://pubmed.ncbi.nlm.nih.gov/24053982/)
