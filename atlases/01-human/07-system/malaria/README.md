---
schema: human-scale-entry/v1
id: malaria
name: Malaria
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Malaria (Plasmodium falciparum primarily) kills ~600,000 annually; Anopheles-transmitted sporozoites → hepatocytes → RBC invasion → haemolysis + fever cycles; artemisinin-based combination therapy is first-line; G6PD and HbS variants confer partial protective advantage."
aliases: ["malaria", "Plasmodium falciparum", "P. falciparum", "P. vivax", "falciparum malaria", "cerebral malaria", "severe malaria", "uncomplicated malaria", "parasitaemia"]
sources:
  - id: who-malaria-report-2023
    type: clinical-guideline
    cite: "World Health Organization. World Malaria Report 2023. WHO; 2023."
    url: "https://www.who.int/teams/global-malaria-programme/reports/world-malaria-report-2023"
    accessed: "2026-06-08"
  - id: white-2014-malaria-lancet
    type: peer-reviewed
    cite: "White NJ, Pukrittayakamee S, Hien TT, et al. Malaria. Lancet. 2014;383(9918):723-735."
    doi: "10.1016/S0140-6736(13)60024-0"
    pmid: "23953767"
    url: "https://doi.org/10.1016/S0140-6736(13)60024-0"
  - id: dondorp-2010-severe-malaria-lancet
    type: peer-reviewed
    cite: "Dondorp AM, Fanello CI, Hendriksen IC, et al. Artesunate versus quinine in the treatment of severe falciparum malaria in African children (AQUAMAT). Lancet. 2010;376(9753):1647-1657."
    doi: "10.1016/S0140-6736(10)61924-1"
    pmid: "21062666"
    url: "https://doi.org/10.1016/S0140-6736(10)61924-1"
