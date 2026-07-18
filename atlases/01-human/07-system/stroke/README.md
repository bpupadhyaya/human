---
schema: human-scale-entry/v1
id: stroke
name: Stroke
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Sudden focal neurological deficit from cerebral ischemia (87%) or hemorrhage (13%). Ischemic stroke treated with IV alteplase (tPA, ≤4.5 h) and thrombectomy (≤24 h); hemorrhagic with BP control. Second leading global cause of death and disability."
aliases: ["cerebrovascular accident", "CVA", "ischemic stroke", "hemorrhagic stroke", "brain attack"]
sources:
  - id: powers-2019-aha-stroke
    type: peer-reviewed
    cite: "Powers WJ, Rabinstein AA, Ackerson T, et al. Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update to the 2018 Guidelines. Stroke. 2019;50(12):e344-e418."
    doi: "10.1161/STR.0000000000000211"
    pmid: "31662037"
    url: "https://doi.org/10.1161/STR.0000000000000211"
  - id: feigin-2021-gbd-stroke
    type: peer-reviewed
    cite: "Feigin VL, Krishnamurthi RV, Parmar P, et al. Update on the Global Burden of Ischemic and Hemorrhagic Stroke in 1990-2013. Neuroepidemiology. 2015;45(3):161-176."
    doi: "10.1159/000441085"
    pmid: "26505981"
    url: "https://doi.org/10.1159/000441085"
  - id: hacke-2008-ecass3
    type: peer-reviewed
    cite: "Hacke W, Kaste M, Bluhmki E, et al. Thrombolysis with alteplase 3 to 4.5 hours after acute ischemic stroke. N Engl J Med. 2008;359(13):1317-1329."
    doi: "10.1056/NEJMoa0804656"
    pmid: "18815396"
    url: "https://doi.org/10.1056/NEJMoa0804656"
