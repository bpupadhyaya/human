---
schema: human-scale-entry/v1
id: aml
name: AML
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Clonal myeloid malignancy; key drivers: FLT3-ITD/TKD (~30%), NPM1 (~30%), DNMT3A (~20%), IDH1/2 (~20%), and KMT2A rearrangements. Venetoclax+azacitidine is frontline for unfit patients; midostaurin (FLT3) and enasidenib/ivosidenib (IDH2/1) are approved targeted therapies."
aliases: ["acute myeloid leukemia", "AML", "acute myelogenous leukemia", "myeloid leukemia", "APL", "acute promyelocytic leukemia", "FLT3-mutant AML", "IDH-mutant AML", "NPM1-mutant AML"]
sources:
  - id: dinardo-2020-viale-a
    type: peer-reviewed
    cite: "DiNardo CD, Jonas BA, Pullarkat V, et al. Azacitidine and venetoclax in previously untreated acute myeloid leukemia. N Engl J Med. 2020;383(7):617-629."
    doi: "10.1056/NEJMoa2012971"
    pmid: "32786187"
    url: "https://doi.org/10.1056/NEJMoa2012971"
  - id: stone-2017-midostaurin
    type: peer-reviewed
    cite: "Stone RM, Mandrekar SJ, Sanford BL, et al. Midostaurin plus chemotherapy for acute myeloid leukemia with a FLT3 mutation. N Engl J Med. 2017;377(5):454-464."
    doi: "10.1056/NEJMoa1614359"
    pmid: "28644114"
    url: "https://doi.org/10.1056/NEJMoa1614359"
  - id: stein-2017-enasidenib
    type: peer-reviewed
    cite: "Stein EM, DiNardo CD, Pollyea DA, et al. Enasidenib in mutant IDH2 relapsed or refractory acute myeloid leukemia. Blood. 2017;130(6):722-731."
    doi: "10.1182/blood-2017-04-779405"
    pmid: "28588020"
    url: "https://doi.org/10.1182/blood-2017-04-779405"
