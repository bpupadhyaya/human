---
schema: human-scale-entry/v1
id: zika-virus
name: Zika Virus
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Zika virus (ZIKV; flavivirus; Aedes aegypti vector) caused the 2015-2016 Americas pandemic; congenital Zika syndrome (microcephaly) via AXL receptor neural progenitor cell tropism; NS5 degrades STAT2; Guillain-Barré association; sexually transmitted; no approved vaccine."
aliases: ["ZIKV", "Zika", "Zika fever", "congenital Zika syndrome", "Zika microcephaly", "Zika GBS", "Aedes Zika", "flavivirus Zika"]
sources:
  - id: musso-2016-zika-review
    type: peer-reviewed
    cite: "Musso D, Gubler DJ. Zika Virus. Clin Microbiol Rev. 2016;29(3):487-524."
    doi: "10.1128/CMR.00072-15"
    pmid: "27029595"
    url: "https://doi.org/10.1128/CMR.00072-15"
    accessed: "2026-06-08"
  - id: brasil-2016-zika-pregnancy
    type: peer-reviewed
    cite: "Brasil P, Pereira JP Jr, Moreira ME, et al. Zika Virus Infection in Pregnant Women in Rio de Janeiro. N Engl J Med. 2016;375(24):2321-2334."
    doi: "10.1056/NEJMoa1602412"
    pmid: "26943629"
    url: "https://doi.org/10.1056/NEJMoa1602412"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "ZIKV dsRNA replication intermediates activate RIG-I/MDA5 → MAVS → TBK1/IRF3 → IFN-β; fetal neural progenitor cells have reduced RIG-I/MAVS → impaired IFN-β → ZIKV amplifies unchecked in fetal brain; MAVS is required for adult innate control limiting ZIKV viremia."
  - target: 01-human/03-molecular/axl-receptor
    relation: connects-to
    note: "ZIKV E protein binds AXL on cortical neural progenitor cells (NPCs) → endocytosis → NPC infection; AXL and TYRO3 are highly expressed in fetal NPCs → ZIKV neural tropism and congenital microcephaly; AXL inhibitors reduce ZIKV NPC infection in cerebral organoid models."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "ZIKV NS5 degrades STAT2 via ubiquitin-proteasomal pathway → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 specifically targets human STAT2 (not mouse) → explains mouse resistance to ZIKV-induced microcephaly without IFNAR/STAT2 knockout in animal models."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "ZIKV and DENV share Aedes aegypti vector and flavivirus biology; cross-reactive anti-DENV antibodies may enhance ZIKV infection via ADE in Fcγ receptor-bearing cells; prior dengue immunity has complex effects on Zika severity; both NS5 proteins degrade STAT2 for IFN evasion."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "WNV and ZIKV are neurotropic flaviviruses; serological cross-reactivity and potential partial cross-protection; unlike ZIKV, WNV is not sexually transmitted and causes no congenital brain malformation; WNV neuroinvasive disease affects elderly/immunocompromised, not fetuses."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "ZIKV fibronectin: fibronectin scaffolds trophoblast and NPC extracellular matrix invaded by ZIKV; fibronectin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "ZIKV notch: ZIKV disrupts NOTCH signalling in neural progenitor cells, impairing self-renewal; NOTCH suppression by NS4A/NS4B amplifies NF-κB and IL-6 and type-i-interferon cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "ZIKV igf-1: ZIKV suppresses IGF-1 and AKT signalling in neural progenitor cells; igf-1 loss amplifies NF-κB and IL-6 and type-i-interferon cascade, compounding NPC depletion and microcephaly of congenital Zika syndrome."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "ZIKV activin-a: activin-A from fetal macrophages and NPCs drives ZIKV neural fibrotic remodelling; activin-a excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "ZIKV tgf-beta: TGF-β from fetal macrophages and NPCs modulates ZIKV immune-fibrotic neural remodelling; tgf-beta excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "ZIKV cgrp: CGRP from fetal macrophages and NPCs modulates ZIKV neuroimmune vascular tone; cgrp excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "ZIKV calcitonin: calcitonin from fetal macrophages and NPCs modulates ZIKV calcium balance; calcitonin dysregulation amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "ZIKV substance-p: substance-P from fetal macrophages and NPCs modulates ZIKV neuroimmune pain signalling; substance-p excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "ZIKV insulin-receptor: insulin-receptor on fetal macrophages and NPCs modulates ZIKV metabolic neural signalling; insulin-receptor dysregulation amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "ZIKV aldosterone: aldosterone from fetal macrophages and NPCs modulates ZIKV mineralocorticoid immune balance; aldosterone excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "ZIKV androgen-receptor: androgen-receptor on fetal macrophages and NPCs modulates ZIKV hormonal neural development; androgen-receptor dysregulation amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "ZIKV norepinephrine: norepinephrine from fetal macrophages and NPCs modulates ZIKV adrenergic neural tone; norepinephrine excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "ZIKV adrenomedullin: adrenomedullin from fetal macrophages and NPCs modulates ZIKV vascular neuroimmune tone; adrenomedullin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "ZIKV bdnf: BDNF from fetal macrophages and NPCs modulates ZIKV neurotrophin neural survival; bdnf excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "ZIKV osteopontin: osteopontin from fetal macrophages and NPCs modulates ZIKV extracellular matrix neural remodelling; osteopontin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "ZIKV fgfr: FGFR on fetal macrophages and NPCs drives ZIKV neural fibroblast growth signalling; fgfr dysregulation amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "ZIKV epinephrine: epinephrine from fetal macrophages and NPCs modulates ZIKV adrenergic neural stress response; epinephrine excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "ZIKV renin: renin from fetal macrophages and NPCs modulates ZIKV renin-angiotensin neural axis; renin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/myostatin
    relation: connects-to
    note: "ZIKV myostatin: myostatin from fetal macrophages and NPCs modulates ZIKV neural muscle wasting axis; myostatin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "ZIKV galectin-3: galectin-3 from fetal macrophages and NPCs drives ZIKV neural immune fibrotic lattice; galectin-3 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "ZIKV angiopoietin: angiopoietin from fetal macrophages and NPCs modulates ZIKV vascular neural immune remodelling; angiopoietin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "ZIKV resistin: resistin from fetal macrophages and NPCs modulates ZIKV metabolic neural inflammatory tone; resistin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "ZIKV cortisol: cortisol from fetal macrophages and NPCs modulates ZIKV stress-immune HPA neural axis; cortisol excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "ZIKV ghrelin: ghrelin from fetal macrophages and NPCs modulates ZIKV metabolic neural appetite axis; ghrelin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "ZIKV glucagon: glucagon from fetal macrophages and NPCs modulates ZIKV metabolic neural glucose axis; glucagon excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "ZIKV leptin: leptin from fetal macrophages and NPCs modulates ZIKV metabolic neural energy axis; leptin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "ZIKV prolactin: prolactin from fetal macrophages and NPCs modulates ZIKV immune neural lactogenic tone; prolactin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "ZIKV estrogen: estrogen from fetal macrophages and NPCs modulates ZIKV hormonal neural immune axis; estrogen excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "ZIKV acetylcholine: acetylcholine from fetal macrophages and NPCs modulates ZIKV cholinergic neural immune axis; acetylcholine excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "ZIKV adenosine: adenosine from fetal macrophages and NPCs modulates ZIKV purinergic neural immune axis; adenosine excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/apoe
    relation: connects-to
    note: "ZIKV apoe: apoe from fetal macrophages and NPCs modulates ZIKV lipid neural immune entry axis; apoe excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "ZIKV testosterone: testosterone from fetal macrophages and NPCs modulates ZIKV androgenic neural immune axis; testosterone excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "ZIKV il-2: il-2 from fetal macrophages and NPCs modulates ZIKV neural lymphocyte activation axis; il-2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "ZIKV il-10: il-10 from fetal macrophages and NPCs modulates ZIKV immunosuppressive neural immune regulation; il-10 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "ZIKV il-12: il-12 from fetal macrophages and NPCs modulates ZIKV neural th1 immune polarization axis; il-12 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "ZIKV il-17a: il-17a from fetal macrophages and NPCs modulates ZIKV mucosal neural immune inflammatory axis; il-17a excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "ZIKV il-13: il-13 from fetal macrophages and NPCs modulates ZIKV neural th2 immune polarization; il-13 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "ZIKV il-1b: il-1b from fetal macrophages and NPCs modulates ZIKV neural pyroptotic immune axis; il-1b excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "ZIKV il-4: il-4 from fetal macrophages and NPCs modulates ZIKV neural th2 immune polarization; il-4 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "ZIKV il-5: il-5 from fetal macrophages and NPCs modulates ZIKV neural eosinophil immune axis; il-5 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "ZIKV il-6: il-6 from fetal macrophages and NPCs modulates ZIKV neural pleiotropic immune axis; il-6 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "ZIKV il-23: il-23 from fetal macrophages and NPCs modulates ZIKV neural th17 immune activation; il-23 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "ZIKV il-31: il-31 from fetal macrophages and NPCs modulates ZIKV neural pruritic immune axis; il-31 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "ZIKV il-33: il-33 from fetal macrophages and NPCs modulates ZIKV neural alarmin immune activation; il-33 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/il-36
    relation: connects-to
    note: "ZIKV il-36: il-36 from fetal macrophages and NPCs modulates ZIKV neural epidermal immune axis; il-36 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "ZIKV tnf-alpha: tnf-alpha from fetal macrophages and NPCs modulates ZIKV neuroinflammatory cytokine storm axis; tnf-alpha excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "ZIKV ifn-gamma: ifn-gamma from fetal macrophages and NPCs modulates ZIKV neural th1 antiviral immune axis; ifn-gamma excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "ZIKV stat1: stat1 from fetal macrophages and NPCs modulates ZIKV neural interferon-signalling immune axis; stat1 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "ZIKV stat3: stat3 from fetal macrophages and NPCs modulates ZIKV neural oncogenic immune signalling axis; stat3 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "ZIKV jak2: jak2 from fetal macrophages and NPCs modulates ZIKV neural cytokine receptor signalling axis; jak2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "ZIKV akt: akt from fetal macrophages and NPCs modulates ZIKV neural pro-survival kinase axis; akt excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "ZIKV mtor: mtor from fetal macrophages and NPCs modulates ZIKV neural metabolic immune growth axis; mtor excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "ZIKV ampk: ampk from fetal macrophages and NPCs modulates ZIKV neural energy-sensing immune metabolic axis; ampk excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "ZIKV hif-1alpha: hif-1alpha from fetal macrophages and NPCs modulates ZIKV neural hypoxic immune axis; hif-1alpha excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "ZIKV ccl2: ccl2 from fetal macrophages and NPCs modulates ZIKV neural monocyte recruitment axis; ccl2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "ZIKV cxcl12: cxcl12 from fetal macrophages and NPCs modulates ZIKV neural stromal immune homing axis; cxcl12 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "ZIKV egfr: egfr from fetal macrophages and NPCs modulates ZIKV neural growth factor receptor axis; egfr excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ZIKV erk1-2: erk1-2 from fetal macrophages and NPCs modulates ZIKV neural mapk proliferative axis; erk1-2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "ZIKV foxo: foxo from fetal macrophages and NPCs modulates ZIKV neural apoptotic immune regulation; foxo excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "ZIKV foxo1: foxo1 from fetal macrophages and NPCs modulates ZIKV neural transcriptional immune regulation; foxo1 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "ZIKV jak1-2: jak1-2 from fetal macrophages and NPCs modulates ZIKV neural interferon receptor signalling axis; jak1-2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "ZIKV mhc-class-ii: mhc-class-ii from fetal macrophages and NPCs modulates ZIKV neural antigen presentation immune axis; mhc-class-ii excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "ZIKV pdgf: pdgf from fetal macrophages and NPCs modulates ZIKV neural growth factor proliferative axis; pdgf excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "ZIKV vegf: vegf from fetal macrophages and NPCs modulates ZIKV neural angiogenic immune activation axis; vegf excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "ZIKV complement-c3: complement-c3 from fetal macrophages and NPCs modulates ZIKV neural innate complement axis; complement-c3 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "ZIKV complement-c5: complement-c5 from fetal macrophages and NPCs modulates ZIKV neural terminal complement axis; complement-c5 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "ZIKV wnt-beta-catenin: wnt-beta-catenin from fetal macrophages and NPCs modulates ZIKV neural wnt proliferative axis; wnt-beta-catenin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "ZIKV cgas-sting: cgas-sting from fetal macrophages and NPCs modulates ZIKV neural innate dna-sensing immune axis; cgas-sting excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "ZIKV autophagy: autophagy from fetal macrophages and NPCs modulates ZIKV neural viral clearance immune axis; autophagy excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "ZIKV bcl-2: bcl-2 from fetal macrophages and NPCs modulates ZIKV neural anti-apoptotic immune survival axis; bcl-2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/ace2
    relation: connects-to
    note: "ZIKV ace2: ace2 from fetal macrophages and NPCs modulates ZIKV neural viral receptor immune entry axis; ace2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "ZIKV btk: btk from fetal macrophages and NPCs modulates ZIKV neural b-cell receptor signalling axis; btk excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "ZIKV caspase-3: caspase-3 from fetal macrophages and NPCs modulates ZIKV neural apoptotic execution immune axis; caspase-3 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "ZIKV cd20: cd20 from fetal macrophages and NPCs modulates ZIKV neural b-cell surface immune activation axis; cd20 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "ZIKV cdk4-6: cdk4-6 from fetal macrophages and NPCs modulates ZIKV neural cell-cycle immune progression axis; cdk4-6 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "ZIKV cyclin-d1: cyclin-d1 from fetal macrophages and NPCs modulates ZIKV neural g1 cell-cycle immune progression; cyclin-d1 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "ZIKV adiponectin: adiponectin from fetal macrophages and NPCs modulates ZIKV neural adipokine immune metabolic axis; adiponectin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "ZIKV angiotensin-ii: angiotensin-ii from fetal macrophages and NPCs modulates ZIKV neural renin-angiotensin immune axis; angiotensin-ii excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome."
