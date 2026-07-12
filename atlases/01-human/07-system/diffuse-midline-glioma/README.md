---
schema: human-scale-entry/v1
id: diffuse-midline-glioma
name: Diffuse Midline Glioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Diffuse midline glioma (H3K27M+) is a WHO Grade 4 pediatric/young adult brain tumor defined by H3K27M mutation; DIPG, thalamic, and spinal cord locations; median OS 12-15 months; ONC201 (imipridone) FDA-approved for relapsed/refractory H3K27M+ DMG; no curative systemic therapy."
aliases: ["DMG", "diffuse midline glioma", "DIPG", "diffuse intrinsic pontine glioma", "H3K27M glioma", "thalamic glioma H3K27M", "H3K27M-altered glioma", "pediatric midline glioma", "pontine glioma", "H3.3K27M brain tumor"]
sources:
  - id: schwartzentruber-2012-h3f3a-glioma
    type: peer-reviewed
    cite: "Schwartzentruber J, Korshunov A, Liu XY, et al. Driver mutations in histone H3.3 and chromatin remodelling genes in paediatric glioblastoma. Nature. 2012;482(7384):226-231."
    doi: "10.1038/nature10833"
    pmid: "22286061"
    url: "https://doi.org/10.1038/nature10833"
  - id: khuong-quang-2012-h3k27m-dipg
    type: peer-reviewed
    cite: "Khuong-Quang DA, Buczkowicz P, Rakopoulos P, et al. K27M mutation in histone H3.3 defines clinically and biologically distinct subgroups of pediatric diffuse intrinsic pontine gliomas. Acta Neuropathol. 2012;124(3):439-447."
    doi: "10.1007/s00401-012-0998-0"
    pmid: "22661320"
    url: "https://doi.org/10.1007/s00401-012-0998-0"
