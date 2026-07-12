---
schema: human-scale-entry/v1
id: glioblastoma
name: Glioblastoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most aggressive primary brain tumor; IDH-wildtype GBM has EGFRvIII amplification (~40%), PTEN loss (~30%), and TERT promoter mutations. Temozolomide + radiotherapy is standard; tumor-treating fields (TTFields) improve OS; MGMT promoter methylation predicts temozolomide benefit."
aliases: ["GBM", "glioblastoma multiforme", "WHO grade 4 glioma", "IDH-wildtype glioblastoma", "GBM IDH-wt", "high-grade glioma"]
sources:
  - id: stupp-2005-temozolomide
    type: peer-reviewed
    cite: "Stupp R, Mason WP, van den Bent MJ, et al. Radiotherapy plus concomitant and adjuvant temozolomide for glioblastoma. N Engl J Med. 2005;352(10):987-996."
    doi: "10.1056/NEJMoa043330"
    pmid: "15758009"
    url: "https://doi.org/10.1056/NEJMoa043330"
  - id: chinot-2014-bevacizumab
    type: peer-reviewed
    cite: "Chinot OL, Wick W, Mason W, et al. Bevacizumab plus radiotherapy-temozolomide for newly diagnosed glioblastoma. N Engl J Med. 2014;370(8):709-722."
    doi: "10.1056/NEJMoa1308345"
    pmid: "24552318"
    url: "https://doi.org/10.1056/NEJMoa1308345"
