---
schema: human-scale-entry/v1
id: dlbcl
name: Diffuse Large B-Cell Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common aggressive B-cell lymphoma (30% of NHL); GCB subtype driven by t(14;18)/BCL-2 and BCR-PI3K; ABC subtype by MYD88/CD79B/NF-κB. R-CHOP is frontline; CAR-T (axi-cel, liso-cel) and bispecifics (epcoritamab, glofitamab) are approved in relapsed/refractory DLBCL."
aliases: ["DLBCL", "diffuse large B-cell lymphoma", "DLBCL NOS", "large B-cell lymphoma", "aggressive NHL", "LBCL"]
sources:
  - id: coiffier-2002-rchop
    type: peer-reviewed
    cite: "Coiffier B, Lepage E, Brière J, et al. CHOP chemotherapy plus rituximab compared with CHOP alone in elderly patients with diffuse large-B-cell lymphoma. N Engl J Med. 2002;346(4):235-242."
    doi: "10.1056/NEJMoa011795"
    pmid: "11807147"
    url: "https://doi.org/10.1056/NEJMoa011795"
  - id: neelapu-2017-axicel
    type: peer-reviewed
    cite: "Neelapu SS, Locke FL, Bartlett NL, et al. Axicabtagene ciloleucel CAR T-cell therapy in refractory large B-cell lymphoma. N Engl J Med. 2017;377(26):2531-2544."
    doi: "10.1056/NEJMoa1707447"
    pmid: "29226797"
    url: "https://doi.org/10.1056/NEJMoa1707447"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "ABC-DLBCL is driven by constitutive NF-κB via MYD88 L265P → IRAK4 → BTK and CD79B mutation → BCR-NF-κB; ibrutinib + R-CHOP (PHOENIX trial) failed in unselected DLBCL but active in MYD88-mutant/non-GCB DLBCL; zanubrutinib + R-CHOP in DLBCL under investigation."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "GCB-DLBCL: t(14;18) → BCL-2 overexpression → apoptosis block; venetoclax + R-CHOP (POLARIX data secondary) in BCL-2-high GCB-DLBCL under study; double-hit lymphoma (MYC + BCL-2) → venetoclax + dose-adjusted EPOCH-R; BCL-2 IHC ≥50% correlates with inferior R-CHOP outcome."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC rearrangement in ~10% of DLBCL; MYC + BCL-2 rearrangement = double-hit (HGBL-DH) → R-CHOP inferior; DA-EPOCH-R or consolidative CAR-T preferred; MYC protein >40% by IHC is independent prognostic marker; c-MYC amplification (without rearrangement) has intermediate prognosis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "DLBCL expresses PD-L1 in ~20-40%; pembrolizumab approved for relapsed/refractory primary mediastinal large B-cell lymphoma (PMBCL) — a CD20+/PD-L1-high subtype with 9p24 amplification; PD-1 blockade + rituximab combinations under study in follicular and DLBCL histologies."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2 gain-of-function mutations (Y641F/N, ~20% GCB-DLBCL) silence differentiation genes via H3K27me3; tazemetostat (EZH2i) FDA-approved for R/R follicular lymphoma; EZH2-mutant DLBCL shows activity with tazemetostat+R-CHOP; CREBBP co-mutation reduces tazemetostat sensitivity."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "DLBCL arises from FL transformation (~3%/year); transformed FL-DLBCL shares t(14;18)/BCL-2 and KMT2D with FL but acquires MYC rearrangement, CDKN2A deletion, or TP53 mutation → worse prognosis than de novo DLBCL; CAR-T consolidation is preferred after induction."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 is the essential rituximab target in R-CHOP; CD20 loss (mutation, methylation, shedding) → rituximab resistance; bispecifics (epcoritamab, glofitamab) bind CD3×CD20 at low CD20 expression; CD19-directed ADCs (loncastuximab) and CAR-T are CD20-loss-resistant alternatives."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "DLBCL is a malignancy of mature B cells whose two subtypes mirror the cell of origin: germinal-center B-cell DLBCL carries the germinal center's BCL-2 translocation, while activated B-cell DLBCL resembles a post-germinal-center plasmablast driven by chronic BCR/NF-κB signaling."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Epstein-Barr virus drives a distinct, more aggressive subtype — EBV-positive DLBCL — chiefly in older or immunosuppressed patients; viral LMP1 and EBNA proteins switch on NF-κB to keep the B cell alive, the same mechanism behind post-transplant lymphoproliferative disease."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Distinguishing DLBCL from Burkitt lymphoma is treatment-critical: both are aggressive GC B-cell tumors, but Burkitt has a pure MYC translocation, near-100% Ki-67, and no BCL-2, whereas a MYC-plus-BCL-2 'double-hit' large-cell lymphoma sits between them and does poorly on R-CHOP."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "DLBCL is the endpoint of Richter transformation: in ~5-10% of CLL the indolent clone evolves into aggressive, often clonally-related diffuse large B-cell lymphoma; this transformation, likelier on BTK-inhibitor therapy, links the commonest indolent and aggressive B-cell cancers."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Primary CNS lymphoma is a DLBCL confined to the brain, eyes and CSF: an aggressive activated-B-cell-type lymphoma that, behind the blood-brain barrier, needs high-dose methotrexate-based regimens rather than standard R-CHOP, and is far more common in immunosuppression."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "DLBCL is classified by its germinal-center relationship: the germinal-center B-cell (GCB) subtype, with BCL2/BCL6 rearrangements, has a better prognosis than the activated B-cell (ABC) subtype driven by chronic NF-κB signaling—a cell-of-origin split that guides therapy."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "DLBCL and mantle cell lymphoma are aggressive B-cell non-Hodgkin lymphomas differing at the core: MCL is defined by t(11;14) cyclin D1 overexpression driving cell-cycle escape, while DLBCL is heterogeneous (GCB vs ABC)—both CD20+ and treated with rituximab regimens."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "DLBCL and Hodgkin lymphoma are both germinal-center B-cell lymphomas but diverge: Hodgkin's malignant Reed-Sternberg cells are sparse amid reactive infiltrate and often EBV-driven, while DLBCL is a sheet of malignant B cells—Hodgkin is highly curable, DLBCL in ~60%."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "DLBCL and multiple myeloma are B-lineage cancers at opposite ends of differentiation: myeloma is a plasma-cell tumor flooding marrow and secreting monoclonal immunoglobulin, while DLBCL is a CD20+ lymph-node B-cell tumor—DLBCL can transform to plasmablastic forms."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "DLBCL spans the B-cell-to-plasma-cell transition: the GCB subtype resembles germinal-center B cells while the ABC subtype leans toward plasma-cell differentiation—and the plasmablastic variant nearly resembles a plasma cell, so cell-of-origin shapes prognosis."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV greatly raises DLBCL risk: immunosuppression and EBV co-infection drive aggressive AIDS-related lymphomas, including DLBCL and its plasmablastic variant—so a new mass in an HIV patient prompts lymphoma workup, and antiretroviral therapy is part of treatment."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation marks high-risk DLBCL: loss of p53 function, often with MYC and BCL2 rearrangements (double/triple-hit lymphoma), predicts resistance to R-CHOP and poor survival—so molecular testing now guides intensified or novel therapy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "DLBCL is the most common aggressive lymphoma of the lymphatic system: it usually presents as rapidly enlarging lymph nodes or an extranodal mass, and because it is fast-growing it is paradoxically curable in many with R-CHOP immunochemotherapy."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "DLBCL can involve the bone marrow, worsening prognosis: marrow infiltration upstages the disease and may cause cytopenias, so staging includes marrow assessment—and concordant large-cell marrow involvement portends a worse outcome than discordant low-grade disease."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy complements chemo in localized DLBCL: photon-beam radiation to involved sites consolidates limited-stage disease after abbreviated R-CHOP and treats bulky masses, so it remains part of curative therapy alongside immunochemotherapy and CAR-T for relapse."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "DLBCL is a triumph of T-cell therapy: CD19-directed CAR-T cells re-engineer the patient's cytotoxic T cells to kill the lymphoma, curing many with relapsed disease—so T cells are now a frontline weapon against this most common aggressive lymphoma."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "DLBCL is the commonest extranodal lymphoma of the stomach: it can arise there directly or transform from indolent gastric MALT lymphoma, so a stomach mass or ulcer that is lymphoma, not carcinoma, changes treatment entirely toward chemo-immunotherapy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages shape DLBCL's fate: tumor-associated macrophages and the CD47 'don't-eat-me' signal let lymphoma cells evade clearance, so blocking CD47 to unleash macrophage phagocytosis is an emerging therapeutic strategy."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "The aggressive ABC subtype of DLBCL is addicted to BTK: chronic B-cell-receptor signaling through Bruton's tyrosine kinase keeps NF-κB switched on, so BTK inhibitors like ibrutinib are aimed at this molecular subset of the lymphoma."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "DLBCL can arise in or invade the spleen: primary splenic large B-cell lymphoma and splenic involvement of nodal disease cause massive splenomegaly, so an enlarging spleen with B-symptoms can be the face of this aggressive lymphoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "DLBCL is increasingly attacked with NK-cell therapy: beyond CAR-T against CD19, engineered NK cells and antibodies that engage NK killing are being developed to clear large B-cell lymphoma, harnessing innate cytotoxicity."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "DLBCL can trigger tumor lysis when treated: this fast-growing lymphoma sheds huge numbers of cells under chemotherapy, dumping potassium into the blood, so hyperkalemia must be anticipated and prevented in bulky disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "DLBCL can invade or relapse in the brain: secondary CNS involvement carries a grim prognosis, so high-risk patients receive CNS-directed prophylaxis to reach a sanctuary that standard chemotherapy penetrates poorly."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells shape the immune fight against DLBCL: as antigen-presenters they prime T-cell responses to the lymphoma, and harnessing them is explored to boost immunity alongside CD20 antibodies and CAR-T therapy."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "DLBCL drains the body's iron and blood: marrow involvement and chronic inflammation suppress red-cell production and lock iron away, so anemia commonly accompanies this aggressive lymphoma."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "DLBCL spreads beyond nodes into the liver: as an aggressive lymphoma it seeds extranodal organs, infiltrating the liver to cause hepatomegaly and abnormal liver tests in advanced disease."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "DLBCL shields itself with regulatory T cells: the lymphoma microenvironment recruits Tregs that suppress the antitumor immune response, a factor in prognosis and a barrier for immunotherapy."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "DLBCL's bulky tumor lyses fast on treatment: dying cells spill phosphate and potassium in tumor lysis syndrome, a metabolic emergency at the start of chemotherapy that needs prevention."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "DLBCL has a skin form: primary cutaneous DLBCL, leg type, appears as firm red-brown nodules, and systemic lymphoma can also infiltrate the skin."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "DLBCL can invade the nerves: neurolymphomatosis, infiltration of peripheral nerves and roots, causes painful neuropathy, a rare and aggressive pattern of spread."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows DLBCL's namesake cell: a large lymphoid blast with abundant cytoplasm, dispersed chromatin, and prominent nucleoli — the big, fast-dividing B cell that gives diffuse large B-cell lymphoma its name."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "DLBCL can both infiltrate and overwhelm the kidney: lymphoma deposits enlarge it directly, and as chemotherapy bursts the bulky tumor in tumor lysis syndrome, urate and phosphate crystals clog the tubules into acute failure."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Treating DLBCL swings the calcium: tumor lysis releases a flood of phosphate that binds calcium, dropping it sharply, a metabolic emergency watched for as the rapidly dividing lymphoma dies under therapy."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "DLBCL was the proving ground for antibody therapy: adding rituximab (anti-CD20) to CHOP transformed survival, and bispecific antibodies and CAR-T now rescue relapsed disease — making it a showcase of immunotherapy."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "DLBCL threatens the nervous system twice: high-risk disease seeds the CNS, prompting intrathecal prophylaxis, while the vincristine in R-CHOP poisons peripheral neurons into a dose-limiting neuropathy."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The cure can weaken the heart: doxorubicin — the 'H' (hydroxydaunorubicin) of R-CHOP — is cumulatively cardiotoxic, so cardiac function is checked before treatment and watched for a later cardiomyopathy."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Anthracyclines kill heart muscle cells directly: doxorubicin poisons topoisomerase-2-beta and floods cardiomyocytes with reactive oxygen, causing irreversible cell loss — the cellular basis of the dose-limiting cardiotoxicity, blunted by dexrazoxane."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Rituximab can wake a sleeping virus: by stripping out B cells it lifts the immune control of hepatitis B, so patients are screened and given antiviral prophylaxis before R-CHOP to prevent a dangerous viral reactivation."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The aggressive ABC subtype runs on chronic signaling: alongside constitutive NF-kB, JAK-STAT3 activation drives survival in activated B-cell DLBCL, marking worse-prognosis tumors and a pathway probed by JAK and STAT inhibitors."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF feeds the malignant B cell: the survival cytokine supports DLBCL cells, especially the NF-κB-addicted activated B-cell subtype, one of the microenvironmental lifelines the lymphoma exploits."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "The newest cure can trigger a storm: CD19 CAR-T therapy for relapsed DLBCL routinely sets off cytokine release syndrome as the engineered cells attack, managed with the IL-6 blocker tocilizumab."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T cells fill and shape the tumor: follicular-helper and other T cells in the DLBCL microenvironment can either support or restrain the lymphoma, and the T-cell-rich variants behave and respond differently."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "MYD88 L265P drives the aggressive subtype: this recurrent mutation in activated B-cell DLBCL (and PCNSL) constitutively fires Toll-like/IL-1 signaling into NF-κB, sustaining the tumor and marking a target alongside BTK inhibition."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Chronic autoimmune stimulation can end in DLBCL: the relentless B-cell drive of Sjögren's syndrome and other autoimmune diseases raises lymphoma risk, with marginal-zone lymphomas able to transform into aggressive DLBCL."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "A rare variant lives inside the vessels: intravascular large B-cell lymphoma grows within small-vessel lumens against the endothelium, causing strokes and organ ischemia without forming a mass — a notoriously elusive DLBCL subtype."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "An aggressive lymphoma that clots: DLBCL carries a high venous thromboembolism risk through tumor-driven hypercoagulability, compounded by central venous catheters and the immobility of intensive treatment."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "R-CHOP empties the marrow's defenses: the chemoimmunotherapy that cures most DLBCL causes neutropenia, so febrile neutropenia and sepsis are the leading treatment-related danger."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can seed the central nervous system: high-risk DLBCL spreads to the leptomeninges and brain as secondary CNS lymphoma, a feared relapse that prompts CNS prophylaxis in those at greatest risk."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Anti-CD20 therapy can reactivate it: the rituximab in R-CHOP depletes B cells and can reawaken latent hepatitis B into fulminant hepatitis, so screening and antiviral prophylaxis precede treatment."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its chemoimmunotherapy opens the lung: R-CHOP and especially regimens with steroids deplete T-cell defenses, so Pneumocystis pneumonia is a risk and prophylaxis is given with more intensive DLBCL treatment."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its anthracycline scars the heart: the doxorubicin in R-CHOP is dose-dependently cardiotoxic, leaving some DLBCL survivors with a cardiomyopathy and heart failure that can emerge years later."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Vincristine leaves the nerves raw: the vinca alkaloid in R-CHOP causes a dose-limiting peripheral neuropathy with numbness and neuropathic pain that can persist after DLBCL treatment."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Tumor lysis and methotrexate threaten the kidneys: high cell turnover at DLBCL induction triggers tumor lysis syndrome, and CNS-prophylactic high-dose methotrexate adds nephrotoxicity, risking kidney injury."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An aggressive cancer and its therapy weigh on mood: the diagnosis, intensive immunochemotherapy and fear of relapse in DLBCL contribute to a substantial burden of depression."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It is the commonest lymphoma of the gut: the GI tract is the leading extranodal site for DLBCL, where gastric or intestinal disease causes bleeding, obstruction and a risk of perforation during chemotherapy."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "R-CHOP reawakens shingles: the rituximab and steroids of DLBCL immunochemotherapy deplete B-cell and T-cell immunity, allowing latent varicella-zoster to reactivate, so prophylaxis is given."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An aggressive but curable cancer breeds worry: the urgency of treatment, intensive immunochemotherapy and scan-anxiety over relapse in DLBCL foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its cure can scar the heart: the doxorubicin in R-CHOP causes dose-dependent cardiotoxicity, and mediastinal disease can directly involve the heart and pericardium."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Bulky chest disease obstructs the airway and vessels: primary mediastinal large B-cell lymphoma and bulky mediastinal nodes cause superior vena cava obstruction, airway compression and pleural effusions."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can take over endocrine glands: DLBCL can present as primary thyroid lymphoma or bilateral adrenal lymphoma, the latter causing adrenal insufficiency."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It infiltrates and obstructs the kidney: DLBCL can directly involve the kidneys or block the ureters with bulky retroperitoneal nodes, and tumour lysis at treatment threatens acute kidney injury."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It grows in bone and marrow: DLBCL can present as primary bone lymphoma or infiltrate the marrow, causing pain, fractures and cytopenias."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The testis is a sanctuary site: primary testicular DLBCL is an aggressive form prone to relapse in the contralateral testis and central nervous system, needing prophylaxis."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "R-CHOP is the curative standard: rituximab with CHOP chemotherapy cures about 60% of diffuse large B-cell lymphoma, the backbone of first-line treatment."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "A cure after relapse: CD19-directed CAR-T cells (axicabtagene, tisagenlecleucel) achieve durable remissions in relapsed or refractory DLBCL, now moving into earlier lines."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "Immunodeficiency drives it: HIV markedly raises the risk of diffuse large B-cell lymphoma, an AIDS-defining cancer often EBV-associated, arising as immune surveillance fails."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Antibodies beyond rituximab: polatuzumab vedotin (anti-CD79b ADC), CD20×CD3 bispecifics like epcoritamab, and BTK inhibitors for ABC-subtype DLBCL extend the targeted armamentarium beyond the rituximab that defined R-CHOP."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Some subtypes are checkpoint-sensitive: primary mediastinal and EBV-positive DLBCL carry 9p24 amplification and high PD-L1, responding to checkpoint blockade unlike most other diffuse large B-cell lymphomas."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Its cure can harm the heart: the anthracycline (doxorubicin) in R-CHOP causes dose-dependent cardiomyopathy, so cardiac function is monitored as DLBCL is treated for cure."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Shared MYD88 driver: activated-B-cell DLBCL and Waldenström macroglobulinaemia both carry the MYD88 L265P mutation that switches on NF-κB, making BTK inhibitors active against both."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The commonest extranodal site: DLBCL frequently arises in the gut, infiltrating the stomach and bowel mucosa and risking perforation when chemotherapy rapidly shrinks transmural tumour."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Immunosuppression-associated lymphoma: chronic immune stimulation and methotrexate or biologic therapy in rheumatoid arthritis raise the risk of DLBCL, sometimes EBV-driven and reversible on stopping the drug."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Chronic antigen and lymphoma: hepatitis C drives chronic B-cell stimulation that can transform into DLBCL, a lymphoma that sometimes regresses with antiviral therapy."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Lymphoma in an autoimmune gland: primary thyroid DLBCL arises in long-standing Hashimoto's thyroiditis, presenting as a rapidly enlarging thyroid mass distinct from thyroid carcinoma."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Tumour-lysis nephropathy: the high tumour burden of DLBCL can flood the blood with urate and phosphate at treatment, precipitating in the glomerulus and tubules to cause acute kidney injury."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "From MALT to DLBCL: chronic Helicobacter pylori gastritis drives gastric MALT lymphoma that can transform into gastric DLBCL, with antibiotic eradication regressing early disease."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "Chronic antigen drive: chronic hepatitis C drives sustained B-cell stimulation that can give rise to DLBCL and marginal-zone lymphoma, sometimes regressing with antiviral therapy."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "Recurrent driver: FOXO1 mutations are recurrent in DLBCL, dysregulating this transcription factor's control of survival and differentiation to promote lymphomagenesis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K/AKT survival: chronic active B-cell-receptor signalling activates the PI3K/AKT pathway in DLBCL, sustaining survival and proliferation alongside the NF-κB axis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: cyclin D-CDK4/6 activity propels DLBCL cells through the G1 checkpoint, the proliferative engine downstream of its oncogenic signalling."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Metabolic adaptation: HIF-1α and MYC drive the glycolytic metabolism of the rapidly proliferating DLBCL, supporting growth in the hypoxic lymph-node microenvironment."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "BCR-PI3K signalling: chronic active B-cell-receptor signalling through PI3K sustains the ABC subtype of DLBCL, cooperating with MYD88 and NF-κB activation to drive survival."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomerase immortalisation: TERT activation maintains telomeres in DLBCL cells, granting the limitless replicative capacity that underlies the rapid growth of this aggressive lymphoma."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Tumour macrophages: CCL2 recruits tumour-associated macrophages into the DLBCL microenvironment, whose abundance carries prognostic weight and shapes response to immunochemotherapy."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Autocrine JAK-STAT: autocrine IL-6 and IL-10 signal through JAK-STAT to sustain the ABC subtype of DLBCL, a cytokine survival loop layered on the chronic-active BCR and MYD88-driven NF-κB activation."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Dissemination: CXCR4 on DLBCL cells follows CXCL12 gradients to the bone marrow and central nervous system, the spread that underlies marrow involvement and the feared CNS relapse of high-risk disease."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 restraint: MDM2 keeps wild-type p53 in check in TP53-intact DLBCL, making MDM2 inhibitors a strategy to restore p53-driven apoptosis in this subset of the lymphoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cellular immunotherapy: CD19 CAR-T cells and CD20-CD3 bispecific antibodies redirect cytotoxic T cells to kill DLBCL through perforin and granzyme, transforming the outlook for relapsed and refractory disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-dependent killing: the anti-CD20 antibody rituximab — the R of R-CHOP — kills DLBCL cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex alongside antibody-dependent cellular cytotoxicity."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: R-CHOP chemoimmunotherapy kills DLBCL cells through caspase-3-mediated apoptosis, and the BCL-2-driven apoptotic resistance of double-hit lymphoma underlies its poor response to standard treatment."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K survival: PTEN loss activates the PI3K-AKT pathway (PIK3CA and AKT already mapped), a survival signal particularly active in the germinal-centre-B-cell subtype of DLBCL."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Proliferative output: MYC and the cyclin-D-CDK4/6 axis (MYC and CDK4/6 already mapped) converge to release E2F1, driving the high proliferative rate of DLBCL."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle brake lost: CDKN2A/p16 deletion is a recurrent adverse lesion in DLBCL, removing the restraint on the cyclin-D-CDK4/6 axis and predicting inferior outcome."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "BCR-MAPK proliferation: B-cell-receptor and RAS signalling converge on ERK1/2 MAPK to drive the proliferation of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Checkpoint restraint: the RB1-E2F checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) restrains cell-cycle entry, and its disruption removes a brake on DLBCL proliferation."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Microenvironmental support: IL-6 from the tumour microenvironment signals through STAT3 (already mapped) to support the survival and proliferation of DLBCL cells."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (AKT, PIK3CA and PTEN mapped) downstream of B-cell-receptor signalling drives the proliferation and survival of DLBCL."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports DLBCL-cell survival and contributes to the immunosuppressive tumour microenvironment."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β within the lymphoma microenvironment modulates immune evasion and the stromal niche of DLBCL."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antitumour immune response of DLBCL, relevant to its CAR-T and checkpoint immunotherapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory and immune microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) normally restrains B-cell proliferation, a brake overridden in the lymphomagenesis of DLBCL."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the MYC stability and NF-κB-driven survival signaling of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory tumor microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH-pathway mutations occur in subsets of diffuse large B-cell lymphoma and contribute to its survival and differentiation biology."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LYN) kinase signaling downstream of the chronically active B-cell receptor supports the survival of the ABC subtype of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of diffuse large B-cell lymphoma cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the trafficking and microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microenvironment and stromal interactions of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune escape: DLBCL frequently loses MHC antigen presentation to evade T cells, especially the ABC subtype, and preserved antigen presentation shapes the response to the bispecific-antibody and CAR-T therapies now central to treatment."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell therapies: IL-2-driven T-cell expansion underlies the CD19 CAR-T and CD20xCD3 bispecific therapies (perforin already mapped) that have transformed the treatment of relapsed diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: bulky, rapidly proliferating diffuse large B-cell lymphoma is prone to tumour-lysis syndrome on treatment, releasing purines that xanthine oxidase converts to uric acid, managed with allopurinol or rasburicase."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the doxorubicin in R-CHOP is cardiotoxic, and troponin elevation helps detect the myocardial injury that limits the cumulative anthracycline dose curing diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Marrow involvement and anaemia: bone-marrow infiltration by diffuse large B-cell lymphoma and its immunochemotherapy lower haemoglobin, the anaemia adding to the constitutional symptoms and treatment morbidity of the disease."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Tumour-lysis acidosis: the rapid lysis of bulky diffuse large B-cell lymphoma by chemotherapy releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate and potassium already mapped)."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunosuppressive microenvironment: IL-10 in the lymphoma microenvironment dampens the anti-tumour T-cell response (PD-1 and MHC class II already mapped), part of the immune escape that DLBCL exploits and CAR-T therapy aims to overcome."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Tumour angiogenesis: VEGF-driven angiogenesis supplies the proliferative diffuse large B-cell lymphoma (HIF-1-alpha already mapped), the increased microvascular density part of its aggressive microenvironment."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the pro-tumour niche of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipose niche: the marrow adipocytes and their adipokine leptin engage in crosstalk with the lymphoma cells, part of the bone-marrow (already mapped) microenvironment that can shelter diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow and stromal adipose tissue signals to the lymphoma cells, part of the metabolic microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the metabolic microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate immune microenvironment: type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune tumour microenvironment relevant to the immunotherapy of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: hepcidin, driven by the IL-6 (already mapped) of the lymphoma inflammation, sequesters iron and produces the anaemia of chronic disease (haemoglobin already mapped) of diffuse large B-cell lymphoma."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Double-hit differential: the diffuse large B-cell lymphoma and Burkitt lymphoma (MYC already mapped) overlap in the high-grade double-hit (MYC + BCL2 already mapped) B-cell lymphomas, a key diagnostic distinction."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Richter transformation: the chronic lymphocytic leukaemia can transform to the diffuse large B-cell lymphoma (Richter's syndrome), an aggressive turning point."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Tumour-lysis potassium: the bulky, chemosensitive DLBCL can release the potassium in the tumour-lysis syndrome at induction, a metabolic emergency."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the CAR-T and bispecific (CD20 already mapped) immunotherapy of DLBCL."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the diffuse-large-B-cell-lymphoma microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the diffuse-large-B-cell-lymphoma microenvironment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Rituximab CDC: the complement C5 (with C3 already mapped) is the effector of the complement-dependent cytotoxicity by which the anti-CD20 (already mapped) rituximab of R-CHOP kills the diffuse-large-B-cell-lymphoma cells (B cell already mapped)."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement (C3 and C5 already mapped) to the myeloid inflammation of the diffuse-large-B-cell-lymphoma microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the diffuse-large-B-cell-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the anti-CD20 complement-dependent killing."
