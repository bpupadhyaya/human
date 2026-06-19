---
schema: human-scale-entry/v1
id: neurofibromatosis-type-2
name: Neurofibromatosis Type 2
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Neurofibromatosis type 2 (NF2) is caused by germline NF2 mutations; bilateral vestibular schwannomas are pathognomonic; meningiomas, ependymomas also occur; merlin activates Hippo-YAP1; bevacizumab improves hearing; TEAD inhibitors in clinical trials."
aliases: ["NF2", "neurofibromatosis type 2", "NF2 syndrome", "bilateral acoustic neuroma", "NF2 vestibular schwannoma", "NF2 merlin", "NF2 bevacizumab", "neurofibromatosis 2", "acoustic neuroma hereditary"]
sources:
  - id: asthagiri-2009-nf2-lancet
    type: peer-reviewed
    cite: "Asthagiri AR, Parry DM, Butman JA, et al. Neurofibromatosis type 2. Lancet. 2009;373(9679):1974-1986."
    doi: "10.1016/S0140-6736(09)60259-2"
    pmid: "19476995"
    url: "https://doi.org/10.1016/S0140-6736(09)60259-2"
  - id: plotkin-2009-nf2-bevacizumab
    type: peer-reviewed
    cite: "Plotkin SR, Stemmer-Rachamimov AO, Barker FG 2nd, et al. Hearing improvement after bevacizumab in patients with neurofibromatosis type 2. N Engl J Med. 2009;361(4):358-367."
    doi: "10.1056/NEJMoa0902579"
    pmid: "19587327"
    url: "https://doi.org/10.1056/NEJMoa0902579"
