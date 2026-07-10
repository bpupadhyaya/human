---
schema: human-scale-entry/v1
id: covid-19-disease
name: COVID-19 Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Multisystem infectious disease caused by SARS-CoV-2; clinical spectrum from asymptomatic to severe ARDS and cytokine storm. Spike protein binds ACE2 for cell entry; hyperinflammation drives severe disease; mRNA vaccines (mRNA-1273, BNT162b2) provide high efficacy."
aliases: ["COVID-19", "coronavirus disease 2019", "SARS-CoV-2 infection", "COVID"]
sources:
  - id: guan-2020-china-cohort
    type: peer-reviewed
    cite: "Guan WJ, Ni ZY, Hu Y, et al. Clinical Characteristics of Coronavirus Disease 2019 in China. N Engl J Med. 2020;382(18):1708-1720."
    doi: "10.1056/NEJMoa2002032"
    pmid: "32109013"
    url: "https://doi.org/10.1056/NEJMoa2002032"
  - id: hoffmann-2020-ace2-entry
    type: peer-reviewed
    cite: "Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. Cell. 2020;181(2):271-280."
    doi: "10.1016/j.cell.2020.02.052"
    pmid: "32142651"
    url: "https://doi.org/10.1016/j.cell.2020.02.052"
  - id: polack-2020-bnt162b2
    type: peer-reviewed
    cite: "Polack FP, Thomas SJ, Kitchin N, et al. Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine. N Engl J Med. 2020;383(27):2603-2615."
    doi: "10.1056/NEJMoa2034577"
    pmid: "33301246"
    url: "https://doi.org/10.1056/NEJMoa2034577"
