---
schema: human-scale-entry/v1
id: osteosarcoma
name: Osteosarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Osteosarcoma is the most common primary malignant bone tumor; peak 10-20 years; RB1 biallelic loss ~70-75%, TP53 ~30-40%, MDM2 amplification ~6-8%, CDKN2A deletion ~20-30%; MAP protocol (methotrexate+doxorubicin+cisplatin); localized 5-year OS ~70-75%; metastatic ~20-25%."
aliases: ["osteosarcoma", "OSA", "OS bone", "osteogenic sarcoma", "high-grade osteosarcoma", "MAP protocol bone tumor", "pediatric bone cancer", "conventional osteosarcoma"]
sources:
  - id: bielack-2002-coss-osteosarcoma
    type: peer-reviewed
    cite: "Bielack SS, Kempf-Bielack B, Delling G, et al. Prognostic factors in high-grade osteosarcoma of the extremities or trunk: an analysis of 1,702 patients treated on neoadjuvant Cooperative Osteosarcoma Study Group protocols. J Clin Oncol. 2002;20(3):776-790."
    doi: "10.1200/JCO.2002.20.3.776"
    pmid: "11821461"
    url: "https://doi.org/10.1200/JCO.2002.20.3.776"
  - id: marina-2016-euramos1-osteosarcoma
    type: peer-reviewed
    cite: "Marina NM, Smeland S, Bielack SS, et al. Comparison of MAPIE versus MAP in patients with a poor response to preoperative chemotherapy for newly diagnosed high-grade osteosarcoma (EURAMOS-1). Lancet Oncol. 2016;17(10):1396-1408."
    doi: "10.1016/S1470-2045(16)30214-5"
    pmid: "27569442"
    url: "https://doi.org/10.1016/S1470-2045(16)30214-5"
