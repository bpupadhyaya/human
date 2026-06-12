---
schema: human-scale-entry/v1
id: noonan-syndrome
name: Noonan Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Noonan syndrome is caused by germline RAS-MAPK pathway mutations (PTPN11 ~50%, SOS1, RAF1, KRAS, LZTR1, others); short stature, pulmonary stenosis, hypertrophic cardiomyopathy, and facial dysmorphia; elevated JMML/leukemia risk; MEK inhibitors in clinical trials."
aliases: ["Noonan syndrome", "Noonan's syndrome", "PTPN11 Noonan", "NS Noonan", "RASopathy Noonan", "Noonan syndrome heart", "Noonan syndrome leukemia", "Noonan syndrome cardiomyopathy", "Noonan with lentigines", "LEOPARD syndrome"]
sources:
  - id: tartaglia-2001-ptpn11-noonan
    type: peer-reviewed
    cite: "Tartaglia M, Mehler EL, Goldberg R, et al. Mutations in PTPN11, encoding the protein tyrosine phosphatase SHP-2, cause Noonan syndrome. Nat Genet. 2001;29(4):465-468."
    doi: "10.1038/ng772"
    pmid: "11704759"
    url: "https://doi.org/10.1038/ng772"
  - id: van-der-burgt-2007-noonan-review
    type: peer-reviewed
    cite: "van der Burgt I. Noonan syndrome. Orphanet J Rare Dis. 2007;2:4."
    doi: "10.1186/1750-1172-2-4"
    pmid: "17222357"
    url: "https://doi.org/10.1186/1750-1172-2-4"
cross_links:
  - target: 01-human/03-molecular/ptpn11
    relation: connects-to
    note: "Germline PTPN11 GOF mutations are the most common cause of Noonan syndrome (~50%); SHP2 hyperactivation → RAS-MAPK overactivation → growth restriction, cardiac development defects, and hematologic abnormalities; JMML risk elevated ~150-fold in Noonan syndrome."
  - target: 01-human/03-molecular/lztr1
    relation: connects-to
    note: "PTPN11 and LZTR1 are both RASopathy genes causing Noonan syndrome: PTPN11 GOF hyperactivates SHP2/RAS signaling; LZTR1 LOF prevents CUL3-mediated RAS ubiquitination → RAS accumulation; both disorders share short stature, pulmonary stenosis, and HCM features."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS mutations cause ~5% of Noonan syndrome; KRAS GOF → constitutive RAS-MAPK activation even without upstream SHP2 signal; Noonan syndrome with KRAS mutations tends to have more severe intellectual disability; KRAS G12D drives JMML in Noonan-associated leukemia."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "Noonan syndrome and neurofibromatosis type 1 (NF1) are both RASopathies with overlapping features (café-au-lait spots, pulmonary stenosis, learning differences, short stature); NF1 LOF → RAS-GTP accumulation via GAP loss; PTPN11 GOF → RAS-GTP accumulation via SHP2 activation."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Congenital heart disease affects ~80% of Noonan syndrome: a dysplastic, thickened pulmonary valve causes stenosis in ~50-60% (often balloon-resistant), while RAF1 mutations drive hypertrophic cardiomyopathy in ~20-30%, which MEK inhibitors can reverse."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Every Noonan gene — PTPN11, SOS1, RAF1, KRAS, RIT1, LZTR1 — converges on ERK1/2 hyperactivation during embryogenesis, and the degree of ERK activity grades severity; because MEK1/2 sits just upstream of ERK, MEK inhibitors (trametinib) can normalize signaling and reverse HCM."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "LZTR1 links Noonan syndrome to schwannomatosis through opposite effects of the same gene: dominant LZTR1 mutations cause Noonan (RAS accumulation, developmental phenotype), whereas biallelic LOF or dominant-negative LZTR1 causes schwannomatosis (multiple painful schwannomas)."
  - target: 01-human/07-system/marfan-syndrome
    relation: connects-to
    note: "Noonan and Marfan are both autosomal-dominant multisystem syndromes causing chest-wall deformity, scoliosis, and congenital heart disease, so they share a clinical differential — but are unrelated: Noonan is a RASopathy while Marfan is a fibrillin-1 connective-tissue disorder."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Noonan syndrome and neurofibromatosis type 1 are overlapping RASopathies — both hyperactivate RAS-MAPK and share café-au-lait spots, pulmonary stenosis, and short stature — but via different lesions: NF1 loses the RAS-GAP neurofibromin while Noonan gains function in SHP2/PTPN11."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Lymphatic dysplasia is a characteristic feature of Noonan syndrome: faulty RAS-MAPK during lymphangiogenesis produces fetal cystic hygroma and nuchal edema (often the first prenatal clue), peripheral lymphedema, and occasionally chylothorax — a developmental lymphatic defect."