cross_links:
  - target: 01-human/03-molecular/ace2
    relation: modulates
    note: "SARS-CoV-2 spike protein binds ACE2 for cell entry; viral binding downregulates surface ACE2, shifting angiotensin II/Ang-(1-7) balance toward pro-inflammatory Ang II signaling — amplifying vascular injury and cytokine release in severe COVID-19."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe COVID-19 is pathologically defined by a hyperinflammatory cytokine release syndrome (elevated IL-6, IL-1β, TNF-α, ferritin); cytokine storm drives the vascular leak, ARDS, multiorgan failure, and high mortality of critical COVID-19."
  - target: 01-human/06-organ/lung
    relation: targets
    note: "The lung is the primary target organ in COVID-19 pneumonitis: diffuse alveolar damage, type II pneumocyte injury, pulmonary vascular thrombosis, and hyaline membrane formation produce the bilateral infiltrates and hypoxemia characteristic of COVID-19 ARDS."
  - target: 01-human/07-system/respiratory-system
    relation: targets
    note: "SARS-CoV-2 infects upper and lower respiratory epithelium via ACE2; initial upper respiratory replication (nasal turbinates, oropharynx) is followed by lower respiratory spread in severe cases, causing COVID-19 pneumonia and respiratory failure."
  - target: 01-human/07-system/sars-cov-2
    relation: connects-to
    note: "SARS-CoV-2 betacoronavirus causes COVID-19; NSP5 Mpro (nirmatrelvir), NSP12 RdRp (remdesivir), and Spike (vaccine antigen) are the key drug/vaccine targets; NSP1/ORF6 IFN evasion enables early viral amplification; Omicron immune escape lineages drive ongoing pandemic waves."
  - target: 01-human/03-molecular/sars-cov-2-spike
    relation: connects-to
    note: "SARS-CoV-2 Spike is the COVID-19 vaccine antigen; RBD:ACE2 binding (Kd ~15 nM) initiates infection of airway epithelium and type II pneumocytes; Spike-mediated ACE2 internalization amplifies ARDS; 2P-stabilized prefusion Spike is the basis of all approved mRNA vaccines."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "COVID-19 and RSV are enveloped respiratory RNA viruses driving the seasonal lower-respiratory burden alongside influenza; both cause bronchiolitis/pneumonia at the extremes of age, both are now vaccine-preventable in older adults, and multiplex panels distinguish them."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "COVID-19 and influenza are the dominant pandemic-capable respiratory viruses—overlapping fever, cough and pneumonia but distinct treatments (nirmatrelvir/remdesivir vs oseltamivir/baloxavir); co-circulation strains health systems and both have annually updated vaccines."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: connects-to
    note: "SARS-CoV-2 targets ACE2-expressing alveolar type II pneumocytes: infection destroys these surfactant-producing progenitor cells → alveolar collapse, hyaline membranes and diffuse alveolar damage → ARDS; their loss impairs lung repair and underlies severe COVID-19 hypoxemia."
  - target: 03-medicine/01-modern/12-anti-inflammatory/dexamethasone
    relation: treated-by
    note: "RECOVERY trial (Horby 2021): 6 mg OD × 10 days reduced 28-day mortality by 17% (RR 0.83) in patients requiring oxygen; 29% reduction in mechanically ventilated patients; no benefit in those not requiring supplemental oxygen."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: treated-by
    note: "RECOVERY trial (2021): dexamethasone 6 mg/d × 10 days; 36% 28-day mortality reduction in mechanically ventilated patients (RR 0.64); 18% reduction in those requiring supplemental oxygen; class mechanism: GR:NF-κB transrepression of cytokine genes."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "COVID-19 is strongly prothrombotic: SARS-CoV-2 endothelial injury and intense inflammation drive immunothrombosis, raising deep vein thrombosis, pulmonary embolism, and microvascular clots—so inpatients get thromboprophylaxis and D-dimer marks severity."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "COVID-19 is in part an endothelial disease: SARS-CoV-2 and inflammation injure ACE2-bearing endothelial cells, causing endotheliitis, microthrombi, and the capillary leak that drives severe lung and multi-organ failure—the virus's vascular face."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages drive severe COVID-19's cytokine storm: dysregulated alveolar macrophages pour out IL-6 and TNF in a macrophage-activation-like syndrome, fueling the hyperinflammation that dexamethasone and IL-6 blockade (tocilizumab) target in critically ill patients."
  - target: 01-human/06-organ/ards
    relation: connects-to
    note: "ARDS is the lethal pulmonary endpoint of severe COVID-19: SARS-CoV-2 injury to alveolar epithelium and endothelium floods the lungs with protein-rich edema, collapsing gas exchange and requiring ventilation or ECMO—the final common pathway of fatal COVID pneumonia."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes markedly worsens COVID-19: hyperglycemia and the inflammatory, prothrombotic milieu of diabetes raise the risk of severe disease and death, while COVID can itself precipitate hyperglycemia and new diabetes—a bidirectional, dangerous interaction."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "COVID-19 raises stroke risk through its prothrombotic state: SARS-CoV-2-driven endothelial injury and hypercoagulability cause arterial thromboses, so ischemic stroke is a recognized complication alongside the venous thromboembolism the infection provokes."
  - target: 01-human/05-tissue/alveolus
    relation: targets
    note: "COVID-19 pneumonia injures the alveolus directly: SARS-CoV-2 infects ACE2-bearing type II pneumocytes lining the air sacs, triggering diffuse alveolar damage, hyaline membranes and flooding that impair gas exchange and underlie hypoxemic respiratory failure."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon is the fault line of severe COVID-19: inborn errors or autoantibodies blunting interferon predispose to critical disease, while SARS-CoV-2 also actively suppresses it—explaining why a weak early interferon response lets the virus run unchecked."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils worsen severe COVID-19: they flood inflamed lungs and release neutrophil extracellular traps (NETs) that drive immunothrombosis, clogging pulmonary microvessels and linking the hyperinflammatory and clotting features of the disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "COVID-19 reaches beyond the lungs to the brain: loss of smell and taste, strokes, and the lingering brain fog of long COVID reflect both direct effects and inflammation, so neurological symptoms are now recognized as core features, not rare complications."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "COVID-19 injures the heart: the infection and its inflammation cause myocarditis, arrhythmias, and raised troponin, and survivors carry elevated cardiovascular risk for months—so cardiac monitoring matters even after the respiratory illness resolves."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are central to COVID immunity: they generate the neutralizing antibodies that vaccines and prior infection rely on, but spike mutations in new variants erode that antibody protection—driving the need for updated boosters and explaining reinfections."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells clear SARS-CoV-2-infected cells: CD8 T-cell responses help end the infection and, as durable memory, underpin protection from severe disease after infection or vaccination even when antibodies wane."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 drives COVID-19's cytokine storm: severe disease floods the blood with IL-6, fueling the hyperinflammation that injures the lungs—so the IL-6-blocker tocilizumab improves survival in critically ill patients alongside steroids."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "COVID-19 frequently injures the kidney: acute kidney injury is common in severe disease from direct infection, cytokines and microthrombi, and needing dialysis sharply worsens outcomes—evidence the virus is multisystem, not just respiratory."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "COVID injures organs by unbalancing angiotensin II: the virus's spike commandeers and downregulates ACE2, the enzyme that normally degrades angiotensin II, so unopposed angiotensin II fuels the vasoconstriction, inflammation, and lung damage of severe disease."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Severe COVID is a clotting disease marked by fibrinogen: the inflamed endothelium and high fibrinogen drive immunothrombosis—microclots in the lungs and elsewhere—so anticoagulation became part of treating hospitalized patients."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK cells are the early antiviral defense against COVID: they kill infected cells before adaptive immunity kicks in, and their exhaustion in severe disease is linked to failure to control the virus and worse outcomes."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "COVID-19's defining danger is silent hypoxia: the virus damages the gas-exchange surface so oxygen falls, sometimes profoundly, before patients feel breathless—why pulse-oximeter monitoring became central to spotting deteriorating disease."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "COVID is not only a lung disease—it hits the gut: ACE2 is abundant on intestinal cells, so the virus infects the bowel, causing diarrhea and prolonged fecal shedding that underpins wastewater surveillance."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "COVID makes blood clot through activated platelets: the infection primes platelets and the endothelium toward thrombosis, driving the strokes, pulmonary emboli and microclots that mark severe disease—why anticoagulation is used."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Chest imaging gauges COVID pneumonia: CT scans read in X-ray photons reveal the hallmark peripheral ground-glass opacities, helping judge how far the lung injury has spread when oxygen levels fall."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Severe COVID can scar the lungs: the diffuse alveolar damage may heal with pulmonary fibrosis, leaving survivors with lasting breathlessness and reduced lung function long after the infection clears."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "COVID derails iron handling: ferritin soars as a marker of the hyperinflammatory state, while iron gets locked away from the blood, contributing to the anemia of inflammation in prolonged illness."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy gave COVID its face: the beam revealed SARS-CoV-2 as a sphere ringed by club-shaped spikes — the 'corona' that names the family — and showed the virions budding inside infected airway cells."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "COVID writes itself on the skin: chilblain-like 'COVID toes,' along with hive-like and measles-like rashes, reflect the small-vessel inflammation and clotting the infection provokes far from the lungs."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D drew intense scrutiny in COVID: deficiency was repeatedly tied to more severe disease, plausible given the vitamin's role in tempering the immune response, though supplementation trials gave mixed results."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "COVID reaches the nervous system: the sudden loss of smell points to damage around olfactory neurons, while brain fog, lingering cognitive complaints, and rare Guillain-Barré mark its broader, sometimes lasting, neural toll."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver often registers the infection: mildly raised transaminases are common in COVID, from direct injury, the cytokine storm, and the drugs used to treat it, usually settling as the patient recovers."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "COVID can disturb blood sugar: SARS-CoV-2 infects the ACE2-bearing islet cells, and new-onset hyperglycemia and diabetes appearing during or after infection suggest the virus can injure the insulin-making pancreas."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies are the immune memory of COVID: neutralizing antibodies against the spike, raised by infection or vaccine, block ACE2 binding, while serology dates past exposure and the monoclonal antibodies that once treated it were outrun by escape variants."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy raises the stakes: COVID is more severe in pregnant women and increases preterm birth and stillbirth, while the virus also transiently lowers sperm quality through ACE2-bearing testicular cells — reasons vaccination is urged."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T cells both fight and falter in COVID: severe disease brings a striking lymphopenia as T helper cells are depleted and exhausted, even as the T-cell response is central to clearing the virus and to lasting vaccine immunity."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "COVID reaches the heart muscle: the virus and the inflammation it ignites injure cardiomyocytes, causing a troponin rise, myocarditis and arrhythmias in acute illness and lingering palpitations and chest pain in long COVID."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The virus trips an inflammatory alarm: SARS-CoV-2 activates the NLRP3 inflammasome in macrophages to release IL-1β, a key spark of the cytokine storm that drives severe COVID and a target of anti-inflammatory therapy."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "COVID can inflame the thyroid: subacute (de Quervain) thyroiditis is a recognized sequela, transiently disturbing thyroid function weeks after the infection through immune-mediated gland injury."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Disabling ACE2 may unleash a 'bradykinin storm': because ACE2 normally degrades bradykinin, the virus's hijacking of the receptor lets this vasodilator build up, a proposed driver of the vascular leak and fluid-filled lungs of severe COVID."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "It can misdirect the immune attack onto nerves: COVID is among the infections that trigger Guillain-Barré syndrome, an autoimmune assault on peripheral nerve myelin causing ascending weakness in the weeks after illness."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Overactive mast cells may fuel the worst of it: mast cell activation contributes to the cytokine surge of severe disease and is a leading suspect in the lingering, multi-system symptoms of long COVID."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB ignites the cytokine storm: SARS-CoV-2 sensing in airway and immune cells drives NF-κB to pour out IL-6, TNF and other mediators, the transcriptional engine behind the hyperinflammation of severe COVID."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 amplifies the inflammatory loop: the flood of IL-6 in severe COVID activates STAT3, sustaining the feed-forward cytokine signaling that the IL-6 blocker tocilizumab targets in critically ill patients."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Severe disease behaves like viral sepsis: critical COVID produces the dysregulated host response, shock and multiorgan failure of sepsis, and bacterial superinfection of the damaged lungs can layer true bacterial sepsis on top."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "It opens the lung to the mold: damaged airway epithelium plus the steroids and immune dysregulation of severe COVID give rise to COVID-associated pulmonary aspergillosis (CAPA), a dangerous superinfection in the ICU."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The kidney is a frequent casualty: COVID causes acute kidney injury through direct ACE2-mediated infection, cytokine injury and microthrombi, and severe AKI can fail to fully recover, leaving chronic kidney disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Its long tail reaches the mind: post-COVID and long-COVID syndromes carry high rates of depression, from the neuroinflammatory effects of the virus and the psychological toll of severe illness and prolonged recovery."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "It can inflame and weaken the heart: SARS-CoV-2 causes myocarditis and direct cardiac injury, and severe COVID's hypoxia and cytokine storm strain the myocardium, leaving some patients with new heart failure."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Lung and clot damage can pressurize the pulmonary arteries: severe COVID's diffuse lung injury, fibrosis and pulmonary emboli can raise pulmonary vascular resistance, leaving chronic thromboembolic or post-inflammatory pulmonary hypertension."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Critical illness leaves psychological scars: survivors of severe COVID, especially ICU and ventilator patients, develop post-traumatic stress as part of the post-intensive-care and long-COVID burden."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It dysregulates immunity in both directions: severe COVID drives a hyperinflammatory cytokine surge yet also causes lymphopenia, and in children the post-infectious MIS-C is a striking immune complication."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The virus reaches the nervous system: COVID causes anosmia, encephalopathy and the brain fog of long COVID, and is linked to Guillain-Barré syndrome and a raised stroke risk."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Both infection and pandemic breed worry: long-COVID symptoms, the dread of severe illness and the upheaval of the pandemic fuelled a marked rise in anxiety alongside the depression and PTSD it left."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It strikes the heart directly: COVID-19 can cause acute myocarditis, arrhythmias and a raised risk of myocardial infarction, with troponin rises marking myocardial injury in severe disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It enters and irritates the gut: ACE2 on intestinal and liver cells lets SARS-CoV-2 cause diarrhoea and nausea and raise transaminases, sometimes as the presenting features of COVID-19."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It leaves marks on the skin: chilblain-like 'COVID toes', maculopapular eruptions and urticaria are recognised cutaneous signs, sometimes appearing when respiratory symptoms are mild."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It depletes the lymphocytes: lymphopenia is a hallmark laboratory finding and prognostic marker in COVID-19, reflecting the immune dysregulation of severe disease."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It can shut down the kidney: severe COVID-19 causes acute kidney injury, and a collapsing glomerulopathy occurs in people carrying high-risk APOL1 variants."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It unsettles glucose and the thyroid: COVID-19 can precipitate new-onset hyperglycaemia and diabetes, and subacute thyroiditis can follow the infection."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "It aches and wastes muscle: COVID-19 causes prominent myalgia and, in severe or prolonged illness, myositis, rhabdomyolysis and the deconditioning of long COVID."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Immunomodulators tame severe disease: the IL-6 inhibitor tocilizumab and the JAK inhibitor baricitinib reduce mortality in severe COVID-19 by dampening the hyperinflammatory response."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Bacteria complicate the viral pneumonia: secondary bacterial infection, including pneumococcal pneumonia, worsens severe COVID-19, as it does in influenza."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: connects-to
    note: "It is a thrombotic disease: severe COVID-19 drives venous thromboembolism and microthrombi, so hospitalised patients receive prophylactic anticoagulation, and the coagulopathy is a central reason for its high mortality."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It injures the heart muscle: COVID-19 causes myocarditis and troponin-positive cardiac injury through direct infection and cytokine storm, with arrhythmia and heart failure — and rare myocarditis also follows mRNA vaccination."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It is an endothelial disease: SARS-CoV-2 infects and inflames the vascular endothelium, and this endotheliitis of the arterial wall underlies the microthrombi, strokes and multi-organ ischaemia of severe COVID-19."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "It injures the kidney's filter: COVID-19 causes acute kidney injury and a collapsing glomerulopathy (especially with APOL1 risk variants), with ACE2 expression making the glomerulus a target of SARS-CoV-2."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Long COVID overlaps chronic-fatigue syndromes: persistent post-COVID fatigue, widespread pain and autonomic dysfunction overlap heavily with fibromyalgia and ME/CFS, a post-viral chronic-symptom state."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "It can precipitate diabetes: COVID-19 raises the risk of new-onset diabetes, both stress-driven type 2 and autoimmune-pattern type 1, with ACE2 on pancreatic islets implicated in beta-cell injury."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Disrupted germinal centres: severe COVID-19 can ablate lymph-node germinal centres, blunting durable antibody maturation, whereas mRNA vaccines instead drive robust, long-lived germinal-centre responses."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "A leading severity risk: obesity was among the strongest predictors of severe COVID-19, through impaired ventilation, a pro-inflammatory adipose milieu and underlying endothelial dysfunction."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Marrow under strain: severe COVID-19 drives profound lymphopenia and emergency myelopoiesis, releasing immature, dysfunctional neutrophils from the bone marrow that amplify the inflammatory response."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Accelerated vascular disease: endothelial injury and systemic inflammation from COVID-19 destabilise atherosclerotic plaque, raising heart-attack and stroke risk for months after even mild infection."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "A distinct coagulopathy: severe COVID-19 produces a hypercoagulable state with high D-dimer and fibrinogen and widespread microthrombi that, in the sickest patients, tips into disseminated intravascular coagulation."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "A pandemic syndemic: COVID-19 disrupted tuberculosis programmes worldwide and reversed years of progress, and the two respiratory infections can coexist and worsen each other's course."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement-driven injury: complement activation, especially C5a, drives the endothelial damage and microthrombosis of severe COVID-19, prompting trials of anti-complement therapy."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammasome cytokine: IL-1β from inflammasome activation fuels the hyperinflammation of severe COVID-19, the target of IL-1 blockade such as anakinra."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Cytokine storm component: TNF-α contributes to the systemic cytokine storm of severe COVID-19, alongside IL-6 in driving its hyperinflammatory state."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Antiviral and immunopathic: IFN-γ from T and NK cells helps clear SARS-CoV-2 but, when dysregulated, drives the macrophage activation and hyperinflammation of severe COVID-19."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes into the infected lung in COVID-19, where they fuel the alveolar inflammation and damage of severe disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic amplification: the profound hypoxia of COVID-19 pneumonia stabilises HIF-1α, which further amplifies inflammation and the prothrombotic state in a vicious cycle."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine-signalling blockade: the hyperinflammatory cytokines of severe COVID-19 signal through JAK-STAT, the rationale for baricitinib (a JAK1/2 inhibitor) which reduces mortality in hospitalised patients."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endotheliopathy: SARS-CoV-2 injury to endothelium releases ultra-large von Willebrand factor multimers, driving the platelet-rich microthrombosis that underlies the characteristic COVID-19 coagulopathy."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate hyperactivation: the SARS-CoV-2 spike protein can engage TLR4 on innate immune cells, triggering the NF-κB-driven cytokine output that contributes to the hyperinflammation of severe COVID-19."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Landmark therapy: dexamethasone acting through the glucocorticoid receptor was the first treatment shown to cut mortality in severe COVID-19, broadly suppressing the NF-κB-driven cytokine programme that injures the lungs in the hyperinflammatory phase."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "Viral RNA sensing: the cytosolic sensor RIG-I detects SARS-CoV-2 RNA to trigger the type-I-interferon response, and the virus's active antagonism of this pathway explains the blunted, delayed interferon that permits early uncontrolled replication."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Immunothrombosis: endothelial injury and neutrophil activation in severe COVID-19 drive excess thrombin generation, producing the pulmonary microthrombi and venous thromboembolism that are a major cause of death and the rationale for anticoagulation."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "Interferon evasion: SARS-CoV-2 proteins antagonise RIG-I/MAVS antiviral signalling (RIG-I already mapped) to suppress the early type-I interferon response, an immune-evasion mechanism that contributes to severe, delayed-interferon COVID-19."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "Blocked IFN induction: multiple SARS-CoV-2 ORF proteins block IRF3 activation and nuclear translocation, dampening interferon induction so that the dysregulated, delayed interferon response shapes COVID-19 severity."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet immunothrombosis: platelet factor 4 is central to the platelet activation and immunothrombosis of severe COVID-19, and anti-PF4 antibodies underlie the rare vaccine-induced thrombotic thrombocytopenia (VITT)."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Antiviral IFN signaling: type-I interferon signals through JAK (mapped) to STAT1 to induce antiviral genes, the program SARS-CoV-2 antagonizes — delayed and then dysregulated IFN-STAT1 signaling drives severe COVID-19."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate amplification: TLR4 (mapped) sensing of spike and DAMPs signals through MyD88 to NF-κB (mapped), amplifying the innate inflammatory response that fuels severe COVID-19."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endotheliopathy: Ang-2 released from activated endothelium marks the endothelial dysfunction and microvascular thrombosis of severe COVID-19, correlating with disease severity."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement amplification: complement activation at C3 (feeding the C5 axis already mapped) amplifies the thromboinflammation and endothelial injury of severe COVID-19."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA-sensing amplification: cGAS-STING sensing of cytosolic and mitochondrial DNA released during severe SARS-CoV-2 infection amplifies the type-I-interferon and inflammatory response (already mapped) contributing to immunopathology."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic antiviral arm: CD8 cytotoxic T cells and NK cells deploy perforin against infected cells in COVID-19, an antiviral effector arm whose dysregulation accompanies the lymphopenia of severe disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the macrophage-driven cytokine storm and NET-associated thromboinflammation of severe COVID-19."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling drives the post-COVID pulmonary fibrosis that follows the diffuse alveolar damage of severe COVID-19."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling in endothelium shapes the vascular dysfunction and procoagulant phenotype underlying the thrombotic complications of COVID-19."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Calprotectin (S100A8/A9) released by emergency myelopoiesis-derived neutrophils is a key driver and severity biomarker of the hyperinflammatory cytokine storm in severe COVID-19."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates lymphocyte homeostasis and oxidative-stress handling, processes whose dysregulation accompanies the lymphopenia and immune dysfunction of severe COVID-19."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of pattern-recognition and cytokine receptors amplifies the macrophage inflammatory response that fuels severe COVID-19."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling drives the metabolic reprogramming of the hyperinflammatory immune cells and is a therapeutic target in severe COVID-19."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven cytokine storm and the platelet activation of COVID-19 coagulopathy."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA) signaling participates in the immune-cell activation and endothelial dysfunction of severe COVID-19."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the immune-cell metabolism of the hyperinflammatory response to SARS-CoV-2."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "SARS-CoV-2 modulates host autophagy to support its replication, and autophagy shapes the innate immune response to COVID-19."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the endothelial and platelet activation of COVID-19 coagulopathy."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the hyperinflammation and lung immunopathology of COVID-19."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune responses to SARS-CoV-2 in COVID-19."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the immune-cell trafficking and vascular responses of COVID-19."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the lung inflammation and cytokine storm of COVID-19 disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the inflammatory and immunopathologic response of COVID-19 disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host immune response of COVID-19 disease."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Neutralising immunity: protective and vaccine-induced immunity to SARS-CoV-2 is carried largely by neutralising IgG against the spike protein (already mapped), and monoclonal IgG antibodies were an early therapeutic before variant escape blunted them."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac injury: myocardial injury marked by troponin elevation is common in severe COVID-19 and independently predicts mortality, reflecting myocarditis, microthrombosis and demand ischaemia from the systemic illness."
  - target: 01-human/03-molecular/surfactant
    relation: connects-to
    note: "Alveolar injury: SARS-CoV-2 infects and kills the type II pneumocytes that produce surfactant, and the resulting surfactant deficiency contributes to the alveolar collapse and ARDS of severe COVID-19 pneumonia."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Mucosal immunity: secretory IgA on the nasal and airway mucosa is a first line of defence against SARS-CoV-2 and a correlate of protection, motivating the intranasal vaccines designed to raise mucosal immunity at the site of entry."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Antigen presentation and vaccines: MHC class II presentation of viral antigens drives the CD4 T-cell help underlying antibody responses to SARS-CoV-2 infection and vaccination, and HLA variation influences the severity of COVID-19."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell response: IL-2-driven T-cell expansion generates the SARS-CoV-2-specific T cells that clear the virus (perforin already mapped) and provide durable protection, while the lymphopenia of severe disease reflects failure of this response."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: SARS-CoV-2 injury to the endothelium (already mapped) reduces protective nitric oxide, contributing to the vasoconstriction and microthrombosis of COVID-19, and inhaled nitric oxide has been trialled for the hypoxaemia."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Vascular permeability: VEGF released in the inflamed COVID-19 lung raises vascular permeability, worsening the pulmonary oedema of acute respiratory distress syndrome (angiopoietin already mapped) that impairs gas exchange."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune counter-regulation: IL-10 rises as a counter-regulatory response to the hyperinflammation of severe COVID-19 (IL-6 and IL-1 already mapped), and the balance between pro- and anti-inflammatory signals shapes whether the cytokine storm resolves."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Eicosanoid inflammation: prostaglandins from the COX pathway (IL-6 and IL-1 already mapped) amplify the inflammation of COVID-19, and thromboxane on the activated platelets (PF4 already mapped) contributes to the immunothrombosis."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "RAAS dysregulation: SARS-CoV-2 downregulates ACE2 (already mapped), the enzyme that degrades angiotensin II (already mapped), shifting the renin-angiotensin balance toward vasoconstriction and inflammation in severe COVID-19."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and antiviral immunity: zinc supports antiviral immunity and inhibits coronavirus replication in vitro, and the anosmia and dysgeusia of COVID-19 have been linked to disturbed zinc-dependent taste and smell signalling."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Hyperferritinaemia: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and drives the hyperferritinaemia that is a marker of the hyperinflammation and severity of COVID-19."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium and antiviral status: the antioxidant selenoprotein status of selenium supports antiviral immunity, and low selenium has been linked to worse COVID-19 outcomes in observational studies."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity risk: the adipokine leptin links obesity — a major risk factor for severe COVID-19 — to the metabolic-inflammatory state and impaired immunity behind the poor outcomes."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is the adipose-derived adipokine of the obesity risk and the metabolic-inflammatory state of severe COVID-19."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the obesity risk and the cytokine milieu (IL-6 already mapped) of severe COVID-19."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 imbalance: IL-4 and the type-2/Th2 arm; the dysregulated type-1/type-2 balance is part of the immune dysregulation of severe COVID-19."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "Causative virus: COVID-19 is caused by SARS-CoV-2, whose spike (already mapped) engages the ACE2 (already mapped) receptor for cell entry, the coronavirus of the pandemic."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 antiviral arm: IL-12 polarises the Th1 (IFN-γ already mapped) antiviral response, part of the type-1 immunity against SARS-CoV-2 in COVID-19."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 imbalance: IL-13, with IL-4 (already mapped), completes the type-2/Th2 arm of the dysregulated type-1/type-2 balance of severe COVID-19."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2/eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension whose blood eosinopenia is a marker of severe COVID-19."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the dysregulated inflammation of severe COVID-19."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the dysregulated type-1/type-2 balance of COVID-19."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "Causative virus: SARS-CoV-2, entering via the ACE2 (already mapped) receptor through its spike (already mapped), is the causative agent of COVID-19."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells: the pDCs are the major producers of the type-I interferon (already mapped), whose impaired or delayed response is a determinant of the severity of COVID-19."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment and the complement-mediated thromboinflammation of severe COVID-19."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation drives the complement-mediated thromboinflammation of severe COVID-19."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin regulation: the C1-esterase inhibitor regulates both the lectin/classical complement and the contact-kinin (bradykinin already mapped) systems whose dysregulation is implicated in the vascular leak and thromboinflammation of severe COVID-19."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Hypoferraemia: transferrin, the iron carrier, reflects the marked hypoferraemia and disordered iron handling (hepcidin already mapped) of the acute-phase response of severe COVID-19."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Airway alarmin: TSLP from the SARS-CoV-2 (already mapped)-infected airway epithelium (alveolus already mapped) activates mast cells (already mapped) and pDCs (dendritic-cell already mapped), amplifying the type-2 hypersensitivity and cytokine storm of severe COVID-19."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Hypoxia-driven EPO: erythropoietin, induced by COVID-19 ARDS hypoxia (oxygen already mapped) via HIF-1α (already mapped), supports erythropoiesis and tissue-protective signalling; EPO may also modulate the long-COVID pulmonary-artery remodelling (PAH already mapped)."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell histamine storm: histamine, released by the mast cells (already mapped) activated by the SARS-CoV-2 (already mapped) spike protein, amplifies the vascular permeability, bronchoconstriction and the inflammatory cytokine (IL-6 already mapped) storm of severe COVID-19."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM/fibrosis alarmin: periostin, induced by IL-4 and IL-13 (already mapped) in the post-COVID pulmonary fibrosis (fibroblast already mapped), promotes type-2 ECM remodelling of the alveoli (already mapped) and contributes to the long-COVID fibrotic lung complication."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian antioxidant: melatonin scavenges mitochondrial ROS (already mapped) and modulates the cytokine storm (IL-6 already mapped) of severe COVID-19; disrupted circadian rhythms worsen disease severity and melatonin deficiency is observed in critically ill patients."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine coupling: prolactin, elevated during the acute-phase response of severe COVID-19, potentiates macrophage (already mapped) and lymphocyte activation, contributing to the cytokine storm (IL-6 already mapped) and the hyperinflammatory state."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "COVID testosterone: androgen receptor signalling upregulates ACE2 (already mapped) in the lung (already mapped), amplifying viral entry; testosterone-driven immunosuppression worsens the male-sex COVID-19 IL-6 (already mapped) driven cytokine storm."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "COVID serotonin: SARS-CoV-2 depletes platelet serotonin via ACE2 (already mapped) mediated enterochromaffin cell damage; serotonin deficiency impairs the endothelial (already mapped) and lung (already mapped) vasoregulation, contributing to the post-COVID dysautonomia phenotype."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "COVID oxytocin: oxytocin reduces SARS-CoV-2 cytokine storm by suppressing IL-6 (already mapped) and TNF-α (already mapped) production; oxytocin also protects the endothelium (already mapped) and lung (already mapped) from COVID-19 thromboinflammatory injury."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "COVID vasopressin: vasopressin (ADH) modulates renal (already mapped) fluid balance in COVID-19 ARDS; AVP-driven V1 receptor activation amplifies pulmonary vascular inflammation and contributes to NF-κB (already mapped) cytokine storm (already mapped) in severe disease."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "COVID iodine: SARS-CoV-2 (already mapped) disrupts thyroid (already mapped) iodine metabolism; iodine deficiency amplifies NF-κB (already mapped) cytokine storm (already mapped) and impairs lung (already mapped) surfactant (already mapped) antioxidant defence via lactoperoxidase."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "COVID sodium: hypernatraemia in severe COVID-19 ARDS activates NF-κB (already mapped) and amplifies IL-6 (already mapped) driven cytokine storm (already mapped); sodium-glucose cotransporter inhibition reduces cardiac (already mapped) and renal (already mapped) complication risk."
