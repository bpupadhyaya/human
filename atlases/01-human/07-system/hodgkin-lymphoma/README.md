---
schema: human-scale-entry/v1
id: hodgkin-lymphoma
name: Hodgkin Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Hodgkin lymphoma is a GC B cell-derived malignancy; RS cells ~100% CD30+; 9p24.1 amplification drives CD30+PD-L1/L2 co-expression; A+AVD (ECHELON-1) is standard for advanced stage; nivolumab/pembrolizumab for R/R; 5-year OS >85% overall; NLPHL has distinct CD20+ biology."
aliases: ["Hodgkin lymphoma", "HL", "cHL", "classical Hodgkin lymphoma", "NLPHL", "Reed-Sternberg", "Hodgkin disease", "nodular sclerosis HL", "mixed cellularity HL"]
sources:
  - id: connors-2018-echelon1
    type: peer-reviewed
    cite: "Connors JM, Jurczak W, Straus DJ, et al. Brentuximab vedotin with chemotherapy for stage III or IV Hodgkin's lymphoma. N Engl J Med. 2018;378(4):331-344."
    doi: "10.1056/NEJMoa1708984"
    pmid: "29360494"
    url: "https://doi.org/10.1056/NEJMoa1708984"
  - id: armand-2018-nivo-hl
    type: peer-reviewed
    cite: "Armand P, Engert A, Younes A, et al. Nivolumab for relapsed/refractory classic Hodgkin lymphoma after failure of autologous hematopoietic cell transplantation: extended follow-up of the multicohort single-arm phase II CheckMate 205 trial. J Clin Oncol. 2018;36(14):1428-1439."
    doi: "10.1200/JCO.2017.77.6717"
    pmid: "29584546"
    url: "https://doi.org/10.1200/JCO.2017.77.6717"
