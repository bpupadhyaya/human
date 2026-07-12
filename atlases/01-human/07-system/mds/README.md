---
schema: human-scale-entry/v1
id: mds
name: Myelodysplastic Syndromes
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Myelodysplastic syndromes are clonal hematopoietic disorders with cytopenias and dysplasia; SF3B1, DNMT3A, TET2, and TP53 mutations define subtypes. Azacitidine+venetoclax is higher-risk standard; luspatercept approved for SF3B1-mutant MDS; allo-SCT is the only cure."
aliases: ["MDS", "myelodysplastic syndrome", "myelodysplasia", "MDS-EB", "refractory anemia", "IPSS-R", "azacitidine MDS", "hypomethylating agent MDS", "SF3B1 MDS", "MDS-MPN"]
sources:
  - id: fenaux-2009-aza001
    type: peer-reviewed
    cite: "Fenaux P, Mufti GJ, Hellstrom-Lindberg E, et al. Efficacy of azacitidine compared with conventional care regimens in patients with higher-risk myelodysplastic syndromes: a randomised open-label phase III study. Lancet Oncol. 2009;10(3):223-232."
    doi: "10.1016/S1470-2045(09)70003-8"
    pmid: "19230772"
    url: "https://doi.org/10.1016/S1470-2045(09)70003-8"
  - id: fenaux-2020-medalist
    type: peer-reviewed
    cite: "Fenaux P, Platzbecker U, Mufti GJ, et al. Luspatercept in patients with lower-risk myelodysplastic syndromes. N Engl J Med. 2020;382(2):140-151."
    doi: "10.1056/NEJMoa1908892"
    pmid: "31914241"
    url: "https://doi.org/10.1056/NEJMoa1908892"
