---
schema: human-scale-entry/v1
id: uveal-melanoma
name: Uveal Melanoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Uveal melanoma is the most common primary intraocular malignancy; GNAQ/GNA11 ~85%, BAP1 ~45%, SF3B1 R625 ~15-20%, EIF1AX ~15%; Class 2 (BAP1 loss) has 25-35% 5-year metastasis-free survival; tebentafusp (gp100×CD3) is FDA-approved for HLA-A*02:01+ metastatic disease."
aliases: ["uveal melanoma", "choroidal melanoma", "iris melanoma", "ciliary body melanoma", "intraocular melanoma", "ocular melanoma", "GNAQ melanoma"]
sources:
  - id: nathan-2021-tebentafusp
    type: peer-reviewed
    cite: "Nathan P, Hassel JC, Rutkowski P, et al. Overall survival benefit with tebentafusp in metastatic uveal melanoma. N Engl J Med. 2021;385(13):1196-1206."
    doi: "10.1056/NEJMoa2103485"
    pmid: "34551229"
    url: "https://doi.org/10.1056/NEJMoa2103485"
  - id: harbour-2010-bap1-uveal
    type: peer-reviewed
    cite: "Harbour JW, Onken MD, Roberson ED, et al. Frequent mutation of BAP1 in metastasizing uveal melanomas. Science. 2010;330(6009):1410-1413."
    doi: "10.1126/science.1194472"
    pmid: "21051595"
    url: "https://doi.org/10.1126/science.1194472"
