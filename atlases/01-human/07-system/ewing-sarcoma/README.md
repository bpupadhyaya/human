---
schema: human-scale-entry/v1
id: ewing-sarcoma
name: Ewing Sarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Ewing sarcoma is an EWSR1-ETS fusion-driven small round blue cell tumor of bone/soft tissue; peak age 10-20 years; EWSR1-FLI1 ~85%; localized 5-year EFS ~60-70%; metastatic ~15-25%; VCD/IE or VIDE induction; local control by surgery ± RT; HDCT+auto-SCT for high-risk."
aliases: ["Ewing sarcoma", "ESFT", "Ewing's sarcoma", "primitive neuroectodermal tumor", "PNET bone", "EWS", "Ewing sarcoma family tumors", "extraskeletal Ewing"]
sources:
  - id: grier-2003-ewing-vdc-ie
    type: peer-reviewed
    cite: "Grier HE, Krailo MD, Tarbell NJ, et al. Addition of ifosfamide and etoposide to standard chemotherapy for Ewing's sarcoma and primitive neuroectodermal tumor of bone. N Engl J Med. 2003;348(8):694-701."
    doi: "10.1056/NEJMoa020890"
    pmid: "12594313"
    url: "https://doi.org/10.1056/NEJMoa020890"
  - id: ladenstein-2010-euro-ewing99-r3
    type: peer-reviewed
    cite: "Ladenstein R, Potschger U, Le Deley MC, et al. Primary disseminated multifocal Ewing sarcoma: results of the Euro-EWING 99 trial. J Clin Oncol. 2010;28(20):3284-3291."
    doi: "10.1200/JCO.2009.22.9864"
    pmid: "20498398"
    url: "https://doi.org/10.1200/JCO.2009.22.9864"
