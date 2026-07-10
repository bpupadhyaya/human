---
schema: human-scale-entry/v1
id: medulloblastoma
name: Medulloblastoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Medulloblastoma is the most common pediatric brain tumor; 4 molecular subgroups: WNT (~10%, OS ~95%), SHH (~38%), Group 3 (~25%, MYC-amplified, worst prognosis), Group 4 (~35%); surgery + CSI + chemotherapy; SHH MB responsive to SMO inhibitors; infant MB: chemo without radiation."
aliases: ["medulloblastoma", "MB", "pediatric medulloblastoma", "SHH medulloblastoma", "WNT medulloblastoma", "Group 3 medulloblastoma", "cerebellar medulloblastoma", "MBEN"]
sources:
  - id: packer-2006-std-risk-mb
    type: peer-reviewed
    cite: "Packer RJ, Gajjar A, Vezina G, et al. Phase III study of craniospinal radiation therapy followed by adjuvant chemotherapy for newly diagnosed average-risk medulloblastoma. J Clin Oncol. 2006;24(25):4202-4208."
    doi: "10.1200/JCO.2006.06.4980"
    pmid: "16943538"
    url: "https://doi.org/10.1200/JCO.2006.06.4980"
  - id: taylor-2012-mb-subgroups
    type: peer-reviewed
    cite: "Taylor MD, Northcott PA, Korshunov A, et al. Molecular subgroups of medulloblastoma: the current consensus. Acta Neuropathol. 2012;123(4):465-472."
    doi: "10.1007/s00401-011-0922-z"
    pmid: "22134537"
    url: "https://doi.org/10.1007/s00401-011-0922-z"
