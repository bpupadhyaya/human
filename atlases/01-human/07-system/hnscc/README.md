---
schema: human-scale-entry/v1
id: hnscc
name: HNSCC
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Head and neck SCC; HPV+ oropharyngeal HNSCC (TP53 WT, PI3K-active) has better prognosis than HPV-negative (TP53 ~80%, CDKN2A ~40%); cetuximab and pembrolizumab are approved; KEYNOTE-048 defines first-line pembrolizumab over EXTREME in PD-L1+ recurrent/metastatic disease."
aliases: ["HNSCC", "head and neck squamous cell carcinoma", "oral cavity cancer", "oropharyngeal cancer", "HPV-positive HNSCC", "laryngeal cancer", "hypopharyngeal cancer", "head and neck cancer"]
sources:
  - id: burtness-2019-keynote048
    type: peer-reviewed
    cite: "Burtness B, Harrington KJ, Greil R, et al. Pembrolizumab alone or with chemotherapy versus cetuximab with chemotherapy for recurrent or metastatic squamous cell carcinoma of the head and neck (KEYNOTE-048). Lancet. 2019;394(10212):1915-1928."
    doi: "10.1016/S0140-6736(19)32591-7"
    pmid: "31679945"
    url: "https://doi.org/10.1016/S0140-6736(19)32591-7"
  - id: vermorken-2008-extreme
    type: peer-reviewed
    cite: "Vermorken JB, Mesia R, Rivera F, et al. Platinum-based chemotherapy plus cetuximab in head and neck cancer. N Engl J Med. 2008;359(11):1116-1127."
    doi: "10.1056/NEJMoa0802656"
    pmid: "18784101"
    url: "https://doi.org/10.1056/NEJMoa0802656"
