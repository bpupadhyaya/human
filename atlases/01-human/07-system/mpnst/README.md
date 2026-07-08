---
schema: human-scale-entry/v1
id: mpnst
name: MPNST
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "MPNST is the most lethal NF1-associated tumor; NF1 LOF + CDKN2A deletion + PRC2/SUZ12 LOF → H3K27me3 loss defines high-grade MPNST; ~50% sporadic; surgery is the only curative modality; 5-year OS ~25-40%; selumetinib active in NF1 plexiform neurofibromas but not MPNST."
aliases: ["MPNST", "malignant peripheral nerve sheath tumor", "NF1 MPNST", "neurofibrosarcoma", "malignant schwannoma", "sarcoma NF1", "plexiform neurofibroma malignant transformation", "MPNST SUZ12", "MPNST H3K27me3", "MPNST PRC2"]
sources:
  - id: evans-2002-mpnst-nf1
    type: peer-reviewed
    cite: "Evans DGR, Baser ME, McGaughran J, et al. Malignant peripheral nerve sheath tumours in neurofibromatosis 1. J Med Genet. 2002;39(5):311-314."
    doi: "10.1136/jmg.39.5.311"
    pmid: "12011145"
    url: "https://doi.org/10.1136/jmg.39.5.311"
  - id: lee-2014-mpnst-prc2
    type: peer-reviewed
    cite: "Lee W, Teckie S, Wiesner T, et al. PRC2 is recurrently inactivated through EED or SUZ12 loss in malignant peripheral nerve sheath tumors. Nat Genet. 2014;46(11):1227-1232."
    doi: "10.1038/ng.3095"
    pmid: "25240281"
    url: "https://doi.org/10.1038/ng.3095"