cross_links:
  - target: 01-human/03-molecular/ptch1
    relation: connects-to
    note: "PTCH1/SMO/SUFU/GLI2 mutations define SHH-activated MB (~38%); germline PTCH1 → Gorlin syndrome + infant/adult SHH-MB; SHH-MB in adults is the primary indication for vismodegib in MB trials; desmoplastic/nodular histology is the hallmark of SHH-MB with PTCH1 LOF."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC amplification (~17%) defines the most aggressive Group 3 MB (5-year OS ~45%); MYCN amplification in SHH-MB + TP53 mutation = highest-risk SHH-MB; MYC drives extreme proliferative rate; BET inhibitors suppress MYC in Group 3/4 MB preclinically."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "WNT-activated MB (~10%) carries CTNNB1 activating mutations + monosomy 6 + nuclear β-catenin; WNT-MB has near-universal cure (5-year OS ~95%); de-escalation trials (reduced CSI 18 Gy) ongoing; CTNNB1 mutations are absent in SHH/Group 3/Group 4 MB."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "SHH-activated/TP53-mutant MB: MYCN amplification + TP53 mutation → 5-year OS ~40%; TP53 mutations are germline in Li-Fraumeni syndrome → elevated MB risk; Group 3 MYC-amplified MB acquires TP53 at relapse; p53 IHC (>10% nuclear) is a surrogate marker in MB."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Medulloblastoma is the most common pediatric brain tumor, arising in the cerebellum (posterior fossa) where it obstructs the 4th ventricle → hydrocephalus; maximal safe resection risks cerebellar mutism syndrome, and craniospinal irradiation drives neurocognitive late effects."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "Gorlin syndrome (germline PTCH1 loss) predisposes to SHH-activated medulloblastoma, typically the desmoplastic/nodular infant form; because these children are radiation-hypersensitive (PTCH1 carriers get RT-field basal cell carcinomas), radiation-sparing strategies are favored."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Germline TP53 (Li-Fraumeni) defines the SHH-activated/TP53-mutant subgroup — often MYCN-amplified, large-cell/anaplastic, ~40% 5-year OS; TP53 germline testing is mandatory for all SHH-MB aged 3-17, and craniospinal irradiation is avoided given LFS radiation sensitivity."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Medulloblastoma and IDH-mutant glioma are both molecularly classified brain tumors but opposite poles: medulloblastoma is a fast embryonal cerebellar tumor of children (SHH/WNT/MYC), while IDH-mutant glioma is a slow diffuse hemispheric tumor of adults driven by 2-HG epigenetics."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Atypical teratoid/rhabdoid tumor is the key infant mimic of medulloblastoma: both are small-round-blue-cell posterior-fossa tumors, but ATRT is defined by SMARCB1 (INI1) loss and far more aggressive — INI1 immunostaining (kept in MB, lost in ATRT) distinguishes them."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "SHH-activated medulloblastoma arises from cerebellar granule neuron precursors of the external granular layer, whose normal proliferation depends on Sonic hedgehog from Purkinje neurons; a PTCH1/SMO lesion locks this hedgehog program on, driving the desmoplastic/nodular tumor."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Craniospinal radiotherapy is central to medulloblastoma treatment: because the tumor seeds the CSF and drops spinal metastases, photon or proton irradiation of the whole brain and spinal axis follows surgery—curative for many but neurocognitively toxic in children."
  - target: 01-human/07-system/dicer1-syndrome
    relation: connects-to
    note: "Medulloblastoma is part of several cancer-predisposition syndromes: germline DICER1 loss can produce a medulloblastoma-like embryonal CNS tumor, as Gorlin (PTCH1) drives SHH-subtype and Li-Fraumeni (TP53) high-risk disease—so syndromic testing is warranted."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "Medulloblastoma and diffuse midline glioma are the major malignant pediatric brain tumors but differ: medulloblastoma is a resectable cerebellar tumor often cured by surgery plus craniospinal radiotherapy, while DMG is an unresectable, fatal H3 K27M brainstem glioma."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "Medulloblastoma links to FAP through Turcot syndrome: germline APC loss that drives colonic polyposis also activates Wnt/β-catenin in the cerebellum, producing WNT-subgroup medulloblastoma—the same pathway connecting a gut cancer syndrome to a brain tumor."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Medulloblastoma and neuroblastoma are both embryonal childhood tumors that look alike as 'small round blue cells' but differ in origin: medulloblastoma from cerebellar progenitors, neuroblastoma from peripheral sympathetic neuroblasts—CNS versus sympathetic chain."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Medulloblastoma and rhabdomyosarcoma are both small-round-blue-cell embryonal tumors told apart by immunohistochemistry: medulloblastoma expresses neuronal markers (synaptophysin), rhabdomyosarcoma skeletal-muscle markers (desmin, myogenin)—same look, different lineage."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "SHH-subtype medulloblastoma is driven by Smoothened: PTCH1 loss or SMO activation unleashes hedgehog signaling, defining one of the four molecular groups, and SMO inhibitors like vismodegib target it—though resistance and growth-plate toxicity limit use in children."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "MYCN amplification marks high-risk medulloblastoma: in Group 3 and 4 tumors, amplified MYC/MYCN drives aggressive proliferation and poor prognosis, so molecular subgrouping—not just histology—now guides how intensively each child's tumor is treated."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Medulloblastoma can spread beyond the CNS to bone marrow: though it usually disseminates through cerebrospinal fluid along the neuraxis, this embryonal tumor occasionally metastasizes to bone and marrow—rare among brain tumors and a sign of aggressive disease."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy is standard for pediatric medulloblastoma's craniospinal radiation: because children need the whole brain and spine irradiated, protons' lack of exit dose spares the heart, lungs and gut, cutting the lifelong toxicity of treating this childhood brain tumor."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Medulloblastoma is the commonest malignant brain tumor of childhood, arising in the cerebellum: it disrupts balance and blocks CSF flow (hydrocephalus), and it seeds along the nervous system's CSF pathways—why staging and radiation cover the whole neuraxis."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Medulloblastoma arises from cerebellar progenitors, distinct from astrocyte-derived gliomas: it is an embryonal small-round-blue-cell tumor of granule-cell precursors, so its biology and treatment differ fundamentally from the astrocytic and oligodendroglial gliomas."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Some medulloblastomas reactivate telomerase via TERT: promoter mutations switch TERT back on, especially in adult SHH-subgroup tumors, letting cells divide indefinitely—a molecular marker that helps subgroup and risk-stratify these embryonal brain cancers."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Medulloblastoma and retinoblastoma are both embryonal childhood cancers: each arises from immature precursor cells—cerebellar in one, retinal in the other—and both can seed the cerebrospinal fluid, a parallel between developing neural tissues turning malignant."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Medulloblastomas recruit brain microglia into their microenvironment: these tumor-associated immune cells can be co-opted to support growth and shape the response to therapy, making the cerebellar tumor's immune niche a focus of new treatment ideas."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Medulloblastoma's WNT subgroup has a leaky, VEGF-rich vasculature: its abnormal fenestrated blood vessels let chemotherapy reach the tumor better, helping explain why WNT medulloblastoma has the best prognosis of the four subgroups."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Medulloblastoma resists immunotherapy partly through regulatory T cells: the tumor's immunosuppressive microenvironment and the brain's immune privilege blunt T-cell attack, so Tregs are among the barriers checkpoint therapy must overcome here."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Curing medulloblastoma can injure oligodendrocytes: the craniospinal radiation that controls it damages these myelinating cells, causing white-matter loss and the neurocognitive decline that shadows childhood survivors."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Medulloblastoma springs from the cerebellum's wiring: it arises from neural precursors that should build cerebellar circuits, and like other brain tumors it can integrate with neurons at synapses, tying the cerebellum's developmental program to the cancer."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Medulloblastoma is largely cold to cytotoxic T cells: with few mutations and a protected brain site, it resists immune attack, so engineered T-cell and other immunotherapies are being developed to reach a tumor that checkpoint drugs miss."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Group 3 medulloblastoma leans on the cell-cycle kinase CDK4/6: MYC-driven proliferation depends on it, so CDK4/6 inhibitors are studied to slow the most aggressive subtype where current therapy often fails."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Medulloblastoma outpaces its oxygen: the fast-growing cerebellar tumor turns hypoxic in its core, switching on VEGF-driven angiogenesis to build the blood supply it needs to keep expanding."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Medulloblastoma shows up in the eyes: by blocking CSF flow it raises intracranial pressure, swelling the optic discs (papilledema) and blurring vision, often among the first signs of the cerebellar tumor."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Medulloblastoma sits in a macrophage-rich niche: tumor-associated macrophages and microglia populate the microenvironment, especially in SHH-subtype tumors, shaping growth and immune evasion."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Medulloblastoma seeds the spinal canal: 'drop metastases' coat the cord and the nerve roots of the cauda equina via the CSF, which is why the whole neuraxis is irradiated, not just the tumor."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Some medulloblastomas calcify: flecks of calcium appear on CT, and the desmoplastic subtype in particular can show calcification within the cerebellar mass."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Medulloblastoma rarely escapes the nervous system: extraneural metastases to bone, marrow, liver and lung can occur, an unusual spread for a brain tumor that shifts the prognosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals medulloblastoma's neuroblastic roots: its small round blue cells ring up into Homer Wright rosettes around tangles of neuritic processes, the ultrastructure of a primitive tumor trying to form neurons."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "When medulloblastoma leaves the brain, the lung is a target: among its rare extraneural metastases — to bone, marrow, and liver — the lungs can be seeded, sometimes via a ventriculoperitoneal shunt."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Shunt-borne medulloblastoma can reach the abdomen: cells draining through a ventriculoperitoneal shunt seed the peritoneum and abdominal organs, an unusual route by which this brain tumor spreads beyond the skull."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains sort the subgroups: immunohistochemistry for nuclear beta-catenin marks the WNT tumors and GAB1/YAP1 the SHH ones, dividing medulloblastoma into the molecular groups that now drive prognosis and how intensely each child is treated."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The cure costs the marrow: craniospinal radiation irradiates a vast volume of blood-forming bone and the accompanying chemotherapy is myelosuppressive, so neutrophil counts fall and febrile neutropenia is a constant hazard during treatment."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Cisplatin in the regimen wastes magnesium: the platinum chemotherapy used against medulloblastoma injures the kidney tubule that reclaims magnesium, so blood levels drop and need replacing alongside watching for the drug's hearing loss."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Curing the brain stunts the body: craniospinal radiation damages the pituitary's growth-hormone output and the spine's own growth plates, so survivors fall off the height curve — growth-hormone deficiency is among the commonest late effects of treatment."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment reaches the reproductive axis: radiation to the brain disturbs the hormones timing puberty while alkylating chemotherapy damages the gonads, so survivors face precocious or delayed puberty and impaired fertility, prompting preservation counseling."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The intensive chemotherapy empties the marrow: the multi-drug regimens for medulloblastoma suppress platelet production into thrombocytopenia, so bleeding risk and transfusion needs are watched through the long months of treatment."
  - target: 01-human/03-molecular/sufu
    relation: connects-to
    note: "A brake on the Hedgehog pathway, when lost, drives one subgroup: SUFU normally restrains SHH signaling, so germline or somatic SUFU loss unleashes the pathway to produce SHH-type medulloblastoma — a target for the same Hedgehog inhibitors aimed at SMO and PTCH1."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Cure comes at a hormonal price: craniospinal radiation and surgery near the hypothalamus and pituitary leave survivors with growth-hormone deficiency, thyroid and adrenal shortfalls and delayed puberty, so lifelong endocrine follow-up is part of survivorship."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "The treatment can seed a second tumor: the cranial radiation that cures medulloblastoma is itself a leading cause of radiation-induced meningiomas decades later, one of the secondary cancers that shadow long-term survivors."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle brakes fail in the aggressive subtypes: CDKN2A loss and the resulting CDK4/6 overactivity drive proliferation in MYC-amplified medulloblastomas, marking poor-prognosis tumors and a rationale for CDK4/6 inhibitors."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Radiation scars the brain's arteries: craniospinal irradiation causes a late cerebral vasculopathy — including moyamoya around the circle of Willis — that raises stroke risk in childhood medulloblastoma survivors."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Intensive therapy strips the defenses: the myelosuppressive chemotherapy used against medulloblastoma produces neutropenia, so febrile neutropenia and sepsis are among the acute treatment hazards."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 supports the aggressive subgroups: Group 3 and SHH medulloblastomas show STAT3 activation that backs proliferation and survival, a pathway studied for the high-risk, MYC-driven tumors that resist standard therapy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB adds a survival signal: medulloblastoma cells engage NF-κB-dependent survival and inflammatory signaling, one of the cooperating pathways alongside the SHH, WNT and MYC programs that define its subgroups."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A brain tumor that clots: like other CNS malignancies, medulloblastoma raises venous thromboembolism risk through tumor tissue factor and the immobility of major posterior-fossa surgery and illness."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Intensive chemo strips the lung's defenses: the dose-dense, often high-dose chemotherapy for medulloblastoma causes profound neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its platinum chemo scars young kidneys: cisplatin central to medulloblastoma regimens is nephrotoxic and ototoxic, and in a child the tubular injury and electrolyte wasting can leave lasting chronic kidney impairment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Craniospinal radiation leaves lasting scars on the mind: medulloblastoma survivors face neurocognitive decline, endocrine failure and the trauma of childhood cancer, carrying a heavy burden of depression."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Vincristine and tumor injure the nerves: the vincristine central to medulloblastoma chemotherapy causes peripheral neuropathy, and posterior-fossa disease adds neurological pain in survivors."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Radiation and steroids disturb glucose: craniospinal radiation damages the hypothalamic-pituitary axis and the dexamethasone for edema induces insulin resistance, predisposing survivors to diabetes."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Posterior-fossa surgery and steroids hinder repair: the craniotomy for medulloblastoma risks CSF leak and poor wound healing, worsened by the chronic dexamethasone used to control edema."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Posterior-fossa damage and treatment hit the gut: brainstem and cerebellar involvement causes dysphagia and aspiration, and craniospinal radiation plus chemotherapy bring mucositis and nausea."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Chemotherapy reawakens shingles: the chemotherapy for medulloblastoma suppresses a child's immunity, allowing latent or primary varicella-zoster to cause severe disseminated infection."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A childhood brain cancer with long survivorship breeds worry: the intensive therapy, neurocognitive late effects and relapse surveillance of medulloblastoma foster chronic anxiety in survivors and families."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Spinal radiation stunts the growing skeleton: craniospinal radiotherapy impairs vertebral growth, leaving survivors with short stature, reduced sitting height and scoliosis — a hallmark late effect."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Posterior-fossa surgery threatens swallowing and breath: cerebellar mutism syndrome with dysphagia raises aspiration risk, and brainstem involvement can compromise respiratory control."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Radiation marks the scalp and skin: craniospinal radiotherapy causes dermatitis and permanent alopecia in the treated field, alongside the skin effects of chemotherapy."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its cure costs the heart later: anthracycline and platinum chemotherapy plus radiation in childhood medulloblastoma carry long-term cardiovascular and cardiotoxic risk in survivors."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Cisplatin threatens the kidney: the platinum chemotherapy central to medulloblastoma treatment is nephrotoxic and ototoxic, demanding careful dosing in children."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Therapy suppresses immunity: intensive craniospinal radiation and chemotherapy leave children profoundly immunocompromised, while WNT and SHH subtypes are explored for targeted and immune therapy."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo joins surgery and radiation: multi-agent chemotherapy with vincristine, cisplatin and cyclophosphamide or CCNU, given with craniospinal radiation, cures most standard-risk medulloblastoma."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Hedgehog inhibitors for one subgroup: vismodegib and sonidegib block SMO in the SHH-activated subgroup of medulloblastoma driven by PTCH1, SMO or SUFU mutations."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Craniospinal radiation stunts the skeleton: irradiating the whole spine in young children impairs vertebral and long-bone growth, causing short stature and spinal deformity among the late effects of cure."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The cure costs memory: craniospinal radiation and the cranial boost damage the hippocampus, impairing the formation of new memories and lowering IQ in childhood medulloblastoma survivors, which drives efforts to spare the hippocampus during radiotherapy."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Two small-round-blue-cell tumours of childhood: medulloblastoma and Ewing sarcoma are both densely cellular embryonal-type cancers of the young but differ at the root—Ewing is driven by an EWSR1-FLI1 fusion, medulloblastoma by SHH, WNT or MYC programmes."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold tumour: medulloblastoma has a low mutational burden and sparse immune infiltrate, so PD-1 checkpoint inhibitors have shown little benefit, and immunotherapy effort has shifted toward CAR-T against B7-H3 and GD2."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "SHH-pathway tumours: SHH-subgroup medulloblastoma and basal cell carcinoma share aberrant Sonic-hedgehog signalling—both arise in Gorlin syndrome—and respond to SMO inhibitors like vismodegib."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Rare extraneural metastasis: although it usually spreads through the CSF, medulloblastoma can disseminate outside the nervous system to bone, marrow and the liver, seeding the hepatic lobule."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Survivorship cardiotoxicity: the anthracycline chemotherapy and incidental cardiac radiation used to cure medulloblastoma injure the myocardium, a late effect monitored for decades in survivors."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Radiation through the neck: the craniospinal radiotherapy that cures medulloblastoma irradiates the thyroid in its exit path, causing hypothyroidism and a raised long-term risk of thyroid cancer in survivors."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Therapy-related leukaemia: the alkylating agents and topoisomerase inhibitors used against medulloblastoma damage haematopoietic stem cells, occasionally causing a secondary myelodysplasia or acute myeloid leukaemia years later."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Stunted growth after cure: radiation to the hypothalamic-pituitary axis blunts growth-hormone and IGF-1 signalling, making growth failure and short stature among the most common endocrine late effects in medulloblastoma survivors."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Stem-cell maintenance: Notch signalling sustains medulloblastoma stem-like cells, especially in Group 3/4 tumours, a candidate therapeutic target for these aggressive subgroups."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dependence: EZH2-driven histone methylation enforces the proliferative programme of Group 3/4 medulloblastoma, an actionable epigenetic vulnerability."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "SHH-driven cell cycle: Hedgehog signalling upregulates cyclin D1, partnering CDK4/6 to push SHH-subgroup medulloblastoma cells through the cell cycle."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: PI3K/AKT signalling supports medulloblastoma cell survival and is implicated in resistance to Hedgehog-pathway inhibitors in the SHH subgroup."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth-signal hub: mTOR integrates the growth-factor signalling of medulloblastoma, driving the protein synthesis and proliferation of these embryonal tumours."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the hypoxic medulloblastoma drives the VEGF angiogenesis and metabolic adaptation that support its rapid growth."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptotic chemosensitivity: high MYC in Group 3 medulloblastoma primes cells for caspase-3-mediated apoptosis, part of why these embryonal tumours respond initially to cytotoxic chemotherapy and radiation."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Microglial microenvironment: CCL2 recruits microglia and macrophages into the medulloblastoma microenvironment, shaping the immunosuppressive niche of this childhood cerebellar tumour."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK proliferation: RAS-RAF-ERK signalling contributes to medulloblastoma proliferation, cooperating with the SHH, WNT and MYC programmes that define its molecular subgroups."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "WNT subgroup driver: activating CTNNB1 (β-catenin) mutations define the WNT subgroup of medulloblastoma, the best-prognosis molecular subgroup with cure rates above 90% in children."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Leptomeningeal dissemination: CXCR4 on medulloblastoma cells follows CXCL12 gradients to seed the cerebrospinal fluid, the leptomeningeal spread that mandates craniospinal irradiation in all but the lowest-risk cases."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Radioresistance: RAD51-mediated homologous-recombination repair helps high-risk medulloblastomas survive radiation-induced DNA damage, a mechanism of the radioresistance that limits cure in the aggressive Group 3 and TP53-mutant SHH tumours."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Methylation classification: medulloblastoma is now defined by its DNA-methylation profile, which separates the WNT, SHH, Group 3 and Group 4 subgroups with their different biology, prognosis and therapy — making the methylome the basis of modern diagnosis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "GD2 immunotherapy: Group 3 medulloblastomas express GD2, and GD2-directed CAR-T cells aim to kill them through perforin and granzyme, an emerging immunotherapy for the highest-risk subgroup that responds poorly to standard treatment."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Granule-precursor origin: SHH-subgroup medulloblastoma arises from cerebellar granule-neuron precursors, whose normal proliferation and differentiation are shaped by neurotrophin-Trk signalling, the developmental context the tumour hijacks."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K growth signal: PIK3CA activates the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) across medulloblastoma subgroups, contributing to growth and to resistance to SHH-pathway inhibitors."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle engine: the cyclin-D-CDK4/6 axis (mapped) releases E2F1 to drive S-phase entry, the proliferative output amplified by the MYC and MYCN (both mapped) of high-risk medulloblastoma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Group 3 driver: TGF-β pathway signalling is a recurrent driver of the aggressive Group 3 medulloblastoma, cooperating with MYC amplification in this poor-prognosis subgroup."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle drive: deregulation of the RB1-E2F checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) drives the proliferation of medulloblastoma, particularly the aggressive MYC-amplified subgroups."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferation: RAS-MAPK signalling (ERK1/2 already mapped) provides a proliferative input cooperating with the subgroup-defining drivers of medulloblastoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 inactivation: MDM2-mediated p53 inactivation (p53 already mapped) contributes to the poor prognosis of TP53-altered SHH medulloblastoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates the invasion and immune microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT3 signalling (STAT3 mapped) provides a proliferative and immunomodulatory input across medulloblastoma subgroups."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) contributes to the biology of Group 3/4 medulloblastoma and shapes its tumour microenvironment."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immunologically cold microenvironment of medulloblastoma, a barrier to its immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment and radiation response of medulloblastoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the cerebellar-progenitor proliferation and survival programmes hijacked by medulloblastoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β regulates GLI and β-catenin stability (SHH/SMO and WNT-β-catenin already mapped), modulating the subtype-defining signaling of medulloblastoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the tumor microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling contributes to the migratory and leptomeningeal-metastatic behavior of medulloblastoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of medulloblastoma cells."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF and the broader chromatin machinery contribute to the epigenetically driven subgroups of medulloblastoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of medulloblastoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of medulloblastoma."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "YAP1-Hippo signaling participates in the proliferation of the granule-neuron-precursor-derived cells of SHH medulloblastoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and tumor-immune microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammatory tumor microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the tumor microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of medulloblastoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin (SPP1) participates in the microglial/macrophage tumor microenvironment and metastatic dissemination of medulloblastoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunotherapy: medulloblastoma is largely immunologically cold, and MHC-based antigen presentation is central to the vaccine and cellular immunotherapy strategies being explored, particularly for the high-risk Group 3 subtype (MYC already mapped)."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cellular immunotherapy: IL-2-driven T-cell expansion supports the CAR-T and adoptive approaches under investigation for medulloblastoma, aiming to reach the tumour cells that seed the cerebrospinal fluid (perforin already mapped)."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint context: PD-1 checkpoint blockade has limited single-agent activity in the cold medulloblastoma microenvironment, motivating combinations with radiation and targeted therapy to render it immunoresponsive."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Chemotherapy anaemia: the intensive multidrug chemotherapy that, with craniospinal radiation, treats medulloblastoma is myelosuppressive, lowering haemoglobin and requiring transfusion support in these young patients."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac late effect: the craniospinal radiation for medulloblastoma exposes the heart, and any anthracycline adds cardiotoxicity, with troponin elevation marking the myocardial injury that threatens the many long-term survivors."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 helps make medulloblastoma an immunologically cold tumour (PD-1 already mapped), dampening the T-cell response that the CAR-T and checkpoint strategies under investigation aim to mount."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Hedgehog-lipid link: cholesterol and its oxysterol derivatives activate Smoothened (already mapped), the driver of the Hedgehog pathway (PTCH1 already mapped) in the SHH subtype of medulloblastoma, linking cellular lipid handling to the oncogenic signalling."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 microglial polarisation: IL-4 polarises the tumour-associated microglia and macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immunologically cold microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6 and IL-1 already mapped) of the medulloblastoma microenvironment."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 microglial (already mapped) niche of the immunologically cold microenvironment of medulloblastoma."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "WNT fenestrated vasculature: the WNT-subgroup medulloblastoma has an aberrant, fenestrated tumour endothelium with a leaky blood-tumour barrier (VEGF already mapped), letting in chemotherapy and helping explain its excellent prognosis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the intensive multi-agent chemotherapy of medulloblastoma is myelosuppressive, causing anaemia (haemoglobin already mapped) needing transfusion that can load the young child with iron."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Hypothalamic obesity: the craniospinal radiation damages the hypothalamic-pituitary (growth hormone already mapped) axis, causing the hypothalamic obesity and leptin dysregulation of the medulloblastoma survivor."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Survivorship metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-endocrine late effects of medulloblastoma survivorship."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic-syndrome adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the metabolic syndrome that complicates the long-term survival of medulloblastoma."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the anthracycline chemotherapy of the medulloblastoma regimens causes the cardiotoxicity (troponin already mapped) of the heart, a survivorship concern in the childhood survivor."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of medulloblastoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the immunologically cold medulloblastoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the medulloblastoma microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of medulloblastoma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of medulloblastoma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of medulloblastoma."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral arm: the plasma cells secrete the antibodies (already mapped) of the humoral response within the immune microenvironment of medulloblastoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the sparse immune infiltrate of the immunologically cold medulloblastoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of medulloblastoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) and myeloid activation of the medulloblastoma microenvironment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Craniospinal RT anaemia: erythropoietin counters the radiation-induced myelosuppression from the craniospinal irradiation used in medulloblastoma; EPO-stimulating agents are a standard supportive measure during and after the CSI phase of medulloblastoma treatment."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement-mediated lysis: the complement C5 effector (with complement C3 already mapped) participates in complement-dependent cytotoxicity against medulloblastoma cells; anti-C5 signalling modulates the immune-infiltration pattern of the immunogenic WNT-subgroup medulloblastoma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "BBB drug delivery: bradykinin (B2 receptor) transiently increases blood-brain barrier permeability, a mechanism exploited to enhance chemotherapy (already mapped) delivery to posterior-fossa medulloblastoma and reduce reliance on high-dose craniospinal irradiation."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Tumour-immune alarmin: TSLP released by the medulloblastoma stroma primes dendritic cells (already mapped) and mast cells (already mapped) toward the Th2 (IL-4, IL-13 already mapped) immune microenvironment of the WNT (wnt-beta-catenin already mapped) subgroup."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) in the medulloblastoma microenvironment, modulating complement-dependent cytotoxicity and the tumour-associated macrophage (already mapped) response."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell histamine in MB microenvironment: histamine, released by the mast cells (already mapped) of the medulloblastoma stroma, modulates microvascular permeability and promotes the VEGF-driven (already mapped) angiogenesis and immunomodulation of medulloblastoma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian antitumour melatonin: melatonin, via MT1/MT2 receptors on medulloblastoma cells and the cerebellar tumour vasculature (already mapped), suppresses SHH-pathway (already mapped) proliferation and VEGF-driven (already mapped) angiogenesis in paediatric medulloblastoma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-SHH axis: testosterone, via androgen receptor on SHH-subgroup (already mapped) medulloblastoma cells, modulates the hedgehog proliferative pathway (already mapped) and the sex-dimorphic vulnerability to medulloblastoma in the paediatric posterior fossa."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Cerebellar neuromodulator: serotonin, via 5-HT3 receptors on cerebellar granule cells (already mapped), modulates the neuronal signalling of the medulloblastoma microenvironment; 5-HT3-driven nausea from craniospinal radiation (already mapped) is a major treatment morbidity."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Medulloblastoma prolactin neuro-immune: prolactin, via PRLR on tumour-associated macrophages (already mapped) and mast cells (already mapped), upregulates NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in the paediatric medulloblastoma microenvironment."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Medulloblastoma oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in the medulloblastoma cerebellar microenvironment."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Medulloblastoma vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the tumour vascular niche; dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in medulloblastoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "MB selenium: selenium, as GPx in microglia (already mapped) and macrophages (already mapped), scavenges ROS in the tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of medulloblastoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MB iodine: iodine-dependent thyroid hormones modulate microglia (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of medulloblastoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "MB sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of medulloblastoma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "MB copper: copper, via SOD1 in macrophages (already mapped) and microglia (already mapped), scavenges tumour ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of medulloblastoma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "MB zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and microglia (already mapped), attenuates brain tumour oxidative stress; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of medulloblastoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "MB potassium: potassium regulates macrophage (already mapped) and T-cytotoxic cell (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour cascade of medulloblastoma."