cross_links:
  - target: 01-human/03-molecular/flt3
    relation: connects-to
    note: "FLT3-ITD (~25-30%) and FLT3-TKD (~7-10%) are the most common actionable AML mutations; midostaurin + 7+3 chemotherapy improves OS in FLT3-mutant AML (RATIFY trial); gilteritinib improves OS vs. salvage chemo in R/R FLT3-mutant AML; quizartinib now approved in frontline FLT3-ITD."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "MYC is amplified and overexpressed in AML; FLT3-ITD and NPM1 mutations upregulate MYC via STAT5/HOXA9; MYC drives LSC self-renewal; BET bromodomain inhibitors suppress MYC transcription in AML; menin inhibitors downregulate HOXA9-MYC axis in KMT2A-r and NPM1-mutant AML."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 is overexpressed in ~80% of AML blasts; venetoclax + azacitidine (VIALE-A) improved OS vs. azacitidine alone in untreated AML (14.7 vs. 9.6 months); venetoclax sensitivity correlates with BCL-2/MCL-1 ratio; MCL-1 upregulation is the primary venetoclax resistance mechanism."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations in ~7% de novo AML and ~30% therapy-related AML; TP53-mutant AML is highly drug-resistant; decitabine/azacitidine + venetoclax modestly active; magrolimab + azacitidine showed activity; eprenetapopt (APR-246) refolded mutant p53 but phase 3 trials negative."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "AML LSCs exploit CXCL12/CXCR4 for bone marrow niche retention and chemotherapy protection; plerixafor (CXCR4 antagonist) disrupts niche retention → sensitizes LSC to chemotherapy; high CXCR4 expression is an adverse prognostic feature in AML and correlates with relapse."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "AML chokes the bone marrow with ≥20% immature myeloid blasts that arrest differentiation and crowd out normal hematopoiesis → anemia, bleeding, and infection; chemo-resistant leukemic stem cells hide in hypoxic, CXCL12-rich endosteal niches, seeding relapse."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Myelodysplastic syndromes are the main precursor of secondary AML (~30% of AML arises from MDS), sharing TP53 mutations, del(5q)/del(7q), and complex karyotypes; MDS-related and therapy-related AML are adverse-risk and treated differently (e.g., CPX-351)."
  - target: 01-human/03-molecular/idh1
    relation: connects-to
    note: "IDH1 and IDH2 mutations (~20% of AML) produce the oncometabolite 2-hydroxyglutarate, which blocks myeloid differentiation; the inhibitors ivosidenib (IDH1) and enasidenib (IDH2) lower 2-HG and let blasts mature, though they can trigger a differentiation syndrome."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "AML is a maturation arrest: leukemic blasts flood the marrow but cannot become functional neutrophils, so patients suffer severe neutropenia and infection even with high white counts; the promyelocytic subtype (APL) is uniquely cured by ATRA/arsenic forcing differentiation."
  - target: 01-human/07-system/cml
    relation: connects-to
    note: "AML and CML are the two principal myeloid leukemias: CML is a chronic BCR-ABL1-driven proliferation of maturing granulocytes that, untreated, accelerates into a blast crisis that is AML-like (myeloid in ~70%); both arise from transformed myeloid progenitors in the marrow."
  - target: 01-human/07-system/myeloproliferative-neoplasms
    relation: connects-to
    note: "Myeloproliferative neoplasms (PV, ET, PMF) carry a risk of leukemic transformation to AML—highest in myelofibrosis—where JAK2/CALR-mutant clones acquire added lesions (TP53, ASXL1); this 'blast phase' AML is treatment-resistant with poor survival."
  - target: 01-human/07-system/all
    relation: connects-to
    note: "AML and ALL are the two acute leukemias, divided by lineage: AML is a myeloblast malignancy of adults with Auer rods and MPO positivity, while ALL is a lymphoblast cancer mostly of children—differing in immunophenotype, treatment, and CNS prophylaxis."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ionizing radiation is an established cause of AML, and photons also treat it: atomic-bomb survivors and radiotherapy patients have raised AML risk, while total-body irradiation conditions the marrow before stem-cell transplant—radiation as cause and cure."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells drive the graft-versus-leukemia effect that helps cure AML: after allogeneic transplant, donor NK and T cells kill residual leukemic blasts, and KIR-ligand mismatch boosts this—the basis for why transplant beats chemo alone for lasting remission."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Myelofibrosis and AML are linked by leukemic transformation: the JAK2/CALR-driven marrow fibrosis of myelofibrosis can accumulate mutations and evolve into secondary AML, a feared 'blast phase'—so MPNs like myelofibrosis shadow AML as a terminal endpoint."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "AML is part of the Li-Fraumeni cancer spectrum: germline TP53 loss predisposes to leukemias—especially therapy-related AML after the chemo and radiation used for earlier cancers—and somatic TP53-mutant AML is among the most chemo-resistant subtypes."
  - target: 01-human/07-system/noonan-syndrome
    relation: connects-to
    note: "Noonan syndrome predisposes to myeloid leukemia: germline PTPN11/RAS-pathway activation drives a JMML-like myeloproliferative disorder in infancy that can progress, and the RAS-pathway link extends to AML—a RASopathy dysregulating myelopoiesis."
  - target: 01-human/03-molecular/npm1
    relation: connects-to
    note: "NPM1 is the most common AML mutation: this nucleophosmin defect mislocalizes the protein and defines a large, often favorable-prognosis AML subtype (when FLT3-ITD is absent), so NPM1 status guides risk-stratification and the choice between chemotherapy and transplant."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "AML causes anemia by crowding out red-cell production: leukemic blasts fill the marrow and suppress erythropoiesis, so fatigue and pallor from anemia—alongside bleeding and infection from low platelets and neutrophils—are how marrow takeover presents."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Acute promyelocytic leukemia, an AML subtype, classically triggers DIC: the malignant promyelocytes release procoagulants that consume clotting factors, causing life-threatening bleeding—so APL is a medical emergency treated urgently with ATRA to halt the coagulopathy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "AML crowds out platelet production: leukemic blasts overrun the marrow, so falling platelets cause bruising, bleeding, and—when promyelocytic AML triggers DIC—life-threatening hemorrhage, making platelet transfusion a mainstay of supportive care."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "AML is curable by harnessing the immune system: allogeneic stem-cell transplant works largely through a graft-versus-leukemia effect, where donor T cells recognize and kill residual blasts—the most powerful anti-leukemic immunotherapy available."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "AML can infiltrate the skin as leukemia cutis: monocytic subtypes especially seed violaceous nodules, and myeloid sarcoma (chloroma) forms solid deposits—skin or soft-tissue lesions that can herald or signal relapse of the marrow disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Allogeneic transplant cures AML through cytotoxic T cells: donor T cells mount a graft-versus-leukemia attack on residual blasts—the curative immune mechanism that makes transplant, not just chemo, definitive for high-risk disease."
  - target: 01-human/03-molecular/idh2
    relation: connects-to
    note: "IDH2 mutations define a targetable AML subset: like IDH1, mutant IDH2 makes the oncometabolite 2-hydroxyglutarate that blocks blood-cell differentiation, and the inhibitor enasidenib releases that block to mature the leukemic cells."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "AML often begins with DNMT3A clonal hematopoiesis: this epigenetic mutation arises in aging blood stem cells (CHIP) years before leukemia, seeding a pre-malignant clone—part of why DNA-methylation drugs like azacitidine treat AML."
  - target: 01-human/03-molecular/tet2
    relation: connects-to
    note: "TET2 and DNMT3A break AML's methylation from opposite ends: TET2 normally erases DNA methylation while DNMT3A writes it, so mutating either scrambles the epigenome of blood stem cells—converging on the same leukemic dysregulation from opposite directions."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "AML's leukemic stem cells survive on autophagy: they recycle their contents to weather metabolic stress and chemotherapy, so blocking autophagy is studied to eradicate the stem cells that drive relapse after remission."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "AML evades immunity with regulatory T cells: the leukemic marrow fills with Tregs that suppress the anti-leukemia response, a barrier to immunotherapy and to the graft-versus-leukemia effect that transplant relies on."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "AML suffocates the body by crowding out red cells: leukemic blasts pack the marrow and choke normal blood production, so anemia and low oxygen delivery—fatigue and breathlessness—are common presenting signs of the disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "AML can invade the brain and meninges: myeloid sarcoma and leptomeningeal spread, more common in monocytic subtypes, seed the CNS, so neurologic symptoms prompt spinal fluid testing and CNS-directed treatment."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are central to anti-leukemia immunity in AML: presenting blast antigens, they prime the T-cell and graft-versus-leukemia response, and dendritic-cell vaccines are explored to prevent relapse after treatment."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "AML's many transfusions load the body with iron: repeated red-cell support and a hungry marrow drive iron overload, and the leukemic cells' own iron handling is studied as a metabolic vulnerability."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "AML can spill out of the marrow into the spleen: leukemic infiltration and extramedullary hematopoiesis enlarge the organ, one of the soft-tissue sites where myeloid blasts gather beyond the bloodstream."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "RUNX1 mutation defines a tough AML subtype: this master transcription factor of blood-cell development, when lost, yields a leukemia with poorer response, recognized as its own high-risk disease entity."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy finds AML's signature crystal: Auer rods, needle-like aggregates of fused azurophilic granules packed inside the myeloblasts, are diagnostic of myeloid leukemia and never seen in lymphoid disease."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "AML can flood the blood with potassium as it dies: the huge mass of leukemic cells, bursting under chemotherapy in tumor lysis syndrome, spills potassium that can stop the heart unless aggressively managed."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Leukemic cells infiltrate the liver: AML blasts seep into hepatic tissue alongside the spleen, swelling it into the hepatomegaly that, with low blood counts, marks the disease's spread beyond the marrow."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "AML threatens neurons from two directions: blasts can seed the CNS, while the high-dose cytarabine used to cure it crosses into the brain and poisons cerebellar neurons, causing a dose-limiting ataxia and slurred speech."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "A flood of blasts can choke the lungs: in hyperleukocytosis the rigid leukemic cells plug pulmonary capillaries (leukostasis), causing breathlessness and hypoxia that is a medical emergency demanding urgent cytoreduction."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Curing AML can wound the heart: the anthracyclines (daunorubicin, idarubicin) at the core of induction are cumulatively cardiotoxic, risking a later cardiomyopathy that survivors are monitored for for years."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies sort and target the blasts: flow-cytometry panels for CD33, CD34, CD13, and MPO classify the leukemia, and the anti-CD33 antibody-drug conjugate gemtuzumab ozogamicin delivers a toxin straight to the AML cells carrying that marker."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Starting treatment can crash the kidney: as a huge blast burden is lysed, tumor lysis syndrome floods the blood with potassium, phosphate, and urate that crystallize in and obstruct the kidney, demanding hydration and rasburicase."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "The cure threatens future fertility: intensive chemotherapy and any conditioning radiation for transplant can sterilize, so fertility preservation is discussed urgently before induction, especially in the young adults AML often strikes."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Induction leans on a cardiotoxic drug: the anthracycline in the '7+3' regimen (daunorubicin or idarubicin) injures cardiomyocytes in a cumulative way, so cardiac function is checked before and during the intensive chemotherapy AML demands."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Transplant trades one disease for another's risk: allogeneic stem-cell transplant cures high-risk AML partly through a graft-versus-leukemia effect, but the same donor cells can turn on the host as graft-versus-host disease."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "KIT mutation reshapes the good-risk leukemias: in core-binding-factor AML — the t(8;21) and inv(16) subtypes — an activating KIT mutation worsens the otherwise favorable prognosis and offers a target for KIT-directed therapy."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Self-renewal is hijacked from stem-cell biology: aberrant Wnt/β-catenin signaling sustains the leukemic stem cells that seed relapse, making the pathway a target for trying to exhaust the reservoir standard chemotherapy leaves behind."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The danger is the empty marrow: AML and its chemotherapy wipe out functioning neutrophils, so overwhelming infection and septic shock through the resulting profound neutropenia are the leading cause of death."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The leukemia bends the niche to its needs: bone-marrow macrophages are reprogrammed to shelter and feed AML cells, and in monocytic subtypes the malignant clone itself differentiates toward macrophages that infiltrate gums and skin."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB keeps the leukemic stem cell alive: AML stem cells show constitutive NF-κB activity that normal blood stem cells lack, a survival signal that makes the pathway an attractive target for sparing healthy marrow."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 carries the FLT3 growth signal: downstream of mutated FLT3 and cytokine receptors, STAT3 activation drives AML proliferation and survival, and high STAT3 activity marks a worse prognosis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "A cancer that both clots and bleeds: AML's tumor burden and procoagulant blasts raise venous thrombosis risk even as the disease destroys platelets, a treacherous balance most extreme in its promyelocytic subtype."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Prolonged neutropenia is its classic opening: the deep, weeks-long neutropenia of AML induction lets inhaled Aspergillus invade the lung as angioinvasive aspergillosis, a leading infectious cause of death that drives antifungal prophylaxis."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Chemo-stripped mucosa and neutropenia let it bloodstream: AML treatment's mucositis and neutropenia allow Candida to translocate from the gut into the blood, causing invasive candidiasis and hepatosplenic disease."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Its cure can wound the heart: the anthracyclines (daunorubicin, idarubicin) central to AML induction are dose-dependently cardiotoxic, and the cumulative exposure can leave a cardiomyopathy and heart failure in survivors."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Tumor lysis and nephrotoxic drugs batter the kidneys: the massive cell turnover at AML induction triggers tumor lysis syndrome, and the chemotherapy and antifungals it requires add nephrotoxicity, together risking acute and chronic kidney injury."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Prolonged immunosuppression invites Pneumocystis: the deep, sustained T-cell suppression of AML therapy and stem-cell transplant predisposes to Pneumocystis pneumonia, so prophylaxis is given through treatment."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An abrupt, life-threatening diagnosis and long isolation weigh on mood: AML's sudden onset, prolonged inpatient induction and transplant impose a heavy psychological burden that contributes to depression and anxiety."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Chemotherapy and transplant reawaken shingles: the deep, prolonged immune suppression of AML induction and stem-cell transplant lets latent varicella-zoster reactivate, so antiviral prophylaxis is standard."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Marrow failure can transform into leukaemia: acquired aplastic anemia carries a real risk of clonal evolution to MDS and acute myeloid leukaemia, linking the empty marrow to the malignant one."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A sudden, relapse-prone cancer breeds dread: the abrupt life-threatening onset, intensive therapy and constant relapse risk of AML fuel chronic anxiety alongside the depression its course imposes."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It writes itself on the skin: monocytic AML infiltrates the dermis as leukaemia cutis and the gums as hyperplasia, and can trigger Sweet syndrome, a paraneoplastic neutrophilic dermatosis of tender plaques."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can seed the central nervous system: monocytic AML subtypes invade the leptomeninges and form myeloid sarcomas, prompting CSF examination and intrathecal therapy when neurological signs appear."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its chemotherapy can rot the gut wall: profound neutropenia after AML induction causes neutropenic enterocolitis (typhlitis), a life-threatening inflammation of the caecum with fever, pain and bleeding."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It clogs and infects the lungs: hyperleukocytosis causes pulmonary leukostasis with breathlessness, and profound neutropenia invites fungal and bacterial pneumonia."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its breakdown floods the kidney: tumour lysis syndrome at induction releases urate and potassium causing acute kidney injury, and monocytic AML lysozyme injures the renal tubules."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its induction chemotherapy is cardiotoxic: the daunorubicin and other anthracyclines used to treat AML carry a dose-dependent risk of cardiomyopathy and heart failure."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Precision drugs now match its mutations: FLT3 inhibitors (midostaurin), IDH inhibitors and the BCL-2 inhibitor venetoclax target specific AML subtypes beyond standard chemotherapy."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It grows in and out of the marrow: AML crowds the bone marrow causing bone pain and cytopenias, and a myeloid sarcoma (chloroma) can form a solid mass in bone or soft tissue."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Treatment leaves endocrine scars: chemotherapy and stem-cell transplant for AML impair fertility and thyroid and gonadal function in survivors."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "The 7+3 backbone: intensive induction with seven days of cytarabine and three of an anthracycline aims to clear the marrow of blasts, followed by consolidation or allogeneic transplant — the cytotoxic core of AML therapy for decades."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Largely resistant to checkpoints: AML evades immunity through antigen loss and an immunosuppressive marrow rather than checkpoint exhaustion, so PD-1 blockade shows limited single-agent activity, studied mainly with hypomethylating agents."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Myeloid versus lymphoid leukaemia: AML is an acute proliferation of myeloid blasts needing urgent intensive therapy, whereas CLL is an indolent accumulation of mature B-lymphocytes often watched for years — opposite poles of leukaemia in lineage and tempo."
  - target: 01-human/07-system/cmml
    relation: connects-to
    note: "A pre-leukaemic myeloid neighbour: chronic myelomonocytic leukaemia, a myelodysplastic/myeloproliferative overlap, frequently transforms into AML and shares its TET2, ASXL1 and SRSF2 epigenetic mutations."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Its cure can scar the heart: anthracyclines like daunorubicin, central to AML induction, are cardiotoxic and damage the myocardium dose-dependently, leaving cardiomyopathy and heart failure as late effects in survivors."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "Shared epigenetic mutations across lineages: angioimmunoblastic T-cell lymphoma carries the same TET2, DNMT3A and IDH2 mutations as AML, sometimes arising from a common clonal-haematopoiesis precursor in blood and lymph node."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Therapy-related AML: the alkylators and topoisomerase-II inhibitors used to cure solid tumours like breast cancer can seed a secondary, poor-prognosis AML years later—a dark side of cytotoxic chemotherapy."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Pulmonary leukostasis: in hyperleukocytic AML, blast cells plug the alveolar capillaries, causing acute hypoxaemic respiratory failure—a haematologic emergency needing urgent cytoreduction."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Tumour-lysis nephropathy: the rapid blast turnover of AML induction floods the blood with urate and phosphate that precipitate in the kidney, injuring the glomerulus and tubules into acute kidney injury."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "A shared oncometabolite: IDH1/IDH2-mutant AML and IDH-mutant glioma both produce 2-hydroxyglutarate that reprograms the epigenome, and both are now treated with the same IDH inhibitors—one drug class across blood and brain cancer."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Leukostasis emergency: extreme blast counts in AML make the blood sludge, obstructing cerebral and pulmonary microvessels to cause stroke-like deficits and respiratory failure that demand urgent cytoreduction."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Tumour-lysis hyperuricaemia: the massive cell turnover of AML treatment releases a flood of urate that overlaps with gout's crystal disease and threatens the kidney unless pre-empted with rasburicase or allopurinol."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "Epigenetic dysregulation: EZH2 and the broader epigenetic machinery (with DNMT3A, TET2 and IDH already implicated) are deranged in AML, a rationale for epigenetic therapy."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival signalling: PI3K-AKT-mTOR signalling, often downstream of FLT3, sustains the survival and proliferation of AML blasts."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Protective marrow niche: HIF-1α-driven adaptation to the hypoxic bone-marrow niche shelters AML leukaemic stem cells, supporting their persistence and relapse."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "Cell-cycle drive: cyclin D-CDK4/6 activity propels AML blasts through the G1 checkpoint, a candidate cell-cycle target alongside the disease's mutational drivers."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Marrow angiogenesis: VEGF raises bone-marrow microvessel density in AML, an autocrine and paracrine signal supporting the leukaemic clone."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory niche: TNF-α in the AML marrow microenvironment suppresses normal haematopoiesis while supporting the survival of the leukaemic clone."
  - target: 01-human/03-molecular/men1
    relation: connects-to
    note: "Menin-MLL dependency: KMT2A-rearranged and NPM1-mutant AML depend on the menin-MLL interaction to maintain HOX/MEIS leukaemic transcription, the target of menin inhibitors (revumenib) now approved in this disease."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "Hedgehog signalling: aberrant Hedgehog pathway activity supports AML stem-cell maintenance, the rationale for the SMO inhibitor glasdegib combined with low-dose cytarabine in older AML patients."
  - target: 01-human/03-molecular/mdm2
    relation: connects-to
    note: "p53 reactivation: most AML retains wild-type TP53 but keeps p53 restrained by high MDM2, making MDM2 inhibitors a strategy to restore p53-driven apoptosis in TP53-wild-type leukaemia."
  - target: 01-human/03-molecular/srsf2
    relation: connects-to
    note: "Splicing-factor class: SRSF2 mutations define the secondary, MDS-related AML that arises from a preceding myelodysplasia, a poor-prognosis subgroup distinct from de-novo disease and a target for splicing-modulator therapy."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "Stem-cell paradox: although a tumour suppressor elsewhere, FOXO transcription factors are paradoxically active in many AMLs, maintaining the quiescent leukaemic stem cells that survive chemotherapy and seed relapse."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Graft-versus-leukaemia: the curative power of allogeneic stem-cell transplant in AML comes from donor T and NK cells killing residual leukaemia through perforin and granzyme, the immunological effect that underlies long-term remission after transplant."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "MAPK proliferation: FLT3-ITD and RAS mutations in AML signal through the MAPK cascade to ERK1/2, driving blast expansion and acting as a route of resistance to FLT3 inhibitors."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Venetoclax dependency: AML blasts evade caspase-3 apoptosis through high anti-apoptotic BCL-2 (already mapped), the dependency the BCL-2 inhibitor venetoclax exploits to restore blast-cell death."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K survival axis: PI3K-AKT-mTOR signalling (AKT already mapped) is constitutively activated in AML and supports blast survival and chemoresistance, a targetable dependency."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR effector: mTOR is the growth-controlling output of the PI3K-AKT axis (PIK3CA and AKT mapped) constitutively activated downstream of FLT3 in AML, sustaining blast metabolism and survival."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK-STAT survival: FLT3 and KIT (both mapped) signal through JAK2-STAT5, a survival and proliferation pathway driving AML blasts and a mechanism of resistance to FLT3 inhibitors."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Cell-cycle drive: the cyclin-D-CDK4/6 axis (CDK4/6 mapped) releases E2F1 to drive the proliferation of AML blasts."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "RAS cooperation: activating RAS-pathway mutations (KRAS/NRAS) are common cooperating lesions in AML, driving the proliferative ERK-MAPK signalling (ERK1/2 already mapped) of the leukemic clone."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "Checkpoint loss: dysregulation of the RB1-E2F checkpoint (CDK4/6 and E2F1 already mapped) contributes to the cell-cycle drive of acute myeloid leukemia."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Chemoresistance: NRF2 antioxidant signalling protects AML blasts and leukemic stem cells from oxidative stress and contributes to chemoresistance."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 supports the survival and bone-marrow-niche adhesion of leukemic stem cells, contributing to chemoresistance and relapse in AML."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the antileukemic immune response and immune-evasion balance of AML, relevant to relapse after allogeneic transplant."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING modulates the inflammatory and immune microenvironment of the AML bone marrow."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling regulates leukemic stem cell quiescence and the protective bone-marrow niche that fosters chemoresistance in AML."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by myeloid blasts drive inflammatory signaling and associate with poor prognosis and chemoresistance in AML."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β sustains leukemic stem cell self-renewal and survival, making it a targetable dependency in AML."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family and LYN kinase signaling downstream of FLT3 and KIT (FLT3 and KIT already mapped) supports the survival of the leukemic blasts of AML."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT signaling relays the cytokine-driven survival of AML blasts (distinct from the JAK2 mutation already mapped)."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A loss releases CDK4/6-cyclin-D control (CDK4/6 already mapped) of the cell cycle in AML."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the metabolic adaptation of the leukemic stem cells of acute myeloid leukemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A and the broader chromatin/cohesin machinery contribute to the epigenetic dysregulation of acute myeloid leukemia."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2-driven monocyte recruitment shapes the inflammatory bone-marrow niche of acute myeloid leukemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the bone-marrow niche interactions of acute myeloid leukemia."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory bone-marrow microenvironment of acute myeloid leukemia."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation in the bone-marrow niche contributes to the leukemic stem-cell maintenance of acute myeloid leukemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of acute myeloid leukemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory bone-marrow microenvironment of acute myeloid leukemia."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the inflammatory bone-marrow microenvironment of acute myeloid leukemia."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immune-evasion relapse: AML relapsing after allogeneic transplant characteristically downregulates HLA class II to escape donor T-cell recognition, so MHC class II expression governs the graft-versus-leukaemia response that underpins cure by transplant."
  - target: 01-human/03-molecular/sf3b1
    relation: connects-to
    note: "Spliceosome drivers: SF3B1 and related splicing-factor mutations drive myelodysplasia-related and secondary AML, a class of spliceosomal lesions complementing the SRSF2 mutations already mapped in the disease's mutational landscape."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "APL coagulopathy: acute promyelocytic leukaemia triggers disseminated intravascular coagulation and hyperfibrinolysis that consume fibrinogen, causing the catastrophic early haemorrhage that is the leading cause of induction death before ATRA takes effect."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Marrow failure cytopenias: AML replaces normal marrow, and the resulting anaemia with falling haemoglobin, alongside thrombocytopenia and neutropenia, produces the fatigue, bleeding and infection that present the disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Tumour lysis: the high blast burden of AML, especially on induction chemotherapy, releases purines that xanthine oxidase converts to uric acid, causing the tumour-lysis syndrome prevented with allopurinol or rasburicase."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Graft-versus-leukaemia: IL-2-driven T- and NK-cell activity underlies the graft-versus-leukaemia effect of allogeneic transplant (perforin already mapped) that cures many AML patients, and the CAR-T and NK approaches under investigation."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Anthracycline cardiotoxicity: the daunorubicin/idarubicin in 7+3 induction for AML is cardiotoxic, and troponin elevation helps detect the myocardial injury that limits the cumulative anthracycline dose in these often already-frail patients."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Tumour-lysis acidosis: the rapid lysis of the high blast burden of AML on induction releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped), part of its acute metabolic emergency."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune evasion: IL-10 in the leukaemic marrow microenvironment dampens the anti-leukaemia T-cell response (MHC class II already mapped), part of the immune escape that AML exploits and that immunotherapy and transplant aim to overcome."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "The MDS-AML continuum: myelodysplastic syndrome transforms to secondary AML, the two sharing the clonal-haematopoiesis mutations (TET2, DNMT3A and SF3B1 already mapped) along a spectrum defined by the blast count."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage niche: IL-4 polarises the marrow macrophages toward an M2 phenotype (IL-10 already mapped), part of the immunosuppressive leukaemic marrow microenvironment that shelters the AML blasts."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Marrow-adipocyte crosstalk: the marrow adipocytes and their adipokine adiponectin engage in metabolic crosstalk with the AML blasts, the marrow adipose tissue supporting the leukaemia's fatty-acid metabolism and survival."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: leptin, with adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk that supports the fatty-acid metabolism and survival of the AML blasts in the marrow niche."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Tumour-lysis hypocalcaemia: the hyperphosphataemia of the tumour lysis syndrome at AML induction binds calcium, causing the hypocalcaemia that accompanies the hyperkalaemia and needs monitoring."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 marrow niche: IL-13, with IL-4 (already mapped), sustains the M2 marrow macrophages (already mapped) of the immunosuppressive leukaemic niche that shelters the AML blasts."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), is the marrow-adipocyte adipokine of the leukaemic niche microenvironment of AML."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin adds an anaemia of chronic disease to the marrow-failure anaemia (iron and haemoglobin already mapped) of AML."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Marrow-adipocyte niche: the bone-marrow (already mapped) adipocytes — the source of the leptin, adiponectin and resistin (already mapped) — form a metabolic niche that supports the AML blasts through fatty-acid transfer."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate antileukaemic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment and is exploited (historically) against the myeloid leukaemias including AML."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1/GVL arm: the IFN-γ of the T and NK cells (perforin already mapped) is the type-II interferon arm of the graft-versus-leukaemia immunity against AML."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the anti-leukaemic immune response of AML."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the AML marrow."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow microenvironment of AML."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the AML marrow microenvironment."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immunosuppressive marrow microenvironment of AML."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Marrow mast cells: the mast cells of the bone-marrow (already mapped) niche contribute to the type-2 (IgE already mapped) and stromal dimension of the AML microenvironment."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) shapes the myeloid and immunosuppressive dimension of the AML marrow microenvironment."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the myeloid and immunosuppressive dimension of the AML marrow microenvironment."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the AML blasts recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the marrow microenvironment."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Anaemia/iron overload: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the marrow-failure anaemia and the transfusional iron overload of AML."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Marrow stromal alarmin: TSLP, released from the AML bone-marrow (already mapped) stromal niche, activates mast cells (already mapped) and plasmacytoid dendritic cells (dendritic-cell already mapped), sustaining the type-2 immunosuppressive leukaemia microenvironment."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Contact-pathway coagulation: bradykinin, generated by contact-pathway activation in the hypercoagulable state and disseminated intravascular coagulation (already mapped) of AML, amplifies the vascular permeability and endothelial dysfunction in leukostasis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Marrow-failure anaemia: erythropoietin supports recovery from the marrow-failure anaemia of AML during and after induction chemotherapy (already mapped), and EPOR expression on AML blasts raises the question of possible direct trophic effects."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact/lectin pathway regulation: the C1-esterase inhibitor controls the contact-pathway activation (bradykinin already mapped) and classical complement in the hypercoagulable state and DIC complicating AML, limiting the vascular permeability cascade."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell–leukaemia crosstalk: histamine, released by mast cells (already mapped) in the bone-marrow microenvironment of AML, signals through H2 receptors on AML blasts, promoting leukaemia cell survival and immunosuppression in the marrow niche."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Matricellular niche factor: periostin, secreted by the bone-marrow stromal niche (already mapped) of AML, promotes leukaemia stem-cell (LSC) adhesion and quiescence through integrin αvβ3/αvβ5 signalling, contributing to chemotherapy resistance."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "AML melatonin: melatonin induces AML blast apoptosis via MT1/MT2-mediated mTOR (already mapped) inhibition; melatonin also enhances FLT3 (already mapped) mutant AML sensitivity to targeted therapy and reduces bone-marrow (already mapped) immunosuppression."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "AML testosterone: androgen receptor signalling in AML blasts promotes leukaemia survival via mTOR (already mapped) and IL-6 (already mapped) driven STAT3 activation; androgen-deprivation therapy sensitises AML to venetoclax in the bone-marrow (already mapped) niche."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "AML serotonin: serotonin, released by activated platelets (already mapped) in the AML bone-marrow (already mapped) niche, signals through 5-HT2 receptors on AML blasts promoting proliferative and anti-apoptotic signalling via the IL-6 (already mapped) pathway."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "AML oxytocin: oxytocin receptor on AML blasts activates cAMP/PKA signalling that attenuates FLT3 (already mapped) and mTOR (already mapped) driven proliferation; oxytocin also modulates NK-cell (already mapped) cytotoxicity against AML in the bone-marrow (already mapped) niche."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "AML vasopressin: vasopressin V1A/V1B receptors on AML blasts intersect the IL-6 (already mapped)/STAT3 and mTOR (already mapped) proliferative axes; AVP-mediated calcium signalling amplifies AML blast survival signals in the bone-marrow (already mapped) leukaemic niche."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "AML prolactin: prolactin via JAK2/STAT5 on AML blasts promotes leukaemia-cell survival through mTOR (already mapped) and IL-6 (already mapped) crosstalk; prolactin modulates the bone-marrow (already mapped) niche and NF-κB (already mapped) anti-apoptotic expression."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "AML selenium: selenoproteins counter ROS-driven DNA damage in AML blasts and bone-marrow (already mapped) stromal cells; selenium deficiency amplifies NF-κB (already mapped) and mTOR (already mapped) and IL-6 (already mapped) blast proliferation and survival cascade of AML."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "AML iodine: thyroid hormones regulate NK-cell (already mapped) and dendritic-cell (already mapped) anti-leukaemic immunity; thyroid deficiency amplifies IL-6 (already mapped) and STAT3 (already mapped) and mTOR (already mapped) blast survival cascade in the AML bone-marrow niche."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "AML sodium: sodium dysregulation in bone-marrow (already mapped) stroma and leukaemic blasts amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) and FLT3 (already mapped) blast proliferation in AML."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "AML zinc: zinc cofactors macrophage (already mapped) anti-tumour function and regulatory T-cell (already mapped) homeostasis; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) leukaemic blast expansion in AML."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "AML magnesium: magnesium supports macrophage (already mapped) anti-inflammatory resolution and bone-marrow (already mapped) haematopoiesis; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) leukaemic cascade in AML."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "copper, via ceruloplasmin and SOD in macrophages (already mapped) and bone-marrow (already mapped) stroma, scavenges ROS; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) leukaemic blast proliferation in AML."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "phosphorus-driven ATP in bone-marrow (already mapped) blast cells and macrophages (already mapped) sustains leukaemic proliferation; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) leukaemic blast cascade in AML."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitric oxide from iNOS in macrophages (already mapped) and bone-marrow (already mapped) stroma modulates leukaemic blast apoptosis; nitrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) proliferative blast cascade in AML."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "AML carbon: carbon, as metabolic backbone of purines and nucleotides in blast cells and macrophages (already mapped), drives leukaemic proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast cascade in AML."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "AML chloride: chloride channels in blast cells and macrophages (already mapped) regulate intracellular pH during leukaemic expansion; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast proliferation in AML."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "AML hydrogen: hydrogen, via redox homeostasis in blast cells and macrophages (already mapped), quenches leukaemic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast proliferative cascade in AML."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "AML sulfur: H2S from sulfur-amino acids in blast cells and macrophages (already mapped) scavenges ROS promoting apoptosis; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast proliferative cascade in AML."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "AML PD-1: PD-1 on macrophages (already mapped) and t-cytotoxic-cell (already mapped) modulates leukaemic immune evasion; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast proliferative cascade in AML."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "AML GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and blast cells modulates metabolic immune homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) leukaemic cascade in AML."