cross_links:
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 syndrome (germline NF1) confers ~10% lifetime MPNST risk; NF1-associated MPNST arises from plexiform neurofibroma transformation; NF1 LOF → RAS → MAPK/PI3K → MPNST growth; NF1-associated MPNST has worse OS than sporadic (~25% vs ~50% 5-year OS)."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A homozygous deletion in ~70-80% high-grade MPNST; NF1+CDKN2A loss → CDK4/6 → RB1 phosphorylation → E2F proliferation; ARF loss → MDM2 unrestricted → p53 inactivation without TP53 mutation; CDK4/6 inhibitors (palbociclib) active in preclinical MPNST."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "PRC2/EZH2 is inactivated in ~70-90% high-grade MPNST by SUZ12 or EED mutations → H3K27me3 LOST (contrast AT/RT/SS where H3K27me3 accumulates); H3K27me3 loss by IHC is a diagnostic marker for high-grade MPNST; EZH2 inhibitors are NOT active in MPNST (PRC2 already lost)."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "NF1 LOF → RAS → MEK/ERK1/2 hyperactivation drives MPNST proliferation; MEK inhibitors (trametinib, binimetinib) explored in preclinical MPNST — less active than in neurofibroma; MPNST MEK resistance via PI3K bypass; MEK + mTOR or MEK + CDK4/6 dual inhibition being studied."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Neurofibromatosis type 1 (germline NF1 loss) carries a ~10% lifetime MPNST risk, arising when a plexiform neurofibroma transforms via CDKN2A deletion then PRC2 inactivation; sudden growth or pain in a stable plexiform lesion demands urgent FDG-PET and biopsy."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "MPNST is a high-grade sarcoma of the Schwann-cell sheath that grows from a major peripheral nerve trunk, often requiring en bloc nerve sacrifice; perineural spread mandates wide (≥2 cm) margins, and S100/SOX10 are only focally positive unlike benign schwannoma."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "MPNST and AT/RT sit at opposite poles of PRC2 biology: MPNST inactivates PRC2 (SUZ12/EED loss) so H3K27me3 is LOST, whereas AT/RT (SMARCB1 loss) leaves PRC2 hyperactive with H3K27me3 retained — so H3K27me3 IHC separates them and EZH2 inhibitors help AT/RT but not MPNST."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "MPNST and schwannomatosis are both peripheral nerve sheath tumor disorders but opposite in behavior: schwannomatosis makes multiple benign, painful schwannomas (SMARCB1/LZTR1), while MPNST is a high-grade Schwann-cell sarcoma arising mostly from NF1 plexiform neurofibromas."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "MPNST and synovial sarcoma are monomorphic spindle-cell sarcomas that mimic each other, but their epigenetics differ diagnostically: MPNST loses PRC2 (H3K27me3 absent by IHC) while synovial sarcoma's SS18-SSX fusion retains it — one stain excludes one and confirms the other."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "MPNST is a high-grade soft-tissue sarcoma of the limbs, trunk, and paraspinal region arising from a major nerve trunk; like other extremity sarcomas it needs wide en-bloc resection plus radiation, but perineural spread and chemoresistance make it among the deadliest."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiation is a key MPNST risk and treatment: prior radiotherapy is a recognized cause of these aggressive nerve-sheath sarcomas (often years later), and because wide margins are hard near nerves, adjuvant radiotherapy is used despite the radiation-induced-second-tumor concern."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "MPNST and rhabdomyosarcoma intersect in the malignant Triton tumor: an MPNST with rhabdomyosarcomatous (skeletal-muscle) differentiation, often arising in NF1, behaves especially aggressively—showing how a nerve-sheath sarcoma can acquire the myogenic program of rhabdomyosarcoma."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "MPNST and Ewing sarcoma are both aggressive sarcomas of young people requiring molecular distinction: MPNST arises from nerve sheath (NF1-driven, S100/SOX10, CDKN2A loss), while Ewing is a small-round-blue-cell tumor with EWSR1-FLI1 and CD99—different cells, drivers and chemo."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "MPNST and GIST are the malignancies most characteristic of neurofibromatosis type 1: NF1 patients develop both, as neurofibromin loss disinhibits Ras in Schwann-cell precursors (MPNST) and interstitial cells of Cajal (NF1-GIST)—one tumor-suppressor loss, two sarcomas."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "MPNST and Li-Fraumeni intersect through sarcoma predisposition: germline TP53 loss predisposes to sarcomas, and somatic TP53/CDKN2A loss marks a benign neurofibroma's transformation into MPNST—losing cell-cycle and apoptosis control turns nerve sheath malignant."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "MPNST and osteosarcoma are both aggressive sarcomas that can be radiation-induced: prior radiotherapy is a recognized cause of each, and both are high-grade and resist chemotherapy—so a new sarcoma in a previously irradiated field raises suspicion for either."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "MPNST grows from and destroys peripheral nerves: this aggressive sarcoma arises from Schwann-cell-lineage cells of a nerve sheath, often transforming a plexiform neurofibroma, so it invades along nerves causing pain and deficits as it engulfs the neurons it surrounds."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "MPNST is a spindle-cell sarcoma resembling fibroblasts: its fascicles of spindle cells can mimic fibrosarcoma, so diagnosis leans on nerve origin, NF1 context and loss of H3K27me3 (from PRC2/SUZ12 loss) rather than appearance alone."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 loss drives malignant transformation to MPNST: a benign neurofibroma becomes MPNST as NF1 loss is joined by CDKN2A and TP53 inactivation, so accumulating tumor-suppressor hits convert a slow plexiform tumor into an aggressive sarcoma."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy helps treat MPNST, a radioresistant sarcoma: arising along nerves often near the spine or skull base, MPNST needs high radiation doses, so protons' sharp dose falloff allows dose escalation while sparing the spinal cord and nearby organs."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "MPNST is the malignant sarcoma of the peripheral nervous system: it arises from nerve-sheath (Schwann) cells, often from a pre-existing neurofibroma in NF1, so rapid growth or new pain in a neurofibroma signals possible malignant transformation."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "MPNST relies on VEGF-driven angiogenesis: like other aggressive sarcomas it secretes VEGF to vascularize its fast-growing mass, so anti-angiogenic tyrosine-kinase inhibitors are among the systemic options for this chemoresistant tumor."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "MPNST runs on the RAS-PI3K-mTOR axis: NF1 loss unleashes RAS, which fires PI3K-AKT-mTOR to drive growth, so mTOR inhibitors (often combined with MEK blockade) are tested against a sarcoma that resists standard chemotherapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages crowd MPNST and its precursor: plexiform neurofibromas are rich in macrophages and mast cells that feed an inflammatory niche promoting growth and malignant transformation, making this immune microenvironment a target."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "NF1 and NF2 split the nerve-tumor risk: NF1's neurofibromas can transform into MPNST, while NF2 instead causes schwannomas and meningiomas that rarely turn malignant—so the two syndromes demand different surveillance for nerve cancers."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "MPNST is fundamentally unleashed RAS: NF1's protein is a brake on RAS, so losing it lets KRAS/RAS-MAPK signaling run wild, transforming benign neurofibromas into this aggressive sarcoma—why MEK inhibitors are tested against it."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "MPNST progression hinges on losing the CDK4/6 brake: CDKN2A deletion removes the inhibitor of these cell-cycle kinases, letting the tumor divide unchecked—a hallmark of the leap from plexiform neurofibroma to malignancy."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "MPNST is studied as a target for NK and immune therapy: because it resists chemo and radiation, harnessing natural killer cells and the immune system is explored to attack this sarcoma where standard treatments fall short."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "MPNST spreads to the lungs above all: this aggressive nerve-sheath sarcoma metastasizes through the blood to seed pulmonary nodules, the dominant site of spread and a leading cause of death, so chest imaging guides staging."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia drives MPNST's aggressiveness: the fast-growing sarcoma outpaces its blood supply, and the low-oxygen microenvironment promotes invasion and resistance, part of why this nerve-sheath tumor responds poorly to radiation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "MPNST largely escapes cytotoxic T cells: with an immunosuppressive, T-cell-poor microenvironment it resists checkpoint drugs, so engineered T-cell and combination immunotherapies are explored against a sarcoma that defies standard care."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "MPNST spreads through the blood to the liver: like other high-grade sarcomas it favors the lungs but also seeds the liver, marking the metastatic stage of this aggressive nerve-sheath cancer."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "MPNST recruits endothelial cells to grow: VEGF from the tumor drives these vessel-lining cells to build a blood supply for its rapid growth, a target of anti-angiogenic strategies."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "MPNST is a spindle-cell tumor woven with collagen: its fibroblast-like cells lay down a dense fibrous matrix, the firm fascicular tissue that, arising from a nerve, distinguishes it from benign neurofibromas."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals MPNST's nerve-sheath roots: scattered cells show schwannian differentiation — interdigitating processes wrapped in basal lamina — the ultrastructural clue to origin in a tumor that often loses its diagnostic S100 staining."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "MPNST exploits an IGF-1 loop: the tumor overexpresses the IGF-1 receptor, and autocrine insulin-like growth factor signaling fuels proliferation and survival — a pathway probed for therapy in a cancer that resists conventional treatment."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Losing NF1 unleashes AKT in MPNST: with neurofibromin gone, RAS activates the PI3K-AKT survival axis alongside MEK, so AKT signaling helps the tumor evade death — part of why dual-pathway blockade is being explored."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "MPNST favors the skeleton when it spreads: after the lungs, bone is a common metastatic site, with deposits in the marrow-bearing vertebrae and long bones marking the aggressive, hard-to-cure disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "MPNST can reach the brain: hematogenous metastases to the central nervous system, though less common than lung spread, are a grim development in this fast-growing nerve-sheath sarcoma."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "In NF1, MPNST often arises deep in the body: retroperitoneal and pelvic tumors grow against the bowel, the large intestine displaced or invaded by a sarcoma transforming from a plexiform neurofibroma."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody stains catch the transformation: loss of H3K27me3 by immunohistochemistry is an MPNST hallmark, and the patchy or absent S100 and SOX10 that once marked the Schwann cell fade as a benign neurofibroma turns malignant."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The chemotherapy taxes the marrow: the doxorubicin-and-ifosfamide regimens thrown at this aggressive sarcoma are strongly myelosuppressive, dropping neutrophil counts and making febrile neutropenia a recurring hazard of treatment."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "A changing lump under the skin is the warning: in NF1 an MPNST usually arises from a plexiform neurofibroma, so a deep mass that suddenly enlarges, hardens, or turns painful beneath the café-au-lait-marked skin demands urgent imaging and biopsy."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The sarcoma chemotherapy strains the heart: when MPNST is treated, the doxorubicin-ifosfamide backbone carries anthracycline cardiotoxicity, injuring cardiomyocytes and demanding cardiac monitoring through the limited chemo that this resistant tumor allows."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Most MPNSTs arise in NF1, which is inherited: the syndrome passes to half of a carrier's children, so a diagnosis prompts family genetic counseling, while the cytotoxic chemotherapy adds its own threat to fertility in these often-young patients."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Like other aggressive sarcomas it drives clotting: MPNST raises the risk of venous thromboembolism through paraneoplastic thrombocytosis and tumor procoagulants, complicating the major surgery its treatment requires."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "An upstream receptor feeds the runaway signaling: MPNST often overexpresses EGFR, pouring extra input into the RAS-MAPK pathway already unleashed by NF1 loss, and making the receptor a candidate target in a sarcoma stubbornly resistant to chemotherapy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The tumor builds an immune-cold niche: regulatory T cells and suppressive myeloid cells crowd the MPNST microenvironment and blunt T-cell attack, part of why single-agent checkpoint blockade has disappointed and combination immunotherapy is being tried."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Two neural-crest tumors meet at the Schwann-melanocyte line: MPNST and melanoma share the S100 and SOX10 lineage markers, and rare melanotic variants blur the boundary, reflecting their common origin in the migrating neural crest."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "New pain in a neurofibroma is the warning sign: malignant transformation to MPNST classically announces itself with rapid growth and worsening neuropathic pain along the nerve, the symptom that prompts urgent imaging and biopsy in NF1."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Growth-factor receptors feed the sarcoma: MPNST cells express PDGF receptors whose autocrine signaling drives proliferation, one of the receptor tyrosine kinases probed for targeted therapy in this treatment-resistant tumor."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 sustains the malignant Schwann cell: activated STAT3 signaling supports MPNST survival and the immunosuppressive microenvironment, marking another node in a tumor driven mainly by loss of NF1 and PRC2."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Loss of NF1 routes RAS into NF-κB: unrestrained RAS signaling in MPNST engages NF-κB-driven survival and inflammation, part of the network that makes this NF1-associated sarcoma so aggressive and treatment-resistant."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A bulky sarcoma that clots: MPNST carries tumor-driven hypercoagulability, and the major limb or trunk surgery and chemotherapy it requires add to the venous thromboembolism risk."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Intensive treatment and large tumors invite infection: the chemotherapy used against this aggressive sarcoma causes neutropenia, and extensive resections risk wound infection — both routes to sepsis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracycline scars the heart: the doxorubicin in MPNST chemotherapy is dose-dependently cardiotoxic, risking a cardiomyopathy and heart failure in survivors of this aggressive sarcoma."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemo neutropenia opens the lung to mold: the dose-intensive doxorubicin-ifosfamide regimens for MPNST cause deep neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An aggressive cancer on top of NF1 weighs on mood: MPNST's poor prognosis, disfiguring surgery and frequent arising in the burden of neurofibromatosis type 1 carry a substantial psychological toll."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Ifosfamide scars the kidney: the alkylator used in MPNST chemotherapy is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Radical resection and radiation heal badly: the wide excision of an MPNST, often with adjuvant radiation, leaves large soft-tissue wounds prone to dehiscence and slow healing."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Aggressive cancer and NF1 surveillance breed worry: the poor prognosis of MPNST and, in NF1 patients, the constant vigilance for malignant change in plexiform neurofibromas foster chronic health anxiety."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It spreads to the lungs: like other soft-tissue sarcomas, MPNST metastasises preferentially to the lungs, so pulmonary metastases dominate its surveillance and drive much of its mortality."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It erupts from a skin-associated nerve tumour: MPNST often arises within the plexiform neurofibromas of NF1, presenting as an enlarging, painful subcutaneous mass that signals malignant change."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its chemotherapy reawakens shingles: the doxorubicin-ifosfamide regimens for MPNST cause deep immunosuppression that allows latent varicella-zoster to reactivate."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its chemotherapy injures the kidney and bladder: the ifosfamide in MPNST regimens causes a Fanconi-like renal tubulopathy and haemorrhagic cystitis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its cure can scar the heart: the doxorubicin used against MPNST carries a dose-dependent cardiotoxicity risk on top of the disease's aggressive course."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It bypasses the lymph nodes: like other sarcomas, MPNST spreads haematogenously to the lungs and only rarely to lymph nodes, so it is staged differently from carcinomas."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It spreads through the bloodstream to the liver: MPNST metastasises haematogenously to the liver and lungs, and its chemotherapy brings nausea and mucositis."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Treatment suppresses immunity and biology invites it: intensive sarcoma chemotherapy is immunosuppressive, while MPNST is studied for immune and combination targeted therapy in NF1 patients."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "It is a target for pathway drugs: arising from NF1 loss with hyperactive RAS-MEK signalling, MPNST is investigated for MEK and other targeted inhibitors beyond standard sarcoma chemotherapy."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Sarcoma chemo for advanced disease: doxorubicin and ifosfamide, the standard soft-tissue sarcoma regimen, are used for unresectable or metastatic MPNST, though responses are limited."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "A fellow neural-crest tumour: like neuroblastoma, MPNST derives from neural-crest lineage, the two among the nerve-associated malignancies that arise in children and young adults."
  - target: 01-human/07-system/chordoma
    relation: connects-to
    note: "A rare tumour where surgery and particle radiation lead: like chordoma, MPNST is a rare, radioresistant malignancy whose control depends on complete resection and high-dose proton or photon radiation."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Two tumours of the NF1 spectrum: neurofibromatosis type 1 predisposes both to malignant peripheral nerve sheath tumours and to pheochromocytoma, neural-crest-derived growths unleashed when neurofibromin no longer restrains RAS signalling."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "A poorly immunogenic sarcoma: malignant peripheral nerve sheath tumours have low mutational burden and respond little to PD-1 checkpoint inhibitors as monotherapy, so immunotherapy is investigated mainly in combinations for this chemoresistant cancer."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "One RAS pathway, blood and nerve: NF1 loss drives RAS-MAPK overactivity, predisposing not only to MPNST but to myeloid neoplasms—juvenile myelomonocytic and chronic myelomonocytic leukaemia—so neurofibromin links a nerve-sheath sarcoma to the marrow."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "Convergent loss of H3K27me3: MPNST (via PRC2/SUZ12 loss) and diffuse midline glioma (via H3K27M) both erase the H3K27me3 repressive mark—two unrelated tumours sharing an epigenetic catastrophe diagnosed by its loss on staining."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Lung is the dominant metastatic site: MPNST spreads through the blood, preferentially seeding the lungs and the alveolar capillary bed, the pattern that dictates chest surveillance."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "It arises within a nerve: MPNST grows from a peripheral nerve (often a plexiform neurofibroma in NF1), destroying the axons it engulfs and heralded by rapid growth and new neurological deficit."
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "A fibroblastic differential: like MPNST, a desmoid tumour presents as a deep, infiltrative soft-tissue mass, and the two sit in the differential of an enlarging extremity or trunk lesion despite their very different biology and prognosis."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "NF1's two malignancies: neurofibromatosis type 1 predisposes to MPNST in peripheral nerves and to high-grade gliomas including glioblastoma in the CNS, both RAS-pathway-driven cancers of the syndrome."
  - target: 01-human/03-molecular/h3k27m
    relation: connects-to
    note: "Two routes to the same epigenetic loss: the H3K27M oncohistone of diffuse midline glioma and PRC2 (SUZ12/EED) inactivation in MPNST both abolish the repressive H3K27me3 mark, a convergence exploited diagnostically by loss of H3K27me3 staining."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Malignant transformation: MYC activation helps drive the progression of plexiform neurofibroma to MPNST, fuelling the proliferation of this aggressive sarcoma."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative immortality: TERT promoter activation maintains telomeres in MPNST, supporting the unlimited division of its transformed cells."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "MAPK amplification: NF1 loss unleashes RAS, and additional BRAF/MAPK-pathway activation further drives the RAS-RAF-MEK-ERK signalling central to MPNST."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: with CDKN2A loss frequent in MPNST, cyclin D1-CDK4/6 activity pushes these aggressive nerve-sheath tumour cells through the G1 checkpoint."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Receptor signalling: MET activation contributes to the growth and invasion of MPNST, a candidate targetable kinase in these treatment-resistant sarcomas."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the hypoxic MPNST drives the VEGF angiogenesis and metabolic adaptation that support its rapid, infiltrative growth."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle escape: RB1-pathway inactivation, with CDKN2A loss, marks the malignant transformation of plexiform neurofibroma to MPNST, releasing the brake on the cell cycle."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into MPNST, building the immunosuppressive stroma of this aggressive nerve-sheath sarcoma."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptosis resistance: MPNST cells evade caspase-3-mediated apoptosis, contributing to the chemoresistance that makes these sarcomas so difficult to treat."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Lung metastasis: CXCR4 on MPNST cells follows CXCL12 gradients to the lung, the dominant site of the metastasis that is the principal cause of death in these aggressive nerve-sheath sarcomas."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Mast-cell niche: the plexiform neurofibromas from which MPNST arises are rich in KIT-dependent mast cells whose stem-cell-factor signalling supports the Schwann-cell tumour microenvironment and its progression to malignancy."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K activation: PTEN loss activates PI3K-AKT signalling during the progression of plexiform neurofibroma to MPNST, cooperating with the NF1-driven RAS hyperactivation to drive malignant transformation."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic dysregulation: loss of PRC2 (EZH2/SUZ12) that abolishes H3K27 trimethylation is a defining MPNST event, and the accompanying DNA-methylation changes reshape the epigenome, marking the malignant transformation from neurofibroma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy: MPNST is an aggressive sarcoma being explored for cellular and checkpoint immunotherapy, which would kill tumour cells through perforin and granzyme — a needed option given its poor response to chemotherapy."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Radioresistance: RAD51-mediated homologous-recombination repair helps MPNST survive radiation, a mechanism of the radioresistance that limits local control of these tumours, which themselves can arise in prior radiation fields."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: with CDKN2A loss and the RB pathway engaged (CDK4/6, cyclin-D1 and RB1 already mapped), E2F1 is released to drive the aggressive proliferation of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K limb: the RAS hyperactivation that follows NF1 loss also engages PI3K (AKT, mTOR and PTEN already mapped), a parallel growth-and-survival pathway in MPNST."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 inactivation: MDM2 amplification and TP53 loss (p53 mapped) contribute to the malignant transformation of a plexiform neurofibroma into MPNST."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "STAT3 survival: JAK-STAT3 signalling (STAT3 already mapped) supports the survival and proliferation of malignant peripheral nerve sheath tumour cells."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis resistance: anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the chemoresistance of MPNST."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Redox and resistance: NRF2 antioxidant signalling shapes the redox balance and treatment resistance of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling modulates the invasion and immunosuppressive microenvironment of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the invasion and survival of malignant peripheral nerve sheath tumour cells."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment relevant to immunotherapy in MPNST."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immunologically cold microenvironment of MPNST, a barrier to its immunotherapy."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the mesenchymal microenvironment and aggressive progression of the NF1-driven MPNST."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, antagonised by NF1-loss-driven RAS-PI3K-AKT signalling, modulate the survival of MPNST cells."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Wnt/β-catenin and survival signaling of the NF1-deficient cells of MPNST."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of the NF1-associated MPNST."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling downstream of receptor tyrosine kinases (EGFR, KIT, MET, and PDGFR already mapped) drives the invasive signaling of MPNST."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and therapy resistance of malignant peripheral nerve sheath tumor cells."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes, alongside PRC2 loss, to the epigenetic dysregulation of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "YAP1-Hippo signaling participates in the proliferation and mesenchymal biology of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the tumor microenvironment and invasion of malignant peripheral nerve sheath tumor."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunosurveillance: MHC class II antigen presentation shapes the T-cell response to malignant peripheral nerve sheath tumour, a chemoresistant sarcoma for which the loss of antigen presentation contributes to immune evasion."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Cellular immunotherapy: IL-2-driven T-cell expansion supports the adoptive-cell and vaccine approaches being explored for malignant peripheral nerve sheath tumour, which responds poorly to conventional chemotherapy."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint context: PD-1-mediated T-cell exhaustion limits anti-tumour immunity in the immunologically cold malignant peripheral nerve sheath tumour, and checkpoint blockade is being tested in combination for this aggressive sarcoma."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Chemotherapy anaemia: the doxorubicin-ifosfamide chemotherapy used for malignant peripheral nerve sheath tumour, which responds poorly, is myelosuppressive and lowers haemoglobin, the anaemia adding to the burden of this aggressive sarcoma."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the doxorubicin in sarcoma regimens for malignant peripheral nerve sheath tumour is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury of the anthracycline dose."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 helps make malignant peripheral nerve sheath tumour an immunologically cold sarcoma (PD-1 already mapped), dampening the T-cell response that combination checkpoint strategies aim to mount."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, immune-evasive microenvironment of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative microenvironment: the aggressive sarcoma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species (NRF2 already mapped) are part of the tumour microenvironment and treatment resistance."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of malignant peripheral nerve sheath tumour, part of the stromal biology of this aggressive sarcoma."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive microenvironment of the malignant peripheral nerve sheath tumour."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the myelosuppressive chemotherapy and the tumour burden of malignant peripheral nerve sheath tumour cause anaemia (haemoglobin already mapped) needing transfusion, whose repeated support can load the body with iron."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone invasion: the aggressive malignant peripheral nerve sheath tumour invades the adjacent bone, and the paraspinal tumours can erode the vertebrae, part of its locally destructive behaviour."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Fibro-adipose adipokine: leptin from the fibro-adipose context of the plexiform neurofibroma from which MPNST arises signals to the tumour, part of its metabolic microenvironment."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Microenvironment adipokine: adiponectin, with leptin (already mapped), from the fibro-adipose microenvironment signals within the malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the microenvironment of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the emerging immunotherapy of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the immunosuppressive microenvironment of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of malignant peripheral nerve sheath tumour."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the malignant peripheral nerve sheath tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the malignant peripheral nerve sheath tumour microenvironment."
