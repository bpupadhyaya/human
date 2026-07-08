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
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Cowden syndrome targets the iodine-trapping thyroid: nearly all patients develop goiters and benign nodules, and their lifetime thyroid cancer risk is high, so the gland that concentrates iodine is watched closely from childhood."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Cowden builds excess fibrous tissue: beyond the classic skin papules, the syndrome causes fibrocystic breast disease and fibromas, a tendency to lay down fibrous overgrowth wherever PTEN's brake is lost."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Cowden syndrome sprouts fatty tumors: patients commonly grow multiple lipomas, benign overgrowths of adipocytes, part of the hamartomatous excess that PTEN loss unleashes across tissues."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Cowden demands lifelong imaging surveillance: breast MRI and mammography, thyroid ultrasound and brain MRI screen the many organs its PTEN mutation threatens with tumors."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "PTEN hamartoma syndrome grows vascular lesions: arteriovenous and venous malformations of endothelial cells are part of Cowden's spectrum, alongside its other hamartomas."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Cowden carpets the gut with polyps: hamartomatous and other polyps stud the intestinal epithelium throughout the GI tract, raising colorectal cancer risk and prompting scope surveillance."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals Cowden's hamartomas: the trichilemmomas studding the face arise from hair-follicle outer-root-sheath cells, while in the brain dysplastic ganglion cells swell the cerebellum into Lhermitte-Duclos disease."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Cowden polyps fill the upper gut too: hamartomatous and hyperplastic polyps line the stomach as well as the colon, part of the diffuse gastrointestinal polyposis that defines the PTEN syndrome."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Cowden's facial papules ring the eyes: the wart-like trichilemmomas cluster around the eyelids and mouth, a characteristic mucocutaneous sign that prompts genetic testing for the underlying PTEN mutation."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "PTEN overgrowth shows in the frame: macrocephaly is a near-constant feature, and the syndrome spawns lipomas and, in its Bannayan-Riley-Ruvalcaba overlap, skeletal and soft-tissue overgrowth from the unleashed mTOR pathway."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Hamartomatous polyps stud the whole gut: beyond the colon and stomach, Cowden seeds the small intestine with polyps of mixed type, part of the diffuse PTEN-driven overgrowth lining the digestive tract."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Cowden leans toward thyroid autoimmunity: alongside its thyroid cancers and goiter, it carries an excess of Hashimoto thyroiditis, so anti-thyroid antibodies often accompany the structural thyroid disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Cowden's hamartomas reach the liver: as a PTEN hamartoma tumor syndrome it can stud the liver with benign hamartomas and hemangiomas, part of the diffuse overgrowth that PTEN loss drives across many organs beyond the classic skin, breast and thyroid sites."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Losing PTEN can dim antitumor immunity: PTEN loss raises PD-L1 and weakens cytotoxic T-cell killing of the tumor, a mechanism studied in PTEN-driven cancers that may shape how Cowden's malignancies respond to checkpoint immunotherapy."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Cowden joins the hereditary kidney-cancer differential: like von Hippel-Lindau and Birt-Hogg-Dubé it predisposes to renal cell carcinoma, so the pattern of other tumors and skin findings is what tells these germline syndromes apart."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Unchecked growth signaling explains the overgrowth: with PTEN's brake gone, IGF-1-driven PI3K-AKT signaling runs free, behind the macrocephaly, hamartomas, and tissue overgrowth that mark the PTEN syndromes."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "PTEN steadies the immune system's brakes: it is essential for regulatory T-cell stability, so PTEN loss can destabilize Tregs into autoimmunity — part of the immune dysregulation seen in PTEN hamartoma syndrome."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Two overgrowth syndromes meet in the brain: like neurofibromatosis type 1, Cowden's PTEN loss feeds the RAS-PI3K axis and brings macrocephaly and a raised rate of autism, overlapping neurodevelopmental features across the two."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "A collagen tumor is a diagnostic clue: the sclerotic fibroma (storiform collagenoma) of the skin, a whorled mass of dense collagen, is a characteristic Cowden lesion alongside the trichilemmomas that flag the syndrome."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "The polyps reach the stomach: Cowden studs the GI tract with hamartomatous polyps and carries an increased risk of gastric and other upper-GI cancers, extending its surveillance beyond the colon."
  - target: 01-human/07-system/hereditary-breast-ovarian-cancer
    relation: connects-to
    note: "It is part of the hereditary breast-cancer differential: Cowden's PTEN-driven breast cancer risk overlaps clinically with BRCA-related hereditary breast and ovarian cancer, so the wider tumor and skin pattern is what distinguishes the syndromes and guides gene testing."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "PTEN loss unleashes more than PI3K: alongside AKT-mTOR, the unrestrained signaling of Cowden activates STAT3, adding a proliferative, pro-survival pathway to the hamartomas and cancers of the syndrome."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Growth signals drive the cell cycle through cyclin D1: PTEN loss and the resulting PI3K-AKT activity push cyclin D1 expression, accelerating the cell-cycle entry behind Cowden's hamartomatous overgrowth and tumors."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "PTEN reaches the developing brain: beyond the autism and macrocephaly of the syndrome, PTEN's role in neuronal signaling is linked to mood and anxiety disorders, part of Cowden's neuropsychiatric spectrum."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A lifetime of cancers and surgery raises the clot risk: the multiple malignancies of Cowden syndrome and the repeated operations they require bring tumor-associated hypercoagulability and perioperative venous thromboembolism."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Bleeding hamartomas and cancer lower the count: the GI hamartomatous polyps of Cowden bleed chronically while its cancers add inflammation, together producing iron loss and an anemia-of-chronic-disease component."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Recurrent kidney tumors cost nephrons: Cowden's high lifetime risk of renal cell carcinoma demands repeated nephron-sparing surgeries, so the cumulative loss of kidney tissue can progress to chronic kidney disease."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Brain hamartomas can spark seizures: Cowden's PTEN defect causes macrocephaly, cortical malformations and the cerebellar Lhermitte-Duclos lesion, raising the risk of seizures and epilepsy."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Treating its many cancers opens the lung to mold: the chemotherapy for the breast, thyroid and other cancers Cowden predisposes to causes neutropenia, allowing inhaled Aspergillus to invade."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Constant cancer surveillance breeds worry: the lifelong multi-organ cancer screening of Cowden, often alongside its associated autism and anxiety traits, fosters chronic health anxiety."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It targets the thyroid above all glands: Cowden syndrome causes multinodular goitre, Hashimoto's thyroiditis and a raised risk of thyroid cancer, reflecting PTEN's role in the endocrine system."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It studs the gut with hamartomas: Cowden syndrome causes numerous hamartomatous polyps and ganglioneuromas throughout the GI tract, alongside its raised colorectal-cancer risk."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its many cancers mean many surgeries: prophylactic and therapeutic operations on the breast, thyroid, uterus and colon in Cowden syndrome leave a lifetime of wounds that must heal."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its pathway spawns vascular malformations: PTEN loss overactivates PI3K-AKT signalling, producing arteriovenous and other vascular malformations across the PTEN hamartoma tumour syndrome spectrum."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It seeds lymphatic and fatty anomalies: the PTEN hamartoma spectrum, overlapping Bannayan-Riley-Ruvalcaba syndrome, features lymphatic malformations and multiple lipomas."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its gene also tunes immunity: PTEN regulates immune-cell signalling, and Cowden syndrome is associated with immune dysregulation and a raised tendency to autoimmunity."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It raises kidney-cancer risk: Cowden syndrome predisposes to renal cell carcinoma, adding the kidney to the breast, thyroid and endometrium in its tumour spectrum and surveillance."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "A fellow multi-cancer syndrome: like Li-Fraumeni, Cowden syndrome is an autosomal-dominant predisposition to several cancers including breast, the two entering each other's differential."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "A comparator skin-marker tumour syndrome: both Cowden and Gorlin syndrome are autosomal-dominant disorders announced by characteristic skin lesions and carrying a raised lifetime tumour risk."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "mTOR drugs match its biology: PTEN loss in Cowden syndrome unleashes PI3K-AKT-mTOR, so mTOR and PI3K inhibitors (sirolimus, alpelisib) are studied for its hamartomas and tumours."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Overlapping breast and thyroid tumours: like Carney complex, Cowden syndrome predisposes to breast and thyroid neoplasia with mucocutaneous lesions, two hamartoma syndromes spanning skin and glands."
  - target: 01-human/07-system/men1-syndrome
    relation: connects-to
    note: "A fellow endocrine-tumour syndrome: Cowden's thyroid and other glandular tumours echo the multiple endocrine neoplasia syndromes like MEN1, both inherited drivers of multi-gland tumour predisposition."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Its many cancers need treating: Cowden syndrome's high lifetime risk of breast, endometrial and thyroid cancer means chemotherapy and cancer-directed therapy join the lifelong surveillance that defines its management."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "PTEN loss malforms vessels: PTEN hamartoma tumour syndrome causes vascular anomalies including arteriovenous malformations, where disordered arterial-wall growth produces the vascular lesions seen alongside its hamartomas."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Two polyposis syndromes contrasted: Cowden produces hamartomatous gastrointestinal polyps, whereas familial adenomatous polyposis carpets the colon with adenomas — different polyp biology demanding different cancer surveillance."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "A sporadic PTEN cancer: PTEN loss is among the commonest events in prostate cancer, and Cowden carriers face elevated risk—the germline syndrome mirroring a frequent somatic driver."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "PTEN loss in the brain tumour too: PTEN is one of the most frequently inactivated genes in glioblastoma, the same tumour-suppressor whose germline loss defines Cowden syndrome."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "PTEN shapes the brain: loss of PTEN drives neuronal overgrowth, underlying the macrocephaly, autism-spectrum features and dysplastic cerebellar gangliocytoma (Lhermitte-Duclos disease) of Cowden syndrome."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "PTEN and overgrowth: germline PTEN loss enhances PI3K-Akt signalling and drives obesity and macrocephaly, the same overgrowth pathway behind Cowden syndrome's hamartomas."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "An insulin-signalling paradox: PTEN loss enhances insulin's PI3K-Akt signal, so Cowden patients are often obese yet paradoxically insulin-sensitive, an unusual metabolic profile that informs diabetes biology."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Cerebellar tumours, benign vs malignant: Cowden's Lhermitte-Duclos disease is a benign dysplastic cerebellar gangliocytoma, contrasting with the malignant cerebellar medulloblastoma of children."
  - target: 01-human/03-molecular/tsc1-tsc2
    relation: connects-to
    note: "Convergent mTOR control: PTEN and the TSC1-TSC2 complex are both brakes on mTORC1, making Cowden and tuberous sclerosis sister hamartoma syndromes driven by unrestrained mTOR signalling."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Cooperating tumour suppressors: PTEN helps stabilise p53, and combined PTEN/p53 dysfunction accelerates the tumours of the Cowden spectrum beyond PTEN loss alone."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Glial overgrowth: PTEN loss in CNS glia including astrocytes drives the megalencephaly and dysplastic cerebellar overgrowth (Lhermitte-Duclos) characteristic of Cowden syndrome."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK crosstalk: PTEN loss in Cowden syndrome also potentiates RAS-ERK signalling, which cooperates with the PI3K/AKT pathway to drive the hamartomas and tumours."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Downstream proliferation: unrestrained PI3K/AKT/mTOR signalling from PTEN loss upregulates MYC, helping drive the cell growth and tumour predisposition of Cowden syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic and angiogenic: AKT/mTOR activation from PTEN loss stabilises HIF-1α, promoting the angiogenesis that supports the vascular hamartomas and tumours of the syndrome."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid neoplasia: Cowden syndrome carries a high risk of follicular thyroid carcinoma and benign thyroid disease, one of the defining components of the PTEN hamartoma tumour syndrome."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormone-driven cancers: the markedly elevated breast and endometrial cancer risk of Cowden syndrome is driven by oestrogen-responsive epithelium proliferating under unrestrained PI3K-AKT signalling."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Suppressed autophagy: PTEN loss hyperactivates mTOR, which suppresses autophagy and shifts the balance toward growth — the rationale for trialling mTOR inhibitors (rapalogs) in Cowden syndrome."
  - target: 01-human/03-molecular/cdkn1b
    relation: connects-to
    note: "Lost cell-cycle brake: PTEN normally stabilises the cell-cycle inhibitor p27 (CDKN1B), so PTEN loss in Cowden syndrome removes this restraint, contributing to the hamartomatous overgrowth and cancer risk."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis evasion: PTEN loss unleashes PI3K-AKT survival signalling that suppresses caspase-3-mediated apoptosis, giving Cowden cells the survival advantage that underlies their hamartomas and tumours."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neurodevelopmental PTEN: PTEN restrains neuronal growth via the PI3K-mTOR pathway that BDNF activates, so its loss causes the macrocephaly and the autism/neurodevelopmental features of the PTEN hamartoma spectrum."
  - target: 01-human/03-molecular/stk11
    relation: connects-to
    note: "Hamartomatous-polyposis differential: Cowden (PTEN) sits beside Peutz-Jeghers (LKB1/STK11) and juvenile polyposis among the hamartomatous-polyposis syndromes, distinct tumour suppressors that converge on mTOR to produce overlapping GI-polyp and cancer phenotypes."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Colorectal risk: the gastrointestinal hamartomas of Cowden carry an elevated colorectal-cancer risk, and malignant progression engages Wnt/β-catenin signalling, the canonical driver of colorectal carcinogenesis, prompting colonoscopic surveillance."
  - target: 01-human/03-molecular/mlh1
    relation: connects-to
    note: "Endometrial-cancer differential: Cowden's high endometrial-cancer risk overlaps clinically with Lynch syndrome's mismatch-repair-deficient endometrial cancer, two distinct hereditary routes to the same tumour that genetic testing must distinguish."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "AKT substrate: the unrestrained AKT of PTEN-deficient Cowden tissue phosphoinhibits GSK-3β (AKT already mapped), stabilising cyclin-D1 and feeding the Wnt/β-catenin signalling (both mapped) that fuels hamartoma overgrowth."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "Breast-cancer input: HER2 and related receptors converge on the PI3K-AKT axis (already mapped), the receptor-level driver feeding the breast carcinomas that are a defining Cowden-syndrome cancer risk."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: downstream of constitutive mTOR-AKT signalling, the cyclin-D1-RB axis (cyclin-D1 and CDKN1B already mapped) releases E2F1 to drive the cell-cycle entry underlying Cowden hamartomas and tumours."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Unopposed RTK input: receptor-tyrosine-kinase signalling through EGFR feeds the PI3K-AKT-mTOR axis that PTEN normally restrains (PI3K, AKT and mTOR all mapped), and its unopposed activity drives the tumours of PTEN-deficient Cowden syndrome."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Checkpoint restraint: the RB1-E2F checkpoint (E2F1, cyclin-D1 and CDKN1B already mapped) restrains the proliferation driven by the mTOR-AKT growth signalling characteristic of Cowden-syndrome lesions."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis evasion: anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), supporting the survival of the hamartomas and carcinomas of Cowden syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a marker of the thyroid neoplasia common in Cowden syndrome and modulates tumour-cell survival."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) provides a tumour-suppressive counterweight whose loss cooperates with PTEN deficiency in Cowden-associated tumours."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) provides an additional proliferative input in the multi-organ tumours of Cowden syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune surveillance of the multi-organ neoplasms that arise in Cowden syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "PTEN loss perturbs genome stability and PTEN's nuclear functions, and the resulting cytosolic DNA can engage cGAS-STING in the lesions of Cowden syndrome."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Loss of PTEN-restrained PI3K-AKT signalling drives cyclin-D-CDK4/6 activity (cyclin-D1 and RB1 mapped) in the hamartomatous and neoplastic growths of Cowden syndrome."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the PTEN-deficient tumors of Cowden syndrome."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the multiple hamartomas and cancers of Cowden syndrome must evade."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory microenvironment of Cowden syndrome lesions."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, in balance with the mTOR pathway (mTOR already mapped) hyperactivated by PTEN loss, regulates the metabolic homeostasis of the hamartomatous lesions of Cowden syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of the tumors of Cowden syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the tumors of Cowden syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of Cowden syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of Cowden syndrome."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A-p16 cell-cycle control participates in the tumor-suppressor network whose disruption cooperates with PTEN loss in Cowden syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the neoplasms of Cowden syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of Cowden syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Cowden syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of the neoplasms of Cowden syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of Cowden syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of Cowden syndrome."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "PI3K-insulin axis: PTEN opposes PI3K signalling downstream of the insulin receptor, so its loss in Cowden syndrome heightens insulin/PI3K-AKT signalling (both already mapped), the basis of both the hamartoma-tumour predisposition and reported insulin sensitivity."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Endometrial hormonal axis: Cowden syndrome confers a high endometrial cancer risk, an estrogen-driven cancer (estrogen already mapped) that progesterone opposes, so the estrogen-progesterone balance is central to the gynaecological surveillance and prevention."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Cancer immunosurveillance: MHC class II-restricted T-cell surveillance influences which of the many hamartomas and early cancers of Cowden syndrome progress, and antigen presentation is relevant to immunotherapy of any advanced tumours."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell responses (MHC class II already mapped) provide the immune surveillance influencing progression of the hamartomas and cancers of Cowden syndrome, and underlie the immunotherapy of any advanced tumours."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Hamartoma stroma: tumour-associated macrophages populate the many hamartomas and early cancers of Cowden syndrome, contributing to the growth-factor-rich stroma (VEGF and TGF-beta already mapped) that supports these PTEN-driven proliferations."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Vascular anomalies: Cowden syndrome includes vascular malformations, and nitric oxide with VEGF (already mapped) regulates the endothelial biology behind these anomalies, part of the broad tissue overgrowth of PTEN loss."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic overgrowth: the PI3K-AKT-mTOR pathway (already mapped) unleashed by PTEN loss intersects with leptin and the metabolic signalling (insulin already mapped) that contributes to the overgrowth and metabolic phenotype of Cowden syndrome."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipid metabolism: PTEN, through the PI3K-AKT pathway (already mapped), regulates cellular lipid and cholesterol metabolism, and its loss shifts the lipid handling that supports the proliferations of Cowden syndrome."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive stroma: IL-10 from the tumour-associated macrophages (already mapped) of the hamartomas and early cancers of Cowden syndrome dampens local immunity, part of the growth-permissive stroma of these PTEN-driven lesions."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an M2 phenotype (IL-10 already mapped), part of the growth-permissive immunosuppressive stroma of the hamartomas and early cancers of Cowden syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the permissive stroma around the PTEN-driven lesions of Cowden syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic-cancer link: adiponectin, with leptin (already mapped), links the PTEN-PI3K-AKT metabolic pathway (insulin already mapped) to the obesity-associated cancer risk of the proliferations of Cowden syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine-cancer milieu: resistin, with leptin and adiponectin (already mapped), links the PTEN-PI3K (already mapped) metabolic pathway to the obesity-associated cancer risk of Cowden syndrome."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Thyroid selenoproteins: selenium supports the selenoprotein deiodinase and antioxidant function of the thyroid (already mapped), the site of the nodular disease and cancer of Cowden syndrome."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Hamartoma stroma: PDGF drives the mesenchymal and stromal proliferation (collagen already mapped) of the hamartomas of Cowden syndrome, part of the PTEN (already mapped)-driven overgrowth."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Lhermitte-Duclos: the dysplastic cerebellar gangliocytoma (Lhermitte-Duclos disease; PTEN/mTOR already mapped) of the brain, and the macrocephaly, are the neurological features of Cowden syndrome."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "GI hamartomas/CRC: the hamartomatous and other colonic polyps of Cowden syndrome (PTEN already mapped) confer a raised colorectal-cancer risk, needing the surveillance."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Macrocephaly-autism: the PTEN (already mapped) mutations cause a macrocephaly-autism spectrum, linking Cowden syndrome to the neurodevelopmental phenotype."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity relevant to the breast, thyroid and endometrial cancers of Cowden syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the Cowden-syndrome tumours."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the PTEN-hamartoma tumours of Cowden syndrome."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the Cowden-syndrome tumours."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the PTEN-hamartoma tumour microenvironment of Cowden syndrome."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of Cowden syndrome."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the hamartoma stroma contribute to the angiogenesis (VEGF already mapped) and the immune microenvironment of the PTEN-hamartoma tumours of Cowden syndrome."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the Cowden-syndrome tumours."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the PTEN-hamartoma tumour stroma of Cowden syndrome."
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
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Cowden syndrome targets the iodine-trapping thyroid: nearly all patients develop goiters and benign nodules, and their lifetime thyroid cancer risk is high, so the gland that concentrates iodine is watched closely from childhood.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Cowden builds excess fibrous tissue: beyond the classic skin papules, the syndrome causes fibrocystic breast disease and fibromas, a tendency to lay down fibrous overgrowth wherever PTEN's brake is lost.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Cowden syndrome sprouts fatty tumors: patients commonly grow multiple lipomas, benign overgrowths of adipocytes, part of the hamartomatous excess that PTEN loss unleashes across tissues.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Cowden demands lifelong imaging surveillance: breast MRI and mammography, thyroid ultrasound and brain MRI screen the many organs its PTEN mutation threatens with tumors.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — PTEN hamartoma syndrome grows vascular lesions: arteriovenous and venous malformations of endothelial cells are part of Cowden's spectrum, alongside its other hamartomas.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Cowden carpets the gut with polyps: hamartomatous and other polyps stud the intestinal epithelium throughout the GI tract, raising colorectal cancer risk and prompting scope surveillance.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals Cowden's hamartomas: the trichilemmomas studding the face arise from hair-follicle outer-root-sheath cells, while in the brain dysplastic ganglion cells swell the cerebellum into Lhermitte-Duclos disease.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Cowden polyps fill the upper gut too: hamartomatous and hyperplastic polyps line the stomach as well as the colon, part of the diffuse gastrointestinal polyposis that defines the PTEN syndrome.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Cowden's facial papules ring the eyes: the wart-like trichilemmomas cluster around the eyelids and mouth, a characteristic mucocutaneous sign that prompts genetic testing for the underlying PTEN mutation.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — PTEN overgrowth shows in the frame: macrocephaly is a near-constant feature, and the syndrome spawns lipomas and, in its Bannayan-Riley-Ruvalcaba overlap, skeletal and soft-tissue overgrowth from the unleashed mTOR pathway.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Hamartomatous polyps stud the whole gut: beyond the colon and stomach, Cowden seeds the small intestine with polyps of mixed type, part of the diffuse PTEN-driven overgrowth lining the digestive tract.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Cowden leans toward thyroid autoimmunity: alongside its thyroid cancers and goiter, it carries an excess of Hashimoto thyroiditis, so anti-thyroid antibodies often accompany the structural thyroid disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Cowden's hamartomas reach the liver: as a PTEN hamartoma tumor syndrome it can stud the liver with benign hamartomas and hemangiomas, part of the diffuse overgrowth that PTEN loss drives across many organs beyond the classic skin, breast and thyroid sites.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Losing PTEN can dim antitumor immunity: PTEN loss raises PD-L1 and weakens cytotoxic T-cell killing of the tumor, a mechanism studied in PTEN-driven cancers that may shape how Cowden's malignancies respond to checkpoint immunotherapy.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — Cowden joins the hereditary kidney-cancer differential: like von Hippel-Lindau and Birt-Hogg-Dubé it predisposes to renal cell carcinoma, so the pattern of other tumors and skin findings is what tells these germline syndromes apart.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Unchecked growth signaling explains the overgrowth: with PTEN's brake gone, IGF-1-driven PI3K-AKT signaling runs free, behind the macrocephaly, hamartomas, and tissue overgrowth that mark the PTEN syndromes.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — PTEN steadies the immune system's brakes: it is essential for regulatory T-cell stability, so PTEN loss can destabilize Tregs into autoimmunity — part of the immune dysregulation seen in PTEN hamartoma syndrome.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Two overgrowth syndromes meet in the brain: like neurofibromatosis type 1, Cowden's PTEN loss feeds the RAS-PI3K axis and brings macrocephaly and a raised rate of autism, overlapping neurodevelopmental features across the two.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — A collagen tumor is a diagnostic clue: the sclerotic fibroma (storiform collagenoma) of the skin, a whorled mass of dense collagen, is a characteristic Cowden lesion alongside the trichilemmomas that flag the syndrome.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — The polyps reach the stomach: Cowden studs the GI tract with hamartomatous polyps and carries an increased risk of gastric and other upper-GI cancers, extending its surveillance beyond the colon.
- `connects-to` → **[Hereditary Breast and Ovarian Cancer](../hereditary-breast-ovarian-cancer/README.md)** — It is part of the hereditary breast-cancer differential: Cowden's PTEN-driven breast cancer risk overlaps clinically with BRCA-related hereditary breast and ovarian cancer, so the wider tumor and skin pattern is what distinguishes the syndromes and guides gene testing.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — PTEN loss unleashes more than PI3K: alongside AKT-mTOR, the unrestrained signaling of Cowden activates STAT3, adding a proliferative, pro-survival pathway to the hamartomas and cancers of the syndrome.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Growth signals drive the cell cycle through cyclin D1: PTEN loss and the resulting PI3K-AKT activity push cyclin D1 expression, accelerating the cell-cycle entry behind Cowden's hamartomatous overgrowth and tumors.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — PTEN reaches the developing brain: beyond the autism and macrocephaly of the syndrome, PTEN's role in neuronal signaling is linked to mood and anxiety disorders, part of Cowden's neuropsychiatric spectrum.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A lifetime of cancers and surgery raises the clot risk: the multiple malignancies of Cowden syndrome and the repeated operations they require bring tumor-associated hypercoagulability and perioperative venous thromboembolism.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Bleeding hamartomas and cancer lower the count: the GI hamartomatous polyps of Cowden bleed chronically while its cancers add inflammation, together producing iron loss and an anemia-of-chronic-disease component.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Recurrent kidney tumors cost nephrons: Cowden's high lifetime risk of renal cell carcinoma demands repeated nephron-sparing surgeries, so the cumulative loss of kidney tissue can progress to chronic kidney disease.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Brain hamartomas can spark seizures: Cowden's PTEN defect causes macrocephaly, cortical malformations and the cerebellar Lhermitte-Duclos lesion, raising the risk of seizures and epilepsy.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Treating its many cancers opens the lung to mold: the chemotherapy for the breast, thyroid and other cancers Cowden predisposes to causes neutropenia, allowing inhaled Aspergillus to invade.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Constant cancer surveillance breeds worry: the lifelong multi-organ cancer screening of Cowden, often alongside its associated autism and anxiety traits, fosters chronic health anxiety.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It targets the thyroid above all glands: Cowden syndrome causes multinodular goitre, Hashimoto's thyroiditis and a raised risk of thyroid cancer, reflecting PTEN's role in the endocrine system.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It studs the gut with hamartomas: Cowden syndrome causes numerous hamartomatous polyps and ganglioneuromas throughout the GI tract, alongside its raised colorectal-cancer risk.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its many cancers mean many surgeries: prophylactic and therapeutic operations on the breast, thyroid, uterus and colon in Cowden syndrome leave a lifetime of wounds that must heal.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its pathway spawns vascular malformations: PTEN loss overactivates PI3K-AKT signalling, producing arteriovenous and other vascular malformations across the PTEN hamartoma tumour syndrome spectrum.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It seeds lymphatic and fatty anomalies: the PTEN hamartoma spectrum, overlapping Bannayan-Riley-Ruvalcaba syndrome, features lymphatic malformations and multiple lipomas.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its gene also tunes immunity: PTEN regulates immune-cell signalling, and Cowden syndrome is associated with immune dysregulation and a raised tendency to autoimmunity.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It raises kidney-cancer risk: Cowden syndrome predisposes to renal cell carcinoma, adding the kidney to the breast, thyroid and endometrium in its tumour spectrum and surveillance.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — A fellow multi-cancer syndrome: like Li-Fraumeni, Cowden syndrome is an autosomal-dominant predisposition to several cancers including breast, the two entering each other's differential.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — A comparator skin-marker tumour syndrome: both Cowden and Gorlin syndrome are autosomal-dominant disorders announced by characteristic skin lesions and carrying a raised lifetime tumour risk.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — mTOR drugs match its biology: PTEN loss in Cowden syndrome unleashes PI3K-AKT-mTOR, so mTOR and PI3K inhibitors (sirolimus, alpelisib) are studied for its hamartomas and tumours.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — Overlapping breast and thyroid tumours: like Carney complex, Cowden syndrome predisposes to breast and thyroid neoplasia with mucocutaneous lesions, two hamartoma syndromes spanning skin and glands.
- `connects-to` → **[MEN1 Syndrome](../men1-syndrome/README.md)** — A fellow endocrine-tumour syndrome: Cowden's thyroid and other glandular tumours echo the multiple endocrine neoplasia syndromes like MEN1, both inherited drivers of multi-gland tumour predisposition.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Its many cancers need treating: Cowden syndrome's high lifetime risk of breast, endometrial and thyroid cancer means chemotherapy and cancer-directed therapy join the lifelong surveillance that defines its management.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — PTEN loss malforms vessels: PTEN hamartoma tumour syndrome causes vascular anomalies including arteriovenous malformations, where disordered arterial-wall growth produces the vascular lesions seen alongside its hamartomas.
- `connects-to` → **[FAP](../fap/README.md)** — Two polyposis syndromes contrasted: Cowden produces hamartomatous gastrointestinal polyps, whereas familial adenomatous polyposis carpets the colon with adenomas — different polyp biology demanding different cancer surveillance.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — A sporadic PTEN cancer: PTEN loss is among the commonest events in prostate cancer, and Cowden carriers face elevated risk—the germline syndrome mirroring a frequent somatic driver.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — PTEN loss in the brain tumour too: PTEN is one of the most frequently inactivated genes in glioblastoma, the same tumour-suppressor whose germline loss defines Cowden syndrome.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — PTEN shapes the brain: loss of PTEN drives neuronal overgrowth, underlying the macrocephaly, autism-spectrum features and dysplastic cerebellar gangliocytoma (Lhermitte-Duclos disease) of Cowden syndrome.
- `connects-to` → **[Obesity](../obesity/README.md)** — PTEN and overgrowth: germline PTEN loss enhances PI3K-Akt signalling and drives obesity and macrocephaly, the same overgrowth pathway behind Cowden syndrome's hamartomas.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — An insulin-signalling paradox: PTEN loss enhances insulin's PI3K-Akt signal, so Cowden patients are often obese yet paradoxically insulin-sensitive, an unusual metabolic profile that informs diabetes biology.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Cerebellar tumours, benign vs malignant: Cowden's Lhermitte-Duclos disease is a benign dysplastic cerebellar gangliocytoma, contrasting with the malignant cerebellar medulloblastoma of children.
- `connects-to` → **[TSC1-TSC2](../../03-molecular/tsc1-tsc2/README.md)** — Convergent mTOR control: PTEN and the TSC1-TSC2 complex are both brakes on mTORC1, making Cowden and tuberous sclerosis sister hamartoma syndromes driven by unrestrained mTOR signalling.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Cooperating tumour suppressors: PTEN helps stabilise p53, and combined PTEN/p53 dysfunction accelerates the tumours of the Cowden spectrum beyond PTEN loss alone.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Glial overgrowth: PTEN loss in CNS glia including astrocytes drives the megalencephaly and dysplastic cerebellar overgrowth (Lhermitte-Duclos) characteristic of Cowden syndrome.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK crosstalk: PTEN loss in Cowden syndrome also potentiates RAS-ERK signalling, which cooperates with the PI3K/AKT pathway to drive the hamartomas and tumours.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Downstream proliferation: unrestrained PI3K/AKT/mTOR signalling from PTEN loss upregulates MYC, helping drive the cell growth and tumour predisposition of Cowden syndrome.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic and angiogenic: AKT/mTOR activation from PTEN loss stabilises HIF-1α, promoting the angiogenesis that supports the vascular hamartomas and tumours of the syndrome.
- `connects-to` → **[Thyroid Hormones](../../03-molecular/thyroid-hormones/README.md)** — Thyroid neoplasia: Cowden syndrome carries a high risk of follicular thyroid carcinoma and benign thyroid disease, one of the defining components of the PTEN hamartoma tumour syndrome.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Hormone-driven cancers: the markedly elevated breast and endometrial cancer risk of Cowden syndrome is driven by oestrogen-responsive epithelium proliferating under unrestrained PI3K-AKT signalling.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Suppressed autophagy: PTEN loss hyperactivates mTOR, which suppresses autophagy and shifts the balance toward growth — the rationale for trialling mTOR inhibitors (rapalogs) in Cowden syndrome.
- `connects-to` → **[p27 (CDKN1B)](../../03-molecular/cdkn1b/README.md)** — PTEN normally stabilizes the cell-cycle inhibitor p27, so PTEN loss in Cowden syndrome removes this restraint—contributing to the hamartomatous overgrowth and the broadly elevated cancer risk of the syndrome.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — PTEN loss unleashes PI3K-AKT survival signaling that suppresses caspase-3-mediated apoptosis, giving Cowden cells the survival advantage that underlies their multiple hamartomas and predisposition to cancer.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — PTEN restrains neuronal growth via the same PI3K-mTOR pathway that BDNF activates, so its loss causes the macrocephaly and the autism and neurodevelopmental features that characterize the PTEN hamartoma tumor spectrum.
- `connects-to` → **[STK11](../../03-molecular/stk11/README.md)** — Cowden (PTEN) sits beside Peutz-Jeghers (LKB1/STK11) and juvenile polyposis among the hamartomatous-polyposis syndromes, distinct tumor suppressors that converge on mTOR to produce overlapping GI-polyp and cancer phenotypes.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — The gastrointestinal hamartomas of Cowden carry an elevated colorectal-cancer risk, and malignant progression engages Wnt/β-catenin signaling, the canonical driver of colorectal carcinogenesis, prompting colonoscopic surveillance.
- `connects-to` → **[MLH1](../../03-molecular/mlh1/README.md)** — Cowden's high endometrial-cancer risk overlaps clinically with Lynch syndrome's mismatch-repair-deficient endometrial cancer, two distinct hereditary routes to the same tumor that genetic testing must distinguish.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — The unrestrained AKT of PTEN-deficient Cowden tissue phosphoinhibits GSK-3β (AKT already mapped), stabilizing cyclin-D1 and feeding the Wnt/β-catenin signaling (both mapped) that fuels hamartoma overgrowth.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — HER2 and related receptors converge on the PI3K-AKT axis (already mapped), the receptor-level driver feeding the breast carcinomas that are a defining Cowden-syndrome cancer risk.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Downstream of constitutive mTOR-AKT signaling, the cyclin-D1-RB axis (cyclin-D1 and CDKN1B already mapped) releases E2F1 to drive the cell-cycle entry underlying Cowden hamartomas and tumors.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Receptor-tyrosine-kinase signaling through EGFR feeds the PI3K-AKT-mTOR axis that PTEN normally restrains (PI3K, AKT and mTOR all mapped), and its unopposed activity drives the tumors of PTEN-deficient Cowden syndrome.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (E2F1, cyclin-D1 and CDKN1B already mapped) restrains the proliferation driven by the mTOR-AKT growth signaling characteristic of Cowden-syndrome lesions.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), supporting the survival of the hamartomas and carcinomas of Cowden syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a marker of the thyroid neoplasia common in Cowden syndrome and modulates tumor-cell survival.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) provides a tumor-suppressive counterweight whose loss cooperates with PTEN deficiency in Cowden-associated tumors.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) provides an additional proliferative input in the multi-organ tumors of Cowden syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune surveillance of the multi-organ neoplasms that arise in Cowden syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — PTEN loss perturbs genome stability and PTEN's nuclear functions, and the resulting cytosolic DNA can engage cGAS-STING in the lesions of Cowden syndrome.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Loss of PTEN-restrained PI3K-AKT signaling drives cyclin-D-CDK4/6 activity (cyclin-D1 and RB1 mapped) in the hamartomatous and neoplastic growths of Cowden syndrome.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in the PTEN-deficient tumors of Cowden syndrome.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is the immune clearance that the multiple hamartomas and cancers of Cowden syndrome must evade.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory microenvironment of Cowden syndrome lesions.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, in balance with the mTOR pathway (mTOR already mapped) hyperactivated by PTEN loss, regulates the metabolic homeostasis of the hamartomatous lesions of Cowden syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the proliferative signaling of the tumors of Cowden syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the tumors of Cowden syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the neoplasms of Cowden syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of the tumors of Cowden syndrome.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A-p16 cell-cycle control participates in the tumor-suppressor network whose disruption cooperates with PTEN loss in Cowden syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of the neoplasms of Cowden syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of the neoplasms of Cowden syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of Cowden syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of the neoplasms of Cowden syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of Cowden syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of Cowden syndrome.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — PI3K-insulin axis: PTEN opposes PI3K signalling downstream of the insulin receptor, so its loss in Cowden syndrome heightens insulin/PI3K-AKT signalling (both already mapped), the basis of both the hamartoma-tumour predisposition and reported insulin sensitivity.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Endometrial hormonal axis: Cowden syndrome confers a high endometrial cancer risk, an estrogen-driven cancer (estrogen already mapped) that progesterone opposes, so the estrogen-progesterone balance is central to the gynaecological surveillance and prevention.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Cancer immunosurveillance: MHC class II-restricted T-cell surveillance influences which of the many hamartomas and early cancers of Cowden syndrome progress, and antigen presentation is relevant to immunotherapy of any advanced tumours.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell responses (MHC class II already mapped) provide the immune surveillance influencing progression of the hamartomas and cancers of Cowden syndrome, and underlie the immunotherapy of any advanced tumours.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Hamartoma stroma: tumour-associated macrophages populate the many hamartomas and early cancers of Cowden syndrome, contributing to the growth-factor-rich stroma (VEGF and TGF-beta already mapped) that supports these PTEN-driven proliferations.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Vascular anomalies: Cowden syndrome includes vascular malformations, and nitric oxide with VEGF (already mapped) regulates the endothelial biology behind these anomalies, part of the broad tissue overgrowth of PTEN loss.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic overgrowth: the PI3K-AKT-mTOR pathway (already mapped) unleashed by PTEN loss intersects with leptin and the metabolic signalling (insulin already mapped) that contributes to the overgrowth and metabolic phenotype of Cowden syndrome.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipid metabolism: PTEN, through the PI3K-AKT pathway (already mapped), regulates cellular lipid and cholesterol metabolism, and its loss shifts the lipid handling that supports the proliferations of Cowden syndrome.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive stroma: IL-10 from the tumour-associated macrophages (already mapped) of the hamartomas and early cancers of Cowden syndrome dampens local immunity, part of the growth-permissive stroma of these PTEN-driven lesions.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an M2 phenotype (IL-10 already mapped), part of the growth-permissive immunosuppressive stroma of the hamartomas and early cancers of Cowden syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the permissive stroma around the PTEN-driven lesions of Cowden syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic-cancer link: adiponectin, with leptin (already mapped), links the PTEN-PI3K-AKT metabolic pathway (insulin already mapped) to the obesity-associated cancer risk of the proliferations of Cowden syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine-cancer milieu: resistin, with leptin and adiponectin (already mapped), links the PTEN-PI3K (already mapped) metabolic pathway to the obesity-associated cancer risk of Cowden syndrome.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Thyroid selenoproteins: selenium supports the selenoprotein deiodinase and antioxidant function of the thyroid (already mapped), the site of the nodular disease and cancer of Cowden syndrome.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Hamartoma stroma: PDGF drives the mesenchymal and stromal proliferation (collagen already mapped) of the hamartomas of Cowden syndrome, part of the PTEN (already mapped)-driven overgrowth.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Lhermitte-Duclos: the dysplastic cerebellar gangliocytoma (Lhermitte-Duclos disease; PTEN/mTOR already mapped) of the brain, and the macrocephaly, are the neurological features of Cowden syndrome.
- `connects-to` → **[Colorectal cancer](../colorectal-cancer/README.md)** — GI hamartomas/CRC: the hamartomatous and other colonic polyps of Cowden syndrome (PTEN already mapped) confer a raised colorectal-cancer risk, needing the surveillance.
- `connects-to` → **[Autism spectrum disorder](../autism-spectrum-disorder/README.md)** — Macrocephaly-autism: the PTEN (already mapped) mutations cause a macrocephaly-autism spectrum, linking Cowden syndrome to the neurodevelopmental phenotype.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity relevant to the breast, thyroid and endometrial cancers of Cowden syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the Cowden-syndrome tumours.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the PTEN-hamartoma tumours of Cowden syndrome.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the Cowden-syndrome tumours.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the PTEN-hamartoma tumour microenvironment of Cowden syndrome.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of Cowden syndrome.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the hamartoma stroma contribute to the angiogenesis (VEGF already mapped) and the immune microenvironment of the PTEN-hamartoma tumours of Cowden syndrome.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the Cowden-syndrome tumours.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the PTEN-hamartoma tumour stroma of Cowden syndrome.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^bubien-2013-cowden-cancer-risk]: Bubien V, Bonnet F, Brouste V, et al. High cumulative risks of cancer in patients with PTEN hamartoma tumour syndrome. *J Med Genet.* 2013;50(4):255-263. [doi:10.1136/jmedgenet-2012-101339](https://doi.org/10.1136/jmedgenet-2012-101339) · [PubMed 23335809](https://pubmed.ncbi.nlm.nih.gov/23335809/)
[^bennett-2010-klln-cowden]: Bennett KL, Mester J, Eng C. Germline epigenetic regulation of KILLIN in Cowden and Cowden-like syndrome. *JAMA.* 2010;304(24):2724-2731. [doi:10.1001/jama.2010.1877](https://doi.org/10.1001/jama.2010.1877) · [PubMed 21177507](https://pubmed.ncbi.nlm.nih.gov/21177507/)