---

# COVID-19 Disease

## Overview

**COVID-19 (Coronavirus Disease 2019)** is an infectious, multisystem disease caused by **SARS-CoV-2** (Severe Acute Respiratory Syndrome Coronavirus 2), a betacoronavirus identified in Wuhan, China in December 2019. It caused the first pandemic of the 21st century, responsible for >7 million documented deaths globally as of 2024 (with substantial excess-mortality estimates suggesting 14–24 million total).

The clinical spectrum is remarkably broad — ranging from **completely asymptomatic** (~35–45% of infections) to **mild-moderate respiratory illness** to **severe pneumonia, ARDS, and multiorgan failure**. Risk stratification is critically determined by age (strong exponential increase in severity/mortality above 50 years), immunosuppression, diabetes, obesity, cardiovascular disease, and CKD. The case-fatality rate (CFR) of the original Wuhan strain was ~1–3%; Omicron subvariants have substantially lower CFR (~0.1–0.3%) due to immune escape mutations reducing lower respiratory tropism and widespread population immunity from vaccination and prior infection.

SARS-CoV-2 belongs to the same betacoronavirus clade as SARS-CoV-1 (2003 outbreak) and shares the ACE2 receptor; its spike protein RBD has ~10–20× higher ACE2 affinity than SARS-CoV-1, contributing to efficient upper respiratory transmission.