cross_links:
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Stroke injures brain via glutamate excitotoxicity → Ca²⁺ overload → neuronal death (ischemic core, minutes); surrounding penumbra survives hours if reperfused — the therapeutic target; hemorrhagic stroke causes parenchymal compression, hematoma expansion, and perilesional edema."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Hypertension is the dominant modifiable stroke risk factor (~60% attributable risk for ischemic, >80% for ICH); small vessel disease causes lacunar infarcts; BP lowering reduces recurrent stroke by 30-40% (ACEi + thiazide, SPS3 trial)."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial eNOS-derived NO maintains cerebral vasodilation; ischemia depletes protective eNOS NO → vasoconstriction; neuronal nNOS in the ischemic core produces peroxynitrite (NO + superoxide) → neurotoxicity; eNOS and nNOS have opposing roles in stroke outcome."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Cardioembolic stroke (25-30% of ischemic strokes) originates from cardiac thrombi: atrial fibrillation (left atrial appendage) is the dominant source; also prosthetic valves, post-MI mural thrombi, and endocarditis; oral anticoagulants (DOACs) prevent cardioembolic stroke in AF."
  - target: 01-human/03-molecular/pcsk9
    relation: connects-to
    note: "LDL-C-driven carotid atherosclerosis causes ischemic stroke via thromboembolism; PCSK9 inhibitors (evolocumab, alirocumab) reduce stroke risk ~25% in post-MI patients; very low LDL-C (<25 mg/dL) with PCSK9 inhibition does not impair cognition and reduces stroke incidence."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Thrombin generates fibrin clots in cerebral arteries → ischemic stroke; AF→ atrial thrombus → embolism → cardioembolic stroke; ICH → thrombin release → perihematomal inflammation and edema; dabigatran (direct thrombin inhibitor) and apixaban/rivaroxaban prevent AF-related stroke."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "SCD is the most common cause of childhood stroke (<10 years; cerebral vasculopathy from sickling → large vessel stenosis); transcranial Doppler (TCD) screening identifies high-risk patients; chronic transfusion (target HbS <30%) reduces stroke risk 92% (STOP trial)."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Migraine with aura (MA) confers 2× ischemic stroke risk; CSD-triggered spreading oligemia → ischemic cascade in vulnerable cortex; PFO prevalence higher in MA; oral contraceptives + MA + smoking multiplies stroke risk; CADASIL (NOTCH3) presents with MA + lacunar strokes."
  - target: 01-human/07-system/familial-hypercholesterolemia
    relation: connects-to
    note: "FH accelerates carotid and cerebrovascular atherosclerosis; HeFH patients have elevated carotid intima-media thickness (cIMT) and higher stroke risk vs. general population; statin + PCSK9 inhibitor reduces cIMT progression and ischemic stroke incidence in FH cohorts."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: prevented-by
    note: "Warfarin prevents AF-related ischemic stroke by 64% (Hart 2007); INR 2.0–3.0; preferred over DOACs for mechanical heart valves (INR 2.5–3.5); antiphospholipid syndrome triple-positive: warfarin INR 3.0–4.0 (TRAPS trial confirmed DOACs inferior)."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "NSAIDs including ibuprofen increase ischemic stroke/MI risk ~1.3–1.5× via ↓ endothelial PGI₂; ibuprofen blocks aspirin irreversible COX-1 acetylation → ↓ cardioprotective antiplatelet effect; avoid in high cardiovascular risk patients."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: treated-by
    note: "Aspirin is first-line secondary stroke prevention after TIA/minor ischemic stroke; irreversible platelet COX-1 blockade → ↓ TXA₂ → ↓ atherothrombotic and cardioembolic risk; 300 mg loading dose reduces 90-day recurrence (CAST, IST); contraindicated in hemorrhagic stroke."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Atherosclerosis is the dominant cause of ischemic stroke: plaques in the carotid and cerebral arteries rupture to form occlusive clots or shed emboli, so the lipid-driven disease behind heart attacks also kills brain tissue—treated by statins and antiplatelets."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Antiphospholipid syndrome is an important cause of stroke in the young: antiphospholipid antibodies make blood prothrombotic, causing arterial and venous clots, so an unexplained young stroke—especially with prior clots or pregnancy loss—warrants APS testing."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Stroke kills neurons through the ischemic cascade: loss of blood flow starves neurons of oxygen and glucose, triggering glutamate excitotoxicity, calcium overload, and death within minutes in the core—so time is brain, and rapid reperfusion salvages the penumbra."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes shape stroke outcome: after ischemia they swell and fail to clear glutamate, worsening excitotoxicity, then form the glial scar that both limits damage and impedes regeneration—so astrocyte responses help determine the size and recovery of the infarct."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate excitotoxicity is the core of stroke neuronal death: energy failure floods the synapse with glutamate, overactivating NMDA receptors and letting calcium pour in to kill neurons, so the excitatory transmitter becomes the executioner in the ischemic penumbra."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Type 2 diabetes roughly doubles stroke risk: chronic hyperglycemia accelerates atherosclerosis and small-vessel disease, and high glucose at stroke onset worsens infarct size and outcome—so glycemic control is central to stroke prevention."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets are central to ischemic stroke and its prevention: clot formation on a ruptured plaque occludes a cerebral artery, so antiplatelet drugs (aspirin, clopidogrel) are the cornerstone of preventing non-cardioembolic stroke."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Stroke is the leading cause of acquired nervous-system disability: sudden loss of blood flow kills neurons in minutes, and which functions are lost—speech, movement, vision—depends entirely on which part of the brain's circuitry the dead tissue served."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Stroke and venous thromboembolism share a prothrombotic basis and complicate each other: immobility after stroke raises DVT/PE risk, and a clot crossing a patent foramen ovale can cause paradoxical embolic stroke—so thromboprophylaxis is routine in stroke care."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Many strokes start in the heart: atrial fibrillation, valve disease, and a patent foramen ovale let clots form and travel to the brain (cardioembolic stroke), so finding the cardiac source guides anticoagulation to prevent the next stroke."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is the executioner in stroke: when ischemia depletes energy, neurons flood with calcium that activates enzymes destroying the cell—the excitotoxic cascade that turns minutes of lost blood flow into permanent brain damage."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia shape stroke's aftermath: the brain's resident immune cells swarm the infarct, first worsening injury with inflammation, then clearing debris and aiding repair—so tipping their balance toward repair is a target for limiting stroke damage."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Stroke's damage begins with failed sodium pumps: when blood flow stops, neurons can't power the Na/K-ATPase, so sodium and water flood in causing cytotoxic edema—the first step of the ischemic cascade before calcium and glutamate finish the job."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression follows stroke in up to a third of survivors: brain injury plus the disability and biochemical changes drive post-stroke depression, which slows rehabilitation and worsens outcomes—so screening and treating mood is part of stroke care."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Stroke kills oligodendrocytes and the myelin they maintain: white-matter ischemia destroys these myelinating cells, and their poor regeneration is why white-matter strokes leave lasting deficits—a target for remyelination and neuroprotection research."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Stroke is fundamentally an oxygen emergency: a blocked or burst vessel cuts the brain's oxygen supply, and because neurons have almost no reserve, the tissue begins to die within minutes—why 'time is brain' drives emergency care."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "The vessel lining is where most strokes begin: endothelial dysfunction and atherosclerosis spawn the clots that block brain arteries, and after a stroke the damaged endothelium lets the blood-brain barrier leak, worsening swelling."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Stroke kills by starving cells of ATP: without oxygen and glucose, neurons cannot make ATP, so their ion pumps fail, calcium and sodium flood in, and the resulting excitotoxic cascade destroys the tissue in the ischemic core."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Stroke collapses the brain's potassium gradient: when energy fails, neurons leak potassium and depolarize in spreading waves that march across the tissue, recruiting the penumbra and enlarging the infarct."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Stroke turns synapses toxic: starved neurons dump glutamate that overexcites neighboring synapses, and this excitotoxic flood—through calcium overload—kills the cells the clot did not directly reach."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Stroke endangers the lungs through swallowing: damage to swallowing control lets food and saliva slip into the airway, so aspiration pneumonia is a leading cause of death in the weeks after a stroke."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Stroke care races on imaging: CT photons instantly separate a bleed from a clot, and MRI and perfusion scans map salvageable brain, deciding who gets clot-busting drugs or thrombectomy."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye warns of stroke: amaurosis fugax, a fleeting curtain of vision loss from a retinal-artery clot, is a TIA of the eye that flags carotid disease and impending stroke."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Recovery after stroke leans on BDNF: this growth factor drives the neuroplasticity that lets surviving brain rewire around the dead tissue, the molecular basis of rehabilitation gains."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy captures the dying neuron: starved of oxygen, it swells with cytotoxic edema as failing pumps let water and calcium flood in, and its mitochondria balloon — the ultrastructure of the excitotoxic cascade that kills brain tissue."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "The brain heals a stroke with a glial scar: astrocytes wall off the dead infarct in a dense gliosis, the central-nervous-system version of fibrosis that contains the damage but blocks the regrowth of axons through it."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "A stroke can bleed the stomach: the surge of stress drives acid-related Cushing ulcers, while damage to the swallowing centers brings the dysphagia that risks aspiration and demands careful feeding."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Reproductive hormones shape stroke risk: estrogen-containing contraception and pregnancy raise the clotting risk — sharply so with migraine aura — while eclampsia and postpartum cerebral angiopathy are direct obstetric causes of stroke."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies can clot the brain young: antiphospholipid antibodies are a major cause of stroke in the under-50s, driving the hypercoagulability that lodges clots in cerebral vessels even without atherosclerosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "A stroke can sever the brain's control of the bowel: damage to the pathways governing continence brings fecal incontinence or, with immobility and reduced intake, stubborn constipation during recovery."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Recovery is fought in the muscles: a stroke leaves hemiparesis, then spasticity and contractures, and disuse wastes the affected limbs — making physical rehabilitation the long, central work of regaining function."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Heart and brain trade blows: a clot from a fibrillating or infarcted heart causes cardioembolic stroke, while the stroke itself can stun the cardiomyocytes — neurogenic Takotsubo and arrhythmia from the catecholamine surge."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Lowering LDL guards against the next one: high cholesterol builds the carotid and cerebral plaques that throw clots, so statins and other LDL-lowering drugs are a cornerstone of preventing ischemic stroke."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "Clotting genes cause stroke in the young: inherited thrombophilias raise the risk of cerebral venous thrombosis and, via a patent foramen, paradoxical arterial stroke, so an unexplained young stroke prompts a hypercoagulability workup."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The artery wall's muscle shapes the stroke: vascular smooth muscle builds the cerebral plaques and, in small-vessel disease and vasospasm after hemorrhage, its dysfunction narrows the arteries that feed the brain."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "A stroke can leave the brain in pain: damage to the thalamus or sensory pathways causes central post-stroke pain, a relentless neuropathic burning on the paralyzed side that is hard to treat."
  - target: 01-human/03-molecular/aquaporin-4
    relation: connects-to
    note: "Brain swelling after stroke runs through aquaporin-4: this astrocyte water channel drives the cytotoxic edema that follows ischemia, and its role makes it a target for limiting the dangerous post-stroke brain swelling."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The heart and brain share the clot risk: heart failure and the atrial fibrillation that accompanies it throw cardioembolic clots to the brain, while a large stroke can in turn stun the heart — a two-way cardio-cerebral link."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Failing kidneys raise the stroke risk: chronic kidney disease accelerates vascular disease and disturbs clotting, increasing both ischemic and hemorrhagic stroke while complicating the anticoagulation used to prevent them."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Reperfusion ignites neuroinflammation through NF-κB: after the clot, NF-κB activation in microglia and the injured brain drives the cytokine surge and edema that extend the infarct in the hours after stroke."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Stroke scars the cortex into a seizure focus: it is the leading cause of new-onset epilepsy in older adults, the gliotic infarct rim becoming an irritable focus for post-stroke seizures."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The aftermath opens the door to infection: stroke brings dysphagia, aspiration and immobility, so pneumonia and urinary infection — and the sepsis they can become — are common, dangerous early complications."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Paralysis melts the bone: disuse of a hemiparetic limb, immobility and low vitamin D after stroke accelerate bone loss on the affected side, raising the risk of fractures from the falls stroke also causes."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Fear shadows recovery: post-stroke anxiety is common alongside depression, driven both by the direct brain injury and by the fear of recurrence and lost independence, and it impedes rehabilitation."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Small-vessel strokes can mimic it: cumulative infarcts in the basal ganglia produce vascular parkinsonism — a lower-body, gait-predominant syndrome that resembles and overlaps with Parkinson's disease."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "It impairs the swallow and seeds the lung: stroke commonly causes dysphagia, and the resulting aspiration pneumonia — often pneumococcal — is a leading early complication and cause of death."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Paralysis and immobility break down the skin: hemiparesis and bedbound recovery after stroke predispose to pressure ulcers over insensate, poorly moved skin that then heal slowly."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Infarcts accelerate cognitive decline: stroke causes vascular dementia directly and lowers the threshold for Alzheimer-type dementia, the two often coexisting as mixed dementia in survivors."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Swallowing failure floods the lungs: stroke causes dysphagia and impaired cough, so aspiration pneumonia is a leading early complication, and large strokes can trigger neurogenic pulmonary oedema."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It disrupts the whole gut from mouth to bowel: stroke-related dysphagia forces modified diets or PEG feeding, and immobility and autonomic change bring constipation and faecal incontinence."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It unsettles the bladder and threatens the kidneys: stroke commonly causes urinary incontinence or retention with infection, and contrast for imaging and thrombectomy can injure the kidneys."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It disturbs glucose and sodium: stress hyperglycaemia worsens stroke outcomes, and hypothalamic or pituitary strokes cause SIADH or cerebral salt wasting with dangerous sodium shifts."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Brain injury suppresses immunity: stroke-induced immunodepression in the days afterward raises the risk of pneumonia and urinary infection, a major driver of early mortality."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Paralysis and immobility break the skin: pressure ulcers over the sacrum and heels are a major preventable complication after a disabling stroke."
  - target: 03-medicine/01-modern/04-cardio/statins
    relation: connects-to
    note: "Lipid-lowering prevents the next one: high-intensity statins reduce recurrent ischaemic stroke by stabilising atherosclerotic plaque, a cornerstone of secondary prevention."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "Blood pressure is the dominant modifiable risk: lowering it with ACE inhibitors and other antihypertensives is the single most effective way to prevent both ischaemic and haemorrhagic stroke."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "A virus that inflames cerebral arteries: varicella-zoster can cause a vasculopathy of the brain arteries leading to stroke, weeks after shingles and especially in children or the immunocompromised."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: connects-to
    note: "Infection raises the risk: COVID-19 promotes a hypercoagulable, inflamed state that increases ischaemic stroke, including large-vessel strokes in younger patients."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: connects-to
    note: "A drug for the bleeding kind: the calcium-channel blocker nimodipine reduces delayed cerebral ischaemia from vasospasm after subarachnoid haemorrhage, improving outcomes."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "A modifiable driver: obesity raises stroke risk through hypertension, diabetes, atrial fibrillation and atherosclerosis, making weight central to prevention."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It begins in the vessel wall: most ischaemic strokes arise from atherosclerotic plaque in the carotid and intracranial arteries, and haemorrhagic stroke from arterial-wall rupture in hypertension or amyloid angiopathy."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "The heart's rhythm throws clots: atrial fibrillation, a disorder of the cardiac conduction system, lets thrombus form in the left atrial appendage and embolise to the brain — the leading cause of cardioembolic stroke."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "It is selectively vulnerable: the hippocampus is exquisitely sensitive to ischaemia, so global hypoperfusion and recurrent strokes injure it preferentially, driving the memory loss of vascular cognitive impairment."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Thalassaemia raises stroke risk: chronic haemolysis, a hypercoagulable state and post-splenectomy thrombocytosis predispose to ischaemic stroke, especially in non-transfusion-dependent thalassaemia."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "The cardioembolic source: clots forming on a fibrillating atrium, a damaged valve or infective endocarditis on the endocardium break off and lodge in cerebral arteries, a leading cause of ischaemic stroke."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Too-thick blood clots the brain: the raised red-cell mass and platelet count of polycythaemia vera cause hyperviscosity and thrombosis, making stroke a presenting feature."
  - target: 01-human/07-system/giant-cell-arteritis
    relation: connects-to
    note: "Vasculitic stroke: giant-cell arteritis and other large-vessel vasculitides can occlude cerebral and ophthalmic arteries, causing stroke and sudden blindness that prompt steroids can prevent."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Infection-triggered clots: COVID-19 raises stroke risk through a hypercoagulable, inflammatory state, sometimes causing large-vessel occlusion even in younger patients."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "A cardioembolic source: a left-ventricular mural thrombus after myocardial infarction or in cardiomyopathy can dislodge from the myocardium and embolise to the brain, causing cardioembolic stroke."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Aspiration pneumonia: stroke commonly impairs swallowing, and aspirated material seeds the alveolus with infection—a leading cause of post-stroke morbidity and death."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Vasculitic stroke: ANCA-associated and other CNS vasculitides inflame and occlude cerebral arteries, causing ischaemic stroke through a non-atherosclerotic mechanism."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Haemorrhagic stroke: severe factor VIII deficiency predisposes to spontaneous intracranial haemorrhage, a leading cause of death in haemophilia and the bleeding counterpart of ischaemic stroke."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Ischaemic response: HIF-1α stabilised in the hypoxic penumbra after stroke drives both protective angiogenesis and harmful inflammation, shaping the fate of salvageable brain tissue."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammatory injury: IL-1β released by activated microglia after ischaemia expands the infarct, and IL-1 blockade is under investigation to limit post-stroke brain damage."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Post-stroke inflammation: IL-6 surges after stroke, both reflecting infarct size and contributing to the systemic inflammatory response that worsens outcome."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Ischaemic inflammasome: NLRP3 inflammasome activation in microglia after ischaemia matures IL-1β and drives pyroptotic cell death, expanding the infarct in the hours after stroke onset."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte infiltration: CCL2 released from the ischaemic brain recruits blood monocytes across the disrupted blood-brain barrier, shaping the secondary inflammatory injury and repair after stroke."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Repair and barrier: VEGF drives post-stroke angiogenesis and neurovascular repair but also opens the blood-brain barrier acutely, a double-edged contributor to oedema and recovery."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Penumbral apoptosis: in the salvageable ischaemic penumbra, neurons die more slowly by caspase-3-mediated apoptosis rather than core necrosis, the delayed cell death that neuroprotective strategies aim to interrupt."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Reperfusion neuroinflammation: DAMPs released by ischaemic brain tissue engage microglial TLR4, igniting the NF-κB-driven inflammation that worsens ischaemia-reperfusion injury after stroke and recanalisation."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Thromboembolic substrate: fibrinogen is converted by thrombin into the fibrin clot of ischaemic stroke, the target of thrombolysis with tPA that cleaves fibrin to restore cerebral perfusion."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Excitotoxic death: glutamate flooding the ischaemic core opens NMDA channels to a lethal calcium influx, and the resulting calcium overload activates proteases and destroys mitochondria — the final common pathway of neuronal death in the stroke penumbra."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Reperfusion injury: when blood flow is restored by thrombolysis or thrombectomy, xanthine-oxidase-derived reactive oxygen species burst into the reoxygenated tissue, the oxidative reperfusion injury that can extend the damage the clot began."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Cerebral vasospasm: endothelin-1 released after subarachnoid haemorrhage is a key driver of the delayed cerebral vasospasm that causes secondary ischaemic stroke days after the initial bleed, a major cause of poor outcome."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Reperfusion oxidative stress: reperfusion after ischaemic stroke generates a burst of reactive oxygen species, and the NRF2 antioxidant response is a key endogenous defence protecting the salvageable penumbra."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Penumbral spread: astrocytic connexin-43 gap junctions and hemichannels propagate peri-infarct spreading depolarisations and release glutamate and ATP, expanding the ischaemic penumbra into completed infarct."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Post-ischaemic inflammation: complement activation after stroke contributes to the secondary neuroinflammatory injury, while also influencing the neural repair and plasticity of recovery."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Sterile neuroinflammation: ischaemic damage-associated molecular patterns engage TLR4 signalling through MyD88 to NF-κB (TLR4 and NF-κB already mapped), igniting the sterile neuroinflammation that expands the infarct in the hours after stroke."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory injury: TNF-α from activated microglia amplifies blood-brain-barrier breakdown and neuronal death in the ischaemic penumbra, a key cytokine driver of secondary injury after stroke."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Recovery plasticity: BDNF signalling through its TrkB receptor (NTRK) drives the neuroplasticity and axonal sprouting that underpin functional recovery in the weeks after stroke."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT prosurvival signalling protects penumbral neurons after ischemic stroke, a target for neuroprotection."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 is strongly induced after ischemic stroke, driving the post-stroke neuroinflammatory response."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3-driven reactive astrogliosis shapes glial-scar formation and tissue repair after stroke."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Mitochondrial and nuclear DNA released by ischaemic cell death engages cGAS-STING, driving the sterile neuroinflammation of the post-stroke penumbra."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling drives the interferon-responsive microglial activation that shapes the inflammatory injury after stroke."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling contributes to the neuroprotective and tissue-repair responses that follow the acute ischaemic injury of stroke."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the neuronal oxidative-stress and autophagy responses to the ischemia-reperfusion injury of stroke."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by infiltrating myeloid cells amplify the post-ischemic neuroinflammation of stroke."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling participates in both the excitotoxic neuronal injury and the reparative neuroplasticity that follow stroke."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β activation contributes to the neuronal apoptosis and blood-brain-barrier injury of ischemic stroke, a target for neuroprotection."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) mediates the neuronal survival and pro-recovery pathways in stroke."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK signaling, activated by the energy crisis of cerebral ischemia, shapes the metabolic and autophagic response to stroke."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal survival and injury responses to the ischemic and reperfusion stress of stroke."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the blood-brain-barrier disruption and excitotoxic injury of stroke."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte infiltration contributes to the post-ischemic neuroinflammation and modulates recovery after stroke."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the neuronal-injury and repair responses of stroke."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neural-progenitor mobilization and post-stroke neurovascular repair of stroke."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory and reparative microglial responses of stroke."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the post-ischemic neuroinflammation of stroke."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neuronal injury and repair gene programs of stroke."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the excitotoxic calcium-mediated neuronal injury of stroke."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Stroke-heart axis: acute stroke frequently raises cardiac troponin through neurogenic myocardial injury and takotsubo cardiomyopathy, and the elevation predicts worse outcomes, reflecting a bidirectional brain-heart interaction."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormonal risk: estrogen influences stroke risk in complex ways, with oral contraceptives and hormone therapy raising thrombotic risk while endogenous estrogen may be neuroprotective before menopause, shaping the sex differences in stroke."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Post-stroke immunosuppression: stroke induces a systemic immunosuppression with reduced monocyte MHC class II, impairing antigen presentation and predisposing to the pneumonia and infections that are a leading cause of post-stroke death."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Ischaemic oxygen deprivation: ischaemic stroke deprives brain tissue of oxygen, and the resulting energy failure (ATP and HIF already mapped) starts the excitotoxic cascade that kills the core while the penumbra survives on marginal perfusion."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Cardioembolic source: much ischaemic stroke is cardioembolic, from atrial fibrillation and other cardiac sources (troponin already mapped), so cardiac evaluation and anticoagulation are central to prevention."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Reparative microglia: IL-4 polarises microglia (already mapped) toward a reparative, anti-inflammatory phenotype that clears debris and supports recovery, so boosting this arm is explored to improve outcomes after stroke."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Ischaemic neuroinflammation: prostaglandins from the activated microglia (already mapped) and the cyclooxygenase pathway contribute to the secondary neuroinflammation of the infarct (IL-1 and TNF already mapped), and antiplatelet aspirin is central to prevention."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory recovery: the anti-inflammatory IL-10, with IL-4 (already mapped), restrains the damaging neuroinflammation after stroke and supports the reparative response, part of the immune balance shaping recovery."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "NMDA neuroprotection: magnesium blocks the NMDA receptor of the glutamate excitotoxicity (already mapped) driving neuronal death, and it has been trialled as a neuroprotectant, while hypomagnesaemia may worsen the ischaemic injury of stroke."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium and excitotoxic death: the glutamate (already mapped) excitotoxicity of the ischaemic penumbra floods the neurons with calcium, triggering the enzymatic cascades of neuronal death that neuroprotection aims to interrupt in stroke."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Cytotoxic oedema: the failure of the sodium-potassium pump as ATP (already mapped) runs out lets sodium and water flood the cells, causing the cytotoxic oedema (aquaporin-4 already mapped) and the spreading depolarisations (connexin43 already mapped) of stroke."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytic oedema and scar: the astrocytes swell in the cytotoxic oedema (aquaporin-4 already mapped) and later form the glial scar that limits repair, central to both the injury and the recovery after stroke."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Ferroptosis and haemorrhage: the iron-dependent lipid-peroxidation cell death (ferroptosis) of the ischaemic neurons, and the iron released by the haemoglobin breakdown after haemorrhagic stroke, drive the secondary neuronal injury."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Reparative type-2 arm: IL-13, with IL-4 (already mapped), supports the M2 microglial (already mapped) anti-inflammatory and reparative arm of the recovery after stroke."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and stroke: leptin links obesity to the stroke risk, and has neuroprotective and reparative actions on the ischaemic brain, part of the metabolic dimension of stroke."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Blood-brain barrier: the endothelial/BBB breakdown (aquaporin-4 and VEGF already mapped) drives the vasogenic oedema and the haemorrhagic transformation of the ischaemic stroke."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thrombus platelets: the platelets form the arterial thrombus (thrombin and fibrinogen already mapped) of the ischaemic stroke, the antiplatelet (aspirin, clopidogrel) target."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Excitotoxic calcium: the glutamate (already mapped)-driven calcium influx triggers the excitotoxic neuronal (already mapped) death of the ischaemic penumbra of stroke."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 post-stroke neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the post-ischaemic neuroinflammation (IL-1 and TNF already mapped, the microglia already mapped) of stroke."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Vascular-inflammatory adipokine: resistin, with leptin (already mapped), is a pro-inflammatory adipokine and a biomarker linked to the atherosclerotic (already mapped) stroke risk and outcome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension linking the metabolic-vascular state to the ischaemic stroke risk."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the post-stroke neuroinflammation and the systemic immune response of stroke."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune response after stroke."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the ischaemic cell death, contributes to the post-stroke neuroinflammation of stroke."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Reperfusion injury: the neutrophils, recruited into the ischaemic brain, drive the reperfusion injury and the NETosis that worsen the tissue damage and the no-reflow of stroke."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment and the complement-mediated injury of the ischaemic brain in stroke."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive neuroinflammation: the cytotoxic T cells (perforin pathway) infiltrate the ischaemic brain in the days after stroke, contributing to the delayed adaptive-immune injury and repair."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) generate the membrane-attack complex of the complement-mediated ischaemia-reperfusion injury of the brain in stroke."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated injury of the ischaemic brain in stroke."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Infiltrating myeloid cells: the blood-derived macrophages, with the resident microglia (already mapped), clear the debris and shape the injury-versus-repair balance of the ischaemic brain after stroke."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-vascular axis: TSLP, from ischaemic endothelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the post-stroke neuroinflammation of stroke."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-oedema axis: bradykinin, via the B2 receptors on brain endothelium, drives the post-ischaemic blood-brain-barrier opening and the vasogenic oedema of the ischaemic brain in stroke."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective cytokine: erythropoietin, via the EPOR on neurons and astrocytes (already mapped), reduces the infarct volume and the apoptosis of the ischaemic neurons in stroke."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "BBB-permeability mediator: histamine, from mast cells (already mapped) at the post-ischaemic blood-brain barrier, amplifies the vasogenic oedema and the neurogenic inflammation of the ischaemic penumbra in the acute and subacute phases of stroke."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Neuroprotective antioxidant: melatonin reduces ROS-driven ischaemia-reperfusion injury, attenuates the NLRP3-inflammasome (already mapped) and NF-κB (already mapped) activation, and modulates the post-stroke circadian disruption of stroke."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-complement and contact brake: C1-esterase inhibitor limits complement and bradykinin (already mapped) activation after ischaemia-reperfusion, reducing the BBB breakdown and the post-ischaemic oedema of the ischaemic brain in stroke."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Stroke testosterone: testosterone, via androgen receptors on neurons (already mapped) and microglia (already mapped), exerts neuroprotection; testosterone deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) post-ischaemic neuroinflammation of stroke."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Stroke serotonin: serotonin, via 5-HT receptors on neurons (already mapped) and astrocytes (already mapped), modulates ischaemic neuroinflammation; serotonin reuptake inhibitors reduce post-stroke depression and amplify the stroke recovery neuroplasticity axis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Stroke prolactin: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates post-ischaemic neuroprotection; hyperprolactinaemia amplifies the IL-6 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of post-ischaemic stroke."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Stroke oxytocin: oxytocin, via OXTR on neurons (already mapped) and microglia (already mapped), exerts anti-inflammatory neuroprotection; oxytocin deficiency amplifies the NLRP3 (already mapped) and IL-6 (already mapped) post-ischaemic neuroinflammatory cascade of stroke."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Stroke vasopressin: vasopressin, via V1aR on astrocytes (already mapped) and neurons (already mapped), modulates cerebral oedema and BBB permeability; vasopressin dysregulation amplifies the NLRP3 (already mapped) and NF-κB (already mapped) ischaemic injury of stroke."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Stroke selenium: selenium, as GPx in neurons (already mapped) and microglia (already mapped), scavenges ischaemia-reperfusion ROS; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of ischaemic stroke."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Stroke zinc: zinc cofactors NRF2 antioxidant defence in neurons (already mapped) and microglia (already mapped); zinc deficiency amplifies NF-κB (already mapped) and glutamate (already mapped) excitotoxicity and IL-6 (already mapped) neuroinflammation in stroke."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Stroke copper: copper-dependent SOD in neurons (already mapped) and microglia (already mapped) quenches ROS amplifying NF-κB (already mapped); copper deficiency amplifies glutamate (already mapped) excitotoxicity and IL-6 (already mapped) neuroinflammation in stroke."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Stroke iodine: iodine-dependent thyroid hormones modulate neurons (already mapped) and microglia (already mapped) neuroinflammatory tone; thyroid-hormone deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and glutamate (already mapped) excitotoxicity in stroke."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Stroke phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), sustains membrane gradients; phosphorus depletion amplifies NF-κB (already mapped) and glutamate (already mapped) excitotoxicity and IL-6 (already mapped) in stroke."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Stroke carbon: carbon, as metabolic backbone of neurons (already mapped) and microglia (already mapped), fuels neuronal energy metabolism; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and glutamate (already mapped) excitotoxicity in stroke."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Stroke chloride: chloride, via KCC2 in neurons (already mapped) and astrocytes (already mapped), regulates inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and glutamate (already mapped) excitotoxic cascade of stroke."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Stroke hydrogen: hydrogen, via redox homeostasis in neurons (already mapped) and microglia (already mapped), quenches ischaemic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and glutamate (already mapped) excitotoxicity of stroke."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Stroke nitrogen: nitric oxide from neurons (already mapped) and endothelial cells (already mapped) modulates cerebrovascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of stroke."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Stroke sulfur: hydrogen sulfide from neurons (already mapped) and endothelial cells (already mapped) modulates cerebrovascular tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Stroke PD-1: PD-1 checkpoint signalling in T-cells (already mapped) and microglia (already mapped) modulates neuroinflammatory tone; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Stroke glp-1: GLP-1 from macrophages (already mapped) and endothelial cells (already mapped) modulates cerebrovascular metabolic tone; glp-1 deficiency amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Stroke angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives acute neuroinflammation; angiotensin-ii excess amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Stroke wnt-beta-catenin: WNT/β-catenin on neurons (already mapped) and endothelial cells (already mapped) regulates blood-brain barrier repair; wnt-beta-catenin loss amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Stroke rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) promotes neuroinflammatory immune activation after stroke; rankl excess amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Stroke il-2: IL-2 from T-cells (already mapped) and microglia (already mapped) regulates post-stroke neuroinflammation; il-2 dysregulation amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Stroke fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) promotes post-stroke ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Stroke notch: Notch signalling in macrophages (already mapped) and endothelial cells (already mapped) regulates post-stroke cell fate; notch dysregulation amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Stroke igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes post-stroke neuronal survival; igf-1 dysregulation amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Stroke activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) regulates post-stroke immune-fibrotic balance; activin-a excess amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke."
