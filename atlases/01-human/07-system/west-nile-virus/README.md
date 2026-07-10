---
schema: human-scale-entry/v1
id: west-nile-virus
name: West Nile Virus
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Flavivirus (Culex mosquito vector); 1937 Uganda origin, 1999 North American invasion; 80% asymptomatic infection; neuroinvasive disease (meningitis, encephalitis, paralysis) in elderly/immunocompromised; NS3/NS5 proteins block IFN signaling; no approved antiviral/vaccine."
aliases: ["WNV", "West Nile virus", "West Nile fever", "West Nile encephalitis", "West Nile neuroinvasive disease", "WNND", "West Nile meningitis", "West Nile paralysis", "Culex WNV", "flavivirus encephalitis"]
sources:
  - id: petersen-2013-wnv-review
    type: peer-reviewed
    cite: "Petersen LR, Brault AC, Nasci RS. West Nile virus: review of the literature. JAMA. 2013;310(3):308-315."
    doi: "10.1001/jama.2013.8042"
    pmid: "23860989"
    url: "https://doi.org/10.1001/jama.2013.8042"
    accessed: "2026-06-08"
  - id: colpitts-2012-wnv-biology
    type: peer-reviewed
    cite: "Colpitts TM, Conway MJ, Montgomery RR, Fikrig E. West Nile Virus: Biology, Transmission, and Human Infection. Clin Microbiol Rev. 2012;25(4):635-648."
    doi: "10.1128/CMR.00045-12"
    pmid: "23034323"
    url: "https://doi.org/10.1128/CMR.00045-12"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "WNV NS3-NS4A complex inhibits RIG-I signaling and disrupts MAVS; NS5-mediated RNA capping (7-methylguanosine) prevents 5′ppp recognition by RIG-I → MAVS not engaged; combined NS3/NS5 strategy suppresses MAVS-TBK1-IRF3 axis enabling WNV establishment."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "WNV NS5 blocks STAT1 by: (1) preventing Tyr701 phosphorylation → ISGF3 cannot form; (2) K48-ubiquitination of STAT1 → proteasomal degradation; NS5-mediated STAT1 antagonism enables WNV to evade ISG-based antiviral defense after IFN-β induction."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "WNV NS5 methyltransferase caps viral RNA with 7-methylguanosine → RIG-I CTD cannot recognize 5′ppp → MAVS not activated; NS3-NS4A helicase also directly inhibits RIG-I signaling; RNA capping mimics host mRNA modification to evade cytosolic innate immunity."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "WNV and DENV share Aedes aegypti + Culex vectors, flavivirus structure, and flaviviral biology; anti-DENV antibodies cross-react with WNV but provide variable protection; WNV neuroinvasive disease has no DENV equivalent; both evade STAT1 via NS5."
  - target: 01-human/07-system/zika-virus
    relation: connects-to
    note: "WNV and ZIKV are neurotropic flaviviruses with serological cross-reactivity; prior WNV immunity may partially protect against ZIKV and vice versa; unlike ZIKV, WNV lacks sexual transmission and does not cause congenital brain malformations; both NS5 proteins evade STAT1."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "About 1 in 150 symptomatic West Nile infections becomes neuroinvasive disease — the leading cause of viral encephalitis in North America — as meningitis, encephalitis with Parkinsonian signs, or poliomyelitis-like flaccid paralysis; the elderly are most at risk."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "West Nile virus is neurotropic, replicating in neurons after crossing the blood-brain barrier; its tropism for anterior-horn motor neurons produces an asymmetric flaccid paralysis resembling polio, while hippocampal infection drives encephalitis."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Once West Nile virus reaches the CNS, microglia and astrocytes mount the neuroinflammatory response that limits viral spread but also contributes to encephalitic injury; CCR5-dependent leukocyte recruitment is protective, and CCR5Δ32 homozygotes fare worse."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "West Nile virus and NMOSD can both cause acute myelitis and optic involvement but differ in mechanism: WNV is a neurotropic flavivirus infecting neurons → flaccid paralysis and encephalitis, while NMOSD is autoimmune AQP4-IgG astrocyte injury; AQP4-IgG and CSF tell them apart."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8+ cytotoxic T cells are essential to clear West Nile virus from infected neurons: they enter the CNS and kill virus-laden cells via perforin/granzyme and Fas, controlling infection but also adding immunopathology; deficient CD8 responses predict severe neuroinvasive disease."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes shape West Nile CNS disease: WNV infects them, and their cytokine output (CXCL10, IL-6) both recruits protective leukocytes and helps open the blood-brain barrier that lets virus and immune cells in; astrocyte responses balance viral control against injury."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "West Nile virus first replicates in skin and lymphoid macrophages and dendritic cells: after a mosquito bite the flavivirus amplifies in these cells, then a viremia can breach the blood-brain barrier—so the innate cells that should contain it help ferry it to the CNS."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Immunosuppression is the key risk for neuroinvasive West Nile disease: in HIV/AIDS, transplant recipients, and the elderly, weak T-cell immunity lets the virus reach the brain, causing encephalitis and flaccid paralysis—so severe WNV is mostly in the immunocompromised."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells are West Nile virus's first targets and gatekeepers: skin Langerhans cells take up the virus at the bite site and carry it to lymph nodes, and their type-I-interferon response largely determines whether infection stays mild or becomes neuroinvasive."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "West Nile virus can cause acute flaccid paralysis resembling Guillain-Barré: the neuroinvasive form attacks anterior-horn motor neurons, producing asymmetric weakness, and rarely a GBS-like demyelinating syndrome—so new flaccid paralysis in summer warrants WNV testing."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help control West Nile virus early: NK cells and interferon limit viral spread before adaptive immunity, and the aging immune system's weaker NK/T-cell response is why neuroinvasive WNV strikes mainly older adults."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "West Nile virus and COVID-19 are both viruses with neuro-invasive potential: most infections spare the CNS, but each can cause encephalitis, and both show how systemic viruses breach the blood-brain barrier in vulnerable hosts—age and immunity shaping severity."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon is the front-line defense against West Nile virus: RIG-I/MAVS sensing of viral RNA triggers interferon that restrains spread, and animals or people with weak interferon responses suffer far more severe neuroinvasive disease."
  - target: 02-pathogen/01-viruses/dengue-virus
    relation: connects-to
    note: "West Nile and dengue are related flaviviruses spread by mosquitoes: they share genome structure and immune-evasion tricks, but West Nile is neuroinvasive (encephalitis) while dengue is hemorrhagic—and cross-reacting antibodies complicate flavivirus serology."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "West Nile virus is defined by its assault on the nervous system: in a minority it crosses into the CNS to cause encephalitis, meningitis and a polio-like acute flaccid paralysis from anterior-horn motor neuron loss, leaving lasting neurological deficits."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells and their antibodies decide West Nile outcomes: a brisk IgM response curbs viremia before the virus invades the brain, and detecting WNV IgM in serum or spinal fluid is the main way it is diagnosed—so weak antibody responses predict severe neuroinvasive disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Immune status governs who gets neuroinvasive West Nile: most infections are mild, but the elderly and immunosuppressed—whose defenses let the virus cross into the brain—account for the rare meningitis, encephalitis, and paralysis that make WNV feared."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "West Nile first multiplies in lymphoid tissue like the spleen: after a mosquito bite the virus replicates in skin and is carried to spleen and lymph nodes, seeding the blood—so this peripheral phase precedes and sets up any later invasion of the nervous system."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "West Nile virus can persist in the kidney: the virus has been detected in urine months after infection and is linked to chronic kidney involvement, so the kidney is both a site of viral persistence and a route of possible shedding."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement is essential to surviving West Nile virus: C3 and the complement cascade are needed to control early viremia and prime antibody and T-cell responses, so complement-deficient hosts suffer far more severe neuroinvasive disease."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T-helper cells coordinate the defense against West Nile virus: CD4 cells sustain the antibody response and support the cytotoxic T cells that clear virus from neurons, so weak helper immunity (as with age or HIV) predicts severe neuroinvasive disease."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "West Nile is diagnosed by its antibodies: WNV-specific IgM in blood or spinal fluid signals acute infection while IgG marks past exposure, and antibody is the basis of protection—the reason the horse vaccine works though no human one yet exists."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "West Nile breaches the brain with help from TNF: inflammatory cytokines like TNF-alpha loosen the blood-brain barrier, letting the virus invade the CNS—a double-edged response that both fights the virus and causes the encephalitis."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells temper West Nile's brain damage: by restraining the antiviral attack within the CNS, Tregs limit collateral neuron injury, so the balance between clearing the virus and sparing the brain shapes recovery from neuroinvasive disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "West Nile leaves a fingerprint in the eye: it commonly causes a distinctive chorioretinitis—clusters of spots in a curved, linear pattern—so an eye exam can help diagnose neuroinvasive infection, and the lesions usually heal as the patient recovers."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "West Nile kills neurons through calcium: in encephalitis, infected and overexcited neurons let calcium flood in, triggering the excitotoxic cell death that destroys brain and spinal motor neurons and leaves lasting deficits."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "West Nile can erase synapses: even after the virus clears, activated microglia and complement prune synapses in the brain, a loss now linked to the memory and cognitive problems that linger in survivors."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Neuroinvasive West Nile is mapped by MRI: its photons reveal inflammation in the thalamus, basal ganglia and brainstem, and the spinal-cord signal behind its polio-like paralysis."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Most West Nile infections show on the skin: West Nile fever brings a blotchy maculopapular rash over the trunk and limbs, the visible face of the far commoner non-neuroinvasive disease."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "West Nile strikes the nervous system broadly: beyond the brain it injures peripheral nerves and the anterior-horn motor neurons, causing a polio-like acute flaccid paralysis that can be permanent."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows West Nile as a classic flavivirus: a small icosahedral core wrapped in a lipid envelope, assembling and budding through the membranes of the endoplasmic reticulum inside infected cells."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "West Nile encephalitis often drops the sodium: inflammation of the brain triggers SIADH, the inappropriate water retention that dilutes blood sodium and can worsen the confusion and seizures of severe neuroinvasive disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "West Nile can inflame the heart: myocarditis and arrhythmias are recognized though underappreciated complications, the virus reaching beyond the nervous system to strain the circulation in severe infection."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "West Nile is diagnosed by its antibody: detecting IgM in serum or — pointing to neuroinvasion — in the cerebrospinal fluid is the mainstay test, since the virus itself is fleeting in the blood by the time symptoms appear."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "West Nile rides the blood supply: it is transmissible through transfusion and organ transplant, so blood banks screen donations for it — a hidden route beyond the mosquito that prompted nationwide testing."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "The virus can cross to the fetus: rare intrauterine West Nile transmission through the placenta, and passage through breast milk, are documented, extending its reach from the mosquito bite to mother and child."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its worst form mimics polio: West Nile attacks the spinal cord's anterior horn motor neurons, causing an acute flaccid paralysis with muscle wasting, while even mild infection brings the prominent myalgia of West Nile fever."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Severe infection drops the platelets: West Nile can cause thrombocytopenia through marrow suppression and consumption, a falling count among the markers of the more dangerous, neuroinvasive course."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Rarely the virus inflames the liver: fulminant West Nile hepatitis is an uncommon but described severe presentation, the flavivirus injuring hepatocytes far from its usual target in the nervous system."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The virus breaches the blood-brain barrier through the vessel wall: it infects brain microvascular endothelial cells and, with TNF-driven leakiness, loosens the barrier so the virus and immune cells flood into the brain."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Neuroinvasive disease runs hot with IL-6: the cytokine pours into the inflamed brain and spinal fluid, and high CSF IL-6 tracks with the severity of West Nile encephalitis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Antibody is the key to survival: plasma cells must quickly pour out neutralizing IgM and IgG to clear the virus from the blood before it reaches the brain, which is why antibody-deficient people fare so badly."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "Sensing the virus triggers the interferon defense: West Nile RNA detected through RIG-I/MAVS activates IRF3 to switch on type I interferon, and the virus's NS proteins fight back by blocking this very pathway."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Its brain invasion can leave a seizure focus: West Nile encephalitis inflames the cortex and can cause acute seizures and lasting epilepsy, part of the neurologic legacy that lingers in survivors of the neuroinvasive form."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils play a double game: they are recruited early to fight the infection yet can also serve as a reservoir that ferries the virus, and their breaching of the blood-brain barrier helps the virus reach the brain."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The virus drives the inflammation that opens the brain: West Nile activates NF-κB in infected and immune cells, and the resulting cytokine surge both fights the virus and loosens the blood-brain barrier it exploits to invade."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Paralysis from neuroinvasion brings clot risk: the acute flaccid paralysis and prolonged immobility of severe West Nile disease create venous stasis that raises the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Critical neuroinvasive disease behaves like sepsis: severe West Nile encephalitis can cause respiratory failure and a critical illness in which secondary bacterial infection and sepsis complicate the course."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Its brain invasion can leave movement disorders: West Nile encephalitis targets the basal ganglia and substantia nigra, causing tremor, rigidity and a post-encephalitic parkinsonism that can persist in survivors."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Recovery carries a long mental tail: survivors of neuroinvasive West Nile disease frequently suffer persistent fatigue, cognitive impairment and depression, a post-encephalitic syndrome lasting months to years."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The virus can persist in and injure the kidney: West Nile causes acute kidney injury in severe disease and can shed in urine for years, with reports linking chronic infection to ongoing renal impairment."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its poliomyelitis-like injury leaves lasting pain: neuroinvasive West Nile can destroy anterior-horn motor neurons and inflame nerves, leaving persistent weakness and neuropathic pain long after the acute illness."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Severe neuroinvasion can damage cerebral vessels: West Nile meningoencephalitis can be complicated by vasculitis and hemorrhage, occasionally precipitating stroke in the acute phase."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Surviving neuroinvasive disease can scar the mind: prolonged ICU care and the slow, incomplete recovery from West Nile encephalitis and paralysis can leave post-traumatic stress alongside its cognitive sequelae."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its polio-like paralysis can stop breathing: neuroinvasive West Nile virus attacks anterior horn cells, causing acute flaccid paralysis that can involve the diaphragm and require prolonged mechanical ventilation."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "West Nile fever often shows on the skin: the milder febrile form commonly produces a transient maculopapular or roseolar rash over the trunk and limbs, a recognised clinical clue."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A slow, uncertain recovery breeds worry: the lingering fatigue, weakness and cognitive problems after West Nile neuroinvasive disease foster chronic health anxiety alongside its depression and PTSD."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its febrile phase upsets the gut: West Nile fever commonly causes nausea, vomiting, diarrhoea and abdominal pain, with rare hepatitis and pancreatitis in severe disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Brain infection unbalances sodium: West Nile encephalitis can trigger SIADH with hyponatraemia, a common electrolyte disturbance in central nervous system infections that needs careful fluid management."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Classic West Nile fever swells the nodes: generalized lymphadenopathy was a defining feature of the originally described illness, accompanying the fever and maculopapular rash."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It can inflame the heart: acute West Nile infection occasionally causes myocarditis and arrhythmia, alongside its dominant neuroinvasive disease."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It can pass through blood and birth: West Nile virus is transmitted by transfusion, organ transplant and breast milk, and rare transplacental transmission causes congenital infection."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "It shares a deadly differential: herpes simplex encephalitis is the key alternative cause of viral encephalitis to exclude and empirically treat when West Nile neuroinvasive disease is suspected."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It can persist in and injure the kidney: West Nile virus RNA can be shed in urine and persist in renal tissue for years, and severe infection causes acute kidney injury."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: connects-to
    note: "A neurotropic flavivirus cousin: Zika, like West Nile, is a mosquito-borne flavivirus that crosses into the nervous system and placenta, sharing antibody cross-reactivity that complicates serological diagnosis."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "They loosen the blood-brain barrier: mast-cell activation during West Nile infection releases chymase and vasoactive mediators that increase vascular permeability, helping the virus cross into the brain."
  - target: 02-pathogen/06-environmental/zoonosis
    relation: connects-to
    note: "A bird-and-mosquito zoonosis: West Nile virus cycles between birds and Culex mosquitoes, with humans and horses dead-end hosts infected by the bite — a One Health problem driven by climate and bird migration."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "It paralyses like polio: West Nile virus has a tropism for spinal anterior-horn motor neurons, and the resulting axonal injury causes an acute asymmetric flaccid paralysis indistinguishable from poliomyelitis."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "It scars memory: neuroinvasive West Nile encephalitis injures deep brain structures including the hippocampus, leaving many survivors with lasting memory, cognitive and fatigue problems after the acute illness."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes raises its danger: advanced age, immunosuppression and diabetes are the main risk factors for severe neuroinvasive West Nile disease—encephalitis, meningitis and acute flaccid paralysis—turning a usually mild infection deadly."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "It can linger in the kidney: West Nile virus can persist in renal tissue with prolonged urinary shedding, and is associated with chronic kidney disease and proteinuria in some survivors."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It occasionally inflames the heart: beyond its neuroinvasive disease, West Nile virus is a rare cause of myocarditis, adding cardiac injury to severe infection."
  - target: 01-human/07-system/als
    relation: connects-to
    note: "A polio-like paralysis: West Nile virus can attack anterior-horn motor neurons, causing an acute asymmetric flaccid paralysis that resembles poliomyelitis and, in its motor-neuron targeting, the cells lost in ALS."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Antibody clears the virus: control of West Nile virus depends on neutralizing antibody matured in germinal centres, which is why B-cell-deficient and elderly patients suffer the severe neuroinvasive disease."
  - target: 01-human/07-system/measles
    relation: connects-to
    note: "Viruses that invade the brain: like measles—which causes acute encephalitis and the late, fatal SSPE—West Nile virus crosses into the CNS, the two showing viral neuroinvasion by different routes."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "Flaccid paralysis and demyelination: West Nile virus causes a poliomyelitis-like acute flaccid paralysis from anterior-horn injury and can also trigger a Guillain-Barré/demyelinating neuropathy on the CIDP spectrum."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Vector-borne febrile differential: West Nile virus (Culex-borne) and malaria both present as acute mosquito-transmitted febrile illness, an overlapping differential in travellers and endemic regions."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Respiratory failure from paralysis: severe neuroinvasive West Nile virus can paralyse the diaphragm and respiratory muscles, leading to ventilator dependence and aspiration that injure the alveoli."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Antiviral defence: IFN-γ from T and NK cells is critical for controlling West Nile virus and clearing it from the CNS, with deficiency predisposing to severe neuroinvasive disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammation: IL-1β from activated microglia drives the inflammatory response to West Nile encephalitis, contributing both to viral control and to bystander neuronal injury."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome sensing: the NLRP3 inflammasome detects West Nile virus and matures IL-1β, a double-edged response that restrains the virus yet aggravates CNS inflammation."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "Leukocyte trafficking to the brain: CCR5 directs protective leukocytes into the West Nile-infected CNS, and the CCR5-Δ32 loss-of-function variant markedly raises the risk of symptomatic and fatal neuroinvasive disease."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws inflammatory monocytes across the blood-brain barrier in West Nile encephalitis, aiding viral clearance while contributing to the immunopathology of the infection."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic clearance: CD8 T cells use perforin and granzyme to eliminate West Nile virus from infected neurons, a defence essential for survival that can also injure the neurons it protects."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 induction: IL-12 from activated dendritic cells drives the Th1 and IFN-γ response that controls West Nile virus, biasing immunity toward the cell-mediated clearance the infection requires."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunoregulatory brake: IL-10 tempers the antiviral response in West Nile infection, and excess IL-10 is associated with worse outcomes by blunting the immunity needed to clear the virus from the CNS."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Blood-brain barrier gatekeeping: CXCL12 at the blood-brain barrier retains CXCR4+ leukocytes in the perivascular space, and CXCR4 antagonism improves West Nile outcomes by letting protective T cells enter the brain parenchyma."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate adaptor: MyD88-dependent Toll-like-receptor signalling is essential for controlling West Nile virus, organising leukocyte positioning in the brain, and MyD88-deficient hosts suffer markedly higher viral burden and neuroinvasion."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Antibody protection: neutralising IgG against the viral envelope is the key correlate of protection from West Nile encephalitis, and FcRn recycling sustains the circulating antibody and the half-life of therapeutic monoclonals and immune globulin under study."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "CD4 help: presentation of West Nile antigens on MHC class II primes the CD4 T-cell help needed for durable antibody responses and for supporting the CD8 T cells that clear virus from infected neurons."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Neuronal apoptosis: West Nile virus drives caspase-3-mediated apoptosis of infected neurons, the cell death directly responsible for the encephalitis and the poliomyelitis-like acute flaccid paralysis of neuroinvasive disease."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Protective complement: the complement system (C3 already mapped, through C5) is essential for the protective antibody and T-cell responses that control West Nile virus, shaping both clearance and immunopathology."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Barrier breakdown: cytokine- and VEGF-driven blood-brain-barrier permeability lets West Nile virus and inflammatory cells enter the CNS, a key step enabling its neuroinvasion."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Excitotoxicity: West-Nile-infected neuron death and the inflammatory milieu drive glutamate excitotoxicity, a mechanism of the neuronal injury underlying West Nile encephalitis."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Neuronal apoptosis: the balance of anti-apoptotic BCL-2 against viral- and immune-driven pro-apoptotic signals (caspase-3 mapped) sets neuronal survival in West Nile neuroinvasive disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Survival hijack: West Nile virus manipulates host PI3K-AKT signalling to delay apoptosis early in infection, sustaining the cellular environment for viral replication."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Type-I-interferon signalling through JAK-STAT (STAT1 mapped) is the principal antiviral defence controlling West Nile virus, which the virus actively antagonises."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "West Nile virus modulates mTOR-regulated translation and autophagy to support its replication in infected cells."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling is engaged during West Nile virus entry and replication and contributes to the inflammatory response in neuroinvasive disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 released by activated microglia amplifies the neuroinflammation and blood-brain-barrier disruption of West Nile virus neuroinvasive disease."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory cytokine response that accompanies West Nile virus encephalitis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling modulates the blood-brain-barrier integrity and the balance between protective and pathological responses in West Nile virus neuroinvasion."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic nucleic-acid sensing through cGAS-STING contributes to the innate antiviral and neuroinflammatory response that restrains West Nile virus."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates neuronal survival and oxidative-stress responses during West Nile virus neuroinvasion."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α responses in infected and inflamed CNS tissue shape the blood-brain-barrier disruption of neuroinvasive West Nile virus."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the innate antiviral and neuronal survival signaling relevant to West Nile virus neuroinvasion."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) is exploited by West Nile virus to support its replication and modulate neuronal survival."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the neuroinflammation of West Nile virus encephalitis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "West Nile virus modulates host autophagy to support its replication in neurons and other cells."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the endothelial and blood-brain-barrier responses to West Nile virus neuroinvasion."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling, exploited for the lipid-dependent replication of West Nile virus, participates in the host response."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the host immune response to West Nile virus."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory and immune responses to West Nile virus."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the blood-brain-barrier permeability and neuroinflammation of West Nile virus neuroinvasive disease."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host response to West Nile virus."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation of the antiviral immune response to West Nile virus."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the leukocyte recruitment and neuroinflammatory response to West Nile virus."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Blood-brain-barrier injury: neuroinflammatory nitric oxide contributes to the blood-brain-barrier disruption and neuronal damage of West Nile encephalitis, part of the immunopathology that accompanies viral clearance from the brain."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell control: IL-2-driven expansion of the CD8 T cells that clear West Nile virus from infected neurons (perforin already mapped) is essential to controlling neuroinvasive infection, and waning T-cell immunity underlies severe disease in the elderly."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Acute flaccid paralysis: West Nile virus can infect anterior-horn motor neurons to cause a poliomyelitis-like acute flaccid paralysis, disrupting cholinergic transmission at the neuromuscular junction and leaving lasting weakness."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Antibody help: IL-4 and type-2 T-cell help support the B-cell (already mapped) production of the neutralising antibodies (IgG already mapped) that protect against West Nile virus, the humoral immunity whose failure permits neuroinvasion."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative neuronal injury: reactive oxygen species from xanthine oxidase and other sources contribute to the oxidative stress that damages neurons during West Nile encephalitis, compounding the direct viral and immune-mediated injury."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Myocarditis: West Nile virus can rarely cause myocarditis, and troponin elevation marks the myocardial injury of this cardiac involvement, one of the recognised extraneural manifestations of severe infection."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) and infiltrating cells contribute to the neuroinflammation and fever of West Nile encephalitis (IL-6 and IL-1 already mapped), part of its inflammatory injury."
  - target: 01-human/03-molecular/aquaporin-4
    relation: connects-to
    note: "Blood-brain-barrier and oedema: the astrocyte water channel aquaporin-4 governs brain water balance, and its disturbance in West Nile encephalitis contributes to the blood-brain-barrier disruption and cerebral oedema (glutamate excitotoxicity already mapped)."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 antibody help: IL-13, with IL-4 (already mapped), supports the B-cell (already mapped) neutralising-antibody response that controls West Nile viraemia, the humoral arm balancing the Th1 (IL-12 and interferon-gamma already mapped) response."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium and excitotoxicity: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity that kills infected neurons (already mapped) in West Nile encephalitis, a neuroprotective ion."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and antiviral immunity: zinc supports the interferon (already mapped) antiviral response and inhibits flavivirus replication, and zinc status influences the immunity that determines the outcome of West Nile virus infection."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium antioxidant defence: selenium and its selenoproteins support the antioxidant defence and the antiviral immunity against West Nile virus, and deficiency can worsen the oxidative injury of the neuroinvasive infection."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Blood-brain-barrier permeability: substance P increases the permeability of the blood-brain barrier, facilitating the neuroinvasion of West Nile virus into the brain (already mapped) and the encephalitis."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Regulatory and repair signalling: TGF-β shapes the regulatory (Treg already mapped) and tissue-repair response that resolves the neuroinflammation of West Nile encephalitis, balancing viral control against immunopathology."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "T-cell exhaustion: the PD-1 checkpoint on the cytotoxic T cells (already mapped) can limit the viral clearance in severe or persistent West Nile virus infection, part of the immune regulation of the disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu; the nutritional and metabolic state modulates the age-dependent (the elderly worse) susceptibility to West Nile virus."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of the West Nile virus infection."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the inflammatory (IL-6 and TNF already mapped) response to West Nile virus."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the protective Th1 (IFN-γ and IL-12 already mapped) antiviral response to West Nile virus."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune response to the West Nile virus infection."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune response to the West Nile virus neuroinvasive infection."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) is part of the complement-mediated protection and neuroinflammation of the West Nile virus infection."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "BBB permeability: the bradykinin-kinin system increases the blood-brain-barrier permeability that facilitates the neuroinvasion of the West Nile virus into the brain (already mapped)."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Vascular permeability: the histamine, from the mast cells (already mapped), increases the vascular permeability that enhances the CNS entry of the West Nile virus."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement evasion: the West Nile virus NS1 protein recruits the host factor H to inactivate the C3 convertase (complement C3, C5 and C5aR1 already mapped) and evade the complement attack."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact (bradykinin already mapped) systems whose activation contributes to the vascular permeability and neuroinvasion of the West Nile virus."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Nutritional immunity: transferrin, by sequestering iron, is part of the host nutritional-immunity response to the West Nile virus infection."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Coagulopathy: thrombin, at the interface of the contact (bradykinin already mapped) and coagulation systems, contributes to the microvascular coagulopathy and thromboinflammation of severe West Nile virus infection."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Astrocyte gap junctions: connexin43, the astrocyte (already mapped) gap-junction protein, is disrupted during the West Nile virus neuroinvasion, compromising the blood-brain-barrier integrity and glial coupling."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Reactive gliosis: periostin, a matricellular mediator, is part of the tissue-remodelling and reactive-gliosis response of the CNS to the West Nile virus encephalitis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuro-epithelial alarmin: TSLP, released from the skin (already mapped) and mucosal barriers at the site of mosquito inoculation and during viraemia, activates mast cells (already mapped) and dendritic cells (already mapped), shaping the early innate response to West Nile virus."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective signal: erythropoietin, acting via EPOR on neurons (already mapped) and astrocytes (already mapped), attenuates the oxidative and neuroinflammatory damage of the West Nile virus encephalitis and promotes neuronal survival."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Antiviral chronobiotic: melatonin, via MT1/MT2 receptors on macrophages (already mapped) and NK cells (already mapped), inhibits NLRP3 inflammasome (already mapped) activation and reduces the neuroinflammatory cytokine storm of West Nile virus encephalitis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine antiviral modulator: prolactin, acting via PRLR on macrophages (already mapped), NK cells (already mapped) and T cells (already mapped), promotes innate antiviral effector responses and modulates the neuroinflammatory milieu of West Nile virus encephalitis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Neuroimmune neuroprotection: oxytocin, via oxytocin receptors on microglia (already mapped) and astrocytes (already mapped), suppresses the pro-inflammatory cytokine (TNF-α and IL-6 already mapped) cascade and the BBB-disrupting neuroinflammation of West Nile virus encephalitis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen sex-differential severity: testosterone, via androgen receptors on microglia (already mapped) and astrocytes (already mapped), modulates the neuroinflammatory response and contributes to the greater severity and higher mortality of WNV encephalitis in males vs. females."
