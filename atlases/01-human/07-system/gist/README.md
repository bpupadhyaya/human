---
schema: human-scale-entry/v1
id: gist
name: GIST
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "GIST is the most common GI mesenchymal tumor, arising from ICC precursors; KIT exon 11 mutations in ~70% and PDGFRA mutations in ~10% drive constitutive RTK signaling. Imatinib is standard first-line; adjuvant imatinib (3 years) reduces recurrence for high-risk GIST."
aliases: ["GIST", "gastrointestinal stromal tumor", "KIT-mutant GIST", "imatinib GIST", "PDGFRA D842V GIST", "SDH-deficient GIST", "CD117 positive tumor"]
sources:
  - id: demetri-2002-imatinib-gist
    type: peer-reviewed
    cite: "Demetri GD, von Mehren M, Blanke CD, et al. Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. N Engl J Med. 2002;347(7):472-480."
    doi: "10.1056/NEJMoa020461"
    pmid: "12181401"
    url: "https://doi.org/10.1056/NEJMoa020461"
  - id: joensuu-2012-ssg18
    type: peer-reviewed
    cite: "Joensuu H, Eriksson M, Sundby Hall K, et al. One vs three years of adjuvant imatinib for operable gastrointestinal stromal tumor: a randomized trial. JAMA. 2012;307(12):1265-1272."
    doi: "10.1001/jama.2012.347"
    pmid: "22453568"
    url: "https://doi.org/10.1001/jama.2012.347"
