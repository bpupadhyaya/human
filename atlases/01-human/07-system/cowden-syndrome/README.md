---
schema: human-scale-entry/v1
id: cowden-syndrome
name: Cowden Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Cowden syndrome (PTEN hamartoma tumor syndrome, PHTS) is caused by germline PTEN mutations or KLLN hypermethylation; breast cancer (~77-85%), thyroid, endometrial, and renal tumors; Lhermitte-Duclos disease is pathognomonic; annual MRI breast surveillance."
aliases: ["Cowden syndrome", "PTEN hamartoma tumor syndrome", "PHTS", "Bannayan-Riley-Ruvalcaba syndrome", "BRRS", "Cowden disease", "PTEN Cowden syndrome", "KLLN Cowden", "Cowden PTEN", "multiple hamartoma syndrome"]
sources:
  - id: bubien-2013-cowden-cancer-risk
    type: peer-reviewed
    cite: "Bubien V, Bonnet F, Brouste V, et al. High cumulative risks of cancer in patients with PTEN hamartoma tumour syndrome. J Med Genet. 2013;50(4):255-263."
    doi: "10.1136/jmedgenet-2012-101339"
    pmid: "23335809"
    url: "https://doi.org/10.1136/jmedgenet-2012-101339"
  - id: bennett-2010-klln-cowden
    type: peer-reviewed
    cite: "Bennett KL, Mester J, Eng C. Germline epigenetic regulation of KILLIN in Cowden and Cowden-like syndrome. JAMA. 2010;304(24):2724-2731."
    doi: "10.1001/jama.2010.1877"
    pmid: "21177507"
    url: "https://doi.org/10.1001/jama.2010.1877"
cross_links:
  - target: 01-human/03-molecular/klln
    relation: connects-to
    note: "KLLN promoter CpG hypermethylation silences KLLN in ~30-35% of PTEN-mutation-negative Cowden patients; KLLN and PTEN are co-located at 10q23 and regulate overlapping tumor suppressor functions; KLLN LOF → replication stress → genomic instability → PHTS tumors."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN germline pathogenic variants (~80% of classic Cowden) are the primary molecular driver; PTEN dephosphorylates PIP3 → reduced PI3K-AKT → cell cycle arrest and apoptosis; PTEN LOF → PI3K-AKT-mTOR hyperactivation → breast, thyroid, endometrial, renal tumors."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Cowden/PHTS female lifetime breast cancer risk is ~77-85% (vs 12% population); annual MRI + mammogram from age 30-35; prophylactic mastectomy is an option; molecular subtype: predominantly HR+/HER2- (similar to BRCA1/2-related BC); PTEN LOF → PI3K-AKT → BC growth."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Cowden/PHTS thyroid cancer risk ~35% lifetime (follicular carcinoma predominates; NOT medullary thyroid cancer — MTC is RET/MEN2); multinodular goiter and thyroid adenomas are common benign features; annual thyroid ultrasound surveillance from diagnosis."
---

# Cowden Syndrome

## Overview

**Cowden syndrome** (PTEN Hamartoma Tumor Syndrome, PHTS) is the unifying term for a spectrum of hereditary conditions — Cowden syndrome (CS), Bannayan-Riley-Ruvalcaba syndrome (BRRS), PTEN-related Proteus syndrome, and Proteus-like syndrome — all caused primarily by germline pathogenic variants in **PTEN** (phosphatase and tensin homolog, 10q23.31) or epigenetic silencing of the co-located **KLLN** gene. PTEN germline variants are identified in ~80% of classic Cowden, ~65% of BRRS, and variable fractions of other PHTS entities. **KLLN promoter CpG hypermethylation** accounts for an additional ~30-35% of PTEN-mutation-negative patients meeting clinical Cowden criteria. PHTS is characterized by a dramatically elevated lifetime risk of breast cancer (~77-85%), thyroid carcinoma (~35%), endometrial carcinoma (~28%), and renal tumors (~34%), along with characteristic benign hamartomatous features — trichilemmomas, papillomatous papules, macrocephaly, and GI polyposis. **Lhermitte-Duclos disease** (adult dysplastic gangliocytoma of the cerebellum) is pathognomonic and when present in an adult virtually defines PTEN mutation until proven otherwise. Prevalence is estimated at ~1/200,000 to 1/250,000 [^bubien-2013-cowden-cancer-risk] [^bennett-2010-klln-cowden].

**Cowden/PHTS lifetime cancer risks:**

| Cancer | PHTS Lifetime Risk | General Population |
|---|---|---|
| Female breast cancer | ~77-85% | ~12% |
| Thyroid (follicular, papillary) | ~35% | ~2% |
| Endometrial carcinoma | ~28% | ~2.5% |
| Renal (papillary, chromophobe) | ~34% | ~1.5% |
| Colorectal | ~9% | ~5% |
| Melanoma | ~6% | ~2% |