cross_links:
  - target: 01-human/03-molecular/h3k27m
    relation: connects-to
    note: "H3K27M mutation in H3F3A or HIST1H3B defines WHO Grade 4 diffuse midline glioma (100% diagnostic criterion since 2021 WHO CNS classification); H3K27M IHC (anti-H3.3K27M, clone D5E7) is the diagnostic standard; TBXT-negative; H3K27M identifies tumor in CSF liquid biopsy."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "H3K27M inhibits EZH2/PRC2 activity in trans → global H3K27me3 loss; this dominant-negative epigenetic mechanism is the oncogenic hallmark of DMG; paradoxically, EZH2 protein is intact and overexpressed in H3K27M DMG; panobinostat (HDAC inhibitor) partially restores H3K27me3."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion in ~15-25% H3K27M DMG (higher in DIPG/thalamic subtypes); NF1+H3K27M co-alteration common in spinal DMG; CDKN2A loss → CDK4/6 → RB1 → E2F proliferation; palbociclib + ONC201 combination being explored in H3K27M+CDKN2A-deleted DMG."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGFRA point mutations and amplification occur in ~25-35% of H3K27M DMG; PDGFRA → MAPK/PI3K → glioma proliferation; PDGFRA co-mutation with H3K27M accelerates malignancy; avapritinib and imatinib explored in PDGFRA-mutant DMG subsets."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 mutations in ~10% of H3K27M DMG, enriched at spinal cord location; NF1 LOF → constitutive RAS-MAPK → MEK-ERK proliferation; NF1+H3K27M spinal DMG shows high macrophage infiltration; selumetinib and trametinib (MEK inhibitors) explored in NF1-mutant H3K27M spinal DMG."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA/PIK3R1 mutations in ~15% of H3K27M DMG; PI3K-AKT-mTOR cooperates with H3K27M epigenetic reprogramming; alpelisib (PI3Kα inhibitor) and copanlisib in combination with ONC201 under investigation; PTEN loss is an alternative PI3K pathway activation mechanism in DMG."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "H3K27M DMG and IDH-wildtype GBM are both WHO Grade 4 but molecularly distinct; GBM shows EGFR amplification/EGFRvIII, TERT promoter mutation, CDK4/6 amplification absent in DMG; ONC201 active in DMG but not GBM; bevacizumab benefits GBM (PFS) but not H3K27M DMG."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Diffuse midline glioma grows in the brain's midline — pons (DIPG), thalamus, and spinal cord — where infiltrative spread makes surgery impossible; the pontine location compresses cranial nerve nuclei and long tracts, and radiation is the only treatment that briefly helps."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "DMG arises from oligodendrocyte precursor cells (OPCs) of the developing midline: the H3K27M mutation freezes these cells in a proliferative, stem-like state by stalling differentiation, which is why the tumor peaks at ages 5-10 when OPCs are most active in the pons."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "The DMG microenvironment is rich in microglia and macrophages, especially NF1-mutant spinal tumors, but these are immunosuppressive rather than tumoricidal — one reason checkpoint inhibitors have largely failed and GD2-directed CAR-T is being explored instead."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Diffuse midline glioma and medulloblastoma are the two great malignant pediatric brain tumors at opposite poles: DMG is an unresectable, fatal H3 K27M brainstem glioma, while medulloblastoma is a resectable cerebellar tumor often cured by surgery plus craniospinal radiotherapy."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Diffuse midline glioma arises from an OPC-like glial precursor of the astrocyte/oligodendrocyte lineage: the H3 K27M oncohistone freezes these cells in a stem-like state by collapsing H3K27 methylation, so the tumor infiltrates the pons diffusely rather than forming a mass."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is the only treatment that reliably helps diffuse midline glioma: focal irradiation of the pons gives transient symptom relief and a few months' benefit, but the H3 K27M tumor inevitably regrows—no chemo, surgery, or re-irradiation is curative."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Diffuse midline glioma and IDH-mutant glioma are epigenetically opposite gliomas: DMG's H3 K27M oncohistone collapses methylation in children with dismal outcomes, while adult IDH-mutant gliomas accumulate 2-HG and fare far better—chromatin reprogramming, not oncogenes."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Diffuse midline glioma and ATRT are aggressive pediatric brain tumors driven by epigenetic dysregulation: DMG by the H3 K27M histone mutation, ATRT by SMARCB1/SWI-SNF loss—both reprogram chromatin and carry a grim prognosis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Diffuse midline glioma forms synapses with neurons to grow: the tumor's OPC-like cells receive glutamatergic input through real neuron-to-glioma synapses that drive proliferation—so neuronal activity feeds the cancer, making activity-blocking drugs a therapeutic idea."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation frequently accompanies the H3K27M driver in DMG: loss of p53 removes the damage checkpoint atop the epigenetic catastrophe of histone mutation, accelerating this fatal pediatric brainstem tumor—a partnership of epigenetic and tumor-suppressor failure."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 amplification helps drive DMG's relentless growth: alongside H3K27M, gains in the cell-cycle machinery push tumor cells past the G1 checkpoint, making CDK4/6 inhibitors one of the targeted strategies tested against this otherwise untreatable tumor."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "DMG often activates the PI3K/AKT/mTOR pathway: mutations in PIK3CA and related genes switch on mTOR-driven growth alongside the H3K27M epigenetic driver, so mTOR-pathway inhibitors are explored as targeted therapy for this lethal midline glioma."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Diffuse midline glioma is the deadliest pediatric tumor of the nervous system: it infiltrates the brainstem (as DIPG), thalamus or spinal cord diffusely, so it cannot be resected and disrupts the very structures that control breathing, movement and consciousness."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Germline TP53 loss in Li-Fraumeni syndrome predisposes to midline gliomas: while most diffuse midline gliomas are sporadic H3K27M-driven, the syndrome shows how inherited tumor-suppressor loss can also seed these lethal childhood brain cancers."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy has been tried in diffuse midline glioma to spare the developing brain: its sharp dose falloff limits collateral damage near the brainstem, but because the tumor infiltrates diffusely and resists treatment, it has not improved the grim prognosis."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Diffuse midline glioma hijacks the synapse: tumor cells form real synapses with neurons and grow in response to neuronal activity, so brain electrical signaling literally feeds the cancer—a discovery opening neuroscience-based therapies for this lethal childhood tumor."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Diffuse midline glioma is a frontier for T-cell therapy: GD2-directed CAR-T cells have shrunk these previously untreatable pontine tumors in early trials, so engineered cytotoxic T cells offer the first real hope against a near-uniformly fatal cancer."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate drives diffuse midline glioma growth: neuron-released glutamate acting on tumor AMPA receptors stimulates proliferation, so the same excitatory signaling that runs the brain fuels the cancer—making glutamate pathways a therapeutic target."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Diffuse midline glioma's most promising drug works on dopamine signaling: ONC201 (dordaviprone) antagonizes the dopamine D2 receptor (and mitochondrial ClpP) and has produced rare responses in H3K27M tumors, a surprising therapeutic angle in an otherwise fatal cancer."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "A thalamic subset of diffuse midline glioma is driven by EGFR: bithalamic H3-wildtype midline gliomas carry EGFR mutations rather than H3K27M, so molecular testing splits these tumors into biologically distinct, differently-targetable groups."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Diffuse midline glioma is a target for NK and cell therapies: because it is so hard to resect or irradiate, engineered NK cells and GD2 CAR-T are being tested to attack the tumor immunologically where surgery and drugs fail."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Diffuse midline glioma grows on calcium from neuron-glioma synapses: real synapses form between neurons and tumor cells, and the glutamate-driven calcium influx through them spurs the cancer to proliferate—a striking link between brain activity and tumor growth."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Diffuse midline glioma recruits blood supply via VEGF: though infiltrative, the tumor releases VEGF to coax new vessels and loosen the blood-brain barrier, a process studied as a target in a cancer that resists almost all therapy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Tumor-associated microglia feed diffuse midline glioma through NF-kB: this inflammatory switch in the brain's immune cells drives cytokines that support the glioma's growth, part of the supportive niche around this lethal pediatric tumor."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Diffuse midline glioma announces itself in the eyes: a pontine tumor first palsies the cranial nerves that move the eyes and face, so double vision, a crossed eye, and facial droop are classic early signs of DIPG."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Diffuse midline glioma ultimately stops the breath: as it destroys the brainstem's control of breathing and swallowing, patients lose airway protection and respiratory drive, the failure that ends this lethal disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Diffuse midline glioma works on endothelial cells: VEGF from the tumor loosens the blood-brain barrier these cells form and recruits new vessels, both feeding growth and complicating drug delivery to the brainstem."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Diffuse midline glioma destabilizes the brainstem's autonomic control: infiltrating the pons it disrupts the centers governing heart rate and blood pressure, causing dangerous swings late in the disease."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Diffuse midline glioma picks off the cranial nerves: invading the pons it palsies the nerves controlling eye movement, the face and swallowing, the cranial-nerve deficits that often herald it."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Some diffuse midline gliomas are driven by activin signaling: ACVR1 mutations switch on the activin-A/BMP pathway, a recurrent driver in the pontine tumors of young children and a drug target."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy made a startling discovery: real synapses form between healthy neurons and glioma cells, the neuron's terminal wiring directly onto the tumor — an electrical hijacking that drives the cancer's growth."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "The tumor plugs into the brain's electricity: glioma cells carry potassium and other ion channels that let them depolarize in response to neuronal firing, the electrical excitability that the neuron-glioma synapse feeds and that spurs invasion."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Glutamate from the neuron-glioma synapse pours sodium into the tumor: AMPA-receptor currents flood the glioma cell with sodium and calcium, the depolarizing signal by which neural activity literally powers the cancer's spread."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Engineered antibody-based cells offer new hope: GD2-directed CAR-T cells have shrunk H3K27M-mutant diffuse midline gliomas in early trials, the first therapy to dent a tumor that radiation only briefly holds."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Its pontine home wrecks swallowing: the tumor infiltrates the brainstem's bulbar centers, so dysphagia and impaired airway protection bring aspiration and the need for feeding tubes as the disease advances."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Radiation and chemotherapy thin the blood: the craniospinal radiation and any added chemotherapy suppress the marrow, dropping neutrophils and raising the infection risk during the months of treatment."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "A midline tumor sits beside the master glands: thalamic and pontine gliomas and the radiation aimed at them border the hypothalamus and pituitary, so survivors face deficits of growth, thyroid and sex hormones that need lifelong endocrine follow-up."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "A subset of these gliomas amplify MYC: alongside the defining H3K27M mutation, MYC or PVT1 amplification drives some diffuse midline gliomas, adding a proliferative push that marks particularly aggressive, fast-growing tumors."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The tumor is immunologically cold: it carries few mutations to flag and recruits regulatory T cells that suppress attack, an immune-evasive microenvironment that has frustrated immunotherapy and shapes the GD2 CAR-T trials now under way."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β helps the glioma spread and hide: it drives the diffuse invasion through the brainstem and dampens the local immune response, part of why these tumors are unresectable and immune-resistant."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages fill the tumor but don't fight it: monocyte-derived macrophages, alongside microglia, dominate the DMG microenvironment in an immunosuppressive state that helps the cancer evade attack."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "An NF1 background can seed the glioma: loss of the NF1 tumor suppressor is a recurrent driver of diffuse midline glioma, and the syndrome's lifelong predisposition to gliomas links it to this lethal childhood tumor."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "ATRX loss often joins the H3K27M hit: especially in thalamic and spinal diffuse midline gliomas, ATRX mutation accompanies the histone mutation, driving alternative lengthening of telomeres and genomic instability."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "The infiltrating glioma irritates the cortex: as diffuse midline glioma spreads from the pons or thalamus it can trigger seizures, and seizure control is part of the supportive care for these children."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Brainstem and spinal infiltration brings pain: tumor invasion of sensory pathways causes neuropathic pain and, in spinal diffuse midline glioma, radicular pain — a symptom burden central to palliative management."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 supports the H3K27M-driven tumor: diffuse midline glioma cells show STAT3 activation that backs proliferation and immune evasion, a pathway studied for this almost uniformly fatal childhood brainstem tumor."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Brain tumors are strongly prothrombotic: like other high-grade gliomas, diffuse midline glioma raises venous thromboembolism risk through tumor tissue factor and the immobility that progressive brainstem disease brings."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Brainstem failure routes food to the lungs: as the tumor disables swallowing and airway protection, aspiration pneumonia becomes common, and it with the immunosuppression of high-dose steroids can progress to sepsis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its radiation can scar the brain's vessels: the high-dose radiotherapy that is the mainstay of palliation for diffuse midline glioma injures cerebral vessels, causing a delayed vasculopathy and stroke risk in longer survivors."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An almost uniformly fatal childhood tumor devastates: the relentless brainstem decline and dismal prognosis of diffuse midline glioma impose profound depression and grief on patients and families."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Advanced disease and its therapy blunt the marrow: progressive tumor burden with its inflammation, plus any chemotherapy and radiation, depress erythropoiesis into an anemia of chronic disease late in the course."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its steroids raise blood sugar: the high-dose dexamethasone used to control peritumoral edema in diffuse midline glioma induces insulin resistance, frequently causing steroid-induced hyperglycemia and diabetes."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Steroids and radiation blunt immunity: the prolonged dexamethasone and cranial radiation for diffuse midline glioma suppress immune defense, occasionally permitting invasive aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Chronic steroids impair repair: the long-term dexamethasone needed to manage symptoms of diffuse midline glioma thins skin and slows healing of surgical biopsy and other wounds."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It strikes the brain's breathing centre: diffuse midline glioma of the pons infiltrates the brainstem respiratory and cardiovascular nuclei, so progression leads to respiratory failure, a common terminal event."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Brainstem invasion robs swallowing: the pontine and bulbar involvement of diffuse midline glioma causes dysphagia and aspiration, driving the need for modified feeding or a gastrostomy."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A uniformly fatal childhood tumour breeds anguish: the dismal prognosis and relentless neurological decline of diffuse midline glioma impose profound anxiety on families alongside depression."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Treatment burdens the growing body: craniospinal radiation impairs growth and the long-term high-dose dexamethasone used to control oedema causes steroid myopathy and bone loss."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Radiation and steroids mark the skin: radiotherapy causes dermatitis over the treatment field, and the dexamethasone needed for mass effect brings acne, striae and skin thinning."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its steroids suppress immunity: the prolonged dexamethasone used to control peritumoural oedema blunts immune defence, raising infection risk including Pneumocystis pneumonia."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It sits at the body's control centre: a pontine diffuse midline glioma can disturb the brainstem cardiorespiratory and autonomic centres, causing blood-pressure and heart-rate instability."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Treatment reaches the hormone axis: radiation near the hypothalamus and pituitary can disturb puberty and fertility in children surviving midline glioma."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Long steroids invite an opportunist: the prolonged dexamethasone used for diffuse midline glioma suppresses immunity enough to risk Pneumocystis pneumonia, so prophylaxis is advised."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Epigenetic and targeted drugs are the hope: ONC201/dordaviprone and agents aimed at the H3K27M-driven PRC2/EZH2 dysregulation are the leading experimental therapies for this otherwise untreatable tumour."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Cell therapy enters the brainstem: GD2- and B7-H3-directed CAR-T cells have produced the first meaningful responses in H3K27M diffuse midline glioma, a landmark for solid-tumour cell therapy."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Conventional chemo barely helps: diffuse midline glioma is notoriously chemoresistant and the intact blood-brain barrier keeps drugs out, leaving radiation as the only standard treatment."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold tumour: diffuse midline glioma has a low mutational burden and sparse T-cell infiltrate in an immunosuppressed brain, so checkpoint inhibitors have shown little benefit, redirecting effort to engineered cell therapies."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "It infiltrates along the white matter: diffuse midline glioma spreads diffusely through the pons and brainstem tracts rather than as a resectable mass, weaving among axons in a way that makes surgery impossible."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "A shared GD2 target: both diffuse midline glioma and neuroblastoma express the GD2 disialoganglioside, and GD2-directed CAR-T and antibody therapy developed for neuroblastoma now show promise against this glioma."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neuron-glioma synapses: neuronal activity and BDNF-TrkB signalling drive diffuse midline glioma growth through electrical and paracrine synapses with neurons, a discovery reframing the tumour as part of a neural circuit."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Immortality without TERT: ATRX loss in diffuse midline glioma maintains telomeres by alternative lengthening (ALT) rather than the TERT-promoter activation other cancers use—two routes to replicative immortality."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Cognition in the crossfire: midline and thalamic tumours, and the radiotherapy that palliates them, injure the hippocampus and memory circuits, adding neurocognitive decline to the disease's burden."
  - target: 01-human/07-system/chordoma
    relation: connects-to
    note: "Midline tumours of the neuraxis: diffuse midline glioma (brainstem, thalamus, cord) and chordoma (clivus, sacrum) both arise along the body's midline axis, posing similar surgical-access challenges despite different origins."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "The CNS-tumour spectrum: against the lethal, infiltrative diffuse midline glioma, meningioma represents the benign, resectable extreme of brain tumours—two poles of neuro-oncology."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Deep brain masses on imaging: a brainstem or thalamic mass raises a differential that includes diffuse midline glioma and, in older or immunocompromised patients, primary CNS lymphoma, told apart by biopsy and steroid response."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle amplification: CDK4/6 and cyclin D gains drive cell-cycle progression in diffuse midline glioma, a recurrent secondary lesion and the rationale for CDK4/6 inhibition."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT survival: PIK3CA-activated AKT signalling feeds the mTOR pathway sustaining diffuse midline glioma cells, a cooperating driver alongside the defining H3K27M mutation."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-factor dependence: IGF-1/IGF1R signalling supports the proliferation and survival of diffuse midline glioma cells, an investigational therapeutic vulnerability in this lethal tumour."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic pons: HIF-1α stabilised in the hypoxic, infiltrative diffuse midline glioma drives the VEGF angiogenesis and metabolic adaptation that support its growth in the brainstem."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Receptor amplification: MET amplification occurs in a subset of diffuse midline gliomas, marking an actionable receptor tyrosine kinase alongside the defining H3K27M epigenetic lesion."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Rare actionable fusion: NTRK fusions, though uncommon, render some diffuse midline gliomas sensitive to TRK inhibitors, a precision-oncology option for this otherwise untreatable tumour."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Myeloid microenvironment: CCL2 recruits microglia and monocyte-derived macrophages that dominate the diffuse midline glioma microenvironment, supporting an immunosuppressive niche resistant to immunotherapy."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK-MAPK signalling: RAS-RAF-ERK signalling downstream of PDGFRA and EGFR amplification drives proliferation in diffuse midline glioma, complementing its defining H3K27M epigenetic reprogramming."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle deregulation: CDKN2A loss and CDK4/6 activity unleash E2F1-driven cell-cycle entry in diffuse midline glioma, sustaining the relentless proliferation of this lethal tumour."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "White-matter infiltration: CXCR4 on diffuse midline glioma cells follows CXCL12 gradients along white-matter tracts, driving the diffuse brainstem infiltration that makes the tumour inoperable."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Radiation response: radiotherapy — the only treatment that helps in DIPG — kills tumour cells through caspase-3-mediated apoptosis, but apoptosis resistance underlies the inevitable relapse after the transient response."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Radioresistance: RAD51-mediated homologous-recombination repair helps diffuse midline glioma survive radiation-induced DNA damage, a mechanism of the radioresistance that limits the durability of treatment."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Neuron-glioma synapses: diffuse midline glioma cells form functional AMPA-receptor synapses with neurons, and the resulting calcium-mediated electrical activity drives tumour proliferation — a striking dependence on neuronal activity that opens new therapeutic angles."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "GD2 CAR-T therapy: GD2-directed CAR-T cells, the first immunotherapy to show responses in diffuse midline glioma, kill the GD2-expressing tumour cells through perforin and granzyme, a breakthrough against this previously untreatable cancer."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenome reprogramming: the H3K27M mutation globally reshapes the epigenome, redistributing DNA methylation alongside the loss of PRC2-mediated H3K27 trimethylation, the epigenetic catastrophe at the root of diffuse midline glioma."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K activation: PTEN loss activates the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped), a recurrent co-alteration with H3K27M that supports growth in diffuse midline glioma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Progenitor maintenance: NOTCH signalling sustains the neural-progenitor-like state that the H3K27M epigenetic reprogramming exploits, helping maintain the stem-like, proliferative cell population of diffuse midline glioma."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint lost: the RB-E2F axis (CDK4/6, cyclin-D1, CDKN2A and E2F1 all already mapped) is deregulated in diffuse midline glioma, and RB inactivation releases the cell-cycle progression these tumours depend on."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferative drive: RAS-MAPK signalling (NF1 loss and ERK1/2 already mapped) provides a proliferative input cooperating with the H3K27M epigenetic reprogramming that defines diffuse midline glioma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 survival: JAK-STAT3 signalling (STAT3 already mapped) supports the survival and immunosuppressive microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Therapy resistance: anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the profound radio- and chemo-resistance of diffuse midline glioma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "ACVR1-activin-SMAD signalling (activin-A mapped) is constitutively activated by the ACVR1 mutations that co-occur with H3K27M in diffuse midline glioma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 promotes the invasive and immunosuppressive phenotype of diffuse midline glioma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment and radiation response of diffuse midline glioma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immunologically cold microenvironment of diffuse midline glioma, a barrier to its immunotherapy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the metabolic and oxidative stress of the H3K27M-driven tumour cells of diffuse midline glioma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling modulates the neural-progenitor proliferation and survival programmes hijacked by diffuse midline glioma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in diffuse midline glioma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the immunosuppressive microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling downstream of PDGFR (PDGF already mapped) drives the invasive signaling of diffuse midline glioma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of the H3K27M-driven cells of diffuse midline glioma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation cooperating with the H3K27M mutation of diffuse midline glioma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the brainstem-infiltrating cells of diffuse midline glioma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven microglial and myeloid recruitment shapes the immunosuppressive microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of diffuse midline glioma."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt-β-catenin signaling participates in the glioma-stem-cell maintenance of diffuse midline glioma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammatory microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of diffuse midline glioma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microglial/macrophage-rich tumor microenvironment and invasion of diffuse midline glioma."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "GD2 CAR-T therapy: IL-2-driven T-cell expansion powers the GD2-directed CAR-T therapy that has produced striking early responses in H3K27M diffuse midline glioma, a landmark immunotherapy for this otherwise uniformly fatal tumour."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation: MHC class II-restricted antigen presentation shapes the T-cell response to diffuse midline glioma, relevant to the peptide vaccines targeting the H3K27M neoantigen (already mapped) being tested in this tumour."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint context: diffuse midline glioma is an immunologically cold tumour, and PD-1 checkpoint blockade is explored in combination with CAR-T and vaccine strategies to sustain the anti-tumour T-cell response."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: the anti-inflammatory cytokine IL-10 helps make diffuse midline glioma an immunologically cold tumour (PD-1 already mapped), blunting the T-cell response that CAR-T and vaccine strategies aim to mount."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Neuronal activity: alongside the glutamatergic neuron-glioma synapses (glutamate already mapped), GABAergic signalling modulates the neuronal electrical activity that drives the growth of diffuse midline glioma, an emerging neuro-oncology target."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide regulates vascular tone and, with VEGF (already mapped), the angiogenesis and hypoxic microenvironment of diffuse midline glioma, part of the stromal biology of this infiltrative brainstem tumour."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia (already mapped) and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6 and IL-1 already mapped) of the diffuse midline glioma microenvironment."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative microenvironment: the infiltrative diffuse midline glioma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of its hypoxic (HIF-1-alpha already mapped) tumour microenvironment."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 microglial polarisation: IL-4 polarises the tumour-associated microglia and macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive niche of diffuse midline glioma."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 arm and CAR-T target: IL-13, with IL-4 (already mapped), supports the M2 microglial niche, and the IL-13 receptor alpha-2 is a target of the CAR-T-cell approaches being trialled against diffuse midline glioma."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Neuron-glioma signalling: alongside the glutamate and GABA (already mapped) synapses, cholinergic acetylcholine signalling is part of the neuronal activity that drives the growth of the electrically integrated diffuse midline glioma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Ferroptosis vulnerability: the iron-dependent lipid peroxidation of ferroptosis is a metabolic vulnerability of diffuse midline glioma (xanthine oxidase and oxidative stress already mapped), an emerging therapeutic angle in this incurable tumour."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonergic neuromodulation: serotonin modulates the neuron-glioma (glutamate, GABA and dopamine already mapped) circuits whose activity drives the growth of the electrically integrated diffuse midline glioma."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Noradrenergic input: noradrenaline is part of the neuronal-activity-dependent (glutamate already mapped) signalling that stimulates the proliferation of diffuse midline glioma."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipid metabolic dependency: the cholesterol and lipid metabolism on which diffuse midline glioma depends is a metabolic vulnerability, alongside the ferroptosis (iron already mapped), being explored therapeutically."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Tumour-associated microglia: the microglia and macrophages (CCL2 already mapped) dominate the immunosuppressive, immunologically cold microenvironment of the diffuse midline glioma."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "High-grade-glioma differential: the diffuse midline glioma (H3K27M already mapped) is a distinct WHO-grade-4 midline glioma, molecularly separate from the adult, IDH-wildtype glioblastoma."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Palliative radiotherapy: the focal photon radiotherapy is the only standard treatment of the diffuse midline glioma, providing the temporary response of the incurable tumour."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, explored with the GD2 CAR-T and checkpoint (PD-1 already mapped) trials in diffuse midline glioma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immunosuppressive microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immunosuppressive microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the diffuse-midline-glioma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of diffuse midline glioma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) and myeloid activation of the immunosuppressive microenvironment of diffuse midline glioma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the sparse immune infiltrate of the immunologically cold diffuse midline glioma."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the tumour antigen (MHC already mapped) to the T cells (already mapped), a rationale for the GD2 CAR-T and vaccine immunotherapy of diffuse midline glioma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the microglial (already mapped) and myeloid inflammation of the diffuse-midline-glioma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the diffuse-midline-glioma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack in the immunologically cold tumour."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the H3K27M-mutant (already mapped) glioma cells and the disordered brain-iron handling of diffuse midline glioma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-DMG axis: TSLP, from the DMG stromal cells and astrocytes (already mapped), primes dendritic cells (already mapped) and amplifies the Th2-skewed immunosuppressive microenvironment of the H3K27M-mutant (already mapped) diffuse midline glioma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-DMG axis: bradykinin, via B1/B2 receptors on the DMG tumour endothelium (already mapped) and microglia (already mapped), augments blood-brain-barrier permeability, oedema, and the inflammatory milieu of diffuse midline glioma."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-DMG axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia of the DMG tumour core, activates the EPOR on H3K27M-mutant (already mapped) glioma cells and modulates macrophage/microglia (already mapped) polarisation."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell DMG axis: histamine, from the mast cells (already mapped) in the DMG tumour microenvironment and brain border compartments, amplifies the blood-brain-barrier permeability and the immunosuppressive neuroinflammatory milieu of DMG."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-H3K27M axis: melatonin, via MT1/MT2 receptors on H3K27M-mutant (already mapped) glioma cells and microglia (already mapped), modulates the epigenetic-hypoxic (HIF-1α already mapped) stress and the immunosuppressive milieu of DMG."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation can contribute to the neuroinflammatory milieu and the blood-brain-barrier disruption of DMG."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "DMG oxytocin: oxytocin, via OXTR on microglia (already mapped) and macrophages (already mapped), attenuates neuroinflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of diffuse midline glioma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "DMG vasopressin: vasopressin, via V1aR on microglia (already mapped) and macrophages (already mapped), modulates neuroinflammation; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) glioma-promoting cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "DMG selenium: selenium, via selenoprotein activity in microglia (already mapped) and glioma cells, suppresses the oxidative stress that amplifies the NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive neuroinflammatory cascade of diffuse midline glioma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "DMG prolactin: prolactin, via PRLR on microglia (already mapped) and macrophages (already mapped), modulates neuroinflammation; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) glioma-promoting immunosuppressive cascade of diffuse midline glioma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "DMG testosterone: testosterone, via androgen receptors on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; testosterone deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "DMG iodine: iodine-dependent thyroid hormones modulate microglia (already mapped) polarisation and neuroinflammation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive glioma cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "DMG magnesium: magnesium cofactors kinase signalling in microglia (already mapped) and macrophages (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive neuroinflammatory glioma cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "DMG copper: copper supports microglia (already mapped) and macrophage (already mapped) antioxidant function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive neuroinflammatory cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "DMG zinc: zinc cofactors microglia (already mapped) and macrophage (already mapped) anti-tumour immune function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive glioma cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "phosphorus, as ATP in microglia (already mapped) and macrophage (already mapped), fuels mTOR (already mapped) glioma proliferative signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and p53 (already mapped) immunosuppressive cascade."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride channels on microglia (already mapped) and macrophage (already mapped) regulate membrane potential; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) immunosuppressive glioma cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "sulfur, as glutathione precursor in microglia (already mapped) and macrophage (already mapped), counters oxidative stress; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) glioma cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "DMG carbon: carbon in nucleotides fuels microglia (already mapped) and macrophage (already mapped) glioma growth; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) immunosuppressive cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "DMG hydrogen: hydrogen via ROS from microglia (already mapped) and macrophage (already mapped) modulates glioma redox; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) immunosuppressive cascade of diffuse midline glioma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "DMG nitrogen: nitrogen in DNA bases of microglia (already mapped) and macrophage (already mapped) sustains glioma growth; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of diffuse midline glioma."