cross_links:
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "SF3B1 R625C/H occurs in ~15-20% uveal melanoma → cryptic 3' SS activation → Class 1B (intermediate prognosis, late relapses); SF3B1-mutant uveal melanoma has a distinct transcriptome from BAP1-loss Class 2; H3B-8800 may exploit this vulnerability."
  - target: 01-human/03-molecular/bap1
    relation: connects-to
    note: "BAP1 biallelic loss → Class 2 uveal melanoma (~45%; high metastatic risk, early liver relapse); BAP1 IHC nuclear loss is the primary prognostic marker; BAP1-TPDS germline → uveal melanoma lifetime risk ~30-45%; EZH2 inhibition studied in BAP1-null disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss occurs in ~15-20% of metastatic uveal melanoma; PI3K-AKT-mTOR activation drives progression; PI3K/mTOR + MEK inhibitor combinations overcome GNAQ-driven resistance in preclinical uveal melanoma models; everolimus studied in metastatic disease."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1/PD-L1 checkpoint inhibitors have very low activity in uveal melanoma (ORR <5%) due to low tumor mutational burden and immunosuppressive tumor microenvironment; tebentafusp bypasses checkpoint resistance by directly recruiting T cells via gp100-TCR×CD3 bispecific mechanism."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Uveal melanoma is biologically distinct from cutaneous melanoma: GNAQ/GNA11 (not BRAF V600E) → MEK inhibitors only partial activity; very low TMB vs UV-mutational burden; ICB ORR <5% in uveal vs 30-60% in cutaneous; liver-dominant metastasis vs lung/brain tropism."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "GNAQ/GNA11 → PLCβ → PKC → Rho → YAP/TAZ nuclear entry (Hippo-independent); YAP/TAZ drive CTGF, CYR61, BIRC5 → uveal melanoma proliferation and survival; verteporfin (YAP inhibitor) active in preclinical uveal models; YAP-TEAD inhibitors (IAG933, VT3989) in Phase 1/2 trials."
  - target: 01-human/03-molecular/braf
    relation: connects-to
    note: "BRAF V600E absent in uveal melanoma (0%); GNAQ/GNA11 → PLCβ/PKC → MEK (RAS-independent) → BRAF inhibitors ineffective; MEK inhibitors (selumetinib): ORR ~15% (SUMIT trial) but no OS benefit; MEK + PKC combinations overcome adaptive resistance in preclinical uveal melanoma models."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Uveal melanoma is the commonest primary intraocular cancer in adults, from melanocytes of the uveal tract — choroid (~90%), ciliary body, or iris; it presents with painless vision change or floaters, and globe-sparing brachytherapy or proton therapy has replaced most enucleation."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is uveal melanoma's near-exclusive metastatic target: ~90% of metastases home there (the eye lacks lymphatics), often years after the eye is treated — so lifelong liver surveillance is essential, and liver-directed therapy plus tebentafusp are mainstays."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Uveal melanoma resists checkpoint inhibitors (ORR <5%, low mutational burden), so it engages cytotoxic T cells differently: tebentafusp, a gp100-HLA × CD3 bispecific, tethers CD8+ T cells to HLA-A*02:01 tumor cells — the first drug to improve survival in metastatic disease."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Uveal melanoma and mesothelioma both define the BAP1 tumor predisposition syndrome: germline BAP1 loss raises risk of both, plus renal cell carcinoma and skin tumors, and BAP1 loss in a uveal melanoma marks the high-risk class with the worst metastatic prognosis."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "Uveal melanoma and NF2 converge on the Hippo pathway: NF2's Merlin restrains YAP, while uveal melanoma's GNAQ/GNA11 mutations activate YAP through Hippo—so both illustrate how unleashed YAP/TEAD drives growth, here in the pigmented cells of the eye."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is the eye-sparing mainstay for uveal melanoma: plaque brachytherapy and proton or photon beams deliver tumoricidal radiation to the choroidal tumor while preserving the globe—an alternative to enucleation, though metastatic risk depends on genetics."
  - target: 01-human/07-system/retinoblastoma
    relation: connects-to
    note: "Uveal melanoma and retinoblastoma are the two principal intraocular malignancies: retinoblastoma is a childhood RB1-driven retinal tumor, while uveal melanoma is an adult melanocytic tumor of the choroid driven by GNAQ/GNA11 and BAP1—both threaten the eye and vision."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Uveal melanoma and cholangiocarcinoma both belong to the BAP1 syndrome: germline BAP1 loss raises risk of both, and in uveal melanoma somatic BAP1 loss marks the liver-metastasizing tumors—linking an eye cancer to a bile-duct cancer through one chromatin gene."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Uveal melanoma and clear-cell renal cell carcinoma are joined by the BAP1 syndrome: BAP1 loss drives aggressive forms of both, so germline-mutation families are surveilled for eye, kidney, mesothelioma and skin tumors—BAP1 a shared deubiquitinase tumor suppressor."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven angiogenesis and a leaky vasculature mark uveal melanoma: the tumor secretes VEGF to vascularize the eye and prepare its spread, high levels predict metastasis, and anti-VEGF agents are explored alongside the liver-directed therapy this cancer needs."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Uveal melanoma is immunologically cold yet newly targetable: it carries few mutations and sits in the immune-privileged eye, so checkpoint inhibitors disappoint—but tebentafusp, a gp100-directed bispecific that redirects T cells, is the first agent to improve survival."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells shape uveal melanoma's spread to the liver: circulating tumor cells that downregulate MHC become NK targets, so the balance of NK surveillance versus escape influences whether liver micrometastases grow—central to this cancer's lethal course."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Uveal melanoma is notorious for vasculogenic mimicry: aggressive tumor cells form PAS-positive vascular loops that mimic endothelial channels, supplying blood without true vessels—a pattern that marks poor prognosis and blunts conventional anti-angiogenic therapy."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Uveal melanoma's lethal liver tropism depends on stroma: hepatic stellate cells and fibroblasts build the fibrotic niche that dormant tumor cells colonize, so the liver microenvironment, not just tumor genetics, governs when micrometastases awaken and grow."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The eye's immune privilege shields uveal melanoma: a TGF-β-rich anterior chamber suppresses helper T-cell responses (ACAID), so tumors grow unchecked locally—part of why this cancer is immunologically cold and slow to trigger systemic immunity."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Uveal melanoma is driven through ERK by Gq signaling: activating GNAQ/GNA11 mutations fire PLC-PKC to switch on the MAPK/ERK cascade—unlike cutaneous melanoma's BRAF route—so MEK/ERK-pathway inhibition has been the focus of targeted trials."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages mark high-risk uveal melanoma: paradoxically, a dense macrophage infiltrate (with monosomy 3 and BAP1 loss) signals worse prognosis and higher metastatic risk rather than protective immunity."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Uveal melanoma differs from skin melanoma at the telomere: it lacks the UV-signature TERT promoter mutations that drive cutaneous melanoma, reflecting its distinct, non-sun-related mutational origin (GNAQ/GNA11, BAP1) and biology."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Uveal melanoma's driver mutations signal through calcium: GNAQ/GNA11 lock the Gq protein on, firing phospholipase C to release calcium that activates PKC and MAPK—the core engine of this eye cancer, distinct from cutaneous melanoma's BRAF."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Uveal melanoma hides in the eye's immune privilege behind regulatory T cells: a Treg-rich, cold microenvironment makes it resist the checkpoint drugs that work in skin melanoma—why the T-cell engager tebentafusp was needed instead."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Uveal melanoma leans on PI3K-AKT through PTEN loss: alongside its Gq-MAPK driver, losing PTEN switches on AKT survival signaling, so combining MAPK and PI3K/AKT blockade is explored against this treatment-resistant cancer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Hypoxia drives uveal melanoma's aggressiveness: low oxygen in the eye tumor stabilizes HIF and pushes invasion and the metabolic shift that helps it seed the liver, the near-universal site of its lethal spread."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Beyond its near-exclusive liver spread, uveal melanoma can reach the lungs: hematogenous metastasis occasionally seeds pulmonary and other sites, so surveillance looks past the liver in advanced disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells underpin the new immunotherapy for uveal melanoma: this normally immune-cold tumor is now attacked with tebentafusp, which redirects T cells to a melanocyte antigen—an approach that leans on antigen presentation."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Uveal melanoma's defining pigment is melanin, built by the copper-dependent enzyme tyrosinase: this trace-metal chemistry marks the tumor's melanocytic origin and supplies the melanoma antigens that tebentafusp exploits."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Though it arises in the eye and is biologically distinct from skin melanoma, uveal melanoma can metastasize to skin and subcutaneous tissue: an unusual cutaneous site of spread beyond its dominant route to the liver."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Uveal melanoma rarely reaches the brain: while the liver dominates its metastatic pattern, late hematogenous spread can seed the central nervous system, a hard-to-treat site that worsens prognosis in advanced disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy proves the eye tumor is melanocytic: even when pigment is scant, the beam reveals melanosomes and striated premelanosomes — the same pigment-making organelles found in skin melanoma — settling the cell of origin."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Uveal melanoma can only spread through blood: the eye has no lymphatics, so tumor cells must enter the bloodstream, where they cloak themselves in platelets to survive the journey and lodge in the liver."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Beyond the liver, uveal melanoma can seed the skeleton: widespread hematogenous disease reaches bone and its marrow, a late metastatic site that adds to the burden once the cancer has escaped the eye."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "The growing tumor blinds by lifting the retina: a choroidal melanoma bulges beneath and detaches the retina, starving its photoreceptor neurons and causing the flashes, floaters, and field loss that often bring the patient in."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Uveal melanoma builds its own false vessels: aggressive tumors weave PAS-positive collagen loops and networks (vasculogenic mimicry), and these closed loops are a histologic marker of the worst-prognosis tumors."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The blood's inflammatory balance forecasts the course: a high neutrophil-to-lymphocyte ratio tracks with worse survival in uveal melanoma, and tumor-associated neutrophils help build the niche its liver metastases settle into."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody-like therapy finally moved the needle: tebentafusp, a bispecific gp100-CD3 engager, is the first agent to extend survival in metastatic uveal melanoma, while HMB-45 and Melan-A stains and loss of BAP1 confirm the tumor and predict spread."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Uveal melanoma is uniquely liver-hungry: over 90% of metastases home to the liver, the tumor cells seeding among the hepatocytes, which is why surveillance and liver-directed therapy dominate management of advanced disease."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Advanced disease shows in the red cells: extensive hepatic metastatic burden and its treatment depress erythrocyte production into an anemia, while rising liver enzymes and falling counts together signal progression."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Protons spare the eye: proton-beam radiotherapy and plaque brachytherapy deliver a sharp, contained dose to the ocular tumor while sparing the optic nerve and retina, letting many patients keep the eye instead of losing it to enucleation."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Uveal melanoma can run in families: germline BAP1 mutations transmit a tumor-predisposition syndrome — uveal melanoma with mesothelioma, kidney and skin cancers — so a diagnosis can prompt genetic testing and counseling of relatives."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxia shapes its spread to the liver: HIF signaling and the angiogenesis it drives help uveal melanoma colonize the liver, its near-exclusive metastatic site, a hypoxic-niche dependence studied as a therapeutic angle."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint drugs barely dent it: unlike cutaneous melanoma, uveal melanoma's low mutation load makes anti-CTLA-4 and anti-PD-1 largely ineffective, which is why the T-cell-redirecting drug tebentafusp, not classic checkpoint blockade, became its breakthrough therapy."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The mutant G-protein feeds growth hubs: GNAQ/GNA11 signaling activates PKC-MAPK and the PI3K-AKT-mTOR axis, so mTOR sits among the downstream nodes targeted to slow a tumor lacking the BRAF mutations that drive skin melanoma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Its immune infiltrate predicts danger: tumor-infiltrating macrophages and mast cells mark the inflammatory, monosomy-3 uveal melanomas with the worst prognosis, so the immune microenvironment is read as a marker of metastatic risk."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 runs downstream of the driver mutation: GNAQ/GNA11 signaling activates STAT3, which supports uveal melanoma proliferation and immune evasion — one of the hubs explored for therapy in a tumor that resists checkpoint drugs."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB helps it dodge immunity: the inflammatory, monosomy-3 uveal melanomas show NF-κB-driven signaling that shapes their immunosuppressive microenvironment, part of why these tumors respond poorly to standard immunotherapy."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Liver-metastatic disease raises clot risk: like other advanced solid cancers, metastatic uveal melanoma carries tumor-driven hypercoagulability that increases deep-vein thrombosis and pulmonary embolism risk."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Its breakthrough drug ignites one: tebentafusp, the first therapy to extend survival in metastatic uveal melanoma, is a T-cell engager that commonly triggers cytokine release syndrome — fever, hypotension and rash — needing close monitoring early in treatment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Liver replacement and inflammation drag down the count: the near-universal hepatic metastases of advanced uveal melanoma, with their inflammatory burden and crowding of marrow and liver, produce an anemia of chronic disease in progressive cases."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Losing an eye and facing the liver verdict weigh heavily: enucleation or vision loss plus the knowledge that monosomy-3 disease carries a high risk of fatal liver metastasis impose a substantial psychological burden and depression."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Its immunotherapy can trigger autoimmune diabetes: the checkpoint inhibitors and tebentafusp used in metastatic uveal melanoma can unleash autoimmunity against pancreatic islets, causing fulminant insulin-dependent diabetes."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Immune-activating therapy can inflame the heart: checkpoint inhibitors used against metastatic uveal melanoma occasionally cause myocarditis, and tebentafusp's cytokine release stresses the circulation, both routes toward acute heart failure."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Checkpoint immunotherapy can scar the kidneys: the PD-1 and CTLA-4 inhibitors given for advanced uveal melanoma can provoke an immune-mediated interstitial nephritis that, if it recurs, leaves chronic kidney impairment."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It spreads almost only to the liver: uveal melanoma is strikingly hepatotropic, with the great majority of metastases lodging in the liver, so surveillance and treatment centre on hepatic disease."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Enucleation is a healing challenge: removing the eye for a large uveal melanoma and fitting an orbital implant leaves a socket that must heal, and any prior plaque brachytherapy compromises the tissue."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Vision loss and lifelong liver-metastasis surveillance breed worry: the threat of late hepatic spread years after treatment and the loss of an eye foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "After the liver, it favours the lungs: pulmonary metastases are the second commonest site of uveal-melanoma spread, often appearing as nodules years after the primary eye tumour is treated."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It shares a lineage with skin melanoma but differs sharply: oculodermal melanocytosis (nevus of Ota) raises its risk, yet uveal melanoma is driven by GNAQ/GNA11 rather than the BRAF mutations of cutaneous disease."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The eye has no lymphatics, so it cannot spread to nodes: unlike cutaneous melanoma, uveal melanoma disseminates almost purely haematogenously to the liver, which is why sentinel-node biopsy plays no role."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "After liver and lung it seeds bone: skeletal metastases occur in disseminated uveal melanoma, causing painful deposits in the spine and pelvis."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can reach the brain late: brain metastases occur in widely disseminated uveal melanoma, though far less commonly than its dominant liver spread."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its breakthrough drug stresses the circulation: tebentafusp triggers cytokine release with hypotension and fluid shifts, and disseminated disease can rarely involve the heart."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A bispecific T-cell engager extended survival: tebentafusp redirects T cells against the gp100-HLA complex on uveal melanoma, the first therapy to improve survival in this checkpoint-resistant cancer."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Liver-dominant spread disrupts metabolism: uveal melanoma metastasises overwhelmingly to the liver, whose failure in advanced disease deranges glucose and hormone metabolism."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "Ocular masses have infectious mimics: chorioretinitis from toxoplasmosis is among the differentials of a pigmented or inflammatory intraocular lesion that uveal melanoma must be distinguished from."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Unlike skin melanoma, it resists checkpoints: uveal melanoma carries a low mutational burden and an immunosuppressive microenvironment, so PD-1 and CTLA-4 blockade that transforms cutaneous melanoma works poorly — the gap that drove tebentafusp's development."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Largely chemoresistant: conventional cytotoxic chemotherapy such as dacarbazine, of limited use in any melanoma, achieves little in metastatic uveal melanoma, leaving liver-directed and T-cell-redirecting approaches as the mainstays."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It seeds the liver sinusoids: uveal melanoma cells lodge in the hepatic sinusoids and grow within the lobule as micrometastases that can smoulder for years, the reason serial liver MRI surveillance underpins follow-up after the eye is treated."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "An immune-privileged, cold tumour: arising in the immune-privileged eye with a low mutational burden, uveal melanoma rarely forms the germinal-centre-like lymphoid structures that predict checkpoint response, so the TCR-bispecific tebentafusp—not PD-1 blockade—extends survival."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "A shared splicing-factor mutation: SF3B1, mutated in a subset of uveal melanomas, is the same spliceosome gene that defines myelodysplastic syndrome with ring sideroblasts—one splicing defect across an eye cancer and a marrow disease."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Liver-directed therapy unites them: uveal melanoma metastasises almost exclusively to the liver, so like hepatocellular carcinoma it is treated with liver-directed approaches—hepatic perfusion, radioembolization and resection—when disease is liver-confined."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Vasculogenic mimicry: uveal melanoma cells form their own PAS-positive vascular channels that imitate the arterial wall, a pattern predicting metastasis and helping explain its resistance to anti-angiogenic therapy."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Engineered T-cells for cold tumours: uveal melanoma (treated with the gp100 ImmTAC tebentafusp) and synovial sarcoma (treated with NY-ESO-1 TCR cells) both resist checkpoint blockade and instead yield to HLA-restricted redirected T-cells."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "The choroid as a target: uveal melanoma is the commonest primary intraocular tumour in adults, but the choroid is also the commonest site of intraocular metastasis—classically from breast cancer—a key differential."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "A shared splicing-factor mutation: SF3B1 mutations recur across uveal melanoma, myelodysplasia and a subset of chronic lymphocytic leukaemia, an unexpected molecular thread linking an eye cancer to blood cancers."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Beyond the liver: while uveal melanoma overwhelmingly metastasises to the liver, the lung is its second site, the tumour seeding the alveolar bed in later disseminated disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Late skeletal spread: in advanced uveal melanoma, metastases reach the bone, depositing in the cortical skeleton alongside the dominant hepatic and pulmonary disease."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "BAP1-linked epigenetics: BAP1 loss in high-risk uveal melanoma creates a dependence on EZH2, paralleling the BAP1-EZH2 synthetic lethality seen in mesothelioma."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: cyclin D1 with CDK4/6 propels uveal melanoma proliferation downstream of GNAQ/GNA11-driven MAPK signalling."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Amplified aggression: MYC amplification (chromosome 8q gain) marks high-risk, metastasis-prone uveal melanoma."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "Hepatic tropism: MET (c-Met) signalling drives the striking liver tropism of uveal melanoma metastasis, the dominant and usually fatal site of spread."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Stromal growth: PDGF signalling supports the proliferation and angiogenesis of uveal melanoma, part of its receptor-tyrosine-kinase landscape."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage infiltration: CCL2 recruits tumour-associated macrophages whose abundance, paradoxically, marks the more aggressive uveal melanomas."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Wild-type p53 restraint: uveal melanoma rarely mutates TP53 and instead keeps p53 suppressed through high MDM2, making MDM2 inhibitors that reactivate p53 a rational therapeutic strategy in this otherwise treatment-resistant tumour."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Hepatic tropism: CXCR4 on uveal-melanoma cells follows CXCL12 gradients to the liver, explaining the near-exclusive hepatic pattern of metastasis that dominates uveal-melanoma mortality."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "Invasion signalling: GAS6-AXL signalling promotes the migration and epithelial-mesenchymal-like invasion of uveal melanoma, contributing to the early micrometastatic spread that precedes clinical detection."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Tebentafusp killing: the gp100-HLA-A*02/CD3 bispecific tebentafusp — the first therapy to extend survival in metastatic uveal melanoma — redirects cytotoxic T cells to kill tumour cells through perforin and granzyme, despite this tumour's low mutational burden."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Hepatotropism: uveal melanoma cells strongly express IGF-1R, and the liver's abundant IGF-1 helps explain the near-exclusive hepatic homing of metastases, making IGF-1R a candidate target against the liver disease that dominates outcome."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Melanocyte GPCR: uveal melanoma cells express the endothelin-B receptor inherited from their melanocyte lineage, an EDNRB signalling axis that supports proliferation and survival and is being explored as a therapeutic vulnerability."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival arm: downstream of the GNAQ/GNA11 drivers, PI3K-AKT-mTOR signalling (AKT, mTOR and PTEN already mapped) supports uveal melanoma survival, a targetable axis parallel to its YAP and MAPK arms."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptosis resistance: uveal melanoma characteristically over-expresses anti-apoptotic BCL-2, underlying its resistance to chemotherapy and the long survival of the dormant liver micrometastases that determine its lethality."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Metastatic phenotype: NOTCH signalling promotes the proliferation and invasive, metastatic phenotype of uveal melanoma, cooperating with the YAP and MAPK arms already mapped downstream of GNAQ/GNA11."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: cyclin-D1 (mapped) and CDK4/6 release E2F1 to drive proliferation downstream of the constitutive GNAQ/GNA11-MAPK signalling of uveal melanoma."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle brake: CDKN2A loss removes the restraint on the cyclin-D1-CDK4/6 axis and is associated with progression of uveal melanoma."
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "Metastatic spread: loss of E-cadherin and the dedifferentiation accompanying BAP1 loss (mapped) promote the epithelial-mesenchymal-like transition that drives the hepatotropic metastasis of uveal melanoma."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: dysregulation of the RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) contributes to the proliferation of uveal melanoma."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Immune-evasion signalling: JAK-STAT3 signalling (STAT3 already mapped) contributes to the survival and immune-evasion signalling of uveal melanoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Hepatic-metastasis niche: IL-6-STAT3 signalling (STAT3 already mapped) supports the survival of uveal-melanoma cells, particularly in the liver microenvironment that is its predominant site of metastasis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of uveal melanoma, a tumour notable for its poor response to checkpoint immunotherapy."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling governs the interferon-driven antitumour response and immune-evasion balance of the immunologically cold uveal melanoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports immune evasion and the hepatic metastatic colonisation that determines outcome in uveal melanoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling shapes EMT and the hepatic metastatic niche that dictates the liver-tropic spread of uveal melanoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "PI3K-AKT-mediated FOXO inactivation removes a pro-apoptotic brake, supporting survival of uveal melanoma cells (PI3K-AKT already mapped)."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven cyclin-D1-RB1 cell-cycle entry (cyclin-D1 and RB1 mapped) sustains proliferation in uveal melanoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β acts downstream of the GNAQ/GNA11-PKC-YAP axis, modulating the survival signaling of uveal melanoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the immunosuppressive, immune-cold microenvironment of uveal melanoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the GNAQ/11-activated pathways contributes to the invasion and hepatic-metastatic tropism of uveal melanoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation, alongside BAP1 loss (BAP1 already mapped), of uveal melanoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and dormancy of the hepatic-metastatic cells of uveal melanoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of uveal melanoma."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of uveal melanoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of uveal melanoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling downstream of GNAQ/GNA11-PLCβ participates in the oncogenic signaling of uveal melanoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of uveal melanoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of uveal melanoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of uveal melanoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HLA-restricted immunotherapy: uveal melanoma resists checkpoint blockade, yet the bispecific tebentafusp, the first agent to extend survival, redirects T cells to gp100 presented on HLA, underscoring the central role of antigen presentation in its treatment."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Intact p53 vulnerability: uveal melanoma rarely mutates TP53 and instead suppresses wild-type p53 through MDM2 (already mapped), making pharmacologic p53 reactivation a rational strategy distinct from the mutant-p53 biology of many cancers."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Radiotherapy execution: primary uveal melanoma is controlled by plaque brachytherapy and proton-beam radiation that kill tumour cells via caspase-3-mediated apoptosis, the pathway whose evasion (BCL-2 already mapped) underlies radioresistant relapse."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Tebentafusp immunotherapy: tebentafusp, a gp100-directed T-cell engager, is the first therapy to extend survival in metastatic uveal melanoma (in HLA-A*02:01 patients; MHC class II already mapped), and IL-2-driven T-cell activity underlies the adoptive approaches."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cytokine-release cardiotoxicity: the T-cell-engaging immunotherapy for uveal melanoma can provoke cytokine-release syndrome with hypotension and cardiac stress, and troponin elevation helps detect the myocardial injury of these reactions."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Metastatic anaemia: extensive hepatic metastasis (liver already mapped) and its treatment lower haemoglobin in advanced uveal melanoma, contributing to the fatigue and decline of the metastatic disease that dominates prognosis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the uveal melanoma microenvironment, favoured by the immune privilege of the eye, dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the resistance to conventional checkpoint blockade."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF and endothelin-1 (already mapped) shapes the vasculature of uveal melanoma, including the vasculogenic-mimicry networks that are an adverse prognostic feature of the tumour."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: the metabolically active uveal melanoma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species add to the biology of this pigment-cell tumour of the eye."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), and a high macrophage infiltrate is an adverse prognostic feature of uveal melanoma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Ocular immune privilege: TGF-β in the eye's immune-privileged microenvironment (SMAD4 already mapped) suppresses the anti-tumour response, helping uveal melanoma evade immunity, part of why checkpoint blockade works poorly against it."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia of advanced disease: the hepatic metastatic burden (liver already mapped) and the systemic therapy of advanced uveal melanoma cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immune-privileged (TGF-β already mapped) microenvironment of uveal melanoma."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Melanocyte metals: zinc supports the enzymes of melanogenesis and the melanocyte function, part of the trace-metal biology (copper already mapped) of the uveal melanocytes from which uveal melanoma arises."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) to add an anaemia of chronic disease to the metastatic-burden anaemia (haemoglobin already mapped) of advanced uveal melanoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metastatic-niche adipokine: leptin, the adipokine of the metabolic microenvironment, signals within the hepatic (liver already mapped) metastatic niche of uveal melanoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is the adipokine of the metabolic milieu of uveal melanoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the uveal-melanoma microenvironment."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the (immunologically cold) uveal melanoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm engaged by the tebentafusp (gp100-HLA, MHC already mapped) against uveal melanoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the uveal-melanoma immune microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of uveal melanoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the uveal-melanoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immunologically cold uveal-melanoma microenvironment."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Tertiary lymphoid structures: the B cells and the tertiary lymphoid structures, though scarce in the immunologically cold uveal melanoma, are a candidate correlate of the tebentafusp response."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a contribute to the inflammatory and immunosuppressive dimension of the uveal-melanoma microenvironment and its hepatic (liver already mapped) metastatic niche."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells to an immunosuppressive phenotype in the uveal-melanoma microenvironment."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Central complement: the complement C3, upstream of the C5 and C5aR1 (already mapped), is the pivot of the complement activation within the immunosuppressive uveal-melanoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the uveal-melanoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), evading the complement attack in the primary tumour and its hepatic (liver already mapped) metastatic niche."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Tumour iron: transferrin, the iron carrier, supplies the iron demand of the uveal-melanoma cells and their iron-rich hepatic (liver already mapped) metastatic niche."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Stromal alarmin: TSLP released from the uveal-melanoma stromal fibroblasts (already mapped) and choroidal stroma activates mast cells (already mapped) and dendritic cells (already mapped), sustaining the type-2 immunosuppressive microenvironment that blunts cytotoxic immunity."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Tumour anaemia and EPO-R: erythropoietin corrects the anaemia of chronic disease (already mapped) of advanced uveal melanoma, and EPOR expression on choroidal melanocytes has been reported, suggesting possible direct trophic effects on tumour growth."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Invasion ECM scaffold: periostin is upregulated in the uveal-melanoma stromal niche and the hepatic (liver already mapped) metastatic microenvironment, promoting the extracellular matrix remodelling and the invasion of the GNAQ/GNA11-driven melanoma cells."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Intraocular kinin: bradykinin, generated in the choroidal vasculature by kallikrein-kinin activation, amplifies vascular permeability and the inflammatory microenvironment of uveal melanoma, promoting tumour growth and metastatic spread."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement-contact brake: C1-esterase inhibitor restrains the classical complement C1 and the contact system (C3/C5/C5aR1/factor-H already mapped) activated in the uveal-melanoma microenvironment and its hepatic metastatic niche."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Choroidal mast-cell effector: histamine released by mast cells (already mapped) in the choroidal uveal-melanoma stroma amplifies local vascular permeability and the immunosuppressive microenvironment that blunts cytotoxic T-cell surveillance."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "UM melatonin: melatonin suppresses uveal-melanoma proliferation via MT1/MT2 receptor-mediated inhibition of cAMP and mTOR (already mapped) signalling; it also augments NK-cell (already mapped) cytotoxicity against the immunosuppressive uveal-melanoma tumour microenvironment."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "UM testosterone: androgen receptor signalling in uveal melanoma promotes tumour-cell proliferation and survival; testosterone drives the liver (already mapped) metastatic niche via androgen-mediated hepatic immune reprogramming that blunts NK-cell (already mapped) surveillance."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "UM serotonin: serotonin, co-produced by neuroendocrine uveal tissue, acts on 5-HT receptors on uveal melanoma cells driving autocrine proliferative signalling and promotes the liver (already mapped) metastatic niche via serotonin-mediated hepatic immunosuppression."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "UM oxytocin: oxytocin receptor on uveal melanoma cells attenuates GNAQ (already mapped)-driven cAMP/PKA and mTOR (already mapped) oncogenic signalling; oxytocin also enhances NK-cell (already mapped) cytotoxicity against the immune-evading uveal-melanoma microenvironment."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "UM vasopressin: vasopressin V1A receptor on uveal melanoma cells intersects GNAQ (already mapped)/PLC/PKC and mTOR (already mapped) oncogenic axes; V1A-driven calcium-PKC signalling amplifies uveal-melanoma proliferation and immune evasion in the ocular microenvironment."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "UM prolactin: prolactin via JAK2/STAT3 (already mapped) on uveal melanoma cells promotes tumour-cell survival and NF-κB (already mapped)-mediated anti-apoptotic expression; prolactin also modulates the hepatic (already mapped) metastatic niche of uveal melanoma."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "UM selenium: selenoproteins quench ROS from mTOR (already mapped) and VEGF (already mapped) in uveal melanoma; selenium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs T-cytotoxic-cell (already mapped) and macrophage (already mapped) immunity."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "UM iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour surveillance; thyroid deficiency amplifies VEGF (already mapped) and mTOR (already mapped)-driven uveal melanoma growth and NF-κB (already mapped) cascade."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "UM sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplify VEGF (already mapped) and mTOR (already mapped) and STAT3 (already mapped)-driven cascade of uveal melanoma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "UM magnesium: magnesium, as mTOR (already mapped) kinase cofactor in macrophages (already mapped) and uveal melanoma cells, supports tumour growth; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of uveal melanoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "UM potassium: potassium efflux from macrophages (already mapped) and uveal melanoma cells drives NLRP3-IL-1β; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) and mTOR (already mapped) tumour cascade of uveal melanoma."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "UM phosphorus: phosphorus, as ATP precursor in macrophages (already mapped) and T-cytotoxic-cell (already mapped), fuels anti-tumour immunity; phosphorus deficiency amplifies NF-κB (already mapped) and VEGF (already mapped) and mTOR (already mapped) uveal melanoma cascade."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "UM carbon: carbon, as metabolic backbone of VEGF (already mapped) and tumour lipids in macrophages (already mapped) and uveal melanoma cells, drives tumour growth; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of uveal melanoma."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "UM chloride: chloride channels in macrophages (already mapped) and T-cytotoxic-cell (already mapped) modulate tumour-immune homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of uveal melanoma."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "UM hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and T-cytotoxic-cell (already mapped), quenches tumour ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and VEGF (already mapped) and mTOR (already mapped) cascade of uveal melanoma."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "UM nitrogen: nitric oxide from macrophages (already mapped) and tumour vasculature modulates angiogenic tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade of uveal melanoma."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "UM sulfur: hydrogen sulfide from macrophages (already mapped) and tumour vasculature modulates angiogenic tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of uveal melanoma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "UM GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and tumour vasculature modulates metabolic angiogenesis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of uveal melanoma."
---