---

# Noonan Syndrome

## Overview

**Noonan syndrome (NS)** is one of the most common **autosomal dominant RASopathies**, with an estimated prevalence of ~1 in 1,000-2,500 live births, making it among the most frequent non-chromosomal developmental syndromes. NS is caused by germline gain-of-function mutations in genes encoding components of the **RAS-MAPK signaling pathway**: most commonly **PTPN11** (~50%), encoding the SHP2 phosphatase; and also **SOS1** (~13%), **RAF1** (~5%), **KRAS** (~5%), **BRAF** (~2%), **MAP2K1** (~2%), **LZTR1** (~2%), **RIT1** (~9%), **NRAS** (~1%), and others. Each gene mutation dysregulates RAS-MAPK signaling differently, but the net phenotypic outcome — constitutive ERK1/2 hyperactivation during embryogenesis — produces the characteristic Noonan syndrome phenotype. NS was first characterized by Jacqueline Noonan in 1963 as a syndrome of congenital heart disease with short stature and facial dysmorphia in phenotypically normal chromosomal patients. PTPN11 was identified as the causative gene by Tartaglia et al. in 2001 [^tartaglia-2001-ptpn11-noonan] [^van-der-burgt-2007-noonan-review].

NS is characterized by four cardinal features: **(1) short stature** (below 3rd percentile in ~70%; mean adult height ~161 cm males, ~153 cm females); **(2) congenital heart defects** (pulmonary valve stenosis ~50-60%; hypertrophic cardiomyopathy ~20-30%; atrial septal defect, atrioventricular canal defect in subset); **(3) characteristic facial dysmorphia** (hypertelorism, broad forehead, ptosis, low-set posteriorly-rotated ears, short neck with low hairline, high-arched palate); and **(4) variable intellectual disability or learning difficulties** (~25% have some degree of intellectual disability; remainder have normal intelligence but specific learning differences, especially in visuospatial processing). Noonan syndrome is distinguished from Turner syndrome (XO) — which has an overlapping phenotype — by normal karyotype, autosomal dominant transmission, and male sex involvement (NS equally affects males and females; Turner affects only females with 45,X karyotype).

**Noonan syndrome vs. related RASopathies:**

| RASopathy | Gene(s) | Distinguishing features |
|---|---|---|
| Noonan syndrome | PTPN11, SOS1, RAF1, KRAS, LZTR1, RIT1, others | Short stature, pulmonic stenosis, HCM, facial dysmorphia |
| Noonan with multiple lentigines (LEOPARD) | PTPN11 (LOF mutations) | Multiple lentigines, HCM > pulmonic stenosis, EKG abnormalities |
| Cardiofaciocutaneous syndrome (CFC) | BRAF, MAP2K1/2, KRAS | Severe intellectual disability, ectodermal abnormalities, no PTPN11 |
| Costello syndrome | HRAS | Papillomata, redundant skin, rhabdomyosarcoma risk, HRAS |
| Neurofibromatosis type 1 | NF1 (LOF, RAS-GAP) | Café-au-lait spots, neurofibromas, optic glioma, NF1 LOF |