---

# Medulloblastoma

## Overview

**Medulloblastoma (MB)** is the most common malignant **pediatric brain tumor**, comprising ~20% of all pediatric CNS tumors and ~40% of pediatric posterior fossa tumors. MB arises in the cerebellum from aberrant progenitor cell proliferation and is classified into **four molecular subgroups** by the WHO (2021) — WNT-activated, SHH-activated, and non-WNT/non-SHH (Group 3 and Group 4) — with profoundly different biological mechanisms, treatment responses, and prognoses [^taylor-2012-mb-subgroups]. Modern treatment for standard-risk MB involves maximal surgical resection followed by **craniospinal irradiation (CSI) and adjuvant chemotherapy** (vincristine+CCNU+cisplatin × 8 cycles), achieving 5-year event-free survival (EFS) of ~81% in standard-risk disease [^packer-2006-std-risk-mb]; high-risk MB requires escalated CSI (36 Gy) and intensified chemotherapy. Key challenges include: (1) devastating neurocognitive late effects of irradiation (IQ loss, endocrinopathy, secondary tumors); (2) extreme heterogeneity in prognosis across subgroups (WNT-MB OS ~95% vs Group 3 MYC-amplified OS ~45%); and (3) lack of approved targeted therapies beyond SMO inhibitors for SHH-MB.

