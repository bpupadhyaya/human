---
schema: human-scale-entry/v1
id: schwannomatosis
name: Schwannomatosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Schwannomatosis is caused by germline SMARCB1 (~40%) or LZTR1 (~30%) mutations; multiple peripheral schwannomas WITHOUT bilateral vestibular schwannomas; chronic pain is the hallmark; distinct from NF2; treatment: surgical resection for symptomatic tumors."
aliases: ["schwannomatosis", "multiple schwannomatosis", "SMARCB1 schwannomatosis", "LZTR1 schwannomatosis", "schwannomatosis type 1", "schwannomatosis type 2", "sporadic schwannomatosis", "schwannomatosis NF2-negative", "hereditary schwannomatosis"]
sources:
  - id: merker-2012-schwannomatosis
    type: peer-reviewed
    cite: "Merker VL, Esparza S, Smith MJ, Stemmer-Rachamimov A, Plotkin SR. Clinical features of schwannomatosis: a retrospective analysis of 87 patients. Oncologist. 2012;17(10):1317-1322."
    doi: "10.1634/theoncologist.2012-0162"
    pmid: "22927469"
    url: "https://doi.org/10.1634/theoncologist.2012-0162"
  - id: piotrowski-2014-lztr1
    type: peer-reviewed
    cite: "Piotrowski A, Xie J, Liu YF, et al. Germline loss-of-function mutations in LZTR1 predispose to an inherited disorder of multiple schwannomas. Nat Genet. 2014;46(2):182-187."
    doi: "10.1038/ng.2855"
    pmid: "24362817"
    url: "https://doi.org/10.1038/ng.2855"