# Uveal Melanoma

## Overview

**Uveal melanoma** is the most common primary **intraocular malignancy** in adults, arising from melanocytes of the uveal tract (choroid ~90%, ciliary body ~7%, iris ~3%). Despite its rarity (~5 cases/100,000/year), uveal melanoma carries the worst prognosis among ocular cancers and is biologically distinct from cutaneous melanoma — driven by **GNAQ/GNA11 Gαq-family mutations** (not BRAF V600E), with a profoundly **immunologically cold** tumor microenvironment and near-universal liver tropism for metastases. The landmark molecular classification divides uveal melanoma into four classes based on **BAP1, SF3B1, and EIF1AX** mutation status, each with distinct metastatic risk [^harbour-2010-bap1-uveal]. **Tebentafusp** (ImmTAC bispecific redirecting T cells to gp100-expressing cells) became the first agent to demonstrate OS benefit in metastatic uveal melanoma in the randomized Phase 3 IMCgp100-202 trial (FDA approved January 2022), a landmark achievement given the total failure of checkpoint inhibitors in this disease [^nathan-2021-tebentafusp].

**Epidemiology:**
- Incidence: ~6-7/million/year USA; ~7,000 cases/year globally
- Median age: ~60 years; slight male predominance (M:F ~1.3:1)
- Risk factors: fair skin, light-colored iris, UV light exposure (iris melanoma), BAP1-TPDS germline syndrome, large ocular nevi
- Race: predominantly Caucasians; rare in African Americans (~6-fold lower risk)
- ~50% develop metastatic disease within 15 years; liver is the dominant metastatic site (~90%)