cross_links:
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A mutations in ~20% of MDS and ~40% of CHIP; DNMT3A is the most commonly mutated gene in clonal hematopoiesis; CHIP-to-MDS progression involves co-mutation of DNMT3A with TET2, ASXL1, or splicing factors (SF3B1, SRSF2); DNMT3A R882H is the dominant hotspot."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "EZH2 loss-of-function mutations in ~6% of MDS; EZH2 and DNMT3A/TET2 mutations co-occur in MDS, compounding epigenetic deregulation; EZH2 deletion/mutation is an adverse prognostic factor in MDS; tazemetostat is not currently approved for MDS."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 biallelic mutations define ultra-high risk MDS (WHO 2022: MDS-biTP53); monosomal karyotype; median OS <1 year; venetoclax+azacitidine has limited activity in TP53-mutant MDS; eprenetapopt (p53 reactivator)+azacitidine showed CR ~35% in Phase 2."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH1/2 mutations in ~10% of MDS (IDH1 ~5%, IDH2 ~5%); 2-HG → TET2 inhibition → hypermethylation amplifies DNMT3A epigenetic dysfunction; ivosidenib (IDH1) and enasidenib (IDH2) active in IDH-mutant MDS; FDA-approved in AML, under investigation in MDS."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Activin A/B → ActRIIB on erythroid progenitors → SMAD2/3 → suppression of late erythroid maturation → ineffective erythropoiesis in MDS and beta-thalassemia; luspatercept (MEDALIST trial: 38% transfusion independence vs. 13% placebo) traps activin A/B to restore erythropoiesis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Myelodysplastic syndromes are clonal disorders defined by marrow dysplasia (≥10% in a lineage), ring sideroblasts, and rising blasts; the signature paradox is a hypercellular marrow yielding peripheral cytopenias, because dysplastic progenitors die in the marrow before maturing."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "MDS is a pre-leukemic clonal disorder on a continuum with AML: rising marrow blasts (≥20% defines AML) and new driver mutations mark transformation, ranging from ~10%/year in low-risk to ~50% over 2 years in MDS-EB2; shared biology drives shared therapy (azacitidine, venetoclax)."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Ineffective erythropoiesis is the core lesion of lower-risk MDS — erythroid progenitors mature abnormally and die before producing red cells, causing transfusion-dependent anemia; luspatercept traps activin/GDF11 to release late erythroid maturation."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "MDS and myelofibrosis are overlapping clonal marrow disorders: MDS-with-fibrosis and MDS/MPN overlap (e.g. CMML) blur the boundary, both share mutations (ASXL1, SRSF2, TP53), both cause cytopenias, and both can transform to AML; marrow fibrosis in MDS is adverse."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Hypoplastic MDS overlaps with aplastic anemia — both present with pancytopenia and a hypocellular marrow, and both can respond to immunosuppression (ATG/ciclosporin); a PNH clone or MDS-defining cytogenetics/mutations help distinguish clonal MDS from immune aplastic anemia."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "MDS produces dysplastic, hypogranular neutrophils with hyposegmented (pseudo-Pelger-Huët) nuclei and impaired function; neutropenia plus qualitative defects make infection a leading cause of death; the absolute neutrophil count feeds IPSS-R risk scoring and antibiotic planning."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "MDS and CMML are overlapping clonal marrow disorders divided by the WHO: pure MDS is dysplasia with cytopenias and no proliferation, while CMML (an MDS/MPN overlap) adds persistent monocytosis—but both share mutations (TET2, SRSF2, ASXL1) and can progress to AML."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ionizing radiation is an established cause of MDS: atomic-bomb survivors and patients given radiotherapy develop therapy-related MDS years later, typically with -7/-5 cytogenetics and TP53 mutations and a poor prognosis—radiation injuring the hematopoietic stem cell."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thrombocytopenia from dysplastic megakaryopoiesis is a key MDS cytopenia: the clone produces few and abnormal platelets, causing bleeding, while the del(5q) MDS subtype paradoxically runs high platelets and responds dramatically to lenalidomide."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "MDS and myeloproliferative neoplasms are overlapping clonal stem-cell disorders: MDS shows dysplasia and cytopenias, MPNs show overproduction, and the MDS/MPN-overlap category blends both—different faces of mutated hematopoietic stem cells."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "MDS is part of the Li-Fraumeni and inherited marrow-failure spectrum: germline TP53 loss predisposes to MDS and therapy-related MDS/AML, and TP53-mutant MDS is high-risk and treatment-resistant—linking a hereditary cancer syndrome to clonal marrow disease."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "MDS and iron-deficiency anemia are opposite anemias: iron deficiency is microcytic from low iron, while MDS is a macrocytic dysplastic marrow-failure anemia with normal/high iron—so unexplained macrocytic anemia in older adults warrants marrow study."
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "SF3B1 mutation defines a favorable MDS subtype: this splicing-factor gene, when mutated, produces ring sideroblasts and an indolent anemia—now its own WHO entity, often responsive to luspatercept and carrying a comparatively good prognosis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietin underlies both the anemia and the treatment of lower-risk MDS: ineffective marrow erythropoiesis fails to answer EPO, so erythropoiesis-stimulating agents are first-line for the anemia when endogenous EPO levels are low."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "MDS has an immune dimension: a subset, especially hypoplastic MDS, involves T-cell-mediated marrow suppression and responds to immunosuppression, while inflammatory signaling in the marrow niche helps drive the ineffective blood production."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Transfusion-dependent MDS overloads the liver with iron: repeated red-cell transfusions deposit excess iron in the liver (and heart), causing secondary hemochromatosis, so iron chelation is part of long-term care for chronically transfused patients."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "MDS overlap syndromes enlarge the spleen: in CMML and MDS/MPN forms, abnormal myeloid cells and extramedullary hematopoiesis swell the spleen, causing fullness and worsening cytopenias—a feature that distinguishes them from pure dysplastic MDS."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "MDS is a key cause of unexplained anemia in older adults: unlike anemia of chronic disease, its low counts stem from a clonal dysplastic marrow making defective cells, so a macrocytic anemia not explained by B12, folate, or inflammation warrants a marrow biopsy."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "MDS patients drown in iron from transfusions: chronic red-cell transfusions for the anemia deposit iron in heart, liver and endocrine organs, so iron chelation is needed to prevent organ damage in lower-risk patients who live long enough."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "MDS arises from mutated blood stem cells, often via TET2: this epigenetic regulator is one of the recurrent clonal-hematopoiesis mutations that, accumulating with age, derange marrow maturation—and that hypomethylating drugs like azacitidine target."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Some MDS is driven by an immune attack from cytotoxic T cells: in hypoplastic MDS overlapping aplastic anemia, T cells suppress the marrow, so these patients can respond to immunosuppression rather than chemotherapy."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "MDS marrow cells die by pyroptosis via the NLRP3 inflammasome: chronic inflammasome activation makes the dysplastic precursors self-destruct inflammatorily, so the bone marrow is packed yet the blood counts are low—ineffective hematopoiesis."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "MDS's cytopenias come from excess apoptosis: caspase-driven death of marrow progenitors means cells are made but die before maturing, explaining the paradox of a hypercellular marrow with too few blood cells reaching circulation."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "MDS festers in an inflammatory marrow run by macrophages: myeloid cells pour out alarmins (S100A8/A9) and cytokines that fire the inflammasome and worsen the ineffective hematopoiesis—an inflammatory niche now itself a treatment target."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Years of MDS transfusions can poison the heart: each unit of red cells delivers iron the body cannot excrete, and the overload deposits in heart muscle, causing an iron cardiomyopathy and arrhythmias that drive the need for chelation."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "MDS starves tissues of oxygen: failed marrow makes too few red cells, so chronic anemia leaves the body short of oxygen, producing the fatigue and breathlessness that dominate the disease and force transfusion dependence."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "MDS warps the marrow's immune balance: in early disease autoimmune T cells attack progenitors (why immunosuppression can help), while advancing disease expands regulatory T cells that shield the malignant clone from immune attack."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper deficiency mimics MDS: too little copper—often from excess zinc or gut surgery—causes a reversible myelodysplasia with anemia, neutropenia and ringed sideroblasts, an imitator to exclude before diagnosis."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "MDS can announce itself on the skin: neutrophilic dermatoses like Sweet syndrome may herald or accompany it, a paraneoplastic clue that prompts a look at the marrow."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Some MDS scars the marrow: reticulin fibrosis worsens the cytopenias and carries a poorer prognosis, blurring the boundary with primary myelofibrosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals MDS's iron-clogged cells: ringed sideroblasts pack iron into mitochondria circling the red-cell nucleus, while dysplastic granulocytes and giant platelets betray a marrow producing defective blood."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Too much zinc can fake MDS: excess zinc drives out copper, and the resulting copper deficiency causes a reversible dysplasia and cytopenias that mimic the marrow disease — a mimic worth excluding before the real diagnosis."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Years of transfusions overload the liver: as MDS patients receive red cells for their anemia, iron with nowhere to go accumulates in hepatocytes, driving the fibrosis that makes iron chelation part of long-term care."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Transfusional iron poisons the pancreas: deposited in the islet cells over years of red-cell support, the excess iron can damage insulin production into a secondary diabetes — one of the endocrine costs of treating MDS anemia."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "MDS keeps strange autoimmune company: it associates with vasculitis, Sweet's syndrome, and the VEXAS syndrome, and some patients' cytopenias are immune-driven and respond to immunosuppression — autoimmunity riding alongside the clonal marrow."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lungs are a frequent battleground: deep neutropenia leaves MDS patients prone to pneumonia and fungal infection, and the hypomethylating drug azacitidine can itself rarely inflame the lungs into a pneumonitis."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "Metabolic mutations open a targeted door: IDH1 and IDH2 mutations in a subset of MDS make the oncometabolite 2-hydroxyglutarate, and IDH inhibitors that switch them off can restore healthy blood-cell maturation."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Transfusional iron overload silts up the endocrine glands: the relentless transfusions MDS often needs deposit iron in the thyroid and other glands, causing hypothyroidism and the endocrinopathies that iron chelation aims to prevent."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "A transplant means weighing fertility: the conditioning chemotherapy and radiation before an allogeneic stem-cell transplant can sterilize, so fertility preservation is discussed with younger MDS patients before the curative attempt."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "RUNX1 sits at the heart of MDS biology: somatic mutations of this master hematopoietic transcription factor drive dysplasia and progression to AML, and inherited RUNX1 defects (familial platelet disorder) predispose to MDS decades early."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "MDS and PNH are overlapping marrow-failure clones: small PNH clones often lurk in hypoplastic MDS, and the shared immune-mediated attack on the marrow blurs the line between clonal escape and aplasia."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Immune surveillance falters in MDS: natural killer cells that should cull the dysplastic clone are reduced and functionally impaired, helping the abnormal stem cells expand and dimming the marrow's own defense."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Excess TGF-β strangles red-cell maturation: overactive TGF-β/SMAD signaling blocks late erythroid maturation in MDS, the ineffective erythropoiesis that the trap drug luspatercept relieves to lift the anemia."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "The soil can drive the disease, not just the seed: a dysfunctional bone-marrow niche — including its osteoblast and mesenchymal cells — fosters and shelters the dysplastic clone, making the microenvironment part of MDS pathogenesis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic anemia and iron overload tax the heart: years of low hemoglobin force a high-output strain while transfusional iron deposits in the myocardium, so cardiovascular complications are a major cause of death in MDS."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation poisons the marrow's own output: NF-κB signaling is overactive in MDS progenitors, priming the NLRP3 inflammasome and pyroptotic cell death that produce the ineffective hematopoiesis and cytopenias of the disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Clonal immune signaling shadows the disease: STAT3-activating mutations in associated large granular lymphocyte clones, and STAT3 signaling in the marrow, contribute to the immune dysregulation and cytopenias seen in MDS."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Empty defenses invite fatal infection: the neutropenia of MDS, deepened by hypomethylating-agent therapy, leaves patients prone to overwhelming infection, and sepsis is among the commonest causes of death."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Prolonged neutropenia opens the lung to mold: the deep, sustained neutropenia of MDS and its therapy lets inhaled Aspergillus invade as angioinvasive pulmonary aspergillosis, a feared infectious complication."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Failing neutrophils let the yeast bloodstream: neutropenia and disrupted mucosa in MDS allow Candida to translocate into the blood, causing invasive candidiasis in these immunocompromised patients."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Transfusions rust the heart: lifelong red-cell transfusions for MDS anemia deposit iron in the myocardium, and this siderosis — atop the strain of chronic anemia — can drive a cardiomyopathy and heart failure."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its hypomethylating therapy deepens immune suppression: azacitidine and decitabine for MDS add to the disease's own neutropenia and T-cell dysfunction, raising the risk of Pneumocystis pneumonia."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Lenalidomide for low-risk MDS clots the veins: the immunomodulatory drug used for del(5q) MDS carries a recognized prothrombotic signal, raising venous thromboembolism risk during treatment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic, transfusion-dependent cancer weighs on mood: the fatigue, frequent hospital visits, poor prognosis and looming leukemic transformation of MDS, mostly in older patients, contribute to depression."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Transfusion iron overload poisons the glands: years of red-cell transfusions in MDS deposit iron in the pancreas, pituitary and thyroid, causing diabetes, hypogonadism and other endocrinopathies."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its therapy reawakens shingles: the hypomethylating agents, immunosuppression and stem-cell transplant used in MDS deplete T-cell immunity, allowing latent varicella-zoster to reactivate."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A transfusion-dependent pre-leukaemia breeds worry: the cytopenias, transfusion dependence and ever-present threat of progression to AML in MDS foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It erupts on the skin: MDS is a classic trigger of Sweet syndrome, a neutrophilic dermatosis of tender plaques, and other autoinflammatory eruptions, with leukaemia cutis if it transforms to AML."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It overlaps systemic autoinflammation: MDS associates with VEXAS syndrome and relapsing polychondritis, producing inflammatory arthritis, chondritis and other rheumatic features alongside the cytopenias."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Years of transfusion poison the liver: repeated red-cell transfusions in MDS deposit iron in hepatocytes, causing iron-overload liver injury that iron chelation aims to prevent."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Its low platelets and anaemia reach the brain: severe thrombocytopenia risks intracranial haemorrhage, and chronic anaemia causes fatigue and cognitive slowing."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Failing marrow exposes the lungs: neutropenia invites bacterial and invasive fungal pneumonia, and repeated transfusion can cause circulatory overload or lung injury."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its autoinflammation can swell the nodes and spleen: MDS-associated systemic inflammation, including VEXAS syndrome, can cause lymphadenopathy, and overlap forms bring splenomegaly."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Treatment and overload reach the kidney: hypomethylating chemotherapy plus the renal effects of anaemia and transfusional iron overload strain the kidney in MDS."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Tailored drugs match its biology: hypomethylating agents (azacitidine, decitabine), lenalidomide for del(5q) MDS and luspatercept for anaemia are mainstays beyond supportive transfusion."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Transplant reawakens latent virus: many MDS patients undergo allogeneic stem-cell transplant, after which cytomegalovirus and other herpesviruses reactivate under immunosuppression."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Both consequence and treatment: therapy-related MDS arises years after alkylator or topoisomerase chemotherapy, while high-risk MDS itself is treated with intensive chemotherapy or hypomethylating agents en route to transplant."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Transfusional iron poisons the heart: chronic red-cell transfusions for MDS anaemia deposit iron in the myocardium, causing a siderotic cardiomyopathy and heart failure that iron chelation aims to prevent."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Shared transfusion dependence: like transfusion-dependent thalassemia, lower-risk MDS causes chronic anaemia needing regular transfusions and the iron overload they bring — one a marrow-failure clone, the other an inherited globin defect."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Transfusions overload the liver with iron: transfusion-dependent MDS accumulates iron in the hepatic lobule as haemosiderosis, adding liver iron toxicity to the cardiac loading that chelation therapy aims to prevent."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Its therapy can cause it: alkylating chemotherapy and autologous transplant for multiple myeloma raise the risk of therapy-related myelodysplastic syndrome years later, a feared late complication of cure."
  - target: 01-human/07-system/uveal-melanoma
    relation: connects-to
    note: "A shared splicing-factor mutation: SF3B1, which defines MDS with ring sideroblasts, is the same spliceosome gene mutated in a subset of uveal melanomas—one splicing defect across a marrow and an eye cancer."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Therapy-related MDS: the alkylators and radiation used to cure solid tumours such as breast cancer can damage the marrow's stem cells, seeding a secondary, poor-prognosis MDS that often progresses to AML."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Myeloid clone meets autoinflammation: MDS associates with systemic autoinflammatory and autoimmune syndromes—including VEXAS and vasculitis—where the mutant clone drives inflammation overlapping ANCA-associated disease."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Transfusional iron and the heart: years of red-cell transfusions for MDS deposit iron in the heart, injuring the myocardium and cardiac conduction system into cardiomyopathy and arrhythmia unless iron is chelated."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Clonal haematopoiesis and the artery: the TET2 and DNMT3A clones underlying MDS and CHIP spawn inflammatory monocytes that accelerate atherosclerosis, linking clonal marrow disease to heart attacks and strokes."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "A shared oncometabolite: IDH1/IDH2-mutant MDS and IDH-mutant glioma both generate 2-hydroxyglutarate that reprograms the epigenome and respond to the same IDH inhibitors, one drug class across blood and brain."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Iron-driven diabetes: transfusional iron overload in MDS deposits in the pancreas, impairing insulin secretion and causing a secondary 'bronze' diabetes alongside the cardiac and hepatic iron loading."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammaging marrow: TNF-α and other inflammatory cytokines drive the ineffective haematopoiesis and apoptosis that cause the cytopenias of myelodysplastic syndrome."
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "Transformation kinase: FLT3 mutations, though less common than in AML, appear in MDS and mark progression toward acute myeloid leukaemia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Clonal survival signalling: PI3K-AKT-mTOR signalling supports the survival of the dysplastic clone in myelodysplastic syndrome."
  - target: 01-human/03-molecular/srsf2
    relation: connects-to
    note: "Spliceosome mutation: SRSF2 is one of the recurrently mutated splicing factors in MDS, corrupting mRNA splicing across the genome and a hallmark driver alongside SF3B1 of the dysplastic clone."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Alarmin-driven dysplasia: S100A8/A9 released in the MDS marrow activates the NLRP3 inflammasome in progenitors, driving the chronic inflammation and pyroptotic cell death behind ineffective haematopoiesis."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Thrombopoiesis support: thrombopoietin-receptor agonists are used to raise platelet counts in the thrombocytopenia of lower-risk MDS, addressing the bleeding risk of ineffective megakaryopoiesis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Pyroptotic output: IL-1β matured by the NLRP3 inflammasome in MDS progenitors drives the inflammatory, pyroptotic cell death that produces the ineffective haematopoiesis and cytopenias central to the disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Iron overload: the ineffective erythropoiesis of MDS suppresses hepcidin, and chronic red-cell transfusion compounds the resulting parenchymal iron loading that damages heart and liver and is treated with chelation."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Immune-mediated suppression: in hypocellular MDS, T-cell IFN-γ suppresses haematopoietic progenitors, the rationale for immunosuppressive therapy that can restore counts in this subset overlapping with aplastic anaemia."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptotic therapy: higher-risk MDS evolving toward AML becomes dependent on anti-apoptotic BCL-2, the rationale for adding venetoclax to hypomethylating agents to push the dysplastic clone back into the apoptosis it has been evading."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 restraint: in TP53-wild-type MDS, high MDM2 holds p53 in check, so MDM2 inhibitors are a strategy to reactivate p53-driven apoptosis — distinct from the dismal-prognosis TP53-mutant MDS where the protein itself is lost."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Niche dependence: CXCL12 from marrow stromal cells anchors the MDS clone in its bone-marrow niche, and a disordered, inflammatory niche both supports the dysplastic clone and contributes to the ineffective haematopoiesis that defines the disease."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate-immune drive: chronic TLR4 activation by danger signals such as the S100A8/A9 already mapped fuels the NLRP3-inflammasome inflammation and pyroptotic cell death behind the ineffective haematopoiesis of MDS."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Ineffective erythropoiesis: TGF-β-SMAD signalling represses erythroid maturation in MDS, the mechanism that luspatercept — acting on the activin/SMAD pathway already mapped — relieves to improve transfusion-dependent anaemia."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory anaemia: IL-6 in the MDS marrow microenvironment drives hepcidin and the anaemia of inflammation while suppressing residual normal haematopoiesis, deepening the cytopenias of the disease."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate-immune ineffective haematopoiesis: chronic TLR-MyD88 signalling (TLR4 and S100A8/A9 mapped) in MDS stem and progenitor cells activates the NLRP3 inflammasome and pyroptosis, driving the ineffective haematopoiesis and cytopenias."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Clonal survival: PI3K-AKT-mTOR signalling (AKT mapped) supports the survival and growth advantage of the MDS clone over normal haematopoiesis."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Leukaemic progression: acquisition of RAS-pathway mutations marks the progression of MDS toward secondary acute myeloid leukaemia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT signalling (STAT3 mapped) is constitutively engaged in MDS progenitors and in MDS/MPN-overlap disease, a target of JAK inhibitor therapy."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN-restrained PI3K-AKT-mTOR signalling (AKT and mTOR mapped) promotes survival and proliferation of the dysplastic clone in MDS."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING amplifies the NLRP3-inflammasome-driven inflammatory bone-marrow milieu (NLRP3 mapped) characteristic of MDS."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports the survival and bone-marrow-niche adhesion of the dysplastic clone and contributes to the inflammatory marrow microenvironment of MDS."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune-mediated cytopenias and the inflammatory bone-marrow milieu of MDS."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "RAS-ERK signalling (KRAS already mapped) provides a proliferative input in the subset of MDS that progresses toward acute myeloid leukemia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate hematopoietic stem-cell quiescence and oxidative-stress handling, programs disrupted in myelodysplastic syndromes."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α shapes the hypoxic bone-marrow niche and the ineffective erythropoiesis of myelodysplastic syndromes."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β dysregulation contributes to the impaired differentiation and clonal advantage of myelodysplastic-syndrome progenitors."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxic immunosurveillance of the dysplastic clone shapes the immune-mediated cytopenias and clonal evolution of myelodysplastic syndrome."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Dysregulated CDK4/6-cyclin-D cell-cycle control contributes to the clonal proliferation and leukemic evolution of myelodysplastic syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the aberrant survival and inflammatory signaling of the myelodysplastic clone."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the clonal hematopoietic cells of myelodysplastic syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival and differentiation of the dysplastic hematopoietic progenitors of myelodysplastic syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic stem cells of myelodysplastic syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the bone-marrow niche and immune interactions of myelodysplastic syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of myelodysplastic syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of myelodysplastic syndrome."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory bone-marrow microenvironment of myelodysplastic syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory bone-marrow microenvironment of myelodysplastic syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell-mediated immune dysregulation (relevant to the immunosuppressive-therapy-responsive subset) of myelodysplastic syndrome."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune-mediated subset: hypoplastic MDS features T-cell-mediated suppression of haematopoiesis, where MHC class II-restricted autoreactive T cells attack progenitors, the basis for the response of this subset to immunosuppressive therapy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow angiogenesis: increased bone-marrow microvascular density and VEGF signalling accompany MDS and support the dysplastic clone, correlating with disease burden and progression toward acute myeloid leukaemia."
  - target: 01-human/03-molecular/calr
    relation: connects-to
    note: "MDS/MPN overlap: CALR mutations mark the overlap syndromes such as MDS/MPN with ring sideroblasts and thrombocytosis (SF3B1 already mapped), extending the clonal driver landscape beyond the classic MDS lesions."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Anaemia: anaemia is the commonest cytopenia of MDS, and the resulting fatigue and transfusion dependence dominate the illness, driving the use of erythropoiesis-stimulating agents and luspatercept (both already mapped) to raise haemoglobin."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Immunosuppressive therapy: hypoplastic MDS overlaps with aplastic anaemia (already mapped) and can respond to T-cell-directed immunosuppression, reflecting an IL-2-driven autoreactive attack on the marrow in a subset of patients."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Marrow angiogenesis: increased bone-marrow microvascular density in MDS is supported by angiopoietin-Tie2 signalling alongside VEGF (already mapped), part of the altered microenvironment that sustains the dysplastic clone."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Iron overload and sideroblasts: chronic transfusion and the SF3B1 ring-sideroblast phenotype (already mapped) disturb iron handling in MDS, and ferroportin, regulated by hepcidin (already mapped), governs the iron export relevant to the overload requiring chelation."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative dyspoiesis: the iron overload and inflammation of MDS generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress worsens the ineffective, apoptosis- and pyroptosis-prone (NLRP3 already mapped) haematopoiesis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune dysregulation: IL-10 among the cytokines of the inflammatory MDS marrow microenvironment (IFN-gamma, TNF and IL-6 already mapped) shapes the immune milieu that both suppresses normal haematopoiesis and is targeted by immunosuppression in a subset."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage niche: IL-4 polarises the marrow macrophages toward an M2 phenotype (IL-10 already mapped), part of the altered immune microenvironment of the dysplastic MDS marrow that shapes the ineffective haematopoiesis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipocyte crosstalk: the marrow adipocytes and their adipokine adiponectin engage in metabolic crosstalk with the dysplastic clone, the expanding marrow adipose tissue of MDS shaping the haematopoietic microenvironment."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine marrow signalling: leptin, with adiponectin (already mapped), from the marrow adipose tissue signals to the haematopoietic cells, part of the metabolic microenvironment influencing the dysplastic haematopoiesis of MDS."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 marrow inflammation: IL-13, with IL-4 (already mapped), supports the M2 marrow macrophages of the inflammatory (NLRP3 and S100A8/A9 already mapped) microenvironment that shapes the ineffective haematopoiesis of MDS."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk that shapes the dysplastic haematopoietic microenvironment of MDS."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc-copper balance: excess zinc induces copper (already mapped) deficiency, which causes a reversible MDS-like myelodysplasia, and zinc is itself required for normal haematopoiesis — a mimic to exclude in MDS."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Inflammaging interferon: the innate immune inflammaging (the cGAS-STING and S100A8/9 already mapped) drives the type-I interferon and the inflammatory bone-marrow (already mapped) microenvironment of MDS."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "MDS/MPN overlap: the MDS and the myeloproliferative neoplasms overlap in the MDS/MPN syndromes (like CMML), sharing the clonal (TET2 and splicing already mapped) haematopoiesis."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Erythroblastic-island macrophages: the marrow macrophages (the nurse cells of the erythroblastic islands, the erythrophagocytosis) and their inflammatory (S100A8/9 already mapped) activation shape the dysplastic microenvironment of MDS."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells contribute to the immune surveillance and the dysregulated inflammatory (S100A8/9 and TLR4 already mapped) microenvironment of the myelodysplastic marrow."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-mediated marrow suppression of MDS."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the dysregulated immune microenvironment of MDS."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow (already mapped) microenvironment of MDS."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the dysregulated marrow microenvironment of MDS."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Humoral/autoimmune arm: the plasma cells secrete the antibodies (already mapped) of the autoimmune and paraproteinaemic phenomena associated with MDS."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the inflammatory, dysplastic marrow (already mapped) microenvironment of MDS."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the inflammasome (NLRP3 already mapped)-linked marrow inflammation and the ineffective haematopoiesis of MDS."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the myeloid recruitment and the inflammatory marrow niche driving the ineffective haematopoiesis of MDS."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the inflammatory marrow niche driving the ineffective haematopoiesis of MDS."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Transfusional iron overload: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin and ferroportin already mapped) of the anaemia and the transfusional iron overload of MDS."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Marrow niche matricellular: osteopontin, a matricellular cytokine of the bone-marrow (already mapped) niche, contributes to the inflammatory stromal remodelling of the ineffective haematopoiesis of MDS."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Marrow alarmin: TSLP, produced by the dysplastic marrow stroma, activates the dendritic cells (already mapped) and mast cells in the marrow microenvironment, sustaining the inflammatory milieu that drives the ineffective haematopoiesis of MDS."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-marrow axis: bradykinin, generated by the contact-kinin activation in the inflamed marrow sinusoids, amplifies the endothelial permeability and the cytokine (TNF-α and IL-1β already mapped) signalling of the dysfunctional marrow microenvironment of MDS."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) over-activation in the inflamed marrow niche, moderating the immune-mediated haematopoietic suppression of MDS."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Marrow mast-cell effector: histamine, released by mast cells in the dysplastic marrow niche of MDS, amplifies the cytokine (TNF-α and IL-1β already mapped) signalling and the inflammatory microenvironment that suppresses the effective haematopoiesis of MDS."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Marrow stromal ECM: periostin, secreted by marrow stromal cells under TGF-β (already mapped) signalling, promotes the fibrotic remodelling of the bone-marrow (already mapped) niche and the dysfunctional haematopoietic stem-cell (already mapped) environment of MDS."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Antioxidant marrow protection: melatonin, via MT1/MT2 receptors on haematopoietic progenitors (already mapped), scavenges the ROS (already mapped) generated by dysfunctional mitochondria and may attenuate the oxidative damage driving the clonal evolution of MDS."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "MDS testosterone: androgen signalling on haematopoietic progenitors supports erythroid differentiation and attenuates TGF-β (already mapped) suppression; testosterone deficiency worsens the MDS anaemia in the dysplastic bone-marrow (already mapped) niche."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "MDS serotonin: serotonin released by dysplastic megakaryocytes modulates haematopoietic progenitor proliferation via 5-HT receptors; platelet (already mapped) serotonin promotes marrow fibrosis via TGF-β (already mapped) activation in MDS."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "MDS prolactin: prolactin synergises with erythropoietin (already mapped) to stimulate erythropoiesis in the dysplastic bone-marrow (already mapped); prolactin also modulates the T-helper cell (already mapped) and macrophage (already mapped) immune surveillance of MDS clones."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "MDS oxytocin: oxytocin modulates NF-κB (already mapped) and TNF-α (already mapped) driven bone-marrow (already mapped) signalling in MDS; oxytocin also supports erythropoietin (already mapped) mediated erythropoiesis and macrophage (already mapped) immune surveillance."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "MDS vasopressin: vasopressin (ADH) amplifies NF-κB (already mapped) and IL-6 (already mapped) driven bone-marrow (already mapped) inflammation; vasopressin modulates macrophage (already mapped) TGF-β (already mapped) and erythropoietin (already mapped) mediated erythropoiesis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "MDS selenium: selenoproteins suppress ROS-driven NF-κB (already mapped) and TNF-α (already mapped) mediated bone-marrow (already mapped) inflammation; selenium deficiency amplifies oxidative DNA damage and worsens macrophage (already mapped) immune dysregulation."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MDS iodine: iodine-dependent thyroid hormones regulate erythropoietin (already mapped) mediated erythropoiesis; iodine deficiency impairs the NF-κB (already mapped) and IL-6 (already mapped) macrophage (already mapped) immune surveillance in myelodysplastic syndrome."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "MDS sodium: sodium-driven macrophage (already mapped) and neutrophil (already mapped) activation amplifies the NF-κB (already mapped) and TNF-α (already mapped) inflammatory cascade of MDS; excess sodium worsens bone-marrow (already mapped) haematopoietic dysregulation."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "MDS magnesium: magnesium, as cofactor of nucleotide repair enzymes in erythrocytes (already mapped) and macrophages (already mapped), supports haematopoiesis; magnesium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of MDS."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "MDS calcium: calcium, as second messenger in macrophages (already mapped) and erythrocytes (already mapped), regulates haematopoietic signalling; calcium dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of MDS."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "MDS potassium: potassium regulates macrophage (already mapped) and neutrophil (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and bone-marrow (already mapped) haematopoietic cascade of MDS."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "MDS phosphorus: phosphorus, as ATP in macrophages (already mapped) and erythrocytes (already mapped), fuels haematopoiesis and DNA repair; phosphorus deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and bone-marrow (already mapped) cascade of MDS."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "MDS carbon: carbon as backbone of erythropoietin (already mapped) and myeloid receptor proteins in haematopoietic stem cells (already mapped) sustains erythropoiesis; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) dysplastic cascade of MDS."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "MDS nitrogen: nitrogen in amino-acid scaffold of RUNX1 and TP53 proteins modulates haematopoietic (already mapped) stem-cell differentiation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) dysplastic cascade of MDS."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "MDS chloride: chloride regulates haematopoietic stem cells (already mapped) and macrophages (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) dysplastic cascade of MDS."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "MDS hydrogen: hydrogen in water and redox chemistry of haematopoietic stem cells (already mapped) modulates RUNX1 and TP53 protein folding; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) dysplastic cascade of MDS."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "MDS sulfur: sulfur in cysteine residues of RUNX1 and TP53 proteins sustains redox stability in haematopoietic stem cells (already mapped); sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) dysplastic cascade of MDS."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "MDS pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates marrow immune surveillance; pd-1 dysregulation amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade of MDS."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "MDS glp-1: GLP-1 from macrophages (already mapped) and dendritic cells (already mapped) modulates metabolic-inflammatory marrow tone; glp-1 dysfunction amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade of MDS."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "MDS angiotensin-ii: angiotensin-II from macrophages (already mapped) and hepatocytes (already mapped) drives haematopoietic vascular tone; angiotensin-ii excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "MDS wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and hepatocytes (already mapped) regulates haematopoietic stem fate; wnt-beta-catenin dysregulation amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "MDS rankl: RANKL from macrophages (already mapped) and hepatocytes (already mapped) promotes marrow immune evasion; rankl excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "MDS fibronectin: fibronectin in macrophages (already mapped) and hepatocytes (already mapped) promotes marrow ECM remodelling; fibronectin excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "MDS notch: NOTCH in macrophages (already mapped) and hepatocytes (already mapped) regulates haematopoietic stem lineage; notch dysregulation amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "MDS igf-1: IGF-1 from macrophages (already mapped) and hepatocytes (already mapped) modulates marrow metabolic repair; igf-1 excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "MDS activin-a: activin-A from macrophages (already mapped) and hepatocytes (already mapped) promotes marrow fibrosis; activin-a excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade."