cross_links:
  - target: 01-human/03-molecular/g6pd
    relation: connects-to
    note: "G6PD heterozygosity confers ~50% protection vs severe malaria in females (mosaic RBC); G6PD-deficient patients risk haemolysis with primaquine or tafenoquine; WHO mandates G6PD quantitative testing before 8-aminoquinoline prescription."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "HbAS (sickle trait) confers ~60% protection against severe P. falciparum malaria; HbC and thalassaemia trait also protective; P. falciparum digests haemoglobin → haemozoin; Hb variants and G6PD polymorphisms co-distribute with malaria endemicity."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "HbAS (sickle trait) confers ~60% protection against severe malaria (balanced polymorphism); HbSS patients in endemic regions face compounded risk: fever + dehydration → sickling crises; antimalarial prophylaxis planning is essential for HbSS in endemic areas."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Severe falciparum malaria causes AKI in 4-8% (haemoglobinuria + microvascular obstruction + cytokine storm); cerebral malaria + AKI → high mortality; repeated malaria episodes contribute to CKD burden in endemic populations."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Iron deficiency partially protective against P. falciparum (iron-restricted parasites grow less vigorously); iron supplementation in endemic areas should follow malaria treatment to avoid feeding parasites; IDA and malaria co-exist in sub-Saharan Africa."
  - target: 02-pathogen/04-parasites/plasmodium-falciparum
    relation: connects-to
    note: "Plasmodium falciparum, spread by Anopheles mosquitoes, is the deadliest malaria parasite: it cytoadheres infected red cells to brain endothelium via PfEMP1, evades immunity by var-gene switching, and is treated with artemisinin combinations now threatened by kelch13 resistance."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Malaria's blood stage runs in red cells: merozoites invade via AMA1/EBA-glycophorin, digest hemoglobin into haemozoin, and rupture every 48h triggering fever; haemolysis plus dyserythropoiesis causes severe anemia, while inherited RBC variants (HbS, G6PD) blunt parasite growth."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Cerebral malaria is the most lethal complication of P. falciparum: PfEMP1-coated red cells sequester on ICAM-1 in brain microvessels, obstructing flow and breaking the blood-brain barrier → coma; mortality is 15-25%, and ~25% of survivors retain neurological sequelae."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "Both are vector-borne protozoan parasites of the global poor: Anopheles-borne Plasmodium invades erythrocytes, sand-fly-borne Leishmania hides in macrophages; both cause fever, splenomegaly and anemia in overlapping tropical regions, and HIV co-infection worsens both."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Malaria's obligatory pre-erythrocytic stage is hepatic: sporozoites invade hepatocytes and mature into thousands of merozoites before blood-stage disease; P. vivax/ovale form dormant hypnozoites needing primaquine/tafenoquine for radical cure; severe malaria also causes jaundice."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α drives malaria's inflammatory pathology: schizont rupture and GPI anchors trigger macrophage TNF-α → fever, hypoglycemia and ICAM-1 upregulation, promoting PfEMP1-mediated sequestration in cerebral malaria; high circulating TNF-α correlates with severity and mortality."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Thalassemia, like sickle cell trait, is maintained by malaria selection: abnormal or reduced hemoglobin makes red cells a poorer host for Plasmodium, conferring partial protection from severe malaria—why it is common across the historic malaria belt."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is central to malaria: it filters and destroys parasitized red cells, driving the splenomegaly typical of chronic infection, and the parasite evades it by sequestering in deep vasculature—so splenectomy or asplenia markedly worsens malaria severity."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Endemic Burkitt lymphoma is a malaria-driven cancer: chronic Plasmodium falciparum infection causes intense B-cell proliferation and weakens control of co-infecting Epstein-Barr virus, together driving the MYC translocation behind the jaw tumors of African children."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Malaria causes severe anemia by several routes: rupture of infected red cells, splenic clearance of uninfected cells, and inflammatory suppression of erythropoiesis (an anemia-of-chronic-disease component) combine, making anemia a leading cause of malaria death in children."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "Severe falciparum malaria can cause ARDS: sequestration of infected red cells and intense inflammation injure the pulmonary capillaries, flooding alveoli with edema even after parasite clearance—acute respiratory distress is a feared complication of severe malaria."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Severe malaria can trigger disseminated intravascular coagulation: widespread endothelial activation and cytokine storm in falciparum infection consume clotting factors and platelets, causing bleeding—part of the multi-organ failure that makes severe malaria lethal."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Severe malaria injures the kidney: hemolysis and sequestration cause acute kidney injury and, classically, blackwater fever (massive hemoglobinuria), so renal failure marks severe falciparum malaria and worsens its high mortality."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe malaria is partly a cytokine storm: schizont rupture triggers a TNF-driven inflammatory surge causing fever, and excess cytokines contribute to cerebral malaria and organ failure—so the host inflammatory response, not just the parasite, drives lethal disease."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "Malaria and dengue are the great overlapping tropical fevers: both cause fever and thrombocytopenia in the same regions, so a febrile traveler needs both excluded—malaria (a treatable parasite) must never be missed while dengue (a virus) is managed supportively."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Malaria targets the placenta in pregnancy: infected red cells bind a unique placental receptor (CSA) and sequester there, causing maternal anemia, low birth weight, and stillbirth—so first pregnancies in endemic areas carry special risk, prompting preventive treatment."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Cerebral malaria is a disease of the endothelium: infected red cells express adhesion proteins that stick to blood-vessel linings, sequestering in the brain's microvessels, blocking flow and inflaming the barrier—causing the coma that makes falciparum malaria lethal."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Malaria immunity is hard-won and incomplete: repeated infection builds partial 'premunition' that lets endemic adults tolerate parasites, but it wanes without exposure—and this slow, leaky immunity is exactly why an effective malaria vaccine (RTS,S, R21) took so long."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Malaria's silent first stage is in hepatocytes: injected sporozoites invade liver cells and multiply before the blood stage, and in P. vivax and ovale dormant hypnozoites hide there for months—causing relapses that need a separate drug (primaquine) to clear."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide is double-edged in malaria: it helps kill parasites, but in cerebral malaria dysregulated NO and endothelial activation contribute to the coma and brain injury that make it the deadliest complication."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron and malaria are dangerously intertwined: the parasite needs iron to grow, so iron supplementation can worsen malaria in endemic areas—while repeated infection also causes anemia, complicating how iron deficiency is treated where malaria is common."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Severe malaria spills potassium from burst red cells: massive hemolysis and kidney injury raise blood potassium, and the released hemoglobin can darken the urine (blackwater fever)—dangerous electrolyte shifts in the sickest patients."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "The spleen's macrophages fight and are fooled by malaria: they engulf parasitized red cells and the dark hemozoin pigment, enlarging the spleen, yet the parasite's surface tricks sustain infection—and a ruptured malarial spleen is a feared emergency."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Severe malaria activates complement: C3 and the cascade fire on parasite and immune complexes, fueling the inflammation and red-cell destruction behind severe anemia and organ damage—part of the immune over-response that turns malaria lethal."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Malaria cripples the bone marrow: the parasite and its hemozoin pigment suppress red-cell production (dyserythropoiesis), so blunted marrow output compounds the destruction of infected cells to deepen malarial anemia."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Severe malaria floods the blood with hydrogen ions: parasite and tissue starvation generate lactic acid, and the resulting metabolic acidosis (acidemia) is one of the strongest predictors of death in severe disease."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thrombocytopenia is the rule in malaria: platelets are consumed and trapped in the spleen as the infection activates clotting, so a low platelet count is one of the most reliable clues that a fever is malaria."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Malaria is still diagnosed by light: Giemsa-stained thick and thin blood films under the microscope reveal the parasites inside red cells, letting the species be identified and the parasite load counted."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Severe malaria suffocates tissues: sequestered red cells block capillaries while profound anemia cuts oxygen delivery, driving the lactic acidosis and organ failure that mark the deadliest disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The retina betrays cerebral malaria: malarial retinopathy—patchy whitening, vessel discoloration and hemorrhages—is a specific bedside sign that a comatose child's illness is truly malaria and not another cause."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals how malaria sticks and hides: the infected red cell sprouts surface knobs that anchor adhesion proteins to vessel walls, while inside, the parasite crystallizes toxic heme into inert hemozoin pigment within its digestive vacuole."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium signals the parasite's every move: rising calcium triggers the merozoites to burst from and reinvade red cells, making the ion a drug target — while severe malaria itself drives the blood calcium dangerously low."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Severe malaria can paralyze the gut: parasitized red cells sequester in the intestinal microvasculature, causing the abdominal pain, diarrhea, and bowel ischemia of 'algid malaria' that can mimic a surgical abdomen."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Cerebral malaria is the deadliest face of the disease: parasitized red cells jam the brain's microvessels, and the resulting ischemia and inflammation injure neurons into coma and seizures, leaving lasting cognitive deficits in surviving children."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Malaria can crash the blood sugar: the parasite's heavy glucose consumption plus quinine-driven insulin release from the pancreas cause a dangerous hypoglycemia, especially in pregnant women and severe disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Severe malaria dilutes the blood's sodium: an SIADH-like release of vasopressin and fluid shifts commonly drop sodium into hyponatremia, which can worsen the confusion and seizures of the acute illness."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both detect and defend against malaria: rapid tests catch the parasite's HRP-2 antigen with antibodies, partial immunity in endemic areas is antibody-mediated, and the RTS,S and R21 vaccines work by raising anti-circumsporozoite antibody."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy is a malaria magnet: parasites sequester in the placenta, causing maternal anemia, low birth weight, and fetal loss, which is why intermittent preventive treatment is given through pregnancy in endemic regions."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Malaria leaves the host open to bacteria: it impairs neutrophil function and the gut barrier, so severe disease — especially in children — carries a high risk of invasive nontyphoidal Salmonella and other bacterial co-infections."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Cerebral malaria is a brain-wide inflammation: parasitized red cells jam the brain's capillaries while activated microglia pour out cytokines, the combined sequestration and neuroinflammation driving the seizures and coma that can kill."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Malaria reshapes the body's iron traffic: inflammation drives hepcidin up, locking iron away in macrophages — starving the marrow into anemia while also denying the parasite the iron it needs, a double-edged host defense."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV and malaria worsen each other: HIV's weakened immunity makes malaria more frequent and severe, especially in pregnancy, while acute malaria transiently spikes HIV viral load — a vicious interaction across co-endemic regions."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "The liver stage is killed by T cells: cytotoxic CD8 T cells recognize Plasmodium-infected hepatocytes before the blood stage begins, the immunity that the RTS,S and R21 vaccines try to harness to stop infection at its silent start."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "A counter-cytokine decides severity: IL-10 restrains the TNF-driven inflammation of malaria, so the balance between them shapes whether infection stays mild or tips into cerebral malaria and severe disease."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate killers sound the first alarm: natural killer cells are among the earliest responders to blood-stage parasites, pouring out interferon-gamma that shapes the downstream immune response to the infection."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Parasite debris lights the inflammatory fuse: hemozoin pigment and GPI anchors released when red cells rupture activate NF-κB in immune cells, driving the TNF surge that underlies the fever cycles and the cytokine storm of severe malaria."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Cerebral malaria can stroke the brain: infected red cells sequester in and obstruct the brain's microvessels, causing the coma of cerebral malaria and leaving some survivors with focal deficits and stroke-like injury."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Severe disease tips the blood toward clotting: falciparum malaria activates endothelium and coagulation, a prothrombotic state that, alongside its consumptive coagulopathy, raises the risk of venous thrombosis."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Cerebral malaria scars the brain into seizures: the microvascular brain injury of cerebral malaria, especially in children, causes acute seizures and leaves many survivors with epilepsy and lasting neurocognitive impairment."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Profound anemia overworks the heart: the massive red-cell destruction of severe malaria can drop hemoglobin so low that the heart must pump in overdrive, precipitating high-output cardiac failure in vulnerable patients."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Its neurological aftermath darkens mood: survivors of cerebral and severe malaria carry higher rates of depression and cognitive sequelae, from the brain injury itself and the burden of recurrent, debilitating illness."
  - target: 02-pathogen/02-bacteria/salmonella-typhi
    relation: connects-to
    note: "It opens the door to invasive Salmonella: malaria classically predisposes to non-typhoidal and typhoidal Salmonella bloodstream infection, through hemolysis-impaired macrophage function and gut barrier breakdown."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Severe malaria blurs into sepsis: high parasite loads with cytokine storm, and frequent gram-negative bacterial co-infection, produce a septic-shock picture that drives much of malaria's mortality."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Surviving a life-threatening attack can scar the mind: the terror of cerebral malaria, intensive-care treatment and recurrent severe episodes can leave post-traumatic stress in survivors and families."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can seize the brain itself: cerebral malaria, from sequestration of infected red cells in cerebral capillaries, causes coma and seizures and leaves lasting neurological and cognitive deficits in survivors."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Severe malaria floods the lungs: it can cause acute respiratory distress syndrome and pulmonary oedema from capillary leak, a life-threatening complication even as parasites are cleared."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It enlarges the liver and yellows the skin: malaria causes hepatosplenomegaly and, from massive haemolysis and hepatic dysfunction, the jaundice and dark urine of blackwater fever."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe falciparum shuts down the kidney: acute kidney injury from haemoglobinuria and tubular necrosis — blackwater fever — is a defining feature of severe malaria and often needs dialysis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It drops blood sugar dangerously: severe malaria causes hypoglycaemia through impaired gluconeogenesis and parasite glucose use, and quinine treatment worsens it by triggering hyperinsulinaemia, especially in children and pregnancy."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It swells and can rupture the spleen: the spleen enlarges as it clears parasitised red cells, risking splenic rupture in acute infection and causing hyperreactive malarial splenomegaly with chronic exposure."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Severe disease collapses the circulation: 'algid malaria' brings hypotension and shock, with myocardial dysfunction from microvascular sequestration and the inflammatory response."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It aches deep in the muscles: prominent myalgia and back pain accompany the fever and rigors of a malarial paroxysm."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It pointedly spares the skin: malaria characteristically causes no rash — a clue distinguishing it from dengue and other tropical fevers — though pallor and jaundice from haemolysis appear."
  - target: 02-pathogen/06-environmental/zoonosis
    relation: connects-to
    note: "A species jumps from monkeys: Plasmodium knowlesi malaria is a zoonosis spread from macaques in Southeast Asia, an emerging cause of severe human malaria."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "It cooperates to cause lymphoma: chronic malaria is the key co-factor with Epstein-Barr virus in endemic Burkitt lymphoma, driving the B-cell proliferation the virus transforms."
  - target: 02-pathogen/06-environmental/diarrheal-disease
    relation: connects-to
    note: "Two great child killers overlap: in endemic regions malaria and diarrhoeal disease are leading causes of childhood death, frequently co-occurring and straining the same fragile health systems."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "It scars the kidney filter: Plasmodium malariae deposits immune complexes in the glomerulus causing quartan malarial nephropathy, while severe falciparum brings blackwater fever and acute tubular injury — major contributors to malarial death."
  - target: 02-pathogen/04-parasites/toxoplasma-gondii
    relation: connects-to
    note: "A fellow apicomplexan: Plasmodium and Toxoplasma are both apicomplexan parasites with an apicoplast organelle, the shared vulnerability that antifolates and other antiparasitics exploit against both."
  - target: 03-medicine/02-traditional/berberine
    relation: connects-to
    note: "A plant alkaloid with antiplasmodial activity: berberine, from Berberis and related plants used in traditional medicine, shows antimalarial activity in the laboratory, echoing how the wormwood-derived artemisinins became frontline therapy."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The silent liver stage comes first: injected Plasmodium sporozoites invade hepatocytes in the hepatic lobule to multiply before the blood stage, and vivax and ovale leave dormant hypnozoites there that cause relapses."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "It can flood the lungs: severe falciparum malaria causes acute lung injury and ARDS, with inflammatory alveolar-capillary leak filling the alveoli even as parasitaemia is being cleared."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Chronic infection over-activates B cells: repeated malaria drives intense polyclonal B-cell activation and germinal-centre expansion with hypergammaglobulinaemia, the immune over-stimulation that, with EBV, underlies endemic Burkitt lymphoma."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "A thrombotic microangiopathy mimic: severe falciparum malaria's microvascular obstruction, thrombocytopenia and haemolysis can resemble thrombotic thrombocytopenic purpura in a returning traveller, a key differential."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Cytoadherence to the vessel: P. falciparum-infected red cells bind endothelial receptors (ICAM-1, EPCR) on small-vessel walls, and this sequestration drives the obstruction behind cerebral and placental malaria."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Why anaemia outlasts the parasite: malaria blunts the erythropoietin response and causes dyserythropoiesis in the marrow, so the anaemia persists for weeks after the parasites are cleared."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Overlapping fevers and a syndemic: COVID-19 and malaria present with similar acute febrile illness, risking misdiagnosis, and the pandemic disrupted malaria control programmes across endemic regions."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Antimalarials and the QT interval: quinine, chloroquine and related drugs prolong cardiac repolarisation and can trigger arrhythmia, so the conduction system is watched closely during treatment of severe malaria."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "The heart in severe malaria: cytokines and microvascular sequestration can depress myocardial function in severe disease, a strain compounded by the cardiotoxicity of high-dose antimalarials."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Hemozoin-driven fevers: malaria pigment (hemozoin) and parasite products activate the NLRP3 inflammasome to release IL-1β, driving the cyclical fevers and inflammation of malaria."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Protective but double-edged: IFN-γ-driven Th1 immunity controls blood-stage malaria yet contributes to the immunopathology of cerebral malaria."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement in severe disease: complement activation, including C5a, contributes to the malarial anaemia and microvascular injury of severe malaria."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial dysfunction: a high angiopoietin-2 to angiopoietin-1 ratio destabilises the Tie2-regulated endothelium in severe and cerebral malaria, a key biomarker and mediator of vascular leak and poor outcome."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Microvascular thrombosis: parasite sequestration activates the endothelium to release ultra-large von Willebrand factor multimers, promoting platelet adhesion and microthrombi in cerebral malaria."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome fever: hemozoin and parasite products trigger IL-1β release downstream of inflammasome activation, driving the paroxysmal fevers and inflammatory injury of malaria."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "PAMP sensing: Plasmodium GPI anchors and hemozoin engage TLR4 (and TLR2/TLR9) on macrophages, triggering the NF-κB-driven cytokine surge that produces the paroxysmal fever and systemic inflammation of malaria."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cerebral malaria pathology: CD8 T cells deploy perforin against the parasite-sequestered brain endothelium, disrupting the blood-brain barrier in the immunopathology that underlies fatal cerebral malaria."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA sensing: Plasmodium DNA and hemozoin-bound DNA reaching the cytosol activate cGAS-STING, contributing the type-I-interferon response that modulates immunity and immunopathology during blood-stage malaria."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Cerebral malaria: endothelin-1 released by the activated, parasite-sequestered cerebral endothelium causes vasoconstriction and blood-brain-barrier dysfunction, contributing to the impaired perfusion and coma of cerebral malaria."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Hemozoin immunopathology: the malaria pigment hemozoin and the DAMP HMGB1 signal through RAGE to amplify the inflammatory cascade, contributing to the cytokine-driven immunopathology of severe and cerebral malaria."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: parasite digestion of haemoglobin and host xanthine-oxidase activity generate reactive oxygen species during blood-stage malaria, the oxidative pressure against which G6PD and sickle-cell traits confer their protective advantage."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Cerebral-malaria coagulopathy: P. falciparum PfEMP1 binds endothelial EPCR, displacing protein C and crippling its anticoagulant and barrier-protective signalling, a mechanism of the microvascular thrombosis and brain swelling of severe malaria."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Iron sequestration: malarial inflammation drives hepcidin (already mapped), which degrades ferroportin to lock iron inside macrophages, producing the hypoferraemia and anaemia of malaria while restricting iron from the parasite."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Cytokine storm: IL-6 is part of the pro-inflammatory cytokine surge (with the TNF-α and IL-1β already mapped) that drives the high fever and systemic pathology of severe Plasmodium infection."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate sensing: TLR recognition of parasite GPI anchors and hemozoin (TLR4 mapped) signals through MyD88 to NF-κB (mapped), driving the TNF/IL-1 cytokine surge that times the febrile paroxysms of malaria."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 induction: IL-12 from infected macrophages drives the protective Th1/IFN-γ response (IFN-γ mapped) against blood-stage malaria, while its dysregulation contributes to immunopathology."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Cerebral microthrombosis: endothelial activation and thrombin generation (with protein-C and von Willebrand factor mapped) drive the microvascular coagulation and sequestration of cerebral malaria."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IFN-γ-driven control of blood-stage malaria signals through JAK-STAT (IFN-γ mapped), the macrophage-activating axis central to parasite clearance."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Microvascular sequestration of infected erythrocytes produces local hypoxia that stabilises HIF-1α, contributing to the tissue injury of severe and cerebral malaria."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-mediated endothelial activation and blood-brain-barrier disruption contributes to the cerebral malaria syndrome, complementing the angiopoietin-Tie axis already mapped."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the macrophage inflammatory response to Plasmodium and contributes to the endothelial activation underlying severe malaria."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-γ-STAT1 signalling drives the macrophage antiparasitic program that controls Plasmodium but also contributes to the immunopathology of severe malaria."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling is exploited by Plasmodium during the hepatocyte liver-stage infection and shapes the endothelial responses of severe malaria."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6/IL-10-STAT3 signaling shapes the inflammatory-versus-regulatory balance and the anemia of inflammation in malaria."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by activated myeloid cells amplify the systemic inflammation and endothelial activation of severe malaria."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the oxidative-stress and cytokine balance that tips immunopathology versus parasite control in malaria."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the macrophage inflammatory response and cytokine balance that shape the pathology of severe malaria."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of pattern-recognition receptors amplifies the inflammatory cytokine output driving the pathology of malaria."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CCL2-driven monocyte recruitment contributes to the sequestration and inflammation of the cerebral and placental pathology of malaria."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the endothelial activation and immune-cell responses of severe malaria."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the host and parasite metabolic interplay of malaria."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven monocyte recruitment contributes to the inflammatory sequestration and cerebral pathology of severe malaria."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy participates in the hepatocyte and immune-cell responses to the liver and blood stages of malaria."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the host immune response to Plasmodium in malaria."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and splenic and marrow responses of malaria."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the immune response and immunopathology of malaria."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory immunopathology of malaria."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the macrophage activation and splenic immune response of malaria."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Hypoglycaemia: severe malaria and its quinine treatment cause dangerous hypoglycaemia through impaired hepatic gluconeogenesis and quinine-induced hyperinsulinaemia, a complication requiring close glucose monitoring, especially in children and pregnancy."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Vaccine immunity: MHC class II-restricted CD4 T-cell help underlies the antibody and cellular responses to the circumsporozoite antigen targeted by the RTS,S and R21 malaria vaccines, linking antigen presentation to protective immunity."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate sensing: blood-stage Plasmodium nucleic acids and hemozoin trigger a type I interferon response (cGAS-STING already mapped) that shapes early immunopathology and can both aid and impair control of the infection."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Metabolic acidosis: severe malaria produces a lactic and metabolic acidosis, an excess of protons from anaerobic glycolysis in sequestered tissues and impaired hepatic clearance, and this acidosis is one of the strongest predictors of death."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Malarial ARDS: severe falciparum malaria can cause acute respiratory distress and pulmonary oedema, a non-cardiogenic lung injury from increased capillary permeability that may appear even as parasitaemia falls with treatment."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Adaptive immunity: IL-2-driven T-cell expansion supports the cellular and antibody responses to Plasmodium (MHC class II already mapped), and this adaptive immunity underlies the partial, non-sterilising protection acquired after repeated infection."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Febrile paroxysms: pyrogenic prostaglandins, induced by the TNF and IL-1 (already mapped) released when infected red cells rupture, drive the characteristic cyclical fevers of malaria synchronised to the parasite's erythrocytic cycle."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Hypoglycaemia: severe malaria causes hypoglycaemia from parasite glucose consumption and impaired gluconeogenesis, compounded by quinine-induced hyperinsulinaemia (insulin already mapped) that disturbs the incretin GLP-1 axis of glucose control."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Antibody help: IL-4 and the Th2 response support the B-cell antibody production against Plasmodium (IL-12 and interferon-gamma already mapped for Th1), the humoral arm of the partial immunity acquired with repeated malaria."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Cytoadherence and sequestration: falciparum-infected red cells bind the endothelial cells via PfEMP1 (angiopoietin and von Willebrand factor already mapped), sequestering in the microvasculature to cause the cerebral and placental complications of severe malaria."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Malaria-protective haemoglobinopathy: the thalassaemia trait, like sickle trait, offers partial protection against severe malaria (haemoglobin already mapped), the balancing selection that maintains these haemoglobinopathies in malaria-endemic regions."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron tug-of-war: Plasmodium needs iron to grow, and the host restricts it through hepcidin and ferroportin (already mapped), a nutritional-immunity battle in which iron status also influences susceptibility to malaria."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 immune arm: IL-13, with IL-4 (already mapped), is part of the Th2 response whose balance against the Th1 (IL-12 and IFN-γ already mapped) shapes the immune control and immunopathology of malaria."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and nutritional immunity: zinc, with the iron (already mapped) of nutritional immunity, is important for the antimalarial immune response, and zinc deficiency in endemic malnourished children increases the malaria morbidity."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Malnutrition and immunity: the adipokine leptin links the undernutrition common in endemic regions to the impaired immune response, modulating the susceptibility to and severity of malaria in undernourished children."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Malnutrition adipokine: adiponectin, with leptin (already mapped), is the adipokine of the malnutrition-immunity axis of the undernourished endemic children that modulates the malaria susceptibility."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the malnutrition-immunity axis and the inflammatory (TNF and IL-6 already mapped) response of malaria."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present the Plasmodium antigens and prime the T-cell (already mapped) response, though the malaria also impairs their function as immune evasion."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Immunosuppressive Tregs: the Plasmodium induces the regulatory T cells (IL-10 already mapped) that dampen the protective immunity, enabling the parasite persistence in malaria."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia of the type-2 immune response in malaria."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Polyclonal IgE: the polyclonal B-cell activation of malaria raises the IgE (with IL-4 and IL-13 already mapped), part of the type-2 immune dimension of the infection."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory immune response to the malaria parasite."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper balance: the CD4 T-helper cells set the Th1 (IFN-γ already mapped) protective versus Th2 (IL-4 already mapped) balance that determines the outcome of the malaria infection."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Atypical memory B cells: the malaria drives the expansion of the atypical memory B cells and the polyclonal (IgE already mapped) activation, shaping the slowly-acquired antibody immunity to the parasite."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped), driven by the excess C5a, contributes to the inflammation and the endothelial injury of severe and cerebral malaria."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: Plasmodium recruits the host factor H (via the RIFIN and Pf surface proteins) to its infected erythrocytes (already mapped) to accelerate the C3-convertase decay and evade the complement attack."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron competition: transferrin, the iron carrier, is part of the host iron-handling that, with the disordered hepcidin (already mapped), governs the iron availability contested between the host and the intraerythrocytic parasite in malaria."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical/lectin complement (C3, C5, C5aR1 and factor H already mapped) and the contact-kinin systems activated in the microvascular thromboinflammation of severe malaria."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "vWF microthrombosis: the ADAMTS13 protease is consumed in severe malaria, so the ultra-large von Willebrand factor (already mapped) multimers persist and drive the platelet (already mapped) microthrombosis and endothelial sequestration of cerebral malaria."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Vascular mast cells: the mast cells, activated in malaria, contribute to the vascular permeability and the intestinal and systemic inflammation accompanying the infection."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-parasite axis: TSLP, released from barrier epithelial cells during the systemic inflammation of malaria, activates dendritic cells (already mapped) and shapes the Th2-biased immune response that facilitates the parasite (Plasmodium already mapped) persistence in malaria."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin fever amplifier: bradykinin, generated by the kallikrein-kinin pathway activated by Plasmodium (already mapped) metabolites and haemolysis products, amplifies the vascular permeability, fever, and the cytokine storm (already mapped) of severe malaria."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell histamine: histamine, released by the mast cells (already mapped) activated during malaria, amplifies the vascular permeability, the pain of the haemolytic fever episodes, and the intestinal inflammation of the disease."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Hepatosplenic fibrosis: periostin, induced by TGF-β (already mapped) in the spleen (already mapped) and liver (already mapped) during Plasmodium (already mapped) infection, promotes the fibrotic remodelling and hypersplenism sequelae of chronic malaria."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian fever synchrony: melatonin regulates the circadian pattern of the Plasmodium (already mapped) release from erythrocytes (already mapped), synchronising the periodic fever paroxysms (complement already mapped) of malaria to nocturnal peaks of melatonin."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine coupling: prolactin, elevated during the acute febrile response of malaria, potentiates macrophage (already mapped) and NK-cell (already mapped) activation, contributing to the Th1/IFN-γ (already mapped) immunity and the immunopathology of severe malaria."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "MAL testosterone: androgen signalling suppresses the IFN-γ (already mapped) Th1 response to Plasmodium (already mapped), increasing male susceptibility to severe malaria; testosterone modulates erythrocyte (already mapped) membrane deformability in the infected red cell."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "MAL serotonin: platelet (already mapped) serotonin released during haemolysis in malaria amplifies vascular permeability and the thromboinflammation of severe malaria; 5-HT2 signalling on endothelial cells (already mapped) promotes Plasmodium (already mapped) rosetting."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "MAL vasopressin: vasopressin released during severe malaria drives cerebral oedema via brain (already mapped) swelling and hyponatraemia via sodium (already mapped) dysregulation; V2-receptor signalling on the kidney (already mapped) modulates renal water retention."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "MAL oxytocin: oxytocin suppresses NF-κB (already mapped) and TNF-α (already mapped) driven endothelial-cell (already mapped) activation during severe malaria; oxytocin attenuates macrophage (already mapped) inflammatory cytokine release and platelet (already mapped) aggregation."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "MAL selenium: selenoproteins attenuate ROS-driven NF-κB (already mapped) and TNF-α (already mapped) mediated endothelial-cell (already mapped) damage during malaria; selenium deficiency worsens haemolytic anaemia via erythrocyte (already mapped) membrane oxidative stress."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MAL iodine: thyroid hormones modulate macrophage (already mapped) and nitric-oxide (already mapped) driven immune responses during malaria; iodine deficiency impairs NF-κB (already mapped) and IL-6 (already mapped) driven defence against Plasmodium falciparum (already mapped)."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "MAL magnesium: magnesium, as enzymatic cofactor in macrophages (already mapped) and erythrocytes (already mapped), supports immune and oxygen-transport function; magnesium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) haemolytic cascade of malaria."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "MAL copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) oxidative haemolytic cascade of malaria."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "MAL phosphorus: phosphorus, as ATP precursor in erythrocytes (already mapped) and macrophages (already mapped), supports cellular energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of malaria."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "MAL chloride: chloride regulates macrophage (already mapped) and erythrocyte (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) haemolytic cascade of malaria."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "MAL sulfur: sulfur, as glutathione precursor in erythrocytes (already mapped) and macrophages (already mapped), scavenges haemolytic ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of malaria."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "MAL nitrogen: nitrogen, as RNS via iNOS in macrophages (already mapped) and erythrocytes (already mapped), drives haemolytic stress; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of malaria."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Malaria carbon: carbon as backbone of haemoglobin (already mapped) and merozoite structural proteins sustains erythrocyte (already mapped) invasion; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of malaria."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Malaria PD-1: PD-1 checkpoint on T-cells (already mapped) drives immune exhaustion during chronic Plasmodium infection; PD-1 overexpression amplifies IL-10 (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) immune-suppression cascade of malaria."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Malaria angiotensin-II: angiotensin-II drives macrophage (already mapped) and endothelial (already mapped) inflammation in Plasmodium infection; angiotensin-II amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) haemolytic cascade of malaria."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Malaria WNT: WNT-β-catenin in macrophages (already mapped) and hepatocytes (already mapped) modulates Plasmodium liver-stage invasion; WNT dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) immune cascade of malaria."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Malaria RANKL: RANKL drives dendritic-cell (already mapped) and macrophage (already mapped) immune activation against Plasmodium; RANKL dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) immune cascade of malaria."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Malaria smad4: SMAD4 in hepatocytes (already mapped) and macrophages (already mapped) mediates TGF-β signalling; smad4 dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Malaria fibronectin: fibronectin in endothelial cells (already mapped) and macrophages (already mapped) mediates parasite sequestration; fibronectin dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) cascade of malaria."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Malaria notch: NOTCH in macrophages (already mapped) and dendritic cells (already mapped) regulates anti-malarial immunity; notch dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Malaria igf-1: IGF-1 from macrophages (already mapped) and dendritic cells (already mapped) modulates anti-malarial immunity; igf-1 dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Malaria activin-a: activin-A from macrophages (already mapped) and dendritic cells (already mapped) drives immune polarisation; activin-a excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Malaria tgf-beta: TGF-β from macrophages (already mapped) and dendritic cells (already mapped) regulates malarial immunosuppression; tgf-beta excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Malaria cgrp: CGRP from macrophages (already mapped) and dendritic cells (already mapped) modulates malarial neuroimmune tone; cgrp excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Malaria calcitonin: calcitonin from macrophages (already mapped) and dendritic cells (already mapped) modulates calcium tone; calcitonin excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Malaria substance-p: substance-P from macrophages (already mapped) and dendritic cells (already mapped) modulates immune tone; substance-p excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria."
