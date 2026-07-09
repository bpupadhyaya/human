---
schema: human-scale-entry/v1
id: retinoblastoma
name: Retinoblastoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Retinoblastoma is the most common intraocular childhood tumor (1/15,000); bilateral = germline RB1; unilateral = usually somatic; leukocoria is the classic presentation; intra-arterial/intravitreal chemotherapy preserves vision; hereditary RB1 confers osteosarcoma risk."
aliases: ["retinoblastoma", "RB1 tumor", "bilateral retinoblastoma", "hereditary retinoblastoma", "RBL", "retinoblastoma leukocoria", "intraocular tumor child", "retinoblastoma treatment", "retinoblastoma genetics"]
sources:
  - id: shields-2008-retinoblastoma
    type: peer-reviewed
    cite: "Shields CL, Shields JA. Retinoblastoma management: advances in enucleation, intravenous chemoreduction, and intra-arterial chemotherapy. Curr Opin Ophthalmol. 2010;21(3):203-212."
    doi: "10.1097/ICU.0b013e328338676a"
    pmid: "20224400"
    url: "https://doi.org/10.1097/ICU.0b013e328338676a"
  - id: knudson-1971-two-hit
    type: peer-reviewed
    cite: "Knudson AG Jr. Mutation and cancer: statistical study of retinoblastoma. Proc Natl Acad Sci USA. 1971;68(4):820-823."
    doi: "10.1073/pnas.68.4.820"
    pmid: "5279523"
    url: "https://doi.org/10.1073/pnas.68.4.820"