## Structure

### Genetic basis of Noonan syndrome

**Gene prevalence and variant types:**
- **PTPN11 (~50%)**: N-SH2 or PTP domain interface residues (D61Y, D61G, E76K, E76G, Y63C, T468M, I282V); N308D most common overall; associated with pulmonic stenosis; lower HCM rate than RAF1; JMML risk highest with E76K
- **SOS1 (~13%)**: RAS guanine nucleotide exchange factor; SOS1 GOF → sustained RAS activation; associated with pulmonic stenosis, lentigines, normal/high cognition; tallest stature of any NS gene
- **RAF1 (~5%)**: serine/threonine kinase in MAPK cascade; RAF1 GOF (S257L, L613V) strongly associated with HCM (~95% of RAF1-NS have HCM); highest HCM rate of any NS gene
- **KRAS (~5%)**: direct RAS GOF; Noonan phenotype with variable features; higher rate of intellectual disability; some KRAS variants cause cardiofaciocutaneous syndrome if more severe GOF
- **LZTR1 (~2%)**: CUL3 E3 ligase adaptor; dominant mutations causing Noonan syndrome (distinct from biallelic LOF causing schwannomatosis); LZTR1 AD mutations → RAS protein accumulation
- **RIT1 (~9%)**: RAS-related protein; GOF mutations; associated with HCM and pulmonary features; RIT1 does not interact with SHP2
- **BRAF (~2%)**: if mild GOF → Noonan; if more severe GOF → CFC syndrome
- **SHOC2 (~2%)**: Noonan syndrome with loose anagen hair (NSLAH); SHOC2 S2G → myristoylated SHOC2 → constitutive RAS-MAPK; characteristic loose anagen hair, premature skin aging

**Molecular diagnosis:**
- PTPN11 sequencing first (~50% yield); then multi-gene RASopathy panel (SOS1, RAF1, KRAS, LZTR1, RIT1, BRAF, MAP2K1, NRAS, SHOC2, CBL, RRAS); overall panel diagnostic yield ~80% of clinically diagnosed NS
- De novo mutations predominate (~75%); familial transmission in ~25% (AD, variable expressivity)
- Recurrence risk: affected parent → 50% per child; unaffected parents with de novo child: low recurrence (<1%), though germline mosaicism rarely reported

**RAS-MAPK pathway and phenotypic convergence:**
- All Noonan syndrome-causing genes converge on ERK1/2 hyperactivation during embryogenesis
- ERK hyperactivation in specific cell lineages determines the phenotypic features: cardiac progenitors → congenital heart defects; growth plate chondrocytes → short stature; craniofacial neural crest → facial dysmorphia; hematopoietic progenitors → myeloproliferation
- Degree of ERK activation differs by gene: KRAS and RAF1 → highest ERK activity → most severe phenotype; PTPN11 (D61Y) → intermediate; SOS1 → lower → mildest cognitive features

## Function

### Clinical features of Noonan syndrome

**Short stature:**
- Present in ~70% of NS patients; below 3rd percentile in childhood; mean final adult height 161-167 cm (males), 150-155 cm (females)
- GH axis: GH secretion intact; IGF-1 often low-normal; GH insensitivity at chondrocyte level due to ERK hyperactivation interfering with GH/IGF-1 signaling
- **Recombinant GH therapy (somatropin)**: FDA-approved for Noonan syndrome growth failure; dose ~0.066 mg/kg/day; achieves final adult height gain of ~3-5 cm vs. untreated; response rate ~75%; start by age 5-8 years for optimal benefit
- MEK inhibitor (trametinib) trials: early data suggest ERK normalization → improved growth plate function; height improvement in NS mouse models; clinical trials ongoing (NCT04074785)

