---
schema: human-scale-entry/v1
id: cll
name: CLL
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Most common adult leukemia; clonal CD5+/CD19+/CD23+ B-cell malignancy; del(17p)/TP53 mutation is highest-risk. Ibrutinib and venetoclax transformed CLL; obinutuzumab+venetoclax is first-line for unfit patients; pirtobrutinib is active in covalent BTK-inhibitor-resistant CLL."
aliases: ["CLL", "chronic lymphocytic leukemia", "small lymphocytic lymphoma", "SLL", "B-CLL", "CLL/SLL", "del(17p) CLL", "del(11q) CLL"]
sources:
  - id: fischer-2019-clb-cll14
    type: peer-reviewed
    cite: "Fischer K, Al-Sawaf O, Bahlo J, et al. Venetoclax and obinutuzumab in patients with CLL and coexisting conditions. N Engl J Med. 2019;380(23):2225-2236."
    doi: "10.1056/NEJMoa1815281"
    pmid: "31166681"
    url: "https://doi.org/10.1056/NEJMoa1815281"
  - id: shanafelt-2019-ecog-e1912
    type: peer-reviewed
    cite: "Shanafelt TD, Wang XV, Kay NE, et al. Ibrutinib-rituximab or chemoimmunotherapy for chronic lymphocytic leukemia. N Engl J Med. 2019;381(5):432-443."
    doi: "10.1056/NEJMoa1817073"
    pmid: "31365801"
    url: "https://doi.org/10.1056/NEJMoa1815281"