---

# Diffuse Midline Glioma

## Overview

**Diffuse midline glioma (DMG), H3K27M-altered** is a WHO Grade 4 primary brain tumor defined by the presence of the **H3K27M oncohistone mutation** in a diffuse infiltrating glioma arising at a midline neuroanatomical location. Since the 2021 WHO Classification of CNS Tumors (5th edition), the H3K27M mutation is the defining molecular criterion — replacing histological grade for diagnosis. DMG encompasses the clinically defined **diffuse intrinsic pontine glioma (DIPG)** and H3K27M-mutant gliomas of the thalamus, cerebellum, and spinal cord. DMG is uniformly lethal, with no curative treatment; it is the **leading cause of brain tumor-related mortality in children** [^schwartzentruber-2012-h3f3a-glioma] [^khuong-quang-2012-h3k27m-dipg].

**Epidemiology:**
- Incidence: ~300-400 DIPG cases/year USA; ~100-150 additional thalamic/spinal H3K27M DMG
- Peak age: 5-10 years for DIPG; 10-15 years for thalamic; young adults (20-40 years) for ~15-20% of cases
- No sex predominance; no known germline predisposition; no environmental risk factors identified
- Rarely familial; somatic H3K27M always

**Sites:**

| Location | Frequency of H3K27M+ | Key features |
|---|---|---|
| Pons (DIPG) | ~80% | Peak age 6-9 yr; cranial nerve palsies (VI, VII most common); long tract signs; Parinaud syndrome rare |
| Thalamus | ~50% | Unilateral thalamic mass → hydrocephalus; older pediatric age; some resectable; worse prognosis than DIPG in adults |
| Spinal cord | ~30% | Cervical > thoracic; NF1 co-mutations common; ~15% adult patients; more amenable to biopsy |
| Cerebellum | ~15% | Often H3.3 K27M; frequently adult; mass lesion; partial resection possible |