**Congenital heart defects (~80% of NS patients):**
- **Pulmonary valve stenosis (~50-60%)**: most characteristic; dysplastic (thick, immobile) pulmonic valve leaflets; causes right ventricular outflow obstruction; treatment: balloon valvotomy (less effective than typical PS due to dysplastic morphology) or surgical valvotomy/repair; outcome generally favorable
- **Hypertrophic cardiomyopathy (HCM, ~20-30%)**: predominantly associated with RAF1 mutations; biventricular or isolated ventricular hypertrophy; neonatal HCM can cause heart failure in infancy; treatment: beta-blockers, negative inotropes; septal myectomy or ablation for obstructive HCM; prognosis variable (may regress with age in some)
- **Atrial septal defect (~10%)**: ostium secundum ASD; closure when hemodynamically significant
- **Other**: atrioventricular canal defect, aortic coarctation, ventricular septal defect, mitral valve prolapse/regurgitation; complex congenital heart disease uncommon but reported
- Echocardiography: at diagnosis and annually; ECG: for arrhythmia surveillance (NS patients have risk of prolonged QT, Wolf-Parkinson-White in some)

**Facial dysmorphia (the most diagnostically useful feature):**
- Hypertelorism (wide-set eyes): most consistent; OFC (orbital canthal distance) > 97th percentile
- Epicanthal folds, ptosis (50-70%), downslanting palpebral fissures
- Broad forehead, low-set posteriorly-rotated ears with thick helices
- Broad/short nose with wide, depressed nasal root; prominent nasal tip
- Short neck, webbed neck (pterygium colli, ~25%); low posterior hairline
- Dental crowding, high-arched palate; malocclusion common
- Gestalt of the face changes substantially with age — characteristic in infancy and childhood, more subtle in adults

**Neurodevelopmental features:**
- Intellectual disability: ~25% have IQ <70; most have low-normal to normal IQ; full-spectrum IQ range from severe ID to gifted
- Learning differences: specific learning disability common (reading, math, processing speed); visuospatial difficulties most common
- Language: mild expressive language delays common; most achieve normal speech by school age
- Motor: gross motor delays (hypotonia at birth → delayed walking in 30%); fine motor coordination difficulties persist
- Autism spectrum features: ~20-30% of NS have some ASD features; full ASD diagnosis in subset
- Speech therapy, occupational therapy, and physical therapy from early childhood improve outcomes

**Other features:**
- Coagulopathy: bleeding tendency in ~65%; factors VIII, IX, XI deficiency; platelet dysfunction; preoperative evaluation essential; DDAVP may be needed for surgery
- Lymphatic abnormalities: lymphedema (~20%), chylothorax, lymphangiectasia; especially in fetal NS (hydrops fetalis → resolves with birth in survivors)
- Cryptorchidism (males): ~60-80% of males; spontaneous descent unusual; orchiopexy recommended by 12-18 months to reduce infertility and malignancy risk
- Ophthalmology: strabismus (~50%), nystagmus, amblyopia, refractive errors; keratoconus in adults
- Hearing: sensorineural or conductive hearing loss in ~15%
- Feeding difficulties: poor suck in infancy → gastroesophageal reflux, failure to thrive; nasogastric or gastrostomy tube in some infants

### Cancer in Noonan syndrome

**JMML (juvenile myelomonocytic leukemia):**
- Occurs in ~5% of NS patients with PTPN11 mutations (disproportionately E76K and E76V → highest SHP2 activity)
- Age: first 4 years of life; some resolve spontaneously (distinguishing feature of NS-JMML from sporadic JMML — spontaneous remission more common in NS-JMML)
- Sporadic JMML progresses aggressively and requires allogeneic SCT; NS-JMML: watchful waiting may be appropriate in infants with stable disease; SCT reserved for progression
- Distinguishing NS-JMML from sporadic: NS germline mutation + JMML → Noonan-JMML; in sporadic JMML, PTPN11 E76K is typically somatic

