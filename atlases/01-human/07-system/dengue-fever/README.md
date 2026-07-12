---
schema: human-scale-entry/v1
id: dengue-fever
name: Dengue Fever
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Dengue fever (DENV 1-4; Aedes aegypti vector; flavivirus) causes 400M infections annually; NS1/TLR4 → vascular leak; ADE drives dengue hemorrhagic fever in secondary infections; Dengvaxia restricted to seropositive individuals; TAK-003 (Qdenga) approved 2022."
aliases: ["DENV", "dengue", "dengue hemorrhagic fever", "DHF", "dengue shock syndrome", "DSS", "breakbone fever", "Aedes aegypti", "flavivirus dengue", "ADE dengue", "Dengvaxia", "TAK-003"]
sources:
  - id: bhatt-2013-dengue-burden
    type: peer-reviewed
    cite: "Bhatt S, Gething PW, Brady OJ, et al. The global distribution and burden of dengue. Nature. 2013;496(7446):504-507."
    doi: "10.1038/nature12060"
    pmid: "23563266"
    url: "https://doi.org/10.1038/nature12060"
    accessed: "2026-06-08"
  - id: who-2009-dengue-guidelines
    type: clinical-guideline
    cite: "World Health Organization. Dengue: Guidelines for Diagnosis, Treatment, Prevention and Control. Geneva: WHO; 2009."
    url: "https://www.who.int/publications/i/item/9789241547871"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "DENV positive-sense ssRNA activates RIG-I and MDA5 → MAVS → IFN-β; DENV evades MAVS by: NS4B blocking RIG-I signaling, NS2B/NS3 protease disrupting MAVS, NS5 targeting STAT2 for degradation; early robust IFN-β correlates with mild dengue; IFN evasion drives severe disease."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Dengue NS1 protein activates TLR4 on endothelial cells: NS1 hexamer → TLR4/MD-2 → NF-κB → CXCL1, IL-8 → endothelial permeability and plasma leakage; TLR4-mediated NS1 endothelial activation is a key mechanism of dengue hemorrhagic fever; anti-TLR4 may reduce plasma leakage."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Dengue actively evades type I IFN: NS5 targets STAT2 for proteasomal degradation → blocks IFNAR/STAT1/STAT2 signaling; NS2B/NS3 inhibit IRF3; early IFN-β (first 24 h) limits viral replication; delayed IFN induction after immune evasion correlates with severe dengue."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Dengue evades both RNA (MAVS) and DNA (cGAS-STING) sensing: mitochondrial DNA released during dengue-induced apoptosis → cGAS → cGAMP → STING; however, DENV NS2B/NS3 disrupts STING signaling; dengue-mtDNA-cGAS-STING axis activates inflammatory cytokines during severe dengue."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "DENV NS5 degrades STAT2 via UBR4 → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 selectively targets human STAT2 (not mouse) → human-specific IFN evasion; STAT2 degradation is a major determinant of dengue viremia and is absent in murine dengue models."
  - target: 01-human/07-system/zika-virus
    relation: connects-to
    note: "ZIKV and DENV share Aedes aegypti vector and flavivirus biology; cross-reactive anti-DENV antibodies may enhance ZIKV infection via ADE in Fcγ receptor-bearing cells; prior dengue immunity has complex effects on Zika severity; both NS5 proteins degrade STAT2 for IFN evasion."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "WNV and DENV share flavivirus biology and NS5-mediated STAT1/STAT2 evasion; anti-DENV IgG cross-reacts with WNV E protein but provides limited protection; WNV causes neuroinvasive disease (encephalitis, AFP) not seen in DENV; both lack approved antivirals."
  - target: 02-pathogen/06-environmental/aedes-aegypti
    relation: connects-to
    note: "Dengue is spread by the day-biting Aedes aegypti mosquito, which also carries Zika, chikungunya, and yellow fever; its spread into the warming, urbanizing tropics is why dengue now causes ~400 million infections a year, and vector control remains a mainstay of prevention."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are dengue's main host cell and engine of severe disease: in reinfection with another serotype, non-neutralizing antibodies ferry virus into Fcγ-bearing macrophages — antibody-dependent enhancement — raising viral load and the cytokines that drive hemorrhagic dengue."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe dengue is partly a cytokine storm: antibody-enhanced macrophage infection plus cross-reactive memory T cells pour out TNF-α, IL-6, and IFN-γ that — with NS1 acting on the endothelium — break vascular integrity, causing the plasma leak of dengue hemorrhagic fever and shock."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Severe dengue is a disease of the endothelium: viral NS1 protein and cytokines transiently disrupt the endothelial glycocalyx and tight junctions, causing the plasma leakage (hemoconcentration, effusions, shock) that defines dengue hemorrhagic fever and dengue shock syndrome."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Severe dengue can trigger disseminated intravascular coagulation: endothelial injury, thrombocytopenia and cytokine-driven tissue-factor activation consume clotting factors, producing the bleeding of dengue hemorrhagic fever; DIC marks the severe end and worsens shock."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a key dengue target: the virus replicates in hepatocytes and Kupffer cells, raising transaminases in most cases and occasionally causing fulminant hepatitis; marked AST/ALT elevation is a warning sign of progression to severe dengue and correlates with bleeding."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thrombocytopenia defines severe dengue: the virus suppresses marrow megakaryopoiesis and antibodies destroy platelets, while plasma leak concentrates the blood—so a falling platelet count with rising hematocrit warns of progression to dengue hemorrhagic fever."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dengue virus first infects dendritic cells via DC-SIGN: skin dendritic cells captured at the mosquito bite are the earliest replication site and carry the virus onward, and antibody-dependent enhancement on a second infection worsens this uptake—driving severe dengue."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Dengue and malaria are the two great mosquito-borne tropical fevers and key differentials: both cause fever, thrombocytopenia, and can be severe, but dengue (Aedes flavivirus) brings plasma leak and hemorrhage while malaria (Plasmodium) brings hemolysis and cerebral disease."
  - target: 02-pathogen/01-viruses/dengue-virus
    relation: connects-to
    note: "Dengue virus drives the disease through four serotypes: infection gives lasting immunity to one serotype but only brief cross-protection, so later infection by a different serotype risks severe dengue—the serotype diversity central to the virus's danger."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Pre-existing IgG can worsen dengue via antibody-dependent enhancement: non-neutralizing antibodies from a prior serotype bind the new virus and ferry it into macrophages, boosting viral load—why second heterotypic infections cause severe, hemorrhagic dengue."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Dengue suppresses the bone marrow: the virus infects marrow progenitors and dampens production, causing the falling platelet and white-cell counts that define and grade the illness—so cytopenias track severity and signal the risk of hemorrhage."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells help drive severe dengue: cross-reactive memory T cells from a prior dengue serotype respond suboptimally on reinfection, releasing cytokines that worsen vascular leak—part of why a second, different-serotype infection is the dangerous one."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Dengue's danger is immunological: antibodies from a first infection can enhance uptake of a second serotype (antibody-dependent enhancement), amplifying viral load and the immune overreaction that causes plasma leak—so prior immunity paradoxically raises severe-dengue risk."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Dengue can invade the nervous system: beyond classic fever and bleeding, the virus and its immune response cause encephalitis, Guillain-Barré-like syndromes and stroke, so neurological dengue is an increasingly recognized severe manifestation."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Dengue's danger lies in B-cell antibodies: non-neutralizing antibodies from a prior infection can enhance a second one (antibody-dependent enhancement), so partial immunity worsens disease—the paradox that makes dengue vaccines hard to design."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Severe dengue is a cardiovascular emergency: cytokines make capillaries leak plasma, dropping blood volume into dengue shock syndrome, so careful fluid management—not antivirals—is what saves lives in the critical phase."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Severe dengue can injure the kidney: shock, hemolysis, and direct viral effects cause acute kidney injury in the critical phase, so renal function is watched closely as a marker of severity and a target for supportive care."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Severe dengue is defined by leaking albumin: the virus makes capillaries leak, so plasma and albumin escape into the chest and belly, concentrating the blood and dropping pressure into the shock that makes dengue hemorrhagic fever deadly."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help make dengue severe: infection activates them to release chymase and vasoactive mediators that pull apart vascular junctions, driving the plasma leak of severe dengue—and blood chymase levels track with disease severity."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Dengue can inflame the heart: the virus causes myocarditis with weakened contraction and arrhythmias, an underrecognized contributor to the shock and fluid-balance problems that complicate severe infection."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Severe dengue leaks plasma via VEGF: the virus and the immune response drive VEGF that loosens the junctions between endothelial cells, so fluid escapes the vessels into tissues—the plasma leakage behind dengue shock syndrome."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Dengue often drops blood sodium: plasma leakage, vomiting and fluid shifts cause hyponatremia, a common electrolyte disturbance in severe disease that worsens confusion and must be corrected carefully during fluid resuscitation."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Dengue enlarges and endangers the spleen: viral replication and immune activation swell the organ, and in rare cases the engorged spleen ruptures—a life-threatening bleed to consider in a dengue patient with sudden abdominal pain."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Severe dengue acidifies the blood: massive plasma leakage drops blood pressure into dengue shock, and the underperfused tissues generate lactic acid, so metabolic acidosis is a marker of the dangerous phase."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Dengue can invade the brain: beyond the classic fever, severe disease causes encephalitis and encephalopathy with seizures and altered consciousness, part of the expanded dengue syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells meet dengue early: they mount a rapid antiviral attack in the first days of infection, and the strength of this innate response helps shape whether the illness stays mild or turns severe."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ultrasound and X-ray photons catch dengue's plasma leak: pleural effusions, ascites and a thickened gallbladder wall reveal the capillary leakage that marks the dangerous critical phase."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Dengue's capillary leak floods the chest: plasma seeps into the pleural space, causing effusions and, in severe cases, respiratory distress, part of the third-spacing of dengue shock."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Dengue disturbs potassium: hypokalemia is common in the acute phase, while kidney injury in severe disease can drive it up, so electrolytes are watched closely during the critical leak phase."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows dengue's two threats: the small icosahedral flavivirus replicating in scaffolds of host membrane, and the widened junctions between endothelial cells through which plasma leaks in severe disease."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Dengue paints the skin: a flushed rash gives way to the petechiae of falling platelets and the classic 'islands of white in a sea of red,' and a tourniquet test bringing out spots warns of bleeding risk."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Dengue can blur vision weeks in: dengue maculopathy with retinal hemorrhage, edema, and foveolitis appears around the time platelets bottom out, sometimes leaving lasting blind spots."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody is dengue's double-edged sword: it diagnoses infection (IgM, NS1) and confers serotype immunity, but partial antibody from a prior serotype enhances a second infection (ADE), making the repeat illness far more dangerous."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "A rising hematocrit signals the danger: as plasma leaks from the vessels in severe dengue, the red cells concentrate, so a climbing hematocrit (hemoconcentration) is a key warning sign that shock may be near."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Dengue drops the white count: a marked leukopenia, with falling neutrophils, is an early and characteristic feature that — alongside the plunging platelets — helps point to the diagnosis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha opens the vessels in severe dengue: the cytokine storm's TNF loosens endothelial junctions, and this surge in vascular permeability is what drives the plasma leak, hemoconcentration and shock that define dengue hemorrhagic fever."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Old immunity makes the second infection worse: cross-reactive memory helper T cells from a prior dengue serotype respond to the new one with a distorted, overexuberant cytokine burst — 'original antigenic sin' that helps tip a repeat infection into severe disease."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Dengue can inflame the pancreas: the virus is a recognized cause of acute pancreatitis, with abdominal pain and raised enzymes appearing in severe cases, one of the visceral complications that can accompany the plasma-leak phase."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 helps spring the vascular leak: the cytokine surge of severe dengue, with IL-6 prominent, loosens the endothelial barrier and drives the plasma leakage and shock that define dengue hemorrhagic fever."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "The leaking plasma can flood the lungs: severe dengue causes pleural effusions and, at its worst, acute respiratory distress syndrome, the capillary leak filling the alveoli as it does the body cavities."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Dengue can strike the heart: viral myocarditis depresses contractility and causes arrhythmia, so cardiac dysfunction and heart failure add to the shock of the severe disease."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine helps spring the leak: mast-cell histamine released during dengue widens endothelial junctions, contributing to the vascular permeability and plasma leakage that define severe dengue, and its levels track disease severity."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Dengue is hepatotropic: the virus replicates in hepatocytes, and the resulting liver-cell injury raises transaminases and, in severe cases, causes the acute liver failure that worsens the bleeding and shock."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Severe dengue mimics and invites sepsis: dengue shock syndrome resembles septic shock, and the gut-barrier breakdown and immune exhaustion of severe disease open the door to secondary bacterial sepsis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The virus throws the inflammatory switch that leaks the vessels: dengue activates NF-κB in infected and immune cells, driving the cytokine surge that makes capillaries leak plasma — the core of dengue hemorrhagic fever and shock."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "It can misdirect immunity onto the nerves: dengue is among the infections that trigger Guillain-Barré syndrome, an autoimmune attack on peripheral nerve myelin causing ascending weakness in the weeks after the fever."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Shock and muscle breakdown injure the kidneys: dengue causes acute kidney injury through hypotension, hemolysis and rhabdomyolysis, and severe or repeated episodes can leave lasting chronic kidney disease."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "It can strike the brain both ways: dengue is associated with both hemorrhagic stroke from severe thrombocytopenia and ischemic stroke from its vasculopathy and shock, a recognized neurological complication."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Despite the bleeding, it can also clot: the endothelial activation and immobilization of severe dengue, with its DIC physiology, can paradoxically cause venous thromboembolism alongside the hemorrhagic risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Recovery carries a long tail of fatigue and low mood: post-dengue syndrome brings prolonged fatigue, malaise and depression for weeks to months after the acute illness resolves."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "It can leave chronic widespread pain: post-dengue syndrome includes prolonged arthralgia, fatigue and a fibromyalgia-like central pain that can persist for months after the infection clears."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "It inflames the peripheral nerves: dengue can cause a post-infectious neuropathy and Guillain-Barré-type injury, leaving neuropathic pain among its neurological sequelae."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "It transiently suppresses the marrow: dengue infects bone-marrow precursors and drives inflammation that depresses blood-cell production, contributing to anemia during and after the illness."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It earns the name breakbone fever: dengue causes severe myalgia, arthralgia and deep bone pain at its peak, a defining feature so intense it gave the disease its classic nickname."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It writes itself on the skin: dengue produces a flushed face and a characteristic maculopapular rash with 'white islands in a sea of red', and petechiae and bruising as platelets fall."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It inflames the liver and bleeds the gut: dengue commonly raises transaminases with hepatomegaly, and abdominal pain and GI bleeding are warning signs of progression to severe dengue."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Plasma leak floods the lungs: the capillary leak of severe dengue causes pleural effusions and pulmonary oedema, and the most severe cases progress to acute respiratory distress syndrome."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe disease shuts down the kidney: shock, rhabdomyolysis and acute tubular necrosis in severe dengue cause acute kidney injury that worsens prognosis."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It swells nodes and leaks into cavities: tender lymphadenopathy and hepatosplenomegaly are typical, and as capillary integrity fails plasma leaks into the pleural and peritoneal spaces."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It crosses to the fetus: dengue in pregnancy raises the risk of preterm birth, low birth weight and peripartum haemorrhage, and vertical transmission can infect the newborn."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "Some painkillers are dangerous here: NSAIDs like ibuprofen are avoided in dengue because they worsen the bleeding tendency and gastritis of thrombocytopenia, so paracetamol is preferred."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It can disturb the glands: severe dengue is reported to cause transient thyroid dysfunction and, through profound shock, rare pituitary and adrenal insufficiency."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: connects-to
    note: "A flavivirus cousin and immune trap: Zika shares dengue's Aedes vector and produces cross-reactive antibodies that can worsen the other infection through antibody-dependent enhancement, complicating diagnosis and vaccine design."
  - target: 02-pathogen/02-bacteria/salmonella-typhi
    relation: connects-to
    note: "A fever to tell apart: in endemic regions and returning travellers, dengue must be distinguished from typhoid and malaria, overlapping febrile illnesses with very different treatments."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "It crashes the platelets: dengue causes a profound thrombocytopenia through marrow suppression and immune platelet destruction, overlapping mechanistically with immune thrombocytopenia."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "It injures the liver lobule: severe dengue causes midzonal hepatocellular necrosis with Councilman bodies in the liver lobule, and the steep transaminase rise it produces is a warning sign of progression to severe disease."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It can inflame the heart: dengue myocarditis depresses myocardial function and causes arrhythmia in severe disease, contributing — alongside plasma leak — to the shock of dengue haemorrhagic fever."
  - target: 02-pathogen/01-viruses/ebola-virus
    relation: connects-to
    note: "A fellow viral haemorrhagic fever: like Ebola, severe dengue is a viral haemorrhagic fever where endothelial leak, thrombocytopenia and coagulopathy cause bleeding and shock, though dengue's plasma leak dominates over frank haemorrhage."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Dengue acute kidney injury: capillary leak, rhabdomyolysis and immune-complex deposition injure the glomerulus, and AKI marks severe dengue and predicts mortality."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Plasma leak floods the lungs: severe dengue's vascular leak fills the pleura and alveoli, and pulmonary haemorrhage and ARDS at the gas-exchange surface mark its most dangerous form."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Antibody-dependent enhancement: cross-reactive antibodies from a prior serotype, made in germinal centres, can paradoxically worsen a second dengue infection by ferrying virus into macrophages."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Plasma leak through the vessel: dengue's severe form leaks plasma across a cytokine-damaged endothelium of the arterial wall and capillaries, causing the shock and effusions of dengue haemorrhagic fever."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Cardiac dengue: dengue commonly causes bradycardia and conduction abnormalities, and a viral myocarditis, affecting the cardiac conduction system even in non-severe disease."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Overlapping fevers: dengue and COVID-19 co-circulate in many regions and share early features—fever, myalgia, thrombocytopenia and cytokine-driven illness—posing a diagnostic and co-infection challenge."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Viral RNA sensing: RIG-I detects dengue's RNA and signals through MAVS to trigger interferon, and the virus's NS proteins antagonise this sensor to blunt the early antiviral response."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement and leak: excessive complement activation generates anaphylatoxins that help drive the vascular permeability and plasma leakage of dengue haemorrhagic fever and shock."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Peripheral neuropathy: beyond Guillain-Barré, dengue can injure peripheral nerves directly, causing mononeuropathies, brachial neuritis and post-infectious neuropathic syndromes."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Vascular leak cytokine: IL-1β from inflammasome-activated monocytes contributes to the endothelial permeability and plasma leakage of severe dengue."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome activation: dengue virus and platelet activation trigger the NLRP3 inflammasome, whose IL-1β release drives the vascular leak of dengue haemorrhagic fever."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Antiviral and immunopathic: IFN-γ from T and NK cells helps control dengue but, in secondary infection, contributes to the cytokine surge behind severe disease."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial destabilisation: a surge in angiopoietin-2 over angiopoietin-1 disrupts the Tie2-stabilised endothelium in severe dengue, a key driver of the plasma leak that causes dengue shock syndrome."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: complement activation through to C5 contributes to the endothelial injury and vascular permeability of severe dengue, part of the immunopathology of haemorrhagic disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte target and recruitment: CCL2 recruits the monocytes that are dengue's principal host cell, amplifying infection and the inflammatory response that drives vascular leak."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endothelial activation: dengue activates the endothelium to release von Willebrand factor, contributing to the platelet consumption and vascular dysfunction behind the bleeding and plasma leak of severe disease."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Thrombocytopenia: dengue causes marrow suppression and peripheral platelet consumption, and the thrombopoietin-driven recovery of platelet counts tracks the resolution of the thrombocytopenia central to the disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "T-cell immunopathology: in secondary dengue infection, cross-reactive CD8 T cells deploy perforin in a way that injures the endothelium, contributing to the immunopathological plasma leak of severe dengue."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Maternal-antibody enhancement: FcRn transfers maternal anti-dengue IgG across the placenta, and as it wanes to sub-neutralising levels it can enhance rather than protect, explaining the peak of severe dengue in infants of previously infected mothers."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Consumptive coagulopathy: severe dengue activates and consumes the coagulation system, lowering fibrinogen and producing the disseminated intravascular coagulation that, with thrombocytopenia, drives the bleeding of dengue haemorrhagic fever."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Vascular permeability: kinin-system activation generating bradykinin increases endothelial permeability in severe dengue, contributing alongside the viral NS1 protein to the plasma leak that defines dengue shock syndrome."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Severity biomarker: IL-10 rises sharply in severe dengue, and its immunosuppressive action — blunting antiviral T-cell responses — tracks with and helps predict progression to dengue haemorrhagic fever and shock syndrome."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: dysregulated nitric oxide signalling in the dengue-infected endothelium contributes to the loss of vascular barrier integrity that underlies the plasma leak of severe disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 permeability: IL-17A is elevated in severe dengue and amplifies endothelial inflammation and vascular permeability, adding to the cytokine-driven leak that characterises dengue haemorrhagic fever."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Interferon evasion: dengue NS5 degrades STAT2 to block JAK-STAT interferon signalling (type-I interferon and STAT1 already mapped), a key immune-evasion strategy that permits high viral replication."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate inflammatory drive: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped) contributes to the inflammatory cytokine response that drives the vascular permeability of severe dengue."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Haemorrhagic coagulopathy: activation of coagulation generates thrombin and, with thrombocytopenia, produces the bleeding diathesis and disseminated intravascular coagulation of severe dengue haemorrhagic fever."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling is engaged during dengue-virus entry and replication and contributes to the endothelial activation of severe dengue."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Dengue virus exploits PI3K-AKT signalling to support replication and delay apoptosis in infected cells."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 contributes to the endothelial dysfunction and vascular permeability underlying the plasma leakage of severe dengue."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response that drives the vascular leak and plasma leakage of severe dengue."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Dengue virus exploits PI3K-AKT signalling (AKT already mapped) to support its replication and modulate the survival of infected cells."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling shapes the endothelial and immune responses that contribute to the vascular permeability of severe dengue."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial and immune-cell responses to dengue virus."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α contributes to the vascular permeability and metabolic reprogramming of the plasma-leakage phase of severe dengue."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the myeloid inflammation and correlate with disease severity in dengue."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the innate inflammatory signaling and endothelial activation relevant to the vascular leak of severe dengue."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Dengue virus induces and subverts host autophagy to support its replication and lipid metabolism."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling, exploited by dengue for its lipid-dependent replication, participates in dengue infection."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the endothelial barrier dysfunction and vascular leak of severe dengue."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the immune response and immunopathology of dengue fever."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation modulates the host immune-cell responses to dengue virus infection."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and endothelial responses of dengue fever."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial activation and vascular leakage of dengue fever."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling, exploited by dengue virus for replication, participates in the host response to dengue fever."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the antiviral and immune gene programs of dengue fever."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of the immune response to dengue fever."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the immunomodulation and vascular-permeability responses of dengue fever."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Haemoconcentration: the plasma leakage of severe dengue concentrates the blood, and a rising haematocrit and haemoglobin is a cardinal warning sign of impending dengue shock, while haemorrhage can conversely drop it."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Immunity and vaccine: MHC class II-restricted T-cell help shapes dengue immunity and vaccine responses, and cross-reactive immunity from a prior serotype underlies the antibody-dependent enhancement (IgG already mapped) that worsens secondary infection."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell response: IL-2-driven T-cell expansion contributes to dengue immunity, but cross-reactive memory T cells from a previous serotype can produce a suboptimal, inflammation-amplifying response (original antigenic sin) in secondary infection."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Dengue myocarditis: dengue can cause myocarditis and myocardial dysfunction, and troponin elevation marks the cardiac injury of this recognised manifestation of severe infection that contributes to the shock of dengue."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Coagulopathy: severe dengue consumes the natural anticoagulant protein C, and this with thrombocytopenia and the fibrinogen and thrombin derangements already mapped drives the bleeding and disseminated intravascular coagulation of dengue haemorrhagic fever."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative endothelial injury: oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, damages the endothelium (already mapped) in severe dengue, adding to the vascular dysfunction behind the plasma leak."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Fever and permeability: prostaglandins from the inflammatory response (IL-6, TNF and histamine already mapped) drive the fever and contribute to the vascular permeability behind the plasma leak of severe dengue."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Falling cholesterol: serum cholesterol and LDL fall in severe dengue, reflecting the hepatic (liver already mapped) dysfunction and the metabolic disturbance, and the drop tracks with disease severity and plasma leak."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Hypocalcaemia: hypocalcaemia is common in severe dengue and correlates with severity and plasma leak, part of the electrolyte derangement (sodium already mapped) of the vascular and metabolic disturbance."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 response: IL-4 and the type-2 cytokine skewing shape the T-cell response to dengue, and the cross-reactive memory (immunoglobulin G already mapped) of secondary infection contributes to the immunopathology of severe disease."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hyperferritinaemia: the intense inflammation (IL-6 already mapped) of severe dengue raises hepcidin and ferritin, the hyperferritinaemia a marker of severity that reflects the macrophage activation of the disease."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron sequestration: the hepcidin-driven (already mapped) iron sequestration of the severe dengue inflammatory response contributes to the hyperferritinaemia and the transient anaemia (haemoglobin already mapped) of the illness."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), is part of the type-2 immune arm of the dengue response, contributing to the cytokine milieu of the illness."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Marrow suppression: the dengue virus suppresses the bone marrow (thrombopoietin already mapped), causing the thrombocytopenia and leukopenia that are hallmarks of the acute febrile illness."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cross-reactive T-cell immunopathology: the cross-reactive memory cytotoxic T cells (perforin already mapped) from a prior serotype contribute, with the antibody-dependent enhancement (immunoglobulin already mapped), to the immunopathology of severe secondary dengue."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "ADE target: the dengue virus infects the macrophages/monocytes, and the antibody-dependent enhancement (immunoglobulin already mapped) increases the FcγR-mediated uptake, amplifying the severe secondary dengue."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Dengue hepatitis: the dengue causes the hepatocyte infection and the transaminitis/hepatitis of the liver, a marker of the disease severity."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "DC-SIGN target: the dengue virus targets the DC-SIGN-expressing dendritic cells, the skin (Aedes-bite) entry and the initial infection."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the antiviral immune response to the dengue virus."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin links the metabolic state to the immune response and is associated with the severity of the dengue plasma-leak syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, a pro-inflammatory adipokine, is elevated in severe dengue and correlates with the plasma leak (endothelial already mapped) and severity."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune response to the dengue virus."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune response and the vascular inflammation of dengue."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), arms the mast cells (already mapped) whose degranulation contributes to the vascular permeability of severe dengue."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the complement-mediated endothelial (already mapped) activation and vascular leak of severe dengue."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the dengue-virus NS1 protein recruits the host factor H to regulate the complement (C3, C5 and C5aR1 already mapped), while the NS1–complement interaction also contributes to the vascular leak of severe dengue."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact (bradykinin already mapped) systems whose activation drives the plasma leakage of dengue haemorrhagic fever."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Glycocalyx/matrix leak: the endothelial glycocalyx and the collagen basement membrane are degraded during the NS1-driven vascular injury, contributing to the plasma leakage of severe dengue."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Immune-activation matricellular: osteopontin, a matricellular cytokine, is part of the strong pro-inflammatory immune activation of the acute dengue infection."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Acute-phase iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the acute-phase response to the dengue infection."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-dengue axis: TSLP, from dengue-infected keratinocytes and epithelial cells, primes dendritic cells (already mapped) and amplifies the Th2 immune skew and the aberrant cytokine production of the severe dengue immunopathology."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "EPO-dengue axis: erythropoietin, induced by dengue-driven anaemia and bone-marrow (already mapped) suppression, mobilises erythroid progenitors and modulates macrophage (already mapped) polarisation in the haematopoietic recovery of dengue fever."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Vascular-remodelling axis: periostin, from the activated endothelial cells (already mapped) and fibroblasts, contributes to the vascular remodelling and repair after the endothelial leak that defines the severe dengue vascular permeability syndrome."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-dengue axis: melatonin, via MT1/MT2 receptors and its antioxidant activity, modulates the oxidative stress of the NS1-driven endothelial (already mapped) injury and the vascular permeability of severe dengue fever."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone dengue axis: testosterone, via androgen receptors on immune effectors (macrophages and T cells already mapped), modulates the sex-differential dengue-fever severity and the inflammatory cytokine response."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet-serotonin dengue axis: serotonin, released by the dengue-virus-activated and the dengue-driven thrombocytopenic platelets (already mapped), amplifies the vascular permeability and the bleeding tendency of severe dengue fever."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Dengue prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune response; hyperprolactinaemia amplifies the NF-κB (already mapped) and TNF-α (already mapped) hyperinflammatory cascade of dengue fever."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Dengue oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates vascular inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) hyperinflammatory cascade of dengue fever."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Dengue vasopressin: vasopressin, via V2R on macrophages (already mapped) and neutrophils (already mapped), modulates vascular fluid homeostasis; vasopressin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of dengue fever."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Dengue selenium: selenium, as GPx in macrophages (already mapped) and endothelial cells (already mapped), scavenges NS1-driven ROS; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) vascular-leak cascade of dengue fever."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Dengue iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) and endothelial (already mapped) function; iodine deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) vascular-leak cascade of dengue fever."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Dengue magnesium: magnesium, as cofactor of immune enzymes in macrophages (already mapped) and T cells (already mapped), restrains NF-κB (already mapped) and TNF-α (already mapped); magnesium deficiency amplifies the hyperinflammatory vascular-leak cascade of dengue fever."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Dengue copper: copper in macrophages (already mapped) and endothelial cells (already mapped) scavenges NS1-driven ROS; copper deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Dengue zinc: zinc cofactors macrophage (already mapped) and endothelial (already mapped) anti-inflammatory function; zinc deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) hyperinflammatory vascular cascade of dengue fever."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Dengue phosphorus: phosphorus, as ATP in macrophages (already mapped) and endothelial cells (already mapped), fuels repair signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of dengue fever."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "chloride channels on macrophage (already mapped) and endothelial cell (already mapped) regulate membrane potential; chloride dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "sulfur, as glutathione precursor in macrophage (already mapped) and endothelial cell (already mapped), counters NS1-driven ROS; sulfur deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "nitrogen, as nitric oxide (already mapped) precursor in macrophage (already mapped) and endothelial cell (already mapped), modulates antiviral innate immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) cascade of dengue fever."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "dengue carbon: carbon in nucleotides fuels macrophage (already mapped) and endothelial cell (already mapped) viral replication; carbon dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "dengue oxygen: oxygen via ROS from macrophage (already mapped) and endothelial cell (already mapped) modulates viral cytopathology; oxygen excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "dengue pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses antiviral immunity; pd-1 dysfunction amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "dengue-fever glp-1: GLP-1 from macrophages (already mapped) and endothelial cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of dengue fever."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "dengue-fever angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes vascular permeability; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of dengue fever."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "dengue-fever wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and endothelial cells (already mapped) regulates tone; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of dengue fever."
