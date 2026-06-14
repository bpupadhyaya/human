---
schema: human-scale-entry/v1
id: migraine
name: Migraine
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Migraine (1.1B affected; #2 cause of disability) is a neurovascular disorder with unilateral throbbing headache, nausea, and photophobia; CGRP-mediated trigeminovascular activation drives pain; triptans (5-HT1B/D agonists) and anti-CGRP mAbs are first-line treatments."
aliases: ["migraine", "migraine with aura", "migraine without aura", "hemiplegic migraine", "chronic migraine", "episodic migraine", "trigeminovascular", "cortical spreading depression", "CGRP migraine", "triptan", "sumatriptan"]
sources:
  - id: gbd-2016-migraine-burden
    type: peer-reviewed
    cite: "GBD 2016 Headache Collaborators. Global, regional, and national burden of migraine and tension-type headache, 1990-2016: a systematic analysis for the Global Burden of Disease Study 2016. Lancet Neurol. 2018;17(11):954-976."
    doi: "10.1016/S1474-4422(18)30322-3"
    pmid: "30353868"
    url: "https://doi.org/10.1016/S1474-4422(18)30322-3"
    accessed: "2026-06-08"
  - id: goadsby-2002-migraine-review
    type: peer-reviewed
    cite: "Goadsby PJ, Lipton RB, Ferrari MD. Migraine — current understanding and treatment. N Engl J Med. 2002;346(4):257-270."
    doi: "10.1056/NEJMra010917"
    pmid: "11807151"
    url: "https://doi.org/10.1056/NEJMra010917"
    accessed: "2026-06-08"
  - id: dodick-2018-erenumab-arise
    type: peer-reviewed
    cite: "Dodick DW, Ashina M, Brandes JL, et al. ARISE: A Phase 3 randomized trial of erenumab for episodic migraine. Cephalalgia. 2018;38(6):1026-1037."
    doi: "10.1177/0333102418759786"
    pmid: "29471679"
    url: "https://doi.org/10.1177/0333102418759786"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "CGRP released from trigeminal C-fibers drives dural vasodilation and neurogenic inflammation; plasma CGRP rises during migraine and normalizes after successful triptan treatment; anti-CGRP mAbs and gepants block CGRP signaling for prevention and acute treatment."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Triptans (5-HT1B/D agonists) are mainstay acute migraine therapy — constrict dural vessels and inhibit trigeminal CGRP release; lasmiditan (5-HT1F ditan) avoids vasoconstriction; low interictal serotonin may prime trigeminovascular sensitization."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Migraine involves cortical spreading depression (CSD) as the aura generator in occipital cortex; hypothalamus drives prodromal symptoms; pain localizes to TNC and thalamus; PET identifies a brainstem migraine generator in dorsal raphe and PAG."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Migraine with aura (MA) confers 2× ischemic stroke risk; CSD-triggered spreading oligemia → ischemic cascade in vulnerable cortex; PFO prevalence higher in MA; oral contraceptives + MA + smoking multiplies stroke risk; CADASIL (NOTCH3) presents with MA + lacunar strokes."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "NO triggers cortical spreading depression (CSD); nitroglycerin (GTN) reliably provokes migraine attacks — the GTN model; NO-driven vasodilation sensitizes trigeminovascular nociceptors; triptans reduce NO-mediated dilation; iNOS upregulated in CSD-affected cortex."
  - target: 01-human/03-molecular/scn1a
    relation: connects-to
    note: "SCN1A (Nav1.1) gain-of-function → FHM3 (familial hemiplegic migraine type 3); loss-of-function → Dravet syndrome (epilepsy); both share cortical hyperexcitability; FHM3 SCN1A variants increase persistent Na⁺ current → lower CSD threshold."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Migraine and epilepsy are comorbid disorders of cortical hyperexcitability — migraineurs have 2-3× the epilepsy risk — sharing mechanisms like cortical spreading depression and SCN1A channel mutations (FHM3 vs Dravet); valproate and topiramate prevent both."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen shapes migraine: the 3:1 female predominance and menstrual migraine reflect attacks triggered by the perimenstrual estrogen drop, which lowers the trigeminovascular threshold; this is also why oral contraceptives plus migraine-with-aura sharply raise stroke risk."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Cortical spreading depression — the wave behind migraine aura — is not purely neuronal: astrocytes propagate it through calcium waves and gap junctions and shape it by buffering the massive extracellular potassium and glutamate the depolarizing front releases."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Migraine and fibromyalgia frequently co-occur and share central sensitization: both feature amplified pain processing, failed descending inhibition and CGRP/serotonin involvement, so the comorbidity worsens disability, and SNRIs and anti-CGRP antibodies are studied across both."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Migraine and insomnia are bidirectionally linked through shared hypothalamic and brainstem circuitry: poor sleep is a common migraine trigger while migraine disrupts sleep, both involve orexin and serotonergic systems, and treating insomnia (CBT-I) reduces headache frequency."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Migraine aura is a neuronal event: cortical spreading depression—a slow wave of neuronal and glial depolarization then suppression—sweeps the cortex producing visual aura and activating trigeminal pain pathways; neuronal hyperexcitability underlies susceptibility."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Migraine and neuropathic pain share central sensitization and CGRP signaling: trigeminovascular activation amplifies pain like a sensitized nerve, and the two overlap in treatment—anti-CGRP antibodies, sodium-channel blockers, and tricyclics help both."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Migraine and generalized anxiety are bidirectionally linked: anxiety is a leading migraine comorbidity, each worsens the other, and shared serotonergic and stress-axis biology underlies the overlap—so screening for and treating anxiety improves migraine outcomes."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia are implicated in migraine through neuroinflammation: cortical spreading depression—the wave behind aura—activates microglia that release mediators sensitizing trigeminal pain pathways, so glial neuroinflammation is an emerging target in chronic migraine."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Migraine and major depression are bidirectionally linked: each roughly doubles the other's risk, sharing serotonergic dysfunction and genetics, so depression worsens migraine frequency while chronic migraine drives mood decline—and drugs like amitriptyline treat both."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium deficiency is implicated in migraine: low brain magnesium lowers the threshold for cortical spreading depression and NMDA-receptor excitability, which is why magnesium supplementation is evidence-based prophylaxis, especially for aura-predominant migraine."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate drives the migraine aura: cortical spreading depression—the slow depolarization wave underlying aura—is fueled by massive glutamate release and NMDA-receptor activation, linking the excitatory transmitter to the sensory disturbances that precede the headache."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine shapes migraine's premonitory and nausea symptoms: dopaminergic activation underlies the yawning, mood change and nausea that precede the headache, and dopamine antagonists (e.g. metoclopramide, prochlorperazine) are effective acute migraine treatments."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium channels link genetics to migraine: mutations in the CACNA1A calcium-channel gene cause familial hemiplegic migraine, and altered neuronal calcium handling helps drive the cortical spreading depression that underlies aura."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Migraine is a primary disorder of the nervous system, not just a vascular headache: it is a brain-network disease of sensory processing in which the trigeminovascular system, brainstem and cortex misfire—reframing it from blood vessels to neural circuits."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Migraine often centers on the eye: visual aura (shimmering zigzags) signals the cortical spreading depression that precedes the headache, and severe photophobia and rare retinal migraine make the visual system both an early warning and a target of attacks."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Migraine is deeply tied to the gut: nausea and vomiting are core symptoms, gastric emptying slows during attacks (impairing oral drugs), and childhood cyclic vomiting and abdominal migraine are gut-centered variants of the same disorder."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Migraine reflects an excitable, under-inhibited brain: weak GABA-mediated inhibition lowers the threshold for cortical spreading depression, which is why GABA-enhancing drugs like topiramate and valproate are effective migraine preventives."
---

# Migraine

## Overview

**Migraine** is the **second leading cause of disability worldwide** (after low back pain) and the most disabling neurological disorder by years lived with disability [^gbd-2016-migraine-burden]. It affects approximately **1.1 billion people** globally — 12% of adults in high-income countries — with a striking 3:1 female predominance, peak incidence between ages 25–55, and substantial economic burden (~$36 billion/year in the US alone from lost productivity and treatment costs.

Migraine is a **neurovascular disorder** — a term that replaced both the historical "vascular theory" (excess dilation of intracranial vessels) and the competing "neurological theory" (cortical spreading depression), because the pathophysiology integrates both in a cascade:

1. **Prodrome** (hours to days before pain): hypothalamic activation → yawning, food craving, mood changes, neck stiffness
2. **Aura** (20–30% of migraineurs): cortical spreading depression (CSD) → visual scotoma, spreading tingling, language disturbance (each symptom 5–60 min, fully reversible)
3. **Headache** (4–72 hours): trigeminovascular CGRP release → dural neurogenic inflammation → unilateral pulsating pain, nausea, photophobia, phonophobia
4. **Postdrome** (hours to days): fatigue, cognitive slowing, mood changes — "migraine hangover"

## Structure

### Clinical criteria (ICHD-3)

**Migraine without aura (MO)** — ≥5 attacks fulfilling:
- Duration 4–72 hours
- ≥2 of: **unilateral** location, **pulsating** quality, **moderate/severe** intensity, aggravated by routine physical activity
- ≥1 of: nausea and/or vomiting; photophobia AND phonophobia

**Migraine with aura (MA)** — ≥2 attacks with ≥1 fully reversible aura symptom (visual, sensory, motor, language, brainstem, retinal) that:
- Spreads gradually over ≥5 minutes
- Each symptom lasts 5–60 minutes
- ≥1 migraine symptom follows or accompanies aura within 60 minutes

**Subtypes:**

| Subtype | Key features | Genetics |
|:---|:---|:---|
| **Chronic migraine** | ≥15 headache days/month, ≥8 migraine days/month, for >3 months | — |
| **Hemiplegic migraine (FHM)** | Motor aura (hemiplegia); can mimic stroke | CACNA1A (FHM1), ATP1A2 (FHM2), SCN1A (FHM3) |
| **Migraine with brainstem aura** | Vertigo, diplopia, dysarthria; brainstem aura symptoms | — |
| **Menstrual migraine** | Attacks 2 days before to 3 days after menstruation; estrogen withdrawal trigger | — |
| **Medication overuse headache (MOH)** | ≥15 headache days/month + regular overuse of acute drugs | — |

### Neurobiology of the fear circuit

**Cortical spreading depression (CSD):**
- Discovered by Leão in 1944; propagates at 3–5 mm/min across occipital cortex
- A self-sustaining wave of near-complete neuronal and glial depolarization followed by prolonged suppression
- Ion fluxes: massive K⁺ efflux, Na⁺/Ca²⁺ influx, glutamate and H⁺ release into extracellular space → neighbor cell depolarization
- Generates visual aura (positive symptoms: sparkles → negative: scotoma); occipital cortex most susceptible due to high metabolic demand

**Trigeminovascular system:**
- Trigeminal ganglion (TG) — the pain-sensing structure; V1/ophthalmic division C-fibers densely innervate dura and pia mater
- CGRP and substance P stored in TG C-fiber terminals; released by CSD-driven activation and directly by triggers (stress, caffeine withdrawal)
- Trigeminal nucleus caudalis (TNC) at C1–C2 cervical cord: first central relay for migraine pain; convergence with neck afferents explains referred neck pain

**Descending pain modulation:**
- Periaqueductal gray (PAG) and rostral ventromedial medulla (RVM) provide endogenous opioid/serotonin suppression of TNC
- PET studies (Weiller 1995) identified a **brainstem migraine generator** in dorsal raphe and LC that remains active during migraine even after triptan-induced headache relief — explaining triptan's inability to prevent migraine recurrence and the persistent neurobiological state

**Hypothalamus:**
- Activated during prodrome before headache onset; functional MRI shows posterior hypothalamus activation 24–48h before migraine
- Explains premonitory symptoms (yawning, fatigue, food craving, mood changes) that allow many migraineurs to predict attacks

## Function

### Sensitization cascade

A key pathophysiological concept in migraine is the progression from **peripheral sensitization** to **central sensitization**:

1. **Peripheral sensitization** — TG neurons sensitized by CGRP, bradykinin, prostaglandins → threshold for C-fiber activation lowered → pulsatile pain (intracranial pulsations that normally go unnoticed become painful)

2. **Central sensitization** — Sustained TNC activation → NMDA receptor wind-up → TNC neurons develop spontaneous activity and expanded receptive fields → **cutaneous allodynia** (scalp/face sensitive to light touch, hair brushing becomes painful in ~70% of migraine sufferers during attacks)

3. **Higher-order central sensitization** — Thalamic and cortical sensitization in prolonged attacks → allodynia spreads beyond face/scalp to limbs; triptans lose efficacy after central sensitization is established

**Clinical implication:** Early acute treatment (within 30 minutes of onset, before central sensitization develops) substantially improves triptan efficacy — supporting the "treat early" strategy.

### Triggers and threshold model

Migraine attacks are not random but reflect a **biological threshold** model: migraine occurs when cumulative sensitizing factors exceed the threshold for trigeminovascular activation:

| Category | Examples |
|:---|:---|
| **Hormonal** | Estrogen withdrawal (perimenstrual); oral contraceptive fluctuation |
| **Sleep** | Sleep deprivation OR excess sleep (weekend migraine) |
| **Dietary** | Alcohol (esp. red wine — histamine/tyramine); fasting; caffeine withdrawal |
| **Environmental** | Bright/flickering light; strong odors; weather/barometric pressure change |
| **Psychological** | Stress; post-stress "letdown migraine" (weekend migraine) |
| **Sensory** | Loud noise; strong perfume; visual motion |

## Pathology

### Risk factors and transformation to chronic migraine

Episodic migraine (EM, <15 headache days/month) transforms to **chronic migraine** (CM, ≥15 days/month) in ~3% of EM patients per year. Risk factors for chronification:
- Medication overuse (analgesics, triptans >10 days/month; opioids >8 days/month) — MOH dramatically increases headache frequency
- Obesity (BMI >30 — triples CM risk; adipokines sensitize trigeminovascular system)
- Sleep disorders (sleep apnea, insomnia)
- Comorbid depression or anxiety (bidirectional relationship; shared serotonin and BDNF pathways)
- Head trauma, stressful life events, low socioeconomic status

### Comorbidities

- **Depression and anxiety:** 2–4× elevated in migraineurs; shared genetic and serotonergic mechanisms
- **Stroke:** Migraine with aura (MA) associated with 2× elevated ischemic stroke risk, especially in women who smoke and use combined oral contraceptives
- **Patent foramen ovale (PFO):** Overrepresented in MA patients; PFO closure trials show modest migraine improvement
- **Epilepsy:** 2-3× elevated in migraineurs; shared cortical hyperexcitability (SCN1A mutations cause both FHM3 and Dravet syndrome)
- **PTSD and trauma:** Shared stress-sensitization biology; PTSD increases migraine chronification risk

### Treatment

**Acute therapy (goal: pain-free at 2 hours, sustained 24-hour relief):**

| Drug | Mechanism | Indication | Key caveat |
|:---|:---|:---|:---|
| Sumatriptan, rizatriptan, eletriptan | 5-HT1B/D agonist: dural vasoconstriction + ↓CGRP release | Moderate–severe acute migraine | Contraindicated in CAD, stroke, uncontrolled HTN |
| Lasmiditan | 5-HT1F agonist: TNC inhibition without vasoconstriction | Acute migraine with cardiovascular risk | CNS sedation/dizziness; driving restriction 8h |
| Rimegepant (Nurtec ODT) | CGRP receptor antagonist | Acute + prevention (same drug) | No cardiovascular contraindication |
| Ubrogepant (Ubrelvy) | CGRP receptor antagonist | Acute migraine | Avoid with strong CYP3A4 inhibitors |
| NSAIDs (naproxen, ibuprofen) | COX inhibition; prostaglandin reduction | Mild–moderate migraine | GI risk with frequent use |
| Prochlorperazine / metoclopramide | D2 antagonist; antiemetic | Acute + antiemetic; ED setting | Akathisia; metoclopramide useful for gastric stasis |

**Prevention (indicated for ≥4 migraine days/month or severe disability):**

| Drug | Mechanism | Efficacy | Notes |
|:---|:---|:---|:---|
| Erenumab (Aimovig) | Anti-CGRP receptor mAb (CLR/RAMP1) | ~40% ≥50% responders | Monthly SC; FDA-approved 2018 |
| Fremanezumab (Ajovy) | Anti-CGRP ligand mAb | ~40–50% responders | Monthly or quarterly SC |
| Galcanezumab (Emgality) | Anti-CGRP ligand mAb | ~40–50% responders | Monthly SC; also cluster headache |
| Eptinezumab (Vyepti) | Anti-CGRP ligand mAb (IV) | Rapid onset; ~40% responders | IV infusion quarterly; fastest onset |
| Atogepant (Qulipta) | Oral CGRP receptor antagonist | ~60% responders (≥50% reduction) | Daily oral; well-tolerated |
| Rimegepant (Nurtec, EOD) | Oral CGRP receptor antagonist | Prevention + acute | Every-other-day dosing |
| OnabotulinumtoxinA (Botox) | Blocks CGRP/SP release from TG terminals | ~50% responders (CM only) | 31-site injection every 12 weeks; FDA CM only |
| Topiramate | Na⁺/Ca²⁺ channel block + GABA-A enhancement | ~40–50% responders | Cognitive impairment ("dopamax"); teratogenic |
| Valproate | Na⁺ channel block + GABA enhancement | ~40% responders | Highly teratogenic; avoid women of childbearing age |
| Propranolol, metoprolol | β-blockade; ↓CSD susceptibility | ~40% responders | Useful if comorbid HTN/anxiety |
| Amitriptyline | TCA; serotonin/NE reuptake block | Useful in comorbid depression | Sedation; dry mouth; cardiac monitoring in elderly |

**The anti-CGRP revolution:** Before 2018, all migraine preventives were repurposed from other conditions (epilepsy, hypertension, depression) and had modest efficacy and poor tolerability. Anti-CGRP mAbs were the **first migraine-specific preventive drugs** — designed mechanistically for the disease — achieving ~40% responder rates with excellent safety profiles [^dodick-2018-erenumab-arise].

## Connections

- `connects-to` → **[CGRP](../../../03-molecular/cgrp/README.md)** — CGRP released from trigeminal C-fibers drives dural vasodilation and neurogenic inflammation; plasma CGRP rises during migraine and normalizes after successful triptan treatment; anti-CGRP mAbs and gepants block CGRP signaling for prevention and acute treatment.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — triptans (5-HT1B/D agonists) are the mainstay acute migraine therapy, constricting dural vessels and inhibiting trigeminal CGRP release; lasmiditan (5-HT1F) avoids vasoconstriction; low interictal serotonin may prime trigeminovascular sensitization.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — migraine involves cortical spreading depression (CSD) as the aura generator in occipital cortex; hypothalamus drives prodromal symptoms; pain localizes to trigeminal nucleus caudalis (TNC) and thalamus; PET identifies a brainstem migraine generator in dorsal raphe and PAG.
- `connects-to` → **[Stroke](../stroke/README.md)** — migraine with aura (MA) confers 2× ischemic stroke risk; CSD-triggered spreading oligemia → ischemic cascade in vulnerable cortex; PFO prevalence higher in MA; oral contraceptives + MA + smoking multiplies stroke risk; CADASIL (NOTCH3) presents with MA + lacunar strokes.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — NO triggers cortical spreading depression (CSD); nitroglycerin (GTN) reliably provokes migraine attacks — the GTN model; NO-driven vasodilation sensitizes trigeminovascular nociceptors; triptans reduce NO-mediated dilation; iNOS upregulated in CSD-affected cortex.
- `connects-to` → **[SCN1A](../../03-molecular/scn1a/README.md)** — SCN1A (Nav1.1) gain-of-function → FHM3 (familial hemiplegic migraine type 3); loss-of-function → Dravet syndrome (epilepsy); both share cortical hyperexcitability; FHM3 SCN1A variants increase persistent Na⁺ current → lower CSD threshold.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Migraine and epilepsy are comorbid disorders of cortical hyperexcitability — migraineurs have 2-3× the epilepsy risk — sharing mechanisms like cortical spreading depression and SCN1A channel mutations (FHM3 vs Dravet); valproate and topiramate prevent both.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen shapes migraine: the 3:1 female predominance and menstrual migraine reflect attacks triggered by the perimenstrual estrogen drop, which lowers the trigeminovascular threshold; this is also why oral contraceptives plus migraine-with-aura sharply raise stroke risk.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Cortical spreading depression — the wave behind migraine aura — is not purely neuronal: astrocytes propagate it through calcium waves and gap junctions and shape it by buffering the massive extracellular potassium and glutamate the depolarizing front releases.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Migraine and fibromyalgia frequently co-occur and share central sensitization: both feature amplified pain processing, failed descending inhibition and CGRP/serotonin involvement, so the comorbidity worsens disability, and SNRIs and anti-CGRP antibodies are studied across both.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Migraine and insomnia are bidirectionally linked through shared hypothalamic and brainstem circuitry: poor sleep is a common migraine trigger while migraine disrupts sleep, both involve orexin and serotonergic systems, and treating insomnia (CBT-I) reduces headache frequency.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Migraine aura is a neuronal event: cortical spreading depression—a slow wave of neuronal and glial depolarization then suppression—sweeps the cortex producing visual aura and activating trigeminal pain pathways; neuronal hyperexcitability underlies susceptibility.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Migraine and neuropathic pain share central sensitization and CGRP signaling: trigeminovascular activation amplifies pain like a sensitized nerve, and the two overlap in treatment—anti-CGRP antibodies, sodium-channel blockers, and tricyclics help both.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Migraine and generalized anxiety are bidirectionally linked: anxiety is a leading migraine comorbidity, each worsens the other, and shared serotonergic and stress-axis biology underlies the overlap—so screening for and treating anxiety improves migraine outcomes.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia are implicated in migraine through neuroinflammation: cortical spreading depression—the wave behind aura—activates microglia that release mediators sensitizing trigeminal pain pathways, so glial neuroinflammation is an emerging target in chronic migraine.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Migraine and major depression are bidirectionally linked: each roughly doubles the other's risk, sharing serotonergic dysfunction and genetics, so depression worsens migraine frequency while chronic migraine drives mood decline—and drugs like amitriptyline treat both.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium deficiency is implicated in migraine: low brain magnesium lowers the threshold for cortical spreading depression and NMDA-receptor excitability, which is why magnesium supplementation is evidence-based prophylaxis, especially for aura-predominant migraine.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate drives the migraine aura: cortical spreading depression—the slow depolarization wave underlying aura—is fueled by massive glutamate release and NMDA-receptor activation, linking the excitatory transmitter to the sensory disturbances that precede the headache.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine shapes migraine's premonitory and nausea symptoms: dopaminergic activation underlies the yawning, mood change and nausea that precede the headache, and dopamine antagonists (e.g. metoclopramide, prochlorperazine) are effective acute migraine treatments.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium channels link genetics to migraine: mutations in the CACNA1A calcium-channel gene cause familial hemiplegic migraine, and altered neuronal calcium handling helps drive the cortical spreading depression that underlies aura.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Migraine is a primary disorder of the nervous system, not just a vascular headache: it is a brain-network disease of sensory processing in which the trigeminovascular system, brainstem and cortex misfire—reframing it from blood vessels to neural circuits.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Migraine often centers on the eye: visual aura (shimmering zigzags) signals the cortical spreading depression that precedes the headache, and severe photophobia and rare retinal migraine make the visual system both an early warning and a target of attacks.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Migraine is deeply tied to the gut: nausea and vomiting are core symptoms, gastric emptying slows during attacks (impairing oral drugs), and childhood cyclic vomiting and abdominal migraine are gut-centered variants of the same disorder.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Migraine reflects an excitable, under-inhibited brain: weak GABA-mediated inhibition lowers the threshold for cortical spreading depression, which is why GABA-enhancing drugs like topiramate and valproate are effective migraine preventives.

[^gbd-2016-migraine-burden]: GBD 2016 Headache Collaborators. Global, regional, and national burden of migraine and tension-type headache, 1990-2016. *Lancet Neurol.* 2018;17(11):954-976. [doi:10.1016/S1474-4422(18)30322-3](https://doi.org/10.1016/S1474-4422(18)30322-3) · [PubMed 30353868](https://pubmed.ncbi.nlm.nih.gov/30353868/)
[^goadsby-2002-migraine-review]: Goadsby PJ, Lipton RB, Ferrari MD. Migraine — current understanding and treatment. *N Engl J Med.* 2002;346(4):257-270. [doi:10.1056/NEJMra010917](https://doi.org/10.1056/NEJMra010917) · [PubMed 11807151](https://pubmed.ncbi.nlm.nih.gov/11807151/)
[^dodick-2018-erenumab-arise]: Dodick DW, Ashina M, Brandes JL, et al. ARISE: A Phase 3 randomized trial of erenumab for episodic migraine. *Cephalalgia.* 2018;38(6):1026-1037. [doi:10.1177/0333102418759786](https://doi.org/10.1177/0333102418759786) · [PubMed 29471679](https://pubmed.ncbi.nlm.nih.gov/29471679/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