---

# AML

## Overview

**Acute myeloid leukemia (AML)** is a clonal hematopoietic malignancy characterized by the accumulation of immature myeloid blasts (≥20% in bone marrow or blood) that have arrested differentiation and outcompete normal hematopoiesis → profound bone marrow failure. AML is the most common acute leukemia in adults (~21,000 new cases and ~11,000 deaths annually in the United States) and has a poor overall prognosis despite modern therapy: median OS with standard induction is ~12-18 months in fit patients; 5-year OS ~30% overall (higher in younger/favorable risk, lower in elderly/adverse risk) [^dinardo-2020-viale-a].

**Incidence and risk factors:**
- **Age:** Median diagnosis ~68; incidence increases sharply with age; AML in children (~15% of pediatric leukemia vs. ~80% in adults) has different biology and better outcomes
- **Prior cytotoxic therapy:** Therapy-related AML (t-AML) occurs after alkylating agent exposure (latency 5-10 years, often complex karyotype, TP53 mutation) or topoisomerase II inhibitor exposure (latency 2-3 years, often MLL rearrangements)
- **Antecedent hematologic disease:** MDS → AML transformation (~30% of AML); MDS-related AML has TP53 mutations, del(5q), del(7q), complex karyotype, and is treated differently (CPX-351 liposomal cytarabine/daunorubicin FDA-approved for secondary AML)
- **Myeloproliferative neoplasms:** Polycythemia vera, essential thrombocythemia, myelofibrosis → blast phase AML; JAK2-mutant → JAK2 V617F often retained in transformed AML
- **Germline predisposition (~5-10% of all AML):**
  - *RUNX1* germline → Familial platelet disorder + AML predisposition
  - *CEBPA* germline (N-terminal) → familial AML
  - *DDX41* germline → predominantly myeloid malignancies in older adults (~4% of AML); autosomal dominant; splicing factor mutations are a hallmark
  - *GATA2* germline → GATA2 deficiency syndrome → immune deficiency + MDS/AML
  - Down syndrome (trisomy 21) → GATA1 somatic mutation → transient myeloproliferative disorder (TMD) in neonates → AML in 20% of TMD if untreated; GATA1-mutant DS-AML is exquisitely chemosensitive

