---
schema: human-scale-entry/v1
id: chordoma
name: Chordoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chordoma arises from notochordal remnants; skull base (~35%), sacrococcygeal (~50%), mobile spine (~15%); TBXT overexpression in >95%; physaliferous cell histology; proton RT + surgery standard; no FDA-approved systemic agent; imatinib, sorafenib, mTOR inhibitors active."
aliases: ["chordoma", "skull base chordoma", "sacral chordoma", "clival chordoma", "spinal chordoma", "brachyury chordoma", "notochordal tumor", "chordoma TBXT", "physaliferous cell tumor", "chordoma dedifferentiated"]
sources:
  - id: stacchiotti-2012-imatinib-chordoma
    type: peer-reviewed
    cite: "Stacchiotti S, Longhi A, Ferraresi V, et al. Phase II study of imatinib in advanced chordoma. J Clin Oncol. 2012;30(9):914-920."
    doi: "10.1200/JCO.2011.35.3656"
    pmid: "22330157"
    url: "https://doi.org/10.1200/JCO.2011.35.3656"
  - id: yang-2009-tbxt-chordoma
    type: peer-reviewed
    cite: "Yang XR, Ng D, Alcorta DA, et al. T (brachyury) gene duplication confers major susceptibility to familial chordoma. Nat Genet. 2009;41(11):1176-1178."
    doi: "10.1038/ng.454"
    pmid: "19801977"
    url: "https://doi.org/10.1038/ng.454"
