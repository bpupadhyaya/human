---
schema: human-scale-entry/v1
id: giant-cell-arteritis
name: Giant Cell Arteritis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Giant cell arteritis (GCA) is the most common primary vasculitis in adults >50; granulomatous inflammation of temporal arteries and aortic branches; IL-6 and IL-1β drive pathogenesis. Tocilizumab (anti-IL-6R; GiACTA; FDA May 2017) is the first approved steroid-sparing therapy."
aliases: ["GCA", "giant cell arteritis", "temporal arteritis", "cranial arteritis", "Horton disease", "polymyalgia rheumatica"]
sources:
  - id: stone-2017-giact
    type: peer-reviewed
    cite: "Stone JH, Tuckwell K, Dimonaco S, et al. Trial of tocilizumab in giant-cell arteritis. N Engl J Med. 2017;377(4):317-328."
    doi: "10.1056/NEJMoa1613849"
    pmid: "28745999"
    url: "https://doi.org/10.1056/NEJMoa1613849"
  - id: weyand-2014-gca-review
    type: peer-reviewed
    cite: "Weyand CM, Goronzy JJ. Clinical practice. Giant-cell arteritis and polymyalgia rheumatica. N Engl J Med. 2014;371(1):50-57."
    doi: "10.1056/NEJMcp1214926"
    pmid: "24988557"
    url: "https://doi.org/10.1056/NEJMcp1214926"
