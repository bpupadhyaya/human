---
schema: human-scale-entry/v1
id: rothmund-thomson
name: Rothmund-Thomson Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Rothmund-Thomson syndrome is caused by biallelic RECQL4 mutations; poikiloderma (onset 3-6 months), skeletal abnormalities, juvenile cataracts; ~30% osteosarcoma risk (peak age 11-14 years); SCE not elevated; management centers on osteosarcoma surveillance."
aliases: ["Rothmund-Thomson syndrome", "Rothmund-Thomson", "RTS syndrome", "RECQL4 syndrome", "Rothmund Thomson poikiloderma", "Rothmund-Thomson osteosarcoma", "RTS osteosarcoma", "Rothmund-Thomson RECQL4", "poikiloderma with osteosarcoma"]
sources:
  - id: kitao-1999-recql4-rts
    type: peer-reviewed
    cite: "Kitao S, Shimamoto A, Goto M, et al. Mutations in RECQL4 cause a subset of cases of Rothmund-Thomson syndrome. Nat Genet. 1999;22(1):82-84."
    doi: "10.1038/8788"
    pmid: "10319867"
    url: "https://doi.org/10.1038/8788"
  - id: wang-2003-rts-cancer
    type: peer-reviewed
    cite: "Wang LL, Gannavarapu A, Kozinetz CA, et al. Association between osteosarcoma and deleterious mutations in the RECQL4 gene in Rothmund-Thomson syndrome. J Natl Cancer Inst. 2003;95(9):669-674."
    doi: "10.1093/jnci/95.9.669"
    pmid: "12734318"
    url: "https://doi.org/10.1093/jnci/95.9.669"