cross_links:
  - target: 01-human/03-molecular/cd30
    relation: connects-to
    note: "CD30 is expressed on ~100% of RS cells (WHO diagnostic criterion for cHL); brentuximab vedotin is the backbone of A+AVD (ECHELON-1) and consolidation post-auto-SCT (AETHERA); 9p24.1 amplification co-amplifies CD30 with PD-L1/PD-L2 in RS cells."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "9p24.1 amplification in RS cells drives PD-L1/PD-L2 overexpression → profound T-cell exhaustion in tumor microenvironment; nivolumab (CheckMate 205) and pembrolizumab (KEYNOTE-087) show ORR ~65-70% in R/R cHL; KEYNOTE-204 (pembrolizumab vs BV): PFS 13.2 vs 8.3 months."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB is constitutively active in RS cells via CD30, CD40, EBV-LMP1, and CARD11 signaling; NF-κB drives RS cell survival by upregulating BCL-2, BCL-XL, and cFLIP; microenvironmental TNF-α further activates NF-κB; NF-κB inhibition is a preclinical therapeutic target in R/R cHL."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "9p24.1 amplification co-amplifies JAK2 with PD-L1/PD-L2 and CD30 in RS cells; JAK2 → constitutive STAT6 → IL-13 autocrine + PD-L1 transcription; ruxolitinib studied in R/R cHL; JAK2 amplification is a primary oncogenic driver in cHL."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Reed-Sternberg cells arise from germinal-center B cells that acquired crippling Ig V-gene mutations and should have died during negative selection; they survive via CD30/CD40/NF-κB and EBV rescue while shedding the B-cell program (no surface Ig, loss of OCT2/BOB1)."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "EBV is found in 30-50% of classical HL (up to 80-90% in lymphocyte-depleted and HIV-associated cases); its LMP1 protein mimics a constitutively active CD40 receptor → NF-κB survival signaling in RS cells; prior infectious mononucleosis roughly triples HL risk."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 status splits Hodgkin lymphoma: RS cells of classical HL are CD20-negative, whereas the popcorn (L&H) cells of NLPHL retain the B-cell program and are CD20-positive — making rituximab effective in NLPHL but not classical HL."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Hodgkin lymphoma is unusual: malignant Reed-Sternberg cells are <1% of the tumor, the bulk being reactive CD4+ T cells (rosetting around RS cells), eosinophils, and histiocytes that RS cells recruit and depend on — why PD-1 blockade freeing exhausted T cells works so well."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is a key Hodgkin lymphoma site: classical HL spreads contiguously node to adjacent node and to the spleen, and splenic involvement upstages disease and historically guided staging laparotomy; this orderly spread (unlike scattered NHL) reflects HL's lymphatic biology."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Hodgkin lymphoma is the prototypical lymphatic-system cancer: it arises in lymph nodes and spreads in an orderly, contiguous fashion down chains of nodes (Ann Arbor staging), usually as painless cervical or mediastinal adenopathy — distinguishing it from non-Hodgkin lymphomas."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Hodgkin lymphoma and DLBCL are the two ends of large-B-cell lymphoma, bridged by gray-zone lymphoma: classic Hodgkin's CD30+ Reed-Sternberg cells lose most B-cell markers while DLBCL keeps them, and gray-zone tumors share both—the distinction drives very different chemo."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "The Reed-Sternberg cell of classic Hodgkin lymphoma is a crippled B cell: a germinal-center B cell that lost its B-cell receptor and most B-lineage markers yet escaped apoptosis via constitutive NF-κB and EBV, surviving as a rare malignant cell amid a reactive immune infiltrate."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV raises Hodgkin lymphoma risk several-fold and changes its biology: HIV-associated Hodgkin is almost always EBV-driven, presents at advanced stage with B symptoms and marrow involvement, and—unlike AIDS-defining lymphomas—its incidence did not fall with antiretroviral therapy."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Radiotherapy is woven into Hodgkin lymphoma's cure: because HL spreads contiguously between nodes, involved-site photon irradiation (lower-dose, after chemo) controls it well—but extended-field radiation's late second cancers and heart disease pushed toward less."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Hodgkin lymphoma is mostly microenvironment: the malignant Reed-Sternberg cells are rare amid an immune infiltrate, and abundant tumor-associated macrophages predict worse outcomes—so the supporting macrophages, not just the cancer cells, shape prognosis."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Hodgkin lymphoma and CLL are both B-cell neoplasms that can intersect through transformation: CLL occasionally undergoes Richter transformation into Hodgkin lymphoma, and both can be EBV-associated—so an indolent leukemia can give rise to an aggressive lymphoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Hodgkin lymphoma evades NK and immune killing despite few tumor cells: the rare Reed-Sternberg cells survive amid abundant immune cells by suppressing NK and T-cell attack and overexpressing PD-L1—why PD-1 blockade is strikingly effective in Hodgkin lymphoma."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone marrow involvement upstages Hodgkin lymphoma: though it usually spreads predictably node-to-node, marrow infiltration signals advanced (stage IV) disease, so staging marrow assessment (now often PET) guides whether limited or extended chemotherapy is used."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Reed-Sternberg cells secrete IL-10 to build an immunosuppressive niche: this and other cytokines recruit and pacify the reactive immune cells that make up most of the tumor, letting the few malignant cells thrive—explaining Hodgkin lymphoma's odd cellular makeup."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Nodular sclerosing Hodgkin lymphoma favors the mediastinum near the thymus: it classically presents as an anterior mediastinal mass in young adults, so it enters the differential of a mediastinal mass alongside thymoma and germ-cell tumors."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Hodgkin lymphoma commonly causes anemia: cytokines from Reed-Sternberg cells drive anemia of chronic disease, and marrow involvement or autoimmune hemolysis can deepen it—so falling red cells are part of the systemic 'B-symptom' illness of advanced HL."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Hodgkin lymphoma thrives by hijacking the immune system: Reed-Sternberg cells amplify PD-L1 to silence surrounding T cells and recruit a protective inflammatory infiltrate, which is exactly why PD-1 checkpoint blockade is strikingly effective in relapsed HL."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Hodgkin lymphoma has a curious alcohol sign: in a minority of patients, drinking alcohol triggers pain in affected lymph nodes within minutes—an unusual, near-specific clue that points to Hodgkin rather than other lymphomas."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Curing Hodgkin lymphoma can later cost the heart: chest radiation and anthracycline chemotherapy raise the risk of coronary disease, valve damage, and heart failure decades on, so cardiac surveillance is central to long-term survivor care."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Curing Hodgkin lymphoma raises later breast cancer risk: chest (mantle) radiation in young women sharply increases breast cancer decades later, so female survivors irradiated young begin breast MRI screening years before the general population."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Hodgkin lymphoma is mostly a crowd of protective cells: the rare malignant Reed-Sternberg cells survive by surrounding themselves with regulatory T cells and other immune cells that shield them, so the tumor is <1% cancer cells and 99% recruited defenders."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Nodular sclerosis Hodgkin lymphoma is defined by fibrosis: broad bands of collagen divide the lymph node into nodules, the histologic signature of the commonest subtype, typically affecting the chest of young adults."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Reed-Sternberg cells grow on their own IL-13: they secrete this Th2 cytokine as an autocrine growth signal and to recruit the eosinophil-rich infiltrate, shaping the inflammatory backdrop that defines Hodgkin lymphoma."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Hodgkin lymphoma centers on the chest and threatens the lungs: it classically forms a mediastinal mass and can invade lung tissue, while bleomycin in its chemotherapy risks pulmonary fibrosis—so the lungs matter both to the disease and its cure."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta lays down the bands of nodular sclerosis Hodgkin: the commonest subtype is defined by collagen bands that TGF-beta drives fibroblasts to deposit, walling the Reed-Sternberg cells into fibrous nodules."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells fill Hodgkin's reactive infiltrate: the tumor is mostly normal immune cells around scarce Reed-Sternberg cells, and dysfunctional antigen presentation by dendritic cells helps the malignant cells evade the surrounding immunity."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Hodgkin lymphoma drains the body's iron: its systemic inflammation and any marrow involvement suppress red-cell production and lock iron away, so anemia of chronic disease is a common feature."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Hodgkin lymphoma can itch through the skin: severe generalized pruritus, sometimes with the lymph-node pain that alcohol triggers, is a classic paraneoplastic symptom that may precede the diagnosis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells populate the Hodgkin microenvironment: drawn around the Reed-Sternberg cells, they engage CD30 ligand to support the malignant cells, and their numbers can track with prognosis."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Hodgkin can raise blood calcium: its activated macrophages convert vitamin D to its active form, driving the hypercalcemia it shares with granulomatous diseases."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Hodgkin's classic kidney lesion is minimal-change nephrotic syndrome: the lymphoma's cytokines make the glomeruli leak protein, a paraneoplastic effect that resolves when the cancer is treated."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Hodgkin draws eosinophils with IL-5: the Reed-Sternberg cells secrete it to recruit the eosinophils that fill the reactive infiltrate, part of the inflamed microenvironment that hides the rare malignant cells."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy hunts Hodgkin's rare giant cell: the binucleate Reed-Sternberg cell with its two huge 'owl-eye' nucleoli sits sparse amid a sea of reactive immune cells, the diagnostic needle in the haystack."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Advanced Hodgkin lymphoma involves the liver: stage IV disease seeds hepatic deposits, and bulky disease can crowd the organ, a marker of widespread spread beyond the lymph nodes and spleen."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Hodgkin rarely strays into the gut: primary or secondary gastrointestinal involvement of the bowel is uncommon for a disease that spreads node to node, but it occurs in advanced or immunosuppressed cases."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Hodgkin is exquisitely vulnerable to antibody drugs: brentuximab vedotin, an anti-CD30 antibody-drug conjugate, and the checkpoint antibodies nivolumab and pembrolizumab have transformed treatment of relapsed disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Curing Hodgkin frays the nerves: both the vincristine of ABVD and brentuximab vedotin injure peripheral neurons into a dose-limiting neuropathy that often dictates how much treatment a patient can take."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It strikes the young, so fertility matters: the alkylating chemotherapy of escalated regimens and any pelvic radiation can cause infertility, so sperm banking and ovarian preservation are offered before treatment."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Neck radiation lands on the thyroid: the mantle or involved-field irradiation that helps cure Hodgkin commonly leaves survivors hypothyroid years later, and carries a long-term risk of radiation-induced thyroid cancer."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The cure can seed a second blood cancer: the alkylating agents and radiation used against Hodgkin carry a delayed risk of therapy-related myelodysplastic syndrome and acute leukemia, among the most feared late effects of treatment."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Hodgkin can turn the immune system on the platelets: it is a recognized cause of secondary immune thrombocytopenia, and the chemotherapy that treats it suppresses platelet production too, so bleeding and low counts are watched for."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK-STAT3 keeps the Reed-Sternberg cell alive: constitutive STAT3 signaling, downstream of JAK2 and cytokine loops, sustains the malignant cell and shapes the immunosuppressive milieu around it."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Reed-Sternberg cells recruit a reactive crowd: the cytokines they secrete pull in neutrophils, eosinophils, and other inflammatory cells that vastly outnumber the rare tumor cells in the node."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The cure shadows the survivor's heart: anthracycline chemotherapy and mediastinal radiation cause late cardiomyopathy, valve disease, and heart failure, among the leading non-relapse causes of death in long-term Hodgkin survivors."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 carries the B symptoms: Reed-Sternberg cells and their reactive infiltrate pour out IL-6, driving the fevers, night sweats, and weight loss that mark advanced Hodgkin lymphoma and track with worse prognosis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Treatment and asplenia open the door to sepsis: chemotherapy neutropenia and the splenectomy or splenic radiation once used leave Hodgkin patients vulnerable to overwhelming infection from encapsulated bacteria."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A bulky mediastinal mass clots the blood: Hodgkin lymphoma, especially with a large mediastinal tumor compressing veins, carries a high venous thromboembolism risk during diagnosis and treatment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Its cytokines blunt the marrow: the IL-6 and inflammatory output of Hodgkin lymphoma — the same drive behind its B symptoms — suppresses erythropoiesis, producing an anemia of chronic disease that tracks with tumor burden."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "Cure casts a long shadow: decades after thoracic (mantle) radiotherapy, Hodgkin survivors face a markedly raised risk of second cancers including lung cancer, a central concern of long-term survivorship care."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Impaired cell-mediated immunity invites an opportunist: Hodgkin lymphoma classically weakens T-cell immunity, and with chemotherapy this leaves patients at risk of Pneumocystis pneumonia, prompting prophylaxis."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Its cure can sow a leukemia: the alkylators and etoposide used to treat Hodgkin lymphoma carry a real risk of therapy-related myelodysplasia and acute myeloid leukemia years later, a feared late effect."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "Mantle radiation breeds lung cancer: decades after chest radiotherapy, and amplified by smoking, Hodgkin survivors face a sharply raised risk of lung cancer including the aggressive small cell type."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Neck and chest radiation scar the arteries: mediastinal and cervical radiotherapy for Hodgkin lymphoma accelerates carotid and coronary atherosclerosis, raising the long-term risk of stroke in survivors."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its chemo injures the nerves: the vinblastine in ABVD and brentuximab vedotin used for Hodgkin lymphoma cause a dose-limiting peripheral neuropathy with numbness and neuropathic pain."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Chemotherapy opens the lung to mold: the neutropenia from Hodgkin-lymphoma chemotherapy, and bleomycin lung injury, can let inhaled Aspergillus invade as pulmonary aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A cancer of the young and its long survivorship weigh on mood: the diagnosis in young adults, intensive therapy and decades of late-effect surveillance contribute to depression in Hodgkin survivors."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its drugs and bulk attack the lungs: bleomycin in ABVD causes pulmonary fibrosis, and a bulky mediastinal Hodgkin mass can compress the airway and superior vena cava."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Mantle radiation silences glands and gonads: neck radiotherapy for Hodgkin lymphoma causes late hypothyroidism, while chemotherapy and pelvic radiation impair fertility and gonadal function."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A young cancer with decades of late-effect risk breeds worry: the diagnosis in youth and the lifelong surveillance for second cancers and cardiac and lung damage foster chronic health anxiety."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its cure scars the heart for decades: mediastinal radiation and the doxorubicin in ABVD cause late premature coronary disease, valve damage and cardiomyopathy in young survivors."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It announces itself through the skin: severe generalised pruritus is a classic constitutional feature of Hodgkin lymphoma, and alcohol-induced pain at involved nodes is a curious sign."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It can leak protein from the kidney: Hodgkin lymphoma is the cancer most classically associated with paraneoplastic minimal-change nephrotic syndrome, which resolves when the lymphoma is treated."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It reaches bone and marrow: advanced Hodgkin lymphoma can infiltrate the bone marrow and skeleton, and treatment-related avascular necrosis follows long steroid use."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can attack the nerves remotely: Hodgkin lymphoma is a classic cause of paraneoplastic cerebellar degeneration and limbic encephalitis, and vinca-alkaloid chemotherapy causes peripheral neuropathy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It can involve gut and liver: Hodgkin lymphoma occasionally infiltrates the liver and gastrointestinal tract, and treatment brings nausea and hepatotoxicity."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "ABVD cures most: doxorubicin-bleomycin-vinblastine-dacarbazine chemotherapy, sometimes with radiation, cures the great majority of Hodgkin lymphoma."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Brentuximab targets CD30: the anti-CD30 antibody-drug conjugate brentuximab vedotin, replacing bleomycin in A+AVD, is central to modern Hodgkin lymphoma treatment."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Uniquely sensitive to PD-1 blockade: 9p24.1 amplification floods Reed-Sternberg cells with PD-L1, making Hodgkin lymphoma exquisitely responsive to nivolumab and pembrolizumab."
