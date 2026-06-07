---
schema: human-scale-entry/v1
id: hereditary-diffuse-gastric-cancer
name: Hereditary Diffuse Gastric Cancer
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary diffuse gastric cancer (HDGC) is caused by germline CDH1 (~25%) or CTNNA1 (~2-5%) mutations; diffuse/signet ring histology; lifetime GC risk ~83% (CDH1 male); prophylactic gastrectomy is recommended; lobular breast cancer risk is elevated in CDH1/CTNNA1 carriers."
aliases: ["HDGC", "hereditary diffuse gastric cancer", "CDH1 gastric cancer", "CTNNA1 HDGC", "diffuse gastric cancer hereditary", "signet ring cell hereditary", "E-cadherin gastric cancer", "CDH1 prophylactic gastrectomy", "HDGC lobular breast cancer"]
sources:
  - id: van-der-post-2015-hdgc-guidelines
    type: peer-reviewed
    cite: "van der Post RS, Vogelaar IP, Carneiro F, et al. Hereditary diffuse gastric cancer: updated clinical guidelines with an emphasis on germline CDH1 mutation carriers. J Med Genet. 2015;52(6):361-374."
    doi: "10.1136/jmedgenet-2015-103094"
    pmid: "25979631"
    url: "https://doi.org/10.1136/jmedgenet-2015-103094"
  - id: hansford-2015-hdgc
    type: peer-reviewed
    cite: "Hansford S, Kaurah P, Li-Chang H, et al. Hereditary Diffuse Gastric Cancer Syndrome: CDH1 Mutations and Beyond. JAMA Oncol. 2015;1(1):23-32."
    doi: "10.1001/jamaoncol.2014.168"
    pmid: "26182300"
    url: "https://doi.org/10.1001/jamaoncol.2014.168"
cross_links:
  - target: 01-human/03-molecular/ctnna1
    relation: connects-to
    note: "Germline CTNNA1 LOF causes HDGC in CDH1-negative families (~2-5% of HDGC); prophylactic gastrectomy is recommended for pathogenic CTNNA1 carriers; penetrance estimated similar to CDH1; somatic CTNNA1 serves as the second hit in CDH1-germline HDGC tumors."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "Germline CDH1 pathogenic variants cause ~25-30% of HDGC; E-cadherin loss → diffuse signet ring cell carcinoma; prophylactic gastrectomy reveals T1a SRCC foci in ~90% of carriers; CDH1 also drives lobular breast cancer risk (~39-52% lifetime in female CDH1 carriers."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "HDGC is a hereditary form of diffuse-type gastric cancer (Lauren classification); signet ring cell histology; endoscopic surveillance is insufficient for SRCC → prophylactic gastrectomy preferred; CDH1/CTNNA1 germline accounts for ~1-3% of all GC globally."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Female CDH1 germline carriers have ~39-52% lifetime lobular breast cancer risk; CTNNA1 carriers also have elevated lobular BC risk; annual breast MRI from age 30 recommended; lobular BC in HDGC families is driven by E-cadherin/alpha-catenin pathway loss in breast epithelium."
---

# Hereditary Diffuse Gastric Cancer

## Overview

**Hereditary diffuse gastric cancer (HDGC)** is an autosomal dominant hereditary cancer predisposition syndrome defined by a predisposition to **diffuse-type gastric cancer (DGC)** — specifically the **signet ring cell carcinoma (SRCC)** histological subtype — and to **lobular breast carcinoma**. HDGC is caused by germline pathogenic variants in **CDH1** (E-cadherin; ~25-30% of HDGC probands) or **CTNNA1** (alpha-E-catenin; ~2-5%) or remains genetically uncharacterized in the majority of families meeting clinical criteria. CDH1 was established as the HDGC gene by Guilford et al. in 1998 in Māori families with clustering of diffuse gastric cancer; CTNNA1 was subsequently identified in CDH1-negative HDGC families by Majewski et al. in 2013. The HDGC germline prevalence is ~1 in 5,000-10,000 in populations with elevated gastric cancer background rates (East Asia, South America) and rarer in low-incidence populations [^van-der-post-2015-hdgc-guidelines] [^hansford-2015-hdgc].