---

# Stroke

## Overview

**Stroke** is the sudden onset of focal neurological deficit resulting from cerebrovascular disease — the **second leading cause of death globally** and the **leading cause of long-term adult disability**. Approximately **15 million strokes** occur annually worldwide, resulting in ~6 million deaths and leaving ~5 million people permanently disabled. The fundamental pathological event is either **interruption of blood flow** to a brain region (ischemic stroke, 87%) or **bleeding into the brain parenchyma or subarachnoid space** (hemorrhagic stroke, 13%).

**Classification:**
- **Ischemic stroke (87%):**
  - *Large artery atherothrombotic:* Stenosis/plaque rupture at carotid bifurcation, basilar artery, intracranial ICA → local thrombosis or artery-to-artery embolism (~25%)
  - *Cardioembolic:* Cardiac thrombi (AF, prosthetic valve, MI, endocarditis) → embolism to intracranial vessels (~25%)
  - *Small vessel lacunar:* Lipohyalinosis of penetrating arteries (lenticulostriate, pontine perforators) from chronic hypertension → small deep infarcts (<15 mm) (~25%)
  - *Cryptogenic (unknown cause):* (~25%); often occult AF (extended cardiac monitoring, implantable loop recorder)
  - *Other:* Arterial dissection, thrombophilia, sickle cell, CADASIL, vasculitis