**Median OS by location and subtype:**
- DIPG (children): 9-11 months from diagnosis without modern therapy; 14-17 months with RT + ONC201 era
- Thalamic DMG (pediatric): 12-18 months
- Thalamic/spinal DMG (adult): 14-24 months (slightly better)
- Adult cerebellar DMG: 18-28 months (most favorable H3K27M DMG subgroup)

## Structure

### Molecular subtypes and co-driver mutations

**H3.3K27M (H3F3A)** — ~75% of all H3K27M DMG:
- Pontine and thalamic locations
- Co-mutations: PDGFRA (amplification or D842V/N659K point mutations ~25-35%), PIK3CA/R1 (~15%), NF1 (~10%), ATRX (~15%)
- Slightly older pediatric/young adult age (median 8-10 years for DIPG, 15-20 years for thalamic)
- Slightly worse prognosis than H3.1K27M

**H3.1K27M (HIST1H3B/HIST1H3C)** — ~25% of all H3K27M DMG:
- Exclusively pontine (DIPG); the "pure DIPG" subtype
- Co-mutations: ACVR1 gain-of-function mutations (~40-50%, activating BMP signaling), PPM1D (~20%), HIST1H3B Q86R/H3.1K36M (rare)
- Younger age (median 5-7 years)
- Slightly longer OS than H3.3K27M DIPG (~11-13 months vs ~9-11 months)

**H3.2K27M (HIST2H3C)** — rare: similar biology to H3.1; predominantly pontine

**H3K27M-altered DMG, NOS:** small subset where H3K27M is confirmed but histone subtype undetermined

### Imaging and diagnosis

**MRI features of DIPG:**
- T1: hypointense, iso/hypointense; poorly marginated; encompasses >50% of pons in classic DIPG
- T2/FLAIR: hyperintense; engulfs basilar artery without encasing
- Enhancement: ring enhancement or heterogeneous enhancement (may indicate transformation); non-enhancing ~60% of classic DIPG
- DWI: variable; restricted diffusion in higher-grade regions
- MR spectroscopy: elevated choline:NAA ratio; elevated lactate in high-grade areas

**Biopsy:**
- Stereotactic biopsy of DIPG: historically avoided; now standard for molecular diagnosis and trial eligibility
- Pontine biopsy safety: <1% permanent neurological deficit in experienced centers; typically 2-3 core biopsies
- H3K27M IHC (clone D5E7): performed on biopsy; sensitivity ~95% for H3K27M+ DMG
- Liquid biopsy: CSF cfDNA H3K27M detection; plasma ctDNA (lower sensitivity); H3K27M ddPCR for monitoring

### IHC and molecular workup

**H3K27M IHC (D5E7 clone):** strong nuclear positivity; diagnostic; approved diagnostic antibody
**H3K27me3 IHC:** globally reduced/lost (contrast with normal brain parenchyma which is strongly H3K27me3+)
**EZH2 IHC:** expressed/overexpressed in tumor cells despite functional inactivation by H3K27M
**PDGFRA IHC:** overexpressed in ~40-50%; does not predict response without mutation confirmation
**Next-generation sequencing panel:** confirms H3K27M variant allele, identifies co-driver mutations (ACVR1, PIK3CA, NF1, PDGFRA) for clinical trial stratification
**FISH:** PDGFRA amplification, CDK6 amplification, MYCN amplification

## Function

### Oncogenesis: H3K27M epigenetic reprogramming

H3K27M-driven global H3K27me3 loss creates a fundamentally permissive chromatin state in DMG:

