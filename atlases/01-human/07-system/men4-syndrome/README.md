---
schema: human-scale-entry/v1
id: men4-syndrome
name: MEN4 Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Multiple Endocrine Neoplasia type 4 (MEN4) is caused by germline CDKN1B (p27KIP1) mutations; pituitary adenomas, parathyroid tumors, and pancreatic NETs similar to MEN1 but driven by CDK inhibitor LOF; annual biochemical and MRI surveillance; rarer than MEN1."
aliases: ["MEN4", "multiple endocrine neoplasia type 4", "MEN4 syndrome", "CDKN1B MEN4", "p27KIP1 syndrome", "MEN4 pituitary", "MEN4 parathyroid", "CDKN1B multiple endocrine neoplasia", "MEN4 CDKN1B germline"]
sources:
  - id: alrezk-2017-men4
    type: peer-reviewed
    cite: "Alrezk R, Hannah-Shmouni F, Stratakis CA. MEN4 and CDKN1B mutations: the latest of the MEN syndromes. Endocr Relat Cancer. 2017;24(10):T195-T208."
    doi: "10.1530/ERC-17-0243"
    pmid: "28894007"
    url: "https://doi.org/10.1530/ERC-17-0243"
  - id: pellegata-2006-cdkn1b-men4
    type: peer-reviewed
    cite: "Pellegata NS, Quintanilla-Martinez L, Siggelkow H, et al. Germ-line mutations in p27Kip1 cause a multiple endocrine neoplasia syndrome in rats and humans. Proc Natl Acad Sci USA. 2006;103(42):15558-15563."
    doi: "10.1073/pnas.0603306103"
    pmid: "17030811"
    url: "https://doi.org/10.1073/pnas.0603306103"
cross_links:
  - target: 01-human/03-molecular/cdkn1b
    relation: connects-to
    note: "CDKN1B (p27KIP1) LOF → CDK2-CyclinE derepressed at G1/S → neuroendocrine cell proliferation; p27 nuclear expression is prognostic in sporadic pNETs (low nuclear p27 = poor prognosis); SKP2-mediated p27 proteolysis is a druggable target in cancer; germline = MEN4."
  - target: 01-human/03-molecular/men1
    relation: connects-to
    note: "Menin (MEN1) regulates CDKN1B expression via H3K4me3 at the CDKN1B promoter; both MEN1 and CDKN1B are tumor suppressors in pituitary/parathyroid/pNET lineages; MEN4 tumors may show secondary CDKN1B loss; MEN1 negative MEN families should receive CDKN1B testing."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "MEN4 has an overlapping tumor spectrum with MEN1 (pituitary, parathyroid, pNETs); key differences: MEN4 is rarer; less frequent gastrinoma/ZES; no known skin features; CDKN1B germline LOF mechanism is distinct from menin LOF; combined MEN1+CDKN1B testing recommended."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "MEN4-associated pNETs and pituitary adenomas are driven by CDK2-CyclinE derepression due to CDKN1B LOF; p27 IHC loss in pNETs is a prognostic biomarker; CDK4/6 inhibitors (palbociclib, ribociclib) in SSTR-refractory pNETs target the same CDK cell cycle axis."
---

# MEN4 Syndrome

## Overview

**Multiple Endocrine Neoplasia type 4 (MEN4)** is a rare autosomal dominant hereditary endocrine tumor predisposition syndrome caused by germline pathogenic variants in **CDKN1B** (cyclin-dependent kinase inhibitor 1B; encodes p27KIP1). MEN4 was established as a distinct clinical entity following the identification of homozygous *Cdkn1b* mutations in the MENX rat model of multiple endocrine neoplasia by Pellegata et al. in 2006, with subsequent identification of heterozygous CDKN1B mutations in MEN1-negative human patients with the MEN clinical phenotype. MEN4 is formally recognized by **WHO 2022** Classification of Endocrine and Neuroendocrine Tumors as a category distinct from MEN1, MEN2, and MEN3. The clinical syndrome resembles MEN1 in its major tumor types (pituitary adenomas, primary hyperparathyroidism, pancreatic NETs) but results from CDK inhibitor LOF (loss of p27-mediated G1/S arrest) rather than epigenetic scaffold dysfunction (menin). MEN4 is approximately **1/100 as prevalent as MEN1**, with fewer than 100 well-documented cases in the literature as of 2025 [^pellegata-2006-cdkn1b-men4] [^alrezk-2017-men4].

**MEN4 vs. MEN1 vs. MEN2A comparison:**

