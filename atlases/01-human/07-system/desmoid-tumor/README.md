---
schema: human-scale-entry/v1
id: desmoid-tumor
name: Desmoid Tumor
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Desmoid tumor (aggressive fibromatosis) is a locally invasive spindle cell neoplasm; ~80% harbor CTNNB1 activating mutations; no metastatic potential; nirogacestat (gamma-secretase inhibitor, DeFi trial) FDA-approved 2023; sorafenib active; watch-and-wait for stable disease."
aliases: ["desmoid tumor", "aggressive fibromatosis", "desmoid fibromatosis", "deep fibromatosis", "desmoid CTNNB1", "FAP desmoid", "mesenteric fibromatosis", "sporadic desmoid", "beta-catenin fibromatosis", "APC desmoid"]
sources:
  - id: gounder-2023-nirogacestat-desmoid
    type: peer-reviewed
    cite: "Gounder M, Ratan R, Alcindor T, et al. Nirogacestat, a gamma-secretase inhibitor, for desmoid tumors. N Engl J Med. 2023;388(10):898-912."
    doi: "10.1056/NEJMoa2209457"
    pmid: "36884316"
    url: "https://doi.org/10.1056/NEJMoa2209457"
  - id: lazar-2008-ctnnb1-desmoid
    type: peer-reviewed
    cite: "Lazar AJ, Tuvin D, Hajibashi S, et al. Specific mutations in the beta-catenin gene (CTNNB1) correlate with local recurrence in sporadic desmoid tumors. Am J Pathol. 2008;173(5):1518-1527."
    doi: "10.2353/ajpath.2008.080475"
    pmid: "18832571"
    url: "https://doi.org/10.2353/ajpath.2008.080475"
