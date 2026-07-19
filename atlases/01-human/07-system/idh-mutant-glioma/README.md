---
schema: human-scale-entry/v1
id: idh-mutant-glioma
name: IDH-Mutant Glioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "IDH-mutant glioma (Grade 2-3) defined by IDH1/2 mutations; 2-HG → TET2 inhibition → G-CIMP hypermethylation; WHO 2021 separates astrocytoma (ATRX LOF) from oligodendroglioma (1p/19q codeletion); vorasidenib FDA-approved August 2024 (INDIGO trial); median OS ~10-15 years."
aliases: ["IDH-mutant glioma", "IDH glioma", "IDH mutant astrocytoma", "IDH mutant oligodendroglioma", "lower grade glioma", "LGG", "diffuse glioma IDH", "IDH1 glioma", "IDH1 R132H glioma", "Grade 2 glioma vorasidenib"]
sources:
  - id: mellinghoff-2023-vorasidenib-lgg
    type: peer-reviewed
    cite: "Mellinghoff IK, van den Bent MJ, Blumenthal DT, et al. Vorasidenib in IDH1- or IDH2-mutant low-grade glioma. N Engl J Med. 2023;389(7):589-601."
    doi: "10.1056/NEJMoa2304194"
    pmid: "37272530"
    url: "https://doi.org/10.1056/NEJMoa2304194"
  - id: jiao-2012-atrx-glioma
    type: peer-reviewed
    cite: "Jiao Y, Killela PJ, Reitman ZJ, et al. Frequent ATRX, CIC, FUBP1 and IDH mutations refine the classification of malignant gliomas. Oncotarget. 2012;3(7):709-722."
    doi: "10.18632/oncotarget.588"
    pmid: "22869205"
    url: "https://doi.org/10.18632/oncotarget.588"