## Structure

### Molecular subtypes (WHO/TCGA classification)

**Class 1A (~25-30%) — EIF1AX mutation:**
- EIF1AX (eukaryotic initiation factor 1A, X-linked): mutations in intron 5-6 splice site or exon 1/2 → aberrant translation initiation; functionally alters protein synthesis
- 5-year metastasis-free survival: ~95-100%; extremely favorable; late relapses rare
- BAP1 and SF3B1 intact; chromosome 3 disomy; 6p gain often present
- Usually requires no systemic surveillance after local treatment; ophthalmologic follow-up

**Class 1B (~20-25%) — SF3B1 mutation (R625C/H/S):**
- SF3B1 R625 in HEAT repeat 12 → cryptic 3' splice site activation (same mechanism as K700E in MDS)
- 5-year metastasis-free survival: ~80-85%; late relapses documented 10-20 years post-diagnosis
- Chromosome 6p gain, 8q gain patterns; BAP1 intact
- Requires prolonged surveillance (annual liver MRI for ≥15 years)

**Class 2 (~40-45%) — BAP1 loss:**
- BAP1 biallelic loss (somatic mutation + LOH at chromosome 3): ~45% of all uveal melanoma; nearly all Class 2 tumors
- 5-year metastasis-free survival: ~25-35%; median time to metastasis ~2-3 years
- Early liver metastases; poor prognosis
- Monosomy 3 (chromosome 3 loss of heterozygosity) is the cytogenetic hallmark
- BAP1 IHC (nuclear loss in >90% of tumor cells): primary clinical prognostic test

**Class overlap:** A minority of tumors harbor two driver mutations or don't fit neatly into one class; EIF1AX+SF3B1 co-mutations have been reported rarely.

### Oncogenic drivers

**GNAQ/GNA11 (Gαq/Gα11 mutations, ~85% combined):**
- GNAQ R183Q (codon 183, GTP-to-GDP exchange) or Q209L/P (effector binding domain): ~45%
- GNA11 Q209L: ~40%
- Both Q209 mutations: equivalent functional outcome — constitutive GTP-bound active Gαq/Gα11
- **Downstream:** PLCβ → IP₃ → Ca²⁺ + DAG → PKC activation → MEK/ERK (MAPK) + YAP/TAZ (Hippo pathway) constitutive activation
- **NOT RAS-BRAF-MEK:** Unlike cutaneous melanoma; RAS not required; BRAF V600E absent
- **Therapeutic implications:** MEK inhibitors (selumetinib, trametinib) have activity (ORR ~15-20%) but limited duration; PKC inhibitors (sotrastaurin) studied; YAP/TAZ inhibitors preclinical

**CYSLTR2 and PLCB4 (rare alternative drivers, ~3% each):**
- CYSLTR2 L129Q (cysteinyl leukotriene receptor 2) → constitutive Gαq activation without GNAQ/GNA11 mutation
- PLCB4 D630N → downstream PLCβ constitutive activation

**Secondary somatic events (metastatic progression):**
- Monosomy 3 (~50% of all uveal melanoma): loss of BAP1 (chromosome 3p) is the key event; non-random
- 8q gain (MYC amplification): ~50-60%; correlates with metastatic risk
- 6p gain: ~40%; associated with Class 1B
- MDM2 amplification: ~20%; p53 pathway inhibition

## Function

### Normal uveal melanocyte biology

Uveal melanocytes are neural crest-derived, residing in the uveal stroma and maintaining retinal pigment epithelium-independent pigmentation. They do not cycle under normal conditions (post-mitotic). GNAQ/GNA11 mutations in uveal melanocytes → constitutive MAPK + PKC-β signaling → cell cycle re-entry → proliferation while retaining melanocyte identity (S100, HMB-45, gp100/PMEL17 expression). gp100 (PMEL17, a premelanosomal protein responsible for melanin granule structure) is ubiquitously and stably expressed in uveal melanoma → the basis for tebentafusp's TCR targeting.

### Uveal melanoma vs. cutaneous melanoma differences