cross_links:
  - target: 01-human/03-molecular/ewsr1
    relation: connects-to
    note: "EWSR1-FLI1 t(11;22) (~85%) and EWSR1-ERG t(21;22) (~10%) are the defining fusions; EWSR1 break-apart FISH confirms rearrangement; RNA-seq specifies fusion partner; EWSR1-FLI1 activates GGAA microsatellite neo-enhancers driving a unique neuroectodermal program."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "EWSR1-FLI1 transcriptionally activates IGF1R → autocrine IGF loop → PI3K-AKT-mTOR → survival; mTOR inhibitors have modest single-agent activity in Ewing; dual IGF1R+mTOR inhibition explored; IGF1R antibodies (ganitumab) had ~10-15% ORR in R/R Ewing."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations are rare at Ewing diagnosis (<5%) but acquired in ~20-30% at relapse; CDKN2A/ARF deletion in ~15% primary Ewing; MDM2 amplification ~3%; idasanutlin (MDM2 inhibitor) + chemotherapy explored in pediatric solid tumors including R/R Ewing."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EWSR1-FLI1 activates IGF1R/RAS → ERK1/2 → Ewing survival and NKX2-2 transcription; RAS/MAPK pathway mutations (KRAS, NRAS, NF1) are acquired at relapse in ~30% Ewing; MEK inhibitors explored in refractory disease; ERK1/2 co-activates the neuroectodermal blast program."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss enhances IGF1R→PI3K-AKT signaling in Ewing; PTEN deletions uncommon at diagnosis but acquired at relapse; mTOR inhibitors + IGF1R antibodies show synergy in preclinical Ewing; PI3K/AKT/mTOR inhibitors (temsirolimus) explored in R/R Ewing and pediatric solid tumors."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A/ARF deletion in ~15% of primary Ewing sarcoma; ARF loss → MDM2 unchecked → p53 suppressed → apoptosis evasion; CDKN2A deletion co-occurs with poor histologic response; MDM2 inhibitors (idasanutlin) + VDC/IE under study; CDKN2A deletion acquired in ~25% at relapse."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ewing sarcoma is angiogenic; cabozantinib (VEGFR2+MET+RET) showed ORR ~20% in R/R Ewing; EWSR1-FLI1 upregulates VEGF expression; regorafenib (VEGFR+KIT) active in some R/R pediatric sarcomas; anti-angiogenic strategies combined with VEGFR inhibition under investigation."
  - target: 01-human/07-system/chordoma
    relation: connects-to
    note: "Ewing sarcoma and chordoma are both fusion/lineage-defined bone tumors but opposites: Ewing a fast small-round-blue-cell tumor of children driven by EWSR1-FLI1, chordoma a slow midline notochordal tumor of adults driven by TBXT — one genetic lesion specifying an entire sarcoma."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the most common metastatic site in Ewing sarcoma, and isolated pulmonary metastases carry a better prognosis than bone or marrow spread; whole-lung irradiation is added for lung-only metastatic disease, and metastasectomy of residual nodules is considered after chemo."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Ewing sarcoma and osteosarcoma are the two main pediatric bone cancers but differ fundamentally: osteosarcoma is an osteoid-producing tumor of the metaphysis, Ewing a small-round-cell tumor of the diaphysis driven by EWSR1-FLI1 — and unlike osteosarcoma, Ewing is radiosensitive."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Ewing sarcoma is a small-round-blue-cell malignancy of the musculoskeletal system: it arises in bone (pelvis, femur, ribs) or soft tissue of children and young adults with pain and a mass, driven by the EWSR1-FLI1 fusion rather than the osteoid production of osteosarcoma."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Ewing sarcoma and rhabdomyosarcoma are the two commonest pediatric small-round-blue-cell sarcomas and key differentials: both need molecular work-up—Ewing has EWSR1-FLI1 and CD99, rhabdomyosarcoma shows myogenic markers (desmin, myogenin) and PAX-FOXO1—since treatment differs."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ewing sarcoma is notably radiosensitive: unlike most bone sarcomas, radiotherapy is a primary local-control option (with surgery) for tumors in unresectable sites like the pelvis or spine, integrated with intensive multi-agent chemotherapy—photon/proton radiation exploits it."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Ewing sarcoma and neuroblastoma are both 'small round blue cell' childhood tumors that can look alike on biopsy but are biologically distinct: Ewing is driven by the EWSR1-FLI1 fusion in bone, neuroblastoma by MYCN-amplified sympathetic neuroblasts—IHC separates them."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Ewing sarcoma's cell of origin is debated between mesenchymal stem cells and the neural-crest/osteoblast lineage: unlike osteosarcoma it makes no bone matrix, so the EWSR1-FLI1 fusion—not an osteoblast program—defines it, arising within bone yet producing no osteoid."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Ewing sarcoma and Li-Fraumeni syndrome intersect at TP53: germline p53 loss in Li-Fraumeni predisposes to many sarcomas, and somatic TP53 mutation worsens Ewing's prognosis—both show how losing the genome's guardian fuels these aggressive bone and soft-tissue cancers."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone marrow involvement marks advanced Ewing sarcoma: this small round blue cell bone tumor can spread to the marrow, so staging includes marrow assessment and metastasis signals worse prognosis—why systemic chemotherapy is essential even for localized disease."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Ewing sarcoma's cell of origin is a debated mesenchymal progenitor: it likely arises from a mesenchymal or neural-crest cell related to fibroblasts, and the EWSR1-FLI1 fusion reprograms it into the aggressive small round blue cell tumor."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Ewing sarcoma and synovial sarcoma are both translocation-driven sarcomas of young people: Ewing carries EWSR1-FLI1 and synovial sarcoma SS18-SSX, single fusion oncogenes that define each tumor—so molecular testing for the specific fusion secures the diagnosis."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy benefits Ewing sarcoma, often in children: the tumor frequently sits in the pelvis or spine near growing tissue and organs, so protons' sharp dose falloff delivers curative radiation while limiting growth disturbance and second cancers in young patients."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "IGF-1 signaling helps drive Ewing sarcoma: the EWS-FLI1 fusion sensitizes tumor cells to IGF-1R, and although IGF-1R inhibitors gave only transient responses in trials, the pathway remains a key therapeutic target in this aggressive bone tumor."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Ewing sarcoma blurs into the nervous system as a small-round-blue-cell tumor: it shares neuroectodermal features with primitive neuroectodermal tumors (the Ewing family) and can arise in or compress nerves and spine—so neurological deficits can be a presenting sign."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Ewing sarcoma is an immunologically 'cold' tumor: its single EWS-FLI1 fusion creates few neoantigens and little immune infiltrate, so checkpoint inhibitors largely fail—driving research into vaccines and engineered cells to make the immune system see it."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Ewing sarcoma was once called diffuse endothelioma for its vascularity: the tumor is richly perfused and can form vessel-like channels, so its blood supply and VEGF-driven angiogenesis are features that anti-angiogenic strategies aim to exploit."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Ewing sarcoma can spread to the brain: although it favors lung and bone, late metastasis to the central nervous system occurs, so new neurological symptoms in advanced disease prompt brain imaging and change the treatment plan."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Ewing sarcoma eats through bone via osteoclasts: the tumor secretes signals that activate bone-resorbing osteoclasts, producing the destructive 'onion-skin' lytic lesions seen on X-ray, so osteoclast-blocking drugs are studied to limit skeletal damage."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Ewing sarcoma is a target for NK-cell immunotherapy: the tumor expresses little MHC, which normally exposes cells to natural killer attack, so NK-based and CAR therapies are being developed against this hard-to-cure childhood cancer."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Ewing sarcoma's bone destruction frees calcium: as osteolysis dissolves mineralized matrix it releases calcium, and widespread skeletal involvement can push blood calcium high—part of why the tumor's bone turnover is tracked during treatment."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia makes Ewing sarcoma more dangerous: low oxygen in the tumor amplifies the EWS-FLI1 program and pushes cells toward invasion and metastasis, so the oxygen-starved microenvironment helps explain its aggressive spread."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Ewing sarcoma resists cytotoxic T cells: with few mutations and little antigen display it is an immune-cold tumor, so engineered T-cell and CAR approaches are needed to direct killing where checkpoint drugs alone fall short."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages worsen Ewing sarcoma: infiltrating the bone tumor, they promote angiogenesis and immune suppression, and a macrophage-rich tumor tends to carry a poorer prognosis in this childhood cancer."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Ewing sarcoma carries a neural streak: it belongs to the primitive neuroectodermal tumor family, and its cells can show neuron-like differentiation, a clue to the embryonic precursor from which this bone-and-soft-tissue cancer springs."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Ewing sarcoma can spread to the liver: though it favors the lungs and other bones, widespread disease seeds visceral organs including the liver, marking the metastatic stage that sharply worsens survival."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Treating Ewing sarcoma can unleash potassium: chemotherapy bursting a large tumor causes tumor lysis, spilling potassium from dying cells and risking the hyperkalemia that can stop the heart."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Ewing sarcoma trades in phosphate: chemotherapy lysing the tumor spills phosphorus along with potassium, and the bone it eats away releases its calcium-phosphate mineral into the blood."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Ewing, a neural-flavored small-round-cell tumor, grows where it harms nerves: paraspinal and pelvic tumors compress nerve roots, causing the pain and weakness that often bring it to attention."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Ewing sarcoma has a skin-deep variant: rare superficial (cutaneous and subcutaneous) Ewing tumors form a nodule under the skin and carry a notably better prognosis than the deep bone disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy helps identify Ewing's small round blue cell: sparse organelles but abundant glycogen pools fill the cytoplasm, and rosette formation hints at the neural differentiation of this EWSR1-driven tumor."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "A retroperitoneal Ewing can press on the kidney, and chemotherapy threatens it: bursting the tumor in tumor lysis syndrome floods the blood with urate and phosphate that crystallize in the renal tubules."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Pelvic Ewing sarcoma crowds the bowel: tumors of the pelvis and sacrum grow against the rectum and colon, and the bulky mass can obstruct or displace the large intestine."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody pins down the diagnosis: Ewing sarcoma's cells stain strongly for CD99 (MIC2), and that membrane immunostain — confirmed by the EWSR1 fusion — distinguishes it from the other small round blue cell tumors."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Its chemotherapy wastes magnesium: ifosfamide, central to the Ewing regimen, injures the kidney's tubules into a Fanconi-like syndrome that spills magnesium and phosphate, demanding monitoring and replacement."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Curing a young patient threatens fertility: the alkylating chemotherapy and any pelvic radiation can wipe out the gonads, so sperm banking and ovarian preservation are discussed before treating these children and young adults."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The doxorubicin that cures it scars the heart: a backbone of Ewing chemotherapy, this anthracycline kills cardiomyocytes through oxidative and topoisomerase damage, so survivors carry a lifelong risk of cardiomyopathy from the cumulative dose."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "The fusion switches telomerase back on: EWS-FLI1 drives TERT expression, letting Ewing cells rebuild their telomeres and divide without limit — one of the ways the single fusion oncoprotein makes the tumor immortal."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Its alkylating drugs scar the bladder and seed later cancer: cyclophosphamide and ifosfamide release acrolein that causes hemorrhagic cystitis (blunted by mesna) and, over decades, raise the risk of secondary bladder cancer in survivors."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 keeps the fusion-driven cell alive: the EWS-FLI1 program activates STAT3 signaling that sustains Ewing proliferation and survival, a pathway probed for targeted therapy in this hard-to-treat sarcoma."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Ewing is an immunologically cold tumor: its low mutation burden and infiltrating regulatory T cells blunt the antitumor response, a barrier that the immunotherapy and CAR-T trials in Ewing must overcome."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "It sits among the small round blue cell tumors: like ATRT, neuroblastoma, and rhabdomyosarcoma, Ewing's sheets of small round blue cells force a differential resolved by its EWSR1 translocation and CD99 staining."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "The fusion drives the cell cycle: EWS-FLI1 transactivates cyclin D1, pushing Ewing cells past the G1 checkpoint — one of the proliferative programs the single oncoprotein switches on."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Immunotherapy must wake the cold tumor: dendritic-cell vaccines and approaches that boost antigen presentation are tested to mount a T-cell response against Ewing, whose few mutations give the immune system little to see."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Cure can sow a second cancer: the alkylating agents and topoisomerase inhibitors that treat Ewing damage the marrow, so survivors face a real risk of therapy-related myelodysplastic syndrome and secondary leukemia."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The fusion oncoprotein engages NF-κB: EWS-FLI1-driven Ewing cells show NF-κB-dependent survival and inflammatory signaling, one of the cooperating pathways explored as a target in this fusion-driven sarcoma."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Intensive chemo empties the marrow: the multidrug, dose-dense regimens that cure many Ewing sarcomas cause profound neutropenia, making febrile neutropenia and sepsis a recurrent treatment hazard."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A sarcoma and its treatment that clot: Ewing sarcoma raises thrombosis risk through tumor-driven hypercoagulability, compounded by central venous catheters and the immobility of intensive therapy and limb surgery."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its cure can sow a later leukemia: the alkylators and etoposide central to Ewing sarcoma therapy carry a real risk of therapy-related myelodysplasia and acute myeloid leukemia years after treatment."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracyclines scar the heart: the doxorubicin in Ewing sarcoma regimens is dose-dependently cardiotoxic, leaving survivors at risk of a cardiomyopathy and heart failure decades on."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Prolonged neutropenia opens the lung to mold: the deep neutropenia of dose-dense Ewing chemotherapy lets inhaled Aspergillus invade as pulmonary aspergillosis, a feared infection in these patients."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Vincristine and tumor injure the nerves: the vincristine in Ewing regimens causes peripheral neuropathy, and tumor near the spine or pelvis can compress nerves, together producing neuropathic pain."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Ifosfamide scars the young kidney: the alkylator central to Ewing chemotherapy is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment in treated children."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A bone cancer of the young with hard therapy weighs on mood: Ewing's diagnosis in children and young adults, amputation or limb-salvage surgery and grueling chemotherapy contribute to depression and distress."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Limb salvage and radiation heal poorly: the wide bone resection with endoprosthesis or amputation in Ewing sarcoma, in irradiated and chemotherapy-suppressed tissue, leaves wounds prone to breakdown."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Intensive chemo reawakens shingles: the dose-dense VDC/IE chemotherapy for Ewing sarcoma deeply suppresses a young patient's immunity, allowing latent or primary varicella-zoster to cause severe disease."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A young cancer with relapse risk breeds worry: the limb loss, lung-metastasis surveillance and long survivorship of Ewing sarcoma foster chronic anxiety in survivors and families."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "The lungs are its commonest target: Ewing sarcoma metastasises preferentially to the lungs, so chest imaging stages disease and pulmonary metastases are treated with whole-lung radiation."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its chemotherapy injures the kidney and bladder: ifosfamide causes a Fanconi-like renal tubulopathy, and cyclophosphamide and ifosfamide cause haemorrhagic cystitis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its cure can scar the heart: the doxorubicin in Ewing sarcoma chemotherapy carries a dose-dependent, long-term cardiotoxicity risk in the young survivors who receive it."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Treatment leaves lasting hormone effects: chemotherapy and radiation in childhood Ewing sarcoma impair growth, fertility and thyroid function in survivors."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Therapy hits the gut: the intensive multi-agent chemotherapy used against Ewing sarcoma causes severe nausea, mucositis and the risk of neutropenic colitis."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It and its treatment mark the skin: chemotherapy causes alopecia and mucositis, radiotherapy produces dermatitis over the treated bone, and rare cutaneous Ewing tumours occur."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Intensive chemo is curative: alternating vincristine-doxorubicin-cyclophosphamide with ifosfamide-etoposide, around surgery or radiation, cures most localised Ewing sarcoma."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A testbed for targeted drugs: Ewing sarcoma's IGF-1 dependence made it an early target for IGF-1R antibodies, and agents aimed at the EWSR1-FLI1 fusion are in development."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Cell therapy in trials: GD2- and other antigen-directed CAR-T and immunotherapies are being trialled for relapsed Ewing sarcoma, which resists conventional salvage treatment."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It is a bone tumour of the young: Ewing sarcoma arises in the diaphysis of long bones and the pelvis, destroying cortical bone with a permeative lytic pattern and the classic onion-skin periosteal reaction."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold sarcoma: Ewing sarcoma has a very low mutational burden and sparse T-cell infiltrate, so checkpoint inhibitors have shown little benefit, keeping chemotherapy and emerging cell therapies central."
  - target: 01-human/05-tissue/lung-slice
    relation: connects-to
    note: "It seeds the lungs: Ewing sarcoma metastasises preferentially to the lungs, where pulmonary metastases on a lung slice are staged by chest CT and treated with whole-lung irradiation."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Neuroectodermal character: Ewing sarcoma (once called PNET) shows neural differentiation and expresses neuronal markers, reflecting a neuroectodermal lineage despite arising in bone."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "A small-round-blue-cell mimic: Ewing sarcoma joins Burkitt lymphoma, neuroblastoma and rhabdomyosarcoma in the small-round-blue-cell tumour differential of childhood, distinguished by EWSR1 rearrangement."
  - target: 01-human/07-system/wilms-tumor
    relation: connects-to
    note: "Another childhood small-cell tumour: Wilms tumour and Ewing sarcoma are both paediatric malignancies treated on cooperative-group protocols, differentiated by site (kidney vs bone) and molecular markers."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Lung-predominant metastasis: Ewing sarcoma spreads chiefly to the lungs and bone, seeding the alveolar parenchyma—isolated pulmonary metastases carry a better prognosis than bone spread."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Chemotherapy cardiotoxicity: the anthracycline-heavy regimens (doxorubicin) that cure Ewing sarcoma can leave childhood survivors with a late cardiomyopathy of the myocardium."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Late second cancers: childhood Ewing survivors treated with radiation face raised risks of second malignancies, including breast cancer after chest irradiation and therapy-related leukaemia."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EWS-FLI1's epigenetic effector: the EWS-FLI1 fusion upregulates EZH2 to enforce the oncogenic, anti-differentiation chromatin programme of Ewing sarcoma, a candidate therapeutic target."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Fusion-driven oncogene: EWS-FLI1 activates MYC, whose proliferative transcriptional programme is essential to the rapid growth of Ewing sarcoma cells."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Plasticity and spread: Wnt/β-catenin signalling modulates EWS-FLI1 activity and promotes the phenotypic plasticity and metastasis that drive aggressive Ewing sarcoma."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival signalling: IGF-1R-driven PI3K/AKT signalling sustains Ewing sarcoma cell survival, cooperating with EWS-FLI1 and offering a combination therapeutic target."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Stromal growth factor: PDGF signalling, an EWS-FLI1 target, supports the autocrine growth and angiogenesis of Ewing sarcoma."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic aggression: HIF-1α stabilised in the hypoxic Ewing sarcoma enhances EWS-FLI1 activity and drives the angiogenesis and metastasis of more aggressive disease."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "BRCAness and PARP sensitivity: EWS-FLI1 impairs homologous recombination and RAD51 function, creating the 'BRCAness' that makes Ewing sarcoma sensitive to PARP inhibitors and DNA-damaging therapy."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Osteolytic destruction: Ewing sarcoma drives RANKL-mediated osteoclast activation to destroy the bone it arises in, the mechanism of the lytic lesions and pain of the disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the immunologically cold Ewing sarcoma, shaping a microenvironment that supports growth and resists immunotherapy."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic homing: CXCR4 on Ewing sarcoma cells follows CXCL12 gradients to the lung and bone, the principal sites of the metastasis whose presence at diagnosis is the dominant adverse prognostic factor."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Replication-stress immunity: the EWS-FLI1 fusion generates R-loops and replication stress that release cytosolic DNA capable of engaging cGAS-STING, intertwined with the 'BRCAness' that confers PARP-inhibitor sensitivity."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: Ewing sarcoma's intensive multi-agent chemotherapy kills tumour cells through caspase-3-mediated apoptosis, the effector step whose evasion underlies the relapses that follow initial response."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Immunotherapy: Ewing sarcoma expresses GD2 and other surface antigens, and GD2-directed CAR-T and other cellular therapies aim to kill the tumour through perforin and granzyme, an emerging approach against this immunologically cold sarcoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "Epigenetic reprogramming: the EWS-FLI1 fusion acts as a neomorphic transcription factor at GGAA microsatellites, reshaping the chromatin and DNA-methylation landscape — an epigenetic dependency that makes Ewing sarcoma a target for epigenetic therapy."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 restraint: Ewing sarcoma usually retains wild-type TP53 held in check by MDM2, so MDM2 inhibitors that reactivate p53 are a strategy to restore apoptosis in this genomically quiet, fusion-driven tumour."