- **Hemorrhagic stroke (13%):**
  - *Intracerebral hemorrhage (ICH):* Rupture of deep perforating arteries (hypertension-related) → hematoma in basal ganglia, thalamus, pons, cerebellum; or lobar hemorrhage from CAA (cerebral amyloid angiopathy, elderly) or vascular malformation (~10% of all strokes)
  - *Subarachnoid hemorrhage (SAH):* Rupture of berry aneurysm at Circle of Willis → sudden "thunderclap" headache; ~3% of all strokes but catastrophic mortality

**Time is brain:** ~1.9 million neurons die per minute during a large ischemic stroke. The fundamental principle of stroke management is **rapid reperfusion** within the therapeutic time window.

## Structure

### Ischemic penumbra and infarct core

The pathological anatomy of ischemic stroke defines treatment targets:

- **Infarct core:** Cerebral blood flow (CBF) <10-15 mL/100g/min → irreversible neuronal death within minutes; this tissue cannot be saved regardless of reperfusion; appears as DWI restriction on MRI (early), CT hypodensity (>6 hours)
- **Ischemic penumbra:** CBF 10-30 mL/100g/min → functionally impaired but structurally viable; survives for hours if reperfused; identified on MRI as DWI-PWI mismatch or CT perfusion (CBF/CBV mismatch); the therapeutic target of thrombolysis and thrombectomy
- **Oligemia:** CBF 30-50% of normal → mild dysfunction; recovers without intervention
- **Time evolution:** Core expands into penumbra at ~10% per hour without reperfusion; collateral circulation (leptomeningeal anastomoses) slows core expansion and extends the therapeutic window

**Cerebral autoregulation:**
Normal brain maintains CBF constant (50-150 mmHg MAP range) via autoregulation (myogenic + metabolic). Ischemia disrupts autoregulation → CBF becomes pressure-dependent → hypotension worsens ischemia → permissive hypertension (target SBP <180 mmHg post-tPA, ≤220 mmHg without tPA before 24h)

## Function

### Ischemic stroke pathophysiology: excitotoxic cascade

**The ischemic cascade** unfolds in minutes-to-hours [^powers-2019-aha-stroke]:

1. **Energy failure (minutes):** Blood flow cessation → glucose/O₂ deprivation → ATP synthesis stops → Na⁺/K⁺-ATPase fails → membrane depolarization → **anoxic depolarization**
2. **Glutamate excitotoxicity (minutes-hours):** Depolarization → vesicular glutamate release + reversal of glutamate transporters → massive extracellular glutamate → NMDA receptor activation → Ca²⁺ influx → Ca²⁺-mediated neurotoxicity cascade:
   - Phospholipase A2/C → arachidonic acid → ROS, prostaglandins
   - Calcineurin, calpain → cytoskeletal degradation
   - nNOS activation → NO + superoxide → peroxynitrite → DNA damage → PARP1 activation
   - Mitochondrial permeability transition → cytochrome c → caspase-9/3 → apoptosis (in penumbra)
3. **Peri-infarct depolarizations (spreading depression, hours):** Repetitive waves of depolarization propagating from infarct core → metabolic demand spikes → expand ischemic core; each depolarization → additional damage
4. **Neuroinflammation (hours-days):** Microglia activated → IL-1β, TNF-α, IL-6, MMPs → BBB breakdown → peripheral leukocyte infiltration → cerebral edema → secondary injury; also phagocytosis of debris (some beneficial for recovery)