cross_links:
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR overexpression in ~90% of HNSCC (copy number gain, not mutation); cetuximab + cisplatin/5-FU (EXTREME) improved OS vs. chemo alone (10.1 vs. 7.4 months); cetuximab+radiation is definitive for locally advanced HNSCC in platinum-ineligible patients."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Pembrolizumab (KEYNOTE-048) improved OS vs. EXTREME in PD-L1 CPS≥20 (14.9 vs. 10.7 months) and CPS≥1 (13.6 vs. 10.4 months); pembrolizumab+chemotherapy improved OS for CPS≥1; nivolumab (CheckMate 141) improved OS vs. chemotherapy in platinum-refractory R/M HNSCC."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations in ~80% of HPV-negative HNSCC (UV and tobacco mutational signatures; R175H, R248W hotspots); HPV-positive HNSCC has WT TP53 (HPV E6 degrades p53 via E6AP ubiquitin ligase); TP53 mutation correlates with poor prognosis and cisplatin resistance in HNSCC."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA mutation/amplification in ~20-30% of HNSCC; especially HPV+ oropharyngeal HNSCC (HPV E7 → RB disruption → CDK activation; higher PI3K pathway activity); PI3K inhibitors (copanlisib, alpelisib) studied in HNSCC; AKT inhibitors in clinical trials."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Epstein-Barr virus — not HPV — drives nasopharyngeal carcinoma, a distinct head-and-neck SCC: >95% of endemic undifferentiated NPC is EBV+; EBER in-situ hybridization confirms it and plasma EBV DNA tracks tumor burden; pembrolizumab and nivolumab are active in recurrent EBV+ NPC."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "HPV16 E7 binds and inactivates RB1, releasing E2F to drive S-phase entry without mitogens — the RB arm of HPV oncogenesis that pairs with E6-mediated p53 degradation; because RB is disabled by protein, HPV+ HNSCC rarely carries RB1 or CDKN2A mutations."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A/p16 behaves oppositely by HPV status: deleted in ~40% of tobacco-driven HPV-negative HNSCC, but strongly overexpressed in HPV+ tumors (RB loss removes feedback), making p16 immunostaining the practical surrogate marker for HPV-positive oropharyngeal cancer."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Head and neck and esophageal squamous cell carcinomas are linked by field cancerization: chronic alcohol and tobacco mutagenizes the whole aerodigestive squamous mucosa, so HNSCC patients carry elevated risk of esophageal SCC — both TP53-driven, immunotherapy-responsive tumors."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "HNSCC and cervical cancer are united by HPV: high-risk HPV16 drives oropharyngeal HNSCC as it drives cervical cancer, E6 degrading p53 and E7 inactivating RB; HPV-positive oropharyngeal cancer has a better prognosis than tobacco-driven HNSCC, and the same vaccine prevents both."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "HNSCC is one of the more immunogenic solid tumors — heavy tobacco or viral mutational load generates neoantigens — so anti-PD-1 (pembrolizumab, nivolumab) reactivating cytotoxic CD8+ T cells extended survival in recurrent/metastatic disease (KEYNOTE-048, CheckMate 141)."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol is a primary cause of head and neck squamous cell carcinoma: acetaldehyde is a direct mucosal carcinogen that synergizes strongly with tobacco to multiply oral, pharyngeal and laryngeal cancer risk—an etiology distinct from the HPV-driven oropharyngeal subset."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Tobacco smoke is the dominant cause of head and neck squamous cell carcinoma: its carbon-based polycyclic aromatic hydrocarbons and nitrosamines damage upper-aerodigestive mucosal DNA, producing field cancerization with multiple primaries, especially when combined with alcohol."
  - target: 02-pathogen/01-viruses/hpv-16
    relation: connects-to
    note: "HPV-16 drives a distinct, rising subset of head and neck squamous cell carcinoma: the virus infects oropharyngeal (tonsil, base of tongue) crypt epithelium, its E6/E7 oncoproteins inactivating p53 and Rb; HPV-positive HNSCC affects younger non-smokers and has a better prognosis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is central to head and neck cancer: definitive chemoradiation can cure many HNSCCs (especially HPV-positive oropharyngeal tumors) and organ-preserve the larynx, while IMRT spares salivary glands—radiation is as pivotal here as surgery."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Cancer-associated fibroblasts shape head and neck cancer: HNSCC recruits and reprograms fibroblasts that secrete growth factors, remodel matrix and blunt immunity, promoting invasion and resistance—making the fibroblast-rich microenvironment a therapeutic target."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "Head and neck cancer and thyroid cancer both arise in the neck but differ: HNSCC is a smoking/HPV-driven squamous carcinoma of the aerodigestive mucosa, while thyroid cancer is a usually indolent endocrine tumor—neck radiation, a thyroid-cancer risk factor, links them."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "HNSCC and lung cancer share tobacco field cancerization: the same carcinogen exposure mutates the entire aerodigestive lining, so head-and-neck cancer patients carry a high risk of synchronous or later lung cancer—warranting chest screening and smoking cessation."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Tumor-associated macrophages shape HNSCC: they infiltrate the tumor, suppress T-cell responses and promote invasion and angiogenesis, contributing to the immunosuppressive microenvironment that immune checkpoint inhibitors aim to reverse in recurrent disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-driven angiogenesis sustains HNSCC: these tumors secrete VEGF to build new vessels, high levels predict worse outcomes, and anti-angiogenic approaches are studied alongside the radiation, chemotherapy and EGFR-targeted therapy that anchor treatment."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT promoter mutations help immortalize head and neck cancer: reactivating telomerase lets HPV-negative, smoking-related HNSCC cells bypass the telomere limit on division, complementing TP53 loss—one of the genetic steps from chronic carcinogen exposure to cancer."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Head and neck cancer spreads first to cervical lymph nodes: the rich lymphatic drainage of the upper aerodigestive tract carries tumor to neck nodes early, so nodal status dominates staging and dictates whether the neck is treated surgically or with radiation."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "HNSCC is a checkpoint-immunotherapy-responsive cancer: carcinogen- and HPV-driven tumors carry neoantigens and immune infiltrate, so anti-PD-1 therapy (pembrolizumab, nivolumab) now treats recurrent and metastatic disease, sometimes as first-line care."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy refines head and neck radiation: its sharp dose stop spares salivary glands, swallowing muscles, and the spinal cord beside the tumor, so protons can cut the dry mouth and swallowing damage of conventional photon treatment."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells now prevent many head and neck cancers: the HPV vaccine elicits antibodies that block the oral HPV infection driving rising oropharyngeal SCC, so a B-cell-based vaccine is set to lower this cancer's incidence."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Head and neck cancer shares field cancerization with the lung: the same tobacco and alcohol carcinogens that mutate the airway lining cause both, so HNSCC patients face high rates of second primary lung cancers, prompting chest surveillance."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "HPV-negative head and neck cancers amplify cyclin D1: gain of CCND1 at 11q13, paired with p16/CDKN2A loss, throws the cell cycle into overdrive—a hallmark of the tobacco-and-alcohol-driven tumors that behave worse than HPV-positive ones."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Cetuximab fights head and neck cancer through NK cells: the anti-EGFR antibody not only blocks growth signaling but flags tumor cells for natural killer cells to destroy by antibody-dependent killing, adding an immune mechanism to a targeted drug."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Head and neck tumors silence immunity with regulatory T cells: Tregs accumulate in the tumor and suppress the cytotoxic response, part of the immune evasion that PD-1 blockade (pembrolizumab, nivolumab) tries to reverse in this cancer."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Head and neck tumors resist radiation when starved of oxygen: hypoxic regions survive radiotherapy because oxygen is needed to fix radiation-induced DNA damage, so tumor hypoxia predicts worse control and drives research to overcome it."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-kB is constitutively switched on in head and neck cancer: tobacco, alcohol and HPV keep this inflammatory survival pathway active, driving proliferation and resistance to therapy and marking it as a target in the disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells shape the immune fight in head and neck cancer: as antigen-presenters they prime T cells against the tumor, and their dysfunction in the tumor helps explain immune escape that PD-1 blockade tries to reverse."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency feeds into head and neck cancer: Plummer-Vinson webs from chronic iron lack raise hypopharyngeal squamous cancer risk, and the tumor's own bleeding worsens anemia."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Curing head and neck cancer leaves fibrosis: the radiotherapy central to treatment scars neck tissues, causing lasting stiffness, trismus, and swallowing trouble that shape survivors' quality of life."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Head and neck cancer recruits endothelial cells: VEGF from the tumor drives these vessel-lining cells to build new blood supply, fueling growth and the hypoxia-driven resistance that complicates radiotherapy."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc touches both cause and toxicity in head and neck cancer: deficiency contributes to risk, and radiotherapy's loss of taste is a zinc-related effect, so the trace metal matters across the disease."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Head and neck cancer creeps along nerves: perineural invasion lets it spread beyond the visible tumor, a poor prognostic feature that widens the surgical margins and radiation fields needed."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Head and neck cancer spreads to distant organs late: beyond the lungs it can seed the liver and bone, marking the metastatic disease that shifts care toward systemic treatment."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy confirms head and neck cancer's squamous nature: the cells lock together with desmosomes, fill with keratin tonofilaments, and whorl into keratin pearls — the differentiation that grades the tumor."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Head and neck cancer eats into bone: oral and pharyngeal tumors invade the marrow-bearing mandible and maxilla, and advanced disease can seed distant skeletal metastases, the bony reach that complicates surgery."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sinonasal and nasopharyngeal head-and-neck cancers threaten the eye: spreading through the thin orbital walls they cause proptosis, double vision, and vision loss as they invade the orbit."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies attack head-and-neck cancer two ways: cetuximab blocks EGFR, and the checkpoint antibodies pembrolizumab and nivolumab release the immune brakes in recurrent or metastatic disease."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Its drugs strip magnesium twice over: cetuximab blocks the EGFR-dependent magnesium channel in the kidney, and the cisplatin given with radiation wastes it through tubular injury, so magnesium is closely monitored."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Treatment forces a feeding tube: tumor and the brutal mucositis of chemoradiation make swallowing impossible for a time, so a gastrostomy into the stomach is often placed to maintain nutrition through therapy."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "A rising share is sexually transmitted: HPV-driven oropharyngeal cancer of the tonsil and base of tongue is spreading the virus's reach from the genital tract to the throat, giving these tumors a younger, better-prognosis profile distinct from smoking-related disease."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The radiation field catches the thyroid: neck irradiation for head and neck cancer commonly damages the thyroid into hypothyroidism months to years later, and carries a small long-term risk of radiation-induced thyroid cancer."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "These tumors run a clotting risk: paraneoplastic thrombocytosis is common and marks worse prognosis, while the cisplatin chemoradiation that treats them can conversely drop platelet counts during therapy."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT is a central growth circuit: downstream of frequent PIK3CA and EGFR activation, AKT drives proliferation and survival in head and neck cancer, a much-pursued therapeutic target."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Tumor-promoting neutrophils crowd the blood: head and neck cancer recruits neutrophils that aid invasion, and a high neutrophil-to-lymphocyte ratio is a consistent marker of worse prognosis."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Smoking sows cancer across many linings: head-and-neck and bladder cancers share tobacco and carcinogen exposure, so field cancerization gives a patient with one a raised risk of the other."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 is a master driver of HNSCC: constitutively active STAT3, often downstream of EGFR, sustains proliferation and survival while reprogramming the microenvironment into an immunosuppressive state — a node tied to therapy resistance."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells stock the tumor stroma: they accumulate in head-and-neck cancers and release angiogenic and matrix-remodeling mediators, their density correlating with invasion and prognosis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The disease and its treatment invite sepsis: airway tumors cause aspiration pneumonia, and chemoradiation plus major surgery (with tracheostomy and feeding access) open routes to bloodstream infection and sepsis."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Radiation strips the mouth's defenses for a fungus: the mucositis and xerostomia of head-and-neck radiotherapy, on top of the tumor itself, let Candida overgrow into oral and esophageal candidiasis that hampers eating and treatment."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Neck irradiation scars the carotids: radiotherapy to head-and-neck cancer accelerates carotid atherosclerosis and stenosis, raising the risk of ischemic stroke years after treatment."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Cancer and long reconstructive surgery clot the veins: head-and-neck squamous cell carcinoma carries tumor-driven hypercoagulability, and its lengthy free-flap reconstructions add major perioperative venous thromboembolism risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Disfigurement and lost speech devastate: head-and-neck cancer disrupts the face, voice and swallowing, and carries among the highest rates of depression and suicide of any cancer."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Chronic disease and treatment lower the count: tumor bleeding, the inflammatory burden of HNSCC and the marrow effects of chemoradiation combine to produce an anemia that also blunts radiotherapy response."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Damaged sinonasal tissue and immunosuppression let mold in: radiation injury, mucosal breakdown and chemotherapy in head-and-neck cancer can permit invasive sinonasal or pulmonary aspergillosis."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Tumor, surgery and radiation savage the nerves: head-and-neck cancer invades cranial nerves, and its surgery, cisplatin and radiation produce severe, often refractory neuropathic pain."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Irradiated tissue heals badly: head-and-neck radiation causes osteoradionecrosis of the jaw, fistulas and flap failure, so wounds in the treated field heal slowly and break down."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Lost swallow sends food to the lungs: tumor, surgery and radiation impair swallowing and the airway in head-and-neck cancer, and the resulting aspiration pneumonia — often pneumococcal — is a common cause of death."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It wrecks the entrance to the gut: head-and-neck cancer and its radiation cause xerostomia, mucositis and dysphagia of the mouth and pharynx, often forcing gastrostomy feeding and altering taste and nutrition."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Neck radiation silences the thyroid: radiotherapy fields for head-and-neck cancer irradiate the thyroid gland, so hypothyroidism is a common late complication needing lifelong hormone replacement."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Disfigurement and lost voice breed worry: the impact on appearance, speech and swallowing, plus recurrence surveillance, in head-and-neck cancer foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It blocks and floods the airway: tumour and post-treatment dysphagia cause aspiration and airway obstruction often needing tracheostomy, and field cancerisation seeds lung second primaries."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It tracks along and damages the nerves: perineural invasion and skull-base extension cause cranial nerve palsies, and the cisplatin used to treat it causes ototoxicity and peripheral neuropathy."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Neck radiation endangers the carotid: it accelerates carotid atherosclerosis and can precipitate the catastrophic carotid blowout syndrome, a sudden rupture of the irradiated artery."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It invades and the radiation breaks bone: head and neck cancer erodes the mandible, and radiotherapy can cause osteoradionecrosis of the jaw, a painful, hard-to-heal complication."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Cisplatin threatens the kidney: the platinum chemoradiation central to head and neck cancer treatment is markedly nephrotoxic, requiring hydration and monitoring."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Treatment scars the skin: radiotherapy causes neck dermatitis and fibrosis, and the EGFR antibody cetuximab produces a characteristic acneiform rash."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy leads recurrent disease: pembrolizumab, alone or with chemotherapy, is first-line for recurrent or metastatic head-and-neck squamous cancer, which is often immunogenic."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cisplatin chemoradiation is the curative core: concurrent platinum chemotherapy with radiation, sometimes after induction chemotherapy, is the organ-preserving standard for locally advanced disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It invades and the radiation scars bone: head-and-neck cancer erodes the mandible, and the radiotherapy that treats it can cause osteoradionecrosis of the jaw."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "EGFR is its druggable handle: head-and-neck squamous cancers overexpress EGFR, and the anti-EGFR antibody cetuximab combined with radiotherapy or chemotherapy improves survival—the main targeted therapy in a cancer otherwise driven by loss of tumour suppressors."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Lymphoid islands predict response: HPV-positive head-and-neck cancers often contain tertiary lymphoid structures with germinal-center-like B-cell aggregates, and their presence forecasts better outcomes and response to checkpoint immunotherapy."
  - target: 03-medicine/03-food/curcumin
    relation: connects-to
    note: "A dietary chemoprevention candidate: curcumin is studied for reversing oral premalignant lesions such as leukoplakia that precede head-and-neck squamous carcinoma, targeting the NF-κB and STAT3 inflammation that fuels the tobacco-damaged mucosa."