| Feature | MEN4 (CDKN1B) | MEN1 (MEN1) | MEN2A (RET) |
|---|---|---|---|
| Gene | CDKN1B (12p13.1) | MEN1 (11q13.1) | RET (10q11.21) |
| Mechanism | CDK inhibitor LOF | Epigenetic scaffold LOF | Receptor tyrosine kinase GOF |
| Prevalence | 1/10,000,000 (est.) | 1/20,000-30,000 | 1/35,000 |
| Parathyroid | Primary hyperparathyroidism | >95% | ~20-30% (2A only) |
| Pituitary | ~60% (all subtypes) | ~20-65% | Not characteristic |
| Pancreatic NETs | ~15-35% | ~30-80% | Not characteristic |
| MTC | No | No | ~100% (2A carriers) |
| Pheochromocytoma | Rare | Rare | ~50% (2A) |
| Gastrinoma/ZES | Rare reports | Common (~25-40%) | No |

## Structure

### Genetic basis of MEN4

**CDKN1B gene (12p13.1):**
- 3 exons (2 coding); 198 aa; 27 kDa; ubiquitously expressed with highest levels in post-mitotic and quiescent cells
- Germline pathogenic variant spectrum: frameshift/nonsense (~55%), missense in CDK inhibitory domain (~25%), splice site (~10%), 5'UTR variants altering Kozak context or translation initiation (~10%)
- Haploinsufficiency mechanism: single functional allele → reduced p27 dosage → insufficient CDK2 inhibition → neuroendocrine progenitor cell proliferation → tumor formation
- Complete CDKN1B biallelic loss: not observed in germline (homozygous LOF lethal embryonically in mice); only heterozygous germline → MEN4; somatic second hit (LOH at 12p13) may occur in tumor tissue
- Penetrance: incompletely defined (rare syndrome); estimated >50% by age 60 for at least one MEN4 manifestation; pituitary adenomas appear most penetrant

**Where to suspect CDKN1B germline testing:**
1. MEN1-negative patient with at least 2 typical MEN1 tumor types (pituitary + parathyroid, or pituitary + pNET, etc.)
2. Young-onset primary hyperparathyroidism + pituitary adenoma
3. Multiglandular primary hyperparathyroidism without MEN1 mutation
4. Family history of MEN clinical phenotype with negative MEN1 testing

Recommended testing approach: multigene panel (MEN1 + CDKN1B + other MEN genes) when clinical suspicion; CDKN1B sequencing + MLPA for deletions.

### CDKN1B molecular mechanism in MEN4

p27KIP1 haploinsufficiency → insufficient CDK2-CyclinE inhibition → premature cell cycle entry in:
- Pituitary somatotrophs → GH-secreting adenoma (acromegaly)
- Pituitary corticotrophs → ACTH-secreting adenoma (Cushing disease)
- Pituitary lactotrophs → prolactinoma
- Parathyroid chief cells → chief cell hyperplasia / adenoma → PTH-mediated hypercalcemia
- Pancreatic islet β-cells / δ-cells / α-cells → pNET

The MEN1-p27 axis: Menin (MEN1 protein) regulates CDKN1B transcription via H3K4me3 deposition at the CDKN1B promoter. MEN1 LOF → reduced CDKN1B expression → p27 falls → CDK2 derepressed → neuroendocrine proliferation. This makes p27 a **downstream effector** of menin in the same pathway, explaining the overlapping tumor spectrum of MEN1 and MEN4 despite different gene mutations.

## Function

### Clinical manifestations of MEN4

**Pituitary adenomas (~60% of MEN4 patients):**
- All subtypes reported: prolactinoma (most common in some series), GH-secreting (acromegaly), ACTH-secreting (Cushing disease), non-functioning
- Treatment: same as sporadic pituitary adenoma — dopamine agonists (prolactinoma); transsphenoidal surgery; somatostatin receptor ligands (GH adenoma); radiotherapy for residual/refractory
- MEN4 pituitary adenoma may be more aggressive than sporadic adenomas (biallelic CDK inhibitor LOF in pituitary progenitors); surveillance brain MRI every 3-5 years

**Primary hyperparathyroidism (PHPT; ~60-80% of MEN4 patients):**
- Multiglandular (chief cell hyperplasia → multigland disease) or single adenoma
- Presentation: hypercalcemia, elevated PTH, nephrolithiasis, bone loss (osteoporosis)
- Annual Ca, PTH, 24h urine calcium; neck ultrasound every 2-3 years
- Surgical management: 3.5-gland parathyroidectomy (similar to MEN1-PHPT) given multiglandular risk; intraoperative PTH monitoring

**Pancreatic NETs (~15-35% of MEN4 patients):**
- Functional (gastrinoma, insulinoma) or non-functional; similar to MEN1-pNETs but gastrinoma/ZES appears less frequent in MEN4 vs MEN1
- Surveillance: annual plasma chromogranin A, fasting glucose/insulin, gastrin (if symptoms); annual abdominal MRI ± EUS
- Management: similar to MEN1-pNETs; somatostatin analogs (octreotide/lanreotide); targeted therapy (everolimus, sunitinib) for advanced/metastatic; surgical resection for localized