cross_links:
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFRvIII (exons 2-7 deletion) is amplified in ~40% of IDH-wt GBM → constitutive EGFR signaling without ligand; EGFR inhibitors ineffective in GBM due to PTEN co-deletion and lack of kinase domain mutation; EGFRvIII-targeted therapies (depatux-m, AMG 596 BiTE) under investigation."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN deletion in ~30-40% of GBM → unrestrained PI3K-AKT-mTOR → proliferation and survival; PTEN/EGFRvIII co-occurrence → RTK-independent PI3K activation; PTEN loss is a major driver of EGFR-targeted therapy resistance in GBM; PI3K inhibitors under clinical investigation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "GBM is among the most angiogenic solid tumors; intratumoral hypoxia → HIF-1alpha → VEGF, PDGF, and SDF-1 → neovascularization and invasion; bevacizumab (anti-VEGF) improves PFS but not OS in newly diagnosed or recurrent GBM; HIF-1alpha also drives GBM stem cell self-renewal."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations in ~85% of IDH-wt GBM and ~90% of oligodendrogliomas → telomere maintenance → replicative immortality; TERT promoter mutation is a diagnostic criterion for IDH-wt GBM in WHO 2021; G-CIMP-positive IDH-mutant gliomas have TERT mutations via separate pathway."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH-wildtype GBM is defined by IDH-WT; IDH-mutant gliomas (grades 2-4) are distinct entities with better prognosis; vorasidenib (IDH1/2 inhibitor) approved 2024 for grade 2 IDH-mutant glioma (INDIGO trial: 27.7 vs 11.1 months PFS); IDH1 IHC distinguishes IDH-mutant from wt GBM."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 mutations in ~15% of GBM define the mesenchymal subtype; NF1 LOF → constitutive RAS-GTP → RAF-MEK-ERK → GBM invasion; NF1-mutant GBM has highest macrophage/microglia infiltration; MEK inhibitors (selumetinib, cobimetinib) under investigation in NF1-mutant recurrent GBM."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "GBM is highly angiogenic; hypoxia → HIF-1α → VEGF → neovascularization; bevacizumab (anti-VEGF) approved for recurrent GBM (2009): improves PFS and reduces edema/steroid use but no OS benefit; bevacizumab+lomustine no better than lomustine alone (EORTC 26101)."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "Glioblastoma and H3K27M diffuse midline glioma are both WHO grade 4 gliomas but molecularly opposite: GBM is the adult hemispheric tumor driven by EGFR/TERT/PTEN, DMG the pediatric midline tumor driven by an epigenetic H3K27M mutation — ONC201 helps DMG, bevacizumab helps GBM."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Glioblastoma is the most aggressive primary brain tumor, infiltrating along white-matter tracts so diffusely that even gross-total resection leaves cells behind, guaranteeing recurrence; the blood-brain barrier blocks most systemic drugs, capping median survival near 15 months."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Up to a third to half of glioblastoma's mass is tumor-associated macrophages and microglia recruited by tumor chemokines; rather than attacking, they are reprogrammed to an immunosuppressive state promoting invasion and angiogenesis, a key reason immunotherapy has failed in GBM."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Glioblastoma is the malignant endpoint of the astrocytic lineage: it arises from astrocytes or their progenitors, retaining GFAP expression, and reactive astrocytes at the tumor margin help build the invasive, pro-tumor microenvironment."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Glioblastoma is defined molecularly against IDH-mutant glioma: true GBM is IDH-wildtype with TERT-promoter mutation, EGFR amplification and +7/-10, carrying the worst prognosis, whereas IDH-mutant astrocytomas are a separate, better-prognosis entity—so IDH status now defines GBM."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Glioblastoma and meningioma are the two commonest primary brain tumors but opposite in nature: GBM is intra-axial, diffusely infiltrative and malignant, while meningioma is extra-axial, usually benign and dural-based, so resectable—distinguished on MRI by location and dural tail."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is a pillar of glioblastoma care: after maximal safe resection, fractionated radiation with concurrent temozolomide (the Stupp protocol) extends survival, yet the tumor inevitably recurs in the irradiated field—radiation delays but cannot cure GBM."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Glioblastoma wires itself into neural circuits: tumor cells form glutamatergic synapses with neurons and interconnect through gap junctions, so neuronal activity drives proliferation—a discovery making synaptic signaling a therapeutic target in this lethal brain cancer."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Glioblastoma is part of the Li-Fraumeni cancer spectrum: germline TP53 loss predisposes to gliomas, and somatic TP53 mutation is a defining alteration in many GBMs—both show how losing p53, the genome's guardian, helps spawn this aggressive tumor."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Glioblastoma blurs glial lineages: though classed as an astrocytic tumor, it harbors cells with oligodendrocyte and progenitor features, reflecting a glioma stem cell of uncertain origin—this plasticity and heterogeneity is a key reason GBM resists targeted therapy."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 loss is a core glioblastoma driver: in one major molecular subtype p53 inactivation, with NF1 and PDGFRA changes, removes the damage checkpoint—so p53 status helps define GBM subgroups even though it has not yet yielded a targeted treatment."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Seizures are a common presentation and complication of glioblastoma: the tumor's glutamate release and cortical irritation provoke epilepsy, so anticonvulsants are often needed—and the neuron-glioma excitatory signaling that causes seizures also fuels growth."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Glioblastoma is the most aggressive primary cancer of the nervous system: it infiltrates the brain diffusely along white-matter tracts, so it cannot be fully removed and recurs despite surgery, radiation and temozolomide—median survival stays around a year."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion helps define and grade glioblastoma: homozygous loss of this cell-cycle brake marks IDH-mutant astrocytomas as grade 4 (glioblastoma-equivalent), so the molecular lesion now overrides histology in classifying these lethal gliomas."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Microvascular proliferation is a hallmark of glioblastoma: VEGF-driven endothelial overgrowth builds abnormal, leaky tumor vessels (with necrosis), so the disordered endothelium defines the pathology and is the target of anti-angiogenic bevacizumab."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Glioblastoma wires itself into neural circuits: like other gliomas it forms synapses with neurons and grows in response to their electrical activity, so peritumoral synaptic signaling fuels invasion—reframing GBM as partly a disease of brain connectivity."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages dominate the glioblastoma microenvironment: tumor-associated macrophages and microglia can make up half the tumor mass and are co-opted to suppress immunity and promote growth, so they are a prime target for breaking GBM's treatment resistance."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate links glioblastoma to seizures and growth: the tumor releases excess glutamate that excites and kills surrounding neurons (causing seizures and making room to invade) while stimulating its own proliferation—so glutamate is both weapon and growth signal."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Glioblastoma builds a profoundly cold immune microenvironment: regulatory T cells and suppressive myeloid cells crowd out cytotoxic lymphocytes, which is why checkpoint immunotherapy that works in other cancers has so far largely failed against GBM."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "One molecular subtype of glioblastoma is driven by PDGF: proneural GBMs amplify PDGFRA, so platelet-derived growth factor signaling defines a distinct class of the tumor alongside the classical EGFR-driven and mesenchymal NF1-driven types."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Glioblastoma disables the cell-cycle brake through CDK4/6: amplification of these kinases (with CDKN2A loss) drives uncontrolled division by inactivating Rb, making CDK4/6 inhibitors a rational—if still experimental—targeted strategy."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Glioblastoma's hallmark is death from lack of oxygen: the tumor outgrows its blood supply, leaving necrotic cores ringed by 'pseudopalisading' cells, and the surrounding hypoxia drives the VEGF angiogenesis and treatment resistance that define it."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Glioblastoma taps brain activity through calcium: it forms functional synapses with neurons, and the glutamate-triggered calcium influx spurs the tumor to grow and invade, linking neural firing to its relentless spread."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Glioblastoma fends off cytotoxic T cells: it builds a deeply immunosuppressive, T-cell-poor microenvironment, which is why checkpoint inhibitors have largely failed and why getting killer T cells into the tumor is a major research goal."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton beams help spare the brain in glioma radiotherapy: by depositing their energy at a precise depth, protons hit the tumor while sparing surrounding healthy brain, an option weighed for selected gliomas."
  - target: 01-human/03-molecular/aquaporin-4
    relation: connects-to
    note: "Glioblastoma swells the brain through aquaporin-4: the water channel on astrocytes governs the vasogenic edema that surrounds the tumor, raising intracranial pressure—the swelling steroids are given to control."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Glioblastoma disturbs the brain's potassium: astrocyte potassium buffering fails around the tumor, and the resulting ionic imbalance fuels the peritumoral excitability and seizures that often herald the cancer."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Glioblastoma hoards iron to grow and may die by ferroptosis: its high iron demand fuels proliferation, so triggering iron-dependent cell death is an emerging strategy against this lethal tumor."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The mesenchymal subtype of glioblastoma turns fibroblast-like: it takes on an invasive, scar-cell character, and perivascular fibroblasts help build the treatment-resistant niche that shields it."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Glioblastoma's chemotherapy hits the marrow: temozolomide's main toxicity is myelosuppression, dropping platelets and blood counts, the limit on how much of the drug can be given."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows glioblastoma's defining features: tumor cells crowding in palisades around ribbons of necrosis, and the bizarre glomeruloid tufts of microvascular proliferation, hallmarks that separate it from lower-grade gliomas."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Glioblastoma almost never leaves the brain, but rarely it does: extracranial metastases to the lung, bone, and lymph nodes — sometimes seeded by surgery or a shunt — are a rare curiosity of an otherwise CNS-confined cancer."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Glioblastoma steals vision as it grows: invading the optic pathways and raising pressure in the skull, it cuts out fields of sight and swells the optic disc, neurological signs that often bring the patient in."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An anti-angiogenic antibody fights its blood supply: bevacizumab, targeting VEGF, is used in recurrent glioblastoma to starve the tumor's vessels and shrink the edema, easing symptoms though not curing the disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Temozolomide quietly empties the marrow: the alkylating chemotherapy paired with radiation suppresses neutrophils and lymphocytes, so blood counts are monitored and PJP prophylaxis given against the resulting infection risk."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "High-dose steroids tame the brain swelling at a cost: dexamethasone shrinks glioblastoma's peritumoral edema but suppresses the adrenal glands and raises blood sugar, so it is tapered as carefully as it is started."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Glioblastoma is one of the most clot-prone cancers: the tumor pours out tissue factor while paresis and surgery add stasis, so deep-vein thrombosis and pulmonary embolism strike a large share of patients and complicate their care."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 fuels the tumor's worst traits: it drives the aggressive mesenchymal subtype and reprograms infiltrating microglia and macrophages into an immunosuppressive state, helping glioblastoma evade attack and resist therapy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are being enlisted against it: vaccines that load a patient's own dendritic cells with tumor antigen (DCVax-L) aim to prime an immune attack on glioblastoma, one of the immunotherapy strategies tested against this cold tumor."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PTEN loss unleashes mTOR: the resulting PI3K-AKT-mTOR overdrive fuels glioblastoma growth and survival, a pathway repeatedly targeted — though resistance has frustrated mTOR inhibitors in the clinic."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells are recruited to fight the cold tumor: glioblastoma evades them through stress-ligand shedding and an immunosuppressive microenvironment, and NK-cell and CAR-NK therapies aim to restore that attack."
  - target: 01-human/07-system/lynch-syndrome
    relation: connects-to
    note: "Mismatch-repair failure can seed it: constitutional MMR deficiency and Lynch (Turcot) syndrome predispose to glioblastoma, and the hypermutated tumors that result are a rare setting where checkpoint immunotherapy may help."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "ATRX loss marks the astrocytic lineage: especially in IDH-mutant glioblastomas, ATRX inactivation drives alternative lengthening of telomeres and helps distinguish astrocytoma-derived tumors from oligodendroglial ones."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB powers the mesenchymal subtype: constitutive NF-κB signaling (often with NF1 loss) drives the aggressive, treatment-resistant mesenchymal glioblastoma and its immunosuppressive, inflamed microenvironment."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "The tumor and its therapy strike the brain's vessels: glioblastoma's hypercoagulable state and the radiation used to treat it injure cerebral arteries, raising the risk of ischemic stroke alongside the tumor itself."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Tumor-associated microglia stoke the inflammasome: NLRP3 activation in glioblastoma's myeloid cells releases IL-1β that fuels the immunosuppressive, pro-tumor inflammation of its microenvironment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "The tumor and its toll darken mood: depression is strikingly common in glioblastoma, arising from the diagnosis, frontal-lobe disruption and corticosteroids, and it independently worsens function and survival."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Treatment strips immunity: temozolomide-induced lymphopenia and prolonged dexamethasone leave glioblastoma patients prone to opportunistic infection, including Pneumocystis pneumonia, and to sepsis."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its therapy specifically courts it: the combination of temozolomide lymphopenia and prolonged dexamethasone in glioblastoma is a classic setup for Pneumocystis pneumonia, so prophylaxis is given during chemoradiation."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chemo and chronic illness blunt the marrow: temozolomide myelosuppression plus the inflammatory burden of advanced glioblastoma depress erythropoiesis, contributing an anemia of chronic disease to treatment cytopenias."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Antiangiogenic therapy injures the kidney: bevacizumab used in recurrent glioblastoma causes hypertension and proteinuria with glomerular injury that can progress to chronic kidney disease."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its steroids raise blood sugar: the high-dose dexamethasone used to control peritumoral edema in glioblastoma induces insulin resistance, frequently causing steroid-induced hyperglycemia and diabetes."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Temozolomide and steroids open the lung to mold: the lymphopenia from temozolomide plus prolonged dexamethasone deeply suppress immunity in glioblastoma, occasionally permitting invasive aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Steroids and anti-VEGF therapy impair healing: chronic dexamethasone and the bevacizumab used for recurrent glioblastoma blunt the repair of craniotomy wounds, risking dehiscence."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Chronic dexamethasone disturbs the glands: the prolonged steroids used to control glioblastoma oedema cause steroid-induced diabetes and adrenal suppression, and tumours near the sella can damage the pituitary."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its drugs trouble the gut: dexamethasone raises peptic-ulcer risk, temozolomide causes nausea and hepatotoxicity, and progressive disease can impair swallowing with aspiration."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A rapidly fatal brain cancer breeds dread: the dismal prognosis, cognitive decline and steroid effects of glioblastoma foster intense anxiety in patients and families alongside depression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It hides from the immune system: glioblastoma is profoundly immunosuppressive — an immunologically 'cold' tumour that resists checkpoint inhibitors — and the dexamethasone used for oedema further blunts immunity."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Treatment marks the scalp and skin: radiotherapy causes dermatitis and alopecia, dexamethasone thins the skin, and the tumour-treating-fields device causes scalp contact dermatitis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its steroids waste the muscles: the prolonged high-dose dexamethasone used to control peritumoural oedema causes a proximal steroid myopathy and bone loss."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It is intensely prothrombotic: glioblastoma carries one of the highest rates of venous thromboembolism of any cancer, and corticosteroids for oedema add hypertension."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Immobility and immunosuppression threaten the lungs: pulmonary embolism, aspiration in late disease and steroid-related Pneumocystis pneumonia all endanger glioblastoma patients."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Chemotherapy can impair fertility: the temozolomide used against glioblastoma is gonadotoxic, a consideration for the younger patients who receive it."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Temozolomide defines its care: the Stupp protocol — temozolomide chemotherapy with radiation after maximal surgery — is the standard treatment, with benefit greatest in MGMT-methylated tumours."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Anti-angiogenics for recurrence: bevacizumab against VEGF controls oedema and is used at recurrence, though EGFR and other targeted drugs have largely failed against glioblastoma's heterogeneity."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold tumour: PD-1 checkpoint inhibitors have mostly failed in glioblastoma, which has few mutations and a profoundly immunosuppressive microenvironment behind the blood-brain barrier."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Engineering T cells against the brain tumour: CAR-T therapies targeting EGFRvIII, IL13Rα2 and HER2 are in trials for glioblastoma, but antigen heterogeneity, the immunosuppressive microenvironment and the blood-brain barrier have so far limited durable responses."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "It wires itself into the brain like a neuron: glioblastoma cells extend tumour microtubes—long axon-like membrane protrusions built on cytoskeletal transport machinery—that interconnect cells into an invasive network and receive neuron-to-glioma synaptic drive."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Twin emblems of lethal cancer: glioblastoma and pancreatic adenocarcinoma share dismal survival, dense treatment-resistant stroma that walls out drugs, and infiltrative margins that defeat complete surgery despite their different organs and drivers."
  - target: 01-human/07-system/cowden-syndrome
    relation: connects-to
    note: "Germline meets somatic PTEN loss: Cowden syndrome's inherited PTEN inactivation mirrors the somatic PTEN loss common in glioblastoma, a shared driver of the PI3K-AKT-mTOR pathway."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neuron-glioma synapses: glioblastoma, like diffuse midline glioma, wires into neural circuits through activity-dependent and BDNF-driven synapses with neurons that fuel its growth and invasion."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Memory in the crossfire: glioblastoma infiltration and the radiotherapy that treats it injure the hippocampus, driving the memory loss and cognitive decline that dominate quality of life."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Gliomas in NF1: neurofibromatosis type 1 predisposes to optic pathway gliomas in children and higher-grade gliomas including glioblastoma in adults, NF1 loss being a recurrent GBM driver."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Microvascular proliferation: glioblastoma's defining histology is florid, abnormal angiogenesis—glomeruloid tufts of disordered arterial-wall growth driven by VEGF and hypoxia, the target of bevacizumab."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Brain tumours of different ages: glioblastoma is the commonest malignant brain tumour of adults, while medulloblastoma is its childhood counterpart in the cerebellum—two ends of the neuro-oncology spectrum."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Resistance kinase: MET amplification and activation drive glioblastoma growth and emerge as a resistance mechanism to EGFR-targeted therapy, a candidate co-target."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Stem-cell maintenance: Notch signalling sustains glioblastoma stem cells and their self-renewal, contributing to therapy resistance and recurrence after treatment."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Core PI3K-AKT axis: loss of PTEN unleashes PI3K-AKT-mTOR signalling, one of glioblastoma's defining altered pathways driving proliferation and survival."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Stemness oncogene: MYC sustains the glioblastoma stem cells and their biosynthetic, proliferative programme, a downstream hub of its many growth-factor pathways."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: with CDKN2A loss and CDK4 amplification frequent in glioblastoma, cyclin D-CDK4/6 activity drives unrestrained passage through the G1 checkpoint."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic stemness: EZH2 enforces the repressive chromatin state of glioblastoma stem cells, an epigenetic dependency promoting self-renewal and therapy resistance."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Myeloid dominance: CCL2 recruits microglia and monocyte-derived macrophages that make up much of the glioblastoma mass, building the profoundly immunosuppressive microenvironment that defeats immunotherapy."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Immunosuppression and invasion: TGF-beta secreted by glioblastoma suppresses anti-tumour T cells and promotes the diffuse infiltration that makes the tumour impossible to fully resect."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK-RAS-MAPK: ERK signalling downstream of EGFR amplification and PDGFRA drives glioblastoma proliferation, a core mitogenic output of its receptor-tyrosine-kinase lesions."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Stem-cell niche and invasion: CXCL12-CXCR4 signalling anchors glioblastoma stem cells in the perivascular niche and drives the diffuse white-matter invasion that makes the tumour impossible to cure surgically."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cold-tumour innate immunity: the chromosomal instability of glioblastoma generates micronuclei and cytosolic DNA, and STING agonists are being explored to ignite an innate immune response in this immunologically cold tumour."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Treatment resistance: RAD51-mediated homologous-recombination repair helps glioblastoma survive the DNA damage of radiation and temozolomide, a mechanism of the therapy resistance behind its near-universal recurrence."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Neuron-glioma networks: glioblastoma cells form electrical and AMPA-receptor synapses with neurons and connect to each other through gap junctions, and the resulting calcium-mediated network activity drives invasion and proliferation."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "MGMT methylation: methylation of the MGMT DNA-repair-gene promoter silences it and predicts response to temozolomide, the single most important predictive epigenetic biomarker in glioblastoma and an example of DNA methylation determining therapy."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy: EGFRvIII- and other-targeted CAR-T cells aim to kill glioblastoma through perforin and granzyme, though the immunosuppressive microenvironment of this 'cold' tumour has so far limited durable responses."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "RTK-PI3K core pathway: PIK3CA and PIK3R1 mutations activate PI3K (PTEN loss, AKT and mTOR already mapped), the central effector of the receptor-tyrosine-kinase axis that is one of glioblastoma's three core dysregulated pathways."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "RB core pathway: the RB pathway (CDK4/6, cyclin-D1 and CDKN2A already mapped) is inactivated in most glioblastomas, the second of the three core pathways driving this tumour."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 core pathway: MDM2 amplification inactivates p53 (already mapped) in glioblastoma, completing the trio of core dysregulated pathways alongside RTK/PI3K and RB."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RTK-RAS proliferation: RAS-MAPK signalling (NF1 loss and ERK1/2 already mapped) downstream of amplified EGFR and PDGFRA drives the proliferation of glioblastoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 stemness: JAK-STAT3 signalling (STAT3 already mapped) sustains glioblastoma-cell proliferation, stemness, and the immunosuppressive tumour microenvironment."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Therapy resistance: NRF2 antioxidant signalling protects glioblastoma cells from oxidative and alkylating (temozolomide) stress, contributing to treatment resistance."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is highly expressed in glioblastoma, promoting invasion, the mesenchymal phenotype and immune suppression."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) drives the invasion, stemness and immunosuppression of glioblastoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "STAT1-dependent interferon signalling shapes the immune microenvironment and the therapy response of glioblastoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by the PTEN-PI3K-AKT axis, regulate the stemness and metabolic adaptation of glioblastoma stem cells."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling supports the survival and self-renewal of glioblastoma stem cells and is a candidate therapeutic target."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signalling downstream of receptor tyrosine kinases drives the invasion and migration of glioblastoma cells."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from myeloid-derived suppressor cells shape the immunosuppressive microenvironment of glioblastoma."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt-β-catenin signaling sustains glioma stem-cell self-renewal and therapy resistance in glioblastoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the metabolic adaptation and treatment resistance of glioblastoma cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the treatment-resistant glioblastoma stem cells."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of glioblastoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) from the tumor and microglia sustains the immunosuppressive, proliferative microenvironment of glioblastoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven tumor-associated-macrophage recruitment shapes the immunosuppressive microenvironment of glioblastoma."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "YAP1-Hippo signaling participates in the mesenchymal transition and glioma-stem-cell biology of glioblastoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the invasion and proliferation of glioblastoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the immunosuppressive tumor microenvironment of glioblastoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and tumor-immune microenvironment of glioblastoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammatory tumor microenvironment of glioblastoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the immunosuppressive tumor microenvironment of glioblastoma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of glioblastoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin (SPP1) participates in the microglial/macrophage-rich tumor microenvironment and invasion of glioblastoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Cold-tumour antigen presentation: glioblastoma is profoundly immunosuppressive with low MHC-based antigen presentation, and restoring T-cell recognition is central to the vaccine and cellular immunotherapy strategies being tested against it."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "CAR-T therapy: IL-2-driven T-cell expansion supports the EGFRvIII- and other antigen-directed CAR-T therapies (EGFR already mapped) under investigation for glioblastoma, though antigen heterogeneity limits durable responses."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint resistance: glioblastoma has largely resisted PD-1 checkpoint blockade owing to its cold, myeloid-dominated microenvironment, making it a key testbed for combinations that aim to convert it into an immunoresponsive tumour."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Dexamethasone for oedema: glucocorticoids acting through the glucocorticoid receptor reduce the peritumoral vasogenic oedema (aquaporin-4 and VEGF already mapped) of glioblastoma, the mainstay symptom control despite immunosuppressive drawbacks."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 from the myeloid-dominated stroma helps make glioblastoma an immunologically cold tumour (PD-1 already mapped), dampening the T-cell response that checkpoint and CAR-T strategies aim to mount."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Neuronal circuit integration: alongside the glutamatergic neuron-glioma synapses (glutamate already mapped), GABAergic signalling shapes the neuronal activity that drives glioblastoma growth and the peritumoral seizures that mark it."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 microglial polarisation: IL-4 polarises the dominant tumour-associated microglia and macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), central to the immunologically cold microenvironment of glioblastoma."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia (already mapped) and the cyclooxygenase pathway contribute to the immunosuppression and neuroinflammation (IL-6 and IL-1 already mapped) of the glioblastoma microenvironment."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative necrosis: the hypoxic (HIF-1-alpha already mapped) and necrotic glioblastoma generates oxidative stress, to which xanthine oxidase contributes, and the reactive oxygen species add to the tumour microenvironment and treatment resistance."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 niche and CAR-T target: IL-13, with IL-4 (already mapped), supports the M2 microglial niche, and the IL-13 receptor alpha-2 is a glioblastoma-associated antigen targeted by CAR-T and immunotoxin approaches."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Neuron-glioma signalling: alongside the glutamate and GABA (already mapped) synapses, cholinergic acetylcholine signalling is part of the neuronal activity that drives the growth of the electrically integrated glioblastoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "NMDA modulation: magnesium blocks the NMDA receptor and modulates the glutamate (already mapped) excitotoxicity and the neuron-glioma synaptic drive that promote the invasion of glioblastoma."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipid metabolic dependency: glioblastoma depends on the cholesterol and lipid metabolism, importing the astrocyte (already mapped)-derived cholesterol, a metabolic vulnerability being explored therapeutically."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonergic neuromodulation: serotonin modulates the neuron-glioma (glutamate, GABA and acetylcholine already mapped) circuits whose activity drives the growth and invasion of glioblastoma."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Noradrenergic input: noradrenaline is part of the neuronal-activity-dependent (glutamate already mapped) signalling that stimulates the proliferation and invasion of glioblastoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (with the type-I interferon already mapped) is the type-II interferon arm largely defeated by the immunosuppressive, cold microenvironment of glioblastoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate cGAS-STING interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of glioblastoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response, explored (e.g. engineered/oncolytic delivery) against the immunosuppressive glioblastoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin links the metabolic state to the immune response and, with the dexamethasone (glucocorticoid-receptor already mapped)-induced metabolic syndrome, is part of the systemic milieu of glioblastoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu, altered by the steroid therapy of glioblastoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the neuroinflammatory microenvironment of glioblastoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immunosuppressive microenvironment of glioblastoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of the glioblastoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of glioblastoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) and glioma-associated macrophage (already mapped) activation of the immunosuppressive glioblastoma microenvironment."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the sparse T-cell infiltrate of the immunologically cold glioblastoma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the vascular permeability of the glioblastoma microenvironment."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the microglial (already mapped) and myeloid inflammation of the glioblastoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the glioblastoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack in the immunologically cold tumour."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the proliferating glioblastoma cells and the disordered brain-iron handling of the tumour."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-GBM axis: TSLP, from the glioblastoma stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of the EGFR-amplified (already mapped) glioblastoma tumour niche."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-GBM axis: bradykinin, via B1/B2 receptors on glioblastoma endothelium (already mapped) and microglia (already mapped), augments blood-brain-barrier permeability, tumour oedema, and the pro-inflammatory milieu of the glioblastoma microenvironment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-GBM axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia of the glioblastoma core, activates the EPOR on tumour cells (already mapped) and modulates microglia/macrophage (already mapped) polarisation toward a pro-tumour M2 phenotype."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-GBM axis: histamine, released by microglia (already mapped) and mast cells in the glioblastoma microenvironment, signals via H1/H2 receptors on tumour cells and endothelium (already mapped), modulating blood-brain-barrier permeability and immunosuppressive milieu."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-GBM axis: melatonin, crossing the blood-brain barrier, suppresses EGFR (already mapped) and HIF-1α (already mapped) signalling in glioblastoma cells, modulates the circadian immune clock, and enhances sensitivity to temozolomide chemotherapy."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement regulation-GBM axis: the C1-esterase inhibitor limits classical and contact-pathway complement activation in the glioblastoma microenvironment (complement C3/C5/C5aR1 already mapped), modulating the neuroinflammatory and tumour milieu."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "GBM prolactin: prolactin, via PRLR on microglia (already mapped) and macrophages (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "GBM oxytocin: oxytocin, via OXTR on microglia (already mapped) and macrophages (already mapped), attenuates neuroinflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "GBM vasopressin: vasopressin, via V1aR on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "GBM testosterone: testosterone, via AR on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; testosterone deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) glioblastoma cascade."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "GBM selenium: selenium, as GPx in microglia (already mapped) and macrophages (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative T-cytotoxic (already mapped) cascade of glioblastoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "GBM iodine: iodine-dependent thyroid hormones modulate microglia (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of glioblastoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "GBM sodium: sodium-driven osmotic stress on glioma cells and microglia (already mapped) amplifies NF-κB (already mapped) and VEGF (already mapped) tumour-proliferative signalling; sodium excess worsens the IL-6 (already mapped) neuroinflammatory TME of glioblastoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "GBM copper: copper, via ceruloplasmin and SOD in microglia (already mapped) and macrophages (already mapped), scavenges ROS; copper excess amplifies NF-κB (already mapped) and VEGF (already mapped) and mTOR (already mapped) glioblastoma tumour growth and neovascularisation."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "GBM zinc: zinc, via SOD and NF-κB (already mapped) modulation in microglia (already mapped) and T-cytotoxic cells (already mapped), attenuates tumour neuroinflammation; zinc deficiency amplifies VEGF (already mapped) and IL-6 (already mapped) glioblastoma cascade."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "GBM phosphorus: phosphorus, as ATP in microglia (already mapped) and macrophages (already mapped), fuels neuroinflammatory signalling; phosphorus excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) glioblastoma tumour growth cascade."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "GBM chloride: chloride channels on microglia (already mapped) and macrophages (already mapped) regulate volume-regulated apoptosis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade of glioblastoma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "GBM nitrogen: nitric oxide from iNOS in microglia (already mapped) and macrophages (already mapped) modulates tumour immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of glioblastoma."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "GBM carbon: carbon in nucleotides of microglia (already mapped) and macrophages (already mapped) fuels glioblastoma proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade of glioblastoma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "GBM hydrogen: hydrogen via ROS from microglia (already mapped) and macrophages (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) glioblastoma cascade of glioblastoma."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "GBM sulfur: sulfur-containing amino acids in microglia (already mapped) and macrophages (already mapped) regulate redox signalling; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade of glioblastoma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "glioblastoma glp-1: GLP-1 from microglia (already mapped) and astrocytes (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies EGFR (already mapped) and VEGF (already mapped) and mTOR (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "glioblastoma angiotensin-ii: angiotensin II on endothelial cells (already mapped) and glioma cells (already mapped) promotes angiogenesis; angiotensin-II excess amplifies EGFR (already mapped) and VEGF (already mapped) and mTOR (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "glioblastoma rankl: RANKL from microglia (already mapped) and tumour cells (already mapped) modulates neuro-inflammation; rankl excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "glioblastoma fibronectin: fibronectin in microglia (already mapped) and tumour cells (already mapped) promotes invasive ECM remodelling; fibronectin excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "glioblastoma igf-1: IGF-1 from microglia (already mapped) and tumour cells (already mapped) promotes glioma proliferation; igf-1 excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "glioblastoma activin-a: activin-A from microglia (already mapped) and tumour cells (already mapped) promotes glioma invasion; activin-a excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "glioblastoma cgrp: CGRP from microglia (already mapped) and tumour cells (already mapped) modulates glioma neuroimmune tone; cgrp excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "glioblastoma calcitonin: calcitonin from microglia (already mapped) and tumour cells (already mapped) modulates glioma calcium balance; calcitonin dysregulation amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "glioblastoma substance-p: substance-P from microglia (already mapped) and tumour cells (already mapped) modulates glioma pain tone; substance-P excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma."