---

# Ewing Sarcoma

## Overview

**Ewing sarcoma** is the second most common primary malignant bone tumor in children and young adults (after osteosarcoma), and the most common **soft tissue sarcoma** in the first decade of life. It belongs to the **Ewing Sarcoma Family of Tumors (ESFT)**, defined by chromosomal translocations fusing **EWSR1 (22q12)** to an **ETS family transcription factor** — most commonly FLI1 [t(11;22), ~85%] or ERG [t(21;22), ~10%] — creating a fusion oncoprotein that drives a pathological neuroectodermal transcriptional program. Ewing sarcoma is a **small round blue cell tumor (SRBCT)** with characteristic CD99+ immunophenotype and molecular confirmation required by FISH or RNA sequencing. Peak incidence occurs at ages 10-20 years; it is notably rare in African Americans (possibly due to GGAA microsatellite repeat frequency differences in African genomic backgrounds). Treatment is multimodal: **VCD/IE chemotherapy** (vincristine+cyclophosphamide+doxorubicin alternating with ifosfamide+etoposide), established as superior to VCD alone by the landmark INT-0091 trial [^grier-2003-ewing-vdc-ie], followed by **local control** (surgery, RT, or both) and consolidation; **high-risk/metastatic disease** benefits from **high-dose chemotherapy + autologous SCT** (Euro-EWING99: HDCT achieved 3-year EFS ~27% vs ~6% conventional consolidation in multifocal Ewing) [^ladenstein-2010-euro-ewing99-r3].