cross_links:
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "E2F1 is released constitutively when RB1 is biallelically lost in retinoblastoma; unchecked E2F1 drives retinal progenitor proliferation → tumor mass; retinoblastoma cells have MYCN amplification and additional mutations that cooperate with E2F1 dysregulation."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Biallelic RB1 loss is the universal initiating event in retinoblastoma; hereditary (bilateral) = germline RB1 + somatic LOH; sporadic (unilateral) = two somatic RB1 hits; MYCN amplification is an alternative RB-independent driver in a rare subset."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 pathway is bypassed in retinoblastoma via MDM2 amplification, MDM4 overexpression, or MYCN amplification; p53 pathway loss allows retinal progenitors to survive RB1 LOF-driven E2F1 pro-apoptotic signaling; TP53 mutations are rare in primary retinoblastoma."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Hereditary RB1 carriers have 30-50× risk of osteosarcoma as a second malignancy; radiation exposure dramatically amplifies this risk — external beam RT now avoided in hereditary RB; germline RB1 is found in ~3-5% of sporadic osteosarcomas."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Retinoblastoma is the most common intraocular tumor of childhood, presenting as leukocoria (white pupillary reflex) or strabismus; globe-sparing therapy — intra-arterial and intravitreal chemotherapy — salvages most eyes, reserving enucleation for advanced (Group E) disease."
  - target: 01-human/03-molecular/mycn
    relation: connects-to
    note: "A small (~2%) RB1-wildtype subset of retinoblastoma is instead driven by massive MYCN amplification, which raises CCNE1/CDK2 to hyperphosphorylate Rb and release E2F1 despite intact RB1; these aggressive, non-hereditary tumors are harder to salvage than RB1-mutant ones."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Retinoblastoma must neutralize the p53 apoptosis that RB1 loss would otherwise trigger: MDM2 amplification (~4%) and MDM4 overexpression (~65%) degrade or inhibit p53, so TP53 itself is rarely mutated — making MDM2/MDM4 antagonists a rational therapeutic strategy."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Retinoblastoma arises from a neuron: the developing cone photoreceptor precursor, which depends on RB1 to restrain proliferation; biallelic RB1 loss unleashes E2F-driven division, why the tumor is so specific to the retina despite RB1 being lost in every cell of carriers."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Germline retinoblastoma carries a brain risk: trilateral retinoblastoma is a pineoblastoma or suprasellar PNET — an intracranial embryonal tumor sharing the retina photoreceptor lineage — arising in a few percent of bilateral RB patients, prompting routine brain MRI surveillance."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Retinoblastoma and Li-Fraumeni are the paradigm hereditary cancer-predisposition syndromes built on tumor-suppressor loss: RB1 (the first tumor suppressor found, basis of Knudson's two-hit hypothesis) versus TP53; both inherit one bad allele and need only a somatic second hit."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy has a fraught role in retinoblastoma: external-beam photon radiation can control the tumor and save the eye, but in heritable RB1-mutant children it sharply raises second-cancer risk (especially osteosarcoma) in the field—so it is now largely avoided."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "Retinoblastoma and small cell lung cancer are united by RB1 loss: the tumor-suppressor that, germline-mutated, causes childhood retinoblastoma is inactivated (with TP53) in nearly all small cell lung cancers—one gene across utterly different cancers."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Survivors of heritable retinoblastoma face a lifelong excess of second cancers including melanoma: the germline RB1 mutation in every cell, compounded by radiotherapy, predisposes to melanoma and sarcomas decades later—so survivorship means lifelong surveillance."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "Retinoblastoma and uveal melanoma are primary intraocular malignancies at opposite ages: retinoblastoma is a childhood RB1-driven retinal tumor causing leukocoria, while uveal melanoma is an adult GNAQ/BAP1-driven choroidal tumor—differing in cell, age and genetics."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Retinoblastoma and neuroblastoma are both embryonal childhood tumors with eye signs: retinoblastoma causes leukocoria from a retinal tumor, while neuroblastoma causes periorbital metastases and opsoclonus—different origins, overlapping pediatric presentations."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Retinoblastoma links to medulloblastoma through trilateral retinoblastoma: heritable RB1 loss can produce bilateral eye tumors plus a midline brain PNET (pineoblastoma), so RB1, like other embryonal-tumor genes, can seed both retinal and CNS neuroectodermal tumors."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Retinoblastoma is the namesake of the RB-CDK4/6 cell-cycle brake: the RB protein normally blocks CDK4/6-cyclin D from pushing cells past the G1 checkpoint, so its loss removes that brake—the same axis CDK4/6 inhibitors restore in other RB-intact cancers."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Advanced retinoblastoma spreads to the bone marrow and CNS: untreated, it extends along the optic nerve into the brain and disseminates to marrow, so metastatic workup and intrathecal/systemic therapy are added when the tumor breaches the eye."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Hereditary retinoblastoma survivors face lifelong second-cancer risk: germline RB1 loss predisposes to sarcomas, melanoma and later epithelial cancers (worsened by past radiotherapy)—and RB1 is itself lost in many breast cancers, tying the genes together."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy is preferred when retinoblastoma needs external radiation: in heritable RB1 patients, who are highly prone to radiation-induced second cancers, protons' sharp dose falloff spares orbital bone and brain, lowering that lifelong risk."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Retinoblastoma is a tumor of the developing nervous system's retina: arising from retinal precursor cells, heritable RB1 loss can also produce an intracranial pineal tumor ('trilateral retinoblastoma'), so the eye lesion is part of a broader neural predisposition."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Retinoblastoma names the master cell-cycle brake that CDKN2A protects: RB1 loss removes the restraint on E2F that CDKN2A's p16 normally reinforces, so the two tumor-suppressors guard the same G1/S checkpoint that, when broken, unleashes cancer."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Retinoblastoma anchors the cyclin D-CDK-RB axis: cyclin D1 with CDK4/6 phosphorylates and inactivates the RB protein, releasing E2F to drive the cell cycle—so when RB1 is lost, this brake fails entirely, the defining lesion of the disease."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Eye-sparing retinoblastoma treatment includes radioactive iodine plaques: an I-125 episcleral plaque delivers localized radiation to the tumor while sparing the rest of the eye, one way to treat tumors and try to preserve vision short of removing the eye."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Retinal astrocytic hamartomas mimic retinoblastoma: these benign glial (astrocyte) tumors, often from tuberous sclerosis, can cause leukocoria too, so distinguishing them from retinoblastoma is a key part of evaluating a white pupil in a child."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Retinoblastoma can become 'trilateral' in the melatonin-making pineal gland: germline RB1 carriers develop pineoblastoma, a tumor of the pineal—the brain's light-sensing, melatonin-secreting organ—mirroring the eye's photoreceptor cancer."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Retinoblastoma is a vascular tumor treated through its blood supply: it expresses VEGF to grow vessels, and chemotherapy delivered straight into the ophthalmic artery (with anti-angiogenic strategies) targets the tumor while sparing the eye."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Retinoblastoma recruits tumor-associated macrophages: these infiltrating immune cells populate the tumor and may support its growth and survival, making the eye tumor's immune microenvironment a subject of study for new therapies."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium gives retinoblastoma away on imaging: the tumor characteristically calcifies, so flecks of calcium within an eye mass on ultrasound or CT are a key diagnostic clue in a child with leukocoria (white pupil)."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Retinoblastoma is being opened to cytotoxic T cells: long treated by local and chemo approaches, it is now studied for immunotherapy, with engineered T cells explored to attack the eye tumor and spare vision where possible."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Retinoblastoma can spread through the blood to the liver: beyond optic-nerve and CNS extension, hematogenous metastasis seeds organs including the liver, a sign of advanced disease that shifts treatment to intensive systemic therapy."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Retinoblastoma gives itself away by calcium phosphate: the tumor classically calcifies, and these calcium-phosphate flecks on ultrasound or CT are a key clue distinguishing it from other causes of a white pupil."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Retinoblastoma recruits endothelial cells to grow: VEGF from the tumor drives the new vessels that feed it within the eye, a target explored alongside the chemotherapy delivered into the eye's artery."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Hereditary retinoblastoma raises lifelong skin-cancer risk: survivors with a germline RB1 mutation face an elevated chance of melanoma and other second cancers, so skin surveillance joins their long-term care."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals retinoblastoma's photoreceptor roots: well-differentiated tumors form Flexner-Wintersteiner rosettes ringing a central lumen and sprout primitive light-sensing cilia, ultrastructure betraying their origin in the developing retina."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Retinoblastoma enlists the retina's own immune cells: tumor-associated microglia infiltrate the growing mass and, rather than fighting it, secrete factors that support its proliferation, with their density tracking more aggressive disease."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "When retinoblastoma escapes the eye it can reach the lung: though it usually spreads up the optic nerve to the brain or into the marrow, rare hematogenous metastases seed the lungs in advanced, treatment-resistant disease."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "A collagen sieve marks the point of no return: the lamina cribrosa, the collagen plate where the optic nerve leaves the eye, is the barrier retinoblastoma must breach, and tumor invasion beyond it sharply raises the risk of spread and worsens prognosis."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Curing retinoblastoma drains the red cells: the carboplatin-vincristine-etoposide chemotherapy suppresses the marrow, dropping the erythrocyte count into an anemia that may need transfusion support through treatment."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Platinum chemotherapy wastes magnesium: carboplatin injures the kidney's tubular handling of the mineral, so magnesium is monitored and replaced during the months of retinoblastoma treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains read the retinal tumor: because biopsy is avoided to prevent seeding, the diagnosis rests on imaging, but an enucleated eye stains with CRX and synaptophysin antibodies that confirm its photoreceptor-precursor, neuroendocrine origin."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The chemotherapy opens the door to infection: carboplatin, vincristine, and etoposide suppress the marrow, dropping neutrophil counts so that febrile neutropenia is a constant watch during a small child's retinoblastoma treatment."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Heritable retinoblastoma echoes into the next generation: a survivor of the germline form carries the RB1 mutation in every cell and passes it to about half their children, making genetic counseling and family screening central to care."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Radiation comes back to haunt survivors: heritable retinoblastoma carries a high lifetime risk of second cancers, and external-beam radiation to the head adds radiation-induced thyroid cancer to the osteosarcoma and melanoma these patients already face."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Systemic chemotherapy lowers the platelets: the carboplatin-etoposide-vincristine regimens used to shrink the tumor suppress platelet production into thrombocytopenia, so blood counts are watched and dosing adjusted through treatment."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The platinum chemotherapy taxes the kidneys: carboplatin used against retinoblastoma is cleared renally and can injure the tubules, wasting magnesium and other electrolytes that must be monitored in these small children."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "It must still solve the immortality problem: with RB1 lost, retinoblastoma reactivates telomerase via TERT to keep dividing, escaping the telomere shortening that would otherwise limit the runaway growth the missing checkpoint allows."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "The germline defect echoes in adulthood: heritable retinoblastoma survivors carry a lifelong raised risk of second cancers including bladder cancer, where RB1 loss is also a common driver — the same broken gene surfacing decades and organs apart."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate killers are enlisted against it: retinoblastoma is relatively immune-cold, so harnessing natural killer cells is among the immunotherapy strategies explored to spare the eye in tumors that resist chemotherapy."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Chemotherapy exposes the child to sepsis: the systemic carboplatin-etoposide-vincristine regimens drop neutrophils, so febrile neutropenia and bloodstream infection are constant dangers in treating these infants."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Radiation scars the young brain's vessels: external-beam radiation to the orbit and head in heritable retinoblastoma causes a late cerebral vasculopathy (including moyamoya) that raises stroke risk in survivors."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Central lines and chemotherapy clot the veins: the indwelling venous access and pro-thrombotic chemotherapy used in retinoblastoma treatment predispose to catheter-associated venous thromboembolism."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its cure can sow a second cancer: the etoposide and alkylators used against retinoblastoma — on a germline-RB1 background already prone to second malignancies — can cause therapy-related acute myeloid leukemia years later."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The platinum is hard on small kidneys: carboplatin and cisplatin central to retinoblastoma chemotherapy are nephrotoxic, and in a young child the tubular and electrolyte injury can leave lasting chronic kidney impairment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow suppression and chronic illness lower the count: intensive chemotherapy plus the inflammatory burden of an advanced tumor blunt erythropoiesis, adding an anemia-of-chronic-disease component to treatment-related cytopenias."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Germline RB1 loss seeds soft-tissue cancers later: hereditary retinoblastoma survivors carry a lifelong risk of second primary sarcomas, including rhabdomyosarcoma, especially within prior radiation fields."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its chemotherapy strips the lung's defenses: the systemic chemotherapy used to shrink retinoblastoma causes neutropenia in young children, allowing inhaled Aspergillus to invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Eye loss and an inherited cancer weigh on families: enucleation, disfigurement and the burden of a heritable cancer with lifelong second-tumor surveillance contribute to depression in survivors and their parents."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Enucleation is a healing challenge in a child: removing the eye and fitting an orbital implant leaves a socket that must heal, and chemotherapy and any orbital radiation slow and complicate that closure."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Chemotherapy reawakens shingles: the systemic chemotherapy for retinoblastoma suppresses a child's immunity, allowing latent or primary varicella-zoster to cause severe disseminated infection."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A heritable childhood cancer breeds lasting worry: vision loss, the genetic risk to future children and lifelong second-cancer surveillance after RB1 retinoblastoma foster chronic anxiety in survivors and families."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Radiation deforms the growing face and seeds sarcoma: orbital radiotherapy stunts midfacial bone growth, and germline RB1 carriers face a high risk of radiation-induced and spontaneous bone sarcomas."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its chemotherapy injures the gut: the systemic chemotherapy for retinoblastoma causes mucositis, nausea and, with some agents, hepatotoxicity in the young patient."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Enucleation and radiation mark the orbit: removing the eye leaves a socket fitted with a prosthesis, and orbital radiation thins and scars the periorbital skin and lashes."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its chemotherapy taxes the kidney: the carboplatin used to treat retinoblastoma is nephrotoxic and can cause electrolyte wasting, needing monitoring in small children."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Orbital radiation reaches the growing child: external-beam radiation for hereditary retinoblastoma can impair facial-bone growth and nearby endocrine structures and raises the risk of second cancers in the field."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Survivors face second cancers in the chest: hereditary retinoblastoma carriers have a high lifetime risk of second primary cancers including lung cancer, especially with smoking, and sarcomas."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Treatment can reach the heart: systemic chemotherapy for retinoblastoma, and the radiation given historically, carry long-term cardiovascular risk in survivors."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Therapy suppresses immunity: intensive chemotherapy for advanced retinoblastoma leaves children immunocompromised, and immunotherapy is being explored for refractory disease."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Extraocular spread reaches the nodes: when retinoblastoma extends beyond the eye, it can metastasise to preauricular and cervical lymph nodes, a marker of advanced disease."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemoreduction by route saves eyes: systemic carboplatin-vincristine-etoposide, intra-arterial melphalan, and intravitreal injection shrink retinoblastoma so focal therapy can preserve vision and avoid enucleation."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Rb loss defies CDK4/6 inhibitors: because retinoblastoma deletes RB1 itself, the target downstream of CDK4/6 is already gone, so CDK4/6 inhibitors that need intact Rb fail — the disease that named the pathway resists blocking it."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Survivors face bone sarcomas: children with heritable RB1 mutations, and those given external-beam radiotherapy, carry a high lifetime risk of osteosarcoma and radiation-induced bone sarcomas, often in the irradiated facial bones."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "A shared broken cell-cycle brake: retinoblastoma is defined by loss of RB1, while glioblastoma routinely inactivates the same RB pathway via CDKN2A loss or CDK4 gain—the founding tumour-suppressor circuit failing in a childhood and an adult cancer."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "It springs from a photoreceptor precursor: retinoblastoma arises from maturing cone precursors of the retina, the neurons that wire into the retinal ribbon synapses—linking the tumour to the synaptic machinery of vision."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Borrowing neuroblastoma's target: retinoblastoma expresses the disialoganglioside GD2, so GD2-directed CAR-T cells developed against neuroblastoma are being explored for refractory intraocular and metastatic retinoblastoma."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Optic nerve and CNS spread: retinoblastoma invades the optic nerve and tracks along its axons into the CNS, so optic-nerve involvement at the resection margin is the key prognostic factor and route to fatal leptomeningeal disease."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "Two embryonal childhood cancers: retinoblastoma (RB1, eye) and Wilms tumour (WT1, kidney) are both classic tumours of infancy, paradigms of inherited and developmental cancer."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Metastatic spread to the liver: extraocular retinoblastoma seeds the liver and bone marrow, depositing in the hepatic lobule in the disseminated disease that dominates late presentations in low-resource settings."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Radiation-induced second tumour: hereditary retinoblastoma survivors treated with external-beam radiotherapy face a raised risk of meningioma in the radiation field decades later, a survivorship hazard like that in Li-Fraumeni."
  - target: 01-human/07-system/prostate-cancer
    relation: connects-to
    note: "RB1 across cancers: loss of RB1, the gene behind retinoblastoma, also drives treatment-emergent neuroendocrine prostate cancer and small-cell transformation, the same tumour suppressor failing in very different tissues."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Second cancers of survivors: germline RB1 carriers face a high lifetime risk of second malignancies including soft-tissue sarcomas such as synovial sarcoma, especially within prior radiation fields."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified aggression: MYC and MYCN amplification mark aggressive retinoblastomas, including rare RB1-wild-type tumours driven by MYCN amplification alone."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis-resistant origin: the cone-precursor cell of origin highly expresses anti-apoptotic BCL-2 and MDM2, helping retinoblastoma cells survive despite RB1 loss."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dependence: EZH2/polycomb activity helps maintain the proliferative, dedifferentiated state of retinoblastoma, a candidate epigenetic vulnerability."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival signalling: PI3K/AKT activation helps retinoblastoma cells survive and proliferate downstream of RB1 loss, a candidate combination target."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Growth-signal hub: mTOR drives the protein synthesis and growth of retinoblastoma cells, integrating the proliferative signalling unleashed by RB1 inactivation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the hypoxic intraocular retinoblastoma drives the VEGF angiogenesis that supports its growth within the eye."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptotic evasion: retinoblastoma resists caspase-3-mediated apoptosis through high BCL-2 and survivin, the basis for chemoresistance and the rationale for pro-apoptotic agents added to intra-arterial chemotherapy."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CNS dissemination: CXCR4 on retinoblastoma cells responds to CXCL12 gradients along the optic nerve and meninges, contributing to the extraocular and central-nervous-system spread that worsens prognosis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Invasion marker: osteopontin is upregulated in retinoblastoma and correlates with optic-nerve invasion, the key histological feature that signals high-risk disease and the need for adjuvant chemotherapy."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Cell of origin: retinoblastoma arises from a cone-precursor cell whose fate and proliferation are patterned by Notch signalling during retinal development, the developmental context in which RB1 loss unleashes uncontrolled division."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Tumour-associated macrophages: CCL2 recruits the macrophages found within retinoblastoma, a myeloid infiltrate that supports angiogenesis and invasion and is being studied as part of the tumour microenvironment beyond the malignant cells themselves."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neurotrophin survival: retinoblastoma cells express TrkB and respond to BDNF with pro-survival signalling, a neurotrophic dependency inherited from their neural-retina origin that helps the tumour resist apoptosis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Survival signalling: PI3K-AKT-mTOR activity supports retinoblastoma cell survival and growth downstream of the deregulated RB-E2F proliferation, complementing the AKT and mTOR already mapped as a targetable dependency."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor dependence: IGF-1/IGF-1R signalling is expressed in retinoblastoma and drives proliferation and survival, a growth-factor axis under study as a therapeutic target in this childhood retinal tumour."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic progression: retinoblastoma carries strikingly few genetic lesions beyond RB1 loss and instead advances through widespread epigenetic deregulation, including DNA-methylation changes effected by DNMTs such as DNMT3A."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Survival signalling: PTEN restrains the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) that supports the survival of retinoblastoma cells and is a candidate therapeutic target."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Growth-factor MAPK: IGF-1R signalling (IGF-1 mapped) feeds the MAPK-ERK cascade that supports proliferation and survival in retinoblastoma."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Pro-survival STAT3: STAT3 signalling promotes the survival and chemoresistance of retinoblastoma cells, complementing the loss of RB-mediated cell-cycle control."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferation: RAS-ERK signalling (ERK1/2 already mapped) provides a proliferative input cooperating with RB1 loss and MYCN amplification in retinoblastoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Upstream of STAT3: JAK kinases signal to STAT3 (already mapped), the survival pathway whose activity sustains retinoblastoma-cell chemoresistance."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Survival signalling: NF-κB-driven survival and inflammatory signalling supports the growth of retinoblastoma and contributes to chemoresistance."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the invasion and survival of retinoblastoma cells."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling modulates the proliferation and microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune surveillance of the RB1-driven retinoblastoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the differentiation and microenvironment of the retinal-progenitor-derived cells of retinoblastoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by the PI3K-AKT axis, modulate the survival and oxidative-stress balance of retinoblastoma cells."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the MYCN stability and survival signaling of retinoblastoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is a component of the immune response to retinoblastoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the tumor microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the survival and invasion of retinoblastoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of retinoblastoma cells."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of retinoblastoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of retinoblastoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of retinoblastoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neurotrophin survival: retinoblastoma cells express the TrkB receptor for BDNF (BDNF already mapped), and this neurotrophin signalling supports tumour-cell survival and chemoresistance, a targetable axis in this photoreceptor-derived cancer."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Cone-precursor origin: retinoblastoma arises from cone photoreceptor precursors whose identity depends on thyroid-hormone-receptor (TRbeta) signalling, tying the tumour's cell of origin to thyroid-hormone-driven cone specification in the developing retina."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune-cold tumour: retinoblastoma grows in the immune-privileged eye with low MHC class II antigen presentation, limiting T-cell recognition, a barrier to the immunotherapies increasingly explored for refractory and metastatic disease."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cellular immunotherapy: IL-2-driven T-cell expansion supports the CAR-T and adoptive approaches (GD2 and others) being explored for refractory or metastatic retinoblastoma, which resists immune attack in its privileged ocular site (MHC class II already mapped)."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint context: PD-1 checkpoint blockade is of limited benefit in the immune-cold, low-mutation retinoblastoma, motivating combination strategies for the rare metastatic cases that escape local control."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Chemotherapy myelosuppression: the systemic and intra-arterial chemotherapy used to preserve the eye in retinoblastoma is myelosuppressive, lowering haemoglobin and requiring supportive care in these young children."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Chemotherapy cardiotoxicity: the carboplatin and, in extraocular disease, anthracycline-containing regimens for retinoblastoma carry cardiotoxic risk, and troponin elevation helps detect the myocardial injury threatening these very young survivors."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 helps make retinoblastoma an immunologically cold, low-mutation tumour (PD-1 already mapped), dampening the T-cell response, which limits the benefit of checkpoint blockade in the rare metastatic cases."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and lysis stress: chemotherapy of retinoblastoma generates oxidative stress and, in bulky disease, rapid cell lysis releasing purines that xanthine oxidase converts to uric acid, contributing to tumour-lysis and oxidative burden."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, low-mutation microenvironment of retinoblastoma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the systemic chemotherapy of retinoblastoma is myelosuppressive, causing anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the young child with iron."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of retinoblastoma, part of the stromal microenvironment of this intraocular tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immune microenvironment of the intraocular retinoblastoma."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the tumour-associated macrophages (already mapped) and the cyclooxygenase pathway (IL-6 and IL-1 already mapped) contribute to the inflammatory microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin adds an anaemia of chronic disease to the chemotherapy anaemia (iron and haemoglobin already mapped) of retinoblastoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic microenvironment: leptin from the marrow and stromal adipose tissue signals within the metabolic microenvironment of the metastatic/chemotherapy-treated retinoblastoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipose adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the metabolic microenvironment of the metastatic retinoblastoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic milieu of retinoblastoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the emerging immunotherapy of retinoblastoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of retinoblastoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the retinoblastoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the retinoblastoma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of retinoblastoma."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the tumour antigen to the T cells (already mapped) shaping the adaptive immune response against retinoblastoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of retinoblastoma."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of retinoblastoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tumour complement: the complement C3 activation contributes to the inflammatory dimension of the intraocular retinoblastoma microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment into the retinoblastoma microenvironment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chemotherapy anaemia support: erythropoietin corrects the anaemia from VAC-based chemotherapy in retinoblastoma, and EPOR expression on retinal progenitor cells hints at a developmental role in the retinoblastoma cell of origin."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Intraocular mast-cell mediator: histamine from intraocular mast cells promotes the angiogenesis (VEGF already mapped) and the vascular permeability that sustain the highly vascular growth pattern of retinoblastoma within the vitreous."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Blood-ocular-barrier modulation: bradykinin B2-receptor agonists increase the permeability of the blood-ocular barrier, a pharmacological strategy explored to enhance intra-arterial and intravitreal chemotherapy delivery in retinoblastoma."