---

# West Nile Virus

## Overview

**West Nile virus (WNV)** is a positive-sense single-stranded RNA virus of the family *Flaviviridae* (genus *Flavivirus*), transmitted in an enzootic bird–mosquito cycle and incidentally infecting humans via the bite of infected *Culex* mosquitoes, primarily *Culex pipiens* and *Culex quinquefasciatus*. First isolated from a febrile patient in the West Nile Province of Uganda in 1947, WNV circulated primarily in Africa, the Middle East, and South Asia for decades before causing explosive outbreaks in Romania (1996) and then **invading North America in 1999** — appearing suddenly in New York City and spreading to all contiguous US states within 4 years, becoming the leading cause of domestically acquired viral encephalitis in North America [^petersen-2013-wnv-review].

WNV infection follows a stark **80/20 rule**: ~80% of infections are completely asymptomatic, ~20% cause **West Nile fever** (a self-limited febrile illness), and ~1 in 150 symptomatic infections progresses to **West Nile neuroinvasive disease (WNND)** — encompassing meningitis, encephalitis, and an acute flaccid paralysis (AFP) syndrome resembling poliomyelitis. The elderly and immunocompromised are disproportionately affected by WNND, with case-fatality rates of 3–15% in hospitalized patients [^colpitts-2012-wnv-biology].

