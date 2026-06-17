---
schema: human-scale-entry/v1
id: werner-syndrome
name: Werner Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Werner syndrome is caused by biallelic WRN mutations; premature aging onset in 3rd decade — cataracts, scleroderma-like skin, gray hair, type 2 diabetes, dyslipidemia, osteoporosis, atherosclerosis; cancer risk elevated (sarcomas, melanoma, thyroid); median survival ~47-54 years."
aliases: ["Werner syndrome", "Werner's syndrome", "Werner progeroid syndrome", "WRN syndrome", "adult progeria", "Werner syndrome WRN", "premature aging Werner", "Werner syndrome cancer", "RECQL2 Werner syndrome"]
sources:
  - id: yu-1996-wrn
    type: peer-reviewed
    cite: "Yu CE, Oshima J, Fu YH, et al. Positional cloning of the Werner's syndrome gene. Science. 1996;272(5259):258-262."
    doi: "10.1126/science.272.5259.258"
    pmid: "8602509"
    url: "https://doi.org/10.1126/science.272.5259.258"
  - id: lauper-2013-wrn-neoplasia
    type: peer-reviewed
    cite: "Lauper JM, Krause A, Vaughan TL, Monnat RJ Jr. Spectrum and risk of neoplasia in Werner syndrome: a systematic review. PLoS One. 2013;8(4):e59709."
    doi: "10.1371/journal.pone.0059709"
    pmid: "23579047"
    url: "https://doi.org/10.1371/journal.pone.0059709"