---

# Glioblastoma

## Overview

**Glioblastoma (GBM)** is the most common and lethal primary brain tumor in adults, classified as **WHO grade 4 glioma**. Under the WHO 2021 CNS tumor classification, glioblastoma is defined as an **IDH-wildtype astrocytic glioma** bearing at least one of: EGFR amplification, TERT promoter mutation, or chromosome 7 gain/10 loss — regardless of histological grade (a histologically grade 2-3 astrocytoma with these molecular features is classified as GBM). This molecular definition replaced the prior histology-only classification and substantially changed clinical trial design and patient prognostication [^stupp-2005-temozolomide].

**Epidemiology:**
- Incidence: ~3.2/100,000 per year; ~15,000 new cases/year in the United States
- Median age at diagnosis: ~64 years; rare before age 40
- Slight male predominance (M:F ~1.6:1)
- Median OS: ~15-17 months with standard treatment (Stupp protocol + TTFields)
- 2-year OS: ~25-30%; 5-year OS: ~5-10%
- No established environmental risk factors; prior cranial irradiation is the only known risk factor

**GBM subtypes (TCGA molecular classification):**
- **Proneural:** IDH-mutant (now reclassified) or IDH-wt with PDGFRA amplification; G-CIMP subtype
- **Classical:** EGFR amplification; RB1 loss; CDKN2A deletion; most common subtype
- **Mesenchymal:** NF1 mutation; CHI3L1/YKL-40 high; MET amplification; associated with higher macrophage infiltration; worst prognosis
- **Neural:** (largely invalidated by subsequent deconvolution studies — contaminating normal neurons)