cross_links:
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 overexpression in ~85-90% of CLL via 13q14 deletion (miR-15a/16-1 loss); venetoclax is transformative — CLL14 trial: 57% MRD-undetectable vs. 17% for chlorambucil+obinutuzumab; tumor lysis syndrome risk with initial dosing."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Del(17p13)/TP53 mutation in ~7% of newly diagnosed CLL and ~30% of relapsed CLL → resistance to chemoimmunotherapy; ibrutinib and venetoclax retain activity in TP53-mutant CLL; del(17p) CLL no longer requires allo-SCT in the targeted therapy era."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "B-cell receptor (BCR) → BTK → PLCγ → PKCβ → NF-κB → BCL-2, MYC, CXCR4 → CLL survival and proliferation; ibrutinib inhibits BTK → blocks BCR-NF-κB → CLL mobilization from lymph nodes (lymphocytosis) and apoptosis; SYK inhibitors (entospletinib) also block BCR upstream of BTK."
  - target: 01-human/03-molecular/atm
    relation: connects-to
    note: "Del(11q22.3)/ATM deletion in ~15-20% of CLL → impaired DDR → bulky adenopathy; del(11q) was high-risk in FCR era; ibrutinib/venetoclax show equal efficacy regardless of del(11q); venetoclax bypasses ATM/TP53 defects by directly engaging mitochondrial apoptosis."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "BTK is the key BCR kinase downstream of LYN/SYK; ibrutinib covalently inhibits BTK at Cys481 → blocks BCR-NF-κB → CLL mobilization and apoptosis; BTK C481S mutation confers covalent BTK inhibitor resistance → switch to non-covalent pirtobrutinib or venetoclax."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "CLL is a clonal CD5+/CD19+/CD23+ B-cell malignancy arising from antigen-experienced B cells; IGHV mutation status (>2% = mutated M-CLL; indolent) is the most important prognostic factor; tonic BCR signaling drives CLL survival; CLL cells home to BM/LN niches via CXCR4/CXCR5."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20 is dimly expressed on CLL cells limiting anti-CD20 antibody efficacy; obinutuzumab (type II, glycoengineered; superior ADCC) + venetoclax (CLL14) achieves 57% MRD-undetectable CR; rituximab + ibrutinib (ECOG E1912) FDA-approved first-line for fit CLL patients."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "CLL accumulates clonal B cells in the bone marrow, where progressive infiltration causes the anemia and thrombocytopenia that mark treatment indication; the marrow and lymph-node niches supply the stromal CD40L and CXCL12 survival signals CLL cells depend on."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly is a common sign and a treatment trigger in CLL: clonal lymphocytes infiltrate the spleen and lymph nodes, and massive or progressive splenomegaly with cytopenias from hypersplenism is one of the Hallek criteria prompting therapy."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Richter transformation is the dreaded complication of CLL — in ~5-10% the indolent clone evolves into aggressive diffuse large B-cell lymphoma, often clonally related, with a poor median survival of about a year; it is even worse when it arises on BTK-inhibitor therapy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "CLL and its tissue form SLL are a disease of the lymphatic system: clonal mature B cells accumulate in blood, bone marrow and lymph nodes, producing painless generalized lymphadenopathy and splenomegaly; the same cells circulate, so blood counts and nodes reflect one disease."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "CLL and mantle cell lymphoma are both CD5-positive mature B-cell neoplasms that can look alike on blood films but differ critically: MCL carries cyclin D1/t(11;14) and is aggressive while CLL is usually indolent—cyclin D1 and SOX11 staining separate them as prognosis diverges."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "CLL is as much an immunodeficiency as a cancer: the malignant B cells suppress normal immunity, causing hypogammaglobulinemia and T-cell dysfunction, so infection is a leading cause of death; CLL also drives autoimmune cytopenias (hemolytic anemia, ITP)."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "CLL and CML are the two chronic leukemias of opposite lineages: CLL accumulates mature B lymphocytes (smudge cells, often asymptomatic), while CML is a BCR-ABL-driven myeloid proliferation—and where CML is cured by TKIs, CLL uses BTK and BCL-2 inhibitors."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "CLL and follicular lymphoma are the commonest indolent B-cell neoplasms but distinct: CLL is a CD5+ small-lymphocyte disease driven by BCL-2 (venetoclax-targeted), while follicular lymphoma is BCL2-translocated and germinal-center-derived—both treatable but incurable."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CLL famously exhausts cytotoxic T cells, undermining immunity: the leukemic B cells suppress and dysregulate CD8 T cells, causing the immunodeficiency and infection risk that dominate CLL—and this exhaustion is why CAR-T works less well in CLL."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "CLL is a mature B-cell cancer that fails to become a plasma cell: the malignant clone is frozen short of antibody-secreting differentiation, so it accumulates uselessly while normal antibody production falls—causing the hypogammaglobulinemia behind CLL infections."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Hypogammaglobulinemia drives infection risk in CLL: the leukemic B cells crowd out and suppress normal plasma cells, so IgG levels fall and patients suffer recurrent bacterial infections—a leading cause of death, sometimes needing immunoglobulin replacement."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "CLL cripples natural killer and overall immune surveillance: beyond low antibodies, the disease impairs NK and T-cell function, raising infection and second-cancer risk—and this immune dysfunction, not just tumor bulk, shapes the prognosis and treatment of CLL."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "CLL commonly turns the immune system against red cells: autoimmune hemolytic anemia, driven by the dysregulated CLL clone, destroys erythrocytes—so a positive Coombs test and brisk hemolysis are characteristic autoimmune complications of the leukemia."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "PD-1 blockade is studied in CLL, especially Richter transformation: the leukemic microenvironment exhausts T cells via PD-1, so checkpoint inhibition aims to restore anti-tumor immunity where CLL becomes an aggressive large-cell lymphoma."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "CLL frequently causes immune thrombocytopenia: the disordered clone produces antiplatelet autoantibodies that destroy platelets, so unexplained low platelets in CLL may be autoimmune rather than marrow failure—a distinction that changes treatment."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "CLL's targeted drugs strain the heart: BTK inhibitors like ibrutinib commonly cause atrial fibrillation and hypertension, so cardiac monitoring shapes drug choice—a reminder that even well-tolerated targeted therapy carries organ-specific risk."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "CLL is as much an immune-failure disease as a cancer: the malignant B cells expand regulatory T cells and disarm normal immunity, so infections—not the leukemia itself—are a leading cause of death, and vaccines respond poorly."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "CLL can transform into aggressive lymphoma (Richter), sometimes of Hodgkin type: a sudden change with rapid nodal growth and B-symptoms signals transformation to Hodgkin or diffuse large B-cell lymphoma, a feared and hard-to-treat turn."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "CLL cells survive inside a protective niche of nurse-like cells: monocyte-derived macrophages in the marrow and lymph nodes shield leukemic B cells from death, so disrupting this microenvironment is a strategy to overcome drug resistance."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "CLL leans on IL-4 for survival: this T-cell cytokine signals leukemic B cells to resist apoptosis and upregulate Bcl-2, part of the external support that keeps these slow-dividing cells alive far longer than they should."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "CLL cells make their own VEGF to stay alive: autocrine VEGF signaling props up anti-apoptotic proteins and feeds the vascular niche in marrow and nodes, adding angiogenesis to the survival tricks behind this indolent leukemia."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "B-cell receptor signaling in CLL runs on calcium: when the receptor fires, BTK and PLC drive a calcium flux that keeps the leukemic cells alive—the very pathway BTK inhibitors interrupt to treat the disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "CLL infiltrates the liver as it spreads: leukemic B cells lodge in the liver causing hepatomegaly, part of the organ enlargement that, with big nodes and spleen, marks advancing disease and guides staging."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CLL cripples dendritic cells and immunity: the leukemia impairs antigen-presenting cell function and broader immune defense, so infections—not the leukemia itself—are a leading cause of death and the reason vaccines respond poorly."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "CLL turns the skin cancer-prone: its deep immune suppression sharply raises the risk of aggressive skin cancers, and the leukemia itself can infiltrate the skin (leukemia cutis), so dermatologic surveillance matters."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "CLL leaves patients short of neutrophils: marrow crowding and treatment cause neutropenia, and with few of these first-responder cells the infections that dominate CLL's course take hold."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "CLL cells secrete immunosuppressive IL-10: this cytokine damps the surrounding immune response, helping the leukemia evade attack while deepening the broader immune failure that leaves patients vulnerable to infection."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging stages and watches CLL: CT photons measure the enlarged lymph nodes and spleen, and a PET scan flags Richter's transformation into aggressive lymphoma."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "CLL's venetoclax can trigger tumor lysis: the BCL-2 drug kills cells so fast that potassium and phosphate flood the blood, so the dose is ramped up slowly to avoid the metabolic crisis."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "CLL proliferates in lymph-node centers: the tumor cells gather in 'proliferation centers' within nodes, fed by helper T-cell signals, the engine that resists therapies aimed only at circulating cells."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows CLL's fragile cells: small mature lymphocytes with clumped chromatin so delicate they rupture on the slide into the 'smudge cells' that are a clue to the diagnosis on a blood smear."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "CLL leaves the lungs defenseless: by crippling normal antibody production it brings recurrent pneumonias, and leukemic cells can themselves infiltrate the lung, infection being a leading cause of death."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Potent new CLL drugs can trigger tumor lysis: venetoclax kills the cells so fast that phosphorus and other contents spill into the blood, so the drug is started in careful dose steps to avoid the metabolic crisis."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "CLL warps antibody both ways: the failing immune system makes too little normal immunoglobulin, leaving patients prone to infection, while anti-CD20 antibodies like obinutuzumab are a core treatment and autoantibodies can attack the blood cells."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "CLL drops the platelets by two routes: marrow crowding by leukemic cells and an autoimmune destruction (ITP) both lower the count, and a falling platelet level marks advancing disease that prompts treatment."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney bears the brunt of tumor lysis: as venetoclax bursts the leukemic mass, surging uric acid and phosphate crystallize in the renal tubules, threatening acute kidney injury that hydration and rasburicase guard against."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "CLL leaves patients open to pneumococcus: the leukemic B cells crowd out normal antibody production, and the hypogammaglobulinemia invites recurrent pneumonia and sepsis from encapsulated bacteria — why pneumococcal vaccination and immunoglobulin replacement are used."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH1 is a recurrent driver in CLL: activating NOTCH1 mutations in roughly a tenth of cases sustain the leukemic cells and mark adverse prognosis and resistance to CD20 antibodies, helping risk-stratify whom to treat more aggressively."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "CLL's broken immunity lets other cancers through: with weakened tumor surveillance, patients face a markedly higher risk of second malignancies including melanoma, which tends to behave more aggressively, so regular skin checks are advised."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "The microenvironment feeds the leukemia with BAFF: stromal and accessory cells supply this survival cytokine (with APRIL) to keep CLL cells alive, one of the external lifelines that anti-apoptotic therapy aims to cut."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "Skin cancers run rampant in CLL: the immune deficit drives numerous, recurrent, and more aggressive basal cell and other non-melanoma skin cancers, making dermatologic surveillance a routine part of care."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The leukemia grooms its own helpers: in the lymph-node proliferation centers, CLL cells recruit and corrupt T-helper cells to support their growth, while the resulting T-cell dysfunction fuels the infections that often kill."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12 anchors CLL in its sanctuaries: stromal cells secrete this chemokine to draw leukemic cells via CXCR4 into protective marrow and lymph-node niches, where survival signals shield them from therapy — a homing axis targeted to mobilize the cells."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Treatment deepens the immune defect: the purine analogues and other therapies for CLL suppress T cells enough that opportunistic Pneumocystis pneumonia becomes a risk, which is why prophylaxis is given during these regimens."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "BTK inhibitors trade one risk for another: ibrutinib used to treat CLL provokes atrial fibrillation and, through off-target platelet effects, both raises embolic stroke risk and complicates the anticoagulation meant to prevent it."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 keeps the leukemic B cell alive: microenvironmental cytokines activate STAT3 in CLL cells, supporting their survival and helping the clone resist apoptosis within its protective lymph-node niche."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Immune failure is the great killer: progressive hypogammaglobulinemia and T-cell dysfunction, deepened by therapy, leave CLL patients prone to overwhelming infection, and sepsis is a leading cause of death."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The malignancy and its drugs raise clot risk: CLL carries an increased venous thromboembolism rate, and some targeted agents add their own thrombotic and bleeding hazards on top of the disease's baseline risk."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its immune defects and BTK inhibitors invite mold: CLL's profound immune dysfunction, and ibrutinib in particular, are associated with invasive aspergillosis, a serious opportunistic infection in these patients."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Anti-CD20 therapy can reactivate it: the rituximab and obinutuzumab used against CLL deplete B cells and can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede treatment."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Marrow takeover and inflammation lower the count: alongside its autoimmune hemolytic anemia, CLL crowds the marrow and drives inflammation that suppresses erythropoiesis into an anemia of chronic disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its BTK-inhibitor therapy strains the heart: ibrutinib, a mainstay for CLL, causes atrial fibrillation, hypertension and cardiotoxicity that can precipitate heart failure."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its immune defect reawakens shingles: the profound immunodeficiency of CLL and its therapies readily reactivate latent varicella-zoster as herpes zoster, prompting prophylaxis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A chronic, watch-and-wait cancer weighs on mood: the indolent but incurable course, repeated relapses and lifelong monitoring of CLL carry a substantial burden of depression and anxiety."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its BTK inhibitors stress the heart: ibrutinib used for CLL causes atrial fibrillation, hypertension, ventricular arrhythmia and bleeding, the main cardiovascular toxicities limiting its long-term use."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Immune dysregulation shows on the skin: CLL brings leukaemia cutis, exaggerated insect-bite reactions and a markedly raised risk of skin cancers from its underlying immune defect."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Watchful waiting breeds worry: living with an untreated but incurable leukaemia under active surveillance, plus the infection risk of its immune defect, fosters chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Failing antibodies leave the lungs exposed: the hypogammaglobulinaemia of CLL drives recurrent bacterial respiratory infections, a leading cause of morbidity, and the lung can be infiltrated."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its therapy can flood the kidney: venetoclax can trigger tumour lysis syndrome with acute kidney injury at initiation, and autoimmune or infiltrative processes occasionally affect the kidneys."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It enlarges the liver and weighs on the gut: hepatomegaly and bulky abdominal nodes cause early satiety and discomfort, and CLL can drive autoimmune liver involvement."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Marrow crowding and drugs reach bone and muscle: CLL infiltrates the bone marrow to cause cytopenias, and BTK inhibitors like ibrutinib commonly cause arthralgia and muscle cramps."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It occasionally invades the nervous system: leptomeningeal CLL and Richter transformation can affect the CNS, and autoimmune and infectious neuropathies complicate its immune dysregulation."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its autoimmunity can strike glands: the immune dysregulation that causes autoimmune haemolysis in CLL can extend to autoimmune thyroid disease, and steroids used for cytopenias bring endocrine effects."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "A chemo-free targeted era: BTK inhibitors (ibrutinib, acalabrutinib) and the BCL-2 inhibitor venetoclax have replaced chemotherapy as first-line treatment for chronic lymphocytic leukaemia."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "A fellow indolent B-cell cancer: like Waldenström macroglobulinaemia, CLL is a slow-growing mature B-cell malignancy driven by B-cell-receptor signalling and treated with BTK inhibitors."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "A driver of dangerous transformation: EBV is implicated in the Richter transformation of CLL into aggressive diffuse large B-cell lymphoma, and reactivates under its immune suppression."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "From chemo to targeted era: the old FCR regimen — fludarabine, cyclophosphamide and rituximab — cured some fit CLL patients but is now largely replaced by BTK and BCL-2 inhibitors that spare cytotoxic toxicity."
  - target: 03-medicine/01-modern/13-cancer/car-t
    relation: connects-to
    note: "Engineered cells for refractory disease: CD19-directed CAR-T achieves remissions in CLL that has failed BTK and BCL-2 inhibitors, extending cellular immunotherapy to the commonest adult leukaemia."
  - target: 01-human/07-system/aml
    relation: connects-to
    note: "Chronic lymphoid versus acute myeloid: CLL is an indolent accumulation of mature B-cells often watched for years, whereas AML is an explosive proliferation of myeloid blasts demanding urgent therapy — the slow and fast extremes of leukaemia."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Opposite tempos of B-cell cancer: CLL is the most indolent mature B-cell malignancy, accumulating cells over years, whereas Burkitt lymphoma is the fastest-growing human tumour—the extremes of the B-cell spectrum."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Two clonal B-lineage cancers of the marrow: CLL accumulates mature B-lymphocytes while multiple myeloma accumulates antibody-secreting plasma cells, distinct stops along B-cell maturation."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It infiltrates the liver: CLL cells pack the portal tracts of the hepatic lobule, contributing to the hepatomegaly and organ infiltration of advanced disease."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Immunodeficiency and infection: CLL's hypogammaglobulinaemia and blunted vaccine responses make COVID-19 and other infections more severe and prolonged—infection being a leading cause of death."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Targeted-therapy cardiotoxicity: the BTK inhibitors (ibrutinib) that treat CLL commonly cause atrial fibrillation and hypertension, disturbing the cardiac conduction system."
  - target: 01-human/07-system/nsclc
    relation: connects-to
    note: "A second-cancer risk: the immune dysfunction of CLL raises the risk of second cancers, including aggressive skin cancers and lung cancer such as NSCLC."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Therapy-related marrow failure: chemoimmunotherapy for CLL and underlying clonal haematopoiesis raise the risk of treatment-related myelodysplastic syndrome and secondary AML."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BCR survival signal: PI3K-AKT signalling downstream of the B-cell receptor sustains CLL cell survival, the axis blocked by PI3K-delta inhibitors complementing BTK-targeted therapy."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "A distinguishing marker: unlike mantle cell lymphoma, CLL does not overexpress cyclin D1, a key feature separating the two CD5-positive B-cell neoplasms at diagnosis."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes in CLL and is implicated in its aggressive Richter transformation to diffuse large B-cell lymphoma."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Supportive microenvironment: IL-6 from the lymph-node and marrow niche supports CLL cell survival and proliferation, part of the protective stromal milieu the cells depend on."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Microenvironment cytokine: TNF-α produced within the CLL microenvironment acts as an autocrine and paracrine growth factor sustaining the malignant B-cell clone."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3Kδ signalling: chronic B-cell-receptor signalling through PI3K (especially the δ isoform) sustains CLL cell survival, the target of idelalisib and duvelisib in the disease."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "Richter transformation: MYC activation drives the transformation of CLL into aggressive diffuse large B-cell lymphoma (Richter syndrome), a feared and poor-prognosis evolution of the disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Nurse-like cells: CLL cells secrete CCL2 that recruits and polarises the nurse-like macrophages of the lymph-node niche, which in turn protect the leukaemic cells from apoptosis."
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "Splicing-factor mutation: recurrent SF3B1 mutations corrupt mRNA splicing across the genome in CLL and mark a more aggressive, adverse-prognosis subset of the disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "BCR-proximal kinase: Src-family kinases such as LYN transduce the chronic B-cell-receptor signal upstream of BTK that drives CLL survival, the proximal node of the pathway BTK inhibitors target downstream."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "Telomere dynamics: short telomeres and telomerase reactivation mark the genomically unstable, rapidly proliferating CLL clones and correlate with the adverse outcomes of the disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement-dependent killing: anti-CD20 antibodies (rituximab, obinutuzumab) kill CLL cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex, one of the immune effector mechanisms of antibody therapy in the disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cellular immunotherapy: NK-cell antibody-dependent cytotoxicity against anti-CD20-coated cells and CD19 CAR-T cells both kill CLL through perforin and granzyme, the cellular effector arm complementing antibody and small-molecule therapy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Survival signalling: tonic B-cell-receptor signalling through PI3K-AKT inactivates FOXO transcription factors to promote CLL-cell survival, part of the BCR-dependence that BTK and PI3K inhibitors exploit."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PI3Kδ target: PTEN normally restrains the PI3K-AKT signalling (PIK3CA and AKT already mapped) that drives CLL survival, the very pathway the PI3Kδ inhibitors idelalisib and duvelisib block in this leukaemia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "BCR-RAS arm: alongside BTK and SRC (both mapped), the B-cell receptor activates the RAS-MAPK-ERK cascade in CLL, a parallel proliferative limb of the antigen-driven signalling that sustains the malignant clone."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Richter transformation: deletion of the CDKN2A locus is a recurrent event in the transformation of CLL to aggressive diffuse large B-cell lymphoma, releasing the cell-cycle brake on the cyclin-D1 axis already mapped."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR survival signalling: MyD88-dependent Toll-like-receptor signalling (recurrently mutated in a CLL subset) amplifies NF-κB (already mapped) survival signals in the leukemic B cells of CLL."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Microenvironmental cytokines: cytokine signalling through JAK-STAT3 (STAT3 already mapped) from the supportive lymphoid niche promotes the survival of CLL cells outside the circulation."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "BCR growth axis: the PI3K-AKT-mTOR pathway (AKT and PIK3CA already mapped) downstream of tonic B-cell-receptor signalling drives the growth and survival of CLL cells."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β within the lymph-node and marrow microenvironment modulates CLL-cell survival and the immune suppression characteristic of the disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 in the CLL microenvironment supports leukemic B-cell survival and stromal interactions."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING links the genomic instability of CLL to its inflammatory and immune microenvironment."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antileukemic immune response and immune-evasion balance of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling normally restrains B-cell proliferation, a brake that the CLL clone evades within its supportive microenvironment."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-cyclin-D activity (cyclin-D1 already mapped) drives the proliferative-centre expansion of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the survival and Wnt/β-catenin signaling of the chronic lymphocytic leukemia clone."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins shape the inflammatory nurse-like-cell-supported microenvironment of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in chronic lymphocytic leukemia, relevant given the prognostic weight of TP53 status."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic lymph-node and marrow niche supports the survival and metabolic adaptation of chronic lymphocytic leukemia cells."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy supports the survival and drug resistance of chronic lymphocytic leukemia cells, a candidate therapeutic vulnerability."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation and microenvironment interactions of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the lymph-node homing and microenvironment of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the tumor-microenvironment and lymphoid-niche interactions of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the tumor-immune microenvironment of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory microenvironment of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the microenvironment and stromal interactions of chronic lymphocytic leukemia."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune dysfunction: CLL causes profound immune impairment with hypogammaglobulinaemia (IgG already mapped) and defective antigen presentation, driving the infections that are a leading cause of death, while antigen presentation also underlies CAR-T therapy."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Autoimmune haemolysis: CLL is complicated by autoimmune haemolytic anaemia and pure red-cell aplasia, lowering haemoglobin through immune-mediated red-cell destruction (complement C3 already mapped) beyond marrow infiltration alone."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell dysfunction: the T cells in CLL are functionally exhausted with impaired IL-2 responses, a defect that both weakens immunity and is engineered around by CD19-directed CAR-T cells."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "BTK-inhibitor cardiotoxicity: ibrutinib and other BTK inhibitors (BTK already mapped) cause atrial fibrillation and, rarely, ventricular arrhythmia, and troponin elevation can mark the myocardial injury of this major class toxicity in CLL."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Venetoclax tumour lysis: the rapid killing of the large CLL burden by venetoclax (BCL-2 already mapped) releases purines that xanthine oxidase converts to uric acid, causing the tumour-lysis syndrome that mandates careful ramp-up dosing."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Immunodeficiency: the hypogammaglobulinaemia of CLL depletes normal immunoglobulins including secretory IgA (IgG already mapped), impairing mucosal defence and causing the recurrent infections that are a leading cause of death."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia and transfusion: the marrow infiltration and the autoimmune haemolytic anaemia of CLL (haemoglobin already mapped) cause anaemia often needing transfusion, whose repeated support can load the body with iron."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune skewing: IL-13, with IL-4 (already mapped), reflects the type-2 cytokine skewing of the immune dysfunction of CLL, part of the T-cell dysregulation that accompanies the malignant B-cell clone."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Microenvironment inflammation: prostaglandins in the lymph-node and marrow microenvironment (IL-6 and TNF already mapped) support the survival signalling of the CLL clone, part of the pro-tumour inflammatory milieu."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and contributes, with the marrow infiltration and the autoimmune haemolysis, to the anaemia (haemoglobin already mapped) of CLL."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow adipose niche: the marrow adipocytes and their adipokine leptin engage in crosstalk with the CLL clone, part of the bone-marrow microenvironment (CXCL12 already mapped) that supports its survival."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow and stromal adipose tissue signals to the CLL cells, part of the metabolic microenvironment sustaining the clone."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the metabolic microenvironment sustaining the CLL clone."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Immunosuppressive Tregs: the expanded regulatory T cells contribute to the immunosuppression (IL-10 already mapped) and the immune dysfunction (hypogammaglobulinaemia, immunoglobulin already mapped) of chronic lymphocytic leukaemia."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Haemolytic and marrow anaemia: the iron of the autoimmune haemolytic anaemia (haemoglobin already mapped) and the anaemia of the marrow infiltration (hepcidin already mapped) of chronic lymphocytic leukaemia."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Immunosuppressive Tregs: the expanded regulatory T cells (IL-10 already mapped) contribute to the immunosuppression and the immune dysfunction (hypogammaglobulinaemia) of chronic lymphocytic leukaemia."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "ADCC effectors: the NK cells mediate the antibody-dependent cellular cytotoxicity of the anti-CD20 (already mapped) antibodies (rituximab, obinutuzumab) against the CLL B cells (already mapped)."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Indolent mature-B relative: chronic lymphocytic leukaemia and Waldenström macroglobulinaemia are indolent mature-B-cell neoplasms (the BCR/BTK already mapped signalling), overlapping in the BTK-inhibitor therapy."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 antitumour arm: the IFN-γ of the T and NK (already mapped) cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the immune dysfunction and CAR-T of CLL."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of chronic lymphocytic leukaemia."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of chronic lymphocytic leukaemia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of chronic lymphocytic leukaemia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the chronic-lymphocytic-leukaemia microenvironment."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of chronic lymphocytic leukaemia."
---