cross_links:
  - target: 01-human/03-molecular/wrn
    relation: connects-to
    note: "Biallelic WRN LOF causes Werner syndrome via unchecked G-quadruplex accumulation, replication fork collapse, and telomere attrition; premature aging features appear in the 3rd decade; cancer risk predominantly mesenchymal (sarcomas); median survival ~47 years."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Accelerated telomere attrition in Werner syndrome fibroblasts due to WRN LOF → TERT cannot elongate G-quadruplex-obstructed telomeres → critically short telomeres → replicative senescence → progeroid cell behavior; WRN and TERT cooperate at telomeres to enable their maintenance."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Werner syndrome features early-onset type 2 diabetes (~50-75% of patients) due to adipose redistribution and insulin resistance; dyslipidemia (hypertriglyceridemia, low HDL) is also characteristic; T2DM is treated with standard glucose-lowering agents and lifestyle modification."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Werner syndrome causes early-onset osteoporosis from ~30s (generalized cortical bone loss, vertebral compression fractures); mechanism: premature osteoblast senescence via WRN LOF → reduced bone formation; managed with bisphosphonates, calcium, vitamin D supplementation."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Werner syndrome fibroblasts are a classic cellular model of aging: lacking WRN helicase they senesce after only ~20 population doublings (vs ~60 normal), accumulate chromosomal rearrangements, and pour out a senescence-associated secretory phenotype that ages surrounding tissue."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Bilateral posterior subcapsular cataracts develop in nearly all Werner patients by their 30s — decades before age-related cataracts — and are often the presenting sign that should trigger WRN testing; they are managed with routine phacoemulsification and lens implantation."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Accelerated atherosclerosis is the leading killer in Werner syndrome, producing myocardial infarction and stroke roughly 30 years early, compounded by the syndrome's diabetes and dyslipidemia; aggressive statins, antihypertensives, and antiplatelet therapy begin in the 30s."
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "Werner, Bloom, and Rothmund-Thomson are the three RecQ-helicase disorders — WRN, BLM, and RECQL4 loss — all causing genomic instability and cancer; but Werner is the 'adult progeria,' with premature aging, atherosclerosis, and diabetes from the third decade, unlike the others."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Werner syndrome cancers are characteristically mesenchymal: osteosarcoma and soft-tissue sarcomas occur at elevated rates (alongside thyroid cancer and acral melanoma), reflecting WRN-deficient replication stress in mesenchyme — a spectrum shared with Rothmund-Thomson."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Thyroid cancer is the most common malignancy in Werner syndrome (often follicular), part of its distinctive non-epithelial-skewed tumor spectrum (sarcomas, melanoma, meningioma); WRN-deficient genomic instability drives these, warranting thyroid surveillance from early adulthood."
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "Werner and Rothmund-Thomson are RecQ-helicase disorders of premature aging: WRN loss causes adult-onset progeroid features (cataracts, atherosclerosis, diabetes), while RECQL4 loss causes Rothmund-Thomson—both genome-instability syndromes raising sarcoma risk."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Werner syndrome shifts the cancer spectrum toward rare tumors including melanoma: WRN-driven genome instability predisposes to soft-tissue sarcomas, thyroid cancer, and notably acral-lentiginous melanoma of the palms, soles, and nasal mucosa rather than sun-exposed sites."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Meningioma is over-represented in Werner syndrome: loss of WRN helicase leaves cells unable to resolve replication stress and telomere attrition, accumulating the genomic instability that seeds tumors like meningioma decades earlier than in the general population."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Werner and Li-Fraumeni both predispose to multiple cancers via different failures: Werner's WRN helicase loss causes genomic instability and rare sarcomas/melanoma, while Li-Fraumeni's TP53 loss removes the genome's guardian—instability versus checkpoint failure."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Werner syndrome accelerates the cellular senescence that CDKN2A governs: WRN helicase loss causes replicative stress and telomere attrition, so cells hit p16/CDKN2A senescence early—driving premature aging, while CDKN2A loss instead enables its cancers."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Werner syndrome is a model of premature cardiovascular aging: WRN loss accelerates atherosclerosis, so myocardial infarction and stroke are leading causes of death by the third-to-fifth decades—a monogenic window onto how cellular aging drives cardiovascular disease."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Werner syndrome is accelerated aging from genome instability overwhelming p53: WRN helicase loss lets DNA damage and telomere attrition accumulate, triggering premature senescence and cancer—so the p53 checkpoint fires early, aging the body decades ahead of time."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Werner syndrome's skin mimics scleroderma and aging: WRN loss produces tight, atrophic, scleroderma-like skin with ulcers over pressure points and graying hair in early adulthood—often the first visible sign of this segmental progeroid syndrome."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Werner syndrome drives premature fibrosis and connective-tissue aging: defective DNA repair pushes fibroblasts into senescence, and the resulting tissue stiffening underlies its scleroderma-like skin and atherosclerosis—aging at the connective-tissue level."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Werner's WRN helicase is now a cancer drug target: MSI-high tumors—many colorectal—depend on WRN to survive their unstable DNA, so WRN inhibitors are synthetically lethal in them, turning a premature-aging gene into precision oncology."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Werner syndrome distorts fat tissue: patients lose subcutaneous fat yet accumulate visceral fat, with insulin-resistant adipocytes driving severe type 2 diabetes and lipid abnormalities—part of the metabolic face of accelerated aging."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Werner syndrome prematurely ages the musculoskeletal system: muscle wasting, tight scleroderma-like skin over joints, soft-tissue calcification, and osteoporosis cause early frailty—mirroring the sarcopenia and bone loss of normal aging decades early."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Werner syndrome is a genome-instability disorder signaled by ATM: the missing WRN helicase leaves DNA replication and repair error-prone, generating the breaks ATM senses—accelerating the cellular aging and cancer risk that define adult progeria."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Werner syndrome causes severe insulin-resistant diabetes: visceral fat accumulation and a lipodystrophy-like pattern blunt insulin action, making type 2 diabetes a hallmark of this premature-aging syndrome from early adulthood."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Werner syndrome accelerates the mTOR-senescence axis of aging: WRN-deficient cells enter premature senescence, and chronically active mTOR signaling drives the aged phenotype—linking this progeria to the pathway whose inhibition (rapamycin) extends lifespan in models."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Werner syndrome is a replication-repair disease tied to RAD51: the WRN helicase resolves stalled forks and aids RAD51-driven homologous recombination, so its loss leaves the genomic instability behind the premature aging and cancers."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Werner cells age fast under oxygen's damage: without WRN, accumulating oxidative DNA damage and reactive oxygen species speed cellular senescence, contributing to the accelerated aging that defines this adult progeria."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Werner syndrome stiffens the skin's collagen: a scleroderma-like tightening with loss of subcutaneous fat and intractable ankle ulcers reflects disordered collagen and fibroblast aging, a hallmark physical sign of the disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Werner syndrome ages the heart early: premature, severe atherosclerosis leads to heart attacks in the patients' forties—one of the two leading causes of death, alongside cancer, in this accelerated-aging disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Werner syndrome calcifies soft tissues and vessels: disordered repair and aging promote arterial and soft-tissue calcification, contributing to the early atherosclerosis and the stiff, aged appearance of affected tissues."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Werner syndrome thins bone through failing osteoblasts: accelerated cellular aging impairs the bone-building cells, producing the early, severe osteoporosis—especially of the limbs—that is a hallmark of the disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Werner syndrome ages the vessel lining: senescent, repair-deficient endothelial cells lose their protective function, driving the premature atherosclerosis and arteriosclerosis that make heart attack a leading cause of death."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Diabetes is a hallmark of Werner syndrome: tied to its lipodystrophy and accelerated aging, the pancreas faces severe insulin resistance, so glucose intolerance and diabetes mellitus appear early in affected patients."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Werner's genomic instability reaches the blood-forming marrow: failing DNA repair raises the risk of myelodysplastic syndrome and myeloid leukemias, part of the syndrome's broad, early predisposition to cancer."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons reveal Werner's premature aging: slit-lamp light catches the early bilateral cataracts, and imaging shows the soft-tissue and vascular calcifications — including the classic Achilles tendon deposits — that mark this adult progeria."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Werner shifts the cancer spectrum toward the gut and beyond: alongside its trademark rare mesenchymal tumors, it raises colorectal cancer risk, so the large intestine joins the broad early-onset malignancy that shadows the syndrome."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Werner's metabolic derangement burdens the liver: the severe insulin resistance and diabetes that come with its accelerated aging drive fatty liver disease, part of the early metabolic syndrome that defines the disorder."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Werner patients never get their growth spurt: short stature is an early sign, the missing adolescent surge of growth-hormone-driven bone growth leaving adults strikingly small — one of the first clues that aging has gone awry."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "The gonads age early too: Werner syndrome brings hypogonadism with testicular or ovarian atrophy and reduced fertility, dropping sex-hormone output as part of the body-wide premature aging."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Werner's cells age fast in the dish: fibroblasts from patients hit replicative senescence early, and electron microscopy shows the enlarged, granular, senescent morphology that made the syndrome a model for studying human aging."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The genomic chaos is visible by antibody: WRN-deficient cells accumulate DNA double-strand breaks, and γH2AX antibody staining lights up the foci of damage and senescence that underlie Werner's premature aging and cancer-proneness."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The marrow ages and falters too: Werner syndrome carries a raised risk of myelodysplastic syndrome, whose ineffective hematopoiesis stalls erythrocyte production into the anemia that can mark the marrow's premature decline."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Premature marrow failure reaches the white cells: the myelodysplasia and leukemias that Werner syndrome predisposes to drop neutrophil counts, adding infection risk to the syndrome's long catalogue of accelerated aging."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Aging arrives early at the gonads: Werner syndrome brings hypogonadism and reduced fertility, the reproductive system winding down prematurely alongside the graying hair, cataracts and skin changes that mark the accelerated aging."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The vessel walls age fast: WRN loss drives premature senescence of vascular smooth-muscle cells, accelerating the atherosclerosis and medial calcification that make heart attacks a leading cause of early death in Werner syndrome."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Werner has a striking thyroid-cancer profile: the syndrome markedly raises thyroid cancer risk — especially follicular subtypes, and notably in reported Japanese cohorts — so the gland is watched as part of its broad cancer predisposition."
  - target: 01-human/03-molecular/recql4
    relation: connects-to
    note: "It belongs to a family of broken helicases: WRN is one of the RecQ DNA helicases, kin to RECQL4 (mutated in Rothmund-Thomson) and BLM, so losing it cripples the same genome-maintenance machinery, explaining why these syndromes share instability and cancer risk."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its skin will not knit: chronic, deep ulcers around the ankles and elbows are a hallmark of Werner, as failing fibroblasts and aged tissue cripple wound healing, producing sores that resist closure for years."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Aging cells stew the body in inflammation: senescent fibroblasts pour out a secretory phenotype that activates macrophages into chronic 'inflammaging', fueling the atherosclerosis, diabetes and poor wound healing that mark the premature-aging syndrome."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is the master switch behind that inflammation: it is the transcription factor that drives the senescence-associated secretory phenotype, so WRN loss accelerates senescence and tips NF-κB toward the chronic inflammatory output of Werner."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 amplifies the senescent secretome: responding to the IL-6 that senescent Werner cells release, STAT3 signaling helps sustain the inflammatory loop that propagates premature aging through the tissues."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Aged vessels and inactivity invite clots: Werner's accelerated atherosclerosis, leg ulcers and reduced mobility combine into a prothrombotic state that raises the risk of deep-vein thrombosis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Premature atherosclerosis reaches the brain: the accelerated vascular aging of Werner syndrome drives early cerebrovascular disease, making ischemic stroke — alongside myocardial infarction — a leading cause of its shortened lifespan."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The aged heart fails early: decades-premature coronary atherosclerosis and ischemic damage in Werner syndrome lead to early myocardial infarction and heart failure, the cardiovascular disease that is its commonest cause of death."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Genome instability courts the marrow: the WRN helicase defect predisposes Werner patients to myelodysplastic syndromes and other myeloid neoplasms, part of the broad cancer spectrum its impaired DNA repair produces."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its faulty DNA repair can tip into acute leukemia: beyond myelodysplasia, the genome instability of Werner syndrome raises the risk of acute myeloid leukemia, completing a myeloid-malignancy spectrum driven by WRN loss."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Its chronic ankle ulcers get colonized and infected: the intractable, slow-healing skin ulcers over the ankles and feet that typify Werner syndrome are readily invaded by Staphylococcus aureus, risking cellulitis and deep infection."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Premature aging and disfigurement weigh on mood: the early greying, cataracts, skin changes and the awareness of accelerated aging and cancer risk in Werner syndrome contribute to depression and impaired quality of life."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It ages and tightens the skin early: Werner syndrome produces sclerodermatous taut skin, premature greying and hair loss, subcutaneous atrophy and the intractable ankle ulcers that are diagnostic hallmarks."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It disturbs several endocrine axes at once: Werner syndrome characteristically brings insulin-resistant diabetes, hypogonadism with early menopause, and a raised rate of thyroid disease and cancer."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Accelerated aging and cancer risk breed worry: the visible premature ageing, multiple comorbidities and elevated malignancy risk of Werner syndrome foster chronic health anxiety alongside depression."