---

# HNSCC

## Overview

**Head and neck squamous cell carcinoma (HNSCC)** refers to SCC arising in the oral cavity, oropharynx, hypopharynx, larynx, and nasopharynx — a heterogeneous group of mucosal cancers unified by squamous histology and key oncogenic pathways (EGFR, TP53, CDKN2A, PIK3CA). HNSCC is globally common (~900,000 cases/year worldwide) and is etiologically divided into two biologically distinct groups: **HPV-positive oropharyngeal HNSCC** (driven by HPV16/18 E6/E7 oncoproteins targeting p53 and RB; rising incidence due to sexual transmission; favorable prognosis) and **HPV-negative HNSCC** (driven by tobacco and alcohol; TP53 mutations ~80%; worse prognosis). The systemic therapy landscape has been transformed by the KEYNOTE-048 trial demonstrating pembrolizumab superiority over the EXTREME regimen (cetuximab + platinum + 5-FU) for PD-L1-expressing recurrent/metastatic disease [^burtness-2019-keynote048].

**Epidemiology:**
- ~65,000 new cases/year in the US; ~14,000 deaths/year; 6th most common cancer worldwide
- HPV+ oropharyngeal SCC: Rising incidence (~70-80% of oropharyngeal HNSCC in the US); younger patients (~55 years), non-smokers, better prognosis
- HPV- HNSCC: Tobacco + alcohol; oral cavity, hypopharynx, larynx; older patients; worse outcomes
- 5-year overall survival: ~50-60% for locally advanced; ~30% for recurrent/metastatic