**De-repressed target programs:**
- **PDGFRA super-enhancer**: H3K27ac gain at PDGFRA locus → PDGFRA overexpression (even without genetic amplification); PDGFRA → MAPK/PI3K → proliferation
- **CDK6 enhancer de-repression**: CDK6 overexpression → RB1 hyperphosphorylation → E2F-driven cell cycle
- **Stem cell programs**: SOX2, OLIG2, NESTIN, ID1 maintained by loss of H3K27me3-mediated silencing → neural stem cell identity preserved; DMG cells remain in a progenitor state unable to terminally differentiate
- **HOX gene dysregulation**: posterior HOX genes de-repressed → aberrant positional identity
- **EMT programs**: CDH2 (N-cadherin), fibronectin, MMP9 → diffuse infiltration pattern (histological hallmark: "diffuse")

**The developmental timing hypothesis:**
H3K27M is only oncogenic in specific progenitor populations at specific developmental windows — during peak pontine/thalamic oligodendrogenesis. H3K27M in mature neurons or mature glia does not produce glioma. This explains: (1) the pediatric age peak of DIPG, (2) the pontine/thalamic predilection, (3) why adult H3K27M DMGs are less common (fewer susceptible progenitors exist).

## Pathology

### Treatment

**Radiation therapy (standard of care, first-line):**
- DIPG: 54 Gy in 30 fractions (1.8 Gy/fx) focal RT; conformal RT (IMRT or proton); whole-brain RT NOT used
- Radiological response: ~85% show T2/FLAIR reduction at 6-8 weeks post-RT; most are transient
- Median TTP after RT: 6-8 months; RT is palliative, not curative
- Re-irradiation at progression: 21-30 Gy additional; used in most centers; extends OS ~3-5 months
- Hypofractionated RT (39 Gy/13 fr or 54 Gy/18 fr): equivalent outcomes; preferred in young children or those unable to tolerate conventional fractionation

**ONC201 (imipridone) — FDA approved April 2024:**
First FDA-approved drug for H3K27M-mutant diffuse glioma; approved for adults and pediatric patients ≥1 year:
- Mechanism: DRD2/DRD5 antagonism → ISR/ATF4 activation + ClpP mitochondrial agonist → bioenergetic collapse selectively in H3K27M cells
- Dosing: 625 mg weekly (adult); pediatric weight-based weekly dosing
- Phase 2 (ACTION study): ORR ~22-30%; DCR ~60%; median OS ~15-17 months in H3F3A K27M cohort
- ONC201 crosses blood-brain barrier well (CNS penetrance ~40-60% relative to plasma)
- Toxicity: nausea, fatigue, elevated transaminases (grade 1-2); well tolerated
- Ongoing Phase 3 confirmatory trial

**Panobinostat (HDAC inhibitor):**
- Mechanism: H3K27ac reduction → partial H3K27me3 restoration at polycomb target loci
- Phase 1 PBTC-047: MTD established; CNS penetrance adequate at MTD; stable disease signals
- Phase 2 PBTC-047b (with RT): ongoing; primary endpoint: 12-month OS vs historical control
- Combination panobinostat + ONC201: synergistic in preclinical DMG models

**Targeted therapy (co-driver directed):**
- **ACVR1 inhibitors** (for ACVR1-mutant H3.1K27M DIPG): LDN-212854, M4K2009; preclinical activity; Phase 1 trials ongoing
- **PDGFRA inhibitors** (for PDGFRA-amplified/mutant DMG): avapritinib (PDGFRA D842V), dasatinib, imatinib; Phase 1/2 in PDGFRA-altered DMG
- **PI3K/mTOR inhibitors** (for PIK3CA/R1-mutant DMG): copanlisib, alpelisib; combination with ONC201 under investigation
- **MEK inhibitors** (for NF1-mutant DMG): selumetinib, trametinib; Phase 1 in NF1+H3K27M spinal DMG

**Immunotherapy:**
- DMG is immunologically cold: low TMB (~1-2 mut/Mb), minimal TILs, immunosuppressive microenvironment
- Anti-PD-1 (nivolumab, pembrolizumab): ORR <5% in single-agent trials
- CAR-T therapy targeting H3K27M peptide-MHC complex: preclinical; GD2-CAR-T (GD2 expressed on DIPG cells); B7H3-CAR-T; Phase 1 trials open (intrathecal delivery explored)
- Vaccine targeting H3K27M neoepitope: H3K27M is an ideal neoantigen target; Phase 1 peptide vaccine in H3K27M DMG ongoing (NCT03299309)

**Convection-enhanced delivery (CED):**
Direct infusion of drugs into the pons via stereotactic catheter; bypasses BBB; explored with panobinostat, ONC201, gemcitabine; early Phase 1 data; logistically complex; neurotoxicity at high doses

**Prognosis:**
- Median OS without treatment: ~3-5 months (DIPG untreated historic controls)
- Median OS with RT alone: ~9-11 months (DIPG); ~12-18 months (thalamic)
- Median OS with RT + ONC201 (post-RT maintenance): ~14-17 months (emerging data)
- 2-year OS: ~5-10% in DIPG; ~15-20% in thalamic DMG
- Long-term survivors (>3 years): ~5% of DIPG; often harbor specific molecular features (ACVR1 co-mutation, H3.1K27M)
- Predictors of longer OS: H3.1K27M (vs H3.3K27M), adult age, spinal location, no PDGFRA amplification, ONC201 response at 12 weeks by MRI

## Connections