**HDGC Clinical Criteria (IGCLC 2015, updated):**

Testing for CDH1 (and CTNNA1) is indicated in any of the following:
1. ≥2 cases of gastric cancer in family, any age, ≥1 confirmed diffuse type (or SRCC)
2. ≥1 case of diffuse gastric cancer at any age in a family with ≥1 case of lobular breast cancer (one diagnosed <50 years)
3. Individual diagnosed with diffuse gastric cancer at age <40 (no family history required)
4. Personal or family history of bilateral lobular breast cancer diagnosed <50 years
5. Personal history of SRCC in situ in otherwise healthy gastric mucosa

**Lifetime cancer risks by gene:**

| Cancer | CDH1 male | CDH1 female | CTNNA1 (estimated) |
|---|---|---|---|
| Diffuse gastric cancer | ~67-83% | ~56-83% | ~50-80% (limited data) |
| Lobular breast cancer | N/A | ~39-52% | Elevated (exact figure unclear) |
| Colorectal cancer | Modest elevation reported in some families | Same | Under investigation |

## Structure

### Genetic basis of HDGC

**CDH1 (E-cadherin; 16q22.1):**
- 16 exons; 882 aa; transmembrane cadherin; extracellular Ca²⁺-dependent homotypic adhesion; cytoplasmic tail binds CTNNB1 → CTNNA1 → F-actin
- Germline pathogenic variant spectrum: frameshift + nonsense (~25%), splice site (~20%), missense in EC domains (~20%), large deletions (~10%), promoter mutations (~5%), intronic variants with impact on splicing (~20%)
- Somatic second hit: LOH at 16q22 (CDH1 locus) in most HDGC tumor foci; methylation-driven silencing of the second CDH1 allele less common but described
- Phenotype: extremely high penetrance for diffuse GC (>80% by age 80 in white European HDGC families); lobular BC penetrance elevated in female carriers (~39-52% by age 80)
- Founder variants: Māori (c.1137G>A, p.=, exon 9 skipping); Northern Ireland and Newfoundland kindreds (specific splice and truncating variants)

**CTNNA1 (alpha-E-catenin; 5q31.2):**
- 9 exons encoding 906 aa; links CTNNB1-CDH1 complex to F-actin
- Germline pathogenic variant spectrum: frameshift, nonsense, splice site — LOF variants; missense variants of uncertain significance being classified
- Penetrance: estimated ~50-80% lifetime diffuse GC risk; data from smaller family cohorts than CDH1; prophylactic gastrectomies in CTNNA1 carriers reveal T1a SRCC foci confirming cancer susceptibility
- Lobular breast cancer elevation: biologically expected (same pathway as CDH1); clinical data accumulating from family registries

**Uncharacterized HDGC families (~65-70% of HDGC probands):**
- Despite meeting clinical criteria and negative CDH1/CTNNA1 testing, many HDGC families remain gene-negative
- Candidates: MAP3K6 (regulation of CDH1 expression; identified in some HDGC families); RhoA activating mutations (somatic in sporadic DGC but not established as germline HDGC genes); RHOA pathway genes; INSR; ongoing research
- Clinical management: same surveillance and prophylactic surgery recommendations as for CDH1/CTNNA1 variants in families with strong HDGC pedigrees

### Pathology — diffuse gastric cancer histology

**Lauren classification:**
- **Intestinal type** (~40% of GC): glandular; CDH1-retained; H. pylori → IM → dysplasia → adenocarcinoma; prevalent in East Asia; males > females
- **Diffuse type** (~35% of GC): signet ring cells and poorly cohesive carcinoma; CDH1/CTNNA1 lost; no glandular architecture; infiltrates stomach wall diffusely (linitis plastica in advanced cases)
- **Mixed type** (~15%)