---

# Malaria

## Overview

**Malaria** is a mosquito-borne infectious disease caused by intracellular parasites of the genus *Plasmodium*, transmitted exclusively by female *Anopheles* mosquitoes. It remains one of the most significant infectious diseases globally: in 2022, the WHO estimated **249 million cases** and **608,000 deaths** annually — predominantly children <5 years in sub-Saharan Africa [^who-malaria-report-2023].

**Five *Plasmodium* species cause human malaria:**

| Species | Clinical severity | Unique feature |
|:--------|:----------------|:---------------|
| ***P. falciparum*** | Highest; most deaths | Cytoadherence of infected RBCs → microvascular obstruction; cerebral malaria; artemisinin resistance emerging |
| ***P. vivax*** | Moderate; liver hypnozoites | Relapsing malaria (Duffy antigen receptor required for RBC invasion; absent in most West Africans → natural resistance) |
| ***P. ovale*** | Mild; hypnozoites | Two subspecies (curtisi/wallikeri); difficult to distinguish from P. vivax clinically |
| ***P. malariae*** | Mild; very long latency | Can persist decades; associated with nephrotic syndrome |
| ***P. knowlesi*** | Moderate-severe | Zoonosis from macaques in Southeast Asia; formerly mistaken for P. malariae |

## Structure