**Epidemiology:**
- ~500-600 cases/year in the USA; ~15,000-20,000/year globally
- Median age at diagnosis: 6-7 years; peak 3-9 years; bimodal distribution with adult peak 25-40 years
- Male predominance 2:1 for Group 3/4; female predominance for WNT-MB
- Almost universal cerebellar location; ~5-10% spinal seeding at diagnosis; ~20-30% metastatic disease overall (M+)

## Structure

### WHO 2021 molecular subgroups

**1. WNT-activated MB (~10%):**
- **Molecular:** CTNNB1 (β-catenin) activating mutations (~85%); SMARCA4 mutations (~20%); monosomy 6 (pathognomonic); isochromosome 17q absent; nuclear β-catenin by IHC confirms WNT activation
- **Histology:** Classic MB (most); large cell/anaplastic extremely rare
- **Demographics:** Peak age 10-15 years; adults; male = female
- **Prognosis:** 5-year OS ~95% — best of all subgroups; highly curable; near-zero mortality with standard therapy in classic WNT-MB; de-escalation is the major research priority
- **Cell of origin:** Dorsal brainstem progenitors (lower rhombic lip near 4th ventricle roof)

**2. SHH-activated/TP53-wildtype MB (~28%):**
- **Molecular:** PTCH1 LOF (~55%), SUFU LOF (~10%), SMO GOF (~5%), GLI2 amplification (~10%); TERT promoter mutations (~80% of adult SHH-MB); 9q loss
- **Histology:** Desmoplastic/nodular (infants — excellent prognosis), medulloblastoma with extensive nodularity (MBEN, infants — best prognosis), classic
- **Demographics:** Infants (<3 years) and adults (>17 years); bimodal; rare in 3-17-year age range
- **Prognosis:** Highly variable — infants with MBEN: 5-year OS ~90-100%; infants with SHH non-MBEN: ~70-80%; adults: ~75-80%; worse with MYCN amplification
- **Cell of origin:** Cerebellar granule cell progenitors (GCPs) in external granule layer

**3. SHH-activated/TP53-mutant MB (~10%):**
- **Molecular:** MYCN amplification (~50%); TP53 mutations (~100% by definition); GLI2 amplification; predominantly germline TP53 in ~50% (Li-Fraumeni syndrome)
- **Histology:** Large cell/anaplastic predominantly
- **Demographics:** Children 3-17 years; male predominance
- **Prognosis:** 5-year OS ~40-60% — worst SHH subgroup; high-risk treatment regardless of M-staging
- **Significance:** Mandatory TP53 germline testing for all SHH-activated children aged 3-17 years

**4. Non-WNT/Non-SHH MB — Group 3 (~25%):**
- **Molecular:** MYC amplification (~17%); OTX2 overexpression (~65%); GFI1/GFI1B enhancer hijacking with MYC; SMARCA4 mutations; isochromosome 17q
- **Histology:** Classic, large cell/anaplastic (MYC-amplified often LCA)
- **Demographics:** Infants and young children (<10 years); male predominance; highest rate of M+ disease (~45%)
- **Prognosis:** 5-year OS ~45-60% (worst non-SHH group); MYC-amplified Group 3: OS ~40%
- **Cell of origin:** Progenitors near rhombic lip (same as WNT but different activation)

**5. Non-WNT/Non-SHH MB — Group 4 (~35%):**
- **Molecular:** CDK6 amplification; MYCN amplification (~5%); SNCAIP duplication (tandem duplication); KDM6A/KDM6B mutations; isochromosome 17q
- **Histology:** Classic predominantly; rare large cell/anaplastic
- **Demographics:** Most common MB; all ages (peak 10-17 years); male predominance ~3:1
- **Prognosis:** 5-year OS ~75-85% (intermediate)
- **Cell of origin:** Unipolar brush cells (glutamatergic cerebellar interneurons)

### Histological classification

**Classic (most common, ~72%):** Densely packed, uniform small round cells with scant cytoplasm; Homer-Wright rosettes (~40%); high mitotic rate.

**Desmoplastic/Nodular (DN, ~15%):** Nodular pale islands (reticulin-free zones) surrounded by dense reticulin-rich desmoplastic stroma; characteristic of SHH-MB in infants; favorable prognosis even with leptomeningeal spread in infants.

**Medulloblastoma with Extensive Nodularity (MBEN, ~5%):** Extreme version of DN; >50% nodular architecture; SHH-MB in infants; best prognosis (5-year OS ~100% with some protocols).

**Large Cell/Anaplastic (LCA, ~8%):** Nuclear enlargement (large cell) and nuclear molding, apoptosis, prominent mitoses (anaplastic); marks highest-risk histology; MYC-amplified Group 3 MB often LCA; adverse prognosis regardless of molecular subgroup.

## Function

### Biology of medulloblastoma subgroups

**WNT-MB biology:**
CTNNB1 mutation → β-catenin accumulates in nucleus → TCF/LEF target gene activation → WNT target program; the WNT pathway in rhombic lip progenitors drives cell proliferation; nuclear β-catenin in MB cells is sufficient for transformation; Gorlin syndrome (PTCH1 germline) does NOT predispose to WNT-MB; Li-Fraumeni (TP53) can occasionally produce WNT-activated tumors; WNT-MB uniquely lacks isochromosome 17q and monosomy 6 is present → monosomy 6 is the cytogenetic signature.