**The WHO 2022 and ELN 2022 classification:**
- WHO 2022 replaces the blast threshold approach with genotype-first classification:
  - *AML with defining genetic abnormalities:* t(8;21)/RUNX1-RUNX1T1; inv(16)/t(16;16)/CBFB-MYH11; t(15;17)/PML-RARA (APL); t(9;11)/KMT2A-MLLT3; t(6;9)/DEK-NUP214; NPM1 mutation; CEBPA mutation (biallelic or bZIP-domain); TP53 biallelic mutation (AML-TP53); IDH1/2 mutations (with specific co-mutations)
  - *AML not otherwise specified (NOS):* When none of the above define the entity

## Structure

### Bone marrow and blast biology

**Normal myelopoiesis:**
- HSC (CD34+/CD38-/Lin-) → MPP → CMP (common myeloid progenitor) → GMP (granulocyte-monocyte progenitor) → monocytes or neutrophils/granulocytes; AML arises from HSC or early progenitor with acquisition of "driver" mutations → differentiation block at GMP or promyelocyte stage (depending on subtype)
- **Morphological classification (AML FAB M0-M7):** M0 (undifferentiated), M1 (minimal maturation), M2 (maturation — most common), M3 (APL, promyelocytic), M4 (myelomonocytic), M5 (monocytic), M6 (erythroid), M7 (megakaryoblastic); WHO 2022 largely superseded FAB but FAB terminology persists clinically

**Leukemic stem cells (LSCs):**
- AML LSCs (CD34+/CD38-/CD123+/TIM-3+) are rare (0.01-0.1% of blasts) but self-renewing and chemotherapy-resistant; LSCs reside in hypoxic endosteal niches (CXCL12-rich) and are quiescent during induction → survive → give rise to MRD and relapse
- **LSC targeting strategies:** CD33 (gemtuzumab ozogamicin ADC), CD123 (IMGN632, flotetuzumab), CD47 ("don't eat me" signal — magrolimab), CLL-1 (emerging target); FLT3 inhibitors partially target LSCs (FLT3+ LSCs)
- **BCL-2 in LSC survival:** LSCs depend on BCL-2 for survival in the bone marrow niche → venetoclax disrupts BCL-2/BIM interaction → LSC apoptosis; LSCs have low OXPHOS metabolism → venetoclax (which requires OXPHOS) selectively kills LSCs

**Molecular pathogenesis:**
AML requires cooperative mutations in at least 2 functional categories (Gilliland-Druker model):
- **Class I:** Activation of proliferation (FLT3-ITD, KRAS/NRAS, KIT D816V) — alone insufficient for AML
- **Class II:** Impaired differentiation (RUNX1-RUNX1T1, CBFB-MYH11, PML-RARA, NPM1, CEBPA, IDH1/2) — alone insufficient for AML
- **Epigenetic modifiers (Class III):** DNMT3A, TET2, IDH1/2, ASXL1, EZH2 — often in ancestral clones predating AML, also seen in CHIP (clonal hematopoiesis of indeterminate potential)

## Function

### Clinical presentation and diagnosis

**Presentation:**
- **Bone marrow failure symptoms:** Anemia (fatigue, pallor, dyspnea), thrombocytopenia (petechiae, bruising, mucosal bleeding — gum bleeding in monocytic AML), neutropenia (febrile, infection — often presenting illness)
- **Leukostasis:** WBC >50,000-100,000/μL → viscous blood → pulmonary and cerebral capillary plugging → dyspnea, hypoxemia, altered consciousness; emergency leukapheresis or hydroxyurea cytoreduction
- **Tissue infiltration:** Gingival hyperplasia (AML M4/M5 monocytic subtypes — monocytes home to gingiva); skin (leukemia cutis); CNS (rare in AML vs. ALL; more common in monocytic/M4-M5); chloroma (extramedullary myeloid tumor at any site)
- **APL emergency (M3):** Coagulopathy (DIC, hyperfibrinolysis) from promyelocyte granule contents (tissue factor, annexin II); bleeding → ICH is the leading cause of early death in APL; ATRA must be started immediately upon APL suspicion before genetic confirmation

**Diagnostic workup:**
- **CBC/peripheral smear:** Blasts on smear; cytopenia(s); circulating blasts ≥20% → AML by WHO (blast threshold); some WHO 2022 entities diagnosed with <20% if genetic abnormality present (e.g., NPM1-mutant)
- **Bone marrow biopsy and aspirate:** Morphology; blast count; immunohistochemistry (CD34, MPO, TDT)
- **Flow cytometry (immunophenotyping):** Myeloid markers: CD13, CD33, CD117 (KIT), MPO, CD34, CD38, HLA-DR; monocytic: CD14, CD64, CD11b; megakaryoblastic: CD41/61; erythroid: CD71, glycophorin A; aberrant antigen expression → measurable residual disease (MRD) tracking
- **Cytogenetics (karyotype):** FISH and conventional G-banded; 24-48 hrs; t(8;21), inv(16), t(15;17) = core-binding factor AML (CBF-AML) → favorable; del(5q), del(7), complex karyotype (≥3 abnormalities) → adverse; results critical for ELN 2022 risk stratification
- **Molecular profiling (NGS):** FLT3-ITD/TKD, NPM1, CEBPA, IDH1, IDH2, DNMT3A, TP53, RUNX1, ASXL1, SRSF2, SF3B1, STAG2, RAD21; required for ELN 2022 risk group and therapeutic decisions; FLT3 and NPM1 simultaneously tested (co-mutation common)
- **MRD assessment:** NPM1-PCR (most sensitive; 1 mutation/10^6 normal cells) or multicolor flow cytometry (10^-4 sensitivity); MRD negativity after induction/consolidation → lower relapse risk; MRD-guided treatment adaptation (alloSCT decision, maintenance)

