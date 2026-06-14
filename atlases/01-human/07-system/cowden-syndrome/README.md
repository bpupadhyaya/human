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
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PTEN LOF → PI3K-AKT → mTOR hyperactivation in all PHTS tumors; mTORC1 drives S6K1/4EBP1 → protein synthesis and cell growth; everolimus (mTORC1 inhibitor) active in HR+/HER2- BC, RCC, and PHTS-associated lesions; mTOR is the canonical PHTS therapeutic target."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PTEN LOF → constitutive AKT phosphorylation (Ser473/Thr308) → survival, proliferation, and cell cycle entry; capivasertib and ipatasertib active in PTEN-deficient BC; capivasertib + fulvestrant approved (CAPItello-291) for HR+/HER2- BC with PI3K/AKT/PTEN alterations."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Cowden/PHTS endometrial cancer risk ~28% lifetime; endometrioid adenocarcinoma predominates; PTEN is most frequently mutated in sporadic endometrioid EC (~65%); often early-stage, well-differentiated; annual TVU/biopsy from age 35; prophylactic hysterectomy after childbearing."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "PTEN is a major autism gene: in Cowden/PTEN hamartoma syndrome, germline PTEN loss produces megalencephaly and, in 10-20% of macrocephalic carriers, autism spectrum disorder — and PTEN testing is recommended for any child with autism plus a very large head."
  - target: 01-human/07-system/birt-hogg-dube-syndrome
    relation: connects-to
    note: "Cowden and Birt-Hogg-Dubé syndromes are hereditary tumour syndromes that converge on mTOR: Cowden loses PTEN (over-activating PI3K-AKT-mTOR) while BHD loses folliculin (a RagC/D GAP feeding mTORC1), and both produce skin hamartomas and an elevated risk of renal cell carcinoma."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Cowden syndrome leaves two brain signatures: megalencephaly (≥97th-percentile head size in ~90% of carriers) and Lhermitte-Duclos disease — a dysplastic cerebellar gangliocytoma whose 'tiger-stripe' MRI is pathognomonic and, in an adult, essentially defines a PTEN mutation."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Cowden syndrome raises colorectal-cancer risk through PTEN hamartoma-tumor biology: PTEN loss disinhibits PI3K-AKT-mTOR in the colon, producing mixed hamartomatous, ganglioneuromatous and adenomatous polyps and increased colorectal-cancer risk, so colonoscopy is recommended."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Cowden and juvenile polyposis are overlapping hamartomatous polyposis syndromes hard to separate: both produce GI hamartomatous polyps and cancer risk, but Cowden (PTEN) adds macrocephaly, trichilemmomas and breast/thyroid cancer, while JPS (SMAD4/BMPR1A) is more gut-confined."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Renal cell carcinoma is part of the Cowden tumor spectrum: PTEN loss driving PI3K-AKT-mTOR raises the lifetime risk of (usually papillary or chromophobe) RCC alongside breast, thyroid and endometrial cancer, so renal imaging is part of PTEN-hamartoma-syndrome surveillance."
  - target: 01-human/07-system/peutz-jeghers-syndrome
    relation: connects-to
    note: "Cowden and Peutz-Jeghers are both hamartomatous tumor syndromes on different pathways: Cowden's PTEN loss unleashes PI3K/mTOR, causing hamartomas plus breast, thyroid, and endometrial cancer, while Peutz-Jeghers' STK11 loss causes GI hamartomas with mucocutaneous pigmentation."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Cowden syndrome and tuberous sclerosis are hamartoma syndromes converging on mTOR from opposite ends: Cowden's PTEN loss removes a brake upstream of mTOR, while TSC1/TSC2 loss directly unleashes it—so both cause hamartomas and respond to mTOR inhibitors."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin gives the earliest clues to Cowden syndrome: trichilemmomas (facial papules), oral papillomas, and acral keratoses are diagnostic mucocutaneous hamartomas of PTEN loss, often appearing before the breast and thyroid cancers—a dermatologist may diagnose it first."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid gland is a hallmark Cowden target: PTEN loss causes multinodular goiter, adenomas and a raised risk of (especially follicular) thyroid cancer, so Cowden patients undergo thyroid surveillance from childhood—often where the syndrome first declares itself."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cowden's signature skin lesions are fibroblast-driven hamartomas: trichilemmomas and fibromas arise as PTEN-deficient cells including fibroblasts overgrow in benign tumors—these mucocutaneous bumps are a key diagnostic clue to the underlying PTEN mutation."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Cowden and Lynch syndrome are both hereditary cancer syndromes with colon risk but different polyps: Cowden causes hamartomatous polyps via PTEN loss, while Lynch drives mismatch-repair-deficient adenomas—so polyp histology and gene testing tell them apart."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin is central to diagnosing Cowden syndrome: PTEN loss produces near-pathognomonic mucocutaneous hamartomas—facial trichilemmomas, oral papillomas and palmoplantar keratoses—so these benign growths are major criteria flagging the cancer-prone syndrome."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Cowden syndrome modestly raises melanoma risk: PTEN loss deregulates the PI3K/AKT pathway in melanocytes too, adding skin-cancer surveillance to the breast, thyroid, endometrial and renal screening this multi-cancer syndrome demands."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Cowden syndrome reaches the nervous system: macrocephaly, autism-spectrum features and the rare cerebellar Lhermitte-Duclos hamartoma reflect PTEN's role in neuronal growth, so neurodevelopmental signs can be the first clue to the PTEN mutation."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Cowden syndrome unleashes the PI3K pathway: losing PTEN removes the brake on PI3K-AKT-mTOR signaling, so cells over-grow into hamartomas and cancers—making PI3K/mTOR inhibitors a rational targeted therapy for this PTEN-hamartoma syndrome."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Cowden syndrome carpets the colon with polyps: hamartomatous (and other) polyps stud the large intestine and raise colorectal cancer risk, so regular colonoscopy is part of the intensive cancer surveillance these patients need."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cowden syndrome affects the reproductive tract: uterine fibroids are common and endometrial cancer risk is high, so gynecologic surveillance and counseling about hysterectomy are part of managing this PTEN-driven syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Cowden syndrome silences FOXO by unleashing AKT: PTEN normally restrains AKT, so its loss lets AKT shut down FOXO transcription factors that would trigger apoptosis and cell-cycle arrest—removing a brake and letting hamartomas and cancers grow."
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "Some Cowden-like patients carry SDHB instead of PTEN: a subset with the classic features but no PTEN mutation have variants in mitochondrial SDHB/SDHD, so testing these genes helps explain PTEN-negative cases and refines cancer risk."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Cowden syndrome warps cerebellar neurons in Lhermitte-Duclos disease: PTEN loss drives a hamartomatous overgrowth of dysplastic neurons in the cerebellum, the nervous-system hallmark that, with macrocephaly, points to the diagnosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Cowden syndrome raises the risk of kidney cancer: PTEN loss unleashes the PI3K-mTOR growth axis in renal cells too, so renal cell carcinoma joins breast, thyroid and uterine cancers in the surveillance these patients need."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "PTEN loss in Cowden drives VEGF and abnormal vessels: with the PI3K-mTOR brake gone, cells overproduce VEGF, fueling the vascular malformations and the blood supply of the hamartomas and tumors the syndrome spawns."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Cowden's hamartomas are overgrowths shaped by TGF-beta: unchecked PTEN-pathway signaling with TGF-beta drives the fibrous proliferation behind the skin trichilemmomas, oral papillomas and intestinal hamartomas that define the syndrome."
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
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Cowden/PHTS thyroid cancer risk ~35% lifetime (follicular carcinoma predominates; NOT medullary thyroid cancer — MTC is RET/MEN2); multinodular goiter and thyroid adenomas are common benign features; annual thyroid ultrasound surveillance from diagnosis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PTEN LOF → PI3K-AKT → mTOR hyperactivation in all PHTS tumors; mTORC1 drives S6K1/4EBP1 → protein synthesis and cell growth; everolimus (mTORC1 inhibitor) active in HR+/HER2- BC, RCC, and PHTS-associated lesions; mTOR is the canonical PHTS therapeutic target.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PTEN LOF → constitutive AKT phosphorylation (Ser473/Thr308) → survival, proliferation, and cell cycle entry; capivasertib and ipatasertib active in PTEN-deficient BC; capivasertib + fulvestrant approved (CAPItello-291) for HR+/HER2- BC with PI3K/AKT/PTEN alterations.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Cowden/PHTS endometrial cancer risk ~28% lifetime; endometrioid adenocarcinoma predominates; PTEN is most frequently mutated in sporadic endometrioid EC (~65%); often early-stage, well-differentiated; annual TVU/biopsy from age 35; prophylactic hysterectomy after childbearing.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — PTEN is a major autism gene: in Cowden/PTEN hamartoma syndrome, germline PTEN loss produces megalencephaly and, in 10-20% of macrocephalic carriers, autism spectrum disorder — and PTEN testing is recommended for any child with autism plus a very large head.
- `connects-to` → **[Birt-Hogg-Dubé Syndrome](../birt-hogg-dube-syndrome/README.md)** — Cowden and Birt-Hogg-Dubé syndromes are hereditary tumour syndromes that converge on mTOR: Cowden loses PTEN (over-activating PI3K-AKT-mTOR) while BHD loses folliculin (a RagC/D GAP feeding mTORC1), and both produce skin hamartomas and an elevated risk of renal cell carcinoma.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Cowden syndrome leaves two brain signatures: megalencephaly (≥97th-percentile head size in ~90% of carriers) and Lhermitte-Duclos disease — a dysplastic cerebellar gangliocytoma whose 'tiger-stripe' MRI is pathognomonic and, in an adult, essentially defines a PTEN mutation.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Cowden syndrome raises colorectal-cancer risk through PTEN hamartoma-tumor biology: PTEN loss disinhibits PI3K-AKT-mTOR in the colon, producing mixed hamartomatous, ganglioneuromatous and adenomatous polyps and increased colorectal-cancer risk, so colonoscopy is recommended.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — Cowden and juvenile polyposis are overlapping hamartomatous polyposis syndromes hard to separate: both produce GI hamartomatous polyps and cancer risk, but Cowden (PTEN) adds macrocephaly, trichilemmomas and breast/thyroid cancer, while JPS (SMAD4/BMPR1A) is more gut-confined.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Renal cell carcinoma is part of the Cowden tumor spectrum: PTEN loss driving PI3K-AKT-mTOR raises the lifetime risk of (usually papillary or chromophobe) RCC alongside breast, thyroid and endometrial cancer, so renal imaging is part of PTEN-hamartoma-syndrome surveillance.
- `connects-to` → **[Peutz-Jeghers Syndrome](../peutz-jeghers-syndrome/README.md)** — Cowden and Peutz-Jeghers are both hamartomatous tumor syndromes on different pathways: Cowden's PTEN loss unleashes PI3K/mTOR, causing hamartomas plus breast, thyroid, and endometrial cancer, while Peutz-Jeghers' STK11 loss causes GI hamartomas with mucocutaneous pigmentation.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Cowden syndrome and tuberous sclerosis are hamartoma syndromes converging on mTOR from opposite ends: Cowden's PTEN loss removes a brake upstream of mTOR, while TSC1/TSC2 loss directly unleashes it—so both cause hamartomas and respond to mTOR inhibitors.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin gives the earliest clues to Cowden syndrome: trichilemmomas (facial papules), oral papillomas, and acral keratoses are diagnostic mucocutaneous hamartomas of PTEN loss, often appearing before the breast and thyroid cancers—a dermatologist may diagnose it first.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid gland is a hallmark Cowden target: PTEN loss causes multinodular goiter, adenomas and a raised risk of (especially follicular) thyroid cancer, so Cowden patients undergo thyroid surveillance from childhood—often where the syndrome first declares itself.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cowden's signature skin lesions are fibroblast-driven hamartomas: trichilemmomas and fibromas arise as PTEN-deficient cells including fibroblasts overgrow in benign tumors—these mucocutaneous bumps are a key diagnostic clue to the underlying PTEN mutation.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Cowden and Lynch syndrome are both hereditary cancer syndromes with colon risk but different polyps: Cowden causes hamartomatous polyps via PTEN loss, while Lynch drives mismatch-repair-deficient adenomas—so polyp histology and gene testing tell them apart.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin is central to diagnosing Cowden syndrome: PTEN loss produces near-pathognomonic mucocutaneous hamartomas—facial trichilemmomas, oral papillomas and palmoplantar keratoses—so these benign growths are major criteria flagging the cancer-prone syndrome.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Cowden syndrome modestly raises melanoma risk: PTEN loss deregulates the PI3K/AKT pathway in melanocytes too, adding skin-cancer surveillance to the breast, thyroid, endometrial and renal screening this multi-cancer syndrome demands.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Cowden syndrome reaches the nervous system: macrocephaly, autism-spectrum features and the rare cerebellar Lhermitte-Duclos hamartoma reflect PTEN's role in neuronal growth, so neurodevelopmental signs can be the first clue to the PTEN mutation.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Cowden syndrome unleashes the PI3K pathway: losing PTEN removes the brake on PI3K-AKT-mTOR signaling, so cells over-grow into hamartomas and cancers—making PI3K/mTOR inhibitors a rational targeted therapy for this PTEN-hamartoma syndrome.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Cowden syndrome carpets the colon with polyps: hamartomatous (and other) polyps stud the large intestine and raise colorectal cancer risk, so regular colonoscopy is part of the intensive cancer surveillance these patients need.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cowden syndrome affects the reproductive tract: uterine fibroids are common and endometrial cancer risk is high, so gynecologic surveillance and counseling about hysterectomy are part of managing this PTEN-driven syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — Cowden syndrome silences FOXO by unleashing AKT: PTEN normally restrains AKT, so its loss lets AKT shut down FOXO transcription factors that would trigger apoptosis and cell-cycle arrest—removing a brake and letting hamartomas and cancers grow.
- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — Some Cowden-like patients carry SDHB instead of PTEN: a subset with the classic features but no PTEN mutation have variants in mitochondrial SDHB/SDHD, so testing these genes helps explain PTEN-negative cases and refines cancer risk.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Cowden syndrome warps cerebellar neurons in Lhermitte-Duclos disease: PTEN loss drives a hamartomatous overgrowth of dysplastic neurons in the cerebellum, the nervous-system hallmark that, with macrocephaly, points to the diagnosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Cowden syndrome raises the risk of kidney cancer: PTEN loss unleashes the PI3K-mTOR growth axis in renal cells too, so renal cell carcinoma joins breast, thyroid and uterine cancers in the surveillance these patients need.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — PTEN loss in Cowden drives VEGF and abnormal vessels: with the PI3K-mTOR brake gone, cells overproduce VEGF, fueling the vascular malformations and the blood supply of the hamartomas and tumors the syndrome spawns.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Cowden's hamartomas are overgrowths shaped by TGF-beta: unchecked PTEN-pathway signaling with TGF-beta drives the fibrous proliferation behind the skin trichilemmomas, oral papillomas and intestinal hamartomas that define the syndrome.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^bubien-2013-cowden-cancer-risk]: Bubien V, Bonnet F, Brouste V, et al. High cumulative risks of cancer in patients with PTEN hamartoma tumour syndrome. *J Med Genet.* 2013;50(4):255-263. [doi:10.1136/jmedgenet-2012-101339](https://doi.org/10.1136/jmedgenet-2012-101339) · [PubMed 23335809](https://pubmed.ncbi.nlm.nih.gov/23335809/)
[^bennett-2010-klln-cowden]: Bennett KL, Mester J, Eng C. Germline epigenetic regulation of KILLIN in Cowden and Cowden-like syndrome. *JAMA.* 2010;304(24):2724-2731. [doi:10.1001/jama.2010.1877](https://doi.org/10.1001/jama.2010.1877) · [PubMed 21177507](https://pubmed.ncbi.nlm.nih.gov/21177507/)
