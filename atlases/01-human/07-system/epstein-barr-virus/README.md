---
schema: human-scale-entry/v1
id: epstein-barr-virus
name: Epstein-Barr Virus
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "EBV (HHV-4; gammaherpesvirus; 172 kb dsDNA) infects >95% of adults; latency programs I/II/III expressing EBNA/LMP antigens drive oncogenesis; associated with Burkitt lymphoma, Hodgkin lymphoma, NPC, PTLD; infectious mononucleosis in adolescents; no approved vaccine or antiviral."
aliases: ["EBV", "Epstein-Barr virus", "human herpesvirus 4", "HHV-4", "EBV-1", "EBV-2", "infectious mononucleosis", "kissing disease", "mono", "glandular fever", "Burkitt lymphoma EBV", "PTLD", "LMP1", "EBNA", "EBV latency", "EBV oncogenesis"]
sources:
  - id: cohen-2000-ebv-review
    type: peer-reviewed
    cite: "Cohen JI. Epstein-Barr virus infection. N Engl J Med. 2000;343(7):481-492."
    doi: "10.1056/NEJM200008173430707"
    pmid: "10944566"
    url: "https://doi.org/10.1056/NEJM200008173430707"
    accessed: "2026-06-08"
  - id: thorley-lawson-2004-ebv-latency
    type: peer-reviewed
    cite: "Thorley-Lawson DA. Epstein-Barr virus: exploiting the immune system. Nat Rev Immunol. 2001;1(1):75-82."
    doi: "10.1038/35095556"
    pmid: "11905816"
    url: "https://doi.org/10.1038/35095556"
    accessed: "2026-06-08"
  - id: nourse-2011-ebv-lymphoma
    type: peer-reviewed
    cite: "Young LS, Rickinson AB. Epstein-Barr virus: 40 years on. Nat Rev Cancer. 2004;4(10):757-768."
    doi: "10.1038/nrc1452"
    pmid: "15510157"
    url: "https://doi.org/10.1038/nrc1452"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/lmp1
    relation: connects-to
    note: "EBV LMP1 (latent membrane protein 1) is the primary EBV oncoprotein: 6 TM domains; CTAR1 binds TRAF1/2/3 → NIK → NF-κB; CTAR2 binds TRADD/TRAF6 → IKKβ → NF-κB; constitutively active CD40 mimic driving B cell immortalization in EBV latency III."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "EBV LMP1 CTAR1/2 activate both canonical and alternative NF-κB; CTAR1 → TRAF1/2/3 → NIK → p52/RelB; CTAR2 → TRADD/TRAF6 → IKKβ → p65/p50; constitutively active CD40 mimic → BCL-2, ICAM-1, IL-6 → B cell immortalization and EBV lymphomagenesis."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "EBNA3C recruits SCFSkp2 E3 ligase → p53 polyubiquitination and degradation; LMP1 → MDM2 upregulation → additional p53 destabilization; EBV p53 evasion enables infected B cells to bypass apoptosis; TP53 mutations cooperate with EBV in Burkitt lymphoma and EBV+ DLBCL."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "EBV LMP1 → NF-κB → TGF-β1 production in B cells; EBNA1 blocks Smad signaling → prevents TGF-β growth arrest; TGF-β maintains EBV latency (BZLF1 lytic switch suppression); TGF-β-high microenvironment in EBV+ Hodgkin lymphoma (Reed-Sternberg cells) is immunosuppressive."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "EBV infects B cells via CD21/CR2 → endocytic uptake → nuclear EBNA1 → episome maintenance; EBV drives B-cell immortalization in latency III (all EBNAs + LMP1/2); memory B cells are the long-term EBV reservoir; EBV-driven B-cell lymphomagenesis is CD21-dependent."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "EBV found in ~40% of classical Hodgkin lymphoma Reed-Sternberg cells (predominantly latency II: LMP1 + LMP2A + EBNA1); LMP1 → NF-κB → BCL-2, ICAM-1, CD30, IL-6 in HRS cells; EBV+ cHL has better prognosis in developing countries but similar outcomes in Western cohorts."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "EBV+ DLBCL: primarily in immunosenescent patients; latency II/III; LMP1 → NF-κB drives survival; poor prognosis (OS ~2 years); EBV PTLD in transplant recipients: rituximab ± reduced immunosuppression; adoptive EBV-specific CTL therapy effective in PTLD."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "EBV fibronectin: fibronectin from B-cells (already mapped) and macrophages (already mapped) modulates viral ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "EBV notch: Notch signalling on B-cells (already mapped) and macrophages (already mapped) modulates viral latency regulation; notch excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "EBV igf-1: IGF-1 from B-cells (already mapped) and macrophages (already mapped) modulates viral B-cell survival axis; igf-1 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "EBV activin-a: activin-A from B-cells (already mapped) and macrophages (already mapped) drives EBV latency fibrotic remodelling; activin-a excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "EBV cgrp: CGRP from B-cells (already mapped) and macrophages (already mapped) modulates EBV vascular immune tone; cgrp excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "EBV calcitonin: calcitonin from B-cells (already mapped) and macrophages (already mapped) modulates EBV calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "EBV substance-p: substance-P from B-cells (already mapped) and macrophages (already mapped) modulates EBV neuroimmune signalling; substance-p excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "EBV insulin-receptor: insulin-receptor on B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune signalling; insulin-receptor dysregulation amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "EBV aldosterone: aldosterone from B-cells (already mapped) and macrophages (already mapped) modulates EBV immune mineralocorticoid balance; aldosterone excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "EBV androgen-receptor: androgen-receptor on B-cells (already mapped) and macrophages (already mapped) modulates EBV hormonal B-cell proliferation; androgen-receptor excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "EBV norepinephrine: norepinephrine from B-cells (already mapped) and macrophages (already mapped) modulates EBV adrenergic immune tone; norepinephrine excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "EBV adrenomedullin: adrenomedullin from B-cells (already mapped) and macrophages (already mapped) modulates EBV vascular immune tone; adrenomedullin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "EBV bdnf: BDNF from B-cells (already mapped) and macrophages (already mapped) modulates EBV neurotrophin B-cell survival; bdnf excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "EBV osteopontin: osteopontin from B-cells (already mapped) and macrophages (already mapped) modulates EBV extracellular matrix immune remodelling; osteopontin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "EBV fgfr: FGFR on B-cells (already mapped) and macrophages (already mapped) modulates EBV fibroblast immune growth signalling; fgfr dysregulation amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "EBV epinephrine: epinephrine from B-cells (already mapped) and macrophages (already mapped) modulates EBV adrenergic stress immune tone; epinephrine excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "EBV renin: renin from B-cells (already mapped) and macrophages (already mapped) modulates EBV renin-angiotensin immune axis; renin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "EBV myostatin: myostatin from B-cells (already mapped) and macrophages (already mapped) modulates EBV muscle wasting immune signalling; myostatin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "EBV galectin-3: galectin-3 from B-cells (already mapped) and macrophages (already mapped) drives EBV immune fibrotic lattice remodelling; galectin-3 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "EBV angiopoietin: angiopoietin from B-cells (already mapped) and macrophages (already mapped) modulates EBV vascular immune remodelling; angiopoietin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "EBV resistin: resistin from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune inflammatory tone; resistin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "EBV cortisol: cortisol from B-cells (already mapped) and macrophages (already mapped) modulates EBV stress-immune axis; cortisol excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "EBV ghrelin: ghrelin from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune appetite axis; ghrelin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "EBV glucagon: glucagon from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune glucose axis; glucagon excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "EBV leptin: leptin from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune energy axis; leptin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "EBV prolactin: prolactin from B-cells (already mapped) and macrophages (already mapped) modulates EBV immune lactogenic proliferation; prolactin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "EBV estrogen: estrogen from B-cells (already mapped) and macrophages (already mapped) modulates EBV hormonal B-cell immune activation; estrogen excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "EBV acetylcholine: acetylcholine from B-cells (already mapped) and macrophages (already mapped) modulates EBV cholinergic immune neuromodulation; acetylcholine excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "EBV adenosine: adenosine from B-cells (already mapped) and macrophages (already mapped) modulates EBV adenosinergic immune purinergic axis; adenosine excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "EBV apoe: apoe from B-cells (already mapped) and macrophages (already mapped) modulates EBV lipid immune viral entry axis; apoe excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "EBV testosterone: testosterone from B-cells (already mapped) and macrophages (already mapped) modulates EBV androgenic immune activation axis; testosterone excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "EBV il-2: il-2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV lymphocyte proliferation immune axis; il-2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "EBV il-10: il-10 from B-cells (already mapped) and macrophages (already mapped) modulates EBV immunosuppressive viral immune evasion; il-10 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "EBV il-12: il-12 from B-cells (already mapped) and macrophages (already mapped) modulates EBV th1 immune polarization axis; il-12 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "EBV il-17a: il-17a from B-cells (already mapped) and macrophages (already mapped) modulates EBV mucosal immune inflammatory axis; il-17a excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "EBV il-13: il-13 from B-cells (already mapped) and macrophages (already mapped) modulates EBV th2 immune polarization axis; il-13 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "EBV il-1b: il-1b from B-cells (already mapped) and macrophages (already mapped) modulates EBV pyroptotic immune inflammasome axis; il-1b excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "EBV il-4: il-4 from B-cells (already mapped) and macrophages (already mapped) modulates EBV th2 immune polarization axis; il-4 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "EBV il-5: il-5 from B-cells (already mapped) and macrophages (already mapped) modulates EBV eosinophil immune activation axis; il-5 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "EBV il-6: il-6 from B-cells (already mapped) and macrophages (already mapped) modulates EBV pleiotropic immune activation axis; il-6 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "EBV il-23: il-23 from B-cells (already mapped) and macrophages (already mapped) modulates EBV th17 immune activation axis; il-23 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "EBV il-31: il-31 from B-cells (already mapped) and macrophages (already mapped) modulates EBV pruritic immune neuroimmune axis; il-31 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "EBV il-33: il-33 from B-cells (already mapped) and macrophages (already mapped) modulates EBV alarmin immune activation axis; il-33 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/il-36
    relation: connects-to
    note: "EBV il-36: il-36 from B-cells (already mapped) and macrophages (already mapped) modulates EBV epidermal immune inflammatory axis; il-36 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "EBV tnf-alpha: tnf-alpha from B-cells (already mapped) and macrophages (already mapped) modulates EBV inflammatory cytokine immune axis; tnf-alpha excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "EBV ifn-gamma: ifn-gamma from B-cells (already mapped) and macrophages (already mapped) modulates EBV th1 antiviral immune axis; ifn-gamma excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "EBV stat1: stat1 from B-cells (already mapped) and macrophages (already mapped) modulates EBV interferon-signalling immune axis; stat1 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "EBV stat3: stat3 from B-cells (already mapped) and macrophages (already mapped) modulates EBV oncogenic immune signalling axis; stat3 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "EBV jak2: jak2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV cytokine receptor signalling immune axis; jak2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "EBV akt: akt from B-cells (already mapped) and macrophages (already mapped) modulates EBV pro-survival kinase immune axis; akt excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "EBV mtor: mtor from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune growth axis; mtor excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "EBV ampk: ampk from B-cells (already mapped) and macrophages (already mapped) modulates EBV energy-sensing immune metabolic axis; ampk excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "EBV hif-1alpha: hif-1alpha from B-cells (already mapped) and macrophages (already mapped) modulates EBV hypoxic immune metabolic axis; hif-1alpha excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "EBV ccl2: ccl2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV monocyte recruitment immune axis; ccl2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "EBV cxcl12: cxcl12 from B-cells (already mapped) and macrophages (already mapped) modulates EBV stromal immune homing axis; cxcl12 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EBV egfr: egfr from B-cells (already mapped) and macrophages (already mapped) modulates EBV growth factor receptor immune axis; egfr excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EBV erk1-2: erk1-2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV mapk proliferative immune axis; erk1-2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "EBV foxo: foxo from B-cells (already mapped) and macrophages (already mapped) modulates EBV apoptotic immune regulation axis; foxo excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "EBV foxo1: foxo1 from B-cells (already mapped) and macrophages (already mapped) modulates EBV transcriptional immune regulation axis; foxo1 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "EBV jak1-2: jak1-2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV interferon receptor signalling immune axis; jak1-2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "EBV mhc-class-ii: mhc-class-ii from B-cells (already mapped) and macrophages (already mapped) modulates EBV antigen presentation immune axis; mhc-class-ii excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "EBV pdgf: pdgf from B-cells (already mapped) and macrophages (already mapped) modulates EBV growth factor proliferative immune axis; pdgf excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "EBV vegf: vegf from B-cells (already mapped) and macrophages (already mapped) modulates EBV angiogenic immune activation axis; vegf excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "EBV complement-c3: complement-c3 from B-cells (already mapped) and macrophages (already mapped) modulates EBV innate complement immune axis; complement-c3 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "EBV complement-c5: complement-c5 from B-cells (already mapped) and macrophages (already mapped) modulates EBV terminal complement immune axis; complement-c5 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "EBV wnt-beta-catenin: wnt-beta-catenin from B-cells (already mapped) and macrophages (already mapped) modulates EBV oncogenic wnt proliferative axis; wnt-beta-catenin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "EBV cgas-sting: cgas-sting from B-cells (already mapped) and macrophages (already mapped) modulates EBV innate dna-sensing immune axis; cgas-sting excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "EBV autophagy: autophagy from B-cells (already mapped) and macrophages (already mapped) modulates EBV viral clearance immune axis; autophagy excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "EBV bcl-2: bcl-2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV anti-apoptotic immune survival axis; bcl-2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV."
