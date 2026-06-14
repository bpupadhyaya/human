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

[^powers-2019-aha-stroke]: Powers WJ, Rabinstein AA, Ackerson T, et al. Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update to the 2018 Guidelines. *Stroke.* 2019;50(12):e344-e418. [doi:10.1161/STR.0000000000000211](https://doi.org/10.1161/STR.0000000000000211) · [PubMed 31662037](https://pubmed.ncbi.nlm.nih.gov/31662037/)
[^feigin-2021-gbd-stroke]: Feigin VL, Krishnamurthi RV, Parmar P, et al. Update on the Global Burden of Ischemic and Hemorrhagic Stroke in 1990-2013. *Neuroepidemiology.* 2015;45(3):161-176. [doi:10.1159/000441085](https://doi.org/10.1159/000441085) · [PubMed 26505981](https://pubmed.ncbi.nlm.nih.gov/26505981/)
[^hacke-2008-ecass3]: Hacke W, Kaste M, Bluhmki E, et al. Thrombolysis with alteplase 3 to 4.5 hours after acute ischemic stroke. *N Engl J Med.* 2008;359(13):1317-1329. [doi:10.1056/NEJMoa0804656](https://doi.org/10.1056/NEJMoa0804656) · [PubMed 18815396](https://pubmed.ncbi.nlm.nih.gov/18815396/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