cross_links:
  - target: 01-human/03-molecular/lztr1
    relation: connects-to
    note: "Germline biallelic LZTR1 LOF (or dominant negative missense) causes LZTR1-schwannomatosis; LZTR1 somatic second hit in each schwannoma; Schwann cells with loss of both LZTR1 alleles → RAS-MAPK → schwannoma; presents as chronic pain and multiple peripheral nerve tumors."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SMARCB1 (INI1) germline monoallelic LOF with somatic NF2 LOH as second hit → SMARCB1-schwannomatosis; SMARCB1 acts via Cullin3-RING ligase E3 pathway to regulate SWI/SNF complex; distinct from biallelic SMARCB1 LOF in AT/RT; no increased rhabdoid tumor risk in schwannomatosis."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "NF2 and schwannomatosis both cause multiple schwannomas; NF2 = bilateral VS (pathognomonic) + meningiomas; schwannomatosis = no bilateral VS, peripheral schwannomas, chronic pain; gene panel (NF2/SMARCB1/LZTR1) required for diagnosis; audiogram helps distinguish."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "SMARCB1 biallelic somatic LOF causes AT/RT; germline monoallelic SMARCB1 + somatic NF2 LOH second hit → schwannomatosis (NOT AT/RT); AT/RT risk is not elevated in schwannomatosis carriers; SMARCB1 LOF mechanism is distinct between these two tumor types."
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "Somatic NF2 LOH (22q loss) is the typical second hit in SMARCB1-schwannomatosis schwannomas — the 3-hit model: germline SMARCB1 LOF, then somatic NF2 loss yields the tumor; NF2, SMARCB1, and LZTR1 all cluster on chromosome 22q, so 22q loss inactivates them together."
  - target: 01-human/07-system/noonan-syndrome
    relation: connects-to
    note: "LZTR1 is shared: dominant heterozygous LOF causes Noonan syndrome (a RASopathy), while biallelic LOF or dominant-negative missense variants cause LZTR1-schwannomatosis; some D-N carriers show overlapping Noonan features plus schwannomas — same gene, different dose and mechanism."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Schwannomas arise from the Schwann-cell sheath of peripheral and spinal nerves; spinal nerve roots are the most common site in schwannomatosis; chronic neuropathic pain comes from intraneural growth and nerve compression; fascicle-sparing excision preserves nerve function."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "Schwannomatosis and MPNST sit at opposite ends of nerve-sheath biology: schwannomatosis makes multiple benign but painful schwannomas (SMARCB1/LZTR1), while MPNST is the malignant Schwann-cell sarcoma — transformation is rare in schwannomatosis, unlike the ~10% MPNST risk in NF1."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Schwannomatosis is the third neurofibromatosis with NF1 and NF2: all make multiple nerve-sheath tumors, but NF1 (RAS) makes neurofibromas with café-au-lait spots, NF2 (merlin) bilateral vestibular schwannomas, and schwannomatosis (SMARCB1/LZTR1) painful schwannomas without VS."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Schwannomatosis is a disease of the peripheral nervous system: schwannomas stud peripheral and spinal nerve roots, and its hallmark is severe chronic neuropathic pain out of proportion to size from intraneural growth — distinguishing it from NF2 even when both make schwannomas."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Schwannomatosis and meningioma overlap through the NF2/SWI-SNF axis: SMARCB1 and LZTR1 mutations cause schwannomatosis, and SMARCB1-mutant cases can also develop meningiomas, while NF2-related schwannomatosis classically combines schwannomas with meningiomas and ependymomas."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Chronic pain, not hearing loss, is the defining feature of schwannomatosis: unlike NF2, its multiple peripheral-nerve schwannomas cause severe, often disproportionate neuropathic pain as the presenting complaint, making pain management central to care."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Schwannomatosis and synovial sarcoma both disrupt the SWI/SNF chromatin-remodeling complex: SMARCB1 loss drives SMARCB1-related schwannomatosis (and rhabdoid tumors), while synovial sarcoma's SS18-SSX fusion hijacks the same BAF complex—shared epigenetic biology."
  - target: 01-human/07-system/chordoma
    relation: connects-to
    note: "Schwannomatosis and poorly differentiated chordoma share SMARCB1 loss: this SWI/SNF tumor-suppressor, mutated in some schwannomatosis families, is also lost in aggressive SMARCB1-deficient chordomas—linking a benign nerve-tumor syndrome to chromatin-driven cancers."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Schwannomatosis and Li-Fraumeni are both tumor-predisposition syndromes via different mechanisms: schwannomatosis from SMARCB1/LZTR1 (SWI-SNF) loss, Li-Fraumeni from germline TP53 loss—chromatin-remodeling versus genome-guardian failure."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Schwannomatosis tumors enter the sarcoma differential: schwannomas and arising MPNSTs must be distinguished from EWSR1-driven Ewing sarcoma and synovial sarcoma by immunohistochemistry and molecular testing—nerve-sheath versus translocation-driven tumors."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Schwannomatosis grows painful tumors along peripheral nerves: SMARCB1 or LZTR1 loss produces multiple schwannomas on nerve sheaths that compress neurons, so chronic pain—more than the deafness of NF2—is its dominant, defining symptom."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Schwannomatosis spares the vestibular nerves that NF2 attacks: it causes cranial and spinal schwannomas but characteristically NOT bilateral vestibular schwannomas, so the absence of those hearing-nerve tumors distinguishes it from neurofibromatosis type 2."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Schwannomas in schwannomatosis are well-circumscribed nerve-sheath tumors with a fibroblast-like stroma: their spindle (Schwann) cells and collagenous matrix form encapsulated masses distinct from the infiltrating plexiform neurofibromas of NF1."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Schwannomatosis can surface in the skin: peripheral and cutaneous schwannomas form palpable nodules along nerves, and unlike NF2 these patients lack vestibular schwannomas—so painful subcutaneous nerve tumors without hearing loss suggest schwannomatosis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Stereotactic radiosurgery (photon-based) treats select schwannomas: focused radiation can control growing or surgically risky nerve-sheath tumors, though in a tumor-prone syndrome it is balanced against the small risk of inducing further or malignant tumors."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Schwannomatosis dominates the musculoskeletal experience as chronic pain: multiple schwannomas along spinal and peripheral nerves cause severe, often disabling pain rather than the deficits seen in NF2—so pain control is the central management challenge."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Schwannomatosis links to RAS-ERK through LZTR1: the LZTR1 gene normally degrades RAS, so its loss lets RAS-ERK signaling drive Schwann-cell tumor growth—one of the two molecular routes (with SMARCB1) to this multiple-schwannoma syndrome."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Schwannomatosis tumors arise from Schwann cells, the peripheral counterpart of oligodendrocytes: both make myelin, but Schwann cells wrap peripheral nerves—so these tumors form along peripheral nerves rather than in the brain's oligodendrocyte territory."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Schwannoma growth engages PI3K-mTOR signaling: alongside RAS-ERK, loss of the tumor-suppressor inputs activates mTOR to drive proliferation, making the pathway a candidate target in a syndrome whose tumors are otherwise managed surgically."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Schwannomatosis can trace to runaway RAS: LZTR1 normally tags RAS for destruction, so losing it lets RAS-MAPK signaling build up and drive schwannomas—linking the syndrome to the RASopathies like Noonan."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Schwannomatosis tumors grow through the Hippo effector YAP1: like NF2 schwannomas, loss of merlin and SWI/SNF function releases YAP1 to switch on growth genes, the shared pathway behind these nerve-sheath tumors."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Schwannomatosis pain is fueled by macrophages: its schwannomas are infiltrated by macrophages that release inflammatory mediators sensitizing nerves, helping explain why chronic pain—not hearing loss—is this syndrome's hallmark."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha drives the chronic pain of schwannomatosis: tumor and immune cells release this cytokine, which sensitizes nerve fibers, helping explain why disabling pain—not hearing loss—is the syndrome's defining feature."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Schwannomatosis tumors grow on PDGF and related signals: autocrine growth-factor loops feed the multiple schwannomas, so PDGF-receptor and other kinase inhibitors are explored to slow them in this hard-to-treat nerve disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame the schwannomatosis nerve: recruited into the schwannomas, they release histamine and proteases that sensitize nerve endings, adding to the macrophage-driven neuroinflammation behind the syndrome's relentless pain."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Schwannomatosis pain is electrical, carried by sodium: schwannoma-damaged nerves cluster sodium channels that fire spontaneously, generating the relentless, hard-to-treat pain that defines the syndrome."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Schwannomas are built on thick-walled vessels: their endothelial cells form the hyalinized, dilated blood vessels that, with Antoni A and B areas, are a histologic hallmark of the tumors."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Schwannomatosis pain becomes wired into synapses: relentless nerve-tumor input sensitizes spinal dorsal-horn synapses, so central sensitization sustains the pain even beyond what the tumors alone explain."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy confirms the tumors are schwannomas: their cells wrap in continuous basal lamina and stack long-spacing collagen as Luse bodies, the same ultrastructure of nerve-sheath origin found across the schwannoma family."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Substance P carries schwannomatosis's defining misery: the tumors irritate sensory nerves into releasing this pain neuropeptide, driving the chronic, often disabling pain that — more than tumor growth — dominates the disorder."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium currents amplify the pain: tumor-irritated sensory neurons open voltage-gated calcium channels to fire and release their neuropeptides, so calcium-channel blockers are among the drugs tried against schwannomatosis pain."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Schwannomas betray themselves by their weave: the compact Antoni A zones palisade into collagen-walled Verocay bodies while loose, collagen-rich Antoni B areas fill the rest — the matrix architecture pathologists read to call a schwannoma."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Losing the brake on growth wakes a survival pathway: when the tumor-suppressor merlin or its partners fail, PI3K-AKT-mTOR signaling runs unchecked, helping the Schwann cells proliferate into the multiple schwannomas that define the syndrome."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium channels are the nerve's brake on firing: by setting the resting potential and cutting short each spike, channels like Kv7 quiet overactive pain neurons, making potassium-channel openers a target for the relentless pain of schwannomatosis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains read these tumors: a schwannoma stains strongly and diffusely for S100 and SOX10, and the mosaic, patchy loss of SMARCB1 (INI1) staining points to schwannomatosis and away from the NF2-type tumors it mimics."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "The defining feature is pain, and serotonin helps tame it: SNRI antidepressants like duloxetine boost serotonin and noradrenaline in the spinal cord's descending pain pathways, a mainstay against the chronic neuropathic pain that dominates schwannomatosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Schwannomas can stud the gut: the syndrome's nerve-sheath tumors arise along abdominal and pelvic nerves and within the bowel wall, where they can bleed or, growing large, press on and obstruct the intestine."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Losing SMARCB1 hands control to EZH2: the SWI/SNF subunit normally opposes the EZH2-PRC2 complex, so its loss in schwannomatosis tumors leaves them dependent on EZH2 — the vulnerability that EZH2 inhibitors like tazemetostat exploit in SMARCB1-deficient cancers."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Inheritance in schwannomatosis is tricky: SMARCB1 and LZTR1 pass dominantly but with incomplete penetrance and frequent mosaicism, so genetic counseling must explain why a parent may be mildly affected yet a child severely so."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The tumor's immune surroundings draw interest: schwannomas recruit regulatory T cells and macrophages into their microenvironment, and SMARCB1-deficient tumors more broadly are studied for how this immune setting might be turned against them."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "The pain becomes wired into the cord: persistent input from the schwannomas drives glutamate-NMDA central sensitization in the spinal dorsal horn, amplifying signals so the pain outlasts and outstrips the tumors themselves — a target for drugs like gabapentin."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Inflammation around the tumor lights up nociceptors: bradykinin released in the irritated tissue directly excites and sensitizes the pain nerve endings of nearby schwannomas, a peripheral trigger of the disorder's defining chronic pain."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "The tumors recruit their own blood supply: schwannomas express VEGF to drive angiogenesis, and anti-VEGF therapy with bevacizumab — used in related NF2 schwannomas — can shrink them and ease symptoms."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Merlin loss lifts a brake on STAT3: beyond Hippo-YAP, the NF2/SMARCB1-deficient schwannoma cell shows STAT3 activation that supports its survival and growth, a signaling node studied alongside the syndrome's other pathways."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Repeated tumor surgery clots the veins: schwannomatosis often requires multiple operations to remove painful schwannomas, and the immobility and surgery carry a perioperative venous thromboembolism risk."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Surgery carries infectious risk: the repeated spinal and peripheral-nerve operations used to debulk painful schwannomas can be complicated by wound infection and sepsis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Unrelenting pain darkens mood: the defining feature of schwannomatosis is chronic, often severe pain, and living with intractable pain and progressive disease drives a high burden of depression that shapes quality of life."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Treating its pain courts dependence: because chronic pain dominates schwannomatosis and responds poorly to surgery, long-term opioid use is common and carries the attendant risk of tolerance, dependence and opioid use disorder."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Its widespread pain overlaps and confounds: the diffuse, multifocal pain of schwannomatosis can resemble or coexist with fibromyalgia, complicating diagnosis and sharing the central pain-sensitization that resists analgesia."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Relentless pain robs patients of sleep: the chronic, often nocturnal pain that defines schwannomatosis fragments sleep and drives a persistent insomnia that in turn lowers pain tolerance the next day."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Unpredictable pain and tumor uncertainty breed worry: the constant pain, surveillance for new schwannomas and fear of progression in schwannomatosis foster chronic anxiety alongside its better-recognized depression."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Its long-term opioids quietly thin the bones: the chronic opioid therapy needed for schwannomatosis pain suppresses sex hormones, and the resulting hypogonadism, with pain-related inactivity, accelerates loss of bone density."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Repeated tumour surgery means repeated wounds: the surgical resection of painful schwannomas — often multiple over a lifetime in schwannomatosis — leaves wounds that must heal, sometimes near nerves."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its chronic opioids constipate the gut: the long-term opioid analgesia central to schwannomatosis pain control slows intestinal transit, causing opioid-induced constipation that can become severe."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Long-term NSAIDs wear on the kidneys: the chronic non-steroidal anti-inflammatory use that helps control schwannomatosis pain can cause analgesic nephropathy and a slow decline in kidney function."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its tumours can be felt under the skin: schwannomatosis produces cutaneous and subcutaneous schwannomas as palpable, often painful nodules along peripheral nerves."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its chronic opioids suppress the hormones: the long-term opioid therapy that controls schwannomatosis pain causes opioid-induced androgen deficiency with hypogonadism and low libido."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Tumours and opioids both threaten breathing: intrathoracic or vagal schwannomas can compress the airway, and the high-dose opioids used for its pain carry a risk of respiratory depression."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Pelvic tumours can block the urinary tract: retroperitoneal and pelvic schwannomas can compress the ureters and bladder, causing obstruction and urinary symptoms."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chest tumours sit against the great vessels: intrathoracic and paraspinal schwannomas can lie against the great vessels and sympathetic chain, complicating surgery and causing autonomic symptoms."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its tumour-suppressor loss shapes immunity: the SMARCB1 (SWI/SNF) loss it shares with rhabdoid tumours alters chromatin regulation and the tumour's immune microenvironment."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "Pain is its dominant feature: chronic, often severe pain from schwannomas is treated multimodally with NSAIDs like ibuprofen, alongside neuropathic agents and opioids."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "A fellow schwannoma syndrome: Carney complex causes psammomatous melanotic schwannomas, joining schwannomatosis and NF2 among the inherited schwannoma-predisposing disorders."
  - target: 03-medicine/03-food/curcumin
    relation: connects-to
    note: "Anti-inflammatory adjuncts are tried: turmeric-derived curcumin and other anti-inflammatory supplements are used by some for the chronic pain of schwannomatosis, though evidence is limited."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Anti-angiogenics shrink schwannomas: bevacizumab against VEGF can reduce schwannoma volume and stabilise hearing in NF2-spectrum disease, and mTOR and MEK inhibitors are under study for inoperable or progressive tumours."
  - target: 03-medicine/01-modern/12-anti-inflammatory/dexamethasone
    relation: connects-to
    note: "Steroids calm acute flares: corticosteroids like dexamethasone reduce peritumoral oedema and the acute nerve-compression pain of an enlarging schwannoma, and are used perioperatively, though they do not control the underlying tumour."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "A converging mTOR syndrome: like TSC, schwannomatosis is a tumour-suppressor disorder whose pathway feeds into mTOR signalling — merlin loss de-represses mTOR much as hamartin-tuberin loss does — making mTOR inhibition a shared therapeutic theme."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "A shared SMARCB1 lesion: SMARCB1-related schwannomatosis loses the same SWI/SNF subunit inactivated in SMARCB1-deficient renal medullary carcinoma and rhabdoid tumours, linking a benign nerve-tumour syndrome to an aggressive kidney cancer."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Both run through merlin and Hippo: schwannomatosis tumours (NF2/LZTR1) and many mesotheliomas inactivate NF2/merlin, unleashing the Hippo effector YAP—shared loss of a contact-inhibition brake in unrelated tissues."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "Two diseases of the Schwann cell: schwannomatosis grows benign tumours from Schwann cells, while Guillain-Barré is an autoimmune attack on the myelin those cells make—opposite pathologies of one peripheral-nerve cell."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain is the defining feature: unlike NF2, schwannomatosis presents primarily with severe chronic neuropathic pain from peripheral schwannomas, often out of proportion to tumour size—the dominant management problem."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Schwannomas compress nerves: schwannomatosis's multiple peripheral and spinal schwannomas press on nerves and their axons, causing pain, weakness and sensory loss, without the bilateral vestibular tumours of NF2."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "A collagen-rich tumour stroma: schwannomas lay down the dense, fibrous Antoni-A matrix, and the SMARCB1/NF2-merlin loss of schwannomatosis promotes this profibrotic phenotype."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "SWI/SNF chromatin disorders: schwannomatosis (SMARCB1) and ovarian clear-cell carcinoma (ARID1A) both arise from loss of subunits of the SWI/SNF chromatin-remodelling complex, a shared epigenetic route to very different tumours."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "Chronic peripheral nerve disease: schwannomatosis sits in the differential of acquired chronic neuropathies like CIDP, both presenting with progressive peripheral nerve dysfunction though one is tumoural and the other inflammatory."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "A Schwann-cell disease: schwannomatosis tumours arise from the Schwann cells that ensheath peripheral nerves all the way to the neuromuscular junction, SMARCB1/LZTR1 loss driving their multifocal growth."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Pain mediator: COX-derived prostaglandins contribute to the chronic, often severe pain that dominates schwannomatosis, the rationale for NSAIDs in symptom control."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: SMARCB1/LZTR1 loss with CDK4/6-cyclin dysregulation propels the proliferation of the multiple schwannomas characteristic of the syndrome."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Hippo crosstalk: Notch signalling interacts with the NF2-merlin-Hippo-YAP axis to promote schwannoma growth in schwannomatosis."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "G1 progression: cyclin D1, upregulated by SMARCB1/LZTR1 loss, partners CDK4/6 to push schwannoma cells through the G1 checkpoint in schwannomatosis."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative oncogene: MYC activation downstream of the dysregulated Hippo and growth-factor pathways drives the proliferation of schwannomatosis tumours."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the growing schwannomas drives the VEGF angiogenesis that supplies these nerve-sheath tumours."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Nociceptor sensitisation: NGF signalling through TrkA sensitises the sensory nerve fibres entangled by schwannomatosis tumours, contributing to the chronic, often severe pain that dominates this syndrome."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Neurogenic pain: CGRP released from the peri-tumoural sensory nerves mediates the neurogenic inflammation and chronic pain that is the defining clinical feature of schwannomatosis, distinguishing it from NF2."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophages and pain: schwannomatosis tumours recruit CCL2-driven macrophages that both sustain tumour growth and release mediators that sensitise nociceptors, linking the immune infiltrate to the pain phenotype."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Mast-cell infiltrate: like other nerve-sheath tumours, schwannomatosis schwannomas contain KIT-dependent mast cells whose stem-cell-factor signalling contributes to the inflammatory microenvironment that supports tumour growth and nociceptor sensitisation."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Schwannoma niche: CXCL12-CXCR4 signalling supports the growth and survival of the multiple schwannomas of schwannomatosis, anchoring the Schwann tumour cells within their peripheral-nerve microenvironment."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "Merlin-pathway signalling: schwannomatosis tumours frequently carry a second-hit NF2/merlin loss, and because merlin normally restrains Src/FAK at the membrane, Src disinhibition drives the loss of contact inhibition that lets schwannoma cells proliferate."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "ErbB disinhibition: merlin normally holds EGFR/ErbB receptors inactive at cell contacts, so the merlin-pathway loss of schwannomatosis releases EGFR-driven proliferative signalling in Schwann cells."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival axis: downstream of merlin loss, PI3K-AKT-mTOR signalling (AKT and mTOR already mapped) is activated in schwannomas, a proliferative survival pathway and candidate target for these otherwise drug-resistant tumours."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Pain mediator: the chronic neuropathic pain that dominates schwannomatosis involves inflammatory cytokines including IL-6 sensitising sensory neurons, acting alongside the substance-P and CGRP already mapped."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: the cyclin-D1-CDK4/6 axis (both mapped) releases E2F1 to drive the proliferation of the multiple schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K restraint: loss of the SMARCB1/LZTR1-merlin tumour-suppressor network de-represses PI3K-AKT-mTOR signalling (PIK3CA, AKT and mTOR already mapped), which PTEN normally limits, fuelling schwannoma growth."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Schwannoma stroma: TGF-β signalling shapes the collagenous extracellular matrix (collagen mapped) and fibroblastic stroma of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: dysregulation of the RB1-E2F checkpoint (CDK4/6, cyclin-D1 and E2F1 already mapped) contributes to the proliferation of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 survival: JAK-STAT3 signalling (STAT3 already mapped) contributes to the survival signalling of schwannomatosis-associated schwannomas."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neuropathic pain: TLR4-driven neuroinflammation around tumour-infiltrated nerves contributes to the chronic neuropathic pain that is the predominant clinical feature of schwannomatosis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is expressed in schwannomas and contributes to their tumour-microenvironment interactions in schwannomatosis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) modulates the Schwann-cell proliferation and stroma of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, regulated by the merlin/PI3K-AKT axis, modulate the survival of the Schwann-cell tumours of schwannomatosis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated CD8 cytotoxicity contributes to the immune surveillance of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling of the SMARCB1/LZTR1-deficient schwannoma cells of schwannomatosis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation restrains apoptosis in the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory and neuropathic-pain microenvironment of schwannomatosis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the SMARCB1/LZTR1-deficient schwannoma cells of schwannomatosis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A and the SWI/SNF machinery (SMARCB1 already mapped) contribute to the epigenetic dysregulation of schwannomatosis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of schwannomatosis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven neuroinflammation participates in the chronic pain and tumor microenvironment of schwannomatosis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory and pain-associated microenvironment of schwannomatosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of schwannomatosis."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Pain as the defining burden: chronic, often disabling pain out of proportion to tumour size is the hallmark of schwannomatosis, and the mu-opioid receptor mediates the opioid analgesia central to its frequently refractory pain management."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Neuropathic-pain mechanism: the neuropathic pain of schwannomatosis is treated with gabapentinoids that act on the voltage-gated calcium-channel alpha-2-delta subunit, and calcium influx drives the ectopic nociceptor firing from tumour-compressed nerves."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "YAP-driven signaling: SMARCB1- and NF2/merlin-related loss de-represses YAP (already mapped), upregulating the AXL receptor tyrosine kinase that promotes schwannoma growth and offers a targetable node downstream of the core tumour-suppressor defect."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Neurogenic pain: nitric oxide participates in the neuroinflammation and sensitisation of the nerves compressed by schwannomas, contributing to the chronic pain that is the dominant and often disabling symptom of schwannomatosis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Tumour immune microenvironment: MHC class II-mediated antigen presentation shapes the T-cell and macrophage infiltrate of schwannomas, of interest as immunotherapy and anti-inflammatory approaches to their growth and pain are explored."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormone sensitivity: like the related meningiomas and schwannomas of NF2, the tumours of schwannomatosis can express hormone receptors, and estrogen may influence their growth, including reports of enlargement during pregnancy."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Immune infiltrate: cytotoxic CD8 T cells (MHC class II and perforin already mapped) form part of the immune infiltrate of schwannomas, of interest to the immunotherapy approaches explored for these painful nerve-sheath tumours."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune microenvironment: IL-10 in the schwannoma microenvironment shapes its immune and inflammatory milieu (MHC class II already mapped), part of the neuroinflammation that drives the chronic pain characteristic of schwannomatosis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell pain: mast cells releasing histamine in and around schwannomas contribute to the neuroinflammatory environment and the sensitisation (substance P and CGRP already mapped) that produces the dominant chronic pain of schwannomatosis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 mast-cell milieu: IL-4 supports the mast cells (already mapped) and polarises macrophages (already mapped) toward an M2 phenotype (IL-10 already mapped), part of the type-2 neuroinflammatory microenvironment that drives the pain of schwannomatosis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 inflammation: IL-13, with IL-4 (already mapped), reflects the type-2 cytokine arm of the mast-cell-rich (already mapped) neuroinflammatory milieu of the schwannomas, part of the microenvironment behind the chronic pain of schwannomatosis."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative microenvironment: the schwannomas generate oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of the tumour and neuroinflammatory microenvironment of schwannomatosis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Analgesic magnesium: magnesium blocks the NMDA receptor of the glutamate (already mapped) signalling, and it is used as an adjunct for the chronic neuropathic pain (substance P and CGRP already mapped) that dominates schwannomatosis."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton radiotherapy: proton radiosurgery treats the spinal and skull-base schwannomas of schwannomatosis where surgery risks the nerve, sparing the adjacent cord and cranial nerves."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophilic milieu: IL-5, with the mast cells and the type-2 cytokines (IL-4 and IL-13 already mapped), recruits eosinophils to the neuroinflammatory schwannoma microenvironment behind the chronic pain of schwannomatosis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Nerve-adipose adipokine: leptin from the nerve-associated and marrow adipose tissue signals within the metabolic microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is the adipokine of the metabolic microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the neuroinflammatory schwannoma microenvironment of schwannomatosis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the neuroinflammatory microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the schwannoma microenvironment of schwannomatosis."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen (MHC already mapped) within the immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral arm: the plasma cells secrete the antibodies (already mapped) of the humoral response within the immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance within the immune microenvironment of the schwannomas of schwannomatosis."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the schwannomas of schwannomatosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Tumour complement: the complement C3 activation contributes to the inflammatory dimension of the macrophage-rich (already mapped) schwannoma microenvironment of schwannomatosis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the schwannoma stroma of schwannomatosis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Perineural alarmin: TSLP released by the schwannoma's perineurial fibroblasts and macrophages (already mapped) activates mast cells (present in schwannoma stroma) to promote the type-2 microenvironment and the chronic pain that defines schwannomatosis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement brake: C1-esterase inhibitor modulates the classical complement pathway (C3 and C5aR1 already mapped) activated on the macrophage-rich (already mapped) schwannoma stroma of schwannomatosis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Perineural EPO signalling: erythropoietin, via EPOR expressed on Schwann cells and perineural cells, exerts anti-apoptotic and anti-inflammatory effects that modulate the neuropathic pain and nerve dysfunction of schwannomatosis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Schwannoma stroma scaffold: periostin secreted by fibroblastic stroma of schwannomatosis tumours promotes Schwann-cell survival and tumour-cell integrin-αv signalling, amplifying nerve-sheath tumour growth driven by SMARCB1/LZTR1 loss."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement in schwannoma: complement C5a, generated from C3 (already mapped) and acting via C5aR1 (already mapped) on the macrophage-rich schwannomatosis stroma, amplifies the neuroinflammation and chronic neuropathic pain of the disease."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement-evasion scaffold: schwannomatosis tumour cells recruit factor H to shield against complement lysis, exploiting the same C3/C5aR1 complement cascade already mapped and limiting immune clearance of merlin-deficient nerve-sheath tumours."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "SWN melatonin: melatonin via MT1/MT2 receptors on schwannomatosis Schwann cells (already mapped) and macrophages modulates the neuroinflammatory chronic pain of schwannomatosis, counteracting the substance-P (already mapped) and bradykinin (already mapped) pain sensitisation."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "SWN androgen axis: testosterone via androgen receptor on SMARCB1/LZTR1-deficient (already mapped) Schwann cells modulates the NF2 (already mapped) tumour-suppressor pathway and the sex-dimorphic growth of peripheral nerve-sheath tumours in schwannomatosis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "SWN prolactin: prolactin via JAK2 (already mapped) and STAT3 (already mapped) signalling on SMARCB1-deficient schwannoma cells promotes tumour-cell survival, amplifying the proliferative drive from the EGFR (already mapped) and mTOR (already mapped) axes in schwannomatosis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "SWN oxytocin: oxytocin via OXTR on schwannomatosis Schwann cells (already mapped) modulates the neuroinflammatory pain cascade, reducing the substance-P (already mapped) and bradykinin (already mapped)-driven chronic neuropathic pain of schwannomatosis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "SWN vasopressin: vasopressin via V1aR on schwannomatosis macrophages (already mapped) modulates neuroinflammatory bradykinin (already mapped) and substance-P (already mapped)-driven pain sensitisation of peripheral nerve-sheath tumours in schwannomatosis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "SWN selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species in SMARCB1/LZTR1-deficient schwannoma cells, reducing oxidative-stress-driven mTOR (already mapped) and EGFR (already mapped) proliferative signalling in schwannomatosis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SWN iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour surveillance; thyroid deficiency amplifies VEGF (already mapped) and mTOR (already mapped) schwannoma growth and IL-6 (already mapped) cascade of schwannomatosis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "SWN copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped), drives tumour stromal remodelling; copper angiogenesis amplifies VEGF (already mapped); copper deficiency impairs macrophage (already mapped) and T-cytotoxic-cell (already mapped) immunity in SWN."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "SWN zinc: zinc, as metalloproteinase cofactor in macrophages (already mapped) and mast-cell (already mapped), modulates schwannoma invasion; zinc deficiency amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped)-driven cascade of schwannomatosis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "SWN iron: iron, as ribonucleotide reductase cofactor in macrophages (already mapped) and mast-cell (already mapped), supports DNA repair; iron overload amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) tumour cascade of schwannomatosis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "SWN phosphorus: phosphorus, as ATP donor in mTOR (already mapped) signalling in macrophages (already mapped) and mast-cell (already mapped), fuels tumour proliferation; phosphorus dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) cascade of schwannomatosis."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "SWN chloride: chloride channels in macrophages (already mapped) and mast-cell (already mapped) regulate tumour-immune homeostasis; chloride dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "SWN carbon: carbon, as metabolic backbone of mTOR (already mapped) and EGFR (already mapped) in macrophages (already mapped) and mast-cell (already mapped), drives proliferative signalling; carbon dysregulation amplifies IL-6 (already mapped) cascade of schwannomatosis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "SWN hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and mast-cell (already mapped), modulates tumour-immune balance; hydrogen dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "SWN nitrogen: nitrogen, as purine backbone in macrophages (already mapped) and mast-cell (already mapped), fuels nucleotide synthesis; nitrogen dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "SWN oxygen: tumour hypoxia in schwannomatosis drives HIF-1α and VEGF (already mapped) angiogenesis; oxygen depletion amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "SWN sulfur: sulfur, as glutathione in macrophages (already mapped) and mast-cell (already mapped), quenches oxidative stress; sulfur deficiency amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "SWN PD-1: PD-1 checkpoint on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates tumour-immune surveillance; PD-1 dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "SWN glp-1: GLP-1 from macrophages (already mapped) and mast cells (already mapped) modulates schwannoma metabolic-inflammatory tone; glp-1 dysfunction amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "SWN angiotensin-ii: angiotensin-II from macrophages (already mapped) and endothelial cells (already mapped) drives schwannoma angiogenesis; angiotensin-ii excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "SWN wnt-beta-catenin: WNT/β-catenin on Schwann cells (already mapped) and macrophages (already mapped) drives schwannoma growth; wnt-beta-catenin loss amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "SWN rankl: RANKL from macrophages (already mapped) and Schwann cells (already mapped) promotes schwannoma immune evasion; rankl excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "SWN il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates schwannoma immune surveillance; il-2 dysregulation amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "SWN fibronectin: fibronectin in Schwann cells (already mapped) and macrophages (already mapped) promotes schwannoma ECM remodelling; fibronectin excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "SWN igf-1: IGF-1 from Schwann cells (already mapped) and macrophages (already mapped) drives schwannoma growth; igf-1 excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) proliferative cascade of schwannomatosis."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "SWN activin-a: activin-A from Schwann cells (already mapped) and macrophages (already mapped) regulates schwannoma immune-fibrotic balance; activin-a excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "SWN calcitonin: calcitonin from macrophages (already mapped) and Schwann cells (already mapped) modulates calcium balance in schwannomatosis; calcitonin excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "SWN insulin-receptor: insulin receptor on macrophages (already mapped) and Schwann cells (already mapped) drives schwannoma metabolic repair; insulin-receptor loss amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "SWN aldosterone: aldosterone from macrophages (already mapped) and Schwann cells (already mapped) modulates ion balance in schwannomatosis; aldosterone excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "SWN androgen-receptor: androgen receptor on macrophages (already mapped) and Schwann cells (already mapped) modulates schwannoma hormonal tone; androgen excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "SWN norepinephrine: norepinephrine from macrophages (already mapped) and Schwann cells (already mapped) modulates adrenergic tone in schwannomas; norepinephrine excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "SWN adrenomedullin: adrenomedullin from macrophages (already mapped) and Schwann cells (already mapped) modulates vascular tone in schwannomas; adrenomedullin loss amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "SWN bdnf: BDNF from macrophages (already mapped) and Schwann cells (already mapped) drives nerve sheath proliferation; bdnf excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "SWN osteopontin: osteopontin from macrophages (already mapped) and Schwann cells (already mapped) promotes schwannoma invasion; osteopontin excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "SWN fgfr: FGFR on macrophages (already mapped) and Schwann cells (already mapped) drives schwannoma stromal growth; fgfr dysregulation amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "SWN epinephrine: epinephrine from macrophages (already mapped) and Schwann cells (already mapped) modulates schwannoma adrenergic tone; epinephrine excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis."