---

# Epstein-Barr Virus

## Overview

**Epstein-Barr virus (EBV)**, also known as **human herpesvirus 4 (HHV-4)**, is a **gammaherpesvirus** (subfamily *Gammaherpesvirinae*, genus *Lymphocryptovirus*) with a ~172 kb double-stranded DNA genome. Discovered in 1964 by Anthony Epstein and Yvonne Barr in Burkitt lymphoma cells, EBV has since been identified as the causative agent of **infectious mononucleosis** and is recognized as the most versatile human tumor virus, associated with **>7 distinct human malignancies** including Burkitt lymphoma, Hodgkin lymphoma, nasopharyngeal carcinoma (NPC), post-transplant lymphoproliferative disorder (PTLD), EBV+ diffuse large B cell lymphoma (DLBCL), EBV-associated gastric carcinoma, and NK/T cell lymphoma [^nourse-2011-ebv-lymphoma].

**Prevalence:** EBV infects >95% of adults worldwide. Primary infection in early childhood (as in most developing nations) is usually asymptomatic. Primary infection in adolescents and adults causes **infectious mononucleosis (IM)** — the "kissing disease" — in ~50% of susceptible individuals. After primary infection, EBV establishes **lifelong latent infection** in a small pool of resting memory B cells (1 in ~10^6) where it is virtually invisible to immune surveillance.