---

# Zika Virus

## Overview

**Zika virus (ZIKV)** is a positive-sense single-stranded RNA virus of the family *Flaviviridae* (genus *Flavivirus*), transmitted primarily by the bite of *Aedes aegypti* and *Aedes albopictus* mosquitoes. First isolated from a sentinel monkey in the Zika Forest of Uganda in 1947, ZIKV remained an obscure tropical pathogen until it emerged explosively in the Pacific Islands (2007, 2013-2014) and then caused a pandemic across the Americas beginning in 2015, centered in Brazil [^musso-2016-zika-review].

The ZIKV pandemic revealed two unexpected features that transformed ZIKV from a clinical curiosity into a global health emergency:

1. **Congenital Zika syndrome**: Intrauterine ZIKV infection causes severe fetal brain malformations — particularly **microcephaly** (head circumference >3 SD below mean) — due to infection and destruction of cortical neural progenitor cells (NPCs) via the **AXL receptor tyrosine kinase** [^brasil-2016-zika-pregnancy]. This was the first demonstration that a mosquito-borne virus causes congenital brain malformations, prompting WHO to declare a Public Health Emergency of International Concern (PHEIC) in February 2016.

2. **Sexual transmission**: ZIKV persists in semen for >6 months after acute infection, enabling sexual transmission — unusual for an arboviral flavivirus and requiring novel prevention messaging for pregnant couples.