---

# MPNST

## Overview

**Malignant peripheral nerve sheath tumor (MPNST)** is a high-grade soft tissue sarcoma arising from the neural crest-derived Schwann cell lineage, defined by a characteristic molecular signature of **NF1 LOF + CDKN2A deletion + PRC2 (SUZ12/EED) inactivation**. MPNST is the most lethal tumor associated with **neurofibromatosis type 1 (NF1) syndrome** and the leading cause of NF1-related mortality. It arises predominantly from malignant transformation of plexiform neurofibromas, but ~40-50% of cases occur sporadically without germline NF1 mutation. MPNST has no approved targeted therapy; surgery is the only curative modality, and prognosis remains poor, particularly in NF1-associated disease [^evans-2002-mpnst-nf1].

**Epidemiology:**
- Incidence: ~1,500-2,000 cases/year USA (~0.001% general population); ~10% lifetime risk in NF1 syndrome
- NF1-associated MPNST: ~50-60% of all MPNST; arises from plexiform neurofibroma
- Sporadic MPNST: ~40-50%; arise de novo from peripheral nerve without NF1; molecularly distinct from NF1-associated in ~30-40% (lack biallelic NF1 mutation but share CDKN2A + PRC2 alterations)
- Radiation-induced MPNST: ~10%; arises in radiation field, median 10-15 years after exposure; worst prognosis
- Median age: NF1-associated ~26-30 years; sporadic ~40-50 years; MPNST is a "young adult" sarcoma
- Sex: equal M:F distribution