---

# Diffuse Large B-Cell Lymphoma

## Overview

**Diffuse Large B-Cell Lymphoma (DLBCL)** is the most common aggressive lymphoma in adults, comprising ~30% of all non-Hodgkin lymphomas (NHL) with ~25,000 new cases per year in the United States. DLBCL is defined histologically by large, diffusely growing B-lymphoid cells that express B-cell markers (CD19, CD20, CD79a, PAX5) and have a proliferative fraction (Ki-67) typically >40%. With standard R-CHOP therapy, approximately 60-70% of patients are cured — a triumph of combined chemo-immunotherapy — but the ~30-40% who relapse have historically had poor outcomes [^coiffier-2002-rchop].

**Epidemiology:**
- Incidence: ~7-8/100,000 per year
- Median age: ~64 years; slight male predominance
- Risk factors: immunosuppression (HIV, organ transplant → PTLD), autoimmune disease (Sjögren's, RA, SLE), EBV infection (EBV+ DLBCL NOS), prior indolent lymphoma transformation (Richter transformation in CLL, transformation of FL)

**Key clinical features:**
- Rapidly growing lymphadenopathy (often weeks); B symptoms (fever, night sweats, weight loss) in ~30%
- Extranodal involvement common: GI tract (most common), CNS, testis, bone marrow, skin
- **Bulky disease** (≥10 cm): Adverse prognosis; consolidative radiotherapy considered
- International Prognostic Index (IPI): Age >60, ECOG PS ≥2, elevated LDH, >1 extranodal site, Ann Arbor stage III-IV → 5-year OS from 37% (high-risk) to 94% (low-risk) with R-CHOP

## Structure

### Molecular classification

**Cell of origin (COO):**
Gene expression profiling (GEP; NanoString-based Lymph2Cx assay) classifies DLBCL into two major subtypes based on differentiation state of the cell of origin:

**GCB (germinal center B-cell, ~50%):**
- Resembles germinal center B cells
- Genomic features: t(14;18)/BCL-2 rearrangement (~30%), EZH2 mutation (~20%), CREBBP mutation (~40%), KMT2D mutation (~30%), SGK1 mutation
- Better prognosis with R-CHOP vs. ABC (5-year OS ~75%)
- BCR-PI3K dependency; relatively lower NF-κB activity

**ABC (activated B-cell, ~30%):**
- Resembles post-germinal center, plasmablastic differentiation stage
- Genomic features: MYD88 L265P (~30%), CD79B mutation (Y196 "ITAM hotspot", ~20%), CARD11 mutation (~10%), TNFAIP3/A20 deletion (~20%)
- Constitutive NF-κB → BCL-XL, FLIP, IRF4 → survival
- Worse prognosis with standard R-CHOP (5-year OS ~55%)
- Potential benefit of BTK inhibition (ibrutinib, zanubrutinib) in MYD88+/CD79B+ dual mutation

**Unclassified (GCB/ABC, ~15-20%):** Intermediate characteristics

**Newly recognized DLBCL entities (WHO 2022 / ICC 2022):**
- **DLBCL, NOS** (not otherwise specified): The majority
- **High-grade B-cell lymphoma with MYC and BCL-2 rearrangements (HGBL-DH):** Double-hit; distinct entity
- **EBV+ DLBCL, NOS:** EBV-driven; older/immunocompromised patients; more aggressive
- **Primary DLBCL of the CNS (PCNSL):** CD10−, BCL-6+, MUM1+; high MYD88; high-dose methotrexate-based regimens
- **Primary mediastinal large B-cell lymphoma (PMBCL):** Mediastinal origin; JAK-STAT and 9p24 amplification → PD-L1 high; pembrolizumab approved

### Genetic landscape

**Most frequently mutated genes in DLBCL NOS:**
- KMT2D (~35%), CREBBP (~30%), DDX3X (~20%), EZH2 (~20%), BCL-2 (~25% rearranged), TP53 (~20%), CD79B (~20%), MYD88 (~30% overall, enriched in ABC), BCL-6 rearrangement (~35% overall)

**MYC biology in DLBCL:**
- MYC rearrangement (Ig-MYC) in ~10% — the IGH-MYC t(8;14) is most common, also IGL-MYC, IGK-MYC
- MYC co-rearrangement with BCL-2: "double-hit" → high-grade B-cell lymphoma (HGBL); HGBL-DH median OS ~6-12 months with R-CHOP → requires intensified or CAR-T approaches
- MYC co-rearrangement with BCL-2 + BCL-6: "triple-hit" (HGBL-TH)
- MYC protein overexpression (without rearrangement) in ~30% of DLBCL (copy number gain, post-transcriptional); intermediate prognostic impact vs. rearranged MYC

## Function

### Normal diffuse large B-cell biology

DLBCL is an aggressive malignancy of mature B cells. The normal equivalents are large germinal center B cells (centroblasts) for GCB-DLBCL and post-GC B cells (plasmablasts) for ABC-DLBCL. GCB-DLBCL bears the imprint of somatic hypermutation, class switch recombination, and t(14;18) — events that normally occur in germinal centers.

### Tumor microenvironment (TME)

**Immune infiltration in DLBCL:**
- **T-cell inflamed (hot) TME:** CD8+ T cells, PD-1+ T cells → associated with higher PD-L1 and potential immunotherapy response; seen more in EBV+ DLBCL and PMBCL
- **Immune-excluded TME:** T cells present but excluded from tumor nests; poor prognosis; common in ABC-DLBCL
- **Immunologically cold TME:** Low lymphocyte infiltration; worst prognosis

**Macrophage polarization:**
- Tumor-associated macrophages (TAMs) in DLBCL; M2-polarized TAMs (CD163+) → immunosuppression; high TAM density correlates with inferior R-CHOP outcome in some analyses
- Lenalidomide + R-CHOP → macrophage repolarization (ROBUST trial for ABC-DLBCL: no significant improvement in primary endpoint but ongoing)

## Pathology

### Diagnosis and staging

**Excisional biopsy required:** Core needle biopsy acceptable if excisional not feasible; fine needle aspirate is insufficient (architectural information needed for subtyping)

**Pathological workup:**
- Morphology: Large lymphoid cells, diffuse pattern, mitoses, necrosis
- Immunohistochemistry: CD20+, CD19+, CD79a+, PAX5+; BCL-2 (% positivity), BCL-6 (GCB marker), CD10 (GCB marker), MUM1/IRF4 (ABC marker), MYC (% positivity)
- FISH: MYC, BCL-2, BCL-6 rearrangements — required to identify HGBL-DH/TH
- COO by GEP or IHC algorithm (Hans algorithm: CD10/BCL-6/MUM1)
- PET/CT for staging (Ann Arbor); Deauville score for response assessment
- Bone marrow biopsy or PET-based marrow assessment

**Response criteria (Lugano 2014):**
- Complete metabolic response (CMR): Deauville 1-3 at end-of-treatment PET
- Partial metabolic response (PMR): Deauville 4-5 with ≥50% decrease in SUV
- Progressive disease (PD): Deauville 4-5 + new lesions

### Treatment

**Frontline (R-CHOP):**
- Rituximab 375 mg/m² + CHOP (cyclophosphamide, doxorubicin, vincristine, prednisone); 6 cycles every 21 days [^coiffier-2002-rchop]
- Cure rate ~60-70% (all-comer DLBCL); 5-year EFS ~55-60%
- **Pola-R-CHP** (polatuzumab vedotin-piiq + R-CHP, without vincristine): POLARIX trial → superior 2-year PFS 76.7% vs. 70.2% for R-CHOP; FDA approved 2023 for previously untreated DLBCL (excluding HGBL); new standard option
- **High-intermediate/high IPI + DLBCL:** CNS prophylaxis with intrathecal or high-dose methotrexate in high-risk anatomic sites (testis, paranasal sinus, epidural, bone marrow)

**Relapsed/Refractory (R/R) DLBCL (≥2nd line):**
- **CAR-T cell therapy:**
  - Axicabtagene ciloleucel (axi-cel, Yescarta): CD19-directed; ZUMA-1 → 52% CR in R/R DLBCL; approved 2017 [^neelapu-2017-axicel]
  - Lisocabtagene maraleucel (liso-cel, Breyanzi): CD19-directed 1:1 CD4:CD8 ratio; TRANSCEND → 53% CR
  - Tisagenlecleucel (tisa-cel, Kymriah): CD19-directed; JULIET → 40% CR
  - **2nd-line CAR-T:** ZUMA-7 (axi-cel) and TRANSFORM (liso-cel) → superior to salvage chemo + ASCT in R/R DLBCL ≤12 months from frontline; EFS benefit → axi-cel now preferred 2nd-line option if early relapse
- **CD20×CD3 bispecific antibodies:**
  - Epcoritamab (subcutaneous): CR 39%; approved for R/R DLBCL (3rd-line+)
  - Glofitamab (obinutuzumab pre-treated): CR 39%; fixed duration; approved 2023
- **Loncastuximab tesirine (Zynlonta):** CD19-directed ADC (PBD warhead); approved for R/R DLBCL
- **Tafasitamab + lenalidomide (L-MIND trial):** CR 43% in transplant-ineligible R/R DLBCL; approved 2020
- **Salvage chemo + ASCT:** R-ICE, R-DHAP, R-ESHAP → if chemosensitive; standard for 2nd-line in late-relapsing (>12 months) fit patients

**Special entities:**
- PCNSL: HD-methotrexate + rituximab induction; consolidation with WBRT or HD-thiotepa-based ASCT; maintenance rituximab
- PMBCL: R-DA-EPOCH (BV-CHP under study); pembrolizumab in R/R PMBCL (approved)
- HGBL-DH: DA-EPOCH-R + venetoclax; or CAR-T consolidation after induction — no definitive superior frontline regimen established

## Connections

- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — ABC-DLBCL is driven by constitutive NF-κB via MYD88 L265P → IRAK4 → BTK and CD79B mutation → BCR-NF-κB; ibrutinib + R-CHOP (PHOENIX trial) failed in unselected DLBCL but active in MYD88-mutant/non-GCB DLBCL; zanubrutinib + R-CHOP in DLBCL under investigation.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — GCB-DLBCL: t(14;18) → BCL-2 overexpression → apoptosis block; venetoclax + R-CHOP (POLARIX data secondary) in BCL-2-high GCB-DLBCL under study; double-hit lymphoma (MYC + BCL-2) → venetoclax + dose-adjusted EPOCH-R; BCL-2 IHC ≥50% correlates with inferior R-CHOP outcome.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC rearrangement in ~10% of DLBCL; MYC + BCL-2 rearrangement = double-hit (HGBL-DH) → R-CHOP inferior; DA-EPOCH-R or consolidative CAR-T preferred; MYC protein >40% by IHC is independent prognostic marker; c-MYC amplification (without rearrangement) has intermediate prognosis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — DLBCL expresses PD-L1 in ~20-40%; pembrolizumab approved for relapsed/refractory primary mediastinal large B-cell lymphoma (PMBCL) — a CD20+/PD-L1-high subtype with 9p24 amplification; PD-1 blockade + rituximab combinations under study in follicular and DLBCL histologies.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2 gain-of-function mutations (Y641F/N, ~20% GCB-DLBCL) silence differentiation genes via H3K27me3; tazemetostat (EZH2i) FDA-approved for R/R follicular lymphoma; EZH2-mutant DLBCL shows activity with tazemetostat+R-CHOP; CREBBP co-mutation reduces tazemetostat sensitivity.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — DLBCL arises from FL transformation (~3%/year); transformed FL-DLBCL shares t(14;18)/BCL-2 and KMT2D with FL but acquires MYC rearrangement, CDKN2A deletion, or TP53 mutation → worse prognosis than de novo DLBCL; CAR-T consolidation is preferred after induction.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 is the essential rituximab target in R-CHOP; CD20 loss (mutation, methylation, shedding) → rituximab resistance; bispecifics (epcoritamab, glofitamab) bind CD3×CD20 at low CD20 expression; CD19-directed ADCs (loncastuximab) and CAR-T are CD20-loss-resistant alternatives.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — DLBCL is a malignancy of mature B cells whose two subtypes mirror the cell of origin: germinal-center B-cell DLBCL carries the germinal center's BCL-2 translocation, while activated B-cell DLBCL resembles a post-germinal-center plasmablast driven by chronic BCR/NF-κB signaling.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Epstein-Barr virus drives a distinct, more aggressive subtype — EBV-positive DLBCL — chiefly in older or immunosuppressed patients; viral LMP1 and EBNA proteins switch on NF-κB to keep the B cell alive, the same mechanism behind post-transplant lymphoproliferative disease.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Distinguishing DLBCL from Burkitt lymphoma is treatment-critical: both are aggressive GC B-cell tumors, but Burkitt has a pure MYC translocation, near-100% Ki-67, and no BCL-2, whereas a MYC-plus-BCL-2 'double-hit' large-cell lymphoma sits between them and does poorly on R-CHOP.
- `connects-to` → **[CLL](../cll/README.md)** — DLBCL is the endpoint of Richter transformation: in ~5-10% of CLL the indolent clone evolves into aggressive, often clonally-related diffuse large B-cell lymphoma; this transformation, likelier on BTK-inhibitor therapy, links the commonest indolent and aggressive B-cell cancers.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Primary CNS lymphoma is a DLBCL confined to the brain, eyes and CSF: an aggressive activated-B-cell-type lymphoma that, behind the blood-brain barrier, needs high-dose methotrexate-based regimens rather than standard R-CHOP, and is far more common in immunosuppression.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — DLBCL is classified by its germinal-center relationship: the germinal-center B-cell (GCB) subtype, with BCL2/BCL6 rearrangements, has a better prognosis than the activated B-cell (ABC) subtype driven by chronic NF-κB signaling—a cell-of-origin split that guides therapy.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — DLBCL and mantle cell lymphoma are aggressive B-cell non-Hodgkin lymphomas differing at the core: MCL is defined by t(11;14) cyclin D1 overexpression driving cell-cycle escape, while DLBCL is heterogeneous (GCB vs ABC)—both CD20+ and treated with rituximab regimens.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — DLBCL and Hodgkin lymphoma are both germinal-center B-cell lymphomas but diverge: Hodgkin's malignant Reed-Sternberg cells are sparse amid reactive infiltrate and often EBV-driven, while DLBCL is a sheet of malignant B cells—Hodgkin is highly curable, DLBCL in ~60%.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — DLBCL and multiple myeloma are B-lineage cancers at opposite ends of differentiation: myeloma is a plasma-cell tumor flooding marrow and secreting monoclonal immunoglobulin, while DLBCL is a CD20+ lymph-node B-cell tumor—DLBCL can transform to plasmablastic forms.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — DLBCL spans the B-cell-to-plasma-cell transition: the GCB subtype resembles germinal-center B cells while the ABC subtype leans toward plasma-cell differentiation—and the plasmablastic variant nearly resembles a plasma cell, so cell-of-origin shapes prognosis.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV greatly raises DLBCL risk: immunosuppression and EBV co-infection drive aggressive AIDS-related lymphomas, including DLBCL and its plasmablastic variant—so a new mass in an HIV patient prompts lymphoma workup, and antiretroviral therapy is part of treatment.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation marks high-risk DLBCL: loss of p53 function, often with MYC and BCL2 rearrangements (double/triple-hit lymphoma), predicts resistance to R-CHOP and poor survival—so molecular testing now guides intensified or novel therapy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — DLBCL is the most common aggressive lymphoma of the lymphatic system: it usually presents as rapidly enlarging lymph nodes or an extranodal mass, and because it is fast-growing it is paradoxically curable in many with R-CHOP immunochemotherapy.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — DLBCL can involve the bone marrow, worsening prognosis: marrow infiltration upstages the disease and may cause cytopenias, so staging includes marrow assessment—and concordant large-cell marrow involvement portends a worse outcome than discordant low-grade disease.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy complements chemo in localized DLBCL: photon-beam radiation to involved sites consolidates limited-stage disease after abbreviated R-CHOP and treats bulky masses, so it remains part of curative therapy alongside immunochemotherapy and CAR-T for relapse.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — DLBCL is a triumph of T-cell therapy: CD19-directed CAR-T cells re-engineer the patient's cytotoxic T cells to kill the lymphoma, curing many with relapsed disease—so T cells are now a frontline weapon against this most common aggressive lymphoma.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — DLBCL is the commonest extranodal lymphoma of the stomach: it can arise there directly or transform from indolent gastric MALT lymphoma, so a stomach mass or ulcer that is lymphoma, not carcinoma, changes treatment entirely toward chemo-immunotherapy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages shape DLBCL's fate: tumor-associated macrophages and the CD47 'don't-eat-me' signal let lymphoma cells evade clearance, so blocking CD47 to unleash macrophage phagocytosis is an emerging therapeutic strategy.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — The aggressive ABC subtype of DLBCL is addicted to BTK: chronic B-cell-receptor signaling through Bruton's tyrosine kinase keeps NF-κB switched on, so BTK inhibitors like ibrutinib are aimed at this molecular subset of the lymphoma.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — DLBCL can arise in or invade the spleen: primary splenic large B-cell lymphoma and splenic involvement of nodal disease cause massive splenomegaly, so an enlarging spleen with B-symptoms can be the face of this aggressive lymphoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — DLBCL is increasingly attacked with NK-cell therapy: beyond CAR-T against CD19, engineered NK cells and antibodies that engage NK killing are being developed to clear large B-cell lymphoma, harnessing innate cytotoxicity.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — DLBCL can trigger tumor lysis when treated: this fast-growing lymphoma sheds huge numbers of cells under chemotherapy, dumping potassium into the blood, so hyperkalemia must be anticipated and prevented in bulky disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — DLBCL can invade or relapse in the brain: secondary CNS involvement carries a grim prognosis, so high-risk patients receive CNS-directed prophylaxis to reach a sanctuary that standard chemotherapy penetrates poorly.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells shape the immune fight against DLBCL: as antigen-presenters they prime T-cell responses to the lymphoma, and harnessing them is explored to boost immunity alongside CD20 antibodies and CAR-T therapy.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — DLBCL drains the body's iron and blood: marrow involvement and chronic inflammation suppress red-cell production and lock iron away, so anemia commonly accompanies this aggressive lymphoma.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — DLBCL spreads beyond nodes into the liver: as an aggressive lymphoma it seeds extranodal organs, infiltrating the liver to cause hepatomegaly and abnormal liver tests in advanced disease.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — DLBCL shields itself with regulatory T cells: the lymphoma microenvironment recruits Tregs that suppress the antitumor immune response, a factor in prognosis and a barrier for immunotherapy.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — DLBCL's bulky tumor lyses fast on treatment: dying cells spill phosphate and potassium in tumor lysis syndrome, a metabolic emergency at the start of chemotherapy that needs prevention.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — DLBCL has a skin form: primary cutaneous DLBCL, leg type, appears as firm red-brown nodules, and systemic lymphoma can also infiltrate the skin.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — DLBCL can invade the nerves: neurolymphomatosis, infiltration of peripheral nerves and roots, causes painful neuropathy, a rare and aggressive pattern of spread.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows DLBCL's namesake cell: a large lymphoid blast with abundant cytoplasm, dispersed chromatin, and prominent nucleoli — the big, fast-dividing B cell that gives diffuse large B-cell lymphoma its name.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — DLBCL can both infiltrate and overwhelm the kidney: lymphoma deposits enlarge it directly, and as chemotherapy bursts the bulky tumor in tumor lysis syndrome, urate and phosphate crystals clog the tubules into acute failure.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Treating DLBCL swings the calcium: tumor lysis releases a flood of phosphate that binds calcium, dropping it sharply, a metabolic emergency watched for as the rapidly dividing lymphoma dies under therapy.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — DLBCL was the proving ground for antibody therapy: adding rituximab (anti-CD20) to CHOP transformed survival, and bispecific antibodies and CAR-T now rescue relapsed disease — making it a showcase of immunotherapy.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — DLBCL threatens the nervous system twice: high-risk disease seeds the CNS, prompting intrathecal prophylaxis, while the vincristine in R-CHOP poisons peripheral neurons into a dose-limiting neuropathy.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The cure can weaken the heart: doxorubicin — the 'H' (hydroxydaunorubicin) of R-CHOP — is cumulatively cardiotoxic, so cardiac function is checked before treatment and watched for a later cardiomyopathy.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Anthracyclines kill heart muscle cells directly: doxorubicin poisons topoisomerase-2-beta and floods cardiomyocytes with reactive oxygen, causing irreversible cell loss — the cellular basis of the dose-limiting cardiotoxicity, blunted by dexrazoxane.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Rituximab can wake a sleeping virus: by stripping out B cells it lifts the immune control of hepatitis B, so patients are screened and given antiviral prophylaxis before R-CHOP to prevent a dangerous viral reactivation.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The aggressive ABC subtype runs on chronic signaling: alongside constitutive NF-kB, JAK-STAT3 activation drives survival in activated B-cell DLBCL, marking worse-prognosis tumors and a pathway probed by JAK and STAT inhibitors.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF feeds the malignant B cell: the survival cytokine supports DLBCL cells, especially the NF-κB-addicted activated B-cell subtype, one of the microenvironmental lifelines the lymphoma exploits.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — The newest cure can trigger a storm: CD19 CAR-T therapy for relapsed DLBCL routinely sets off cytokine release syndrome as the engineered cells attack, managed with the IL-6 blocker tocilizumab.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T cells fill and shape the tumor: follicular-helper and other T cells in the DLBCL microenvironment can either support or restrain the lymphoma, and the T-cell-rich variants behave and respond differently.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — MYD88 L265P drives the aggressive subtype: this recurrent mutation in activated B-cell DLBCL (and PCNSL) constitutively fires Toll-like/IL-1 signaling into NF-κB, sustaining the tumor and marking a target alongside BTK inhibition.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Chronic autoimmune stimulation can end in DLBCL: the relentless B-cell drive of Sjögren's syndrome and other autoimmune diseases raises lymphoma risk, with marginal-zone lymphomas able to transform into aggressive DLBCL.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — A rare variant lives inside the vessels: intravascular large B-cell lymphoma grows within small-vessel lumens against the endothelium, causing strokes and organ ischemia without forming a mass — a notoriously elusive DLBCL subtype.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — An aggressive lymphoma that clots: DLBCL carries a high venous thromboembolism risk through tumor-driven hypercoagulability, compounded by central venous catheters and the immobility of intensive treatment.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — R-CHOP empties the marrow's defenses: the chemoimmunotherapy that cures most DLBCL causes neutropenia, so febrile neutropenia and sepsis are the leading treatment-related danger.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can seed the central nervous system: high-risk DLBCL spreads to the leptomeninges and brain as secondary CNS lymphoma, a feared relapse that prompts CNS prophylaxis in those at greatest risk.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Anti-CD20 therapy can reactivate it: the rituximab in R-CHOP depletes B cells and can reawaken latent hepatitis B into fulminant hepatitis, so screening and antiviral prophylaxis precede treatment.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its chemoimmunotherapy opens the lung: R-CHOP and especially regimens with steroids deplete T-cell defenses, so Pneumocystis pneumonia is a risk and prophylaxis is given with more intensive DLBCL treatment.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its anthracycline scars the heart: the doxorubicin in R-CHOP is dose-dependently cardiotoxic, leaving some DLBCL survivors with a cardiomyopathy and heart failure that can emerge years later.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Vincristine leaves the nerves raw: the vinca alkaloid in R-CHOP causes a dose-limiting peripheral neuropathy with numbness and neuropathic pain that can persist after DLBCL treatment.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Tumor lysis and methotrexate threaten the kidneys: high cell turnover at DLBCL induction triggers tumor lysis syndrome, and CNS-prophylactic high-dose methotrexate adds nephrotoxicity, risking kidney injury.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An aggressive cancer and its therapy weigh on mood: the diagnosis, intensive immunochemotherapy and fear of relapse in DLBCL contribute to a substantial burden of depression.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It is the commonest lymphoma of the gut: the GI tract is the leading extranodal site for DLBCL, where gastric or intestinal disease causes bleeding, obstruction and a risk of perforation during chemotherapy.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — R-CHOP reawakens shingles: the rituximab and steroids of DLBCL immunochemotherapy deplete B-cell and T-cell immunity, allowing latent varicella-zoster to reactivate, so prophylaxis is given.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An aggressive but curable cancer breeds worry: the urgency of treatment, intensive immunochemotherapy and scan-anxiety over relapse in DLBCL foster chronic health anxiety alongside depression.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its cure can scar the heart: the doxorubicin in R-CHOP causes dose-dependent cardiotoxicity, and mediastinal disease can directly involve the heart and pericardium.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Bulky chest disease obstructs the airway and vessels: primary mediastinal large B-cell lymphoma and bulky mediastinal nodes cause superior vena cava obstruction, airway compression and pleural effusions.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can take over endocrine glands: DLBCL can present as primary thyroid lymphoma or bilateral adrenal lymphoma, the latter causing adrenal insufficiency.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It infiltrates and obstructs the kidney: DLBCL can directly involve the kidneys or block the ureters with bulky retroperitoneal nodes, and tumour lysis at treatment threatens acute kidney injury.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It grows in bone and marrow: DLBCL can present as primary bone lymphoma or infiltrate the marrow, causing pain, fractures and cytopenias.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The testis is a sanctuary site: primary testicular DLBCL is an aggressive form prone to relapse in the contralateral testis and central nervous system, needing prophylaxis.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — R-CHOP is the curative standard: rituximab with CHOP chemotherapy cures about 60% of diffuse large B-cell lymphoma, the backbone of first-line treatment.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — A cure after relapse: CD19-directed CAR-T cells (axicabtagene, tisagenlecleucel) achieve durable remissions in relapsed or refractory DLBCL, now moving into earlier lines.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — Immunodeficiency drives it: HIV markedly raises the risk of diffuse large B-cell lymphoma, an AIDS-defining cancer often EBV-associated, arising as immune surveillance fails.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Antibodies beyond rituximab: polatuzumab vedotin (anti-CD79b ADC), CD20×CD3 bispecifics like epcoritamab, and BTK inhibitors for ABC-subtype DLBCL extend the targeted armamentarium beyond the rituximab that defined R-CHOP.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Some subtypes are checkpoint-sensitive: primary mediastinal and EBV-positive DLBCL carry 9p24 amplification and high PD-L1, responding to checkpoint blockade unlike most other diffuse large B-cell lymphomas.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Its cure can harm the heart: the anthracycline (doxorubicin) in R-CHOP causes dose-dependent cardiomyopathy, so cardiac function is monitored as DLBCL is treated for cure.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Shared MYD88 driver: activated-B-cell DLBCL and Waldenström macroglobulinaemia both carry the MYD88 L265P mutation that switches on NF-κB, making BTK inhibitors active against both.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The commonest extranodal site: DLBCL frequently arises in the gut, infiltrating the stomach and bowel mucosa and risking perforation when chemotherapy rapidly shrinks transmural tumour.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Immunosuppression-associated lymphoma: chronic immune stimulation and methotrexate or biologic therapy in rheumatoid arthritis raise the risk of DLBCL, sometimes EBV-driven and reversible on stopping the drug.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Chronic antigen and lymphoma: hepatitis C drives chronic B-cell stimulation that can transform into DLBCL, a lymphoma that sometimes regresses with antiviral therapy.
- `connects-to` → **[Thyroid](../../06-organ/thyroid/README.md)** — Lymphoma in an autoimmune gland: primary thyroid DLBCL arises in long-standing Hashimoto's thyroiditis, presenting as a rapidly enlarging thyroid mass distinct from thyroid carcinoma.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Tumour-lysis nephropathy: the high tumour burden of DLBCL can flood the blood with urate and phosphate at treatment, precipitating in the glomerulus and tubules to cause acute kidney injury.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — From MALT to DLBCL: chronic Helicobacter pylori gastritis drives gastric MALT lymphoma that can transform into gastric DLBCL, with antibiotic eradication regressing early disease.
- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — Chronic antigen drive: chronic hepatitis C drives sustained B-cell stimulation that can give rise to DLBCL and marginal-zone lymphoma, sometimes regressing with antiviral therapy.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — Recurrent driver: FOXO1 mutations are recurrent in DLBCL, dysregulating this transcription factor's control of survival and differentiation to promote lymphomagenesis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K/AKT survival: chronic active B-cell-receptor signalling activates the PI3K/AKT pathway in DLBCL, sustaining survival and proliferation alongside the NF-κB axis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: cyclin D-CDK4/6 activity propels DLBCL cells through the G1 checkpoint, the proliferative engine downstream of its oncogenic signalling.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Metabolic adaptation: HIF-1α and MYC drive the glycolytic metabolism of the rapidly proliferating DLBCL, supporting growth in the hypoxic lymph-node microenvironment.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — BCR-PI3K signalling: chronic active B-cell-receptor signalling through PI3K sustains the ABC subtype of DLBCL, cooperating with MYD88 and NF-κB activation to drive survival.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Telomerase immortalisation: TERT activation maintains telomeres in DLBCL cells, granting the limitless replicative capacity that underlies the rapid growth of this aggressive lymphoma.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Tumour macrophages: CCL2 recruits tumour-associated macrophages into the DLBCL microenvironment, whose abundance carries prognostic weight and shapes response to immunochemotherapy.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Autocrine IL-6 and IL-10 signal through JAK-STAT to sustain the ABC subtype of DLBCL, a cytokine survival loop layered on the chronic-active B-cell-receptor and MYD88-driven NF-κB activation of that subtype.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCR4 on DLBCL cells follows CXCL12 gradients to the bone marrow and central nervous system, the spread that underlies marrow involvement and the feared CNS relapse that prophylaxis aims to prevent.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2 keeps wild-type p53 in check in TP53-intact DLBCL, making MDM2 inhibitors that reactivate p53 a strategy to restore apoptosis in the subset of cases without TP53 mutation.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD19 CAR-T cells and CD20-CD3 bispecific antibodies redirect cytotoxic T cells to kill DLBCL through perforin and granzyme, transforming the outlook for relapsed and refractory disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — The anti-CD20 antibody rituximab—the R of R-CHOP—kills DLBCL cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex alongside antibody-dependent cellular cytotoxicity.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — R-CHOP chemoimmunotherapy kills DLBCL cells through caspase-3-mediated apoptosis, and the BCL-2-driven apoptotic resistance of double-hit lymphoma underlies its poor response to standard treatment.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K-AKT-mTOR signaling (AKT, PIK3CA and PTEN mapped) downstream of B-cell-receptor signaling drives the proliferation and survival of DLBCL.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports DLBCL-cell survival and contributes to the immunosuppressive tumor microenvironment.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β within the lymphoma microenvironment modulates immune evasion and the stromal niche of DLBCL.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss activates the PI3K-AKT pathway (PIK3CA and AKT already mapped), a survival signal particularly active in the germinal-center-B-cell subtype of DLBCL.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — MYC and the cyclin-D-CDK4/6 axis (MYC and CDK4/6 already mapped) converge to release E2F1, driving the high proliferative rate of DLBCL.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/p16 deletion is a recurrent adverse lesion in DLBCL, removing the restraint on the cyclin-D-CDK4/6 axis and predicting inferior outcome.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — B-cell-receptor and RAS signaling converge on ERK1/2 MAPK to drive the proliferation of diffuse large B-cell lymphoma.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (E2F1, CDK4/6 and CDKN2A already mapped) restrains cell-cycle entry, and its disruption removes a brake on DLBCL proliferation.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 from the tumor microenvironment signals through STAT3 (already mapped) to support the survival and proliferation of DLBCL cells.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antitumor immune response of DLBCL, relevant to its CAR-T and checkpoint immunotherapy.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory and immune microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) normally restrains B-cell proliferation, a brake overridden in the lymphomagenesis of DLBCL.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the MYC stability and NF-κB-driven survival signaling of diffuse large B-cell lymphoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory tumor microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH-pathway mutations occur in subsets of diffuse large B-cell lymphoma and contribute to its survival and differentiation biology.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LYN) kinase signaling downstream of the chronically active B-cell receptor supports the survival of the ABC subtype of diffuse large B-cell lymphoma.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of diffuse large B-cell lymphoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of diffuse large B-cell lymphoma cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of diffuse large B-cell lymphoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the trafficking and microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of diffuse large B-cell lymphoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of diffuse large B-cell lymphoma.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microenvironment and stromal interactions of diffuse large B-cell lymphoma.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune escape: DLBCL frequently loses MHC antigen presentation to evade T cells, especially the ABC subtype, and preserved antigen presentation shapes the response to the bispecific-antibody and CAR-T therapies now central to treatment.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell therapies: IL-2-driven T-cell expansion underlies the CD19 CAR-T and CD20xCD3 bispecific therapies (perforin already mapped) that have transformed the treatment of relapsed diffuse large B-cell lymphoma.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: bulky, rapidly proliferating diffuse large B-cell lymphoma is prone to tumour-lysis syndrome on treatment, releasing purines that xanthine oxidase converts to uric acid, managed with allopurinol or rasburicase.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the doxorubicin in R-CHOP is cardiotoxic, and troponin elevation helps detect the myocardial injury that limits the cumulative anthracycline dose curing diffuse large B-cell lymphoma.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Marrow involvement and anaemia: bone-marrow infiltration by diffuse large B-cell lymphoma and its immunochemotherapy lower haemoglobin, the anaemia adding to the constitutional symptoms and treatment morbidity of the disease.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Tumour-lysis acidosis: the rapid lysis of bulky diffuse large B-cell lymphoma by chemotherapy releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate and potassium already mapped).
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunosuppressive microenvironment: IL-10 in the lymphoma microenvironment dampens the anti-tumour T-cell response (PD-1 and MHC class II already mapped), part of the immune escape that DLBCL exploits and CAR-T therapy aims to overcome.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Tumour angiogenesis: VEGF-driven angiogenesis supplies the proliferative diffuse large B-cell lymphoma (HIF-1-alpha already mapped), the increased microvascular density part of its aggressive microenvironment.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage polarisation: IL-4 polarises the tumour-associated macrophages toward an immunosuppressive M2 phenotype (IL-10 already mapped), part of the pro-tumour niche of diffuse large B-cell lymphoma.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), supports the M2 macrophage and type-2 milieu of the immunosuppressive microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipose niche: the marrow adipocytes and their adipokine leptin engage in crosstalk with the lymphoma cells, part of the bone-marrow (already mapped) microenvironment that can shelter diffuse large B-cell lymphoma.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow and stromal adipose tissue signals to the lymphoma cells, part of the metabolic microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the metabolic microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate immune microenvironment: type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune tumour microenvironment relevant to the immunotherapy of diffuse large B-cell lymphoma.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: hepcidin, driven by the IL-6 (already mapped) of the lymphoma inflammation, sequesters iron and produces the anaemia of chronic disease (haemoglobin already mapped) of diffuse large B-cell lymphoma.
- `connects-to` → **[Burkitt lymphoma](../burkitt-lymphoma/README.md)** — Double-hit differential: the diffuse large B-cell lymphoma and Burkitt lymphoma (MYC already mapped) overlap in the high-grade double-hit (MYC + BCL2 already mapped) B-cell lymphomas, a key diagnostic distinction.
- `connects-to` → **[CLL](../cll/README.md)** — Richter transformation: the chronic lymphocytic leukaemia can transform to the diffuse large B-cell lymphoma (Richter's syndrome), an aggressive turning point.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Tumour-lysis potassium: the bulky, chemosensitive DLBCL can release the potassium in the tumour-lysis syndrome at induction, a metabolic emergency.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the T cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the CAR-T and bispecific (CD20 already mapped) immunotherapy of DLBCL.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the diffuse-large-B-cell-lymphoma microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the diffuse-large-B-cell-lymphoma microenvironment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Stromal mast cells: the mast cells of the tumour stroma contribute to the angiogenesis (VEGF already mapped) and the type-2 microenvironment of diffuse large B-cell lymphoma.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Rituximab CDC: the complement C5 (with C3 already mapped) is the effector of the complement-dependent cytotoxicity by which the anti-CD20 (already mapped) rituximab of R-CHOP kills the diffuse-large-B-cell-lymphoma cells (B cell already mapped).
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement (C3 and C5 already mapped) to the myeloid inflammation of the diffuse-large-B-cell-lymphoma microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the diffuse-large-B-cell-lymphoma cells recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), a resistance mechanism to the anti-CD20 complement-dependent killing.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^coiffier-2002-rchop]: Coiffier B, Lepage E, Brière J, et al. CHOP chemotherapy plus rituximab compared with CHOP alone in elderly patients with diffuse large-B-cell lymphoma. *N Engl J Med.* 2002;346(4):235-242. [doi:10.1056/NEJMoa011795](https://doi.org/10.1056/NEJMoa011795) · [PubMed 11807147](https://pubmed.ncbi.nlm.nih.gov/11807147/)
[^neelapu-2017-axicel]: Neelapu SS, Locke FL, Bartlett NL, et al. Axicabtagene ciloleucel CAR T-cell therapy in refractory large B-cell lymphoma. *N Engl J Med.* 2017;377(26):2531-2544. [doi:10.1056/NEJMoa1707447](https://doi.org/10.1056/NEJMoa1707447) · [PubMed 29226797](https://pubmed.ncbi.nlm.nih.gov/29226797/)