cross_links:
  - target: 01-human/03-molecular/recql4
    relation: connects-to
    note: "Biallelic RECQL4 LOF → Rothmund-Thomson syndrome; RECQL4 loss impairs replication initiation (CMG loading) and mitochondrial DNA repair; poikiloderma, skeletal defects (radial ray), juvenile cataracts, and ~30% lifetime osteosarcoma risk; SCE is not elevated."
  - target: 01-human/03-molecular/wrn
    relation: connects-to
    note: "RECQL4 and WRN are both RecQ helicases with distinct mechanisms: WRN has exonuclease activity and resolves G-quadruplex structures; RECQL4 initiates DNA replication via CMG complex; WRN LOF → Werner syndrome (progeroid, sarcomas); RECQL4 LOF → Rothmund-Thomson (osteosarcoma)."
  - target: 01-human/03-molecular/blm
    relation: connects-to
    note: "RECQL4 and BLM are both RecQ helicases: BLM dissolves Holliday junctions and suppresses crossover (SCE ~10x elevated in BLM LOF); RECQL4 initiates replication; both cause cancer predisposition — BLM LOF pan-cancer, RECQL4 LOF predominantly osteosarcoma."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "Rothmund-Thomson syndrome (RECQL4 LOF) and Werner syndrome (WRN LOF) are both RecQ helicase disorders: Rothmund-Thomson presents in infancy with poikiloderma and osteosarcoma risk; Werner syndrome presents in the 3rd decade with progeroid features, sarcomas, and atherosclerosis."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Rothmund-Thomson type II carries a ~30% lifetime osteosarcoma risk peaking at age 11-14; RECQL4 replication stress accelerates the same RB1 and TP53 loss that causes sporadic OS, so whole-body MRI surveillance runs through skeletal maturity."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Poikiloderma is the defining feature of Rothmund-Thomson, beginning at 3-6 months as cheek erythema then evolving into mottled pigmentation, telangiectasia, and atrophy; it is photo-exacerbated (sun protection) but, unlike xeroderma pigmentosum, does not cause skin cancer."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "RECQL4 loss inflicts replication stress on the rapidly dividing osteoblast precursors of the adolescent growth plate → double-strand breaks → biallelic RB1 and TP53 inactivation → osteosarcoma, the same transformation as sporadic OS but reached one to two decades early."
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "Rothmund-Thomson, Bloom, and Werner are the three classic RecQ-helicase disorders, each from loss of a different RecQ DNA helicase: RECQL4, BLM, and WRN; all cause genomic instability and cancer predisposition but differ in the dominant tumor and aging or growth phenotype."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Juvenile bilateral cataracts are a hallmark of Rothmund-Thomson syndrome: they appear in early childhood, decades before age-related cataracts, and their presence with poikiloderma helps establish the diagnosis and prompt RECQL4 testing."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Rothmund-Thomson is a skeletal dysplasia as much as a skin disorder: radial-ray defects (absent or hypoplastic thumbs and radii), short stature, and abnormal bone formation accompany its ~30% osteosarcoma risk, reflecting RECQL4's role in skeletal progenitor replication stress."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Rothmund-Thomson and Li-Fraumeni converge on osteosarcoma risk by different routes: RTS's biallelic RECQL4 helicase loss causes genome instability, while Li-Fraumeni's germline TP53 loss disables the genome's guardian—both among the highest osteosarcoma predispositions."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Rothmund-Thomson and hereditary retinoblastoma share a striking osteosarcoma susceptibility: RTS via RECQL4-driven genome instability, RB via germline RB1 loss—with Li-Fraumeni they form the trio of inherited syndromes behind most familial osteosarcoma."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "Rothmund-Thomson syndrome predisposes to skin cancers including basal and squamous cell carcinoma: poikiloderma plus defective RECQL4-dependent DNA repair leaves the skin vulnerable to UV damage, so sun protection and dermatologic surveillance are core to RTS care."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Rothmund-Thomson is studied in patient fibroblasts: cultured RTS fibroblasts show genomic instability from RECQL4 helicase loss—defective DNA replication and repair—a cellular model of how a broken DNA-maintenance enzyme causes premature aging and cancer predisposition."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A loss compounds Rothmund-Thomson's cancer risk: RTS's RECQL4 helicase defect already destabilizes the genome, and losing CDKN2A (p16, the CDK4/6 brake) on top removes cell-cycle control—a combination seen in the osteosarcomas and skin cancers RTS patients develop."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Rothmund-Thomson and Ewing sarcoma both connect DNA-repair biology to bone tumors: RTS's RECQL4 loss markedly raises osteosarcoma and other sarcoma risk, while Ewing arises in bone via EWSR1-FLI1—both remind that genomic instability and bone sarcomas often coincide."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Rothmund-Thomson cells are radiosensitive from defective DNA repair: RECQL4 helicase loss impairs repair of UV and ionizing damage, so sun causes the poikiloderma rash and radiotherapy must be used cautiously—mirroring other genome-instability syndromes."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "RTS shows how a DNA-repair defect becomes oncogenic: RECQL4 loss lets unrepaired damage accumulate and overwhelm p53-guarded checkpoints, so genomic instability drives the osteosarcoma and skin cancers that define the syndrome's cancer risk."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Some Rothmund-Thomson patients develop bone marrow failure: RECQL4 loss can impair hematopoiesis, causing cytopenias and a leukemia predisposition—placing RTS among the inherited genome-instability syndromes that threaten the marrow as well as bone."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin is the defining feature of Rothmund-Thomson: poikiloderma—mottled pigmentation, telangiectasia and atrophy—appears in infancy along with sparse hair, nail and tooth defects, so the integumentary system gives the syndrome its name and earliest sign."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Rothmund-Thomson affects the reproductive system: hypogonadism and reduced fertility accompany the syndrome, reflecting how a RECQL4 DNA-repair defect that disturbs growth and predisposes to cancer also impairs gonadal development."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "RTS spans both solid and blood cancer: besides its hallmark osteosarcoma, RECQL4-driven genome instability confers a risk of myelodysplasia and leukemia—so the syndrome predisposes across tumor types rather than to one, like other DNA-repair disorders."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Rothmund-Thomson is a genome-instability disorder sensed by ATM: defective RECQL4 helicase leaves DNA replication and repair error-prone, generating the double-strand breaks that ATM signals—the molecular root of its cancer-prone, prematurely aged phenotype."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Rothmund-Thomson disrupts skin and skeletal connective tissue: poikiloderma, sparse hair and bone defects (including absent or hypoplastic bones) reflect how RECQL4 loss impairs the cells that build collagen-rich skin and skeleton."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Rothmund-Thomson osteosarcomas often amplify MDM2: this p53 antagonist is amplified in the bone tumors that complicate RTS, switching off p53 to drive the sarcoma—mirroring the MDM2-amplified osteosarcomas seen across cancer-prone syndromes."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Rothmund-Thomson is a DNA-repair disease that leans on RAD51: the RECQL4 helicase helps repair and restart broken replication forks alongside RAD51-driven homologous recombination, so its loss leaves genomic instability that breeds osteosarcoma."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Rothmund-Thomson cells buckle under oxygen's damage: beyond DNA repair, RECQL4 supports mitochondria, so its loss raises reactive oxygen species and oxidative DNA damage—part of the premature aging and cancer risk of the syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Rothmund-Thomson's cancer risk meets immune surveillance by NK cells: as the unstable genome throws off mutated, stressed cells, natural killer cells help cull them before they form the tumors these patients are prone to."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Rothmund-Thomson disturbs the calcium-built skeleton: RECQL4 loss causes bone defects and a high osteosarcoma risk, so disordered bone—where calcium is laid down—is a defining feature beyond the poikiloderma skin changes."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells join NK cells in policing Rothmund-Thomson: as the helicase defect spawns mutated, stressed cells, T-cell surveillance helps cull them, and its strength may shape the timing of the cancers these patients face."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "The osteosarcomas of Rothmund-Thomson recruit blood via VEGF: the genomically chaotic bone tumors drive angiogenesis to grow and spread, so VEGF-targeted strategies are considered in this cancer-prone syndrome."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Rothmund-Thomson disturbs the bone's mineral: its skeletal dysplasias and high osteosarcoma risk involve the calcium-phosphate matrix, so the phosphorus-rich bone bears much of the syndrome's burden."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Rothmund-Thomson dilates the skin's vessels: poikiloderma's web of telangiectasias is endothelial cells forming widened surface capillaries, part of the mottled rash that defines the disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Rothmund-Thomson's chronic skin atrophies and scars: long-standing poikiloderma thins and fibroses the dermis alongside its pigment and vascular changes, the lasting cutaneous mark of the helicase defect."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "The broken RECQL4 helicase leaves cells unable to mend radiation damage: ionizing rays knock electrons loose to shatter DNA, and without the repair enzyme the breaks persist — so these patients tolerate radiotherapy poorly and accumulate the mutations that drive their cancers."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Rothmund-Thomson unsettles bone remodeling: radial-ray defects, low bone density, and a high osteosarcoma risk reflect a skeleton out of balance, where osteoclasts resorbing bone are no longer matched by healthy bone-building."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "The RECQL4 spectrum can starve the blood of iron's payload: related helicase disorders feature bone-marrow failure and anemia, so the same defect that scars skin and bone can leave the marrow unable to keep red cells filled."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Rothmund-Thomson children stay small: short stature is a core feature, driven by intrinsic growth failure and skeletal dysplasia, and a subset have true growth-hormone deficiency that can be treated to improve final height."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "The faulty helicase courts leukemia too: beyond its signature osteosarcoma, RECQL4 loss leaves DNA poorly repaired in blood-forming cells, raising the risk of myelodysplasia that can progress to acute myeloid leukemia."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The marrow trouble reaches the platelets: the bone-marrow dysfunction of the RECQL4 disorders can drop platelet counts into a thrombocytopenia, adding a bleeding tendency to the syndrome's skin, bone, and cancer problems."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Sun-sensitive, repair-poor skin courts skin cancer: beyond the basal and squamous tumors of its poikiloderma, RECQL4 deficiency raises melanoma risk, so lifelong sun protection and skin surveillance are core to RTS care."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The failing marrow also thins the red cells: the same RECQL4-driven dysfunction that courts MDS can crowd and stall erythrocyte production, leaving an anemia that, with the low platelets, marks the syndrome's bone-marrow involvement."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Sun avoidance collides with bone fragility: RTS demands strict photoprotection, yet the skeletal dysplasia and low bone density of the syndrome need vitamin D, so supplementation replaces the sunlight these children must shun."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "A faulty replication helicase can starve the marrow: RECQL4 loss impairs DNA replication in blood stem cells, so some children with RTS develop cytopenias and aplastic anemia alongside their later risk of myelodysplasia and leukemia."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "RTS belongs to the genome-instability family: its RECQL4 helicase, like the telomere-maintaining TERT, guards genome integrity, and its loss leaves cells with replication stress and the chromosomal chaos that fuels osteosarcoma."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Immune defenses can run low in RTS: some patients show immunodeficiency with poor antibody and T-cell responses, leaving them prone to recurrent infections — a reminder the RECQL4 defect reaches beyond skin, bone and cancer risk."
  - target: 01-human/07-system/hnscc
    relation: connects-to
    note: "Skin cancer is not the only squamous risk: the photodamaged, repair-deficient epithelium of RTS predisposes to squamous cell carcinomas of the skin and head-and-neck mucosa, a second-cancer threat alongside the syndrome's signature osteosarcoma."
  - target: 01-human/03-molecular/brca2
    relation: connects-to
    note: "RECQL4 works in the same repair shop: the helicase helps replication and homologous-recombination repair, the pathway anchored by BRCA2 and RAD51, so its loss leaves the cell unable to fix the breaks that BRCA-deficient cells also fail."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Sun strips away the skin's sentinels: in photosensitive RTS, ultraviolet exposure depletes the dendritic Langerhans cells that police the epidermis, weakening immune surveillance and helping the damaged keratinocytes escape into skin cancer."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RTS osteosarcoma runs through the RB pathway: the genomic instability of RECQL4 loss promotes RB1 inactivation, the same cell-cycle brake whose loss drives sporadic and Li-Fraumeni osteosarcomas."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Cancer therapy invites sepsis: the intensive chemotherapy for the osteosarcoma RTS predisposes to, on top of the syndrome's own immunodeficiency and marrow failure, leaves patients prone to neutropenic infection and sepsis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Tumor and major surgery raise the clot risk: the osteosarcoma resections and chemotherapy these patients undergo predispose to perioperative venous thromboembolism."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "The skeleton is built fragile: RTS's skeletal dysplasia, short stature and defective bone formation leave reduced bone density, so osteopenia and osteoporosis with fracture risk accompany the radial-ray and other bony defects."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Beyond marrow failure, chronic illness saps the count: alongside the aplastic-anemia tendency of the RECQL4 disorder, ongoing cancer and inflammation can add an anemia-of-chronic-disease component to the low blood counts."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its osteosarcoma chemo is nephrotoxic: high-dose methotrexate, cisplatin and ifosfamide used against the bone cancers RTS predisposes to injure the kidney, threatening lasting chronic kidney impairment in these patients."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Treating its bone cancers stresses the heart: the doxorubicin in osteosarcoma regimens, which RTS patients frequently need, is dose-dependently cardiotoxic and can leave a cardiomyopathy and heart failure in survivors."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Sarcoma chemotherapy opens the lung to mold: the deep neutropenia from treating the osteosarcomas RTS predisposes to lets inhaled Aspergillus invade as pulmonary aspergillosis in these vulnerable patients."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A disfiguring, cancer-prone condition weighs on mood: lifelong poikiloderma, sparse hair, short stature and the constant cancer-surveillance burden of Rothmund-Thomson contribute to depression and impaired quality of life."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Fragile poikilodermatous skin and cancer surgery heal poorly: the atrophic, telangiectatic skin of RTS plus resections for the osteosarcomas and skin cancers it predisposes to leave wounds slow to close."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The syndrome disturbs growth and gonads: Rothmund-Thomson often features short stature with growth-hormone deficiency and hypogonadism, so endocrine assessment is part of its care."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Lifelong cancer risk and disfigurement breed worry: the very high osteosarcoma and skin-cancer risk and constant surveillance of RTS foster chronic health anxiety alongside low mood."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It troubles the gut from infancy: Rothmund-Thomson commonly causes feeding difficulties and chronic diarrhoea in early childhood, and the chemotherapy for its osteosarcomas adds mucositis."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its sarcomas spread to the lungs: the osteosarcomas that Rothmund-Thomson strongly predisposes to metastasise to the lungs, making pulmonary metastases a key prognostic concern."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Sarcoma chemotherapy reawakens shingles: the chemotherapy for RTS-associated osteosarcoma deeply suppresses immunity, allowing latent or primary varicella-zoster to cause severe disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "A subset have weakened immunity: some Rothmund-Thomson patients show immune dysfunction with recurrent infections and impaired antibody responses, on top of the chemo-related immunosuppression."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its sarcoma chemotherapy taxes the kidney: the cisplatin and high-dose methotrexate used for RTS-associated osteosarcoma are nephrotoxic, needing protective hydration and rescue."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "That chemotherapy can scar the heart: the doxorubicin in osteosarcoma regimens for Rothmund-Thomson carries a dose-dependent cardiotoxicity risk."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Juvenile cataracts cloud its vision: Rothmund-Thomson syndrome characteristically causes early bilateral cataracts, part of its multisystem developmental defects."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Its osteosarcomas may need targeted drugs: the high osteosarcoma risk of Rothmund-Thomson syndrome is treated with chemotherapy and, in relapse, the multikinase inhibitors used for sporadic osteosarcoma."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Some patients are immunodeficient: a subset of Rothmund-Thomson syndrome has impaired immunity with low immunoglobulins and recurrent infections, reflecting its broad developmental defect."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "RECQL4 loss heightens genotoxic toxicity: without the RECQL4 helicase to repair DNA, Rothmund-Thomson cells are hypersensitive to DNA-damaging chemotherapy and radiotherapy, so genotoxic regimens must be dose-adjusted to avoid severe marrow and tissue toxicity."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Sun-driven skin cancers may respond: lifelong photodamage gives RTS patients cutaneous squamous and basal cell carcinomas whose high mutational burden can make advanced cutaneous SCC responsive to anti-PD-1 checkpoint blockade."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Osteosarcoma springs from its bones: RECQL4 maintains genome stability in osteoblasts, so its loss — with the radial-ray and metaphyseal skeletal malformations of RTS — predisposes the long-bone metaphyses to early osteosarcoma."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Its hallmark sarcoma seeds the lung: the osteosarcoma that defines Rothmund-Thomson metastasises to the lungs like sporadic osteosarcoma, studding the alveolar parenchyma, so chest surveillance and pulmonary metastasectomy matter."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Genomic instability widens the sarcoma risk: beyond its hallmark osteosarcoma, the chromosomal instability of Rothmund-Thomson can predispose to soft-tissue sarcomas including rhabdomyosarcoma, reflecting RECQL4's role in genome maintenance."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "Leukaemia rounds out its cancer spectrum: alongside the myelodysplasia and acute myeloid leukaemia already tied to it, Rothmund-Thomson's genome instability has been reported with lymphoid leukaemias, so blood counts are watched lifelong."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Recessive DNA-repair cancer syndromes: like MUTYH-associated polyposis, Rothmund-Thomson is autosomal-recessive—a defect in DNA repair (RECQL4 helicase versus base-excision repair) that drives cancer through accumulated mutations."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Where its osteosarcoma can spread: the osteosarcoma that Rothmund-Thomson predisposes to metastasises chiefly to the lung and, less often, the liver, seeding the hepatic lobule."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "A mitochondrial role too: RECQL4, the helicase lost in Rothmund-Thomson, also localises to mitochondria and supports their DNA, so its loss impairs mitochondrial function and ATP production beyond the nuclear genome."
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "Homologous recombination in common: RECQL4 works alongside the BRCA1-driven repair machinery, so like BRCA-deficient cells, Rothmund-Thomson cells handle DNA double-strand breaks poorly and show sensitivity to replication stress and PARP inhibition."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "Myeloid clonal evolution: the genomic instability of Rothmund-Thomson predisposes to myeloid neoplasia, with myelodysplasia and overlap disorders like CMML arising as the damaged marrow accumulates mutations."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Vulnerable to infection: Rothmund-Thomson can include immune dysfunction and bone-marrow failure, leaving affected patients more susceptible to severe infections including COVID-19."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle in osteosarcoma: the genomic instability of RECQL4 loss cooperates with CDK4/6-cyclin dysregulation to drive the osteosarcomas characteristic of Rothmund-Thomson."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth axis and bone tumours: GH/IGF-1 signalling, relevant to the short stature of Rothmund-Thomson, also feeds the osteosarcomas that are its signature malignancy."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified oncogene: MYC amplification drives the osteosarcomas that arise in Rothmund-Thomson, downstream of its defective DNA repair and genomic instability."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival signalling: PI3K/AKT activation supports the survival of the genomically unstable cells of Rothmund-Thomson, cooperating with its DNA-repair defect in tumorigenesis."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: the genomic instability of Rothmund-Thomson readily amplifies cyclin D1 and other cell-cycle drivers, fuelling the osteosarcomas and skin cancers it predisposes to."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the bone and skin tumours of Rothmund-Thomson drives the angiogenesis that supports their growth."
  - target: 01-human/03-molecular/cdkn1a
    relation: connects-to
    note: "Checkpoint engagement: the genomic instability of RECQL4-deficient Rothmund-Thomson cells triggers the p53-p21 (CDKN1A) checkpoint, arresting cells with unresolved replication damage and contributing to the syndrome's growth deficiency."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Bone predisposition: Rothmund-Thomson carries a high osteosarcoma risk and skeletal dysplasia, and RANKL-driven osteoclast activity shapes the abnormal bone remodelling that underlies both the dysplasia and the tumours."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptotic clearance: cells in Rothmund-Thomson that accumulate irreparable DNA damage from RECQL4 loss undergo caspase-3-mediated apoptosis, the cell-loss that contributes to the poikiloderma and tissue atrophy of the syndrome."
