---
schema: human-scale-entry/v1
id: pcnsl
name: Primary CNS Lymphoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "PCNSL is ABC-DLBCL confined to CNS; MYD88 L265P ~90%, CD79B ~70%; high-dose methotrexate is the treatment backbone; ibrutinib shows ~50-60% ORR in R/R disease; 5-year OS ~30-40% with HDMTX-based therapy; vitreous IL-10 >10 pg/mL is pathognomonic."
aliases: ["PCNSL", "primary CNS lymphoma", "primary central nervous system lymphoma", "CNS lymphoma", "cerebral lymphoma", "vitreoretinal lymphoma", "primary intraocular lymphoma"]
sources:
  - id: bromberg-2019-hovon105
    type: peer-reviewed
    cite: "Bromberg JE, Issa S, Bakunina K, et al. Rituximab in patients with primary CNS lymphoma (HOVON 105/ALLG NHL 24): a randomised, open-label, phase 3 intergroup study. Lancet Oncol. 2019;20(2):216-228."
    doi: "10.1016/S1470-2045(18)30747-2"
    pmid: "30528440"
    url: "https://doi.org/10.1016/S1470-2045(18)30747-2"
  - id: grommes-2017-ibrutinib-pcnsl
    type: peer-reviewed
    cite: "Grommes C, Pastore A, Palaskas N, et al. Ibrutinib unmasks critical role of Bruton tyrosine kinase in primary CNS lymphoma. Cancer Cell. 2017;31(6):833-843."
    doi: "10.1016/j.ccell.2017.04.012"
    pmid: "28552327"
    url: "https://doi.org/10.1016/j.ccell.2017.04.012"