---

# Myelodysplastic Syndromes

## Overview

**Myelodysplastic syndromes (MDS)** are a heterogeneous group of clonal hematopoietic stem cell (HSC) disorders characterized by ineffective hematopoiesis, peripheral blood cytopenias, bone marrow dysplasia, and variable risk of transformation to acute myeloid leukemia (AML). MDS is fundamentally an epigenetic and splicing disorder — most driver mutations affect DNA methylation (DNMT3A, TET2, IDH1/2), chromatin remodeling (ASXL1, EZH2, SRSF2-cohesin), or RNA splicing (SF3B1, SRSF2, U2AF1, ZRSR2) — converging on dysplastic differentiation, ineffective erythropoiesis, and immune evasion by pre-leukemic clones. MDS affects ~15,000-20,000 Americans per year; the median age at diagnosis is 70-75 years; it is more common in males (1.5:1). Prognosis varies enormously from near-normal life expectancy in very-low-risk disease to <1 year in high-risk MDS-EB2. Allogeneic stem cell transplantation is the only potentially curative treatment. The approval of azacitidine (AZA-001 trial, 2009) and subsequently venetoclax+azacitidine (2024) and luspatercept (2020) has transformed the therapeutic landscape [^fenaux-2009-aza001] [^fenaux-2020-medalist].