**Clinical spectrum:**
- **Asymptomatic**: ~80% of infections
- **Acute Zika fever**: Mild fever, maculopapular rash, arthralgia, conjunctivitis, headache; 2–7 days; self-limited; rarely hospitalization
- **Guillain-Barré syndrome (GBS)**: ~1 per 4,000 symptomatic Zika infections; acute motor polyneuropathy; typically AIDP or AMSAN pattern; peak risk 1–3 weeks after acute illness; usually recovers but severe cases require ICU
- **Congenital Zika syndrome**: Microcephaly, ventriculomegaly, cerebellar hypoplasia, lissencephaly, subcortical calcifications, clubfoot, joint contractures, ocular malformations (chorioretinal scarring, optic atrophy)

## Structure

### Zika virus biology

ZIKV is an enveloped virus (~50 nm) with a **10.8 kb positive-sense ssRNA genome** encoding a single polyprotein:

| Protein | Function |
|---------|----------|
| C (capsid) | Nucleocapsid; lipid droplet association |
| prM/M | Precursor membrane protein; furin-cleaved during maturation |
| E (envelope) | Receptor binding (AXL, DC-SIGN, heparan sulfate); membrane fusion; neutralizing antibody target |
| NS1 | Secreted hexamer; complement activation; endothelial disruption |
| NS2A/2B | Replication complex assembly; NS2B is NS3 cofactor |
| NS3 | Serine protease + RNA helicase |
| NS4A/4B | Membrane remodeling; NS4B blocks IFN-β signaling |
| NS5 | RNA-dependent RNA polymerase + methyltransferase; **degrades STAT2** → IFN evasion |