---

# Werner Syndrome

## Overview

**Werner syndrome (WS)** is a rare autosomal recessive **progeroid syndrome** (premature aging condition) caused by biallelic loss-of-function mutations in the **WRN** gene (8p12), encoding a RecQ family helicase/exonuclease that resolves G-quadruplex DNA structures, protects stalled replication forks, and maintains telomere integrity. Werner syndrome was first described by Otto Werner in 1904 and clinically defined as an adult-onset progeroid syndrome — in contrast to Hutchinson-Gilford progeria (LMNA mutation, childhood onset). The WRN gene was positionally cloned by Yu et al. in 1996. WS is characterized by the **appearance of multiple age-related diseases simultaneously in the 3rd-5th decades of life**: bilateral cataracts, scleroderma-like skin changes, premature graying and hair loss, hypogonadism, short stature, and a characteristic metabolic triad of type 2 diabetes, dyslipidemia, and accelerated atherosclerosis. Cardiovascular disease (~50% of deaths) and cancer (~30% of deaths) are the primary causes of mortality; **median survival is ~47-54 years** (mean age at death has improved somewhat with modern cardiovascular medicine). The cancer spectrum is unusual: predominantly **mesenchymal tumors** (sarcomas, meningiomas) rather than the carcinomas typical of most cancer predisposition syndromes. Worldwide prevalence is ~1 in 200,000; Japan has the highest reported prevalence (~1 in 100,000 due to a founder mutation) [^yu-1996-wrn] [^lauper-2013-wrn-neoplasia].