**Clinical significance:** WNV has caused over 25,000 neuroinvasive disease cases and ~2,500 deaths in the United States since 1999. There is no approved antiviral therapy or human vaccine. WNV serves as a model for understanding neurotropic flavivirus pathogenesis, BBB breach mechanisms, and innate immune evasion via RNA capping.

## Structure

### WNV biology

WNV is an enveloped icosahedral virus (~50 nm) with an **~11 kb positive-sense ssRNA genome** encoding a single polyprotein processed into three structural and seven non-structural proteins:

| Protein | Function |
|---------|----------|
| C (capsid) | Nucleocapsid assembly; interacts with genomic RNA |
| prM/M | Precursor membrane protein; furin-cleaved during maturation; protects E during assembly |
| E (envelope) | Receptor binding (TIM-1/HAVCR1, integrins, heparan sulfate); membrane fusion at endosomal pH 5–6; target of neutralizing antibodies |
| NS1 | Secreted hexamer; evades complement via C4b-binding protein; used as serologic diagnostic marker; endothelial activation |
| NS2A/2B | NS2A: replication complex; NS2B: NS3 serine protease cofactor |
| NS3 | Serine protease (with NS2B) + RNA helicase; cleaves viral polyprotein; inhibits RIG-I/MAVS signaling |
| NS4A/4B | Membrane rearrangement; replication organelles; NS4A blocks JAK-STAT signaling |
| NS5 | RNA-dependent RNA polymerase + **methyltransferase** (caps viral RNA → evades RIG-I); **blocks STAT1** → IFN evasion |