### Life cycle — key stages relevant to immunity and treatment

**Mosquito → Human transmission:**
1. *Anopheles* female takes blood meal → injects **sporozoites** from salivary glands into dermis → sporozoites reach bloodstream within 30-60 min
2. Sporozoites traverse Kupffer cells → infect **hepatocytes** via interactions with heparan sulfate proteoglycans and CD81/SR-BI receptors

**Liver stage (exoerythrocytic schizogony; 6-15 days, species-dependent):**
3. Sporozoite → **liver schizont** (asymptomatic); massive replication: 1 sporozoite → ~10,000–40,000 **merozoites** per hepatocyte
4. **P. vivax and P. ovale only:** Some sporozoites form dormant **hypnozoites** in hepatocytes → weeks to years later, hypnozoites reactivate → relapse; requires primaquine/tafenoquine for radical cure
5. Schizont ruptures → **merozoites** released into bloodstream as **merosomes** (protected from immune attack by host platelet/fibrin coating)

**Blood stage (erythrocytic schizogony; 48h for P. falciparum; 72h for P. malariae):**
6. Merozoite invades RBC via: **AMA1/RON complex**, **MSP1**, **EBA175/EBA140** binding to glycophorin A/B, band 3; RBC deforms → merozoite enters sealed parasitophorous vacuole membrane (PVM)
7. **Ring stage** (1-24h): Parasite metabolically active; HRP2 antigen shed
8. **Trophozoite stage** (24-36h): Haemoglobin digestion → **haemozoin (malaria pigment)** crystals; PfEMP1 (P. falciparum erythrocyte membrane protein 1) expressed on RBC surface → cytoadherence to ICAM-1 on brain endothelium (cerebral malaria), CD36 on placental syncytiotrophoblasts (placental malaria)
9. **Schizont stage** (36-48h): Division → 16-32 daughter merozoites
10. **Schizont rupture → fever spike**: Merozoite egress → haemozoin + GPI anchors + uric acid crystals released → TLR-9/NLRP3 activation → TNF-α, IL-6, IL-1β → fever + rigors + systemic inflammation
11. **Gametocytes**: Some parasites differentiate into gametocytes → ingested by mosquito → sexual reproduction in mosquito gut → oocyst → sporozoites → salivary glands → new cycle

### *P. falciparum* virulence mechanisms

**Cytoadherence:**
- PfEMP1 binds CD36 (rosetting), ICAM-1 (cerebral malaria), EPCR (severe malaria), chondroitin sulfate A (CSA; placental malaria)
- Brain endothelium: PfEMP1/ICAM-1 → infected RBCs trapped in cerebral microvessels → direct obstruction + endothelial activation + blood-brain barrier breakdown → cerebral malaria

**Rosetting:**
- Infected RBCs bind uninfected RBCs → rosettes → microvascular blockade + shielding of PfEMP1 from antibodies

**Knob formation:**
- Parasite remodels RBC cytoskeleton → knobs on RBC surface → projections for cytoadherence; KHARP and PfEMP3 cross-link spectrin network

**Immune evasion:**
- PfEMP1 has ~60 var gene variants per parasite genome; var gene switching → antigenic variation → parasites escape existing antibodies; children develop immunity only after years of repeated infections (var gene repertoire exhaustion)

## Function

### Pathophysiology of severe malaria

**Severe malaria criteria (WHO 2015):**
- **Cerebral malaria:** Unrousable coma + P. falciparum parasitaemia + no other cause; retinal haemorrhages on fundoscopy (80% sensitive); mortality 15-25% with treatment; neurological sequelae in ~25% of survivors
- **Severe anaemia:** Hb <5 g/dL in adults (<7 g/dL in children) + parasitaemia; from RBC haemolysis + dyserythropoiesis + splenic sequestration
- **Respiratory distress / ARDS:** Cytokine storm → pulmonary capillary leak → non-cardiogenic pulmonary oedema; mortality >40%
- **Acute kidney injury:** Haemoglobinuria (blackwater fever) + microvascular obstruction; IV artesunate reduces AKI risk vs. quinine (AQUAMAT)
- **Hypoglycaemia:** Parasite glucose consumption + insulin secretion from quinine/quinidine treatment + counter-regulatory failure
- **Hyperparasitaemia:** >10% parasitaemia associated with poor prognosis; exchange transfusion controversial
- **Coagulopathy/DIC:** Cytokine storm → TF expression → thrombin → fibrin; haemolysis → haem → endothelial injury

**Mechanisms of malarial anaemia:**
1. Direct haemolysis (schizont rupture; infected RBC lifespan ~48h vs. 120 days normal)
2. Destruction of uninfected RBCs (bystander haemolysis; antibody + complement-mediated; phagocytosis by activated macrophages)
3. Dyserythropoiesis (suppression of erythroid progenitors by TNF-α, IL-10, haemozoin; ineffective erythropoiesis)
4. Splenic clearance (clearance of ring-infected RBCs by enhanced splenic filtration; splenomegaly)
5. Rosetting reduces RBC deformability → mechanical haemolysis in capillaries

**Cerebral malaria mechanism:**
- PfEMP1-ICAM-1 cytoadherence in brain microvessels + rosetting → obstructed flow → reduced O₂ delivery → lactic acidosis
- Endothelial activation → NO depletion (haemoglobin scavenges NO from haemolysis), TNF-α, VEGF → blood-brain barrier disruption → cerebral oedema
- Brain herniation → brainstem compression → death

## Pathology

### Diagnosis

**Microscopy (gold standard):**
- Thick blood smear: Sensitive (~10 parasites/μL); quantifies parasitaemia
- Thin blood smear: Species identification; ring vs. trophozoite vs. schizont; gametocytes
- Giemsa stain: Required for definitive diagnosis
- Limitation: Requires skilled microscopist; time-consuming

