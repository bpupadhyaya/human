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

[^powers-2019-aha-stroke]: Powers WJ, Rabinstein AA, Ackerson T, et al. Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update to the 2018 Guidelines. *Stroke.* 2019;50(12):e344-e418. [doi:10.1161/STR.0000000000000211](https://doi.org/10.1161/STR.0000000000000211) · [PubMed 31662037](https://pubmed.ncbi.nlm.nih.gov/31662037/)
[^feigin-2021-gbd-stroke]: Feigin VL, Krishnamurthi RV, Parmar P, et al. Update on the Global Burden of Ischemic and Hemorrhagic Stroke in 1990-2013. *Neuroepidemiology.* 2015;45(3):161-176. [doi:10.1159/000441085](https://doi.org/10.1159/000441085) · [PubMed 26505981](https://pubmed.ncbi.nlm.nih.gov/26505981/)
[^hacke-2008-ecass3]: Hacke W, Kaste M, Bluhmki E, et al. Thrombolysis with alteplase 3 to 4.5 hours after acute ischemic stroke. *N Engl J Med.* 2008;359(13):1317-1329. [doi:10.1056/NEJMoa0804656](https://doi.org/10.1056/NEJMoa0804656) · [PubMed 18815396](https://pubmed.ncbi.nlm.nih.gov/18815396/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