---

# Schwannomatosis

## Overview

**Schwannomatosis** is a rare hereditary tumor predisposition syndrome characterized by the development of **multiple schwannomas** (benign Schwann cell tumors) arising from peripheral and spinal nerves, **without bilateral vestibular schwannomas** (which would define NF2). Schwannomatosis is clinically defined by **chronic severe pain** as the primary symptom — arising from direct nerve compression or intraneural tumor growth — and by an absence of the pathognomonic NF2 features (bilateral acoustic neuromas, meningiomas). Schwannomatosis is genetically heterogeneous: germline pathogenic variants in **SMARCB1** (schwannomatosis type 1, SWN1; ~40% of familial cases) or **LZTR1** (schwannomatosis type 2, SWN2; ~30% of familial cases) account for ~70% of familial schwannomatosis; ~30% of familial cases remain genetically undefined. Approximately ~70% of schwannomatosis cases are apparently sporadic (no family history); of these, SMARCB1 (~10%) and LZTR1 (~20%) germline variants explain a subset. Schwannomatosis prevalence is estimated at ~1 in 40,000-70,000 [^merker-2012-schwannomatosis] [^piotrowski-2014-lztr1].

**Schwannomatosis vs. NF2 — key distinguishing features:**

| Feature | Schwannomatosis | NF2 |
|---|---|---|
| Bilateral vestibular schwannomas | ABSENT (defines non-NF2) | PRESENT (pathognomonic) |
| Peripheral schwannomas | Multiple; all nerve distributions | Present; less prominent than VS |
| Chronic pain | Hallmark; often debilitating | Less characteristic |
| Meningiomas | Rare (in SMARCB1 cases) | Common (~50-80%) |
| Hearing loss | Not primary | Progressive SNHL → deafness |
| Ependymomas | Not characteristic | ~3-10% |
| Genes | SMARCB1, LZTR1, unknown | NF2 |
| Location of VS | N/A | Bilateral; IAC/CPA |
| Cataracts | Not characteristic | Posterior subcapsular (~80%) |