**Rapid diagnostic tests (RDTs):**
- Immunochromatographic strips detecting **HRP2** (*P. falciparum*-specific; high sensitivity), **pLDH** (all species), or **aldolase** (pan-*Plasmodium*)
- WHO mandates RDT or microscopy confirmation before treatment
- HRP2 RDT can remain positive for 2-3 weeks after successful treatment (persistent antigen)
- *Pfhrp2/3* gene deletions in some *P. falciparum* strains → false-negative HRP2 RDT (emerging problem in South America, Africa)

**PCR/qPCR:**
- Most sensitive (1-5 parasites/μL); gold standard for low parasitaemia, species confirmation, mixed infections, resistance genotyping
- Not routinely available in endemic settings

### Treatment

**WHO 2023 treatment guidelines [^white-2014-malaria-lancet]:**

**Uncomplicated P. falciparum malaria — first-line: Artemisinin-based combination therapy (ACT):**

| ACT | Components | Dosing | Notes |
|:----|:-----------|:-------|:------|
| **Artemether-lumefantrine (Coartem)** | Artemether 20 mg + lumefantrine 120 mg | 4-dose over 3 days (weight-based) | Most widely used globally; with fatty food |
| **Artesunate-amodiaquine** | Artesunate 100 mg + amodiaquine 270 mg | 3-day course | Sub-Saharan Africa; G6PD concerns with amodiaquine |
| **Artesunate-mefloquine** | Artesunate 200 mg + mefloquine 440 mg | 3-day course | Southeast Asia (especially Thailand-Myanmar border) |
| **Dihydroartemisinin-piperaquine (DHA-PPQ; Eurartesim)** | DHA 40 mg + piperaquine 320 mg | 3-day course | Fasting required; QTc prolongation monitoring |
| **Artesunate-pyronaridine** | Artesunate 200 mg + pyronaridine 540 mg | 3-day course | Newer; effective against artemisinin-partial resistance |

**Mechanism of artemisinins:**
- Artemisinins are sesquiterpene lactones with an endoperoxide bridge → activated by haem iron released during haemoglobin digestion → carbon-centered free radicals → alkylate parasite proteins (PfKRS, PfATP4) and membranes → parasite death
- **Partial artemisinin resistance (kelch13 mutations):** K13 propeller domain mutations (C580Y most common; Southeast Asia) → delayed parasite ring-stage clearance; clinical artemisinin resistance defined as >10% ring-stage survival in RSA assay or persistent parasitaemia at 72h
- ACT remains effective if partner drug is active → but partner drug (piperaquine, lumefantrine) resistance accumulating in Southeast Asia → TRIPLE artemisinin-based combination therapies (TACTs) under development

**Severe P. falciparum malaria — IV artesunate (first-line):**
- Artesunate 2.4 mg/kg IV at 0, 12, 24h then daily; superior to quinine in SEAQUAMAT (adult Asia) and AQUAMAT (children Africa) trials → ~22-35% mortality reduction
- Switch to oral ACT as soon as tolerated; complete 3-day ACT course
- Supportive care: IV glucose (hypoglycaemia), transfusion if Hb <7 g/dL, exchange transfusion (debated; parasitaemia >10%), broad-spectrum antibiotics (frequent bacterial co-infection)

**P. vivax / P. ovale — radical cure:**
- Blood stage: Chloroquine (where sensitive) 3 days; ACT if chloroquine-resistant P. vivax (e.g., Indonesia, Papua New Guinea)
- Radical cure (hypnozoites): **Primaquine 15 mg/day × 14 days** (WHO standard) or **primaquine 30 mg/day × 7 days** (short-course, if G6PD normal); **tafenoquine 300 mg × 1 dose** (single-dose radical cure, FDA/TGA approved 2018)
- **Mandatory G6PD testing before primaquine or tafenoquine**: G6PD-deficient patients → primaquine → haemolysis; tafenoquine contraindicated if G6PD <70% of normal; supervised weekly primaquine (0.75 mg/kg once weekly × 8 weeks) is alternative for G6PD-deficient individuals (Class III)

**Prevention and chemoprophylaxis:**
- **Personal protection:** Insecticide-treated bed nets (ITNs); indoor residual spraying (IRS); DEET/picaridin repellents
- **Chemoprophylaxis:**
  - Atovaquone-proguanil (Malarone): Daily, start 1-2 days before, continue 7 days after travel; well-tolerated; broad-spectrum
  - Doxycycline: Daily; carotid for Southeast Asia (mefloquine resistance); photosensitivity; contraindicated in pregnancy/children
  - Mefloquine: Weekly; prophylactic for chloroquine-resistant areas; neuropsychiatric side effects
  - Chloroquine: Weekly; only for chloroquine-sensitive areas (Central America, some Caribbean)
- **Seasonal malaria chemoprevention (SMC):** Intermittent preventive treatment with SP-AQ in children <5 in Sahel region; reduces malaria incidence by 75%
- **Preventive treatment in pregnancy (IPTp):** SP (sulfadoxine-pyrimethamine) 3+ doses in pregnancy in sub-Saharan Africa; reduces placental malaria and LBW
- **Vaccine (RTS,S/AS01; Mosquirix and R21/Matrix-M):**
  - **RTS,S/AS01E (Mosquirix):** WHO-recommended 2021; 4-dose schedule; 36-40% efficacy against clinical malaria over 4 years; widely deployed in Ghana, Kenya, Malawi (pilot program)
  - **R21/Matrix-M (Serum Institute/Oxford):** WHO-prequalified 2023; 75-77% efficacy in seasonal areas; superior to RTS,S; scale-up underway

### Immunity and genetic resistance

**Naturally acquired immunity:**
- After repeated exposure, adults in high-transmission areas develop clinical immunity (non-sterile; parasites persist but at lower density → asymptomatic)
- Immunity mediated by: IgG antibodies against PfEMP1 variants (var gene collection), merozoite surface antigens (MSP1, MSP2, AMA1); CD4+ T cells; regulatory T cells can suppress inflammation (beneficial in severe malaria)
- Maternal antibody transfer → neonates protected for 3-6 months → "honeymoon period" before first malaria episode

**Genetic protective factors:**
| Variant | Mechanism of protection | Population |
|:--------|:------------------------|:-----------|
| HbAS (sickle cell trait) | Impaired parasite invasion/growth; HbS polymerization in low O₂ → parasite can't grow → enhanced clearance | Sub-Saharan Africa |
| HbSS | Partial protection in endemic areas; severe malaria risk reduced | |
| HbC (heterozygous) | Reduced RBC surface PfEMP1 expression → less cytoadherence | West Africa |
| α-thalassaemia | Reduces severe malaria mortality; increases mild malaria frequency (epidemiological paradox) | Worldwide |
| G6PD heterozygosity (females) | Mosaic RBC population → infected G6PD-deficient RBCs cleared faster | Africa, Asia |
| Duffy antigen negativity | *P. vivax* requires Duffy antigen (DARC) for invasion → 95% of West Africans Duffy-negative → complete P. vivax resistance | West Africa |
| HLA-B53 | Enhanced CD8+ T cell responses to liver stage | West Africa |

## Connections