---

# Dengue Fever

## Overview

**Dengue fever** is the most prevalent arboviral disease globally, caused by **dengue virus (DENV)** — a positive-sense single-stranded RNA virus of the *Flaviviridae* family (genus *Flavivirus*), with four antigenically distinct serotypes (DENV-1 through DENV-4). Transmitted by the bite of infected *Aedes aegypti* (primary vector) and *Aedes albopictus* mosquitoes, dengue causes an estimated **400 million infections annually** across 128 countries, with ~100 million symptomatic cases and 22,000 deaths, primarily in tropical and subtropical regions [^bhatt-2013-dengue-burden].

The **central immunological challenge** of dengue is the phenomenon of **antibody-dependent enhancement (ADE)**: prior immunity to one DENV serotype does not protect against and can actually exacerbate infection by a different serotype — through subneutralizing antibodies that enhance viral uptake by Fc-receptor-bearing cells (monocytes/macrophages) → higher viral load → more severe disease. This ADE biology has frustrated vaccine development for decades and remains the dominant constraint on dengue vaccine deployment.

**Clinical spectrum:**
- **Dengue fever (DF)**: Fever, severe headache, retro-orbital pain, myalgia/arthralgia ("breakbone fever"), rash; self-limiting ~7 days
- **Dengue hemorrhagic fever (DHF)**: Plasma leakage (hematocrit rise ≥20%, pleural effusion/ascites), thrombocytopenia, hemorrhagic manifestations
- **Dengue shock syndrome (DSS)**: DHF + circulatory failure (narrow pulse pressure or hypotension); mortality ~1-5% with proper management