cross_links:
  - target: 01-human/03-molecular/tbxt
    relation: connects-to
    note: "TBXT (brachyury) overexpression in >95% chordomas defines lineage identity; tandem TBXT duplication at 6q27 → familial chordoma; TBXT FISH or IHC (strong nuclear brachyury) is the diagnostic confirmatory test; TBXT knockdown → chordoma cell growth arrest and apoptosis in vitro."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PTEN loss in ~15-20% chordomas → AKT/mTOR hyperactivation; mTOR pathway activated downstream of FGFR/PDGFR in chordoma; everolimus achieves stable disease in ~50% (Schwab 2015, Phase 2); mTOR + FGFR combinations under investigation; lapatinib + everolimus Phase 2 showed activity."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGFR1/2/3 overexpressed in ~50% chordomas; FGFR-driven MAPK/PI3K → tumor growth; erdafitinib (pan-FGFR) active in FGFR-altered chordoma (Phase 2); FGF4/FGF8 autocrine loop driven by TBXT transcription; FGFR inhibitors synergize with mTOR inhibitors in preclinical models."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGFRA/PDGFRB overexpressed in >80% chordomas; imatinib (PDGFR inhibitor) achieves stable disease in ~35-40% (Stacchiotti 2012, Phase 2); PDGF-BB autocrine loop in chordoma cells; erlotinib + imatinib combination achieves partial response in small Phase 2 series."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss in ~15-20% chordomas → AKT-mTOR hyperactivation + increased VEGF; PI3K inhibitors studied in PTEN-deficient chordoma; PTEN co-deletion with CDKN2A in ~8-10% → simultaneous CDK4/6 and mTOR hyperactivation; PTEN loss correlates with worse prognosis in chordoma."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDKN2A deletion in ~30-40% of chordomas → CDK4/6 hyperactivation → RB1 phosphorylation → S-phase entry; palbociclib Phase 2 (NCT03110744) in CDKN2A-deleted chordoma; dedifferentiated chordoma shows CDK4 amplification and MDM2 co-amplification as hallmarks."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A homozygous deletion in ~30-40% chordomas; eliminates both p16 (CDK4/6 checkpoint) and ARF (p53 stabilization); deletion at 9p21 is among the earliest molecular events in chordoma progression; CDKN2A loss correlates with worse prognosis and dedifferentiated transformation."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Chordoma and Ewing sarcoma are both rare bone tumors with one defining genetic lesion — chordoma's TBXT/brachyury overexpression versus Ewing's EWSR1-FLI1 fusion — but chordoma is a slow midline tumor of adults from notochord remnants, Ewing a small-cell tumor of children."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Chordoma arises along the axial skeleton from embryonic notochord remnants — ~50% sacrum, ~35% skull base (clivus), the rest mobile spine; this midline bony location, often diagnosed late and abutting critical structures, makes en-bloc resection the mainstay yet often incomplete."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Skull-base (clival) chordomas grow against the brainstem, cavernous sinus, and cranial nerves, causing diplopia, headache, and cranial-nerve palsies; their proximity to brain and vessels limits margins, making proton-beam radiotherapy central to controlling residual tumor."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Chordoma is defined by its radiotherapy needs: nestled against the brainstem and cord at the skull base and sacrum, it needs very high radiation doses that proton-beam therapy delivers while sparing neural tissue—central since complete resection is often impossible."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Chordoma and osteosarcoma are both primary bone malignancies but differ fundamentally: chordoma is a slow-growing notochord-remnant tumor of the axial skeleton (skull base/sacrum) driven by brachyury, while osteosarcoma is an aggressive osteoid-producing tumor of long bones."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Chordoma's relationship to bone-forming cells is distinctive: although it grows within and destroys bone, it does not arise from osteoblasts but from notochord remnants, producing a lytic, gelatinous mass rather than the bone matrix osteoblasts lay down—imaging shows destruction."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Chordoma and meningioma are both slow-growing skull-base/spinal tumors in the same differential: chordoma is a destructive midline tumor of notochord remnants, while meningioma is a dural-based extra-axial tumor—told apart by location, imaging, and immunostains."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Chordoma's characteristic histology is a myxoid, fibroblast-like stroma studded with physaliphorous (bubbly) cells: the matrix and spindle-cell background give a deceptively bland, cartilage-like look, so brachyury immunostaining confirms its notochordal origin."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Chordoma and synovial sarcoma are rare tumors of young adults with aggressive local behavior needing wide resection plus radiotherapy: chordoma is brachyury-driven from notochord remnants, synovial sarcoma SS18-SSX-fusion-driven—different drivers, similar challenge."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR is a therapeutic target in chordoma: these slow-growing notochordal tumors often activate EGFR signaling, so EGFR inhibitors like erlotinib are used off-label in advanced disease where surgery and radiation fail—chordoma resists conventional chemotherapy."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Chordoma threatens neurons by location: arising along the spine and skull base from notochord remnants, it compresses the brainstem, spinal cord and cranial nerves, so neurological deficits—not metastasis—drive its morbidity despite slow growth."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Chordoma's hallmark cells sit in a collagen-rich matrix: physaliphorous bubble cells float in a myxoid, collagenous stroma recapitulating the notochord, giving the tumor its distinctive histology that, with brachyury staining, confirms the diagnosis."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy is the radiation mainstay for chordoma: these radioresistant skull-base and sacral tumors sit against the brainstem and spinal cord, so protons' sharp dose falloff delivers high tumor dose while sparing critical neural structures."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Chordoma threatens the nervous system by location: arising along the spine and skull base from notochord remnants, it compresses the brainstem, cranial nerves and spinal cord, so its slow growth still causes severe neurological deficits and demands aggressive local control."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-ion radiotherapy is an alternative for chordoma: heavy carbon ions deliver dense, highly damaging dose to these notoriously radioresistant tumors, useful when surgery is incomplete or the tumor abuts neural structures—an option in specialized particle centers."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Chordoma spreads most often to the lung: though it grows slowly and locally along the spine and skull base, late metastasis favors the lungs, so chest imaging is part of follow-up for this notochord-derived bone tumor."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Chordoma is a target for vaccine immunotherapy: nearly all chordomas express brachyury (TBXT), and a brachyury-directed cancer vaccine trains the immune system against this otherwise hard-to-drug developmental transcription factor."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Chordoma's radioresistance is partly an oxygen problem: poorly oxygenated tumor regions resist conventional X-rays, so high-dose proton and carbon-ion radiotherapy—less dependent on oxygen and more precise near the spinal cord—are used instead."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Chordoma destroys bone through osteoclasts: as it grows in the skull base or sacrum it recruits bone-resorbing osteoclasts that erode the surrounding skeleton, so anti-resorptive drugs are explored to slow the local destruction this hard-to-resect tumor causes."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Chordoma is a vascular tumor that responds to anti-VEGF therapy: it expresses VEGF to grow blood vessels, which is why multi-target TKIs that block VEGF receptors (like sunitinib) can stall this otherwise treatment-resistant cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Losing p53 makes chordoma more aggressive: while most chordomas grow slowly on brachyury, TP53 mutation marks the dangerous shift toward dedifferentiated, fast-growing tumors with a far worse prognosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Chordoma leans on the PI3K-AKT-mTOR growth axis: AKT signaling is frequently active and, with PTEN loss, drives proliferation in these brachyury-dependent tumors, so AKT-mTOR inhibitors are studied for a cancer resistant to chemotherapy."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "MET signaling can drive aggressive chordoma: amplification or activation of this receptor promotes invasion and growth, adding to the brachyury-driven biology and offering another targetable kinase in a notoriously treatment-resistant bone tumor."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Chordoma is a target for T-cell immunotherapy against brachyury: because the tumor depends on this lineage antigen, vaccines and engineered cytotoxic T cells aim to direct a killing response at a protein cancer cells cannot easily discard."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Chordoma eats away calcium-rich bone: arising in the skull base and sacrum, it destroys the bony matrix as it grows, dissolving the calcium scaffold and threatening the spine and cranial nerves it surrounds."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Chordoma shelters in a macrophage-rich stroma: tumor-associated macrophages populate its microenvironment and dampen immunity, part of why this slow but stubborn tumor resists treatment and recurs."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Sacral chordoma presses on the bowel: the most common chordoma site sits against the rectum and pelvic nerves, so large tumors cause constipation, bowel and bladder dysfunction, and low back pain."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Chordoma grows against the nerves: skull-base and sacral tumors compress cranial nerves and the cauda equina, causing the neuropathic pain, weakness and bowel-bladder dysfunction that often first signal it."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Chordoma metastasizes late: though slow-growing and locally destructive, it can seed the lungs, liver and bone over years, especially after repeated local recurrences."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Chordoma builds its own vasculature: VEGF recruits endothelial cells to feed the tumor, and anti-angiogenic drugs are among the systemic options for this radiation- and surgery-dependent cancer."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy names the chordoma cell: the physaliphorous ('bubble-bearing') cell, its cytoplasm ballooning with glycogen and mucin-filled vacuoles, betrays the tumor's origin in leftover notochord tissue."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Chordoma is born in bone: it grows from notochord remnants in the marrow-bearing vertebrae of the sacrum and skull base, destroying the bone it arises in and occasionally seeding distant skeletal metastases."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "A skull-base chordoma blurs and crosses the vision: growing at the clivus it compresses the cranial nerves that move the eyes, causing double vision and gaze palsies that often first bring the patient in."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody marks and may treat the notochordal tumor: the brachyury (TBXT) protein, detected by immunostaining, is the diagnostic hallmark of chordoma, and a brachyury cancer vaccine is in trials to rouse immunity against it."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "A sacral chordoma strikes at the body's lower controls: growing in the sacrum it compresses the nerve roots governing erection, ejaculation, and continence, so sexual and pelvic dysfunction can be early or surgical consequences."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The sacral tumor disconnects the pelvic smooth muscle: damage to the sacral roots from the chordoma or its removal leaves the bladder and bowel smooth muscle without control, causing retention, incontinence, and constipation."
  - target: 01-human/07-system/tuberous-sclerosis-complex
    relation: connects-to
    note: "Chordoma turns up in tuberous sclerosis: pediatric chordomas are reported in TSC patients, a link that fits chordoma's reliance on PI3K-AKT-mTOR signaling — the same pathway that TSC1/TSC2 loss unleashes — and points to mTOR inhibitors as therapy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Chordoma is an immunologically cold tumor: it expresses PD-L1 and recruits regulatory T cells that suppress local immunity, a microenvironment that helps it evade attack and is the rationale for testing checkpoint blockade in this radioresistant cancer."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Chordoma is treated with hydrogen nuclei: proton-beam radiation — accelerated bare hydrogen nuclei — deposits its dose at a sharp Bragg peak, letting high doses hit clival and sacral tumors while sparing the brainstem and spinal cord just millimeters away."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "A rare aggressive variant loses SMARCB1: poorly-differentiated chordoma deletes this chromatin-remodeling gene, the same loss that defines rhabdoid tumors, marking a more lethal subtype that strikes the young."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "SMARCB1 loss links them across tissues: poorly-differentiated chordoma and ATRT share deletion of the same chromatin-remodeling gene, an epigenetic lesion that ties a notochordal bone tumor to a brain rhabdoid tumor."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Immunotherapy aims past the cold tumor: brachyury-targeted vaccines and natural-killer-cell-engaging approaches are being tested to attack chordoma, whose poor blood supply and immune evasion resist conventional treatment."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Hippo-YAP signaling feeds the notochordal tumor: YAP1 activity cooperates with brachyury to sustain chordoma cell proliferation and survival, marking the Hippo pathway as a candidate target in a cancer with few effective drugs."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Chordoma hurts by crushing nerves: as it grows in the sacrum or clivus it compresses nerve roots and the spinal cord, causing the radicular and neuropathic pain that is often its first symptom."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "A destructive axial bone lesion poses a differential: a lytic sacral or vertebral mass on imaging must be told apart from myeloma and metastasis, since chordoma's notochordal origin and brachyury staining set it apart and change treatment."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 supports the slow-growing tumor: chordoma cells show STAT3 activation downstream of receptor signaling that backs their survival, one of the pathways explored where this radioresistant tumor needs systemic options."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Major axial surgery clots the veins: the long sacral and skull-base resections chordoma requires, with prolonged immobility afterward, make deep-vein thrombosis and pulmonary embolism a real perioperative risk."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Deep resections invite infection: extensive sacral and clival surgery, sometimes with CSF leak, can be complicated by deep wound infection and meningitis that progress to sepsis."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "It destroys bone and its radiation weakens more: chordoma erodes the sacrum and clivus directly, while the high-dose proton/photon radiation used to control it causes osteoradionecrosis and insufficiency fractures."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Relentless pain and a poor cure weigh on mood: chronic neuropathic pain, disfiguring skull-base surgery, bowel-bladder dysfunction and high recurrence give chordoma a substantial psychological burden."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Advanced disease blunts the marrow: locally aggressive or metastatic chordoma with its inflammatory burden, compounded by major surgery and radiation, can produce an anemia of chronic disease."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its radical resections heal poorly: the extensive skull-base and sacral surgery for chordoma, often with prior or adjuvant radiation, leaves complex wounds prone to dehiscence, CSF leak and slow healing."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Skull-base tumor encircles the great vessels: clival chordomas encase the carotid and basilar arteries, and tumor or its surgery can compromise these vessels, risking ischemic stroke."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Sacral tumor disrupts the bladder: a sacral chordoma damages the nerves controlling the bladder, and the resulting neurogenic bladder with recurrent infection and obstruction can injure the kidneys over time."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It compresses the gut from both ends: a sacral chordoma damages the nerves to the rectum, causing constipation and faecal incontinence, while a clival tumour near the brainstem can impair swallowing."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Skull-base tumours threaten the pituitary: clival chordomas sit beside the sella and can compress the pituitary, and surgery or radiation to the region can cause hypopituitarism."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A locally relentless tumour breeds worry: the high recurrence rate, repeated surgery and proton radiation, and slow inexorable course of chordoma foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Sacral tumours wreck pelvic nerve control: a sacral chordoma and its resection damage the sacral nerve roots, causing neurogenic bladder and bowel dysfunction and incontinence."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Skull-base tumours wrap the great arteries: clival chordoma encases the carotid and vertebral arteries, making resection hazardous and risking stroke from vessel injury."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Late disease reaches the lungs: although chordoma is mainly locally destructive, advanced tumours can metastasise to the lungs over their slow, relentless course."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Sacral tumours reach the skin: a large sacrococcygeal chordoma can bulge beneath and ulcerate the overlying skin, and its extensive resection leaves difficult wounds to heal."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It can spread to nodes late: though chordoma chiefly recurs locally, advanced disease occasionally metastasises to lymph nodes as well as lung and bone."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Skull-base surgery risks meningitis: resecting a clival chordoma can cause a cerebrospinal-fluid leak, opening a route for bacterial meningitis from organisms such as Streptococcus pneumoniae."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Kinase inhibitors when surgery fails: chordoma expresses PDGFR and EGFR, so imatinib and EGFR inhibitors are used for advanced disease that has exhausted surgery and radiation."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "A fellow rare tumour of the skull base: like parameningeal rhabdomyosarcoma, chordoma arises near the cranial base and brainstem, demanding complex resection and high-dose particle radiation."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It eats through the axial skeleton: chordoma destroys the cortical bone of the clivus, spine and sacrum as it grows, the bone destruction driving its pain and instability."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "It defies conventional chemo: chordoma is largely resistant to cytotoxic chemotherapy, so treatment rests on en-bloc surgery and high-dose proton-beam radiation rather than the drugs that work in other sarcomas."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy is being tested: chordomas often express PD-L1 and the notochordal antigen brachyury, prompting trials of checkpoint inhibitors and brachyury-targeted vaccines in this hard-to-treat tumour."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "It crushes the neural axis: growing at the clivus or sacrum, chordoma compresses the brainstem, cranial nerves and spinal cord, and the resulting axonal injury produces its cranial neuropathies and myelopathy."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Where it spreads: although slow-growing, chordoma metastasises late—most often to the lungs—seeding the alveolar capillary bed."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "A shared SMARCB1 loss: poorly-differentiated chordoma loses the SMARCB1/INI1 tumour suppressor, the same lesion that defines rhabdoid tumours and SMARCB1-related schwannomatosis."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Late liver metastasis: advanced chordoma can spread beyond bone to the liver, seeding the hepatic lobule among its distant metastatic sites."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "SMARCB1 loss links them: poorly differentiated chordoma loses SMARCB1, the same chromatin-remodeller deficiency that defines renal medullary carcinoma and AT/RT—a family of SMARCB1-deficient cancers."
  - target: 01-human/07-system/ovarian-clear-cell-carcinoma
    relation: connects-to
    note: "Chromatin-remodeller cancers: chordoma's SMARCB1 loss and ovarian clear cell carcinoma's ARID1A loss both disable the SWI/SNF complex, different subunits crippling the same machine."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Brachyury beyond the notochord: the TBXT/brachyury transcription factor defining chordoma is reactivated in carcinomas like NSCLC to drive epithelial-mesenchymal transition and treatment resistance."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic vulnerability: poorly differentiated, SMARCB1-deleted chordomas become dependent on EZH2, making this histone methyltransferase a rational drug target as in other rhabdoid tumours."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "KIT and imatinib: chordomas frequently express KIT (CD117) alongside PDGFR, the rationale behind imatinib therapy that gives modest disease control in advanced chordoma."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomere maintenance: TERT activation helps chordoma cells sustain replicative immortality, a shared hallmark with other slow-growing but relentless bone and soft-tissue tumours."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic skull-base niche: HIF-1α stabilised in the poorly vascularised chordoma promotes the VEGF angiogenesis and metabolic adaptation that sustain its slow but relentless growth."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Proliferative drive: MYC activation, downstream of growth-factor receptor signalling, contributes to the biosynthesis and proliferation of chordoma cells."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle progression: with CDKN2A loss common in chordoma, cyclin D1-CDK4/6 activity drives cells through the G1 checkpoint, a rationale for CDK4/6 inhibition."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Osteolytic bone invasion: chordoma destroys the clival and sacral bone it arises in by driving RANKL-mediated osteoclast activation, a key mechanism of its locally aggressive growth."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "IGF-1R signalling: insulin-like growth factor signalling is active in chordoma and supports its survival and proliferation, a studied therapeutic target alongside its brachyury dependence."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the chordoma stroma, shaping the immunosuppressive niche of this slow-growing but treatment-resistant tumour."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Invasion and spread: the CXCL12-CXCR4 axis drives the local bone and soft-tissue invasion of chordoma and contributes to the late metastases that arise in a minority of these axial-skeleton tumours."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Notochordal programme: Notch signalling is active in chordoma and, with the master regulator brachyury, sustains the notochordal stem-like phenotype that defines this tumour of embryonic-notochord remnants."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Radioresistance: chordoma resists caspase-3-mediated apoptosis, a key reason it is notoriously radioresistant and requires the high doses delivered by proton or carbon-ion therapy for local control."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Brachyury immunotherapy: because brachyury (TBXT) is the lineage-defining oncogenic dependency of chordoma, brachyury-targeted cancer vaccines aim to direct cytotoxic T cells to kill tumour cells through perforin and granzyme, an immunotherapeutic strategy unique to this tumour."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Notochordal development: brachyury sits within the Wnt/β-catenin developmental programme that builds the notochord, the embryonic structure whose persistent remnants give rise to chordoma along the axial skeleton."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Myxoid stroma: TGF-β drives the production of the abundant myxoid, chondroid extracellular matrix that gives chordoma its characteristic gelatinous histology and supports the physaliphorous tumour cells embedded within it."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK convergence: the receptor kinases driving chordoma — EGFR, MET, PDGFR, KIT and FGFR (all already mapped) — funnel into the MAPK-ERK cascade, the proliferative hub targeted by the multi-kinase inhibitors used in this tumour."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K initiation: PIK3CA activates the AKT-mTOR axis (AKT, mTOR and PTEN already mapped) that is co-activated downstream of chordoma's receptor tyrosine kinases to sustain growth and survival."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle output: RB phosphorylation by the CDK4/6-cyclin-D1 axis (mapped, with CDKN2A loss) releases E2F1 to drive S-phase entry in the slow-growing but relentless proliferation of chordoma."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Checkpoint loss: functional loss of the RB1 checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) removes a brake on cell-cycle entry, contributing to the dysregulated proliferation of chordoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 survival signalling: JAK-STAT signalling to STAT3 (already mapped) sustains the survival and proliferative programmes of chordoma cells downstream of receptor-tyrosine-kinase and cytokine inputs."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis resistance: anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the treatment resistance of the slow-growing but locally aggressive chordoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is expressed in the physaliphorous tumour cells of chordoma and contributes to its survival and matrix interactions."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) modulates the matrix-rich, slowly proliferating phenotype of chordoma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment relevant to emerging immunotherapy in chordoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of chordoma, relevant to its emerging checkpoint immunotherapy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the metabolic and oxidative stress of the slow-growing notochordal tumour cells of chordoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling modulates the brachyury (TBXT) and Wnt activity (both mapped) that drive the notochordal phenotype of chordoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling downstream of the receptor tyrosine kinases (EGFR, MET, and PDGFR already mapped) drives the invasive and survival signaling of chordoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in chordoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory microenvironment of chordoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the brachyury-driven program of chordoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of the notochordal-derived cells of chordoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling (SMARCB1 already mapped) is disrupted in the poorly differentiated variants of chordoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of chordoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of chordoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory tumor-microenvironment and survival signaling of chordoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of chordoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of chordoma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of chordoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of chordoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of chordoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the bone-invasion and tumor-microenvironment interactions of chordoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Brachyury immunotherapy: brachyury (TBXT already mapped) is a chordoma-defining shared tumour antigen, and brachyury-targeting vaccines and T-cell therapies depend on MHC-restricted antigen presentation, a distinctive immune strategy for this otherwise chemoresistant tumour."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint blockade: chordomas can express PD-L1, and checkpoint inhibitors are under investigation to unleash T-cell attack on a tumour that resists conventional systemic therapy."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cellular immunotherapy: IL-2-driven T-cell expansion supports the adoptive and vaccine-primed T-cell approaches (perforin already mapped) being explored against chordoma's brachyury antigen."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Vaccine T-cell help: helper T cells provide the CD4 help needed for durable CD8 responses (already mapped) against the brachyury antigen, the basis of the therapeutic cancer vaccines tested in chordoma."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: the anti-inflammatory cytokine IL-10 in the chordoma microenvironment blunts anti-tumour immunity, part of the immune evasion that limits the checkpoint and vaccine approaches (PD-1 already mapped)."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide regulates the vascular tone and, with VEGF (already mapped), the angiogenesis supplying the slow-growing chordoma, a mediator of the tumour microenvironment beyond the growth-factor drivers."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Osteolytic inflammation: prostaglandins from the tumour and its bone-resorptive microenvironment (RANKL already mapped) promote the osteolysis and inflammation of the bone (already mapped) destruction that drives much of chordoma's local morbidity."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative microenvironment: the slow-growing chordoma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of the tumour microenvironment beyond the growth-factor (already mapped) drivers."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in chordoma, part of the immune evasion that limits the checkpoint and vaccine approaches against this tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of chordoma."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy: conventional and stereotactic photon radiotherapy treats chordoma where proton therapy (already mapped) is unavailable, though the dose is limited by the nearby brainstem and spinal cord."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Tumour-bone interface: the osteoblasts and the bone remodelling (RANKL and osteopontin already mapped) at the interface with the destructive axial chordoma respond to the tumour invading the skull base and sacrum."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Matrix cross-linking: copper is the cofactor of lysyl oxidase that cross-links the collagen (already mapped) of the myxoid/chondroid matrix of chordoma, and supports the copper-dependent angiogenesis (VEGF already mapped)."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Matrix metalloproteinases: the zinc-dependent matrix metalloproteinases remodel the extracellular matrix (collagen already mapped) at the invasive front of chordoma into the skull base and sacrum."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow-bone adipokine: leptin from the marrow adipose tissue of the bone (RANKL and osteoblast already mapped) microenvironment signals to the axial chordoma, part of its bone-niche metabolic crosstalk."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-bone adipokine: adiponectin, with leptin (already mapped), is part of the marrow-adipose (RANKL already mapped) bone-niche adipokine crosstalk of the axial chordoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the bone-niche adipokine crosstalk of chordoma."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Prognostic neutrophils: the tumour-infiltrating neutrophils and the neutrophil-lymphocyte ratio are prognostic markers in chordoma, part of its inflammatory microenvironment (CCL2 already mapped)."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the checkpoint (PD-1 already mapped) immunotherapy and brachyury (TBXT already mapped) vaccine of chordoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of chordoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of chordoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of chordoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the chordoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of chordoma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the myxoid immune microenvironment of chordoma."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the brachyury and other tumour antigens (MHC already mapped) to the T cells (already mapped), a rationale for the brachyury-vaccine immunotherapy of chordoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the chordoma stroma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the chordoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the chordoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the slow-growing notochordal (brachyury/TBXT already mapped) tumour cells of chordoma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-TME axis: TSLP, from notochordal stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppression of the chordoma tumour microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-tumour axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability and the inflammatory milieu of the chordoma microenvironment."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Tumour-EPO axis: erythropoietin, via the EPOR on chordoma tumour cells (already mapped), modulates the survival, proliferation, and the angiogenic (already mapped) dimension of this aggressive sacral/skull-base tumour."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell chordoma axis: histamine, from mast cells (already mapped) in the notochordal tumour microenvironment, amplifies the vascular permeability, the angiogenesis (already mapped) and the immunosuppressive milieu of chordoma."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-notochordal axis: melatonin, via MT1/MT2 receptors and its radical-scavenging activity, modulates the oxidative stress of the brachyury/TBXT-driven (already mapped) slow proliferation and angiogenic dimension of chordoma."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation can contribute to the inflammatory milieu and the immune evasion of the chordoma microenvironment."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Chordoma testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the TME; testosterone deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) cascade of chordoma."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Chordoma serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the chordoma TME; serotonin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of chordoma."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Chordoma prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the chordoma immune TME; hyperprolactinaemia amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of chordoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Chordoma oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the tumour-promoting inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of chordoma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Chordoma vasopressin: vasopressin, via V1aR on mast cells (already mapped) and macrophages (already mapped), modulates the tumour vascular milieu; vasopressin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of chordoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Chordoma selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) oxidative TME cascade of chordoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Chordoma iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) surveillance; iodine deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of chordoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Chordoma magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting signalling cascade of chordoma."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Chordoma phosphorus: phosphorus, as ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped), fuels proliferative and cytotoxic signalling; phosphorus dysregulation amplifies the IL-6 (already mapped) and mast-cell (already mapped) TME of chordoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "sodium homeostasis in macrophage (already mapped) and fibroblast (already mapped) regulates tumour ionic microenvironment; sodium dysregulation amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in chordoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "potassium channels on T-cytotoxic cell (already mapped) and macrophage (already mapped) regulate anti-tumour immunity; potassium dysregulation amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in chordoma."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "iron in macrophage (already mapped) and fibroblast (already mapped) fuels oxidative tumour microenvironment; iron excess amplifies mTOR (already mapped) and P53 (already mapped) and VEGF (already mapped) cascade in chordoma."