---

# Hodgkin Lymphoma

## Overview

**Hodgkin lymphoma (HL)** is a B-cell-derived malignancy defined by the presence of neoplastic **Reed-Sternberg (RS) cells** (binucleated giant cells with prominent "owl eye" nucleoli) within an inflammatory tumor microenvironment. HL is one of oncology's major treatment success stories: overall 5-year OS exceeds **85-90%** with modern therapy, including cures in the majority of patients with advanced-stage disease. RS cells represent only ~0.1-1% of the tumor mass and are derived from **germinal center (GC) B cells** that have undergone incomplete apoptosis during negative selection — they carry somatic hypermutated Ig V genes but have catastrophically lost the B-cell transcription program (no surface Ig, absent BOB1/OCT2/PU.1). The landmark identification of **9p24.1 chromosomal amplification** in RS cells — co-amplifying CD30, PDL1, PDL2, and JAK2 — explained the extraordinary sensitivity of HL to PD-1 checkpoint inhibitors and the tumor's immune evasion strategy [^armand-2018-nivo-hl]. **Brentuximab vedotin (anti-CD30 ADC) + AVD** replaced ABVD as the standard for advanced stage cHL after ECHELON-1 demonstrated superior OS [^connors-2018-echelon1].

**Epidemiology:**
- Incidence: ~8,500 cases/year USA; ~83,000 globally
- Bimodal age distribution: peak 1 at 15-34 years (NSHL predominant); peak 2 at >55 years (MCHL and LDHL)
- Male slight predominance; EBV+ forms more common in low-resource settings and older/young children
- Risk factors: infectious mononucleosis (EBV) — 3-fold elevated risk; HIV; immunosuppression; family history