### Comparison with dengue

ZIKV shares ~57% amino acid identity with DENV2. Key differences:
- **Unique AXL tropism**: ZIKV E protein domain III binds AXL more efficiently than DENV E → neural cell tropism
- **Sexual transmission**: ZIKV persists in testes/epididymis; DENV does not transmit sexually
- **Congenital disease**: ZIKV causes microcephaly; DENV does not cross placenta efficiently
- **No ADE-driven hemorrhagic fever**: Unlike DENV, severe secondary ZIKV in ADE setting is not the dominant clinical concern
- **STAT2 degradation**: Both use NS5 to target STAT2, but via slightly different E3 ligase interactions; both are human STAT2-specific

## Function

### Neural tropism — congenital Zika syndrome mechanism

The pivotal discovery of 2016 was ZIKV's selective infection of cortical neural progenitor cells (NPCs):

1. **AXL receptor expression**: AXL tyrosine kinase is highly expressed on radial glia (the cortical NPC population), Hofbauer cells in placenta, and trophoblasts. TYRO3 is co-expressed. AXL mediates apoptotic body phagocytosis → ZIKV exploits this "eat-me signal" pathway to enter cells.

2. **Placental crossing**: ZIKV infects trophoblasts and Hofbauer macrophages via AXL and DC-SIGN → amniotic fluid → fetal compartment. Risk highest in first trimester (organogenesis).