cross_links:
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "Germline NF2 LOF causes NF2 disease; merlin (NF2) is a FERM domain protein that activates the Hippo pathway (MST1/2 → LATS1/2 → YAP phosphorylation); NF2 LOF → nuclear YAP → schwannoma/meningioma; somatic NF2 in mesothelioma, rare ccRCC, astrocytoma."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "YAP1 is the principal Hippo pathway effector released by NF2 LOF; nuclear YAP1-TEAD drives CTGF, CYR61, survivin target genes → schwannoma and meningioma proliferation; TEAD inhibitors (K-975, IK-930, VT3989) in clinical trials for NF2-deficient tumors."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Meningioma is the most common NF2 disease tumor; NF2 germline → bilateral and multiple meningiomas (and cranial nerve schwannomas); NF2 somatic LOF is the most common alteration in sporadic meningioma (~55%); RT avoided when possible in NF2 disease to prevent new tumor induction."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "NF2 somatic LOF in ~50% of mesothelioma → nuclear YAP1 → TEAD-driven survival; NF2 germline carriers have elevated mesothelioma risk (beyond asbestos exposure); TEAD inhibitors (K-975, VT3989) in clinical trials for NF2-deficient mesothelioma; merlin IHC loss in diagnosis."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VS stromal cells secrete VEGF (driven by nuclear YAP1), producing edema and vascularity that compress the cochlear nerve; bevacizumab (anti-VEGF) shrinks ~55% of growing vestibular schwannomas and improves hearing in ~57% — a non-surgical option for failing hearing."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "Schwannomatosis is the key NF2 mimic: both cause multiple schwannomas, but bilateral vestibular schwannomas are pathognomonic for NF2 and absent in schwannomatosis (SMARCB1/LZTR1, chronic-pain-predominant); a gene panel and dedicated internal-auditory-canal MRI separate them."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "NF2 schwannomas arise from the Schwann-cell sheath of cranial and peripheral nerves — bilateral on the vestibular nerve (CN VIII), plus spinal nerve-root schwannomas in ~43% (string-of-pearls on MRI); each tumor needs an independent somatic second hit at the NF2 locus."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "NF2 and NF1 share a name but are unrelated diseases: NF2 (merlin, a Hippo regulator) causes bilateral vestibular schwannomas and meningiomas, while NF1 (neurofibromin, a RAS-GAP) causes café-au-lait spots and neurofibromas — different genes, tumors, and pathways."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "NF2 is fundamentally a brain-and-nerve tumor syndrome: bilateral vestibular schwannomas on cranial nerve VIII cause progressive deafness, balance loss, and brainstem compression, alongside multiple meningiomas and ependymomas — tumor burden, not malignancy, drives the morbidity."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "The NF2/merlin-Hippo axis extends beyond nerve tumors: somatic NF2 loss occurs in a subset of renal cell carcinomas (as in mesothelioma), where merlin loss frees YAP/TEAD to drive proliferation — placing TEAD inhibitors under study for NF2-deficient kidney cancer too."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "NF2 and tuberous sclerosis are both autosomal-dominant neurocutaneous tumor syndromes, but of different pathways: NF2's Merlin loss drives schwannomas, meningiomas, and ependymomas via Hippo, while TSC's mTOR activation drives hamartomas across brain, kidney, and skin."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "NF2/Merlin and uveal melanoma converge on the Hippo pathway: Merlin normally restrains YAP, and uveal melanoma's GNAQ/GNA11 mutations activate YAP through Hippo—so both tumor biologies illustrate how unleashed YAP drives growth, here in the eye."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "NF2 produces glial as well as Schwann-cell tumors: spinal ependymomas and gliomas of astrocytic/ependymal lineage arise when Merlin loss disinhibits proliferation, part of the schwannoma-meningioma-ependymoma triad that defines the syndrome."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "NF2 and glioblastoma intersect through merlin: NF2 patients develop gliomas from biallelic NF2/merlin loss, and merlin is also inactivated in some sporadic glioblastomas—linking an inherited schwannoma/meningioma syndrome to malignant glioma."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "NF2 and von Hippel-Lindau are both dominant tumor-suppressor syndromes: NF2 (merlin loss) gives bilateral vestibular schwannomas and meningiomas, VHL gives hemangioblastomas and renal cancer—each one gene seeding a distinct tumor constellation."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye carries diagnostic clues to NF2: posterior subcapsular cataracts and retinal hamartomas are characteristic, often appearing before the bilateral vestibular schwannomas that define NF2—so an early cataract in a young person can prompt NF2 evaluation."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "NF2 is defined by tumors on the hearing nerve: bilateral vestibular schwannomas grow on cranial nerve VIII, compressing the neurons that carry sound and balance, so progressive deafness and imbalance in a young person are the hallmark of neurofibromatosis type 2."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiation is used cautiously in NF2: stereotactic radiosurgery can control vestibular schwannomas, but in NF2's tumor-prone, merlin-deficient tissue it risks inducing new tumors or malignant transformation—so timing and dose are weighed carefully against surgery."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Merlin loss in NF2 deranges growth signaling including mTOR: NF2's merlin normally restrains the Hippo pathway and mTOR-linked proliferation, so its loss drives schwannoma growth—making mTOR and VEGF (bevacizumab) inhibition rational targeted approaches."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "NF2 is defined by tumors throughout the nervous system: bilateral vestibular schwannomas on the hearing/balance nerves cause progressive deafness, alongside meningiomas and ependymomas—so merlin loss makes the nervous system the syndrome's near-exclusive target."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "NF2 has subtler skin findings than NF1: instead of café-au-lait spots and plentiful neurofibromas, patients develop a smaller number of cutaneous schwannomas and plaques, so the skin gives quieter but real clues to the diagnosis."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Radiation, including proton and stereotactic radiosurgery, treats NF2 schwannomas: focused radiation can control vestibular schwannomas near the brainstem without open surgery, though in NF2's multiple, recurring tumors it is weighed against the risk of further tumors."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "NF2 tumors grow when merlin stops restraining ERK: loss of the NF2 protein merlin unleashes Ras-ERK signaling that drives schwannoma and meningioma proliferation, motivating trials of MEK-pathway inhibitors in these tumors."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Merlin loss in NF2 drives cyclin D1: with the Hippo brake gone, cyclin D1 pushes cells through the cell cycle, explaining the relentless growth of the multiple schwannomas and meningiomas that define the syndrome."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "NF2 schwannomas depend on their blood supply: the tumors are richly vascular, and anti-VEGF bevacizumab—acting on endothelial cells—can shrink vestibular schwannomas and even recover some hearing, a rare medical therapy for these tumors."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "NF2 tumors turn dangerous when they also lose CDKN2A: while merlin loss alone makes benign schwannomas and meningiomas, added CDKN2A deletion drives the leap to malignant, fast-growing tumors—a key prognostic event."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "NF2 schwannomas are packed with macrophages: tumor-associated macrophages dominate these nerve-sheath tumors and correlate with their growth and the hearing loss they cause, making the immune niche a target to slow vestibular schwannomas."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NF2 tumors are studied as targets for NK and immune therapy: because repeated surgery and radiation risk nerve damage and hearing loss, immune approaches engaging natural killer cells are explored to control the schwannomas non-destructively."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "NF2's merlin loss unleashes growth via AKT-mTOR: without merlin's restraint, signaling flows into the PI3K-AKT-mTOR pathway alongside Hippo-YAP, driving the schwannomas and meningiomas—so mTOR-pathway drugs are studied to slow them."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "NF2 schwannomas grow on PDGF among other factors: autocrine growth-factor loops including PDGF feed the tumors, so PDGF-receptor and other kinase inhibitors are explored alongside the anti-VEGF drugs that can shrink vestibular schwannomas."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "NF2 tumors are studied as targets for cytotoxic T cells: because surgery and radiation risk hearing and nerve damage, engineered T-cell and other immunotherapies aim to control the schwannomas without destroying the nerves they sit on."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "NF2 destroys the ear's potassium-driven hearing: bilateral vestibular schwannomas crush the nerve carrying signals from cochlear hair cells, whose sound transduction runs on a potassium current—so hearing fades on both sides."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "NF2 cuts the synapses that relay sound and balance: as the schwannomas compress the vestibulocochlear nerve, the synaptic transmission from the inner ear to the brain fails, causing the deafness and unsteadiness."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "NF2's meningiomas are built with fibroblast-like cells: alongside the schwannomas, patients grow meningiomas whose fibrous, collagen-laying cells form firm masses that compress the brain and cord."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy fingerprints NF2's schwannomas: their cells wrap in continuous basal lamina and pile up long-spacing collagen as Luse bodies — ultrastructure that distinguishes a nerve-sheath tumor when histology alone is uncertain."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium betrays NF2's meningiomas: these slow-growing tumors deposit calcium in laminated psammoma bodies, giving the gritty calcification seen on CT that, scattered through the skull and spine, hints at multiple meningiomas."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations mark the dangerous ones: when an NF2-associated meningioma reactivates telomerase, it signals a more aggressive, recurrence-prone tumor — a molecular flag that pushes toward closer surveillance and earlier treatment."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "NF2's schwannomas come from the nerve's myelinators: the Schwann cell is the peripheral counterpart of the CNS oligodendrocyte, and loss of merlin lets these insulating cells pile up around the vestibular nerve into the hallmark bilateral tumors."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Schwannomas weave a telltale stroma: their loose Antoni B regions are rich in collagen and microcysts, while the compact Antoni A zones form palisading Verocay bodies — the matrix architecture pathologists read to call the tumor."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The NF2 gene is a frequent casualty in the chest: it is among the most commonly inactivated genes in pleural mesothelioma, the cancer of the membrane wrapping the lung, linking this tumor-suppressor to malignancy far beyond the nervous system."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody can save hearing in NF2: bevacizumab, a monoclonal against VEGF, shrinks vestibular schwannomas and recovers some hearing, while diffuse S100 and SOX10 stains confirm a schwannoma's Schwann-cell origin on biopsy."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "NF2 marks the skin in its own way: rather than NF1's café-au-lait neurofibromas, most patients carry cutaneous and subcutaneous schwannomas — raised plaques and nodules whose discovery in a young person can be the first prompt to look for the brain tumors."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy and inheritance both bear on NF2: vestibular schwannomas can accelerate during pregnancy, and as a dominant disorder each child of an affected parent faces a 50% risk, making genetic counseling central to family planning."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Bevacizumab is the main systemic NF2 drug: this anti-VEGF antibody can shrink vestibular schwannomas and preserve hearing, but by impairing the vessel lining it raises bleeding, clotting and platelet-related complications that must be watched."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "NF2's tumors are immunologically quiet: schwannomas and meningiomas recruit regulatory T cells and few effectors, a cold microenvironment that has limited immunotherapy and is studied to make these slow tumors more visible to attack."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its anti-VEGF therapy carries a vascular price: prolonged bevacizumab raises the risk of hypertension and arterial thromboembolic events including stroke, a trade-off weighed against the hearing it can save in NF2."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Merlin's day job is restraining receptors: the NF2 protein holds EGFR and other growth-factor receptors in check at the cell membrane and enforces contact inhibition, so losing it lets EGFR-driven signaling run on and feed the schwannomas and meningiomas."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Its brain tumors can spark seizures: the meningiomas and ependymomas that stud the nervous system in NF2 irritate the cortex, so epilepsy is among the ways the disease declares itself beyond the hallmark hearing loss."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "The tumors recruit inflammatory help: like the nerve-sheath tumors of NF1, NF2 schwannomas harbor infiltrating mast cells whose mediators are thought to support the tumor microenvironment and its slow, relentless growth."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "It anchors the schwannoma-predisposition spectrum: SMARCB1 (with LZTR1) causes schwannomatosis that overlaps NF2 clinically, so molecular testing distinguishes NF2 from these related multiple-schwannoma syndromes."
  - target: 01-human/03-molecular/lztr1
    relation: connects-to
    note: "LZTR1 marks the NF2 mimic: germline LZTR1 mutations cause a schwannomatosis that produces multiple schwannomas without the vestibular tumors of true NF2, a key genetic distinction in the differential."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Schwannomas on the nerves bring chronic pain: spinal and peripheral schwannomas in NF2 compress and irritate nerve roots, making neuropathic pain a major symptom alongside the hearing loss."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Merlin normally restrains NF-κB: its loss in NF2 lifts that brake, engaging NF-κB-driven survival and inflammatory signaling that supports the schwannomas and meningiomas of the syndrome."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Merlin loss activates STAT3: NF2-deficient schwannoma and meningioma cells show STAT3 signaling that backs their growth, one of the pathways downstream of the lost tumor suppressor."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Repeated CNS surgery carries infectious risk: NF2 patients undergo many operations for vestibular schwannomas and meningiomas over a lifetime, and these craniotomies can be complicated by meningitis and sepsis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Progressive deafness and tumor burden weigh on mood: NF2 typically takes hearing and balance in young adulthood while demanding repeated surgery, a combination that drives substantial depression and reduced quality of life."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Its neurosurgery and bevacizumab raise clot risk: long craniotomies with post-operative immobility, plus the anti-VEGF bevacizumab used to shrink vestibular schwannomas, together predispose NF2 patients to venous thromboembolism."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Anti-VEGF therapy drives up blood pressure: bevacizumab, used to control growing NF2 schwannomas and preserve hearing, blocks VEGF signaling in the vasculature and commonly produces new or worsened hypertension."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The same anti-VEGF drug spills protein into the urine: bevacizumab used long-term for NF2 schwannomas injures the glomerular filtration barrier, causing proteinuria and a gradual decline in kidney function."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Repeated neurosurgery and bevacizumab heal slowly: the many craniotomies NF2 demands, compounded by anti-VEGF therapy that impairs angiogenesis, leave surgical wounds prone to dehiscence and delayed closure."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Progressive deafness and endless tumours breed worry: the inexorable bilateral hearing loss, balance failure and lifelong brain-and-spine tumour surveillance of NF2 foster chronic health anxiety."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Losing balance topples the body: the bilateral vestibular schwannomas of NF2 destroy balance as well as hearing, and spinal tumours add weakness, together causing falls and fractures."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its anti-VEGF drug strains the vessels: the bevacizumab used to shrink NF2 schwannomas and preserve hearing causes hypertension and a recognised risk of arterial thromboembolic events."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The same drug can perforate the gut: bevacizumab therapy for NF2, by impairing angiogenesis, carries a risk of gastrointestinal bleeding and bowel perforation."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "High tumours can stop the breath: foramen-magnum and high cervical-cord schwannomas, ependymomas and meningiomas, or a phrenic-nerve schwannoma, can impair the respiratory muscles."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its biology and drug work on growth signals: merlin, the NF2 protein, enforces contact-dependent growth arrest, and the bevacizumab that shrinks vestibular schwannomas blocks tumour angiogenesis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its anti-angiogenic drug unsettles the thyroid: bevacizumab, used to shrink vestibular schwannomas in NF2, can cause hypothyroidism and hypertension as class effects of VEGF blockade."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Systemic therapy supplements surgery: when its schwannomas and meningiomas are too numerous to resect, NF2 is treated with targeted agents such as bevacizumab and trial mTOR and merlin-pathway inhibitors."
  - target: 01-human/07-system/gorlin-syndrome
    relation: connects-to
    note: "A fellow CNS-tumour syndrome: like Gorlin syndrome, NF2 is an autosomal-dominant disorder predisposing to nervous-system tumours, here multiple schwannomas, meningiomas and ependymomas."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "They share a schwannoma link: Carney complex causes psammomatous melanotic schwannomas, placing it alongside NF2 and schwannomatosis among the inherited schwannoma-predisposing syndromes."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "A limited role against its tumours: the schwannomas, meningiomas and ependymomas of NF2 are largely chemoresistant, managed by surgery and radiosurgery, with bevacizumab the main systemic option."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunologically quiet tumours: NF2-related schwannomas and meningiomas have low mutational burden and a cold microenvironment, so checkpoint inhibitors play little role."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Its meningiomas remodel bone: NF2 causes multiple meningiomas that provoke reactive hyperostosis of the skull, alongside its hallmark bilateral vestibular schwannomas."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Merlin loss drives liver cancer through YAP: the NF2 protein merlin restrains the Hippo effector YAP, so NF2 inactivation—somatic in many hepatocellular carcinomas—unleashes YAP-driven proliferation, linking the schwannoma gene to liver cancer."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Overlapping at SMARCB1: NF2-related and schwannomatosis tumours can involve SMARCB1, the SWI/SNF subunit whose biallelic loss defines atypical teratoid/rhabdoid tumours, tying nerve-sheath tumour biology to a malignant childhood CNS cancer."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The Hippo brake on organ size: merlin (NF2) signals cell-contact density to the Hippo pathway that caps proliferation, a mechanism vivid in the hepatic lobule where merlin loss lets hepatocytes overgrow—the tumour-suppressor role behind NF2 cancers."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Bilateral vestibular schwannomas: NF2's hallmark tumours arise from the Schwann cells of cranial nerve VIII, compressing the nerve and its axons to cause the progressive hearing loss and imbalance that define the syndrome."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Dense fibrous tumour stroma: NF2 schwannomas and meningiomas lay down a collagen-rich, fibroblastic matrix—the firm Antoni-A texture of schwannoma—and merlin loss promotes this profibrotic phenotype."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Hippo-YAP and heart regeneration: the merlin-Hippo-YAP pathway that NF2 disrupts is a leading target to coax the adult myocardium to regenerate after infarction, a striking spin-off from a nerve-tumour gene."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "The nerve-sheath-tumour family: NF2 produces benign Schwann-cell schwannomas while NF1 produces neurofibromas that can transform into MPNST, the two neurofibromatoses bracketing the spectrum of peripheral-nerve-sheath tumours."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "A disease of Schwann cells: NF2 tumours arise from the Schwann cells that ensheath peripheral nerves down to the neuromuscular junction, merlin loss driving their relentless proliferation along the nerve."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Meningioma-predisposing syndromes: NF2 is the leading germline cause of multiple meningiomas, while Li-Fraumeni patients develop them after radiotherapy—two inherited routes to the same intracranial tumour."