cross_links:
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGFRA (type III RTK paralog of KIT) is mutated in ~10% of GIST; PDGFRA D842V (exon 18) → imatinib-resistant; avapritinib (NAVIGATOR trial: ORR 84%) is FDA approved for PDGFRA D842V GIST; KIT and PDGFRA are mutually exclusive in GIST."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Sunitinib (VEGFR1/2/3+KIT+PDGFR inhibitor) approved second-line for GIST after imatinib failure (SU11248 trial: PFS 27.3 vs. 6.4 weeks vs. placebo); regorafenib (VEGFR1-3+PDGFR+KIT) approved third-line (GRID trial); ripretinib (pan-KIT/PDGFRA) approved fourth-line."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "KIT-driven PI3K-AKT-mTOR pathway mediates GIST cell survival; KIT exon 17 resistance mutations → secondary resistance to imatinib; PI3K/mTOR inhibitors studied in combination with KIT inhibitors for refractory GIST; mTOR is activated independently of KIT via RAS feedback loops."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC kinase is activated downstream of KIT Tyr568/570 → FAK-SRC complex → invasion in GIST; SRC mediates KIT-independent survival in imatinib-resistant GIST; dasatinib (KIT+SRC) studied in imatinib-resistant GIST; SRC contributes to resistance to selective KIT inhibitors."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "KIT gain-of-function mutations in ~85% of GIST (exon 11 ~70%, exon 9 ~10%); constitutive KIT → PI3K-AKT-mTOR and RAS-ERK → ICC immortalization; imatinib achieves ORR ~80% in exon 11 GIST; dose escalation to 800 mg for exon 9; GIST is the paradigm of KIT-targeted therapy."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1-associated GIST (~2%): germline NF1 LOF → constitutive RAS-GTP → RAS-MAPK-driven GIST; KIT/PDGFRA-WT; small intestinal, multifocal, spindle cell; imatinib ineffective; MEK inhibitors (trametinib) under investigation; distinct from KIT-mutant and SDH-deficient GIST subtypes."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E mutations in ~1% of KIT/PDGFRA-WT GIST; constitutive BRAF → MAPK → GIST proliferation; vemurafenib/dabrafenib active in BRAF V600E GIST; imatinib ineffective; molecular testing distinguishes BRAF V600E from SDH-deficient and NF1 WT-GIST requiring distinct approaches."
  - target: 01-human/07-system/desmoid-tumor
    relation: connects-to
    note: "GIST and desmoid are the main intra-abdominal mesenchymal tumors that mimic each other on imaging but differ fundamentally: GIST is a KIT/PDGFRA-driven Cajal-cell tumor that responds to imatinib and can metastasize; desmoid is a CTNNB1/Wnt fibroblastic tumor that never spreads."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "About 60% of GISTs arise in the stomach (another ~30% in the small intestine), growing from the interstitial cells of Cajal in the muscularis as submucosal masses that can ulcerate and bleed; gastric GISTs are generally less aggressive than small-bowel GISTs of equal size."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "Neurofibromatosis type 1 is a hereditary cause of GIST: germline NF1 loss drives RAS-MAPK in interstitial cells of Cajal, producing multifocal small-intestinal KIT/PDGFRA-wild-type GISTs that resist imatinib — a subtype needing MEK-directed strategies rather than KIT inhibition."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine is the second commonest GIST site after the stomach: arising from interstitial cells of Cajal in the bowel wall, small-bowel GISTs present with occult GI bleeding, anemia or obstruction and are often more aggressive than gastric ones, guiding imatinib therapy."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "GIST links to paraganglioma via the Carney-Stratakis dyad: germline SDH mutations cause SDH-deficient, KIT/PDGFRA-wildtype GISTs together with paragangliomas, a distinct imatinib-resistant subset—so a young patient with GIST plus paraganglioma warrants SDH genetic testing."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "GIST is the commonest mesenchymal tumor of the digestive system: it arises from the interstitial cells of Cajal—the gut's pacemaker cells—anywhere from esophagus to rectum (most often stomach), and its KIT/PDGFRA mutations made it the model disease for imatinib."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Gastric cancer and GIST are the stomach's two principal tumors but biologically opposite: gastric carcinoma is an epithelial adenocarcinoma (H. pylori, CDH1), while GIST is a mesenchymal KIT-driven tumor of Cajal cells—imatinib transforms GIST, not carcinoma."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "GIST and synovial sarcoma are mesenchymal tumors each defined by a single driver: GIST by activating KIT/PDGFRA mutations (targetable with imatinib), synovial sarcoma by the SS18-SSX fusion—proof that one genetic lesion can define, and for GIST drug, a sarcoma."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "GIST and colorectal cancer both occur in the gut wall but from different layers: colorectal cancer arises from mucosal epithelium via APC/Wnt, while GIST grows from KIT-mutant Cajal cells in the muscularis—epithelial carcinoma versus a mesenchymal kinase-driven tumor."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "GIST is often mistaken for a smooth-muscle tumor but isn't: it arises from the interstitial cells of Cajal (the gut's pacemaker cells), not smooth muscle, so KIT/DOG1 staining separates GIST from true leiomyomas and leiomyosarcomas of the GI tract."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is GIST's main metastatic site: gastrointestinal stromal tumors spread hematogenously to the liver and peritoneum rather than lymph nodes, so liver imaging drives staging and follow-up—and imatinib can control even widespread hepatic disease for years."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "GIST growth runs through KIT into the PI3K/AKT pathway: the activating KIT or PDGFRA mutation signals via AKT and MAPK to drive proliferation, so imatinib blocks the receptor while AKT-pathway resistance mutations explain why tumors eventually escape therapy."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "GIST is part of the Carney triad: a subset of GISTs are SDH-deficient (succinate dehydrogenase loss) and occur with paraganglioma and pulmonary chondroma in young patients, a wild-type GIST distinct from the common KIT/PDGFRA-mutant tumors."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "GIST sits in the soft-tissue sarcoma differential with tumors like rhabdomyosarcoma: GIST arises from interstitial cells of Cajal and is defined by KIT/PDGFRA mutation, so immunostaining and molecular testing separate it from other mesenchymal malignancies."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "GIST often bleeds into the gut: these submucosal tumors ulcerate and ooze, so chronic blood loss depletes red cells and iron, making anemia and GI bleeding—rather than the mass itself—a common way GIST first comes to attention."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "GIST and mast cells share a KIT addiction: both depend on the KIT receptor tyrosine kinase, so the same imatinib that blocks KIT in GIST also treats KIT-driven systemic mastocytosis—a striking molecular cousinship across two diseases."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "GIST's response to imatinib is partly immune: beyond blocking KIT, the drug unleashes cytotoxic T and NK cells against the tumor, so combining KIT inhibition with immunotherapy is an active strategy in this kinase-driven sarcoma."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "GIST largely resists radiation: unlike many sarcomas it responds poorly to photon radiotherapy, so radiation is reserved for rare palliation while surgery and KIT-targeted drugs carry treatment—a tumor defined by drugs, not the beam."
  - target: 01-human/03-molecular/sdhb
    relation: connects-to
    note: "A subset of GIST is SDH-deficient rather than KIT-driven: wild-type tumors lacking KIT/PDGFRA mutations often lose SDH function (as in Carney triad), striking young patients and resisting imatinib, so they need different management."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Imatinib fights GIST partly by unleashing NK cells: beyond blocking KIT, the drug boosts natural killer cell activity and IFN-γ release against the tumor, and strong NK responses predict better outcomes—an unexpected immune dimension to a targeted drug."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "GIST is rich in tumor-associated macrophages: they populate the tumor and shift toward an anti-tumor state under imatinib, so the drug's benefit comes partly from reprogramming these innate immune cells, not just from blocking KIT signaling."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "SDH-deficient GIST behaves as if starved of oxygen: losing the SDH enzyme makes succinate pile up and mimic hypoxia, stabilizing HIF and driving these KIT-wild-type tumors common in young patients—a pseudohypoxia like the one in paragangliomas."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "GIST can arise the length of the gut, including the large intestine: though most start in stomach or small bowel, rectal and colonic GISTs occur, so a submucosal mass anywhere along the digestive tract raises the possibility."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Imatinib's benefit in GIST runs partly through dendritic cells: beyond blocking KIT, the drug reshapes the immune microenvironment so dendritic cells better prime T-cell attack, adding an immune dimension to a targeted therapy."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "GIST often announces itself by bleeding iron away: the submucosal tumor erodes and oozes into the gut, so a slow iron-deficiency anemia is a common first sign before the mass is found."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "GISTs are richly vascular tumors: KIT and VEGF signaling recruit endothelial cells to build a dense blood supply, which is why anti-angiogenic drugs like sunitinib work when imatinib fails."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "SDH-deficient GIST travels with adrenal tumors: in the Carney triad and Carney-Stratakis dyad, this GIST subtype co-occurs with paragangliomas, including adrenal pheochromocytomas, sharing an SDH defect."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "GISTs bleed by breaching the gut lining: as the submucosal tumor grows it ulcerates the overlying intestinal epithelium, causing the GI hemorrhage and anemia that often first reveal it."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "GIST's parent cells are pacemakers: the interstitial cells of Cajal generate the gut's electrical slow waves using calcium oscillations, the rhythm of peristalsis from which GIST arises."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "GIST springs from the gut's pacemaker network: interstitial cells of Cajal interface with the enteric neurons that coordinate motility, tying this mesenchymal tumor to the bowel's nervous system."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy ties GIST to the gut's pacemaker: its spindle cells resemble the interstitial cells of Cajal, with bundled cytoplasmic filaments and, in some, tangled skeinoid fibers of extracellular collagen."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "GIST rarely reaches bone: it almost always spreads to the liver and across the peritoneum, but in advanced, drug-resistant disease it can seed skeletal and marrow metastases, an unusual late event."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary spread is the exception in GIST: unlike most sarcomas it spares the lungs early, favoring liver and peritoneum, so lung metastases appear only in late, widely disseminated disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody stain clinches GIST: nearly all express KIT (CD117) and the more specific DOG1, immunostains that distinguish the tumor from the leiomyomas and schwannomas it can resemble in the gut wall."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The later-line drugs strain the heart: when imatinib fails, sunitinib and regorafenib drive hypertension and can impair cardiac function, a vascular toll monitored through the years of targeted therapy."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Indefinite TKI therapy collides with fertility: imatinib is teratogenic and taken for years, so contraception and pregnancy planning are necessary parts of managing GIST in younger patients."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "SDH-deficient GISTs run pseudo-hypoxic: when succinate dehydrogenase fails, succinate piles up and stabilizes HIF, so these KIT/PDGFRA-wild-type tumors behave as if starved of oxygen — the same pathway that drives their paraganglioma partners in Carney triad."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The kinase inhibitors can strain the heart: sunitinib, used when imatinib fails, injures cardiomyocytes and can cause left-ventricular dysfunction and heart failure, so cardiac function is monitored during the long course of therapy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Imatinib does more than block KIT: in GIST it also reshapes immunity, lowering regulatory T cells and unleashing natural killer and T-cell attack on the tumor — an off-target immune boost that adds to its direct effect."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "GIST is a true stromal tumor: it arises from the interstitial cells of Cajal, a mesenchymal lineage akin to fibroblasts, which is why it grows in the gut wall rather than the lining and is named for the stroma it springs from."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "A shared KIT mutation links gut to skin: the same activating KIT changes that drive GIST also power a subset of acral and mucosal melanomas, so both can respond to the KIT inhibitor imatinib."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Constitutive KIT signaling pushes the cell cycle: it drives cyclin D1 to release the G1 checkpoint, the proliferative engine downstream of the mutant receptor that defines GIST."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "GISTs bleed into the gut: ulcerating over the bowel lumen, they cause chronic occult or overt GI bleeding, so iron-deficiency anemia (or melena) is a common way the tumor first declares itself."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy is how GIST survives imatinib: rather than dying, KIT-inhibited cells enter an autophagy-dependent dormancy, a survival mechanism behind residual disease and relapse that combination autophagy blockade aims to overcome."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The tumor and its surgery raise the clot risk: like other abdominal malignancies GIST predisposes to venous thromboembolism, a perioperative hazard during the resections its treatment requires."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Constitutive KIT signals through STAT3: the mutant KIT or PDGFRA driving GIST activates STAT3 among its downstream pathways, supporting proliferation and survival alongside the PI3K-AKT and MAPK arms."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "KIT routes survival through NF-κB too: oncogenic KIT signaling engages NF-κB to sustain GIST-cell survival, part of the network that keeps the tumor alive and contributes to imatinib resistance."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A bleeding or ruptured tumor can seed infection: GISTs ulcerate into the gut lumen and can rupture into the peritoneum, and the major resections they require risk anastomotic leak and abdominal sepsis."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic GI bleeding and inflammation lower the count: beyond the iron-deficiency anemia from tumor ulceration, the inflammatory burden of GIST adds an anemia-of-chronic-disease component, especially in advanced disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its targeted drugs can strain the heart: sunitinib and other later-line tyrosine-kinase inhibitors for GIST cause hypertension and a cardiotoxicity that can precipitate left-ventricular dysfunction and heart failure."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Later-line TKIs are hard on the kidney: sunitinib and regorafenib used in advanced GIST cause hypertension and proteinuria with glomerular injury, which over prolonged therapy can progress to chronic kidney disease."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Its anti-angiogenic TKIs impair healing: sunitinib and regorafenib block VEGF signaling needed for tissue repair, so wounds and surgical sites heal poorly, and GI bleeding from the tumor adds to the burden."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Advanced disease and its drugs hurt nerves: bone and nerve involvement by metastatic GIST, plus the muscle cramps and sensory effects of long-term tyrosine-kinase inhibitors, produce chronic and neuropathic pain."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong targeted therapy weighs on mood: the open-ended daily TKI treatment, its chronic side effects and the threat of resistance and recurrence in GIST contribute to depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its targeted drugs mark the skin: imatinib for GIST commonly causes rashes and periorbital oedema and can lighten skin pigmentation through KIT inhibition, while later TKIs cause hand-foot skin reaction."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It ties to endocrine tumours and thyroid: SDH-deficient GIST clusters with paraganglioma in Carney-Stratakis syndrome, and the TKIs used to treat GIST commonly induce hypothyroidism."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Open-ended targeted therapy breeds worry: the indefinite daily TKI treatment, the threat of resistance and recurrence surveillance in GIST foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its targeted drugs strain the heart: the tyrosine-kinase inhibitors imatinib and especially sunitinib cause cardiotoxicity, heart failure and hypertension during long-term treatment."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It skips the lymph nodes: unlike GI carcinomas, GIST spreads haematogenously to the liver and peritoneum and rarely to lymph nodes, so routine lymphadenectomy is unnecessary."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Sunitinib taxes the kidney: the multi-target inhibitor sunitinib causes hypertension, proteinuria and occasional thrombotic microangiopathy affecting renal function."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its targeted drugs ache the body: imatinib and other KIT inhibitors commonly cause muscle cramps, myalgia and fluid retention with periorbital oedema."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It travels in rare syndromes and to the chest: the Carney triad pairs GIST with pulmonary chondroma and paraganglioma, and advanced GIST can metastasise to the lungs."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It springs from the gut's pacemaker cells: GIST arises from the interstitial cells of Cajal that drive peristalsis, and it is over-represented in neurofibromatosis type 1."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "The model of targeted therapy in solid tumours: imatinib against KIT, with sunitinib, regorafenib, avapritinib and ripretinib, transformed GIST from chemoresistant to a manageable cancer."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "A shared imatinib triumph: GIST (KIT-driven) and chronic myeloid leukaemia (BCR-ABL-driven) were the twin proofs that a single kinase inhibitor could control cancer."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Conventional chemo fails it: GIST is resistant to cytotoxic chemotherapy, which is why kinase inhibitors rather than chemo became its treatment."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold tumour: GIST responds poorly to checkpoint inhibitors as monotherapy because of its low mutational burden, though combinations with KIT inhibitors that may boost antigen presentation are under trial investigation."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "One gene, two druggabilities: GIST is driven by KIT juxtamembrane (exon 11) and extracellular (exon 9) mutations that imatinib blocks, whereas core-binding-factor AML and mastocytosis carry KIT D816V in the activation loop that resists imatinib."
  - target: 01-human/07-system/mpnst
    relation: connects-to
    note: "Two tumours from one lost gene: germline NF1 loss drives both NF1-associated GIST (KIT/PDGFRA-wildtype, RAS-MAPK-driven) and malignant peripheral nerve sheath tumours, so an NF1 patient's abdominal mass may be either—distinct neoplasms sharing a RAS engine."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Liver is the dominant metastatic site: GIST spreads within the abdomen, seeding the hepatic lobule and peritoneum, the pattern that defines advanced disease and drives lifelong imatinib."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Shared SDH loss: SDH-deficient GIST (Carney-Stratakis) and SDH-deficient renal cell carcinoma both arise from succinate-dehydrogenase failure, a metabolic route to two very different tumours."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "KIT's downstream switch: the mutant KIT and PDGFRA receptors of GIST signal through the MAPK/ERK pathway, the proliferative effector that imatinib and successor inhibitors shut off."
  - target: 01-human/07-system/neuroendocrine-tumors
    relation: connects-to
    note: "Two submucosal gut tumours: GISTs (KIT-driven, from interstitial cells of Cajal) and gastrointestinal neuroendocrine tumours both present as submucosal masses but arise from different cells and need different therapy."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Pacemaker cells of two organs: GIST arises from the interstitial cells of Cajal—the gut's electrical pacemaker—conceptually paralleling the cardiac conduction system that paces the heart."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Uncommon distant spread: although GIST metastasises mainly to the liver and peritoneum, advanced disease can reach the lungs and bone, unusual sites for this sarcoma."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Wild-type GIST driver: SDH-deficient (KIT/PDGFRA wild-type) GISTs overexpress IGF1R, making IGF-1 signalling a therapeutic target in this distinct, often paediatric subtype."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Rare targetable fusion: a small subset of quadruple-wild-type GISTs harbour NTRK gene fusions, rendering them sensitive to TRK inhibitors beyond the usual KIT-directed drugs."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Another wild-type lever: FGFR fusions and activation arise in some KIT/PDGFRA wild-type GISTs, an alternative oncogenic driver targetable with FGFR inhibitors."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic silencing: EZH2-mediated PRC2 repression of tumour-suppressor genes contributes to GIST progression, an epigenetic vulnerability under study."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Downstream oncogene: KIT/PDGFRA signalling activates MYC in GIST, driving the biosynthetic and proliferative programme of the tumour."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Malignant progression: TERT promoter mutations and reactivation mark the progression of GIST toward higher-grade, metastatic behaviour."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Progression and resistance: CDKN2A deletion releases the cell-cycle brake in GIST, marking malignant progression and contributing to resistance to KIT-targeted imatinib therapy."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "High-risk transformation: TP53 alterations accumulate as GIST progresses from low-risk to high-grade, metastatic disease, beyond the initiating KIT or PDGFRA mutation."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the GIST stroma, shaping a microenvironment that supports tumour growth and modulates response to therapy."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Imatinib apoptosis: imatinib kills GIST cells by relieving the anti-apoptotic signal of the mutant KIT receptor, restoring caspase-3-mediated apoptosis — the basis for the dramatic responses that transformed GIST therapy."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Metastatic homing: CXCR4 on GIST cells follows CXCL12 gradients to the liver and peritoneum, the dominant sites of the metastatic spread that determines prognosis in the disease."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "Pseudohypoxia in SDH-deficient GIST: in wild-type GIST with SDH deficiency, accumulating succinate inhibits the EGLN1/PHD prolyl hydroxylases that mark HIF for degradation, locking in a pseudohypoxic programme shared with SDH-mutant paraganglioma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNA hypermethylation: in SDH-deficient wild-type GIST, accumulated succinate also inhibits the TET DNA-demethylases, producing a globally hypermethylated genome that drives a distinct epigenetic subtype of the disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptotic response: imatinib's killing of KIT-driven GIST depends on tipping the BCL-2-family balance toward apoptosis, and persistent anti-apoptotic signalling leaves a residual drug-tolerant cell population that underlies relapse on therapy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Survival signalling: oncogenic KIT signals through AKT to inactivate FOXO transcription factors, removing a pro-apoptotic brake — part of the survival programme that imatinib reverses by restoring FOXO activity in GIST cells."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K resistance: KIT and PDGFRA activate PI3K (AKT and mTOR already mapped), and acquired PIK3CA mutations are a mechanism of secondary resistance to imatinib in GIST."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss-of-brake: PTEN normally restrains the same PI3K-AKT signalling, and its loss amplifies survival signalling, contributing to tyrosine-kinase-inhibitor resistance in GIST."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle output: the cyclin-D1-CDK4/6 axis (cyclin-D1 mapped, with CDKN2A loss in malignant GIST) releases E2F1 to drive the proliferation that distinguishes high-risk from indolent tumours."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Downstream RAS drive: RAS-MAPK signalling (NF1 and BRAF already mapped) lies downstream of the KIT and PDGFRA driver mutations, transmitting the proliferative signal of gastrointestinal stromal tumour."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Progression checkpoint: deregulation of the RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) marks the progression of GIST toward higher-risk, more aggressive disease."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "KIT survival signalling: JAK-STAT3 signalling (STAT3 already mapped) contributes to the survival signalling downstream of KIT in gastrointestinal stromal tumour."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "In SDH-deficient GIST, succinate accumulation stabilises HIF-2α (EPAS1), producing a pseudohypoxic transcriptional program (EGLN1 and HIF-1α mapped) that drives tumorigenesis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the survival and stromal interactions of gastrointestinal stromal tumours."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β within the tumour microenvironment modulates the invasive and immune behaviour of GIST."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of GIST, relevant to combining immunotherapy with KIT-targeted therapy."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression downstream of KIT/PDGFRA in GIST."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment of gastrointestinal stromal tumour."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β supports the survival signaling downstream of KIT/PDGFRA in gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic killing contributes to the imatinib-enhanced antitumor immune response in gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory microenvironment of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of gastrointestinal stromal tumor, particularly in SDH-deficient subtypes."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the proliferation and differentiation biology of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory tumor microenvironment of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the tumor microenvironment and metastatic interactions of gastrointestinal stromal tumor."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Imatinib immunomodulation: beyond blocking KIT, imatinib has immune effects, and MHC class II antigen presentation shapes the T-cell response that may contribute to the durable control of gastrointestinal stromal tumour."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Resistance signalling: the AXL receptor tyrosine kinase provides a bypass survival signal that can drive resistance to KIT-directed therapy (KIT already mapped) in gastrointestinal stromal tumour, a mechanism of escape beyond secondary KIT mutations."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint context: PD-1-mediated T-cell exhaustion limits anti-tumour immunity in gastrointestinal stromal tumour, and checkpoint blockade is being explored alongside tyrosine-kinase inhibitors, especially in KIT/PDGFRA-wild-type disease."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Gastrointestinal bleeding: mucosal ulceration over a gastrointestinal stromal tumour causes acute or chronic bleeding, and the resulting anaemia with falling haemoglobin is the commonest presentation prompting endoscopy and diagnosis."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "TKI cardiotoxicity: the multitargeted kinase inhibitors sunitinib and regorafenib used after imatinib (KIT already mapped) cause hypertension and cardiac dysfunction, and troponin elevation marks the myocardial injury of this class toxicity in GIST."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immunity: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) supports the anti-tumour immunity that checkpoint blockade aims to unleash in gastrointestinal stromal tumour, especially the KIT/PDGFRA-wild-type subtype."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "NF1-associated GIST: neurofibromatosis type 1 (NF1 already mapped) predisposes to multiple small-bowel GISTs that are typically KIT/PDGFRA-wild-type and imatinib-resistant, one of the wild-type subtypes of the tumour."
  - target: 01-human/07-system/carney-complex
    relation: connects-to
    note: "Carney triad and dyad: SDH-deficient wild-type GIST (SDHB already mapped) occurs in the Carney triad with paraganglioma and pulmonary chondroma, and the Carney-Stratakis dyad, linking GIST to the paraganglioma syndromes."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion relevant to the checkpoint immunotherapy explored in wild-type GIST."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the gastrointestinal stromal tumour."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumour-associated macrophages: the macrophages (CCL2 already mapped) infiltrate the GIST stroma, and their M2 polarisation (IL-4 already mapped) supports the immunosuppression relevant to the immunotherapy explored in wild-type disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron-deficiency anaemia: the mucosal-ulcerating GIST commonly bleeds into the gut, causing the iron-deficiency anaemia (haemoglobin already mapped) that is a frequent presenting sign of the tumour."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 stromal arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the immunosuppressive stroma relevant to the immunotherapy explored in wild-type GIST."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Mesenteric adipokine: leptin from the GI and mesenteric adipose microenvironment signals to the GIST, part of the metabolic crosstalk of the gastrointestinal stromal tumour."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and, with the chronic gut bleeding, contributes to the anaemia (haemoglobin already mapped) of GIST."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Mesenteric adipokine: adiponectin, with leptin (already mapped), is part of the GI/mesenteric-adipose adipokine crosstalk of the GIST microenvironment."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the GIST microenvironment."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Prognostic neutrophils: the tumour-associated neutrophils and the neutrophil-lymphocyte ratio (S100A8/9 already mapped) are studied prognostic markers in GIST."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the imatinib-induced immune activation and checkpoint (PD-1 already mapped) trials in GIST."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the gastrointestinal stromal tumour."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of GIST."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the gastrointestinal stromal tumour."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the GIST microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the gastrointestinal stromal tumour."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the gastrointestinal stromal tumour."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the gastrointestinal stromal tumour."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the macrophage-rich (already mapped) stroma of the gastrointestinal stromal tumour."