**Other MEN4 features (rarer):**
- Adrenal tumors: some cases reported; adrenal CT annually
- Carcinoid tumors: bronchial, gastric; more data needed
- Renal angiomyolipoma: rare case reports; unclear if true MEN4 association
- Cervical cancer: limited data; may represent background incidence

**Features NOT characteristic of MEN4 (unlike MEN1):**
- Medullary thyroid cancer (MTC): not part of MEN4 (MTC is MEN2/RET)
- Cutaneous lipomas, angiofibromas, collagenomas: MEN1 skin features not described in MEN4
- Gastrinoma/ZES: rare in MEN4 vs. 25-40% in MEN1

## Pathology

### Surveillance and management

**Annual biochemical screening (from age 20, or 5-10 years before youngest affected family member):**
- Serum calcium, PTH → parathyroid
- Prolactin, IGF-1 (acromegaly), ACTH/cortisol (Cushing) → pituitary
- Chromogranin A, fasting glucose, insulin, gastrin (if symptoms), glucagon → pNETs
- 24h urine catecholamines/metanephrines → pheochromocytoma (uncommon but reported)

**Imaging:**
- Brain MRI (pituitary protocol): at diagnosis; every 3-5 years if no adenoma; more frequent if symptoms
- Abdominal MRI or CT: annually; pancreatic lesions ≥1 cm → surgery or close follow-up
- Neck ultrasound: every 2-3 years for parathyroid

**Genetic counseling:**
- Autosomal dominant; 50% offspring risk
- Testing of at-risk relatives from childhood (biochemical) and genetically from adolescence
- Prenatal/PGT-M testing available

### Multigene panel testing strategy for MEN syndromes

When clinical MEN features are present:
1. **First test**: MEN1 sequencing + MLPA (identifies ~70-80% of MEN1 syndrome)
2. **If MEN1 negative**: multigene panel including CDKN1B (MEN4), RET (MEN2), CDKN2B, CDKN2C, AIP (pituitary adenoma predisposition), MAX (pheochromocytoma)
3. **Pituitary adenoma isolated**: AIP (aryl hydrocarbon receptor-interacting protein) mutations cause familial isolated pituitary adenoma (FIPA), especially GH-secreting; distinct from MEN4
4. **Parathyroid alone**: germline HRPT2/CDC73 mutations (hyperparathyroidism-jaw tumor syndrome); CASR variants (FHH)

## Connections

- `connects-to` → **[CDKN1B](../../03-molecular/cdkn1b/README.md)** — CDKN1B (p27KIP1) LOF → CDK2-CyclinE derepressed at G1/S → neuroendocrine cell proliferation; p27 nuclear expression is prognostic in sporadic pNETs (low nuclear p27 = poor prognosis); SKP2-mediated p27 proteolysis is a druggable target in cancer; germline = MEN4.
- `connects-to` → **[MEN1](../../03-molecular/men1/README.md)** — Menin (MEN1) regulates CDKN1B expression via H3K4me3 at the CDKN1B promoter; both MEN1 and CDKN1B are tumor suppressors in pituitary/parathyroid/pNET lineages; MEN4 tumors may show secondary CDKN1B loss; MEN1 negative MEN families should receive CDKN1B testing.
- `connects-to` → **[MEN1 Syndrome](../../07-system/men1-syndrome/README.md)** — MEN4 has an overlapping tumor spectrum with MEN1 (pituitary, parathyroid, pNETs); key differences: MEN4 is rarer; less frequent gastrinoma/ZES; no known skin features; CDKN1B germline LOF mechanism is distinct from menin LOF; combined MEN1+CDKN1B testing recommended.
- `connects-to` → **[Neuroendocrine Tumors](../../07-system/neuroendocrine-tumors/README.md)** — MEN4-associated pNETs and pituitary adenomas are driven by CDK2-CyclinE derepression due to CDKN1B LOF; p27 IHC loss in pNETs is a prognostic biomarker; CDK4/6 inhibitors (palbociclib, ribociclib) in SSTR-refractory pNETs target the same CDK cell cycle axis.

[^alrezk-2017-men4]: Alrezk R, Hannah-Shmouni F, Stratakis CA. MEN4 and CDKN1B mutations: the latest of the MEN syndromes. *Endocr Relat Cancer.* 2017;24(10):T195-T208. [doi:10.1530/ERC-17-0243](https://doi.org/10.1530/ERC-17-0243) · [PubMed 28894007](https://pubmed.ncbi.nlm.nih.gov/28894007/)
[^pellegata-2006-cdkn1b-men4]: Pellegata NS, Quintanilla-Martinez L, Siggelkow H, et al. Germ-line mutations in p27Kip1 cause a multiple endocrine neoplasia syndrome in rats and humans. *Proc Natl Acad Sci USA.* 2006;103(42):15558-15563. [doi:10.1073/pnas.0603306103](https://doi.org/10.1073/pnas.0603306103) · [PubMed 17030811](https://pubmed.ncbi.nlm.nih.gov/17030811/)