**Other hematologic malignancies:**
- ALL (acute lymphoblastic leukemia): modestly elevated (~2-3x general population)
- AML: some risk, particularly with RAS-MAPK mutations
- Myeloproliferative disease: transient myeloproliferation in neonatal period (often self-limited); may resemble transient abnormal myelopoiesis of Down syndrome

**Neuroblastoma and rhabdomyosarcoma:**
- Modest excess risk vs. general population (2-5x); primarily associated with PTPN11 and KRAS-NS variants
- Tumor surveillance: no formal surveillance protocol for solid tumors; JMML surveillance with CBC + differential every 3-6 months in infancy (especially PTPN11-NS)

## Pathology

### Diagnosis

**Clinical diagnosis (van der Burgt criteria):**
- Definite NS: cardiac (pulmonic stenosis or HCM) + 2 minor features; or facial + 1 major or 2 minor
- Major features: facial dysmorphia, short stature, chest deformity (pectus carinatum/excavatum), cardiac (pulmonic stenosis/HCM/typical ECG)
- Minor features: lower-grade facial/cardiac/height features; cryptorchidism; learning disability; family history
- Molecular confirmation: NGS-based RASopathy gene panel (yield ~80% of clinically diagnosed NS)

**Differential diagnosis:**
- Turner syndrome (45,X): short stature, webbed neck, cardiac, but female-only and 45,X karyotype; NS can mimic Turner in females → karyotype first, then PTPN11 testing
- Cardiofaciocutaneous (CFC) syndrome: BRAF/MAP2K1/KRAS mutations; more severe ID, keratosis pilaris, absent/sparse eyebrows; overlaps Noonan
- Costello syndrome (HRAS): papillomata, neonatal feeding, rhabdomyosarcoma risk; distinctive skin redundancy
- LEOPARD/Noonan with lentigines (PTPN11 LOF): multiple lentigines, HCM, EKG abnormalities; same gene, different mutation type
- Williams syndrome (ELN deletion): elfin face, cocktail personality, aortic supravalvular stenosis, hypercalcemia; 7q11.23 deletion; FISH/microarray
- Neurofibromatosis type 1 (NF1): café-au-lait spots, axillary freckling, neurofibromas; overlapping cardiovascular features (NF1-NS/Neurofibromatosis-Noonan syndrome)

**Multidisciplinary management:**
- **Cardiology**: echocardiogram at diagnosis and annually; pulmonic stenosis → balloon or surgical intervention; HCM → beta-blocker prophylaxis; arrhythmia monitoring
- **Endocrinology**: GH treatment for short stature (FDA-approved); monthly monitoring of response; bone age × 6-12 months
- **Hematology**: CBC at diagnosis; JMML monitoring in infants; preoperative bleeding screen (factors, platelet function); DDAVP for surgery
- **Neurodevelopment**: developmental assessment; speech, OT, PT from infancy; educational accommodations; cognitive behavioral support
- **Ophthalmology**: strabismus treatment; annual eye exam
- **Orthopedics**: pectus deformity monitoring; scoliosis screening
- **Urology**: orchiopexy in males by 12-18 months
- **Genetics**: cascade family testing (50% risk per child); prenatal diagnosis; PGT-A for affected individuals wishing to avoid transmission
- **Research registries**: International NS Registry; MEK inhibitor trial referral for eligible patients

**MEK inhibitor therapy (emerging):**
- Trametinib (MEK1/2 inhibitor): case reports of dramatic response in NS-HCM (resolution of HCM within months); Phase 2 trials (NCT04074785) enrolling NS patients with HCM, growth failure, or symptomatic disease
- Rationale: MEK1/2 is 2 steps downstream of the RASopathy mutations → MEK inhibition normalizes ERK → may reverse cardiac hypertrophy, improve growth, reduce leukemia risk
- Safety concern: MEK inhibitors can cause ocular toxicity (retinopathy, blurred vision), skin toxicity, fever; long-term use in children not yet established

## Connections