---

# Chordoma

## Overview

**Chordoma** is a rare, locally aggressive, low-to-intermediate grade malignant tumor arising from notochordal remnants that persist in the axial skeleton. Despite a typically slow growth rate, chordoma is associated with high rates of local recurrence, late metastases, and significant morbidity from its location adjacent to critical neural structures. TBXT (brachyury), expressed in >95% of chordomas, defines tumor identity and is the diagnostic hallmark [^yang-2009-tbxt-chordoma].

**Epidemiology:**
- Incidence: ~1-2 per million/year; ~300-400 cases/year USA; one of the rarest primary bone tumors
- Peak age: 50-60 years (skull base ~40-50 years; sacral ~55-65 years); male predominance ~1.8:1
- Median OS: skull base ~10-14 years; sacral ~7-10 years; mobile spine ~6-8 years
- Metastases at diagnosis: ~5-10%; eventual metastases in ~30-40% of patients over the disease course; lung (most common), bone, lymph node, liver

**Sites and locations:**

| Location | Frequency | Key features |
|---|---|---|
| Sacrococcygeal | ~50% | Largest at presentation (often >10 cm); late symptoms; S3/S4 roots → bowel/bladder; en bloc sacrectomy |
| Skull base (clivus) | ~35% | Cranial nerve palsies (VI most common); encases basilar artery; radical resection difficult; endoscopic endonasal approach |
| Mobile spine (C/T/L) | ~15% | Cervical > lumbar; cord compression; multilevel resection; highest local recurrence |