---

# GIST

## Overview

**Gastrointestinal stromal tumor (GIST)** is the most common primary mesenchymal neoplasm of the GI tract (~5,000-6,000 new cases/year in the US), arising from the interstitial cells of Cajal (ICC) — the pacemaker cells of GI peristalsis — or ICC precursors. GISTs express KIT (CD117) in ~95% of cases and are driven by **gain-of-function mutations** in KIT (~85%) or PDGFRA (~10%), making GIST the paradigmatic molecularly-targeted solid tumor. The landmark 2001-2002 trial demonstrating imatinib (STI571) activity in KIT-mutant advanced GIST — with unprecedented ORR of ~80% in a disease previously unresponsive to conventional chemotherapy — established GIST as proof-of-concept for oncogene-driven targeted therapy in solid tumors [^demetri-2002-imatinib-gist]. Subsequent SSG XVIII trial demonstrated that 3 years of adjuvant imatinib versus 1 year is superior for high-risk localized GIST [^joensuu-2012-ssg18].

**Epidemiology:**
- ~5,000-6,000 new cases/year in US; worldwide ~14,000/year; 5th-6th decade peak; M:F equal
- Site distribution: Stomach ~60% (best prognosis), small intestine ~30%, colon/rectum ~5%, esophagus ~1-2%, extra-GI (omentum, mesentery) ~1%
- 5-year survival: ~80-90% for localized GIST; ~50-55% for metastatic KIT-mutant GIST with imatinib; ~20-30% for PDGFRA D842V (historically poor, improving with avapritinib)
- Metastasis pattern: Liver and peritoneal metastases predominant; LN and lung involvement uncommon (unlike carcinomas)