---

# Neurofibromatosis Type 2

## Overview

**Neurofibromatosis type 2 (NF2)** is an autosomal dominant hereditary tumor predisposition syndrome caused by germline pathogenic variants in the **NF2** tumor suppressor gene (chromosome 22q12.2; 17 exons; 595 aa merlin/schwannomin protein). NF2 is defined by the development of **bilateral vestibular schwannomas (acoustic neuromas)** — which are pathognomonic — along with a predisposition to meningiomas, spinal and cranial nerve schwannomas, ependymomas, and ocular abnormalities (posterior subcapsular cataracts, epiretinal membranes). NF2 affects approximately **1 in 25,000-33,000** individuals; ~50% of NF2 cases arise from de novo mutations (no family history). NF2 is clinically distinct from NF1 (von Recklinghausen disease): NF2 has fewer skin features, no Lisch nodules, different tumor spectrum, and a molecular basis in the **Hippo/YAP tumor suppressor pathway** rather than the RAS-MAPK pathway. Progressive bilateral sensorineural hearing loss (SNHL) and deafness are the primary sources of morbidity; **bevacizumab (anti-VEGF)** produces hearing improvement in a subset of patients with enlarging vestibular schwannomas [^asthagiri-2009-nf2-lancet] [^plotkin-2009-nf2-bevacizumab].