---

# Rothmund-Thomson Syndrome

## Overview

**Rothmund-Thomson syndrome (RTS)** is a rare autosomal recessive **chromosomal instability and cancer predisposition syndrome** caused by biallelic loss-of-function mutations in **RECQL4** (8q24.12), encoding a RecQ helicase required for DNA replication initiation and mitochondrial DNA integrity. RTS was first described by August Rothmund in 1868 (poikiloderma congenitale with juvenile cataracts) and by Matthew Thomson in 1936 (congenital poikiloderma). The RECQL4 gene was identified as the cause by Kitao et al. in 1999. RTS is classified into two types based on the presence of osteosarcoma risk: **RTS type II** (biallelic RECQL4 mutations; poikiloderma + osteosarcoma risk) is the classic form, while **RTS type I** (no RECQL4 mutations; poikiloderma without osteosarcoma) has incompletely characterized genetics [^kitao-1999-recql4-rts].

The cardinal features of RTS type II are: (1) **poikiloderma** — the defining skin eruption — beginning as erythema and edema of the cheeks at 3-6 months of age, progressing to mottled hypo/hyperpigmentation, telangiectasias, and skin atrophy over the face, extremities, and buttocks; (2) **skeletal abnormalities**, particularly radial ray defects (hypoplastic or absent radius/thumb) and short stature; (3) **juvenile cataracts** (bilateral, cortical/posterior subcapsular, onset in first decade); and (4) **~30% lifetime osteosarcoma risk**, the dominant life-threatening feature. Unlike Bloom syndrome (SCE elevated ~10x) and Werner syndrome (SCE elevated ~2-3x), **SCE is NOT elevated** in RTS — a key cytogenetic distinguishing feature. Worldwide prevalence is <1/500,000; approximately 300 patients have been documented in the literature [^wang-2003-rts-cancer].