**Werner syndrome vs. other progeroid syndromes:**

| Feature | Werner Syndrome (WRN) | Hutchinson-Gilford Progeria (LMNA) | Bloom Syndrome (BLM) |
|---|---|---|---|
| Inheritance | AR | AD (de novo) | AR |
| Onset | 3rd-4th decade | Childhood (1-2 years) | Childhood |
| Cataracts | Yes (bilateral, posterior) | Not typical | Not typical |
| Cancer risk | Sarcomas, melanoma, thyroid | Low (die from CVD) | ALL, lymphoma, GI carcinoma |
| Cardiovascular | Atherosclerosis, MI | Vascular disease, MI | Mild |
| Diabetes | Yes (~70%) | No | Rare |
| Skin | Scleroderma-like, ulcers | Lipodystrophy, aged skin | Sun-sensitive, telangiectasia |
| Median survival | ~47-54 years | ~13 years | ~26 years |

## Structure

### Genetic basis of Werner syndrome

**WRN gene (8p12):**
- 35 exons; 1,432 aa; 162 kDa; ubiquitously expressed with highest levels in proliferating tissues
- All disease-causing WRN germline mutations produce truncated proteins lacking the C-terminal nuclear localization signal (NLS) → cytoplasmic retention → loss of nuclear function → the functional equivalent of null
- Most common Japanese founder mutation: 4-bp deletion at IVS25-IVS26 junction (c.3139-1G→C splice site; resulting in premature stop) — accounts for ~60% of Japanese WS cases
- Other common mutations: nonsense, frameshift throughout the gene; invariably result in NLS loss
- Over 80 distinct WRN mutations identified worldwide; no hotspot outside of founder mutations

**Penetrance and prevalence:**
- Biallelic WRN LOF → Werner syndrome with nearly complete penetrance (>95%); phenotypic severity varies by age, lifestyle, and modifier genes
- Carrier frequency: ~1/150-200 in Japan; ~1/500-1000 globally
- Heterozygous WRN carriers (parents of WS patients): no WS features; some studies suggest modestly elevated age-related disease risk — not clinically actionable

### Cellular and molecular pathology

**Hallmarks of Werner syndrome cells:**
- **Premature replicative senescence**: WS fibroblasts senesce after ~20 population doublings (vs ~60 for normal); this is the WRN LOF cellular phenotype
- **Elevated sister chromatid exchanges (SCE)**: ~2-3x elevated vs normal (less dramatic than Bloom syndrome, where SCE are 10x elevated); distinguishable from BLM by this quantitative difference
- **Chromosomal instability**: large deletions, inversions, translocations; "variegated translocation mosaicism" pattern of chromosomal abnormalities characteristic of WS
- **G-quadruplex (G4) accumulation**: G4 structures persist at telomeres, rDNA, and oncogene promoters → replication stalling → fork collapse → DSBs
- **Elevated SASP** (senescence-associated secretory phenotype): IL-6, IL-1β, TNF-α, MMP3 secreted by senescent WS cells → chronic inflammatory microenvironment → tissue aging acceleration

## Function

### Clinical features of Werner syndrome

**Age of onset and diagnostic timeline:**
- Childhood: normal development (distinguishes WS from HGPS); may have slightly short stature in adolescence
- ~20-30 years: first clinical signs — bilateral posterior subcapsular cataracts (often presenting feature), premature graying and hair loss, high-pitched voice (laryngeal changes), facial skin tightening, short stature (if not already apparent)
- ~30-40 years: scleroderma-like skin changes (skin atrophy, hyperkeratosis, ulcers around ankles/feet); T2DM; hypogonadism; dyslipidemia; osteosarcoma/sarcoma risk increases
- ~40-50 years: cardiovascular events (MI, stroke) — leading cause of mortality; continued cancer risk; renal disease (atherosclerotic)

**Bilateral cataracts (~100% of WS patients by 40y):**
- Posterior subcapsular cataracts developing in late 20s-30s (much earlier than age-related cataracts in general population which peak in 60s-70s)
- Managed identically to age-related cataracts: phacoemulsification + IOL implantation; excellent visual outcomes after surgery
- Cataracts are one of the most consistent and early diagnostic features; should trigger WRN genetic testing in a young adult

**Scleroderma-like skin:**
- Skin atrophy, loss of subcutaneous fat, pigmentation changes (hypo- and hyperpigmented areas); hyperkeratosis over pressure points
- **Chronic skin ulcers**: characteristic perimalleolar (around ankles) and plantar ulcers from ischemia (small vessel atherosclerosis) and pressure; can be severe, requiring wound care; may necessitate amputation
- Bird-like facies: beaked nose, retrognathia, sunken cheeks — from subcutaneous fat loss and skin tightening
- Hard to distinguish from early systemic sclerosis (scleroderma) clinically; WRN gene testing required