## Structure

### Genetic basis of PHTS

**PTEN (10q23.31):**
- 9 exons; 403 aa; 54 kDa; dual specificity phosphatase (lipid + protein); primary substrate = PIP3 → PIP2 (directly antagonizes PI3K); also has nuclear functions (genomic stability)
- Germline variant spectrum: missense (~35%; highest in phosphatase domain exons 5-8), frameshift/nonsense (~30%), splice site (~10%), promoter/5'UTR (~10%), large deletions (~10-15%)
- Haploinsufficiency: heterozygous LOF in germline; second somatic hit (LOH, methylation, point mutation) in tumors; biallelic PTEN loss is embryonic lethal in mice; germline homozygous PTEN LOF not viable
- Genotype-phenotype correlations:
  - Phosphatase domain missense (exons 5-8): highest cancer risk; classic Cowden + BRRS overlap possible
  - C-terminal domain variants (exons 7-9): associated with autism/macrocephaly spectrum without full Cowden cancer penetrance (some variants)
  - Promoter/5'UTR: lower expression → milder but still elevated cancer risk

**KLLN (10q23.31, antisense):**
- Germline epigenetic silencing (promoter CpG methylation) → haploinsufficiency via epigenetic mechanism rather than sequence mutation
- Found in ~30-35% of PTEN-coding-negative patients meeting clinical CS criteria; germline methylation detectable in blood DNA by bisulfite pyrosequencing (methylation ≥10-15% vs <5% in controls)
- Explains transmission of CS-like phenotype in families without PTEN coding mutation

**Other molecular causes (PTEN-negative, KLLN-negative Cowden-like):**
- SEC23B (COPII vesicle transport): variants found in ~5-10% of PTEN/KLLN-negative cases; mechanism unclear; thyroid tumor risk especially elevated
- SDHB/SDHC/SDHD: SDH variants in subset of Cowden-like patients with concurrent pheochromocytoma or paraganglioma features; distinct "SDH Cowden-like" entity
- PIK3CA somatic mosaicism: some Proteus-like features with somatic PIK3CA GOF (mosaicism)

### Clinical diagnostic criteria (NCCN Cowden/PHTS revised)

**Pathognomonic:**
- Lhermitte-Duclos disease (dysplastic gangliocytoma of the cerebellum) — adult onset

**Major criteria:**
- Breast carcinoma (or high-density breast lesion)
- Follicular thyroid carcinoma
- Macrocephaly (≥97th percentile; ≥58 cm head circumference in adults)
- Endometrial carcinoma
- Multiple GI hamartomas or ganglioneuromas (≥3)

**Minor criteria:**
- Autism spectrum disorder; intellectual disability
- Single GI hamartoma or ganglioneuroma
- Thyroid structural lesions (multinodular goiter, adenoma); lipoma; arteriovenous malformation
- Trichilemmoma (facial) — minor when single; pathognomonic when ≥3 or biopsied
- Penile freckling (lentigines on glans); fibrocystic breast disease; renal carcinoma; uterine fibroids

**Clinical diagnosis requires:**
- 1 pathognomonic criterion; OR
- ≥3 major criteria; OR
- 2 major criteria (one being macrocephaly or GI hamartomas) + ≥1 minor; OR
- 1 major + ≥3 minor criteria

**Indication for PTEN/KLLN molecular testing:**
- Meeting or borderline meeting clinical CS criteria
- ≥3 Cowden minor criteria
- Family member of known PTEN/KLLN carrier
- Macrocephaly + autism/intellectual disability
- Lhermitte-Duclos disease (adult onset)
- Young-onset breast + thyroid or endometrial cancer in same patient

## Function

### Cancer manifestations

**Breast cancer (~77-85% lifetime risk, female):**
- Onset typically younger than sporadic breast cancer (median ~38-46y in PTEN carriers vs ~61y sporadic)
- Predominant molecular subtype: HR+/HER2- (luminal-type); triple-negative less common than in BRCA1 carriers
- Both ductal and lobular subtypes; lobular BC also associated with CDH1/E-cadherin loss (HDGC) — distinct from PHTS
- Risk management: annual breast MRI + mammogram from age 30-35 (or 5-10 years before youngest affected family member); clinical breast exam every 6 months; prophylactic bilateral mastectomy reduces risk by ~90% and is a valid option after counseling
- PTEN IHC loss: found in ~5-15% of sporadic breast cancers; used as companion diagnostic marker for PI3K pathway inhibitor sensitivity (alpelisib, everolimus combinations)