**ELN 2022 risk stratification:**
- **Favorable:** t(8;21)/RUNX1-RUNX1T1; inv(16)/CBFB-MYH11; NPM1-mutant (without FLT3-ITD or low AR FLT3-ITD); CEBPA bZIP-domain mutation; 5-year OS ~65-75%
- **Intermediate:** NPM1-mutant with FLT3-ITD high AR; NPM1-WT with FLT3-ITD; t(9;11)/KMT2A-MLLT3; others; 5-year OS ~35-50%
- **Adverse:** TP53 mutation (biallelic or monoallelic); RUNX1-mutant; ASXL1-mutant; t(6;9)/DEK-NUP214; inv(3)/t(3;3)/GATA2-MECOM; del(5q); del(7); del(17p); complex/monosomal karyotype; 5-year OS <15%

## Pathology

### Diagnosis

**APL diagnosis and management (urgent):**
- Morphology: Hypergranular promyelocytes with Auer rods ± faggot cells; Microgranular variant (M3v): bilobed/kidney-shaped nuclei, high WBC → leukostasis risk
- FISH/PCR for PML-RARA: Positive → start ATRA immediately (do not wait for PCR confirmation)
- **ATRA + ATO (arsenic trioxide) for APL (Lo-Coco 2013, ATRA-ATO):** Standard for non-high-risk APL; CR 100%, 2-year EFS 97% (vs. ATRA-chemo 86%); no chemotherapy needed; differentiation syndrome (ATRA syndrome) — rapid promyelocyte differentiation → capillary leak → pulmonary infiltrates/fever → dexamethasone; ATO-ATRA also FDA-approved for high-risk APL (WBC >10,000 — add gemtuzumab ozogamicin)

### Treatment

**Fit patients (ECOG PS 0-2, age <75 with adequate organ function) — standard induction:**
- **7+3 induction:** Cytarabine 100-200 mg/m² continuous IV infusion × 7 days + daunorubicin 60-90 mg/m² × 3 days; CR ~65-80%; refractory AML (~10%) → salvage
- **7+3 + midostaurin** (for FLT3-mutant AML; RATIFY trial): Addition of midostaurin 50 mg BID days 8-21 of each cycle → OS benefit [^stone-2017-midostaurin]; standard for FLT3-mutant newly diagnosed AML
- **CPX-351 (Vyxeos)** — liposomal cytarabine:daunorubicin (5:1 molar ratio): Preferred induction for therapy-related AML and AML-MRC (MDS-related changes or AML with MDS defining mutations); CPX-351 trial: OS 9.56 vs. 5.95 months vs. 7+3 in secondary AML; FDA-approved 2017
- **Gemtuzumab ozogamicin (GO, Mylotarg):** Anti-CD33 ADC; added to 7+3 for de novo AML (CBF-AML benefit; ALFA 0701 trial); AAML1031 (pediatric CBF-AML) — major benefit; FDA-approved 2017 (re-approved after voluntary withdrawal)

**Consolidation after CR:**
- **Favorable risk (CBF-AML):** High-dose cytarabine (HiDAC, 3 g/m² q12h × 6 doses) × 3-4 cycles ± GO; alloSCT only in first relapse or MRD-positive disease
- **Intermediate/adverse risk:** AlloSCT in first CR (CR1) is standard; HLA typing at diagnosis; MRD status after induction guides alloSCT urgency; FLT3-ITD high AR → alloSCT + gilteritinib or midostaurin maintenance
- **MRD-guided approach:** NPM1-PCR MRD negativity after consolidation → continue without alloSCT in favorable/intermediate risk; NPM1-PCR MRD positive → alloSCT

**Older/unfit patients — venetoclax-based therapy [^dinardo-2020-viale-a]:**
- **Venetoclax + azacitidine (Ven+Aza, VIALE-A trial):** CR+CRi 36.7% vs. 17.9%; OS 14.7 vs. 9.6 months; FDA-approved 2020 for newly diagnosed AML in adults ≥75 or unfit; standard of care; tumor lysis syndrome (TLS) prophylaxis required; grade 3-4 neutropenia nearly universal
- **Venetoclax + decitabine:** Alternative to azacitidine; similar CR rates
- **Venetoclax + gilteritinib** (for FLT3-mutant AML in older/unfit patients): Under clinical investigation; early phase response rates promising
- **Glasdegib + cytarabine (BRIGHT 1003):** Hedgehog (SMO) inhibitor + LDAC for unfit AML; modest OS benefit; FDA-approved 2018

**Targeted therapies in AML:**
- **Midostaurin + 7+3:** FLT3-mutant, fit; RATIFY OS benefit; FDA-approved 2017 [^stone-2017-midostaurin]
- **Quizartinib + 7+3:** FLT3-ITD, fit; QuANTUM-First OS benefit; FDA-approved 2023
- **Gilteritinib (R/R FLT3-mutant):** ADMIRAL OS 9.3 vs. 5.6 months; FDA-approved 2018 [^perl-2019-gilteritinib — referenced via flt3 entry]
- **Enasidenib (IDH2-mutant R/R):** IDH2 inhibitor → 2-HG reduction → differentiation; ORR 40.3%, CR 19.3% (AGILE-2 trial) [^stein-2017-enasidenib]; FDA-approved 2017; differentiation syndrome (IDH-DS) — corticosteroids required
- **Ivosidenib (IDH1-mutant):** IDH1 inhibitor; FDA-approved 2018 for R/R IDH1-mutant AML; enasidenib + azacitidine and ivosidenib + azacitidine frontline trials showed CR benefit
- **Olutasidenib (IDH1-mutant R/R):** Second-generation IDH1 inhibitor; FDA-approved 2022
- **Revumenib (KMT2A-r or NPM1-mutant R/R):** Menin-MLL interaction inhibitor; ORR 23%, CR 17%; FDA-approved 2024 for R/R KMT2A-r or NPM1-mutant AML (AUGMENT-101)

**Relapsed/Refractory AML:**
- **FLAG-IDA** (fludarabine + cytarabine + G-CSF + idarubicin): Standard salvage; CR2 ~40-50% in first relapse
- **AlloSCT after CR2:** Only curative option; outcomes determined by remission status at transplant and cytogenetics
- **Gilteritinib (FLT3-mutant):** Monotherapy or + venetoclax
- **Venetoclax-based combinations:** Ven+Aza, Ven+decitabine; CR rates ~40-50% in venetoclax-naive; much lower in venetoclax-resistant (MCL-1-driven)
- **Magrolimab (anti-CD47) + azacitidine:** "Don't eat me" signal blockade → macrophage phagocytosis of AML blasts; TP53-mutant AML (ENHANCE-2 trial) — ongoing; early signal in TP53-mutant disease
- **Pivekimab sunirine (IMGN632):** Anti-CD123 ADC (IGN with DGN462 pyrrolobenzodiazepine payload); activity in R/R AML

## Connections