**Diagnostic criteria (revised NIH criteria + Manchester criteria):**

**NIH 1997 criteria — any one of the following:**
1. Bilateral vestibular schwannomas (on MRI)
2. First-degree relative with NF2 + either: unilateral VS diagnosed before age 30, OR any two of: meningioma, schwannoma, glioma, neurofibroma, posterior subcapsular lenticular opacity
3. Unilateral VS before age 30 + any one of: meningioma, schwannoma, glioma, neurofibroma, posterior subcapsular lenticular opacity

**Manchester criteria (more sensitive for early/mosaic diagnosis):**
- Includes bilateral VS, OR unilateral VS before 30 + additional NF2 features, OR multiple meningiomas + unilateral VS or any NF2 features, etc.

## Structure

### Genetic basis

**NF2 gene (22q12.2):**
- 17 exons; 595 aa merlin (schwannomin); FERM (4.1-Ezrin-Radixin-Moesin) domain superfamily
- Germline pathogenic variant spectrum: truncating nonsense/frameshift (~60%), splice site (~15%), missense (~15%), large deletions (~10%)
- De novo rate: ~50% of NF2 patients; among the highest de novo rates of major cancer predisposition syndromes (22q12 is a mutation hotspot)
- **Somatic mosaicism**: ~30% of apparent NF2 are somatic mosaic (postzygotic mutation) → milder phenotype; may have only unilateral VS or fewer tumors; germline testing negative, but tumor tissue testing or deep sequencing identifies mosaic allele

**Genotype-phenotype correlations:**
- **Wishart (severe) type**: truncating/frameshift variants, especially in exons 1-8 → young onset (often <20 years), rapid progression, bilateral VS + multiple meningiomas
- **Gardner (mild) type**: splice site variants, late exon missense, C-terminal truncations → onset 30s-40s, slower progression, bilateral VS often predominant
- Same mutation → variable expressivity within families; modifier genes and stochastic somatic second-hit timing influence phenotype

**Merlin protein — structure and Hippo activation:**
Merlin has an N-terminal FERM domain (α, β, γ lobes) that binds membrane lipids and cell surface proteins (CD44, PDGFR, ErbB2), and a C-terminal domain. Merlin exists in two conformations:
- **Closed (inactive)**: C-terminal intramolecular binds FERM → no Hippo activation; occurs in rapidly cycling cells
- **Open (active)**: head-to-tail intramolecular inhibition relieved (by Ser518 dephosphorylation, mediated by serum starvation, cell-cell contact) → merlin activates MST1/2 kinases → LATS1/2 → pYAP1 → cytoplasmic
- Ser518 phosphorylation (by p21-activated kinase PAK, downstream of RAC1/CDC42): converts merlin open→closed → abolishes Hippo activation → YAP nuclear

**Merlin function beyond Hippo:**
- Inhibits mTORC1 at lysosomes (merlin binds IRTS and blocks mTORC1 assembly → mTOR inhibition in quiescent cells; NF2 LOF → mTORC1 active → protein synthesis)
- Regulates primary ciliogenesis
- Prevents RTK (ErbB2, PDGFR) internalization → modulates growth factor sensitivity

## Function

### Vestibular schwannoma (VS) — the defining NF2 tumor

**Vestibular schwannoma biology:**
- Schwann cells of the vestibular division of cranial nerve VIII (CN VIII); CNVIII has two vestibular branches (superior and inferior) and one cochlear branch → VS arises from the vestibular branches, compresses the cochlear portion → hearing loss
- NF2 LOH in Schwann cells: germline NF2 allele (first hit) + somatic LOH at 22q12 (second hit) in each individual tumor focus → NF2−/− Schwann cells → nuclear YAP1/TAZ → VEGF, CTGF → highly vascular tumor with edema
- Bilateral VS: each VS arises from an independent somatic LOH event in a separate Schwann cell; presence of bilateral VS (and not just unilateral) defines NF2 disease