## Structure

### Viral cell entry and early replication

SARS-CoV-2 infects cells via the **spike (S) protein** trimer on the viral surface [^hoffmann-2020-ace2-entry]:
1. **Receptor binding:** The spike receptor-binding domain (RBD) binds **ACE2** (angiotensin-converting enzyme 2) on host cell surfaces; ACE2 is highly expressed on type II pneumocytes, nasal goblet/ciliated cells, enterocytes, cardiomyocytes, and renal proximal tubule cells — explaining the multiorgan tropism
2. **Spike priming:** Host serine protease **TMPRSS2** (or cathepsin L in endosomes) cleaves the spike at S1/S2 and S2' sites → conformational change → fusion peptide insertion into host membrane → membrane fusion and viral entry
3. **Replication:** Positive-sense ssRNA genome (29.9 kb) → translation of replicase (ORF1a/1b, pp1a/pp1ab, cleaved to nsp1-16) → RNA-dependent RNA polymerase (nsp12) → genome replication and subgenomic mRNA synthesis → structural proteins (S, E, M, N) → assembly and budding from ER-Golgi intermediate compartment (ERGIC)

### Innate immune evasion and early pathogenesis

A key feature distinguishing SARS-CoV-2 from influenza is its ability to **suppress early innate immune responses**:
- ORF6 and ORF9b block type I interferon (IFN-α/β) signaling by sequestering KPNA2 and blocking STAT1/2 import
- nsp3 (papain-like protease) deubiquitinates innate signaling intermediates; nsp16 methylates viral RNA cap to avoid MDA5 recognition
- Result: initial viral replication can proceed with minimal IFN response → high viral loads in the nasopharynx → efficient spread; then delayed, dysregulated immune activation produces hyperinflammation

## Function

### Clinical course and staging [^guan-2020-china-cohort]

**Stage I — Asymptomatic/presymptomatic (days 1–5):**
Active viral replication in upper respiratory tract (nasopharynx, oropharynx); peak infectivity occurs 1–2 days before and within ~5 days of symptom onset; most transmission occurs in this window.

**Stage II — Mild-moderate disease (days 1–10):**
Fever, cough, myalgia, fatigue, headache, anosmia/ageusia (loss of smell/taste — characteristic of original strain and Delta but less prominent in Omicron); most patients recover without hospitalization; oxygen saturation normal at rest.

**Stage III — Severe disease (days 7–14, ~15% of symptomatic):**
COVID-19 pneumonia: bilateral infiltrates, progressive hypoxemia (SpO₂ <94%), dyspnea; CT: "ground-glass opacities," consolidation, vascular congestion; driven by viral cytopathology in type II pneumocytes and alveolar macrophage hyperactivation.