## Structure

### Classification

**Classical Hodgkin lymphoma (cHL, ~95%):**
RS cells: CD15+, CD30+, PAX5 dim, CD20−, OCT2−, BOB1−, CD45−; EBV in 30-50% (depends on subtype and geography)

Histological subtypes:
- **Nodular sclerosis (NSHL, ~60-65%):** Young adults; mediastinal mass common (~75%); broad collagen bands ("lacunar cells" — RS cell variant); EBV+ ~10-25%; most common in high-income countries; favorable prognosis
- **Mixed cellularity (MCHL, ~25%):** Older adults and young children; EBV+ ~50-70%; no fibrosis; rich inflammatory infiltrate; often stage III-IV at presentation
- **Lymphocyte-rich (LRHL, ~5%):** Rare; similar to NLPHL but CD30+; excellent prognosis; difficult to distinguish from NLPHL without IHC
- **Lymphocyte-depleted (LDHL, ~1%):** Elderly; advanced stage; HIV-associated; EBV+ ~80-90%; worst prognosis of cHL subtypes

**Nodular lymphocyte predominant HL (NLPHL, ~5%):**
Neoplastic "lymphocytic and histiocytic" (L&H) cells, also called "popcorn cells":
- CD20+, CD19+, CD79a+, BCL6+, OCT2+, BOB1+ — maintains B-cell program (unlike RS cells)
- CD30−, CD15−, EBV−
- Distinctly different from cHL: GC B cell origin with intact B-cell transcription; NF-κB via BCR signaling
- Treatment: rituximab (anti-CD20) effective alone or with CHOP; excellent prognosis; late relapses possible; may transform to DLBCL
- Sometimes reclassified as T-cell/histiocyte-rich large B-cell lymphoma (THRLBCL) after transformation

### Reed-Sternberg cell molecular biology

**Origin:**
RS cells originate from GC B cells that failed negative selection: they carry clonal rearranged Ig V genes with somatic hypermutations but often have "crippling" mutations in the Ig V gene that abolish BCR expression — these cells would normally die in the GC by apoptosis; RS cells escape via rescue mechanisms involving CD30, NF-κB, and possibly EBV.

**9p24.1 amplification (~97% cHL):**
Chromosome 9p24.1 harbors JAK2, PD-L1 (CD274), PD-L2 (PDCD1LG2), and CD30 (TNFRSF8) within a shared amplicon; amplification (and polysomy) increases: (1) JAK2 expression → constitutive JAK2-STAT6 → IL-13 auto-stimulation + PD-L1 transcription; (2) PD-L1/PD-L2 surface expression → T-cell exhaustion in tumor microenvironment; (3) CD30 overexpression → TRAF/NF-κB survival signals; this convergent amplification explains the >60-70% ORR to PD-1 inhibitors.

**Other molecular features:**
- SOCS1 mutations/deletions (~40%): loss of JAK-STAT negative regulator → enhanced IL-13 signaling
- TNFRSF14 (HVEM) mutations (~15%): impairs CD8+ T-cell activation in microenvironment
- CARD11 mutations (~5%): constitutive NF-κB activation
- A20 (TNFAIP3) deletions (~30%): NF-κB negative regulator loss
- EBV LMP1: functional CD40 mimic → TRAF2/TRAF3/TRAF6 → NF-κB; also induces PD-L1; expressed in ~40-50% cHL RS cells