# CLL

## Overview

**Chronic lymphocytic leukemia (CLL)** is the most common leukemia in adults in the Western world, characterized by the progressive accumulation of mature, functionally incompetent B lymphocytes (CD5+/CD19+/CD23+/CD20dim) in the blood, bone marrow, and lymphoid organs. CLL and **small lymphocytic lymphoma (SLL)** represent the same biological entity distinguished by the site of predominant involvement (blood/BM vs. lymph node). The disease has a highly variable course: approximately one-third of patients never require treatment, while others progress rapidly and require early intervention. The introduction of **BTK inhibitors (ibrutinib)** and **BCL-2 inhibitors (venetoclax)** has transformed CLL therapy — achieving unprecedented rates of MRD-undetectable remissions and extending survival even in high-risk disease (del17p, TP53-mutant) [^fischer-2019-clb-cll14].

**Epidemiology:**
- ~20,000 new cases/year in the US; median age at diagnosis ~70 years; M:F ~2:1
- Most common adult leukemia in the West; rare in East Asia (genetic/environmental differences)
- 5-year survival: ~83% overall; improving rapidly with targeted therapy
- Familial aggregation: ~10% of CLL patients have a first-degree relative with CLL or related B-cell lymphoproliferative disorder; GWAS identified >40 susceptibility loci