## Structure

### Tumor architecture and heterogeneity

**Intratumoral heterogeneity:**
GBM is defined by extreme intra- and inter-tumoral heterogeneity. Single-cell RNA sequencing reveals four cellular states within a single tumor:
- **Mesenchymal-like (MES):** High invasive capacity; NF1 mutations; hypoxia-driven; resilient to therapy
- **Neural progenitor-like (NPC):** Sox2+; cycling; TCA-cycle dependent
- **Oligodendrocyte progenitor-like (OPC):** Intermediate proliferative
- **Astrocyte-like (AC):** EGFR-high; quiescent; CDK4 amplification

GBM stem cells (GSCs) cycle between states — particularly from AC/NPC → MES under hypoxia or therapy pressure — explaining therapeutic resistance and recurrence.

**Anatomical compartments:**
- **Enhancing tumor core:** Contrast-enhancing on MRI; necrotic center (pseudopalisading necrosis); active proliferating tumor cells; well-vascularized (VEGF-driven)
- **Non-enhancing infiltrating tumor:** T2/FLAIR abnormality beyond the enhancing rim; diffusely infiltrating GBM cells along white matter tracts → cannot be surgically resected; source of almost all recurrences
- **Perivascular niche:** GSCs reside adjacent to blood vessels; CXCL12/CXCR4 axis maintains GSC niche

### Molecular architecture

**Core GBM driver alterations:**

| Alteration | Frequency | Pathway | Therapeutic Implication |
|------------|-----------|---------|------------------------|
| EGFR amplification | ~40% | RTK → RAS/PI3K | TKIs ineffective; EGFRvIII bispecifics |
| EGFRvIII mutation | ~25% | Constitutive RTK | Vaccine (DCVax-L), bispecifics |
| PTEN deletion | ~30% | PI3K-AKT-mTOR | PI3K inhibitors under study |
| CDKN2A/B deletion | ~50% | CDK4/6-RB | CDK4/6 inhibitors + RT |
| TERT promoter | ~85% | Telomere | No direct target yet |
| TP53 mutation | ~30% | DNA damage | MDM2 inhibitors in study |
| NF1 mutation | ~15% | RAS-MAPK | MEK inhibitors investigated |
| MDM2 amplification | ~15% | p53 suppression | MDM2 inhibitors |
| CDK4 amplification | ~15% | CDK4-RB | CDK4/6 inhibitors |
| PDGFRA amplification | ~10% | RTK/proneural | PDGFR TKIs (limited benefit) |