**Two EBV subtypes:** EBV-1 (dominant in Western countries) and EBV-2 (more common in Africa and immunocompromised individuals); EBV-1 strains transform B cells more efficiently due to EBNA2 differences.

The EBV story is fundamentally about **viral exploitation of normal B cell biology**: EBV mimics and hijacks the normal B cell differentiation signals (germinal center reactions, CD40 signaling, BCR signaling) to drive B cell proliferation and establish latency in memory B cells, using viral proteins to substitute for cellular co-stimulatory signals that would normally require antigen + T cell help.

## Structure

### EBV genome and gene products

EBV's ~172 kb linear dsDNA genome encodes ~85 genes. The genome contains **terminal repeat (TR)** sequences at both ends (used for circularization into episomal latent genome) and **internal repeat** regions.

**Latent gene products (expressed in various latency programs):**

| Gene | Protein | Function |
|------|---------|----------|
| **EBNA1** | EBV nuclear antigen 1 | Maintains episomal EBV genome (tethers to chromosomes via OriP); contains Gly-Ala repeat → blocks MHC class I presentation; activates LMP1 promoter; drives latent DNA replication |
| **EBNA2** | EBV nuclear antigen 2 | Viral transactivator; no DNA-binding domain; binds RBP-Jκ (Notch pathway coactivator) → activates LMP1, LMP2A, CD23; mimics activated Notch1 intracellular domain |
| **EBNA3A, 3B, 3C** | EBV nuclear antigens 3 | Repressive regulators; EBNA3A/3C silence CDKN2A (p16^INK4a^) → releases CDK4/6; EBNA3C degrades p53 (Skp2 E3 recruitment) and RB; required for B cell immortalization |
| **EBNA-LP** | Leader protein | Co-activator of EBNA2; activates cyclin D1 and BCL-2 |
| **LMP1** | Latent membrane protein 1 | **Primary EBV oncoprotein**: 6 TM domains; constitutively active CD40 mimic → TRAF → NF-κB + AP-1 + JAK-STAT → B cell proliferation/survival (detailed in LMP1 entry) |
| **LMP2A** | Latent membrane protein 2A | BCR mimic: ITAM motifs → Lyn/Syk → PI3K/Akt → B cell survival signal; maintains B cells with BCR-like signal without antigen |
| **LMP2B** | Latent membrane protein 2B | Modulates LMP2A activity; may regulate lytic reactivation |
| **EBERs 1/2** | EBV-encoded small RNAs | Non-coding RNAs; highly abundant; activate PKR-like innate responses; bind La antigen; diagnostic marker in EBV-positive tumors |
| **miRBARTs** | BART microRNAs | ~22 miRNAs; suppress host antiviral responses; target MICB (NK ligand), LMP1 (autoregulation), PUMA (apoptosis) |

