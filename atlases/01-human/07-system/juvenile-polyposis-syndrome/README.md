---
schema: human-scale-entry/v1
id: juvenile-polyposis-syndrome
name: Juvenile Polyposis Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Juvenile polyposis syndrome (JPS) is caused by germline SMAD4 (~20%) or BMPR1A (~25%) mutations; hamartomatous GI polyps with CRC risk ~40-50% by age 60; SMAD4-JPS patients also have hereditary hemorrhagic telangiectasia features; colonoscopy from age 15."
aliases: ["juvenile polyposis syndrome", "JPS", "SMAD4 JPS", "BMPR1A JPS", "hamartomatous polyposis", "juvenile polyps GI", "JPS CRC risk", "JPS HHT overlap", "hereditary juvenile polyposis"]
sources:
  - id: howe-1998-smad4-jps
    type: peer-reviewed
    cite: "Howe JR, Roth S, Ringold JC, et al. Mutations in the SMAD4/DPC4 gene in juvenile polyposis. Science. 1998;280(5366):1086-1088."
    doi: "10.1126/science.280.5366.1086"
    pmid: "9582123"
    url: "https://doi.org/10.1126/science.280.5366.1086"
  - id: aretz-2007-jps-spectrum
    type: peer-reviewed
    cite: "Aretz S, Stienen D, Uhlhaas S, et al. High proportion of large genomic deletions and a genotype-phenotype update in 80 unrelated families with juvenile polyposis syndrome. J Med Genet. 2007;44(11):702-709."
    doi: "10.1136/jmg.2007.051839"
    pmid: "17601924"
    url: "https://doi.org/10.1136/jmg.2007.051839"