---

# Retinoblastoma

## Overview

**Retinoblastoma** is the most common primary **intraocular malignancy of childhood**, arising from immature retinal progenitor cells of the inner nuclear layer. It occurs in approximately **1 in 15,000-20,000** live births worldwide and accounts for ~3% of all childhood cancers. Retinoblastoma is the paradigmatic tumor for **Knudson's two-hit hypothesis** (1971): the observation that bilateral (hereditary) retinoblastoma required both germline and somatic RB1 inactivation, while unilateral (sporadic) retinoblastoma required two independent somatic hits in the same cell, established the concept of tumor suppressor gene LOF. Retinoblastoma occurs in two forms: **bilateral/hereditary (~40%)** from germline RB1 pathogenic variants, and **unilateral/sporadic (~60%)** from somatic biallelic RB1 inactivation. Modern therapy has transformed retinoblastoma from a blinding and frequently lethal disease to one with >95% overall survival and high rates of globe salvage [^knudson-1971-two-hit] [^shields-2008-retinoblastoma].

**Retinoblastoma characteristics by hereditary status:**

| Feature | Bilateral (hereditary) | Unilateral (usually sporadic) |
|---|---|---|
| Genetic basis | Germline RB1 + somatic LOH | Two somatic RB1 hits |
| Frequency | ~40% of all retinoblastoma | ~60% of all retinoblastoma |
| Age at diagnosis | Median 12-15 months | Median 24-30 months |
| Laterality | Bilateral, often multifocal | Unilateral, unifocal |
| Second malignancy risk | 30-50× elevated | Not elevated above population |
| De novo germline | ~25% of hereditary cases | — |
| Offspring risk | 50% (autosomal dominant) | <1% (germline test negative) |

