---
schema: human-scale-entry/v1
id: cmml
name: Chronic Myelomonocytic Leukemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic myelomonocytic leukemia (CMML) is an MDS/MPN overlap with persistent monocytosis; TET2 (~60%) and SRSF2 (~45%) are the dominant mutations; PDGFRB rearrangements → imatinib-responsive CMML-like disease. Azacitidine is standard; allo-SCT is the only cure; OS ~2 years."
aliases: ["CMML", "chronic myelomonocytic leukemia", "CMML-0", "CMML-1", "CMML-2", "myelodysplastic/myeloproliferative neoplasm", "MDS/MPN overlap", "proliferative CMML", "myelodysplastic CMML"]
sources:
  - id: itzykson-2013-cmml-prognosis
    type: peer-reviewed
    cite: "Itzykson R, Kosmider O, Renneville A, et al. Prognostic score including gene mutations in chronic myelomonocytic leukemia. J Clin Oncol. 2013;31(19):2428-2436."
    doi: "10.1200/JCO.2012.47.3314"
    pmid: "23690417"
    url: "https://doi.org/10.1200/JCO.2012.47.3314"
  - id: patnaik-2022-cmml-review
    type: peer-reviewed
    cite: "Patnaik MM, Tefferi A. Chronic myelomonocytic leukemia: 2022 update on diagnosis, risk stratification and management. Am J Hematol. 2022;97(3):352-372."
    doi: "10.1002/ajh.26457"
    pmid: "34958140"
    url: "https://doi.org/10.1002/ajh.26457"
