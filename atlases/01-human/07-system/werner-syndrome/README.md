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
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Premature metabolic disease reaches the liver: the visceral adiposity, dyslipidaemia and insulin resistance of Werner syndrome drive fatty liver disease as part of its accelerated-ageing metabolic syndrome."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is a disease of inflammaging: defective WRN genome maintenance raises chronic inflammatory cytokines that speed atherosclerosis and may erode immune surveillance against Werner's many cancers."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Accelerated vascular ageing reaches the brain: systemic premature atherosclerosis affects cerebral vessels, while high-frequency sensorineural hearing loss reflects the wider neural-ageing phenotype of Werner syndrome."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its metabolic and vascular ageing scars the kidney: the diabetes and premature atherosclerosis of Werner syndrome drive diabetic and renovascular nephropathy with declining renal function."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It predisposes to marrow cancers: Werner syndrome carries an increased risk of myelodysplastic syndrome and acute myeloid leukaemia arising in the bone marrow."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Its chronic ulcers invite infection: the intractable ankle and foot ulcers of Werner syndrome become colonised and infected, classically by Staphylococcus aureus, and heal poorly."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "Its early diabetes needs control: Werner syndrome causes insulin-resistant diabetes in early adulthood, managed with metformin as part of its accelerated metabolic ageing."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "Premature atherosclerosis demands lipid control: Werner syndrome brings early, severe atherosclerosis, and statins are used against the dyslipidaemia and vascular disease that often kill these patients young."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Antiplatelet cover follows the early arteries: the premature coronary and cerebrovascular disease of Werner syndrome prompts aspirin for secondary prevention, as in other accelerated-atherosclerosis states."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Its cancers need careful chemo: Werner syndrome predisposes to sarcomas, thyroid cancer and melanoma, but WRN-deficient cells are hypersensitive to DNA-crosslinking and topoisomerase agents, so chemotherapy must be dosed cautiously to limit toxicity."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It thins and warps bone: Werner syndrome causes early osteoporosis concentrated in the distal limbs, soft-tissue and tendon calcification, and a raised risk of osteosarcoma at unusual sites such as the patella and feet."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "The artery wall itself ages: beyond lipids, Werner syndrome thickens the intima and lays down medial and arteriolar calcification, the structural arterial-wall changes that make its atherosclerosis so premature and diffuse."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Its gene became a drug target: WRN-helicase inhibitors are synthetically lethal in microsatellite-unstable cancers that depend on WRN to survive their unstable DNA—turning the premature-aging gene of Werner syndrome into precision oncology."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Synthetic lethality meets mismatch repair: the MSI-high tumours that WRN inhibitors kill are largely the mismatch-repair-deficient cancers of Lynch syndrome, so Werner's helicase is the vulnerability that Lynch's genomic instability creates."
  - target: 01-human/05-tissue/islet-of-langerhans
    relation: connects-to
    note: "It brings a severe diabetes: Werner syndrome causes lipodystrophy and visceral fat that drive profound insulin resistance, overworking the islets of Langerhans into an early, hard-to-control type 2 diabetes."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "WRN as a drug target: WRN helicase is synthetically lethal in microsatellite-unstable cancers such as MSI-high endometrial and gastric tumours, so the very gene mutated in Werner syndrome is now a sought-after oncology target."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Premature heart death: accelerated atherosclerosis in Werner syndrome causes early myocardial infarction, and along with cancer it is one of the two leading causes of death in these patients in their fifties."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "An unusual tumour spectrum: Werner's genomic instability skews cancers toward mesenchymal types—soft-tissue sarcomas like synovial sarcoma and osteosarcoma—rather than the epithelial carcinomas of most cancer syndromes."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "Replication-fork repair: the WRN helicase works alongside the homologous-recombination machinery, so like BRCA1-deficient cells, Werner cells suffer replication stress and double-strand-break repair defects with potential PARP sensitivity."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Lipodystrophic metabolic disease: Werner syndrome strips subcutaneous fat while accumulating visceral fat, driving severe insulin resistance and hepatic steatosis that progresses to NASH alongside its diabetes."
  - target: 01-human/07-system/familial-hypercholesterolemia
    relation: connects-to
    note: "Two roads to early heart attacks: Werner syndrome causes premature atherosclerosis through accelerated cellular ageing, paralleling the early coronary disease of familial hypercholesterolaemia driven instead by lifelong high LDL."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle in cancer: the genomic instability of WRN loss with cell-cycle dysregulation (CDKN2A, cyclin D1) drives the diverse, often mesenchymal cancers of Werner syndrome."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Oncogene activation: MYC activation contributes to the sarcomas and other malignancies that arise from the genomic instability of Werner syndrome."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Metabolism and growth: PI3K-AKT-mTOR signalling links Werner syndrome's insulin resistance and diabetes to the growth signalling of its cancers."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Angiogenesis: VEGF drives the tumour angiogenesis of the sarcomas that arise in Werner syndrome and contributes to its accelerated atherosclerosis."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Fibroblast and vessel signalling: PDGF acting on the prematurely senescent fibroblasts and vascular smooth muscle of Werner syndrome contributes to its fibrosis and atherosclerosis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the cancers of Werner syndrome drives the angiogenesis and metabolic adaptation that support their growth."
  - target: 01-human/03-molecular/blm
    relation: connects-to
    note: "RecQ helicase family: WRN and BLM (Bloom syndrome) are sister RecQ helicases, so the loss of WRN in Werner syndrome parallels BLM loss — both cause genomic instability and cancer predisposition from failed replication-fork and recombination repair."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "Accelerated senescence: WRN loss leaves replication stress unresolved, triggering p21 (CDKN1A)-driven cell-cycle arrest and premature replicative senescence — a core mechanism of the accelerated-ageing phenotype of Werner syndrome."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Premature osteoporosis: severe osteoporosis, especially of the limbs, is a hallmark of Werner syndrome, reflecting the RANKL-driven osteoclast activity that outpaces bone formation in this accelerated-ageing disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Inflammaging: WRN-deficient cells accumulate micronuclei and cytosolic DNA that activate cGAS-STING, generating the chronic senescence-associated inflammatory secretome (SASP) that helps drive the accelerated tissue ageing of Werner syndrome."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Premature atherosclerosis: severe, early atherosclerosis is a leading cause of death in Werner syndrome, the cholesterol-laden arterial disease appearing decades early and compounded by the syndrome's dyslipidaemia and insulin resistance."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic syndrome: Werner syndrome is a classic model of hypoadiponectinaemia, where the loss of insulin-sensitising adiponectin from dysfunctional visceral fat underlies its severe insulin resistance and early type-2 diabetes."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammaging SASP: Werner cells undergo accelerated replicative senescence and adopt a senescence-associated secretory phenotype rich in IL-6, the chronic inflammation that drives the premature atherosclerosis and tissue ageing of the syndrome."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Genome-instability cell cycle: WRN-helicase loss causes replication stress that deregulates the RB-E2F1 cell-cycle checkpoint (with the CDKN2A and cyclin-D already mapped), pushing cells toward senescence and the cancer predisposition of Werner syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Energy-sensing dysfunction: the severe insulin resistance and metabolic derangement of Werner syndrome engage the AMPK energy-sensing pathway (the target of the metformin already mapped), part of its accelerated-ageing metabolic phenotype."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative overwhelm: chronic oxidative stress overwhelms NRF2 antioxidant defences in WRN-deficient cells, accelerating the DNA damage and cellular senescence that underlie the premature ageing of Werner syndrome."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammaging SASP: WRN-deficient senescent cells secrete a senescence-associated secretory phenotype rich in TNF-α (with IL-6 and NF-κB mapped), driving the chronic inflammation and atherosclerosis of Werner syndrome."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "Telomere maintenance: with telomerase (TERT mapped) insufficient against WRN-driven telomere dysfunction, the cancers of Werner syndrome — notably osteosarcoma — may engage the ATRX-associated alternative lengthening of telomeres."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammaging SASP: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped) drives the senescence-associated secretory phenotype and chronic inflammation ('inflammaging') that accelerates the premature aging of Werner syndrome."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Damage-driven inflammaging: NLRP3-inflammasome activation by the accumulating cellular damage of Werner syndrome contributes to the inflammaging underlying its premature atherosclerosis and metabolic disease."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Senescence-cancer balance: MDM2 regulation of p53 (already mapped) shapes the balance between senescence and apoptosis of genomically unstable cells and the cancer predisposition of Werner syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling is activated by the cytosolic DNA of senescent cells and contributes to the inflammatory, interferon-driven component of the premature ageing of Werner syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the tissue fibrosis and chronic inflammation that accompany the accelerated ageing phenotype of Werner syndrome."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling drives the premature atherosclerosis and fibrotic tissue remodelling characteristic of the accelerated ageing of Werner syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO longevity transcription factors govern the oxidative-stress resistance and senescence programs whose dysregulation accelerates the aging phenotype of Werner syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic clearance of senescent cells by NK and T cells is a surveillance axis whose failure lets senescent cells accumulate in Werner syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 is a senescence-associated secretory-phenotype alarmin that amplifies the chronic inflammaging underlying Werner syndrome tissue damage."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and metabolic signaling relevant to the accelerated cellular aging of Werner syndrome."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Dysregulated CDK4/6-cyclin-D activity (cyclin-D1 already mapped) contributes to the replicative-senescence dynamics and cancer predisposition of Werner syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling contributes to the mesenchymal-tumor (sarcoma) predisposition of Werner syndrome."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the genomically unstable cells and participates in the metabolic aging of Werner syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic-aging-clock alterations of Werner syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy declines with the cellular senescence of Werner syndrome, contributing to its premature-aging phenotype."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the inflammaging and tissue inflammation of Werner syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape accompanying the genomic instability of Werner syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven senescence-associated inflammation (inflammaging) participates in the premature-aging phenotypes of Werner syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the senescence-associated secretory and tumor-stromal interactions of Werner syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammaging and immune microenvironment of Werner syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the chronic inflammation (inflammaging) of Werner syndrome."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Premature atherosclerosis: Werner patients develop early, severe atherosclerosis that is a leading cause of death, with endothelial nitric-oxide dysfunction driving the accelerated vascular aging of this adult progeroid syndrome."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Accelerated osteoporosis: Werner syndrome causes early, characteristically distal-limb osteoporosis, and sclerostin, the osteocyte Wnt brake on bone formation, is central to the deficient bone accrual of this premature skeletal aging."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Insulin resistance: Werner syndrome features visceral adiposity and severe insulin resistance, and the adipokine resistin links the dysfunctional fat to the metabolic syndrome and diabetes (insulin already mapped) that mark its accelerated aging."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Premature myocardial infarction: the accelerated atherosclerosis of Werner syndrome (cholesterol/nitric oxide already mapped) causes myocardial infarction in the fourth to fifth decade, a leading cause of death, with troponin marking the cardiac injury."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Cancer immunosurveillance: Werner syndrome predisposes to a spectrum of cancers (melanoma, thyroid, sarcoma already mapped), and MHC class II-restricted T-cell surveillance influences which of these genome-instability-driven tumours emerge."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative aging: accumulation of oxidative damage accelerates the cellular senescence of Werner syndrome, and xanthine-oxidase-derived reactive oxygen species contribute to the redox stress that compounds its genome-instability-driven premature aging."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Inflammaging balance: the anti-inflammatory IL-10 counters the senescence-associated secretory phenotype (IL-6, TNF and IL-1 already mapped) of the many senescent cells in Werner syndrome, and this cytokine imbalance drives its inflammaging."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Metabolic dysfunction: the insulin-resistant diabetes (insulin already mapped) and visceral adiposity of Werner syndrome disturb the incretin GLP-1 axis, part of the accelerated metabolic ageing of the disorder."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammaging eicosanoids: prostaglandins from the chronic low-grade inflammation of senescent tissues contribute, with the cytokines already mapped, to the atherosclerosis and tissue dysfunction of the premature ageing of Werner syndrome."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine dysfunction: the abnormal fat distribution and metabolic ageing of Werner syndrome disturb the adipokine leptin (adiponectin and resistin already mapped), part of the insulin-resistant metabolic derangement of the disorder."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "Atherogenic lipids: the dyslipidaemia of Werner syndrome, in which PCSK9 regulates LDL clearance (cholesterol already mapped), contributes to the premature atherosclerosis that is a leading cause of death in the disorder."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth and ageing axis: the growth-hormone-IGF-1 axis (growth hormone already mapped) underlies the short stature of Werner syndrome, and the insulin/IGF-1 signalling that this axis feeds is central to the biology of ageing."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Senescence and SASP: IL-4 and the M2 arm (IL-10 already mapped) balance the senescence-associated secretory phenotype (TNF, IL-6 and IL-1 already mapped) of the accelerated cellular ageing of Werner syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 arm: IL-13, with IL-4 (already mapped), is part of the type-2 cytokine response whose balance against the pro-inflammatory SASP shapes the inflammatory ageing of Werner syndrome."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Cancer-therapy anaemia: the frequent sarcomas and other cancers of Werner syndrome and their chemotherapy cause anaemia (haemoglobin already mapped) needing transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Senescence interferon: the cGAS-STING (already mapped) sensing of the genomic instability and cytoplasmic DNA of the WRN-deficient (already mapped) senescent cells drives the type-I interferon and the SASP (IL-6 and TNF already mapped) of Werner syndrome."
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "RecQ-helicase sibling: Bloom syndrome (BLM already mapped), with Werner (WRN already mapped) and Rothmund-Thomson (already mapped), are the RecQ-helicase genome-instability syndromes sharing the DNA-repair defect and cancer predisposition."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Sarcoma predisposition: Werner syndrome (WRN already mapped) carries a high risk of sarcomas, notably the osteosarcoma (often at unusual sites), a leading cancer of the syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Immunosenescence: the NK cells (perforin already mapped) decline as part of the accelerated immunosenescence of the premature-aging phenotype of Werner syndrome."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Inflammaging Th1 arm: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the chronic 'inflammaging' (IL-6 and TNF already mapped) of Werner syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory dimension of the accelerated aging of Werner syndrome."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the accelerated aging of Werner syndrome."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic 'inflammaging' (IL-6 and TNF already mapped) of Werner syndrome."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of Werner syndrome."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Aged-skin mast cells: the mast cells of the atrophic, scleroderma-like skin contribute to the type-2 (IgE already mapped) and inflammaging (IL-6 and TNF already mapped) dimension of Werner syndrome."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 inflammaging source: the CD4 T-helper cells, with immunosenescence, are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the chronic inflammaging of Werner syndrome."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Immunosenescent antigen presentation: the dendritic cells, with the age-associated decline in function, present antigen to the T cells (already mapped) in the immune dysregulation of Werner syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Inflammaging complement: the complement C3 activation is part of the chronic low-grade innate inflammation (inflammaging) of the accelerated ageing of Werner syndrome."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the macrophage (already mapped) inflammation of the inflammaging of Werner syndrome."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immunosenescent surveillance: the cytotoxic T cells (perforin already mapped), with the age-associated exhaustion, provide the impaired surveillance of the senescent cells of Werner syndrome."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Inflammaging alarmin: TSLP from the senescent skin (already mapped) and adipose fibroblasts (already mapped) of Werner syndrome activates mast cells (already mapped) and dendritic cells (already mapped), driving the chronic low-grade inflammaging phenotype."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Senescent vascular kallikrein: bradykinin, generated by the heightened kallikrein activity in the arterial wall (already mapped) of the accelerated atherosclerosis of Werner syndrome, amplifies vascular permeability and endothelial (already mapped) dysfunction."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Myeloid ageing: erythropoietin supports erythropoiesis from the genomically-unstable bone marrow (already mapped) of Werner syndrome, and EPO signalling may modulate the MDS/AML (mds, aml already mapped) risk of the haematopoietic ageing phenotype."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement-contact senescent regulation: C1-esterase inhibitor restrains the classical complement C1 and the contact system (C3/C5aR1 already mapped) activated in the inflammaging and the atherosclerotic (already mapped) vasculopathy of Werner syndrome."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Inflammaging mast-cell effector: histamine released by mast cells (already mapped) in the chronically inflamed senescent skin and adipose tissue of Werner syndrome amplifies local vascular permeability and the SASP-driven inflammaging cycle."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Senescent fibrotic matrix: periostin, downstream of TGF-β (already mapped) in the senescent fibroblasts (already mapped) of Werner syndrome, promotes the peri-vascular fibrosis and the cutaneous ulcer-prone ECM remodelling of the disorder."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Werner melatonin: melatonin opposes the oxidative DNA damage accumulation (WRN already mapped) in Werner syndrome by scavenging ROS; melatonin also suppresses the NF-κB (already mapped) and TNF-α (already mapped) driven SASP, slowing the inflammaging and progeroid phenotype."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Werner serotonin: serotonin signalling modulates mTOR (already mapped) activity and the insulin (already mapped) sensitivity axis in Werner syndrome; serotonin deficiency amplifies the NF-κB (already mapped) driven inflammaging and the accelerated metabolic dysfunction."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Werner prolactin: prolactin modulates the insulin (already mapped) sensitivity and mTOR (already mapped) signalling dysregulation in Werner syndrome; elevated prolactin in progeroid states amplifies the NF-κB (already mapped) driven inflammaging and worsens the metabolic triad."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Werner oxytocin: oxytocin receptor-cAMP/PKA signalling on Werner syndrome fibroblasts (WRN already mapped) attenuates NF-κB (already mapped) driven SASP and oxidative DNA damage; oxytocin modulates the premature-ageing phenotype and accelerated atherosclerosis of Werner syndrome."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Werner vasopressin: vasopressin V1A receptor in Werner syndrome intersects mTOR (already mapped) and NF-κB (already mapped) pathways; AVP-mediated calcium signalling amplifies the SASP and the progeroid metabolic triad of insulin (already mapped) resistance and dyslipidaemia."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Werner selenium: selenium-dependent GPX and TrxR enzymes counter ROS-driven DNA damage accumulation in Werner syndrome (WRN already mapped); selenium deficiency worsens NF-κB (already mapped)-mediated SASP and accelerates the progeroid inflammaging phenotype."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Werner iodine: thyroid hormones regulate macrophage (already mapped) and mast-cell (already mapped) immune surveillance; thyroid deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) SASP cascade of Werner syndrome."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Werner sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) amplifies IL-6 (already mapped) and mTOR (already mapped) SASP cascade of WRN (already mapped)-deficient Werner fibroblasts (already mapped)."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Werner magnesium: magnesium, as WRN (already mapped) cofactor in fibroblasts (already mapped) and osteoblasts (already mapped), supports DNA repair; deficiency amplifies p53 (already mapped) instability, NF-κB (already mapped) and IL-6 (already mapped) cascade of Werner syndrome."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Werner copper: copper-dependent SOD in fibroblasts (already mapped) and macrophages (already mapped) quenches ROS-driven DNA damage amplifying WRN (already mapped) instability; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) SASP of Werner syndrome."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Werner zinc: zinc-dependent SOD in fibroblasts (already mapped) and macrophages (already mapped) counters ROS amplifying WRN (already mapped) instability; zinc deficiency amplifies p53 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) SASP of Werner syndrome."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Werner potassium: potassium efflux from fibroblasts (already mapped) and macrophages (already mapped) drives NLRP3-IL-1β; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) SASP cascade of Werner syndrome."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Werner carbon: carbon, as metabolic backbone of WRN (already mapped) protein and fibroblast (already mapped) membranes, drives telomere maintenance; carbon dysregulation amplifies NF-κB (already mapped) and p53 (already mapped) and IL-6 (already mapped) SASP of Werner syndrome."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Werner chloride: chloride channels in fibroblasts (already mapped) and macrophages (already mapped) modulate SASP secretion; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) senescence cascade of Werner syndrome."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Werner hydrogen: hydrogen, via redox homeostasis in fibroblasts (already mapped) and macrophages (already mapped), quenches WRN (already mapped)-driven ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) SASP of Werner syndrome."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Werner nitrogen: nitric oxide from fibroblasts (already mapped) and macrophages (already mapped) modulates SASP and vascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) senescence cascade of Werner syndrome."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Werner sulfur: hydrogen sulfide from fibroblasts (already mapped) and macrophages (already mapped) quenches SASP-driven ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) senescence cascade of Werner syndrome."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Werner phosphorus: phosphorus, as ATP precursor in fibroblasts (already mapped) and macrophages (already mapped), fuels DNA repair; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of Werner syndrome."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "WS PD-1: PD-1 on macrophages (already mapped) and T-cytotoxic-cell (already mapped) modulates premature ageing immune exhaustion; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) inflammatory cascade of Werner syndrome."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "WS angiotensin-II: Angiotensin-II in fibroblasts (already mapped) and macrophages (already mapped) promotes vascular stiffness in Werner syndrome; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "WS Wnt/β-catenin: Wnt/β-catenin in fibroblasts (already mapped) and macrophages (already mapped) modulates WRN-deficient stem-cell renewal; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "WS il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates WRN-deficient immune surveillance; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "WS fibronectin: Fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds WRN-deficient ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "WS notch: NOTCH on fibroblasts (already mapped) and macrophages (already mapped) regulates WRN-deficient stem-cell fate; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "WS activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) drives WRN-deficient fibrotic remodelling; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "WS tgf-beta: TGF-β from fibroblasts (already mapped) and macrophages (already mapped) amplifies WRN-deficient tissue fibrosis; tgf-beta excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "WS cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates WS vascular tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "WS calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates WS calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "WS substance-p: substance P from macrophages (already mapped) and fibroblasts (already mapped) modulates WS neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "WS insulin-receptor: insulin receptor on macrophages (already mapped) and fibroblasts (already mapped) drives WS metabolic senescence; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "WS aldosterone: aldosterone from macrophages (already mapped) and fibroblasts (already mapped) modulates WS ion balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of Werner syndrome."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "WS androgen-receptor: androgen receptor on macrophages (already mapped) and fibroblasts (already mapped) modulates WS hormonal senescence; androgen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of Werner syndrome."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "WS norepinephrine: norepinephrine from macrophages (already mapped) and fibroblasts (already mapped) modulates vascular tone in Werner syndrome; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of WS."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "WS adrenomedullin: adrenomedullin from macrophages (already mapped) and fibroblasts (already mapped) modulates vascular tone in Werner syndrome; adrenomedullin loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of WS."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "WS bdnf: BDNF from macrophages (already mapped) and fibroblasts (already mapped) modulates WS neuroimmune tone; bdnf loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) premature ageing cascade of WS."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "WS osteopontin: osteopontin from macrophages (already mapped) and fibroblasts (already mapped) promotes WS ECM remodelling; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) premature ageing cascade of WS."
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
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Premature metabolic disease reaches the liver: the visceral adiposity, dyslipidaemia and insulin resistance of Werner syndrome drive fatty liver disease as part of its accelerated-ageing metabolic syndrome.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is a disease of inflammaging: defective WRN genome maintenance raises chronic inflammatory cytokines that speed atherosclerosis and may erode immune surveillance against Werner's many cancers.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Accelerated vascular ageing reaches the brain: systemic premature atherosclerosis affects cerebral vessels, while high-frequency sensorineural hearing loss reflects the wider neural-ageing phenotype of Werner syndrome.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its metabolic and vascular ageing scars the kidney: the diabetes and premature atherosclerosis of Werner syndrome drive diabetic and renovascular nephropathy with declining renal function.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It predisposes to marrow cancers: Werner syndrome carries an increased risk of myelodysplastic syndrome and acute myeloid leukaemia arising in the bone marrow.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Its chronic ulcers invite infection: the intractable ankle and foot ulcers of Werner syndrome become colonised and infected, classically by Staphylococcus aureus, and heal poorly.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — Its early diabetes needs control: Werner syndrome causes insulin-resistant diabetes in early adulthood, managed with metformin as part of its accelerated metabolic ageing.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — Premature atherosclerosis demands lipid control: Werner syndrome brings early, severe atherosclerosis, and statins are used against the dyslipidaemia and vascular disease that often kill these patients young.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Antiplatelet cover follows the early arteries: the premature coronary and cerebrovascular disease of Werner syndrome prompts aspirin for secondary prevention, as in other accelerated-atherosclerosis states.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Its cancers need careful chemo: Werner syndrome predisposes to sarcomas, thyroid cancer and melanoma, but WRN-deficient cells are hypersensitive to DNA-crosslinking and topoisomerase agents, so chemotherapy must be dosed cautiously to limit toxicity.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It thins and warps bone: Werner syndrome causes early osteoporosis concentrated in the distal limbs, soft-tissue and tendon calcification, and a raised risk of osteosarcoma at unusual sites such as the patella and feet.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — The artery wall itself ages: beyond lipids, Werner syndrome thickens the intima and lays down medial and arteriolar calcification, the structural arterial-wall changes that make its atherosclerosis so premature and diffuse.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Its gene became a drug target: WRN-helicase inhibitors are synthetically lethal in microsatellite-unstable cancers that depend on WRN to survive their unstable DNA—turning the premature-aging gene of Werner syndrome into precision oncology.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Synthetic lethality meets mismatch repair: the MSI-high tumours that WRN inhibitors kill are largely the mismatch-repair-deficient cancers of Lynch syndrome, so Werner's helicase is the vulnerability that Lynch's genomic instability creates.
- `connects-to` → **[Islet of Langerhans](../../05-tissue/islet-of-langerhans/README.md)** — It brings a severe diabetes: Werner syndrome causes lipodystrophy and visceral fat that drive profound insulin resistance, overworking the islets of Langerhans into an early, hard-to-control type 2 diabetes.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — WRN as a drug target: WRN helicase is synthetically lethal in microsatellite-unstable cancers such as MSI-high endometrial and gastric tumours, so the very gene mutated in Werner syndrome is now a sought-after oncology target.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Premature heart death: accelerated atherosclerosis in Werner syndrome causes early myocardial infarction, and along with cancer it is one of the two leading causes of death in these patients in their fifties.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — An unusual tumour spectrum: Werner's genomic instability skews cancers toward mesenchymal types—soft-tissue sarcomas like synovial sarcoma and osteosarcoma—rather than the epithelial carcinomas of most cancer syndromes.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — Replication-fork repair: the WRN helicase works alongside the homologous-recombination machinery, so like BRCA1-deficient cells, Werner cells suffer replication stress and double-strand-break repair defects with potential PARP sensitivity.
- `connects-to` → **[NASH](../nash/README.md)** — Lipodystrophic metabolic disease: Werner syndrome strips subcutaneous fat while accumulating visceral fat, driving severe insulin resistance and hepatic steatosis that progresses to NASH alongside its diabetes.
- `connects-to` → **[Familial Hypercholesterolemia](../familial-hypercholesterolemia/README.md)** — Two roads to early heart attacks: Werner syndrome causes premature atherosclerosis through accelerated cellular ageing, paralleling the early coronary disease of familial hypercholesterolaemia driven instead by lifelong high LDL.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle in cancer: the genomic instability of WRN loss with cell-cycle dysregulation (CDKN2A, cyclin D1) drives the diverse, often mesenchymal cancers of Werner syndrome.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Oncogene activation: MYC activation contributes to the sarcomas and other malignancies that arise from the genomic instability of Werner syndrome.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Metabolism and growth: PI3K-AKT-mTOR signalling links Werner syndrome's insulin resistance and diabetes to the growth signalling of its cancers.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Angiogenesis: VEGF drives the tumour angiogenesis of the sarcomas that arise in Werner syndrome and contributes to its accelerated atherosclerosis.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Fibroblast and vessel signalling: PDGF acting on the prematurely senescent fibroblasts and vascular smooth muscle of Werner syndrome contributes to its fibrosis and atherosclerosis.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the cancers of Werner syndrome drives the angiogenesis and metabolic adaptation that support their growth.
- `connects-to` → **[BLM](../../03-molecular/blm/README.md)** — WRN and BLM (Bloom syndrome) are sister RecQ helicases, so the loss of WRN in Werner syndrome parallels BLM loss—both cause genomic instability and cancer predisposition from failed replication-fork and homologous-recombination repair.
- `connects-to` → **[p21 (CDKN1A)](../../03-molecular/cdkn1a/README.md)** — WRN loss leaves replication stress unresolved, triggering p21-driven cell-cycle arrest and premature replicative senescence—a core mechanism of the accelerated-aging phenotype, where cells exhaust their replicative capacity early.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Severe osteoporosis, especially of the distal limbs, is a hallmark of Werner syndrome, reflecting the RANKL-driven osteoclast activity that outpaces bone formation in this accelerated-aging disorder long before normal old age.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — WRN-deficient cells accumulate micronuclei and cytosolic DNA that activate cGAS-STING, generating the chronic senescence-associated inflammatory secretome (SASP) that helps drive the accelerated tissue aging of Werner syndrome.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Severe, early atherosclerosis is a leading cause of death in Werner syndrome, the cholesterol-laden arterial disease appearing decades early and compounded by the syndrome's dyslipidemia and insulin resistance.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Werner syndrome is a classic model of hypoadiponectinemia, where the loss of insulin-sensitizing adiponectin from dysfunctional visceral fat underlies its severe insulin resistance and early type-2 diabetes.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Werner cells undergo accelerated replicative senescence and adopt a senescence-associated secretory phenotype rich in IL-6, the chronic inflammation that drives the premature atherosclerosis and tissue aging of the syndrome.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — WRN-helicase loss causes replication stress that deregulates the RB-E2F1 cell-cycle checkpoint (with the CDKN2A and cyclin-D already mapped), pushing cells toward senescence and the cancer predisposition of Werner syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — The severe insulin resistance and metabolic derangement of Werner syndrome engage the AMPK energy-sensing pathway (the target of the metformin already mapped), part of its accelerated-aging metabolic phenotype.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Chronic oxidative stress overwhelms NRF2 antioxidant defenses in WRN-deficient cells, accelerating the DNA damage and cellular senescence that underlie the premature aging of Werner syndrome.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — WRN-deficient senescent cells secrete a senescence-associated secretory phenotype rich in TNF-α (with IL-6 and NF-κB mapped), driving the chronic inflammation and atherosclerosis of Werner syndrome.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — With telomerase (TERT mapped) insufficient against WRN-driven telomere dysfunction, the cancers of Werner syndrome—notably osteosarcoma—may engage the ATRX-associated alternative lengthening of telomeres.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped) drives the senescence-associated secretory phenotype and chronic inflammation ('inflammaging') that accelerates the premature aging of Werner syndrome.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — NLRP3-inflammasome activation by the accumulating cellular damage of Werner syndrome contributes to the inflammaging underlying its premature atherosclerosis and metabolic disease.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 regulation of p53 (already mapped) shapes the balance between senescence and apoptosis of genomically unstable cells and the cancer predisposition of Werner syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling is activated by the cytosolic DNA of senescent cells and contributes to the inflammatory, interferon-driven component of the premature aging of Werner syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the tissue fibrosis and chronic inflammation that accompany the accelerated aging phenotype of Werner syndrome.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling drives the premature atherosclerosis and fibrotic tissue remodeling characteristic of the accelerated aging of Werner syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO longevity transcription factors govern the oxidative-stress resistance and senescence programs whose dysregulation accelerates the aging phenotype of Werner syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic clearance of senescent cells by NK and T cells is a surveillance axis whose failure lets senescent cells accumulate in Werner syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 is a senescence-associated secretory-phenotype alarmin that amplifies the chronic inflammaging underlying Werner syndrome tissue damage.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and metabolic signaling relevant to the accelerated cellular aging of Werner syndrome.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Dysregulated CDK4/6-cyclin-D activity (cyclin-D1 already mapped) contributes to the replicative-senescence dynamics and cancer predisposition of Werner syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling contributes to the mesenchymal-tumor (sarcoma) predisposition of Werner syndrome.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the genomically unstable cells and participates in the metabolic aging of Werner syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic-aging-clock alterations of Werner syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy declines with the cellular senescence of Werner syndrome, contributing to its premature-aging phenotype.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the inflammaging and tissue inflammation of Werner syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape accompanying the genomic instability of Werner syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven senescence-associated inflammation (inflammaging) participates in the premature-aging phenotypes of Werner syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the senescence-associated secretory and tumor-stromal interactions of Werner syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammaging and immune microenvironment of Werner syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the chronic inflammation (inflammaging) of Werner syndrome.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Premature atherosclerosis: Werner patients develop early, severe atherosclerosis that is a leading cause of death, with endothelial nitric-oxide dysfunction driving the accelerated vascular aging of this adult progeroid syndrome.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — Accelerated osteoporosis: Werner syndrome causes early, characteristically distal-limb osteoporosis, and sclerostin, the osteocyte Wnt brake on bone formation, is central to the deficient bone accrual of this premature skeletal aging.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Insulin resistance: Werner syndrome features visceral adiposity and severe insulin resistance, and the adipokine resistin links the dysfunctional fat to the metabolic syndrome and diabetes (insulin already mapped) that mark its accelerated aging.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Premature myocardial infarction: the accelerated atherosclerosis of Werner syndrome (cholesterol/nitric oxide already mapped) causes myocardial infarction in the fourth to fifth decade, a leading cause of death, with troponin marking the cardiac injury.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Cancer immunosurveillance: Werner syndrome predisposes to a spectrum of cancers (melanoma, thyroid, sarcoma already mapped), and MHC class II-restricted T-cell surveillance influences which of these genome-instability-driven tumours emerge.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative aging: accumulation of oxidative damage accelerates the cellular senescence of Werner syndrome, and xanthine-oxidase-derived reactive oxygen species contribute to the redox stress that compounds its genome-instability-driven premature aging.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Inflammaging balance: the anti-inflammatory IL-10 counters the senescence-associated secretory phenotype (IL-6, TNF and IL-1 already mapped) of the many senescent cells in Werner syndrome, and this cytokine imbalance drives its inflammaging.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Metabolic dysfunction: the insulin-resistant diabetes (insulin already mapped) and visceral adiposity of Werner syndrome disturb the incretin GLP-1 axis, part of the accelerated metabolic ageing of the disorder.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammaging eicosanoids: prostaglandins from the chronic low-grade inflammation of senescent tissues contribute, with the cytokines already mapped, to the atherosclerosis and tissue dysfunction of the premature ageing of Werner syndrome.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine dysfunction: the abnormal fat distribution and metabolic ageing of Werner syndrome disturb the adipokine leptin (adiponectin and resistin already mapped), part of the insulin-resistant metabolic derangement of the disorder.
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — Atherogenic lipids: the dyslipidaemia of Werner syndrome, in which PCSK9 regulates LDL clearance (cholesterol already mapped), contributes to the premature atherosclerosis that is a leading cause of death in the disorder.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth and ageing axis: the growth-hormone-IGF-1 axis (growth hormone already mapped) underlies the short stature of Werner syndrome, and the insulin/IGF-1 signalling that this axis feeds is central to the biology of ageing.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Senescence and SASP: IL-4 and the M2 arm (IL-10 already mapped) balance the senescence-associated secretory phenotype (TNF, IL-6 and IL-1 already mapped) of the accelerated cellular ageing of Werner syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 arm: IL-13, with IL-4 (already mapped), is part of the type-2 cytokine response whose balance against the pro-inflammatory SASP shapes the inflammatory ageing of Werner syndrome.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Cancer-therapy anaemia: the frequent sarcomas and other cancers of Werner syndrome and their chemotherapy cause anaemia (haemoglobin already mapped) needing transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Senescence interferon: the cGAS-STING (already mapped) sensing of the genomic instability and cytoplasmic DNA of the WRN-deficient (already mapped) senescent cells drives the type-I interferon and the SASP (IL-6 and TNF already mapped) of Werner syndrome.
- `connects-to` → **[Bloom syndrome](../bloom-syndrome/README.md)** — RecQ-helicase sibling: Bloom syndrome (BLM already mapped), with Werner (WRN already mapped) and Rothmund-Thomson (already mapped), are the RecQ-helicase genome-instability syndromes sharing the DNA-repair defect and cancer predisposition.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Sarcoma predisposition: Werner syndrome (WRN already mapped) carries a high risk of sarcomas, notably the osteosarcoma (often at unusual sites), a leading cancer of the syndrome.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Immunosenescence: the NK cells (perforin already mapped) decline as part of the accelerated immunosenescence of the premature-aging phenotype of Werner syndrome.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Inflammaging Th1 arm: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the chronic 'inflammaging' (IL-6 and TNF already mapped) of Werner syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory dimension of the accelerated aging of Werner syndrome.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the accelerated aging of Werner syndrome.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic 'inflammaging' (IL-6 and TNF already mapped) of Werner syndrome.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of Werner syndrome.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Aged-skin mast cells: the mast cells of the atrophic, scleroderma-like skin contribute to the type-2 (IgE already mapped) and inflammaging (IL-6 and TNF already mapped) dimension of Werner syndrome.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 inflammaging source: the CD4 T-helper cells, with immunosenescence, are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the chronic inflammaging of Werner syndrome.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Immunosenescent antigen presentation: the dendritic cells, with the age-associated decline in function, present antigen to the T cells (already mapped) in the immune dysregulation of Werner syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Inflammaging complement: the complement C3 activation is part of the chronic low-grade innate inflammation (inflammaging) of the accelerated ageing of Werner syndrome.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the macrophage (already mapped) inflammation of the inflammaging of Werner syndrome.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immunosenescent surveillance: the cytotoxic T cells (perforin already mapped), with the age-associated exhaustion, provide the impaired surveillance of the senescent cells of Werner syndrome.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Inflammaging alarmin: TSLP released from the senescent skin (already mapped) and adipose fibroblasts (already mapped) of Werner syndrome activates mast cells (already mapped) and dendritic cells (already mapped), contributing to the chronic inflammaging of the premature-ageing syndrome.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Senescent vascular kallikrein: bradykinin, generated by the heightened kallikrein activity in the arterial wall (already mapped) of the accelerated atherosclerosis of Werner syndrome, amplifies vascular permeability and endothelial (already mapped) dysfunction.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Myeloid ageing: erythropoietin supports erythropoiesis from the bone marrow (already mapped) affected by the WRN-deficiency-driven genomic instability of Werner syndrome, and EPO signalling may modulate the MDS/AML (mds, aml already mapped) risk of the haematopoietic ageing phenotype.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement-contact senescent regulation: C1-esterase inhibitor restrains the classical complement C1 and the contact system (C3/C5aR1 already mapped) activated in the inflammaging and the atherosclerotic (already mapped) vasculopathy of Werner syndrome.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Inflammaging mast-cell effector: histamine released by mast cells (already mapped) in the chronically inflamed senescent skin and adipose tissue of Werner syndrome amplifies local vascular permeability and the SASP-driven inflammaging cycle.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Senescent fibrotic matrix: periostin, downstream of TGF-β (already mapped) in the senescent fibroblasts (already mapped) of Werner syndrome, promotes the peri-vascular fibrosis and the cutaneous ulcer-prone ECM remodelling of the disorder.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Werner melatonin: melatonin opposes the oxidative DNA damage accumulation (WRN already mapped) in Werner syndrome by scavenging ROS; melatonin also suppresses the NF-κB (already mapped) and TNF-α (already mapped) driven SASP, slowing the inflammaging and progeroid phenotype.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Werner serotonin: serotonin signalling modulates mTOR (already mapped) activity and the insulin (already mapped) sensitivity axis in Werner syndrome; serotonin deficiency amplifies the NF-κB (already mapped) driven inflammaging and the accelerated metabolic dysfunction.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Werner prolactin: prolactin modulates the insulin (already mapped) sensitivity and mTOR (already mapped) signalling dysregulation in Werner syndrome; elevated prolactin in progeroid states amplifies the NF-κB (already mapped) driven inflammaging and worsens the metabolic triad.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Werner oxytocin: oxytocin receptor-cAMP/PKA signalling on Werner syndrome fibroblasts (WRN already mapped) attenuates NF-κB (already mapped) driven SASP and oxidative DNA damage; oxytocin modulates the premature-ageing phenotype and accelerated atherosclerosis of Werner syndrome.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Werner vasopressin: vasopressin V1A receptor in Werner syndrome intersects mTOR (already mapped) and NF-κB (already mapped) pathways; AVP-mediated calcium signalling amplifies the SASP and the progeroid metabolic triad of insulin (already mapped) resistance and dyslipidaemia.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Werner selenium: selenium-dependent GPX and TrxR enzymes counter ROS-driven DNA damage accumulation in Werner syndrome (WRN already mapped); selenium deficiency worsens NF-κB (already mapped)-mediated SASP and accelerates the progeroid inflammaging phenotype.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Werner iodine: thyroid hormones regulate macrophage (already mapped) and mast-cell (already mapped) immune surveillance; thyroid deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) SASP cascade of Werner syndrome.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Werner sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) amplifies IL-6 (already mapped) and mTOR (already mapped) SASP cascade of WRN (already mapped)-deficient Werner fibroblasts (already mapped).
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Werner magnesium: magnesium, as WRN (already mapped) cofactor in fibroblasts (already mapped) and osteoblasts (already mapped), supports DNA repair; deficiency amplifies p53 (already mapped) instability, NF-κB (already mapped) and IL-6 (already mapped) cascade of Werner syndrome.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Werner copper: copper-dependent SOD in fibroblasts (already mapped) and macrophages (already mapped) quenches ROS-driven DNA damage amplifying WRN (already mapped) instability; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) SASP of Werner syndrome.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Werner zinc: zinc-dependent SOD in fibroblasts (already mapped) and macrophages (already mapped) counters ROS amplifying WRN (already mapped) instability; zinc deficiency amplifies p53 (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) SASP of Werner syndrome.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Werner potassium: potassium efflux from fibroblasts (already mapped) and macrophages (already mapped) drives NLRP3-IL-1β; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) SASP cascade of Werner syndrome.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Werner carbon: carbon, as metabolic backbone of WRN (already mapped) protein and fibroblast (already mapped) membranes, drives telomere maintenance; carbon dysregulation amplifies NF-κB (already mapped) and p53 (already mapped) and IL-6 (already mapped) SASP of Werner syndrome.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Werner chloride: chloride channels in fibroblasts (already mapped) and macrophages (already mapped) modulate SASP secretion; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) senescence cascade of Werner syndrome.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Werner hydrogen: hydrogen, via redox homeostasis in fibroblasts (already mapped) and macrophages (already mapped), quenches WRN (already mapped)-driven ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) SASP of Werner syndrome.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Werner nitrogen: nitric oxide from fibroblasts (already mapped) and macrophages (already mapped) modulates SASP and vascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) senescence cascade of Werner syndrome.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Werner sulfur: hydrogen sulfide from fibroblasts (already mapped) and macrophages (already mapped) quenches SASP-driven ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) senescence cascade of Werner syndrome.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Werner phosphorus: phosphorus, as ATP precursor in fibroblasts (already mapped) and macrophages (already mapped), fuels DNA repair; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of Werner syndrome.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — WS PD-1: PD-1 on macrophages (already mapped) and T-cytotoxic-cell (already mapped) modulates premature ageing immune exhaustion; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) inflammatory cascade of Werner syndrome.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — WS angiotensin-II: Angiotensin-II in fibroblasts (already mapped) and macrophages (already mapped) promotes vascular stiffness in Werner syndrome; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — WS Wnt/β-catenin: Wnt/β-catenin in fibroblasts (already mapped) and macrophages (already mapped) modulates WRN-deficient stem-cell renewal; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — WS il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates WRN-deficient immune surveillance; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — WS fibronectin: Fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds WRN-deficient ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — WS notch: NOTCH on fibroblasts (already mapped) and macrophages (already mapped) regulates WRN-deficient stem-cell fate; NOTCH dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — WS activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) drives WRN-deficient fibrotic remodelling; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — WS tgf-beta: TGF-β from fibroblasts (already mapped) and macrophages (already mapped) amplifies WRN-deficient tissue fibrosis; tgf-beta excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — WS cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates WS vascular tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — WS calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates WS calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — WS substance-p: substance P from macrophages (already mapped) and fibroblasts (already mapped) modulates WS neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — WS insulin-receptor: insulin receptor on macrophages (already mapped) and fibroblasts (already mapped) drives WS metabolic senescence; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) progeroid cascade of Werner syndrome.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — WS aldosterone: aldosterone from macrophages (already mapped) and fibroblasts (already mapped) modulates WS ion balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of Werner syndrome.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — WS androgen-receptor: androgen receptor on macrophages (already mapped) and fibroblasts (already mapped) modulates WS hormonal senescence; androgen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of Werner syndrome.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — WS norepinephrine: norepinephrine from macrophages (already mapped) and fibroblasts (already mapped) modulates vascular tone in Werner syndrome; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of WS.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — WS adrenomedullin: adrenomedullin from macrophages (already mapped) and fibroblasts (already mapped) modulates vascular tone in Werner syndrome; adrenomedullin loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of WS.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — WS bdnf: BDNF from macrophages (already mapped) and fibroblasts (already mapped) modulates WS neuroimmune tone; bdnf loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) premature ageing cascade of WS.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — WS osteopontin: osteopontin from macrophages (already mapped) and fibroblasts (already mapped) promotes WS ECM remodelling; osteopontin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) premature ageing cascade of WS.

[^yu-1996-wrn]: Yu CE, Oshima J, Fu YH, et al. Positional cloning of the Werner's syndrome gene. *Science.* 1996;272(5259):258-262. [doi:10.1126/science.272.5259.258](https://doi.org/10.1126/science.272.5259.258) · [PubMed 8602509](https://pubmed.ncbi.nlm.nih.gov/8602509/)
[^lauper-2013-wrn-neoplasia]: Lauper JM, Krause A, Vaughan TL, Monnat RJ Jr. Spectrum and risk of neoplasia in Werner syndrome: a systematic review. *PLoS One.* 2013;8(4):e59709. [doi:10.1371/journal.pone.0059709](https://doi.org/10.1371/journal.pone.0059709) · [PubMed 23579047](https://pubmed.ncbi.nlm.nih.gov/23579047/)