cross_links:
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion (~20-30% osteosarcoma) eliminates both p16 (→ CDK4/6 → RB1 inactivation) and ARF (→ MDM2 → p53 loss); CDK4 amplification (~6-8%) and CDKN2A deletion are mutually exclusive alternative Rb/p53 co-inactivation mechanisms in OS."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB1 biallelic inactivation in ~70-75% high-grade osteosarcoma via deletion, mutation, or methylation; RB1 LOF → E2F-driven proliferation → CCND1/CDK4 upregulation; germline RB1 (hereditary retinoblastoma) increases osteosarcoma risk ~1,000-fold."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations/deletions in ~30-40% high-grade osteosarcoma; MDM2 amplification is mutually exclusive with TP53 mutation as both de-repress MDM2 → p53 degradation; Li-Fraumeni syndrome (germline TP53) confers ~15-fold excess OS risk; TP53 loss predicts poor histologic response."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2 amplification (~6-8% osteosarcoma, ~90% well-differentiated liposarcoma) functionally mimics ARF loss → rapid p53 ubiquitination; MDM2 amplification and TP53 mutation are mutually exclusive in OS; MDM2 inhibitors (idasanutlin) in trials for MDM2-amplified sarcomas."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Osteosarcoma arises from osteoblast progenitors that produce malignant osteoid — its diagnostic hallmark; loss of RB1 and TP53 checkpoints lets these RUNX2/Osterix-lineage cells proliferate, and the growth spurt's high osteoprogenitor turnover explains the adolescent peak."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Hereditary retinoblastoma (germline RB1 loss) is the prototypical osteosarcoma predisposition, raising OS risk ~500-1000-fold as the classic second malignancy — especially within prior radiation fields; this mirrors the somatic RB1 loss in ~70-75% of sporadic high-grade OS."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The pubertal IGF-1 surge drives osteoprogenitor proliferation via IGF1R → PI3K/AKT and MEK/ERK, helping explain why osteosarcoma peaks during the adolescent growth spurt at the fast-growing metaphyses of the distal femur and proximal tibia; ~40% of OS overexpress IGF1R."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Li-Fraumeni syndrome (germline TP53) is a major osteosarcoma predisposition, raising OS risk ~15-fold and making bone sarcoma a sentinel cancer; this mirrors the somatic TP53 loss in ~30-40% of sporadic high-grade OS, as p53 checkpoint failure is central to osteosarcoma biology."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Osteosarcoma is the most common primary bone cancer, arising at the fast-growing metaphyses of long bones — classically the distal femur and proximal tibia around the knee — in the adolescent growth spurt; it produces malignant osteoid and destroys bone, causing pain and a mass."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the dominant metastatic site in osteosarcoma: hematogenous spread seeds pulmonary nodules that determine prognosis, so chest CT staging is essential and surgical metastasectomy of lung lesions — even repeated — is part of curative-intent therapy with chemotherapy."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Osteosarcoma and Ewing sarcoma are the two commonest bone cancers of adolescence: osteosarcoma makes malignant osteoid and arises at the metaphysis of long bones, while Ewing is a small-round-blue-cell tumor driven by EWSR1-FLI1, often diaphyseal or in flat bones."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Osteosarcoma subverts bone remodeling: its malignant osteoblasts lay down disorganized osteoid and recruit osteoclasts that resorb bone, fueling growth—so bone-targeted agents like bisphosphonates, denosumab, and mifamurtide have been trialed against it."
  - target: 01-human/07-system/rothmund-thomson
    relation: connects-to
    note: "Rothmund-Thomson syndrome is a hereditary cause of osteosarcoma: biallelic RECQL4 helicase loss yields poikiloderma, skeletal defects, and a markedly raised osteosarcoma risk—a DNA-repair syndrome that, with Li-Fraumeni and retinoblastoma, predisposes to it."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "Osteosarcoma and MPNST are both aggressive sarcomas that arise as radiation-induced second cancers: years after radiotherapy a high-grade sarcoma can emerge in the treated field, both resist chemotherapy—so a new mass in an irradiated bone or nerve raises alarm."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Osteosarcoma is the tumor that makes bone: its malignant osteoblasts deposit immature osteoid that mineralizes with calcium, producing the dense, disorganized 'sunburst' bone on imaging—calcified matrix distinguishes it from other bone sarcomas."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Osteosarcoma is relatively radioresistant, unlike Ewing sarcoma: photon radiotherapy gives poor local control, so wide surgical resection plus chemotherapy is the mainstay, with radiation reserved for unresectable or palliative cases."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Osteosarcoma is a malignant spindle-cell tumor making osteoid: its fibroblast-like mesenchymal cells produce immature bone matrix directly, distinguishing it from other sarcomas—so finding tumor cells laying down osteoid is the diagnostic hallmark on biopsy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven angiogenesis fuels osteosarcoma and predicts spread: the tumor secretes VEGF to vascularize and metastasize (chiefly to lung), high levels worsen prognosis, and anti-angiogenic kinase inhibitors are used in relapsed disease."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The PI3K/mTOR pathway is active in osteosarcoma: growth signaling through mTOR drives proliferation and survival, so mTOR inhibitors (often with other agents) are studied in this chemotherapy-resistant sarcoma where few targeted options exist."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy treats osteosarcomas at hard-to-reach sites: axial and skull-base tumors that resist surgery and need high radiation doses benefit from protons' sharp dose falloff, sparing the spinal cord and nearby organs in this radioresistant bone cancer."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-ion radiotherapy is an option for unresectable osteosarcoma: heavy ions deliver dense, highly damaging dose to this radioresistant tumor, useful for pelvic or spinal lesions that cannot be removed surgically—available at specialized particle centers."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Osteosarcoma is defined by malignant osteoid: its hallmark is tumor cells laying down disorganized bone matrix (collagen-rich osteoid), so producing osteoid distinguishes it histologically from other bone tumors like Ewing sarcoma."
  - target: 01-human/03-molecular/her2
    relation: connects-to
    note: "Osteosarcoma can express HER2: a fraction of tumors show HER2 on their surface, which correlates with worse outcome and has prompted trials of HER2-directed therapy and CAR-T cells in this hard-to-treat bone cancer."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Osteosarcoma immunotherapy works through macrophages: mifamurtide, added to chemotherapy, activates macrophages to attack residual tumor and improves survival, while tumor-associated macrophages in the lung niche influence whether metastases take hold."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Osteosarcoma grows from the marrow-filled metaphysis outward: it can seed 'skip metastases' elsewhere in the same bone's marrow cavity, a pattern whole-bone MRI looks for because it changes the surgical margin needed for cure."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Osteosarcoma builds disorganized mineralized bone from calcium and phosphorus: the malignant osteoblasts lay down osteoid that calcifies into the 'sunburst' matrix seen on X-ray, and the high bone turnover spills alkaline phosphatase into the blood."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Osteosarcoma is a target for NK-based immunotherapy: because chemotherapy plateaued decades ago, harnessing natural killer cells—and the macrophage-activating drug mifamurtide—is explored to attack the tumor and its lung metastases."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Osteosarcoma leans on the epigenetic enzyme EZH2: this chromatin modifier is overexpressed and silences genes that would restrain growth and promote differentiation, so EZH2 inhibitors are studied against this genomically chaotic cancer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia makes osteosarcoma more aggressive: the bulky, fast-growing bone tumor outstrips its blood supply, and low oxygen drives invasion, metastasis and resistance, helping explain its tendency to spread to the lungs."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Osteosarcoma leans on the PI3K-AKT-mTOR axis: AKT signaling, amplified in this genomically chaotic cancer, fuels growth and survival alongside its mangled tumor-suppressor genes, so AKT-mTOR inhibitors are studied against it."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Osteosarcoma largely evades cytotoxic T cells: despite its many mutations it keeps an immunosuppressive, T-cell-poor microenvironment, so getting killer T cells into the tumor is a major goal where checkpoint drugs alone have disappointed."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Osteosarcoma is a vascular tumor fed by endothelial cells: VEGF drives them to build the dense, chaotic blood supply that nourishes its rapid growth and helps it seed the lungs."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Osteosarcoma chemotherapy threatens the kidneys: the high-dose methotrexate and cisplatin central to its treatment are nephrotoxic, so kidney function is watched closely and guides dosing."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "The fibroblastic osteosarcoma weaves fibrous tissue: this subtype's spindle cells lay down collagen alongside malignant osteoid, blending bone-forming and scar-like tissue within the tumor."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy catches osteosarcoma making bone: the malignant cells swell with dilated rough endoplasmic reticulum spilling disordered osteoid — ultrastructure that betrays their osteoblastic nature when the tumor is too primitive to recognize."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc sits at the heart of osteosarcoma's blood marker: alkaline phosphatase, the enzyme whose serum rise signals tumor bulk and relapse, is a zinc metalloenzyme made by the malignant osteoblasts as they mineralize bone."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Osteosarcoma can drive platelets up: paraneoplastic thrombocytosis appears in a share of patients, and a high platelet count at diagnosis tracks with larger tumors, metastasis, and a poorer prognosis."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Curing osteosarcoma can cost the heart: doxorubicin, a backbone of the MAP chemotherapy regimen, is cardiotoxic in a cumulative dose-dependent way, risking a late dilated cardiomyopathy that survivors must be monitored for for decades."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Osteosarcoma rides the growth spurt: its incidence peaks in adolescence at the fastest-growing metaphyses — the distal femur and proximal tibia — and taller children carry higher risk, tying the tumor to the growth-hormone-driven surge in bone turnover."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Osteosarcoma's chemotherapy frays the nerves: cisplatin, the 'P' of the MAP regimen, damages peripheral sensory neurons and the cochlear nerve, leaving lasting numbness and hearing loss as a price of the cure."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains read the bone tumor: SATB2 and osteocalcin staining confirm the malignant cells are making bone (osteoid), distinguishing osteosarcoma from other small-cell and spindle-cell sarcomas on a difficult biopsy."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The MAP regimen empties the marrow: high-dose methotrexate, doxorubicin, and cisplatin are heavily myelosuppressive, so neutrophil counts crater between cycles and febrile neutropenia is a recurring danger of curative treatment."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Cisplatin in the regimen wastes magnesium: the platinum drug injures the kidney tubule that reclaims it, dropping blood magnesium and potassium so they must be replaced alongside the careful hydration the chemotherapy demands."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Cure threatens fertility in the young: osteosarcoma strikes adolescents, and its high-dose cisplatin and alkylating chemotherapy damages the gonads, so sperm banking and fertility preservation are discussed before the months of treatment begin."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Osteosarcoma keeps its telomeres long: it sustains division either by reactivating TERT telomerase or through the alternative-lengthening-of-telomeres pathway, the immortality mechanism behind one of the most genomically chaotic of cancers."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The tumor stays a step ahead of immunity: osteosarcoma recruits regulatory T cells and tumor-associated macrophages into an immunosuppressive microenvironment, a coldness that has frustrated checkpoint immunotherapy against it."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "It hijacks bone's own demolition signal: osteosarcoma drives RANKL to activate osteoclasts that chew away surrounding bone, feeding a vicious cycle of destruction and tumor growth that makes the RANKL-blocker denosumab a candidate therapy."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "One subtype is defined by a cell-cycle amplicon: parosteal and dedifferentiated osteosarcomas co-amplify CDK4 with MDM2, locking the cell cycle on, which both confirms the diagnosis and points to CDK4/6 inhibitors as targeted treatment."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "It keeps its telomeres long without telomerase: many osteosarcomas lose ATRX and switch on the alternative lengthening of telomeres pathway, an escape from cellular aging that marks aggressive disease and is being explored as a vulnerability."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC amplification drives the aggressive tumor: gains of MYC are recurrent in osteosarcoma's chaotic genome, pushing proliferation and marking metastatic, chemoresistant disease."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The cure scars the heart: doxorubicin, a backbone of osteosarcoma chemotherapy, poisons cardiomyocytes through oxidative and topoisomerase-2β damage, leaving survivors with a lifelong dose-dependent cardiomyopathy risk."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Bone tumor and its surgery both hurt: osteosarcoma causes deep bone pain and can compress nerves, and limb-salvage or amputation leaves neuropathic and phantom-limb pain that shapes long-term rehabilitation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 supports the osteosarcoma cell: activated STAT3 signaling drives proliferation, metastasis and chemoresistance in osteosarcoma, a pathway studied for this tumor that has seen little therapeutic progress in decades."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A sarcoma and major bone surgery clot the veins: osteosarcoma's hypercoagulability, plus the limb-salvage or amputation surgery and immobility of treatment, make venous thromboembolism a significant risk."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Chemo and prosthetic surgery invite infection: dose-dense chemotherapy causes neutropenia, and the endoprosthetic implants of limb-salvage surgery can become infected — both routes to sepsis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracyclines scar a young heart: doxorubicin is a backbone of the MAP regimen for osteosarcoma, and its cumulative dose-dependent cardiotoxicity risks a cardiomyopathy and heart failure that surface during survivorship."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Cisplatin and high-dose methotrexate batter the kidneys: both are central to osteosarcoma chemotherapy and are directly nephrotoxic, and the tubular and electrolyte injury can settle into chronic kidney disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An adolescent cancer with disfiguring surgery strains the mind: the diagnosis in teens and young adults, amputation or limb-salvage and long inpatient chemotherapy contribute to high rates of depression and distress."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Limb-salvage and amputation heal badly: the major bone resection with endoprosthesis or amputation in osteosarcoma, done in chemotherapy-suppressed tissue, leaves wounds prone to infection and slow closure."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Intensive chemotherapy opens the lung to mould: the profound neutropenia from high-dose methotrexate, doxorubicin and cisplatin lets inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A young cancer with high relapse risk breeds worry: the limb loss, lung-metastasis surveillance and uncertain prognosis of osteosarcoma foster chronic health anxiety in survivors alongside low mood."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its metastases home to the lungs: osteosarcoma spreads almost exclusively to the lungs, so pulmonary metastasectomy and lung surveillance dominate its management and prognosis."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Intensive chemo reawakens shingles: the high-dose methotrexate, doxorubicin and cisplatin regimens for osteosarcoma deeply suppress immunity, allowing latent varicella-zoster to reactivate."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its chemo injures the gut and liver: high-dose methotrexate causes severe mucositis and hepatotoxicity, and the multi-agent osteosarcoma regimen brings nausea and GI toxicity."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its chemotherapy is hard on the kidney: cisplatin is nephrotoxic and high-dose methotrexate can precipitate in the renal tubules, needing urine alkalinisation and leucovorin rescue to prevent acute kidney injury."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its cure can scar the heart: the doxorubicin in the MAP regimen for osteosarcoma carries a dose-dependent, long-term cardiotoxicity risk in young survivors."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its drugs and spread reach the nerves: cisplatin causes ototoxicity and peripheral neuropathy, and spinal metastases can compress the cord."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "An immune drug joins its chemo: mifamurtide, a macrophage-activating immunostimulant, is added to chemotherapy for osteosarcoma, while the chemotherapy itself is profoundly immunosuppressive."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It peaks in the growing skeleton: osteosarcoma arises most often at the rapidly growing metaphyses during the adolescent growth spurt, and treatment impairs growth and fertility in survivors."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Beyond chemo, targeted options emerge: multikinase inhibitors such as regorafenib and cabozantinib supplement the MAP chemotherapy backbone in relapsed osteosarcoma, with newer agents under study."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "The MAP regimen is curative: methotrexate, doxorubicin and cisplatin around limb-salvage surgery cure most localised osteosarcoma, the chemotherapy backbone since the 1980s."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It arises in and destroys bone: osteosarcoma is a malignant bone-forming tumour of the metaphysis that breaks through the cortical bone, producing the Codman triangle and sunburst pattern on imaging."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold sarcoma: osteosarcoma has few mutations and an immunosuppressive microenvironment, so PD-1 checkpoint inhibitors have shown little benefit despite trials."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Its metastases home to the lungs: osteosarcoma spreads almost exclusively to the lungs, seeding nodules in the alveolar parenchyma, and surgically removing these pulmonary metastases is central to achieving cure."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Its cure threatens the heart: doxorubicin, a backbone of osteosarcoma chemotherapy, is cardiotoxic and damages the myocardium dose-dependently, so survivors carry a lifelong risk of cardiomyopathy and heart failure."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Two sarcomas of the young, different roots: osteosarcoma arises in bone with a chaotic, p53/RB-driven genome, while rhabdomyosarcoma arises in skeletal-muscle lineage often from a PAX-FOXO1 fusion—distinct origins guiding distinct chemotherapy."
  - target: 01-human/07-system/werner-syndrome
    relation: connects-to
    note: "A RecQ-helicase predisposition: like Rothmund-Thomson, Werner syndrome's RecQ-helicase defect raises osteosarcoma risk, one of the genome-instability syndromes that spawn this bone cancer."
  - target: 01-human/07-system/bloom-syndrome
    relation: connects-to
    note: "Another genome-instability syndrome: Bloom syndrome, a RecQ-helicase disorder with extreme chromosomal instability, predisposes to osteosarcoma among its many early-onset cancers."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Beyond the lungs: while osteosarcoma metastasises chiefly to the lungs, advanced disease can also seed the liver, depositing in the hepatic lobule."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Opposite ways to destroy bone: osteosarcoma is bone-forming, laying down malignant osteoid, whereas multiple myeloma is bone-lytic, activating osteoclasts—two primary bone-resident malignancies that bracket the differential of a destructive bone lesion."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Therapy-related leukaemia: the alkylating agents and etoposide in osteosarcoma chemotherapy damage haematopoietic stem cells, occasionally causing secondary myelodysplasia and acute myeloid leukaemia in long-term survivors."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Hijacked bone-building signal: Wnt/beta-catenin normally commits stem cells to the osteoblast lineage, and its dysregulation in osteosarcoma drives the tumour's aberrant differentiation and metastatic spread."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Kinase target: PDGFR signalling supports osteosarcoma growth and angiogenesis, the basis for multikinase inhibitors such as regorafenib and cabozantinib in advanced disease."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo activation: nuclear YAP from a deregulated Hippo pathway drives osteosarcoma proliferation and is associated with poor prognosis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxia and spread: HIF-1α-driven angiogenesis and adaptation to the hypoxic bone tumour microenvironment promote osteosarcoma growth and metastasis to the lungs."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: with RB1 and CDKN2A loss frequent in osteosarcoma, cyclin D1-CDK4/6 activity propels its cells through the G1 checkpoint."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Developmental signalling: dysregulated Notch signalling promotes osteosarcoma proliferation, invasion and metastasis, an emerging therapeutic target."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Growth-factor signalling: FGFR signalling contributes to osteosarcoma proliferation and is a candidate targetable receptor in this aggressive bone cancer."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "Invasion and metastasis: SRC is hyperactive in osteosarcoma, driving the migration and invasion that seed lung metastases — the rationale for testing SRC inhibitors such as dasatinib in this aggressive bone cancer."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic homing: the CXCL12-CXCR4 axis directs osteosarcoma cells toward the lung and bone marrow, and high CXCR4 expression predicts the pulmonary metastases that dominate osteosarcoma mortality."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Genomic instability: osteosarcoma genomes show chromothripsis and homologous-recombination defects that engage RAD51-mediated repair, underpinning the rationale for PARP inhibitors in HRD-bearing tumours."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: the MAP regimen (methotrexate, doxorubicin, cisplatin) kills osteosarcoma cells through caspase-3-mediated apoptosis, and defects in this death programme underlie the chemoresistance that limits survival in metastatic disease."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Bone-matrix metastasis: osteosarcoma cells secrete osteopontin, the bone-matrix phosphoprotein that promotes their migration and seeding of the lungs, the metastatic site that determines prognosis in this aggressive bone tumour."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage immunotherapy: CCL2 recruits the tumour-associated macrophages of osteosarcoma, the cells reprogrammed by mifamurtide (liposomal MTP-PE), the macrophage-activating immunotherapy added to chemotherapy in non-metastatic disease."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Bone-matrix vicious cycle: bone is the body's largest reservoir of latent TGF-β, and osteoclastic resorption in osteosarcoma releases it to drive tumour proliferation and lung metastasis, the feed-forward loop that links bone turnover to disease progression."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6/STAT3 axis: osteosarcoma cells and their microenvironment secrete IL-6, activating the STAT3 signalling already mapped here to promote proliferation, chemoresistance and lung metastasis, with high IL-6 marking poorer prognosis."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "HGF-MET driver: MET overexpression establishes an autocrine HGF-MET loop capable of transforming osteoblasts, driving the invasive, metastatic phenotype of osteosarcoma and offering a target for MET tyrosine-kinase inhibitors."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "RB-pathway loss: RB1 inactivation (mapped) — the same lesion that links hereditary retinoblastoma to osteosarcoma — releases E2F1 to drive unrestrained proliferation, reinforced by the CDK4/cyclin-D1 amplification already mapped."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K signalling: PIK3CA drives the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) that supports growth and survival in osteosarcoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK-MAPK proliferation: the receptor kinases of osteosarcoma — MET, FGFR, HER2 and PDGFR (all already mapped) — converge on the MAPK-ERK cascade to drive proliferation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory metastasis: IL-6-JAK-STAT3 signalling (IL-6 and STAT3 already mapped) supports osteosarcoma-cell proliferation and the immunosuppressive, pro-metastatic microenvironment."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Chemoresistance: anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the chemoresistance of osteosarcoma."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferation: RAS-ERK signalling (ERK1/2 already mapped) downstream of the receptor tyrosine kinases active in osteosarcoma provides a proliferative input."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes osteosarcoma invasion, pulmonary metastasis and immune evasion."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) within the bone microenvironment promotes osteosarcoma progression and metastasis."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) promotes survival and proliferation in osteosarcoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immunologically variable microenvironment of osteosarcoma, relevant to its emerging immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "The chromosomal instability of osteosarcoma generates cytosolic DNA sensed by cGAS-STING, shaping its inflammatory and immune microenvironment."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by the PTEN-PI3K-AKT axis, modulate the survival and oxidative-stress balance of osteosarcoma cells."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling of osteosarcoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory and immunosuppressive microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic killing is the immune-clearance axis that the immunotherapy-resistant osteosarcoma evades."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the genomically complex osteosarcoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of osteosarcoma cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of osteosarcoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven macrophage recruitment shapes the immunosuppressive microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of osteosarcoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation in the bone microenvironment participates in the progression and osteolysis of osteosarcoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the osteoclast-driven and inflammatory tumor microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Osteoblast-lineage signaling: osteosarcoma arises from the osteoblast lineage whose anabolic program is governed by PTH/PTH1R signaling, the same pathway whose agonism (teriparatide) carries an osteosarcoma safety signal, tying the tumour to bone-anabolic endocrinology."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Invasion and drug resistance: the AXL receptor tyrosine kinase is expressed in osteosarcoma and drives the mesenchymal-like invasion, pulmonary metastasis and chemoresistance that dominate its course, making AXL a candidate target beyond conventional cytotoxics."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune recognition: MHC class II expression on osteosarcoma and its antigen-presenting infiltrate shapes CD4 T-cell help, and its downregulation contributes to the immune evasion that has limited checkpoint-inhibitor efficacy in this immunologically cold sarcoma."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Immune stimulation: IL-2-driven immune-cell activation, alongside the macrophage-activating drug mifamurtide (macrophages already mapped) used in osteosarcoma, aims to mobilise anti-tumour immunity against this chemoresistant sarcoma."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the doxorubicin in the MAP chemotherapy backbone of osteosarcoma is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that limits the dose and threatens long-term survivors."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint context: PD-1 checkpoint blockade has had limited single-agent activity in the cold, low-mutation osteosarcoma, motivating combinations aimed at converting it into an immunoresponsive tumour."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Chemotherapy anaemia: the MAP chemotherapy (methotrexate, doxorubicin, cisplatin) backbone of osteosarcoma is profoundly myelosuppressive, lowering haemoglobin and requiring transfusion support in these young patients."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and lysis stress: the high-dose methotrexate and cisplatin of osteosarcoma therapy generate oxidative stress, to which xanthine oxidase contributes, and rapid cell lysis raises urate, adding tumour-lysis and renal risk."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 helps make osteosarcoma an immunologically cold tumour (PD-1 already mapped), dampening the T-cell response (CD8 already mapped) that the combination immunotherapies under investigation aim to mount."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Osteolytic inflammation: prostaglandins from the tumour and its bone-resorptive microenvironment (RANKL and osteopontin already mapped) promote the osteolysis and inflammation of the bone destruction of osteosarcoma."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, immune-evasive microenvironment of osteosarcoma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the intensive methotrexate, doxorubicin and cisplatin chemotherapy of osteosarcoma is myelosuppressive, causing anaemia (haemoglobin already mapped) that needs transfusion whose repeated support can load the young survivor with iron."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunologically cold microenvironment of osteosarcoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and matrix: copper is the cofactor of lysyl oxidase that cross-links the collagen (already mapped) osteoid, and copper supports the angiogenesis (VEGF already mapped) of the highly vascular osteosarcoma."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the angiogenesis and vascular tone of the highly vascular osteosarcoma, part of the stromal biology of the tumour."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow-adipose growth adipokine: leptin from the marrow adipose tissue and the growth (GH and IGF-1 already mapped) axis signals within the bone microenvironment of the adolescent-peak osteosarcoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipose adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the bone microenvironment of osteosarcoma."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Bone-mineral calcium: the calcium of the bone (RANKL and collagen already mapped) mineral is disturbed by the osteoblastic bone formation and the osteolytic destruction of osteosarcoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Marrow-adipose adipokine: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipose adipokine signalling of the bone microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of osteosarcoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of osteosarcoma (and the mifamurtide-augmented macrophage/Th1 response)."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of osteosarcoma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of osteosarcoma."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the tumour antigen to the T cells (already mapped) shaping the adaptive immune response against osteosarcoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of osteosarcoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of osteosarcoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the macrophage-rich (already mapped) osteosarcoma stroma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chemotherapy anaemia: erythropoietin corrects the severe anaemia induced by MAP chemotherapy in osteosarcoma patients and its receptor (EPOR) on tumour cells suggests a potential direct mitogenic effect."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Bone-pain mediator: bradykinin released at the tumour-bone interface activates B1/B2 receptors on periosteal nociceptors, driving the deep aching bone pain of osteosarcoma—the commonest presenting symptom."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: C5 cleavage generates C5a, which alongside C5aR1 (already mapped) amplifies myeloid recruitment and M2 macrophage polarisation in the osteosarcoma stroma, reinforcing immunosuppression."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Stroma alarmin: TSLP released by the inflamed periosteum and marrow stroma activates dendritic cells (already mapped) and mast cells (already mapped) to shape the type-2 microenvironment of osteosarcoma."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation: C1-esterase inhibitor restrains the complement cascade whose C5a/C5aR1 arm (both already mapped) promotes myeloid recruitment and M2 macrophage polarisation in the osteosarcoma stroma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Stroma mast-cell mediator: histamine released by stromal mast cells (already mapped) amplifies angiogenesis (VEGF already mapped) and prostaglandin-mediated immune evasion in the osteosarcoma microenvironment."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Osteosarcoma melatonin: melatonin inhibits osteosarcoma proliferation and metastasis by suppressing PI3K/AKT (already mapped) and Wnt/β-catenin (already mapped) pathways through MT1/MT2 receptor-mediated cAMP reduction and apoptosis induction in osteosarcoma cells."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Osteosarcoma androgen axis: testosterone via androgen receptor modulates osteosarcoma cell proliferation and mTOR (already mapped) signalling, and the male adolescent peak of osteosarcoma incidence implicates androgen-driven bone growth as a tumour co-driver."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Osteosarcoma serotonin signalling: serotonin via 5-HT2 receptors on osteosarcoma cells activates cAMP-PKA and Wnt/β-catenin (already mapped) pathways, promoting osteosarcoma proliferation and matrix invasion via the bone tumour neuroendocrine axis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Osteosarcoma prolactin: prolactin via JAK2/STAT3 activates osteosarcoma cells and macrophages (already mapped), upregulating mTOR (already mapped) and VEGF (already mapped) pro-proliferative signalling in the osteosarcoma immunosuppressive microenvironment."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Osteosarcoma oxytocin: oxytocin receptors on osteosarcoma cells couple to Gαq-PKC, augmenting Wnt/β-catenin (already mapped) and mTOR (already mapped) signalling to promote osteosarcoma cell proliferation and matrix invasion."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Osteosarcoma vasopressin: vasopressin via V1a receptors on osteosarcoma stroma activates Gαq-PKC-IP3 signalling, converging on mTOR (already mapped) and VEGF (already mapped) angiogenic and pro-invasive cascades in bone tumour progression."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Osteosarcoma selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the osteosarcoma tumour microenvironment; selenium deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Osteosarcoma iodine: iodine-dependent thyroid hormones regulate osteoblast (already mapped) differentiation and T-cytotoxic (already mapped) immune surveillance; iodine deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade of osteosarcoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Osteosarcoma sodium: excess sodium promotes macrophage (already mapped) and T-cytotoxic (already mapped) pro-inflammatory skewing; sodium-induced IL-6 (already mapped) amplifies the VEGF (already mapped) and mTOR (already mapped) angiogenic cascade of osteosarcoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Osteosarcoma potassium: potassium regulates macrophage (already mapped) and T-cytotoxic (already mapped) membrane excitability in the tumour microenvironment; potassium deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade of osteosarcoma."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Osteosarcoma chloride: chloride channels in macrophages (already mapped) and tumour cells modulate cell-volume and invasive potential; chloride dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) angiogenic signalling in the osteosarcoma microenvironment."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Osteosarcoma sulfur: sulfur-containing collagen (already mapped) cross-links and glutathione in macrophages (already mapped) limit oxidative stress; sulfur deficiency amplifies mTOR (already mapped) and IL-6 (already mapped) tumour-promoting cascade of osteosarcoma."