**GIST subtypes by molecular driver:**
- **KIT exon 11 (~70%):** Best imatinib response (ORR >80%); del557-558 most common specific mutation; gastric and small intestinal; Miettinen low-risk to high-risk spectrum
- **KIT exon 9 (~10%):** Ala502_Tyr503dup; extracellular domain; more aggressive; small intestine predominant; higher-dose imatinib 800 mg/day or sunitinib preferred
- **KIT exon 13/17 (~3-5%):** Kinase domain; less common; mixed imatinib sensitivity
- **PDGFRA exon 18 D842V (~6%):** Stomach; epithelioid morphology; imatinib resistant; avapritinib (NAVIGATOR: ORR 84%)
- **PDGFRA exon 18 non-D842V, PDGFRA exon 12/14:** Partial imatinib sensitivity; less common
- **SDH-deficient (~5%):** KIT/PDGFRA WT; SDHA/B/C/D mutation (germline or somatic); young women; gastric; nodal metastasis; indolent multifocal course; no effective targeted therapy; associated with Carney triad and Carney-Stratakis syndrome
- **NF1-associated (~2%):** NF1 germline mutation → RAS activation; KIT/PDGFRA WT; small intestinal multiple; imatinib ineffective; MEK inhibitor studied
- **BRAF V600E (~1%):** Rare KIT/PDGFRA-WT GIST; vemurafenib/dabrafenib active
- **Quadruple WT (~1%):** No KIT/PDGFRA/SDH/BRAF mutations; FGFR1 fusions or other alterations

## Structure

### Histological subtypes

**Spindle cell GIST (~70%):**
Fascicles of uniform spindle cells with eosinophilic or amphophilic cytoplasm; perinuclear cytoplasmic vacuoles (characteristic); skenoid fibers (periodic acid-Schiff positive); most common in stomach

**Epithelioid GIST (~20%):**
Rounded cells with clear or eosinophilic cytoplasm; nest pattern; more common in PDGFRA-mutant gastric GIST; larger mitochondria; may lack CD117 by IHC (particularly PDGFRA-mutant)

**Mixed spindle/epithelioid (~10%):**
Both morphologies in same tumor; associated with gastric location and higher-grade behavior

**IHC markers:**
- CD117 (KIT): >95% positive; cytoplasmic or perinuclear dot pattern; most specific for GIST among mesenchymal tumors
- DOG1 (ANO1, chloride channel): >95% positive; even more sensitive and specific than KIT for GIST; positive in some KIT-negative GIST (PDGFRA-mutant, SDH-deficient)
- CD34: ~70%; loss may indicate more aggressive biology
- SMA (smooth muscle actin): ~30% (weak focal); GIST is not a smooth muscle tumor
- S100: ~5%; negative helps distinguish from neural tumors
- Desmin: ~5%; negative helps distinguish from true smooth muscle tumors (leiomyosarcoma)

### Risk stratification (Miettinen-Lasota criteria)

Risk is based on tumor size (cm), mitotic rate (per 50 HPF), and primary site:

| Location | Size | Mitotic rate | Risk |
|----------|------|--------------|------|
| Stomach | ≤2 cm | ≤5/50 HPF | None |
| Stomach | 2-5 cm | ≤5/50 HPF | Very low |
| Stomach | 5-10 cm | ≤5/50 HPF | Low |
| Stomach | >10 cm | ≤5/50 HPF | Moderate |
| Small intestine | ≤2 cm | ≤5/50 HPF | None |
| Small intestine | 2-5 cm | ≤5/50 HPF | Low |
| Small intestine | 5-10 cm | ≤5/50 HPF | Moderate-high |
| Any site | Any size | >5/50 HPF | High (>50%) |
| Any site | Rupture | Any | High |

Small intestinal GIST has higher recurrence risk than gastric GIST of same size/mitotic rate.

## Function

### ICC pacemaker biology

**Normal ICC function:**
ICC (Kit+/DOG1+/CD34+) form a network in the myenteric plexus and submucous plexus of the GI wall → generate slow waves (electrical pacemaker activity) → coordinate smooth muscle contraction → peristalsis. ICC require continuous KIT-SCF signaling for survival (KIT W/Wv mice → no ICC → intestinal pseudo-obstruction). GIST cells retain this ICC signature (CD117, DOG1, ANO1 expression) while losing normal ICC pacemaker function.

**GIST as ICC disease:**
KIT gain-of-function mutation in an ICC precursor or ICC → constitutive KIT signaling → ICC/GIST progenitor proliferation → clonal expansion → GIST tumor. GIST cells maintain ICC morphology (spindle cells with perinuclear vacuoles = displaced organelles from vacuolated ICC cytoplasm) and ICC markers. This explains why GIST does not respond to conventional sarcoma chemotherapy (doxorubicin, ifosfamide) — it is fundamentally a disease of ICC biology, not smooth muscle or nerve sheath biology.

### KIT-driven oncogenesis in GIST