cross_links:
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β, released by activated macrophages in the adventitia and media, amplifies vascular NF-κB activation and macrophage recruitment in GCA; anakinra and canakinumab (IL-1 blockers) are in Phase 2/3 investigation for GCA as steroid-sparing alternatives."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is the dominant systemic effector in GCA — drives CRP/ESR elevation, fever, and constitutional symptoms; tocilizumab (anti-IL-6R; GiACTA: 56% vs 18% sustained remission at 52 weeks; FDA May 2017) is the cornerstone biologic for GCA."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "GCA involves Th17 (IL-17A) and Th1 (IFN-γ) CD4+ T cell infiltrate in the arterial adventitia; IL-17A amplifies macrophage/neutrophil recruitment and intimal hyperplasia; secukinumab (anti-IL-17A) and upadacitinib (JAK1 inhibitor; SELECT-GCA) are under investigation."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "IFN-γ from Th1 CD4+ T cells drives macrophage activation → multinucleated giant cell formation and intimal hyperplasia in GCA; high IFN-γ in arterial tissue correlates with GCA activity and distinguishes GCA from Takayasu arteritis histologically."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "GCA is named for the multinucleated giant cells formed when IFN-γ-activated M1 macrophages fuse at the intima-media junction; these macrophages secrete IL-6, VEGF, PDGF, and IGF-1, driving the acute-phase response, neovascularization, and intimal hyperplasia."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Adventitial CD4+ T cells drive the adaptive phase of GCA: Th1 cells secrete IFN-γ (macrophage activation, giant cells) and Th17 cells secrete IL-17A (constitutional symptoms); both arms resist steroids, motivating IL-6R (tocilizumab) and JAK (upadacitinib) blockade."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Macrophage-derived PDGF and IGF-1 drive vascular smooth muscle cell migration from media to intima with myofibroblast proliferation → intimal hyperplasia → luminal occlusion → the ischemia behind headache, jaw claudication, and irreversible anterior ischemic optic neuropathy."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Giant cell arteritis and ANCA vasculitis are vasculitides contrasted by vessel caliber: GCA strikes large arteries with granulomatous giant-cell inflammation, AAV small vessels with pauci-immune necrosis — poles of the vasculitis spectrum sharing IL-6-driven inflammation."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "GCA inflammation centers on the artery wall: macrophage VEGF drives neovascularization of the normally avascular media, while intimal endothelial and myofibroblast proliferation narrows the lumen, producing the ischemic optic neuropathy and jaw claudication that define it."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "GCA of the vertebral and carotid arteries can cause posterior-circulation (vertebrobasilar) stroke — distinct from the more common anterior ischemic optic neuropathy; prompt high-dose glucocorticoids reduce this risk, making GCA a treatable cause of stroke in the elderly."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sudden permanent blindness is the feared emergency of giant-cell arteritis: inflammatory occlusion of the posterior ciliary arteries causes anterior ischemic optic neuropathy, often after jaw claudication and amaurosis fugax; suspected GCA gets immediate high-dose steroids."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Giant-cell arteritis is a large-vessel vasculitis of the cardiovascular system: granulomatous inflammation of the aorta and its branches can cause aneurysm, dissection and arm claudication years after the cranial phase, so long-term vascular imaging surveillance is recommended."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells ignite giant-cell arteritis: resident vascular dendritic cells in the artery's adventitia activate and recruit the CD4+ T cells and macrophages that form the granulomas and giant cells, making them the proposed initiator of the arterial attack."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Giant cell arteritis and rheumatoid arthritis are both IL-6-driven autoimmune diseases of older adults that respond to tocilizumab: GCA inflames large arteries while RA destroys synovial joints—shared cytokine biology lets one biologic treat both."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 helps polarize the T-cell response in giant cell arteritis: dendritic cells in the arterial wall secrete IL-12 to push T cells toward Th1, generating IFN-γ-producing cells whose granulomatous infiltrate, with giant cells, destroys the artery's elastic lamina."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK-STAT signaling is a therapeutic target in giant cell arteritis: the IL-6 and IFN-γ driving arterial inflammation act through JAK kinases, so JAK inhibitors are in trials to spare steroids—linking GCA to the node mutated in myeloproliferative disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF helps GCA both damage and compensate: inflammatory cytokines drive VEGF that promotes neovascularization in the inflamed artery wall, while ischemia downstream stimulates collateral vessels—so angiogenesis is part of both injury and response in GCA."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Giant cell arteritis is a large-vessel disease that threatens the aorta: beyond the temporal artery, granulomatous inflammation can involve the aorta and its branches, causing thoracic aortic aneurysm and dissection years later—so GCA needs vascular surveillance."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Giant cell arteritis and lupus are both autoimmune but differ sharply: GCA is a granulomatous large-vessel vasculitis of the elderly driven by Th1/Th17 and IL-6, while SLE is an immune-complex multisystem disease of the young—contrasting mechanisms of autoimmunity."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Giant cell arteritis is a glucocorticoid emergency: high-dose cortisol-mimicking steroids must start immediately on suspicion to prevent irreversible blindness from ischemic optic neuropathy—treatment precedes biopsy because delay risks sudden, permanent vision loss."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Giant cell arteritis threatens the nervous system through vascular ischemia: inflamed cranial arteries cause severe headache, jaw claudication and, most feared, sudden blindness from anterior ischemic optic neuropathy, plus a raised risk of stroke."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Giant cell arteritis is an autoimmune large-vessel vasculitis: dendritic cells and IL-6-driven Th17/Th1 responses inflame the artery wall with granulomas and giant cells, so it overlaps with other autoimmunity and responds to IL-6 blockade and steroids."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Giant cell arteritis overlaps polymyalgia rheumatica: up to half of GCA patients have the proximal shoulder- and hip-girdle aching of PMR, and jaw claudication reflects muscle ischemia—so a musculoskeletal syndrome and a blinding vasculitis are two faces of one disease."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts cause the vessel-narrowing of giant cell arteritis: activated by inflammation, intimal myofibroblasts proliferate and thicken the artery wall, so the lumen occludes and downstream tissue (optic nerve, brain) is starved of blood—GCA's ischemic basis."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Giant cell arteritis reflects failed immune regulation: deficient regulatory T cells let Th1 and Th17 cells attack the arterial wall, so the imbalance between effector and regulatory T cells underlies the granulomatous inflammation that defines the disease."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Giant cell arteritis announces itself through red cells: the inflammation drives a sky-high erythrocyte sedimentation rate (ESR) and an anemia of chronic disease, so a markedly elevated ESR in an older patient with headache is a classic trigger to start steroids urgently."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Giant cell arteritis blocks arteries by laying down collagen: after inflammation chews up the elastic lamina, the wall heals with collagen-rich intimal thickening that narrows the lumen, causing the jaw claudication and sudden vision loss that make it an emergency."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Giant cell arteritis builds granulomas with TNF: this cytokine helps fuse macrophages into the multinucleated giant cells that define the lesion, part of the Th1/Th17 inflammatory storm attacking the artery wall."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Giant cell arteritis blinds by cutting off oxygen: inflammation narrows the arteries feeding the optic nerve, and the resulting ischemia (arteritic AION) can cause sudden, permanent vision loss—why suspected GCA is a steroid emergency."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Giant cell arteritis can starve the brain: when the inflamed large arteries supplying the head narrow or clot, patients suffer TIAs and strokes, so cranial and vertebral artery involvement makes prompt treatment urgent."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF drives the artery-closing overgrowth in giant cell arteritis: it pushes smooth muscle cells to migrate and proliferate into the intima, thickening the wall until the lumen narrows—the structural step from inflammation to ischemia."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Giant cell arteritis drives down iron use: its intense systemic inflammation suppresses red-cell production and locks iron away, causing the anemia of chronic disease that, with a sky-high ESR, supports the diagnosis."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Giant cell arteritis can show on the scalp: the inflamed scalp arteries make it tender and, when severely blocked, can cause scalp or tongue necrosis—dramatic signs of the vasculitis starving surface tissues."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Giant cell arteritis heals into fibrosis: the inflamed artery wall thickens its inner layer with fibrous tissue, narrowing the lumen, so scarring—not just acute swelling—drives the lasting blockage and ischemia."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "GCA is found by imaging and biopsy: ultrasound shows the artery-wall 'halo,' PET lights up large-vessel inflammation, and the temporal-artery biopsy reveals giant cells under the microscope."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "GCA can starve the nerves: ischemia from vasculitis of the vasa nervorum causes peripheral neuropathy and mononeuritis, beyond the optic-nerve infarction that threatens sight."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "GCA's treatment threatens bone: the prolonged high-dose steroids needed to prevent blindness leach calcium and cause osteoporosis, a major long-term harm of controlling the disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows GCA chewing through the artery wall: multinucleated giant cells gather along the fragmented internal elastic lamina they are destroying, the granulomatous lesion that names the disease."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "GCA can starve the gut: when the large-vessel inflammation reaches the mesenteric arteries, it threatens bowel ischemia, a rare but grave extension of a disease usually thought of as confined to the head."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "GCA occasionally speaks through the lungs: a dry cough or other respiratory symptoms can be the unexpected presenting complaint, the vasculitis reaching the airways and pulmonary vessels."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "An antibody spares the steroids: tocilizumab, a monoclonal antibody against the IL-6 receptor, is the key steroid-sparing treatment for GCA, calming the IL-6-driven inflammation that powers the arteritis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "GCA's most feared blow is sudden blindness: inflammation of the arteries feeding the optic nerve causes anterior ischemic optic neuropathy, an emergency that demands immediate steroids to save the second eye."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Months of high-dose steroids suppress the adrenals: the prolonged prednisone needed to control GCA shuts down the body's own cortisol production, so the dose must be tapered slowly to avoid an adrenal crisis."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets both flag and threaten in GCA: a raised platelet count is a useful diagnostic clue alongside the inflammatory markers, and because the inflamed artery clots, low-dose aspirin is often added to guard against the dreaded vision loss and stroke."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "The treatment thins the bones: the months to years of high-dose glucocorticoids that control GCA are a leading cause of steroid-induced osteoporosis, so calcium, vitamin D and a bone-protecting drug are started alongside the prednisone."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "A viral trigger has been proposed: varicella-zoster virus antigen was reported in some inflamed temporal arteries, raising the idea that the reactivated virus helps ignite GCA — a link that remains debated and unproven."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "IL-23 sustains the Th17 arm of the attack: alongside the IL-12/Th1 axis, IL-23 drives the IL-17-producing T cells that inflame the artery wall in GCA, part of why cytokine-directed therapy is explored beyond IL-6 blockade."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells join the vascular infiltrate: they accumulate in the inflamed arterial wall and contribute, with T cells and macrophages, to the granulomatous destruction of the vessel."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "The cure brings its own disease: the prolonged high-dose glucocorticoids needed to control GCA commonly induce steroid diabetes, one of the metabolic harms that make sparing the steroid a goal of newer therapy."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT carries the vascular inflammation: IL-6 and interferon-γ signal through JAK1/2 to sustain the arterial-wall attack in GCA, the rationale behind the JAK inhibitors (upadacitinib) now trialed as steroid-sparing therapy."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "Large-vessel vasculitis can flag a myeloid clone: GCA and other vasculitides are over-represented in CMML and the VEXAS spectrum, where a somatic marrow mutation drives systemic inflammation alongside the cytopenias."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The aorta is in the firing line: GCA aortitis can cause aortic aneurysm and regurgitation that overload the left ventricle into heart failure, why large-vessel imaging follow-up is part of long-term care."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 drives the arteritis through STAT3: the hallmark IL-6 of GCA signals via JAK-STAT3 to sustain the Th17 and macrophage response in the vessel wall, the axis that the IL-6 blocker tocilizumab interrupts."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Systemic inflammation raises the clot risk: the intense acute-phase response of GCA, plus the high-dose corticosteroids used to treat it, increase the risk of venous thromboembolism."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Long steroid courses invite infection: GCA demands prolonged high-dose glucocorticoids, often in older patients, leaving them prone to serious infection and sepsis — a leading cause of treatment-related death."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Its inflammation blunts the marrow: GCA's intense IL-6-driven acute-phase response raises hepcidin and suppresses erythropoiesis, so a normocytic anemia of chronic disease is a common and supportive diagnostic clue."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Prolonged high-dose steroids open the lung: the months of glucocorticoids that control GCA deplete T-cell defenses, raising Pneumocystis pneumonia risk enough that prophylaxis is considered in higher-dose regimens."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Steroids and vision loss weigh on mood: the high-dose glucocorticoids for GCA cause mood disturbance and depression, compounded by the fear and disability of the irreversible blindness the disease can cause."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its high-dose steroids open the lung to mold: the prolonged glucocorticoids needed to control giant-cell arteritis deeply suppress immunity, occasionally permitting invasive aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Arterial occlusion and steroids starve tissue: severe giant-cell arteritis can cause ischemic scalp and tongue necrosis, and its chronic steroids thin skin and slow the healing of the resulting wounds."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Steroids and the threat of blindness breed worry: the psychiatric effects of high-dose glucocorticoids and the fear of sudden irreversible vision loss in GCA foster anxiety alongside depression."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Months of high-dose steroids reshape metabolism: the prolonged glucocorticoids that control GCA cause steroid-induced diabetes, adrenal suppression and a Cushingoid state, the endocrine cost of treatment."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Steroids and IL-6 blockade trouble the gut: high-dose steroids for GCA raise peptic-ulcer risk, the tocilizumab used to spare them carries a risk of lower-GI perforation, and jaw claudication makes eating painful."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its long steroid courses thin the skin: prolonged glucocorticoids for GCA cause skin atrophy, easy bruising and striae, on top of the thickened, tender temporal artery palpable on examination."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can present as a new cough: a persistent dry cough is an under-recognised symptom of giant cell arteritis, reflecting large-vessel and aortic involvement of the disease."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It spares the kidney, unlike small-vessel vasculitis: GCA characteristically leaves the kidneys untouched — a key feature distinguishing it from ANCA-associated vasculitis — though large-vessel disease can rarely involve the renal arteries."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It can masquerade as occult disease: large-vessel GCA presents as fever of unknown origin with intense systemic inflammation that mimics lymphoma, distinguished by PET showing vasculitic aortic uptake rather than nodal disease."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "High-dose steroids are the emergency treatment: prompt glucocorticoids prevent the irreversible blindness of giant cell arteritis, then taper over many months despite their cumulative toxicity."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Low-dose aspirin guards the circulation: it is often added in giant cell arteritis to reduce the risk of the ischaemic visual loss and strokes the vasculitis can cause."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Long steroids demand bone protection: patients on prolonged glucocorticoids for giant cell arteritis take vitamin D and calcium, often with a bisphosphonate, to counter steroid-induced osteoporosis."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It inflames the artery wall itself: giant cell arteritis is a granulomatous vasculitis of the media and adventitia of medium and large arteries, where T cells and macrophage-derived giant cells destroy the elastic lamina."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "A steroid-sparing immunosuppressant: methotrexate, a low-dose chemotherapy agent, is used to reduce glucocorticoid exposure in giant cell arteritis alongside IL-6 blockade."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Two ways to thicken an artery: giant cell arteritis must be distinguished from atherosclerosis on vascular imaging, and the chronic vascular inflammation it causes also accelerates atherosclerotic disease."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Biologics spare the steroids: tocilizumab (anti-IL-6R) and JAK inhibitors such as upadacitinib are targeted therapies that maintain remission in giant cell arteritis, cutting the toxic glucocorticoid burden long-term GCA control once demanded."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy can ignite the artery: large-vessel vasculitis resembling giant cell arteritis is a recognised immune-related adverse event of checkpoint inhibitors, where releasing T-cell brakes against a tumour also unleashes inflammation in the aorta and its branches."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "The inflamed artery builds its own lymphoid tissue: giant cell arteritis forms tertiary lymphoid structures with germinal-center-like T- and B-cell aggregates in the adventitia, organising the local immune attack much as a lymph node germinal center does."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Coronary and aortic involvement: giant-cell arteritis inflames large arteries including the aorta and coronaries, causing aortitis with aneurysm and, rarely, myocardial ischaemia."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Steroids thin the bone: the prolonged high-dose glucocorticoids needed to control GCA cause osteoporosis and fracture, a major iatrogenic harm driving steroid-sparing tocilizumab use."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "The sky-high ESR: acute-phase fibrinogen produced in the inflammation of GCA drives the markedly raised ESR and CRP that are central to its diagnosis and monitoring."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Clonal inflammation in older men: VEXAS syndrome and other clonal myeloid diseases (MDS) can present with a giant-cell-arteritis-like large-vessel vasculitis, blurring autoinflammation and myeloid neoplasia."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "A debated trigger and a treatment risk: varicella-zoster virus has been controversially implicated in giant-cell arteritis, and the steroid/IL-6 immunosuppression that treats it reactivates VZV as shingles."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Shared IL-6 biology: COVID-19 and giant-cell arteritis both feature IL-6-driven inflammation (both treated with tocilizumab), and de novo GCA and flares have been reported after infection or vaccination."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Ischaemia from vasoconstriction: endothelin-1 released by the inflamed vessel wall drives the vasoconstriction underlying the ischaemic blindness and jaw claudication of giant-cell arteritis."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Notch-driven vasculitis: Notch signalling activates the pathogenic Th1 and Th17 vascular T cells and promotes the vessel-wall remodelling central to giant-cell arteritis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8 T-cell infiltrate: cytotoxic and tissue-resident memory CD8 T cells populate the inflamed arterial wall in giant-cell arteritis, contributing to vessel damage and relapse."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Innate vasculitis: NLRP3-inflammasome activation in vessel-wall macrophages matures the IL-1β that amplifies the granulomatous inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes into the arterial wall in giant-cell arteritis, where they fuse into the multinucleated giant cells that name the disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Ischaemic wall: the inflamed, thickened artery in giant-cell arteritis becomes hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis of neovascularisation in the vessel wall."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Genetic risk and presentation: the strong HLA-DRB1 association of giant-cell arteritis points to MHC class II presentation of arterial-wall antigens to the CD4 T cells that orchestrate the granulomatous attack."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Myeloid alarmin: S100A8/A9 from the monocytes and neutrophils infiltrating the temporal artery amplifies inflammation in giant-cell arteritis and circulates as a marker of disease activity."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Treg failure and remodelling: defective TGF-beta-dependent regulatory T cells permit the autoreactive vascular inflammation of giant-cell arteritis, while TGF-beta also drives the intimal fibrotic remodelling."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Adventitial ignition: TLR-mediated activation of the vascular dendritic cells guarding the adventitia breaks the immune privilege of the artery wall, the initiating event that licenses the granulomatous attack of giant-cell arteritis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Occlusive intimal hyperplasia: mTOR signalling drives the proliferation of the myofibroblasts that thicken the intima and occlude the lumen in giant-cell arteritis, the process behind the ischaemic blindness it can cause."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Immune-cell recruitment: chemokines including CXCL12 draw T cells and monocytes into the inflamed artery wall in giant-cell arteritis, building the transmural infiltrate that defines the granulomatous vasculitis."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Sight-saving therapy: high-dose glucocorticoids acting through the glucocorticoid receptor are started urgently in giant-cell arteritis to prevent the irreversible blindness of ophthalmic-artery occlusion, with tocilizumab now allowing steroid sparing."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Vascular remodelling: angiopoietin- and VEGF-driven neovascularisation of the inflamed arterial wall feeds the intimal hyperplasia that narrows the lumen in giant-cell arteritis, the occlusive remodelling behind the ischaemic complications."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Antiplatelet prevention: low-dose aspirin, by shifting the platelet thromboxane-prostacyclin balance, is used in giant-cell arteritis to reduce the cranial-ischaemic events — visual loss and stroke — that complicate the occlusive vasculitis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammatory hub: NF-κB is the central transcription factor downstream of TLR4 and IL-1β (both mapped) that drives the cytokine output of the inflamed arterial wall in giant-cell arteritis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Failed regulation: IL-10 from regulatory T cells normally counters the Th1/Th17 response, and its relative insufficiency permits the sustained vascular inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Intimal hyperplasia: PDGF-driven (PDGF mapped) ERK signalling promotes the myointimal proliferation that narrows the affected artery, producing the ischaemic vision loss and stroke of giant-cell arteritis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Dendritic-cell initiation: vascular dendritic cells activated through TLR-MyD88-NF-κB signalling (TLR4 and NF-κB already mapped) initiate the adventitial immune response of giant-cell arteritis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint failure: a deficient PD-1/PD-L1 checkpoint in the arterial wall fails to restrain the vasculitogenic T-cell response, a mechanism permitting the persistent inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic injury: CD8 cytotoxic T cells and NK cells contribute perforin-mediated injury to the inflamed arterial wall in giant-cell arteritis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ signalling through STAT1 (IFN-γ mapped) drives the macrophage and Th1 activation central to the granulomatous vascular inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) sustains the pathogenic T-cell responses and vascular-smooth-muscle proliferation of giant-cell arteritis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the macrophage-driven vascular inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) drives the intimal hyperplasia and vascular remodelling that occlude the arteries in giant-cell arteritis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory activation of the arterial wall in giant-cell arteritis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-AKT signalling (AKT already mapped) supports the T-cell and macrophage activation that drives the granulomatous inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the T-cell and vascular smooth-muscle oxidative-stress responses relevant to the arterial inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven vascular smooth-muscle and myofibroblast proliferation contributes to the intimal hyperplasia and luminal occlusion of giant-cell arteritis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the T-cell activation and Notch signaling (Notch already mapped) that drive the vascular inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the T-cell and dendritic-cell receptors amplifies the vascular-wall inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the T-cell activation state driving giant-cell arteritis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the dendritic-cell and T-cell responses that drive the granulomatous vascular inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the arterial wall contributes to the granulomatous inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive T-cell responses of giant-cell arteritis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation driving the vascular inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the vascular inflammation and immune activation of giant-cell arteritis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the vascular inflammation of giant-cell arteritis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling provides immunoregulatory modulation of the T-cell responses of giant-cell arteritis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the vascular-inflammatory immune gene programs of giant cell arteritis."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the macrophage and giant-cell activation of the vascular inflammation of giant cell arteritis."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon signaling participates in the immune dysregulation of giant cell arteritis."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "T-cell costimulation: giant cell arteritis is a CD4 T-cell-driven disease, and CTLA-4-Ig (abatacept), which blocks the costimulation that activates those T cells, has shown benefit in trials, supporting the central role of T-cell activation."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Large-vessel and cardiac involvement: giant cell arteritis extends to the aorta and its branches, and the resulting aortitis, aneurysm or coronary involvement can injure the heart, with troponin elevation marking such ischaemic damage."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia of inflammation: the sustained IL-6-driven inflammation of giant cell arteritis suppresses erythropoiesis, and a normocytic anaemia with a very high ESR is a common laboratory clue to the diagnosis."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: inflammation of the arterial wall in giant cell arteritis impairs nitric oxide signalling and, with endothelin-1 (already mapped), disturbs the vascular tone and endothelial function that contribute to the ischaemic complications."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell activation: IL-2 drives the clonal expansion of the CD4 T cells (MHC class II and CTLA-4 already mapped) that infiltrate the arterial wall in giant cell arteritis, sustaining the Th1 and Th17 responses that direct the vasculitis."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative wall injury: reactive oxygen species generated in the granulomatous inflammation, to which xanthine oxidase contributes, damage the vascular smooth muscle and elastic lamina (collagen already mapped) of the artery in giant cell arteritis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of inflammation: the IL-6 surge (already mapped) of giant cell arteritis raises hepcidin, sequestering iron to produce the anaemia of chronic disease (haemoglobin already mapped) common at presentation."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Steroid hyperglycaemia: the prolonged high-dose glucocorticoids (glucocorticoid receptor already mapped) that treat giant cell arteritis impair insulin action, causing the steroid-induced hyperglycaemia and diabetes that burden these older patients."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Steroid dyslipidaemia: chronic glucocorticoid therapy raises cholesterol and drives an atherogenic dyslipidaemia, adding to the cardiovascular risk of the long steroid courses used in giant cell arteritis."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Steroid osteoporosis: the prolonged high-dose glucocorticoids (already mapped) that treat giant cell arteritis activate RANKL-driven osteoclasts, causing the steroid-induced osteoporosis that needs bone-protective prophylaxis (calcium and vitamin D already mapped)."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Steroid hypokalaemia: the mineralocorticoid effect of the high-dose glucocorticoids used in giant cell arteritis promotes renal potassium loss, contributing to the hypokalaemia that adds to the steroid burden in these older patients."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Counter-regulatory arm: IL-4 and the M2 anti-inflammatory response (IL-10 already mapped) counter the dominant Th1 and Th17 (IFN-γ, IL-17 and IL-23 already mapped) drive of the arterial inflammation of giant cell arteritis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 counter-regulation: IL-13, with IL-4 (already mapped), is part of the M2 counter-regulatory arm balancing the Th1 and Th17 (IFN-γ and IL-17 already mapped) drive of the arterial inflammation of giant cell arteritis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Inflammation and steroid metabolism: leptin is the adipokine of the systemic inflammation (IL-6 already mapped) and the steroid-related metabolic (insulin already mapped) disturbance of giant cell arteritis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the systemic inflammation and steroid-related metabolic disturbance of giant cell arteritis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of giant cell arteritis."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Acute inflammatory infiltrate: the neutrophils and the neutrophil-lymphocyte ratio (S100A8/9 already mapped) reflect the acute-phase systemic inflammation of giant cell arteritis."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B-cell component: the B cells contribute to the vascular inflammation and the systemic autoantibody/IL-6 (already mapped) milieu of giant cell arteritis, a rationale explored for the B-cell-directed therapy."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma-cell humoral arm: the plasma cells, downstream of the B cells (already mapped), secrete the antibodies of the humoral component of giant cell arteritis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the dominant Th1/Th17 (IFN-γ, IL-12 and IL-23 already mapped) drive of giant cell arteritis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension present in a subset of giant cell arteritis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Vascular mast cells: the mast cells are increased in the inflamed arterial wall of giant cell arteritis and contribute to the vascular remodelling and the type-2 (IgE already mapped) dimension."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell mediator: the histamine, from the vascular mast cells (already mapped), contributes to the vascular permeability and the inflammatory remodelling of the arteritis of giant cell arteritis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the oxidative-stress and micronutrient dimension of the vascular inflammation of giant cell arteritis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed vessel wall of giant cell arteritis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3 and C5aR1 already mapped) active on the inflamed arterial wall of giant cell arteritis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Nutritional immunity: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic inflammation of giant cell arteritis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3, C5aR1 and factor H already mapped) contribute to the complement-mediated injury of the inflamed arterial wall of giant cell arteritis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway of the vascular inflammation of giant cell arteritis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Vascular remodelling: periostin, a matricellular mediator, contributes to the intimal hyperplasia and the vascular-wall remodelling (with collagen and osteopontin already mapped) of giant cell arteritis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-GCA axis: TSLP, from the inflamed aortic/temporal-artery wall and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th1/Th17 (IFN-γ and IL-17 already mapped) granulomatous inflammation of giant cell arteritis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-GCA axis: bradykinin, via B1/B2 receptors on the inflamed large-vessel endothelium (already mapped) and the adventitial mast cells (already mapped), amplifies the vascular permeability, neutrophil (already mapped) recruitment, and the arteritic wall inflammation of GCA."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-GCA axis: erythropoietin, induced by the HIF-1α (already mapped) ischaemia of the inflammatory vascular occlusion of GCA, modulates macrophage (already mapped) polarisation and erythroid response to the anaemia of chronic inflammation (already mapped) in giant cell arteritis."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin-GCA axis: melatonin, via MT1/MT2 receptors on adventitial macrophages (already mapped) and large-vessel endothelium, suppresses Th1/Th17 (already mapped) arteritic inflammation, modulates GCA flare circadian rhythms, and regulates IL-6 (already mapped) secretion."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-GCA axis: testosterone, via androgen receptor signalling on adventitial macrophages and T cells (already mapped), modulates the Th1/Th17-driven (already mapped) arteritic inflammation and the female sex predominance of giant cell arteritis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Prolactin-GCA axis: prolactin, acting on macrophage (already mapped) prolactin receptors in the arteritic adventitia, amplifies the Th1/Th17-driven (already mapped) immune activation and the autoimmune neuroendocrine cross-talk of giant cell arteritis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "GCA oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the arteritic inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) T-cytotoxic (already mapped) cascade of GCA."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "GCA vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates arterial vascular tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of GCA."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "GCA serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the arteritic inflammatory tone; serotonin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "GCA iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) Th1/Th17-driven arteritic cascade of giant-cell arteritis."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "GCA sodium: high dietary sodium promotes macrophage (already mapped) activation and Th17 polarisation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the arteritic inflammatory cascade of giant-cell arteritis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "GCA magnesium: magnesium, as cofactor of immune enzymes in macrophages (already mapped), restrains NF-κB (already mapped) and TNF-α (already mapped) signalling; magnesium deficiency amplifies the Th1/Th17-driven arteritic cascade of giant-cell arteritis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "GCA copper: copper, via ceruloplasmin and SOD in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) Th1/Th17-driven arteritic cascade of giant-cell arteritis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "GCA zinc: zinc, via NF-κB (already mapped) inhibitory pathways in macrophages (already mapped), restrains Th1/Th17 polarisation; zinc deficiency amplifies IL-6 (already mapped) and TNF-α (already mapped) arteritic inflammation of giant-cell arteritis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "GCA phosphorus: phosphorus-driven ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustains the arteritic immune response; phosphorus deficiency impairs NF-κB (already mapped) resolution and amplifies IL-6 (already mapped) vascular inflammation in GCA."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "GCA chloride: chloride channels on macrophages (already mapped) and T-cytotoxic cells (already mapped) regulate arteritic immune signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) vascular inflammation of GCA."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "GCA sulfur: glutathione from sulfur amino acids in macrophages (already mapped) counters oxidative arteritic injury; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) Th1/Th17 vascular inflammation of giant-cell arteritis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "GCA nitrogen: nitric oxide from iNOS in macrophages (already mapped) regulates arterial vasodilation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) arteritic inflammation of giant-cell arteritis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "GCA carbon: carbon in nucleotides of macrophages (already mapped) and T-cytotoxic cells (already mapped) fuels arteritic inflammation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "GCA hydrogen: hydrogen via ROS from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates oxidative vascular injury; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "GCA pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses arteritic immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) vascular cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "GCA glp-1: GLP-1 from macrophages (already mapped) and giant cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) arteritis cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "GCA angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "GCA wnt-beta-catenin: WNT/β-catenin on endothelial cells (already mapped) and macrophages (already mapped) regulates tone; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "GCA fibronectin: fibronectin in endothelial cells (already mapped) and macrophages (already mapped) promotes vascular ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "GCA igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes vascular smooth-muscle repair; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "GCA activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) promotes vascular remodelling; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "GCA cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "GCA calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "GCA substance-p: substance-P from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular pain tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "GCA insulin-receptor: insulin receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates GCA metabolic axis; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "GCA aldosterone: aldosterone from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "GCA androgen-receptor: androgen receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "GCA norepinephrine: norepinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates GCA adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "GCA adrenomedullin: adrenomedullin from macrophages (already mapped) and endothelial cells (already mapped) modulates GCA vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "GCA bdnf: BDNF from macrophages (already mapped) and endothelial cells (already mapped) modulates GCA neural vascular repair; bdnf excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA."
---