## Structure

### Genetic basis of schwannomatosis

**SMARCB1 (22q11.23) — Schwannomatosis type 1 (SWN1):**
- 9 exons; 385 aa; INI1 (Integrase Interactor 1) / SNF5 (Sucrose Non-Fermenting 5); core subunit of SWI/SNF chromatin remodeling complex
- Germline pathogenic variants: truncating frameshift/nonsense/splice (most common); missense (rare); mostly monoallelic (heterozygous) in schwannomatosis
- **Two-hit mechanism in schwannomatosis (unusual)**: SMARCB1 germline monoallelic LOF (first hit) + somatic second hit — but the second hit in SMARCB1-schwannomatosis is typically **NF2 LOH (22q loss)**, NOT a second SMARCB1 mutation. This is the "3-hit" model of schwannomatosis: (1) germline SMARCB1 LOF → (2) somatic loss of NF2 → Schwann cell with NF2 LOH + hemizygous SMARCB1 → (3) a third hit (LOH of remaining SMARCB1 allele) in malignant contexts (AT/RT). Schwannoma = steps 1+2; AT/RT = steps 1+2+3.
- SMARCB1 germline monoallelic loss → mild phenotype (schwannomatosis); biallelic SMARCB1 somatic loss → AT/RT (different tumor, requires complete SMARCB1 inactivation); AT/RT risk is NOT elevated in schwannomatosis carriers (the third hit is very rare in Schwann cells)
- **Segmental schwannomatosis**: ~5% of schwannomatosis patients have schwannomas restricted to one body segment (arm, leg); often mosaic for somatic SMARCB1 or LZTR1 first hit rather than true germline

**LZTR1 (22q11.21) — Schwannomatosis type 2 (SWN2):**
- 17 exons; 836 aa; BTB-Kelch domain protein; CUL3 E3 ubiquitin ligase adaptor; ubiquitinates RAS GTPases (KRAS4B, MRAS, RRAS2) → proteasomal degradation → RAS-MAPK suppression
- Germline pathogenic variants: biallelic LOF (homozygous or compound heterozygous) = recessive schwannomatosis; heterozygous dominant negative (D-N) missense variants in BTB/BACK domain = dominant schwannomatosis (D-N mutant poisons CUL3 recruitment)
- Somatic second hit: in each schwannoma from LZTR1-germline patients, a second somatic event (LOH, nonsense, frameshift) inactivates the remaining functional LZTR1 allele → biallelic LZTR1 LOF in tumor → RRAS2 accumulation → schwannoma
- LZTR1 is also a **Noonan syndrome gene** (see molecular entry); dominant LOF → Noonan; biallelic/D-N → schwannomatosis; heterozygous D-N variants may cause both NS features + schwannomas

**Note on chromosome 22q clustering:**
Both NF2 (22q12.2), SMARCB1 (22q11.23), and LZTR1 (22q11.21) are on chromosome 22q → somatic 22q loss is a common second hit in all three: NF2 LOH provides the second hit for SMARCB1-schwannomatosis schwannomas; LZTR1 LOH often accompanies NF2 LOH on the same chromosome arm.