**Indications for treatment (Hallek 2018 criteria):**
- Symptomatic progressive marrow failure (Hgb <10 or plt <100)
- Massive or progressive splenomegaly/lymphadenopathy (>10 cm or rapidly growing)
- Progressive lymphocytosis (>50% increase/2 months or LDT <6 months)
- Autoimmune cytopenia not responsive to corticosteroids
- Constitutional symptoms (>10% weight loss, fatigue, fevers, night sweats)
- NOT: absolute lymphocyte count alone, even if very high

## Structure

### CLL cell biology and immunophenotype

**Immunophenotype (Matutes score ≥3/5 = CLL):**
- CD19+, CD5+, CD23+ (cardinal triad)
- CD20dim (low CD20 expression — key therapeutic implication: anti-CD20 antibodies less effective than in DLBCL)
- FMC7−, CD79b− or dim; sIg dim (kappa or lambda light chain restriction)
- Ki-67 low (<5%): Non-proliferating circulating cells; proliferation occurs in lymph node pseudo-follicles ("proliferation centers")

**CLL cell of origin:** Antigen-experienced B cells (post-germinal center or marginal zone B cells); BCR stereotypy in ~30% of CLL → antigen-driven selection

**IGHV mutation status:**
- **IGHV mutated (M-CLL):** >2% somatic mutations from germline; post-GC B cell; indolent; time to first treatment longer; better OS
- **IGHV unmutated (U-CLL):** <2% somatic mutations; pre-GC B cell; more aggressive; BCR signaling more active; ibrutinib especially effective; U-CLL has higher NF-κB activity

### Prognostic classification

**Binet staging (clinical, Europe):**
- A: <3 lymph node areas; Hgb ≥10, plt ≥100 — favorable
- B: ≥3 lymph node areas; Hgb ≥10, plt ≥100 — intermediate
- C: Hgb <10 or plt <100 — poor (treatment indication)

**Rai staging (clinical, US):**
- 0: Lymphocytosis only → low risk
- I: Lymphocytosis + lymphadenopathy → intermediate
- II: + splenomegaly/hepatomegaly → intermediate
- III: + anemia (Hgb <11) → high risk
- IV: + thrombocytopenia (plt <100) → high risk

**Genomic prognostic factors:**
- **Del(13q14) (~55%):** Most common; miR-15a/miR-16-1 deletion → BCL-2 upregulation; isolated del(13q) = best prognosis
- **Trisomy 12 (~15%):** CD38+, stereotyped BCR; intermediate prognosis; often NOTCH1-mutant
- **Del(11q22.3)/ATM (~15%):** Bulky adenopathy; intermediate-poor in FCR era; equal ibrutinib/venetoclax outcomes
- **Del(17p13.1)/TP53 mutation (~7% newly diagnosed, ~30% relapsed):** Highest risk; no meaningful response to chemoimmunotherapy; requires targeted therapy

**FISH panel standard:** del(13q), trisomy 12, del(11q), del(17p) — performed at diagnosis for staging and treatment planning.

**Recurrent somatic mutations:**
- NOTCH1 (~15%): Trisomy 12-associated; ibrutinib-resistant biology; aggressive
- SF3B1 (~15%): Splicing factor; intermediate risk; del(11q) co-occurrence
- TP53 (see above)
- ATM (~15%)
- BIRC3 (~5%): NF-κB pathway; high-risk in chemotherapy era; ibrutinib active

## Function

### Normal B-cell biology and CLL pathogenesis