**RTS vs. related RecQ helicase syndromes:**

| Feature | RTS (RECQL4) | Bloom Syndrome (BLM) | Werner Syndrome (WRN) |
|---|---|---|---|
| Onset | Infancy (3-6 months) | Birth | 3rd decade |
| SCE | Not elevated | ~10x elevated | ~2-3x elevated |
| Skin | Poikiloderma | Sun-sensitive telangiectasia | Scleroderma-like, ulcers |
| Cancer risk | Osteosarcoma (~30%) | Pan-cancer | Sarcomas, melanoma, thyroid |
| Skeletal | Radial ray defects, short stature | Short stature (uniform) | Osteoporosis (adult) |
| Cataracts | Juvenile (1st decade) | Not typical | Adult (3rd decade, diagnostic) |
| Immunodeficiency | No | Yes (IgA/IgM low) | Mild |

## Structure

### Genetic basis of Rothmund-Thomson syndrome

**RECQL4 gene (8q24.12):**
- 21 exons; 1,208 aa; 133 kDa; ubiquitously expressed in proliferating tissues
- All RTS-causing mutations are biallelic LOF: nonsense, frameshift, missense in the helicase core (abolish ATPase/helicase activity), and splice site mutations
- No clear hot spot; mutations distributed throughout the helicase domain; compound heterozygotes predominate in non-consanguineous families
- Genotype-phenotype correlation is imperfect: mutations in the helicase core are most consistently associated with osteosarcoma risk; mutations closer to N-terminus or C-terminus may have less severe helicase LOF

**RECQL4 mutation spectrum and associated syndromes:**
- RTS type II: helicase core missense, truncating mutations → classic syndrome with poikiloderma + osteosarcoma
- RAPADILINO syndrome: splice site c.1390+2T>C (Finnish founder) → exon 7 skipping → partial LOF → radial/patellar anomalies without poikiloderma; lower osteosarcoma risk (~8%)
- Baller-Gerold syndrome: some cases with RECQL4 biallelic mutations → craniosynostosis + radial aplasia; poikiloderma may or may not be present
- These three syndromes form an allelic spectrum; phenotypic overlap is substantial

**Cellular pathology of RECQL4 LOF:**
- Replication defect: RECQL4-deficient cells show reduced origin firing → compensatory activation of dormant origins → prolonged S-phase → sensitivity to replication stress (hydroxyurea, aphidicolin)
- Chromosomal instability: elevated chromosomal rearrangements (deletions, translocations) without elevated SCE (distinguishes from BLM/WRN)
- Mitochondrial dysfunction: reduced mtDNA copy number; elevated mitochondrial ROS → accelerated mitochondrial aging; contributes to premature aging features in older RTS patients
- SCE: NOT elevated (distinguishing from BLM where SCE ~10x; from WRN where SCE ~2-3x); normal SCE rules out Bloom syndrome and substantially against Werner syndrome as the diagnosis in an RTS-like presentation

## Function

### Clinical features of Rothmund-Thomson syndrome

**Poikiloderma — the defining feature:**
- Onset at 3-6 months of age as erythema and bullae/edema on the cheeks; often initially mistaken for contact dermatitis or systemic lupus
- Over 1-2 years: progresses to classic **poikiloderma**: triad of skin atrophy, mottled hypo- and hyperpigmentation (giving a "marbled" or "mottled" appearance), and telangiectasias
- Distribution: face (cheeks, nose, forehead, chin); spreads to arms, hands, legs; trunk and torso less commonly affected; palms/soles often spared
- Photo-exacerbated: UVA and UVB exposure worsens erythema and telangiectasias; photoprotection from infancy
- NOT associated with photodamage (no actinic keratosis, no basal/squamous cell carcinoma from UV); distinguish from xeroderma pigmentosum and Cockayne syndrome
- Poikiloderma is stable or slowly progressive after childhood; not life-threatening but can be cosmetically significant

**Skeletal abnormalities:**
- **Radial ray defects**: hypoplasia or aplasia of the radius; hypoplastic or absent thumb; may be unilateral or bilateral; often the presenting birth defect; range from mild radial hypoplasia to complete absence with distal limb involvement
- **Short stature**: below 3rd percentile in most RTS patients; intrauterine growth restriction in some; NOT growth hormone-deficient; GH treatment rarely effective
- **Osteoporosis/osteopenia**: premature bone loss in adolescence and adulthood; vertebral compression fractures in some; replication defect in osteoblast precursors → reduced bone accretion
- Patellar hypoplasia/aplasia: seen in RAPADILINO overlap; may occur in RTS
- Dental anomalies: microdontia, malformed crowns, delayed eruption

