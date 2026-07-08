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
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Hypertrophic cardiomyopathy is a defining Noonan feature: RAS-MAPK overactivation from PTPN11/RAF1 mutations drives cardiomyocyte hypertrophy independent of sarcomere genes, so Noonan HCM often appears in infancy alongside the syndrome's pulmonary valve stenosis."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Noonan syndrome carries a bleeding diathesis: many patients have platelet dysfunction or factor XI/VIII/XII deficiencies, so easy bruising and surgical bleeding are common and warrant coagulation and platelet-function testing before any procedure."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "As a RASopathy, Noonan syndrome modestly raises cancer risk including rhabdomyosarcoma: constitutive RAS-MAPK signaling that drives the syndrome also promotes myogenic tumors, part of a spectrum that includes JMML, neuroblastoma, and brain tumors."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Noonan syndrome and neuroblastoma both stem from RAS-MAPK overactivity: Noonan from germline PTPN11/SOS1 activation, neuroblastoma often from somatic ALK or RAS lesions—Noonan raises neuroblastoma risk, one pathway shaping a malformation syndrome and a tumor."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Noonan syndrome commonly causes a bleeding tendency: many patients have von Willebrand factor and platelet-function defects, so easy bruising and surgical bleeding are common—coagulation screening is advised before any procedure in Noonan patients."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Noonan syndrome predisposes to myeloid leukemia: germline PTPN11 (SHP2) activation drives a JMML-like myeloproliferative disorder in infancy that is often self-limited but can progress, and the RAS-pathway link extends to AML—Ras overactivity dysregulating myelopoiesis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Congenital heart disease is central to Noonan syndrome: RAS/MAPK overactivity disrupts cardiac development, classically causing pulmonary valve stenosis and hypertrophic cardiomyopathy, so the cardiovascular system bears the syndrome's most serious manifestations."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Short stature in Noonan reflects disrupted growth signaling: RAS-pathway overactivity blunts the growth-hormone/IGF-1 axis, so children are short and growth-hormone therapy is used—though efficacy varies and RAS activation raises theoretical tumor concerns."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Noonan syndrome can weaken bone: reduced bone mineral density and increased fracture risk accompany the syndrome, reflecting RAS-pathway effects on bone metabolism—so skeletal health joins cardiac and growth issues in long-term Noonan care."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Noonan syndrome affects the developing nervous system: many children have developmental delay and learning differences, and RASopathy signaling shapes brain development, so neurodevelopmental support is part of managing this multisystem condition."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Noonan syndrome reshapes the skeleton and stature: short stature, a broad webbed neck, chest deformity (pectus) and scoliosis are characteristic, so the musculoskeletal features are central to recognizing this RAS-pathway syndrome."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Noonan syndrome affects the reproductive system in males: undescended testes (cryptorchidism) are common and can impair fertility, reflecting how RASopathy signaling disturbs gonadal development alongside the heart and growth abnormalities."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Short stature in Noonan syndrome involves the GH-IGF-1 axis: RAS-pathway overactivity blunts growth-hormone signaling and IGF-1 generation, so many children have low-normal IGF-1 and are treated with growth hormone to improve final height."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Noonan syndrome carries a raised leukemia risk: beyond the myeloproliferative JMML of infancy, RAS-pathway germline mutations predispose to acute leukemias including B-ALL, so persistent cytopenias or organomegaly warrant a blood and marrow evaluation."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eyes carry Noonan's diagnostic facial signs: hypertelorism, downslanting palpebral fissures and ptosis are hallmark features, and refractive errors and strabismus are common—so an eye exam supports the clinical diagnosis and protects vision."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "Noonan syndrome sits on a RASopathy spectrum that includes BRAF: while most cases stem from PTPN11, BRAF mutations cause the overlapping cardiofaciocutaneous syndrome, all sharing the overactive RAS-MAPK signaling behind the heart and growth defects."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Noonan syndrome disturbs the bone marrow: PTPN11 mutations can spark a juvenile myelomonocytic leukemia-like myeloproliferation in infancy—often self-limited but sometimes progressing—so blood counts are watched in affected children."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Noonan's hypertrophic cardiomyopathy runs partly through mTOR: overactive RAS feeds PI3K-AKT-mTOR signaling that thickens heart muscle, so mTOR inhibitors are being tested to reverse the cardiomyopathy that threatens these patients."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Noonan syndrome overdrives the AKT-mTOR growth axis: the RAS-pathway mutations that define it push signaling into PI3K-AKT-mTOR as well as ERK, helping explain the heart-muscle thickening and growth problems—and the rationale for mTOR inhibitors."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Faulty lymphatic endothelium underlies Noonan's swelling: abnormal development of lymphatic vessels causes the lymphedema and fetal cystic hygroma typical of the syndrome, and can lead to chylothorax—the lymphatic side of a RASopathy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Noonan syndrome reaches the brain: Chiari I malformation, hydrocephalus and learning differences are recognized features, so neurodevelopmental and structural brain issues join the heart and growth problems in the syndrome's care."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Noonan syndrome can malform the kidneys: renal and urinary-tract anomalies, such as a dilated collecting system, are recognized features that round out the syndrome's developmental defects."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Noonan's thickened heart leans on calcium: its hypertrophic cardiomyopathy disturbs the cardiomyocyte calcium handling that drives contraction, contributing to the stiff, poorly relaxing ventricle."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Noonan's RAS activation can expand the macrophage lineage: in young children it predisposes to a JMML-like myelomonocytic proliferation, overgrowing the monocyte-macrophage cells of the blood."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons reveal Noonan before and after birth: prenatal ultrasound flags the thick nuchal fold and cystic hygroma of lymphatic excess, while echocardiography after birth maps the pulmonary valve stenosis and hypertrophic cardiomyopathy that define the heart disease."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Noonan writes itself on the skin: curly or sparse hair, widespread keratosis pilaris, lymphedema, and — in the lentigines variant — a freckling of dark spots, cutaneous clues that steer the clinical diagnosis."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen often enlarges in Noonan: hepatosplenomegaly is common, especially when the syndrome's RAS overactivity tips into the JMML-like myeloproliferation that swells the blood-forming organs in early childhood."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Noonan's signature heart defect guards the lungs' gateway: pulmonary valve stenosis — often with a dysplastic, thickened valve — narrows the path from the right heart into the lungs, the most common cardiac lesion driving the diagnosis."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Noonan can leak the gut's lymph: intestinal lymphangiectasia and protein-losing enteropathy, tied to the syndrome's faulty lymphatic plumbing, drain protein from the small bowel and compound the feeding difficulties and failure to thrive of infancy."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reads Noonan's heart muscle: when the syndrome causes hypertrophic cardiomyopathy, the myocardium shows the chaotic myofibrillar disarray that distinguishes it from a normally thickened, athletic heart."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "A RASopathy with an autoimmune streak: Noonan patients show antithyroid and antinuclear antibodies and develop autoimmune thyroiditis and lupus more often than expected, immune dysregulation riding alongside the syndrome's overactive RAS-MAPK signaling."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The same RAS defect can derange the marrow: infants with Noonan may develop a juvenile myelomonocytic leukemia or a transient myeloproliferative disorder that crowds out red cells, the anemia and low counts revealing the blood's involvement."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "When Noonan's blood disorder flares, the liver swells: the juvenile myelomonocytic proliferation enlarges the liver and spleen, hepatosplenomegaly that, with the protein-losing gut, adds to the failure to thrive of a difficult infancy."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "The RASopathy reaches the developing brain: most children with Noonan have learning difficulties and attention problems, as the same overactive RAS-MAPK signaling that shapes the face and heart disturbs the circuits underlying learning and focus."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "Noonan's signaling defect predisposes to monocytic leukemia: germline PTPN11 mutations drive juvenile myelomonocytic leukemia, the childhood RAS-pathway counterpart of the adult chronic myelomonocytic leukemia, both fueled by hyperactive SHP2."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Noonan unsettles bone remodeling: RAS-MAPK dysregulation skews the osteoclast-osteoblast balance toward resorption, contributing to the reduced bone density and skeletal anomalies like pectus deformity seen across the syndrome."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The heart is the syndrome's gravest organ: hypertrophic cardiomyopathy and pulmonary valve stenosis from RAS-MAPK overdrive can thicken and obstruct the heart, driving some Noonan patients toward heart failure as a leading cause of early death."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Autoimmunity rides along: Noonan carries an increased rate of autoimmune thyroiditis and hypothyroidism, so thyroid antibodies and function are monitored as part of routine care even though the syndrome's core defect is in growth signaling."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "RAS-pathway signaling shapes the developing brain: beyond the learning difficulties and ADHD common in Noonan, autism spectrum features occur more often than in the general population, reflecting how this growth-signaling cascade tunes synapse formation."
  - target: 01-human/03-molecular/spred1
    relation: connects-to
    note: "It belongs to the RASopathy family: SPRED1 loss causes Legius syndrome, a milder NF1-like RASopathy, so SPRED1 anchors the overlapping RAS-MAPK disorders that Noonan must be distinguished from on the gene panel."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "The lymphatic-vascular defect reaches the lung circulation: Noonan and related RASopathies carry a recognized association with pulmonary arterial hypertension, compounding their congenital heart disease."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "Embryonal tumors join the spectrum: beyond the JMML predisposition, Noonan's RAS-MAPK overdrive carries a raised risk of childhood embryonal cancers including Wilms tumor, part of its tumor surveillance."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "SHP2 feeds JAK-STAT as well as RAS: the PTPN11/SHP2 mutations of Noonan amplify not only RAS-MAPK but STAT signaling, a crosstalk that contributes to its developmental features and leukemia predisposition."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "RAS-MAPK overdrive engages NF-κB: the constitutive RAS signaling of Noonan's RASopathy mutations activates NF-κB-linked survival and inflammatory pathways alongside the MAPK cascade."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "The syndrome carries a psychosocial toll: short stature, distinctive features, learning differences and cardiac disease in Noonan contribute to elevated rates of depression and anxiety."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its heart disease can throw clots to the brain: the hypertrophic cardiomyopathy, valve disease and arrhythmias of Noonan create conditions for cardioembolism, raising the risk of embolic stroke."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Congenital kidney anomalies set up later failure: Noonan frequently includes renal and urinary-tract malformations such as dysplasia or obstruction, which over years can progress toward chronic kidney disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Neonatal surgery and lymphatic dysplasia invite infection: early cardiac operations plus the lymphedema and chylous effusions of Noonan's lymphatic anomalies leave infants prone to severe infection and sepsis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "RAS dysregulation unsettles growth and gonads: Noonan brings short stature with partial growth-hormone insensitivity, delayed puberty and cryptorchidism, so endocrine assessment and GH therapy are routine in care."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The syndrome is written on the skin: Noonan features curly or sparse hair, keratosis pilaris, lymphedema and, in the lentigines variant, widespread café-au-lait macules and lentigines."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A complex lifelong condition fosters worry: the heart disease, short stature, social and learning difficulties and ongoing medical surveillance of Noonan syndrome are associated with raised anxiety."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It starts with feeding failure and leaks protein: Noonan infants struggle to feed and fail to thrive, and the intestinal lymphangiectasia of its lymphatic dysplasia causes protein-losing enteropathy."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its faulty lymphatics flood the chest: the lymphatic dysplasia of Noonan syndrome causes chylothorax and chylous pleural effusions, sometimes from birth, compromising breathing."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its developmental defects reach the kidneys: Noonan syndrome includes congenital renal and urinary-tract anomalies such as dysplasia, duplication and obstruction that can impair kidney function."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its RAS pathway disturbs immunity: Noonan syndrome can feature immune dysregulation with autoimmunity and lymphoproliferation, and RAS-pathway activation predisposes to juvenile myelomonocytic leukaemia."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Its heart defects invite endocarditis: the congenital heart disease of Noonan syndrome raises the risk of infective endocarditis, classically from Staphylococcus aureus and viridans streptococci."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "Beta-blockers ease its thickened heart: the hypertrophic cardiomyopathy of Noonan syndrome is managed with beta-blockers to reduce outflow obstruction and control arrhythmia."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A pathway drug for its heart disease: MEK inhibitors that block the overactive RAS-MAPK signalling of Noonan syndrome are being trialled to reverse its hypertrophic cardiomyopathy."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "A lentigines-and-heart comparator: like the LEOPARD variant of Noonan syndrome, Carney complex combines multiple skin lentigines with cardiac disease, here from cAMP rather than RAS signalling."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "A fellow syndromic cause of childhood heart tumours: like tuberous sclerosis with its cardiac rhabdomyomas, Noonan syndrome produces congenital heart disease in a multisystem autosomal-dominant disorder."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo for its leukaemias: Noonan syndrome greatly raises the risk of juvenile myelomonocytic leukaemia and other myeloid neoplasms, treated with chemotherapy and stem-cell transplant."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "A dysplastic pulmonary valve defines its heart disease: Noonan syndrome characteristically causes pulmonary valve stenosis from a thickened dysplastic valve, alongside hypertrophic cardiomyopathy."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Its ECG bears a signature: Noonan syndrome produces characteristic conduction abnormalities and a superior QRS axis, reflecting the RASopathy's effect on cardiac development."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It thickens the heart muscle: hypertrophic cardiomyopathy is a major Noonan feature—especially with PTPN11 and RAF1 mutations—as overactive RAS-MAPK drives myocardial hypertrophy independent of the pulmonary valve stenosis that also marks the syndrome."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "RAS dysregulation reaches the skeleton: Noonan syndrome causes short stature, pectus deformity and reduced cortical bone density, and growth-hormone signalling blunted by overactive RAS-MAPK contributes to the impaired bone growth."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "A milder, mixed bleeding tendency: Noonan syndrome carries a bleeding diathesis from factor XI/VIII deficiency and platelet dysfunction—not the single clotting-factor loss of haemophilia A, but a reason to screen coagulation before surgery."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "JMML and myeloid disease: PTPN11/RAS mutations in Noonan cause a juvenile myelomonocytic leukaemia-like myeloproliferative disorder in infancy, often self-limiting, and raise overall leukaemia risk."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Chylothorax and lymphatic dysplasia: Noonan's abnormal lymphatics can leak chyle into the pleural space and cause pulmonary lymphangiectasia, flooding the region around the alveoli and impairing breathing."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "A prenatal presentation: severe Noonan can cause fetal hydrops and an oedematous, enlarged placenta from lymphatic dysplasia, alongside increased nuchal translucency seen on prenatal ultrasound."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "RAS-driven hypertrophy: the hypertrophic cardiomyopathy of Noonan thickens the myocardium and impairs the troponin-regulated contractile apparatus, phenocopying sarcomeric HCM through overactive RAS-MAPK signalling rather than a sarcomere-gene mutation."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Monitoring the strained heart: the hypertrophic cardiomyopathy and pulmonary-valve stenosis of Noonan raise wall stress, lifting BNP as a biomarker of the cardiac burden these congenital lesions impose."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "A RASopathy tumour: gastrointestinal stromal tumours occur in Noonan syndrome as part of the broader cancer predisposition of the RASopathies, the same RAS-MAPK overactivity driving the neoplasm."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Hypertrophic heart: calcineurin-NFAT signalling, amplified by RAS-MAPK overactivity, drives the hypertrophic cardiomyopathy that is a hallmark cardiac feature of Noonan syndrome."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Lymphatic dysplasia: dysregulated VEGF-driven lymphangiogenesis underlies the lymphoedema, chylothorax and lymphatic malformations characteristic of Noonan syndrome."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Proliferative drive: RAS-MAPK hyperactivation in Noonan syndrome upregulates cyclin D1, contributing to its predisposition to juvenile myelomonocytic leukaemia and other neoplasms."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "RAS-driven oncogene: the constitutive RAS-MAPK signalling of Noonan syndrome upregulates MYC, underlying its predisposition to JMML and other childhood cancers."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Parallel PI3K pathway: PI3K/AKT signalling crosstalks with the hyperactive RAS-MAPK axis in Noonan syndrome, contributing to its cardiac hypertrophy and growth phenotypes."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Growth-factor signalling: PDGF acts through the RAS-MAPK pathway dysregulated in Noonan syndrome, feeding into the developmental and proliferative abnormalities of the disorder."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Convergent hypertrophy node: chronic RAS-MAPK and PI3K-AKT signalling in Noonan syndrome inactivates GSK-3β, removing its anti-hypertrophic brake on cardiomyocytes and contributing to the hypertrophic cardiomyopathy seen in the disorder."
  - target: 01-human/03-molecular/serca2a
    relation: connects-to
    note: "Diastolic dysfunction: SERCA2a-mediated SR calcium reuptake is impaired in the hypertrophied Noonan myocardium, slowing relaxation and contributing to the diastolic dysfunction that complicates the syndrome's hypertrophic cardiomyopathy."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Lymphatic dysplasia: Noonan and the broader RASopathy spectrum cause lymphedema and central conducting lymphatic anomalies, where dysregulated angiopoietin-Tie2 signalling underlies the malformed, leaky lymphatic channels."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Hypertrophic cardiomyopathy fibrosis: TGF-β drives the interstitial myocardial fibrosis of Noonan HCM and the myxomatous thickening of the dysplastic pulmonary valve, the structural cardiac lesions that define the syndrome's heart disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K brake and tumour risk: PTEN is the lipid-phosphatase brake on the RAS-PI3K arm hyperactivated in Noonan; somatic second hits in this pathway underlie the predisposition to juvenile myelomonocytic leukaemia and embryonal tumours."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Cognitive deficits: RAS-MAPK signalling is the effector arm of BDNF-TrkB synaptic plasticity, and its constitutive dysregulation in Noonan disrupts hippocampal long-term potentiation, contributing to the learning difficulties of the RASopathies."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Genital and pubertal: cryptorchidism is common in Noonan boys and, with the disordered RAS-MAPK signalling, can impair testosterone production and delay puberty, contributing to the reduced fertility seen in affected males."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Skeletal manifestations: Noonan syndrome features reduced bone mineral density and skeletal anomalies (pectus, scoliosis), reflecting RANKL-driven osteoclast activity dysregulated within the broader RASopathy effects on bone."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Cardiac contraction: the hypertrophic cardiomyopathy of Noonan disrupts myocardial calcium handling and excitation-contraction coupling, the ionic basis of the impaired contractility and arrhythmia risk that accompany the structural heart disease."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Valve development: NOTCH signalling governs cardiac valve and outflow-tract development, and its interplay with the RAS-MAPK overactivation of Noonan contributes to the pulmonary-valve stenosis that is the commonest cardiac defect."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Cardiac conduction: gap-junction connexin-43 couples cardiomyocytes for coordinated conduction, relevant to the conduction abnormalities and arrhythmia risk of the Noonan heart."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Leukaemia predisposition: RAS-MAPK overactivation drives cyclin-D1 (mapped) and E2F1-dependent cell-cycle entry, underpinning the juvenile myelomonocytic leukaemia predisposition of Noonan syndrome."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "SHP2-cytokine signalling: the PTPN11/SHP2 phosphatase mutated in Noonan syndrome positively regulates both RAS-MAPK and JAK-STAT signalling, the latter contributing to the cytokine-driven myeloproliferation of its JMML predisposition."
  - target: 01-human/03-molecular/ryr2
    relation: connects-to
    note: "Cardiac calcium handling: RyR2-mediated sarcoplasmic calcium release (with SERCA2a already mapped) governs the excitation-contraction coupling of the cardiomyocyte, stressed in the hypertrophic cardiomyopathy of Noonan syndrome."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: the RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) restrains the RAS-MAPK-driven proliferation underlying the leukaemia predisposition of Noonan syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 drives the cardiac fibrosis underlying the hypertrophic cardiomyopathy of Noonan syndrome and is a biomarker of its progression."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) contributes to the cardiac and connective-tissue remodelling of Noonan syndrome."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "The CDK4/6-cyclin-D inhibitor CDKN2A (cyclin-D1 mapped) is a brake on the RAS-MAPK-driven myelomonocytic proliferation that predisposes Noonan syndrome to juvenile myelomonocytic leukaemia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune surveillance relevant to the leukemia predisposition of Noonan syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the inflammatory tone associated with the RAS-MAPK dysregulation of Noonan syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, antagonised by the constitutive RAS-PI3K-AKT signalling of Noonan syndrome, modulate the growth and developmental programmes it disrupts."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1 and RB1 already mapped) downstream of the RAS-MAPK hyperactivation contributes to the proliferative and developmental effects of Noonan syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the myeloid inflammatory activation relevant to the juvenile-myelomonocytic-leukemia predisposition of Noonan syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic signaling contributes to the cardiac hypertrophy and developmental features of Noonan syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of receptor tyrosine kinases, whose signals PTPN11/SHP2 amplifies (PTPN11 already mapped), participates in the RAS-MAPK hyperactivation of Noonan syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the developmental gene programs affected in Noonan syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the cardiomyocyte homeostasis relevant to the hypertrophic cardiomyopathy of Noonan syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the cardiac and growth-related metabolic phenotypes of Noonan syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid signaling participates in the myeloproliferative predisposition and immune features of Noonan syndrome."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-p53 signaling participates in the cellular-proliferation control relevant to the leukemia predisposition of Noonan syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the cardiac-developmental and vascular processes relevant to Noonan syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory and cardiac-remodeling processes relevant to Noonan syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the cardiac-remodeling and immune processes relevant to Noonan syndrome."
  - target: 01-human/03-molecular/phospholamban
    relation: connects-to
    note: "Diastolic calcium handling: Noonan hypertrophic cardiomyopathy impairs relaxation via the phospholamban-SERCA2a axis (SERCA already mapped) controlling diastolic calcium reuptake into the sarcoplasmic reticulum, the basis of the stiff ventricle."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Skeletal fragility: Noonan syndrome carries reduced bone mineral density and osteopenia, and sclerostin is the osteocyte Wnt brake restraining bone formation, mechanistically linking the RASopathy to the low bone mass tracked alongside its osteoporosis risk."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Endocrine autoimmunity: Noonan syndrome is associated with an increased incidence of autoimmune thyroiditis and subclinical hypothyroidism, so thyroid-hormone deficiency is a recurrent endocrine comorbidity beyond the growth-hormone axis already mapped."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Cardiomyopathy management: the hypertrophic cardiomyopathy of Noonan syndrome (troponin/BNP already mapped) is treated with beta-blockade at the beta1-adrenergic receptor to reduce outflow obstruction and protect the RAS-driven hypertrophied heart."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Cardiac remodelling: angiotensin II drives the fibrosis and hypertrophy of cardiac remodelling, a pathway overlaid on the RAS-MAPK (already mapped) overactivity that produces the hypertrophic cardiomyopathy of Noonan syndrome."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Autoimmune thyroiditis: MHC class II-restricted presentation of thyroid antigens underlies the autoimmune thyroiditis (thyroid hormones already mapped) that is more common in Noonan syndrome, part of its immune-endocrine comorbidity."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Myeloproliferation and bleeding: PTPN11-mutant Noonan syndrome carries a juvenile myelomonocytic leukaemia-like myeloproliferation and a bleeding diathesis (von Willebrand factor already mapped), both of which can lower haemoglobin."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Cardiac RAAS: aldosterone, with angiotensin II (already mapped), drives the fibrosis of the cardiac remodelling overlaid on the RAS-MAPK overactivity that produces the hypertrophic cardiomyopathy of Noonan syndrome."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Vascular and lymphatic tone: nitric oxide regulates the vascular and lymphatic tone disturbed in Noonan syndrome, contributing to the endothelial function relevant to its cardiovascular and lymphatic (already mapped) manifestations."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Bleeding diathesis: Noonan syndrome carries a bleeding tendency from clotting-factor deficiencies and platelet dysfunction (von Willebrand factor already mapped), and the coagulation abnormalities involving fibrinogen and factors require care around surgery."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "RAAS and cardiac remodelling: the renin-angiotensin-aldosterone system (angiotensin II and aldosterone already mapped), overlaid on the RAS-MAPK overactivity, contributes to the fibrosis and hypertrophic cardiomyopathy of Noonan syndrome."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Cardiac electrolyte balance: magnesium, with the calcium cycling (SERCA2a and RYR2 already mapped), influences the myocardial excitability and arrhythmia risk of the hypertrophic cardiomyopathy of Noonan syndrome."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Myocardial excitability: potassium, with the magnesium and calcium cycling (SERCA2a and RYR2 already mapped), sets the myocardial repolarisation and the arrhythmia risk of the hypertrophic cardiomyopathy of Noonan syndrome."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Skeletal features: the short stature (growth hormone and IGF-1 already mapped), the pectus deformity and the cubitus valgus of Noonan syndrome reflect the skeletal involvement (RANKL and sclerostin already mapped) of the RASopathy."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Neurodevelopment: the mild developmental delay and the learning difficulties (BDNF already mapped) of Noonan syndrome reflect the effect of the RAS-MAPK (already mapped) overactivity on the developing brain."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Growth-metabolic adipokine: leptin reflects the short stature (growth hormone and IGF-1 already mapped) and the altered growth and metabolism of Noonan syndrome."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 allergic tendency: IL-4 is part of the type-2 immune arm of the increased allergic/atopic and autoimmune tendency reported in the RASopathies including Noonan syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm of the atopic tendency of the RAS-MAPK (already mapped) overactivity of Noonan syndrome."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil atopic arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophil arm of the allergic/atopic tendency of the RASopathy Noonan syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic profile of Noonan syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic profile of Noonan syndrome."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immune arm: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation and the JMML-spectrum myeloproliferation risk (PTPN11 already mapped) of Noonan syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm balancing the type-2 (IL-4, IL-5 and IL-13 already mapped) dimension of the immune profile of Noonan syndrome."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune dimension of Noonan syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 effector: IL-17A is the Th17 effector cytokine complementing the Th1/type-2 (IFN-γ, IL-4, IL-5 and IL-13 already mapped) balance of the immune profile of Noonan syndrome."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 arm) of the immune-inflammatory dimension of Noonan syndrome."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune profile of Noonan syndrome."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the immune-inflammatory dimension of Noonan syndrome."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells: the mast cells (via the KIT-adjacent RAS/MAPK signalling, ERK already mapped) contribute to the type-2 (IgE already mapped) immune dimension of Noonan syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement: the complement C3 activation is part of the innate immune dimension and the lymphatic-dysplasia-associated inflammation of Noonan syndrome."
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
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — Chronic RAS-MAPK and PI3K-AKT signaling in Noonan syndrome inactivates GSK-3β, removing its anti-hypertrophic brake on cardiomyocytes—a convergent signaling node contributing to the hypertrophic cardiomyopathy that drives much of the syndrome's cardiac morbidity.
- `connects-to` → **[SERCA2a](../../03-molecular/serca2a/README.md)** — SERCA2a-mediated sarcoplasmic-reticulum calcium reuptake is impaired in the hypertrophied Noonan myocardium, slowing relaxation and contributing to the diastolic dysfunction that complicates the disorder's hypertrophic cardiomyopathy beyond the systolic obstruction.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Noonan and the broader RASopathy spectrum cause lymphedema and central conducting lymphatic anomalies, where dysregulated angiopoietin-Tie2 signaling underlies the malformed, leaky lymphatic channels—linking the RAS pathway to the syndrome's lymphatic phenotype.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Congenital heart disease affects ~80% of Noonan syndrome: a dysplastic, thickened pulmonary valve causes stenosis in ~50-60% (often balloon-resistant), while RAF1 mutations drive hypertrophic cardiomyopathy in ~20-30%, which MEK inhibitors can reverse.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Every Noonan gene — PTPN11, SOS1, RAF1, KRAS, RIT1, LZTR1 — converges on ERK1/2 hyperactivation during embryogenesis, and the degree of ERK activity grades severity; because MEK1/2 sits just upstream of ERK, MEK inhibitors (trametinib) can normalize signaling and reverse HCM.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — LZTR1 links Noonan syndrome to schwannomatosis through opposite effects of the same gene: dominant LZTR1 mutations cause Noonan (RAS accumulation, developmental phenotype), whereas biallelic LOF or dominant-negative LZTR1 causes schwannomatosis (multiple painful schwannomas).
- `connects-to` → **[Marfan Syndrome](../marfan-syndrome/README.md)** — Noonan and Marfan are both autosomal-dominant multisystem syndromes causing chest-wall deformity, scoliosis, and congenital heart disease, so they share a clinical differential — but are unrelated: Noonan is a RASopathy while Marfan is a fibrillin-1 connective-tissue disorder.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Noonan syndrome and neurofibromatosis type 1 are overlapping RASopathies — both hyperactivate RAS-MAPK and share café-au-lait spots, pulmonary stenosis, and short stature — but via different lesions: NF1 loses the RAS-GAP neurofibromin while Noonan gains function in SHP2/PTPN11.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Lymphatic dysplasia is a characteristic feature of Noonan syndrome: faulty RAS-MAPK during lymphangiogenesis produces fetal cystic hygroma and nuchal edema (often the first prenatal clue), peripheral lymphedema, and occasionally chylothorax — a developmental lymphatic defect.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Hypertrophic cardiomyopathy is a defining Noonan feature: RAS-MAPK overactivation from PTPN11/RAF1 mutations drives cardiomyocyte hypertrophy independent of sarcomere genes, so Noonan HCM often appears in infancy alongside the syndrome's pulmonary valve stenosis.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Noonan syndrome carries a bleeding diathesis: many patients have platelet dysfunction or factor XI/VIII/XII deficiencies, so easy bruising and surgical bleeding are common and warrant coagulation and platelet-function testing before any procedure.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — As a RASopathy, Noonan syndrome modestly raises cancer risk including rhabdomyosarcoma: constitutive RAS-MAPK signaling that drives the syndrome also promotes myogenic tumors, part of a spectrum that includes JMML, neuroblastoma, and brain tumors.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Noonan syndrome and neuroblastoma both stem from RAS-MAPK overactivity: Noonan from germline PTPN11/SOS1 activation, neuroblastoma often from somatic ALK or RAS lesions—Noonan raises neuroblastoma risk, one pathway shaping a malformation syndrome and a tumor.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Noonan syndrome commonly causes a bleeding tendency: many patients have von Willebrand factor and platelet-function defects, so easy bruising and surgical bleeding are common—coagulation screening is advised before any procedure in Noonan patients.
- `connects-to` → **[AML](../aml/README.md)** — Noonan syndrome predisposes to myeloid leukemia: germline PTPN11 (SHP2) activation drives a JMML-like myeloproliferative disorder in infancy that is often self-limited but can progress, and the RAS-pathway link extends to AML—Ras overactivity dysregulating myelopoiesis.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Congenital heart disease is central to Noonan syndrome: RAS/MAPK overactivity disrupts cardiac development, classically causing pulmonary valve stenosis and hypertrophic cardiomyopathy, so the cardiovascular system bears the syndrome's most serious manifestations.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Short stature in Noonan reflects disrupted growth signaling: RAS-pathway overactivity blunts the growth-hormone/IGF-1 axis, so children are short and growth-hormone therapy is used—though efficacy varies and RAS activation raises theoretical tumor concerns.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Noonan syndrome can weaken bone: reduced bone mineral density and increased fracture risk accompany the syndrome, reflecting RAS-pathway effects on bone metabolism—so skeletal health joins cardiac and growth issues in long-term Noonan care.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Noonan syndrome affects the developing nervous system: many children have developmental delay and learning differences, and RASopathy signaling shapes brain development, so neurodevelopmental support is part of managing this multisystem condition.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Noonan syndrome reshapes the skeleton and stature: short stature, a broad webbed neck, chest deformity (pectus) and scoliosis are characteristic, so the musculoskeletal features are central to recognizing this RAS-pathway syndrome.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Noonan syndrome affects the reproductive system in males: undescended testes (cryptorchidism) are common and can impair fertility, reflecting how RASopathy signaling disturbs gonadal development alongside the heart and growth abnormalities.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Short stature in Noonan syndrome involves the GH-IGF-1 axis: RAS-pathway overactivity blunts growth-hormone signaling and IGF-1 generation, so many children have low-normal IGF-1 and are treated with growth hormone to improve final height.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — Noonan syndrome carries a raised leukemia risk: beyond the myeloproliferative JMML of infancy, RAS-pathway germline mutations predispose to acute leukemias including B-ALL, so persistent cytopenias or organomegaly warrant a blood and marrow evaluation.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eyes carry Noonan's diagnostic facial signs: hypertelorism, downslanting palpebral fissures and ptosis are hallmark features, and refractive errors and strabismus are common—so an eye exam supports the clinical diagnosis and protects vision.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — Noonan syndrome sits on a RASopathy spectrum that includes BRAF: while most cases stem from PTPN11, BRAF mutations cause the overlapping cardiofaciocutaneous syndrome, all sharing the overactive RAS-MAPK signaling behind the heart and growth defects.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Noonan syndrome disturbs the bone marrow: PTPN11 mutations can spark a juvenile myelomonocytic leukemia-like myeloproliferation in infancy—often self-limited but sometimes progressing—so blood counts are watched in affected children.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Noonan's hypertrophic cardiomyopathy runs partly through mTOR: overactive RAS feeds PI3K-AKT-mTOR signaling that thickens heart muscle, so mTOR inhibitors are being tested to reverse the cardiomyopathy that threatens these patients.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Noonan syndrome overdrives the AKT-mTOR growth axis: the RAS-pathway mutations that define it push signaling into PI3K-AKT-mTOR as well as ERK, helping explain the heart-muscle thickening and growth problems—and the rationale for mTOR inhibitors.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Faulty lymphatic endothelium underlies Noonan's swelling: abnormal development of lymphatic vessels causes the lymphedema and fetal cystic hygroma typical of the syndrome, and can lead to chylothorax—the lymphatic side of a RASopathy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Noonan syndrome reaches the brain: Chiari I malformation, hydrocephalus and learning differences are recognized features, so neurodevelopmental and structural brain issues join the heart and growth problems in the syndrome's care.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Noonan syndrome can malform the kidneys: renal and urinary-tract anomalies, such as a dilated collecting system, are recognized features that round out the syndrome's developmental defects.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Noonan's thickened heart leans on calcium: its hypertrophic cardiomyopathy disturbs the cardiomyocyte calcium handling that drives contraction, contributing to the stiff, poorly relaxing ventricle.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Noonan's RAS activation can expand the macrophage lineage: in young children it predisposes to a JMML-like myelomonocytic proliferation, overgrowing the monocyte-macrophage cells of the blood.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons reveal Noonan before and after birth: prenatal ultrasound flags the thick nuchal fold and cystic hygroma of lymphatic excess, while echocardiography after birth maps the pulmonary valve stenosis and hypertrophic cardiomyopathy that define the heart disease.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Noonan writes itself on the skin: curly or sparse hair, widespread keratosis pilaris, lymphedema, and — in the lentigines variant — a freckling of dark spots, cutaneous clues that steer the clinical diagnosis.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen often enlarges in Noonan: hepatosplenomegaly is common, especially when the syndrome's RAS overactivity tips into the JMML-like myeloproliferation that swells the blood-forming organs in early childhood.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Noonan's signature heart defect guards the lungs' gateway: pulmonary valve stenosis — often with a dysplastic, thickened valve — narrows the path from the right heart into the lungs, the most common cardiac lesion driving the diagnosis.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Noonan can leak the gut's lymph: intestinal lymphangiectasia and protein-losing enteropathy, tied to the syndrome's faulty lymphatic plumbing, drain protein from the small bowel and compound the feeding difficulties and failure to thrive of infancy.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reads Noonan's heart muscle: when the syndrome causes hypertrophic cardiomyopathy, the myocardium shows the chaotic myofibrillar disarray that distinguishes it from a normally thickened, athletic heart.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — A RASopathy with an autoimmune streak: Noonan patients show antithyroid and antinuclear antibodies and develop autoimmune thyroiditis and lupus more often than expected, immune dysregulation riding alongside the syndrome's overactive RAS-MAPK signaling.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The same RAS defect can derange the marrow: infants with Noonan may develop a juvenile myelomonocytic leukemia or a transient myeloproliferative disorder that crowds out red cells, the anemia and low counts revealing the blood's involvement.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — When Noonan's blood disorder flares, the liver swells: the juvenile myelomonocytic proliferation enlarges the liver and spleen, hepatosplenomegaly that, with the protein-losing gut, adds to the failure to thrive of a difficult infancy.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — The RASopathy reaches the developing brain: most children with Noonan have learning difficulties and attention problems, as the same overactive RAS-MAPK signaling that shapes the face and heart disturbs the circuits underlying learning and focus.
- `connects-to` → **[Chronic Myelomonocytic Leukemia](../cmml/README.md)** — Noonan's signaling defect predisposes to monocytic leukemia: germline PTPN11 mutations drive juvenile myelomonocytic leukemia, the childhood RAS-pathway counterpart of the adult chronic myelomonocytic leukemia, both fueled by hyperactive SHP2.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Noonan unsettles bone remodeling: RAS-MAPK dysregulation skews the osteoclast-osteoblast balance toward resorption, contributing to the reduced bone density and skeletal anomalies like pectus deformity seen across the syndrome.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The heart is the syndrome's gravest organ: hypertrophic cardiomyopathy and pulmonary valve stenosis from RAS-MAPK overdrive can thicken and obstruct the heart, driving some Noonan patients toward heart failure as a leading cause of early death.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Autoimmunity rides along: Noonan carries an increased rate of autoimmune thyroiditis and hypothyroidism, so thyroid antibodies and function are monitored as part of routine care even though the syndrome's core defect is in growth signaling.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — RAS-pathway signaling shapes the developing brain: beyond the learning difficulties and ADHD common in Noonan, autism spectrum features occur more often than in the general population, reflecting how this growth-signaling cascade tunes synapse formation.
- `connects-to` → **[SPRED1](../../03-molecular/spred1/README.md)** — It belongs to the RASopathy family: SPRED1 loss causes Legius syndrome, a milder NF1-like RASopathy, so SPRED1 anchors the overlapping RAS-MAPK disorders that Noonan must be distinguished from on the gene panel.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — The lymphatic-vascular defect reaches the lung circulation: Noonan and related RASopathies carry a recognized association with pulmonary arterial hypertension, compounding their congenital heart disease.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — Embryonal tumors join the spectrum: beyond the JMML predisposition, Noonan's RAS-MAPK overdrive carries a raised risk of childhood embryonal cancers including Wilms tumor, part of its tumor surveillance.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — SHP2 feeds JAK-STAT as well as RAS: the PTPN11/SHP2 mutations of Noonan amplify not only RAS-MAPK but STAT signaling, a crosstalk that contributes to its developmental features and leukemia predisposition.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — RAS-MAPK overdrive engages NF-κB: the constitutive RAS signaling of Noonan's RASopathy mutations activates NF-κB-linked survival and inflammatory pathways alongside the MAPK cascade.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — The syndrome carries a psychosocial toll: short stature, distinctive features, learning differences and cardiac disease in Noonan contribute to elevated rates of depression and anxiety.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its heart disease can throw clots to the brain: the hypertrophic cardiomyopathy, valve disease and arrhythmias of Noonan create conditions for cardioembolism, raising the risk of embolic stroke.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Congenital kidney anomalies set up later failure: Noonan frequently includes renal and urinary-tract malformations such as dysplasia or obstruction, which over years can progress toward chronic kidney disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Neonatal surgery and lymphatic dysplasia invite infection: early cardiac operations plus the lymphedema and chylous effusions of Noonan's lymphatic anomalies leave infants prone to severe infection and sepsis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — RAS dysregulation unsettles growth and gonads: Noonan brings short stature with partial growth-hormone insensitivity, delayed puberty and cryptorchidism, so endocrine assessment and GH therapy are routine in care.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The syndrome is written on the skin: Noonan features curly or sparse hair, keratosis pilaris, lymphedema and, in the lentigines variant, widespread café-au-lait macules and lentigines.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A complex lifelong condition fosters worry: the heart disease, short stature, social and learning difficulties and ongoing medical surveillance of Noonan syndrome are associated with raised anxiety.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It starts with feeding failure and leaks protein: Noonan infants struggle to feed and fail to thrive, and the intestinal lymphangiectasia of its lymphatic dysplasia causes protein-losing enteropathy.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its faulty lymphatics flood the chest: the lymphatic dysplasia of Noonan syndrome causes chylothorax and chylous pleural effusions, sometimes from birth, compromising breathing.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its developmental defects reach the kidneys: Noonan syndrome includes congenital renal and urinary-tract anomalies such as dysplasia, duplication and obstruction that can impair kidney function.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its RAS pathway disturbs immunity: Noonan syndrome can feature immune dysregulation with autoimmunity and lymphoproliferation, and RAS-pathway activation predisposes to juvenile myelomonocytic leukaemia.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Its heart defects invite endocarditis: the congenital heart disease of Noonan syndrome raises the risk of infective endocarditis, classically from Staphylococcus aureus and viridans streptococci.
- `connects-to` → **[Beta-Blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — Beta-blockers ease its thickened heart: the hypertrophic cardiomyopathy of Noonan syndrome is managed with beta-blockers to reduce outflow obstruction and control arrhythmia.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A pathway drug for its heart disease: MEK inhibitors that block the overactive RAS-MAPK signalling of Noonan syndrome are being trialled to reverse its hypertrophic cardiomyopathy.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — A lentigines-and-heart comparator: like the LEOPARD variant of Noonan syndrome, Carney complex combines multiple skin lentigines with cardiac disease, here from cAMP rather than RAS signalling.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — A fellow syndromic cause of childhood heart tumours: like tuberous sclerosis with its cardiac rhabdomyomas, Noonan syndrome produces congenital heart disease in a multisystem autosomal-dominant disorder.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo for its leukaemias: Noonan syndrome greatly raises the risk of juvenile myelomonocytic leukaemia and other myeloid neoplasms, treated with chemotherapy and stem-cell transplant.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — A dysplastic pulmonary valve defines its heart disease: Noonan syndrome characteristically causes pulmonary valve stenosis from a thickened dysplastic valve, alongside hypertrophic cardiomyopathy.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Its ECG bears a signature: Noonan syndrome produces characteristic conduction abnormalities and a superior QRS axis, reflecting the RASopathy's effect on cardiac development.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It thickens the heart muscle: hypertrophic cardiomyopathy is a major Noonan feature—especially with PTPN11 and RAF1 mutations—as overactive RAS-MAPK drives myocardial hypertrophy independent of the pulmonary valve stenosis that also marks the syndrome.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — RAS dysregulation reaches the skeleton: Noonan syndrome causes short stature, pectus deformity and reduced cortical bone density, and growth-hormone signalling blunted by overactive RAS-MAPK contributes to the impaired bone growth.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — A milder, mixed bleeding tendency: Noonan syndrome carries a bleeding diathesis from factor XI/VIII deficiency and platelet dysfunction—not the single clotting-factor loss of haemophilia A, but a reason to screen coagulation before surgery.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — JMML and myeloid disease: PTPN11/RAS mutations in Noonan cause a juvenile myelomonocytic leukaemia-like myeloproliferative disorder in infancy, often self-limiting, and raise overall leukaemia risk.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Chylothorax and lymphatic dysplasia: Noonan's abnormal lymphatics can leak chyle into the pleural space and cause pulmonary lymphangiectasia, flooding the region around the alveoli and impairing breathing.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — A prenatal presentation: severe Noonan can cause fetal hydrops and an oedematous, enlarged placenta from lymphatic dysplasia, alongside increased nuchal translucency seen on prenatal ultrasound.
- `connects-to` → **[Troponin Complex](../../03-molecular/troponin-complex/README.md)** — RAS-driven hypertrophy: the hypertrophic cardiomyopathy of Noonan thickens the myocardium and impairs the troponin-regulated contractile apparatus, phenocopying sarcomeric HCM through overactive RAS-MAPK signalling rather than a sarcomere-gene mutation.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Monitoring the strained heart: the hypertrophic cardiomyopathy and pulmonary-valve stenosis of Noonan raise wall stress, lifting BNP as a biomarker of the cardiac burden these congenital lesions impose.
- `connects-to` → **[GIST](../gist/README.md)** — A RASopathy tumour: gastrointestinal stromal tumours occur in Noonan syndrome as part of the broader cancer predisposition of the RASopathies, the same RAS-MAPK overactivity driving the neoplasm.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Hypertrophic heart: calcineurin-NFAT signalling, amplified by RAS-MAPK overactivity, drives the hypertrophic cardiomyopathy that is a hallmark cardiac feature of Noonan syndrome.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Lymphatic dysplasia: dysregulated VEGF-driven lymphangiogenesis underlies the lymphoedema, chylothorax and lymphatic malformations characteristic of Noonan syndrome.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Proliferative drive: RAS-MAPK hyperactivation in Noonan syndrome upregulates cyclin D1, contributing to its predisposition to juvenile myelomonocytic leukaemia and other neoplasms.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — RAS-driven oncogene: the constitutive RAS-MAPK signalling of Noonan syndrome upregulates MYC, underlying its predisposition to JMML and other childhood cancers.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Parallel PI3K pathway: PI3K/AKT signalling crosstalks with the hyperactive RAS-MAPK axis in Noonan syndrome, contributing to its cardiac hypertrophy and growth phenotypes.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Growth-factor signalling: PDGF acts through the RAS-MAPK pathway dysregulated in Noonan syndrome, feeding into the developmental and proliferative abnormalities of the disorder.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the interstitial myocardial fibrosis of Noonan hypertrophic cardiomyopathy and the myxomatous thickening of the dysplastic pulmonary valve, the structural cardiac lesions that define the syndrome's heart disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN is the lipid-phosphatase brake on the RAS-PI3K arm hyperactivated in Noonan; somatic second hits in this pathway underlie the predisposition to juvenile myelomonocytic leukemia and embryonal tumors.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — RAS-MAPK signaling is the effector arm of BDNF-TrkB synaptic plasticity, and its constitutive dysregulation in Noonan disrupts hippocampal long-term potentiation, contributing to the learning difficulties of the RASopathies.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Cryptorchidism is common in Noonan boys and, with the disordered RAS-MAPK signaling, can impair testosterone production and delay puberty, contributing to the reduced fertility seen in affected males.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Noonan syndrome features reduced bone mineral density and skeletal anomalies (pectus, scoliosis), reflecting RANKL-driven osteoclast activity dysregulated within the broader RASopathy effects on bone.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — The hypertrophic cardiomyopathy of Noonan disrupts myocardial calcium handling and excitation-contraction coupling, the ionic basis of the impaired contractility and arrhythmia risk that accompany the structural heart disease.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling governs cardiac valve and outflow-tract development, and its interplay with the RAS-MAPK overactivation of Noonan contributes to the pulmonary-valve stenosis that is the commonest cardiac defect.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Gap-junction connexin-43 couples cardiomyocytes for coordinated conduction, relevant to the conduction abnormalities and arrhythmia risk of the Noonan heart.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — RAS-MAPK overactivation drives cyclin-D1 (mapped) and E2F1-dependent cell-cycle entry, underpinning the juvenile myelomonocytic leukemia predisposition of Noonan syndrome.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The PTPN11/SHP2 phosphatase mutated in Noonan syndrome positively regulates both RAS-MAPK and JAK-STAT signaling, the latter contributing to the cytokine-driven myeloproliferation of its JMML predisposition.
- `connects-to` → **[Ryanodine receptor 2 (RyR2)](../../03-molecular/ryr2/README.md)** — RyR2-mediated sarcoplasmic calcium release (with SERCA2a already mapped) governs the excitation-contraction coupling of the cardiomyocyte, stressed in the hypertrophic cardiomyopathy of Noonan syndrome.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (cyclin-D1 and E2F1 already mapped) restrains the RAS-MAPK-driven proliferation underlying the leukemia predisposition of Noonan syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 drives the cardiac fibrosis underlying the hypertrophic cardiomyopathy of Noonan syndrome and is a biomarker of its progression.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) contributes to the cardiac and connective-tissue remodeling of Noonan syndrome.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — The CDK4/6-cyclin-D inhibitor CDKN2A (cyclin-D1 mapped) is a brake on the RAS-MAPK-driven myelomonocytic proliferation that predisposes Noonan syndrome to juvenile myelomonocytic leukemia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune surveillance relevant to the leukemia predisposition of Noonan syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the inflammatory tone associated with the RAS-MAPK dysregulation of Noonan syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, antagonized by the constitutive RAS-PI3K-AKT signaling of Noonan syndrome, modulate the growth and developmental programs it disrupts.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1 and RB1 already mapped) downstream of the RAS-MAPK hyperactivation contributes to the proliferative and developmental effects of Noonan syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the myeloid inflammatory activation relevant to the juvenile-myelomonocytic-leukemia predisposition of Noonan syndrome.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic signaling contributes to the cardiac hypertrophy and developmental features of Noonan syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of receptor tyrosine kinases, whose signals PTPN11/SHP2 amplifies (PTPN11 already mapped), participates in the RAS-MAPK hyperactivation of Noonan syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the developmental gene programs affected in Noonan syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the cardiomyocyte homeostasis relevant to the hypertrophic cardiomyopathy of Noonan syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the cardiac and growth-related metabolic phenotypes of Noonan syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid signaling participates in the myeloproliferative predisposition and immune features of Noonan syndrome.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-p53 signaling participates in the cellular-proliferation control relevant to the leukemia predisposition of Noonan syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the cardiac-developmental and vascular processes relevant to Noonan syndrome.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory and cardiac-remodeling processes relevant to Noonan syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the cardiac-remodeling and immune processes relevant to Noonan syndrome.
- `connects-to` → **[Phospholamban](../../03-molecular/phospholamban/README.md)** — Diastolic calcium handling: Noonan hypertrophic cardiomyopathy impairs relaxation via the phospholamban-SERCA2a axis (SERCA already mapped) controlling diastolic calcium reuptake into the sarcoplasmic reticulum, the basis of the stiff ventricle.
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — Skeletal fragility: Noonan syndrome carries reduced bone mineral density and osteopenia, and sclerostin is the osteocyte Wnt brake restraining bone formation, mechanistically linking the RASopathy to the low bone mass tracked alongside its osteoporosis risk.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Endocrine autoimmunity: Noonan syndrome is associated with an increased incidence of autoimmune thyroiditis and subclinical hypothyroidism, so thyroid-hormone deficiency is a recurrent endocrine comorbidity beyond the growth-hormone axis already mapped.
- `connects-to` → **[β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — Cardiomyopathy management: the hypertrophic cardiomyopathy of Noonan syndrome (troponin/BNP already mapped) is treated with beta-blockade at the beta1-adrenergic receptor to reduce outflow obstruction and protect the RAS-driven hypertrophied heart.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Cardiac remodelling: angiotensin II drives the fibrosis and hypertrophy of cardiac remodelling, a pathway overlaid on the RAS-MAPK (already mapped) overactivity that produces the hypertrophic cardiomyopathy of Noonan syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Autoimmune thyroiditis: MHC class II-restricted presentation of thyroid antigens underlies the autoimmune thyroiditis (thyroid hormones already mapped) that is more common in Noonan syndrome, part of its immune-endocrine comorbidity.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Myeloproliferation and bleeding: PTPN11-mutant Noonan syndrome carries a juvenile myelomonocytic leukaemia-like myeloproliferation and a bleeding diathesis (von Willebrand factor already mapped), both of which can lower haemoglobin.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Cardiac RAAS: aldosterone, with angiotensin II (already mapped), drives the fibrosis of the cardiac remodelling overlaid on the RAS-MAPK overactivity that produces the hypertrophic cardiomyopathy of Noonan syndrome.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Vascular and lymphatic tone: nitric oxide regulates the vascular and lymphatic tone disturbed in Noonan syndrome, contributing to the endothelial function relevant to its cardiovascular and lymphatic (already mapped) manifestations.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Bleeding diathesis: Noonan syndrome carries a bleeding tendency from clotting-factor deficiencies and platelet dysfunction (von Willebrand factor already mapped), and the coagulation abnormalities involving fibrinogen and factors require care around surgery.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — RAAS and cardiac remodelling: the renin-angiotensin-aldosterone system (angiotensin II and aldosterone already mapped), overlaid on the RAS-MAPK overactivity, contributes to the fibrosis and hypertrophic cardiomyopathy of Noonan syndrome.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Cardiac electrolyte balance: magnesium, with the calcium cycling (SERCA2a and RYR2 already mapped), influences the myocardial excitability and arrhythmia risk of the hypertrophic cardiomyopathy of Noonan syndrome.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Myocardial excitability: potassium, with the magnesium and calcium cycling (SERCA2a and RYR2 already mapped), sets the myocardial repolarisation and the arrhythmia risk of the hypertrophic cardiomyopathy of Noonan syndrome.
- `connects-to` → **[Cortical bone](../../05-tissue/cortical-bone/README.md)** — Skeletal features: the short stature (growth hormone and IGF-1 already mapped), the pectus deformity and the cubitus valgus of Noonan syndrome reflect the skeletal involvement (RANKL and sclerostin already mapped) of the RASopathy.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Neurodevelopment: the mild developmental delay and the learning difficulties (BDNF already mapped) of Noonan syndrome reflect the effect of the RAS-MAPK (already mapped) overactivity on the developing brain.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Growth-metabolic adipokine: leptin reflects the short stature (growth hormone and IGF-1 already mapped) and the altered growth and metabolism of Noonan syndrome.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 allergic tendency: IL-4 is part of the type-2 immune arm of the increased allergic/atopic and autoimmune tendency reported in the RASopathies including Noonan syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm of the atopic tendency of the RAS-MAPK (already mapped) overactivity of Noonan syndrome.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil atopic arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophil arm of the allergic/atopic tendency of the RASopathy Noonan syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic profile of Noonan syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the metabolic profile of Noonan syndrome.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immune arm: the IFN-γ of the T cells is the type-II interferon arm of the immune dysregulation and the JMML-spectrum myeloproliferation risk (PTPN11 already mapped) of Noonan syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm balancing the type-2 (IL-4, IL-5 and IL-13 already mapped) dimension of the immune profile of Noonan syndrome.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune dimension of Noonan syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 effector: IL-17A is the Th17 effector cytokine complementing the Th1/type-2 (IFN-γ, IL-4, IL-5 and IL-13 already mapped) balance of the immune profile of Noonan syndrome.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 arm) of the immune-inflammatory dimension of Noonan syndrome.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune profile of Noonan syndrome.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the immune-inflammatory dimension of Noonan syndrome.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast cells: the mast cells (via the KIT-adjacent RAS/MAPK signalling, ERK already mapped) contribute to the type-2 (IgE already mapped) immune dimension of Noonan syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement: the complement C3 activation is part of the innate immune dimension and the lymphatic-dysplasia-associated inflammation of Noonan syndrome.

[^tartaglia-2001-ptpn11-noonan]: Tartaglia M, Mehler EL, Goldberg R, et al. Mutations in PTPN11, encoding the protein tyrosine phosphatase SHP-2, cause Noonan syndrome. *Nat Genet.* 2001;29(4):465-468. [doi:10.1038/ng772](https://doi.org/10.1038/ng772) · [PubMed 11704759](https://pubmed.ncbi.nlm.nih.gov/11704759/)
[^van-der-burgt-2007-noonan-review]: van der Burgt I. Noonan syndrome. *Orphanet J Rare Dis.* 2007;2:4. [doi:10.1186/1750-1172-2-4](https://doi.org/10.1186/1750-1172-2-4) · [PubMed 17222357](https://pubmed.ncbi.nlm.nih.gov/17222357/)