**Familial chordoma:** ~5% of patients have a family history; tandem germline TBXT duplication at 6q27 is the most common predisposing variant [^yang-2009-tbxt-chordoma]; other predisposing conditions include tuberous sclerosis complex (TSC1/TSC2 germline) and rarely NF2 syndrome

## Structure

### Histological subtypes

**Conventional (classic) chordoma (~85%):**
- **Physaliferous cells** ("bubble-bearing" cells): large vacuolated cells with intracytoplasmic mucin inclusions pushing the nucleus to one side; cytoplasm has "soap bubble" appearance on H&E
- Mucoid/myxoid stroma (chondromucin)
- Lobular architecture separated by fibrous septa
- Low mitotic rate (<2/10 HPF); necrosis absent in most cases

**Chondroid chordoma (~5-10%):**
- Mixed chordoma + hyaline cartilage; predominantly skull base
- Better prognosis than conventional; lower rate of metastasis
- Must be distinguished from chondrosarcoma (chondrosarcoma is TBXT-negative)

**Dedifferentiated chordoma (~5%):**
- Biphasic: classic chordoma + high-grade sarcomatous component
- Abrupt junction between components
- CDK4 amplification, MDM2 amplification common in dedifferentiated component
- 5-year OS ~10-15%; aggressive systemic metastases; worst prognosis variant

**Poorly differentiated chordoma:**
- SMARCB1/INI1 loss in ~75% (biallelic loss, distinct from conventional); primarily pediatric; skull base; rhabdoid morphology; treated similarly to AT/RT

### IHC panel

- **TBXT (brachyury)**: strong nuclear positivity — pathognomonic; ~95-100% of conventional chordoma; negative in chondrosarcoma, meningeal tumors, and carcinoma
- **S100**: positive in ~95% of chordoma; nuclear and cytoplasmic
- **Cytokeratin (AE1/AE3, CAM5.2)**: positive in ~85%; differentiates from chondrosarcoma (CK-negative)
- **EMA**: positive in ~60-70%
- **GFAP**: positive in ~25-35%; notochordal origin
- **SOX9**: positive in most chordomas
- **SMARCB1/INI1**: intact in conventional; LOST in poorly differentiated chordoma variant

## Function

### Notochordal biology and chordoma origin

The notochord is a transient axial structure in all chordate embryos; in humans:
- Forms during gastrulation (week 3); provides mechanical support and signaling
- Regresses completely by week 8-12 as vertebral bodies form
- Notochordal remnants (benign notochordal cell tumors, BNCTs) persist in nucleus pulposus (intervertebral discs) and occasionally in vertebral bodies (ecchordosis physaliphora)
- BNCT: asymptomatic incidental finding; TBXT-positive but no somatic mutations or atypia; may be the precursor lesion for chordoma

**Chordoma oncogenesis:** TBXT-overexpressing notochordal cells escape senescence (via CDK4/cyclin D1, anti-apoptotic BCL-2) → acquire somatic mutations in CDKN2A (~30-40% deletion), PIK3CA, TP53, PTEN, ATRX → invasive chordoma; the transformation from BNCT to chordoma may take decades