- `connects-to` → **[FLT3](../../03-molecular/flt3/README.md)** — FLT3-ITD (~25-30%) and FLT3-TKD (~7-10%) are the most common actionable AML mutations; midostaurin + 7+3 chemotherapy improves OS in FLT3-mutant AML (RATIFY trial); gilteritinib improves OS vs. salvage chemo in R/R FLT3-mutant AML; quizartinib now approved in frontline FLT3-ITD.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — MYC is amplified and overexpressed in AML; FLT3-ITD and NPM1 mutations upregulate MYC via STAT5/HOXA9; MYC drives LSC self-renewal; BET bromodomain inhibitors (JQ1, ABBV-075) suppress MYC transcription in AML; menin inhibitors downregulate HOXA9-MYC axis in KMT2A-r and NPM1-mutant AML.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 is overexpressed in ~80% of AML blasts; venetoclax (BCL-2 inhibitor) + azacitidine (VIALE-A) improved OS vs. azacitidine alone in untreated AML (14.7 vs. 9.6 months); venetoclax sensitivity correlates with BCL-2/MCL-1 ratio; MCL-1 upregulation is the primary venetoclax resistance mechanism.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutations in ~7% of de novo AML and ~30% of therapy-related AML; TP53-mutant AML is highly drug-resistant; decitabine/azacitidine + venetoclax modestly active; magrolimab (anti-CD47) + azacitidine showed activity; eprenetapopt (APR-246) refolded mutant p53 but phase 3 trials negative.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — AML LSCs exploit CXCL12/CXCR4 for bone marrow niche retention and chemotherapy protection; plerixafor (CXCR4 antagonist) disrupts niche retention → sensitizes LSC to chemotherapy; high CXCR4 expression is an adverse prognostic feature in AML and correlates with relapse.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — AML chokes the bone marrow with ≥20% immature myeloid blasts that arrest differentiation and crowd out normal hematopoiesis → anemia, bleeding, and infection; chemo-resistant leukemic stem cells hide in hypoxic, CXCL12-rich endosteal niches, seeding relapse.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — Myelodysplastic syndromes are the main precursor of secondary AML (~30% of AML arises from MDS), sharing TP53 mutations, del(5q)/del(7q), and complex karyotypes; MDS-related and therapy-related AML are adverse-risk and treated differently (e.g., CPX-351).
- `connects-to` → **[IDH1](../../03-molecular/idh1/README.md)** — IDH1 and IDH2 mutations (~20% of AML) produce the oncometabolite 2-hydroxyglutarate, which blocks myeloid differentiation; the inhibitors ivosidenib (IDH1) and enasidenib (IDH2) lower 2-HG and let blasts mature, though they can trigger a differentiation syndrome.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — AML is a maturation arrest: leukemic blasts flood the marrow but cannot become functional neutrophils, so patients suffer severe neutropenia and infection even with high white counts; the promyelocytic subtype (APL) is uniquely cured by ATRA/arsenic forcing differentiation.
- `connects-to` → **[Chronic Myeloid Leukemia](../cml/README.md)** — AML and CML are the two principal myeloid leukemias: CML is a chronic BCR-ABL1-driven proliferation of maturing granulocytes that, untreated, accelerates into a blast crisis that is AML-like (myeloid in ~70%); both arise from transformed myeloid progenitors in the marrow.
- `connects-to` → **[Myeloproliferative Neoplasms](../myeloproliferative-neoplasms/README.md)** — Myeloproliferative neoplasms (PV, ET, PMF) carry a risk of leukemic transformation to AML—highest in myelofibrosis—where JAK2/CALR-mutant clones acquire added lesions (TP53, ASXL1); this 'blast phase' AML is treatment-resistant with poor survival.
- `connects-to` → **[Acute Lymphoblastic Leukemia](../all/README.md)** — AML and ALL are the two acute leukemias, divided by lineage: AML is a myeloblast malignancy of adults with Auer rods and MPO positivity, while ALL is a lymphoblast cancer mostly of children—differing in immunophenotype, treatment, and CNS prophylaxis.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ionizing radiation is an established cause of AML, and photons also treat it: atomic-bomb survivors and radiotherapy patients have raised AML risk, while total-body irradiation conditions the marrow before stem-cell transplant—radiation as cause and cure.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells drive the graft-versus-leukemia effect that helps cure AML: after allogeneic transplant, donor NK and T cells kill residual leukemic blasts, and KIR-ligand mismatch boosts this—the basis for why transplant beats chemo alone for lasting remission.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Myelofibrosis and AML are linked by leukemic transformation: the JAK2/CALR-driven marrow fibrosis of myelofibrosis can accumulate mutations and evolve into secondary AML, a feared 'blast phase'—so MPNs like myelofibrosis shadow AML as a terminal endpoint.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — AML is part of the Li-Fraumeni cancer spectrum: germline TP53 loss predisposes to leukemias—especially therapy-related AML after the chemo and radiation used for earlier cancers—and somatic TP53-mutant AML is among the most chemo-resistant subtypes.
- `connects-to` → **[Noonan Syndrome](../noonan-syndrome/README.md)** — Noonan syndrome predisposes to myeloid leukemia: germline PTPN11/RAS-pathway activation drives a JMML-like myeloproliferative disorder in infancy that can progress, and the RAS-pathway link extends to AML—a RASopathy dysregulating myelopoiesis.
- `connects-to` → **[NPM1](../../03-molecular/npm1/README.md)** — NPM1 is the most common AML mutation: this nucleophosmin defect mislocalizes the protein and defines a large, often favorable-prognosis AML subtype (when FLT3-ITD is absent), so NPM1 status guides risk-stratification and the choice between chemotherapy and transplant.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — AML causes anemia by crowding out red-cell production: leukemic blasts fill the marrow and suppress erythropoiesis, so fatigue and pallor from anemia—alongside bleeding and infection from low platelets and neutrophils—are how marrow takeover presents.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Acute promyelocytic leukemia, an AML subtype, classically triggers DIC: the malignant promyelocytes release procoagulants that consume clotting factors, causing life-threatening bleeding—so APL is a medical emergency treated urgently with ATRA to halt the coagulopathy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — AML crowds out platelet production: leukemic blasts overrun the marrow, so falling platelets cause bruising, bleeding, and—when promyelocytic AML triggers DIC—life-threatening hemorrhage, making platelet transfusion a mainstay of supportive care.
- `connects-to` → **[Immune System](../immune-system/README.md)** — AML is curable by harnessing the immune system: allogeneic stem-cell transplant works largely through a graft-versus-leukemia effect, where donor T cells recognize and kill residual blasts—the most powerful anti-leukemic immunotherapy available.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — AML can infiltrate the skin as leukemia cutis: monocytic subtypes especially seed violaceous nodules, and myeloid sarcoma (chloroma) forms solid deposits—skin or soft-tissue lesions that can herald or signal relapse of the marrow disease.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Allogeneic transplant cures AML through cytotoxic T cells: donor T cells mount a graft-versus-leukemia attack on residual blasts—the curative immune mechanism that makes transplant, not just chemo, definitive for high-risk disease.
- `connects-to` → **[IDH2](../../03-molecular/idh2/README.md)** — IDH2 mutations define a targetable AML subset: like IDH1, mutant IDH2 makes the oncometabolite 2-hydroxyglutarate that blocks blood-cell differentiation, and the inhibitor enasidenib releases that block to mature the leukemic cells.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — AML often begins with DNMT3A clonal hematopoiesis: this epigenetic mutation arises in aging blood stem cells (CHIP) years before leukemia, seeding a pre-malignant clone—part of why DNA-methylation drugs like azacitidine treat AML.
- `connects-to` → **[TET2](../../03-molecular/tet2/README.md)** — TET2 and DNMT3A break AML's methylation from opposite ends: TET2 normally erases DNA methylation while DNMT3A writes it, so mutating either scrambles the epigenome of blood stem cells—converging on the same leukemic dysregulation from opposite directions.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — AML's leukemic stem cells survive on autophagy: they recycle their contents to weather metabolic stress and chemotherapy, so blocking autophagy is studied to eradicate the stem cells that drive relapse after remission.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — AML evades immunity with regulatory T cells: the leukemic marrow fills with Tregs that suppress the anti-leukemia response, a barrier to immunotherapy and to the graft-versus-leukemia effect that transplant relies on.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — AML suffocates the body by crowding out red cells: leukemic blasts pack the marrow and choke normal blood production, so anemia and low oxygen delivery—fatigue and breathlessness—are common presenting signs of the disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — AML can invade the brain and meninges: myeloid sarcoma and leptomeningeal spread, more common in monocytic subtypes, seed the CNS, so neurologic symptoms prompt spinal fluid testing and CNS-directed treatment.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are central to anti-leukemia immunity in AML: presenting blast antigens, they prime the T-cell and graft-versus-leukemia response, and dendritic-cell vaccines are explored to prevent relapse after treatment.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — AML's many transfusions load the body with iron: repeated red-cell support and a hungry marrow drive iron overload, and the leukemic cells' own iron handling is studied as a metabolic vulnerability.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — AML can spill out of the marrow into the spleen: leukemic infiltration and extramedullary hematopoiesis enlarge the organ, one of the soft-tissue sites where myeloid blasts gather beyond the bloodstream.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — RUNX1 mutation defines a tough AML subtype: this master transcription factor of blood-cell development, when lost, yields a leukemia with poorer response, recognized as its own high-risk disease entity.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy finds AML's signature crystal: Auer rods, needle-like aggregates of fused azurophilic granules packed inside the myeloblasts, are diagnostic of myeloid leukemia and never seen in lymphoid disease.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — AML can flood the blood with potassium as it dies: the huge mass of leukemic cells, bursting under chemotherapy in tumor lysis syndrome, spills potassium that can stop the heart unless aggressively managed.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Leukemic cells infiltrate the liver: AML blasts seep into hepatic tissue alongside the spleen, swelling it into the hepatomegaly that, with low blood counts, marks the disease's spread beyond the marrow.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — AML threatens neurons from two directions: blasts can seed the CNS, while the high-dose cytarabine used to cure it crosses into the brain and poisons cerebellar neurons, causing a dose-limiting ataxia and slurred speech.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — A flood of blasts can choke the lungs: in hyperleukocytosis the rigid leukemic cells plug pulmonary capillaries (leukostasis), causing breathlessness and hypoxia that is a medical emergency demanding urgent cytoreduction.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Curing AML can wound the heart: the anthracyclines (daunorubicin, idarubicin) at the core of induction are cumulatively cardiotoxic, risking a later cardiomyopathy that survivors are monitored for for years.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies sort and target the blasts: flow-cytometry panels for CD33, CD34, CD13, and MPO classify the leukemia, and the anti-CD33 antibody-drug conjugate gemtuzumab ozogamicin delivers a toxin straight to the AML cells carrying that marker.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Starting treatment can crash the kidney: as a huge blast burden is lysed, tumor lysis syndrome floods the blood with potassium, phosphate, and urate that crystallize in and obstruct the kidney, demanding hydration and rasburicase.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — The cure threatens future fertility: intensive chemotherapy and any conditioning radiation for transplant can sterilize, so fertility preservation is discussed urgently before induction, especially in the young adults AML often strikes.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Induction leans on a cardiotoxic drug: the anthracycline in the '7+3' regimen (daunorubicin or idarubicin) injures cardiomyocytes in a cumulative way, so cardiac function is checked before and during the intensive chemotherapy AML demands.
- `connects-to` → **[Graft-Versus-Host Disease](../gvhd/README.md)** — Transplant trades one disease for another's risk: allogeneic stem-cell transplant cures high-risk AML partly through a graft-versus-leukemia effect, but the same donor cells can turn on the host as graft-versus-host disease.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT mutation reshapes the good-risk leukemias: in core-binding-factor AML — the t(8;21) and inv(16) subtypes — an activating KIT mutation worsens the otherwise favorable prognosis and offers a target for KIT-directed therapy.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Self-renewal is hijacked from stem-cell biology: aberrant Wnt/β-catenin signaling sustains the leukemic stem cells that seed relapse, making the pathway a target for trying to exhaust the reservoir standard chemotherapy leaves behind.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The danger is the empty marrow: AML and its chemotherapy wipe out functioning neutrophils, so overwhelming infection and septic shock through the resulting profound neutropenia are the leading cause of death.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The leukemia bends the niche to its needs: bone-marrow macrophages are reprogrammed to shelter and feed AML cells, and in monocytic subtypes the malignant clone itself differentiates toward macrophages that infiltrate gums and skin.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB keeps the leukemic stem cell alive: AML stem cells show constitutive NF-κB activity that normal blood stem cells lack, a survival signal that makes the pathway an attractive target for sparing healthy marrow.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 carries the FLT3 growth signal: downstream of mutated FLT3 and cytokine receptors, STAT3 activation drives AML proliferation and survival, and high STAT3 activity marks a worse prognosis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — A cancer that both clots and bleeds: AML's tumor burden and procoagulant blasts raise venous thrombosis risk even as the disease destroys platelets, a treacherous balance most extreme in its promyelocytic subtype.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Prolonged neutropenia is its classic opening: the deep, weeks-long neutropenia of AML induction lets inhaled Aspergillus invade the lung as angioinvasive aspergillosis, a leading infectious cause of death that drives antifungal prophylaxis.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Chemo-stripped mucosa and neutropenia let it bloodstream: AML treatment's mucositis and neutropenia allow Candida to translocate from the gut into the blood, causing invasive candidiasis and hepatosplenic disease.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Its cure can wound the heart: the anthracyclines (daunorubicin, idarubicin) central to AML induction are dose-dependently cardiotoxic, and the cumulative exposure can leave a cardiomyopathy and heart failure in survivors.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Tumor lysis and nephrotoxic drugs batter the kidneys: the massive cell turnover at AML induction triggers tumor lysis syndrome, and the chemotherapy and antifungals it requires add nephrotoxicity, together risking acute and chronic kidney injury.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Prolonged immunosuppression invites Pneumocystis: the deep, sustained T-cell suppression of AML therapy and stem-cell transplant predisposes to Pneumocystis pneumonia, so prophylaxis is given through treatment.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An abrupt, life-threatening diagnosis and long isolation weigh on mood: AML's sudden onset, prolonged inpatient induction and transplant impose a heavy psychological burden that contributes to depression and anxiety.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Chemotherapy and transplant reawaken shingles: the deep, prolonged immune suppression of AML induction and stem-cell transplant lets latent varicella-zoster reactivate, so antiviral prophylaxis is standard.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Marrow failure can transform into leukaemia: acquired aplastic anemia carries a real risk of clonal evolution to MDS and acute myeloid leukaemia, linking the empty marrow to the malignant one.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A sudden, relapse-prone cancer breeds dread: the abrupt life-threatening onset, intensive therapy and constant relapse risk of AML fuel chronic anxiety alongside the depression its course imposes.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It writes itself on the skin: monocytic AML infiltrates the dermis as leukaemia cutis and the gums as hyperplasia, and can trigger Sweet syndrome, a paraneoplastic neutrophilic dermatosis of tender plaques.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can seed the central nervous system: monocytic AML subtypes invade the leptomeninges and form myeloid sarcomas, prompting CSF examination and intrathecal therapy when neurological signs appear.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its chemotherapy can rot the gut wall: profound neutropenia after AML induction causes neutropenic enterocolitis (typhlitis), a life-threatening inflammation of the caecum with fever, pain and bleeding.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It clogs and infects the lungs: hyperleukocytosis causes pulmonary leukostasis with breathlessness, and profound neutropenia invites fungal and bacterial pneumonia.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its breakdown floods the kidney: tumour lysis syndrome at induction releases urate and potassium causing acute kidney injury, and monocytic AML lysozyme injures the renal tubules.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its induction chemotherapy is cardiotoxic: the daunorubicin and other anthracyclines used to treat AML carry a dose-dependent risk of cardiomyopathy and heart failure.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Precision drugs now match its mutations: FLT3 inhibitors (midostaurin), IDH inhibitors and the BCL-2 inhibitor venetoclax target specific AML subtypes beyond standard chemotherapy.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It grows in and out of the marrow: AML crowds the bone marrow causing bone pain and cytopenias, and a myeloid sarcoma (chloroma) can form a solid mass in bone or soft tissue.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Treatment leaves endocrine scars: chemotherapy and stem-cell transplant for AML impair fertility and thyroid and gonadal function in survivors.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — The 7+3 backbone: intensive induction with seven days of cytarabine and three of an anthracycline aims to clear the marrow of blasts, followed by consolidation or allogeneic transplant — the cytotoxic core of AML therapy for decades.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Largely resistant to checkpoints: AML evades immunity through antigen loss and an immunosuppressive marrow rather than checkpoint exhaustion, so PD-1 blockade shows limited single-agent activity, studied mainly with hypomethylating agents.
- `connects-to` → **[CLL](../cll/README.md)** — Myeloid versus lymphoid leukaemia: AML is an acute proliferation of myeloid blasts needing urgent intensive therapy, whereas CLL is an indolent accumulation of mature B-lymphocytes often watched for years — opposite poles of leukaemia in lineage and tempo.
- `connects-to` → **[CMML](../cmml/README.md)** — A pre-leukaemic myeloid neighbour: chronic myelomonocytic leukaemia, a myelodysplastic/myeloproliferative overlap, frequently transforms into AML and shares its TET2, ASXL1 and SRSF2 epigenetic mutations.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Its cure can scar the heart: anthracyclines like daunorubicin, central to AML induction, are cardiotoxic and damage the myocardium dose-dependently, leaving cardiomyopathy and heart failure as late effects in survivors.
- `connects-to` → **[PTCL](../ptcl/README.md)** — Shared epigenetic mutations across lineages: angioimmunoblastic T-cell lymphoma carries the same TET2, DNMT3A and IDH2 mutations as AML, sometimes arising from a common clonal-haematopoiesis precursor in blood and lymph node.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Therapy-related AML: the alkylators and topoisomerase-II inhibitors used to cure solid tumours like breast cancer can seed a secondary, poor-prognosis AML years later—a dark side of cytotoxic chemotherapy.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Pulmonary leukostasis: in hyperleukocytic AML, blast cells plug the alveolar capillaries, causing acute hypoxaemic respiratory failure—a haematologic emergency needing urgent cytoreduction.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Tumour-lysis nephropathy: the rapid blast turnover of AML induction floods the blood with urate and phosphate that precipitate in the kidney, injuring the glomerulus and tubules into acute kidney injury.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — A shared oncometabolite: IDH1/IDH2-mutant AML and IDH-mutant glioma both produce 2-hydroxyglutarate that reprograms the epigenome, and both are now treated with the same IDH inhibitors—one drug class across blood and brain cancer.
- `connects-to` → **[Stroke](../stroke/README.md)** — Leukostasis emergency: extreme blast counts in AML make the blood sludge, obstructing cerebral and pulmonary microvessels to cause stroke-like deficits and respiratory failure that demand urgent cytoreduction.
- `connects-to` → **[Gout](../gout/README.md)** — Tumour-lysis hyperuricaemia: the massive cell turnover of AML treatment releases a flood of urate that overlaps with gout's crystal disease and threatens the kidney unless pre-empted with rasburicase or allopurinol.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — Epigenetic dysregulation: EZH2 and the broader epigenetic machinery (with DNMT3A, TET2 and IDH already implicated) are deranged in AML, a rationale for epigenetic therapy.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Survival signalling: PI3K-AKT-mTOR signalling, often downstream of FLT3, sustains the survival and proliferation of AML blasts.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Protective marrow niche: HIF-1α-driven adaptation to the hypoxic bone-marrow niche shelters AML leukaemic stem cells, supporting their persistence and relapse.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — Cell-cycle drive: cyclin D-CDK4/6 activity propels AML blasts through the G1 checkpoint, a candidate cell-cycle target alongside the disease's mutational drivers.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Marrow angiogenesis: VEGF raises bone-marrow microvessel density in AML, an autocrine and paracrine signal supporting the leukaemic clone.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory niche: TNF-α in the AML marrow microenvironment suppresses normal haematopoiesis while supporting the survival of the leukaemic clone.
- `connects-to` → **[Menin (MEN1)](../../03-molecular/men1/README.md)** — KMT2A-rearranged and NPM1-mutant AML depend on the menin-MLL interaction to maintain HOX/MEIS leukemic transcription—the target of menin inhibitors (revumenib) now approved, a rare instance of drugging a transcriptional dependency directly.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — Aberrant Hedgehog pathway activity supports AML stem-cell maintenance, the rationale for the SMO inhibitor glasdegib combined with low-dose cytarabine as a lower-intensity option for older AML patients unfit for chemotherapy.
- `connects-to` → **[MDM2](../../03-molecular/mdm2/README.md)** — Most AML retains wild-type TP53 but keeps p53 restrained by high MDM2, making MDM2 inhibitors a strategy to restore p53-driven apoptosis in TP53-wild-type leukemia—complementary to the BCL-2 inhibition of venetoclax.
- `connects-to` → **[SRSF2](../../03-molecular/srsf2/README.md)** — SRSF2 mutations define the secondary, MDS-related AML that arises from a preceding myelodysplasia, a poor-prognosis subgroup distinct from de-novo disease and a target for splicing-modulator therapy.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — Although a tumor suppressor elsewhere, FOXO transcription factors are paradoxically active in many AMLs, maintaining the quiescent leukemic stem cells that survive chemotherapy and seed relapse.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — The curative power of allogeneic stem-cell transplant in AML comes from donor T and NK cells killing residual leukemia through perforin and granzyme, the graft-versus-leukemia effect that underlies long-term remission after transplant.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — FLT3-ITD and RAS mutations in AML signal through the MAPK cascade to ERK1/2, driving blast expansion and acting as a route of resistance to FLT3 inhibitors.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — AML blasts evade caspase-3 apoptosis through high anti-apoptotic BCL-2 (already mapped), the dependency the BCL-2 inhibitor venetoclax exploits to restore blast-cell death.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K-AKT-mTOR signaling (AKT already mapped) is constitutively activated in AML and supports blast survival and chemoresistance, a targetable dependency.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR is the growth-controlling output of the PI3K-AKT axis (PIK3CA and AKT mapped) constitutively activated downstream of FLT3 in AML, sustaining blast metabolism and survival.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — FLT3 and KIT (both mapped) signal through JAK2-STAT5, a survival and proliferation pathway driving AML blasts and a mechanism of resistance to FLT3 inhibitors.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — The cyclin-D-CDK4/6 axis (CDK4/6 mapped) releases E2F1 to drive the proliferation of AML blasts.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Activating RAS-pathway mutations (KRAS/NRAS) are common cooperating lesions in AML, driving the proliferative ERK-MAPK signaling (ERK1/2 already mapped) of the leukemic clone.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — Dysregulation of the RB1-E2F checkpoint (CDK4/6 and E2F1 already mapped) contributes to the cell-cycle drive of acute myeloid leukemia.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling protects AML blasts and leukemic stem cells from oxidative stress and contributes to chemoresistance.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 supports the survival and bone-marrow-niche adhesion of leukemic stem cells, contributing to chemoresistance and relapse in AML.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the antileukemic immune response and immune-evasion balance of AML, relevant to relapse after allogeneic transplant.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING modulates the inflammatory and immune microenvironment of the AML bone marrow.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling regulates leukemic stem cell quiescence and the protective bone-marrow niche that fosters chemoresistance in AML.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by myeloid blasts drive inflammatory signaling and associate with poor prognosis and chemoresistance in AML.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β sustains leukemic stem cell self-renewal and survival, making it a targetable dependency in AML.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family and LYN kinase signaling downstream of FLT3 and KIT (FLT3 and KIT already mapped) supports the survival of the leukemic blasts of AML.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT signaling relays the cytokine-driven survival of AML blasts (distinct from the JAK2 mutation already mapped).
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A loss releases CDK4/6-cyclin-D control (CDK4/6 already mapped) of the cell cycle in AML.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the metabolic adaptation of the leukemic stem cells of acute myeloid leukemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A and the broader chromatin/cohesin machinery contribute to the epigenetic dysregulation of acute myeloid leukemia.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2-driven monocyte recruitment shapes the inflammatory bone-marrow niche of acute myeloid leukemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the bone-marrow niche interactions of acute myeloid leukemia.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6-STAT3 signaling (STAT3 already mapped) participates in the inflammatory bone-marrow microenvironment of acute myeloid leukemia.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation in the bone-marrow niche contributes to the leukemic stem-cell maintenance of acute myeloid leukemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the inflammatory bone-marrow microenvironment of acute myeloid leukemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory bone-marrow microenvironment of acute myeloid leukemia.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the inflammatory bone-marrow microenvironment of acute myeloid leukemia.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immune-evasion relapse: AML relapsing after allogeneic transplant characteristically downregulates HLA class II to escape donor T-cell recognition, so MHC class II expression governs the graft-versus-leukaemia response that underpins cure by transplant.
- `connects-to` → **[SF3B1](../../03-molecular/sf3b1/README.md)** — Spliceosome drivers: SF3B1 and related splicing-factor mutations drive myelodysplasia-related and secondary AML, a class of spliceosomal lesions complementing the SRSF2 mutations already mapped in the disease's mutational landscape.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — APL coagulopathy: acute promyelocytic leukaemia triggers disseminated intravascular coagulation and hyperfibrinolysis that consume fibrinogen, causing the catastrophic early haemorrhage that is the leading cause of induction death before ATRA takes effect.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Marrow failure cytopenias: AML replaces normal marrow, and the resulting anaemia with falling haemoglobin, alongside thrombocytopenia and neutropenia, produces the fatigue, bleeding and infection that present the disease.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Tumour lysis: the high blast burden of AML, especially on induction chemotherapy, releases purines that xanthine oxidase converts to uric acid, causing the tumour-lysis syndrome prevented with allopurinol or rasburicase.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Graft-versus-leukaemia: IL-2-driven T- and NK-cell activity underlies the graft-versus-leukaemia effect of allogeneic transplant (perforin already mapped) that cures many AML patients, and the CAR-T and NK approaches under investigation.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Anthracycline cardiotoxicity: the daunorubicin/idarubicin in 7+3 induction for AML is cardiotoxic, and troponin elevation helps detect the myocardial injury that limits the cumulative anthracycline dose in these often already-frail patients.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Tumour-lysis acidosis: the rapid lysis of the high blast burden of AML on induction releases acids that, with lactate, produce the metabolic acidosis of tumour-lysis syndrome (urate already mapped), part of its acute metabolic emergency.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune evasion: IL-10 in the leukaemic marrow microenvironment dampens the anti-leukaemia T-cell response (MHC class II already mapped), part of the immune escape that AML exploits and that immunotherapy and transplant aim to overcome.
- `connects-to` → **[Myelodysplastic syndrome](../mds/README.md)** — The MDS-AML continuum: myelodysplastic syndrome transforms to secondary AML, the two sharing the clonal-haematopoiesis mutations (TET2, DNMT3A and SF3B1 already mapped) along a spectrum defined by the blast count.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage niche: IL-4 polarises the marrow macrophages toward an M2 phenotype (IL-10 already mapped), part of the immunosuppressive leukaemic marrow microenvironment that shelters the AML blasts.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Marrow-adipocyte crosstalk: the marrow adipocytes and their adipokine adiponectin engage in metabolic crosstalk with the AML blasts, the marrow adipose tissue supporting the leukaemia's fatty-acid metabolism and survival.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Marrow-adipocyte adipokine: leptin, with adiponectin (already mapped), is part of the marrow-adipocyte adipokine crosstalk that supports the fatty-acid metabolism and survival of the AML blasts in the marrow niche.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Tumour-lysis hypocalcaemia: the hyperphosphataemia of the tumour lysis syndrome at AML induction binds calcium, causing the hypocalcaemia that accompanies the hyperkalaemia and needs monitoring.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 marrow niche: IL-13, with IL-4 (already mapped), sustains the M2 marrow macrophages (already mapped) of the immunosuppressive leukaemic niche that shelters the AML blasts.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Marrow-adipocyte adipokine: resistin, with leptin and adiponectin (already mapped), is the marrow-adipocyte adipokine of the leukaemic niche microenvironment of AML.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin adds an anaemia of chronic disease to the marrow-failure anaemia (iron and haemoglobin already mapped) of AML.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Marrow-adipocyte niche: the bone-marrow (already mapped) adipocytes — the source of the leptin, adiponectin and resistin (already mapped) — form a metabolic niche that supports the AML blasts through fatty-acid transfer.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate antileukaemic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, shapes the innate-immune microenvironment and is exploited (historically) against the myeloid leukaemias including AML.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1/GVL arm: the IFN-γ of the T and NK cells (perforin already mapped) is the type-II interferon arm of the graft-versus-leukaemia immunity against AML.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the anti-leukaemic immune response of AML.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune microenvironment of the AML marrow.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory bone-marrow microenvironment of AML.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the AML marrow microenvironment.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines shaping the immunosuppressive marrow microenvironment of AML.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Marrow mast cells: the mast cells of the bone-marrow (already mapped) niche contribute to the type-2 (IgE already mapped) and stromal dimension of the AML microenvironment.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) shapes the myeloid and immunosuppressive dimension of the AML marrow microenvironment.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) contribute to the myeloid and immunosuppressive dimension of the AML marrow microenvironment.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the AML blasts recruit factor H to regulate the alternative complement pathway (C3, C5 and C5aR1 already mapped), tempering the complement attack within the marrow microenvironment.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Anaemia/iron overload: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the marrow-failure anaemia and the transfusional iron overload of AML.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Marrow stromal alarmin: TSLP, released from the AML bone-marrow (already mapped) stromal niche, activates mast cells (already mapped) and plasmacytoid dendritic cells (dendritic-cell already mapped), sustaining the type-2 immunosuppressive leukaemia microenvironment.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Contact-pathway coagulation: bradykinin, generated by contact-pathway activation in the hypercoagulable state and disseminated intravascular coagulation (already mapped) of AML, amplifies the vascular permeability and endothelial dysfunction in leukostasis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Marrow-failure anaemia: erythropoietin supports recovery from the marrow-failure anaemia of AML during and after induction chemotherapy (already mapped), and EPOR expression on AML blasts raises the question of possible direct trophic effects.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact/lectin pathway regulation: the C1-esterase inhibitor controls the contact-pathway activation (bradykinin already mapped) and classical complement in the hypercoagulable state and DIC complicating AML, limiting the vascular permeability cascade.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell–leukaemia crosstalk: histamine, released by mast cells (already mapped) in the bone-marrow microenvironment of AML, signals through H2 receptors on AML blasts, promoting leukaemia cell survival and immunosuppression in the marrow niche.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Matricellular niche factor: periostin, secreted by the bone-marrow stromal niche (already mapped) of AML, promotes leukaemia stem-cell (LSC) adhesion and quiescence through integrin αvβ3/αvβ5 signalling, contributing to chemotherapy resistance.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — AML melatonin: melatonin induces AML blast apoptosis via MT1/MT2-mediated mTOR (already mapped) inhibition; melatonin also enhances FLT3 (already mapped) mutant AML sensitivity to targeted therapy and reduces bone-marrow (already mapped) immunosuppression.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — AML testosterone: androgen receptor signalling in AML blasts promotes leukaemia survival via mTOR (already mapped) and IL-6 (already mapped) driven STAT3 activation; androgen-deprivation therapy sensitises AML to venetoclax in the bone-marrow (already mapped) niche.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — AML serotonin: serotonin, released by activated platelets (already mapped) in the AML bone-marrow (already mapped) niche, signals through 5-HT2 receptors on AML blasts promoting proliferative and anti-apoptotic signalling via the IL-6 (already mapped) pathway.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — AML oxytocin: oxytocin receptor on AML blasts activates cAMP/PKA signalling that attenuates FLT3 (already mapped) and mTOR (already mapped) driven proliferation; oxytocin also modulates NK-cell (already mapped) cytotoxicity against AML in the bone-marrow (already mapped) niche.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — AML vasopressin: vasopressin V1A/V1B receptors on AML blasts intersect the IL-6 (already mapped)/STAT3 and mTOR (already mapped) proliferative axes; AVP-mediated calcium signalling amplifies AML blast survival signals in the bone-marrow (already mapped) leukaemic niche.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — AML prolactin: prolactin via JAK2/STAT5 on AML blasts promotes leukaemia-cell survival through mTOR (already mapped) and IL-6 (already mapped) crosstalk; prolactin modulates the bone-marrow (already mapped) niche and NF-κB (already mapped) anti-apoptotic expression.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — AML selenium: selenoproteins counter ROS-driven DNA damage in AML blasts and bone-marrow (already mapped) stromal cells; selenium deficiency amplifies NF-κB (already mapped) and mTOR (already mapped) and IL-6 (already mapped) blast proliferation and survival cascade of AML.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — AML iodine: thyroid hormones regulate NK-cell (already mapped) and dendritic-cell (already mapped) anti-leukaemic immunity; thyroid deficiency amplifies IL-6 (already mapped) and STAT3 (already mapped) and mTOR (already mapped) blast survival cascade in the AML bone-marrow niche.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — AML sodium: sodium dysregulation in bone-marrow (already mapped) stroma and leukaemic blasts amplifies ionic stress; osmotic changes worsen NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) and FLT3 (already mapped) blast proliferation in AML.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — AML zinc: zinc cofactors macrophage (already mapped) anti-tumour function and regulatory T-cell (already mapped) homeostasis; zinc deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) leukaemic blast expansion in AML.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — AML magnesium: magnesium supports macrophage (already mapped) anti-inflammatory resolution and bone-marrow (already mapped) haematopoiesis; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) leukaemic cascade in AML.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — copper, via ceruloplasmin and SOD in macrophages (already mapped) and bone-marrow (already mapped) stroma, scavenges ROS; copper excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) leukaemic blast proliferation in AML.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — phosphorus-driven ATP in bone-marrow (already mapped) blast cells and macrophages (already mapped) sustains leukaemic proliferation; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) leukaemic blast cascade in AML.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitric oxide from iNOS in macrophages (already mapped) and bone-marrow (already mapped) stroma modulates leukaemic blast apoptosis; nitrogen excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) proliferative blast cascade in AML.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — AML carbon: carbon, as metabolic backbone of purines and nucleotides in blast cells and macrophages (already mapped), drives leukaemic proliferation; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast cascade in AML.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — AML chloride: chloride channels in blast cells and macrophages (already mapped) regulate intracellular pH during leukaemic expansion; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast proliferation in AML.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — AML hydrogen: hydrogen, via redox homeostasis in blast cells and macrophages (already mapped), quenches leukaemic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast proliferative cascade in AML.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — AML sulfur: H2S from sulfur-amino acids in blast cells and macrophages (already mapped) scavenges ROS promoting apoptosis; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast proliferative cascade in AML.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — AML PD-1: PD-1 on macrophages (already mapped) and t-cytotoxic-cell (already mapped) modulates leukaemic immune evasion; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) blast proliferative cascade in AML.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — AML GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and blast cells modulates metabolic immune homeostasis; GLP-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and FLT3 (already mapped) leukaemic cascade in AML.