- `connects-to` → **[H3K27M](../../03-molecular/h3k27m/README.md)** — H3K27M mutation in H3F3A or HIST1H3B defines WHO Grade 4 diffuse midline glioma (100% diagnostic criterion since 2021 WHO CNS classification); H3K27M IHC (anti-H3.3K27M, clone D5E7) is the diagnostic standard; TBXT-negative; H3K27M identifies tumor in CSF liquid biopsy.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — H3K27M inhibits EZH2/PRC2 activity in trans → global H3K27me3 loss; this dominant-negative epigenetic mechanism is the oncogenic hallmark of DMG; paradoxically, EZH2 protein is intact and overexpressed in H3K27M DMG; panobinostat (HDAC inhibitor) partially restores H3K27me3.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion in ~15-25% H3K27M DMG (higher in DIPG/thalamic subtypes); NF1+H3K27M co-alteration common in spinal DMG; CDKN2A loss → CDK4/6 → RB1 → E2F proliferation; palbociclib + ONC201 combination being explored in H3K27M+CDKN2A-deleted DMG.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGFRA point mutations and amplification occur in ~25-35% of H3K27M DMG; PDGFRA → MAPK/PI3K → glioma proliferation; PDGFRA co-mutation with H3K27M accelerates malignancy; avapritinib and imatinib explored in PDGFRA-mutant DMG subsets.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 mutations in ~10% of H3K27M DMG, enriched at spinal cord location; NF1 LOF → constitutive RAS-MAPK → MEK-ERK proliferation; NF1+H3K27M spinal DMG shows high macrophage infiltration; selumetinib and trametinib (MEK inhibitors) explored in NF1-mutant H3K27M spinal DMG.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA/PIK3R1 mutations in ~15% of H3K27M DMG; PI3K-AKT-mTOR cooperates with H3K27M epigenetic reprogramming; alpelisib (PI3Kα inhibitor) and copanlisib in combination with ONC201 under investigation; PTEN loss is an alternative PI3K pathway activation mechanism in DMG.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — H3K27M DMG and IDH-wildtype GBM are both WHO Grade 4 but molecularly distinct; GBM shows EGFR amplification/EGFRvIII, TERT promoter mutation, CDK4/6 amplification absent in DMG; ONC201 active in DMG but not GBM; bevacizumab benefits GBM (PFS) but not H3K27M DMG.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Diffuse midline glioma grows in the brain's midline — pons (DIPG), thalamus, and spinal cord — where infiltrative spread makes surgery impossible; the pontine location compresses cranial nerve nuclei and long tracts, and radiation is the only treatment that briefly helps.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — DMG arises from oligodendrocyte precursor cells (OPCs) of the developing midline: the H3K27M mutation freezes these cells in a proliferative, stem-like state by stalling differentiation, which is why the tumor peaks at ages 5-10 when OPCs are most active in the pons.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — The DMG microenvironment is rich in microglia and macrophages, especially NF1-mutant spinal tumors, but these are immunosuppressive rather than tumoricidal — one reason checkpoint inhibitors have largely failed and GD2-directed CAR-T is being explored instead.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Diffuse midline glioma and medulloblastoma are the two great malignant pediatric brain tumors at opposite poles: DMG is an unresectable, fatal H3 K27M brainstem glioma, while medulloblastoma is a resectable cerebellar tumor often cured by surgery plus craniospinal radiotherapy.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Diffuse midline glioma arises from an OPC-like glial precursor of the astrocyte/oligodendrocyte lineage: the H3 K27M oncohistone freezes these cells in a stem-like state by collapsing H3K27 methylation, so the tumor infiltrates the pons diffusely rather than forming a mass.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is the only treatment that reliably helps diffuse midline glioma: focal irradiation of the pons gives transient symptom relief and a few months' benefit, but the H3 K27M tumor inevitably regrows—no chemo, surgery, or re-irradiation is curative.
- `connects-to` → **[IDH-mutant glioma](../idh-mutant-glioma/README.md)** — Diffuse midline glioma and IDH-mutant glioma are epigenetically opposite gliomas: DMG's H3 K27M oncohistone collapses methylation in children with dismal outcomes, while adult IDH-mutant gliomas accumulate 2-HG and fare far better—chromatin reprogramming, not oncogenes.
- `connects-to` → **[Atypical teratoid/rhabdoid tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Diffuse midline glioma and ATRT are aggressive pediatric brain tumors driven by epigenetic dysregulation: DMG by the H3 K27M histone mutation, ATRT by SMARCB1/SWI-SNF loss—both reprogram chromatin and carry a grim prognosis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Diffuse midline glioma forms synapses with neurons to grow: the tumor's OPC-like cells receive glutamatergic input through real neuron-to-glioma synapses that drive proliferation—so neuronal activity feeds the cancer, making activity-blocking drugs a therapeutic idea.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation frequently accompanies the H3K27M driver in DMG: loss of p53 removes the damage checkpoint atop the epigenetic catastrophe of histone mutation, accelerating this fatal pediatric brainstem tumor—a partnership of epigenetic and tumor-suppressor failure.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 amplification helps drive DMG's relentless growth: alongside H3K27M, gains in the cell-cycle machinery push tumor cells past the G1 checkpoint, making CDK4/6 inhibitors one of the targeted strategies tested against this otherwise untreatable tumor.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — DMG often activates the PI3K/AKT/mTOR pathway: mutations in PIK3CA and related genes switch on mTOR-driven growth alongside the H3K27M epigenetic driver, so mTOR-pathway inhibitors are explored as targeted therapy for this lethal midline glioma.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Diffuse midline glioma is the deadliest pediatric tumor of the nervous system: it infiltrates the brainstem (as DIPG), thalamus or spinal cord diffusely, so it cannot be resected and disrupts the very structures that control breathing, movement and consciousness.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Germline TP53 loss in Li-Fraumeni syndrome predisposes to midline gliomas: while most diffuse midline gliomas are sporadic H3K27M-driven, the syndrome shows how inherited tumor-suppressor loss can also seed these lethal childhood brain cancers.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy has been tried in diffuse midline glioma to spare the developing brain: its sharp dose falloff limits collateral damage near the brainstem, but because the tumor infiltrates diffusely and resists treatment, it has not improved the grim prognosis.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Diffuse midline glioma hijacks the synapse: tumor cells form real synapses with neurons and grow in response to neuronal activity, so brain electrical signaling literally feeds the cancer—a discovery opening neuroscience-based therapies for this lethal childhood tumor.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Diffuse midline glioma is a frontier for T-cell therapy: GD2-directed CAR-T cells have shrunk these previously untreatable pontine tumors in early trials, so engineered cytotoxic T cells offer the first real hope against a near-uniformly fatal cancer.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate drives diffuse midline glioma growth: neuron-released glutamate acting on tumor AMPA receptors stimulates proliferation, so the same excitatory signaling that runs the brain fuels the cancer—making glutamate pathways a therapeutic target.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Diffuse midline glioma's most promising drug works on dopamine signaling: ONC201 (dordaviprone) antagonizes the dopamine D2 receptor (and mitochondrial ClpP) and has produced rare responses in H3K27M tumors, a surprising therapeutic angle in an otherwise fatal cancer.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — A thalamic subset of diffuse midline glioma is driven by EGFR: bithalamic H3-wildtype midline gliomas carry EGFR mutations rather than H3K27M, so molecular testing splits these tumors into biologically distinct, differently-targetable groups.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Diffuse midline glioma is a target for NK and cell therapies: because it is so hard to resect or irradiate, engineered NK cells and GD2 CAR-T are being tested to attack the tumor immunologically where surgery and drugs fail.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Diffuse midline glioma grows on calcium from neuron-glioma synapses: real synapses form between neurons and tumor cells, and the glutamate-driven calcium influx through them spurs the cancer to proliferate—a striking link between brain activity and tumor growth.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Diffuse midline glioma recruits blood supply via VEGF: though infiltrative, the tumor releases VEGF to coax new vessels and loosen the blood-brain barrier, a process studied as a target in a cancer that resists almost all therapy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Tumor-associated microglia feed diffuse midline glioma through NF-kB: this inflammatory switch in the brain's immune cells drives cytokines that support the glioma's growth, part of the supportive niche around this lethal pediatric tumor.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Diffuse midline glioma announces itself in the eyes: a pontine tumor first palsies the cranial nerves that move the eyes and face, so double vision, a crossed eye, and facial droop are classic early signs of DIPG.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Diffuse midline glioma ultimately stops the breath: as it destroys the brainstem's control of breathing and swallowing, patients lose airway protection and respiratory drive, the failure that ends this lethal disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Diffuse midline glioma works on endothelial cells: VEGF from the tumor loosens the blood-brain barrier these cells form and recruits new vessels, both feeding growth and complicating drug delivery to the brainstem.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Diffuse midline glioma destabilizes the brainstem's autonomic control: infiltrating the pons it disrupts the centers governing heart rate and blood pressure, causing dangerous swings late in the disease.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Diffuse midline glioma picks off the cranial nerves: invading the pons it palsies the nerves controlling eye movement, the face and swallowing, the cranial-nerve deficits that often herald it.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Some diffuse midline gliomas are driven by activin signaling: ACVR1 mutations switch on the activin-A/BMP pathway, a recurrent driver in the pontine tumors of young children and a drug target.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy made a startling discovery: real synapses form between healthy neurons and glioma cells, the neuron's terminal wiring directly onto the tumor — an electrical hijacking that drives the cancer's growth.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — The tumor plugs into the brain's electricity: glioma cells carry potassium and other ion channels that let them depolarize in response to neuronal firing, the electrical excitability that the neuron-glioma synapse feeds and that spurs invasion.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Glutamate from the neuron-glioma synapse pours sodium into the tumor: AMPA-receptor currents flood the glioma cell with sodium and calcium, the depolarizing signal by which neural activity literally powers the cancer's spread.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Engineered antibody-based cells offer new hope: GD2-directed CAR-T cells have shrunk H3K27M-mutant diffuse midline gliomas in early trials, the first therapy to dent a tumor that radiation only briefly holds.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Its pontine home wrecks swallowing: the tumor infiltrates the brainstem's bulbar centers, so dysphagia and impaired airway protection bring aspiration and the need for feeding tubes as the disease advances.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Radiation and chemotherapy thin the blood: the craniospinal radiation and any added chemotherapy suppress the marrow, dropping neutrophils and raising the infection risk during the months of treatment.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — A midline tumor sits beside the master glands: thalamic and pontine gliomas and the radiation aimed at them border the hypothalamus and pituitary, so survivors face deficits of growth, thyroid and sex hormones that need lifelong endocrine follow-up.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — A subset of these gliomas amplify MYC: alongside the defining H3K27M mutation, MYC or PVT1 amplification drives some diffuse midline gliomas, adding a proliferative push that marks particularly aggressive, fast-growing tumors.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The tumor is immunologically cold: it carries few mutations to flag and recruits regulatory T cells that suppress attack, an immune-evasive microenvironment that has frustrated immunotherapy and shapes the GD2 CAR-T trials now under way.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β helps the glioma spread and hide: it drives the diffuse invasion through the brainstem and dampens the local immune response, part of why these tumors are unresectable and immune-resistant.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages fill the tumor but don't fight it: monocyte-derived macrophages, alongside microglia, dominate the DMG microenvironment in an immunosuppressive state that helps the cancer evade attack.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — An NF1 background can seed the glioma: loss of the NF1 tumor suppressor is a recurrent driver of diffuse midline glioma, and the syndrome's lifelong predisposition to gliomas links it to this lethal childhood tumor.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — ATRX loss often joins the H3K27M hit: especially in thalamic and spinal diffuse midline gliomas, ATRX mutation accompanies the histone mutation, driving alternative lengthening of telomeres and genomic instability.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — The infiltrating glioma irritates the cortex: as diffuse midline glioma spreads from the pons or thalamus it can trigger seizures, and seizure control is part of the supportive care for these children.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Brainstem and spinal infiltration brings pain: tumor invasion of sensory pathways causes neuropathic pain and, in spinal diffuse midline glioma, radicular pain — a symptom burden central to palliative management.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 supports the H3K27M-driven tumor: diffuse midline glioma cells show STAT3 activation that backs proliferation and immune evasion, a pathway studied for this almost uniformly fatal childhood brainstem tumor.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Brain tumors are strongly prothrombotic: like other high-grade gliomas, diffuse midline glioma raises venous thromboembolism risk through tumor tissue factor and the immobility that progressive brainstem disease brings.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Brainstem failure routes food to the lungs: as the tumor disables swallowing and airway protection, aspiration pneumonia becomes common, and it with the immunosuppression of high-dose steroids can progress to sepsis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its radiation can scar the brain's vessels: the high-dose radiotherapy that is the mainstay of palliation for diffuse midline glioma injures cerebral vessels, causing a delayed vasculopathy and stroke risk in longer survivors.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An almost uniformly fatal childhood tumor devastates: the relentless brainstem decline and dismal prognosis of diffuse midline glioma impose profound depression and grief on patients and families.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Advanced disease and its therapy blunt the marrow: progressive tumor burden with its inflammation, plus any chemotherapy and radiation, depress erythropoiesis into an anemia of chronic disease late in the course.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its steroids raise blood sugar: the high-dose dexamethasone used to control peritumoral edema in diffuse midline glioma induces insulin resistance, frequently causing steroid-induced hyperglycemia and diabetes.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Steroids and radiation blunt immunity: the prolonged dexamethasone and cranial radiation for diffuse midline glioma suppress immune defense, occasionally permitting invasive aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Chronic steroids impair repair: the long-term dexamethasone needed to manage symptoms of diffuse midline glioma thins skin and slows healing of surgical biopsy and other wounds.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It strikes the brain's breathing centre: diffuse midline glioma of the pons infiltrates the brainstem respiratory and cardiovascular nuclei, so progression leads to respiratory failure, a common terminal event.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Brainstem invasion robs swallowing: the pontine and bulbar involvement of diffuse midline glioma causes dysphagia and aspiration, driving the need for modified feeding or a gastrostomy.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A uniformly fatal childhood tumour breeds anguish: the dismal prognosis and relentless neurological decline of diffuse midline glioma impose profound anxiety on families alongside depression.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Treatment burdens the growing body: craniospinal radiation impairs growth and the long-term high-dose dexamethasone used to control oedema causes steroid myopathy and bone loss.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Radiation and steroids mark the skin: radiotherapy causes dermatitis over the treatment field, and the dexamethasone needed for mass effect brings acne, striae and skin thinning.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its steroids suppress immunity: the prolonged dexamethasone used to control peritumoural oedema blunts immune defence, raising infection risk including Pneumocystis pneumonia.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It sits at the body's control centre: a pontine diffuse midline glioma can disturb the brainstem cardiorespiratory and autonomic centres, causing blood-pressure and heart-rate instability.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Treatment reaches the hormone axis: radiation near the hypothalamus and pituitary can disturb puberty and fertility in children surviving midline glioma.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Long steroids invite an opportunist: the prolonged dexamethasone used for diffuse midline glioma suppresses immunity enough to risk Pneumocystis pneumonia, so prophylaxis is advised.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Epigenetic and targeted drugs are the hope: ONC201/dordaviprone and agents aimed at the H3K27M-driven PRC2/EZH2 dysregulation are the leading experimental therapies for this otherwise untreatable tumour.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Cell therapy enters the brainstem: GD2- and B7-H3-directed CAR-T cells have produced the first meaningful responses in H3K27M diffuse midline glioma, a landmark for solid-tumour cell therapy.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Conventional chemo barely helps: diffuse midline glioma is notoriously chemoresistant and the intact blood-brain barrier keeps drugs out, leaving radiation as the only standard treatment.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold tumour: diffuse midline glioma has a low mutational burden and sparse T-cell infiltrate in an immunosuppressed brain, so checkpoint inhibitors have shown little benefit, redirecting effort to engineered cell therapies.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — It infiltrates along the white matter: diffuse midline glioma spreads diffusely through the pons and brainstem tracts rather than as a resectable mass, weaving among axons in a way that makes surgery impossible.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — A shared GD2 target: both diffuse midline glioma and neuroblastoma express the GD2 disialoganglioside, and GD2-directed CAR-T and antibody therapy developed for neuroblastoma now show promise against this glioma.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Neuron-glioma synapses: neuronal activity and BDNF-TrkB signalling drive diffuse midline glioma growth through electrical and paracrine synapses with neurons, a discovery reframing the tumour as part of a neural circuit.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Immortality without TERT: ATRX loss in diffuse midline glioma maintains telomeres by alternative lengthening (ALT) rather than the TERT-promoter activation other cancers use—two routes to replicative immortality.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Cognition in the crossfire: midline and thalamic tumours, and the radiotherapy that palliates them, injure the hippocampus and memory circuits, adding neurocognitive decline to the disease's burden.
- `connects-to` → **[Chordoma](../chordoma/README.md)** — Midline tumours of the neuraxis: diffuse midline glioma (brainstem, thalamus, cord) and chordoma (clivus, sacrum) both arise along the body's midline axis, posing similar surgical-access challenges despite different origins.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — The CNS-tumour spectrum: against the lethal, infiltrative diffuse midline glioma, meningioma represents the benign, resectable extreme of brain tumours—two poles of neuro-oncology.
- `connects-to` → **[PCNSL](../pcnsl/README.md)** — Deep brain masses on imaging: a brainstem or thalamic mass raises a differential that includes diffuse midline glioma and, in older or immunocompromised patients, primary CNS lymphoma, told apart by biopsy and steroid response.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle amplification: CDK4/6 and cyclin D gains drive cell-cycle progression in diffuse midline glioma, a recurrent secondary lesion and the rationale for CDK4/6 inhibition.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT survival: PIK3CA-activated AKT signalling feeds the mTOR pathway sustaining diffuse midline glioma cells, a cooperating driver alongside the defining H3K27M mutation.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Growth-factor dependence: IGF-1/IGF1R signalling supports the proliferation and survival of diffuse midline glioma cells, an investigational therapeutic vulnerability in this lethal tumour.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic pons: HIF-1α stabilised in the hypoxic, infiltrative diffuse midline glioma drives the VEGF angiogenesis and metabolic adaptation that support its growth in the brainstem.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Receptor amplification: MET amplification occurs in a subset of diffuse midline gliomas, marking an actionable receptor tyrosine kinase alongside the defining H3K27M epigenetic lesion.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — Rare actionable fusion: NTRK fusions, though uncommon, render some diffuse midline gliomas sensitive to TRK inhibitors, a precision-oncology option for this otherwise untreatable tumour.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Myeloid microenvironment: CCL2 recruits microglia and monocyte-derived macrophages that dominate the diffuse midline glioma microenvironment, supporting an immunosuppressive niche resistant to immunotherapy.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RTK-MAPK signalling: RAS-RAF-ERK signalling downstream of PDGFRA and EGFR amplification drives proliferation in diffuse midline glioma, complementing its defining H3K27M epigenetic reprogramming.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Cell-cycle deregulation: CDKN2A loss and CDK4/6 activity unleash E2F1-driven cell-cycle entry in diffuse midline glioma, sustaining the relentless proliferation of this lethal tumour.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on diffuse midline glioma cells follows CXCL12 gradients along white-matter tracts, driving the diffuse brainstem infiltration that makes the tumor inoperable and defines its lethal natural history.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Radiotherapy—the only treatment that meaningfully helps in DIPG—kills tumor cells through caspase-3-mediated apoptosis, but apoptosis resistance underlies the inevitable relapse after the transient clinical response.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — RAD51-mediated homologous-recombination repair helps diffuse midline glioma survive radiation-induced DNA damage, a mechanism of the radioresistance that limits the durability of the only effective treatment.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Diffuse midline glioma cells form functional AMPA-receptor synapses with neurons, and the resulting calcium-mediated electrical activity drives tumor proliferation—a striking dependence on neuronal activity that opens new therapeutic angles.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — GD2-directed CAR-T cells, the first immunotherapy to show responses in diffuse midline glioma, kill the GD2-expressing tumor cells through perforin and granzyme, a breakthrough against this previously untreatable cancer.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — The H3K27M mutation globally reshapes the epigenome, redistributing DNA methylation alongside the loss of PRC2-mediated H3K27 trimethylation, the epigenetic catastrophe at the root of diffuse midline glioma.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates the PI3K-AKT-mTOR axis (PIK3CA, AKT and mTOR already mapped), a recurrent co-alteration with H3K27M that supports growth in diffuse midline glioma.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling sustains the neural-progenitor-like state that the H3K27M epigenetic reprogramming exploits, helping maintain the stem-like, proliferative cell population of diffuse midline glioma.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB-E2F axis (CDK4/6, cyclin-D1, CDKN2A and E2F1 all already mapped) is deregulated in diffuse midline glioma, and RB inactivation releases the cell-cycle progression these tumors depend on.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (NF1 loss and ERK1/2 already mapped) provides a proliferative input cooperating with the H3K27M epigenetic reprogramming that defines diffuse midline glioma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) supports the survival and immunosuppressive microenvironment of diffuse midline glioma.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the profound radio- and chemo-resistance of diffuse midline glioma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — ACVR1-activin-SMAD signaling (activin-A mapped) is constitutively activated by the ACVR1 mutations that co-occur with H3K27M in diffuse midline glioma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the invasive and immunosuppressive phenotype of diffuse midline glioma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment and radiation response of diffuse midline glioma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immunologically cold microenvironment of diffuse midline glioma, a barrier to its immunotherapy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the metabolic and oxidative stress of the H3K27M-driven tumor cells of diffuse midline glioma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling modulates the neural-progenitor proliferation and survival programs hijacked by diffuse midline glioma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in diffuse midline glioma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the immunosuppressive microenvironment of diffuse midline glioma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling downstream of PDGFR (PDGF already mapped) drives the invasive signaling of diffuse midline glioma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of the H3K27M-driven cells of diffuse midline glioma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation cooperating with the H3K27M mutation of diffuse midline glioma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the brainstem-infiltrating cells of diffuse midline glioma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven microglial and myeloid recruitment shapes the immunosuppressive microenvironment of diffuse midline glioma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of diffuse midline glioma.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt-β-catenin signaling participates in the glioma-stem-cell maintenance of diffuse midline glioma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of diffuse midline glioma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of diffuse midline glioma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammatory microenvironment of diffuse midline glioma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of diffuse midline glioma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of diffuse midline glioma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microglial/macrophage-rich tumor microenvironment and invasion of diffuse midline glioma.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — GD2 CAR-T therapy: IL-2-driven T-cell expansion powers the GD2-directed CAR-T therapy that has produced striking early responses in H3K27M diffuse midline glioma, a landmark immunotherapy for this otherwise uniformly fatal tumour.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen presentation: MHC class II-restricted antigen presentation shapes the T-cell response to diffuse midline glioma, relevant to the peptide vaccines targeting the H3K27M neoantigen (already mapped) being tested in this tumour.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint context: diffuse midline glioma is an immunologically cold tumour, and PD-1 checkpoint blockade is explored in combination with CAR-T and vaccine strategies to sustain the anti-tumour T-cell response.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: the anti-inflammatory cytokine IL-10 helps make diffuse midline glioma an immunologically cold tumour (PD-1 already mapped), blunting the T-cell response that CAR-T and vaccine strategies aim to mount.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Neuronal activity: alongside the glutamatergic neuron-glioma synapses (glutamate already mapped), GABAergic signalling modulates the neuronal electrical activity that drives the growth of diffuse midline glioma, an emerging neuro-oncology target.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide regulates vascular tone and, with VEGF (already mapped), the angiogenesis and hypoxic microenvironment of diffuse midline glioma, part of the stromal biology of this infiltrative brainstem tumour.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia (already mapped) and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6 and IL-1 already mapped) of the diffuse midline glioma microenvironment.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative microenvironment: the infiltrative diffuse midline glioma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of its hypoxic (HIF-1-alpha already mapped) tumour microenvironment.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 microglial polarisation: IL-4 polarises the tumour-associated microglia and macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive niche of diffuse midline glioma.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 arm and CAR-T target: IL-13, with IL-4 (already mapped), supports the M2 microglial niche, and the IL-13 receptor alpha-2 is a target of the CAR-T-cell approaches being trialled against diffuse midline glioma.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Neuron-glioma signalling: alongside the glutamate and GABA (already mapped) synapses, cholinergic acetylcholine signalling is part of the neuronal activity that drives the growth of the electrically integrated diffuse midline glioma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Ferroptosis vulnerability: the iron-dependent lipid peroxidation of ferroptosis is a metabolic vulnerability of diffuse midline glioma (xanthine oxidase and oxidative stress already mapped), an emerging therapeutic angle in this incurable tumour.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonergic neuromodulation: serotonin modulates the neuron-glioma (glutamate, GABA and dopamine already mapped) circuits whose activity drives the growth of the electrically integrated diffuse midline glioma.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Noradrenergic input: noradrenaline is part of the neuronal-activity-dependent (glutamate already mapped) signalling that stimulates the proliferation of diffuse midline glioma.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipid metabolic dependency: the cholesterol and lipid metabolism on which diffuse midline glioma depends is a metabolic vulnerability, alongside the ferroptosis (iron already mapped), being explored therapeutically.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Tumour-associated microglia: the microglia and macrophages (CCL2 already mapped) dominate the immunosuppressive, immunologically cold microenvironment of the diffuse midline glioma.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — High-grade-glioma differential: the diffuse midline glioma (H3K27M already mapped) is a distinct WHO-grade-4 midline glioma, molecularly separate from the adult, IDH-wildtype glioblastoma.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Palliative radiotherapy: the focal photon radiotherapy is the only standard treatment of the diffuse midline glioma, providing the temporary response of the incurable tumour.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, explored with the GD2 CAR-T and checkpoint (PD-1 already mapped) trials in diffuse midline glioma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immunosuppressive microenvironment of diffuse midline glioma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of diffuse midline glioma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immunosuppressive microenvironment of diffuse midline glioma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the diffuse-midline-glioma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of diffuse midline glioma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) and myeloid activation of the immunosuppressive microenvironment of diffuse midline glioma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the sparse immune infiltrate of the immunologically cold diffuse midline glioma.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the tumour antigen (MHC already mapped) to the T cells (already mapped), a rationale for the GD2 CAR-T and vaccine immunotherapy of diffuse midline glioma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the microglial (already mapped) and myeloid inflammation of the diffuse-midline-glioma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the diffuse-midline-glioma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack in the immunologically cold tumour.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the H3K27M-mutant (already mapped) glioma cells and the disordered brain-iron handling of diffuse midline glioma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-DMG axis: TSLP, from the DMG stromal cells and astrocytes (already mapped), primes dendritic cells (already mapped) and amplifies the Th2-skewed immunosuppressive microenvironment of the H3K27M-mutant (already mapped) diffuse midline glioma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-DMG axis: bradykinin, via B1/B2 receptors on the DMG tumour endothelium (already mapped) and microglia (already mapped), augments blood-brain-barrier permeability, oedema, and the inflammatory milieu of diffuse midline glioma.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-DMG axis: erythropoietin, induced by the HIF-1α (already mapped) hypoxia of the DMG tumour core, activates the EPOR on H3K27M-mutant (already mapped) glioma cells and modulates macrophage/microglia (already mapped) polarisation.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell DMG axis: histamine, from the mast cells (already mapped) in the DMG tumour microenvironment and brain border compartments, amplifies the blood-brain-barrier permeability and the immunosuppressive neuroinflammatory milieu of DMG.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-H3K27M axis: melatonin, via MT1/MT2 receptors on H3K27M-mutant (already mapped) glioma cells and microglia (already mapped), modulates the epigenetic-hypoxic (HIF-1α already mapped) stress and the immunosuppressive milieu of DMG.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation can contribute to the neuroinflammatory milieu and the blood-brain-barrier disruption of DMG.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — DMG oxytocin: oxytocin, via OXTR on microglia (already mapped) and macrophages (already mapped), attenuates neuroinflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive cascade of diffuse midline glioma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — DMG vasopressin: vasopressin, via V1aR on microglia (already mapped) and macrophages (already mapped), modulates neuroinflammation; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) glioma-promoting cascade of diffuse midline glioma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — DMG selenium: selenium, via selenoprotein activity in microglia (already mapped) and glioma cells, suppresses the oxidative stress that amplifies the NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive neuroinflammatory cascade of diffuse midline glioma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — DMG prolactin: prolactin, via PRLR on microglia (already mapped) and macrophages (already mapped), modulates neuroinflammation; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) glioma-promoting immunosuppressive cascade of diffuse midline glioma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — DMG testosterone: testosterone, via androgen receptors on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; testosterone deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of diffuse midline glioma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — DMG iodine: iodine-dependent thyroid hormones modulate microglia (already mapped) polarisation and neuroinflammation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive glioma cascade of diffuse midline glioma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — DMG magnesium: magnesium cofactors kinase signalling in microglia (already mapped) and macrophages (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive neuroinflammatory glioma cascade of diffuse midline glioma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — DMG copper: copper supports microglia (already mapped) and macrophage (already mapped) antioxidant function; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive neuroinflammatory cascade of diffuse midline glioma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — DMG zinc: zinc cofactors microglia (already mapped) and macrophage (already mapped) anti-tumour immune function; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) immunosuppressive glioma cascade of diffuse midline glioma.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — phosphorus, as ATP in microglia (already mapped) and macrophage (already mapped), fuels mTOR (already mapped) glioma proliferative signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and p53 (already mapped) immunosuppressive cascade.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride channels on microglia (already mapped) and macrophage (already mapped) regulate membrane potential; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) immunosuppressive glioma cascade of diffuse midline glioma.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — sulfur, as glutathione precursor in microglia (already mapped) and macrophage (already mapped), counters oxidative stress; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) glioma cascade of diffuse midline glioma.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — DMG carbon: carbon in nucleotides fuels microglia (already mapped) and macrophage (already mapped) glioma growth; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) immunosuppressive cascade of diffuse midline glioma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — DMG hydrogen: hydrogen via ROS from microglia (already mapped) and macrophage (already mapped) modulates glioma redox; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) immunosuppressive cascade of diffuse midline glioma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — DMG nitrogen: nitrogen in DNA bases of microglia (already mapped) and macrophage (already mapped) sustains glioma growth; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and mTOR (already mapped) cascade of diffuse midline glioma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^schwartzentruber-2012-h3f3a-glioma]: Schwartzentruber J, Korshunov A, Liu XY, et al. Driver mutations in histone H3.3 and chromatin remodelling genes in paediatric glioblastoma. *Nature.* 2012;482(7384):226-231. [doi:10.1038/nature10833](https://doi.org/10.1038/nature10833) · [PubMed 22286061](https://pubmed.ncbi.nlm.nih.gov/22286061/)
[^khuong-quang-2012-h3k27m-dipg]: Khuong-Quang DA, Buczkowicz P, Rakopoulos P, et al. K27M mutation in histone H3.3 defines clinically and biologically distinct subgroups of pediatric diffuse intrinsic pontine gliomas. *Acta Neuropathol.* 2012;124(3):439-447. [doi:10.1007/s00401-012-0998-0](https://doi.org/10.1007/s00401-012-0998-0) · [PubMed 22661320](https://pubmed.ncbi.nlm.nih.gov/22661320/)