**Hypogonadism and reproductive features:**
- Both males (testicular atrophy, azoospermia) and females (premature ovarian failure, early menopause ~30s); infertility is very common
- Short stature: mean height ~155 cm for males, ~148 cm for females; pubertal growth spurt may be absent or blunted

**Voice change:**
- High-pitched, hoarse voice; due to laryngeal and vocal cord changes; distinctive clinical finding prompting WS consideration

### Cancer risk in Werner syndrome

**Cancer spectrum (from Lauper 2013 systematic review of 275 neoplasms in WS patients):**
- Soft tissue and bone sarcomas: ~25% of all WS cancers (osteosarcoma, malignant fibrous histiocytoma, fibrosarcoma, leiomyosarcoma, liposarcoma)
- Thyroid carcinoma (all types): ~13%
- Melanoma: ~6%
- Meningioma: ~6%
- Other: leukemia, lymphoma, liver cancer, bladder cancer — each ~2-5%
- Notably low carcinoma risk (breast, lung, colorectal) — opposite of BRCA1/2 and Lynch syndrome

**Why mesenchymal tumors?**
- WRN LOF generates large chromosomal rearrangements (deletions, translocations) rather than point mutations; chromosomal instability drives mesenchymal transformation
- Mesenchymal cells (fibroblasts, osteoblasts, adipocytes) may be particularly dependent on WRN for replication fidelity given their chromatin organization and G4 distribution

**Cancer surveillance in WS:**
- Annual dermatological exam (melanoma)
- Annual thyroid ultrasound (thyroid carcinoma)
- Musculoskeletal evaluation for bone/soft tissue sarcoma if symptoms (pain, mass)
- No established efficacy screening protocol for WS (rare syndrome; no RCT data)
- If cancer develops: standard-of-care treatment; special consideration: Werner syndrome cells may have altered DNA damage response → inform chemotherapy/radiation sensitivity

### Metabolic features

**Type 2 diabetes mellitus (~50-90% of WS patients):**
- Central lipodystrophy + peripheral fat atrophy → relative insulin resistance → T2DM; islet function initially preserved; eventually β-cell exhaustion in some
- Onset typically 30s-40s; managed as T2DM: metformin (first-line; also has anti-aging properties via AMPK), GLP-1 agonists, insulin if needed
- Hypoglycemia risk if insulin used (given concurrent cardiovascular disease and renal disease)

**Dyslipidemia:**
- Hypertriglyceridemia (often severe; may cause pancreatitis); low HDL cholesterol; LDL may be modestly elevated but often normal — the atherogenic profile is predominantly TG/HDL-based
- Treatment: statins, fibrates, omega-3 fatty acids; statin use also reduces cardiovascular events (primary prevention indication from ~30s in WS)

**Atherosclerosis:**
- Accelerated severe coronary, cerebral, peripheral arterial atherosclerosis; MI and stroke occur ~30 years earlier than in the general population
- Valvular heart disease (aortic sclerosis/stenosis) also reported
- Management: aggressive risk factor control (statin, antihypertensives, antiplatelet agents); revascularization as needed; antiplatelet therapy from ~30s

**Osteoporosis:**
- Generalized cortical and trabecular bone loss; vertebral compression fractures from 30s-40s; premature osteoblast senescence (WRN LOF in osteoblast precursors → reduced osteoblast lifespan → less bone formed)
- DEXA scan from diagnosis; bisphosphonates (alendronate, zoledronate) + calcium + vitamin D supplementation; annual fracture risk assessment

## Pathology

### Diagnosis

**Diagnostic criteria (Goto revised 2013):**

**Obligatory criteria (all 4 required):**
1. Bilateral cataracts
2. Characteristic skin changes ≥1: bird-like facies; scleroderma-like skin; atrophic skin; ulcerations; keratosis; regional subcutaneous calcification
3. Short stature
4. Premature aging of hair: prematurely gray and/or sparse hair; alopecia

**Additional signs (2+ further support diagnosis):**
5. Type 2 diabetes mellitus
6. Hypogonadism
7. Osteoporosis
8. Soft tissue calcification
9. Abnormal voice (high-pitched, hoarse)
10. Flat feet
11. Family history (affected sibling)
12. Positive WRN genetic test

**Definite WS**: obligatory criteria 1-4 + 2 or more additional signs
**Probable WS**: cataracts + 2 additional signs
**Possible WS**: cataracts OR 2 or more additional signs without cataracts

**Genetic testing:**
- WRN sequencing + MLPA (multiplex ligation-dependent probe amplification for large deletions); panel testing often efficient
- Most cases diagnosed in 3rd decade when multiple features co-occur; some are diagnosed by ophthalmologist (cataracts first)