**SHH-MB biology:**
Purkinje cells express SHH → activates PTCH1 on GCPs → normally drives transient proliferation during cerebellar development (neonatal) → GCPs differentiate and migrate to form internal granular layer; PTCH1 LOF in GCPs → constitutive SMO → GLI2 → CCND2 (cyclin D2) → persistent GCP proliferation → tumor; adult SHH-MB: TERT promoter activation (~80%) → telomere maintenance → enables transformation in older, less proliferative progenitor pool.

**Group 3 MB biology:**
MYC amplification → extreme transcriptional activation → LCA-phenotype rapid cycling → pro-apoptotic stress countered by GFI1/GFI1B (oncogene enhancer hijacking) and OTX2 (neural stem cell TF); highest rate of leptomeningeal dissemination at diagnosis; resistant to standard chemotherapy when MYC-amplified; BET inhibitors (JQ1) suppress MYC expression in Group 3 MB preclinically.

**Group 4 MB biology:**
CDK6 amplification → constitutive CDK6 kinase → RB phosphorylation → E2F → proliferative gene program; KDM6A/KDM6B (histone H3K27 demethylases) — LOF → H3K27me3 accumulation → epigenetic silencing of differentiating genes; SNCAIP (synuclein alpha-interacting protein) tandem duplication is a unique chromatin regulatory alteration; methylation profiling is essential to distinguish from SHH/WNT.

## Pathology

### Staging — Chang classification (updated)

| Stage | Definition |
|-------|-----------|
| M0 | No metastases |
| M1 | Microscopic tumor cells found in CSF cytology |
| M2 | Gross nodular seeding in cerebellar/cerebral subarachnoid space or in third/fourth ventricles |
| M3 | Gross nodular seeding in spinal subarachnoid space |
| M4 | Extraneuraxial metastases |

**Risk stratification:**
- **Standard risk:** Localized (M0), ≤3 years old not eligible (infant protocols), resected (<1.5 cm² residual), non-LCA histology, WNT or SHH-TP53wt or Group 4 (with MYC-negative)
- **High risk:** M1-M4, residual tumor >1.5 cm², LCA histology, MYC amplification, SHH-TP53-mutant, or Group 3

### Treatment

**Surgery (maximal safe resection):**
Gross or near-total resection (NTR, ≤1.5 cm² residual) → significantly improved EFS; median resection achieves NTR/GTR in ~70-80% with modern neuro-navigation; posterior fossa craniotomy with tumor in 4th ventricle; hydrocephalus management (ventriculostomy/EVD during surgery, ETV or shunt for refractory hydrocephalus); cerebellar mutism syndrome (CMS, ~25% of posterior fossa surgery): transient inability to speak, ataxia, emotional lability → majority recover over months; risk reduction: approach via telovelar vs midline vermian splitting.

**Craniospinal irradiation (CSI):**
- **Standard risk:** CSI 23.4 Gy + posterior fossa boost to 54-55.8 Gy total; proton beam preferred (reduces integral dose to developing CNS and off-target organs); 5-year EFS ~81% [^packer-2006-std-risk-mb]
- **High risk:** CSI 36 Gy + posterior fossa 55.8 Gy ± spinal metastatic site boosts
- **WNT-MB de-escalation:** ACNS1422 (CSI 18 Gy reduced): results pending; MBWNT-3 (omit radiation in CSF-negative WNT-MB): ongoing; chemotherapy intensification may offset reduced RT
- **Infants (<3 years):** Radiation causes catastrophic neurotoxicity in developing brain → CSI deferred/avoided; HD chemotherapy induction (carboplatin+vincristine+cyclophosphamide+methotrexate or HDCT+auto-SCT); SHH-MBEN infants: induction + maintenance without RT achieves ~100% EFS; Head-start III: HDCT+auto-SCT for poor-risk infant MB

**Adjuvant chemotherapy (standard risk):**
Packer/CCSG-923: vincristine during RT → 8 cycles of CCNU+cisplatin+vincristine (weekly × 8 courses over ~16 months); 5-year EFS ~81% [^packer-2006-std-risk-mb]; major toxicities: ototoxicity (cisplatin, ~30% requiring hearing aids), myelosuppression, neurotoxicity (vincristine neuropathy).

**High-risk MB chemotherapy:**
COG ACNS0332: standard vs carboplatin+thiotepa induction → CCNU+cisplatin+vincristine maintenance; carboplatin during radiation improved EFS (62.3% vs 59.3%) but increased hematologic toxicity; HDCT + auto-SCT: used in some high-risk protocols (particularly Group 3 MYC-amplified); tandem HDCT in Group 3/4 high-risk explored in cooperative group studies.

**Targeted therapy:**
- **SMO inhibitors in SHH-MB:** Sonidegib + craniospinal radiation: Phase 2 (PBTC-039): for adult/pediatric SHH-MB; vismodegib single-agent in adult SHH-MB (PBTC-025B): ORR ~41%; ongoing frontline Phase 3 trials combining SMO inhibitors with standard therapy in SHH-MB
- **Pemetrexed + gemcitabine:** Active in R/R pediatric MB across subgroups (ORR ~40%); now incorporated in some maintenance protocols for high-risk Group 3/4
- **ONC201 (dopamine receptor D2 antagonist):** Group 4 MB with SNCAIP or H3K27me3 markers → active in R/R Group 4 (unique mechanism); Phase 1/2 data showing ORR ~20-40% in H3-altered/Group 4 MB
- **PLK4 inhibitor (CFI-400945):** Centrosome amplification in LCA MB → Phase 1 in pediatric solid tumors
- **Immunotherapy (pembrolizumab, nivolumab):** Limited activity in MB (low mutational burden, immunologically cold); ongoing trials with combination strategies

### Long-term effects

MB survivors face substantial late effects — inversely proportional to age at irradiation:
- **Neurocognitive:** IQ decline 1-2 points/year post-CSI in young children; processing speed, working memory, attention most affected; proton beam reduces dose to hippocampus → preserves verbal memory better than photon CSI; executive function impairment limits academic/vocational achievement
- **Endocrine:** GH deficiency (~80%); hypothyroidism; precocious or delayed puberty; obesity; GH supplementation recommended; monitor TSH, FSH/LH annually
- **Second malignancies:** CSI field → radiation-induced glioma, meningioma (10-20 years post-irradiation); chemotherapy → secondary AML/MDS (alkylators)
- **Hearing loss:** Cisplatin ototoxicity (~30-40%); proton beam reduces cochlear dose; sodium thiosulfate amifostine protective in some trials
- **Cardiovascular:** Radiation-induced vasculopathy, moyamoya syndrome (radiation to circle of Willis); metabolic syndrome
- **Quality of life:** Social isolation, reduced independence, impaired quality of life in a substantial minority of survivors; neurocognitive rehabilitation programs beneficial

## Connections