## Structure

### RB1 gene and protein biology

**RB1 gene (13q14.2):**
- 200 kb, 27 exons; encodes 928 aa (110 kDa) pRb protein
- Germline pathogenic variant spectrum: truncating variants (frameshift ~35%, nonsense ~20%, splice ~15%); missense in conserved pocket residues (~20%); large deletions (MLPA required, ~10%)
- De novo germline: ~25% of bilateral cases; test both parents
- Penetrance: nearly 100% for bilateral retinoblastoma in germline RB1 carriers; ~10% of germline RB1 carriers develop only unilateral (incomplete penetrance)
- Low-penetrance alleles: missense at Arg552 (R552Q), splice-site variants with partial exon skipping, deep intronic variants → reduced pRb expression → incomplete penetrance; risk of unilateral retinoblastoma + reduced second cancer risk

**MYCN-amplified retinoblastoma:**
- ~2% of retinoblastoma (predominantly unilateral sporadic); RB1 wildtype at diagnosis; MYCN amplification (50-200× copies) drives retinal progenitor proliferation via a different mechanism; aggressive histology; less globe-salvageable than RB1-mutant tumors; genetic counseling: not hereditary (germline MYCN not found)
- Represents an RB-independent mechanism of retinoblastoma: CDK2-CyclinE hyperactivation secondary to MYCN (which activates CCNE1) → Rb hyperphosphorylation → E2F1 release despite intact RB1

### Tumor biology

**Cell of origin:** inner nuclear layer retinal progenitor cells (RPC) in the retina; these mitotically active cells in fetal/early postnatal retina require Rb for exit from the cell cycle; Rb depletion → RPCs cannot exit proliferation → tumor formation. Specifically, cone precursors (identified by Rb−/− mouse models and gene expression) appear most susceptible; human retinoblastoma expresses cone photoreceptor markers (RXRγ, IRBPα, OPN1MW/LW).

**Molecular alterations beyond RB1:**
- **MDM2 amplification** (~4%): suppresses E2F1-induced p53-dependent apoptosis
- **MDM4 overexpression** (~65%): MDM4 (MDMX) inhibits p53 independently of MDM2; the most common mechanism by which retinoblastoma bypasses E2F1-induced apoptosis
- **MYCN amplification** (~2%; see above)
- **CDK4 amplification** (~2%): bypasses Rb if RB1 wild-type
- Genome is otherwise relatively quiet (few mutations); retinoblastoma is genomically simple compared to adult carcinomas; anaplastic retinoblastoma (rare) has copy number gains in 2p, 6p, 13q gain with additional TP53 mutations

## Function

### Clinical presentation and staging

**Leukocoria (white pupillary reflex):** the classic presenting sign; caused by the white tumor mass seen through the pupil; first noticed in photographs (loss of red-eye reflex on one side); median age at diagnosis ~12-18 months (bilateral) or ~24-30 months (unilateral)