cross_links:
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "MYD88 L265P is present in ~90% of PCNSL — the highest prevalence in any cancer outside WM; constitutive IRAK4-NF-κB signaling drives RS cell survival; ibrutinib (BTK inhibitor) crosses the blood-brain barrier and shows ORR ~50-60% in R/R PCNSL via MYD88-BTK pathway suppression."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PCNSL tumor cells express PD-L1 driven by MYD88-NF-κB and JAK-STAT3 signaling; CNS immune privilege maintains low T-cell surveillance; nivolumab and pembrolizumab show modest activity in R/R PCNSL (ORR ~35%); PD-L1 blockade combined with HDMTX is under investigation."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "BTK is the downstream effector of BCR and MYD88 signaling in PCNSL; ibrutinib (BTK covalent inhibitor) achieves ~50-75% of plasma levels in CSF and shows ORR ~50-60% in R/R PCNSL; ibrutinib+MTX+rituximab (TEDDi-R) studied as frontline; zanubrutinib also CNS-penetrant."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "MYD88 L265P drives IL-6 and IL-10 autocrine in PCNSL; vitreous IL-10 >10 pg/mL and IL-10:IL-6 ratio >1 are pathognomonic for PCNSL/vitreoretinal lymphoma; IL-10 drives JAK1-STAT3 survival in tumor cells; CSF IL-10 elevation correlates with PCNSL disease burden and response."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "PCNSL is non-Hodgkin lymphoma confined to the CNS (periventricular, basal ganglia, corpus callosum) as homogeneously enhancing masses with restricted diffusion; the blood-brain barrier blocks most lymphoma drugs, making BBB-penetrant high-dose methotrexate the backbone."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "PCNSL is an aggressive B-cell lymphoma (ABC-DLBCL): CD20+ neoplastic B cells with MYD88 L265P and CD79B mutations driving NF-κB; they home to the CNS via CXCR4/CXCR5 and evade immunity by downregulating MHC — rituximab penetrates the BBB poorly, limiting anti-CD20 benefit."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "In immunosuppressed patients (HIV with CD4 <50, transplant), PCNSL is typically EBV-driven and EBER-positive — a distinct entity from the EBV-negative, MYD88-mutant immunocompetent form; restoring immunity with HAART can induce regression of EBV-associated CNS lymphoma."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "Primary CNS lymphoma and peripheral T-cell lymphoma are aggressive non-Hodgkin lymphomas of opposite lineage: PCNSL is a B-cell (ABC-DLBCL) tumor driven by MYD88/CD79B-NF-κB, PTCL a heterogeneous T-cell group driven by TET2/RHOA/STAT3 — different cells, different therapies."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Primary CNS lymphoma is essentially a diffuse large B-cell lymphoma (ABC type) trapped in the CNS: it shares DLBCL's CD20+ biology and MYD88/CD79B-NF-κB drivers, but immune privilege and the blood-brain barrier make it behave differently — high-dose methotrexate, not R-CHOP."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Primary CNS lymphoma has an ocular form — vitreoretinal lymphoma — that seeds the eye as painless floaters or steroid-refractory uveitis; a vitreous IL-10:IL-6 ratio >1 and MYD88 L265P clinch the diagnosis, and ~15-25% of PCNSL involves the eye, often bilaterally."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Primary CNS lymphoma is an AIDS-defining cancer: in advanced HIV with low CD4 counts, EBV-driven B-cell lymphoma arises in the brain, so a periventricular mass in AIDS raises PCNSL versus toxoplasmosis—distinguished by EBV PCR of CSF and thallium imaging."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Whole-brain photon radiotherapy once anchored PCNSL treatment but is now used cautiously: the tumor is exquisitely radiosensitive, yet WBRT causes severe delayed neurocognitive decline, so high-dose methotrexate is preferred and radiation reserved or dose-reduced."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "PCNSL grows in the unique immune environment policed by microglia: this EBV-driven B-cell lymphoma proliferates around vessels in brain parenchyma, and reactive microglia form the perivascular cuffs and inflammatory backdrop characteristic of its histology."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "PCNSL and glioblastoma are the two great intra-axial brain masses that imaging can confuse: both enhance and infiltrate, but PCNSL is a B-cell lymphoma exquisitely steroid- and methotrexate-sensitive, while GBM needs surgery and chemoradiation—biopsy is decisive."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "PCNSL and meningioma are both intracranial tumors but opposite: PCNSL is an intra-axial B-cell lymphoma treated with methotrexate, while meningioma is an extra-axial dural tumor cured by resection—MRI location usually separates the medical from the surgical disease."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "PCNSL and mantle cell lymphoma can both involve the CNS: primary CNS lymphoma is a brain-confined DLBCL, while aggressive systemic lymphomas like MCL can spread secondarily to the leptomeninges—so CNS lymphoma may be primary or secondary."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "PCNSL is largely a disease of immune failure: it is far commoner in HIV/AIDS and transplant immunosuppression, where unchecked EBV transforms B cells in the brain—so immune status drives both its incidence and (with immune restoration) sometimes its regression."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "PCNSL arises from a late germinal-center B cell trapped in the CNS: it is a post-germinal-center DLBCL expressing BCL6/IRF4 that, oddly, homes to and grows within the immune-privileged brain—so it shares lymphoma-node biology yet behaves as a CNS tumor."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC and BCL2 co-expression marks aggressive PCNSL: like systemic DLBCL, double-expressor PCNSL carries a worse prognosis, but the blood-brain barrier limits which drugs reach it—so high-dose methotrexate, not standard R-CHOP, anchors treatment."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "PCNSL is a CD20-positive B-cell lymphoma treated through that target: high-dose methotrexate crosses the blood-brain barrier and is combined with the anti-CD20 antibody rituximab, exploiting the same B-cell marker used against systemic lymphomas."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Primary CNS lymphoma is a lymphoma confined to the nervous system: it grows in the brain, spinal cord, eyes and meninges without nodal disease, so it presents with focal deficits and cognitive change—and its CNS sanctuary demands brain-penetrant therapy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "PCNSL is a striking exception within the lymphatic system: though a B-cell lymphoma, it arises and stays in the immune-privileged CNS rather than lymph nodes, so staging is typically negative outside the brain and eye—unlike systemic DLBCL."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "PCNSL survives on chronic NF-kB signaling: MYD88 and CD79B mutations lock this pathway on, driving the lymphoma's growth—the rationale for BTK inhibitors like ibrutinib that choke off the B-cell-receptor input to NF-kB."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CAR-T cells are reaching into the brain for PCNSL: CD19-directed cytotoxic T cells engineered to kill B-cell lymphoma are being trialed in relapsed central-nervous-system lymphoma, with responses showing the cells can work inside the CNS."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "PCNSL and Waldenstrom share the MYD88 L265P mutation: both are MYD88-driven B-cell malignancies that respond to BTK inhibition, so a brain lymphoma's mutation links it mechanistically to this marrow-based lymphoplasmacytic cancer."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "PCNSL stays trapped in the brain by CXCL12: the CNS pours out this chemokine, and the lymphoma cells' CXCR4 receptor locks onto it, explaining why this aggressive B-cell lymphoma homes to and stays confined within the brain and eye."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "PCNSL is laced with reactive macrophages and microglia: a perivascular cuff of these innate immune cells surrounds the tumor, a histologic hallmark that both shapes the immune-privileged niche and can confound the biopsy diagnosis."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "PCNSL exploits the brain's immune privilege with regulatory T cells: behind the blood-brain barrier and amid Treg-rich infiltrates, the tumor evades attack, part of why systemic immunotherapy struggles to reach and clear CNS lymphoma."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "PCNSL survives on B-cell-receptor calcium signaling: with MYD88 and BTK-driven activation, a calcium flux keeps the malignant B cells alive in the brain, which is why BTK inhibitors that interrupt this pathway can penetrate the CNS and work."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are scarce in the brain that PCNSL exploits: the CNS has few professional antigen-presenters, so the lymphoma faces weak priming of an immune response—part of the immune privilege that lets it grow behind the blood-brain barrier."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PCNSL leans on the PI3K-AKT-mTOR axis downstream of BTK: chronic B-cell-receptor and MYD88 signaling feed AKT to drive survival, so AKT-mTOR inhibitors are studied alongside BTK inhibitors for this aggressive brain lymphoma."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "PCNSL's cure depends on the kidneys: its mainstay treatment, high-dose methotrexate, is cleared by the kidneys and is toxic to them, so renal function must be protected to deliver the drug safely."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "PCNSL grows hugging the blood vessels: the malignant B cells cuff around cerebral vessels in an angiocentric pattern, leaning on the endothelial-lined vasculature behind the blood-brain barrier."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "PCNSL can spill potassium when it melts: this aggressive lymphoma responds fast to steroids and chemo, and the rapid cell death can trigger tumor lysis that floods the blood with potassium."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "The bone marrow defines what PCNSL is not: by definition the lymphoma stays in the brain, eye, and CSF, so a marrow biopsy is part of staging to rule out a systemic lymphoma that has merely spread to the nervous system."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "PCNSL is confirmed by an absent spleen lesion: full-body staging checks the spleen and other nodal sites because finding systemic disease would reclassify it as ordinary lymphoma, while late relapses can occasionally break out to these organs."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "PCNSL leans toward the plasma cell end of the B-lineage: its hallmark MYD88 mutation is shared with plasmacytic lymphomas, and the tumor cells often show plasmablastic features driving the same NF-κB survival signaling."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "PCNSL menaces the neuron from two sides: the infiltrating lymphoma crowds and destroys brain tissue to cause focal deficits, and the curative high-dose methotrexate with whole-brain radiation can later leave a disabling cognitive decline."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Treating PCNSL can strip the brain's myelin: high-dose methotrexate and whole-brain radiation injure oligodendrocytes, producing the delayed white-matter leukoencephalopathy that dims memory and slows thinking in survivors."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "PCNSL is defined by what it spares: by definition the lymphoma is confined to the CNS, so staging scans the liver and marrow precisely to exclude systemic DLBCL, whose visceral spread would change the disease and its treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both name and treat PCNSL: CD20 and MUM1 stains confirm its diffuse large B-cell nature on a stereotactic biopsy, and the anti-CD20 antibody rituximab is added to high-dose methotrexate to attack those same B cells."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Steroids make PCNSL a 'ghost tumor': corticosteroids are so lymphotoxic that the mass can melt away within days, erasing the target before biopsy — so steroids are held until tissue is obtained, even when the swelling tempts early use."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The methotrexate cure batters the marrow: the high-dose methotrexate regimens central to PCNSL are myelosuppressive, dropping neutrophil counts so that leucovorin rescue and infection vigilance run through every cycle."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "PCNSL survives on chronic signaling: alongside MYD88 and NF-kB activation, JAK-STAT3 signaling drives the lymphoma's growth and helps it evade immunity within the brain's sheltered environment, a pathway probed for targeted therapy."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The testis is a sanctuary that talks to the brain: testicular lymphoma notoriously relapses in the CNS, both being immune-privileged sites, so testicular DLBCL gets CNS prophylaxis — and PCNSL's intensive chemo threatens fertility in younger patients."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "The treatment also drops the platelets: high-dose methotrexate and the cytarabine often added suppress platelet production into thrombocytopenia, raising bleeding risk and limiting dose intensity through the months of therapy."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "It often carries a survival overdrive: many CNS lymphomas co-express BCL-2 with MYC as 'double-expressors', the anti-apoptotic signal keeping malignant B cells alive and a rationale for testing the BCL-2 inhibitor venetoclax against the disease."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "The tumor grows in glial turf: PCNSL infiltrates the brain parenchyma in angiocentric cuffs, surrounded by reactive astrocytes whose microenvironment and the blood-brain barrier shape both its growth and the difficulty of getting drugs to it."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Both lymphomas court the nervous system: like PCNSL, Burkitt lymphoma has a strong tropism for the central nervous system, which is why aggressive B-cell lymphomas demand CNS-penetrating therapy and prophylaxis to reach sanctuary sites."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "CAR-T against PCNSL can storm the brain: CD19 CAR-T therapy for refractory CNS lymphoma triggers cytokine release syndrome and ICANS neurotoxicity, a particular hazard when the tumor sits within the brain itself."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Deep immunosuppression invites infection: high-dose methotrexate, the steroids it accompanies, and the disease's frequent HIV/immune-deficient context leave PCNSL patients prone to opportunistic infection and sepsis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Brain tumor and immobility clot the veins: like other CNS malignancies, PCNSL carries a high venous thromboembolism risk, complicated by the bleeding concern of anticoagulating a brain lesion."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "Its great mimic in AIDS is a parasite: a ring-enhancing brain lesion in an immunocompromised patient forces the distinction between PCNSL and cerebral toxoplasmosis, sometimes settled only by EBV PCR, thallium scan or biopsy."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "A brain mass can spark seizures: PCNSL infiltrating the cerebral cortex can irritate it into seizures, part of the neurological presentation alongside cognitive and focal deficits."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Its mainstay drug is hard on the kidneys: high-dose methotrexate, the backbone of PCNSL therapy, is nephrotoxic and itself cleared renally, so impaired or injured kidneys both threaten and are threatened by treatment."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its therapy's deep immunosuppression invites Pneumocystis: high-dose methotrexate, rituximab and corticosteroids leave PCNSL patients profoundly T-cell-suppressed, so prophylaxis against Pneumocystis pneumonia is routine throughout treatment."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Prolonged neutropenia and steroids open the door to mold: the intensive chemoimmunotherapy for PCNSL causes deep neutropenia and immune suppression, letting inhaled Aspergillus invade as life-threatening pulmonary or cerebral aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A brain cancer and its toxic therapy darken mood: PCNSL itself disrupts cerebral function, and the steroids, methotrexate neurotoxicity and possible whole-brain radiation add cognitive and depressive symptoms on top of the diagnosis."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Deep immune suppression reawakens shingles: the high-dose methotrexate chemoimmunotherapy and steroids for PCNSL deplete T-cell immunity, allowing latent varicella-zoster to reactivate, so antiviral prophylaxis is standard."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow-suppressing therapy and a chronic cancer blunt the blood: the cytotoxic chemotherapy for PCNSL plus the inflammatory state of an aggressive lymphoma produce anemia during treatment."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "An aggressive brain lymphoma breeds worry: the poor prognosis, relapse risk and intensive neurotoxic therapy of PCNSL foster chronic health anxiety alongside the depression and cognitive change it brings."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Steroids and radiation disturb the glands: the high-dose dexamethasone used in PCNSL causes steroid diabetes, and whole-brain radiation or sellar-region disease can damage the pituitary."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its mainstay drug injures gut and liver: high-dose methotrexate for PCNSL causes severe mucositis and hepatotoxicity, and chronic dexamethasone raises peptic-ulcer risk."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Prolonged steroids waste muscle and bone: the chronic dexamethasone used to control PCNSL oedema causes proximal steroid myopathy, osteoporosis and avascular necrosis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its key drug can block the kidney: the high-dose methotrexate central to PCNSL treatment can precipitate in the renal tubules causing acute kidney injury, needing hydration, alkalinisation and leucovorin rescue."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Drug and immunosuppression hit the lungs: methotrexate can cause pneumonitis, and the profound immunosuppression of PCNSL and its therapy invites Pneumocystis and fungal pneumonia."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its therapy assaults skin and mucosa: high-dose methotrexate causes severe mucositis and skin toxicity, and the dexamethasone used for oedema thins and bruises the skin."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Treatment and immobility strain the circulation: high-dose methotrexate regimens, corticosteroids and the high venous-thrombosis risk of CNS lymphoma all burden the cardiovascular system."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Targeted agents enter the brain: BTK inhibitors like ibrutinib, immunomodulators and rituximab supplement high-dose methotrexate against primary CNS lymphoma."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "Immunodeficiency invites it: in advanced HIV infection, EBV-driven primary CNS lymphoma emerges, historically an AIDS-defining brain tumour distinguished from toxoplasmosis."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "High-dose methotrexate is the backbone: HD-MTX-based chemoimmunotherapy, which crosses the blood-brain barrier, is the curative-intent treatment for primary CNS lymphoma, often consolidated with autologous transplant."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Cell therapy crosses into the brain: CD19 CAR-T cells produce responses in relapsed primary CNS lymphoma, showing engineered T cells can reach and clear disease behind the blood-brain barrier."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Uniquely PD-L1-rich among lymphomas: 9p24.1 alterations raise PD-L1 in primary CNS lymphoma, and PD-1 inhibitors such as nivolumab have shown activity in relapsed disease."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Opposite ends of the B-cell spectrum: primary CNS lymphoma is an aggressive ABC-type diffuse large B-cell lymphoma (MYD88/CD79B), whereas follicular lymphoma is an indolent germinal-centre-derived B-cell lymphoma—same lineage, opposite tempo and biology."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "A shared dependence on BTK: primary CNS lymphoma's MYD88-driven NF-κB and CLL's B-cell-receptor signalling both run through Bruton tyrosine kinase, so BTK inhibitors like ibrutinib are active against both."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Immunosuppression can seed it: methotrexate and other immunosuppressants used in rheumatoid arthritis can trigger EBV-driven lymphoproliferative disease, including CNS lymphoma that may regress when the drug is withdrawn."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Neurotoxicity and memory: primary CNS lymphoma and the high-dose methotrexate and whole-brain radiation used to treat it injure the hippocampus, causing the cognitive decline that especially burdens older survivors."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Angiocentric infiltration: PCNSL grows in perivascular cuffs deep in the brain, diffusely infiltrating white-matter tracts rather than forming a resectable mass—why diagnosis is by biopsy, not surgery."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "A steroid-responsive mimic: PCNSL can transiently shrink with corticosteroids, masquerading as an inflammatory or demyelinating lesion like multiple sclerosis and delaying diagnosis if steroids precede biopsy."
  - target: 02-pathogen/03-fungi/cryptococcus-neoformans
    relation: connects-to
    note: "An infectious mass mimic: in an HIV or immunosuppressed patient, a brain lesion's differential includes cryptococcoma alongside toxoplasmosis and PCNSL, so biopsy and CSF studies are needed to tell tumour from infection."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Iatrogenic lymphoma: long-term immunosuppression for autoimmune diseases such as lupus predisposes to EBV-driven CNS lymphoproliferative disease, an immunodeficiency-associated route to PCNSL like that seen with methotrexate."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Angiocentric growth: PCNSL characteristically grows in perivascular cuffs around cerebral vessels, infiltrating the arterial wall and Virchow-Robin spaces, a pattern that helps distinguish it from glioma at biopsy."
  - target: 01-human/03-molecular/foxo1
    relation: connects-to
    note: "Recurrent driver: FOXO1 mutations recur in primary CNS lymphoma, dysregulating this transcription factor in the malignant germinal-centre-derived B cells."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Cell-cycle brake lost: CDKN2A deletion is frequent in PCNSL, removing a key cell-cycle checkpoint and conferring a poorer prognosis."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Germinal-centre epigenetics: EZH2 enforces the proliferative, anti-differentiation chromatin programme of the germinal-centre B cells from which PCNSL arises."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "Cell-cycle drive: with CDKN2A loss frequent in PCNSL, cyclin D-CDK4/6 activity propels the lymphoma cells through the G1 checkpoint."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "CNS angiogenesis: VEGF drives the angiogenesis of these brain lymphomas, whose angiocentric growth pattern wraps proliferating B cells around cerebral vessels."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Tumour hypoxia: HIF-1α stabilised in the hypoxic CNS lymphoma drives the metabolic adaptation and angiogenesis that support its growth within the brain."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine survival loop: autocrine IL-6 in PCNSL signals through JAK1/2-STAT3 to sustain the malignant B cells, an axis layered on the MYD88-driven NF-κB activation that defines this ABC-type lymphoma."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PI3K-AKT-mTOR drive: constitutive BCR and MYD88 signalling converge on PI3K-AKT-mTOR in PCNSL, driving the protein synthesis and proliferation that fuel its rapid intracerebral growth."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune escape: PCNSL frequently deletes the 6p21 HLA region and loses MHC class II expression, blunting antigen presentation so the tumour evades immune surveillance within the immune-privileged CNS."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Chemotherapy apoptosis: high-dose methotrexate that crosses the blood-brain barrier kills PCNSL cells through caspase-3-mediated apoptosis, and the BCL-2-driven apoptotic resistance of this lymphoma underlies the relapses that follow initial response."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Diagnostic biomarker: PCNSL cells secrete IL-10, and an elevated cerebrospinal-fluid IL-10 level (and high IL-10/IL-6 ratio) is a diagnostic and prognostic marker that also serves as autocrine survival signalling for the tumour."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3K-pathway loss: PCNSL frequently deletes PTEN on 9p alongside CDKN2A, releasing the brake on PI3K-AKT-mTOR signalling that drives proliferation and supports the dependence on the same pathway targeted by mTOR and PI3K inhibitors."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K activation: with PTEN deleted, PIK3CA-driven PI3K signalling sustains the constitutive AKT-mTOR activity of PCNSL, working alongside the BTK/MYD88-NF-κB axis and offering a second targetable node for PI3K inhibitors in this aggressive CNS lymphoma."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "PD-L1 induction: interferon-γ from the reactive T-cell infiltrate, together with 9p24.1 copy gains, drives PD-L1 expression on PCNSL cells, creating the immune-checkpoint vulnerability that motivates PD-1 blockade in this immune-privileged tumour."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ signalling: STAT1 is the transcription factor relaying interferon-γ signals to induce PD-L1 and antigen-presentation genes in PCNSL, the JAK-STAT arm (with the JAK2 of 9p24.1) shaping its immunosuppressive microenvironment."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: CDKN2A loss (mapped) frees the cyclin-D1-CDK4/6 axis to release E2F1, driving the high proliferative rate of primary CNS lymphoma."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Adverse genetics: TP53 alterations occur in primary CNS lymphoma and are associated with a poorer response to high-dose-methotrexate-based therapy."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell survival: the cytokine BAFF supports the survival of the malignant B cells of PCNSL, reinforcing the MYD88-CD79B-BTK-NF-κB signalling (mapped) on which they depend."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Cell-cycle restraint: the RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) restrains proliferation, and its dysregulation contributes to the aggressive growth of primary CNS lymphoma."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "BCR-MAPK proliferation: chronic-active B-cell-receptor signalling activates RAS-ERK alongside the MYD88-NF-κB axis (already mapped) to drive proliferation in primary CNS lymphoma."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "Apoptosis evasion: MDM2-mediated p53 inactivation (p53 already mapped) contributes to the apoptosis evasion of primary CNS lymphoma."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the immunosuppressive CNS microenvironment and survival of primary CNS lymphoma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β within the immune-privileged CNS shapes the immunosuppressive microenvironment that shelters primary CNS lymphoma."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING influences the immune microenvironment and immunotherapy responsiveness of primary CNS lymphoma."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) normally restrains B-cell proliferation, a brake overridden in the lymphomagenesis of primary CNS lymphoma."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors, restrained by the BCR-PI3K-AKT signalling of the MYD88/CD79B-mutant clone, modulate the survival of primary CNS lymphoma."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression of primary CNS lymphoma."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the MYC stability and NF-κB-driven survival signaling of primary CNS lymphoma."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance targets the immune-privileged-site primary CNS lymphoma."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the neuroinflammatory microenvironment of primary CNS lymphoma."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LYN) kinase signaling downstream of the chronically active B-cell receptor supports the survival of primary CNS lymphoma cells."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of primary CNS lymphoma."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and chemoresistance of primary CNS lymphoma cells."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of primary CNS lymphoma."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the CNS homing of primary CNS lymphoma."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of primary CNS lymphoma."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor microenvironment of primary CNS lymphoma."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory tumor-immune microenvironment of primary CNS lymphoma."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory tumor microenvironment of primary CNS lymphoma."
  - target: 01-human/03-molecular/lmp1
    relation: connects-to
    note: "EBV-driven variant: in immunocompromised hosts primary CNS lymphoma is typically EBV-positive, and the viral oncoprotein LMP1 mimics constitutive CD40 signalling to activate NF-kB (already mapped), driving the B-cell transformation of this immunodeficiency-associated subtype."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-4/STAT6 survival axis: an IL-4 signature expressed by tumour vasculature in primary CNS lymphoma engages STAT6 to support malignant B-cell survival and correlates with outcome, a microenvironmental dependency beyond the intrinsic MYD88/BTK signalling."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory milieu: TNF-alpha is an NF-kB-driven cytokine (NF-kB already mapped) enriched in the primary CNS lymphoma microenvironment, sustaining the reactive perivascular inflammation and blood-brain-barrier disruption that accompany the tumour."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "CNS-directed CAR-T: IL-2-driven T-cell expansion powers the CD19 CAR-T therapy (perforin already mapped) that can cross into the central nervous system and produce responses in relapsed primary CNS lymphoma."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Checkpoint blockade: primary CNS lymphoma, which often amplifies PD-L1 (PD-1 already mapped), can respond to checkpoint inhibitors, and CTLA-4 blockade is explored in combination to strengthen the anti-tumour T-cell response."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Treatment myelosuppression: the high-dose methotrexate-based chemotherapy central to primary CNS lymphoma is myelosuppressive, lowering haemoglobin and requiring transfusion and growth-factor support during treatment."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: initiating chemotherapy for bulky primary CNS lymphoma can lyse the tumour rapidly, releasing purines that xanthine oxidase converts to uric acid, a tumour-lysis risk managed with allopurinol and hydration."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Tumour-lysis acidosis: the rapid lysis of primary CNS lymphoma by chemotherapy releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped), part of its acute metabolic risk."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of primary CNS lymphoma, part of the microenvironment behind its characteristic angiocentric growth around cerebral vessels."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6 and IL-1 already mapped) of the primary CNS lymphoma microenvironment."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chemotherapy anaemia: the high-dose methotrexate-based chemotherapy of primary CNS lymphoma is myelosuppressive, causing anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune milieu: IL-13, with IL-4 (already mapped), reflects the type-2 cytokine arm of the immune microenvironment of primary CNS lymphoma, part of the cytokine milieu shaping the tumour."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and adds an anaemia of chronic disease to the high-dose-methotrexate anaemia (iron already mapped) of primary CNS lymphoma."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic and cachexia: the corticosteroids (cortisol already mapped) and the disease disturb leptin and energy balance, part of the metabolic dimension and the cachexia of the often-elderly primary-CNS-lymphoma patient."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate CNS immunity: type-I interferon signalling is part of the innate antiviral immunity of the immune-privileged CNS, relevant to the EBV-driven (LMP1 already mapped) primary CNS lymphoma of the immunosuppressed."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic-cachexia adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-cachexia axis of the often-elderly primary CNS lymphoma patient."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic milieu of primary CNS lymphoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate CNS surveillance: the natural killer cells (perforin already mapped) provide the innate cytotoxic surveillance of the CNS, and the CAR-NK cell therapy is explored for the immune-privileged primary CNS lymphoma."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-lymphoma response of the immune-privileged primary CNS lymphoma microenvironment."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immune microenvironment of primary CNS lymphoma."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune microenvironment of primary CNS lymphoma."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 antibody arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 humoral dimension of the immune microenvironment of primary CNS lymphoma."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell infiltrate: the mast cells are part of the tumour immune microenvironment infiltrate of primary CNS lymphoma, contributing to the type-2 and pro-angiogenic (VEGF already mapped) milieu."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin arm: TSLP, an epithelial/stromal alarmin, is part of the type-2 (IL-4 and IL-13 already mapped) dimension of the immune microenvironment of primary CNS lymphoma."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells of the reactive infiltrate are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of primary CNS lymphoma."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Type-2 cytokine: IL-31, with TSLP (already mapped), extends the type-2 (IL-4 and IL-13 already mapped) dimension of the immune microenvironment of primary CNS lymphoma."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is part of the type-2 stromal-remodelling dimension of the primary-CNS-lymphoma microenvironment."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Rituximab CDC: the complement C3 activation is the initiating step of the complement-dependent cytotoxicity by which the anti-CD20 (already mapped) rituximab kills the primary-CNS-lymphoma B cells (already mapped)."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 (with C3 already mapped) is the effector of the membrane-attack complex of the rituximab complement-dependent cytotoxicity against primary CNS lymphoma."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) and myeloid inflammation of the primary-CNS-lymphoma microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "BBB-permeability therapy: bradykinin B2-receptor agonists (e.g. labradimil) have been used experimentally to transiently open the blood-brain barrier, enhancing the CNS delivery of the methotrexate that is central to primary-CNS-lymphoma treatment."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway brake: C1-esterase inhibitor regulates the classical complement pathway activated by the anti-CD20 (already mapped) rituximab in the CSF compartment, modulating complement-dependent cytotoxicity in primary CNS lymphoma."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Neuroinflammatory mediator: histamine, released by the CNS-infiltrating mast cells and tumour-associated macrophages (microglia already mapped) of primary CNS lymphoma, promotes the neuroinflammatory microenvironment and angiogenesis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Chemotherapy anaemia: erythropoietin corrects the high-dose methotrexate- and rituximab-induced marrow suppression anaemia of primary CNS lymphoma; EPOR expression in the CNS lymphoma B cells has also been reported."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion in CSF: primary CNS lymphoma cells recruit factor H to limit the C3/C5/C5aR1 (all already mapped) complement-dependent cytotoxicity of rituximab within the immune-privileged CNS compartment."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-immune axis: melatonin modulates CNS immune surveillance (microglia already mapped), regulating natural killer cell activity (already mapped) and the B-cell proliferation underlying the immune dysregulation of primary CNS lymphoma."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "PCNSL androgen axis: testosterone via androgen receptor modulates CNS B-cell proliferation and the blood-brain barrier permeability governing PCNSL compartmentalisation, intersecting the BCR (already mapped) and PI3K/AKT (already mapped) signalling pathways."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "PCNSL serotonin: serotonin modulates CNS immune microenvironment and B-cell proliferation underlying primary CNS lymphoma, and serotonin receptor signalling on CNS B-cell lymphoma cells intersects the BCR (already mapped) and PI3K/AKT (already mapped) pathways."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "PCNSL prolactin: prolactin promotes B-cell survival and class-switching via JAK2/STAT5 (already mapped) signalling, amplifying the malignant CNS B-cell proliferation and CXCR4 (already mapped)-mediated CNS compartmentalisation of primary CNS lymphoma."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PCNSL oxytocin: oxytocin modulates CNS immune surveillance and blood-brain barrier integrity, intersecting the neuroinflammatory microenvironment (microglia already mapped) and B-cell proliferation (BCR already mapped) underlying primary CNS lymphoma compartmentalisation."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PCNSL vasopressin: vasopressin via AVPR modulates blood-brain barrier permeability and CNS fluid homeostasis, influencing the immune-privileged compartment that permits primary CNS lymphoma escape from systemic immune surveillance (NF-κB already mapped)."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "PCNSL selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species driving genomic instability and lymphoma-promoting NF-κB (already mapped) signalling in the malignant B cells of primary CNS lymphoma."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PCNSL iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of primary CNS lymphoma."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "PCNSL sodium: excess sodium promotes macrophage (already mapped) and microglia (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) CNS lymphoma cascade."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "PCNSL magnesium: magnesium, as cofactor of DNA repair enzymes in neurons (already mapped) and macrophages (already mapped), supports brain-immune homeostasis; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of PCNSL."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "PCNSL copper: copper-dependent enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustain CNS tumour-immune balance; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in the primary CNS lymphoma microenvironment."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "PCNSL phosphorus: phosphorus-dependent ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) drives lymphoma-infiltrating immune responses; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in PCNSL."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "PCNSL zinc: zinc co-factors in macrophage (already mapped) and T-cytotoxic (already mapped) immune effector functions; zinc depletion exacerbates NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling and microglia (already mapped) activation in PCNSL."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "PCNSL carbon: carbon as backbone of NF-κB (already mapped) and BCL-2 proteins in lymphoma cells and microglia (already mapped) sustains tumour survival signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in PCNSL."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "PCNSL chloride: chloride channels in microglia (already mapped) and lymphoma cells modulate cell-volume and invasive potential in the CNS; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of PCNSL."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "PCNSL hydrogen: hydrogen, via redox homeostasis in microglia (already mapped) and lymphoma cells, supports BCL-2-mediated survival; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of PCNSL."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "PCNSL nitrogen: nitrogen in amino-acid scaffold of BCL-2 (already mapped) and NF-κB (already mapped) proteins in lymphoma cells sustains oncogenic CNS signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of PCNSL."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "PCNSL oxygen: oxygen, via mitochondrial respiration in microglia (already mapped) and lymphoma cells, sustains CNS energy homeostasis; oxygen depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of PCNSL."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "PCNSL sulfur: sulfur in cysteine residues of BCL-2 (already mapped) and NF-κB (already mapped) proteins in lymphoma cells sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of PCNSL."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "PCNSL glp-1: GLP-1 from macrophages (already mapped) and microglia (already mapped) modulates metabolic-inflammatory CNS tumour tone; glp-1 dysfunction amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PCNSL."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "PCNSL angiotensin-ii: angiotensin-II from macrophages (already mapped) and microglia (already mapped) drives CNS tumour angiogenesis; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PCNSL."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "PCNSL wnt-beta-catenin: WNT/β-catenin on lymphoma cells (already mapped) and microglia (already mapped) drives CNS tumour invasion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of PCNSL."