### Hemorrhagic stroke

**Intracerebral hemorrhage:**
- Hematoma formation → mass effect → midline shift → herniation (early mortality)
- Perihematomal edema: plasma proteins (thrombin, hemoglobin) → inflammatory cascade → edema → surrounds hematoma (expands over 24-48 hours)
- **Hematoma expansion** (~20-30% of patients in first 24 hours): poor prognosis; coagulopathy, anticoagulant use, and liver disease are risk factors

**SAH:**
- Aneurysm rupture → blood in subarachnoid space → ICP spike → "thunderclap" headache
- Complications: rebleeding (highest risk in first 24h → early aneurysm securing), vasospasm (days 4-14 → delayed cerebral ischemia in ~30%), hydrocephalus

## Pathology

### Clinical presentation and diagnosis

**FAST + BE acronym:**
- **F**ace drooping (unilateral), **A**rm weakness (drift), **S**peech difficulty, **T**ime to call 911
- **B**alance loss, **E**yes (sudden vision change) added in BE-FAST

**Imaging protocol:**
1. Non-contrast CT (immediate): Rules out hemorrhage (hyperdense blood) vs. ischemia; early CT signs (loss of gray-white differentiation, insular ribbon sign)
2. CT angiography (CTA): Visualizes large vessel occlusion (LVO) → guides thrombectomy eligibility
3. CT perfusion (CTP): Maps core vs. penumbra → guides late-window (6-24h) thrombectomy
4. MRI DWI: Most sensitive for acute ischemia; DWI-PWI mismatch = penumbra

**NIHSS (NIH Stroke Scale):** 0-42 points; quantifies stroke severity across consciousness, gaze, visual fields, facial palsy, motor, ataxia, sensation, language, dysarthria, neglect; guides tPA candidacy and outcome prediction.

### Treatment [^hacke-2008-ecass3]

**Acute ischemic stroke — reperfusion:**

*IV alteplase (tPA) — NINDS and ECASS trials:*
- Dose: 0.9 mg/kg (max 90 mg); 10% IV bolus, remainder over 60 minutes
- Time window: ≤3.0 hours (NINDS, 1995): relative risk of good outcome 1.7×; ≤4.5 hours (ECASS-3, 2008): modest but significant benefit [^hacke-2008-ecass3]
- **Tenecteplase (TNK-tPA):** Single IV bolus (0.25 mg/kg); non-inferior to alteplase; increasingly preferred (AHA 2023 guidelines update)
- Contraindications: hemorrhage on CT, coagulopathy, recent surgery, uncontrolled hypertension (>185/110), blood glucose <50 or >400

*Mechanical thrombectomy (EVT):*
- Stent-retriever or aspiration catheter removes clot in M1/M2 MCA, ICA, basilar artery occlusion
- 0-6 hours (MR CLEAN, SWIFT PRIME, EXTEND-IA, ESCAPE): NNT ~3-5 for functional independence → strongest effect size in modern stroke trials
- 6-24 hours (DAWN, DEFUSE-3): Select patients with large penumbra by CTP/MRI → significant benefit (DAWN: 49% vs 13% functional independence at 90 days)
- Basilar artery occlusion: Treated up to 24 hours (BASICS trial, extended window based on collateral status)

**Secondary prevention:**
- Non-cardioembolic: Antiplatelet therapy (aspirin, clopidogrel, dual antiplatelet for 21 days post-TIA/minor stroke per POINT/CHANCE trials)
- Cardioembolic/AF: Oral anticoagulation (DOACs: rivaroxaban, apixaban, dabigatran — superior to warfarin for AF stroke prevention; start 1-14 days post-stroke depending on infarct size)
- Risk factor control: Statin (high-intensity), BP reduction, smoking cessation, diabetes management, sleep apnea treatment

**ICH management:**
- **Blood pressure:** Target SBP 130-140 mmHg within 2h (INTERACT-2: modestly improved outcomes)
- **Anticoagulant reversal:** Warfarin → vitamin K + 4-factor PCC (Kcentra); dabigatran → idarucizumab; rivaroxaban/apixaban → andexanet alfa
- **Surgical evacuation:** For cerebellar hemorrhage >3 cm with deterioration; selected supratentorial cases
- **FAST-MAG trial:** Field-administered magnesium sulfate — negative; multiple neuroprotection trials have failed

## Connections