**Microenvironment composition:**
RS cells recruit and program an inflammatory microenvironment via secreted chemokines and cytokines:
- CCL17/TARC, CCL22: recruit regulatory T cells (Treg) and Th2 cells → immune suppression
- IL-5, eotaxin: recruit eosinophils (prominent in NSHL and MCHL)
- IL-13: auto-stimulatory for RS cells; also drives fibrosis (NSHL collagen bands)
- PGE2: suppresses NK and CD8+ T cells
- CD47 ("don't eat me"): expressed on RS cells → blocks macrophage phagocytosis

## Function

### Staging

**Ann Arbor / Lugano staging (PET-CT based):**
- Stage I: Single lymph node region or single extralymphatic site
- Stage II: ≥2 lymph node regions, same side of diaphragm (± contiguous extranodal site)
- Stage III: Lymph node regions or structures on both sides of diaphragm
- Stage IV: Disseminated extranodal involvement (liver, bone marrow, lungs)

**Modifiers:**
- B symptoms: fever >38°C, drenching night sweats, >10% body weight loss in 6 months (adverse; B-symptom stage is worse prognosis)
- Bulky disease: mediastinal mass >1/3 of thoracic diameter OR any mass >10 cm

**IPS (International Prognostic Score) for advanced stage:**
7 adverse factors (1 point each): albumin <4 g/dL, Hgb <10.5 g/dL, male sex, stage IV, age ≥45, WBC ≥15,000/μL, lymphocyte count <600/μL or <8% of WBC
Score 0-1: 5-year FFS ~77%; Score ≥5: ~42% (though A+AVD has improved outcomes across all IPS groups)

## Pathology

### Treatment approach

**Early-stage favorable cHL (Stage I-II, no bulky disease, no B symptoms):**
- ABVD × 2 cycles + ISRT (involved-site radiotherapy, 20 Gy): ~95% 5-year PFS; standard
- Or ABVD × 4 cycles without RT (for patients refusing RT; slightly inferior PFS but equivalent OS)
- PET-adapted: interim PET-2 (after 2 ABVD) negative → complete ABVD without RT; positive → escalate to BEACOPP

**Early-stage unfavorable cHL (Stage I-II with bulk/B symptoms/other risk factors):**
- ABVD × 4 cycles + ISRT 30 Gy
- Or 2 cycles eBEACOPP + 2 cycles ABVD + RT (HD14 trial)
- A+AVD being studied in early-stage unfavorable (ECHELON-1 enrolled advanced stage only)

**Advanced-stage cHL (Stage III-IV):**
- **A+AVD (brentuximab vedotin + doxorubicin, vinblastine, dacarbazine) × 6 cycles:** Standard of care [^connors-2018-echelon1]; G-CSF primary prophylaxis required (higher neutropenia vs ABVD)
- Or eBEACOPP (escalated bleomycin, etoposide, doxorubicin, cyclophosphamide, vincristine, procarbazine, prednisone): higher toxicity; used in some European centers; higher 2-year PFS than ABVD but OS equivalent; may be preferred in IPS 4-7 patients
- PET-adapted de-escalation: interim PET-2 negative → switch to ABVD for cycles 3-6 (RATHL trial)

**Relapsed/Refractory cHL:**
- **Salvage chemotherapy:** DHAP, ICE, GVD, IGEV → aiming for CR → proceed to auto-SCT
- **Auto-SCT** (autologous stem cell transplant): standard for chemosensitive R/R cHL; 50-55% 5-year OS in auto-SCT-eligible patients
- **Brentuximab vedotin consolidation post-auto-SCT (AETHERA):** 5-year PFS 59% vs 41%; standard post-auto-SCT for high-risk patients
- **Nivolumab (CheckMate 205):** ORR ~69% in auto-SCT-relapsed/refractory cHL; CR ~16%; duration of response ~17 months; FDA 2016 [^armand-2018-nivo-hl]
- **Pembrolizumab (KEYNOTE-087):** ORR ~69% in R/R cHL; FDA 2017
- **KEYNOTE-204** (pembrolizumab vs brentuximab vedotin in R/R cHL): PFS 13.2 vs 8.3 months (HR 0.65) → pembrolizumab superior to brentuximab monotherapy in R/R; brentuximab now used more in combination or post-PD-1
- **Allo-SCT:** Chemorefractory disease; higher NRM than auto-SCT; DLI for molecular relapse
- **Camidanlumab tesirine (ADCT-301):** CD25 ADC (PBD dimer); ORR ~70% in R/R cHL; under investigation

**NLPHL treatment:**
- Stage IA: Involved site RT alone (excellent prognosis); observation considered in some
- Stage II-IV: R-CHOP or R-CVP; rituximab monotherapy for relapse; watch-and-wait for asymptomatic advanced stage
- Late relapses (10-20 years) common; requires long-term surveillance

### Long-term effects and survivorship

Hodgkin lymphoma survivors (~150,000 in USA) face significant late treatment toxicity:
- **Secondary malignancies:** Breast cancer (RT to mediastinum), lung cancer (bleomycin+RT+smoking), secondary AML/MDS (alkylating agents, etoposide — BEACOPP > ABVD risk), NHL
- **Cardiovascular:** Coronary artery disease and cardiomyopathy from mediastinal RT and anthracyclines; major cause of late mortality
- **Pulmonary:** Bleomycin-induced pulmonary fibrosis (~5-10% clinically significant; dose-dependent); pneumonitis from RT
- **Hypothyroidism:** From neck/mediastinal RT (~50% at 20 years)
- **Infertility:** Procarbazine-containing regimens (BEACOPP) → gonadal toxicity; ABVD and A+AVD have lower infertility risk; fertility preservation counseling before therapy

Modern protocols minimize RT fields and doses (ISRT replacing extended-field RT), reduce bleomycin exposure (A+AVD eliminates bleomycin), and use PET-adapted de-escalation to decrease cumulative toxicity.

## Connections