cross_links:
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "ATRX LOF defines the astrocytoma lineage in IDH-mutant glioma (vs 1p/19q codeletion in oligodendroglioma); ~80% of IDH-mutant astrocytoma Grade 3/4 harbor ATRX LOF; ATRX LOF IHC (nuclear staining lost) used diagnostically; ATRX LOF + TP53 = canonical astrocytoma signature."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH1 R132H mutation (>90% of IDH-mutant gliomas) → 2-hydroxyglutarate → TET2/KDM inhibition → G-CIMP; vorasidenib (IDH1/2 inhibitor) FDA-approved August 2024 for IDH-mutant Grade 2 glioma (INDIGO trial: PFS HR 0.39); IDH1 IHC (anti-R132H) is the initial diagnostic test."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "ATRX LOF + IDH1 → 2-HG → TET2 inhibition → DNA hypermethylation (G-CIMP); ATRX-DAXX deposits H3.3 at telomeric chromatin; ATRX LOF impairs H3.3 telomeric deposition → ALT mechanism → telomere lengthening independent of TERT; ATRX and TET2 cooperate in chromatin maintenance."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A homozygous deletion occurs in ~50-70% of IDH-mutant astrocytoma Grade 4; CDK4/6 hyperactivation → RB1 → E2F proliferation; CDKN2A deletion defines WHO Grade 4 IDH-mutant astrocytoma (from Grade 3); ATRX LOF + CDKN2A deletion → worst IDH-mutant glioma prognosis."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "IDH-mutant gliomas are diffuse, infiltrative brain tumors (astrocytoma favors frontal lobe, oligodendroglioma frontotemporal) that cannot be fully excised; maximal safe resection — often via awake craniotomy with cortical mapping — improves PFS and delays transformation."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "IDH status is the great divide in adult diffuse glioma: IDH-mutant tumors run a far more indolent course (median OS ~10-15 years) than IDH-wildtype glioblastoma (~15 months); WHO 2021 reserves the name 'glioblastoma' for IDH-wildtype tumors only."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "IDH-mutant astrocytoma is the glial-lineage arm of the family (ATRX LOF + TP53, 1p/19q intact), as opposed to oligodendroglioma; IDH mutation creates a neural-progenitor-like epigenetic state (G-CIMP) that blocks normal astrocytic differentiation."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "IDH-mutant glioma and medulloblastoma are both molecularly classified brain tumors at opposite poles: IDH-mutant glioma is a slow, diffuse hemispheric tumor of adults driven by 2-HG epigenetics, while medulloblastoma is a fast embryonal cerebellar tumor of children (SHH/WNT/MYC)."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "IDH-mutant glioma and IDH-mutant AML share the same driver: IDH1/2 mutation produces 2-hydroxyglutarate that blocks TET/KDM demethylases, hypermethylating DNA and blocking differentiation; the same drugs cross over — ivosidenib (IDH1) and enasidenib treat both glioma and AML."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "IDH-mutant glioma and cholangiocarcinoma are distant cancers united by IDH1 mutation and 2-HG: ~15-20% of intrahepatic CCA carries IDH1 R132, and ivosidenib — first approved in IDH1-mutant AML — is now used in both IDH1-mutant cholangiocarcinoma and grade 2 IDH-mutant glioma."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Oligodendroglioma is the IDH-mutant glioma defined by oligodendrocyte-like cells: IDH mutation plus 1p/19q codeletion marks this tumor, whose round 'fried-egg' cells resemble oligodendrocytes and whose codeletion predicts good PCV-chemo response and long survival."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Seizures are the commonest presentation of IDH-mutant glioma: these slow-growing, cortically-based tumors irritate neurons—partly via the oncometabolite 2-hydroxyglutarate altering glutamate—so new focal epilepsy in a young adult often first reveals the glioma."
  - target: 01-human/07-system/diffuse-midline-glioma
    relation: connects-to
    note: "IDH-mutant glioma and diffuse midline glioma sit at opposite ends of glioma biology: both are diffuse gliomas defined by a single metabolic/epigenetic driver, but IDH-mutant gliomas (adults, better prognosis) contrast with H3 K27M DMG (children, dismal prognosis)."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is standard for IDH-mutant glioma: after maximal resection, radiation plus PCV or temozolomide markedly extends survival in these slower-growing gliomas, and the new IDH inhibitor vorasidenib can now delay when radiation is needed."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "IDH-mutant glioma and Li-Fraumeni intersect at p53: many IDH-mutant astrocytomas carry TP53 mutations, and germline TP53 loss in Li-Fraumeni predisposes to gliomas in young adults—so the metabolic IDH lesion and loss of the genome's guardian often co-occur in one tumor."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "IDH-mutant gliomas integrate into neural circuits: their tumor cells form functional synapses with neurons, and the seizures these gliomas commonly cause reflect this electrical coupling—so neuronal activity both signals and may feed the slow-growing tumor."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH2 mutation is the rarer twin of IDH1 in glioma: both produce the oncometabolite 2-hydroxyglutarate that reprograms the epigenome, so IDH2 defines the same favorable-prognosis glioma class and is targetable by the same IDH inhibitors as IDH1."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 and ATRX mutation define the astrocytoma arm of IDH-mutant glioma: when an IDH-mutant tumor also loses p53 and ATRX it is an astrocytoma, whereas 1p/19q-codeleted TERT-mutant tumors are oligodendrogliomas—so p53 status splits the two IDH-glioma lineages."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutation marks the oligodendroglioma arm of IDH-mutant glioma: combined with 1p/19q codeletion it defines oligodendroglioma, the most treatment-responsive glioma—so TERT status, opposite TP53/ATRX, separates the two IDH-mutant subtypes."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy suits IDH-mutant glioma's long survivors: because these lower-grade gliomas strike younger patients who live many years, protons' reduced dose to surrounding brain helps limit late cognitive and endocrine toxicity from radiation."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "IDH-mutant glioma is built on a carbon-metabolism quirk: the mutant enzyme converts a Krebs-cycle intermediate into the carbon oncometabolite 2-hydroxyglutarate, which reprograms DNA and histone methylation to drive these gliomas—and is now a drug target."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "IDH-mutant gliomas are the more indolent diffuse tumors of the nervous system: they infiltrate the brain like glioblastoma but, being IDH-mutant, grow slower and respond better to treatment—so molecular status, not just appearance, predicts the course."
  - target: 01-human/07-system/hlrcc
    relation: connects-to
    note: "IDH-mutant glioma and HLRCC are sibling oncometabolite cancers: IDH mutation makes 2-hydroxyglutarate while FH loss makes fumarate, and both metabolites block the same dioxygenases to rewire epigenetics—so distinct enzymes converge on one cancer mechanism."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "IDH-mutant glioma is a vaccine target for T cells: the shared IDH1-R132H mutation creates a public neoantigen, and a peptide vaccine has induced cytotoxic T-cell responses against it—an early step toward immunotherapy for these gliomas."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "IDH-mutant gliomas drive seizures through glutamate: the 2-HG oncometabolite resembles glutamate and the tumor disturbs glutamate balance, so epilepsy is an early, common presenting symptom—seizure control is part of routine care."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "IDH-mutant gliomas build a quiet immune microenvironment: the oncometabolite 2-HG dampens microglia and other immune cells, so these tumors are less inflamed than IDH-wildtype glioblastoma—part of why they grow slowly but resist immunotherapy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The 2-HG made by IDH-mutant gliomas suppresses T cells: the oncometabolite impairs effector T-cell function and favors a tolerant, regulatory-T-cell-leaning state, blunting the antitumor immune response within the tumor."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "IDH-mutant gliomas still lean on mTOR growth signaling: the PI3K-AKT-mTOR pathway drives their proliferation alongside the defining IDH mutation, making mTOR a potential target to pair with IDH inhibitors like vorasidenib."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "IDH-mutant gliomas wire into the brain at synapses: like other gliomas they form connections with neurons, and this synaptic integration with glutamate signaling both spurs tumor growth and helps generate the seizures these tumors cause."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium signaling links IDH-mutant glioma to its seizures: glutamate from the tumor and its circuits drives calcium influx that overexcites neighboring neurons, helping explain why epilepsy is so often the first sign of these slow gliomas."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells anchor vaccine strategies against IDH-mutant glioma: the shared IDH1-R132H mutation makes a clean target, and presenting this neoantigen via dendritic cells aims to rally a T-cell attack on the tumor."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "IDH-mutant glioma sabotages iron-dependent enzymes: its oncometabolite 2-hydroxyglutarate blocks iron-and-oxoglutarate dioxygenases—including the DNA demethylases—rewiring the epigenome into the methylator phenotype."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "IDH-mutant glioma sits in a macrophage-rich niche: tumor-associated macrophages and microglia populate the microenvironment, though the mutant metabolite makes it less inflamed than aggressive glioblastoma."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "IDH-mutant glioma turns to VEGF as it progresses: initially less vascular than glioblastoma, it ramps up VEGF-driven angiogenesis when it transforms to higher grade, marking the dangerous turn."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "IDH-mutant gliomas favor the frontal and temporal lobes: temporal tumors invade the hippocampus, causing memory loss and the seizures that are often the first symptom of these slow-growing cancers."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "IDH-mutant glioma can steal vision: tumors near the optic pathways cause visual-field defects, and their location often shapes the first symptoms as much as the seizures do."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "IDH-mutant glioma keeps a tighter blood-brain barrier: its endothelial cells stay relatively intact, so the low-grade tumor often shows little contrast enhancement on MRI and resists drug delivery."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows IDH glioma's quiet infiltration: well-differentiated tumor cells slip diffusely between intact neurons and vessels, lacking the necrosis and bizarre vasculature of glioblastoma — the ultrastructure of a lower-grade, slower cancer."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Even a low-grade glioma plugs into the brain's electricity: its cells carry the potassium and other ion channels that let them depolarize with neuronal activity, an excitability that promotes migration and sparks the seizures these tumors so often cause."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "IDH glioma almost never leaves the brain, but rarely it can: like other gliomas, extracranial spread to the lung and bone is an exceptional late event, usually after surgery has breached the natural barriers."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The mutant enzyme is itself a target: IDH1 R132H is so uniform that a specific antibody stains it on biopsy, instantly confirming the diagnosis, and the neoantigen it creates is being chased by IDH-vaccine trials to provoke an antibody and T-cell response."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Long-term seizure control leans on magnesium and other ions: anticonvulsants and the tumor's own ion fluxes disturb electrolyte balance, and magnesium is watched in these patients as both an anti-seizure adjunct and a casualty of supportive care."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Treatment turns on the marrow: temozolomide chemoradiation suppresses neutrophil counts, and a rising neutrophil-to-lymphocyte ratio in the blood tracks the inflammatory, immune-suppressive state that marks more aggressive glioma behavior."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "These gliomas hit young adults in their reproductive years: the alkylating PCV and temozolomide chemotherapy used against them is gonadotoxic, so fertility preservation is discussed before treating a disease whose long survival makes it matter."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "The mutation rewrites the cell's methylation: 2-hydroxyglutarate from mutant IDH blocks the TET demethylases, tipping the balance toward DNMT-driven DNA methylation and the glioma CpG-island methylator phenotype that defines these tumors."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The oncometabolite muffles the immune attack: 2-hydroxyglutarate leaks from the tumor and suppresses helper T-cell activation and infiltration, helping IDH-mutant gliomas stay immunologically cold and dampening responses to immunotherapy."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR sorts gliomas the other way: amplification of this receptor marks the aggressive IDH-wildtype glioblastomas, so its absence helps confirm the IDH-mutant diagnosis — the two molecular profiles define largely separate diseases with very different prognoses."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "The oncometabolite also blunts innate killing: 2-hydroxyglutarate downregulates NKG2D-ligand display and impairs natural killer cell cytotoxicity, another way IDH-mutant tumors evade immune clearance beyond their effect on T cells."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "The mutation rewires metabolism: instead of making NADPH from isocitrate, mutant IDH burns it to manufacture 2-hydroxyglutarate, perturbing the cell's redox and energy economy that normally feeds ATP production through the TCA cycle."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "The oncometabolite perturbs the oxygen sensor: 2-hydroxyglutarate competitively inhibits the α-ketoglutarate-dependent prolyl hydroxylases that regulate HIF-1α, disturbing the hypoxia-response pathway as part of IDH-mutant tumor metabolism."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Brain irradiation injures the vessels: the radiotherapy used for IDH-mutant glioma causes a late cerebral vasculopathy that raises stroke risk in these often long-surviving patients, a delayed cost of treatment."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Tumor and treatment can hurt the nerves: infiltrating glioma and the surgery and radiation used against it injure sensory pathways, contributing to headache and neuropathic pain in the disease course."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Tumor-associated microglia stoke the inflammasome: NLRP3 activation in the glioma microenvironment releases IL-1β that shapes the immunosuppressive, pro-tumor inflammation even in these slower-growing IDH-mutant gliomas."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Brain tumors clot the veins: like other gliomas, IDH-mutant tumors raise venous thromboembolism risk through tumor tissue factor and the immobility of neurological disease and surgery."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Temozolomide opens an infection gap: the alkylating chemotherapy used in IDH-mutant glioma causes lymphopenia, predisposing to opportunistic infection including Pneumocystis pneumonia and to sepsis."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its therapy specifically courts it: temozolomide-induced lymphopenia plus the prolonged dexamethasone used for tumor edema set up Pneumocystis pneumonia, so prophylaxis is recommended during chemoradiation."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chemo and chronic illness blunt the marrow: temozolomide myelosuppression plus the inflammatory burden of a long-standing glioma depress erythropoiesis, adding an anemia-of-chronic-disease component."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A young-onset brain tumor weighs on mood: depression is common in IDH-mutant glioma, arising from tumor disruption of brain networks, corticosteroids and the burden of a slowly progressive, ultimately incurable cancer in young adults."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Its steroids raise blood sugar: the dexamethasone used to control peritumoral edema in IDH-mutant glioma induces insulin resistance, frequently causing steroid-induced hyperglycemia and diabetes."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Temozolomide and steroids open the lung to mold: the lymphopenia from temozolomide plus prolonged dexamethasone suppress immunity, occasionally permitting invasive aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Chronic steroids impair repair: the long-term dexamethasone used to manage IDH-mutant glioma thins skin and slows the healing of craniotomy and biopsy wounds."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Steroids and radiation disturb the glands: the prolonged dexamethasone for IDH-mutant glioma causes steroid diabetes and adrenal suppression, and radiation near the sella can damage the pituitary."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its drugs trouble the gut: dexamethasone raises peptic-ulcer risk and temozolomide causes nausea and hepatotoxicity, complicating the long treatment course of IDH-mutant glioma."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A slow but incurable brain tumour breeds worry: the indolent-but-progressive course, repeated scans and eventual transformation risk of IDH-mutant glioma foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its oncometabolite hides it from immunity: the D-2-hydroxyglutarate made by IDH-mutant tumours is immunosuppressive, making these 'cold' tumours, and dexamethasone further blunts immune defence."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The same mutation deforms bone: mosaic IDH mutations cause the multiple enchondromas of Ollier disease and Maffucci syndrome, which themselves predispose to gliomas."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It can come with skin haemangiomas: Maffucci syndrome pairs IDH-driven enchondromas with spindle-cell haemangiomas of the skin, on top of the radiation and steroid skin effects of treatment."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Brain tumours are prothrombotic: IDH-mutant glioma carries a raised venous thromboembolism risk, and the corticosteroids used for oedema add hypertension."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Immobility and steroids endanger the lungs: pulmonary embolism, aspiration and steroid-related Pneumocystis pneumonia threaten patients during long glioma treatment."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A new oncometabolite-targeted drug: IDH inhibitors such as vorasidenib block the mutant enzyme's 2-hydroxyglutarate production, delaying progression of IDH-mutant glioma."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo follows surgery and radiation: PCV (procarbazine-CCNU-vincristine) or temozolomide is the chemotherapy backbone, with the 1p/19q-codeleted oligodendroglioma especially chemosensitive."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "An immunologically cold tumour: the 2-hydroxyglutarate oncometabolite suppresses T-cell infiltration, leaving IDH-mutant glioma largely unresponsive to PD-1 checkpoint inhibitors."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Brain drainage shapes its immunity: CNS antigens drain through meningeal lymphatics, and the limited immune surveillance of this route helps keep IDH-mutant glioma immunologically cold."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "The oncometabolite reaches beyond DNA: D-2-hydroxyglutarate inhibits α-ketoglutarate-dependent prolyl-hydroxylases that mature collagen, so IDH-mutant cells suffer impaired collagen and basement-membrane assembly alongside the DNA hypermethylation that defines them."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "A targeted-therapy milestone repeated: as imatinib turned chronic myeloid leukaemia controllable, vorasidenib (INDIGO, 2023) became the first targeted drug to delay treatment in IDH-mutant glioma—each proof that blocking one driver reshapes a cancer."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "One epigenetic lesion, blood and brain: CMML, a myelodysplastic/myeloproliferative overlap, is driven by TET2-pathway methylation disturbances akin to the DNA hypermethylation IDH mutation causes in glioma—convergent epigenetic dysregulation in unrelated tissues."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neuron-glioma synapses: IDH-mutant gliomas, like glioblastoma and diffuse midline glioma, wire into neural circuits through activity-dependent and BDNF-driven synapses with neurons that drive growth and invasion."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "IDH inhibitors across cancers: IDH1/2 mutations also drive a subset of myelodysplastic syndromes and AML, so the same IDH inhibitors (ivosidenib, enasidenib) target glioma, MDS and leukaemia."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Diffuse white-matter infiltration: IDH-mutant gliomas spread along white-matter tracts and the axonal scaffold far beyond the visible tumour, the reason they cannot be cured by surgery despite slow growth."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Oncometabolite paradigm: the 2-hydroxyglutarate of IDH-mutant glioma parallels the succinate of SDH-mutant paraganglioma and the fumarate of HLRCC—each oncometabolite inhibits alpha-ketoglutarate dioxygenases and drives DNA hypermethylation."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Methylator phenotypes converge: the IDH-driven hypermethylation (G-CIMP) of IDH-mutant glioma mirrors the CpG-island methylator phenotype (CIMP) of a colorectal cancer subset, both silencing tumour suppressors epigenetically."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Tumour vasculature on transformation: high-grade progression of IDH-mutant glioma brings microvascular proliferation, the abnormal leaky arterial walls of tumour angiogenesis driven by VEGF and hypoxia."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Locked-in hypermethylation: the 2-hydroxyglutarate-driven CpG-island methylator phenotype, reinforced by polycomb/EZH2 activity, blocks differentiation in IDH-mutant glioma."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT progression: activation of PI3K-AKT-mTOR signalling contributes to the malignant progression of IDH-mutant glioma to higher grades."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Oncogenic transcription: MYC programmes become activated during the transformation of IDH-mutant glioma, driving the proliferation that marks high-grade disease."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: CDKN2A/B homozygous deletion—a marker of grade-4 IDH-mutant glioma—unleashes CDK4/6, accelerating the cell cycle and worsening prognosis."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "G1 progression: cyclin D1-CDK4/6 activity drives IDH-mutant glioma cells through the G1 checkpoint, the proliferative output that intensifies with malignant progression."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Glioma growth factor: PDGF signalling supports the proliferation and stromal recruitment of IDH-mutant gliomas, an autocrine driver of these astrocytic and oligodendroglial tumours."
  - target: 01-human/03-molecular/rad51
    relation: connects-to
    note: "Oncometabolite BRCAness: 2-hydroxyglutarate from mutant IDH impairs homologous-recombination repair (a RAD51-dependent 'BRCAness'), creating sensitivity to PARP inhibitors and DNA-damaging therapy."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Myeloid recruitment: CCL2 recruits microglia and macrophages into IDH-mutant gliomas, though the 2-HG-rich microenvironment is less myeloid-inflamed than IDH-wildtype glioblastoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RTK-MAPK proliferation: RAS-RAF-ERK signalling downstream of growth-factor receptors contributes to IDH-mutant glioma proliferation and intensifies with malignant transformation."
  - target: 01-human/03-molecular/egln1
    relation: connects-to
    note: "Dioxygenase competition: the 2-hydroxyglutarate produced by mutant IDH competitively inhibits α-ketoglutarate-dependent dioxygenases including the EGLN/PHD prolyl hydroxylases and the TET and histone demethylases, the broad epigenetic dysregulation defining these tumours."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Diffuse infiltration: CXCR4 on IDH-mutant glioma cells follows CXCL12 gradients to drive the diffuse white-matter infiltration that makes even these lower-grade gliomas impossible to fully resect."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Treatment-responsive apoptosis: IDH-mutant gliomas are more sensitive to radiation and temozolomide than IDH-wildtype tumours, engaging caspase-3-mediated apoptosis more readily — part of why they carry a markedly better prognosis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Neoantigen vaccine: the uniform IDH1 R132H mutation creates a shared neoantigen, and IDH vaccines aim to direct cytotoxic T cells to kill the tumour through perforin and granzyme, an immunotherapy strategy unique to this molecularly defined glioma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Immune-cold metabolism: the oncometabolite 2-hydroxyglutarate suppresses innate immune signalling including the STING-interferon axis and impairs T-cell function, helping make IDH-mutant glioma an immunologically cold tumour that IDH inhibitors may help thaw."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial response: galectin-3 from activated microglia contributes to the neuroinflammatory microenvironment of IDH-mutant glioma, a microglial signal increasingly studied as a modifier of glioma progression."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K growth signal: PIK3CA activates the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) that is co-active in IDH-mutant glioma and contributes to its growth."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle progression: the cyclin-D-CDK4/6 axis (mapped, with CDKN2A loss marking grade progression) releases E2F1 to drive the proliferation accompanying transformation of IDH-mutant glioma to higher grade."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Glial lineage: NOTCH signalling shapes the oligodendroglial and astrocytic differentiation programmes of IDH-mutant glioma, influencing the lineage and behaviour of these lower-grade tumours."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Grade progression: deregulation of the RB1-E2F checkpoint (CDKN2A, CDK4/6 and cyclin-D1 already mapped) drives the malignant progression of IDH-mutant glioma toward higher grade."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS proliferation: RAS-MAPK signalling (ERK1/2 already mapped) downstream of receptor tyrosine kinases contributes a proliferative input to IDH-mutant glioma."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Redox vulnerability: the IDH-mutant oncometabolite 2-hydroxyglutarate alters cellular redox and glutathione metabolism, and NRF2 antioxidant signalling shapes the resulting oxidative vulnerability of these gliomas."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β signalling modulates the invasion and immunosuppressive microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 signalling contributes to the proliferative and reactive-astrocytic responses in IDH-mutant glioma."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN restraint on PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) accompanies progression of IDH-mutant glioma toward secondary glioblastoma."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "The 2-hydroxyglutarate of IDH-mutant glioma suppresses IFN-STAT1 signalling, contributing to the immunologically cold microenvironment of these tumours."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the microenvironment and invasive behaviour of IDH-mutant glioma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the metabolic and oxidative stress of the 2-hydroxyglutarate-accumulating cells of IDH-mutant glioma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt/β-catenin signaling of IDH-mutant glioma cells."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in IDH-mutant glioma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the relatively immune-cold microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of growth-factor receptors contributes to the invasive signaling of IDH-mutant glioma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the metabolic adaptation of the 2-hydroxyglutarate-producing cells of IDH-mutant glioma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic reprogramming of IDH-mutant glioma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the tumor microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape (interacting with the 2-hydroxyglutarate-driven hypermethylation) of IDH-mutant glioma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of IDH-mutant glioma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the microglial and tumor-immune microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammatory tumor microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the tumor microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of IDH-mutant glioma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microglial/macrophage tumor microenvironment of IDH-mutant glioma (which is comparatively immune-cold relative to IDH-wildtype glioblastoma)."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "IDH neoantigen vaccine: the IDH1-R132H mutation (IDH1 already mapped) creates a shared neoantigen, and MHC class II-restricted presentation of it underlies the IDH peptide vaccines being tested to mobilise T cells against IDH-mutant glioma."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell mobilisation: IL-2-driven T-cell expansion supports the vaccine and cellular immunotherapy approaches for IDH-mutant glioma, whose 2-hydroxyglutarate-rich microenvironment otherwise suppresses effective T-cell responses."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Immune-cold checkpoint: IDH-mutant glioma is relatively immune-cold, the oncometabolite 2-hydroxyglutarate dampening immune infiltration, which blunts PD-1 checkpoint-blockade responses and motivates combination strategies with IDH inhibitors."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive metabolite: the oncometabolite 2-hydroxyglutarate and IL-10 in the microenvironment blunt T-cell responses (PD-1 already mapped), part of the immune-cold state of IDH-mutant glioma that IDH inhibitors aim to reverse."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Neuronal signalling: alongside the glutamatergic input (glutamate already mapped), GABAergic signalling shapes the neuronal activity of the infiltrated cortex, contributing to the seizures that frequently present IDH-mutant glioma."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of IDH-mutant glioma, part of the stromal microenvironment of this more indolent but ultimately progressive diffuse glioma."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia (already mapped) and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6 and IL-1 already mapped) of the IDH-mutant glioma microenvironment."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 microglial polarisation: IL-4 polarises the tumour-associated microglia and macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive niche of IDH-mutant glioma."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and metabolic stress: the 2-hydroxyglutarate-driven metabolic rewiring of the IDH-mutant cell generates oxidative stress (NRF2 already mapped), to which xanthine oxidase contributes, part of the tumour microenvironment."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 microglial (already mapped) niche of the relatively cold immune microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Neuron-glioma signalling: alongside the glutamate and GABA (already mapped) synapses, cholinergic acetylcholine signalling is part of the neuronal activity that drives the growth of the electrically integrated IDH-mutant glioma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "NMDA modulation: magnesium blocks the NMDA receptor and modulates the glutamate (already mapped) excitotoxicity and the neuron-glioma synaptic drive that promote the growth of IDH-mutant glioma."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lipid metabolic reprogramming: the cholesterol and lipid metabolism of the IDH-mutant glioma, part of the metabolic reprogramming driven by the 2-hydroxyglutarate (IDH already mapped), is a therapeutic vulnerability."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonergic neuromodulation: serotonin modulates the neuron-glioma (glutamate, GABA and acetylcholine already mapped) circuits whose activity drives the growth of IDH-mutant glioma."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Noradrenergic input: noradrenaline is part of the neuronal-activity-dependent (glutamate already mapped) signalling that stimulates the proliferation of IDH-mutant glioma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Cold-tumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is suppressed by the 2-hydroxyglutarate (IDH already mapped), contributing to the immunologically cold microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells is dampened by the 2-hydroxyglutarate (IDH already mapped) immunosuppression of IDH-mutant glioma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response opposing the immunosuppressive, oncometabolite-driven (IDH already mapped) microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin links the metabolic state to the immune response and, with the dexamethasone-induced metabolic syndrome, is part of the systemic milieu of IDH-mutant glioma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu, altered by the steroid therapy of IDH-mutant glioma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the neuroinflammatory microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immunologically cold microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of the IDH-mutant-glioma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of IDH-mutant glioma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) and myeloid activation of the immunosuppressive IDH-mutant-glioma microenvironment (blunted by the 2-hydroxyglutarate)."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the vascular permeability of the IDH-mutant-glioma microenvironment."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of IDH-mutant glioma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: complement C5 and its C5a anaphylatoxin (with C3 and C5aR1 already mapped) drive myeloid infiltration and the pro-tumour neuroinflammation of the IDH-mutant glioma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: IDH-mutant glioma cells recruit factor H to bind C3b and downregulate the alternative pathway (C3, C5 and C5aR1 already mapped), evading complement-mediated tumour surveillance."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Anti-glioma VDR signalling: vitamin D (VDR expressed in IDH-mutant glioma) suppresses proliferation and correlates with better prognosis; low serum levels associate with shorter time to progression in lower-grade glioma."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin in the glioma microenvironment: TSLP released by IDH-mutant glioma cells primes dendritic cells (already mapped) and mast cells (already mapped) to sustain the Th2-skewed (IL-4, IL-13 already mapped) immunosuppressive microenvironment of lower-grade glioma."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Vascular permeability mediator: bradykinin, acting on B2 receptors of the endothelial cells (already mapped) of the blood-brain barrier, amplifies its disruption in IDH-mutant glioma, contributing to peritumoral oedema and the nitric oxide (already mapped) signalling."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement regulation: C1-INH controls the classical-pathway arm (C3, C5, C5aR1 and factor H already mapped) of the complement-mediated immune surveillance of IDH-mutant glioma cells, whose 2-hydroxyglutarate blunts the innate immune response."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine-IDH-glioma axis: histamine, released by microglia (already mapped) and mast cells in the IDH-mutant glioma microenvironment, signals via H3 receptors on neurons (already mapped) and H1/H2 on tumour cells, modulating 2-HG-mediated immunosuppression."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-IDH-glioma axis: melatonin, crossing the blood-brain barrier, suppresses IDH-mutant glioma cell proliferation, modulates the 2-HG (IDH1/2 already mapped) metabolic milieu and its epigenetic silencing, and enhances apoptotic sensitivity to temozolomide."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-IDH-glioma axis: erythropoietin, via the EPOR on IDH-mutant glioma cells (already mapped), activates the JAK-STAT (already mapped) neuroprotective pathway and modulates microglia/macrophage (already mapped) polarisation in the IDH-mutant glioma microenvironment."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "IDH-glioma prolactin: prolactin, via PRLR on microglia (already mapped) and macrophages (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the IL-6 (already mapped) and mast-cell (already mapped) T-cytotoxic (already mapped) cascade of IDH-mutant glioma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "IDH-glioma oxytocin: oxytocin, via OXTR on microglia (already mapped) and macrophages (already mapped), attenuates neuroinflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) T-cytotoxic (already mapped) cascade of IDH-mutant glioma."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "IDH-glioma vasopressin: vasopressin, via V1aR on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; vasopressin dysregulation amplifies the IL-6 (already mapped) and mast-cell (already mapped) cascade of IDH-mutant glioma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "IDH-glioma testosterone: testosterone, via AR on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; testosterone deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of IDH-mutant glioma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "IDH-glioma selenium: selenium, as GPx in microglia (already mapped) and macrophages (already mapped), scavenges ROS; selenium deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) oxidative cascade of IDH-mutant glioma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "IDH-glioma iodine: iodine-dependent thyroid hormones modulate microglia (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) cascade of IDH-mutant glioma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "IDH-glioma sodium: high dietary sodium promotes microglia (already mapped) and mast-cell (already mapped) activation; sodium-induced IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of IDH-mutant glioma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "IDH-glioma copper: copper supports microglia (already mapped) and T-cytotoxic (already mapped) anti-tumour function; copper deficiency amplifies IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of IDH-mutant glioma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "IDH-glioma zinc: zinc cofactors antioxidant enzymes in microglia (already mapped) and T-cytotoxic cells (already mapped); zinc deficiency amplifies IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of IDH-mutant glioma."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "IDH-glioma chloride: chloride channels regulate microglia (already mapped) and T-cytotoxic (already mapped) volume during tumour microenvironment stress; chloride dysregulation amplifies IL-6 (already mapped) and mast-cell (already mapped) tumour cascade in IDH-mutant glioma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "IDH-glioma nitrogen: nitrogen as backbone of IDH-mutant oncoproteins and cytokines (already mapped) sustains oncometabolite signalling; nitrogen-derived RNS from microglia (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) in IDH-mutant glioma."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "IDH-glioma phosphorus: phosphorus as ATP in microglia (already mapped) and T-cytotoxic cells (already mapped) fuels anti-tumour kinase signalling; phosphorus dysregulation amplifies IL-6 (already mapped) and mast-cell (already mapped) cascade in IDH-mutant glioma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "IDH-glioma hydrogen: hydrogen via ROS from microglia (already mapped) and T-cytotoxic cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "IDH-glioma oxygen: ROS from NADPH-oxidase in microglia (already mapped) and T-cytotoxic cells (already mapped) drives tumour oxidative stress; oxygen dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "IDH-glioma sulfur: sulfur-containing amino acids in microglia (already mapped) and T-cytotoxic cells (already mapped) regulate redox signalling; sulfur dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "IDH-glioma glp-1: GLP-1 from neurons (already mapped) and microglia (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-mutant glioma."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "IDH-glioma angiotensin-ii: angiotensin-II from microglia (already mapped) and endothelial cells (already mapped) drives vascular remodelling; angiotensin-ii excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "IDH-glioma wnt-beta-catenin: WNT/β-catenin on microglia (already mapped) and tumour cells (already mapped) regulates invasion; wnt-beta-catenin dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "IDH-glioma rankl: RANKL from microglia (already mapped) and tumour cells (already mapped) modulates glioma immune crosstalk; rankl excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "IDH-glioma fibronectin: fibronectin in microglia (already mapped) and tumour cells (already mapped) promotes glioma ECM remodelling; fibronectin excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "IDH-glioma igf-1: IGF-1 from microglia (already mapped) and tumour cells (already mapped) promotes glioma proliferation; igf-1 excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "IDH-glioma activin-a: activin-A from microglia (already mapped) and tumour cells (already mapped) promotes glioma fibrosis; activin-a excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "IDH-glioma cgrp: CGRP from microglia (already mapped) and tumour cells (already mapped) modulates glioma neuroimmune tone; cgrp excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "IDH-glioma calcitonin: calcitonin from microglia (already mapped) and tumour cells (already mapped) modulates glioma calcium tone; calcitonin dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "IDH-glioma substance-p: substance-P from microglia (already mapped) and tumour cells (already mapped) modulates glioma pain tone; substance-P excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "IDH-glioma insulin-receptor: insulin receptor on microglia (already mapped) and tumour cells (already mapped) modulates glioma metabolic axis; insulin-receptor loss amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "IDH-glioma aldosterone: aldosterone from microglia (already mapped) and tumour cells (already mapped) modulates glioma fluid balance; aldosterone excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma."
---

# IDH-Mutant Glioma

## Overview

**IDH-mutant glioma** encompasses a family of diffuse glial brain tumors defined by somatic mutations in **IDH1** (most commonly R132H, >90%) or **IDH2** (R172K/M, ~5-8%). These mutations convert α-ketoglutarate to **2-hydroxyglutarate (2-HG)**, an oncometabolite that competitively inhibits α-KG-dependent dioxygenases including **TET2** (DNA demethylase) and histone KDMs → DNA hypermethylation (G-CIMP) → epigenetic silencing of tumor suppressor loci. Under the **WHO 2021 CNS tumor classification**, IDH-mutant diffuse gliomas are divided into two lineages by molecular markers: **astrocytoma** (ATRX LOF + TP53 mutation, 1p/19q intact) and **oligodendroglioma** (1p/19q codeletion + TERT promoter mutation, ATRX intact). IDH-mutant gliomas have a markedly better prognosis than IDH-wildtype glioblastoma (median OS ~10-15 years for Grade 2 vs ~15 months for GBM). **Vorasidenib**, a brain-penetrant IDH1/2 inhibitor, was FDA-approved in August 2024 for Grade 2 IDH-mutant glioma following the INDIGO trial [^mellinghoff-2023-vorasidenib-lgg] [^jiao-2012-atrx-glioma].

**Epidemiology:**
- Incidence: ~5,000-6,000 IDH-mutant glioma cases/year USA (~Grade 2: 2,500-3,000; Grade 3: 2,000; Grade 4 IDH-mutant astrocytoma: ~500-700)
- Median age: Grade 2 ~35-40 years; Grade 3 ~40-50 years; Grade 4 IDH-mutant astrocytoma ~45-55 years (significantly younger than IDH-wildtype GBM, median age ~64 years)
- IDH1 R132H: ~90% of IDH-mutant gliomas; IDH1 non-R132H variants: ~3-5%; IDH2 mutations: ~5-8%; exclusively IDH2 in some Grade 3 oligodendrogliomas
- Geographic distribution: no significant ethnic variation; incidence ~5 per 100,000 for all diffuse gliomas combined

**IDH-mutant glioma molecular subtypes (WHO 2021):**

| Feature | IDH-mutant Astrocytoma | IDH-mutant Oligodendroglioma |
|---|---|---|
| ATRX | LOST (LOF) | INTACT |
| 1p/19q | Intact | Codeleted |
| TP53 | Mutated (~80%) | Usually wildtype |
| TERT promoter | Rare | Mutated (~90%) |
| Grade range | 2, 3, 4 | 2, 3 |
| CDKN2A deletion | Grade 4 defining | Rare |
| Median OS (Grade 2) | ~12-15 yrs | ~15-18 yrs |
| Chemotherapy | PCV or TMZ | PCV preferred |

## Structure

### 2-HG oncometabolite mechanism

**IDH1/2 neomorphic activity:**
Normal IDH1 (cytoplasm) and IDH2 (mitochondria): oxidative decarboxylation of isocitrate → α-ketoglutarate + CO2 + NADPH; oncogenic IDH1/2: gain-of-function neomorphic activity → uses NADPH to reduce α-ketoglutarate → 2-hydroxyglutarate (2-HG); 2-HG accumulates to millimolar concentrations in IDH-mutant gliomas; 2-HG can be measured by MR spectroscopy (non-invasive) or HPLC/mass spec (tissue)

**2-HG targets:**
- **TET2** (5-methylcytosine dioxygenase): converts 5mC → 5hmC → active DNA demethylation; 2-HG competitively inhibits TET2 at the α-KG cofactor site → DNA hypermethylation → G-CIMP (glioma CpG island methylator phenotype) → silencing of MGMT (promoter methylated in ~85% IDH-mutant gliomas), CDKN2A, and other TSGs
- **KDMs** (histone lysine demethylases, KDM4A, KDM5C, KDM6A): α-KG-dependent demethylases; 2-HG inhibition → histone hypermethylation (H3K9me3, H3K27me3, H3K36me3); epigenetic silencing beyond DNA methylation
- **ALKBH** enzymes: DNA/RNA demethylases; 2-HG inhibition → elevated N6-methyladenosine (m6A) in RNA → altered mRNA stability

**G-CIMP:**
G-CIMP (glioma CpG island methylator phenotype): concerted hypermethylation of >1000 CpG island promoters in IDH-mutant gliomas; G-CIMP is pathognomonic for IDH-mutant diffuse gliomas; includes MGMT (predictive of alkylating agent sensitivity), CDKN2A, RASSF1A, and other TSGs; G-CIMP can be measured by methylation arrays (450K/EPIC); DNA methylation profiling is now part of integrated WHO 2021 diagnosis

### MGMT promoter methylation

**MGMT in IDH-mutant glioma:**
MGMT (O6-methylguanine-DNA methyltransferase) repairs O6-methylguanine adducts created by alkylating agents (temozolomide); MGMT promoter methylated in ~85% of IDH-mutant Grade 2-3 gliomas (downstream of G-CIMP) → MGMT protein absent → alkylating agent DNA damage not repaired → tumor cell death; MGMT methylation predicts temozolomide benefit; unmethylated MGMT (rare in IDH-mutant glioma) associated with alkylating agent resistance

## Function

### Molecular consequences of IDH mutation

**Epigenetic reprogramming:**
IDH mutation is an early (possibly initiating) event in gliomagenesis: IDH1 R132H creates the G-CIMP state → neural progenitor-like epigenetic landscape → blocked differentiation; IDH mutation precedes ATRX LOF and TP53 in the evolutionary sequence of astrocytoma; IDH mutation is the defining event from which astrocytoma and oligodendroglioma diverge (ATRX vs 1p/19q)

**Metabolic consequences:**
2-HG accumulation → NADPH consumption (reversal of normal IDH reaction) → oxidative stress; IDH-mutant glioma cells are more vulnerable to oxidative stress than IDH-wildtype; IDH mutant cells show impaired glutamine metabolism; 2-HG acts as an HIF prolyl hydroxylase activator → pseudonormoxic signaling; IDH-mutant tumor microenvironment is relatively immunosuppressed

**Immune evasion:**
IDH-mutant gliomas are immunologically "cold": low TMB (IDH-mutant gliomas have low mutation burden, ~1-2 mut/Mb), low PD-L1 expression; G-CIMP suppresses inflammatory gene expression including cytokine signaling; 2-HG is directly immunosuppressive: inhibits T cell proliferation and NK cell activity at physiological 2-HG concentrations; immunotherapy (pembrolizumab, bevacizumab + pembrolizumab) has not shown significant benefit in IDH-mutant glioma trials

## Pathology

### Diagnosis and grading

**WHO 2021 CNS Grade system:**
IDH-mutant astrocytoma:
- **Grade 2**: IDH-mutant + ATRX LOF + TP53 mutation + no CDKN2A deletion + no necrosis/microvascular proliferation; most favorable; 10-year OS ~70-80%
- **Grade 3**: above + anaplasia (increased mitoses, cellularity); some CDKN2A deletion; 10-year OS ~50-60%
- **Grade 4**: IDH-mutant astrocytoma with CDKN2A homozygous deletion AND/OR necrosis+microvascular proliferation; no EGFR amp, no TERT mutation; 10-year OS ~30-40%

IDH-mutant oligodendroglioma:
- **Grade 2**: IDH-mutant + 1p/19q codeleted + TERT promoter mutation; ATRX intact; 10-year OS ~80-90%
- **Grade 3**: above + anaplastic features; 10-year OS ~65-75%
- Note: no Grade 4 in oligodendroglioma (1p/19q codeletion blocks GBM-like progression)

**Diagnostic workup:**
1. MRI brain: IDH-mutant glioma: T2/FLAIR hyperintense cortical/subcortical infiltrative mass, minimal enhancement (Grade 2-3); frontal lobe predilection (astrocytoma), frontotemporal (oligodendroglioma)
2. IDH1 R132H IHC (anti-IDH1 R132H clone H09): positive in ~90% IDH-mutant; negative → IDH1/2 sequencing
3. ATRX IHC: lost = astrocytoma lineage; intact = oligodendroglioma lineage
4. FISH: 1p/19q codeletion (oligodendroglioma) vs intact (astrocytoma)
5. TERT promoter sequencing (C228T, C250T): mutated in ~90% oligodendroglioma
6. CDKN2A FISH or CNV array: homozygous deletion = WHO Grade 4 astrocytoma
7. DNA methylation profiling (EPIC array): G-CIMP confirmation; classifier at molecularneuropathology.org for CNS tumor subtype

### Standard treatment

**Surgery:**
Maximum safe resection is first-line for newly diagnosed IDH-mutant glioma; gross total resection associated with PFS benefit; eloquent cortex involvement limits resection; awake craniotomy for language/motor mapping; extent of resection correlates with OS and time to malignant transformation in Grade 2

**Radiation:**
- Grade 2: RT 50.4-54 Gy in 1.8 Gy fractions; delayed RT vs immediate RT (RTOG 9802, EORTC 22845): no OS difference; immediate RT improves PFS by ~3 years
- Grade 3: RT 60 Gy + PCV or TMZ; CATNON trial: RT + TMZ (concurrent + adjuvant) improved OS in IDH-mutant Grade 3 (5-yr OS 55% vs 44%)
- Grade 4: 60 Gy + TMZ (Stupp protocol, adapted); CDKN2A-deleted Grade 4 IDH-mutant has similar treatment as GBM

**Chemotherapy:**
- **PCV** (procarbazine + CCNU/lomustine + vincristine): Phase 3 RTOG 9802 (Grade 2 with RF): RT + PCV improved 10-yr OS (60% vs 40%) and PFS (10.4 yr vs 4.0 yr); PCV preferred for oligodendroglioma (1p/19q codeleted)
- **Temozolomide (TMZ)**: alkylating agent; MGMT methylated (~85% IDH-mutant) → high sensitivity; oral daily 75 mg/m² concurrent + adjuvant 150-200 mg/m² ×5d/28d ×12 cycles; CATNON Phase 3 (IDH-mutant Grade 3): RT + adjuvant TMZ improved OS

**Vorasidenib (FDA-approved August 2024):** [^mellinghoff-2023-vorasidenib-lgg]
- Mechanism: brain-penetrant, dual IDH1/2 inhibitor; 40 mg oral once daily; suppresses 2-HG production → reverses epigenetic reprogramming (partial); crosses blood-brain barrier (Kp,uu ~0.6 for mouse brain)
- INDIGO Phase 3 trial (N=331 Grade 2 IDH-mutant glioma after surgery): vorasidenib vs placebo; primary endpoint PFS; vorasidenib median PFS 27.7 months vs 11.1 months (HR 0.39, p<0.001); time to next intervention HR 0.26; OS data immature at primary analysis
- Eligibility: residual/recurrent Grade 2 IDH-mutant (IDH1/2) glioma; after at least one prior surgery; no prior RT or chemo required (RT/chemo-naive population)
- FDA indication (August 2024): adults with residual or recurrent Grade 2 IDH1- or IDH2-mutant glioma
- Toxicity: transaminase elevation (Gr3: ~10%), grade 1-2 nausea/fatigue; liver function monitoring required
- Note: not yet studied in Grade 3-4 IDH-mutant glioma; trials ongoing

**Olutasidenib (IDH1 inhibitor):**
Olutasidenib 150 mg BID: FDA-approved October 2022 for IDH1-mutant AML (relapsed/refractory); not approved for glioma; Phase 2 glioma study ongoing; less brain-penetrant than vorasidenib; ORR ~35% in IDH1-mutant AML

**MGMT-based temozolomide sensitivity:**
IDH-mutant glioma with MGMT methylation shows strong alkylating agent sensitivity; TMZ + RT remains standard for Grade 3-4; MGMT unmethylated IDH-mutant glioma: PCV may be preferred (not dependent on MGMT for efficacy — different mechanism via inter-strand cross-links)

### Recurrent disease

**Patterns of progression:**
- Grade 2 → Grade 3 transformation: ~30-40% over 5-10 years; acquisition of CDKN2A deletion, EGFR, or other alterations
- Grade 3 → Grade 4 transformation: additional molecular events
- Malignant transformation (MT): when IDH-mutant glioma acquires GBM-like features (necrosis, MGMT loss, EGFR amplification); MT associated with dismal prognosis; re-biopsy important to confirm

**Salvage options at recurrence:**
- Rechallenge with TMZ or lomustine (if MGMT methylated)
- Bevacizumab: ORR ~25-30% radiographic response in recurrent glioma; FDA-approved for GBM; used off-label in IDH-mutant glioma recurrence
- Clinical trials: CDK4/6 inhibitors (palbociclib for CDKN2A-deleted Grade 4), ONC201 (H3K27M-negative IDH-mutant; exploratory), mTOR inhibitors, immunotherapy (pembrolizumab)
- Vorasidenib continuation after RT/chemo: INDIGO 2 trial design ongoing

**Prognosis by molecular subtype:**
- IDH-mutant oligodendroglioma Grade 2: median OS ~18-20 years; best among gliomas
- IDH-mutant astrocytoma Grade 2: median OS ~12-15 years
- IDH-mutant astrocytoma Grade 3: median OS ~7-9 years
- IDH-mutant astrocytoma Grade 4 (CDKN2A-deleted): median OS ~3-5 years (significantly worse than Grade 3 but better than IDH-wildtype GBM)

## Connections

- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — ATRX LOF defines the astrocytoma lineage in IDH-mutant glioma (vs 1p/19q codeletion in oligodendroglioma); ~80% of IDH-mutant astrocytoma Grade 3/4 harbor ATRX LOF; ATRX LOF IHC (nuclear staining lost) used diagnostically; ATRX LOF + TP53 = canonical astrocytoma signature.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH1 R132H mutation (>90% of IDH-mutant gliomas) → 2-hydroxyglutarate → TET2/KDM inhibition → G-CIMP; vorasidenib (IDH1/2 inhibitor) FDA-approved August 2024 for IDH-mutant Grade 2 glioma (INDIGO trial: PFS HR 0.39); IDH1 IHC (anti-R132H) is the initial diagnostic test.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — ATRX LOF + IDH1 → 2-HG → TET2 inhibition → DNA hypermethylation (G-CIMP); ATRX-DAXX deposits H3.3 at telomeric chromatin; ATRX LOF impairs H3.3 telomeric deposition → ALT mechanism → telomere lengthening independent of TERT; ATRX and TET2 cooperate in chromatin maintenance.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A homozygous deletion occurs in ~50-70% of IDH-mutant astrocytoma Grade 4; CDK4/6 hyperactivation → RB1 → E2F proliferation; CDKN2A deletion defines WHO Grade 4 IDH-mutant astrocytoma (from Grade 3); ATRX LOF + CDKN2A deletion → worst IDH-mutant glioma prognosis.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — IDH-mutant gliomas are diffuse, infiltrative brain tumors (astrocytoma favors frontal lobe, oligodendroglioma frontotemporal) that cannot be fully excised; maximal safe resection — often via awake craniotomy with cortical mapping — improves PFS and delays transformation.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — IDH status is the great divide in adult diffuse glioma: IDH-mutant tumors run a far more indolent course (median OS ~10-15 years) than IDH-wildtype glioblastoma (~15 months); WHO 2021 reserves the name 'glioblastoma' for IDH-wildtype tumors only.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — IDH-mutant astrocytoma is the glial-lineage arm of the family (ATRX LOF + TP53, 1p/19q intact), as opposed to oligodendroglioma; IDH mutation creates a neural-progenitor-like epigenetic state (G-CIMP) that blocks normal astrocytic differentiation.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — IDH-mutant glioma and medulloblastoma are both molecularly classified brain tumors at opposite poles: IDH-mutant glioma is a slow, diffuse hemispheric tumor of adults driven by 2-HG epigenetics, while medulloblastoma is a fast embryonal cerebellar tumor of children (SHH/WNT/MYC).
- `connects-to` → **[AML](../aml/README.md)** — IDH-mutant glioma and IDH-mutant AML share the same driver: IDH1/2 mutation produces 2-hydroxyglutarate that blocks TET/KDM demethylases, hypermethylating DNA and blocking differentiation; the same drugs cross over — ivosidenib (IDH1) and enasidenib treat both glioma and AML.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — IDH-mutant glioma and cholangiocarcinoma are distant cancers united by IDH1 mutation and 2-HG: ~15-20% of intrahepatic CCA carries IDH1 R132, and ivosidenib — first approved in IDH1-mutant AML — is now used in both IDH1-mutant cholangiocarcinoma and grade 2 IDH-mutant glioma.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Oligodendroglioma is the IDH-mutant glioma defined by oligodendrocyte-like cells: IDH mutation plus 1p/19q codeletion marks this tumor, whose round 'fried-egg' cells resemble oligodendrocytes and whose codeletion predicts good PCV-chemo response and long survival.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Seizures are the commonest presentation of IDH-mutant glioma: these slow-growing, cortically-based tumors irritate neurons—partly via the oncometabolite 2-hydroxyglutarate altering glutamate—so new focal epilepsy in a young adult often first reveals the glioma.
- `connects-to` → **[Diffuse Midline Glioma](../diffuse-midline-glioma/README.md)** — IDH-mutant glioma and diffuse midline glioma sit at opposite ends of glioma biology: both are diffuse gliomas defined by a single metabolic/epigenetic driver, but IDH-mutant gliomas (adults, better prognosis) contrast with H3 K27M DMG (children, dismal prognosis).
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is standard for IDH-mutant glioma: after maximal resection, radiation plus PCV or temozolomide markedly extends survival in these slower-growing gliomas, and the new IDH inhibitor vorasidenib can now delay when radiation is needed.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — IDH-mutant glioma and Li-Fraumeni intersect at p53: many IDH-mutant astrocytomas carry TP53 mutations, and germline TP53 loss in Li-Fraumeni predisposes to gliomas in young adults—so the metabolic IDH lesion and loss of the genome's guardian often co-occur in one tumor.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — IDH-mutant gliomas integrate into neural circuits: their tumor cells form functional synapses with neurons, and the seizures these gliomas commonly cause reflect this electrical coupling—so neuronal activity both signals and may feed the slow-growing tumor.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH2 mutation is the rarer twin of IDH1 in glioma: both produce the oncometabolite 2-hydroxyglutarate that reprograms the epigenome, so IDH2 defines the same favorable-prognosis glioma class and is targetable by the same IDH inhibitors as IDH1.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 and ATRX mutation define the astrocytoma arm of IDH-mutant glioma: when an IDH-mutant tumor also loses p53 and ATRX it is an astrocytoma, whereas 1p/19q-codeleted TERT-mutant tumors are oligodendrogliomas—so p53 status splits the two IDH-glioma lineages.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutation marks the oligodendroglioma arm of IDH-mutant glioma: combined with 1p/19q codeletion it defines oligodendroglioma, the most treatment-responsive glioma—so TERT status, opposite TP53/ATRX, separates the two IDH-mutant subtypes.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy suits IDH-mutant glioma's long survivors: because these lower-grade gliomas strike younger patients who live many years, protons' reduced dose to surrounding brain helps limit late cognitive and endocrine toxicity from radiation.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — IDH-mutant glioma is built on a carbon-metabolism quirk: the mutant enzyme converts a Krebs-cycle intermediate into the carbon oncometabolite 2-hydroxyglutarate, which reprograms DNA and histone methylation to drive these gliomas—and is now a drug target.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — IDH-mutant gliomas are the more indolent diffuse tumors of the nervous system: they infiltrate the brain like glioblastoma but, being IDH-mutant, grow slower and respond better to treatment—so molecular status, not just appearance, predicts the course.
- `connects-to` → **[Hereditary Leiomyomatosis and Renal Cell Carcinoma](../hlrcc/README.md)** — IDH-mutant glioma and HLRCC are sibling oncometabolite cancers: IDH mutation makes 2-hydroxyglutarate while FH loss makes fumarate, and both metabolites block the same dioxygenases to rewire epigenetics—so distinct enzymes converge on one cancer mechanism.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — IDH-mutant glioma is a vaccine target for T cells: the shared IDH1-R132H mutation creates a public neoantigen, and a peptide vaccine has induced cytotoxic T-cell responses against it—an early step toward immunotherapy for these gliomas.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — IDH-mutant gliomas drive seizures through glutamate: the 2-HG oncometabolite resembles glutamate and the tumor disturbs glutamate balance, so epilepsy is an early, common presenting symptom—seizure control is part of routine care.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — IDH-mutant gliomas build a quiet immune microenvironment: the oncometabolite 2-HG dampens microglia and other immune cells, so these tumors are less inflamed than IDH-wildtype glioblastoma—part of why they grow slowly but resist immunotherapy.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The 2-HG made by IDH-mutant gliomas suppresses T cells: the oncometabolite impairs effector T-cell function and favors a tolerant, regulatory-T-cell-leaning state, blunting the antitumor immune response within the tumor.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — IDH-mutant gliomas still lean on mTOR growth signaling: the PI3K-AKT-mTOR pathway drives their proliferation alongside the defining IDH mutation, making mTOR a potential target to pair with IDH inhibitors like vorasidenib.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — IDH-mutant gliomas wire into the brain at synapses: like other gliomas they form connections with neurons, and this synaptic integration with glutamate signaling both spurs tumor growth and helps generate the seizures these tumors cause.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium signaling links IDH-mutant glioma to its seizures: glutamate from the tumor and its circuits drives calcium influx that overexcites neighboring neurons, helping explain why epilepsy is so often the first sign of these slow gliomas.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells anchor vaccine strategies against IDH-mutant glioma: the shared IDH1-R132H mutation makes a clean target, and presenting this neoantigen via dendritic cells aims to rally a T-cell attack on the tumor.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — IDH-mutant glioma sabotages iron-dependent enzymes: its oncometabolite 2-hydroxyglutarate blocks iron-and-oxoglutarate dioxygenases—including the DNA demethylases—rewiring the epigenome into the methylator phenotype.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — IDH-mutant glioma sits in a macrophage-rich niche: tumor-associated macrophages and microglia populate the microenvironment, though the mutant metabolite makes it less inflamed than aggressive glioblastoma.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — IDH-mutant glioma turns to VEGF as it progresses: initially less vascular than glioblastoma, it ramps up VEGF-driven angiogenesis when it transforms to higher grade, marking the dangerous turn.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — IDH-mutant gliomas favor the frontal and temporal lobes: temporal tumors invade the hippocampus, causing memory loss and the seizures that are often the first symptom of these slow-growing cancers.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — IDH-mutant glioma can steal vision: tumors near the optic pathways cause visual-field defects, and their location often shapes the first symptoms as much as the seizures do.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — IDH-mutant glioma keeps a tighter blood-brain barrier: its endothelial cells stay relatively intact, so the low-grade tumor often shows little contrast enhancement on MRI and resists drug delivery.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows IDH glioma's quiet infiltration: well-differentiated tumor cells slip diffusely between intact neurons and vessels, lacking the necrosis and bizarre vasculature of glioblastoma — the ultrastructure of a lower-grade, slower cancer.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Even a low-grade glioma plugs into the brain's electricity: its cells carry the potassium and other ion channels that let them depolarize with neuronal activity, an excitability that promotes migration and sparks the seizures these tumors so often cause.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — IDH glioma almost never leaves the brain, but rarely it can: like other gliomas, extracranial spread to the lung and bone is an exceptional late event, usually after surgery has breached the natural barriers.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — The mutant enzyme is itself a target: IDH1 R132H is so uniform that a specific antibody stains it on biopsy, instantly confirming the diagnosis, and the neoantigen it creates is being chased by IDH-vaccine trials to provoke an antibody and T-cell response.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Long-term seizure control leans on magnesium and other ions: anticonvulsants and the tumor's own ion fluxes disturb electrolyte balance, and magnesium is watched in these patients as both an anti-seizure adjunct and a casualty of supportive care.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Treatment turns on the marrow: temozolomide chemoradiation suppresses neutrophil counts, and a rising neutrophil-to-lymphocyte ratio in the blood tracks the inflammatory, immune-suppressive state that marks more aggressive glioma behavior.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — These gliomas hit young adults in their reproductive years: the alkylating PCV and temozolomide chemotherapy used against them is gonadotoxic, so fertility preservation is discussed before treating a disease whose long survival makes it matter.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — The mutation rewrites the cell's methylation: 2-hydroxyglutarate from mutant IDH blocks the TET demethylases, tipping the balance toward DNMT-driven DNA methylation and the glioma CpG-island methylator phenotype that defines these tumors.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The oncometabolite muffles the immune attack: 2-hydroxyglutarate leaks from the tumor and suppresses helper T-cell activation and infiltration, helping IDH-mutant gliomas stay immunologically cold and dampening responses to immunotherapy.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR sorts gliomas the other way: amplification of this receptor marks the aggressive IDH-wildtype glioblastomas, so its absence helps confirm the IDH-mutant diagnosis — the two molecular profiles define largely separate diseases with very different prognoses.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — The oncometabolite also blunts innate killing: 2-hydroxyglutarate downregulates NKG2D-ligand display and impairs natural killer cell cytotoxicity, another way IDH-mutant tumors evade immune clearance beyond their effect on T cells.
- `connects-to` → **[ATP](../../03-molecular/atp/README.md)** — The mutation rewires metabolism: instead of making NADPH from isocitrate, mutant IDH burns it to manufacture 2-hydroxyglutarate, perturbing the cell's redox and energy economy that normally feeds ATP production through the TCA cycle.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — The oncometabolite perturbs the oxygen sensor: 2-hydroxyglutarate competitively inhibits the α-ketoglutarate-dependent prolyl hydroxylases that regulate HIF-1α, disturbing the hypoxia-response pathway as part of IDH-mutant tumor metabolism.
- `connects-to` → **[Stroke](../stroke/README.md)** — Brain irradiation injures the vessels: the radiotherapy used for IDH-mutant glioma causes a late cerebral vasculopathy that raises stroke risk in these often long-surviving patients, a delayed cost of treatment.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Tumor and treatment can hurt the nerves: infiltrating glioma and the surgery and radiation used against it injure sensory pathways, contributing to headache and neuropathic pain in the disease course.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Tumor-associated microglia stoke the inflammasome: NLRP3 activation in the glioma microenvironment releases IL-1β that shapes the immunosuppressive, pro-tumor inflammation even in these slower-growing IDH-mutant gliomas.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Brain tumors clot the veins: like other gliomas, IDH-mutant tumors raise venous thromboembolism risk through tumor tissue factor and the immobility of neurological disease and surgery.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Temozolomide opens an infection gap: the alkylating chemotherapy used in IDH-mutant glioma causes lymphopenia, predisposing to opportunistic infection including Pneumocystis pneumonia and to sepsis.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its therapy specifically courts it: temozolomide-induced lymphopenia plus the prolonged dexamethasone used for tumor edema set up Pneumocystis pneumonia, so prophylaxis is recommended during chemoradiation.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chemo and chronic illness blunt the marrow: temozolomide myelosuppression plus the inflammatory burden of a long-standing glioma depress erythropoiesis, adding an anemia-of-chronic-disease component.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A young-onset brain tumor weighs on mood: depression is common in IDH-mutant glioma, arising from tumor disruption of brain networks, corticosteroids and the burden of a slowly progressive, ultimately incurable cancer in young adults.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Its steroids raise blood sugar: the dexamethasone used to control peritumoral edema in IDH-mutant glioma induces insulin resistance, frequently causing steroid-induced hyperglycemia and diabetes.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Temozolomide and steroids open the lung to mold: the lymphopenia from temozolomide plus prolonged dexamethasone suppress immunity, occasionally permitting invasive aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Chronic steroids impair repair: the long-term dexamethasone used to manage IDH-mutant glioma thins skin and slows the healing of craniotomy and biopsy wounds.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Steroids and radiation disturb the glands: the prolonged dexamethasone for IDH-mutant glioma causes steroid diabetes and adrenal suppression, and radiation near the sella can damage the pituitary.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its drugs trouble the gut: dexamethasone raises peptic-ulcer risk and temozolomide causes nausea and hepatotoxicity, complicating the long treatment course of IDH-mutant glioma.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A slow but incurable brain tumour breeds worry: the indolent-but-progressive course, repeated scans and eventual transformation risk of IDH-mutant glioma foster chronic health anxiety alongside depression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its oncometabolite hides it from immunity: the D-2-hydroxyglutarate made by IDH-mutant tumours is immunosuppressive, making these 'cold' tumours, and dexamethasone further blunts immune defence.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The same mutation deforms bone: mosaic IDH mutations cause the multiple enchondromas of Ollier disease and Maffucci syndrome, which themselves predispose to gliomas.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It can come with skin haemangiomas: Maffucci syndrome pairs IDH-driven enchondromas with spindle-cell haemangiomas of the skin, on top of the radiation and steroid skin effects of treatment.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Brain tumours are prothrombotic: IDH-mutant glioma carries a raised venous thromboembolism risk, and the corticosteroids used for oedema add hypertension.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Immobility and steroids endanger the lungs: pulmonary embolism, aspiration and steroid-related Pneumocystis pneumonia threaten patients during long glioma treatment.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A new oncometabolite-targeted drug: IDH inhibitors such as vorasidenib block the mutant enzyme's 2-hydroxyglutarate production, delaying progression of IDH-mutant glioma.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo follows surgery and radiation: PCV (procarbazine-CCNU-vincristine) or temozolomide is the chemotherapy backbone, with the 1p/19q-codeleted oligodendroglioma especially chemosensitive.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — An immunologically cold tumour: the 2-hydroxyglutarate oncometabolite suppresses T-cell infiltration, leaving IDH-mutant glioma largely unresponsive to PD-1 checkpoint inhibitors.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Brain drainage shapes its immunity: CNS antigens drain through meningeal lymphatics, and the limited immune surveillance of this route helps keep IDH-mutant glioma immunologically cold.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — The oncometabolite reaches beyond DNA: D-2-hydroxyglutarate inhibits α-ketoglutarate-dependent prolyl-hydroxylases that mature collagen, so IDH-mutant cells suffer impaired collagen and basement-membrane assembly alongside the DNA hypermethylation that defines them.
- `connects-to` → **[CML](../cml/README.md)** — A targeted-therapy milestone repeated: as imatinib turned chronic myeloid leukaemia controllable, vorasidenib (INDIGO, 2023) became the first targeted drug to delay treatment in IDH-mutant glioma—each proof that blocking one driver reshapes a cancer.
- `connects-to` → **[CMML](../cmml/README.md)** — One epigenetic lesion, blood and brain: CMML, a myelodysplastic/myeloproliferative overlap, is driven by TET2-pathway methylation disturbances akin to the DNA hypermethylation IDH mutation causes in glioma—convergent epigenetic dysregulation in unrelated tissues.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Neuron-glioma synapses: IDH-mutant gliomas, like glioblastoma and diffuse midline glioma, wire into neural circuits through activity-dependent and BDNF-driven synapses with neurons that drive growth and invasion.
- `connects-to` → **[MDS](../mds/README.md)** — IDH inhibitors across cancers: IDH1/2 mutations also drive a subset of myelodysplastic syndromes and AML, so the same IDH inhibitors (ivosidenib, enasidenib) target glioma, MDS and leukaemia.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Diffuse white-matter infiltration: IDH-mutant gliomas spread along white-matter tracts and the axonal scaffold far beyond the visible tumour, the reason they cannot be cured by surgery despite slow growth.
- `connects-to` → **[Pheochromocytoma & Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Oncometabolite paradigm: the 2-hydroxyglutarate of IDH-mutant glioma parallels the succinate of SDH-mutant paraganglioma and the fumarate of HLRCC—each oncometabolite inhibits alpha-ketoglutarate dioxygenases and drives DNA hypermethylation.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Methylator phenotypes converge: the IDH-driven hypermethylation (G-CIMP) of IDH-mutant glioma mirrors the CpG-island methylator phenotype (CIMP) of a colorectal cancer subset, both silencing tumour suppressors epigenetically.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Tumour vasculature on transformation: high-grade progression of IDH-mutant glioma brings microvascular proliferation, the abnormal leaky arterial walls of tumour angiogenesis driven by VEGF and hypoxia.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Locked-in hypermethylation: the 2-hydroxyglutarate-driven CpG-island methylator phenotype, reinforced by polycomb/EZH2 activity, blocks differentiation in IDH-mutant glioma.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT progression: activation of PI3K-AKT-mTOR signalling contributes to the malignant progression of IDH-mutant glioma to higher grades.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Oncogenic transcription: MYC programmes become activated during the transformation of IDH-mutant glioma, driving the proliferation that marks high-grade disease.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: CDKN2A/B homozygous deletion—a marker of grade-4 IDH-mutant glioma—unleashes CDK4/6, accelerating the cell cycle and worsening prognosis.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — G1 progression: cyclin D1-CDK4/6 activity drives IDH-mutant glioma cells through the G1 checkpoint, the proliferative output that intensifies with malignant progression.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Glioma growth factor: PDGF signalling supports the proliferation and stromal recruitment of IDH-mutant gliomas, an autocrine driver of these astrocytic and oligodendroglial tumours.
- `connects-to` → **[RAD51](../../03-molecular/rad51/README.md)** — Oncometabolite BRCAness: 2-hydroxyglutarate from mutant IDH impairs homologous-recombination repair (a RAD51-dependent 'BRCAness'), creating sensitivity to PARP inhibitors and DNA-damaging therapy.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Myeloid recruitment: CCL2 recruits microglia and macrophages into IDH-mutant gliomas, though the 2-HG-rich microenvironment is less myeloid-inflamed than IDH-wildtype glioblastoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RTK-MAPK proliferation: RAS-RAF-ERK signalling downstream of growth-factor receptors contributes to IDH-mutant glioma proliferation and intensifies with malignant transformation.
- `connects-to` → **[EGLN1 (PHD2)](../../03-molecular/egln1/README.md)** — The 2-hydroxyglutarate produced by mutant IDH competitively inhibits α-ketoglutarate-dependent dioxygenases including the EGLN/PHD prolyl hydroxylases and the TET and histone demethylases—the broad epigenetic dysregulation (the G-CIMP phenotype) that defines these tumors.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on IDH-mutant glioma cells follows CXCL12 gradients to drive the diffuse white-matter infiltration that makes even these lower-grade gliomas impossible to fully resect and dooms them to eventual recurrence.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — IDH-mutant gliomas are more sensitive to radiation and temozolomide than IDH-wildtype tumors, engaging caspase-3-mediated apoptosis more readily—part of why they carry a markedly better prognosis than glioblastoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The uniform IDH1 R132H mutation creates a shared neoantigen, and IDH vaccines aim to direct cytotoxic T cells to kill the tumor through perforin and granzyme, an immunotherapy strategy unique to this molecularly defined glioma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — The oncometabolite 2-hydroxyglutarate suppresses innate immune signaling including the STING-interferon axis and impairs T-cell function, helping make IDH-mutant glioma an immunologically cold tumor that IDH inhibitors may help thaw.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 from activated microglia contributes to the neuroinflammatory microenvironment of IDH-mutant glioma, a microglial signal increasingly studied as a modifier of glioma progression.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA activates the PI3K-AKT-mTOR axis (AKT and mTOR already mapped) that is co-active in IDH-mutant glioma and contributes to its growth.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis (mapped, with CDKN2A loss marking grade progression) releases E2F1 to drive the proliferation accompanying transformation of IDH-mutant glioma to higher grade.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling shapes the oligodendroglial and astrocytic differentiation programs of IDH-mutant glioma, influencing the lineage and behavior of these lower-grade tumors.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Deregulation of the RB1-E2F checkpoint (CDKN2A, CDK4/6 and cyclin-D1 already mapped) drives the malignant progression of IDH-mutant glioma toward higher grade.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — RAS-MAPK signaling (ERK1/2 already mapped) downstream of receptor tyrosine kinases contributes a proliferative input to IDH-mutant glioma.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — The IDH-mutant oncometabolite 2-hydroxyglutarate alters cellular redox and glutathione metabolism, and NRF2 antioxidant signaling shapes the resulting oxidative vulnerability of these gliomas.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling modulates the invasion and immunosuppressive microenvironment of IDH-mutant glioma.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 signaling contributes to the proliferative and reactive-astrocytic responses in IDH-mutant glioma.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN restraint on PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) accompanies progression of IDH-mutant glioma toward secondary glioblastoma.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — The 2-hydroxyglutarate of IDH-mutant glioma suppresses IFN-STAT1 signaling, contributing to the immunologically cold microenvironment of these tumors.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the microenvironment and invasive behavior of IDH-mutant glioma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the metabolic and oxidative stress of the 2-hydroxyglutarate-accumulating cells of IDH-mutant glioma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt/β-catenin signaling of IDH-mutant glioma cells.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in IDH-mutant glioma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the relatively immune-cold microenvironment of IDH-mutant glioma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of growth-factor receptors contributes to the invasive signaling of IDH-mutant glioma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the metabolic adaptation of the 2-hydroxyglutarate-producing cells of IDH-mutant glioma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic reprogramming of IDH-mutant glioma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the tumor microenvironment of IDH-mutant glioma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape (interacting with the 2-hydroxyglutarate-driven hypermethylation) of IDH-mutant glioma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the tumor-microenvironment and survival signaling of IDH-mutant glioma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of IDH-mutant glioma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the microglial and tumor-immune microenvironment of IDH-mutant glioma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammatory tumor microenvironment of IDH-mutant glioma.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the tumor microenvironment of IDH-mutant glioma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the tumor microenvironment and immune signaling of IDH-mutant glioma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microglial/macrophage tumor microenvironment of IDH-mutant glioma (which is comparatively immune-cold relative to IDH-wildtype glioblastoma).
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — IDH neoantigen vaccine: the IDH1-R132H mutation (IDH1 already mapped) creates a shared neoantigen, and MHC class II-restricted presentation of it underlies the IDH peptide vaccines being tested to mobilise T cells against IDH-mutant glioma.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell mobilisation: IL-2-driven T-cell expansion supports the vaccine and cellular immunotherapy approaches for IDH-mutant glioma, whose 2-hydroxyglutarate-rich microenvironment otherwise suppresses effective T-cell responses.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Immune-cold checkpoint: IDH-mutant glioma is relatively immune-cold, the oncometabolite 2-hydroxyglutarate dampening immune infiltration, which blunts PD-1 checkpoint-blockade responses and motivates combination strategies with IDH inhibitors.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive metabolite: the oncometabolite 2-hydroxyglutarate and IL-10 in the microenvironment blunt T-cell responses (PD-1 already mapped), part of the immune-cold state of IDH-mutant glioma that IDH inhibitors aim to reverse.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Neuronal signalling: alongside the glutamatergic input (glutamate already mapped), GABAergic signalling shapes the neuronal activity of the infiltrated cortex, contributing to the seizures that frequently present IDH-mutant glioma.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of IDH-mutant glioma, part of the stromal microenvironment of this more indolent but ultimately progressive diffuse glioma.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia (already mapped) and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6 and IL-1 already mapped) of the IDH-mutant glioma microenvironment.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 microglial polarisation: IL-4 polarises the tumour-associated microglia and macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the immune-evasive niche of IDH-mutant glioma.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and metabolic stress: the 2-hydroxyglutarate-driven metabolic rewiring of the IDH-mutant cell generates oxidative stress (NRF2 already mapped), to which xanthine oxidase contributes, part of the tumour microenvironment.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 microglial (already mapped) niche of the relatively cold immune microenvironment of IDH-mutant glioma.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Neuron-glioma signalling: alongside the glutamate and GABA (already mapped) synapses, cholinergic acetylcholine signalling is part of the neuronal activity that drives the growth of the electrically integrated IDH-mutant glioma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — NMDA modulation: magnesium blocks the NMDA receptor and modulates the glutamate (already mapped) excitotoxicity and the neuron-glioma synaptic drive that promote the growth of IDH-mutant glioma.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lipid metabolic reprogramming: the cholesterol and lipid metabolism of the IDH-mutant glioma, part of the metabolic reprogramming driven by the 2-hydroxyglutarate (IDH already mapped), is a therapeutic vulnerability.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Serotonergic neuromodulation: serotonin modulates the neuron-glioma (glutamate, GABA and acetylcholine already mapped) circuits whose activity drives the growth of IDH-mutant glioma.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Noradrenergic input: noradrenaline is part of the neuronal-activity-dependent (glutamate already mapped) signalling that stimulates the proliferation of IDH-mutant glioma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Cold-tumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is suppressed by the 2-hydroxyglutarate (IDH already mapped), contributing to the immunologically cold microenvironment of IDH-mutant glioma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells is dampened by the 2-hydroxyglutarate (IDH already mapped) immunosuppression of IDH-mutant glioma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) response opposing the immunosuppressive, oncometabolite-driven (IDH already mapped) microenvironment of IDH-mutant glioma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin links the metabolic state to the immune response and, with the dexamethasone-induced metabolic syndrome, is part of the systemic milieu of IDH-mutant glioma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu, altered by the steroid therapy of IDH-mutant glioma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine dimension of the neuroinflammatory microenvironment of IDH-mutant glioma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immunologically cold microenvironment of IDH-mutant glioma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of the IDH-mutant-glioma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune microenvironment of IDH-mutant glioma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the microglial (already mapped) and myeloid activation of the immunosuppressive IDH-mutant-glioma microenvironment (blunted by the 2-hydroxyglutarate).
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Meningeal mast cells: the mast cells of the meninges and the brain (already mapped) contribute to the neuroinflammation and the vascular permeability of the IDH-mutant-glioma microenvironment.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells organise the tertiary lymphoid structures whose presence, with the CD8 (already mapped) TILs, may mark the immune response of IDH-mutant glioma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: complement C5 and its C5a anaphylatoxin (with C3 and C5aR1 already mapped) drive myeloid infiltration and the pro-tumour neuroinflammation of the IDH-mutant glioma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: IDH-mutant glioma cells recruit factor H to bind C3b and downregulate the alternative pathway (C3, C5 and C5aR1 already mapped), evading complement-mediated tumour surveillance.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Anti-glioma VDR signalling: vitamin D (VDR expressed in IDH-mutant glioma) suppresses proliferation and correlates with better prognosis; low serum levels associate with shorter time to progression in lower-grade glioma.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin in the glioma microenvironment: TSLP released by IDH-mutant glioma cells primes dendritic cells (already mapped) and mast cells (already mapped) to sustain the Th2-skewed (IL-4, IL-13 already mapped) immunosuppressive microenvironment of lower-grade glioma.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Vascular permeability mediator: bradykinin, acting on B2 receptors of the endothelial cells (already mapped) of the blood-brain barrier, amplifies its disruption in IDH-mutant glioma, contributing to peritumoral oedema and the nitric oxide (already mapped) signalling.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement regulation: C1-INH controls the classical-pathway arm (C3, C5, C5aR1 and factor H already mapped) of the complement-mediated immune surveillance of IDH-mutant glioma cells, whose 2-hydroxyglutarate blunts the innate immune response.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine-IDH-glioma axis: histamine, released by microglia (already mapped) and mast cells in the IDH-mutant glioma microenvironment, signals via H3 receptors on neurons (already mapped) and H1/H2 on tumour cells, modulating 2-HG-mediated immunosuppression.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-IDH-glioma axis: melatonin, crossing the blood-brain barrier, suppresses IDH-mutant glioma cell proliferation, modulates the 2-HG (IDH1/2 already mapped) metabolic milieu and its epigenetic silencing, and enhances apoptotic sensitivity to temozolomide.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-IDH-glioma axis: erythropoietin, via the EPOR on IDH-mutant glioma cells (already mapped), activates the JAK-STAT (already mapped) neuroprotective pathway and modulates microglia/macrophage (already mapped) polarisation in the IDH-mutant glioma microenvironment.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — IDH-glioma prolactin: prolactin, via PRLR on microglia (already mapped) and macrophages (already mapped), modulates the immune TME; hyperprolactinaemia amplifies the IL-6 (already mapped) and mast-cell (already mapped) T-cytotoxic (already mapped) cascade of IDH-mutant glioma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — IDH-glioma oxytocin: oxytocin, via OXTR on microglia (already mapped) and macrophages (already mapped), attenuates neuroinflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) T-cytotoxic (already mapped) cascade of IDH-mutant glioma.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — IDH-glioma vasopressin: vasopressin, via V1aR on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; vasopressin dysregulation amplifies the IL-6 (already mapped) and mast-cell (already mapped) cascade of IDH-mutant glioma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — IDH-glioma testosterone: testosterone, via AR on microglia (already mapped) and macrophages (already mapped), modulates the neuroinflammatory TME; testosterone deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) cascade of IDH-mutant glioma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — IDH-glioma selenium: selenium, as GPx in microglia (already mapped) and macrophages (already mapped), scavenges ROS; selenium deficiency amplifies the IL-6 (already mapped) and T-cytotoxic (already mapped) oxidative cascade of IDH-mutant glioma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — IDH-glioma iodine: iodine-dependent thyroid hormones modulate microglia (already mapped) polarisation and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the IL-6 (already mapped) and mast-cell (already mapped) cascade of IDH-mutant glioma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — IDH-glioma sodium: high dietary sodium promotes microglia (already mapped) and mast-cell (already mapped) activation; sodium-induced IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) tumour cascade of IDH-mutant glioma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — IDH-glioma copper: copper supports microglia (already mapped) and T-cytotoxic (already mapped) anti-tumour function; copper deficiency amplifies IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of IDH-mutant glioma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — IDH-glioma zinc: zinc cofactors antioxidant enzymes in microglia (already mapped) and T-cytotoxic cells (already mapped); zinc deficiency amplifies IL-6 (already mapped) and mast-cell (already mapped) tumour-promoting cascade of IDH-mutant glioma.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — IDH-glioma chloride: chloride channels regulate microglia (already mapped) and T-cytotoxic (already mapped) volume during tumour microenvironment stress; chloride dysregulation amplifies IL-6 (already mapped) and mast-cell (already mapped) tumour cascade in IDH-mutant glioma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — IDH-glioma nitrogen: nitrogen as backbone of IDH-mutant oncoproteins and cytokines (already mapped) sustains oncometabolite signalling; nitrogen-derived RNS from microglia (already mapped) amplifies NF-κB (already mapped) and IL-6 (already mapped) in IDH-mutant glioma.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — IDH-glioma phosphorus: phosphorus as ATP in microglia (already mapped) and T-cytotoxic cells (already mapped) fuels anti-tumour kinase signalling; phosphorus dysregulation amplifies IL-6 (already mapped) and mast-cell (already mapped) cascade in IDH-mutant glioma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — IDH-glioma hydrogen: hydrogen via ROS from microglia (already mapped) and T-cytotoxic cells (already mapped) modulates redox homeostasis; hydrogen excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — IDH-glioma oxygen: ROS from NADPH-oxidase in microglia (already mapped) and T-cytotoxic cells (already mapped) drives tumour oxidative stress; oxygen dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — IDH-glioma sulfur: sulfur-containing amino acids in microglia (already mapped) and T-cytotoxic cells (already mapped) regulate redox signalling; sulfur dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — IDH-glioma glp-1: GLP-1 from neurons (already mapped) and microglia (already mapped) modulates metabolic-inflammatory tone; glp-1 dysfunction amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-mutant glioma.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — IDH-glioma angiotensin-ii: angiotensin-II from microglia (already mapped) and endothelial cells (already mapped) drives vascular remodelling; angiotensin-ii excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[WNT/β-Catenin](../../03-molecular/wnt-beta-catenin/README.md)** — IDH-glioma wnt-beta-catenin: WNT/β-catenin on microglia (already mapped) and tumour cells (already mapped) regulates invasion; wnt-beta-catenin dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — IDH-glioma rankl: RANKL from microglia (already mapped) and tumour cells (already mapped) modulates glioma immune crosstalk; rankl excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — IDH-glioma fibronectin: fibronectin in microglia (already mapped) and tumour cells (already mapped) promotes glioma ECM remodelling; fibronectin excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IDH-glioma igf-1: IGF-1 from microglia (already mapped) and tumour cells (already mapped) promotes glioma proliferation; igf-1 excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — IDH-glioma activin-a: activin-A from microglia (already mapped) and tumour cells (already mapped) promotes glioma fibrosis; activin-a excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — IDH-glioma cgrp: CGRP from microglia (already mapped) and tumour cells (already mapped) modulates glioma neuroimmune tone; cgrp excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — IDH-glioma calcitonin: calcitonin from microglia (already mapped) and tumour cells (already mapped) modulates glioma calcium tone; calcitonin dysregulation amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — IDH-glioma substance-p: substance-P from microglia (already mapped) and tumour cells (already mapped) modulates glioma pain tone; substance-P excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — IDH-glioma insulin-receptor: insulin receptor on microglia (already mapped) and tumour cells (already mapped) modulates glioma metabolic axis; insulin-receptor loss amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — IDH-glioma aldosterone: aldosterone from microglia (already mapped) and tumour cells (already mapped) modulates glioma fluid balance; aldosterone excess amplifies IL-6 (already mapped) and NF-κB (already mapped) and mast-cell (already mapped) cascade in IDH-glioma.

[^mellinghoff-2023-vorasidenib-lgg]: Mellinghoff IK, van den Bent MJ, Blumenthal DT, et al. Vorasidenib in IDH1- or IDH2-mutant low-grade glioma. *N Engl J Med.* 2023;389(7):589-601. [doi:10.1056/NEJMoa2304194](https://doi.org/10.1056/NEJMoa2304194) · [PubMed 37272530](https://pubmed.ncbi.nlm.nih.gov/37272530/)
[^jiao-2012-atrx-glioma]: Jiao Y, Killela PJ, Reitman ZJ, et al. Frequent ATRX, CIC, FUBP1 and IDH mutations refine the classification of malignant gliomas. *Oncotarget.* 2012;3(7):709-722. [doi:10.18632/oncotarget.588](https://doi.org/10.18632/oncotarget.588) · [PubMed 22869205](https://pubmed.ncbi.nlm.nih.gov/22869205/)