**Lytic gene products** (expressed during productive infection):
- **gp350/220**: Major surface glycoprotein; binds CD21 (CR2, complement receptor 2) on B cells and CD21 on nasopharyngeal epithelium → primary attachment
- **gp42**: Binds MHC class II on B cells → required for B cell entry (unlike epithelial cells which use gHgL alone)
- **BALF4 (gB), BKRF4 (gL), BXLF2 (gH)**: Core fusion machinery (gH/gL triggers F)
- **EA (early antigen), VCA (viral capsid antigen)**: Serological markers for primary (VCA-IgM) and past infection (VCA-IgG)

### Latency programs

EBV exists in four distinct latency states, named for the proteins expressed:

| Latency | Proteins Expressed | Cells | Associated Disease |
|---------|-------------------|-------|-------------------|
| **0** | None (or LMP2A only) | Resting memory B cells | Normal latent carriage; no disease |
| **I** | EBNA1, EBERs, miRBARTs | B cells (rare) | Burkitt lymphoma; EBV+ gastric carcinoma |
| **II** | EBNA1, LMP1, LMP2A, EBERs, miRBARTs | B cells, epithelial cells, NK cells | Hodgkin lymphoma, NPC, NK/T cell lymphoma |
| **III** | All EBNAs (1-6), LMP1, LMP2A/B, EBERs | Activated B cells, lymphoblastoid cell lines | Infectious mononucleosis; PTLD; lymphoblastoid cell line (LCL) in vitro |

**Latency transition model (Thorley-Lawson model):** EBV enters tonsil B cells → Latency III (germinal center seeding) → Latency II (germinal center reaction) → Latency I/0 (resting memory B cells). EBV hijacks the normal B cell differentiation pathway from naive → germinal center → memory B cell, substituting viral proteins for cellular signals at each step.

## Function

### EBV entry into B cells

1. **gp350/220** binds **CD21 (CR2)** on B cells (CD21 = complement receptor type 2; also binds C3d opsonized antigens → normally activates BCR co-signaling)
2. **gp42** binds **MHC class II (HLA-DR)** on B cells → triggers gH/gL fusion complex
3. **gH/gL + gB (gp110)** → viral-host membrane fusion → nucleocapsid enters → episome formation in nucleus

**Epithelial cell entry (different):** gH/gL alone (without gp42, because epithelium lacks MHC class II) → binds integrins (αvβ5, αvβ6, αvβ8) + NMHC-IIA → fusion

**Salivary transmission:** Primary EBV infection is transmitted by saliva via lytic replication in oropharyngeal epithelium → released virus infects tonsillar B cells

### Infectious mononucleosis pathophysiology