---

# Primary CNS Lymphoma

## Overview

**Primary CNS lymphoma (PCNSL)** is a rare extranodal non-Hodgkin lymphoma confined at diagnosis to the **central nervous system** (brain parenchyma, spinal cord, leptomeninges, cranial nerves, eyes) without systemic involvement. PCNSL is almost universally of **ABC-DLBCL (activated B-cell-like diffuse large B-cell lymphoma) histology**, with near-universal expression of **MYD88 L265P** (~90%) and frequent **CD79B mutations** (~70%) — creating a distinct genomic profile that explains CNS tropism and BTK inhibitor sensitivity [^grommes-2017-ibrutinib-pcnsl]. The **blood-brain barrier (BBB)** presents a fundamental challenge to drug delivery: most effective systemic lymphoma therapies (rituximab, cyclophosphamide, doxorubicin) achieve inadequate CNS penetration, making **high-dose methotrexate (HDMTX)** — which crosses the BBB via organic anion transporters — the irreplaceable backbone of PCNSL treatment. Despite high initial response rates to HDMTX-based therapy (~75-80% CR), PCNSL has a high relapse rate and poor long-term outcomes (5-year OS ~30-40%), underscoring the need for effective consolidation strategies and novel agents [^bromberg-2019-hovon105].

**Epidemiology:**
- Incidence: ~1,500 cases/year USA; ~7,000 globally; 1-5% of all primary brain tumors
- Median age at diagnosis: ~65 years (immunocompetent); younger in HIV-associated (median ~35 years)
- Risk factors: Immunosuppression (HIV, solid organ transplant, autoimmune therapy); age >60; male predominance (M:F ~1.3:1)
- HIV-associated PCNSL: EBV-driven; CD4 count usually <50/μL; dramatically reduced in HAART era
- Immunocompetent PCNSL: EBV-negative; MYD88 L265P ~90%; genetically distinct