- `connects-to` → **[PTPN11](../../03-molecular/ptpn11/README.md)** — Germline PTPN11 GOF mutations are the most common cause of Noonan syndrome (~50%); SHP2 hyperactivation → RAS-MAPK overactivation → growth restriction, cardiac development defects, and hematologic abnormalities; JMML risk elevated ~150-fold in Noonan syndrome.
- `connects-to` → **[LZTR1](../../03-molecular/lztr1/README.md)** — PTPN11 and LZTR1 are both RASopathy genes causing Noonan syndrome: PTPN11 GOF hyperactivates SHP2/RAS signaling; LZTR1 LOF prevents CUL3-mediated RAS ubiquitination → RAS accumulation; both disorders share short stature, pulmonary stenosis, and HCM features.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS mutations cause ~5% of Noonan syndrome; KRAS GOF → constitutive RAS-MAPK activation even without upstream SHP2 signal; Noonan syndrome with KRAS mutations tends to have more severe intellectual disability; KRAS G12D drives JMML in Noonan-associated leukemia.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — Noonan syndrome and neurofibromatosis type 1 (NF1) are both RASopathies with overlapping features (café-au-lait spots, pulmonary stenosis, learning differences, short stature); NF1 LOF → RAS-GTP accumulation via GAP loss; PTPN11 GOF → RAS-GTP accumulation via SHP2 activation.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Congenital heart disease affects ~80% of Noonan syndrome: a dysplastic, thickened pulmonary valve causes stenosis in ~50-60% (often balloon-resistant), while RAF1 mutations drive hypertrophic cardiomyopathy in ~20-30%, which MEK inhibitors can reverse.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Every Noonan gene — PTPN11, SOS1, RAF1, KRAS, RIT1, LZTR1 — converges on ERK1/2 hyperactivation during embryogenesis, and the degree of ERK activity grades severity; because MEK1/2 sits just upstream of ERK, MEK inhibitors (trametinib) can normalize signaling and reverse HCM.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — LZTR1 links Noonan syndrome to schwannomatosis through opposite effects of the same gene: dominant LZTR1 mutations cause Noonan (RAS accumulation, developmental phenotype), whereas biallelic LOF or dominant-negative LZTR1 causes schwannomatosis (multiple painful schwannomas).
- `connects-to` → **[Marfan Syndrome](../marfan-syndrome/README.md)** — Noonan and Marfan are both autosomal-dominant multisystem syndromes causing chest-wall deformity, scoliosis, and congenital heart disease, so they share a clinical differential — but are unrelated: Noonan is a RASopathy while Marfan is a fibrillin-1 connective-tissue disorder.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Noonan syndrome and neurofibromatosis type 1 are overlapping RASopathies — both hyperactivate RAS-MAPK and share café-au-lait spots, pulmonary stenosis, and short stature — but via different lesions: NF1 loses the RAS-GAP neurofibromin while Noonan gains function in SHP2/PTPN11.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Lymphatic dysplasia is a characteristic feature of Noonan syndrome: faulty RAS-MAPK during lymphangiogenesis produces fetal cystic hygroma and nuchal edema (often the first prenatal clue), peripheral lymphedema, and occasionally chylothorax — a developmental lymphatic defect.

[^tartaglia-2001-ptpn11-noonan]: Tartaglia M, Mehler EL, Goldberg R, et al. Mutations in PTPN11, encoding the protein tyrosine phosphatase SHP-2, cause Noonan syndrome. *Nat Genet.* 2001;29(4):465-468. [doi:10.1038/ng772](https://doi.org/10.1038/ng772) · [PubMed 11704759](https://pubmed.ncbi.nlm.nih.gov/11704759/)
[^van-der-burgt-2007-noonan-review]: van der Burgt I. Noonan syndrome. *Orphanet J Rare Dis.* 2007;2:4. [doi:10.1186/1750-1172-2-4](https://doi.org/10.1186/1750-1172-2-4) · [PubMed 17222357](https://pubmed.ncbi.nlm.nih.gov/17222357/)