**Thyroid cancer (~35% lifetime):**
- Follicular thyroid carcinoma (FTC) is the hallmark PHTS thyroid malignancy; papillary thyroid carcinoma also occurs; anaplastic rare
- Medullary thyroid cancer (MTC) is NOT a PHTS feature (MTC = germline RET/MEN2)
- Benign thyroid disease precedes malignancy: multinodular goiter in >50%, multiple thyroid adenomas; thyroid architecture is abnormal on ultrasound from early life
- Surveillance: annual thyroid ultrasound from diagnosis; FNA for suspicious nodules (BETHESDA IV-VI)
- Surgery: hemithyroidectomy (diagnostic) or total thyroidectomy (confirmed FTC or bilateral nodularity); completion thyroidectomy if hemithyroid shows FTC

**Endometrial cancer (~28% lifetime):**
- Endometrioid adenocarcinoma predominates (same histology as in Lynch syndrome but molecular basis differs: PTEN/PI3K vs MMR)
- PTEN is the most frequently mutated gene in sporadic endometrioid EC (~65% of sporadic EC have somatic PTEN mutation) → PTEN is the master tumor suppressor in endometrium; germline PTEN LOF → >10-fold lifetime risk elevation
- Often early-stage, well-differentiated (Grade 1-2), good prognosis if detected early
- Surveillance: annual transvaginal ultrasound (TVU) or endometrial biopsy from age 35; low threshold for biopsy in any symptomatic patient
- Prophylactic hysterectomy ± bilateral salpingo-oophorectomy: offered after childbearing is complete; eliminates ~28% lifetime EC risk

**Renal tumors (~34% lifetime):**
- Chromophobe RCC and papillary RCC (type 2) predominate; clear cell RCC less common (contrast: VHL disease, BHD both also cause renal tumors with different histology)
- Screening: renal ultrasound or MRI every 1-2 years from age 40 (or from diagnosis)
- Management: same as sporadic RCC by subtype; partial nephrectomy when feasible

**Colorectal (~9% lifetime):**
- Cowden GI polyposis: mixture of hamartomatous (lipomatous/inflammatory), hyperplastic, adenomatous polyps
- Not as high-risk as FAP (no obligate progression); but adenomatous component elevates CRC risk above population
- Colonoscopy every 5 years from age 35; polypectomy of adenomas

### Benign and hamartoma features

**Mucocutaneous (clinical hallmarks):**
- Trichilemmomas: benign hair follicle hamartomas; multiple lesions on face (nose, ears, perioral area, cheeks) are pathognomonic; confirmed by skin biopsy (squamous epithelium with clear cell glycogen-rich cytoplasm)
- Papillomatous papules: cobblestone-like keratoses on tongue, gingiva, buccal mucosa; oral papillomas
- Acral keratoses: palmar/plantar pitting, punctate keratoses
- Penile freckling: lentigines on glans penis in males — a highly specific but minor clinical finding; triggers PTEN testing
- Lipomas, hemangiomas, arteriovenous malformations: common; lipomas can be multiple

**Macrocephaly and neurological features:**
- Megalencephaly (true brain overgrowth): head circumference ≥97th percentile in ~90% of PTEN mutation carriers; most sensitive screening criterion for the syndrome
- Lhermitte-Duclos disease (LDD): dysplastic gangliocytoma of the cerebellum; slowly growing hamartoma (not malignant) that replaces normal cerebellar cortex; presents with cerebellar ataxia, headache, signs of obstructive hydrocephalus; MRI = pathognomonic "tiger stripe" pattern (alternating T2 bright and dark bands in cerebellum); adult onset LDD = PTEN mutation until proven otherwise; treatment: surgery for symptomatic disease only; recurrence common after resection; no malignant transformation
- Autism spectrum disorder / intellectual disability: ~10-20% of macrocephalic PTEN mutation carriers; PTEN is a major ASD susceptibility gene (somatic/de novo PTEN variants in ASD cohorts)

**Bannayan-Riley-Ruvalcaba syndrome (BRRS) — pediatric PHTS:**
- Macrocephaly + penile freckling (highly specific) + lipomatosis (multiple subcutaneous lipomas) + GI polyposis + vascular malformations + developmental delay/intellectual disability
- BRRS is the pediatric presentation of the PTEN mutation spectrum; adult BRRS patients carry full Cowden cancer risks → transition to Cowden surveillance at adulthood

## Pathology

### Surveillance protocol (NCCN/ESMO recommendations)

**Breast:**
- Annual breast MRI + mammogram from age 30-35 (or 5-10 years before youngest affected family member, whichever is younger)
- Clinical breast exam every 6 months
- Prophylactic bilateral mastectomy: offered after counseling; reduces breast cancer risk by ~90%; reconstruction options discussed

**Thyroid:**
- Annual thyroid ultrasound from diagnosis (at any age if mutation confirmed)
- FNA for suspicious nodules (BETHESDA IV or higher)
- Baseline ultrasound establishes architecture reference for comparison