**Epidemiology:**
- ~250-300 cases/year in the USA; ~2,000-2,500/year globally
- Median age 15 years; second pediatric bone tumor peak (osteosarcoma is the first); rare after age 40
- Nearly exclusively affects people of European descent (~4:1 White:Black incidence; African Americans rarely develop Ewing)
- Slight male predominance (~1.5:1)
- Primary sites: diaphysis/metadiaphysis of long bones (~50%), pelvis (~25%), chest wall (~15%), spine (~10%)
- Extraskeletal Ewing (extraosseous): ~20% of all Ewing; same biology, management, prognosis as skeletal

## Structure

### Molecular landscape

**EWSR1-FLI1 t(11;22)(q24;q12) (~85%):**
Most common Ewing fusion; Type 1 (EWSR1 exon 7 – FLI1 exon 6) ~60%; Type 2 (EWSR1 exon 7 – FLI1 exon 5) ~25%; less common fusion types; EWSR1-FLI1 is virtually pathognomonic for Ewing sarcoma (distinguishes from other SRBCTs).

**EWSR1-ERG t(21;22)(q22;q12) (~10%):**
ERG is an ETS factor also involved in prostate cancer (ERG fusions via TMPRSS2); EWSR1-ERG and EWSR1-FLI1 drive nearly identical transcriptional programs (same ETS domain biology); clinically equivalent prognosis; both bind GGAA microsatellite neo-enhancers.

**Rare fusions (<5%):** EWSR1-ETV1, EWSR1-ETV4, EWSR1-FEV — all ETS family; similar but subtle biologic distinctions.

**EWSR1-negative Ewing-like sarcomas (now separate WHO entities):**
- **CIC-rearranged sarcoma** (CIC::DUX4, CIC::FOXO4): EWSR1 FISH negative; CD99 variable; more aggressive than Ewing
- **BCOR-rearranged sarcoma** (BCOR::CCNB3, BCOR::MAML3): EWSR1 FISH negative; bone/soft tissue; EFS inferior to typical Ewing
These are classified separately in WHO Classification of Soft Tissue and Bone Tumours 2020.

**Acquired mutations at relapse:**
RAS/MAPK pathway mutations (KRAS, NRAS, NF1, BRAF): ~30% at relapse; TP53 mutations: ~20-30% at relapse; CDKN2A deletion: ~15% primary Ewing; BRG1 (SMARCA4) loss: rare (<5%); chemotherapy resistance mediated largely through RAS/MAPK and p53 pathway derangements.

### Histology and immunophenotype

**Small round blue cells:** Uniform, tightly packed cells with round nuclei, finely dispersed chromatin, inconspicuous nucleoli, scant clear cytoplasm; no matrix production (absent osteoid or chondroid); sheets of cells without geographic necrosis (compared to central necrosis in osteosarcoma); Homer-Wright rosettes visible in PNET variant (attempt at neural-tube rosette formation).

**Immunophenotype:**
- **CD99 (MIC2):** ~95-100% strong membranous positivity — most sensitive marker; not specific (positive in T-LBL, synovial sarcoma, poorly differentiated synovial sarcoma)
- **NKX2-2:** ~90-95% nuclear positive — best available specific marker for Ewing (downstream EWSR1-FLI1 target); negative in most other SRBCTs
- **FLI1:** Nuclear positive (~85%) but also positive in vascular tumors (angiosarcoma, hemangioma) — specificity limited
- **Synaptophysin, CD56 (NCAM):** Variable (~50%); reflects neural crest/neuroectodermal origin
- **TdT:** Negative (distinguishes from T-LBL/lymphoma)
- **Desmin, myogenin:** Negative (distinguishes from rhabdomyosarcoma)

**Differential diagnosis of SRBCTs:**
- Ewing sarcoma
- Rhabdomyosarcoma (desmin+, myogenin+, FOXO1 or PAX3/7 fusions)
- Poorly differentiated synovial sarcoma (SS18-SSX fusion)
- Neuroblastoma (MYCN amp, TH+, synaptophysin+, neural features)
- Desmoplastic small round cell tumor (DSRCT, EWSR1-WT1, desmoplastic stroma)
- CIC-rearranged sarcoma

## Function

### Pathophysiology

**Ewing sarcoma cell of origin:**
Still debated; most evidence supports **mesenchymal stem cell** (bone marrow stromal/progenitor) as origin — EWSR1-FLI1 expression in MSC → reprogramming toward neuroectodermal state; some evidence for neural crest cell of origin in extraskeletal Ewing; key: the cell-of-origin must tolerate EWSR1-FLI1 without immediate apoptosis; in most cell types, forced EWSR1-FLI1 expression → massive apoptosis; MSCs are uniquely tolerant → selective outgrowth.