**HDGC/SRCC histopathology:**
- Signet ring cell carcinoma: individual malignant cells with intracytoplasmic mucin vacuole displacing nucleus to periphery; no cell-cell adhesion (mimicking isolated cell invasion); linitis plastica when diffuse submucosal spread occurs
- In prophylactic gastrectomy specimens: multiple microscopic T1a SRCC foci (typically 2-100 foci) scattered throughout otherwise normal-appearing gastric mucosa; most common at the junction between gastric body and antrum (transition zone); atrophic mucosa, intestinal metaplasia, or dysplasia NOT present (HDGC lacks H. pylori pathway)
- Distinction from sporadic DGC: germline-driven HDGC has multifocal microscopic disease without pre-malignant mucosal changes; sporadic DGC may have H. pylori-associated atrophy in some cases

## Function

### Clinical management — HDGC

**Prophylactic total gastrectomy:**
- **Recommended for all CDH1 germline carriers** who have been adequately counseled; standard recommendation is gastrectomy between age 20-30 (after multidisciplinary counseling) or at an age 5-10 years before the earliest case in the family
- Evidence: ~90% of prophylactic gastrectomy specimens from CDH1 carriers contain at least one focus of T1a SRCC; this validates gastrectomy as life-saving even in asymptomatic carriers; most individuals who defer gastrectomy and develop advanced GC have stage III-IV disease due to insidious growth
- Surgical approach: total gastrectomy with Roux-en-Y esophagojejunostomy; D1+ or D2 lymphadenectomy; minimally invasive (laparoscopic) preferred at experienced centers
- Postoperative: dumping syndrome management (small meals, dietary modification); vitamin B12 IM supplementation (lifelong); iron, D, Ca²⁺ supplementation; nutritional counseling; weight management
- **CTNNA1 carriers**: prophylactic gastrectomy recommended following same CDH1 guidelines given equivalent penetrance estimates and confirmed SRCC foci in gastrectomy specimens

**Endoscopic surveillance (for carriers deferring gastrectomy):**
- Annual upper endoscopy with random biopsies from 6 sites (body, antrum, cardia/squamocolumnar junction) per Cambridge protocol
- Limitations: SRCC foci are submucous, pale, flat; easily missed on standard white-light endoscopy; magnification + narrow-band imaging + chromo-endoscopy (congo red + methylene blue) improve detection
- Consensus: endoscopic surveillance is **not equivalent to prophylactic gastrectomy** and should only be used for carriers who decline surgery or when surgery is contraindicated; not a substitute for gastrectomy
- Endoscopic surveillance schedule: annually from age 20 (or 5-10 years before earliest family case)

**Breast surveillance (female CDH1 and CTNNA1 carriers):**
- Lobular breast cancer elevated risk: CDH1 female carriers have ~39-52% lifetime risk; MRI is the primary modality (lobular BC is mammographically occult in ~30-40% of cases due to infiltrative growth pattern)
- Protocol: annual breast MRI ± mammography from age 30 (or 5-10 years before earliest family lobular BC)
- Risk-reducing options: bilateral prophylactic mastectomy (after gastrectomy); aromatase inhibitor or tamoxifen not validated specifically for CDH1-lobular BC prevention

**Genetic testing and counseling:**
- **Multigene panel recommended**: CDH1 + CTNNA1 + MAP3K6 ± other emerging genes
- Cascade testing: 50% offspring risk for CDH1/CTNNA1 pathogenic variants; first-degree relatives should undergo testing
- Prenatal/preimplantation: available for CDH1 pathogenic variants

## Pathology

### HDGC vs other hereditary GC syndromes