## Structure

### Dengue virus biology

DENV is a spherical enveloped virus (~50 nm):

- **Genome**: 10.7 kb positive-sense ssRNA; single open reading frame → polyprotein → cleaved into 3 structural + 7 non-structural proteins
- **Structural proteins**:
  - **C (capsid)**: Nucleocapsid core protein
  - **prM/M (precursor membrane/membrane)**: Furin-cleaved during maturation; immature virions (prM) are less infectious
  - **E (envelope)**: Major surface glycoprotein; receptor binding (AXL, DC-SIGN, heparan sulfate); fusion at endosomal pH 5-6; target of neutralizing antibodies
- **Non-structural (NS) proteins**:
  - **NS1**: Secreted hexamer; diagnostic antigen; activates TLR4 on endothelium → plasma leakage; disrupts endothelial junction proteins
  - **NS3/NS2B**: Serine protease (cleaves polyprotein) + RNA helicase; immune evasion (MAVS, STING disruption)
  - **NS5**: RNA-dependent RNA polymerase + cap methyltransferase; degrades STAT2 → IFN evasion

### DENV entry

1. E protein binds DC-SIGN (CD209), AXL, heparan sulfate proteoglycans on dendritic cells and macrophages
2. Clathrin-mediated endocytosis → endosomal acidification → E protein conformational change → membrane fusion → RNA release into cytoplasm
3. DENV replication on ER-derived replication compartments → assembly → budding into ER lumen → Golgi maturation → secretion