**Key clinical features:**
- Rapidly enlarging, painful mass arising from or along a peripheral nerve trunk
- Most common sites: proximal extremities (thigh, upper arm), trunk/paraspinal region, head and neck
- In NF1 patients: rapid growth or pain in a previously stable plexiform neurofibroma → urgent workup
- FDG-PET: highly SUV-avid (SUVmax typically >4-6); distinguishes MPNST from benign plexiform (SUVmax <3.5) and guides biopsy; MPNST FDG-PET sensitivity ~89%, specificity ~95%

## Structure

### Molecular classification

**The three-hit model of MPNST:**
1. **NF1 LOF**: biallelic NF1 inactivation (germline + somatic LOH, or two somatic hits) → RAS constitutive activation
2. **CDKN2A homozygous deletion** (~70-80%): p16(INK4a) loss → CDK4/6 → RB1 hyperphosphorylation → E2F cell cycle; ARF loss → MDM2 unrestricted → p53 pathway loss (without TP53 mutation)
3. **PRC2 inactivation** (SUZ12 or EED mutation, ~70-90%): [^lee-2014-mpnst-prc2] H3K27 trimethylation LOST → de-repression of developmental transcription factors; inverse of AT/RT and synovial sarcoma (where PRC2 is hyperactive)

**Additional somatic alterations in MPNST:**
- TP53 mutations: ~15-25%; late event; radiotherapy-induced MPNST enriched
- ATRX mutations: ~20%; alternative lengthening of telomeres
- RB1 mutations: ~10-15%; often in the setting of CDKN2A deletion
- EGFR amplification: ~15-20%; receptor tyrosine kinase amplification
- MET amplification: ~10%; poor prognosis
- CDC42/RAC1 mutations: rare; cytoskeletal signaling

### Histology

**Classic MPNST histology:**
- Fascicular architecture of spindle cells with hyperchromatic, wavy, or comma-shaped nuclei; reminiscent of cellular schwannoma but with atypia
- Alternating hypercellular and hypocellular areas ("marbling pattern")
- Geographic necrosis; hemangiopericytoma-like vessels
- High mitotic rate (>4/10 HPF in WHO definition; typically >10/10 HPF in high-grade)
- Variable "heterologous differentiation" (rhabdomyoblastic = Triton tumor, osteosarcomatous, chondroid): ~15-20% of MPNST have divergent elements

**Grading:** MPNST are uniformly FNCLCC grade 2-3; grade 3 features (>10 mitoses/10 HPF, necrosis, high cellularity) confer worse prognosis

### IHC panel and diagnostic workup

**SOX10**: most sensitive marker for Schwann cell lineage in MPNST; positive in ~40-50%; focal; absent in ~50% (unlike benign schwannoma where SOX10 is diffusely positive)

**S100**: positive in ~50-70% of low-grade MPNST; only ~30-40% of high-grade MPNST; focal/patchy (unlike diffuse S100 in schwannoma)

**H3K27me3 (trimethyl H3K27 IHC):** LOST (complete loss of nuclear H3K27me3 staining) in ~70-90% of high-grade MPNST due to PRC2 inactivation; highly diagnostic — complete H3K27me3 loss in a spindle cell sarcoma = strong evidence for MPNST; retained in schwannoma, neurofibroma, synovial sarcoma, AT/RT; sensitivity ~70-90%, specificity ~95% for MPNST vs benign NF1 neurofibroma

**CDKN2A FISH:** homozygous deletion by FISH → confirms MPNST molecular signature; useful in NF1 patients where biopsy shows borderline atypia

**NF1 protein (neurofibromin IHC):** neurofibromin expression lost in most MPNST; however, IHC is variable and not routinely used in diagnosis; NF1 FISH/sequencing preferred

**Ki-67:** typically >30% in high-grade MPNST; useful for distinguishing from atypical neurofibroma (Ki-67 <10%)

## Function

### Oncogenesis: plexiform neurofibroma → MPNST

The malignant transformation of plexiform neurofibroma to MPNST follows an ordered acquisition of molecular hits:

**Step 1 — NF1 LOF (neurofibroma):**
Germline NF1 + somatic LOH at 17q11.2 → biallelic NF1 loss in Schwann cell → RAS-GTP accumulation → mast cell recruitment (SCF/c-KIT) → neurofibroma microenvironment; benign neurofibromas require mast cell support and are indolent

**Step 2 — CDKN2A deletion (atypical neurofibroma):**
Emerging somatic CDKN2A homozygous deletion → p16 loss → CDK4/6 hyperactivation → first step toward autonomy; "atypical neurofibromatous neoplasm of uncertain biological potential" (ANNUBP) = intermediate lesion with CDKN2A deletion but lacking PRC2 mutations or high-grade features

**Step 3 — PRC2 inactivation (MPNST):**
SUZ12 or EED mutation (often biallelic) → EZH2 enzymatic activity lost → H3K27me3 erased → developmental transcription factors (HOXC, HOXD clusters, TWIST1, SOX11) de-repressed → Schwann cells lose lineage identity → mesenchymal plasticity → high-grade sarcomatous phenotype

**Key distinction from AT/RT and synovial sarcoma:**
- **AT/RT**: SMARCB1 biallelic deletion → BAF lost → PRC2/EZH2 hyperactive → H3K27me3 accumulated → EZH2 inhibitors active
- **Synovial sarcoma**: SS18-SSX → SMARCB1 displaced from BAF → PRC2/EZH2 hyperactive → H3K27me3 accumulated → EZH2 inhibitors active
- **MPNST**: SUZ12/EED LOF → PRC2/EZH2 catalytically dead → H3K27me3 LOST → EZH2 inhibitors NOT active (PRC2 cannot be further inhibited)

This is a critical diagnostic and therapeutic distinction: H3K27me3 IHC distinguishes MPNST (lost) from AT/RT and SS (retained/elevated).

## Pathology

### Staging and risk stratification

**Prognostic factors:**
- **Germline NF1 status**: NF1-associated MPNST 5-year OS ~25-40%; sporadic MPNST ~50-60%; radiation-induced MPNST ~20-30%
- **Tumor size**: most important single factor; ≤5 cm → 5-year OS ~55-70%; >5 cm → ~30-40%
- **Margin status**: R0 resection essential; R1 → 50% local recurrence; R2 → near-universal recurrence
- **Grade**: FNCLCC grade 3 → significantly worse prognosis than grade 2
- **CDKN2A deletion**: independently associated with worse OS
- **Metastases**: lung (~80% of metastases), liver, bone; ~20% metastatic at diagnosis; 5-year OS ~15%

### Treatment

**Surgery:**
Wide local excision with negative margins is the only potentially curative intervention; MPNST margins must be generous (≥2 cm) due to perineural spread tendency; limb-sparing preferred; en bloc nerve sacrifice required if MPNST arises from named nerve (sciatic, brachial plexus); compartmental resection for large tumors; spinal MPNST requires vertebrectomy ± cord decompression

**Radiation therapy:**
- Pre- or postoperative RT for high-risk features (tumor >5 cm, positive margin, recurrence, radiation-naive)
- Standard dose: 50-54 Gy preoperative or 60-66 Gy postoperative
- RT for MPNST must balance efficacy against radiation-field carcinogenesis risk (especially in NF1 patients)
- NF1 patients have increased radiation sensitivity and secondary malignancy risk → limit RT field/dose where possible

**Chemotherapy:**
- MPNST is chemotherapy-resistant compared to other sarcomas; responses are modest
- **Doxorubicin + ifosfamide (AI)**: standard first-line for metastatic/unresectable; ORR ~20-30% (lower than synovial sarcoma ORR ~40-60%)
- **Ifosfamide monotherapy**: ORR ~10-15% in MPNST
- **Gemcitabine + docetaxel**: second-line option; ORR ~10-15%
- No clinical trial has demonstrated OS benefit from chemotherapy in MPNST to date; chemotherapy used to control symptoms/slow progression

**Targeted therapies (no approved agent for MPNST):**
- **MEK inhibitors** (selumetinib, trametinib): active in NF1 plexiform neurofibromas but largely inactive in MPNST (CDKN2A + PRC2 co-mutations bypass MEK dependence); single-arm Phase 2 trials: selumetinib ORR 0% in MPNST; MEK + CDK4/6 and MEK + mTOR combinations in Phase 1/2
- **CDK4/6 inhibitors** (palbociclib): CDKN2A deletion in ~70-80% provides rationale; preclinical activity; clinical trials ongoing (NCT03605654)
- **PRC2 reconstitution**: investigational — strategies to restore H3K27me3 via epigenetic modulators; no clinical agents yet
- **Cabozantinib** (MET/VEGFR/RET): Phase 2 SARC051 ongoing in advanced sarcomas including MPNST
- **VEGFR inhibitors** (pazopanib): modest activity in MPNST as part of STS population trials

**Prognosis:**
- NF1-associated MPNST: 5-year OS ~25-40%; local recurrence major problem (~40-50%)
- Sporadic MPNST: 5-year OS ~50-60%
- Radiation-induced MPNST: 5-year OS ~20-25%; worst outcome subgroup
- Metastatic MPNST: median OS ~12-18 months; no curative option
- Local recurrence: ~40-50% at 5 years even after R0 resection; re-resection if technically feasible
- Primary CNS MPNST (optic nerve, cranial nerve VIII): particularly difficult; CN VIII MPNST rare; surgical approach highly morbid

## Connections

- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 syndrome (germline NF1) confers ~10% lifetime MPNST risk; NF1-associated MPNST arises from plexiform neurofibroma transformation; NF1 LOF → RAS → MAPK/PI3K → MPNST growth; NF1-associated MPNST has worse OS than sporadic (~25% vs ~50% 5-year OS).
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A homozygous deletion in ~70-80% high-grade MPNST; NF1+CDKN2A loss → CDK4/6 → RB1 phosphorylation → E2F proliferation; ARF loss → MDM2 unrestricted → p53 inactivation without TP53 mutation; CDK4/6 inhibitors (palbociclib) active in preclinical MPNST.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — PRC2/EZH2 is inactivated in ~70-90% high-grade MPNST by SUZ12 or EED mutations → H3K27me3 LOST (contrast AT/RT/SS where H3K27me3 accumulates); H3K27me3 loss by IHC is a diagnostic marker for high-grade MPNST; EZH2 inhibitors are NOT active in MPNST (PRC2 already lost).
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — NF1 LOF → RAS → MEK/ERK1/2 hyperactivation drives MPNST proliferation; MEK inhibitors (trametinib, binimetinib) explored in preclinical MPNST — less active than in neurofibroma; MPNST MEK resistance via PI3K bypass; MEK + mTOR or MEK + CDK4/6 dual inhibition being studied.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Neurofibromatosis type 1 (germline NF1 loss) carries a ~10% lifetime MPNST risk, arising when a plexiform neurofibroma transforms via CDKN2A deletion then PRC2 inactivation; sudden growth or pain in a stable plexiform lesion demands urgent FDG-PET and biopsy.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — MPNST is a high-grade sarcoma of the Schwann-cell sheath that grows from a major peripheral nerve trunk, often requiring en bloc nerve sacrifice; perineural spread mandates wide (≥2 cm) margins, and S100/SOX10 are only focally positive unlike benign schwannoma.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — MPNST and AT/RT sit at opposite poles of PRC2 biology: MPNST inactivates PRC2 (SUZ12/EED loss) so H3K27me3 is LOST, whereas AT/RT (SMARCB1 loss) leaves PRC2 hyperactive with H3K27me3 retained — so H3K27me3 IHC separates them and EZH2 inhibitors help AT/RT but not MPNST.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — MPNST and schwannomatosis are both peripheral nerve sheath tumor disorders but opposite in behavior: schwannomatosis makes multiple benign, painful schwannomas (SMARCB1/LZTR1), while MPNST is a high-grade Schwann-cell sarcoma arising mostly from NF1 plexiform neurofibromas.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — MPNST and synovial sarcoma are monomorphic spindle-cell sarcomas that mimic each other, but their epigenetics differ diagnostically: MPNST loses PRC2 (H3K27me3 absent by IHC) while synovial sarcoma's SS18-SSX fusion retains it — one stain excludes one and confirms the other.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — MPNST is a high-grade soft-tissue sarcoma of the limbs, trunk, and paraspinal region arising from a major nerve trunk; like other extremity sarcomas it needs wide en-bloc resection plus radiation, but perineural spread and chemoresistance make it among the deadliest.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiation is a key MPNST risk and treatment: prior radiotherapy is a recognized cause of these aggressive nerve-sheath sarcomas (often years later), and because wide margins are hard near nerves, adjuvant radiotherapy is used despite the radiation-induced-second-tumor concern.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — MPNST and rhabdomyosarcoma intersect in the malignant Triton tumor: an MPNST with rhabdomyosarcomatous (skeletal-muscle) differentiation, often arising in NF1, behaves especially aggressively—showing how a nerve-sheath sarcoma can acquire the myogenic program of rhabdomyosarcoma.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — MPNST and Ewing sarcoma are both aggressive sarcomas of young people requiring molecular distinction: MPNST arises from nerve sheath (NF1-driven, S100/SOX10, CDKN2A loss), while Ewing is a small-round-blue-cell tumor with EWSR1-FLI1 and CD99—different cells, drivers and chemo.
- `connects-to` → **[GIST](../gist/README.md)** — MPNST and GIST are the malignancies most characteristic of neurofibromatosis type 1: NF1 patients develop both, as neurofibromin loss disinhibits Ras in Schwann-cell precursors (MPNST) and interstitial cells of Cajal (NF1-GIST)—one tumor-suppressor loss, two sarcomas.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — MPNST and Li-Fraumeni intersect through sarcoma predisposition: germline TP53 loss predisposes to sarcomas, and somatic TP53/CDKN2A loss marks a benign neurofibroma's transformation into MPNST—losing cell-cycle and apoptosis control turns nerve sheath malignant.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — MPNST and osteosarcoma are both aggressive sarcomas that can be radiation-induced: prior radiotherapy is a recognized cause of each, and both are high-grade and resist chemotherapy—so a new sarcoma in a previously irradiated field raises suspicion for either.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — MPNST grows from and destroys peripheral nerves: this aggressive sarcoma arises from Schwann-cell-lineage cells of a nerve sheath, often transforming a plexiform neurofibroma, so it invades along nerves causing pain and deficits as it engulfs the neurons it surrounds.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — MPNST is a spindle-cell sarcoma resembling fibroblasts: its fascicles of spindle cells can mimic fibrosarcoma, so diagnosis leans on nerve origin, NF1 context and loss of H3K27me3 (from PRC2/SUZ12 loss) rather than appearance alone.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 loss drives malignant transformation to MPNST: a benign neurofibroma becomes MPNST as NF1 loss is joined by CDKN2A and TP53 inactivation, so accumulating tumor-suppressor hits convert a slow plexiform tumor into an aggressive sarcoma.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy helps treat MPNST, a radioresistant sarcoma: arising along nerves often near the spine or skull base, MPNST needs high radiation doses, so protons' sharp dose falloff allows dose escalation while sparing the spinal cord and nearby organs.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — MPNST is the malignant sarcoma of the peripheral nervous system: it arises from nerve-sheath (Schwann) cells, often from a pre-existing neurofibroma in NF1, so rapid growth or new pain in a neurofibroma signals possible malignant transformation.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — MPNST relies on VEGF-driven angiogenesis: like other aggressive sarcomas it secretes VEGF to vascularize its fast-growing mass, so anti-angiogenic tyrosine-kinase inhibitors are among the systemic options for this chemoresistant tumor.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — MPNST runs on the RAS-PI3K-mTOR axis: NF1 loss unleashes RAS, which fires PI3K-AKT-mTOR to drive growth, so mTOR inhibitors (often combined with MEK blockade) are tested against a sarcoma that resists standard chemotherapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages crowd MPNST and its precursor: plexiform neurofibromas are rich in macrophages and mast cells that feed an inflammatory niche promoting growth and malignant transformation, making this immune microenvironment a target.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — NF1 and NF2 split the nerve-tumor risk: NF1's neurofibromas can transform into MPNST, while NF2 instead causes schwannomas and meningiomas that rarely turn malignant—so the two syndromes demand different surveillance for nerve cancers.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — MPNST is fundamentally unleashed RAS: NF1's protein is a brake on RAS, so losing it lets KRAS/RAS-MAPK signaling run wild, transforming benign neurofibromas into this aggressive sarcoma—why MEK inhibitors are tested against it.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — MPNST progression hinges on losing the CDK4/6 brake: CDKN2A deletion removes the inhibitor of these cell-cycle kinases, letting the tumor divide unchecked—a hallmark of the leap from plexiform neurofibroma to malignancy.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — MPNST is studied as a target for NK and immune therapy: because it resists chemo and radiation, harnessing natural killer cells and the immune system is explored to attack this sarcoma where standard treatments fall short.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — MPNST spreads to the lungs above all: this aggressive nerve-sheath sarcoma metastasizes through the blood to seed pulmonary nodules, the dominant site of spread and a leading cause of death, so chest imaging guides staging.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia drives MPNST's aggressiveness: the fast-growing sarcoma outpaces its blood supply, and the low-oxygen microenvironment promotes invasion and resistance, part of why this nerve-sheath tumor responds poorly to radiation.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — MPNST largely escapes cytotoxic T cells: with an immunosuppressive, T-cell-poor microenvironment it resists checkpoint drugs, so engineered T-cell and combination immunotherapies are explored against a sarcoma that defies standard care.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — MPNST spreads through the blood to the liver: like other high-grade sarcomas it favors the lungs but also seeds the liver, marking the metastatic stage of this aggressive nerve-sheath cancer.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — MPNST recruits endothelial cells to grow: VEGF from the tumor drives these vessel-lining cells to build a blood supply for its rapid growth, a target of anti-angiogenic strategies.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — MPNST is a spindle-cell tumor woven with collagen: its fibroblast-like cells lay down a dense fibrous matrix, the firm fascicular tissue that, arising from a nerve, distinguishes it from benign neurofibromas.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals MPNST's nerve-sheath roots: scattered cells show schwannian differentiation — interdigitating processes wrapped in basal lamina — the ultrastructural clue to origin in a tumor that often loses its diagnostic S100 staining.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — MPNST exploits an IGF-1 loop: the tumor overexpresses the IGF-1 receptor, and autocrine insulin-like growth factor signaling fuels proliferation and survival — a pathway probed for therapy in a cancer that resists conventional treatment.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Losing NF1 unleashes AKT in MPNST: with neurofibromin gone, RAS activates the PI3K-AKT survival axis alongside MEK, so AKT signaling helps the tumor evade death — part of why dual-pathway blockade is being explored.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — MPNST favors the skeleton when it spreads: after the lungs, bone is a common metastatic site, with deposits in the marrow-bearing vertebrae and long bones marking the aggressive, hard-to-cure disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — MPNST can reach the brain: hematogenous metastases to the central nervous system, though less common than lung spread, are a grim development in this fast-growing nerve-sheath sarcoma.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — In NF1, MPNST often arises deep in the body: retroperitoneal and pelvic tumors grow against the bowel, the large intestine displaced or invaded by a sarcoma transforming from a plexiform neurofibroma.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody stains catch the transformation: loss of H3K27me3 by immunohistochemistry is an MPNST hallmark, and the patchy or absent S100 and SOX10 that once marked the Schwann cell fade as a benign neurofibroma turns malignant.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The chemotherapy taxes the marrow: the doxorubicin-and-ifosfamide regimens thrown at this aggressive sarcoma are strongly myelosuppressive, dropping neutrophil counts and making febrile neutropenia a recurring hazard of treatment.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — A changing lump under the skin is the warning: in NF1 an MPNST usually arises from a plexiform neurofibroma, so a deep mass that suddenly enlarges, hardens, or turns painful beneath the café-au-lait-marked skin demands urgent imaging and biopsy.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The sarcoma chemotherapy strains the heart: when MPNST is treated, the doxorubicin-ifosfamide backbone carries anthracycline cardiotoxicity, injuring cardiomyocytes and demanding cardiac monitoring through the limited chemo that this resistant tumor allows.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Most MPNSTs arise in NF1, which is inherited: the syndrome passes to half of a carrier's children, so a diagnosis prompts family genetic counseling, while the cytotoxic chemotherapy adds its own threat to fertility in these often-young patients.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Like other aggressive sarcomas it drives clotting: MPNST raises the risk of venous thromboembolism through paraneoplastic thrombocytosis and tumor procoagulants, complicating the major surgery its treatment requires.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — An upstream receptor feeds the runaway signaling: MPNST often overexpresses EGFR, pouring extra input into the RAS-MAPK pathway already unleashed by NF1 loss, and making the receptor a candidate target in a sarcoma stubbornly resistant to chemotherapy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The tumor builds an immune-cold niche: regulatory T cells and suppressive myeloid cells crowd the MPNST microenvironment and blunt T-cell attack, part of why single-agent checkpoint blockade has disappointed and combination immunotherapy is being tried.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Two neural-crest tumors meet at the Schwann-melanocyte line: MPNST and melanoma share the S100 and SOX10 lineage markers, and rare melanotic variants blur the boundary, reflecting their common origin in the migrating neural crest.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — New pain in a neurofibroma is the warning sign: malignant transformation to MPNST classically announces itself with rapid growth and worsening neuropathic pain along the nerve, the symptom that prompts urgent imaging and biopsy in NF1.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Growth-factor receptors feed the sarcoma: MPNST cells express PDGF receptors whose autocrine signaling drives proliferation, one of the receptor tyrosine kinases probed for targeted therapy in this treatment-resistant tumor.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 sustains the malignant Schwann cell: activated STAT3 signaling supports MPNST survival and the immunosuppressive microenvironment, marking another node in a tumor driven mainly by loss of NF1 and PRC2.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Loss of NF1 routes RAS into NF-κB: unrestrained RAS signaling in MPNST engages NF-κB-driven survival and inflammation, part of the network that makes this NF1-associated sarcoma so aggressive and treatment-resistant.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A bulky sarcoma that clots: MPNST carries tumor-driven hypercoagulability, and the major limb or trunk surgery and chemotherapy it requires add to the venous thromboembolism risk.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Intensive treatment and large tumors invite infection: the chemotherapy used against this aggressive sarcoma causes neutropenia, and extensive resections risk wound infection — both routes to sepsis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracycline scars the heart: the doxorubicin in MPNST chemotherapy is dose-dependently cardiotoxic, risking a cardiomyopathy and heart failure in survivors of this aggressive sarcoma.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemo neutropenia opens the lung to mold: the dose-intensive doxorubicin-ifosfamide regimens for MPNST cause deep neutropenia, letting inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An aggressive cancer on top of NF1 weighs on mood: MPNST's poor prognosis, disfiguring surgery and frequent arising in the burden of neurofibromatosis type 1 carry a substantial psychological toll.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Ifosfamide scars the kidney: the alkylator used in MPNST chemotherapy is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Radical resection and radiation heal badly: the wide excision of an MPNST, often with adjuvant radiation, leaves large soft-tissue wounds prone to dehiscence and slow healing.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Aggressive cancer and NF1 surveillance breed worry: the poor prognosis of MPNST and, in NF1 patients, the constant vigilance for malignant change in plexiform neurofibromas foster chronic health anxiety.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It spreads to the lungs: like other soft-tissue sarcomas, MPNST metastasises preferentially to the lungs, so pulmonary metastases dominate its surveillance and drive much of its mortality.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It erupts from a skin-associated nerve tumour: MPNST often arises within the plexiform neurofibromas of NF1, presenting as an enlarging, painful subcutaneous mass that signals malignant change.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its chemotherapy reawakens shingles: the doxorubicin-ifosfamide regimens for MPNST cause deep immunosuppression that allows latent varicella-zoster to reactivate.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its chemotherapy injures the kidney and bladder: the ifosfamide in MPNST regimens causes a Fanconi-like renal tubulopathy and haemorrhagic cystitis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its cure can scar the heart: the doxorubicin used against MPNST carries a dose-dependent cardiotoxicity risk on top of the disease's aggressive course.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It bypasses the lymph nodes: like other sarcomas, MPNST spreads haematogenously to the lungs and only rarely to lymph nodes, so it is staged differently from carcinomas.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It spreads through the bloodstream to the liver: MPNST metastasises haematogenously to the liver and lungs, and its chemotherapy brings nausea and mucositis.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Treatment suppresses immunity and biology invites it: intensive sarcoma chemotherapy is immunosuppressive, while MPNST is studied for immune and combination targeted therapy in NF1 patients.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — It is a target for pathway drugs: arising from NF1 loss with hyperactive RAS-MEK signalling, MPNST is investigated for MEK and other targeted inhibitors beyond standard sarcoma chemotherapy.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Sarcoma chemo for advanced disease: doxorubicin and ifosfamide, the standard soft-tissue sarcoma regimen, are used for unresectable or metastatic MPNST, though responses are limited.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — A fellow neural-crest tumour: like neuroblastoma, MPNST derives from neural-crest lineage, the two among the nerve-associated malignancies that arise in children and young adults.
- `connects-to` → **[Chordoma](../chordoma/README.md)** — A rare tumour where surgery and particle radiation lead: like chordoma, MPNST is a rare, radioresistant malignancy whose control depends on complete resection and high-dose proton or photon radiation.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Two tumours of the NF1 spectrum: neurofibromatosis type 1 predisposes both to malignant peripheral nerve sheath tumours and to pheochromocytoma, neural-crest-derived growths unleashed when neurofibromin no longer restrains RAS signalling.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — A poorly immunogenic sarcoma: malignant peripheral nerve sheath tumours have low mutational burden and respond little to PD-1 checkpoint inhibitors as monotherapy, so immunotherapy is investigated mainly in combinations for this chemoresistant cancer.
- `connects-to` → **[CMML](../cmml/README.md)** — One RAS pathway, blood and nerve: NF1 loss drives RAS-MAPK overactivity, predisposing not only to MPNST but to myeloid neoplasms—juvenile myelomonocytic and chronic myelomonocytic leukaemia—so neurofibromin links a nerve-sheath sarcoma to the marrow.
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — Convergent loss of H3K27me3: MPNST (via PRC2/SUZ12 loss) and diffuse midline glioma (via H3K27M) both erase the H3K27me3 repressive mark—two unrelated tumours sharing an epigenetic catastrophe diagnosed by its loss on staining.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Lung is the dominant metastatic site: MPNST spreads through the blood, preferentially seeding the lungs and the alveolar capillary bed, the pattern that dictates chest surveillance.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — It arises within a nerve: MPNST grows from a peripheral nerve (often a plexiform neurofibroma in NF1), destroying the axons it engulfs and heralded by rapid growth and new neurological deficit.
- `connects-to` → **[Desmoid Tumor](../desmoid-tumor/README.md)** — A fibroblastic differential: like MPNST, a desmoid tumour presents as a deep, infiltrative soft-tissue mass, and the two sit in the differential of an enlarging extremity or trunk lesion despite their very different biology and prognosis.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — NF1's two malignancies: neurofibromatosis type 1 predisposes to MPNST in peripheral nerves and to high-grade gliomas including glioblastoma in the CNS, both RAS-pathway-driven cancers of the syndrome.
- `connects-to` → **[H3K27M](../../03-molecular/h3k27m/README.md)** — Two routes to the same epigenetic loss: the H3K27M oncohistone of diffuse midline glioma and PRC2 (SUZ12/EED) inactivation in MPNST both abolish the repressive H3K27me3 mark, a convergence exploited diagnostically by loss of H3K27me3 staining.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Malignant transformation: MYC activation helps drive the progression of plexiform neurofibroma to MPNST, fuelling the proliferation of this aggressive sarcoma.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative immortality: TERT promoter activation maintains telomeres in MPNST, supporting the unlimited division of its transformed cells.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — MAPK amplification: NF1 loss unleashes RAS, and additional BRAF/MAPK-pathway activation further drives the RAS-RAF-MEK-ERK signalling central to MPNST.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: with CDKN2A loss frequent in MPNST, cyclin D1-CDK4/6 activity pushes these aggressive nerve-sheath tumour cells through the G1 checkpoint.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Receptor signalling: MET activation contributes to the growth and invasion of MPNST, a candidate targetable kinase in these treatment-resistant sarcomas.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the hypoxic MPNST drives the VEGF angiogenesis and metabolic adaptation that support its rapid, infiltrative growth.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Cell-cycle escape: RB1-pathway inactivation, with CDKN2A loss, marks the malignant transformation of plexiform neurofibroma to MPNST, releasing the brake on the cell cycle.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into MPNST, building the immunosuppressive stroma of this aggressive nerve-sheath sarcoma.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Apoptosis resistance: MPNST cells evade caspase-3-mediated apoptosis, contributing to the chemoresistance that makes these sarcomas so difficult to treat.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on MPNST cells follows CXCL12 gradients to the lung, the dominant site of the metastasis that is the principal cause of death in these aggressive nerve-sheath sarcomas arising in neurofibromatosis type 1.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — The plexiform neurofibromas from which MPNST arises are rich in KIT-dependent mast cells whose stem-cell-factor signaling supports the Schwann-cell tumor microenvironment and its progression toward malignancy.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates PI3K-AKT signaling during the progression of plexiform neurofibroma to MPNST, cooperating with the NF1-driven RAS hyperactivation and CDKN2A loss to drive the malignant transformation.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — Loss of PRC2 (EZH2/SUZ12) that abolishes H3K27 trimethylation is a defining MPNST event, and the accompanying DNA-methylation changes reshape the epigenome, marking the malignant transformation from neurofibroma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — MPNST is an aggressive sarcoma being explored for cellular and checkpoint immunotherapy, which would kill tumor cells through perforin and granzyme—a needed option given its poor response to chemotherapy.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — RAD51-mediated homologous-recombination repair helps MPNST survive radiation, a mechanism of the radioresistance that limits local control of these tumors, which themselves can arise in prior radiation fields.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — With CDKN2A loss and the RB pathway engaged (CDK4/6, cyclin-D1 and RB1 already mapped), E2F1 is released to drive the aggressive proliferation of malignant peripheral nerve sheath tumor.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — The RAS hyperactivation that follows NF1 loss also engages PI3K (AKT, mTOR and PTEN already mapped), a parallel growth-and-survival pathway in MPNST.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 amplification and TP53 loss (p53 mapped) contribute to the malignant transformation of a plexiform neurofibroma into MPNST.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) supports the survival and proliferation of malignant peripheral nerve sheath tumor cells.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the chemoresistance of MPNST.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling shapes the redox balance and treatment resistance of malignant peripheral nerve sheath tumor.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling modulates the invasion and immunosuppressive microenvironment of malignant peripheral nerve sheath tumor.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the invasion and survival of malignant peripheral nerve sheath tumor cells.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment relevant to immunotherapy in MPNST.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immunologically cold microenvironment of MPNST, a barrier to its immunotherapy.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the mesenchymal microenvironment and aggressive progression of the NF1-driven MPNST.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, antagonized by NF1-loss-driven RAS-PI3K-AKT signaling, modulate the survival of MPNST cells.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Wnt/β-catenin and survival signaling of the NF1-deficient cells of MPNST.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of the NF1-associated MPNST.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling downstream of receptor tyrosine kinases (EGFR, KIT, MET, and PDGFR already mapped) drives the invasive signaling of MPNST.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and therapy resistance of malignant peripheral nerve sheath tumor cells.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes, alongside PRC2 loss, to the epigenetic dysregulation of malignant peripheral nerve sheath tumor.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of malignant peripheral nerve sheath tumor.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of malignant peripheral nerve sheath tumor.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of malignant peripheral nerve sheath tumor.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — YAP1-Hippo signaling participates in the proliferation and mesenchymal biology of malignant peripheral nerve sheath tumor.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of malignant peripheral nerve sheath tumor.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of malignant peripheral nerve sheath tumor.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of malignant peripheral nerve sheath tumor.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of malignant peripheral nerve sheath tumor.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of malignant peripheral nerve sheath tumor.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the tumor microenvironment and invasion of malignant peripheral nerve sheath tumor.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunosurveillance: MHC class II antigen presentation shapes the T-cell response to malignant peripheral nerve sheath tumour, a chemoresistant sarcoma for which the loss of antigen presentation contributes to immune evasion.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Cellular immunotherapy: IL-2-driven T-cell expansion supports the adoptive-cell and vaccine approaches being explored for malignant peripheral nerve sheath tumour, which responds poorly to conventional chemotherapy.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint context: PD-1-mediated T-cell exhaustion limits anti-tumour immunity in the immunologically cold malignant peripheral nerve sheath tumour, and checkpoint blockade is being tested in combination for this aggressive sarcoma.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Chemotherapy anaemia: the doxorubicin-ifosfamide chemotherapy used for malignant peripheral nerve sheath tumour, which responds poorly, is myelosuppressive and lowers haemoglobin, the anaemia adding to the burden of this aggressive sarcoma.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the doxorubicin in sarcoma regimens for malignant peripheral nerve sheath tumour is cardiotoxic, and troponin elevation helps detect the cumulative myocardial injury of the anthracycline dose.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 helps make malignant peripheral nerve sheath tumour an immunologically cold sarcoma (PD-1 already mapped), dampening the T-cell response that combination checkpoint strategies aim to mount.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the cold, immune-evasive microenvironment of malignant peripheral nerve sheath tumour.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative microenvironment: the aggressive sarcoma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species (NRF2 already mapped) are part of the tumour microenvironment and treatment resistance.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of malignant peripheral nerve sheath tumour, part of the stromal biology of this aggressive sarcoma.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immunosuppressive microenvironment of the malignant peripheral nerve sheath tumour.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the myelosuppressive chemotherapy and the tumour burden of malignant peripheral nerve sheath tumour cause anaemia (haemoglobin already mapped) needing transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[Cortical bone](../../05-tissue/cortical-bone/README.md)** — Bone invasion: the aggressive malignant peripheral nerve sheath tumour invades the adjacent bone, and the paraspinal tumours can erode the vertebrae, part of its locally destructive behaviour.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Fibro-adipose adipokine: leptin from the fibro-adipose context of the plexiform neurofibroma from which MPNST arises signals to the tumour, part of its metabolic microenvironment.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Microenvironment adipokine: adiponectin, with leptin (already mapped), from the fibro-adipose microenvironment signals within the malignant peripheral nerve sheath tumour.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the microenvironment of malignant peripheral nerve sheath tumour.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment relevant to the emerging immunotherapy of malignant peripheral nerve sheath tumour.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune microenvironment of malignant peripheral nerve sheath tumour.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the immunosuppressive microenvironment of malignant peripheral nerve sheath tumour.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of malignant peripheral nerve sheath tumour.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the malignant peripheral nerve sheath tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the malignant peripheral nerve sheath tumour microenvironment.

[^evans-2002-mpnst-nf1]: Evans DGR, Baser ME, McGaughran J, et al. Malignant peripheral nerve sheath tumours in neurofibromatosis 1. *J Med Genet.* 2002;39(5):311-314. [doi:10.1136/jmg.39.5.311](https://doi.org/10.1136/jmg.39.5.311) · [PubMed 12011145](https://pubmed.ncbi.nlm.nih.gov/12011145/)
[^lee-2014-mpnst-prc2]: Lee W, Teckie S, Wiesner T, et al. PRC2 is recurrently inactivated through EED or SUZ12 loss in malignant peripheral nerve sheath tumors. *Nat Genet.* 2014;46(11):1227-1232. [doi:10.1038/ng.3095](https://doi.org/10.1038/ng.3095) · [PubMed 25240281](https://pubmed.ncbi.nlm.nih.gov/25240281/)