**Epidemiology and risk factors:**
- Incidence: ~15,000-20,000 new cases/year USA; prevalence ~60,000; rising with aging population
- Risk factors: Prior chemotherapy or radiation (therapy-related MDS, t-MDS; ~10-15% of MDS; typically presents 2-7 years after alkylating agents or radiation, or 1-3 years after topoisomerase II inhibitors); older age (median onset 70 years); benzene/organic solvent exposure; congenital syndromes (Fanconi anemia, Diamond-Blackfan, Shwachman-Diamond, dyskeratosis congenita); CHIP → MDS progression (especially DNMT3A, TET2, ASXL1 CHIP); germline predisposition syndromes (GATA2, DDX41, RUNX1 germline variants → familial MDS/AML)

**Molecular landscape:**
- **Splicing factor mutations (~50% of MDS total):** SF3B1 (25%; ring sideroblasts, favorable prognosis), SRSF2 (15%; chronic myelomonocytic leukemia overlap), U2AF1 (10%; del20q association), ZRSR2 (X-linked; ~5%)
- **DNA methylation:** DNMT3A (~20%), TET2 (~20%), IDH1/IDH2 (~10%)
- **Chromatin remodeling:** ASXL1 (~20%; adverse; PRC1 complex loss), EZH2 (~6%; adverse; PRC2 loss), BCOR (~5%), KDM6A
- **Transcription factors:** RUNX1 (~15%; adverse; AML-RGA defining), ETV6 (~10%)
- **Cohesins and DNA repair:** STAG2 (~7%), RAD21 (~2%), CTCF; impair sister chromatid cohesion → genomic instability
- **TP53:** ~10% of MDS; biallelic (MDS-biTP53) = WHO 2022 specific subtype; complex karyotype; worst prognosis

## Structure

### Bone marrow and peripheral blood findings

**Morphological dysplasia:**
MDS diagnosis requires ≥10% dysplastic cells in ≥1 hematopoietic lineage (erythroid, myeloid, megakaryocytic) on bone marrow aspirate/biopsy:
- **Erythroid dysplasia:** Nuclear budding, multinucleation, nuclear bridging, ringed sideroblasts (pathological iron deposition around mitochondria in perinuclear ring pattern on Prussian Blue stain; ≥5% ringed sideroblasts = MDS-RS); SF3B1 mutation drives ring sideroblast formation
- **Myeloid dysplasia:** Hypogranular/agranular neutrophils, Pelger-Huet anomaly (bilobed hyposegmented neutrophils → hypolobated PMNs); pseudo-Pelger-Huet cells; abnormal granulation; monocytoid change
- **Megakaryocytic dysplasia:** Micromegakaryocytes (small, hypolobated), non-lobulated megakaryocytes, wide-spread nuclear segments; megakaryocyte dysplasia alone is insufficient for MDS diagnosis

**Bone marrow blasts:**
Myeloid blasts are the critical quantitative threshold determining MDS subtype and prognosis:
- <5% blasts: MDS (non-EB variants): MDS-LB, MDS-RS, MDS-del5q, MDS-hypo, MDS-SLD/MLD
- 5-9% blasts: MDS-EB1 (excess blasts 1): High-risk; AML transformation risk ~30% at 2 years
- 10-19% blasts: MDS-EB2 (excess blasts 2): Very high-risk; treat as AML in many centers; AML transformation risk ~50% at 2 years
- ≥20% blasts: AML by definition (WHO 2022; ≥20% remains AML threshold; alternative ICC 2022 uses ≥20% for AML unless defining cytogenetics)

**Cytogenetics (key prognostic cytogenetic abnormalities):**
- Favorable: del(5q) isolated, del(20q), -Y
- Intermediate: +8, del(7q), del(11q), others
- Adverse: del(7)/monosomy 7, del(17p), i(17q), complex karyotype (≥3 abnormalities), monosomal karyotype
- **Monosomal karyotype (MK):** ≥2 autosomal monosomies or 1 monosomy + 1 structural abnormality → extremely adverse (IPSS-R very poor; often concurrent with TP53 biallelic, del(17p))
- **del(5q) isolated (MDS-del5q):** Haploinsufficiency of RPS14 (ribosomal protein S14) → erythroid maturation defect; lenalidomide is highly effective (TI rate ~67%); favorable prognosis; TP53 mutation acquisition on lenalidomide is a resistance mechanism

### Prognostic scoring

**IPSS-R (International Prognostic Scoring System — Revised, 2012):**
Five variables: cytogenetic risk (very good/good/intermediate/poor/very poor), hemoglobin, platelet count, ANC, blast percentage. Risk categories: Very Low (<1.5), Low (1.5-3), Intermediate (3-4.5), High (4.5-6), Very High (>6). Median OS from 8.8 years (Very Low) to 0.8 years (Very High). IPSS-R guides treatment decisions (low vs. high risk).

**IPSS-M (Molecular IPSS, 2022):**
Integrates 31 gene mutation data with 6 clinical variables → more granular risk stratification; reclassifies ~40% of patients compared to IPSS-R; identifies very-low-risk patients with favorable mutations (SF3B1 without co-mutations) and very-high-risk patients with co-mutations (RUNX1+ASXL1, TP53 biallelic). Available online via IPSS-M calculator.