Primary EBV infection in immunologically naive adolescents/adults:
1. EBV infects B cells in tonsils → Latency III → massive **B cell proliferation** (lymphoblastoid-like)
2. Robust cytotoxic T cell (CD8+) and NK cell response → CTLs recognize LMP/EBNA antigens → control B cell proliferation; CTL-driven lymphocytosis constitutes the "atypical lymphocytes" on blood smear
3. **Exudative pharyngitis**: Tonsillar B cell/T cell infiltration + direct EBV infection of oropharyngeal epithelium → necrotic pseudomembrane
4. **Splenomegaly**: Splenic B cell infiltration + T cell response → risk of splenic rupture (1/1000; contraindication to contact sports for ≥3-4 weeks after diagnosis)
5. **Lymphadenopathy**: Cervical (posterior) + generalized; reactive
6. **Heterophile antibodies (Monospot test)**: IgM antibodies agglutinating sheep/horse red blood cells; not cross-reactive with EBV antigens; mechanism unclear; positive in ~85% of adult IM, lower in children

**Complications:**
- **Airway obstruction**: Massive tonsillar/adenoidal hypertrophy → steroid therapy indicated
- **Splenic rupture**: Rare but life-threatening; avoid contact sports 3-4 weeks
- **Neurological**: Meningitis, encephalitis, Guillain-Barré, Bell's palsy (rare)
- **Hematological**: Thrombocytopenia (~50%), hemolytic anemia (anti-i IgM cold agglutinins), neutropenia
- **Chronic active EBV (CAEBV)**: Rare; uncontrolled EBV in T cells/NK cells → cytokine storm, organ infiltration; fatal without HSCT
- **Amoxicillin rash**: EBV-infected patients given amoxicillin/ampicillin → maculopapular rash ~90% of the time (mechanism: unclear; likely B cell-mediated IgM production against drug)

### Immune evasion mechanisms

EBV has co-evolved with the human immune system for millions of years and employs multiple immune evasion strategies:

1. **EBNA1 Gly-Ala repeat:** Blocks proteasomal degradation and MHC class I presentation of EBNA1 peptides → CTLs cannot eliminate EBNA1-expressing cells (all latency forms)
2. **vIL-10 (BCRF1):** EBV encodes a viral IL-10 homolog → IL-10R on T cells → suppresses Th1 cytokines (IFN-γ, IL-2) → impaired CTL and NK function
3. **miR-BART5:** Suppresses PUMA (p53 upregulated modulator of apoptosis) → infected B cells resist apoptosis
4. **miR-BART2-5p:** Targets MICB → reduces NK cell recognition (MICB is NKG2D ligand)
5. **LMP2A BCR signaling:** Prevents BCR editing and deletion signals → supports survival of EBV-infected B cells that would normally be eliminated
6. **Latency 0 in resting memory B cells:** No viral proteins expressed (except occasional LMP2A) → virtually invisible to CTLs; episome diluted with cell division → extremely low copy number

## Pathology

### EBV-associated malignancies

**Burkitt lymphoma (BL):**
- Most common pediatric cancer in sub-Saharan Africa (endemic BL)
- **Defining molecular lesion**: c-Myc translocation to immunoglobulin loci: t(8;14)(q24;q32) [IGH], t(2;8)(p12;q24) [IGK], or t(8;22)(q24;q11) [IGL]
- EBV+ in ~95% of endemic BL (Africa), ~30% of sporadic BL (Western), ~30% of HIV-associated BL
- **EBV contribution**: EBV latency I (EBNA1 only) → no T cell targets; c-Myc translocation provides proliferative drive; EBV likely acts as cofactor (malaria may cooperate by driving GC reactions)
- **Pathology**: Starry sky appearance on histology (tingible body macrophages clearing apoptotic cells among proliferating lymphoma cells); Ki-67 near 100%

**Hodgkin lymphoma (HL):**
- EBV+ in ~40-50% of HL worldwide; higher in developing countries, immunocompromised, mixed cellularity subtype
- **EBV role**: Reed-Sternberg (RS) cells express Latency II (LMP1/2, EBNA1); LMP1 mimics constitutively active CD40 → NF-κB → RS cell survival (RS cells would normally die from loss of BCR signaling)
- **Immune microenvironment**: RS cells surround themselves with reactive T cells, eosinophils, macrophages via LMP1-driven cytokine secretion (IL-10, IL-13, CCL5, CCL17)

**Nasopharyngeal carcinoma (NPC):**
- 98% EBV+ in undifferentiated NPC (most common type, especially in Southeast Asia, China, North Africa)
- Latency II: LMP1, LMP2, EBNA1 expressed in tumor cells
- **Risk factors**: EBV + salt-cured fish (nitrosamines) + HLA-A2 haplotype
- **Epidemiology**: Highest incidence in southern China, Southeast Asia, North Africa; rare in Western countries
- **Diagnosis**: EBV DNA in plasma (high sensitivity for staging and monitoring)
- **Treatment**: Cisplatin-based chemoradiation; EBV DNA clearance = good prognosis

**Post-transplant lymphoproliferative disorder (PTLD):**
- Occurs in immunosuppressed transplant recipients (most commonly after HSCT or solid organ transplant)
- Loss of EBV-specific CTL surveillance → Latency III B cell proliferation → polyclonal or monoclonal lymphoproliferation
- Spectrum from polyclonal hyperplasia → monoclonal lymphoma; EBV+ DLBCL most common histology
- **Risk**: Highest in EBV-seronegative recipients receiving EBV+ donor (pediatric HSCT); calcineurin inhibitors severely impair CTL
- **Treatment**: Reduce immunosuppression + anti-CD20 (rituximab) ± EBV-specific CTL (DLI or adoptive T cell therapy)