cross_links:
  - target: 01-human/03-molecular/srsf2
    relation: connects-to
    note: "SRSF2 P95H in ~45% of CMML; most common splicing factor mutation; co-occurs with TET2 (~60%) in the dominant CMML doublet; P95H alters CCNG ESE splicing → monocytic differentiation bias; SRSF2+TET2 knockin mice develop CMML-like disease with full penetrance."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A mutations in ~10% of CMML; DNMT3A is an early CHIP hit establishing pre-malignant HSC clones before SRSF2 or TET2 co-mutation; DNMT3A+TET2+SRSF2 triplet occurs in ~5% of CMML → aggressive progression; DNMT3A-CHIP → CMML progression rate ~1-2% per year."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "KRAS/NRAS mutations in ~15% of CMML; RAS activation → monocyte proliferation → MP-CMML phenotype (WBC >13×10⁹/L, splenomegaly, organomegaly); KRAS-mutant CMML is aggressive with poor HMA response; MEK inhibitor trametinib shows early activity in RAS-mutant CMML."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB promotes monocyte/macrophage survival in CMML; SRSF2/ASXL1 mutations dysregulate NF-κB pathway activity; ruxolitinib reduces cytokine-driven NF-κB signaling in MP-CMML → splenomegaly response ~40-50%; GM-CSF/M-CSF autocrine loops drive NF-κB in CMML monocytes."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "TET2 mutations in ~60% of CMML; TET2 catalyses 5-mC → 5-hmC → promoter demethylation; TET2 loss → hypermethylation of tumor suppressor promoters + monocyte progenitor expansion; TET2+SRSF2 doublet is the dominant CMML genotype; TET2 CHIP evolves to CMML at ~1% per year."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK2 V617F in ~15-20% of CMML; enriched in MP-CMML (WBC >13×10⁹/L); JAK2 V617F → STAT5 → monocyte proliferation and splenomegaly; ruxolitinib (JAK1/2 inhibitor) achieves splenomegaly response ~30-50% in MP-CMML; JAK2-mutant CMML may overlap with MDS/MPN-SF3B1."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "CMML monocytes differentiate into patrolling and pro-inflammatory macrophages; GM-CSF/M-CSF autocrine loops drive monocyte survival; tumor-associated macrophages suppress NK killing in the marrow niche; monocytosis (AMC ≥0.5×10⁹/L, ≥10% of WBC) is the defining CMML criterion."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "CMML straddles the MDS and MPN categories in its own WHO class, MDS/MPN-overlap: it has MDS dysplasia and cytopenias plus proliferative monocytosis, splenomegaly, and JAK2/RAS features, sharing biology and JAK-inhibitor responses with the myeloproliferative neoplasms."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "CMML was historically classified with the myelodysplastic syndromes and shares their dysplastic, cytopenic marrow and AML transformation risk; the WHO now separates it as MDS/MPN-overlap for its peripheral monocytosis, but azacitidine remains a shared therapy."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "CMML is a clonal bone marrow stem-cell disease: SRSF2/TET2/ASXL1-mutant progenitors expand the monocyte lineage into a hypercellular dysplastic marrow with monocytosis; marrow blasts and cytogenetics define the CPSS prognostic groups, and allogeneic transplant is the only cure."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "CMML is a myelodysplastic/myeloproliferative overlap that transforms to AML in ~15-20%: accumulating mutations (often ASXL1, RUNX1, or NRAS on a TET2/SRSF2 background) drive blast expansion, and CMML-derived AML carries a poor prognosis."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "CMML is defined partly by what it is NOT—Philadelphia-negative: persistent monocytosis with absent BCR-ABL1 separates CMML from chronic myeloid leukemia, a distinction made by cytogenetics/PCR that changes treatment entirely (no TKI for CMML)."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CMML can be accompanied by clonal plasmacytoid dendritic cell proliferations: nodular aggregates of pDCs arise from the same mutated clone, a clue that monocytic and dendritic lineages share progenitors and a marker of more aggressive disease."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "CMML's myelodysplasia shows in dysplastic neutrophils alongside its defining monocytosis: hypogranular, pseudo-Pelger-Huët neutrophils reflect the clonal marrow defect, and persistent monocytosis with these features separates CMML from a reactive monocytosis."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The proliferative form of CMML enlarges the spleen: when the clone behaves myeloproliferatively (high white count), extramedullary hematopoiesis causes splenomegaly—unlike the dysplastic, cytopenic form, marking the MDS/MPN-overlap spectrum CMML spans."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "CMML and myelofibrosis are both MDS/MPN-spectrum disorders that can develop marrow fibrosis and splenomegaly: CMML is defined by monocytosis with dysplasia, myelofibrosis by JAK2/CALR with teardrop cells—but both are clonal stem-cell diseases that can transform to AML."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "CMML disrupts red cell production: as the dysplastic clone expands, anemia from ineffective erythropoiesis is common alongside monocytosis, so fatigue and transfusion dependence mark the myelodysplastic side of this MDS/MPN overlap disorder."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "RUNX1 mutations worsen CMML prognosis: this transcription-factor gene, often mutated alongside ASXL1 and SRSF2, impairs normal myeloid differentiation and predicts faster progression to AML—part of the molecular risk profile now guiding CMML treatment."
  - target: 01-human/07-system/essential-thrombocythemia
    relation: connects-to
    note: "CMML and essential thrombocythemia both blur the MDS/MPN border: CMML is the overlap disorder with monocytosis and dysplasia, while ET is a classic MPN with platelet excess—yet both are clonal stem-cell diseases, and CMML's proliferative type can mimic an MPN."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "CMML disrupts platelet production: the dysplastic clone often causes thrombocytopenia from ineffective marrow output, raising bleeding risk, though some cases instead run high platelets—reflecting CMML's mixed dysplastic and proliferative nature."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CMML frequently carries systemic autoimmune and inflammatory features: roughly a fifth of patients develop vasculitis, arthritis or other immune-mediated disease, because the mutant monocytes fuel inflammation—so CMML can present to rheumatology before hematology."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "CMML often infiltrates the skin: monocytic leukemia cutis and neutrophilic dermatoses like Sweet syndrome produce papules and plaques, so a skin biopsy can reveal the leukemic clone or its inflammatory companions in this monocyte-driven disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "CMML often enlarges the liver: the proliferating monocytic clone infiltrates the liver and spleen, causing hepatosplenomegaly, so organ enlargement marks the more proliferative, MPN-like end of this MDS/MPN-overlap disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CMML's main cure relies on T cells: allogeneic stem-cell transplant works through a graft-versus-leukemia effect in which donor cytotoxic T cells clear the clone, the only therapy that reliably eradicates this otherwise progressive disease."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "CMML's high cell turnover can trigger gout: rapid production and destruction of monocytic cells floods the blood with uric acid, so hyperuricemia and gout flares accompany this and other myeloproliferative disorders."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "CMML can injure the kidney through lysozyme: its excess monocytes pour out lysozyme (muramidase) that damages the proximal tubules, causing potassium wasting and renal impairment—an unusual organ complication of monocytic leukemias."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK cells matter in CMML, the only curable path being transplant: natural killer and donor immune cells mount a graft-versus-leukemia response, so harnessing NK-mediated surveillance is central to controlling a disease drugs only restrain."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "CMML smolders with inflammatory IL-6: its malignant monocytes and marrow pump out IL-6 and other cytokines that drive proliferation and the systemic symptoms—fevers, weight loss, and autoimmune features—that often accompany the leukemia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "CMML's failing marrow starves tissues of oxygen: as the malignant clone crowds out normal blood production, anemia develops and the blood carries less oxygen, driving the fatigue and breathlessness common in the disease."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "CMML can infiltrate and inflame the lungs: its excess monocytes seed pulmonary tissue and, with weakened immunity, leave patients prone to pneumonia, so respiratory infiltrates and infection are recurring complications."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "RAS-pathway mutations push CMML growth through mTOR: KRAS and related lesions activate downstream mTOR signaling that drives the monocyte proliferation, making this growth axis a target studied alongside hypomethylating drugs."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "CMML's anemia leads to iron overload: many patients become transfusion-dependent, and each unit delivers iron the body cannot excrete, building toxic deposits over the disease's course."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "CMML burdens the heart: chronic anemia forces high-output work, transfusional iron can deposit in the muscle, and the disease's inflammation can inflame the pericardium, together straining cardiac function."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "CMML comes with immune dysregulation via regulatory T cells: skewed Treg balance underlies the autoimmune and inflammatory complications—vasculitis and serositis—that often accompany the leukemia."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "CMML is diagnosed down the microscope: the blood smear and marrow show the persistent monocytosis that defines it, and imaging gauges the splenomegaly and any organ infiltration."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "CMML's monocytes spill lysozyme that injures the kidney tubules, wasting potassium, so an unexplained low potassium can be a curious clue to this monocytic leukemia."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "CMML can fibrose the marrow: reticulin fibrosis worsens the cytopenias and marks a more aggressive, MPN-leaning course of this MDS/MPN overlap disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows CMML's defining excess: a flood of abnormal monocytes pours from the marrow into the blood, their folded nuclei and granular cytoplasm the hallmark of this MDS/MPN overlap disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "The rogue monocytes can raise blood calcium: like activated macrophages they can make extra calcitriol, the active vitamin D, driving a paraneoplastic hypercalcemia occasionally seen in CMML."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Leukemic monocytes infiltrate the gut: CMML can seed the bowel wall and serous cavities with monocytic deposits, causing effusions and gastrointestinal involvement in advanced disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "CMML keeps strange autoimmune company: it associates with vasculitis, neutrophilic dermatoses, and the autoantibody-rich VEXAS syndrome, so systemic inflammation and autoimmunity often shadow the clonal monocytosis."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Years of transfusion overload the endocrine organs: as transfusion-dependent CMML accumulates iron, deposits in the pancreatic islets can damage insulin output toward a secondary diabetes."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Inflammation can reach the eye: the autoimmune and VEXAS-spectrum disease that overlaps CMML brings episcleritis and orbital inflammation, and leukemic infiltration can rarely involve the eye directly."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "CMML's monocytes are abundant but defective: despite the high monocyte count, these cells function poorly, so patients suffer recurrent bacterial infections like pneumococcal pneumonia — infection, alongside transformation, is a leading cause of death."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation marks the worst CMML: though uncommon, p53 loss predicts rapid progression to acute leukemia and resistance to hypomethylating agents, flagging patients who need transplant or trial therapy rather than standard treatment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "CMML can travel with mast-cell disease: it is a recognized partner in systemic mastocytosis with an associated hematologic neoplasm, where a shared KIT-mutant or RAS-driven clone produces both the abnormal mast cells and the monocytic leukemia."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Transplant is CMML's only cure, with a catch: allogeneic stem-cell transplant can eradicate the clone via graft-versus-leukemia, but graft-versus-host disease and relapse limit it, so it is reserved for fit, higher-risk patients."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "CMML smolders with autoimmunity: it is strikingly associated with systemic inflammatory and autoimmune disease, including vasculitis and neutrophilic dermatoses, the dysplastic clone driving an inflammatory state alongside the cytopenias."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The clone unbalances the immune system: skewed T-helper populations and cytokine output in CMML both abet the leukemic monocytes and drive the autoinflammatory complications that shadow the disease."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The clone is wired to inflame: NLRP3-driven IL-1β release from the dysplastic monocytes underlies the autoinflammatory state of CMML, linking the somatic mutations to the fevers and tissue inflammation that accompany the cytopenias."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "CMML straddles the myeloid divide: as an MDS/MPN-overlap neoplasm it shares proliferative features with classic MPNs like polycythemia vera, the proliferative subtype showing the high counts and splenomegaly of its MPN cousins."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Marrow failure poses the differential: a hypocellular CMML can resemble aplastic anemia on biopsy, so monocytosis, dysplasia, and clonal mutations are what separate a proliferating clone from an empty, failing marrow."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "CMML cells are hypersensitive to GM-CSF through JAK-STAT: the clone's exaggerated response to GM-CSF activates STAT signaling including STAT3/STAT5, a dependency that makes the JAK-STAT axis a therapeutic target."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Plentiful but dysfunctional monocytes still fail: despite the monocytosis, the cells of CMML work poorly and the disease causes neutropenia, so infection and sepsis are a leading cause of death."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A myeloid neoplasm that can clot: like other MDS/MPN-overlap disorders, CMML carries an increased thrombosis risk through its abnormal, activated myeloid cells and inflammatory milieu."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Dysfunctional myeloid cells let mold in: despite monocytosis, CMML's defective phagocytes and treatment-related neutropenia leave the lung open to invasive aspergillosis, a dangerous opportunistic infection."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow takeover and inflammation lower the count: CMML crowds the marrow while its high inflammatory cytokine output raises hepcidin and suppresses erythropoiesis, adding an anemia-of-chronic-disease component."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Transfusions and chronic anemia burden the heart: the repeated red-cell transfusions for CMML deposit iron in the myocardium while the anemia adds high-output strain, together risking heart failure."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its hypomethylating therapy deepens immune suppression: azacitidine for CMML adds to the disease's own immune dysfunction, raising the risk of Pneumocystis pneumonia."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Monocyte products injure the kidney: the marked monocytosis of CMML can infiltrate the kidney and release lysozyme that damages the renal tubules, contributing to kidney impairment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic leukemia with leukemic threat weighs on mood: the transfusion dependence, poor prognosis and risk of transformation to acute leukemia in CMML, mostly in older patients, contribute to depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its monocytes infiltrate the skin: CMML characteristically causes leukaemia cutis and is associated with Sweet syndrome, neutrophilic dermatoses that flag the underlying monocytic disorder."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Monocytic infiltration swells the gut organs: CMML commonly enlarges the spleen and liver through tissue infiltration, causing early satiety, and can produce serous effusions and ascites."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A transfusion-dependent pre-leukaemia breeds worry: the cytopenias, transfusion dependence and threat of transformation to acute leukaemia in CMML foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Its proliferative form swells the spleen: leukemic infiltration in CMML causes splenomegaly and hepatomegaly, distinguishing the myeloproliferative subtype from the dysplastic one."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its monocytes poison the tubules: the excess monocytes of CMML release lysozyme that injures the renal tubules, causing tubular dysfunction with hypokalaemia."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It can flood the body cavities: leukemic infiltration in CMML can cause pleural and pericardial effusions, and neutropenia leaves the lungs prone to infection."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Marrow disease and inflammation reach bone and joints: CMML crowds the marrow causing cytopenias, and it is notably associated with systemic inflammatory and autoimmune syndromes, including arthritis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Anaemia and infiltration burden the heart: chronic cytopenia forces a high-output state, and leukaemic monocytes can rarely infiltrate the myocardium."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can deposit beyond the marrow: myeloid (granulocytic) sarcomas and rare central-nervous-system involvement occur as CMML progresses, especially near transformation to acute leukaemia."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Hypomethylating agents lead its care: azacitidine and decitabine, with hydroxyurea for proliferative disease, are the mainstays for chronic myelomonocytic leukaemia short of transplant."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Clonal mutations inflame the arteries: the TET2 and DNMT3A mutations that drive CMML also define clonal haematopoiesis, which independently accelerates atherosclerosis through inflammatory monocytes."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Clonal monocytes injure the vessel lining: the mutant monocytes of CMML and clonal haematopoiesis promote endothelial inflammation, linking the marrow disorder to vascular disease."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Hypomethylators and JAK inhibition: azacitidine and decitabine (hypomethylating agents) are mainstays for higher-risk CMML, and JAK inhibitors are used for the proliferative, splenomegalic subtype driven by its monocytosis."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Monocytes infiltrate the liver: proliferative CMML causes hepatosplenomegaly as malignant monocytes and extramedullary haematopoiesis populate the liver lobule, adding organomegaly to its cytopenias."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "It comes with autoimmunity: CMML and the myelodysplastic syndromes are associated with systemic inflammatory and autoimmune disorders including inflammatory arthritis and vasculitis, paraneoplastic manifestations of the clonal marrow."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Monocytes inflame the arteries: CMML's expanded monocytes and its clonal-haematopoiesis biology infiltrate and inflame the arterial wall, accelerating atherosclerosis and cardiovascular risk."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "An inflammatory cytokine drive: TNF-alpha and IL-6 from the clonal monocytes drive the fevers, weight loss and cytopenias that give CMML its systemic, inflammatory character."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Clonal haematopoiesis and vascular events: the TET2- and DNMT3A-mutant clones of CMML, like clonal haematopoiesis generally, raise the risk of stroke and other cardiovascular events."
  - target: 01-human/07-system/giant-cell-arteritis
    relation: connects-to
    note: "Clonal autoinflammation: CMML and VEXAS-spectrum clonal myeloid disease associate with systemic inflammatory syndromes overlapping giant-cell arteritis, polymyalgia and other vasculitides."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Renal injury from monocytes: CMML can cause a paraneoplastic glomerulonephritis, and lysozyme released by its excess monocytes damages the renal tubules and glomerulus."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Pulmonary infiltration: CMML's excess monocytes can infiltrate the lung as leukaemic infiltrates and cause effusions around the alveoli, compromising gas exchange."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Polycomb dysregulation: loss-of-function EZH2 mutations are recurrent in CMML, disrupting epigenetic repression and conferring a poorer prognosis among its driver lesions."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "Oncometabolite target: IDH2 (and IDH1) mutations arise in a subset of CMML, generating 2-hydroxyglutarate that blocks differentiation and is targetable with IDH inhibitors."
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "Kinase at transformation: FLT3 activation, though less common than in AML, can appear as CMML progresses, marking a targetable driver of its leukaemic transformation."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory cytokine: IL-1β from the dysplastic myeloid clone drives the inflammatory bone-marrow milieu of CMML, with IL-1 blockade explored to ease its symptoms."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Marrow hypoxia: HIF-1α stabilised in the crowded, hypoxic CMML marrow supports the survival and angiogenic signalling of the dysplastic clone."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow angiogenesis: elevated VEGF increases bone-marrow microvessel density in CMML, part of the proliferative microenvironment of the disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "GM-CSF hypersensitivity: RAS-RAF-ERK hyperactivation makes CMML progenitors hypersensitive to GM-CSF, the signalling lesion behind the monocytic proliferation that defines the disease."
  - target: 01-human/03-molecular/ptpn11
    relation: connects-to
    note: "RAS-pathway mutation: PTPN11 (SHP2) and other RAS-pathway mutations are recurrent in CMML, driving the ERK signalling that fuels its myelomonocytic expansion."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Myeloid alarmin: S100A8/A9 from the expanded monocytes and neutrophils amplifies the inflammatory bone-marrow milieu of CMML, contributing to its dysplasia and systemic symptoms."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte expansion: CCL2 drives the recruitment and accumulation of monocytes that produce the persistent peripheral monocytosis defining CMML, a chemokine output of the malignant myelomonocytic clone."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK-STAT hypersensitivity: the GM-CSF hypersensitivity of CMML monocytes signals through JAK-STAT, the rationale for testing JAK inhibitors like ruxolitinib to dampen the cytokine-driven proliferation."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Mast-cell overlap: KIT-expressing mast cells are increased in some CMML, reflecting the close relationship between CMML and systemic mastocytosis in the spectrum of myeloid neoplasms."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Apoptotic therapy: CMML, like the AML it can transform into, depends on anti-apoptotic BCL-2, the rationale for adding venetoclax to hypomethylating agents to push the dysplastic monocytic clone into apoptosis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Marrow-niche dependence: CXCL12 from stromal cells anchors the CMML clone in its bone-marrow niche, an inflammatory microenvironment that both supports the abnormal monocytic proliferation and contributes to the ineffective haematopoiesis of the disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Curative transplant: allogeneic stem-cell transplant is the only curative therapy for CMML, working through donor T- and NK-cell graft-versus-leukaemia killing of the clone via perforin and granzyme."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K limb: downstream of CMML's activated RAS pathway (KRAS, PTPN11 and ERK1/2 already mapped), PIK3CA initiates PI3K signalling that provides a parallel growth-and-survival input to the monocytic clone."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival kinase: AKT relays PI3K signalling to mTOR (already mapped), sustaining the survival and cytokine-hypersensitive proliferation of CMML monocytes."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Leukaemic progression: CDKN2A loss removes the cell-cycle brake and is associated with transformation of CMML to secondary acute myeloid leukaemia."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammatory monocytosis: TLR-MyD88-NF-κB innate signalling (NF-κB already mapped) drives the inflammatory cytokine milieu and the characteristic monocytosis of CMML."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Marrow dysplasia: TGF-β signalling contributes to the marrow dysplasia and fibrosis of CMML, its suppression of normal haematopoiesis favouring the dysplastic clone."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Clonal self-renewal: aberrant Wnt/β-catenin signalling supports the self-renewal of the leukemic stem cells driving the clonal myeloproliferation of CMML."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3, abundantly expressed by the monocytic lineage that expands in CMML, supports monocyte/macrophage survival and the inflammatory phenotype of the disease."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN restraint of PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) downstream of the RAS-pathway mutations (KRAS and PTPN11 mapped) shapes proliferation in CMML."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β mapped) modulates the dysplastic haematopoiesis and marrow microenvironment of CMML."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the inflammatory bone-marrow milieu and immune surveillance of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING amplifies the inflammatory marrow microenvironment characteristic of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity drives the myeloproliferative cell-cycle progression of chronic myelomonocytic leukemia, often alongside CDKN2A loss."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the hematopoietic stem-cell quiescence and oxidative-stress handling dysregulated in chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the myeloid progenitor survival and differentiation signaling perturbed in chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family and LYN kinase signaling downstream of FLT3 and KIT (both already mapped) supports the survival of the leukemic monocytes of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and differentiation of the clonal myelomonocytic cells of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic cells of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the marrow homing and monocyte trafficking of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH1 mutation (IDH2 already mapped) contributes to the epigenetic (2-hydroxyglutarate-driven) dysregulation of a subset of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory bone-marrow microenvironment of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory microenvironment of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the myelomonocytic proliferation and immune signaling of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunosuppressive bone-marrow microenvironment of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the leukemic-stem-cell-niche and bone-marrow-microenvironment interactions of chronic myelomonocytic leukemia."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Hyperuricaemia: the increased cell turnover of proliferative chronic myelomonocytic leukaemia raises uric acid through xanthine oxidase, causing the hyperuricaemia and gout risk managed with allopurinol during cytoreduction."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Dysplastic anaemia: as a myelodysplastic/myeloproliferative overlap, CMML impairs effective erythropoiesis, lowering haemoglobin and making transfusion-dependent anaemia a common and prognostically important feature."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Monocyte dysfunction: the clonal monocytes of CMML have altered HLA-DR (MHC class II) expression and impaired antigen presentation, contributing to the immune dysfunction and the autoinflammatory conditions that accompany the disease."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Autoinflammation: CMML frequently associates with systemic autoinflammatory and autoimmune syndromes such as Sweet syndrome and vasculitis, and the balance of the anti-inflammatory IL-10 against the elevated TNF, IL-1 and IL-6 (already mapped) shapes this inflammatory dimension."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Iron cardiomyopathy: transfusion dependence in CMML deposits iron in the heart, and the resulting iron-overload cardiomyopathy, marked by troponin release, adds to the cardiac risk of these often elderly patients."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell immune dysfunction: the immune dysregulation of CMML includes impaired IL-2-driven T-cell responses alongside the monocyte dysfunction (already mapped), contributing to the infections and autoinflammatory syndromes that complicate the disease."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Anaemia and ESAs: the ineffective erythropoiesis of the dysplastic CMML marrow causes anaemia (haemoglobin already mapped), and erythropoiesis-stimulating agents raising erythropoietin are used in lower-risk disease to reduce transfusion need."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Thrombocytopenia and dysplasia: the dysplastic megakaryocytes of CMML disturb thrombopoietin-driven platelet production, contributing to the thrombocytopenia that complicates the disease and its treatment."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Autoinflammatory eicosanoids: prostaglandins from the clonal monocytes (already mapped) amplify the inflammation (IL-1, TNF and NLRP3 already mapped) behind the systemic autoinflammatory syndromes that frequently accompany CMML."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Monocyte-macrophage polarisation: IL-4 polarises the clonal monocytes and macrophages (already mapped) toward an M2 phenotype (IL-10 already mapped), shaping the inflammatory and immunosuppressive milieu of CMML."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Dysgranulopoiesis: alongside the defining monocytosis, the dysplastic neutrophils (S100A8/9 already mapped) of the marrow dysplasia reflect the myeloid lineage involvement of the MDS/MPN overlap in CMML."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Transfusional iron overload: the transfusion-dependent anaemia (haemoglobin and erythropoietin already mapped) of CMML loads the body with iron over time, an overload burden that can require chelation."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: leptin from the marrow adipose tissue of the bone-marrow (already mapped) microenvironment signals to the CMML clone, part of its metabolic niche crosstalk."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the CMML cells of the bone-marrow (already mapped) microenvironment."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 inflammatory arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the inflammatory (TNF and IL-1 already mapped) microenvironment of the monocytic proliferation of CMML."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the CMML microenvironment."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "MDS/MPN overlap: CMML is the MDS/MPN-overlap neoplasm, sharing the myeloproliferative (JAK2 already mapped) features with the classic myeloproliferative neoplasms."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Dysgranulopoiesis: the dysplastic granulocytes and the neutrophil dysplasia accompany the defining monocytosis (macrophage already mapped) of CMML."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 inflammation: the IFN-γ of the T cells (perforin already mapped) is the type-II interferon arm of the inflammatory dysregulation (IL-6 and TNF already mapped) of the MDS/MPN-overlap CMML."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory microenvironment of chronic myelomonocytic leukaemia."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) and inflammasome (NLRP3 already mapped) axis, is part of the inflammatory bone-marrow milieu of CMML."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory bone-marrow (already mapped) microenvironment of CMML."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow milieu of CMML."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory microenvironment of CMML."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the monocyte and myeloid inflammation of the CMML microenvironment."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) are part of the inflammasome-driven (NLRP3 already mapped) inflammation of CMML."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Transfusional iron: transferrin, the iron carrier, reflects the iron handling of the anaemia and the transfusion-dependent iron overload of CMML."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the inflammasome-driven marrow inflammation of CMML."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement and contact systems of the chronic inflammatory marrow niche of CMML."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Marrow fibrosis: periostin, a matricellular mediator, is part of the stromal remodelling and the marrow fibrosis (with osteopontin already mapped) of CMML."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-marrow axis: TSLP, from marrow stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the inflammatory myelomonocytic marrow microenvironment of CMML."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-marrow axis: bradykinin, via B1/B2 receptors on marrow endothelium (already mapped) and monocytic cells, amplifies the vascular permeability and the inflammatory cytokine milieu of the chronic myelomonocytic leukaemia marrow."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell/basophil marrow: histamine, from mast cells (already mapped) and basophils of the CMML myeloid output, amplifies the vascular permeability and the inflammatory milieu of the CMML marrow microenvironment."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-myeloid axis: melatonin, via MT1/MT2 receptors on CMML myeloid progenitors and monocytes (already mapped), modulates the inflammatory cytokine milieu (TNF-alpha and IL-6 already mapped) of the clonal myeloproliferation of CMML."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen-myeloid axis: testosterone, via androgen receptors on myeloid cells (already mapped) and marrow stromal cells, modulates the sex-differential CMML incidence (higher in males) and the myeloproliferative inflammatory marrow niche."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immunomodulatory prolactin: prolactin, via PRL receptors on monocytes (already mapped) and T cells (already mapped), modulates the myeloid cytokine amplification and the immune dysregulation of the chronic myelomonocytic leukaemia."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "CMML serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the CMML marrow niche; serotonin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "CMML oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates marrow niche inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "CMML vasopressin: vasopressin, via V1aR on endothelial cells (already mapped) and macrophages (already mapped), modulates marrow vascular tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "CMML selenium: selenium, as GPx in macrophages (already mapped) and monocytes (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) inflammasome-driven myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "CMML iodine: iodine-dependent thyroid hormones modulate myeloid-cell (already mapped) differentiation and NF-κB (already mapped) signalling; iodine deficiency amplifies the TNF-α (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "CMML sodium: high dietary sodium promotes Th17 polarisation and monocyte (already mapped) activation; sodium-induced NF-κB (already mapped) and TNF-α (already mapped) skewing amplifies the inflammatory myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "CMML magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and monocytes (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "CMML copper: copper, via ceruloplasmin in macrophages (already mapped) and monocytes (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) oxidative myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "CMML zinc: zinc cofactors macrophage (already mapped) and monocyte (already mapped) anti-tumour function; zinc deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "phosphorus, as ATP in macrophage (already mapped) and monocyte (already mapped), fuels myeloproliferative signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride channels on macrophage (already mapped) and monocyte (already mapped) regulate membrane potential; chloride dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "sulfur, as glutathione precursor in macrophage (already mapped) and monocyte (already mapped), counters oxidative stress; sulfur deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "CMML carbon: carbon backbone of nucleotides in macrophages (already mapped) and monocytes (already mapped) fuels myeloproliferative growth; carbon dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "CMML hydrogen: hydrogen via ROS from macrophages (already mapped) and monocytes (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "CMML nitrogen: nitrogen in DNA bases of macrophages (already mapped) and monocytes (already mapped) sustains myeloproliferative growth; nitrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "CMML pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses myeloproliferative immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "CMML glp-1: GLP-1 from macrophages (already mapped) and monocytes (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "CMML angiotensin-ii: angiotensin II on monocytes (already mapped) and macrophages (already mapped) promotes myeloproliferative skewing; angiotensin-II excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "CMML rankl: RANKL in monocytes (already mapped) and macrophages (already mapped) modulates myeloproliferative bone-marrow niche; RANKL excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "CMML fibronectin: fibronectin in monocytes (already mapped) and macrophages (already mapped) promotes myeloproliferative stroma; fibronectin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "CMML notch: Notch on monocytes (already mapped) and macrophages (already mapped) regulates myeloid cell fate; Notch dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML."
---

# Chronic Myelomonocytic Leukemia

## Overview

**Chronic myelomonocytic leukemia (CMML)** is a rare clonal hematopoietic stem cell malignancy classified by the WHO as an **MDS/MPN overlap syndrome** — uniquely combining features of myelodysplastic syndromes (cytopenias, bone marrow dysplasia) and myeloproliferative neoplasms (leukocytosis, monocytosis, splenomegaly, organomegaly). The defining hallmark is **persistent peripheral blood monocytosis** (absolute monocyte count ≥0.5×10⁹/L AND monocytes ≥10% of WBC for ≥3 months) in the absence of a reactive cause. CMML affects ~3-4 per 100,000 adults/year (predominantly ages 65-75, male predominance 2:1), carries a median overall survival of ~2-3 years, and transforms to AML in ~15-30% of patients over 5 years. The molecular landscape of CMML is dominated by mutations in DNA methylation genes (TET2 ~60%, DNMT3A ~10%, IDH1/2 ~10%), splicing factors (SRSF2 ~45%, SF3B1 ~5%), and chromatin regulators (ASXL1 ~40%) — a convergence of epigenetic and RNA processing dysregulation driving monocytic clonal expansion. Critically, ~10% of CMML-like presentations harbor **PDGFRB rearrangements** (or PDGFRA, FGFR1) → these are classified separately (MPN with eosinophilia and tyrosine kinase fusions) and are exquisitely sensitive to **imatinib** [^patnaik-2022-cmml-review] [^itzykson-2013-cmml-prognosis].

**Epidemiology and risk factors:**
- Incidence: ~1,100-1,200 cases/year USA; prevalence ~6,000; ~3-4 per 100,000 adults; median age 70-75 years; male:female ~2:1
- Risk factors: Prior chemotherapy (especially alkylating agents → therapy-related MDS/CMML); radiation; CHIP (especially DNMT3A, TET2, SRSF2 CHIP → CMML evolution); no specific environmental risk factors identified beyond those for MDS

**WHO 2022 classification of CMML:**
- **CMML-0:** <2% blasts in PB and <5% blasts in BM; lowest blast count class; lowest AML transformation risk
- **CMML-1:** 2-4% blasts in PB or 5-9% blasts in BM; intermediate risk
- **CMML-2:** 5-19% blasts in PB or 10-19% blasts in BM; OR Auer rods present; highest AML transformation risk (~30-50% at 2 years); treat as high-risk MDS or AML in some cases

**Proliferative (MP-CMML) vs. myelodysplastic (MD-CMML) subtypes:**
- **MD-CMML (WBC ≤13×10⁹/L):** Cytopenias dominant; myelodysplastic features prominent; splenomegaly mild/absent; HMA therapy preferred
- **MP-CMML (WBC >13×10⁹/L):** Monocytosis + leukocytosis dominant; splenomegaly common (in ~50-60%); KRAS/NRAS mutations enriched; ruxolitinib for splenomegaly control; hydroxyurea for cytoreduction

**Molecular landscape:**
- TET2: ~60% (most common; loss of 5-hydroxymethylcytosine → DNA hypermethylation → monocytic differentiation bias)
- SRSF2: ~45% (P95H hotspot; splicing dysregulation → monocytic fate)
- ASXL1: ~40% (PRC1.1 loss → H2AK119ub loss → aberrant HOX gene expression; poor prognosis)
- KRAS/NRAS: ~15% (RAS-MAPK → monocyte proliferation → MP-CMML phenotype)
- CBL: ~10% (E3 ubiquitin ligase; ring domain mutations → dominant negative → RAS activation)
- DNMT3A: ~10% (early epigenetic hit in CHIP → CMML progression)
- IDH1/2: ~8% (2-HG → TET2 inhibition → hypermethylation; enasidenib/ivosidenib active)
- EZH2: ~7% (PRC2 loss; adverse prognosis)
- TP53: ~5% (biallelic → ultra-high risk; rare in CMML vs. AML)
- SETBP1: ~15% (often co-mutated with ASXL1; poor prognosis; SB1-associated CMML type)

## Structure

### Bone marrow and peripheral blood findings

**Diagnostic criteria (WHO 2022):**
1. Persistent peripheral monocytosis: Absolute monocyte count ≥0.5×10⁹/L AND monocytes ≥10% of WBC for ≥3 months
2. Bone marrow dysplasia in ≥1 myeloid lineage (granulocytic, erythroid, megakaryocytic)
3. Blast count: PB <20%, BM <20%
4. No BCR-ABL1 fusion (CML must be excluded)
5. No PDGFRA, PDGFRB, FGFR1, or PCM1-JAK2 rearrangement → if present, classify as MPN with eosinophilia + RTK fusion → imatinib-sensitive
6. No PML-RARA or other AML-defining cytogenetics/fusions

**Flow cytometry diagnostic criteria:**
Monocytes: CD14+/CD16+ monocytes (non-classical + intermediate) >94% of total monocytes (in contrast to reactive monocytosis where these subsets are ~70-80%); high classical monocyte fraction is characteristic of reactive/infectious monocytosis; CMML monocytes are predominantly CD14+/CD16− classical monocytes (≥94% threshold).

**Cytogenetics:**
Normal karyotype in ~70% of CMML; abnormal in ~30%: trisomy 8 (~10%), monosomy 7/del(7q) (~10%), complex karyotype (~5%), del(20q), del(12p), del(5q); trisomy 8 and monosomy 7 are intermediate-adverse; del(17p)/monosomy 17 → TP53 loss; PDGFRB rearrangement: t(5;12)(q33;p13) → ETV6-PDGFRB fusion → eosinophilic CMML-like → imatinib 400 mg/day.

**Bone marrow biopsy/aspirate:**
Hypercellular (>70%) in MP-CMML; monocytic and granulocytic proliferation; dysplasia in ≥1 lineage; blast percentage (critical for CMML-0/1/2 classification); promonocytes (counted as blasts in CMML); plasmacytoid dendritic cell (pDC) proliferations may accompany CMML (blastic pDC neoplasm [BPDCN] may arise from CMML clones).

### Prognostic scoring systems

**CPSS (CMML-Specific Prognostic Scoring System, 2013):** [^itzykson-2013-cmml-prognosis]
Variables: WHO subtype (CMML-1/2), cytogenetic risk group (low/intermediate/high), RBC-transfusion dependence, WBC (≤13 vs. >13×10⁹/L). Scores: Low (0), Intermediate-1 (0.5-1), Intermediate-2 (1.5-2), High (≥2.5). Median OS: 84 vs. 36 vs. 21 vs. 11 months.

**CPSS-Mol (molecular CPSS, 2022):** Integrates ASXL1, NRAS/KRAS, RUNX1 mutations + cytogenetics + clinical variables → improved stratification. ASXL1 and RAS mutations → upgrade risk category; SETBP1 mutation → poor prognosis regardless of other factors.

**CMML-PM scoring:** Integrated score with WBC, BM blast %, hemoglobin, PLT → used by some centers for transplant decision.

## Function

### Monocyte biology in CMML

**CMML monocyte origin:**
CMML monocytes arise from the malignant HSC clone (proven by detection of SRSF2/TET2 mutations in sorted CD14+ monocytes, CD34+ progenitors, B-cells, T-cells in some cases — indicating oligoclonal multilineage involvement); CMML monocytes have abnormal function: impaired phagocytosis, altered cytokine secretion (high IL-6, IL-10, CCL2, M-CSF), immunosuppressive (similar to M2 macrophage phenotype); CMML monocytes produce excess GM-CSF → autocrine proliferative loop.

**Extramedullary monocytic infiltration:**
CMML monocytes infiltrate skin (leukemia cutis), liver, spleen, lymph nodes → organomegaly; splenomegaly in ~30-50% of MP-CMML; liver enlargement in ~20%; pleural/pericardial effusions in advanced disease; extramedullary infiltration → myeloid sarcoma-like presentations.

## Pathology

### Diagnosis and clinical presentation

**Clinical presentation:**
- Constitutional symptoms: Fatigue, weight loss, night sweats (~50% of patients)
- Splenomegaly: More common in MP-CMML; left upper quadrant fullness; early satiety
- Cytopenias: Anemia (most common, requiring transfusions in ~30%), thrombocytopenia, neutropenia
- Skin lesions: Leukemia cutis (papules, plaques with monocytic/myeloid infiltration); Sweet's syndrome (neutrophilic dermatosis)
- Incidental discovery: CBC showing monocytosis ≥10% of WBC → evaluation

**Diagnostic workup:**
1. CBC with differential: Monocyte count, monocyte percentage, WBC, Hgb, platelets
2. Peripheral blood smear: Promonocytes (bilobed, irregular nuclei, gray cytoplasm) vs. blasts; RBC morphology
3. Flow cytometry (peripheral blood): CD14/CD16 monocyte subset analysis → CMML classical monocytosis pattern (≥94% classical CD14+CD16− monocytes)
4. Bone marrow aspirate + biopsy: Dysplasia; blast %; monocytic infiltration; reticulin fibrosis
5. Conventional karyotype: 20-cell metaphase; FISH for PDGFRB, PDGFRA, FGFR1 if eosinophilia
6. FISH for PDGFRB rearrangement: Required if eosinophilia (absolute eosinophil count ≥1.5×10⁹/L) → if PDGFRB+, classify as MPN-eo + PDGFRB → imatinib
7. Molecular NGS: SRSF2, TET2, ASXL1, KRAS, NRAS, CBL, DNMT3A, IDH1/2, EZH2, SETBP1, TP53

**Excluding reactive monocytosis:**
Reactive causes (infection, inflammatory disease, solid tumors, auto-immune) → monocytosis may mimic CMML; differentiated by: Flow cytometry monocyte subset (reactive: <94% classical), absence of dysplasia/mutations, resolution of monocytosis with treatment of underlying condition; some infections (TB, HIV, CMV) → sustained reactive monocytosis requiring careful exclusion.

### Treatment

**Low/Intermediate-risk CMML (CPSS low/Int-1):**
- **Observation:** Asymptomatic CMML-0/1 without significant cytopenias or organomegaly; CBC monitoring q2-3 months
- **ESA (erythropoiesis-stimulating agents):** For symptomatic anemia + EPO <500 in MD-CMML; response rate ~25-35%
- **Hydroxyurea:** For cytoreduction in MP-CMML (WBC >13); rapid WBC control; does not affect mutations or alter natural history; oral daily dosing
- **Ruxolitinib (JAK1/2 inhibitor):** For MP-CMML with symptomatic splenomegaly (analogous to MF use); spleen response ~40-50%; CMML specific Phase 2 data; not FDA-approved specifically for CMML but used off-label; reduces cytokine-driven monocyte proliferation

**Higher-risk CMML (CPSS Int-2/High) or symptomatic disease:**
- **Azacitidine (75 mg/m² SC days 1-7 q28d):** Most widely used HMA; OS benefit in higher-risk CMML; ORR ~40-50% (including stable disease); CR rate ~10-15%; transfusion independence in ~25%; approved for MDS (FDA 2004) and used routinely in CMML; no dedicated FDA approval for CMML specifically
- **Decitabine (20 mg/m² IV days 1-5 q28d):** Alternative HMA; similar efficacy to azacitidine; may be preferred in some institutions; oral decitabine (decitabine + cedazuridine) available
- **Enasidenib/Ivosidenib:** For IDH2- or IDH1-mutant CMML (~8% total); FDA-approved in IDH-mutant AML; active in IDH-mutant MDS/CMML (trial ongoing); ORR ~30-40% in this subset

**Allogeneic SCT:**
Only potentially curative treatment for CMML; CPSS Int-2/High + age ≤75 + good performance status → transplant evaluation; 5-year OS ~30-40% post-transplant; reduced intensity conditioning (RIC) for older patients; relapse post-transplant remains significant (~30-40%); molecular MRD monitoring (SRSF2, TET2, ASXL1 VAF) post-transplant → guide preemptive therapy.

**PDGFRB-rearranged MPN (imatinib-sensitive):**
~10% of CMML-like presentations have PDGFRB fusions (ETV6-PDGFRB, rabaptin-5-PDGFRB, others) → constitutive PDGFRB kinase → myeloproliferation + eosinophilia; imatinib 400 mg/day → complete hematologic and cytogenetic remission in >90%; sustained long-term; this subset should not be treated as CMML → always exclude PDGFRB by FISH when eosinophilia present.

**Emerging therapies:**
- **Lenzilumab (anti-GM-CSF antibody):** GM-CSF drives CMML monocyte self-renewal → lenzilumab in Phase 2 for MP-CMML; responses in early data (~40%)
- **STP1002 (CSF1R inhibitor):** M-CSF (CSF1) drives monocyte/macrophage proliferation → CSF1R (CD115) inhibition → reduces monocyte burden; Phase 1 for CMML ongoing
- **H3B-8800 (spliceosome modulator):** Selectively toxic to SRSF2/SF3B1-mutant cells; Phase 1 for MDS/AML/CMML; modest early ORR ~12%
- **Venetoclax + azacitidine:** Active in AML/MDS → being evaluated in higher-risk CMML; early data promising
- **Trametinib (MEK inhibitor):** For KRAS/NRAS-mutant CMML; disease control in ~50% in Phase 2 data; KRAS/NRAS-mutant CMML is enriched in MP-CMML and aggressive subtypes

**AML transformation management:**
CMML → AML transformation (~15-30% at 5 years): Treat as secondary AML; CPX-351 (liposomal daunorubicin/cytarabine, AML-MRC indication): Response ~40-50%; venetoclax + azacitidine: Response ~55-65% but duration limited; allo-SCT if CR achieved; prognosis of transformed CMML AML is poor (median OS ~6-8 months with standard therapy).

## Connections

- `connects-to` → **[SRSF2](../../03-molecular/srsf2/README.md)** — SRSF2 P95H in ~45% of CMML; most common splicing factor mutation; co-occurs with TET2 (~60%) in the dominant CMML doublet; P95H alters CCNG ESE splicing → monocytic differentiation bias; SRSF2+TET2 knockin mice develop CMML-like disease with full penetrance.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A mutations in ~10% of CMML; DNMT3A is an early CHIP hit establishing pre-malignant HSC clones before SRSF2 or TET2 co-mutation; DNMT3A+TET2+SRSF2 triplet occurs in ~5% of CMML → aggressive progression; DNMT3A-CHIP → CMML progression rate ~1-2% per year.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — KRAS/NRAS mutations in ~15% of CMML; RAS activation → monocyte proliferation → MP-CMML phenotype (WBC >13×10⁹/L, splenomegaly, organomegaly); KRAS-mutant CMML is aggressive with poor HMA response; MEK inhibitor trametinib shows early activity in RAS-mutant CMML.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB promotes monocyte/macrophage survival in CMML; SRSF2/ASXL1 mutations dysregulate NF-κB pathway activity; ruxolitinib reduces cytokine-driven NF-κB signaling in MP-CMML → splenomegaly response ~40-50%; GM-CSF/M-CSF autocrine loops drive NF-κB in CMML monocytes.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — TET2 mutations in ~60% of CMML; TET2 catalyses 5-mC → 5-hmC → promoter demethylation; TET2 loss → hypermethylation of tumor suppressor promoters + monocyte progenitor expansion; TET2+SRSF2 doublet is the dominant CMML genotype; TET2 CHIP evolves to CMML at ~1% per year.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK2 V617F in ~15-20% of CMML; enriched in MP-CMML (WBC >13×10⁹/L); JAK2 V617F → STAT5 → monocyte proliferation and splenomegaly; ruxolitinib (JAK1/2 inhibitor) achieves splenomegaly response ~30-50% in MP-CMML; JAK2-mutant CMML may overlap with MDS/MPN-SF3B1.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — CMML monocytes differentiate into patrolling and pro-inflammatory macrophages; GM-CSF/M-CSF autocrine loops drive monocyte survival; tumor-associated macrophages suppress NK killing in the marrow niche; monocytosis (AMC ≥0.5×10⁹/L, ≥10% of WBC) is the defining CMML criterion.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — CMML straddles the MDS and MPN categories in its own WHO class, MDS/MPN-overlap: it has MDS dysplasia and cytopenias plus proliferative monocytosis, splenomegaly, and JAK2/RAS features, sharing biology and JAK-inhibitor responses with the myeloproliferative neoplasms.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — CMML was historically classified with the myelodysplastic syndromes and shares their dysplastic, cytopenic marrow and AML transformation risk; the WHO now separates it as MDS/MPN-overlap for its peripheral monocytosis, but azacitidine remains a shared therapy.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — CMML is a clonal bone marrow stem-cell disease: SRSF2/TET2/ASXL1-mutant progenitors expand the monocyte lineage into a hypercellular dysplastic marrow with monocytosis; marrow blasts and cytogenetics define the CPSS prognostic groups, and allogeneic transplant is the only cure.
- `connects-to` → **[AML](../aml/README.md)** — CMML is a myelodysplastic/myeloproliferative overlap that transforms to AML in ~15-20%: accumulating mutations (often ASXL1, RUNX1, or NRAS on a TET2/SRSF2 background) drive blast expansion, and CMML-derived AML carries a poor prognosis.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — CMML is defined partly by what it is NOT—Philadelphia-negative: persistent monocytosis with absent BCR-ABL1 separates CMML from chronic myeloid leukemia, a distinction made by cytogenetics/PCR that changes treatment entirely (no TKI for CMML).
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — CMML can be accompanied by clonal plasmacytoid dendritic cell proliferations: nodular aggregates of pDCs arise from the same mutated clone, a clue that monocytic and dendritic lineages share progenitors and a marker of more aggressive disease.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — CMML's myelodysplasia shows in dysplastic neutrophils alongside its defining monocytosis: hypogranular, pseudo-Pelger-Huët neutrophils reflect the clonal marrow defect, and persistent monocytosis with these features separates CMML from a reactive monocytosis.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The proliferative form of CMML enlarges the spleen: when the clone behaves myeloproliferatively (high white count), extramedullary hematopoiesis causes splenomegaly—unlike the dysplastic, cytopenic form, marking the MDS/MPN-overlap spectrum CMML spans.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — CMML and myelofibrosis are both MDS/MPN-spectrum disorders that can develop marrow fibrosis and splenomegaly: CMML is defined by monocytosis with dysplasia, myelofibrosis by JAK2/CALR with teardrop cells—but both are clonal stem-cell diseases that can transform to AML.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — CMML disrupts red cell production: as the dysplastic clone expands, anemia from ineffective erythropoiesis is common alongside monocytosis, so fatigue and transfusion dependence mark the myelodysplastic side of this MDS/MPN overlap disorder.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — RUNX1 mutations worsen CMML prognosis: this transcription-factor gene, often mutated alongside ASXL1 and SRSF2, impairs normal myeloid differentiation and predicts faster progression to AML—part of the molecular risk profile now guiding CMML treatment.
- `connects-to` → **[Essential Thrombocythemia](../essential-thrombocythemia/README.md)** — CMML and essential thrombocythemia both blur the MDS/MPN border: CMML is the overlap disorder with monocytosis and dysplasia, while ET is a classic MPN with platelet excess—yet both are clonal stem-cell diseases, and CMML's proliferative type can mimic an MPN.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — CMML disrupts platelet production: the dysplastic clone often causes thrombocytopenia from ineffective marrow output, raising bleeding risk, though some cases instead run high platelets—reflecting CMML's mixed dysplastic and proliferative nature.
- `connects-to` → **[Immune System](../immune-system/README.md)** — CMML frequently carries systemic autoimmune and inflammatory features: roughly a fifth of patients develop vasculitis, arthritis or other immune-mediated disease, because the mutant monocytes fuel inflammation—so CMML can present to rheumatology before hematology.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — CMML often infiltrates the skin: monocytic leukemia cutis and neutrophilic dermatoses like Sweet syndrome produce papules and plaques, so a skin biopsy can reveal the leukemic clone or its inflammatory companions in this monocyte-driven disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — CMML often enlarges the liver: the proliferating monocytic clone infiltrates the liver and spleen, causing hepatosplenomegaly, so organ enlargement marks the more proliferative, MPN-like end of this MDS/MPN-overlap disease.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CMML's main cure relies on T cells: allogeneic stem-cell transplant works through a graft-versus-leukemia effect in which donor cytotoxic T cells clear the clone, the only therapy that reliably eradicates this otherwise progressive disease.
- `connects-to` → **[Gout](../gout/README.md)** — CMML's high cell turnover can trigger gout: rapid production and destruction of monocytic cells floods the blood with uric acid, so hyperuricemia and gout flares accompany this and other myeloproliferative disorders.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — CMML can injure the kidney through lysozyme: its excess monocytes pour out lysozyme (muramidase) that damages the proximal tubules, causing potassium wasting and renal impairment—an unusual organ complication of monocytic leukemias.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NK cells matter in CMML, the only curable path being transplant: natural killer and donor immune cells mount a graft-versus-leukemia response, so harnessing NK-mediated surveillance is central to controlling a disease drugs only restrain.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — CMML smolders with inflammatory IL-6: its malignant monocytes and marrow pump out IL-6 and other cytokines that drive proliferation and the systemic symptoms—fevers, weight loss, and autoimmune features—that often accompany the leukemia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — CMML's failing marrow starves tissues of oxygen: as the malignant clone crowds out normal blood production, anemia develops and the blood carries less oxygen, driving the fatigue and breathlessness common in the disease.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — CMML can infiltrate and inflame the lungs: its excess monocytes seed pulmonary tissue and, with weakened immunity, leave patients prone to pneumonia, so respiratory infiltrates and infection are recurring complications.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — RAS-pathway mutations push CMML growth through mTOR: KRAS and related lesions activate downstream mTOR signaling that drives the monocyte proliferation, making this growth axis a target studied alongside hypomethylating drugs.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — CMML's anemia leads to iron overload: many patients become transfusion-dependent, and each unit delivers iron the body cannot excrete, building toxic deposits over the disease's course.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — CMML burdens the heart: chronic anemia forces high-output work, transfusional iron can deposit in the muscle, and the disease's inflammation can inflame the pericardium, together straining cardiac function.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — CMML comes with immune dysregulation via regulatory T cells: skewed Treg balance underlies the autoimmune and inflammatory complications—vasculitis and serositis—that often accompany the leukemia.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — CMML is diagnosed down the microscope: the blood smear and marrow show the persistent monocytosis that defines it, and imaging gauges the splenomegaly and any organ infiltration.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — CMML's monocytes spill lysozyme that injures the kidney tubules, wasting potassium, so an unexplained low potassium can be a curious clue to this monocytic leukemia.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — CMML can fibrose the marrow: reticulin fibrosis worsens the cytopenias and marks a more aggressive, MPN-leaning course of this MDS/MPN overlap disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows CMML's defining excess: a flood of abnormal monocytes pours from the marrow into the blood, their folded nuclei and granular cytoplasm the hallmark of this MDS/MPN overlap disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — The rogue monocytes can raise blood calcium: like activated macrophages they can make extra calcitriol, the active vitamin D, driving a paraneoplastic hypercalcemia occasionally seen in CMML.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Leukemic monocytes infiltrate the gut: CMML can seed the bowel wall and serous cavities with monocytic deposits, causing effusions and gastrointestinal involvement in advanced disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — CMML keeps strange autoimmune company: it associates with vasculitis, neutrophilic dermatoses, and the autoantibody-rich VEXAS syndrome, so systemic inflammation and autoimmunity often shadow the clonal monocytosis.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Years of transfusion overload the endocrine organs: as transfusion-dependent CMML accumulates iron, deposits in the pancreatic islets can damage insulin output toward a secondary diabetes.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Inflammation can reach the eye: the autoimmune and VEXAS-spectrum disease that overlaps CMML brings episcleritis and orbital inflammation, and leukemic infiltration can rarely involve the eye directly.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — CMML's monocytes are abundant but defective: despite the high monocyte count, these cells function poorly, so patients suffer recurrent bacterial infections like pneumococcal pneumonia — infection, alongside transformation, is a leading cause of death.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation marks the worst CMML: though uncommon, p53 loss predicts rapid progression to acute leukemia and resistance to hypomethylating agents, flagging patients who need transplant or trial therapy rather than standard treatment.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — CMML can travel with mast-cell disease: it is a recognized partner in systemic mastocytosis with an associated hematologic neoplasm, where a shared KIT-mutant or RAS-driven clone produces both the abnormal mast cells and the monocytic leukemia.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — Transplant is CMML's only cure, with a catch: allogeneic stem-cell transplant can eradicate the clone via graft-versus-leukemia, but graft-versus-host disease and relapse limit it, so it is reserved for fit, higher-risk patients.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — CMML smolders with autoimmunity: it is strikingly associated with systemic inflammatory and autoimmune disease, including vasculitis and neutrophilic dermatoses, the dysplastic clone driving an inflammatory state alongside the cytopenias.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The clone unbalances the immune system: skewed T-helper populations and cytokine output in CMML both abet the leukemic monocytes and drive the autoinflammatory complications that shadow the disease.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The clone is wired to inflame: NLRP3-driven IL-1β release from the dysplastic monocytes underlies the autoinflammatory state of CMML, linking the somatic mutations to the fevers and tissue inflammation that accompany the cytopenias.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — CMML straddles the myeloid divide: as an MDS/MPN-overlap neoplasm it shares proliferative features with classic MPNs like polycythemia vera, the proliferative subtype showing the high counts and splenomegaly of its MPN cousins.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Marrow failure poses the differential: a hypocellular CMML can resemble aplastic anemia on biopsy, so monocytosis, dysplasia, and clonal mutations are what separate a proliferating clone from an empty, failing marrow.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — CMML cells are hypersensitive to GM-CSF through JAK-STAT: the clone's exaggerated response to GM-CSF activates STAT signaling including STAT3/STAT5, a dependency that makes the JAK-STAT axis a therapeutic target.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Plentiful but dysfunctional monocytes still fail: despite the monocytosis, the cells of CMML work poorly and the disease causes neutropenia, so infection and sepsis are a leading cause of death.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A myeloid neoplasm that can clot: like other MDS/MPN-overlap disorders, CMML carries an increased thrombosis risk through its abnormal, activated myeloid cells and inflammatory milieu.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Dysfunctional myeloid cells let mold in: despite monocytosis, CMML's defective phagocytes and treatment-related neutropenia leave the lung open to invasive aspergillosis, a dangerous opportunistic infection.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow takeover and inflammation lower the count: CMML crowds the marrow while its high inflammatory cytokine output raises hepcidin and suppresses erythropoiesis, adding an anemia-of-chronic-disease component.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Transfusions and chronic anemia burden the heart: the repeated red-cell transfusions for CMML deposit iron in the myocardium while the anemia adds high-output strain, together risking heart failure.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its hypomethylating therapy deepens immune suppression: azacitidine for CMML adds to the disease's own immune dysfunction, raising the risk of Pneumocystis pneumonia.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Monocyte products injure the kidney: the marked monocytosis of CMML can infiltrate the kidney and release lysozyme that damages the renal tubules, contributing to kidney impairment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic leukemia with leukemic threat weighs on mood: the transfusion dependence, poor prognosis and risk of transformation to acute leukemia in CMML, mostly in older patients, contribute to depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its monocytes infiltrate the skin: CMML characteristically causes leukaemia cutis and is associated with Sweet syndrome, neutrophilic dermatoses that flag the underlying monocytic disorder.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Monocytic infiltration swells the gut organs: CMML commonly enlarges the spleen and liver through tissue infiltration, causing early satiety, and can produce serous effusions and ascites.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A transfusion-dependent pre-leukaemia breeds worry: the cytopenias, transfusion dependence and threat of transformation to acute leukaemia in CMML foster chronic health anxiety alongside depression.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Its proliferative form swells the spleen: leukemic infiltration in CMML causes splenomegaly and hepatomegaly, distinguishing the myeloproliferative subtype from the dysplastic one.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its monocytes poison the tubules: the excess monocytes of CMML release lysozyme that injures the renal tubules, causing tubular dysfunction with hypokalaemia.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It can flood the body cavities: leukemic infiltration in CMML can cause pleural and pericardial effusions, and neutropenia leaves the lungs prone to infection.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Marrow disease and inflammation reach bone and joints: CMML crowds the marrow causing cytopenias, and it is notably associated with systemic inflammatory and autoimmune syndromes, including arthritis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Anaemia and infiltration burden the heart: chronic cytopenia forces a high-output state, and leukaemic monocytes can rarely infiltrate the myocardium.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can deposit beyond the marrow: myeloid (granulocytic) sarcomas and rare central-nervous-system involvement occur as CMML progresses, especially near transformation to acute leukaemia.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Hypomethylating agents lead its care: azacitidine and decitabine, with hydroxyurea for proliferative disease, are the mainstays for chronic myelomonocytic leukaemia short of transplant.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Clonal mutations inflame the arteries: the TET2 and DNMT3A mutations that drive CMML also define clonal haematopoiesis, which independently accelerates atherosclerosis through inflammatory monocytes.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Clonal monocytes injure the vessel lining: the mutant monocytes of CMML and clonal haematopoiesis promote endothelial inflammation, linking the marrow disorder to vascular disease.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Hypomethylators and JAK inhibition: azacitidine and decitabine (hypomethylating agents) are mainstays for higher-risk CMML, and JAK inhibitors are used for the proliferative, splenomegalic subtype driven by its monocytosis.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Monocytes infiltrate the liver: proliferative CMML causes hepatosplenomegaly as malignant monocytes and extramedullary haematopoiesis populate the liver lobule, adding organomegaly to its cytopenias.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — It comes with autoimmunity: CMML and the myelodysplastic syndromes are associated with systemic inflammatory and autoimmune disorders including inflammatory arthritis and vasculitis, paraneoplastic manifestations of the clonal marrow.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Monocytes inflame the arteries: CMML's expanded monocytes and its clonal-haematopoiesis biology infiltrate and inflame the arterial wall, accelerating atherosclerosis and cardiovascular risk.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — An inflammatory cytokine drive: TNF-alpha and IL-6 from the clonal monocytes drive the fevers, weight loss and cytopenias that give CMML its systemic, inflammatory character.
- `connects-to` → **[Stroke](../stroke/README.md)** — Clonal haematopoiesis and vascular events: the TET2- and DNMT3A-mutant clones of CMML, like clonal haematopoiesis generally, raise the risk of stroke and other cardiovascular events.
- `connects-to` → **[Giant Cell Arteritis](../giant-cell-arteritis/README.md)** — Clonal autoinflammation: CMML and VEXAS-spectrum clonal myeloid disease associate with systemic inflammatory syndromes overlapping giant-cell arteritis, polymyalgia and other vasculitides.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Renal injury from monocytes: CMML can cause a paraneoplastic glomerulonephritis, and lysozyme released by its excess monocytes damages the renal tubules and glomerulus.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Pulmonary infiltration: CMML's excess monocytes can infiltrate the lung as leukaemic infiltrates and cause effusions around the alveoli, compromising gas exchange.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Polycomb dysregulation: loss-of-function EZH2 mutations are recurrent in CMML, disrupting epigenetic repression and conferring a poorer prognosis among its driver lesions.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — Oncometabolite target: IDH2 (and IDH1) mutations arise in a subset of CMML, generating 2-hydroxyglutarate that blocks differentiation and is targetable with IDH inhibitors.
- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — Kinase at transformation: FLT3 activation, though less common than in AML, can appear as CMML progresses, marking a targetable driver of its leukaemic transformation.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory cytokine: IL-1β from the dysplastic myeloid clone drives the inflammatory bone-marrow milieu of CMML, with IL-1 blockade explored to ease its symptoms.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Marrow hypoxia: HIF-1α stabilised in the crowded, hypoxic CMML marrow supports the survival and angiogenic signalling of the dysplastic clone.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow angiogenesis: elevated VEGF increases bone-marrow microvessel density in CMML, part of the proliferative microenvironment of the disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — GM-CSF hypersensitivity: RAS-RAF-ERK hyperactivation makes CMML progenitors hypersensitive to GM-CSF, the signalling lesion behind the monocytic proliferation that defines the disease.
- `connects-to` → **[PTPN11](../../03-molecular/ptpn11/README.md)** — RAS-pathway mutation: PTPN11 (SHP2) and other RAS-pathway mutations are recurrent in CMML, driving the ERK signalling that fuels its myelomonocytic expansion.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Myeloid alarmin: S100A8/A9 from the expanded monocytes and neutrophils amplifies the inflammatory bone-marrow milieu of CMML, contributing to its dysplasia and systemic symptoms.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 drives the recruitment and accumulation of monocytes that produce the persistent peripheral monocytosis defining CMML, a chemokine output of the malignant myelomonocytic clone.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The GM-CSF hypersensitivity of CMML monocytes signals through JAK-STAT, the rationale for testing JAK inhibitors like ruxolitinib to dampen the cytokine-driven proliferation and splenomegaly of the disease.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT-expressing mast cells are increased in some cases of CMML, reflecting the close biological relationship between CMML and systemic mastocytosis within the spectrum of myeloid neoplasms.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — CMML, like the AML it can transform into, depends on anti-apoptotic BCL-2, the rationale for adding venetoclax to hypomethylating agents to push the dysplastic monocytic clone into apoptosis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 from stromal cells anchors the CMML clone in its bone-marrow niche, an inflammatory microenvironment that both supports the abnormal monocytic proliferation and contributes to the ineffective hematopoiesis of the disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Allogeneic stem-cell transplant is the only curative therapy for CMML, working through donor T- and NK-cell graft-versus-leukemia killing of the clone via perforin and granzyme.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Downstream of CMML's activated RAS pathway (KRAS, PTPN11 and ERK1/2 already mapped), PIK3CA initiates PI3K signaling that provides a parallel growth-and-survival input to the monocytic clone.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — AKT relays PI3K signaling to mTOR (already mapped), sustaining the survival and cytokine-hypersensitive proliferation of CMML monocytes.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss removes the cell-cycle brake and is associated with transformation of CMML to secondary acute myeloid leukemia.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (NF-κB already mapped) drives the inflammatory cytokine milieu and the characteristic monocytosis of CMML.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β signaling contributes to the marrow dysplasia and fibrosis of CMML, its suppression of normal hematopoiesis favoring the dysplastic clone.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Aberrant Wnt/β-catenin signaling supports the self-renewal of the leukemic stem cells driving the clonal myeloproliferation of CMML.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3, abundantly expressed by the monocytic lineage that expands in CMML, supports monocyte/macrophage survival and the inflammatory phenotype of the disease.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN restraint of PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) downstream of the RAS-pathway mutations (KRAS and PTPN11 mapped) shapes proliferation in CMML.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β mapped) modulates the dysplastic hematopoiesis and marrow microenvironment of CMML.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the inflammatory bone-marrow milieu and immune surveillance of chronic myelomonocytic leukemia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING amplifies the inflammatory marrow microenvironment characteristic of chronic myelomonocytic leukemia.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity drives the myeloproliferative cell-cycle progression of chronic myelomonocytic leukemia, often alongside CDKN2A loss.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the hematopoietic stem-cell quiescence and oxidative-stress handling dysregulated in chronic myelomonocytic leukemia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the myeloid progenitor survival and differentiation signaling perturbed in chronic myelomonocytic leukemia.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in chronic myelomonocytic leukemia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family and LYN kinase signaling downstream of FLT3 and KIT (both already mapped) supports the survival of the leukemic monocytes of chronic myelomonocytic leukemia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and differentiation of the clonal myelomonocytic cells of chronic myelomonocytic leukemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the clonal hematopoietic cells of chronic myelomonocytic leukemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the marrow homing and monocyte trafficking of chronic myelomonocytic leukemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of chronic myelomonocytic leukemia.
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH1 mutation (IDH2 already mapped) contributes to the epigenetic (2-hydroxyglutarate-driven) dysregulation of a subset of chronic myelomonocytic leukemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of chronic myelomonocytic leukemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory bone-marrow microenvironment of chronic myelomonocytic leukemia.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory microenvironment of chronic myelomonocytic leukemia.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the myelomonocytic proliferation and immune signaling of chronic myelomonocytic leukemia.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunosuppressive bone-marrow microenvironment of chronic myelomonocytic leukemia.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the leukemic-stem-cell-niche and bone-marrow-microenvironment interactions of chronic myelomonocytic leukemia.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Hyperuricaemia: the increased cell turnover of proliferative chronic myelomonocytic leukaemia raises uric acid through xanthine oxidase, causing the hyperuricaemia and gout risk managed with allopurinol during cytoreduction.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Dysplastic anaemia: as a myelodysplastic/myeloproliferative overlap, CMML impairs effective erythropoiesis, lowering haemoglobin and making transfusion-dependent anaemia a common and prognostically important feature.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Monocyte dysfunction: the clonal monocytes of CMML have altered HLA-DR (MHC class II) expression and impaired antigen presentation, contributing to the immune dysfunction and the autoinflammatory conditions that accompany the disease.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Autoinflammation: CMML frequently associates with systemic autoinflammatory and autoimmune syndromes such as Sweet syndrome and vasculitis, and the balance of the anti-inflammatory IL-10 against the elevated TNF, IL-1 and IL-6 (already mapped) shapes this inflammatory dimension.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Iron cardiomyopathy: transfusion dependence in CMML deposits iron in the heart, and the resulting iron-overload cardiomyopathy, marked by troponin release, adds to the cardiac risk of these often elderly patients.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell immune dysfunction: the immune dysregulation of CMML includes impaired IL-2-driven T-cell responses alongside the monocyte dysfunction (already mapped), contributing to the infections and autoinflammatory syndromes that complicate the disease.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Anaemia and ESAs: the ineffective erythropoiesis of the dysplastic CMML marrow causes anaemia (haemoglobin already mapped), and erythropoiesis-stimulating agents raising erythropoietin are used in lower-risk disease to reduce transfusion need.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Thrombocytopenia and dysplasia: the dysplastic megakaryocytes of CMML disturb thrombopoietin-driven platelet production, contributing to the thrombocytopenia that complicates the disease and its treatment.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Autoinflammatory eicosanoids: prostaglandins from the clonal monocytes (already mapped) amplify the inflammation (IL-1, TNF and NLRP3 already mapped) behind the systemic autoinflammatory syndromes that frequently accompany CMML.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Monocyte-macrophage polarisation: IL-4 polarises the clonal monocytes and macrophages (already mapped) toward an M2 phenotype (IL-10 already mapped), shaping the inflammatory and immunosuppressive milieu of CMML.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Dysgranulopoiesis: alongside the defining monocytosis, the dysplastic neutrophils (S100A8/9 already mapped) of the marrow dysplasia reflect the myeloid lineage involvement of the MDS/MPN overlap in CMML.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Transfusional iron overload: the transfusion-dependent anaemia (haemoglobin and erythropoietin already mapped) of CMML loads the body with iron over time, an overload burden that can require chelation.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow-adipocyte adipokine: leptin from the marrow adipose tissue of the bone-marrow (already mapped) microenvironment signals to the CMML clone, part of its metabolic niche crosstalk.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow adipose tissue signals to the CMML cells of the bone-marrow (already mapped) microenvironment.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 inflammatory arm: IL-13, with IL-4 (already mapped), drives the M2 macrophage (already mapped) arm of the inflammatory (TNF and IL-1 already mapped) microenvironment of the monocytic proliferation of CMML.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the CMML microenvironment.
- `connects-to` → **[Myeloproliferative neoplasms](../myeloproliferative-neoplasms/README.md)** — MDS/MPN overlap: CMML is the MDS/MPN-overlap neoplasm, sharing the myeloproliferative (JAK2 already mapped) features with the classic myeloproliferative neoplasms.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Dysgranulopoiesis: the dysplastic granulocytes and the neutrophil dysplasia accompany the defining monocytosis (macrophage already mapped) of CMML.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 inflammation: the IFN-γ of the T cells (perforin already mapped) is the type-II interferon arm of the inflammatory dysregulation (IL-6 and TNF already mapped) of the MDS/MPN-overlap CMML.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory microenvironment of chronic myelomonocytic leukaemia.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) and inflammasome (NLRP3 already mapped) axis, is part of the inflammatory bone-marrow milieu of CMML.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the inflammatory bone-marrow (already mapped) microenvironment of CMML.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow milieu of CMML.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the inflammatory microenvironment of CMML.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the monocyte and myeloid inflammation of the CMML microenvironment.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) are part of the inflammasome-driven (NLRP3 already mapped) inflammation of CMML.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Transfusional iron: transferrin, the iron carrier, reflects the iron handling of the anaemia and the transfusion-dependent iron overload of CMML.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the inflammasome-driven marrow inflammation of CMML.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement and contact systems of the chronic inflammatory marrow niche of CMML.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Marrow fibrosis: periostin, a matricellular mediator, is part of the stromal remodelling and the marrow fibrosis (with osteopontin already mapped) of CMML.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-marrow axis: TSLP, from marrow stromal cells and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the inflammatory myelomonocytic marrow microenvironment of CMML.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-marrow axis: bradykinin, via B1/B2 receptors on marrow endothelium (already mapped) and monocytic cells, amplifies the vascular permeability and the inflammatory cytokine milieu of the chronic myelomonocytic leukaemia marrow.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell/basophil marrow: histamine, from mast cells (already mapped) and basophils of the CMML myeloid output, amplifies the vascular permeability and the inflammatory milieu of the CMML marrow microenvironment.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-myeloid axis: melatonin, via MT1/MT2 receptors on CMML myeloid progenitors and monocytes (already mapped), modulates the inflammatory cytokine milieu (TNF-alpha and IL-6 already mapped) of the clonal myeloproliferation of CMML.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen-myeloid axis: testosterone, via androgen receptors on myeloid cells (already mapped) and marrow stromal cells, modulates the sex-differential CMML incidence (higher in males) and the myeloproliferative inflammatory marrow niche.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immunomodulatory prolactin: prolactin, via PRL receptors on monocytes (already mapped) and T cells (already mapped), modulates the myeloid cytokine amplification and the immune dysregulation of the chronic myelomonocytic leukaemia.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — CMML serotonin: serotonin, via 5-HT receptors on macrophages (already mapped) and mast cells (already mapped), modulates the CMML marrow niche; serotonin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — CMML oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates marrow niche inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — CMML vasopressin: vasopressin, via V1aR on endothelial cells (already mapped) and macrophages (already mapped), modulates marrow vascular tone; vasopressin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — CMML selenium: selenium, as GPx in macrophages (already mapped) and monocytes (already mapped), scavenges ROS; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) inflammasome-driven myeloproliferative cascade of CMML.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — CMML iodine: iodine-dependent thyroid hormones modulate myeloid-cell (already mapped) differentiation and NF-κB (already mapped) signalling; iodine deficiency amplifies the TNF-α (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — CMML sodium: high dietary sodium promotes Th17 polarisation and monocyte (already mapped) activation; sodium-induced NF-κB (already mapped) and TNF-α (already mapped) skewing amplifies the inflammatory myeloproliferative cascade of CMML.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — CMML magnesium: magnesium cofactors kinase signalling in macrophages (already mapped) and monocytes (already mapped); magnesium deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — CMML copper: copper, via ceruloplasmin in macrophages (already mapped) and monocytes (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) oxidative myeloproliferative cascade of CMML.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — CMML zinc: zinc cofactors macrophage (already mapped) and monocyte (already mapped) anti-tumour function; zinc deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — phosphorus, as ATP in macrophage (already mapped) and monocyte (already mapped), fuels myeloproliferative signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride channels on macrophage (already mapped) and monocyte (already mapped) regulate membrane potential; chloride dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — sulfur, as glutathione precursor in macrophage (already mapped) and monocyte (already mapped), counters oxidative stress; sulfur deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — CMML carbon: carbon backbone of nucleotides in macrophages (already mapped) and monocytes (already mapped) fuels myeloproliferative growth; carbon dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — CMML hydrogen: hydrogen via ROS from macrophages (already mapped) and monocytes (already mapped) modulates oxidative stress; hydrogen excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — CMML nitrogen: nitrogen in DNA bases of macrophages (already mapped) and monocytes (already mapped) sustains myeloproliferative growth; nitrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — CMML pd-1: PD-1 on t-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses myeloproliferative immune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — CMML glp-1: GLP-1 from macrophages (already mapped) and monocytes (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — CMML angiotensin-ii: angiotensin II on monocytes (already mapped) and macrophages (already mapped) promotes myeloproliferative skewing; angiotensin-II excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — CMML rankl: RANKL in monocytes (already mapped) and macrophages (already mapped) modulates myeloproliferative bone-marrow niche; RANKL excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — CMML fibronectin: fibronectin in monocytes (already mapped) and macrophages (already mapped) promotes myeloproliferative stroma; fibronectin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of CMML.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — CMML notch: Notch on monocytes (already mapped) and macrophages (already mapped) regulates myeloid cell fate; Notch dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) myeloproliferative cascade of CMML.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^itzykson-2013-cmml-prognosis]: Itzykson R, Kosmider O, Renneville A, et al. Prognostic score including gene mutations in chronic myelomonocytic leukemia. *J Clin Oncol.* 2013;31(19):2428-2436. [doi:10.1200/JCO.2012.47.3314](https://doi.org/10.1200/JCO.2012.47.3314) · [PubMed 23690417](https://pubmed.ncbi.nlm.nih.gov/23690417/)
[^patnaik-2022-cmml-review]: Patnaik MM, Tefferi A. Chronic myelomonocytic leukemia: 2022 update on diagnosis, risk stratification and management. *Am J Hematol.* 2022;97(3):352-372. [doi:10.1002/ajh.26457](https://doi.org/10.1002/ajh.26457) · [PubMed 34958140](https://pubmed.ncbi.nlm.nih.gov/34958140/)