3. **NPC infection**: ZIKV infects radial glia → triggers apoptosis and autophagy → reduces NPC pool → impaired cortical neurogenesis → microcephaly. The outer subventricular zone (oSVZ) NPCs, critical for human brain expansion, are particularly vulnerable.

4. **Reduced innate immunity in NPCs**: Fetal NPCs express lower RIG-I, MAVS, and type I IFN compared to adult cells → reduced antiviral response → sustained ZIKV replication in NPCs → greater cell death.

5. **Direct CNS effects**: ZIKV also infects astrocytes and microglia → neuroinflammation; mitotic spindle disruption in NPCs impairs cell division independent of apoptosis.

### Immune response and evasion

| Component | Response | ZIKV counter |
|-----------|----------|--------------|
| RIG-I/MDA5 | Sense ZIKV dsRNA → MAVS → IFN-β | NS4B blocks RIG-I signaling |
| Type I IFN | ISG induction → antiviral state | NS5 degrades STAT2 → blocks ISG transcription |
| Complement | NS1 activates C4b-binding protein → C5a | Mimics dengue NS1 mechanism |
| Adaptive | CD8+ T cells; neutralizing anti-E antibodies | Viral diversity limits cross-protection |
| Cross-reactive DENV | Anti-DENV IgG binds ZIKV → potential ADE | Observed in vitro; clinical significance debated |

### Guillain-Barré syndrome mechanism

Proposed mechanism: **molecular mimicry** between ZIKV envelope glycan epitopes and ganglioside GM1 on peripheral nerve myelin → autoantibodies cross-reactive with gangliosides → complement-mediated nerve damage. Evidence:
- Epidemiological: GBS incidence 10-fold higher in ZIKV-exposed populations
- Immunological: Anti-GM1 and anti-GD1b antibodies found in some ZIKV-GBS patients
- Timing: GBS onset 5–14 days after acute Zika fever (consistent with post-infectious autoimmunity)
- Treatment: IV immunoglobulin (IVIG); plasmapheresis for severe cases

## Pathology

### Congenital surveillance and diagnosis

**In pregnancy:**
- Maternal: RT-PCR of blood/urine (positive within 2 weeks of symptom onset); serology (IgM) after 2 weeks — cross-reactive with DENV antibodies (plaque reduction neutralization test PRNT required for confirmation)
- Fetal: Amniocentesis (RT-PCR of amniotic fluid); serial fetal head circumference ultrasound; MRI if microcephaly suspected
- Postnatal: Infant RT-PCR (urine, CSF, serum); brain ultrasound or MRI; ophthalmology examination; audiometry

**Fetal outcomes** after ZIKV in first trimester: ~1–30% risk of fetal brain abnormality (wide range across studies depending on case ascertainment); 2016 Brazilian cohort: microcephaly in ~1% of live births in endemic areas at peak transmission.

### Post-acute sequelae

- Prolonged arthralgia (weeks-months)
- Persistent ZIKV RNA in semen (>6 months in some cases)
- Ophthalmological: Anterior uveitis, macular lesions in adults (rare)
- Encephalitis/myelitis (rare adult complication)
- GBS recovery: Most patients recover substantially over 3–6 months; ~15% have residual deficits

### Treatment and prevention

**No approved antiviral therapy.** Management is supportive:
- Acute: Paracetamol for fever/pain (avoid NSAIDs in first 2 weeks — dengue cannot be excluded without testing)
- GBS: IVIG 2 g/kg or plasmapheresis; ICU if respiratory compromise

**Prevention:**
- Mosquito control (insecticide-treated bed nets, indoor spraying, larval source reduction)
- **Sexual transmission**: Condoms for ≥6 months after potential ZIKV exposure in men, ≥2 months in women
- **Travel advisory**: Pregnant women advised to avoid travel to ZIKV-endemic areas; those who travel should use strict mosquito precautions