# Giant Cell Arteritis

## Overview

**Giant cell arteritis (GCA)** is the **most common primary systemic vasculitis** in adults over 50 years, with a prevalence of approximately 200 per 100,000 in populations of Northern European ancestry. It is a **granulomatous, large-to-medium vessel vasculitis** predominantly affecting the extracranial branches of the carotid artery — especially the **temporal arteries** — as well as the **aorta and its primary branches** [^weyand-2014-gca-review].

GCA is a medical urgency: **permanent visual loss** occurs in 15–20% of untreated patients within days to weeks of symptom onset due to ischemic optic neuropathy. Immediate initiation of high-dose corticosteroids is mandatory before diagnostic confirmation. The FDA approval of **tocilizumab** (anti-IL-6R; GiACTA trial; May 2017) established the first biologic therapy for GCA and demonstrated the centrality of IL-6 in its pathogenesis [^stone-2017-giact].

**Key facts:**
- Age: virtually all patients >50; peak incidence 70–80 years; F:M ratio ~3:1
- Ethnicity: highest prevalence in Northern European (Scandinavian) populations; rare in East Asian populations
- **PMR overlap:** ~50% of GCA patients have concurrent polymyalgia rheumatica (PMR); 15–20% of isolated PMR patients develop GCA over time
- **Large-vessel involvement:** 20–40% of GCA patients have aortic or subclavian/axillary artery involvement detectable by PET-CT; aortic aneurysm risk 17× baseline