| Syndrome | Gene(s) | GC histology | GC risk | Other cancers |
|---|---|---|---|---|
| HDGC | CDH1, CTNNA1 | Diffuse/SRCC | ~67-83% (CDH1) | Lobular BC (CDH1 female ~50%) |
| Lynch syndrome | MLH1, MSH2, MSH6, PMS2 | Intestinal type | 5-13% | CRC, endometrial, ovarian |
| Hereditary intestinal GC | APC (FAP-associated), MUTYH | Intestinal | Moderate (in FAP context) | Colorectal polyps/cancer |
| Li-Fraumeni (TP53) | TP53 | Intestinal or diffuse | Slightly elevated | Sarcoma, breast, brain |
| Peutz-Jeghers (STK11) | STK11 | Intestinal | Elevated | GI polyps, sex cord tumors |
| Juvenile polyposis (SMAD4/BMPR1A) | SMAD4, BMPR1A | Intestinal | Elevated | Hamartomatous GI polyps |

**H. pylori and HDGC:**
- H. pylori is NOT the driver of CDH1/CTNNA1-germline HDGC (no H. pylori-associated IM or SPEM in prophylactic specimens); however, H. pylori eradication is still recommended as a general GC risk reduction measure in HDGC carriers, as co-infection may accelerate the somatic second hit
- Alcohol and smoking: may modify penetrance in HDGC (data limited); general risk reduction counseling appropriate

**Somatic CDH1 methylation in sporadic DGC:**
- ~50% of sporadic diffuse GC cases have somatic CDH1 promoter hypermethylation (epigenetic silencing of both alleles); this is distinct from germline mutation but produces identical loss of E-cadherin protein → same diffuse/SRCC histology; not hereditary
- HDGC vs sporadic DGC: IHC for E-cadherin protein (absent in both); germline testing required to distinguish

## Connections

- `connects-to` → **[CTNNA1](../../03-molecular/ctnna1/README.md)** — Germline CTNNA1 LOF causes HDGC in CDH1-negative families (~2-5% of HDGC); prophylactic gastrectomy is recommended for pathogenic CTNNA1 carriers; penetrance estimated similar to CDH1; somatic CTNNA1 serves as the second hit in CDH1-germline HDGC tumors.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Germline CDH1 pathogenic variants cause ~25-30% of HDGC; E-cadherin loss → diffuse signet ring cell carcinoma; prophylactic gastrectomy reveals T1a SRCC foci in ~90% of carriers; CDH1 also drives lobular breast cancer risk (~39-52% lifetime in female CDH1 carriers.
- `connects-to` → **[Gastric Cancer](../../07-system/gastric-cancer/README.md)** — HDGC is a hereditary form of diffuse-type gastric cancer (Lauren classification); signet ring cell histology; endoscopic surveillance is insufficient for SRCC → prophylactic gastrectomy preferred; CDH1/CTNNA1 germline accounts for ~1-3% of all GC globally.
- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — Female CDH1 germline carriers have ~39-52% lifetime lobular breast cancer risk; CTNNA1 carriers also have elevated lobular BC risk; annual breast MRI from age 30 recommended; lobular BC in HDGC families is driven by E-cadherin/alpha-catenin pathway loss in breast epithelium.

[^van-der-post-2015-hdgc-guidelines]: van der Post RS, Vogelaar IP, Carneiro F, et al. Hereditary diffuse gastric cancer: updated clinical guidelines with an emphasis on germline CDH1 mutation carriers. *J Med Genet.* 2015;52(6):361-374. [doi:10.1136/jmedgenet-2015-103094](https://doi.org/10.1136/jmedgenet-2015-103094) · [PubMed 25979631](https://pubmed.ncbi.nlm.nih.gov/25979631/)
[^hansford-2015-hdgc]: Hansford S, Kaurah P, Li-Chang H, et al. Hereditary Diffuse Gastric Cancer Syndrome: CDH1 Mutations and Beyond. *JAMA Oncol.* 2015;1(1):23-32. [doi:10.1001/jamaoncol.2014.168](https://doi.org/10.1001/jamaoncol.2014.168) · [PubMed 26182300](https://pubmed.ncbi.nlm.nih.gov/26182300/)