**Differential diagnosis:**
- Hutchinson-Gilford progeria (LMNA): childhood onset, no cataracts, more severe cardiovascular disease in teens; LMNA sequencing
- Rothmund-Thomson syndrome (RECQL4): poikiloderma (mottled red-white skin), cataracts, skeletal abnormalities; childhood onset; RECQL4 testing
- Mandibuloacral dysplasia (LMNA or ZMPSTE24): lipodystrophy, skeletal dysplasia
- Systemic sclerosis (scleroderma): ANA+, specific SSc autoantibodies (anti-Scl-70, anti-centromere); younger onset Werner can mimic SSc
- Cockayne syndrome (ERCC8/ERCC6): UV-sensitive, neurological, shorter; predominantly skin/neurological
- Progeroid laminopathies: BANF1, LEMD3 variants; milder; neurological features variable

**Multidisciplinary management:**
- Ophthalmology: annual eye exam; phacoemulsification for cataracts
- Endocrinology: T2DM, dyslipidemia, hypogonadism management
- Cardiology: risk factor management; echo annually; stress testing in symptomatic patients
- Dermatology: wound care for perimalleolar ulcers; melanoma surveillance
- Orthopedics: osteoporosis management; fracture repair
- Genetics: family counseling; cascade testing for siblings (25% recurrence risk)
- Registry: Werner Syndrome Registry (University of Washington, Seattle) — research coordination

## Connections