**No approved vaccine:**
- mRNA, DNA, live-attenuated, subunit vaccines in Phase I/II trials
- Challenges: AXL receptor involvement in NPC tropism needs to be addressed without blocking AXL function; cross-reactivity with dengue antigens complicates design
- Timeline: No vaccine approval expected until 2026+ given reduced outbreak transmission

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: ZIKV replication intermediates (dsRNA) activate RIG-I/MDA5 → MAVS → TBK1/IRF3 → IFN-β; fetal neural progenitor cells have reduced MAVS/RIG-I expression → impaired IFN-β response → ZIKV amplifies unchecked in fetal brain; MAVS is required for adult innate control of ZIKV infection.

**→ [AXL Receptor](../../../03-molecular/axl-receptor/)**: ZIKV E protein binds AXL receptor on cortical neural progenitor cells (NPCs) → clathrin-mediated endocytosis → NPC infection; AXL and TYRO3 are highly expressed in fetal NPCs → ZIKV neural tropism and microcephaly; AXL inhibitors (bemcentinib) reduce ZIKV NPC infection in brain organoids.

**→ [STAT1](../../../03-molecular/stat1/)**: ZIKV NS5 degrades STAT2 via ubiquitin-proteasomal pathway → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 specifically targets human STAT2 (not mouse) → explains mouse resistance to ZIKV-induced microcephaly without IFNAR/STAT2 knockout in animal models.

**→ [Dengue Fever](../dengue-fever/)**: ZIKV and DENV share Aedes aegypti vector and flavivirus biology; cross-reactive anti-DENV antibodies may enhance ZIKV infection via ADE in Fcγ receptor-bearing cells; prior dengue immunity has complex effects on Zika severity; both NS5 proteins degrade STAT2 for IFN evasion.