**Stage IV — Critical disease (~5% of symptomatic):**
ARDS (PaO₂/FiO₂ <300), requiring mechanical ventilation; associated:
- **Cytokine storm:** Hyperactivated innate immunity (macrophage activation, complement activation, NF-κB) → massive release of IL-6, IL-1β, TNF-α, GM-CSF → diffuse vascular leak, coagulation activation, multiorgan dysfunction
- **COVID-19-associated coagulopathy:** Microvascular thrombosis (fibrin, platelet-rich thrombi) in pulmonary vasculature and systemic organs → thrombocytopenia, elevated D-dimer, arterial/venous thromboembolism

**Long COVID (post-acute sequelae of SARS-CoV-2 / PASC):**
Symptoms persisting >4 weeks: fatigue (most common), cognitive impairment ("brain fog"), dyspnea, autonomic dysfunction (POTS), musculoskeletal pain. Affects 10–20% of hospitalized and 5–10% of non-hospitalized patients. Mechanisms: viral persistence, autoantibodies, immune dysregulation, mitochondrial dysfunction, gut microbiome disruption.

### Treatment

**Antivirals:**
- **Nirmatrelvir/ritonavir (Paxlovid):** Protease inhibitor combination; >85% reduction in hospitalization/death if given within 5 days of symptom onset to high-risk patients; broad effectiveness across variants (targets conserved Mpro)
- **Remdesivir:** Nucleoside analog inhibiting RdRp (nsp12); IV formulation; reduces hospitalization duration and progression to ARDS in moderately ill patients
- **Molnupiravir:** Oral mutagenic nucleoside; 30% risk reduction; inferior to nirmatrelvir

**Immunomodulation (severe/critical disease):**
- **Dexamethasone 6 mg daily × 10 days:** Reduces 28-day mortality by 35% in ventilated patients (RECOVERY trial); no benefit in non-oxygen-requiring patients
- **Anti-IL-6 (tocilizumab, sarilumab):** Additional mortality benefit in patients already on dexamethasone with severe disease (CRP-guided)
- **Baricitinib (JAK1/2 inhibitor):** WHO-recommended for severe/critical disease; reduces mortality

**mRNA vaccines [^polack-2020-bnt162b2]:**
- BNT162b2 (Pfizer-BioNTech): 95% efficacy against original-strain symptomatic infection (Phase 3); encodes pre-fusion stabilized spike (2P mutations)
- mRNA-1273 (Moderna): 94% efficacy; higher dose (100 μg), more reactogenic; similar durability
- Both vaccines drive robust germinal center reactions in draining lymph nodes (months-long GC persistence), generating high-affinity memory B cells and long-lived plasma cells

## Connections