- `targets` → **[Brain](../../06-organ/brain/README.md)** — stroke directly destroys brain tissue via ischemic excitotoxicity or hemorrhagic compression; 1.9 million neurons die per minute during large ischemic stroke; the ischemic penumbra is the therapeutic target of tPA and thrombectomy.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — hypertension is the dominant modifiable stroke risk factor; drives small vessel disease (lacunar infarcts), ICH, and accelerates atherosclerosis; BP lowering reduces recurrent stroke by 30-40%.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — eNOS-derived NO maintains cerebral vasodilation and platelet inhibition; ischemia depletes protective NO and activates nNOS → peroxynitrite neurotoxicity; the dual role of NO isoforms in stroke is therapeutically important.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — cardioembolic stroke (25-30%) arises from cardiac thrombi in AF, post-MI, and endocarditis; atrial fibrillation is the single most treatable cardioembolic risk factor (DOACs reduce AF stroke by ~64% vs warfarin by ~60%).
- `connects-to` → **[PCSK9](../../03-molecular/pcsk9/README.md)** — LDL-C-driven carotid atherosclerosis causes ischemic stroke via thromboembolism; PCSK9 inhibitors (evolocumab, alirocumab) reduce stroke risk ~25% in post-MI patients; very low LDL-C (<25 mg/dL) with PCSK9 inhibition does not impair cognition and reduces stroke incidence.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Thrombin generates fibrin clots in cerebral arteries → ischemic stroke; AF→ atrial thrombus → embolism → cardioembolic stroke; ICH → thrombin release → perihematomal inflammation and edema; dabigatran (direct thrombin inhibitor) and apixaban/rivaroxaban prevent AF-related stroke.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — SCD is the most common cause of childhood stroke (<10 years; cerebral vasculopathy from sickling → large vessel stenosis); transcranial Doppler (TCD) screening identifies high-risk patients; chronic transfusion (target HbS <30%) reduces stroke risk 92% (STOP trial).
- `connects-to` → **[Migraine](../migraine/README.md)** — migraine with aura (MA) confers 2× ischemic stroke risk; CSD-triggered spreading oligemia → ischemic cascade in vulnerable cortex; PFO prevalence higher in MA; oral contraceptives + MA + smoking multiplies stroke risk; CADASIL (NOTCH3) presents with MA + lacunar strokes.
- `connects-to` → **[Familial Hypercholesterolemia](../familial-hypercholesterolemia/README.md)** — FH accelerates carotid and cerebrovascular atherosclerosis; HeFH patients have elevated carotid intima-media thickness (cIMT) and higher stroke risk vs. general population; statin + PCSK9 inhibitor reduces cIMT progression and ischemic stroke incidence in FH cohorts.
- `prevented-by` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — Warfarin prevents AF-related ischemic stroke by 64% (Hart 2007); INR 2.0–3.0; preferred over DOACs for mechanical heart valves; antiphospholipid syndrome triple-positive: warfarin INR 3.0–4.0 (TRAPS trial confirmed DOACs inferior).
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs including ibuprofen increase ischemic stroke/MI risk ~1.3–1.5× via ↓ endothelial PGI₂; ibuprofen blocks aspirin irreversible COX-1 acetylation → ↓ cardioprotective antiplatelet effect; avoid in high cardiovascular risk patients.
- `treated-by` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — aspirin is first-line secondary stroke prevention after TIA/minor ischemic stroke; 300 mg loading dose reduces 90-day recurrence; irreversible platelet COX-1 blockade prevents atherothrombotic and cardioembolic thrombosis; contraindicated in hemorrhagic stroke.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Atherosclerosis is the dominant cause of ischemic stroke: plaques in the carotid and cerebral arteries rupture to form occlusive clots or shed emboli, so the lipid-driven disease behind heart attacks also kills brain tissue—treated by statins and antiplatelets.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Antiphospholipid syndrome is an important cause of stroke in the young: antiphospholipid antibodies make blood prothrombotic, causing arterial and venous clots, so an unexplained young stroke—especially with prior clots or pregnancy loss—warrants APS testing.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Stroke kills neurons through the ischemic cascade: loss of blood flow starves neurons of oxygen and glucose, triggering glutamate excitotoxicity, calcium overload, and death within minutes in the core—so time is brain, and rapid reperfusion salvages the penumbra.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes shape stroke outcome: after ischemia they swell and fail to clear glutamate, worsening excitotoxicity, then form the glial scar that both limits damage and impedes regeneration—so astrocyte responses help determine the size and recovery of the infarct.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate excitotoxicity is the core of stroke neuronal death: energy failure floods the synapse with glutamate, overactivating NMDA receptors and letting calcium pour in to kill neurons, so the excitatory transmitter becomes the executioner in the ischemic penumbra.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Type 2 diabetes roughly doubles stroke risk: chronic hyperglycemia accelerates atherosclerosis and small-vessel disease, and high glucose at stroke onset worsens infarct size and outcome—so glycemic control is central to stroke prevention.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets are central to ischemic stroke and its prevention: clot formation on a ruptured plaque occludes a cerebral artery, so antiplatelet drugs (aspirin, clopidogrel) are the cornerstone of preventing non-cardioembolic stroke.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Stroke is the leading cause of acquired nervous-system disability: sudden loss of blood flow kills neurons in minutes, and which functions are lost—speech, movement, vision—depends entirely on which part of the brain's circuitry the dead tissue served.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Stroke and venous thromboembolism share a prothrombotic basis and complicate each other: immobility after stroke raises DVT/PE risk, and a clot crossing a patent foramen ovale can cause paradoxical embolic stroke—so thromboprophylaxis is routine in stroke care.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Many strokes start in the heart: atrial fibrillation, valve disease, and a patent foramen ovale let clots form and travel to the brain (cardioembolic stroke), so finding the cardiac source guides anticoagulation to prevent the next stroke.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is the executioner in stroke: when ischemia depletes energy, neurons flood with calcium that activates enzymes destroying the cell—the excitotoxic cascade that turns minutes of lost blood flow into permanent brain damage.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia shape stroke's aftermath: the brain's resident immune cells swarm the infarct, first worsening injury with inflammation, then clearing debris and aiding repair—so tipping their balance toward repair is a target for limiting stroke damage.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Stroke's damage begins with failed sodium pumps: when blood flow stops, neurons can't power the Na/K-ATPase, so sodium and water flood in causing cytotoxic edema—the first step of the ischemic cascade before calcium and glutamate finish the job.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression follows stroke in up to a third of survivors: brain injury plus the disability and biochemical changes drive post-stroke depression, which slows rehabilitation and worsens outcomes—so screening and treating mood is part of stroke care.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Stroke kills oligodendrocytes and the myelin they maintain: white-matter ischemia destroys these myelinating cells, and their poor regeneration is why white-matter strokes leave lasting deficits—a target for remyelination and neuroprotection research.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Stroke is fundamentally an oxygen emergency: a blocked or burst vessel cuts the brain's oxygen supply, and because neurons have almost no reserve, the tissue begins to die within minutes—why 'time is brain' drives emergency care.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — The vessel lining is where most strokes begin: endothelial dysfunction and atherosclerosis spawn the clots that block brain arteries, and after a stroke the damaged endothelium lets the blood-brain barrier leak, worsening swelling.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — Stroke kills by starving cells of ATP: without oxygen and glucose, neurons cannot make ATP, so their ion pumps fail, calcium and sodium flood in, and the resulting excitotoxic cascade destroys the tissue in the ischemic core.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Stroke collapses the brain's potassium gradient: when energy fails, neurons leak potassium and depolarize in spreading waves that march across the tissue, recruiting the penumbra and enlarging the infarct.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Stroke turns synapses toxic: starved neurons dump glutamate that overexcites neighboring synapses, and this excitotoxic flood—through calcium overload—kills the cells the clot did not directly reach.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Stroke endangers the lungs through swallowing: damage to swallowing control lets food and saliva slip into the airway, so aspiration pneumonia is a leading cause of death in the weeks after a stroke.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Stroke care races on imaging: CT photons instantly separate a bleed from a clot, and MRI and perfusion scans map salvageable brain, deciding who gets clot-busting drugs or thrombectomy.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye warns of stroke: amaurosis fugax, a fleeting curtain of vision loss from a retinal-artery clot, is a TIA of the eye that flags carotid disease and impending stroke.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Recovery after stroke leans on BDNF: this growth factor drives the neuroplasticity that lets surviving brain rewire around the dead tissue, the molecular basis of rehabilitation gains.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy captures the dying neuron: starved of oxygen, it swells with cytotoxic edema as failing pumps let water and calcium flood in, and its mitochondria balloon — the ultrastructure of the excitotoxic cascade that kills brain tissue.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — The brain heals a stroke with a glial scar: astrocytes wall off the dead infarct in a dense gliosis, the central-nervous-system version of fibrosis that contains the damage but blocks the regrowth of axons through it.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — A stroke can bleed the stomach: the surge of stress drives acid-related Cushing ulcers, while damage to the swallowing centers brings the dysphagia that risks aspiration and demands careful feeding.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Reproductive hormones shape stroke risk: estrogen-containing contraception and pregnancy raise the clotting risk — sharply so with migraine aura — while eclampsia and postpartum cerebral angiopathy are direct obstetric causes of stroke.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies can clot the brain young: antiphospholipid antibodies are a major cause of stroke in the under-50s, driving the hypercoagulability that lodges clots in cerebral vessels even without atherosclerosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — A stroke can sever the brain's control of the bowel: damage to the pathways governing continence brings fecal incontinence or, with immobility and reduced intake, stubborn constipation during recovery.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Recovery is fought in the muscles: a stroke leaves hemiparesis, then spasticity and contractures, and disuse wastes the affected limbs — making physical rehabilitation the long, central work of regaining function.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Heart and brain trade blows: a clot from a fibrillating or infarcted heart causes cardioembolic stroke, while the stroke itself can stun the cardiomyocytes — neurogenic Takotsubo and arrhythmia from the catecholamine surge.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Lowering LDL guards against the next one: high cholesterol builds the carotid and cerebral plaques that throw clots, so statins and other LDL-lowering drugs are a cornerstone of preventing ischemic stroke.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — Clotting genes cause stroke in the young: inherited thrombophilias raise the risk of cerebral venous thrombosis and, via a patent foramen, paradoxical arterial stroke, so an unexplained young stroke prompts a hypercoagulability workup.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The artery wall's muscle shapes the stroke: vascular smooth muscle builds the cerebral plaques and, in small-vessel disease and vasospasm after hemorrhage, its dysfunction narrows the arteries that feed the brain.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — A stroke can leave the brain in pain: damage to the thalamus or sensory pathways causes central post-stroke pain, a relentless neuropathic burning on the paralyzed side that is hard to treat.
- `connects-to` → **[Aquaporin-4](../../03-molecular/aquaporin-4/README.md)** — Brain swelling after stroke runs through aquaporin-4: this astrocyte water channel drives the cytotoxic edema that follows ischemia, and its role makes it a target for limiting the dangerous post-stroke brain swelling.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The heart and brain share the clot risk: heart failure and the atrial fibrillation that accompanies it throw cardioembolic clots to the brain, while a large stroke can in turn stun the heart — a two-way cardio-cerebral link.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Failing kidneys raise the stroke risk: chronic kidney disease accelerates vascular disease and disturbs clotting, increasing both ischemic and hemorrhagic stroke while complicating the anticoagulation used to prevent them.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Reperfusion ignites neuroinflammation through NF-κB: after the clot, NF-κB activation in microglia and the injured brain drives the cytokine surge and edema that extend the infarct in the hours after stroke.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Stroke scars the cortex into a seizure focus: it is the leading cause of new-onset epilepsy in older adults, the gliotic infarct rim becoming an irritable focus for post-stroke seizures.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The aftermath opens the door to infection: stroke brings dysphagia, aspiration and immobility, so pneumonia and urinary infection — and the sepsis they can become — are common, dangerous early complications.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Paralysis melts the bone: disuse of a hemiparetic limb, immobility and low vitamin D after stroke accelerate bone loss on the affected side, raising the risk of fractures from the falls stroke also causes.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Fear shadows recovery: post-stroke anxiety is common alongside depression, driven both by the direct brain injury and by the fear of recurrence and lost independence, and it impedes rehabilitation.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Small-vessel strokes can mimic it: cumulative infarcts in the basal ganglia produce vascular parkinsonism — a lower-body, gait-predominant syndrome that resembles and overlaps with Parkinson's disease.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — It impairs the swallow and seeds the lung: stroke commonly causes dysphagia, and the resulting aspiration pneumonia — often pneumococcal — is a leading early complication and cause of death.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Paralysis and immobility break down the skin: hemiparesis and bedbound recovery after stroke predispose to pressure ulcers over insensate, poorly moved skin that then heal slowly.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Infarcts accelerate cognitive decline: stroke causes vascular dementia directly and lowers the threshold for Alzheimer-type dementia, the two often coexisting as mixed dementia in survivors.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Swallowing failure floods the lungs: stroke causes dysphagia and impaired cough, so aspiration pneumonia is a leading early complication, and large strokes can trigger neurogenic pulmonary oedema.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It disrupts the whole gut from mouth to bowel: stroke-related dysphagia forces modified diets or PEG feeding, and immobility and autonomic change bring constipation and faecal incontinence.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It unsettles the bladder and threatens the kidneys: stroke commonly causes urinary incontinence or retention with infection, and contrast for imaging and thrombectomy can injure the kidneys.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It disturbs glucose and sodium: stress hyperglycaemia worsens stroke outcomes, and hypothalamic or pituitary strokes cause SIADH or cerebral salt wasting with dangerous sodium shifts.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Brain injury suppresses immunity: stroke-induced immunodepression in the days afterward raises the risk of pneumonia and urinary infection, a major driver of early mortality.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Paralysis and immobility break the skin: pressure ulcers over the sacrum and heels are a major preventable complication after a disabling stroke.
- `connects-to` → **[Statins](../../../03-medicine/01-modern/04-cardio/statins/README.md)** — Lipid-lowering prevents the next one: high-intensity statins reduce recurrent ischaemic stroke by stabilising atherosclerotic plaque, a cornerstone of secondary prevention.
- `connects-to` → **[ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — Blood pressure is the dominant modifiable risk: lowering it with ACE inhibitors and other antihypertensives is the single most effective way to prevent both ischaemic and haemorrhagic stroke.
- `connects-to` → **[Varicella-zoster virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — A virus that inflames cerebral arteries: varicella-zoster can cause a vasculopathy of the brain arteries leading to stroke, weeks after shingles and especially in children or the immunocompromised.
- `connects-to` → **[SARS-CoV-2](../../../02-pathogen/01-viruses/sars-cov-2/README.md)** — Infection raises the risk: COVID-19 promotes a hypercoagulable, inflamed state that increases ischaemic stroke, including large-vessel strokes in younger patients.
- `connects-to` → **[Calcium-Channel Blockers](../../../03-medicine/01-modern/04-cardio/calcium-channel-blockers/README.md)** — A drug for the bleeding kind: the calcium-channel blocker nimodipine reduces delayed cerebral ischaemia from vasospasm after subarachnoid haemorrhage, improving outcomes.
- `connects-to` → **[Obesity](../obesity/README.md)** — A modifiable driver: obesity raises stroke risk through hypertension, diabetes, atrial fibrillation and atherosclerosis, making weight central to prevention.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It begins in the vessel wall: most ischaemic strokes arise from atherosclerotic plaque in the carotid and intracranial arteries, and haemorrhagic stroke from arterial-wall rupture in hypertension or amyloid angiopathy.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — The heart's rhythm throws clots: atrial fibrillation, a disorder of the cardiac conduction system, lets thrombus form in the left atrial appendage and embolise to the brain — the leading cause of cardioembolic stroke.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — It is selectively vulnerable: the hippocampus is exquisitely sensitive to ischaemia, so global hypoperfusion and recurrent strokes injure it preferentially, driving the memory loss of vascular cognitive impairment.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Thalassaemia raises stroke risk: chronic haemolysis, a hypercoagulable state and post-splenectomy thrombocytosis predispose to ischaemic stroke, especially in non-transfusion-dependent thalassaemia.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — The cardioembolic source: clots forming on a fibrillating atrium, a damaged valve or infective endocarditis on the endocardium break off and lodge in cerebral arteries, a leading cause of ischaemic stroke.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Too-thick blood clots the brain: the raised red-cell mass and platelet count of polycythaemia vera cause hyperviscosity and thrombosis, making stroke a presenting feature.
- `connects-to` → **[Giant Cell Arteritis](../giant-cell-arteritis/README.md)** — Vasculitic stroke: giant-cell arteritis and other large-vessel vasculitides can occlude cerebral and ophthalmic arteries, causing stroke and sudden blindness that prompt steroids can prevent.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Infection-triggered clots: COVID-19 raises stroke risk through a hypercoagulable, inflammatory state, sometimes causing large-vessel occlusion even in younger patients.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — A cardioembolic source: a left-ventricular mural thrombus after myocardial infarction or in cardiomyopathy can dislodge from the myocardium and embolise to the brain, causing cardioembolic stroke.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Aspiration pneumonia: stroke commonly impairs swallowing, and aspirated material seeds the alveolus with infection—a leading cause of post-stroke morbidity and death.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Vasculitic stroke: ANCA-associated and other CNS vasculitides inflame and occlude cerebral arteries, causing ischaemic stroke through a non-atherosclerotic mechanism.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Haemorrhagic stroke: severe factor VIII deficiency predisposes to spontaneous intracranial haemorrhage, a leading cause of death in haemophilia and the bleeding counterpart of ischaemic stroke.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Ischaemic response: HIF-1α stabilised in the hypoxic penumbra after stroke drives both protective angiogenesis and harmful inflammation, shaping the fate of salvageable brain tissue.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuroinflammatory injury: IL-1β released by activated microglia after ischaemia expands the infarct, and IL-1 blockade is under investigation to limit post-stroke brain damage.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Post-stroke inflammation: IL-6 surges after stroke, both reflecting infarct size and contributing to the systemic inflammatory response that worsens outcome.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Ischaemic inflammasome: NLRP3 inflammasome activation in microglia after ischaemia matures IL-1β and drives pyroptotic cell death, expanding the infarct in the hours after stroke onset.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte infiltration: CCL2 released from the ischaemic brain recruits blood monocytes across the disrupted blood-brain barrier, shaping the secondary inflammatory injury and repair after stroke.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Repair and barrier: VEGF drives post-stroke angiogenesis and neurovascular repair but also opens the blood-brain barrier acutely, a double-edged contributor to oedema and recovery.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — In the salvageable ischemic penumbra, neurons die more slowly by caspase-3-mediated apoptosis rather than the necrosis of the core—the delayed, potentially interruptible cell death that neuroprotection strategies target.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — DAMPs released by ischemic brain tissue engage microglial TLR4, igniting the NF-κB-driven inflammation that worsens ischemia-reperfusion injury after stroke and after the recanalization of thrombectomy.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Fibrinogen is converted by thrombin into the fibrin clot of ischemic stroke, the substrate of thrombolysis with tPA that cleaves fibrin to dissolve the occlusion and restore cerebral perfusion within the treatment window.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Glutamate flooding the ischemic core opens NMDA channels to a lethal calcium influx, and the resulting calcium overload activates proteases and destroys mitochondria—the final common pathway of neuronal death in the stroke penumbra.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — When blood flow is restored by thrombolysis or thrombectomy, xanthine-oxidase-derived reactive oxygen species burst into the reoxygenated tissue, the oxidative reperfusion injury that can extend the damage the clot began.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 released after subarachnoid hemorrhage is a key driver of the delayed cerebral vasospasm that causes secondary ischemic stroke days after the initial bleed, a major cause of poor outcome.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Reperfusion after ischemic stroke generates a burst of reactive oxygen species, and the NRF2 antioxidant response is a key endogenous defense protecting the salvageable penumbra.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Astrocytic connexin-43 gap junctions and hemichannels propagate peri-infarct spreading depolarizations and release glutamate and ATP, expanding the ischemic penumbra into completed infarct.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation after stroke contributes to the secondary neuroinflammatory injury, while also influencing the neural repair and plasticity of recovery.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Ischemic damage-associated molecular patterns engage TLR4 signaling through MyD88 to NF-κB (TLR4 and NF-κB already mapped), igniting the sterile neuroinflammation that expands the infarct in the hours after stroke.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α from activated microglia amplifies blood-brain-barrier breakdown and neuronal death in the ischemic penumbra, a key cytokine driver of secondary injury after stroke.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) drives the neuroplasticity and axonal sprouting that underpin functional recovery in the weeks after stroke.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT prosurvival signaling protects penumbral neurons after ischemic stroke, a target for neuroprotection.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 is strongly induced after ischemic stroke, driving the post-stroke neuroinflammatory response.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3-driven reactive astrogliosis shapes glial-scar formation and tissue repair after stroke.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Mitochondrial and nuclear DNA released by ischemic cell death engages cGAS-STING, driving the sterile neuroinflammation of the post-stroke penumbra.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling drives the interferon-responsive microglial activation that shapes the inflammatory injury after stroke.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling contributes to the neuroprotective and tissue-repair responses that follow the acute ischemic injury of stroke.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the neuronal oxidative-stress and autophagy responses to the ischemia-reperfusion injury of stroke.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by infiltrating myeloid cells amplify the post-ischemic neuroinflammation of stroke.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling participates in both the excitotoxic neuronal injury and the reparative neuroplasticity that follow stroke.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β activation contributes to the neuronal apoptosis and blood-brain-barrier injury of ischemic stroke, a target for neuroprotection.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) mediates the neuronal survival and pro-recovery pathways in stroke.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK signaling, activated by the energy crisis of cerebral ischemia, shapes the metabolic and autophagic response to stroke.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal survival and injury responses to the ischemic and reperfusion stress of stroke.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the blood-brain-barrier disruption and excitotoxic injury of stroke.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte infiltration contributes to the post-ischemic neuroinflammation and modulates recovery after stroke.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the neuronal-injury and repair responses of stroke.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neural-progenitor mobilization and post-stroke neurovascular repair of stroke.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory and reparative microglial responses of stroke.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the post-ischemic neuroinflammation of stroke.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the neuronal injury and repair gene programs of stroke.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the excitotoxic calcium-mediated neuronal injury of stroke.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Stroke-heart axis: acute stroke frequently raises cardiac troponin through neurogenic myocardial injury and takotsubo cardiomyopathy, and the elevation predicts worse outcomes, reflecting a bidirectional brain-heart interaction.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Hormonal risk: estrogen influences stroke risk in complex ways, with oral contraceptives and hormone therapy raising thrombotic risk while endogenous estrogen may be neuroprotective before menopause, shaping the sex differences in stroke.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Post-stroke immunosuppression: stroke induces a systemic immunosuppression with reduced monocyte MHC class II, impairing antigen presentation and predisposing to the pneumonia and infections that are a leading cause of post-stroke death.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Ischaemic oxygen deprivation: ischaemic stroke deprives brain tissue of oxygen, and the resulting energy failure (ATP and HIF already mapped) starts the excitotoxic cascade that kills the core while the penumbra survives on marginal perfusion.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Cardioembolic source: much ischaemic stroke is cardioembolic, from atrial fibrillation and other cardiac sources (troponin already mapped), so cardiac evaluation and anticoagulation are central to prevention.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Reparative microglia: IL-4 polarises microglia (already mapped) toward a reparative, anti-inflammatory phenotype that clears debris and supports recovery, so boosting this arm is explored to improve outcomes after stroke.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Ischaemic neuroinflammation: prostaglandins from the activated microglia (already mapped) and the cyclooxygenase pathway contribute to the secondary neuroinflammation of the infarct (IL-1 and TNF already mapped), and antiplatelet aspirin is central to prevention.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory recovery: the anti-inflammatory IL-10, with IL-4 (already mapped), restrains the damaging neuroinflammation after stroke and supports the reparative response, part of the immune balance shaping recovery.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — NMDA neuroprotection: magnesium blocks the NMDA receptor of the glutamate excitotoxicity (already mapped) driving neuronal death, and it has been trialled as a neuroprotectant, while hypomagnesaemia may worsen the ischaemic injury of stroke.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium and excitotoxic death: the glutamate (already mapped) excitotoxicity of the ischaemic penumbra floods the neurons with calcium, triggering the enzymatic cascades of neuronal death that neuroprotection aims to interrupt in stroke.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Cytotoxic oedema: the failure of the sodium-potassium pump as ATP (already mapped) runs out lets sodium and water flood the cells, causing the cytotoxic oedema (aquaporin-4 already mapped) and the spreading depolarisations (connexin43 already mapped) of stroke.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytic oedema and scar: the astrocytes swell in the cytotoxic oedema (aquaporin-4 already mapped) and later form the glial scar that limits repair, central to both the injury and the recovery after stroke.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Ferroptosis and haemorrhage: the iron-dependent lipid-peroxidation cell death (ferroptosis) of the ischaemic neurons, and the iron released by the haemoglobin breakdown after haemorrhagic stroke, drive the secondary neuronal injury.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Reparative type-2 arm: IL-13, with IL-4 (already mapped), supports the M2 microglial (already mapped) anti-inflammatory and reparative arm of the recovery after stroke.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and stroke: leptin links obesity to the stroke risk, and has neuroprotective and reparative actions on the ischaemic brain, part of the metabolic dimension of stroke.
- `connects-to` → **[Endothelial cell](../../04-cellular/endothelial-cell/README.md)** — Blood-brain barrier: the endothelial/BBB breakdown (aquaporin-4 and VEGF already mapped) drives the vasogenic oedema and the haemorrhagic transformation of the ischaemic stroke.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thrombus platelets: the platelets form the arterial thrombus (thrombin and fibrinogen already mapped) of the ischaemic stroke, the antiplatelet (aspirin, clopidogrel) target.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Excitotoxic calcium: the glutamate (already mapped)-driven calcium influx triggers the excitotoxic neuronal (already mapped) death of the ischaemic penumbra of stroke.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 post-stroke neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the post-ischaemic neuroinflammation (IL-1 and TNF already mapped, the microglia already mapped) of stroke.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Vascular-inflammatory adipokine: resistin, with leptin (already mapped), is a pro-inflammatory adipokine and a biomarker linked to the atherosclerotic (already mapped) stroke risk and outcome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension linking the metabolic-vascular state to the ischaemic stroke risk.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the post-stroke neuroinflammation and the systemic immune response of stroke.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune response after stroke.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the ischaemic cell death, contributes to the post-stroke neuroinflammation of stroke.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Reperfusion injury: the neutrophils, recruited into the ischaemic brain, drive the reperfusion injury and the NETosis that worsen the tissue damage and the no-reflow of stroke.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment and the complement-mediated injury of the ischaemic brain in stroke.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive neuroinflammation: the cytotoxic T cells (perforin pathway) infiltrate the ischaemic brain in the days after stroke, contributing to the delayed adaptive-immune injury and repair.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) generate the membrane-attack complex of the complement-mediated ischaemia-reperfusion injury of the brain in stroke.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the complement-mediated injury of the ischaemic brain in stroke.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Infiltrating myeloid cells: the blood-derived macrophages, with the resident microglia (already mapped), clear the debris and shape the injury-versus-repair balance of the ischaemic brain after stroke.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-vascular axis: TSLP, from ischaemic endothelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the post-stroke neuroinflammation of stroke.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-oedema axis: bradykinin, via the B2 receptors on brain endothelium, drives the post-ischaemic blood-brain-barrier opening and the vasogenic oedema of the ischaemic brain in stroke.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective cytokine: erythropoietin, via the EPOR on neurons and astrocytes (already mapped), reduces the infarct volume and the apoptosis of the ischaemic neurons in stroke.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — BBB-permeability mediator: histamine, from mast cells (already mapped) at the post-ischaemic blood-brain barrier, amplifies the vasogenic oedema and the neurogenic inflammation of the ischaemic penumbra in the acute and subacute phases of stroke.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Neuroprotective antioxidant: melatonin reduces ROS-driven ischaemia-reperfusion injury, attenuates the NLRP3-inflammasome (already mapped) and NF-κB (already mapped) activation, and modulates the post-stroke circadian disruption of stroke.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-complement and contact brake: C1-esterase inhibitor limits complement and bradykinin (already mapped) activation after ischaemia-reperfusion, reducing the BBB breakdown and the post-ischaemic oedema of the ischaemic brain in stroke.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Stroke testosterone: testosterone, via androgen receptors on neurons (already mapped) and microglia (already mapped), exerts neuroprotection; testosterone deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) post-ischaemic neuroinflammation of stroke.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Stroke serotonin: serotonin, via 5-HT receptors on neurons (already mapped) and astrocytes (already mapped), modulates ischaemic neuroinflammation; serotonin reuptake inhibitors reduce post-stroke depression and amplify the stroke recovery neuroplasticity axis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Stroke prolactin: prolactin, via PRLR on neurons (already mapped) and microglia (already mapped), modulates post-ischaemic neuroprotection; hyperprolactinaemia amplifies the IL-6 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of post-ischaemic stroke.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Anti-inflammatory neuroprotection: oxytocin, via OXTR on neurons (already mapped) and microglia (already mapped), exerts anti-inflammatory neuroprotection; oxytocin deficiency amplifies the NLRP3 (already mapped) and IL-6 (already mapped) post-ischaemic neuroinflammatory cascade of stroke.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Cerebral oedema modulator: vasopressin, via V1aR on astrocytes (already mapped) and neurons (already mapped), modulates cerebral oedema and BBB permeability; vasopressin dysregulation amplifies the NLRP3 (already mapped) and NF-κB (already mapped) ischaemic injury of stroke.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Ischaemia-reperfusion antioxidant: selenium, as GPx in neurons (already mapped) and microglia (already mapped), scavenges ischaemia-reperfusion ROS; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) neuroinflammatory cascade of ischaemic stroke.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Stroke zinc: zinc cofactors NRF2 antioxidant defence in neurons (already mapped) and microglia (already mapped); zinc deficiency amplifies NF-κB (already mapped) and glutamate (already mapped) excitotoxicity and IL-6 (already mapped) neuroinflammation in stroke.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Stroke copper: copper-dependent SOD in neurons (already mapped) and microglia (already mapped) quenches ROS amplifying NF-κB (already mapped); copper deficiency amplifies glutamate (already mapped) excitotoxicity and IL-6 (already mapped) neuroinflammation in stroke.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Stroke iodine: iodine-dependent thyroid hormones modulate neurons (already mapped) and microglia (already mapped) neuroinflammatory tone; thyroid-hormone deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and glutamate (already mapped) excitotoxicity in stroke.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Stroke phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and microglia (already mapped), sustains membrane gradients; phosphorus depletion amplifies NF-κB (already mapped) and glutamate (already mapped) excitotoxicity and IL-6 (already mapped) in stroke.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Stroke carbon: carbon, as metabolic backbone of neurons (already mapped) and microglia (already mapped), fuels neuronal energy metabolism; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and glutamate (already mapped) excitotoxicity in stroke.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Stroke chloride: chloride, via KCC2 in neurons (already mapped) and astrocytes (already mapped), regulates inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and glutamate (already mapped) excitotoxic cascade of stroke.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Stroke hydrogen: hydrogen, via redox homeostasis in neurons (already mapped) and microglia (already mapped), quenches ischaemic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and glutamate (already mapped) excitotoxicity of stroke.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Stroke nitrogen: nitric oxide from neurons (already mapped) and endothelial cells (already mapped) modulates cerebrovascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of stroke.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Stroke sulfur: hydrogen sulfide from neurons (already mapped) and endothelial cells (already mapped) modulates cerebrovascular tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of stroke.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Stroke PD-1: PD-1 checkpoint signalling in T-cells (already mapped) and microglia (already mapped) modulates neuroinflammatory tone; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of stroke.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Stroke glp-1: GLP-1 from macrophages (already mapped) and endothelial cells (already mapped) modulates cerebrovascular metabolic tone; glp-1 deficiency amplifies NF-κB (already mapped) and TNF-α (already mapped) and Glutamate (already mapped) cascade of stroke.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Stroke angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives acute neuroinflammation; angiotensin-ii excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and Glutamate (already mapped) cascade of stroke.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Stroke wnt-beta-catenin: WNT/β-catenin on neurons (already mapped) and endothelial cells (already mapped) regulates blood-brain barrier repair; wnt-beta-catenin loss amplifies NF-κB (already mapped) and TNF-α (already mapped) and Glutamate (already mapped) cascade of stroke.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Stroke rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) promotes neuroinflammatory immune activation after stroke; rankl excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and Glutamate (already mapped) cascade of stroke.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Stroke il-2: IL-2 from T-cells (already mapped) and microglia (already mapped) regulates post-stroke neuroinflammation; il-2 dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and Glutamate (already mapped) cascade of stroke.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Stroke fibronectin: fibronectin in macrophages (already mapped) and endothelial cells (already mapped) promotes post-stroke ECM remodelling; fibronectin excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and Glutamate (already mapped) cascade of stroke.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Stroke notch: Notch signalling in macrophages (already mapped) and endothelial cells (already mapped) regulates post-stroke cell fate; notch dysregulation amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Stroke igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes post-stroke neuronal survival; igf-1 dysregulation amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Stroke activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) regulates post-stroke immune-fibrotic balance; activin-a excess amplifies nf-kb (already mapped) and tnf-alpha (already mapped) and glutamate (already mapped) cascade of stroke.

[^powers-2019-aha-stroke]: Powers WJ, Rabinstein AA, Ackerson T, et al. Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update to the 2018 Guidelines. *Stroke.* 2019;50(12):e344-e418. [doi:10.1161/STR.0000000000000211](https://doi.org/10.1161/STR.0000000000000211) · [PubMed 31662037](https://pubmed.ncbi.nlm.nih.gov/31662037/)
[^feigin-2021-gbd-stroke]: Feigin VL, Krishnamurthi RV, Parmar P, et al. Update on the Global Burden of Ischemic and Hemorrhagic Stroke in 1990-2013. *Neuroepidemiology.* 2015;45(3):161-176. [doi:10.1159/000441085](https://doi.org/10.1159/000441085) · [PubMed 26505981](https://pubmed.ncbi.nlm.nih.gov/26505981/)
[^hacke-2008-ecass3]: Hacke W, Kaste M, Bluhmki E, et al. Thrombolysis with alteplase 3 to 4.5 hours after acute ischemic stroke. *N Engl J Med.* 2008;359(13):1317-1329. [doi:10.1056/NEJMoa0804656](https://doi.org/10.1056/NEJMoa0804656) · [PubMed 18815396](https://pubmed.ncbi.nlm.nih.gov/18815396/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