**MGMT methylation:**
- MGMT (O⁶-methylguanine-DNA methyltransferase) repairs the DNA alkylation caused by temozolomide
- **MGMT promoter methylation** (~40-50% of GBM) silences MGMT expression → reduced DNA repair capacity → 3-4x improved response to temozolomide; methylated tumors have ~23 months median OS vs. ~12.6 months in unmethylated [^stupp-2005-temozolomide]
- MGMT status is assessed by pyrosequencing or methylation-specific PCR; not yet FDA-approved as a companion diagnostic but routinely used in clinical practice

## Function

### Normal glial biology

**Astrocytes (GBM precursor cell type):**
- Provide metabolic support (lactate shuttle, glutamate clearance) for neurons
- Maintain blood-brain barrier
- Respond to injury via reactive astrogliosis (GFAP upregulation)

GBM likely arises from neural stem cells or oligodendrocyte precursor cells (OPCs) rather than mature astrocytes, based on cellular state analysis. IDH-mutant gliomas arise at an earlier, more differentiated progenitor state.

### BBB and immunological sanctuary

The blood-brain barrier (BBB) creates a pharmacological challenge:
- Large molecule drugs (antibodies, ADCs) have minimal BBB penetration
- Temozolomide is a rare alkylating agent with >90% oral bioavailability and good CNS penetration
- Bevacizumab reduces contrast enhancement (BBB disruption) but does not effectively penetrate beyond the non-enhancing infiltrating tumor
- Immunological isolation: brain has reduced lymphocyte trafficking (no lymphatics in parenchyma); GBM exploits this → profound immunosuppression; PD-L1 expression + TGF-beta and IDO secretion by tumor → T cell exclusion

## Pathology

### Histological features

**Pseudopalisading necrosis:** Characteristic GBM hallmark; cells arrayed around necrotic foci in a radiating pattern; driven by hypoxia (necrotic zone) → HIF-1alpha → MES transition → migration away from necrosis → creates moving wave of invasion; area between necrosis and pseudopalisade is maximally hypoxic

**Microvascular proliferation:** Glomeruloid vascular tufts → result of VEGF/PDGFR-B-driven angiogenesis; another WHO diagnostic criterion for grade 4; not seen in grade 2-3 gliomas

**Mitotic activity:** High Ki-67/MIB-1 index (often >20%); numerous mitoses

### Recurrence and progression

**Pattern of recurrence:**
- ~90% recur within 2 cm of the original tumor margin (non-enhancing infiltrating cells)
- True distant recurrence is rare in IDH-wt GBM (vs. IDH-mutant gliomas which can occasionally disseminate via CSF)
- Recurrence is nearly universal despite treatment; median time to progression ~7 months

**Resistance mechanisms:**
- GSC state transition (AC/NPC → MES) under temozolomide pressure
- MGMT upregulation (acquired from unmethylated subclone outgrowth)
- PI3K-AKT-mTOR upregulation after EGFR-targeted therapy
- Hypermutation phenotype in patients treated with prolonged temozolomide (~20% of recurrent GBM)

### Treatment

**Standard frontline (Stupp protocol, 2005):**
1. Maximal safe surgical resection (goal: >95% gross total resection if achievable)
2. Concomitant temozolomide (75 mg/m²/day) + focal radiotherapy (60 Gy in 30 fractions)
3. Adjuvant temozolomide (150-200 mg/m² × 5 days, 28-day cycles × 6 cycles)
4. **+ Tumor-treating fields (TTFields, Optune device):** Alternating electric fields 200 kHz → disrupt mitotic spindle → cell death; EF14 trial → OS 20.9 vs. 16.0 months (Stupp 2017); now standard of care with temozolomide

**Bevacizumab (anti-VEGF):**
- FDA-approved for recurrent GBM (accelerated approval, 2009)
- RTOG 0825 and AVAglio trials: no OS benefit in newly diagnosed GBM despite PFS improvement [^chinot-2014-bevacizumab]
- Reduces corticosteroid requirement; palliative benefit; shrinks contrast enhancement (pseudoresponse pitfall)

**Recurrent GBM:**
- No universally effective standard; options: bevacizumab, lomustine (CCNU), re-irradiation, temozolomide re-challenge (if MGMT methylated + hypermutation-free), clinical trial
- Lomustine + bevacizumab: EORTC 26101 — OS 9.1 vs. 8.6 months (no benefit)

**Immunotherapy (disappointing to date):**
- Pembrolizumab (CheckMate 143, Keynote-028): no significant benefit in recurrent GBM
- DCVax-L (autologous dendritic cell vaccine loaded with tumor lysate): phase 3 showed 19.3 months OS vs. 16.5 months for placebo in newly diagnosed GBM; FDA approved 2023 (accelerated approval)
- EGFRvIII CAR-T, bispecifics, oncolytic virus (DNX-2401): active early-phase studies

**IDH-mutant grade 2 glioma:**
- Vorasidenib (IDH1/2 inhibitor): INDIGO trial → 27.7 vs. 11.1 months PFS; approved 2024; watch-and-wait alternative to RT/chemo in select low-grade IDH-mutant glioma

## Connections

- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFRvIII (exons 2-7 deletion) is amplified in ~40% of IDH-wt GBM → constitutive EGFR signaling without ligand; EGFR inhibitors ineffective in GBM due to PTEN co-deletion and lack of kinase domain mutation; EGFRvIII-targeted therapies (depatux-m, AMG 596 BiTE) under investigation.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN deletion in ~30-40% of GBM → unrestrained PI3K-AKT-mTOR → proliferation and survival; PTEN loss co-occurs with EGFRvIII → redundant RTK-independent PI3K activation; PTEN loss is a major driver of EGFR-targeted therapy resistance in GBM; PI3K inhibitors under clinical investigation.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — GBM is among the most angiogenic solid tumors; intratumoral hypoxia → HIF-1alpha → VEGF, PDGF, and SDF-1 → neovascularization and invasion; bevacizumab (anti-VEGF) improves PFS but not OS in newly diagnosed or recurrent GBM; HIF-1alpha also drives GBM stem cell self-renewal.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations (C228T, C250T) in ~85% of IDH-wt GBM and ~90% of oligodendrogliomas → telomere maintenance → replicative immortality; TERT promoter mutation is a diagnostic criterion for IDH-wt GBM in WHO 2021; G-CIMP-positive IDH-mutant gliomas have TERT mutations via separate pathway.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH-wildtype GBM is defined by IDH-WT; IDH-mutant gliomas (grades 2-4) are distinct entities with better prognosis; vorasidenib (IDH1/2 inhibitor) approved 2024 for grade 2 IDH-mutant glioma (INDIGO trial: 27.7 vs 11.1 months PFS); IDH1 IHC distinguishes IDH-mutant from wt GBM.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 mutations in ~15% of GBM define the mesenchymal subtype; NF1 LOF → constitutive RAS-GTP → RAF-MEK-ERK → GBM invasion; NF1-mutant GBM has highest macrophage/microglia infiltration; MEK inhibitors (selumetinib, cobimetinib) under investigation in NF1-mutant recurrent GBM.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — GBM is highly angiogenic; hypoxia → HIF-1α → VEGF → neovascularization; bevacizumab (anti-VEGF) approved for recurrent GBM (2009): improves PFS and reduces edema/steroid use but no OS benefit; bevacizumab+lomustine no better than lomustine alone (EORTC 26101).
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — Glioblastoma and H3K27M diffuse midline glioma are both WHO grade 4 gliomas but molecularly opposite: GBM is the adult hemispheric tumor driven by EGFR/TERT/PTEN, DMG the pediatric midline tumor driven by an epigenetic H3K27M mutation — ONC201 helps DMG, bevacizumab helps GBM.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Glioblastoma is the most aggressive primary brain tumor, infiltrating along white-matter tracts so diffusely that even gross-total resection leaves cells behind, guaranteeing recurrence; the blood-brain barrier blocks most systemic drugs, capping median survival near 15 months.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Up to a third to half of glioblastoma's mass is tumor-associated macrophages and microglia recruited by tumor chemokines; rather than attacking, they are reprogrammed to an immunosuppressive state promoting invasion and angiogenesis, a key reason immunotherapy has failed in GBM.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Glioblastoma is the malignant endpoint of the astrocytic lineage: it arises from astrocytes or their progenitors, retaining GFAP expression, and reactive astrocytes at the tumor margin help build the invasive, pro-tumor microenvironment.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Glioblastoma is defined molecularly against IDH-mutant glioma: true GBM is IDH-wildtype with TERT-promoter mutation, EGFR amplification and +7/-10, carrying the worst prognosis, whereas IDH-mutant astrocytomas are a separate, better-prognosis entity—so IDH status now defines GBM.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Glioblastoma and meningioma are the two commonest primary brain tumors but opposite in nature: GBM is intra-axial, diffusely infiltrative and malignant, while meningioma is extra-axial, usually benign and dural-based, so resectable—distinguished on MRI by location and dural tail.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is a pillar of glioblastoma care: after maximal safe resection, fractionated radiation with concurrent temozolomide (the Stupp protocol) extends survival, yet the tumor inevitably recurs in the irradiated field—radiation delays but cannot cure GBM.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Glioblastoma wires itself into neural circuits: tumor cells form glutamatergic synapses with neurons and interconnect through gap junctions, so neuronal activity drives proliferation—a discovery making synaptic signaling a therapeutic target in this lethal brain cancer.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Glioblastoma is part of the Li-Fraumeni cancer spectrum: germline TP53 loss predisposes to gliomas, and somatic TP53 mutation is a defining alteration in many GBMs—both show how losing p53, the genome's guardian, helps spawn this aggressive tumor.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Glioblastoma blurs glial lineages: though classed as an astrocytic tumor, it harbors cells with oligodendrocyte and progenitor features, reflecting a glioma stem cell of uncertain origin—this plasticity and heterogeneity is a key reason GBM resists targeted therapy.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 loss is a core glioblastoma driver: in one major molecular subtype p53 inactivation, with NF1 and PDGFRA changes, removes the damage checkpoint—so p53 status helps define GBM subgroups even though it has not yet yielded a targeted treatment.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Seizures are a common presentation and complication of glioblastoma: the tumor's glutamate release and cortical irritation provoke epilepsy, so anticonvulsants are often needed—and the neuron-glioma excitatory signaling that causes seizures also fuels growth.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Glioblastoma is the most aggressive primary cancer of the nervous system: it infiltrates the brain diffusely along white-matter tracts, so it cannot be fully removed and recurs despite surgery, radiation and temozolomide—median survival stays around a year.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion helps define and grade glioblastoma: homozygous loss of this cell-cycle brake marks IDH-mutant astrocytomas as grade 4 (glioblastoma-equivalent), so the molecular lesion now overrides histology in classifying these lethal gliomas.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Microvascular proliferation is a hallmark of glioblastoma: VEGF-driven endothelial overgrowth builds abnormal, leaky tumor vessels (with necrosis), so the disordered endothelium defines the pathology and is the target of anti-angiogenic bevacizumab.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Glioblastoma wires itself into neural circuits: like other gliomas it forms synapses with neurons and grows in response to their electrical activity, so peritumoral synaptic signaling fuels invasion—reframing GBM as partly a disease of brain connectivity.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages dominate the glioblastoma microenvironment: tumor-associated macrophages and microglia can make up half the tumor mass and are co-opted to suppress immunity and promote growth, so they are a prime target for breaking GBM's treatment resistance.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate links glioblastoma to seizures and growth: the tumor releases excess glutamate that excites and kills surrounding neurons (causing seizures and making room to invade) while stimulating its own proliferation—so glutamate is both weapon and growth signal.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Glioblastoma builds a profoundly cold immune microenvironment: regulatory T cells and suppressive myeloid cells crowd out cytotoxic lymphocytes, which is why checkpoint immunotherapy that works in other cancers has so far largely failed against GBM.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — One molecular subtype of glioblastoma is driven by PDGF: proneural GBMs amplify PDGFRA, so platelet-derived growth factor signaling defines a distinct class of the tumor alongside the classical EGFR-driven and mesenchymal NF1-driven types.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Glioblastoma disables the cell-cycle brake through CDK4/6: amplification of these kinases (with CDKN2A loss) drives uncontrolled division by inactivating Rb, making CDK4/6 inhibitors a rational—if still experimental—targeted strategy.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Glioblastoma's hallmark is death from lack of oxygen: the tumor outgrows its blood supply, leaving necrotic cores ringed by 'pseudopalisading' cells, and the surrounding hypoxia drives the VEGF angiogenesis and treatment resistance that define it.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Glioblastoma taps brain activity through calcium: it forms functional synapses with neurons, and the glutamate-triggered calcium influx spurs the tumor to grow and invade, linking neural firing to its relentless spread.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Glioblastoma fends off cytotoxic T cells: it builds a deeply immunosuppressive, T-cell-poor microenvironment, which is why checkpoint inhibitors have largely failed and why getting killer T cells into the tumor is a major research goal.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton beams help spare the brain in glioma radiotherapy: by depositing their energy at a precise depth, protons hit the tumor while sparing surrounding healthy brain, an option weighed for selected gliomas.
- `connects-to` → **[Aquaporin-4](../../03-molecular/aquaporin-4/README.md)** — Glioblastoma swells the brain through aquaporin-4: the water channel on astrocytes governs the vasogenic edema that surrounds the tumor, raising intracranial pressure—the swelling steroids are given to control.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Glioblastoma disturbs the brain's potassium: astrocyte potassium buffering fails around the tumor, and the resulting ionic imbalance fuels the peritumoral excitability and seizures that often herald the cancer.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Glioblastoma hoards iron to grow and may die by ferroptosis: its high iron demand fuels proliferation, so triggering iron-dependent cell death is an emerging strategy against this lethal tumor.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The mesenchymal subtype of glioblastoma turns fibroblast-like: it takes on an invasive, scar-cell character, and perivascular fibroblasts help build the treatment-resistant niche that shields it.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Glioblastoma's chemotherapy hits the marrow: temozolomide's main toxicity is myelosuppression, dropping platelets and blood counts, the limit on how much of the drug can be given.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows glioblastoma's defining features: tumor cells crowding in palisades around ribbons of necrosis, and the bizarre glomeruloid tufts of microvascular proliferation, hallmarks that separate it from lower-grade gliomas.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Glioblastoma almost never leaves the brain, but rarely it does: extracranial metastases to the lung, bone, and lymph nodes — sometimes seeded by surgery or a shunt — are a rare curiosity of an otherwise CNS-confined cancer.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Glioblastoma steals vision as it grows: invading the optic pathways and raising pressure in the skull, it cuts out fields of sight and swells the optic disc, neurological signs that often bring the patient in.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An anti-angiogenic antibody fights its blood supply: bevacizumab, targeting VEGF, is used in recurrent glioblastoma to starve the tumor's vessels and shrink the edema, easing symptoms though not curing the disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Temozolomide quietly empties the marrow: the alkylating chemotherapy paired with radiation suppresses neutrophils and lymphocytes, so blood counts are monitored and PJP prophylaxis given against the resulting infection risk.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — High-dose steroids tame the brain swelling at a cost: dexamethasone shrinks glioblastoma's peritumoral edema but suppresses the adrenal glands and raises blood sugar, so it is tapered as carefully as it is started.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Glioblastoma is one of the most clot-prone cancers: the tumor pours out tissue factor while paresis and surgery add stasis, so deep-vein thrombosis and pulmonary embolism strike a large share of patients and complicate their care.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 fuels the tumor's worst traits: it drives the aggressive mesenchymal subtype and reprograms infiltrating microglia and macrophages into an immunosuppressive state, helping glioblastoma evade attack and resist therapy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are being enlisted against it: vaccines that load a patient's own dendritic cells with tumor antigen (DCVax-L) aim to prime an immune attack on glioblastoma, one of the immunotherapy strategies tested against this cold tumor.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PTEN loss unleashes mTOR: the resulting PI3K-AKT-mTOR overdrive fuels glioblastoma growth and survival, a pathway repeatedly targeted — though resistance has frustrated mTOR inhibitors in the clinic.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells are recruited to fight the cold tumor: glioblastoma evades them through stress-ligand shedding and an immunosuppressive microenvironment, and NK-cell and CAR-NK therapies aim to restore that attack.
- `connects-to` → **[Lynch Syndrome](../lynch-syndrome/README.md)** — Mismatch-repair failure can seed it: constitutional MMR deficiency and Lynch (Turcot) syndrome predispose to glioblastoma, and the hypermutated tumors that result are a rare setting where checkpoint immunotherapy may help.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — ATRX loss marks the astrocytic lineage: especially in IDH-mutant glioblastomas, ATRX inactivation drives alternative lengthening of telomeres and helps distinguish astrocytoma-derived tumors from oligodendroglial ones.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB powers the mesenchymal subtype: constitutive NF-κB signaling (often with NF1 loss) drives the aggressive, treatment-resistant mesenchymal glioblastoma and its immunosuppressive, inflamed microenvironment.
- `connects-to` → **[Stroke](../stroke/README.md)** — The tumor and its therapy strike the brain's vessels: glioblastoma's hypercoagulable state and the radiation used to treat it injure cerebral arteries, raising the risk of ischemic stroke alongside the tumor itself.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Tumor-associated microglia stoke the inflammasome: NLRP3 activation in glioblastoma's myeloid cells releases IL-1β that fuels the immunosuppressive, pro-tumor inflammation of its microenvironment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — The tumor and its toll darken mood: depression is strikingly common in glioblastoma, arising from the diagnosis, frontal-lobe disruption and corticosteroids, and it independently worsens function and survival.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Treatment strips immunity: temozolomide-induced lymphopenia and prolonged dexamethasone leave glioblastoma patients prone to opportunistic infection, including Pneumocystis pneumonia, and to sepsis.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its therapy specifically courts it: the combination of temozolomide lymphopenia and prolonged dexamethasone in glioblastoma is a classic setup for Pneumocystis pneumonia, so prophylaxis is given during chemoradiation.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chemo and chronic illness blunt the marrow: temozolomide myelosuppression plus the inflammatory burden of advanced glioblastoma depress erythropoiesis, contributing an anemia of chronic disease to treatment cytopenias.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Antiangiogenic therapy injures the kidney: bevacizumab used in recurrent glioblastoma causes hypertension and proteinuria with glomerular injury that can progress to chronic kidney disease.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its steroids raise blood sugar: the high-dose dexamethasone used to control peritumoral edema in glioblastoma induces insulin resistance, frequently causing steroid-induced hyperglycemia and diabetes.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Temozolomide and steroids open the lung to mold: the lymphopenia from temozolomide plus prolonged dexamethasone deeply suppress immunity in glioblastoma, occasionally permitting invasive aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Steroids and anti-VEGF therapy impair healing: chronic dexamethasone and the bevacizumab used for recurrent glioblastoma blunt the repair of craniotomy wounds, risking dehiscence.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Chronic dexamethasone disturbs the glands: the prolonged steroids used to control glioblastoma oedema cause steroid-induced diabetes and adrenal suppression, and tumours near the sella can damage the pituitary.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its drugs trouble the gut: dexamethasone raises peptic-ulcer risk, temozolomide causes nausea and hepatotoxicity, and progressive disease can impair swallowing with aspiration.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A rapidly fatal brain cancer breeds dread: the dismal prognosis, cognitive decline and steroid effects of glioblastoma foster intense anxiety in patients and families alongside depression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It hides from the immune system: glioblastoma is profoundly immunosuppressive — an immunologically 'cold' tumour that resists checkpoint inhibitors — and the dexamethasone used for oedema further blunts immunity.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Treatment marks the scalp and skin: radiotherapy causes dermatitis and alopecia, dexamethasone thins the skin, and the tumour-treating-fields device causes scalp contact dermatitis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its steroids waste the muscles: the prolonged high-dose dexamethasone used to control peritumoural oedema causes a proximal steroid myopathy and bone loss.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It is intensely prothrombotic: glioblastoma carries one of the highest rates of venous thromboembolism of any cancer, and corticosteroids for oedema add hypertension.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Immobility and immunosuppression threaten the lungs: pulmonary embolism, aspiration in late disease and steroid-related Pneumocystis pneumonia all endanger glioblastoma patients.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Chemotherapy can impair fertility: the temozolomide used against glioblastoma is gonadotoxic, a consideration for the younger patients who receive it.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Temozolomide defines its care: the Stupp protocol — temozolomide chemotherapy with radiation after maximal surgery — is the standard treatment, with benefit greatest in MGMT-methylated tumours.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Anti-angiogenics for recurrence: bevacizumab against VEGF controls oedema and is used at recurrence, though EGFR and other targeted drugs have largely failed against glioblastoma's heterogeneity.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold tumour: PD-1 checkpoint inhibitors have mostly failed in glioblastoma, which has few mutations and a profoundly immunosuppressive microenvironment behind the blood-brain barrier.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Engineering T cells against the brain tumour: CAR-T therapies targeting EGFRvIII, IL13Rα2 and HER2 are in trials for glioblastoma, but antigen heterogeneity, the immunosuppressive microenvironment and the blood-brain barrier have so far limited durable responses.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — It wires itself into the brain like a neuron: glioblastoma cells extend tumour microtubes—long axon-like membrane protrusions built on cytoskeletal transport machinery—that interconnect cells into an invasive network and receive neuron-to-glioma synaptic drive.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Twin emblems of lethal cancer: glioblastoma and pancreatic adenocarcinoma share dismal survival, dense treatment-resistant stroma that walls out drugs, and infiltrative margins that defeat complete surgery despite their different organs and drivers.
- `connects-to` → **[Cowden Syndrome](../cowden-syndrome/README.md)** — Germline meets somatic PTEN loss: Cowden syndrome's inherited PTEN inactivation mirrors the somatic PTEN loss common in glioblastoma, a shared driver of the PI3K-AKT-mTOR pathway.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Neuron-glioma synapses: glioblastoma, like diffuse midline glioma, wires into neural circuits through activity-dependent and BDNF-driven synapses with neurons that fuel its growth and invasion.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Memory in the crossfire: glioblastoma infiltration and the radiotherapy that treats it injure the hippocampus, driving the memory loss and cognitive decline that dominate quality of life.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Gliomas in NF1: neurofibromatosis type 1 predisposes to optic pathway gliomas in children and higher-grade gliomas including glioblastoma in adults, NF1 loss being a recurrent GBM driver.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Microvascular proliferation: glioblastoma's defining histology is florid, abnormal angiogenesis—glomeruloid tufts of disordered arterial-wall growth driven by VEGF and hypoxia, the target of bevacizumab.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Brain tumours of different ages: glioblastoma is the commonest malignant brain tumour of adults, while medulloblastoma is its childhood counterpart in the cerebellum—two ends of the neuro-oncology spectrum.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Resistance kinase: MET amplification and activation drive glioblastoma growth and emerge as a resistance mechanism to EGFR-targeted therapy, a candidate co-target.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Stem-cell maintenance: Notch signalling sustains glioblastoma stem cells and their self-renewal, contributing to therapy resistance and recurrence after treatment.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Core PI3K-AKT axis: loss of PTEN unleashes PI3K-AKT-mTOR signalling, one of glioblastoma's defining altered pathways driving proliferation and survival.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Stemness oncogene: MYC sustains the glioblastoma stem cells and their biosynthetic, proliferative programme, a downstream hub of its many growth-factor pathways.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: with CDKN2A loss and CDK4 amplification frequent in glioblastoma, cyclin D-CDK4/6 activity drives unrestrained passage through the G1 checkpoint.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic stemness: EZH2 enforces the repressive chromatin state of glioblastoma stem cells, an epigenetic dependency promoting self-renewal and therapy resistance.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Myeloid dominance: CCL2 recruits microglia and monocyte-derived macrophages that make up much of the glioblastoma mass, building the profoundly immunosuppressive microenvironment that defeats immunotherapy.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Immunosuppression and invasion: TGF-beta secreted by glioblastoma suppresses anti-tumour T cells and promotes the diffuse infiltration that makes the tumour impossible to fully resect.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RTK-RAS-MAPK: ERK signalling downstream of EGFR amplification and PDGFRA drives glioblastoma proliferation, a core mitogenic output of its receptor-tyrosine-kinase lesions.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling anchors glioblastoma stem cells in the perivascular niche and drives the diffuse white-matter invasion that makes the tumor impossible to fully resect and dooms it to recurrence.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The chromosomal instability of glioblastoma generates micronuclei and cytosolic DNA, and STING agonists are being explored to ignite an innate immune response in this immunologically "cold" tumor that resists checkpoint blockade.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — RAD51-mediated homologous-recombination repair helps glioblastoma survive the DNA damage of radiation and temozolomide, a mechanism of the treatment resistance that underlies its near-universal recurrence and lethality.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Glioblastoma cells form electrical and AMPA-receptor synapses with neurons and connect to each other through gap junctions, and the resulting calcium-mediated network activity drives invasion and proliferation.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Methylation of the MGMT DNA-repair-gene promoter silences it and predicts response to temozolomide, the single most important predictive epigenetic biomarker in glioblastoma and an example of DNA methylation determining therapy.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — EGFRvIII- and other-targeted CAR-T cells aim to kill glioblastoma through perforin and granzyme, though the immunosuppressive microenvironment of this "cold" tumor has so far limited durable responses.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA and PIK3R1 mutations activate PI3K (PTEN loss, AKT and mTOR already mapped), the central effector of the receptor-tyrosine-kinase axis that is one of glioblastoma's three core dysregulated pathways.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB pathway (CDK4/6, cyclin-D1 and CDKN2A already mapped) is inactivated in most glioblastomas, the second of the three core pathways driving this tumor.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 amplification inactivates p53 (already mapped) in glioblastoma, completing the trio of core dysregulated pathways alongside RTK/PI3K and RB.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (NF1 loss and ERK1/2 already mapped) downstream of amplified EGFR and PDGFRA drives the proliferation of glioblastoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) sustains glioblastoma-cell proliferation, stemness, and the immunosuppressive tumor microenvironment.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling protects glioblastoma cells from oxidative and alkylating (temozolomide) stress, contributing to treatment resistance.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is highly expressed in glioblastoma, promoting invasion, the mesenchymal phenotype and immune suppression.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) drives the invasion, stemness and immunosuppression of glioblastoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — STAT1-dependent interferon signaling shapes the immune microenvironment and the therapy response of glioblastoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by the PTEN-PI3K-AKT axis, regulate the stemness and metabolic adaptation of glioblastoma stem cells.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling supports the survival and self-renewal of glioblastoma stem cells and is a candidate therapeutic target.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of receptor tyrosine kinases drives the invasion and migration of glioblastoma cells.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from myeloid-derived suppressor cells shape the immunosuppressive microenvironment of glioblastoma.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt-β-catenin signaling sustains glioma stem-cell self-renewal and therapy resistance in glioblastoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the metabolic adaptation and treatment resistance of glioblastoma cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the treatment-resistant glioblastoma stem cells.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of glioblastoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) from the tumor and microglia sustains the immunosuppressive, proliferative microenvironment of glioblastoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven tumor-associated-macrophage recruitment shapes the immunosuppressive microenvironment of glioblastoma.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — YAP1-Hippo signaling participates in the mesenchymal transition and glioma-stem-cell biology of glioblastoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the invasion and proliferation of glioblastoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the immunosuppressive tumor microenvironment of glioblastoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and tumor-immune microenvironment of glioblastoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammatory tumor microenvironment of glioblastoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the immunosuppressive tumor microenvironment of glioblastoma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of glioblastoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin (SPP1) participates in the microglial/macrophage-rich tumor microenvironment and invasion of glioblastoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Cold-tumour antigen presentation: glioblastoma is profoundly immunosuppressive with low MHC-based antigen presentation, and restoring T-cell recognition is central to the vaccine and cellular immunotherapy strategies being tested against it.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — CAR-T therapy: IL-2-driven T-cell expansion supports the EGFRvIII- and other antigen-directed CAR-T therapies (EGFR already mapped) under investigation for glioblastoma, though antigen heterogeneity limits durable responses.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint resistance: glioblastoma has largely resisted PD-1 checkpoint blockade owing to its cold, myeloid-dominated microenvironment, making it a key testbed for combinations that aim to convert it into an immunoresponsive tumour.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Dexamethasone for oedema: glucocorticoids acting through the glucocorticoid receptor reduce the peritumoral vasogenic oedema (aquaporin-4 and VEGF already mapped) of glioblastoma, the mainstay symptom control despite immunosuppressive drawbacks.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 from the myeloid-dominated stroma helps make glioblastoma an immunologically cold tumour (PD-1 already mapped), dampening the T-cell response that checkpoint and CAR-T strategies aim to mount.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Neuronal circuit integration: alongside the glutamatergic neuron-glioma synapses (glutamate already mapped), GABAergic signalling shapes the neuronal activity that drives glioblastoma growth and the peritumoral seizures that mark it.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 microglial polarisation: IL-4 polarises the dominant tumour-associated microglia and macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), central to the immunologically cold microenvironment of glioblastoma.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia (already mapped) and the cyclooxygenase pathway contribute to the immunosuppression and neuroinflammation (IL-6 and IL-1 already mapped) of the glioblastoma microenvironment.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative necrosis: the hypoxic (HIF-1-alpha already mapped) and necrotic glioblastoma generates oxidative stress, to which xanthine oxidase contributes, and the reactive oxygen species add to the tumour microenvironment and treatment resistance.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 niche and CAR-T target: IL-13, with IL-4 (already mapped), supports the M2 microglial niche, and the IL-13 receptor alpha-2 is a glioblastoma-associated antigen targeted by CAR-T and immunotoxin approaches.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Neuron-glioma signalling: alongside the glutamate and GABA (already mapped) synapses, cholinergic acetylcholine signalling is part of the neuronal activity that drives the growth of the electrically integrated glioblastoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — NMDA modulation: magnesium blocks the NMDA receptor and modulates the glutamate (already mapped) excitotoxicity and the neuron-glioma synaptic drive that promote the invasion of glioblastoma.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipid metabolic dependency: glioblastoma depends on the cholesterol and lipid metabolism, importing the astrocyte (already mapped)-derived cholesterol, a metabolic vulnerability being explored therapeutically.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonergic neuromodulation: serotonin modulates the neuron-glioma (glutamate, GABA and acetylcholine already mapped) circuits whose activity drives the growth and invasion of glioblastoma.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Noradrenergic input: noradrenaline is part of the neuronal-activity-dependent (glutamate already mapped) signalling that stimulates the proliferation and invasion of glioblastoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (with the type-I interferon already mapped) is the type-II interferon arm largely defeated by the immunosuppressive, cold microenvironment of glioblastoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate cGAS-STING interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of glioblastoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response, explored (e.g. engineered/oncolytic delivery) against the immunosuppressive glioblastoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin links the metabolic state to the immune response and, with the dexamethasone (glucocorticoid-receptor already mapped)-induced metabolic syndrome, is part of the systemic milieu of glioblastoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu, altered by the steroid therapy of glioblastoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the neuroinflammatory microenvironment of glioblastoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immunosuppressive microenvironment of glioblastoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of the glioblastoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of glioblastoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) and glioma-associated macrophage (already mapped) activation of the immunosuppressive glioblastoma microenvironment.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the sparse T-cell infiltrate of the immunologically cold glioblastoma.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the vascular permeability of the glioblastoma microenvironment.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the microglial (already mapped) and myeloid inflammation of the glioblastoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the glioblastoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack in the immunologically cold tumour.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the proliferating glioblastoma cells and the disordered brain-iron handling of the tumour.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-GBM axis: TSLP, from the glioblastoma stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of the EGFR-amplified (already mapped) glioblastoma tumour niche.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-GBM axis: bradykinin, via B1/B2 receptors on glioblastoma endothelium (already mapped) and microglia (already mapped), augments blood-brain-barrier permeability, tumour oedema, and the pro-inflammatory milieu of the glioblastoma microenvironment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-GBM axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia of the glioblastoma core, activates the EPOR on tumour cells (already mapped) and modulates microglia/macrophage (already mapped) polarisation toward a pro-tumour M2 phenotype.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-GBM axis: histamine, released by microglia (already mapped) and mast cells in the glioblastoma microenvironment, signals via H1/H2 receptors on tumour cells and endothelium (already mapped), modulating blood-brain-barrier permeability and immunosuppressive milieu.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-GBM axis: melatonin, crossing the blood-brain barrier, suppresses EGFR (already mapped) and HIF-1α (already mapped) signalling in glioblastoma cells, modulates the circadian immune clock, and enhances sensitivity to temozolomide chemotherapy.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement regulation-GBM axis: the C1-esterase inhibitor limits classical and contact-pathway complement activation in the glioblastoma microenvironment (complement C3/C5/C5aR1 already mapped), modulating the neuroinflammatory and tumour milieu.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — GBM prolactin: prolactin, via PRLR on microglia (already mapped) and macrophages (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of glioblastoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — GBM oxytocin: oxytocin, via OXTR on microglia (already mapped) and macrophages (already mapped), attenuates neuroinflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of glioblastoma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — GBM vasopressin: vasopressin, via V1aR on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of glioblastoma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — GBM testosterone: testosterone, via AR on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; testosterone deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) glioblastoma cascade.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — GBM selenium: selenium, as GPx in microglia (already mapped) and macrophages (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative T-cytotoxic (already mapped) cascade of glioblastoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — GBM iodine: iodine-dependent thyroid hormones modulate microglia (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of glioblastoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — GBM sodium: sodium-driven osmotic stress on glioma cells and microglia (already mapped) amplifies NF-κB (already mapped) and VEGF (already mapped) tumour-proliferative signalling; sodium excess worsens the IL-6 (already mapped) neuroinflammatory TME of glioblastoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — GBM copper: copper, via ceruloplasmin and SOD in microglia (already mapped) and macrophages (already mapped), scavenges ROS; copper excess amplifies NF-κB (already mapped) and VEGF (already mapped) and mTOR (already mapped) glioblastoma tumour growth and neovascularisation.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — GBM zinc: zinc, via SOD and NF-κB (already mapped) modulation in microglia (already mapped) and T-cytotoxic cells (already mapped), attenuates tumour neuroinflammation; zinc deficiency amplifies VEGF (already mapped) and IL-6 (already mapped) glioblastoma cascade.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — GBM phosphorus: phosphorus, as ATP in microglia (already mapped) and macrophages (already mapped), fuels neuroinflammatory signalling; phosphorus excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) glioblastoma tumour growth cascade.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — GBM chloride: chloride channels on microglia (already mapped) and macrophages (already mapped) regulate volume-regulated apoptosis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade of glioblastoma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — GBM nitrogen: nitric oxide from iNOS in microglia (already mapped) and macrophages (already mapped) modulates tumour immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of glioblastoma.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — GBM carbon: carbon in nucleotides of microglia (already mapped) and macrophages (already mapped) fuels glioblastoma proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade of glioblastoma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — GBM hydrogen: hydrogen via ROS from microglia (already mapped) and macrophages (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) glioblastoma cascade of glioblastoma.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — GBM sulfur: sulfur-containing amino acids in microglia (already mapped) and macrophages (already mapped) regulate redox signalling; sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade of glioblastoma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — glioblastoma glp-1: GLP-1 from microglia (already mapped) and astrocytes (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies EGFR (already mapped) and VEGF (already mapped) and mTOR (already mapped) cascade of glioblastoma.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — glioblastoma angiotensin-ii: angiotensin II on endothelial cells (already mapped) and glioma cells (already mapped) promotes angiogenesis; angiotensin-II excess amplifies EGFR (already mapped) and VEGF (already mapped) and mTOR (already mapped) cascade of glioblastoma.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — glioblastoma rankl: RANKL from microglia (already mapped) and tumour cells (already mapped) modulates neuro-inflammation; rankl excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — glioblastoma fibronectin: fibronectin in microglia (already mapped) and tumour cells (already mapped) promotes invasive ECM remodelling; fibronectin excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — glioblastoma igf-1: IGF-1 from microglia (already mapped) and tumour cells (already mapped) promotes glioma proliferation; igf-1 excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — glioblastoma activin-a: activin-A from microglia (already mapped) and tumour cells (already mapped) promotes glioma invasion; activin-a excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — glioblastoma cgrp: CGRP from microglia (already mapped) and tumour cells (already mapped) modulates glioma neuroimmune tone; cgrp excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — glioblastoma calcitonin: calcitonin from microglia (already mapped) and tumour cells (already mapped) modulates glioma calcium balance; calcitonin dysregulation amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — glioblastoma substance-p: substance-P from microglia (already mapped) and tumour cells (already mapped) modulates glioma pain tone; substance-P excess amplifies EGFR (already mapped) and NF-κB (already mapped) and VEGF (already mapped) cascade of glioblastoma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stupp-2005-temozolomide]: Stupp R, Mason WP, van den Bent MJ, et al. Radiotherapy plus concomitant and adjuvant temozolomide for glioblastoma. *N Engl J Med.* 2005;352(10):987-996. [doi:10.1056/NEJMoa043330](https://doi.org/10.1056/NEJMoa043330) · [PubMed 15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/)
[^chinot-2014-bevacizumab]: Chinot OL, Wick W, Mason W, et al. Bevacizumab plus radiotherapy-temozolomide for newly diagnosed glioblastoma. *N Engl J Med.* 2014;370(8):709-722. [doi:10.1056/NEJMoa1308345](https://doi.org/10.1056/NEJMoa1308345) · [PubMed 24552318](https://pubmed.ncbi.nlm.nih.gov/24552318/)