## Structure

### Molecular and genomic architecture

**Core driver mutations:**
- **MYD88 L265P (~90%):** Constitutive IRAK4-NF-κB + JAK1-STAT3 → lymphocyte survival; highest MYD88 L265P prevalence of any cancer type
- **CD79B Y196H/N/S/D (~70%):** BCR co-receptor mutations → chronic active BCR signaling → BTK activation → NF-κB; CD79B Y196 is the primary phosphorylation site for SYK → Y196 mutation prevents ITAM-dependent SYK downregulation → persistent BCR signal
- **MYD88+CD79B co-mutation (~65% PCNSL):** Near-universal co-occurrence drives synergistic NF-κB from two converging pathways; predicts BTK inhibitor sensitivity; together called the "double-mutant" PCNSL
- **CARD11 mutations (~15%):** Constitutive NF-κB via CBM complex
- **CDKN2A deletion (~50%):** p16/p14 loss; p53 pathway impairment
- **HLA class I and II loss (~40%):** Immune evasion in CNS immune-privileged site
- **MYC rearrangement/amplification (~15%):** Aggressive subset; double-hit PCNSL (MYD88+MYC) has very poor prognosis

**Immune privilege mechanism:**
PCNSL exploits CNS immune privilege: (1) BBB restricts lymphocyte trafficking — fewer patrolling cytotoxic T cells; (2) Microglia (CNS-resident macrophages) are anti-inflammatory; (3) PCNSL cells downregulate MHC class I/II → evade CTL killing; (4) PD-L1 overexpression (MYD88-NF-κB → PD-L1 transcription) further suppresses T-cell function; the CNS thus provides a sanctuary from immune surveillance analogous to the testicular "immune privilege" that explains primary testicular DLBCL sharing the same MYD88+CD79B profile.

**Vitreoretinal lymphoma (VRL):**
~15-25% of PCNSL involves the vitreous/retina simultaneously (primary intraocular lymphoma); VRL is usually the ocular manifestation of the same PCNSL clone; shares MYD88 L265P (~90%), CD79B mutations (~60%); vitreous biopsy with cytology + IL-10 measurement is diagnostic; often presents as "uveitis" and is misdiagnosed; PCNSL can follow isolated VRL by months to years.

### Histopathology

**Morphology:** Large B cells with prominent nucleoli; perivascular (angiocentric) growth pattern (tumor cells cuffing blood vessels); necrosis variable; reactive T cells sparse (immune-depleted microenvironment); prominent gliosis.

**Immunophenotype:** CD20+, CD19+, CD10−, BCL6±, IRF4/MUM1+, PAX5+, BOB1+, OCT2+ (ABC-DLBCL pattern); Ki-67 >90% common; EBV EBER negative (immunocompetent); EBER+ only in HIV-associated.

**Radiologic features (MRI):**
- Solitary or multiple lesions (75% in brain parenchyma); hemispheres most common; periventricular white matter; basal ganglia; corpus callosum
- Isointense T1, homogeneous gadolinium enhancement (vivid enhancement due to BBB disruption); no ring enhancement (unlike glioblastoma/abscess)
- Restricted diffusion on DWI (hypercellular tumor)
- Spontaneous regression on steroids (lympholytic effect) → "ghost tumor" phenomenon; biopsy before steroids if possible

## Function

### Normal BBB and CNS lymphocyte trafficking

Lymphocytes normally cross the BBB via VCAM-1/ICAM-1 and VLA-4/LFA-1 interactions at postcapillary venules → patrolling within the CNS parenchyma; in PCNSL, neoplastic B cells with high CXCR4 and CXCR5 expression home to CXCL12-rich (CNS endothelium) and CXCL13-rich (follicular microenvironment-like niches) zones within the CNS, explaining CNS tropism; intact BBB explains why rituximab (168 kDa, poor BBB penetration) adds little benefit over HDMTX alone in the CNS.

## Pathology

### Diagnosis

**Clinical presentation:**
Cognitive decline (~70%), focal neurologic deficits (hemiparesis, aphasia, ~50%), personality change, headache, seizures (~10%); visual symptoms (floaters, blurred vision if VRL); B symptoms uncommon (not systemic lymphoma); rapid progression over weeks without treatment → herniation.