- `modulates` → **[ACE2](../../03-molecular/ace2/README.md)** — SARS-CoV-2 binds and downregulates ACE2, shifting Ang II/Ang-(1-7) balance toward pro-inflammatory Ang II signaling; ACE2 downregulation contributes to vascular dysfunction, hypertension, and ARDS in severe COVID-19.
- `connects-to` → **[Cytokine Storm](../cytokine-storm/README.md)** — severe COVID-19 is characterized by pathological cytokine release (IL-6, IL-1β, TNF-α, ferritin elevation); cytokine storm is the proximate driver of ARDS, vascular injury, and multiorgan failure in critical COVID-19.
- `targets` → **[Lung](../../06-organ/lung/README.md)** — the lung is the primary COVID-19 target organ; diffuse alveolar damage, type II pneumocyte necrosis, and pulmonary vascular thrombosis produce the bilateral ground-glass infiltrates and hypoxemia of COVID-19 pneumonia.
- `targets` → **[Respiratory System](../respiratory-system/README.md)** — SARS-CoV-2 initiates infection in the upper respiratory epithelium (ACE2-TMPRSS2 expression) and progresses to lower respiratory tract pneumonitis in severe disease; respiratory failure is the leading cause of COVID-19 mortality.
- `connects-to` → **[SARS-CoV-2](../sars-cov-2/README.md)** — SARS-CoV-2 is the causative betacoronavirus; NSP5 Mpro (nirmatrelvir), NSP12 RdRp (remdesivir), and Spike (vaccine antigen) are the key targets; NSP1/ORF6 IFN evasion enables early viral amplification before adaptive immunity responds.
- `connects-to` → **[SARS-CoV-2 Spike](../../03-molecular/sars-cov-2-spike/README.md)** — Spike is the primary COVID-19 vaccine antigen; RBD:ACE2 binding initiates infection; Spike-mediated ACE2 internalization amplifies ARDS; 2P prefusion-stabilized Spike is the basis of all approved mRNA vaccines; Omicron BA.1's 37 Spike mutations drive extensive immune escape.
- `treated-by` → **[Dexamethasone](../../03-medicine/01-modern/12-anti-inflammatory/dexamethasone/README.md)** — RECOVERY trial (Horby 2021): 6 mg OD × 10 days reduced 28-day mortality by 17% (RR 0.83) in patients requiring oxygen; 29% mortality reduction in mechanically ventilated patients; no benefit in those not requiring supplemental oxygen.
- `treated-by` → **[Corticosteroids](../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — RECOVERY trial (2021): dexamethasone 6 mg/d × 10 days; 36% mortality reduction in mechanically ventilated patients (RR 0.64); 18% reduction in those requiring supplemental oxygen; mechanism: GR:NF-κB transrepression of pro-inflammatory cytokine genes.
- `connects-to` → **[RSV](../rsv/README.md)** — COVID-19 and RSV are enveloped respiratory RNA viruses driving the seasonal lower-respiratory burden alongside influenza; both cause bronchiolitis/pneumonia at the extremes of age, both are now vaccine-preventable in older adults, and multiplex panels distinguish them.
- `connects-to` → **[Influenza](../influenza/README.md)** — COVID-19 and influenza are the dominant pandemic-capable respiratory viruses—overlapping fever, cough and pneumonia but distinct treatments (nirmatrelvir/remdesivir vs oseltamivir/baloxavir); co-circulation strains health systems and both have annually updated vaccines.
- `connects-to` → **[Type II pneumocyte](../../04-cellular/type-ii-pneumocyte/README.md)** — SARS-CoV-2 targets ACE2-expressing alveolar type II pneumocytes: infection destroys these surfactant-producing progenitor cells → alveolar collapse, hyaline membranes and diffuse alveolar damage → ARDS; their loss impairs lung repair and underlies severe COVID-19 hypoxemia.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — COVID-19 is strongly prothrombotic: SARS-CoV-2 endothelial injury and intense inflammation drive immunothrombosis, raising deep vein thrombosis, pulmonary embolism, and microvascular clots—so inpatients get thromboprophylaxis and D-dimer marks severity.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — COVID-19 is in part an endothelial disease: SARS-CoV-2 and inflammation injure ACE2-bearing endothelial cells, causing endotheliitis, microthrombi, and the capillary leak that drives severe lung and multi-organ failure—the virus's vascular face.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages drive severe COVID-19's cytokine storm: dysregulated alveolar macrophages pour out IL-6 and TNF in a macrophage-activation-like syndrome, fueling the hyperinflammation that dexamethasone and IL-6 blockade (tocilizumab) target in critically ill patients.
- `connects-to` → **[Acute Respiratory Distress Syndrome](../../06-organ/ards/README.md)** — ARDS is the lethal pulmonary endpoint of severe COVID-19: SARS-CoV-2 injury to alveolar epithelium and endothelium floods the lungs with protein-rich edema, collapsing gas exchange and requiring ventilation or ECMO—the final common pathway of fatal COVID pneumonia.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes markedly worsens COVID-19: hyperglycemia and the inflammatory, prothrombotic milieu of diabetes raise the risk of severe disease and death, while COVID can itself precipitate hyperglycemia and new diabetes—a bidirectional, dangerous interaction.
- `connects-to` → **[Stroke](../stroke/README.md)** — COVID-19 raises stroke risk through its prothrombotic state: SARS-CoV-2-driven endothelial injury and hypercoagulability cause arterial thromboses, so ischemic stroke is a recognized complication alongside the venous thromboembolism the infection provokes.
- `targets` → **[Alveolus](../../05-tissue/alveolus/README.md)** — COVID-19 pneumonia injures the alveolus directly: SARS-CoV-2 infects ACE2-bearing type II pneumocytes lining the air sacs, triggering diffuse alveolar damage, hyaline membranes and flooding that impair gas exchange and underlie hypoxemic respiratory failure.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon is the fault line of severe COVID-19: inborn errors or autoantibodies blunting interferon predispose to critical disease, while SARS-CoV-2 also actively suppresses it—explaining why a weak early interferon response lets the virus run unchecked.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils worsen severe COVID-19: they flood inflamed lungs and release neutrophil extracellular traps (NETs) that drive immunothrombosis, clogging pulmonary microvessels and linking the hyperinflammatory and clotting features of the disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — COVID-19 reaches beyond the lungs to the brain: loss of smell and taste, strokes, and the lingering brain fog of long COVID reflect both direct effects and inflammation, so neurological symptoms are now recognized as core features, not rare complications.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — COVID-19 injures the heart: the infection and its inflammation cause myocarditis, arrhythmias, and raised troponin, and survivors carry elevated cardiovascular risk for months—so cardiac monitoring matters even after the respiratory illness resolves.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are central to COVID immunity: they generate the neutralizing antibodies that vaccines and prior infection rely on, but spike mutations in new variants erode that antibody protection—driving the need for updated boosters and explaining reinfections.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells clear SARS-CoV-2-infected cells: CD8 T-cell responses help end the infection and, as durable memory, underpin protection from severe disease after infection or vaccination even when antibodies wane.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 drives COVID-19's cytokine storm: severe disease floods the blood with IL-6, fueling the hyperinflammation that injures the lungs—so the IL-6-blocker tocilizumab improves survival in critically ill patients alongside steroids.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — COVID-19 frequently injures the kidney: acute kidney injury is common in severe disease from direct infection, cytokines and microthrombi, and needing dialysis sharply worsens outcomes—evidence the virus is multisystem, not just respiratory.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — COVID injures organs by unbalancing angiotensin II: the virus's spike commandeers and downregulates ACE2, the enzyme that normally degrades angiotensin II, so unopposed angiotensin II fuels the vasoconstriction, inflammation, and lung damage of severe disease.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Severe COVID is a clotting disease marked by fibrinogen: the inflamed endothelium and high fibrinogen drive immunothrombosis—microclots in the lungs and elsewhere—so anticoagulation became part of treating hospitalized patients.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — NK cells are the early antiviral defense against COVID: they kill infected cells before adaptive immunity kicks in, and their exhaustion in severe disease is linked to failure to control the virus and worse outcomes.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — COVID-19's defining danger is silent hypoxia: the virus damages the gas-exchange surface so oxygen falls, sometimes profoundly, before patients feel breathless—why pulse-oximeter monitoring became central to spotting deteriorating disease.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — COVID is not only a lung disease—it hits the gut: ACE2 is abundant on intestinal cells, so the virus infects the bowel, causing diarrhea and prolonged fecal shedding that underpins wastewater surveillance.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — COVID makes blood clot through activated platelets: the infection primes platelets and the endothelium toward thrombosis, driving the strokes, pulmonary emboli and microclots that mark severe disease—why anticoagulation is used.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Chest imaging gauges COVID pneumonia: CT scans read in X-ray photons reveal the hallmark peripheral ground-glass opacities, helping judge how far the lung injury has spread when oxygen levels fall.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Severe COVID can scar the lungs: the diffuse alveolar damage may heal with pulmonary fibrosis, leaving survivors with lasting breathlessness and reduced lung function long after the infection clears.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — COVID derails iron handling: ferritin soars as a marker of the hyperinflammatory state, while iron gets locked away from the blood, contributing to the anemia of inflammation in prolonged illness.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy gave COVID its face: the beam revealed SARS-CoV-2 as a sphere ringed by club-shaped spikes — the 'corona' that names the family — and showed the virions budding inside infected airway cells.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — COVID writes itself on the skin: chilblain-like 'COVID toes,' along with hive-like and measles-like rashes, reflect the small-vessel inflammation and clotting the infection provokes far from the lungs.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D drew intense scrutiny in COVID: deficiency was repeatedly tied to more severe disease, plausible given the vitamin's role in tempering the immune response, though supplementation trials gave mixed results.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — COVID reaches the nervous system: the sudden loss of smell points to damage around olfactory neurons, while brain fog, lingering cognitive complaints, and rare Guillain-Barré mark its broader, sometimes lasting, neural toll.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver often registers the infection: mildly raised transaminases are common in COVID, from direct injury, the cytokine storm, and the drugs used to treat it, usually settling as the patient recovers.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — COVID can disturb blood sugar: SARS-CoV-2 infects the ACE2-bearing islet cells, and new-onset hyperglycemia and diabetes appearing during or after infection suggest the virus can injure the insulin-making pancreas.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies are the immune memory of COVID: neutralizing antibodies against the spike, raised by infection or vaccine, block ACE2 binding, while serology dates past exposure and the monoclonal antibodies that once treated it were outrun by escape variants.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy raises the stakes: COVID is more severe in pregnant women and increases preterm birth and stillbirth, while the virus also transiently lowers sperm quality through ACE2-bearing testicular cells — reasons vaccination is urged.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T cells both fight and falter in COVID: severe disease brings a striking lymphopenia as T helper cells are depleted and exhausted, even as the T-cell response is central to clearing the virus and to lasting vaccine immunity.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — COVID reaches the heart muscle: the virus and the inflammation it ignites injure cardiomyocytes, causing a troponin rise, myocarditis and arrhythmias in acute illness and lingering palpitations and chest pain in long COVID.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The virus trips an inflammatory alarm: SARS-CoV-2 activates the NLRP3 inflammasome in macrophages to release IL-1β, a key spark of the cytokine storm that drives severe COVID and a target of anti-inflammatory therapy.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — COVID can inflame the thyroid: subacute (de Quervain) thyroiditis is a recognized sequela, transiently disturbing thyroid function weeks after the infection through immune-mediated gland injury.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Disabling ACE2 may unleash a 'bradykinin storm': because ACE2 normally degrades bradykinin, the virus's hijacking of the receptor lets this vasodilator build up, a proposed driver of the vascular leak and fluid-filled lungs of severe COVID.
- `connects-to` → **[Guillain-Barré Syndrome](../../05-tissue/guillain-barre/README.md)** — It can misdirect the immune attack onto nerves: COVID is among the infections that trigger Guillain-Barré syndrome, an autoimmune assault on peripheral nerve myelin causing ascending weakness in the weeks after illness.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Overactive mast cells may fuel the worst of it: mast cell activation contributes to the cytokine surge of severe disease and is a leading suspect in the lingering, multi-system symptoms of long COVID.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB ignites the cytokine storm: SARS-CoV-2 sensing in airway and immune cells drives NF-κB to pour out IL-6, TNF and other mediators, the transcriptional engine behind the hyperinflammation of severe COVID.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 amplifies the inflammatory loop: the flood of IL-6 in severe COVID activates STAT3, sustaining the feed-forward cytokine signaling that the IL-6 blocker tocilizumab targets in critically ill patients.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Severe disease behaves like viral sepsis: critical COVID produces the dysregulated host response, shock and multiorgan failure of sepsis, and bacterial superinfection of the damaged lungs can layer true bacterial sepsis on top.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — It opens the lung to the mold: damaged airway epithelium plus the steroids and immune dysregulation of severe COVID give rise to COVID-associated pulmonary aspergillosis (CAPA), a dangerous superinfection in the ICU.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The kidney is a frequent casualty: COVID causes acute kidney injury through direct ACE2-mediated infection, cytokine injury and microthrombi, and severe AKI can fail to fully recover, leaving chronic kidney disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Its long tail reaches the mind: post-COVID and long-COVID syndromes carry high rates of depression, from the neuroinflammatory effects of the virus and the psychological toll of severe illness and prolonged recovery.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — It can inflame and weaken the heart: SARS-CoV-2 causes myocarditis and direct cardiac injury, and severe COVID's hypoxia and cytokine storm strain the myocardium, leaving some patients with new heart failure.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Lung and clot damage can pressurize the pulmonary arteries: severe COVID's diffuse lung injury, fibrosis and pulmonary emboli can raise pulmonary vascular resistance, leaving chronic thromboembolic or post-inflammatory pulmonary hypertension.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Critical illness leaves psychological scars: survivors of severe COVID, especially ICU and ventilator patients, develop post-traumatic stress as part of the post-intensive-care and long-COVID burden.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It dysregulates immunity in both directions: severe COVID drives a hyperinflammatory cytokine surge yet also causes lymphopenia, and in children the post-infectious MIS-C is a striking immune complication.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — The virus reaches the nervous system: COVID causes anosmia, encephalopathy and the brain fog of long COVID, and is linked to Guillain-Barré syndrome and a raised stroke risk.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Both infection and pandemic breed worry: long-COVID symptoms, the dread of severe illness and the upheaval of the pandemic fuelled a marked rise in anxiety alongside the depression and PTSD it left.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It strikes the heart directly: COVID-19 can cause acute myocarditis, arrhythmias and a raised risk of myocardial infarction, with troponin rises marking myocardial injury in severe disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It enters and irritates the gut: ACE2 on intestinal and liver cells lets SARS-CoV-2 cause diarrhoea and nausea and raise transaminases, sometimes as the presenting features of COVID-19.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It leaves marks on the skin: chilblain-like 'COVID toes', maculopapular eruptions and urticaria are recognised cutaneous signs, sometimes appearing when respiratory symptoms are mild.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It depletes the lymphocytes: lymphopenia is a hallmark laboratory finding and prognostic marker in COVID-19, reflecting the immune dysregulation of severe disease.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It can shut down the kidney: severe COVID-19 causes acute kidney injury, and a collapsing glomerulopathy occurs in people carrying high-risk APOL1 variants.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It unsettles glucose and the thyroid: COVID-19 can precipitate new-onset hyperglycaemia and diabetes, and subacute thyroiditis can follow the infection.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — It aches and wastes muscle: COVID-19 causes prominent myalgia and, in severe or prolonged illness, myositis, rhabdomyolysis and the deconditioning of long COVID.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Immunomodulators tame severe disease: the IL-6 inhibitor tocilizumab and the JAK inhibitor baricitinib reduce mortality in severe COVID-19 by dampening the hyperinflammatory response.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Bacteria complicate the viral pneumonia: secondary bacterial infection, including pneumococcal pneumonia, worsens severe COVID-19, as it does in influenza.
- `connects-to` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — It is a thrombotic disease: severe COVID-19 drives venous thromboembolism and microthrombi, so hospitalised patients receive prophylactic anticoagulation, and the coagulopathy is a central reason for its high mortality.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It injures the heart muscle: COVID-19 causes myocarditis and troponin-positive cardiac injury through direct infection and cytokine storm, with arrhythmia and heart failure — and rare myocarditis also follows mRNA vaccination.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It is an endothelial disease: SARS-CoV-2 infects and inflames the vascular endothelium, and this endotheliitis of the arterial wall underlies the microthrombi, strokes and multi-organ ischaemia of severe COVID-19.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — It injures the kidney's filter: COVID-19 causes acute kidney injury and a collapsing glomerulopathy (especially with APOL1 risk variants), with ACE2 expression making the glomerulus a target of SARS-CoV-2.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Long COVID overlaps chronic-fatigue syndromes: persistent post-COVID fatigue, widespread pain and autonomic dysfunction overlap heavily with fibromyalgia and ME/CFS, a post-viral chronic-symptom state.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — It can precipitate diabetes: COVID-19 raises the risk of new-onset diabetes, both stress-driven type 2 and autoimmune-pattern type 1, with ACE2 on pancreatic islets implicated in beta-cell injury.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Disrupted germinal centres: severe COVID-19 can ablate lymph-node germinal centres, blunting durable antibody maturation, whereas mRNA vaccines instead drive robust, long-lived germinal-centre responses.
- `connects-to` → **[Obesity](../obesity/README.md)** — A leading severity risk: obesity was among the strongest predictors of severe COVID-19, through impaired ventilation, a pro-inflammatory adipose milieu and underlying endothelial dysfunction.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Marrow under strain: severe COVID-19 drives profound lymphopenia and emergency myelopoiesis, releasing immature, dysfunctional neutrophils from the bone marrow that amplify the inflammatory response.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Accelerated vascular disease: endothelial injury and systemic inflammation from COVID-19 destabilise atherosclerotic plaque, raising heart-attack and stroke risk for months after even mild infection.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — A distinct coagulopathy: severe COVID-19 produces a hypercoagulable state with high D-dimer and fibrinogen and widespread microthrombi that, in the sickest patients, tips into disseminated intravascular coagulation.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — A pandemic syndemic: COVID-19 disrupted tuberculosis programmes worldwide and reversed years of progress, and the two respiratory infections can coexist and worsen each other's course.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement-driven injury: complement activation, especially C5a, drives the endothelial damage and microthrombosis of severe COVID-19, prompting trials of anti-complement therapy.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammasome cytokine: IL-1β from inflammasome activation fuels the hyperinflammation of severe COVID-19, the target of IL-1 blockade such as anakinra.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Cytokine storm component: TNF-α contributes to the systemic cytokine storm of severe COVID-19, alongside IL-6 in driving its hyperinflammatory state.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Antiviral and immunopathic: IFN-γ from T and NK cells helps clear SARS-CoV-2 but, when dysregulated, drives the macrophage activation and hyperinflammation of severe COVID-19.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes into the infected lung in COVID-19, where they fuel the alveolar inflammation and damage of severe disease.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic amplification: the profound hypoxia of COVID-19 pneumonia stabilises HIF-1α, which further amplifies inflammation and the prothrombotic state in a vicious cycle.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The hyperinflammatory cytokines of severe COVID-19 signal through JAK-STAT, the rationale for baricitinib—a JAK1/2 inhibitor that reduces mortality in hospitalized patients, validating cytokine-signaling blockade in the disease.
- `connects-to` → **[von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — SARS-CoV-2 injury to the endothelium releases ultra-large von Willebrand factor multimers, driving the platelet-rich microthrombosis that underlies the characteristic COVID-19 coagulopathy and elevated thrombotic risk.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — The SARS-CoV-2 spike protein can engage TLR4 on innate immune cells, triggering the NF-κB-driven cytokine output that contributes to the hyperinflammation distinguishing severe COVID-19 from mild infection.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Dexamethasone acting through the glucocorticoid receptor was the first treatment shown to cut mortality in severe COVID-19, broadly suppressing the NF-κB-driven cytokine program that injures the lungs in the hyperinflammatory phase.
- `connects-to` → **[RIG-I](../../03-molecular/rig-i/README.md)** — The cytosolic sensor RIG-I detects SARS-CoV-2 RNA to trigger the type-I-interferon response, and the virus's active antagonism of this pathway explains the blunted, delayed interferon that permits early uncontrolled replication.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Endothelial injury and neutrophil activation in severe COVID-19 drive excess thrombin generation, producing the pulmonary microthrombi and venous thromboembolism that are a major cause of death and the rationale for anticoagulation.
- `connects-to` → **[MAVS](../../03-molecular/mavs/README.md)** — SARS-CoV-2 proteins antagonize RIG-I/MAVS antiviral signaling (RIG-I already mapped) to suppress the early type-I interferon response, an immune-evasion mechanism that contributes to severe, delayed-interferon COVID-19.
- `connects-to` → **[IRF3](../../03-molecular/irf3/README.md)** — Multiple SARS-CoV-2 ORF proteins block IRF3 activation and nuclear translocation, dampening interferon induction so that the dysregulated, delayed interferon response shapes COVID-19 severity.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Platelet factor 4 is central to the platelet activation and immunothrombosis of severe COVID-19, and anti-PF4 antibodies underlie the rare vaccine-induced thrombotic thrombocytopenia (VITT).
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Type-I interferon signals through JAK (mapped) to STAT1 to induce antiviral genes, the program SARS-CoV-2 antagonizes—delayed and then dysregulated IFN-STAT1 signaling drives severe COVID-19.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 (mapped) sensing of spike and DAMPs signals through MyD88 to NF-κB (mapped), amplifying the innate inflammatory response that fuels severe COVID-19.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-2 released from activated endothelium marks the endothelial dysfunction and microvascular thrombosis of severe COVID-19, correlating with disease severity.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation at C3 (feeding the C5 axis already mapped) amplifies the thromboinflammation and endothelial injury of severe COVID-19.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING sensing of cytosolic and mitochondrial DNA released during severe SARS-CoV-2 infection amplifies the type-I-interferon and inflammatory response (already mapped) contributing to immunopathology.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD8 cytotoxic T cells and NK cells deploy perforin against infected cells in COVID-19, an antiviral effector arm whose dysregulation accompanies the lymphopenia of severe disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the macrophage-driven cytokine storm and NET-associated thromboinflammation of severe COVID-19.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling drives the post-COVID pulmonary fibrosis that follows the diffuse alveolar damage of severe COVID-19.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling in endothelium shapes the vascular dysfunction and procoagulant phenotype underlying the thrombotic complications of COVID-19.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Calprotectin (S100A8/A9) released by emergency myelopoiesis-derived neutrophils is a key driver and severity biomarker of the hyperinflammatory cytokine storm in severe COVID-19.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates lymphocyte homeostasis and oxidative-stress handling, processes whose dysregulation accompanies the lymphopenia and immune dysfunction of severe COVID-19.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of pattern-recognition and cytokine receptors amplifies the macrophage inflammatory response that fuels severe COVID-19.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling drives the metabolic reprogramming of the hyperinflammatory immune cells and is a therapeutic target in severe COVID-19.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven cytokine storm and the platelet activation of COVID-19 coagulopathy.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA) signaling participates in the immune-cell activation and endothelial dysfunction of severe COVID-19.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the immune-cell metabolism of the hyperinflammatory response to SARS-CoV-2.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — SARS-CoV-2 modulates host autophagy to support its replication, and autophagy shapes the innate immune response to COVID-19.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the endothelial and platelet activation of COVID-19 coagulopathy.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the hyperinflammation and lung immunopathology of COVID-19.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the immune responses to SARS-CoV-2 in COVID-19.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the immune-cell trafficking and vascular responses of COVID-19.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the lung inflammation and cytokine storm of COVID-19 disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the inflammatory and immunopathologic response of COVID-19 disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host immune response of COVID-19 disease.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Neutralising immunity: protective and vaccine-induced immunity to SARS-CoV-2 is carried largely by neutralising IgG against the spike protein (already mapped), and monoclonal IgG antibodies were an early therapeutic before variant escape blunted them.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac injury: myocardial injury marked by troponin elevation is common in severe COVID-19 and independently predicts mortality, reflecting myocarditis, microthrombosis and demand ischaemia from the systemic illness.
- `connects-to` → **[Surfactant](../../03-molecular/surfactant/README.md)** — Alveolar injury: SARS-CoV-2 infects and kills the type II pneumocytes that produce surfactant, and the resulting surfactant deficiency contributes to the alveolar collapse and ARDS of severe COVID-19 pneumonia.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Mucosal immunity: secretory IgA on the nasal and airway mucosa is a first line of defence against SARS-CoV-2 and a correlate of protection, motivating the intranasal vaccines designed to raise mucosal immunity at the site of entry.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Antigen presentation and vaccines: MHC class II presentation of viral antigens drives the CD4 T-cell help underlying antibody responses to SARS-CoV-2 infection and vaccination, and HLA variation influences the severity of COVID-19.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell response: IL-2-driven T-cell expansion generates the SARS-CoV-2-specific T cells that clear the virus (perforin already mapped) and provide durable protection, while the lymphopenia of severe disease reflects failure of this response.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial dysfunction: SARS-CoV-2 injury to the endothelium (already mapped) reduces protective nitric oxide, contributing to the vasoconstriction and microthrombosis of COVID-19, and inhaled nitric oxide has been trialled for the hypoxaemia.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Vascular permeability: VEGF released in the inflamed COVID-19 lung raises vascular permeability, worsening the pulmonary oedema of acute respiratory distress syndrome (angiopoietin already mapped) that impairs gas exchange.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune counter-regulation: IL-10 rises as a counter-regulatory response to the hyperinflammation of severe COVID-19 (IL-6 and IL-1 already mapped), and the balance between pro- and anti-inflammatory signals shapes whether the cytokine storm resolves.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Eicosanoid inflammation: prostaglandins from the COX pathway (IL-6 and IL-1 already mapped) amplify the inflammation of COVID-19, and thromboxane on the activated platelets (PF4 already mapped) contributes to the immunothrombosis.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — RAAS dysregulation: SARS-CoV-2 downregulates ACE2 (already mapped), the enzyme that degrades angiotensin II (already mapped), shifting the renin-angiotensin balance toward vasoconstriction and inflammation in severe COVID-19.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and antiviral immunity: zinc supports antiviral immunity and inhibits coronavirus replication in vitro, and the anosmia and dysgeusia of COVID-19 have been linked to disturbed zinc-dependent taste and smell signalling.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Hyperferritinaemia: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) and drives the hyperferritinaemia that is a marker of the hyperinflammation and severity of COVID-19.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium and antiviral status: the antioxidant selenoprotein status of selenium supports antiviral immunity, and low selenium has been linked to worse COVID-19 outcomes in observational studies.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity risk: the adipokine leptin links obesity — a major risk factor for severe COVID-19 — to the metabolic-inflammatory state and impaired immunity behind the poor outcomes.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is the adipose-derived adipokine of the obesity risk and the metabolic-inflammatory state of severe COVID-19.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the obesity risk and the cytokine milieu (IL-6 already mapped) of severe COVID-19.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 imbalance: IL-4 and the type-2/Th2 arm; the dysregulated type-1/type-2 balance is part of the immune dysregulation of severe COVID-19.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — Causative virus: COVID-19 is caused by SARS-CoV-2, whose spike (already mapped) engages the ACE2 (already mapped) receptor for cell entry, the coronavirus of the pandemic.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 antiviral arm: IL-12 polarises the Th1 (IFN-γ already mapped) antiviral response, part of the type-1 immunity against SARS-CoV-2 in COVID-19.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 imbalance: IL-13, with IL-4 (already mapped), completes the type-2/Th2 arm of the dysregulated type-1/type-2 balance of severe COVID-19.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2/eosinophil arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension whose blood eosinopenia is a marker of severe COVID-19.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the dysregulated inflammation of severe COVID-19.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the dysregulated type-1/type-2 balance of COVID-19.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — Causative virus: SARS-CoV-2, entering via the ACE2 (already mapped) receptor through its spike (already mapped), is the causative agent of COVID-19.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells: the pDCs are the major producers of the type-I interferon (already mapped), whose impaired or delayed response is a determinant of the severity of COVID-19.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment and the complement-mediated thromboinflammation of severe COVID-19.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation drives the complement-mediated thromboinflammation of severe COVID-19.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin regulation: the C1-esterase inhibitor regulates both the lectin/classical complement and the contact-kinin (bradykinin already mapped) systems whose dysregulation is implicated in the vascular leak and thromboinflammation of severe COVID-19.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Hypoferraemia: transferrin, the iron carrier, reflects the marked hypoferraemia and disordered iron handling (hepcidin already mapped) of the acute-phase response of severe COVID-19.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Airway epithelial alarmin: TSLP released from the SARS-CoV-2 (already mapped)-infected airway epithelium (alveolus already mapped) and bronchial epithelium activates mast cells (already mapped) and pDCs (dendritic-cell already mapped), amplifying the type-2 hypersensitivity and cytokine storm of severe COVID-19.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Hypoxia-driven EPO: erythropoietin, induced by the severe hypoxia (oxygen already mapped) of COVID-19 ARDS via HIF-1α (already mapped), supports erythropoiesis and tissue-protective signalling; EPO may also modulate the pulmonary-artery vascular remodelling of long-COVID PAH (already mapped).
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell histamine storm: histamine, released by the mast cells (already mapped) activated by the SARS-CoV-2 (already mapped) spike protein, amplifies the vascular permeability, bronchoconstriction and the inflammatory cytokine (IL-6 already mapped) storm of severe COVID-19.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM/fibrosis alarmin: periostin, induced by IL-4 and IL-13 (already mapped) in the post-COVID pulmonary fibrosis (fibroblast already mapped), promotes type-2 ECM remodelling of the alveoli (already mapped) and contributes to the long-COVID fibrotic lung complication.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian antioxidant: melatonin scavenges mitochondrial ROS (already mapped) and modulates the cytokine storm (IL-6 already mapped) of severe COVID-19; disrupted circadian rhythms worsen disease severity and melatonin deficiency is observed in critically ill patients.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine coupling: prolactin, elevated during the acute-phase response of severe COVID-19, potentiates macrophage (already mapped) and lymphocyte activation, contributing to the cytokine storm (IL-6 already mapped) and the hyperinflammatory state.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — COVID testosterone: androgen receptor signalling upregulates ACE2 (already mapped) in the lung (already mapped), amplifying viral entry; testosterone-driven immunosuppression worsens the male-sex COVID-19 IL-6 (already mapped) driven cytokine storm.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — COVID serotonin: SARS-CoV-2 depletes platelet serotonin via ACE2 (already mapped) mediated enterochromaffin cell damage; serotonin deficiency impairs the endothelial (already mapped) and lung (already mapped) vasoregulation, contributing to the post-COVID dysautonomia phenotype.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — COVID oxytocin: oxytocin reduces SARS-CoV-2 cytokine storm by suppressing IL-6 (already mapped) and TNF-α (already mapped) production; oxytocin also protects the endothelium (already mapped) and lung (already mapped) from COVID-19 thromboinflammatory injury.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — COVID vasopressin: vasopressin (ADH) modulates renal (already mapped) fluid balance in COVID-19 ARDS; AVP-driven V1 receptor activation amplifies pulmonary vascular inflammation and contributes to NF-κB (already mapped) cytokine storm (already mapped) in severe disease.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — COVID iodine: SARS-CoV-2 (already mapped) disrupts thyroid (already mapped) iodine metabolism; iodine deficiency amplifies NF-κB (already mapped) cytokine storm (already mapped) and impairs lung (already mapped) surfactant (already mapped) antioxidant defence via lactoperoxidase.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — COVID sodium: hypernatraemia in severe COVID-19 ARDS activates NF-κB (already mapped) and amplifies IL-6 (already mapped) driven cytokine storm (already mapped); sodium-glucose cotransporter inhibition reduces cardiac (already mapped) and renal (already mapped) complication risk.