## Function

### Clinical features

**Multiple schwannomas — distribution:**
- Peripheral schwannomas: spinal nerve roots (spinal schwannomas most common in schwannomatosis → intraforaminal or extraforaminal masses; cord compression if large), peripheral nerves (brachial plexus, lumbosacral plexus, sciatic nerve, digital nerves)
- Cranial schwannomas: cranial nerves III, V, VII, IX-XII; unilateral CN VIII schwannoma in ~10% of schwannomatosis (UNILATERAL only, not bilateral)
- Cutaneous schwannomas: subcutaneous masses along nerve courses
- Total number: variable; some patients have <10 schwannomas over a lifetime; others develop 50+

**Chronic pain:**
- The dominant clinical problem; pain is often disproportionate to schwannoma size
- Mechanisms: intraneural tumor compression → neuropathic pain; tumor hypersensitivity of nearby nerve fibers; central sensitization
- Character: burning, constant, severe (often 7-10/10 on VAS); affects quality of life dramatically
- Medical management: pregabalin/gabapentin (neuropathic pain); duloxetine; opioids (for severe refractory pain); ketamine infusions; pain clinic involvement critical
- Surgical pain relief: excision of identified schwannomas → often only partial pain relief because multiple tumors exist

**Spinal schwannomas:**
- Spinal cord compression from large intraforaminal/intraspinal schwannomas → myelopathy, radiculopathy; MRI spine is essential for surveillance
- Cauda equina syndrome possible with large lumbosacral schwannomas
- Surgery: primary treatment for symptomatic/compressive spinal schwannomas; goal is nerve preservation (schwannoma arises from nerve sheath but nerve fascicles often preserved → fascicle-sparing excision)

### Malignant peripheral nerve sheath tumor (MPNST)

- MPNST risk in schwannomatosis: controversy; historically reported as elevated; recent data suggest MPNST risk in schwannomatosis is LOW or similar to population baseline (unlike NF1 where MPNST risk is ~10%)
- Key distinction: plexiform neurofibromas (NF1) → MPNST; schwannomas → malignant change is extremely rare
- If rapid growth, pain escalation, new neurological deficit in a known schwannoma → MRI ± FDG-PET; biopsy if malignancy suspected

## Pathology

### Diagnosis of schwannomatosis

**Diagnostic criteria (2022 revised):**
- **Definite schwannomatosis**: ≥2 non-intradermal schwannomas, at least one histopathologically confirmed, NO ipsilateral CN VIII tumor, NO bilateral VS, NO evidence of NF2 germline mutation
- **Suspected schwannomatosis**: ≥2 non-intradermal schwannomas with compatible MRI, no bilateral VS
- **Genetic (molecularly confirmed) schwannomatosis**: meeting above + germline SMARCB1 or LZTR1 pathogenic variant confirmed

**Testing strategy:**
1. MRI brain (with gadolinium): exclude bilateral VS (NF2); detect any unilateral VS (suspicious but not diagnostic for NF2; unilateral VS can occur in schwannomatosis)
2. MRI spine (with gadolinium): spinal schwannomas (most common schwannomatosis location)
3. Audiologic testing: if any VS identified → bilateral hearing evaluation
4. Genetic testing: SMARCB1 sequencing + MLPA; LZTR1 sequencing + MLPA; NF2 sequencing (to exclude NF2)
5. Pathological confirmation: at least one schwannoma from biopsied tumor (histology: Antoni A + Antoni B areas, Verocay bodies, S100+ cells)

**Surveillance:**
- MRI brain + spine: every 2-3 years (all patients); more frequently in symptomatic patients or known growing lesions
- No specific biomarker surveillance (no serum markers established)
- Pain management: referral to specialized pain medicine

**Surgical management:**
- Symptomatic schwannomas (pain, neurological deficit): surgical excision; microsurgical nerve-sparing technique; incomplete excision → recurrence risk ~10% in schwannomatosis vs ~5% in sporadic schwannoma
- Asymptomatic schwannomas: observation; no prophylactic excision
- Gamma Knife / radiosurgery: not typically used for peripheral schwannomas (no established efficacy data for pain relief; RT-associated risk of malignant transformation in multiply irradiated field)

**Family screening:**
- Autosomal dominant for SMARCB1 or LZTR1 dominant schwannomatosis: 50% offspring risk; genetic testing of first-degree relatives
- Recessive LZTR1: siblings of proband have 25% risk (compound het)
- Cascade testing: clinical + genetic screening from age 20

## Connections