**Risk factors:**
- HPV infection (HPV16 most common): Oropharynx (tonsil, base of tongue); sexual transmission; vaccination (Gardasil 9) reduces risk
- Tobacco (cigarettes, smokeless tobacco): Risk proportional to pack-years; 5-10× increased risk
- Alcohol: Synergistic with tobacco (~15× combined vs. either alone)
- Betel quid chewing: Major risk factor in South and Southeast Asia (buccal/oral cavity SCC)
- Prior radiation: Secondary malignancy

## Structure

### Molecular subtypes

**HPV-positive oropharyngeal HNSCC:**
- HPV16 E6 → targets p53 via E6AP ubiquitin ligase → p53 degradation; HPV16 E7 → binds RB → releases E2F → cell cycle entry
- Molecular: PIK3CA mutation/amplification (~20-30%); FGFR3 alterations; minimal TP53 mutation (wild-type p53 degraded post-translationally)
- Immunological: High TIL density; PD-L1 high; HPV peptide neoantigens → immunogenic; responds to de-escalated therapy
- Prognosis: 5-year OS ~80% for locally advanced vs. ~45-50% for HPV-negative; used in treatment de-escalation trials (PATHOS, QUARTERBACK, De-ESCALaTE)

**HPV-negative HNSCC (oral cavity, larynx, hypopharynx):**
- TP53 mutations ~80%; CDKN2A (p16) deletion ~40% (tobacco signature); CCND1 amplification (~30%); EGFR amplification (~30%); MYC amplification
- High TMB but lower neoantigen immunogenicity than HPV+ (due to fewer frameshift mutations, no viral peptides)
- Tobacco-driven mutational signature (C→A transversions); alcohol → acetaldehyde → DNA adducts

**Genomic landscape (TCGA 2015):**
HNSCC molecular subtypes (4 clusters):
1. **Atypical:** TP53 WT, PIK3CA/HRAS mutation, often HPV+
2. **Classical:** EGFR amplification, CDKN2A loss, smoker-associated
3. **Basal:** EGFR overexpression, YAP1 amplification
4. **Mesenchymal:** Immune-rich, EMT markers, MET/AXL high

### Site-specific features

**Oral cavity (lip, tongue, floor of mouth, hard palate, buccal mucosa):**
- High tobacco/alcohol/betel; TP53 ~85%; CCND1 amplification; worst nodal spread pattern
- Surgery preferred for resectable disease; adjuvant chemoradiation for high-risk pathology (positive margins, perineural invasion, lymphovascular invasion, ≥2 LN, extranodal extension)

**Oropharynx (tonsil, soft palate, base of tongue, pharyngeal walls):**
- HPV+ increasingly common; p16 IHC as surrogate for HPV testing; p16+ = HPV+ in oropharynx (high sensitivity/specificity)
- Favorable prognosis → de-escalation trials testing reduced chemoradiation doses or radiation alone for early-stage HPV+ disease