**→ [West Nile Virus](../west-nile-virus/)**: WNV and ZIKV are neurotropic flaviviruses; serological cross-reactivity and potential partial cross-protection; unlike ZIKV, WNV is not sexually transmitted and causes no congenital brain malformation; WNV neuroinvasive disease affects elderly/immunocompromised, not fetuses.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — ZIKV fibronectin: fibronectin scaffolds trophoblast and NPC extracellular matrix invaded by ZIKV; fibronectin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — ZIKV notch: ZIKV disrupts NOTCH signalling in neural progenitor cells, impairing self-renewal; NOTCH suppression by NS4A/NS4B amplifies NF-κB and IL-6 and type-i-interferon cascade of congenital Zika syndrome.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — ZIKV igf-1: ZIKV suppresses IGF-1 and AKT signalling in neural progenitor cells; igf-1 loss amplifies NF-κB and IL-6 and type-i-interferon cascade, compounding NPC depletion and microcephaly of congenital Zika syndrome.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — ZIKV activin-a: activin-A from fetal macrophages and NPCs drives ZIKV neural fibrotic remodelling; activin-a excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — ZIKV tgf-beta: TGF-β from fetal macrophages and NPCs modulates ZIKV immune-fibrotic neural remodelling; tgf-beta excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — ZIKV cgrp: CGRP from fetal macrophages and NPCs modulates ZIKV neuroimmune vascular tone; cgrp excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — ZIKV calcitonin: calcitonin from fetal macrophages and NPCs modulates ZIKV calcium balance; calcitonin dysregulation amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — ZIKV substance-p: substance-P from fetal macrophages and NPCs modulates ZIKV neuroimmune pain signalling; substance-p excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — ZIKV insulin-receptor: insulin-receptor on fetal macrophages and NPCs modulates ZIKV metabolic neural signalling; insulin-receptor dysregulation amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — ZIKV aldosterone: aldosterone from fetal macrophages and NPCs modulates ZIKV mineralocorticoid immune balance; aldosterone excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — ZIKV androgen-receptor: androgen-receptor on fetal macrophages and NPCs modulates ZIKV hormonal neural development; androgen-receptor dysregulation amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — ZIKV norepinephrine: norepinephrine from fetal macrophages and NPCs modulates ZIKV adrenergic neural tone; norepinephrine excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — ZIKV adrenomedullin: adrenomedullin from fetal macrophages and NPCs modulates ZIKV vascular neuroimmune tone; adrenomedullin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — ZIKV bdnf: BDNF from fetal macrophages and NPCs modulates ZIKV neurotrophin neural survival; bdnf excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — ZIKV osteopontin: osteopontin from fetal macrophages and NPCs modulates ZIKV extracellular matrix neural remodelling; osteopontin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — ZIKV fgfr: FGFR on fetal macrophages and NPCs drives ZIKV neural fibroblast growth signalling; fgfr dysregulation amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — ZIKV epinephrine: epinephrine from fetal macrophages and NPCs modulates ZIKV adrenergic neural stress response; epinephrine excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — ZIKV renin: renin from fetal macrophages and NPCs modulates ZIKV renin-angiotensin neural axis; renin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Myostatin](../../03-molecular/myostatin/README.md)** — ZIKV myostatin: myostatin from fetal macrophages and NPCs modulates ZIKV neural muscle wasting axis; myostatin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — ZIKV galectin-3: galectin-3 from fetal macrophages and NPCs drives ZIKV neural immune fibrotic lattice; galectin-3 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — ZIKV angiopoietin: angiopoietin from fetal macrophages and NPCs modulates ZIKV vascular neural immune remodelling; angiopoietin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — ZIKV resistin: resistin from fetal macrophages and NPCs modulates ZIKV metabolic neural inflammatory tone; resistin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — ZIKV cortisol: cortisol from fetal macrophages and NPCs modulates ZIKV stress-immune HPA neural axis; cortisol excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — ZIKV ghrelin: ghrelin from fetal macrophages and NPCs modulates ZIKV metabolic neural appetite axis; ghrelin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — ZIKV glucagon: glucagon from fetal macrophages and NPCs modulates ZIKV metabolic neural glucose axis; glucagon excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — ZIKV leptin: leptin from fetal macrophages and NPCs modulates ZIKV metabolic neural energy axis; leptin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — ZIKV prolactin: prolactin from fetal macrophages and NPCs modulates ZIKV immune neural lactogenic tone; prolactin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — ZIKV estrogen: estrogen from fetal macrophages and NPCs modulates ZIKV hormonal neural immune axis; estrogen excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — ZIKV acetylcholine: acetylcholine from fetal macrophages and NPCs modulates ZIKV cholinergic neural immune axis; acetylcholine excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — ZIKV adenosine: adenosine from fetal macrophages and NPCs modulates ZIKV purinergic neural immune axis; adenosine excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[ApoE](../../03-molecular/apoe/README.md)** — ZIKV apoe: apoe from fetal macrophages and NPCs modulates ZIKV lipid neural immune entry axis; apoe excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — ZIKV testosterone: testosterone from fetal macrophages and NPCs modulates ZIKV androgenic neural immune axis; testosterone excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — ZIKV il-2: il-2 from fetal macrophages and NPCs modulates ZIKV neural lymphocyte activation axis; il-2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — ZIKV il-10: il-10 from fetal macrophages and NPCs modulates ZIKV immunosuppressive neural immune regulation; il-10 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — ZIKV il-12: il-12 from fetal macrophages and NPCs modulates ZIKV neural th1 immune polarization axis; il-12 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — ZIKV il-17a: il-17a from fetal macrophages and NPCs modulates ZIKV mucosal neural immune inflammatory axis; il-17a excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — ZIKV il-13: il-13 from fetal macrophages and NPCs modulates ZIKV neural th2 immune polarization; il-13 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — ZIKV il-1b: il-1b from fetal macrophages and NPCs modulates ZIKV neural pyroptotic immune axis; il-1b excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — ZIKV il-4: il-4 from fetal macrophages and NPCs modulates ZIKV neural th2 immune polarization; il-4 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — ZIKV il-5: il-5 from fetal macrophages and NPCs modulates ZIKV neural eosinophil immune axis; il-5 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — ZIKV il-6: il-6 from fetal macrophages and NPCs modulates ZIKV neural pleiotropic immune axis; il-6 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — ZIKV il-23: il-23 from fetal macrophages and NPCs modulates ZIKV neural th17 immune activation; il-23 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — ZIKV il-31: il-31 from fetal macrophages and NPCs modulates ZIKV neural pruritic immune axis; il-31 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — ZIKV il-33: il-33 from fetal macrophages and NPCs modulates ZIKV neural alarmin immune activation; il-33 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IL-36](../../03-molecular/il-36/README.md)** — ZIKV il-36: il-36 from fetal macrophages and NPCs modulates ZIKV neural epidermal immune axis; il-36 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — ZIKV tnf-alpha: tnf-alpha from fetal macrophages and NPCs modulates ZIKV neuroinflammatory cytokine storm axis; tnf-alpha excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — ZIKV ifn-gamma: ifn-gamma from fetal macrophages and NPCs modulates ZIKV neural th1 antiviral immune axis; ifn-gamma excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — ZIKV stat1: stat1 from fetal macrophages and NPCs modulates ZIKV neural interferon-signalling immune axis; stat1 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — ZIKV stat3: stat3 from fetal macrophages and NPCs modulates ZIKV neural oncogenic immune signalling axis; stat3 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — ZIKV jak2: jak2 from fetal macrophages and NPCs modulates ZIKV neural cytokine receptor signalling axis; jak2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — ZIKV akt: akt from fetal macrophages and NPCs modulates ZIKV neural pro-survival kinase axis; akt excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — ZIKV mtor: mtor from fetal macrophages and NPCs modulates ZIKV neural metabolic immune growth axis; mtor excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — ZIKV ampk: ampk from fetal macrophages and NPCs modulates ZIKV neural energy-sensing immune metabolic axis; ampk excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — ZIKV hif-1alpha: hif-1alpha from fetal macrophages and NPCs modulates ZIKV neural hypoxic immune axis; hif-1alpha excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — ZIKV ccl2: ccl2 from fetal macrophages and NPCs modulates ZIKV neural monocyte recruitment axis; ccl2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — ZIKV cxcl12: cxcl12 from fetal macrophages and NPCs modulates ZIKV neural stromal immune homing axis; cxcl12 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — ZIKV egfr: egfr from fetal macrophages and NPCs modulates ZIKV neural growth factor receptor axis; egfr excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ZIKV erk1-2: erk1-2 from fetal macrophages and NPCs modulates ZIKV neural mapk proliferative axis; erk1-2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — ZIKV foxo: foxo from fetal macrophages and NPCs modulates ZIKV neural apoptotic immune regulation; foxo excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — ZIKV foxo1: foxo1 from fetal macrophages and NPCs modulates ZIKV neural transcriptional immune regulation; foxo1 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — ZIKV jak1-2: jak1-2 from fetal macrophages and NPCs modulates ZIKV neural interferon receptor signalling axis; jak1-2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — ZIKV mhc-class-ii: mhc-class-ii from fetal macrophages and NPCs modulates ZIKV neural antigen presentation immune axis; mhc-class-ii excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — ZIKV pdgf: pdgf from fetal macrophages and NPCs modulates ZIKV neural growth factor proliferative axis; pdgf excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — ZIKV vegf: vegf from fetal macrophages and NPCs modulates ZIKV neural angiogenic immune activation axis; vegf excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — ZIKV complement-c3: complement-c3 from fetal macrophages and NPCs modulates ZIKV neural innate complement axis; complement-c3 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — ZIKV complement-c5: complement-c5 from fetal macrophages and NPCs modulates ZIKV neural terminal complement axis; complement-c5 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — ZIKV wnt-beta-catenin: wnt-beta-catenin from fetal macrophages and NPCs modulates ZIKV neural wnt proliferative axis; wnt-beta-catenin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — ZIKV cgas-sting: cgas-sting from fetal macrophages and NPCs modulates ZIKV neural innate dna-sensing immune axis; cgas-sting excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — ZIKV autophagy: autophagy from fetal macrophages and NPCs modulates ZIKV neural viral clearance immune axis; autophagy excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — ZIKV bcl-2: bcl-2 from fetal macrophages and NPCs modulates ZIKV neural anti-apoptotic immune survival axis; bcl-2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[ACE2](../../03-molecular/ace2/README.md)** — ZIKV ace2: ace2 from fetal macrophages and NPCs modulates ZIKV neural viral receptor immune entry axis; ace2 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — ZIKV btk: btk from fetal macrophages and NPCs modulates ZIKV neural b-cell receptor signalling axis; btk excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — ZIKV caspase-3: caspase-3 from fetal macrophages and NPCs modulates ZIKV neural apoptotic execution immune axis; caspase-3 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — ZIKV cd20: cd20 from fetal macrophages and NPCs modulates ZIKV neural b-cell surface immune activation axis; cd20 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — ZIKV cdk4-6: cdk4-6 from fetal macrophages and NPCs modulates ZIKV neural cell-cycle immune progression axis; cdk4-6 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — ZIKV cyclin-d1: cyclin-d1 from fetal macrophages and NPCs modulates ZIKV neural g1 cell-cycle immune progression; cyclin-d1 excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — ZIKV adiponectin: adiponectin from fetal macrophages and NPCs modulates ZIKV neural adipokine immune metabolic axis; adiponectin excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — ZIKV angiotensin-ii: angiotensin-ii from fetal macrophages and NPCs modulates ZIKV neural renin-angiotensin immune axis; angiotensin-ii excess amplifies NF-κB and IL-6 and type-i-interferon neuroinflammatory cascade of congenital Zika syndrome.