**Clinical presentation:**
- Progressive unilateral SNHL: the usual initial symptom; often subtle, asymmetric; audiogram shows high-frequency SNHL initially; tinnitus may precede hearing loss
- Bilateral SNHL progressing to deafness: the life-defining morbidity of NF2
- Tinnitus: high-pitched, unilateral initially; can become bilateral
- Vertigo/balance problems: especially with larger tumors
- Facial nerve palsy: CN VII runs adjacent to CN VIII in the internal auditory canal → facial numbness, palsy with large or surgical/radiosurgical manipulation of tumor
- Brainstem compression: very large VS → obstructive hydrocephalus → urgent surgical intervention

**VS imaging:**
- MRI with gadolinium: gold standard; enhancing mass in the internal auditory canal ± cerebellopontine angle; the fundus of the IAC involvement is NF2-characteristic (vs sporadic VS which may be more CPA-dominant)
- Annual MRI surveillance from diagnosis (or as often as every 6 months in young patients with rapidly growing tumors)
- Tumor volume doubling time: key metric for management decisions; fast-growing (>20%/year volume increase) → early intervention

### Meningioma in NF2

- NF2 germline carriers have ~50-80% lifetime risk of meningioma; often multiple; any site (convexity, skull base, spinal)
- NF2 somatic LOF is the most common alteration in sporadic meningioma (~55% of cases) — sporadic meningioma is not a hereditary syndrome but shares the NF2 molecular driver
- NF2-associated meningiomas: may be WHO grade 1 (benign), grade 2 (atypical), or grade 3 (anaplastic); grade 2/3 NF2-associated meningioma → worse prognosis; management: observation (grade 1, asymptomatic) vs surgery ± RT (symptomatic/progressive)
- RT concern in NF2: ionizing radiation can induce new schwannomas and meningiomas within the radiation field; external beam RT avoided when possible, especially in young patients; SRS (radiosurgery) used cautiously for smaller tumors where surgery is high-risk

### Spinal disease

- Spinal schwannomas: ~43% of NF2 patients; arise from dorsal root ganglia; may be multiple (string of pearls appearance on spine MRI); most are asymptomatic; large ones → myelopathy, radiculopathy
- Spinal ependymomas: ~3-10% of NF2; typically WHO grade 2 (myxopapillary in conus, classic cellular in cervical cord); often slow-growing; asymptomatic until large; surgery if symptomatic or progressive
- Annual full spine MRI recommended for NF2 patients

### Ocular manifestations

- Posterior subcapsular cataracts: ~80% of NF2 patients by age 30; often juvenile-onset; may be the earliest detectable NF2 feature in young at-risk children; distinct from age-related nuclear cataracts
- Epiretinal membrane (ERM): surface wrinkling retinopathy; may cause visual distortion
- Retinal hamartomas: combined pigment epithelial/retinal hamartomas; rare; pathognomonic for NF2

## Pathology

### Management of NF2-associated vestibular schwannoma

**Observation:**
- Small VS (<2.5 cm) that are not rapidly growing in patients with useful hearing → active surveillance with MRI every 6-12 months and serial audiometry
- When to intervene: tumor growth (>20% volume/year), hearing decline (>10 dB pure tone average or >10% speech discrimination), new symptoms (vertigo, facial nerve dysfunction), or brainstem compression

**Surgery:**
- Approaches: retrosigmoid (hearing preservation possible for small VS), translabyrinthine (complete tumor removal; hearing sacrifice), middle cranial fossa (hearing preservation for intracanalicular VS)
- NF2 bilateral VS: surgery typically offered on the "better hearing" ear only after the other ear has lost useful hearing (or simultaneously staged); goal is to preserve any residual hearing
- Facial nerve monitoring: intraoperative EMG of facial nerve (CN VII) throughout surgery; nerve preservation priority even if tumor residual
- Auditory brainstem implant (ABI) or cochlear implant: after bilateral deafness; ABI placed at tumor resection (cochlear nerve intact) or at pontomedullary junction (CN VIII damaged); provides environmental sound awareness; speech understanding limited with ABI

**Bevacizumab (anti-VEGF):**
- Plotkin 2009 NEJM: 57% of NF2 patients with growing VS had hearing improvement (>10 dB gain in 4-frequency PTA), 55% had ≥20% tumor volume reduction; treatment duration 6-24 months; FDA Breakthrough Therapy Designation for VS
- Mechanism: VS stromal cells secrete VEGF (YAP1-driven CTGF/VEGF) → tumor edema and vascularity → bevacizumab reduces tumor edema → improved hearing (cochlear nerve decompression effect)
- Clinical use: symptomatic/enlarging VS in patients who are poor surgical candidates; hearing-preservation alternative to surgery
- Limitations: not curative; tumors often regrow after discontinuation; bevacizumab toxicity (hypertension, proteinuria, thrombosis, wound healing impairment)

**Radiosurgery (Gamma Knife, CyberKnife):**
- Used cautiously in NF2: good local tumor control for VS; concern for post-SRS malignant transformation (rare but reported), radiation-induced meningiomas/schwannomas in radiation field, CN VII and CN VIII dose-related dysfunction
- Preferred in elderly patients with poor surgical candidacy, or contralateral tumor after surgical deafness on one side

**Emerging therapies:**
- **TEAD inhibitors** (K-975, IK-930, VT3989): NF2 LOF → nuclear YAP1/TAZ → TEAD → proliferation; TEAD inhibition should suppress VS/meningioma growth; clinical trials ongoing
- **mTOR inhibitors** (everolimus): rationale = NF2 LOF → mTORC1 active; small clinical trials suggest minor VS volume stabilization; not FDA approved for NF2
- **Lapatinib + bevacizumab**: ErbB pathway active in NF2-LOF Schwann cells (merlin normally suppresses ErbB internalization); clinical studies ongoing

**Genetic counseling:**
- 50% offspring risk (NF2 autosomal dominant)
- Prenatal testing: available for known familial mutation
- Testing of children: recommended at diagnosis/birth for first-degree relatives of NF2; annual ophthalmology (cataracts) and audiology in at-risk children from birth

## Connections

- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — Germline NF2 LOF causes NF2 disease; merlin (NF2) is a FERM domain protein that activates the Hippo pathway (MST1/2 → LATS1/2 → YAP phosphorylation); NF2 LOF → nuclear YAP → schwannoma/meningioma; somatic NF2 in mesothelioma, rare ccRCC, astrocytoma.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — YAP1 is the principal Hippo pathway effector released by NF2 LOF; nuclear YAP1-TEAD drives CTGF, CYR61, survivin target genes → schwannoma and meningioma proliferation; TEAD inhibitors (K-975, IK-930, VT3989) in clinical trials for NF2-deficient tumors.
- `connects-to` → **[Meningioma](../../07-system/meningioma/README.md)** — Meningioma is the most common NF2 disease tumor; NF2 germline → bilateral and multiple meningiomas (and cranial nerve schwannomas); NF2 somatic LOF is the most common alteration in sporadic meningioma (~55%); RT avoided when possible in NF2 disease to prevent new tumor induction.
- `connects-to` → **[Mesothelioma](../../07-system/mesothelioma/README.md)** — NF2 somatic LOF in ~50% of mesothelioma → nuclear YAP1 → TEAD-driven survival; NF2 germline carriers have elevated mesothelioma risk (beyond asbestos exposure); TEAD inhibitors (K-975, VT3989) in clinical trials for NF2-deficient mesothelioma; merlin IHC loss in diagnosis.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VS stromal cells secrete VEGF (driven by nuclear YAP1), producing edema and vascularity that compress the cochlear nerve; bevacizumab (anti-VEGF) shrinks ~55% of growing vestibular schwannomas and improves hearing in ~57% — a non-surgical option for failing hearing.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — Schwannomatosis is the key NF2 mimic: both cause multiple schwannomas, but bilateral vestibular schwannomas are pathognomonic for NF2 and absent in schwannomatosis (SMARCB1/LZTR1, chronic-pain-predominant); a gene panel and dedicated internal-auditory-canal MRI separate them.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — NF2 schwannomas arise from the Schwann-cell sheath of cranial and peripheral nerves — bilateral on the vestibular nerve (CN VIII), plus spinal nerve-root schwannomas in ~43% (string-of-pearls on MRI); each tumor needs an independent somatic second hit at the NF2 locus.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — NF2 and NF1 share a name but are unrelated diseases: NF2 (merlin, a Hippo regulator) causes bilateral vestibular schwannomas and meningiomas, while NF1 (neurofibromin, a RAS-GAP) causes café-au-lait spots and neurofibromas — different genes, tumors, and pathways.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — NF2 is fundamentally a brain-and-nerve tumor syndrome: bilateral vestibular schwannomas on cranial nerve VIII cause progressive deafness, balance loss, and brainstem compression, alongside multiple meningiomas and ependymomas — tumor burden, not malignancy, drives the morbidity.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — The NF2/merlin-Hippo axis extends beyond nerve tumors: somatic NF2 loss occurs in a subset of renal cell carcinomas (as in mesothelioma), where merlin loss frees YAP/TEAD to drive proliferation — placing TEAD inhibitors under study for NF2-deficient kidney cancer too.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — NF2 and tuberous sclerosis are both autosomal-dominant neurocutaneous tumor syndromes, but of different pathways: NF2's Merlin loss drives schwannomas, meningiomas, and ependymomas via Hippo, while TSC's mTOR activation drives hamartomas across brain, kidney, and skin.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — NF2/Merlin and uveal melanoma converge on the Hippo pathway: Merlin normally restrains YAP, and uveal melanoma's GNAQ/GNA11 mutations activate YAP through Hippo—so both tumor biologies illustrate how unleashed YAP drives growth, here in the eye.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — NF2 produces glial as well as Schwann-cell tumors: spinal ependymomas and gliomas of astrocytic/ependymal lineage arise when Merlin loss disinhibits proliferation, part of the schwannoma-meningioma-ependymoma triad that defines the syndrome.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — NF2 and glioblastoma intersect through merlin: NF2 patients develop gliomas from biallelic NF2/merlin loss, and merlin is also inactivated in some sporadic glioblastomas—linking an inherited schwannoma/meningioma syndrome to malignant glioma.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — NF2 and von Hippel-Lindau are both dominant tumor-suppressor syndromes: NF2 (merlin loss) gives bilateral vestibular schwannomas and meningiomas, VHL gives hemangioblastomas and renal cancer—each one gene seeding a distinct tumor constellation.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye carries diagnostic clues to NF2: posterior subcapsular cataracts and retinal hamartomas are characteristic, often appearing before the bilateral vestibular schwannomas that define NF2—so an early cataract in a young person can prompt NF2 evaluation.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — NF2 is defined by tumors on the hearing nerve: bilateral vestibular schwannomas grow on cranial nerve VIII, compressing the neurons that carry sound and balance, so progressive deafness and imbalance in a young person are the hallmark of neurofibromatosis type 2.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiation is used cautiously in NF2: stereotactic radiosurgery can control vestibular schwannomas, but in NF2's tumor-prone, merlin-deficient tissue it risks inducing new tumors or malignant transformation—so timing and dose are weighed carefully against surgery.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Merlin loss in NF2 deranges growth signaling including mTOR: NF2's merlin normally restrains the Hippo pathway and mTOR-linked proliferation, so its loss drives schwannoma growth—making mTOR and VEGF (bevacizumab) inhibition rational targeted approaches.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — NF2 is defined by tumors throughout the nervous system: bilateral vestibular schwannomas on the hearing/balance nerves cause progressive deafness, alongside meningiomas and ependymomas—so merlin loss makes the nervous system the syndrome's near-exclusive target.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — NF2 has subtler skin findings than NF1: instead of café-au-lait spots and plentiful neurofibromas, patients develop a smaller number of cutaneous schwannomas and plaques, so the skin gives quieter but real clues to the diagnosis.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Radiation, including proton and stereotactic radiosurgery, treats NF2 schwannomas: focused radiation can control vestibular schwannomas near the brainstem without open surgery, though in NF2's multiple, recurring tumors it is weighed against the risk of further tumors.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — NF2 tumors grow when merlin stops restraining ERK: loss of the NF2 protein merlin unleashes Ras-ERK signaling that drives schwannoma and meningioma proliferation, motivating trials of MEK-pathway inhibitors in these tumors.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Merlin loss in NF2 drives cyclin D1: with the Hippo brake gone, cyclin D1 pushes cells through the cell cycle, explaining the relentless growth of the multiple schwannomas and meningiomas that define the syndrome.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — NF2 schwannomas depend on their blood supply: the tumors are richly vascular, and anti-VEGF bevacizumab—acting on endothelial cells—can shrink vestibular schwannomas and even recover some hearing, a rare medical therapy for these tumors.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — NF2 tumors turn dangerous when they also lose CDKN2A: while merlin loss alone makes benign schwannomas and meningiomas, added CDKN2A deletion drives the leap to malignant, fast-growing tumors—a key prognostic event.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — NF2 schwannomas are packed with macrophages: tumor-associated macrophages dominate these nerve-sheath tumors and correlate with their growth and the hearing loss they cause, making the immune niche a target to slow vestibular schwannomas.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NF2 tumors are studied as targets for NK and immune therapy: because repeated surgery and radiation risk nerve damage and hearing loss, immune approaches engaging natural killer cells are explored to control the schwannomas non-destructively.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — NF2's merlin loss unleashes growth via AKT-mTOR: without merlin's restraint, signaling flows into the PI3K-AKT-mTOR pathway alongside Hippo-YAP, driving the schwannomas and meningiomas—so mTOR-pathway drugs are studied to slow them.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — NF2 schwannomas grow on PDGF among other factors: autocrine growth-factor loops including PDGF feed the tumors, so PDGF-receptor and other kinase inhibitors are explored alongside the anti-VEGF drugs that can shrink vestibular schwannomas.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — NF2 tumors are studied as targets for cytotoxic T cells: because surgery and radiation risk hearing and nerve damage, engineered T-cell and other immunotherapies aim to control the schwannomas without destroying the nerves they sit on.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — NF2 destroys the ear's potassium-driven hearing: bilateral vestibular schwannomas crush the nerve carrying signals from cochlear hair cells, whose sound transduction runs on a potassium current—so hearing fades on both sides.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — NF2 cuts the synapses that relay sound and balance: as the schwannomas compress the vestibulocochlear nerve, the synaptic transmission from the inner ear to the brain fails, causing the deafness and unsteadiness.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — NF2's meningiomas are built with fibroblast-like cells: alongside the schwannomas, patients grow meningiomas whose fibrous, collagen-laying cells form firm masses that compress the brain and cord.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy fingerprints NF2's schwannomas: their cells wrap in continuous basal lamina and pile up long-spacing collagen as Luse bodies — ultrastructure that distinguishes a nerve-sheath tumor when histology alone is uncertain.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium betrays NF2's meningiomas: these slow-growing tumors deposit calcium in laminated psammoma bodies, giving the gritty calcification seen on CT that, scattered through the skull and spine, hints at multiple meningiomas.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations mark the dangerous ones: when an NF2-associated meningioma reactivates telomerase, it signals a more aggressive, recurrence-prone tumor — a molecular flag that pushes toward closer surveillance and earlier treatment.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — NF2's schwannomas come from the nerve's myelinators: the Schwann cell is the peripheral counterpart of the CNS oligodendrocyte, and loss of merlin lets these insulating cells pile up around the vestibular nerve into the hallmark bilateral tumors.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Schwannomas weave a telltale stroma: their loose Antoni B regions are rich in collagen and microcysts, while the compact Antoni A zones form palisading Verocay bodies — the matrix architecture pathologists read to call the tumor.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The NF2 gene is a frequent casualty in the chest: it is among the most commonly inactivated genes in pleural mesothelioma, the cancer of the membrane wrapping the lung, linking this tumor-suppressor to malignancy far beyond the nervous system.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody can save hearing in NF2: bevacizumab, a monoclonal against VEGF, shrinks vestibular schwannomas and recovers some hearing, while diffuse S100 and SOX10 stains confirm a schwannoma's Schwann-cell origin on biopsy.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — NF2 marks the skin in its own way: rather than NF1's café-au-lait neurofibromas, most patients carry cutaneous and subcutaneous schwannomas — raised plaques and nodules whose discovery in a young person can be the first prompt to look for the brain tumors.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy and inheritance both bear on NF2: vestibular schwannomas can accelerate during pregnancy, and as a dominant disorder each child of an affected parent faces a 50% risk, making genetic counseling central to family planning.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Bevacizumab is the main systemic NF2 drug: this anti-VEGF antibody can shrink vestibular schwannomas and preserve hearing, but by impairing the vessel lining it raises bleeding, clotting and platelet-related complications that must be watched.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — NF2's tumors are immunologically quiet: schwannomas and meningiomas recruit regulatory T cells and few effectors, a cold microenvironment that has limited immunotherapy and is studied to make these slow tumors more visible to attack.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its anti-VEGF therapy carries a vascular price: prolonged bevacizumab raises the risk of hypertension and arterial thromboembolic events including stroke, a trade-off weighed against the hearing it can save in NF2.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Merlin's day job is restraining receptors: the NF2 protein holds EGFR and other growth-factor receptors in check at the cell membrane and enforces contact inhibition, so losing it lets EGFR-driven signaling run on and feed the schwannomas and meningiomas.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Its brain tumors can spark seizures: the meningiomas and ependymomas that stud the nervous system in NF2 irritate the cortex, so epilepsy is among the ways the disease declares itself beyond the hallmark hearing loss.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — The tumors recruit inflammatory help: like the nerve-sheath tumors of NF1, NF2 schwannomas harbor infiltrating mast cells whose mediators are thought to support the tumor microenvironment and its slow, relentless growth.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — It anchors the schwannoma-predisposition spectrum: SMARCB1 (with LZTR1) causes schwannomatosis that overlaps NF2 clinically, so molecular testing distinguishes NF2 from these related multiple-schwannoma syndromes.
- `connects-to` → **[LZTR1](../../03-molecular/lztr1/README.md)** — LZTR1 marks the NF2 mimic: germline LZTR1 mutations cause a schwannomatosis that produces multiple schwannomas without the vestibular tumors of true NF2, a key genetic distinction in the differential.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Schwannomas on the nerves bring chronic pain: spinal and peripheral schwannomas in NF2 compress and irritate nerve roots, making neuropathic pain a major symptom alongside the hearing loss.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Merlin normally restrains NF-κB: its loss in NF2 lifts that brake, engaging NF-κB-driven survival and inflammatory signaling that supports the schwannomas and meningiomas of the syndrome.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Merlin loss activates STAT3: NF2-deficient schwannoma and meningioma cells show STAT3 signaling that backs their growth, one of the pathways downstream of the lost tumor suppressor.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Repeated CNS surgery carries infectious risk: NF2 patients undergo many operations for vestibular schwannomas and meningiomas over a lifetime, and these craniotomies can be complicated by meningitis and sepsis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Progressive deafness and tumor burden weigh on mood: NF2 typically takes hearing and balance in young adulthood while demanding repeated surgery, a combination that drives substantial depression and reduced quality of life.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Its neurosurgery and bevacizumab raise clot risk: long craniotomies with post-operative immobility, plus the anti-VEGF bevacizumab used to shrink vestibular schwannomas, together predispose NF2 patients to venous thromboembolism.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Anti-VEGF therapy drives up blood pressure: bevacizumab, used to control growing NF2 schwannomas and preserve hearing, blocks VEGF signaling in the vasculature and commonly produces new or worsened hypertension.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The same anti-VEGF drug spills protein into the urine: bevacizumab used long-term for NF2 schwannomas injures the glomerular filtration barrier, causing proteinuria and a gradual decline in kidney function.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Repeated neurosurgery and bevacizumab heal slowly: the many craniotomies NF2 demands, compounded by anti-VEGF therapy that impairs angiogenesis, leave surgical wounds prone to dehiscence and delayed closure.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Progressive deafness and endless tumours breed worry: the inexorable bilateral hearing loss, balance failure and lifelong brain-and-spine tumour surveillance of NF2 foster chronic health anxiety.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Losing balance topples the body: the bilateral vestibular schwannomas of NF2 destroy balance as well as hearing, and spinal tumours add weakness, together causing falls and fractures.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its anti-VEGF drug strains the vessels: the bevacizumab used to shrink NF2 schwannomas and preserve hearing causes hypertension and a recognised risk of arterial thromboembolic events.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The same drug can perforate the gut: bevacizumab therapy for NF2, by impairing angiogenesis, carries a risk of gastrointestinal bleeding and bowel perforation.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — High tumours can stop the breath: foramen-magnum and high cervical-cord schwannomas, ependymomas and meningiomas, or a phrenic-nerve schwannoma, can impair the respiratory muscles.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its biology and drug work on growth signals: merlin, the NF2 protein, enforces contact-dependent growth arrest, and the bevacizumab that shrinks vestibular schwannomas blocks tumour angiogenesis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its anti-angiogenic drug unsettles the thyroid: bevacizumab, used to shrink vestibular schwannomas in NF2, can cause hypothyroidism and hypertension as class effects of VEGF blockade.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Systemic therapy supplements surgery: when its schwannomas and meningiomas are too numerous to resect, NF2 is treated with targeted agents such as bevacizumab and trial mTOR and merlin-pathway inhibitors.
- `connects-to` → **[Gorlin Syndrome](../gorlin-syndrome/README.md)** — A fellow CNS-tumour syndrome: like Gorlin syndrome, NF2 is an autosomal-dominant disorder predisposing to nervous-system tumours, here multiple schwannomas, meningiomas and ependymomas.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — They share a schwannoma link: Carney complex causes psammomatous melanotic schwannomas, placing it alongside NF2 and schwannomatosis among the inherited schwannoma-predisposing syndromes.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — A limited role against its tumours: the schwannomas, meningiomas and ependymomas of NF2 are largely chemoresistant, managed by surgery and radiosurgery, with bevacizumab the main systemic option.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunologically quiet tumours: NF2-related schwannomas and meningiomas have low mutational burden and a cold microenvironment, so checkpoint inhibitors play little role.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Its meningiomas remodel bone: NF2 causes multiple meningiomas that provoke reactive hyperostosis of the skull, alongside its hallmark bilateral vestibular schwannomas.
- `connects-to` → **[HCC](../hcc/README.md)** — Merlin loss drives liver cancer through YAP: the NF2 protein merlin restrains the Hippo effector YAP, so NF2 inactivation—somatic in many hepatocellular carcinomas—unleashes YAP-driven proliferation, linking the schwannoma gene to liver cancer.
- `connects-to` → **[Atypical Teratoid Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Overlapping at SMARCB1: NF2-related and schwannomatosis tumours can involve SMARCB1, the SWI/SNF subunit whose biallelic loss defines atypical teratoid/rhabdoid tumours, tying nerve-sheath tumour biology to a malignant childhood CNS cancer.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The Hippo brake on organ size: merlin (NF2) signals cell-contact density to the Hippo pathway that caps proliferation, a mechanism vivid in the hepatic lobule where merlin loss lets hepatocytes overgrow—the tumour-suppressor role behind NF2 cancers.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Bilateral vestibular schwannomas: NF2's hallmark tumours arise from the Schwann cells of cranial nerve VIII, compressing the nerve and its axons to cause the progressive hearing loss and imbalance that define the syndrome.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Dense fibrous tumour stroma: NF2 schwannomas and meningiomas lay down a collagen-rich, fibroblastic matrix—the firm Antoni-A texture of schwannoma—and merlin loss promotes this profibrotic phenotype.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Hippo-YAP and heart regeneration: the merlin-Hippo-YAP pathway that NF2 disrupts is a leading target to coax the adult myocardium to regenerate after infarction, a striking spin-off from a nerve-tumour gene.
- `connects-to` → **[MPNST](../mpnst/README.md)** — The nerve-sheath-tumour family: NF2 produces benign Schwann-cell schwannomas while NF1 produces neurofibromas that can transform into MPNST, the two neurofibromatoses bracketing the spectrum of peripheral-nerve-sheath tumours.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — A disease of Schwann cells: NF2 tumours arise from the Schwann cells that ensheath peripheral nerves down to the neuromuscular junction, merlin loss driving their relentless proliferation along the nerve.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Meningioma-predisposing syndromes: NF2 is the leading germline cause of multiple meningiomas, while Li-Fraumeni patients develop them after radiotherapy—two inherited routes to the same intracranial tumour.

[^asthagiri-2009-nf2-lancet]: Asthagiri AR, Parry DM, Butman JA, et al. Neurofibromatosis type 2. *Lancet.* 2009;373(9679):1974-1986. [doi:10.1016/S0140-6736(09)60259-2](https://doi.org/10.1016/S0140-6736(09)60259-2) · [PubMed 19476995](https://pubmed.ncbi.nlm.nih.gov/19476995/)
[^plotkin-2009-nf2-bevacizumab]: Plotkin SR, Stemmer-Rachamimov AO, Barker FG 2nd, et al. Hearing improvement after bevacizumab in patients with neurofibromatosis type 2. *N Engl J Med.* 2009;361(4):358-367. [doi:10.1056/NEJMoa0902579](https://doi.org/10.1056/NEJMoa0902579) · [PubMed 19587327](https://pubmed.ncbi.nlm.nih.gov/19587327/)