- `connects-to` → **[G6PD](../../03-molecular/g6pd/README.md)** — G6PD heterozygosity confers ~50% protection against severe malaria; G6PD-deficient patients risk acute haemolysis with primaquine (P. vivax radical cure) or tafenoquine; WHO mandates G6PD testing before 8-aminoquinoline prescription; G6PD deficiency is the dominant pharmacogenomic interaction in malaria treatment.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — HbAS (sickle trait) confers ~60% protection against severe P. falciparum malaria; HbSS provides partial protection (parasite invasion of sickled RBCs impaired); thalassaemia and HbC also protective; overlapping Hb variant and G6PD polymorphism distributions reflect centuries of malaria selection.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — HbAS (sickle cell trait) confers ~60% protection against severe and fatal malaria; the HbS allele frequency in sub-Saharan Africa (6-15%) is maintained by malaria selection (balanced polymorphism); HbSS patients exposed to malaria face increased sickling crises from fever + dehydration.
- `connects-to` → **[CKD](../ckd/README.md)** — Severe falciparum malaria causes acute kidney injury (AKI) in 4-8% of cases (haemoglobinuria, parasite microvascular obstruction, cytokine storm); cerebral malaria + AKI → poor prognosis; malaria-endemic populations have higher CKD prevalence partly from repeated acute kidney insults.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Iron deficiency partially protective against P. falciparum (iron-restricted parasites grow less vigorously); iron supplementation in endemic areas should follow malaria treatment to avoid feeding parasites; IDA and malaria co-exist in sub-Saharan Africa.
- `connects-to` → **[Plasmodium falciparum](../../../02-pathogen/04-parasites/plasmodium-falciparum/README.md)** — Plasmodium falciparum, spread by Anopheles mosquitoes, is the deadliest malaria parasite: it cytoadheres infected red cells to brain endothelium via PfEMP1, evades immunity by var-gene switching, and is treated with artemisinin combinations now threatened by kelch13 resistance.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Malaria's blood stage runs in red cells: merozoites invade via AMA1/EBA-glycophorin, digest hemoglobin into haemozoin, and rupture every 48h triggering fever; haemolysis plus dyserythropoiesis causes severe anemia, while inherited RBC variants (HbS, G6PD) blunt parasite growth.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Cerebral malaria is the most lethal complication of P. falciparum: PfEMP1-coated red cells sequester on ICAM-1 in brain microvessels, obstructing flow and breaking the blood-brain barrier → coma; mortality is 15-25%, and ~25% of survivors retain neurological sequelae.
- `connects-to` → **[Leishmaniasis](../leishmaniasis/README.md)** — Both are vector-borne protozoan parasites of the global poor: Anopheles-borne Plasmodium invades erythrocytes, sand-fly-borne Leishmania hides in macrophages; both cause fever, splenomegaly and anemia in overlapping tropical regions, and HIV co-infection worsens both.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Malaria's obligatory pre-erythrocytic stage is hepatic: sporozoites invade hepatocytes and mature into thousands of merozoites before blood-stage disease; P. vivax/ovale form dormant hypnozoites needing primaquine/tafenoquine for radical cure; severe malaria also causes jaundice.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α drives malaria's inflammatory pathology: schizont rupture and GPI anchors trigger macrophage TNF-α → fever, hypoglycemia and ICAM-1 upregulation, promoting PfEMP1-mediated sequestration in cerebral malaria; high circulating TNF-α correlates with severity and mortality.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Thalassemia, like sickle cell trait, is maintained by malaria selection: abnormal or reduced hemoglobin makes red cells a poorer host for Plasmodium, conferring partial protection from severe malaria—why it is common across the historic malaria belt.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is central to malaria: it filters and destroys parasitized red cells, driving the splenomegaly typical of chronic infection, and the parasite evades it by sequestering in deep vasculature—so splenectomy or asplenia markedly worsens malaria severity.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Endemic Burkitt lymphoma is a malaria-driven cancer: chronic Plasmodium falciparum infection causes intense B-cell proliferation and weakens control of co-infecting Epstein-Barr virus, together driving the MYC translocation behind the jaw tumors of African children.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Malaria causes severe anemia by several routes: rupture of infected red cells, splenic clearance of uninfected cells, and inflammatory suppression of erythropoiesis (an anemia-of-chronic-disease component) combine, making anemia a leading cause of malaria death in children.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — Severe falciparum malaria can cause ARDS: sequestration of infected red cells and intense inflammation injure the pulmonary capillaries, flooding alveoli with edema even after parasite clearance—acute respiratory distress is a feared complication of severe malaria.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Severe malaria can trigger disseminated intravascular coagulation: widespread endothelial activation and cytokine storm in falciparum infection consume clotting factors and platelets, causing bleeding—part of the multi-organ failure that makes severe malaria lethal.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Severe malaria injures the kidney: hemolysis and sequestration cause acute kidney injury and, classically, blackwater fever (massive hemoglobinuria), so renal failure marks severe falciparum malaria and worsens its high mortality.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — Severe malaria is partly a cytokine storm: schizont rupture triggers a TNF-driven inflammatory surge causing fever, and excess cytokines contribute to cerebral malaria and organ failure—so the host inflammatory response, not just the parasite, drives lethal disease.
- `connects-to` → **[Dengue Fever](../dengue-fever/README.md)** — Malaria and dengue are the great overlapping tropical fevers: both cause fever and thrombocytopenia in the same regions, so a febrile traveler needs both excluded—malaria (a treatable parasite) must never be missed while dengue (a virus) is managed supportively.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Malaria targets the placenta in pregnancy: infected red cells bind a unique placental receptor (CSA) and sequester there, causing maternal anemia, low birth weight, and stillbirth—so first pregnancies in endemic areas carry special risk, prompting preventive treatment.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Cerebral malaria is a disease of the endothelium: infected red cells express adhesion proteins that stick to blood-vessel linings, sequestering in the brain's microvessels, blocking flow and inflaming the barrier—causing the coma that makes falciparum malaria lethal.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Malaria immunity is hard-won and incomplete: repeated infection builds partial 'premunition' that lets endemic adults tolerate parasites, but it wanes without exposure—and this slow, leaky immunity is exactly why an effective malaria vaccine (RTS,S, R21) took so long.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Malaria's silent first stage is in hepatocytes: injected sporozoites invade liver cells and multiply before the blood stage, and in P. vivax and ovale dormant hypnozoites hide there for months—causing relapses that need a separate drug (primaquine) to clear.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide is double-edged in malaria: it helps kill parasites, but in cerebral malaria dysregulated NO and endothelial activation contribute to the coma and brain injury that make it the deadliest complication.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron and malaria are dangerously intertwined: the parasite needs iron to grow, so iron supplementation can worsen malaria in endemic areas—while repeated infection also causes anemia, complicating how iron deficiency is treated where malaria is common.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Severe malaria spills potassium from burst red cells: massive hemolysis and kidney injury raise blood potassium, and the released hemoglobin can darken the urine (blackwater fever)—dangerous electrolyte shifts in the sickest patients.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — The spleen's macrophages fight and are fooled by malaria: they engulf parasitized red cells and the dark hemozoin pigment, enlarging the spleen, yet the parasite's surface tricks sustain infection—and a ruptured malarial spleen is a feared emergency.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Severe malaria activates complement: C3 and the cascade fire on parasite and immune complexes, fueling the inflammation and red-cell destruction behind severe anemia and organ damage—part of the immune over-response that turns malaria lethal.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Malaria cripples the bone marrow: the parasite and its hemozoin pigment suppress red-cell production (dyserythropoiesis), so blunted marrow output compounds the destruction of infected cells to deepen malarial anemia.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Severe malaria floods the blood with hydrogen ions: parasite and tissue starvation generate lactic acid, and the resulting metabolic acidosis (acidemia) is one of the strongest predictors of death in severe disease.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thrombocytopenia is the rule in malaria: platelets are consumed and trapped in the spleen as the infection activates clotting, so a low platelet count is one of the most reliable clues that a fever is malaria.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Malaria is still diagnosed by light: Giemsa-stained thick and thin blood films under the microscope reveal the parasites inside red cells, letting the species be identified and the parasite load counted.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Severe malaria suffocates tissues: sequestered red cells block capillaries while profound anemia cuts oxygen delivery, driving the lactic acidosis and organ failure that mark the deadliest disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The retina betrays cerebral malaria: malarial retinopathy—patchy whitening, vessel discoloration and hemorrhages—is a specific bedside sign that a comatose child's illness is truly malaria and not another cause.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals how malaria sticks and hides: the infected red cell sprouts surface knobs that anchor adhesion proteins to vessel walls, while inside, the parasite crystallizes toxic heme into inert hemozoin pigment within its digestive vacuole.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium signals the parasite's every move: rising calcium triggers the merozoites to burst from and reinvade red cells, making the ion a drug target — while severe malaria itself drives the blood calcium dangerously low.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Severe malaria can paralyze the gut: parasitized red cells sequester in the intestinal microvasculature, causing the abdominal pain, diarrhea, and bowel ischemia of 'algid malaria' that can mimic a surgical abdomen.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Cerebral malaria is the deadliest face of the disease: parasitized red cells jam the brain's microvessels, and the resulting ischemia and inflammation injure neurons into coma and seizures, leaving lasting cognitive deficits in surviving children.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Malaria can crash the blood sugar: the parasite's heavy glucose consumption plus quinine-driven insulin release from the pancreas cause a dangerous hypoglycemia, especially in pregnant women and severe disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Severe malaria dilutes the blood's sodium: an SIADH-like release of vasopressin and fluid shifts commonly drop sodium into hyponatremia, which can worsen the confusion and seizures of the acute illness.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both detect and defend against malaria: rapid tests catch the parasite's HRP-2 antigen with antibodies, partial immunity in endemic areas is antibody-mediated, and the RTS,S and R21 vaccines work by raising anti-circumsporozoite antibody.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy is a malaria magnet: parasites sequester in the placenta, causing maternal anemia, low birth weight, and fetal loss, which is why intermittent preventive treatment is given through pregnancy in endemic regions.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Malaria leaves the host open to bacteria: it impairs neutrophil function and the gut barrier, so severe disease — especially in children — carries a high risk of invasive nontyphoidal Salmonella and other bacterial co-infections.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Cerebral malaria is a brain-wide inflammation: parasitized red cells jam the brain's capillaries while activated microglia pour out cytokines, the combined sequestration and neuroinflammation driving the seizures and coma that can kill.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Malaria reshapes the body's iron traffic: inflammation drives hepcidin up, locking iron away in macrophages — starving the marrow into anemia while also denying the parasite the iron it needs, a double-edged host defense.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV and malaria worsen each other: HIV's weakened immunity makes malaria more frequent and severe, especially in pregnancy, while acute malaria transiently spikes HIV viral load — a vicious interaction across co-endemic regions.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — The liver stage is killed by T cells: cytotoxic CD8 T cells recognize Plasmodium-infected hepatocytes before the blood stage begins, the immunity that the RTS,S and R21 vaccines try to harness to stop infection at its silent start.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — A counter-cytokine decides severity: IL-10 restrains the TNF-driven inflammation of malaria, so the balance between them shapes whether infection stays mild or tips into cerebral malaria and severe disease.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Innate killers sound the first alarm: natural killer cells are among the earliest responders to blood-stage parasites, pouring out interferon-gamma that shapes the downstream immune response to the infection.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Parasite debris lights the inflammatory fuse: hemozoin pigment and GPI anchors released when red cells rupture activate NF-κB in immune cells, driving the TNF surge that underlies the fever cycles and the cytokine storm of severe malaria.
- `connects-to` → **[Stroke](../stroke/README.md)** — Cerebral malaria can stroke the brain: infected red cells sequester in and obstruct the brain's microvessels, causing the coma of cerebral malaria and leaving some survivors with focal deficits and stroke-like injury.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Severe disease tips the blood toward clotting: falciparum malaria activates endothelium and coagulation, a prothrombotic state that, alongside its consumptive coagulopathy, raises the risk of venous thrombosis.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Cerebral malaria scars the brain into seizures: the microvascular brain injury of cerebral malaria, especially in children, causes acute seizures and leaves many survivors with epilepsy and lasting neurocognitive impairment.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Profound anemia overworks the heart: the massive red-cell destruction of severe malaria can drop hemoglobin so low that the heart must pump in overdrive, precipitating high-output cardiac failure in vulnerable patients.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Its neurological aftermath darkens mood: survivors of cerebral and severe malaria carry higher rates of depression and cognitive sequelae, from the brain injury itself and the burden of recurrent, debilitating illness.
- `connects-to` → **[Salmonella Typhi](../../../02-pathogen/02-bacteria/salmonella-typhi/README.md)** — It opens the door to invasive Salmonella: malaria classically predisposes to non-typhoidal and typhoidal Salmonella bloodstream infection, through hemolysis-impaired macrophage function and gut barrier breakdown.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Severe malaria blurs into sepsis: high parasite loads with cytokine storm, and frequent gram-negative bacterial co-infection, produce a septic-shock picture that drives much of malaria's mortality.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Surviving a life-threatening attack can scar the mind: the terror of cerebral malaria, intensive-care treatment and recurrent severe episodes can leave post-traumatic stress in survivors and families.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can seize the brain itself: cerebral malaria, from sequestration of infected red cells in cerebral capillaries, causes coma and seizures and leaves lasting neurological and cognitive deficits in survivors.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Severe malaria floods the lungs: it can cause acute respiratory distress syndrome and pulmonary oedema from capillary leak, a life-threatening complication even as parasites are cleared.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It enlarges the liver and yellows the skin: malaria causes hepatosplenomegaly and, from massive haemolysis and hepatic dysfunction, the jaundice and dark urine of blackwater fever.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe falciparum shuts down the kidney: acute kidney injury from haemoglobinuria and tubular necrosis — blackwater fever — is a defining feature of severe malaria and often needs dialysis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It drops blood sugar dangerously: severe malaria causes hypoglycaemia through impaired gluconeogenesis and parasite glucose use, and quinine treatment worsens it by triggering hyperinsulinaemia, especially in children and pregnancy.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It swells and can rupture the spleen: the spleen enlarges as it clears parasitised red cells, risking splenic rupture in acute infection and causing hyperreactive malarial splenomegaly with chronic exposure.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Severe disease collapses the circulation: 'algid malaria' brings hypotension and shock, with myocardial dysfunction from microvascular sequestration and the inflammatory response.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It aches deep in the muscles: prominent myalgia and back pain accompany the fever and rigors of a malarial paroxysm.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It pointedly spares the skin: malaria characteristically causes no rash — a clue distinguishing it from dengue and other tropical fevers — though pallor and jaundice from haemolysis appear.
- `connects-to` → **[Zoonosis](../../../02-pathogen/06-environmental/zoonosis/README.md)** — A species jumps from monkeys: Plasmodium knowlesi malaria is a zoonosis spread from macaques in Southeast Asia, an emerging cause of severe human malaria.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — It cooperates to cause lymphoma: chronic malaria is the key co-factor with Epstein-Barr virus in endemic Burkitt lymphoma, driving the B-cell proliferation the virus transforms.
- `connects-to` → **[Diarrheal Disease](../../../02-pathogen/06-environmental/diarrheal-disease/README.md)** — Two great child killers overlap: in endemic regions malaria and diarrhoeal disease are leading causes of childhood death, frequently co-occurring and straining the same fragile health systems.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — It scars the kidney filter: Plasmodium malariae deposits immune complexes in the glomerulus causing quartan malarial nephropathy, while severe falciparum brings blackwater fever and acute tubular injury — major contributors to malarial death.
- `connects-to` → **[Toxoplasma gondii](../../../02-pathogen/04-parasites/toxoplasma-gondii/README.md)** — A fellow apicomplexan: Plasmodium and Toxoplasma are both apicomplexan parasites with an apicoplast organelle, the shared vulnerability that antifolates and other antiparasitics exploit against both.
- `connects-to` → **[Berberine](../../../03-medicine/02-traditional/berberine/README.md)** — A plant alkaloid with antiplasmodial activity: berberine, from Berberis and related plants used in traditional medicine, shows antimalarial activity in the laboratory, echoing how the wormwood-derived artemisinins became frontline therapy.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The silent liver stage comes first: injected Plasmodium sporozoites invade hepatocytes in the hepatic lobule to multiply before the blood stage, and vivax and ovale leave dormant hypnozoites there that cause relapses.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — It can flood the lungs: severe falciparum malaria causes acute lung injury and ARDS, with inflammatory alveolar-capillary leak filling the alveoli even as parasitaemia is being cleared.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Chronic infection over-activates B cells: repeated malaria drives intense polyclonal B-cell activation and germinal-centre expansion with hypergammaglobulinaemia, the immune over-stimulation that, with EBV, underlies endemic Burkitt lymphoma.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — A thrombotic microangiopathy mimic: severe falciparum malaria's microvascular obstruction, thrombocytopenia and haemolysis can resemble thrombotic thrombocytopenic purpura in a returning traveller, a key differential.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Cytoadherence to the vessel: P. falciparum-infected red cells bind endothelial receptors (ICAM-1, EPCR) on small-vessel walls, and this sequestration drives the obstruction behind cerebral and placental malaria.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Why anaemia outlasts the parasite: malaria blunts the erythropoietin response and causes dyserythropoiesis in the marrow, so the anaemia persists for weeks after the parasites are cleared.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Overlapping fevers and a syndemic: COVID-19 and malaria present with similar acute febrile illness, risking misdiagnosis, and the pandemic disrupted malaria control programmes across endemic regions.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Antimalarials and the QT interval: quinine, chloroquine and related drugs prolong cardiac repolarisation and can trigger arrhythmia, so the conduction system is watched closely during treatment of severe malaria.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — The heart in severe malaria: cytokines and microvascular sequestration can depress myocardial function in severe disease, a strain compounded by the cardiotoxicity of high-dose antimalarials.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Hemozoin-driven fevers: malaria pigment (hemozoin) and parasite products activate the NLRP3 inflammasome to release IL-1β, driving the cyclical fevers and inflammation of malaria.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Protective but double-edged: IFN-γ-driven Th1 immunity controls blood-stage malaria yet contributes to the immunopathology of cerebral malaria.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement in severe disease: complement activation, including C5a, contributes to the malarial anaemia and microvascular injury of severe malaria.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial dysfunction: a high angiopoietin-2 to angiopoietin-1 ratio destabilises the Tie2-regulated endothelium in severe and cerebral malaria, a key biomarker and mediator of vascular leak and poor outcome.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Microvascular thrombosis: parasite sequestration activates the endothelium to release ultra-large von Willebrand factor multimers, promoting platelet adhesion and microthrombi in cerebral malaria.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome fever: hemozoin and parasite products trigger IL-1β release downstream of inflammasome activation, driving the paroxysmal fevers and inflammatory injury of malaria.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Plasmodium GPI anchors and hemozoin engage TLR4 (with TLR2 and TLR9) on macrophages, triggering the NF-κB-driven cytokine surge that produces the paroxysmal fever and systemic inflammation of malaria.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD8 T cells deploy perforin against the parasite-sequestered brain endothelium, disrupting the blood-brain barrier in the immunopathology that underlies fatal cerebral malaria—where the host response, not the parasite alone, kills.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Plasmodium DNA and hemozoin-bound DNA reaching the cytosol activate cGAS-STING, contributing the type-I-interferon response that modulates both protective immunity and the immunopathology of blood-stage malaria.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 released by the activated, parasite-sequestered cerebral endothelium causes vasoconstriction and blood-brain-barrier dysfunction, contributing to the impaired perfusion and coma of cerebral malaria.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — The malaria pigment hemozoin and the DAMP HMGB1 signal through RAGE to amplify the inflammatory cascade, contributing to the cytokine-driven immunopathology of severe and cerebral malaria.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Parasite digestion of hemoglobin and host xanthine-oxidase activity generate reactive oxygen species during blood-stage malaria, the oxidative pressure against which G6PD and sickle-cell traits confer their protective advantage.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — P. falciparum PfEMP1 binds endothelial EPCR, displacing protein C and crippling its anticoagulant and barrier-protective signaling, a mechanism of the microvascular thrombosis and brain swelling of severe malaria.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Malarial inflammation drives hepcidin (already mapped), which degrades ferroportin to lock iron inside macrophages, producing the hypoferremia and anemia of malaria while restricting iron from the parasite.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 is part of the pro-inflammatory cytokine surge (with the TNF-α and IL-1β already mapped) that drives the high fever and systemic pathology of severe Plasmodium infection.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR recognition of parasite GPI anchors and hemozoin (TLR4 mapped) signals through MyD88 to NF-κB (mapped), driving the TNF/IL-1 cytokine surge that times the febrile paroxysms of malaria.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 from infected macrophages drives the protective Th1/IFN-γ response (IFN-γ mapped) against blood-stage malaria, while its dysregulation contributes to immunopathology.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Endothelial activation and thrombin generation (with protein-C and von Willebrand factor mapped) drive the microvascular coagulation and sequestration of cerebral malaria.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IFN-γ-driven control of blood-stage malaria signals through JAK-STAT (IFN-γ mapped), the macrophage-activating axis central to parasite clearance.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Microvascular sequestration of infected erythrocytes produces local hypoxia that stabilizes HIF-1α, contributing to the tissue injury of severe and cerebral malaria.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-mediated endothelial activation and blood-brain-barrier disruption contributes to the cerebral malaria syndrome, complementing the angiopoietin-Tie axis already mapped.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the macrophage inflammatory response to Plasmodium and contributes to the endothelial activation underlying severe malaria.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-γ-STAT1 signaling drives the macrophage antiparasitic program that controls Plasmodium but also contributes to the immunopathology of severe malaria.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling is exploited by Plasmodium during the hepatocyte liver-stage infection and shapes the endothelial responses of severe malaria.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6/IL-10-STAT3 signaling shapes the inflammatory-versus-regulatory balance and the anemia of inflammation in malaria.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by activated myeloid cells amplify the systemic inflammation and endothelial activation of severe malaria.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the oxidative-stress and cytokine balance that tips immunopathology versus parasite control in malaria.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the macrophage inflammatory response and cytokine balance that shape the pathology of severe malaria.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of pattern-recognition receptors amplifies the inflammatory cytokine output driving the pathology of malaria.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2-driven monocyte recruitment contributes to the sequestration and inflammation of the cerebral and placental pathology of malaria.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the endothelial activation and immune-cell responses of severe malaria.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the host and parasite metabolic interplay of malaria.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven monocyte recruitment contributes to the inflammatory sequestration and cerebral pathology of severe malaria.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy participates in the hepatocyte and immune-cell responses to the liver and blood stages of malaria.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the host immune response to Plasmodium in malaria.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and splenic and marrow responses of malaria.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the immune response and immunopathology of malaria.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory immunopathology of malaria.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the macrophage activation and splenic immune response of malaria.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Hypoglycaemia: severe malaria and its quinine treatment cause dangerous hypoglycaemia through impaired hepatic gluconeogenesis and quinine-induced hyperinsulinaemia, a complication requiring close glucose monitoring, especially in children and pregnancy.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Vaccine immunity: MHC class II-restricted CD4 T-cell help underlies the antibody and cellular responses to the circumsporozoite antigen targeted by the RTS,S and R21 malaria vaccines, linking antigen presentation to protective immunity.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Innate sensing: blood-stage Plasmodium nucleic acids and hemozoin trigger a type I interferon response (cGAS-STING already mapped) that shapes early immunopathology and can both aid and impair control of the infection.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Metabolic acidosis: severe malaria produces a lactic and metabolic acidosis, an excess of protons from anaerobic glycolysis in sequestered tissues and impaired hepatic clearance, and this acidosis is one of the strongest predictors of death.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Malarial ARDS: severe falciparum malaria can cause acute respiratory distress and pulmonary oedema, a non-cardiogenic lung injury from increased capillary permeability that may appear even as parasitaemia falls with treatment.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Adaptive immunity: IL-2-driven T-cell expansion supports the cellular and antibody responses to Plasmodium (MHC class II already mapped), and this adaptive immunity underlies the partial, non-sterilising protection acquired after repeated infection.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Febrile paroxysms: pyrogenic prostaglandins, induced by the TNF and IL-1 (already mapped) released when infected red cells rupture, drive the characteristic cyclical fevers of malaria synchronised to the parasite's erythrocytic cycle.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Hypoglycaemia: severe malaria causes hypoglycaemia from parasite glucose consumption and impaired gluconeogenesis, compounded by quinine-induced hyperinsulinaemia (insulin already mapped) that disturbs the incretin GLP-1 axis of glucose control.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Antibody help: IL-4 and the Th2 response support the B-cell antibody production against Plasmodium (IL-12 and interferon-gamma already mapped for Th1), the humoral arm of the partial immunity acquired with repeated malaria.
- `connects-to` → **[Endothelial cell](../../04-cellular/endothelial-cell/README.md)** — Cytoadherence and sequestration: falciparum-infected red cells bind the endothelial cells via PfEMP1 (angiopoietin and von Willebrand factor already mapped), sequestering in the microvasculature to cause the cerebral and placental complications of severe malaria.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Malaria-protective haemoglobinopathy: the thalassaemia trait, like sickle trait, offers partial protection against severe malaria (haemoglobin already mapped), the balancing selection that maintains these haemoglobinopathies in malaria-endemic regions.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron tug-of-war: Plasmodium needs iron to grow, and the host restricts it through hepcidin and ferroportin (already mapped), a nutritional-immunity battle in which iron status also influences susceptibility to malaria.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 immune arm: IL-13, with IL-4 (already mapped), is part of the Th2 response whose balance against the Th1 (IL-12 and IFN-γ already mapped) shapes the immune control and immunopathology of malaria.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and nutritional immunity: zinc, with the iron (already mapped) of nutritional immunity, is important for the antimalarial immune response, and zinc deficiency in endemic malnourished children increases the malaria morbidity.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Malnutrition and immunity: the adipokine leptin links the undernutrition common in endemic regions to the impaired immune response, modulating the susceptibility to and severity of malaria in undernourished children.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Malnutrition adipokine: adiponectin, with leptin (already mapped), is the adipokine of the malnutrition-immunity axis of the undernourished endemic children that modulates the malaria susceptibility.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the malnutrition-immunity axis and the inflammatory (TNF and IL-6 already mapped) response of malaria.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present the Plasmodium antigens and prime the T-cell (already mapped) response, though the malaria also impairs their function as immune evasion.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Immunosuppressive Tregs: the Plasmodium induces the regulatory T cells (IL-10 already mapped) that dampen the protective immunity, enabling the parasite persistence in malaria.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophilia of the type-2 immune response in malaria.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Polyclonal IgE: the polyclonal B-cell activation of malaria raises the IgE (with IL-4 and IL-13 already mapped), part of the type-2 immune dimension of the infection.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory immune response to the malaria parasite.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper balance: the CD4 T-helper cells set the Th1 (IFN-γ already mapped) protective versus Th2 (IL-4 already mapped) balance that determines the outcome of the malaria infection.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Atypical memory B cells: the malaria drives the expansion of the atypical memory B cells and the polyclonal (IgE already mapped) activation, shaping the slowly-acquired antibody immunity to the parasite.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped), driven by the excess C5a, contributes to the inflammation and the endothelial injury of severe and cerebral malaria.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: Plasmodium recruits the host factor H (via the RIFIN and Pf surface proteins) to its infected erythrocytes (already mapped) to accelerate the C3-convertase decay and evade the complement attack.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron competition: transferrin, the iron carrier, is part of the host iron-handling that, with the disordered hepcidin (already mapped), governs the iron availability contested between the host and the intraerythrocytic parasite in malaria.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical/lectin complement (C3, C5, C5aR1 and factor H already mapped) and the contact-kinin systems activated in the microvascular thromboinflammation of severe malaria.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — vWF microthrombosis: the ADAMTS13 protease is consumed in severe malaria, so the ultra-large von Willebrand factor (already mapped) multimers persist and drive the platelet (already mapped) microthrombosis and endothelial sequestration of cerebral malaria.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Vascular mast cells: the mast cells, activated in malaria, contribute to the vascular permeability and the intestinal and systemic inflammation accompanying the infection.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-parasite axis: TSLP, released from barrier epithelial cells during the systemic inflammation of malaria, activates dendritic cells (already mapped) and shapes the Th2-biased immune response that facilitates the parasite (Plasmodium already mapped) persistence in malaria.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin fever amplifier: bradykinin, generated by the kallikrein-kinin pathway activated by Plasmodium (already mapped) metabolites and haemolysis products, amplifies the vascular permeability, fever, and the cytokine storm (already mapped) of severe malaria.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell histamine: histamine, released by the mast cells (already mapped) activated during malaria, amplifies the vascular permeability, the pain of the haemolytic fever episodes, and the intestinal inflammation of the disease.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Hepatosplenic fibrosis: periostin, induced by TGF-β (already mapped) in the spleen (already mapped) and liver (already mapped) during Plasmodium (already mapped) infection, promotes the fibrotic remodelling and hypersplenism sequelae of chronic malaria.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian fever synchrony: melatonin regulates the circadian pattern of the Plasmodium (already mapped) release from erythrocytes (already mapped), synchronising the periodic fever paroxysms (complement already mapped) of malaria to nocturnal peaks of melatonin.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine coupling: prolactin, elevated during the acute febrile response of malaria, potentiates macrophage (already mapped) and NK-cell (already mapped) activation, contributing to the Th1/IFN-γ (already mapped) immunity and the immunopathology of severe malaria.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — MAL testosterone: androgen signalling suppresses the IFN-γ (already mapped) Th1 response to Plasmodium (already mapped), increasing male susceptibility to severe malaria; testosterone modulates erythrocyte (already mapped) membrane deformability in the infected red cell.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — MAL serotonin: platelet (already mapped) serotonin released during haemolysis in malaria amplifies vascular permeability and the thromboinflammation of severe malaria; 5-HT2 signalling on endothelial cells (already mapped) promotes Plasmodium (already mapped) rosetting.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — MAL vasopressin: vasopressin released during severe malaria drives cerebral oedema via brain (already mapped) swelling and hyponatraemia via sodium (already mapped) dysregulation; V2-receptor signalling on the kidney (already mapped) modulates renal water retention.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — MAL oxytocin: oxytocin suppresses NF-κB (already mapped) and TNF-α (already mapped) driven endothelial-cell (already mapped) activation during severe malaria; oxytocin attenuates macrophage (already mapped) inflammatory cytokine release and platelet (already mapped) aggregation.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — MAL selenium: selenoproteins attenuate ROS-driven NF-κB (already mapped) and TNF-α (already mapped) mediated endothelial-cell (already mapped) damage during malaria; selenium deficiency worsens haemolytic anaemia via erythrocyte (already mapped) membrane oxidative stress.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — MAL iodine: thyroid hormones modulate macrophage (already mapped) and nitric-oxide (already mapped) driven immune responses during malaria; iodine deficiency impairs NF-κB (already mapped) and IL-6 (already mapped) driven defence against Plasmodium falciparum (already mapped).
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — MAL magnesium: magnesium, as enzymatic cofactor in macrophages (already mapped) and erythrocytes (already mapped), supports immune and oxygen-transport function; magnesium deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) haemolytic cascade of malaria.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — MAL copper: copper, as cofactor of SOD1 in macrophages (already mapped) and neutrophils (already mapped), neutralises ROS; copper deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) oxidative haemolytic cascade of malaria.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — MAL phosphorus: phosphorus, as ATP precursor in erythrocytes (already mapped) and macrophages (already mapped), supports cellular energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of malaria.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — MAL chloride: chloride regulates macrophage (already mapped) and erythrocyte (already mapped) ion homeostasis; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) haemolytic cascade of malaria.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — MAL sulfur: sulfur, as glutathione precursor in erythrocytes (already mapped) and macrophages (already mapped), scavenges haemolytic ROS; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of malaria.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — MAL nitrogen: nitrogen, as RNS via iNOS in macrophages (already mapped) and erythrocytes (already mapped), drives haemolytic stress; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of malaria.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Malaria carbon: carbon as backbone of haemoglobin (already mapped) and merozoite structural proteins sustains erythrocyte (already mapped) invasion; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of malaria.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Malaria PD-1: PD-1 checkpoint on T-cells (already mapped) drives immune exhaustion during chronic Plasmodium infection; PD-1 overexpression amplifies IL-10 (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) immune-suppression cascade of malaria.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Malaria angiotensin-II: angiotensin-II drives macrophage (already mapped) and endothelial (already mapped) inflammation in Plasmodium infection; angiotensin-II amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) haemolytic cascade of malaria.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Malaria WNT: WNT-β-catenin in macrophages (already mapped) and hepatocytes (already mapped) modulates Plasmodium liver-stage invasion; WNT dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) immune cascade of malaria.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Malaria RANKL: RANKL drives dendritic-cell (already mapped) and macrophage (already mapped) immune activation against Plasmodium; RANKL dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) immune cascade of malaria.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Malaria smad4: SMAD4 in hepatocytes (already mapped) and macrophages (already mapped) mediates TGF-β signalling; smad4 dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Malaria fibronectin: fibronectin in endothelial cells (already mapped) and macrophages (already mapped) mediates parasite sequestration; fibronectin dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) cascade of malaria.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Malaria notch: NOTCH in macrophages (already mapped) and dendritic cells (already mapped) regulates anti-malarial immunity; notch dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Malaria igf-1: IGF-1 from macrophages (already mapped) and dendritic cells (already mapped) modulates anti-malarial immunity; igf-1 dysregulation amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Malaria activin-a: activin-A from macrophages (already mapped) and dendritic cells (already mapped) drives immune polarisation; activin-a excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Malaria tgf-beta: TGF-β from macrophages (already mapped) and dendritic cells (already mapped) regulates malarial immunosuppression; tgf-beta excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Malaria cgrp: CGRP from macrophages (already mapped) and dendritic cells (already mapped) modulates malarial neuroimmune tone; cgrp excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Malaria calcitonin: calcitonin from macrophages (already mapped) and dendritic cells (already mapped) modulates calcium tone; calcitonin excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — Malaria substance-p: substance-P from macrophages (already mapped) and dendritic cells (already mapped) modulates immune tone; substance-p excess amplifies il-6 (already mapped) and tnf-alpha (already mapped) and nf-kb (already mapped) immunopathological cascade of malaria.

[^who-malaria-report-2023]: World Health Organization. World Malaria Report 2023. WHO; 2023.
[^white-2014-malaria-lancet]: White NJ, Pukrittayakamee S, Hien TT, et al. Malaria. *Lancet.* 2014;383(9918):723-735. [doi:10.1016/S0140-6736(13)60024-0](https://doi.org/10.1016/S0140-6736(13)60024-0) · [PubMed 23953767](https://pubmed.ncbi.nlm.nih.gov/23953767/)
[^dondorp-2010-severe-malaria-lancet]: Dondorp AM, Fanello CI, Hendriksen IC, et al. Artesunate versus quinine in the treatment of severe falciparum malaria in African children (AQUAMAT). *Lancet.* 2010;376(9753):1647-1657. [doi:10.1016/S0140-6736(10)61924-1](https://doi.org/10.1016/S0140-6736(10)61924-1) · [PubMed 21062666](https://pubmed.ncbi.nlm.nih.gov/21062666/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