- `connects-to` → **[LZTR1](../../03-molecular/lztr1/README.md)** — Germline biallelic LZTR1 LOF (or dominant negative missense) causes LZTR1-schwannomatosis; LZTR1 somatic second hit in each schwannoma; Schwann cells with loss of both LZTR1 alleles → RAS-MAPK → schwannoma; presents as chronic pain and multiple peripheral nerve tumors.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SMARCB1 (INI1) germline monoallelic LOF with somatic NF2 LOH as second hit → SMARCB1-schwannomatosis; SMARCB1 acts via Cullin3-RING ligase E3 pathway to regulate SWI/SNF complex; distinct from biallelic SMARCB1 LOF in AT/RT; no increased rhabdoid tumor risk in schwannomatosis.
- `connects-to` → **[Neurofibromatosis Type 2](../../07-system/neurofibromatosis-type-2/README.md)** — NF2 and schwannomatosis both cause multiple schwannomas; NF2 = bilateral VS (pathognomonic) + meningiomas; schwannomatosis = no bilateral VS, peripheral schwannomas, chronic pain; gene panel (NF2/SMARCB1/LZTR1) required for diagnosis; audiogram helps distinguish.
- `connects-to` → **[Atypical Teratoid Rhabdoid Tumor](../../07-system/atypical-teratoid-rhabdoid-tumor/README.md)** — SMARCB1 biallelic somatic LOF causes AT/RT; germline monoallelic SMARCB1 + somatic NF2 LOH second hit → schwannomatosis (NOT AT/RT); AT/RT risk is not elevated in schwannomatosis carriers; SMARCB1 LOF mechanism is distinct between these two tumor types.
- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — Somatic NF2 LOH (22q loss) is the typical second hit in SMARCB1-schwannomatosis schwannomas — the 3-hit model: germline SMARCB1 LOF, then somatic NF2 loss yields the tumor; NF2, SMARCB1, and LZTR1 all cluster on chromosome 22q, so 22q loss inactivates them together.
- `connects-to` → **[Noonan Syndrome](../noonan-syndrome/README.md)** — LZTR1 is shared: dominant heterozygous LOF causes Noonan syndrome (a RASopathy), while biallelic LOF or dominant-negative missense variants cause LZTR1-schwannomatosis; some D-N carriers show overlapping Noonan features plus schwannomas — same gene, different dose and mechanism.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Schwannomas arise from the Schwann-cell sheath of peripheral and spinal nerves; spinal nerve roots are the most common site in schwannomatosis; chronic neuropathic pain comes from intraneural growth and nerve compression; fascicle-sparing excision preserves nerve function.
- `connects-to` → **[MPNST](../mpnst/README.md)** — Schwannomatosis and MPNST sit at opposite ends of nerve-sheath biology: schwannomatosis makes multiple benign but painful schwannomas (SMARCB1/LZTR1), while MPNST is the malignant Schwann-cell sarcoma — transformation is rare in schwannomatosis, unlike the ~10% MPNST risk in NF1.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Schwannomatosis is the third neurofibromatosis with NF1 and NF2: all make multiple nerve-sheath tumors, but NF1 (RAS) makes neurofibromas with café-au-lait spots, NF2 (merlin) bilateral vestibular schwannomas, and schwannomatosis (SMARCB1/LZTR1) painful schwannomas without VS.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Schwannomatosis is a disease of the peripheral nervous system: schwannomas stud peripheral and spinal nerve roots, and its hallmark is severe chronic neuropathic pain out of proportion to size from intraneural growth — distinguishing it from NF2 even when both make schwannomas.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Schwannomatosis and meningioma overlap through the NF2/SWI-SNF axis: SMARCB1 and LZTR1 mutations cause schwannomatosis, and SMARCB1-mutant cases can also develop meningiomas, while NF2-related schwannomatosis classically combines schwannomas with meningiomas and ependymomas.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Chronic pain, not hearing loss, is the defining feature of schwannomatosis: unlike NF2, its multiple peripheral-nerve schwannomas cause severe, often disproportionate neuropathic pain as the presenting complaint, making pain management central to care.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Schwannomatosis and synovial sarcoma both disrupt the SWI/SNF chromatin-remodeling complex: SMARCB1 loss drives SMARCB1-related schwannomatosis (and rhabdoid tumors), while synovial sarcoma's SS18-SSX fusion hijacks the same BAF complex—shared epigenetic biology.
- `connects-to` → **[Chordoma](../chordoma/README.md)** — Schwannomatosis and poorly differentiated chordoma share SMARCB1 loss: this SWI/SNF tumor-suppressor, mutated in some schwannomatosis families, is also lost in aggressive SMARCB1-deficient chordomas—linking a benign nerve-tumor syndrome to chromatin-driven cancers.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Schwannomatosis and Li-Fraumeni are both tumor-predisposition syndromes via different mechanisms: schwannomatosis from SMARCB1/LZTR1 (SWI-SNF) loss, Li-Fraumeni from germline TP53 loss—chromatin-remodeling versus genome-guardian failure.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Schwannomatosis tumors enter the sarcoma differential: schwannomas and arising MPNSTs must be distinguished from EWSR1-driven Ewing sarcoma and synovial sarcoma by immunohistochemistry and molecular testing—nerve-sheath versus translocation-driven tumors.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Schwannomatosis grows painful tumors along peripheral nerves: SMARCB1 or LZTR1 loss produces multiple schwannomas on nerve sheaths that compress neurons, so chronic pain—more than the deafness of NF2—is its dominant, defining symptom.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Schwannomatosis spares the vestibular nerves that NF2 attacks: it causes cranial and spinal schwannomas but characteristically NOT bilateral vestibular schwannomas, so the absence of those hearing-nerve tumors distinguishes it from neurofibromatosis type 2.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Schwannomas in schwannomatosis are well-circumscribed nerve-sheath tumors with a fibroblast-like stroma: their spindle (Schwann) cells and collagenous matrix form encapsulated masses distinct from the infiltrating plexiform neurofibromas of NF1.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Schwannomatosis can surface in the skin: peripheral and cutaneous schwannomas form palpable nodules along nerves, and unlike NF2 these patients lack vestibular schwannomas—so painful subcutaneous nerve tumors without hearing loss suggest schwannomatosis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Stereotactic radiosurgery (photon-based) treats select schwannomas: focused radiation can control growing or surgically risky nerve-sheath tumors, though in a tumor-prone syndrome it is balanced against the small risk of inducing further or malignant tumors.
- `connects-to` → **[Musculoskeletal system](../musculoskeletal-system/README.md)** — Schwannomatosis dominates the musculoskeletal experience as chronic pain: multiple schwannomas along spinal and peripheral nerves cause severe, often disabling pain rather than the deficits seen in NF2—so pain control is the central management challenge.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Schwannomatosis links to RAS-ERK through LZTR1: the LZTR1 gene normally degrades RAS, so its loss lets RAS-ERK signaling drive Schwann-cell tumor growth—one of the two molecular routes (with SMARCB1) to this multiple-schwannoma syndrome.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Schwannomatosis tumors arise from Schwann cells, the peripheral counterpart of oligodendrocytes: both make myelin, but Schwann cells wrap peripheral nerves—so these tumors form along peripheral nerves rather than in the brain's oligodendrocyte territory.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Schwannoma growth engages PI3K-mTOR signaling: alongside RAS-ERK, loss of the tumor-suppressor inputs activates mTOR to drive proliferation, making the pathway a candidate target in a syndrome whose tumors are otherwise managed surgically.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Schwannomatosis can trace to runaway RAS: LZTR1 normally tags RAS for destruction, so losing it lets RAS-MAPK signaling build up and drive schwannomas—linking the syndrome to the RASopathies like Noonan.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Schwannomatosis tumors grow through the Hippo effector YAP1: like NF2 schwannomas, loss of merlin and SWI/SNF function releases YAP1 to switch on growth genes, the shared pathway behind these nerve-sheath tumors.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Schwannomatosis pain is fueled by macrophages: its schwannomas are infiltrated by macrophages that release inflammatory mediators sensitizing nerves, helping explain why chronic pain—not hearing loss—is this syndrome's hallmark.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha drives the chronic pain of schwannomatosis: tumor and immune cells release this cytokine, which sensitizes nerve fibers, helping explain why disabling pain—not hearing loss—is the syndrome's defining feature.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Schwannomatosis tumors grow on PDGF and related signals: autocrine growth-factor loops feed the multiple schwannomas, so PDGF-receptor and other kinase inhibitors are explored to slow them in this hard-to-treat nerve disease.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame the schwannomatosis nerve: recruited into the schwannomas, they release histamine and proteases that sensitize nerve endings, adding to the macrophage-driven neuroinflammation behind the syndrome's relentless pain.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Schwannomatosis pain is electrical, carried by sodium: schwannoma-damaged nerves cluster sodium channels that fire spontaneously, generating the relentless, hard-to-treat pain that defines the syndrome.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Schwannomas are built on thick-walled vessels: their endothelial cells form the hyalinized, dilated blood vessels that, with Antoni A and B areas, are a histologic hallmark of the tumors.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Schwannomatosis pain becomes wired into synapses: relentless nerve-tumor input sensitizes spinal dorsal-horn synapses, so central sensitization sustains the pain even beyond what the tumors alone explain.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy confirms the tumors are schwannomas: their cells wrap in continuous basal lamina and stack long-spacing collagen as Luse bodies, the same ultrastructure of nerve-sheath origin found across the schwannoma family.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P carries schwannomatosis's defining misery: the tumors irritate sensory nerves into releasing this pain neuropeptide, driving the chronic, often disabling pain that — more than tumor growth — dominates the disorder.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium currents amplify the pain: tumor-irritated sensory neurons open voltage-gated calcium channels to fire and release their neuropeptides, so calcium-channel blockers are among the drugs tried against schwannomatosis pain.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Schwannomas betray themselves by their weave: the compact Antoni A zones palisade into collagen-walled Verocay bodies while loose, collagen-rich Antoni B areas fill the rest — the matrix architecture pathologists read to call a schwannoma.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Losing the brake on growth wakes a survival pathway: when the tumor-suppressor merlin or its partners fail, PI3K-AKT-mTOR signaling runs unchecked, helping the Schwann cells proliferate into the multiple schwannomas that define the syndrome.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium channels are the nerve's brake on firing: by setting the resting potential and cutting short each spike, channels like Kv7 quiet overactive pain neurons, making potassium-channel openers a target for the relentless pain of schwannomatosis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains read these tumors: a schwannoma stains strongly and diffusely for S100 and SOX10, and the mosaic, patchy loss of SMARCB1 (INI1) staining points to schwannomatosis and away from the NF2-type tumors it mimics.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — The defining feature is pain, and serotonin helps tame it: SNRI antidepressants like duloxetine boost serotonin and noradrenaline in the spinal cord's descending pain pathways, a mainstay against the chronic neuropathic pain that dominates schwannomatosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Schwannomas can stud the gut: the syndrome's nerve-sheath tumors arise along abdominal and pelvic nerves and within the bowel wall, where they can bleed or, growing large, press on and obstruct the intestine.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Losing SMARCB1 hands control to EZH2: the SWI/SNF subunit normally opposes the EZH2-PRC2 complex, so its loss in schwannomatosis tumors leaves them dependent on EZH2 — the vulnerability that EZH2 inhibitors like tazemetostat exploit in SMARCB1-deficient cancers.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Inheritance in schwannomatosis is tricky: SMARCB1 and LZTR1 pass dominantly but with incomplete penetrance and frequent mosaicism, so genetic counseling must explain why a parent may be mildly affected yet a child severely so.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The tumor's immune surroundings draw interest: schwannomas recruit regulatory T cells and macrophages into their microenvironment, and SMARCB1-deficient tumors more broadly are studied for how this immune setting might be turned against them.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — The pain becomes wired into the cord: persistent input from the schwannomas drives glutamate-NMDA central sensitization in the spinal dorsal horn, amplifying signals so the pain outlasts and outstrips the tumors themselves — a target for drugs like gabapentin.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Inflammation around the tumor lights up nociceptors: bradykinin released in the irritated tissue directly excites and sensitizes the pain nerve endings of nearby schwannomas, a peripheral trigger of the disorder's defining chronic pain.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — The tumors recruit their own blood supply: schwannomas express VEGF to drive angiogenesis, and anti-VEGF therapy with bevacizumab — used in related NF2 schwannomas — can shrink them and ease symptoms.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Merlin loss lifts a brake on STAT3: beyond Hippo-YAP, the NF2/SMARCB1-deficient schwannoma cell shows STAT3 activation that supports its survival and growth, a signaling node studied alongside the syndrome's other pathways.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Repeated tumor surgery clots the veins: schwannomatosis often requires multiple operations to remove painful schwannomas, and the immobility and surgery carry a perioperative venous thromboembolism risk.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Surgery carries infectious risk: the repeated spinal and peripheral-nerve operations used to debulk painful schwannomas can be complicated by wound infection and sepsis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Unrelenting pain darkens mood: the defining feature of schwannomatosis is chronic, often severe pain, and living with intractable pain and progressive disease drives a high burden of depression that shapes quality of life.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Treating its pain courts dependence: because chronic pain dominates schwannomatosis and responds poorly to surgery, long-term opioid use is common and carries the attendant risk of tolerance, dependence and opioid use disorder.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Its widespread pain overlaps and confounds: the diffuse, multifocal pain of schwannomatosis can resemble or coexist with fibromyalgia, complicating diagnosis and sharing the central pain-sensitization that resists analgesia.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Relentless pain robs patients of sleep: the chronic, often nocturnal pain that defines schwannomatosis fragments sleep and drives a persistent insomnia that in turn lowers pain tolerance the next day.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Unpredictable pain and tumor uncertainty breed worry: the constant pain, surveillance for new schwannomas and fear of progression in schwannomatosis foster chronic anxiety alongside its better-recognized depression.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Its long-term opioids quietly thin the bones: the chronic opioid therapy needed for schwannomatosis pain suppresses sex hormones, and the resulting hypogonadism, with pain-related inactivity, accelerates loss of bone density.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Repeated tumour surgery means repeated wounds: the surgical resection of painful schwannomas — often multiple over a lifetime in schwannomatosis — leaves wounds that must heal, sometimes near nerves.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its chronic opioids constipate the gut: the long-term opioid analgesia central to schwannomatosis pain control slows intestinal transit, causing opioid-induced constipation that can become severe.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Long-term NSAIDs wear on the kidneys: the chronic non-steroidal anti-inflammatory use that helps control schwannomatosis pain can cause analgesic nephropathy and a slow decline in kidney function.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its tumours can be felt under the skin: schwannomatosis produces cutaneous and subcutaneous schwannomas as palpable, often painful nodules along peripheral nerves.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its chronic opioids suppress the hormones: the long-term opioid therapy that controls schwannomatosis pain causes opioid-induced androgen deficiency with hypogonadism and low libido.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Tumours and opioids both threaten breathing: intrathoracic or vagal schwannomas can compress the airway, and the high-dose opioids used for its pain carry a risk of respiratory depression.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Pelvic tumours can block the urinary tract: retroperitoneal and pelvic schwannomas can compress the ureters and bladder, causing obstruction and urinary symptoms.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chest tumours sit against the great vessels: intrathoracic and paraspinal schwannomas can lie against the great vessels and sympathetic chain, complicating surgery and causing autonomic symptoms.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its tumour-suppressor loss shapes immunity: the SMARCB1 (SWI/SNF) loss it shares with rhabdoid tumours alters chromatin regulation and the tumour's immune microenvironment.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — Pain is its dominant feature: chronic, often severe pain from schwannomas is treated multimodally with NSAIDs like ibuprofen, alongside neuropathic agents and opioids.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — A fellow schwannoma syndrome: Carney complex causes psammomatous melanotic schwannomas, joining schwannomatosis and NF2 among the inherited schwannoma-predisposing disorders.
- `connects-to` → **[Curcumin](../../../03-medicine/03-food/curcumin/README.md)** — Anti-inflammatory adjuncts are tried: turmeric-derived curcumin and other anti-inflammatory supplements are used by some for the chronic pain of schwannomatosis, though evidence is limited.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Anti-angiogenics shrink schwannomas: bevacizumab against VEGF can reduce schwannoma volume and stabilise hearing in NF2-spectrum disease, and mTOR and MEK inhibitors are under study for inoperable or progressive tumours.
- `connects-to` → **[Dexamethasone](../../../03-medicine/01-modern/12-anti-inflammatory/dexamethasone/README.md)** — Steroids calm acute flares: corticosteroids like dexamethasone reduce peritumoral oedema and the acute nerve-compression pain of an enlarging schwannoma, and are used perioperatively, though they do not control the underlying tumour.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — A converging mTOR syndrome: like TSC, schwannomatosis is a tumour-suppressor disorder whose pathway feeds into mTOR signalling — merlin loss de-represses mTOR much as hamartin-tuberin loss does — making mTOR inhibition a shared therapeutic theme.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — A shared SMARCB1 lesion: SMARCB1-related schwannomatosis loses the same SWI/SNF subunit inactivated in SMARCB1-deficient renal medullary carcinoma and rhabdoid tumours, linking a benign nerve-tumour syndrome to an aggressive kidney cancer.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — Both run through merlin and Hippo: schwannomatosis tumours (NF2/LZTR1) and many mesotheliomas inactivate NF2/merlin, unleashing the Hippo effector YAP—shared loss of a contact-inhibition brake in unrelated tissues.
- `connects-to` → **[Guillain-Barré](../../05-tissue/guillain-barre/README.md)** — Two diseases of the Schwann cell: schwannomatosis grows benign tumours from Schwann cells, while Guillain-Barré is an autoimmune attack on the myelin those cells make—opposite pathologies of one peripheral-nerve cell.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain is the defining feature: unlike NF2, schwannomatosis presents primarily with severe chronic neuropathic pain from peripheral schwannomas, often out of proportion to tumour size—the dominant management problem.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Schwannomas compress nerves: schwannomatosis's multiple peripheral and spinal schwannomas press on nerves and their axons, causing pain, weakness and sensory loss, without the bilateral vestibular tumours of NF2.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — A collagen-rich tumour stroma: schwannomas lay down the dense, fibrous Antoni-A matrix, and the SMARCB1/NF2-merlin loss of schwannomatosis promotes this profibrotic phenotype.
- `connects-to` → **[Ovarian Clear-Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — SWI/SNF chromatin disorders: schwannomatosis (SMARCB1) and ovarian clear-cell carcinoma (ARID1A) both arise from loss of subunits of the SWI/SNF chromatin-remodelling complex, a shared epigenetic route to very different tumours.
- `connects-to` → **[CIDP](../cidp/README.md)** — Chronic peripheral nerve disease: schwannomatosis sits in the differential of acquired chronic neuropathies like CIDP, both presenting with progressive peripheral nerve dysfunction though one is tumoural and the other inflammatory.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — A Schwann-cell disease: schwannomatosis tumours arise from the Schwann cells that ensheath peripheral nerves all the way to the neuromuscular junction, SMARCB1/LZTR1 loss driving their multifocal growth.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Pain mediator: COX-derived prostaglandins contribute to the chronic, often severe pain that dominates schwannomatosis, the rationale for NSAIDs in symptom control.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: SMARCB1/LZTR1 loss with CDK4/6-cyclin dysregulation propels the proliferation of the multiple schwannomas characteristic of the syndrome.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Hippo crosstalk: Notch signalling interacts with the NF2-merlin-Hippo-YAP axis to promote schwannoma growth in schwannomatosis.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — G1 progression: cyclin D1, upregulated by SMARCB1/LZTR1 loss, partners CDK4/6 to push schwannoma cells through the G1 checkpoint in schwannomatosis.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative oncogene: MYC activation downstream of the dysregulated Hippo and growth-factor pathways drives the proliferation of schwannomatosis tumours.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the growing schwannomas drives the VEGF angiogenesis that supplies these nerve-sheath tumours.
- `connects-to` → **[NTRK / TrkA](../../03-molecular/ntrk/README.md)** — NGF signaling through TrkA sensitizes the sensory nerve fibers entangled by schwannomatosis tumors, contributing to the chronic, often severe pain that dominates this syndrome more than the tumor mass itself.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — CGRP released from the peri-tumoral sensory nerves mediates the neurogenic inflammation and chronic pain that is the defining clinical feature of schwannomatosis—the symptom that, more than tumor burden, distinguishes it from NF2.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Schwannomatosis tumors recruit CCL2-driven macrophages that both sustain tumor growth and release mediators sensitizing nociceptors, linking the immune infiltrate directly to the pain phenotype that defines the disease.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — Like other nerve-sheath tumors, schwannomatosis schwannomas contain KIT-dependent mast cells whose stem-cell-factor signaling contributes to the inflammatory microenvironment that supports tumor growth and nociceptor sensitization.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling supports the growth and survival of the multiple schwannomas of schwannomatosis, anchoring the Schwann tumor cells within their peripheral-nerve microenvironment.
- `connects-to` → **[Src kinase](../../03-molecular/src-kinase/README.md)** — Schwannomatosis tumors frequently carry a second-hit NF2/merlin loss, and because merlin normally restrains Src/FAK at the membrane, Src disinhibition drives the loss of contact inhibition that lets schwannoma cells proliferate.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Merlin normally holds EGFR/ErbB receptors inactive at cell contacts, so the merlin-pathway loss of schwannomatosis releases EGFR-driven proliferative signaling in Schwann cells.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Downstream of merlin loss, PI3K-AKT-mTOR signaling (AKT and mTOR already mapped) is activated in schwannomas, a proliferative survival pathway and candidate target for these otherwise drug-resistant tumors.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — The chronic neuropathic pain that dominates schwannomatosis involves inflammatory cytokines including IL-6 sensitizing sensory neurons, acting alongside the substance-P and CGRP already mapped.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D1-CDK4/6 axis (both mapped) releases E2F1 to drive the proliferation of the multiple schwannomas of schwannomatosis.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of the SMARCB1/LZTR1-merlin tumor-suppressor network de-represses PI3K-AKT-mTOR signaling (PIK3CA, AKT and mTOR already mapped), which PTEN normally limits, fueling schwannoma growth.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling shapes the collagenous extracellular matrix (collagen mapped) and fibroblastic stroma of the schwannomas of schwannomatosis.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (CDK4/6, cyclin-D1 and E2F1 already mapped) contributes to the proliferation of the schwannomas of schwannomatosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) contributes to the survival signaling of schwannomatosis-associated schwannomas.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4-driven neuroinflammation around tumor-infiltrated nerves contributes to the chronic neuropathic pain that is the predominant clinical feature of schwannomatosis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is expressed in schwannomas and contributes to their tumor-microenvironment interactions in schwannomatosis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) modulates the Schwann-cell proliferation and stroma of the schwannomas of schwannomatosis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, regulated by the merlin/PI3K-AKT axis, modulate the survival of the Schwann-cell tumors of schwannomatosis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated CD8 cytotoxicity contributes to the immune surveillance of the schwannomas of schwannomatosis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling of the SMARCB1/LZTR1-deficient schwannoma cells of schwannomatosis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation restrains apoptosis in the schwannomas of schwannomatosis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory and neuropathic-pain microenvironment of schwannomatosis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the SMARCB1/LZTR1-deficient schwannoma cells of schwannomatosis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A and the SWI/SNF machinery (SMARCB1 already mapped) contribute to the epigenetic dysregulation of schwannomatosis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of schwannomatosis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the schwannomas of schwannomatosis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven neuroinflammation participates in the chronic pain and tumor microenvironment of schwannomatosis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory and pain-associated microenvironment of schwannomatosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of schwannomatosis.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Pain as the defining burden: chronic, often disabling pain out of proportion to tumour size is the hallmark of schwannomatosis, and the mu-opioid receptor mediates the opioid analgesia central to its frequently refractory pain management.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Neuropathic-pain mechanism: the neuropathic pain of schwannomatosis is treated with gabapentinoids that act on the voltage-gated calcium-channel alpha-2-delta subunit, and calcium influx drives the ectopic nociceptor firing from tumour-compressed nerves.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — YAP-driven signaling: SMARCB1- and NF2/merlin-related loss de-represses YAP (already mapped), upregulating the AXL receptor tyrosine kinase that promotes schwannoma growth and offers a targetable node downstream of the core tumour-suppressor defect.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Neurogenic pain: nitric oxide participates in the neuroinflammation and sensitisation of the nerves compressed by schwannomas, contributing to the chronic pain that is the dominant and often disabling symptom of schwannomatosis.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Tumour immune microenvironment: MHC class II-mediated antigen presentation shapes the T-cell and macrophage infiltrate of schwannomas, of interest as immunotherapy and anti-inflammatory approaches to their growth and pain are explored.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Hormone sensitivity: like the related meningiomas and schwannomas of NF2, the tumours of schwannomatosis can express hormone receptors, and estrogen may influence their growth, including reports of enlargement during pregnancy.
- `connects-to` → **[T-cytotoxic cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Immune infiltrate: cytotoxic CD8 T cells (MHC class II and perforin already mapped) form part of the immune infiltrate of schwannomas, of interest to the immunotherapy approaches explored for these painful nerve-sheath tumours.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune microenvironment: IL-10 in the schwannoma microenvironment shapes its immune and inflammatory milieu (MHC class II already mapped), part of the neuroinflammation that drives the chronic pain characteristic of schwannomatosis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell pain: mast cells releasing histamine in and around schwannomas contribute to the neuroinflammatory environment and the sensitisation (substance P and CGRP already mapped) that produces the dominant chronic pain of schwannomatosis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 mast-cell milieu: IL-4 supports the mast cells (already mapped) and polarises macrophages (already mapped) toward an M2 phenotype (IL-10 already mapped), part of the type-2 neuroinflammatory microenvironment that drives the pain of schwannomatosis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 inflammation: IL-13, with IL-4 (already mapped), reflects the type-2 cytokine arm of the mast-cell-rich (already mapped) neuroinflammatory milieu of the schwannomas, part of the microenvironment behind the chronic pain of schwannomatosis.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative microenvironment: the schwannomas generate oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of the tumour and neuroinflammatory microenvironment of schwannomatosis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Analgesic magnesium: magnesium blocks the NMDA receptor of the glutamate (already mapped) signalling, and it is used as an adjunct for the chronic neuropathic pain (substance P and CGRP already mapped) that dominates schwannomatosis.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton radiotherapy: proton radiosurgery treats the spinal and skull-base schwannomas of schwannomatosis where surgery risks the nerve, sparing the adjacent cord and cranial nerves.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophilic milieu: IL-5, with the mast cells and the type-2 cytokines (IL-4 and IL-13 already mapped), recruits eosinophils to the neuroinflammatory schwannoma microenvironment behind the chronic pain of schwannomatosis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Nerve-adipose adipokine: leptin from the nerve-associated and marrow adipose tissue signals within the metabolic microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is the adipokine of the metabolic microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the neuroinflammatory schwannoma microenvironment of schwannomatosis.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the neuroinflammatory microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the schwannoma microenvironment of schwannomatosis.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen (MHC already mapped) within the immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral arm: the plasma cells secrete the antibodies (already mapped) of the humoral response within the immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate cytotoxicity: the NK cells (perforin already mapped) provide the innate cytotoxic surveillance within the immune microenvironment of the schwannomas of schwannomatosis.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the schwannomas of schwannomatosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Tumour complement: the complement C3 activation contributes to the inflammatory dimension of the macrophage-rich (already mapped) schwannoma microenvironment of schwannomatosis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the schwannoma stroma of schwannomatosis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Perineural alarmin: TSLP released by the schwannoma's perineurial fibroblasts and macrophages (already mapped) activates mast cells (present in schwannoma stroma) to promote the type-2 microenvironment and the chronic pain that defines schwannomatosis.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement brake: C1-esterase inhibitor modulates the classical complement pathway (C3 and C5aR1 already mapped) activated on the macrophage-rich (already mapped) schwannoma stroma of schwannomatosis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Perineural EPO signalling: erythropoietin, via EPOR expressed on Schwann cells and perineural cells, exerts anti-apoptotic and anti-inflammatory effects that modulate the neuropathic pain and nerve dysfunction of schwannomatosis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Schwannoma stroma scaffold: periostin secreted by fibroblastic stroma of schwannomatosis tumours promotes Schwann-cell survival and tumour-cell integrin-αv signalling, amplifying nerve-sheath tumour growth driven by SMARCB1/LZTR1 loss.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement in schwannoma: complement C5a, generated from C3 (already mapped) and acting via C5aR1 (already mapped) on the macrophage-rich schwannomatosis stroma, amplifies the neuroinflammation and chronic neuropathic pain of the disease.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement-evasion scaffold: schwannomatosis tumour cells recruit factor H to shield against complement lysis, exploiting the same C3/C5aR1 complement cascade already mapped and limiting immune clearance of merlin-deficient nerve-sheath tumours.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — SWN melatonin: melatonin via MT1/MT2 receptors on schwannomatosis Schwann cells (already mapped) and macrophages modulates the neuroinflammatory chronic pain of schwannomatosis, counteracting the substance-P (already mapped) and bradykinin (already mapped) pain sensitisation.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — SWN androgen axis: testosterone via androgen receptor on SMARCB1/LZTR1-deficient (already mapped) Schwann cells modulates the NF2 (already mapped) tumour-suppressor pathway and the sex-dimorphic growth of peripheral nerve-sheath tumours in schwannomatosis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — SWN prolactin: prolactin via JAK2 (already mapped) and STAT3 (already mapped) signalling on SMARCB1-deficient schwannoma cells promotes tumour-cell survival, amplifying the proliferative drive from the EGFR (already mapped) and mTOR (already mapped) axes in schwannomatosis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — SWN oxytocin: oxytocin via OXTR on schwannomatosis Schwann cells (already mapped) modulates the neuroinflammatory pain cascade, reducing the substance-P (already mapped) and bradykinin (already mapped)-driven chronic neuropathic pain of schwannomatosis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — SWN vasopressin: vasopressin via V1aR on schwannomatosis macrophages (already mapped) modulates neuroinflammatory bradykinin (already mapped) and substance-P (already mapped)-driven pain sensitisation of peripheral nerve-sheath tumours in schwannomatosis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — SWN selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species in SMARCB1/LZTR1-deficient schwannoma cells, reducing oxidative-stress-driven mTOR (already mapped) and EGFR (already mapped) proliferative signalling in schwannomatosis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — SWN iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour surveillance; thyroid deficiency amplifies VEGF (already mapped) and mTOR (already mapped) schwannoma growth and IL-6 (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — SWN copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped), drives tumour stromal remodelling; copper angiogenesis amplifies VEGF (already mapped); copper deficiency impairs macrophage (already mapped) and T-cytotoxic-cell (already mapped) immunity in SWN.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — SWN zinc: zinc, as metalloproteinase cofactor in macrophages (already mapped) and mast-cell (already mapped), modulates schwannoma invasion; zinc deficiency amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped)-driven cascade of schwannomatosis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — SWN iron: iron, as ribonucleotide reductase cofactor in macrophages (already mapped) and mast-cell (already mapped), supports DNA repair; iron overload amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) tumour cascade of schwannomatosis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — SWN phosphorus: phosphorus, as ATP donor in mTOR (already mapped) signalling in macrophages (already mapped) and mast-cell (already mapped), fuels tumour proliferation; phosphorus dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — SWN chloride: chloride channels in macrophages (already mapped) and mast-cell (already mapped) regulate tumour-immune homeostasis; chloride dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — SWN carbon: carbon, as metabolic backbone of mTOR (already mapped) and EGFR (already mapped) in macrophages (already mapped) and mast-cell (already mapped), drives proliferative signalling; carbon dysregulation amplifies IL-6 (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — SWN hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and mast-cell (already mapped), modulates tumour-immune balance; hydrogen dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — SWN nitrogen: nitrogen, as purine backbone in macrophages (already mapped) and mast-cell (already mapped), fuels nucleotide synthesis; nitrogen dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — SWN oxygen: tumour hypoxia in schwannomatosis drives HIF-1α and VEGF (already mapped) angiogenesis; oxygen depletion amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — SWN sulfur: sulfur, as glutathione in macrophages (already mapped) and mast-cell (already mapped), quenches oxidative stress; sulfur deficiency amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — SWN PD-1: PD-1 checkpoint on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates tumour-immune surveillance; PD-1 dysregulation amplifies IL-6 (already mapped) and EGFR (already mapped) and mTOR (already mapped) cascade of schwannomatosis.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — SWN glp-1: GLP-1 from macrophages (already mapped) and mast cells (already mapped) modulates schwannoma metabolic-inflammatory tone; glp-1 dysfunction amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — SWN angiotensin-ii: angiotensin-II from macrophages (already mapped) and endothelial cells (already mapped) drives schwannoma angiogenesis; angiotensin-ii excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — SWN wnt-beta-catenin: WNT/β-catenin on Schwann cells (already mapped) and macrophages (already mapped) drives schwannoma growth; wnt-beta-catenin loss amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — SWN rankl: RANKL from macrophages (already mapped) and Schwann cells (already mapped) promotes schwannoma immune evasion; rankl excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — SWN il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates schwannoma immune surveillance; il-2 dysregulation amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — SWN fibronectin: fibronectin in Schwann cells (already mapped) and macrophages (already mapped) promotes schwannoma ECM remodelling; fibronectin excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — SWN igf-1: IGF-1 from Schwann cells (already mapped) and macrophages (already mapped) drives schwannoma growth; igf-1 excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) proliferative cascade of schwannomatosis.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — SWN activin-a: activin-A from Schwann cells (already mapped) and macrophages (already mapped) regulates schwannoma immune-fibrotic balance; activin-a excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — SWN calcitonin: calcitonin from macrophages (already mapped) and Schwann cells (already mapped) modulates calcium balance in schwannomatosis; calcitonin excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — SWN insulin-receptor: insulin receptor on macrophages (already mapped) and Schwann cells (already mapped) drives schwannoma metabolic repair; insulin-receptor loss amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — SWN aldosterone: aldosterone from macrophages (already mapped) and Schwann cells (already mapped) modulates ion balance in schwannomatosis; aldosterone excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — SWN androgen-receptor: androgen receptor on macrophages (already mapped) and Schwann cells (already mapped) modulates schwannoma hormonal tone; androgen excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — SWN norepinephrine: norepinephrine from macrophages (already mapped) and Schwann cells (already mapped) modulates adrenergic tone in schwannomas; norepinephrine excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — SWN adrenomedullin: adrenomedullin from macrophages (already mapped) and Schwann cells (already mapped) modulates vascular tone in schwannomas; adrenomedullin loss amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — SWN bdnf: BDNF from macrophages (already mapped) and Schwann cells (already mapped) drives nerve sheath proliferation; bdnf excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — SWN osteopontin: osteopontin from macrophages (already mapped) and Schwann cells (already mapped) promotes schwannoma invasion; osteopontin excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — SWN fgfr: FGFR on macrophages (already mapped) and Schwann cells (already mapped) drives schwannoma stromal growth; fgfr dysregulation amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — SWN epinephrine: epinephrine from macrophages (already mapped) and Schwann cells (already mapped) modulates schwannoma adrenergic tone; epinephrine excess amplifies il-6 (already mapped) and egfr (already mapped) and mtor (already mapped) cascade of schwannomatosis.

[^merker-2012-schwannomatosis]: Merker VL, Esparza S, Smith MJ, Stemmer-Rachamimov A, Plotkin SR. Clinical features of schwannomatosis: a retrospective analysis of 87 patients. *Oncologist.* 2012;17(10):1317-1322. [doi:10.1634/theoncologist.2012-0162](https://doi.org/10.1634/theoncologist.2012-0162) · [PubMed 22927469](https://pubmed.ncbi.nlm.nih.gov/22927469/)
[^piotrowski-2014-lztr1]: Piotrowski A, Xie J, Liu YF, et al. Germline loss-of-function mutations in LZTR1 predispose to an inherited disorder of multiple schwannomas. *Nat Genet.* 2014;46(2):182-187. [doi:10.1038/ng.2855](https://doi.org/10.1038/ng.2855) · [PubMed 24362817](https://pubmed.ncbi.nlm.nih.gov/24362817/)