**EWSR1-FLI1 → NKX2-2 → arrested differentiation:**
The cardinal downstream event: EWSR1-FLI1 activates NKX2-2 from a GGAA microsatellite neo-enhancer ~60 kb upstream of NKX2-2 → NKX2-2 is a homeodomain TF that normally programs pancreatic β-cell and neural identity; in Ewing, NKX2-2 suppresses mesenchymal/adipogenic differentiation genes (PPARG, CEBPA) → arrests cells in a progenitor state; NKX2-2 is the single most diagnostic IHC marker for Ewing and the mechanistically central EWSR1-FLI1 target.

**IGF autocrine loop:**
EWSR1-FLI1 transcriptionally activates IGF1R and suppresses IGFBP3 (negative IGF regulator) → high free IGF2 + high IGF1R → constitutive IGF1R → JAK2/STAT5, PI3K-AKT-mTOR, MAPK → proliferation, survival, resistance to apoptosis; this loop is why IGF1R antibodies were tested (and showed partial activity) in Ewing.

## Pathology

### Staging

**ESFT staging (COG and EURO-EWING):**
- **Localized:** Primary tumor without distant metastases (~50-60% at diagnosis); includes tumors with local extension (soft tissue mass around bone, no distant mets)
- **Regional:** Pathologically involved regional lymph nodes (uncommon in bone primaries)
- **Metastatic:** Distant hematogenous metastases → lung (~40% of metastatic), bone (~30%), bone marrow (~10%), combinations; multiple bone/BM sites = "multifocal" (worst prognosis)
- **Extent of disease by site:** Pelvic primary → adverse (large, unresectable); axial primary → worse than extremity; pulmonary metastases only → intermediate prognosis; bone/BM metastases → poorest prognosis

### Treatment

**Induction chemotherapy (14-17 weeks):**
Two equivalent induction regimens (center-dependent):
- **VCD/IE (COG):** Vincristine+cyclophosphamide+doxorubicin (VCD) alternating with ifosfamide+etoposide (IE) every 2 weeks × 14 cycles total; 5-year EFS for localized disease: ~70%; addition of IE to VC+D improved 5-year EFS from ~54% to ~69% (INT-0091/Grier 2003) [^grier-2003-ewing-vdc-ie]; G-CSF support required for 14-day intervals
- **VIDE (EURO-EWING):** Vincristine+ifosfamide+doxorubicin+etoposide × 6 cycles (21-day) as induction; roughly equivalent outcomes; more ifosfamide per cycle

**Histologic response assessment:**
After induction → surgical specimen assessed for percent tumor necrosis (Salzer-Kuntschik grading or Huvos grading); **>90% necrosis = good histologic response** → independent favorable prognostic factor; poor response (<90% necrosis) → consider consolidation intensification or HDCT.

**Local control:**
- **Surgery (preferred if R0 achievable):** Wide resection with negative margins; reconstruction (endoprosthesis, allograft, recycled autograft); if R0 achieved → no additional RT required; R1/R2 resection → adjuvant RT
- **Definitive RT (for unresectable tumors):** 45-55.8 Gy involved-field RT; for spine/sacrum (unresectable sites); RT alone for local control inferior to surgery but achieves local control in ~70%
- **Combined surgery+RT:** For incomplete margins or specific anatomical sites (pelvis with soft tissue involvement)

**Consolidation:**
- **Localized, good response:** VCD/IE maintenance × additional 8-10 cycles → 5-year EFS ~70%; no HDCT for most localized good-response Ewing
- **Localized, poor response or high-risk features (pelvic, large tumor >200 mL):** Consider HDCT+auto-SCT (busulfan+melphalan myeloablative; some centers use treosulfan+melphalan to reduce hepatotoxicity)
- **Metastatic (pulmonary only):** Standard VCD/IE + local control + whole-lung irradiation (WLI, 15-18 Gy) → 5-year EFS ~25-35%; WLI significantly improves pulmonary EFS
- **Multifocal/disseminated metastatic:** Euro-EWING99-R3: HDCT (busulfan+melphalan) vs conventional therapy in primary disseminated multifocal Ewing → 3-year EFS 27% vs 6% (HR 0.60, p=0.005) [^ladenstein-2010-euro-ewing99-r3]; tandem HDCT exploring in worst-risk group

**Novel and investigational agents:**
- **TK216 (OBI-3424 analog):** EWS-FLI1-interfering agent; Phase 1/2: modest single-agent activity; Phase 2 ongoing
- **Olaparib + temozolomide:** HR deficiency rationale (EWSR1 loss reduces HR); pediatric Phase 1/2 (SARC024): ORR ~30% in relapsed Ewing
- **Anti-GD2 (dinutuximab):** GD2 expressed on Ewing; Phase 2 AEWS0821 (dinutuximab + VDC/IE): not superior to VDC/IE alone in localized disease; ongoing refinement in metastatic disease
- **Alisertib (AURKA):** Phase 2 in R/R pediatric solid tumors including Ewing: ORR ~10-20%
- **Cabozantinib (VEGFR/MET/RET):** Phase 2 in R/R Ewing: ORR ~20% (modest); some molecular responses
- **CAR-T (anti-GD2, anti-CD99):** Phase 1 trials; manufacturing challenges in pediatric patients

**Relapsed Ewing sarcoma:**
- If ≥12 months from prior ifosfamide/etoposide: topotecan+cyclophosphamide (TC) or irinotecan+temozolomide (IT); ORR ~30-40%
- If <12 months (early relapse): gemcitabine+docetaxel; ORR ~15-25%
- Overall salvage: 5-year OS <10-20% for relapsed metastatic Ewing; salvage surgery for isolated pulmonary relapse most likely to achieve cure
- Allo-SCT: some centers after second remission; limited data; associated with high TRM

### Long-term effects

- **Secondary malignancy:** RT field → secondary bone sarcoma (osteosarcoma, fibrosarcoma) in ~5% at 20 years; alkylator/etoposide → secondary AML/MDS
- **Infertility:** Cyclophosphamide+ifosfamide → gonadal damage; fertility preservation (sperm cryopreservation, oocyte preservation) strongly recommended before therapy
- **Orthopedic:** Endoprosthetic reconstruction → infection risk, mechanical failure at ~15-20 years; physeal damage from RT → limb length discrepancy
- **Pulmonary:** WLI → restrictive lung disease; bleomycin not used in Ewing (unlike older regimens)
- **Cardiac:** Doxorubicin → cardiomyopathy (standard cumulative dose limits ~375-450 mg/m²); cardiac surveillance post-therapy

## Connections