- `connects-to` → **[PTCH1](../../03-molecular/ptch1/README.md)** — PTCH1/SMO/SUFU/GLI2 mutations define SHH-activated MB (~38%); germline PTCH1 → Gorlin syndrome + infant/adult SHH-MB; SHH-MB in adults is the primary indication for vismodegib in MB trials; desmoplastic/nodular histology is the hallmark of SHH-MB with PTCH1 LOF.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC amplification (~17%) defines the most aggressive Group 3 MB (5-year OS ~45%); MYCN amplification in SHH-MB + TP53 mutation = highest-risk SHH-MB; MYC drives extreme proliferative rate; BET inhibitors suppress MYC in Group 3/4 MB preclinically.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — WNT-activated MB (~10%) carries CTNNB1 activating mutations + monosomy 6 + nuclear β-catenin; WNT-MB has near-universal cure (5-year OS ~95%); de-escalation trials (reduced CSI 18 Gy) ongoing; CTNNB1 mutations are absent in SHH/Group 3/Group 4 MB.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — SHH-activated/TP53-mutant MB: MYCN amplification + TP53 mutation → 5-year OS ~40%; TP53 mutations are germline in Li-Fraumeni syndrome → elevated MB risk; Group 3 MYC-amplified MB acquires TP53 at relapse; p53 IHC (>10% nuclear) is a surrogate marker in MB.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Medulloblastoma is the most common pediatric brain tumor, arising in the cerebellum (posterior fossa) where it obstructs the 4th ventricle → hydrocephalus; maximal safe resection risks cerebellar mutism syndrome, and craniospinal irradiation drives neurocognitive late effects.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — Gorlin syndrome (germline PTCH1 loss) predisposes to SHH-activated medulloblastoma, typically the desmoplastic/nodular infant form; because these children are radiation-hypersensitive (PTCH1 carriers get RT-field basal cell carcinomas), radiation-sparing strategies are favored.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Germline TP53 (Li-Fraumeni) defines the SHH-activated/TP53-mutant subgroup — often MYCN-amplified, large-cell/anaplastic, ~40% 5-year OS; TP53 germline testing is mandatory for all SHH-MB aged 3-17, and craniospinal irradiation is avoided given LFS radiation sensitivity.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Medulloblastoma and IDH-mutant glioma are both molecularly classified brain tumors but opposite poles: medulloblastoma is a fast embryonal cerebellar tumor of children (SHH/WNT/MYC), while IDH-mutant glioma is a slow diffuse hemispheric tumor of adults driven by 2-HG epigenetics.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Atypical teratoid/rhabdoid tumor is the key infant mimic of medulloblastoma: both are small-round-blue-cell posterior-fossa tumors, but ATRT is defined by SMARCB1 (INI1) loss and far more aggressive — INI1 immunostaining (kept in MB, lost in ATRT) distinguishes them.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — SHH-activated medulloblastoma arises from cerebellar granule neuron precursors of the external granular layer, whose normal proliferation depends on Sonic hedgehog from Purkinje neurons; a PTCH1/SMO lesion locks this hedgehog program on, driving the desmoplastic/nodular tumor.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Craniospinal radiotherapy is central to medulloblastoma treatment: because the tumor seeds the CSF and drops spinal metastases, photon or proton irradiation of the whole brain and spinal axis follows surgery—curative for many but neurocognitively toxic in children.
- `connects-to` → **[DICER1 Syndrome](../dicer1-syndrome/README.md)** — Medulloblastoma is part of several cancer-predisposition syndromes: germline DICER1 loss can produce a medulloblastoma-like embryonal CNS tumor, as Gorlin (PTCH1) drives SHH-subtype and Li-Fraumeni (TP53) high-risk disease—so syndromic testing is warranted.
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — Medulloblastoma and diffuse midline glioma are the major malignant pediatric brain tumors but differ: medulloblastoma is a resectable cerebellar tumor often cured by surgery plus craniospinal radiotherapy, while DMG is an unresectable, fatal H3 K27M brainstem glioma.
- `connects-to` → **[Familial Adenomatous Polyposis](../fap/README.md)** — Medulloblastoma links to FAP through Turcot syndrome: germline APC loss that drives colonic polyposis also activates Wnt/β-catenin in the cerebellum, producing WNT-subgroup medulloblastoma—the same pathway connecting a gut cancer syndrome to a brain tumor.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Medulloblastoma and neuroblastoma are both embryonal childhood tumors that look alike as 'small round blue cells' but differ in origin: medulloblastoma from cerebellar progenitors, neuroblastoma from peripheral sympathetic neuroblasts—CNS versus sympathetic chain.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Medulloblastoma and rhabdomyosarcoma are both small-round-blue-cell embryonal tumors told apart by immunohistochemistry: medulloblastoma expresses neuronal markers (synaptophysin), rhabdomyosarcoma skeletal-muscle markers (desmin, myogenin)—same look, different lineage.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — SHH-subtype medulloblastoma is driven by Smoothened: PTCH1 loss or SMO activation unleashes hedgehog signaling, defining one of the four molecular groups, and SMO inhibitors like vismodegib target it—though resistance and growth-plate toxicity limit use in children.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — MYCN amplification marks high-risk medulloblastoma: in Group 3 and 4 tumors, amplified MYC/MYCN drives aggressive proliferation and poor prognosis, so molecular subgrouping—not just histology—now guides how intensively each child's tumor is treated.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Medulloblastoma can spread beyond the CNS to bone marrow: though it usually disseminates through cerebrospinal fluid along the neuraxis, this embryonal tumor occasionally metastasizes to bone and marrow—rare among brain tumors and a sign of aggressive disease.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy is standard for pediatric medulloblastoma's craniospinal radiation: because children need the whole brain and spine irradiated, protons' lack of exit dose spares the heart, lungs and gut, cutting the lifelong toxicity of treating this childhood brain tumor.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Medulloblastoma is the commonest malignant brain tumor of childhood, arising in the cerebellum: it disrupts balance and blocks CSF flow (hydrocephalus), and it seeds along the nervous system's CSF pathways—why staging and radiation cover the whole neuraxis.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Medulloblastoma arises from cerebellar progenitors, distinct from astrocyte-derived gliomas: it is an embryonal small-round-blue-cell tumor of granule-cell precursors, so its biology and treatment differ fundamentally from the astrocytic and oligodendroglial gliomas.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Some medulloblastomas reactivate telomerase via TERT: promoter mutations switch TERT back on, especially in adult SHH-subgroup tumors, letting cells divide indefinitely—a molecular marker that helps subgroup and risk-stratify these embryonal brain cancers.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Medulloblastoma and retinoblastoma are both embryonal childhood cancers: each arises from immature precursor cells—cerebellar in one, retinal in the other—and both can seed the cerebrospinal fluid, a parallel between developing neural tissues turning malignant.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Medulloblastomas recruit brain microglia into their microenvironment: these tumor-associated immune cells can be co-opted to support growth and shape the response to therapy, making the cerebellar tumor's immune niche a focus of new treatment ideas.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Medulloblastoma's WNT subgroup has a leaky, VEGF-rich vasculature: its abnormal fenestrated blood vessels let chemotherapy reach the tumor better, helping explain why WNT medulloblastoma has the best prognosis of the four subgroups.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Medulloblastoma resists immunotherapy partly through regulatory T cells: the tumor's immunosuppressive microenvironment and the brain's immune privilege blunt T-cell attack, so Tregs are among the barriers checkpoint therapy must overcome here.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Curing medulloblastoma can injure oligodendrocytes: the craniospinal radiation that controls it damages these myelinating cells, causing white-matter loss and the neurocognitive decline that shadows childhood survivors.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Medulloblastoma springs from the cerebellum's wiring: it arises from neural precursors that should build cerebellar circuits, and like other brain tumors it can integrate with neurons at synapses, tying the cerebellum's developmental program to the cancer.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Medulloblastoma is largely cold to cytotoxic T cells: with few mutations and a protected brain site, it resists immune attack, so engineered T-cell and other immunotherapies are being developed to reach a tumor that checkpoint drugs miss.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Group 3 medulloblastoma leans on the cell-cycle kinase CDK4/6: MYC-driven proliferation depends on it, so CDK4/6 inhibitors are studied to slow the most aggressive subtype where current therapy often fails.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Medulloblastoma outpaces its oxygen: the fast-growing cerebellar tumor turns hypoxic in its core, switching on VEGF-driven angiogenesis to build the blood supply it needs to keep expanding.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Medulloblastoma shows up in the eyes: by blocking CSF flow it raises intracranial pressure, swelling the optic discs (papilledema) and blurring vision, often among the first signs of the cerebellar tumor.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Medulloblastoma sits in a macrophage-rich niche: tumor-associated macrophages and microglia populate the microenvironment, especially in SHH-subtype tumors, shaping growth and immune evasion.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Medulloblastoma seeds the spinal canal: 'drop metastases' coat the cord and the nerve roots of the cauda equina via the CSF, which is why the whole neuraxis is irradiated, not just the tumor.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Some medulloblastomas calcify: flecks of calcium appear on CT, and the desmoplastic subtype in particular can show calcification within the cerebellar mass.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Medulloblastoma rarely escapes the nervous system: extraneural metastases to bone, marrow, liver and lung can occur, an unusual spread for a brain tumor that shifts the prognosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals medulloblastoma's neuroblastic roots: its small round blue cells ring up into Homer Wright rosettes around tangles of neuritic processes, the ultrastructure of a primitive tumor trying to form neurons.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — When medulloblastoma leaves the brain, the lung is a target: among its rare extraneural metastases — to bone, marrow, and liver — the lungs can be seeded, sometimes via a ventriculoperitoneal shunt.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Shunt-borne medulloblastoma can reach the abdomen: cells draining through a ventriculoperitoneal shunt seed the peritoneum and abdominal organs, an unusual route by which this brain tumor spreads beyond the skull.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains sort the subgroups: immunohistochemistry for nuclear beta-catenin marks the WNT tumors and GAB1/YAP1 the SHH ones, dividing medulloblastoma into the molecular groups that now drive prognosis and how intensely each child is treated.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The cure costs the marrow: craniospinal radiation irradiates a vast volume of blood-forming bone and the accompanying chemotherapy is myelosuppressive, so neutrophil counts fall and febrile neutropenia is a constant hazard during treatment.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Cisplatin in the regimen wastes magnesium: the platinum chemotherapy used against medulloblastoma injures the kidney tubule that reclaims magnesium, so blood levels drop and need replacing alongside watching for the drug's hearing loss.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Curing the brain stunts the body: craniospinal radiation damages the pituitary's growth-hormone output and the spine's own growth plates, so survivors fall off the height curve — growth-hormone deficiency is among the commonest late effects of treatment.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment reaches the reproductive axis: radiation to the brain disturbs the hormones timing puberty while alkylating chemotherapy damages the gonads, so survivors face precocious or delayed puberty and impaired fertility, prompting preservation counseling.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The intensive chemotherapy empties the marrow: the multi-drug regimens for medulloblastoma suppress platelet production into thrombocytopenia, so bleeding risk and transfusion needs are watched through the long months of treatment.
- `connects-to` → **[SUFU](../../03-molecular/sufu/README.md)** — A brake on the Hedgehog pathway, when lost, drives one subgroup: SUFU normally restrains SHH signaling, so germline or somatic SUFU loss unleashes the pathway to produce SHH-type medulloblastoma — a target for the same Hedgehog inhibitors aimed at SMO and PTCH1.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Cure comes at a hormonal price: craniospinal radiation and surgery near the hypothalamus and pituitary leave survivors with growth-hormone deficiency, thyroid and adrenal shortfalls and delayed puberty, so lifelong endocrine follow-up is part of survivorship.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — The treatment can seed a second tumor: the cranial radiation that cures medulloblastoma is itself a leading cause of radiation-induced meningiomas decades later, one of the secondary cancers that shadow long-term survivors.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Cell-cycle brakes fail in the aggressive subtypes: CDKN2A loss and the resulting CDK4/6 overactivity drive proliferation in MYC-amplified medulloblastomas, marking poor-prognosis tumors and a rationale for CDK4/6 inhibitors.
- `connects-to` → **[Stroke](../stroke/README.md)** — Radiation scars the brain's arteries: craniospinal irradiation causes a late cerebral vasculopathy — including moyamoya around the circle of Willis — that raises stroke risk in childhood medulloblastoma survivors.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Intensive therapy strips the defenses: the myelosuppressive chemotherapy used against medulloblastoma produces neutropenia, so febrile neutropenia and sepsis are among the acute treatment hazards.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 supports the aggressive subgroups: Group 3 and SHH medulloblastomas show STAT3 activation that backs proliferation and survival, a pathway studied for the high-risk, MYC-driven tumors that resist standard therapy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB adds a survival signal: medulloblastoma cells engage NF-κB-dependent survival and inflammatory signaling, one of the cooperating pathways alongside the SHH, WNT and MYC programs that define its subgroups.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A brain tumor that clots: like other CNS malignancies, medulloblastoma raises venous thromboembolism risk through tumor tissue factor and the immobility of major posterior-fossa surgery and illness.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Intensive chemo strips the lung's defenses: the dose-dense, often high-dose chemotherapy for medulloblastoma causes profound neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its platinum chemo scars young kidneys: cisplatin central to medulloblastoma regimens is nephrotoxic and ototoxic, and in a child the tubular injury and electrolyte wasting can leave lasting chronic kidney impairment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Craniospinal radiation leaves lasting scars on the mind: medulloblastoma survivors face neurocognitive decline, endocrine failure and the trauma of childhood cancer, carrying a heavy burden of depression.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Vincristine and tumor injure the nerves: the vincristine central to medulloblastoma chemotherapy causes peripheral neuropathy, and posterior-fossa disease adds neurological pain in survivors.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Radiation and steroids disturb glucose: craniospinal radiation damages the hypothalamic-pituitary axis and the dexamethasone for edema induces insulin resistance, predisposing survivors to diabetes.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Posterior-fossa surgery and steroids hinder repair: the craniotomy for medulloblastoma risks CSF leak and poor wound healing, worsened by the chronic dexamethasone used to control edema.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Posterior-fossa damage and treatment hit the gut: brainstem and cerebellar involvement causes dysphagia and aspiration, and craniospinal radiation plus chemotherapy bring mucositis and nausea.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Chemotherapy reawakens shingles: the chemotherapy for medulloblastoma suppresses a child's immunity, allowing latent or primary varicella-zoster to cause severe disseminated infection.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A childhood brain cancer with long survivorship breeds worry: the intensive therapy, neurocognitive late effects and relapse surveillance of medulloblastoma foster chronic anxiety in survivors and families.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Spinal radiation stunts the growing skeleton: craniospinal radiotherapy impairs vertebral growth, leaving survivors with short stature, reduced sitting height and scoliosis — a hallmark late effect.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Posterior-fossa surgery threatens swallowing and breath: cerebellar mutism syndrome with dysphagia raises aspiration risk, and brainstem involvement can compromise respiratory control.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Radiation marks the scalp and skin: craniospinal radiotherapy causes dermatitis and permanent alopecia in the treated field, alongside the skin effects of chemotherapy.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its cure costs the heart later: anthracycline and platinum chemotherapy plus radiation in childhood medulloblastoma carry long-term cardiovascular and cardiotoxic risk in survivors.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Cisplatin threatens the kidney: the platinum chemotherapy central to medulloblastoma treatment is nephrotoxic and ototoxic, demanding careful dosing in children.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Therapy suppresses immunity: intensive craniospinal radiation and chemotherapy leave children profoundly immunocompromised, while WNT and SHH subtypes are explored for targeted and immune therapy.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo joins surgery and radiation: multi-agent chemotherapy with vincristine, cisplatin and cyclophosphamide or CCNU, given with craniospinal radiation, cures most standard-risk medulloblastoma.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Hedgehog inhibitors for one subgroup: vismodegib and sonidegib block SMO in the SHH-activated subgroup of medulloblastoma driven by PTCH1, SMO or SUFU mutations.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Craniospinal radiation stunts the skeleton: irradiating the whole spine in young children impairs vertebral and long-bone growth, causing short stature and spinal deformity among the late effects of cure.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The cure costs memory: craniospinal radiation and the cranial boost damage the hippocampus, impairing the formation of new memories and lowering IQ in childhood medulloblastoma survivors, which drives efforts to spare the hippocampus during radiotherapy.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Two small-round-blue-cell tumours of childhood: medulloblastoma and Ewing sarcoma are both densely cellular embryonal-type cancers of the young but differ at the root—Ewing is driven by an EWSR1-FLI1 fusion, medulloblastoma by SHH, WNT or MYC programmes.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold tumour: medulloblastoma has a low mutational burden and sparse immune infiltrate, so PD-1 checkpoint inhibitors have shown little benefit, and immunotherapy effort has shifted toward CAR-T against B7-H3 and GD2.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — SHH-pathway tumours: SHH-subgroup medulloblastoma and basal cell carcinoma share aberrant Sonic-hedgehog signalling—both arise in Gorlin syndrome—and respond to SMO inhibitors like vismodegib.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Rare extraneural metastasis: although it usually spreads through the CSF, medulloblastoma can disseminate outside the nervous system to bone, marrow and the liver, seeding the hepatic lobule.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Survivorship cardiotoxicity: the anthracycline chemotherapy and incidental cardiac radiation used to cure medulloblastoma injure the myocardium, a late effect monitored for decades in survivors.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Radiation through the neck: the craniospinal radiotherapy that cures medulloblastoma irradiates the thyroid in its exit path, causing hypothyroidism and a raised long-term risk of thyroid cancer in survivors.
- `connects-to` → **[AML](../aml/README.md)** — Therapy-related leukaemia: the alkylating agents and topoisomerase inhibitors used against medulloblastoma damage haematopoietic stem cells, occasionally causing a secondary myelodysplasia or acute myeloid leukaemia years later.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Stunted growth after cure: radiation to the hypothalamic-pituitary axis blunts growth-hormone and IGF-1 signalling, making growth failure and short stature among the most common endocrine late effects in medulloblastoma survivors.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Stem-cell maintenance: Notch signalling sustains medulloblastoma stem-like cells, especially in Group 3/4 tumours, a candidate therapeutic target for these aggressive subgroups.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dependence: EZH2-driven histone methylation enforces the proliferative programme of Group 3/4 medulloblastoma, an actionable epigenetic vulnerability.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — SHH-driven cell cycle: Hedgehog signalling upregulates cyclin D1, partnering CDK4/6 to push SHH-subgroup medulloblastoma cells through the cell cycle.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: PI3K/AKT signalling supports medulloblastoma cell survival and is implicated in resistance to Hedgehog-pathway inhibitors in the SHH subgroup.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Growth-signal hub: mTOR integrates the growth-factor signalling of medulloblastoma, driving the protein synthesis and proliferation of these embryonal tumours.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the hypoxic medulloblastoma drives the VEGF angiogenesis and metabolic adaptation that support its rapid growth.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Apoptotic chemosensitivity: high MYC in Group 3 medulloblastoma primes cells for caspase-3-mediated apoptosis, part of why these embryonal tumours respond initially to cytotoxic chemotherapy and radiation.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Microglial microenvironment: CCL2 recruits microglia and macrophages into the medulloblastoma microenvironment, shaping the immunosuppressive niche of this childhood cerebellar tumour.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK proliferation: RAS-RAF-ERK signalling contributes to medulloblastoma proliferation, cooperating with the SHH, WNT and MYC programmes that define its molecular subgroups.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — Activating CTNNB1 (β-catenin) mutations define the WNT subgroup of medulloblastoma, the best-prognosis molecular subgroup whose cure rates exceed 90%—driving efforts to de-escalate therapy and spare these children long-term toxicity.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on medulloblastoma cells follows CXCL12 gradients to seed the cerebrospinal fluid, the leptomeningeal dissemination that mandates craniospinal irradiation in all but the lowest-risk cases of this cerebellar tumor.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — RAD51-mediated homologous-recombination repair helps high-risk medulloblastomas survive radiation-induced DNA damage, a mechanism of the radioresistance that limits cure in the aggressive Group 3 and TP53-mutant SHH tumors.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Medulloblastoma is now defined by its DNA-methylation profile, which separates the WNT, SHH, Group 3 and Group 4 subgroups with their different biology, prognosis and therapy—making the methylome the basis of modern diagnosis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Group 3 medulloblastomas express GD2, and GD2-directed CAR-T cells aim to kill them through perforin and granzyme, an emerging immunotherapy for the highest-risk subgroup that responds poorly to standard treatment.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — SHH-subgroup medulloblastoma arises from cerebellar granule-neuron precursors, whose normal proliferation and differentiation are shaped by neurotrophin-Trk signaling, the developmental context the tumor hijacks.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA activates the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) across medulloblastoma subgroups, contributing to growth and to resistance to SHH-pathway inhibitors.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis (mapped) releases E2F1 to drive S-phase entry, the proliferative output amplified by the MYC and MYCN (both mapped) of high-risk medulloblastoma.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β pathway signaling is a recurrent driver of the aggressive Group 3 medulloblastoma, cooperating with MYC amplification in this poor-prognosis subgroup.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Deregulation of the RB1-E2F checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) drives the proliferation of medulloblastoma, particularly the aggressive MYC-amplified subgroups.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (ERK1/2 already mapped) provides a proliferative input cooperating with the subgroup-defining drivers of medulloblastoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 inactivation (p53 already mapped) contributes to the poor prognosis of TP53-altered SHH medulloblastoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates the invasion and immune microenvironment of medulloblastoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 mapped) provides a proliferative and immunomodulatory input across medulloblastoma subgroups.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) contributes to the biology of Group 3/4 medulloblastoma and shapes its tumor microenvironment.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immunologically cold microenvironment of medulloblastoma, a barrier to its immunotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment and radiation response of medulloblastoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the cerebellar-progenitor proliferation and survival programs hijacked by medulloblastoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β regulates GLI and β-catenin stability (SHH/SMO and WNT-β-catenin already mapped), modulating the subtype-defining signaling of medulloblastoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the tumor microenvironment of medulloblastoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling contributes to the migratory and leptomeningeal-metastatic behavior of medulloblastoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of medulloblastoma cells.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF and the broader chromatin machinery contribute to the epigenetically driven subgroups of medulloblastoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of medulloblastoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of medulloblastoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of medulloblastoma.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — YAP1-Hippo signaling participates in the proliferation of the granule-neuron-precursor-derived cells of SHH medulloblastoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of medulloblastoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and tumor-immune microenvironment of medulloblastoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammatory tumor microenvironment of medulloblastoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the tumor microenvironment of medulloblastoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of medulloblastoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin (SPP1) participates in the microglial/macrophage tumor microenvironment and metastatic dissemination of medulloblastoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunotherapy: medulloblastoma is largely immunologically cold, and MHC-based antigen presentation is central to the vaccine and cellular immunotherapy strategies being explored, particularly for the high-risk Group 3 subtype (MYC already mapped).
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cellular immunotherapy: IL-2-driven T-cell expansion supports the CAR-T and adoptive approaches under investigation for medulloblastoma, aiming to reach the tumour cells that seed the cerebrospinal fluid (perforin already mapped).
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint context: PD-1 checkpoint blockade has limited single-agent activity in the cold medulloblastoma microenvironment, motivating combinations with radiation and targeted therapy to render it immunoresponsive.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Chemotherapy anaemia: the intensive multidrug chemotherapy that, with craniospinal radiation, treats medulloblastoma is myelosuppressive, lowering haemoglobin and requiring transfusion support in these young patients.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac late effect: the craniospinal radiation for medulloblastoma exposes the heart, and any anthracycline adds cardiotoxicity, with troponin elevation marking the myocardial injury that threatens the many long-term survivors.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 helps make medulloblastoma an immunologically cold tumour (PD-1 already mapped), dampening the T-cell response that the CAR-T and checkpoint strategies under investigation aim to mount.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Hedgehog-lipid link: cholesterol and its oxysterol derivatives activate Smoothened (already mapped), the driver of the Hedgehog pathway (PTCH1 already mapped) in the SHH subtype of medulloblastoma, linking cellular lipid handling to the oncogenic signalling.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 microglial polarisation: IL-4 polarises the tumour-associated microglia and macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immunologically cold microenvironment of medulloblastoma.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6 and IL-1 already mapped) of the medulloblastoma microenvironment.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 microglial (already mapped) niche of the immunologically cold microenvironment of medulloblastoma.
- `connects-to` → **[Endothelial cell](../../04-cellular/endothelial-cell/README.md)** — WNT fenestrated vasculature: the WNT-subgroup medulloblastoma has an aberrant, fenestrated tumour endothelium with a leaky blood-tumour barrier (VEGF already mapped), letting in chemotherapy and helping explain its excellent prognosis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the intensive multi-agent chemotherapy of medulloblastoma is myelosuppressive, causing anaemia (haemoglobin already mapped) needing transfusion that can load the young child with iron.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Hypothalamic obesity: the craniospinal radiation damages the hypothalamic-pituitary (growth hormone already mapped) axis, causing the hypothalamic obesity and leptin dysregulation of the medulloblastoma survivor.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Survivorship metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-endocrine late effects of medulloblastoma survivorship.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic-syndrome adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the metabolic syndrome that complicates the long-term survival of medulloblastoma.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Anthracycline cardiotoxicity: the anthracycline chemotherapy of the medulloblastoma regimens causes the cardiotoxicity (troponin already mapped) of the heart, a survivorship concern in the childhood survivor.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the immunotherapy of medulloblastoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of medulloblastoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the immunologically cold medulloblastoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the medulloblastoma microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of medulloblastoma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of medulloblastoma.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of medulloblastoma.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral arm: the plasma cells secrete the antibodies (already mapped) of the humoral response within the immune microenvironment of medulloblastoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the sparse immune infiltrate of the immunologically cold medulloblastoma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of medulloblastoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) and myeloid activation of the medulloblastoma microenvironment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Craniospinal RT anaemia: erythropoietin counters the radiation-induced myelosuppression from the craniospinal irradiation used in medulloblastoma; EPO-stimulating agents are a standard supportive measure during and after the CSI phase of medulloblastoma treatment.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement-mediated lysis: the complement C5 effector (with complement C3 already mapped) participates in complement-dependent cytotoxicity against medulloblastoma cells; anti-C5 signalling modulates the immune-infiltration pattern of the immunogenic WNT-subgroup medulloblastoma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — BBB drug delivery: bradykinin (B2 receptor) transiently increases blood-brain barrier permeability, a mechanism exploited to enhance chemotherapy (already mapped) delivery to posterior-fossa medulloblastoma and reduce reliance on high-dose craniospinal irradiation.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Tumour-immune alarmin: TSLP released by the medulloblastoma stroma primes dendritic cells (already mapped) and mast cells (already mapped) toward the Th2 (IL-4, IL-13 already mapped) immune microenvironment of the WNT (wnt-beta-catenin already mapped) subgroup.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: C1-INH controls the classical-pathway arm (C3, C5 and C5aR1 already mapped) in the medulloblastoma microenvironment, modulating complement-dependent cytotoxicity and the tumour-associated macrophage (already mapped) response.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell histamine in MB microenvironment: histamine, released by the mast cells (already mapped) of the medulloblastoma stroma, modulates microvascular permeability and promotes the VEGF-driven (already mapped) angiogenesis and immunomodulation of medulloblastoma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian antitumour melatonin: melatonin, via MT1/MT2 receptors on medulloblastoma cells and the cerebellar tumour vasculature (already mapped), suppresses SHH-pathway (already mapped) proliferation and VEGF-driven (already mapped) angiogenesis in paediatric medulloblastoma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-SHH axis: testosterone, via androgen receptor on SHH-subgroup (already mapped) medulloblastoma cells, modulates the hedgehog proliferative pathway (already mapped) and the sex-dimorphic vulnerability to medulloblastoma in the paediatric posterior fossa.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Cerebellar neuromodulator: serotonin, via 5-HT3 receptors on cerebellar granule cells (already mapped), modulates the neuronal signalling of the medulloblastoma microenvironment; 5-HT3-driven nausea from craniospinal radiation (already mapped) is a major treatment morbidity.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Medulloblastoma prolactin neuro-immune: prolactin, via PRLR on tumour-associated macrophages (already mapped) and mast cells (already mapped), upregulates NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in the paediatric medulloblastoma microenvironment.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Medulloblastoma oxytocin anti-tumour: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in the medulloblastoma cerebellar microenvironment.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Medulloblastoma vasopressin vascular: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates the tumour vascular niche; dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling in medulloblastoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — MB selenium: selenium, as GPx in microglia (already mapped) and macrophages (already mapped), scavenges ROS in the tumour microenvironment; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of medulloblastoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MB iodine: iodine-dependent thyroid hormones modulate microglia (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of medulloblastoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — MB sodium: high dietary sodium promotes macrophage (already mapped) and mast-cell (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of medulloblastoma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — MB copper: copper, via SOD1 in macrophages (already mapped) and microglia (already mapped), scavenges tumour ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and T-cytotoxic (already mapped) tumour cascade of medulloblastoma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — MB zinc: zinc, as cofactor of antioxidant enzymes in macrophages (already mapped) and microglia (already mapped), attenuates brain tumour oxidative stress; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of medulloblastoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — MB potassium: potassium regulates macrophage (already mapped) and T-cytotoxic cell (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mast-cell (already mapped) tumour cascade of medulloblastoma.

[^packer-2006-std-risk-mb]: Packer RJ, Gajjar A, Vezina G, et al. Phase III study of craniospinal radiation therapy followed by adjuvant chemotherapy for newly diagnosed average-risk medulloblastoma. *J Clin Oncol.* 2006;24(25):4202-4208. [doi:10.1200/JCO.2006.06.4980](https://doi.org/10.1200/JCO.2006.06.4980) · [PubMed 16943538](https://pubmed.ncbi.nlm.nih.gov/16943538/)
[^taylor-2012-mb-subgroups]: Taylor MD, Northcott PA, Korshunov A, et al. Molecular subgroups of medulloblastoma: the current consensus. *Acta Neuropathol.* 2012;123(4):465-472. [doi:10.1007/s00401-011-0922-z](https://doi.org/10.1007/s00401-011-0922-z) · [PubMed 22134537](https://pubmed.ncbi.nlm.nih.gov/22134537/)