## Function

### Immune response timeline

| Phase | Time | Host response | Viral countermeasures |
|-------|------|---------------|----------------------|
| Early innate | 0–24 h | RIG-I/MDA5 → MAVS → IFN-β | NS4B blocks RIG-I; NS2B/NS3 cleaves MAVS |
| Amplification | 24–48 h | pDC IFN-α; NK cell activation; CXCL10 recruitment | NS5 degrades STAT2; JAK-STAT blocked |
| Adaptive | Day 4–7 | Virus-specific CD8+ T cells; neutralizing IgM | Cytokine storm from T cell cross-reactivity |
| Febrile phase | Day 2–7 | Fever, myalgia; viremia peaks Day 4–5 | — |
| Critical phase | Day 4–6 | Plasma leakage (secondary infection); thrombocytopenia | ADE enhances monocyte infection → NS1-TLR4 vascular leak |
| Recovery | Day 6–7+ | Reabsorption of leaked fluid; platelet recovery | — |

### Antibody-dependent enhancement (ADE)

In secondary heterotypic infection (different serotype):

1. Pre-existing non-neutralizing anti-DENV IgG (from previous serotype) binds virions
2. Immune complexes bind Fcγ receptors (FcγRIIA/FcγRI) on monocytes/macrophages → enhanced viral entry
3. Higher viral load in macrophages → increased cytokine production (TNF-α, IL-6, IL-10)
4. IL-10 suppresses antiviral T cell responses → more permissive infection
5. T cell cross-reactivity (original antigenic sin): memory T cells from prior serotype activated → cytokine storm without efficient viral clearance