**Juvenile bilateral cataracts:**
- Onset in first decade (earlier than Werner syndrome which presents in 3rd decade; earlier than normal aging cataracts)
- Cortical or posterior subcapsular pattern; bilateral; can cause significant visual impairment by adolescence
- Management: phacoemulsification + IOL implantation; excellent visual outcomes
- Present in ~50% of classic RTS type II patients; absence does not exclude diagnosis

**Other features:**
- Hair and adnexal: sparse scalp hair, eyebrows, and eyelashes; may be patchy; alopecia in some
- Nail dystrophy: brittle, hypoplastic nails
- Normal intelligence: cognitive development typically unaffected
- Hypogonadism: reduced fertility in females; males typically fertile (contrast with Bloom syndrome where male azoospermia is near-universal)
- No immunodeficiency: serum immunoglobulins normal; T-cell function intact (contrast with Bloom syndrome)

### Osteosarcoma in Rothmund-Thomson syndrome

**Epidemiology:**
- **~30% lifetime osteosarcoma risk** in RTS type II (RECQL4 biallelic LOF) — among the highest for any single-gene cancer predisposition syndrome for osteosarcoma
- Wang et al. (2003) systematic analysis: 41% of RTS patients with helicase-domain RECQL4 mutations developed osteosarcoma vs. 0% with non-helicase-domain mutations [^wang-2003-rts-cancer]
- Peak age of diagnosis: **11-14 years** (during the adolescent growth spurt — parallel to sporadic osteosarcoma peak)
- Sites: distal femur, proximal tibia, proximal humerus — same distribution as sporadic osteosarcoma
- Often **multifocal** at presentation; metastatic disease at diagnosis (~20-25%)

**Pathogenesis:**
- RECQL4 LOF → replication stress in rapidly proliferating osteoblast precursors → DSBs → LOH at RB1 and TP53 → biallelic inactivation → osteoblast transformation
- Same molecular events (RB1 LOH, TP53 mutation) as sporadic osteosarcoma — RECQL4 LOF accelerates their occurrence by 10-20 years
- Osteosarcoma histology: high-grade osteoblastic, chondroblastic, or fibroblastic; indistinguishable from sporadic on pathology; requires RECQL4 germline testing for RTS diagnosis

**Treatment:**
- Standard MAP chemotherapy regimen (methotrexate, doxorubicin, cisplatin) + surgical resection with limb salvage where possible
- Chemotherapy in RTS: RECQL4 LOF may alter drug sensitivity (unvalidated in clinical trials); consult sarcoma oncology center with RTS expertise
- Radiation: avoid if possible (underlying chromosomal instability may increase radiation sensitivity)
- Prognosis: 5-year OS ~60-70% (comparable to sporadic osteosarcoma); multifocal disease carries worse prognosis
- Recurrence after primary resection: same surveillance as sporadic osteosarcoma (CT chest every 3 months for 2 years)

## Pathology

### Diagnosis

**Diagnostic approach:**
1. **Clinical**: poikiloderma with classic onset (3-6 months), radial ray defects, juvenile cataracts, short stature, family history → suspect RTS
2. **Cytogenetics**: SCE assay — NOT elevated (normal SCE rules out Bloom syndrome; ~2-3x elevated would suggest Werner syndrome)
3. **Molecular confirmation**: RECQL4 sequencing + MLPA; compound heterozygous LOF mutations in helicase domain = RTS type II; confirm with parental testing
4. **Skin biopsy**: characteristic poikilodermatous changes (dermal fibrosis, epidermal atrophy, dermal hemosiderin, dilated superficial vessels); supports but does not confirm diagnosis

**Diagnostic criteria (Vennos & James 1995, modified):**
- **Required**: poikiloderma (onset in infancy/early childhood)
- **Supporting**: RECQL4 biallelic mutations; osteosarcoma; radial ray defect; juvenile cataracts; short stature; sparse hair; normal SCE

**Differential diagnosis:**
- Bloom syndrome: SCE ~10x elevated, NO poikiloderma (telangiectatic erythema different pattern), no skeletal malformations
- Werner syndrome: adult onset, scleroderma-like (not classic poikiloderma), cataracts in 3rd decade
- Kindler syndrome (FERMT1): acral blistering in infancy → poikiloderma; photosensitivity; no osteosarcoma
- Dyskeratosis congenita (DKC1/TERT/TERC): reticulate skin pigmentation (not classic poikiloderma), nail dystrophy, oral leukoplakia, bone marrow failure; telomere shortening
- Fanconi anemia: café-au-lait spots, bone marrow failure, FA gene panel; radial ray defects overlap
- IBIDS/PIBI(D)S (trichothiodystrophy, ERCC2/3): tiger-tail hair (sulfur-poor), ichthyosis, brittle hair; poikiloderma not typical
- Poikiloderma of Kindler vs. RTS: FERMT1 sequencing; onset pattern; blistering
- Ataxia-telangiectasia: cerebellar ataxia, IgA deficiency, telangiectasias of conjunctivae (not skin poikiloderma); ATM mutations

**Cancer surveillance protocol:**
- **Osteosarcoma**: clinical assessment at every visit (bone pain, joint swelling, limp) — from diagnosis; annual whole-body MRI from time of RTS diagnosis (~6 months) until skeletal maturity (~18-20 years); then symptom-directed evaluation
- **Skin**: annual dermatological exam; photoprotection advice and SPF 50+ sunscreen
- **Ophthalmology**: annual eye exam from diagnosis; cataract management
- Avoid excessive radiation exposure: minimize diagnostic CT; use MRI for osteosarcoma surveillance
- No proven benefit of routine cross-sectional imaging for non-osteosarcoma cancers in RTS (other cancer risks are lower than osteosarcoma)

**Management:**
- Photoprotection: strict UVA/UVB protection (SPF 50+ sunscreen, UPF clothing, sun avoidance) from infancy; reduces poikiloderma progression and sun-induced erythema
- Orthopedics: radial ray malformations → occupational therapy, adaptive devices; surgical correction in severe radial aplasia (centralization procedures); fracture management for osteoporosis
- Ophthalmology: phacoemulsification for cataracts; prompt referral at first sign of visual impairment
- Dental: dental anomaly monitoring; early orthodontic evaluation
- Genetic counseling: AR inheritance; sibling recurrence 1/4; prenatal diagnosis by CVS/amniocentesis; cascade testing for siblings; no current role for RECQL4 carrier screening in general population
- Research registries: International Rothmund-Thomson Syndrome Registry (biolgen.com); multi-institutional collaboration for rare syndrome research

## Connections