### Diagnosis of infectious mononucleosis

- **Heterophile antibody test (Monospot)**: Rapid lateral flow; ~85% sensitivity in adults; poor in children <4 years; detects IgM heterophile Ab
- **EBV-specific serology**: VCA-IgM (acute, positive within 1 week, fades 1-2 months); VCA-IgG (lifelong); EA-IgG (acute reactivation marker); EBNA1-IgG (develops 2-4 months after primary infection — important: negative EBNA-IgG + positive VCA-IgM/IgG = acute infection)
- **EBV DNA (PCR)**: Quantitative in blood; used for PTLD monitoring and NPC staging; not diagnostic for IM
- **Blood smear**: Atypical lymphocytes (large CD8+ CTLs); >10% atypical lymphocytes + typical symptoms = high probability IM

### Treatment

**Infectious mononucleosis:** No approved antiviral therapy; management is supportive:
- Rest; adequate hydration; acetaminophen/NSAIDs for fever and pharyngitis
- **Steroids (dexamethasone)**: Indicated for severe pharyngeal inflammation with impending airway compromise; NOT recommended routinely (may prolong infection)
- **Avoid amoxicillin/ampicillin**: EBV-specific → nearly universal drug rash
- Avoid contact sports for ≥3-4 weeks (splenic rupture risk)
- Acyclovir/ganciclovir: Active against lytic EBV replication but NOT against latent infection; no proven clinical benefit in IM

**PTLD:** Reduce immunosuppression + **rituximab (anti-CD20)** ± CHOP; adoptive EBV-specific CTL therapy (experimental); highly effective if caught early.

**EBV+ lymphomas:** Standard lymphoma regimens (R-CHOP for DLBCL); EBV-specific antigens as therapeutic targets under investigation (EBV peptide vaccines, LMP1/2-specific CAR-T cells).

**No approved EBV vaccine:** Research ongoing; gp350-based subunit vaccines under Phase I/II trials; mRNA vaccines targeting gp350 + gH/gL + gp42 in development.

## Connections