## Structure

### Classification and variants

| Subtype | Features |
|:--------|:---------|
| **Cranial GCA** | Temporal/superficial scalp arteries; jaw claudication; visual symptoms; most common presentation |
| **Large-vessel GCA (LV-GCA)** | Aorta, subclavian, axillary arteries; limb claudication; decreased pulses; PET-CT/MRA detectable; aortic aneurysm risk; may lack cranial symptoms |
| **Occult GCA** | FUO + elevated inflammatory markers; diagnosed incidentally on biopsy or PET-CT; no cranial/visual symptoms |
| **GCA + PMR** | ~50% overlap; PMR: symmetric proximal shoulder/pelvic girdle pain/stiffness >45 min, ESR >40; responds rapidly to lower prednisone doses (10-20 mg/day) than cranial GCA |

### Arterial anatomy preferentially targeted

GCA affects **medium and large elastic arteries** above the aortic bifurcation with a rich adventitial vasa vasorum — the hypothesized entry point for dendritic cells and T cells that initiate inflammation. Vessels commonly involved:
- **Temporal arteries** (superficial temporal branches of external carotid)
- **Posterior ciliary arteries** → ischemic optic neuropathy → blindness
- **Ophthalmic artery** → amaurosis fugax
- **Subclavian/axillary arteries** → arm claudication, subclavian steal
- **Aorta** → aneurysm (thoracic > abdominal in GCA)
- **Internal carotid spared** (no vasa vasorum in intradural segment)

## Function

### Normal temporal artery and aortic physiology disrupted in GCA

The temporal arteries supply scalp, temporalis muscle, and dura. In GCA, transmural granulomatous inflammation:
- **Narrows lumen** (intimal hyperplasia → myofibroblast proliferation) → ischemia → headache, jaw claudication, visual loss
- **Destroys media** → aneurysm formation (aortic and large vessel)
- **Activates endothelium** → VEGF → neovascularization (adventitial vessels visible on ultrasound — "halo sign")

## Pathology

### Pathogenesis: two-phase innate-adaptive model

**Phase 1 — Innate activation (adventitial gate):**
- Dendritic cells (pDCs and mDCs) resident in arterial adventitia are activated by an unidentified trigger → mature DCs express CD83, CD86
- Mature DCs produce CXCL9/CXCL10 (CXCR3 ligands) → recruit circulating CD4+ T cells to the arterial wall

**Phase 2 — Adaptive inflammation:**
- **Th1 arm (IFN-γ):** DCs → IL-12 → Th1 CD4+ T cells → IFN-γ → macrophage M1 activation → IL-1β, TNF-α, reactive oxygen species; IFN-γ correlates with vessel inflammation and visual symptoms
- **Th17 arm (IL-17A):** IL-6 + TGF-β → Th17 differentiation → IL-17A → neutrophil/macrophage amplification; IL-17A correlates with systemic constitutional symptoms
- **Macrophage effectors:** M1 macrophages fuse → **multinucleated giant cells** at intima-media junction; produce:
  - **IL-6** → systemic acute-phase response (CRP, ESR, fever, constitutional symptoms)
  - **VEGF** → adventitial neovascularization
  - **PDGF + IGF-1** → VSMC migration and proliferation → **intimal hyperplasia** → luminal occlusion → ischemia

**Skip lesions:** Segmental inflammation in temporal arteries → ~30% false-negative biopsy rate (requires ≥2 cm specimen).

### Clinical features