## Function

### Hematopoietic stem cell dysfunction in MDS

**Ineffective hematopoiesis:**
MDS HSCs undergo clonal expansion and dysplastic differentiation but die within the marrow via accelerated apoptosis of committed progenitors (especially erythroid; TGF-β/activin A → Smad2/3 → GDF11 → GATA1 suppression → erythroid apoptosis; target of luspatercept via activin receptor trap). Peripheral blood cytopenias despite hypercellular marrow (most lower-risk MDS) is the hallmark paradox of MDS — high marrow cellularity with ineffective output.

**MDS immune microenvironment:**
MDS blasts and dysplastic cells evade immune destruction via:
- CD47 overexpression ("don't eat me" signal → blocks macrophage phagocytosis → magrolimab (anti-CD47) disrupts this)
- PD-L1 expression → T-cell exhaustion (pembrolizumab active in MSI-H MDS; azacitidine upregulates PD-L1, may synergize with checkpoint inhibitors)
- MDS regulatory T-cells and MDSCs suppress anti-tumor immunity

## Pathology

### Diagnosis and clinical presentation

**Clinical presentation:**
- Symptomatic anemia (most common): Fatigue, pallor, dyspnea; transfusion-dependent anemia in ~50% of lower-risk MDS patients
- Neutropenia: Recurrent bacterial infections; neutrophil dysfunction (hypogranular PMNs are functionally impaired even when ANC is normal)
- Thrombocytopenia: Bleeding tendency; ecchymoses; platelet dysfunction independent of count
- Incidental discovery on CBC: Macrocytosis (MCV >100 in ~60%), hypersegmented or hyposegmented PMNs → CBC prompts bone marrow evaluation

**Diagnostic workup:**
1. CBC with differential: Cytopenias (1 or more of: Hgb <10, ANC <1800, platelets <100,000)
2. Peripheral blood smear: Dysplastic PMNs, oval macrocytes, hypogranular neutrophils, blasts
3. Bone marrow aspirate + biopsy: Dysplasia in ≥10% cells; blast count; ringed sideroblasts; cellularity
4. Conventional cytogenetics (karyotype): Required; 20-cell metaphase analysis; 50% of MDS have cytogenetic abnormality
5. FISH: del(5q), del(7q)/monosomy 7, del(20q), +8
6. Molecular panel: NGS 40-50 gene panel (SF3B1, ASXL1, TET2, DNMT3A, RUNX1, TP53, U2AF1, SRSF2, IDH1/2, EZH2, STAG2) → IPSS-M calculation
7. Exclude mimics: B12/folate deficiency, copper deficiency, HIV, paroxysmal nocturnal hemoglobinuria (PNH), congenital dyserythropoiesis

### Treatment by risk category

**Lower-risk MDS (IPSS-R Very Low, Low, Intermediate):**
- **Observation:** Asymptomatic lower-risk MDS; close monitoring with CBC every 3-6 months
- **Erythropoiesis-stimulating agents (ESAs):** Epoetin alfa or darbepoetin; indicated if endogenous EPO <500 mU/mL; Hgb response in ~40-50%; predictors of response: low serum EPO, low transfusion burden, ≤5% blasts, SF3B1 mutation
- **Luspatercept (MEDALIST trial, 2020):** [^fenaux-2020-medalist] TGF-β superfamily ligand trap → blocks GDF11/activin A → restores erythroid maturation; MEDALIST: RBC-TI in 38% vs 13% (MDS-RS, prior ESA failure); FDA approved 2020 for lower-risk MDS-RS; COMMANDS trial (luspatercept vs. epoetin alfa first-line): TI rate 58% vs 31% → FDA approved as first-line alternative to ESA (2023)
- **Lenalidomide (del5q MDS):** FDA 2005; TI rate ~67% in del5q MDS; MDS-005 trial: TI rate 56.1% vs 1.3% placebo; TP53 mutation monitoring required (clonal selection on lenalidomide)
- **Transfusion support:** Packed red blood cell transfusions for symptomatic anemia; iron chelation (deferasirox, deferoxamine) if chronic transfusion → ferritin >2500 ng/mL or cumulative transfusion burden >20-25 units
- **Imetelstat (telomerase inhibitor, FDA 2024):** For lower-risk MDS with anemia failing ESA + luspatercept; IMerge: RBC-TI 40% vs 15% (non-del5q, non-RS); first telomerase inhibitor approved for MDS

**Higher-risk MDS (IPSS-R High, Very High):**
- **Azacitidine (AZA-001):** [^fenaux-2009-aza001] OS 24.5 vs 15.0 months vs conventional care (best supportive care, low-dose cytarabine, or induction chemo); CR rate ~17%; TI rate ~45%; 75 mg/m² days 1-7 q28d; now superseded by combination regimens in fit patients; remains standard for unfit patients
- **Azacitidine + venetoclax (VIALE-A for AML; NORSE/BeyondSEVEN for MDS):** FDA approved 2024 for HMA-naive higher-risk MDS; CR+CRi ~67% vs 27% (azacitidine alone) in MDS-EB2 similar to AML data; standard of care for fit higher-risk MDS
- **Decitabine:** Alternative HMA; 20 mg/m² days 1-5 q28d; similar efficacy to azacitidine in indirect comparison; decitabine/cedazuridine (oral decitabine) FDA approved 2020 → same exposure as IV, patient convenience
- **Induction chemotherapy (7+3):** For MDS-EB2 younger/fit patients (age <70, no significant comorbidities); CR rate ~50-60%; bridge to allo-SCT; appropriate for RUNX1-mutant or favorable-cytogenetic MDS-EB2
- **Allogeneic SCT:** Only curative option; IPSS-R ≥3.5 (intermediate-high) should be evaluated for transplant; MIPSS70+v2.0 for molecular-informed transplant timing; reduced intensity conditioning for older (>55) patients; 5-year OS ~30-50% depending on risk group

**TP53-mutant MDS (MDS-biTP53):**
- Venetoclax+azacitidine: Lower activity than TP53-WT (CR ~15-20% vs 60%+); OS remains poor
- Eprenetapopt (APR-246, p53 reactivator) + azacitidine: Phase 2: CR ~33%, ORR ~58% in MDS-biTP53; Phase 3 confirmatory ongoing
- Magrolimab (anti-CD47) + azacitidine: Phase 2: ORR ~65% in TP53-mutant MDS; Phase 3 ongoing (clinical hold resolved 2024)
- Allo-SCT: Poor outcomes in TP53-mutant MDS even post-transplant due to rapid relapse

### AML transformation

MDS → AML transformation rate: ~10% at 1 year for very-low risk; ~40-50% at 2 years for MDS-EB2. Triggers: acquisition of additional mutations (FLT3-ITD, NRAS/KRAS, IDH2); blast percentage increase; loss of response to HMA (azacitidine failure → median OS 5-6 months; venetoclax+azacitidine re-exposure or CPX-351 or clinical trial). Monitoring: CBC q4-8 weeks on therapy; marrow reassessment at 4-6 cycles of HMA to assess blast response.

## Connections

- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A mutations in ~20% of MDS and ~40% of CHIP; DNMT3A is the most commonly mutated gene in clonal hematopoiesis; CHIP-to-MDS progression involves co-mutation of DNMT3A with TET2, ASXL1, or splicing factors (SF3B1, SRSF2); DNMT3A R882H is the dominant hotspot.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — EZH2 loss-of-function mutations in ~6% of MDS; EZH2 and DNMT3A/TET2 mutations co-occur in MDS, compounding epigenetic deregulation; EZH2 deletion/mutation is an adverse prognostic factor in MDS; tazemetostat is not currently approved for MDS.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 biallelic mutations define ultra-high risk MDS (WHO 2022: MDS-biTP53); monosomal karyotype; median OS <1 year; venetoclax+azacitidine has limited activity in TP53-mutant MDS; eprenetapopt (p53 reactivator)+azacitidine showed CR ~35% in Phase 2.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH1/2 mutations in ~10% of MDS (IDH1 ~5%, IDH2 ~5%); 2-HG → TET2 inhibition → hypermethylation amplifies DNMT3A epigenetic dysfunction; ivosidenib (IDH1) and enasidenib (IDH2) active in IDH-mutant MDS; FDA-approved in AML, under investigation in MDS.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Myelodysplastic syndromes are clonal disorders defined by marrow dysplasia (≥10% in a lineage), ring sideroblasts, and rising blasts; the signature paradox is a hypercellular marrow yielding peripheral cytopenias, because dysplastic progenitors die in the marrow before maturing.
- `connects-to` → **[AML](../aml/README.md)** — MDS is a pre-leukemic clonal disorder on a continuum with AML: rising marrow blasts (≥20% defines AML) and new driver mutations mark transformation, ranging from ~10%/year in low-risk to ~50% over 2 years in MDS-EB2; shared biology drives shared therapy (azacitidine, venetoclax).
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Ineffective erythropoiesis is the core lesion of lower-risk MDS — erythroid progenitors mature abnormally and die before producing red cells, causing transfusion-dependent anemia; luspatercept traps activin/GDF11 to release late erythroid maturation.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — MDS and myelofibrosis are overlapping clonal marrow disorders: MDS-with-fibrosis and MDS/MPN overlap (e.g. CMML) blur the boundary, both share mutations (ASXL1, SRSF2, TP53), both cause cytopenias, and both can transform to AML; marrow fibrosis in MDS is adverse.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Hypoplastic MDS overlaps with aplastic anemia — both present with pancytopenia and a hypocellular marrow, and both can respond to immunosuppression (ATG/ciclosporin); a PNH clone or MDS-defining cytogenetics/mutations help distinguish clonal MDS from immune aplastic anemia.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — MDS produces dysplastic, hypogranular neutrophils with hyposegmented (pseudo-Pelger-Huët) nuclei and impaired function; neutropenia plus qualitative defects make infection a leading cause of death; the absolute neutrophil count feeds IPSS-R risk scoring and antibiotic planning.
- `connects-to` → **[Chronic Myelomonocytic Leukemia](../cmml/README.md)** — MDS and CMML are overlapping clonal marrow disorders divided by the WHO: pure MDS is dysplasia with cytopenias and no proliferation, while CMML (an MDS/MPN overlap) adds persistent monocytosis—but both share mutations (TET2, SRSF2, ASXL1) and can progress to AML.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ionizing radiation is an established cause of MDS: atomic-bomb survivors and patients given radiotherapy develop therapy-related MDS years later, typically with -7/-5 cytogenetics and TP53 mutations and a poor prognosis—radiation injuring the hematopoietic stem cell.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thrombocytopenia from dysplastic megakaryopoiesis is a key MDS cytopenia: the clone produces few and abnormal platelets, causing bleeding, while the del(5q) MDS subtype paradoxically runs high platelets and responds dramatically to lenalidomide.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — MDS and myeloproliferative neoplasms are overlapping clonal stem-cell disorders: MDS shows dysplasia and cytopenias, MPNs show overproduction, and the MDS/MPN-overlap category blends both—different faces of mutated hematopoietic stem cells.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — MDS is part of the Li-Fraumeni and inherited marrow-failure spectrum: germline TP53 loss predisposes to MDS and therapy-related MDS/AML, and TP53-mutant MDS is high-risk and treatment-resistant—linking a hereditary cancer syndrome to clonal marrow disease.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — MDS and iron-deficiency anemia are opposite anemias: iron deficiency is microcytic from low iron, while MDS is a macrocytic dysplastic marrow-failure anemia with normal/high iron—so unexplained macrocytic anemia in older adults warrants marrow study.
- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — SF3B1 mutation defines a favorable MDS subtype: this splicing-factor gene, when mutated, produces ring sideroblasts and an indolent anemia—now its own WHO entity, often responsive to luspatercept and carrying a comparatively good prognosis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietin underlies both the anemia and the treatment of lower-risk MDS: ineffective marrow erythropoiesis fails to answer EPO, so erythropoiesis-stimulating agents are first-line for the anemia when endogenous EPO levels are low.
- `connects-to` → **[Immune System](../immune-system/README.md)** — MDS has an immune dimension: a subset, especially hypoplastic MDS, involves T-cell-mediated marrow suppression and responds to immunosuppression, while inflammatory signaling in the marrow niche helps drive the ineffective blood production.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Transfusion-dependent MDS overloads the liver with iron: repeated red-cell transfusions deposit excess iron in the liver (and heart), causing secondary hemochromatosis, so iron chelation is part of long-term care for chronically transfused patients.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — MDS overlap syndromes enlarge the spleen: in CMML and MDS/MPN forms, abnormal myeloid cells and extramedullary hematopoiesis swell the spleen, causing fullness and worsening cytopenias—a feature that distinguishes them from pure dysplastic MDS.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — MDS is a key cause of unexplained anemia in older adults: unlike anemia of chronic disease, its low counts stem from a clonal dysplastic marrow making defective cells, so a macrocytic anemia not explained by B12, folate, or inflammation warrants a marrow biopsy.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — MDS patients drown in iron from transfusions: chronic red-cell transfusions for the anemia deposit iron in heart, liver and endocrine organs, so iron chelation is needed to prevent organ damage in lower-risk patients who live long enough.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — MDS arises from mutated blood stem cells, often via TET2: this epigenetic regulator is one of the recurrent clonal-hematopoiesis mutations that, accumulating with age, derange marrow maturation—and that hypomethylating drugs like azacitidine target.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Some MDS is driven by an immune attack from cytotoxic T cells: in hypoplastic MDS overlapping aplastic anemia, T cells suppress the marrow, so these patients can respond to immunosuppression rather than chemotherapy.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — MDS marrow cells die by pyroptosis via the NLRP3 inflammasome: chronic inflammasome activation makes the dysplastic precursors self-destruct inflammatorily, so the bone marrow is packed yet the blood counts are low—ineffective hematopoiesis.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — MDS's cytopenias come from excess apoptosis: caspase-driven death of marrow progenitors means cells are made but die before maturing, explaining the paradox of a hypercellular marrow with too few blood cells reaching circulation.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — MDS festers in an inflammatory marrow run by macrophages: myeloid cells pour out alarmins (S100A8/A9) and cytokines that fire the inflammasome and worsen the ineffective hematopoiesis—an inflammatory niche now itself a treatment target.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Years of MDS transfusions can poison the heart: each unit of red cells delivers iron the body cannot excrete, and the overload deposits in heart muscle, causing an iron cardiomyopathy and arrhythmias that drive the need for chelation.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — MDS starves tissues of oxygen: failed marrow makes too few red cells, so chronic anemia leaves the body short of oxygen, producing the fatigue and breathlessness that dominate the disease and force transfusion dependence.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — MDS warps the marrow's immune balance: in early disease autoimmune T cells attack progenitors (why immunosuppression can help), while advancing disease expands regulatory T cells that shield the malignant clone from immune attack.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper deficiency mimics MDS: too little copper—often from excess zinc or gut surgery—causes a reversible myelodysplasia with anemia, neutropenia and ringed sideroblasts, an imitator to exclude before diagnosis.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — MDS can announce itself on the skin: neutrophilic dermatoses like Sweet syndrome may herald or accompany it, a paraneoplastic clue that prompts a look at the marrow.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Some MDS scars the marrow: reticulin fibrosis worsens the cytopenias and carries a poorer prognosis, blurring the boundary with primary myelofibrosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals MDS's iron-clogged cells: ringed sideroblasts pack iron into mitochondria circling the red-cell nucleus, while dysplastic granulocytes and giant platelets betray a marrow producing defective blood.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Too much zinc can fake MDS: excess zinc drives out copper, and the resulting copper deficiency causes a reversible dysplasia and cytopenias that mimic the marrow disease — a mimic worth excluding before the real diagnosis.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Years of transfusions overload the liver: as MDS patients receive red cells for their anemia, iron with nowhere to go accumulates in hepatocytes, driving the fibrosis that makes iron chelation part of long-term care.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Transfusional iron poisons the pancreas: deposited in the islet cells over years of red-cell support, the excess iron can damage insulin production into a secondary diabetes — one of the endocrine costs of treating MDS anemia.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — MDS keeps strange autoimmune company: it associates with vasculitis, Sweet's syndrome, and the VEXAS syndrome, and some patients' cytopenias are immune-driven and respond to immunosuppression — autoimmunity riding alongside the clonal marrow.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lungs are a frequent battleground: deep neutropenia leaves MDS patients prone to pneumonia and fungal infection, and the hypomethylating drug azacitidine can itself rarely inflame the lungs into a pneumonitis.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — Metabolic mutations open a targeted door: IDH1 and IDH2 mutations in a subset of MDS make the oncometabolite 2-hydroxyglutarate, and IDH inhibitors that switch them off can restore healthy blood-cell maturation.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Transfusional iron overload silts up the endocrine glands: the relentless transfusions MDS often needs deposit iron in the thyroid and other glands, causing hypothyroidism and the endocrinopathies that iron chelation aims to prevent.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — A transplant means weighing fertility: the conditioning chemotherapy and radiation before an allogeneic stem-cell transplant can sterilize, so fertility preservation is discussed with younger MDS patients before the curative attempt.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — RUNX1 sits at the heart of MDS biology: somatic mutations of this master hematopoietic transcription factor drive dysplasia and progression to AML, and inherited RUNX1 defects (familial platelet disorder) predispose to MDS decades early.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — MDS and PNH are overlapping marrow-failure clones: small PNH clones often lurk in hypoplastic MDS, and the shared immune-mediated attack on the marrow blurs the line between clonal escape and aplasia.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Immune surveillance falters in MDS: natural killer cells that should cull the dysplastic clone are reduced and functionally impaired, helping the abnormal stem cells expand and dimming the marrow's own defense.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Excess TGF-β strangles red-cell maturation: overactive TGF-β/SMAD signaling blocks late erythroid maturation in MDS, the ineffective erythropoiesis that the trap drug luspatercept relieves to lift the anemia.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — The soil can drive the disease, not just the seed: a dysfunctional bone-marrow niche — including its osteoblast and mesenchymal cells — fosters and shelters the dysplastic clone, making the microenvironment part of MDS pathogenesis.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Chronic anemia and iron overload tax the heart: years of low hemoglobin force a high-output strain while transfusional iron deposits in the myocardium, so cardiovascular complications are a major cause of death in MDS.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation poisons the marrow's own output: NF-κB signaling is overactive in MDS progenitors, priming the NLRP3 inflammasome and pyroptotic cell death that produce the ineffective hematopoiesis and cytopenias of the disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Clonal immune signaling shadows the disease: STAT3-activating mutations in associated large granular lymphocyte clones, and STAT3 signaling in the marrow, contribute to the immune dysregulation and cytopenias seen in MDS.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Empty defenses invite fatal infection: the neutropenia of MDS, deepened by hypomethylating-agent therapy, leaves patients prone to overwhelming infection, and sepsis is among the commonest causes of death.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Prolonged neutropenia opens the lung to mold: the deep, sustained neutropenia of MDS and its therapy lets inhaled Aspergillus invade as angioinvasive pulmonary aspergillosis, a feared infectious complication.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Failing neutrophils let the yeast bloodstream: neutropenia and disrupted mucosa in MDS allow Candida to translocate into the blood, causing invasive candidiasis in these immunocompromised patients.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Transfusions rust the heart: lifelong red-cell transfusions for MDS anemia deposit iron in the myocardium, and this siderosis — atop the strain of chronic anemia — can drive a cardiomyopathy and heart failure.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its hypomethylating therapy deepens immune suppression: azacitidine and decitabine for MDS add to the disease's own neutropenia and T-cell dysfunction, raising the risk of Pneumocystis pneumonia.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Lenalidomide for low-risk MDS clots the veins: the immunomodulatory drug used for del(5q) MDS carries a recognized prothrombotic signal, raising venous thromboembolism risk during treatment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic, transfusion-dependent cancer weighs on mood: the fatigue, frequent hospital visits, poor prognosis and looming leukemic transformation of MDS, mostly in older patients, contribute to depression.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Transfusion iron overload poisons the glands: years of red-cell transfusions in MDS deposit iron in the pancreas, pituitary and thyroid, causing diabetes, hypogonadism and other endocrinopathies.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its therapy reawakens shingles: the hypomethylating agents, immunosuppression and stem-cell transplant used in MDS deplete T-cell immunity, allowing latent varicella-zoster to reactivate.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A transfusion-dependent pre-leukaemia breeds worry: the cytopenias, transfusion dependence and ever-present threat of progression to AML in MDS foster chronic health anxiety alongside depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It erupts on the skin: MDS is a classic trigger of Sweet syndrome, a neutrophilic dermatosis of tender plaques, and other autoinflammatory eruptions, with leukaemia cutis if it transforms to AML.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It overlaps systemic autoinflammation: MDS associates with VEXAS syndrome and relapsing polychondritis, producing inflammatory arthritis, chondritis and other rheumatic features alongside the cytopenias.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Years of transfusion poison the liver: repeated red-cell transfusions in MDS deposit iron in hepatocytes, causing iron-overload liver injury that iron chelation aims to prevent.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Its low platelets and anaemia reach the brain: severe thrombocytopenia risks intracranial haemorrhage, and chronic anaemia causes fatigue and cognitive slowing.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Failing marrow exposes the lungs: neutropenia invites bacterial and invasive fungal pneumonia, and repeated transfusion can cause circulatory overload or lung injury.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its autoinflammation can swell the nodes and spleen: MDS-associated systemic inflammation, including VEXAS syndrome, can cause lymphadenopathy, and overlap forms bring splenomegaly.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Treatment and overload reach the kidney: hypomethylating chemotherapy plus the renal effects of anaemia and transfusional iron overload strain the kidney in MDS.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Tailored drugs match its biology: hypomethylating agents (azacitidine, decitabine), lenalidomide for del(5q) MDS and luspatercept for anaemia are mainstays beyond supportive transfusion.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Transplant reawakens latent virus: many MDS patients undergo allogeneic stem-cell transplant, after which cytomegalovirus and other herpesviruses reactivate under immunosuppression.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Both consequence and treatment: therapy-related MDS arises years after alkylator or topoisomerase chemotherapy, while high-risk MDS itself is treated with intensive chemotherapy or hypomethylating agents en route to transplant.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Transfusional iron poisons the heart: chronic red-cell transfusions for MDS anaemia deposit iron in the myocardium, causing a siderotic cardiomyopathy and heart failure that iron chelation aims to prevent.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Shared transfusion dependence: like transfusion-dependent thalassemia, lower-risk MDS causes chronic anaemia needing regular transfusions and the iron overload they bring — one a marrow-failure clone, the other an inherited globin defect.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Transfusions overload the liver with iron: transfusion-dependent MDS accumulates iron in the hepatic lobule as haemosiderosis, adding liver iron toxicity to the cardiac loading that chelation therapy aims to prevent.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Its therapy can cause it: alkylating chemotherapy and autologous transplant for multiple myeloma raise the risk of therapy-related myelodysplastic syndrome years later, a feared late complication of cure.
- `connects-to` → **[Uveal Melanoma](../uveal-melanoma/README.md)** — A shared splicing-factor mutation: SF3B1, which defines MDS with ring sideroblasts, is the same spliceosome gene mutated in a subset of uveal melanomas—one splicing defect across a marrow and an eye cancer.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Therapy-related MDS: the alkylators and radiation used to cure solid tumours such as breast cancer can damage the marrow's stem cells, seeding a secondary, poor-prognosis MDS that often progresses to AML.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Myeloid clone meets autoinflammation: MDS associates with systemic autoinflammatory and autoimmune syndromes—including VEXAS and vasculitis—where the mutant clone drives inflammation overlapping ANCA-associated disease.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Transfusional iron and the heart: years of red-cell transfusions for MDS deposit iron in the heart, injuring the myocardium and cardiac conduction system into cardiomyopathy and arrhythmia unless iron is chelated.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Clonal haematopoiesis and the artery: the TET2 and DNMT3A clones underlying MDS and CHIP spawn inflammatory monocytes that accelerate atherosclerosis, linking clonal marrow disease to heart attacks and strokes.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — A shared oncometabolite: IDH1/IDH2-mutant MDS and IDH-mutant glioma both generate 2-hydroxyglutarate that reprograms the epigenome and respond to the same IDH inhibitors, one drug class across blood and brain.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Iron-driven diabetes: transfusional iron overload in MDS deposits in the pancreas, impairing insulin secretion and causing a secondary 'bronze' diabetes alongside the cardiac and hepatic iron loading.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammaging marrow: TNF-α and other inflammatory cytokines drive the ineffective haematopoiesis and apoptosis that cause the cytopenias of myelodysplastic syndrome.
- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — Transformation kinase: FLT3 mutations, though less common than in AML, appear in MDS and mark progression toward acute myeloid leukaemia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Clonal survival signalling: PI3K-AKT-mTOR signalling supports the survival of the dysplastic clone in myelodysplastic syndrome.
- `connects-to` → **[SRSF2](../../03-molecular/srsf2/README.md)** — Spliceosome mutation: SRSF2 is one of the recurrently mutated splicing factors in MDS, corrupting mRNA splicing across the genome and a hallmark driver alongside SF3B1 of the dysplastic clone.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Alarmin-driven dysplasia: S100A8/A9 released in the MDS marrow activates the NLRP3 inflammasome in progenitors, driving the chronic inflammation and pyroptotic cell death behind ineffective haematopoiesis.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Thrombopoiesis support: thrombopoietin-receptor agonists are used to raise platelet counts in the thrombocytopenia of lower-risk MDS, addressing the bleeding risk of ineffective megakaryopoiesis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β matured by the NLRP3 inflammasome in MDS progenitors drives the inflammatory, pyroptotic cell death that produces the ineffective hematopoiesis and the cytopenias central to the disease despite a hypercellular marrow.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — The ineffective erythropoiesis of MDS suppresses hepcidin, and chronic red-cell transfusion compounds the resulting parenchymal iron loading that damages heart and liver—the reason transfusion-dependent patients need iron chelation.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — In hypocellular MDS, T-cell IFN-γ suppresses hematopoietic progenitors—the rationale for immunosuppressive therapy that can restore counts in this subset, which overlaps biologically with aplastic anemia.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Higher-risk MDS evolving toward AML becomes dependent on anti-apoptotic BCL-2, the rationale for adding venetoclax to hypomethylating agents to push the dysplastic clone back into the apoptosis it has been evading.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — In TP53-wild-type MDS, high MDM2 holds p53 in check, so MDM2 inhibitors are a strategy to reactivate p53-driven apoptosis—distinct from the dismal-prognosis TP53-mutant MDS where the protein itself is lost.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 from marrow stromal cells anchors the MDS clone in its bone-marrow niche, and a disordered, inflammatory niche both supports the dysplastic clone and contributes to the ineffective hematopoiesis that defines the disease.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Chronic TLR4 activation by danger signals such as the S100A8/A9 already mapped fuels the NLRP3-inflammasome inflammation and pyroptotic cell death behind the ineffective hematopoiesis of MDS.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling represses erythroid maturation in MDS, the mechanism that luspatercept—acting on the activin/SMAD pathway already mapped—relieves to improve transfusion-dependent anemia.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 in the MDS marrow microenvironment drives hepcidin and the anemia of inflammation while suppressing residual normal hematopoiesis, deepening the cytopenias of the disease.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Chronic TLR-MyD88 signaling (TLR4 and S100A8/A9 mapped) in MDS stem and progenitor cells activates the NLRP3 inflammasome and pyroptosis, driving the ineffective hematopoiesis and cytopenias.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K-AKT-mTOR signaling (AKT mapped) supports the survival and growth advantage of the MDS clone over normal hematopoiesis.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Acquisition of RAS-pathway mutations marks the progression of MDS toward secondary acute myeloid leukemia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK-STAT signaling (STAT3 mapped) is constitutively engaged in MDS progenitors and in MDS/MPN-overlap disease, a target of JAK inhibitor therapy.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN-restrained PI3K-AKT-mTOR signaling (AKT and mTOR mapped) promotes survival and proliferation of the dysplastic clone in MDS.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING amplifies the NLRP3-inflammasome-driven inflammatory bone-marrow milieu (NLRP3 mapped) characteristic of MDS.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports the survival and bone-marrow-niche adhesion of the dysplastic clone and contributes to the inflammatory marrow microenvironment of MDS.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune-mediated cytopenias and the inflammatory bone-marrow milieu of MDS.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — RAS-ERK signaling (KRAS already mapped) provides a proliferative input in the subset of MDS that progresses toward acute myeloid leukemia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate hematopoietic stem-cell quiescence and oxidative-stress handling, programs disrupted in myelodysplastic syndromes.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α shapes the hypoxic bone-marrow niche and the ineffective erythropoiesis of myelodysplastic syndromes.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β dysregulation contributes to the impaired differentiation and clonal advantage of myelodysplastic-syndrome progenitors.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxic immunosurveillance of the dysplastic clone shapes the immune-mediated cytopenias and clonal evolution of myelodysplastic syndrome.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Dysregulated CDK4/6-cyclin-D cell-cycle control contributes to the clonal proliferation and leukemic evolution of myelodysplastic syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the aberrant survival and inflammatory signaling of the myelodysplastic clone.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the clonal hematopoietic cells of myelodysplastic syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival and differentiation of the dysplastic hematopoietic progenitors of myelodysplastic syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic stem cells of myelodysplastic syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the bone-marrow niche and immune interactions of myelodysplastic syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic landscape of myelodysplastic syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of myelodysplastic syndrome.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory bone-marrow microenvironment of myelodysplastic syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory bone-marrow microenvironment of myelodysplastic syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell-mediated immune dysregulation (relevant to the immunosuppressive-therapy-responsive subset) of myelodysplastic syndrome.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune-mediated subset: hypoplastic MDS features T-cell-mediated suppression of haematopoiesis, where MHC class II-restricted autoreactive T cells attack progenitors, the basis for the response of this subset to immunosuppressive therapy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow angiogenesis: increased bone-marrow microvascular density and VEGF signalling accompany MDS and support the dysplastic clone, correlating with disease burden and progression toward acute myeloid leukaemia.
- `connects-to` → **[CALR](../../03-molecular/calr/README.md)** — MDS/MPN overlap: CALR mutations mark the overlap syndromes such as MDS/MPN with ring sideroblasts and thrombocytosis (SF3B1 already mapped), extending the clonal driver landscape beyond the classic MDS lesions.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Anaemia: anaemia is the commonest cytopenia of MDS, and the resulting fatigue and transfusion dependence dominate the illness, driving the use of erythropoiesis-stimulating agents and luspatercept (both already mapped) to raise haemoglobin.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Immunosuppressive therapy: hypoplastic MDS overlaps with aplastic anaemia (already mapped) and can respond to T-cell-directed immunosuppression, reflecting an IL-2-driven autoreactive attack on the marrow in a subset of patients.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Marrow angiogenesis: increased bone-marrow microvascular density in MDS is supported by angiopoietin-Tie2 signalling alongside VEGF (already mapped), part of the altered microenvironment that sustains the dysplastic clone.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Iron overload and sideroblasts: chronic transfusion and the SF3B1 ring-sideroblast phenotype (already mapped) disturb iron handling in MDS, and ferroportin, regulated by hepcidin (already mapped), governs the iron export relevant to the overload requiring chelation.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative dyspoiesis: the iron overload and inflammation of MDS generate reactive oxygen species, to which xanthine oxidase contributes, and this oxidative stress worsens the ineffective, apoptosis- and pyroptosis-prone (NLRP3 already mapped) haematopoiesis.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune dysregulation: IL-10 among the cytokines of the inflammatory MDS marrow microenvironment (IFN-gamma, TNF and IL-6 already mapped) shapes the immune milieu that both suppresses normal haematopoiesis and is targeted by immunosuppression in a subset.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage niche: IL-4 polarises the marrow macrophages toward an M2 phenotype (IL-10 already mapped), part of the altered immune microenvironment of the dysplastic MDS marrow that shapes the ineffective haematopoiesis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipocyte crosstalk: the marrow adipocytes and their adipokine adiponectin engage in metabolic crosstalk with the dysplastic clone, the expanding marrow adipose tissue of MDS shaping the haematopoietic microenvironment.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine marrow signalling: leptin, with adiponectin (already mapped), from the marrow adipose tissue signals to the haematopoietic cells, part of the metabolic microenvironment influencing the dysplastic haematopoiesis of MDS.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 marrow inflammation: IL-13, with IL-4 (already mapped), supports the M2 marrow macrophages of the inflammatory (NLRP3 and S100A8/A9 already mapped) microenvironment that shapes the ineffective haematopoiesis of MDS.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk that shapes the dysplastic haematopoietic microenvironment of MDS.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc-copper balance: excess zinc induces copper (already mapped) deficiency, which causes a reversible MDS-like myelodysplasia, and zinc is itself required for normal haematopoiesis — a mimic to exclude in MDS.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Inflammaging interferon: the innate immune inflammaging (the cGAS-STING and S100A8/9 already mapped) drives the type-I interferon and the inflammatory bone-marrow (already mapped) microenvironment of MDS.
- `connects-to` → **[Myeloproliferative neoplasms](../myeloproliferative-neoplasms/README.md)** — MDS/MPN overlap: the MDS and the myeloproliferative neoplasms overlap in the MDS/MPN syndromes (like CMML), sharing the clonal (TET2 and splicing already mapped) haematopoiesis.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Erythroblastic-island macrophages: the marrow macrophages (the nurse cells of the erythroblastic islands, the erythrophagocytosis) and their inflammatory (S100A8/9 already mapped) activation shape the dysplastic microenvironment of MDS.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells contribute to the immune surveillance and the dysregulated inflammatory (S100A8/9 and TLR4 already mapped) microenvironment of the myelodysplastic marrow.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-mediated marrow suppression of MDS.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the dysregulated immune microenvironment of MDS.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow (already mapped) microenvironment of MDS.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the dysregulated marrow microenvironment of MDS.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Humoral/autoimmune arm: the plasma cells secrete the antibodies (already mapped) of the autoimmune and paraproteinaemic phenomena associated with MDS.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the inflammatory, dysplastic marrow (already mapped) microenvironment of MDS.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the inflammasome (NLRP3 already mapped)-linked marrow inflammation and the ineffective haematopoiesis of MDS.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the myeloid recruitment and the inflammatory marrow niche driving the ineffective haematopoiesis of MDS.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the inflammatory marrow niche driving the ineffective haematopoiesis of MDS.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Transfusional iron overload: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin and ferroportin already mapped) of the anaemia and the transfusional iron overload of MDS.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Marrow niche matricellular: osteopontin, a matricellular cytokine of the bone-marrow (already mapped) niche, contributes to the inflammatory stromal remodelling of the ineffective haematopoiesis of MDS.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Marrow alarmin: TSLP, produced by the dysplastic marrow stroma, activates the dendritic cells (already mapped) and mast cells in the marrow microenvironment, sustaining the inflammatory milieu that drives the ineffective haematopoiesis of MDS.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-marrow axis: bradykinin, generated by the contact-kinin activation in the inflamed marrow sinusoids, amplifies the endothelial permeability and the cytokine (TNF-α and IL-1β already mapped) signalling of the dysfunctional marrow microenvironment of MDS.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) over-activation in the inflamed marrow niche, moderating the immune-mediated haematopoietic suppression of MDS.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Marrow mast-cell effector: histamine, released by mast cells in the dysplastic marrow niche of MDS, amplifies the cytokine (TNF-α and IL-1β already mapped) signalling and the inflammatory microenvironment that suppresses the effective haematopoiesis of MDS.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Marrow stromal ECM: periostin, secreted by marrow stromal cells under TGF-β (already mapped) signalling, promotes the fibrotic remodelling of the bone-marrow (already mapped) niche and the dysfunctional haematopoietic stem-cell (already mapped) environment of MDS.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Antioxidant marrow protection: melatonin, via MT1/MT2 receptors on haematopoietic progenitors (already mapped), scavenges the ROS (already mapped) generated by dysfunctional mitochondria and may attenuate the oxidative damage driving the clonal evolution of MDS.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — MDS testosterone: androgen signalling on haematopoietic progenitors supports erythroid differentiation and attenuates TGF-β (already mapped) suppression; testosterone deficiency worsens the MDS anaemia in the dysplastic bone-marrow (already mapped) niche.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — MDS serotonin: serotonin released by dysplastic megakaryocytes modulates haematopoietic progenitor proliferation via 5-HT receptors; platelet (already mapped) serotonin promotes marrow fibrosis via TGF-β (already mapped) activation in MDS.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — MDS prolactin: prolactin synergises with erythropoietin (already mapped) to stimulate erythropoiesis in the dysplastic bone-marrow (already mapped); prolactin also modulates the T-helper cell (already mapped) and macrophage (already mapped) immune surveillance of MDS clones.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — MDS oxytocin: oxytocin modulates NF-κB (already mapped) and TNF-α (already mapped) driven bone-marrow (already mapped) signalling in MDS; oxytocin also supports erythropoietin (already mapped) mediated erythropoiesis and macrophage (already mapped) immune surveillance.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — MDS vasopressin: vasopressin (ADH) amplifies NF-κB (already mapped) and IL-6 (already mapped) driven bone-marrow (already mapped) inflammation; vasopressin modulates macrophage (already mapped) TGF-β (already mapped) and erythropoietin (already mapped) mediated erythropoiesis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — MDS selenium: selenoproteins suppress ROS-driven NF-κB (already mapped) and TNF-α (already mapped) mediated bone-marrow (already mapped) inflammation; selenium deficiency amplifies oxidative DNA damage and worsens macrophage (already mapped) immune dysregulation.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MDS iodine: iodine-dependent thyroid hormones regulate erythropoietin (already mapped) mediated erythropoiesis; iodine deficiency impairs the NF-κB (already mapped) and IL-6 (already mapped) macrophage (already mapped) immune surveillance in myelodysplastic syndrome.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — MDS sodium: sodium-driven macrophage (already mapped) and neutrophil (already mapped) activation amplifies the NF-κB (already mapped) and TNF-α (already mapped) inflammatory cascade of MDS; excess sodium worsens bone-marrow (already mapped) haematopoietic dysregulation.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — MDS magnesium: magnesium, as cofactor of nucleotide repair enzymes in erythrocytes (already mapped) and macrophages (already mapped), supports haematopoiesis; magnesium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of MDS.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — MDS calcium: calcium, as second messenger in macrophages (already mapped) and erythrocytes (already mapped), regulates haematopoietic signalling; calcium dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of MDS.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — MDS potassium: potassium regulates macrophage (already mapped) and neutrophil (already mapped) membrane potential; potassium dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and bone-marrow (already mapped) haematopoietic cascade of MDS.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — MDS phosphorus: phosphorus, as ATP in macrophages (already mapped) and erythrocytes (already mapped), fuels haematopoiesis and DNA repair; phosphorus deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and bone-marrow (already mapped) cascade of MDS.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — MDS carbon: carbon as backbone of erythropoietin (already mapped) and myeloid receptor proteins in haematopoietic stem cells (already mapped) sustains erythropoiesis; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) dysplastic cascade of MDS.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — MDS nitrogen: nitrogen in amino-acid scaffold of RUNX1 and TP53 proteins modulates haematopoietic (already mapped) stem-cell differentiation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) dysplastic cascade of MDS.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — MDS chloride: chloride regulates haematopoietic stem cells (already mapped) and macrophages (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) dysplastic cascade of MDS.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — MDS hydrogen: hydrogen in water and redox chemistry of haematopoietic stem cells (already mapped) modulates RUNX1 and TP53 protein folding; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) dysplastic cascade of MDS.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — MDS sulfur: sulfur in cysteine residues of RUNX1 and TP53 proteins sustains redox stability in haematopoietic stem cells (already mapped); sulfur dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) dysplastic cascade of MDS.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — MDS pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates marrow immune surveillance; pd-1 dysregulation amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade of MDS.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — MDS glp-1: GLP-1 from macrophages (already mapped) and dendritic cells (already mapped) modulates metabolic-inflammatory marrow tone; glp-1 dysfunction amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade of MDS.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — MDS angiotensin-ii: angiotensin-II from macrophages (already mapped) and hepatocytes (already mapped) drives haematopoietic vascular tone; angiotensin-ii excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — MDS wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and hepatocytes (already mapped) regulates haematopoietic stem fate; wnt-beta-catenin dysregulation amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — MDS rankl: RANKL from macrophages (already mapped) and hepatocytes (already mapped) promotes marrow immune evasion; rankl excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — MDS fibronectin: fibronectin in macrophages (already mapped) and hepatocytes (already mapped) promotes marrow ECM remodelling; fibronectin excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — MDS notch: NOTCH in macrophages (already mapped) and hepatocytes (already mapped) regulates haematopoietic stem lineage; notch dysregulation amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — MDS igf-1: IGF-1 from macrophages (already mapped) and hepatocytes (already mapped) modulates marrow metabolic repair; igf-1 excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — MDS activin-a: activin-A from macrophages (already mapped) and hepatocytes (already mapped) promotes marrow fibrosis; activin-a excess amplifies smad4 (already mapped) and vegf (already mapped) and il-2 (already mapped) myelodysplastic cascade.

[^fenaux-2009-aza001]: Fenaux P, Mufti GJ, Hellstrom-Lindberg E, et al. Efficacy of azacitidine compared with conventional care regimens in patients with higher-risk myelodysplastic syndromes. *Lancet Oncol.* 2009;10(3):223-232. [doi:10.1016/S1470-2045(09)70003-8](https://doi.org/10.1016/S1470-2045(09)70003-8) · [PubMed 19230772](https://pubmed.ncbi.nlm.nih.gov/19230772/)
[^fenaux-2020-medalist]: Fenaux P, Platzbecker U, Mufti GJ, et al. Luspatercept in patients with lower-risk myelodysplastic syndromes. *N Engl J Med.* 2020;382(2):140-151. [doi:10.1056/NEJMoa1908892](https://doi.org/10.1056/NEJMoa1908892) · [PubMed 31914241](https://pubmed.ncbi.nlm.nih.gov/31914241/)