| Feature | Uveal Melanoma | Cutaneous Melanoma |
|---------|---------------|-------------------|
| Primary driver | GNAQ/GNA11 (~85%) | BRAF V600E (~40-50%) |
| TMB | Very low (<1 mut/Mb) | High (10-50 mut/Mb) |
| PD-L1 | Low/absent | Variable |
| ICI response | <5% ORR | 30-60% ORR |
| Metastatic site | Liver (~90%) | Lung, brain, liver |
| Liver microenvironment | Immunosuppressive | Less suppressive |
| UV mutation signature | Absent | Present (C>T transitions) |

## Pathology

### Local tumor characteristics

**Primary tumor staging (AJCC 8th edition):**
- T1: Tumor ≤12 mm largest basal diameter; ≤3 mm height → T1a (no ciliary body, no extraocular ext.), T1b-c (ciliary body involvement ± extraocular)
- T2: 12.1-18 mm and/or 3.1-6 mm height
- T3: >18 mm and/or >6 mm height
- T4: With extraocular extension (T4a: ≤5 mm, T4b: >5 mm)

**Histological types:**
- Spindle cell (most favorable): uniform spindle-shaped cells; rare mitoses
- Epithelioid (most aggressive): large polygonal cells; prominent nucleoli; frequent mitoses
- Mixed: mixed spindle and epithelioid (most common)

**Prognostic biomarkers:**
- BAP1 IHC (nuclear loss): ~45% of cases; highest-risk marker; clinical standard
- Monosomy 3 FISH: equivalent to BAP1 loss; performed on tumor biopsy
- Gene expression profiling (GEP, DecisionDx-UM): 15-gene assay; Class 1A/1B/2 classification; validated in multiple cohorts
- SF3B1 molecular testing: next-gen sequencing; identifies Class 1B for late-relapse surveillance

### Treatment of primary uveal melanoma

**Local treatment (eye preservation or enucleation):**
- **Plaque brachytherapy (I-125 episcleral plaque):** Standard for medium tumors (≤10 mm height); comparable local control to enucleation; 5-year local failure rate ~10%; visual acuity decline over time (radiation optic neuropathy, maculopathy)
- **Proton beam radiotherapy:** Requires specialized facility (Boston, San Francisco, Philadelphia); excellent local control; particularly for large/posteriorly located tumors
- **Stereotactic radiosurgery (Gamma Knife, CyberKnife):** Emerging for select cases
- **Enucleation:** Required for large tumors (>12 mm height) or those not amenable to globe-sparing treatment; no OS benefit over brachytherapy (COMS trial)
- **COMS Trial:** Iodine-125 brachytherapy vs. enucleation for medium choroidal melanoma: equivalent 5-year survival (~81% both arms) — established eye-preserving therapy as standard

**Iris melanoma:** Wide local excision or iridocyclectomy; low metastatic risk; usually indolent

### Treatment of metastatic uveal melanoma

**Systemic therapy (prior era — largely ineffective):**
- Dacarbazine, ipilimumab, nivolumab, pembrolizumab: ORR <5%; no OS benefit vs best supportive care
- Selumetinib (MEK1/2 inhibitor): ORR ~15%; improved PFS over chemotherapy but no OS benefit (SUMIT trial vs dacarbazine+temozolomide)
- Combination MEK+PKC (selumetinib+sotrastaurin): modest activity

**Tebentafusp (Kimmtrak — FDA Jan 2022 for HLA-A*02:01+ metastatic uveal melanoma):**
- **Mechanism:** ImmTAC (immune-mobilizing monoclonal TCR against cancer) bispecific: one arm is a soluble high-affinity TCR binding gp100/PMEL17 peptide-HLA-A*02:01 complex on melanoma cells; other arm is anti-CD3 scFv → recruits polyclonal T cells → directed killing regardless of TCR specificity
- **HLA restriction:** Requires HLA-A*02:01 genotype (~50% of Caucasians, ~25% of Asians); companion diagnostic required
- **IMCgp100-202 (Phase 3 RCT, N=378):** Tebentafusp vs. investigator's choice (pembrolizumab, ipilimumab, or dacarbazine) in HLA-A*02:01+ treatment-naive metastatic uveal melanoma: OS 21.7 vs 16.0 months (HR 0.51, p<0.001); 1-year OS 73% vs 58%; first Phase 3 OS benefit in metastatic uveal melanoma [^nathan-2021-tebentafusp]
- **Toxicity:** Cytokine release syndrome (grades 1-3 in >80%, Grade 4 rare); skin reactions (rash, erythema); pyrexia; most toxicities occur with first 3 infusions and diminish
- **Limitation:** Only for HLA-A*02:01+ patients; liver metastasis ORR ~10% (better for non-liver sites); primary benefit likely through immune activation rather than direct tumor lysis

**Liver-directed therapies:**
- Hepatic arterial infusion (HAI): melphalan via isolated hepatic perfusion (IHP/Delcath); ORR ~35-50%; liver-directed control; ~6-month hepatic PFS; not OS benefit demonstrated in Phase 3
- TACE (transarterial chemoembolization): ORR ~25-35%; symptom control
- Y-90 radioembolization (SIR-spheres/TheraSphere): moderate activity in liver metastases
- Surgical resection: for solitary/few hepatic metastases; 3-year OS ~30-40% in selected series

**Surveillance:**
- Liver MRI or ultrasound every 6 months for ≥5 years after primary treatment
- Class 1B (SF3B1): surveillance extended to 15+ years given late relapse pattern
- LFTs, LDH at each visit
- COMS trial showed no benefit of pre-enucleation radiation in reducing metastasis

## Connections

- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — SF3B1 R625C/H occurs in ~15-20% uveal melanoma → cryptic 3' SS activation → Class 1B (intermediate prognosis, late relapses); SF3B1-mutant uveal melanoma has a distinct transcriptome from BAP1-loss Class 2; H3B-8800 may exploit this vulnerability.
- `connects-to` → **[BAP1](../../03-molecular/bap1/README.md)** — BAP1 biallelic loss → Class 2 uveal melanoma (~45%; high metastatic risk, early liver relapse); BAP1 IHC nuclear loss is the primary prognostic marker; BAP1-TPDS germline → uveal melanoma lifetime risk ~30-45%; EZH2 inhibition studied in BAP1-null disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss occurs in ~15-20% of metastatic uveal melanoma; PI3K-AKT-mTOR activation drives progression; PI3K/mTOR + MEK inhibitor combinations overcome GNAQ-driven resistance in preclinical uveal melanoma models; everolimus studied in metastatic disease.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1/PD-L1 checkpoint inhibitors have very low activity in uveal melanoma (ORR <5%) due to low tumor mutational burden and immunosuppressive tumor microenvironment; tebentafusp bypasses checkpoint resistance by directly recruiting T cells via gp100-TCR×CD3 bispecific mechanism.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — Uveal melanoma is biologically distinct from cutaneous melanoma: GNAQ/GNA11 (not BRAF V600E) → MEK inhibitors only partial activity; very low TMB vs UV-mutational burden; ICB ORR <5% in uveal vs 30-60% in cutaneous; liver-dominant metastasis vs lung/brain tropism.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — GNAQ/GNA11 → PLCβ → PKC → Rho → YAP/TAZ nuclear entry (Hippo-independent); YAP/TAZ drive CTGF, CYR61, BIRC5 → uveal melanoma proliferation and survival; verteporfin (YAP inhibitor) active in preclinical uveal models; YAP-TEAD inhibitors (IAG933, VT3989) in Phase 1/2 trials.
- `connects-to` → **[BRAF](../../03-molecular/braf/README.md)** — BRAF V600E absent in uveal melanoma (0%); GNAQ/GNA11 → PLCβ/PKC → MEK (RAS-independent) → BRAF inhibitors ineffective; MEK inhibitors (selumetinib): ORR ~15% (SUMIT trial) but no OS benefit; MEK + PKC combinations overcome adaptive resistance in preclinical uveal melanoma models.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Uveal melanoma is the commonest primary intraocular cancer in adults, from melanocytes of the uveal tract — choroid (~90%), ciliary body, or iris; it presents with painless vision change or floaters, and globe-sparing brachytherapy or proton therapy has replaced most enucleation.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is uveal melanoma's near-exclusive metastatic target: ~90% of metastases home there (the eye lacks lymphatics), often years after the eye is treated — so lifelong liver surveillance is essential, and liver-directed therapy plus tebentafusp are mainstays.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Uveal melanoma resists checkpoint inhibitors (ORR <5%, low mutational burden), so it engages cytotoxic T cells differently: tebentafusp, a gp100-HLA × CD3 bispecific, tethers CD8+ T cells to HLA-A*02:01 tumor cells — the first drug to improve survival in metastatic disease.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — Uveal melanoma and mesothelioma both define the BAP1 tumor predisposition syndrome: germline BAP1 loss raises risk of both, plus renal cell carcinoma and skin tumors, and BAP1 loss in a uveal melanoma marks the high-risk class with the worst metastatic prognosis.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — Uveal melanoma and NF2 converge on the Hippo pathway: NF2's Merlin restrains YAP, while uveal melanoma's GNAQ/GNA11 mutations activate YAP through Hippo—so both illustrate how unleashed YAP/TEAD drives growth, here in the pigmented cells of the eye.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is the eye-sparing mainstay for uveal melanoma: plaque brachytherapy and proton or photon beams deliver tumoricidal radiation to the choroidal tumor while preserving the globe—an alternative to enucleation, though metastatic risk depends on genetics.
- `connects-to` → **[Retinoblastoma](../retinoblastoma/README.md)** — Uveal melanoma and retinoblastoma are the two principal intraocular malignancies: retinoblastoma is a childhood RB1-driven retinal tumor, while uveal melanoma is an adult melanocytic tumor of the choroid driven by GNAQ/GNA11 and BAP1—both threaten the eye and vision.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Uveal melanoma and cholangiocarcinoma both belong to the BAP1 syndrome: germline BAP1 loss raises risk of both, and in uveal melanoma somatic BAP1 loss marks the liver-metastasizing tumors—linking an eye cancer to a bile-duct cancer through one chromatin gene.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Uveal melanoma and clear-cell renal cell carcinoma are joined by the BAP1 syndrome: BAP1 loss drives aggressive forms of both, so germline-mutation families are surveilled for eye, kidney, mesothelioma and skin tumors—BAP1 a shared deubiquitinase tumor suppressor.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis and a leaky vasculature mark uveal melanoma: the tumor secretes VEGF to vascularize the eye and prepare its spread, high levels predict metastasis, and anti-VEGF agents are explored alongside the liver-directed therapy this cancer needs.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Uveal melanoma is immunologically cold yet newly targetable: it carries few mutations and sits in the immune-privileged eye, so checkpoint inhibitors disappoint—but tebentafusp, a gp100-directed bispecific that redirects T cells, is the first agent to improve survival.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells shape uveal melanoma's spread to the liver: circulating tumor cells that downregulate MHC become NK targets, so the balance of NK surveillance versus escape influences whether liver micrometastases grow—central to this cancer's lethal course.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Uveal melanoma is notorious for vasculogenic mimicry: aggressive tumor cells form PAS-positive vascular loops that mimic endothelial channels, supplying blood without true vessels—a pattern that marks poor prognosis and blunts conventional anti-angiogenic therapy.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Uveal melanoma's lethal liver tropism depends on stroma: hepatic stellate cells and fibroblasts build the fibrotic niche that dormant tumor cells colonize, so the liver microenvironment, not just tumor genetics, governs when micrometastases awaken and grow.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The eye's immune privilege shields uveal melanoma: a TGF-β-rich anterior chamber suppresses helper T-cell responses (ACAID), so tumors grow unchecked locally—part of why this cancer is immunologically cold and slow to trigger systemic immunity.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Uveal melanoma is driven through ERK by Gq signaling: activating GNAQ/GNA11 mutations fire PLC-PKC to switch on the MAPK/ERK cascade—unlike cutaneous melanoma's BRAF route—so MEK/ERK-pathway inhibition has been the focus of targeted trials.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages mark high-risk uveal melanoma: paradoxically, a dense macrophage infiltrate (with monosomy 3 and BAP1 loss) signals worse prognosis and higher metastatic risk rather than protective immunity.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Uveal melanoma differs from skin melanoma at the telomere: it lacks the UV-signature TERT promoter mutations that drive cutaneous melanoma, reflecting its distinct, non-sun-related mutational origin (GNAQ/GNA11, BAP1) and biology.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Uveal melanoma's driver mutations signal through calcium: GNAQ/GNA11 lock the Gq protein on, firing phospholipase C to release calcium that activates PKC and MAPK—the core engine of this eye cancer, distinct from cutaneous melanoma's BRAF.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Uveal melanoma hides in the eye's immune privilege behind regulatory T cells: a Treg-rich, cold microenvironment makes it resist the checkpoint drugs that work in skin melanoma—why the T-cell engager tebentafusp was needed instead.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Uveal melanoma leans on PI3K-AKT through PTEN loss: alongside its Gq-MAPK driver, losing PTEN switches on AKT survival signaling, so combining MAPK and PI3K/AKT blockade is explored against this treatment-resistant cancer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Hypoxia drives uveal melanoma's aggressiveness: low oxygen in the eye tumor stabilizes HIF and pushes invasion and the metabolic shift that helps it seed the liver, the near-universal site of its lethal spread.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Beyond its near-exclusive liver spread, uveal melanoma can reach the lungs: hematogenous metastasis occasionally seeds pulmonary and other sites, so surveillance looks past the liver in advanced disease.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells underpin the new immunotherapy for uveal melanoma: this normally immune-cold tumor is now attacked with tebentafusp, which redirects T cells to a melanocyte antigen—an approach that leans on antigen presentation.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Uveal melanoma's defining pigment is melanin, built by the copper-dependent enzyme tyrosinase: this trace-metal chemistry marks the tumor's melanocytic origin and supplies the melanoma antigens that tebentafusp exploits.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Though it arises in the eye and is biologically distinct from skin melanoma, uveal melanoma can metastasize to skin and subcutaneous tissue: an unusual cutaneous site of spread beyond its dominant route to the liver.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Uveal melanoma rarely reaches the brain: while the liver dominates its metastatic pattern, late hematogenous spread can seed the central nervous system, a hard-to-treat site that worsens prognosis in advanced disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy proves the eye tumor is melanocytic: even when pigment is scant, the beam reveals melanosomes and striated premelanosomes — the same pigment-making organelles found in skin melanoma — settling the cell of origin.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Uveal melanoma can only spread through blood: the eye has no lymphatics, so tumor cells must enter the bloodstream, where they cloak themselves in platelets to survive the journey and lodge in the liver.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Beyond the liver, uveal melanoma can seed the skeleton: widespread hematogenous disease reaches bone and its marrow, a late metastatic site that adds to the burden once the cancer has escaped the eye.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — The growing tumor blinds by lifting the retina: a choroidal melanoma bulges beneath and detaches the retina, starving its photoreceptor neurons and causing the flashes, floaters, and field loss that often bring the patient in.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Uveal melanoma builds its own false vessels: aggressive tumors weave PAS-positive collagen loops and networks (vasculogenic mimicry), and these closed loops are a histologic marker of the worst-prognosis tumors.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The blood's inflammatory balance forecasts the course: a high neutrophil-to-lymphocyte ratio tracks with worse survival in uveal melanoma, and tumor-associated neutrophils help build the niche its liver metastases settle into.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody-like therapy finally moved the needle: tebentafusp, a bispecific gp100-CD3 engager, is the first agent to extend survival in metastatic uveal melanoma, while HMB-45 and Melan-A stains and loss of BAP1 confirm the tumor and predict spread.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Uveal melanoma is uniquely liver-hungry: over 90% of metastases home to the liver, the tumor cells seeding among the hepatocytes, which is why surveillance and liver-directed therapy dominate management of advanced disease.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Advanced disease shows in the red cells: extensive hepatic metastatic burden and its treatment depress erythrocyte production into an anemia, while rising liver enzymes and falling counts together signal progression.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Protons spare the eye: proton-beam radiotherapy and plaque brachytherapy deliver a sharp, contained dose to the ocular tumor while sparing the optic nerve and retina, letting many patients keep the eye instead of losing it to enucleation.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Uveal melanoma can run in families: germline BAP1 mutations transmit a tumor-predisposition syndrome — uveal melanoma with mesothelioma, kidney and skin cancers — so a diagnosis can prompt genetic testing and counseling of relatives.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Hypoxia shapes its spread to the liver: HIF signaling and the angiogenesis it drives help uveal melanoma colonize the liver, its near-exclusive metastatic site, a hypoxic-niche dependence studied as a therapeutic angle.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint drugs barely dent it: unlike cutaneous melanoma, uveal melanoma's low mutation load makes anti-CTLA-4 and anti-PD-1 largely ineffective, which is why the T-cell-redirecting drug tebentafusp, not classic checkpoint blockade, became its breakthrough therapy.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The mutant G-protein feeds growth hubs: GNAQ/GNA11 signaling activates PKC-MAPK and the PI3K-AKT-mTOR axis, so mTOR sits among the downstream nodes targeted to slow a tumor lacking the BRAF mutations that drive skin melanoma.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Its immune infiltrate predicts danger: tumor-infiltrating macrophages and mast cells mark the inflammatory, monosomy-3 uveal melanomas with the worst prognosis, so the immune microenvironment is read as a marker of metastatic risk.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 runs downstream of the driver mutation: GNAQ/GNA11 signaling activates STAT3, which supports uveal melanoma proliferation and immune evasion — one of the hubs explored for therapy in a tumor that resists checkpoint drugs.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB helps it dodge immunity: the inflammatory, monosomy-3 uveal melanomas show NF-κB-driven signaling that shapes their immunosuppressive microenvironment, part of why these tumors respond poorly to standard immunotherapy.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Liver-metastatic disease raises clot risk: like other advanced solid cancers, metastatic uveal melanoma carries tumor-driven hypercoagulability that increases deep-vein thrombosis and pulmonary embolism risk.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Its breakthrough drug ignites one: tebentafusp, the first therapy to extend survival in metastatic uveal melanoma, is a T-cell engager that commonly triggers cytokine release syndrome — fever, hypotension and rash — needing close monitoring early in treatment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Liver replacement and inflammation drag down the count: the near-universal hepatic metastases of advanced uveal melanoma, with their inflammatory burden and crowding of marrow and liver, produce an anemia of chronic disease in progressive cases.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Losing an eye and facing the liver verdict weigh heavily: enucleation or vision loss plus the knowledge that monosomy-3 disease carries a high risk of fatal liver metastasis impose a substantial psychological burden and depression.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Its immunotherapy can trigger autoimmune diabetes: the checkpoint inhibitors and tebentafusp used in metastatic uveal melanoma can unleash autoimmunity against pancreatic islets, causing fulminant insulin-dependent diabetes.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Immune-activating therapy can inflame the heart: checkpoint inhibitors used against metastatic uveal melanoma occasionally cause myocarditis, and tebentafusp's cytokine release stresses the circulation, both routes toward acute heart failure.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Checkpoint immunotherapy can scar the kidneys: the PD-1 and CTLA-4 inhibitors given for advanced uveal melanoma can provoke an immune-mediated interstitial nephritis that, if it recurs, leaves chronic kidney impairment.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It spreads almost only to the liver: uveal melanoma is strikingly hepatotropic, with the great majority of metastases lodging in the liver, so surveillance and treatment centre on hepatic disease.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Enucleation is a healing challenge: removing the eye for a large uveal melanoma and fitting an orbital implant leaves a socket that must heal, and any prior plaque brachytherapy compromises the tissue.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Vision loss and lifelong liver-metastasis surveillance breed worry: the threat of late hepatic spread years after treatment and the loss of an eye foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — After the liver, it favours the lungs: pulmonary metastases are the second commonest site of uveal-melanoma spread, often appearing as nodules years after the primary eye tumour is treated.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It shares a lineage with skin melanoma but differs sharply: oculodermal melanocytosis (nevus of Ota) raises its risk, yet uveal melanoma is driven by GNAQ/GNA11 rather than the BRAF mutations of cutaneous disease.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The eye has no lymphatics, so it cannot spread to nodes: unlike cutaneous melanoma, uveal melanoma disseminates almost purely haematogenously to the liver, which is why sentinel-node biopsy plays no role.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — After liver and lung it seeds bone: skeletal metastases occur in disseminated uveal melanoma, causing painful deposits in the spine and pelvis.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can reach the brain late: brain metastases occur in widely disseminated uveal melanoma, though far less commonly than its dominant liver spread.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its breakthrough drug stresses the circulation: tebentafusp triggers cytokine release with hypotension and fluid shifts, and disseminated disease can rarely involve the heart.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A bispecific T-cell engager extended survival: tebentafusp redirects T cells against the gp100-HLA complex on uveal melanoma, the first therapy to improve survival in this checkpoint-resistant cancer.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Liver-dominant spread disrupts metabolism: uveal melanoma metastasises overwhelmingly to the liver, whose failure in advanced disease deranges glucose and hormone metabolism.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — Ocular masses have infectious mimics: chorioretinitis from toxoplasmosis is among the differentials of a pigmented or inflammatory intraocular lesion that uveal melanoma must be distinguished from.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Unlike skin melanoma, it resists checkpoints: uveal melanoma carries a low mutational burden and an immunosuppressive microenvironment, so PD-1 and CTLA-4 blockade that transforms cutaneous melanoma works poorly — the gap that drove tebentafusp's development.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Largely chemoresistant: conventional cytotoxic chemotherapy such as dacarbazine, of limited use in any melanoma, achieves little in metastatic uveal melanoma, leaving liver-directed and T-cell-redirecting approaches as the mainstays.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It seeds the liver sinusoids: uveal melanoma cells lodge in the hepatic sinusoids and grow within the lobule as micrometastases that can smoulder for years, the reason serial liver MRI surveillance underpins follow-up after the eye is treated.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — An immune-privileged, cold tumour: arising in the immune-privileged eye with a low mutational burden, uveal melanoma rarely forms the germinal-centre-like lymphoid structures that predict checkpoint response, so the TCR-bispecific tebentafusp—not PD-1 blockade—extends survival.
- `connects-to` → **[MDS](../mds/README.md)** — A shared splicing-factor mutation: SF3B1, mutated in a subset of uveal melanomas, is the same spliceosome gene that defines myelodysplastic syndrome with ring sideroblasts—one splicing defect across an eye cancer and a marrow disease.
- `connects-to` → **[HCC](../hcc/README.md)** — Liver-directed therapy unites them: uveal melanoma metastasises almost exclusively to the liver, so like hepatocellular carcinoma it is treated with liver-directed approaches—hepatic perfusion, radioembolization and resection—when disease is liver-confined.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Vasculogenic mimicry: uveal melanoma cells form their own PAS-positive vascular channels that imitate the arterial wall, a pattern predicting metastasis and helping explain its resistance to anti-angiogenic therapy.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Engineered T-cells for cold tumours: uveal melanoma (treated with the gp100 ImmTAC tebentafusp) and synovial sarcoma (treated with NY-ESO-1 TCR cells) both resist checkpoint blockade and instead yield to HLA-restricted redirected T-cells.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — The choroid as a target: uveal melanoma is the commonest primary intraocular tumour in adults, but the choroid is also the commonest site of intraocular metastasis—classically from breast cancer—a key differential.
- `connects-to` → **[CLL](../cll/README.md)** — A shared splicing-factor mutation: SF3B1 mutations recur across uveal melanoma, myelodysplasia and a subset of chronic lymphocytic leukaemia, an unexpected molecular thread linking an eye cancer to blood cancers.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Beyond the liver: while uveal melanoma overwhelmingly metastasises to the liver, the lung is its second site, the tumour seeding the alveolar bed in later disseminated disease.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Late skeletal spread: in advanced uveal melanoma, metastases reach the bone, depositing in the cortical skeleton alongside the dominant hepatic and pulmonary disease.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — BAP1-linked epigenetics: BAP1 loss in high-risk uveal melanoma creates a dependence on EZH2, paralleling the BAP1-EZH2 synthetic lethality seen in mesothelioma.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: cyclin D1 with CDK4/6 propels uveal melanoma proliferation downstream of GNAQ/GNA11-driven MAPK signalling.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Amplified aggression: MYC amplification (chromosome 8q gain) marks high-risk, metastasis-prone uveal melanoma.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — Hepatic tropism: MET (c-Met) signalling drives the striking liver tropism of uveal melanoma metastasis, the dominant and usually fatal site of spread.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Stromal growth: PDGF signalling supports the proliferation and angiogenesis of uveal melanoma, part of its receptor-tyrosine-kinase landscape.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage infiltration: CCL2 recruits tumour-associated macrophages whose abundance, paradoxically, marks the more aggressive uveal melanomas.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — Uveal melanoma rarely mutates TP53 and instead keeps p53 suppressed through high MDM2, making MDM2 inhibitors that reactivate wild-type p53 a rational strategy in a tumor with few other actionable targets and poor response to checkpoint blockade.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on uveal-melanoma cells follows CXCL12 gradients to the liver, explaining the near-exclusive hepatic pattern of metastasis that dominates uveal-melanoma mortality and drives liver-directed therapies.
- `connects-to` → **[AXL receptor](../../03-molecular/axl-receptor/README.md)** — GAS6-AXL signaling promotes the migration and epithelial-mesenchymal-like invasion of uveal melanoma, contributing to the early micrometastatic seeding of the liver that often precedes diagnosis of the primary by years.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The gp100-HLA-A*02/CD3 bispecific tebentafusp—the first therapy to extend survival in metastatic uveal melanoma—redirects cytotoxic T cells to kill tumor cells through perforin and granzyme, despite this tumor's low mutational burden.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Uveal melanoma cells strongly express IGF-1R, and the liver's abundant IGF-1 helps explain the near-exclusive hepatic homing of metastases, making IGF-1R a candidate target against the liver disease that dominates outcome.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Uveal melanoma cells express the endothelin-B receptor inherited from their melanocyte lineage, an EDNRB signaling axis that supports proliferation and survival and is being explored as a therapeutic vulnerability.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Downstream of the GNAQ/GNA11 drivers, PI3K-AKT-mTOR signaling (AKT, mTOR and PTEN already mapped) supports uveal melanoma survival, a targetable axis parallel to its YAP and MAPK arms.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Uveal melanoma characteristically over-expresses anti-apoptotic BCL-2, underlying its resistance to chemotherapy and the long survival of the dormant liver micrometastases that determine its lethality.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling promotes the proliferation and invasive, metastatic phenotype of uveal melanoma, cooperating with the YAP and MAPK arms already mapped downstream of GNAQ/GNA11.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Cyclin-D1 (mapped) and CDK4/6 release E2F1 to drive proliferation downstream of the constitutive GNAQ/GNA11-MAPK signaling of uveal melanoma.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss removes the restraint on the cyclin-D1-CDK4/6 axis and is associated with progression of uveal melanoma.
- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — Loss of E-cadherin and the dedifferentiation accompanying BAP1 loss (mapped) promote the epithelial-mesenchymal-like transition that drives the hepatotropic metastasis of uveal melanoma.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) contributes to the proliferation of uveal melanoma.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT3 signaling (STAT3 already mapped) contributes to the survival and immune-evasion signaling of uveal melanoma.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) supports the survival of uveal-melanoma cells, particularly in the liver microenvironment that is its predominant site of metastasis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING shapes the immune microenvironment of uveal melanoma, a tumor notable for its poor response to checkpoint immunotherapy.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling governs the interferon-driven antitumor response and immune-evasion balance of the immunologically cold uveal melanoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports immune evasion and the hepatic metastatic colonization that determines outcome in uveal melanoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes EMT and the hepatic metastatic niche that dictates the liver-tropic spread of uveal melanoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — PI3K-AKT-mediated FOXO inactivation removes a pro-apoptotic brake, supporting survival of uveal melanoma cells (PI3K-AKT already mapped).
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven cyclin-D1-RB1 cell-cycle entry (cyclin-D1 and RB1 mapped) sustains proliferation in uveal melanoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β acts downstream of the GNAQ/GNA11-PKC-YAP axis, modulating the survival signaling of uveal melanoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the immunosuppressive, immune-cold microenvironment of uveal melanoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the GNAQ/11-activated pathways contributes to the invasion and hepatic-metastatic tropism of uveal melanoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation, alongside BAP1 loss (BAP1 already mapped), of uveal melanoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and dormancy of the hepatic-metastatic cells of uveal melanoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling contributes to the epigenetic dysregulation of uveal melanoma.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of uveal melanoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven myeloid recruitment shapes the immunosuppressive microenvironment of uveal melanoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling downstream of GNAQ/GNA11-PLCβ participates in the oncogenic signaling of uveal melanoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of uveal melanoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of uveal melanoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of uveal melanoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — HLA-restricted immunotherapy: uveal melanoma resists checkpoint blockade, yet the bispecific tebentafusp, the first agent to extend survival, redirects T cells to gp100 presented on HLA, underscoring the central role of antigen presentation in its treatment.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Intact p53 vulnerability: uveal melanoma rarely mutates TP53 and instead suppresses wild-type p53 through MDM2 (already mapped), making pharmacologic p53 reactivation a rational strategy distinct from the mutant-p53 biology of many cancers.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Radiotherapy execution: primary uveal melanoma is controlled by plaque brachytherapy and proton-beam radiation that kill tumour cells via caspase-3-mediated apoptosis, the pathway whose evasion (BCL-2 already mapped) underlies radioresistant relapse.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Tebentafusp immunotherapy: tebentafusp, a gp100-directed T-cell engager, is the first therapy to extend survival in metastatic uveal melanoma (in HLA-A*02:01 patients; MHC class II already mapped), and IL-2-driven T-cell activity underlies the adoptive approaches.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cytokine-release cardiotoxicity: the T-cell-engaging immunotherapy for uveal melanoma can provoke cytokine-release syndrome with hypotension and cardiac stress, and troponin elevation helps detect the myocardial injury of these reactions.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Metastatic anaemia: extensive hepatic metastasis (liver already mapped) and its treatment lower haemoglobin in advanced uveal melanoma, contributing to the fatigue and decline of the metastatic disease that dominates prognosis.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the uveal melanoma microenvironment, favoured by the immune privilege of the eye, dampens the anti-tumour T-cell response (PD-1 and CTLA-4 already mapped), part of the resistance to conventional checkpoint blockade.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF and endothelin-1 (already mapped) shapes the vasculature of uveal melanoma, including the vasculogenic-mimicry networks that are an adverse prognostic feature of the tumour.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: the metabolically active uveal melanoma generates oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species add to the biology of this pigment-cell tumour of the eye.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), and a high macrophage infiltrate is an adverse prognostic feature of uveal melanoma.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Ocular immune privilege: TGF-β in the eye's immune-privileged microenvironment (SMAD4 already mapped) suppresses the anti-tumour response, helping uveal melanoma evade immunity, part of why checkpoint blockade works poorly against it.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia of advanced disease: the hepatic metastatic burden (liver already mapped) and the systemic therapy of advanced uveal melanoma cause anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) and type-2 milieu of the immune-privileged (TGF-β already mapped) microenvironment of uveal melanoma.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Melanocyte metals: zinc supports the enzymes of melanogenesis and the melanocyte function, part of the trace-metal biology (copper already mapped) of the uveal melanocytes from which uveal melanoma arises.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) to add an anaemia of chronic disease to the metastatic-burden anaemia (haemoglobin already mapped) of advanced uveal melanoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metastatic-niche adipokine: leptin, the adipokine of the metabolic microenvironment, signals within the hepatic (liver already mapped) metastatic niche of uveal melanoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is the adipokine of the metabolic milieu of uveal melanoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the uveal-melanoma microenvironment.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antitumour interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of the (immunologically cold) uveal melanoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the tumour-infiltrating T cells (perforin already mapped) is the type-II interferon arm engaged by the tebentafusp (gp100-HLA, MHC already mapped) against uveal melanoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-tumour response of the uveal-melanoma immune microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of uveal melanoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the uveal-melanoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immunologically cold uveal-melanoma microenvironment.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Tertiary lymphoid structures: the B cells and the tertiary lymphoid structures, though scarce in the immunologically cold uveal melanoma, are a candidate correlate of the tebentafusp response.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a contribute to the inflammatory and immunosuppressive dimension of the uveal-melanoma microenvironment and its hepatic (liver already mapped) metastatic niche.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling recruits and polarises the myeloid cells to an immunosuppressive phenotype in the uveal-melanoma microenvironment.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Central complement: the complement C3, upstream of the C5 and C5aR1 (already mapped), is the pivot of the complement activation within the immunosuppressive uveal-melanoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the uveal-melanoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), evading the complement attack in the primary tumour and its hepatic (liver already mapped) metastatic niche.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Tumour iron: transferrin, the iron carrier, supplies the iron demand of the uveal-melanoma cells and their iron-rich hepatic (liver already mapped) metastatic niche.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Stromal alarmin: TSLP released from the uveal-melanoma stromal fibroblasts (already mapped) and choroidal stroma activates mast cells (already mapped) and dendritic cells (already mapped), sustaining the type-2 immunosuppressive microenvironment that blunts cytotoxic immunity.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Tumour anaemia and EPO-R: erythropoietin corrects the anaemia of chronic disease (already mapped) of advanced uveal melanoma, and EPOR expression on choroidal melanocytes has been reported, suggesting possible direct trophic effects on tumour growth.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Invasion ECM scaffold: periostin is upregulated in the uveal-melanoma stromal niche and the hepatic (liver already mapped) metastatic microenvironment, promoting the extracellular matrix remodelling and the invasion of the GNAQ/GNA11-driven melanoma cells.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Intraocular kinin: bradykinin, generated in the choroidal vasculature by kallikrein-kinin activation, amplifies vascular permeability and the inflammatory microenvironment of uveal melanoma, promoting tumour growth and metastatic spread.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement-contact brake: C1-esterase inhibitor restrains the classical complement C1 and the contact system (C3/C5/C5aR1/factor-H already mapped) activated in the uveal-melanoma microenvironment and its hepatic metastatic niche.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Choroidal mast-cell effector: histamine released by mast cells (already mapped) in the choroidal uveal-melanoma stroma amplifies local vascular permeability and the immunosuppressive microenvironment that blunts cytotoxic T-cell surveillance.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — UM melatonin: melatonin suppresses uveal-melanoma proliferation via MT1/MT2 receptor-mediated inhibition of cAMP and mTOR (already mapped) signalling; it also augments NK-cell (already mapped) cytotoxicity against the immunosuppressive uveal-melanoma tumour microenvironment.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — UM testosterone: androgen receptor signalling in uveal melanoma promotes tumour-cell proliferation and survival; testosterone drives the liver (already mapped) metastatic niche via androgen-mediated hepatic immune reprogramming that blunts NK-cell (already mapped) surveillance.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — UM serotonin: serotonin, co-produced by neuroendocrine uveal tissue, acts on 5-HT receptors on uveal melanoma cells driving autocrine proliferative signalling and promotes the liver (already mapped) metastatic niche via serotonin-mediated hepatic immunosuppression.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — UM oxytocin: oxytocin receptor on uveal melanoma cells attenuates GNAQ (already mapped)-driven cAMP/PKA and mTOR (already mapped) oncogenic signalling; oxytocin also enhances NK-cell (already mapped) cytotoxicity against the immune-evading uveal-melanoma microenvironment.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — UM vasopressin: vasopressin V1A receptor on uveal melanoma cells intersects GNAQ (already mapped)/PLC/PKC and mTOR (already mapped) oncogenic axes; V1A-driven calcium-PKC signalling amplifies uveal-melanoma proliferation and immune evasion in the ocular microenvironment.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — UM prolactin: prolactin via JAK2/STAT3 (already mapped) on uveal melanoma cells promotes tumour-cell survival and NF-κB (already mapped)-mediated anti-apoptotic expression; prolactin also modulates the hepatic (already mapped) metastatic niche of uveal melanoma.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — UM selenium: selenoproteins quench ROS from mTOR (already mapped) and VEGF (already mapped) in uveal melanoma; selenium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and impairs T-cytotoxic-cell (already mapped) and macrophage (already mapped) immunity.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — UM iodine: thyroid hormones regulate macrophage (already mapped) and T-cytotoxic-cell (already mapped) anti-tumour surveillance; thyroid deficiency amplifies VEGF (already mapped) and mTOR (already mapped)-driven uveal melanoma growth and NF-κB (already mapped) cascade.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — UM sodium: excess sodium promotes macrophage (already mapped) pro-inflammatory skewing; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) amplify VEGF (already mapped) and mTOR (already mapped) and STAT3 (already mapped)-driven cascade of uveal melanoma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — UM magnesium: magnesium, as mTOR (already mapped) kinase cofactor in macrophages (already mapped) and uveal melanoma cells, supports tumour growth; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of uveal melanoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — UM potassium: potassium efflux from macrophages (already mapped) and uveal melanoma cells drives NLRP3-IL-1β; potassium dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) and mTOR (already mapped) tumour cascade of uveal melanoma.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — UM phosphorus: phosphorus, as ATP precursor in macrophages (already mapped) and T-cytotoxic-cell (already mapped), fuels anti-tumour immunity; phosphorus deficiency amplifies NF-κB (already mapped) and VEGF (already mapped) and mTOR (already mapped) uveal melanoma cascade.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — UM carbon: carbon, as metabolic backbone of VEGF (already mapped) and tumour lipids in macrophages (already mapped) and uveal melanoma cells, drives tumour growth; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of uveal melanoma.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — UM chloride: chloride channels in macrophages (already mapped) and T-cytotoxic-cell (already mapped) modulate tumour-immune homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of uveal melanoma.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — UM hydrogen: hydrogen, via redox homeostasis in macrophages (already mapped) and T-cytotoxic-cell (already mapped), quenches tumour ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and VEGF (already mapped) and mTOR (already mapped) cascade of uveal melanoma.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — UM nitrogen: nitric oxide from macrophages (already mapped) and tumour vasculature modulates angiogenic tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) tumour cascade of uveal melanoma.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — UM sulfur: hydrogen sulfide from macrophages (already mapped) and tumour vasculature modulates angiogenic tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of uveal melanoma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — UM GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and tumour vasculature modulates metabolic angiogenesis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of uveal melanoma.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^nathan-2021-tebentafusp]: Nathan P, Hassel JC, Rutkowski P, et al. Overall survival benefit with tebentafusp in metastatic uveal melanoma. *N Engl J Med.* 2021;385(13):1196-1206. [doi:10.1056/NEJMoa2103485](https://doi.org/10.1056/NEJMoa2103485) · [PubMed 34551229](https://pubmed.ncbi.nlm.nih.gov/34551229/)
[^harbour-2010-bap1-uveal]: Harbour JW, Onken MD, Roberson ED, et al. Frequent mutation of BAP1 in metastasizing uveal melanomas. *Science.* 2010;330(6009):1410-1413. [doi:10.1126/science.1194472](https://doi.org/10.1126/science.1194472) · [PubMed 21051595](https://pubmed.ncbi.nlm.nih.gov/21051595/)