| Feature | Prevalence | Pathomechanism |
|:--------|:----------|:--------------|
| New headache (temporal, occipital) | ~65–70% | Temporal artery inflammation → pain |
| Jaw claudication | ~35–50% | Masseter ischemia (facial artery branch); pathognomonic for GCA |
| Scalp tenderness | ~40% | Superficial temporal and scalp artery inflammation |
| Visual symptoms (amaurosis fugax) | ~20–25% | Ophthalmic/posterior ciliary artery occlusion |
| Permanent visual loss | ~15–20% untreated | Anterior ischemic optic neuropathy (AION) |
| Constitutional (fever, fatigue, weight loss) | ~50% | IL-6/IL-1β → acute-phase response |
| PMR symptoms (shoulder/pelvic girdle stiffness) | ~50% | Proximal synovitis + periarticular inflammation |

**Visual loss is irreversible** — an ophthalmologic emergency. Start IV methylprednisolone 1 g/day × 3 days immediately when visual symptoms are present.

### Diagnostic workup

| Test | Findings | Notes |
|:-----|:---------|:------|
| ESR | >50 mm/h (often 80–120) | Elevated >95%; driven by fibrinogen (IL-1β/IL-6 dependent) |
| CRP | >10 mg/L (often >50 mg/L) | More sensitive than ESR; suppressed on tocilizumab (misleading) |
| Temporal artery biopsy (TAB) | Granulomatous transmural inflammation; giant cells; fragmentation of internal elastic lamina | ≥2 cm required; treat first to save vision |
| Ultrasound (temporal artery) | "Halo sign" — hypoechoic edema ring around lumen | Sensitivity ~75%, specificity ~83%; operator-dependent |
| PET-CT | FDG uptake in aorta/subclavian arteries | Best for large-vessel GCA; suppressed on corticosteroids within 3–4 days |
| MRA/CTA | Wall thickening and stenosis of temporal arteries + aorta | Alternative to TAB + large-vessel assessment |

### Treatment

**1. Corticosteroids (start immediately — before biopsy):**
- Cranial GCA without visual symptoms: prednisone 40–60 mg/day orally
- Visual symptoms or recent vision loss: IV methylprednisolone 1 g/day × 3 days → oral prednisone
- PMR without GCA: prednisone 15–20 mg/day
- Slow taper over 12–24 months; relapse in ~50% on taper requiring dose escalation

**2. Tocilizumab (Actemra; anti-IL-6R; Roche):** [^stone-2017-giact]
- **GiACTA Phase 3** (N=251; weekly SC tocilizumab 162 mg + 26-week prednisone taper vs. placebo + 26- or 52-week taper):
  - Weekly TCZ + 26-week taper: **56% sustained remission at week 52** (vs. 18% placebo 26-week; p<0.0001)
  - 50% of TCZ patients achieved sustained remission without any prednisone by week 52
  - TCZ significantly reduced flare rate and cumulative corticosteroid dose
- FDA approved **May 2017** for giant cell arteritis — the first FDA-approved biologic for GCA
- Dosing: SC 162 mg weekly or every 2 weeks (Q2W)
- Limitation: **CRP becomes unreliable** as disease activity biomarker on tocilizumab (IL-6 drives CRP; blocking IL-6R suppresses CRP regardless of disease activity)

**3. Aspirin (75–100 mg/day):** Reduces ischemic complications (visual loss, TIA/stroke) by ~50% in observational data; recommended as adjunct to corticosteroids in all GCA patients without contraindication.

**4. Emerging therapies:**
- **Upadacitinib** (JAK1 inhibitor; SELECT-GCA Phase 3; final results pending): targets JAK1-STAT signaling downstream of IL-6R, IL-17R, and IFN-γR; oral once-daily administration advantage
- **Secukinumab** (anti-IL-17A; Phase 2 trials): targets Th17 arm
- **Abatacept** (CTLA4-Ig; ABAACTA Phase 3): T cell co-stimulation blockade; did not meet primary endpoint in GCA (2023)
- **IL-1 blockade** (anakinra, canakinumab; Phase 2): emerging evidence for IL-1β role in vascular inflammation

## Connections

- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β, released by activated macrophages in the adventitia and media, amplifies vascular NF-κB activation and macrophage recruitment in GCA; anakinra and canakinumab (IL-1 blockers) are in Phase 2/3 investigation for GCA as steroid-sparing alternatives.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is the dominant systemic effector in GCA — drives CRP/ESR elevation, fever, and constitutional symptoms; tocilizumab (anti-IL-6R; GiACTA: 56% vs 18% sustained remission at 52 weeks; FDA May 2017) is the cornerstone biologic for GCA.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — GCA involves Th17 (IL-17A) and Th1 (IFN-γ) CD4+ T cell infiltrate in the arterial adventitia; IL-17A amplifies macrophage/neutrophil recruitment and intimal hyperplasia; secukinumab (anti-IL-17A) and upadacitinib (JAK1 inhibitor; SELECT-GCA) are under investigation.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — IFN-γ from Th1 CD4+ T cells drives macrophage activation → multinucleated giant cell formation and intimal hyperplasia in GCA; high IFN-γ in arterial tissue correlates with GCA activity and distinguishes GCA from Takayasu arteritis histologically.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — GCA is named for the multinucleated giant cells formed when IFN-γ-activated M1 macrophages fuse at the intima-media junction; these macrophages secrete IL-6, VEGF, PDGF, and IGF-1, driving the acute-phase response, neovascularization, and intimal hyperplasia.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Adventitial CD4+ T cells drive the adaptive phase of GCA: Th1 cells secrete IFN-γ (macrophage activation, giant cells) and Th17 cells secrete IL-17A (constitutional symptoms); both arms resist steroids, motivating IL-6R (tocilizumab) and JAK (upadacitinib) blockade.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Macrophage-derived PDGF and IGF-1 drive vascular smooth muscle cell migration from media to intima with myofibroblast proliferation → intimal hyperplasia → luminal occlusion → the ischemia behind headache, jaw claudication, and irreversible anterior ischemic optic neuropathy.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Giant cell arteritis and ANCA vasculitis are vasculitides contrasted by vessel caliber: GCA strikes large arteries with granulomatous giant-cell inflammation, AAV small vessels with pauci-immune necrosis — poles of the vasculitis spectrum sharing IL-6-driven inflammation.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — GCA inflammation centers on the artery wall: macrophage VEGF drives neovascularization of the normally avascular media, while intimal endothelial and myofibroblast proliferation narrows the lumen, producing the ischemic optic neuropathy and jaw claudication that define it.
- `connects-to` → **[Stroke](../stroke/README.md)** — GCA of the vertebral and carotid arteries can cause posterior-circulation (vertebrobasilar) stroke — distinct from the more common anterior ischemic optic neuropathy; prompt high-dose glucocorticoids reduce this risk, making GCA a treatable cause of stroke in the elderly.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sudden permanent blindness is the feared emergency of giant-cell arteritis: inflammatory occlusion of the posterior ciliary arteries causes anterior ischemic optic neuropathy, often after jaw claudication and amaurosis fugax; suspected GCA gets immediate high-dose steroids.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Giant-cell arteritis is a large-vessel vasculitis of the cardiovascular system: granulomatous inflammation of the aorta and its branches can cause aneurysm, dissection and arm claudication years after the cranial phase, so long-term vascular imaging surveillance is recommended.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells ignite giant-cell arteritis: resident vascular dendritic cells in the artery's adventitia activate and recruit the CD4+ T cells and macrophages that form the granulomas and giant cells, making them the proposed initiator of the arterial attack.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Giant cell arteritis and rheumatoid arthritis are both IL-6-driven autoimmune diseases of older adults that respond to tocilizumab: GCA inflames large arteries while RA destroys synovial joints—shared cytokine biology lets one biologic treat both.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 helps polarize the T-cell response in giant cell arteritis: dendritic cells in the arterial wall secrete IL-12 to push T cells toward Th1, generating IFN-γ-producing cells whose granulomatous infiltrate, with giant cells, destroys the artery's elastic lamina.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK-STAT signaling is a therapeutic target in giant cell arteritis: the IL-6 and IFN-γ driving arterial inflammation act through JAK kinases, so JAK inhibitors are in trials to spare steroids—linking GCA to the node mutated in myeloproliferative disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF helps GCA both damage and compensate: inflammatory cytokines drive VEGF that promotes neovascularization in the inflamed artery wall, while ischemia downstream stimulates collateral vessels—so angiogenesis is part of both injury and response in GCA.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Giant cell arteritis is a large-vessel disease that threatens the aorta: beyond the temporal artery, granulomatous inflammation can involve the aorta and its branches, causing thoracic aortic aneurysm and dissection years later—so GCA needs vascular surveillance.
- `connects-to` → **[Targeted therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Biologics spare the steroids: tocilizumab (anti-IL-6R) and JAK inhibitors such as upadacitinib are targeted therapies that maintain remission in giant cell arteritis, cutting the toxic glucocorticoid burden long-term GCA control once demanded.
- `connects-to` → **[Checkpoint inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy can ignite the artery: large-vessel vasculitis resembling giant cell arteritis is a recognised immune-related adverse event of checkpoint inhibitors, where releasing T-cell brakes against a tumour also unleashes inflammation in the aorta and its branches.
- `connects-to` → **[Germinal center](../../05-tissue/germinal-center/README.md)** — The inflamed artery builds its own lymphoid tissue: giant cell arteritis forms tertiary lymphoid structures with germinal-center-like T- and B-cell aggregates in the adventitia, organising the local immune attack much as a lymph node germinal center does.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Giant cell arteritis and lupus are both autoimmune but differ sharply: GCA is a granulomatous large-vessel vasculitis of the elderly driven by Th1/Th17 and IL-6, while SLE is an immune-complex multisystem disease of the young—contrasting mechanisms of autoimmunity.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Giant cell arteritis is a glucocorticoid emergency: high-dose cortisol-mimicking steroids must start immediately on suspicion to prevent irreversible blindness from ischemic optic neuropathy—treatment precedes biopsy because delay risks sudden, permanent vision loss.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Giant cell arteritis threatens the nervous system through vascular ischemia: inflamed cranial arteries cause severe headache, jaw claudication and, most feared, sudden blindness from anterior ischemic optic neuropathy, plus a raised risk of stroke.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Giant cell arteritis is an autoimmune large-vessel vasculitis: dendritic cells and IL-6-driven Th17/Th1 responses inflame the artery wall with granulomas and giant cells, so it overlaps with other autoimmunity and responds to IL-6 blockade and steroids.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Giant cell arteritis overlaps polymyalgia rheumatica: up to half of GCA patients have the proximal shoulder- and hip-girdle aching of PMR, and jaw claudication reflects muscle ischemia—so a musculoskeletal syndrome and a blinding vasculitis are two faces of one disease.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts cause the vessel-narrowing of giant cell arteritis: activated by inflammation, intimal myofibroblasts proliferate and thicken the artery wall, so the lumen occludes and downstream tissue (optic nerve, brain) is starved of blood—GCA's ischemic basis.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Giant cell arteritis reflects failed immune regulation: deficient regulatory T cells let Th1 and Th17 cells attack the arterial wall, so the imbalance between effector and regulatory T cells underlies the granulomatous inflammation that defines the disease.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Giant cell arteritis announces itself through red cells: the inflammation drives a sky-high erythrocyte sedimentation rate (ESR) and an anemia of chronic disease, so a markedly elevated ESR in an older patient with headache is a classic trigger to start steroids urgently.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Giant cell arteritis blocks arteries by laying down collagen: after inflammation chews up the elastic lamina, the wall heals with collagen-rich intimal thickening that narrows the lumen, causing the jaw claudication and sudden vision loss that make it an emergency.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Giant cell arteritis builds granulomas with TNF: this cytokine helps fuse macrophages into the multinucleated giant cells that define the lesion, part of the Th1/Th17 inflammatory storm attacking the artery wall.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Giant cell arteritis blinds by cutting off oxygen: inflammation narrows the arteries feeding the optic nerve, and the resulting ischemia (arteritic AION) can cause sudden, permanent vision loss—why suspected GCA is a steroid emergency.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Giant cell arteritis can starve the brain: when the inflamed large arteries supplying the head narrow or clot, patients suffer TIAs and strokes, so cranial and vertebral artery involvement makes prompt treatment urgent.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF drives the artery-closing overgrowth in giant cell arteritis: it pushes smooth muscle cells to migrate and proliferate into the intima, thickening the wall until the lumen narrows—the structural step from inflammation to ischemia.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Giant cell arteritis drives down iron use: its intense systemic inflammation suppresses red-cell production and locks iron away, causing the anemia of chronic disease that, with a sky-high ESR, supports the diagnosis.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Giant cell arteritis can show on the scalp: the inflamed scalp arteries make it tender and, when severely blocked, can cause scalp or tongue necrosis—dramatic signs of the vasculitis starving surface tissues.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Giant cell arteritis heals into fibrosis: the inflamed artery wall thickens its inner layer with fibrous tissue, narrowing the lumen, so scarring—not just acute swelling—drives the lasting blockage and ischemia.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — GCA is found by imaging and biopsy: ultrasound shows the artery-wall 'halo,' PET lights up large-vessel inflammation, and the temporal-artery biopsy reveals giant cells under the microscope.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — GCA can starve the nerves: ischemia from vasculitis of the vasa nervorum causes peripheral neuropathy and mononeuritis, beyond the optic-nerve infarction that threatens sight.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — GCA's treatment threatens bone: the prolonged high-dose steroids needed to prevent blindness leach calcium and cause osteoporosis, a major long-term harm of controlling the disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows GCA chewing through the artery wall: multinucleated giant cells gather along the fragmented internal elastic lamina they are destroying, the granulomatous lesion that names the disease.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — GCA can starve the gut: when the large-vessel inflammation reaches the mesenteric arteries, it threatens bowel ischemia, a rare but grave extension of a disease usually thought of as confined to the head.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — GCA occasionally speaks through the lungs: a dry cough or other respiratory symptoms can be the unexpected presenting complaint, the vasculitis reaching the airways and pulmonary vessels.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — An antibody spares the steroids: tocilizumab, a monoclonal antibody against the IL-6 receptor, is the key steroid-sparing treatment for GCA, calming the IL-6-driven inflammation that powers the arteritis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — GCA's most feared blow is sudden blindness: inflammation of the arteries feeding the optic nerve causes anterior ischemic optic neuropathy, an emergency that demands immediate steroids to save the second eye.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Months of high-dose steroids suppress the adrenals: the prolonged prednisone needed to control GCA shuts down the body's own cortisol production, so the dose must be tapered slowly to avoid an adrenal crisis.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets both flag and threaten in GCA: a raised platelet count is a useful diagnostic clue alongside the inflammatory markers, and because the inflamed artery clots, low-dose aspirin is often added to guard against the dreaded vision loss and stroke.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — The treatment thins the bones: the months to years of high-dose glucocorticoids that control GCA are a leading cause of steroid-induced osteoporosis, so calcium, vitamin D and a bone-protecting drug are started alongside the prednisone.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — A viral trigger has been proposed: varicella-zoster virus antigen was reported in some inflamed temporal arteries, raising the idea that the reactivated virus helps ignite GCA — a link that remains debated and unproven.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the Th17 arm of the attack: alongside the IL-12/Th1 axis, IL-23 drives the IL-17-producing T cells that inflame the artery wall in GCA, part of why cytokine-directed therapy is explored beyond IL-6 blockade.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells join the vascular infiltrate: they accumulate in the inflamed arterial wall and contribute, with T cells and macrophages, to the granulomatous destruction of the vessel.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — The cure brings its own disease: the prolonged high-dose glucocorticoids needed to control GCA commonly induce steroid diabetes, one of the metabolic harms that make sparing the steroid a goal of newer therapy.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT carries the vascular inflammation: IL-6 and interferon-γ signal through JAK1/2 to sustain the arterial-wall attack in GCA, the rationale behind the JAK inhibitors (upadacitinib) now trialed as steroid-sparing therapy.
- `connects-to` → **[Chronic Myelomonocytic Leukemia](../cmml/README.md)** — Large-vessel vasculitis can flag a myeloid clone: GCA and other vasculitides are over-represented in CMML and the VEXAS spectrum, where a somatic marrow mutation drives systemic inflammation alongside the cytopenias.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The aorta is in the firing line: GCA aortitis can cause aortic aneurysm and regurgitation that overload the left ventricle into heart failure, why large-vessel imaging follow-up is part of long-term care.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 drives the arteritis through STAT3: the hallmark IL-6 of GCA signals via JAK-STAT3 to sustain the Th17 and macrophage response in the vessel wall, the axis that the IL-6 blocker tocilizumab interrupts.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Systemic inflammation raises the clot risk: the intense acute-phase response of GCA, plus the high-dose corticosteroids used to treat it, increase the risk of venous thromboembolism.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Long steroid courses invite infection: GCA demands prolonged high-dose glucocorticoids, often in older patients, leaving them prone to serious infection and sepsis — a leading cause of treatment-related death.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Its inflammation blunts the marrow: GCA's intense IL-6-driven acute-phase response raises hepcidin and suppresses erythropoiesis, so a normocytic anemia of chronic disease is a common and supportive diagnostic clue.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Prolonged high-dose steroids open the lung: the months of glucocorticoids that control GCA deplete T-cell defenses, raising Pneumocystis pneumonia risk enough that prophylaxis is considered in higher-dose regimens.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Steroids and vision loss weigh on mood: the high-dose glucocorticoids for GCA cause mood disturbance and depression, compounded by the fear and disability of the irreversible blindness the disease can cause.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its high-dose steroids open the lung to mold: the prolonged glucocorticoids needed to control giant-cell arteritis deeply suppress immunity, occasionally permitting invasive aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Arterial occlusion and steroids starve tissue: severe giant-cell arteritis can cause ischemic scalp and tongue necrosis, and its chronic steroids thin skin and slow the healing of the resulting wounds.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Steroids and the threat of blindness breed worry: the psychiatric effects of high-dose glucocorticoids and the fear of sudden irreversible vision loss in GCA foster anxiety alongside depression.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Months of high-dose steroids reshape metabolism: the prolonged glucocorticoids that control GCA cause steroid-induced diabetes, adrenal suppression and a Cushingoid state, the endocrine cost of treatment.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Steroids and IL-6 blockade trouble the gut: high-dose steroids for GCA raise peptic-ulcer risk, the tocilizumab used to spare them carries a risk of lower-GI perforation, and jaw claudication makes eating painful.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its long steroid courses thin the skin: prolonged glucocorticoids for GCA cause skin atrophy, easy bruising and striae, on top of the thickened, tender temporal artery palpable on examination.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can present as a new cough: a persistent dry cough is an under-recognised symptom of giant cell arteritis, reflecting large-vessel and aortic involvement of the disease.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It spares the kidney, unlike small-vessel vasculitis: GCA characteristically leaves the kidneys untouched — a key feature distinguishing it from ANCA-associated vasculitis — though large-vessel disease can rarely involve the renal arteries.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It can masquerade as occult disease: large-vessel GCA presents as fever of unknown origin with intense systemic inflammation that mimics lymphoma, distinguished by PET showing vasculitic aortic uptake rather than nodal disease.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — High-dose steroids are the emergency treatment: prompt glucocorticoids prevent the irreversible blindness of giant cell arteritis, then taper over many months despite their cumulative toxicity.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Low-dose aspirin guards the circulation: it is often added in giant cell arteritis to reduce the risk of the ischaemic visual loss and strokes the vasculitis can cause.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Long steroids demand bone protection: patients on prolonged glucocorticoids for giant cell arteritis take vitamin D and calcium, often with a bisphosphonate, to counter steroid-induced osteoporosis.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It inflames the artery wall itself: giant cell arteritis is a granulomatous vasculitis of the media and adventitia of medium and large arteries, where T cells and macrophage-derived giant cells destroy the elastic lamina.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — A steroid-sparing immunosuppressant: methotrexate, a low-dose chemotherapy agent, is used to reduce glucocorticoid exposure in giant cell arteritis alongside IL-6 blockade.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Two ways to thicken an artery: giant cell arteritis must be distinguished from atherosclerosis on vascular imaging, and the chronic vascular inflammation it causes also accelerates atherosclerotic disease.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Coronary and aortic involvement: giant-cell arteritis inflames large arteries including the aorta and coronaries, causing aortitis with aneurysm and, rarely, myocardial ischaemia.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Steroids thin the bone: the prolonged high-dose glucocorticoids needed to control GCA cause osteoporosis and fracture, a major iatrogenic harm driving steroid-sparing tocilizumab use.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — The sky-high ESR: acute-phase fibrinogen produced in the inflammation of GCA drives the markedly raised ESR and CRP that are central to its diagnosis and monitoring.
- `connects-to` → **[MDS](../mds/README.md)** — Clonal inflammation in older men: VEXAS syndrome and other clonal myeloid diseases (MDS) can present with a giant-cell-arteritis-like large-vessel vasculitis, blurring autoinflammation and myeloid neoplasia.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — A debated trigger and a treatment risk: varicella-zoster virus has been controversially implicated in giant-cell arteritis, and the steroid/IL-6 immunosuppression that treats it reactivates VZV as shingles.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Shared IL-6 biology: COVID-19 and giant-cell arteritis both feature IL-6-driven inflammation (both treated with tocilizumab), and de novo GCA and flares have been reported after infection or vaccination.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Ischaemia from vasoconstriction: endothelin-1 released by the inflamed vessel wall drives the vasoconstriction underlying the ischaemic blindness and jaw claudication of giant-cell arteritis.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Notch-driven vasculitis: Notch signalling activates the pathogenic Th1 and Th17 vascular T cells and promotes the vessel-wall remodelling central to giant-cell arteritis.
- `connects-to` → **[T Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8 T-cell infiltrate: cytotoxic and tissue-resident memory CD8 T cells populate the inflamed arterial wall in giant-cell arteritis, contributing to vessel damage and relapse.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Innate vasculitis: NLRP3-inflammasome activation in vessel-wall macrophages matures the IL-1β that amplifies the granulomatous inflammation of giant-cell arteritis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes into the arterial wall in giant-cell arteritis, where they fuse into the multinucleated giant cells that name the disease.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Ischaemic wall: the inflamed, thickened artery in giant-cell arteritis becomes hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis of neovascularisation in the vessel wall.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Genetic risk and presentation: the strong HLA-DRB1 association of giant-cell arteritis points to MHC class II presentation of arterial-wall antigens to the CD4 T cells that orchestrate the granulomatous attack.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Myeloid alarmin: S100A8/A9 from the monocytes and neutrophils infiltrating the temporal artery amplifies inflammation in giant-cell arteritis and circulates as a marker of disease activity.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Treg failure and remodelling: defective TGF-beta-dependent regulatory T cells permit the autoreactive vascular inflammation of giant-cell arteritis, while TGF-beta also drives the intimal fibrotic remodelling.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR-mediated activation of the vascular dendritic cells guarding the adventitia breaks the immune privilege of the artery wall, the initiating event that licenses the granulomatous attack of giant-cell arteritis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling drives the proliferation of the myofibroblasts that thicken the intima and occlude the lumen in giant-cell arteritis, the remodeling process behind the irreversible ischemic blindness the disease can cause.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — Chemokines including CXCL12 draw T cells and monocytes into the inflamed artery wall in giant-cell arteritis, building the transmural infiltrate of CD4 T cells, macrophages, and giant cells that defines the vasculitis.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — High-dose glucocorticoids acting through the glucocorticoid receptor are started urgently in giant-cell arteritis to prevent the irreversible blindness of ophthalmic-artery occlusion, with tocilizumab now allowing steroid sparing.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Angiopoietin- and VEGF-driven neovascularization of the inflamed arterial wall feeds the intimal hyperplasia that narrows the lumen in giant-cell arteritis, the occlusive remodeling behind the ischemic complications.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Low-dose aspirin, by shifting the platelet thromboxane-prostacyclin balance, is used in giant-cell arteritis to reduce the cranial-ischemic events—visual loss and stroke—that complicate the occlusive vasculitis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is the central transcription factor downstream of TLR4 and IL-1β (both mapped) that drives the cytokine output of the inflamed arterial wall in giant-cell arteritis.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10 from regulatory T cells normally counters the Th1/Th17 response, and its relative insufficiency permits the sustained vascular inflammation of giant-cell arteritis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — PDGF-driven (PDGF mapped) ERK signaling promotes the myointimal proliferation that narrows the affected artery, producing the ischemic vision loss and stroke of giant-cell arteritis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Vascular dendritic cells activated through TLR-MyD88-NF-κB signaling (TLR4 and NF-κB already mapped) initiate the adventitial immune response of giant-cell arteritis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — A deficient PD-1/PD-L1 checkpoint in the arterial wall fails to restrain the vasculitogenic T-cell response, a mechanism permitting the persistent inflammation of giant-cell arteritis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD8 cytotoxic T cells and NK cells contribute perforin-mediated injury to the inflamed arterial wall in giant-cell arteritis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ signaling through STAT1 (IFN-γ mapped) drives the macrophage and Th1 activation central to the granulomatous vascular inflammation of giant-cell arteritis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) sustains the pathogenic T-cell responses and vascular-smooth-muscle proliferation of giant-cell arteritis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the macrophage-driven vascular inflammation of giant-cell arteritis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) drives the intimal hyperplasia and vascular remodeling that occlude the arteries in giant-cell arteritis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the innate inflammatory activation of the arterial wall in giant-cell arteritis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT signaling (AKT already mapped) supports the T-cell and macrophage activation that drives the granulomatous inflammation of giant-cell arteritis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the T-cell and vascular smooth-muscle oxidative-stress responses relevant to the arterial inflammation of giant-cell arteritis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven vascular smooth-muscle and myofibroblast proliferation contributes to the intimal hyperplasia and luminal occlusion of giant-cell arteritis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the T-cell activation and Notch signaling (Notch already mapped) that drive the vascular inflammation of giant-cell arteritis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the T-cell and dendritic-cell receptors amplifies the vascular-wall inflammation of giant-cell arteritis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the T-cell activation state driving giant-cell arteritis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the dendritic-cell and T-cell responses that drive the granulomatous vascular inflammation of giant-cell arteritis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the arterial wall contributes to the granulomatous inflammation of giant-cell arteritis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive T-cell responses of giant-cell arteritis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation driving the vascular inflammation of giant-cell arteritis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the vascular inflammation and immune activation of giant-cell arteritis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the vascular inflammation of giant-cell arteritis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling provides immunoregulatory modulation of the T-cell responses of giant-cell arteritis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the vascular-inflammatory immune gene programs of giant cell arteritis.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the macrophage and giant-cell activation of the vascular inflammation of giant cell arteritis.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon signaling participates in the immune dysregulation of giant cell arteritis.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — T-cell costimulation: giant cell arteritis is a CD4 T-cell-driven disease, and CTLA-4-Ig (abatacept), which blocks the costimulation that activates those T cells, has shown benefit in trials, supporting the central role of T-cell activation.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Large-vessel and cardiac involvement: giant cell arteritis extends to the aorta and its branches, and the resulting aortitis, aneurysm or coronary involvement can injure the heart, with troponin elevation marking such ischaemic damage.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia of inflammation: the sustained IL-6-driven inflammation of giant cell arteritis suppresses erythropoiesis, and a normocytic anaemia with a very high ESR is a common laboratory clue to the diagnosis.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial dysfunction: inflammation of the arterial wall in giant cell arteritis impairs nitric oxide signalling and, with endothelin-1 (already mapped), disturbs the vascular tone and endothelial function that contribute to the ischaemic complications.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell activation: IL-2 drives the clonal expansion of the CD4 T cells (MHC class II and CTLA-4 already mapped) that infiltrate the arterial wall in giant cell arteritis, sustaining the Th1 and Th17 responses that direct the vasculitis.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative wall injury: reactive oxygen species generated in the granulomatous inflammation, to which xanthine oxidase contributes, damage the vascular smooth muscle and elastic lamina (collagen already mapped) of the artery in giant cell arteritis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of inflammation: the IL-6 surge (already mapped) of giant cell arteritis raises hepcidin, sequestering iron to produce the anaemia of chronic disease (haemoglobin already mapped) common at presentation.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Steroid hyperglycaemia: the prolonged high-dose glucocorticoids (glucocorticoid receptor already mapped) that treat giant cell arteritis impair insulin action, causing the steroid-induced hyperglycaemia and diabetes that burden these older patients.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Steroid dyslipidaemia: chronic glucocorticoid therapy raises cholesterol and drives an atherogenic dyslipidaemia, adding to the cardiovascular risk of the long steroid courses used in giant cell arteritis.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Steroid osteoporosis: the prolonged high-dose glucocorticoids (already mapped) that treat giant cell arteritis activate RANKL-driven osteoclasts, causing the steroid-induced osteoporosis that needs bone-protective prophylaxis (calcium and vitamin D already mapped).
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Steroid hypokalaemia: the mineralocorticoid effect of the high-dose glucocorticoids used in giant cell arteritis promotes renal potassium loss, contributing to the hypokalaemia that adds to the steroid burden in these older patients.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Counter-regulatory arm: IL-4 and the M2 anti-inflammatory response (IL-10 already mapped) counter the dominant Th1 and Th17 (IFN-γ, IL-17 and IL-23 already mapped) drive of the arterial inflammation of giant cell arteritis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 counter-regulation: IL-13, with IL-4 (already mapped), is part of the M2 counter-regulatory arm balancing the Th1 and Th17 (IFN-γ and IL-17 already mapped) drive of the arterial inflammation of giant cell arteritis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Inflammation and steroid metabolism: leptin is the adipokine of the systemic inflammation (IL-6 already mapped) and the steroid-related metabolic (insulin already mapped) disturbance of giant cell arteritis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the systemic inflammation and steroid-related metabolic disturbance of giant cell arteritis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the systemic inflammation (IL-6 already mapped) of giant cell arteritis.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Acute inflammatory infiltrate: the neutrophils and the neutrophil-lymphocyte ratio (S100A8/9 already mapped) reflect the acute-phase systemic inflammation of giant cell arteritis.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — B-cell component: the B cells contribute to the vascular inflammation and the systemic autoantibody/IL-6 (already mapped) milieu of giant cell arteritis, a rationale explored for the B-cell-directed therapy.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Plasma-cell humoral arm: the plasma cells, downstream of the B cells (already mapped), secrete the antibodies of the humoral component of giant cell arteritis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the dominant Th1/Th17 (IFN-γ, IL-12 and IL-23 already mapped) drive of giant cell arteritis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension present in a subset of giant cell arteritis.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Vascular mast cells: the mast cells are increased in the inflamed arterial wall of giant cell arteritis and contribute to the vascular remodelling and the type-2 (IgE already mapped) dimension.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell mediator: the histamine, from the vascular mast cells (already mapped), contributes to the vascular permeability and the inflammatory remodelling of the arteritis of giant cell arteritis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein cofactor, is part of the oxidative-stress and micronutrient dimension of the vascular inflammation of giant cell arteritis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed vessel wall of giant cell arteritis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3 and C5aR1 already mapped) active on the inflamed arterial wall of giant cell arteritis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Nutritional immunity: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic inflammation of giant cell arteritis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3, C5aR1 and factor H already mapped) contribute to the complement-mediated injury of the inflamed arterial wall of giant cell arteritis.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway of the vascular inflammation of giant cell arteritis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Vascular remodelling: periostin, a matricellular mediator, contributes to the intimal hyperplasia and the vascular-wall remodelling (with collagen and osteopontin already mapped) of giant cell arteritis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-GCA axis: TSLP, from the inflamed aortic/temporal-artery wall and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th1/Th17 (IFN-γ and IL-17 already mapped) granulomatous inflammation of giant cell arteritis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-GCA axis: bradykinin, via B1/B2 receptors on the inflamed large-vessel endothelium (already mapped) and the adventitial mast cells (already mapped), amplifies the vascular permeability, neutrophil (already mapped) recruitment, and the arteritic wall inflammation of GCA.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-GCA axis: erythropoietin, induced by the HIF-1α (already mapped) ischaemia of the inflammatory vascular occlusion of GCA, modulates macrophage (already mapped) polarisation and erythroid response to the anaemia of chronic inflammation (already mapped) in giant cell arteritis.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin-GCA axis: melatonin, via MT1/MT2 receptors on adventitial macrophages (already mapped) and large-vessel endothelium, suppresses Th1/Th17 (already mapped) arteritic inflammation, modulates GCA flare circadian rhythms, and regulates IL-6 (already mapped) secretion.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-GCA axis: testosterone, via androgen receptor signalling on adventitial macrophages and T cells (already mapped), modulates the Th1/Th17-driven (already mapped) arteritic inflammation and the female sex predominance of giant cell arteritis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Prolactin-GCA axis: prolactin, acting on macrophage (already mapped) prolactin receptors in the arteritic adventitia, amplifies the Th1/Th17-driven (already mapped) immune activation and the autoimmune neuroendocrine cross-talk of giant cell arteritis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — GCA oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates the arteritic inflammatory cascade; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) T-cytotoxic (already mapped) cascade of GCA.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — GCA vasopressin: vasopressin, via V1aR on macrophages (already mapped) and mast cells (already mapped), modulates arterial vascular tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and IL-6 (already mapped) T-cytotoxic (already mapped) cascade of GCA.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — GCA serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the arteritic inflammatory tone; serotonin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — GCA iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) polarisation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) Th1/Th17-driven arteritic cascade of giant-cell arteritis.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — GCA sodium: high dietary sodium promotes macrophage (already mapped) activation and Th17 polarisation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the arteritic inflammatory cascade of giant-cell arteritis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — GCA magnesium: magnesium, as cofactor of immune enzymes in macrophages (already mapped), restrains NF-κB (already mapped) and TNF-α (already mapped) signalling; magnesium deficiency amplifies the Th1/Th17-driven arteritic cascade of giant-cell arteritis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — GCA copper: copper, via ceruloplasmin and SOD in macrophages (already mapped) and T-cytotoxic cells (already mapped), scavenges ROS; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) Th1/Th17-driven arteritic cascade of giant-cell arteritis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — GCA zinc: zinc, via NF-κB (already mapped) inhibitory pathways in macrophages (already mapped), restrains Th1/Th17 polarisation; zinc deficiency amplifies IL-6 (already mapped) and TNF-α (already mapped) arteritic inflammation of giant-cell arteritis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — GCA phosphorus: phosphorus-driven ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustains the arteritic immune response; phosphorus deficiency impairs NF-κB (already mapped) resolution and amplifies IL-6 (already mapped) vascular inflammation in GCA.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — GCA chloride: chloride channels on macrophages (already mapped) and T-cytotoxic cells (already mapped) regulate arteritic immune signalling; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) vascular inflammation of GCA.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — GCA sulfur: glutathione from sulfur amino acids in macrophages (already mapped) counters oxidative arteritic injury; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) Th1/Th17 vascular inflammation of giant-cell arteritis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — GCA nitrogen: nitric oxide from iNOS in macrophages (already mapped) regulates arterial vasodilation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) arteritic inflammation of giant-cell arteritis.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — GCA carbon: carbon in nucleotides of macrophages (already mapped) and T-cytotoxic cells (already mapped) fuels arteritic inflammation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — GCA hydrogen: hydrogen via ROS from macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates oxidative vascular injury; hydrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — GCA pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses arteritic immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) vascular cascade of giant-cell arteritis.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — GCA glp-1: GLP-1 from macrophages (already mapped) and giant cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) arteritis cascade of giant-cell arteritis.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — GCA angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — GCA wnt-beta-catenin: WNT/β-catenin on endothelial cells (already mapped) and macrophages (already mapped) regulates tone; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — GCA fibronectin: fibronectin in endothelial cells (already mapped) and macrophages (already mapped) promotes vascular ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — GCA igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes vascular smooth-muscle repair; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — GCA activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) promotes vascular remodelling; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — GCA cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular neuroimmune tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — GCA calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — GCA substance-p: substance-P from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular pain tone; substance-P excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of giant-cell arteritis.
- `connects-to` → **[Insulin-Receptor](../../03-molecular/insulin-receptor/README.md)** — GCA insulin-receptor: insulin receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates GCA metabolic axis; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — GCA aldosterone: aldosterone from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular fluid balance; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA.
- `connects-to` → **[Androgen-Receptor](../../03-molecular/androgen-receptor/README.md)** — GCA androgen-receptor: androgen receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates androgen axis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — GCA norepinephrine: norepinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates GCA adrenergic tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — GCA adrenomedullin: adrenomedullin from macrophages (already mapped) and endothelial cells (already mapped) modulates GCA vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — GCA bdnf: BDNF from macrophages (already mapped) and endothelial cells (already mapped) modulates GCA neural vascular repair; bdnf excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of GCA.

[^stone-2017-giact]: Stone JH, Tuckwell K, Dimonaco S, et al. Trial of tocilizumab in giant-cell arteritis. *N Engl J Med.* 2017;377(4):317-328. [doi:10.1056/NEJMoa1613849](https://doi.org/10.1056/NEJMoa1613849) · [PubMed 28745999](https://pubmed.ncbi.nlm.nih.gov/28745999/)
[^weyand-2014-gca-review]: Weyand CM, Goronzy JJ. Clinical practice. Giant-cell arteritis and polymyalgia rheumatica. *N Engl J Med.* 2014;371(1):50-57. [doi:10.1056/NEJMcp1214926](https://doi.org/10.1056/NEJMcp1214926) · [PubMed 24988557](https://pubmed.ncbi.nlm.nih.gov/24988557/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