**Endometrial:**
- Annual TVU or endometrial biopsy/aspiration from age 35
- Consider prophylactic hysterectomy ± BSO after childbearing; most effective risk reduction for EC

**Renal:**
- Renal ultrasound or MRI every 1-2 years from age 40

**Colorectal:**
- Colonoscopy every 5 years from age 35; polypectomy of adenomatous polyps
- Annual fecal occult blood test as adjunct (not a replacement for colonoscopy)

**Dermatology:**
- Annual skin exam for new trichilemmomas, keratoses

**Neurological:**
- Clinical neurological assessment annually; brain MRI only if symptomatic (LDD suspected)

**Family and genetic cascade testing:**
- Autosomal dominant; 50% offspring risk
- PTEN mutation: offer testing to all first-degree relatives from adolescence (surveillance begins on identification)
- KLLN methylation: testing of at-risk relatives; detectable in blood DNA by bisulfite pyrosequencing; some methylation may arise de novo rather than being inherited, so family testing is important
- Genetic counseling: penetrance is high (~90% for at least one feature by age 20 for mucocutaneous signs; cancer risks accumulate through 4th-6th decade)

### mTOR-targeted therapy in PHTS

**Rationale:** PTEN LOF → PI3K-AKT hyperactivation → mTORC1 activation → S6K1/4EBP1 phosphorylation → protein synthesis, cell growth, cell cycle progression; all PHTS tumors are PI3K-AKT-mTOR dependent (mechanistically)

**Everolimus (Afinitor, mTORC1 inhibitor):**
- Approved for: HR+/HER2- advanced BC (with exemestane; BOLERO-2 included PTEN-low subgroup), advanced RCC (RECORD-1), pancreatic NETs (RADIANT-3), renal angiomyolipomas in TSC (EXIST-2) — overlapping biology with PHTS
- In PHTS-associated tumors: activity demonstrated in case series; formal clinical trials limited by rare syndrome prevalence

**Alpelisib (Piqray, PI3Kα inhibitor):**
- Approved for PIK3CA-mutant HR+/HER2- BC (SOLAR-1); less directly applicable to PTEN-null tumors (since PTEN LOF activates all PI3K isoforms, not just p110α); combinations with mTOR inhibitors under investigation

**AKT inhibitors (capivasertib, ipatasertib):**
- Clinical trials in PTEN-deficient BC (capivasertib/CAPItello-291 included PTEN-loss biomarker cohort); mechanistically rational for PTEN LOF

## Connections

- `connects-to` → **[KLLN](../../03-molecular/klln/README.md)** — KLLN promoter CpG hypermethylation silences KLLN in ~30-35% of PTEN-mutation-negative Cowden patients; KLLN and PTEN are co-located at 10q23 and regulate overlapping tumor suppressor functions; KLLN LOF → replication stress → genomic instability → PHTS tumors.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN germline pathogenic variants (~80% of classic Cowden) are the primary molecular driver; PTEN dephosphorylates PIP3 → reduced PI3K-AKT → cell cycle arrest and apoptosis; PTEN LOF → PI3K-AKT-mTOR hyperactivation → breast, thyroid, endometrial, renal tumors.
- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — Cowden/PHTS female lifetime breast cancer risk is ~77-85% (vs 12% population); annual MRI + mammogram from age 30-35; prophylactic mastectomy is an option; molecular subtype: predominantly HR+/HER2- (similar to BRCA1/2-related BC); PTEN LOF → PI3K-AKT → BC growth.
- `connects-to` → **[Thyroid Cancer](../../07-system/thyroid-cancer/README.md)** — Cowden/PHTS thyroid cancer risk ~35% lifetime (follicular carcinoma predominates; NOT medullary thyroid cancer — MTC is RET/MEN2); multinodular goiter and thyroid adenomas are common benign features; annual thyroid ultrasound surveillance from diagnosis.

[^bubien-2013-cowden-cancer-risk]: Bubien V, Bonnet F, Brouste V, et al. High cumulative risks of cancer in patients with PTEN hamartoma tumour syndrome. *J Med Genet.* 2013;50(4):255-263. [doi:10.1136/jmedgenet-2012-101339](https://doi.org/10.1136/jmedgenet-2012-101339) · [PubMed 23335809](https://pubmed.ncbi.nlm.nih.gov/23335809/)
[^bennett-2010-klln-cowden]: Bennett KL, Mester J, Eng C. Germline epigenetic regulation of KILLIN in Cowden and Cowden-like syndrome. *JAMA.* 2010;304(24):2724-2731. [doi:10.1001/jama.2010.1877](https://doi.org/10.1001/jama.2010.1877) · [PubMed 21177507](https://pubmed.ncbi.nlm.nih.gov/21177507/)
