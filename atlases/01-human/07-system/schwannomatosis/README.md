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

[^merker-2012-schwannomatosis]: Merker VL, Esparza S, Smith MJ, Stemmer-Rachamimov A, Plotkin SR. Clinical features of schwannomatosis: a retrospective analysis of 87 patients. *Oncologist.* 2012;17(10):1317-1322. [doi:10.1634/theoncologist.2012-0162](https://doi.org/10.1634/theoncologist.2012-0162) · [PubMed 22927469](https://pubmed.ncbi.nlm.nih.gov/22927469/)
[^piotrowski-2014-lztr1]: Piotrowski A, Xie J, Liu YF, et al. Germline loss-of-function mutations in LZTR1 predispose to an inherited disorder of multiple schwannomas. *Nat Genet.* 2014;46(2):182-187. [doi:10.1038/ng.2855](https://doi.org/10.1038/ng.2855) · [PubMed 24362817](https://pubmed.ncbi.nlm.nih.gov/24362817/)