- `connects-to` → **[RECQL4](../../03-molecular/recql4/README.md)** — Biallelic RECQL4 LOF → Rothmund-Thomson syndrome; RECQL4 loss impairs replication initiation (CMG loading) and mitochondrial DNA repair; poikiloderma, skeletal defects (radial ray), juvenile cataracts, and ~30% lifetime osteosarcoma risk; SCE is not elevated.
- `connects-to` → **[WRN](../../03-molecular/wrn/README.md)** — RECQL4 and WRN are both RecQ helicases with distinct mechanisms: WRN has exonuclease activity and resolves G-quadruplex structures; RECQL4 initiates DNA replication via CMG complex; WRN LOF → Werner syndrome (progeroid, sarcomas); RECQL4 LOF → Rothmund-Thomson (osteosarcoma).
- `connects-to` → **[BLM](../../03-molecular/blm/README.md)** — RECQL4 and BLM are both RecQ helicases: BLM dissolves Holliday junctions and suppresses crossover (SCE ~10x elevated in BLM LOF); RECQL4 initiates replication; both cause cancer predisposition — BLM LOF pan-cancer, RECQL4 LOF predominantly osteosarcoma.
- `connects-to` → **[Werner Syndrome](../../07-system/werner-syndrome/README.md)** — Rothmund-Thomson syndrome (RECQL4 LOF) and Werner syndrome (WRN LOF) are both RecQ helicase disorders: Rothmund-Thomson presents in infancy with poikiloderma and osteosarcoma risk; Werner syndrome presents in the 3rd decade with progeroid features, sarcomas, and atherosclerosis.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Rothmund-Thomson type II carries a ~30% lifetime osteosarcoma risk peaking at age 11-14; RECQL4 replication stress accelerates the same RB1 and TP53 loss that causes sporadic OS, so whole-body MRI surveillance runs through skeletal maturity.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Poikiloderma is the defining feature of Rothmund-Thomson, beginning at 3-6 months as cheek erythema then evolving into mottled pigmentation, telangiectasia, and atrophy; it is photo-exacerbated (sun protection) but, unlike xeroderma pigmentosum, does not cause skin cancer.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — RECQL4 loss inflicts replication stress on the rapidly dividing osteoblast precursors of the adolescent growth plate → double-strand breaks → biallelic RB1 and TP53 inactivation → osteosarcoma, the same transformation as sporadic OS but reached one to two decades early.
- `connects-to` → **[Bloom Syndrome](../bloom-syndrome/README.md)** — Rothmund-Thomson, Bloom, and Werner are the three classic RecQ-helicase disorders, each from loss of a different RecQ DNA helicase: RECQL4, BLM, and WRN; all cause genomic instability and cancer predisposition but differ in the dominant tumor and aging or growth phenotype.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Juvenile bilateral cataracts are a hallmark of Rothmund-Thomson syndrome: they appear in early childhood, decades before age-related cataracts, and their presence with poikiloderma helps establish the diagnosis and prompt RECQL4 testing.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Rothmund-Thomson is a skeletal dysplasia as much as a skin disorder: radial-ray defects (absent or hypoplastic thumbs and radii), short stature, and abnormal bone formation accompany its ~30% osteosarcoma risk, reflecting RECQL4's role in skeletal progenitor replication stress.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Rothmund-Thomson and Li-Fraumeni converge on osteosarcoma risk by different routes: RTS's biallelic RECQL4 helicase loss causes genome instability, while Li-Fraumeni's germline TP53 loss disables the genome's guardian—both among the highest osteosarcoma predispositions.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Rothmund-Thomson and hereditary retinoblastoma share a striking osteosarcoma susceptibility: RTS via RECQL4-driven genome instability, RB via germline RB1 loss—with Li-Fraumeni they form the trio of inherited syndromes behind most familial osteosarcoma.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — Rothmund-Thomson syndrome predisposes to skin cancers including basal and squamous cell carcinoma: poikiloderma plus defective RECQL4-dependent DNA repair leaves the skin vulnerable to UV damage, so sun protection and dermatologic surveillance are core to RTS care.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Rothmund-Thomson is studied in patient fibroblasts: cultured RTS fibroblasts show genomic instability from RECQL4 helicase loss—defective DNA replication and repair—a cellular model of how a broken DNA-maintenance enzyme causes premature aging and cancer predisposition.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss compounds Rothmund-Thomson's cancer risk: RTS's RECQL4 helicase defect already destabilizes the genome, and losing CDKN2A (p16, the CDK4/6 brake) on top removes cell-cycle control—a combination seen in the osteosarcomas and skin cancers RTS patients develop.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Rothmund-Thomson and Ewing sarcoma both connect DNA-repair biology to bone tumors: RTS's RECQL4 loss markedly raises osteosarcoma and other sarcoma risk, while Ewing arises in bone via EWSR1-FLI1—both remind that genomic instability and bone sarcomas often coincide.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Rothmund-Thomson cells are radiosensitive from defective DNA repair: RECQL4 helicase loss impairs repair of UV and ionizing damage, so sun causes the poikiloderma rash and radiotherapy must be used cautiously—mirroring other genome-instability syndromes.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — RTS shows how a DNA-repair defect becomes oncogenic: RECQL4 loss lets unrepaired damage accumulate and overwhelm p53-guarded checkpoints, so genomic instability drives the osteosarcoma and skin cancers that define the syndrome's cancer risk.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Some Rothmund-Thomson patients develop bone marrow failure: RECQL4 loss can impair hematopoiesis, causing cytopenias and a leukemia predisposition—placing RTS among the inherited genome-instability syndromes that threaten the marrow as well as bone.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin is the defining feature of Rothmund-Thomson: poikiloderma—mottled pigmentation, telangiectasia and atrophy—appears in infancy along with sparse hair, nail and tooth defects, so the integumentary system gives the syndrome its name and earliest sign.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Rothmund-Thomson affects the reproductive system: hypogonadism and reduced fertility accompany the syndrome, reflecting how a RECQL4 DNA-repair defect that disturbs growth and predisposes to cancer also impairs gonadal development.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — RTS spans both solid and blood cancer: besides its hallmark osteosarcoma, RECQL4-driven genome instability confers a risk of myelodysplasia and leukemia—so the syndrome predisposes across tumor types rather than to one, like other DNA-repair disorders.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — Rothmund-Thomson is a genome-instability disorder sensed by ATM: defective RECQL4 helicase leaves DNA replication and repair error-prone, generating the double-strand breaks that ATM signals—the molecular root of its cancer-prone, prematurely aged phenotype.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Rothmund-Thomson disrupts skin and skeletal connective tissue: poikiloderma, sparse hair and bone defects (including absent or hypoplastic bones) reflect how RECQL4 loss impairs the cells that build collagen-rich skin and skeleton.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — Rothmund-Thomson osteosarcomas often amplify MDM2: this p53 antagonist is amplified in the bone tumors that complicate RTS, switching off p53 to drive the sarcoma—mirroring the MDM2-amplified osteosarcomas seen across cancer-prone syndromes.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — Rothmund-Thomson is a DNA-repair disease that leans on RAD51: the RECQL4 helicase helps repair and restart broken replication forks alongside RAD51-driven homologous recombination, so its loss leaves genomic instability that breeds osteosarcoma.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Rothmund-Thomson cells buckle under oxygen's damage: beyond DNA repair, RECQL4 supports mitochondria, so its loss raises reactive oxygen species and oxidative DNA damage—part of the premature aging and cancer risk of the syndrome.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Rothmund-Thomson's cancer risk meets immune surveillance by NK cells: as the unstable genome throws off mutated, stressed cells, natural killer cells help cull them before they form the tumors these patients are prone to.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Rothmund-Thomson disturbs the calcium-built skeleton: RECQL4 loss causes bone defects and a high osteosarcoma risk, so disordered bone—where calcium is laid down—is a defining feature beyond the poikiloderma skin changes.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells join NK cells in policing Rothmund-Thomson: as the helicase defect spawns mutated, stressed cells, T-cell surveillance helps cull them, and its strength may shape the timing of the cancers these patients face.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — The osteosarcomas of Rothmund-Thomson recruit blood via VEGF: the genomically chaotic bone tumors drive angiogenesis to grow and spread, so VEGF-targeted strategies are considered in this cancer-prone syndrome.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Rothmund-Thomson disturbs the bone's mineral: its skeletal dysplasias and high osteosarcoma risk involve the calcium-phosphate matrix, so the phosphorus-rich bone bears much of the syndrome's burden.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Rothmund-Thomson dilates the skin's vessels: poikiloderma's web of telangiectasias is endothelial cells forming widened surface capillaries, part of the mottled rash that defines the disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Rothmund-Thomson's chronic skin atrophies and scars: long-standing poikiloderma thins and fibroses the dermis alongside its pigment and vascular changes, the lasting cutaneous mark of the helicase defect.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — The broken RECQL4 helicase leaves cells unable to mend radiation damage: ionizing rays knock electrons loose to shatter DNA, and without the repair enzyme the breaks persist — so these patients tolerate radiotherapy poorly and accumulate the mutations that drive their cancers.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Rothmund-Thomson unsettles bone remodeling: radial-ray defects, low bone density, and a high osteosarcoma risk reflect a skeleton out of balance, where osteoclasts resorbing bone are no longer matched by healthy bone-building.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — The RECQL4 spectrum can starve the blood of iron's payload: related helicase disorders feature bone-marrow failure and anemia, so the same defect that scars skin and bone can leave the marrow unable to keep red cells filled.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Rothmund-Thomson children stay small: short stature is a core feature, driven by intrinsic growth failure and skeletal dysplasia, and a subset have true growth-hormone deficiency that can be treated to improve final height.
- `connects-to` → **[AML](../aml/README.md)** — The faulty helicase courts leukemia too: beyond its signature osteosarcoma, RECQL4 loss leaves DNA poorly repaired in blood-forming cells, raising the risk of myelodysplasia that can progress to acute myeloid leukemia.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The marrow trouble reaches the platelets: the bone-marrow dysfunction of the RECQL4 disorders can drop platelet counts into a thrombocytopenia, adding a bleeding tendency to the syndrome's skin, bone, and cancer problems.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Sun-sensitive, repair-poor skin courts skin cancer: beyond the basal and squamous tumors of its poikiloderma, RECQL4 deficiency raises melanoma risk, so lifelong sun protection and skin surveillance are core to RTS care.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The failing marrow also thins the red cells: the same RECQL4-driven dysfunction that courts MDS can crowd and stall erythrocyte production, leaving an anemia that, with the low platelets, marks the syndrome's bone-marrow involvement.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Sun avoidance collides with bone fragility: RTS demands strict photoprotection, yet the skeletal dysplasia and low bone density of the syndrome need vitamin D, so supplementation replaces the sunlight these children must shun.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — A faulty replication helicase can starve the marrow: RECQL4 loss impairs DNA replication in blood stem cells, so some children with RTS develop cytopenias and aplastic anemia alongside their later risk of myelodysplasia and leukemia.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — RTS belongs to the genome-instability family: its RECQL4 helicase, like the telomere-maintaining TERT, guards genome integrity, and its loss leaves cells with replication stress and the chromosomal chaos that fuels osteosarcoma.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Immune defenses can run low in RTS: some patients show immunodeficiency with poor antibody and T-cell responses, leaving them prone to recurrent infections — a reminder the RECQL4 defect reaches beyond skin, bone and cancer risk.
- `connects-to` → **[HNSCC](../hnscc/README.md)** — Skin cancer is not the only squamous risk: the photodamaged, repair-deficient epithelium of RTS predisposes to squamous cell carcinomas of the skin and head-and-neck mucosa, a second-cancer threat alongside the syndrome's signature osteosarcoma.
- `connects-to` → **[BRCA2](../../03-molecular/brca2/README.md)** — RECQL4 works in the same repair shop: the helicase helps replication and homologous-recombination repair, the pathway anchored by BRCA2 and RAD51, so its loss leaves the cell unable to fix the breaks that BRCA-deficient cells also fail.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Sun strips away the skin's sentinels: in photosensitive RTS, ultraviolet exposure depletes the dendritic Langerhans cells that police the epidermis, weakening immune surveillance and helping the damaged keratinocytes escape into skin cancer.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RTS osteosarcoma runs through the RB pathway: the genomic instability of RECQL4 loss promotes RB1 inactivation, the same cell-cycle brake whose loss drives sporadic and Li-Fraumeni osteosarcomas.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Cancer therapy invites sepsis: the intensive chemotherapy for the osteosarcoma RTS predisposes to, on top of the syndrome's own immunodeficiency and marrow failure, leaves patients prone to neutropenic infection and sepsis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Tumor and major surgery raise the clot risk: the osteosarcoma resections and chemotherapy these patients undergo predispose to perioperative venous thromboembolism.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — The skeleton is built fragile: RTS's skeletal dysplasia, short stature and defective bone formation leave reduced bone density, so osteopenia and osteoporosis with fracture risk accompany the radial-ray and other bony defects.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Beyond marrow failure, chronic illness saps the count: alongside the aplastic-anemia tendency of the RECQL4 disorder, ongoing cancer and inflammation can add an anemia-of-chronic-disease component to the low blood counts.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its osteosarcoma chemo is nephrotoxic: high-dose methotrexate, cisplatin and ifosfamide used against the bone cancers RTS predisposes to injure the kidney, threatening lasting chronic kidney impairment in these patients.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Treating its bone cancers stresses the heart: the doxorubicin in osteosarcoma regimens, which RTS patients frequently need, is dose-dependently cardiotoxic and can leave a cardiomyopathy and heart failure in survivors.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Sarcoma chemotherapy opens the lung to mold: the deep neutropenia from treating the osteosarcomas RTS predisposes to lets inhaled Aspergillus invade as pulmonary aspergillosis in these vulnerable patients.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A disfiguring, cancer-prone condition weighs on mood: lifelong poikiloderma, sparse hair, short stature and the constant cancer-surveillance burden of Rothmund-Thomson contribute to depression and impaired quality of life.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Fragile poikilodermatous skin and cancer surgery heal poorly: the atrophic, telangiectatic skin of RTS plus resections for the osteosarcomas and skin cancers it predisposes to leave wounds slow to close.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — The syndrome disturbs growth and gonads: Rothmund-Thomson often features short stature with growth-hormone deficiency and hypogonadism, so endocrine assessment is part of its care.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Lifelong cancer risk and disfigurement breed worry: the very high osteosarcoma and skin-cancer risk and constant surveillance of RTS foster chronic health anxiety alongside low mood.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It troubles the gut from infancy: Rothmund-Thomson commonly causes feeding difficulties and chronic diarrhoea in early childhood, and the chemotherapy for its osteosarcomas adds mucositis.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its sarcomas spread to the lungs: the osteosarcomas that Rothmund-Thomson strongly predisposes to metastasise to the lungs, making pulmonary metastases a key prognostic concern.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Sarcoma chemotherapy reawakens shingles: the chemotherapy for RTS-associated osteosarcoma deeply suppresses immunity, allowing latent or primary varicella-zoster to cause severe disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — A subset have weakened immunity: some Rothmund-Thomson patients show immune dysfunction with recurrent infections and impaired antibody responses, on top of the chemo-related immunosuppression.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its sarcoma chemotherapy taxes the kidney: the cisplatin and high-dose methotrexate used for RTS-associated osteosarcoma are nephrotoxic, needing protective hydration and rescue.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — That chemotherapy can scar the heart: the doxorubicin in osteosarcoma regimens for Rothmund-Thomson carries a dose-dependent cardiotoxicity risk.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Juvenile cataracts cloud its vision: Rothmund-Thomson syndrome characteristically causes early bilateral cataracts, part of its multisystem developmental defects.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Its osteosarcomas may need targeted drugs: the high osteosarcoma risk of Rothmund-Thomson syndrome is treated with chemotherapy and, in relapse, the multikinase inhibitors used for sporadic osteosarcoma.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Some patients are immunodeficient: a subset of Rothmund-Thomson syndrome has impaired immunity with low immunoglobulins and recurrent infections, reflecting its broad developmental defect.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — RECQL4 loss heightens genotoxic toxicity: without the RECQL4 helicase to repair DNA, Rothmund-Thomson cells are hypersensitive to DNA-damaging chemotherapy and radiotherapy, so genotoxic regimens must be dose-adjusted to avoid severe marrow and tissue toxicity.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Sun-driven skin cancers may respond: lifelong photodamage gives RTS patients cutaneous squamous and basal cell carcinomas whose high mutational burden can make advanced cutaneous SCC responsive to anti-PD-1 checkpoint blockade.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Osteosarcoma springs from its bones: RECQL4 maintains genome stability in osteoblasts, so its loss — with the radial-ray and metaphyseal skeletal malformations of RTS — predisposes the long-bone metaphyses to early osteosarcoma.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Its hallmark sarcoma seeds the lung: the osteosarcoma that defines Rothmund-Thomson metastasises to the lungs like sporadic osteosarcoma, studding the alveolar parenchyma, so chest surveillance and pulmonary metastasectomy matter.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Genomic instability widens the sarcoma risk: beyond its hallmark osteosarcoma, the chromosomal instability of Rothmund-Thomson can predispose to soft-tissue sarcomas including rhabdomyosarcoma, reflecting RECQL4's role in genome maintenance.
- `connects-to` → **[ALL](../all/README.md)** — Leukaemia rounds out its cancer spectrum: alongside the myelodysplasia and acute myeloid leukaemia already tied to it, Rothmund-Thomson's genome instability has been reported with lymphoid leukaemias, so blood counts are watched lifelong.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — Recessive DNA-repair cancer syndromes: like MUTYH-associated polyposis, Rothmund-Thomson is autosomal-recessive—a defect in DNA repair (RECQL4 helicase versus base-excision repair) that drives cancer through accumulated mutations.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Where its osteosarcoma can spread: the osteosarcoma that Rothmund-Thomson predisposes to metastasises chiefly to the lung and, less often, the liver, seeding the hepatic lobule.
- `connects-to` → **[ATP](../../03-molecular/atp/README.md)** — A mitochondrial role too: RECQL4, the helicase lost in Rothmund-Thomson, also localises to mitochondria and supports their DNA, so its loss impairs mitochondrial function and ATP production beyond the nuclear genome.
- `connects-to` → **[BRCA1](../../03-molecular/brca1/README.md)** — Homologous recombination in common: RECQL4 works alongside the BRCA1-driven repair machinery, so like BRCA-deficient cells, Rothmund-Thomson cells handle DNA double-strand breaks poorly and show sensitivity to replication stress and PARP inhibition.
- `connects-to` → **[CMML](../cmml/README.md)** — Myeloid clonal evolution: the genomic instability of Rothmund-Thomson predisposes to myeloid neoplasia, with myelodysplasia and overlap disorders like CMML arising as the damaged marrow accumulates mutations.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Vulnerable to infection: Rothmund-Thomson can include immune dysfunction and bone-marrow failure, leaving affected patients more susceptible to severe infections including COVID-19.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle in osteosarcoma: the genomic instability of RECQL4 loss cooperates with CDK4/6-cyclin dysregulation to drive the osteosarcomas characteristic of Rothmund-Thomson.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth axis and bone tumours: GH/IGF-1 signalling, relevant to the short stature of Rothmund-Thomson, also feeds the osteosarcomas that are its signature malignancy.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified oncogene: MYC amplification drives the osteosarcomas that arise in Rothmund-Thomson, downstream of its defective DNA repair and genomic instability.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Survival signalling: PI3K/AKT activation supports the survival of the genomically unstable cells of Rothmund-Thomson, cooperating with its DNA-repair defect in tumorigenesis.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: the genomic instability of Rothmund-Thomson readily amplifies cyclin D1 and other cell-cycle drivers, fuelling the osteosarcomas and skin cancers it predisposes to.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the bone and skin tumours of Rothmund-Thomson drives the angiogenesis that supports their growth.
- `connects-to` → **[p21 (CDKN1A)](../../03-molecular/cdkn1a/README.md)** — The genomic instability of RECQL4-deficient Rothmund-Thomson cells triggers the p53-p21 checkpoint, arresting cells with unresolved replication damage—a brake that protects against cancer but also contributes to the syndrome's growth deficiency.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Rothmund-Thomson carries a high osteosarcoma risk and skeletal dysplasia, and RANKL-driven osteoclast activity shapes the abnormal bone remodeling that underlies both the radial-ray and skeletal defects and the bone tumors.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Cells in Rothmund-Thomson that accumulate irreparable DNA damage from RECQL4 loss undergo caspase-3-mediated apoptosis—the cell loss that contributes to the poikiloderma and tissue atrophy characteristic of the syndrome.

[^kitao-1999-recql4-rts]: Kitao S, Shimamoto A, Goto M, et al. Mutations in RECQL4 cause a subset of cases of Rothmund-Thomson syndrome. *Nat Genet.* 1999;22(1):82-84. [doi:10.1038/8788](https://doi.org/10.1038/8788) · [PubMed 10319867](https://pubmed.ncbi.nlm.nih.gov/10319867/)
[^wang-2003-rts-cancer]: Wang LL, Gannavarapu A, Kozinetz CA, et al. Association between osteosarcoma and deleterious mutations in the RECQL4 gene in Rothmund-Thomson syndrome. *J Natl Cancer Inst.* 2003;95(9):669-674. [doi:10.1093/jnci/95.9.669](https://doi.org/10.1093/jnci/95.9.669) · [PubMed 12734318](https://pubmed.ncbi.nlm.nih.gov/12734318/)