ADE is most dangerous with DENV-2 secondary to DENV-1 primary infection; explains why DHF and DSS occur predominantly in secondary infections.

## Pathology

### Vascular leak mechanism

Central to DHF/DSS pathogenesis:

- **NS1-TLR4 axis**: Secreted NS1 hexamer → TLR4 on vascular endothelium → NF-κB → CXCL1, IL-8 → endothelial activation; NS1 also disrupts glycocalyx (by activating endothelial sialidase) → junction protein degradation → plasma leakage
- **Complement activation**: NS1 activates complement via C4b-binding protein → C5a → mast cell degranulation → histamine → vascular permeability
- **T cell cytokine storm**: DENV-specific T cells produce IFN-γ, TNF-α, LTA → endothelial activation

### Thrombocytopenia

- Direct BM suppression: DENV infects megakaryocyte precursors → reduced platelet production
- Platelet destruction: Autoantibodies (anti-platelet NS1 antibodies — molecular mimicry); complement-mediated platelet lysis
- Platelet consumption: Endothelial activation → platelet aggregation and consumption

### Diagnosis

- **NS1 antigen RDT**: Positive Day 1–5 (viremic phase); ~80% sensitivity; preferred for febrile phase
- **IgM/IgG serology**: Positive from Day 4; IgG-dominant in secondary infection; dengue NS1 IgG correlates with ADE risk
- **RT-PCR**: Gold standard Day 1–5; not routinely available in endemic regions
- **CBC**: Leukopenia + thrombocytopenia + rising hematocrit = dengue hemorrhagic fever

### Treatment

No approved antiviral therapy for dengue. Management is entirely supportive:

- **Oral hydration** for uncomplicated dengue fever
- **IV crystalloid** (NOT colloid) for plasma leakage; careful fluid balance (risk of fluid overload in recovery phase)
- **Paracetamol** for fever/pain (avoid NSAIDs — antiplatelet effect; avoid corticosteroids — no benefit, potential harm)
- **Platelet transfusion**: Only for active significant bleeding + platelets <20,000/μL; prophylactic transfusion not recommended
- **Critical monitoring**: Hematocrit, urine output, hemodynamic status during critical phase (Day 4–6)

### Vaccines

**Dengvaxia (CYD-TDV; Sanofi Pasteur)**: Live-attenuated chimeric tetravalent (yellow fever backbone + DENV1-4 prM/E). FDA-approved 2019 but **restricted to individuals 9–45 years with documented prior dengue infection** — seronegative recipients had increased severe dengue risk (through ADE mechanism with waning vaccine-induced immunity). Mass vaccination program in Philippines caused public health controversy.

**TAK-003 (Qdenga; Takeda)**: Live-attenuated tetravalent (DENV-2 backbone). EU-approved 2022; WHO prequalified 2023; efficacy 80% against symptomatic dengue (3 years post-vaccination); can be given regardless of prior serostatus (though seropositive recipients have higher protection). Active rollout in endemic countries.

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: DENV positive-sense ssRNA activates RIG-I and MDA5 → MAVS → IFN-β; DENV evades MAVS by: NS4B blocking RIG-I signaling, NS2B/NS3 protease disrupting MAVS, NS5 targeting STAT2 for degradation; early robust IFN-β correlates with mild dengue; IFN evasion drives severe disease.

**→ [TLR4](../../../03-molecular/tlr4/)**: Dengue NS1 protein activates TLR4 on endothelial cells: NS1 hexamer → TLR4/MD-2 → NF-κB → CXCL1, IL-8 → endothelial permeability and plasma leakage; TLR4-mediated NS1 endothelial activation is a key mechanism of dengue hemorrhagic fever; anti-TLR4 may reduce plasma leakage.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: Dengue actively evades type I IFN: NS5 targets STAT2 for ubiquitin-mediated degradation → blocks IFNAR-JAK1/TYK2/STAT1/STAT2 signaling; NS2B/NS3 inhibit IRF3; early IFN-β (first 24 h) limits viral replication; delayed IFN induction after immune evasion correlates with severe dengue.

**→ [cGAS-STING](../../../03-molecular/cgas-sting/)**: Dengue evades both RNA (MAVS) and DNA (cGAS-STING) sensing: mitochondrial DNA released during dengue-induced apoptosis → cGAS → cGAMP → STING; however, DENV NS2B/NS3 disrupts STING signaling; dengue-mtDNA-cGAS-STING axis activates inflammatory cytokines during severe dengue.

**→ [STAT1](../../../03-molecular/stat1/)**: DENV NS5 degrades STAT2 via UBR4 → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 selectively targets human STAT2 (not mouse) → human-specific IFN evasion; STAT2 degradation is a major determinant of dengue viremia and is absent in murine dengue models.

**→ [Zika Virus](../zika-virus/)**: ZIKV and DENV share Aedes aegypti vector and flavivirus biology; cross-reactive anti-DENV antibodies may enhance ZIKV infection via ADE in Fcγ receptor-bearing cells; prior dengue immunity has complex effects on Zika severity; both NS5 proteins degrade STAT2 for IFN evasion.

**→ [West Nile Virus](../west-nile-virus/)**: WNV and DENV share flavivirus biology and NS5-mediated STAT1/STAT2 evasion; anti-DENV IgG cross-reacts with WNV E protein but provides limited protection; WNV causes neuroinvasive disease (encephalitis, AFP) not seen in DENV; both lack approved antivirals.

**→ [Aedes aegypti](../../../../02-pathogen/06-environmental/aedes-aegypti/)**: Dengue is spread by the day-biting Aedes aegypti mosquito, which also carries Zika, chikungunya, and yellow fever; its spread into the warming, urbanizing tropics is why dengue now causes ~400 million infections a year, and vector control remains a mainstay of prevention.

**→ [Macrophage](../../04-cellular/macrophage/)**: Macrophages are dengue's main host cell and engine of severe disease: in reinfection with another serotype, non-neutralizing antibodies ferry virus into Fcγ-bearing macrophages — antibody-dependent enhancement — raising viral load and the cytokines that drive hemorrhagic dengue.

**→ [Cytokine Storm](../cytokine-storm/)**: Severe dengue is partly a cytokine storm: antibody-enhanced macrophage infection plus cross-reactive memory T cells pour out TNF-α, IL-6, and IFN-γ that — with NS1 acting on the endothelium — break vascular integrity, causing the plasma leak of dengue hemorrhagic fever and shock.

- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Severe dengue is a disease of the endothelium: viral NS1 protein and cytokines transiently disrupt the endothelial glycocalyx and tight junctions, causing the plasma leakage (hemoconcentration, effusions, shock) that defines dengue hemorrhagic fever and dengue shock syndrome.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Severe dengue can trigger disseminated intravascular coagulation: endothelial injury, thrombocytopenia and cytokine-driven tissue-factor activation consume clotting factors, producing the bleeding of dengue hemorrhagic fever; DIC marks the severe end and worsens shock.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a key dengue target: the virus replicates in hepatocytes and Kupffer cells, raising transaminases in most cases and occasionally causing fulminant hepatitis; marked AST/ALT elevation is a warning sign of progression to severe dengue and correlates with bleeding.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thrombocytopenia defines severe dengue: the virus suppresses marrow megakaryopoiesis and antibodies destroy platelets, while plasma leak concentrates the blood—so a falling platelet count with rising hematocrit warns of progression to dengue hemorrhagic fever.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dengue virus first infects dendritic cells via DC-SIGN: skin dendritic cells captured at the mosquito bite are the earliest replication site and carry the virus onward, and antibody-dependent enhancement on a second infection worsens this uptake—driving severe dengue.
- `connects-to` → **[Malaria](../malaria/README.md)** — Dengue and malaria are the two great mosquito-borne tropical fevers and key differentials: both cause fever, thrombocytopenia, and can be severe, but dengue (Aedes flavivirus) brings plasma leak and hemorrhage while malaria (Plasmodium) brings hemolysis and cerebral disease.
- `connects-to` → **[Dengue virus](../../../02-pathogen/01-viruses/dengue-virus/README.md)** — Dengue virus drives the disease through four serotypes: infection gives lasting immunity to one serotype but only brief cross-protection, so later infection by a different serotype risks severe dengue—the serotype diversity central to the virus's danger.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Pre-existing IgG can worsen dengue via antibody-dependent enhancement: non-neutralizing antibodies from a prior serotype bind the new virus and ferry it into macrophages, boosting viral load—why second heterotypic infections cause severe, hemorrhagic dengue.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Dengue suppresses the bone marrow: the virus infects marrow progenitors and dampens production, causing the falling platelet and white-cell counts that define and grade the illness—so cytopenias track severity and signal the risk of hemorrhage.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells help drive severe dengue: cross-reactive memory T cells from a prior dengue serotype respond suboptimally on reinfection, releasing cytokines that worsen vascular leak—part of why a second, different-serotype infection is the dangerous one.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Dengue's danger is immunological: antibodies from a first infection can enhance uptake of a second serotype (antibody-dependent enhancement), amplifying viral load and the immune overreaction that causes plasma leak—so prior immunity paradoxically raises severe-dengue risk.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Dengue can invade the nervous system: beyond classic fever and bleeding, the virus and its immune response cause encephalitis, Guillain-Barré-like syndromes and stroke, so neurological dengue is an increasingly recognized severe manifestation.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Dengue's danger lies in B-cell antibodies: non-neutralizing antibodies from a prior infection can enhance a second one (antibody-dependent enhancement), so partial immunity worsens disease—the paradox that makes dengue vaccines hard to design.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Severe dengue is a cardiovascular emergency: cytokines make capillaries leak plasma, dropping blood volume into dengue shock syndrome, so careful fluid management—not antivirals—is what saves lives in the critical phase.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Severe dengue can injure the kidney: shock, hemolysis, and direct viral effects cause acute kidney injury in the critical phase, so renal function is watched closely as a marker of severity and a target for supportive care.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Severe dengue is defined by leaking albumin: the virus makes capillaries leak, so plasma and albumin escape into the chest and belly, concentrating the blood and dropping pressure into the shock that makes dengue hemorrhagic fever deadly.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help make dengue severe: infection activates them to release chymase and vasoactive mediators that pull apart vascular junctions, driving the plasma leak of severe dengue—and blood chymase levels track with disease severity.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Dengue can inflame the heart: the virus causes myocarditis with weakened contraction and arrhythmias, an underrecognized contributor to the shock and fluid-balance problems that complicate severe infection.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Severe dengue leaks plasma via VEGF: the virus and the immune response drive VEGF that loosens the junctions between endothelial cells, so fluid escapes the vessels into tissues—the plasma leakage behind dengue shock syndrome.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Dengue often drops blood sodium: plasma leakage, vomiting and fluid shifts cause hyponatremia, a common electrolyte disturbance in severe disease that worsens confusion and must be corrected carefully during fluid resuscitation.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Dengue enlarges and endangers the spleen: viral replication and immune activation swell the organ, and in rare cases the engorged spleen ruptures—a life-threatening bleed to consider in a dengue patient with sudden abdominal pain.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Severe dengue acidifies the blood: massive plasma leakage drops blood pressure into dengue shock, and the underperfused tissues generate lactic acid, so metabolic acidosis is a marker of the dangerous phase.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Dengue can invade the brain: beyond the classic fever, severe disease causes encephalitis and encephalopathy with seizures and altered consciousness, part of the expanded dengue syndrome.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells meet dengue early: they mount a rapid antiviral attack in the first days of infection, and the strength of this innate response helps shape whether the illness stays mild or turns severe.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ultrasound and X-ray photons catch dengue's plasma leak: pleural effusions, ascites and a thickened gallbladder wall reveal the capillary leakage that marks the dangerous critical phase.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Dengue's capillary leak floods the chest: plasma seeps into the pleural space, causing effusions and, in severe cases, respiratory distress, part of the third-spacing of dengue shock.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Dengue disturbs potassium: hypokalemia is common in the acute phase, while kidney injury in severe disease can drive it up, so electrolytes are watched closely during the critical leak phase.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows dengue's two threats: the small icosahedral flavivirus replicating in scaffolds of host membrane, and the widened junctions between endothelial cells through which plasma leaks in severe disease.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Dengue paints the skin: a flushed rash gives way to the petechiae of falling platelets and the classic 'islands of white in a sea of red,' and a tourniquet test bringing out spots warns of bleeding risk.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Dengue can blur vision weeks in: dengue maculopathy with retinal hemorrhage, edema, and foveolitis appears around the time platelets bottom out, sometimes leaving lasting blind spots.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody is dengue's double-edged sword: it diagnoses infection (IgM, NS1) and confers serotype immunity, but partial antibody from a prior serotype enhances a second infection (ADE), making the repeat illness far more dangerous.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — A rising hematocrit signals the danger: as plasma leaks from the vessels in severe dengue, the red cells concentrate, so a climbing hematocrit (hemoconcentration) is a key warning sign that shock may be near.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Dengue drops the white count: a marked leukopenia, with falling neutrophils, is an early and characteristic feature that — alongside the plunging platelets — helps point to the diagnosis.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha opens the vessels in severe dengue: the cytokine storm's TNF loosens endothelial junctions, and this surge in vascular permeability is what drives the plasma leak, hemoconcentration and shock that define dengue hemorrhagic fever.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Old immunity makes the second infection worse: cross-reactive memory helper T cells from a prior dengue serotype respond to the new one with a distorted, overexuberant cytokine burst — 'original antigenic sin' that helps tip a repeat infection into severe disease.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Dengue can inflame the pancreas: the virus is a recognized cause of acute pancreatitis, with abdominal pain and raised enzymes appearing in severe cases, one of the visceral complications that can accompany the plasma-leak phase.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 helps spring the vascular leak: the cytokine surge of severe dengue, with IL-6 prominent, loosens the endothelial barrier and drives the plasma leakage and shock that define dengue hemorrhagic fever.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — The leaking plasma can flood the lungs: severe dengue causes pleural effusions and, at its worst, acute respiratory distress syndrome, the capillary leak filling the alveoli as it does the body cavities.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Dengue can strike the heart: viral myocarditis depresses contractility and causes arrhythmia, so cardiac dysfunction and heart failure add to the shock of the severe disease.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine helps spring the leak: mast-cell histamine released during dengue widens endothelial junctions, contributing to the vascular permeability and plasma leakage that define severe dengue, and its levels track disease severity.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Dengue is hepatotropic: the virus replicates in hepatocytes, and the resulting liver-cell injury raises transaminases and, in severe cases, causes the acute liver failure that worsens the bleeding and shock.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Severe dengue mimics and invites sepsis: dengue shock syndrome resembles septic shock, and the gut-barrier breakdown and immune exhaustion of severe disease open the door to secondary bacterial sepsis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The virus throws the inflammatory switch that leaks the vessels: dengue activates NF-κB in infected and immune cells, driving the cytokine surge that makes capillaries leak plasma — the core of dengue hemorrhagic fever and shock.
- `connects-to` → **[Guillain-Barré Syndrome](../../05-tissue/guillain-barre/README.md)** — It can misdirect immunity onto the nerves: dengue is among the infections that trigger Guillain-Barré syndrome, an autoimmune attack on peripheral nerve myelin causing ascending weakness in the weeks after the fever.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Shock and muscle breakdown injure the kidneys: dengue causes acute kidney injury through hypotension, hemolysis and rhabdomyolysis, and severe or repeated episodes can leave lasting chronic kidney disease.
- `connects-to` → **[Stroke](../stroke/README.md)** — It can strike the brain both ways: dengue is associated with both hemorrhagic stroke from severe thrombocytopenia and ischemic stroke from its vasculopathy and shock, a recognized neurological complication.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Despite the bleeding, it can also clot: the endothelial activation and immobilization of severe dengue, with its DIC physiology, can paradoxically cause venous thromboembolism alongside the hemorrhagic risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Recovery carries a long tail of fatigue and low mood: post-dengue syndrome brings prolonged fatigue, malaise and depression for weeks to months after the acute illness resolves.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — It can leave chronic widespread pain: post-dengue syndrome includes prolonged arthralgia, fatigue and a fibromyalgia-like central pain that can persist for months after the infection clears.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — It inflames the peripheral nerves: dengue can cause a post-infectious neuropathy and Guillain-Barré-type injury, leaving neuropathic pain among its neurological sequelae.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — It transiently suppresses the marrow: dengue infects bone-marrow precursors and drives inflammation that depresses blood-cell production, contributing to anemia during and after the illness.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It earns the name breakbone fever: dengue causes severe myalgia, arthralgia and deep bone pain at its peak, a defining feature so intense it gave the disease its classic nickname.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It writes itself on the skin: dengue produces a flushed face and a characteristic maculopapular rash with 'white islands in a sea of red', and petechiae and bruising as platelets fall.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It inflames the liver and bleeds the gut: dengue commonly raises transaminases with hepatomegaly, and abdominal pain and GI bleeding are warning signs of progression to severe dengue.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Plasma leak floods the lungs: the capillary leak of severe dengue causes pleural effusions and pulmonary oedema, and the most severe cases progress to acute respiratory distress syndrome.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe disease shuts down the kidney: shock, rhabdomyolysis and acute tubular necrosis in severe dengue cause acute kidney injury that worsens prognosis.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It swells nodes and leaks into cavities: tender lymphadenopathy and hepatosplenomegaly are typical, and as capillary integrity fails plasma leaks into the pleural and peritoneal spaces.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It crosses to the fetus: dengue in pregnancy raises the risk of preterm birth, low birth weight and peripartum haemorrhage, and vertical transmission can infect the newborn.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — Some painkillers are dangerous here: NSAIDs like ibuprofen are avoided in dengue because they worsen the bleeding tendency and gastritis of thrombocytopenia, so paracetamol is preferred.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It can disturb the glands: severe dengue is reported to cause transient thyroid dysfunction and, through profound shock, rare pituitary and adrenal insufficiency.
- `connects-to` → **[Zika Virus](../../../02-pathogen/01-viruses/zika-virus/README.md)** — A flavivirus cousin and immune trap: Zika shares dengue's Aedes vector and produces cross-reactive antibodies that can worsen the other infection through antibody-dependent enhancement, complicating diagnosis and vaccine design.
- `connects-to` → **[Salmonella typhi](../../../02-pathogen/02-bacteria/salmonella-typhi/README.md)** — A fever to tell apart: in endemic regions and returning travellers, dengue must be distinguished from typhoid and malaria, overlapping febrile illnesses with very different treatments.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — It crashes the platelets: dengue causes a profound thrombocytopenia through marrow suppression and immune platelet destruction, overlapping mechanistically with immune thrombocytopenia.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — It injures the liver lobule: severe dengue causes midzonal hepatocellular necrosis with Councilman bodies in the liver lobule, and the steep transaminase rise it produces is a warning sign of progression to severe disease.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It can inflame the heart: dengue myocarditis depresses myocardial function and causes arrhythmia in severe disease, contributing — alongside plasma leak — to the shock of dengue haemorrhagic fever.
- `connects-to` → **[Ebola Virus](../../../02-pathogen/01-viruses/ebola-virus/README.md)** — A fellow viral haemorrhagic fever: like Ebola, severe dengue is a viral haemorrhagic fever where endothelial leak, thrombocytopenia and coagulopathy cause bleeding and shock, though dengue's plasma leak dominates over frank haemorrhage.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Dengue acute kidney injury: capillary leak, rhabdomyolysis and immune-complex deposition injure the glomerulus, and AKI marks severe dengue and predicts mortality.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Plasma leak floods the lungs: severe dengue's vascular leak fills the pleura and alveoli, and pulmonary haemorrhage and ARDS at the gas-exchange surface mark its most dangerous form.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Antibody-dependent enhancement: cross-reactive antibodies from a prior serotype, made in germinal centres, can paradoxically worsen a second dengue infection by ferrying virus into macrophages.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Plasma leak through the vessel: dengue's severe form leaks plasma across a cytokine-damaged endothelium of the arterial wall and capillaries, causing the shock and effusions of dengue haemorrhagic fever.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Cardiac dengue: dengue commonly causes bradycardia and conduction abnormalities, and a viral myocarditis, affecting the cardiac conduction system even in non-severe disease.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Overlapping fevers: dengue and COVID-19 co-circulate in many regions and share early features—fever, myalgia, thrombocytopenia and cytokine-driven illness—posing a diagnostic and co-infection challenge.
- `connects-to` → **[RIG-I](../../03-molecular/rig-i/README.md)** — Viral RNA sensing: RIG-I detects dengue's RNA and signals through MAVS to trigger interferon, and the virus's NS proteins antagonise this sensor to blunt the early antiviral response.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement and leak: excessive complement activation generates anaphylatoxins that help drive the vascular permeability and plasma leakage of dengue haemorrhagic fever and shock.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Peripheral neuropathy: beyond Guillain-Barré, dengue can injure peripheral nerves directly, causing mononeuropathies, brachial neuritis and post-infectious neuropathic syndromes.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Vascular leak cytokine: IL-1β from inflammasome-activated monocytes contributes to the endothelial permeability and plasma leakage of severe dengue.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome activation: dengue virus and platelet activation trigger the NLRP3 inflammasome, whose IL-1β release drives the vascular leak of dengue haemorrhagic fever.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Antiviral and immunopathic: IFN-γ from T and NK cells helps control dengue but, in secondary infection, contributes to the cytokine surge behind severe disease.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial destabilisation: a surge in angiopoietin-2 over angiopoietin-1 disrupts the Tie2-stabilised endothelium in severe dengue, a key driver of the plasma leak that causes dengue shock syndrome.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: complement activation through to C5 contributes to the endothelial injury and vascular permeability of severe dengue, part of the immunopathology of haemorrhagic disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte target and recruitment: CCL2 recruits the monocytes that are dengue's principal host cell, amplifying infection and the inflammatory response that drives vascular leak.
- `connects-to` → **[von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Dengue activates the endothelium to release von Willebrand factor, contributing to the platelet consumption and microvascular dysfunction behind the bleeding and plasma leak of severe dengue.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Dengue causes both marrow suppression and peripheral platelet consumption, and thrombopoietin-driven recovery of platelet counts tracks the resolution of the thrombocytopenia that is a defining laboratory feature and bleeding risk.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — In secondary dengue infection, cross-reactive CD8 T cells deploy perforin in a way that injures the endothelium, contributing to the immunopathological plasma leak that drives dengue hemorrhagic fever and shock.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — FcRn transfers maternal anti-dengue IgG across the placenta, and as it wanes to sub-neutralizing levels it can enhance rather than protect, explaining the peak of severe dengue in infants of previously infected mothers.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Severe dengue activates and consumes the coagulation system, lowering fibrinogen and producing the disseminated intravascular coagulation that, with thrombocytopenia, drives the bleeding of dengue hemorrhagic fever.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-system activation generating bradykinin increases endothelial permeability in severe dengue, contributing alongside the viral NS1 protein to the plasma leak that defines dengue shock syndrome.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — IL-10 rises sharply in severe dengue, and its immunosuppressive action—blunting antiviral T-cell responses—tracks with and helps predict progression to dengue hemorrhagic fever and shock syndrome.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Dysregulated nitric oxide signaling in the dengue-infected endothelium contributes to the loss of vascular barrier integrity that underlies the plasma leak of severe disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A is elevated in severe dengue and amplifies endothelial inflammation and vascular permeability, adding to the cytokine-driven leak that characterizes dengue hemorrhagic fever.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Dengue NS5 degrades STAT2 to block JAK-STAT interferon signaling (type-I interferon and STAT1 already mapped), a key immune-evasion strategy that permits high viral replication.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped) contributes to the inflammatory cytokine response that drives the vascular permeability of severe dengue.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Activation of coagulation generates thrombin and, with thrombocytopenia, produces the bleeding diathesis and disseminated intravascular coagulation of severe dengue hemorrhagic fever.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling is engaged during dengue-virus entry and replication and contributes to the endothelial activation of severe dengue.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Dengue virus exploits PI3K-AKT signaling to support replication and delay apoptosis in infected cells.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 contributes to the endothelial dysfunction and vascular permeability underlying the plasma leakage of severe dengue.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response that drives the vascular leak and plasma leakage of severe dengue.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Dengue virus exploits PI3K-AKT signaling (AKT already mapped) to support its replication and modulate the survival of infected cells.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling shapes the endothelial and immune responses that contribute to the vascular permeability of severe dengue.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial and immune-cell responses to dengue virus.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α contributes to the vascular permeability and metabolic reprogramming of the plasma-leakage phase of severe dengue.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the myeloid inflammation and correlate with disease severity in dengue.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the innate inflammatory signaling and endothelial activation relevant to the vascular leak of severe dengue.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Dengue virus induces and subverts host autophagy to support its replication and lipid metabolism.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling, exploited by dengue for its lipid-dependent replication, participates in dengue infection.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the endothelial barrier dysfunction and vascular leak of severe dengue.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the immune response and immunopathology of dengue fever.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation modulates the host immune-cell responses to dengue virus infection.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and endothelial responses of dengue fever.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial activation and vascular leakage of dengue fever.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling, exploited by dengue virus for replication, participates in the host response to dengue fever.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the antiviral and immune gene programs of dengue fever.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of the immune response to dengue fever.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the immunomodulation and vascular-permeability responses of dengue fever.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Haemoconcentration: the plasma leakage of severe dengue concentrates the blood, and a rising haematocrit and haemoglobin is a cardinal warning sign of impending dengue shock, while haemorrhage can conversely drop it.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Immunity and vaccine: MHC class II-restricted T-cell help shapes dengue immunity and vaccine responses, and cross-reactive immunity from a prior serotype underlies the antibody-dependent enhancement (IgG already mapped) that worsens secondary infection.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell response: IL-2-driven T-cell expansion contributes to dengue immunity, but cross-reactive memory T cells from a previous serotype can produce a suboptimal, inflammation-amplifying response (original antigenic sin) in secondary infection.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Dengue myocarditis: dengue can cause myocarditis and myocardial dysfunction, and troponin elevation marks the cardiac injury of this recognised manifestation of severe infection that contributes to the shock of dengue.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Coagulopathy: severe dengue consumes the natural anticoagulant protein C, and this with thrombocytopenia and the fibrinogen and thrombin derangements already mapped drives the bleeding and disseminated intravascular coagulation of dengue haemorrhagic fever.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative endothelial injury: oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, damages the endothelium (already mapped) in severe dengue, adding to the vascular dysfunction behind the plasma leak.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Fever and permeability: prostaglandins from the inflammatory response (IL-6, TNF and histamine already mapped) drive the fever and contribute to the vascular permeability behind the plasma leak of severe dengue.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Falling cholesterol: serum cholesterol and LDL fall in severe dengue, reflecting the hepatic (liver already mapped) dysfunction and the metabolic disturbance, and the drop tracks with disease severity and plasma leak.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Hypocalcaemia: hypocalcaemia is common in severe dengue and correlates with severity and plasma leak, part of the electrolyte derangement (sodium already mapped) of the vascular and metabolic disturbance.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 response: IL-4 and the type-2 cytokine skewing shape the T-cell response to dengue, and the cross-reactive memory (immunoglobulin G already mapped) of secondary infection contributes to the immunopathology of severe disease.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Hyperferritinaemia: the intense inflammation (IL-6 already mapped) of severe dengue raises hepcidin and ferritin, the hyperferritinaemia a marker of severity that reflects the macrophage activation of the disease.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron sequestration: the hepcidin-driven (already mapped) iron sequestration of the severe dengue inflammatory response contributes to the hyperferritinaemia and the transient anaemia (haemoglobin already mapped) of the illness.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), is part of the type-2 immune arm of the dengue response, contributing to the cytokine milieu of the illness.
- `connects-to` → **[Bone marrow](../../05-tissue/bone-marrow/README.md)** — Marrow suppression: the dengue virus suppresses the bone marrow (thrombopoietin already mapped), causing the thrombocytopenia and leukopenia that are hallmarks of the acute febrile illness.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cross-reactive T-cell immunopathology: the cross-reactive memory cytotoxic T cells (perforin already mapped) from a prior serotype contribute, with the antibody-dependent enhancement (immunoglobulin already mapped), to the immunopathology of severe secondary dengue.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — ADE target: the dengue virus infects the macrophages/monocytes, and the antibody-dependent enhancement (immunoglobulin already mapped) increases the FcγR-mediated uptake, amplifying the severe secondary dengue.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Dengue hepatitis: the dengue causes the hepatocyte infection and the transaminitis/hepatitis of the liver, a marker of the disease severity.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — DC-SIGN target: the dengue virus targets the DC-SIGN-expressing dendritic cells, the skin (Aedes-bite) entry and the initial infection.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the antiviral immune response to the dengue virus.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin links the metabolic state to the immune response and is associated with the severity of the dengue plasma-leak syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, a pro-inflammatory adipokine, is elevated in severe dengue and correlates with the plasma leak (endothelial already mapped) and severity.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune response to the dengue virus.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune response and the vascular inflammation of dengue.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), arms the mast cells (already mapped) whose degranulation contributes to the vascular permeability of severe dengue.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the complement-mediated endothelial (already mapped) activation and vascular leak of severe dengue.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the dengue-virus NS1 protein recruits the host factor H to regulate the complement (C3, C5 and C5aR1 already mapped), while the NS1–complement interaction also contributes to the vascular leak of severe dengue.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact (bradykinin already mapped) systems whose activation drives the plasma leakage of dengue haemorrhagic fever.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Glycocalyx/matrix leak: the endothelial glycocalyx and the collagen basement membrane are degraded during the NS1-driven vascular injury, contributing to the plasma leakage of severe dengue.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Immune-activation matricellular: osteopontin, a matricellular cytokine, is part of the strong pro-inflammatory immune activation of the acute dengue infection.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Acute-phase iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the acute-phase response to the dengue infection.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-dengue axis: TSLP, from dengue-infected keratinocytes and epithelial cells, primes dendritic cells (already mapped) and amplifies the Th2 immune skew and the aberrant cytokine production of the severe dengue immunopathology.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — EPO-dengue axis: erythropoietin, induced by dengue-driven anaemia and bone-marrow (already mapped) suppression, mobilises erythroid progenitors and modulates macrophage (already mapped) polarisation in the haematopoietic recovery of dengue fever.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Vascular-remodelling axis: periostin, from the activated endothelial cells (already mapped) and fibroblasts, contributes to the vascular remodelling and repair after the endothelial leak that defines the severe dengue vascular permeability syndrome.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-dengue axis: melatonin, via MT1/MT2 receptors and its antioxidant activity, modulates the oxidative stress of the NS1-driven endothelial (already mapped) injury and the vascular permeability of severe dengue fever.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone dengue axis: testosterone, via androgen receptors on immune effectors (macrophages and T cells already mapped), modulates the sex-differential dengue-fever severity and the inflammatory cytokine response.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet-serotonin dengue axis: serotonin, released by the dengue-virus-activated and the dengue-driven thrombocytopenic platelets (already mapped), amplifies the vascular permeability and the bleeding tendency of severe dengue fever.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Dengue prolactin: prolactin, via PRLR on macrophages (already mapped) and mast cells (already mapped), modulates the immune response; hyperprolactinaemia amplifies the NF-κB (already mapped) and TNF-α (already mapped) hyperinflammatory cascade of dengue fever.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Dengue oxytocin: oxytocin, via OXTR on macrophages (already mapped) and mast cells (already mapped), attenuates vascular inflammation; oxytocin deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) hyperinflammatory cascade of dengue fever.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Dengue vasopressin: vasopressin, via V2R on macrophages (already mapped) and neutrophils (already mapped), modulates vascular fluid homeostasis; vasopressin dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) cascade of dengue fever.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Dengue selenium: selenium, as GPx in macrophages (already mapped) and endothelial cells (already mapped), scavenges NS1-driven ROS; selenium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) vascular-leak cascade of dengue fever.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Dengue iodine: iodine-dependent thyroid hormones modulate macrophage (already mapped) and endothelial (already mapped) function; iodine deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) vascular-leak cascade of dengue fever.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Dengue magnesium: magnesium, as cofactor of immune enzymes in macrophages (already mapped) and T cells (already mapped), restrains NF-κB (already mapped) and TNF-α (already mapped); magnesium deficiency amplifies the hyperinflammatory vascular-leak cascade of dengue fever.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Dengue copper: copper in macrophages (already mapped) and endothelial cells (already mapped) scavenges NS1-driven ROS; copper deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Dengue zinc: zinc cofactors macrophage (already mapped) and endothelial (already mapped) anti-inflammatory function; zinc deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) hyperinflammatory vascular cascade of dengue fever.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Dengue phosphorus: phosphorus, as ATP in macrophages (already mapped) and endothelial cells (already mapped), fuels repair signalling; phosphorus dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of dengue fever.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — chloride channels on macrophage (already mapped) and endothelial cell (already mapped) regulate membrane potential; chloride dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — sulfur, as glutathione precursor in macrophage (already mapped) and endothelial cell (already mapped), counters NS1-driven ROS; sulfur deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — nitrogen, as nitric oxide (already mapped) precursor in macrophage (already mapped) and endothelial cell (already mapped), modulates antiviral innate immunity; nitrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) cascade of dengue fever.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — dengue carbon: carbon in nucleotides fuels macrophage (already mapped) and endothelial cell (already mapped) viral replication; carbon dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — dengue oxygen: oxygen via ROS from macrophage (already mapped) and endothelial cell (already mapped) modulates viral cytopathology; oxygen excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — dengue pd-1: PD-1 on T-cytotoxic cells (already mapped) and macrophages (already mapped) suppresses antiviral immunity; pd-1 dysfunction amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) vascular-leak cascade of dengue fever.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — dengue-fever glp-1: GLP-1 from macrophages (already mapped) and endothelial cells (already mapped) modulates metabolic immune tone; glp-1 dysfunction amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of dengue fever.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — dengue-fever angiotensin-ii: angiotensin II on endothelial cells (already mapped) and macrophages (already mapped) promotes vascular permeability; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of dengue fever.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — dengue-fever wnt-beta-catenin: WNT/β-catenin on macrophages (already mapped) and endothelial cells (already mapped) regulates tone; wnt-beta-catenin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of dengue fever.