**Larynx (supraglottic, glottic, subglottic):**
- Glottic SCC: Often early hoarseness → early diagnosis; favorable prognosis; voice preservation with radiotherapy
- Supraglottic SCC: Late presentation; poor prognosis; tobacco-driven
- Larynx preservation: Concurrent cisplatin + radiotherapy (VA Cooperative Study and RTOG 91-11) established as alternative to laryngectomy for organ preservation

**Hypopharynx:**
- Poorest prognosis of all HNSCC (late presentation, high nodal involvement); pyriform sinus most common

## Function

### HPV oncogenesis vs. tobacco/alcohol carcinogenesis

**HPV oncogenesis (HPV+ HNSCC):**
HPV16/18 infects basal cells of the oropharyngeal mucosa → viral episome (circular dsDNA) integrates into host genome → E6/E7 oncoproteins expressed:
- E6 + E6AP → p53 ubiquitination/degradation → impaired apoptosis and G1 checkpoint
- E7 → binds pRB LXCXE motif → RB inactivation → E2F release → S-phase entry even without mitogens
- E5: Promotes EGFR recycling → enhanced EGF signaling
Result: Immortalized basal cells with active PI3K/CDK4 and impaired DNA damage response → HNSCC initiation.

**Tobacco/alcohol carcinogenesis (HPV- HNSCC):**
Polycyclic aromatic hydrocarbons (PAH) in tobacco → carcinogen-DNA adducts → C→A transversions at TP53/CDKN2A; acetaldehyde (from alcohol) → N2-ethylidene-dG adducts → TP53 mutations; combined → 15× elevated HNSCC risk; accumulating TP53 mutations in field cancerization → synchronous/metachronous multiple primary tumors (field effect throughout entire aerodigestive tract).

## Pathology

### Staging and workup

**AJCC 8th edition (HPV+ and HPV- staged separately):**
HPV+ oropharyngeal: Node staging based on number (not laterality); HPV-negative staging follows standard pT/pN/pM.
- Most patients present with locally advanced stage III-IV (~60%)

**Staging workup:**
- CT with contrast (neck/chest/abdomen): Primary tumor and nodal assessment; distant staging
- FDG-PET/CT: Standard for N0 clinical staging (detect occult N+ disease); post-treatment assessment (12-16 weeks post-CRT) to determine need for planned neck dissection
- MRI: Preferred for soft tissue involvement (tongue base, skull base)
- HPV testing: p16 IHC in oropharynx (positive = CPS >70%, practically all oropharyngeal SCC p16+ are HPV+); HPV ISH or PCR for equivocal cases

### Treatment

**Locally advanced HNSCC (Stage III-IVB):**
- **Concurrent cisplatin (100 mg/m² q3w) + IMRT:** Standard of care for resectable/unresectable disease; cisplatin superior to carboplatin or cetuximab with radiation (TROG 02.02); 3-year locoregional control ~75%
- **Cetuximab + radiation (Bonner trial):** Inferior to cisplatin+RT in fit patients (RTOG 1016, De-ESCALaTE trials); reserved for cisplatin-ineligible patients; cisplatin+RT now preferred when feasible
- **Surgery ± adjuvant chemoradiation:** Resectable oral cavity and selected oropharynx tumors; adjuvant CRT for positive margins or extranodal extension (EORTC 22931/RTOG 9501 trials)
- **De-escalation (HPV+):** PATHOS, QUARTERBACK, NRG-HN002 trials studying reduced dose radiation (50-60 Gy vs. 70 Gy) in p16+/HPV+ oropharynx; not yet standard

**Recurrent/metastatic HNSCC (R/M HNSCC):**

**First-line:**
- **Pembrolizumab monotherapy (CPS≥1):** FDA approved for R/M HNSCC; OS 14.9 months (CPS≥20), 13.6 months (CPS≥1) — first-line standard for PD-L1+ disease [^burtness-2019-keynote048]
- **Pembrolizumab + platinum + 5-FU (CPS≥1):** OS benefit; preferred over EXTREME for PD-L1+ patients; ORR ~36%
- **EXTREME (cetuximab + cisplatin/carboplatin + 5-FU):** [^vermorken-2008-extreme] OS 10.1 vs. 7.4 months vs. chemo alone; FDA approved 2011; still used for CPS<1 patients where pembrolizumab alone is not recommended; 6 cycles then maintenance cetuximab

**Second-line and beyond:**
- **Nivolumab (CheckMate 141):** OS 7.5 vs. 5.1 months vs. chemotherapy in platinum-refractory R/M HNSCC; ORR 13%; FDA approved 2016; now largely used after pembrolizumab failure
- **Cetuximab monotherapy:** ORR ~13% in platinum-refractory disease; option for cetuximab-naive patients
- **Docetaxel, paclitaxel, methotrexate:** Palliative options in later lines

**Nasopharyngeal carcinoma (NPC — distinct from HNSCC):**
- EBV-associated (>95% of undifferentiated/non-keratinizing NPC in endemic regions)
- Cisplatin + radiation (NPC-specific protocols); induction chemotherapy with cisplatin+gemcitabine → CRT for locally advanced
- Pembrolizumab and nivolumab active in recurrent/metastatic EBV+ NPC

## Connections

- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR overexpression in ~90% of HNSCC (mainly copy number gain, not mutation); cetuximab (anti-EGFR mAb) + cisplatin/5-FU (EXTREME regimen) improved OS vs. chemo alone (10.1 vs. 7.4 months); cetuximab + radiation is definitive for locally advanced HNSCC in platinum-ineligible patients.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Pembrolizumab (KEYNOTE-048) improved OS vs. EXTREME in PD-L1 CPS≥20 (14.9 vs. 10.7 months) and CPS≥1 (13.6 vs. 10.4 months); pembrolizumab+chemotherapy improved OS for CPS≥1; nivolumab (CheckMate 141) improved OS vs. chemotherapy in platinum-refractory R/M HNSCC.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations in ~80% of HPV-negative HNSCC (UV and tobacco mutational signatures; R175H, R248W hotspots); HPV-positive HNSCC has WT TP53 (HPV E6 degrades p53 via E6AP ubiquitin ligase); TP53 mutation correlates with poor prognosis and cisplatin resistance in HNSCC.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA mutation/amplification in ~20-30% of HNSCC; especially HPV-positive oropharyngeal HNSCC (HPV E7 → retinoblastoma pathway disruption → CDK activation; HPV-positive HNSCC has higher PI3K pathway activation); PI3K inhibitors (copanlisib, alpelisib) studied in HNSCC; AKT inhibitors in clinical trials.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Epstein-Barr virus — not HPV — drives nasopharyngeal carcinoma, a distinct head-and-neck SCC: >95% of endemic undifferentiated NPC is EBV+; EBER in-situ hybridization confirms it and plasma EBV DNA tracks tumor burden; pembrolizumab and nivolumab are active in recurrent EBV+ NPC.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — HPV16 E7 binds and inactivates RB1, releasing E2F to drive S-phase entry without mitogens — the RB arm of HPV oncogenesis that pairs with E6-mediated p53 degradation; because RB is disabled by protein, HPV+ HNSCC rarely carries RB1 or CDKN2A mutations.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/p16 behaves oppositely by HPV status: deleted in ~40% of tobacco-driven HPV-negative HNSCC, but strongly overexpressed in HPV+ tumors (RB loss removes feedback), making p16 immunostaining the practical surrogate marker for HPV-positive oropharyngeal cancer.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Head and neck and esophageal squamous cell carcinomas are linked by field cancerization: chronic alcohol and tobacco mutagenizes the whole aerodigestive squamous mucosa, so HNSCC patients carry elevated risk of esophageal SCC — both TP53-driven, immunotherapy-responsive tumors.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — HNSCC and cervical cancer are united by HPV: high-risk HPV16 drives oropharyngeal HNSCC as it drives cervical cancer, E6 degrading p53 and E7 inactivating RB; HPV-positive oropharyngeal cancer has a better prognosis than tobacco-driven HNSCC, and the same vaccine prevents both.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — HNSCC is one of the more immunogenic solid tumors — heavy tobacco or viral mutational load generates neoantigens — so anti-PD-1 (pembrolizumab, nivolumab) reactivating cytotoxic CD8+ T cells extended survival in recurrent/metastatic disease (KEYNOTE-048, CheckMate 141).
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Alcohol is a primary cause of head and neck squamous cell carcinoma: acetaldehyde is a direct mucosal carcinogen that synergizes strongly with tobacco to multiply oral, pharyngeal and laryngeal cancer risk—an etiology distinct from the HPV-driven oropharyngeal subset.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Tobacco smoke is the dominant cause of head and neck squamous cell carcinoma: its carbon-based polycyclic aromatic hydrocarbons and nitrosamines damage upper-aerodigestive mucosal DNA, producing field cancerization with multiple primaries, especially when combined with alcohol.
- `connects-to` → **[HPV-16](../../../02-pathogen/01-viruses/hpv-16/README.md)** — HPV-16 drives a distinct, rising subset of head and neck squamous cell carcinoma: the virus infects oropharyngeal (tonsil, base of tongue) crypt epithelium, its E6/E7 oncoproteins inactivating p53 and Rb; HPV-positive HNSCC affects younger non-smokers and has a better prognosis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is central to head and neck cancer: definitive chemoradiation can cure many HNSCCs (especially HPV-positive oropharyngeal tumors) and organ-preserve the larynx, while IMRT spares salivary glands—radiation is as pivotal here as surgery.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Cancer-associated fibroblasts shape head and neck cancer: HNSCC recruits and reprograms fibroblasts that secrete growth factors, remodel matrix and blunt immunity, promoting invasion and resistance—making the fibroblast-rich microenvironment a therapeutic target.
- `connects-to` → **[Thyroid Cancer](../thyroid-cancer/README.md)** — Head and neck cancer and thyroid cancer both arise in the neck but differ: HNSCC is a smoking/HPV-driven squamous carcinoma of the aerodigestive mucosa, while thyroid cancer is a usually indolent endocrine tumor—neck radiation, a thyroid-cancer risk factor, links them.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — HNSCC and lung cancer share tobacco field cancerization: the same carcinogen exposure mutates the entire aerodigestive lining, so head-and-neck cancer patients carry a high risk of synchronous or later lung cancer—warranting chest screening and smoking cessation.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Tumor-associated macrophages shape HNSCC: they infiltrate the tumor, suppress T-cell responses and promote invasion and angiogenesis, contributing to the immunosuppressive microenvironment that immune checkpoint inhibitors aim to reverse in recurrent disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-driven angiogenesis sustains HNSCC: these tumors secrete VEGF to build new vessels, high levels predict worse outcomes, and anti-angiogenic approaches are studied alongside the radiation, chemotherapy and EGFR-targeted therapy that anchor treatment.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT promoter mutations help immortalize head and neck cancer: reactivating telomerase lets HPV-negative, smoking-related HNSCC cells bypass the telomere limit on division, complementing TP53 loss—one of the genetic steps from chronic carcinogen exposure to cancer.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Head and neck cancer spreads first to cervical lymph nodes: the rich lymphatic drainage of the upper aerodigestive tract carries tumor to neck nodes early, so nodal status dominates staging and dictates whether the neck is treated surgically or with radiation.
- `connects-to` → **[Immune System](../immune-system/README.md)** — HNSCC is a checkpoint-immunotherapy-responsive cancer: carcinogen- and HPV-driven tumors carry neoantigens and immune infiltrate, so anti-PD-1 therapy (pembrolizumab, nivolumab) now treats recurrent and metastatic disease, sometimes as first-line care.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy refines head and neck radiation: its sharp dose stop spares salivary glands, swallowing muscles, and the spinal cord beside the tumor, so protons can cut the dry mouth and swallowing damage of conventional photon treatment.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells now prevent many head and neck cancers: the HPV vaccine elicits antibodies that block the oral HPV infection driving rising oropharyngeal SCC, so a B-cell-based vaccine is set to lower this cancer's incidence.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Head and neck cancer shares field cancerization with the lung: the same tobacco and alcohol carcinogens that mutate the airway lining cause both, so HNSCC patients face high rates of second primary lung cancers, prompting chest surveillance.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — HPV-negative head and neck cancers amplify cyclin D1: gain of CCND1 at 11q13, paired with p16/CDKN2A loss, throws the cell cycle into overdrive—a hallmark of the tobacco-and-alcohol-driven tumors that behave worse than HPV-positive ones.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Cetuximab fights head and neck cancer through NK cells: the anti-EGFR antibody not only blocks growth signaling but flags tumor cells for natural killer cells to destroy by antibody-dependent killing, adding an immune mechanism to a targeted drug.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Head and neck tumors silence immunity with regulatory T cells: Tregs accumulate in the tumor and suppress the cytotoxic response, part of the immune evasion that PD-1 blockade (pembrolizumab, nivolumab) tries to reverse in this cancer.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Head and neck tumors resist radiation when starved of oxygen: hypoxic regions survive radiotherapy because oxygen is needed to fix radiation-induced DNA damage, so tumor hypoxia predicts worse control and drives research to overcome it.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-kB is constitutively switched on in head and neck cancer: tobacco, alcohol and HPV keep this inflammatory survival pathway active, driving proliferation and resistance to therapy and marking it as a target in the disease.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells shape the immune fight in head and neck cancer: as antigen-presenters they prime T cells against the tumor, and their dysfunction in the tumor helps explain immune escape that PD-1 blockade tries to reverse.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency feeds into head and neck cancer: Plummer-Vinson webs from chronic iron lack raise hypopharyngeal squamous cancer risk, and the tumor's own bleeding worsens anemia.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Curing head and neck cancer leaves fibrosis: the radiotherapy central to treatment scars neck tissues, causing lasting stiffness, trismus, and swallowing trouble that shape survivors' quality of life.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Head and neck cancer recruits endothelial cells: VEGF from the tumor drives these vessel-lining cells to build new blood supply, fueling growth and the hypoxia-driven resistance that complicates radiotherapy.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc touches both cause and toxicity in head and neck cancer: deficiency contributes to risk, and radiotherapy's loss of taste is a zinc-related effect, so the trace metal matters across the disease.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Head and neck cancer creeps along nerves: perineural invasion lets it spread beyond the visible tumor, a poor prognostic feature that widens the surgical margins and radiation fields needed.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Head and neck cancer spreads to distant organs late: beyond the lungs it can seed the liver and bone, marking the metastatic disease that shifts care toward systemic treatment.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy confirms head and neck cancer's squamous nature: the cells lock together with desmosomes, fill with keratin tonofilaments, and whorl into keratin pearls — the differentiation that grades the tumor.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Head and neck cancer eats into bone: oral and pharyngeal tumors invade the marrow-bearing mandible and maxilla, and advanced disease can seed distant skeletal metastases, the bony reach that complicates surgery.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sinonasal and nasopharyngeal head-and-neck cancers threaten the eye: spreading through the thin orbital walls they cause proptosis, double vision, and vision loss as they invade the orbit.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies attack head-and-neck cancer two ways: cetuximab blocks EGFR, and the checkpoint antibodies pembrolizumab and nivolumab release the immune brakes in recurrent or metastatic disease.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Its drugs strip magnesium twice over: cetuximab blocks the EGFR-dependent magnesium channel in the kidney, and the cisplatin given with radiation wastes it through tubular injury, so magnesium is closely monitored.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Treatment forces a feeding tube: tumor and the brutal mucositis of chemoradiation make swallowing impossible for a time, so a gastrostomy into the stomach is often placed to maintain nutrition through therapy.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — A rising share is sexually transmitted: HPV-driven oropharyngeal cancer of the tonsil and base of tongue is spreading the virus's reach from the genital tract to the throat, giving these tumors a younger, better-prognosis profile distinct from smoking-related disease.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The radiation field catches the thyroid: neck irradiation for head and neck cancer commonly damages the thyroid into hypothyroidism months to years later, and carries a small long-term risk of radiation-induced thyroid cancer.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — These tumors run a clotting risk: paraneoplastic thrombocytosis is common and marks worse prognosis, while the cisplatin chemoradiation that treats them can conversely drop platelet counts during therapy.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT is a central growth circuit: downstream of frequent PIK3CA and EGFR activation, AKT drives proliferation and survival in head and neck cancer, a much-pursued therapeutic target.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Tumor-promoting neutrophils crowd the blood: head and neck cancer recruits neutrophils that aid invasion, and a high neutrophil-to-lymphocyte ratio is a consistent marker of worse prognosis.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Smoking sows cancer across many linings: head-and-neck and bladder cancers share tobacco and carcinogen exposure, so field cancerization gives a patient with one a raised risk of the other.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 is a master driver of HNSCC: constitutively active STAT3, often downstream of EGFR, sustains proliferation and survival while reprogramming the microenvironment into an immunosuppressive state — a node tied to therapy resistance.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells stock the tumor stroma: they accumulate in head-and-neck cancers and release angiogenic and matrix-remodeling mediators, their density correlating with invasion and prognosis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The disease and its treatment invite sepsis: airway tumors cause aspiration pneumonia, and chemoradiation plus major surgery (with tracheostomy and feeding access) open routes to bloodstream infection and sepsis.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Radiation strips the mouth's defenses for a fungus: the mucositis and xerostomia of head-and-neck radiotherapy, on top of the tumor itself, let Candida overgrow into oral and esophageal candidiasis that hampers eating and treatment.
- `connects-to` → **[Stroke](../stroke/README.md)** — Neck irradiation scars the carotids: radiotherapy to head-and-neck cancer accelerates carotid atherosclerosis and stenosis, raising the risk of ischemic stroke years after treatment.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Cancer and long reconstructive surgery clot the veins: head-and-neck squamous cell carcinoma carries tumor-driven hypercoagulability, and its lengthy free-flap reconstructions add major perioperative venous thromboembolism risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Disfigurement and lost speech devastate: head-and-neck cancer disrupts the face, voice and swallowing, and carries among the highest rates of depression and suicide of any cancer.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Chronic disease and treatment lower the count: tumor bleeding, the inflammatory burden of HNSCC and the marrow effects of chemoradiation combine to produce an anemia that also blunts radiotherapy response.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Damaged sinonasal tissue and immunosuppression let mold in: radiation injury, mucosal breakdown and chemotherapy in head-and-neck cancer can permit invasive sinonasal or pulmonary aspergillosis.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Tumor, surgery and radiation savage the nerves: head-and-neck cancer invades cranial nerves, and its surgery, cisplatin and radiation produce severe, often refractory neuropathic pain.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Irradiated tissue heals badly: head-and-neck radiation causes osteoradionecrosis of the jaw, fistulas and flap failure, so wounds in the treated field heal slowly and break down.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Lost swallow sends food to the lungs: tumor, surgery and radiation impair swallowing and the airway in head-and-neck cancer, and the resulting aspiration pneumonia — often pneumococcal — is a common cause of death.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It wrecks the entrance to the gut: head-and-neck cancer and its radiation cause xerostomia, mucositis and dysphagia of the mouth and pharynx, often forcing gastrostomy feeding and altering taste and nutrition.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Neck radiation silences the thyroid: radiotherapy fields for head-and-neck cancer irradiate the thyroid gland, so hypothyroidism is a common late complication needing lifelong hormone replacement.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Disfigurement and lost voice breed worry: the impact on appearance, speech and swallowing, plus recurrence surveillance, in head-and-neck cancer foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It blocks and floods the airway: tumour and post-treatment dysphagia cause aspiration and airway obstruction often needing tracheostomy, and field cancerisation seeds lung second primaries.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It tracks along and damages the nerves: perineural invasion and skull-base extension cause cranial nerve palsies, and the cisplatin used to treat it causes ototoxicity and peripheral neuropathy.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Neck radiation endangers the carotid: it accelerates carotid atherosclerosis and can precipitate the catastrophic carotid blowout syndrome, a sudden rupture of the irradiated artery.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It invades and the radiation breaks bone: head and neck cancer erodes the mandible, and radiotherapy can cause osteoradionecrosis of the jaw, a painful, hard-to-heal complication.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Cisplatin threatens the kidney: the platinum chemoradiation central to head and neck cancer treatment is markedly nephrotoxic, requiring hydration and monitoring.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Treatment scars the skin: radiotherapy causes neck dermatitis and fibrosis, and the EGFR antibody cetuximab produces a characteristic acneiform rash.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy leads recurrent disease: pembrolizumab, alone or with chemotherapy, is first-line for recurrent or metastatic head-and-neck squamous cancer, which is often immunogenic.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cisplatin chemoradiation is the curative core: concurrent platinum chemotherapy with radiation, sometimes after induction chemotherapy, is the organ-preserving standard for locally advanced disease.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It invades and the radiation scars bone: head-and-neck cancer erodes the mandible, and the radiotherapy that treats it can cause osteoradionecrosis of the jaw.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — EGFR is its druggable handle: head-and-neck squamous cancers overexpress EGFR, and the anti-EGFR antibody cetuximab combined with radiotherapy or chemotherapy improves survival—the main targeted therapy in a cancer otherwise driven by loss of tumour suppressors.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Lymphoid islands predict response: HPV-positive head-and-neck cancers often contain tertiary lymphoid structures with germinal-center-like B-cell aggregates, and their presence forecasts better outcomes and response to checkpoint immunotherapy.
- `connects-to` → **[Curcumin](../../../03-medicine/03-food/curcumin/README.md)** — A dietary chemoprevention candidate: curcumin is studied for reversing oral premalignant lesions such as leukoplakia that precede head-and-neck squamous carcinoma, targeting the NF-κB and STAT3 inflammation that fuels the tobacco-damaged mucosa.

[^burtness-2019-keynote048]: Burtness B, Harrington KJ, Greil R, et al. Pembrolizumab alone or with chemotherapy versus cetuximab with chemotherapy for recurrent or metastatic squamous cell carcinoma of the head and neck (KEYNOTE-048). *Lancet.* 2019;394(10212):1915-1928. [doi:10.1016/S0140-6736(19)32591-7](https://doi.org/10.1016/S0140-6736(19)32591-7) · [PubMed 31679945](https://pubmed.ncbi.nlm.nih.gov/31679945/)
[^vermorken-2008-extreme]: Vermorken JB, Mesia R, Rivera F, et al. Platinum-based chemotherapy plus cetuximab in head and neck cancer. *N Engl J Med.* 2008;359(11):1116-1127. [doi:10.1056/NEJMoa0802656](https://doi.org/10.1056/NEJMoa0802656) · [PubMed 18784101](https://pubmed.ncbi.nlm.nih.gov/18784101/)