**Diagnostic workup:**
- Brain MRI with gadolinium (mandatory); whole-spine MRI if cord symptoms
- CSF analysis: cytology (lymphoma cells in ~50%), flow cytometry (CD19+CD10-), protein (elevated), glucose, VDRL; CSF cell-free DNA (cfDNA) for MYD88 L265P (sensitivity ~60-70%); IgH rearrangement by PCR
- **Vitreous/aqueous humor IL-10:** IL-10 >10 pg/mL + IL-10:IL-6 ratio >1 in VRL is highly specific (>90%); send both IL-6 and IL-10
- **Slit-lamp examination:** VRL in vitreous; subretinal infiltrates
- Brain biopsy (stereotactic): gold standard; defer until after CSF/vitreous attempts; avoid corticosteroids before biopsy (steroid-induced CR can prevent diagnosis)
- Systemic staging: PET-CT (exclude systemic involvement); testicular ultrasound in males (testis is immune-privileged site; occult testicular lymphoma can present as PCNSL); BM biopsy
- HIV testing, immunosuppression history
- Ophthalmologic evaluation (slit-lamp + fundus)

### Treatment

**Induction (fit patients):**
- **HDMTX-based regimens:** Methotrexate 3-8 g/m²  over 3-4 hours IV with leucovorin rescue + alkaline hydration; penetrates BBB via reduced folate carrier; CSF levels reach therapeutic concentrations; ORR ~75-80%
- **R-MPV (rituximab, methotrexate, procarbazine, vincristine):** Widely used; MTX 3.5 g/m² days 2, 15; rituximab IV (poor BBB penetration but may reach leptomeninges); ORR ~78% CR; HOVON 105 trial (rituximab + HDMTX vs HDMTX alone): CR 49% vs 38% (p=0.071, not significant); rituximab benefit trend but not proven [^bromberg-2019-hovon105]
- **MATRix (methotrexate, cytarabine, thiotepa, rituximab):** IELSG32 trial: CR 49% vs 23% (HDMTX alone); PFS superior; used widely in Europe
- Intrathecal MTX or cytarabine: for leptomeningeal disease; not routinely added to systemic HDMTX

**Consolidation:**
- **Autologous SCT (BEAM or thiotepa-based conditioning):** IELSG43 trial (auto-SCT vs WBRT): equivalent PFS ~2 years; auto-SCT preferred (avoids neurotoxicity of WBRT); BEAM-R: carmustine, etoposide, cytarabine, melphalan + rituximab conditioning
- **WBRT (whole-brain radiotherapy, 23.4-45 Gy):** Highly effective (ORR ~90% in recurrent) but severe neurotoxicity (white matter changes, cognitive decline, leukoencephalopathy) in >60% of patients >60 years; now reserved for young/fit patients or relapse setting
- **High-dose cytarabine consolidation:** Alternative to auto-SCT in older/frail patients
- **Maintenance rituximab:** Under investigation; limited CNS penetration argues against utility

**Relapsed/Refractory PCNSL:**
- **Ibrutinib (BTK inhibitor):** ORR ~50-60% (Phase 1/2: 15/20 patients responded, CR in 10/20); CSF penetration ~50-75% of plasma; CNS response correlates with MYD88 L265P; combinations with MTX, rituximab being studied; atrial fibrillation, bleeding risk [^grommes-2017-ibrutinib-pcnsl]
- **Zanubrutinib:** More selective BTK inhibitor; better CNS penetration; Phase 2 in R/R PCNSL ongoing
- **Pirtobrutinib (non-covalent BTK inhibitor):** Active after covalent BTK inhibitor failure; PCNSL cohort in Phase 2
- **TEDDi-R (thiotepa, etoposide, dexamethasone, dexamethasone, ibrutinib, rituximab):** Feasibility shown; high ORR (~90%) but high toxicity
- **Lenalidomide + rituximab (R²):** ORR ~35% in R/R PCNSL; immunomodulatory
- **Nivolumab/pembrolizumab:** ORR ~35% in R/R PCNSL (MYD88-driven PD-L1 upregulation); durable responses in subset
- Re-HDMTX: Active in patients relapsing >12 months after initial HDMTX

**Elderly/frail patients (age >70):**
- Reduced-dose MTX (1.5-2 g/m²) ± procarbazine/vincristine
- Ibrutinib as primary therapy or maintenance
- WBRT at reduced dose (23.4 Gy) as monotherapy in very frail patients

**HIV-associated PCNSL:**
- HAART + HDMTX-based therapy if CD4 >50 and performance status allows
- EBV-driven: HAART alone may induce regression in some (immune reconstitution)
- Prognosis significantly improved with HAART era vs pre-HAART (OS weeks → months/years)

### Prognostic scoring (IELSG score)

International Extranodal Lymphoma Study Group (IELSG) score — 5 adverse factors:
1. Age >60 years
2. ECOG PS >1
3. Elevated LDH
4. High CSF protein
5. Deep brain involvement (corpus callosum, basal ganglia, brainstem, cerebellum)

Score 0-1: 2-year OS ~80%; Score 2-3: ~48%; Score 4-5: ~15%

## Connections

- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — MYD88 L265P is present in ~90% of PCNSL — the highest prevalence in any cancer outside WM; constitutive IRAK4-NF-κB signaling drives RS cell survival; ibrutinib (BTK inhibitor) crosses the blood-brain barrier and shows ORR ~50-60% in R/R PCNSL via MYD88-BTK pathway suppression.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PCNSL tumor cells express PD-L1 driven by MYD88-NF-κB and JAK-STAT3 signaling; CNS immune privilege maintains low T-cell surveillance; nivolumab and pembrolizumab show modest activity in R/R PCNSL (ORR ~35%); PD-L1 blockade combined with HDMTX is under investigation.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK is the downstream effector of BCR and MYD88 signaling in PCNSL; ibrutinib (BTK covalent inhibitor) achieves ~50-75% of plasma levels in CSF and shows ORR ~50-60% in R/R PCNSL; ibrutinib+MTX+rituximab (TEDDi-R) studied as frontline; zanubrutinib also CNS-penetrant.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — MYD88 L265P drives IL-6 and IL-10 autocrine in PCNSL; vitreous IL-10 >10 pg/mL and IL-10:IL-6 ratio >1 are pathognomonic for PCNSL/vitreoretinal lymphoma; IL-10 drives JAK1-STAT3 survival in tumor cells; CSF IL-10 elevation correlates with PCNSL disease burden and response.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — PCNSL is non-Hodgkin lymphoma confined to the CNS (periventricular, basal ganglia, corpus callosum) as homogeneously enhancing masses with restricted diffusion; the blood-brain barrier blocks most lymphoma drugs, making BBB-penetrant high-dose methotrexate the backbone.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — PCNSL is an aggressive B-cell lymphoma (ABC-DLBCL): CD20+ neoplastic B cells with MYD88 L265P and CD79B mutations driving NF-κB; they home to the CNS via CXCR4/CXCR5 and evade immunity by downregulating MHC — rituximab penetrates the BBB poorly, limiting anti-CD20 benefit.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — In immunosuppressed patients (HIV with CD4 <50, transplant), PCNSL is typically EBV-driven and EBER-positive — a distinct entity from the EBV-negative, MYD88-mutant immunocompetent form; restoring immunity with HAART can induce regression of EBV-associated CNS lymphoma.
- `connects-to` → **[Peripheral T-cell Lymphoma](../ptcl/README.md)** — Primary CNS lymphoma and peripheral T-cell lymphoma are aggressive non-Hodgkin lymphomas of opposite lineage: PCNSL is a B-cell (ABC-DLBCL) tumor driven by MYD88/CD79B-NF-κB, PTCL a heterogeneous T-cell group driven by TET2/RHOA/STAT3 — different cells, different therapies.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Primary CNS lymphoma is essentially a diffuse large B-cell lymphoma (ABC type) trapped in the CNS: it shares DLBCL's CD20+ biology and MYD88/CD79B-NF-κB drivers, but immune privilege and the blood-brain barrier make it behave differently — high-dose methotrexate, not R-CHOP.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Primary CNS lymphoma has an ocular form — vitreoretinal lymphoma — that seeds the eye as painless floaters or steroid-refractory uveitis; a vitreous IL-10:IL-6 ratio >1 and MYD88 L265P clinch the diagnosis, and ~15-25% of PCNSL involves the eye, often bilaterally.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Primary CNS lymphoma is an AIDS-defining cancer: in advanced HIV with low CD4 counts, EBV-driven B-cell lymphoma arises in the brain, so a periventricular mass in AIDS raises PCNSL versus toxoplasmosis—distinguished by EBV PCR of CSF and thallium imaging.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Whole-brain photon radiotherapy once anchored PCNSL treatment but is now used cautiously: the tumor is exquisitely radiosensitive, yet WBRT causes severe delayed neurocognitive decline, so high-dose methotrexate is preferred and radiation reserved or dose-reduced.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — PCNSL grows in the unique immune environment policed by microglia: this EBV-driven B-cell lymphoma proliferates around vessels in brain parenchyma, and reactive microglia form the perivascular cuffs and inflammatory backdrop characteristic of its histology.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — PCNSL and glioblastoma are the two great intra-axial brain masses that imaging can confuse: both enhance and infiltrate, but PCNSL is a B-cell lymphoma exquisitely steroid- and methotrexate-sensitive, while GBM needs surgery and chemoradiation—biopsy is decisive.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — PCNSL and meningioma are both intracranial tumors but opposite: PCNSL is an intra-axial B-cell lymphoma treated with methotrexate, while meningioma is an extra-axial dural tumor cured by resection—MRI location usually separates the medical from the surgical disease.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — PCNSL and mantle cell lymphoma can both involve the CNS: primary CNS lymphoma is a brain-confined DLBCL, while aggressive systemic lymphomas like MCL can spread secondarily to the leptomeninges—so CNS lymphoma may be primary or secondary.
- `connects-to` → **[Immune System](../immune-system/README.md)** — PCNSL is largely a disease of immune failure: it is far commoner in HIV/AIDS and transplant immunosuppression, where unchecked EBV transforms B cells in the brain—so immune status drives both its incidence and (with immune restoration) sometimes its regression.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — PCNSL arises from a late germinal-center B cell trapped in the CNS: it is a post-germinal-center DLBCL expressing BCL6/IRF4 that, oddly, homes to and grows within the immune-privileged brain—so it shares lymphoma-node biology yet behaves as a CNS tumor.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC and BCL2 co-expression marks aggressive PCNSL: like systemic DLBCL, double-expressor PCNSL carries a worse prognosis, but the blood-brain barrier limits which drugs reach it—so high-dose methotrexate, not standard R-CHOP, anchors treatment.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — PCNSL is a CD20-positive B-cell lymphoma treated through that target: high-dose methotrexate crosses the blood-brain barrier and is combined with the anti-CD20 antibody rituximab, exploiting the same B-cell marker used against systemic lymphomas.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Primary CNS lymphoma is a lymphoma confined to the nervous system: it grows in the brain, spinal cord, eyes and meninges without nodal disease, so it presents with focal deficits and cognitive change—and its CNS sanctuary demands brain-penetrant therapy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — PCNSL is a striking exception within the lymphatic system: though a B-cell lymphoma, it arises and stays in the immune-privileged CNS rather than lymph nodes, so staging is typically negative outside the brain and eye—unlike systemic DLBCL.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — PCNSL survives on chronic NF-kB signaling: MYD88 and CD79B mutations lock this pathway on, driving the lymphoma's growth—the rationale for BTK inhibitors like ibrutinib that choke off the B-cell-receptor input to NF-kB.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CAR-T cells are reaching into the brain for PCNSL: CD19-directed cytotoxic T cells engineered to kill B-cell lymphoma are being trialed in relapsed central-nervous-system lymphoma, with responses showing the cells can work inside the CNS.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — PCNSL and Waldenstrom share the MYD88 L265P mutation: both are MYD88-driven B-cell malignancies that respond to BTK inhibition, so a brain lymphoma's mutation links it mechanistically to this marrow-based lymphoplasmacytic cancer.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — PCNSL stays trapped in the brain by CXCL12: the CNS pours out this chemokine, and the lymphoma cells' CXCR4 receptor locks onto it, explaining why this aggressive B-cell lymphoma homes to and stays confined within the brain and eye.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — PCNSL is laced with reactive macrophages and microglia: a perivascular cuff of these innate immune cells surrounds the tumor, a histologic hallmark that both shapes the immune-privileged niche and can confound the biopsy diagnosis.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — PCNSL exploits the brain's immune privilege with regulatory T cells: behind the blood-brain barrier and amid Treg-rich infiltrates, the tumor evades attack, part of why systemic immunotherapy struggles to reach and clear CNS lymphoma.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — PCNSL survives on B-cell-receptor calcium signaling: with MYD88 and BTK-driven activation, a calcium flux keeps the malignant B cells alive in the brain, which is why BTK inhibitors that interrupt this pathway can penetrate the CNS and work.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are scarce in the brain that PCNSL exploits: the CNS has few professional antigen-presenters, so the lymphoma faces weak priming of an immune response—part of the immune privilege that lets it grow behind the blood-brain barrier.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PCNSL leans on the PI3K-AKT-mTOR axis downstream of BTK: chronic B-cell-receptor and MYD88 signaling feed AKT to drive survival, so AKT-mTOR inhibitors are studied alongside BTK inhibitors for this aggressive brain lymphoma.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — PCNSL's cure depends on the kidneys: its mainstay treatment, high-dose methotrexate, is cleared by the kidneys and is toxic to them, so renal function must be protected to deliver the drug safely.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — PCNSL grows hugging the blood vessels: the malignant B cells cuff around cerebral vessels in an angiocentric pattern, leaning on the endothelial-lined vasculature behind the blood-brain barrier.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — PCNSL can spill potassium when it melts: this aggressive lymphoma responds fast to steroids and chemo, and the rapid cell death can trigger tumor lysis that floods the blood with potassium.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — The bone marrow defines what PCNSL is not: by definition the lymphoma stays in the brain, eye, and CSF, so a marrow biopsy is part of staging to rule out a systemic lymphoma that has merely spread to the nervous system.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — PCNSL is confirmed by an absent spleen lesion: full-body staging checks the spleen and other nodal sites because finding systemic disease would reclassify it as ordinary lymphoma, while late relapses can occasionally break out to these organs.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — PCNSL leans toward the plasma cell end of the B-lineage: its hallmark MYD88 mutation is shared with plasmacytic lymphomas, and the tumor cells often show plasmablastic features driving the same NF-κB survival signaling.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — PCNSL menaces the neuron from two sides: the infiltrating lymphoma crowds and destroys brain tissue to cause focal deficits, and the curative high-dose methotrexate with whole-brain radiation can later leave a disabling cognitive decline.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Treating PCNSL can strip the brain's myelin: high-dose methotrexate and whole-brain radiation injure oligodendrocytes, producing the delayed white-matter leukoencephalopathy that dims memory and slows thinking in survivors.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — PCNSL is defined by what it spares: by definition the lymphoma is confined to the CNS, so staging scans the liver and marrow precisely to exclude systemic DLBCL, whose visceral spread would change the disease and its treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both name and treat PCNSL: CD20 and MUM1 stains confirm its diffuse large B-cell nature on a stereotactic biopsy, and the anti-CD20 antibody rituximab is added to high-dose methotrexate to attack those same B cells.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Steroids make PCNSL a 'ghost tumor': corticosteroids are so lymphotoxic that the mass can melt away within days, erasing the target before biopsy — so steroids are held until tissue is obtained, even when the swelling tempts early use.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The methotrexate cure batters the marrow: the high-dose methotrexate regimens central to PCNSL are myelosuppressive, dropping neutrophil counts so that leucovorin rescue and infection vigilance run through every cycle.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — PCNSL survives on chronic signaling: alongside MYD88 and NF-kB activation, JAK-STAT3 signaling drives the lymphoma's growth and helps it evade immunity within the brain's sheltered environment, a pathway probed for targeted therapy.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The testis is a sanctuary that talks to the brain: testicular lymphoma notoriously relapses in the CNS, both being immune-privileged sites, so testicular DLBCL gets CNS prophylaxis — and PCNSL's intensive chemo threatens fertility in younger patients.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — The treatment also drops the platelets: high-dose methotrexate and the cytarabine often added suppress platelet production into thrombocytopenia, raising bleeding risk and limiting dose intensity through the months of therapy.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — It often carries a survival overdrive: many CNS lymphomas co-express BCL-2 with MYC as 'double-expressors', the anti-apoptotic signal keeping malignant B cells alive and a rationale for testing the BCL-2 inhibitor venetoclax against the disease.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — The tumor grows in glial turf: PCNSL infiltrates the brain parenchyma in angiocentric cuffs, surrounded by reactive astrocytes whose microenvironment and the blood-brain barrier shape both its growth and the difficulty of getting drugs to it.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Both lymphomas court the nervous system: like PCNSL, Burkitt lymphoma has a strong tropism for the central nervous system, which is why aggressive B-cell lymphomas demand CNS-penetrating therapy and prophylaxis to reach sanctuary sites.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — CAR-T against PCNSL can storm the brain: CD19 CAR-T therapy for refractory CNS lymphoma triggers cytokine release syndrome and ICANS neurotoxicity, a particular hazard when the tumor sits within the brain itself.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Deep immunosuppression invites infection: high-dose methotrexate, the steroids it accompanies, and the disease's frequent HIV/immune-deficient context leave PCNSL patients prone to opportunistic infection and sepsis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Brain tumor and immobility clot the veins: like other CNS malignancies, PCNSL carries a high venous thromboembolism risk, complicated by the bleeding concern of anticoagulating a brain lesion.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — Its great mimic in AIDS is a parasite: a ring-enhancing brain lesion in an immunocompromised patient forces the distinction between PCNSL and cerebral toxoplasmosis, sometimes settled only by EBV PCR, thallium scan or biopsy.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — A brain mass can spark seizures: PCNSL infiltrating the cerebral cortex can irritate it into seizures, part of the neurological presentation alongside cognitive and focal deficits.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Its mainstay drug is hard on the kidneys: high-dose methotrexate, the backbone of PCNSL therapy, is nephrotoxic and itself cleared renally, so impaired or injured kidneys both threaten and are threatened by treatment.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its therapy's deep immunosuppression invites Pneumocystis: high-dose methotrexate, rituximab and corticosteroids leave PCNSL patients profoundly T-cell-suppressed, so prophylaxis against Pneumocystis pneumonia is routine throughout treatment.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Prolonged neutropenia and steroids open the door to mold: the intensive chemoimmunotherapy for PCNSL causes deep neutropenia and immune suppression, letting inhaled Aspergillus invade as life-threatening pulmonary or cerebral aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A brain cancer and its toxic therapy darken mood: PCNSL itself disrupts cerebral function, and the steroids, methotrexate neurotoxicity and possible whole-brain radiation add cognitive and depressive symptoms on top of the diagnosis.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Deep immune suppression reawakens shingles: the high-dose methotrexate chemoimmunotherapy and steroids for PCNSL deplete T-cell immunity, allowing latent varicella-zoster to reactivate, so antiviral prophylaxis is standard.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow-suppressing therapy and a chronic cancer blunt the blood: the cytotoxic chemotherapy for PCNSL plus the inflammatory state of an aggressive lymphoma produce anemia during treatment.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — An aggressive brain lymphoma breeds worry: the poor prognosis, relapse risk and intensive neurotoxic therapy of PCNSL foster chronic health anxiety alongside the depression and cognitive change it brings.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Steroids and radiation disturb the glands: the high-dose dexamethasone used in PCNSL causes steroid diabetes, and whole-brain radiation or sellar-region disease can damage the pituitary.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its mainstay drug injures gut and liver: high-dose methotrexate for PCNSL causes severe mucositis and hepatotoxicity, and chronic dexamethasone raises peptic-ulcer risk.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Prolonged steroids waste muscle and bone: the chronic dexamethasone used to control PCNSL oedema causes proximal steroid myopathy, osteoporosis and avascular necrosis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its key drug can block the kidney: the high-dose methotrexate central to PCNSL treatment can precipitate in the renal tubules causing acute kidney injury, needing hydration, alkalinisation and leucovorin rescue.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Drug and immunosuppression hit the lungs: methotrexate can cause pneumonitis, and the profound immunosuppression of PCNSL and its therapy invites Pneumocystis and fungal pneumonia.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its therapy assaults skin and mucosa: high-dose methotrexate causes severe mucositis and skin toxicity, and the dexamethasone used for oedema thins and bruises the skin.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Treatment and immobility strain the circulation: high-dose methotrexate regimens, corticosteroids and the high venous-thrombosis risk of CNS lymphoma all burden the cardiovascular system.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Targeted agents enter the brain: BTK inhibitors like ibrutinib, immunomodulators and rituximab supplement high-dose methotrexate against primary CNS lymphoma.
- `connects-to` → **[HIV-1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — Immunodeficiency invites it: in advanced HIV infection, EBV-driven primary CNS lymphoma emerges, historically an AIDS-defining brain tumour distinguished from toxoplasmosis.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — High-dose methotrexate is the backbone: HD-MTX-based chemoimmunotherapy, which crosses the blood-brain barrier, is the curative-intent treatment for primary CNS lymphoma, often consolidated with autologous transplant.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Cell therapy crosses into the brain: CD19 CAR-T cells produce responses in relapsed primary CNS lymphoma, showing engineered T cells can reach and clear disease behind the blood-brain barrier.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Uniquely PD-L1-rich among lymphomas: 9p24.1 alterations raise PD-L1 in primary CNS lymphoma, and PD-1 inhibitors such as nivolumab have shown activity in relapsed disease.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Opposite ends of the B-cell spectrum: primary CNS lymphoma is an aggressive ABC-type diffuse large B-cell lymphoma (MYD88/CD79B), whereas follicular lymphoma is an indolent germinal-centre-derived B-cell lymphoma—same lineage, opposite tempo and biology.
- `connects-to` → **[CLL](../cll/README.md)** — A shared dependence on BTK: primary CNS lymphoma's MYD88-driven NF-κB and CLL's B-cell-receptor signalling both run through Bruton tyrosine kinase, so BTK inhibitors like ibrutinib are active against both.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Immunosuppression can seed it: methotrexate and other immunosuppressants used in rheumatoid arthritis can trigger EBV-driven lymphoproliferative disease, including CNS lymphoma that may regress when the drug is withdrawn.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Neurotoxicity and memory: primary CNS lymphoma and the high-dose methotrexate and whole-brain radiation used to treat it injure the hippocampus, causing the cognitive decline that especially burdens older survivors.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Angiocentric infiltration: PCNSL grows in perivascular cuffs deep in the brain, diffusely infiltrating white-matter tracts rather than forming a resectable mass—why diagnosis is by biopsy, not surgery.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — A steroid-responsive mimic: PCNSL can transiently shrink with corticosteroids, masquerading as an inflammatory or demyelinating lesion like multiple sclerosis and delaying diagnosis if steroids precede biopsy.
- `connects-to` → **[Cryptococcus neoformans](../../../02-pathogen/03-fungi/cryptococcus-neoformans/README.md)** — An infectious mass mimic: in an HIV or immunosuppressed patient, a brain lesion's differential includes cryptococcoma alongside toxoplasmosis and PCNSL, so biopsy and CSF studies are needed to tell tumour from infection.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Iatrogenic lymphoma: long-term immunosuppression for autoimmune diseases such as lupus predisposes to EBV-driven CNS lymphoproliferative disease, an immunodeficiency-associated route to PCNSL like that seen with methotrexate.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Angiocentric growth: PCNSL characteristically grows in perivascular cuffs around cerebral vessels, infiltrating the arterial wall and Virchow-Robin spaces, a pattern that helps distinguish it from glioma at biopsy.
- `connects-to` → **[FOXO1](../../03-molecular/foxo1/README.md)** — Recurrent driver: FOXO1 mutations recur in primary CNS lymphoma, dysregulating this transcription factor in the malignant germinal-centre-derived B cells.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Cell-cycle brake lost: CDKN2A deletion is frequent in PCNSL, removing a key cell-cycle checkpoint and conferring a poorer prognosis.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Germinal-centre epigenetics: EZH2 enforces the proliferative, anti-differentiation chromatin programme of the germinal-centre B cells from which PCNSL arises.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — Cell-cycle drive: with CDKN2A loss frequent in PCNSL, cyclin D-CDK4/6 activity propels the lymphoma cells through the G1 checkpoint.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — CNS angiogenesis: VEGF drives the angiogenesis of these brain lymphomas, whose angiocentric growth pattern wraps proliferating B cells around cerebral vessels.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Tumour hypoxia: HIF-1α stabilised in the hypoxic CNS lymphoma drives the metabolic adaptation and angiogenesis that support its growth within the brain.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Autocrine IL-6 in PCNSL signals through JAK1/2-STAT3 to sustain the malignant B cells, a cytokine survival loop layered on the MYD88-driven NF-κB activation that defines this ABC-type CNS lymphoma.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Constitutive B-cell-receptor and MYD88 signaling converge on PI3K-AKT-mTOR in PCNSL, driving the protein synthesis and proliferation that fuel its rapid intracerebral growth and underpin trials of mTOR-pathway inhibitors.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — PCNSL frequently deletes the 6p21 HLA region and loses MHC class II expression, blunting antigen presentation so the tumor evades immune surveillance within the already immune-privileged central nervous system.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — High-dose methotrexate that crosses the blood-brain barrier kills PCNSL cells through caspase-3-mediated apoptosis, and the BCL-2-driven apoptotic resistance of this lymphoma underlies the relapses that follow initial response.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — PCNSL cells secrete IL-10, and an elevated cerebrospinal-fluid IL-10 level (and high IL-10/IL-6 ratio) is a diagnostic and prognostic marker that also serves as autocrine survival signaling for the tumor.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PCNSL frequently deletes PTEN on 9p alongside CDKN2A, releasing the brake on PI3K-AKT-mTOR signaling that drives proliferation and supports the dependence on the same pathway targeted by mTOR and PI3K inhibitors.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — With PTEN deleted, PIK3CA-driven PI3K signaling sustains the constitutive AKT-mTOR activity of PCNSL, working alongside the BTK/MYD88-NF-κB axis and offering a second targetable node for PI3K inhibitors in this aggressive CNS lymphoma.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Interferon-γ from the reactive T-cell infiltrate, together with 9p24.1 copy gains, drives PD-L1 expression on PCNSL cells, creating the immune-checkpoint vulnerability that motivates PD-1 blockade in this immune-privileged tumor.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — STAT1 is the transcription factor relaying interferon-γ signals to induce PD-L1 and antigen-presentation genes in PCNSL, the JAK-STAT arm (with the JAK2 of 9p24.1) shaping its immunosuppressive microenvironment.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — CDKN2A loss (mapped) frees the cyclin-D1-CDK4/6 axis to release E2F1, driving the high proliferative rate of primary CNS lymphoma.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 alterations occur in primary CNS lymphoma and are associated with a poorer response to high-dose-methotrexate-based therapy.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — The cytokine BAFF supports the survival of the malignant B cells of PCNSL, reinforcing the MYD88-CD79B-BTK-NF-κB signaling (mapped) on which they depend.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — The RB1-E2F checkpoint (CDKN2A, cyclin-D1 and E2F1 already mapped) restrains proliferation, and its dysregulation contributes to the aggressive growth of primary CNS lymphoma.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Chronic-active B-cell-receptor signaling activates RAS-ERK alongside the MYD88-NF-κB axis (already mapped) to drive proliferation in primary CNS lymphoma.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 inactivation (p53 already mapped) contributes to the apoptosis evasion of primary CNS lymphoma.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the immunosuppressive CNS microenvironment and survival of primary CNS lymphoma.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β within the immune-privileged CNS shapes the immunosuppressive microenvironment that shelters primary CNS lymphoma.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING influences the immune microenvironment and immunotherapy responsiveness of primary CNS lymphoma.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) normally restrains B-cell proliferation, a brake overridden in the lymphomagenesis of primary CNS lymphoma.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors, restrained by the BCR-PI3K-AKT signaling of the MYD88/CD79B-mutant clone, modulate the survival of primary CNS lymphoma.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1, CDKN2A and RB1 already mapped) drives the cell-cycle progression of primary CNS lymphoma.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the MYC stability and NF-κB-driven survival signaling of primary CNS lymphoma.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance targets the immune-privileged-site primary CNS lymphoma.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the neuroinflammatory microenvironment of primary CNS lymphoma.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LYN) kinase signaling downstream of the chronically active B-cell receptor supports the survival of primary CNS lymphoma cells.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of primary CNS lymphoma.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and chemoresistance of primary CNS lymphoma cells.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of primary CNS lymphoma.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the CNS homing of primary CNS lymphoma.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of primary CNS lymphoma.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor microenvironment of primary CNS lymphoma.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory tumor-immune microenvironment of primary CNS lymphoma.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory tumor microenvironment of primary CNS lymphoma.
- `connects-to` → **[LMP1](../../03-molecular/lmp1/README.md)** — EBV-driven variant: in immunocompromised hosts primary CNS lymphoma is typically EBV-positive, and the viral oncoprotein LMP1 mimics constitutive CD40 signalling to activate NF-kB (already mapped), driving the B-cell transformation of this immunodeficiency-associated subtype.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4/STAT6 survival axis: an IL-4 signature expressed by tumour vasculature in primary CNS lymphoma engages STAT6 to support malignant B-cell survival and correlates with outcome, a microenvironmental dependency beyond the intrinsic MYD88/BTK signalling.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — Inflammatory milieu: TNF-alpha is an NF-kB-driven cytokine (NF-kB already mapped) enriched in the primary CNS lymphoma microenvironment, sustaining the reactive perivascular inflammation and blood-brain-barrier disruption that accompany the tumour.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — CNS-directed CAR-T: IL-2-driven T-cell expansion powers the CD19 CAR-T therapy (perforin already mapped) that can cross into the central nervous system and produce responses in relapsed primary CNS lymphoma.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Checkpoint blockade: primary CNS lymphoma, which often amplifies PD-L1 (PD-1 already mapped), can respond to checkpoint inhibitors, and CTLA-4 blockade is explored in combination to strengthen the anti-tumour T-cell response.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Treatment myelosuppression: the high-dose methotrexate-based chemotherapy central to primary CNS lymphoma is myelosuppressive, lowering haemoglobin and requiring transfusion and growth-factor support during treatment.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: initiating chemotherapy for bulky primary CNS lymphoma can lyse the tumour rapidly, releasing purines that xanthine oxidase converts to uric acid, a tumour-lysis risk managed with allopurinol and hydration.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Tumour-lysis acidosis: the rapid lysis of primary CNS lymphoma by chemotherapy releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped), part of its acute metabolic risk.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Tumour vasculature: nitric oxide with VEGF (already mapped) regulates the vascular tone and angiogenesis of primary CNS lymphoma, part of the microenvironment behind its characteristic angiocentric growth around cerebral vessels.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the tumour-associated microglia and the cyclooxygenase pathway contribute to the neuroinflammation (IL-6 and IL-1 already mapped) of the primary CNS lymphoma microenvironment.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chemotherapy anaemia: the high-dose methotrexate-based chemotherapy of primary CNS lymphoma is myelosuppressive, causing anaemia (haemoglobin already mapped) that can require transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune milieu: IL-13, with IL-4 (already mapped), reflects the type-2 cytokine arm of the immune microenvironment of primary CNS lymphoma, part of the cytokine milieu shaping the tumour.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and adds an anaemia of chronic disease to the high-dose-methotrexate anaemia (iron already mapped) of primary CNS lymphoma.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic and cachexia: the corticosteroids (cortisol already mapped) and the disease disturb leptin and energy balance, part of the metabolic dimension and the cachexia of the often-elderly primary-CNS-lymphoma patient.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate CNS immunity: type-I interferon signalling is part of the innate antiviral immunity of the immune-privileged CNS, relevant to the EBV-driven (LMP1 already mapped) primary CNS lymphoma of the immunosuppressed.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic-cachexia adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic-cachexia axis of the often-elderly primary CNS lymphoma patient.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic milieu of primary CNS lymphoma.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate CNS surveillance: the natural killer cells (perforin already mapped) provide the innate cytotoxic surveillance of the CNS, and the CAR-NK cell therapy is explored for the immune-privileged primary CNS lymphoma.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) anti-lymphoma response of the immune-privileged primary CNS lymphoma microenvironment.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm of the immune microenvironment of primary CNS lymphoma.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune microenvironment of primary CNS lymphoma.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 antibody arm: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the type-2 humoral dimension of the immune microenvironment of primary CNS lymphoma.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell infiltrate: the mast cells are part of the tumour immune microenvironment infiltrate of primary CNS lymphoma, contributing to the type-2 and pro-angiogenic (VEGF already mapped) milieu.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin arm: TSLP, an epithelial/stromal alarmin, is part of the type-2 (IL-4 and IL-13 already mapped) dimension of the immune microenvironment of primary CNS lymphoma.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells of the reactive infiltrate are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immune microenvironment of primary CNS lymphoma.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Type-2 cytokine: IL-31, with TSLP (already mapped), extends the type-2 (IL-4 and IL-13 already mapped) dimension of the immune microenvironment of primary CNS lymphoma.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 remodelling: periostin, downstream of the type-2 (IL-4 and IL-13 already mapped) cytokines, is part of the type-2 stromal-remodelling dimension of the primary-CNS-lymphoma microenvironment.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Rituximab CDC: the complement C3 activation is the initiating step of the complement-dependent cytotoxicity by which the anti-CD20 (already mapped) rituximab kills the primary-CNS-lymphoma B cells (already mapped).
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 (with C3 already mapped) is the effector of the membrane-attack complex of the rituximab complement-dependent cytotoxicity against primary CNS lymphoma.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the microglial (already mapped) and myeloid inflammation of the primary-CNS-lymphoma microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — BBB-permeability therapy: bradykinin B2-receptor agonists (e.g. labradimil) have been used experimentally to transiently open the blood-brain barrier, enhancing the CNS delivery of the methotrexate that is central to primary-CNS-lymphoma treatment.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway brake: C1-esterase inhibitor regulates the classical complement pathway activated by the anti-CD20 (already mapped) rituximab in the CSF compartment, modulating complement-dependent cytotoxicity in primary CNS lymphoma.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Neuroinflammatory mediator: histamine, released by the CNS-infiltrating mast cells and tumour-associated macrophages (microglia already mapped) of primary CNS lymphoma, promotes the neuroinflammatory microenvironment and angiogenesis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Chemotherapy anaemia: erythropoietin corrects the high-dose methotrexate- and rituximab-induced marrow suppression anaemia of primary CNS lymphoma; EPOR expression in the CNS lymphoma B cells has also been reported.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion in CSF: primary CNS lymphoma cells recruit factor H to limit the C3/C5/C5aR1 (all already mapped) complement-dependent cytotoxicity of rituximab within the immune-privileged CNS compartment.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-immune axis: melatonin modulates CNS immune surveillance (microglia already mapped), regulating natural killer cell activity (already mapped) and the B-cell proliferation underlying the immune dysregulation of primary CNS lymphoma.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — PCNSL androgen axis: testosterone via androgen receptor modulates CNS B-cell proliferation and the blood-brain barrier permeability governing PCNSL compartmentalisation, intersecting the BCR (already mapped) and PI3K/AKT (already mapped) signalling pathways.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — PCNSL serotonin: serotonin modulates CNS immune microenvironment and B-cell proliferation underlying primary CNS lymphoma, and serotonin receptor signalling on CNS B-cell lymphoma cells intersects the BCR (already mapped) and PI3K/AKT (already mapped) pathways.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — PCNSL prolactin: prolactin promotes B-cell survival and class-switching via JAK2/STAT5 (already mapped) signalling, amplifying the malignant CNS B-cell proliferation and CXCR4 (already mapped)-mediated CNS compartmentalisation of primary CNS lymphoma.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PCNSL oxytocin: oxytocin modulates CNS immune surveillance and blood-brain barrier integrity, intersecting the neuroinflammatory microenvironment (microglia already mapped) and B-cell proliferation (BCR already mapped) underlying primary CNS lymphoma compartmentalisation.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PCNSL vasopressin: vasopressin via AVPR modulates blood-brain barrier permeability and CNS fluid homeostasis, influencing the immune-privileged compartment that permits primary CNS lymphoma escape from systemic immune surveillance (NF-κB already mapped).
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — PCNSL selenium: selenium-dependent glutathione peroxidase (GPX) quenches reactive-oxygen-species driving genomic instability and lymphoma-promoting NF-κB (already mapped) signalling in the malignant B cells of primary CNS lymphoma.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PCNSL iodine: iodine-dependent thyroid hormones regulate macrophage (already mapped) and T-cytotoxic (already mapped) immune activation; iodine deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-tumour cascade of primary CNS lymphoma.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — PCNSL sodium: excess sodium promotes macrophage (already mapped) and microglia (already mapped) pro-inflammatory activation; sodium-induced NF-κB (already mapped) and IL-6 (already mapped) skewing amplifies the T-cytotoxic (already mapped) CNS lymphoma cascade.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — PCNSL magnesium: magnesium, as cofactor of DNA repair enzymes in neurons (already mapped) and macrophages (already mapped), supports brain-immune homeostasis; magnesium deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) cascade of PCNSL.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — PCNSL copper: copper-dependent enzymes in macrophages (already mapped) and T-cytotoxic cells (already mapped) sustain CNS tumour-immune balance; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in the primary CNS lymphoma microenvironment.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — PCNSL phosphorus: phosphorus-dependent ATP in macrophages (already mapped) and T-cytotoxic cells (already mapped) drives lymphoma-infiltrating immune responses; phosphorus dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in PCNSL.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — PCNSL zinc: zinc co-factors in macrophage (already mapped) and T-cytotoxic (already mapped) immune effector functions; zinc depletion exacerbates NF-κB (already mapped) and IL-6 (already mapped) pro-tumour signalling and microglia (already mapped) activation in PCNSL.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — PCNSL carbon: carbon as backbone of NF-κB (already mapped) and BCL-2 proteins in lymphoma cells and microglia (already mapped) sustains tumour survival signalling; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade in PCNSL.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — PCNSL chloride: chloride channels in microglia (already mapped) and lymphoma cells modulate cell-volume and invasive potential in the CNS; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) inflammatory cascade of PCNSL.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — PCNSL hydrogen: hydrogen, via redox homeostasis in microglia (already mapped) and lymphoma cells, supports BCL-2-mediated survival; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) oxidative cascade of PCNSL.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — PCNSL nitrogen: nitrogen in amino-acid scaffold of BCL-2 (already mapped) and NF-κB (already mapped) proteins in lymphoma cells sustains oncogenic CNS signalling; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of PCNSL.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — PCNSL oxygen: oxygen, via mitochondrial respiration in microglia (already mapped) and lymphoma cells, sustains CNS energy homeostasis; oxygen depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of PCNSL.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — PCNSL sulfur: sulfur in cysteine residues of BCL-2 (already mapped) and NF-κB (already mapped) proteins in lymphoma cells sustains thiol-redox balance; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) tumour cascade of PCNSL.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — PCNSL glp-1: GLP-1 from macrophages (already mapped) and microglia (already mapped) modulates metabolic-inflammatory CNS tumour tone; glp-1 dysfunction amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PCNSL.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — PCNSL angiotensin-ii: angiotensin-II from macrophages (already mapped) and microglia (already mapped) drives CNS tumour angiogenesis; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) tumour cascade of PCNSL.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — PCNSL wnt-beta-catenin: WNT/β-catenin on lymphoma cells (already mapped) and microglia (already mapped) drives CNS tumour invasion; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of PCNSL.

[^bromberg-2019-hovon105]: Bromberg JE, Issa S, Bakunina K, et al. Rituximab in patients with primary CNS lymphoma (HOVON 105/ALLG NHL 24): a randomised, open-label, phase 3 intergroup study. *Lancet Oncol.* 2019;20(2):216-228. [doi:10.1016/S1470-2045(18)30747-2](https://doi.org/10.1016/S1470-2045(18)30747-2) · [PubMed 30528440](https://pubmed.ncbi.nlm.nih.gov/30528440/)
[^grommes-2017-ibrutinib-pcnsl]: Grommes C, Pastore A, Palaskas N, et al. Ibrutinib unmasks critical role of Bruton tyrosine kinase in primary CNS lymphoma. *Cancer Cell.* 2017;31(6):833-843. [doi:10.1016/j.ccell.2017.04.012](https://doi.org/10.1016/j.ccell.2017.04.012) · [PubMed 28552327](https://pubmed.ncbi.nlm.nih.gov/28552327/)