**Typical somatic alterations in chordoma:**
- CDKN2A homozygous deletion: ~30-40%; worst prognosis; CDK4/6 hyperactivation
- PIK3CA mutations: ~15-20%; mTOR pathway activation
- PTEN loss: ~15%; AKT/mTOR
- ATRX mutations: ~15%; alternative lengthening of telomeres
- TP53 mutations: ~5-10%; usually late event
- LYST, SETD2, BRCA2: rare; identified in chordoma genome sequencing
- Chromosome arm losses: 1p, 3p, 4, 9p (CDKN2A), 10 (PTEN), 13q (RB1) common

## Pathology

### Surgical management

**Skull base chordoma:**
- Endoscopic endonasal approach (EEA): minimally invasive, direct clival access; standard for midline/paramedian clivus lesions; combined with neurosurgery team
- Craniotomy: lateral tumors, extensive lateral extension, cavernous sinus involvement
- Extent of resection: GTR correlated with better PFS (5-year local control ~60-70% with GTR + proton)
- Critical structures: basilar artery, CN VI (most commonly affected), CN III, carotid siphon, brainstem; incomplete resection for safety → adjuvant proton beam

**Sacral chordoma:**
- En bloc resection: wide margins essential; preserve S1-S2 (bilateral) for ambulatory function and S2-S3 (bilateral) for bladder/bowel continence; sacrifice below S3 acceptable with continent function
- High sacral (S1-S2) tumors: combined anterior (laparoscopic) + posterior approach; major morbidity
- Recurrence rate: ~50-60% at 5 years even after R0 resection; proton boost reduces recurrence
- Lumbopelvic stability: instrumented fusion required if sacroiliac joint disrupted

**Mobile spine chordoma:**
- Cervical: highest rate of incomplete resection due to vertebral artery, esophagus, trachea
- Thoracic/lumbar: en bloc spondylectomy (total vertebrectomy) with reconstruction; spinal cord monitoring
- Circumferential resection: requires anterior + posterior staged approach or single-stage

### Radiation therapy

**Proton beam radiotherapy (PBRT) / Carbon ion radiotherapy (CIRT):**
- Superior to photon RT due to sharp Bragg peak → maximal dose at tumor with minimal exit dose
- Skull base standard: 74-78 Gy (RBE) in 35-40 fractions; local control at 5 years: ~70-75%
- Sacral: 70-77.4 Gy (RBE) combined with surgery; local control 5-year: ~55-65%
- CIRT (carbon ion): available in Japan and Germany; superior biological effectiveness → may achieve ~80% local control in skull base; head-to-head vs proton ongoing

### Systemic therapy (no FDA-approved agent exists)

**Imatinib (PDGFR/KIT/ABL inhibitor):** [^stacchiotti-2012-imatinib-chordoma]
Phase 2 (Stacchiotti 2012, N=50): ORR 0% (partial response in 0), stable disease 70% (35/50); median PFS 9.9 months; PDGFRA/B expression predicts stable disease; used as standard-of-care systemic option for progressive chordoma despite no objective responses

**Sorafenib (multikinase: VEGFR/PDGFR/BRAF/RAF):**
Phase 2 (Bompas 2015, N=27): ORR 7% (2/27 PR), SD 70%; PFS 5.8 months; modest activity; toxicity includes hand-foot syndrome

**Erlotinib + imatinib:**
Phase 2 (Stacchiotti 2013): ORR 10% (PR); combination tolerated; activity mainly stable disease; EGFR overexpressed in ~75% of chordoma cells

**mTOR inhibitors (everolimus, rapamycin):**
Rationale: PTEN loss/PI3K/AKT hyperactivation → mTOR; everolimus Phase 2 (Schwab 2015): SD in ~50%, no objective responses; lapatinib + everolimus Phase 2: similar results; rapamycin retrospective series: SD in recurrent disease; combination with FGFR inhibitors preferred investigational approach

**Pembrolizumab/nivolumab:**
Low TMB (~1-2 mut/Mb); PD-L1 expressed in ~20-30%; anti-PD-1 ORR ~10-15% in case series; chordoma TME is immune-cold; combination with radiation (immune priming) under investigation

**Palbociclib (CDK4/6 inhibitor):**
CDKN2A deletion in ~30-40% → CDK4/6 hyperactivation → RB1 phosphorylation; palbociclib Phase 2 in CDKN2A-deleted chordoma (NCT03110744): ongoing; rationale strong for CDK4/6-deleted subset

**Prognosis:**
- 5-year OS: skull base ~70-80%; sacral ~65-75%; mobile spine ~55-65%; dedifferentiated ~10-15%
- 10-year OS: skull base ~45-60%; sacral ~40-55%
- Local recurrence: major cause of morbidity and mortality; most patients undergo multiple surgeries
- Late metastases (>5 years from diagnosis): ~25-30%; lung most common; may respond temporarily to imatinib or sorafenib

## Connections