---

# Osteosarcoma

## Overview

**Osteosarcoma (OS)** is the most common primary malignant bone tumor, with ~1,000 new cases/year in the USA (~5 per million/year). It arises from primitive mesenchymal bone-forming cells (osteoblast progenitors) and is defined by the production of malignant osteoid. OS shows a **bimodal age distribution**: a dominant first peak in adolescents and young adults (10-20 years, coinciding with the pubertal growth spurt) and a smaller second peak in adults >65 years (often secondary to Paget's disease, prior radiation, or de-differentiated bone lesions). The metaphyses of the long bones in the lower extremity are the most common sites: **distal femur** (~40%), **proximal tibia** (~20%), and **proximal humerus** (~10%).

**Predisposition syndromes:**
- **Hereditary retinoblastoma** (germline RB1): ~500-fold increased OS risk (~6% lifetime); the prototypical RB1-associated second malignancy; OS risk further elevated in patients who received external-beam radiation for the primary retinoblastoma
- **Li-Fraumeni syndrome** (germline TP53): ~15-fold excess OS risk; ~3-4% of all OS have germline TP53
- **Rothmund-Thomson syndrome** (RECQL4 helicase): congenital poikiloderma + ~30% lifetime OS risk; RECQL4 mutations disrupt DNA replication and repair in osteoprogenitors
- **Werner syndrome** (WRN helicase): adult-onset progeria; premature OS in second OS peak
- **Paget's disease of bone**: osteosarcomatous transformation in ~1% after >10 years; 5-year OS after transformation <5%

**OS prognosis:**
- Localized extremity: 5-year OS ~70-75%
- Localized axial/pelvis/skull: 5-year OS ~30-50% (R0 resection often unachievable)
- Pulmonary metastases (most common site, ~20% at diagnosis): 5-year OS ~20-30%; complete resection of lung mets improves survival
- Relapsed/refractory: 5-year OS ~15-20% (second-line chemotherapy + surgery)

## Structure

### Histological subtypes

**High-grade conventional OS (~80% of all OS):**
- **Osteoblastic** (~50% of conventional): abundant osteoid/woven bone; densely packed spindle cells; "sunburst" periosteal reaction on X-ray; ALP markedly elevated
- **Chondroblastic** (~25%): malignant chondroid matrix predominates; cartilaginous lobules + osteoid foci; MRI shows lobulated T2-hyperintense areas; can mimic chondrosarcoma (IDHA-negative, p53 IHC positive in OS)
- **Fibroblastic** (~25%): spindled cells with minimal osteoid; worst histologic response to chemotherapy among conventional subtypes; overlaps morphologically with fibrosarcoma or MFH — osteoid required for diagnosis

**Low-grade OS:**
- **Parosteal OS** (low-grade, surface): posterior distal femur; densely mineralized; "cauliflower" exophytic; MDM2+/CDK4+ by FISH/IHC; 5-year OS ~90% after surgery alone (no chemotherapy needed)
- **Periosteal OS** (intermediate-grade): posterior tibia/femur; cartilage-predominant; limited chemotherapy use

**Other:**
- **Telangiectatic OS**: cystic spaces filled with blood; X-ray shows "blow-out" lesion; ~5% of OS; responds well to preoperative chemotherapy
- **Small cell OS**: SRBCT morphology; must exclude Ewing sarcoma (EWSR1 FISH negative; osteoid present)
- **Secondary OS**: Paget's, post-irradiation; poor prognosis; older patients; often polyostotic or axial

### Key radiographic features

- "Sunburst" periosteal reaction (perpendicular spicules of periosteal new bone)
- Codman triangle (periosteal elevation at tumor margin)
- Ill-defined permeative bone destruction on X-ray
- MRI: T1-hypointense, T2-heterogeneous; essential for marrow extent and skip lesions
- Staging: CT chest (lung mets), bone scan or FDG-PET (skip mets/distant bone mets)

## Function

### Normal osteoblast biology and OS origin

OS arises from uncommitted or committed osteoblast progenitors in the bone marrow stroma; the cell of origin is likely the **mesenchymal stem cell (MSC)** or an **osteoblast progenitor** that has lost RB1- and TP53-mediated checkpoints:

**Normal osteoblastogenesis:**
- MSC → pre-osteoblast (RUNX2+, SP7/Osterix+) → osteoblast (ALP+, osteocalcin+) → osteocyte
- RB1 enforces differentiation checkpoint: RB1-null osteoprogenitors fail to exit the cell cycle → accumulate genomic instability
- p53 enforces DNA damage response: TP53-null osteoprogenitors escape apoptosis after genotoxic stress → acquire further mutations
- Growth plates in adolescents have the highest osteoprogenitor proliferation rate → peak susceptibility to RB1/TP53 loss events → explains adolescent incidence peak

**IGF-1 signaling in OS:**
High IGF-1 levels during pubertal growth → IGF1R → PI3K/AKT + MEK/ERK → osteoprogenitor proliferation; OS cells overexpress IGF1R (~40%); anti-IGF1R antibodies (robatumumab, ganitumab) showed modest Phase 2 activity in recurrent OS; not yet standard.

## Pathology

### Molecular drivers

**Core tumor suppressors (co-lost in >80% high-grade OS):**
- **RB1 biallelic LOF** (~70-75%): deletion (13q14), frameshift, or nonsense mutations; loss of RB1 G1 checkpoint → E2F-driven osteoprogenitor hyperproliferation; RB1 loss is an early initiating event (shown in Rb1+/+ heterozygous mice with p53 loss)
- **TP53 mutations/deletions** (~30-40%): loss of DNA damage checkpoint; enables acquisition of complex chromosomal instability; TP53 LOF in pediatric OS often occurs via large chromosomal deletions (17p13)

**Alternative pathway activation (mutually exclusive events):**
- **MDM2 amplification** (~6-8%): functionally equivalent to TP53 mutation; co-amplified with CDK4 at 12q14-15 in a subset (especially dedifferentiated osteosarcoma, parosteal OS)
- **CDK4 amplification** (~6-8%): functionally equivalent to CDKN2A deletion; drives G1 bypass
- **CDKN2A homozygous deletion** (~20-30%): eliminates both p16 (→ CDK4/6 → RB1) and p14/ARF (→ MDM2 → p53)

**Secondary alterations:**
- **ATRX mutations** (~25%): alternative lengthening of telomeres (ALT pathway); associated with longer median OS survival in some series
- **DLG2 deletions** (~30%): postsynaptic density protein; mechanism of pro-tumorigenic effect unclear
- **WNT pathway**: CTNNB1 mutations (rare); DKK1 overexpression in OS stroma
- **PI3K/AKT/mTOR** pathway activation (~30-35%): PIK3CA mutations, PTEN loss, AKT amplification
- **VEGF/PDGFR** overexpression: correlates with metastatic phenotype; sorafenib, cabozantinib, regorafenib target these

**Chromosomal instability:**
OS karyotypes are typically highly complex (tens of structural rearrangements, chromothripsis events); unlike Ewing sarcoma or synovial sarcoma, OS has no single defining translocation; WGS reveals chromothripsis at chromosome 11, 12, and 17 in ~30-50% of OS; the extremely complex karyotype reflects the consequences of early RB1/TP53 loss allowing unchecked mitotic errors.

### Treatment

**Neoadjuvant MAP protocol (standard backbone):**
- **M** = high-dose methotrexate (HDMTX) 12 g/m²/cycle with leucovorin rescue; mechanism: DHFR inhibition → thymidylate depletion → DNA replication block
- **A** = doxorubicin 75 mg/m² (Adriamycin); intercalation → TOP2A inhibition → DSBs
- **P** = cisplatin 100-120 mg/m²/cycle; DNA intrastrand cross-links → apoptosis
- Standard cycle: 2 cycles MAP neoadjuvant → surgery → 4 cycles MAP adjuvant (total 6 cycles MAP over ~9-10 months); some protocols use 3 cycles neoadjuvant

**Histologic response (Huvos grading):**
- Grade I: <50% necrosis (poor)
- Grade II: 50-89% necrosis (partial response)
- Grade III: 90-99% necrosis (good response)
- Grade IV: 100% necrosis (complete pathologic response)
- **Good responder (≥90% necrosis)**: continue MAP adjuvant → 5-year EFS ~75-80%
- **Poor responder (<90% necrosis)**: historically, no benefit adding ifosfamide+etoposide (IE)

**EURAMOS-1 (Marina 2016):** [^marina-2016-euramos1-osteosarcoma] N=2,260 patients; largest prospective OS study; poor responders randomized to MAP vs MAP+IE: 3-year EFS 48% vs 47% (HR 0.98, 95% CI 0.77-1.25); no benefit to intensification with IE in poor responders; MAP remains standard for all risk groups; 5-year EFS for good responders 65%, poor responders 52%.

**COSS data (Bielack 2002):** [^bielack-2002-coss-osteosarcoma] Prognostic factors from 1,702 patients: poor response to chemotherapy, axial location, metastases at diagnosis, and elevated LDH are independent adverse prognostic factors.

**Limb-salvage surgery:**
- ~90% of OS patients can undergo limb-salvage surgery (endoprosthesis, allograft, rotationplasty)
- R0 resection required: wide surgical margin (≥2 cm preferred, or anatomical barrier)
- Local recurrence with R0: <5%; R1/R2 → high local recurrence risk
- Rotationplasty (Van Nes procedure): ankle-joint as neo-knee; functional outcomes comparable to endoprosthesis in very young children

**Radiation:**
OS is relatively radiation-resistant (high-dose radiation ~70+ Gy may achieve local control); primary RT reserved for unresectable lesions (skull base, spine); palliative RT for pain control; no role for adjuvant RT after R0 surgery.

**Relapsed/refractory OS:**
- Second-line chemotherapy: ifosfamide+etoposide (IE), gemcitabine+docetaxel (~20-25% ORR), carboplatin+etoposide
- Sorafenib (Phase 2, Grignani 2012): median OS 14 weeks vs 4 weeks historical control in relapsed OS; modest activity
- Regorafenib (REGOBONE trial, Duffaud 2019): ORR 5%, but PFS benefit (3.6 vs 1.7 months, HR 0.43, p=0.008) in relapsed OS
- Cabozantinib: MET/VEGFR/RET inhibitor; Phase 2 CABONE trial in bone sarcomas showing some PFS benefit
- Pulmonary metastasectomy: if lung mets are few and resectable, aggressive thoracotomy → 5-year OS ~25-35% in selected patients
- HDCT+auto-SCT: no proven benefit in OS (unlike Ewing sarcoma); not standard
- Immunotherapy: immune desert tumor (low TMB, immunosuppressive TME); PD-L1 variable; pembrolizumab single-agent ORR ~5% in unselected OS; dinutuximab (anti-GD2): GD2 expressed on ~40-60% OS → Phase 2 trials ongoing

**Emerging targets:**
- CDK4/6 inhibitors: MDM2/CDK4-co-amplified OS (parosteal) are sensitive; palbociclib Phase 2 (SARC033) for CDK4-amplified sarcomas
- MDM2 inhibitors (idasanutlin, milademetan): TP53-WT MDM2-amplified OS; dose-limiting thrombocytopenia managed with G-CSF
- WEE1 inhibitors (adavosertib): exploit replication stress in p53-deficient OS; Phase 2 ongoing
- mTOR inhibitors (ridaforolimus): activity in bone sarcomas; Phase 2 data modest; used in combination with PI3K inhibitors
- CAR-T cell therapy: GD2-directed, HER2-directed, B7-H3-directed CAR-T constructs in early Phase 1 trials

## Connections

- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion (~20-30% osteosarcoma) eliminates both p16 (→ CDK4/6 → RB1 inactivation) and ARF (→ MDM2 → p53 loss); CDK4 amplification (~6-8%) and CDKN2A deletion are mutually exclusive alternative Rb/p53 co-inactivation mechanisms in OS.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — RB1 biallelic inactivation in ~70-75% high-grade osteosarcoma via deletion, mutation, or methylation; RB1 LOF → E2F-driven proliferation → CCND1/CDK4 upregulation; germline RB1 (hereditary retinoblastoma) increases osteosarcoma risk ~1,000-fold.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations/deletions in ~30-40% high-grade osteosarcoma; MDM2 amplification is mutually exclusive with TP53 mutation as both de-repress MDM2 → p53 degradation; Li-Fraumeni syndrome (germline TP53) confers ~15-fold excess OS risk; TP53 loss predicts poor histologic response.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 amplification (~6-8% osteosarcoma, ~90% well-differentiated liposarcoma) functionally mimics ARF loss → rapid p53 ubiquitination; MDM2 amplification and TP53 mutation are mutually exclusive in OS; MDM2 inhibitors (idasanutlin) in trials for MDM2-amplified sarcomas.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Osteosarcoma arises from osteoblast progenitors that produce malignant osteoid — its diagnostic hallmark; loss of RB1 and TP53 checkpoints lets these RUNX2/Osterix-lineage cells proliferate, and the growth spurt's high osteoprogenitor turnover explains the adolescent peak.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Hereditary retinoblastoma (germline RB1 loss) is the prototypical osteosarcoma predisposition, raising OS risk ~500-1000-fold as the classic second malignancy — especially within prior radiation fields; this mirrors the somatic RB1 loss in ~70-75% of sporadic high-grade OS.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The pubertal IGF-1 surge drives osteoprogenitor proliferation via IGF1R → PI3K/AKT and MEK/ERK, helping explain why osteosarcoma peaks during the adolescent growth spurt at the fast-growing metaphyses of the distal femur and proximal tibia; ~40% of OS overexpress IGF1R.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Li-Fraumeni syndrome (germline TP53) is a major osteosarcoma predisposition, raising OS risk ~15-fold and making bone sarcoma a sentinel cancer; this mirrors the somatic TP53 loss in ~30-40% of sporadic high-grade OS, as p53 checkpoint failure is central to osteosarcoma biology.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Osteosarcoma is the most common primary bone cancer, arising at the fast-growing metaphyses of long bones — classically the distal femur and proximal tibia around the knee — in the adolescent growth spurt; it produces malignant osteoid and destroys bone, causing pain and a mass.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the dominant metastatic site in osteosarcoma: hematogenous spread seeds pulmonary nodules that determine prognosis, so chest CT staging is essential and surgical metastasectomy of lung lesions — even repeated — is part of curative-intent therapy with chemotherapy.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Osteosarcoma and Ewing sarcoma are the two commonest bone cancers of adolescence: osteosarcoma makes malignant osteoid and arises at the metaphysis of long bones, while Ewing is a small-round-blue-cell tumor driven by EWSR1-FLI1, often diaphyseal or in flat bones.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Osteosarcoma subverts bone remodeling: its malignant osteoblasts lay down disorganized osteoid and recruit osteoclasts that resorb bone, fueling growth—so bone-targeted agents like bisphosphonates, denosumab, and mifamurtide have been trialed against it.
- `connects-to` → **[Rothmund-Thomson Syndrome](../rothmund-thomson/README.md)** — Rothmund-Thomson syndrome is a hereditary cause of osteosarcoma: biallelic RECQL4 helicase loss yields poikiloderma, skeletal defects, and a markedly raised osteosarcoma risk—a DNA-repair syndrome that, with Li-Fraumeni and retinoblastoma, predisposes to it.
- `connects-to` → **[MPNST](../mpnst/README.md)** — Osteosarcoma and MPNST are both aggressive sarcomas that arise as radiation-induced second cancers: years after radiotherapy a high-grade sarcoma can emerge in the treated field, both resist chemotherapy—so a new mass in an irradiated bone or nerve raises alarm.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Osteosarcoma is the tumor that makes bone: its malignant osteoblasts deposit immature osteoid that mineralizes with calcium, producing the dense, disorganized 'sunburst' bone on imaging—calcified matrix distinguishes it from other bone sarcomas.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Osteosarcoma is relatively radioresistant, unlike Ewing sarcoma: photon radiotherapy gives poor local control, so wide surgical resection plus chemotherapy is the mainstay, with radiation reserved for unresectable or palliative cases.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Osteosarcoma is a malignant spindle-cell tumor making osteoid: its fibroblast-like mesenchymal cells produce immature bone matrix directly, distinguishing it from other sarcomas—so finding tumor cells laying down osteoid is the diagnostic hallmark on biopsy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis fuels osteosarcoma and predicts spread: the tumor secretes VEGF to vascularize and metastasize (chiefly to lung), high levels worsen prognosis, and anti-angiogenic kinase inhibitors are used in relapsed disease.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The PI3K/mTOR pathway is active in osteosarcoma: growth signaling through mTOR drives proliferation and survival, so mTOR inhibitors (often with other agents) are studied in this chemotherapy-resistant sarcoma where few targeted options exist.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy treats osteosarcomas at hard-to-reach sites: axial and skull-base tumors that resist surgery and need high radiation doses benefit from protons' sharp dose falloff, sparing the spinal cord and nearby organs in this radioresistant bone cancer.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-ion radiotherapy is an option for unresectable osteosarcoma: heavy ions deliver dense, highly damaging dose to this radioresistant tumor, useful for pelvic or spinal lesions that cannot be removed surgically—available at specialized particle centers.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Osteosarcoma is defined by malignant osteoid: its hallmark is tumor cells laying down disorganized bone matrix (collagen-rich osteoid), so producing osteoid distinguishes it histologically from other bone tumors like Ewing sarcoma.
- `connects-to` → **[HER2](../../03-molecular/her2/README.md)** — Osteosarcoma can express HER2: a fraction of tumors show HER2 on their surface, which correlates with worse outcome and has prompted trials of HER2-directed therapy and CAR-T cells in this hard-to-treat bone cancer.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Osteosarcoma immunotherapy works through macrophages: mifamurtide, added to chemotherapy, activates macrophages to attack residual tumor and improves survival, while tumor-associated macrophages in the lung niche influence whether metastases take hold.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Osteosarcoma grows from the marrow-filled metaphysis outward: it can seed 'skip metastases' elsewhere in the same bone's marrow cavity, a pattern whole-bone MRI looks for because it changes the surgical margin needed for cure.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Osteosarcoma builds disorganized mineralized bone from calcium and phosphorus: the malignant osteoblasts lay down osteoid that calcifies into the 'sunburst' matrix seen on X-ray, and the high bone turnover spills alkaline phosphatase into the blood.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Osteosarcoma is a target for NK-based immunotherapy: because chemotherapy plateaued decades ago, harnessing natural killer cells—and the macrophage-activating drug mifamurtide—is explored to attack the tumor and its lung metastases.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Osteosarcoma leans on the epigenetic enzyme EZH2: this chromatin modifier is overexpressed and silences genes that would restrain growth and promote differentiation, so EZH2 inhibitors are studied against this genomically chaotic cancer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia makes osteosarcoma more aggressive: the bulky, fast-growing bone tumor outstrips its blood supply, and low oxygen drives invasion, metastasis and resistance, helping explain its tendency to spread to the lungs.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Osteosarcoma leans on the PI3K-AKT-mTOR axis: AKT signaling, amplified in this genomically chaotic cancer, fuels growth and survival alongside its mangled tumor-suppressor genes, so AKT-mTOR inhibitors are studied against it.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Osteosarcoma largely evades cytotoxic T cells: despite its many mutations it keeps an immunosuppressive, T-cell-poor microenvironment, so getting killer T cells into the tumor is a major goal where checkpoint drugs alone have disappointed.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Osteosarcoma is a vascular tumor fed by endothelial cells: VEGF drives them to build the dense, chaotic blood supply that nourishes its rapid growth and helps it seed the lungs.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Osteosarcoma chemotherapy threatens the kidneys: the high-dose methotrexate and cisplatin central to its treatment are nephrotoxic, so kidney function is watched closely and guides dosing.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — The fibroblastic osteosarcoma weaves fibrous tissue: this subtype's spindle cells lay down collagen alongside malignant osteoid, blending bone-forming and scar-like tissue within the tumor.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy catches osteosarcoma making bone: the malignant cells swell with dilated rough endoplasmic reticulum spilling disordered osteoid — ultrastructure that betrays their osteoblastic nature when the tumor is too primitive to recognize.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc sits at the heart of osteosarcoma's blood marker: alkaline phosphatase, the enzyme whose serum rise signals tumor bulk and relapse, is a zinc metalloenzyme made by the malignant osteoblasts as they mineralize bone.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Osteosarcoma can drive platelets up: paraneoplastic thrombocytosis appears in a share of patients, and a high platelet count at diagnosis tracks with larger tumors, metastasis, and a poorer prognosis.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Curing osteosarcoma can cost the heart: doxorubicin, a backbone of the MAP chemotherapy regimen, is cardiotoxic in a cumulative dose-dependent way, risking a late dilated cardiomyopathy that survivors must be monitored for for decades.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Osteosarcoma rides the growth spurt: its incidence peaks in adolescence at the fastest-growing metaphyses — the distal femur and proximal tibia — and taller children carry higher risk, tying the tumor to the growth-hormone-driven surge in bone turnover.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Osteosarcoma's chemotherapy frays the nerves: cisplatin, the 'P' of the MAP regimen, damages peripheral sensory neurons and the cochlear nerve, leaving lasting numbness and hearing loss as a price of the cure.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains read the bone tumor: SATB2 and osteocalcin staining confirm the malignant cells are making bone (osteoid), distinguishing osteosarcoma from other small-cell and spindle-cell sarcomas on a difficult biopsy.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The MAP regimen empties the marrow: high-dose methotrexate, doxorubicin, and cisplatin are heavily myelosuppressive, so neutrophil counts crater between cycles and febrile neutropenia is a recurring danger of curative treatment.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Cisplatin in the regimen wastes magnesium: the platinum drug injures the kidney tubule that reclaims it, dropping blood magnesium and potassium so they must be replaced alongside the careful hydration the chemotherapy demands.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Cure threatens fertility in the young: osteosarcoma strikes adolescents, and its high-dose cisplatin and alkylating chemotherapy damages the gonads, so sperm banking and fertility preservation are discussed before the months of treatment begin.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Osteosarcoma keeps its telomeres long: it sustains division either by reactivating TERT telomerase or through the alternative-lengthening-of-telomeres pathway, the immortality mechanism behind one of the most genomically chaotic of cancers.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The tumor stays a step ahead of immunity: osteosarcoma recruits regulatory T cells and tumor-associated macrophages into an immunosuppressive microenvironment, a coldness that has frustrated checkpoint immunotherapy against it.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — It hijacks bone's own demolition signal: osteosarcoma drives RANKL to activate osteoclasts that chew away surrounding bone, feeding a vicious cycle of destruction and tumor growth that makes the RANKL-blocker denosumab a candidate therapy.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — One subtype is defined by a cell-cycle amplicon: parosteal and dedifferentiated osteosarcomas co-amplify CDK4 with MDM2, locking the cell cycle on, which both confirms the diagnosis and points to CDK4/6 inhibitors as targeted treatment.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — It keeps its telomeres long without telomerase: many osteosarcomas lose ATRX and switch on the alternative lengthening of telomeres pathway, an escape from cellular aging that marks aggressive disease and is being explored as a vulnerability.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC amplification drives the aggressive tumor: gains of MYC are recurrent in osteosarcoma's chaotic genome, pushing proliferation and marking metastatic, chemoresistant disease.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The cure scars the heart: doxorubicin, a backbone of osteosarcoma chemotherapy, poisons cardiomyocytes through oxidative and topoisomerase-2β damage, leaving survivors with a lifelong dose-dependent cardiomyopathy risk.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Bone tumor and its surgery both hurt: osteosarcoma causes deep bone pain and can compress nerves, and limb-salvage or amputation leaves neuropathic and phantom-limb pain that shapes long-term rehabilitation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 supports the osteosarcoma cell: activated STAT3 signaling drives proliferation, metastasis and chemoresistance in osteosarcoma, a pathway studied for this tumor that has seen little therapeutic progress in decades.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A sarcoma and major bone surgery clot the veins: osteosarcoma's hypercoagulability, plus the limb-salvage or amputation surgery and immobility of treatment, make venous thromboembolism a significant risk.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Chemo and prosthetic surgery invite infection: dose-dense chemotherapy causes neutropenia, and the endoprosthetic implants of limb-salvage surgery can become infected — both routes to sepsis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracyclines scar a young heart: doxorubicin is a backbone of the MAP regimen for osteosarcoma, and its cumulative dose-dependent cardiotoxicity risks a cardiomyopathy and heart failure that surface during survivorship.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Cisplatin and high-dose methotrexate batter the kidneys: both are central to osteosarcoma chemotherapy and are directly nephrotoxic, and the tubular and electrolyte injury can settle into chronic kidney disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An adolescent cancer with disfiguring surgery strains the mind: the diagnosis in teens and young adults, amputation or limb-salvage and long inpatient chemotherapy contribute to high rates of depression and distress.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Limb-salvage and amputation heal badly: the major bone resection with endoprosthesis or amputation in osteosarcoma, done in chemotherapy-suppressed tissue, leaves wounds prone to infection and slow closure.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Intensive chemotherapy opens the lung to mould: the profound neutropenia from high-dose methotrexate, doxorubicin and cisplatin lets inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A young cancer with high relapse risk breeds worry: the limb loss, lung-metastasis surveillance and uncertain prognosis of osteosarcoma foster chronic health anxiety in survivors alongside low mood.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its metastases home to the lungs: osteosarcoma spreads almost exclusively to the lungs, so pulmonary metastasectomy and lung surveillance dominate its management and prognosis.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Intensive chemo reawakens shingles: the high-dose methotrexate, doxorubicin and cisplatin regimens for osteosarcoma deeply suppress immunity, allowing latent varicella-zoster to reactivate.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its chemo injures the gut and liver: high-dose methotrexate causes severe mucositis and hepatotoxicity, and the multi-agent osteosarcoma regimen brings nausea and GI toxicity.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its chemotherapy is hard on the kidney: cisplatin is nephrotoxic and high-dose methotrexate can precipitate in the renal tubules, needing urine alkalinisation and leucovorin rescue to prevent acute kidney injury.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its cure can scar the heart: the doxorubicin in the MAP regimen for osteosarcoma carries a dose-dependent, long-term cardiotoxicity risk in young survivors.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its drugs and spread reach the nerves: cisplatin causes ototoxicity and peripheral neuropathy, and spinal metastases can compress the cord.
- `connects-to` → **[Immune System](../immune-system/README.md)** — An immune drug joins its chemo: mifamurtide, a macrophage-activating immunostimulant, is added to chemotherapy for osteosarcoma, while the chemotherapy itself is profoundly immunosuppressive.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It peaks in the growing skeleton: osteosarcoma arises most often at the rapidly growing metaphyses during the adolescent growth spurt, and treatment impairs growth and fertility in survivors.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Beyond chemo, targeted options emerge: multikinase inhibitors such as regorafenib and cabozantinib supplement the MAP chemotherapy backbone in relapsed osteosarcoma, with newer agents under study.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — The MAP regimen is curative: methotrexate, doxorubicin and cisplatin around limb-salvage surgery cure most localised osteosarcoma, the chemotherapy backbone since the 1980s.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It arises in and destroys bone: osteosarcoma is a malignant bone-forming tumour of the metaphysis that breaks through the cortical bone, producing the Codman triangle and sunburst pattern on imaging.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold sarcoma: osteosarcoma has few mutations and an immunosuppressive microenvironment, so PD-1 checkpoint inhibitors have shown little benefit despite trials.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Its metastases home to the lungs: osteosarcoma spreads almost exclusively to the lungs, seeding nodules in the alveolar parenchyma, and surgically removing these pulmonary metastases is central to achieving cure.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Its cure threatens the heart: doxorubicin, a backbone of osteosarcoma chemotherapy, is cardiotoxic and damages the myocardium dose-dependently, so survivors carry a lifelong risk of cardiomyopathy and heart failure.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Two sarcomas of the young, different roots: osteosarcoma arises in bone with a chaotic, p53/RB-driven genome, while rhabdomyosarcoma arises in skeletal-muscle lineage often from a PAX-FOXO1 fusion—distinct origins guiding distinct chemotherapy.
- `connects-to` → **[Werner Syndrome](../werner-syndrome/README.md)** — A RecQ-helicase predisposition: like Rothmund-Thomson, Werner syndrome's RecQ-helicase defect raises osteosarcoma risk, one of the genome-instability syndromes that spawn this bone cancer.
- `connects-to` → **[Bloom Syndrome](../bloom-syndrome/README.md)** — Another genome-instability syndrome: Bloom syndrome, a RecQ-helicase disorder with extreme chromosomal instability, predisposes to osteosarcoma among its many early-onset cancers.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Beyond the lungs: while osteosarcoma metastasises chiefly to the lungs, advanced disease can also seed the liver, depositing in the hepatic lobule.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Opposite ways to destroy bone: osteosarcoma is bone-forming, laying down malignant osteoid, whereas multiple myeloma is bone-lytic, activating osteoclasts—two primary bone-resident malignancies that bracket the differential of a destructive bone lesion.
- `connects-to` → **[AML](../aml/README.md)** — Therapy-related leukaemia: the alkylating agents and etoposide in osteosarcoma chemotherapy damage haematopoietic stem cells, occasionally causing secondary myelodysplasia and acute myeloid leukaemia in long-term survivors.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Hijacked bone-building signal: Wnt/beta-catenin normally commits stem cells to the osteoblast lineage, and its dysregulation in osteosarcoma drives the tumour's aberrant differentiation and metastatic spread.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Kinase target: PDGFR signalling supports osteosarcoma growth and angiogenesis, the basis for multikinase inhibitors such as regorafenib and cabozantinib in advanced disease.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo activation: nuclear YAP from a deregulated Hippo pathway drives osteosarcoma proliferation and is associated with poor prognosis.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxia and spread: HIF-1α-driven angiogenesis and adaptation to the hypoxic bone tumour microenvironment promote osteosarcoma growth and metastasis to the lungs.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: with RB1 and CDKN2A loss frequent in osteosarcoma, cyclin D1-CDK4/6 activity propels its cells through the G1 checkpoint.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Developmental signalling: dysregulated Notch signalling promotes osteosarcoma proliferation, invasion and metastasis, an emerging therapeutic target.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Growth-factor signalling: FGFR signalling contributes to osteosarcoma proliferation and is a candidate targetable receptor in this aggressive bone cancer.
- `connects-to` → **[Src kinase](../../03-molecular/src-kinase/README.md)** — SRC is hyperactive in osteosarcoma, driving the migration and invasion that seed lung metastases—the rationale for testing SRC inhibitors such as dasatinib in this aggressive bone cancer where metastatic spread dominates mortality.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — The CXCL12-CXCR4 axis directs osteosarcoma cells toward the lung and bone marrow, and high CXCR4 expression predicts the pulmonary metastases that dominate osteosarcoma mortality—linking a chemokine gradient to the disease's lethal endpoint.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — Osteosarcoma genomes show chromothripsis and homologous-recombination defects that engage RAD51-mediated repair, underpinning the rationale for PARP inhibitors in the subset of HRD-bearing tumors with this BRCA-like signature.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — The MAP regimen (methotrexate, doxorubicin, cisplatin) kills osteosarcoma cells through caspase-3-mediated apoptosis, and defects in this death program underlie the chemoresistance that limits survival in metastatic disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteosarcoma cells secrete osteopontin, the bone-matrix phosphoprotein that promotes their migration and seeding of the lungs, the metastatic site that determines prognosis in this aggressive bone tumor.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits the tumor-associated macrophages of osteosarcoma, the cells reprogrammed by mifamurtide (liposomal MTP-PE), the macrophage-activating immunotherapy added to chemotherapy in non-metastatic disease.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Bone is the body's largest reservoir of latent TGF-β, and osteoclastic resorption in osteosarcoma releases it to drive tumor proliferation and lung metastasis, a feed-forward loop linking bone turnover to disease progression.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Osteosarcoma cells and their microenvironment secrete IL-6, activating the STAT3 signaling already mapped here to promote proliferation, chemoresistance and lung metastasis, with high IL-6 marking poorer prognosis.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — MET overexpression establishes an autocrine HGF-MET loop capable of transforming osteoblasts, driving the invasive, metastatic phenotype of osteosarcoma and offering a target for MET tyrosine-kinase inhibitors.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — RB1 inactivation (mapped)—the same lesion that links hereditary retinoblastoma to osteosarcoma—releases E2F1 to drive unrestrained proliferation, reinforced by the CDK4/cyclin-D1 amplification already mapped.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA drives the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) that supports growth and survival in osteosarcoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The receptor kinases of osteosarcoma—MET, FGFR, HER2 and PDGFR (all already mapped)—converge on the MAPK-ERK cascade to drive proliferation.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT3 signaling (IL-6 and STAT3 already mapped) supports osteosarcoma-cell proliferation and the immunosuppressive, pro-metastatic microenvironment.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the chemoresistance of osteosarcoma.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-ERK signaling (ERK1/2 already mapped) downstream of the receptor tyrosine kinases active in osteosarcoma provides a proliferative input.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes osteosarcoma invasion, pulmonary metastasis and immune evasion.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) within the bone microenvironment promotes osteosarcoma progression and metastasis.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) promotes survival and proliferation in osteosarcoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immunologically variable microenvironment of osteosarcoma, relevant to its emerging immunotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The chromosomal instability of osteosarcoma generates cytosolic DNA sensed by cGAS-STING, shaping its inflammatory and immune microenvironment.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by the PTEN-PI3K-AKT axis, modulate the survival and oxidative-stress balance of osteosarcoma cells.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling of osteosarcoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory and immunosuppressive microenvironment of osteosarcoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic killing is the immune-clearance axis that the immunotherapy-resistant osteosarcoma evades.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the genomically complex osteosarcoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of osteosarcoma cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of osteosarcoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven macrophage recruitment shapes the immunosuppressive microenvironment of osteosarcoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of osteosarcoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation in the bone microenvironment participates in the progression and osteolysis of osteosarcoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of osteosarcoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the osteoclast-driven and inflammatory tumor microenvironment of osteosarcoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of osteosarcoma.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Osteoblast-lineage signaling: osteosarcoma arises from the osteoblast lineage whose anabolic program is governed by PTH/PTH1R signaling, the same pathway whose agonism (teriparatide) carries an osteosarcoma safety signal, tying the tumour to bone-anabolic endocrinology.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Invasion and drug resistance: the AXL receptor tyrosine kinase is expressed in osteosarcoma and drives the mesenchymal-like invasion, pulmonary metastasis and chemoresistance that dominate its course, making AXL a candidate target beyond conventional cytotoxics.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune recognition: MHC class II expression on osteosarcoma and its antigen-presenting infiltrate shapes CD4 T-cell help, and its downregulation contributes to the immune evasion that has limited checkpoint-inhibitor efficacy in this immunologically cold sarcoma.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Immune stimulation: IL-2-driven immune-cell activation, alongside the macrophage-activating drug mifamurtide (macrophages already mapped) used in osteosarcoma, aims to mobilise anti-tumour immunity against this chemoresistant sarcoma.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the doxorubicin in the MAP chemotherapy backbone of osteosarcoma is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury that limits the dose and threatens long-term survivors.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint context: PD-1 checkpoint blockade has had limited single-agent activity in the cold, low-mutation osteosarcoma, motivating combinations aimed at converting it into an immunoresponsive tumour.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Chemotherapy anaemia: the MAP chemotherapy (methotrexate, doxorubicin, cisplatin) backbone of osteosarcoma is profoundly myelosuppressive, lowering haemoglobin and requiring transfusion support in these young patients.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and lysis stress: the high-dose methotrexate and cisplatin of osteosarcoma therapy generate oxidative stress, to which xanthine oxidase contributes, and rapid cell lysis raises urate, adding tumour-lysis and renal risk.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 helps make osteosarcoma an immunologically cold tumour (PD-1 already mapped), dampening the T-cell response (CD8 already mapped) that the combination immunotherapies under investigation aim to mount.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Osteolytic inflammation: prostaglandins from the tumour and its bone-resorptive microenvironment (RANKL and osteopontin already mapped) promote the osteolysis and inflammation of the bone destruction of osteosarcoma.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages (already mapped) toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, immune-evasive microenvironment of osteosarcoma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the intensive methotrexate, doxorubicin and cisplatin chemotherapy of osteosarcoma is myelosuppressive, causing anaemia (haemoglobin already mapped) that needs transfusion whose repeated support can load the young survivor with iron.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunologically cold microenvironment of osteosarcoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and matrix: copper is the cofactor of lysyl oxidase that cross-links the collagen (already mapped) osteoid, and copper supports the angiogenesis (VEGF already mapped) of the highly vascular osteosarcoma.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the angiogenesis and vascular tone of the highly vascular osteosarcoma, part of the stromal biology of the tumour.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow-adipose growth adipokine: leptin from the marrow adipose tissue and the growth (GH and IGF-1 already mapped) axis signals within the bone microenvironment of the adolescent-peak osteosarcoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipose adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the bone microenvironment of osteosarcoma.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Bone-mineral calcium: the calcium of the bone (RANKL and collagen already mapped) mineral is disturbed by the osteoblastic bone formation and the osteolytic destruction of osteosarcoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Marrow-adipose adipokine: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipose adipokine signalling of the bone microenvironment of osteosarcoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of osteosarcoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of osteosarcoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of osteosarcoma (and the mifamurtide-augmented macrophage/Th1 response).
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of osteosarcoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory microenvironment of osteosarcoma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of osteosarcoma.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of osteosarcoma.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the tumour antigen to the T cells (already mapped) shaping the adaptive immune response against osteosarcoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of osteosarcoma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of osteosarcoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the macrophage-rich (already mapped) osteosarcoma stroma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chemotherapy anaemia: erythropoietin corrects the severe anaemia induced by MAP chemotherapy in osteosarcoma patients and its receptor (EPOR) on tumour cells suggests a potential direct mitogenic effect.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Bone-pain mediator: bradykinin released at the tumour-bone interface activates B1/B2 receptors on periosteal nociceptors, driving the deep aching bone pain of osteosarcoma—the commonest presenting symptom.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: C5 cleavage generates C5a, which alongside C5aR1 (already mapped) amplifies myeloid recruitment and M2 macrophage polarisation in the osteosarcoma stroma, reinforcing immunosuppression.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Stroma alarmin: TSLP released by the inflamed periosteum and marrow stroma activates dendritic cells (already mapped) and mast cells (already mapped) to shape the type-2 microenvironment of osteosarcoma.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation: C1-esterase inhibitor restrains the complement cascade whose C5a/C5aR1 arm (both already mapped) promotes myeloid recruitment and M2 macrophage polarisation in the osteosarcoma stroma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Stroma mast-cell mediator: histamine released by stromal mast cells (already mapped) amplifies angiogenesis (VEGF already mapped) and prostaglandin-mediated immune evasion in the osteosarcoma microenvironment.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Osteosarcoma melatonin: melatonin inhibits osteosarcoma proliferation and metastasis by suppressing PI3K/AKT (already mapped) and Wnt/β-catenin (already mapped) pathways through MT1/MT2 receptor-mediated cAMP reduction and apoptosis induction in osteosarcoma cells.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Osteosarcoma androgen axis: testosterone via androgen receptor modulates osteosarcoma cell proliferation and mTOR (already mapped) signalling, and the male adolescent peak of osteosarcoma incidence implicates androgen-driven bone growth as a tumour co-driver.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Osteosarcoma serotonin signalling: serotonin via 5-HT2 receptors on osteosarcoma cells activates cAMP-PKA and Wnt/β-catenin (already mapped) pathways, promoting osteosarcoma proliferation and matrix invasion via the bone tumour neuroendocrine axis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Osteosarcoma prolactin: prolactin via JAK2/STAT3 activates osteosarcoma cells and macrophages (already mapped), upregulating mTOR (already mapped) and VEGF (already mapped) pro-proliferative signalling in the osteosarcoma immunosuppressive microenvironment.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Osteosarcoma oxytocin: oxytocin receptors on osteosarcoma cells couple to Gαq-PKC, augmenting Wnt/β-catenin (already mapped) and mTOR (already mapped) signalling to promote osteosarcoma cell proliferation and matrix invasion.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Osteosarcoma vasopressin: vasopressin via V1a receptors on osteosarcoma stroma activates Gαq-PKC-IP3 signalling, converging on mTOR (already mapped) and VEGF (already mapped) angiogenic and pro-invasive cascades in bone tumour progression.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Osteosarcoma selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS in the osteosarcoma tumour microenvironment; selenium deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Osteosarcoma iodine: iodine-dependent thyroid hormones regulate osteoblast (already mapped) differentiation and T-cytotoxic (already mapped) immune surveillance; iodine deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade of osteosarcoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Osteosarcoma sodium: excess sodium promotes macrophage (already mapped) and T-cytotoxic (already mapped) pro-inflammatory skewing; sodium-induced IL-6 (already mapped) amplifies the VEGF (already mapped) and mTOR (already mapped) angiogenic cascade of osteosarcoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Osteosarcoma potassium: potassium regulates macrophage (already mapped) and T-cytotoxic (already mapped) membrane excitability in the tumour microenvironment; potassium deficiency amplifies the IL-6 (already mapped) and mTOR (already mapped) pro-tumour cascade of osteosarcoma.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Osteosarcoma chloride: chloride channels in macrophages (already mapped) and tumour cells modulate cell-volume and invasive potential; chloride dysregulation amplifies IL-6 (already mapped) and VEGF (already mapped) angiogenic signalling in the osteosarcoma microenvironment.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Osteosarcoma sulfur: sulfur-containing collagen (already mapped) cross-links and glutathione in macrophages (already mapped) limit oxidative stress; sulfur deficiency amplifies mTOR (already mapped) and IL-6 (already mapped) tumour-promoting cascade of osteosarcoma.

[^bielack-2002-coss-osteosarcoma]: Bielack SS, Kempf-Bielack B, Delling G, et al. Prognostic factors in high-grade osteosarcoma of the extremities or trunk: an analysis of 1,702 patients treated on neoadjuvant Cooperative Osteosarcoma Study Group protocols. *J Clin Oncol.* 2002;20(3):776-790. [doi:10.1200/JCO.2002.20.3.776](https://doi.org/10.1200/JCO.2002.20.3.776) · [PubMed 11821461](https://pubmed.ncbi.nlm.nih.gov/11821461/)
[^marina-2016-euramos1-osteosarcoma]: Marina NM, Smeland S, Bielack SS, et al. Comparison of MAPIE versus MAP in patients with a poor response to preoperative chemotherapy for newly diagnosed high-grade osteosarcoma (EURAMOS-1). *Lancet Oncol.* 2016;17(10):1396-1408. [doi:10.1016/S1470-2045(16)30214-5](https://doi.org/10.1016/S1470-2045(16)30214-5) · [PubMed 27569442](https://pubmed.ncbi.nlm.nih.gov/27569442/)