cross_links:
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "CTNNB1 activating mutations (S45F, T41A, S33C) in ~80% sporadic desmoid tumors → nuclear β-catenin → TCF/LEF-dependent transcription → MYC, CCND1 → desmoid fibroblast proliferation; APC germline mutations (FAP) account for ~20%; CTNNB1 T41A predicts best prognosis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CTNNB1 encodes β-catenin, the terminal Wnt effector; Wnt → LRP5/6 + FZD → Axin/APC complex inhibition → β-catenin stabilization → nuclear translocation → TCF/LEF co-activator; activating CTNNB1 mutations mimic Wnt-ON state regardless of ligand; Wnt+CTNNB1 mutation = maximum Wnt."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Nirogacestat (gamma-secretase inhibitor) blocks Notch signaling → NICD1 suppression → desmoid cell apoptosis; DeFi Phase 3: ORR 41% vs 8% placebo, PFS HR 0.29; FDA-approved November 2023; Notch-Wnt crosstalk amplifies CTNNB1-driven desmoid proliferation."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "CTNNB1/β-catenin activates VEGFA transcription via TCF/LEF elements → tumor angiogenesis in desmoid and colorectal cancer; VEGF blockade (bevacizumab) explored in desmoid tumor trials; VEGFR/PDGFR inhibitor sorafenib achieves ORR ~15% in desmoid (DESMOID Phase 2, PFS HR 0.13)."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "APC germline truncating mutations (codons 1310-2011) cause FAP; ~20% of desmoid tumors arise in FAP via APC LOF → insufficient β-catenin destruction → nuclear β-catenin → Wnt targets; FAP mesenteric desmoid is the leading non-cancer cause of death post-colectomy in FAP patients."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "FAP (germline APC) carries ~10-20% lifetime desmoid tumor risk; FAP mesenteric desmoid is the leading non-cancer cause of mortality in post-colectomy FAP; laparotomy wound triggers mesenteric desmoid; prophylactic sulindac and close surveillance are standard at FAP centers."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Desmoid tumor arises from fibroblastic/myofibroblastic progenitors in CTNNB1-mutant cells triggered by trauma or surgery; desmoid myofibroblasts (αSMA+, nuclear β-catenin) secrete dense collagen and resist apoptosis; TGF-β amplifies myofibroblastic activation in desmoid stroma."
  - target: 01-human/07-system/gist
    relation: connects-to
    note: "Desmoid tumors and GISTs are intra-abdominal mesenchymal tumors often confused on imaging but molecularly opposite: desmoid is a non-metastasizing fibroblastic proliferation driven by CTNNB1/APC-Wnt, while GIST is a KIT/PDGFRA-driven Cajal-cell tumor that can metastasize."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Mesenteric desmoid tumors arise in the small-bowel mesentery, especially after abdominal surgery in FAP, encasing mesenteric vessels and bowel; this infiltrative, non-metastasizing growth causes obstruction, ischemia, and fistulae — a leading non-cancer cause of death in FAP."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Extra-abdominal desmoids (aggressive fibromatosis) of the shoulder, abdominal wall, and limbs are locally infiltrative soft-tissue tumors that recur after resection but never metastasize; since surgery often triggers regrowth, surveillance and systemic drugs are first-line."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Desmoid tumors are a hallmark of familial adenomatous polyposis (Gardner syndrome), the same APC/Wnt disorder that causes colorectal cancer: ~10-15% of FAP patients develop desmoids, often intra-abdominal and triggered by colectomy, where they become a leading cause of death."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Desmoid tumors are frequently hormone-responsive: many express estrogen receptors, can grow during pregnancy or with oral contraceptives and regress after menopause, so anti-estrogens (tamoxifen) with NSAIDs are an established option for these non-metastasizing fibromatoses."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Desmoid tumors are driven by a profibrotic program in which TGF-β is central: alongside constitutive Wnt/β-catenin, TGF-β stimulates myofibroblasts to lay down the dense collagenous matrix that makes desmoids infiltrative and locally destructive—the hallmark of fibromatosis."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Desmoid tumor and synovial sarcoma are both deep soft-tissue tumors but biologically apart: desmoid is a locally aggressive fibroblastic proliferation driven by CTNNB1/Wnt that never metastasizes, while synovial sarcoma is a malignant SS18-SSX sarcoma that does."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Desmoid tumor and Ewing sarcoma both arise in young people but differ: desmoid is a non-metastasizing fibromatosis often managed by active surveillance, whereas Ewing is an aggressive EWSR1-FLI1 small-round-cell sarcoma needing intensive chemo and radiation."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Desmoid tumors are linked to the reproductive system through estrogen and pregnancy: many are estrogen-responsive and can grow during or after pregnancy, and abdominal-wall desmoids classically follow childbirth—so hormonal therapy is one treatment option."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Desmoid tumors are collagen-rich fibromatoses, not true sarcomas: clonal myofibroblasts driven by beta-catenin lay down dense collagen, producing an infiltrative but non-metastasizing mass—locally aggressive yet unable to spread, shaping conservative treatment."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cyclin D1 links desmoid's Wnt driver to growth: stabilized beta-catenin (from CTNNB1 or APC mutation) switches on cyclin D1, pushing myofibroblasts through the cell cycle—the Wnt/cyclin-D1 axis behind colon cancer here yields a benign-behaving but relentless tumor."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF signaling offers a therapeutic handle in desmoid tumors: these fibromatoses express PDGFR, so multitargeted tyrosine-kinase inhibitors (sorafenib, imatinib) shrink or stabilize them—part of the shift from surgery toward systemic and watchful-waiting management."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is one option for unresectable desmoid tumors: though benign, desmoids invade locally and recur after surgery, so photon-beam radiation can control disease when an operation would be mutilating—balanced against radiation's own risks in young patients."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Desmoid tumors have a special affinity for the abdomen and gut: in FAP/Gardner syndrome they arise in the mesentery and abdominal wall, where they can encase and obstruct the bowel and its vessels—making intra-abdominal desmoids a leading cause of death in FAP."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Desmoid tumors sit in the soft-tissue-mass differential with sarcomas like rhabdomyosarcoma: desmoids are locally aggressive but never metastasize, while rhabdomyosarcoma is frankly malignant—so biopsy distinguishes a benign fibromatosis from a deadly sarcoma."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The desmoid tumor cell is a myofibroblast: it blends fibroblast and smooth-muscle features, expressing actin as it contracts and invades locally, so although benign and non-metastasizing, its smooth-muscle-like infiltration makes desmoids hard to fully excise."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Desmoid tumors are estrogen-sensitive and tied to pregnancy: many abdominal-wall desmoids appear during or after pregnancy as estrogen drives their growth, so they often arise near the gravid uterus and may regress after delivery or with anti-estrogens."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Desmoid is a fibromatosis—benign but relentlessly fibrotic: clonal myofibroblasts lay down dense collagen that infiltrates muscle and fascia, so it behaves like an aggressive scar, distinguishing it from both reactive fibrosis and true sarcoma."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Desmoid tumors can be reined in through mTOR: the same β-catenin and growth signaling that drives them feeds into the PI3K-AKT-mTOR axis, so mTOR inhibitors like sirolimus are used to shrink these locally aggressive fibromatoses that won't metastasize."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Desmoid tumors are seeded with mast cells: these immune cells populate the fibromatosis stroma and release mediators that may spur fibroblast growth, part of the inflammatory microenvironment shaping how aggressively a desmoid behaves."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages help build the desmoid's stroma: tumor-associated macrophages infiltrate the fibrous mass and secrete growth factors that drive the relentless local proliferation of myofibroblasts characteristic of these tumors."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Desmoids also lean on PI3K-AKT growth signaling: alongside the driving Wnt/beta-catenin lesion, AKT-mTOR activity sustains the myofibroblast proliferation, which is why mTOR-pathway drugs have been tried in these locally aggressive fibrous tumors."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Desmoids are immune-cold tumors with few cytotoxic T cells: their dense collagen stroma keeps killer T cells sparse, helping explain why checkpoint immunotherapy has little effect and why treatment instead targets Wnt and growth signals."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "The desmoid's dense fibrous core runs low on oxygen: as the mass outgrows its blood supply it turns hypoxic, stabilizing HIF and driving the VEGF-fueled angiogenesis that lets the relentless fibromatosis keep expanding."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Mesenteric desmoids strangle the bowel: especially in FAP, these fibrous tumors grow through the mesentery and encase the intestine, obstructing the gut and threatening the vessels and ureters around it."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Abdominal desmoids can choke the kidneys: a growing mesenteric mass compresses the ureters, backing urine up into the kidneys (hydronephrosis) and threatening renal function, a feared complication of FAP-associated desmoids."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Desmoids weave a dense matrix of fibronectin: their myofibroblasts pour out fibronectin and collagen to build the tough fibrous stroma that gives the tumor its hardness and infiltrative grip on surrounding tissue."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Desmoids recruit new vessels: VEGF draws endothelial cells to feed the slowly expanding fibrous mass, and anti-angiogenic agents are among the systemic options tried for unresectable tumors."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Desmoids ensnare nerves: the infiltrative fibrous mass wraps and compresses adjacent peripheral nerves, causing the pain and neurological deficits that often drive treatment of an otherwise benign tumor."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Abdominal-wall desmoids surface beneath the skin: they present as a deep, firm mass, classically in women after childbirth or along old surgical scars, the commonest sporadic site."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the desmoid's working cell: the myofibroblast, a fibroblast-smooth-muscle hybrid bristling with rough endoplasmic reticulum and actin bundles, churning out the dense collagen that makes these tumors so firm and infiltrative."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Chest-wall desmoids invade toward the lung: arising in the thoracic wall they grow inward against the pleura and mediastinum, and although they never metastasize, their relentless local spread can compress the chest's contents."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Desmoids gnaw the bone they abut: though purely soft-tissue tumors, their infiltrative growth can erode the cortex of adjacent bone, a sign of how aggressively they invade despite never spreading distantly."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Desmoids entrap the nerves they grow around: their infiltrative edge encases peripheral nerves, causing pain, numbness, and weakness, and making surgery risky for the nerve as much as for the recurrence-prone tumor."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "An intra-abdominal desmoid can throttle the gut: mesenteric tumors — common in familial adenomatous polyposis — compress the stomach and bowel into obstruction, and can encase the mesenteric vessels feeding them."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Desmoids arise amid the body's fat and fascia: springing from the fibrous tissue of the abdominal wall and the fat-rich mesentery, they must be told apart from the benign lipoma and malignant liposarcoma that share that home."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Pregnancy can stir desmoids: many appear or grow during gestation and abdominal-wall desmoids especially, then often stabilize or regress after delivery, a hormone sensitivity to estrogen and progesterone that underlies the anti-hormonal therapies sometimes tried."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Pressing on bone, the desmoid remodels it: extra-abdominal tumors abutting the chest wall or limb girdle scallop the cortex and provoke periosteal new bone from osteoblasts, the bony reaction that imaging picks up at the tumor's edge."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Mesenteric desmoids crowd the upper abdomen: in FAP they grow at the root of the mesentery and can encase the duodenum and pancreas, complicating surgery and sometimes obstructing the bowel or bile drainage."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Desmoids favor sites of injury: they classically arise in surgical scars, including after breast surgery, so a firm mass at a mastectomy or reconstruction site can be a desmoid rather than recurrent cancer."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "An immune-cell milieu shapes the tumor: regulatory T cells populate the desmoid microenvironment, part of the stromal-immune context being explored as these locally aggressive fibromatoses resist conventional treatment."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation feeds the fibromatosis: IL-6 and prostaglandin signaling promote desmoid fibroblast growth, a rationale behind the anti-inflammatory NSAIDs long tried to slow these tumors."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "A desmoid is wound healing that won't switch off: it is a clonal myofibroblast proliferation that classically erupts at sites of surgery, trauma, or pregnancy, as if the repair program ran unchecked under activated β-catenin."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "YAP partners with β-catenin in the desmoid: Hippo-pathway YAP activation cooperates with the driving Wnt/β-catenin signal to sustain the fibroblast proliferation, marking another node studied as a therapeutic target."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Desmoids cluster with the FAP cancers: arising from the same APC loss, they accompany the colorectal and upper-GI tumors of familial adenomatous polyposis, where fundic-gland and gastric neoplasia round out the syndrome's GI risk."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 feeds the fibromatosis through STAT3: the inflamed desmoid stroma's IL-6 activates STAT3, adding a proliferative signal alongside the driving Wnt/β-catenin pathway in this locally aggressive tumor."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "A retroperitoneal mass can strangle the ureters: large mesenteric or retroperitoneal desmoids compress the ureters into hydronephrosis, and prolonged obstruction can erode kidney function toward chronic kidney disease."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Bulky abdominal tumors compress the veins: mesenteric desmoids can obstruct venous return, and the major surgery they sometimes require adds to the risk of deep-vein thrombosis."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Infiltrating fibrosis traps the nerves: desmoid tumors invade locally and compress or encase nerves, causing chronic neuropathic pain that is often the dominant symptom of these aggressive but non-metastasizing growths."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Abdominal desmoids can breach the bowel: mesenteric tumors and their resection can cause bowel obstruction, fistula or perforation, spilling gut flora into the abdomen and seeding sepsis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A relentless, recurring tumor wears on the mind: chronic pain, disfigurement and the high recurrence of desmoid tumors despite their benign label carry a substantial psychological burden and depression."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its targeted drugs strain the heart: the sorafenib and other tyrosine-kinase inhibitors used to control aggressive desmoid tumors raise blood pressure and are cardiotoxic, risking heart failure."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "A large infiltrative tumor drains the blood: bulky mesenteric or abdominal desmoids with their inflammatory burden, and any associated bleeding, can produce an anemia of chronic disease."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Unpredictable recurrence breeds worry: the locally aggressive, frequently recurring behavior of desmoid tumors and the need for ongoing imaging surveillance foster chronic health anxiety."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is fuelled by oestrogen: desmoid tumours often grow during pregnancy and with the contraceptive pill and express oestrogen receptors, so anti-oestrogens like tamoxifen are used to treat them."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Mesenteric tumour can throttle the ureters: a bulky intra-abdominal desmoid, common in FAP, can encase and obstruct the ureters, causing hydronephrosis and threatening kidney function."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It arises in the abdominal wall and skin: desmoid tumours frequently grow in the abdominal-wall soft tissue, and in Gardner syndrome accompany epidermoid cysts and other cutaneous lesions."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It wraps around the great vessels: intra-abdominal and mesenteric desmoids encase and compress mesenteric arteries, the aorta and IVC, risking bowel ischaemia and vascular obstruction."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It infiltrates around the nerves: desmoid tumours grow into and compress nerves and nerve roots, causing pain and neurological deficits, and their resection risks nerve injury."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Mesenteric tumours block lymph flow: a mesenteric desmoid can obstruct lymphatic drainage, causing chylous ascites, on top of the bowel and ureteric compression it produces."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can grow in the chest: thoracic and chest-wall desmoid tumours can encase the ribs and compress the lung, and mesenteric disease can press on the diaphragm."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "Anti-inflammatories can hold it back: NSAIDs such as sulindac, in the same class as ibuprofen, are used to slow desmoid growth, sometimes with anti-oestrogens, before resorting to surgery or systemic therapy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It builds an inflammatory stroma: desmoid tumours carry a fibroinflammatory microenvironment rich in immune cells, and their indolent, sometimes self-regressing behaviour has drawn interest in immune modulation."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A new drug targets its pathway: nirogacestat, a gamma-secretase inhibitor of Notch, and multikinase inhibitors (sorafenib, pazopanib) shrink progressive desmoid tumours that exploit Wnt/β-catenin signalling."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Low-dose chemo controls progression: regimens like methotrexate-vinblastine or liposomal doxorubicin treat progressive or symptomatic desmoid tumours unsuitable for surgery."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Both flag familial polyposis: desmoid tumours and cribriform-morular thyroid carcinoma are extracolonic manifestations of familial adenomatous polyposis, sharing its APC/Wnt-pathway driver."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "It strangles the bowel: in FAP/Gardner syndrome, mesenteric desmoid tumours encase and obstruct the small intestine and its vessels, a leading cause of death after colectomy despite being histologically benign."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It erodes adjacent bone: though non-metastasising, aggressive desmoid fibromatosis infiltrates muscle and fascia and can scallop and erode the cortical bone it abuts, driving pain and local destruction."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Two faces of fibroblast overgrowth: desmoid is a clonal neoplastic proliferation of myofibroblasts laying down collagen, whereas systemic sclerosis is autoimmune-driven fibroblast activation — different triggers converging on excess fibrous tissue."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "The FAP/Turcot connection: APC-mutant familial adenomatous polyposis predisposes to both desmoid tumours and medulloblastoma (Turcot syndrome), two Wnt-pathway lesions of one germline defect."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It encases the great vessels: intra-abdominal desmoids in FAP infiltrate the mesentery, encasing and compressing the mesenteric arteries and causing the bowel ischaemia that makes them lethal."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Obstruction backs up to the kidney: a mesenteric or pelvic desmoid can compress the ureters, and the resulting hydronephrosis backs pressure up to the glomerulus, threatening renal function."
  - target: 01-human/07-system/mutyh-associated-polyposis
    relation: connects-to
    note: "Polyposis and desmoids: desmoid tumours are a hallmark of APC-driven FAP/Gardner syndrome; MUTYH-associated polyposis phenocopies FAP's colorectal polyposis but rarely produces desmoids, a distinguishing feature."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Shared Wnt activation: desmoid tumours and a subset of hepatocellular carcinomas are both driven by activating CTNNB1 (β-catenin) mutations, the same Wnt pathway producing very different tumours."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "Benign-but-aggressive vs malignant: desmoid fibromatosis invades locally but never metastasizes, contrasting with malignant soft-tissue sarcomas like MPNST that both invade and spread distantly."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "NSAID-responsive growth: prostaglandins promote desmoid proliferation, the rationale behind treating these tumours with COX inhibitors such as sulindac and other NSAIDs."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Kinase target: desmoids express KIT and PDGFR receptors, underpinning the partial responses seen with tyrosine kinase inhibitors like imatinib in progressive disease."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Replicative persistence: telomerase activity helps desmoid cells sustain the relentless, locally invasive proliferation that makes these benign tumours so difficult to control."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Wnt target oncogene: nuclear β-catenin in desmoid tumours drives transcription of MYC, helping sustain the proliferative, locally aggressive fibromatosis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle entry: β-catenin-driven cyclin D1 activates CDK4/6 to push desmoid fibroblasts through the G1 checkpoint, the engine of their relentless growth."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic stroma: the dense, poorly vascularised desmoid matrix becomes hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis that supports continued expansion."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Fibroblast growth signal: IGF-1/IGF-1R signalling supports the proliferation and survival of the myofibroblasts that make up desmoid tumours, cooperating with the driving Wnt-β-catenin pathway."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK proliferation: RAF-MEK-ERK signalling drives desmoid fibroblast proliferation, part of why the multi-kinase inhibitor sorafenib produces durable responses in aggressive fibromatosis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Stromal macrophages: CCL2 recruits macrophages into the desmoid stroma, contributing to the inflammatory, matrix-remodelling microenvironment of these locally aggressive fibrous tumours."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Destruction-complex escape: GSK-3β, with APC and Axin, normally phosphorylates β-catenin for degradation, so the CTNNB1 and APC mutations of desmoid tumours evade this control to lock in the Wnt signalling that drives them."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Spontaneous regression: a subset of desmoid tumours spontaneously regress through caspase-3-mediated apoptosis, the biological basis for the active-surveillance strategy now favoured over immediate resection."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Fibroblast growth signalling: FGF-FGFR signalling supports the proliferation of the myofibroblasts that constitute desmoid tumours, an additional growth-factor input to the Wnt-driven fibromatosis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Matricellular matrix: periostin produced by the desmoid myofibroblasts organises the dense collagenous extracellular matrix that gives these tumours their firm, infiltrative consistency and supports the fibroblast invasion into surrounding tissue."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Fibroblast activation: galectin-3 promotes the activation and survival of the myofibroblasts that drive desmoid fibromatosis, a profibrotic lectin contributing to the relentless local growth of these Wnt-driven tumours."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Fibrogenic signalling: TGF-β signalling through SMAD4 sustains the myofibroblast phenotype and collagen production of desmoid tumours, the fibrogenic transcriptional arm cooperating with Wnt/β-catenin to build the fibromatosis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K co-activation: PIK3CA drives the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) co-active in desmoid fibromatosis, the basis for the antitumour activity of mTOR inhibitors such as sirolimus."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: β-catenin transactivates cyclin-D1 (mapped), and the resulting CDK4/6 activity phosphorylates RB to release E2F1, driving the cell-cycle entry that makes desmoid fibromatosis locally aggressive."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K brake: PTEN normally restrains the same PI3K-AKT signalling, and its relative loss tips desmoid fibroblasts toward the growth and survival that complement Wnt-driven proliferation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Inflammatory stroma: IL-6 signalling through JAK-STAT3 (IL-6 and STAT3 already mapped) sustains the inflammatory, proliferative stroma of the desmoid tumour."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis resistance: anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the persistence and treatment-resistance of desmoid fibromatosis."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RTK-RAS proliferation: receptor-tyrosine-kinase signalling (PDGFR and FGFR mapped) converges on RAS-ERK (ERK1/2 mapped) to provide a proliferative input cooperating with Wnt/β-catenin in desmoid growth."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A loss is associated with more aggressive, progressive desmoid tumours, releasing CDK4/6-cyclin-D control (CDK4/6 and cyclin-D mapped)."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB signalling, in crosstalk with Wnt/β-catenin (mapped), supports fibroblast survival and the inflammatory matrix-producing phenotype of desmoid tumours."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of desmoid fibromatosis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune microenvironment of the locally aggressive but non-metastasising desmoid fibromatosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the survival and metabolic signalling of the Wnt-driven myofibroblasts of desmoid fibromatosis."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2-mediated polycomb repression contributes to the epigenetic programme sustaining the proliferative myofibroblast phenotype of desmoid fibromatosis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-kinase signaling downstream of PDGFR and KIT (PDGF and KIT already mapped) drives the proliferative and migratory signaling of desmoid fibromatosis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory stroma of the locally aggressive desmoid fibromatosis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance is an immune axis relevant to the locally invasive desmoid fibromatosis."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 regulation contributes to the survival of the proliferative myofibroblasts of desmoid tumor."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the Wnt-driven program of desmoid tumor."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of the myofibroblast-like cells of desmoid tumor."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of desmoid tumor."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of desmoid tumor."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of desmoid tumor."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of desmoid tumor."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of desmoid tumor."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of desmoid tumor."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of desmoid tumor."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of desmoid tumor."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the fibroblast and immune signaling of desmoid tumor."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Hormonal responsiveness: desmoid tumours express hormone receptors and can respond to anti-hormonal therapy, so the androgen axis, alongside the estrogen and progesterone already mapped, modulates their growth and pregnancy-associated flares."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Fibroblast activation: GAS6-AXL receptor tyrosine kinase signalling promotes the myofibroblast activation and invasive growth of desmoid tumours, a candidate target beyond the Wnt/beta-catenin driver already mapped."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune microenvironment: MHC class II-restricted T-cell surveillance shapes the immune microenvironment of desmoid tumours, and antigen presentation is relevant to the immunotherapy explored for these locally aggressive but non-metastasising fibromatoses."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell responses (MHC class II and CD8 already mapped) shape the immune surveillance of desmoid tumours, relevant to the immunotherapy explored for these locally aggressive fibromatoses."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive stroma: the anti-inflammatory cytokine IL-10 in the desmoid microenvironment dampens anti-tumour immunity, part of the immune tolerance that, with the Wnt drive (already mapped), sustains the infiltrative fibromatosis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide regulates the vascular tone and, with VEGF (already mapped), the angiogenesis supplying desmoid tumours, part of the stromal microenvironment beyond the myofibroblast and growth-factor drivers."
  - target: 01-human/07-system/fap
    relation: connects-to
    note: "FAP-associated desmoids: desmoid tumours are a major extracolonic manifestation of familial adenomatous polyposis (APC already mapped), often arising in the mesentery after colectomy, where they are a leading cause of death in FAP."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative microenvironment: the infiltrative desmoid generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of the fibrotic tumour microenvironment beyond the Wnt (already mapped) drive."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the desmoid stroma, part of the immune tolerance that sustains the infiltrative fibromatosis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Pro-fibrotic type-2: IL-13, with IL-4 (already mapped), drives the M2 macrophage and pro-fibrotic (TGF-β already mapped) programme that lays down the dense collagen (already mapped) matrix of the desmoid tumour."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages (CCL2 already mapped) infiltrate the desmoid stroma, and their M2 polarisation (IL-4 already mapped) supports the immune tolerance and fibrosis of the infiltrative fibromatosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Mesenteric desmoids: the intra-abdominal desmoids arise in the mesentery and encase the large intestine, a feared complication in familial adenomatous polyposis (FAP already mapped) often triggered by the colectomy."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Fibro-adipose crosstalk: leptin from the fibro-adipose tissue in which the desmoids arise engages in adipokine-fibroblast (already mapped) crosstalk, part of the tumour microenvironment of the fibromatosis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Mesenteric adipokine: adiponectin, with leptin (already mapped), from the mesenteric and abdominal-wall fibro-adipose tissue signals within the desmoid microenvironment."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Fibro-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the fibro-inflammatory stroma of the desmoid tumour."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Immune microenvironment: the NK cells and the anti-tumour immune surveillance of the immunologically cold desmoid microenvironment (CCL2 already mapped), relevant to the limited immunotherapy response."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Inflammatory stroma: the tumour-associated neutrophils and the neutrophil-lymphocyte ratio are studied prognostic markers of the fibro-inflammatory (IL-6 already mapped) desmoid stroma."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Mesenchymal-tumour differential: the desmoid and osteosarcoma are locally aggressive mesenchymal neoplasms of the deep soft tissue/bone, in the imaging and biopsy differential of a deep infiltrative mass."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 immune arm: the IFN-γ of the infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune contribution to the fibro-inflammatory (IL-6 already mapped) desmoid stroma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the desmoid tumour."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the desmoid tumour."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the desmoid tumour."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the desmoid-tumour microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the desmoid tumour."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the desmoid tumour."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen (MHC already mapped) to the T cells (already mapped) within the immune microenvironment of the desmoid tumour."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the fibroblast (already mapped)-rich stroma of the desmoid tumour."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the fibroblast-rich desmoid-tumour microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the desmoid-tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the stroma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Fibromatosis matricellular: osteopontin, a matricellular mediator, contributes to the fibroblast (already mapped) activation and the matrix remodelling (with periostin already mapped) of the desmoid tumour."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-desmoid axis: TSLP, from the CTNNB1-mutant desmoid stromal cells and the mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of the desmoid tumour."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-desmoid axis: bradykinin, via B1/B2 receptors on the desmoid endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability, the tumour oedema, and the inflammatory stromal milieu of the desmoid tumour."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-desmoid axis: erythropoietin, via the EPOR on the CTNNB1-activated desmoid tumour cells (already mapped), activates the PI3K/AKT (already mapped) survival axis and the angiogenic (VEGF already mapped) dimension of the desmoid tumour stroma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell desmoid axis: histamine, from the mast cells (already mapped) in the CTNNB1-driven desmoid stroma, amplifies the fibroblast (already mapped) activation and the vascular permeability of the inflammatory desmoid tumour microenvironment."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-Wnt axis: melatonin, via MT1/MT2 receptors and its antioxidant activity, modulates the oxidative stress and the CTNNB1/Wnt (already mapped) signalling of the desmoid-tumour fibroblasts (already mapped) and stromal cells."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation can contribute to the inflammatory stromal milieu of the desmoid tumour microenvironment."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Desmoid testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the TME; testosterone deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) stromal cascade of desmoid tumour."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Desmoid serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) stromal cascade of desmoid tumour."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Desmoid prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) fibroblast-proliferative cascade of desmoid tumour."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Desmoid oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the fibroblast-promoting TME; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) stromal cascade of desmoid tumour."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Desmoid vasopressin: vasopressin, via V1aR on mast cells (already mapped) and macrophages (already mapped), modulates the tumour vascular milieu; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) stromal cascade of desmoid tumour."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Desmoid selenium: selenium, as GPx in macrophages (already mapped) and mast cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative stromal fibroblast cascade of desmoid tumour."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Desmoid iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and mast-cell (already mapped) function; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) fibroblast-proliferative cascade of desmoid tumour."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Desmoid sodium: high dietary sodium promotes macrophage (already mapped) M2-skewing and mast-cell (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the stromal fibroblast cascade of desmoid tumour."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Desmoid magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and mast cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) stromal fibroblast-proliferative cascade of desmoid tumour."
---

# Desmoid Tumor

## Overview

**Desmoid tumor** (deep/aggressive fibromatosis) is a rare, locally invasive, clonally derived spindle cell neoplasm of fibroblastic/myofibroblastic origin that lacks the capacity for metastasis but causes significant morbidity through relentless local infiltration and destruction of adjacent structures. Desmoid tumors are driven in ~80% of sporadic cases by **activating mutations in CTNNB1 (exon 3)**, resulting in constitutive nuclear β-catenin accumulation and TCF/LEF-driven transcription; in ~20%, they arise from **germline APC mutations** in the setting of familial adenomatous polyposis (FAP). Despite being classified as low-grade neoplasms (WHO soft tissue 2020: intermediate — locally aggressive), desmoid tumors cause significant morbidity from infiltration of bowel, mesentery, abdominal wall, extremity musculature, and neurovascular structures [^lazar-2008-ctnnb1-desmoid].

**Epidemiology:**
- Incidence: ~2-4 per million/year; ~900-1,200 cases/year USA
- Age: median 30-40 years; wide range (pediatric to elderly); F:M ~2-3:1 in sporadic cases (hormonal influence — regression during menopause; worsening with estrogen)
- Pregnancy: desmoids can appear or accelerate during pregnancy (estrogen-mediated); post-pregnancy regression possible
- FAP-associated: ~10-20% of FAP patients develop desmoid; FAP desmoid typically mesenteric; accounts for ~15-20% of desmoid morbidity/mortality in FAP post-colectomy era

**Anatomic locations:**

| Location | Frequency | Key features |
|---|---|---|
| Abdominal wall | ~40% | Sporadic; often post-surgical/post-trauma; best prognosis; wide excision usually feasible |
| Mesenteric/intraabdominal | ~35% | FAP>sporadic; encases bowel mesentery; ureteral obstruction; small bowel obstruction; high morbidity |
| Extra-abdominal (extremity, trunk, chest wall) | ~25% | Infiltrates muscle compartments; neurovascular encasement; limb function impaired; recurrence common |
| Head and neck | ~5% | Airway compromise; CN involvement; disfiguring; surgical approach challenging |

**Natural history:**
- Highly variable: ~20-30% of desmoids demonstrate spontaneous regression without treatment
- ~30-40% remain stable for months to years
- ~30-50% progress locally; rapid early progression (first 6-12 months) predicts more aggressive behavior
- No metastatic potential; desmoid is not malignant in the classical oncologic sense
- Local recurrence: ~25-60% after surgery; positive margins not clearly associated with recurrence (controversial)
- Pregnancy-associated: may regress postpartum or after menopause; progesterone may accelerate growth

## Structure

### Histology

**Classic desmoid histology:**
- Uniform bland spindle cells (fibroblasts/myofibroblasts) arranged in long fascicles sweeping in parallel arrays or storiform pattern
- Abundant collagen matrix (pale pink on H&E); "keloid-like" collagen bands
- Elongated bipolar nuclei with vesicular chromatin; 1-2 inconspicuous nucleoli
- Very low mitotic rate (<2/10 HPF); NO atypical mitoses; NO pleomorphism
- Keloid-like hypocellular zones adjacent to hypercellular zones
- Infiltrative borders — tendrils of tumor cells penetrate surrounding fat and muscle (histological hallmark)

**IHC panel:**
- **β-catenin (nuclear)**: nuclear positivity ~85-90% in CTNNB1-mutant sporadic desmoid; weak or membrane-only in FAP-associated (where APC is truncated but CTNNB1 is WT); most specific desmoid marker
- **SMA (smooth muscle actin)**: positive in ~80-90%; myofibroblastic differentiation
- **MSA (muscle-specific actin)**: positive ~70%
- **Vimentin**: diffusely positive
- **Desmin**: focal positive ~10-20%
- **S100**: negative (helpful to exclude nerve sheath tumors)
- **CD34**: negative (helpful to exclude SFT)
- **STAT6**: negative (helps exclude SFT)
- **SOX10**: negative

**Molecular confirmation:**
- CTNNB1 Sanger sequencing (exon 3) or NGS panel: mandatory for ambiguous cases
- APC germline testing: offered to all desmoid patients <40 years, mesenteric location, family history
- CTNNB1 S45F/Y → higher recurrence risk; T41A → lower risk [^lazar-2008-ctnnb1-desmoid]

## Function

### CTNNB1-driven oncogenesis in desmoid

Desmoid tumors arise from fibroblastic/myofibroblastic mesenchymal progenitors in response to triggering events:

**Sporadic desmoid triggers:**
- Trauma/surgery (~40% of cases have history of prior trauma/surgery at the site): physical disruption → fibroblast proliferation → in cells harboring CTNNB1 mutation, proliferative signal persists
- Estrogen: desmoid fibroblasts express estrogen receptor α; estrogen → ERα → β-catenin nuclear translocation amplification; pregnancy-associated growth; anti-estrogen therapy (tamoxifen, toremifene) exploits this

**FAP-associated desmoid:**
- Germline APC truncation (especially codons 1310-2011) → insufficient APC → increased β-catenin; colectomy trigger → laparotomy wound → desmoid at abdominal wall or mesentery; risk: APC genotype (specific mutation sites predispose to mesenteric vs abdominal wall)

**β-catenin/TCF target program in desmoid cells:**
- MYC → drives fibroblast proliferation
- CCND1 (cyclin D1) → CDK4/6 → cell cycle
- VEGFA → angiogenesis (explains vascularity visible on MRI)
- MMP2/9 → matrix degradation → invasion
- DKK1 (secreted Wnt inhibitor) → negative feedback (often silenced in CTNNB1-mutant desmoid, removing the brake)
- AXIN2 → negative feedback (partially functional; explains why some desmoids stabilize)

## Pathology

### Staging and risk stratification

**No standard TNM staging** for desmoid; no metastases possible; risk stratified by:
- **Mutation type** (CTNNB1 S45F > T41A for recurrence)
- **Location** (mesenteric worst; abdominal wall best prognosis)
- **Size**: larger tumors (>10 cm) behave more aggressively
- **Age**: younger patients (<30) have higher recurrence rates
- **FAP vs sporadic**: FAP mesenteric desmoid particularly aggressive and difficult to resect
- **Rate of growth**: rapid early growth → poor prognosis; initial stability → may spontaneously plateau

### Treatment

**Watch and wait (active surveillance):**
Standard initial approach for newly diagnosed desmoid without symptoms or rapid growth; ~20-30% regress spontaneously; monthly or bi-monthly MRI surveillance; intervention deferred until progression, pain, or functional compromise; evidence: prospective observational data from DESMOID-1 (N=439) showed 46% had no treatment in first 3 years; 28-month progression-free rate ~59%

**Nirogacestat (gamma-secretase/Notch inhibitor) — FDA-approved November 2023:** [^gounder-2023-nirogacestat-desmoid]
- **DeFi Phase 3** (Gounder 2023): N=142 adults with progressing desmoid; nirogacestat 150 mg BID vs placebo; primary endpoint PFS; PFS HR 0.29 (95% CI 0.15-0.55, p<0.0001); median PFS not reached vs 15.1 months placebo; ORR 41% vs 8%; time to response median ~5.5 months; most responses durable; OS benefit trending
- Toxicity: diarrhea (grade 3: 12%), ovarian toxicity (amenorrhea, elevated FSH in premenopausal women: ~75% → reversible in most after discontinuation), rash (~35%), fatigue (~30%)
- FDA approved for adults with progressing desmoid tumors; pediatric approval pending
- First FDA-approved drug for desmoid tumors

**Sorafenib:**
- Phase 2 SARC026 (Gounder 2018, N=87): sorafenib 400 mg/day vs placebo; PFS HR 0.13 (p<0.0001); ORR 33% vs 20% at 6 months; widely used off-label for progressive desmoid prior to nirogacestat approval; toxicity: hand-foot syndrome (~40%), fatigue, hypertension

**Hormonal therapy:**
- Tamoxifen 40-120 mg/day or toremifene: ER-based strategy; ORR ~10-15% single agent; widely used in combination with NSAIDs (sulindac); desmoid regression reported especially in post-menopausal patients; safe long-term; low-cost option for stable/slowly growing disease
- NSAID (sulindac 300-400 mg/day): anti-inflammatory → reduces desmoid vascularity; ORR ~10-15% as monotherapy; synergizes with anti-estrogen; mechanism: COX-2 → PGE2 → β-catenin stabilization loop; sulindac breaks this

**Chemotherapy:**
- Methotrexate + vinca alkaloid (vinblastine or vinorelbine): ORR ~40-50% in pediatric/young adult progressive desmoid; used as cytotoxic-sparing protocol; weekly administration; main toxicity: myelosuppression, neuropathy; also used in adult FAP-associated mesenteric disease
- Doxorubicin + dacarbazine: ORR ~20-30%; for rapidly progressive, large-burden, or life-threatening desmoid (mesenteric encasement, ureteral obstruction); similar to soft tissue sarcoma chemotherapy approach
- Pegylated liposomal doxorubicin: ORR ~15-25%; less cardiotoxicity; used in patients who need prolonged doxorubicin

**Surgery:**
- Historically first-line; now reserved for specific indications: abdominal wall desmoid (easily resectable, low recurrence), symptomatic bowel obstruction, failed systemic therapy with isolated resectable disease
- Wide negative margin surgery: recurrence rates ~25-60% regardless of margin status (controversy: positive margins may not increase recurrence in desmoid)
- Surgery CONTRAINDICATED as first-line for: mesenteric desmoid (high morbidity, high recurrence), large extremity/trunk desmoid (amputation not justified for non-malignant tumor), rapidly growing desmoid (active systemic therapy preferred)
- Post-operative stimulus: surgery itself can trigger desmoid growth at anastomosis/scar sites in FAP patients

**Radiation therapy:**
- Used for unresectable, chemotherapy-refractory, or post-surgical recurrence
- 50-56 Gy in 25-28 fractions; local control ~70-80% at 5 years in resectable desmoid; 50-60% in unresectable
- Long-term radiation toxicity concerns (secondary malignancy, fibrosis, neuropathy) limit use; not for young patients or mesenteric disease

**Prognosis:**
- No disease-specific mortality from desmoid in most cases (no metastases); mortality from local complications (bowel obstruction, ureteral obstruction, superior mesenteric artery encasement in FAP mesenteric desmoid)
- Abdominal wall: 5-year recurrence-free survival after resection ~60-75%
- Mesenteric/FAP: most clinically challenging; leading non-cancer cause of mortality in FAP patients post-colectomy; multiple surgical procedures often needed
- Spontaneous regression: ~20-30% (best outcome); regression may take 3-5 years
- Nirogacestat era: median PFS not reached in responders; 2-year PFS ~70% in nirogacestat arm

## Connections

- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — CTNNB1 activating mutations (S45F, T41A, S33C) in ~80% sporadic desmoid tumors → nuclear β-catenin → TCF/LEF-dependent transcription → MYC, CCND1 → desmoid fibroblast proliferation; APC germline mutations (FAP) account for ~20%; CTNNB1 T41A predicts best prognosis.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — CTNNB1 encodes β-catenin, the terminal Wnt effector; Wnt → LRP5/6 + FZD → Axin/APC complex inhibition → β-catenin stabilization → nuclear translocation → TCF/LEF co-activator; activating CTNNB1 mutations mimic Wnt-ON state regardless of ligand; Wnt+CTNNB1 mutation = maximum Wnt.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Nirogacestat (gamma-secretase inhibitor) blocks Notch signaling → NICD1 suppression → desmoid cell apoptosis; DeFi Phase 3: ORR 41% vs 8% placebo, PFS HR 0.29; FDA-approved November 2023; Notch-Wnt crosstalk amplifies CTNNB1-driven desmoid proliferation.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — CTNNB1/β-catenin activates VEGFA transcription via TCF/LEF elements → tumor angiogenesis in desmoid and colorectal cancer; VEGF blockade (bevacizumab) explored in desmoid tumor trials; VEGFR/PDGFR inhibitor sorafenib achieves ORR ~15% in desmoid (DESMOID Phase 2, PFS HR 0.13).
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — APC germline truncating mutations (codons 1310-2011) cause FAP; ~20% of desmoid tumors arise in FAP via APC LOF → insufficient β-catenin destruction → nuclear β-catenin → Wnt targets; FAP mesenteric desmoid is the leading non-cancer cause of death post-colectomy in FAP patients.
- `connects-to` → **[FAP](../fap/README.md)** — FAP (germline APC) carries ~10-20% lifetime desmoid tumor risk; FAP mesenteric desmoid is the leading non-cancer cause of mortality in post-colectomy FAP; laparotomy wound triggers mesenteric desmoid; prophylactic sulindac and close surveillance are standard at FAP centers.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Desmoid tumor arises from fibroblastic/myofibroblastic progenitors in CTNNB1-mutant cells triggered by trauma or surgery; desmoid myofibroblasts (αSMA+, nuclear β-catenin) secrete dense collagen and resist apoptosis; TGF-β amplifies myofibroblastic activation in desmoid stroma.
- `connects-to` → **[GIST](../gist/README.md)** — Desmoid tumors and GISTs are intra-abdominal mesenchymal tumors often confused on imaging but molecularly opposite: desmoid is a non-metastasizing fibroblastic proliferation driven by CTNNB1/APC-Wnt, while GIST is a KIT/PDGFRA-driven Cajal-cell tumor that can metastasize.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Mesenteric desmoid tumors arise in the small-bowel mesentery, especially after abdominal surgery in FAP, encasing mesenteric vessels and bowel; this infiltrative, non-metastasizing growth causes obstruction, ischemia, and fistulae — a leading non-cancer cause of death in FAP.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Extra-abdominal desmoids (aggressive fibromatosis) of the shoulder, abdominal wall, and limbs are locally infiltrative soft-tissue tumors that recur after resection but never metastasize; since surgery often triggers regrowth, surveillance and systemic drugs are first-line.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Desmoid tumors are a hallmark of familial adenomatous polyposis (Gardner syndrome), the same APC/Wnt disorder that causes colorectal cancer: ~10-15% of FAP patients develop desmoids, often intra-abdominal and triggered by colectomy, where they become a leading cause of death.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Desmoid tumors are frequently hormone-responsive: many express estrogen receptors, can grow during pregnancy or with oral contraceptives and regress after menopause, so anti-estrogens (tamoxifen) with NSAIDs are an established option for these non-metastasizing fibromatoses.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Desmoid tumors are driven by a profibrotic program in which TGF-β is central: alongside constitutive Wnt/β-catenin, TGF-β stimulates myofibroblasts to lay down the dense collagenous matrix that makes desmoids infiltrative and locally destructive—the hallmark of fibromatosis.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Desmoid tumor and synovial sarcoma are both deep soft-tissue tumors but biologically apart: desmoid is a locally aggressive fibroblastic proliferation driven by CTNNB1/Wnt that never metastasizes, while synovial sarcoma is a malignant SS18-SSX sarcoma that does.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Desmoid tumor and Ewing sarcoma both arise in young people but differ: desmoid is a non-metastasizing fibromatosis often managed by active surveillance, whereas Ewing is an aggressive EWSR1-FLI1 small-round-cell sarcoma needing intensive chemo and radiation.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Desmoid tumors are linked to the reproductive system through estrogen and pregnancy: many are estrogen-responsive and can grow during or after pregnancy, and abdominal-wall desmoids classically follow childbirth—so hormonal therapy is one treatment option.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Desmoid tumors are collagen-rich fibromatoses, not true sarcomas: clonal myofibroblasts driven by beta-catenin lay down dense collagen, producing an infiltrative but non-metastasizing mass—locally aggressive yet unable to spread, shaping conservative treatment.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cyclin D1 links desmoid's Wnt driver to growth: stabilized beta-catenin (from CTNNB1 or APC mutation) switches on cyclin D1, pushing myofibroblasts through the cell cycle—the Wnt/cyclin-D1 axis behind colon cancer here yields a benign-behaving but relentless tumor.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF signaling offers a therapeutic handle in desmoid tumors: these fibromatoses express PDGFR, so multitargeted tyrosine-kinase inhibitors (sorafenib, imatinib) shrink or stabilize them—part of the shift from surgery toward systemic and watchful-waiting management.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is one option for unresectable desmoid tumors: though benign, desmoids invade locally and recur after surgery, so photon-beam radiation can control disease when an operation would be mutilating—balanced against radiation's own risks in young patients.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Desmoid tumors have a special affinity for the abdomen and gut: in FAP/Gardner syndrome they arise in the mesentery and abdominal wall, where they can encase and obstruct the bowel and its vessels—making intra-abdominal desmoids a leading cause of death in FAP.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Desmoid tumors sit in the soft-tissue-mass differential with sarcomas like rhabdomyosarcoma: desmoids are locally aggressive but never metastasize, while rhabdomyosarcoma is frankly malignant—so biopsy distinguishes a benign fibromatosis from a deadly sarcoma.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The desmoid tumor cell is a myofibroblast: it blends fibroblast and smooth-muscle features, expressing actin as it contracts and invades locally, so although benign and non-metastasizing, its smooth-muscle-like infiltration makes desmoids hard to fully excise.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Desmoid tumors are estrogen-sensitive and tied to pregnancy: many abdominal-wall desmoids appear during or after pregnancy as estrogen drives their growth, so they often arise near the gravid uterus and may regress after delivery or with anti-estrogens.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Desmoid is a fibromatosis—benign but relentlessly fibrotic: clonal myofibroblasts lay down dense collagen that infiltrates muscle and fascia, so it behaves like an aggressive scar, distinguishing it from both reactive fibrosis and true sarcoma.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Desmoid tumors can be reined in through mTOR: the same β-catenin and growth signaling that drives them feeds into the PI3K-AKT-mTOR axis, so mTOR inhibitors like sirolimus are used to shrink these locally aggressive fibromatoses that won't metastasize.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Desmoid tumors are seeded with mast cells: these immune cells populate the fibromatosis stroma and release mediators that may spur fibroblast growth, part of the inflammatory microenvironment shaping how aggressively a desmoid behaves.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages help build the desmoid's stroma: tumor-associated macrophages infiltrate the fibrous mass and secrete growth factors that drive the relentless local proliferation of myofibroblasts characteristic of these tumors.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Desmoids also lean on PI3K-AKT growth signaling: alongside the driving Wnt/beta-catenin lesion, AKT-mTOR activity sustains the myofibroblast proliferation, which is why mTOR-pathway drugs have been tried in these locally aggressive fibrous tumors.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Desmoids are immune-cold tumors with few cytotoxic T cells: their dense collagen stroma keeps killer T cells sparse, helping explain why checkpoint immunotherapy has little effect and why treatment instead targets Wnt and growth signals.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — The desmoid's dense fibrous core runs low on oxygen: as the mass outgrows its blood supply it turns hypoxic, stabilizing HIF and driving the VEGF-fueled angiogenesis that lets the relentless fibromatosis keep expanding.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Mesenteric desmoids strangle the bowel: especially in FAP, these fibrous tumors grow through the mesentery and encase the intestine, obstructing the gut and threatening the vessels and ureters around it.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Abdominal desmoids can choke the kidneys: a growing mesenteric mass compresses the ureters, backing urine up into the kidneys (hydronephrosis) and threatening renal function, a feared complication of FAP-associated desmoids.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Desmoids weave a dense matrix of fibronectin: their myofibroblasts pour out fibronectin and collagen to build the tough fibrous stroma that gives the tumor its hardness and infiltrative grip on surrounding tissue.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Desmoids recruit new vessels: VEGF draws endothelial cells to feed the slowly expanding fibrous mass, and anti-angiogenic agents are among the systemic options tried for unresectable tumors.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Desmoids ensnare nerves: the infiltrative fibrous mass wraps and compresses adjacent peripheral nerves, causing the pain and neurological deficits that often drive treatment of an otherwise benign tumor.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Abdominal-wall desmoids surface beneath the skin: they present as a deep, firm mass, classically in women after childbirth or along old surgical scars, the commonest sporadic site.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the desmoid's working cell: the myofibroblast, a fibroblast-smooth-muscle hybrid bristling with rough endoplasmic reticulum and actin bundles, churning out the dense collagen that makes these tumors so firm and infiltrative.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Chest-wall desmoids invade toward the lung: arising in the thoracic wall they grow inward against the pleura and mediastinum, and although they never metastasize, their relentless local spread can compress the chest's contents.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Desmoids gnaw the bone they abut: though purely soft-tissue tumors, their infiltrative growth can erode the cortex of adjacent bone, a sign of how aggressively they invade despite never spreading distantly.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Desmoids entrap the nerves they grow around: their infiltrative edge encases peripheral nerves, causing pain, numbness, and weakness, and making surgery risky for the nerve as much as for the recurrence-prone tumor.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — An intra-abdominal desmoid can throttle the gut: mesenteric tumors — common in familial adenomatous polyposis — compress the stomach and bowel into obstruction, and can encase the mesenteric vessels feeding them.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Desmoids arise amid the body's fat and fascia: springing from the fibrous tissue of the abdominal wall and the fat-rich mesentery, they must be told apart from the benign lipoma and malignant liposarcoma that share that home.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Pregnancy can stir desmoids: many appear or grow during gestation and abdominal-wall desmoids especially, then often stabilize or regress after delivery, a hormone sensitivity to estrogen and progesterone that underlies the anti-hormonal therapies sometimes tried.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Pressing on bone, the desmoid remodels it: extra-abdominal tumors abutting the chest wall or limb girdle scallop the cortex and provoke periosteal new bone from osteoblasts, the bony reaction that imaging picks up at the tumor's edge.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Mesenteric desmoids crowd the upper abdomen: in FAP they grow at the root of the mesentery and can encase the duodenum and pancreas, complicating surgery and sometimes obstructing the bowel or bile drainage.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Desmoids favor sites of injury: they classically arise in surgical scars, including after breast surgery, so a firm mass at a mastectomy or reconstruction site can be a desmoid rather than recurrent cancer.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — An immune-cell milieu shapes the tumor: regulatory T cells populate the desmoid microenvironment, part of the stromal-immune context being explored as these locally aggressive fibromatoses resist conventional treatment.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation feeds the fibromatosis: IL-6 and prostaglandin signaling promote desmoid fibroblast growth, a rationale behind the anti-inflammatory NSAIDs long tried to slow these tumors.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — A desmoid is wound healing that won't switch off: it is a clonal myofibroblast proliferation that classically erupts at sites of surgery, trauma, or pregnancy, as if the repair program ran unchecked under activated β-catenin.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — YAP partners with β-catenin in the desmoid: Hippo-pathway YAP activation cooperates with the driving Wnt/β-catenin signal to sustain the fibroblast proliferation, marking another node studied as a therapeutic target.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Desmoids cluster with the FAP cancers: arising from the same APC loss, they accompany the colorectal and upper-GI tumors of familial adenomatous polyposis, where fundic-gland and gastric neoplasia round out the syndrome's GI risk.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 feeds the fibromatosis through STAT3: the inflamed desmoid stroma's IL-6 activates STAT3, adding a proliferative signal alongside the driving Wnt/β-catenin pathway in this locally aggressive tumor.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — A retroperitoneal mass can strangle the ureters: large mesenteric or retroperitoneal desmoids compress the ureters into hydronephrosis, and prolonged obstruction can erode kidney function toward chronic kidney disease.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Bulky abdominal tumors compress the veins: mesenteric desmoids can obstruct venous return, and the major surgery they sometimes require adds to the risk of deep-vein thrombosis.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Infiltrating fibrosis traps the nerves: desmoid tumors invade locally and compress or encase nerves, causing chronic neuropathic pain that is often the dominant symptom of these aggressive but non-metastasizing growths.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Abdominal desmoids can breach the bowel: mesenteric tumors and their resection can cause bowel obstruction, fistula or perforation, spilling gut flora into the abdomen and seeding sepsis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A relentless, recurring tumor wears on the mind: chronic pain, disfigurement and the high recurrence of desmoid tumors despite their benign label carry a substantial psychological burden and depression.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its targeted drugs strain the heart: the sorafenib and other tyrosine-kinase inhibitors used to control aggressive desmoid tumors raise blood pressure and are cardiotoxic, risking heart failure.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — A large infiltrative tumor drains the blood: bulky mesenteric or abdominal desmoids with their inflammatory burden, and any associated bleeding, can produce an anemia of chronic disease.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Unpredictable recurrence breeds worry: the locally aggressive, frequently recurring behavior of desmoid tumors and the need for ongoing imaging surveillance foster chronic health anxiety.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is fuelled by oestrogen: desmoid tumours often grow during pregnancy and with the contraceptive pill and express oestrogen receptors, so anti-oestrogens like tamoxifen are used to treat them.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Mesenteric tumour can throttle the ureters: a bulky intra-abdominal desmoid, common in FAP, can encase and obstruct the ureters, causing hydronephrosis and threatening kidney function.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It arises in the abdominal wall and skin: desmoid tumours frequently grow in the abdominal-wall soft tissue, and in Gardner syndrome accompany epidermoid cysts and other cutaneous lesions.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It wraps around the great vessels: intra-abdominal and mesenteric desmoids encase and compress mesenteric arteries, the aorta and IVC, risking bowel ischaemia and vascular obstruction.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It infiltrates around the nerves: desmoid tumours grow into and compress nerves and nerve roots, causing pain and neurological deficits, and their resection risks nerve injury.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Mesenteric tumours block lymph flow: a mesenteric desmoid can obstruct lymphatic drainage, causing chylous ascites, on top of the bowel and ureteric compression it produces.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can grow in the chest: thoracic and chest-wall desmoid tumours can encase the ribs and compress the lung, and mesenteric disease can press on the diaphragm.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — Anti-inflammatories can hold it back: NSAIDs such as sulindac, in the same class as ibuprofen, are used to slow desmoid growth, sometimes with anti-oestrogens, before resorting to surgery or systemic therapy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It builds an inflammatory stroma: desmoid tumours carry a fibroinflammatory microenvironment rich in immune cells, and their indolent, sometimes self-regressing behaviour has drawn interest in immune modulation.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A new drug targets its pathway: nirogacestat, a gamma-secretase inhibitor of Notch, and multikinase inhibitors (sorafenib, pazopanib) shrink progressive desmoid tumours that exploit Wnt/β-catenin signalling.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Low-dose chemo controls progression: regimens like methotrexate-vinblastine or liposomal doxorubicin treat progressive or symptomatic desmoid tumours unsuitable for surgery.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Both flag familial polyposis: desmoid tumours and cribriform-morular thyroid carcinoma are extracolonic manifestations of familial adenomatous polyposis, sharing its APC/Wnt-pathway driver.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — It strangles the bowel: in FAP/Gardner syndrome, mesenteric desmoid tumours encase and obstruct the small intestine and its vessels, a leading cause of death after colectomy despite being histologically benign.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It erodes adjacent bone: though non-metastasising, aggressive desmoid fibromatosis infiltrates muscle and fascia and can scallop and erode the cortical bone it abuts, driving pain and local destruction.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Two faces of fibroblast overgrowth: desmoid is a clonal neoplastic proliferation of myofibroblasts laying down collagen, whereas systemic sclerosis is autoimmune-driven fibroblast activation — different triggers converging on excess fibrous tissue.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — The FAP/Turcot connection: APC-mutant familial adenomatous polyposis predisposes to both desmoid tumours and medulloblastoma (Turcot syndrome), two Wnt-pathway lesions of one germline defect.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It encases the great vessels: intra-abdominal desmoids in FAP infiltrate the mesentery, encasing and compressing the mesenteric arteries and causing the bowel ischaemia that makes them lethal.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Obstruction backs up to the kidney: a mesenteric or pelvic desmoid can compress the ureters, and the resulting hydronephrosis backs pressure up to the glomerulus, threatening renal function.
- `connects-to` → **[MUTYH-Associated Polyposis](../mutyh-associated-polyposis/README.md)** — Polyposis and desmoids: desmoid tumours are a hallmark of APC-driven FAP/Gardner syndrome; MUTYH-associated polyposis phenocopies FAP's colorectal polyposis but rarely produces desmoids, a distinguishing feature.
- `connects-to` → **[HCC](../hcc/README.md)** — Shared Wnt activation: desmoid tumours and a subset of hepatocellular carcinomas are both driven by activating CTNNB1 (β-catenin) mutations, the same Wnt pathway producing very different tumours.
- `connects-to` → **[MPNST](../mpnst/README.md)** — Benign-but-aggressive vs malignant: desmoid fibromatosis invades locally but never metastasizes, contrasting with malignant soft-tissue sarcomas like MPNST that both invade and spread distantly.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — NSAID-responsive growth: prostaglandins promote desmoid proliferation, the rationale behind treating these tumours with COX inhibitors such as sulindac and other NSAIDs.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — Kinase target: desmoids express KIT and PDGFR receptors, underpinning the partial responses seen with tyrosine kinase inhibitors like imatinib in progressive disease.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Replicative persistence: telomerase activity helps desmoid cells sustain the relentless, locally invasive proliferation that makes these benign tumours so difficult to control.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Wnt target oncogene: nuclear β-catenin in desmoid tumours drives transcription of MYC, helping sustain the proliferative, locally aggressive fibromatosis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle entry: β-catenin-driven cyclin D1 activates CDK4/6 to push desmoid fibroblasts through the G1 checkpoint, the engine of their relentless growth.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic stroma: the dense, poorly vascularised desmoid matrix becomes hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis that supports continued expansion.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Fibroblast growth signal: IGF-1/IGF-1R signalling supports the proliferation and survival of the myofibroblasts that make up desmoid tumours, cooperating with the driving Wnt-β-catenin pathway.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — MAPK proliferation: RAF-MEK-ERK signalling drives desmoid fibroblast proliferation, part of why the multi-kinase inhibitor sorafenib produces durable responses in aggressive fibromatosis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Stromal macrophages: CCL2 recruits macrophages into the desmoid stroma, contributing to the inflammatory, matrix-remodelling microenvironment of these locally aggressive fibrous tumours.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β, with APC and Axin, normally phosphorylates β-catenin for degradation, so the CTNNB1 and APC mutations of desmoid tumors evade this destruction complex to lock in the Wnt signaling that drives the fibromatosis.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — A substantial subset of desmoid tumors spontaneously regress through caspase-3-mediated apoptosis, the biological basis for the active-surveillance strategy now favored over immediate surgery for these non-metastasizing tumors.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGF-FGFR signaling supports the proliferation of the myofibroblasts that constitute desmoid tumors, an additional growth-factor input layered on the Wnt-β-catenin pathway that fundamentally drives them.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periostin produced by the desmoid myofibroblasts organizes the dense collagenous extracellular matrix that gives these tumors their firm, infiltrative consistency and supports the fibroblast invasion into surrounding tissue.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the activation and survival of the myofibroblasts that drive desmoid fibromatosis, a profibrotic lectin contributing to the relentless local growth of these Wnt-driven tumors.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β signaling through SMAD4 sustains the myofibroblast phenotype and collagen production of desmoid tumors, the fibrogenic transcriptional arm cooperating with Wnt/β-catenin to build the fibromatosis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA drives the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) co-active in desmoid fibromatosis, the basis for the antitumor activity of mTOR inhibitors such as sirolimus.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — β-catenin transactivates cyclin-D1 (mapped), and the resulting CDK4/6 activity phosphorylates RB to release E2F1, driving the cell-cycle entry that makes desmoid fibromatosis locally aggressive.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN normally restrains the same PI3K-AKT signaling, and its relative loss tips desmoid fibroblasts toward the growth and survival that complement Wnt-driven proliferation.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 signaling through JAK-STAT3 (IL-6 and STAT3 already mapped) sustains the inflammatory, proliferative stroma of the desmoid tumor.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Anti-apoptotic BCL-2 raises the threshold for caspase-3 apoptosis (already mapped), contributing to the persistence and treatment-resistance of desmoid fibromatosis.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Receptor-tyrosine-kinase signaling (PDGFR and FGFR mapped) converges on RAS-ERK (ERK1/2 mapped) to provide a proliferative input cooperating with Wnt/β-catenin in desmoid growth.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss is associated with more aggressive, progressive desmoid tumors, releasing CDK4/6-cyclin-D control (CDK4/6 and cyclin-D mapped).
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB signaling, in crosstalk with Wnt/β-catenin (mapped), supports fibroblast survival and the inflammatory matrix-producing phenotype of desmoid tumors.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of desmoid fibromatosis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune microenvironment of the locally aggressive but non-metastasizing desmoid fibromatosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the survival and metabolic signaling of the Wnt-driven myofibroblasts of desmoid fibromatosis.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2-mediated polycomb repression contributes to the epigenetic program sustaining the proliferative myofibroblast phenotype of desmoid fibromatosis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-kinase signaling downstream of PDGFR and KIT (PDGF and KIT already mapped) drives the proliferative and migratory signaling of desmoid fibromatosis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory stroma of the locally aggressive desmoid fibromatosis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance is an immune axis relevant to the locally invasive desmoid fibromatosis.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 regulation contributes to the survival of the proliferative myofibroblasts of desmoid tumor.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic regulation of the Wnt-driven program of desmoid tumor.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of the myofibroblast-like cells of desmoid tumor.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of desmoid tumor.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of desmoid tumor.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of desmoid tumor.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the tumor-stromal interactions of desmoid tumor.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of desmoid tumor.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of desmoid tumor.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of desmoid tumor.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of desmoid tumor.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the fibroblast and immune signaling of desmoid tumor.
- `connects-to` → **[Androgen receptor](../../03-molecular/androgen-receptor/README.md)** — Hormonal responsiveness: desmoid tumours express hormone receptors and can respond to anti-hormonal therapy, so the androgen axis, alongside the estrogen and progesterone already mapped, modulates their growth and pregnancy-associated flares.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Fibroblast activation: GAS6-AXL receptor tyrosine kinase signalling promotes the myofibroblast activation and invasive growth of desmoid tumours, a candidate target beyond the Wnt/beta-catenin driver already mapped.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune microenvironment: MHC class II-restricted T-cell surveillance shapes the immune microenvironment of desmoid tumours, and antigen presentation is relevant to the immunotherapy explored for these locally aggressive but non-metastasising fibromatoses.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell responses (MHC class II and CD8 already mapped) shape the immune surveillance of desmoid tumours, relevant to the immunotherapy explored for these locally aggressive fibromatoses.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive stroma: the anti-inflammatory cytokine IL-10 in the desmoid microenvironment dampens anti-tumour immunity, part of the immune tolerance that, with the Wnt drive (already mapped), sustains the infiltrative fibromatosis.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide regulates the vascular tone and, with VEGF (already mapped), the angiogenesis supplying desmoid tumours, part of the stromal microenvironment beyond the myofibroblast and growth-factor drivers.
- `connects-to` → **[FAP](../fap/README.md)** — FAP-associated desmoids: desmoid tumours are a major extracolonic manifestation of familial adenomatous polyposis (APC already mapped), often arising in the mesentery after colectomy, where they are a leading cause of death in FAP.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative microenvironment: the infiltrative desmoid generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species are part of the fibrotic tumour microenvironment beyond the Wnt (already mapped) drive.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped) in the desmoid stroma, part of the immune tolerance that sustains the infiltrative fibromatosis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Pro-fibrotic type-2: IL-13, with IL-4 (already mapped), drives the M2 macrophage and pro-fibrotic (TGF-β already mapped) programme that lays down the dense collagen (already mapped) matrix of the desmoid tumour.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages (CCL2 already mapped) infiltrate the desmoid stroma, and their M2 polarisation (IL-4 already mapped) supports the immune tolerance and fibrosis of the infiltrative fibromatosis.
- `connects-to` → **[Large intestine](../../06-organ/large-intestine/README.md)** — Mesenteric desmoids: the intra-abdominal desmoids arise in the mesentery and encase the large intestine, a feared complication in familial adenomatous polyposis (FAP already mapped) often triggered by the colectomy.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Fibro-adipose crosstalk: leptin from the fibro-adipose tissue in which the desmoids arise engages in adipokine-fibroblast (already mapped) crosstalk, part of the tumour microenvironment of the fibromatosis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Mesenteric adipokine: adiponectin, with leptin (already mapped), from the mesenteric and abdominal-wall fibro-adipose tissue signals within the desmoid microenvironment.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Fibro-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the fibro-inflammatory stroma of the desmoid tumour.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Immune microenvironment: the NK cells and the anti-tumour immune surveillance of the immunologically cold desmoid microenvironment (CCL2 already mapped), relevant to the limited immunotherapy response.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Inflammatory stroma: the tumour-associated neutrophils and the neutrophil-lymphocyte ratio are studied prognostic markers of the fibro-inflammatory (IL-6 already mapped) desmoid stroma.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Mesenchymal-tumour differential: the desmoid and osteosarcoma are locally aggressive mesenchymal neoplasms of the deep soft tissue/bone, in the imaging and biopsy differential of a deep infiltrative mass.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 immune arm: the IFN-γ of the infiltrating T cells (perforin already mapped) is the type-II interferon arm of the immune contribution to the fibro-inflammatory (IL-6 already mapped) desmoid stroma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the desmoid tumour.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the desmoid tumour.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the desmoid tumour.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the desmoid-tumour microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the desmoid tumour.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the desmoid tumour.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen (MHC already mapped) to the T cells (already mapped) within the immune microenvironment of the desmoid tumour.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the fibroblast (already mapped)-rich stroma of the desmoid tumour.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the inflammatory dimension of the fibroblast-rich desmoid-tumour microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the desmoid-tumour cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the stroma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Fibromatosis matricellular: osteopontin, a matricellular mediator, contributes to the fibroblast (already mapped) activation and the matrix remodelling (with periostin already mapped) of the desmoid tumour.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-desmoid axis: TSLP, from the CTNNB1-mutant desmoid stromal cells and the mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2 immunosuppressive microenvironment of the desmoid tumour.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-desmoid axis: bradykinin, via B1/B2 receptors on the desmoid endothelium (already mapped) and mast cells (already mapped), amplifies the vascular permeability, the tumour oedema, and the inflammatory stromal milieu of the desmoid tumour.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-desmoid axis: erythropoietin, via the EPOR on the CTNNB1-activated desmoid tumour cells (already mapped), activates the PI3K/AKT (already mapped) survival axis and the angiogenic (VEGF already mapped) dimension of the desmoid tumour stroma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell desmoid axis: histamine, from the mast cells (already mapped) in the CTNNB1-driven desmoid stroma, amplifies the fibroblast (already mapped) activation and the vascular permeability of the inflammatory desmoid tumour microenvironment.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-Wnt axis: melatonin, via MT1/MT2 receptors and its antioxidant activity, modulates the oxidative stress and the CTNNB1/Wnt (already mapped) signalling of the desmoid-tumour fibroblasts (already mapped) and stromal cells.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: the C1-esterase inhibitor regulates the classical complement pathway (C5 and C5aR1 already mapped) whose activation can contribute to the inflammatory stromal milieu of the desmoid tumour microenvironment.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Desmoid testosterone: testosterone, via androgen receptors on macrophages (already mapped) and T-cytotoxic cells (already mapped), modulates the TME; testosterone deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) stromal cascade of desmoid tumour.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Desmoid serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the TME; serotonin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) stromal cascade of desmoid tumour.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Desmoid prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the NF-κB (already mapped) and IL-6 (already mapped) fibroblast-proliferative cascade of desmoid tumour.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Desmoid oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the fibroblast-promoting TME; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) stromal cascade of desmoid tumour.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Desmoid vasopressin: vasopressin, via V1aR on mast cells (already mapped) and macrophages (already mapped), modulates the tumour vascular milieu; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) stromal cascade of desmoid tumour.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Desmoid selenium: selenium, as GPx in macrophages (already mapped) and mast cells (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) oxidative stromal fibroblast cascade of desmoid tumour.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Desmoid iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation and mast-cell (already mapped) function; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) fibroblast-proliferative cascade of desmoid tumour.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Desmoid sodium: high dietary sodium promotes macrophage (already mapped) M2-skewing and mast-cell (already mapped) activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the stromal fibroblast cascade of desmoid tumour.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Desmoid magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and mast cells (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) stromal fibroblast-proliferative cascade of desmoid tumour.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^gounder-2023-nirogacestat-desmoid]: Gounder M, Ratan R, Alcindor T, et al. Nirogacestat, a gamma-secretase inhibitor, for desmoid tumors. *N Engl J Med.* 2023;388(10):898-912. [doi:10.1056/NEJMoa2209457](https://doi.org/10.1056/NEJMoa2209457) · [PubMed 36884316](https://pubmed.ncbi.nlm.nih.gov/36884316/)
[^lazar-2008-ctnnb1-desmoid]: Lazar AJ, Tuvin D, Hajibashi S, et al. Specific mutations in the beta-catenin gene (CTNNB1) correlate with local recurrence in sporadic desmoid tumors. *Am J Pathol.* 2008;173(5):1518-1527. [doi:10.2353/ajpath.2008.080475](https://doi.org/10.2353/ajpath.2008.080475) · [PubMed 18832571](https://pubmed.ncbi.nlm.nih.gov/18832571/)