### WNV lineages

WNV is classified into at least 8 lineages:
- **Lineage 1 clade 1a**: Responsible for most human disease globally including North America (NY99 strain) and European outbreaks; highest neurovirulence
- **Lineage 2**: Historically sub-Saharan Africa; caused 2010–2012 European outbreaks (Hungary, Greece)
- **Lineage 1 clade 1b (Kunjin)**: Australia; lower neurovirulence than lineage 1a

The **NY99 strain** that entered North America in 1999 is closely related to a 1998 Israeli isolate, suggesting a Middle Eastern origin.

## Function

### Viral life cycle

1. **Mosquito-to-host transmission**: *Culex* mosquito takes a blood meal from infected amplifying host (corvids — crows, blue jays — are highly susceptible) → injects WNV in saliva → skin DCs and Langerhans cells infected at inoculation site
2. **Initial replication**: Local replication in skin, draining lymph nodes → primary viremia (Days 1–4)
3. **Systemic dissemination**: Viremia seeds spleen, liver, kidney; amplified in monocytes/macrophages; peak viremia Day 3–7
4. **Neuroinvasion** (minority of cases): WNV crosses BBB via: (a) direct transcytosis through endothelial cells; (b) Trojan horse — infected monocytes traverse BBB; (c) axonal retrograde transport from peripheral nerve terminals; (d) MMP-mediated BBB disruption
5. **CNS infection**: Replication in neurons (especially anterior horn motor neurons, Purkinje cells, hippocampal neurons), astrocytes, and microglia

### Immune evasion

WNV has evolved a multilayered strategy to evade innate immunity:

| Mechanism | Molecular detail |
|-----------|-----------------|
| RNA capping | NS5 methyltransferase adds 7-methylguanosine 5′-cap → viral RNA resembles host mRNA → RIG-I CTD cannot detect 5′ppp → MAVS not activated |
| RIG-I/MDA5 inhibition | NS3-NS4A complex directly disrupts RIG-I signaling |
| STAT1 blockade | NS5 prevents STAT1 Tyr701 phosphorylation and targets STAT1 for K48-ubiquitination → proteasomal degradation → ISGF3 cannot form → ISGs not induced |
| Complement evasion | NS1 binds C4b-binding protein → prevents C3 amplification; inhibits classical complement cascade |
| IFN-β blockade | NS4A/NS4B block TBK1 → IRF3 not fully activated; additive with NS3-NS4A upstream block |

### Innate and adaptive immune response

| Phase | Response |
|-------|---------|
| Hours 0–12 | Skin DC sensing; low-level IFN-β despite NS5 evasion |
| Days 1–3 | NK cell activation; complement-mediated lysis of WNV-infected cells |
| Days 3–7 | WNV-specific CD8+ T cells (E protein peptides dominant); CD4+ Tfh |
| Days 7–14 | Neutralizing IgM (anti-E protein); most infections cleared |
| >14 days | IgG seroconversion; long-lived B cell memory; durable protection from reinfection |

## Pathology

### West Nile fever

**Epidemiology:** ~20% of WNV-infected individuals; incubation 3–14 days.

**Clinical:** Abrupt fever (38–40°C), headache, myalgias, arthralgias, fatigue; **maculopapular rash** (truncal, non-pruritic) in ~50%; lymphadenopathy; gastrointestinal symptoms (nausea, diarrhea) in ~30%. Duration 3–7 days; full recovery typically within weeks but fatigue and cognitive symptoms can persist months.

**Laboratory:** Lymphocytopenia, mild thrombocytopenia, elevated transaminases; WNV IgM in serum/CSF from Day 4–8.

### West Nile neuroinvasive disease (WNND)

**Risk factors:** Age ≥60 years (30-fold higher WNND risk vs. age <20), immunosuppression (transplant, HIV, chemotherapy), diabetes, hypertension, CCR5Δ32 homozygosity (impaired CNS immune control).

**Three WNND syndromes:**

1. **West Nile meningitis** (~45% of WNND): Fever, severe headache, stiff neck, photophobia; CSF shows lymphocytic pleocytosis (10–100 cells/mm³), elevated protein, normal glucose; generally good prognosis

2. **West Nile encephalitis** (~40% of WNND): Altered consciousness, confusion, disorientation, seizures, extrapyramidal signs (tremor, bradykinesia — basal ganglia involvement), Parkinsonism; MRI shows T2/FLAIR signal in basal ganglia, thalamus, brainstem, periventricular white matter; mortality 3–15% in hospitalized patients; cognitive and neurological deficits common in survivors

3. **West Nile acute flaccid paralysis/poliomyelitis** (~10% of WNND): Asymmetric proximal limb weakness (anterior horn cell injury); respiratory failure if diaphragm involved; CSF pleocytosis; EMG shows anterior horn cell pattern; NCS normal → distinguishes from GBS; 50% have permanent residual weakness

### Diagnosis

- **Serology (IgM ELISA)**: Preferred; IgM appears in serum and CSF Days 4–8; highly specific; *note:* cross-reactivity with DENV, ZIKV, SLEV (St. Louis encephalitis) may require PRNT confirmation
- **RT-PCR**: Detects viremia (Days 1–6); low sensitivity after Day 7 (immune clearance); most useful for immunocompromised patients with prolonged viremia
- **Blood supply screening**: US blood supply screened by NAT (nucleic acid testing) — reduces transfusion-associated risk to <1 per million units

### Treatment and prevention

**No approved antiviral therapy.** Management is supportive:
- Uncomplicated fever: Antipyretics, rest, hydration
- Encephalitis/meningitis: Hospitalization; ICP management if severe; seizure control
- AFP: ICU admission, mechanical ventilation for respiratory compromise; physical therapy
- Experimental: IV immunoglobulin (convalescent plasma with high anti-WNV titers) — anecdotal benefit in severe cases; no RCT evidence for IFN-α, ribavirin, or steroids

**Vaccines:**
- **Human vaccines:** No approved vaccine as of 2026; multiple candidates failed in efficacy trials or development was deprioritized due to commercial considerations; candidates include ChimeriVax-WN (Sanofi), DNA vaccine (NIAID Phase II), and recombinant subunit approaches
- **Equine vaccine:** Licensed (West Nile-Innovator, Vetera WNV); ~90% efficacy; 3-dose series; widely used in the US equine industry

**Vector control and prevention:**
- Public health: Insecticide applications (pyrethroid aerial/ground spraying), larval source reduction (standing water elimination), Culex breeding habitat management
- Personal: DEET-containing repellent (≥20%), permethrin-treated clothing, mosquito netting, indoor air conditioning (reduces mosquito exposure)
- Blood donation: NAT screening; donors deferred if recent WNV exposure suspected

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: WNV NS3-NS4A complex inhibits RIG-I signaling and disrupts MAVS; NS5-mediated RNA capping (7-methylguanosine) prevents 5′ppp recognition by RIG-I → MAVS not engaged; combined NS3/NS5 strategy suppresses MAVS-TBK1-IRF3 axis enabling WNV establishment.

**→ [STAT1](../../../03-molecular/stat1/)**: WNV NS5 blocks STAT1 by: (1) preventing Tyr701 phosphorylation → ISGF3 cannot form; (2) K48-ubiquitination of STAT1 → proteasomal degradation; NS5-mediated STAT1 antagonism enables WNV to evade ISG-based antiviral defense after IFN-β induction.

**→ [RIG-I](../../../03-molecular/rig-i/)**: WNV NS5 methyltransferase caps viral RNA with 7-methylguanosine → RIG-I CTD cannot recognize 5′ppp → MAVS not activated; NS3-NS4A helicase also directly inhibits RIG-I signaling; RNA capping mimics host mRNA modification to evade cytosolic innate immunity.

**→ [Dengue Fever](../dengue-fever/)**: WNV and DENV share Aedes aegypti + Culex vectors, flavivirus structure, and flaviviral biology; anti-DENV antibodies cross-react with WNV but provide variable protection; WNV neuroinvasive disease has no DENV equivalent; both evade STAT1 via NS5.

**→ [Zika Virus](../zika-virus/)**: WNV and ZIKV are neurotropic flaviviruses with serological cross-reactivity; prior WNV immunity may partially protect against ZIKV and vice versa; unlike ZIKV, WNV lacks sexual transmission and does not cause congenital brain malformations; both NS5 proteins evade STAT1.

- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — About 1 in 150 symptomatic West Nile infections becomes neuroinvasive disease — the leading cause of viral encephalitis in North America — as meningitis, encephalitis with Parkinsonian signs, or poliomyelitis-like flaccid paralysis; the elderly are most at risk.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — West Nile virus is neurotropic, replicating in neurons after crossing the blood-brain barrier; its tropism for anterior-horn motor neurons produces an asymmetric flaccid paralysis resembling polio, while hippocampal infection drives encephalitis.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Once West Nile virus reaches the CNS, microglia and astrocytes mount the neuroinflammatory response that limits viral spread but also contributes to encephalitic injury; CCR5-dependent leukocyte recruitment is protective, and CCR5Δ32 homozygotes fare worse.
- `connects-to` → **[NMOSD](../nmo/README.md)** — West Nile virus and NMOSD can both cause acute myelitis and optic involvement but differ in mechanism: WNV is a neurotropic flavivirus infecting neurons → flaccid paralysis and encephalitis, while NMOSD is autoimmune AQP4-IgG astrocyte injury; AQP4-IgG and CSF tell them apart.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8+ cytotoxic T cells are essential to clear West Nile virus from infected neurons: they enter the CNS and kill virus-laden cells via perforin/granzyme and Fas, controlling infection but also adding immunopathology; deficient CD8 responses predict severe neuroinvasive disease.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes shape West Nile CNS disease: WNV infects them, and their cytokine output (CXCL10, IL-6) both recruits protective leukocytes and helps open the blood-brain barrier that lets virus and immune cells in; astrocyte responses balance viral control against injury.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — West Nile virus first replicates in skin and lymphoid macrophages and dendritic cells: after a mosquito bite the flavivirus amplifies in these cells, then a viremia can breach the blood-brain barrier—so the innate cells that should contain it help ferry it to the CNS.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Immunosuppression is the key risk for neuroinvasive West Nile disease: in HIV/AIDS, transplant recipients, and the elderly, weak T-cell immunity lets the virus reach the brain, causing encephalitis and flaccid paralysis—so severe WNV is mostly in the immunocompromised.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells are West Nile virus's first targets and gatekeepers: skin Langerhans cells take up the virus at the bite site and carry it to lymph nodes, and their type-I-interferon response largely determines whether infection stays mild or becomes neuroinvasive.
- `connects-to` → **[Guillain-Barré Syndrome](../../05-tissue/guillain-barre/README.md)** — West Nile virus can cause acute flaccid paralysis resembling Guillain-Barré: the neuroinvasive form attacks anterior-horn motor neurons, producing asymmetric weakness, and rarely a GBS-like demyelinating syndrome—so new flaccid paralysis in summer warrants WNV testing.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help control West Nile virus early: NK cells and interferon limit viral spread before adaptive immunity, and the aging immune system's weaker NK/T-cell response is why neuroinvasive WNV strikes mainly older adults.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — West Nile virus and COVID-19 are both viruses with neuro-invasive potential: most infections spare the CNS, but each can cause encephalitis, and both show how systemic viruses breach the blood-brain barrier in vulnerable hosts—age and immunity shaping severity.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon is the front-line defense against West Nile virus: RIG-I/MAVS sensing of viral RNA triggers interferon that restrains spread, and animals or people with weak interferon responses suffer far more severe neuroinvasive disease.
- `connects-to` → **[Dengue virus](../../../02-pathogen/01-viruses/dengue-virus/README.md)** — West Nile and dengue are related flaviviruses spread by mosquitoes: they share genome structure and immune-evasion tricks, but West Nile is neuroinvasive (encephalitis) while dengue is hemorrhagic—and cross-reacting antibodies complicate flavivirus serology.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — West Nile virus is defined by its assault on the nervous system: in a minority it crosses into the CNS to cause encephalitis, meningitis and a polio-like acute flaccid paralysis from anterior-horn motor neuron loss, leaving lasting neurological deficits.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells and their antibodies decide West Nile outcomes: a brisk IgM response curbs viremia before the virus invades the brain, and detecting WNV IgM in serum or spinal fluid is the main way it is diagnosed—so weak antibody responses predict severe neuroinvasive disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Immune status governs who gets neuroinvasive West Nile: most infections are mild, but the elderly and immunosuppressed—whose defenses let the virus cross into the brain—account for the rare meningitis, encephalitis, and paralysis that make WNV feared.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — West Nile first multiplies in lymphoid tissue like the spleen: after a mosquito bite the virus replicates in skin and is carried to spleen and lymph nodes, seeding the blood—so this peripheral phase precedes and sets up any later invasion of the nervous system.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — West Nile virus can persist in the kidney: the virus has been detected in urine months after infection and is linked to chronic kidney involvement, so the kidney is both a site of viral persistence and a route of possible shedding.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement is essential to surviving West Nile virus: C3 and the complement cascade are needed to control early viremia and prime antibody and T-cell responses, so complement-deficient hosts suffer far more severe neuroinvasive disease.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T-helper cells coordinate the defense against West Nile virus: CD4 cells sustain the antibody response and support the cytotoxic T cells that clear virus from neurons, so weak helper immunity (as with age or HIV) predicts severe neuroinvasive disease.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — West Nile is diagnosed by its antibodies: WNV-specific IgM in blood or spinal fluid signals acute infection while IgG marks past exposure, and antibody is the basis of protection—the reason the horse vaccine works though no human one yet exists.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — West Nile breaches the brain with help from TNF: inflammatory cytokines like TNF-alpha loosen the blood-brain barrier, letting the virus invade the CNS—a double-edged response that both fights the virus and causes the encephalitis.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells temper West Nile's brain damage: by restraining the antiviral attack within the CNS, Tregs limit collateral neuron injury, so the balance between clearing the virus and sparing the brain shapes recovery from neuroinvasive disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — West Nile leaves a fingerprint in the eye: it commonly causes a distinctive chorioretinitis—clusters of spots in a curved, linear pattern—so an eye exam can help diagnose neuroinvasive infection, and the lesions usually heal as the patient recovers.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — West Nile kills neurons through calcium: in encephalitis, infected and overexcited neurons let calcium flood in, triggering the excitotoxic cell death that destroys brain and spinal motor neurons and leaves lasting deficits.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — West Nile can erase synapses: even after the virus clears, activated microglia and complement prune synapses in the brain, a loss now linked to the memory and cognitive problems that linger in survivors.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Neuroinvasive West Nile is mapped by MRI: its photons reveal inflammation in the thalamus, basal ganglia and brainstem, and the spinal-cord signal behind its polio-like paralysis.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Most West Nile infections show on the skin: West Nile fever brings a blotchy maculopapular rash over the trunk and limbs, the visible face of the far commoner non-neuroinvasive disease.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — West Nile strikes the nervous system broadly: beyond the brain it injures peripheral nerves and the anterior-horn motor neurons, causing a polio-like acute flaccid paralysis that can be permanent.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows West Nile as a classic flavivirus: a small icosahedral core wrapped in a lipid envelope, assembling and budding through the membranes of the endoplasmic reticulum inside infected cells.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — West Nile encephalitis often drops the sodium: inflammation of the brain triggers SIADH, the inappropriate water retention that dilutes blood sodium and can worsen the confusion and seizures of severe neuroinvasive disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — West Nile can inflame the heart: myocarditis and arrhythmias are recognized though underappreciated complications, the virus reaching beyond the nervous system to strain the circulation in severe infection.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — West Nile is diagnosed by its antibody: detecting IgM in serum or — pointing to neuroinvasion — in the cerebrospinal fluid is the mainstay test, since the virus itself is fleeting in the blood by the time symptoms appear.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — West Nile rides the blood supply: it is transmissible through transfusion and organ transplant, so blood banks screen donations for it — a hidden route beyond the mosquito that prompted nationwide testing.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — The virus can cross to the fetus: rare intrauterine West Nile transmission through the placenta, and passage through breast milk, are documented, extending its reach from the mosquito bite to mother and child.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its worst form mimics polio: West Nile attacks the spinal cord's anterior horn motor neurons, causing an acute flaccid paralysis with muscle wasting, while even mild infection brings the prominent myalgia of West Nile fever.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Severe infection drops the platelets: West Nile can cause thrombocytopenia through marrow suppression and consumption, a falling count among the markers of the more dangerous, neuroinvasive course.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Rarely the virus inflames the liver: fulminant West Nile hepatitis is an uncommon but described severe presentation, the flavivirus injuring hepatocytes far from its usual target in the nervous system.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — The virus breaches the blood-brain barrier through the vessel wall: it infects brain microvascular endothelial cells and, with TNF-driven leakiness, loosens the barrier so the virus and immune cells flood into the brain.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Neuroinvasive disease runs hot with IL-6: the cytokine pours into the inflamed brain and spinal fluid, and high CSF IL-6 tracks with the severity of West Nile encephalitis.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Antibody is the key to survival: plasma cells must quickly pour out neutralizing IgM and IgG to clear the virus from the blood before it reaches the brain, which is why antibody-deficient people fare so badly.
- `connects-to` → **[IRF3](../../03-molecular/irf3/README.md)** — Sensing the virus triggers the interferon defense: West Nile RNA detected through RIG-I/MAVS activates IRF3 to switch on type I interferon, and the virus's NS proteins fight back by blocking this very pathway.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Its brain invasion can leave a seizure focus: West Nile encephalitis inflames the cortex and can cause acute seizures and lasting epilepsy, part of the neurologic legacy that lingers in survivors of the neuroinvasive form.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils play a double game: they are recruited early to fight the infection yet can also serve as a reservoir that ferries the virus, and their breaching of the blood-brain barrier helps the virus reach the brain.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The virus drives the inflammation that opens the brain: West Nile activates NF-κB in infected and immune cells, and the resulting cytokine surge both fights the virus and loosens the blood-brain barrier it exploits to invade.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Paralysis from neuroinvasion brings clot risk: the acute flaccid paralysis and prolonged immobility of severe West Nile disease create venous stasis that raises the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Critical neuroinvasive disease behaves like sepsis: severe West Nile encephalitis can cause respiratory failure and a critical illness in which secondary bacterial infection and sepsis complicate the course.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Its brain invasion can leave movement disorders: West Nile encephalitis targets the basal ganglia and substantia nigra, causing tremor, rigidity and a post-encephalitic parkinsonism that can persist in survivors.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Recovery carries a long mental tail: survivors of neuroinvasive West Nile disease frequently suffer persistent fatigue, cognitive impairment and depression, a post-encephalitic syndrome lasting months to years.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The virus can persist in and injure the kidney: West Nile causes acute kidney injury in severe disease and can shed in urine for years, with reports linking chronic infection to ongoing renal impairment.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its poliomyelitis-like injury leaves lasting pain: neuroinvasive West Nile can destroy anterior-horn motor neurons and inflame nerves, leaving persistent weakness and neuropathic pain long after the acute illness.
- `connects-to` → **[Stroke](../stroke/README.md)** — Severe neuroinvasion can damage cerebral vessels: West Nile meningoencephalitis can be complicated by vasculitis and hemorrhage, occasionally precipitating stroke in the acute phase.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Surviving neuroinvasive disease can scar the mind: prolonged ICU care and the slow, incomplete recovery from West Nile encephalitis and paralysis can leave post-traumatic stress alongside its cognitive sequelae.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its polio-like paralysis can stop breathing: neuroinvasive West Nile virus attacks anterior horn cells, causing acute flaccid paralysis that can involve the diaphragm and require prolonged mechanical ventilation.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — West Nile fever often shows on the skin: the milder febrile form commonly produces a transient maculopapular or roseolar rash over the trunk and limbs, a recognised clinical clue.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A slow, uncertain recovery breeds worry: the lingering fatigue, weakness and cognitive problems after West Nile neuroinvasive disease foster chronic health anxiety alongside its depression and PTSD.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its febrile phase upsets the gut: West Nile fever commonly causes nausea, vomiting, diarrhoea and abdominal pain, with rare hepatitis and pancreatitis in severe disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Brain infection unbalances sodium: West Nile encephalitis can trigger SIADH with hyponatraemia, a common electrolyte disturbance in central nervous system infections that needs careful fluid management.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Classic West Nile fever swells the nodes: generalized lymphadenopathy was a defining feature of the originally described illness, accompanying the fever and maculopapular rash.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It can inflame the heart: acute West Nile infection occasionally causes myocarditis and arrhythmia, alongside its dominant neuroinvasive disease.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It can pass through blood and birth: West Nile virus is transmitted by transfusion, organ transplant and breast milk, and rare transplacental transmission causes congenital infection.
- `connects-to` → **[Herpesviridae](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — It shares a deadly differential: herpes simplex encephalitis is the key alternative cause of viral encephalitis to exclude and empirically treat when West Nile neuroinvasive disease is suspected.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It can persist in and injure the kidney: West Nile virus RNA can be shed in urine and persist in renal tissue for years, and severe infection causes acute kidney injury.
- `connects-to` → **[Zika Virus](../../../02-pathogen/01-viruses/zika-virus/README.md)** — A neurotropic flavivirus cousin: Zika, like West Nile, is a mosquito-borne flavivirus that crosses into the nervous system and placenta, sharing antibody cross-reactivity that complicates serological diagnosis.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — They loosen the blood-brain barrier: mast-cell activation during West Nile infection releases chymase and vasoactive mediators that increase vascular permeability, helping the virus cross into the brain.
- `connects-to` → **[Zoonosis](../../../02-pathogen/06-environmental/zoonosis/README.md)** — A bird-and-mosquito zoonosis: West Nile virus cycles between birds and Culex mosquitoes, with humans and horses dead-end hosts infected by the bite — a One Health problem driven by climate and bird migration.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — It paralyses like polio: West Nile virus has a tropism for spinal anterior-horn motor neurons, and the resulting axonal injury causes an acute asymmetric flaccid paralysis indistinguishable from poliomyelitis.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — It scars memory: neuroinvasive West Nile encephalitis injures deep brain structures including the hippocampus, leaving many survivors with lasting memory, cognitive and fatigue problems after the acute illness.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes raises its danger: advanced age, immunosuppression and diabetes are the main risk factors for severe neuroinvasive West Nile disease—encephalitis, meningitis and acute flaccid paralysis—turning a usually mild infection deadly.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — It can linger in the kidney: West Nile virus can persist in renal tissue with prolonged urinary shedding, and is associated with chronic kidney disease and proteinuria in some survivors.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It occasionally inflames the heart: beyond its neuroinvasive disease, West Nile virus is a rare cause of myocarditis, adding cardiac injury to severe infection.
- `connects-to` → **[ALS](../als/README.md)** — A polio-like paralysis: West Nile virus can attack anterior-horn motor neurons, causing an acute asymmetric flaccid paralysis that resembles poliomyelitis and, in its motor-neuron targeting, the cells lost in ALS.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Antibody clears the virus: control of West Nile virus depends on neutralizing antibody matured in germinal centres, which is why B-cell-deficient and elderly patients suffer the severe neuroinvasive disease.
- `connects-to` → **[Measles](../measles/README.md)** — Viruses that invade the brain: like measles—which causes acute encephalitis and the late, fatal SSPE—West Nile virus crosses into the CNS, the two showing viral neuroinvasion by different routes.
- `connects-to` → **[CIDP](../cidp/README.md)** — Flaccid paralysis and demyelination: West Nile virus causes a poliomyelitis-like acute flaccid paralysis from anterior-horn injury and can also trigger a Guillain-Barré/demyelinating neuropathy on the CIDP spectrum.
- `connects-to` → **[Malaria](../malaria/README.md)** — Vector-borne febrile differential: West Nile virus (Culex-borne) and malaria both present as acute mosquito-transmitted febrile illness, an overlapping differential in travellers and endemic regions.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Respiratory failure from paralysis: severe neuroinvasive West Nile virus can paralyse the diaphragm and respiratory muscles, leading to ventilator dependence and aspiration that injure the alveoli.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Antiviral defence: IFN-γ from T and NK cells is critical for controlling West Nile virus and clearing it from the CNS, with deficiency predisposing to severe neuroinvasive disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuroinflammation: IL-1β from activated microglia drives the inflammatory response to West Nile encephalitis, contributing both to viral control and to bystander neuronal injury.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome sensing: the NLRP3 inflammasome detects West Nile virus and matures IL-1β, a double-edged response that restrains the virus yet aggravates CNS inflammation.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — Leukocyte trafficking to the brain: CCR5 directs protective leukocytes into the West Nile-infected CNS, and the CCR5-Δ32 loss-of-function variant markedly raises the risk of symptomatic and fatal neuroinvasive disease.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws inflammatory monocytes across the blood-brain barrier in West Nile encephalitis, aiding viral clearance while contributing to the immunopathology of the infection.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic clearance: CD8 T cells use perforin and granzyme to eliminate West Nile virus from infected neurons, a defence essential for survival that can also injure the neurons it protects.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 from activated dendritic cells drives the Th1 and IFN-γ response that controls West Nile virus, biasing immunity toward the cell-mediated clearance the neuroinvasive infection requires for survival.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — IL-10 tempers the antiviral response in West Nile infection, and excess IL-10 is associated with worse outcomes by blunting the immunity needed to clear the virus from the central nervous system.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 at the blood-brain barrier retains CXCR4+ leukocytes in the perivascular space, and CXCR4 antagonism improves West Nile outcomes in models by releasing protective T cells into the infected brain parenchyma.
- `connects-to` → **[MyD88](../../03-molecular/myd88/README.md)** — MyD88-dependent Toll-like-receptor signaling is essential for controlling West Nile virus, organizing leukocyte positioning in the brain, and MyD88-deficient hosts suffer markedly higher viral burden and neuroinvasion.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — Neutralizing IgG against the viral envelope is the key correlate of protection from West Nile encephalitis, and FcRn recycling sustains the circulating antibody and the half-life of therapeutic monoclonals and immune globulin under study.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Presentation of West Nile antigens on MHC class II primes the CD4 T-cell help needed for durable antibody responses and for supporting the CD8 T cells that clear virus from infected neurons.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — West Nile virus drives caspase-3-mediated apoptosis of infected neurons, the cell death directly responsible for the encephalitis and the poliomyelitis-like acute flaccid paralysis of neuroinvasive disease.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — The complement system (C3 already mapped, through C5) is essential for the protective antibody and T-cell responses that control West Nile virus, shaping both clearance and immunopathology.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Cytokine- and VEGF-driven blood-brain-barrier permeability lets West Nile virus and inflammatory cells enter the CNS, a key step enabling its neuroinvasion.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — West-Nile-infected neuron death and the inflammatory milieu drive glutamate excitotoxicity, a mechanism of the neuronal injury underlying West Nile encephalitis.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — The balance of anti-apoptotic BCL-2 against viral- and immune-driven pro-apoptotic signals (caspase-3 mapped) sets neuronal survival in West Nile neuroinvasive disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — West Nile virus manipulates host PI3K-AKT signaling to delay apoptosis early in infection, sustaining the cellular environment for viral replication.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Type-I-interferon signaling through JAK-STAT (STAT1 mapped) is the principal antiviral defense controlling West Nile virus, which the virus actively antagonizes.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — West Nile virus modulates mTOR-regulated translation and autophagy to support its replication in infected cells.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling is engaged during West Nile virus entry and replication and contributes to the inflammatory response in neuroinvasive disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by activated microglia amplifies the neuroinflammation and blood-brain-barrier disruption of West Nile virus neuroinvasive disease.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory cytokine response that accompanies West Nile virus encephalitis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling modulates the blood-brain-barrier integrity and the balance between protective and pathological responses in West Nile virus neuroinvasion.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic nucleic-acid sensing through cGAS-STING contributes to the innate antiviral and neuroinflammatory response that restrains West Nile virus.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates neuronal survival and oxidative-stress responses during West Nile virus neuroinvasion.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α responses in infected and inflamed CNS tissue shape the blood-brain-barrier disruption of neuroinvasive West Nile virus.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the innate antiviral and neuronal survival signaling relevant to West Nile virus neuroinvasion.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA)-AKT signaling (AKT already mapped) is exploited by West Nile virus to support its replication and modulate neuronal survival.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the neuroinflammation of West Nile virus encephalitis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — West Nile virus modulates host autophagy to support its replication in neurons and other cells.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the endothelial and blood-brain-barrier responses to West Nile virus neuroinvasion.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling, exploited for the lipid-dependent replication of West Nile virus, participates in the host response.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the host immune response to West Nile virus.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory and immune responses to West Nile virus.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the blood-brain-barrier permeability and neuroinflammation of West Nile virus neuroinvasive disease.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the host response to West Nile virus.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation of the antiviral immune response to West Nile virus.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the leukocyte recruitment and neuroinflammatory response to West Nile virus.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Blood-brain-barrier injury: neuroinflammatory nitric oxide contributes to the blood-brain-barrier disruption and neuronal damage of West Nile encephalitis, part of the immunopathology that accompanies viral clearance from the brain.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell control: IL-2-driven expansion of the CD8 T cells that clear West Nile virus from infected neurons (perforin already mapped) is essential to controlling neuroinvasive infection, and waning T-cell immunity underlies severe disease in the elderly.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Acute flaccid paralysis: West Nile virus can infect anterior-horn motor neurons to cause a poliomyelitis-like acute flaccid paralysis, disrupting cholinergic transmission at the neuromuscular junction and leaving lasting weakness.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Antibody help: IL-4 and type-2 T-cell help support the B-cell (already mapped) production of the neutralising antibodies (IgG already mapped) that protect against West Nile virus, the humoral immunity whose failure permits neuroinvasion.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative neuronal injury: reactive oxygen species from xanthine oxidase and other sources contribute to the oxidative stress that damages neurons during West Nile encephalitis, compounding the direct viral and immune-mediated injury.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Myocarditis: West Nile virus can rarely cause myocarditis, and troponin elevation marks the myocardial injury of this cardiac involvement, one of the recognised extraneural manifestations of severe infection.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammatory eicosanoids: prostaglandins from the activated microglia (already mapped) and infiltrating cells contribute to the neuroinflammation and fever of West Nile encephalitis (IL-6 and IL-1 already mapped), part of its inflammatory injury.
- `connects-to` → **[Aquaporin-4](../../03-molecular/aquaporin-4/README.md)** — Blood-brain-barrier and oedema: the astrocyte water channel aquaporin-4 governs brain water balance, and its disturbance in West Nile encephalitis contributes to the blood-brain-barrier disruption and cerebral oedema (glutamate excitotoxicity already mapped).
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 antibody help: IL-13, with IL-4 (already mapped), supports the B-cell (already mapped) neutralising-antibody response that controls West Nile viraemia, the humoral arm balancing the Th1 (IL-12 and interferon-gamma already mapped) response.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium and excitotoxicity: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity that kills infected neurons (already mapped) in West Nile encephalitis, a neuroprotective ion.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and antiviral immunity: zinc supports the interferon (already mapped) antiviral response and inhibits flavivirus replication, and zinc status influences the immunity that determines the outcome of West Nile virus infection.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium antioxidant defence: selenium and its selenoproteins support the antioxidant defence and the antiviral immunity against West Nile virus, and deficiency can worsen the oxidative injury of the neuroinvasive infection.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Blood-brain-barrier permeability: substance P increases the permeability of the blood-brain barrier, facilitating the neuroinvasion of West Nile virus into the brain (already mapped) and the encephalitis.
- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — Regulatory and repair signalling: TGF-β shapes the regulatory (Treg already mapped) and tissue-repair response that resolves the neuroinflammation of West Nile encephalitis, balancing viral control against immunopathology.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — T-cell exhaustion: the PD-1 checkpoint on the cytotoxic T cells (already mapped) can limit the viral clearance in severe or persistent West Nile virus infection, part of the immune regulation of the disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Immune-metabolic adipokine: leptin is the adipokine of the immune-metabolic milieu; the nutritional and metabolic state modulates the age-dependent (the elderly worse) susceptibility to West Nile virus.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the immune-metabolic milieu of the West Nile virus infection.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the inflammatory (IL-6 and TNF already mapped) response to West Nile virus.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the protective Th1 (IFN-γ and IL-12 already mapped) antiviral response to West Nile virus.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune response to the West Nile virus infection.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune response to the West Nile virus neuroinvasive infection.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) is part of the complement-mediated protection and neuroinflammation of the West Nile virus infection.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — BBB permeability: the bradykinin-kinin system increases the blood-brain-barrier permeability that facilitates the neuroinvasion of the West Nile virus into the brain (already mapped).
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Vascular permeability: the histamine, from the mast cells (already mapped), increases the vascular permeability that enhances the CNS entry of the West Nile virus.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement evasion: the West Nile virus NS1 protein recruits the host factor H to inactivate the C3 convertase (complement C3, C5 and C5aR1 already mapped) and evade the complement attack.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact (bradykinin already mapped) systems whose activation contributes to the vascular permeability and neuroinvasion of the West Nile virus.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Nutritional immunity: transferrin, by sequestering iron, is part of the host nutritional-immunity response to the West Nile virus infection.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Coagulopathy: thrombin, at the interface of the contact (bradykinin already mapped) and coagulation systems, contributes to the microvascular coagulopathy and thromboinflammation of severe West Nile virus infection.
- `connects-to` → **[Connexin43](../../03-molecular/connexin43/README.md)** — Astrocyte gap junctions: connexin43, the astrocyte (already mapped) gap-junction protein, is disrupted during the West Nile virus neuroinvasion, compromising the blood-brain-barrier integrity and glial coupling.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Reactive gliosis: periostin, a matricellular mediator, is part of the tissue-remodelling and reactive-gliosis response of the CNS to the West Nile virus encephalitis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuro-epithelial alarmin: TSLP, released from the skin (already mapped) and mucosal barriers at the site of mosquito inoculation and during viraemia, activates mast cells (already mapped) and dendritic cells (already mapped), shaping the early innate response to West Nile virus.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective signal: erythropoietin, acting via EPOR on neurons (already mapped) and astrocytes (already mapped), attenuates the oxidative and neuroinflammatory damage of the West Nile virus encephalitis and promotes neuronal survival.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Antiviral chronobiotic: melatonin, via MT1/MT2 receptors on macrophages (already mapped) and NK cells (already mapped), inhibits NLRP3 inflammasome (already mapped) activation and reduces the neuroinflammatory cytokine storm of West Nile virus encephalitis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine antiviral modulator: prolactin, acting via PRLR on macrophages (already mapped), NK cells (already mapped) and T cells (already mapped), promotes innate antiviral effector responses and modulates the neuroinflammatory milieu of West Nile virus encephalitis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Neuroimmune neuroprotection: oxytocin, via oxytocin receptors on microglia (already mapped) and astrocytes (already mapped), suppresses the pro-inflammatory cytokine (TNF-α and IL-6 already mapped) cascade and the BBB-disrupting neuroinflammation of West Nile virus encephalitis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen sex-differential severity: testosterone, via androgen receptors on microglia (already mapped) and astrocytes (already mapped), modulates the neuroinflammatory response and contributes to the greater severity and higher mortality of WNV encephalitis in males vs. females.