- `connects-to` → **[TBXT](../../03-molecular/tbxt/README.md)** — TBXT (brachyury) overexpression in >95% chordomas defines lineage identity; tandem TBXT duplication at 6q27 → familial chordoma; TBXT FISH or IHC (strong nuclear brachyury) is the diagnostic confirmatory test; TBXT knockdown → chordoma cell growth arrest and apoptosis in vitro.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PTEN loss in ~15-20% chordomas → AKT/mTOR hyperactivation; mTOR pathway activated downstream of FGFR/PDGFR in chordoma; everolimus achieves stable disease in ~50% (Schwab 2015, Phase 2); mTOR + FGFR combinations under investigation; lapatinib + everolimus Phase 2 showed activity.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR1/2/3 overexpressed in ~50% chordomas; FGFR-driven MAPK/PI3K → tumor growth; erdafitinib (pan-FGFR) active in FGFR-altered chordoma (Phase 2); FGF4/FGF8 autocrine loop driven by TBXT transcription; FGFR inhibitors synergize with mTOR inhibitors in preclinical models.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGFRA/PDGFRB overexpressed in >80% chordomas; imatinib (PDGFR inhibitor) achieves stable disease in ~35-40% (Stacchiotti 2012, Phase 2); PDGF-BB autocrine loop in chordoma cells; erlotinib + imatinib combination achieves partial response in small Phase 2 series.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss in ~15-20% chordomas → AKT-mTOR hyperactivation + increased VEGF; PI3K inhibitors studied in PTEN-deficient chordoma; PTEN co-deletion with CDKN2A in ~8-10% → simultaneous CDK4/6 and mTOR hyperactivation; PTEN loss correlates with worse prognosis in chordoma.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDKN2A deletion in ~30-40% of chordomas → CDK4/6 hyperactivation → RB1 phosphorylation → S-phase entry; palbociclib Phase 2 (NCT03110744) in CDKN2A-deleted chordoma; dedifferentiated chordoma shows CDK4 amplification and MDM2 co-amplification as hallmarks.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A homozygous deletion in ~30-40% chordomas; eliminates both p16 (CDK4/6 checkpoint) and ARF (p53 stabilization); deletion at 9p21 is among the earliest molecular events in chordoma progression; CDKN2A loss correlates with worse prognosis and dedifferentiated transformation.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Chordoma and Ewing sarcoma are both rare bone tumors with one defining genetic lesion — chordoma's TBXT/brachyury overexpression versus Ewing's EWSR1-FLI1 fusion — but chordoma is a slow midline tumor of adults from notochord remnants, Ewing a small-cell tumor of children.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Chordoma arises along the axial skeleton from embryonic notochord remnants — ~50% sacrum, ~35% skull base (clivus), the rest mobile spine; this midline bony location, often diagnosed late and abutting critical structures, makes en-bloc resection the mainstay yet often incomplete.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Skull-base (clival) chordomas grow against the brainstem, cavernous sinus, and cranial nerves, causing diplopia, headache, and cranial-nerve palsies; their proximity to brain and vessels limits margins, making proton-beam radiotherapy central to controlling residual tumor.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Chordoma is defined by its radiotherapy needs: nestled against the brainstem and cord at the skull base and sacrum, it needs very high radiation doses that proton-beam therapy delivers while sparing neural tissue—central since complete resection is often impossible.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Chordoma and osteosarcoma are both primary bone malignancies but differ fundamentally: chordoma is a slow-growing notochord-remnant tumor of the axial skeleton (skull base/sacrum) driven by brachyury, while osteosarcoma is an aggressive osteoid-producing tumor of long bones.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Chordoma's relationship to bone-forming cells is distinctive: although it grows within and destroys bone, it does not arise from osteoblasts but from notochord remnants, producing a lytic, gelatinous mass rather than the bone matrix osteoblasts lay down—imaging shows destruction.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Chordoma and meningioma are both slow-growing skull-base/spinal tumors in the same differential: chordoma is a destructive midline tumor of notochord remnants, while meningioma is a dural-based extra-axial tumor—told apart by location, imaging, and immunostains.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Chordoma's characteristic histology is a myxoid, fibroblast-like stroma studded with physaliphorous (bubbly) cells: the matrix and spindle-cell background give a deceptively bland, cartilage-like look, so brachyury immunostaining confirms its notochordal origin.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Chordoma and synovial sarcoma are rare tumors of young adults with aggressive local behavior needing wide resection plus radiotherapy: chordoma is brachyury-driven from notochord remnants, synovial sarcoma SS18-SSX-fusion-driven—different drivers, similar challenge.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR is a therapeutic target in chordoma: these slow-growing notochordal tumors often activate EGFR signaling, so EGFR inhibitors like erlotinib are used off-label in advanced disease where surgery and radiation fail—chordoma resists conventional chemotherapy.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Chordoma threatens neurons by location: arising along the spine and skull base from notochord remnants, it compresses the brainstem, spinal cord and cranial nerves, so neurological deficits—not metastasis—drive its morbidity despite slow growth.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Chordoma's hallmark cells sit in a collagen-rich matrix: physaliphorous bubble cells float in a myxoid, collagenous stroma recapitulating the notochord, giving the tumor its distinctive histology that, with brachyury staining, confirms the diagnosis.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy is the radiation mainstay for chordoma: these radioresistant skull-base and sacral tumors sit against the brainstem and spinal cord, so protons' sharp dose falloff delivers high tumor dose while sparing critical neural structures.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Chordoma threatens the nervous system by location: arising along the spine and skull base from notochord remnants, it compresses the brainstem, cranial nerves and spinal cord, so its slow growth still causes severe neurological deficits and demands aggressive local control.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-ion radiotherapy is an alternative for chordoma: heavy carbon ions deliver dense, highly damaging dose to these notoriously radioresistant tumors, useful when surgery is incomplete or the tumor abuts neural structures—an option in specialized particle centers.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Chordoma spreads most often to the lung: though it grows slowly and locally along the spine and skull base, late metastasis favors the lungs, so chest imaging is part of follow-up for this notochord-derived bone tumor.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Chordoma is a target for vaccine immunotherapy: nearly all chordomas express brachyury (TBXT), and a brachyury-directed cancer vaccine trains the immune system against this otherwise hard-to-drug developmental transcription factor.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Chordoma's radioresistance is partly an oxygen problem: poorly oxygenated tumor regions resist conventional X-rays, so high-dose proton and carbon-ion radiotherapy—less dependent on oxygen and more precise near the spinal cord—are used instead.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Chordoma destroys bone through osteoclasts: as it grows in the skull base or sacrum it recruits bone-resorbing osteoclasts that erode the surrounding skeleton, so anti-resorptive drugs are explored to slow the local destruction this hard-to-resect tumor causes.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Chordoma is a vascular tumor that responds to anti-VEGF therapy: it expresses VEGF to grow blood vessels, which is why multi-target TKIs that block VEGF receptors (like sunitinib) can stall this otherwise treatment-resistant cancer.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Losing p53 makes chordoma more aggressive: while most chordomas grow slowly on brachyury, TP53 mutation marks the dangerous shift toward dedifferentiated, fast-growing tumors with a far worse prognosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Chordoma leans on the PI3K-AKT-mTOR growth axis: AKT signaling is frequently active and, with PTEN loss, drives proliferation in these brachyury-dependent tumors, so AKT-mTOR inhibitors are studied for a cancer resistant to chemotherapy.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — MET signaling can drive aggressive chordoma: amplification or activation of this receptor promotes invasion and growth, adding to the brachyury-driven biology and offering another targetable kinase in a notoriously treatment-resistant bone tumor.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Chordoma is a target for T-cell immunotherapy against brachyury: because the tumor depends on this lineage antigen, vaccines and engineered cytotoxic T cells aim to direct a killing response at a protein cancer cells cannot easily discard.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Chordoma eats away calcium-rich bone: arising in the skull base and sacrum, it destroys the bony matrix as it grows, dissolving the calcium scaffold and threatening the spine and cranial nerves it surrounds.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Chordoma shelters in a macrophage-rich stroma: tumor-associated macrophages populate its microenvironment and dampen immunity, part of why this slow but stubborn tumor resists treatment and recurs.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Sacral chordoma presses on the bowel: the most common chordoma site sits against the rectum and pelvic nerves, so large tumors cause constipation, bowel and bladder dysfunction, and low back pain.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Chordoma grows against the nerves: skull-base and sacral tumors compress cranial nerves and the cauda equina, causing the neuropathic pain, weakness and bowel-bladder dysfunction that often first signal it.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Chordoma metastasizes late: though slow-growing and locally destructive, it can seed the lungs, liver and bone over years, especially after repeated local recurrences.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Chordoma builds its own vasculature: VEGF recruits endothelial cells to feed the tumor, and anti-angiogenic drugs are among the systemic options for this radiation- and surgery-dependent cancer.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy names the chordoma cell: the physaliphorous ('bubble-bearing') cell, its cytoplasm ballooning with glycogen and mucin-filled vacuoles, betrays the tumor's origin in leftover notochord tissue.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Chordoma is born in bone: it grows from notochord remnants in the marrow-bearing vertebrae of the sacrum and skull base, destroying the bone it arises in and occasionally seeding distant skeletal metastases.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — A skull-base chordoma blurs and crosses the vision: growing at the clivus it compresses the cranial nerves that move the eyes, causing double vision and gaze palsies that often first bring the patient in.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody marks and may treat the notochordal tumor: the brachyury (TBXT) protein, detected by immunostaining, is the diagnostic hallmark of chordoma, and a brachyury cancer vaccine is in trials to rouse immunity against it.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — A sacral chordoma strikes at the body's lower controls: growing in the sacrum it compresses the nerve roots governing erection, ejaculation, and continence, so sexual and pelvic dysfunction can be early or surgical consequences.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The sacral tumor disconnects the pelvic smooth muscle: damage to the sacral roots from the chordoma or its removal leaves the bladder and bowel smooth muscle without control, causing retention, incontinence, and constipation.
- `connects-to` → **[Tuberous Sclerosis Complex](../tuberous-sclerosis-complex/README.md)** — Chordoma turns up in tuberous sclerosis: pediatric chordomas are reported in TSC patients, a link that fits chordoma's reliance on PI3K-AKT-mTOR signaling — the same pathway that TSC1/TSC2 loss unleashes — and points to mTOR inhibitors as therapy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Chordoma is an immunologically cold tumor: it expresses PD-L1 and recruits regulatory T cells that suppress local immunity, a microenvironment that helps it evade attack and is the rationale for testing checkpoint blockade in this radioresistant cancer.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Chordoma is treated with hydrogen nuclei: proton-beam radiation — accelerated bare hydrogen nuclei — deposits its dose at a sharp Bragg peak, letting high doses hit clival and sacral tumors while sparing the brainstem and spinal cord just millimeters away.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — A rare aggressive variant loses SMARCB1: poorly-differentiated chordoma deletes this chromatin-remodeling gene, the same loss that defines rhabdoid tumors, marking a more lethal subtype that strikes the young.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — SMARCB1 loss links them across tissues: poorly-differentiated chordoma and ATRT share deletion of the same chromatin-remodeling gene, an epigenetic lesion that ties a notochordal bone tumor to a brain rhabdoid tumor.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Immunotherapy aims past the cold tumor: brachyury-targeted vaccines and natural-killer-cell-engaging approaches are being tested to attack chordoma, whose poor blood supply and immune evasion resist conventional treatment.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Hippo-YAP signaling feeds the notochordal tumor: YAP1 activity cooperates with brachyury to sustain chordoma cell proliferation and survival, marking the Hippo pathway as a candidate target in a cancer with few effective drugs.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Chordoma hurts by crushing nerves: as it grows in the sacrum or clivus it compresses nerve roots and the spinal cord, causing the radicular and neuropathic pain that is often its first symptom.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — A destructive axial bone lesion poses a differential: a lytic sacral or vertebral mass on imaging must be told apart from myeloma and metastasis, since chordoma's notochordal origin and brachyury staining set it apart and change treatment.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 supports the slow-growing tumor: chordoma cells show STAT3 activation downstream of receptor signaling that backs their survival, one of the pathways explored where this radioresistant tumor needs systemic options.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Major axial surgery clots the veins: the long sacral and skull-base resections chordoma requires, with prolonged immobility afterward, make deep-vein thrombosis and pulmonary embolism a real perioperative risk.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Deep resections invite infection: extensive sacral and clival surgery, sometimes with CSF leak, can be complicated by deep wound infection and meningitis that progress to sepsis.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — It destroys bone and its radiation weakens more: chordoma erodes the sacrum and clivus directly, while the high-dose proton/photon radiation used to control it causes osteoradionecrosis and insufficiency fractures.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Relentless pain and a poor cure weigh on mood: chronic neuropathic pain, disfiguring skull-base surgery, bowel-bladder dysfunction and high recurrence give chordoma a substantial psychological burden.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Advanced disease blunts the marrow: locally aggressive or metastatic chordoma with its inflammatory burden, compounded by major surgery and radiation, can produce an anemia of chronic disease.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its radical resections heal poorly: the extensive skull-base and sacral surgery for chordoma, often with prior or adjuvant radiation, leaves complex wounds prone to dehiscence, CSF leak and slow healing.
- `connects-to` → **[Stroke](../stroke/README.md)** — Skull-base tumor encircles the great vessels: clival chordomas encase the carotid and basilar arteries, and tumor or its surgery can compromise these vessels, risking ischemic stroke.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Sacral tumor disrupts the bladder: a sacral chordoma damages the nerves controlling the bladder, and the resulting neurogenic bladder with recurrent infection and obstruction can injure the kidneys over time.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It compresses the gut from both ends: a sacral chordoma damages the nerves to the rectum, causing constipation and faecal incontinence, while a clival tumour near the brainstem can impair swallowing.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Skull-base tumours threaten the pituitary: clival chordomas sit beside the sella and can compress the pituitary, and surgery or radiation to the region can cause hypopituitarism.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A locally relentless tumour breeds worry: the high recurrence rate, repeated surgery and proton radiation, and slow inexorable course of chordoma foster chronic health anxiety alongside depression.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Sacral tumours wreck pelvic nerve control: a sacral chordoma and its resection damage the sacral nerve roots, causing neurogenic bladder and bowel dysfunction and incontinence.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Skull-base tumours wrap the great arteries: clival chordoma encases the carotid and vertebral arteries, making resection hazardous and risking stroke from vessel injury.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Late disease reaches the lungs: although chordoma is mainly locally destructive, advanced tumours can metastasise to the lungs over their slow, relentless course.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Sacral tumours reach the skin: a large sacrococcygeal chordoma can bulge beneath and ulcerate the overlying skin, and its extensive resection leaves difficult wounds to heal.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It can spread to nodes late: though chordoma chiefly recurs locally, advanced disease occasionally metastasises to lymph nodes as well as lung and bone.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Skull-base surgery risks meningitis: resecting a clival chordoma can cause a cerebrospinal-fluid leak, opening a route for bacterial meningitis from organisms such as Streptococcus pneumoniae.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Kinase inhibitors when surgery fails: chordoma expresses PDGFR and EGFR, so imatinib and EGFR inhibitors are used for advanced disease that has exhausted surgery and radiation.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — A fellow rare tumour of the skull base: like parameningeal rhabdomyosarcoma, chordoma arises near the cranial base and brainstem, demanding complex resection and high-dose particle radiation.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It eats through the axial skeleton: chordoma destroys the cortical bone of the clivus, spine and sacrum as it grows, the bone destruction driving its pain and instability.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — It defies conventional chemo: chordoma is largely resistant to cytotoxic chemotherapy, so treatment rests on en-bloc surgery and high-dose proton-beam radiation rather than the drugs that work in other sarcomas.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy is being tested: chordomas often express PD-L1 and the notochordal antigen brachyury, prompting trials of checkpoint inhibitors and brachyury-targeted vaccines in this hard-to-treat tumour.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — It crushes the neural axis: growing at the clivus or sacrum, chordoma compresses the brainstem, cranial nerves and spinal cord, and the resulting axonal injury produces its cranial neuropathies and myelopathy.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Where it spreads: although slow-growing, chordoma metastasises late—most often to the lungs—seeding the alveolar capillary bed.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — A shared SMARCB1 loss: poorly-differentiated chordoma loses the SMARCB1/INI1 tumour suppressor, the same lesion that defines rhabdoid tumours and SMARCB1-related schwannomatosis.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Late liver metastasis: advanced chordoma can spread beyond bone to the liver, seeding the hepatic lobule among its distant metastatic sites.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — SMARCB1 loss links them: poorly differentiated chordoma loses SMARCB1, the same chromatin-remodeller deficiency that defines renal medullary carcinoma and AT/RT—a family of SMARCB1-deficient cancers.
- `connects-to` → **[Ovarian Clear Cell Carcinoma](../ovarian-clear-cell-carcinoma/README.md)** — Chromatin-remodeller cancers: chordoma's SMARCB1 loss and ovarian clear cell carcinoma's ARID1A loss both disable the SWI/SNF complex, different subunits crippling the same machine.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Brachyury beyond the notochord: the TBXT/brachyury transcription factor defining chordoma is reactivated in carcinomas like NSCLC to drive epithelial-mesenchymal transition and treatment resistance.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic vulnerability: poorly differentiated, SMARCB1-deleted chordomas become dependent on EZH2, making this histone methyltransferase a rational drug target as in other rhabdoid tumours.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT and imatinib: chordomas frequently express KIT (CD117) alongside PDGFR, the rationale behind imatinib therapy that gives modest disease control in advanced chordoma.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomere maintenance: TERT activation helps chordoma cells sustain replicative immortality, a shared hallmark with other slow-growing but relentless bone and soft-tissue tumours.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic skull-base niche: HIF-1α stabilised in the poorly vascularised chordoma promotes the VEGF angiogenesis and metabolic adaptation that sustain its slow but relentless growth.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Proliferative drive: MYC activation, downstream of growth-factor receptor signalling, contributes to the biosynthesis and proliferation of chordoma cells.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle progression: with CDKN2A loss common in chordoma, cyclin D1-CDK4/6 activity drives cells through the G1 checkpoint, a rationale for CDK4/6 inhibition.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Osteolytic bone invasion: chordoma destroys the clival and sacral bone it arises in by driving RANKL-mediated osteoclast activation, a key mechanism of its locally aggressive growth.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1R signalling: insulin-like growth factor signalling is active in chordoma and supports its survival and proliferation, a studied therapeutic target alongside its brachyury dependence.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the chordoma stroma, shaping the immunosuppressive niche of this slow-growing but treatment-resistant tumour.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — The CXCL12-CXCR4 axis drives the local bone and soft-tissue invasion of chordoma and contributes to the late metastases that arise in a minority of these slow-growing axial-skeleton tumors.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch signaling is active in chordoma and, with the master regulator brachyury, sustains the notochordal stem-like phenotype that defines this tumor arising from embryonic-notochord remnants.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Chordoma resists caspase-3-mediated apoptosis, a key reason it is notoriously radioresistant and requires the high doses delivered by proton or carbon-ion therapy to achieve durable local control.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Because brachyury (TBXT) is the lineage-defining oncogenic dependency of chordoma, brachyury-targeted cancer vaccines aim to direct cytotoxic T cells to kill tumor cells through perforin and granzyme, an immunotherapeutic strategy unique to this tumor.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Brachyury sits within the Wnt/β-catenin developmental program that builds the notochord, the embryonic structure whose persistent remnants give rise to chordoma along the axial skeleton.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β drives the production of the abundant myxoid, chondroid extracellular matrix that gives chordoma its characteristic gelatinous histology and supports the physaliphorous tumor cells embedded within it.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The receptor kinases driving chordoma—EGFR, MET, PDGFR, KIT and FGFR (all already mapped)—funnel into the MAPK-ERK cascade, the proliferative hub targeted by the multi-kinase inhibitors used in this tumor.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA activates the AKT-mTOR axis (AKT, mTOR and PTEN already mapped) that is co-activated downstream of chordoma's receptor tyrosine kinases to sustain growth and survival.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — RB phosphorylation by the CDK4/6-cyclin-D1 axis (mapped, with CDKN2A loss) releases E2F1 to drive S-phase entry in the slow-growing but relentless proliferation of chordoma.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Functional loss of the RB1 checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) removes a brake on cell-cycle entry, contributing to the dysregulated proliferation of chordoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT signaling to STAT3 (already mapped) sustains the survival and proliferative programs of chordoma cells downstream of receptor-tyrosine-kinase and cytokine inputs.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the treatment resistance of the slow-growing but locally aggressive chordoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is expressed in the physaliphorous tumor cells of chordoma and contributes to its survival and matrix interactions.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) modulates the matrix-rich, slowly proliferating phenotype of chordoma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment relevant to emerging immunotherapy in chordoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of chordoma, relevant to its emerging checkpoint immunotherapy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the metabolic and oxidative stress of the slow-growing notochordal tumor cells of chordoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling modulates the brachyury (TBXT) and Wnt activity (both mapped) that drive the notochordal phenotype of chordoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling downstream of the receptor tyrosine kinases (EGFR, MET, and PDGFR already mapped) drives the invasive and survival signaling of chordoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in chordoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins from infiltrating myeloid cells shape the inflammatory microenvironment of chordoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the brachyury-driven program of chordoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of the notochordal-derived cells of chordoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling (SMARCB1 already mapped) is disrupted in the poorly differentiated variants of chordoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of chordoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of chordoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory tumor-microenvironment and survival signaling of chordoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of chordoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of chordoma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of chordoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of chordoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of chordoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the bone-invasion and tumor-microenvironment interactions of chordoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Brachyury immunotherapy: brachyury (TBXT already mapped) is a chordoma-defining shared tumour antigen, and brachyury-targeting vaccines and T-cell therapies depend on MHC-restricted antigen presentation, a distinctive immune strategy for this otherwise chemoresistant tumour.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint blockade: chordomas can express PD-L1, and checkpoint inhibitors are under investigation to unleash T-cell attack on a tumour that resists conventional systemic therapy.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cellular immunotherapy: IL-2-driven T-cell expansion supports the adoptive and vaccine-primed T-cell approaches (perforin already mapped) being explored against chordoma's brachyury antigen.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Vaccine T-cell help: helper T cells provide the CD4 help needed for durable CD8 responses (already mapped) against the brachyury antigen, the basis of the therapeutic cancer vaccines tested in chordoma.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: the anti-inflammatory cytokine IL-10 in the chordoma microenvironment blunts anti-tumour immunity, part of the immune evasion that limits the checkpoint and vaccine approaches (PD-1 already mapped).
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide regulates the vascular tone and, with VEGF (already mapped), the angiogenesis supplying the slow-growing chordoma, a mediator of the tumour microenvironment beyond the growth-factor drivers.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Osteolytic inflammation: prostaglandins from the tumour and its bone-resorptive microenvironment (RANKL already mapped) promote the osteolysis and inflammation of the bone (already mapped) destruction that drives much of chordoma's local morbidity.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative microenvironment: the slow-growing chordoma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of the tumour microenvironment beyond the growth-factor (already mapped) drivers.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in chordoma, part of the immune evasion that limits the checkpoint and vaccine approaches against this tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of chordoma.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy: conventional and stereotactic photon radiotherapy treats chordoma where proton therapy (already mapped) is unavailable, though the dose is limited by the nearby brainstem and spinal cord.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Tumour-bone interface: the osteoblasts and the bone remodelling (RANKL and osteopontin already mapped) at the interface with the destructive axial chordoma respond to the tumour invading the skull base and sacrum.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Matrix cross-linking: copper is the cofactor of lysyl oxidase that cross-links the collagen (already mapped) of the myxoid/chondroid matrix of chordoma, and supports the copper-dependent angiogenesis (VEGF already mapped).
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Matrix metalloproteinases: the zinc-dependent matrix metalloproteinases remodel the extracellular matrix (collagen already mapped) at the invasive front of chordoma into the skull base and sacrum.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow-bone adipokine: leptin from the marrow adipose tissue of the bone (RANKL and osteoblast already mapped) microenvironment signals to the axial chordoma, part of its bone-niche metabolic crosstalk.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-bone adipokine: adiponectin, with leptin (already mapped), is part of the marrow-adipose (RANKL already mapped) bone-niche adipokine crosstalk of the axial chordoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the bone-niche adipokine crosstalk of chordoma.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Prognostic neutrophils: the tumour-infiltrating neutrophils and the neutrophil-lymphocyte ratio are prognostic markers in chordoma, part of its inflammatory microenvironment (CCL2 already mapped).
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the checkpoint (PD-1 already mapped) immunotherapy and brachyury (TBXT already mapped) vaccine of chordoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of chordoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of chordoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of chordoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the chordoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of chordoma.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the myxoid immune microenvironment of chordoma.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the brachyury and other tumour antigens (MHC already mapped) to the T cells (already mapped), a rationale for the brachyury-vaccine immunotherapy of chordoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the chordoma stroma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the chordoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the chordoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the tumour stroma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the slow-growing notochordal (brachyury/TBXT already mapped) tumour cells of chordoma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-TME axis: TSLP, from notochordal stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppression of the chordoma tumour microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-tumour axis: bradykinin, via B1/B2 receptors on tumour endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability and the inflammatory milieu of the chordoma microenvironment.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Tumour-EPO axis: erythropoietin, via the EPOR on chordoma tumour cells (already mapped), modulates the survival, proliferation, and the angiogenic (already mapped) dimension of this aggressive sacral/skull-base tumour.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell chordoma axis: histamine, from mast cells (already mapped) in the notochordal tumour microenvironment, amplifies the vascular permeability, the angiogenesis (already mapped) and the immunosuppressive milieu of chordoma.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-notochordal axis: melatonin, via MT1/MT2 receptors and its radical-scavenging activity, modulates the oxidative stress of the brachyury/TBXT-driven (already mapped) slow proliferation and angiogenic dimension of chordoma.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation can contribute to the inflammatory milieu and the immune evasion of the chordoma microenvironment.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Chordoma testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the TME; testosterone deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) cascade of chordoma.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Chordoma serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the chordoma TME; serotonin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of chordoma.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Chordoma prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the chordoma immune TME; hyperprolactinaemia amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of chordoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Chordoma oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the tumour-promoting inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of chordoma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Chordoma vasopressin: vasopressin, via V1aR on mast cells (already mapped) and macrophages (already mapped), modulates the tumour vascular milieu; vasopressin dysregulation amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) antitumour cascade of chordoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Chordoma selenium: selenium, as GPx in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; selenium deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) oxidative TME cascade of chordoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Chordoma iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and T-cytotoxic (already mapped) surveillance; iodine deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of chordoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Chordoma magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and T-cytotoxic cells (already mapped); magnesium deficiency amplifies IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting signalling cascade of chordoma.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Chordoma phosphorus: phosphorus, as ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped), fuels proliferative and cytotoxic signalling; phosphorus dysregulation amplifies the IL-6 (already mapped) and mast-cell (already mapped) TME of chordoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — sodium homeostasis in macrophage (already mapped) and fibroblast (already mapped) regulates tumour ionic microenvironment; sodium dysregulation amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in chordoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — potassium channels on T-cytotoxic cell (already mapped) and macrophage (already mapped) regulate anti-tumour immunity; potassium dysregulation amplifies mTOR (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade in chordoma.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — iron in macrophage (already mapped) and fibroblast (already mapped) fuels oxidative tumour microenvironment; iron excess amplifies mTOR (already mapped) and P53 (already mapped) and VEGF (already mapped) cascade in chordoma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stacchiotti-2012-imatinib-chordoma]: Stacchiotti S, Longhi A, Ferraresi V, et al. Phase II study of imatinib in advanced chordoma. *J Clin Oncol.* 2012;30(9):914-920. [doi:10.1200/JCO.2011.35.3656](https://doi.org/10.1200/JCO.2011.35.3656) · [PubMed 22330157](https://pubmed.ncbi.nlm.nih.gov/22330157/)
[^yang-2009-tbxt-chordoma]: Yang XR, Ng D, Alcorta DA, et al. T (brachyury) gene duplication confers major susceptibility to familial chordoma. *Nat Genet.* 2009;41(11):1176-1178. [doi:10.1038/ng.454](https://doi.org/10.1038/ng.454) · [PubMed 19801977](https://pubmed.ncbi.nlm.nih.gov/19801977/)