**Other presentations:**
- Strabismus (esotropia or exotropia): tumor disrupts foveal fixation
- Vision loss: less commonly noticed in infants; detected on developmental assessment
- Proptosis: indicates extraocular extension; poor prognostic sign
- Glaucoma, uveitis: late or advanced presentation
- Orbital and systemic metastasis: bone marrow, CSF, lymph nodes — uncommon in high-income countries but common at diagnosis in resource-limited settings (presenting with systemic disease in ~10% globally)

**International Intraocular Retinoblastoma Classification (IIRC), Groups A-E:**
- **Group A**: small tumors (≤3 mm), away from fovea and disc, no vitreous/subretinal seeding → focal therapy (laser, cryotherapy)
- **Group B**: larger tumors or subfoveal/juxtapapillary location, no seeding → primary chemotherapy + focal
- **Group C**: focal vitreous or subretinal seeding → systemic or intra-arterial chemotherapy
- **Group D**: diffuse vitreous or subretinal seeding → intra-arterial + intravitreal chemotherapy; globe salvage possible but challenging
- **Group E**: extensive tumor, neovascular glaucoma, opaque media, tumor anterior to anterior vitreous face → enucleation often required

## Pathology

### Treatment modalities

**1. Systemic chemotherapy (chemoreduction):**
Standard regimen: **vincristine + carboplatin + etoposide (VCE)**, 6 cycles; reduces tumor size → enables focal consolidation; primary treatment for bilateral disease; long-term ototoxicity risk from carboplatin (audiologic monitoring)

**2. Intra-arterial chemotherapy (IAC) — ophthalmic artery chemosurgery:**
- Interventional neuroradiology: selective catheterization of ophthalmic artery via femoral approach → melphalan ± carboplatin ± topotecan infused directly into the eye
- Globe salvage rates: Group D eyes: ~60-80% globe retention with IAC vs ~30-40% historically; transformative advance since ~2008
- Advantages: high intravitreal drug concentration, minimal systemic exposure; Disadvantages: arterial risk (stroke, occlusion, rare); radiation exposure of procedure; not suitable for all anatomies
- Bilateral IAC: sequential sessions, one eye per session

**3. Intravitreal chemotherapy (IVitC):**
- Direct injection into vitreous: melphalan (20-30 μg) ± topotecan; specifically treats vitreous seeding (Group C/D)
- Historically avoided due to extraocular spread risk → now performed with safety protocols (avoidance of reflux, immediate cryotherapy of injection site)
- Melphalan kills both clonal and floating seed tumor cells in vitreous cavity
- Combined with IAC for vitreous disease: highest salvage for Group D

**4. Focal therapy (consolidation):**
- **Laser photocoagulation (diode laser, 810 nm)**: direct ablation of small tumors + tumoral blood supply; used after chemoreduction
- **Transpupillary thermotherapy (TTT)**: lower energy laser → hyperthermia → tumor cell death
- **Cryotherapy**: double freeze-thaw cycles; for anterior tumors ≤4 mm

**5. External beam radiotherapy (EBRT):**
- Highly effective (95%+ local control) but **avoided in hereditary retinoblastoma** due to dramatically increased second malignancy risk in the radiation field (20-50× osteosarcoma/STS in irradiated orbits in hereditary RB patients)
- Reserved for: failed all globe-preserving options, unresectable extraocular extension; only when absolutely necessary
- Proton therapy: can minimize scatter to orbit, reducing but not eliminating secondary cancer risk

**6. Enucleation:**
- Removal of the globe; curative for the treated eye; standard for Group E, unilateral disease with no useful vision, or failed globe-preserving therapy
- High-quality prosthetic eye; no visual rehabilitation possible in enucleated eye
- Pathological examination of enucleation specimen: assess optic nerve resection margin, choroidal invasion (>3 mm), scleral invasion → high-risk features → adjuvant systemic chemotherapy

### Hereditary retinoblastoma long-term management

**Second malignancy surveillance:**
- Risk: hereditary RB1 carriers have ~50-fold elevated lifetime risk of second malignancies, predominantly in bone (osteosarcoma), soft tissue (sarcoma), CNS, and melanoma
- Without prior EBRT: ~40% lifetime second malignancy risk (cumulative by age 50)
- With prior EBRT: ~80%+ risk in irradiated field; EBRT dramatically amplifies second cancer risk → primary reason EBRT is now avoided
- Surveillance: annual whole-body MRI from age 5-7 onward; clinical exam; no established consensus but NCCN and international groups recommend continued lifelong surveillance

**Genetic counseling for offspring:**
- Hereditary RB1 carrier: 50% risk to each child; recommend: ophthalmologic exam under anesthesia (EUA) for all infants of carriers beginning at birth/1 month; germline RB1 testing of infant before EUA allows stratification
- EUA schedule (hereditary risk): every 3-4 weeks under anesthesia during first 12-18 months of life; frequency reduced after age 3-4 (when retinal progenitors differentiate and risk window closes); continue annually until age 7

## Connections

- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — E2F1 is released constitutively when RB1 is biallelically lost in retinoblastoma; unchecked E2F1 drives retinal progenitor proliferation → tumor mass; retinoblastoma cells have MYCN amplification and additional mutations that cooperate with E2F1 dysregulation.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Biallelic RB1 loss is the universal initiating event in retinoblastoma; hereditary (bilateral) = germline RB1 + somatic LOH; sporadic (unilateral) = two somatic RB1 hits; MYCN amplification is an alternative RB-independent driver in a rare subset.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 pathway is bypassed in retinoblastoma via MDM2 amplification, MDM4 overexpression, or MYCN amplification; p53 pathway loss allows retinal progenitors to survive RB1 LOF-driven E2F1 pro-apoptotic signaling; TP53 mutations are rare in primary retinoblastoma.
- `connects-to` → **[Osteosarcoma](../../07-system/osteosarcoma/README.md)** — Hereditary RB1 carriers have 30-50× risk of osteosarcoma as a second malignancy; radiation exposure dramatically amplifies this risk — external beam RT now avoided in hereditary RB; germline RB1 is found in ~3-5% of sporadic osteosarcomas.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Retinoblastoma is the most common intraocular tumor of childhood, presenting as leukocoria (white pupillary reflex) or strabismus; globe-sparing therapy — intra-arterial and intravitreal chemotherapy — salvages most eyes, reserving enucleation for advanced (Group E) disease.
- `connects-to` → **[MYCN](../../03-molecular/mycn/README.md)** — A small (~2%) RB1-wildtype subset of retinoblastoma is instead driven by massive MYCN amplification, which raises CCNE1/CDK2 to hyperphosphorylate Rb and release E2F1 despite intact RB1; these aggressive, non-hereditary tumors are harder to salvage than RB1-mutant ones.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — Retinoblastoma must neutralize the p53 apoptosis that RB1 loss would otherwise trigger: MDM2 amplification (~4%) and MDM4 overexpression (~65%) degrade or inhibit p53, so TP53 itself is rarely mutated — making MDM2/MDM4 antagonists a rational therapeutic strategy.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Retinoblastoma arises from a neuron: the developing cone photoreceptor precursor, which depends on RB1 to restrain proliferation; biallelic RB1 loss unleashes E2F-driven division, why the tumor is so specific to the retina despite RB1 being lost in every cell of carriers.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Germline retinoblastoma carries a brain risk: trilateral retinoblastoma is a pineoblastoma or suprasellar PNET — an intracranial embryonal tumor sharing the retina photoreceptor lineage — arising in a few percent of bilateral RB patients, prompting routine brain MRI surveillance.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Retinoblastoma and Li-Fraumeni are the paradigm hereditary cancer-predisposition syndromes built on tumor-suppressor loss: RB1 (the first tumor suppressor found, basis of Knudson's two-hit hypothesis) versus TP53; both inherit one bad allele and need only a somatic second hit.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy has a fraught role in retinoblastoma: external-beam photon radiation can control the tumor and save the eye, but in heritable RB1-mutant children it sharply raises second-cancer risk (especially osteosarcoma) in the field—so it is now largely avoided.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — Retinoblastoma and small cell lung cancer are united by RB1 loss: the tumor-suppressor that, germline-mutated, causes childhood retinoblastoma is inactivated (with TP53) in nearly all small cell lung cancers—one gene across utterly different cancers.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Survivors of heritable retinoblastoma face a lifelong excess of second cancers including melanoma: the germline RB1 mutation in every cell, compounded by radiotherapy, predisposes to melanoma and sarcomas decades later—so survivorship means lifelong surveillance.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — Retinoblastoma and uveal melanoma are primary intraocular malignancies at opposite ages: retinoblastoma is a childhood RB1-driven retinal tumor causing leukocoria, while uveal melanoma is an adult GNAQ/BAP1-driven choroidal tumor—differing in cell, age and genetics.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Retinoblastoma and neuroblastoma are both embryonal childhood tumors with eye signs: retinoblastoma causes leukocoria from a retinal tumor, while neuroblastoma causes periorbital metastases and opsoclonus—different origins, overlapping pediatric presentations.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Retinoblastoma links to medulloblastoma through trilateral retinoblastoma: heritable RB1 loss can produce bilateral eye tumors plus a midline brain PNET (pineoblastoma), so RB1, like other embryonal-tumor genes, can seed both retinal and CNS neuroectodermal tumors.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Retinoblastoma is the namesake of the RB-CDK4/6 cell-cycle brake: the RB protein normally blocks CDK4/6-cyclin D from pushing cells past the G1 checkpoint, so its loss removes that brake—the same axis CDK4/6 inhibitors restore in other RB-intact cancers.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Advanced retinoblastoma spreads to the bone marrow and CNS: untreated, it extends along the optic nerve into the brain and disseminates to marrow, so metastatic workup and intrathecal/systemic therapy are added when the tumor breaches the eye.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Hereditary retinoblastoma survivors face lifelong second-cancer risk: germline RB1 loss predisposes to sarcomas, melanoma and later epithelial cancers (worsened by past radiotherapy)—and RB1 is itself lost in many breast cancers, tying the genes together.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy is preferred when retinoblastoma needs external radiation: in heritable RB1 patients, who are highly prone to radiation-induced second cancers, protons' sharp dose falloff spares orbital bone and brain, lowering that lifelong risk.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Retinoblastoma is a tumor of the developing nervous system's retina: arising from retinal precursor cells, heritable RB1 loss can also produce an intracranial pineal tumor ('trilateral retinoblastoma'), so the eye lesion is part of a broader neural predisposition.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Retinoblastoma names the master cell-cycle brake that CDKN2A protects: RB1 loss removes the restraint on E2F that CDKN2A's p16 normally reinforces, so the two tumor-suppressors guard the same G1/S checkpoint that, when broken, unleashes cancer.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Retinoblastoma anchors the cyclin D-CDK-RB axis: cyclin D1 with CDK4/6 phosphorylates and inactivates the RB protein, releasing E2F to drive the cell cycle—so when RB1 is lost, this brake fails entirely, the defining lesion of the disease.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Eye-sparing retinoblastoma treatment includes radioactive iodine plaques: an I-125 episcleral plaque delivers localized radiation to the tumor while sparing the rest of the eye, one way to treat tumors and try to preserve vision short of removing the eye.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Retinal astrocytic hamartomas mimic retinoblastoma: these benign glial (astrocyte) tumors, often from tuberous sclerosis, can cause leukocoria too, so distinguishing them from retinoblastoma is a key part of evaluating a white pupil in a child.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Retinoblastoma can become 'trilateral' in the melatonin-making pineal gland: germline RB1 carriers develop pineoblastoma, a tumor of the pineal—the brain's light-sensing, melatonin-secreting organ—mirroring the eye's photoreceptor cancer.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Retinoblastoma is a vascular tumor treated through its blood supply: it expresses VEGF to grow vessels, and chemotherapy delivered straight into the ophthalmic artery (with anti-angiogenic strategies) targets the tumor while sparing the eye.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Retinoblastoma recruits tumor-associated macrophages: these infiltrating immune cells populate the tumor and may support its growth and survival, making the eye tumor's immune microenvironment a subject of study for new therapies.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium gives retinoblastoma away on imaging: the tumor characteristically calcifies, so flecks of calcium within an eye mass on ultrasound or CT are a key diagnostic clue in a child with leukocoria (white pupil).
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Retinoblastoma is being opened to cytotoxic T cells: long treated by local and chemo approaches, it is now studied for immunotherapy, with engineered T cells explored to attack the eye tumor and spare vision where possible.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Retinoblastoma can spread through the blood to the liver: beyond optic-nerve and CNS extension, hematogenous metastasis seeds organs including the liver, a sign of advanced disease that shifts treatment to intensive systemic therapy.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Retinoblastoma gives itself away by calcium phosphate: the tumor classically calcifies, and these calcium-phosphate flecks on ultrasound or CT are a key clue distinguishing it from other causes of a white pupil.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Retinoblastoma recruits endothelial cells to grow: VEGF from the tumor drives the new vessels that feed it within the eye, a target explored alongside the chemotherapy delivered into the eye's artery.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Hereditary retinoblastoma raises lifelong skin-cancer risk: survivors with a germline RB1 mutation face an elevated chance of melanoma and other second cancers, so skin surveillance joins their long-term care.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals retinoblastoma's photoreceptor roots: well-differentiated tumors form Flexner-Wintersteiner rosettes ringing a central lumen and sprout primitive light-sensing cilia, ultrastructure betraying their origin in the developing retina.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Retinoblastoma enlists the retina's own immune cells: tumor-associated microglia infiltrate the growing mass and, rather than fighting it, secrete factors that support its proliferation, with their density tracking more aggressive disease.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — When retinoblastoma escapes the eye it can reach the lung: though it usually spreads up the optic nerve to the brain or into the marrow, rare hematogenous metastases seed the lungs in advanced, treatment-resistant disease.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — A collagen sieve marks the point of no return: the lamina cribrosa, the collagen plate where the optic nerve leaves the eye, is the barrier retinoblastoma must breach, and tumor invasion beyond it sharply raises the risk of spread and worsens prognosis.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Curing retinoblastoma drains the red cells: the carboplatin-vincristine-etoposide chemotherapy suppresses the marrow, dropping the erythrocyte count into an anemia that may need transfusion support through treatment.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Platinum chemotherapy wastes magnesium: carboplatin injures the kidney's tubular handling of the mineral, so magnesium is monitored and replaced during the months of retinoblastoma treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains read the retinal tumor: because biopsy is avoided to prevent seeding, the diagnosis rests on imaging, but an enucleated eye stains with CRX and synaptophysin antibodies that confirm its photoreceptor-precursor, neuroendocrine origin.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The chemotherapy opens the door to infection: carboplatin, vincristine, and etoposide suppress the marrow, dropping neutrophil counts so that febrile neutropenia is a constant watch during a small child's retinoblastoma treatment.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Heritable retinoblastoma echoes into the next generation: a survivor of the germline form carries the RB1 mutation in every cell and passes it to about half their children, making genetic counseling and family screening central to care.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Radiation comes back to haunt survivors: heritable retinoblastoma carries a high lifetime risk of second cancers, and external-beam radiation to the head adds radiation-induced thyroid cancer to the osteosarcoma and melanoma these patients already face.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Systemic chemotherapy lowers the platelets: the carboplatin-etoposide-vincristine regimens used to shrink the tumor suppress platelet production into thrombocytopenia, so blood counts are watched and dosing adjusted through treatment.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The platinum chemotherapy taxes the kidneys: carboplatin used against retinoblastoma is cleared renally and can injure the tubules, wasting magnesium and other electrolytes that must be monitored in these small children.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — It must still solve the immortality problem: with RB1 lost, retinoblastoma reactivates telomerase via TERT to keep dividing, escaping the telomere shortening that would otherwise limit the runaway growth the missing checkpoint allows.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — The germline defect echoes in adulthood: heritable retinoblastoma survivors carry a lifelong raised risk of second cancers including bladder cancer, where RB1 loss is also a common driver — the same broken gene surfacing decades and organs apart.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Innate killers are enlisted against it: retinoblastoma is relatively immune-cold, so harnessing natural killer cells is among the immunotherapy strategies explored to spare the eye in tumors that resist chemotherapy.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Chemotherapy exposes the child to sepsis: the systemic carboplatin-etoposide-vincristine regimens drop neutrophils, so febrile neutropenia and bloodstream infection are constant dangers in treating these infants.
- `connects-to` → **[Stroke](../stroke/README.md)** — Radiation scars the young brain's vessels: external-beam radiation to the orbit and head in heritable retinoblastoma causes a late cerebral vasculopathy (including moyamoya) that raises stroke risk in survivors.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Central lines and chemotherapy clot the veins: the indwelling venous access and pro-thrombotic chemotherapy used in retinoblastoma treatment predispose to catheter-associated venous thromboembolism.
- `connects-to` → **[AML](../aml/README.md)** — Its cure can sow a second cancer: the etoposide and alkylators used against retinoblastoma — on a germline-RB1 background already prone to second malignancies — can cause therapy-related acute myeloid leukemia years later.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The platinum is hard on small kidneys: carboplatin and cisplatin central to retinoblastoma chemotherapy are nephrotoxic, and in a young child the tubular and electrolyte injury can leave lasting chronic kidney impairment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow suppression and chronic illness lower the count: intensive chemotherapy plus the inflammatory burden of an advanced tumor blunt erythropoiesis, adding an anemia-of-chronic-disease component to treatment-related cytopenias.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Germline RB1 loss seeds soft-tissue cancers later: hereditary retinoblastoma survivors carry a lifelong risk of second primary sarcomas, including rhabdomyosarcoma, especially within prior radiation fields.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its chemotherapy strips the lung's defenses: the systemic chemotherapy used to shrink retinoblastoma causes neutropenia in young children, allowing inhaled Aspergillus to invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Eye loss and an inherited cancer weigh on families: enucleation, disfigurement and the burden of a heritable cancer with lifelong second-tumor surveillance contribute to depression in survivors and their parents.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Enucleation is a healing challenge in a child: removing the eye and fitting an orbital implant leaves a socket that must heal, and chemotherapy and any orbital radiation slow and complicate that closure.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Chemotherapy reawakens shingles: the systemic chemotherapy for retinoblastoma suppresses a child's immunity, allowing latent or primary varicella-zoster to cause severe disseminated infection.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A heritable childhood cancer breeds lasting worry: vision loss, the genetic risk to future children and lifelong second-cancer surveillance after RB1 retinoblastoma foster chronic anxiety in survivors and families.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Radiation deforms the growing face and seeds sarcoma: orbital radiotherapy stunts midfacial bone growth, and germline RB1 carriers face a high risk of radiation-induced and spontaneous bone sarcomas.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its chemotherapy injures the gut: the systemic chemotherapy for retinoblastoma causes mucositis, nausea and, with some agents, hepatotoxicity in the young patient.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Enucleation and radiation mark the orbit: removing the eye leaves a socket fitted with a prosthesis, and orbital radiation thins and scars the periorbital skin and lashes.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its chemotherapy taxes the kidney: the carboplatin used to treat retinoblastoma is nephrotoxic and can cause electrolyte wasting, needing monitoring in small children.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Orbital radiation reaches the growing child: external-beam radiation for hereditary retinoblastoma can impair facial-bone growth and nearby endocrine structures and raises the risk of second cancers in the field.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Survivors face second cancers in the chest: hereditary retinoblastoma carriers have a high lifetime risk of second primary cancers including lung cancer, especially with smoking, and sarcomas.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Treatment can reach the heart: systemic chemotherapy for retinoblastoma, and the radiation given historically, carry long-term cardiovascular risk in survivors.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Therapy suppresses immunity: intensive chemotherapy for advanced retinoblastoma leaves children immunocompromised, and immunotherapy is being explored for refractory disease.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Extraocular spread reaches the nodes: when retinoblastoma extends beyond the eye, it can metastasise to preauricular and cervical lymph nodes, a marker of advanced disease.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemoreduction by route saves eyes: systemic carboplatin-vincristine-etoposide, intra-arterial melphalan, and intravitreal injection shrink retinoblastoma so focal therapy can preserve vision and avoid enucleation.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Rb loss defies CDK4/6 inhibitors: because retinoblastoma deletes RB1 itself, the target downstream of CDK4/6 is already gone, so CDK4/6 inhibitors that need intact Rb fail — the disease that named the pathway resists blocking it.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Survivors face bone sarcomas: children with heritable RB1 mutations, and those given external-beam radiotherapy, carry a high lifetime risk of osteosarcoma and radiation-induced bone sarcomas, often in the irradiated facial bones.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — A shared broken cell-cycle brake: retinoblastoma is defined by loss of RB1, while glioblastoma routinely inactivates the same RB pathway via CDKN2A loss or CDK4 gain—the founding tumour-suppressor circuit failing in a childhood and an adult cancer.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — It springs from a photoreceptor precursor: retinoblastoma arises from maturing cone precursors of the retina, the neurons that wire into the retinal ribbon synapses—linking the tumour to the synaptic machinery of vision.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Borrowing neuroblastoma's target: retinoblastoma expresses the disialoganglioside GD2, so GD2-directed CAR-T cells developed against neuroblastoma are being explored for refractory intraocular and metastatic retinoblastoma.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Optic nerve and CNS spread: retinoblastoma invades the optic nerve and tracks along its axons into the CNS, so optic-nerve involvement at the resection margin is the key prognostic factor and route to fatal leptomeningeal disease.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — Two embryonal childhood cancers: retinoblastoma (RB1, eye) and Wilms tumour (WT1, kidney) are both classic tumours of infancy, paradigms of inherited and developmental cancer.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Metastatic spread to the liver: extraocular retinoblastoma seeds the liver and bone marrow, depositing in the hepatic lobule in the disseminated disease that dominates late presentations in low-resource settings.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Radiation-induced second tumour: hereditary retinoblastoma survivors treated with external-beam radiotherapy face a raised risk of meningioma in the radiation field decades later, a survivorship hazard like that in Li-Fraumeni.
- `connects-to` → **[Prostate Cancer](../prostate-cancer/README.md)** — RB1 across cancers: loss of RB1, the gene behind retinoblastoma, also drives treatment-emergent neuroendocrine prostate cancer and small-cell transformation, the same tumour suppressor failing in very different tissues.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Second cancers of survivors: germline RB1 carriers face a high lifetime risk of second malignancies including soft-tissue sarcomas such as synovial sarcoma, especially within prior radiation fields.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified aggression: MYC and MYCN amplification mark aggressive retinoblastomas, including rare RB1-wild-type tumours driven by MYCN amplification alone.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Apoptosis-resistant origin: the cone-precursor cell of origin highly expresses anti-apoptotic BCL-2 and MDM2, helping retinoblastoma cells survive despite RB1 loss.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dependence: EZH2/polycomb activity helps maintain the proliferative, dedifferentiated state of retinoblastoma, a candidate epigenetic vulnerability.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Survival signalling: PI3K/AKT activation helps retinoblastoma cells survive and proliferate downstream of RB1 loss, a candidate combination target.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Growth-signal hub: mTOR drives the protein synthesis and growth of retinoblastoma cells, integrating the proliferative signalling unleashed by RB1 inactivation.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the hypoxic intraocular retinoblastoma drives the VEGF angiogenesis that supports its growth within the eye.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Retinoblastoma resists caspase-3-mediated apoptosis through high BCL-2 and survivin expression, the basis for its chemoresistance and the rationale for pro-apoptotic agents added to the intra-arterial chemotherapy used to salvage eyes.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on retinoblastoma cells responds to CXCL12 gradients along the optic nerve and meninges, contributing to the extraocular and central-nervous-system spread that transforms a curable intraocular tumor into life-threatening disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin is upregulated in retinoblastoma and correlates with optic-nerve invasion—the key histological feature that signals high-risk disease and dictates whether adjuvant chemotherapy is needed after enucleation.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Retinoblastoma arises from a cone-precursor cell whose fate and proliferation are patterned by Notch signaling during retinal development, the developmental context in which RB1 loss unleashes uncontrolled division.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 recruits the macrophages found within retinoblastoma, a myeloid infiltrate that supports angiogenesis and invasion and is being studied as part of the tumor microenvironment beyond the malignant cells themselves.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Retinoblastoma cells express TrkB and respond to BDNF with pro-survival signaling, a neurotrophic dependency inherited from their neural-retina origin that helps the tumor resist apoptosis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR activity supports retinoblastoma cell survival and growth downstream of the deregulated RB-E2F proliferation, complementing the AKT and mTOR already mapped as a targetable dependency.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1/IGF-1R signaling is expressed in retinoblastoma and drives proliferation and survival, a growth-factor axis under study as a therapeutic target in this childhood retinal tumor.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Retinoblastoma carries strikingly few genetic lesions beyond RB1 loss and instead advances through widespread epigenetic deregulation, including DNA-methylation changes effected by DNMTs such as DNMT3A.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restrains the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped) that supports the survival of retinoblastoma cells and is a candidate therapeutic target.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — IGF-1R signaling (IGF-1 mapped) feeds the MAPK-ERK cascade that supports proliferation and survival in retinoblastoma.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 signaling promotes the survival and chemoresistance of retinoblastoma cells, complementing the loss of RB-mediated cell-cycle control.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-ERK signaling (ERK1/2 already mapped) provides a proliferative input cooperating with RB1 loss and MYCN amplification in retinoblastoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK kinases signal to STAT3 (already mapped), the survival pathway whose activity sustains retinoblastoma-cell chemoresistance.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB-driven survival and inflammatory signaling supports the growth of retinoblastoma and contributes to chemoresistance.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the invasion and survival of retinoblastoma cells.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling modulates the proliferation and microenvironment of retinoblastoma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of retinoblastoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune surveillance of the RB1-driven retinoblastoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the differentiation and microenvironment of the retinal-progenitor-derived cells of retinoblastoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by the PI3K-AKT axis, modulate the survival and oxidative-stress balance of retinoblastoma cells.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the MYCN stability and survival signaling of retinoblastoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is a component of the immune response to retinoblastoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the tumor microenvironment of retinoblastoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the survival and invasion of retinoblastoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of retinoblastoma cells.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of retinoblastoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of retinoblastoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of retinoblastoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of retinoblastoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of retinoblastoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of retinoblastoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of retinoblastoma.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — Neurotrophin survival: retinoblastoma cells express the TrkB receptor for BDNF (BDNF already mapped), and this neurotrophin signalling supports tumour-cell survival and chemoresistance, a targetable axis in this photoreceptor-derived cancer.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Cone-precursor origin: retinoblastoma arises from cone photoreceptor precursors whose identity depends on thyroid-hormone-receptor (TRbeta) signalling, tying the tumour's cell of origin to thyroid-hormone-driven cone specification in the developing retina.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune-cold tumour: retinoblastoma grows in the immune-privileged eye with low MHC class II antigen presentation, limiting T-cell recognition, a barrier to the immunotherapies increasingly explored for refractory and metastatic disease.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cellular immunotherapy: IL-2-driven T-cell expansion supports the CAR-T and adoptive approaches (GD2 and others) being explored for refractory or metastatic retinoblastoma, which resists immune attack in its privileged ocular site (MHC class II already mapped).
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint context: PD-1 checkpoint blockade is of limited benefit in the immune-cold, low-mutation retinoblastoma, motivating combination strategies for the rare metastatic cases that escape local control.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Chemotherapy myelosuppression: the systemic and intra-arterial chemotherapy used to preserve the eye in retinoblastoma is myelosuppressive, lowering haemoglobin and requiring supportive care in these young children.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Chemotherapy cardiotoxicity: the carboplatin and, in extraocular disease, anthracycline-containing regimens for retinoblastoma carry cardiotoxic risk, and troponin elevation helps detect the myocardial injury threatening these very young survivors.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 helps make retinoblastoma an immunologically cold, low-mutation tumour (PD-1 already mapped), dampening the T-cell response, which limits the benefit of checkpoint blockade in the rare metastatic cases.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and lysis stress: chemotherapy of retinoblastoma generates oxidative stress and, in bulky disease, rapid cell lysis releasing purines that xanthine oxidase converts to uric acid, contributing to tumour-lysis and oxidative burden.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, low-mutation microenvironment of retinoblastoma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the systemic chemotherapy of retinoblastoma is myelosuppressive, causing anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the young child with iron.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of retinoblastoma, part of the stromal microenvironment of this intraocular tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immune microenvironment of the intraocular retinoblastoma.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the tumour-associated macrophages (already mapped) and the cyclooxygenase pathway (IL-6 and IL-1 already mapped) contribute to the inflammatory microenvironment of retinoblastoma.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin adds an anaemia of chronic disease to the chemotherapy anaemia (iron and haemoglobin already mapped) of retinoblastoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic microenvironment: leptin from the marrow and stromal adipose tissue signals within the metabolic microenvironment of the metastatic/chemotherapy-treated retinoblastoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipose adipokine: adiponectin, with leptin (already mapped), is the marrow-adipose adipokine of the metabolic microenvironment of the metastatic retinoblastoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic milieu of retinoblastoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the emerging immunotherapy of retinoblastoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of retinoblastoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of retinoblastoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of retinoblastoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the retinoblastoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the retinoblastoma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of retinoblastoma.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the tumour antigen to the T cells (already mapped) shaping the adaptive immune response against retinoblastoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of retinoblastoma.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of retinoblastoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tumour complement: the complement C3 activation contributes to the inflammatory dimension of the intraocular retinoblastoma microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid (macrophage already mapped) recruitment into the retinoblastoma microenvironment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chemotherapy anaemia support: erythropoietin corrects the anaemia from VAC-based chemotherapy in retinoblastoma, and EPOR expression on retinal progenitor cells hints at a developmental role in the retinoblastoma cell of origin.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Intraocular mast-cell mediator: histamine from intraocular mast cells promotes the angiogenesis (VEGF already mapped) and the vascular permeability that sustain the highly vascular growth pattern of retinoblastoma within the vitreous.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Blood-ocular-barrier modulation: bradykinin B2-receptor agonists increase the permeability of the blood-ocular barrier, a pharmacological strategy explored to enhance intra-arterial and intravitreal chemotherapy delivery in retinoblastoma.

[^knudson-1971-two-hit]: Knudson AG Jr. Mutation and cancer: statistical study of retinoblastoma. *Proc Natl Acad Sci USA.* 1971;68(4):820-823. [doi:10.1073/pnas.68.4.820](https://doi.org/10.1073/pnas.68.4.820) · [PubMed 5279523](https://pubmed.ncbi.nlm.nih.gov/5279523/)
[^shields-2008-retinoblastoma]: Shields CL, Shields JA. Retinoblastoma management: advances in enucleation, intravenous chemoreduction, and intra-arterial chemotherapy. *Curr Opin Ophthalmol.* 2010;21(3):203-212. [doi:10.1097/ICU.0b013e328338676a](https://doi.org/10.1097/ICU.0b013e328338676a) · [PubMed 20224400](https://pubmed.ncbi.nlm.nih.gov/20224400/)