- `connects-to` → **[CD30](../../03-molecular/cd30/README.md)** — CD30 is expressed on ~100% of RS cells (WHO diagnostic criterion for cHL); brentuximab vedotin is the backbone of A+AVD (ECHELON-1) and consolidation post-auto-SCT (AETHERA); 9p24.1 amplification co-amplifies CD30 with PD-L1/PD-L2 in RS cells.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — 9p24.1 amplification in RS cells drives PD-L1/PD-L2 overexpression → profound T-cell exhaustion in tumor microenvironment; nivolumab (CheckMate 205) and pembrolizumab (KEYNOTE-087) show ORR ~65-70% in R/R cHL; KEYNOTE-204 (pembrolizumab vs BV): PFS 13.2 vs 8.3 months.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB is constitutively active in RS cells via CD30, CD40, EBV-LMP1, and CARD11 signaling; NF-κB drives RS cell survival by upregulating BCL-2, BCL-XL, and cFLIP; microenvironmental TNF-α further activates NF-κB; NF-κB inhibition is a preclinical therapeutic target in R/R cHL.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — 9p24.1 amplification co-amplifies JAK2 with PD-L1/PD-L2 and CD30 in RS cells; JAK2 → constitutive STAT6 → IL-13 autocrine + PD-L1 transcription; ruxolitinib studied in R/R cHL; JAK2 amplification is a primary oncogenic driver in cHL.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Reed-Sternberg cells arise from germinal-center B cells that acquired crippling Ig V-gene mutations and should have died during negative selection; they survive via CD30/CD40/NF-κB and EBV rescue while shedding the B-cell program (no surface Ig, loss of OCT2/BOB1).
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — EBV is found in 30-50% of classical HL (up to 80-90% in lymphocyte-depleted and HIV-associated cases); its LMP1 protein mimics a constitutively active CD40 receptor → NF-κB survival signaling in RS cells; prior infectious mononucleosis roughly triples HL risk.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 status splits Hodgkin lymphoma: RS cells of classical HL are CD20-negative, whereas the popcorn (L&H) cells of NLPHL retain the B-cell program and are CD20-positive — making rituximab effective in NLPHL but not classical HL.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Hodgkin lymphoma is unusual: malignant Reed-Sternberg cells are <1% of the tumor, the bulk being reactive CD4+ T cells (rosetting around RS cells), eosinophils, and histiocytes that RS cells recruit and depend on — why PD-1 blockade freeing exhausted T cells works so well.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is a key Hodgkin lymphoma site: classical HL spreads contiguously node to adjacent node and to the spleen, and splenic involvement upstages disease and historically guided staging laparotomy; this orderly spread (unlike scattered NHL) reflects HL's lymphatic biology.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Hodgkin lymphoma is the prototypical lymphatic-system cancer: it arises in lymph nodes and spreads in an orderly, contiguous fashion down chains of nodes (Ann Arbor staging), usually as painless cervical or mediastinal adenopathy — distinguishing it from non-Hodgkin lymphomas.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Hodgkin lymphoma and DLBCL are the two ends of large-B-cell lymphoma, bridged by gray-zone lymphoma: classic Hodgkin's CD30+ Reed-Sternberg cells lose most B-cell markers while DLBCL keeps them, and gray-zone tumors share both—the distinction drives very different chemo.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — The Reed-Sternberg cell of classic Hodgkin lymphoma is a crippled B cell: a germinal-center B cell that lost its B-cell receptor and most B-lineage markers yet escaped apoptosis via constitutive NF-κB and EBV, surviving as a rare malignant cell amid a reactive immune infiltrate.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV raises Hodgkin lymphoma risk several-fold and changes its biology: HIV-associated Hodgkin is almost always EBV-driven, presents at advanced stage with B symptoms and marrow involvement, and—unlike AIDS-defining lymphomas—its incidence did not fall with antiretroviral therapy.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Radiotherapy is woven into Hodgkin lymphoma's cure: because HL spreads contiguously between nodes, involved-site photon irradiation (lower-dose, after chemo) controls it well—but extended-field radiation's late second cancers and heart disease pushed toward less.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Hodgkin lymphoma is mostly microenvironment: the malignant Reed-Sternberg cells are rare amid an immune infiltrate, and abundant tumor-associated macrophages predict worse outcomes—so the supporting macrophages, not just the cancer cells, shape prognosis.
- `connects-to` → **[CLL](../cll/README.md)** — Hodgkin lymphoma and CLL are both B-cell neoplasms that can intersect through transformation: CLL occasionally undergoes Richter transformation into Hodgkin lymphoma, and both can be EBV-associated—so an indolent leukemia can give rise to an aggressive lymphoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Hodgkin lymphoma evades NK and immune killing despite few tumor cells: the rare Reed-Sternberg cells survive amid abundant immune cells by suppressing NK and T-cell attack and overexpressing PD-L1—why PD-1 blockade is strikingly effective in Hodgkin lymphoma.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone marrow involvement upstages Hodgkin lymphoma: though it usually spreads predictably node-to-node, marrow infiltration signals advanced (stage IV) disease, so staging marrow assessment (now often PET) guides whether limited or extended chemotherapy is used.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Reed-Sternberg cells secrete IL-10 to build an immunosuppressive niche: this and other cytokines recruit and pacify the reactive immune cells that make up most of the tumor, letting the few malignant cells thrive—explaining Hodgkin lymphoma's odd cellular makeup.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Nodular sclerosing Hodgkin lymphoma favors the mediastinum near the thymus: it classically presents as an anterior mediastinal mass in young adults, so it enters the differential of a mediastinal mass alongside thymoma and germ-cell tumors.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Hodgkin lymphoma commonly causes anemia: cytokines from Reed-Sternberg cells drive anemia of chronic disease, and marrow involvement or autoimmune hemolysis can deepen it—so falling red cells are part of the systemic 'B-symptom' illness of advanced HL.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Hodgkin lymphoma thrives by hijacking the immune system: Reed-Sternberg cells amplify PD-L1 to silence surrounding T cells and recruit a protective inflammatory infiltrate, which is exactly why PD-1 checkpoint blockade is strikingly effective in relapsed HL.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Hodgkin lymphoma has a curious alcohol sign: in a minority of patients, drinking alcohol triggers pain in affected lymph nodes within minutes—an unusual, near-specific clue that points to Hodgkin rather than other lymphomas.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Curing Hodgkin lymphoma can later cost the heart: chest radiation and anthracycline chemotherapy raise the risk of coronary disease, valve damage, and heart failure decades on, so cardiac surveillance is central to long-term survivor care.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Curing Hodgkin lymphoma raises later breast cancer risk: chest (mantle) radiation in young women sharply increases breast cancer decades later, so female survivors irradiated young begin breast MRI screening years before the general population.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Hodgkin lymphoma is mostly a crowd of protective cells: the rare malignant Reed-Sternberg cells survive by surrounding themselves with regulatory T cells and other immune cells that shield them, so the tumor is <1% cancer cells and 99% recruited defenders.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Nodular sclerosis Hodgkin lymphoma is defined by fibrosis: broad bands of collagen divide the lymph node into nodules, the histologic signature of the commonest subtype, typically affecting the chest of young adults.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — Reed-Sternberg cells grow on their own IL-13: they secrete this Th2 cytokine as an autocrine growth signal and to recruit the eosinophil-rich infiltrate, shaping the inflammatory backdrop that defines Hodgkin lymphoma.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Hodgkin lymphoma centers on the chest and threatens the lungs: it classically forms a mediastinal mass and can invade lung tissue, while bleomycin in its chemotherapy risks pulmonary fibrosis—so the lungs matter both to the disease and its cure.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta lays down the bands of nodular sclerosis Hodgkin: the commonest subtype is defined by collagen bands that TGF-beta drives fibroblasts to deposit, walling the Reed-Sternberg cells into fibrous nodules.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells fill Hodgkin's reactive infiltrate: the tumor is mostly normal immune cells around scarce Reed-Sternberg cells, and dysfunctional antigen presentation by dendritic cells helps the malignant cells evade the surrounding immunity.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Hodgkin lymphoma drains the body's iron: its systemic inflammation and any marrow involvement suppress red-cell production and lock iron away, so anemia of chronic disease is a common feature.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Hodgkin lymphoma can itch through the skin: severe generalized pruritus, sometimes with the lymph-node pain that alcohol triggers, is a classic paraneoplastic symptom that may precede the diagnosis.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells populate the Hodgkin microenvironment: drawn around the Reed-Sternberg cells, they engage CD30 ligand to support the malignant cells, and their numbers can track with prognosis.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Hodgkin can raise blood calcium: its activated macrophages convert vitamin D to its active form, driving the hypercalcemia it shares with granulomatous diseases.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Hodgkin's classic kidney lesion is minimal-change nephrotic syndrome: the lymphoma's cytokines make the glomeruli leak protein, a paraneoplastic effect that resolves when the cancer is treated.
- `connects-to` → **[Interleukin-5](../../03-molecular/il-5/README.md)** — Hodgkin draws eosinophils with IL-5: the Reed-Sternberg cells secrete it to recruit the eosinophils that fill the reactive infiltrate, part of the inflamed microenvironment that hides the rare malignant cells.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy hunts Hodgkin's rare giant cell: the binucleate Reed-Sternberg cell with its two huge 'owl-eye' nucleoli sits sparse amid a sea of reactive immune cells, the diagnostic needle in the haystack.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Advanced Hodgkin lymphoma involves the liver: stage IV disease seeds hepatic deposits, and bulky disease can crowd the organ, a marker of widespread spread beyond the lymph nodes and spleen.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Hodgkin rarely strays into the gut: primary or secondary gastrointestinal involvement of the bowel is uncommon for a disease that spreads node to node, but it occurs in advanced or immunosuppressed cases.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Hodgkin is exquisitely vulnerable to antibody drugs: brentuximab vedotin, an anti-CD30 antibody-drug conjugate, and the checkpoint antibodies nivolumab and pembrolizumab have transformed treatment of relapsed disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Curing Hodgkin frays the nerves: both the vincristine of ABVD and brentuximab vedotin injure peripheral neurons into a dose-limiting neuropathy that often dictates how much treatment a patient can take.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It strikes the young, so fertility matters: the alkylating chemotherapy of escalated regimens and any pelvic radiation can cause infertility, so sperm banking and ovarian preservation are offered before treatment.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Neck radiation lands on the thyroid: the mantle or involved-field irradiation that helps cure Hodgkin commonly leaves survivors hypothyroid years later, and carries a long-term risk of radiation-induced thyroid cancer.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — The cure can seed a second blood cancer: the alkylating agents and radiation used against Hodgkin carry a delayed risk of therapy-related myelodysplastic syndrome and acute leukemia, among the most feared late effects of treatment.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Hodgkin can turn the immune system on the platelets: it is a recognized cause of secondary immune thrombocytopenia, and the chemotherapy that treats it suppresses platelet production too, so bleeding and low counts are watched for.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK-STAT3 keeps the Reed-Sternberg cell alive: constitutive STAT3 signaling, downstream of JAK2 and cytokine loops, sustains the malignant cell and shapes the immunosuppressive milieu around it.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Reed-Sternberg cells recruit a reactive crowd: the cytokines they secrete pull in neutrophils, eosinophils, and other inflammatory cells that vastly outnumber the rare tumor cells in the node.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The cure shadows the survivor's heart: anthracycline chemotherapy and mediastinal radiation cause late cardiomyopathy, valve disease, and heart failure, among the leading non-relapse causes of death in long-term Hodgkin survivors.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 carries the B symptoms: Reed-Sternberg cells and their reactive infiltrate pour out IL-6, driving the fevers, night sweats, and weight loss that mark advanced Hodgkin lymphoma and track with worse prognosis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Treatment and asplenia open the door to sepsis: chemotherapy neutropenia and the splenectomy or splenic radiation once used leave Hodgkin patients vulnerable to overwhelming infection from encapsulated bacteria.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A bulky mediastinal mass clots the blood: Hodgkin lymphoma, especially with a large mediastinal tumor compressing veins, carries a high venous thromboembolism risk during diagnosis and treatment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Its cytokines blunt the marrow: the IL-6 and inflammatory output of Hodgkin lymphoma — the same drive behind its B symptoms — suppresses erythropoiesis, producing an anemia of chronic disease that tracks with tumor burden.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — Cure casts a long shadow: decades after thoracic (mantle) radiotherapy, Hodgkin survivors face a markedly raised risk of second cancers including lung cancer, a central concern of long-term survivorship care.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Impaired cell-mediated immunity invites an opportunist: Hodgkin lymphoma classically weakens T-cell immunity, and with chemotherapy this leaves patients at risk of Pneumocystis pneumonia, prompting prophylaxis.
- `connects-to` → **[AML](../aml/README.md)** — Its cure can sow a leukemia: the alkylators and etoposide used to treat Hodgkin lymphoma carry a real risk of therapy-related myelodysplasia and acute myeloid leukemia years later, a feared late effect.
- `connects-to` → **[Small Cell Lung Cancer](../sclc/README.md)** — Mantle radiation breeds lung cancer: decades after chest radiotherapy, and amplified by smoking, Hodgkin survivors face a sharply raised risk of lung cancer including the aggressive small cell type.
- `connects-to` → **[Stroke](../stroke/README.md)** — Neck and chest radiation scar the arteries: mediastinal and cervical radiotherapy for Hodgkin lymphoma accelerates carotid and coronary atherosclerosis, raising the long-term risk of stroke in survivors.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its chemo injures the nerves: the vinblastine in ABVD and brentuximab vedotin used for Hodgkin lymphoma cause a dose-limiting peripheral neuropathy with numbness and neuropathic pain.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Chemotherapy opens the lung to mold: the neutropenia from Hodgkin-lymphoma chemotherapy, and bleomycin lung injury, can let inhaled Aspergillus invade as pulmonary aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A cancer of the young and its long survivorship weigh on mood: the diagnosis in young adults, intensive therapy and decades of late-effect surveillance contribute to depression in Hodgkin survivors.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its drugs and bulk attack the lungs: bleomycin in ABVD causes pulmonary fibrosis, and a bulky mediastinal Hodgkin mass can compress the airway and superior vena cava.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Mantle radiation silences glands and gonads: neck radiotherapy for Hodgkin lymphoma causes late hypothyroidism, while chemotherapy and pelvic radiation impair fertility and gonadal function.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A young cancer with decades of late-effect risk breeds worry: the diagnosis in youth and the lifelong surveillance for second cancers and cardiac and lung damage foster chronic health anxiety.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its cure scars the heart for decades: mediastinal radiation and the doxorubicin in ABVD cause late premature coronary disease, valve damage and cardiomyopathy in young survivors.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It announces itself through the skin: severe generalised pruritus is a classic constitutional feature of Hodgkin lymphoma, and alcohol-induced pain at involved nodes is a curious sign.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It can leak protein from the kidney: Hodgkin lymphoma is the cancer most classically associated with paraneoplastic minimal-change nephrotic syndrome, which resolves when the lymphoma is treated.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It reaches bone and marrow: advanced Hodgkin lymphoma can infiltrate the bone marrow and skeleton, and treatment-related avascular necrosis follows long steroid use.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can attack the nerves remotely: Hodgkin lymphoma is a classic cause of paraneoplastic cerebellar degeneration and limbic encephalitis, and vinca-alkaloid chemotherapy causes peripheral neuropathy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It can involve gut and liver: Hodgkin lymphoma occasionally infiltrates the liver and gastrointestinal tract, and treatment brings nausea and hepatotoxicity.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — ABVD cures most: doxorubicin-bleomycin-vinblastine-dacarbazine chemotherapy, sometimes with radiation, cures the great majority of Hodgkin lymphoma.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Brentuximab targets CD30: the anti-CD30 antibody-drug conjugate brentuximab vedotin, replacing bleomycin in A+AVD, is central to modern Hodgkin lymphoma treatment.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Uniquely sensitive to PD-1 blockade: 9p24.1 amplification floods Reed-Sternberg cells with PD-L1, making Hodgkin lymphoma exquisitely responsive to nivolumab and pembrolizumab.

[^connors-2018-echelon1]: Connors JM, Jurczak W, Straus DJ, et al. Brentuximab vedotin with chemotherapy for stage III or IV Hodgkin's lymphoma. *N Engl J Med.* 2018;378(4):331-344. [doi:10.1056/NEJMoa1708984](https://doi.org/10.1056/NEJMoa1708984) · [PubMed 29360494](https://pubmed.ncbi.nlm.nih.gov/29360494/)
[^armand-2018-nivo-hl]: Armand P, Engert A, Younes A, et al. Nivolumab for relapsed/refractory classic Hodgkin lymphoma after failure of autologous hematopoietic cell transplantation: extended follow-up of the multicohort single-arm phase II CheckMate 205 trial. *J Clin Oncol.* 2018;36(14):1428-1439. [doi:10.1200/JCO.2017.77.6717](https://doi.org/10.1200/JCO.2017.77.6717) · [PubMed 29584546](https://pubmed.ncbi.nlm.nih.gov/29584546/)