- `connects-to` → **[WRN](../../03-molecular/wrn/README.md)** — Biallelic WRN LOF causes Werner syndrome via unchecked G-quadruplex accumulation, replication fork collapse, and telomere attrition; premature aging features appear in the 3rd decade; cancer risk predominantly mesenchymal (sarcomas); median survival ~47 years.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Accelerated telomere attrition in Werner syndrome fibroblasts due to WRN LOF → TERT cannot elongate G-quadruplex-obstructed telomeres → critically short telomeres → replicative senescence → progeroid cell behavior; WRN and TERT cooperate at telomeres to enable their maintenance.
- `connects-to` → **[Type 2 Diabetes](../../07-system/type-2-diabetes/README.md)** — Werner syndrome features early-onset type 2 diabetes (~50-75% of patients) due to adipose redistribution and insulin resistance; dyslipidemia (hypertriglyceridemia, low HDL) is also characteristic; T2DM is treated with standard glucose-lowering agents and lifestyle modification.
- `connects-to` → **[Osteoporosis](../../07-system/osteoporosis/README.md)** — Werner syndrome causes early-onset osteoporosis from ~30s (generalized cortical bone loss, vertebral compression fractures); mechanism: premature osteoblast senescence via WRN LOF → reduced bone formation; managed with bisphosphonates, calcium, vitamin D supplementation.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Werner syndrome fibroblasts are a classic cellular model of aging: lacking WRN helicase they senesce after only ~20 population doublings (vs ~60 normal), accumulate chromosomal rearrangements, and pour out a senescence-associated secretory phenotype that ages surrounding tissue.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Bilateral posterior subcapsular cataracts develop in nearly all Werner patients by their 30s — decades before age-related cataracts — and are often the presenting sign that should trigger WRN testing; they are managed with routine phacoemulsification and lens implantation.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Accelerated atherosclerosis is the leading killer in Werner syndrome, producing myocardial infarction and stroke roughly 30 years early, compounded by the syndrome's diabetes and dyslipidemia; aggressive statins, antihypertensives, and antiplatelet therapy begin in the 30s.
- `connects-to` → **[Bloom Syndrome](../bloom-syndrome/README.md)** — Werner, Bloom, and Rothmund-Thomson are the three RecQ-helicase disorders — WRN, BLM, and RECQL4 loss — all causing genomic instability and cancer; but Werner is the 'adult progeria,' with premature aging, atherosclerosis, and diabetes from the third decade, unlike the others.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Werner syndrome cancers are characteristically mesenchymal: osteosarcoma and soft-tissue sarcomas occur at elevated rates (alongside thyroid cancer and acral melanoma), reflecting WRN-deficient replication stress in mesenchyme — a spectrum shared with Rothmund-Thomson.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Thyroid cancer is the most common malignancy in Werner syndrome (often follicular), part of its distinctive non-epithelial-skewed tumor spectrum (sarcomas, melanoma, meningioma); WRN-deficient genomic instability drives these, warranting thyroid surveillance from early adulthood.
- `connects-to` → **[Rothmund-Thomson Syndrome](../rothmund-thomson/README.md)** — Werner and Rothmund-Thomson are RecQ-helicase disorders of premature aging: WRN loss causes adult-onset progeroid features (cataracts, atherosclerosis, diabetes), while RECQL4 loss causes Rothmund-Thomson—both genome-instability syndromes raising sarcoma risk.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Werner syndrome shifts the cancer spectrum toward rare tumors including melanoma: WRN-driven genome instability predisposes to soft-tissue sarcomas, thyroid cancer, and notably acral-lentiginous melanoma of the palms, soles, and nasal mucosa rather than sun-exposed sites.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Meningioma is over-represented in Werner syndrome: loss of WRN helicase leaves cells unable to resolve replication stress and telomere attrition, accumulating the genomic instability that seeds tumors like meningioma decades earlier than in the general population.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Werner and Li-Fraumeni both predispose to multiple cancers via different failures: Werner's WRN helicase loss causes genomic instability and rare sarcomas/melanoma, while Li-Fraumeni's TP53 loss removes the genome's guardian—instability versus checkpoint failure.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Werner syndrome accelerates the cellular senescence that CDKN2A governs: WRN helicase loss causes replicative stress and telomere attrition, so cells hit p16/CDKN2A senescence early—driving premature aging, while CDKN2A loss instead enables its cancers.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Werner syndrome is a model of premature cardiovascular aging: WRN loss accelerates atherosclerosis, so myocardial infarction and stroke are leading causes of death by the third-to-fifth decades—a monogenic window onto how cellular aging drives cardiovascular disease.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Werner syndrome is accelerated aging from genome instability overwhelming p53: WRN helicase loss lets DNA damage and telomere attrition accumulate, triggering premature senescence and cancer—so the p53 checkpoint fires early, aging the body decades ahead of time.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Werner syndrome's skin mimics scleroderma and aging: WRN loss produces tight, atrophic, scleroderma-like skin with ulcers over pressure points and graying hair in early adulthood—often the first visible sign of this segmental progeroid syndrome.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Werner syndrome drives premature fibrosis and connective-tissue aging: defective DNA repair pushes fibroblasts into senescence, and the resulting tissue stiffening underlies its scleroderma-like skin and atherosclerosis—aging at the connective-tissue level.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Werner's WRN helicase is now a cancer drug target: MSI-high tumors—many colorectal—depend on WRN to survive their unstable DNA, so WRN inhibitors are synthetically lethal in them, turning a premature-aging gene into precision oncology.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Werner syndrome distorts fat tissue: patients lose subcutaneous fat yet accumulate visceral fat, with insulin-resistant adipocytes driving severe type 2 diabetes and lipid abnormalities—part of the metabolic face of accelerated aging.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Werner syndrome prematurely ages the musculoskeletal system: muscle wasting, tight scleroderma-like skin over joints, soft-tissue calcification, and osteoporosis cause early frailty—mirroring the sarcopenia and bone loss of normal aging decades early.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — Werner syndrome is a genome-instability disorder signaled by ATM: the missing WRN helicase leaves DNA replication and repair error-prone, generating the breaks ATM senses—accelerating the cellular aging and cancer risk that define adult progeria.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Werner syndrome causes severe insulin-resistant diabetes: visceral fat accumulation and a lipodystrophy-like pattern blunt insulin action, making type 2 diabetes a hallmark of this premature-aging syndrome from early adulthood.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Werner syndrome accelerates the mTOR-senescence axis of aging: WRN-deficient cells enter premature senescence, and chronically active mTOR signaling drives the aged phenotype—linking this progeria to the pathway whose inhibition (rapamycin) extends lifespan in models.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — Werner syndrome is a replication-repair disease tied to RAD51: the WRN helicase resolves stalled forks and aids RAD51-driven homologous recombination, so its loss leaves the genomic instability behind the premature aging and cancers.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Werner cells age fast under oxygen's damage: without WRN, accumulating oxidative DNA damage and reactive oxygen species speed cellular senescence, contributing to the accelerated aging that defines this adult progeria.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Werner syndrome stiffens the skin's collagen: a scleroderma-like tightening with loss of subcutaneous fat and intractable ankle ulcers reflects disordered collagen and fibroblast aging, a hallmark physical sign of the disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Werner syndrome ages the heart early: premature, severe atherosclerosis leads to heart attacks in the patients' forties—one of the two leading causes of death, alongside cancer, in this accelerated-aging disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Werner syndrome calcifies soft tissues and vessels: disordered repair and aging promote arterial and soft-tissue calcification, contributing to the early atherosclerosis and the stiff, aged appearance of affected tissues.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Werner syndrome thins bone through failing osteoblasts: accelerated cellular aging impairs the bone-building cells, producing the early, severe osteoporosis—especially of the limbs—that is a hallmark of the disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Werner syndrome ages the vessel lining: senescent, repair-deficient endothelial cells lose their protective function, driving the premature atherosclerosis and arteriosclerosis that make heart attack a leading cause of death.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Diabetes is a hallmark of Werner syndrome: tied to its lipodystrophy and accelerated aging, the pancreas faces severe insulin resistance, so glucose intolerance and diabetes mellitus appear early in affected patients.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Werner's genomic instability reaches the blood-forming marrow: failing DNA repair raises the risk of myelodysplastic syndrome and myeloid leukemias, part of the syndrome's broad, early predisposition to cancer.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons reveal Werner's premature aging: slit-lamp light catches the early bilateral cataracts, and imaging shows the soft-tissue and vascular calcifications — including the classic Achilles tendon deposits — that mark this adult progeria.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Werner shifts the cancer spectrum toward the gut and beyond: alongside its trademark rare mesenchymal tumors, it raises colorectal cancer risk, so the large intestine joins the broad early-onset malignancy that shadows the syndrome.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Werner's metabolic derangement burdens the liver: the severe insulin resistance and diabetes that come with its accelerated aging drive fatty liver disease, part of the early metabolic syndrome that defines the disorder.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Werner patients never get their growth spurt: short stature is an early sign, the missing adolescent surge of growth-hormone-driven bone growth leaving adults strikingly small — one of the first clues that aging has gone awry.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — The gonads age early too: Werner syndrome brings hypogonadism with testicular or ovarian atrophy and reduced fertility, dropping sex-hormone output as part of the body-wide premature aging.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Werner's cells age fast in the dish: fibroblasts from patients hit replicative senescence early, and electron microscopy shows the enlarged, granular, senescent morphology that made the syndrome a model for studying human aging.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — The genomic chaos is visible by antibody: WRN-deficient cells accumulate DNA double-strand breaks, and γH2AX antibody staining lights up the foci of damage and senescence that underlie Werner's premature aging and cancer-proneness.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The marrow ages and falters too: Werner syndrome carries a raised risk of myelodysplastic syndrome, whose ineffective hematopoiesis stalls erythrocyte production into the anemia that can mark the marrow's premature decline.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Premature marrow failure reaches the white cells: the myelodysplasia and leukemias that Werner syndrome predisposes to drop neutrophil counts, adding infection risk to the syndrome's long catalogue of accelerated aging.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Aging arrives early at the gonads: Werner syndrome brings hypogonadism and reduced fertility, the reproductive system winding down prematurely alongside the graying hair, cataracts and skin changes that mark the accelerated aging.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The vessel walls age fast: WRN loss drives premature senescence of vascular smooth-muscle cells, accelerating the atherosclerosis and medial calcification that make heart attacks a leading cause of early death in Werner syndrome.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Werner has a striking thyroid-cancer profile: the syndrome markedly raises thyroid cancer risk — especially follicular subtypes, and notably in reported Japanese cohorts — so the gland is watched as part of its broad cancer predisposition.
- `connects-to` → **[RECQL4](../../03-molecular/recql4/README.md)** — It belongs to a family of broken helicases: WRN is one of the RecQ DNA helicases, kin to RECQL4 (mutated in Rothmund-Thomson) and BLM, so losing it cripples the same genome-maintenance machinery, explaining why these syndromes share instability and cancer risk.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its skin will not knit: chronic, deep ulcers around the ankles and elbows are a hallmark of Werner, as failing fibroblasts and aged tissue cripple wound healing, producing sores that resist closure for years.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Aging cells stew the body in inflammation: senescent fibroblasts pour out a secretory phenotype that activates macrophages into chronic 'inflammaging', fueling the atherosclerosis, diabetes and poor wound healing that mark the premature-aging syndrome.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the master switch behind that inflammation: it is the transcription factor that drives the senescence-associated secretory phenotype, so WRN loss accelerates senescence and tips NF-κB toward the chronic inflammatory output of Werner.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 amplifies the senescent secretome: responding to the IL-6 that senescent Werner cells release, STAT3 signaling helps sustain the inflammatory loop that propagates premature aging through the tissues.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Aged vessels and inactivity invite clots: Werner's accelerated atherosclerosis, leg ulcers and reduced mobility combine into a prothrombotic state that raises the risk of deep-vein thrombosis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Premature atherosclerosis reaches the brain: the accelerated vascular aging of Werner syndrome drives early cerebrovascular disease, making ischemic stroke — alongside myocardial infarction — a leading cause of its shortened lifespan.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The aged heart fails early: decades-premature coronary atherosclerosis and ischemic damage in Werner syndrome lead to early myocardial infarction and heart failure, the cardiovascular disease that is its commonest cause of death.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — Genome instability courts the marrow: the WRN helicase defect predisposes Werner patients to myelodysplastic syndromes and other myeloid neoplasms, part of the broad cancer spectrum its impaired DNA repair produces.
- `connects-to` → **[Acute Myeloid Leukemia](../aml/README.md)** — Its faulty DNA repair can tip into acute leukemia: beyond myelodysplasia, the genome instability of Werner syndrome raises the risk of acute myeloid leukemia, completing a myeloid-malignancy spectrum driven by WRN loss.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Its chronic ankle ulcers get colonized and infected: the intractable, slow-healing skin ulcers over the ankles and feet that typify Werner syndrome are readily invaded by Staphylococcus aureus, risking cellulitis and deep infection.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Premature aging and disfigurement weigh on mood: the early greying, cataracts, skin changes and the awareness of accelerated aging and cancer risk in Werner syndrome contribute to depression and impaired quality of life.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It ages and tightens the skin early: Werner syndrome produces sclerodermatous taut skin, premature greying and hair loss, subcutaneous atrophy and the intractable ankle ulcers that are diagnostic hallmarks.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It disturbs several endocrine axes at once: Werner syndrome characteristically brings insulin-resistant diabetes, hypogonadism with early menopause, and a raised rate of thyroid disease and cancer.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Accelerated aging and cancer risk breed worry: the visible premature ageing, multiple comorbidities and elevated malignancy risk of Werner syndrome foster chronic health anxiety alongside depression.

[^yu-1996-wrn]: Yu CE, Oshima J, Fu YH, et al. Positional cloning of the Werner's syndrome gene. *Science.* 1996;272(5259):258-262. [doi:10.1126/science.272.5259.258](https://doi.org/10.1126/science.272.5259.258) · [PubMed 8602509](https://pubmed.ncbi.nlm.nih.gov/8602509/)
[^lauper-2013-wrn-neoplasia]: Lauper JM, Krause A, Vaughan TL, Monnat RJ Jr. Spectrum and risk of neoplasia in Werner syndrome: a systematic review. *PLoS One.* 2013;8(4):e59709. [doi:10.1371/journal.pone.0059709](https://doi.org/10.1371/journal.pone.0059709) · [PubMed 23579047](https://pubmed.ncbi.nlm.nih.gov/23579047/)