**B-cell receptor signaling:**
BCR cross-linking → LYN (SRC kinase) phosphorylates CD79a/b ITAMs → SYK recruitment → PI3Kδ → PDK1 → AKT; BTK (Bruton's tyrosine kinase) → PLCγ2 → IP3/DAG → Ca²⁺ flux/PKC → NF-κB → B-cell activation, proliferation, and survival gene expression (BCL-2, MYC, CXCR4). In CLL, tonic BCR signaling (antigen-independent) sustains this pathway constitutively → ibrutinib exploits this dependency.

**Tumor microenvironment:**
- CLL cells require stromal signals for survival; nurse-like cells (NLCs, CD68+) secrete CXCL12/CXCL13 → CXCR4/CXCR5 on CLL cells → homing to marrow and lymph node niches
- CD4+ T cells provide CD40L → CD40 signaling → CLL proliferation in lymph node pseudo-follicles
- Ibrutinib → reduced CXCR4 expression → CLL mobilization from niches → transient lymphocytosis (not progression)

## Pathology

### Staging and complications

**Complications of CLL:**
- **Autoimmune hemolytic anemia (AIHA, ~10%):** Warm IgG AIHA; treat with corticosteroids (prednisone) → rituximab; ibrutinib may worsen AIHA
- **Immune thrombocytopenia (ITP):** Autoimmune platelet destruction
- **Richter's transformation (~5-10%):** CLL → DLBCL (most common) or Hodgkin lymphoma; DLBCL transformation = poor prognosis (median OS ~1 year); ibrutinib-related Richter's has even worse outcome
- **Hypogammaglobulinemia:** Progressive with disease; IV immunoglobulin (IVIG) if recurrent bacterial infections
- **Infections:** Recurrent bacterial (pneumococcal pneumonia), PCP risk during treatment, CMV reactivation with ibrutinib

### Treatment

**Watch-and-wait:**
- Appropriate for asymptomatic low/intermediate-stage CLL; no survival benefit to early treatment in asymptomatic patients (CLL1, French CLL trial)

**First-line treatment for fit patients (without del17p/TP53mut):**
- **Ibrutinib + rituximab (ECOG-E1912 trial):** [^shanafelt-2019-ecog-e1912] PFS at 3 years 89% vs. 73% vs. FCR; ibrutinib-rituximab superior to FCR in all molecular subgroups; FDA approved 2019
- **Venetoclax + obinutuzumab (CLL14 trial):** [^fischer-2019-clb-cll14] Fixed-duration 12 cycles; MRD-undetectable in 57% of PB; 3-year PFS 81% vs. 49% vs. chlorambucil+obinutuzumab; FDA approved 2019 for unfit patients; increasingly used in fit patients for fixed-duration appeal
- **Acalabrutinib ± obinutuzumab (ELEVATE-TN):** Acalabrutinib (more selective BTK inhibitor) + obinutuzumab PFS 90% at 4 years vs. 47% for chlorambucil+obinutuzumab; fewer cardiac adverse events than ibrutinib (less off-target ITK inhibition → fewer AF events)

**First-line for del(17p)/TP53-mutant:**
- Ibrutinib, acalabrutinib, venetoclax+obinutuzumab — all active; no FCR or BR (alkylating agents/anti-CD20 alone)
- Consider allo-SCT for young fit patients with del(17p) achieving deep remission (decreasing role with targeted therapies)

**Relapsed/refractory:**
- **Venetoclax + rituximab (MURANO trial):** R/R CLL; fixed-duration 2 years; MRD-undetectable 62%; superior to BR; FDA approved 2018
- **BTK C481S mutation (ibrutinib resistance, ~50%):** Cysteine-481 in BTK covalent binding site → ibrutinib cannot covalently bind → resistance; switch to venetoclax; novel non-covalent BTK inhibitors (pirtobrutinib, BRUIN trial → ORR 73% in BTK-inhibitor-resistant CLL) or BTK degraders (ARQ531, BGB-16673) active against C481S
- **Pirtobrutinib (Jaypirca):** Non-covalent BTK inhibitor; FDA approved 2023 for relapsed/refractory CLL after ≥2 lines including BTK inhibitor + BCL-2 inhibitor; ORR 82% in BTK-inhibitor-resistant CLL (BRUIN trial)

**Richter's transformation:**
- R-CHOP ± ibrutinib; CAR-T cells in clinical trials; checkpoint inhibitors (pembrolizumab, nivolumab) for DLBCL transformation; prognosis poor (median OS ~7-12 months)

## Connections

- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 overexpression in ~85-90% of CLL (via 13q14 deletion affecting miR-15a/16-1 which suppress BCL-2); venetoclax (BCL-2 inhibitor) is transformative in CLL — CLL14 trial: 57% MRD-undetectable in PB at end of treatment vs. 17% for chlorambucil+obinutuzumab; tumor lysis syndrome risk in initial dosing.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Del(17p13)/TP53 mutation in ~7% of treatment-naive CLL, ~30% of relapsed CLL → loss of p53-mediated apoptosis → resistance to alkylating agents and anti-CD20 chemoimmunotherapy; ibrutinib and venetoclax retain activity in TP53-mutant CLL; del(17p) CLL no longer requires allo-SCT with targeted agents.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — B-cell receptor (BCR) → BTK → PLCγ → PKCβ → NF-κB → BCL-2, MYC, CXCR4 → CLL survival and proliferation; ibrutinib inhibits BTK → blocks BCR-NF-κB → CLL mobilization from lymph nodes (lymphocytosis) and apoptosis; SYK inhibitors (entospletinib) also block BCR upstream of BTK.
- `connects-to` → **[ATM](../../03-molecular/atm/README.md)** — ATM deletion at del(11q22.3) in ~15-20% of CLL → impaired DDR → bulky adenopathy; in FCR era, del(11q) was high-risk; ibrutinib/venetoclax show equal efficacy in del(11q) CLL compared to non-del(11q); ATM and TP53 pathway defects are mechanistically distinct — venetoclax bypasses both by directly triggering apoptosis.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK is the key BCR kinase downstream of LYN/SYK; ibrutinib covalently inhibits BTK at Cys481 → blocks BCR-NF-κB → CLL mobilization and apoptosis; BTK C481S mutation confers covalent BTK inhibitor resistance → switch to non-covalent pirtobrutinib or venetoclax.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — CLL is a clonal CD5+/CD19+/CD23+ B-cell malignancy arising from antigen-experienced B cells; IGHV mutation status (>2% = mutated M-CLL; indolent) is the most important prognostic factor; tonic BCR signaling drives CLL survival; CLL cells home to BM/LN niches via CXCR4/CXCR5.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20 is dimly expressed on CLL cells limiting anti-CD20 antibody efficacy; obinutuzumab (type II, glycoengineered; superior ADCC) + venetoclax (CLL14) achieves 57% MRD-undetectable CR; rituximab + ibrutinib (ECOG E1912) FDA-approved first-line for fit CLL patients.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — CLL accumulates clonal B cells in the bone marrow, where progressive infiltration causes the anemia and thrombocytopenia that mark treatment indication; the marrow and lymph-node niches supply the stromal CD40L and CXCL12 survival signals CLL cells depend on.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly is a common sign and a treatment trigger in CLL: clonal lymphocytes infiltrate the spleen and lymph nodes, and massive or progressive splenomegaly with cytopenias from hypersplenism is one of the Hallek criteria prompting therapy.
- `connects-to` → **[Diffuse Large B-Cell Lymphoma](../dlbcl/README.md)** — Richter transformation is the dreaded complication of CLL — in ~5-10% the indolent clone evolves into aggressive diffuse large B-cell lymphoma, often clonally related, with a poor median survival of about a year; it is even worse when it arises on BTK-inhibitor therapy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — CLL and its tissue form SLL are a disease of the lymphatic system: clonal mature B cells accumulate in blood, bone marrow and lymph nodes, producing painless generalized lymphadenopathy and splenomegaly; the same cells circulate, so blood counts and nodes reflect one disease.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — CLL and mantle cell lymphoma are both CD5-positive mature B-cell neoplasms that can look alike on blood films but differ critically: MCL carries cyclin D1/t(11;14) and is aggressive while CLL is usually indolent—cyclin D1 and SOX11 staining separate them as prognosis diverges.
- `connects-to` → **[Immune System](../immune-system/README.md)** — CLL is as much an immunodeficiency as a cancer: the malignant B cells suppress normal immunity, causing hypogammaglobulinemia and T-cell dysfunction, so infection is a leading cause of death; CLL also drives autoimmune cytopenias (hemolytic anemia, ITP).
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — CLL and CML are the two chronic leukemias of opposite lineages: CLL accumulates mature B lymphocytes (smudge cells, often asymptomatic), while CML is a BCR-ABL-driven myeloid proliferation—and where CML is cured by TKIs, CLL uses BTK and BCL-2 inhibitors.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — CLL and follicular lymphoma are the commonest indolent B-cell neoplasms but distinct: CLL is a CD5+ small-lymphocyte disease driven by BCL-2 (venetoclax-targeted), while follicular lymphoma is BCL2-translocated and germinal-center-derived—both treatable but incurable.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CLL famously exhausts cytotoxic T cells, undermining immunity: the leukemic B cells suppress and dysregulate CD8 T cells, causing the immunodeficiency and infection risk that dominate CLL—and this exhaustion is why CAR-T works less well in CLL.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — CLL is a mature B-cell cancer that fails to become a plasma cell: the malignant clone is frozen short of antibody-secreting differentiation, so it accumulates uselessly while normal antibody production falls—causing the hypogammaglobulinemia behind CLL infections.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Hypogammaglobulinemia drives infection risk in CLL: the leukemic B cells crowd out and suppress normal plasma cells, so IgG levels fall and patients suffer recurrent bacterial infections—a leading cause of death, sometimes needing immunoglobulin replacement.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — CLL cripples natural killer and overall immune surveillance: beyond low antibodies, the disease impairs NK and T-cell function, raising infection and second-cancer risk—and this immune dysfunction, not just tumor bulk, shapes the prognosis and treatment of CLL.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — CLL commonly turns the immune system against red cells: autoimmune hemolytic anemia, driven by the dysregulated CLL clone, destroys erythrocytes—so a positive Coombs test and brisk hemolysis are characteristic autoimmune complications of the leukemia.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — PD-1 blockade is studied in CLL, especially Richter transformation: the leukemic microenvironment exhausts T cells via PD-1, so checkpoint inhibition aims to restore anti-tumor immunity where CLL becomes an aggressive large-cell lymphoma.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — CLL frequently causes immune thrombocytopenia: the disordered clone produces antiplatelet autoantibodies that destroy platelets, so unexplained low platelets in CLL may be autoimmune rather than marrow failure—a distinction that changes treatment.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — CLL's targeted drugs strain the heart: BTK inhibitors like ibrutinib commonly cause atrial fibrillation and hypertension, so cardiac monitoring shapes drug choice—a reminder that even well-tolerated targeted therapy carries organ-specific risk.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — CLL is as much an immune-failure disease as a cancer: the malignant B cells expand regulatory T cells and disarm normal immunity, so infections—not the leukemia itself—are a leading cause of death, and vaccines respond poorly.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — CLL can transform into aggressive lymphoma (Richter), sometimes of Hodgkin type: a sudden change with rapid nodal growth and B-symptoms signals transformation to Hodgkin or diffuse large B-cell lymphoma, a feared and hard-to-treat turn.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — CLL cells survive inside a protective niche of nurse-like cells: monocyte-derived macrophages in the marrow and lymph nodes shield leukemic B cells from death, so disrupting this microenvironment is a strategy to overcome drug resistance.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — CLL leans on IL-4 for survival: this T-cell cytokine signals leukemic B cells to resist apoptosis and upregulate Bcl-2, part of the external support that keeps these slow-dividing cells alive far longer than they should.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — CLL cells make their own VEGF to stay alive: autocrine VEGF signaling props up anti-apoptotic proteins and feeds the vascular niche in marrow and nodes, adding angiogenesis to the survival tricks behind this indolent leukemia.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — B-cell receptor signaling in CLL runs on calcium: when the receptor fires, BTK and PLC drive a calcium flux that keeps the leukemic cells alive—the very pathway BTK inhibitors interrupt to treat the disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — CLL infiltrates the liver as it spreads: leukemic B cells lodge in the liver causing hepatomegaly, part of the organ enlargement that, with big nodes and spleen, marks advancing disease and guides staging.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — CLL cripples dendritic cells and immunity: the leukemia impairs antigen-presenting cell function and broader immune defense, so infections—not the leukemia itself—are a leading cause of death and the reason vaccines respond poorly.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — CLL turns the skin cancer-prone: its deep immune suppression sharply raises the risk of aggressive skin cancers, and the leukemia itself can infiltrate the skin (leukemia cutis), so dermatologic surveillance matters.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — CLL leaves patients short of neutrophils: marrow crowding and treatment cause neutropenia, and with few of these first-responder cells the infections that dominate CLL's course take hold.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — CLL cells secrete immunosuppressive IL-10: this cytokine damps the surrounding immune response, helping the leukemia evade attack while deepening the broader immune failure that leaves patients vulnerable to infection.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging stages and watches CLL: CT photons measure the enlarged lymph nodes and spleen, and a PET scan flags Richter's transformation into aggressive lymphoma.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — CLL's venetoclax can trigger tumor lysis: the BCL-2 drug kills cells so fast that potassium and phosphate flood the blood, so the dose is ramped up slowly to avoid the metabolic crisis.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — CLL proliferates in lymph-node centers: the tumor cells gather in 'proliferation centers' within nodes, fed by helper T-cell signals, the engine that resists therapies aimed only at circulating cells.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows CLL's fragile cells: small mature lymphocytes with clumped chromatin so delicate they rupture on the slide into the 'smudge cells' that are a clue to the diagnosis on a blood smear.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — CLL leaves the lungs defenseless: by crippling normal antibody production it brings recurrent pneumonias, and leukemic cells can themselves infiltrate the lung, infection being a leading cause of death.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Potent new CLL drugs can trigger tumor lysis: venetoclax kills the cells so fast that phosphorus and other contents spill into the blood, so the drug is started in careful dose steps to avoid the metabolic crisis.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — CLL warps antibody both ways: the failing immune system makes too little normal immunoglobulin, leaving patients prone to infection, while anti-CD20 antibodies like obinutuzumab are a core treatment and autoantibodies can attack the blood cells.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — CLL drops the platelets by two routes: marrow crowding by leukemic cells and an autoimmune destruction (ITP) both lower the count, and a falling platelet level marks advancing disease that prompts treatment.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney bears the brunt of tumor lysis: as venetoclax bursts the leukemic mass, surging uric acid and phosphate crystallize in the renal tubules, threatening acute kidney injury that hydration and rasburicase guard against.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — CLL leaves patients open to pneumococcus: the leukemic B cells crowd out normal antibody production, and the hypogammaglobulinemia invites recurrent pneumonia and sepsis from encapsulated bacteria — why pneumococcal vaccination and immunoglobulin replacement are used.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH1 is a recurrent driver in CLL: activating NOTCH1 mutations in roughly a tenth of cases sustain the leukemic cells and mark adverse prognosis and resistance to CD20 antibodies, helping risk-stratify whom to treat more aggressively.
- `connects-to` → **[Melanoma](../melanoma/README.md)** — CLL's broken immunity lets other cancers through: with weakened tumor surveillance, patients face a markedly higher risk of second malignancies including melanoma, which tends to behave more aggressively, so regular skin checks are advised.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — The microenvironment feeds the leukemia with BAFF: stromal and accessory cells supply this survival cytokine (with APRIL) to keep CLL cells alive, one of the external lifelines that anti-apoptotic therapy aims to cut.
- `connects-to` → **[Basal Cell Carcinoma](../basal-cell-carcinoma/README.md)** — Skin cancers run rampant in CLL: the immune deficit drives numerous, recurrent, and more aggressive basal cell and other non-melanoma skin cancers, making dermatologic surveillance a routine part of care.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The leukemia grooms its own helpers: in the lymph-node proliferation centers, CLL cells recruit and corrupt T-helper cells to support their growth, while the resulting T-cell dysfunction fuels the infections that often kill.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 anchors CLL in its sanctuaries: stromal cells secrete this chemokine to draw leukemic cells via CXCR4 into protective marrow and lymph-node niches, where survival signals shield them from therapy — a homing axis targeted to mobilize the cells.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Treatment deepens the immune defect: the purine analogues and other therapies for CLL suppress T cells enough that opportunistic Pneumocystis pneumonia becomes a risk, which is why prophylaxis is given during these regimens.
- `connects-to` → **[Stroke](../stroke/README.md)** — BTK inhibitors trade one risk for another: ibrutinib used to treat CLL provokes atrial fibrillation and, through off-target platelet effects, both raises embolic stroke risk and complicates the anticoagulation meant to prevent it.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 keeps the leukemic B cell alive: microenvironmental cytokines activate STAT3 in CLL cells, supporting their survival and helping the clone resist apoptosis within its protective lymph-node niche.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Immune failure is the great killer: progressive hypogammaglobulinemia and T-cell dysfunction, deepened by therapy, leave CLL patients prone to overwhelming infection, and sepsis is a leading cause of death.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The malignancy and its drugs raise clot risk: CLL carries an increased venous thromboembolism rate, and some targeted agents add their own thrombotic and bleeding hazards on top of the disease's baseline risk.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its immune defects and BTK inhibitors invite mold: CLL's profound immune dysfunction, and ibrutinib in particular, are associated with invasive aspergillosis, a serious opportunistic infection in these patients.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Anti-CD20 therapy can reactivate it: the rituximab and obinutuzumab used against CLL deplete B cells and can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede treatment.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Marrow takeover and inflammation lower the count: alongside its autoimmune hemolytic anemia, CLL crowds the marrow and drives inflammation that suppresses erythropoiesis into an anemia of chronic disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its BTK-inhibitor therapy strains the heart: ibrutinib, a mainstay for CLL, causes atrial fibrillation, hypertension and cardiotoxicity that can precipitate heart failure.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its immune defect reawakens shingles: the profound immunodeficiency of CLL and its therapies readily reactivate latent varicella-zoster as herpes zoster, prompting prophylaxis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A chronic, watch-and-wait cancer weighs on mood: the indolent but incurable course, repeated relapses and lifelong monitoring of CLL carry a substantial burden of depression and anxiety.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its BTK inhibitors stress the heart: ibrutinib used for CLL causes atrial fibrillation, hypertension, ventricular arrhythmia and bleeding, the main cardiovascular toxicities limiting its long-term use.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Immune dysregulation shows on the skin: CLL brings leukaemia cutis, exaggerated insect-bite reactions and a markedly raised risk of skin cancers from its underlying immune defect.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Watchful waiting breeds worry: living with an untreated but incurable leukaemia under active surveillance, plus the infection risk of its immune defect, fosters chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Failing antibodies leave the lungs exposed: the hypogammaglobulinaemia of CLL drives recurrent bacterial respiratory infections, a leading cause of morbidity, and the lung can be infiltrated.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its therapy can flood the kidney: venetoclax can trigger tumour lysis syndrome with acute kidney injury at initiation, and autoimmune or infiltrative processes occasionally affect the kidneys.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It enlarges the liver and weighs on the gut: hepatomegaly and bulky abdominal nodes cause early satiety and discomfort, and CLL can drive autoimmune liver involvement.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Marrow crowding and drugs reach bone and muscle: CLL infiltrates the bone marrow to cause cytopenias, and BTK inhibitors like ibrutinib commonly cause arthralgia and muscle cramps.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It occasionally invades the nervous system: leptomeningeal CLL and Richter transformation can affect the CNS, and autoimmune and infectious neuropathies complicate its immune dysregulation.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its autoimmunity can strike glands: the immune dysregulation that causes autoimmune haemolysis in CLL can extend to autoimmune thyroid disease, and steroids used for cytopenias bring endocrine effects.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — A chemo-free targeted era: BTK inhibitors (ibrutinib, acalabrutinib) and the BCL-2 inhibitor venetoclax have replaced chemotherapy as first-line treatment for chronic lymphocytic leukaemia.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — A fellow indolent B-cell cancer: like Waldenström macroglobulinaemia, CLL is a slow-growing mature B-cell malignancy driven by B-cell-receptor signalling and treated with BTK inhibitors.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — A driver of dangerous transformation: EBV is implicated in the Richter transformation of CLL into aggressive diffuse large B-cell lymphoma, and reactivates under its immune suppression.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — From chemo to targeted era: the old FCR regimen — fludarabine, cyclophosphamide and rituximab — cured some fit CLL patients but is now largely replaced by BTK and BCL-2 inhibitors that spare cytotoxic toxicity.
- `connects-to` → **[CAR-T](../../../03-medicine/01-modern/13-cancer/car-t/README.md)** — Engineered cells for refractory disease: CD19-directed CAR-T achieves remissions in CLL that has failed BTK and BCL-2 inhibitors, extending cellular immunotherapy to the commonest adult leukaemia.
- `connects-to` → **[AML](../aml/README.md)** — Chronic lymphoid versus acute myeloid: CLL is an indolent accumulation of mature B-cells often watched for years, whereas AML is an explosive proliferation of myeloid blasts demanding urgent therapy — the slow and fast extremes of leukaemia.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Opposite tempos of B-cell cancer: CLL is the most indolent mature B-cell malignancy, accumulating cells over years, whereas Burkitt lymphoma is the fastest-growing human tumour—the extremes of the B-cell spectrum.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Two clonal B-lineage cancers of the marrow: CLL accumulates mature B-lymphocytes while multiple myeloma accumulates antibody-secreting plasma cells, distinct stops along B-cell maturation.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It infiltrates the liver: CLL cells pack the portal tracts of the hepatic lobule, contributing to the hepatomegaly and organ infiltration of advanced disease.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Immunodeficiency and infection: CLL's hypogammaglobulinaemia and blunted vaccine responses make COVID-19 and other infections more severe and prolonged—infection being a leading cause of death.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Targeted-therapy cardiotoxicity: the BTK inhibitors (ibrutinib) that treat CLL commonly cause atrial fibrillation and hypertension, disturbing the cardiac conduction system.
- `connects-to` → **[NSCLC](../nsclc/README.md)** — A second-cancer risk: the immune dysfunction of CLL raises the risk of second cancers, including aggressive skin cancers and lung cancer such as NSCLC.
- `connects-to` → **[MDS](../mds/README.md)** — Therapy-related marrow failure: chemoimmunotherapy for CLL and underlying clonal haematopoiesis raise the risk of treatment-related myelodysplastic syndrome and secondary AML.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BCR survival signal: PI3K-AKT signalling downstream of the B-cell receptor sustains CLL cell survival, the axis blocked by PI3K-delta inhibitors complementing BTK-targeted therapy.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — A distinguishing marker: unlike mantle cell lymphoma, CLL does not overexpress cyclin D1, a key feature separating the two CD5-positive B-cell neoplasms at diagnosis.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic driver: EZH2 overexpression silences tumour-suppressor genes in CLL and is implicated in its aggressive Richter transformation to diffuse large B-cell lymphoma.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Supportive microenvironment: IL-6 from the lymph-node and marrow niche supports CLL cell survival and proliferation, part of the protective stromal milieu the cells depend on.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Microenvironment cytokine: TNF-α produced within the CLL microenvironment acts as an autocrine and paracrine growth factor sustaining the malignant B-cell clone.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3Kδ signalling: chronic B-cell-receptor signalling through PI3K (especially the δ isoform) sustains CLL cell survival, the target of idelalisib and duvelisib in the disease.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — Richter transformation: MYC activation drives the transformation of CLL into aggressive diffuse large B-cell lymphoma (Richter syndrome), a feared and poor-prognosis evolution of the disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Nurse-like cells: CLL cells secrete CCL2 that recruits and polarises the nurse-like macrophages of the lymph-node niche, which in turn protect the leukaemic cells from apoptosis.
- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — Recurrent SF3B1 mutations corrupt mRNA splicing across the genome in CLL and mark a more aggressive, adverse-prognosis subset—one of the recurrently mutated drivers that refine risk beyond the classic cytogenetic markers.
- `connects-to` → **[Src kinase](../../03-molecular/src-kinase/README.md)** — Src-family kinases such as LYN transduce the chronic B-cell-receptor signal upstream of BTK that drives CLL survival, the proximal node of the very pathway that BTK inhibitors block further downstream.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — Short telomeres and telomerase reactivation mark the genomically unstable, rapidly proliferating CLL clones and correlate with the adverse outcomes and richter-transformation risk of the disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Anti-CD20 antibodies (rituximab, obinutuzumab) kill CLL cells partly through complement-dependent cytotoxicity, fixing C3 and the membrane-attack complex, one of the immune effector mechanisms of antibody therapy in the disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — NK-cell antibody-dependent cytotoxicity against anti-CD20-coated cells and CD19 CAR-T cells both kill CLL through perforin and granzyme, the cellular effector arm complementing antibody and small-molecule therapy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — Tonic B-cell-receptor signaling through PI3K-AKT inactivates FOXO transcription factors to promote CLL-cell survival, part of the BCR-dependence that BTK and PI3K inhibitors exploit.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN normally restrains the PI3K-AKT signaling (PIK3CA and AKT already mapped) that drives CLL survival, the very pathway the PI3Kδ inhibitors idelalisib and duvelisib block in this leukemia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Alongside BTK and SRC (both mapped), the B-cell receptor activates the RAS-MAPK-ERK cascade in CLL, a parallel proliferative limb of the antigen-driven signaling that sustains the malignant clone.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Deletion of the CDKN2A locus is a recurrent event in the transformation of CLL to aggressive diffuse large B-cell lymphoma, releasing the cell-cycle brake on the cyclin-D1 axis already mapped.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — MyD88-dependent Toll-like-receptor signaling (recurrently mutated in a CLL subset) amplifies NF-κB (already mapped) survival signals in the leukemic B cells of CLL.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Cytokine signaling through JAK-STAT3 (STAT3 already mapped) from the supportive lymphoid niche promotes the survival of CLL cells outside the circulation.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The PI3K-AKT-mTOR pathway (AKT and PIK3CA already mapped) downstream of tonic B-cell-receptor signaling drives the growth and survival of CLL cells.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β within the lymph-node and marrow microenvironment modulates CLL-cell survival and the immune suppression characteristic of the disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 in the CLL microenvironment supports leukemic B-cell survival and stromal interactions.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING links the genomic instability of CLL to its inflammatory and immune microenvironment.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antileukemic immune response and immune-evasion balance of chronic lymphocytic leukemia.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling normally restrains B-cell proliferation, a brake that the CLL clone evades within its supportive microenvironment.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-cyclin-D activity (cyclin-D1 already mapped) drives the proliferative-centre expansion of chronic lymphocytic leukemia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the survival and Wnt/β-catenin signaling of the chronic lymphocytic leukemia clone.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins shape the inflammatory nurse-like-cell-supported microenvironment of chronic lymphocytic leukemia.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — MDM2-mediated p53 degradation (p53 already mapped) restrains apoptosis in chronic lymphocytic leukemia, relevant given the prognostic weight of TP53 status.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic lymph-node and marrow niche supports the survival and metabolic adaptation of chronic lymphocytic leukemia cells.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy supports the survival and drug resistance of chronic lymphocytic leukemia cells, a candidate therapeutic vulnerability.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of chronic lymphocytic leukemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation and microenvironment interactions of chronic lymphocytic leukemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling (CXCL12/CXCR4 already mapped) participates in the lymph-node homing and microenvironment of chronic lymphocytic leukemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic dysregulation of chronic lymphocytic leukemia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the tumor-microenvironment and lymphoid-niche interactions of chronic lymphocytic leukemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the tumor-immune microenvironment of chronic lymphocytic leukemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory microenvironment of chronic lymphocytic leukemia.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling downstream of the B-cell receptor participates in the survival signaling of chronic lymphocytic leukemia.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine (CD39/CD73-adenosine) signaling participates in the immunosuppressive tumor microenvironment of chronic lymphocytic leukemia.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the microenvironment and stromal interactions of chronic lymphocytic leukemia.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune dysfunction: CLL causes profound immune impairment with hypogammaglobulinaemia (IgG already mapped) and defective antigen presentation, driving the infections that are a leading cause of death, while antigen presentation also underlies CAR-T therapy.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Autoimmune haemolysis: CLL is complicated by autoimmune haemolytic anaemia and pure red-cell aplasia, lowering haemoglobin through immune-mediated red-cell destruction (complement C3 already mapped) beyond marrow infiltration alone.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell dysfunction: the T cells in CLL are functionally exhausted with impaired IL-2 responses, a defect that both weakens immunity and is engineered around by CD19-directed CAR-T cells.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — BTK-inhibitor cardiotoxicity: ibrutinib and other BTK inhibitors (BTK already mapped) cause atrial fibrillation and, rarely, ventricular arrhythmia, and troponin elevation can mark the myocardial injury of this major class toxicity in CLL.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Venetoclax tumour lysis: the rapid killing of the large CLL burden by venetoclax (BCL-2 already mapped) releases purines that xanthine oxidase converts to uric acid, causing the tumour-lysis syndrome that mandates careful ramp-up dosing.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Immunodeficiency: the hypogammaglobulinaemia of CLL depletes normal immunoglobulins including secretory IgA (IgG already mapped), impairing mucosal defence and causing the recurrent infections that are a leading cause of death.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia and transfusion: the marrow infiltration and the autoimmune haemolytic anaemia of CLL (haemoglobin already mapped) cause anaemia often needing transfusion, whose repeated support can load the body with iron.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune skewing: IL-13, with IL-4 (already mapped), reflects the type-2 cytokine skewing of the immune dysfunction of CLL, part of the T-cell dysregulation that accompanies the malignant B-cell clone.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Microenvironment inflammation: prostaglandins in the lymph-node and marrow microenvironment (IL-6 and TNF already mapped) support the survival signalling of the CLL clone, part of the pro-tumour inflammatory milieu.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron and contributes, with the marrow infiltration and the autoimmune haemolysis, to the anaemia (haemoglobin already mapped) of CLL.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow adipose niche: the marrow adipocytes and their adipokine leptin engage in crosstalk with the CLL clone, part of the bone-marrow microenvironment (CXCL12 already mapped) that supports its survival.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine microenvironment: adiponectin, with leptin (already mapped), from the marrow and stromal adipose tissue signals to the CLL cells, part of the metabolic microenvironment sustaining the clone.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipokine milieu: resistin, with leptin and adiponectin (already mapped), completes the marrow-adipocyte adipokine signalling of the metabolic microenvironment sustaining the CLL clone.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Immunosuppressive Tregs: the expanded regulatory T cells contribute to the immunosuppression (IL-10 already mapped) and the immune dysfunction (hypogammaglobulinaemia, immunoglobulin already mapped) of chronic lymphocytic leukaemia.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Haemolytic and marrow anaemia: the iron of the autoimmune haemolytic anaemia (haemoglobin already mapped) and the anaemia of the marrow infiltration (hepcidin already mapped) of chronic lymphocytic leukaemia.
- `connects-to` → **[Regulatory T-cell](../../04-cellular/regulatory-t-cell/README.md)** — Immunosuppressive Tregs: the expanded regulatory T cells (IL-10 already mapped) contribute to the immunosuppression and the immune dysfunction (hypogammaglobulinaemia) of chronic lymphocytic leukaemia.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — ADCC effectors: the NK cells mediate the antibody-dependent cellular cytotoxicity of the anti-CD20 (already mapped) antibodies (rituximab, obinutuzumab) against the CLL B cells (already mapped).
- `connects-to` → **[Waldenström macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Indolent mature-B relative: chronic lymphocytic leukaemia and Waldenström macroglobulinaemia are indolent mature-B-cell neoplasms (the BCR/BTK already mapped signalling), overlapping in the BTK-inhibitor therapy.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 antitumour arm: the IFN-γ of the T and NK (already mapped) cells (perforin already mapped) is the type-II interferon arm of the anti-tumour immunity, relevant to the immune dysfunction and CAR-T of CLL.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune microenvironment of chronic lymphocytic leukaemia.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment of chronic lymphocytic leukaemia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of chronic lymphocytic leukaemia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory dimension of the chronic-lymphocytic-leukaemia microenvironment.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of chronic lymphocytic leukaemia.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^fischer-2019-clb-cll14]: Fischer K, Al-Sawaf O, Bahlo J, et al. Venetoclax and obinutuzumab in patients with CLL and coexisting conditions. *N Engl J Med.* 2019;380(23):2225-2236. [doi:10.1056/NEJMoa1815281](https://doi.org/10.1056/NEJMoa1815281) · [PubMed 31166681](https://pubmed.ncbi.nlm.nih.gov/31166681/)
[^shanafelt-2019-ecog-e1912]: Shanafelt TD, Wang XV, Kay NE, et al. Ibrutinib-rituximab or chemoimmunotherapy for chronic lymphocytic leukemia. *N Engl J Med.* 2019;381(5):432-443. [doi:10.1056/NEJMoa1817073](https://doi.org/10.1056/NEJMoa1817073) · [PubMed 31365801](https://pubmed.ncbi.nlm.nih.gov/31365801/)