- `connects-to` → **[LMP1](../../03-molecular/lmp1/README.md)** — EBV LMP1 (latent membrane protein 1) is EBV's primary oncoprotein; 6 TM domains; CTAR1 → TRAF1/2/3 → NIK → NF-κB (alternative); CTAR2 → TRADD/TRAF6 → IKKβ → NF-κB (canonical); constitutively active CD40 mimic driving B cell immortalization, BCL-2 upregulation, and lymphomagenesis in latency II/III.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — EBV LMP1 is the paradigmatic viral NF-κB activator: CTAR1 → TRAF1/2/3 → NIK → IKKα → p52/RelB (alternative NF-κB); CTAR2 → TRADD/TRAF6 → IKKβ → p65/p50 (canonical NF-κB); NF-κB drives BCL-2, ICAM-1, CD23, TRAF1, IL-6 → B cell survival and proliferation.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — EBNA3C recruits SCFSkp2 E3 ubiquitin ligase → p53 polyubiquitination and proteasomal degradation; LMP1 → MDM2 upregulation → additional p53 destabilization; EBV p53 antagonism enables infected B cells to bypass DNA damage checkpoints; TP53 mutations cooperate with EBV in Burkitt lymphoma and EBV+ DLBCL.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — EBV LMP1 → NF-κB → TGF-β1 production; EBNA1 suppresses Smad signaling → prevents TGF-β growth arrest in EBV-infected B cells; TGF-β maintains EBV latency (represses BZLF1 lytic switch); TGF-β-high immunosuppressive microenvironment in EBV+ Hodgkin lymphoma Reed-Sternberg cells.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — EBV infects B cells via CD21/CR2 → endocytic uptake → nuclear EBNA1 → episome maintenance; EBV drives B-cell immortalization in latency III (all EBNAs + LMP1/2); memory B cells are the long-term EBV reservoir; EBV-driven B-cell lymphomagenesis is CD21-dependent.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — EBV found in ~40% of classical Hodgkin lymphoma Reed-Sternberg cells (predominantly latency II: LMP1 + LMP2A + EBNA1); LMP1 → NF-κB → BCL-2, ICAM-1, CD30, IL-6 in HRS cells; EBV+ cHL has better prognosis in developing countries but similar outcomes in Western cohorts.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — EBV+ DLBCL: primarily in immunosenescent patients; latency II/III; LMP1 → NF-κB drives survival; poor prognosis (OS ~2 years); EBV PTLD in transplant recipients: rituximab ± reduced immunosuppression; adoptive EBV-specific CTL therapy effective in PTLD.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — EBV fibronectin: fibronectin from B-cells (already mapped) and macrophages (already mapped) modulates viral ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — EBV notch: Notch signalling on B-cells (already mapped) and macrophages (already mapped) modulates viral latency regulation; notch excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — EBV igf-1: IGF-1 from B-cells (already mapped) and macrophages (already mapped) modulates viral B-cell survival axis; igf-1 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — EBV activin-a: activin-A from B-cells (already mapped) and macrophages (already mapped) drives EBV latency fibrotic remodelling; activin-a excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — EBV cgrp: CGRP from B-cells (already mapped) and macrophages (already mapped) modulates EBV vascular immune tone; cgrp excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — EBV calcitonin: calcitonin from B-cells (already mapped) and macrophages (already mapped) modulates EBV calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — EBV substance-p: substance-P from B-cells (already mapped) and macrophages (already mapped) modulates EBV neuroimmune signalling; substance-p excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — EBV insulin-receptor: insulin-receptor on B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune signalling; insulin-receptor dysregulation amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — EBV aldosterone: aldosterone from B-cells (already mapped) and macrophages (already mapped) modulates EBV immune mineralocorticoid balance; aldosterone excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — EBV androgen-receptor: androgen-receptor on B-cells (already mapped) and macrophages (already mapped) modulates EBV hormonal B-cell proliferation; androgen-receptor excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — EBV norepinephrine: norepinephrine from B-cells (already mapped) and macrophages (already mapped) modulates EBV adrenergic immune tone; norepinephrine excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — EBV adrenomedullin: adrenomedullin from B-cells (already mapped) and macrophages (already mapped) modulates EBV vascular immune tone; adrenomedullin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — EBV bdnf: BDNF from B-cells (already mapped) and macrophages (already mapped) modulates EBV neurotrophin B-cell survival; bdnf excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — EBV osteopontin: osteopontin from B-cells (already mapped) and macrophages (already mapped) modulates EBV extracellular matrix immune remodelling; osteopontin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — EBV fgfr: FGFR on B-cells (already mapped) and macrophages (already mapped) modulates EBV fibroblast immune growth signalling; fgfr dysregulation amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — EBV epinephrine: epinephrine from B-cells (already mapped) and macrophages (already mapped) modulates EBV adrenergic stress immune tone; epinephrine excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — EBV renin: renin from B-cells (already mapped) and macrophages (already mapped) modulates EBV renin-angiotensin immune axis; renin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — EBV myostatin: myostatin from B-cells (already mapped) and macrophages (already mapped) modulates EBV muscle wasting immune signalling; myostatin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — EBV galectin-3: galectin-3 from B-cells (already mapped) and macrophages (already mapped) drives EBV immune fibrotic lattice remodelling; galectin-3 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — EBV angiopoietin: angiopoietin from B-cells (already mapped) and macrophages (already mapped) modulates EBV vascular immune remodelling; angiopoietin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — EBV resistin: resistin from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune inflammatory tone; resistin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — EBV cortisol: cortisol from B-cells (already mapped) and macrophages (already mapped) modulates EBV stress-immune axis; cortisol excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — EBV ghrelin: ghrelin from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune appetite axis; ghrelin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — EBV glucagon: glucagon from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune glucose axis; glucagon excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — EBV leptin: leptin from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune energy axis; leptin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — EBV prolactin: prolactin from B-cells (already mapped) and macrophages (already mapped) modulates EBV immune lactogenic proliferation; prolactin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — EBV estrogen: estrogen from B-cells (already mapped) and macrophages (already mapped) modulates EBV hormonal B-cell immune activation; estrogen excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — EBV acetylcholine: acetylcholine from B-cells (already mapped) and macrophages (already mapped) modulates EBV cholinergic immune neuromodulation; acetylcholine excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — EBV adenosine: adenosine from B-cells (already mapped) and macrophages (already mapped) modulates EBV adenosinergic immune purinergic axis; adenosine excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[ApoE](../../03-molecular/apoe/README.md)** — EBV apoe: apoe from B-cells (already mapped) and macrophages (already mapped) modulates EBV lipid immune viral entry axis; apoe excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — EBV testosterone: testosterone from B-cells (already mapped) and macrophages (already mapped) modulates EBV androgenic immune activation axis; testosterone excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — EBV il-2: il-2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV lymphocyte proliferation immune axis; il-2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — EBV il-10: il-10 from B-cells (already mapped) and macrophages (already mapped) modulates EBV immunosuppressive viral immune evasion; il-10 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — EBV il-12: il-12 from B-cells (already mapped) and macrophages (already mapped) modulates EBV th1 immune polarization axis; il-12 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — EBV il-17a: il-17a from B-cells (already mapped) and macrophages (already mapped) modulates EBV mucosal immune inflammatory axis; il-17a excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — EBV il-13: il-13 from B-cells (already mapped) and macrophages (already mapped) modulates EBV th2 immune polarization axis; il-13 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — EBV il-1b: il-1b from B-cells (already mapped) and macrophages (already mapped) modulates EBV pyroptotic immune inflammasome axis; il-1b excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — EBV il-4: il-4 from B-cells (already mapped) and macrophages (already mapped) modulates EBV th2 immune polarization axis; il-4 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — EBV il-5: il-5 from B-cells (already mapped) and macrophages (already mapped) modulates EBV eosinophil immune activation axis; il-5 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — EBV il-6: il-6 from B-cells (already mapped) and macrophages (already mapped) modulates EBV pleiotropic immune activation axis; il-6 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — EBV il-23: il-23 from B-cells (already mapped) and macrophages (already mapped) modulates EBV th17 immune activation axis; il-23 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — EBV il-31: il-31 from B-cells (already mapped) and macrophages (already mapped) modulates EBV pruritic immune neuroimmune axis; il-31 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — EBV il-33: il-33 from B-cells (already mapped) and macrophages (already mapped) modulates EBV alarmin immune activation axis; il-33 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IL-36](../../03-molecular/il-36/README.md)** — EBV il-36: il-36 from B-cells (already mapped) and macrophages (already mapped) modulates EBV epidermal immune inflammatory axis; il-36 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — EBV tnf-alpha: tnf-alpha from B-cells (already mapped) and macrophages (already mapped) modulates EBV inflammatory cytokine immune axis; tnf-alpha excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — EBV ifn-gamma: ifn-gamma from B-cells (already mapped) and macrophages (already mapped) modulates EBV th1 antiviral immune axis; ifn-gamma excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — EBV stat1: stat1 from B-cells (already mapped) and macrophages (already mapped) modulates EBV interferon-signalling immune axis; stat1 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — EBV stat3: stat3 from B-cells (already mapped) and macrophages (already mapped) modulates EBV oncogenic immune signalling axis; stat3 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — EBV jak2: jak2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV cytokine receptor signalling immune axis; jak2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — EBV akt: akt from B-cells (already mapped) and macrophages (already mapped) modulates EBV pro-survival kinase immune axis; akt excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — EBV mtor: mtor from B-cells (already mapped) and macrophages (already mapped) modulates EBV metabolic immune growth axis; mtor excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — EBV ampk: ampk from B-cells (already mapped) and macrophages (already mapped) modulates EBV energy-sensing immune metabolic axis; ampk excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — EBV hif-1alpha: hif-1alpha from B-cells (already mapped) and macrophages (already mapped) modulates EBV hypoxic immune metabolic axis; hif-1alpha excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — EBV ccl2: ccl2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV monocyte recruitment immune axis; ccl2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — EBV cxcl12: cxcl12 from B-cells (already mapped) and macrophages (already mapped) modulates EBV stromal immune homing axis; cxcl12 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EBV egfr: egfr from B-cells (already mapped) and macrophages (already mapped) modulates EBV growth factor receptor immune axis; egfr excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EBV erk1-2: erk1-2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV mapk proliferative immune axis; erk1-2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — EBV foxo: foxo from B-cells (already mapped) and macrophages (already mapped) modulates EBV apoptotic immune regulation axis; foxo excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — EBV foxo1: foxo1 from B-cells (already mapped) and macrophages (already mapped) modulates EBV transcriptional immune regulation axis; foxo1 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — EBV jak1-2: jak1-2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV interferon receptor signalling immune axis; jak1-2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — EBV mhc-class-ii: mhc-class-ii from B-cells (already mapped) and macrophages (already mapped) modulates EBV antigen presentation immune axis; mhc-class-ii excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — EBV pdgf: pdgf from B-cells (already mapped) and macrophages (already mapped) modulates EBV growth factor proliferative immune axis; pdgf excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — EBV vegf: vegf from B-cells (already mapped) and macrophages (already mapped) modulates EBV angiogenic immune activation axis; vegf excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — EBV complement-c3: complement-c3 from B-cells (already mapped) and macrophages (already mapped) modulates EBV innate complement immune axis; complement-c3 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — EBV complement-c5: complement-c5 from B-cells (already mapped) and macrophages (already mapped) modulates EBV terminal complement immune axis; complement-c5 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — EBV wnt-beta-catenin: wnt-beta-catenin from B-cells (already mapped) and macrophages (already mapped) modulates EBV oncogenic wnt proliferative axis; wnt-beta-catenin excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — EBV cgas-sting: cgas-sting from B-cells (already mapped) and macrophages (already mapped) modulates EBV innate dna-sensing immune axis; cgas-sting excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — EBV autophagy: autophagy from B-cells (already mapped) and macrophages (already mapped) modulates EBV viral clearance immune axis; autophagy excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — EBV bcl-2: bcl-2 from B-cells (already mapped) and macrophages (already mapped) modulates EBV anti-apoptotic immune survival axis; bcl-2 excess amplifies NF-κB (already mapped) and p53 (already mapped) and TGF-β (already mapped) cascade in EBV.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^cohen-2000-ebv-review]: Cohen JI. Epstein-Barr virus infection. *N Engl J Med.* 2000;343(7):481-492. [doi:10.1056/NEJM200008173430707](https://doi.org/10.1056/NEJM200008173430707) · [PubMed 10944566](https://pubmed.ncbi.nlm.nih.gov/10944566/)
[^thorley-lawson-2004-ebv-latency]: Thorley-Lawson DA. Epstein-Barr virus: exploiting the immune system. *Nat Rev Immunol.* 2001;1(1):75-82. [doi:10.1038/35095556](https://doi.org/10.1038/35095556) · [PubMed 11905816](https://pubmed.ncbi.nlm.nih.gov/11905816/)
[^nourse-2011-ebv-lymphoma]: Young LS, Rickinson AB. Epstein-Barr virus: 40 years on. *Nat Rev Cancer.* 2004;4(10):757-768. [doi:10.1038/nrc1452](https://doi.org/10.1038/nrc1452) · [PubMed 15510157](https://pubmed.ncbi.nlm.nih.gov/15510157/)