[^dinardo-2020-viale-a]: DiNardo CD, Jonas BA, Pullarkat V, et al. Azacitidine and venetoclax in previously untreated acute myeloid leukemia. *N Engl J Med.* 2020;383(7):617-629. [doi:10.1056/NEJMoa2012971](https://doi.org/10.1056/NEJMoa2012971) · [PubMed 32786187](https://pubmed.ncbi.nlm.nih.gov/32786187/)
[^stone-2017-midostaurin]: Stone RM, Mandrekar SJ, Sanford BL, et al. Midostaurin plus chemotherapy for acute myeloid leukemia with a FLT3 mutation. *N Engl J Med.* 2017;377(5):454-464. [doi:10.1056/NEJMoa1614359](https://doi.org/10.1056/NEJMoa1614359) · [PubMed 28644114](https://pubmed.ncbi.nlm.nih.gov/28644114/)
[^stein-2017-enasidenib]: Stein EM, DiNardo CD, Pollyea DA, et al. Enasidenib in mutant IDH2 relapsed or refractory acute myeloid leukemia. *Blood.* 2017;130(6):722-731. [doi:10.1182/blood-2017-04-779405](https://doi.org/10.1182/blood-2017-04-779405) · [PubMed 28588020](https://pubmed.ncbi.nlm.nih.gov/28588020/)