cross_links:
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Germline SMAD4 loss causes ~20% of JPS; SMAD4-JPS has larger, more numerous polyps, earlier CRC onset, and concurrent HHT features (pulmonary/cerebral AVMs, telangiectasias) requiring vascular surveillance beyond standard JPS protocol."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "JPS polyps arise from TGF-β/BMP pathway disruption (SMAD4 or BMPR1A LOF) → stromal hamartomatous growth; wild-type epithelium overgrows abnormal stroma; TGF-β loss promotes adenomatous transformation within JPS polyps → elevated CRC risk."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "JPS confers ~40-50% lifetime CRC risk by age 60 (vs ~5% population risk); CRC arises from adenomatous foci within JPS hamartomas; SMAD4-JPS has the highest CRC risk; annual colonoscopy from age 15 with polypectomy; colectomy if polyp burden unmanageable."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "JPS hamartomas differ from FAP (APC-mutant) adenomas: hamartomas have a complex stroma with muscle fibers and cysts (not pure epithelial dysplasia); however, adenomatous foci within JPS polyps carry CRC risk; colonoscopic polypectomy controls burden in both syndromes."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN ties JPS to the overlapping hamartoma syndromes: contiguous 10q22-23 deletions can remove both BMPR1A and PTEN → a severe combined JPS/Cowden phenotype, and the BMP→SMAD4→PTEN→mTOR axis is the rationale for rapamycin chemoprevention being explored in JPS."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Peutz-Jeghers is the main hamartomatous-polyposis differential: STK11-driven polyps have an arborizing smooth-muscle core (vs JPS's edematous, cyst-rich juvenile stroma) plus mucocutaneous melanotic macules absent in JPS; both carry high GI cancer risk via different pathways."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "JPS studs the colorectum with hamartomatous polyps (5-200) from which adenomatous foci drive a ~40-50% lifetime colorectal cancer risk; annual colonoscopy with polypectomy from age 15 controls burden, and colectomy is indicated when polyps become unmanageable."
---

# Juvenile Polyposis Syndrome

## Overview

**Juvenile polyposis syndrome (JPS)** is an autosomal dominant hereditary gastrointestinal polyposis syndrome characterized by multiple hamartomatous polyps of the colon, rectum, stomach, and small intestine, with a significantly elevated risk of colorectal and gastric cancers. JPS affects approximately **1 in 100,000-160,000** individuals and is caused by germline pathogenic variants in **SMAD4** (~20%), **BMPR1A** (~25%), or as yet unidentified genes (~55%) [^howe-1998-smad4-jps] [^aretz-2007-jps-spectrum]. The term "juvenile" refers to the characteristic **juvenile polyp histology** (edematous stroma, dilated mucus-filled glands, inflammatory infiltrate, surface erosion) — not to patient age at onset, though onset in childhood is common. JPS is distinct from Peutz-Jeghers syndrome (STK11-driven hamartomas with arborizing smooth muscle core) and Cowden syndrome (PTEN-driven; trichilemmomal cysts, macrocephaly, breast/thyroid risk).

**JPS compared to other hamartomatous polyposis syndromes:**

| Feature | JPS | Peutz-Jeghers (PJS) | Cowden (CS) |
|---|---|---|---|
| Gene(s) | SMAD4, BMPR1A | STK11 | PTEN |
| Polyp histology | Juvenile (edematous stroma) | Hamartoma with arborizing smooth muscle | Hamartoma (variable) |
| GI distribution | Colon > stomach > SI | Small intestine > colon > stomach | Colon, stomach, esophagus |
| Melanotic macules | Absent | Present (lips, buccal, digits) | Absent |
| Skin lesions | Rare | None | Trichilemmoma, keratoses |
| CRC lifetime risk | ~40-50% | ~39% | ~9-18% |
| HHT overlap | SMAD4-JPS only | Absent | Absent |
| Pathway | TGF-β/BMP (SMAD) | LKB1/AMPK/mTOR | PI3K/AKT/mTOR |

## Structure

### Diagnostic criteria for JPS

Clinical diagnosis requires **one or more** of:
1. **≥5 juvenile polyps** in the colorectum
2. **Juvenile polyps throughout the GI tract** (colon + stomach/small bowel)
3. **Any number of juvenile polyps** with a family history of JPS

Juvenile polyp histology: pedunculated or sessile; smooth rounded surface; edematous lamina propria with inflammatory cells (eosinophils, plasma cells, neutrophils); dilated mucus-filled crypts (retention cysts); surface erosion and granulation tissue; no smooth muscle core (distinguishes from PJS hamartoma)

JPS differs from a **solitary juvenile polyp** (common in children 2-5 years, ~1% of children; benign, no increased cancer risk; >1 polyp raises JPS concern; ≥5 polyps = likely JPS).

### Genetic subtypes

**SMAD4-JPS (~20%):**
- Germline SMAD4 pathogenic variants (missense, truncating, splice, large deletions — MLPA required)
- **SMAD4-HHT overlap syndrome**: JPS + hereditary hemorrhagic telangiectasia (HHT) phenotype
  - Telangiectasias: mucocutaneous (lips, tongue, fingertips), GI (epistaxis, GI bleeding)
  - Pulmonary AVMs: right-to-left shunt → paradoxical embolism → stroke, brain abscess
  - Hepatic AVMs: high-output cardiac failure in severe cases
  - Cerebral AVMs: hemorrhagic stroke risk
  - Nasal epistaxis (recurrent): most common early symptom
- SMAD4-JPS polyps: often larger, more numerous, pancolonic; earlier onset of CRC; higher density gastric juvenile polyposis
- Screening: cardiac echo (bubble study) + chest CT + brain MRI for AVM detection at diagnosis

**BMPR1A-JPS (~25%):**
- Germline BMPR1A pathogenic variants (BMP type I receptor; chromosome 10q22-q23)
- No HHT features
- Pure polyposis phenotype; some overlap with Cowden-like features (macrocephaly, PTEN-like features in a few families)
- Large genomic deletions of BMPR1A (up to entire gene) detected by MLPA; ~30% of BMPR1A pathogenic variants are large deletions
- Overlapping 10q deletion: contiguous deletions of BMPR1A + PTEN have been reported → more severe phenotype (Cowden + JPS features)

**Unknown genetic cause (~55%):**
- May include: PTEN variants (overlap with Cowden), BMPR1A large deletions missed by sequencing, BMPR2 variants, somatic mosaic SMAD4/BMPR1A mutations, or as-yet-unidentified genes
- No pathogenic variant found on clinical germline testing does not exclude JPS clinically

### GI polyposis distribution

- **Colorectal polyps**: present in virtually all JPS patients; polyp count 5-200 (variable); colon is most common site
- **Gastric juvenile polyposis (GJP)**: ~15-30% of JPS patients; diffuse fundic gland polyposis + juvenile polyp histology; higher in SMAD4-JPS; protein-losing enteropathy, hypoalbuminemia, edema
- **Small bowel polyps**: 10-15%; usually fewer; small bowel capsule endoscopy for detection
- **Duodenal polyps**: 10-15%; Spigelman staging not established for JPS (unlike FAP)
- **Rectal sparing**: uncommon; rectum usually involved

## Function

### Disease mechanism: stromal-epithelial BMP signaling disruption

JPS hamartomas arise from disrupted **BMP/SMAD signaling in the intestinal stroma**. In normal intestine:
- Mesenchymal cells secrete BMP2/4/7 → bind BMPR1A/BMPR2 on epithelial crypt cells → SMAD1/5/8 phosphorylation → SMAD4 complex → p21/Notch suppression → stem cell quiescence
- BMP gradient: high at crypt-villus boundary (suppresses proliferation), low at crypt base (allows stem cell cycling)

In JPS (SMAD4 or BMPR1A LOF in epithelium):
- BMP signals cannot be transduced → epithelial SMAD1/5/8-SMAD4 complex non-functional → loss of BMP anti-proliferative output → crypt cell proliferation + polyp formation
- Stromal component: edematous stromal expansion (inflammatory infiltrate, granulation tissue) — the "hamartoma" stroma — is thought to result from aberrant paracrine signaling between dysregulated epithelium and mesenchyme
- Adenomatous foci within JPS polyps: where biallelic SMAD4/BMPR1A LOH occurs → loss of remaining allele → adenoma-carcinoma sequence can proceed → CRC risk

### Cancer risk

**Colorectal cancer (CRC):**
- Lifetime CRC risk: ~40-50% by age 60 (vs ~5% population); may reach 68% in some series by age 70
- CRC arises predominantly from adenomatous transformation within JPS polyps, not de novo
- SMAD4-JPS: higher CRC risk than BMPR1A-JPS
- Median age of CRC diagnosis: ~37-44 years in JPS (vs ~72 years for sporadic CRC)

**Gastric cancer:**
- Risk: ~15-21% lifetime; particularly in SMAD4-JPS with diffuse gastric polyposis
- Gastric cancer surveillance: upper endoscopy every 1-2 years

**Small bowel and duodenal cancer:**
- Risk elevated but rare; small bowel surveillance with capsule endoscopy

**Pancreatic cancer:**
- Some families with SMAD4-JPS report elevated pancreatic cancer risk (SMAD4 is also a major PDAC driver); formal risk quantification limited by small series

## Pathology

### Surveillance recommendations

**Genetic testing:**
- Germline SMAD4 and BMPR1A sequencing + large deletion analysis (MLPA)
- Predictive testing of at-risk relatives after age 15 (onset of endoscopy surveillance)
- Testing of all first-degree relatives if pathogenic variant identified

**Endoscopic surveillance:**
- **Colonoscopy**: from age 15 (or when diagnosis suspected); annually if polyps present; every 2-3 years if no polyps
- **Upper endoscopy (EGD)**: from age 15; annually if gastric polyps present; every 2-3 years if clean
- **Small bowel capsule endoscopy**: every 2-3 years if small bowel polyps

**SMAD4-specific vascular surveillance (HHT overlap):**
- Transthoracic echocardiogram with bubble study (TTCE): screen for pulmonary AVM at diagnosis
- If TTCE positive → CT pulmonary angiogram → transcatheter embolization of pulmonary AVMs >3 mm
- Brain MRI (gadolinium): screen for cerebral AVM at diagnosis; repeat every 5 years
- Annual CBC (anemia from GI/epistaxis blood loss); iron supplementation

**Surgical management:**
- **Colectomy with ileorectal anastomosis (IRA)**: for unmanageable polyp burden; ileal pouch-anal anastomosis (IPAA) if rectum involved; prophylactic surgery generally at age 15-25 when polyp count becomes unmanageable (>50-100 polyps)
- **Total/subtotal gastrectomy**: for severe gastric polyposis with protein-losing enteropathy or unresectable polyps; nutritional reconstruction after gastrectomy in young patients
- **Appendectomy**: at time of colectomy; appendiceal juvenile polyps reported

### Medical management

No approved chemopreventive agents specifically for JPS. Options under investigation or used off-label:
- **COX-2 inhibitors (celecoxib)**: rationale from FAP data; reduces polyp formation in animal models of Smad4-deficient polyposis; no Phase 3 JPS data
- **Rapamycin/mTOR inhibitors**: rationale from BMPR1A-JPS (BMP → SMAD4 → PTEN → mTOR pathway); pre-clinical data; no clinical trials
- **Bevacizumab**: used in SMAD4-HHT for severe GI telangiectasia bleeding and pulmonary AVMs unresponsive to embolization; off-label; reduces bleeding frequency

## Connections

- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Germline SMAD4 loss causes ~20% of JPS; SMAD4-JPS has larger, more numerous polyps, earlier CRC onset, and concurrent HHT features (pulmonary/cerebral AVMs, telangiectasias) requiring vascular surveillance beyond standard JPS protocol.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — JPS polyps arise from TGF-β/BMP pathway disruption (SMAD4 or BMPR1A LOF) → stromal hamartomatous growth; wild-type epithelium overgrows abnormal stroma; TGF-β loss promotes adenomatous transformation within JPS polyps → elevated CRC risk.
- `connects-to` → **[Colorectal Cancer](../../07-system/colorectal-cancer/README.md)** — JPS confers ~40-50% lifetime CRC risk by age 60 (vs ~5% population risk); CRC arises from adenomatous foci within JPS hamartomas; SMAD4-JPS has the highest CRC risk; annual colonoscopy from age 15 with polypectomy; colectomy if polyp burden unmanageable.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — JPS hamartomas differ from FAP (APC-mutant) adenomas: hamartomas have a complex stroma with muscle fibers and cysts (not pure epithelial dysplasia); however, adenomatous foci within JPS polyps carry CRC risk; colonoscopic polypectomy controls burden in both syndromes.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN ties JPS to the overlapping hamartoma syndromes: contiguous 10q22-23 deletions can remove both BMPR1A and PTEN → a severe combined JPS/Cowden phenotype, and the BMP→SMAD4→PTEN→mTOR axis is the rationale for rapamycin chemoprevention being explored in JPS.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Peutz-Jeghers is the main hamartomatous-polyposis differential: STK11-driven polyps have an arborizing smooth-muscle core (vs JPS's edematous, cyst-rich juvenile stroma) plus mucocutaneous melanotic macules absent in JPS; both carry high GI cancer risk via different pathways.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — JPS studs the colorectum with hamartomatous polyps (5-200) from which adenomatous foci drive a ~40-50% lifetime colorectal cancer risk; annual colonoscopy with polypectomy from age 15 controls burden, and colectomy is indicated when polyps become unmanageable.

[^howe-1998-smad4-jps]: Howe JR, Roth S, Ringold JC, et al. Mutations in the SMAD4/DPC4 gene in juvenile polyposis. *Science.* 1998;280(5366):1086-1088. [doi:10.1126/science.280.5366.1086](https://doi.org/10.1126/science.280.5366.1086) · [PubMed 9582123](https://pubmed.ncbi.nlm.nih.gov/9582123/)
[^aretz-2007-jps-spectrum]: Aretz S, Stienen D, Uhlhaas S, et al. High proportion of large genomic deletions and a genotype-phenotype update in 80 unrelated families with juvenile polyposis syndrome. *J Med Genet.* 2007;44(11):702-709. [doi:10.1136/jmg.2007.051839](https://doi.org/10.1136/jmg.2007.051839) · [PubMed 17601924](https://pubmed.ncbi.nlm.nih.gov/17601924/)