- `connects-to` → **[EWSR1](../../03-molecular/ewsr1/README.md)** — EWSR1-FLI1 t(11;22) (~85%) and EWSR1-ERG t(21;22) (~10%) are the defining fusions; EWSR1 break-apart FISH confirms rearrangement; RNA-seq specifies fusion partner; EWSR1-FLI1 activates GGAA microsatellite neo-enhancers driving a unique neuroectodermal program.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — EWSR1-FLI1 transcriptionally activates IGF1R → autocrine IGF loop → PI3K-AKT-mTOR → survival; mTOR inhibitors have modest single-agent activity in Ewing; dual IGF1R+mTOR inhibition explored; IGF1R antibodies (ganitumab) had ~10-15% ORR in R/R Ewing.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — TP53 mutations are rare at Ewing diagnosis (<5%) but acquired in ~20-30% at relapse; CDKN2A/ARF deletion in ~15% primary Ewing; MDM2 amplification ~3%; idasanutlin (MDM2 inhibitor) + chemotherapy explored in pediatric solid tumors including R/R Ewing.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EWSR1-FLI1 activates IGF1R/RAS → ERK1/2 → Ewing survival and NKX2-2 transcription; RAS/MAPK pathway mutations (KRAS, NRAS, NF1) are acquired at relapse in ~30% Ewing; MEK inhibitors explored in refractory disease; ERK1/2 co-activates the neuroectodermal blast program.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss enhances IGF1R→PI3K-AKT signaling in Ewing; PTEN deletions uncommon at diagnosis but acquired at relapse; mTOR inhibitors + IGF1R antibodies show synergy in preclinical Ewing; PI3K/AKT/mTOR inhibitors (temsirolimus) explored in R/R Ewing and pediatric solid tumors.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/ARF deletion in ~15% of primary Ewing sarcoma; ARF loss → MDM2 unchecked → p53 suppressed → apoptosis evasion; CDKN2A deletion co-occurs with poor histologic response; MDM2 inhibitors (idasanutlin) + VDC/IE under study; CDKN2A deletion acquired in ~25% at relapse.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Ewing sarcoma is angiogenic; cabozantinib (VEGFR2+MET+RET) showed ORR ~20% in R/R Ewing; EWSR1-FLI1 upregulates VEGF expression; regorafenib (VEGFR+KIT) active in some R/R pediatric sarcomas; anti-angiogenic strategies combined with VEGFR inhibition under investigation.
- `connects-to` → **[Chordoma](../chordoma/README.md)** — Ewing sarcoma and chordoma are both fusion/lineage-defined bone tumors but opposites: Ewing a fast small-round-blue-cell tumor of children driven by EWSR1-FLI1, chordoma a slow midline notochordal tumor of adults driven by TBXT — one genetic lesion specifying an entire sarcoma.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the most common metastatic site in Ewing sarcoma, and isolated pulmonary metastases carry a better prognosis than bone or marrow spread; whole-lung irradiation is added for lung-only metastatic disease, and metastasectomy of residual nodules is considered after chemo.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Ewing sarcoma and osteosarcoma are the two main pediatric bone cancers but differ fundamentally: osteosarcoma is an osteoid-producing tumor of the metaphysis, Ewing a small-round-cell tumor of the diaphysis driven by EWSR1-FLI1 — and unlike osteosarcoma, Ewing is radiosensitive.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Ewing sarcoma is a small-round-blue-cell malignancy of the musculoskeletal system: it arises in bone (pelvis, femur, ribs) or soft tissue of children and young adults with pain and a mass, driven by the EWSR1-FLI1 fusion rather than the osteoid production of osteosarcoma.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Ewing sarcoma and rhabdomyosarcoma are the two commonest pediatric small-round-blue-cell sarcomas and key differentials: both need molecular work-up—Ewing has EWSR1-FLI1 and CD99, rhabdomyosarcoma shows myogenic markers (desmin, myogenin) and PAX-FOXO1—since treatment differs.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ewing sarcoma is notably radiosensitive: unlike most bone sarcomas, radiotherapy is a primary local-control option (with surgery) for tumors in unresectable sites like the pelvis or spine, integrated with intensive multi-agent chemotherapy—photon/proton radiation exploits it.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Ewing sarcoma and neuroblastoma are both 'small round blue cell' childhood tumors that can look alike on biopsy but are biologically distinct: Ewing is driven by the EWSR1-FLI1 fusion in bone, neuroblastoma by MYCN-amplified sympathetic neuroblasts—IHC separates them.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Ewing sarcoma's cell of origin is debated between mesenchymal stem cells and the neural-crest/osteoblast lineage: unlike osteosarcoma it makes no bone matrix, so the EWSR1-FLI1 fusion—not an osteoblast program—defines it, arising within bone yet producing no osteoid.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Ewing sarcoma and Li-Fraumeni syndrome intersect at TP53: germline p53 loss in Li-Fraumeni predisposes to many sarcomas, and somatic TP53 mutation worsens Ewing's prognosis—both show how losing the genome's guardian fuels these aggressive bone and soft-tissue cancers.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone marrow involvement marks advanced Ewing sarcoma: this small round blue cell bone tumor can spread to the marrow, so staging includes marrow assessment and metastasis signals worse prognosis—why systemic chemotherapy is essential even for localized disease.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Ewing sarcoma's cell of origin is a debated mesenchymal progenitor: it likely arises from a mesenchymal or neural-crest cell related to fibroblasts, and the EWSR1-FLI1 fusion reprograms it into the aggressive small round blue cell tumor.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Ewing sarcoma and synovial sarcoma are both translocation-driven sarcomas of young people: Ewing carries EWSR1-FLI1 and synovial sarcoma SS18-SSX, single fusion oncogenes that define each tumor—so molecular testing for the specific fusion secures the diagnosis.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy benefits Ewing sarcoma, often in children: the tumor frequently sits in the pelvis or spine near growing tissue and organs, so protons' sharp dose falloff delivers curative radiation while limiting growth disturbance and second cancers in young patients.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1 signaling helps drive Ewing sarcoma: the EWS-FLI1 fusion sensitizes tumor cells to IGF-1R, and although IGF-1R inhibitors gave only transient responses in trials, the pathway remains a key therapeutic target in this aggressive bone tumor.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Ewing sarcoma blurs into the nervous system as a small-round-blue-cell tumor: it shares neuroectodermal features with primitive neuroectodermal tumors (the Ewing family) and can arise in or compress nerves and spine—so neurological deficits can be a presenting sign.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Ewing sarcoma is an immunologically 'cold' tumor: its single EWS-FLI1 fusion creates few neoantigens and little immune infiltrate, so checkpoint inhibitors largely fail—driving research into vaccines and engineered cells to make the immune system see it.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Ewing sarcoma was once called diffuse endothelioma for its vascularity: the tumor is richly perfused and can form vessel-like channels, so its blood supply and VEGF-driven angiogenesis are features that anti-angiogenic strategies aim to exploit.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Ewing sarcoma can spread to the brain: although it favors lung and bone, late metastasis to the central nervous system occurs, so new neurological symptoms in advanced disease prompt brain imaging and change the treatment plan.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Ewing sarcoma eats through bone via osteoclasts: the tumor secretes signals that activate bone-resorbing osteoclasts, producing the destructive 'onion-skin' lytic lesions seen on X-ray, so osteoclast-blocking drugs are studied to limit skeletal damage.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Ewing sarcoma is a target for NK-cell immunotherapy: the tumor expresses little MHC, which normally exposes cells to natural killer attack, so NK-based and CAR therapies are being developed against this hard-to-cure childhood cancer.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Ewing sarcoma's bone destruction frees calcium: as osteolysis dissolves mineralized matrix it releases calcium, and widespread skeletal involvement can push blood calcium high—part of why the tumor's bone turnover is tracked during treatment.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia makes Ewing sarcoma more dangerous: low oxygen in the tumor amplifies the EWS-FLI1 program and pushes cells toward invasion and metastasis, so the oxygen-starved microenvironment helps explain its aggressive spread.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Ewing sarcoma resists cytotoxic T cells: with few mutations and little antigen display it is an immune-cold tumor, so engineered T-cell and CAR approaches are needed to direct killing where checkpoint drugs alone fall short.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages worsen Ewing sarcoma: infiltrating the bone tumor, they promote angiogenesis and immune suppression, and a macrophage-rich tumor tends to carry a poorer prognosis in this childhood cancer.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Ewing sarcoma carries a neural streak: it belongs to the primitive neuroectodermal tumor family, and its cells can show neuron-like differentiation, a clue to the embryonic precursor from which this bone-and-soft-tissue cancer springs.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Ewing sarcoma can spread to the liver: though it favors the lungs and other bones, widespread disease seeds visceral organs including the liver, marking the metastatic stage that sharply worsens survival.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Treating Ewing sarcoma can unleash potassium: chemotherapy bursting a large tumor causes tumor lysis, spilling potassium from dying cells and risking the hyperkalemia that can stop the heart.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Ewing sarcoma trades in phosphate: chemotherapy lysing the tumor spills phosphorus along with potassium, and the bone it eats away releases its calcium-phosphate mineral into the blood.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Ewing, a neural-flavored small-round-cell tumor, grows where it harms nerves: paraspinal and pelvic tumors compress nerve roots, causing the pain and weakness that often bring it to attention.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Ewing sarcoma has a skin-deep variant: rare superficial (cutaneous and subcutaneous) Ewing tumors form a nodule under the skin and carry a notably better prognosis than the deep bone disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy helps identify Ewing's small round blue cell: sparse organelles but abundant glycogen pools fill the cytoplasm, and rosette formation hints at the neural differentiation of this EWSR1-driven tumor.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — A retroperitoneal Ewing can press on the kidney, and chemotherapy threatens it: bursting the tumor in tumor lysis syndrome floods the blood with urate and phosphate that crystallize in the renal tubules.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Pelvic Ewing sarcoma crowds the bowel: tumors of the pelvis and sacrum grow against the rectum and colon, and the bulky mass can obstruct or displace the large intestine.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody pins down the diagnosis: Ewing sarcoma's cells stain strongly for CD99 (MIC2), and that membrane immunostain — confirmed by the EWSR1 fusion — distinguishes it from the other small round blue cell tumors.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Its chemotherapy wastes magnesium: ifosfamide, central to the Ewing regimen, injures the kidney's tubules into a Fanconi-like syndrome that spills magnesium and phosphate, demanding monitoring and replacement.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Curing a young patient threatens fertility: the alkylating chemotherapy and any pelvic radiation can wipe out the gonads, so sperm banking and ovarian preservation are discussed before treating these children and young adults.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The doxorubicin that cures it scars the heart: a backbone of Ewing chemotherapy, this anthracycline kills cardiomyocytes through oxidative and topoisomerase damage, so survivors carry a lifelong risk of cardiomyopathy from the cumulative dose.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — The fusion switches telomerase back on: EWS-FLI1 drives TERT expression, letting Ewing cells rebuild their telomeres and divide without limit — one of the ways the single fusion oncoprotein makes the tumor immortal.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Its alkylating drugs scar the bladder and seed later cancer: cyclophosphamide and ifosfamide release acrolein that causes hemorrhagic cystitis (blunted by mesna) and, over decades, raise the risk of secondary bladder cancer in survivors.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 keeps the fusion-driven cell alive: the EWS-FLI1 program activates STAT3 signaling that sustains Ewing proliferation and survival, a pathway probed for targeted therapy in this hard-to-treat sarcoma.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Ewing is an immunologically cold tumor: its low mutation burden and infiltrating regulatory T cells blunt the antitumor response, a barrier that the immunotherapy and CAR-T trials in Ewing must overcome.
- `connects-to` → **[Atypical Teratoid/Rhabdoid Tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — It sits among the small round blue cell tumors: like ATRT, neuroblastoma, and rhabdomyosarcoma, Ewing's sheets of small round blue cells force a differential resolved by its EWSR1 translocation and CD99 staining.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — The fusion drives the cell cycle: EWS-FLI1 transactivates cyclin D1, pushing Ewing cells past the G1 checkpoint — one of the proliferative programs the single oncoprotein switches on.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Immunotherapy must wake the cold tumor: dendritic-cell vaccines and approaches that boost antigen presentation are tested to mount a T-cell response against Ewing, whose few mutations give the immune system little to see.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — Cure can sow a second cancer: the alkylating agents and topoisomerase inhibitors that treat Ewing damage the marrow, so survivors face a real risk of therapy-related myelodysplastic syndrome and secondary leukemia.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The fusion oncoprotein engages NF-κB: EWS-FLI1-driven Ewing cells show NF-κB-dependent survival and inflammatory signaling, one of the cooperating pathways explored as a target in this fusion-driven sarcoma.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Intensive chemo empties the marrow: the multidrug, dose-dense regimens that cure many Ewing sarcomas cause profound neutropenia, making febrile neutropenia and sepsis a recurrent treatment hazard.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A sarcoma and its treatment that clot: Ewing sarcoma raises thrombosis risk through tumor-driven hypercoagulability, compounded by central venous catheters and the immobility of intensive therapy and limb surgery.
- `connects-to` → **[AML](../aml/README.md)** — Its cure can sow a later leukemia: the alkylators and etoposide central to Ewing sarcoma therapy carry a real risk of therapy-related myelodysplasia and acute myeloid leukemia years after treatment.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracyclines scar the heart: the doxorubicin in Ewing sarcoma regimens is dose-dependently cardiotoxic, leaving survivors at risk of a cardiomyopathy and heart failure decades on.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Prolonged neutropenia opens the lung to mold: the deep neutropenia of dose-dense Ewing chemotherapy lets inhaled Aspergillus invade as pulmonary aspergillosis, a feared infection in these patients.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Vincristine and tumor injure the nerves: the vincristine in Ewing regimens causes peripheral neuropathy, and tumor near the spine or pelvis can compress nerves, together producing neuropathic pain.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Ifosfamide scars the young kidney: the alkylator central to Ewing chemotherapy is tubulotoxic, causing a Fanconi-type tubulopathy and lasting chronic kidney impairment in treated children.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A bone cancer of the young with hard therapy weighs on mood: Ewing's diagnosis in children and young adults, amputation or limb-salvage surgery and grueling chemotherapy contribute to depression and distress.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Limb salvage and radiation heal poorly: the wide bone resection with endoprosthesis or amputation in Ewing sarcoma, in irradiated and chemotherapy-suppressed tissue, leaves wounds prone to breakdown.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Intensive chemo reawakens shingles: the dose-dense VDC/IE chemotherapy for Ewing sarcoma deeply suppresses a young patient's immunity, allowing latent or primary varicella-zoster to cause severe disease.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A young cancer with relapse risk breeds worry: the limb loss, lung-metastasis surveillance and long survivorship of Ewing sarcoma foster chronic anxiety in survivors and families.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — The lungs are its commonest target: Ewing sarcoma metastasises preferentially to the lungs, so chest imaging stages disease and pulmonary metastases are treated with whole-lung radiation.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its chemotherapy injures the kidney and bladder: ifosfamide causes a Fanconi-like renal tubulopathy, and cyclophosphamide and ifosfamide cause haemorrhagic cystitis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its cure can scar the heart: the doxorubicin in Ewing sarcoma chemotherapy carries a dose-dependent, long-term cardiotoxicity risk in the young survivors who receive it.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Treatment leaves lasting hormone effects: chemotherapy and radiation in childhood Ewing sarcoma impair growth, fertility and thyroid function in survivors.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Therapy hits the gut: the intensive multi-agent chemotherapy used against Ewing sarcoma causes severe nausea, mucositis and the risk of neutropenic colitis.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It and its treatment mark the skin: chemotherapy causes alopecia and mucositis, radiotherapy produces dermatitis over the treated bone, and rare cutaneous Ewing tumours occur.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Intensive chemo is curative: alternating vincristine-doxorubicin-cyclophosphamide with ifosfamide-etoposide, around surgery or radiation, cures most localised Ewing sarcoma.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A testbed for targeted drugs: Ewing sarcoma's IGF-1 dependence made it an early target for IGF-1R antibodies, and agents aimed at the EWSR1-FLI1 fusion are in development.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Cell therapy in trials: GD2- and other antigen-directed CAR-T and immunotherapies are being trialled for relapsed Ewing sarcoma, which resists conventional salvage treatment.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It is a bone tumour of the young: Ewing sarcoma arises in the diaphysis of long bones and the pelvis, destroying cortical bone with a permeative lytic pattern and the classic onion-skin periosteal reaction.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold sarcoma: Ewing sarcoma has a very low mutational burden and sparse T-cell infiltrate, so checkpoint inhibitors have shown little benefit, keeping chemotherapy and emerging cell therapies central.
- `connects-to` → **[Lung Slice](../../05-tissue/lung-slice/README.md)** — It seeds the lungs: Ewing sarcoma metastasises preferentially to the lungs, where pulmonary metastases on a lung slice are staged by chest CT and treated with whole-lung irradiation.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Neuroectodermal character: Ewing sarcoma (once called PNET) shows neural differentiation and expresses neuronal markers, reflecting a neuroectodermal lineage despite arising in bone.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — A small-round-blue-cell mimic: Ewing sarcoma joins Burkitt lymphoma, neuroblastoma and rhabdomyosarcoma in the small-round-blue-cell tumour differential of childhood, distinguished by EWSR1 rearrangement.
- `connects-to` → **[Wilms Tumor](../wilms-tumor/README.md)** — Another childhood small-cell tumour: Wilms tumour and Ewing sarcoma are both paediatric malignancies treated on cooperative-group protocols, differentiated by site (kidney vs bone) and molecular markers.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Lung-predominant metastasis: Ewing sarcoma spreads chiefly to the lungs and bone, seeding the alveolar parenchyma—isolated pulmonary metastases carry a better prognosis than bone spread.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Chemotherapy cardiotoxicity: the anthracycline-heavy regimens (doxorubicin) that cure Ewing sarcoma can leave childhood survivors with a late cardiomyopathy of the myocardium.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Late second cancers: childhood Ewing survivors treated with radiation face raised risks of second malignancies, including breast cancer after chest irradiation and therapy-related leukaemia.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EWS-FLI1's epigenetic effector: the EWS-FLI1 fusion upregulates EZH2 to enforce the oncogenic, anti-differentiation chromatin programme of Ewing sarcoma, a candidate therapeutic target.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Fusion-driven oncogene: EWS-FLI1 activates MYC, whose proliferative transcriptional programme is essential to the rapid growth of Ewing sarcoma cells.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Plasticity and spread: Wnt/β-catenin signalling modulates EWS-FLI1 activity and promotes the phenotypic plasticity and metastasis that drive aggressive Ewing sarcoma.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Survival signalling: IGF-1R-driven PI3K/AKT signalling sustains Ewing sarcoma cell survival, cooperating with EWS-FLI1 and offering a combination therapeutic target.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Stromal growth factor: PDGF signalling, an EWS-FLI1 target, supports the autocrine growth and angiogenesis of Ewing sarcoma.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic aggression: HIF-1α stabilised in the hypoxic Ewing sarcoma enhances EWS-FLI1 activity and drives the angiogenesis and metastasis of more aggressive disease.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — BRCAness and PARP sensitivity: EWS-FLI1 impairs homologous recombination and RAD51 function, creating the 'BRCAness' that makes Ewing sarcoma sensitive to PARP inhibitors and DNA-damaging therapy.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Osteolytic destruction: Ewing sarcoma drives RANKL-mediated osteoclast activation to destroy the bone it arises in, the mechanism of the lytic lesions and pain of the disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the immunologically cold Ewing sarcoma, shaping a microenvironment that supports growth and resists immunotherapy.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on Ewing sarcoma cells follows CXCL12 gradients to the lung and bone, the principal sites of the metastasis whose presence at diagnosis is the single dominant adverse prognostic factor in the disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The EWS-FLI1 fusion generates R-loops and replication stress that release cytosolic DNA capable of engaging cGAS-STING, biology intertwined with the "BRCAness" that confers the PARP-inhibitor sensitivity of Ewing sarcoma.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Ewing sarcoma's intensive multi-agent chemotherapy kills tumor cells through caspase-3-mediated apoptosis, the effector step whose evasion underlies the relapses that follow an initially good response.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Ewing sarcoma expresses GD2 and other surface antigens, and GD2-directed CAR-T and other cellular therapies aim to kill the tumor through perforin and granzyme, an emerging approach against this immunologically cold sarcoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — The EWS-FLI1 fusion acts as a neomorphic transcription factor at GGAA microsatellites, reshaping the chromatin and DNA-methylation landscape—an epigenetic dependency that makes Ewing sarcoma a target for epigenetic therapy.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — Ewing sarcoma usually retains wild-type TP53 held in check by MDM2, so MDM2 inhibitors that reactivate p53 are a strategy to restore apoptosis in this genomically quiet, fusion-driven tumor.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^grier-2003-ewing-vdc-ie]: Grier HE, Krailo MD, Tarbell NJ, et al. Addition of ifosfamide and etoposide to standard chemotherapy for Ewing's sarcoma and primitive neuroectodermal tumor of bone. *N Engl J Med.* 2003;348(8):694-701. [doi:10.1056/NEJMoa020890](https://doi.org/10.1056/NEJMoa020890) · [PubMed 12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/)
[^ladenstein-2010-euro-ewing99-r3]: Ladenstein R, Potschger U, Le Deley MC, et al. Primary disseminated multifocal Ewing sarcoma: results of the Euro-EWING 99 trial. *J Clin Oncol.* 2010;28(20):3284-3291. [doi:10.1200/JCO.2009.22.9864](https://doi.org/10.1200/JCO.2009.22.9864) · [PubMed 20498398](https://pubmed.ncbi.nlm.nih.gov/20498398/)