**KIT exon 11 juxtamembrane mutations:**
JMD restrains KIT kinase in inactive state; del557-558 removes inhibitory residues → constitutive kinase dimerization and activation independent of SCF → autonomous PI3K/RAS/STAT signaling → ICC progenitor immortalization → GIST. Exon 11 del557-558 is associated with higher risk (more aggressive) gastric GIST vs. point mutations which may be found in low-risk GIST.

**KIT exon 9 mutations:**
Ala502_Tyr503dup in the extracellular D5 domain → constitutive receptor dimerization by mimicking ligand-induced D4-D5 interactions → KIT kinase activation without SCF; these tumors have a constitutively dimerized conformation (vs. monomer activation in exon 11); imatinib IC50 is higher (~3×) for exon 9 vs. exon 11 → higher-dose imatinib (800 mg) or sunitinib preferred.

## Pathology

### Staging and workup

**TNM staging (AJCC 8th edition — separate staging for stomach vs. non-stomach GIST):**
- T1: ≤2 cm; T2: >2 to ≤5 cm; T3: >5 to ≤10 cm; T4: >10 cm
- N0: No nodal involvement (GIST rarely spreads to lymph nodes, unlike carcinoma)
- M1: Distant metastasis (liver, peritoneum most common)
- **N+ is very rare in GIST** (except SDH-deficient GIST which can spread to local nodes)

**Staging workup:**
- CT chest/abdomen/pelvis with contrast: Standard staging; GIST is hypervascular on arterial phase (KIT/VEGF expression); peritoneal studding assessment
- MRI abdomen/pelvis: Preferred for rectal GIST; superior soft tissue resolution vs. CT
- FDG-PET/CT: Highly FDG-avid; particularly useful for early response assessment (response visible on PET within days of imatinib initiation — Choi criteria)
- Biopsy: EUS-guided (endoscopic ultrasound) for gastric GIST; percutaneous for large tumors; avoid laparoscopic biopsy of ruptured-risk tumors (rupture → peritoneal seeding)
- Molecular: KIT exon 9/11/13/17 + PDGFRA exon 12/14/18 mutation testing → essential for treatment decision (imatinib dose, avapritinib vs. imatinib for D842V)
- SDHB IHC: Negative = SDH-deficient GIST; recommend germline SDHA/B/C/D testing for SDH-deficient GIST

**Response assessment (Choi criteria):**
Standard RECIST underestimates GIST response to imatinib (KIT-inhibited GIST become cystic/myxoid → may increase in size by RECIST yet respond molecularly). Choi criteria: Response = CT attenuation decrease ≥15 HU or size decrease ≥10% on CT; better correlates with PFS than RECIST for GIST.

### Treatment

**Localized/resectable GIST:**
- **Surgery (en-bloc resection):** Complete macroscopic resection (R0) is curative for localized GIST; no routine lymph node dissection; laparoscopic approach for small (<5 cm) tumors in favorable locations; open for large or adherent tumors; avoid tumor rupture (converts to high-risk, peritoneal contamination)
- **Neoadjuvant imatinib:** For locally advanced/technically unresectable GIST → reduce tumor size → facilitate R0 resection; response in ~80%; continue neoadjuvant for 6-12 months then reassess; RTOG 0132 and other trials support pre-operative imatinib
- **Adjuvant imatinib (400 mg/day × 3 years):** [^joensuu-2012-ssg18] SSG XVIII trial: 3 years vs. 1 year adjuvant imatinib → RFS 65.6% vs. 47.9% at 5 years; OS benefit at 5 years; recommended for high-risk GIST (size >10 cm, mitotic rate >10/50 HPF, small intestinal location, rupture); mutation testing essential (KIT exon 11 → adjuvant benefit; exon 9 → may need 800 mg; PDGFRA D842V → imatinib ineffective → omit adjuvant; SDH-deficient → no adjuvant benefit)
- **Very low/low risk GIST:** Surgery alone; no adjuvant (ACOSOG Z9001: low-risk GIST no benefit from imatinib); annual surveillance imaging × 5 years

**Advanced/metastatic GIST:**

**First-line:**
- **Imatinib 400 mg/day:** [^demetri-2002-imatinib-gist] ORR ~80% for KIT exon 11; ~40-50% for exon 9; median PFS ~24 months; OS >50 months; FDA approved 2002; continue indefinitely (discontinuation → rapid progression); dose-escalate to 800 mg if progression on 400 mg (especially exon 9)
- **KIT exon 9:** Imatinib 800 mg/day or sunitinib as preferred first-line option (non-inferior vs. imatinib 400 mg in some analyses)
- **PDGFRA D842V:** Avapritinib 300 mg/day (NAVIGATOR trial: ORR 84%, CR 9%); FDA approved 2020; not imatinib

**Second-line:**
- **Sunitinib 50 mg/day (4 weeks on/2 weeks off):** SU11248 trial: PFS 27.3 vs. 6.4 weeks vs. placebo; ORR 7% (many stable disease); FDA approved 2006; continuous dosing 37.5 mg/day also used; toxicities: hand-foot syndrome, hypertension, hypothyroidism, fatigue; active against KIT exon 13 (V654A) and some exon 17 mutations

**Third-line:**
- **Regorafenib 160 mg/day (3 weeks on/1 week off):** GRID trial: PFS 4.8 vs. 0.9 months vs. placebo; FDA approved 2013; inhibits VEGFR+PDGFR+KIT+RET+BRAF; toxicities: hand-foot syndrome, fatigue, hypertension

**Fourth-line:**
- **Ripretinib 150 mg/day:** INVICTUS trial: PFS 6.3 vs. 1.0 months vs. placebo; ORR 9%; FDA approved 2020; pan-KIT/PDGFRA switch-pocket inhibitor; active against most secondary resistance mutations; toxicities: alopecia, myalgia, fatigue

**SDH-deficient GIST:**
No approved targeted therapy; sunitinib may have modest activity; clinical trials (HIF-2α inhibitor belzutifan, HIF pathway); surgery for resectable lesions; watch-and-wait for indolent multifocal disease

## Connections

- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGFRA (type III RTK paralog of KIT) is mutated in ~10% of GIST; PDGFRA D842V (exon 18) → imatinib-resistant; avapritinib (NAVIGATOR trial: ORR 84%) is FDA approved for PDGFRA D842V GIST; KIT and PDGFRA are mutually exclusive in GIST.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Sunitinib (VEGFR1/2/3+KIT+PDGFR inhibitor) approved second-line for GIST after imatinib failure (SU11248 trial: PFS 27.3 vs. 6.4 weeks vs. placebo); regorafenib (VEGFR1-3+PDGFR+KIT) approved third-line (GRID trial); ripretinib (pan-KIT/PDGFRA) approved fourth-line.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — KIT-driven PI3K-AKT-mTOR pathway mediates GIST cell survival; KIT exon 17 resistance mutations → secondary resistance to imatinib; PI3K/mTOR inhibitors studied in combination with KIT inhibitors for refractory GIST; mTOR is activated independently of KIT via RAS feedback loops.
- `connects-to` → **[SRC kinase](../../03-molecular/src-kinase/README.md)** — SRC kinase is activated downstream of KIT Tyr568/570 → FAK-SRC complex → invasion in GIST; SRC mediates KIT-independent survival in imatinib-resistant GIST; dasatinib (KIT+SRC inhibitor) studied in imatinib-resistant GIST; SRC contributes to resistance to selective KIT inhibitors.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT gain-of-function mutations in ~85% of GIST (exon 11 ~70%, exon 9 ~10%); constitutive KIT → PI3K-AKT-mTOR and RAS-ERK → ICC immortalization; imatinib achieves ORR ~80% in exon 11 GIST; dose escalation to 800 mg for exon 9; GIST is the paradigm of KIT-targeted therapy.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1-associated GIST (~2%): germline NF1 LOF → constitutive RAS-GTP → RAS-MAPK-driven GIST; KIT/PDGFRA-WT; small intestinal, multifocal, spindle cell; imatinib ineffective; MEK inhibitors (trametinib) under investigation; distinct from KIT-mutant and SDH-deficient GIST subtypes.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E mutations in ~1% of KIT/PDGFRA-WT GIST; constitutive BRAF → MAPK → GIST proliferation; vemurafenib/dabrafenib active in BRAF V600E GIST; imatinib ineffective; molecular testing distinguishes BRAF V600E from SDH-deficient and NF1 WT-GIST requiring distinct approaches.
- `connects-to` → **[Desmoid Tumor](../desmoid-tumor/README.md)** — GIST and desmoid are the main intra-abdominal mesenchymal tumors that mimic each other on imaging but differ fundamentally: GIST is a KIT/PDGFRA-driven Cajal-cell tumor that responds to imatinib and can metastasize; desmoid is a CTNNB1/Wnt fibroblastic tumor that never spreads.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — About 60% of GISTs arise in the stomach (another ~30% in the small intestine), growing from the interstitial cells of Cajal in the muscularis as submucosal masses that can ulcerate and bleed; gastric GISTs are generally less aggressive than small-bowel GISTs of equal size.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — Neurofibromatosis type 1 is a hereditary cause of GIST: germline NF1 loss drives RAS-MAPK in interstitial cells of Cajal, producing multifocal small-intestinal KIT/PDGFRA-wild-type GISTs that resist imatinib — a subtype needing MEK-directed strategies rather than KIT inhibition.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine is the second commonest GIST site after the stomach: arising from interstitial cells of Cajal in the bowel wall, small-bowel GISTs present with occult GI bleeding, anemia or obstruction and are often more aggressive than gastric ones, guiding imatinib therapy.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — GIST links to paraganglioma via the Carney-Stratakis dyad: germline SDH mutations cause SDH-deficient, KIT/PDGFRA-wildtype GISTs together with paragangliomas, a distinct imatinib-resistant subset—so a young patient with GIST plus paraganglioma warrants SDH genetic testing.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — GIST is the commonest mesenchymal tumor of the digestive system: it arises from the interstitial cells of Cajal—the gut's pacemaker cells—anywhere from esophagus to rectum (most often stomach), and its KIT/PDGFRA mutations made it the model disease for imatinib.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Gastric cancer and GIST are the stomach's two principal tumors but biologically opposite: gastric carcinoma is an epithelial adenocarcinoma (H. pylori, CDH1), while GIST is a mesenchymal KIT-driven tumor of Cajal cells—imatinib transforms GIST, not carcinoma.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — GIST and synovial sarcoma are mesenchymal tumors each defined by a single driver: GIST by activating KIT/PDGFRA mutations (targetable with imatinib), synovial sarcoma by the SS18-SSX fusion—proof that one genetic lesion can define, and for GIST drug, a sarcoma.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — GIST and colorectal cancer both occur in the gut wall but from different layers: colorectal cancer arises from mucosal epithelium via APC/Wnt, while GIST grows from KIT-mutant Cajal cells in the muscularis—epithelial carcinoma versus a mesenchymal kinase-driven tumor.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — GIST is often mistaken for a smooth-muscle tumor but isn't: it arises from the interstitial cells of Cajal (the gut's pacemaker cells), not smooth muscle, so KIT/DOG1 staining separates GIST from true leiomyomas and leiomyosarcomas of the GI tract.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is GIST's main metastatic site: gastrointestinal stromal tumors spread hematogenously to the liver and peritoneum rather than lymph nodes, so liver imaging drives staging and follow-up—and imatinib can control even widespread hepatic disease for years.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — GIST growth runs through KIT into the PI3K/AKT pathway: the activating KIT or PDGFRA mutation signals via AKT and MAPK to drive proliferation, so imatinib blocks the receptor while AKT-pathway resistance mutations explain why tumors eventually escape therapy.
- `connects-to` → **[Checkpoint inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold tumour: GIST responds poorly to checkpoint inhibitors as monotherapy because of its low mutational burden, though combinations with KIT inhibitors that may boost antigen presentation are under trial investigation.
- `connects-to` → **[AML](../aml/README.md)** — One gene, two druggabilities: GIST is driven by KIT juxtamembrane (exon 11) and extracellular (exon 9) mutations that imatinib blocks, whereas core-binding-factor AML and mastocytosis carry KIT D816V in the activation loop that resists imatinib.
- `connects-to` → **[MPNST](../mpnst/README.md)** — Two tumours from one lost gene: germline NF1 loss drives both NF1-associated GIST (KIT/PDGFRA-wildtype, RAS-MAPK-driven) and malignant peripheral nerve sheath tumours, so an NF1 patient's abdominal mass may be either—distinct neoplasms sharing a RAS engine.
- `connects-to` → **[Carney Complex](../carney-complex/README.md)** — GIST is part of the Carney triad: a subset of GISTs are SDH-deficient (succinate dehydrogenase loss) and occur with paraganglioma and pulmonary chondroma in young patients, a wild-type GIST distinct from the common KIT/PDGFRA-mutant tumors.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — GIST sits in the soft-tissue sarcoma differential with tumors like rhabdomyosarcoma: GIST arises from interstitial cells of Cajal and is defined by KIT/PDGFRA mutation, so immunostaining and molecular testing separate it from other mesenchymal malignancies.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — GIST often bleeds into the gut: these submucosal tumors ulcerate and ooze, so chronic blood loss depletes red cells and iron, making anemia and GI bleeding—rather than the mass itself—a common way GIST first comes to attention.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — GIST and mast cells share a KIT addiction: both depend on the KIT receptor tyrosine kinase, so the same imatinib that blocks KIT in GIST also treats KIT-driven systemic mastocytosis—a striking molecular cousinship across two diseases.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — GIST's response to imatinib is partly immune: beyond blocking KIT, the drug unleashes cytotoxic T and NK cells against the tumor, so combining KIT inhibition with immunotherapy is an active strategy in this kinase-driven sarcoma.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — GIST largely resists radiation: unlike many sarcomas it responds poorly to photon radiotherapy, so radiation is reserved for rare palliation while surgery and KIT-targeted drugs carry treatment—a tumor defined by drugs, not the beam.
- `connects-to` → **[SDHB](../../03-molecular/sdhb/README.md)** — A subset of GIST is SDH-deficient rather than KIT-driven: wild-type tumors lacking KIT/PDGFRA mutations often lose SDH function (as in Carney triad), striking young patients and resisting imatinib, so they need different management.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Imatinib fights GIST partly by unleashing NK cells: beyond blocking KIT, the drug boosts natural killer cell activity and IFN-γ release against the tumor, and strong NK responses predict better outcomes—an unexpected immune dimension to a targeted drug.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — GIST is rich in tumor-associated macrophages: they populate the tumor and shift toward an anti-tumor state under imatinib, so the drug's benefit comes partly from reprogramming these innate immune cells, not just from blocking KIT signaling.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — SDH-deficient GIST behaves as if starved of oxygen: losing the SDH enzyme makes succinate pile up and mimic hypoxia, stabilizing HIF and driving these KIT-wild-type tumors common in young patients—a pseudohypoxia like the one in paragangliomas.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — GIST can arise the length of the gut, including the large intestine: though most start in stomach or small bowel, rectal and colonic GISTs occur, so a submucosal mass anywhere along the digestive tract raises the possibility.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Imatinib's benefit in GIST runs partly through dendritic cells: beyond blocking KIT, the drug reshapes the immune microenvironment so dendritic cells better prime T-cell attack, adding an immune dimension to a targeted therapy.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — GIST often announces itself by bleeding iron away: the submucosal tumor erodes and oozes into the gut, so a slow iron-deficiency anemia is a common first sign before the mass is found.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — GISTs are richly vascular tumors: KIT and VEGF signaling recruit endothelial cells to build a dense blood supply, which is why anti-angiogenic drugs like sunitinib work when imatinib fails.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — SDH-deficient GIST travels with adrenal tumors: in the Carney triad and Carney-Stratakis dyad, this GIST subtype co-occurs with paragangliomas, including adrenal pheochromocytomas, sharing an SDH defect.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — GISTs bleed by breaching the gut lining: as the submucosal tumor grows it ulcerates the overlying intestinal epithelium, causing the GI hemorrhage and anemia that often first reveal it.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — GIST's parent cells are pacemakers: the interstitial cells of Cajal generate the gut's electrical slow waves using calcium oscillations, the rhythm of peristalsis from which GIST arises.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — GIST springs from the gut's pacemaker network: interstitial cells of Cajal interface with the enteric neurons that coordinate motility, tying this mesenchymal tumor to the bowel's nervous system.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy ties GIST to the gut's pacemaker: its spindle cells resemble the interstitial cells of Cajal, with bundled cytoplasmic filaments and, in some, tangled skeinoid fibers of extracellular collagen.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — GIST rarely reaches bone: it almost always spreads to the liver and across the peritoneum, but in advanced, drug-resistant disease it can seed skeletal and marrow metastases, an unusual late event.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary spread is the exception in GIST: unlike most sarcomas it spares the lungs early, favoring liver and peritoneum, so lung metastases appear only in late, widely disseminated disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody stain clinches GIST: nearly all express KIT (CD117) and the more specific DOG1, immunostains that distinguish the tumor from the leiomyomas and schwannomas it can resemble in the gut wall.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The later-line drugs strain the heart: when imatinib fails, sunitinib and regorafenib drive hypertension and can impair cardiac function, a vascular toll monitored through the years of targeted therapy.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Indefinite TKI therapy collides with fertility: imatinib is teratogenic and taken for years, so contraception and pregnancy planning are necessary parts of managing GIST in younger patients.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — SDH-deficient GISTs run pseudo-hypoxic: when succinate dehydrogenase fails, succinate piles up and stabilizes HIF, so these KIT/PDGFRA-wild-type tumors behave as if starved of oxygen — the same pathway that drives their paraganglioma partners in Carney triad.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The kinase inhibitors can strain the heart: sunitinib, used when imatinib fails, injures cardiomyocytes and can cause left-ventricular dysfunction and heart failure, so cardiac function is monitored during the long course of therapy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Imatinib does more than block KIT: in GIST it also reshapes immunity, lowering regulatory T cells and unleashing natural killer and T-cell attack on the tumor — an off-target immune boost that adds to its direct effect.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — GIST is a true stromal tumor: it arises from the interstitial cells of Cajal, a mesenchymal lineage akin to fibroblasts, which is why it grows in the gut wall rather than the lining and is named for the stroma it springs from.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — A shared KIT mutation links gut to skin: the same activating KIT changes that drive GIST also power a subset of acral and mucosal melanomas, so both can respond to the KIT inhibitor imatinib.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Constitutive KIT signaling pushes the cell cycle: it drives cyclin D1 to release the G1 checkpoint, the proliferative engine downstream of the mutant receptor that defines GIST.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — GISTs bleed into the gut: ulcerating over the bowel lumen, they cause chronic occult or overt GI bleeding, so iron-deficiency anemia (or melena) is a common way the tumor first declares itself.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy is how GIST survives imatinib: rather than dying, KIT-inhibited cells enter an autophagy-dependent dormancy, a survival mechanism behind residual disease and relapse that combination autophagy blockade aims to overcome.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The tumor and its surgery raise the clot risk: like other abdominal malignancies GIST predisposes to venous thromboembolism, a perioperative hazard during the resections its treatment requires.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Constitutive KIT signals through STAT3: the mutant KIT or PDGFRA driving GIST activates STAT3 among its downstream pathways, supporting proliferation and survival alongside the PI3K-AKT and MAPK arms.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — KIT routes survival through NF-κB too: oncogenic KIT signaling engages NF-κB to sustain GIST-cell survival, part of the network that keeps the tumor alive and contributes to imatinib resistance.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A bleeding or ruptured tumor can seed infection: GISTs ulcerate into the gut lumen and can rupture into the peritoneum, and the major resections they require risk anastomotic leak and abdominal sepsis.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic GI bleeding and inflammation lower the count: beyond the iron-deficiency anemia from tumor ulceration, the inflammatory burden of GIST adds an anemia-of-chronic-disease component, especially in advanced disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its targeted drugs can strain the heart: sunitinib and other later-line tyrosine-kinase inhibitors for GIST cause hypertension and a cardiotoxicity that can precipitate left-ventricular dysfunction and heart failure.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Later-line TKIs are hard on the kidney: sunitinib and regorafenib used in advanced GIST cause hypertension and proteinuria with glomerular injury, which over prolonged therapy can progress to chronic kidney disease.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Its anti-angiogenic TKIs impair healing: sunitinib and regorafenib block VEGF signaling needed for tissue repair, so wounds and surgical sites heal poorly, and GI bleeding from the tumor adds to the burden.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Advanced disease and its drugs hurt nerves: bone and nerve involvement by metastatic GIST, plus the muscle cramps and sensory effects of long-term tyrosine-kinase inhibitors, produce chronic and neuropathic pain.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong targeted therapy weighs on mood: the open-ended daily TKI treatment, its chronic side effects and the threat of resistance and recurrence in GIST contribute to depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its targeted drugs mark the skin: imatinib for GIST commonly causes rashes and periorbital oedema and can lighten skin pigmentation through KIT inhibition, while later TKIs cause hand-foot skin reaction.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It ties to endocrine tumours and thyroid: SDH-deficient GIST clusters with paraganglioma in Carney-Stratakis syndrome, and the TKIs used to treat GIST commonly induce hypothyroidism.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Open-ended targeted therapy breeds worry: the indefinite daily TKI treatment, the threat of resistance and recurrence surveillance in GIST foster chronic health anxiety alongside depression.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its targeted drugs strain the heart: the tyrosine-kinase inhibitors imatinib and especially sunitinib cause cardiotoxicity, heart failure and hypertension during long-term treatment.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It skips the lymph nodes: unlike GI carcinomas, GIST spreads haematogenously to the liver and peritoneum and rarely to lymph nodes, so routine lymphadenectomy is unnecessary.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Sunitinib taxes the kidney: the multi-target inhibitor sunitinib causes hypertension, proteinuria and occasional thrombotic microangiopathy affecting renal function.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its targeted drugs ache the body: imatinib and other KIT inhibitors commonly cause muscle cramps, myalgia and fluid retention with periorbital oedema.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It travels in rare syndromes and to the chest: the Carney triad pairs GIST with pulmonary chondroma and paraganglioma, and advanced GIST can metastasise to the lungs.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It springs from the gut's pacemaker cells: GIST arises from the interstitial cells of Cajal that drive peristalsis, and it is over-represented in neurofibromatosis type 1.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — The model of targeted therapy in solid tumours: imatinib against KIT, with sunitinib, regorafenib, avapritinib and ripretinib, transformed GIST from chemoresistant to a manageable cancer.
- `connects-to` → **[CML](../cml/README.md)** — A shared imatinib triumph: GIST (KIT-driven) and chronic myeloid leukaemia (BCR-ABL-driven) were the twin proofs that a single kinase inhibitor could control cancer.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Conventional chemo fails it: GIST is resistant to cytotoxic chemotherapy, which is why kinase inhibitors rather than chemo became its treatment.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Liver is the dominant metastatic site: GIST spreads within the abdomen, seeding the hepatic lobule and peritoneum, the pattern that defines advanced disease and drives lifelong imatinib.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Shared SDH loss: SDH-deficient GIST (Carney-Stratakis) and SDH-deficient renal cell carcinoma both arise from succinate-dehydrogenase failure, a metabolic route to two very different tumours.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — KIT's downstream switch: the mutant KIT and PDGFRA receptors of GIST signal through the MAPK/ERK pathway, the proliferative effector that imatinib and successor inhibitors shut off.
- `connects-to` → **[Neuroendocrine Tumors](../neuroendocrine-tumors/README.md)** — Two submucosal gut tumours: GISTs (KIT-driven, from interstitial cells of Cajal) and gastrointestinal neuroendocrine tumours both present as submucosal masses but arise from different cells and need different therapy.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Pacemaker cells of two organs: GIST arises from the interstitial cells of Cajal—the gut's electrical pacemaker—conceptually paralleling the cardiac conduction system that paces the heart.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Uncommon distant spread: although GIST metastasises mainly to the liver and peritoneum, advanced disease can reach the lungs and bone, unusual sites for this sarcoma.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Wild-type GIST driver: SDH-deficient (KIT/PDGFRA wild-type) GISTs overexpress IGF1R, making IGF-1 signalling a therapeutic target in this distinct, often paediatric subtype.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — Rare targetable fusion: a small subset of quadruple-wild-type GISTs harbour NTRK gene fusions, rendering them sensitive to TRK inhibitors beyond the usual KIT-directed drugs.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Another wild-type lever: FGFR fusions and activation arise in some KIT/PDGFRA wild-type GISTs, an alternative oncogenic driver targetable with FGFR inhibitors.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic silencing: EZH2-mediated PRC2 repression of tumour-suppressor genes contributes to GIST progression, an epigenetic vulnerability under study.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Downstream oncogene: KIT/PDGFRA signalling activates MYC in GIST, driving the biosynthetic and proliferative programme of the tumour.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Malignant progression: TERT promoter mutations and reactivation mark the progression of GIST toward higher-grade, metastatic behaviour.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Progression and resistance: CDKN2A deletion releases the cell-cycle brake in GIST, marking malignant progression and contributing to resistance to KIT-targeted imatinib therapy.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — High-risk transformation: TP53 alterations accumulate as GIST progresses from low-risk to high-grade, metastatic disease, beyond the initiating KIT or PDGFRA mutation.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage microenvironment: CCL2 recruits tumour-associated macrophages into the GIST stroma, shaping a microenvironment that supports tumour growth and modulates response to therapy.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Imatinib kills GIST cells by relieving the anti-apoptotic signal of the mutant KIT receptor, restoring caspase-3-mediated apoptosis—the basis for the dramatic responses that made GIST the paradigm of targeted therapy in solid tumors.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on GIST cells follows CXCL12 gradients to the liver and peritoneum, the dominant sites of the metastatic spread that, more than the primary tumor, determines prognosis in the disease.
- `connects-to` → **[EGLN1 (PHD2)](../../03-molecular/egln1/README.md)** — In wild-type GIST with SDH deficiency, accumulating succinate inhibits the EGLN1/PHD prolyl hydroxylases that mark HIF for degradation, locking in a pseudohypoxic program shared with SDH-mutant paraganglioma and pheochromocytoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — In SDH-deficient wild-type GIST, accumulated succinate also inhibits the TET DNA-demethylases, producing a globally hypermethylated genome that drives a distinct epigenetic subtype of the disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Imatinib's killing of KIT-driven GIST depends on tipping the BCL-2-family balance toward apoptosis, and persistent anti-apoptotic signaling leaves a residual drug-tolerant cell population that underlies relapse on therapy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — Oncogenic KIT signals through AKT to inactivate FOXO transcription factors, removing a pro-apoptotic brake—part of the survival program that imatinib reverses by restoring FOXO activity in GIST cells.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — KIT and PDGFRA activate PI3K (AKT and mTOR already mapped), and acquired PIK3CA mutations are a mechanism of secondary resistance to imatinib in GIST.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN normally restrains the same PI3K-AKT signaling, and its loss amplifies survival signaling, contributing to tyrosine-kinase-inhibitor resistance in GIST.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D1-CDK4/6 axis (cyclin-D1 mapped, with CDKN2A loss in malignant GIST) releases E2F1 to drive the proliferation that distinguishes high-risk from indolent tumors.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (NF1 and BRAF already mapped) lies downstream of the KIT and PDGFRA driver mutations, transmitting the proliferative signal of gastrointestinal stromal tumor.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Deregulation of the RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) marks the progression of GIST toward higher-risk, more aggressive disease.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) contributes to the survival signaling downstream of KIT in gastrointestinal stromal tumor.
- `connects-to` → **[EPAS1](../../03-molecular/epas1/README.md)** — In SDH-deficient GIST, succinate accumulation stabilizes HIF-2α (EPAS1), producing a pseudohypoxic transcriptional program (EGLN1 and HIF-1α mapped) that drives tumorigenesis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the survival and stromal interactions of gastrointestinal stromal tumors.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β within the tumor microenvironment modulates the invasive and immune behavior of GIST.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of GIST, relevant to combining immunotherapy with KIT-targeted therapy.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression downstream of KIT/PDGFRA in GIST.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the immune microenvironment of gastrointestinal stromal tumor.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β supports the survival signaling downstream of KIT/PDGFRA in gastrointestinal stromal tumor.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in gastrointestinal stromal tumor.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic killing contributes to the imatinib-enhanced antitumor immune response in gastrointestinal stromal tumor.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory microenvironment of gastrointestinal stromal tumor.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of gastrointestinal stromal tumor, particularly in SDH-deficient subtypes.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the proliferation and differentiation biology of gastrointestinal stromal tumor.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of gastrointestinal stromal tumor.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of gastrointestinal stromal tumor.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of gastrointestinal stromal tumor.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of gastrointestinal stromal tumor.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of gastrointestinal stromal tumor.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of gastrointestinal stromal tumor.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory tumor microenvironment of gastrointestinal stromal tumor.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of gastrointestinal stromal tumor.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the tumor microenvironment and metastatic interactions of gastrointestinal stromal tumor.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Imatinib immunomodulation: beyond blocking KIT, imatinib has immune effects, and MHC class II antigen presentation shapes the T-cell response that may contribute to the durable control of gastrointestinal stromal tumour.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — Resistance signalling: the AXL receptor tyrosine kinase provides a bypass survival signal that can drive resistance to KIT-directed therapy (KIT already mapped) in gastrointestinal stromal tumour, a mechanism of escape beyond secondary KIT mutations.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint context: PD-1-mediated T-cell exhaustion limits anti-tumour immunity in gastrointestinal stromal tumour, and checkpoint blockade is being explored alongside tyrosine-kinase inhibitors, especially in KIT/PDGFRA-wild-type disease.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Gastrointestinal bleeding: mucosal ulceration over a gastrointestinal stromal tumour causes acute or chronic bleeding, and the resulting anaemia with falling haemoglobin is the commonest presentation prompting endoscopy and diagnosis.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — TKI cardiotoxicity: the multitargeted kinase inhibitors sunitinib and regorafenib used after imatinib (KIT already mapped) cause hypertension and cardiac dysfunction, and troponin elevation marks the myocardial injury of this class toxicity in GIST.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immunity: IL-2-driven T-cell expansion (PD-1 and perforin already mapped) supports the anti-tumour immunity that checkpoint blockade aims to unleash in gastrointestinal stromal tumour, especially the KIT/PDGFRA-wild-type subtype.
- `connects-to` → **[Neurofibromatosis type 1](../neurofibromatosis-type-1/README.md)** — NF1-associated GIST: neurofibromatosis type 1 (NF1 already mapped) predisposes to multiple small-bowel GISTs that are typically KIT/PDGFRA-wild-type and imatinib-resistant, one of the wild-type subtypes of the tumour.
- `connects-to` → **[Carney complex](../carney-complex/README.md)** — Carney triad and dyad: SDH-deficient wild-type GIST (SDHB already mapped) occurs in the Carney triad with paraganglioma and pulmonary chondroma, and the Carney-Stratakis dyad, linking GIST to the paraganglioma syndromes.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the tumour microenvironment dampens the anti-tumour T-cell response (PD-1 already mapped), part of the immune evasion relevant to the checkpoint immunotherapy explored in wild-type GIST.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune microenvironment of the gastrointestinal stromal tumour.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumour-associated macrophages: the macrophages (CCL2 already mapped) infiltrate the GIST stroma, and their M2 polarisation (IL-4 already mapped) supports the immunosuppression relevant to the immunotherapy explored in wild-type disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron-deficiency anaemia: the mucosal-ulcerating GIST commonly bleeds into the gut, causing the iron-deficiency anaemia (haemoglobin already mapped) that is a frequent presenting sign of the tumour.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 stromal arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the immunosuppressive stroma relevant to the immunotherapy explored in wild-type GIST.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Mesenteric adipokine: leptin from the GI and mesenteric adipose microenvironment signals to the GIST, part of the metabolic crosstalk of the gastrointestinal stromal tumour.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and, with the chronic gut bleeding, contributes to the anaemia (haemoglobin already mapped) of GIST.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Mesenteric adipokine: adiponectin, with leptin (already mapped), is part of the GI/mesenteric-adipose adipokine crosstalk of the GIST microenvironment.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the GIST microenvironment.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Prognostic neutrophils: the tumour-associated neutrophils and the neutrophil-lymphocyte ratio (S100A8/9 already mapped) are studied prognostic markers in GIST.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the imatinib-induced immune activation and checkpoint (PD-1 already mapped) trials in GIST.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of the gastrointestinal stromal tumour.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of GIST.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the gastrointestinal stromal tumour.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the GIST microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of the gastrointestinal stromal tumour.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of the gastrointestinal stromal tumour.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of the gastrointestinal stromal tumour.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the macrophage-rich (already mapped) stroma of the gastrointestinal stromal tumour.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^demetri-2002-imatinib-gist]: Demetri GD, von Mehren M, Blanke CD, et al. Efficacy and safety of imatinib mesylate in advanced gastrointestinal stromal tumors. *N Engl J Med.* 2002;347(7):472-480. [doi:10.1056/NEJMoa020461](https://doi.org/10.1056/NEJMoa020461) · [PubMed 12181401](https://pubmed.ncbi.nlm.nih.gov/12181401/)
[^joensuu-2012-ssg18]: Joensuu H, Eriksson M, Sundby Hall K, et al. One vs three years of adjuvant imatinib for operable gastrointestinal stromal tumor: a randomized trial. *JAMA.* 2012;307(12):1265-1272. [doi:10.1001/jama.2012.347](https://doi.org/10.1001/jama.2012.347) · [PubMed 22453568](https://pubmed.ncbi.nlm.nih.gov/22453568/)