## Pathology

**Diffuse alveolar damage (DAD):** Autopsy studies of COVID-19 ARDS show exudative phase DAD: protein-rich edema, hyaline membranes, type I pneumocyte necrosis, fibrin deposition, and reactive type II pneumocyte hyperplasia. Organizing phase: fibroblast proliferation, myofibroblast invasion, progressive fibrosis in some survivors.

**COVID-19-associated coagulopathy:** Elevated D-dimer, fibrinogen, and PT; microvascular fibrin thrombi throughout pulmonary and systemic capillaries (distinctive from DIC); likely driven by endothelialitis, platelet-endothelium interactions, and complement activation. Anticoagulation (prophylactic heparin) is standard for hospitalized COVID-19.

**Myocarditis/pericarditis:** Cardiac complications from direct myocardial ACE2-mediated infection or immune-mediated injury; also seen as rare (1 in 50,000–100,000) complication of mRNA vaccination, predominantly in young males, mostly mild and self-limited.

**COVID-19 and special populations:**
- Pregnancy: Higher risk of preterm birth, ICU admission, preeclampsia; vaccine strongly recommended
- Immunocompromised: Prolonged infection, viral evolution to immune-escape variants; chronic infection documented in hematology/oncology patients

[^guan-2020-china-cohort]: Guan WJ, Ni ZY, Hu Y, et al. Clinical Characteristics of Coronavirus Disease 2019 in China. *N Engl J Med.* 2020;382(18):1708-1720. [doi:10.1056/NEJMoa2002032](https://doi.org/10.1056/NEJMoa2002032) · [PubMed 32109013](https://pubmed.ncbi.nlm.nih.gov/32109013/)
[^hoffmann-2020-ace2-entry]: Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2. *Cell.* 2020;181(2):271-280. [doi:10.1016/j.cell.2020.02.052](https://doi.org/10.1016/j.cell.2020.02.052) · [PubMed 32142651](https://pubmed.ncbi.nlm.nih.gov/32142651/)
[^polack-2020-bnt162b2]: Polack FP, Thomas SJ, Kitchin N, et al. Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine. *N Engl J Med.* 2020;383(27):2603-2615. [doi:10.1056/NEJMoa2034577](https://doi.org/10.1056/NEJMoa2034577) · [PubMed 33301246](https://pubmed.ncbi.nlm.nih.gov/33301246/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
